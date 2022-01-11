from __future__ import annotations

from abc import ABC
from typing import Callable, Generic, List, Protocol, Tuple, TypeVar, Union, overload

from System import Action, Array, AsyncCallback, Boolean, Byte, Char, DateTime, DateTimeOffset, Decimal, Double, Enum, EventArgs, Exception, Func, Guid, IAsyncResult, ICloneable, IDisposable, Int16, Int32, Int64, IntPtr, MulticastDelegate, Object, SByte, Single, String, SystemException, TimeSpan, Tuple, Type, UInt16, UInt32, UInt64, Uri, ValueType, Void
from System.Collections import ICollection, IEnumerable, IEnumerator
from System.Collections.Generic import IDictionary, IEnumerable, IEqualityComparer
from System.ComponentModel import CategoryAttribute, DescriptionAttribute
from System.Diagnostics import BooleanSwitch, TraceSwitch
from System.IO import MemoryStream, SeekOrigin, Stream, TextReader, TextWriter
from System.Net import ICredentials, IWebProxy
from System.Net.Cache import RequestCachePolicy
from System.Resources import ResourceManager
from System.Runtime.InteropServices import _Attribute, _Exception
from System.Runtime.Serialization import ISerializable, SerializationInfo, StreamingContext
from System.Security import PermissionSet
from System.Security.Policy import Evidence
from System.Text import Decoder, Encoder, EncoderFallback, EncoderFallbackBuffer, Encoding, StringBuilder
from System.Threading.Tasks import Task
from System.Xml.Schema import IXmlSchemaInfo, ValidationEventHandler, XmlSchemaAttribute, XmlSchemaCollection, XmlSchemaElement, XmlSchemaSet, XmlSchemaSimpleType, XmlSchemaType, XmlSchemaValidationFlags, XmlSchemaValidity, XmlSeverityType
from System.Xml.XPath import IXPathNavigable, XPathNamespaceScope, XPathNavigator, XPathNodeIterator, XPathNodeType

# ---------- Types ---------- #

T = TypeVar('T')

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
ByteType = Union[int, Byte]
CharType = Union[str, Char]
DecimalType = Union[float, Decimal]
DoubleType = Union[float, Double]
FloatType = Union[float, Single]
IntType = Union[int, Int32]
LongType = Union[int, Int64]
NIntType = Union[int, IntPtr]
ObjectType = Object
SByteType = Union[int, SByte]
ShortType = Union[int, Int16]
StringType = Union[str, String]
TypeType = Union[type, Type]
UIntType = Union[int, UInt32]
ULongType = Union[int, UInt64]
UShortType = Union[int, UInt16]
VoidType = Union[None, Void]


class EventType(Generic[T]):
    def __iadd__(self, other: T): ...
    
    def __isub__(self, other: T): ...



# ---------- Classes ---------- #

class AsyncHelper(ABC, ObjectType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def DoneTask() -> Task: ...
    
    @staticmethod
    @property
    def DoneTaskFalse() -> Task[BooleanType]: ...
    
    @staticmethod
    @property
    def DoneTaskTrue() -> Task[BooleanType]: ...
    
    @staticmethod
    @property
    def DoneTaskZero() -> Task[IntType]: ...
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def CallBoolTaskFuncWhenFinish(task: Task, func: Func[Task[BooleanType]]) -> Task[BooleanType]: ...
    
    @staticmethod
    def CallTaskFuncWhenFinish(task: Task, func: Func[Task]) -> Task: ...
    
    @staticmethod
    def CallVoidFuncWhenFinish(task: Task, func: Action) -> Task: ...
    
    @staticmethod
    def ContinueBoolTaskFuncWhenFalse(task: Task[BooleanType], func: Func[Task[BooleanType]]) -> Task[BooleanType]: ...
    
    @staticmethod
    def IsSuccess(task: Task) -> BooleanType: ...
    
    @staticmethod
    def ReturnTaskBoolWhenFinish(task: Task, ret: BooleanType) -> Task[BooleanType]: ...
    
    @staticmethod
    def _ReturnTaskBoolWhenFinish(task: Task, ret: BooleanType) -> Task[BooleanType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AsyncHelper(ABC, ObjectType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def DoneTask() -> Task: ...
    
    @staticmethod
    @property
    def DoneTaskFalse() -> Task[BooleanType]: ...
    
    @staticmethod
    @property
    def DoneTaskTrue() -> Task[BooleanType]: ...
    
    @staticmethod
    @property
    def DoneTaskZero() -> Task[IntType]: ...
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def CallBoolTaskFuncWhenFinish(task: Task, func: Func[Task[BooleanType]]) -> Task[BooleanType]: ...
    
    @staticmethod
    def CallTaskFuncWhenFinish(task: Task, func: Func[Task]) -> Task: ...
    
    @staticmethod
    def CallVoidFuncWhenFinish(task: Task, func: Action) -> Task: ...
    
    @staticmethod
    def ContinueBoolTaskFuncWhenFalse(task: Task[BooleanType], func: Func[Task[BooleanType]]) -> Task[BooleanType]: ...
    
    @staticmethod
    def IsSuccess(task: Task) -> BooleanType: ...
    
    @staticmethod
    def ReturnTaskBoolWhenFinish(task: Task, ret: BooleanType) -> Task[BooleanType]: ...
    
    @staticmethod
    def _ReturnTaskBoolWhenFinish(task: Task, ret: BooleanType) -> Task[BooleanType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AttributePSVIInfo(ObjectType):
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


class AttributePSVIInfo(ObjectType):
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


class Base64Decoder(IncrementalReadDecoder):
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


class Base64Decoder(IncrementalReadDecoder):
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


class Base64Encoder(ABC, ObjectType):
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


class Base64Encoder(ABC, ObjectType):
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


class BinHexDecoder(IncrementalReadDecoder):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def Decode(chars: ArrayType[CharType], allowOddChars: BooleanType) -> ArrayType[ByteType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class BinHexDecoder(IncrementalReadDecoder):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def Decode(chars: ArrayType[CharType], allowOddChars: BooleanType) -> ArrayType[ByteType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class BinHexEncoder(ABC, ObjectType):
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


class BinHexEncoder(ABC, ObjectType):
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


class BinXmlDateTime(ABC, ObjectType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def SQLTicksPerHour() -> IntType: ...
    
    @staticmethod
    @property
    def SQLTicksPerMinute() -> IntType: ...
    
    @staticmethod
    @property
    def SQLTicksPerSecond() -> IntType: ...
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def SqlDateTimeToDateTime(dateticks: IntType, timeticks: UIntType) -> DateTime: ...
    
    @staticmethod
    def SqlDateTimeToString(dateticks: IntType, timeticks: UIntType) -> StringType: ...
    
    @staticmethod
    def SqlSmallDateTimeToDateTime(dateticks: ShortType, timeticks: UShortType) -> DateTime: ...
    
    @staticmethod
    def SqlSmallDateTimeToString(dateticks: ShortType, timeticks: UShortType) -> StringType: ...
    
    @staticmethod
    def XsdDateTimeToDateTime(val: LongType) -> DateTime: ...
    
    @staticmethod
    def XsdDateTimeToString(val: LongType) -> StringType: ...
    
    @staticmethod
    def XsdDateToDateTime(val: LongType) -> DateTime: ...
    
    @staticmethod
    def XsdDateToString(val: LongType) -> StringType: ...
    
    @staticmethod
    def XsdKatmaiDateOffsetToDateTime(data: ArrayType[ByteType], offset: IntType) -> DateTime: ...
    
    @staticmethod
    def XsdKatmaiDateOffsetToDateTimeOffset(data: ArrayType[ByteType], offset: IntType) -> DateTimeOffset: ...
    
    @staticmethod
    def XsdKatmaiDateOffsetToString(data: ArrayType[ByteType], offset: IntType) -> StringType: ...
    
    @staticmethod
    def XsdKatmaiDateTimeOffsetToDateTime(data: ArrayType[ByteType], offset: IntType) -> DateTime: ...
    
    @staticmethod
    def XsdKatmaiDateTimeOffsetToDateTimeOffset(data: ArrayType[ByteType], offset: IntType) -> DateTimeOffset: ...
    
    @staticmethod
    def XsdKatmaiDateTimeOffsetToString(data: ArrayType[ByteType], offset: IntType) -> StringType: ...
    
    @staticmethod
    def XsdKatmaiDateTimeToDateTime(data: ArrayType[ByteType], offset: IntType) -> DateTime: ...
    
    @staticmethod
    def XsdKatmaiDateTimeToDateTimeOffset(data: ArrayType[ByteType], offset: IntType) -> DateTimeOffset: ...
    
    @staticmethod
    def XsdKatmaiDateTimeToString(data: ArrayType[ByteType], offset: IntType) -> StringType: ...
    
    @staticmethod
    def XsdKatmaiDateToDateTime(data: ArrayType[ByteType], offset: IntType) -> DateTime: ...
    
    @staticmethod
    def XsdKatmaiDateToDateTimeOffset(data: ArrayType[ByteType], offset: IntType) -> DateTimeOffset: ...
    
    @staticmethod
    def XsdKatmaiDateToString(data: ArrayType[ByteType], offset: IntType) -> StringType: ...
    
    @staticmethod
    def XsdKatmaiTimeOffsetToDateTime(data: ArrayType[ByteType], offset: IntType) -> DateTime: ...
    
    @staticmethod
    def XsdKatmaiTimeOffsetToDateTimeOffset(data: ArrayType[ByteType], offset: IntType) -> DateTimeOffset: ...
    
    @staticmethod
    def XsdKatmaiTimeOffsetToString(data: ArrayType[ByteType], offset: IntType) -> StringType: ...
    
    @staticmethod
    def XsdKatmaiTimeToDateTime(data: ArrayType[ByteType], offset: IntType) -> DateTime: ...
    
    @staticmethod
    def XsdKatmaiTimeToDateTimeOffset(data: ArrayType[ByteType], offset: IntType) -> DateTimeOffset: ...
    
    @staticmethod
    def XsdKatmaiTimeToString(data: ArrayType[ByteType], offset: IntType) -> StringType: ...
    
    @staticmethod
    def XsdTimeToDateTime(val: LongType) -> DateTime: ...
    
    @staticmethod
    def XsdTimeToString(val: LongType) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class BinXmlDateTime(ABC, ObjectType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def SQLTicksPerHour() -> IntType: ...
    
    @staticmethod
    @property
    def SQLTicksPerMinute() -> IntType: ...
    
    @staticmethod
    @property
    def SQLTicksPerSecond() -> IntType: ...
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def SqlDateTimeToDateTime(dateticks: IntType, timeticks: UIntType) -> DateTime: ...
    
    @staticmethod
    def SqlDateTimeToString(dateticks: IntType, timeticks: UIntType) -> StringType: ...
    
    @staticmethod
    def SqlSmallDateTimeToDateTime(dateticks: ShortType, timeticks: UShortType) -> DateTime: ...
    
    @staticmethod
    def SqlSmallDateTimeToString(dateticks: ShortType, timeticks: UShortType) -> StringType: ...
    
    @staticmethod
    def XsdDateTimeToDateTime(val: LongType) -> DateTime: ...
    
    @staticmethod
    def XsdDateTimeToString(val: LongType) -> StringType: ...
    
    @staticmethod
    def XsdDateToDateTime(val: LongType) -> DateTime: ...
    
    @staticmethod
    def XsdDateToString(val: LongType) -> StringType: ...
    
    @staticmethod
    def XsdKatmaiDateOffsetToDateTime(data: ArrayType[ByteType], offset: IntType) -> DateTime: ...
    
    @staticmethod
    def XsdKatmaiDateOffsetToDateTimeOffset(data: ArrayType[ByteType], offset: IntType) -> DateTimeOffset: ...
    
    @staticmethod
    def XsdKatmaiDateOffsetToString(data: ArrayType[ByteType], offset: IntType) -> StringType: ...
    
    @staticmethod
    def XsdKatmaiDateTimeOffsetToDateTime(data: ArrayType[ByteType], offset: IntType) -> DateTime: ...
    
    @staticmethod
    def XsdKatmaiDateTimeOffsetToDateTimeOffset(data: ArrayType[ByteType], offset: IntType) -> DateTimeOffset: ...
    
    @staticmethod
    def XsdKatmaiDateTimeOffsetToString(data: ArrayType[ByteType], offset: IntType) -> StringType: ...
    
    @staticmethod
    def XsdKatmaiDateTimeToDateTime(data: ArrayType[ByteType], offset: IntType) -> DateTime: ...
    
    @staticmethod
    def XsdKatmaiDateTimeToDateTimeOffset(data: ArrayType[ByteType], offset: IntType) -> DateTimeOffset: ...
    
    @staticmethod
    def XsdKatmaiDateTimeToString(data: ArrayType[ByteType], offset: IntType) -> StringType: ...
    
    @staticmethod
    def XsdKatmaiDateToDateTime(data: ArrayType[ByteType], offset: IntType) -> DateTime: ...
    
    @staticmethod
    def XsdKatmaiDateToDateTimeOffset(data: ArrayType[ByteType], offset: IntType) -> DateTimeOffset: ...
    
    @staticmethod
    def XsdKatmaiDateToString(data: ArrayType[ByteType], offset: IntType) -> StringType: ...
    
    @staticmethod
    def XsdKatmaiTimeOffsetToDateTime(data: ArrayType[ByteType], offset: IntType) -> DateTime: ...
    
    @staticmethod
    def XsdKatmaiTimeOffsetToDateTimeOffset(data: ArrayType[ByteType], offset: IntType) -> DateTimeOffset: ...
    
    @staticmethod
    def XsdKatmaiTimeOffsetToString(data: ArrayType[ByteType], offset: IntType) -> StringType: ...
    
    @staticmethod
    def XsdKatmaiTimeToDateTime(data: ArrayType[ByteType], offset: IntType) -> DateTime: ...
    
    @staticmethod
    def XsdKatmaiTimeToDateTimeOffset(data: ArrayType[ByteType], offset: IntType) -> DateTimeOffset: ...
    
    @staticmethod
    def XsdKatmaiTimeToString(data: ArrayType[ByteType], offset: IntType) -> StringType: ...
    
    @staticmethod
    def XsdTimeToDateTime(val: LongType) -> DateTime: ...
    
    @staticmethod
    def XsdTimeToString(val: LongType) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class BinaryCompatibility(ABC, ObjectType):
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


class BinaryCompatibility(ABC, ObjectType):
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


class BitStack(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def IsEmpty(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def PeekBit(self) -> BooleanType: ...
    
    def PopBit(self) -> BooleanType: ...
    
    def PushBit(self, bit: BooleanType) -> VoidType: ...
    
    def get_IsEmpty(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class BitStack(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def IsEmpty(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def PeekBit(self) -> BooleanType: ...
    
    def PopBit(self) -> BooleanType: ...
    
    def PushBit(self, bit: BooleanType) -> VoidType: ...
    
    def get_IsEmpty(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Bits(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def ClearLeast(num: UIntType) -> UIntType: ...
    
    @staticmethod
    def Count(num: UIntType) -> IntType: ...
    
    @staticmethod
    def ExactlyOne(num: UIntType) -> BooleanType: ...
    
    @staticmethod
    def LeastPosition(num: UIntType) -> IntType: ...
    
    @staticmethod
    def MoreThanOne(num: UIntType) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Bits(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def ClearLeast(num: UIntType) -> UIntType: ...
    
    @staticmethod
    def Count(num: UIntType) -> IntType: ...
    
    @staticmethod
    def ExactlyOne(num: UIntType) -> BooleanType: ...
    
    @staticmethod
    def LeastPosition(num: UIntType) -> IntType: ...
    
    @staticmethod
    def MoreThanOne(num: UIntType) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ByteStack(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, growthRate: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Length(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def Peek(self) -> ByteType: ...
    
    def Pop(self) -> ByteType: ...
    
    def Push(self, data: ByteType) -> VoidType: ...
    
    def get_Length(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ByteStack(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, growthRate: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Length(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def Peek(self) -> ByteType: ...
    
    def Pop(self) -> ByteType: ...
    
    def Push(self, data: ByteType) -> VoidType: ...
    
    def get_Length(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CachingEventHandler(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, cachingReader: XsdCachingReader, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, cachingReader: XsdCachingReader) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CachingEventHandler(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, cachingReader: XsdCachingReader, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, cachingReader: XsdCachingReader) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CharEntityEncoderFallback(EncoderFallback):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def MaxCharCount(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def CreateFallbackBuffer(self) -> EncoderFallbackBuffer: ...
    
    def get_MaxCharCount(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CharEntityEncoderFallback(EncoderFallback):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def MaxCharCount(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def CreateFallbackBuffer(self) -> EncoderFallbackBuffer: ...
    
    def get_MaxCharCount(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CharEntityEncoderFallbackBuffer(EncoderFallbackBuffer):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Remaining(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Fallback(self, charUnknown: CharType, index: IntType) -> BooleanType: ...
    
    @overload
    def Fallback(self, charUnknownHigh: CharType, charUnknownLow: CharType, index: IntType) -> BooleanType: ...
    
    def GetNextChar(self) -> CharType: ...
    
    def MovePrevious(self) -> BooleanType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Remaining(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CharEntityEncoderFallbackBuffer(EncoderFallbackBuffer):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Remaining(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Fallback(self, charUnknown: CharType, index: IntType) -> BooleanType: ...
    
    @overload
    def Fallback(self, charUnknownHigh: CharType, charUnknownLow: CharType, index: IntType) -> BooleanType: ...
    
    def GetNextChar(self) -> CharType: ...
    
    def MovePrevious(self) -> BooleanType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Remaining(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DiagnosticsSwitches(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def KeepTempFiles() -> BooleanSwitch: ...
    
    @staticmethod
    @property
    def NonRecursiveTypeLoading() -> BooleanSwitch: ...
    
    @staticmethod
    @property
    def PregenEventLog() -> BooleanSwitch: ...
    
    @staticmethod
    @property
    def XmlSchema() -> TraceSwitch: ...
    
    @staticmethod
    @property
    def XmlSchemaContentModel() -> BooleanSwitch: ...
    
    @staticmethod
    @property
    def XmlSerialization() -> TraceSwitch: ...
    
    @staticmethod
    @property
    def XslTypeInference() -> TraceSwitch: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def get_KeepTempFiles() -> BooleanSwitch: ...
    
    @staticmethod
    def get_NonRecursiveTypeLoading() -> BooleanSwitch: ...
    
    @staticmethod
    def get_PregenEventLog() -> BooleanSwitch: ...
    
    @staticmethod
    def get_XmlSchema() -> TraceSwitch: ...
    
    @staticmethod
    def get_XmlSchemaContentModel() -> BooleanSwitch: ...
    
    @staticmethod
    def get_XmlSerialization() -> TraceSwitch: ...
    
    @staticmethod
    def get_XslTypeInference() -> TraceSwitch: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DiagnosticsSwitches(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def KeepTempFiles() -> BooleanSwitch: ...
    
    @staticmethod
    @property
    def NonRecursiveTypeLoading() -> BooleanSwitch: ...
    
    @staticmethod
    @property
    def PregenEventLog() -> BooleanSwitch: ...
    
    @staticmethod
    @property
    def XmlSchema() -> TraceSwitch: ...
    
    @staticmethod
    @property
    def XmlSchemaContentModel() -> BooleanSwitch: ...
    
    @staticmethod
    @property
    def XmlSerialization() -> TraceSwitch: ...
    
    @staticmethod
    @property
    def XslTypeInference() -> TraceSwitch: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def get_KeepTempFiles() -> BooleanSwitch: ...
    
    @staticmethod
    def get_NonRecursiveTypeLoading() -> BooleanSwitch: ...
    
    @staticmethod
    def get_PregenEventLog() -> BooleanSwitch: ...
    
    @staticmethod
    def get_XmlSchema() -> TraceSwitch: ...
    
    @staticmethod
    def get_XmlSchemaContentModel() -> BooleanSwitch: ...
    
    @staticmethod
    def get_XmlSerialization() -> TraceSwitch: ...
    
    @staticmethod
    def get_XslTypeInference() -> TraceSwitch: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DocumentSchemaValidator(ObjectType, IXmlNamespaceResolver):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, ownerDocument: XmlDocument, schemas: XmlSchemaSet, eventHandler: ValidationEventHandler): ...
    
    # ---------- Properties ---------- #
    
    @property
    def PsviAugmentation(self) -> BooleanType: ...
    
    @PsviAugmentation.setter
    def PsviAugmentation(self, value: BooleanType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def GetNamespacesInScope(self, scope: XmlNamespaceScope) -> IDictionary[StringType, StringType]: ...
    
    def LookupNamespace(self, prefix: StringType) -> StringType: ...
    
    def LookupPrefix(self, namespaceName: StringType) -> StringType: ...
    
    def Validate(self, nodeToValidate: XmlNode) -> BooleanType: ...
    
    def get_PsviAugmentation(self) -> BooleanType: ...
    
    def set_PsviAugmentation(self, value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DocumentSchemaValidator(ObjectType, IXmlNamespaceResolver):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, ownerDocument: XmlDocument, schemas: XmlSchemaSet, eventHandler: ValidationEventHandler): ...
    
    # ---------- Properties ---------- #
    
    @property
    def PsviAugmentation(self) -> BooleanType: ...
    
    @PsviAugmentation.setter
    def PsviAugmentation(self, value: BooleanType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def GetNamespacesInScope(self, scope: XmlNamespaceScope) -> IDictionary[StringType, StringType]: ...
    
    def LookupNamespace(self, prefix: StringType) -> StringType: ...
    
    def LookupPrefix(self, namespaceName: StringType) -> StringType: ...
    
    def Validate(self, nodeToValidate: XmlNode) -> BooleanType: ...
    
    def get_PsviAugmentation(self) -> BooleanType: ...
    
    def set_PsviAugmentation(self, value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DocumentXPathNavigator(XPathNavigator, ICloneable, IXPathNavigable, IXmlNamespaceResolver, IHasXmlNode):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, document: XmlDocument, node: XmlNode): ...
    
    @overload
    def __init__(self, other: DocumentXPathNavigator): ...
    
    # ---------- Properties ---------- #
    
    @property
    def BaseURI(self) -> StringType: ...
    
    @property
    def CanEdit(self) -> BooleanType: ...
    
    @property
    def HasAttributes(self) -> BooleanType: ...
    
    @property
    def HasChildren(self) -> BooleanType: ...
    
    @property
    def IsEmptyElement(self) -> BooleanType: ...
    
    @property
    def LocalName(self) -> StringType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def NameTable(self) -> XmlNameTable: ...
    
    @property
    def NamespaceURI(self) -> StringType: ...
    
    @property
    def NodeType(self) -> XPathNodeType: ...
    
    @property
    def Prefix(self) -> StringType: ...
    
    @property
    def SchemaInfo(self) -> IXmlSchemaInfo: ...
    
    @property
    def UnderlyingObject(self) -> ObjectType: ...
    
    @property
    def Value(self) -> StringType: ...
    
    @property
    def XmlLang(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def AppendChild(self) -> XmlWriter: ...
    
    def CheckValidity(self, schemas: XmlSchemaSet, validationEventHandler: ValidationEventHandler) -> BooleanType: ...
    
    def Clone(self) -> XPathNavigator: ...
    
    def ComparePosition(self, other: XPathNavigator) -> XmlNodeOrder: ...
    
    def CreateAttributes(self) -> XmlWriter: ...
    
    def DeleteRange(self, lastSiblingToDelete: XPathNavigator) -> VoidType: ...
    
    def DeleteSelf(self) -> VoidType: ...
    
    def GetAttribute(self, localName: StringType, namespaceURI: StringType) -> StringType: ...
    
    def GetNamespace(self, name: StringType) -> StringType: ...
    
    @overload
    def InsertAfter(self) -> XmlWriter: ...
    
    @overload
    def InsertBefore(self) -> XmlWriter: ...
    
    def IsDescendant(self, other: XPathNavigator) -> BooleanType: ...
    
    def IsSamePosition(self, other: XPathNavigator) -> BooleanType: ...
    
    def LookupNamespace(self, prefix: StringType) -> StringType: ...
    
    def MoveTo(self, other: XPathNavigator) -> BooleanType: ...
    
    def MoveToAttribute(self, localName: StringType, namespaceURI: StringType) -> BooleanType: ...
    
    @overload
    def MoveToChild(self, localName: StringType, namespaceUri: StringType) -> BooleanType: ...
    
    @overload
    def MoveToChild(self, type: XPathNodeType) -> BooleanType: ...
    
    def MoveToFirst(self) -> BooleanType: ...
    
    def MoveToFirstAttribute(self) -> BooleanType: ...
    
    def MoveToFirstChild(self) -> BooleanType: ...
    
    @overload
    def MoveToFirstNamespace(self, scope: XPathNamespaceScope) -> BooleanType: ...
    
    @overload
    def MoveToFollowing(self, localName: StringType, namespaceUri: StringType, end: XPathNavigator) -> BooleanType: ...
    
    @overload
    def MoveToFollowing(self, type: XPathNodeType, end: XPathNavigator) -> BooleanType: ...
    
    def MoveToId(self, id: StringType) -> BooleanType: ...
    
    def MoveToNamespace(self, name: StringType) -> BooleanType: ...
    
    @overload
    def MoveToNext(self) -> BooleanType: ...
    
    @overload
    def MoveToNext(self, localName: StringType, namespaceUri: StringType) -> BooleanType: ...
    
    @overload
    def MoveToNext(self, type: XPathNodeType) -> BooleanType: ...
    
    def MoveToNextAttribute(self) -> BooleanType: ...
    
    @overload
    def MoveToNextNamespace(self, scope: XPathNamespaceScope) -> BooleanType: ...
    
    def MoveToParent(self) -> BooleanType: ...
    
    def MoveToPrevious(self) -> BooleanType: ...
    
    def MoveToRoot(self) -> VoidType: ...
    
    @overload
    def PrependChild(self) -> XmlWriter: ...
    
    def ReplaceRange(self, lastSiblingToReplace: XPathNavigator) -> XmlWriter: ...
    
    @overload
    def SelectDescendants(self, localName: StringType, namespaceURI: StringType, matchSelf: BooleanType) -> XPathNodeIterator: ...
    
    @overload
    def SelectDescendants(self, nt: XPathNodeType, includeSelf: BooleanType) -> XPathNodeIterator: ...
    
    def SetValue(self, value: StringType) -> VoidType: ...
    
    def get_BaseURI(self) -> StringType: ...
    
    def get_CanEdit(self) -> BooleanType: ...
    
    def get_HasAttributes(self) -> BooleanType: ...
    
    def get_HasChildren(self) -> BooleanType: ...
    
    def get_IsEmptyElement(self) -> BooleanType: ...
    
    def get_LocalName(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_NameTable(self) -> XmlNameTable: ...
    
    def get_NamespaceURI(self) -> StringType: ...
    
    def get_NodeType(self) -> XPathNodeType: ...
    
    def get_Prefix(self) -> StringType: ...
    
    def get_SchemaInfo(self) -> IXmlSchemaInfo: ...
    
    def get_UnderlyingObject(self) -> ObjectType: ...
    
    def get_Value(self) -> StringType: ...
    
    def get_XmlLang(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DocumentXPathNavigator(XPathNavigator, ICloneable, IXPathNavigable, IXmlNamespaceResolver, IHasXmlNode):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, document: XmlDocument, node: XmlNode): ...
    
    @overload
    def __init__(self, other: DocumentXPathNavigator): ...
    
    # ---------- Properties ---------- #
    
    @property
    def BaseURI(self) -> StringType: ...
    
    @property
    def CanEdit(self) -> BooleanType: ...
    
    @property
    def HasAttributes(self) -> BooleanType: ...
    
    @property
    def HasChildren(self) -> BooleanType: ...
    
    @property
    def IsEmptyElement(self) -> BooleanType: ...
    
    @property
    def LocalName(self) -> StringType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def NameTable(self) -> XmlNameTable: ...
    
    @property
    def NamespaceURI(self) -> StringType: ...
    
    @property
    def NodeType(self) -> XPathNodeType: ...
    
    @property
    def Prefix(self) -> StringType: ...
    
    @property
    def SchemaInfo(self) -> IXmlSchemaInfo: ...
    
    @property
    def UnderlyingObject(self) -> ObjectType: ...
    
    @property
    def Value(self) -> StringType: ...
    
    @property
    def XmlLang(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def AppendChild(self) -> XmlWriter: ...
    
    def CheckValidity(self, schemas: XmlSchemaSet, validationEventHandler: ValidationEventHandler) -> BooleanType: ...
    
    def Clone(self) -> XPathNavigator: ...
    
    def ComparePosition(self, other: XPathNavigator) -> XmlNodeOrder: ...
    
    def CreateAttributes(self) -> XmlWriter: ...
    
    def DeleteRange(self, lastSiblingToDelete: XPathNavigator) -> VoidType: ...
    
    def DeleteSelf(self) -> VoidType: ...
    
    def GetAttribute(self, localName: StringType, namespaceURI: StringType) -> StringType: ...
    
    def GetNamespace(self, name: StringType) -> StringType: ...
    
    @overload
    def InsertAfter(self) -> XmlWriter: ...
    
    @overload
    def InsertBefore(self) -> XmlWriter: ...
    
    def IsDescendant(self, other: XPathNavigator) -> BooleanType: ...
    
    def IsSamePosition(self, other: XPathNavigator) -> BooleanType: ...
    
    def LookupNamespace(self, prefix: StringType) -> StringType: ...
    
    def MoveTo(self, other: XPathNavigator) -> BooleanType: ...
    
    def MoveToAttribute(self, localName: StringType, namespaceURI: StringType) -> BooleanType: ...
    
    @overload
    def MoveToChild(self, localName: StringType, namespaceUri: StringType) -> BooleanType: ...
    
    @overload
    def MoveToChild(self, type: XPathNodeType) -> BooleanType: ...
    
    def MoveToFirst(self) -> BooleanType: ...
    
    def MoveToFirstAttribute(self) -> BooleanType: ...
    
    def MoveToFirstChild(self) -> BooleanType: ...
    
    @overload
    def MoveToFirstNamespace(self, scope: XPathNamespaceScope) -> BooleanType: ...
    
    @overload
    def MoveToFollowing(self, localName: StringType, namespaceUri: StringType, end: XPathNavigator) -> BooleanType: ...
    
    @overload
    def MoveToFollowing(self, type: XPathNodeType, end: XPathNavigator) -> BooleanType: ...
    
    def MoveToId(self, id: StringType) -> BooleanType: ...
    
    def MoveToNamespace(self, name: StringType) -> BooleanType: ...
    
    @overload
    def MoveToNext(self) -> BooleanType: ...
    
    @overload
    def MoveToNext(self, localName: StringType, namespaceUri: StringType) -> BooleanType: ...
    
    @overload
    def MoveToNext(self, type: XPathNodeType) -> BooleanType: ...
    
    def MoveToNextAttribute(self) -> BooleanType: ...
    
    @overload
    def MoveToNextNamespace(self, scope: XPathNamespaceScope) -> BooleanType: ...
    
    def MoveToParent(self) -> BooleanType: ...
    
    def MoveToPrevious(self) -> BooleanType: ...
    
    def MoveToRoot(self) -> VoidType: ...
    
    @overload
    def PrependChild(self) -> XmlWriter: ...
    
    def ReplaceRange(self, lastSiblingToReplace: XPathNavigator) -> XmlWriter: ...
    
    @overload
    def SelectDescendants(self, localName: StringType, namespaceURI: StringType, matchSelf: BooleanType) -> XPathNodeIterator: ...
    
    @overload
    def SelectDescendants(self, nt: XPathNodeType, includeSelf: BooleanType) -> XPathNodeIterator: ...
    
    def SetValue(self, value: StringType) -> VoidType: ...
    
    def get_BaseURI(self) -> StringType: ...
    
    def get_CanEdit(self) -> BooleanType: ...
    
    def get_HasAttributes(self) -> BooleanType: ...
    
    def get_HasChildren(self) -> BooleanType: ...
    
    def get_IsEmptyElement(self) -> BooleanType: ...
    
    def get_LocalName(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_NameTable(self) -> XmlNameTable: ...
    
    def get_NamespaceURI(self) -> StringType: ...
    
    def get_NodeType(self) -> XPathNodeType: ...
    
    def get_Prefix(self) -> StringType: ...
    
    def get_SchemaInfo(self) -> IXmlSchemaInfo: ...
    
    def get_UnderlyingObject(self) -> ObjectType: ...
    
    def get_Value(self) -> StringType: ...
    
    def get_XmlLang(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DocumentXPathNodeIterator_AllElemChildren(DocumentXPathNodeIterator_ElemDescendants, ICloneable, IEnumerable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XPathNodeIterator: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DocumentXPathNodeIterator_AllElemChildren(DocumentXPathNodeIterator_ElemDescendants, ICloneable, IEnumerable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XPathNodeIterator: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DocumentXPathNodeIterator_AllElemChildren_AndSelf(DocumentXPathNodeIterator_AllElemChildren, ICloneable, IEnumerable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def MoveNext(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DocumentXPathNodeIterator_AllElemChildren_AndSelf(DocumentXPathNodeIterator_AllElemChildren, ICloneable, IEnumerable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def MoveNext(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DocumentXPathNodeIterator_ElemChildren(DocumentXPathNodeIterator_ElemDescendants, ICloneable, IEnumerable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XPathNodeIterator: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DocumentXPathNodeIterator_ElemChildren(DocumentXPathNodeIterator_ElemDescendants, ICloneable, IEnumerable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XPathNodeIterator: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DocumentXPathNodeIterator_ElemChildren_AndSelf(DocumentXPathNodeIterator_ElemChildren, ICloneable, IEnumerable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def MoveNext(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DocumentXPathNodeIterator_ElemChildren_AndSelf(DocumentXPathNodeIterator_ElemChildren, ICloneable, IEnumerable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def MoveNext(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DocumentXPathNodeIterator_ElemChildren_AndSelf_NoLocalName(DocumentXPathNodeIterator_ElemChildren_NoLocalName, ICloneable, IEnumerable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def MoveNext(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DocumentXPathNodeIterator_ElemChildren_AndSelf_NoLocalName(DocumentXPathNodeIterator_ElemChildren_NoLocalName, ICloneable, IEnumerable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def MoveNext(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DocumentXPathNodeIterator_ElemChildren_NoLocalName(DocumentXPathNodeIterator_ElemDescendants, ICloneable, IEnumerable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XPathNodeIterator: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DocumentXPathNodeIterator_ElemChildren_NoLocalName(DocumentXPathNodeIterator_ElemDescendants, ICloneable, IEnumerable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XPathNodeIterator: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DocumentXPathNodeIterator_ElemDescendants(ABC, XPathNodeIterator, ICloneable, IEnumerable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Current(self) -> XPathNavigator: ...
    
    @property
    def CurrentPosition(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def MoveNext(self) -> BooleanType: ...
    
    def get_Current(self) -> XPathNavigator: ...
    
    def get_CurrentPosition(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DocumentXPathNodeIterator_ElemDescendants(ABC, XPathNodeIterator, ICloneable, IEnumerable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Current(self) -> XPathNavigator: ...
    
    @property
    def CurrentPosition(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def MoveNext(self) -> BooleanType: ...
    
    def get_Current(self) -> XPathNavigator: ...
    
    def get_CurrentPosition(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DocumentXPathNodeIterator_Empty(XPathNodeIterator, ICloneable, IEnumerable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def Current(self) -> XPathNavigator: ...
    
    @property
    def CurrentPosition(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def MoveNext(self) -> BooleanType: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_Current(self) -> XPathNavigator: ...
    
    def get_CurrentPosition(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DocumentXPathNodeIterator_Empty(XPathNodeIterator, ICloneable, IEnumerable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def Current(self) -> XPathNavigator: ...
    
    @property
    def CurrentPosition(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def MoveNext(self) -> BooleanType: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_Current(self) -> XPathNavigator: ...
    
    def get_CurrentPosition(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DocumentXmlWriter(XmlRawWriter, IDisposable, IXmlNamespaceResolver):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, type: DocumentXmlWriterType, start: XmlNode, document: XmlDocument): ...
    
    # ---------- Properties ---------- #
    
    @EndNode.setter
    def EndNode(self, value: XmlNode) -> None: ...
    
    @NamespaceManager.setter
    def NamespaceManager(self, value: XmlNamespaceManager) -> None: ...
    
    @Navigator.setter
    def Navigator(self, value: DocumentXPathNavigator) -> None: ...
    
    @property
    def Settings(self) -> XmlWriterSettings: ...
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    def Flush(self) -> VoidType: ...
    
    def WriteCData(self, text: StringType) -> VoidType: ...
    
    def WriteCharEntity(self, ch: CharType) -> VoidType: ...
    
    def WriteChars(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> VoidType: ...
    
    def WriteComment(self, text: StringType) -> VoidType: ...
    
    def WriteDocType(self, name: StringType, pubid: StringType, sysid: StringType, subset: StringType) -> VoidType: ...
    
    def WriteEndAttribute(self) -> VoidType: ...
    
    def WriteEndDocument(self) -> VoidType: ...
    
    def WriteEndElement(self) -> VoidType: ...
    
    def WriteEntityRef(self, name: StringType) -> VoidType: ...
    
    def WriteFullEndElement(self) -> VoidType: ...
    
    def WriteProcessingInstruction(self, name: StringType, text: StringType) -> VoidType: ...
    
    @overload
    def WriteRaw(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> VoidType: ...
    
    @overload
    def WriteRaw(self, data: StringType) -> VoidType: ...
    
    @overload
    def WriteStartAttribute(self, prefix: StringType, localName: StringType, ns: StringType) -> VoidType: ...
    
    @overload
    def WriteStartDocument(self) -> VoidType: ...
    
    @overload
    def WriteStartDocument(self, standalone: BooleanType) -> VoidType: ...
    
    @overload
    def WriteStartElement(self, prefix: StringType, localName: StringType, ns: StringType) -> VoidType: ...
    
    def WriteString(self, text: StringType) -> VoidType: ...
    
    def WriteSurrogateCharEntity(self, lowCh: CharType, highCh: CharType) -> VoidType: ...
    
    def WriteWhitespace(self, text: StringType) -> VoidType: ...
    
    def get_Settings(self) -> XmlWriterSettings: ...
    
    def set_EndNode(self, value: XmlNode) -> VoidType: ...
    
    def set_NamespaceManager(self, value: XmlNamespaceManager) -> VoidType: ...
    
    def set_Navigator(self, value: DocumentXPathNavigator) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DocumentXmlWriter(XmlRawWriter, IDisposable, IXmlNamespaceResolver):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, type: DocumentXmlWriterType, start: XmlNode, document: XmlDocument): ...
    
    # ---------- Properties ---------- #
    
    @EndNode.setter
    def EndNode(self, value: XmlNode) -> None: ...
    
    @NamespaceManager.setter
    def NamespaceManager(self, value: XmlNamespaceManager) -> None: ...
    
    @Navigator.setter
    def Navigator(self, value: DocumentXPathNavigator) -> None: ...
    
    @property
    def Settings(self) -> XmlWriterSettings: ...
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    def Flush(self) -> VoidType: ...
    
    def WriteCData(self, text: StringType) -> VoidType: ...
    
    def WriteCharEntity(self, ch: CharType) -> VoidType: ...
    
    def WriteChars(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> VoidType: ...
    
    def WriteComment(self, text: StringType) -> VoidType: ...
    
    def WriteDocType(self, name: StringType, pubid: StringType, sysid: StringType, subset: StringType) -> VoidType: ...
    
    def WriteEndAttribute(self) -> VoidType: ...
    
    def WriteEndDocument(self) -> VoidType: ...
    
    def WriteEndElement(self) -> VoidType: ...
    
    def WriteEntityRef(self, name: StringType) -> VoidType: ...
    
    def WriteFullEndElement(self) -> VoidType: ...
    
    def WriteProcessingInstruction(self, name: StringType, text: StringType) -> VoidType: ...
    
    @overload
    def WriteRaw(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> VoidType: ...
    
    @overload
    def WriteRaw(self, data: StringType) -> VoidType: ...
    
    @overload
    def WriteStartAttribute(self, prefix: StringType, localName: StringType, ns: StringType) -> VoidType: ...
    
    @overload
    def WriteStartDocument(self) -> VoidType: ...
    
    @overload
    def WriteStartDocument(self, standalone: BooleanType) -> VoidType: ...
    
    @overload
    def WriteStartElement(self, prefix: StringType, localName: StringType, ns: StringType) -> VoidType: ...
    
    def WriteString(self, text: StringType) -> VoidType: ...
    
    def WriteSurrogateCharEntity(self, lowCh: CharType, highCh: CharType) -> VoidType: ...
    
    def WriteWhitespace(self, text: StringType) -> VoidType: ...
    
    def get_Settings(self) -> XmlWriterSettings: ...
    
    def set_EndNode(self, value: XmlNode) -> VoidType: ...
    
    def set_NamespaceManager(self, value: XmlNamespaceManager) -> VoidType: ...
    
    def set_Navigator(self, value: DocumentXPathNavigator) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DomNameTable(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, document: XmlDocument): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def AddName(self, prefix: StringType, localName: StringType, ns: StringType, schemaInfo: IXmlSchemaInfo) -> XmlName: ...
    
    def GetName(self, prefix: StringType, localName: StringType, ns: StringType, schemaInfo: IXmlSchemaInfo) -> XmlName: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DomNameTable(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, document: XmlDocument): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def AddName(self, prefix: StringType, localName: StringType, ns: StringType, schemaInfo: IXmlSchemaInfo) -> XmlName: ...
    
    def GetName(self, prefix: StringType, localName: StringType, ns: StringType, schemaInfo: IXmlSchemaInfo) -> XmlName: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DtdParser(ObjectType, IDtdParser):
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


class DtdParser(ObjectType, IDtdParser):
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


class EmptyEnumerator(ObjectType, IEnumerator):
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


class EmptyEnumerator(ObjectType, IEnumerator):
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


class HWStack(ObjectType, ICloneable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class HWStack(ObjectType, ICloneable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class HtmlEncodedRawTextWriter(XmlEncodedRawTextWriter, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, writer: TextWriter, settings: XmlWriterSettings): ...
    
    @overload
    def __init__(self, stream: Stream, settings: XmlWriterSettings): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def WriteCharEntity(self, ch: CharType) -> VoidType: ...
    
    def WriteChars(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> VoidType: ...
    
    def WriteDocType(self, name: StringType, pubid: StringType, sysid: StringType, subset: StringType) -> VoidType: ...
    
    def WriteEndAttribute(self) -> VoidType: ...
    
    def WriteEntityRef(self, name: StringType) -> VoidType: ...
    
    def WriteProcessingInstruction(self, target: StringType, text: StringType) -> VoidType: ...
    
    @overload
    def WriteStartAttribute(self, prefix: StringType, localName: StringType, ns: StringType) -> VoidType: ...
    
    @overload
    def WriteStartElement(self, prefix: StringType, localName: StringType, ns: StringType) -> VoidType: ...
    
    def WriteString(self, text: StringType) -> VoidType: ...
    
    def WriteSurrogateCharEntity(self, lowChar: CharType, highChar: CharType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class HtmlEncodedRawTextWriter(XmlEncodedRawTextWriter, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, writer: TextWriter, settings: XmlWriterSettings): ...
    
    @overload
    def __init__(self, stream: Stream, settings: XmlWriterSettings): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def WriteCharEntity(self, ch: CharType) -> VoidType: ...
    
    def WriteChars(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> VoidType: ...
    
    def WriteDocType(self, name: StringType, pubid: StringType, sysid: StringType, subset: StringType) -> VoidType: ...
    
    def WriteEndAttribute(self) -> VoidType: ...
    
    def WriteEntityRef(self, name: StringType) -> VoidType: ...
    
    def WriteProcessingInstruction(self, target: StringType, text: StringType) -> VoidType: ...
    
    @overload
    def WriteStartAttribute(self, prefix: StringType, localName: StringType, ns: StringType) -> VoidType: ...
    
    @overload
    def WriteStartElement(self, prefix: StringType, localName: StringType, ns: StringType) -> VoidType: ...
    
    def WriteString(self, text: StringType) -> VoidType: ...
    
    def WriteSurrogateCharEntity(self, lowChar: CharType, highChar: CharType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class HtmlEncodedRawTextWriterIndent(HtmlEncodedRawTextWriter, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, writer: TextWriter, settings: XmlWriterSettings): ...
    
    @overload
    def __init__(self, stream: Stream, settings: XmlWriterSettings): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def WriteDocType(self, name: StringType, pubid: StringType, sysid: StringType, subset: StringType) -> VoidType: ...
    
    @overload
    def WriteStartAttribute(self, prefix: StringType, localName: StringType, ns: StringType) -> VoidType: ...
    
    @overload
    def WriteStartElement(self, prefix: StringType, localName: StringType, ns: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class HtmlEncodedRawTextWriterIndent(HtmlEncodedRawTextWriter, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, writer: TextWriter, settings: XmlWriterSettings): ...
    
    @overload
    def __init__(self, stream: Stream, settings: XmlWriterSettings): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def WriteDocType(self, name: StringType, pubid: StringType, sysid: StringType, subset: StringType) -> VoidType: ...
    
    @overload
    def WriteStartAttribute(self, prefix: StringType, localName: StringType, ns: StringType) -> VoidType: ...
    
    @overload
    def WriteStartElement(self, prefix: StringType, localName: StringType, ns: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class HtmlTernaryTree(ABC, ObjectType):
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


class HtmlTernaryTree(ABC, ObjectType):
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


class HtmlUtf8RawTextWriter(XmlUtf8RawTextWriter, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, stream: Stream, settings: XmlWriterSettings): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def WriteCharEntity(self, ch: CharType) -> VoidType: ...
    
    def WriteChars(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> VoidType: ...
    
    def WriteDocType(self, name: StringType, pubid: StringType, sysid: StringType, subset: StringType) -> VoidType: ...
    
    def WriteEndAttribute(self) -> VoidType: ...
    
    def WriteEntityRef(self, name: StringType) -> VoidType: ...
    
    def WriteProcessingInstruction(self, target: StringType, text: StringType) -> VoidType: ...
    
    @overload
    def WriteStartAttribute(self, prefix: StringType, localName: StringType, ns: StringType) -> VoidType: ...
    
    @overload
    def WriteStartElement(self, prefix: StringType, localName: StringType, ns: StringType) -> VoidType: ...
    
    def WriteString(self, text: StringType) -> VoidType: ...
    
    def WriteSurrogateCharEntity(self, lowChar: CharType, highChar: CharType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class HtmlUtf8RawTextWriter(XmlUtf8RawTextWriter, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, stream: Stream, settings: XmlWriterSettings): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def WriteCharEntity(self, ch: CharType) -> VoidType: ...
    
    def WriteChars(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> VoidType: ...
    
    def WriteDocType(self, name: StringType, pubid: StringType, sysid: StringType, subset: StringType) -> VoidType: ...
    
    def WriteEndAttribute(self) -> VoidType: ...
    
    def WriteEntityRef(self, name: StringType) -> VoidType: ...
    
    def WriteProcessingInstruction(self, target: StringType, text: StringType) -> VoidType: ...
    
    @overload
    def WriteStartAttribute(self, prefix: StringType, localName: StringType, ns: StringType) -> VoidType: ...
    
    @overload
    def WriteStartElement(self, prefix: StringType, localName: StringType, ns: StringType) -> VoidType: ...
    
    def WriteString(self, text: StringType) -> VoidType: ...
    
    def WriteSurrogateCharEntity(self, lowChar: CharType, highChar: CharType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class HtmlUtf8RawTextWriterIndent(HtmlUtf8RawTextWriter, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, stream: Stream, settings: XmlWriterSettings): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def WriteDocType(self, name: StringType, pubid: StringType, sysid: StringType, subset: StringType) -> VoidType: ...
    
    @overload
    def WriteStartAttribute(self, prefix: StringType, localName: StringType, ns: StringType) -> VoidType: ...
    
    @overload
    def WriteStartElement(self, prefix: StringType, localName: StringType, ns: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class HtmlUtf8RawTextWriterIndent(HtmlUtf8RawTextWriter, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, stream: Stream, settings: XmlWriterSettings): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def WriteDocType(self, name: StringType, pubid: StringType, sysid: StringType, subset: StringType) -> VoidType: ...
    
    @overload
    def WriteStartAttribute(self, prefix: StringType, localName: StringType, ns: StringType) -> VoidType: ...
    
    @overload
    def WriteStartElement(self, prefix: StringType, localName: StringType, ns: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IncrementalReadCharsDecoder(IncrementalReadDecoder):
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


class IncrementalReadCharsDecoder(IncrementalReadDecoder):
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


class IncrementalReadDecoder(ABC, ObjectType):
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


class IncrementalReadDecoder(ABC, ObjectType):
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


class IncrementalReadDummyDecoder(IncrementalReadDecoder):
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


class IncrementalReadDummyDecoder(IncrementalReadDecoder):
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


class NameTable(XmlNameTable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def Add(self, key: StringType) -> StringType: ...
    
    @overload
    def Add(self, key: ArrayType[CharType], start: IntType, len: IntType) -> StringType: ...
    
    @overload
    def Get(self, value: StringType) -> StringType: ...
    
    @overload
    def Get(self, key: ArrayType[CharType], start: IntType, len: IntType) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class NameTable(XmlNameTable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def Add(self, key: StringType) -> StringType: ...
    
    @overload
    def Add(self, key: ArrayType[CharType], start: IntType, len: IntType) -> StringType: ...
    
    @overload
    def Get(self, value: StringType) -> StringType: ...
    
    @overload
    def Get(self, key: ArrayType[CharType], start: IntType, len: IntType) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class OnRemoveWriter(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, writer: XmlRawWriter, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, writer: XmlRawWriter) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class OnRemoveWriter(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, writer: XmlRawWriter, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, writer: XmlRawWriter) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class OpenedHost(ObjectType):
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


class OpenedHost(ObjectType):
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


class PositionInfo(ObjectType, IXmlLineInfo):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def LineNumber(self) -> IntType: ...
    
    @property
    def LinePosition(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def GetPositionInfo(o: ObjectType) -> PositionInfo: ...
    
    def HasLineInfo(self) -> BooleanType: ...
    
    def get_LineNumber(self) -> IntType: ...
    
    def get_LinePosition(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PositionInfo(ObjectType, IXmlLineInfo):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def LineNumber(self) -> IntType: ...
    
    @property
    def LinePosition(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def GetPositionInfo(o: ObjectType) -> PositionInfo: ...
    
    def HasLineInfo(self) -> BooleanType: ...
    
    def get_LineNumber(self) -> IntType: ...
    
    def get_LinePosition(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class QueryOutputWriter(XmlRawWriter, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, writer: XmlRawWriter, settings: XmlWriterSettings): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Settings(self) -> XmlWriterSettings: ...
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    def Flush(self) -> VoidType: ...
    
    def WriteCData(self, text: StringType) -> VoidType: ...
    
    def WriteCharEntity(self, ch: CharType) -> VoidType: ...
    
    def WriteChars(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> VoidType: ...
    
    def WriteComment(self, text: StringType) -> VoidType: ...
    
    def WriteDocType(self, name: StringType, pubid: StringType, sysid: StringType, subset: StringType) -> VoidType: ...
    
    def WriteEndAttribute(self) -> VoidType: ...
    
    def WriteEntityRef(self, name: StringType) -> VoidType: ...
    
    def WriteProcessingInstruction(self, name: StringType, text: StringType) -> VoidType: ...
    
    @overload
    def WriteRaw(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> VoidType: ...
    
    @overload
    def WriteRaw(self, data: StringType) -> VoidType: ...
    
    @overload
    def WriteStartAttribute(self, prefix: StringType, localName: StringType, ns: StringType) -> VoidType: ...
    
    @overload
    def WriteStartElement(self, prefix: StringType, localName: StringType, ns: StringType) -> VoidType: ...
    
    def WriteString(self, text: StringType) -> VoidType: ...
    
    def WriteSurrogateCharEntity(self, lowChar: CharType, highChar: CharType) -> VoidType: ...
    
    def WriteWhitespace(self, ws: StringType) -> VoidType: ...
    
    def get_Settings(self) -> XmlWriterSettings: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class QueryOutputWriter(XmlRawWriter, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, writer: XmlRawWriter, settings: XmlWriterSettings): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Settings(self) -> XmlWriterSettings: ...
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    def Flush(self) -> VoidType: ...
    
    def WriteCData(self, text: StringType) -> VoidType: ...
    
    def WriteCharEntity(self, ch: CharType) -> VoidType: ...
    
    def WriteChars(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> VoidType: ...
    
    def WriteComment(self, text: StringType) -> VoidType: ...
    
    def WriteDocType(self, name: StringType, pubid: StringType, sysid: StringType, subset: StringType) -> VoidType: ...
    
    def WriteEndAttribute(self) -> VoidType: ...
    
    def WriteEntityRef(self, name: StringType) -> VoidType: ...
    
    def WriteProcessingInstruction(self, name: StringType, text: StringType) -> VoidType: ...
    
    @overload
    def WriteRaw(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> VoidType: ...
    
    @overload
    def WriteRaw(self, data: StringType) -> VoidType: ...
    
    @overload
    def WriteStartAttribute(self, prefix: StringType, localName: StringType, ns: StringType) -> VoidType: ...
    
    @overload
    def WriteStartElement(self, prefix: StringType, localName: StringType, ns: StringType) -> VoidType: ...
    
    def WriteString(self, text: StringType) -> VoidType: ...
    
    def WriteSurrogateCharEntity(self, lowChar: CharType, highChar: CharType) -> VoidType: ...
    
    def WriteWhitespace(self, ws: StringType) -> VoidType: ...
    
    def get_Settings(self) -> XmlWriterSettings: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class QueryOutputWriterV1(XmlWriter, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, writer: XmlWriter, settings: XmlWriterSettings): ...
    
    # ---------- Properties ---------- #
    
    @property
    def WriteState(self) -> WriteState: ...
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    def Flush(self) -> VoidType: ...
    
    def LookupPrefix(self, ns: StringType) -> StringType: ...
    
    def WriteBase64(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> VoidType: ...
    
    def WriteCData(self, text: StringType) -> VoidType: ...
    
    def WriteCharEntity(self, ch: CharType) -> VoidType: ...
    
    def WriteChars(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> VoidType: ...
    
    def WriteComment(self, text: StringType) -> VoidType: ...
    
    def WriteDocType(self, name: StringType, pubid: StringType, sysid: StringType, subset: StringType) -> VoidType: ...
    
    def WriteEndAttribute(self) -> VoidType: ...
    
    def WriteEndDocument(self) -> VoidType: ...
    
    def WriteEndElement(self) -> VoidType: ...
    
    def WriteEntityRef(self, name: StringType) -> VoidType: ...
    
    def WriteFullEndElement(self) -> VoidType: ...
    
    def WriteProcessingInstruction(self, name: StringType, text: StringType) -> VoidType: ...
    
    @overload
    def WriteRaw(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> VoidType: ...
    
    @overload
    def WriteRaw(self, data: StringType) -> VoidType: ...
    
    @overload
    def WriteStartAttribute(self, prefix: StringType, localName: StringType, ns: StringType) -> VoidType: ...
    
    @overload
    def WriteStartDocument(self) -> VoidType: ...
    
    @overload
    def WriteStartDocument(self, standalone: BooleanType) -> VoidType: ...
    
    @overload
    def WriteStartElement(self, prefix: StringType, localName: StringType, ns: StringType) -> VoidType: ...
    
    def WriteString(self, text: StringType) -> VoidType: ...
    
    def WriteSurrogateCharEntity(self, lowChar: CharType, highChar: CharType) -> VoidType: ...
    
    def WriteWhitespace(self, ws: StringType) -> VoidType: ...
    
    def get_WriteState(self) -> WriteState: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class QueryOutputWriterV1(XmlWriter, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, writer: XmlWriter, settings: XmlWriterSettings): ...
    
    # ---------- Properties ---------- #
    
    @property
    def WriteState(self) -> WriteState: ...
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    def Flush(self) -> VoidType: ...
    
    def LookupPrefix(self, ns: StringType) -> StringType: ...
    
    def WriteBase64(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> VoidType: ...
    
    def WriteCData(self, text: StringType) -> VoidType: ...
    
    def WriteCharEntity(self, ch: CharType) -> VoidType: ...
    
    def WriteChars(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> VoidType: ...
    
    def WriteComment(self, text: StringType) -> VoidType: ...
    
    def WriteDocType(self, name: StringType, pubid: StringType, sysid: StringType, subset: StringType) -> VoidType: ...
    
    def WriteEndAttribute(self) -> VoidType: ...
    
    def WriteEndDocument(self) -> VoidType: ...
    
    def WriteEndElement(self) -> VoidType: ...
    
    def WriteEntityRef(self, name: StringType) -> VoidType: ...
    
    def WriteFullEndElement(self) -> VoidType: ...
    
    def WriteProcessingInstruction(self, name: StringType, text: StringType) -> VoidType: ...
    
    @overload
    def WriteRaw(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> VoidType: ...
    
    @overload
    def WriteRaw(self, data: StringType) -> VoidType: ...
    
    @overload
    def WriteStartAttribute(self, prefix: StringType, localName: StringType, ns: StringType) -> VoidType: ...
    
    @overload
    def WriteStartDocument(self) -> VoidType: ...
    
    @overload
    def WriteStartDocument(self, standalone: BooleanType) -> VoidType: ...
    
    @overload
    def WriteStartElement(self, prefix: StringType, localName: StringType, ns: StringType) -> VoidType: ...
    
    def WriteString(self, text: StringType) -> VoidType: ...
    
    def WriteSurrogateCharEntity(self, lowChar: CharType, highChar: CharType) -> VoidType: ...
    
    def WriteWhitespace(self, ws: StringType) -> VoidType: ...
    
    def get_WriteState(self) -> WriteState: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ReadContentAsBinaryHelper(ObjectType):
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


class ReadContentAsBinaryHelper(ObjectType):
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


class ReaderPositionInfo(PositionInfo, IXmlLineInfo):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, lineInfo: IXmlLineInfo): ...
    
    # ---------- Properties ---------- #
    
    @property
    def LineNumber(self) -> IntType: ...
    
    @property
    def LinePosition(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def HasLineInfo(self) -> BooleanType: ...
    
    def get_LineNumber(self) -> IntType: ...
    
    def get_LinePosition(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ReaderPositionInfo(PositionInfo, IXmlLineInfo):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, lineInfo: IXmlLineInfo): ...
    
    # ---------- Properties ---------- #
    
    @property
    def LineNumber(self) -> IntType: ...
    
    @property
    def LinePosition(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def HasLineInfo(self) -> BooleanType: ...
    
    def get_LineNumber(self) -> IntType: ...
    
    def get_LinePosition(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Ref(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def Equal(strA: StringType, strB: StringType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def Equals(objA: ObjectType, objB: ObjectType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Ref(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def Equal(strA: StringType, strB: StringType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def Equals(objA: ObjectType, objB: ObjectType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Res(ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def Resources() -> ResourceManager: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def GetObject(name: StringType) -> ObjectType: ...
    
    @staticmethod
    @overload
    def GetString(name: StringType, args: ArrayType[ObjectType]) -> StringType: ...
    
    @staticmethod
    @overload
    def GetString(name: StringType) -> StringType: ...
    
    @staticmethod
    @overload
    def GetString(name: StringType, usedFallback: BooleanType) -> Tuple[StringType, BooleanType]: ...
    
    @staticmethod
    def get_Resources() -> ResourceManager: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Res(ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def Resources() -> ResourceManager: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def GetObject(name: StringType) -> ObjectType: ...
    
    @staticmethod
    @overload
    def GetString(name: StringType, args: ArrayType[ObjectType]) -> StringType: ...
    
    @staticmethod
    @overload
    def GetString(name: StringType) -> StringType: ...
    
    @staticmethod
    @overload
    def GetString(name: StringType, usedFallback: BooleanType) -> Tuple[StringType, BooleanType]: ...
    
    @staticmethod
    def get_Resources() -> ResourceManager: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ResCategoryAttribute(CategoryAttribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, category: StringType): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ResCategoryAttribute(CategoryAttribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, category: StringType): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ResDescriptionAttribute(DescriptionAttribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, description: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Description(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_Description(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ResDescriptionAttribute(DescriptionAttribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, description: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Description(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_Description(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SafeAsciiDecoder(Decoder):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def Convert(self, bytes: ArrayType[ByteType], byteIndex: IntType, byteCount: IntType, chars: ArrayType[CharType], charIndex: IntType, charCount: IntType, flush: BooleanType, bytesUsed: IntType, charsUsed: IntType, completed: BooleanType) -> Tuple[VoidType, IntType, IntType, BooleanType]: ...
    
    @overload
    def GetCharCount(self, bytes: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    @overload
    def GetChars(self, bytes: ArrayType[ByteType], byteIndex: IntType, byteCount: IntType, chars: ArrayType[CharType], charIndex: IntType) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SafeAsciiDecoder(Decoder):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def Convert(self, bytes: ArrayType[ByteType], byteIndex: IntType, byteCount: IntType, chars: ArrayType[CharType], charIndex: IntType, charCount: IntType, flush: BooleanType, bytesUsed: IntType, charsUsed: IntType, completed: BooleanType) -> Tuple[VoidType, IntType, IntType, BooleanType]: ...
    
    @overload
    def GetCharCount(self, bytes: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    @overload
    def GetChars(self, bytes: ArrayType[ByteType], byteIndex: IntType, byteCount: IntType, chars: ArrayType[CharType], charIndex: IntType) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SecureStringHasher(ObjectType, IEqualityComparer[StringType]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def Equals(self, x: StringType, y: StringType) -> BooleanType: ...
    
    @overload
    def GetHashCode(self, key: StringType) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SecureStringHasher(ObjectType, IEqualityComparer[StringType]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def Equals(self, x: StringType, y: StringType) -> BooleanType: ...
    
    @overload
    def GetHashCode(self, key: StringType) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TernaryTreeReadOnly(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, nodeBuffer: ArrayType[ByteType]): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def FindCaseInsensitiveString(self, stringToFind: StringType) -> ByteType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TernaryTreeReadOnly(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, nodeBuffer: ArrayType[ByteType]): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def FindCaseInsensitiveString(self, stringToFind: StringType) -> ByteType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TextEncodedRawTextWriter(XmlEncodedRawTextWriter, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, writer: TextWriter, settings: XmlWriterSettings): ...
    
    @overload
    def __init__(self, stream: Stream, settings: XmlWriterSettings): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def WriteCData(self, text: StringType) -> VoidType: ...
    
    def WriteCharEntity(self, ch: CharType) -> VoidType: ...
    
    def WriteChars(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> VoidType: ...
    
    def WriteComment(self, text: StringType) -> VoidType: ...
    
    def WriteDocType(self, name: StringType, pubid: StringType, sysid: StringType, subset: StringType) -> VoidType: ...
    
    def WriteEndAttribute(self) -> VoidType: ...
    
    def WriteEntityRef(self, name: StringType) -> VoidType: ...
    
    def WriteProcessingInstruction(self, name: StringType, text: StringType) -> VoidType: ...
    
    @overload
    def WriteRaw(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> VoidType: ...
    
    @overload
    def WriteRaw(self, data: StringType) -> VoidType: ...
    
    @overload
    def WriteStartAttribute(self, prefix: StringType, localName: StringType, ns: StringType) -> VoidType: ...
    
    @overload
    def WriteStartElement(self, prefix: StringType, localName: StringType, ns: StringType) -> VoidType: ...
    
    def WriteString(self, textBlock: StringType) -> VoidType: ...
    
    def WriteSurrogateCharEntity(self, lowChar: CharType, highChar: CharType) -> VoidType: ...
    
    def WriteWhitespace(self, ws: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TextEncodedRawTextWriter(XmlEncodedRawTextWriter, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, writer: TextWriter, settings: XmlWriterSettings): ...
    
    @overload
    def __init__(self, stream: Stream, settings: XmlWriterSettings): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def WriteCData(self, text: StringType) -> VoidType: ...
    
    def WriteCharEntity(self, ch: CharType) -> VoidType: ...
    
    def WriteChars(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> VoidType: ...
    
    def WriteComment(self, text: StringType) -> VoidType: ...
    
    def WriteDocType(self, name: StringType, pubid: StringType, sysid: StringType, subset: StringType) -> VoidType: ...
    
    def WriteEndAttribute(self) -> VoidType: ...
    
    def WriteEntityRef(self, name: StringType) -> VoidType: ...
    
    def WriteProcessingInstruction(self, name: StringType, text: StringType) -> VoidType: ...
    
    @overload
    def WriteRaw(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> VoidType: ...
    
    @overload
    def WriteRaw(self, data: StringType) -> VoidType: ...
    
    @overload
    def WriteStartAttribute(self, prefix: StringType, localName: StringType, ns: StringType) -> VoidType: ...
    
    @overload
    def WriteStartElement(self, prefix: StringType, localName: StringType, ns: StringType) -> VoidType: ...
    
    def WriteString(self, textBlock: StringType) -> VoidType: ...
    
    def WriteSurrogateCharEntity(self, lowChar: CharType, highChar: CharType) -> VoidType: ...
    
    def WriteWhitespace(self, ws: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TextUtf8RawTextWriter(XmlUtf8RawTextWriter, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, stream: Stream, settings: XmlWriterSettings): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def WriteCData(self, text: StringType) -> VoidType: ...
    
    def WriteCharEntity(self, ch: CharType) -> VoidType: ...
    
    def WriteChars(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> VoidType: ...
    
    def WriteComment(self, text: StringType) -> VoidType: ...
    
    def WriteDocType(self, name: StringType, pubid: StringType, sysid: StringType, subset: StringType) -> VoidType: ...
    
    def WriteEndAttribute(self) -> VoidType: ...
    
    def WriteEntityRef(self, name: StringType) -> VoidType: ...
    
    def WriteProcessingInstruction(self, name: StringType, text: StringType) -> VoidType: ...
    
    @overload
    def WriteRaw(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> VoidType: ...
    
    @overload
    def WriteRaw(self, data: StringType) -> VoidType: ...
    
    @overload
    def WriteStartAttribute(self, prefix: StringType, localName: StringType, ns: StringType) -> VoidType: ...
    
    @overload
    def WriteStartElement(self, prefix: StringType, localName: StringType, ns: StringType) -> VoidType: ...
    
    def WriteString(self, textBlock: StringType) -> VoidType: ...
    
    def WriteSurrogateCharEntity(self, lowChar: CharType, highChar: CharType) -> VoidType: ...
    
    def WriteWhitespace(self, ws: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TextUtf8RawTextWriter(XmlUtf8RawTextWriter, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, stream: Stream, settings: XmlWriterSettings): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def WriteCData(self, text: StringType) -> VoidType: ...
    
    def WriteCharEntity(self, ch: CharType) -> VoidType: ...
    
    def WriteChars(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> VoidType: ...
    
    def WriteComment(self, text: StringType) -> VoidType: ...
    
    def WriteDocType(self, name: StringType, pubid: StringType, sysid: StringType, subset: StringType) -> VoidType: ...
    
    def WriteEndAttribute(self) -> VoidType: ...
    
    def WriteEntityRef(self, name: StringType) -> VoidType: ...
    
    def WriteProcessingInstruction(self, name: StringType, text: StringType) -> VoidType: ...
    
    @overload
    def WriteRaw(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> VoidType: ...
    
    @overload
    def WriteRaw(self, data: StringType) -> VoidType: ...
    
    @overload
    def WriteStartAttribute(self, prefix: StringType, localName: StringType, ns: StringType) -> VoidType: ...
    
    @overload
    def WriteStartElement(self, prefix: StringType, localName: StringType, ns: StringType) -> VoidType: ...
    
    def WriteString(self, textBlock: StringType) -> VoidType: ...
    
    def WriteSurrogateCharEntity(self, lowChar: CharType, highChar: CharType) -> VoidType: ...
    
    def WriteWhitespace(self, ws: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UTF16Decoder(Decoder):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, bigEndian: BooleanType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def Convert(self, bytes: ArrayType[ByteType], byteIndex: IntType, byteCount: IntType, chars: ArrayType[CharType], charIndex: IntType, charCount: IntType, flush: BooleanType, bytesUsed: IntType, charsUsed: IntType, completed: BooleanType) -> Tuple[VoidType, IntType, IntType, BooleanType]: ...
    
    @overload
    def GetCharCount(self, bytes: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    @overload
    def GetCharCount(self, bytes: ArrayType[ByteType], index: IntType, count: IntType, flush: BooleanType) -> IntType: ...
    
    @overload
    def GetChars(self, bytes: ArrayType[ByteType], byteIndex: IntType, byteCount: IntType, chars: ArrayType[CharType], charIndex: IntType) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UTF16Decoder(Decoder):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, bigEndian: BooleanType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def Convert(self, bytes: ArrayType[ByteType], byteIndex: IntType, byteCount: IntType, chars: ArrayType[CharType], charIndex: IntType, charCount: IntType, flush: BooleanType, bytesUsed: IntType, charsUsed: IntType, completed: BooleanType) -> Tuple[VoidType, IntType, IntType, BooleanType]: ...
    
    @overload
    def GetCharCount(self, bytes: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    @overload
    def GetCharCount(self, bytes: ArrayType[ByteType], index: IntType, count: IntType, flush: BooleanType) -> IntType: ...
    
    @overload
    def GetChars(self, bytes: ArrayType[ByteType], byteIndex: IntType, byteCount: IntType, chars: ArrayType[CharType], charIndex: IntType) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Ucs4Decoder(ABC, Decoder):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def Convert(self, bytes: ArrayType[ByteType], byteIndex: IntType, byteCount: IntType, chars: ArrayType[CharType], charIndex: IntType, charCount: IntType, flush: BooleanType, bytesUsed: IntType, charsUsed: IntType, completed: BooleanType) -> Tuple[VoidType, IntType, IntType, BooleanType]: ...
    
    @overload
    def GetCharCount(self, bytes: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    @overload
    def GetChars(self, bytes: ArrayType[ByteType], byteIndex: IntType, byteCount: IntType, chars: ArrayType[CharType], charIndex: IntType) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Ucs4Decoder(ABC, Decoder):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def Convert(self, bytes: ArrayType[ByteType], byteIndex: IntType, byteCount: IntType, chars: ArrayType[CharType], charIndex: IntType, charCount: IntType, flush: BooleanType, bytesUsed: IntType, charsUsed: IntType, completed: BooleanType) -> Tuple[VoidType, IntType, IntType, BooleanType]: ...
    
    @overload
    def GetCharCount(self, bytes: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    @overload
    def GetChars(self, bytes: ArrayType[ByteType], byteIndex: IntType, byteCount: IntType, chars: ArrayType[CharType], charIndex: IntType) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Ucs4Decoder1234(Ucs4Decoder):
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


class Ucs4Decoder1234(Ucs4Decoder):
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


class Ucs4Decoder2143(Ucs4Decoder):
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


class Ucs4Decoder2143(Ucs4Decoder):
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


class Ucs4Decoder3412(Ucs4Decoder):
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


class Ucs4Decoder3412(Ucs4Decoder):
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


class Ucs4Decoder4321(Ucs4Decoder):
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


class Ucs4Decoder4321(Ucs4Decoder):
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


class Ucs4Encoding(Encoding, ICloneable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CodePage(self) -> IntType: ...
    
    @property
    def WebName(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def GetByteCount(self, chars: ArrayType[CharType], index: IntType, count: IntType) -> IntType: ...
    
    @overload
    def GetByteCount(self, chars: ArrayType[CharType]) -> IntType: ...
    
    @overload
    def GetBytes(self, s: StringType) -> ArrayType[ByteType]: ...
    
    @overload
    def GetBytes(self, chars: ArrayType[CharType], charIndex: IntType, charCount: IntType, bytes: ArrayType[ByteType], byteIndex: IntType) -> IntType: ...
    
    @overload
    def GetCharCount(self, bytes: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    @overload
    def GetCharCount(self, bytes: ArrayType[ByteType]) -> IntType: ...
    
    @overload
    def GetChars(self, bytes: ArrayType[ByteType], byteIndex: IntType, byteCount: IntType, chars: ArrayType[CharType], charIndex: IntType) -> IntType: ...
    
    def GetDecoder(self) -> Decoder: ...
    
    def GetEncoder(self) -> Encoder: ...
    
    def GetMaxByteCount(self, charCount: IntType) -> IntType: ...
    
    def GetMaxCharCount(self, byteCount: IntType) -> IntType: ...
    
    def get_CodePage(self) -> IntType: ...
    
    def get_WebName(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Ucs4Encoding(Encoding, ICloneable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CodePage(self) -> IntType: ...
    
    @property
    def WebName(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def GetByteCount(self, chars: ArrayType[CharType], index: IntType, count: IntType) -> IntType: ...
    
    @overload
    def GetByteCount(self, chars: ArrayType[CharType]) -> IntType: ...
    
    @overload
    def GetBytes(self, s: StringType) -> ArrayType[ByteType]: ...
    
    @overload
    def GetBytes(self, chars: ArrayType[CharType], charIndex: IntType, charCount: IntType, bytes: ArrayType[ByteType], byteIndex: IntType) -> IntType: ...
    
    @overload
    def GetCharCount(self, bytes: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    @overload
    def GetCharCount(self, bytes: ArrayType[ByteType]) -> IntType: ...
    
    @overload
    def GetChars(self, bytes: ArrayType[ByteType], byteIndex: IntType, byteCount: IntType, chars: ArrayType[CharType], charIndex: IntType) -> IntType: ...
    
    def GetDecoder(self) -> Decoder: ...
    
    def GetEncoder(self) -> Encoder: ...
    
    def GetMaxByteCount(self, charCount: IntType) -> IntType: ...
    
    def GetMaxCharCount(self, byteCount: IntType) -> IntType: ...
    
    def get_CodePage(self) -> IntType: ...
    
    def get_WebName(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Ucs4Encoding1234(Ucs4Encoding, ICloneable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def EncodingName(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetPreamble(self) -> ArrayType[ByteType]: ...
    
    def get_EncodingName(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Ucs4Encoding1234(Ucs4Encoding, ICloneable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def EncodingName(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetPreamble(self) -> ArrayType[ByteType]: ...
    
    def get_EncodingName(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Ucs4Encoding2143(Ucs4Encoding, ICloneable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def EncodingName(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetPreamble(self) -> ArrayType[ByteType]: ...
    
    def get_EncodingName(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Ucs4Encoding2143(Ucs4Encoding, ICloneable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def EncodingName(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetPreamble(self) -> ArrayType[ByteType]: ...
    
    def get_EncodingName(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Ucs4Encoding3412(Ucs4Encoding, ICloneable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def EncodingName(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetPreamble(self) -> ArrayType[ByteType]: ...
    
    def get_EncodingName(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Ucs4Encoding3412(Ucs4Encoding, ICloneable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def EncodingName(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetPreamble(self) -> ArrayType[ByteType]: ...
    
    def get_EncodingName(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Ucs4Encoding4321(Ucs4Encoding, ICloneable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def EncodingName(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetPreamble(self) -> ArrayType[ByteType]: ...
    
    def get_EncodingName(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Ucs4Encoding4321(Ucs4Encoding, ICloneable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def EncodingName(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetPreamble(self) -> ArrayType[ByteType]: ...
    
    def get_EncodingName(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ValidateNames(ABC, ObjectType):
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


class ValidateNames(ABC, ObjectType):
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


class ValidatingReaderNodeData(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, nodeType: XmlNodeType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AttInfo(self) -> AttributePSVIInfo: ...
    
    @AttInfo.setter
    def AttInfo(self, value: AttributePSVIInfo) -> None: ...
    
    @property
    def Depth(self) -> IntType: ...
    
    @Depth.setter
    def Depth(self, value: IntType) -> None: ...
    
    @property
    def LineNumber(self) -> IntType: ...
    
    @property
    def LinePosition(self) -> IntType: ...
    
    @property
    def LocalName(self) -> StringType: ...
    
    @LocalName.setter
    def LocalName(self, value: StringType) -> None: ...
    
    @property
    def Namespace(self) -> StringType: ...
    
    @Namespace.setter
    def Namespace(self, value: StringType) -> None: ...
    
    @property
    def NodeType(self) -> XmlNodeType: ...
    
    @NodeType.setter
    def NodeType(self, value: XmlNodeType) -> None: ...
    
    @property
    def OriginalStringValue(self) -> StringType: ...
    
    @OriginalStringValue.setter
    def OriginalStringValue(self, value: StringType) -> None: ...
    
    @property
    def Prefix(self) -> StringType: ...
    
    @Prefix.setter
    def Prefix(self, value: StringType) -> None: ...
    
    @property
    def RawValue(self) -> StringType: ...
    
    @RawValue.setter
    def RawValue(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def GetAtomizedNameWPrefix(self, nameTable: XmlNameTable) -> StringType: ...
    
    def get_AttInfo(self) -> AttributePSVIInfo: ...
    
    def get_Depth(self) -> IntType: ...
    
    def get_LineNumber(self) -> IntType: ...
    
    def get_LinePosition(self) -> IntType: ...
    
    def get_LocalName(self) -> StringType: ...
    
    def get_Namespace(self) -> StringType: ...
    
    def get_NodeType(self) -> XmlNodeType: ...
    
    def get_OriginalStringValue(self) -> StringType: ...
    
    def get_Prefix(self) -> StringType: ...
    
    def get_RawValue(self) -> StringType: ...
    
    def set_AttInfo(self, value: AttributePSVIInfo) -> VoidType: ...
    
    def set_Depth(self, value: IntType) -> VoidType: ...
    
    def set_LocalName(self, value: StringType) -> VoidType: ...
    
    def set_Namespace(self, value: StringType) -> VoidType: ...
    
    def set_NodeType(self, value: XmlNodeType) -> VoidType: ...
    
    def set_OriginalStringValue(self, value: StringType) -> VoidType: ...
    
    def set_Prefix(self, value: StringType) -> VoidType: ...
    
    def set_RawValue(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ValidatingReaderNodeData(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, nodeType: XmlNodeType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AttInfo(self) -> AttributePSVIInfo: ...
    
    @AttInfo.setter
    def AttInfo(self, value: AttributePSVIInfo) -> None: ...
    
    @property
    def Depth(self) -> IntType: ...
    
    @Depth.setter
    def Depth(self, value: IntType) -> None: ...
    
    @property
    def LineNumber(self) -> IntType: ...
    
    @property
    def LinePosition(self) -> IntType: ...
    
    @property
    def LocalName(self) -> StringType: ...
    
    @LocalName.setter
    def LocalName(self, value: StringType) -> None: ...
    
    @property
    def Namespace(self) -> StringType: ...
    
    @Namespace.setter
    def Namespace(self, value: StringType) -> None: ...
    
    @property
    def NodeType(self) -> XmlNodeType: ...
    
    @NodeType.setter
    def NodeType(self, value: XmlNodeType) -> None: ...
    
    @property
    def OriginalStringValue(self) -> StringType: ...
    
    @OriginalStringValue.setter
    def OriginalStringValue(self, value: StringType) -> None: ...
    
    @property
    def Prefix(self) -> StringType: ...
    
    @Prefix.setter
    def Prefix(self, value: StringType) -> None: ...
    
    @property
    def RawValue(self) -> StringType: ...
    
    @RawValue.setter
    def RawValue(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def GetAtomizedNameWPrefix(self, nameTable: XmlNameTable) -> StringType: ...
    
    def get_AttInfo(self) -> AttributePSVIInfo: ...
    
    def get_Depth(self) -> IntType: ...
    
    def get_LineNumber(self) -> IntType: ...
    
    def get_LinePosition(self) -> IntType: ...
    
    def get_LocalName(self) -> StringType: ...
    
    def get_Namespace(self) -> StringType: ...
    
    def get_NodeType(self) -> XmlNodeType: ...
    
    def get_OriginalStringValue(self) -> StringType: ...
    
    def get_Prefix(self) -> StringType: ...
    
    def get_RawValue(self) -> StringType: ...
    
    def set_AttInfo(self, value: AttributePSVIInfo) -> VoidType: ...
    
    def set_Depth(self, value: IntType) -> VoidType: ...
    
    def set_LocalName(self, value: StringType) -> VoidType: ...
    
    def set_Namespace(self, value: StringType) -> VoidType: ...
    
    def set_NodeType(self, value: XmlNodeType) -> VoidType: ...
    
    def set_OriginalStringValue(self, value: StringType) -> VoidType: ...
    
    def set_Prefix(self, value: StringType) -> VoidType: ...
    
    def set_RawValue(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XPathNodeList(XmlNodeList, IEnumerable, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, nodeIterator: XPathNodeIterator): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def GetEnumerator(self) -> IEnumerator: ...
    
    def Item(self, index: IntType) -> XmlNode: ...
    
    def get_Count(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XPathNodeList(XmlNodeList, IEnumerable, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, nodeIterator: XPathNodeIterator): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def GetEnumerator(self) -> IEnumerator: ...
    
    def Item(self, index: IntType) -> XmlNode: ...
    
    def get_Count(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlAsyncCheckReader(XmlReader, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, reader: XmlReader): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AttributeCount(self) -> IntType: ...
    
    @property
    def BaseURI(self) -> StringType: ...
    
    @property
    def CanReadBinaryContent(self) -> BooleanType: ...
    
    @property
    def CanReadValueChunk(self) -> BooleanType: ...
    
    @property
    def CanResolveEntity(self) -> BooleanType: ...
    
    @property
    def Depth(self) -> IntType: ...
    
    @property
    def EOF(self) -> BooleanType: ...
    
    @property
    def HasAttributes(self) -> BooleanType: ...
    
    @property
    def HasValue(self) -> BooleanType: ...
    
    @property
    def IsDefault(self) -> BooleanType: ...
    
    @property
    def IsEmptyElement(self) -> BooleanType: ...
    
    def __getitem__(self, key: IntType) -> StringType: ...
    
    def __getitem__(self, key: StringType) -> StringType: ...
    
    def __getitem__(self, key: StringType) -> StringType: ...
    
    @property
    def LocalName(self) -> StringType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def NameTable(self) -> XmlNameTable: ...
    
    @property
    def NamespaceURI(self) -> StringType: ...
    
    @property
    def NodeType(self) -> XmlNodeType: ...
    
    @property
    def Prefix(self) -> StringType: ...
    
    @property
    def QuoteChar(self) -> CharType: ...
    
    @property
    def ReadState(self) -> ReadState: ...
    
    @property
    def SchemaInfo(self) -> IXmlSchemaInfo: ...
    
    @property
    def Settings(self) -> XmlReaderSettings: ...
    
    @property
    def Value(self) -> StringType: ...
    
    @property
    def ValueType(self) -> TypeType: ...
    
    @property
    def XmlLang(self) -> StringType: ...
    
    @property
    def XmlSpace(self) -> XmlSpace: ...
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    @staticmethod
    def CreateAsyncCheckWrapper(reader: XmlReader) -> XmlAsyncCheckReader: ...
    
    @overload
    def GetAttribute(self, name: StringType) -> StringType: ...
    
    @overload
    def GetAttribute(self, name: StringType, namespaceURI: StringType) -> StringType: ...
    
    @overload
    def GetAttribute(self, i: IntType) -> StringType: ...
    
    def GetValueAsync(self) -> Task[StringType]: ...
    
    @overload
    def IsStartElement(self) -> BooleanType: ...
    
    @overload
    def IsStartElement(self, name: StringType) -> BooleanType: ...
    
    @overload
    def IsStartElement(self, localname: StringType, ns: StringType) -> BooleanType: ...
    
    def LookupNamespace(self, prefix: StringType) -> StringType: ...
    
    @overload
    def MoveToAttribute(self, name: StringType) -> BooleanType: ...
    
    @overload
    def MoveToAttribute(self, name: StringType, ns: StringType) -> BooleanType: ...
    
    @overload
    def MoveToAttribute(self, i: IntType) -> VoidType: ...
    
    def MoveToContent(self) -> XmlNodeType: ...
    
    def MoveToContentAsync(self) -> Task[XmlNodeType]: ...
    
    def MoveToElement(self) -> BooleanType: ...
    
    def MoveToFirstAttribute(self) -> BooleanType: ...
    
    def MoveToNextAttribute(self) -> BooleanType: ...
    
    def Read(self) -> BooleanType: ...
    
    def ReadAsync(self) -> Task[BooleanType]: ...
    
    def ReadAttributeValue(self) -> BooleanType: ...
    
    def ReadContentAs(self, returnType: TypeType, namespaceResolver: IXmlNamespaceResolver) -> ObjectType: ...
    
    def ReadContentAsAsync(self, returnType: TypeType, namespaceResolver: IXmlNamespaceResolver) -> Task[ObjectType]: ...
    
    def ReadContentAsBase64(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadContentAsBase64Async(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> Task[IntType]: ...
    
    def ReadContentAsBinHex(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadContentAsBinHexAsync(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> Task[IntType]: ...
    
    def ReadContentAsBoolean(self) -> BooleanType: ...
    
    def ReadContentAsDateTime(self) -> DateTime: ...
    
    def ReadContentAsDateTimeOffset(self) -> DateTimeOffset: ...
    
    def ReadContentAsDecimal(self) -> DecimalType: ...
    
    def ReadContentAsDouble(self) -> DoubleType: ...
    
    def ReadContentAsFloat(self) -> FloatType: ...
    
    def ReadContentAsInt(self) -> IntType: ...
    
    def ReadContentAsLong(self) -> LongType: ...
    
    def ReadContentAsObject(self) -> ObjectType: ...
    
    def ReadContentAsObjectAsync(self) -> Task[ObjectType]: ...
    
    def ReadContentAsString(self) -> StringType: ...
    
    def ReadContentAsStringAsync(self) -> Task[StringType]: ...
    
    @overload
    def ReadElementContentAs(self, returnType: TypeType, namespaceResolver: IXmlNamespaceResolver) -> ObjectType: ...
    
    @overload
    def ReadElementContentAs(self, returnType: TypeType, namespaceResolver: IXmlNamespaceResolver, localName: StringType, namespaceURI: StringType) -> ObjectType: ...
    
    def ReadElementContentAsAsync(self, returnType: TypeType, namespaceResolver: IXmlNamespaceResolver) -> Task[ObjectType]: ...
    
    def ReadElementContentAsBase64(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadElementContentAsBase64Async(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> Task[IntType]: ...
    
    def ReadElementContentAsBinHex(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadElementContentAsBinHexAsync(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> Task[IntType]: ...
    
    @overload
    def ReadElementContentAsBoolean(self) -> BooleanType: ...
    
    @overload
    def ReadElementContentAsBoolean(self, localName: StringType, namespaceURI: StringType) -> BooleanType: ...
    
    @overload
    def ReadElementContentAsDateTime(self) -> DateTime: ...
    
    @overload
    def ReadElementContentAsDateTime(self, localName: StringType, namespaceURI: StringType) -> DateTime: ...
    
    @overload
    def ReadElementContentAsDecimal(self) -> DecimalType: ...
    
    @overload
    def ReadElementContentAsDecimal(self, localName: StringType, namespaceURI: StringType) -> DecimalType: ...
    
    @overload
    def ReadElementContentAsDouble(self) -> DoubleType: ...
    
    @overload
    def ReadElementContentAsDouble(self, localName: StringType, namespaceURI: StringType) -> DoubleType: ...
    
    @overload
    def ReadElementContentAsFloat(self) -> FloatType: ...
    
    @overload
    def ReadElementContentAsFloat(self, localName: StringType, namespaceURI: StringType) -> FloatType: ...
    
    @overload
    def ReadElementContentAsInt(self) -> IntType: ...
    
    @overload
    def ReadElementContentAsInt(self, localName: StringType, namespaceURI: StringType) -> IntType: ...
    
    @overload
    def ReadElementContentAsLong(self) -> LongType: ...
    
    @overload
    def ReadElementContentAsLong(self, localName: StringType, namespaceURI: StringType) -> LongType: ...
    
    @overload
    def ReadElementContentAsObject(self) -> ObjectType: ...
    
    @overload
    def ReadElementContentAsObject(self, localName: StringType, namespaceURI: StringType) -> ObjectType: ...
    
    def ReadElementContentAsObjectAsync(self) -> Task[ObjectType]: ...
    
    @overload
    def ReadElementContentAsString(self) -> StringType: ...
    
    @overload
    def ReadElementContentAsString(self, localName: StringType, namespaceURI: StringType) -> StringType: ...
    
    def ReadElementContentAsStringAsync(self) -> Task[StringType]: ...
    
    @overload
    def ReadElementString(self) -> StringType: ...
    
    @overload
    def ReadElementString(self, name: StringType) -> StringType: ...
    
    @overload
    def ReadElementString(self, localname: StringType, ns: StringType) -> StringType: ...
    
    def ReadEndElement(self) -> VoidType: ...
    
    def ReadInnerXml(self) -> StringType: ...
    
    def ReadInnerXmlAsync(self) -> Task[StringType]: ...
    
    def ReadOuterXml(self) -> StringType: ...
    
    def ReadOuterXmlAsync(self) -> Task[StringType]: ...
    
    @overload
    def ReadStartElement(self) -> VoidType: ...
    
    @overload
    def ReadStartElement(self, name: StringType) -> VoidType: ...
    
    @overload
    def ReadStartElement(self, localname: StringType, ns: StringType) -> VoidType: ...
    
    def ReadString(self) -> StringType: ...
    
    def ReadSubtree(self) -> XmlReader: ...
    
    @overload
    def ReadToDescendant(self, name: StringType) -> BooleanType: ...
    
    @overload
    def ReadToDescendant(self, localName: StringType, namespaceURI: StringType) -> BooleanType: ...
    
    @overload
    def ReadToFollowing(self, name: StringType) -> BooleanType: ...
    
    @overload
    def ReadToFollowing(self, localName: StringType, namespaceURI: StringType) -> BooleanType: ...
    
    @overload
    def ReadToNextSibling(self, name: StringType) -> BooleanType: ...
    
    @overload
    def ReadToNextSibling(self, localName: StringType, namespaceURI: StringType) -> BooleanType: ...
    
    def ReadValueChunk(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadValueChunkAsync(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> Task[IntType]: ...
    
    def ResolveEntity(self) -> VoidType: ...
    
    def Skip(self) -> VoidType: ...
    
    def SkipAsync(self) -> Task: ...
    
    def get_AttributeCount(self) -> IntType: ...
    
    def get_BaseURI(self) -> StringType: ...
    
    def get_CanReadBinaryContent(self) -> BooleanType: ...
    
    def get_CanReadValueChunk(self) -> BooleanType: ...
    
    def get_CanResolveEntity(self) -> BooleanType: ...
    
    def get_Depth(self) -> IntType: ...
    
    def get_EOF(self) -> BooleanType: ...
    
    def get_HasAttributes(self) -> BooleanType: ...
    
    def get_HasValue(self) -> BooleanType: ...
    
    def get_IsDefault(self) -> BooleanType: ...
    
    def get_IsEmptyElement(self) -> BooleanType: ...
    
    @overload
    def get_Item(self, i: IntType) -> StringType: ...
    
    @overload
    def get_Item(self, name: StringType) -> StringType: ...
    
    @overload
    def get_Item(self, name: StringType, namespaceURI: StringType) -> StringType: ...
    
    def get_LocalName(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_NameTable(self) -> XmlNameTable: ...
    
    def get_NamespaceURI(self) -> StringType: ...
    
    def get_NodeType(self) -> XmlNodeType: ...
    
    def get_Prefix(self) -> StringType: ...
    
    def get_QuoteChar(self) -> CharType: ...
    
    def get_ReadState(self) -> ReadState: ...
    
    def get_SchemaInfo(self) -> IXmlSchemaInfo: ...
    
    def get_Settings(self) -> XmlReaderSettings: ...
    
    def get_Value(self) -> StringType: ...
    
    def get_ValueType(self) -> TypeType: ...
    
    def get_XmlLang(self) -> StringType: ...
    
    def get_XmlSpace(self) -> XmlSpace: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlAsyncCheckReader(XmlReader, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, reader: XmlReader): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AttributeCount(self) -> IntType: ...
    
    @property
    def BaseURI(self) -> StringType: ...
    
    @property
    def CanReadBinaryContent(self) -> BooleanType: ...
    
    @property
    def CanReadValueChunk(self) -> BooleanType: ...
    
    @property
    def CanResolveEntity(self) -> BooleanType: ...
    
    @property
    def Depth(self) -> IntType: ...
    
    @property
    def EOF(self) -> BooleanType: ...
    
    @property
    def HasAttributes(self) -> BooleanType: ...
    
    @property
    def HasValue(self) -> BooleanType: ...
    
    @property
    def IsDefault(self) -> BooleanType: ...
    
    @property
    def IsEmptyElement(self) -> BooleanType: ...
    
    def __getitem__(self, key: IntType) -> StringType: ...
    
    def __getitem__(self, key: StringType) -> StringType: ...
    
    def __getitem__(self, key: StringType) -> StringType: ...
    
    @property
    def LocalName(self) -> StringType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def NameTable(self) -> XmlNameTable: ...
    
    @property
    def NamespaceURI(self) -> StringType: ...
    
    @property
    def NodeType(self) -> XmlNodeType: ...
    
    @property
    def Prefix(self) -> StringType: ...
    
    @property
    def QuoteChar(self) -> CharType: ...
    
    @property
    def ReadState(self) -> ReadState: ...
    
    @property
    def SchemaInfo(self) -> IXmlSchemaInfo: ...
    
    @property
    def Settings(self) -> XmlReaderSettings: ...
    
    @property
    def Value(self) -> StringType: ...
    
    @property
    def ValueType(self) -> TypeType: ...
    
    @property
    def XmlLang(self) -> StringType: ...
    
    @property
    def XmlSpace(self) -> XmlSpace: ...
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    @staticmethod
    def CreateAsyncCheckWrapper(reader: XmlReader) -> XmlAsyncCheckReader: ...
    
    @overload
    def GetAttribute(self, name: StringType) -> StringType: ...
    
    @overload
    def GetAttribute(self, name: StringType, namespaceURI: StringType) -> StringType: ...
    
    @overload
    def GetAttribute(self, i: IntType) -> StringType: ...
    
    def GetValueAsync(self) -> Task[StringType]: ...
    
    @overload
    def IsStartElement(self) -> BooleanType: ...
    
    @overload
    def IsStartElement(self, name: StringType) -> BooleanType: ...
    
    @overload
    def IsStartElement(self, localname: StringType, ns: StringType) -> BooleanType: ...
    
    def LookupNamespace(self, prefix: StringType) -> StringType: ...
    
    @overload
    def MoveToAttribute(self, name: StringType) -> BooleanType: ...
    
    @overload
    def MoveToAttribute(self, name: StringType, ns: StringType) -> BooleanType: ...
    
    @overload
    def MoveToAttribute(self, i: IntType) -> VoidType: ...
    
    def MoveToContent(self) -> XmlNodeType: ...
    
    def MoveToContentAsync(self) -> Task[XmlNodeType]: ...
    
    def MoveToElement(self) -> BooleanType: ...
    
    def MoveToFirstAttribute(self) -> BooleanType: ...
    
    def MoveToNextAttribute(self) -> BooleanType: ...
    
    def Read(self) -> BooleanType: ...
    
    def ReadAsync(self) -> Task[BooleanType]: ...
    
    def ReadAttributeValue(self) -> BooleanType: ...
    
    def ReadContentAs(self, returnType: TypeType, namespaceResolver: IXmlNamespaceResolver) -> ObjectType: ...
    
    def ReadContentAsAsync(self, returnType: TypeType, namespaceResolver: IXmlNamespaceResolver) -> Task[ObjectType]: ...
    
    def ReadContentAsBase64(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadContentAsBase64Async(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> Task[IntType]: ...
    
    def ReadContentAsBinHex(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadContentAsBinHexAsync(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> Task[IntType]: ...
    
    def ReadContentAsBoolean(self) -> BooleanType: ...
    
    def ReadContentAsDateTime(self) -> DateTime: ...
    
    def ReadContentAsDateTimeOffset(self) -> DateTimeOffset: ...
    
    def ReadContentAsDecimal(self) -> DecimalType: ...
    
    def ReadContentAsDouble(self) -> DoubleType: ...
    
    def ReadContentAsFloat(self) -> FloatType: ...
    
    def ReadContentAsInt(self) -> IntType: ...
    
    def ReadContentAsLong(self) -> LongType: ...
    
    def ReadContentAsObject(self) -> ObjectType: ...
    
    def ReadContentAsObjectAsync(self) -> Task[ObjectType]: ...
    
    def ReadContentAsString(self) -> StringType: ...
    
    def ReadContentAsStringAsync(self) -> Task[StringType]: ...
    
    @overload
    def ReadElementContentAs(self, returnType: TypeType, namespaceResolver: IXmlNamespaceResolver) -> ObjectType: ...
    
    @overload
    def ReadElementContentAs(self, returnType: TypeType, namespaceResolver: IXmlNamespaceResolver, localName: StringType, namespaceURI: StringType) -> ObjectType: ...
    
    def ReadElementContentAsAsync(self, returnType: TypeType, namespaceResolver: IXmlNamespaceResolver) -> Task[ObjectType]: ...
    
    def ReadElementContentAsBase64(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadElementContentAsBase64Async(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> Task[IntType]: ...
    
    def ReadElementContentAsBinHex(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadElementContentAsBinHexAsync(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> Task[IntType]: ...
    
    @overload
    def ReadElementContentAsBoolean(self) -> BooleanType: ...
    
    @overload
    def ReadElementContentAsBoolean(self, localName: StringType, namespaceURI: StringType) -> BooleanType: ...
    
    @overload
    def ReadElementContentAsDateTime(self) -> DateTime: ...
    
    @overload
    def ReadElementContentAsDateTime(self, localName: StringType, namespaceURI: StringType) -> DateTime: ...
    
    @overload
    def ReadElementContentAsDecimal(self) -> DecimalType: ...
    
    @overload
    def ReadElementContentAsDecimal(self, localName: StringType, namespaceURI: StringType) -> DecimalType: ...
    
    @overload
    def ReadElementContentAsDouble(self) -> DoubleType: ...
    
    @overload
    def ReadElementContentAsDouble(self, localName: StringType, namespaceURI: StringType) -> DoubleType: ...
    
    @overload
    def ReadElementContentAsFloat(self) -> FloatType: ...
    
    @overload
    def ReadElementContentAsFloat(self, localName: StringType, namespaceURI: StringType) -> FloatType: ...
    
    @overload
    def ReadElementContentAsInt(self) -> IntType: ...
    
    @overload
    def ReadElementContentAsInt(self, localName: StringType, namespaceURI: StringType) -> IntType: ...
    
    @overload
    def ReadElementContentAsLong(self) -> LongType: ...
    
    @overload
    def ReadElementContentAsLong(self, localName: StringType, namespaceURI: StringType) -> LongType: ...
    
    @overload
    def ReadElementContentAsObject(self) -> ObjectType: ...
    
    @overload
    def ReadElementContentAsObject(self, localName: StringType, namespaceURI: StringType) -> ObjectType: ...
    
    def ReadElementContentAsObjectAsync(self) -> Task[ObjectType]: ...
    
    @overload
    def ReadElementContentAsString(self) -> StringType: ...
    
    @overload
    def ReadElementContentAsString(self, localName: StringType, namespaceURI: StringType) -> StringType: ...
    
    def ReadElementContentAsStringAsync(self) -> Task[StringType]: ...
    
    @overload
    def ReadElementString(self) -> StringType: ...
    
    @overload
    def ReadElementString(self, name: StringType) -> StringType: ...
    
    @overload
    def ReadElementString(self, localname: StringType, ns: StringType) -> StringType: ...
    
    def ReadEndElement(self) -> VoidType: ...
    
    def ReadInnerXml(self) -> StringType: ...
    
    def ReadInnerXmlAsync(self) -> Task[StringType]: ...
    
    def ReadOuterXml(self) -> StringType: ...
    
    def ReadOuterXmlAsync(self) -> Task[StringType]: ...
    
    @overload
    def ReadStartElement(self) -> VoidType: ...
    
    @overload
    def ReadStartElement(self, name: StringType) -> VoidType: ...
    
    @overload
    def ReadStartElement(self, localname: StringType, ns: StringType) -> VoidType: ...
    
    def ReadString(self) -> StringType: ...
    
    def ReadSubtree(self) -> XmlReader: ...
    
    @overload
    def ReadToDescendant(self, name: StringType) -> BooleanType: ...
    
    @overload
    def ReadToDescendant(self, localName: StringType, namespaceURI: StringType) -> BooleanType: ...
    
    @overload
    def ReadToFollowing(self, name: StringType) -> BooleanType: ...
    
    @overload
    def ReadToFollowing(self, localName: StringType, namespaceURI: StringType) -> BooleanType: ...
    
    @overload
    def ReadToNextSibling(self, name: StringType) -> BooleanType: ...
    
    @overload
    def ReadToNextSibling(self, localName: StringType, namespaceURI: StringType) -> BooleanType: ...
    
    def ReadValueChunk(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadValueChunkAsync(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> Task[IntType]: ...
    
    def ResolveEntity(self) -> VoidType: ...
    
    def Skip(self) -> VoidType: ...
    
    def SkipAsync(self) -> Task: ...
    
    def get_AttributeCount(self) -> IntType: ...
    
    def get_BaseURI(self) -> StringType: ...
    
    def get_CanReadBinaryContent(self) -> BooleanType: ...
    
    def get_CanReadValueChunk(self) -> BooleanType: ...
    
    def get_CanResolveEntity(self) -> BooleanType: ...
    
    def get_Depth(self) -> IntType: ...
    
    def get_EOF(self) -> BooleanType: ...
    
    def get_HasAttributes(self) -> BooleanType: ...
    
    def get_HasValue(self) -> BooleanType: ...
    
    def get_IsDefault(self) -> BooleanType: ...
    
    def get_IsEmptyElement(self) -> BooleanType: ...
    
    @overload
    def get_Item(self, i: IntType) -> StringType: ...
    
    @overload
    def get_Item(self, name: StringType) -> StringType: ...
    
    @overload
    def get_Item(self, name: StringType, namespaceURI: StringType) -> StringType: ...
    
    def get_LocalName(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_NameTable(self) -> XmlNameTable: ...
    
    def get_NamespaceURI(self) -> StringType: ...
    
    def get_NodeType(self) -> XmlNodeType: ...
    
    def get_Prefix(self) -> StringType: ...
    
    def get_QuoteChar(self) -> CharType: ...
    
    def get_ReadState(self) -> ReadState: ...
    
    def get_SchemaInfo(self) -> IXmlSchemaInfo: ...
    
    def get_Settings(self) -> XmlReaderSettings: ...
    
    def get_Value(self) -> StringType: ...
    
    def get_ValueType(self) -> TypeType: ...
    
    def get_XmlLang(self) -> StringType: ...
    
    def get_XmlSpace(self) -> XmlSpace: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlAsyncCheckReaderWithLineInfo(XmlAsyncCheckReader, IDisposable, IXmlLineInfo):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, reader: XmlReader): ...
    
    # ---------- Properties ---------- #
    
    @property
    def LineNumber(self) -> IntType: ...
    
    @property
    def LinePosition(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def HasLineInfo(self) -> BooleanType: ...
    
    def get_LineNumber(self) -> IntType: ...
    
    def get_LinePosition(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlAsyncCheckReaderWithLineInfo(XmlAsyncCheckReader, IDisposable, IXmlLineInfo):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, reader: XmlReader): ...
    
    # ---------- Properties ---------- #
    
    @property
    def LineNumber(self) -> IntType: ...
    
    @property
    def LinePosition(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def HasLineInfo(self) -> BooleanType: ...
    
    def get_LineNumber(self) -> IntType: ...
    
    def get_LinePosition(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlAsyncCheckReaderWithLineInfoNS(XmlAsyncCheckReaderWithLineInfo, IDisposable, IXmlLineInfo, IXmlNamespaceResolver):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, reader: XmlReader): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlAsyncCheckReaderWithLineInfoNS(XmlAsyncCheckReaderWithLineInfo, IDisposable, IXmlLineInfo, IXmlNamespaceResolver):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, reader: XmlReader): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlAsyncCheckReaderWithLineInfoNSSchema(XmlAsyncCheckReaderWithLineInfoNS, IDisposable, IXmlLineInfo, IXmlNamespaceResolver, IXmlSchemaInfo):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, reader: XmlReader): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlAsyncCheckReaderWithLineInfoNSSchema(XmlAsyncCheckReaderWithLineInfoNS, IDisposable, IXmlLineInfo, IXmlNamespaceResolver, IXmlSchemaInfo):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, reader: XmlReader): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlAsyncCheckReaderWithNS(XmlAsyncCheckReader, IDisposable, IXmlNamespaceResolver):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, reader: XmlReader): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlAsyncCheckReaderWithNS(XmlAsyncCheckReader, IDisposable, IXmlNamespaceResolver):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, reader: XmlReader): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlAsyncCheckWriter(XmlWriter, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, writer: XmlWriter): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Settings(self) -> XmlWriterSettings: ...
    
    @property
    def WriteState(self) -> WriteState: ...
    
    @property
    def XmlLang(self) -> StringType: ...
    
    @property
    def XmlSpace(self) -> XmlSpace: ...
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    def Flush(self) -> VoidType: ...
    
    def FlushAsync(self) -> Task: ...
    
    def LookupPrefix(self, ns: StringType) -> StringType: ...
    
    def WriteAttributes(self, reader: XmlReader, defattr: BooleanType) -> VoidType: ...
    
    def WriteAttributesAsync(self, reader: XmlReader, defattr: BooleanType) -> Task: ...
    
    def WriteBase64(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> VoidType: ...
    
    def WriteBase64Async(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> Task: ...
    
    def WriteBinHex(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> VoidType: ...
    
    def WriteBinHexAsync(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> Task: ...
    
    def WriteCData(self, text: StringType) -> VoidType: ...
    
    def WriteCDataAsync(self, text: StringType) -> Task: ...
    
    def WriteCharEntity(self, ch: CharType) -> VoidType: ...
    
    def WriteCharEntityAsync(self, ch: CharType) -> Task: ...
    
    def WriteChars(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> VoidType: ...
    
    def WriteCharsAsync(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> Task: ...
    
    def WriteComment(self, text: StringType) -> VoidType: ...
    
    def WriteCommentAsync(self, text: StringType) -> Task: ...
    
    def WriteDocType(self, name: StringType, pubid: StringType, sysid: StringType, subset: StringType) -> VoidType: ...
    
    def WriteDocTypeAsync(self, name: StringType, pubid: StringType, sysid: StringType, subset: StringType) -> Task: ...
    
    def WriteEndAttribute(self) -> VoidType: ...
    
    def WriteEndDocument(self) -> VoidType: ...
    
    def WriteEndDocumentAsync(self) -> Task: ...
    
    def WriteEndElement(self) -> VoidType: ...
    
    def WriteEndElementAsync(self) -> Task: ...
    
    def WriteEntityRef(self, name: StringType) -> VoidType: ...
    
    def WriteEntityRefAsync(self, name: StringType) -> Task: ...
    
    def WriteFullEndElement(self) -> VoidType: ...
    
    def WriteFullEndElementAsync(self) -> Task: ...
    
    def WriteName(self, name: StringType) -> VoidType: ...
    
    def WriteNameAsync(self, name: StringType) -> Task: ...
    
    def WriteNmToken(self, name: StringType) -> VoidType: ...
    
    def WriteNmTokenAsync(self, name: StringType) -> Task: ...
    
    @overload
    def WriteNode(self, reader: XmlReader, defattr: BooleanType) -> VoidType: ...
    
    @overload
    def WriteNode(self, navigator: XPathNavigator, defattr: BooleanType) -> VoidType: ...
    
    @overload
    def WriteNodeAsync(self, reader: XmlReader, defattr: BooleanType) -> Task: ...
    
    @overload
    def WriteNodeAsync(self, navigator: XPathNavigator, defattr: BooleanType) -> Task: ...
    
    def WriteProcessingInstruction(self, name: StringType, text: StringType) -> VoidType: ...
    
    def WriteProcessingInstructionAsync(self, name: StringType, text: StringType) -> Task: ...
    
    def WriteQualifiedName(self, localName: StringType, ns: StringType) -> VoidType: ...
    
    def WriteQualifiedNameAsync(self, localName: StringType, ns: StringType) -> Task: ...
    
    @overload
    def WriteRaw(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> VoidType: ...
    
    @overload
    def WriteRaw(self, data: StringType) -> VoidType: ...
    
    @overload
    def WriteRawAsync(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> Task: ...
    
    @overload
    def WriteRawAsync(self, data: StringType) -> Task: ...
    
    @overload
    def WriteStartAttribute(self, prefix: StringType, localName: StringType, ns: StringType) -> VoidType: ...
    
    @overload
    def WriteStartDocument(self) -> VoidType: ...
    
    @overload
    def WriteStartDocument(self, standalone: BooleanType) -> VoidType: ...
    
    @overload
    def WriteStartDocumentAsync(self) -> Task: ...
    
    @overload
    def WriteStartDocumentAsync(self, standalone: BooleanType) -> Task: ...
    
    @overload
    def WriteStartElement(self, prefix: StringType, localName: StringType, ns: StringType) -> VoidType: ...
    
    def WriteStartElementAsync(self, prefix: StringType, localName: StringType, ns: StringType) -> Task: ...
    
    def WriteString(self, text: StringType) -> VoidType: ...
    
    def WriteStringAsync(self, text: StringType) -> Task: ...
    
    def WriteSurrogateCharEntity(self, lowChar: CharType, highChar: CharType) -> VoidType: ...
    
    def WriteSurrogateCharEntityAsync(self, lowChar: CharType, highChar: CharType) -> Task: ...
    
    @overload
    def WriteValue(self, value: ObjectType) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: StringType) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: BooleanType) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: DateTime) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: DateTimeOffset) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: DoubleType) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: FloatType) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: DecimalType) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: IntType) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: LongType) -> VoidType: ...
    
    def WriteWhitespace(self, ws: StringType) -> VoidType: ...
    
    def WriteWhitespaceAsync(self, ws: StringType) -> Task: ...
    
    def get_Settings(self) -> XmlWriterSettings: ...
    
    def get_WriteState(self) -> WriteState: ...
    
    def get_XmlLang(self) -> StringType: ...
    
    def get_XmlSpace(self) -> XmlSpace: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlAsyncCheckWriter(XmlWriter, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, writer: XmlWriter): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Settings(self) -> XmlWriterSettings: ...
    
    @property
    def WriteState(self) -> WriteState: ...
    
    @property
    def XmlLang(self) -> StringType: ...
    
    @property
    def XmlSpace(self) -> XmlSpace: ...
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    def Flush(self) -> VoidType: ...
    
    def FlushAsync(self) -> Task: ...
    
    def LookupPrefix(self, ns: StringType) -> StringType: ...
    
    def WriteAttributes(self, reader: XmlReader, defattr: BooleanType) -> VoidType: ...
    
    def WriteAttributesAsync(self, reader: XmlReader, defattr: BooleanType) -> Task: ...
    
    def WriteBase64(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> VoidType: ...
    
    def WriteBase64Async(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> Task: ...
    
    def WriteBinHex(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> VoidType: ...
    
    def WriteBinHexAsync(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> Task: ...
    
    def WriteCData(self, text: StringType) -> VoidType: ...
    
    def WriteCDataAsync(self, text: StringType) -> Task: ...
    
    def WriteCharEntity(self, ch: CharType) -> VoidType: ...
    
    def WriteCharEntityAsync(self, ch: CharType) -> Task: ...
    
    def WriteChars(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> VoidType: ...
    
    def WriteCharsAsync(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> Task: ...
    
    def WriteComment(self, text: StringType) -> VoidType: ...
    
    def WriteCommentAsync(self, text: StringType) -> Task: ...
    
    def WriteDocType(self, name: StringType, pubid: StringType, sysid: StringType, subset: StringType) -> VoidType: ...
    
    def WriteDocTypeAsync(self, name: StringType, pubid: StringType, sysid: StringType, subset: StringType) -> Task: ...
    
    def WriteEndAttribute(self) -> VoidType: ...
    
    def WriteEndDocument(self) -> VoidType: ...
    
    def WriteEndDocumentAsync(self) -> Task: ...
    
    def WriteEndElement(self) -> VoidType: ...
    
    def WriteEndElementAsync(self) -> Task: ...
    
    def WriteEntityRef(self, name: StringType) -> VoidType: ...
    
    def WriteEntityRefAsync(self, name: StringType) -> Task: ...
    
    def WriteFullEndElement(self) -> VoidType: ...
    
    def WriteFullEndElementAsync(self) -> Task: ...
    
    def WriteName(self, name: StringType) -> VoidType: ...
    
    def WriteNameAsync(self, name: StringType) -> Task: ...
    
    def WriteNmToken(self, name: StringType) -> VoidType: ...
    
    def WriteNmTokenAsync(self, name: StringType) -> Task: ...
    
    @overload
    def WriteNode(self, reader: XmlReader, defattr: BooleanType) -> VoidType: ...
    
    @overload
    def WriteNode(self, navigator: XPathNavigator, defattr: BooleanType) -> VoidType: ...
    
    @overload
    def WriteNodeAsync(self, reader: XmlReader, defattr: BooleanType) -> Task: ...
    
    @overload
    def WriteNodeAsync(self, navigator: XPathNavigator, defattr: BooleanType) -> Task: ...
    
    def WriteProcessingInstruction(self, name: StringType, text: StringType) -> VoidType: ...
    
    def WriteProcessingInstructionAsync(self, name: StringType, text: StringType) -> Task: ...
    
    def WriteQualifiedName(self, localName: StringType, ns: StringType) -> VoidType: ...
    
    def WriteQualifiedNameAsync(self, localName: StringType, ns: StringType) -> Task: ...
    
    @overload
    def WriteRaw(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> VoidType: ...
    
    @overload
    def WriteRaw(self, data: StringType) -> VoidType: ...
    
    @overload
    def WriteRawAsync(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> Task: ...
    
    @overload
    def WriteRawAsync(self, data: StringType) -> Task: ...
    
    @overload
    def WriteStartAttribute(self, prefix: StringType, localName: StringType, ns: StringType) -> VoidType: ...
    
    @overload
    def WriteStartDocument(self) -> VoidType: ...
    
    @overload
    def WriteStartDocument(self, standalone: BooleanType) -> VoidType: ...
    
    @overload
    def WriteStartDocumentAsync(self) -> Task: ...
    
    @overload
    def WriteStartDocumentAsync(self, standalone: BooleanType) -> Task: ...
    
    @overload
    def WriteStartElement(self, prefix: StringType, localName: StringType, ns: StringType) -> VoidType: ...
    
    def WriteStartElementAsync(self, prefix: StringType, localName: StringType, ns: StringType) -> Task: ...
    
    def WriteString(self, text: StringType) -> VoidType: ...
    
    def WriteStringAsync(self, text: StringType) -> Task: ...
    
    def WriteSurrogateCharEntity(self, lowChar: CharType, highChar: CharType) -> VoidType: ...
    
    def WriteSurrogateCharEntityAsync(self, lowChar: CharType, highChar: CharType) -> Task: ...
    
    @overload
    def WriteValue(self, value: ObjectType) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: StringType) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: BooleanType) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: DateTime) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: DateTimeOffset) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: DoubleType) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: FloatType) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: DecimalType) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: IntType) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: LongType) -> VoidType: ...
    
    def WriteWhitespace(self, ws: StringType) -> VoidType: ...
    
    def WriteWhitespaceAsync(self, ws: StringType) -> Task: ...
    
    def get_Settings(self) -> XmlWriterSettings: ...
    
    def get_WriteState(self) -> WriteState: ...
    
    def get_XmlLang(self) -> StringType: ...
    
    def get_XmlSpace(self) -> XmlSpace: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlAttribute(XmlNode, ICloneable, IEnumerable, IXPathNavigable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def BaseURI(self) -> StringType: ...
    
    @InnerText.setter
    def InnerText(self, value: StringType) -> None: ...
    
    @InnerXml.setter
    def InnerXml(self, value: StringType) -> None: ...
    
    @property
    def LocalName(self) -> StringType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def NamespaceURI(self) -> StringType: ...
    
    @property
    def NodeType(self) -> XmlNodeType: ...
    
    @property
    def OwnerDocument(self) -> XmlDocument: ...
    
    @property
    def OwnerElement(self) -> XmlElement: ...
    
    @property
    def ParentNode(self) -> XmlNode: ...
    
    @property
    def Prefix(self) -> StringType: ...
    
    @Prefix.setter
    def Prefix(self, value: StringType) -> None: ...
    
    @property
    def SchemaInfo(self) -> IXmlSchemaInfo: ...
    
    @property
    def Specified(self) -> BooleanType: ...
    
    @property
    def Value(self) -> StringType: ...
    
    @Value.setter
    def Value(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def AppendChild(self, newChild: XmlNode) -> XmlNode: ...
    
    def CloneNode(self, deep: BooleanType) -> XmlNode: ...
    
    def InsertAfter(self, newChild: XmlNode, refChild: XmlNode) -> XmlNode: ...
    
    def InsertBefore(self, newChild: XmlNode, refChild: XmlNode) -> XmlNode: ...
    
    def PrependChild(self, newChild: XmlNode) -> XmlNode: ...
    
    def RemoveChild(self, oldChild: XmlNode) -> XmlNode: ...
    
    def ReplaceChild(self, newChild: XmlNode, oldChild: XmlNode) -> XmlNode: ...
    
    def WriteContentTo(self, w: XmlWriter) -> VoidType: ...
    
    def WriteTo(self, w: XmlWriter) -> VoidType: ...
    
    def get_BaseURI(self) -> StringType: ...
    
    def get_LocalName(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_NamespaceURI(self) -> StringType: ...
    
    def get_NodeType(self) -> XmlNodeType: ...
    
    def get_OwnerDocument(self) -> XmlDocument: ...
    
    def get_OwnerElement(self) -> XmlElement: ...
    
    def get_ParentNode(self) -> XmlNode: ...
    
    def get_Prefix(self) -> StringType: ...
    
    def get_SchemaInfo(self) -> IXmlSchemaInfo: ...
    
    def get_Specified(self) -> BooleanType: ...
    
    def get_Value(self) -> StringType: ...
    
    def set_InnerText(self, value: StringType) -> VoidType: ...
    
    def set_InnerXml(self, value: StringType) -> VoidType: ...
    
    def set_Prefix(self, value: StringType) -> VoidType: ...
    
    def set_Value(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlAttribute(XmlNode, ICloneable, IEnumerable, IXPathNavigable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def BaseURI(self) -> StringType: ...
    
    @InnerText.setter
    def InnerText(self, value: StringType) -> None: ...
    
    @InnerXml.setter
    def InnerXml(self, value: StringType) -> None: ...
    
    @property
    def LocalName(self) -> StringType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def NamespaceURI(self) -> StringType: ...
    
    @property
    def NodeType(self) -> XmlNodeType: ...
    
    @property
    def OwnerDocument(self) -> XmlDocument: ...
    
    @property
    def OwnerElement(self) -> XmlElement: ...
    
    @property
    def ParentNode(self) -> XmlNode: ...
    
    @property
    def Prefix(self) -> StringType: ...
    
    @Prefix.setter
    def Prefix(self, value: StringType) -> None: ...
    
    @property
    def SchemaInfo(self) -> IXmlSchemaInfo: ...
    
    @property
    def Specified(self) -> BooleanType: ...
    
    @property
    def Value(self) -> StringType: ...
    
    @Value.setter
    def Value(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def AppendChild(self, newChild: XmlNode) -> XmlNode: ...
    
    def CloneNode(self, deep: BooleanType) -> XmlNode: ...
    
    def InsertAfter(self, newChild: XmlNode, refChild: XmlNode) -> XmlNode: ...
    
    def InsertBefore(self, newChild: XmlNode, refChild: XmlNode) -> XmlNode: ...
    
    def PrependChild(self, newChild: XmlNode) -> XmlNode: ...
    
    def RemoveChild(self, oldChild: XmlNode) -> XmlNode: ...
    
    def ReplaceChild(self, newChild: XmlNode, oldChild: XmlNode) -> XmlNode: ...
    
    def WriteContentTo(self, w: XmlWriter) -> VoidType: ...
    
    def WriteTo(self, w: XmlWriter) -> VoidType: ...
    
    def get_BaseURI(self) -> StringType: ...
    
    def get_LocalName(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_NamespaceURI(self) -> StringType: ...
    
    def get_NodeType(self) -> XmlNodeType: ...
    
    def get_OwnerDocument(self) -> XmlDocument: ...
    
    def get_OwnerElement(self) -> XmlElement: ...
    
    def get_ParentNode(self) -> XmlNode: ...
    
    def get_Prefix(self) -> StringType: ...
    
    def get_SchemaInfo(self) -> IXmlSchemaInfo: ...
    
    def get_Specified(self) -> BooleanType: ...
    
    def get_Value(self) -> StringType: ...
    
    def set_InnerText(self, value: StringType) -> VoidType: ...
    
    def set_InnerXml(self, value: StringType) -> VoidType: ...
    
    def set_Prefix(self, value: StringType) -> VoidType: ...
    
    def set_Value(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlAttributeCollection(XmlNamedNodeMap, IEnumerable, ICollection):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def ItemOf(self) -> XmlAttribute: ...
    
    @property
    def ItemOf(self) -> XmlAttribute: ...
    
    @property
    def ItemOf(self) -> XmlAttribute: ...
    
    # ---------- Methods ---------- #
    
    def Append(self, node: XmlAttribute) -> XmlAttribute: ...
    
    def CopyTo(self, array: ArrayType[XmlAttribute], index: IntType) -> VoidType: ...
    
    def InsertAfter(self, newNode: XmlAttribute, refNode: XmlAttribute) -> XmlAttribute: ...
    
    def InsertBefore(self, newNode: XmlAttribute, refNode: XmlAttribute) -> XmlAttribute: ...
    
    def Prepend(self, node: XmlAttribute) -> XmlAttribute: ...
    
    def Remove(self, node: XmlAttribute) -> XmlAttribute: ...
    
    def RemoveAll(self) -> VoidType: ...
    
    def RemoveAt(self, i: IntType) -> XmlAttribute: ...
    
    def SetNamedItem(self, node: XmlNode) -> XmlNode: ...
    
    @overload
    def get_ItemOf(self, i: IntType) -> XmlAttribute: ...
    
    @overload
    def get_ItemOf(self, name: StringType) -> XmlAttribute: ...
    
    @overload
    def get_ItemOf(self, localName: StringType, namespaceURI: StringType) -> XmlAttribute: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlAttributeCollection(XmlNamedNodeMap, IEnumerable, ICollection):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def ItemOf(self) -> XmlAttribute: ...
    
    @property
    def ItemOf(self) -> XmlAttribute: ...
    
    @property
    def ItemOf(self) -> XmlAttribute: ...
    
    # ---------- Methods ---------- #
    
    def Append(self, node: XmlAttribute) -> XmlAttribute: ...
    
    def CopyTo(self, array: ArrayType[XmlAttribute], index: IntType) -> VoidType: ...
    
    def InsertAfter(self, newNode: XmlAttribute, refNode: XmlAttribute) -> XmlAttribute: ...
    
    def InsertBefore(self, newNode: XmlAttribute, refNode: XmlAttribute) -> XmlAttribute: ...
    
    def Prepend(self, node: XmlAttribute) -> XmlAttribute: ...
    
    def Remove(self, node: XmlAttribute) -> XmlAttribute: ...
    
    def RemoveAll(self) -> VoidType: ...
    
    def RemoveAt(self, i: IntType) -> XmlAttribute: ...
    
    def SetNamedItem(self, node: XmlNode) -> XmlNode: ...
    
    @overload
    def get_ItemOf(self, i: IntType) -> XmlAttribute: ...
    
    @overload
    def get_ItemOf(self, name: StringType) -> XmlAttribute: ...
    
    @overload
    def get_ItemOf(self, localName: StringType, namespaceURI: StringType) -> XmlAttribute: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlAutoDetectWriter(XmlRawWriter, IDisposable, IRemovableWriter):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, textWriter: TextWriter, writerSettings: XmlWriterSettings): ...
    
    @overload
    def __init__(self, strm: Stream, writerSettings: XmlWriterSettings): ...
    
    # ---------- Properties ---------- #
    
    @property
    def OnRemoveWriterEvent(self) -> OnRemoveWriter: ...
    
    @OnRemoveWriterEvent.setter
    def OnRemoveWriterEvent(self, value: OnRemoveWriter) -> None: ...
    
    @property
    def Settings(self) -> XmlWriterSettings: ...
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    def Flush(self) -> VoidType: ...
    
    def WriteBase64(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> VoidType: ...
    
    def WriteBinHex(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> VoidType: ...
    
    def WriteCData(self, text: StringType) -> VoidType: ...
    
    def WriteCharEntity(self, ch: CharType) -> VoidType: ...
    
    def WriteChars(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> VoidType: ...
    
    def WriteComment(self, text: StringType) -> VoidType: ...
    
    def WriteDocType(self, name: StringType, pubid: StringType, sysid: StringType, subset: StringType) -> VoidType: ...
    
    def WriteEndAttribute(self) -> VoidType: ...
    
    def WriteEntityRef(self, name: StringType) -> VoidType: ...
    
    def WriteProcessingInstruction(self, name: StringType, text: StringType) -> VoidType: ...
    
    @overload
    def WriteRaw(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> VoidType: ...
    
    @overload
    def WriteRaw(self, data: StringType) -> VoidType: ...
    
    @overload
    def WriteStartAttribute(self, prefix: StringType, localName: StringType, ns: StringType) -> VoidType: ...
    
    @overload
    def WriteStartElement(self, prefix: StringType, localName: StringType, ns: StringType) -> VoidType: ...
    
    def WriteString(self, text: StringType) -> VoidType: ...
    
    def WriteSurrogateCharEntity(self, lowChar: CharType, highChar: CharType) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: ObjectType) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: StringType) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: BooleanType) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: DateTime) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: DateTimeOffset) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: DoubleType) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: FloatType) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: DecimalType) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: IntType) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: LongType) -> VoidType: ...
    
    def WriteWhitespace(self, ws: StringType) -> VoidType: ...
    
    def get_OnRemoveWriterEvent(self) -> OnRemoveWriter: ...
    
    def get_Settings(self) -> XmlWriterSettings: ...
    
    def set_OnRemoveWriterEvent(self, value: OnRemoveWriter) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlAutoDetectWriter(XmlRawWriter, IDisposable, IRemovableWriter):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, textWriter: TextWriter, writerSettings: XmlWriterSettings): ...
    
    @overload
    def __init__(self, strm: Stream, writerSettings: XmlWriterSettings): ...
    
    # ---------- Properties ---------- #
    
    @property
    def OnRemoveWriterEvent(self) -> OnRemoveWriter: ...
    
    @OnRemoveWriterEvent.setter
    def OnRemoveWriterEvent(self, value: OnRemoveWriter) -> None: ...
    
    @property
    def Settings(self) -> XmlWriterSettings: ...
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    def Flush(self) -> VoidType: ...
    
    def WriteBase64(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> VoidType: ...
    
    def WriteBinHex(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> VoidType: ...
    
    def WriteCData(self, text: StringType) -> VoidType: ...
    
    def WriteCharEntity(self, ch: CharType) -> VoidType: ...
    
    def WriteChars(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> VoidType: ...
    
    def WriteComment(self, text: StringType) -> VoidType: ...
    
    def WriteDocType(self, name: StringType, pubid: StringType, sysid: StringType, subset: StringType) -> VoidType: ...
    
    def WriteEndAttribute(self) -> VoidType: ...
    
    def WriteEntityRef(self, name: StringType) -> VoidType: ...
    
    def WriteProcessingInstruction(self, name: StringType, text: StringType) -> VoidType: ...
    
    @overload
    def WriteRaw(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> VoidType: ...
    
    @overload
    def WriteRaw(self, data: StringType) -> VoidType: ...
    
    @overload
    def WriteStartAttribute(self, prefix: StringType, localName: StringType, ns: StringType) -> VoidType: ...
    
    @overload
    def WriteStartElement(self, prefix: StringType, localName: StringType, ns: StringType) -> VoidType: ...
    
    def WriteString(self, text: StringType) -> VoidType: ...
    
    def WriteSurrogateCharEntity(self, lowChar: CharType, highChar: CharType) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: ObjectType) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: StringType) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: BooleanType) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: DateTime) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: DateTimeOffset) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: DoubleType) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: FloatType) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: DecimalType) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: IntType) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: LongType) -> VoidType: ...
    
    def WriteWhitespace(self, ws: StringType) -> VoidType: ...
    
    def get_OnRemoveWriterEvent(self) -> OnRemoveWriter: ...
    
    def get_Settings(self) -> XmlWriterSettings: ...
    
    def set_OnRemoveWriterEvent(self, value: OnRemoveWriter) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlCDataSection(XmlCharacterData, ICloneable, IEnumerable, IXPathNavigable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def LocalName(self) -> StringType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def NodeType(self) -> XmlNodeType: ...
    
    @property
    def ParentNode(self) -> XmlNode: ...
    
    @property
    def PreviousText(self) -> XmlNode: ...
    
    # ---------- Methods ---------- #
    
    def CloneNode(self, deep: BooleanType) -> XmlNode: ...
    
    def WriteContentTo(self, w: XmlWriter) -> VoidType: ...
    
    def WriteTo(self, w: XmlWriter) -> VoidType: ...
    
    def get_LocalName(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_NodeType(self) -> XmlNodeType: ...
    
    def get_ParentNode(self) -> XmlNode: ...
    
    def get_PreviousText(self) -> XmlNode: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlCDataSection(XmlCharacterData, ICloneable, IEnumerable, IXPathNavigable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def LocalName(self) -> StringType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def NodeType(self) -> XmlNodeType: ...
    
    @property
    def ParentNode(self) -> XmlNode: ...
    
    @property
    def PreviousText(self) -> XmlNode: ...
    
    # ---------- Methods ---------- #
    
    def CloneNode(self, deep: BooleanType) -> XmlNode: ...
    
    def WriteContentTo(self, w: XmlWriter) -> VoidType: ...
    
    def WriteTo(self, w: XmlWriter) -> VoidType: ...
    
    def get_LocalName(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_NodeType(self) -> XmlNodeType: ...
    
    def get_ParentNode(self) -> XmlNode: ...
    
    def get_PreviousText(self) -> XmlNode: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlCachedStream(MemoryStream, IDisposable):
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


class XmlCachedStream(MemoryStream, IDisposable):
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


class XmlCharCheckingReader(XmlWrappingReader, IDisposable, IXmlLineInfo):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def CanReadBinaryContent(self) -> BooleanType: ...
    
    @property
    def ReadState(self) -> ReadState: ...
    
    @property
    def Settings(self) -> XmlReaderSettings: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def MoveToAttribute(self, name: StringType) -> BooleanType: ...
    
    @overload
    def MoveToAttribute(self, name: StringType, ns: StringType) -> BooleanType: ...
    
    @overload
    def MoveToAttribute(self, i: IntType) -> VoidType: ...
    
    def MoveToElement(self) -> BooleanType: ...
    
    def MoveToFirstAttribute(self) -> BooleanType: ...
    
    def MoveToNextAttribute(self) -> BooleanType: ...
    
    def Read(self) -> BooleanType: ...
    
    def ReadAsync(self) -> Task[BooleanType]: ...
    
    def ReadAttributeValue(self) -> BooleanType: ...
    
    def ReadContentAsBase64(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadContentAsBase64Async(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> Task[IntType]: ...
    
    def ReadContentAsBinHex(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadContentAsBinHexAsync(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> Task[IntType]: ...
    
    def ReadElementContentAsBase64(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadElementContentAsBase64Async(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> Task[IntType]: ...
    
    def ReadElementContentAsBinHex(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadElementContentAsBinHexAsync(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> Task[IntType]: ...
    
    def get_CanReadBinaryContent(self) -> BooleanType: ...
    
    def get_ReadState(self) -> ReadState: ...
    
    def get_Settings(self) -> XmlReaderSettings: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlCharCheckingReader(XmlWrappingReader, IDisposable, IXmlLineInfo):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def CanReadBinaryContent(self) -> BooleanType: ...
    
    @property
    def ReadState(self) -> ReadState: ...
    
    @property
    def Settings(self) -> XmlReaderSettings: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def MoveToAttribute(self, name: StringType) -> BooleanType: ...
    
    @overload
    def MoveToAttribute(self, name: StringType, ns: StringType) -> BooleanType: ...
    
    @overload
    def MoveToAttribute(self, i: IntType) -> VoidType: ...
    
    def MoveToElement(self) -> BooleanType: ...
    
    def MoveToFirstAttribute(self) -> BooleanType: ...
    
    def MoveToNextAttribute(self) -> BooleanType: ...
    
    def Read(self) -> BooleanType: ...
    
    def ReadAsync(self) -> Task[BooleanType]: ...
    
    def ReadAttributeValue(self) -> BooleanType: ...
    
    def ReadContentAsBase64(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadContentAsBase64Async(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> Task[IntType]: ...
    
    def ReadContentAsBinHex(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadContentAsBinHexAsync(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> Task[IntType]: ...
    
    def ReadElementContentAsBase64(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadElementContentAsBase64Async(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> Task[IntType]: ...
    
    def ReadElementContentAsBinHex(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadElementContentAsBinHexAsync(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> Task[IntType]: ...
    
    def get_CanReadBinaryContent(self) -> BooleanType: ...
    
    def get_ReadState(self) -> ReadState: ...
    
    def get_Settings(self) -> XmlReaderSettings: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlCharCheckingReaderWithNS(XmlCharCheckingReader, IDisposable, IXmlLineInfo, IXmlNamespaceResolver):
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


class XmlCharCheckingReaderWithNS(XmlCharCheckingReader, IDisposable, IXmlLineInfo, IXmlNamespaceResolver):
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


class XmlCharCheckingWriter(XmlWrappingWriter, IDisposable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Settings(self) -> XmlWriterSettings: ...
    
    # ---------- Methods ---------- #
    
    def WriteCData(self, text: StringType) -> VoidType: ...
    
    def WriteCDataAsync(self, text: StringType) -> Task: ...
    
    def WriteChars(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> VoidType: ...
    
    def WriteCharsAsync(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> Task: ...
    
    def WriteComment(self, text: StringType) -> VoidType: ...
    
    def WriteCommentAsync(self, text: StringType) -> Task: ...
    
    def WriteDocType(self, name: StringType, pubid: StringType, sysid: StringType, subset: StringType) -> VoidType: ...
    
    def WriteDocTypeAsync(self, name: StringType, pubid: StringType, sysid: StringType, subset: StringType) -> Task: ...
    
    def WriteEntityRef(self, name: StringType) -> VoidType: ...
    
    def WriteEntityRefAsync(self, name: StringType) -> Task: ...
    
    def WriteName(self, name: StringType) -> VoidType: ...
    
    def WriteNameAsync(self, name: StringType) -> Task: ...
    
    def WriteNmToken(self, name: StringType) -> VoidType: ...
    
    def WriteNmTokenAsync(self, name: StringType) -> Task: ...
    
    def WriteProcessingInstruction(self, name: StringType, text: StringType) -> VoidType: ...
    
    def WriteProcessingInstructionAsync(self, name: StringType, text: StringType) -> Task: ...
    
    def WriteQualifiedName(self, localName: StringType, ns: StringType) -> VoidType: ...
    
    def WriteQualifiedNameAsync(self, localName: StringType, ns: StringType) -> Task: ...
    
    @overload
    def WriteStartAttribute(self, prefix: StringType, localName: StringType, ns: StringType) -> VoidType: ...
    
    @overload
    def WriteStartElement(self, prefix: StringType, localName: StringType, ns: StringType) -> VoidType: ...
    
    def WriteStartElementAsync(self, prefix: StringType, localName: StringType, ns: StringType) -> Task: ...
    
    def WriteString(self, text: StringType) -> VoidType: ...
    
    def WriteStringAsync(self, text: StringType) -> Task: ...
    
    def WriteSurrogateCharEntity(self, lowChar: CharType, highChar: CharType) -> VoidType: ...
    
    def WriteSurrogateCharEntityAsync(self, lowChar: CharType, highChar: CharType) -> Task: ...
    
    def WriteWhitespace(self, ws: StringType) -> VoidType: ...
    
    def WriteWhitespaceAsync(self, ws: StringType) -> Task: ...
    
    def get_Settings(self) -> XmlWriterSettings: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlCharCheckingWriter(XmlWrappingWriter, IDisposable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Settings(self) -> XmlWriterSettings: ...
    
    # ---------- Methods ---------- #
    
    def WriteCData(self, text: StringType) -> VoidType: ...
    
    def WriteCDataAsync(self, text: StringType) -> Task: ...
    
    def WriteChars(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> VoidType: ...
    
    def WriteCharsAsync(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> Task: ...
    
    def WriteComment(self, text: StringType) -> VoidType: ...
    
    def WriteCommentAsync(self, text: StringType) -> Task: ...
    
    def WriteDocType(self, name: StringType, pubid: StringType, sysid: StringType, subset: StringType) -> VoidType: ...
    
    def WriteDocTypeAsync(self, name: StringType, pubid: StringType, sysid: StringType, subset: StringType) -> Task: ...
    
    def WriteEntityRef(self, name: StringType) -> VoidType: ...
    
    def WriteEntityRefAsync(self, name: StringType) -> Task: ...
    
    def WriteName(self, name: StringType) -> VoidType: ...
    
    def WriteNameAsync(self, name: StringType) -> Task: ...
    
    def WriteNmToken(self, name: StringType) -> VoidType: ...
    
    def WriteNmTokenAsync(self, name: StringType) -> Task: ...
    
    def WriteProcessingInstruction(self, name: StringType, text: StringType) -> VoidType: ...
    
    def WriteProcessingInstructionAsync(self, name: StringType, text: StringType) -> Task: ...
    
    def WriteQualifiedName(self, localName: StringType, ns: StringType) -> VoidType: ...
    
    def WriteQualifiedNameAsync(self, localName: StringType, ns: StringType) -> Task: ...
    
    @overload
    def WriteStartAttribute(self, prefix: StringType, localName: StringType, ns: StringType) -> VoidType: ...
    
    @overload
    def WriteStartElement(self, prefix: StringType, localName: StringType, ns: StringType) -> VoidType: ...
    
    def WriteStartElementAsync(self, prefix: StringType, localName: StringType, ns: StringType) -> Task: ...
    
    def WriteString(self, text: StringType) -> VoidType: ...
    
    def WriteStringAsync(self, text: StringType) -> Task: ...
    
    def WriteSurrogateCharEntity(self, lowChar: CharType, highChar: CharType) -> VoidType: ...
    
    def WriteSurrogateCharEntityAsync(self, lowChar: CharType, highChar: CharType) -> Task: ...
    
    def WriteWhitespace(self, ws: StringType) -> VoidType: ...
    
    def WriteWhitespaceAsync(self, ws: StringType) -> Task: ...
    
    def get_Settings(self) -> XmlWriterSettings: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlCharacterData(ABC, XmlLinkedNode, ICloneable, IEnumerable, IXPathNavigable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Data(self) -> StringType: ...
    
    @Data.setter
    def Data(self, value: StringType) -> None: ...
    
    @property
    def InnerText(self) -> StringType: ...
    
    @InnerText.setter
    def InnerText(self, value: StringType) -> None: ...
    
    @property
    def Length(self) -> IntType: ...
    
    @property
    def Value(self) -> StringType: ...
    
    @Value.setter
    def Value(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def AppendData(self, strData: StringType) -> VoidType: ...
    
    def DeleteData(self, offset: IntType, count: IntType) -> VoidType: ...
    
    def InsertData(self, offset: IntType, strData: StringType) -> VoidType: ...
    
    def ReplaceData(self, offset: IntType, count: IntType, strData: StringType) -> VoidType: ...
    
    def Substring(self, offset: IntType, count: IntType) -> StringType: ...
    
    def get_Data(self) -> StringType: ...
    
    def get_InnerText(self) -> StringType: ...
    
    def get_Length(self) -> IntType: ...
    
    def get_Value(self) -> StringType: ...
    
    def set_Data(self, value: StringType) -> VoidType: ...
    
    def set_InnerText(self, value: StringType) -> VoidType: ...
    
    def set_Value(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlCharacterData(ABC, XmlLinkedNode, ICloneable, IEnumerable, IXPathNavigable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Data(self) -> StringType: ...
    
    @Data.setter
    def Data(self, value: StringType) -> None: ...
    
    @property
    def InnerText(self) -> StringType: ...
    
    @InnerText.setter
    def InnerText(self, value: StringType) -> None: ...
    
    @property
    def Length(self) -> IntType: ...
    
    @property
    def Value(self) -> StringType: ...
    
    @Value.setter
    def Value(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def AppendData(self, strData: StringType) -> VoidType: ...
    
    def DeleteData(self, offset: IntType, count: IntType) -> VoidType: ...
    
    def InsertData(self, offset: IntType, strData: StringType) -> VoidType: ...
    
    def ReplaceData(self, offset: IntType, count: IntType, strData: StringType) -> VoidType: ...
    
    def Substring(self, offset: IntType, count: IntType) -> StringType: ...
    
    def get_Data(self) -> StringType: ...
    
    def get_InnerText(self) -> StringType: ...
    
    def get_Length(self) -> IntType: ...
    
    def get_Value(self) -> StringType: ...
    
    def set_Data(self, value: StringType) -> VoidType: ...
    
    def set_InnerText(self, value: StringType) -> VoidType: ...
    
    def set_Value(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlChildEnumerator(ObjectType, IEnumerator):
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


class XmlChildEnumerator(ObjectType, IEnumerator):
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


class XmlChildNodes(XmlNodeList, IEnumerable, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, container: XmlNode): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def GetEnumerator(self) -> IEnumerator: ...
    
    def Item(self, i: IntType) -> XmlNode: ...
    
    def get_Count(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlChildNodes(XmlNodeList, IEnumerable, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, container: XmlNode): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def GetEnumerator(self) -> IEnumerator: ...
    
    def Item(self, i: IntType) -> XmlNode: ...
    
    def get_Count(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlComment(XmlCharacterData, ICloneable, IEnumerable, IXPathNavigable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def LocalName(self) -> StringType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def NodeType(self) -> XmlNodeType: ...
    
    # ---------- Methods ---------- #
    
    def CloneNode(self, deep: BooleanType) -> XmlNode: ...
    
    def WriteContentTo(self, w: XmlWriter) -> VoidType: ...
    
    def WriteTo(self, w: XmlWriter) -> VoidType: ...
    
    def get_LocalName(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_NodeType(self) -> XmlNodeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlComment(XmlCharacterData, ICloneable, IEnumerable, IXPathNavigable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def LocalName(self) -> StringType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def NodeType(self) -> XmlNodeType: ...
    
    # ---------- Methods ---------- #
    
    def CloneNode(self, deep: BooleanType) -> XmlNode: ...
    
    def WriteContentTo(self, w: XmlWriter) -> VoidType: ...
    
    def WriteTo(self, w: XmlWriter) -> VoidType: ...
    
    def get_LocalName(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_NodeType(self) -> XmlNodeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlComplianceUtil(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def CDataNormalize(value: StringType) -> StringType: ...
    
    @staticmethod
    def IsValidLanguageID(value: ArrayType[CharType], startPos: IntType, length: IntType) -> BooleanType: ...
    
    @staticmethod
    def NonCDataNormalize(value: StringType) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlComplianceUtil(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def CDataNormalize(value: StringType) -> StringType: ...
    
    @staticmethod
    def IsValidLanguageID(value: ArrayType[CharType], startPos: IntType, length: IntType) -> BooleanType: ...
    
    @staticmethod
    def NonCDataNormalize(value: StringType) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlConvert(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def DecodeName(name: StringType) -> StringType: ...
    
    @staticmethod
    def EncodeLocalName(name: StringType) -> StringType: ...
    
    @staticmethod
    def EncodeName(name: StringType) -> StringType: ...
    
    @staticmethod
    def EncodeNmToken(name: StringType) -> StringType: ...
    
    @staticmethod
    def IsNCNameChar(ch: CharType) -> BooleanType: ...
    
    @staticmethod
    def IsPublicIdChar(ch: CharType) -> BooleanType: ...
    
    @staticmethod
    def IsStartNCNameChar(ch: CharType) -> BooleanType: ...
    
    @staticmethod
    def IsWhitespaceChar(ch: CharType) -> BooleanType: ...
    
    @staticmethod
    def IsXmlChar(ch: CharType) -> BooleanType: ...
    
    @staticmethod
    def IsXmlSurrogatePair(lowChar: CharType, highChar: CharType) -> BooleanType: ...
    
    @staticmethod
    def ToBoolean(s: StringType) -> BooleanType: ...
    
    @staticmethod
    def ToByte(s: StringType) -> ByteType: ...
    
    @staticmethod
    def ToChar(s: StringType) -> CharType: ...
    
    @staticmethod
    @overload
    def ToDateTime(s: StringType) -> DateTime: ...
    
    @staticmethod
    @overload
    def ToDateTime(s: StringType, format: StringType) -> DateTime: ...
    
    @staticmethod
    @overload
    def ToDateTime(s: StringType, formats: ArrayType[StringType]) -> DateTime: ...
    
    @staticmethod
    @overload
    def ToDateTime(s: StringType, dateTimeOption: XmlDateTimeSerializationMode) -> DateTime: ...
    
    @staticmethod
    @overload
    def ToDateTimeOffset(s: StringType) -> DateTimeOffset: ...
    
    @staticmethod
    @overload
    def ToDateTimeOffset(s: StringType, format: StringType) -> DateTimeOffset: ...
    
    @staticmethod
    @overload
    def ToDateTimeOffset(s: StringType, formats: ArrayType[StringType]) -> DateTimeOffset: ...
    
    @staticmethod
    def ToDecimal(s: StringType) -> DecimalType: ...
    
    @staticmethod
    def ToDouble(s: StringType) -> DoubleType: ...
    
    @staticmethod
    def ToGuid(s: StringType) -> Guid: ...
    
    @staticmethod
    def ToInt16(s: StringType) -> ShortType: ...
    
    @staticmethod
    def ToInt32(s: StringType) -> IntType: ...
    
    @staticmethod
    def ToInt64(s: StringType) -> LongType: ...
    
    @staticmethod
    def ToSByte(s: StringType) -> SByteType: ...
    
    @staticmethod
    def ToSingle(s: StringType) -> FloatType: ...
    
    @staticmethod
    @overload
    def ToString(value: CharType) -> StringType: ...
    
    @staticmethod
    @overload
    def ToString(value: DecimalType) -> StringType: ...
    
    @staticmethod
    @overload
    def ToString(value: SByteType) -> StringType: ...
    
    @staticmethod
    @overload
    def ToString(value: ShortType) -> StringType: ...
    
    @staticmethod
    @overload
    def ToString(value: IntType) -> StringType: ...
    
    @staticmethod
    @overload
    def ToString(value: LongType) -> StringType: ...
    
    @staticmethod
    @overload
    def ToString(value: ByteType) -> StringType: ...
    
    @staticmethod
    @overload
    def ToString(value: UShortType) -> StringType: ...
    
    @staticmethod
    @overload
    def ToString(value: UIntType) -> StringType: ...
    
    @staticmethod
    @overload
    def ToString(value: ULongType) -> StringType: ...
    
    @staticmethod
    @overload
    def ToString(value: TimeSpan) -> StringType: ...
    
    @staticmethod
    @overload
    def ToString(value: DateTime, format: StringType) -> StringType: ...
    
    @staticmethod
    @overload
    def ToString(value: DateTimeOffset) -> StringType: ...
    
    @staticmethod
    @overload
    def ToString(value: DateTimeOffset, format: StringType) -> StringType: ...
    
    @staticmethod
    @overload
    def ToString(value: Guid) -> StringType: ...
    
    @staticmethod
    @overload
    def ToString(value: FloatType) -> StringType: ...
    
    @staticmethod
    @overload
    def ToString(value: DoubleType) -> StringType: ...
    
    @staticmethod
    @overload
    def ToString(value: DateTime) -> StringType: ...
    
    @staticmethod
    @overload
    def ToString(value: BooleanType) -> StringType: ...
    
    @staticmethod
    @overload
    def ToString(value: DateTime, dateTimeOption: XmlDateTimeSerializationMode) -> StringType: ...
    
    @staticmethod
    def ToTimeSpan(s: StringType) -> TimeSpan: ...
    
    @staticmethod
    def ToUInt16(s: StringType) -> UShortType: ...
    
    @staticmethod
    def ToUInt32(s: StringType) -> UIntType: ...
    
    @staticmethod
    def ToUInt64(s: StringType) -> ULongType: ...
    
    @staticmethod
    def VerifyNCName(name: StringType) -> StringType: ...
    
    @staticmethod
    def VerifyNMTOKEN(name: StringType) -> StringType: ...
    
    @staticmethod
    def VerifyName(name: StringType) -> StringType: ...
    
    @staticmethod
    def VerifyPublicId(publicId: StringType) -> StringType: ...
    
    @staticmethod
    def VerifyTOKEN(token: StringType) -> StringType: ...
    
    @staticmethod
    def VerifyWhitespace(content: StringType) -> StringType: ...
    
    @staticmethod
    def VerifyXmlChars(content: StringType) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlConvert(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def DecodeName(name: StringType) -> StringType: ...
    
    @staticmethod
    def EncodeLocalName(name: StringType) -> StringType: ...
    
    @staticmethod
    def EncodeName(name: StringType) -> StringType: ...
    
    @staticmethod
    def EncodeNmToken(name: StringType) -> StringType: ...
    
    @staticmethod
    def IsNCNameChar(ch: CharType) -> BooleanType: ...
    
    @staticmethod
    def IsPublicIdChar(ch: CharType) -> BooleanType: ...
    
    @staticmethod
    def IsStartNCNameChar(ch: CharType) -> BooleanType: ...
    
    @staticmethod
    def IsWhitespaceChar(ch: CharType) -> BooleanType: ...
    
    @staticmethod
    def IsXmlChar(ch: CharType) -> BooleanType: ...
    
    @staticmethod
    def IsXmlSurrogatePair(lowChar: CharType, highChar: CharType) -> BooleanType: ...
    
    @staticmethod
    def ToBoolean(s: StringType) -> BooleanType: ...
    
    @staticmethod
    def ToByte(s: StringType) -> ByteType: ...
    
    @staticmethod
    def ToChar(s: StringType) -> CharType: ...
    
    @staticmethod
    @overload
    def ToDateTime(s: StringType) -> DateTime: ...
    
    @staticmethod
    @overload
    def ToDateTime(s: StringType, format: StringType) -> DateTime: ...
    
    @staticmethod
    @overload
    def ToDateTime(s: StringType, formats: ArrayType[StringType]) -> DateTime: ...
    
    @staticmethod
    @overload
    def ToDateTime(s: StringType, dateTimeOption: XmlDateTimeSerializationMode) -> DateTime: ...
    
    @staticmethod
    @overload
    def ToDateTimeOffset(s: StringType) -> DateTimeOffset: ...
    
    @staticmethod
    @overload
    def ToDateTimeOffset(s: StringType, format: StringType) -> DateTimeOffset: ...
    
    @staticmethod
    @overload
    def ToDateTimeOffset(s: StringType, formats: ArrayType[StringType]) -> DateTimeOffset: ...
    
    @staticmethod
    def ToDecimal(s: StringType) -> DecimalType: ...
    
    @staticmethod
    def ToDouble(s: StringType) -> DoubleType: ...
    
    @staticmethod
    def ToGuid(s: StringType) -> Guid: ...
    
    @staticmethod
    def ToInt16(s: StringType) -> ShortType: ...
    
    @staticmethod
    def ToInt32(s: StringType) -> IntType: ...
    
    @staticmethod
    def ToInt64(s: StringType) -> LongType: ...
    
    @staticmethod
    def ToSByte(s: StringType) -> SByteType: ...
    
    @staticmethod
    def ToSingle(s: StringType) -> FloatType: ...
    
    @staticmethod
    @overload
    def ToString(value: CharType) -> StringType: ...
    
    @staticmethod
    @overload
    def ToString(value: DecimalType) -> StringType: ...
    
    @staticmethod
    @overload
    def ToString(value: SByteType) -> StringType: ...
    
    @staticmethod
    @overload
    def ToString(value: ShortType) -> StringType: ...
    
    @staticmethod
    @overload
    def ToString(value: IntType) -> StringType: ...
    
    @staticmethod
    @overload
    def ToString(value: LongType) -> StringType: ...
    
    @staticmethod
    @overload
    def ToString(value: ByteType) -> StringType: ...
    
    @staticmethod
    @overload
    def ToString(value: UShortType) -> StringType: ...
    
    @staticmethod
    @overload
    def ToString(value: UIntType) -> StringType: ...
    
    @staticmethod
    @overload
    def ToString(value: ULongType) -> StringType: ...
    
    @staticmethod
    @overload
    def ToString(value: TimeSpan) -> StringType: ...
    
    @staticmethod
    @overload
    def ToString(value: DateTime, format: StringType) -> StringType: ...
    
    @staticmethod
    @overload
    def ToString(value: DateTimeOffset) -> StringType: ...
    
    @staticmethod
    @overload
    def ToString(value: DateTimeOffset, format: StringType) -> StringType: ...
    
    @staticmethod
    @overload
    def ToString(value: Guid) -> StringType: ...
    
    @staticmethod
    @overload
    def ToString(value: FloatType) -> StringType: ...
    
    @staticmethod
    @overload
    def ToString(value: DoubleType) -> StringType: ...
    
    @staticmethod
    @overload
    def ToString(value: DateTime) -> StringType: ...
    
    @staticmethod
    @overload
    def ToString(value: BooleanType) -> StringType: ...
    
    @staticmethod
    @overload
    def ToString(value: DateTime, dateTimeOption: XmlDateTimeSerializationMode) -> StringType: ...
    
    @staticmethod
    def ToTimeSpan(s: StringType) -> TimeSpan: ...
    
    @staticmethod
    def ToUInt16(s: StringType) -> UShortType: ...
    
    @staticmethod
    def ToUInt32(s: StringType) -> UIntType: ...
    
    @staticmethod
    def ToUInt64(s: StringType) -> ULongType: ...
    
    @staticmethod
    def VerifyNCName(name: StringType) -> StringType: ...
    
    @staticmethod
    def VerifyNMTOKEN(name: StringType) -> StringType: ...
    
    @staticmethod
    def VerifyName(name: StringType) -> StringType: ...
    
    @staticmethod
    def VerifyPublicId(publicId: StringType) -> StringType: ...
    
    @staticmethod
    def VerifyTOKEN(token: StringType) -> StringType: ...
    
    @staticmethod
    def VerifyWhitespace(content: StringType) -> StringType: ...
    
    @staticmethod
    def VerifyXmlChars(content: StringType) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlDOMTextWriter(XmlTextWriter, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, w: Stream, encoding: Encoding): ...
    
    @overload
    def __init__(self, filename: StringType, encoding: Encoding): ...
    
    @overload
    def __init__(self, w: TextWriter): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def WriteStartAttribute(self, prefix: StringType, localName: StringType, ns: StringType) -> VoidType: ...
    
    @overload
    def WriteStartElement(self, prefix: StringType, localName: StringType, ns: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlDOMTextWriter(XmlTextWriter, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, w: Stream, encoding: Encoding): ...
    
    @overload
    def __init__(self, filename: StringType, encoding: Encoding): ...
    
    @overload
    def __init__(self, w: TextWriter): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def WriteStartAttribute(self, prefix: StringType, localName: StringType, ns: StringType) -> VoidType: ...
    
    @overload
    def WriteStartElement(self, prefix: StringType, localName: StringType, ns: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlDeclaration(XmlLinkedNode, ICloneable, IEnumerable, IXPathNavigable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Encoding(self) -> StringType: ...
    
    @Encoding.setter
    def Encoding(self, value: StringType) -> None: ...
    
    @property
    def InnerText(self) -> StringType: ...
    
    @InnerText.setter
    def InnerText(self, value: StringType) -> None: ...
    
    @property
    def LocalName(self) -> StringType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def NodeType(self) -> XmlNodeType: ...
    
    @property
    def Standalone(self) -> StringType: ...
    
    @Standalone.setter
    def Standalone(self, value: StringType) -> None: ...
    
    @property
    def Value(self) -> StringType: ...
    
    @Value.setter
    def Value(self, value: StringType) -> None: ...
    
    @property
    def Version(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def CloneNode(self, deep: BooleanType) -> XmlNode: ...
    
    def WriteContentTo(self, w: XmlWriter) -> VoidType: ...
    
    def WriteTo(self, w: XmlWriter) -> VoidType: ...
    
    def get_Encoding(self) -> StringType: ...
    
    def get_InnerText(self) -> StringType: ...
    
    def get_LocalName(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_NodeType(self) -> XmlNodeType: ...
    
    def get_Standalone(self) -> StringType: ...
    
    def get_Value(self) -> StringType: ...
    
    def get_Version(self) -> StringType: ...
    
    def set_Encoding(self, value: StringType) -> VoidType: ...
    
    def set_InnerText(self, value: StringType) -> VoidType: ...
    
    def set_Standalone(self, value: StringType) -> VoidType: ...
    
    def set_Value(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlDeclaration(XmlLinkedNode, ICloneable, IEnumerable, IXPathNavigable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Encoding(self) -> StringType: ...
    
    @Encoding.setter
    def Encoding(self, value: StringType) -> None: ...
    
    @property
    def InnerText(self) -> StringType: ...
    
    @InnerText.setter
    def InnerText(self, value: StringType) -> None: ...
    
    @property
    def LocalName(self) -> StringType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def NodeType(self) -> XmlNodeType: ...
    
    @property
    def Standalone(self) -> StringType: ...
    
    @Standalone.setter
    def Standalone(self, value: StringType) -> None: ...
    
    @property
    def Value(self) -> StringType: ...
    
    @Value.setter
    def Value(self, value: StringType) -> None: ...
    
    @property
    def Version(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def CloneNode(self, deep: BooleanType) -> XmlNode: ...
    
    def WriteContentTo(self, w: XmlWriter) -> VoidType: ...
    
    def WriteTo(self, w: XmlWriter) -> VoidType: ...
    
    def get_Encoding(self) -> StringType: ...
    
    def get_InnerText(self) -> StringType: ...
    
    def get_LocalName(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_NodeType(self) -> XmlNodeType: ...
    
    def get_Standalone(self) -> StringType: ...
    
    def get_Value(self) -> StringType: ...
    
    def get_Version(self) -> StringType: ...
    
    def set_Encoding(self, value: StringType) -> VoidType: ...
    
    def set_InnerText(self, value: StringType) -> VoidType: ...
    
    def set_Standalone(self, value: StringType) -> VoidType: ...
    
    def set_Value(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlDocument(XmlNode, ICloneable, IEnumerable, IXPathNavigable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, nt: XmlNameTable): ...
    
    # ---------- Properties ---------- #
    
    @property
    def BaseURI(self) -> StringType: ...
    
    @property
    def DocumentElement(self) -> XmlElement: ...
    
    @property
    def DocumentType(self) -> XmlDocumentType: ...
    
    @property
    def Implementation(self) -> XmlImplementation: ...
    
    @InnerText.setter
    def InnerText(self, value: StringType) -> None: ...
    
    @property
    def InnerXml(self) -> StringType: ...
    
    @InnerXml.setter
    def InnerXml(self, value: StringType) -> None: ...
    
    @property
    def IsReadOnly(self) -> BooleanType: ...
    
    @property
    def LocalName(self) -> StringType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def NameTable(self) -> XmlNameTable: ...
    
    @property
    def NodeType(self) -> XmlNodeType: ...
    
    @property
    def OwnerDocument(self) -> XmlDocument: ...
    
    @property
    def ParentNode(self) -> XmlNode: ...
    
    @property
    def PreserveWhitespace(self) -> BooleanType: ...
    
    @PreserveWhitespace.setter
    def PreserveWhitespace(self, value: BooleanType) -> None: ...
    
    @property
    def SchemaInfo(self) -> IXmlSchemaInfo: ...
    
    @property
    def Schemas(self) -> XmlSchemaSet: ...
    
    @Schemas.setter
    def Schemas(self, value: XmlSchemaSet) -> None: ...
    
    @XmlResolver.setter
    def XmlResolver(self, value: XmlResolver) -> None: ...
    
    # ---------- Methods ---------- #
    
    def CloneNode(self, deep: BooleanType) -> XmlNode: ...
    
    @overload
    def CreateAttribute(self, name: StringType) -> XmlAttribute: ...
    
    @overload
    def CreateAttribute(self, qualifiedName: StringType, namespaceURI: StringType) -> XmlAttribute: ...
    
    @overload
    def CreateAttribute(self, prefix: StringType, localName: StringType, namespaceURI: StringType) -> XmlAttribute: ...
    
    def CreateCDataSection(self, data: StringType) -> XmlCDataSection: ...
    
    def CreateComment(self, data: StringType) -> XmlComment: ...
    
    def CreateDocumentFragment(self) -> XmlDocumentFragment: ...
    
    def CreateDocumentType(self, name: StringType, publicId: StringType, systemId: StringType, internalSubset: StringType) -> XmlDocumentType: ...
    
    @overload
    def CreateElement(self, name: StringType) -> XmlElement: ...
    
    @overload
    def CreateElement(self, qualifiedName: StringType, namespaceURI: StringType) -> XmlElement: ...
    
    @overload
    def CreateElement(self, prefix: StringType, localName: StringType, namespaceURI: StringType) -> XmlElement: ...
    
    def CreateEntityReference(self, name: StringType) -> XmlEntityReference: ...
    
    def CreateNavigator(self) -> XPathNavigator: ...
    
    @overload
    def CreateNode(self, nodeTypeString: StringType, name: StringType, namespaceURI: StringType) -> XmlNode: ...
    
    @overload
    def CreateNode(self, type: XmlNodeType, name: StringType, namespaceURI: StringType) -> XmlNode: ...
    
    @overload
    def CreateNode(self, type: XmlNodeType, prefix: StringType, name: StringType, namespaceURI: StringType) -> XmlNode: ...
    
    def CreateProcessingInstruction(self, target: StringType, data: StringType) -> XmlProcessingInstruction: ...
    
    def CreateSignificantWhitespace(self, text: StringType) -> XmlSignificantWhitespace: ...
    
    def CreateTextNode(self, text: StringType) -> XmlText: ...
    
    def CreateWhitespace(self, text: StringType) -> XmlWhitespace: ...
    
    def CreateXmlDeclaration(self, version: StringType, encoding: StringType, standalone: StringType) -> XmlDeclaration: ...
    
    def GetElementById(self, elementId: StringType) -> XmlElement: ...
    
    @overload
    def GetElementsByTagName(self, name: StringType) -> XmlNodeList: ...
    
    @overload
    def GetElementsByTagName(self, localName: StringType, namespaceURI: StringType) -> XmlNodeList: ...
    
    def ImportNode(self, node: XmlNode, deep: BooleanType) -> XmlNode: ...
    
    @overload
    def Load(self, filename: StringType) -> VoidType: ...
    
    @overload
    def Load(self, inStream: Stream) -> VoidType: ...
    
    @overload
    def Load(self, txtReader: TextReader) -> VoidType: ...
    
    @overload
    def Load(self, reader: XmlReader) -> VoidType: ...
    
    def LoadXml(self, xml: StringType) -> VoidType: ...
    
    def ReadNode(self, reader: XmlReader) -> XmlNode: ...
    
    @overload
    def Save(self, filename: StringType) -> VoidType: ...
    
    @overload
    def Save(self, outStream: Stream) -> VoidType: ...
    
    @overload
    def Save(self, writer: TextWriter) -> VoidType: ...
    
    @overload
    def Save(self, w: XmlWriter) -> VoidType: ...
    
    @overload
    def Validate(self, validationEventHandler: ValidationEventHandler) -> VoidType: ...
    
    @overload
    def Validate(self, validationEventHandler: ValidationEventHandler, nodeToValidate: XmlNode) -> VoidType: ...
    
    def WriteContentTo(self, xw: XmlWriter) -> VoidType: ...
    
    def WriteTo(self, w: XmlWriter) -> VoidType: ...
    
    def add_NodeChanged(self, value: XmlNodeChangedEventHandler) -> VoidType: ...
    
    def add_NodeChanging(self, value: XmlNodeChangedEventHandler) -> VoidType: ...
    
    def add_NodeInserted(self, value: XmlNodeChangedEventHandler) -> VoidType: ...
    
    def add_NodeInserting(self, value: XmlNodeChangedEventHandler) -> VoidType: ...
    
    def add_NodeRemoved(self, value: XmlNodeChangedEventHandler) -> VoidType: ...
    
    def add_NodeRemoving(self, value: XmlNodeChangedEventHandler) -> VoidType: ...
    
    def get_BaseURI(self) -> StringType: ...
    
    def get_DocumentElement(self) -> XmlElement: ...
    
    def get_DocumentType(self) -> XmlDocumentType: ...
    
    def get_Implementation(self) -> XmlImplementation: ...
    
    def get_InnerXml(self) -> StringType: ...
    
    def get_IsReadOnly(self) -> BooleanType: ...
    
    def get_LocalName(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_NameTable(self) -> XmlNameTable: ...
    
    def get_NodeType(self) -> XmlNodeType: ...
    
    def get_OwnerDocument(self) -> XmlDocument: ...
    
    def get_ParentNode(self) -> XmlNode: ...
    
    def get_PreserveWhitespace(self) -> BooleanType: ...
    
    def get_SchemaInfo(self) -> IXmlSchemaInfo: ...
    
    def get_Schemas(self) -> XmlSchemaSet: ...
    
    def remove_NodeChanged(self, value: XmlNodeChangedEventHandler) -> VoidType: ...
    
    def remove_NodeChanging(self, value: XmlNodeChangedEventHandler) -> VoidType: ...
    
    def remove_NodeInserted(self, value: XmlNodeChangedEventHandler) -> VoidType: ...
    
    def remove_NodeInserting(self, value: XmlNodeChangedEventHandler) -> VoidType: ...
    
    def remove_NodeRemoved(self, value: XmlNodeChangedEventHandler) -> VoidType: ...
    
    def remove_NodeRemoving(self, value: XmlNodeChangedEventHandler) -> VoidType: ...
    
    def set_InnerText(self, value: StringType) -> VoidType: ...
    
    def set_InnerXml(self, value: StringType) -> VoidType: ...
    
    def set_PreserveWhitespace(self, value: BooleanType) -> VoidType: ...
    
    def set_Schemas(self, value: XmlSchemaSet) -> VoidType: ...
    
    def set_XmlResolver(self, value: XmlResolver) -> VoidType: ...
    
    # ---------- Events ---------- #
    
    NodeChanged: EventType[XmlNodeChangedEventHandler] = ...
    
    NodeChanging: EventType[XmlNodeChangedEventHandler] = ...
    
    NodeInserted: EventType[XmlNodeChangedEventHandler] = ...
    
    NodeInserting: EventType[XmlNodeChangedEventHandler] = ...
    
    NodeRemoved: EventType[XmlNodeChangedEventHandler] = ...
    
    NodeRemoving: EventType[XmlNodeChangedEventHandler] = ...
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlDocument(XmlNode, ICloneable, IEnumerable, IXPathNavigable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, nt: XmlNameTable): ...
    
    # ---------- Properties ---------- #
    
    @property
    def BaseURI(self) -> StringType: ...
    
    @property
    def DocumentElement(self) -> XmlElement: ...
    
    @property
    def DocumentType(self) -> XmlDocumentType: ...
    
    @property
    def Implementation(self) -> XmlImplementation: ...
    
    @InnerText.setter
    def InnerText(self, value: StringType) -> None: ...
    
    @property
    def InnerXml(self) -> StringType: ...
    
    @InnerXml.setter
    def InnerXml(self, value: StringType) -> None: ...
    
    @property
    def IsReadOnly(self) -> BooleanType: ...
    
    @property
    def LocalName(self) -> StringType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def NameTable(self) -> XmlNameTable: ...
    
    @property
    def NodeType(self) -> XmlNodeType: ...
    
    @property
    def OwnerDocument(self) -> XmlDocument: ...
    
    @property
    def ParentNode(self) -> XmlNode: ...
    
    @property
    def PreserveWhitespace(self) -> BooleanType: ...
    
    @PreserveWhitespace.setter
    def PreserveWhitespace(self, value: BooleanType) -> None: ...
    
    @property
    def SchemaInfo(self) -> IXmlSchemaInfo: ...
    
    @property
    def Schemas(self) -> XmlSchemaSet: ...
    
    @Schemas.setter
    def Schemas(self, value: XmlSchemaSet) -> None: ...
    
    @XmlResolver.setter
    def XmlResolver(self, value: XmlResolver) -> None: ...
    
    # ---------- Methods ---------- #
    
    def CloneNode(self, deep: BooleanType) -> XmlNode: ...
    
    @overload
    def CreateAttribute(self, name: StringType) -> XmlAttribute: ...
    
    @overload
    def CreateAttribute(self, qualifiedName: StringType, namespaceURI: StringType) -> XmlAttribute: ...
    
    @overload
    def CreateAttribute(self, prefix: StringType, localName: StringType, namespaceURI: StringType) -> XmlAttribute: ...
    
    def CreateCDataSection(self, data: StringType) -> XmlCDataSection: ...
    
    def CreateComment(self, data: StringType) -> XmlComment: ...
    
    def CreateDocumentFragment(self) -> XmlDocumentFragment: ...
    
    def CreateDocumentType(self, name: StringType, publicId: StringType, systemId: StringType, internalSubset: StringType) -> XmlDocumentType: ...
    
    @overload
    def CreateElement(self, name: StringType) -> XmlElement: ...
    
    @overload
    def CreateElement(self, qualifiedName: StringType, namespaceURI: StringType) -> XmlElement: ...
    
    @overload
    def CreateElement(self, prefix: StringType, localName: StringType, namespaceURI: StringType) -> XmlElement: ...
    
    def CreateEntityReference(self, name: StringType) -> XmlEntityReference: ...
    
    def CreateNavigator(self) -> XPathNavigator: ...
    
    @overload
    def CreateNode(self, nodeTypeString: StringType, name: StringType, namespaceURI: StringType) -> XmlNode: ...
    
    @overload
    def CreateNode(self, type: XmlNodeType, name: StringType, namespaceURI: StringType) -> XmlNode: ...
    
    @overload
    def CreateNode(self, type: XmlNodeType, prefix: StringType, name: StringType, namespaceURI: StringType) -> XmlNode: ...
    
    def CreateProcessingInstruction(self, target: StringType, data: StringType) -> XmlProcessingInstruction: ...
    
    def CreateSignificantWhitespace(self, text: StringType) -> XmlSignificantWhitespace: ...
    
    def CreateTextNode(self, text: StringType) -> XmlText: ...
    
    def CreateWhitespace(self, text: StringType) -> XmlWhitespace: ...
    
    def CreateXmlDeclaration(self, version: StringType, encoding: StringType, standalone: StringType) -> XmlDeclaration: ...
    
    def GetElementById(self, elementId: StringType) -> XmlElement: ...
    
    @overload
    def GetElementsByTagName(self, name: StringType) -> XmlNodeList: ...
    
    @overload
    def GetElementsByTagName(self, localName: StringType, namespaceURI: StringType) -> XmlNodeList: ...
    
    def ImportNode(self, node: XmlNode, deep: BooleanType) -> XmlNode: ...
    
    @overload
    def Load(self, filename: StringType) -> VoidType: ...
    
    @overload
    def Load(self, inStream: Stream) -> VoidType: ...
    
    @overload
    def Load(self, txtReader: TextReader) -> VoidType: ...
    
    @overload
    def Load(self, reader: XmlReader) -> VoidType: ...
    
    def LoadXml(self, xml: StringType) -> VoidType: ...
    
    def ReadNode(self, reader: XmlReader) -> XmlNode: ...
    
    @overload
    def Save(self, filename: StringType) -> VoidType: ...
    
    @overload
    def Save(self, outStream: Stream) -> VoidType: ...
    
    @overload
    def Save(self, writer: TextWriter) -> VoidType: ...
    
    @overload
    def Save(self, w: XmlWriter) -> VoidType: ...
    
    @overload
    def Validate(self, validationEventHandler: ValidationEventHandler) -> VoidType: ...
    
    @overload
    def Validate(self, validationEventHandler: ValidationEventHandler, nodeToValidate: XmlNode) -> VoidType: ...
    
    def WriteContentTo(self, xw: XmlWriter) -> VoidType: ...
    
    def WriteTo(self, w: XmlWriter) -> VoidType: ...
    
    def add_NodeChanged(self, value: XmlNodeChangedEventHandler) -> VoidType: ...
    
    def add_NodeChanging(self, value: XmlNodeChangedEventHandler) -> VoidType: ...
    
    def add_NodeInserted(self, value: XmlNodeChangedEventHandler) -> VoidType: ...
    
    def add_NodeInserting(self, value: XmlNodeChangedEventHandler) -> VoidType: ...
    
    def add_NodeRemoved(self, value: XmlNodeChangedEventHandler) -> VoidType: ...
    
    def add_NodeRemoving(self, value: XmlNodeChangedEventHandler) -> VoidType: ...
    
    def get_BaseURI(self) -> StringType: ...
    
    def get_DocumentElement(self) -> XmlElement: ...
    
    def get_DocumentType(self) -> XmlDocumentType: ...
    
    def get_Implementation(self) -> XmlImplementation: ...
    
    def get_InnerXml(self) -> StringType: ...
    
    def get_IsReadOnly(self) -> BooleanType: ...
    
    def get_LocalName(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_NameTable(self) -> XmlNameTable: ...
    
    def get_NodeType(self) -> XmlNodeType: ...
    
    def get_OwnerDocument(self) -> XmlDocument: ...
    
    def get_ParentNode(self) -> XmlNode: ...
    
    def get_PreserveWhitespace(self) -> BooleanType: ...
    
    def get_SchemaInfo(self) -> IXmlSchemaInfo: ...
    
    def get_Schemas(self) -> XmlSchemaSet: ...
    
    def remove_NodeChanged(self, value: XmlNodeChangedEventHandler) -> VoidType: ...
    
    def remove_NodeChanging(self, value: XmlNodeChangedEventHandler) -> VoidType: ...
    
    def remove_NodeInserted(self, value: XmlNodeChangedEventHandler) -> VoidType: ...
    
    def remove_NodeInserting(self, value: XmlNodeChangedEventHandler) -> VoidType: ...
    
    def remove_NodeRemoved(self, value: XmlNodeChangedEventHandler) -> VoidType: ...
    
    def remove_NodeRemoving(self, value: XmlNodeChangedEventHandler) -> VoidType: ...
    
    def set_InnerText(self, value: StringType) -> VoidType: ...
    
    def set_InnerXml(self, value: StringType) -> VoidType: ...
    
    def set_PreserveWhitespace(self, value: BooleanType) -> VoidType: ...
    
    def set_Schemas(self, value: XmlSchemaSet) -> VoidType: ...
    
    def set_XmlResolver(self, value: XmlResolver) -> VoidType: ...
    
    # ---------- Events ---------- #
    
    NodeChanged: EventType[XmlNodeChangedEventHandler] = ...
    
    NodeChanging: EventType[XmlNodeChangedEventHandler] = ...
    
    NodeInserted: EventType[XmlNodeChangedEventHandler] = ...
    
    NodeInserting: EventType[XmlNodeChangedEventHandler] = ...
    
    NodeRemoved: EventType[XmlNodeChangedEventHandler] = ...
    
    NodeRemoving: EventType[XmlNodeChangedEventHandler] = ...
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlDocumentFragment(XmlNode, ICloneable, IEnumerable, IXPathNavigable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def InnerXml(self) -> StringType: ...
    
    @InnerXml.setter
    def InnerXml(self, value: StringType) -> None: ...
    
    @property
    def LocalName(self) -> StringType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def NodeType(self) -> XmlNodeType: ...
    
    @property
    def OwnerDocument(self) -> XmlDocument: ...
    
    @property
    def ParentNode(self) -> XmlNode: ...
    
    # ---------- Methods ---------- #
    
    def CloneNode(self, deep: BooleanType) -> XmlNode: ...
    
    def WriteContentTo(self, w: XmlWriter) -> VoidType: ...
    
    def WriteTo(self, w: XmlWriter) -> VoidType: ...
    
    def get_InnerXml(self) -> StringType: ...
    
    def get_LocalName(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_NodeType(self) -> XmlNodeType: ...
    
    def get_OwnerDocument(self) -> XmlDocument: ...
    
    def get_ParentNode(self) -> XmlNode: ...
    
    def set_InnerXml(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlDocumentFragment(XmlNode, ICloneable, IEnumerable, IXPathNavigable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def InnerXml(self) -> StringType: ...
    
    @InnerXml.setter
    def InnerXml(self, value: StringType) -> None: ...
    
    @property
    def LocalName(self) -> StringType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def NodeType(self) -> XmlNodeType: ...
    
    @property
    def OwnerDocument(self) -> XmlDocument: ...
    
    @property
    def ParentNode(self) -> XmlNode: ...
    
    # ---------- Methods ---------- #
    
    def CloneNode(self, deep: BooleanType) -> XmlNode: ...
    
    def WriteContentTo(self, w: XmlWriter) -> VoidType: ...
    
    def WriteTo(self, w: XmlWriter) -> VoidType: ...
    
    def get_InnerXml(self) -> StringType: ...
    
    def get_LocalName(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_NodeType(self) -> XmlNodeType: ...
    
    def get_OwnerDocument(self) -> XmlDocument: ...
    
    def get_ParentNode(self) -> XmlNode: ...
    
    def set_InnerXml(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlDocumentType(XmlLinkedNode, ICloneable, IEnumerable, IXPathNavigable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Entities(self) -> XmlNamedNodeMap: ...
    
    @property
    def InternalSubset(self) -> StringType: ...
    
    @property
    def IsReadOnly(self) -> BooleanType: ...
    
    @property
    def LocalName(self) -> StringType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def NodeType(self) -> XmlNodeType: ...
    
    @property
    def Notations(self) -> XmlNamedNodeMap: ...
    
    @property
    def PublicId(self) -> StringType: ...
    
    @property
    def SystemId(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def CloneNode(self, deep: BooleanType) -> XmlNode: ...
    
    def WriteContentTo(self, w: XmlWriter) -> VoidType: ...
    
    def WriteTo(self, w: XmlWriter) -> VoidType: ...
    
    def get_Entities(self) -> XmlNamedNodeMap: ...
    
    def get_InternalSubset(self) -> StringType: ...
    
    def get_IsReadOnly(self) -> BooleanType: ...
    
    def get_LocalName(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_NodeType(self) -> XmlNodeType: ...
    
    def get_Notations(self) -> XmlNamedNodeMap: ...
    
    def get_PublicId(self) -> StringType: ...
    
    def get_SystemId(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlDocumentType(XmlLinkedNode, ICloneable, IEnumerable, IXPathNavigable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Entities(self) -> XmlNamedNodeMap: ...
    
    @property
    def InternalSubset(self) -> StringType: ...
    
    @property
    def IsReadOnly(self) -> BooleanType: ...
    
    @property
    def LocalName(self) -> StringType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def NodeType(self) -> XmlNodeType: ...
    
    @property
    def Notations(self) -> XmlNamedNodeMap: ...
    
    @property
    def PublicId(self) -> StringType: ...
    
    @property
    def SystemId(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def CloneNode(self, deep: BooleanType) -> XmlNode: ...
    
    def WriteContentTo(self, w: XmlWriter) -> VoidType: ...
    
    def WriteTo(self, w: XmlWriter) -> VoidType: ...
    
    def get_Entities(self) -> XmlNamedNodeMap: ...
    
    def get_InternalSubset(self) -> StringType: ...
    
    def get_IsReadOnly(self) -> BooleanType: ...
    
    def get_LocalName(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_NodeType(self) -> XmlNodeType: ...
    
    def get_Notations(self) -> XmlNamedNodeMap: ...
    
    def get_PublicId(self) -> StringType: ...
    
    def get_SystemId(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlDownloadManager(ObjectType):
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


class XmlDownloadManager(ObjectType):
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


class XmlElement(XmlLinkedNode, ICloneable, IEnumerable, IXPathNavigable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Attributes(self) -> XmlAttributeCollection: ...
    
    @property
    def HasAttributes(self) -> BooleanType: ...
    
    @property
    def InnerText(self) -> StringType: ...
    
    @InnerText.setter
    def InnerText(self, value: StringType) -> None: ...
    
    @property
    def InnerXml(self) -> StringType: ...
    
    @InnerXml.setter
    def InnerXml(self, value: StringType) -> None: ...
    
    @property
    def IsEmpty(self) -> BooleanType: ...
    
    @IsEmpty.setter
    def IsEmpty(self, value: BooleanType) -> None: ...
    
    @property
    def LocalName(self) -> StringType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def NamespaceURI(self) -> StringType: ...
    
    @property
    def NextSibling(self) -> XmlNode: ...
    
    @property
    def NodeType(self) -> XmlNodeType: ...
    
    @property
    def OwnerDocument(self) -> XmlDocument: ...
    
    @property
    def ParentNode(self) -> XmlNode: ...
    
    @property
    def Prefix(self) -> StringType: ...
    
    @Prefix.setter
    def Prefix(self, value: StringType) -> None: ...
    
    @property
    def SchemaInfo(self) -> IXmlSchemaInfo: ...
    
    # ---------- Methods ---------- #
    
    def CloneNode(self, deep: BooleanType) -> XmlNode: ...
    
    @overload
    def GetAttribute(self, name: StringType) -> StringType: ...
    
    @overload
    def GetAttribute(self, localName: StringType, namespaceURI: StringType) -> StringType: ...
    
    @overload
    def GetAttributeNode(self, name: StringType) -> XmlAttribute: ...
    
    @overload
    def GetAttributeNode(self, localName: StringType, namespaceURI: StringType) -> XmlAttribute: ...
    
    @overload
    def GetElementsByTagName(self, name: StringType) -> XmlNodeList: ...
    
    @overload
    def GetElementsByTagName(self, localName: StringType, namespaceURI: StringType) -> XmlNodeList: ...
    
    @overload
    def HasAttribute(self, name: StringType) -> BooleanType: ...
    
    @overload
    def HasAttribute(self, localName: StringType, namespaceURI: StringType) -> BooleanType: ...
    
    def RemoveAll(self) -> VoidType: ...
    
    def RemoveAllAttributes(self) -> VoidType: ...
    
    @overload
    def RemoveAttribute(self, name: StringType) -> VoidType: ...
    
    @overload
    def RemoveAttribute(self, localName: StringType, namespaceURI: StringType) -> VoidType: ...
    
    def RemoveAttributeAt(self, i: IntType) -> XmlNode: ...
    
    @overload
    def RemoveAttributeNode(self, oldAttr: XmlAttribute) -> XmlAttribute: ...
    
    @overload
    def RemoveAttributeNode(self, localName: StringType, namespaceURI: StringType) -> XmlAttribute: ...
    
    @overload
    def SetAttribute(self, name: StringType, value: StringType) -> VoidType: ...
    
    @overload
    def SetAttribute(self, localName: StringType, namespaceURI: StringType, value: StringType) -> StringType: ...
    
    @overload
    def SetAttributeNode(self, newAttr: XmlAttribute) -> XmlAttribute: ...
    
    @overload
    def SetAttributeNode(self, localName: StringType, namespaceURI: StringType) -> XmlAttribute: ...
    
    def WriteContentTo(self, w: XmlWriter) -> VoidType: ...
    
    def WriteTo(self, w: XmlWriter) -> VoidType: ...
    
    def get_Attributes(self) -> XmlAttributeCollection: ...
    
    def get_HasAttributes(self) -> BooleanType: ...
    
    def get_InnerText(self) -> StringType: ...
    
    def get_InnerXml(self) -> StringType: ...
    
    def get_IsEmpty(self) -> BooleanType: ...
    
    def get_LocalName(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_NamespaceURI(self) -> StringType: ...
    
    def get_NextSibling(self) -> XmlNode: ...
    
    def get_NodeType(self) -> XmlNodeType: ...
    
    def get_OwnerDocument(self) -> XmlDocument: ...
    
    def get_ParentNode(self) -> XmlNode: ...
    
    def get_Prefix(self) -> StringType: ...
    
    def get_SchemaInfo(self) -> IXmlSchemaInfo: ...
    
    def set_InnerText(self, value: StringType) -> VoidType: ...
    
    def set_InnerXml(self, value: StringType) -> VoidType: ...
    
    def set_IsEmpty(self, value: BooleanType) -> VoidType: ...
    
    def set_Prefix(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlElement(XmlLinkedNode, ICloneable, IEnumerable, IXPathNavigable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Attributes(self) -> XmlAttributeCollection: ...
    
    @property
    def HasAttributes(self) -> BooleanType: ...
    
    @property
    def InnerText(self) -> StringType: ...
    
    @InnerText.setter
    def InnerText(self, value: StringType) -> None: ...
    
    @property
    def InnerXml(self) -> StringType: ...
    
    @InnerXml.setter
    def InnerXml(self, value: StringType) -> None: ...
    
    @property
    def IsEmpty(self) -> BooleanType: ...
    
    @IsEmpty.setter
    def IsEmpty(self, value: BooleanType) -> None: ...
    
    @property
    def LocalName(self) -> StringType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def NamespaceURI(self) -> StringType: ...
    
    @property
    def NextSibling(self) -> XmlNode: ...
    
    @property
    def NodeType(self) -> XmlNodeType: ...
    
    @property
    def OwnerDocument(self) -> XmlDocument: ...
    
    @property
    def ParentNode(self) -> XmlNode: ...
    
    @property
    def Prefix(self) -> StringType: ...
    
    @Prefix.setter
    def Prefix(self, value: StringType) -> None: ...
    
    @property
    def SchemaInfo(self) -> IXmlSchemaInfo: ...
    
    # ---------- Methods ---------- #
    
    def CloneNode(self, deep: BooleanType) -> XmlNode: ...
    
    @overload
    def GetAttribute(self, name: StringType) -> StringType: ...
    
    @overload
    def GetAttribute(self, localName: StringType, namespaceURI: StringType) -> StringType: ...
    
    @overload
    def GetAttributeNode(self, name: StringType) -> XmlAttribute: ...
    
    @overload
    def GetAttributeNode(self, localName: StringType, namespaceURI: StringType) -> XmlAttribute: ...
    
    @overload
    def GetElementsByTagName(self, name: StringType) -> XmlNodeList: ...
    
    @overload
    def GetElementsByTagName(self, localName: StringType, namespaceURI: StringType) -> XmlNodeList: ...
    
    @overload
    def HasAttribute(self, name: StringType) -> BooleanType: ...
    
    @overload
    def HasAttribute(self, localName: StringType, namespaceURI: StringType) -> BooleanType: ...
    
    def RemoveAll(self) -> VoidType: ...
    
    def RemoveAllAttributes(self) -> VoidType: ...
    
    @overload
    def RemoveAttribute(self, name: StringType) -> VoidType: ...
    
    @overload
    def RemoveAttribute(self, localName: StringType, namespaceURI: StringType) -> VoidType: ...
    
    def RemoveAttributeAt(self, i: IntType) -> XmlNode: ...
    
    @overload
    def RemoveAttributeNode(self, oldAttr: XmlAttribute) -> XmlAttribute: ...
    
    @overload
    def RemoveAttributeNode(self, localName: StringType, namespaceURI: StringType) -> XmlAttribute: ...
    
    @overload
    def SetAttribute(self, name: StringType, value: StringType) -> VoidType: ...
    
    @overload
    def SetAttribute(self, localName: StringType, namespaceURI: StringType, value: StringType) -> StringType: ...
    
    @overload
    def SetAttributeNode(self, newAttr: XmlAttribute) -> XmlAttribute: ...
    
    @overload
    def SetAttributeNode(self, localName: StringType, namespaceURI: StringType) -> XmlAttribute: ...
    
    def WriteContentTo(self, w: XmlWriter) -> VoidType: ...
    
    def WriteTo(self, w: XmlWriter) -> VoidType: ...
    
    def get_Attributes(self) -> XmlAttributeCollection: ...
    
    def get_HasAttributes(self) -> BooleanType: ...
    
    def get_InnerText(self) -> StringType: ...
    
    def get_InnerXml(self) -> StringType: ...
    
    def get_IsEmpty(self) -> BooleanType: ...
    
    def get_LocalName(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_NamespaceURI(self) -> StringType: ...
    
    def get_NextSibling(self) -> XmlNode: ...
    
    def get_NodeType(self) -> XmlNodeType: ...
    
    def get_OwnerDocument(self) -> XmlDocument: ...
    
    def get_ParentNode(self) -> XmlNode: ...
    
    def get_Prefix(self) -> StringType: ...
    
    def get_SchemaInfo(self) -> IXmlSchemaInfo: ...
    
    def set_InnerText(self, value: StringType) -> VoidType: ...
    
    def set_InnerXml(self, value: StringType) -> VoidType: ...
    
    def set_IsEmpty(self, value: BooleanType) -> VoidType: ...
    
    def set_Prefix(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlElementList(XmlNodeList, IEnumerable, IDisposable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def GetEnumerator(self) -> IEnumerator: ...
    
    def GetNextNode(self, n: XmlNode) -> XmlNode: ...
    
    def Item(self, index: IntType) -> XmlNode: ...
    
    def get_Count(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlElementList(XmlNodeList, IEnumerable, IDisposable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def GetEnumerator(self) -> IEnumerator: ...
    
    def GetNextNode(self, n: XmlNode) -> XmlNode: ...
    
    def Item(self, index: IntType) -> XmlNode: ...
    
    def get_Count(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlElementListEnumerator(ObjectType, IEnumerator):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, list: XmlElementList): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Current(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def MoveNext(self) -> BooleanType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Current(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlElementListEnumerator(ObjectType, IEnumerator):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, list: XmlElementList): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Current(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def MoveNext(self) -> BooleanType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Current(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlElementListListener(ObjectType):
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


class XmlElementListListener(ObjectType):
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


class XmlEmptyElementListEnumerator(ObjectType, IEnumerator):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, list: XmlElementList): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Current(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def MoveNext(self) -> BooleanType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Current(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlEmptyElementListEnumerator(ObjectType, IEnumerator):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, list: XmlElementList): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Current(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def MoveNext(self) -> BooleanType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Current(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlEncodedRawTextWriter(XmlRawWriter, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, writer: TextWriter, settings: XmlWriterSettings): ...
    
    @overload
    def __init__(self, stream: Stream, settings: XmlWriterSettings): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Settings(self) -> XmlWriterSettings: ...
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    def Flush(self) -> VoidType: ...
    
    def FlushAsync(self) -> Task: ...
    
    def WriteCData(self, text: StringType) -> VoidType: ...
    
    def WriteCDataAsync(self, text: StringType) -> Task: ...
    
    def WriteCharEntity(self, ch: CharType) -> VoidType: ...
    
    def WriteCharEntityAsync(self, ch: CharType) -> Task: ...
    
    def WriteChars(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> VoidType: ...
    
    def WriteCharsAsync(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> Task: ...
    
    def WriteComment(self, text: StringType) -> VoidType: ...
    
    def WriteCommentAsync(self, text: StringType) -> Task: ...
    
    def WriteDocType(self, name: StringType, pubid: StringType, sysid: StringType, subset: StringType) -> VoidType: ...
    
    def WriteDocTypeAsync(self, name: StringType, pubid: StringType, sysid: StringType, subset: StringType) -> Task: ...
    
    def WriteEndAttribute(self) -> VoidType: ...
    
    def WriteEntityRef(self, name: StringType) -> VoidType: ...
    
    def WriteEntityRefAsync(self, name: StringType) -> Task: ...
    
    def WriteProcessingInstruction(self, name: StringType, text: StringType) -> VoidType: ...
    
    def WriteProcessingInstructionAsync(self, name: StringType, text: StringType) -> Task: ...
    
    @overload
    def WriteRaw(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> VoidType: ...
    
    @overload
    def WriteRaw(self, data: StringType) -> VoidType: ...
    
    @overload
    def WriteRawAsync(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> Task: ...
    
    @overload
    def WriteRawAsync(self, data: StringType) -> Task: ...
    
    @overload
    def WriteStartAttribute(self, prefix: StringType, localName: StringType, ns: StringType) -> VoidType: ...
    
    @overload
    def WriteStartElement(self, prefix: StringType, localName: StringType, ns: StringType) -> VoidType: ...
    
    def WriteStartElementAsync(self, prefix: StringType, localName: StringType, ns: StringType) -> Task: ...
    
    def WriteString(self, text: StringType) -> VoidType: ...
    
    def WriteStringAsync(self, text: StringType) -> Task: ...
    
    def WriteSurrogateCharEntity(self, lowChar: CharType, highChar: CharType) -> VoidType: ...
    
    def WriteSurrogateCharEntityAsync(self, lowChar: CharType, highChar: CharType) -> Task: ...
    
    def WriteWhitespace(self, ws: StringType) -> VoidType: ...
    
    def WriteWhitespaceAsync(self, ws: StringType) -> Task: ...
    
    def get_Settings(self) -> XmlWriterSettings: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlEncodedRawTextWriter(XmlRawWriter, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, writer: TextWriter, settings: XmlWriterSettings): ...
    
    @overload
    def __init__(self, stream: Stream, settings: XmlWriterSettings): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Settings(self) -> XmlWriterSettings: ...
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    def Flush(self) -> VoidType: ...
    
    def FlushAsync(self) -> Task: ...
    
    def WriteCData(self, text: StringType) -> VoidType: ...
    
    def WriteCDataAsync(self, text: StringType) -> Task: ...
    
    def WriteCharEntity(self, ch: CharType) -> VoidType: ...
    
    def WriteCharEntityAsync(self, ch: CharType) -> Task: ...
    
    def WriteChars(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> VoidType: ...
    
    def WriteCharsAsync(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> Task: ...
    
    def WriteComment(self, text: StringType) -> VoidType: ...
    
    def WriteCommentAsync(self, text: StringType) -> Task: ...
    
    def WriteDocType(self, name: StringType, pubid: StringType, sysid: StringType, subset: StringType) -> VoidType: ...
    
    def WriteDocTypeAsync(self, name: StringType, pubid: StringType, sysid: StringType, subset: StringType) -> Task: ...
    
    def WriteEndAttribute(self) -> VoidType: ...
    
    def WriteEntityRef(self, name: StringType) -> VoidType: ...
    
    def WriteEntityRefAsync(self, name: StringType) -> Task: ...
    
    def WriteProcessingInstruction(self, name: StringType, text: StringType) -> VoidType: ...
    
    def WriteProcessingInstructionAsync(self, name: StringType, text: StringType) -> Task: ...
    
    @overload
    def WriteRaw(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> VoidType: ...
    
    @overload
    def WriteRaw(self, data: StringType) -> VoidType: ...
    
    @overload
    def WriteRawAsync(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> Task: ...
    
    @overload
    def WriteRawAsync(self, data: StringType) -> Task: ...
    
    @overload
    def WriteStartAttribute(self, prefix: StringType, localName: StringType, ns: StringType) -> VoidType: ...
    
    @overload
    def WriteStartElement(self, prefix: StringType, localName: StringType, ns: StringType) -> VoidType: ...
    
    def WriteStartElementAsync(self, prefix: StringType, localName: StringType, ns: StringType) -> Task: ...
    
    def WriteString(self, text: StringType) -> VoidType: ...
    
    def WriteStringAsync(self, text: StringType) -> Task: ...
    
    def WriteSurrogateCharEntity(self, lowChar: CharType, highChar: CharType) -> VoidType: ...
    
    def WriteSurrogateCharEntityAsync(self, lowChar: CharType, highChar: CharType) -> Task: ...
    
    def WriteWhitespace(self, ws: StringType) -> VoidType: ...
    
    def WriteWhitespaceAsync(self, ws: StringType) -> Task: ...
    
    def get_Settings(self) -> XmlWriterSettings: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlEncodedRawTextWriterIndent(XmlEncodedRawTextWriter, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, writer: TextWriter, settings: XmlWriterSettings): ...
    
    @overload
    def __init__(self, stream: Stream, settings: XmlWriterSettings): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Settings(self) -> XmlWriterSettings: ...
    
    # ---------- Methods ---------- #
    
    def WriteBase64(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> VoidType: ...
    
    def WriteBase64Async(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> Task: ...
    
    def WriteCData(self, text: StringType) -> VoidType: ...
    
    def WriteCDataAsync(self, text: StringType) -> Task: ...
    
    def WriteCharEntity(self, ch: CharType) -> VoidType: ...
    
    def WriteCharEntityAsync(self, ch: CharType) -> Task: ...
    
    def WriteChars(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> VoidType: ...
    
    def WriteCharsAsync(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> Task: ...
    
    def WriteComment(self, text: StringType) -> VoidType: ...
    
    def WriteCommentAsync(self, text: StringType) -> Task: ...
    
    def WriteDocType(self, name: StringType, pubid: StringType, sysid: StringType, subset: StringType) -> VoidType: ...
    
    def WriteDocTypeAsync(self, name: StringType, pubid: StringType, sysid: StringType, subset: StringType) -> Task: ...
    
    def WriteEntityRef(self, name: StringType) -> VoidType: ...
    
    def WriteEntityRefAsync(self, name: StringType) -> Task: ...
    
    def WriteProcessingInstruction(self, target: StringType, text: StringType) -> VoidType: ...
    
    def WriteProcessingInstructionAsync(self, target: StringType, text: StringType) -> Task: ...
    
    @overload
    def WriteRaw(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> VoidType: ...
    
    @overload
    def WriteRaw(self, data: StringType) -> VoidType: ...
    
    @overload
    def WriteRawAsync(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> Task: ...
    
    @overload
    def WriteRawAsync(self, data: StringType) -> Task: ...
    
    @overload
    def WriteStartAttribute(self, prefix: StringType, localName: StringType, ns: StringType) -> VoidType: ...
    
    @overload
    def WriteStartElement(self, prefix: StringType, localName: StringType, ns: StringType) -> VoidType: ...
    
    def WriteStartElementAsync(self, prefix: StringType, localName: StringType, ns: StringType) -> Task: ...
    
    def WriteString(self, text: StringType) -> VoidType: ...
    
    def WriteStringAsync(self, text: StringType) -> Task: ...
    
    def WriteSurrogateCharEntity(self, lowChar: CharType, highChar: CharType) -> VoidType: ...
    
    def WriteSurrogateCharEntityAsync(self, lowChar: CharType, highChar: CharType) -> Task: ...
    
    def WriteWhitespace(self, ws: StringType) -> VoidType: ...
    
    def WriteWhitespaceAsync(self, ws: StringType) -> Task: ...
    
    def get_Settings(self) -> XmlWriterSettings: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlEncodedRawTextWriterIndent(XmlEncodedRawTextWriter, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, writer: TextWriter, settings: XmlWriterSettings): ...
    
    @overload
    def __init__(self, stream: Stream, settings: XmlWriterSettings): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Settings(self) -> XmlWriterSettings: ...
    
    # ---------- Methods ---------- #
    
    def WriteBase64(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> VoidType: ...
    
    def WriteBase64Async(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> Task: ...
    
    def WriteCData(self, text: StringType) -> VoidType: ...
    
    def WriteCDataAsync(self, text: StringType) -> Task: ...
    
    def WriteCharEntity(self, ch: CharType) -> VoidType: ...
    
    def WriteCharEntityAsync(self, ch: CharType) -> Task: ...
    
    def WriteChars(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> VoidType: ...
    
    def WriteCharsAsync(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> Task: ...
    
    def WriteComment(self, text: StringType) -> VoidType: ...
    
    def WriteCommentAsync(self, text: StringType) -> Task: ...
    
    def WriteDocType(self, name: StringType, pubid: StringType, sysid: StringType, subset: StringType) -> VoidType: ...
    
    def WriteDocTypeAsync(self, name: StringType, pubid: StringType, sysid: StringType, subset: StringType) -> Task: ...
    
    def WriteEntityRef(self, name: StringType) -> VoidType: ...
    
    def WriteEntityRefAsync(self, name: StringType) -> Task: ...
    
    def WriteProcessingInstruction(self, target: StringType, text: StringType) -> VoidType: ...
    
    def WriteProcessingInstructionAsync(self, target: StringType, text: StringType) -> Task: ...
    
    @overload
    def WriteRaw(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> VoidType: ...
    
    @overload
    def WriteRaw(self, data: StringType) -> VoidType: ...
    
    @overload
    def WriteRawAsync(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> Task: ...
    
    @overload
    def WriteRawAsync(self, data: StringType) -> Task: ...
    
    @overload
    def WriteStartAttribute(self, prefix: StringType, localName: StringType, ns: StringType) -> VoidType: ...
    
    @overload
    def WriteStartElement(self, prefix: StringType, localName: StringType, ns: StringType) -> VoidType: ...
    
    def WriteStartElementAsync(self, prefix: StringType, localName: StringType, ns: StringType) -> Task: ...
    
    def WriteString(self, text: StringType) -> VoidType: ...
    
    def WriteStringAsync(self, text: StringType) -> Task: ...
    
    def WriteSurrogateCharEntity(self, lowChar: CharType, highChar: CharType) -> VoidType: ...
    
    def WriteSurrogateCharEntityAsync(self, lowChar: CharType, highChar: CharType) -> Task: ...
    
    def WriteWhitespace(self, ws: StringType) -> VoidType: ...
    
    def WriteWhitespaceAsync(self, ws: StringType) -> Task: ...
    
    def get_Settings(self) -> XmlWriterSettings: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlEntity(XmlNode, ICloneable, IEnumerable, IXPathNavigable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def BaseURI(self) -> StringType: ...
    
    @property
    def InnerText(self) -> StringType: ...
    
    @InnerText.setter
    def InnerText(self, value: StringType) -> None: ...
    
    @property
    def InnerXml(self) -> StringType: ...
    
    @InnerXml.setter
    def InnerXml(self, value: StringType) -> None: ...
    
    @property
    def IsReadOnly(self) -> BooleanType: ...
    
    @property
    def LocalName(self) -> StringType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def NodeType(self) -> XmlNodeType: ...
    
    @property
    def NotationName(self) -> StringType: ...
    
    @property
    def OuterXml(self) -> StringType: ...
    
    @property
    def PublicId(self) -> StringType: ...
    
    @property
    def SystemId(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def CloneNode(self, deep: BooleanType) -> XmlNode: ...
    
    def WriteContentTo(self, w: XmlWriter) -> VoidType: ...
    
    def WriteTo(self, w: XmlWriter) -> VoidType: ...
    
    def get_BaseURI(self) -> StringType: ...
    
    def get_InnerText(self) -> StringType: ...
    
    def get_InnerXml(self) -> StringType: ...
    
    def get_IsReadOnly(self) -> BooleanType: ...
    
    def get_LocalName(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_NodeType(self) -> XmlNodeType: ...
    
    def get_NotationName(self) -> StringType: ...
    
    def get_OuterXml(self) -> StringType: ...
    
    def get_PublicId(self) -> StringType: ...
    
    def get_SystemId(self) -> StringType: ...
    
    def set_InnerText(self, value: StringType) -> VoidType: ...
    
    def set_InnerXml(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlEntity(XmlNode, ICloneable, IEnumerable, IXPathNavigable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def BaseURI(self) -> StringType: ...
    
    @property
    def InnerText(self) -> StringType: ...
    
    @InnerText.setter
    def InnerText(self, value: StringType) -> None: ...
    
    @property
    def InnerXml(self) -> StringType: ...
    
    @InnerXml.setter
    def InnerXml(self, value: StringType) -> None: ...
    
    @property
    def IsReadOnly(self) -> BooleanType: ...
    
    @property
    def LocalName(self) -> StringType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def NodeType(self) -> XmlNodeType: ...
    
    @property
    def NotationName(self) -> StringType: ...
    
    @property
    def OuterXml(self) -> StringType: ...
    
    @property
    def PublicId(self) -> StringType: ...
    
    @property
    def SystemId(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def CloneNode(self, deep: BooleanType) -> XmlNode: ...
    
    def WriteContentTo(self, w: XmlWriter) -> VoidType: ...
    
    def WriteTo(self, w: XmlWriter) -> VoidType: ...
    
    def get_BaseURI(self) -> StringType: ...
    
    def get_InnerText(self) -> StringType: ...
    
    def get_InnerXml(self) -> StringType: ...
    
    def get_IsReadOnly(self) -> BooleanType: ...
    
    def get_LocalName(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_NodeType(self) -> XmlNodeType: ...
    
    def get_NotationName(self) -> StringType: ...
    
    def get_OuterXml(self) -> StringType: ...
    
    def get_PublicId(self) -> StringType: ...
    
    def get_SystemId(self) -> StringType: ...
    
    def set_InnerText(self, value: StringType) -> VoidType: ...
    
    def set_InnerXml(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlEntityReference(XmlLinkedNode, ICloneable, IEnumerable, IXPathNavigable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def BaseURI(self) -> StringType: ...
    
    @property
    def IsReadOnly(self) -> BooleanType: ...
    
    @property
    def LocalName(self) -> StringType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def NodeType(self) -> XmlNodeType: ...
    
    @property
    def Value(self) -> StringType: ...
    
    @Value.setter
    def Value(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def CloneNode(self, deep: BooleanType) -> XmlNode: ...
    
    def WriteContentTo(self, w: XmlWriter) -> VoidType: ...
    
    def WriteTo(self, w: XmlWriter) -> VoidType: ...
    
    def get_BaseURI(self) -> StringType: ...
    
    def get_IsReadOnly(self) -> BooleanType: ...
    
    def get_LocalName(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_NodeType(self) -> XmlNodeType: ...
    
    def get_Value(self) -> StringType: ...
    
    def set_Value(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlEntityReference(XmlLinkedNode, ICloneable, IEnumerable, IXPathNavigable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def BaseURI(self) -> StringType: ...
    
    @property
    def IsReadOnly(self) -> BooleanType: ...
    
    @property
    def LocalName(self) -> StringType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def NodeType(self) -> XmlNodeType: ...
    
    @property
    def Value(self) -> StringType: ...
    
    @Value.setter
    def Value(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def CloneNode(self, deep: BooleanType) -> XmlNode: ...
    
    def WriteContentTo(self, w: XmlWriter) -> VoidType: ...
    
    def WriteTo(self, w: XmlWriter) -> VoidType: ...
    
    def get_BaseURI(self) -> StringType: ...
    
    def get_IsReadOnly(self) -> BooleanType: ...
    
    def get_LocalName(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_NodeType(self) -> XmlNodeType: ...
    
    def get_Value(self) -> StringType: ...
    
    def set_Value(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlEventCache(XmlRawWriter, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, baseUri: StringType, hasRootNode: BooleanType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def BaseUri(self) -> StringType: ...
    
    @property
    def HasRootNode(self) -> BooleanType: ...
    
    @property
    def Settings(self) -> XmlWriterSettings: ...
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    def EndEvents(self) -> VoidType: ...
    
    def EventsToString(self) -> StringType: ...
    
    def EventsToWriter(self, writer: XmlWriter) -> VoidType: ...
    
    def Flush(self) -> VoidType: ...
    
    def WriteBase64(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> VoidType: ...
    
    def WriteBinHex(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> VoidType: ...
    
    def WriteCData(self, text: StringType) -> VoidType: ...
    
    def WriteCharEntity(self, ch: CharType) -> VoidType: ...
    
    def WriteChars(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> VoidType: ...
    
    def WriteComment(self, text: StringType) -> VoidType: ...
    
    def WriteDocType(self, name: StringType, pubid: StringType, sysid: StringType, subset: StringType) -> VoidType: ...
    
    def WriteEndAttribute(self) -> VoidType: ...
    
    def WriteEntityRef(self, name: StringType) -> VoidType: ...
    
    def WriteProcessingInstruction(self, name: StringType, text: StringType) -> VoidType: ...
    
    @overload
    def WriteRaw(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> VoidType: ...
    
    @overload
    def WriteRaw(self, data: StringType) -> VoidType: ...
    
    @overload
    def WriteStartAttribute(self, prefix: StringType, localName: StringType, ns: StringType) -> VoidType: ...
    
    @overload
    def WriteStartElement(self, prefix: StringType, localName: StringType, ns: StringType) -> VoidType: ...
    
    def WriteString(self, text: StringType) -> VoidType: ...
    
    def WriteSurrogateCharEntity(self, lowChar: CharType, highChar: CharType) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: ObjectType) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: StringType) -> VoidType: ...
    
    def WriteWhitespace(self, ws: StringType) -> VoidType: ...
    
    def get_BaseUri(self) -> StringType: ...
    
    def get_HasRootNode(self) -> BooleanType: ...
    
    def get_Settings(self) -> XmlWriterSettings: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlEventCache(XmlRawWriter, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, baseUri: StringType, hasRootNode: BooleanType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def BaseUri(self) -> StringType: ...
    
    @property
    def HasRootNode(self) -> BooleanType: ...
    
    @property
    def Settings(self) -> XmlWriterSettings: ...
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    def EndEvents(self) -> VoidType: ...
    
    def EventsToString(self) -> StringType: ...
    
    def EventsToWriter(self, writer: XmlWriter) -> VoidType: ...
    
    def Flush(self) -> VoidType: ...
    
    def WriteBase64(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> VoidType: ...
    
    def WriteBinHex(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> VoidType: ...
    
    def WriteCData(self, text: StringType) -> VoidType: ...
    
    def WriteCharEntity(self, ch: CharType) -> VoidType: ...
    
    def WriteChars(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> VoidType: ...
    
    def WriteComment(self, text: StringType) -> VoidType: ...
    
    def WriteDocType(self, name: StringType, pubid: StringType, sysid: StringType, subset: StringType) -> VoidType: ...
    
    def WriteEndAttribute(self) -> VoidType: ...
    
    def WriteEntityRef(self, name: StringType) -> VoidType: ...
    
    def WriteProcessingInstruction(self, name: StringType, text: StringType) -> VoidType: ...
    
    @overload
    def WriteRaw(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> VoidType: ...
    
    @overload
    def WriteRaw(self, data: StringType) -> VoidType: ...
    
    @overload
    def WriteStartAttribute(self, prefix: StringType, localName: StringType, ns: StringType) -> VoidType: ...
    
    @overload
    def WriteStartElement(self, prefix: StringType, localName: StringType, ns: StringType) -> VoidType: ...
    
    def WriteString(self, text: StringType) -> VoidType: ...
    
    def WriteSurrogateCharEntity(self, lowChar: CharType, highChar: CharType) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: ObjectType) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: StringType) -> VoidType: ...
    
    def WriteWhitespace(self, ws: StringType) -> VoidType: ...
    
    def get_BaseUri(self) -> StringType: ...
    
    def get_HasRootNode(self) -> BooleanType: ...
    
    def get_Settings(self) -> XmlWriterSettings: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlException(SystemException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception, lineNumber: IntType, linePosition: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def LineNumber(self) -> IntType: ...
    
    @property
    def LinePosition(self) -> IntType: ...
    
    @property
    def Message(self) -> StringType: ...
    
    @property
    def SourceUri(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    
    def get_LineNumber(self) -> IntType: ...
    
    def get_LinePosition(self) -> IntType: ...
    
    def get_Message(self) -> StringType: ...
    
    def get_SourceUri(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlException(SystemException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception, lineNumber: IntType, linePosition: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def LineNumber(self) -> IntType: ...
    
    @property
    def LinePosition(self) -> IntType: ...
    
    @property
    def Message(self) -> StringType: ...
    
    @property
    def SourceUri(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    
    def get_LineNumber(self) -> IntType: ...
    
    def get_LinePosition(self) -> IntType: ...
    
    def get_Message(self) -> StringType: ...
    
    def get_SourceUri(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlImplementation(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, nt: XmlNameTable): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def CreateDocument(self) -> XmlDocument: ...
    
    def HasFeature(self, strFeature: StringType, strVersion: StringType) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlImplementation(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, nt: XmlNameTable): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def CreateDocument(self) -> XmlDocument: ...
    
    def HasFeature(self, strFeature: StringType, strVersion: StringType) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlLinkedNode(ABC, XmlNode, ICloneable, IEnumerable, IXPathNavigable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def NextSibling(self) -> XmlNode: ...
    
    @property
    def PreviousSibling(self) -> XmlNode: ...
    
    # ---------- Methods ---------- #
    
    def get_NextSibling(self) -> XmlNode: ...
    
    def get_PreviousSibling(self) -> XmlNode: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlLinkedNode(ABC, XmlNode, ICloneable, IEnumerable, IXPathNavigable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def NextSibling(self) -> XmlNode: ...
    
    @property
    def PreviousSibling(self) -> XmlNode: ...
    
    # ---------- Methods ---------- #
    
    def get_NextSibling(self) -> XmlNode: ...
    
    def get_PreviousSibling(self) -> XmlNode: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlLoader(ObjectType):
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


class XmlLoader(ObjectType):
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


class XmlName(ObjectType, IXmlSchemaInfo):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def HashCode(self) -> IntType: ...
    
    @property
    def IsDefault(self) -> BooleanType: ...
    
    @property
    def IsNil(self) -> BooleanType: ...
    
    @property
    def LocalName(self) -> StringType: ...
    
    @property
    def MemberType(self) -> XmlSchemaSimpleType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def NamespaceURI(self) -> StringType: ...
    
    @property
    def OwnerDocument(self) -> XmlDocument: ...
    
    @property
    def Prefix(self) -> StringType: ...
    
    @property
    def SchemaAttribute(self) -> XmlSchemaAttribute: ...
    
    @property
    def SchemaElement(self) -> XmlSchemaElement: ...
    
    @property
    def SchemaType(self) -> XmlSchemaType: ...
    
    @property
    def Validity(self) -> XmlSchemaValidity: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def Create(prefix: StringType, localName: StringType, ns: StringType, hashCode: IntType, ownerDoc: XmlDocument, next: XmlName, schemaInfo: IXmlSchemaInfo) -> XmlName: ...
    
    @overload
    def Equals(self, schemaInfo: IXmlSchemaInfo) -> BooleanType: ...
    
    @staticmethod
    @overload
    def GetHashCode(name: StringType) -> IntType: ...
    
    def get_HashCode(self) -> IntType: ...
    
    def get_IsDefault(self) -> BooleanType: ...
    
    def get_IsNil(self) -> BooleanType: ...
    
    def get_LocalName(self) -> StringType: ...
    
    def get_MemberType(self) -> XmlSchemaSimpleType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_NamespaceURI(self) -> StringType: ...
    
    def get_OwnerDocument(self) -> XmlDocument: ...
    
    def get_Prefix(self) -> StringType: ...
    
    def get_SchemaAttribute(self) -> XmlSchemaAttribute: ...
    
    def get_SchemaElement(self) -> XmlSchemaElement: ...
    
    def get_SchemaType(self) -> XmlSchemaType: ...
    
    def get_Validity(self) -> XmlSchemaValidity: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlName(ObjectType, IXmlSchemaInfo):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def HashCode(self) -> IntType: ...
    
    @property
    def IsDefault(self) -> BooleanType: ...
    
    @property
    def IsNil(self) -> BooleanType: ...
    
    @property
    def LocalName(self) -> StringType: ...
    
    @property
    def MemberType(self) -> XmlSchemaSimpleType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def NamespaceURI(self) -> StringType: ...
    
    @property
    def OwnerDocument(self) -> XmlDocument: ...
    
    @property
    def Prefix(self) -> StringType: ...
    
    @property
    def SchemaAttribute(self) -> XmlSchemaAttribute: ...
    
    @property
    def SchemaElement(self) -> XmlSchemaElement: ...
    
    @property
    def SchemaType(self) -> XmlSchemaType: ...
    
    @property
    def Validity(self) -> XmlSchemaValidity: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def Create(prefix: StringType, localName: StringType, ns: StringType, hashCode: IntType, ownerDoc: XmlDocument, next: XmlName, schemaInfo: IXmlSchemaInfo) -> XmlName: ...
    
    @overload
    def Equals(self, schemaInfo: IXmlSchemaInfo) -> BooleanType: ...
    
    @staticmethod
    @overload
    def GetHashCode(name: StringType) -> IntType: ...
    
    def get_HashCode(self) -> IntType: ...
    
    def get_IsDefault(self) -> BooleanType: ...
    
    def get_IsNil(self) -> BooleanType: ...
    
    def get_LocalName(self) -> StringType: ...
    
    def get_MemberType(self) -> XmlSchemaSimpleType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_NamespaceURI(self) -> StringType: ...
    
    def get_OwnerDocument(self) -> XmlDocument: ...
    
    def get_Prefix(self) -> StringType: ...
    
    def get_SchemaAttribute(self) -> XmlSchemaAttribute: ...
    
    def get_SchemaElement(self) -> XmlSchemaElement: ...
    
    def get_SchemaType(self) -> XmlSchemaType: ...
    
    def get_Validity(self) -> XmlSchemaValidity: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlNameEx(XmlName, IXmlSchemaInfo):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def IsDefault(self) -> BooleanType: ...
    
    @property
    def IsNil(self) -> BooleanType: ...
    
    @property
    def MemberType(self) -> XmlSchemaSimpleType: ...
    
    @property
    def SchemaAttribute(self) -> XmlSchemaAttribute: ...
    
    @property
    def SchemaElement(self) -> XmlSchemaElement: ...
    
    @property
    def SchemaType(self) -> XmlSchemaType: ...
    
    @property
    def Validity(self) -> XmlSchemaValidity: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Equals(self, schemaInfo: IXmlSchemaInfo) -> BooleanType: ...
    
    def SetIsDefault(self, value: BooleanType) -> VoidType: ...
    
    def SetIsNil(self, value: BooleanType) -> VoidType: ...
    
    def SetValidity(self, value: XmlSchemaValidity) -> VoidType: ...
    
    def get_IsDefault(self) -> BooleanType: ...
    
    def get_IsNil(self) -> BooleanType: ...
    
    def get_MemberType(self) -> XmlSchemaSimpleType: ...
    
    def get_SchemaAttribute(self) -> XmlSchemaAttribute: ...
    
    def get_SchemaElement(self) -> XmlSchemaElement: ...
    
    def get_SchemaType(self) -> XmlSchemaType: ...
    
    def get_Validity(self) -> XmlSchemaValidity: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlNameEx(XmlName, IXmlSchemaInfo):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def IsDefault(self) -> BooleanType: ...
    
    @property
    def IsNil(self) -> BooleanType: ...
    
    @property
    def MemberType(self) -> XmlSchemaSimpleType: ...
    
    @property
    def SchemaAttribute(self) -> XmlSchemaAttribute: ...
    
    @property
    def SchemaElement(self) -> XmlSchemaElement: ...
    
    @property
    def SchemaType(self) -> XmlSchemaType: ...
    
    @property
    def Validity(self) -> XmlSchemaValidity: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Equals(self, schemaInfo: IXmlSchemaInfo) -> BooleanType: ...
    
    def SetIsDefault(self, value: BooleanType) -> VoidType: ...
    
    def SetIsNil(self, value: BooleanType) -> VoidType: ...
    
    def SetValidity(self, value: XmlSchemaValidity) -> VoidType: ...
    
    def get_IsDefault(self) -> BooleanType: ...
    
    def get_IsNil(self) -> BooleanType: ...
    
    def get_MemberType(self) -> XmlSchemaSimpleType: ...
    
    def get_SchemaAttribute(self) -> XmlSchemaAttribute: ...
    
    def get_SchemaElement(self) -> XmlSchemaElement: ...
    
    def get_SchemaType(self) -> XmlSchemaType: ...
    
    def get_Validity(self) -> XmlSchemaValidity: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlNameTable(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def Add(self, array: ArrayType[CharType], offset: IntType, length: IntType) -> StringType: ...
    
    @overload
    def Add(self, array: StringType) -> StringType: ...
    
    @overload
    def Get(self, array: ArrayType[CharType], offset: IntType, length: IntType) -> StringType: ...
    
    @overload
    def Get(self, array: StringType) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlNameTable(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def Add(self, array: ArrayType[CharType], offset: IntType, length: IntType) -> StringType: ...
    
    @overload
    def Add(self, array: StringType) -> StringType: ...
    
    @overload
    def Get(self, array: ArrayType[CharType], offset: IntType, length: IntType) -> StringType: ...
    
    @overload
    def Get(self, array: StringType) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlNamedNodeMap(ObjectType, IEnumerable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def GetEnumerator(self) -> IEnumerator: ...
    
    @overload
    def GetNamedItem(self, name: StringType) -> XmlNode: ...
    
    @overload
    def GetNamedItem(self, localName: StringType, namespaceURI: StringType) -> XmlNode: ...
    
    def Item(self, index: IntType) -> XmlNode: ...
    
    @overload
    def RemoveNamedItem(self, name: StringType) -> XmlNode: ...
    
    @overload
    def RemoveNamedItem(self, localName: StringType, namespaceURI: StringType) -> XmlNode: ...
    
    def SetNamedItem(self, node: XmlNode) -> XmlNode: ...
    
    def get_Count(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlNamedNodeMap(ObjectType, IEnumerable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def GetEnumerator(self) -> IEnumerator: ...
    
    @overload
    def GetNamedItem(self, name: StringType) -> XmlNode: ...
    
    @overload
    def GetNamedItem(self, localName: StringType, namespaceURI: StringType) -> XmlNode: ...
    
    def Item(self, index: IntType) -> XmlNode: ...
    
    @overload
    def RemoveNamedItem(self, name: StringType) -> XmlNode: ...
    
    @overload
    def RemoveNamedItem(self, localName: StringType, namespaceURI: StringType) -> XmlNode: ...
    
    def SetNamedItem(self, node: XmlNode) -> XmlNode: ...
    
    def get_Count(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlNamespaceManager(ObjectType, IXmlNamespaceResolver, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, nameTable: XmlNameTable): ...
    
    # ---------- Properties ---------- #
    
    @property
    def DefaultNamespace(self) -> StringType: ...
    
    @property
    def NameTable(self) -> XmlNameTable: ...
    
    # ---------- Methods ---------- #
    
    def AddNamespace(self, prefix: StringType, uri: StringType) -> VoidType: ...
    
    def GetEnumerator(self) -> IEnumerator: ...
    
    def GetNamespacesInScope(self, scope: XmlNamespaceScope) -> IDictionary[StringType, StringType]: ...
    
    def HasNamespace(self, prefix: StringType) -> BooleanType: ...
    
    def LookupNamespace(self, prefix: StringType) -> StringType: ...
    
    def LookupPrefix(self, uri: StringType) -> StringType: ...
    
    def PopScope(self) -> BooleanType: ...
    
    def PushScope(self) -> VoidType: ...
    
    def RemoveNamespace(self, prefix: StringType, uri: StringType) -> VoidType: ...
    
    def get_DefaultNamespace(self) -> StringType: ...
    
    def get_NameTable(self) -> XmlNameTable: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlNamespaceManager(ObjectType, IXmlNamespaceResolver, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, nameTable: XmlNameTable): ...
    
    # ---------- Properties ---------- #
    
    @property
    def DefaultNamespace(self) -> StringType: ...
    
    @property
    def NameTable(self) -> XmlNameTable: ...
    
    # ---------- Methods ---------- #
    
    def AddNamespace(self, prefix: StringType, uri: StringType) -> VoidType: ...
    
    def GetEnumerator(self) -> IEnumerator: ...
    
    def GetNamespacesInScope(self, scope: XmlNamespaceScope) -> IDictionary[StringType, StringType]: ...
    
    def HasNamespace(self, prefix: StringType) -> BooleanType: ...
    
    def LookupNamespace(self, prefix: StringType) -> StringType: ...
    
    def LookupPrefix(self, uri: StringType) -> StringType: ...
    
    def PopScope(self) -> BooleanType: ...
    
    def PushScope(self) -> VoidType: ...
    
    def RemoveNamespace(self, prefix: StringType, uri: StringType) -> VoidType: ...
    
    def get_DefaultNamespace(self) -> StringType: ...
    
    def get_NameTable(self) -> XmlNameTable: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlNode(ABC, ObjectType, ICloneable, IEnumerable, IXPathNavigable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Attributes(self) -> XmlAttributeCollection: ...
    
    @property
    def BaseURI(self) -> StringType: ...
    
    @property
    def ChildNodes(self) -> XmlNodeList: ...
    
    @property
    def FirstChild(self) -> XmlNode: ...
    
    @property
    def HasChildNodes(self) -> BooleanType: ...
    
    @property
    def InnerText(self) -> StringType: ...
    
    @InnerText.setter
    def InnerText(self, value: StringType) -> None: ...
    
    @property
    def InnerXml(self) -> StringType: ...
    
    @InnerXml.setter
    def InnerXml(self, value: StringType) -> None: ...
    
    @property
    def IsReadOnly(self) -> BooleanType: ...
    
    def __getitem__(self, key: StringType) -> XmlElement: ...
    
    def __getitem__(self, key: StringType) -> XmlElement: ...
    
    @property
    def LastChild(self) -> XmlNode: ...
    
    @property
    def LocalName(self) -> StringType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def NamespaceURI(self) -> StringType: ...
    
    @property
    def NextSibling(self) -> XmlNode: ...
    
    @property
    def NodeType(self) -> XmlNodeType: ...
    
    @property
    def OuterXml(self) -> StringType: ...
    
    @property
    def OwnerDocument(self) -> XmlDocument: ...
    
    @property
    def ParentNode(self) -> XmlNode: ...
    
    @property
    def Prefix(self) -> StringType: ...
    
    @Prefix.setter
    def Prefix(self, value: StringType) -> None: ...
    
    @property
    def PreviousSibling(self) -> XmlNode: ...
    
    @property
    def PreviousText(self) -> XmlNode: ...
    
    @property
    def SchemaInfo(self) -> IXmlSchemaInfo: ...
    
    @property
    def Value(self) -> StringType: ...
    
    @Value.setter
    def Value(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def AppendChild(self, newChild: XmlNode) -> XmlNode: ...
    
    def Clone(self) -> XmlNode: ...
    
    def CloneNode(self, deep: BooleanType) -> XmlNode: ...
    
    def CreateNavigator(self) -> XPathNavigator: ...
    
    def GetEnumerator(self) -> IEnumerator: ...
    
    def GetNamespaceOfPrefix(self, prefix: StringType) -> StringType: ...
    
    def GetPrefixOfNamespace(self, namespaceURI: StringType) -> StringType: ...
    
    def InsertAfter(self, newChild: XmlNode, refChild: XmlNode) -> XmlNode: ...
    
    def InsertBefore(self, newChild: XmlNode, refChild: XmlNode) -> XmlNode: ...
    
    def Normalize(self) -> VoidType: ...
    
    def PrependChild(self, newChild: XmlNode) -> XmlNode: ...
    
    def RemoveAll(self) -> VoidType: ...
    
    def RemoveChild(self, oldChild: XmlNode) -> XmlNode: ...
    
    def ReplaceChild(self, newChild: XmlNode, oldChild: XmlNode) -> XmlNode: ...
    
    @overload
    def SelectNodes(self, xpath: StringType) -> XmlNodeList: ...
    
    @overload
    def SelectNodes(self, xpath: StringType, nsmgr: XmlNamespaceManager) -> XmlNodeList: ...
    
    @overload
    def SelectSingleNode(self, xpath: StringType) -> XmlNode: ...
    
    @overload
    def SelectSingleNode(self, xpath: StringType, nsmgr: XmlNamespaceManager) -> XmlNode: ...
    
    def Supports(self, feature: StringType, version: StringType) -> BooleanType: ...
    
    def WriteContentTo(self, w: XmlWriter) -> VoidType: ...
    
    def WriteTo(self, w: XmlWriter) -> VoidType: ...
    
    def get_Attributes(self) -> XmlAttributeCollection: ...
    
    def get_BaseURI(self) -> StringType: ...
    
    def get_ChildNodes(self) -> XmlNodeList: ...
    
    def get_FirstChild(self) -> XmlNode: ...
    
    def get_HasChildNodes(self) -> BooleanType: ...
    
    def get_InnerText(self) -> StringType: ...
    
    def get_InnerXml(self) -> StringType: ...
    
    def get_IsReadOnly(self) -> BooleanType: ...
    
    @overload
    def get_Item(self, name: StringType) -> XmlElement: ...
    
    @overload
    def get_Item(self, localname: StringType, ns: StringType) -> XmlElement: ...
    
    def get_LastChild(self) -> XmlNode: ...
    
    def get_LocalName(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_NamespaceURI(self) -> StringType: ...
    
    def get_NextSibling(self) -> XmlNode: ...
    
    def get_NodeType(self) -> XmlNodeType: ...
    
    def get_OuterXml(self) -> StringType: ...
    
    def get_OwnerDocument(self) -> XmlDocument: ...
    
    def get_ParentNode(self) -> XmlNode: ...
    
    def get_Prefix(self) -> StringType: ...
    
    def get_PreviousSibling(self) -> XmlNode: ...
    
    def get_PreviousText(self) -> XmlNode: ...
    
    def get_SchemaInfo(self) -> IXmlSchemaInfo: ...
    
    def get_Value(self) -> StringType: ...
    
    def set_InnerText(self, value: StringType) -> VoidType: ...
    
    def set_InnerXml(self, value: StringType) -> VoidType: ...
    
    def set_Prefix(self, value: StringType) -> VoidType: ...
    
    def set_Value(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlNode(ABC, ObjectType, ICloneable, IEnumerable, IXPathNavigable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Attributes(self) -> XmlAttributeCollection: ...
    
    @property
    def BaseURI(self) -> StringType: ...
    
    @property
    def ChildNodes(self) -> XmlNodeList: ...
    
    @property
    def FirstChild(self) -> XmlNode: ...
    
    @property
    def HasChildNodes(self) -> BooleanType: ...
    
    @property
    def InnerText(self) -> StringType: ...
    
    @InnerText.setter
    def InnerText(self, value: StringType) -> None: ...
    
    @property
    def InnerXml(self) -> StringType: ...
    
    @InnerXml.setter
    def InnerXml(self, value: StringType) -> None: ...
    
    @property
    def IsReadOnly(self) -> BooleanType: ...
    
    def __getitem__(self, key: StringType) -> XmlElement: ...
    
    def __getitem__(self, key: StringType) -> XmlElement: ...
    
    @property
    def LastChild(self) -> XmlNode: ...
    
    @property
    def LocalName(self) -> StringType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def NamespaceURI(self) -> StringType: ...
    
    @property
    def NextSibling(self) -> XmlNode: ...
    
    @property
    def NodeType(self) -> XmlNodeType: ...
    
    @property
    def OuterXml(self) -> StringType: ...
    
    @property
    def OwnerDocument(self) -> XmlDocument: ...
    
    @property
    def ParentNode(self) -> XmlNode: ...
    
    @property
    def Prefix(self) -> StringType: ...
    
    @Prefix.setter
    def Prefix(self, value: StringType) -> None: ...
    
    @property
    def PreviousSibling(self) -> XmlNode: ...
    
    @property
    def PreviousText(self) -> XmlNode: ...
    
    @property
    def SchemaInfo(self) -> IXmlSchemaInfo: ...
    
    @property
    def Value(self) -> StringType: ...
    
    @Value.setter
    def Value(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def AppendChild(self, newChild: XmlNode) -> XmlNode: ...
    
    def Clone(self) -> XmlNode: ...
    
    def CloneNode(self, deep: BooleanType) -> XmlNode: ...
    
    def CreateNavigator(self) -> XPathNavigator: ...
    
    def GetEnumerator(self) -> IEnumerator: ...
    
    def GetNamespaceOfPrefix(self, prefix: StringType) -> StringType: ...
    
    def GetPrefixOfNamespace(self, namespaceURI: StringType) -> StringType: ...
    
    def InsertAfter(self, newChild: XmlNode, refChild: XmlNode) -> XmlNode: ...
    
    def InsertBefore(self, newChild: XmlNode, refChild: XmlNode) -> XmlNode: ...
    
    def Normalize(self) -> VoidType: ...
    
    def PrependChild(self, newChild: XmlNode) -> XmlNode: ...
    
    def RemoveAll(self) -> VoidType: ...
    
    def RemoveChild(self, oldChild: XmlNode) -> XmlNode: ...
    
    def ReplaceChild(self, newChild: XmlNode, oldChild: XmlNode) -> XmlNode: ...
    
    @overload
    def SelectNodes(self, xpath: StringType) -> XmlNodeList: ...
    
    @overload
    def SelectNodes(self, xpath: StringType, nsmgr: XmlNamespaceManager) -> XmlNodeList: ...
    
    @overload
    def SelectSingleNode(self, xpath: StringType) -> XmlNode: ...
    
    @overload
    def SelectSingleNode(self, xpath: StringType, nsmgr: XmlNamespaceManager) -> XmlNode: ...
    
    def Supports(self, feature: StringType, version: StringType) -> BooleanType: ...
    
    def WriteContentTo(self, w: XmlWriter) -> VoidType: ...
    
    def WriteTo(self, w: XmlWriter) -> VoidType: ...
    
    def get_Attributes(self) -> XmlAttributeCollection: ...
    
    def get_BaseURI(self) -> StringType: ...
    
    def get_ChildNodes(self) -> XmlNodeList: ...
    
    def get_FirstChild(self) -> XmlNode: ...
    
    def get_HasChildNodes(self) -> BooleanType: ...
    
    def get_InnerText(self) -> StringType: ...
    
    def get_InnerXml(self) -> StringType: ...
    
    def get_IsReadOnly(self) -> BooleanType: ...
    
    @overload
    def get_Item(self, name: StringType) -> XmlElement: ...
    
    @overload
    def get_Item(self, localname: StringType, ns: StringType) -> XmlElement: ...
    
    def get_LastChild(self) -> XmlNode: ...
    
    def get_LocalName(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_NamespaceURI(self) -> StringType: ...
    
    def get_NextSibling(self) -> XmlNode: ...
    
    def get_NodeType(self) -> XmlNodeType: ...
    
    def get_OuterXml(self) -> StringType: ...
    
    def get_OwnerDocument(self) -> XmlDocument: ...
    
    def get_ParentNode(self) -> XmlNode: ...
    
    def get_Prefix(self) -> StringType: ...
    
    def get_PreviousSibling(self) -> XmlNode: ...
    
    def get_PreviousText(self) -> XmlNode: ...
    
    def get_SchemaInfo(self) -> IXmlSchemaInfo: ...
    
    def get_Value(self) -> StringType: ...
    
    def set_InnerText(self, value: StringType) -> VoidType: ...
    
    def set_InnerXml(self, value: StringType) -> VoidType: ...
    
    def set_Prefix(self, value: StringType) -> VoidType: ...
    
    def set_Value(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlNodeChangedEventArgs(EventArgs):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, node: XmlNode, oldParent: XmlNode, newParent: XmlNode, oldValue: StringType, newValue: StringType, action: XmlNodeChangedAction): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Action(self) -> XmlNodeChangedAction: ...
    
    @property
    def NewParent(self) -> XmlNode: ...
    
    @property
    def NewValue(self) -> StringType: ...
    
    @property
    def Node(self) -> XmlNode: ...
    
    @property
    def OldParent(self) -> XmlNode: ...
    
    @property
    def OldValue(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_Action(self) -> XmlNodeChangedAction: ...
    
    def get_NewParent(self) -> XmlNode: ...
    
    def get_NewValue(self) -> StringType: ...
    
    def get_Node(self) -> XmlNode: ...
    
    def get_OldParent(self) -> XmlNode: ...
    
    def get_OldValue(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlNodeChangedEventArgs(EventArgs):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, node: XmlNode, oldParent: XmlNode, newParent: XmlNode, oldValue: StringType, newValue: StringType, action: XmlNodeChangedAction): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Action(self) -> XmlNodeChangedAction: ...
    
    @property
    def NewParent(self) -> XmlNode: ...
    
    @property
    def NewValue(self) -> StringType: ...
    
    @property
    def Node(self) -> XmlNode: ...
    
    @property
    def OldParent(self) -> XmlNode: ...
    
    @property
    def OldValue(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_Action(self) -> XmlNodeChangedAction: ...
    
    def get_NewParent(self) -> XmlNode: ...
    
    def get_NewValue(self) -> StringType: ...
    
    def get_Node(self) -> XmlNode: ...
    
    def get_OldParent(self) -> XmlNode: ...
    
    def get_OldValue(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlNodeChangedEventHandler(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, sender: ObjectType, e: XmlNodeChangedEventArgs, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, sender: ObjectType, e: XmlNodeChangedEventArgs) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlNodeChangedEventHandler(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, sender: ObjectType, e: XmlNodeChangedEventArgs, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, sender: ObjectType, e: XmlNodeChangedEventArgs) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlNodeList(ABC, ObjectType, IEnumerable, IDisposable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def ItemOf(self) -> XmlNode: ...
    
    # ---------- Methods ---------- #
    
    def GetEnumerator(self) -> IEnumerator: ...
    
    def Item(self, index: IntType) -> XmlNode: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_ItemOf(self, i: IntType) -> XmlNode: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlNodeList(ABC, ObjectType, IEnumerable, IDisposable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def ItemOf(self) -> XmlNode: ...
    
    # ---------- Methods ---------- #
    
    def GetEnumerator(self) -> IEnumerator: ...
    
    def Item(self, index: IntType) -> XmlNode: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_ItemOf(self, i: IntType) -> XmlNode: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlNodeListEnumerator(ObjectType, IEnumerator):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, list: XPathNodeList): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Current(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def MoveNext(self) -> BooleanType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Current(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlNodeListEnumerator(ObjectType, IEnumerator):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, list: XPathNodeList): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Current(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def MoveNext(self) -> BooleanType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Current(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlNodeReader(XmlReader, IDisposable, IXmlNamespaceResolver):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, node: XmlNode): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AttributeCount(self) -> IntType: ...
    
    @property
    def BaseURI(self) -> StringType: ...
    
    @property
    def CanReadBinaryContent(self) -> BooleanType: ...
    
    @property
    def CanResolveEntity(self) -> BooleanType: ...
    
    @property
    def Depth(self) -> IntType: ...
    
    @property
    def EOF(self) -> BooleanType: ...
    
    @property
    def HasAttributes(self) -> BooleanType: ...
    
    @property
    def HasValue(self) -> BooleanType: ...
    
    @property
    def IsDefault(self) -> BooleanType: ...
    
    @property
    def IsEmptyElement(self) -> BooleanType: ...
    
    @property
    def LocalName(self) -> StringType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def NameTable(self) -> XmlNameTable: ...
    
    @property
    def NamespaceURI(self) -> StringType: ...
    
    @property
    def NodeType(self) -> XmlNodeType: ...
    
    @property
    def Prefix(self) -> StringType: ...
    
    @property
    def ReadState(self) -> ReadState: ...
    
    @property
    def SchemaInfo(self) -> IXmlSchemaInfo: ...
    
    @property
    def Value(self) -> StringType: ...
    
    @property
    def XmlLang(self) -> StringType: ...
    
    @property
    def XmlSpace(self) -> XmlSpace: ...
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    @overload
    def GetAttribute(self, name: StringType) -> StringType: ...
    
    @overload
    def GetAttribute(self, name: StringType, namespaceURI: StringType) -> StringType: ...
    
    @overload
    def GetAttribute(self, attributeIndex: IntType) -> StringType: ...
    
    def LookupNamespace(self, prefix: StringType) -> StringType: ...
    
    @overload
    def MoveToAttribute(self, name: StringType) -> BooleanType: ...
    
    @overload
    def MoveToAttribute(self, name: StringType, namespaceURI: StringType) -> BooleanType: ...
    
    @overload
    def MoveToAttribute(self, attributeIndex: IntType) -> VoidType: ...
    
    def MoveToElement(self) -> BooleanType: ...
    
    def MoveToFirstAttribute(self) -> BooleanType: ...
    
    def MoveToNextAttribute(self) -> BooleanType: ...
    
    def Read(self) -> BooleanType: ...
    
    def ReadAttributeValue(self) -> BooleanType: ...
    
    def ReadContentAsBase64(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadContentAsBinHex(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadElementContentAsBase64(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadElementContentAsBinHex(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadString(self) -> StringType: ...
    
    def ResolveEntity(self) -> VoidType: ...
    
    def Skip(self) -> VoidType: ...
    
    def get_AttributeCount(self) -> IntType: ...
    
    def get_BaseURI(self) -> StringType: ...
    
    def get_CanReadBinaryContent(self) -> BooleanType: ...
    
    def get_CanResolveEntity(self) -> BooleanType: ...
    
    def get_Depth(self) -> IntType: ...
    
    def get_EOF(self) -> BooleanType: ...
    
    def get_HasAttributes(self) -> BooleanType: ...
    
    def get_HasValue(self) -> BooleanType: ...
    
    def get_IsDefault(self) -> BooleanType: ...
    
    def get_IsEmptyElement(self) -> BooleanType: ...
    
    def get_LocalName(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_NameTable(self) -> XmlNameTable: ...
    
    def get_NamespaceURI(self) -> StringType: ...
    
    def get_NodeType(self) -> XmlNodeType: ...
    
    def get_Prefix(self) -> StringType: ...
    
    def get_ReadState(self) -> ReadState: ...
    
    def get_SchemaInfo(self) -> IXmlSchemaInfo: ...
    
    def get_Value(self) -> StringType: ...
    
    def get_XmlLang(self) -> StringType: ...
    
    def get_XmlSpace(self) -> XmlSpace: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlNodeReader(XmlReader, IDisposable, IXmlNamespaceResolver):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, node: XmlNode): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AttributeCount(self) -> IntType: ...
    
    @property
    def BaseURI(self) -> StringType: ...
    
    @property
    def CanReadBinaryContent(self) -> BooleanType: ...
    
    @property
    def CanResolveEntity(self) -> BooleanType: ...
    
    @property
    def Depth(self) -> IntType: ...
    
    @property
    def EOF(self) -> BooleanType: ...
    
    @property
    def HasAttributes(self) -> BooleanType: ...
    
    @property
    def HasValue(self) -> BooleanType: ...
    
    @property
    def IsDefault(self) -> BooleanType: ...
    
    @property
    def IsEmptyElement(self) -> BooleanType: ...
    
    @property
    def LocalName(self) -> StringType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def NameTable(self) -> XmlNameTable: ...
    
    @property
    def NamespaceURI(self) -> StringType: ...
    
    @property
    def NodeType(self) -> XmlNodeType: ...
    
    @property
    def Prefix(self) -> StringType: ...
    
    @property
    def ReadState(self) -> ReadState: ...
    
    @property
    def SchemaInfo(self) -> IXmlSchemaInfo: ...
    
    @property
    def Value(self) -> StringType: ...
    
    @property
    def XmlLang(self) -> StringType: ...
    
    @property
    def XmlSpace(self) -> XmlSpace: ...
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    @overload
    def GetAttribute(self, name: StringType) -> StringType: ...
    
    @overload
    def GetAttribute(self, name: StringType, namespaceURI: StringType) -> StringType: ...
    
    @overload
    def GetAttribute(self, attributeIndex: IntType) -> StringType: ...
    
    def LookupNamespace(self, prefix: StringType) -> StringType: ...
    
    @overload
    def MoveToAttribute(self, name: StringType) -> BooleanType: ...
    
    @overload
    def MoveToAttribute(self, name: StringType, namespaceURI: StringType) -> BooleanType: ...
    
    @overload
    def MoveToAttribute(self, attributeIndex: IntType) -> VoidType: ...
    
    def MoveToElement(self) -> BooleanType: ...
    
    def MoveToFirstAttribute(self) -> BooleanType: ...
    
    def MoveToNextAttribute(self) -> BooleanType: ...
    
    def Read(self) -> BooleanType: ...
    
    def ReadAttributeValue(self) -> BooleanType: ...
    
    def ReadContentAsBase64(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadContentAsBinHex(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadElementContentAsBase64(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadElementContentAsBinHex(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadString(self) -> StringType: ...
    
    def ResolveEntity(self) -> VoidType: ...
    
    def Skip(self) -> VoidType: ...
    
    def get_AttributeCount(self) -> IntType: ...
    
    def get_BaseURI(self) -> StringType: ...
    
    def get_CanReadBinaryContent(self) -> BooleanType: ...
    
    def get_CanResolveEntity(self) -> BooleanType: ...
    
    def get_Depth(self) -> IntType: ...
    
    def get_EOF(self) -> BooleanType: ...
    
    def get_HasAttributes(self) -> BooleanType: ...
    
    def get_HasValue(self) -> BooleanType: ...
    
    def get_IsDefault(self) -> BooleanType: ...
    
    def get_IsEmptyElement(self) -> BooleanType: ...
    
    def get_LocalName(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_NameTable(self) -> XmlNameTable: ...
    
    def get_NamespaceURI(self) -> StringType: ...
    
    def get_NodeType(self) -> XmlNodeType: ...
    
    def get_Prefix(self) -> StringType: ...
    
    def get_ReadState(self) -> ReadState: ...
    
    def get_SchemaInfo(self) -> IXmlSchemaInfo: ...
    
    def get_Value(self) -> StringType: ...
    
    def get_XmlLang(self) -> StringType: ...
    
    def get_XmlSpace(self) -> XmlSpace: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlNodeReaderNavigator(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, node: XmlNode): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AttributeCount(self) -> IntType: ...
    
    @property
    def BaseURI(self) -> StringType: ...
    
    @property
    def Document(self) -> XmlDocument: ...
    
    @property
    def HasValue(self) -> BooleanType: ...
    
    @property
    def IsDefault(self) -> BooleanType: ...
    
    @property
    def IsEmptyElement(self) -> BooleanType: ...
    
    @property
    def LocalName(self) -> StringType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def NameTable(self) -> XmlNameTable: ...
    
    @property
    def NamespaceURI(self) -> StringType: ...
    
    @property
    def NodeType(self) -> XmlNodeType: ...
    
    @property
    def Prefix(self) -> StringType: ...
    
    @property
    def SchemaInfo(self) -> IXmlSchemaInfo: ...
    
    @property
    def Value(self) -> StringType: ...
    
    @property
    def XmlLang(self) -> StringType: ...
    
    @property
    def XmlSpace(self) -> XmlSpace: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def GetAttribute(self, name: StringType) -> StringType: ...
    
    @overload
    def GetAttribute(self, name: StringType, ns: StringType) -> StringType: ...
    
    @overload
    def GetAttribute(self, attributeIndex: IntType) -> StringType: ...
    
    def GetDecAttrInd(self, name: StringType) -> IntType: ...
    
    @overload
    def GetDeclarationAttr(self, i: IntType) -> StringType: ...
    
    @overload
    def GetDeclarationAttr(self, decl: XmlDeclaration, name: StringType) -> StringType: ...
    
    def GetDocTypeAttrInd(self, name: StringType) -> IntType: ...
    
    @overload
    def GetDocumentTypeAttr(self, i: IntType) -> StringType: ...
    
    @overload
    def GetDocumentTypeAttr(self, docType: XmlDocumentType, name: StringType) -> StringType: ...
    
    def LogMove(self, level: IntType) -> VoidType: ...
    
    def LookupNamespace(self, prefix: StringType) -> StringType: ...
    
    @overload
    def MoveToAttribute(self, name: StringType) -> BooleanType: ...
    
    @overload
    def MoveToAttribute(self, name: StringType, namespaceURI: StringType) -> BooleanType: ...
    
    @overload
    def MoveToAttribute(self, attributeIndex: IntType) -> VoidType: ...
    
    def MoveToElement(self) -> BooleanType: ...
    
    def MoveToFirstChild(self) -> BooleanType: ...
    
    def MoveToNext(self) -> BooleanType: ...
    
    def MoveToNextAttribute(self, level: IntType) -> Tuple[BooleanType, IntType]: ...
    
    def MoveToParent(self) -> BooleanType: ...
    
    def ReadAttributeValue(self, level: IntType, bResolveEntity: BooleanType, nt: XmlNodeType) -> Tuple[BooleanType, IntType, BooleanType, XmlNodeType]: ...
    
    def ResetMove(self, level: IntType, nt: XmlNodeType) -> Tuple[VoidType, IntType, XmlNodeType]: ...
    
    def ResetToAttribute(self, level: IntType) -> Tuple[VoidType, IntType]: ...
    
    def RollBackMove(self, level: IntType) -> Tuple[VoidType, IntType]: ...
    
    def get_AttributeCount(self) -> IntType: ...
    
    def get_BaseURI(self) -> StringType: ...
    
    def get_Document(self) -> XmlDocument: ...
    
    def get_HasValue(self) -> BooleanType: ...
    
    def get_IsDefault(self) -> BooleanType: ...
    
    def get_IsEmptyElement(self) -> BooleanType: ...
    
    def get_LocalName(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_NameTable(self) -> XmlNameTable: ...
    
    def get_NamespaceURI(self) -> StringType: ...
    
    def get_NodeType(self) -> XmlNodeType: ...
    
    def get_Prefix(self) -> StringType: ...
    
    def get_SchemaInfo(self) -> IXmlSchemaInfo: ...
    
    def get_Value(self) -> StringType: ...
    
    def get_XmlLang(self) -> StringType: ...
    
    def get_XmlSpace(self) -> XmlSpace: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlNodeReaderNavigator(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, node: XmlNode): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AttributeCount(self) -> IntType: ...
    
    @property
    def BaseURI(self) -> StringType: ...
    
    @property
    def Document(self) -> XmlDocument: ...
    
    @property
    def HasValue(self) -> BooleanType: ...
    
    @property
    def IsDefault(self) -> BooleanType: ...
    
    @property
    def IsEmptyElement(self) -> BooleanType: ...
    
    @property
    def LocalName(self) -> StringType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def NameTable(self) -> XmlNameTable: ...
    
    @property
    def NamespaceURI(self) -> StringType: ...
    
    @property
    def NodeType(self) -> XmlNodeType: ...
    
    @property
    def Prefix(self) -> StringType: ...
    
    @property
    def SchemaInfo(self) -> IXmlSchemaInfo: ...
    
    @property
    def Value(self) -> StringType: ...
    
    @property
    def XmlLang(self) -> StringType: ...
    
    @property
    def XmlSpace(self) -> XmlSpace: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def GetAttribute(self, name: StringType) -> StringType: ...
    
    @overload
    def GetAttribute(self, name: StringType, ns: StringType) -> StringType: ...
    
    @overload
    def GetAttribute(self, attributeIndex: IntType) -> StringType: ...
    
    def GetDecAttrInd(self, name: StringType) -> IntType: ...
    
    @overload
    def GetDeclarationAttr(self, i: IntType) -> StringType: ...
    
    @overload
    def GetDeclarationAttr(self, decl: XmlDeclaration, name: StringType) -> StringType: ...
    
    def GetDocTypeAttrInd(self, name: StringType) -> IntType: ...
    
    @overload
    def GetDocumentTypeAttr(self, i: IntType) -> StringType: ...
    
    @overload
    def GetDocumentTypeAttr(self, docType: XmlDocumentType, name: StringType) -> StringType: ...
    
    def LogMove(self, level: IntType) -> VoidType: ...
    
    def LookupNamespace(self, prefix: StringType) -> StringType: ...
    
    @overload
    def MoveToAttribute(self, name: StringType) -> BooleanType: ...
    
    @overload
    def MoveToAttribute(self, name: StringType, namespaceURI: StringType) -> BooleanType: ...
    
    @overload
    def MoveToAttribute(self, attributeIndex: IntType) -> VoidType: ...
    
    def MoveToElement(self) -> BooleanType: ...
    
    def MoveToFirstChild(self) -> BooleanType: ...
    
    def MoveToNext(self) -> BooleanType: ...
    
    def MoveToNextAttribute(self, level: IntType) -> Tuple[BooleanType, IntType]: ...
    
    def MoveToParent(self) -> BooleanType: ...
    
    def ReadAttributeValue(self, level: IntType, bResolveEntity: BooleanType, nt: XmlNodeType) -> Tuple[BooleanType, IntType, BooleanType, XmlNodeType]: ...
    
    def ResetMove(self, level: IntType, nt: XmlNodeType) -> Tuple[VoidType, IntType, XmlNodeType]: ...
    
    def ResetToAttribute(self, level: IntType) -> Tuple[VoidType, IntType]: ...
    
    def RollBackMove(self, level: IntType) -> Tuple[VoidType, IntType]: ...
    
    def get_AttributeCount(self) -> IntType: ...
    
    def get_BaseURI(self) -> StringType: ...
    
    def get_Document(self) -> XmlDocument: ...
    
    def get_HasValue(self) -> BooleanType: ...
    
    def get_IsDefault(self) -> BooleanType: ...
    
    def get_IsEmptyElement(self) -> BooleanType: ...
    
    def get_LocalName(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_NameTable(self) -> XmlNameTable: ...
    
    def get_NamespaceURI(self) -> StringType: ...
    
    def get_NodeType(self) -> XmlNodeType: ...
    
    def get_Prefix(self) -> StringType: ...
    
    def get_SchemaInfo(self) -> IXmlSchemaInfo: ...
    
    def get_Value(self) -> StringType: ...
    
    def get_XmlLang(self) -> StringType: ...
    
    def get_XmlSpace(self) -> XmlSpace: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlNotation(XmlNode, ICloneable, IEnumerable, IXPathNavigable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def InnerXml(self) -> StringType: ...
    
    @InnerXml.setter
    def InnerXml(self, value: StringType) -> None: ...
    
    @property
    def IsReadOnly(self) -> BooleanType: ...
    
    @property
    def LocalName(self) -> StringType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def NodeType(self) -> XmlNodeType: ...
    
    @property
    def OuterXml(self) -> StringType: ...
    
    @property
    def PublicId(self) -> StringType: ...
    
    @property
    def SystemId(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def CloneNode(self, deep: BooleanType) -> XmlNode: ...
    
    def WriteContentTo(self, w: XmlWriter) -> VoidType: ...
    
    def WriteTo(self, w: XmlWriter) -> VoidType: ...
    
    def get_InnerXml(self) -> StringType: ...
    
    def get_IsReadOnly(self) -> BooleanType: ...
    
    def get_LocalName(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_NodeType(self) -> XmlNodeType: ...
    
    def get_OuterXml(self) -> StringType: ...
    
    def get_PublicId(self) -> StringType: ...
    
    def get_SystemId(self) -> StringType: ...
    
    def set_InnerXml(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlNotation(XmlNode, ICloneable, IEnumerable, IXPathNavigable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def InnerXml(self) -> StringType: ...
    
    @InnerXml.setter
    def InnerXml(self, value: StringType) -> None: ...
    
    @property
    def IsReadOnly(self) -> BooleanType: ...
    
    @property
    def LocalName(self) -> StringType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def NodeType(self) -> XmlNodeType: ...
    
    @property
    def OuterXml(self) -> StringType: ...
    
    @property
    def PublicId(self) -> StringType: ...
    
    @property
    def SystemId(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def CloneNode(self, deep: BooleanType) -> XmlNode: ...
    
    def WriteContentTo(self, w: XmlWriter) -> VoidType: ...
    
    def WriteTo(self, w: XmlWriter) -> VoidType: ...
    
    def get_InnerXml(self) -> StringType: ...
    
    def get_IsReadOnly(self) -> BooleanType: ...
    
    def get_LocalName(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_NodeType(self) -> XmlNodeType: ...
    
    def get_OuterXml(self) -> StringType: ...
    
    def get_PublicId(self) -> StringType: ...
    
    def get_SystemId(self) -> StringType: ...
    
    def set_InnerXml(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlNullResolver(XmlResolver):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Singleton() -> XmlNullResolver: ...
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @Credentials.setter
    def Credentials(self, value: ICredentials) -> None: ...
    
    # ---------- Methods ---------- #
    
    def GetEntity(self, absoluteUri: Uri, role: StringType, ofObjectToReturn: TypeType) -> ObjectType: ...
    
    def set_Credentials(self, value: ICredentials) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlNullResolver(XmlResolver):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Singleton() -> XmlNullResolver: ...
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @Credentials.setter
    def Credentials(self, value: ICredentials) -> None: ...
    
    # ---------- Methods ---------- #
    
    def GetEntity(self, absoluteUri: Uri, role: StringType, ofObjectToReturn: TypeType) -> ObjectType: ...
    
    def set_Credentials(self, value: ICredentials) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlParserContext(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, nt: XmlNameTable, nsMgr: XmlNamespaceManager, xmlLang: StringType, xmlSpace: XmlSpace): ...
    
    @overload
    def __init__(self, nt: XmlNameTable, nsMgr: XmlNamespaceManager, xmlLang: StringType, xmlSpace: XmlSpace, enc: Encoding): ...
    
    @overload
    def __init__(self, nt: XmlNameTable, nsMgr: XmlNamespaceManager, docTypeName: StringType, pubId: StringType, sysId: StringType, internalSubset: StringType, baseURI: StringType, xmlLang: StringType, xmlSpace: XmlSpace): ...
    
    @overload
    def __init__(self, nt: XmlNameTable, nsMgr: XmlNamespaceManager, docTypeName: StringType, pubId: StringType, sysId: StringType, internalSubset: StringType, baseURI: StringType, xmlLang: StringType, xmlSpace: XmlSpace, enc: Encoding): ...
    
    # ---------- Properties ---------- #
    
    @property
    def BaseURI(self) -> StringType: ...
    
    @BaseURI.setter
    def BaseURI(self, value: StringType) -> None: ...
    
    @property
    def DocTypeName(self) -> StringType: ...
    
    @DocTypeName.setter
    def DocTypeName(self, value: StringType) -> None: ...
    
    @property
    def Encoding(self) -> Encoding: ...
    
    @Encoding.setter
    def Encoding(self, value: Encoding) -> None: ...
    
    @property
    def InternalSubset(self) -> StringType: ...
    
    @InternalSubset.setter
    def InternalSubset(self, value: StringType) -> None: ...
    
    @property
    def NameTable(self) -> XmlNameTable: ...
    
    @NameTable.setter
    def NameTable(self, value: XmlNameTable) -> None: ...
    
    @property
    def NamespaceManager(self) -> XmlNamespaceManager: ...
    
    @NamespaceManager.setter
    def NamespaceManager(self, value: XmlNamespaceManager) -> None: ...
    
    @property
    def PublicId(self) -> StringType: ...
    
    @PublicId.setter
    def PublicId(self, value: StringType) -> None: ...
    
    @property
    def SystemId(self) -> StringType: ...
    
    @SystemId.setter
    def SystemId(self, value: StringType) -> None: ...
    
    @property
    def XmlLang(self) -> StringType: ...
    
    @XmlLang.setter
    def XmlLang(self, value: StringType) -> None: ...
    
    @property
    def XmlSpace(self) -> XmlSpace: ...
    
    @XmlSpace.setter
    def XmlSpace(self, value: XmlSpace) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_BaseURI(self) -> StringType: ...
    
    def get_DocTypeName(self) -> StringType: ...
    
    def get_Encoding(self) -> Encoding: ...
    
    def get_InternalSubset(self) -> StringType: ...
    
    def get_NameTable(self) -> XmlNameTable: ...
    
    def get_NamespaceManager(self) -> XmlNamespaceManager: ...
    
    def get_PublicId(self) -> StringType: ...
    
    def get_SystemId(self) -> StringType: ...
    
    def get_XmlLang(self) -> StringType: ...
    
    def get_XmlSpace(self) -> XmlSpace: ...
    
    def set_BaseURI(self, value: StringType) -> VoidType: ...
    
    def set_DocTypeName(self, value: StringType) -> VoidType: ...
    
    def set_Encoding(self, value: Encoding) -> VoidType: ...
    
    def set_InternalSubset(self, value: StringType) -> VoidType: ...
    
    def set_NameTable(self, value: XmlNameTable) -> VoidType: ...
    
    def set_NamespaceManager(self, value: XmlNamespaceManager) -> VoidType: ...
    
    def set_PublicId(self, value: StringType) -> VoidType: ...
    
    def set_SystemId(self, value: StringType) -> VoidType: ...
    
    def set_XmlLang(self, value: StringType) -> VoidType: ...
    
    def set_XmlSpace(self, value: XmlSpace) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlParserContext(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, nt: XmlNameTable, nsMgr: XmlNamespaceManager, xmlLang: StringType, xmlSpace: XmlSpace): ...
    
    @overload
    def __init__(self, nt: XmlNameTable, nsMgr: XmlNamespaceManager, xmlLang: StringType, xmlSpace: XmlSpace, enc: Encoding): ...
    
    @overload
    def __init__(self, nt: XmlNameTable, nsMgr: XmlNamespaceManager, docTypeName: StringType, pubId: StringType, sysId: StringType, internalSubset: StringType, baseURI: StringType, xmlLang: StringType, xmlSpace: XmlSpace): ...
    
    @overload
    def __init__(self, nt: XmlNameTable, nsMgr: XmlNamespaceManager, docTypeName: StringType, pubId: StringType, sysId: StringType, internalSubset: StringType, baseURI: StringType, xmlLang: StringType, xmlSpace: XmlSpace, enc: Encoding): ...
    
    # ---------- Properties ---------- #
    
    @property
    def BaseURI(self) -> StringType: ...
    
    @BaseURI.setter
    def BaseURI(self, value: StringType) -> None: ...
    
    @property
    def DocTypeName(self) -> StringType: ...
    
    @DocTypeName.setter
    def DocTypeName(self, value: StringType) -> None: ...
    
    @property
    def Encoding(self) -> Encoding: ...
    
    @Encoding.setter
    def Encoding(self, value: Encoding) -> None: ...
    
    @property
    def InternalSubset(self) -> StringType: ...
    
    @InternalSubset.setter
    def InternalSubset(self, value: StringType) -> None: ...
    
    @property
    def NameTable(self) -> XmlNameTable: ...
    
    @NameTable.setter
    def NameTable(self, value: XmlNameTable) -> None: ...
    
    @property
    def NamespaceManager(self) -> XmlNamespaceManager: ...
    
    @NamespaceManager.setter
    def NamespaceManager(self, value: XmlNamespaceManager) -> None: ...
    
    @property
    def PublicId(self) -> StringType: ...
    
    @PublicId.setter
    def PublicId(self, value: StringType) -> None: ...
    
    @property
    def SystemId(self) -> StringType: ...
    
    @SystemId.setter
    def SystemId(self, value: StringType) -> None: ...
    
    @property
    def XmlLang(self) -> StringType: ...
    
    @XmlLang.setter
    def XmlLang(self, value: StringType) -> None: ...
    
    @property
    def XmlSpace(self) -> XmlSpace: ...
    
    @XmlSpace.setter
    def XmlSpace(self, value: XmlSpace) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_BaseURI(self) -> StringType: ...
    
    def get_DocTypeName(self) -> StringType: ...
    
    def get_Encoding(self) -> Encoding: ...
    
    def get_InternalSubset(self) -> StringType: ...
    
    def get_NameTable(self) -> XmlNameTable: ...
    
    def get_NamespaceManager(self) -> XmlNamespaceManager: ...
    
    def get_PublicId(self) -> StringType: ...
    
    def get_SystemId(self) -> StringType: ...
    
    def get_XmlLang(self) -> StringType: ...
    
    def get_XmlSpace(self) -> XmlSpace: ...
    
    def set_BaseURI(self, value: StringType) -> VoidType: ...
    
    def set_DocTypeName(self, value: StringType) -> VoidType: ...
    
    def set_Encoding(self, value: Encoding) -> VoidType: ...
    
    def set_InternalSubset(self, value: StringType) -> VoidType: ...
    
    def set_NameTable(self, value: XmlNameTable) -> VoidType: ...
    
    def set_NamespaceManager(self, value: XmlNamespaceManager) -> VoidType: ...
    
    def set_PublicId(self, value: StringType) -> VoidType: ...
    
    def set_SystemId(self, value: StringType) -> VoidType: ...
    
    def set_XmlLang(self, value: StringType) -> VoidType: ...
    
    def set_XmlSpace(self, value: XmlSpace) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlProcessingInstruction(XmlLinkedNode, ICloneable, IEnumerable, IXPathNavigable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Data(self) -> StringType: ...
    
    @Data.setter
    def Data(self, value: StringType) -> None: ...
    
    @property
    def InnerText(self) -> StringType: ...
    
    @InnerText.setter
    def InnerText(self, value: StringType) -> None: ...
    
    @property
    def LocalName(self) -> StringType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def NodeType(self) -> XmlNodeType: ...
    
    @property
    def Target(self) -> StringType: ...
    
    @property
    def Value(self) -> StringType: ...
    
    @Value.setter
    def Value(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def CloneNode(self, deep: BooleanType) -> XmlNode: ...
    
    def WriteContentTo(self, w: XmlWriter) -> VoidType: ...
    
    def WriteTo(self, w: XmlWriter) -> VoidType: ...
    
    def get_Data(self) -> StringType: ...
    
    def get_InnerText(self) -> StringType: ...
    
    def get_LocalName(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_NodeType(self) -> XmlNodeType: ...
    
    def get_Target(self) -> StringType: ...
    
    def get_Value(self) -> StringType: ...
    
    def set_Data(self, value: StringType) -> VoidType: ...
    
    def set_InnerText(self, value: StringType) -> VoidType: ...
    
    def set_Value(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlProcessingInstruction(XmlLinkedNode, ICloneable, IEnumerable, IXPathNavigable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Data(self) -> StringType: ...
    
    @Data.setter
    def Data(self, value: StringType) -> None: ...
    
    @property
    def InnerText(self) -> StringType: ...
    
    @InnerText.setter
    def InnerText(self, value: StringType) -> None: ...
    
    @property
    def LocalName(self) -> StringType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def NodeType(self) -> XmlNodeType: ...
    
    @property
    def Target(self) -> StringType: ...
    
    @property
    def Value(self) -> StringType: ...
    
    @Value.setter
    def Value(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def CloneNode(self, deep: BooleanType) -> XmlNode: ...
    
    def WriteContentTo(self, w: XmlWriter) -> VoidType: ...
    
    def WriteTo(self, w: XmlWriter) -> VoidType: ...
    
    def get_Data(self) -> StringType: ...
    
    def get_InnerText(self) -> StringType: ...
    
    def get_LocalName(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_NodeType(self) -> XmlNodeType: ...
    
    def get_Target(self) -> StringType: ...
    
    def get_Value(self) -> StringType: ...
    
    def set_Data(self, value: StringType) -> VoidType: ...
    
    def set_InnerText(self, value: StringType) -> VoidType: ...
    
    def set_Value(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlQualifiedName(ObjectType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Empty() -> XmlQualifiedName: ...
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, name: StringType): ...
    
    @overload
    def __init__(self, name: StringType, ns: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def IsEmpty(self) -> BooleanType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def Namespace(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, other: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    @overload
    def ToString(self) -> StringType: ...
    
    @staticmethod
    @overload
    def ToString(name: StringType, ns: StringType) -> StringType: ...
    
    def get_IsEmpty(self) -> BooleanType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_Namespace(self) -> StringType: ...
    
    @staticmethod
    def op_Equality(a: XmlQualifiedName, b: XmlQualifiedName) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(a: XmlQualifiedName, b: XmlQualifiedName) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlQualifiedName(ObjectType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Empty() -> XmlQualifiedName: ...
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, name: StringType): ...
    
    @overload
    def __init__(self, name: StringType, ns: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def IsEmpty(self) -> BooleanType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def Namespace(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, other: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    @overload
    def ToString(self) -> StringType: ...
    
    @staticmethod
    @overload
    def ToString(name: StringType, ns: StringType) -> StringType: ...
    
    def get_IsEmpty(self) -> BooleanType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_Namespace(self) -> StringType: ...
    
    @staticmethod
    def op_Equality(a: XmlQualifiedName, b: XmlQualifiedName) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(a: XmlQualifiedName, b: XmlQualifiedName) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlRawWriter(ABC, XmlWriter, IDisposable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def WriteState(self) -> WriteState: ...
    
    @property
    def XmlLang(self) -> StringType: ...
    
    @property
    def XmlSpace(self) -> XmlSpace: ...
    
    # ---------- Methods ---------- #
    
    def LookupPrefix(self, ns: StringType) -> StringType: ...
    
    def WriteAttributes(self, reader: XmlReader, defattr: BooleanType) -> VoidType: ...
    
    def WriteAttributesAsync(self, reader: XmlReader, defattr: BooleanType) -> Task: ...
    
    def WriteBase64(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> VoidType: ...
    
    def WriteBase64Async(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> Task: ...
    
    def WriteCData(self, text: StringType) -> VoidType: ...
    
    def WriteCDataAsync(self, text: StringType) -> Task: ...
    
    def WriteCharEntity(self, ch: CharType) -> VoidType: ...
    
    def WriteCharEntityAsync(self, ch: CharType) -> Task: ...
    
    def WriteChars(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> VoidType: ...
    
    def WriteCharsAsync(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> Task: ...
    
    def WriteDocType(self, name: StringType, pubid: StringType, sysid: StringType, subset: StringType) -> VoidType: ...
    
    def WriteDocTypeAsync(self, name: StringType, pubid: StringType, sysid: StringType, subset: StringType) -> Task: ...
    
    def WriteEndDocument(self) -> VoidType: ...
    
    def WriteEndDocumentAsync(self) -> Task: ...
    
    def WriteEndElement(self) -> VoidType: ...
    
    def WriteEndElementAsync(self) -> Task: ...
    
    def WriteFullEndElement(self) -> VoidType: ...
    
    def WriteFullEndElementAsync(self) -> Task: ...
    
    def WriteName(self, name: StringType) -> VoidType: ...
    
    def WriteNameAsync(self, name: StringType) -> Task: ...
    
    def WriteNmToken(self, name: StringType) -> VoidType: ...
    
    def WriteNmTokenAsync(self, name: StringType) -> Task: ...
    
    @overload
    def WriteNode(self, reader: XmlReader, defattr: BooleanType) -> VoidType: ...
    
    @overload
    def WriteNode(self, navigator: XPathNavigator, defattr: BooleanType) -> VoidType: ...
    
    @overload
    def WriteNodeAsync(self, reader: XmlReader, defattr: BooleanType) -> Task: ...
    
    @overload
    def WriteNodeAsync(self, navigator: XPathNavigator, defattr: BooleanType) -> Task: ...
    
    def WriteQualifiedName(self, localName: StringType, ns: StringType) -> VoidType: ...
    
    def WriteQualifiedNameAsync(self, localName: StringType, ns: StringType) -> Task: ...
    
    @overload
    def WriteRaw(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> VoidType: ...
    
    @overload
    def WriteRaw(self, data: StringType) -> VoidType: ...
    
    @overload
    def WriteRawAsync(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> Task: ...
    
    @overload
    def WriteRawAsync(self, data: StringType) -> Task: ...
    
    @overload
    def WriteStartDocument(self) -> VoidType: ...
    
    @overload
    def WriteStartDocument(self, standalone: BooleanType) -> VoidType: ...
    
    @overload
    def WriteStartDocumentAsync(self) -> Task: ...
    
    @overload
    def WriteStartDocumentAsync(self, standalone: BooleanType) -> Task: ...
    
    def WriteSurrogateCharEntity(self, lowChar: CharType, highChar: CharType) -> VoidType: ...
    
    def WriteSurrogateCharEntityAsync(self, lowChar: CharType, highChar: CharType) -> Task: ...
    
    @overload
    def WriteValue(self, value: ObjectType) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: StringType) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: DateTimeOffset) -> VoidType: ...
    
    def WriteWhitespace(self, ws: StringType) -> VoidType: ...
    
    def WriteWhitespaceAsync(self, ws: StringType) -> Task: ...
    
    def get_WriteState(self) -> WriteState: ...
    
    def get_XmlLang(self) -> StringType: ...
    
    def get_XmlSpace(self) -> XmlSpace: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlRawWriter(ABC, XmlWriter, IDisposable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def WriteState(self) -> WriteState: ...
    
    @property
    def XmlLang(self) -> StringType: ...
    
    @property
    def XmlSpace(self) -> XmlSpace: ...
    
    # ---------- Methods ---------- #
    
    def LookupPrefix(self, ns: StringType) -> StringType: ...
    
    def WriteAttributes(self, reader: XmlReader, defattr: BooleanType) -> VoidType: ...
    
    def WriteAttributesAsync(self, reader: XmlReader, defattr: BooleanType) -> Task: ...
    
    def WriteBase64(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> VoidType: ...
    
    def WriteBase64Async(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> Task: ...
    
    def WriteCData(self, text: StringType) -> VoidType: ...
    
    def WriteCDataAsync(self, text: StringType) -> Task: ...
    
    def WriteCharEntity(self, ch: CharType) -> VoidType: ...
    
    def WriteCharEntityAsync(self, ch: CharType) -> Task: ...
    
    def WriteChars(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> VoidType: ...
    
    def WriteCharsAsync(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> Task: ...
    
    def WriteDocType(self, name: StringType, pubid: StringType, sysid: StringType, subset: StringType) -> VoidType: ...
    
    def WriteDocTypeAsync(self, name: StringType, pubid: StringType, sysid: StringType, subset: StringType) -> Task: ...
    
    def WriteEndDocument(self) -> VoidType: ...
    
    def WriteEndDocumentAsync(self) -> Task: ...
    
    def WriteEndElement(self) -> VoidType: ...
    
    def WriteEndElementAsync(self) -> Task: ...
    
    def WriteFullEndElement(self) -> VoidType: ...
    
    def WriteFullEndElementAsync(self) -> Task: ...
    
    def WriteName(self, name: StringType) -> VoidType: ...
    
    def WriteNameAsync(self, name: StringType) -> Task: ...
    
    def WriteNmToken(self, name: StringType) -> VoidType: ...
    
    def WriteNmTokenAsync(self, name: StringType) -> Task: ...
    
    @overload
    def WriteNode(self, reader: XmlReader, defattr: BooleanType) -> VoidType: ...
    
    @overload
    def WriteNode(self, navigator: XPathNavigator, defattr: BooleanType) -> VoidType: ...
    
    @overload
    def WriteNodeAsync(self, reader: XmlReader, defattr: BooleanType) -> Task: ...
    
    @overload
    def WriteNodeAsync(self, navigator: XPathNavigator, defattr: BooleanType) -> Task: ...
    
    def WriteQualifiedName(self, localName: StringType, ns: StringType) -> VoidType: ...
    
    def WriteQualifiedNameAsync(self, localName: StringType, ns: StringType) -> Task: ...
    
    @overload
    def WriteRaw(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> VoidType: ...
    
    @overload
    def WriteRaw(self, data: StringType) -> VoidType: ...
    
    @overload
    def WriteRawAsync(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> Task: ...
    
    @overload
    def WriteRawAsync(self, data: StringType) -> Task: ...
    
    @overload
    def WriteStartDocument(self) -> VoidType: ...
    
    @overload
    def WriteStartDocument(self, standalone: BooleanType) -> VoidType: ...
    
    @overload
    def WriteStartDocumentAsync(self) -> Task: ...
    
    @overload
    def WriteStartDocumentAsync(self, standalone: BooleanType) -> Task: ...
    
    def WriteSurrogateCharEntity(self, lowChar: CharType, highChar: CharType) -> VoidType: ...
    
    def WriteSurrogateCharEntityAsync(self, lowChar: CharType, highChar: CharType) -> Task: ...
    
    @overload
    def WriteValue(self, value: ObjectType) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: StringType) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: DateTimeOffset) -> VoidType: ...
    
    def WriteWhitespace(self, ws: StringType) -> VoidType: ...
    
    def WriteWhitespaceAsync(self, ws: StringType) -> Task: ...
    
    def get_WriteState(self) -> WriteState: ...
    
    def get_XmlLang(self) -> StringType: ...
    
    def get_XmlSpace(self) -> XmlSpace: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlRawWriterBase64Encoder(Base64Encoder):
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


class XmlRawWriterBase64Encoder(Base64Encoder):
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


class XmlReader(ABC, ObjectType, IDisposable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def AttributeCount(self) -> IntType: ...
    
    @property
    def BaseURI(self) -> StringType: ...
    
    @property
    def CanReadBinaryContent(self) -> BooleanType: ...
    
    @property
    def CanReadValueChunk(self) -> BooleanType: ...
    
    @property
    def CanResolveEntity(self) -> BooleanType: ...
    
    @property
    def Depth(self) -> IntType: ...
    
    @property
    def EOF(self) -> BooleanType: ...
    
    @property
    def HasAttributes(self) -> BooleanType: ...
    
    @property
    def HasValue(self) -> BooleanType: ...
    
    @property
    def IsDefault(self) -> BooleanType: ...
    
    @property
    def IsEmptyElement(self) -> BooleanType: ...
    
    def __getitem__(self, key: IntType) -> StringType: ...
    
    def __getitem__(self, key: StringType) -> StringType: ...
    
    def __getitem__(self, key: StringType) -> StringType: ...
    
    @property
    def LocalName(self) -> StringType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def NameTable(self) -> XmlNameTable: ...
    
    @property
    def NamespaceURI(self) -> StringType: ...
    
    @property
    def NodeType(self) -> XmlNodeType: ...
    
    @property
    def Prefix(self) -> StringType: ...
    
    @property
    def QuoteChar(self) -> CharType: ...
    
    @property
    def ReadState(self) -> ReadState: ...
    
    @property
    def SchemaInfo(self) -> IXmlSchemaInfo: ...
    
    @property
    def Settings(self) -> XmlReaderSettings: ...
    
    @property
    def Value(self) -> StringType: ...
    
    @property
    def ValueType(self) -> TypeType: ...
    
    @property
    def XmlLang(self) -> StringType: ...
    
    @property
    def XmlSpace(self) -> XmlSpace: ...
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    @staticmethod
    @overload
    def Create(inputUri: StringType) -> XmlReader: ...
    
    @staticmethod
    @overload
    def Create(inputUri: StringType, settings: XmlReaderSettings) -> XmlReader: ...
    
    @staticmethod
    @overload
    def Create(inputUri: StringType, settings: XmlReaderSettings, inputContext: XmlParserContext) -> XmlReader: ...
    
    @staticmethod
    @overload
    def Create(input: Stream) -> XmlReader: ...
    
    @staticmethod
    @overload
    def Create(input: Stream, settings: XmlReaderSettings) -> XmlReader: ...
    
    @staticmethod
    @overload
    def Create(input: Stream, settings: XmlReaderSettings, baseUri: StringType) -> XmlReader: ...
    
    @staticmethod
    @overload
    def Create(input: Stream, settings: XmlReaderSettings, inputContext: XmlParserContext) -> XmlReader: ...
    
    @staticmethod
    @overload
    def Create(input: TextReader) -> XmlReader: ...
    
    @staticmethod
    @overload
    def Create(input: TextReader, settings: XmlReaderSettings) -> XmlReader: ...
    
    @staticmethod
    @overload
    def Create(input: TextReader, settings: XmlReaderSettings, baseUri: StringType) -> XmlReader: ...
    
    @staticmethod
    @overload
    def Create(input: TextReader, settings: XmlReaderSettings, inputContext: XmlParserContext) -> XmlReader: ...
    
    @staticmethod
    @overload
    def Create(reader: XmlReader, settings: XmlReaderSettings) -> XmlReader: ...
    
    def Dispose(self) -> VoidType: ...
    
    @overload
    def GetAttribute(self, name: StringType) -> StringType: ...
    
    @overload
    def GetAttribute(self, name: StringType, namespaceURI: StringType) -> StringType: ...
    
    @overload
    def GetAttribute(self, i: IntType) -> StringType: ...
    
    def GetValueAsync(self) -> Task[StringType]: ...
    
    @staticmethod
    def IsName(str: StringType) -> BooleanType: ...
    
    @staticmethod
    def IsNameToken(str: StringType) -> BooleanType: ...
    
    @overload
    def IsStartElement(self) -> BooleanType: ...
    
    @overload
    def IsStartElement(self, name: StringType) -> BooleanType: ...
    
    @overload
    def IsStartElement(self, localname: StringType, ns: StringType) -> BooleanType: ...
    
    def LookupNamespace(self, prefix: StringType) -> StringType: ...
    
    @overload
    def MoveToAttribute(self, i: IntType) -> VoidType: ...
    
    @overload
    def MoveToAttribute(self, name: StringType) -> BooleanType: ...
    
    @overload
    def MoveToAttribute(self, name: StringType, ns: StringType) -> BooleanType: ...
    
    def MoveToContent(self) -> XmlNodeType: ...
    
    def MoveToContentAsync(self) -> Task[XmlNodeType]: ...
    
    def MoveToElement(self) -> BooleanType: ...
    
    def MoveToFirstAttribute(self) -> BooleanType: ...
    
    def MoveToNextAttribute(self) -> BooleanType: ...
    
    def Read(self) -> BooleanType: ...
    
    def ReadAsync(self) -> Task[BooleanType]: ...
    
    def ReadAttributeValue(self) -> BooleanType: ...
    
    def ReadContentAs(self, returnType: TypeType, namespaceResolver: IXmlNamespaceResolver) -> ObjectType: ...
    
    def ReadContentAsAsync(self, returnType: TypeType, namespaceResolver: IXmlNamespaceResolver) -> Task[ObjectType]: ...
    
    def ReadContentAsBase64(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadContentAsBase64Async(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> Task[IntType]: ...
    
    def ReadContentAsBinHex(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadContentAsBinHexAsync(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> Task[IntType]: ...
    
    def ReadContentAsBoolean(self) -> BooleanType: ...
    
    def ReadContentAsDateTime(self) -> DateTime: ...
    
    def ReadContentAsDateTimeOffset(self) -> DateTimeOffset: ...
    
    def ReadContentAsDecimal(self) -> DecimalType: ...
    
    def ReadContentAsDouble(self) -> DoubleType: ...
    
    def ReadContentAsFloat(self) -> FloatType: ...
    
    def ReadContentAsInt(self) -> IntType: ...
    
    def ReadContentAsLong(self) -> LongType: ...
    
    def ReadContentAsObject(self) -> ObjectType: ...
    
    def ReadContentAsObjectAsync(self) -> Task[ObjectType]: ...
    
    def ReadContentAsString(self) -> StringType: ...
    
    def ReadContentAsStringAsync(self) -> Task[StringType]: ...
    
    @overload
    def ReadElementContentAs(self, returnType: TypeType, namespaceResolver: IXmlNamespaceResolver, localName: StringType, namespaceURI: StringType) -> ObjectType: ...
    
    @overload
    def ReadElementContentAs(self, returnType: TypeType, namespaceResolver: IXmlNamespaceResolver) -> ObjectType: ...
    
    def ReadElementContentAsAsync(self, returnType: TypeType, namespaceResolver: IXmlNamespaceResolver) -> Task[ObjectType]: ...
    
    def ReadElementContentAsBase64(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadElementContentAsBase64Async(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> Task[IntType]: ...
    
    def ReadElementContentAsBinHex(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadElementContentAsBinHexAsync(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> Task[IntType]: ...
    
    @overload
    def ReadElementContentAsBoolean(self, localName: StringType, namespaceURI: StringType) -> BooleanType: ...
    
    @overload
    def ReadElementContentAsBoolean(self) -> BooleanType: ...
    
    @overload
    def ReadElementContentAsDateTime(self, localName: StringType, namespaceURI: StringType) -> DateTime: ...
    
    @overload
    def ReadElementContentAsDateTime(self) -> DateTime: ...
    
    @overload
    def ReadElementContentAsDecimal(self, localName: StringType, namespaceURI: StringType) -> DecimalType: ...
    
    @overload
    def ReadElementContentAsDecimal(self) -> DecimalType: ...
    
    @overload
    def ReadElementContentAsDouble(self, localName: StringType, namespaceURI: StringType) -> DoubleType: ...
    
    @overload
    def ReadElementContentAsDouble(self) -> DoubleType: ...
    
    @overload
    def ReadElementContentAsFloat(self, localName: StringType, namespaceURI: StringType) -> FloatType: ...
    
    @overload
    def ReadElementContentAsFloat(self) -> FloatType: ...
    
    @overload
    def ReadElementContentAsInt(self, localName: StringType, namespaceURI: StringType) -> IntType: ...
    
    @overload
    def ReadElementContentAsInt(self) -> IntType: ...
    
    @overload
    def ReadElementContentAsLong(self, localName: StringType, namespaceURI: StringType) -> LongType: ...
    
    @overload
    def ReadElementContentAsLong(self) -> LongType: ...
    
    @overload
    def ReadElementContentAsObject(self, localName: StringType, namespaceURI: StringType) -> ObjectType: ...
    
    @overload
    def ReadElementContentAsObject(self) -> ObjectType: ...
    
    def ReadElementContentAsObjectAsync(self) -> Task[ObjectType]: ...
    
    @overload
    def ReadElementContentAsString(self, localName: StringType, namespaceURI: StringType) -> StringType: ...
    
    @overload
    def ReadElementContentAsString(self) -> StringType: ...
    
    def ReadElementContentAsStringAsync(self) -> Task[StringType]: ...
    
    @overload
    def ReadElementString(self, name: StringType) -> StringType: ...
    
    @overload
    def ReadElementString(self) -> StringType: ...
    
    @overload
    def ReadElementString(self, localname: StringType, ns: StringType) -> StringType: ...
    
    def ReadEndElement(self) -> VoidType: ...
    
    def ReadInnerXml(self) -> StringType: ...
    
    def ReadInnerXmlAsync(self) -> Task[StringType]: ...
    
    def ReadOuterXml(self) -> StringType: ...
    
    def ReadOuterXmlAsync(self) -> Task[StringType]: ...
    
    @overload
    def ReadStartElement(self) -> VoidType: ...
    
    @overload
    def ReadStartElement(self, name: StringType) -> VoidType: ...
    
    @overload
    def ReadStartElement(self, localname: StringType, ns: StringType) -> VoidType: ...
    
    def ReadString(self) -> StringType: ...
    
    def ReadSubtree(self) -> XmlReader: ...
    
    @overload
    def ReadToDescendant(self, name: StringType) -> BooleanType: ...
    
    @overload
    def ReadToDescendant(self, localName: StringType, namespaceURI: StringType) -> BooleanType: ...
    
    @overload
    def ReadToFollowing(self, name: StringType) -> BooleanType: ...
    
    @overload
    def ReadToFollowing(self, localName: StringType, namespaceURI: StringType) -> BooleanType: ...
    
    @overload
    def ReadToNextSibling(self, name: StringType) -> BooleanType: ...
    
    @overload
    def ReadToNextSibling(self, localName: StringType, namespaceURI: StringType) -> BooleanType: ...
    
    def ReadValueChunk(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadValueChunkAsync(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> Task[IntType]: ...
    
    def ResolveEntity(self) -> VoidType: ...
    
    def Skip(self) -> VoidType: ...
    
    def SkipAsync(self) -> Task: ...
    
    def get_AttributeCount(self) -> IntType: ...
    
    def get_BaseURI(self) -> StringType: ...
    
    def get_CanReadBinaryContent(self) -> BooleanType: ...
    
    def get_CanReadValueChunk(self) -> BooleanType: ...
    
    def get_CanResolveEntity(self) -> BooleanType: ...
    
    def get_Depth(self) -> IntType: ...
    
    def get_EOF(self) -> BooleanType: ...
    
    def get_HasAttributes(self) -> BooleanType: ...
    
    def get_HasValue(self) -> BooleanType: ...
    
    def get_IsDefault(self) -> BooleanType: ...
    
    def get_IsEmptyElement(self) -> BooleanType: ...
    
    @overload
    def get_Item(self, i: IntType) -> StringType: ...
    
    @overload
    def get_Item(self, name: StringType) -> StringType: ...
    
    @overload
    def get_Item(self, name: StringType, namespaceURI: StringType) -> StringType: ...
    
    def get_LocalName(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_NameTable(self) -> XmlNameTable: ...
    
    def get_NamespaceURI(self) -> StringType: ...
    
    def get_NodeType(self) -> XmlNodeType: ...
    
    def get_Prefix(self) -> StringType: ...
    
    def get_QuoteChar(self) -> CharType: ...
    
    def get_ReadState(self) -> ReadState: ...
    
    def get_SchemaInfo(self) -> IXmlSchemaInfo: ...
    
    def get_Settings(self) -> XmlReaderSettings: ...
    
    def get_Value(self) -> StringType: ...
    
    def get_ValueType(self) -> TypeType: ...
    
    def get_XmlLang(self) -> StringType: ...
    
    def get_XmlSpace(self) -> XmlSpace: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlReader(ABC, ObjectType, IDisposable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def AttributeCount(self) -> IntType: ...
    
    @property
    def BaseURI(self) -> StringType: ...
    
    @property
    def CanReadBinaryContent(self) -> BooleanType: ...
    
    @property
    def CanReadValueChunk(self) -> BooleanType: ...
    
    @property
    def CanResolveEntity(self) -> BooleanType: ...
    
    @property
    def Depth(self) -> IntType: ...
    
    @property
    def EOF(self) -> BooleanType: ...
    
    @property
    def HasAttributes(self) -> BooleanType: ...
    
    @property
    def HasValue(self) -> BooleanType: ...
    
    @property
    def IsDefault(self) -> BooleanType: ...
    
    @property
    def IsEmptyElement(self) -> BooleanType: ...
    
    def __getitem__(self, key: IntType) -> StringType: ...
    
    def __getitem__(self, key: StringType) -> StringType: ...
    
    def __getitem__(self, key: StringType) -> StringType: ...
    
    @property
    def LocalName(self) -> StringType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def NameTable(self) -> XmlNameTable: ...
    
    @property
    def NamespaceURI(self) -> StringType: ...
    
    @property
    def NodeType(self) -> XmlNodeType: ...
    
    @property
    def Prefix(self) -> StringType: ...
    
    @property
    def QuoteChar(self) -> CharType: ...
    
    @property
    def ReadState(self) -> ReadState: ...
    
    @property
    def SchemaInfo(self) -> IXmlSchemaInfo: ...
    
    @property
    def Settings(self) -> XmlReaderSettings: ...
    
    @property
    def Value(self) -> StringType: ...
    
    @property
    def ValueType(self) -> TypeType: ...
    
    @property
    def XmlLang(self) -> StringType: ...
    
    @property
    def XmlSpace(self) -> XmlSpace: ...
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    @staticmethod
    @overload
    def Create(inputUri: StringType) -> XmlReader: ...
    
    @staticmethod
    @overload
    def Create(inputUri: StringType, settings: XmlReaderSettings) -> XmlReader: ...
    
    @staticmethod
    @overload
    def Create(inputUri: StringType, settings: XmlReaderSettings, inputContext: XmlParserContext) -> XmlReader: ...
    
    @staticmethod
    @overload
    def Create(input: Stream) -> XmlReader: ...
    
    @staticmethod
    @overload
    def Create(input: Stream, settings: XmlReaderSettings) -> XmlReader: ...
    
    @staticmethod
    @overload
    def Create(input: Stream, settings: XmlReaderSettings, baseUri: StringType) -> XmlReader: ...
    
    @staticmethod
    @overload
    def Create(input: Stream, settings: XmlReaderSettings, inputContext: XmlParserContext) -> XmlReader: ...
    
    @staticmethod
    @overload
    def Create(input: TextReader) -> XmlReader: ...
    
    @staticmethod
    @overload
    def Create(input: TextReader, settings: XmlReaderSettings) -> XmlReader: ...
    
    @staticmethod
    @overload
    def Create(input: TextReader, settings: XmlReaderSettings, baseUri: StringType) -> XmlReader: ...
    
    @staticmethod
    @overload
    def Create(input: TextReader, settings: XmlReaderSettings, inputContext: XmlParserContext) -> XmlReader: ...
    
    @staticmethod
    @overload
    def Create(reader: XmlReader, settings: XmlReaderSettings) -> XmlReader: ...
    
    def Dispose(self) -> VoidType: ...
    
    @overload
    def GetAttribute(self, name: StringType) -> StringType: ...
    
    @overload
    def GetAttribute(self, name: StringType, namespaceURI: StringType) -> StringType: ...
    
    @overload
    def GetAttribute(self, i: IntType) -> StringType: ...
    
    def GetValueAsync(self) -> Task[StringType]: ...
    
    @staticmethod
    def IsName(str: StringType) -> BooleanType: ...
    
    @staticmethod
    def IsNameToken(str: StringType) -> BooleanType: ...
    
    @overload
    def IsStartElement(self) -> BooleanType: ...
    
    @overload
    def IsStartElement(self, name: StringType) -> BooleanType: ...
    
    @overload
    def IsStartElement(self, localname: StringType, ns: StringType) -> BooleanType: ...
    
    def LookupNamespace(self, prefix: StringType) -> StringType: ...
    
    @overload
    def MoveToAttribute(self, i: IntType) -> VoidType: ...
    
    @overload
    def MoveToAttribute(self, name: StringType) -> BooleanType: ...
    
    @overload
    def MoveToAttribute(self, name: StringType, ns: StringType) -> BooleanType: ...
    
    def MoveToContent(self) -> XmlNodeType: ...
    
    def MoveToContentAsync(self) -> Task[XmlNodeType]: ...
    
    def MoveToElement(self) -> BooleanType: ...
    
    def MoveToFirstAttribute(self) -> BooleanType: ...
    
    def MoveToNextAttribute(self) -> BooleanType: ...
    
    def Read(self) -> BooleanType: ...
    
    def ReadAsync(self) -> Task[BooleanType]: ...
    
    def ReadAttributeValue(self) -> BooleanType: ...
    
    def ReadContentAs(self, returnType: TypeType, namespaceResolver: IXmlNamespaceResolver) -> ObjectType: ...
    
    def ReadContentAsAsync(self, returnType: TypeType, namespaceResolver: IXmlNamespaceResolver) -> Task[ObjectType]: ...
    
    def ReadContentAsBase64(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadContentAsBase64Async(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> Task[IntType]: ...
    
    def ReadContentAsBinHex(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadContentAsBinHexAsync(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> Task[IntType]: ...
    
    def ReadContentAsBoolean(self) -> BooleanType: ...
    
    def ReadContentAsDateTime(self) -> DateTime: ...
    
    def ReadContentAsDateTimeOffset(self) -> DateTimeOffset: ...
    
    def ReadContentAsDecimal(self) -> DecimalType: ...
    
    def ReadContentAsDouble(self) -> DoubleType: ...
    
    def ReadContentAsFloat(self) -> FloatType: ...
    
    def ReadContentAsInt(self) -> IntType: ...
    
    def ReadContentAsLong(self) -> LongType: ...
    
    def ReadContentAsObject(self) -> ObjectType: ...
    
    def ReadContentAsObjectAsync(self) -> Task[ObjectType]: ...
    
    def ReadContentAsString(self) -> StringType: ...
    
    def ReadContentAsStringAsync(self) -> Task[StringType]: ...
    
    @overload
    def ReadElementContentAs(self, returnType: TypeType, namespaceResolver: IXmlNamespaceResolver, localName: StringType, namespaceURI: StringType) -> ObjectType: ...
    
    @overload
    def ReadElementContentAs(self, returnType: TypeType, namespaceResolver: IXmlNamespaceResolver) -> ObjectType: ...
    
    def ReadElementContentAsAsync(self, returnType: TypeType, namespaceResolver: IXmlNamespaceResolver) -> Task[ObjectType]: ...
    
    def ReadElementContentAsBase64(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadElementContentAsBase64Async(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> Task[IntType]: ...
    
    def ReadElementContentAsBinHex(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadElementContentAsBinHexAsync(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> Task[IntType]: ...
    
    @overload
    def ReadElementContentAsBoolean(self, localName: StringType, namespaceURI: StringType) -> BooleanType: ...
    
    @overload
    def ReadElementContentAsBoolean(self) -> BooleanType: ...
    
    @overload
    def ReadElementContentAsDateTime(self, localName: StringType, namespaceURI: StringType) -> DateTime: ...
    
    @overload
    def ReadElementContentAsDateTime(self) -> DateTime: ...
    
    @overload
    def ReadElementContentAsDecimal(self, localName: StringType, namespaceURI: StringType) -> DecimalType: ...
    
    @overload
    def ReadElementContentAsDecimal(self) -> DecimalType: ...
    
    @overload
    def ReadElementContentAsDouble(self, localName: StringType, namespaceURI: StringType) -> DoubleType: ...
    
    @overload
    def ReadElementContentAsDouble(self) -> DoubleType: ...
    
    @overload
    def ReadElementContentAsFloat(self, localName: StringType, namespaceURI: StringType) -> FloatType: ...
    
    @overload
    def ReadElementContentAsFloat(self) -> FloatType: ...
    
    @overload
    def ReadElementContentAsInt(self, localName: StringType, namespaceURI: StringType) -> IntType: ...
    
    @overload
    def ReadElementContentAsInt(self) -> IntType: ...
    
    @overload
    def ReadElementContentAsLong(self, localName: StringType, namespaceURI: StringType) -> LongType: ...
    
    @overload
    def ReadElementContentAsLong(self) -> LongType: ...
    
    @overload
    def ReadElementContentAsObject(self, localName: StringType, namespaceURI: StringType) -> ObjectType: ...
    
    @overload
    def ReadElementContentAsObject(self) -> ObjectType: ...
    
    def ReadElementContentAsObjectAsync(self) -> Task[ObjectType]: ...
    
    @overload
    def ReadElementContentAsString(self, localName: StringType, namespaceURI: StringType) -> StringType: ...
    
    @overload
    def ReadElementContentAsString(self) -> StringType: ...
    
    def ReadElementContentAsStringAsync(self) -> Task[StringType]: ...
    
    @overload
    def ReadElementString(self, name: StringType) -> StringType: ...
    
    @overload
    def ReadElementString(self) -> StringType: ...
    
    @overload
    def ReadElementString(self, localname: StringType, ns: StringType) -> StringType: ...
    
    def ReadEndElement(self) -> VoidType: ...
    
    def ReadInnerXml(self) -> StringType: ...
    
    def ReadInnerXmlAsync(self) -> Task[StringType]: ...
    
    def ReadOuterXml(self) -> StringType: ...
    
    def ReadOuterXmlAsync(self) -> Task[StringType]: ...
    
    @overload
    def ReadStartElement(self) -> VoidType: ...
    
    @overload
    def ReadStartElement(self, name: StringType) -> VoidType: ...
    
    @overload
    def ReadStartElement(self, localname: StringType, ns: StringType) -> VoidType: ...
    
    def ReadString(self) -> StringType: ...
    
    def ReadSubtree(self) -> XmlReader: ...
    
    @overload
    def ReadToDescendant(self, name: StringType) -> BooleanType: ...
    
    @overload
    def ReadToDescendant(self, localName: StringType, namespaceURI: StringType) -> BooleanType: ...
    
    @overload
    def ReadToFollowing(self, name: StringType) -> BooleanType: ...
    
    @overload
    def ReadToFollowing(self, localName: StringType, namespaceURI: StringType) -> BooleanType: ...
    
    @overload
    def ReadToNextSibling(self, name: StringType) -> BooleanType: ...
    
    @overload
    def ReadToNextSibling(self, localName: StringType, namespaceURI: StringType) -> BooleanType: ...
    
    def ReadValueChunk(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadValueChunkAsync(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> Task[IntType]: ...
    
    def ResolveEntity(self) -> VoidType: ...
    
    def Skip(self) -> VoidType: ...
    
    def SkipAsync(self) -> Task: ...
    
    def get_AttributeCount(self) -> IntType: ...
    
    def get_BaseURI(self) -> StringType: ...
    
    def get_CanReadBinaryContent(self) -> BooleanType: ...
    
    def get_CanReadValueChunk(self) -> BooleanType: ...
    
    def get_CanResolveEntity(self) -> BooleanType: ...
    
    def get_Depth(self) -> IntType: ...
    
    def get_EOF(self) -> BooleanType: ...
    
    def get_HasAttributes(self) -> BooleanType: ...
    
    def get_HasValue(self) -> BooleanType: ...
    
    def get_IsDefault(self) -> BooleanType: ...
    
    def get_IsEmptyElement(self) -> BooleanType: ...
    
    @overload
    def get_Item(self, i: IntType) -> StringType: ...
    
    @overload
    def get_Item(self, name: StringType) -> StringType: ...
    
    @overload
    def get_Item(self, name: StringType, namespaceURI: StringType) -> StringType: ...
    
    def get_LocalName(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_NameTable(self) -> XmlNameTable: ...
    
    def get_NamespaceURI(self) -> StringType: ...
    
    def get_NodeType(self) -> XmlNodeType: ...
    
    def get_Prefix(self) -> StringType: ...
    
    def get_QuoteChar(self) -> CharType: ...
    
    def get_ReadState(self) -> ReadState: ...
    
    def get_SchemaInfo(self) -> IXmlSchemaInfo: ...
    
    def get_Settings(self) -> XmlReaderSettings: ...
    
    def get_Value(self) -> StringType: ...
    
    def get_ValueType(self) -> TypeType: ...
    
    def get_XmlLang(self) -> StringType: ...
    
    def get_XmlSpace(self) -> XmlSpace: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlReaderSettings(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, resolver: XmlResolver): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Async(self) -> BooleanType: ...
    
    @Async.setter
    def Async(self, value: BooleanType) -> None: ...
    
    @property
    def CheckCharacters(self) -> BooleanType: ...
    
    @CheckCharacters.setter
    def CheckCharacters(self, value: BooleanType) -> None: ...
    
    @property
    def CloseInput(self) -> BooleanType: ...
    
    @CloseInput.setter
    def CloseInput(self, value: BooleanType) -> None: ...
    
    @property
    def ConformanceLevel(self) -> ConformanceLevel: ...
    
    @ConformanceLevel.setter
    def ConformanceLevel(self, value: ConformanceLevel) -> None: ...
    
    @property
    def DtdProcessing(self) -> DtdProcessing: ...
    
    @DtdProcessing.setter
    def DtdProcessing(self, value: DtdProcessing) -> None: ...
    
    @property
    def IgnoreComments(self) -> BooleanType: ...
    
    @IgnoreComments.setter
    def IgnoreComments(self, value: BooleanType) -> None: ...
    
    @property
    def IgnoreProcessingInstructions(self) -> BooleanType: ...
    
    @IgnoreProcessingInstructions.setter
    def IgnoreProcessingInstructions(self, value: BooleanType) -> None: ...
    
    @property
    def IgnoreWhitespace(self) -> BooleanType: ...
    
    @IgnoreWhitespace.setter
    def IgnoreWhitespace(self, value: BooleanType) -> None: ...
    
    @property
    def LineNumberOffset(self) -> IntType: ...
    
    @LineNumberOffset.setter
    def LineNumberOffset(self, value: IntType) -> None: ...
    
    @property
    def LinePositionOffset(self) -> IntType: ...
    
    @LinePositionOffset.setter
    def LinePositionOffset(self, value: IntType) -> None: ...
    
    @property
    def MaxCharactersFromEntities(self) -> LongType: ...
    
    @MaxCharactersFromEntities.setter
    def MaxCharactersFromEntities(self, value: LongType) -> None: ...
    
    @property
    def MaxCharactersInDocument(self) -> LongType: ...
    
    @MaxCharactersInDocument.setter
    def MaxCharactersInDocument(self, value: LongType) -> None: ...
    
    @property
    def NameTable(self) -> XmlNameTable: ...
    
    @NameTable.setter
    def NameTable(self, value: XmlNameTable) -> None: ...
    
    @property
    def ProhibitDtd(self) -> BooleanType: ...
    
    @ProhibitDtd.setter
    def ProhibitDtd(self, value: BooleanType) -> None: ...
    
    @property
    def Schemas(self) -> XmlSchemaSet: ...
    
    @Schemas.setter
    def Schemas(self, value: XmlSchemaSet) -> None: ...
    
    @property
    def ValidationFlags(self) -> XmlSchemaValidationFlags: ...
    
    @ValidationFlags.setter
    def ValidationFlags(self, value: XmlSchemaValidationFlags) -> None: ...
    
    @property
    def ValidationType(self) -> ValidationType: ...
    
    @ValidationType.setter
    def ValidationType(self, value: ValidationType) -> None: ...
    
    @XmlResolver.setter
    def XmlResolver(self, value: XmlResolver) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XmlReaderSettings: ...
    
    def Reset(self) -> VoidType: ...
    
    def add_ValidationEventHandler(self, value: ValidationEventHandler) -> VoidType: ...
    
    def get_Async(self) -> BooleanType: ...
    
    def get_CheckCharacters(self) -> BooleanType: ...
    
    def get_CloseInput(self) -> BooleanType: ...
    
    def get_ConformanceLevel(self) -> ConformanceLevel: ...
    
    def get_DtdProcessing(self) -> DtdProcessing: ...
    
    def get_IgnoreComments(self) -> BooleanType: ...
    
    def get_IgnoreProcessingInstructions(self) -> BooleanType: ...
    
    def get_IgnoreWhitespace(self) -> BooleanType: ...
    
    def get_LineNumberOffset(self) -> IntType: ...
    
    def get_LinePositionOffset(self) -> IntType: ...
    
    def get_MaxCharactersFromEntities(self) -> LongType: ...
    
    def get_MaxCharactersInDocument(self) -> LongType: ...
    
    def get_NameTable(self) -> XmlNameTable: ...
    
    def get_ProhibitDtd(self) -> BooleanType: ...
    
    def get_Schemas(self) -> XmlSchemaSet: ...
    
    def get_ValidationFlags(self) -> XmlSchemaValidationFlags: ...
    
    def get_ValidationType(self) -> ValidationType: ...
    
    def remove_ValidationEventHandler(self, value: ValidationEventHandler) -> VoidType: ...
    
    def set_Async(self, value: BooleanType) -> VoidType: ...
    
    def set_CheckCharacters(self, value: BooleanType) -> VoidType: ...
    
    def set_CloseInput(self, value: BooleanType) -> VoidType: ...
    
    def set_ConformanceLevel(self, value: ConformanceLevel) -> VoidType: ...
    
    def set_DtdProcessing(self, value: DtdProcessing) -> VoidType: ...
    
    def set_IgnoreComments(self, value: BooleanType) -> VoidType: ...
    
    def set_IgnoreProcessingInstructions(self, value: BooleanType) -> VoidType: ...
    
    def set_IgnoreWhitespace(self, value: BooleanType) -> VoidType: ...
    
    def set_LineNumberOffset(self, value: IntType) -> VoidType: ...
    
    def set_LinePositionOffset(self, value: IntType) -> VoidType: ...
    
    def set_MaxCharactersFromEntities(self, value: LongType) -> VoidType: ...
    
    def set_MaxCharactersInDocument(self, value: LongType) -> VoidType: ...
    
    def set_NameTable(self, value: XmlNameTable) -> VoidType: ...
    
    def set_ProhibitDtd(self, value: BooleanType) -> VoidType: ...
    
    def set_Schemas(self, value: XmlSchemaSet) -> VoidType: ...
    
    def set_ValidationFlags(self, value: XmlSchemaValidationFlags) -> VoidType: ...
    
    def set_ValidationType(self, value: ValidationType) -> VoidType: ...
    
    def set_XmlResolver(self, value: XmlResolver) -> VoidType: ...
    
    # ---------- Events ---------- #
    
    ValidationEventHandler: EventType[ValidationEventHandler] = ...
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlReaderSettings(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, resolver: XmlResolver): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Async(self) -> BooleanType: ...
    
    @Async.setter
    def Async(self, value: BooleanType) -> None: ...
    
    @property
    def CheckCharacters(self) -> BooleanType: ...
    
    @CheckCharacters.setter
    def CheckCharacters(self, value: BooleanType) -> None: ...
    
    @property
    def CloseInput(self) -> BooleanType: ...
    
    @CloseInput.setter
    def CloseInput(self, value: BooleanType) -> None: ...
    
    @property
    def ConformanceLevel(self) -> ConformanceLevel: ...
    
    @ConformanceLevel.setter
    def ConformanceLevel(self, value: ConformanceLevel) -> None: ...
    
    @property
    def DtdProcessing(self) -> DtdProcessing: ...
    
    @DtdProcessing.setter
    def DtdProcessing(self, value: DtdProcessing) -> None: ...
    
    @property
    def IgnoreComments(self) -> BooleanType: ...
    
    @IgnoreComments.setter
    def IgnoreComments(self, value: BooleanType) -> None: ...
    
    @property
    def IgnoreProcessingInstructions(self) -> BooleanType: ...
    
    @IgnoreProcessingInstructions.setter
    def IgnoreProcessingInstructions(self, value: BooleanType) -> None: ...
    
    @property
    def IgnoreWhitespace(self) -> BooleanType: ...
    
    @IgnoreWhitespace.setter
    def IgnoreWhitespace(self, value: BooleanType) -> None: ...
    
    @property
    def LineNumberOffset(self) -> IntType: ...
    
    @LineNumberOffset.setter
    def LineNumberOffset(self, value: IntType) -> None: ...
    
    @property
    def LinePositionOffset(self) -> IntType: ...
    
    @LinePositionOffset.setter
    def LinePositionOffset(self, value: IntType) -> None: ...
    
    @property
    def MaxCharactersFromEntities(self) -> LongType: ...
    
    @MaxCharactersFromEntities.setter
    def MaxCharactersFromEntities(self, value: LongType) -> None: ...
    
    @property
    def MaxCharactersInDocument(self) -> LongType: ...
    
    @MaxCharactersInDocument.setter
    def MaxCharactersInDocument(self, value: LongType) -> None: ...
    
    @property
    def NameTable(self) -> XmlNameTable: ...
    
    @NameTable.setter
    def NameTable(self, value: XmlNameTable) -> None: ...
    
    @property
    def ProhibitDtd(self) -> BooleanType: ...
    
    @ProhibitDtd.setter
    def ProhibitDtd(self, value: BooleanType) -> None: ...
    
    @property
    def Schemas(self) -> XmlSchemaSet: ...
    
    @Schemas.setter
    def Schemas(self, value: XmlSchemaSet) -> None: ...
    
    @property
    def ValidationFlags(self) -> XmlSchemaValidationFlags: ...
    
    @ValidationFlags.setter
    def ValidationFlags(self, value: XmlSchemaValidationFlags) -> None: ...
    
    @property
    def ValidationType(self) -> ValidationType: ...
    
    @ValidationType.setter
    def ValidationType(self, value: ValidationType) -> None: ...
    
    @XmlResolver.setter
    def XmlResolver(self, value: XmlResolver) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XmlReaderSettings: ...
    
    def Reset(self) -> VoidType: ...
    
    def add_ValidationEventHandler(self, value: ValidationEventHandler) -> VoidType: ...
    
    def get_Async(self) -> BooleanType: ...
    
    def get_CheckCharacters(self) -> BooleanType: ...
    
    def get_CloseInput(self) -> BooleanType: ...
    
    def get_ConformanceLevel(self) -> ConformanceLevel: ...
    
    def get_DtdProcessing(self) -> DtdProcessing: ...
    
    def get_IgnoreComments(self) -> BooleanType: ...
    
    def get_IgnoreProcessingInstructions(self) -> BooleanType: ...
    
    def get_IgnoreWhitespace(self) -> BooleanType: ...
    
    def get_LineNumberOffset(self) -> IntType: ...
    
    def get_LinePositionOffset(self) -> IntType: ...
    
    def get_MaxCharactersFromEntities(self) -> LongType: ...
    
    def get_MaxCharactersInDocument(self) -> LongType: ...
    
    def get_NameTable(self) -> XmlNameTable: ...
    
    def get_ProhibitDtd(self) -> BooleanType: ...
    
    def get_Schemas(self) -> XmlSchemaSet: ...
    
    def get_ValidationFlags(self) -> XmlSchemaValidationFlags: ...
    
    def get_ValidationType(self) -> ValidationType: ...
    
    def remove_ValidationEventHandler(self, value: ValidationEventHandler) -> VoidType: ...
    
    def set_Async(self, value: BooleanType) -> VoidType: ...
    
    def set_CheckCharacters(self, value: BooleanType) -> VoidType: ...
    
    def set_CloseInput(self, value: BooleanType) -> VoidType: ...
    
    def set_ConformanceLevel(self, value: ConformanceLevel) -> VoidType: ...
    
    def set_DtdProcessing(self, value: DtdProcessing) -> VoidType: ...
    
    def set_IgnoreComments(self, value: BooleanType) -> VoidType: ...
    
    def set_IgnoreProcessingInstructions(self, value: BooleanType) -> VoidType: ...
    
    def set_IgnoreWhitespace(self, value: BooleanType) -> VoidType: ...
    
    def set_LineNumberOffset(self, value: IntType) -> VoidType: ...
    
    def set_LinePositionOffset(self, value: IntType) -> VoidType: ...
    
    def set_MaxCharactersFromEntities(self, value: LongType) -> VoidType: ...
    
    def set_MaxCharactersInDocument(self, value: LongType) -> VoidType: ...
    
    def set_NameTable(self, value: XmlNameTable) -> VoidType: ...
    
    def set_ProhibitDtd(self, value: BooleanType) -> VoidType: ...
    
    def set_Schemas(self, value: XmlSchemaSet) -> VoidType: ...
    
    def set_ValidationFlags(self, value: XmlSchemaValidationFlags) -> VoidType: ...
    
    def set_ValidationType(self, value: ValidationType) -> VoidType: ...
    
    def set_XmlResolver(self, value: XmlResolver) -> VoidType: ...
    
    # ---------- Events ---------- #
    
    ValidationEventHandler: EventType[ValidationEventHandler] = ...
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlRegisteredNonCachedStream(Stream, IDisposable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def CanRead(self) -> BooleanType: ...
    
    @property
    def CanSeek(self) -> BooleanType: ...
    
    @property
    def CanWrite(self) -> BooleanType: ...
    
    @property
    def Length(self) -> LongType: ...
    
    @property
    def Position(self) -> LongType: ...
    
    @Position.setter
    def Position(self, value: LongType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def BeginRead(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType, callback: AsyncCallback, state: ObjectType) -> IAsyncResult: ...
    
    def BeginWrite(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType, callback: AsyncCallback, state: ObjectType) -> IAsyncResult: ...
    
    def EndRead(self, asyncResult: IAsyncResult) -> IntType: ...
    
    def EndWrite(self, asyncResult: IAsyncResult) -> VoidType: ...
    
    def Flush(self) -> VoidType: ...
    
    def Read(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType) -> IntType: ...
    
    def ReadByte(self) -> IntType: ...
    
    def Seek(self, offset: LongType, origin: SeekOrigin) -> LongType: ...
    
    def SetLength(self, value: LongType) -> VoidType: ...
    
    def Write(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType) -> VoidType: ...
    
    def WriteByte(self, value: ByteType) -> VoidType: ...
    
    def get_CanRead(self) -> BooleanType: ...
    
    def get_CanSeek(self) -> BooleanType: ...
    
    def get_CanWrite(self) -> BooleanType: ...
    
    def get_Length(self) -> LongType: ...
    
    def get_Position(self) -> LongType: ...
    
    def set_Position(self, value: LongType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlRegisteredNonCachedStream(Stream, IDisposable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def CanRead(self) -> BooleanType: ...
    
    @property
    def CanSeek(self) -> BooleanType: ...
    
    @property
    def CanWrite(self) -> BooleanType: ...
    
    @property
    def Length(self) -> LongType: ...
    
    @property
    def Position(self) -> LongType: ...
    
    @Position.setter
    def Position(self, value: LongType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def BeginRead(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType, callback: AsyncCallback, state: ObjectType) -> IAsyncResult: ...
    
    def BeginWrite(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType, callback: AsyncCallback, state: ObjectType) -> IAsyncResult: ...
    
    def EndRead(self, asyncResult: IAsyncResult) -> IntType: ...
    
    def EndWrite(self, asyncResult: IAsyncResult) -> VoidType: ...
    
    def Flush(self) -> VoidType: ...
    
    def Read(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType) -> IntType: ...
    
    def ReadByte(self) -> IntType: ...
    
    def Seek(self, offset: LongType, origin: SeekOrigin) -> LongType: ...
    
    def SetLength(self, value: LongType) -> VoidType: ...
    
    def Write(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType) -> VoidType: ...
    
    def WriteByte(self, value: ByteType) -> VoidType: ...
    
    def get_CanRead(self) -> BooleanType: ...
    
    def get_CanSeek(self) -> BooleanType: ...
    
    def get_CanWrite(self) -> BooleanType: ...
    
    def get_Length(self) -> LongType: ...
    
    def get_Position(self) -> LongType: ...
    
    def set_Position(self, value: LongType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlReservedNs(ABC, ObjectType):
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


class XmlReservedNs(ABC, ObjectType):
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


class XmlResolver(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @Credentials.setter
    def Credentials(self, value: ICredentials) -> None: ...
    
    # ---------- Methods ---------- #
    
    def GetEntity(self, absoluteUri: Uri, role: StringType, ofObjectToReturn: TypeType) -> ObjectType: ...
    
    def GetEntityAsync(self, absoluteUri: Uri, role: StringType, ofObjectToReturn: TypeType) -> Task[ObjectType]: ...
    
    def ResolveUri(self, baseUri: Uri, relativeUri: StringType) -> Uri: ...
    
    def SupportsType(self, absoluteUri: Uri, type: TypeType) -> BooleanType: ...
    
    def set_Credentials(self, value: ICredentials) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlResolver(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @Credentials.setter
    def Credentials(self, value: ICredentials) -> None: ...
    
    # ---------- Methods ---------- #
    
    def GetEntity(self, absoluteUri: Uri, role: StringType, ofObjectToReturn: TypeType) -> ObjectType: ...
    
    def GetEntityAsync(self, absoluteUri: Uri, role: StringType, ofObjectToReturn: TypeType) -> Task[ObjectType]: ...
    
    def ResolveUri(self, baseUri: Uri, relativeUri: StringType) -> Uri: ...
    
    def SupportsType(self, absoluteUri: Uri, type: TypeType) -> BooleanType: ...
    
    def set_Credentials(self, value: ICredentials) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSecureResolver(XmlResolver):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, resolver: XmlResolver, securityUrl: StringType): ...
    
    @overload
    def __init__(self, resolver: XmlResolver, evidence: Evidence): ...
    
    @overload
    def __init__(self, resolver: XmlResolver, permissionSet: PermissionSet): ...
    
    # ---------- Properties ---------- #
    
    @Credentials.setter
    def Credentials(self, value: ICredentials) -> None: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def CreateEvidenceForUrl(securityUrl: StringType) -> Evidence: ...
    
    def GetEntity(self, absoluteUri: Uri, role: StringType, ofObjectToReturn: TypeType) -> ObjectType: ...
    
    def GetEntityAsync(self, absoluteUri: Uri, role: StringType, ofObjectToReturn: TypeType) -> Task[ObjectType]: ...
    
    def ResolveUri(self, baseUri: Uri, relativeUri: StringType) -> Uri: ...
    
    def set_Credentials(self, value: ICredentials) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSecureResolver(XmlResolver):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, resolver: XmlResolver, securityUrl: StringType): ...
    
    @overload
    def __init__(self, resolver: XmlResolver, evidence: Evidence): ...
    
    @overload
    def __init__(self, resolver: XmlResolver, permissionSet: PermissionSet): ...
    
    # ---------- Properties ---------- #
    
    @Credentials.setter
    def Credentials(self, value: ICredentials) -> None: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def CreateEvidenceForUrl(securityUrl: StringType) -> Evidence: ...
    
    def GetEntity(self, absoluteUri: Uri, role: StringType, ofObjectToReturn: TypeType) -> ObjectType: ...
    
    def GetEntityAsync(self, absoluteUri: Uri, role: StringType, ofObjectToReturn: TypeType) -> Task[ObjectType]: ...
    
    def ResolveUri(self, baseUri: Uri, relativeUri: StringType) -> Uri: ...
    
    def set_Credentials(self, value: ICredentials) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSignificantWhitespace(XmlCharacterData, ICloneable, IEnumerable, IXPathNavigable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def LocalName(self) -> StringType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def NodeType(self) -> XmlNodeType: ...
    
    @property
    def ParentNode(self) -> XmlNode: ...
    
    @property
    def PreviousText(self) -> XmlNode: ...
    
    @property
    def Value(self) -> StringType: ...
    
    @Value.setter
    def Value(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def CloneNode(self, deep: BooleanType) -> XmlNode: ...
    
    def WriteContentTo(self, w: XmlWriter) -> VoidType: ...
    
    def WriteTo(self, w: XmlWriter) -> VoidType: ...
    
    def get_LocalName(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_NodeType(self) -> XmlNodeType: ...
    
    def get_ParentNode(self) -> XmlNode: ...
    
    def get_PreviousText(self) -> XmlNode: ...
    
    def get_Value(self) -> StringType: ...
    
    def set_Value(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSignificantWhitespace(XmlCharacterData, ICloneable, IEnumerable, IXPathNavigable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def LocalName(self) -> StringType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def NodeType(self) -> XmlNodeType: ...
    
    @property
    def ParentNode(self) -> XmlNode: ...
    
    @property
    def PreviousText(self) -> XmlNode: ...
    
    @property
    def Value(self) -> StringType: ...
    
    @Value.setter
    def Value(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def CloneNode(self, deep: BooleanType) -> XmlNode: ...
    
    def WriteContentTo(self, w: XmlWriter) -> VoidType: ...
    
    def WriteTo(self, w: XmlWriter) -> VoidType: ...
    
    def get_LocalName(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_NodeType(self) -> XmlNodeType: ...
    
    def get_ParentNode(self) -> XmlNode: ...
    
    def get_PreviousText(self) -> XmlNode: ...
    
    def get_Value(self) -> StringType: ...
    
    def set_Value(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSqlBinaryReader(XmlReader, IDisposable, IXmlNamespaceResolver):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, stream: Stream, data: ArrayType[ByteType], len: IntType, baseUri: StringType, closeInput: BooleanType, settings: XmlReaderSettings): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AttributeCount(self) -> IntType: ...
    
    @property
    def BaseURI(self) -> StringType: ...
    
    @property
    def Depth(self) -> IntType: ...
    
    @property
    def EOF(self) -> BooleanType: ...
    
    @property
    def HasValue(self) -> BooleanType: ...
    
    @property
    def IsEmptyElement(self) -> BooleanType: ...
    
    @property
    def LocalName(self) -> StringType: ...
    
    @property
    def NameTable(self) -> XmlNameTable: ...
    
    @property
    def NamespaceURI(self) -> StringType: ...
    
    @property
    def NodeType(self) -> XmlNodeType: ...
    
    @property
    def Prefix(self) -> StringType: ...
    
    @property
    def ReadState(self) -> ReadState: ...
    
    @property
    def Settings(self) -> XmlReaderSettings: ...
    
    @property
    def Value(self) -> StringType: ...
    
    @property
    def ValueType(self) -> TypeType: ...
    
    @property
    def XmlLang(self) -> StringType: ...
    
    @property
    def XmlSpace(self) -> XmlSpace: ...
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    @overload
    def GetAttribute(self, name: StringType, ns: StringType) -> StringType: ...
    
    @overload
    def GetAttribute(self, name: StringType) -> StringType: ...
    
    @overload
    def GetAttribute(self, i: IntType) -> StringType: ...
    
    def GetValueAsync(self) -> Task[StringType]: ...
    
    def LookupNamespace(self, prefix: StringType) -> StringType: ...
    
    @overload
    def MoveToAttribute(self, name: StringType, ns: StringType) -> BooleanType: ...
    
    @overload
    def MoveToAttribute(self, name: StringType) -> BooleanType: ...
    
    @overload
    def MoveToAttribute(self, i: IntType) -> VoidType: ...
    
    def MoveToContentAsync(self) -> Task[XmlNodeType]: ...
    
    def MoveToElement(self) -> BooleanType: ...
    
    def MoveToFirstAttribute(self) -> BooleanType: ...
    
    def MoveToNextAttribute(self) -> BooleanType: ...
    
    def Read(self) -> BooleanType: ...
    
    def ReadAsync(self) -> Task[BooleanType]: ...
    
    def ReadAttributeValue(self) -> BooleanType: ...
    
    def ReadContentAs(self, returnType: TypeType, namespaceResolver: IXmlNamespaceResolver) -> ObjectType: ...
    
    def ReadContentAsAsync(self, returnType: TypeType, namespaceResolver: IXmlNamespaceResolver) -> Task[ObjectType]: ...
    
    def ReadContentAsBase64Async(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> Task[IntType]: ...
    
    def ReadContentAsBoolean(self) -> BooleanType: ...
    
    def ReadContentAsDateTime(self) -> DateTime: ...
    
    def ReadContentAsDecimal(self) -> DecimalType: ...
    
    def ReadContentAsDouble(self) -> DoubleType: ...
    
    def ReadContentAsFloat(self) -> FloatType: ...
    
    def ReadContentAsInt(self) -> IntType: ...
    
    def ReadContentAsLong(self) -> LongType: ...
    
    def ReadContentAsObject(self) -> ObjectType: ...
    
    def ReadContentAsObjectAsync(self) -> Task[ObjectType]: ...
    
    def ReadContentAsStringAsync(self) -> Task[StringType]: ...
    
    def ReadElementContentAsAsync(self, returnType: TypeType, namespaceResolver: IXmlNamespaceResolver) -> Task[ObjectType]: ...
    
    def ReadElementContentAsBinHexAsync(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> Task[IntType]: ...
    
    def ReadElementContentAsObjectAsync(self) -> Task[ObjectType]: ...
    
    def ReadElementContentAsStringAsync(self) -> Task[StringType]: ...
    
    def ReadInnerXmlAsync(self) -> Task[StringType]: ...
    
    def ReadOuterXmlAsync(self) -> Task[StringType]: ...
    
    def ReadValueChunkAsync(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> Task[IntType]: ...
    
    def ResolveEntity(self) -> VoidType: ...
    
    def SkipAsync(self) -> Task: ...
    
    def get_AttributeCount(self) -> IntType: ...
    
    def get_BaseURI(self) -> StringType: ...
    
    def get_Depth(self) -> IntType: ...
    
    def get_EOF(self) -> BooleanType: ...
    
    def get_HasValue(self) -> BooleanType: ...
    
    def get_IsEmptyElement(self) -> BooleanType: ...
    
    def get_LocalName(self) -> StringType: ...
    
    def get_NameTable(self) -> XmlNameTable: ...
    
    def get_NamespaceURI(self) -> StringType: ...
    
    def get_NodeType(self) -> XmlNodeType: ...
    
    def get_Prefix(self) -> StringType: ...
    
    def get_ReadState(self) -> ReadState: ...
    
    def get_Settings(self) -> XmlReaderSettings: ...
    
    def get_Value(self) -> StringType: ...
    
    def get_ValueType(self) -> TypeType: ...
    
    def get_XmlLang(self) -> StringType: ...
    
    def get_XmlSpace(self) -> XmlSpace: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSqlBinaryReader(XmlReader, IDisposable, IXmlNamespaceResolver):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, stream: Stream, data: ArrayType[ByteType], len: IntType, baseUri: StringType, closeInput: BooleanType, settings: XmlReaderSettings): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AttributeCount(self) -> IntType: ...
    
    @property
    def BaseURI(self) -> StringType: ...
    
    @property
    def Depth(self) -> IntType: ...
    
    @property
    def EOF(self) -> BooleanType: ...
    
    @property
    def HasValue(self) -> BooleanType: ...
    
    @property
    def IsEmptyElement(self) -> BooleanType: ...
    
    @property
    def LocalName(self) -> StringType: ...
    
    @property
    def NameTable(self) -> XmlNameTable: ...
    
    @property
    def NamespaceURI(self) -> StringType: ...
    
    @property
    def NodeType(self) -> XmlNodeType: ...
    
    @property
    def Prefix(self) -> StringType: ...
    
    @property
    def ReadState(self) -> ReadState: ...
    
    @property
    def Settings(self) -> XmlReaderSettings: ...
    
    @property
    def Value(self) -> StringType: ...
    
    @property
    def ValueType(self) -> TypeType: ...
    
    @property
    def XmlLang(self) -> StringType: ...
    
    @property
    def XmlSpace(self) -> XmlSpace: ...
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    @overload
    def GetAttribute(self, name: StringType, ns: StringType) -> StringType: ...
    
    @overload
    def GetAttribute(self, name: StringType) -> StringType: ...
    
    @overload
    def GetAttribute(self, i: IntType) -> StringType: ...
    
    def GetValueAsync(self) -> Task[StringType]: ...
    
    def LookupNamespace(self, prefix: StringType) -> StringType: ...
    
    @overload
    def MoveToAttribute(self, name: StringType, ns: StringType) -> BooleanType: ...
    
    @overload
    def MoveToAttribute(self, name: StringType) -> BooleanType: ...
    
    @overload
    def MoveToAttribute(self, i: IntType) -> VoidType: ...
    
    def MoveToContentAsync(self) -> Task[XmlNodeType]: ...
    
    def MoveToElement(self) -> BooleanType: ...
    
    def MoveToFirstAttribute(self) -> BooleanType: ...
    
    def MoveToNextAttribute(self) -> BooleanType: ...
    
    def Read(self) -> BooleanType: ...
    
    def ReadAsync(self) -> Task[BooleanType]: ...
    
    def ReadAttributeValue(self) -> BooleanType: ...
    
    def ReadContentAs(self, returnType: TypeType, namespaceResolver: IXmlNamespaceResolver) -> ObjectType: ...
    
    def ReadContentAsAsync(self, returnType: TypeType, namespaceResolver: IXmlNamespaceResolver) -> Task[ObjectType]: ...
    
    def ReadContentAsBase64Async(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> Task[IntType]: ...
    
    def ReadContentAsBoolean(self) -> BooleanType: ...
    
    def ReadContentAsDateTime(self) -> DateTime: ...
    
    def ReadContentAsDecimal(self) -> DecimalType: ...
    
    def ReadContentAsDouble(self) -> DoubleType: ...
    
    def ReadContentAsFloat(self) -> FloatType: ...
    
    def ReadContentAsInt(self) -> IntType: ...
    
    def ReadContentAsLong(self) -> LongType: ...
    
    def ReadContentAsObject(self) -> ObjectType: ...
    
    def ReadContentAsObjectAsync(self) -> Task[ObjectType]: ...
    
    def ReadContentAsStringAsync(self) -> Task[StringType]: ...
    
    def ReadElementContentAsAsync(self, returnType: TypeType, namespaceResolver: IXmlNamespaceResolver) -> Task[ObjectType]: ...
    
    def ReadElementContentAsBinHexAsync(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> Task[IntType]: ...
    
    def ReadElementContentAsObjectAsync(self) -> Task[ObjectType]: ...
    
    def ReadElementContentAsStringAsync(self) -> Task[StringType]: ...
    
    def ReadInnerXmlAsync(self) -> Task[StringType]: ...
    
    def ReadOuterXmlAsync(self) -> Task[StringType]: ...
    
    def ReadValueChunkAsync(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> Task[IntType]: ...
    
    def ResolveEntity(self) -> VoidType: ...
    
    def SkipAsync(self) -> Task: ...
    
    def get_AttributeCount(self) -> IntType: ...
    
    def get_BaseURI(self) -> StringType: ...
    
    def get_Depth(self) -> IntType: ...
    
    def get_EOF(self) -> BooleanType: ...
    
    def get_HasValue(self) -> BooleanType: ...
    
    def get_IsEmptyElement(self) -> BooleanType: ...
    
    def get_LocalName(self) -> StringType: ...
    
    def get_NameTable(self) -> XmlNameTable: ...
    
    def get_NamespaceURI(self) -> StringType: ...
    
    def get_NodeType(self) -> XmlNodeType: ...
    
    def get_Prefix(self) -> StringType: ...
    
    def get_ReadState(self) -> ReadState: ...
    
    def get_Settings(self) -> XmlReaderSettings: ...
    
    def get_Value(self) -> StringType: ...
    
    def get_ValueType(self) -> TypeType: ...
    
    def get_XmlLang(self) -> StringType: ...
    
    def get_XmlSpace(self) -> XmlSpace: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSubtreeReader(XmlWrappingReader, IDisposable, IXmlLineInfo, IXmlNamespaceResolver):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def AttributeCount(self) -> IntType: ...
    
    @property
    def BaseURI(self) -> StringType: ...
    
    @property
    def CanReadBinaryContent(self) -> BooleanType: ...
    
    @property
    def CanReadValueChunk(self) -> BooleanType: ...
    
    @property
    def Depth(self) -> IntType: ...
    
    @property
    def EOF(self) -> BooleanType: ...
    
    @property
    def IsEmptyElement(self) -> BooleanType: ...
    
    @property
    def LocalName(self) -> StringType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def NameTable(self) -> XmlNameTable: ...
    
    @property
    def NamespaceURI(self) -> StringType: ...
    
    @property
    def NodeType(self) -> XmlNodeType: ...
    
    @property
    def Prefix(self) -> StringType: ...
    
    @property
    def ReadState(self) -> ReadState: ...
    
    @property
    def Value(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    @overload
    def GetAttribute(self, name: StringType) -> StringType: ...
    
    @overload
    def GetAttribute(self, name: StringType, namespaceURI: StringType) -> StringType: ...
    
    @overload
    def GetAttribute(self, i: IntType) -> StringType: ...
    
    def GetValueAsync(self) -> Task[StringType]: ...
    
    def LookupNamespace(self, prefix: StringType) -> StringType: ...
    
    @overload
    def MoveToAttribute(self, name: StringType) -> BooleanType: ...
    
    @overload
    def MoveToAttribute(self, name: StringType, ns: StringType) -> BooleanType: ...
    
    @overload
    def MoveToAttribute(self, i: IntType) -> VoidType: ...
    
    def MoveToElement(self) -> BooleanType: ...
    
    def MoveToFirstAttribute(self) -> BooleanType: ...
    
    def MoveToNextAttribute(self) -> BooleanType: ...
    
    def Read(self) -> BooleanType: ...
    
    def ReadAsync(self) -> Task[BooleanType]: ...
    
    def ReadAttributeValue(self) -> BooleanType: ...
    
    def ReadContentAs(self, returnType: TypeType, namespaceResolver: IXmlNamespaceResolver) -> ObjectType: ...
    
    def ReadContentAsAsync(self, returnType: TypeType, namespaceResolver: IXmlNamespaceResolver) -> Task[ObjectType]: ...
    
    def ReadContentAsBase64(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadContentAsBase64Async(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> Task[IntType]: ...
    
    def ReadContentAsBinHex(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadContentAsBinHexAsync(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> Task[IntType]: ...
    
    def ReadContentAsBoolean(self) -> BooleanType: ...
    
    def ReadContentAsDateTime(self) -> DateTime: ...
    
    def ReadContentAsDecimal(self) -> DecimalType: ...
    
    def ReadContentAsDouble(self) -> DoubleType: ...
    
    def ReadContentAsFloat(self) -> FloatType: ...
    
    def ReadContentAsInt(self) -> IntType: ...
    
    def ReadContentAsLong(self) -> LongType: ...
    
    def ReadContentAsObject(self) -> ObjectType: ...
    
    def ReadContentAsObjectAsync(self) -> Task[ObjectType]: ...
    
    def ReadContentAsString(self) -> StringType: ...
    
    def ReadContentAsStringAsync(self) -> Task[StringType]: ...
    
    def ReadElementContentAsBase64(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadElementContentAsBase64Async(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> Task[IntType]: ...
    
    def ReadElementContentAsBinHex(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadElementContentAsBinHexAsync(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> Task[IntType]: ...
    
    def ReadValueChunk(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadValueChunkAsync(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> Task[IntType]: ...
    
    def Skip(self) -> VoidType: ...
    
    def SkipAsync(self) -> Task: ...
    
    def get_AttributeCount(self) -> IntType: ...
    
    def get_BaseURI(self) -> StringType: ...
    
    def get_CanReadBinaryContent(self) -> BooleanType: ...
    
    def get_CanReadValueChunk(self) -> BooleanType: ...
    
    def get_Depth(self) -> IntType: ...
    
    def get_EOF(self) -> BooleanType: ...
    
    def get_IsEmptyElement(self) -> BooleanType: ...
    
    def get_LocalName(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_NameTable(self) -> XmlNameTable: ...
    
    def get_NamespaceURI(self) -> StringType: ...
    
    def get_NodeType(self) -> XmlNodeType: ...
    
    def get_Prefix(self) -> StringType: ...
    
    def get_ReadState(self) -> ReadState: ...
    
    def get_Value(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSubtreeReader(XmlWrappingReader, IDisposable, IXmlLineInfo, IXmlNamespaceResolver):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def AttributeCount(self) -> IntType: ...
    
    @property
    def BaseURI(self) -> StringType: ...
    
    @property
    def CanReadBinaryContent(self) -> BooleanType: ...
    
    @property
    def CanReadValueChunk(self) -> BooleanType: ...
    
    @property
    def Depth(self) -> IntType: ...
    
    @property
    def EOF(self) -> BooleanType: ...
    
    @property
    def IsEmptyElement(self) -> BooleanType: ...
    
    @property
    def LocalName(self) -> StringType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def NameTable(self) -> XmlNameTable: ...
    
    @property
    def NamespaceURI(self) -> StringType: ...
    
    @property
    def NodeType(self) -> XmlNodeType: ...
    
    @property
    def Prefix(self) -> StringType: ...
    
    @property
    def ReadState(self) -> ReadState: ...
    
    @property
    def Value(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    @overload
    def GetAttribute(self, name: StringType) -> StringType: ...
    
    @overload
    def GetAttribute(self, name: StringType, namespaceURI: StringType) -> StringType: ...
    
    @overload
    def GetAttribute(self, i: IntType) -> StringType: ...
    
    def GetValueAsync(self) -> Task[StringType]: ...
    
    def LookupNamespace(self, prefix: StringType) -> StringType: ...
    
    @overload
    def MoveToAttribute(self, name: StringType) -> BooleanType: ...
    
    @overload
    def MoveToAttribute(self, name: StringType, ns: StringType) -> BooleanType: ...
    
    @overload
    def MoveToAttribute(self, i: IntType) -> VoidType: ...
    
    def MoveToElement(self) -> BooleanType: ...
    
    def MoveToFirstAttribute(self) -> BooleanType: ...
    
    def MoveToNextAttribute(self) -> BooleanType: ...
    
    def Read(self) -> BooleanType: ...
    
    def ReadAsync(self) -> Task[BooleanType]: ...
    
    def ReadAttributeValue(self) -> BooleanType: ...
    
    def ReadContentAs(self, returnType: TypeType, namespaceResolver: IXmlNamespaceResolver) -> ObjectType: ...
    
    def ReadContentAsAsync(self, returnType: TypeType, namespaceResolver: IXmlNamespaceResolver) -> Task[ObjectType]: ...
    
    def ReadContentAsBase64(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadContentAsBase64Async(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> Task[IntType]: ...
    
    def ReadContentAsBinHex(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadContentAsBinHexAsync(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> Task[IntType]: ...
    
    def ReadContentAsBoolean(self) -> BooleanType: ...
    
    def ReadContentAsDateTime(self) -> DateTime: ...
    
    def ReadContentAsDecimal(self) -> DecimalType: ...
    
    def ReadContentAsDouble(self) -> DoubleType: ...
    
    def ReadContentAsFloat(self) -> FloatType: ...
    
    def ReadContentAsInt(self) -> IntType: ...
    
    def ReadContentAsLong(self) -> LongType: ...
    
    def ReadContentAsObject(self) -> ObjectType: ...
    
    def ReadContentAsObjectAsync(self) -> Task[ObjectType]: ...
    
    def ReadContentAsString(self) -> StringType: ...
    
    def ReadContentAsStringAsync(self) -> Task[StringType]: ...
    
    def ReadElementContentAsBase64(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadElementContentAsBase64Async(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> Task[IntType]: ...
    
    def ReadElementContentAsBinHex(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadElementContentAsBinHexAsync(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> Task[IntType]: ...
    
    def ReadValueChunk(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadValueChunkAsync(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> Task[IntType]: ...
    
    def Skip(self) -> VoidType: ...
    
    def SkipAsync(self) -> Task: ...
    
    def get_AttributeCount(self) -> IntType: ...
    
    def get_BaseURI(self) -> StringType: ...
    
    def get_CanReadBinaryContent(self) -> BooleanType: ...
    
    def get_CanReadValueChunk(self) -> BooleanType: ...
    
    def get_Depth(self) -> IntType: ...
    
    def get_EOF(self) -> BooleanType: ...
    
    def get_IsEmptyElement(self) -> BooleanType: ...
    
    def get_LocalName(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_NameTable(self) -> XmlNameTable: ...
    
    def get_NamespaceURI(self) -> StringType: ...
    
    def get_NodeType(self) -> XmlNodeType: ...
    
    def get_Prefix(self) -> StringType: ...
    
    def get_ReadState(self) -> ReadState: ...
    
    def get_Value(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlText(XmlCharacterData, ICloneable, IEnumerable, IXPathNavigable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def LocalName(self) -> StringType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def NodeType(self) -> XmlNodeType: ...
    
    @property
    def ParentNode(self) -> XmlNode: ...
    
    @property
    def PreviousText(self) -> XmlNode: ...
    
    @property
    def Value(self) -> StringType: ...
    
    @Value.setter
    def Value(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def CloneNode(self, deep: BooleanType) -> XmlNode: ...
    
    def SplitText(self, offset: IntType) -> XmlText: ...
    
    def WriteContentTo(self, w: XmlWriter) -> VoidType: ...
    
    def WriteTo(self, w: XmlWriter) -> VoidType: ...
    
    def get_LocalName(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_NodeType(self) -> XmlNodeType: ...
    
    def get_ParentNode(self) -> XmlNode: ...
    
    def get_PreviousText(self) -> XmlNode: ...
    
    def get_Value(self) -> StringType: ...
    
    def set_Value(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlText(XmlCharacterData, ICloneable, IEnumerable, IXPathNavigable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def LocalName(self) -> StringType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def NodeType(self) -> XmlNodeType: ...
    
    @property
    def ParentNode(self) -> XmlNode: ...
    
    @property
    def PreviousText(self) -> XmlNode: ...
    
    @property
    def Value(self) -> StringType: ...
    
    @Value.setter
    def Value(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def CloneNode(self, deep: BooleanType) -> XmlNode: ...
    
    def SplitText(self, offset: IntType) -> XmlText: ...
    
    def WriteContentTo(self, w: XmlWriter) -> VoidType: ...
    
    def WriteTo(self, w: XmlWriter) -> VoidType: ...
    
    def get_LocalName(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_NodeType(self) -> XmlNodeType: ...
    
    def get_ParentNode(self) -> XmlNode: ...
    
    def get_PreviousText(self) -> XmlNode: ...
    
    def get_Value(self) -> StringType: ...
    
    def set_Value(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlTextEncoder(ObjectType):
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


class XmlTextEncoder(ObjectType):
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


class XmlTextReader(XmlReader, IDisposable, IXmlLineInfo, IXmlNamespaceResolver):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, input: Stream): ...
    
    @overload
    def __init__(self, url: StringType, input: Stream): ...
    
    @overload
    def __init__(self, input: Stream, nt: XmlNameTable): ...
    
    @overload
    def __init__(self, url: StringType, input: Stream, nt: XmlNameTable): ...
    
    @overload
    def __init__(self, input: TextReader): ...
    
    @overload
    def __init__(self, url: StringType, input: TextReader): ...
    
    @overload
    def __init__(self, input: TextReader, nt: XmlNameTable): ...
    
    @overload
    def __init__(self, url: StringType, input: TextReader, nt: XmlNameTable): ...
    
    @overload
    def __init__(self, xmlFragment: Stream, fragType: XmlNodeType, context: XmlParserContext): ...
    
    @overload
    def __init__(self, xmlFragment: StringType, fragType: XmlNodeType, context: XmlParserContext): ...
    
    @overload
    def __init__(self, url: StringType): ...
    
    @overload
    def __init__(self, url: StringType, nt: XmlNameTable): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AttributeCount(self) -> IntType: ...
    
    @property
    def BaseURI(self) -> StringType: ...
    
    @property
    def CanReadBinaryContent(self) -> BooleanType: ...
    
    @property
    def CanReadValueChunk(self) -> BooleanType: ...
    
    @property
    def CanResolveEntity(self) -> BooleanType: ...
    
    @property
    def Depth(self) -> IntType: ...
    
    @property
    def DtdProcessing(self) -> DtdProcessing: ...
    
    @DtdProcessing.setter
    def DtdProcessing(self, value: DtdProcessing) -> None: ...
    
    @property
    def EOF(self) -> BooleanType: ...
    
    @property
    def Encoding(self) -> Encoding: ...
    
    @property
    def EntityHandling(self) -> EntityHandling: ...
    
    @EntityHandling.setter
    def EntityHandling(self, value: EntityHandling) -> None: ...
    
    @property
    def HasValue(self) -> BooleanType: ...
    
    @property
    def IsDefault(self) -> BooleanType: ...
    
    @property
    def IsEmptyElement(self) -> BooleanType: ...
    
    @property
    def LineNumber(self) -> IntType: ...
    
    @property
    def LinePosition(self) -> IntType: ...
    
    @property
    def LocalName(self) -> StringType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def NameTable(self) -> XmlNameTable: ...
    
    @property
    def NamespaceURI(self) -> StringType: ...
    
    @property
    def Namespaces(self) -> BooleanType: ...
    
    @Namespaces.setter
    def Namespaces(self, value: BooleanType) -> None: ...
    
    @property
    def NodeType(self) -> XmlNodeType: ...
    
    @property
    def Normalization(self) -> BooleanType: ...
    
    @Normalization.setter
    def Normalization(self, value: BooleanType) -> None: ...
    
    @property
    def Prefix(self) -> StringType: ...
    
    @property
    def ProhibitDtd(self) -> BooleanType: ...
    
    @ProhibitDtd.setter
    def ProhibitDtd(self, value: BooleanType) -> None: ...
    
    @property
    def QuoteChar(self) -> CharType: ...
    
    @property
    def ReadState(self) -> ReadState: ...
    
    @property
    def Value(self) -> StringType: ...
    
    @property
    def WhitespaceHandling(self) -> WhitespaceHandling: ...
    
    @WhitespaceHandling.setter
    def WhitespaceHandling(self, value: WhitespaceHandling) -> None: ...
    
    @property
    def XmlLang(self) -> StringType: ...
    
    @XmlResolver.setter
    def XmlResolver(self, value: XmlResolver) -> None: ...
    
    @property
    def XmlSpace(self) -> XmlSpace: ...
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    @overload
    def GetAttribute(self, name: StringType) -> StringType: ...
    
    @overload
    def GetAttribute(self, localName: StringType, namespaceURI: StringType) -> StringType: ...
    
    @overload
    def GetAttribute(self, i: IntType) -> StringType: ...
    
    def GetNamespacesInScope(self, scope: XmlNamespaceScope) -> IDictionary[StringType, StringType]: ...
    
    def GetRemainder(self) -> TextReader: ...
    
    def HasLineInfo(self) -> BooleanType: ...
    
    def LookupNamespace(self, prefix: StringType) -> StringType: ...
    
    @overload
    def MoveToAttribute(self, name: StringType) -> BooleanType: ...
    
    @overload
    def MoveToAttribute(self, localName: StringType, namespaceURI: StringType) -> BooleanType: ...
    
    @overload
    def MoveToAttribute(self, i: IntType) -> VoidType: ...
    
    def MoveToElement(self) -> BooleanType: ...
    
    def MoveToFirstAttribute(self) -> BooleanType: ...
    
    def MoveToNextAttribute(self) -> BooleanType: ...
    
    def Read(self) -> BooleanType: ...
    
    def ReadAttributeValue(self) -> BooleanType: ...
    
    def ReadBase64(self, array: ArrayType[ByteType], offset: IntType, len: IntType) -> IntType: ...
    
    def ReadBinHex(self, array: ArrayType[ByteType], offset: IntType, len: IntType) -> IntType: ...
    
    def ReadChars(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadContentAsBase64(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadContentAsBinHex(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadElementContentAsBase64(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadElementContentAsBinHex(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadString(self) -> StringType: ...
    
    def ResetState(self) -> VoidType: ...
    
    def ResolveEntity(self) -> VoidType: ...
    
    def Skip(self) -> VoidType: ...
    
    def get_AttributeCount(self) -> IntType: ...
    
    def get_BaseURI(self) -> StringType: ...
    
    def get_CanReadBinaryContent(self) -> BooleanType: ...
    
    def get_CanReadValueChunk(self) -> BooleanType: ...
    
    def get_CanResolveEntity(self) -> BooleanType: ...
    
    def get_Depth(self) -> IntType: ...
    
    def get_DtdProcessing(self) -> DtdProcessing: ...
    
    def get_EOF(self) -> BooleanType: ...
    
    def get_Encoding(self) -> Encoding: ...
    
    def get_EntityHandling(self) -> EntityHandling: ...
    
    def get_HasValue(self) -> BooleanType: ...
    
    def get_IsDefault(self) -> BooleanType: ...
    
    def get_IsEmptyElement(self) -> BooleanType: ...
    
    def get_LineNumber(self) -> IntType: ...
    
    def get_LinePosition(self) -> IntType: ...
    
    def get_LocalName(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_NameTable(self) -> XmlNameTable: ...
    
    def get_NamespaceURI(self) -> StringType: ...
    
    def get_Namespaces(self) -> BooleanType: ...
    
    def get_NodeType(self) -> XmlNodeType: ...
    
    def get_Normalization(self) -> BooleanType: ...
    
    def get_Prefix(self) -> StringType: ...
    
    def get_ProhibitDtd(self) -> BooleanType: ...
    
    def get_QuoteChar(self) -> CharType: ...
    
    def get_ReadState(self) -> ReadState: ...
    
    def get_Value(self) -> StringType: ...
    
    def get_WhitespaceHandling(self) -> WhitespaceHandling: ...
    
    def get_XmlLang(self) -> StringType: ...
    
    def get_XmlSpace(self) -> XmlSpace: ...
    
    def set_DtdProcessing(self, value: DtdProcessing) -> VoidType: ...
    
    def set_EntityHandling(self, value: EntityHandling) -> VoidType: ...
    
    def set_Namespaces(self, value: BooleanType) -> VoidType: ...
    
    def set_Normalization(self, value: BooleanType) -> VoidType: ...
    
    def set_ProhibitDtd(self, value: BooleanType) -> VoidType: ...
    
    def set_WhitespaceHandling(self, value: WhitespaceHandling) -> VoidType: ...
    
    def set_XmlResolver(self, value: XmlResolver) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlTextReader(XmlReader, IDisposable, IXmlLineInfo, IXmlNamespaceResolver):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, input: Stream): ...
    
    @overload
    def __init__(self, url: StringType, input: Stream): ...
    
    @overload
    def __init__(self, input: Stream, nt: XmlNameTable): ...
    
    @overload
    def __init__(self, url: StringType, input: Stream, nt: XmlNameTable): ...
    
    @overload
    def __init__(self, input: TextReader): ...
    
    @overload
    def __init__(self, url: StringType, input: TextReader): ...
    
    @overload
    def __init__(self, input: TextReader, nt: XmlNameTable): ...
    
    @overload
    def __init__(self, url: StringType, input: TextReader, nt: XmlNameTable): ...
    
    @overload
    def __init__(self, xmlFragment: Stream, fragType: XmlNodeType, context: XmlParserContext): ...
    
    @overload
    def __init__(self, xmlFragment: StringType, fragType: XmlNodeType, context: XmlParserContext): ...
    
    @overload
    def __init__(self, url: StringType): ...
    
    @overload
    def __init__(self, url: StringType, nt: XmlNameTable): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AttributeCount(self) -> IntType: ...
    
    @property
    def BaseURI(self) -> StringType: ...
    
    @property
    def CanReadBinaryContent(self) -> BooleanType: ...
    
    @property
    def CanReadValueChunk(self) -> BooleanType: ...
    
    @property
    def CanResolveEntity(self) -> BooleanType: ...
    
    @property
    def Depth(self) -> IntType: ...
    
    @property
    def DtdProcessing(self) -> DtdProcessing: ...
    
    @DtdProcessing.setter
    def DtdProcessing(self, value: DtdProcessing) -> None: ...
    
    @property
    def EOF(self) -> BooleanType: ...
    
    @property
    def Encoding(self) -> Encoding: ...
    
    @property
    def EntityHandling(self) -> EntityHandling: ...
    
    @EntityHandling.setter
    def EntityHandling(self, value: EntityHandling) -> None: ...
    
    @property
    def HasValue(self) -> BooleanType: ...
    
    @property
    def IsDefault(self) -> BooleanType: ...
    
    @property
    def IsEmptyElement(self) -> BooleanType: ...
    
    @property
    def LineNumber(self) -> IntType: ...
    
    @property
    def LinePosition(self) -> IntType: ...
    
    @property
    def LocalName(self) -> StringType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def NameTable(self) -> XmlNameTable: ...
    
    @property
    def NamespaceURI(self) -> StringType: ...
    
    @property
    def Namespaces(self) -> BooleanType: ...
    
    @Namespaces.setter
    def Namespaces(self, value: BooleanType) -> None: ...
    
    @property
    def NodeType(self) -> XmlNodeType: ...
    
    @property
    def Normalization(self) -> BooleanType: ...
    
    @Normalization.setter
    def Normalization(self, value: BooleanType) -> None: ...
    
    @property
    def Prefix(self) -> StringType: ...
    
    @property
    def ProhibitDtd(self) -> BooleanType: ...
    
    @ProhibitDtd.setter
    def ProhibitDtd(self, value: BooleanType) -> None: ...
    
    @property
    def QuoteChar(self) -> CharType: ...
    
    @property
    def ReadState(self) -> ReadState: ...
    
    @property
    def Value(self) -> StringType: ...
    
    @property
    def WhitespaceHandling(self) -> WhitespaceHandling: ...
    
    @WhitespaceHandling.setter
    def WhitespaceHandling(self, value: WhitespaceHandling) -> None: ...
    
    @property
    def XmlLang(self) -> StringType: ...
    
    @XmlResolver.setter
    def XmlResolver(self, value: XmlResolver) -> None: ...
    
    @property
    def XmlSpace(self) -> XmlSpace: ...
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    @overload
    def GetAttribute(self, name: StringType) -> StringType: ...
    
    @overload
    def GetAttribute(self, localName: StringType, namespaceURI: StringType) -> StringType: ...
    
    @overload
    def GetAttribute(self, i: IntType) -> StringType: ...
    
    def GetNamespacesInScope(self, scope: XmlNamespaceScope) -> IDictionary[StringType, StringType]: ...
    
    def GetRemainder(self) -> TextReader: ...
    
    def HasLineInfo(self) -> BooleanType: ...
    
    def LookupNamespace(self, prefix: StringType) -> StringType: ...
    
    @overload
    def MoveToAttribute(self, name: StringType) -> BooleanType: ...
    
    @overload
    def MoveToAttribute(self, localName: StringType, namespaceURI: StringType) -> BooleanType: ...
    
    @overload
    def MoveToAttribute(self, i: IntType) -> VoidType: ...
    
    def MoveToElement(self) -> BooleanType: ...
    
    def MoveToFirstAttribute(self) -> BooleanType: ...
    
    def MoveToNextAttribute(self) -> BooleanType: ...
    
    def Read(self) -> BooleanType: ...
    
    def ReadAttributeValue(self) -> BooleanType: ...
    
    def ReadBase64(self, array: ArrayType[ByteType], offset: IntType, len: IntType) -> IntType: ...
    
    def ReadBinHex(self, array: ArrayType[ByteType], offset: IntType, len: IntType) -> IntType: ...
    
    def ReadChars(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadContentAsBase64(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadContentAsBinHex(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadElementContentAsBase64(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadElementContentAsBinHex(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadString(self) -> StringType: ...
    
    def ResetState(self) -> VoidType: ...
    
    def ResolveEntity(self) -> VoidType: ...
    
    def Skip(self) -> VoidType: ...
    
    def get_AttributeCount(self) -> IntType: ...
    
    def get_BaseURI(self) -> StringType: ...
    
    def get_CanReadBinaryContent(self) -> BooleanType: ...
    
    def get_CanReadValueChunk(self) -> BooleanType: ...
    
    def get_CanResolveEntity(self) -> BooleanType: ...
    
    def get_Depth(self) -> IntType: ...
    
    def get_DtdProcessing(self) -> DtdProcessing: ...
    
    def get_EOF(self) -> BooleanType: ...
    
    def get_Encoding(self) -> Encoding: ...
    
    def get_EntityHandling(self) -> EntityHandling: ...
    
    def get_HasValue(self) -> BooleanType: ...
    
    def get_IsDefault(self) -> BooleanType: ...
    
    def get_IsEmptyElement(self) -> BooleanType: ...
    
    def get_LineNumber(self) -> IntType: ...
    
    def get_LinePosition(self) -> IntType: ...
    
    def get_LocalName(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_NameTable(self) -> XmlNameTable: ...
    
    def get_NamespaceURI(self) -> StringType: ...
    
    def get_Namespaces(self) -> BooleanType: ...
    
    def get_NodeType(self) -> XmlNodeType: ...
    
    def get_Normalization(self) -> BooleanType: ...
    
    def get_Prefix(self) -> StringType: ...
    
    def get_ProhibitDtd(self) -> BooleanType: ...
    
    def get_QuoteChar(self) -> CharType: ...
    
    def get_ReadState(self) -> ReadState: ...
    
    def get_Value(self) -> StringType: ...
    
    def get_WhitespaceHandling(self) -> WhitespaceHandling: ...
    
    def get_XmlLang(self) -> StringType: ...
    
    def get_XmlSpace(self) -> XmlSpace: ...
    
    def set_DtdProcessing(self, value: DtdProcessing) -> VoidType: ...
    
    def set_EntityHandling(self, value: EntityHandling) -> VoidType: ...
    
    def set_Namespaces(self, value: BooleanType) -> VoidType: ...
    
    def set_Normalization(self, value: BooleanType) -> VoidType: ...
    
    def set_ProhibitDtd(self, value: BooleanType) -> VoidType: ...
    
    def set_WhitespaceHandling(self, value: WhitespaceHandling) -> VoidType: ...
    
    def set_XmlResolver(self, value: XmlResolver) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlTextReaderImpl(XmlReader, IDisposable, IXmlLineInfo, IXmlNamespaceResolver):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, url: StringType): ...
    
    @overload
    def __init__(self, url: StringType, nt: XmlNameTable): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AttributeCount(self) -> IntType: ...
    
    @property
    def BaseURI(self) -> StringType: ...
    
    @property
    def CanReadBinaryContent(self) -> BooleanType: ...
    
    @property
    def CanReadValueChunk(self) -> BooleanType: ...
    
    @property
    def CanResolveEntity(self) -> BooleanType: ...
    
    @property
    def Depth(self) -> IntType: ...
    
    @property
    def EOF(self) -> BooleanType: ...
    
    @property
    def IsDefault(self) -> BooleanType: ...
    
    @property
    def IsEmptyElement(self) -> BooleanType: ...
    
    @property
    def LineNumber(self) -> IntType: ...
    
    @property
    def LinePosition(self) -> IntType: ...
    
    @property
    def LocalName(self) -> StringType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def NameTable(self) -> XmlNameTable: ...
    
    @property
    def NamespaceURI(self) -> StringType: ...
    
    @property
    def NodeType(self) -> XmlNodeType: ...
    
    @property
    def Prefix(self) -> StringType: ...
    
    @property
    def QuoteChar(self) -> CharType: ...
    
    @property
    def ReadState(self) -> ReadState: ...
    
    @property
    def Settings(self) -> XmlReaderSettings: ...
    
    @property
    def Value(self) -> StringType: ...
    
    @property
    def XmlLang(self) -> StringType: ...
    
    @property
    def XmlSpace(self) -> XmlSpace: ...
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    @overload
    def GetAttribute(self, name: StringType) -> StringType: ...
    
    @overload
    def GetAttribute(self, localName: StringType, namespaceURI: StringType) -> StringType: ...
    
    @overload
    def GetAttribute(self, i: IntType) -> StringType: ...
    
    def GetValueAsync(self) -> Task[StringType]: ...
    
    def HasLineInfo(self) -> BooleanType: ...
    
    def LookupNamespace(self, prefix: StringType) -> StringType: ...
    
    @overload
    def MoveToAttribute(self, name: StringType) -> BooleanType: ...
    
    @overload
    def MoveToAttribute(self, localName: StringType, namespaceURI: StringType) -> BooleanType: ...
    
    @overload
    def MoveToAttribute(self, i: IntType) -> VoidType: ...
    
    def MoveToElement(self) -> BooleanType: ...
    
    def MoveToFirstAttribute(self) -> BooleanType: ...
    
    def MoveToNextAttribute(self) -> BooleanType: ...
    
    def Read(self) -> BooleanType: ...
    
    def ReadAsync(self) -> Task[BooleanType]: ...
    
    def ReadAttributeValue(self) -> BooleanType: ...
    
    def ReadContentAsBase64(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadContentAsBase64Async(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> Task[IntType]: ...
    
    def ReadContentAsBinHex(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadContentAsBinHexAsync(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> Task[IntType]: ...
    
    def ReadElementContentAsBase64(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadElementContentAsBase64Async(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> Task[IntType]: ...
    
    def ReadElementContentAsBinHex(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadElementContentAsBinHexAsync(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> Task[IntType]: ...
    
    def ReadString(self) -> StringType: ...
    
    def ReadValueChunk(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadValueChunkAsync(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> Task[IntType]: ...
    
    def ResolveEntity(self) -> VoidType: ...
    
    def Skip(self) -> VoidType: ...
    
    def SkipAsync(self) -> Task: ...
    
    def get_AttributeCount(self) -> IntType: ...
    
    def get_BaseURI(self) -> StringType: ...
    
    def get_CanReadBinaryContent(self) -> BooleanType: ...
    
    def get_CanReadValueChunk(self) -> BooleanType: ...
    
    def get_CanResolveEntity(self) -> BooleanType: ...
    
    def get_Depth(self) -> IntType: ...
    
    def get_EOF(self) -> BooleanType: ...
    
    def get_IsDefault(self) -> BooleanType: ...
    
    def get_IsEmptyElement(self) -> BooleanType: ...
    
    def get_LineNumber(self) -> IntType: ...
    
    def get_LinePosition(self) -> IntType: ...
    
    def get_LocalName(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_NameTable(self) -> XmlNameTable: ...
    
    def get_NamespaceURI(self) -> StringType: ...
    
    def get_NodeType(self) -> XmlNodeType: ...
    
    def get_Prefix(self) -> StringType: ...
    
    def get_QuoteChar(self) -> CharType: ...
    
    def get_ReadState(self) -> ReadState: ...
    
    def get_Settings(self) -> XmlReaderSettings: ...
    
    def get_Value(self) -> StringType: ...
    
    def get_XmlLang(self) -> StringType: ...
    
    def get_XmlSpace(self) -> XmlSpace: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlTextReaderImpl(XmlReader, IDisposable, IXmlLineInfo, IXmlNamespaceResolver):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, url: StringType): ...
    
    @overload
    def __init__(self, url: StringType, nt: XmlNameTable): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AttributeCount(self) -> IntType: ...
    
    @property
    def BaseURI(self) -> StringType: ...
    
    @property
    def CanReadBinaryContent(self) -> BooleanType: ...
    
    @property
    def CanReadValueChunk(self) -> BooleanType: ...
    
    @property
    def CanResolveEntity(self) -> BooleanType: ...
    
    @property
    def Depth(self) -> IntType: ...
    
    @property
    def EOF(self) -> BooleanType: ...
    
    @property
    def IsDefault(self) -> BooleanType: ...
    
    @property
    def IsEmptyElement(self) -> BooleanType: ...
    
    @property
    def LineNumber(self) -> IntType: ...
    
    @property
    def LinePosition(self) -> IntType: ...
    
    @property
    def LocalName(self) -> StringType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def NameTable(self) -> XmlNameTable: ...
    
    @property
    def NamespaceURI(self) -> StringType: ...
    
    @property
    def NodeType(self) -> XmlNodeType: ...
    
    @property
    def Prefix(self) -> StringType: ...
    
    @property
    def QuoteChar(self) -> CharType: ...
    
    @property
    def ReadState(self) -> ReadState: ...
    
    @property
    def Settings(self) -> XmlReaderSettings: ...
    
    @property
    def Value(self) -> StringType: ...
    
    @property
    def XmlLang(self) -> StringType: ...
    
    @property
    def XmlSpace(self) -> XmlSpace: ...
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    @overload
    def GetAttribute(self, name: StringType) -> StringType: ...
    
    @overload
    def GetAttribute(self, localName: StringType, namespaceURI: StringType) -> StringType: ...
    
    @overload
    def GetAttribute(self, i: IntType) -> StringType: ...
    
    def GetValueAsync(self) -> Task[StringType]: ...
    
    def HasLineInfo(self) -> BooleanType: ...
    
    def LookupNamespace(self, prefix: StringType) -> StringType: ...
    
    @overload
    def MoveToAttribute(self, name: StringType) -> BooleanType: ...
    
    @overload
    def MoveToAttribute(self, localName: StringType, namespaceURI: StringType) -> BooleanType: ...
    
    @overload
    def MoveToAttribute(self, i: IntType) -> VoidType: ...
    
    def MoveToElement(self) -> BooleanType: ...
    
    def MoveToFirstAttribute(self) -> BooleanType: ...
    
    def MoveToNextAttribute(self) -> BooleanType: ...
    
    def Read(self) -> BooleanType: ...
    
    def ReadAsync(self) -> Task[BooleanType]: ...
    
    def ReadAttributeValue(self) -> BooleanType: ...
    
    def ReadContentAsBase64(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadContentAsBase64Async(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> Task[IntType]: ...
    
    def ReadContentAsBinHex(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadContentAsBinHexAsync(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> Task[IntType]: ...
    
    def ReadElementContentAsBase64(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadElementContentAsBase64Async(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> Task[IntType]: ...
    
    def ReadElementContentAsBinHex(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadElementContentAsBinHexAsync(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> Task[IntType]: ...
    
    def ReadString(self) -> StringType: ...
    
    def ReadValueChunk(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadValueChunkAsync(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> Task[IntType]: ...
    
    def ResolveEntity(self) -> VoidType: ...
    
    def Skip(self) -> VoidType: ...
    
    def SkipAsync(self) -> Task: ...
    
    def get_AttributeCount(self) -> IntType: ...
    
    def get_BaseURI(self) -> StringType: ...
    
    def get_CanReadBinaryContent(self) -> BooleanType: ...
    
    def get_CanReadValueChunk(self) -> BooleanType: ...
    
    def get_CanResolveEntity(self) -> BooleanType: ...
    
    def get_Depth(self) -> IntType: ...
    
    def get_EOF(self) -> BooleanType: ...
    
    def get_IsDefault(self) -> BooleanType: ...
    
    def get_IsEmptyElement(self) -> BooleanType: ...
    
    def get_LineNumber(self) -> IntType: ...
    
    def get_LinePosition(self) -> IntType: ...
    
    def get_LocalName(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_NameTable(self) -> XmlNameTable: ...
    
    def get_NamespaceURI(self) -> StringType: ...
    
    def get_NodeType(self) -> XmlNodeType: ...
    
    def get_Prefix(self) -> StringType: ...
    
    def get_QuoteChar(self) -> CharType: ...
    
    def get_ReadState(self) -> ReadState: ...
    
    def get_Settings(self) -> XmlReaderSettings: ...
    
    def get_Value(self) -> StringType: ...
    
    def get_XmlLang(self) -> StringType: ...
    
    def get_XmlSpace(self) -> XmlSpace: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlTextWriter(XmlWriter, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, w: Stream, encoding: Encoding): ...
    
    @overload
    def __init__(self, filename: StringType, encoding: Encoding): ...
    
    @overload
    def __init__(self, w: TextWriter): ...
    
    # ---------- Properties ---------- #
    
    @property
    def BaseStream(self) -> Stream: ...
    
    @property
    def Formatting(self) -> Formatting: ...
    
    @Formatting.setter
    def Formatting(self, value: Formatting) -> None: ...
    
    @property
    def IndentChar(self) -> CharType: ...
    
    @IndentChar.setter
    def IndentChar(self, value: CharType) -> None: ...
    
    @property
    def Indentation(self) -> IntType: ...
    
    @Indentation.setter
    def Indentation(self, value: IntType) -> None: ...
    
    @property
    def Namespaces(self) -> BooleanType: ...
    
    @Namespaces.setter
    def Namespaces(self, value: BooleanType) -> None: ...
    
    @property
    def QuoteChar(self) -> CharType: ...
    
    @QuoteChar.setter
    def QuoteChar(self, value: CharType) -> None: ...
    
    @property
    def WriteState(self) -> WriteState: ...
    
    @property
    def XmlLang(self) -> StringType: ...
    
    @property
    def XmlSpace(self) -> XmlSpace: ...
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    def Flush(self) -> VoidType: ...
    
    def LookupPrefix(self, ns: StringType) -> StringType: ...
    
    def WriteBase64(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> VoidType: ...
    
    def WriteBinHex(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> VoidType: ...
    
    def WriteCData(self, text: StringType) -> VoidType: ...
    
    def WriteCharEntity(self, ch: CharType) -> VoidType: ...
    
    def WriteChars(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> VoidType: ...
    
    def WriteComment(self, text: StringType) -> VoidType: ...
    
    def WriteDocType(self, name: StringType, pubid: StringType, sysid: StringType, subset: StringType) -> VoidType: ...
    
    def WriteEndAttribute(self) -> VoidType: ...
    
    def WriteEndDocument(self) -> VoidType: ...
    
    def WriteEndElement(self) -> VoidType: ...
    
    def WriteEntityRef(self, name: StringType) -> VoidType: ...
    
    def WriteFullEndElement(self) -> VoidType: ...
    
    def WriteName(self, name: StringType) -> VoidType: ...
    
    def WriteNmToken(self, name: StringType) -> VoidType: ...
    
    def WriteProcessingInstruction(self, name: StringType, text: StringType) -> VoidType: ...
    
    def WriteQualifiedName(self, localName: StringType, ns: StringType) -> VoidType: ...
    
    @overload
    def WriteRaw(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> VoidType: ...
    
    @overload
    def WriteRaw(self, data: StringType) -> VoidType: ...
    
    @overload
    def WriteStartAttribute(self, prefix: StringType, localName: StringType, ns: StringType) -> VoidType: ...
    
    @overload
    def WriteStartDocument(self) -> VoidType: ...
    
    @overload
    def WriteStartDocument(self, standalone: BooleanType) -> VoidType: ...
    
    @overload
    def WriteStartElement(self, prefix: StringType, localName: StringType, ns: StringType) -> VoidType: ...
    
    def WriteString(self, text: StringType) -> VoidType: ...
    
    def WriteSurrogateCharEntity(self, lowChar: CharType, highChar: CharType) -> VoidType: ...
    
    def WriteWhitespace(self, ws: StringType) -> VoidType: ...
    
    def get_BaseStream(self) -> Stream: ...
    
    def get_Formatting(self) -> Formatting: ...
    
    def get_IndentChar(self) -> CharType: ...
    
    def get_Indentation(self) -> IntType: ...
    
    def get_Namespaces(self) -> BooleanType: ...
    
    def get_QuoteChar(self) -> CharType: ...
    
    def get_WriteState(self) -> WriteState: ...
    
    def get_XmlLang(self) -> StringType: ...
    
    def get_XmlSpace(self) -> XmlSpace: ...
    
    def set_Formatting(self, value: Formatting) -> VoidType: ...
    
    def set_IndentChar(self, value: CharType) -> VoidType: ...
    
    def set_Indentation(self, value: IntType) -> VoidType: ...
    
    def set_Namespaces(self, value: BooleanType) -> VoidType: ...
    
    def set_QuoteChar(self, value: CharType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlTextWriter(XmlWriter, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, w: Stream, encoding: Encoding): ...
    
    @overload
    def __init__(self, filename: StringType, encoding: Encoding): ...
    
    @overload
    def __init__(self, w: TextWriter): ...
    
    # ---------- Properties ---------- #
    
    @property
    def BaseStream(self) -> Stream: ...
    
    @property
    def Formatting(self) -> Formatting: ...
    
    @Formatting.setter
    def Formatting(self, value: Formatting) -> None: ...
    
    @property
    def IndentChar(self) -> CharType: ...
    
    @IndentChar.setter
    def IndentChar(self, value: CharType) -> None: ...
    
    @property
    def Indentation(self) -> IntType: ...
    
    @Indentation.setter
    def Indentation(self, value: IntType) -> None: ...
    
    @property
    def Namespaces(self) -> BooleanType: ...
    
    @Namespaces.setter
    def Namespaces(self, value: BooleanType) -> None: ...
    
    @property
    def QuoteChar(self) -> CharType: ...
    
    @QuoteChar.setter
    def QuoteChar(self, value: CharType) -> None: ...
    
    @property
    def WriteState(self) -> WriteState: ...
    
    @property
    def XmlLang(self) -> StringType: ...
    
    @property
    def XmlSpace(self) -> XmlSpace: ...
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    def Flush(self) -> VoidType: ...
    
    def LookupPrefix(self, ns: StringType) -> StringType: ...
    
    def WriteBase64(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> VoidType: ...
    
    def WriteBinHex(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> VoidType: ...
    
    def WriteCData(self, text: StringType) -> VoidType: ...
    
    def WriteCharEntity(self, ch: CharType) -> VoidType: ...
    
    def WriteChars(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> VoidType: ...
    
    def WriteComment(self, text: StringType) -> VoidType: ...
    
    def WriteDocType(self, name: StringType, pubid: StringType, sysid: StringType, subset: StringType) -> VoidType: ...
    
    def WriteEndAttribute(self) -> VoidType: ...
    
    def WriteEndDocument(self) -> VoidType: ...
    
    def WriteEndElement(self) -> VoidType: ...
    
    def WriteEntityRef(self, name: StringType) -> VoidType: ...
    
    def WriteFullEndElement(self) -> VoidType: ...
    
    def WriteName(self, name: StringType) -> VoidType: ...
    
    def WriteNmToken(self, name: StringType) -> VoidType: ...
    
    def WriteProcessingInstruction(self, name: StringType, text: StringType) -> VoidType: ...
    
    def WriteQualifiedName(self, localName: StringType, ns: StringType) -> VoidType: ...
    
    @overload
    def WriteRaw(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> VoidType: ...
    
    @overload
    def WriteRaw(self, data: StringType) -> VoidType: ...
    
    @overload
    def WriteStartAttribute(self, prefix: StringType, localName: StringType, ns: StringType) -> VoidType: ...
    
    @overload
    def WriteStartDocument(self) -> VoidType: ...
    
    @overload
    def WriteStartDocument(self, standalone: BooleanType) -> VoidType: ...
    
    @overload
    def WriteStartElement(self, prefix: StringType, localName: StringType, ns: StringType) -> VoidType: ...
    
    def WriteString(self, text: StringType) -> VoidType: ...
    
    def WriteSurrogateCharEntity(self, lowChar: CharType, highChar: CharType) -> VoidType: ...
    
    def WriteWhitespace(self, ws: StringType) -> VoidType: ...
    
    def get_BaseStream(self) -> Stream: ...
    
    def get_Formatting(self) -> Formatting: ...
    
    def get_IndentChar(self) -> CharType: ...
    
    def get_Indentation(self) -> IntType: ...
    
    def get_Namespaces(self) -> BooleanType: ...
    
    def get_QuoteChar(self) -> CharType: ...
    
    def get_WriteState(self) -> WriteState: ...
    
    def get_XmlLang(self) -> StringType: ...
    
    def get_XmlSpace(self) -> XmlSpace: ...
    
    def set_Formatting(self, value: Formatting) -> VoidType: ...
    
    def set_IndentChar(self, value: CharType) -> VoidType: ...
    
    def set_Indentation(self, value: IntType) -> VoidType: ...
    
    def set_Namespaces(self, value: BooleanType) -> VoidType: ...
    
    def set_QuoteChar(self, value: CharType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlTextWriterBase64Encoder(Base64Encoder):
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


class XmlTextWriterBase64Encoder(Base64Encoder):
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


class XmlUnspecifiedAttribute(XmlAttribute, ICloneable, IEnumerable, IXPathNavigable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @InnerText.setter
    def InnerText(self, value: StringType) -> None: ...
    
    @property
    def Specified(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def AppendChild(self, newChild: XmlNode) -> XmlNode: ...
    
    def CloneNode(self, deep: BooleanType) -> XmlNode: ...
    
    def InsertAfter(self, newChild: XmlNode, refChild: XmlNode) -> XmlNode: ...
    
    def InsertBefore(self, newChild: XmlNode, refChild: XmlNode) -> XmlNode: ...
    
    def RemoveChild(self, oldChild: XmlNode) -> XmlNode: ...
    
    def ReplaceChild(self, newChild: XmlNode, oldChild: XmlNode) -> XmlNode: ...
    
    def WriteTo(self, w: XmlWriter) -> VoidType: ...
    
    def get_Specified(self) -> BooleanType: ...
    
    def set_InnerText(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlUnspecifiedAttribute(XmlAttribute, ICloneable, IEnumerable, IXPathNavigable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @InnerText.setter
    def InnerText(self, value: StringType) -> None: ...
    
    @property
    def Specified(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def AppendChild(self, newChild: XmlNode) -> XmlNode: ...
    
    def CloneNode(self, deep: BooleanType) -> XmlNode: ...
    
    def InsertAfter(self, newChild: XmlNode, refChild: XmlNode) -> XmlNode: ...
    
    def InsertBefore(self, newChild: XmlNode, refChild: XmlNode) -> XmlNode: ...
    
    def RemoveChild(self, oldChild: XmlNode) -> XmlNode: ...
    
    def ReplaceChild(self, newChild: XmlNode, oldChild: XmlNode) -> XmlNode: ...
    
    def WriteTo(self, w: XmlWriter) -> VoidType: ...
    
    def get_Specified(self) -> BooleanType: ...
    
    def set_InnerText(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlUrlResolver(XmlResolver):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @CachePolicy.setter
    def CachePolicy(self, value: RequestCachePolicy) -> None: ...
    
    @Credentials.setter
    def Credentials(self, value: ICredentials) -> None: ...
    
    @Proxy.setter
    def Proxy(self, value: IWebProxy) -> None: ...
    
    # ---------- Methods ---------- #
    
    def GetEntity(self, absoluteUri: Uri, role: StringType, ofObjectToReturn: TypeType) -> ObjectType: ...
    
    def GetEntityAsync(self, absoluteUri: Uri, role: StringType, ofObjectToReturn: TypeType) -> Task[ObjectType]: ...
    
    def ResolveUri(self, baseUri: Uri, relativeUri: StringType) -> Uri: ...
    
    def set_CachePolicy(self, value: RequestCachePolicy) -> VoidType: ...
    
    def set_Credentials(self, value: ICredentials) -> VoidType: ...
    
    def set_Proxy(self, value: IWebProxy) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlUrlResolver(XmlResolver):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @CachePolicy.setter
    def CachePolicy(self, value: RequestCachePolicy) -> None: ...
    
    @Credentials.setter
    def Credentials(self, value: ICredentials) -> None: ...
    
    @Proxy.setter
    def Proxy(self, value: IWebProxy) -> None: ...
    
    # ---------- Methods ---------- #
    
    def GetEntity(self, absoluteUri: Uri, role: StringType, ofObjectToReturn: TypeType) -> ObjectType: ...
    
    def GetEntityAsync(self, absoluteUri: Uri, role: StringType, ofObjectToReturn: TypeType) -> Task[ObjectType]: ...
    
    def ResolveUri(self, baseUri: Uri, relativeUri: StringType) -> Uri: ...
    
    def set_CachePolicy(self, value: RequestCachePolicy) -> VoidType: ...
    
    def set_Credentials(self, value: ICredentials) -> VoidType: ...
    
    def set_Proxy(self, value: IWebProxy) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlUtf8RawTextWriter(XmlRawWriter, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, stream: Stream, settings: XmlWriterSettings): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Settings(self) -> XmlWriterSettings: ...
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    def Flush(self) -> VoidType: ...
    
    def FlushAsync(self) -> Task: ...
    
    def WriteCData(self, text: StringType) -> VoidType: ...
    
    def WriteCDataAsync(self, text: StringType) -> Task: ...
    
    def WriteCharEntity(self, ch: CharType) -> VoidType: ...
    
    def WriteCharEntityAsync(self, ch: CharType) -> Task: ...
    
    def WriteChars(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> VoidType: ...
    
    def WriteCharsAsync(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> Task: ...
    
    def WriteComment(self, text: StringType) -> VoidType: ...
    
    def WriteCommentAsync(self, text: StringType) -> Task: ...
    
    def WriteDocType(self, name: StringType, pubid: StringType, sysid: StringType, subset: StringType) -> VoidType: ...
    
    def WriteDocTypeAsync(self, name: StringType, pubid: StringType, sysid: StringType, subset: StringType) -> Task: ...
    
    def WriteEndAttribute(self) -> VoidType: ...
    
    def WriteEntityRef(self, name: StringType) -> VoidType: ...
    
    def WriteEntityRefAsync(self, name: StringType) -> Task: ...
    
    def WriteProcessingInstruction(self, name: StringType, text: StringType) -> VoidType: ...
    
    def WriteProcessingInstructionAsync(self, name: StringType, text: StringType) -> Task: ...
    
    @overload
    def WriteRaw(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> VoidType: ...
    
    @overload
    def WriteRaw(self, data: StringType) -> VoidType: ...
    
    @overload
    def WriteRawAsync(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> Task: ...
    
    @overload
    def WriteRawAsync(self, data: StringType) -> Task: ...
    
    @overload
    def WriteStartAttribute(self, prefix: StringType, localName: StringType, ns: StringType) -> VoidType: ...
    
    @overload
    def WriteStartElement(self, prefix: StringType, localName: StringType, ns: StringType) -> VoidType: ...
    
    def WriteStartElementAsync(self, prefix: StringType, localName: StringType, ns: StringType) -> Task: ...
    
    def WriteString(self, text: StringType) -> VoidType: ...
    
    def WriteStringAsync(self, text: StringType) -> Task: ...
    
    def WriteSurrogateCharEntity(self, lowChar: CharType, highChar: CharType) -> VoidType: ...
    
    def WriteSurrogateCharEntityAsync(self, lowChar: CharType, highChar: CharType) -> Task: ...
    
    def WriteWhitespace(self, ws: StringType) -> VoidType: ...
    
    def WriteWhitespaceAsync(self, ws: StringType) -> Task: ...
    
    def get_Settings(self) -> XmlWriterSettings: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlUtf8RawTextWriter(XmlRawWriter, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, stream: Stream, settings: XmlWriterSettings): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Settings(self) -> XmlWriterSettings: ...
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    def Flush(self) -> VoidType: ...
    
    def FlushAsync(self) -> Task: ...
    
    def WriteCData(self, text: StringType) -> VoidType: ...
    
    def WriteCDataAsync(self, text: StringType) -> Task: ...
    
    def WriteCharEntity(self, ch: CharType) -> VoidType: ...
    
    def WriteCharEntityAsync(self, ch: CharType) -> Task: ...
    
    def WriteChars(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> VoidType: ...
    
    def WriteCharsAsync(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> Task: ...
    
    def WriteComment(self, text: StringType) -> VoidType: ...
    
    def WriteCommentAsync(self, text: StringType) -> Task: ...
    
    def WriteDocType(self, name: StringType, pubid: StringType, sysid: StringType, subset: StringType) -> VoidType: ...
    
    def WriteDocTypeAsync(self, name: StringType, pubid: StringType, sysid: StringType, subset: StringType) -> Task: ...
    
    def WriteEndAttribute(self) -> VoidType: ...
    
    def WriteEntityRef(self, name: StringType) -> VoidType: ...
    
    def WriteEntityRefAsync(self, name: StringType) -> Task: ...
    
    def WriteProcessingInstruction(self, name: StringType, text: StringType) -> VoidType: ...
    
    def WriteProcessingInstructionAsync(self, name: StringType, text: StringType) -> Task: ...
    
    @overload
    def WriteRaw(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> VoidType: ...
    
    @overload
    def WriteRaw(self, data: StringType) -> VoidType: ...
    
    @overload
    def WriteRawAsync(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> Task: ...
    
    @overload
    def WriteRawAsync(self, data: StringType) -> Task: ...
    
    @overload
    def WriteStartAttribute(self, prefix: StringType, localName: StringType, ns: StringType) -> VoidType: ...
    
    @overload
    def WriteStartElement(self, prefix: StringType, localName: StringType, ns: StringType) -> VoidType: ...
    
    def WriteStartElementAsync(self, prefix: StringType, localName: StringType, ns: StringType) -> Task: ...
    
    def WriteString(self, text: StringType) -> VoidType: ...
    
    def WriteStringAsync(self, text: StringType) -> Task: ...
    
    def WriteSurrogateCharEntity(self, lowChar: CharType, highChar: CharType) -> VoidType: ...
    
    def WriteSurrogateCharEntityAsync(self, lowChar: CharType, highChar: CharType) -> Task: ...
    
    def WriteWhitespace(self, ws: StringType) -> VoidType: ...
    
    def WriteWhitespaceAsync(self, ws: StringType) -> Task: ...
    
    def get_Settings(self) -> XmlWriterSettings: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlUtf8RawTextWriterIndent(XmlUtf8RawTextWriter, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, stream: Stream, settings: XmlWriterSettings): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Settings(self) -> XmlWriterSettings: ...
    
    # ---------- Methods ---------- #
    
    def WriteBase64(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> VoidType: ...
    
    def WriteBase64Async(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> Task: ...
    
    def WriteCData(self, text: StringType) -> VoidType: ...
    
    def WriteCDataAsync(self, text: StringType) -> Task: ...
    
    def WriteCharEntity(self, ch: CharType) -> VoidType: ...
    
    def WriteCharEntityAsync(self, ch: CharType) -> Task: ...
    
    def WriteChars(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> VoidType: ...
    
    def WriteCharsAsync(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> Task: ...
    
    def WriteComment(self, text: StringType) -> VoidType: ...
    
    def WriteCommentAsync(self, text: StringType) -> Task: ...
    
    def WriteDocType(self, name: StringType, pubid: StringType, sysid: StringType, subset: StringType) -> VoidType: ...
    
    def WriteDocTypeAsync(self, name: StringType, pubid: StringType, sysid: StringType, subset: StringType) -> Task: ...
    
    def WriteEntityRef(self, name: StringType) -> VoidType: ...
    
    def WriteEntityRefAsync(self, name: StringType) -> Task: ...
    
    def WriteProcessingInstruction(self, target: StringType, text: StringType) -> VoidType: ...
    
    def WriteProcessingInstructionAsync(self, target: StringType, text: StringType) -> Task: ...
    
    @overload
    def WriteRaw(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> VoidType: ...
    
    @overload
    def WriteRaw(self, data: StringType) -> VoidType: ...
    
    @overload
    def WriteRawAsync(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> Task: ...
    
    @overload
    def WriteRawAsync(self, data: StringType) -> Task: ...
    
    @overload
    def WriteStartAttribute(self, prefix: StringType, localName: StringType, ns: StringType) -> VoidType: ...
    
    @overload
    def WriteStartElement(self, prefix: StringType, localName: StringType, ns: StringType) -> VoidType: ...
    
    def WriteStartElementAsync(self, prefix: StringType, localName: StringType, ns: StringType) -> Task: ...
    
    def WriteString(self, text: StringType) -> VoidType: ...
    
    def WriteStringAsync(self, text: StringType) -> Task: ...
    
    def WriteSurrogateCharEntity(self, lowChar: CharType, highChar: CharType) -> VoidType: ...
    
    def WriteSurrogateCharEntityAsync(self, lowChar: CharType, highChar: CharType) -> Task: ...
    
    def WriteWhitespace(self, ws: StringType) -> VoidType: ...
    
    def WriteWhitespaceAsync(self, ws: StringType) -> Task: ...
    
    def get_Settings(self) -> XmlWriterSettings: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlUtf8RawTextWriterIndent(XmlUtf8RawTextWriter, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, stream: Stream, settings: XmlWriterSettings): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Settings(self) -> XmlWriterSettings: ...
    
    # ---------- Methods ---------- #
    
    def WriteBase64(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> VoidType: ...
    
    def WriteBase64Async(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> Task: ...
    
    def WriteCData(self, text: StringType) -> VoidType: ...
    
    def WriteCDataAsync(self, text: StringType) -> Task: ...
    
    def WriteCharEntity(self, ch: CharType) -> VoidType: ...
    
    def WriteCharEntityAsync(self, ch: CharType) -> Task: ...
    
    def WriteChars(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> VoidType: ...
    
    def WriteCharsAsync(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> Task: ...
    
    def WriteComment(self, text: StringType) -> VoidType: ...
    
    def WriteCommentAsync(self, text: StringType) -> Task: ...
    
    def WriteDocType(self, name: StringType, pubid: StringType, sysid: StringType, subset: StringType) -> VoidType: ...
    
    def WriteDocTypeAsync(self, name: StringType, pubid: StringType, sysid: StringType, subset: StringType) -> Task: ...
    
    def WriteEntityRef(self, name: StringType) -> VoidType: ...
    
    def WriteEntityRefAsync(self, name: StringType) -> Task: ...
    
    def WriteProcessingInstruction(self, target: StringType, text: StringType) -> VoidType: ...
    
    def WriteProcessingInstructionAsync(self, target: StringType, text: StringType) -> Task: ...
    
    @overload
    def WriteRaw(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> VoidType: ...
    
    @overload
    def WriteRaw(self, data: StringType) -> VoidType: ...
    
    @overload
    def WriteRawAsync(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> Task: ...
    
    @overload
    def WriteRawAsync(self, data: StringType) -> Task: ...
    
    @overload
    def WriteStartAttribute(self, prefix: StringType, localName: StringType, ns: StringType) -> VoidType: ...
    
    @overload
    def WriteStartElement(self, prefix: StringType, localName: StringType, ns: StringType) -> VoidType: ...
    
    def WriteStartElementAsync(self, prefix: StringType, localName: StringType, ns: StringType) -> Task: ...
    
    def WriteString(self, text: StringType) -> VoidType: ...
    
    def WriteStringAsync(self, text: StringType) -> Task: ...
    
    def WriteSurrogateCharEntity(self, lowChar: CharType, highChar: CharType) -> VoidType: ...
    
    def WriteSurrogateCharEntityAsync(self, lowChar: CharType, highChar: CharType) -> Task: ...
    
    def WriteWhitespace(self, ws: StringType) -> VoidType: ...
    
    def WriteWhitespaceAsync(self, ws: StringType) -> Task: ...
    
    def get_Settings(self) -> XmlWriterSettings: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlValidatingReader(XmlReader, IDisposable, IXmlLineInfo, IXmlNamespaceResolver):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, reader: XmlReader): ...
    
    @overload
    def __init__(self, xmlFragment: StringType, fragType: XmlNodeType, context: XmlParserContext): ...
    
    @overload
    def __init__(self, xmlFragment: Stream, fragType: XmlNodeType, context: XmlParserContext): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AttributeCount(self) -> IntType: ...
    
    @property
    def BaseURI(self) -> StringType: ...
    
    @property
    def CanReadBinaryContent(self) -> BooleanType: ...
    
    @property
    def CanResolveEntity(self) -> BooleanType: ...
    
    @property
    def Depth(self) -> IntType: ...
    
    @property
    def EOF(self) -> BooleanType: ...
    
    @property
    def Encoding(self) -> Encoding: ...
    
    @property
    def EntityHandling(self) -> EntityHandling: ...
    
    @EntityHandling.setter
    def EntityHandling(self, value: EntityHandling) -> None: ...
    
    @property
    def HasValue(self) -> BooleanType: ...
    
    @property
    def IsDefault(self) -> BooleanType: ...
    
    @property
    def IsEmptyElement(self) -> BooleanType: ...
    
    @property
    def LineNumber(self) -> IntType: ...
    
    @property
    def LinePosition(self) -> IntType: ...
    
    @property
    def LocalName(self) -> StringType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def NameTable(self) -> XmlNameTable: ...
    
    @property
    def NamespaceURI(self) -> StringType: ...
    
    @property
    def Namespaces(self) -> BooleanType: ...
    
    @Namespaces.setter
    def Namespaces(self, value: BooleanType) -> None: ...
    
    @property
    def NodeType(self) -> XmlNodeType: ...
    
    @property
    def Prefix(self) -> StringType: ...
    
    @property
    def QuoteChar(self) -> CharType: ...
    
    @property
    def ReadState(self) -> ReadState: ...
    
    @property
    def Reader(self) -> XmlReader: ...
    
    @property
    def SchemaType(self) -> ObjectType: ...
    
    @property
    def Schemas(self) -> XmlSchemaCollection: ...
    
    @property
    def ValidationType(self) -> ValidationType: ...
    
    @ValidationType.setter
    def ValidationType(self, value: ValidationType) -> None: ...
    
    @property
    def Value(self) -> StringType: ...
    
    @property
    def XmlLang(self) -> StringType: ...
    
    @XmlResolver.setter
    def XmlResolver(self, value: XmlResolver) -> None: ...
    
    @property
    def XmlSpace(self) -> XmlSpace: ...
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    @overload
    def GetAttribute(self, name: StringType) -> StringType: ...
    
    @overload
    def GetAttribute(self, localName: StringType, namespaceURI: StringType) -> StringType: ...
    
    @overload
    def GetAttribute(self, i: IntType) -> StringType: ...
    
    def HasLineInfo(self) -> BooleanType: ...
    
    def LookupNamespace(self, prefix: StringType) -> StringType: ...
    
    @overload
    def MoveToAttribute(self, name: StringType) -> BooleanType: ...
    
    @overload
    def MoveToAttribute(self, localName: StringType, namespaceURI: StringType) -> BooleanType: ...
    
    @overload
    def MoveToAttribute(self, i: IntType) -> VoidType: ...
    
    def MoveToElement(self) -> BooleanType: ...
    
    def MoveToFirstAttribute(self) -> BooleanType: ...
    
    def MoveToNextAttribute(self) -> BooleanType: ...
    
    def Read(self) -> BooleanType: ...
    
    def ReadAttributeValue(self) -> BooleanType: ...
    
    def ReadContentAsBase64(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadContentAsBinHex(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadElementContentAsBase64(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadElementContentAsBinHex(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadString(self) -> StringType: ...
    
    def ReadTypedValue(self) -> ObjectType: ...
    
    def ResolveEntity(self) -> VoidType: ...
    
    def add_ValidationEventHandler(self, value: ValidationEventHandler) -> VoidType: ...
    
    def get_AttributeCount(self) -> IntType: ...
    
    def get_BaseURI(self) -> StringType: ...
    
    def get_CanReadBinaryContent(self) -> BooleanType: ...
    
    def get_CanResolveEntity(self) -> BooleanType: ...
    
    def get_Depth(self) -> IntType: ...
    
    def get_EOF(self) -> BooleanType: ...
    
    def get_Encoding(self) -> Encoding: ...
    
    def get_EntityHandling(self) -> EntityHandling: ...
    
    def get_HasValue(self) -> BooleanType: ...
    
    def get_IsDefault(self) -> BooleanType: ...
    
    def get_IsEmptyElement(self) -> BooleanType: ...
    
    def get_LineNumber(self) -> IntType: ...
    
    def get_LinePosition(self) -> IntType: ...
    
    def get_LocalName(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_NameTable(self) -> XmlNameTable: ...
    
    def get_NamespaceURI(self) -> StringType: ...
    
    def get_Namespaces(self) -> BooleanType: ...
    
    def get_NodeType(self) -> XmlNodeType: ...
    
    def get_Prefix(self) -> StringType: ...
    
    def get_QuoteChar(self) -> CharType: ...
    
    def get_ReadState(self) -> ReadState: ...
    
    def get_Reader(self) -> XmlReader: ...
    
    def get_SchemaType(self) -> ObjectType: ...
    
    def get_Schemas(self) -> XmlSchemaCollection: ...
    
    def get_ValidationType(self) -> ValidationType: ...
    
    def get_Value(self) -> StringType: ...
    
    def get_XmlLang(self) -> StringType: ...
    
    def get_XmlSpace(self) -> XmlSpace: ...
    
    def remove_ValidationEventHandler(self, value: ValidationEventHandler) -> VoidType: ...
    
    def set_EntityHandling(self, value: EntityHandling) -> VoidType: ...
    
    def set_Namespaces(self, value: BooleanType) -> VoidType: ...
    
    def set_ValidationType(self, value: ValidationType) -> VoidType: ...
    
    def set_XmlResolver(self, value: XmlResolver) -> VoidType: ...
    
    # ---------- Events ---------- #
    
    ValidationEventHandler: EventType[ValidationEventHandler] = ...
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlValidatingReader(XmlReader, IDisposable, IXmlLineInfo, IXmlNamespaceResolver):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, reader: XmlReader): ...
    
    @overload
    def __init__(self, xmlFragment: StringType, fragType: XmlNodeType, context: XmlParserContext): ...
    
    @overload
    def __init__(self, xmlFragment: Stream, fragType: XmlNodeType, context: XmlParserContext): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AttributeCount(self) -> IntType: ...
    
    @property
    def BaseURI(self) -> StringType: ...
    
    @property
    def CanReadBinaryContent(self) -> BooleanType: ...
    
    @property
    def CanResolveEntity(self) -> BooleanType: ...
    
    @property
    def Depth(self) -> IntType: ...
    
    @property
    def EOF(self) -> BooleanType: ...
    
    @property
    def Encoding(self) -> Encoding: ...
    
    @property
    def EntityHandling(self) -> EntityHandling: ...
    
    @EntityHandling.setter
    def EntityHandling(self, value: EntityHandling) -> None: ...
    
    @property
    def HasValue(self) -> BooleanType: ...
    
    @property
    def IsDefault(self) -> BooleanType: ...
    
    @property
    def IsEmptyElement(self) -> BooleanType: ...
    
    @property
    def LineNumber(self) -> IntType: ...
    
    @property
    def LinePosition(self) -> IntType: ...
    
    @property
    def LocalName(self) -> StringType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def NameTable(self) -> XmlNameTable: ...
    
    @property
    def NamespaceURI(self) -> StringType: ...
    
    @property
    def Namespaces(self) -> BooleanType: ...
    
    @Namespaces.setter
    def Namespaces(self, value: BooleanType) -> None: ...
    
    @property
    def NodeType(self) -> XmlNodeType: ...
    
    @property
    def Prefix(self) -> StringType: ...
    
    @property
    def QuoteChar(self) -> CharType: ...
    
    @property
    def ReadState(self) -> ReadState: ...
    
    @property
    def Reader(self) -> XmlReader: ...
    
    @property
    def SchemaType(self) -> ObjectType: ...
    
    @property
    def Schemas(self) -> XmlSchemaCollection: ...
    
    @property
    def ValidationType(self) -> ValidationType: ...
    
    @ValidationType.setter
    def ValidationType(self, value: ValidationType) -> None: ...
    
    @property
    def Value(self) -> StringType: ...
    
    @property
    def XmlLang(self) -> StringType: ...
    
    @XmlResolver.setter
    def XmlResolver(self, value: XmlResolver) -> None: ...
    
    @property
    def XmlSpace(self) -> XmlSpace: ...
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    @overload
    def GetAttribute(self, name: StringType) -> StringType: ...
    
    @overload
    def GetAttribute(self, localName: StringType, namespaceURI: StringType) -> StringType: ...
    
    @overload
    def GetAttribute(self, i: IntType) -> StringType: ...
    
    def HasLineInfo(self) -> BooleanType: ...
    
    def LookupNamespace(self, prefix: StringType) -> StringType: ...
    
    @overload
    def MoveToAttribute(self, name: StringType) -> BooleanType: ...
    
    @overload
    def MoveToAttribute(self, localName: StringType, namespaceURI: StringType) -> BooleanType: ...
    
    @overload
    def MoveToAttribute(self, i: IntType) -> VoidType: ...
    
    def MoveToElement(self) -> BooleanType: ...
    
    def MoveToFirstAttribute(self) -> BooleanType: ...
    
    def MoveToNextAttribute(self) -> BooleanType: ...
    
    def Read(self) -> BooleanType: ...
    
    def ReadAttributeValue(self) -> BooleanType: ...
    
    def ReadContentAsBase64(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadContentAsBinHex(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadElementContentAsBase64(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadElementContentAsBinHex(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadString(self) -> StringType: ...
    
    def ReadTypedValue(self) -> ObjectType: ...
    
    def ResolveEntity(self) -> VoidType: ...
    
    def add_ValidationEventHandler(self, value: ValidationEventHandler) -> VoidType: ...
    
    def get_AttributeCount(self) -> IntType: ...
    
    def get_BaseURI(self) -> StringType: ...
    
    def get_CanReadBinaryContent(self) -> BooleanType: ...
    
    def get_CanResolveEntity(self) -> BooleanType: ...
    
    def get_Depth(self) -> IntType: ...
    
    def get_EOF(self) -> BooleanType: ...
    
    def get_Encoding(self) -> Encoding: ...
    
    def get_EntityHandling(self) -> EntityHandling: ...
    
    def get_HasValue(self) -> BooleanType: ...
    
    def get_IsDefault(self) -> BooleanType: ...
    
    def get_IsEmptyElement(self) -> BooleanType: ...
    
    def get_LineNumber(self) -> IntType: ...
    
    def get_LinePosition(self) -> IntType: ...
    
    def get_LocalName(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_NameTable(self) -> XmlNameTable: ...
    
    def get_NamespaceURI(self) -> StringType: ...
    
    def get_Namespaces(self) -> BooleanType: ...
    
    def get_NodeType(self) -> XmlNodeType: ...
    
    def get_Prefix(self) -> StringType: ...
    
    def get_QuoteChar(self) -> CharType: ...
    
    def get_ReadState(self) -> ReadState: ...
    
    def get_Reader(self) -> XmlReader: ...
    
    def get_SchemaType(self) -> ObjectType: ...
    
    def get_Schemas(self) -> XmlSchemaCollection: ...
    
    def get_ValidationType(self) -> ValidationType: ...
    
    def get_Value(self) -> StringType: ...
    
    def get_XmlLang(self) -> StringType: ...
    
    def get_XmlSpace(self) -> XmlSpace: ...
    
    def remove_ValidationEventHandler(self, value: ValidationEventHandler) -> VoidType: ...
    
    def set_EntityHandling(self, value: EntityHandling) -> VoidType: ...
    
    def set_Namespaces(self, value: BooleanType) -> VoidType: ...
    
    def set_ValidationType(self, value: ValidationType) -> VoidType: ...
    
    def set_XmlResolver(self, value: XmlResolver) -> VoidType: ...
    
    # ---------- Events ---------- #
    
    ValidationEventHandler: EventType[ValidationEventHandler] = ...
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlValidatingReaderImpl(XmlReader, IDisposable, IXmlLineInfo, IXmlNamespaceResolver):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def AttributeCount(self) -> IntType: ...
    
    @property
    def BaseURI(self) -> StringType: ...
    
    @property
    def CanReadBinaryContent(self) -> BooleanType: ...
    
    @property
    def CanResolveEntity(self) -> BooleanType: ...
    
    @property
    def Depth(self) -> IntType: ...
    
    @property
    def EOF(self) -> BooleanType: ...
    
    @property
    def HasValue(self) -> BooleanType: ...
    
    @property
    def IsDefault(self) -> BooleanType: ...
    
    @property
    def IsEmptyElement(self) -> BooleanType: ...
    
    @property
    def LineNumber(self) -> IntType: ...
    
    @property
    def LinePosition(self) -> IntType: ...
    
    @property
    def LocalName(self) -> StringType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def NameTable(self) -> XmlNameTable: ...
    
    @property
    def NamespaceURI(self) -> StringType: ...
    
    @property
    def NodeType(self) -> XmlNodeType: ...
    
    @property
    def Prefix(self) -> StringType: ...
    
    @property
    def QuoteChar(self) -> CharType: ...
    
    @property
    def ReadState(self) -> ReadState: ...
    
    @property
    def Settings(self) -> XmlReaderSettings: ...
    
    @property
    def Value(self) -> StringType: ...
    
    @property
    def XmlLang(self) -> StringType: ...
    
    @property
    def XmlSpace(self) -> XmlSpace: ...
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    @overload
    def GetAttribute(self, name: StringType) -> StringType: ...
    
    @overload
    def GetAttribute(self, localName: StringType, namespaceURI: StringType) -> StringType: ...
    
    @overload
    def GetAttribute(self, i: IntType) -> StringType: ...
    
    def GetValueAsync(self) -> Task[StringType]: ...
    
    def HasLineInfo(self) -> BooleanType: ...
    
    def LookupNamespace(self, prefix: StringType) -> StringType: ...
    
    @overload
    def MoveToAttribute(self, name: StringType) -> BooleanType: ...
    
    @overload
    def MoveToAttribute(self, localName: StringType, namespaceURI: StringType) -> BooleanType: ...
    
    @overload
    def MoveToAttribute(self, i: IntType) -> VoidType: ...
    
    def MoveToElement(self) -> BooleanType: ...
    
    def MoveToFirstAttribute(self) -> BooleanType: ...
    
    def MoveToNextAttribute(self) -> BooleanType: ...
    
    def Read(self) -> BooleanType: ...
    
    def ReadAsync(self) -> Task[BooleanType]: ...
    
    def ReadAttributeValue(self) -> BooleanType: ...
    
    def ReadContentAsBase64(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadContentAsBase64Async(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> Task[IntType]: ...
    
    def ReadContentAsBinHex(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadContentAsBinHexAsync(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> Task[IntType]: ...
    
    def ReadElementContentAsBase64(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadElementContentAsBase64Async(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> Task[IntType]: ...
    
    def ReadElementContentAsBinHex(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadElementContentAsBinHexAsync(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> Task[IntType]: ...
    
    def ReadString(self) -> StringType: ...
    
    def ReadTypedValue(self) -> ObjectType: ...
    
    def ReadTypedValueAsync(self) -> Task[ObjectType]: ...
    
    def ResolveEntity(self) -> VoidType: ...
    
    def get_AttributeCount(self) -> IntType: ...
    
    def get_BaseURI(self) -> StringType: ...
    
    def get_CanReadBinaryContent(self) -> BooleanType: ...
    
    def get_CanResolveEntity(self) -> BooleanType: ...
    
    def get_Depth(self) -> IntType: ...
    
    def get_EOF(self) -> BooleanType: ...
    
    def get_HasValue(self) -> BooleanType: ...
    
    def get_IsDefault(self) -> BooleanType: ...
    
    def get_IsEmptyElement(self) -> BooleanType: ...
    
    def get_LineNumber(self) -> IntType: ...
    
    def get_LinePosition(self) -> IntType: ...
    
    def get_LocalName(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_NameTable(self) -> XmlNameTable: ...
    
    def get_NamespaceURI(self) -> StringType: ...
    
    def get_NodeType(self) -> XmlNodeType: ...
    
    def get_Prefix(self) -> StringType: ...
    
    def get_QuoteChar(self) -> CharType: ...
    
    def get_ReadState(self) -> ReadState: ...
    
    def get_Settings(self) -> XmlReaderSettings: ...
    
    def get_Value(self) -> StringType: ...
    
    def get_XmlLang(self) -> StringType: ...
    
    def get_XmlSpace(self) -> XmlSpace: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlValidatingReaderImpl(XmlReader, IDisposable, IXmlLineInfo, IXmlNamespaceResolver):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def AttributeCount(self) -> IntType: ...
    
    @property
    def BaseURI(self) -> StringType: ...
    
    @property
    def CanReadBinaryContent(self) -> BooleanType: ...
    
    @property
    def CanResolveEntity(self) -> BooleanType: ...
    
    @property
    def Depth(self) -> IntType: ...
    
    @property
    def EOF(self) -> BooleanType: ...
    
    @property
    def HasValue(self) -> BooleanType: ...
    
    @property
    def IsDefault(self) -> BooleanType: ...
    
    @property
    def IsEmptyElement(self) -> BooleanType: ...
    
    @property
    def LineNumber(self) -> IntType: ...
    
    @property
    def LinePosition(self) -> IntType: ...
    
    @property
    def LocalName(self) -> StringType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def NameTable(self) -> XmlNameTable: ...
    
    @property
    def NamespaceURI(self) -> StringType: ...
    
    @property
    def NodeType(self) -> XmlNodeType: ...
    
    @property
    def Prefix(self) -> StringType: ...
    
    @property
    def QuoteChar(self) -> CharType: ...
    
    @property
    def ReadState(self) -> ReadState: ...
    
    @property
    def Settings(self) -> XmlReaderSettings: ...
    
    @property
    def Value(self) -> StringType: ...
    
    @property
    def XmlLang(self) -> StringType: ...
    
    @property
    def XmlSpace(self) -> XmlSpace: ...
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    @overload
    def GetAttribute(self, name: StringType) -> StringType: ...
    
    @overload
    def GetAttribute(self, localName: StringType, namespaceURI: StringType) -> StringType: ...
    
    @overload
    def GetAttribute(self, i: IntType) -> StringType: ...
    
    def GetValueAsync(self) -> Task[StringType]: ...
    
    def HasLineInfo(self) -> BooleanType: ...
    
    def LookupNamespace(self, prefix: StringType) -> StringType: ...
    
    @overload
    def MoveToAttribute(self, name: StringType) -> BooleanType: ...
    
    @overload
    def MoveToAttribute(self, localName: StringType, namespaceURI: StringType) -> BooleanType: ...
    
    @overload
    def MoveToAttribute(self, i: IntType) -> VoidType: ...
    
    def MoveToElement(self) -> BooleanType: ...
    
    def MoveToFirstAttribute(self) -> BooleanType: ...
    
    def MoveToNextAttribute(self) -> BooleanType: ...
    
    def Read(self) -> BooleanType: ...
    
    def ReadAsync(self) -> Task[BooleanType]: ...
    
    def ReadAttributeValue(self) -> BooleanType: ...
    
    def ReadContentAsBase64(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadContentAsBase64Async(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> Task[IntType]: ...
    
    def ReadContentAsBinHex(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadContentAsBinHexAsync(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> Task[IntType]: ...
    
    def ReadElementContentAsBase64(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadElementContentAsBase64Async(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> Task[IntType]: ...
    
    def ReadElementContentAsBinHex(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadElementContentAsBinHexAsync(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> Task[IntType]: ...
    
    def ReadString(self) -> StringType: ...
    
    def ReadTypedValue(self) -> ObjectType: ...
    
    def ReadTypedValueAsync(self) -> Task[ObjectType]: ...
    
    def ResolveEntity(self) -> VoidType: ...
    
    def get_AttributeCount(self) -> IntType: ...
    
    def get_BaseURI(self) -> StringType: ...
    
    def get_CanReadBinaryContent(self) -> BooleanType: ...
    
    def get_CanResolveEntity(self) -> BooleanType: ...
    
    def get_Depth(self) -> IntType: ...
    
    def get_EOF(self) -> BooleanType: ...
    
    def get_HasValue(self) -> BooleanType: ...
    
    def get_IsDefault(self) -> BooleanType: ...
    
    def get_IsEmptyElement(self) -> BooleanType: ...
    
    def get_LineNumber(self) -> IntType: ...
    
    def get_LinePosition(self) -> IntType: ...
    
    def get_LocalName(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_NameTable(self) -> XmlNameTable: ...
    
    def get_NamespaceURI(self) -> StringType: ...
    
    def get_NodeType(self) -> XmlNodeType: ...
    
    def get_Prefix(self) -> StringType: ...
    
    def get_QuoteChar(self) -> CharType: ...
    
    def get_ReadState(self) -> ReadState: ...
    
    def get_Settings(self) -> XmlReaderSettings: ...
    
    def get_Value(self) -> StringType: ...
    
    def get_XmlLang(self) -> StringType: ...
    
    def get_XmlSpace(self) -> XmlSpace: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlWellFormedWriter(XmlWriter, IDisposable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Settings(self) -> XmlWriterSettings: ...
    
    @property
    def WriteState(self) -> WriteState: ...
    
    @property
    def XmlLang(self) -> StringType: ...
    
    @property
    def XmlSpace(self) -> XmlSpace: ...
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    def Flush(self) -> VoidType: ...
    
    def FlushAsync(self) -> Task: ...
    
    def LookupPrefix(self, ns: StringType) -> StringType: ...
    
    def WriteBase64(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> VoidType: ...
    
    def WriteBase64Async(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> Task: ...
    
    def WriteBinHex(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> VoidType: ...
    
    def WriteBinHexAsync(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> Task: ...
    
    def WriteCData(self, text: StringType) -> VoidType: ...
    
    def WriteCDataAsync(self, text: StringType) -> Task: ...
    
    def WriteCharEntity(self, ch: CharType) -> VoidType: ...
    
    def WriteCharEntityAsync(self, ch: CharType) -> Task: ...
    
    def WriteChars(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> VoidType: ...
    
    def WriteCharsAsync(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> Task: ...
    
    def WriteComment(self, text: StringType) -> VoidType: ...
    
    def WriteCommentAsync(self, text: StringType) -> Task: ...
    
    def WriteDocType(self, name: StringType, pubid: StringType, sysid: StringType, subset: StringType) -> VoidType: ...
    
    def WriteDocTypeAsync(self, name: StringType, pubid: StringType, sysid: StringType, subset: StringType) -> Task: ...
    
    def WriteEndAttribute(self) -> VoidType: ...
    
    def WriteEndDocument(self) -> VoidType: ...
    
    def WriteEndDocumentAsync(self) -> Task: ...
    
    def WriteEndElement(self) -> VoidType: ...
    
    def WriteEndElementAsync(self) -> Task: ...
    
    def WriteEntityRef(self, name: StringType) -> VoidType: ...
    
    def WriteEntityRefAsync(self, name: StringType) -> Task: ...
    
    def WriteFullEndElement(self) -> VoidType: ...
    
    def WriteFullEndElementAsync(self) -> Task: ...
    
    def WriteProcessingInstruction(self, name: StringType, text: StringType) -> VoidType: ...
    
    def WriteProcessingInstructionAsync(self, name: StringType, text: StringType) -> Task: ...
    
    def WriteQualifiedName(self, localName: StringType, ns: StringType) -> VoidType: ...
    
    def WriteQualifiedNameAsync(self, localName: StringType, ns: StringType) -> Task: ...
    
    @overload
    def WriteRaw(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> VoidType: ...
    
    @overload
    def WriteRaw(self, data: StringType) -> VoidType: ...
    
    @overload
    def WriteRawAsync(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> Task: ...
    
    @overload
    def WriteRawAsync(self, data: StringType) -> Task: ...
    
    @overload
    def WriteStartAttribute(self, prefix: StringType, localName: StringType, namespaceName: StringType) -> VoidType: ...
    
    @overload
    def WriteStartDocument(self) -> VoidType: ...
    
    @overload
    def WriteStartDocument(self, standalone: BooleanType) -> VoidType: ...
    
    @overload
    def WriteStartDocumentAsync(self) -> Task: ...
    
    @overload
    def WriteStartDocumentAsync(self, standalone: BooleanType) -> Task: ...
    
    @overload
    def WriteStartElement(self, prefix: StringType, localName: StringType, ns: StringType) -> VoidType: ...
    
    def WriteStartElementAsync(self, prefix: StringType, localName: StringType, ns: StringType) -> Task: ...
    
    def WriteString(self, text: StringType) -> VoidType: ...
    
    def WriteStringAsync(self, text: StringType) -> Task: ...
    
    def WriteSurrogateCharEntity(self, lowChar: CharType, highChar: CharType) -> VoidType: ...
    
    def WriteSurrogateCharEntityAsync(self, lowChar: CharType, highChar: CharType) -> Task: ...
    
    @overload
    def WriteValue(self, value: BooleanType) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: DateTime) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: DateTimeOffset) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: DoubleType) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: FloatType) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: DecimalType) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: IntType) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: LongType) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: StringType) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: ObjectType) -> VoidType: ...
    
    def WriteWhitespace(self, ws: StringType) -> VoidType: ...
    
    def WriteWhitespaceAsync(self, ws: StringType) -> Task: ...
    
    def get_Settings(self) -> XmlWriterSettings: ...
    
    def get_WriteState(self) -> WriteState: ...
    
    def get_XmlLang(self) -> StringType: ...
    
    def get_XmlSpace(self) -> XmlSpace: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlWellFormedWriter(XmlWriter, IDisposable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Settings(self) -> XmlWriterSettings: ...
    
    @property
    def WriteState(self) -> WriteState: ...
    
    @property
    def XmlLang(self) -> StringType: ...
    
    @property
    def XmlSpace(self) -> XmlSpace: ...
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    def Flush(self) -> VoidType: ...
    
    def FlushAsync(self) -> Task: ...
    
    def LookupPrefix(self, ns: StringType) -> StringType: ...
    
    def WriteBase64(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> VoidType: ...
    
    def WriteBase64Async(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> Task: ...
    
    def WriteBinHex(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> VoidType: ...
    
    def WriteBinHexAsync(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> Task: ...
    
    def WriteCData(self, text: StringType) -> VoidType: ...
    
    def WriteCDataAsync(self, text: StringType) -> Task: ...
    
    def WriteCharEntity(self, ch: CharType) -> VoidType: ...
    
    def WriteCharEntityAsync(self, ch: CharType) -> Task: ...
    
    def WriteChars(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> VoidType: ...
    
    def WriteCharsAsync(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> Task: ...
    
    def WriteComment(self, text: StringType) -> VoidType: ...
    
    def WriteCommentAsync(self, text: StringType) -> Task: ...
    
    def WriteDocType(self, name: StringType, pubid: StringType, sysid: StringType, subset: StringType) -> VoidType: ...
    
    def WriteDocTypeAsync(self, name: StringType, pubid: StringType, sysid: StringType, subset: StringType) -> Task: ...
    
    def WriteEndAttribute(self) -> VoidType: ...
    
    def WriteEndDocument(self) -> VoidType: ...
    
    def WriteEndDocumentAsync(self) -> Task: ...
    
    def WriteEndElement(self) -> VoidType: ...
    
    def WriteEndElementAsync(self) -> Task: ...
    
    def WriteEntityRef(self, name: StringType) -> VoidType: ...
    
    def WriteEntityRefAsync(self, name: StringType) -> Task: ...
    
    def WriteFullEndElement(self) -> VoidType: ...
    
    def WriteFullEndElementAsync(self) -> Task: ...
    
    def WriteProcessingInstruction(self, name: StringType, text: StringType) -> VoidType: ...
    
    def WriteProcessingInstructionAsync(self, name: StringType, text: StringType) -> Task: ...
    
    def WriteQualifiedName(self, localName: StringType, ns: StringType) -> VoidType: ...
    
    def WriteQualifiedNameAsync(self, localName: StringType, ns: StringType) -> Task: ...
    
    @overload
    def WriteRaw(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> VoidType: ...
    
    @overload
    def WriteRaw(self, data: StringType) -> VoidType: ...
    
    @overload
    def WriteRawAsync(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> Task: ...
    
    @overload
    def WriteRawAsync(self, data: StringType) -> Task: ...
    
    @overload
    def WriteStartAttribute(self, prefix: StringType, localName: StringType, namespaceName: StringType) -> VoidType: ...
    
    @overload
    def WriteStartDocument(self) -> VoidType: ...
    
    @overload
    def WriteStartDocument(self, standalone: BooleanType) -> VoidType: ...
    
    @overload
    def WriteStartDocumentAsync(self) -> Task: ...
    
    @overload
    def WriteStartDocumentAsync(self, standalone: BooleanType) -> Task: ...
    
    @overload
    def WriteStartElement(self, prefix: StringType, localName: StringType, ns: StringType) -> VoidType: ...
    
    def WriteStartElementAsync(self, prefix: StringType, localName: StringType, ns: StringType) -> Task: ...
    
    def WriteString(self, text: StringType) -> VoidType: ...
    
    def WriteStringAsync(self, text: StringType) -> Task: ...
    
    def WriteSurrogateCharEntity(self, lowChar: CharType, highChar: CharType) -> VoidType: ...
    
    def WriteSurrogateCharEntityAsync(self, lowChar: CharType, highChar: CharType) -> Task: ...
    
    @overload
    def WriteValue(self, value: BooleanType) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: DateTime) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: DateTimeOffset) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: DoubleType) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: FloatType) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: DecimalType) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: IntType) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: LongType) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: StringType) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: ObjectType) -> VoidType: ...
    
    def WriteWhitespace(self, ws: StringType) -> VoidType: ...
    
    def WriteWhitespaceAsync(self, ws: StringType) -> Task: ...
    
    def get_Settings(self) -> XmlWriterSettings: ...
    
    def get_WriteState(self) -> WriteState: ...
    
    def get_XmlLang(self) -> StringType: ...
    
    def get_XmlSpace(self) -> XmlSpace: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlWhitespace(XmlCharacterData, ICloneable, IEnumerable, IXPathNavigable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def LocalName(self) -> StringType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def NodeType(self) -> XmlNodeType: ...
    
    @property
    def ParentNode(self) -> XmlNode: ...
    
    @property
    def PreviousText(self) -> XmlNode: ...
    
    @property
    def Value(self) -> StringType: ...
    
    @Value.setter
    def Value(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def CloneNode(self, deep: BooleanType) -> XmlNode: ...
    
    def WriteContentTo(self, w: XmlWriter) -> VoidType: ...
    
    def WriteTo(self, w: XmlWriter) -> VoidType: ...
    
    def get_LocalName(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_NodeType(self) -> XmlNodeType: ...
    
    def get_ParentNode(self) -> XmlNode: ...
    
    def get_PreviousText(self) -> XmlNode: ...
    
    def get_Value(self) -> StringType: ...
    
    def set_Value(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlWhitespace(XmlCharacterData, ICloneable, IEnumerable, IXPathNavigable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def LocalName(self) -> StringType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def NodeType(self) -> XmlNodeType: ...
    
    @property
    def ParentNode(self) -> XmlNode: ...
    
    @property
    def PreviousText(self) -> XmlNode: ...
    
    @property
    def Value(self) -> StringType: ...
    
    @Value.setter
    def Value(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def CloneNode(self, deep: BooleanType) -> XmlNode: ...
    
    def WriteContentTo(self, w: XmlWriter) -> VoidType: ...
    
    def WriteTo(self, w: XmlWriter) -> VoidType: ...
    
    def get_LocalName(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_NodeType(self) -> XmlNodeType: ...
    
    def get_ParentNode(self) -> XmlNode: ...
    
    def get_PreviousText(self) -> XmlNode: ...
    
    def get_Value(self) -> StringType: ...
    
    def set_Value(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlWrappingReader(XmlReader, IDisposable, IXmlLineInfo):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def AttributeCount(self) -> IntType: ...
    
    @property
    def BaseURI(self) -> StringType: ...
    
    @property
    def CanResolveEntity(self) -> BooleanType: ...
    
    @property
    def Depth(self) -> IntType: ...
    
    @property
    def EOF(self) -> BooleanType: ...
    
    @property
    def HasAttributes(self) -> BooleanType: ...
    
    @property
    def HasValue(self) -> BooleanType: ...
    
    @property
    def IsDefault(self) -> BooleanType: ...
    
    @property
    def IsEmptyElement(self) -> BooleanType: ...
    
    @property
    def LineNumber(self) -> IntType: ...
    
    @property
    def LinePosition(self) -> IntType: ...
    
    @property
    def LocalName(self) -> StringType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def NameTable(self) -> XmlNameTable: ...
    
    @property
    def NamespaceURI(self) -> StringType: ...
    
    @property
    def NodeType(self) -> XmlNodeType: ...
    
    @property
    def Prefix(self) -> StringType: ...
    
    @property
    def QuoteChar(self) -> CharType: ...
    
    @property
    def ReadState(self) -> ReadState: ...
    
    @property
    def SchemaInfo(self) -> IXmlSchemaInfo: ...
    
    @property
    def Settings(self) -> XmlReaderSettings: ...
    
    @property
    def Value(self) -> StringType: ...
    
    @property
    def ValueType(self) -> TypeType: ...
    
    @property
    def XmlLang(self) -> StringType: ...
    
    @property
    def XmlSpace(self) -> XmlSpace: ...
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    @overload
    def GetAttribute(self, name: StringType) -> StringType: ...
    
    @overload
    def GetAttribute(self, name: StringType, namespaceURI: StringType) -> StringType: ...
    
    @overload
    def GetAttribute(self, i: IntType) -> StringType: ...
    
    def GetValueAsync(self) -> Task[StringType]: ...
    
    def HasLineInfo(self) -> BooleanType: ...
    
    def LookupNamespace(self, prefix: StringType) -> StringType: ...
    
    @overload
    def MoveToAttribute(self, name: StringType) -> BooleanType: ...
    
    @overload
    def MoveToAttribute(self, name: StringType, ns: StringType) -> BooleanType: ...
    
    @overload
    def MoveToAttribute(self, i: IntType) -> VoidType: ...
    
    def MoveToElement(self) -> BooleanType: ...
    
    def MoveToFirstAttribute(self) -> BooleanType: ...
    
    def MoveToNextAttribute(self) -> BooleanType: ...
    
    def Read(self) -> BooleanType: ...
    
    def ReadAsync(self) -> Task[BooleanType]: ...
    
    def ReadAttributeValue(self) -> BooleanType: ...
    
    def ResolveEntity(self) -> VoidType: ...
    
    def Skip(self) -> VoidType: ...
    
    def SkipAsync(self) -> Task: ...
    
    def get_AttributeCount(self) -> IntType: ...
    
    def get_BaseURI(self) -> StringType: ...
    
    def get_CanResolveEntity(self) -> BooleanType: ...
    
    def get_Depth(self) -> IntType: ...
    
    def get_EOF(self) -> BooleanType: ...
    
    def get_HasAttributes(self) -> BooleanType: ...
    
    def get_HasValue(self) -> BooleanType: ...
    
    def get_IsDefault(self) -> BooleanType: ...
    
    def get_IsEmptyElement(self) -> BooleanType: ...
    
    def get_LineNumber(self) -> IntType: ...
    
    def get_LinePosition(self) -> IntType: ...
    
    def get_LocalName(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_NameTable(self) -> XmlNameTable: ...
    
    def get_NamespaceURI(self) -> StringType: ...
    
    def get_NodeType(self) -> XmlNodeType: ...
    
    def get_Prefix(self) -> StringType: ...
    
    def get_QuoteChar(self) -> CharType: ...
    
    def get_ReadState(self) -> ReadState: ...
    
    def get_SchemaInfo(self) -> IXmlSchemaInfo: ...
    
    def get_Settings(self) -> XmlReaderSettings: ...
    
    def get_Value(self) -> StringType: ...
    
    def get_ValueType(self) -> TypeType: ...
    
    def get_XmlLang(self) -> StringType: ...
    
    def get_XmlSpace(self) -> XmlSpace: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlWrappingReader(XmlReader, IDisposable, IXmlLineInfo):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def AttributeCount(self) -> IntType: ...
    
    @property
    def BaseURI(self) -> StringType: ...
    
    @property
    def CanResolveEntity(self) -> BooleanType: ...
    
    @property
    def Depth(self) -> IntType: ...
    
    @property
    def EOF(self) -> BooleanType: ...
    
    @property
    def HasAttributes(self) -> BooleanType: ...
    
    @property
    def HasValue(self) -> BooleanType: ...
    
    @property
    def IsDefault(self) -> BooleanType: ...
    
    @property
    def IsEmptyElement(self) -> BooleanType: ...
    
    @property
    def LineNumber(self) -> IntType: ...
    
    @property
    def LinePosition(self) -> IntType: ...
    
    @property
    def LocalName(self) -> StringType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def NameTable(self) -> XmlNameTable: ...
    
    @property
    def NamespaceURI(self) -> StringType: ...
    
    @property
    def NodeType(self) -> XmlNodeType: ...
    
    @property
    def Prefix(self) -> StringType: ...
    
    @property
    def QuoteChar(self) -> CharType: ...
    
    @property
    def ReadState(self) -> ReadState: ...
    
    @property
    def SchemaInfo(self) -> IXmlSchemaInfo: ...
    
    @property
    def Settings(self) -> XmlReaderSettings: ...
    
    @property
    def Value(self) -> StringType: ...
    
    @property
    def ValueType(self) -> TypeType: ...
    
    @property
    def XmlLang(self) -> StringType: ...
    
    @property
    def XmlSpace(self) -> XmlSpace: ...
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    @overload
    def GetAttribute(self, name: StringType) -> StringType: ...
    
    @overload
    def GetAttribute(self, name: StringType, namespaceURI: StringType) -> StringType: ...
    
    @overload
    def GetAttribute(self, i: IntType) -> StringType: ...
    
    def GetValueAsync(self) -> Task[StringType]: ...
    
    def HasLineInfo(self) -> BooleanType: ...
    
    def LookupNamespace(self, prefix: StringType) -> StringType: ...
    
    @overload
    def MoveToAttribute(self, name: StringType) -> BooleanType: ...
    
    @overload
    def MoveToAttribute(self, name: StringType, ns: StringType) -> BooleanType: ...
    
    @overload
    def MoveToAttribute(self, i: IntType) -> VoidType: ...
    
    def MoveToElement(self) -> BooleanType: ...
    
    def MoveToFirstAttribute(self) -> BooleanType: ...
    
    def MoveToNextAttribute(self) -> BooleanType: ...
    
    def Read(self) -> BooleanType: ...
    
    def ReadAsync(self) -> Task[BooleanType]: ...
    
    def ReadAttributeValue(self) -> BooleanType: ...
    
    def ResolveEntity(self) -> VoidType: ...
    
    def Skip(self) -> VoidType: ...
    
    def SkipAsync(self) -> Task: ...
    
    def get_AttributeCount(self) -> IntType: ...
    
    def get_BaseURI(self) -> StringType: ...
    
    def get_CanResolveEntity(self) -> BooleanType: ...
    
    def get_Depth(self) -> IntType: ...
    
    def get_EOF(self) -> BooleanType: ...
    
    def get_HasAttributes(self) -> BooleanType: ...
    
    def get_HasValue(self) -> BooleanType: ...
    
    def get_IsDefault(self) -> BooleanType: ...
    
    def get_IsEmptyElement(self) -> BooleanType: ...
    
    def get_LineNumber(self) -> IntType: ...
    
    def get_LinePosition(self) -> IntType: ...
    
    def get_LocalName(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_NameTable(self) -> XmlNameTable: ...
    
    def get_NamespaceURI(self) -> StringType: ...
    
    def get_NodeType(self) -> XmlNodeType: ...
    
    def get_Prefix(self) -> StringType: ...
    
    def get_QuoteChar(self) -> CharType: ...
    
    def get_ReadState(self) -> ReadState: ...
    
    def get_SchemaInfo(self) -> IXmlSchemaInfo: ...
    
    def get_Settings(self) -> XmlReaderSettings: ...
    
    def get_Value(self) -> StringType: ...
    
    def get_ValueType(self) -> TypeType: ...
    
    def get_XmlLang(self) -> StringType: ...
    
    def get_XmlSpace(self) -> XmlSpace: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlWrappingWriter(XmlWriter, IDisposable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Settings(self) -> XmlWriterSettings: ...
    
    @property
    def WriteState(self) -> WriteState: ...
    
    @property
    def XmlLang(self) -> StringType: ...
    
    @property
    def XmlSpace(self) -> XmlSpace: ...
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    def Flush(self) -> VoidType: ...
    
    def FlushAsync(self) -> Task: ...
    
    def LookupPrefix(self, ns: StringType) -> StringType: ...
    
    def WriteBase64(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> VoidType: ...
    
    def WriteBase64Async(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> Task: ...
    
    def WriteCData(self, text: StringType) -> VoidType: ...
    
    def WriteCDataAsync(self, text: StringType) -> Task: ...
    
    def WriteCharEntity(self, ch: CharType) -> VoidType: ...
    
    def WriteCharEntityAsync(self, ch: CharType) -> Task: ...
    
    def WriteChars(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> VoidType: ...
    
    def WriteCharsAsync(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> Task: ...
    
    def WriteComment(self, text: StringType) -> VoidType: ...
    
    def WriteCommentAsync(self, text: StringType) -> Task: ...
    
    def WriteDocType(self, name: StringType, pubid: StringType, sysid: StringType, subset: StringType) -> VoidType: ...
    
    def WriteDocTypeAsync(self, name: StringType, pubid: StringType, sysid: StringType, subset: StringType) -> Task: ...
    
    def WriteEndAttribute(self) -> VoidType: ...
    
    def WriteEndDocument(self) -> VoidType: ...
    
    def WriteEndDocumentAsync(self) -> Task: ...
    
    def WriteEndElement(self) -> VoidType: ...
    
    def WriteEndElementAsync(self) -> Task: ...
    
    def WriteEntityRef(self, name: StringType) -> VoidType: ...
    
    def WriteEntityRefAsync(self, name: StringType) -> Task: ...
    
    def WriteFullEndElement(self) -> VoidType: ...
    
    def WriteFullEndElementAsync(self) -> Task: ...
    
    def WriteProcessingInstruction(self, name: StringType, text: StringType) -> VoidType: ...
    
    def WriteProcessingInstructionAsync(self, name: StringType, text: StringType) -> Task: ...
    
    @overload
    def WriteRaw(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> VoidType: ...
    
    @overload
    def WriteRaw(self, data: StringType) -> VoidType: ...
    
    @overload
    def WriteRawAsync(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> Task: ...
    
    @overload
    def WriteRawAsync(self, data: StringType) -> Task: ...
    
    @overload
    def WriteStartAttribute(self, prefix: StringType, localName: StringType, ns: StringType) -> VoidType: ...
    
    @overload
    def WriteStartDocument(self) -> VoidType: ...
    
    @overload
    def WriteStartDocument(self, standalone: BooleanType) -> VoidType: ...
    
    @overload
    def WriteStartDocumentAsync(self) -> Task: ...
    
    @overload
    def WriteStartDocumentAsync(self, standalone: BooleanType) -> Task: ...
    
    @overload
    def WriteStartElement(self, prefix: StringType, localName: StringType, ns: StringType) -> VoidType: ...
    
    def WriteStartElementAsync(self, prefix: StringType, localName: StringType, ns: StringType) -> Task: ...
    
    def WriteString(self, text: StringType) -> VoidType: ...
    
    def WriteStringAsync(self, text: StringType) -> Task: ...
    
    def WriteSurrogateCharEntity(self, lowChar: CharType, highChar: CharType) -> VoidType: ...
    
    def WriteSurrogateCharEntityAsync(self, lowChar: CharType, highChar: CharType) -> Task: ...
    
    @overload
    def WriteValue(self, value: ObjectType) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: StringType) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: BooleanType) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: DateTime) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: DateTimeOffset) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: DoubleType) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: FloatType) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: DecimalType) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: IntType) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: LongType) -> VoidType: ...
    
    def WriteWhitespace(self, ws: StringType) -> VoidType: ...
    
    def WriteWhitespaceAsync(self, ws: StringType) -> Task: ...
    
    def get_Settings(self) -> XmlWriterSettings: ...
    
    def get_WriteState(self) -> WriteState: ...
    
    def get_XmlLang(self) -> StringType: ...
    
    def get_XmlSpace(self) -> XmlSpace: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlWrappingWriter(XmlWriter, IDisposable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Settings(self) -> XmlWriterSettings: ...
    
    @property
    def WriteState(self) -> WriteState: ...
    
    @property
    def XmlLang(self) -> StringType: ...
    
    @property
    def XmlSpace(self) -> XmlSpace: ...
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    def Flush(self) -> VoidType: ...
    
    def FlushAsync(self) -> Task: ...
    
    def LookupPrefix(self, ns: StringType) -> StringType: ...
    
    def WriteBase64(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> VoidType: ...
    
    def WriteBase64Async(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> Task: ...
    
    def WriteCData(self, text: StringType) -> VoidType: ...
    
    def WriteCDataAsync(self, text: StringType) -> Task: ...
    
    def WriteCharEntity(self, ch: CharType) -> VoidType: ...
    
    def WriteCharEntityAsync(self, ch: CharType) -> Task: ...
    
    def WriteChars(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> VoidType: ...
    
    def WriteCharsAsync(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> Task: ...
    
    def WriteComment(self, text: StringType) -> VoidType: ...
    
    def WriteCommentAsync(self, text: StringType) -> Task: ...
    
    def WriteDocType(self, name: StringType, pubid: StringType, sysid: StringType, subset: StringType) -> VoidType: ...
    
    def WriteDocTypeAsync(self, name: StringType, pubid: StringType, sysid: StringType, subset: StringType) -> Task: ...
    
    def WriteEndAttribute(self) -> VoidType: ...
    
    def WriteEndDocument(self) -> VoidType: ...
    
    def WriteEndDocumentAsync(self) -> Task: ...
    
    def WriteEndElement(self) -> VoidType: ...
    
    def WriteEndElementAsync(self) -> Task: ...
    
    def WriteEntityRef(self, name: StringType) -> VoidType: ...
    
    def WriteEntityRefAsync(self, name: StringType) -> Task: ...
    
    def WriteFullEndElement(self) -> VoidType: ...
    
    def WriteFullEndElementAsync(self) -> Task: ...
    
    def WriteProcessingInstruction(self, name: StringType, text: StringType) -> VoidType: ...
    
    def WriteProcessingInstructionAsync(self, name: StringType, text: StringType) -> Task: ...
    
    @overload
    def WriteRaw(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> VoidType: ...
    
    @overload
    def WriteRaw(self, data: StringType) -> VoidType: ...
    
    @overload
    def WriteRawAsync(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> Task: ...
    
    @overload
    def WriteRawAsync(self, data: StringType) -> Task: ...
    
    @overload
    def WriteStartAttribute(self, prefix: StringType, localName: StringType, ns: StringType) -> VoidType: ...
    
    @overload
    def WriteStartDocument(self) -> VoidType: ...
    
    @overload
    def WriteStartDocument(self, standalone: BooleanType) -> VoidType: ...
    
    @overload
    def WriteStartDocumentAsync(self) -> Task: ...
    
    @overload
    def WriteStartDocumentAsync(self, standalone: BooleanType) -> Task: ...
    
    @overload
    def WriteStartElement(self, prefix: StringType, localName: StringType, ns: StringType) -> VoidType: ...
    
    def WriteStartElementAsync(self, prefix: StringType, localName: StringType, ns: StringType) -> Task: ...
    
    def WriteString(self, text: StringType) -> VoidType: ...
    
    def WriteStringAsync(self, text: StringType) -> Task: ...
    
    def WriteSurrogateCharEntity(self, lowChar: CharType, highChar: CharType) -> VoidType: ...
    
    def WriteSurrogateCharEntityAsync(self, lowChar: CharType, highChar: CharType) -> Task: ...
    
    @overload
    def WriteValue(self, value: ObjectType) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: StringType) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: BooleanType) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: DateTime) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: DateTimeOffset) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: DoubleType) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: FloatType) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: DecimalType) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: IntType) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: LongType) -> VoidType: ...
    
    def WriteWhitespace(self, ws: StringType) -> VoidType: ...
    
    def WriteWhitespaceAsync(self, ws: StringType) -> Task: ...
    
    def get_Settings(self) -> XmlWriterSettings: ...
    
    def get_WriteState(self) -> WriteState: ...
    
    def get_XmlLang(self) -> StringType: ...
    
    def get_XmlSpace(self) -> XmlSpace: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlWriter(ABC, ObjectType, IDisposable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Settings(self) -> XmlWriterSettings: ...
    
    @property
    def WriteState(self) -> WriteState: ...
    
    @property
    def XmlLang(self) -> StringType: ...
    
    @property
    def XmlSpace(self) -> XmlSpace: ...
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    @staticmethod
    @overload
    def Create(outputFileName: StringType) -> XmlWriter: ...
    
    @staticmethod
    @overload
    def Create(outputFileName: StringType, settings: XmlWriterSettings) -> XmlWriter: ...
    
    @staticmethod
    @overload
    def Create(output: Stream) -> XmlWriter: ...
    
    @staticmethod
    @overload
    def Create(output: Stream, settings: XmlWriterSettings) -> XmlWriter: ...
    
    @staticmethod
    @overload
    def Create(output: TextWriter) -> XmlWriter: ...
    
    @staticmethod
    @overload
    def Create(output: TextWriter, settings: XmlWriterSettings) -> XmlWriter: ...
    
    @staticmethod
    @overload
    def Create(output: StringBuilder) -> XmlWriter: ...
    
    @staticmethod
    @overload
    def Create(output: StringBuilder, settings: XmlWriterSettings) -> XmlWriter: ...
    
    @staticmethod
    @overload
    def Create(output: XmlWriter) -> XmlWriter: ...
    
    @staticmethod
    @overload
    def Create(output: XmlWriter, settings: XmlWriterSettings) -> XmlWriter: ...
    
    def Dispose(self) -> VoidType: ...
    
    def Flush(self) -> VoidType: ...
    
    def FlushAsync(self) -> Task: ...
    
    def LookupPrefix(self, ns: StringType) -> StringType: ...
    
    @overload
    def WriteAttributeString(self, localName: StringType, ns: StringType, value: StringType) -> VoidType: ...
    
    @overload
    def WriteAttributeString(self, localName: StringType, value: StringType) -> VoidType: ...
    
    @overload
    def WriteAttributeString(self, prefix: StringType, localName: StringType, ns: StringType, value: StringType) -> VoidType: ...
    
    def WriteAttributeStringAsync(self, prefix: StringType, localName: StringType, ns: StringType, value: StringType) -> Task: ...
    
    def WriteAttributes(self, reader: XmlReader, defattr: BooleanType) -> VoidType: ...
    
    def WriteAttributesAsync(self, reader: XmlReader, defattr: BooleanType) -> Task: ...
    
    def WriteBase64(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> VoidType: ...
    
    def WriteBase64Async(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> Task: ...
    
    def WriteBinHex(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> VoidType: ...
    
    def WriteBinHexAsync(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> Task: ...
    
    def WriteCData(self, text: StringType) -> VoidType: ...
    
    def WriteCDataAsync(self, text: StringType) -> Task: ...
    
    def WriteCharEntity(self, ch: CharType) -> VoidType: ...
    
    def WriteCharEntityAsync(self, ch: CharType) -> Task: ...
    
    def WriteChars(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> VoidType: ...
    
    def WriteCharsAsync(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> Task: ...
    
    def WriteComment(self, text: StringType) -> VoidType: ...
    
    def WriteCommentAsync(self, text: StringType) -> Task: ...
    
    def WriteDocType(self, name: StringType, pubid: StringType, sysid: StringType, subset: StringType) -> VoidType: ...
    
    def WriteDocTypeAsync(self, name: StringType, pubid: StringType, sysid: StringType, subset: StringType) -> Task: ...
    
    @overload
    def WriteElementString(self, localName: StringType, value: StringType) -> VoidType: ...
    
    @overload
    def WriteElementString(self, localName: StringType, ns: StringType, value: StringType) -> VoidType: ...
    
    @overload
    def WriteElementString(self, prefix: StringType, localName: StringType, ns: StringType, value: StringType) -> VoidType: ...
    
    def WriteElementStringAsync(self, prefix: StringType, localName: StringType, ns: StringType, value: StringType) -> Task: ...
    
    def WriteEndAttribute(self) -> VoidType: ...
    
    def WriteEndDocument(self) -> VoidType: ...
    
    def WriteEndDocumentAsync(self) -> Task: ...
    
    def WriteEndElement(self) -> VoidType: ...
    
    def WriteEndElementAsync(self) -> Task: ...
    
    def WriteEntityRef(self, name: StringType) -> VoidType: ...
    
    def WriteEntityRefAsync(self, name: StringType) -> Task: ...
    
    def WriteFullEndElement(self) -> VoidType: ...
    
    def WriteFullEndElementAsync(self) -> Task: ...
    
    def WriteName(self, name: StringType) -> VoidType: ...
    
    def WriteNameAsync(self, name: StringType) -> Task: ...
    
    def WriteNmToken(self, name: StringType) -> VoidType: ...
    
    def WriteNmTokenAsync(self, name: StringType) -> Task: ...
    
    @overload
    def WriteNode(self, navigator: XPathNavigator, defattr: BooleanType) -> VoidType: ...
    
    @overload
    def WriteNode(self, reader: XmlReader, defattr: BooleanType) -> VoidType: ...
    
    @overload
    def WriteNodeAsync(self, reader: XmlReader, defattr: BooleanType) -> Task: ...
    
    @overload
    def WriteNodeAsync(self, navigator: XPathNavigator, defattr: BooleanType) -> Task: ...
    
    def WriteProcessingInstruction(self, name: StringType, text: StringType) -> VoidType: ...
    
    def WriteProcessingInstructionAsync(self, name: StringType, text: StringType) -> Task: ...
    
    def WriteQualifiedName(self, localName: StringType, ns: StringType) -> VoidType: ...
    
    def WriteQualifiedNameAsync(self, localName: StringType, ns: StringType) -> Task: ...
    
    @overload
    def WriteRaw(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> VoidType: ...
    
    @overload
    def WriteRaw(self, data: StringType) -> VoidType: ...
    
    @overload
    def WriteRawAsync(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> Task: ...
    
    @overload
    def WriteRawAsync(self, data: StringType) -> Task: ...
    
    @overload
    def WriteStartAttribute(self, localName: StringType, ns: StringType) -> VoidType: ...
    
    @overload
    def WriteStartAttribute(self, localName: StringType) -> VoidType: ...
    
    @overload
    def WriteStartAttribute(self, prefix: StringType, localName: StringType, ns: StringType) -> VoidType: ...
    
    @overload
    def WriteStartDocument(self) -> VoidType: ...
    
    @overload
    def WriteStartDocument(self, standalone: BooleanType) -> VoidType: ...
    
    @overload
    def WriteStartDocumentAsync(self) -> Task: ...
    
    @overload
    def WriteStartDocumentAsync(self, standalone: BooleanType) -> Task: ...
    
    @overload
    def WriteStartElement(self, localName: StringType, ns: StringType) -> VoidType: ...
    
    @overload
    def WriteStartElement(self, localName: StringType) -> VoidType: ...
    
    @overload
    def WriteStartElement(self, prefix: StringType, localName: StringType, ns: StringType) -> VoidType: ...
    
    def WriteStartElementAsync(self, prefix: StringType, localName: StringType, ns: StringType) -> Task: ...
    
    def WriteString(self, text: StringType) -> VoidType: ...
    
    def WriteStringAsync(self, text: StringType) -> Task: ...
    
    def WriteSurrogateCharEntity(self, lowChar: CharType, highChar: CharType) -> VoidType: ...
    
    def WriteSurrogateCharEntityAsync(self, lowChar: CharType, highChar: CharType) -> Task: ...
    
    @overload
    def WriteValue(self, value: ObjectType) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: StringType) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: DateTime) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: DateTimeOffset) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: DoubleType) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: FloatType) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: DecimalType) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: IntType) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: LongType) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: BooleanType) -> VoidType: ...
    
    def WriteWhitespace(self, ws: StringType) -> VoidType: ...
    
    def WriteWhitespaceAsync(self, ws: StringType) -> Task: ...
    
    def get_Settings(self) -> XmlWriterSettings: ...
    
    def get_WriteState(self) -> WriteState: ...
    
    def get_XmlLang(self) -> StringType: ...
    
    def get_XmlSpace(self) -> XmlSpace: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlWriter(ABC, ObjectType, IDisposable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Settings(self) -> XmlWriterSettings: ...
    
    @property
    def WriteState(self) -> WriteState: ...
    
    @property
    def XmlLang(self) -> StringType: ...
    
    @property
    def XmlSpace(self) -> XmlSpace: ...
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    @staticmethod
    @overload
    def Create(outputFileName: StringType) -> XmlWriter: ...
    
    @staticmethod
    @overload
    def Create(outputFileName: StringType, settings: XmlWriterSettings) -> XmlWriter: ...
    
    @staticmethod
    @overload
    def Create(output: Stream) -> XmlWriter: ...
    
    @staticmethod
    @overload
    def Create(output: Stream, settings: XmlWriterSettings) -> XmlWriter: ...
    
    @staticmethod
    @overload
    def Create(output: TextWriter) -> XmlWriter: ...
    
    @staticmethod
    @overload
    def Create(output: TextWriter, settings: XmlWriterSettings) -> XmlWriter: ...
    
    @staticmethod
    @overload
    def Create(output: StringBuilder) -> XmlWriter: ...
    
    @staticmethod
    @overload
    def Create(output: StringBuilder, settings: XmlWriterSettings) -> XmlWriter: ...
    
    @staticmethod
    @overload
    def Create(output: XmlWriter) -> XmlWriter: ...
    
    @staticmethod
    @overload
    def Create(output: XmlWriter, settings: XmlWriterSettings) -> XmlWriter: ...
    
    def Dispose(self) -> VoidType: ...
    
    def Flush(self) -> VoidType: ...
    
    def FlushAsync(self) -> Task: ...
    
    def LookupPrefix(self, ns: StringType) -> StringType: ...
    
    @overload
    def WriteAttributeString(self, localName: StringType, ns: StringType, value: StringType) -> VoidType: ...
    
    @overload
    def WriteAttributeString(self, localName: StringType, value: StringType) -> VoidType: ...
    
    @overload
    def WriteAttributeString(self, prefix: StringType, localName: StringType, ns: StringType, value: StringType) -> VoidType: ...
    
    def WriteAttributeStringAsync(self, prefix: StringType, localName: StringType, ns: StringType, value: StringType) -> Task: ...
    
    def WriteAttributes(self, reader: XmlReader, defattr: BooleanType) -> VoidType: ...
    
    def WriteAttributesAsync(self, reader: XmlReader, defattr: BooleanType) -> Task: ...
    
    def WriteBase64(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> VoidType: ...
    
    def WriteBase64Async(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> Task: ...
    
    def WriteBinHex(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> VoidType: ...
    
    def WriteBinHexAsync(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> Task: ...
    
    def WriteCData(self, text: StringType) -> VoidType: ...
    
    def WriteCDataAsync(self, text: StringType) -> Task: ...
    
    def WriteCharEntity(self, ch: CharType) -> VoidType: ...
    
    def WriteCharEntityAsync(self, ch: CharType) -> Task: ...
    
    def WriteChars(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> VoidType: ...
    
    def WriteCharsAsync(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> Task: ...
    
    def WriteComment(self, text: StringType) -> VoidType: ...
    
    def WriteCommentAsync(self, text: StringType) -> Task: ...
    
    def WriteDocType(self, name: StringType, pubid: StringType, sysid: StringType, subset: StringType) -> VoidType: ...
    
    def WriteDocTypeAsync(self, name: StringType, pubid: StringType, sysid: StringType, subset: StringType) -> Task: ...
    
    @overload
    def WriteElementString(self, localName: StringType, value: StringType) -> VoidType: ...
    
    @overload
    def WriteElementString(self, localName: StringType, ns: StringType, value: StringType) -> VoidType: ...
    
    @overload
    def WriteElementString(self, prefix: StringType, localName: StringType, ns: StringType, value: StringType) -> VoidType: ...
    
    def WriteElementStringAsync(self, prefix: StringType, localName: StringType, ns: StringType, value: StringType) -> Task: ...
    
    def WriteEndAttribute(self) -> VoidType: ...
    
    def WriteEndDocument(self) -> VoidType: ...
    
    def WriteEndDocumentAsync(self) -> Task: ...
    
    def WriteEndElement(self) -> VoidType: ...
    
    def WriteEndElementAsync(self) -> Task: ...
    
    def WriteEntityRef(self, name: StringType) -> VoidType: ...
    
    def WriteEntityRefAsync(self, name: StringType) -> Task: ...
    
    def WriteFullEndElement(self) -> VoidType: ...
    
    def WriteFullEndElementAsync(self) -> Task: ...
    
    def WriteName(self, name: StringType) -> VoidType: ...
    
    def WriteNameAsync(self, name: StringType) -> Task: ...
    
    def WriteNmToken(self, name: StringType) -> VoidType: ...
    
    def WriteNmTokenAsync(self, name: StringType) -> Task: ...
    
    @overload
    def WriteNode(self, navigator: XPathNavigator, defattr: BooleanType) -> VoidType: ...
    
    @overload
    def WriteNode(self, reader: XmlReader, defattr: BooleanType) -> VoidType: ...
    
    @overload
    def WriteNodeAsync(self, reader: XmlReader, defattr: BooleanType) -> Task: ...
    
    @overload
    def WriteNodeAsync(self, navigator: XPathNavigator, defattr: BooleanType) -> Task: ...
    
    def WriteProcessingInstruction(self, name: StringType, text: StringType) -> VoidType: ...
    
    def WriteProcessingInstructionAsync(self, name: StringType, text: StringType) -> Task: ...
    
    def WriteQualifiedName(self, localName: StringType, ns: StringType) -> VoidType: ...
    
    def WriteQualifiedNameAsync(self, localName: StringType, ns: StringType) -> Task: ...
    
    @overload
    def WriteRaw(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> VoidType: ...
    
    @overload
    def WriteRaw(self, data: StringType) -> VoidType: ...
    
    @overload
    def WriteRawAsync(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> Task: ...
    
    @overload
    def WriteRawAsync(self, data: StringType) -> Task: ...
    
    @overload
    def WriteStartAttribute(self, localName: StringType, ns: StringType) -> VoidType: ...
    
    @overload
    def WriteStartAttribute(self, localName: StringType) -> VoidType: ...
    
    @overload
    def WriteStartAttribute(self, prefix: StringType, localName: StringType, ns: StringType) -> VoidType: ...
    
    @overload
    def WriteStartDocument(self) -> VoidType: ...
    
    @overload
    def WriteStartDocument(self, standalone: BooleanType) -> VoidType: ...
    
    @overload
    def WriteStartDocumentAsync(self) -> Task: ...
    
    @overload
    def WriteStartDocumentAsync(self, standalone: BooleanType) -> Task: ...
    
    @overload
    def WriteStartElement(self, localName: StringType, ns: StringType) -> VoidType: ...
    
    @overload
    def WriteStartElement(self, localName: StringType) -> VoidType: ...
    
    @overload
    def WriteStartElement(self, prefix: StringType, localName: StringType, ns: StringType) -> VoidType: ...
    
    def WriteStartElementAsync(self, prefix: StringType, localName: StringType, ns: StringType) -> Task: ...
    
    def WriteString(self, text: StringType) -> VoidType: ...
    
    def WriteStringAsync(self, text: StringType) -> Task: ...
    
    def WriteSurrogateCharEntity(self, lowChar: CharType, highChar: CharType) -> VoidType: ...
    
    def WriteSurrogateCharEntityAsync(self, lowChar: CharType, highChar: CharType) -> Task: ...
    
    @overload
    def WriteValue(self, value: ObjectType) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: StringType) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: DateTime) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: DateTimeOffset) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: DoubleType) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: FloatType) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: DecimalType) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: IntType) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: LongType) -> VoidType: ...
    
    @overload
    def WriteValue(self, value: BooleanType) -> VoidType: ...
    
    def WriteWhitespace(self, ws: StringType) -> VoidType: ...
    
    def WriteWhitespaceAsync(self, ws: StringType) -> Task: ...
    
    def get_Settings(self) -> XmlWriterSettings: ...
    
    def get_WriteState(self) -> WriteState: ...
    
    def get_XmlLang(self) -> StringType: ...
    
    def get_XmlSpace(self) -> XmlSpace: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlWriterSettings(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Async(self) -> BooleanType: ...
    
    @Async.setter
    def Async(self, value: BooleanType) -> None: ...
    
    @property
    def CheckCharacters(self) -> BooleanType: ...
    
    @CheckCharacters.setter
    def CheckCharacters(self, value: BooleanType) -> None: ...
    
    @property
    def CloseOutput(self) -> BooleanType: ...
    
    @CloseOutput.setter
    def CloseOutput(self, value: BooleanType) -> None: ...
    
    @property
    def ConformanceLevel(self) -> ConformanceLevel: ...
    
    @ConformanceLevel.setter
    def ConformanceLevel(self, value: ConformanceLevel) -> None: ...
    
    @property
    def DoNotEscapeUriAttributes(self) -> BooleanType: ...
    
    @DoNotEscapeUriAttributes.setter
    def DoNotEscapeUriAttributes(self, value: BooleanType) -> None: ...
    
    @property
    def Encoding(self) -> Encoding: ...
    
    @Encoding.setter
    def Encoding(self, value: Encoding) -> None: ...
    
    @property
    def Indent(self) -> BooleanType: ...
    
    @Indent.setter
    def Indent(self, value: BooleanType) -> None: ...
    
    @property
    def IndentChars(self) -> StringType: ...
    
    @IndentChars.setter
    def IndentChars(self, value: StringType) -> None: ...
    
    @property
    def NamespaceHandling(self) -> NamespaceHandling: ...
    
    @NamespaceHandling.setter
    def NamespaceHandling(self, value: NamespaceHandling) -> None: ...
    
    @property
    def NewLineChars(self) -> StringType: ...
    
    @NewLineChars.setter
    def NewLineChars(self, value: StringType) -> None: ...
    
    @property
    def NewLineHandling(self) -> NewLineHandling: ...
    
    @NewLineHandling.setter
    def NewLineHandling(self, value: NewLineHandling) -> None: ...
    
    @property
    def NewLineOnAttributes(self) -> BooleanType: ...
    
    @NewLineOnAttributes.setter
    def NewLineOnAttributes(self, value: BooleanType) -> None: ...
    
    @property
    def OmitXmlDeclaration(self) -> BooleanType: ...
    
    @OmitXmlDeclaration.setter
    def OmitXmlDeclaration(self, value: BooleanType) -> None: ...
    
    @property
    def OutputMethod(self) -> XmlOutputMethod: ...
    
    @property
    def WriteEndDocumentOnClose(self) -> BooleanType: ...
    
    @WriteEndDocumentOnClose.setter
    def WriteEndDocumentOnClose(self, value: BooleanType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XmlWriterSettings: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Async(self) -> BooleanType: ...
    
    def get_CheckCharacters(self) -> BooleanType: ...
    
    def get_CloseOutput(self) -> BooleanType: ...
    
    def get_ConformanceLevel(self) -> ConformanceLevel: ...
    
    def get_DoNotEscapeUriAttributes(self) -> BooleanType: ...
    
    def get_Encoding(self) -> Encoding: ...
    
    def get_Indent(self) -> BooleanType: ...
    
    def get_IndentChars(self) -> StringType: ...
    
    def get_NamespaceHandling(self) -> NamespaceHandling: ...
    
    def get_NewLineChars(self) -> StringType: ...
    
    def get_NewLineHandling(self) -> NewLineHandling: ...
    
    def get_NewLineOnAttributes(self) -> BooleanType: ...
    
    def get_OmitXmlDeclaration(self) -> BooleanType: ...
    
    def get_OutputMethod(self) -> XmlOutputMethod: ...
    
    def get_WriteEndDocumentOnClose(self) -> BooleanType: ...
    
    def set_Async(self, value: BooleanType) -> VoidType: ...
    
    def set_CheckCharacters(self, value: BooleanType) -> VoidType: ...
    
    def set_CloseOutput(self, value: BooleanType) -> VoidType: ...
    
    def set_ConformanceLevel(self, value: ConformanceLevel) -> VoidType: ...
    
    def set_DoNotEscapeUriAttributes(self, value: BooleanType) -> VoidType: ...
    
    def set_Encoding(self, value: Encoding) -> VoidType: ...
    
    def set_Indent(self, value: BooleanType) -> VoidType: ...
    
    def set_IndentChars(self, value: StringType) -> VoidType: ...
    
    def set_NamespaceHandling(self, value: NamespaceHandling) -> VoidType: ...
    
    def set_NewLineChars(self, value: StringType) -> VoidType: ...
    
    def set_NewLineHandling(self, value: NewLineHandling) -> VoidType: ...
    
    def set_NewLineOnAttributes(self, value: BooleanType) -> VoidType: ...
    
    def set_OmitXmlDeclaration(self, value: BooleanType) -> VoidType: ...
    
    def set_WriteEndDocumentOnClose(self, value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlWriterSettings(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Async(self) -> BooleanType: ...
    
    @Async.setter
    def Async(self, value: BooleanType) -> None: ...
    
    @property
    def CheckCharacters(self) -> BooleanType: ...
    
    @CheckCharacters.setter
    def CheckCharacters(self, value: BooleanType) -> None: ...
    
    @property
    def CloseOutput(self) -> BooleanType: ...
    
    @CloseOutput.setter
    def CloseOutput(self, value: BooleanType) -> None: ...
    
    @property
    def ConformanceLevel(self) -> ConformanceLevel: ...
    
    @ConformanceLevel.setter
    def ConformanceLevel(self, value: ConformanceLevel) -> None: ...
    
    @property
    def DoNotEscapeUriAttributes(self) -> BooleanType: ...
    
    @DoNotEscapeUriAttributes.setter
    def DoNotEscapeUriAttributes(self, value: BooleanType) -> None: ...
    
    @property
    def Encoding(self) -> Encoding: ...
    
    @Encoding.setter
    def Encoding(self, value: Encoding) -> None: ...
    
    @property
    def Indent(self) -> BooleanType: ...
    
    @Indent.setter
    def Indent(self, value: BooleanType) -> None: ...
    
    @property
    def IndentChars(self) -> StringType: ...
    
    @IndentChars.setter
    def IndentChars(self, value: StringType) -> None: ...
    
    @property
    def NamespaceHandling(self) -> NamespaceHandling: ...
    
    @NamespaceHandling.setter
    def NamespaceHandling(self, value: NamespaceHandling) -> None: ...
    
    @property
    def NewLineChars(self) -> StringType: ...
    
    @NewLineChars.setter
    def NewLineChars(self, value: StringType) -> None: ...
    
    @property
    def NewLineHandling(self) -> NewLineHandling: ...
    
    @NewLineHandling.setter
    def NewLineHandling(self, value: NewLineHandling) -> None: ...
    
    @property
    def NewLineOnAttributes(self) -> BooleanType: ...
    
    @NewLineOnAttributes.setter
    def NewLineOnAttributes(self, value: BooleanType) -> None: ...
    
    @property
    def OmitXmlDeclaration(self) -> BooleanType: ...
    
    @OmitXmlDeclaration.setter
    def OmitXmlDeclaration(self, value: BooleanType) -> None: ...
    
    @property
    def OutputMethod(self) -> XmlOutputMethod: ...
    
    @property
    def WriteEndDocumentOnClose(self) -> BooleanType: ...
    
    @WriteEndDocumentOnClose.setter
    def WriteEndDocumentOnClose(self, value: BooleanType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XmlWriterSettings: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Async(self) -> BooleanType: ...
    
    def get_CheckCharacters(self) -> BooleanType: ...
    
    def get_CloseOutput(self) -> BooleanType: ...
    
    def get_ConformanceLevel(self) -> ConformanceLevel: ...
    
    def get_DoNotEscapeUriAttributes(self) -> BooleanType: ...
    
    def get_Encoding(self) -> Encoding: ...
    
    def get_Indent(self) -> BooleanType: ...
    
    def get_IndentChars(self) -> StringType: ...
    
    def get_NamespaceHandling(self) -> NamespaceHandling: ...
    
    def get_NewLineChars(self) -> StringType: ...
    
    def get_NewLineHandling(self) -> NewLineHandling: ...
    
    def get_NewLineOnAttributes(self) -> BooleanType: ...
    
    def get_OmitXmlDeclaration(self) -> BooleanType: ...
    
    def get_OutputMethod(self) -> XmlOutputMethod: ...
    
    def get_WriteEndDocumentOnClose(self) -> BooleanType: ...
    
    def set_Async(self, value: BooleanType) -> VoidType: ...
    
    def set_CheckCharacters(self, value: BooleanType) -> VoidType: ...
    
    def set_CloseOutput(self, value: BooleanType) -> VoidType: ...
    
    def set_ConformanceLevel(self, value: ConformanceLevel) -> VoidType: ...
    
    def set_DoNotEscapeUriAttributes(self, value: BooleanType) -> VoidType: ...
    
    def set_Encoding(self, value: Encoding) -> VoidType: ...
    
    def set_Indent(self, value: BooleanType) -> VoidType: ...
    
    def set_IndentChars(self, value: StringType) -> VoidType: ...
    
    def set_NamespaceHandling(self, value: NamespaceHandling) -> VoidType: ...
    
    def set_NewLineChars(self, value: StringType) -> VoidType: ...
    
    def set_NewLineHandling(self, value: NewLineHandling) -> VoidType: ...
    
    def set_NewLineOnAttributes(self, value: BooleanType) -> VoidType: ...
    
    def set_OmitXmlDeclaration(self, value: BooleanType) -> VoidType: ...
    
    def set_WriteEndDocumentOnClose(self, value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlXapResolver(XmlResolver):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetEntity(self, absoluteUri: Uri, role: StringType, ofObjectToReturn: TypeType) -> ObjectType: ...
    
    @staticmethod
    def RegisterApplicationResourceStreamResolver(appStreamResolver: IApplicationResourceStreamResolver) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlXapResolver(XmlResolver):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetEntity(self, absoluteUri: Uri, role: StringType, ofObjectToReturn: TypeType) -> ObjectType: ...
    
    @staticmethod
    def RegisterApplicationResourceStreamResolver(appStreamResolver: IApplicationResourceStreamResolver) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XsdCachingReader(XmlReader, IDisposable, IXmlLineInfo):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def AttributeCount(self) -> IntType: ...
    
    @property
    def BaseURI(self) -> StringType: ...
    
    @property
    def Depth(self) -> IntType: ...
    
    @property
    def EOF(self) -> BooleanType: ...
    
    @property
    def HasValue(self) -> BooleanType: ...
    
    @property
    def IsDefault(self) -> BooleanType: ...
    
    @property
    def IsEmptyElement(self) -> BooleanType: ...
    
    def __getitem__(self, key: IntType) -> StringType: ...
    
    def __getitem__(self, key: StringType) -> StringType: ...
    
    def __getitem__(self, key: StringType) -> StringType: ...
    
    @property
    def LocalName(self) -> StringType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def NameTable(self) -> XmlNameTable: ...
    
    @property
    def NamespaceURI(self) -> StringType: ...
    
    @property
    def NodeType(self) -> XmlNodeType: ...
    
    @property
    def Prefix(self) -> StringType: ...
    
    @property
    def QuoteChar(self) -> CharType: ...
    
    @property
    def ReadState(self) -> ReadState: ...
    
    @property
    def Settings(self) -> XmlReaderSettings: ...
    
    @property
    def Value(self) -> StringType: ...
    
    @property
    def XmlLang(self) -> StringType: ...
    
    @property
    def XmlSpace(self) -> XmlSpace: ...
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    @overload
    def GetAttribute(self, name: StringType) -> StringType: ...
    
    @overload
    def GetAttribute(self, name: StringType, namespaceURI: StringType) -> StringType: ...
    
    @overload
    def GetAttribute(self, i: IntType) -> StringType: ...
    
    def GetValueAsync(self) -> Task[StringType]: ...
    
    def LookupNamespace(self, prefix: StringType) -> StringType: ...
    
    @overload
    def MoveToAttribute(self, name: StringType) -> BooleanType: ...
    
    @overload
    def MoveToAttribute(self, name: StringType, ns: StringType) -> BooleanType: ...
    
    @overload
    def MoveToAttribute(self, i: IntType) -> VoidType: ...
    
    def MoveToElement(self) -> BooleanType: ...
    
    def MoveToFirstAttribute(self) -> BooleanType: ...
    
    def MoveToNextAttribute(self) -> BooleanType: ...
    
    def Read(self) -> BooleanType: ...
    
    def ReadAsync(self) -> Task[BooleanType]: ...
    
    def ReadAttributeValue(self) -> BooleanType: ...
    
    def ResolveEntity(self) -> VoidType: ...
    
    def Skip(self) -> VoidType: ...
    
    def SkipAsync(self) -> Task: ...
    
    def get_AttributeCount(self) -> IntType: ...
    
    def get_BaseURI(self) -> StringType: ...
    
    def get_Depth(self) -> IntType: ...
    
    def get_EOF(self) -> BooleanType: ...
    
    def get_HasValue(self) -> BooleanType: ...
    
    def get_IsDefault(self) -> BooleanType: ...
    
    def get_IsEmptyElement(self) -> BooleanType: ...
    
    @overload
    def get_Item(self, i: IntType) -> StringType: ...
    
    @overload
    def get_Item(self, name: StringType) -> StringType: ...
    
    @overload
    def get_Item(self, name: StringType, namespaceURI: StringType) -> StringType: ...
    
    def get_LocalName(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_NameTable(self) -> XmlNameTable: ...
    
    def get_NamespaceURI(self) -> StringType: ...
    
    def get_NodeType(self) -> XmlNodeType: ...
    
    def get_Prefix(self) -> StringType: ...
    
    def get_QuoteChar(self) -> CharType: ...
    
    def get_ReadState(self) -> ReadState: ...
    
    def get_Settings(self) -> XmlReaderSettings: ...
    
    def get_Value(self) -> StringType: ...
    
    def get_XmlLang(self) -> StringType: ...
    
    def get_XmlSpace(self) -> XmlSpace: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XsdCachingReader(XmlReader, IDisposable, IXmlLineInfo):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def AttributeCount(self) -> IntType: ...
    
    @property
    def BaseURI(self) -> StringType: ...
    
    @property
    def Depth(self) -> IntType: ...
    
    @property
    def EOF(self) -> BooleanType: ...
    
    @property
    def HasValue(self) -> BooleanType: ...
    
    @property
    def IsDefault(self) -> BooleanType: ...
    
    @property
    def IsEmptyElement(self) -> BooleanType: ...
    
    def __getitem__(self, key: IntType) -> StringType: ...
    
    def __getitem__(self, key: StringType) -> StringType: ...
    
    def __getitem__(self, key: StringType) -> StringType: ...
    
    @property
    def LocalName(self) -> StringType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def NameTable(self) -> XmlNameTable: ...
    
    @property
    def NamespaceURI(self) -> StringType: ...
    
    @property
    def NodeType(self) -> XmlNodeType: ...
    
    @property
    def Prefix(self) -> StringType: ...
    
    @property
    def QuoteChar(self) -> CharType: ...
    
    @property
    def ReadState(self) -> ReadState: ...
    
    @property
    def Settings(self) -> XmlReaderSettings: ...
    
    @property
    def Value(self) -> StringType: ...
    
    @property
    def XmlLang(self) -> StringType: ...
    
    @property
    def XmlSpace(self) -> XmlSpace: ...
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    @overload
    def GetAttribute(self, name: StringType) -> StringType: ...
    
    @overload
    def GetAttribute(self, name: StringType, namespaceURI: StringType) -> StringType: ...
    
    @overload
    def GetAttribute(self, i: IntType) -> StringType: ...
    
    def GetValueAsync(self) -> Task[StringType]: ...
    
    def LookupNamespace(self, prefix: StringType) -> StringType: ...
    
    @overload
    def MoveToAttribute(self, name: StringType) -> BooleanType: ...
    
    @overload
    def MoveToAttribute(self, name: StringType, ns: StringType) -> BooleanType: ...
    
    @overload
    def MoveToAttribute(self, i: IntType) -> VoidType: ...
    
    def MoveToElement(self) -> BooleanType: ...
    
    def MoveToFirstAttribute(self) -> BooleanType: ...
    
    def MoveToNextAttribute(self) -> BooleanType: ...
    
    def Read(self) -> BooleanType: ...
    
    def ReadAsync(self) -> Task[BooleanType]: ...
    
    def ReadAttributeValue(self) -> BooleanType: ...
    
    def ResolveEntity(self) -> VoidType: ...
    
    def Skip(self) -> VoidType: ...
    
    def SkipAsync(self) -> Task: ...
    
    def get_AttributeCount(self) -> IntType: ...
    
    def get_BaseURI(self) -> StringType: ...
    
    def get_Depth(self) -> IntType: ...
    
    def get_EOF(self) -> BooleanType: ...
    
    def get_HasValue(self) -> BooleanType: ...
    
    def get_IsDefault(self) -> BooleanType: ...
    
    def get_IsEmptyElement(self) -> BooleanType: ...
    
    @overload
    def get_Item(self, i: IntType) -> StringType: ...
    
    @overload
    def get_Item(self, name: StringType) -> StringType: ...
    
    @overload
    def get_Item(self, name: StringType, namespaceURI: StringType) -> StringType: ...
    
    def get_LocalName(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_NameTable(self) -> XmlNameTable: ...
    
    def get_NamespaceURI(self) -> StringType: ...
    
    def get_NodeType(self) -> XmlNodeType: ...
    
    def get_Prefix(self) -> StringType: ...
    
    def get_QuoteChar(self) -> CharType: ...
    
    def get_ReadState(self) -> ReadState: ...
    
    def get_Settings(self) -> XmlReaderSettings: ...
    
    def get_Value(self) -> StringType: ...
    
    def get_XmlLang(self) -> StringType: ...
    
    def get_XmlSpace(self) -> XmlSpace: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XsdValidatingReader(XmlReader, IDisposable, IXmlSchemaInfo, IXmlLineInfo, IXmlNamespaceResolver):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def AttributeCount(self) -> IntType: ...
    
    @property
    def BaseURI(self) -> StringType: ...
    
    @property
    def CanReadBinaryContent(self) -> BooleanType: ...
    
    @property
    def Depth(self) -> IntType: ...
    
    @property
    def EOF(self) -> BooleanType: ...
    
    @property
    def HasValue(self) -> BooleanType: ...
    
    @property
    def IsDefault(self) -> BooleanType: ...
    
    @property
    def IsEmptyElement(self) -> BooleanType: ...
    
    @property
    def LineNumber(self) -> IntType: ...
    
    @property
    def LinePosition(self) -> IntType: ...
    
    @property
    def LocalName(self) -> StringType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def NameTable(self) -> XmlNameTable: ...
    
    @property
    def NamespaceURI(self) -> StringType: ...
    
    @property
    def NodeType(self) -> XmlNodeType: ...
    
    @property
    def Prefix(self) -> StringType: ...
    
    @property
    def QuoteChar(self) -> CharType: ...
    
    @property
    def ReadState(self) -> ReadState: ...
    
    @property
    def SchemaInfo(self) -> IXmlSchemaInfo: ...
    
    @property
    def Settings(self) -> XmlReaderSettings: ...
    
    @property
    def Value(self) -> StringType: ...
    
    @property
    def ValueType(self) -> TypeType: ...
    
    @property
    def XmlLang(self) -> StringType: ...
    
    @property
    def XmlSpace(self) -> XmlSpace: ...
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    @overload
    def GetAttribute(self, name: StringType) -> StringType: ...
    
    @overload
    def GetAttribute(self, name: StringType, namespaceURI: StringType) -> StringType: ...
    
    @overload
    def GetAttribute(self, i: IntType) -> StringType: ...
    
    def GetValueAsync(self) -> Task[StringType]: ...
    
    def HasLineInfo(self) -> BooleanType: ...
    
    def LookupNamespace(self, prefix: StringType) -> StringType: ...
    
    @overload
    def MoveToAttribute(self, name: StringType) -> BooleanType: ...
    
    @overload
    def MoveToAttribute(self, name: StringType, ns: StringType) -> BooleanType: ...
    
    @overload
    def MoveToAttribute(self, i: IntType) -> VoidType: ...
    
    def MoveToElement(self) -> BooleanType: ...
    
    def MoveToFirstAttribute(self) -> BooleanType: ...
    
    def MoveToNextAttribute(self) -> BooleanType: ...
    
    def Read(self) -> BooleanType: ...
    
    def ReadAsync(self) -> Task[BooleanType]: ...
    
    def ReadAttributeValue(self) -> BooleanType: ...
    
    def ReadContentAs(self, returnType: TypeType, namespaceResolver: IXmlNamespaceResolver) -> ObjectType: ...
    
    def ReadContentAsAsync(self, returnType: TypeType, namespaceResolver: IXmlNamespaceResolver) -> Task[ObjectType]: ...
    
    def ReadContentAsBase64(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadContentAsBase64Async(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> Task[IntType]: ...
    
    def ReadContentAsBinHex(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadContentAsBinHexAsync(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> Task[IntType]: ...
    
    def ReadContentAsBoolean(self) -> BooleanType: ...
    
    def ReadContentAsDateTime(self) -> DateTime: ...
    
    def ReadContentAsDecimal(self) -> DecimalType: ...
    
    def ReadContentAsDouble(self) -> DoubleType: ...
    
    def ReadContentAsFloat(self) -> FloatType: ...
    
    def ReadContentAsInt(self) -> IntType: ...
    
    def ReadContentAsLong(self) -> LongType: ...
    
    def ReadContentAsObject(self) -> ObjectType: ...
    
    def ReadContentAsObjectAsync(self) -> Task[ObjectType]: ...
    
    def ReadContentAsString(self) -> StringType: ...
    
    def ReadContentAsStringAsync(self) -> Task[StringType]: ...
    
    @overload
    def ReadElementContentAs(self, returnType: TypeType, namespaceResolver: IXmlNamespaceResolver) -> ObjectType: ...
    
    def ReadElementContentAsAsync(self, returnType: TypeType, namespaceResolver: IXmlNamespaceResolver) -> Task[ObjectType]: ...
    
    def ReadElementContentAsBase64(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadElementContentAsBase64Async(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> Task[IntType]: ...
    
    def ReadElementContentAsBinHex(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadElementContentAsBinHexAsync(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> Task[IntType]: ...
    
    @overload
    def ReadElementContentAsBoolean(self) -> BooleanType: ...
    
    @overload
    def ReadElementContentAsDateTime(self) -> DateTime: ...
    
    @overload
    def ReadElementContentAsDecimal(self) -> DecimalType: ...
    
    @overload
    def ReadElementContentAsDouble(self) -> DoubleType: ...
    
    @overload
    def ReadElementContentAsFloat(self) -> FloatType: ...
    
    @overload
    def ReadElementContentAsInt(self) -> IntType: ...
    
    @overload
    def ReadElementContentAsLong(self) -> LongType: ...
    
    @overload
    def ReadElementContentAsObject(self) -> ObjectType: ...
    
    def ReadElementContentAsObjectAsync(self) -> Task[ObjectType]: ...
    
    @overload
    def ReadElementContentAsString(self) -> StringType: ...
    
    def ReadElementContentAsStringAsync(self) -> Task[StringType]: ...
    
    def ResolveEntity(self) -> VoidType: ...
    
    def Skip(self) -> VoidType: ...
    
    def SkipAsync(self) -> Task: ...
    
    def get_AttributeCount(self) -> IntType: ...
    
    def get_BaseURI(self) -> StringType: ...
    
    def get_CanReadBinaryContent(self) -> BooleanType: ...
    
    def get_Depth(self) -> IntType: ...
    
    def get_EOF(self) -> BooleanType: ...
    
    def get_HasValue(self) -> BooleanType: ...
    
    def get_IsDefault(self) -> BooleanType: ...
    
    def get_IsEmptyElement(self) -> BooleanType: ...
    
    def get_LineNumber(self) -> IntType: ...
    
    def get_LinePosition(self) -> IntType: ...
    
    def get_LocalName(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_NameTable(self) -> XmlNameTable: ...
    
    def get_NamespaceURI(self) -> StringType: ...
    
    def get_NodeType(self) -> XmlNodeType: ...
    
    def get_Prefix(self) -> StringType: ...
    
    def get_QuoteChar(self) -> CharType: ...
    
    def get_ReadState(self) -> ReadState: ...
    
    def get_SchemaInfo(self) -> IXmlSchemaInfo: ...
    
    def get_Settings(self) -> XmlReaderSettings: ...
    
    def get_Value(self) -> StringType: ...
    
    def get_ValueType(self) -> TypeType: ...
    
    def get_XmlLang(self) -> StringType: ...
    
    def get_XmlSpace(self) -> XmlSpace: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XsdValidatingReader(XmlReader, IDisposable, IXmlSchemaInfo, IXmlLineInfo, IXmlNamespaceResolver):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def AttributeCount(self) -> IntType: ...
    
    @property
    def BaseURI(self) -> StringType: ...
    
    @property
    def CanReadBinaryContent(self) -> BooleanType: ...
    
    @property
    def Depth(self) -> IntType: ...
    
    @property
    def EOF(self) -> BooleanType: ...
    
    @property
    def HasValue(self) -> BooleanType: ...
    
    @property
    def IsDefault(self) -> BooleanType: ...
    
    @property
    def IsEmptyElement(self) -> BooleanType: ...
    
    @property
    def LineNumber(self) -> IntType: ...
    
    @property
    def LinePosition(self) -> IntType: ...
    
    @property
    def LocalName(self) -> StringType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def NameTable(self) -> XmlNameTable: ...
    
    @property
    def NamespaceURI(self) -> StringType: ...
    
    @property
    def NodeType(self) -> XmlNodeType: ...
    
    @property
    def Prefix(self) -> StringType: ...
    
    @property
    def QuoteChar(self) -> CharType: ...
    
    @property
    def ReadState(self) -> ReadState: ...
    
    @property
    def SchemaInfo(self) -> IXmlSchemaInfo: ...
    
    @property
    def Settings(self) -> XmlReaderSettings: ...
    
    @property
    def Value(self) -> StringType: ...
    
    @property
    def ValueType(self) -> TypeType: ...
    
    @property
    def XmlLang(self) -> StringType: ...
    
    @property
    def XmlSpace(self) -> XmlSpace: ...
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    @overload
    def GetAttribute(self, name: StringType) -> StringType: ...
    
    @overload
    def GetAttribute(self, name: StringType, namespaceURI: StringType) -> StringType: ...
    
    @overload
    def GetAttribute(self, i: IntType) -> StringType: ...
    
    def GetValueAsync(self) -> Task[StringType]: ...
    
    def HasLineInfo(self) -> BooleanType: ...
    
    def LookupNamespace(self, prefix: StringType) -> StringType: ...
    
    @overload
    def MoveToAttribute(self, name: StringType) -> BooleanType: ...
    
    @overload
    def MoveToAttribute(self, name: StringType, ns: StringType) -> BooleanType: ...
    
    @overload
    def MoveToAttribute(self, i: IntType) -> VoidType: ...
    
    def MoveToElement(self) -> BooleanType: ...
    
    def MoveToFirstAttribute(self) -> BooleanType: ...
    
    def MoveToNextAttribute(self) -> BooleanType: ...
    
    def Read(self) -> BooleanType: ...
    
    def ReadAsync(self) -> Task[BooleanType]: ...
    
    def ReadAttributeValue(self) -> BooleanType: ...
    
    def ReadContentAs(self, returnType: TypeType, namespaceResolver: IXmlNamespaceResolver) -> ObjectType: ...
    
    def ReadContentAsAsync(self, returnType: TypeType, namespaceResolver: IXmlNamespaceResolver) -> Task[ObjectType]: ...
    
    def ReadContentAsBase64(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadContentAsBase64Async(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> Task[IntType]: ...
    
    def ReadContentAsBinHex(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadContentAsBinHexAsync(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> Task[IntType]: ...
    
    def ReadContentAsBoolean(self) -> BooleanType: ...
    
    def ReadContentAsDateTime(self) -> DateTime: ...
    
    def ReadContentAsDecimal(self) -> DecimalType: ...
    
    def ReadContentAsDouble(self) -> DoubleType: ...
    
    def ReadContentAsFloat(self) -> FloatType: ...
    
    def ReadContentAsInt(self) -> IntType: ...
    
    def ReadContentAsLong(self) -> LongType: ...
    
    def ReadContentAsObject(self) -> ObjectType: ...
    
    def ReadContentAsObjectAsync(self) -> Task[ObjectType]: ...
    
    def ReadContentAsString(self) -> StringType: ...
    
    def ReadContentAsStringAsync(self) -> Task[StringType]: ...
    
    @overload
    def ReadElementContentAs(self, returnType: TypeType, namespaceResolver: IXmlNamespaceResolver) -> ObjectType: ...
    
    def ReadElementContentAsAsync(self, returnType: TypeType, namespaceResolver: IXmlNamespaceResolver) -> Task[ObjectType]: ...
    
    def ReadElementContentAsBase64(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadElementContentAsBase64Async(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> Task[IntType]: ...
    
    def ReadElementContentAsBinHex(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadElementContentAsBinHexAsync(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> Task[IntType]: ...
    
    @overload
    def ReadElementContentAsBoolean(self) -> BooleanType: ...
    
    @overload
    def ReadElementContentAsDateTime(self) -> DateTime: ...
    
    @overload
    def ReadElementContentAsDecimal(self) -> DecimalType: ...
    
    @overload
    def ReadElementContentAsDouble(self) -> DoubleType: ...
    
    @overload
    def ReadElementContentAsFloat(self) -> FloatType: ...
    
    @overload
    def ReadElementContentAsInt(self) -> IntType: ...
    
    @overload
    def ReadElementContentAsLong(self) -> LongType: ...
    
    @overload
    def ReadElementContentAsObject(self) -> ObjectType: ...
    
    def ReadElementContentAsObjectAsync(self) -> Task[ObjectType]: ...
    
    @overload
    def ReadElementContentAsString(self) -> StringType: ...
    
    def ReadElementContentAsStringAsync(self) -> Task[StringType]: ...
    
    def ResolveEntity(self) -> VoidType: ...
    
    def Skip(self) -> VoidType: ...
    
    def SkipAsync(self) -> Task: ...
    
    def get_AttributeCount(self) -> IntType: ...
    
    def get_BaseURI(self) -> StringType: ...
    
    def get_CanReadBinaryContent(self) -> BooleanType: ...
    
    def get_Depth(self) -> IntType: ...
    
    def get_EOF(self) -> BooleanType: ...
    
    def get_HasValue(self) -> BooleanType: ...
    
    def get_IsDefault(self) -> BooleanType: ...
    
    def get_IsEmptyElement(self) -> BooleanType: ...
    
    def get_LineNumber(self) -> IntType: ...
    
    def get_LinePosition(self) -> IntType: ...
    
    def get_LocalName(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_NameTable(self) -> XmlNameTable: ...
    
    def get_NamespaceURI(self) -> StringType: ...
    
    def get_NodeType(self) -> XmlNodeType: ...
    
    def get_Prefix(self) -> StringType: ...
    
    def get_QuoteChar(self) -> CharType: ...
    
    def get_ReadState(self) -> ReadState: ...
    
    def get_SchemaInfo(self) -> IXmlSchemaInfo: ...
    
    def get_Settings(self) -> XmlReaderSettings: ...
    
    def get_Value(self) -> StringType: ...
    
    def get_ValueType(self) -> TypeType: ...
    
    def get_XmlLang(self) -> StringType: ...
    
    def get_XmlSpace(self) -> XmlSpace: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# ---------- Structs ---------- #

class BinXmlSqlDecimal(ValueType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, data: ArrayType[ByteType], offset: IntType, trim: BooleanType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def IsPositive(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def ToDecimal(self) -> DecimalType: ...
    
    def ToString(self) -> StringType: ...
    
    def Write(self, strm: Stream) -> VoidType: ...
    
    def get_IsPositive(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class BinXmlSqlDecimal(ValueType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, data: ArrayType[ByteType], offset: IntType, trim: BooleanType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def IsPositive(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def ToDecimal(self) -> DecimalType: ...
    
    def ToString(self) -> StringType: ...
    
    def Write(self, strm: Stream) -> VoidType: ...
    
    def get_IsPositive(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class BinXmlSqlMoney(ValueType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, v: IntType): ...
    
    @overload
    def __init__(self, v: LongType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def ToDecimal(self) -> DecimalType: ...
    
    def ToString(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class BinXmlSqlMoney(ValueType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, v: IntType): ...
    
    @overload
    def __init__(self, v: LongType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def ToDecimal(self) -> DecimalType: ...
    
    def ToString(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DebuggerDisplayXmlNodeProxy(ValueType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, node: XmlNode): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def ToString(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DebuggerDisplayXmlNodeProxy(ValueType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, node: XmlNode): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def ToString(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class LineInfo(ValueType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, lineNo: IntType, linePos: IntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Set(self, lineNo: IntType, linePos: IntType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class LineInfo(ValueType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, lineNo: IntType, linePos: IntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Set(self, lineNo: IntType, linePos: IntType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlCharType(ValueType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def Instance() -> XmlCharType: ...
    
    # ---------- Methods ---------- #
    
    def IsCharData(self, ch: CharType) -> BooleanType: ...
    
    @staticmethod
    def IsDigit(ch: CharType) -> BooleanType: ...
    
    def IsExtender(self, ch: CharType) -> BooleanType: ...
    
    @staticmethod
    def IsHexDigit(ch: CharType) -> BooleanType: ...
    
    def IsLetter(self, ch: CharType) -> BooleanType: ...
    
    def IsNCNameCharXml4e(self, ch: CharType) -> BooleanType: ...
    
    def IsNCNameSingleChar(self, ch: CharType) -> BooleanType: ...
    
    def IsNameCharXml4e(self, ch: CharType) -> BooleanType: ...
    
    def IsNameSingleChar(self, ch: CharType) -> BooleanType: ...
    
    def IsPubidChar(self, ch: CharType) -> BooleanType: ...
    
    def IsStartNCNameCharXml4e(self, ch: CharType) -> BooleanType: ...
    
    def IsStartNCNameSingleChar(self, ch: CharType) -> BooleanType: ...
    
    def IsStartNameCharXml4e(self, ch: CharType) -> BooleanType: ...
    
    def IsStartNameSingleChar(self, ch: CharType) -> BooleanType: ...
    
    def IsWhiteSpace(self, ch: CharType) -> BooleanType: ...
    
    @staticmethod
    def get_Instance() -> XmlCharType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlCharType(ValueType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def Instance() -> XmlCharType: ...
    
    # ---------- Methods ---------- #
    
    def IsCharData(self, ch: CharType) -> BooleanType: ...
    
    @staticmethod
    def IsDigit(ch: CharType) -> BooleanType: ...
    
    def IsExtender(self, ch: CharType) -> BooleanType: ...
    
    @staticmethod
    def IsHexDigit(ch: CharType) -> BooleanType: ...
    
    def IsLetter(self, ch: CharType) -> BooleanType: ...
    
    def IsNCNameCharXml4e(self, ch: CharType) -> BooleanType: ...
    
    def IsNCNameSingleChar(self, ch: CharType) -> BooleanType: ...
    
    def IsNameCharXml4e(self, ch: CharType) -> BooleanType: ...
    
    def IsNameSingleChar(self, ch: CharType) -> BooleanType: ...
    
    def IsPubidChar(self, ch: CharType) -> BooleanType: ...
    
    def IsStartNCNameCharXml4e(self, ch: CharType) -> BooleanType: ...
    
    def IsStartNCNameSingleChar(self, ch: CharType) -> BooleanType: ...
    
    def IsStartNameCharXml4e(self, ch: CharType) -> BooleanType: ...
    
    def IsStartNameSingleChar(self, ch: CharType) -> BooleanType: ...
    
    def IsWhiteSpace(self, ch: CharType) -> BooleanType: ...
    
    @staticmethod
    def get_Instance() -> XmlCharType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# ---------- Interfaces ---------- #

class IApplicationResourceStreamResolver(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetApplicationResourceStream(self, relativeUri: Uri) -> Stream: ...
    
    # No Events


class IApplicationResourceStreamResolver(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetApplicationResourceStream(self, relativeUri: Uri) -> Stream: ...
    
    # No Events


class IDtdAttributeInfo(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def IsDeclaredInExternal(self) -> BooleanType: ...
    
    @property
    def IsNonCDataType(self) -> BooleanType: ...
    
    @property
    def IsXmlAttribute(self) -> BooleanType: ...
    
    @property
    def LineNumber(self) -> IntType: ...
    
    @property
    def LinePosition(self) -> IntType: ...
    
    @property
    def LocalName(self) -> StringType: ...
    
    @property
    def Prefix(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_IsDeclaredInExternal(self) -> BooleanType: ...
    
    def get_IsNonCDataType(self) -> BooleanType: ...
    
    def get_IsXmlAttribute(self) -> BooleanType: ...
    
    def get_LineNumber(self) -> IntType: ...
    
    def get_LinePosition(self) -> IntType: ...
    
    def get_LocalName(self) -> StringType: ...
    
    def get_Prefix(self) -> StringType: ...
    
    # No Events


class IDtdAttributeInfo(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def IsDeclaredInExternal(self) -> BooleanType: ...
    
    @property
    def IsNonCDataType(self) -> BooleanType: ...
    
    @property
    def IsXmlAttribute(self) -> BooleanType: ...
    
    @property
    def LineNumber(self) -> IntType: ...
    
    @property
    def LinePosition(self) -> IntType: ...
    
    @property
    def LocalName(self) -> StringType: ...
    
    @property
    def Prefix(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_IsDeclaredInExternal(self) -> BooleanType: ...
    
    def get_IsNonCDataType(self) -> BooleanType: ...
    
    def get_IsXmlAttribute(self) -> BooleanType: ...
    
    def get_LineNumber(self) -> IntType: ...
    
    def get_LinePosition(self) -> IntType: ...
    
    def get_LocalName(self) -> StringType: ...
    
    def get_Prefix(self) -> StringType: ...
    
    # No Events


class IDtdAttributeListInfo(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def HasNonCDataAttributes(self) -> BooleanType: ...
    
    @property
    def LocalName(self) -> StringType: ...
    
    @property
    def Prefix(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def LookupAttribute(self, prefix: StringType, localName: StringType) -> IDtdAttributeInfo: ...
    
    def LookupDefaultAttributes(self) -> IEnumerable[IDtdDefaultAttributeInfo]: ...
    
    def LookupIdAttribute(self) -> IDtdAttributeInfo: ...
    
    def get_HasNonCDataAttributes(self) -> BooleanType: ...
    
    def get_LocalName(self) -> StringType: ...
    
    def get_Prefix(self) -> StringType: ...
    
    # No Events


class IDtdAttributeListInfo(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def HasNonCDataAttributes(self) -> BooleanType: ...
    
    @property
    def LocalName(self) -> StringType: ...
    
    @property
    def Prefix(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def LookupAttribute(self, prefix: StringType, localName: StringType) -> IDtdAttributeInfo: ...
    
    def LookupDefaultAttributes(self) -> IEnumerable[IDtdDefaultAttributeInfo]: ...
    
    def LookupIdAttribute(self) -> IDtdAttributeInfo: ...
    
    def get_HasNonCDataAttributes(self) -> BooleanType: ...
    
    def get_LocalName(self) -> StringType: ...
    
    def get_Prefix(self) -> StringType: ...
    
    # No Events


class IDtdDefaultAttributeInfo(Protocol, IDtdAttributeInfo):
    # ---------- Properties ---------- #
    
    @property
    def DefaultValueExpanded(self) -> StringType: ...
    
    @property
    def DefaultValueTyped(self) -> ObjectType: ...
    
    @property
    def ValueLineNumber(self) -> IntType: ...
    
    @property
    def ValueLinePosition(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def get_DefaultValueExpanded(self) -> StringType: ...
    
    def get_DefaultValueTyped(self) -> ObjectType: ...
    
    def get_ValueLineNumber(self) -> IntType: ...
    
    def get_ValueLinePosition(self) -> IntType: ...
    
    # No Events


class IDtdDefaultAttributeInfo(Protocol, IDtdAttributeInfo):
    # ---------- Properties ---------- #
    
    @property
    def DefaultValueExpanded(self) -> StringType: ...
    
    @property
    def DefaultValueTyped(self) -> ObjectType: ...
    
    @property
    def ValueLineNumber(self) -> IntType: ...
    
    @property
    def ValueLinePosition(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def get_DefaultValueExpanded(self) -> StringType: ...
    
    def get_DefaultValueTyped(self) -> ObjectType: ...
    
    def get_ValueLineNumber(self) -> IntType: ...
    
    def get_ValueLinePosition(self) -> IntType: ...
    
    # No Events


class IDtdEntityInfo(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def BaseUriString(self) -> StringType: ...
    
    @property
    def DeclaredUriString(self) -> StringType: ...
    
    @property
    def IsDeclaredInExternal(self) -> BooleanType: ...
    
    @property
    def IsExternal(self) -> BooleanType: ...
    
    @property
    def IsParameterEntity(self) -> BooleanType: ...
    
    @property
    def IsUnparsedEntity(self) -> BooleanType: ...
    
    @property
    def LineNumber(self) -> IntType: ...
    
    @property
    def LinePosition(self) -> IntType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def PublicId(self) -> StringType: ...
    
    @property
    def SystemId(self) -> StringType: ...
    
    @property
    def Text(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_BaseUriString(self) -> StringType: ...
    
    def get_DeclaredUriString(self) -> StringType: ...
    
    def get_IsDeclaredInExternal(self) -> BooleanType: ...
    
    def get_IsExternal(self) -> BooleanType: ...
    
    def get_IsParameterEntity(self) -> BooleanType: ...
    
    def get_IsUnparsedEntity(self) -> BooleanType: ...
    
    def get_LineNumber(self) -> IntType: ...
    
    def get_LinePosition(self) -> IntType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_PublicId(self) -> StringType: ...
    
    def get_SystemId(self) -> StringType: ...
    
    def get_Text(self) -> StringType: ...
    
    # No Events


class IDtdEntityInfo(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def BaseUriString(self) -> StringType: ...
    
    @property
    def DeclaredUriString(self) -> StringType: ...
    
    @property
    def IsDeclaredInExternal(self) -> BooleanType: ...
    
    @property
    def IsExternal(self) -> BooleanType: ...
    
    @property
    def IsParameterEntity(self) -> BooleanType: ...
    
    @property
    def IsUnparsedEntity(self) -> BooleanType: ...
    
    @property
    def LineNumber(self) -> IntType: ...
    
    @property
    def LinePosition(self) -> IntType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def PublicId(self) -> StringType: ...
    
    @property
    def SystemId(self) -> StringType: ...
    
    @property
    def Text(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_BaseUriString(self) -> StringType: ...
    
    def get_DeclaredUriString(self) -> StringType: ...
    
    def get_IsDeclaredInExternal(self) -> BooleanType: ...
    
    def get_IsExternal(self) -> BooleanType: ...
    
    def get_IsParameterEntity(self) -> BooleanType: ...
    
    def get_IsUnparsedEntity(self) -> BooleanType: ...
    
    def get_LineNumber(self) -> IntType: ...
    
    def get_LinePosition(self) -> IntType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_PublicId(self) -> StringType: ...
    
    def get_SystemId(self) -> StringType: ...
    
    def get_Text(self) -> StringType: ...
    
    # No Events


class IDtdInfo(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def HasDefaultAttributes(self) -> BooleanType: ...
    
    @property
    def HasNonCDataAttributes(self) -> BooleanType: ...
    
    @property
    def InternalDtdSubset(self) -> StringType: ...
    
    @property
    def Name(self) -> XmlQualifiedName: ...
    
    # ---------- Methods ---------- #
    
    def GetAttributeLists(self) -> IEnumerable[IDtdAttributeListInfo]: ...
    
    def LookupAttributeList(self, prefix: StringType, localName: StringType) -> IDtdAttributeListInfo: ...
    
    def LookupEntity(self, name: StringType) -> IDtdEntityInfo: ...
    
    def get_HasDefaultAttributes(self) -> BooleanType: ...
    
    def get_HasNonCDataAttributes(self) -> BooleanType: ...
    
    def get_InternalDtdSubset(self) -> StringType: ...
    
    def get_Name(self) -> XmlQualifiedName: ...
    
    # No Events


class IDtdInfo(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def HasDefaultAttributes(self) -> BooleanType: ...
    
    @property
    def HasNonCDataAttributes(self) -> BooleanType: ...
    
    @property
    def InternalDtdSubset(self) -> StringType: ...
    
    @property
    def Name(self) -> XmlQualifiedName: ...
    
    # ---------- Methods ---------- #
    
    def GetAttributeLists(self) -> IEnumerable[IDtdAttributeListInfo]: ...
    
    def LookupAttributeList(self, prefix: StringType, localName: StringType) -> IDtdAttributeListInfo: ...
    
    def LookupEntity(self, name: StringType) -> IDtdEntityInfo: ...
    
    def get_HasDefaultAttributes(self) -> BooleanType: ...
    
    def get_HasNonCDataAttributes(self) -> BooleanType: ...
    
    def get_InternalDtdSubset(self) -> StringType: ...
    
    def get_Name(self) -> XmlQualifiedName: ...
    
    # No Events


class IDtdParser(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def ParseFreeFloatingDtd(self, baseUri: StringType, docTypeName: StringType, publicId: StringType, systemId: StringType, internalSubset: StringType, adapter: IDtdParserAdapter) -> IDtdInfo: ...
    
    def ParseFreeFloatingDtdAsync(self, baseUri: StringType, docTypeName: StringType, publicId: StringType, systemId: StringType, internalSubset: StringType, adapter: IDtdParserAdapter) -> Task[IDtdInfo]: ...
    
    def ParseInternalDtd(self, adapter: IDtdParserAdapter, saveInternalSubset: BooleanType) -> IDtdInfo: ...
    
    def ParseInternalDtdAsync(self, adapter: IDtdParserAdapter, saveInternalSubset: BooleanType) -> Task[IDtdInfo]: ...
    
    # No Events


class IDtdParser(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def ParseFreeFloatingDtd(self, baseUri: StringType, docTypeName: StringType, publicId: StringType, systemId: StringType, internalSubset: StringType, adapter: IDtdParserAdapter) -> IDtdInfo: ...
    
    def ParseFreeFloatingDtdAsync(self, baseUri: StringType, docTypeName: StringType, publicId: StringType, systemId: StringType, internalSubset: StringType, adapter: IDtdParserAdapter) -> Task[IDtdInfo]: ...
    
    def ParseInternalDtd(self, adapter: IDtdParserAdapter, saveInternalSubset: BooleanType) -> IDtdInfo: ...
    
    def ParseInternalDtdAsync(self, adapter: IDtdParserAdapter, saveInternalSubset: BooleanType) -> Task[IDtdInfo]: ...
    
    # No Events


class IDtdParserAdapter(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def BaseUri(self) -> Uri: ...
    
    @property
    def CurrentPosition(self) -> IntType: ...
    
    @CurrentPosition.setter
    def CurrentPosition(self, value: IntType) -> None: ...
    
    @property
    def EntityStackLength(self) -> IntType: ...
    
    @property
    def IsEntityEolNormalized(self) -> BooleanType: ...
    
    @property
    def IsEof(self) -> BooleanType: ...
    
    @property
    def LineNo(self) -> IntType: ...
    
    @property
    def LineStartPosition(self) -> IntType: ...
    
    @property
    def NameTable(self) -> XmlNameTable: ...
    
    @property
    def NamespaceResolver(self) -> IXmlNamespaceResolver: ...
    
    @property
    def ParsingBuffer(self) -> ArrayType[CharType]: ...
    
    @property
    def ParsingBufferLength(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def OnNewLine(self, pos: IntType) -> VoidType: ...
    
    def OnPublicId(self, publicId: StringType, keywordLineInfo: LineInfo, publicLiteralLineInfo: LineInfo) -> VoidType: ...
    
    def OnSystemId(self, systemId: StringType, keywordLineInfo: LineInfo, systemLiteralLineInfo: LineInfo) -> VoidType: ...
    
    def ParseComment(self, sb: StringBuilder) -> VoidType: ...
    
    def ParseCommentAsync(self, sb: StringBuilder) -> Task: ...
    
    def ParseNamedCharRef(self, expand: BooleanType, internalSubsetBuilder: StringBuilder) -> IntType: ...
    
    def ParseNamedCharRefAsync(self, expand: BooleanType, internalSubsetBuilder: StringBuilder) -> Task[IntType]: ...
    
    def ParseNumericCharRef(self, internalSubsetBuilder: StringBuilder) -> IntType: ...
    
    def ParseNumericCharRefAsync(self, internalSubsetBuilder: StringBuilder) -> Task[IntType]: ...
    
    def ParsePI(self, sb: StringBuilder) -> VoidType: ...
    
    def ParsePIAsync(self, sb: StringBuilder) -> Task: ...
    
    def PopEntity(self, oldEntity: IDtdEntityInfo, newEntityId: IntType) -> Tuple[BooleanType, IDtdEntityInfo, IntType]: ...
    
    def PushEntity(self, entity: IDtdEntityInfo, entityId: IntType) -> Tuple[BooleanType, IntType]: ...
    
    def PushEntityAsync(self, entity: IDtdEntityInfo) -> Task[Tuple[IntType, BooleanType]]: ...
    
    def PushExternalSubset(self, systemId: StringType, publicId: StringType) -> BooleanType: ...
    
    def PushExternalSubsetAsync(self, systemId: StringType, publicId: StringType) -> Task[BooleanType]: ...
    
    def PushInternalDtd(self, baseUri: StringType, internalDtd: StringType) -> VoidType: ...
    
    def ReadData(self) -> IntType: ...
    
    def ReadDataAsync(self) -> Task[IntType]: ...
    
    def Throw(self, e: Exception) -> VoidType: ...
    
    def get_BaseUri(self) -> Uri: ...
    
    def get_CurrentPosition(self) -> IntType: ...
    
    def get_EntityStackLength(self) -> IntType: ...
    
    def get_IsEntityEolNormalized(self) -> BooleanType: ...
    
    def get_IsEof(self) -> BooleanType: ...
    
    def get_LineNo(self) -> IntType: ...
    
    def get_LineStartPosition(self) -> IntType: ...
    
    def get_NameTable(self) -> XmlNameTable: ...
    
    def get_NamespaceResolver(self) -> IXmlNamespaceResolver: ...
    
    def get_ParsingBuffer(self) -> ArrayType[CharType]: ...
    
    def get_ParsingBufferLength(self) -> IntType: ...
    
    def set_CurrentPosition(self, value: IntType) -> VoidType: ...
    
    # No Events


class IDtdParserAdapter(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def BaseUri(self) -> Uri: ...
    
    @property
    def CurrentPosition(self) -> IntType: ...
    
    @CurrentPosition.setter
    def CurrentPosition(self, value: IntType) -> None: ...
    
    @property
    def EntityStackLength(self) -> IntType: ...
    
    @property
    def IsEntityEolNormalized(self) -> BooleanType: ...
    
    @property
    def IsEof(self) -> BooleanType: ...
    
    @property
    def LineNo(self) -> IntType: ...
    
    @property
    def LineStartPosition(self) -> IntType: ...
    
    @property
    def NameTable(self) -> XmlNameTable: ...
    
    @property
    def NamespaceResolver(self) -> IXmlNamespaceResolver: ...
    
    @property
    def ParsingBuffer(self) -> ArrayType[CharType]: ...
    
    @property
    def ParsingBufferLength(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def OnNewLine(self, pos: IntType) -> VoidType: ...
    
    def OnPublicId(self, publicId: StringType, keywordLineInfo: LineInfo, publicLiteralLineInfo: LineInfo) -> VoidType: ...
    
    def OnSystemId(self, systemId: StringType, keywordLineInfo: LineInfo, systemLiteralLineInfo: LineInfo) -> VoidType: ...
    
    def ParseComment(self, sb: StringBuilder) -> VoidType: ...
    
    def ParseCommentAsync(self, sb: StringBuilder) -> Task: ...
    
    def ParseNamedCharRef(self, expand: BooleanType, internalSubsetBuilder: StringBuilder) -> IntType: ...
    
    def ParseNamedCharRefAsync(self, expand: BooleanType, internalSubsetBuilder: StringBuilder) -> Task[IntType]: ...
    
    def ParseNumericCharRef(self, internalSubsetBuilder: StringBuilder) -> IntType: ...
    
    def ParseNumericCharRefAsync(self, internalSubsetBuilder: StringBuilder) -> Task[IntType]: ...
    
    def ParsePI(self, sb: StringBuilder) -> VoidType: ...
    
    def ParsePIAsync(self, sb: StringBuilder) -> Task: ...
    
    def PopEntity(self, oldEntity: IDtdEntityInfo, newEntityId: IntType) -> Tuple[BooleanType, IDtdEntityInfo, IntType]: ...
    
    def PushEntity(self, entity: IDtdEntityInfo, entityId: IntType) -> Tuple[BooleanType, IntType]: ...
    
    def PushEntityAsync(self, entity: IDtdEntityInfo) -> Task[Tuple[IntType, BooleanType]]: ...
    
    def PushExternalSubset(self, systemId: StringType, publicId: StringType) -> BooleanType: ...
    
    def PushExternalSubsetAsync(self, systemId: StringType, publicId: StringType) -> Task[BooleanType]: ...
    
    def PushInternalDtd(self, baseUri: StringType, internalDtd: StringType) -> VoidType: ...
    
    def ReadData(self) -> IntType: ...
    
    def ReadDataAsync(self) -> Task[IntType]: ...
    
    def Throw(self, e: Exception) -> VoidType: ...
    
    def get_BaseUri(self) -> Uri: ...
    
    def get_CurrentPosition(self) -> IntType: ...
    
    def get_EntityStackLength(self) -> IntType: ...
    
    def get_IsEntityEolNormalized(self) -> BooleanType: ...
    
    def get_IsEof(self) -> BooleanType: ...
    
    def get_LineNo(self) -> IntType: ...
    
    def get_LineStartPosition(self) -> IntType: ...
    
    def get_NameTable(self) -> XmlNameTable: ...
    
    def get_NamespaceResolver(self) -> IXmlNamespaceResolver: ...
    
    def get_ParsingBuffer(self) -> ArrayType[CharType]: ...
    
    def get_ParsingBufferLength(self) -> IntType: ...
    
    def set_CurrentPosition(self, value: IntType) -> VoidType: ...
    
    # No Events


class IDtdParserAdapterV1(Protocol, IDtdParserAdapterWithValidation, IDtdParserAdapter):
    # ---------- Properties ---------- #
    
    @property
    def Namespaces(self) -> BooleanType: ...
    
    @property
    def Normalization(self) -> BooleanType: ...
    
    @property
    def V1CompatibilityMode(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def get_Namespaces(self) -> BooleanType: ...
    
    def get_Normalization(self) -> BooleanType: ...
    
    def get_V1CompatibilityMode(self) -> BooleanType: ...
    
    # No Events


class IDtdParserAdapterV1(Protocol, IDtdParserAdapterWithValidation, IDtdParserAdapter):
    # ---------- Properties ---------- #
    
    @property
    def Namespaces(self) -> BooleanType: ...
    
    @property
    def Normalization(self) -> BooleanType: ...
    
    @property
    def V1CompatibilityMode(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def get_Namespaces(self) -> BooleanType: ...
    
    def get_Normalization(self) -> BooleanType: ...
    
    def get_V1CompatibilityMode(self) -> BooleanType: ...
    
    # No Events


class IDtdParserAdapterWithValidation(Protocol, IDtdParserAdapter):
    # ---------- Properties ---------- #
    
    @property
    def DtdValidation(self) -> BooleanType: ...
    
    @property
    def ValidationEventHandling(self) -> IValidationEventHandling: ...
    
    # ---------- Methods ---------- #
    
    def get_DtdValidation(self) -> BooleanType: ...
    
    def get_ValidationEventHandling(self) -> IValidationEventHandling: ...
    
    # No Events


class IDtdParserAdapterWithValidation(Protocol, IDtdParserAdapter):
    # ---------- Properties ---------- #
    
    @property
    def DtdValidation(self) -> BooleanType: ...
    
    @property
    def ValidationEventHandling(self) -> IValidationEventHandling: ...
    
    # ---------- Methods ---------- #
    
    def get_DtdValidation(self) -> BooleanType: ...
    
    def get_ValidationEventHandling(self) -> IValidationEventHandling: ...
    
    # No Events


class IHasXmlNode(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetNode(self) -> XmlNode: ...
    
    # No Events


class IHasXmlNode(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetNode(self) -> XmlNode: ...
    
    # No Events


class IRemovableWriter(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def OnRemoveWriterEvent(self) -> OnRemoveWriter: ...
    
    @OnRemoveWriterEvent.setter
    def OnRemoveWriterEvent(self, value: OnRemoveWriter) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_OnRemoveWriterEvent(self) -> OnRemoveWriter: ...
    
    def set_OnRemoveWriterEvent(self, value: OnRemoveWriter) -> VoidType: ...
    
    # No Events


class IRemovableWriter(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def OnRemoveWriterEvent(self) -> OnRemoveWriter: ...
    
    @OnRemoveWriterEvent.setter
    def OnRemoveWriterEvent(self, value: OnRemoveWriter) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_OnRemoveWriterEvent(self) -> OnRemoveWriter: ...
    
    def set_OnRemoveWriterEvent(self, value: OnRemoveWriter) -> VoidType: ...
    
    # No Events


class IValidationEventHandling(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def EventHandler(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def SendEvent(self, exception: Exception, severity: XmlSeverityType) -> VoidType: ...
    
    def get_EventHandler(self) -> ObjectType: ...
    
    # No Events


class IValidationEventHandling(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def EventHandler(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def SendEvent(self, exception: Exception, severity: XmlSeverityType) -> VoidType: ...
    
    def get_EventHandler(self) -> ObjectType: ...
    
    # No Events


class IXmlLineInfo(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def LineNumber(self) -> IntType: ...
    
    @property
    def LinePosition(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def HasLineInfo(self) -> BooleanType: ...
    
    def get_LineNumber(self) -> IntType: ...
    
    def get_LinePosition(self) -> IntType: ...
    
    # No Events


class IXmlLineInfo(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def LineNumber(self) -> IntType: ...
    
    @property
    def LinePosition(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def HasLineInfo(self) -> BooleanType: ...
    
    def get_LineNumber(self) -> IntType: ...
    
    def get_LinePosition(self) -> IntType: ...
    
    # No Events


class IXmlNamespaceResolver(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetNamespacesInScope(self, scope: XmlNamespaceScope) -> IDictionary[StringType, StringType]: ...
    
    def LookupNamespace(self, prefix: StringType) -> StringType: ...
    
    def LookupPrefix(self, namespaceName: StringType) -> StringType: ...
    
    # No Events


class IXmlNamespaceResolver(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetNamespacesInScope(self, scope: XmlNamespaceScope) -> IDictionary[StringType, StringType]: ...
    
    def LookupNamespace(self, prefix: StringType) -> StringType: ...
    
    def LookupPrefix(self, namespaceName: StringType) -> StringType: ...
    
    # No Events


# ---------- Enums ---------- #

class AttributeProperties(Enum):
    DEFAULT: UIntType = 0
    URI: UIntType = 1
    BOOLEAN: UIntType = 2
    NAME: UIntType = 4


class AttributeProperties(Enum):
    DEFAULT: UIntType = 0
    URI: UIntType = 1
    BOOLEAN: UIntType = 2
    NAME: UIntType = 4


class BinXmlToken(Enum):
    NotImpl: IntType = -2
    EOF: IntType = -1
    Error: IntType = 0
    SQL_SMALLINT: IntType = 1
    SQL_INT: IntType = 2
    SQL_REAL: IntType = 3
    SQL_FLOAT: IntType = 4
    SQL_MONEY: IntType = 5
    SQL_BIT: IntType = 6
    SQL_TINYINT: IntType = 7
    SQL_BIGINT: IntType = 8
    SQL_UUID: IntType = 9
    SQL_DECIMAL: IntType = 10
    SQL_NUMERIC: IntType = 11
    SQL_BINARY: IntType = 12
    SQL_CHAR: IntType = 13
    SQL_NCHAR: IntType = 14
    SQL_VARBINARY: IntType = 15
    SQL_VARCHAR: IntType = 16
    SQL_NVARCHAR: IntType = 17
    SQL_DATETIME: IntType = 18
    SQL_SMALLDATETIME: IntType = 19
    SQL_SMALLMONEY: IntType = 20
    SQL_TEXT: IntType = 22
    SQL_IMAGE: IntType = 23
    SQL_NTEXT: IntType = 24
    SQL_UDT: IntType = 27
    XSD_KATMAI_TIMEOFFSET: IntType = 122
    XSD_KATMAI_DATETIMEOFFSET: IntType = 123
    XSD_KATMAI_DATEOFFSET: IntType = 124
    XSD_KATMAI_TIME: IntType = 125
    XSD_KATMAI_DATETIME: IntType = 126
    XSD_KATMAI_DATE: IntType = 127
    XSD_TIME: IntType = 129
    XSD_DATETIME: IntType = 130
    XSD_DATE: IntType = 131
    XSD_BINHEX: IntType = 132
    XSD_BASE64: IntType = 133
    XSD_BOOLEAN: IntType = 134
    XSD_DECIMAL: IntType = 135
    XSD_BYTE: IntType = 136
    XSD_UNSIGNEDSHORT: IntType = 137
    XSD_UNSIGNEDINT: IntType = 138
    XSD_UNSIGNEDLONG: IntType = 139
    XSD_QNAME: IntType = 140
    NmFlush: IntType = 233
    Extn: IntType = 234
    EndNest: IntType = 235
    Nest: IntType = 236
    XmlText: IntType = 237
    QName: IntType = 239
    Name: IntType = 240
    EndCData: IntType = 241
    CData: IntType = 242
    Comment: IntType = 243
    PI: IntType = 244
    EndAttrs: IntType = 245
    Attr: IntType = 246
    EndElem: IntType = 247
    Element: IntType = 248
    Subset: IntType = 249
    Public: IntType = 250
    System: IntType = 251
    DocType: IntType = 252
    Encoding: IntType = 253
    XmlDecl: IntType = 254


class BinXmlToken(Enum):
    NotImpl: IntType = -2
    EOF: IntType = -1
    Error: IntType = 0
    SQL_SMALLINT: IntType = 1
    SQL_INT: IntType = 2
    SQL_REAL: IntType = 3
    SQL_FLOAT: IntType = 4
    SQL_MONEY: IntType = 5
    SQL_BIT: IntType = 6
    SQL_TINYINT: IntType = 7
    SQL_BIGINT: IntType = 8
    SQL_UUID: IntType = 9
    SQL_DECIMAL: IntType = 10
    SQL_NUMERIC: IntType = 11
    SQL_BINARY: IntType = 12
    SQL_CHAR: IntType = 13
    SQL_NCHAR: IntType = 14
    SQL_VARBINARY: IntType = 15
    SQL_VARCHAR: IntType = 16
    SQL_NVARCHAR: IntType = 17
    SQL_DATETIME: IntType = 18
    SQL_SMALLDATETIME: IntType = 19
    SQL_SMALLMONEY: IntType = 20
    SQL_TEXT: IntType = 22
    SQL_IMAGE: IntType = 23
    SQL_NTEXT: IntType = 24
    SQL_UDT: IntType = 27
    XSD_KATMAI_TIMEOFFSET: IntType = 122
    XSD_KATMAI_DATETIMEOFFSET: IntType = 123
    XSD_KATMAI_DATEOFFSET: IntType = 124
    XSD_KATMAI_TIME: IntType = 125
    XSD_KATMAI_DATETIME: IntType = 126
    XSD_KATMAI_DATE: IntType = 127
    XSD_TIME: IntType = 129
    XSD_DATETIME: IntType = 130
    XSD_DATE: IntType = 131
    XSD_BINHEX: IntType = 132
    XSD_BASE64: IntType = 133
    XSD_BOOLEAN: IntType = 134
    XSD_DECIMAL: IntType = 135
    XSD_BYTE: IntType = 136
    XSD_UNSIGNEDSHORT: IntType = 137
    XSD_UNSIGNEDINT: IntType = 138
    XSD_UNSIGNEDLONG: IntType = 139
    XSD_QNAME: IntType = 140
    NmFlush: IntType = 233
    Extn: IntType = 234
    EndNest: IntType = 235
    Nest: IntType = 236
    XmlText: IntType = 237
    QName: IntType = 239
    Name: IntType = 240
    EndCData: IntType = 241
    CData: IntType = 242
    Comment: IntType = 243
    PI: IntType = 244
    EndAttrs: IntType = 245
    Attr: IntType = 246
    EndElem: IntType = 247
    Element: IntType = 248
    Subset: IntType = 249
    Public: IntType = 250
    System: IntType = 251
    DocType: IntType = 252
    Encoding: IntType = 253
    XmlDecl: IntType = 254


class ConformanceLevel(Enum):
    Auto: IntType = 0
    Fragment: IntType = 1
    Document: IntType = 2


class ConformanceLevel(Enum):
    Auto: IntType = 0
    Fragment: IntType = 1
    Document: IntType = 2


class DocumentXmlWriterType(Enum):
    InsertSiblingAfter: IntType = 0
    InsertSiblingBefore: IntType = 1
    PrependChild: IntType = 2
    AppendChild: IntType = 3
    AppendAttribute: IntType = 4
    ReplaceToFollowingSibling: IntType = 5


class DocumentXmlWriterType(Enum):
    InsertSiblingAfter: IntType = 0
    InsertSiblingBefore: IntType = 1
    PrependChild: IntType = 2
    AppendChild: IntType = 3
    AppendAttribute: IntType = 4
    ReplaceToFollowingSibling: IntType = 5


class DtdProcessing(Enum):
    Prohibit: IntType = 0
    Ignore: IntType = 1
    Parse: IntType = 2


class DtdProcessing(Enum):
    Prohibit: IntType = 0
    Ignore: IntType = 1
    Parse: IntType = 2


class ElementProperties(Enum):
    DEFAULT: UIntType = 0
    URI_PARENT: UIntType = 1
    BOOL_PARENT: UIntType = 2
    NAME_PARENT: UIntType = 4
    EMPTY: UIntType = 8
    NO_ENTITIES: UIntType = 16
    HEAD: UIntType = 32
    BLOCK_WS: UIntType = 64
    HAS_NS: UIntType = 128


class ElementProperties(Enum):
    DEFAULT: UIntType = 0
    URI_PARENT: UIntType = 1
    BOOL_PARENT: UIntType = 2
    NAME_PARENT: UIntType = 4
    EMPTY: UIntType = 8
    NO_ENTITIES: UIntType = 16
    HEAD: UIntType = 32
    BLOCK_WS: UIntType = 64
    HAS_NS: UIntType = 128


class EntityHandling(Enum):
    ExpandEntities: IntType = 1
    ExpandCharEntities: IntType = 2


class EntityHandling(Enum):
    ExpandEntities: IntType = 1
    ExpandCharEntities: IntType = 2


class ExceptionType(Enum):
    ArgumentException: IntType = 0
    XmlException: IntType = 1


class ExceptionType(Enum):
    ArgumentException: IntType = 0
    XmlException: IntType = 1


class Formatting(Enum):
    #None: IntType = 0
    Indented: IntType = 1


class Formatting(Enum):
    #None: IntType = 0
    Indented: IntType = 1


class NamespaceHandling(Enum):
    Default: IntType = 0
    OmitDuplicates: IntType = 1


class NamespaceHandling(Enum):
    Default: IntType = 0
    OmitDuplicates: IntType = 1


class NewLineHandling(Enum):
    Replace: IntType = 0
    Entitize: IntType = 1
    #None: IntType = 2


class NewLineHandling(Enum):
    Replace: IntType = 0
    Entitize: IntType = 1
    #None: IntType = 2


class ReadState(Enum):
    Initial: IntType = 0
    Interactive: IntType = 1
    Error: IntType = 2
    EndOfFile: IntType = 3
    Closed: IntType = 4


class ReadState(Enum):
    Initial: IntType = 0
    Interactive: IntType = 1
    Error: IntType = 2
    EndOfFile: IntType = 3
    Closed: IntType = 4


class TernaryTreeByte(Enum):
    characterByte: IntType = 0
    leftTree: IntType = 1
    rightTree: IntType = 2
    data: IntType = 3


class TernaryTreeByte(Enum):
    characterByte: IntType = 0
    leftTree: IntType = 1
    rightTree: IntType = 2
    data: IntType = 3


class TriState(Enum):
    Unknown: IntType = -1
    #False: IntType = 0
    #True: IntType = 1


class TriState(Enum):
    Unknown: IntType = -1
    #False: IntType = 0
    #True: IntType = 1


class ValidationType(Enum):
    #None: IntType = 0
    Auto: IntType = 1
    DTD: IntType = 2
    XDR: IntType = 3
    Schema: IntType = 4


class ValidationType(Enum):
    #None: IntType = 0
    Auto: IntType = 1
    DTD: IntType = 2
    XDR: IntType = 3
    Schema: IntType = 4


class WhitespaceHandling(Enum):
    All: IntType = 0
    Significant: IntType = 1
    #None: IntType = 2


class WhitespaceHandling(Enum):
    All: IntType = 0
    Significant: IntType = 1
    #None: IntType = 2


class WriteState(Enum):
    Start: IntType = 0
    Prolog: IntType = 1
    Element: IntType = 2
    Attribute: IntType = 3
    Content: IntType = 4
    Closed: IntType = 5
    Error: IntType = 6


class WriteState(Enum):
    Start: IntType = 0
    Prolog: IntType = 1
    Element: IntType = 2
    Attribute: IntType = 3
    Content: IntType = 4
    Closed: IntType = 5
    Error: IntType = 6


class XmlDateTimeSerializationMode(Enum):
    Local: IntType = 0
    Utc: IntType = 1
    Unspecified: IntType = 2
    RoundtripKind: IntType = 3


class XmlDateTimeSerializationMode(Enum):
    Local: IntType = 0
    Utc: IntType = 1
    Unspecified: IntType = 2
    RoundtripKind: IntType = 3


class XmlNamespaceScope(Enum):
    All: IntType = 0
    ExcludeXml: IntType = 1
    Local: IntType = 2


class XmlNamespaceScope(Enum):
    All: IntType = 0
    ExcludeXml: IntType = 1
    Local: IntType = 2


class XmlNodeChangedAction(Enum):
    Insert: IntType = 0
    Remove: IntType = 1
    Change: IntType = 2


class XmlNodeChangedAction(Enum):
    Insert: IntType = 0
    Remove: IntType = 1
    Change: IntType = 2


class XmlNodeOrder(Enum):
    Before: IntType = 0
    After: IntType = 1
    Same: IntType = 2
    Unknown: IntType = 3


class XmlNodeOrder(Enum):
    Before: IntType = 0
    After: IntType = 1
    Same: IntType = 2
    Unknown: IntType = 3


class XmlNodeType(Enum):
    #None: IntType = 0
    Element: IntType = 1
    Attribute: IntType = 2
    Text: IntType = 3
    CDATA: IntType = 4
    EntityReference: IntType = 5
    Entity: IntType = 6
    ProcessingInstruction: IntType = 7
    Comment: IntType = 8
    Document: IntType = 9
    DocumentType: IntType = 10
    DocumentFragment: IntType = 11
    Notation: IntType = 12
    Whitespace: IntType = 13
    SignificantWhitespace: IntType = 14
    EndElement: IntType = 15
    EndEntity: IntType = 16
    XmlDeclaration: IntType = 17


class XmlNodeType(Enum):
    #None: IntType = 0
    Element: IntType = 1
    Attribute: IntType = 2
    Text: IntType = 3
    CDATA: IntType = 4
    EntityReference: IntType = 5
    Entity: IntType = 6
    ProcessingInstruction: IntType = 7
    Comment: IntType = 8
    Document: IntType = 9
    DocumentType: IntType = 10
    DocumentFragment: IntType = 11
    Notation: IntType = 12
    Whitespace: IntType = 13
    SignificantWhitespace: IntType = 14
    EndElement: IntType = 15
    EndEntity: IntType = 16
    XmlDeclaration: IntType = 17


class XmlOutputMethod(Enum):
    Xml: IntType = 0
    Html: IntType = 1
    Text: IntType = 2
    AutoDetect: IntType = 3


class XmlOutputMethod(Enum):
    Xml: IntType = 0
    Html: IntType = 1
    Text: IntType = 2
    AutoDetect: IntType = 3


class XmlSpace(Enum):
    #None: IntType = 0
    Default: IntType = 1
    Preserve: IntType = 2


class XmlSpace(Enum):
    #None: IntType = 0
    Default: IntType = 1
    Preserve: IntType = 2


class XmlStandalone(Enum):
    Omit: IntType = 0
    Yes: IntType = 1
    No: IntType = 2


class XmlStandalone(Enum):
    Omit: IntType = 0
    Yes: IntType = 1
    No: IntType = 2


class XmlTokenizedType(Enum):
    CDATA: IntType = 0
    ID: IntType = 1
    IDREF: IntType = 2
    IDREFS: IntType = 3
    ENTITY: IntType = 4
    ENTITIES: IntType = 5
    NMTOKEN: IntType = 6
    NMTOKENS: IntType = 7
    NOTATION: IntType = 8
    ENUMERATION: IntType = 9
    QName: IntType = 10
    NCName: IntType = 11
    #None: IntType = 12


class XmlTokenizedType(Enum):
    CDATA: IntType = 0
    ID: IntType = 1
    IDREF: IntType = 2
    IDREFS: IntType = 3
    ENTITY: IntType = 4
    ENTITIES: IntType = 5
    NMTOKEN: IntType = 6
    NMTOKENS: IntType = 7
    NOTATION: IntType = 8
    ENUMERATION: IntType = 9
    QName: IntType = 10
    NCName: IntType = 11
    #None: IntType = 12


# ---------- Delegates ---------- #

CachingEventHandler = Callable[[XsdCachingReader], VoidType]

CachingEventHandler = Callable[[XsdCachingReader], VoidType]

OnRemoveWriter = Callable[[XmlRawWriter], VoidType]

OnRemoveWriter = Callable[[XmlRawWriter], VoidType]

XmlNodeChangedEventHandler = Callable[[ObjectType, XmlNodeChangedEventArgs], VoidType]

XmlNodeChangedEventHandler = Callable[[ObjectType, XmlNodeChangedEventArgs], VoidType]

__all__ = [
    AsyncHelper,
    AttributePSVIInfo,
    Base64Decoder,
    Base64Encoder,
    BinHexDecoder,
    BinHexEncoder,
    BinXmlDateTime,
    BinaryCompatibility,
    BitStack,
    Bits,
    ByteStack,
    CachingEventHandler,
    CharEntityEncoderFallback,
    CharEntityEncoderFallbackBuffer,
    DiagnosticsSwitches,
    DocumentSchemaValidator,
    DocumentXPathNavigator,
    DocumentXPathNodeIterator_AllElemChildren,
    DocumentXPathNodeIterator_AllElemChildren_AndSelf,
    DocumentXPathNodeIterator_ElemChildren,
    DocumentXPathNodeIterator_ElemChildren_AndSelf,
    DocumentXPathNodeIterator_ElemChildren_AndSelf_NoLocalName,
    DocumentXPathNodeIterator_ElemChildren_NoLocalName,
    DocumentXPathNodeIterator_ElemDescendants,
    DocumentXPathNodeIterator_Empty,
    DocumentXmlWriter,
    DomNameTable,
    DtdParser,
    EmptyEnumerator,
    HWStack,
    HtmlEncodedRawTextWriter,
    HtmlEncodedRawTextWriterIndent,
    HtmlTernaryTree,
    HtmlUtf8RawTextWriter,
    HtmlUtf8RawTextWriterIndent,
    IncrementalReadCharsDecoder,
    IncrementalReadDecoder,
    IncrementalReadDummyDecoder,
    NameTable,
    OnRemoveWriter,
    OpenedHost,
    PositionInfo,
    QueryOutputWriter,
    QueryOutputWriterV1,
    ReadContentAsBinaryHelper,
    ReaderPositionInfo,
    Ref,
    Res,
    ResCategoryAttribute,
    ResDescriptionAttribute,
    SafeAsciiDecoder,
    SecureStringHasher,
    TernaryTreeReadOnly,
    TextEncodedRawTextWriter,
    TextUtf8RawTextWriter,
    UTF16Decoder,
    Ucs4Decoder,
    Ucs4Decoder1234,
    Ucs4Decoder2143,
    Ucs4Decoder3412,
    Ucs4Decoder4321,
    Ucs4Encoding,
    Ucs4Encoding1234,
    Ucs4Encoding2143,
    Ucs4Encoding3412,
    Ucs4Encoding4321,
    ValidateNames,
    ValidatingReaderNodeData,
    XPathNodeList,
    XmlAsyncCheckReader,
    XmlAsyncCheckReaderWithLineInfo,
    XmlAsyncCheckReaderWithLineInfoNS,
    XmlAsyncCheckReaderWithLineInfoNSSchema,
    XmlAsyncCheckReaderWithNS,
    XmlAsyncCheckWriter,
    XmlAttribute,
    XmlAttributeCollection,
    XmlAutoDetectWriter,
    XmlCDataSection,
    XmlCachedStream,
    XmlCharCheckingReader,
    XmlCharCheckingReaderWithNS,
    XmlCharCheckingWriter,
    XmlCharacterData,
    XmlChildEnumerator,
    XmlChildNodes,
    XmlComment,
    XmlComplianceUtil,
    XmlConvert,
    XmlDOMTextWriter,
    XmlDeclaration,
    XmlDocument,
    XmlDocumentFragment,
    XmlDocumentType,
    XmlDownloadManager,
    XmlElement,
    XmlElementList,
    XmlElementListEnumerator,
    XmlElementListListener,
    XmlEmptyElementListEnumerator,
    XmlEncodedRawTextWriter,
    XmlEncodedRawTextWriterIndent,
    XmlEntity,
    XmlEntityReference,
    XmlEventCache,
    XmlException,
    XmlImplementation,
    XmlLinkedNode,
    XmlLoader,
    XmlName,
    XmlNameEx,
    XmlNameTable,
    XmlNamedNodeMap,
    XmlNamespaceManager,
    XmlNode,
    XmlNodeChangedEventArgs,
    XmlNodeChangedEventHandler,
    XmlNodeList,
    XmlNodeListEnumerator,
    XmlNodeReader,
    XmlNodeReaderNavigator,
    XmlNotation,
    XmlNullResolver,
    XmlParserContext,
    XmlProcessingInstruction,
    XmlQualifiedName,
    XmlRawWriter,
    XmlRawWriterBase64Encoder,
    XmlReader,
    XmlReaderSettings,
    XmlRegisteredNonCachedStream,
    XmlReservedNs,
    XmlResolver,
    XmlSecureResolver,
    XmlSignificantWhitespace,
    XmlSqlBinaryReader,
    XmlSubtreeReader,
    XmlText,
    XmlTextEncoder,
    XmlTextReader,
    XmlTextReaderImpl,
    XmlTextWriter,
    XmlTextWriterBase64Encoder,
    XmlUnspecifiedAttribute,
    XmlUrlResolver,
    XmlUtf8RawTextWriter,
    XmlUtf8RawTextWriterIndent,
    XmlValidatingReader,
    XmlValidatingReaderImpl,
    XmlWellFormedWriter,
    XmlWhitespace,
    XmlWrappingReader,
    XmlWrappingWriter,
    XmlWriter,
    XmlWriterSettings,
    XmlXapResolver,
    XsdCachingReader,
    XsdValidatingReader,
    BinXmlSqlDecimal,
    BinXmlSqlMoney,
    DebuggerDisplayXmlNodeProxy,
    LineInfo,
    XmlCharType,
    IApplicationResourceStreamResolver,
    IDtdAttributeInfo,
    IDtdAttributeListInfo,
    IDtdDefaultAttributeInfo,
    IDtdEntityInfo,
    IDtdInfo,
    IDtdParser,
    IDtdParserAdapter,
    IDtdParserAdapterV1,
    IDtdParserAdapterWithValidation,
    IHasXmlNode,
    IRemovableWriter,
    IValidationEventHandling,
    IXmlLineInfo,
    IXmlNamespaceResolver,
    AttributeProperties,
    BinXmlToken,
    ConformanceLevel,
    DocumentXmlWriterType,
    DtdProcessing,
    ElementProperties,
    EntityHandling,
    ExceptionType,
    Formatting,
    NamespaceHandling,
    NewLineHandling,
    ReadState,
    TernaryTreeByte,
    TriState,
    ValidationType,
    WhitespaceHandling,
    WriteState,
    XmlDateTimeSerializationMode,
    XmlNamespaceScope,
    XmlNodeChangedAction,
    XmlNodeOrder,
    XmlNodeType,
    XmlOutputMethod,
    XmlSpace,
    XmlStandalone,
    XmlTokenizedType,
    CachingEventHandler,
    OnRemoveWriter,
    XmlNodeChangedEventHandler,
]
