from __future__ import annotations

from abc import ABC
from typing import List, Tuple, Union, overload

from System import ArgumentException, Array, Boolean, Byte, Char, Decimal, Double, Enum, Exception, ICloneable, IFormatProvider, Int16, Int32, Int64, Object, SByte, Single, String, UInt16, UInt32, UInt64, Void
from System.Runtime.InteropServices import _Exception
from System.Runtime.Serialization import IObjectReference, ISerializable, StreamingContext

# ---------- Types ---------- #

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
ByteType = Union[int, Byte]
CharType = Union[str, Char]
DecimalType = Union[float, Decimal]
DoubleType = Union[float, Double]
FloatType = Union[float, Single]
IntType = Union[int, Int32]
LongType = Union[int, Int64]
ObjectType = Object
SByteType = Union[int, SByte]
ShortType = Union[int, Int16]
StringType = Union[str, String]
UIntType = Union[int, UInt32]
ULongType = Union[int, UInt64]
UShortType = Union[int, UInt16]
VoidType = Union[None, Void]

# ---------- Classes ---------- #

class ASCIIEncoding(Encoding, ICloneable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def IsSingleByte(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def GetByteCount(self, chars: StringType) -> IntType: ...
    
    @overload
    def GetByteCount(self, chars: CharType, count: IntType) -> IntType: ...
    
    @overload
    def GetByteCount(self, chars: ArrayType[CharType], index: IntType, count: IntType) -> IntType: ...
    
    @overload
    def GetBytes(self, chars: StringType, charIndex: IntType, charCount: IntType, bytes: ArrayType[ByteType], byteIndex: IntType) -> IntType: ...
    
    @overload
    def GetBytes(self, chars: ArrayType[CharType], charIndex: IntType, charCount: IntType, bytes: ArrayType[ByteType], byteIndex: IntType) -> IntType: ...
    
    @overload
    def GetBytes(self, chars: CharType, charCount: IntType, bytes: ByteType, byteCount: IntType) -> IntType: ...
    
    @overload
    def GetCharCount(self, bytes: ByteType, count: IntType) -> IntType: ...
    
    @overload
    def GetCharCount(self, bytes: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    @overload
    def GetChars(self, bytes: ArrayType[ByteType], byteIndex: IntType, byteCount: IntType, chars: ArrayType[CharType], charIndex: IntType) -> IntType: ...
    
    @overload
    def GetChars(self, bytes: ByteType, byteCount: IntType, chars: CharType, charCount: IntType) -> IntType: ...
    
    def GetDecoder(self) -> Decoder: ...
    
    def GetEncoder(self) -> Encoder: ...
    
    def GetMaxByteCount(self, charCount: IntType) -> IntType: ...
    
    def GetMaxCharCount(self, byteCount: IntType) -> IntType: ...
    
    @overload
    def GetString(self, bytes: ArrayType[ByteType], byteIndex: IntType, byteCount: IntType) -> StringType: ...
    
    def get_IsSingleByte(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ASCIIEncoding(Encoding, ICloneable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def IsSingleByte(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def GetByteCount(self, chars: StringType) -> IntType: ...
    
    @overload
    def GetByteCount(self, chars: CharType, count: IntType) -> IntType: ...
    
    @overload
    def GetByteCount(self, chars: ArrayType[CharType], index: IntType, count: IntType) -> IntType: ...
    
    @overload
    def GetBytes(self, chars: StringType, charIndex: IntType, charCount: IntType, bytes: ArrayType[ByteType], byteIndex: IntType) -> IntType: ...
    
    @overload
    def GetBytes(self, chars: ArrayType[CharType], charIndex: IntType, charCount: IntType, bytes: ArrayType[ByteType], byteIndex: IntType) -> IntType: ...
    
    @overload
    def GetBytes(self, chars: CharType, charCount: IntType, bytes: ByteType, byteCount: IntType) -> IntType: ...
    
    @overload
    def GetCharCount(self, bytes: ByteType, count: IntType) -> IntType: ...
    
    @overload
    def GetCharCount(self, bytes: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    @overload
    def GetChars(self, bytes: ArrayType[ByteType], byteIndex: IntType, byteCount: IntType, chars: ArrayType[CharType], charIndex: IntType) -> IntType: ...
    
    @overload
    def GetChars(self, bytes: ByteType, byteCount: IntType, chars: CharType, charCount: IntType) -> IntType: ...
    
    def GetDecoder(self) -> Decoder: ...
    
    def GetEncoder(self) -> Encoder: ...
    
    def GetMaxByteCount(self, charCount: IntType) -> IntType: ...
    
    def GetMaxCharCount(self, byteCount: IntType) -> IntType: ...
    
    @overload
    def GetString(self, bytes: ArrayType[ByteType], byteIndex: IntType, byteCount: IntType) -> StringType: ...
    
    def get_IsSingleByte(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ASCIIEncoding(Encoding, ICloneable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def IsSingleByte(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def GetByteCount(self, chars: StringType) -> IntType: ...
    
    @overload
    def GetByteCount(self, chars: CharType, count: IntType) -> IntType: ...
    
    @overload
    def GetByteCount(self, chars: ArrayType[CharType], index: IntType, count: IntType) -> IntType: ...
    
    @overload
    def GetBytes(self, chars: StringType, charIndex: IntType, charCount: IntType, bytes: ArrayType[ByteType], byteIndex: IntType) -> IntType: ...
    
    @overload
    def GetBytes(self, chars: ArrayType[CharType], charIndex: IntType, charCount: IntType, bytes: ArrayType[ByteType], byteIndex: IntType) -> IntType: ...
    
    @overload
    def GetBytes(self, chars: CharType, charCount: IntType, bytes: ByteType, byteCount: IntType) -> IntType: ...
    
    @overload
    def GetCharCount(self, bytes: ByteType, count: IntType) -> IntType: ...
    
    @overload
    def GetCharCount(self, bytes: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    @overload
    def GetChars(self, bytes: ArrayType[ByteType], byteIndex: IntType, byteCount: IntType, chars: ArrayType[CharType], charIndex: IntType) -> IntType: ...
    
    @overload
    def GetChars(self, bytes: ByteType, byteCount: IntType, chars: CharType, charCount: IntType) -> IntType: ...
    
    def GetDecoder(self) -> Decoder: ...
    
    def GetEncoder(self) -> Encoder: ...
    
    def GetMaxByteCount(self, charCount: IntType) -> IntType: ...
    
    def GetMaxCharCount(self, byteCount: IntType) -> IntType: ...
    
    @overload
    def GetString(self, bytes: ArrayType[ByteType], byteIndex: IntType, byteCount: IntType) -> StringType: ...
    
    def get_IsSingleByte(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class BaseCodePageEncoding(ABC, EncodingNLS, ICloneable, ISerializable):
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


class BaseCodePageEncoding(ABC, EncodingNLS, ICloneable, ISerializable):
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


class BaseCodePageEncoding(ABC, EncodingNLS, ICloneable, ISerializable):
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


class CodePageEncoding(ObjectType, ISerializable, IObjectReference):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetRealObject(self, context: StreamingContext) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodePageEncoding(ObjectType, ISerializable, IObjectReference):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetRealObject(self, context: StreamingContext) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodePageEncoding(ObjectType, ISerializable, IObjectReference):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetRealObject(self, context: StreamingContext) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DBCSCodePageEncoding(BaseCodePageEncoding, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, codePage: IntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetDecoder(self) -> Decoder: ...
    
    def GetMaxByteCount(self, charCount: IntType) -> IntType: ...
    
    def GetMaxCharCount(self, byteCount: IntType) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DBCSCodePageEncoding(BaseCodePageEncoding, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, codePage: IntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetDecoder(self) -> Decoder: ...
    
    def GetMaxByteCount(self, charCount: IntType) -> IntType: ...
    
    def GetMaxCharCount(self, byteCount: IntType) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DBCSCodePageEncoding(BaseCodePageEncoding, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, codePage: IntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetDecoder(self) -> Decoder: ...
    
    def GetMaxByteCount(self, charCount: IntType) -> IntType: ...
    
    def GetMaxCharCount(self, byteCount: IntType) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Decoder(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Fallback(self) -> DecoderFallback: ...
    
    @Fallback.setter
    def Fallback(self, value: DecoderFallback) -> None: ...
    
    @property
    def FallbackBuffer(self) -> DecoderFallbackBuffer: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Convert(self, bytes: ArrayType[ByteType], byteIndex: IntType, byteCount: IntType, chars: ArrayType[CharType], charIndex: IntType, charCount: IntType, flush: BooleanType, bytesUsed: IntType, charsUsed: IntType, completed: BooleanType) -> Tuple[VoidType, IntType, IntType, BooleanType]: ...
    
    @overload
    def Convert(self, bytes: ByteType, byteCount: IntType, chars: CharType, charCount: IntType, flush: BooleanType, bytesUsed: IntType, charsUsed: IntType, completed: BooleanType) -> Tuple[VoidType, IntType, IntType, BooleanType]: ...
    
    @overload
    def GetCharCount(self, bytes: ArrayType[ByteType], index: IntType, count: IntType, flush: BooleanType) -> IntType: ...
    
    @overload
    def GetCharCount(self, bytes: ByteType, count: IntType, flush: BooleanType) -> IntType: ...
    
    @overload
    def GetCharCount(self, bytes: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    @overload
    def GetChars(self, bytes: ArrayType[ByteType], byteIndex: IntType, byteCount: IntType, chars: ArrayType[CharType], charIndex: IntType, flush: BooleanType) -> IntType: ...
    
    @overload
    def GetChars(self, bytes: ArrayType[ByteType], byteIndex: IntType, byteCount: IntType, chars: ArrayType[CharType], charIndex: IntType) -> IntType: ...
    
    @overload
    def GetChars(self, bytes: ByteType, byteCount: IntType, chars: CharType, charCount: IntType, flush: BooleanType) -> IntType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Fallback(self) -> DecoderFallback: ...
    
    def get_FallbackBuffer(self) -> DecoderFallbackBuffer: ...
    
    def set_Fallback(self, value: DecoderFallback) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Decoder(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Fallback(self) -> DecoderFallback: ...
    
    @Fallback.setter
    def Fallback(self, value: DecoderFallback) -> None: ...
    
    @property
    def FallbackBuffer(self) -> DecoderFallbackBuffer: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Convert(self, bytes: ArrayType[ByteType], byteIndex: IntType, byteCount: IntType, chars: ArrayType[CharType], charIndex: IntType, charCount: IntType, flush: BooleanType, bytesUsed: IntType, charsUsed: IntType, completed: BooleanType) -> Tuple[VoidType, IntType, IntType, BooleanType]: ...
    
    @overload
    def Convert(self, bytes: ByteType, byteCount: IntType, chars: CharType, charCount: IntType, flush: BooleanType, bytesUsed: IntType, charsUsed: IntType, completed: BooleanType) -> Tuple[VoidType, IntType, IntType, BooleanType]: ...
    
    @overload
    def GetCharCount(self, bytes: ArrayType[ByteType], index: IntType, count: IntType, flush: BooleanType) -> IntType: ...
    
    @overload
    def GetCharCount(self, bytes: ByteType, count: IntType, flush: BooleanType) -> IntType: ...
    
    @overload
    def GetCharCount(self, bytes: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    @overload
    def GetChars(self, bytes: ArrayType[ByteType], byteIndex: IntType, byteCount: IntType, chars: ArrayType[CharType], charIndex: IntType, flush: BooleanType) -> IntType: ...
    
    @overload
    def GetChars(self, bytes: ArrayType[ByteType], byteIndex: IntType, byteCount: IntType, chars: ArrayType[CharType], charIndex: IntType) -> IntType: ...
    
    @overload
    def GetChars(self, bytes: ByteType, byteCount: IntType, chars: CharType, charCount: IntType, flush: BooleanType) -> IntType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Fallback(self) -> DecoderFallback: ...
    
    def get_FallbackBuffer(self) -> DecoderFallbackBuffer: ...
    
    def set_Fallback(self, value: DecoderFallback) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Decoder(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Fallback(self) -> DecoderFallback: ...
    
    @Fallback.setter
    def Fallback(self, value: DecoderFallback) -> None: ...
    
    @property
    def FallbackBuffer(self) -> DecoderFallbackBuffer: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Convert(self, bytes: ArrayType[ByteType], byteIndex: IntType, byteCount: IntType, chars: ArrayType[CharType], charIndex: IntType, charCount: IntType, flush: BooleanType, bytesUsed: IntType, charsUsed: IntType, completed: BooleanType) -> Tuple[VoidType, IntType, IntType, BooleanType]: ...
    
    @overload
    def Convert(self, bytes: ByteType, byteCount: IntType, chars: CharType, charCount: IntType, flush: BooleanType, bytesUsed: IntType, charsUsed: IntType, completed: BooleanType) -> Tuple[VoidType, IntType, IntType, BooleanType]: ...
    
    @overload
    def GetCharCount(self, bytes: ArrayType[ByteType], index: IntType, count: IntType, flush: BooleanType) -> IntType: ...
    
    @overload
    def GetCharCount(self, bytes: ByteType, count: IntType, flush: BooleanType) -> IntType: ...
    
    @overload
    def GetCharCount(self, bytes: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    @overload
    def GetChars(self, bytes: ArrayType[ByteType], byteIndex: IntType, byteCount: IntType, chars: ArrayType[CharType], charIndex: IntType, flush: BooleanType) -> IntType: ...
    
    @overload
    def GetChars(self, bytes: ArrayType[ByteType], byteIndex: IntType, byteCount: IntType, chars: ArrayType[CharType], charIndex: IntType) -> IntType: ...
    
    @overload
    def GetChars(self, bytes: ByteType, byteCount: IntType, chars: CharType, charCount: IntType, flush: BooleanType) -> IntType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Fallback(self) -> DecoderFallback: ...
    
    def get_FallbackBuffer(self) -> DecoderFallbackBuffer: ...
    
    def set_Fallback(self, value: DecoderFallback) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DecoderExceptionFallback(DecoderFallback):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def MaxCharCount(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def CreateFallbackBuffer(self) -> DecoderFallbackBuffer: ...
    
    def Equals(self, value: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def get_MaxCharCount(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DecoderExceptionFallback(DecoderFallback):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def MaxCharCount(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def CreateFallbackBuffer(self) -> DecoderFallbackBuffer: ...
    
    def Equals(self, value: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def get_MaxCharCount(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DecoderExceptionFallback(DecoderFallback):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def MaxCharCount(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def CreateFallbackBuffer(self) -> DecoderFallbackBuffer: ...
    
    def Equals(self, value: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def get_MaxCharCount(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DecoderExceptionFallbackBuffer(DecoderFallbackBuffer):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Remaining(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def Fallback(self, bytesUnknown: ArrayType[ByteType], index: IntType) -> BooleanType: ...
    
    def GetNextChar(self) -> CharType: ...
    
    def MovePrevious(self) -> BooleanType: ...
    
    def get_Remaining(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DecoderExceptionFallbackBuffer(DecoderFallbackBuffer):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Remaining(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def Fallback(self, bytesUnknown: ArrayType[ByteType], index: IntType) -> BooleanType: ...
    
    def GetNextChar(self) -> CharType: ...
    
    def MovePrevious(self) -> BooleanType: ...
    
    def get_Remaining(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DecoderExceptionFallbackBuffer(DecoderFallbackBuffer):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Remaining(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def Fallback(self, bytesUnknown: ArrayType[ByteType], index: IntType) -> BooleanType: ...
    
    def GetNextChar(self) -> CharType: ...
    
    def MovePrevious(self) -> BooleanType: ...
    
    def get_Remaining(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DecoderFallback(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def ExceptionFallback() -> DecoderFallback: ...
    
    @property
    def MaxCharCount(self) -> IntType: ...
    
    @staticmethod
    @property
    def ReplacementFallback() -> DecoderFallback: ...
    
    # ---------- Methods ---------- #
    
    def CreateFallbackBuffer(self) -> DecoderFallbackBuffer: ...
    
    @staticmethod
    def get_ExceptionFallback() -> DecoderFallback: ...
    
    def get_MaxCharCount(self) -> IntType: ...
    
    @staticmethod
    def get_ReplacementFallback() -> DecoderFallback: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DecoderFallback(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def ExceptionFallback() -> DecoderFallback: ...
    
    @property
    def MaxCharCount(self) -> IntType: ...
    
    @staticmethod
    @property
    def ReplacementFallback() -> DecoderFallback: ...
    
    # ---------- Methods ---------- #
    
    def CreateFallbackBuffer(self) -> DecoderFallbackBuffer: ...
    
    @staticmethod
    def get_ExceptionFallback() -> DecoderFallback: ...
    
    def get_MaxCharCount(self) -> IntType: ...
    
    @staticmethod
    def get_ReplacementFallback() -> DecoderFallback: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DecoderFallback(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def ExceptionFallback() -> DecoderFallback: ...
    
    @property
    def MaxCharCount(self) -> IntType: ...
    
    @staticmethod
    @property
    def ReplacementFallback() -> DecoderFallback: ...
    
    # ---------- Methods ---------- #
    
    def CreateFallbackBuffer(self) -> DecoderFallbackBuffer: ...
    
    @staticmethod
    def get_ExceptionFallback() -> DecoderFallback: ...
    
    def get_MaxCharCount(self) -> IntType: ...
    
    @staticmethod
    def get_ReplacementFallback() -> DecoderFallback: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DecoderFallbackBuffer(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Remaining(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def Fallback(self, bytesUnknown: ArrayType[ByteType], index: IntType) -> BooleanType: ...
    
    def GetNextChar(self) -> CharType: ...
    
    def MovePrevious(self) -> BooleanType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Remaining(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DecoderFallbackBuffer(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Remaining(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def Fallback(self, bytesUnknown: ArrayType[ByteType], index: IntType) -> BooleanType: ...
    
    def GetNextChar(self) -> CharType: ...
    
    def MovePrevious(self) -> BooleanType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Remaining(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DecoderFallbackBuffer(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Remaining(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def Fallback(self, bytesUnknown: ArrayType[ByteType], index: IntType) -> BooleanType: ...
    
    def GetNextChar(self) -> CharType: ...
    
    def MovePrevious(self) -> BooleanType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Remaining(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DecoderFallbackException(ArgumentException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    @overload
    def __init__(self, message: StringType, bytesUnknown: ArrayType[ByteType], index: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def BytesUnknown(self) -> ArrayType[ByteType]: ...
    
    @property
    def Index(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def get_BytesUnknown(self) -> ArrayType[ByteType]: ...
    
    def get_Index(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DecoderFallbackException(ArgumentException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    @overload
    def __init__(self, message: StringType, bytesUnknown: ArrayType[ByteType], index: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def BytesUnknown(self) -> ArrayType[ByteType]: ...
    
    @property
    def Index(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def get_BytesUnknown(self) -> ArrayType[ByteType]: ...
    
    def get_Index(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DecoderFallbackException(ArgumentException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    @overload
    def __init__(self, message: StringType, bytesUnknown: ArrayType[ByteType], index: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def BytesUnknown(self) -> ArrayType[ByteType]: ...
    
    @property
    def Index(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def get_BytesUnknown(self) -> ArrayType[ByteType]: ...
    
    def get_Index(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DecoderNLS(Decoder, ISerializable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def MustFlush(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Convert(self, bytes: ArrayType[ByteType], byteIndex: IntType, byteCount: IntType, chars: ArrayType[CharType], charIndex: IntType, charCount: IntType, flush: BooleanType, bytesUsed: IntType, charsUsed: IntType, completed: BooleanType) -> Tuple[VoidType, IntType, IntType, BooleanType]: ...
    
    @overload
    def Convert(self, bytes: ByteType, byteCount: IntType, chars: CharType, charCount: IntType, flush: BooleanType, bytesUsed: IntType, charsUsed: IntType, completed: BooleanType) -> Tuple[VoidType, IntType, IntType, BooleanType]: ...
    
    @overload
    def GetCharCount(self, bytes: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    @overload
    def GetCharCount(self, bytes: ByteType, count: IntType, flush: BooleanType) -> IntType: ...
    
    @overload
    def GetCharCount(self, bytes: ArrayType[ByteType], index: IntType, count: IntType, flush: BooleanType) -> IntType: ...
    
    @overload
    def GetChars(self, bytes: ArrayType[ByteType], byteIndex: IntType, byteCount: IntType, chars: ArrayType[CharType], charIndex: IntType, flush: BooleanType) -> IntType: ...
    
    @overload
    def GetChars(self, bytes: ByteType, byteCount: IntType, chars: CharType, charCount: IntType, flush: BooleanType) -> IntType: ...
    
    @overload
    def GetChars(self, bytes: ArrayType[ByteType], byteIndex: IntType, byteCount: IntType, chars: ArrayType[CharType], charIndex: IntType) -> IntType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_MustFlush(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DecoderNLS(Decoder, ISerializable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def MustFlush(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Convert(self, bytes: ArrayType[ByteType], byteIndex: IntType, byteCount: IntType, chars: ArrayType[CharType], charIndex: IntType, charCount: IntType, flush: BooleanType, bytesUsed: IntType, charsUsed: IntType, completed: BooleanType) -> Tuple[VoidType, IntType, IntType, BooleanType]: ...
    
    @overload
    def Convert(self, bytes: ByteType, byteCount: IntType, chars: CharType, charCount: IntType, flush: BooleanType, bytesUsed: IntType, charsUsed: IntType, completed: BooleanType) -> Tuple[VoidType, IntType, IntType, BooleanType]: ...
    
    @overload
    def GetCharCount(self, bytes: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    @overload
    def GetCharCount(self, bytes: ByteType, count: IntType, flush: BooleanType) -> IntType: ...
    
    @overload
    def GetCharCount(self, bytes: ArrayType[ByteType], index: IntType, count: IntType, flush: BooleanType) -> IntType: ...
    
    @overload
    def GetChars(self, bytes: ArrayType[ByteType], byteIndex: IntType, byteCount: IntType, chars: ArrayType[CharType], charIndex: IntType, flush: BooleanType) -> IntType: ...
    
    @overload
    def GetChars(self, bytes: ByteType, byteCount: IntType, chars: CharType, charCount: IntType, flush: BooleanType) -> IntType: ...
    
    @overload
    def GetChars(self, bytes: ArrayType[ByteType], byteIndex: IntType, byteCount: IntType, chars: ArrayType[CharType], charIndex: IntType) -> IntType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_MustFlush(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DecoderNLS(Decoder, ISerializable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def MustFlush(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Convert(self, bytes: ArrayType[ByteType], byteIndex: IntType, byteCount: IntType, chars: ArrayType[CharType], charIndex: IntType, charCount: IntType, flush: BooleanType, bytesUsed: IntType, charsUsed: IntType, completed: BooleanType) -> Tuple[VoidType, IntType, IntType, BooleanType]: ...
    
    @overload
    def Convert(self, bytes: ByteType, byteCount: IntType, chars: CharType, charCount: IntType, flush: BooleanType, bytesUsed: IntType, charsUsed: IntType, completed: BooleanType) -> Tuple[VoidType, IntType, IntType, BooleanType]: ...
    
    @overload
    def GetCharCount(self, bytes: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    @overload
    def GetCharCount(self, bytes: ByteType, count: IntType, flush: BooleanType) -> IntType: ...
    
    @overload
    def GetCharCount(self, bytes: ArrayType[ByteType], index: IntType, count: IntType, flush: BooleanType) -> IntType: ...
    
    @overload
    def GetChars(self, bytes: ArrayType[ByteType], byteIndex: IntType, byteCount: IntType, chars: ArrayType[CharType], charIndex: IntType, flush: BooleanType) -> IntType: ...
    
    @overload
    def GetChars(self, bytes: ByteType, byteCount: IntType, chars: CharType, charCount: IntType, flush: BooleanType) -> IntType: ...
    
    @overload
    def GetChars(self, bytes: ArrayType[ByteType], byteIndex: IntType, byteCount: IntType, chars: ArrayType[CharType], charIndex: IntType) -> IntType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_MustFlush(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DecoderReplacementFallback(DecoderFallback):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, replacement: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def DefaultString(self) -> StringType: ...
    
    @property
    def MaxCharCount(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def CreateFallbackBuffer(self) -> DecoderFallbackBuffer: ...
    
    def Equals(self, value: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def get_DefaultString(self) -> StringType: ...
    
    def get_MaxCharCount(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DecoderReplacementFallback(DecoderFallback):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, replacement: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def DefaultString(self) -> StringType: ...
    
    @property
    def MaxCharCount(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def CreateFallbackBuffer(self) -> DecoderFallbackBuffer: ...
    
    def Equals(self, value: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def get_DefaultString(self) -> StringType: ...
    
    def get_MaxCharCount(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DecoderReplacementFallback(DecoderFallback):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, replacement: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def DefaultString(self) -> StringType: ...
    
    @property
    def MaxCharCount(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def CreateFallbackBuffer(self) -> DecoderFallbackBuffer: ...
    
    def Equals(self, value: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def get_DefaultString(self) -> StringType: ...
    
    def get_MaxCharCount(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DecoderReplacementFallbackBuffer(DecoderFallbackBuffer):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, fallback: DecoderReplacementFallback): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Remaining(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def Fallback(self, bytesUnknown: ArrayType[ByteType], index: IntType) -> BooleanType: ...
    
    def GetNextChar(self) -> CharType: ...
    
    def MovePrevious(self) -> BooleanType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Remaining(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DecoderReplacementFallbackBuffer(DecoderFallbackBuffer):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, fallback: DecoderReplacementFallback): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Remaining(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def Fallback(self, bytesUnknown: ArrayType[ByteType], index: IntType) -> BooleanType: ...
    
    def GetNextChar(self) -> CharType: ...
    
    def MovePrevious(self) -> BooleanType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Remaining(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DecoderReplacementFallbackBuffer(DecoderFallbackBuffer):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, fallback: DecoderReplacementFallback): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Remaining(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def Fallback(self, bytesUnknown: ArrayType[ByteType], index: IntType) -> BooleanType: ...
    
    def GetNextChar(self) -> CharType: ...
    
    def MovePrevious(self) -> BooleanType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Remaining(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EUCJPEncoding(DBCSCodePageEncoding, ICloneable, ISerializable):
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


class EUCJPEncoding(DBCSCodePageEncoding, ICloneable, ISerializable):
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


class EUCJPEncoding(DBCSCodePageEncoding, ICloneable, ISerializable):
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


class Encoder(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Fallback(self) -> EncoderFallback: ...
    
    @Fallback.setter
    def Fallback(self, value: EncoderFallback) -> None: ...
    
    @property
    def FallbackBuffer(self) -> EncoderFallbackBuffer: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Convert(self, chars: ArrayType[CharType], charIndex: IntType, charCount: IntType, bytes: ArrayType[ByteType], byteIndex: IntType, byteCount: IntType, flush: BooleanType, charsUsed: IntType, bytesUsed: IntType, completed: BooleanType) -> Tuple[VoidType, IntType, IntType, BooleanType]: ...
    
    @overload
    def Convert(self, chars: CharType, charCount: IntType, bytes: ByteType, byteCount: IntType, flush: BooleanType, charsUsed: IntType, bytesUsed: IntType, completed: BooleanType) -> Tuple[VoidType, IntType, IntType, BooleanType]: ...
    
    @overload
    def GetByteCount(self, chars: CharType, count: IntType, flush: BooleanType) -> IntType: ...
    
    @overload
    def GetByteCount(self, chars: ArrayType[CharType], index: IntType, count: IntType, flush: BooleanType) -> IntType: ...
    
    @overload
    def GetBytes(self, chars: ArrayType[CharType], charIndex: IntType, charCount: IntType, bytes: ArrayType[ByteType], byteIndex: IntType, flush: BooleanType) -> IntType: ...
    
    @overload
    def GetBytes(self, chars: CharType, charCount: IntType, bytes: ByteType, byteCount: IntType, flush: BooleanType) -> IntType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Fallback(self) -> EncoderFallback: ...
    
    def get_FallbackBuffer(self) -> EncoderFallbackBuffer: ...
    
    def set_Fallback(self, value: EncoderFallback) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Encoder(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Fallback(self) -> EncoderFallback: ...
    
    @Fallback.setter
    def Fallback(self, value: EncoderFallback) -> None: ...
    
    @property
    def FallbackBuffer(self) -> EncoderFallbackBuffer: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Convert(self, chars: ArrayType[CharType], charIndex: IntType, charCount: IntType, bytes: ArrayType[ByteType], byteIndex: IntType, byteCount: IntType, flush: BooleanType, charsUsed: IntType, bytesUsed: IntType, completed: BooleanType) -> Tuple[VoidType, IntType, IntType, BooleanType]: ...
    
    @overload
    def Convert(self, chars: CharType, charCount: IntType, bytes: ByteType, byteCount: IntType, flush: BooleanType, charsUsed: IntType, bytesUsed: IntType, completed: BooleanType) -> Tuple[VoidType, IntType, IntType, BooleanType]: ...
    
    @overload
    def GetByteCount(self, chars: CharType, count: IntType, flush: BooleanType) -> IntType: ...
    
    @overload
    def GetByteCount(self, chars: ArrayType[CharType], index: IntType, count: IntType, flush: BooleanType) -> IntType: ...
    
    @overload
    def GetBytes(self, chars: ArrayType[CharType], charIndex: IntType, charCount: IntType, bytes: ArrayType[ByteType], byteIndex: IntType, flush: BooleanType) -> IntType: ...
    
    @overload
    def GetBytes(self, chars: CharType, charCount: IntType, bytes: ByteType, byteCount: IntType, flush: BooleanType) -> IntType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Fallback(self) -> EncoderFallback: ...
    
    def get_FallbackBuffer(self) -> EncoderFallbackBuffer: ...
    
    def set_Fallback(self, value: EncoderFallback) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Encoder(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Fallback(self) -> EncoderFallback: ...
    
    @Fallback.setter
    def Fallback(self, value: EncoderFallback) -> None: ...
    
    @property
    def FallbackBuffer(self) -> EncoderFallbackBuffer: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Convert(self, chars: ArrayType[CharType], charIndex: IntType, charCount: IntType, bytes: ArrayType[ByteType], byteIndex: IntType, byteCount: IntType, flush: BooleanType, charsUsed: IntType, bytesUsed: IntType, completed: BooleanType) -> Tuple[VoidType, IntType, IntType, BooleanType]: ...
    
    @overload
    def Convert(self, chars: CharType, charCount: IntType, bytes: ByteType, byteCount: IntType, flush: BooleanType, charsUsed: IntType, bytesUsed: IntType, completed: BooleanType) -> Tuple[VoidType, IntType, IntType, BooleanType]: ...
    
    @overload
    def GetByteCount(self, chars: CharType, count: IntType, flush: BooleanType) -> IntType: ...
    
    @overload
    def GetByteCount(self, chars: ArrayType[CharType], index: IntType, count: IntType, flush: BooleanType) -> IntType: ...
    
    @overload
    def GetBytes(self, chars: ArrayType[CharType], charIndex: IntType, charCount: IntType, bytes: ArrayType[ByteType], byteIndex: IntType, flush: BooleanType) -> IntType: ...
    
    @overload
    def GetBytes(self, chars: CharType, charCount: IntType, bytes: ByteType, byteCount: IntType, flush: BooleanType) -> IntType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Fallback(self) -> EncoderFallback: ...
    
    def get_FallbackBuffer(self) -> EncoderFallbackBuffer: ...
    
    def set_Fallback(self, value: EncoderFallback) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EncoderExceptionFallback(EncoderFallback):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def MaxCharCount(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def CreateFallbackBuffer(self) -> EncoderFallbackBuffer: ...
    
    def Equals(self, value: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def get_MaxCharCount(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EncoderExceptionFallback(EncoderFallback):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def MaxCharCount(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def CreateFallbackBuffer(self) -> EncoderFallbackBuffer: ...
    
    def Equals(self, value: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def get_MaxCharCount(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EncoderExceptionFallback(EncoderFallback):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def MaxCharCount(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def CreateFallbackBuffer(self) -> EncoderFallbackBuffer: ...
    
    def Equals(self, value: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def get_MaxCharCount(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EncoderExceptionFallbackBuffer(EncoderFallbackBuffer):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
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
    
    def get_Remaining(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EncoderExceptionFallbackBuffer(EncoderFallbackBuffer):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
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
    
    def get_Remaining(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EncoderExceptionFallbackBuffer(EncoderFallbackBuffer):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
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
    
    def get_Remaining(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EncoderFallback(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def ExceptionFallback() -> EncoderFallback: ...
    
    @property
    def MaxCharCount(self) -> IntType: ...
    
    @staticmethod
    @property
    def ReplacementFallback() -> EncoderFallback: ...
    
    # ---------- Methods ---------- #
    
    def CreateFallbackBuffer(self) -> EncoderFallbackBuffer: ...
    
    @staticmethod
    def get_ExceptionFallback() -> EncoderFallback: ...
    
    def get_MaxCharCount(self) -> IntType: ...
    
    @staticmethod
    def get_ReplacementFallback() -> EncoderFallback: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EncoderFallback(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def ExceptionFallback() -> EncoderFallback: ...
    
    @property
    def MaxCharCount(self) -> IntType: ...
    
    @staticmethod
    @property
    def ReplacementFallback() -> EncoderFallback: ...
    
    # ---------- Methods ---------- #
    
    def CreateFallbackBuffer(self) -> EncoderFallbackBuffer: ...
    
    @staticmethod
    def get_ExceptionFallback() -> EncoderFallback: ...
    
    def get_MaxCharCount(self) -> IntType: ...
    
    @staticmethod
    def get_ReplacementFallback() -> EncoderFallback: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EncoderFallback(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def ExceptionFallback() -> EncoderFallback: ...
    
    @property
    def MaxCharCount(self) -> IntType: ...
    
    @staticmethod
    @property
    def ReplacementFallback() -> EncoderFallback: ...
    
    # ---------- Methods ---------- #
    
    def CreateFallbackBuffer(self) -> EncoderFallbackBuffer: ...
    
    @staticmethod
    def get_ExceptionFallback() -> EncoderFallback: ...
    
    def get_MaxCharCount(self) -> IntType: ...
    
    @staticmethod
    def get_ReplacementFallback() -> EncoderFallback: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EncoderFallbackBuffer(ABC, ObjectType):
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


class EncoderFallbackBuffer(ABC, ObjectType):
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


class EncoderFallbackBuffer(ABC, ObjectType):
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


class EncoderFallbackException(ArgumentException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CharUnknown(self) -> CharType: ...
    
    @property
    def CharUnknownHigh(self) -> CharType: ...
    
    @property
    def CharUnknownLow(self) -> CharType: ...
    
    @property
    def Index(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def IsUnknownSurrogate(self) -> BooleanType: ...
    
    def get_CharUnknown(self) -> CharType: ...
    
    def get_CharUnknownHigh(self) -> CharType: ...
    
    def get_CharUnknownLow(self) -> CharType: ...
    
    def get_Index(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EncoderFallbackException(ArgumentException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CharUnknown(self) -> CharType: ...
    
    @property
    def CharUnknownHigh(self) -> CharType: ...
    
    @property
    def CharUnknownLow(self) -> CharType: ...
    
    @property
    def Index(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def IsUnknownSurrogate(self) -> BooleanType: ...
    
    def get_CharUnknown(self) -> CharType: ...
    
    def get_CharUnknownHigh(self) -> CharType: ...
    
    def get_CharUnknownLow(self) -> CharType: ...
    
    def get_Index(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EncoderFallbackException(ArgumentException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CharUnknown(self) -> CharType: ...
    
    @property
    def CharUnknownHigh(self) -> CharType: ...
    
    @property
    def CharUnknownLow(self) -> CharType: ...
    
    @property
    def Index(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def IsUnknownSurrogate(self) -> BooleanType: ...
    
    def get_CharUnknown(self) -> CharType: ...
    
    def get_CharUnknownHigh(self) -> CharType: ...
    
    def get_CharUnknownLow(self) -> CharType: ...
    
    def get_Index(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EncoderNLS(Encoder, ISerializable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Encoding(self) -> Encoding: ...
    
    @property
    def MustFlush(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Convert(self, chars: ArrayType[CharType], charIndex: IntType, charCount: IntType, bytes: ArrayType[ByteType], byteIndex: IntType, byteCount: IntType, flush: BooleanType, charsUsed: IntType, bytesUsed: IntType, completed: BooleanType) -> Tuple[VoidType, IntType, IntType, BooleanType]: ...
    
    @overload
    def Convert(self, chars: CharType, charCount: IntType, bytes: ByteType, byteCount: IntType, flush: BooleanType, charsUsed: IntType, bytesUsed: IntType, completed: BooleanType) -> Tuple[VoidType, IntType, IntType, BooleanType]: ...
    
    @overload
    def GetByteCount(self, chars: CharType, count: IntType, flush: BooleanType) -> IntType: ...
    
    @overload
    def GetByteCount(self, chars: ArrayType[CharType], index: IntType, count: IntType, flush: BooleanType) -> IntType: ...
    
    @overload
    def GetBytes(self, chars: ArrayType[CharType], charIndex: IntType, charCount: IntType, bytes: ArrayType[ByteType], byteIndex: IntType, flush: BooleanType) -> IntType: ...
    
    @overload
    def GetBytes(self, chars: CharType, charCount: IntType, bytes: ByteType, byteCount: IntType, flush: BooleanType) -> IntType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Encoding(self) -> Encoding: ...
    
    def get_MustFlush(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EncoderNLS(Encoder, ISerializable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Encoding(self) -> Encoding: ...
    
    @property
    def MustFlush(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Convert(self, chars: ArrayType[CharType], charIndex: IntType, charCount: IntType, bytes: ArrayType[ByteType], byteIndex: IntType, byteCount: IntType, flush: BooleanType, charsUsed: IntType, bytesUsed: IntType, completed: BooleanType) -> Tuple[VoidType, IntType, IntType, BooleanType]: ...
    
    @overload
    def Convert(self, chars: CharType, charCount: IntType, bytes: ByteType, byteCount: IntType, flush: BooleanType, charsUsed: IntType, bytesUsed: IntType, completed: BooleanType) -> Tuple[VoidType, IntType, IntType, BooleanType]: ...
    
    @overload
    def GetByteCount(self, chars: CharType, count: IntType, flush: BooleanType) -> IntType: ...
    
    @overload
    def GetByteCount(self, chars: ArrayType[CharType], index: IntType, count: IntType, flush: BooleanType) -> IntType: ...
    
    @overload
    def GetBytes(self, chars: ArrayType[CharType], charIndex: IntType, charCount: IntType, bytes: ArrayType[ByteType], byteIndex: IntType, flush: BooleanType) -> IntType: ...
    
    @overload
    def GetBytes(self, chars: CharType, charCount: IntType, bytes: ByteType, byteCount: IntType, flush: BooleanType) -> IntType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Encoding(self) -> Encoding: ...
    
    def get_MustFlush(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EncoderNLS(Encoder, ISerializable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Encoding(self) -> Encoding: ...
    
    @property
    def MustFlush(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Convert(self, chars: ArrayType[CharType], charIndex: IntType, charCount: IntType, bytes: ArrayType[ByteType], byteIndex: IntType, byteCount: IntType, flush: BooleanType, charsUsed: IntType, bytesUsed: IntType, completed: BooleanType) -> Tuple[VoidType, IntType, IntType, BooleanType]: ...
    
    @overload
    def Convert(self, chars: CharType, charCount: IntType, bytes: ByteType, byteCount: IntType, flush: BooleanType, charsUsed: IntType, bytesUsed: IntType, completed: BooleanType) -> Tuple[VoidType, IntType, IntType, BooleanType]: ...
    
    @overload
    def GetByteCount(self, chars: CharType, count: IntType, flush: BooleanType) -> IntType: ...
    
    @overload
    def GetByteCount(self, chars: ArrayType[CharType], index: IntType, count: IntType, flush: BooleanType) -> IntType: ...
    
    @overload
    def GetBytes(self, chars: ArrayType[CharType], charIndex: IntType, charCount: IntType, bytes: ArrayType[ByteType], byteIndex: IntType, flush: BooleanType) -> IntType: ...
    
    @overload
    def GetBytes(self, chars: CharType, charCount: IntType, bytes: ByteType, byteCount: IntType, flush: BooleanType) -> IntType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Encoding(self) -> Encoding: ...
    
    def get_MustFlush(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EncoderReplacementFallback(EncoderFallback):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, replacement: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def DefaultString(self) -> StringType: ...
    
    @property
    def MaxCharCount(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def CreateFallbackBuffer(self) -> EncoderFallbackBuffer: ...
    
    def Equals(self, value: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def get_DefaultString(self) -> StringType: ...
    
    def get_MaxCharCount(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EncoderReplacementFallback(EncoderFallback):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, replacement: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def DefaultString(self) -> StringType: ...
    
    @property
    def MaxCharCount(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def CreateFallbackBuffer(self) -> EncoderFallbackBuffer: ...
    
    def Equals(self, value: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def get_DefaultString(self) -> StringType: ...
    
    def get_MaxCharCount(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EncoderReplacementFallback(EncoderFallback):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, replacement: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def DefaultString(self) -> StringType: ...
    
    @property
    def MaxCharCount(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def CreateFallbackBuffer(self) -> EncoderFallbackBuffer: ...
    
    def Equals(self, value: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def get_DefaultString(self) -> StringType: ...
    
    def get_MaxCharCount(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EncoderReplacementFallbackBuffer(EncoderFallbackBuffer):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, fallback: EncoderReplacementFallback): ...
    
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


class EncoderReplacementFallbackBuffer(EncoderFallbackBuffer):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, fallback: EncoderReplacementFallback): ...
    
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


class EncoderReplacementFallbackBuffer(EncoderFallbackBuffer):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, fallback: EncoderReplacementFallback): ...
    
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


class Encoding(ABC, ObjectType, ICloneable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def ASCII() -> Encoding: ...
    
    @staticmethod
    @property
    def BigEndianUnicode() -> Encoding: ...
    
    @property
    def BodyName(self) -> StringType: ...
    
    @property
    def CodePage(self) -> IntType: ...
    
    @property
    def DecoderFallback(self) -> DecoderFallback: ...
    
    @DecoderFallback.setter
    def DecoderFallback(self, value: DecoderFallback) -> None: ...
    
    @staticmethod
    @property
    def Default() -> Encoding: ...
    
    @property
    def EncoderFallback(self) -> EncoderFallback: ...
    
    @EncoderFallback.setter
    def EncoderFallback(self, value: EncoderFallback) -> None: ...
    
    @property
    def EncodingName(self) -> StringType: ...
    
    @property
    def HeaderName(self) -> StringType: ...
    
    @property
    def IsBrowserDisplay(self) -> BooleanType: ...
    
    @property
    def IsBrowserSave(self) -> BooleanType: ...
    
    @property
    def IsMailNewsDisplay(self) -> BooleanType: ...
    
    @property
    def IsMailNewsSave(self) -> BooleanType: ...
    
    @property
    def IsReadOnly(self) -> BooleanType: ...
    
    @property
    def IsSingleByte(self) -> BooleanType: ...
    
    @staticmethod
    @property
    def UTF32() -> Encoding: ...
    
    @staticmethod
    @property
    def UTF7() -> Encoding: ...
    
    @staticmethod
    @property
    def UTF8() -> Encoding: ...
    
    @staticmethod
    @property
    def Unicode() -> Encoding: ...
    
    @property
    def WebName(self) -> StringType: ...
    
    @property
    def WindowsCodePage(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> ObjectType: ...
    
    @staticmethod
    @overload
    def Convert(srcEncoding: Encoding, dstEncoding: Encoding, bytes: ArrayType[ByteType]) -> ArrayType[ByteType]: ...
    
    @staticmethod
    @overload
    def Convert(srcEncoding: Encoding, dstEncoding: Encoding, bytes: ArrayType[ByteType], index: IntType, count: IntType) -> ArrayType[ByteType]: ...
    
    def Equals(self, value: ObjectType) -> BooleanType: ...
    
    @overload
    def GetByteCount(self, chars: ArrayType[CharType]) -> IntType: ...
    
    @overload
    def GetByteCount(self, s: StringType) -> IntType: ...
    
    @overload
    def GetByteCount(self, chars: CharType, count: IntType) -> IntType: ...
    
    @overload
    def GetByteCount(self, chars: ArrayType[CharType], index: IntType, count: IntType) -> IntType: ...
    
    @overload
    def GetBytes(self, chars: ArrayType[CharType]) -> ArrayType[ByteType]: ...
    
    @overload
    def GetBytes(self, chars: ArrayType[CharType], index: IntType, count: IntType) -> ArrayType[ByteType]: ...
    
    @overload
    def GetBytes(self, s: StringType) -> ArrayType[ByteType]: ...
    
    @overload
    def GetBytes(self, s: StringType, charIndex: IntType, charCount: IntType, bytes: ArrayType[ByteType], byteIndex: IntType) -> IntType: ...
    
    @overload
    def GetBytes(self, chars: ArrayType[CharType], charIndex: IntType, charCount: IntType, bytes: ArrayType[ByteType], byteIndex: IntType) -> IntType: ...
    
    @overload
    def GetBytes(self, chars: CharType, charCount: IntType, bytes: ByteType, byteCount: IntType) -> IntType: ...
    
    @overload
    def GetCharCount(self, bytes: ArrayType[ByteType]) -> IntType: ...
    
    @overload
    def GetCharCount(self, bytes: ByteType, count: IntType) -> IntType: ...
    
    @overload
    def GetCharCount(self, bytes: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    @overload
    def GetChars(self, bytes: ArrayType[ByteType]) -> ArrayType[CharType]: ...
    
    @overload
    def GetChars(self, bytes: ArrayType[ByteType], index: IntType, count: IntType) -> ArrayType[CharType]: ...
    
    @overload
    def GetChars(self, bytes: ArrayType[ByteType], byteIndex: IntType, byteCount: IntType, chars: ArrayType[CharType], charIndex: IntType) -> IntType: ...
    
    @overload
    def GetChars(self, bytes: ByteType, byteCount: IntType, chars: CharType, charCount: IntType) -> IntType: ...
    
    def GetDecoder(self) -> Decoder: ...
    
    def GetEncoder(self) -> Encoder: ...
    
    @staticmethod
    @overload
    def GetEncoding(codepage: IntType) -> Encoding: ...
    
    @staticmethod
    @overload
    def GetEncoding(codepage: IntType, encoderFallback: EncoderFallback, decoderFallback: DecoderFallback) -> Encoding: ...
    
    @staticmethod
    @overload
    def GetEncoding(name: StringType) -> Encoding: ...
    
    @staticmethod
    @overload
    def GetEncoding(name: StringType, encoderFallback: EncoderFallback, decoderFallback: DecoderFallback) -> Encoding: ...
    
    @staticmethod
    def GetEncodings() -> ArrayType[EncodingInfo]: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def GetMaxByteCount(self, charCount: IntType) -> IntType: ...
    
    def GetMaxCharCount(self, byteCount: IntType) -> IntType: ...
    
    def GetPreamble(self) -> ArrayType[ByteType]: ...
    
    @overload
    def GetString(self, bytes: ByteType, byteCount: IntType) -> StringType: ...
    
    @overload
    def GetString(self, bytes: ArrayType[ByteType]) -> StringType: ...
    
    @overload
    def GetString(self, bytes: ArrayType[ByteType], index: IntType, count: IntType) -> StringType: ...
    
    @overload
    def IsAlwaysNormalized(self) -> BooleanType: ...
    
    @overload
    def IsAlwaysNormalized(self, form: NormalizationForm) -> BooleanType: ...
    
    @staticmethod
    def RegisterProvider(provider: EncodingProvider) -> VoidType: ...
    
    @staticmethod
    def get_ASCII() -> Encoding: ...
    
    @staticmethod
    def get_BigEndianUnicode() -> Encoding: ...
    
    def get_BodyName(self) -> StringType: ...
    
    def get_CodePage(self) -> IntType: ...
    
    def get_DecoderFallback(self) -> DecoderFallback: ...
    
    @staticmethod
    def get_Default() -> Encoding: ...
    
    def get_EncoderFallback(self) -> EncoderFallback: ...
    
    def get_EncodingName(self) -> StringType: ...
    
    def get_HeaderName(self) -> StringType: ...
    
    def get_IsBrowserDisplay(self) -> BooleanType: ...
    
    def get_IsBrowserSave(self) -> BooleanType: ...
    
    def get_IsMailNewsDisplay(self) -> BooleanType: ...
    
    def get_IsMailNewsSave(self) -> BooleanType: ...
    
    def get_IsReadOnly(self) -> BooleanType: ...
    
    def get_IsSingleByte(self) -> BooleanType: ...
    
    @staticmethod
    def get_UTF32() -> Encoding: ...
    
    @staticmethod
    def get_UTF7() -> Encoding: ...
    
    @staticmethod
    def get_UTF8() -> Encoding: ...
    
    @staticmethod
    def get_Unicode() -> Encoding: ...
    
    def get_WebName(self) -> StringType: ...
    
    def get_WindowsCodePage(self) -> IntType: ...
    
    def set_DecoderFallback(self, value: DecoderFallback) -> VoidType: ...
    
    def set_EncoderFallback(self, value: EncoderFallback) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Encoding(ABC, ObjectType, ICloneable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def ASCII() -> Encoding: ...
    
    @staticmethod
    @property
    def BigEndianUnicode() -> Encoding: ...
    
    @property
    def BodyName(self) -> StringType: ...
    
    @property
    def CodePage(self) -> IntType: ...
    
    @property
    def DecoderFallback(self) -> DecoderFallback: ...
    
    @DecoderFallback.setter
    def DecoderFallback(self, value: DecoderFallback) -> None: ...
    
    @staticmethod
    @property
    def Default() -> Encoding: ...
    
    @property
    def EncoderFallback(self) -> EncoderFallback: ...
    
    @EncoderFallback.setter
    def EncoderFallback(self, value: EncoderFallback) -> None: ...
    
    @property
    def EncodingName(self) -> StringType: ...
    
    @property
    def HeaderName(self) -> StringType: ...
    
    @property
    def IsBrowserDisplay(self) -> BooleanType: ...
    
    @property
    def IsBrowserSave(self) -> BooleanType: ...
    
    @property
    def IsMailNewsDisplay(self) -> BooleanType: ...
    
    @property
    def IsMailNewsSave(self) -> BooleanType: ...
    
    @property
    def IsReadOnly(self) -> BooleanType: ...
    
    @property
    def IsSingleByte(self) -> BooleanType: ...
    
    @staticmethod
    @property
    def UTF32() -> Encoding: ...
    
    @staticmethod
    @property
    def UTF7() -> Encoding: ...
    
    @staticmethod
    @property
    def UTF8() -> Encoding: ...
    
    @staticmethod
    @property
    def Unicode() -> Encoding: ...
    
    @property
    def WebName(self) -> StringType: ...
    
    @property
    def WindowsCodePage(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> ObjectType: ...
    
    @staticmethod
    @overload
    def Convert(srcEncoding: Encoding, dstEncoding: Encoding, bytes: ArrayType[ByteType]) -> ArrayType[ByteType]: ...
    
    @staticmethod
    @overload
    def Convert(srcEncoding: Encoding, dstEncoding: Encoding, bytes: ArrayType[ByteType], index: IntType, count: IntType) -> ArrayType[ByteType]: ...
    
    def Equals(self, value: ObjectType) -> BooleanType: ...
    
    @overload
    def GetByteCount(self, chars: ArrayType[CharType]) -> IntType: ...
    
    @overload
    def GetByteCount(self, s: StringType) -> IntType: ...
    
    @overload
    def GetByteCount(self, chars: CharType, count: IntType) -> IntType: ...
    
    @overload
    def GetByteCount(self, chars: ArrayType[CharType], index: IntType, count: IntType) -> IntType: ...
    
    @overload
    def GetBytes(self, chars: ArrayType[CharType]) -> ArrayType[ByteType]: ...
    
    @overload
    def GetBytes(self, chars: ArrayType[CharType], index: IntType, count: IntType) -> ArrayType[ByteType]: ...
    
    @overload
    def GetBytes(self, s: StringType) -> ArrayType[ByteType]: ...
    
    @overload
    def GetBytes(self, s: StringType, charIndex: IntType, charCount: IntType, bytes: ArrayType[ByteType], byteIndex: IntType) -> IntType: ...
    
    @overload
    def GetBytes(self, chars: ArrayType[CharType], charIndex: IntType, charCount: IntType, bytes: ArrayType[ByteType], byteIndex: IntType) -> IntType: ...
    
    @overload
    def GetBytes(self, chars: CharType, charCount: IntType, bytes: ByteType, byteCount: IntType) -> IntType: ...
    
    @overload
    def GetCharCount(self, bytes: ArrayType[ByteType]) -> IntType: ...
    
    @overload
    def GetCharCount(self, bytes: ByteType, count: IntType) -> IntType: ...
    
    @overload
    def GetCharCount(self, bytes: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    @overload
    def GetChars(self, bytes: ArrayType[ByteType]) -> ArrayType[CharType]: ...
    
    @overload
    def GetChars(self, bytes: ArrayType[ByteType], index: IntType, count: IntType) -> ArrayType[CharType]: ...
    
    @overload
    def GetChars(self, bytes: ArrayType[ByteType], byteIndex: IntType, byteCount: IntType, chars: ArrayType[CharType], charIndex: IntType) -> IntType: ...
    
    @overload
    def GetChars(self, bytes: ByteType, byteCount: IntType, chars: CharType, charCount: IntType) -> IntType: ...
    
    def GetDecoder(self) -> Decoder: ...
    
    def GetEncoder(self) -> Encoder: ...
    
    @staticmethod
    @overload
    def GetEncoding(codepage: IntType) -> Encoding: ...
    
    @staticmethod
    @overload
    def GetEncoding(codepage: IntType, encoderFallback: EncoderFallback, decoderFallback: DecoderFallback) -> Encoding: ...
    
    @staticmethod
    @overload
    def GetEncoding(name: StringType) -> Encoding: ...
    
    @staticmethod
    @overload
    def GetEncoding(name: StringType, encoderFallback: EncoderFallback, decoderFallback: DecoderFallback) -> Encoding: ...
    
    @staticmethod
    def GetEncodings() -> ArrayType[EncodingInfo]: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def GetMaxByteCount(self, charCount: IntType) -> IntType: ...
    
    def GetMaxCharCount(self, byteCount: IntType) -> IntType: ...
    
    def GetPreamble(self) -> ArrayType[ByteType]: ...
    
    @overload
    def GetString(self, bytes: ByteType, byteCount: IntType) -> StringType: ...
    
    @overload
    def GetString(self, bytes: ArrayType[ByteType]) -> StringType: ...
    
    @overload
    def GetString(self, bytes: ArrayType[ByteType], index: IntType, count: IntType) -> StringType: ...
    
    @overload
    def IsAlwaysNormalized(self) -> BooleanType: ...
    
    @overload
    def IsAlwaysNormalized(self, form: NormalizationForm) -> BooleanType: ...
    
    @staticmethod
    def RegisterProvider(provider: EncodingProvider) -> VoidType: ...
    
    @staticmethod
    def get_ASCII() -> Encoding: ...
    
    @staticmethod
    def get_BigEndianUnicode() -> Encoding: ...
    
    def get_BodyName(self) -> StringType: ...
    
    def get_CodePage(self) -> IntType: ...
    
    def get_DecoderFallback(self) -> DecoderFallback: ...
    
    @staticmethod
    def get_Default() -> Encoding: ...
    
    def get_EncoderFallback(self) -> EncoderFallback: ...
    
    def get_EncodingName(self) -> StringType: ...
    
    def get_HeaderName(self) -> StringType: ...
    
    def get_IsBrowserDisplay(self) -> BooleanType: ...
    
    def get_IsBrowserSave(self) -> BooleanType: ...
    
    def get_IsMailNewsDisplay(self) -> BooleanType: ...
    
    def get_IsMailNewsSave(self) -> BooleanType: ...
    
    def get_IsReadOnly(self) -> BooleanType: ...
    
    def get_IsSingleByte(self) -> BooleanType: ...
    
    @staticmethod
    def get_UTF32() -> Encoding: ...
    
    @staticmethod
    def get_UTF7() -> Encoding: ...
    
    @staticmethod
    def get_UTF8() -> Encoding: ...
    
    @staticmethod
    def get_Unicode() -> Encoding: ...
    
    def get_WebName(self) -> StringType: ...
    
    def get_WindowsCodePage(self) -> IntType: ...
    
    def set_DecoderFallback(self, value: DecoderFallback) -> VoidType: ...
    
    def set_EncoderFallback(self, value: EncoderFallback) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Encoding(ABC, ObjectType, ICloneable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def ASCII() -> Encoding: ...
    
    @staticmethod
    @property
    def BigEndianUnicode() -> Encoding: ...
    
    @property
    def BodyName(self) -> StringType: ...
    
    @property
    def CodePage(self) -> IntType: ...
    
    @property
    def DecoderFallback(self) -> DecoderFallback: ...
    
    @DecoderFallback.setter
    def DecoderFallback(self, value: DecoderFallback) -> None: ...
    
    @staticmethod
    @property
    def Default() -> Encoding: ...
    
    @property
    def EncoderFallback(self) -> EncoderFallback: ...
    
    @EncoderFallback.setter
    def EncoderFallback(self, value: EncoderFallback) -> None: ...
    
    @property
    def EncodingName(self) -> StringType: ...
    
    @property
    def HeaderName(self) -> StringType: ...
    
    @property
    def IsBrowserDisplay(self) -> BooleanType: ...
    
    @property
    def IsBrowserSave(self) -> BooleanType: ...
    
    @property
    def IsMailNewsDisplay(self) -> BooleanType: ...
    
    @property
    def IsMailNewsSave(self) -> BooleanType: ...
    
    @property
    def IsReadOnly(self) -> BooleanType: ...
    
    @property
    def IsSingleByte(self) -> BooleanType: ...
    
    @staticmethod
    @property
    def UTF32() -> Encoding: ...
    
    @staticmethod
    @property
    def UTF7() -> Encoding: ...
    
    @staticmethod
    @property
    def UTF8() -> Encoding: ...
    
    @staticmethod
    @property
    def Unicode() -> Encoding: ...
    
    @property
    def WebName(self) -> StringType: ...
    
    @property
    def WindowsCodePage(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> ObjectType: ...
    
    @staticmethod
    @overload
    def Convert(srcEncoding: Encoding, dstEncoding: Encoding, bytes: ArrayType[ByteType]) -> ArrayType[ByteType]: ...
    
    @staticmethod
    @overload
    def Convert(srcEncoding: Encoding, dstEncoding: Encoding, bytes: ArrayType[ByteType], index: IntType, count: IntType) -> ArrayType[ByteType]: ...
    
    def Equals(self, value: ObjectType) -> BooleanType: ...
    
    @overload
    def GetByteCount(self, chars: ArrayType[CharType]) -> IntType: ...
    
    @overload
    def GetByteCount(self, s: StringType) -> IntType: ...
    
    @overload
    def GetByteCount(self, chars: CharType, count: IntType) -> IntType: ...
    
    @overload
    def GetByteCount(self, chars: ArrayType[CharType], index: IntType, count: IntType) -> IntType: ...
    
    @overload
    def GetBytes(self, chars: ArrayType[CharType]) -> ArrayType[ByteType]: ...
    
    @overload
    def GetBytes(self, chars: ArrayType[CharType], index: IntType, count: IntType) -> ArrayType[ByteType]: ...
    
    @overload
    def GetBytes(self, s: StringType) -> ArrayType[ByteType]: ...
    
    @overload
    def GetBytes(self, s: StringType, charIndex: IntType, charCount: IntType, bytes: ArrayType[ByteType], byteIndex: IntType) -> IntType: ...
    
    @overload
    def GetBytes(self, chars: ArrayType[CharType], charIndex: IntType, charCount: IntType, bytes: ArrayType[ByteType], byteIndex: IntType) -> IntType: ...
    
    @overload
    def GetBytes(self, chars: CharType, charCount: IntType, bytes: ByteType, byteCount: IntType) -> IntType: ...
    
    @overload
    def GetCharCount(self, bytes: ArrayType[ByteType]) -> IntType: ...
    
    @overload
    def GetCharCount(self, bytes: ByteType, count: IntType) -> IntType: ...
    
    @overload
    def GetCharCount(self, bytes: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    @overload
    def GetChars(self, bytes: ArrayType[ByteType]) -> ArrayType[CharType]: ...
    
    @overload
    def GetChars(self, bytes: ArrayType[ByteType], index: IntType, count: IntType) -> ArrayType[CharType]: ...
    
    @overload
    def GetChars(self, bytes: ArrayType[ByteType], byteIndex: IntType, byteCount: IntType, chars: ArrayType[CharType], charIndex: IntType) -> IntType: ...
    
    @overload
    def GetChars(self, bytes: ByteType, byteCount: IntType, chars: CharType, charCount: IntType) -> IntType: ...
    
    def GetDecoder(self) -> Decoder: ...
    
    def GetEncoder(self) -> Encoder: ...
    
    @staticmethod
    @overload
    def GetEncoding(codepage: IntType) -> Encoding: ...
    
    @staticmethod
    @overload
    def GetEncoding(codepage: IntType, encoderFallback: EncoderFallback, decoderFallback: DecoderFallback) -> Encoding: ...
    
    @staticmethod
    @overload
    def GetEncoding(name: StringType) -> Encoding: ...
    
    @staticmethod
    @overload
    def GetEncoding(name: StringType, encoderFallback: EncoderFallback, decoderFallback: DecoderFallback) -> Encoding: ...
    
    @staticmethod
    def GetEncodings() -> ArrayType[EncodingInfo]: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def GetMaxByteCount(self, charCount: IntType) -> IntType: ...
    
    def GetMaxCharCount(self, byteCount: IntType) -> IntType: ...
    
    def GetPreamble(self) -> ArrayType[ByteType]: ...
    
    @overload
    def GetString(self, bytes: ByteType, byteCount: IntType) -> StringType: ...
    
    @overload
    def GetString(self, bytes: ArrayType[ByteType]) -> StringType: ...
    
    @overload
    def GetString(self, bytes: ArrayType[ByteType], index: IntType, count: IntType) -> StringType: ...
    
    @overload
    def IsAlwaysNormalized(self) -> BooleanType: ...
    
    @overload
    def IsAlwaysNormalized(self, form: NormalizationForm) -> BooleanType: ...
    
    @staticmethod
    def RegisterProvider(provider: EncodingProvider) -> VoidType: ...
    
    @staticmethod
    def get_ASCII() -> Encoding: ...
    
    @staticmethod
    def get_BigEndianUnicode() -> Encoding: ...
    
    def get_BodyName(self) -> StringType: ...
    
    def get_CodePage(self) -> IntType: ...
    
    def get_DecoderFallback(self) -> DecoderFallback: ...
    
    @staticmethod
    def get_Default() -> Encoding: ...
    
    def get_EncoderFallback(self) -> EncoderFallback: ...
    
    def get_EncodingName(self) -> StringType: ...
    
    def get_HeaderName(self) -> StringType: ...
    
    def get_IsBrowserDisplay(self) -> BooleanType: ...
    
    def get_IsBrowserSave(self) -> BooleanType: ...
    
    def get_IsMailNewsDisplay(self) -> BooleanType: ...
    
    def get_IsMailNewsSave(self) -> BooleanType: ...
    
    def get_IsReadOnly(self) -> BooleanType: ...
    
    def get_IsSingleByte(self) -> BooleanType: ...
    
    @staticmethod
    def get_UTF32() -> Encoding: ...
    
    @staticmethod
    def get_UTF7() -> Encoding: ...
    
    @staticmethod
    def get_UTF8() -> Encoding: ...
    
    @staticmethod
    def get_Unicode() -> Encoding: ...
    
    def get_WebName(self) -> StringType: ...
    
    def get_WindowsCodePage(self) -> IntType: ...
    
    def set_DecoderFallback(self, value: DecoderFallback) -> VoidType: ...
    
    def set_EncoderFallback(self, value: EncoderFallback) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EncodingInfo(ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def CodePage(self) -> IntType: ...
    
    @property
    def DisplayName(self) -> StringType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, value: ObjectType) -> BooleanType: ...
    
    def GetEncoding(self) -> Encoding: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def get_CodePage(self) -> IntType: ...
    
    def get_DisplayName(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EncodingInfo(ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def CodePage(self) -> IntType: ...
    
    @property
    def DisplayName(self) -> StringType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, value: ObjectType) -> BooleanType: ...
    
    def GetEncoding(self) -> Encoding: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def get_CodePage(self) -> IntType: ...
    
    def get_DisplayName(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EncodingInfo(ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def CodePage(self) -> IntType: ...
    
    @property
    def DisplayName(self) -> StringType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, value: ObjectType) -> BooleanType: ...
    
    def GetEncoding(self) -> Encoding: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def get_CodePage(self) -> IntType: ...
    
    def get_DisplayName(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EncodingNLS(ABC, Encoding, ICloneable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def GetByteCount(self, s: StringType) -> IntType: ...
    
    @overload
    def GetByteCount(self, chars: CharType, count: IntType) -> IntType: ...
    
    @overload
    def GetByteCount(self, chars: ArrayType[CharType], index: IntType, count: IntType) -> IntType: ...
    
    @overload
    def GetBytes(self, s: StringType, charIndex: IntType, charCount: IntType, bytes: ArrayType[ByteType], byteIndex: IntType) -> IntType: ...
    
    @overload
    def GetBytes(self, chars: ArrayType[CharType], charIndex: IntType, charCount: IntType, bytes: ArrayType[ByteType], byteIndex: IntType) -> IntType: ...
    
    @overload
    def GetBytes(self, chars: CharType, charCount: IntType, bytes: ByteType, byteCount: IntType) -> IntType: ...
    
    @overload
    def GetCharCount(self, bytes: ByteType, count: IntType) -> IntType: ...
    
    @overload
    def GetCharCount(self, bytes: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    @overload
    def GetChars(self, bytes: ArrayType[ByteType], byteIndex: IntType, byteCount: IntType, chars: ArrayType[CharType], charIndex: IntType) -> IntType: ...
    
    @overload
    def GetChars(self, bytes: ByteType, byteCount: IntType, chars: CharType, charCount: IntType) -> IntType: ...
    
    def GetDecoder(self) -> Decoder: ...
    
    def GetEncoder(self) -> Encoder: ...
    
    @overload
    def GetString(self, bytes: ArrayType[ByteType], index: IntType, count: IntType) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EncodingNLS(ABC, Encoding, ICloneable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def GetByteCount(self, s: StringType) -> IntType: ...
    
    @overload
    def GetByteCount(self, chars: CharType, count: IntType) -> IntType: ...
    
    @overload
    def GetByteCount(self, chars: ArrayType[CharType], index: IntType, count: IntType) -> IntType: ...
    
    @overload
    def GetBytes(self, s: StringType, charIndex: IntType, charCount: IntType, bytes: ArrayType[ByteType], byteIndex: IntType) -> IntType: ...
    
    @overload
    def GetBytes(self, chars: ArrayType[CharType], charIndex: IntType, charCount: IntType, bytes: ArrayType[ByteType], byteIndex: IntType) -> IntType: ...
    
    @overload
    def GetBytes(self, chars: CharType, charCount: IntType, bytes: ByteType, byteCount: IntType) -> IntType: ...
    
    @overload
    def GetCharCount(self, bytes: ByteType, count: IntType) -> IntType: ...
    
    @overload
    def GetCharCount(self, bytes: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    @overload
    def GetChars(self, bytes: ArrayType[ByteType], byteIndex: IntType, byteCount: IntType, chars: ArrayType[CharType], charIndex: IntType) -> IntType: ...
    
    @overload
    def GetChars(self, bytes: ByteType, byteCount: IntType, chars: CharType, charCount: IntType) -> IntType: ...
    
    def GetDecoder(self) -> Decoder: ...
    
    def GetEncoder(self) -> Encoder: ...
    
    @overload
    def GetString(self, bytes: ArrayType[ByteType], index: IntType, count: IntType) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EncodingNLS(ABC, Encoding, ICloneable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def GetByteCount(self, s: StringType) -> IntType: ...
    
    @overload
    def GetByteCount(self, chars: CharType, count: IntType) -> IntType: ...
    
    @overload
    def GetByteCount(self, chars: ArrayType[CharType], index: IntType, count: IntType) -> IntType: ...
    
    @overload
    def GetBytes(self, s: StringType, charIndex: IntType, charCount: IntType, bytes: ArrayType[ByteType], byteIndex: IntType) -> IntType: ...
    
    @overload
    def GetBytes(self, chars: ArrayType[CharType], charIndex: IntType, charCount: IntType, bytes: ArrayType[ByteType], byteIndex: IntType) -> IntType: ...
    
    @overload
    def GetBytes(self, chars: CharType, charCount: IntType, bytes: ByteType, byteCount: IntType) -> IntType: ...
    
    @overload
    def GetCharCount(self, bytes: ByteType, count: IntType) -> IntType: ...
    
    @overload
    def GetCharCount(self, bytes: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    @overload
    def GetChars(self, bytes: ArrayType[ByteType], byteIndex: IntType, byteCount: IntType, chars: ArrayType[CharType], charIndex: IntType) -> IntType: ...
    
    @overload
    def GetChars(self, bytes: ByteType, byteCount: IntType, chars: CharType, charCount: IntType) -> IntType: ...
    
    def GetDecoder(self) -> Decoder: ...
    
    def GetEncoder(self) -> Encoder: ...
    
    @overload
    def GetString(self, bytes: ArrayType[ByteType], index: IntType, count: IntType) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EncodingProvider(ABC, ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def GetEncoding(self, name: StringType, encoderFallback: EncoderFallback, decoderFallback: DecoderFallback) -> Encoding: ...
    
    @overload
    def GetEncoding(self, codepage: IntType, encoderFallback: EncoderFallback, decoderFallback: DecoderFallback) -> Encoding: ...
    
    @overload
    def GetEncoding(self, name: StringType) -> Encoding: ...
    
    @overload
    def GetEncoding(self, codepage: IntType) -> Encoding: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EncodingProvider(ABC, ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def GetEncoding(self, name: StringType, encoderFallback: EncoderFallback, decoderFallback: DecoderFallback) -> Encoding: ...
    
    @overload
    def GetEncoding(self, codepage: IntType, encoderFallback: EncoderFallback, decoderFallback: DecoderFallback) -> Encoding: ...
    
    @overload
    def GetEncoding(self, name: StringType) -> Encoding: ...
    
    @overload
    def GetEncoding(self, codepage: IntType) -> Encoding: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EncodingProvider(ABC, ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def GetEncoding(self, name: StringType, encoderFallback: EncoderFallback, decoderFallback: DecoderFallback) -> Encoding: ...
    
    @overload
    def GetEncoding(self, codepage: IntType, encoderFallback: EncoderFallback, decoderFallback: DecoderFallback) -> Encoding: ...
    
    @overload
    def GetEncoding(self, name: StringType) -> Encoding: ...
    
    @overload
    def GetEncoding(self, codepage: IntType) -> Encoding: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class GB18030Encoding(DBCSCodePageEncoding, ICloneable, ISerializable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetDecoder(self) -> Decoder: ...
    
    def GetMaxByteCount(self, charCount: IntType) -> IntType: ...
    
    def GetMaxCharCount(self, byteCount: IntType) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class GB18030Encoding(DBCSCodePageEncoding, ICloneable, ISerializable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetDecoder(self) -> Decoder: ...
    
    def GetMaxByteCount(self, charCount: IntType) -> IntType: ...
    
    def GetMaxCharCount(self, byteCount: IntType) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class GB18030Encoding(DBCSCodePageEncoding, ICloneable, ISerializable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetDecoder(self) -> Decoder: ...
    
    def GetMaxByteCount(self, charCount: IntType) -> IntType: ...
    
    def GetMaxCharCount(self, byteCount: IntType) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ISCIIEncoding(EncodingNLS, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, codePage: IntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetDecoder(self) -> Decoder: ...
    
    def GetEncoder(self) -> Encoder: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def GetMaxByteCount(self, charCount: IntType) -> IntType: ...
    
    def GetMaxCharCount(self, byteCount: IntType) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ISCIIEncoding(EncodingNLS, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, codePage: IntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetDecoder(self) -> Decoder: ...
    
    def GetEncoder(self) -> Encoder: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def GetMaxByteCount(self, charCount: IntType) -> IntType: ...
    
    def GetMaxCharCount(self, byteCount: IntType) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ISCIIEncoding(EncodingNLS, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, codePage: IntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetDecoder(self) -> Decoder: ...
    
    def GetEncoder(self) -> Encoder: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def GetMaxByteCount(self, charCount: IntType) -> IntType: ...
    
    def GetMaxCharCount(self, byteCount: IntType) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ISO2022Encoding(DBCSCodePageEncoding, ICloneable, ISerializable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetDecoder(self) -> Decoder: ...
    
    def GetEncoder(self) -> Encoder: ...
    
    def GetMaxByteCount(self, charCount: IntType) -> IntType: ...
    
    def GetMaxCharCount(self, byteCount: IntType) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ISO2022Encoding(DBCSCodePageEncoding, ICloneable, ISerializable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetDecoder(self) -> Decoder: ...
    
    def GetEncoder(self) -> Encoder: ...
    
    def GetMaxByteCount(self, charCount: IntType) -> IntType: ...
    
    def GetMaxCharCount(self, byteCount: IntType) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ISO2022Encoding(DBCSCodePageEncoding, ICloneable, ISerializable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetDecoder(self) -> Decoder: ...
    
    def GetEncoder(self) -> Encoder: ...
    
    def GetMaxByteCount(self, charCount: IntType) -> IntType: ...
    
    def GetMaxCharCount(self, byteCount: IntType) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class InternalDecoderBestFitFallback(DecoderFallback):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def MaxCharCount(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def CreateFallbackBuffer(self) -> DecoderFallbackBuffer: ...
    
    def Equals(self, value: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def get_MaxCharCount(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class InternalDecoderBestFitFallback(DecoderFallback):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def MaxCharCount(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def CreateFallbackBuffer(self) -> DecoderFallbackBuffer: ...
    
    def Equals(self, value: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def get_MaxCharCount(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class InternalDecoderBestFitFallback(DecoderFallback):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def MaxCharCount(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def CreateFallbackBuffer(self) -> DecoderFallbackBuffer: ...
    
    def Equals(self, value: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def get_MaxCharCount(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class InternalDecoderBestFitFallbackBuffer(DecoderFallbackBuffer):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, fallback: InternalDecoderBestFitFallback): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Remaining(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def Fallback(self, bytesUnknown: ArrayType[ByteType], index: IntType) -> BooleanType: ...
    
    def GetNextChar(self) -> CharType: ...
    
    def MovePrevious(self) -> BooleanType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Remaining(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class InternalDecoderBestFitFallbackBuffer(DecoderFallbackBuffer):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, fallback: InternalDecoderBestFitFallback): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Remaining(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def Fallback(self, bytesUnknown: ArrayType[ByteType], index: IntType) -> BooleanType: ...
    
    def GetNextChar(self) -> CharType: ...
    
    def MovePrevious(self) -> BooleanType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Remaining(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class InternalDecoderBestFitFallbackBuffer(DecoderFallbackBuffer):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, fallback: InternalDecoderBestFitFallback): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Remaining(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def Fallback(self, bytesUnknown: ArrayType[ByteType], index: IntType) -> BooleanType: ...
    
    def GetNextChar(self) -> CharType: ...
    
    def MovePrevious(self) -> BooleanType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Remaining(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class InternalEncoderBestFitFallback(EncoderFallback):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def MaxCharCount(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def CreateFallbackBuffer(self) -> EncoderFallbackBuffer: ...
    
    def Equals(self, value: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def get_MaxCharCount(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class InternalEncoderBestFitFallback(EncoderFallback):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def MaxCharCount(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def CreateFallbackBuffer(self) -> EncoderFallbackBuffer: ...
    
    def Equals(self, value: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def get_MaxCharCount(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class InternalEncoderBestFitFallback(EncoderFallback):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def MaxCharCount(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def CreateFallbackBuffer(self) -> EncoderFallbackBuffer: ...
    
    def Equals(self, value: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def get_MaxCharCount(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class InternalEncoderBestFitFallbackBuffer(EncoderFallbackBuffer):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, fallback: InternalEncoderBestFitFallback): ...
    
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


class InternalEncoderBestFitFallbackBuffer(EncoderFallbackBuffer):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, fallback: InternalEncoderBestFitFallback): ...
    
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


class InternalEncoderBestFitFallbackBuffer(EncoderFallbackBuffer):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, fallback: InternalEncoderBestFitFallback): ...
    
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


class Latin1Encoding(EncodingNLS, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def IsSingleByte(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def GetMaxByteCount(self, charCount: IntType) -> IntType: ...
    
    def GetMaxCharCount(self, byteCount: IntType) -> IntType: ...
    
    @overload
    def IsAlwaysNormalized(self, form: NormalizationForm) -> BooleanType: ...
    
    def get_IsSingleByte(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Latin1Encoding(EncodingNLS, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def IsSingleByte(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def GetMaxByteCount(self, charCount: IntType) -> IntType: ...
    
    def GetMaxCharCount(self, byteCount: IntType) -> IntType: ...
    
    @overload
    def IsAlwaysNormalized(self, form: NormalizationForm) -> BooleanType: ...
    
    def get_IsSingleByte(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Latin1Encoding(EncodingNLS, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def IsSingleByte(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def GetMaxByteCount(self, charCount: IntType) -> IntType: ...
    
    def GetMaxCharCount(self, byteCount: IntType) -> IntType: ...
    
    @overload
    def IsAlwaysNormalized(self, form: NormalizationForm) -> BooleanType: ...
    
    def get_IsSingleByte(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MLangCodePageEncoding(ObjectType, ISerializable, IObjectReference):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetRealObject(self, context: StreamingContext) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MLangCodePageEncoding(ObjectType, ISerializable, IObjectReference):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetRealObject(self, context: StreamingContext) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MLangCodePageEncoding(ObjectType, ISerializable, IObjectReference):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetRealObject(self, context: StreamingContext) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Normalization(ObjectType):
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


class Normalization(ObjectType):
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


class Normalization(ObjectType):
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


class SBCSCodePageEncoding(BaseCodePageEncoding, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, codePage: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def IsSingleByte(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def GetMaxByteCount(self, charCount: IntType) -> IntType: ...
    
    def GetMaxCharCount(self, byteCount: IntType) -> IntType: ...
    
    @overload
    def IsAlwaysNormalized(self, form: NormalizationForm) -> BooleanType: ...
    
    def get_IsSingleByte(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SBCSCodePageEncoding(BaseCodePageEncoding, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, codePage: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def IsSingleByte(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def GetMaxByteCount(self, charCount: IntType) -> IntType: ...
    
    def GetMaxCharCount(self, byteCount: IntType) -> IntType: ...
    
    @overload
    def IsAlwaysNormalized(self, form: NormalizationForm) -> BooleanType: ...
    
    def get_IsSingleByte(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SBCSCodePageEncoding(BaseCodePageEncoding, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, codePage: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def IsSingleByte(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def GetMaxByteCount(self, charCount: IntType) -> IntType: ...
    
    def GetMaxCharCount(self, byteCount: IntType) -> IntType: ...
    
    @overload
    def IsAlwaysNormalized(self, form: NormalizationForm) -> BooleanType: ...
    
    def get_IsSingleByte(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class StringBuilder(ObjectType, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, capacity: IntType): ...
    
    @overload
    def __init__(self, value: StringType): ...
    
    @overload
    def __init__(self, value: StringType, capacity: IntType): ...
    
    @overload
    def __init__(self, value: StringType, startIndex: IntType, length: IntType, capacity: IntType): ...
    
    @overload
    def __init__(self, capacity: IntType, maxCapacity: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Capacity(self) -> IntType: ...
    
    @Capacity.setter
    def Capacity(self, value: IntType) -> None: ...
    
    @property
    def Chars(self) -> CharType: ...
    
    @Chars.setter
    def Chars(self, value: CharType) -> None: ...
    
    @property
    def Length(self) -> IntType: ...
    
    @Length.setter
    def Length(self, value: IntType) -> None: ...
    
    @property
    def MaxCapacity(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Append(self, value: CharType, repeatCount: IntType) -> StringBuilder: ...
    
    @overload
    def Append(self, value: ArrayType[CharType], startIndex: IntType, charCount: IntType) -> StringBuilder: ...
    
    @overload
    def Append(self, value: StringType) -> StringBuilder: ...
    
    @overload
    def Append(self, value: StringType, startIndex: IntType, count: IntType) -> StringBuilder: ...
    
    @overload
    def Append(self, value: SByteType) -> StringBuilder: ...
    
    @overload
    def Append(self, value: ByteType) -> StringBuilder: ...
    
    @overload
    def Append(self, value: CharType) -> StringBuilder: ...
    
    @overload
    def Append(self, value: ShortType) -> StringBuilder: ...
    
    @overload
    def Append(self, value: IntType) -> StringBuilder: ...
    
    @overload
    def Append(self, value: LongType) -> StringBuilder: ...
    
    @overload
    def Append(self, value: FloatType) -> StringBuilder: ...
    
    @overload
    def Append(self, value: DoubleType) -> StringBuilder: ...
    
    @overload
    def Append(self, value: DecimalType) -> StringBuilder: ...
    
    @overload
    def Append(self, value: UShortType) -> StringBuilder: ...
    
    @overload
    def Append(self, value: UIntType) -> StringBuilder: ...
    
    @overload
    def Append(self, value: ULongType) -> StringBuilder: ...
    
    @overload
    def Append(self, value: ObjectType) -> StringBuilder: ...
    
    @overload
    def Append(self, value: ArrayType[CharType]) -> StringBuilder: ...
    
    @overload
    def Append(self, value: CharType, valueCount: IntType) -> StringBuilder: ...
    
    @overload
    def Append(self, value: BooleanType) -> StringBuilder: ...
    
    @overload
    def AppendFormat(self, format: StringType, arg0: ObjectType) -> StringBuilder: ...
    
    @overload
    def AppendFormat(self, format: StringType, arg0: ObjectType, arg1: ObjectType) -> StringBuilder: ...
    
    @overload
    def AppendFormat(self, format: StringType, arg0: ObjectType, arg1: ObjectType, arg2: ObjectType) -> StringBuilder: ...
    
    @overload
    def AppendFormat(self, provider: IFormatProvider, format: StringType, arg0: ObjectType) -> StringBuilder: ...
    
    @overload
    def AppendFormat(self, provider: IFormatProvider, format: StringType, arg0: ObjectType, arg1: ObjectType) -> StringBuilder: ...
    
    @overload
    def AppendFormat(self, provider: IFormatProvider, format: StringType, arg0: ObjectType, arg1: ObjectType, arg2: ObjectType) -> StringBuilder: ...
    
    @overload
    def AppendFormat(self, format: StringType, args: ArrayType[ObjectType]) -> StringBuilder: ...
    
    @overload
    def AppendFormat(self, provider: IFormatProvider, format: StringType, args: ArrayType[ObjectType]) -> StringBuilder: ...
    
    @overload
    def AppendLine(self) -> StringBuilder: ...
    
    @overload
    def AppendLine(self, value: StringType) -> StringBuilder: ...
    
    def Clear(self) -> StringBuilder: ...
    
    def CopyTo(self, sourceIndex: IntType, destination: ArrayType[CharType], destinationIndex: IntType, count: IntType) -> VoidType: ...
    
    def EnsureCapacity(self, capacity: IntType) -> IntType: ...
    
    @overload
    def Equals(self, sb: StringBuilder) -> BooleanType: ...
    
    @overload
    def Insert(self, index: IntType, value: StringType, count: IntType) -> StringBuilder: ...
    
    @overload
    def Insert(self, index: IntType, value: StringType) -> StringBuilder: ...
    
    @overload
    def Insert(self, index: IntType, value: SByteType) -> StringBuilder: ...
    
    @overload
    def Insert(self, index: IntType, value: ByteType) -> StringBuilder: ...
    
    @overload
    def Insert(self, index: IntType, value: ShortType) -> StringBuilder: ...
    
    @overload
    def Insert(self, index: IntType, value: CharType) -> StringBuilder: ...
    
    @overload
    def Insert(self, index: IntType, value: ArrayType[CharType]) -> StringBuilder: ...
    
    @overload
    def Insert(self, index: IntType, value: ArrayType[CharType], startIndex: IntType, charCount: IntType) -> StringBuilder: ...
    
    @overload
    def Insert(self, index: IntType, value: IntType) -> StringBuilder: ...
    
    @overload
    def Insert(self, index: IntType, value: LongType) -> StringBuilder: ...
    
    @overload
    def Insert(self, index: IntType, value: FloatType) -> StringBuilder: ...
    
    @overload
    def Insert(self, index: IntType, value: DoubleType) -> StringBuilder: ...
    
    @overload
    def Insert(self, index: IntType, value: DecimalType) -> StringBuilder: ...
    
    @overload
    def Insert(self, index: IntType, value: UShortType) -> StringBuilder: ...
    
    @overload
    def Insert(self, index: IntType, value: UIntType) -> StringBuilder: ...
    
    @overload
    def Insert(self, index: IntType, value: ULongType) -> StringBuilder: ...
    
    @overload
    def Insert(self, index: IntType, value: ObjectType) -> StringBuilder: ...
    
    @overload
    def Insert(self, index: IntType, value: BooleanType) -> StringBuilder: ...
    
    def Remove(self, startIndex: IntType, length: IntType) -> StringBuilder: ...
    
    @overload
    def Replace(self, oldValue: StringType, newValue: StringType) -> StringBuilder: ...
    
    @overload
    def Replace(self, oldValue: StringType, newValue: StringType, startIndex: IntType, count: IntType) -> StringBuilder: ...
    
    @overload
    def Replace(self, oldChar: CharType, newChar: CharType) -> StringBuilder: ...
    
    @overload
    def Replace(self, oldChar: CharType, newChar: CharType, startIndex: IntType, count: IntType) -> StringBuilder: ...
    
    @overload
    def ToString(self) -> StringType: ...
    
    @overload
    def ToString(self, startIndex: IntType, length: IntType) -> StringType: ...
    
    def get_Capacity(self) -> IntType: ...
    
    def get_Chars(self, index: IntType) -> CharType: ...
    
    def get_Length(self) -> IntType: ...
    
    def get_MaxCapacity(self) -> IntType: ...
    
    def set_Capacity(self, value: IntType) -> VoidType: ...
    
    def set_Chars(self, index: IntType, value: CharType) -> VoidType: ...
    
    def set_Length(self, value: IntType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class StringBuilder(ObjectType, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, capacity: IntType): ...
    
    @overload
    def __init__(self, value: StringType): ...
    
    @overload
    def __init__(self, value: StringType, capacity: IntType): ...
    
    @overload
    def __init__(self, value: StringType, startIndex: IntType, length: IntType, capacity: IntType): ...
    
    @overload
    def __init__(self, capacity: IntType, maxCapacity: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Capacity(self) -> IntType: ...
    
    @Capacity.setter
    def Capacity(self, value: IntType) -> None: ...
    
    @property
    def Chars(self) -> CharType: ...
    
    @Chars.setter
    def Chars(self, value: CharType) -> None: ...
    
    @property
    def Length(self) -> IntType: ...
    
    @Length.setter
    def Length(self, value: IntType) -> None: ...
    
    @property
    def MaxCapacity(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Append(self, value: CharType, repeatCount: IntType) -> StringBuilder: ...
    
    @overload
    def Append(self, value: ArrayType[CharType], startIndex: IntType, charCount: IntType) -> StringBuilder: ...
    
    @overload
    def Append(self, value: StringType) -> StringBuilder: ...
    
    @overload
    def Append(self, value: StringType, startIndex: IntType, count: IntType) -> StringBuilder: ...
    
    @overload
    def Append(self, value: SByteType) -> StringBuilder: ...
    
    @overload
    def Append(self, value: ByteType) -> StringBuilder: ...
    
    @overload
    def Append(self, value: CharType) -> StringBuilder: ...
    
    @overload
    def Append(self, value: ShortType) -> StringBuilder: ...
    
    @overload
    def Append(self, value: IntType) -> StringBuilder: ...
    
    @overload
    def Append(self, value: LongType) -> StringBuilder: ...
    
    @overload
    def Append(self, value: FloatType) -> StringBuilder: ...
    
    @overload
    def Append(self, value: DoubleType) -> StringBuilder: ...
    
    @overload
    def Append(self, value: DecimalType) -> StringBuilder: ...
    
    @overload
    def Append(self, value: UShortType) -> StringBuilder: ...
    
    @overload
    def Append(self, value: UIntType) -> StringBuilder: ...
    
    @overload
    def Append(self, value: ULongType) -> StringBuilder: ...
    
    @overload
    def Append(self, value: ObjectType) -> StringBuilder: ...
    
    @overload
    def Append(self, value: ArrayType[CharType]) -> StringBuilder: ...
    
    @overload
    def Append(self, value: CharType, valueCount: IntType) -> StringBuilder: ...
    
    @overload
    def Append(self, value: BooleanType) -> StringBuilder: ...
    
    @overload
    def AppendFormat(self, format: StringType, arg0: ObjectType) -> StringBuilder: ...
    
    @overload
    def AppendFormat(self, format: StringType, arg0: ObjectType, arg1: ObjectType) -> StringBuilder: ...
    
    @overload
    def AppendFormat(self, format: StringType, arg0: ObjectType, arg1: ObjectType, arg2: ObjectType) -> StringBuilder: ...
    
    @overload
    def AppendFormat(self, provider: IFormatProvider, format: StringType, arg0: ObjectType) -> StringBuilder: ...
    
    @overload
    def AppendFormat(self, provider: IFormatProvider, format: StringType, arg0: ObjectType, arg1: ObjectType) -> StringBuilder: ...
    
    @overload
    def AppendFormat(self, provider: IFormatProvider, format: StringType, arg0: ObjectType, arg1: ObjectType, arg2: ObjectType) -> StringBuilder: ...
    
    @overload
    def AppendFormat(self, format: StringType, args: ArrayType[ObjectType]) -> StringBuilder: ...
    
    @overload
    def AppendFormat(self, provider: IFormatProvider, format: StringType, args: ArrayType[ObjectType]) -> StringBuilder: ...
    
    @overload
    def AppendLine(self) -> StringBuilder: ...
    
    @overload
    def AppendLine(self, value: StringType) -> StringBuilder: ...
    
    def Clear(self) -> StringBuilder: ...
    
    def CopyTo(self, sourceIndex: IntType, destination: ArrayType[CharType], destinationIndex: IntType, count: IntType) -> VoidType: ...
    
    def EnsureCapacity(self, capacity: IntType) -> IntType: ...
    
    @overload
    def Equals(self, sb: StringBuilder) -> BooleanType: ...
    
    @overload
    def Insert(self, index: IntType, value: StringType, count: IntType) -> StringBuilder: ...
    
    @overload
    def Insert(self, index: IntType, value: StringType) -> StringBuilder: ...
    
    @overload
    def Insert(self, index: IntType, value: SByteType) -> StringBuilder: ...
    
    @overload
    def Insert(self, index: IntType, value: ByteType) -> StringBuilder: ...
    
    @overload
    def Insert(self, index: IntType, value: ShortType) -> StringBuilder: ...
    
    @overload
    def Insert(self, index: IntType, value: CharType) -> StringBuilder: ...
    
    @overload
    def Insert(self, index: IntType, value: ArrayType[CharType]) -> StringBuilder: ...
    
    @overload
    def Insert(self, index: IntType, value: ArrayType[CharType], startIndex: IntType, charCount: IntType) -> StringBuilder: ...
    
    @overload
    def Insert(self, index: IntType, value: IntType) -> StringBuilder: ...
    
    @overload
    def Insert(self, index: IntType, value: LongType) -> StringBuilder: ...
    
    @overload
    def Insert(self, index: IntType, value: FloatType) -> StringBuilder: ...
    
    @overload
    def Insert(self, index: IntType, value: DoubleType) -> StringBuilder: ...
    
    @overload
    def Insert(self, index: IntType, value: DecimalType) -> StringBuilder: ...
    
    @overload
    def Insert(self, index: IntType, value: UShortType) -> StringBuilder: ...
    
    @overload
    def Insert(self, index: IntType, value: UIntType) -> StringBuilder: ...
    
    @overload
    def Insert(self, index: IntType, value: ULongType) -> StringBuilder: ...
    
    @overload
    def Insert(self, index: IntType, value: ObjectType) -> StringBuilder: ...
    
    @overload
    def Insert(self, index: IntType, value: BooleanType) -> StringBuilder: ...
    
    def Remove(self, startIndex: IntType, length: IntType) -> StringBuilder: ...
    
    @overload
    def Replace(self, oldValue: StringType, newValue: StringType) -> StringBuilder: ...
    
    @overload
    def Replace(self, oldValue: StringType, newValue: StringType, startIndex: IntType, count: IntType) -> StringBuilder: ...
    
    @overload
    def Replace(self, oldChar: CharType, newChar: CharType) -> StringBuilder: ...
    
    @overload
    def Replace(self, oldChar: CharType, newChar: CharType, startIndex: IntType, count: IntType) -> StringBuilder: ...
    
    @overload
    def ToString(self) -> StringType: ...
    
    @overload
    def ToString(self, startIndex: IntType, length: IntType) -> StringType: ...
    
    def get_Capacity(self) -> IntType: ...
    
    def get_Chars(self, index: IntType) -> CharType: ...
    
    def get_Length(self) -> IntType: ...
    
    def get_MaxCapacity(self) -> IntType: ...
    
    def set_Capacity(self, value: IntType) -> VoidType: ...
    
    def set_Chars(self, index: IntType, value: CharType) -> VoidType: ...
    
    def set_Length(self, value: IntType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class StringBuilder(ObjectType, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, capacity: IntType): ...
    
    @overload
    def __init__(self, value: StringType): ...
    
    @overload
    def __init__(self, value: StringType, capacity: IntType): ...
    
    @overload
    def __init__(self, value: StringType, startIndex: IntType, length: IntType, capacity: IntType): ...
    
    @overload
    def __init__(self, capacity: IntType, maxCapacity: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Capacity(self) -> IntType: ...
    
    @Capacity.setter
    def Capacity(self, value: IntType) -> None: ...
    
    @property
    def Chars(self) -> CharType: ...
    
    @Chars.setter
    def Chars(self, value: CharType) -> None: ...
    
    @property
    def Length(self) -> IntType: ...
    
    @Length.setter
    def Length(self, value: IntType) -> None: ...
    
    @property
    def MaxCapacity(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Append(self, value: CharType, repeatCount: IntType) -> StringBuilder: ...
    
    @overload
    def Append(self, value: ArrayType[CharType], startIndex: IntType, charCount: IntType) -> StringBuilder: ...
    
    @overload
    def Append(self, value: StringType) -> StringBuilder: ...
    
    @overload
    def Append(self, value: StringType, startIndex: IntType, count: IntType) -> StringBuilder: ...
    
    @overload
    def Append(self, value: SByteType) -> StringBuilder: ...
    
    @overload
    def Append(self, value: ByteType) -> StringBuilder: ...
    
    @overload
    def Append(self, value: CharType) -> StringBuilder: ...
    
    @overload
    def Append(self, value: ShortType) -> StringBuilder: ...
    
    @overload
    def Append(self, value: IntType) -> StringBuilder: ...
    
    @overload
    def Append(self, value: LongType) -> StringBuilder: ...
    
    @overload
    def Append(self, value: FloatType) -> StringBuilder: ...
    
    @overload
    def Append(self, value: DoubleType) -> StringBuilder: ...
    
    @overload
    def Append(self, value: DecimalType) -> StringBuilder: ...
    
    @overload
    def Append(self, value: UShortType) -> StringBuilder: ...
    
    @overload
    def Append(self, value: UIntType) -> StringBuilder: ...
    
    @overload
    def Append(self, value: ULongType) -> StringBuilder: ...
    
    @overload
    def Append(self, value: ObjectType) -> StringBuilder: ...
    
    @overload
    def Append(self, value: ArrayType[CharType]) -> StringBuilder: ...
    
    @overload
    def Append(self, value: CharType, valueCount: IntType) -> StringBuilder: ...
    
    @overload
    def Append(self, value: BooleanType) -> StringBuilder: ...
    
    @overload
    def AppendFormat(self, format: StringType, arg0: ObjectType) -> StringBuilder: ...
    
    @overload
    def AppendFormat(self, format: StringType, arg0: ObjectType, arg1: ObjectType) -> StringBuilder: ...
    
    @overload
    def AppendFormat(self, format: StringType, arg0: ObjectType, arg1: ObjectType, arg2: ObjectType) -> StringBuilder: ...
    
    @overload
    def AppendFormat(self, provider: IFormatProvider, format: StringType, arg0: ObjectType) -> StringBuilder: ...
    
    @overload
    def AppendFormat(self, provider: IFormatProvider, format: StringType, arg0: ObjectType, arg1: ObjectType) -> StringBuilder: ...
    
    @overload
    def AppendFormat(self, provider: IFormatProvider, format: StringType, arg0: ObjectType, arg1: ObjectType, arg2: ObjectType) -> StringBuilder: ...
    
    @overload
    def AppendFormat(self, format: StringType, args: ArrayType[ObjectType]) -> StringBuilder: ...
    
    @overload
    def AppendFormat(self, provider: IFormatProvider, format: StringType, args: ArrayType[ObjectType]) -> StringBuilder: ...
    
    @overload
    def AppendLine(self) -> StringBuilder: ...
    
    @overload
    def AppendLine(self, value: StringType) -> StringBuilder: ...
    
    def Clear(self) -> StringBuilder: ...
    
    def CopyTo(self, sourceIndex: IntType, destination: ArrayType[CharType], destinationIndex: IntType, count: IntType) -> VoidType: ...
    
    def EnsureCapacity(self, capacity: IntType) -> IntType: ...
    
    @overload
    def Equals(self, sb: StringBuilder) -> BooleanType: ...
    
    @overload
    def Insert(self, index: IntType, value: StringType, count: IntType) -> StringBuilder: ...
    
    @overload
    def Insert(self, index: IntType, value: StringType) -> StringBuilder: ...
    
    @overload
    def Insert(self, index: IntType, value: SByteType) -> StringBuilder: ...
    
    @overload
    def Insert(self, index: IntType, value: ByteType) -> StringBuilder: ...
    
    @overload
    def Insert(self, index: IntType, value: ShortType) -> StringBuilder: ...
    
    @overload
    def Insert(self, index: IntType, value: CharType) -> StringBuilder: ...
    
    @overload
    def Insert(self, index: IntType, value: ArrayType[CharType]) -> StringBuilder: ...
    
    @overload
    def Insert(self, index: IntType, value: ArrayType[CharType], startIndex: IntType, charCount: IntType) -> StringBuilder: ...
    
    @overload
    def Insert(self, index: IntType, value: IntType) -> StringBuilder: ...
    
    @overload
    def Insert(self, index: IntType, value: LongType) -> StringBuilder: ...
    
    @overload
    def Insert(self, index: IntType, value: FloatType) -> StringBuilder: ...
    
    @overload
    def Insert(self, index: IntType, value: DoubleType) -> StringBuilder: ...
    
    @overload
    def Insert(self, index: IntType, value: DecimalType) -> StringBuilder: ...
    
    @overload
    def Insert(self, index: IntType, value: UShortType) -> StringBuilder: ...
    
    @overload
    def Insert(self, index: IntType, value: UIntType) -> StringBuilder: ...
    
    @overload
    def Insert(self, index: IntType, value: ULongType) -> StringBuilder: ...
    
    @overload
    def Insert(self, index: IntType, value: ObjectType) -> StringBuilder: ...
    
    @overload
    def Insert(self, index: IntType, value: BooleanType) -> StringBuilder: ...
    
    def Remove(self, startIndex: IntType, length: IntType) -> StringBuilder: ...
    
    @overload
    def Replace(self, oldValue: StringType, newValue: StringType) -> StringBuilder: ...
    
    @overload
    def Replace(self, oldValue: StringType, newValue: StringType, startIndex: IntType, count: IntType) -> StringBuilder: ...
    
    @overload
    def Replace(self, oldChar: CharType, newChar: CharType) -> StringBuilder: ...
    
    @overload
    def Replace(self, oldChar: CharType, newChar: CharType, startIndex: IntType, count: IntType) -> StringBuilder: ...
    
    @overload
    def ToString(self) -> StringType: ...
    
    @overload
    def ToString(self, startIndex: IntType, length: IntType) -> StringType: ...
    
    def get_Capacity(self) -> IntType: ...
    
    def get_Chars(self, index: IntType) -> CharType: ...
    
    def get_Length(self) -> IntType: ...
    
    def get_MaxCapacity(self) -> IntType: ...
    
    def set_Capacity(self, value: IntType) -> VoidType: ...
    
    def set_Chars(self, index: IntType, value: CharType) -> VoidType: ...
    
    def set_Length(self, value: IntType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class StringBuilderCache(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def Acquire(capacity: IntType = 16) -> StringBuilder: ...
    
    @staticmethod
    def GetStringAndRelease(sb: StringBuilder) -> StringType: ...
    
    @staticmethod
    def Release(sb: StringBuilder) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class StringBuilderCache(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def Acquire(capacity: IntType = 16) -> StringBuilder: ...
    
    @staticmethod
    def GetStringAndRelease(sb: StringBuilder) -> StringType: ...
    
    @staticmethod
    def Release(sb: StringBuilder) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class StringBuilderCache(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def Acquire(capacity: IntType = 16) -> StringBuilder: ...
    
    @staticmethod
    def GetStringAndRelease(sb: StringBuilder) -> StringType: ...
    
    @staticmethod
    def Release(sb: StringBuilder) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SurrogateEncoder(ObjectType, ISerializable, IObjectReference):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetRealObject(self, context: StreamingContext) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SurrogateEncoder(ObjectType, ISerializable, IObjectReference):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetRealObject(self, context: StreamingContext) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SurrogateEncoder(ObjectType, ISerializable, IObjectReference):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetRealObject(self, context: StreamingContext) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UTF32Encoding(Encoding, ICloneable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, bigEndian: BooleanType, byteOrderMark: BooleanType): ...
    
    @overload
    def __init__(self, bigEndian: BooleanType, byteOrderMark: BooleanType, throwOnInvalidCharacters: BooleanType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Equals(self, value: ObjectType) -> BooleanType: ...
    
    @overload
    def GetByteCount(self, s: StringType) -> IntType: ...
    
    @overload
    def GetByteCount(self, chars: CharType, count: IntType) -> IntType: ...
    
    @overload
    def GetByteCount(self, chars: ArrayType[CharType], index: IntType, count: IntType) -> IntType: ...
    
    @overload
    def GetBytes(self, s: StringType, charIndex: IntType, charCount: IntType, bytes: ArrayType[ByteType], byteIndex: IntType) -> IntType: ...
    
    @overload
    def GetBytes(self, chars: ArrayType[CharType], charIndex: IntType, charCount: IntType, bytes: ArrayType[ByteType], byteIndex: IntType) -> IntType: ...
    
    @overload
    def GetBytes(self, chars: CharType, charCount: IntType, bytes: ByteType, byteCount: IntType) -> IntType: ...
    
    @overload
    def GetCharCount(self, bytes: ByteType, count: IntType) -> IntType: ...
    
    @overload
    def GetCharCount(self, bytes: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    @overload
    def GetChars(self, bytes: ArrayType[ByteType], byteIndex: IntType, byteCount: IntType, chars: ArrayType[CharType], charIndex: IntType) -> IntType: ...
    
    @overload
    def GetChars(self, bytes: ByteType, byteCount: IntType, chars: CharType, charCount: IntType) -> IntType: ...
    
    def GetDecoder(self) -> Decoder: ...
    
    def GetEncoder(self) -> Encoder: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def GetMaxByteCount(self, charCount: IntType) -> IntType: ...
    
    def GetMaxCharCount(self, byteCount: IntType) -> IntType: ...
    
    def GetPreamble(self) -> ArrayType[ByteType]: ...
    
    @overload
    def GetString(self, bytes: ArrayType[ByteType], index: IntType, count: IntType) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UTF32Encoding(Encoding, ICloneable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, bigEndian: BooleanType, byteOrderMark: BooleanType): ...
    
    @overload
    def __init__(self, bigEndian: BooleanType, byteOrderMark: BooleanType, throwOnInvalidCharacters: BooleanType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Equals(self, value: ObjectType) -> BooleanType: ...
    
    @overload
    def GetByteCount(self, s: StringType) -> IntType: ...
    
    @overload
    def GetByteCount(self, chars: CharType, count: IntType) -> IntType: ...
    
    @overload
    def GetByteCount(self, chars: ArrayType[CharType], index: IntType, count: IntType) -> IntType: ...
    
    @overload
    def GetBytes(self, s: StringType, charIndex: IntType, charCount: IntType, bytes: ArrayType[ByteType], byteIndex: IntType) -> IntType: ...
    
    @overload
    def GetBytes(self, chars: ArrayType[CharType], charIndex: IntType, charCount: IntType, bytes: ArrayType[ByteType], byteIndex: IntType) -> IntType: ...
    
    @overload
    def GetBytes(self, chars: CharType, charCount: IntType, bytes: ByteType, byteCount: IntType) -> IntType: ...
    
    @overload
    def GetCharCount(self, bytes: ByteType, count: IntType) -> IntType: ...
    
    @overload
    def GetCharCount(self, bytes: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    @overload
    def GetChars(self, bytes: ArrayType[ByteType], byteIndex: IntType, byteCount: IntType, chars: ArrayType[CharType], charIndex: IntType) -> IntType: ...
    
    @overload
    def GetChars(self, bytes: ByteType, byteCount: IntType, chars: CharType, charCount: IntType) -> IntType: ...
    
    def GetDecoder(self) -> Decoder: ...
    
    def GetEncoder(self) -> Encoder: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def GetMaxByteCount(self, charCount: IntType) -> IntType: ...
    
    def GetMaxCharCount(self, byteCount: IntType) -> IntType: ...
    
    def GetPreamble(self) -> ArrayType[ByteType]: ...
    
    @overload
    def GetString(self, bytes: ArrayType[ByteType], index: IntType, count: IntType) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UTF32Encoding(Encoding, ICloneable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, bigEndian: BooleanType, byteOrderMark: BooleanType): ...
    
    @overload
    def __init__(self, bigEndian: BooleanType, byteOrderMark: BooleanType, throwOnInvalidCharacters: BooleanType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Equals(self, value: ObjectType) -> BooleanType: ...
    
    @overload
    def GetByteCount(self, s: StringType) -> IntType: ...
    
    @overload
    def GetByteCount(self, chars: CharType, count: IntType) -> IntType: ...
    
    @overload
    def GetByteCount(self, chars: ArrayType[CharType], index: IntType, count: IntType) -> IntType: ...
    
    @overload
    def GetBytes(self, s: StringType, charIndex: IntType, charCount: IntType, bytes: ArrayType[ByteType], byteIndex: IntType) -> IntType: ...
    
    @overload
    def GetBytes(self, chars: ArrayType[CharType], charIndex: IntType, charCount: IntType, bytes: ArrayType[ByteType], byteIndex: IntType) -> IntType: ...
    
    @overload
    def GetBytes(self, chars: CharType, charCount: IntType, bytes: ByteType, byteCount: IntType) -> IntType: ...
    
    @overload
    def GetCharCount(self, bytes: ByteType, count: IntType) -> IntType: ...
    
    @overload
    def GetCharCount(self, bytes: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    @overload
    def GetChars(self, bytes: ArrayType[ByteType], byteIndex: IntType, byteCount: IntType, chars: ArrayType[CharType], charIndex: IntType) -> IntType: ...
    
    @overload
    def GetChars(self, bytes: ByteType, byteCount: IntType, chars: CharType, charCount: IntType) -> IntType: ...
    
    def GetDecoder(self) -> Decoder: ...
    
    def GetEncoder(self) -> Encoder: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def GetMaxByteCount(self, charCount: IntType) -> IntType: ...
    
    def GetMaxCharCount(self, byteCount: IntType) -> IntType: ...
    
    def GetPreamble(self) -> ArrayType[ByteType]: ...
    
    @overload
    def GetString(self, bytes: ArrayType[ByteType], index: IntType, count: IntType) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UTF7Encoding(Encoding, ICloneable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, allowOptionals: BooleanType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Equals(self, value: ObjectType) -> BooleanType: ...
    
    @overload
    def GetByteCount(self, s: StringType) -> IntType: ...
    
    @overload
    def GetByteCount(self, chars: CharType, count: IntType) -> IntType: ...
    
    @overload
    def GetByteCount(self, chars: ArrayType[CharType], index: IntType, count: IntType) -> IntType: ...
    
    @overload
    def GetBytes(self, s: StringType, charIndex: IntType, charCount: IntType, bytes: ArrayType[ByteType], byteIndex: IntType) -> IntType: ...
    
    @overload
    def GetBytes(self, chars: ArrayType[CharType], charIndex: IntType, charCount: IntType, bytes: ArrayType[ByteType], byteIndex: IntType) -> IntType: ...
    
    @overload
    def GetBytes(self, chars: CharType, charCount: IntType, bytes: ByteType, byteCount: IntType) -> IntType: ...
    
    @overload
    def GetCharCount(self, bytes: ByteType, count: IntType) -> IntType: ...
    
    @overload
    def GetCharCount(self, bytes: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    @overload
    def GetChars(self, bytes: ArrayType[ByteType], byteIndex: IntType, byteCount: IntType, chars: ArrayType[CharType], charIndex: IntType) -> IntType: ...
    
    @overload
    def GetChars(self, bytes: ByteType, byteCount: IntType, chars: CharType, charCount: IntType) -> IntType: ...
    
    def GetDecoder(self) -> Decoder: ...
    
    def GetEncoder(self) -> Encoder: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def GetMaxByteCount(self, charCount: IntType) -> IntType: ...
    
    def GetMaxCharCount(self, byteCount: IntType) -> IntType: ...
    
    @overload
    def GetString(self, bytes: ArrayType[ByteType], index: IntType, count: IntType) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UTF7Encoding(Encoding, ICloneable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, allowOptionals: BooleanType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Equals(self, value: ObjectType) -> BooleanType: ...
    
    @overload
    def GetByteCount(self, s: StringType) -> IntType: ...
    
    @overload
    def GetByteCount(self, chars: CharType, count: IntType) -> IntType: ...
    
    @overload
    def GetByteCount(self, chars: ArrayType[CharType], index: IntType, count: IntType) -> IntType: ...
    
    @overload
    def GetBytes(self, s: StringType, charIndex: IntType, charCount: IntType, bytes: ArrayType[ByteType], byteIndex: IntType) -> IntType: ...
    
    @overload
    def GetBytes(self, chars: ArrayType[CharType], charIndex: IntType, charCount: IntType, bytes: ArrayType[ByteType], byteIndex: IntType) -> IntType: ...
    
    @overload
    def GetBytes(self, chars: CharType, charCount: IntType, bytes: ByteType, byteCount: IntType) -> IntType: ...
    
    @overload
    def GetCharCount(self, bytes: ByteType, count: IntType) -> IntType: ...
    
    @overload
    def GetCharCount(self, bytes: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    @overload
    def GetChars(self, bytes: ArrayType[ByteType], byteIndex: IntType, byteCount: IntType, chars: ArrayType[CharType], charIndex: IntType) -> IntType: ...
    
    @overload
    def GetChars(self, bytes: ByteType, byteCount: IntType, chars: CharType, charCount: IntType) -> IntType: ...
    
    def GetDecoder(self) -> Decoder: ...
    
    def GetEncoder(self) -> Encoder: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def GetMaxByteCount(self, charCount: IntType) -> IntType: ...
    
    def GetMaxCharCount(self, byteCount: IntType) -> IntType: ...
    
    @overload
    def GetString(self, bytes: ArrayType[ByteType], index: IntType, count: IntType) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UTF7Encoding(Encoding, ICloneable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, allowOptionals: BooleanType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Equals(self, value: ObjectType) -> BooleanType: ...
    
    @overload
    def GetByteCount(self, s: StringType) -> IntType: ...
    
    @overload
    def GetByteCount(self, chars: CharType, count: IntType) -> IntType: ...
    
    @overload
    def GetByteCount(self, chars: ArrayType[CharType], index: IntType, count: IntType) -> IntType: ...
    
    @overload
    def GetBytes(self, s: StringType, charIndex: IntType, charCount: IntType, bytes: ArrayType[ByteType], byteIndex: IntType) -> IntType: ...
    
    @overload
    def GetBytes(self, chars: ArrayType[CharType], charIndex: IntType, charCount: IntType, bytes: ArrayType[ByteType], byteIndex: IntType) -> IntType: ...
    
    @overload
    def GetBytes(self, chars: CharType, charCount: IntType, bytes: ByteType, byteCount: IntType) -> IntType: ...
    
    @overload
    def GetCharCount(self, bytes: ByteType, count: IntType) -> IntType: ...
    
    @overload
    def GetCharCount(self, bytes: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    @overload
    def GetChars(self, bytes: ArrayType[ByteType], byteIndex: IntType, byteCount: IntType, chars: ArrayType[CharType], charIndex: IntType) -> IntType: ...
    
    @overload
    def GetChars(self, bytes: ByteType, byteCount: IntType, chars: CharType, charCount: IntType) -> IntType: ...
    
    def GetDecoder(self) -> Decoder: ...
    
    def GetEncoder(self) -> Encoder: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def GetMaxByteCount(self, charCount: IntType) -> IntType: ...
    
    def GetMaxCharCount(self, byteCount: IntType) -> IntType: ...
    
    @overload
    def GetString(self, bytes: ArrayType[ByteType], index: IntType, count: IntType) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UTF8Encoding(Encoding, ICloneable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, encoderShouldEmitUTF8Identifier: BooleanType): ...
    
    @overload
    def __init__(self, encoderShouldEmitUTF8Identifier: BooleanType, throwOnInvalidBytes: BooleanType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Equals(self, value: ObjectType) -> BooleanType: ...
    
    @overload
    def GetByteCount(self, chars: ArrayType[CharType], index: IntType, count: IntType) -> IntType: ...
    
    @overload
    def GetByteCount(self, chars: StringType) -> IntType: ...
    
    @overload
    def GetByteCount(self, chars: CharType, count: IntType) -> IntType: ...
    
    @overload
    def GetBytes(self, s: StringType, charIndex: IntType, charCount: IntType, bytes: ArrayType[ByteType], byteIndex: IntType) -> IntType: ...
    
    @overload
    def GetBytes(self, chars: ArrayType[CharType], charIndex: IntType, charCount: IntType, bytes: ArrayType[ByteType], byteIndex: IntType) -> IntType: ...
    
    @overload
    def GetBytes(self, chars: CharType, charCount: IntType, bytes: ByteType, byteCount: IntType) -> IntType: ...
    
    @overload
    def GetCharCount(self, bytes: ByteType, count: IntType) -> IntType: ...
    
    @overload
    def GetCharCount(self, bytes: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    @overload
    def GetChars(self, bytes: ArrayType[ByteType], byteIndex: IntType, byteCount: IntType, chars: ArrayType[CharType], charIndex: IntType) -> IntType: ...
    
    @overload
    def GetChars(self, bytes: ByteType, byteCount: IntType, chars: CharType, charCount: IntType) -> IntType: ...
    
    def GetDecoder(self) -> Decoder: ...
    
    def GetEncoder(self) -> Encoder: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def GetMaxByteCount(self, charCount: IntType) -> IntType: ...
    
    def GetMaxCharCount(self, byteCount: IntType) -> IntType: ...
    
    def GetPreamble(self) -> ArrayType[ByteType]: ...
    
    @overload
    def GetString(self, bytes: ArrayType[ByteType], index: IntType, count: IntType) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UTF8Encoding(Encoding, ICloneable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, encoderShouldEmitUTF8Identifier: BooleanType): ...
    
    @overload
    def __init__(self, encoderShouldEmitUTF8Identifier: BooleanType, throwOnInvalidBytes: BooleanType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Equals(self, value: ObjectType) -> BooleanType: ...
    
    @overload
    def GetByteCount(self, chars: ArrayType[CharType], index: IntType, count: IntType) -> IntType: ...
    
    @overload
    def GetByteCount(self, chars: StringType) -> IntType: ...
    
    @overload
    def GetByteCount(self, chars: CharType, count: IntType) -> IntType: ...
    
    @overload
    def GetBytes(self, s: StringType, charIndex: IntType, charCount: IntType, bytes: ArrayType[ByteType], byteIndex: IntType) -> IntType: ...
    
    @overload
    def GetBytes(self, chars: ArrayType[CharType], charIndex: IntType, charCount: IntType, bytes: ArrayType[ByteType], byteIndex: IntType) -> IntType: ...
    
    @overload
    def GetBytes(self, chars: CharType, charCount: IntType, bytes: ByteType, byteCount: IntType) -> IntType: ...
    
    @overload
    def GetCharCount(self, bytes: ByteType, count: IntType) -> IntType: ...
    
    @overload
    def GetCharCount(self, bytes: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    @overload
    def GetChars(self, bytes: ArrayType[ByteType], byteIndex: IntType, byteCount: IntType, chars: ArrayType[CharType], charIndex: IntType) -> IntType: ...
    
    @overload
    def GetChars(self, bytes: ByteType, byteCount: IntType, chars: CharType, charCount: IntType) -> IntType: ...
    
    def GetDecoder(self) -> Decoder: ...
    
    def GetEncoder(self) -> Encoder: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def GetMaxByteCount(self, charCount: IntType) -> IntType: ...
    
    def GetMaxCharCount(self, byteCount: IntType) -> IntType: ...
    
    def GetPreamble(self) -> ArrayType[ByteType]: ...
    
    @overload
    def GetString(self, bytes: ArrayType[ByteType], index: IntType, count: IntType) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UTF8Encoding(Encoding, ICloneable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, encoderShouldEmitUTF8Identifier: BooleanType): ...
    
    @overload
    def __init__(self, encoderShouldEmitUTF8Identifier: BooleanType, throwOnInvalidBytes: BooleanType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Equals(self, value: ObjectType) -> BooleanType: ...
    
    @overload
    def GetByteCount(self, chars: ArrayType[CharType], index: IntType, count: IntType) -> IntType: ...
    
    @overload
    def GetByteCount(self, chars: StringType) -> IntType: ...
    
    @overload
    def GetByteCount(self, chars: CharType, count: IntType) -> IntType: ...
    
    @overload
    def GetBytes(self, s: StringType, charIndex: IntType, charCount: IntType, bytes: ArrayType[ByteType], byteIndex: IntType) -> IntType: ...
    
    @overload
    def GetBytes(self, chars: ArrayType[CharType], charIndex: IntType, charCount: IntType, bytes: ArrayType[ByteType], byteIndex: IntType) -> IntType: ...
    
    @overload
    def GetBytes(self, chars: CharType, charCount: IntType, bytes: ByteType, byteCount: IntType) -> IntType: ...
    
    @overload
    def GetCharCount(self, bytes: ByteType, count: IntType) -> IntType: ...
    
    @overload
    def GetCharCount(self, bytes: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    @overload
    def GetChars(self, bytes: ArrayType[ByteType], byteIndex: IntType, byteCount: IntType, chars: ArrayType[CharType], charIndex: IntType) -> IntType: ...
    
    @overload
    def GetChars(self, bytes: ByteType, byteCount: IntType, chars: CharType, charCount: IntType) -> IntType: ...
    
    def GetDecoder(self) -> Decoder: ...
    
    def GetEncoder(self) -> Encoder: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def GetMaxByteCount(self, charCount: IntType) -> IntType: ...
    
    def GetMaxCharCount(self, byteCount: IntType) -> IntType: ...
    
    def GetPreamble(self) -> ArrayType[ByteType]: ...
    
    @overload
    def GetString(self, bytes: ArrayType[ByteType], index: IntType, count: IntType) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UnicodeEncoding(Encoding, ICloneable):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def CharSize() -> IntType: ...
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, bigEndian: BooleanType, byteOrderMark: BooleanType): ...
    
    @overload
    def __init__(self, bigEndian: BooleanType, byteOrderMark: BooleanType, throwOnInvalidBytes: BooleanType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Equals(self, value: ObjectType) -> BooleanType: ...
    
    @overload
    def GetByteCount(self, s: StringType) -> IntType: ...
    
    @overload
    def GetByteCount(self, chars: CharType, count: IntType) -> IntType: ...
    
    @overload
    def GetByteCount(self, chars: ArrayType[CharType], index: IntType, count: IntType) -> IntType: ...
    
    @overload
    def GetBytes(self, s: StringType, charIndex: IntType, charCount: IntType, bytes: ArrayType[ByteType], byteIndex: IntType) -> IntType: ...
    
    @overload
    def GetBytes(self, chars: ArrayType[CharType], charIndex: IntType, charCount: IntType, bytes: ArrayType[ByteType], byteIndex: IntType) -> IntType: ...
    
    @overload
    def GetBytes(self, chars: CharType, charCount: IntType, bytes: ByteType, byteCount: IntType) -> IntType: ...
    
    @overload
    def GetCharCount(self, bytes: ByteType, count: IntType) -> IntType: ...
    
    @overload
    def GetCharCount(self, bytes: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    @overload
    def GetChars(self, bytes: ArrayType[ByteType], byteIndex: IntType, byteCount: IntType, chars: ArrayType[CharType], charIndex: IntType) -> IntType: ...
    
    @overload
    def GetChars(self, bytes: ByteType, byteCount: IntType, chars: CharType, charCount: IntType) -> IntType: ...
    
    def GetDecoder(self) -> Decoder: ...
    
    def GetEncoder(self) -> Encoder: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def GetMaxByteCount(self, charCount: IntType) -> IntType: ...
    
    def GetMaxCharCount(self, byteCount: IntType) -> IntType: ...
    
    def GetPreamble(self) -> ArrayType[ByteType]: ...
    
    @overload
    def GetString(self, bytes: ArrayType[ByteType], index: IntType, count: IntType) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UnicodeEncoding(Encoding, ICloneable):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def CharSize() -> IntType: ...
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, bigEndian: BooleanType, byteOrderMark: BooleanType): ...
    
    @overload
    def __init__(self, bigEndian: BooleanType, byteOrderMark: BooleanType, throwOnInvalidBytes: BooleanType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Equals(self, value: ObjectType) -> BooleanType: ...
    
    @overload
    def GetByteCount(self, s: StringType) -> IntType: ...
    
    @overload
    def GetByteCount(self, chars: CharType, count: IntType) -> IntType: ...
    
    @overload
    def GetByteCount(self, chars: ArrayType[CharType], index: IntType, count: IntType) -> IntType: ...
    
    @overload
    def GetBytes(self, s: StringType, charIndex: IntType, charCount: IntType, bytes: ArrayType[ByteType], byteIndex: IntType) -> IntType: ...
    
    @overload
    def GetBytes(self, chars: ArrayType[CharType], charIndex: IntType, charCount: IntType, bytes: ArrayType[ByteType], byteIndex: IntType) -> IntType: ...
    
    @overload
    def GetBytes(self, chars: CharType, charCount: IntType, bytes: ByteType, byteCount: IntType) -> IntType: ...
    
    @overload
    def GetCharCount(self, bytes: ByteType, count: IntType) -> IntType: ...
    
    @overload
    def GetCharCount(self, bytes: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    @overload
    def GetChars(self, bytes: ArrayType[ByteType], byteIndex: IntType, byteCount: IntType, chars: ArrayType[CharType], charIndex: IntType) -> IntType: ...
    
    @overload
    def GetChars(self, bytes: ByteType, byteCount: IntType, chars: CharType, charCount: IntType) -> IntType: ...
    
    def GetDecoder(self) -> Decoder: ...
    
    def GetEncoder(self) -> Encoder: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def GetMaxByteCount(self, charCount: IntType) -> IntType: ...
    
    def GetMaxCharCount(self, byteCount: IntType) -> IntType: ...
    
    def GetPreamble(self) -> ArrayType[ByteType]: ...
    
    @overload
    def GetString(self, bytes: ArrayType[ByteType], index: IntType, count: IntType) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UnicodeEncoding(Encoding, ICloneable):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def CharSize() -> IntType: ...
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, bigEndian: BooleanType, byteOrderMark: BooleanType): ...
    
    @overload
    def __init__(self, bigEndian: BooleanType, byteOrderMark: BooleanType, throwOnInvalidBytes: BooleanType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Equals(self, value: ObjectType) -> BooleanType: ...
    
    @overload
    def GetByteCount(self, s: StringType) -> IntType: ...
    
    @overload
    def GetByteCount(self, chars: CharType, count: IntType) -> IntType: ...
    
    @overload
    def GetByteCount(self, chars: ArrayType[CharType], index: IntType, count: IntType) -> IntType: ...
    
    @overload
    def GetBytes(self, s: StringType, charIndex: IntType, charCount: IntType, bytes: ArrayType[ByteType], byteIndex: IntType) -> IntType: ...
    
    @overload
    def GetBytes(self, chars: ArrayType[CharType], charIndex: IntType, charCount: IntType, bytes: ArrayType[ByteType], byteIndex: IntType) -> IntType: ...
    
    @overload
    def GetBytes(self, chars: CharType, charCount: IntType, bytes: ByteType, byteCount: IntType) -> IntType: ...
    
    @overload
    def GetCharCount(self, bytes: ByteType, count: IntType) -> IntType: ...
    
    @overload
    def GetCharCount(self, bytes: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    @overload
    def GetChars(self, bytes: ArrayType[ByteType], byteIndex: IntType, byteCount: IntType, chars: ArrayType[CharType], charIndex: IntType) -> IntType: ...
    
    @overload
    def GetChars(self, bytes: ByteType, byteCount: IntType, chars: CharType, charCount: IntType) -> IntType: ...
    
    def GetDecoder(self) -> Decoder: ...
    
    def GetEncoder(self) -> Encoder: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def GetMaxByteCount(self, charCount: IntType) -> IntType: ...
    
    def GetMaxCharCount(self, byteCount: IntType) -> IntType: ...
    
    def GetPreamble(self) -> ArrayType[ByteType]: ...
    
    @overload
    def GetString(self, bytes: ArrayType[ByteType], index: IntType, count: IntType) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# No Structs

# No Interfaces

# ---------- Enums ---------- #

class ExtendedNormalizationForms(Enum):
    FormC: IntType = 1
    FormD: IntType = 2
    FormKC: IntType = 5
    FormKD: IntType = 6
    FormIdna: IntType = 13
    FormCDisallowUnassigned: IntType = 257
    FormDDisallowUnassigned: IntType = 258
    FormKCDisallowUnassigned: IntType = 261
    FormKDDisallowUnassigned: IntType = 262
    FormIdnaDisallowUnassigned: IntType = 269


class ExtendedNormalizationForms(Enum):
    FormC: IntType = 1
    FormD: IntType = 2
    FormKC: IntType = 5
    FormKD: IntType = 6
    FormIdna: IntType = 13
    FormCDisallowUnassigned: IntType = 257
    FormDDisallowUnassigned: IntType = 258
    FormKCDisallowUnassigned: IntType = 261
    FormKDDisallowUnassigned: IntType = 262
    FormIdnaDisallowUnassigned: IntType = 269


class ExtendedNormalizationForms(Enum):
    FormC: IntType = 1
    FormD: IntType = 2
    FormKC: IntType = 5
    FormKD: IntType = 6
    FormIdna: IntType = 13
    FormCDisallowUnassigned: IntType = 257
    FormDDisallowUnassigned: IntType = 258
    FormKCDisallowUnassigned: IntType = 261
    FormKDDisallowUnassigned: IntType = 262
    FormIdnaDisallowUnassigned: IntType = 269


class NormalizationForm(Enum):
    FormC: IntType = 1
    FormD: IntType = 2
    FormKC: IntType = 5
    FormKD: IntType = 6


class NormalizationForm(Enum):
    FormC: IntType = 1
    FormD: IntType = 2
    FormKC: IntType = 5
    FormKD: IntType = 6


class NormalizationForm(Enum):
    FormC: IntType = 1
    FormD: IntType = 2
    FormKC: IntType = 5
    FormKD: IntType = 6


# No Delegates

__all__ = [
    ASCIIEncoding,
    BaseCodePageEncoding,
    CodePageEncoding,
    DBCSCodePageEncoding,
    Decoder,
    DecoderExceptionFallback,
    DecoderExceptionFallbackBuffer,
    DecoderFallback,
    DecoderFallbackBuffer,
    DecoderFallbackException,
    DecoderNLS,
    DecoderReplacementFallback,
    DecoderReplacementFallbackBuffer,
    EUCJPEncoding,
    Encoder,
    EncoderExceptionFallback,
    EncoderExceptionFallbackBuffer,
    EncoderFallback,
    EncoderFallbackBuffer,
    EncoderFallbackException,
    EncoderNLS,
    EncoderReplacementFallback,
    EncoderReplacementFallbackBuffer,
    Encoding,
    EncodingInfo,
    EncodingNLS,
    EncodingProvider,
    GB18030Encoding,
    ISCIIEncoding,
    ISO2022Encoding,
    InternalDecoderBestFitFallback,
    InternalDecoderBestFitFallbackBuffer,
    InternalEncoderBestFitFallback,
    InternalEncoderBestFitFallbackBuffer,
    Latin1Encoding,
    MLangCodePageEncoding,
    Normalization,
    SBCSCodePageEncoding,
    StringBuilder,
    StringBuilderCache,
    SurrogateEncoder,
    UTF32Encoding,
    UTF7Encoding,
    UTF8Encoding,
    UnicodeEncoding,
    ExtendedNormalizationForms,
    NormalizationForm,
]
