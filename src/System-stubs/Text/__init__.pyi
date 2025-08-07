"""Automatically generated stubs for C# namespace: System.Text."""

from abc import ABC
from typing import ClassVar
from typing import overload

from System import ArgumentException
from System import Array
from System import Boolean
from System import Char
from System import Decimal
from System import Enum
from System import Exception
from System import ICloneable
from System import IFormatProvider
from System import Int32
from System import Object
from System import Type
from System.Collections import IDictionary
from System.Reflection import MethodBase
from System.Runtime.InteropServices import _Exception
from System.Runtime.Serialization import IObjectReference
from System.Runtime.Serialization import ISerializable
from System.Runtime.Serialization import SerializationInfo
from System.Runtime.Serialization import StreamingContext

class ASCIIEncoding(Encoding, ICloneable):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def BodyName(self) -> str:
        """"""
    @property
    def CodePage(self) -> int:
        """"""
    @property
    def DecoderFallback(self) -> DecoderFallback:
        """"""
    @DecoderFallback.setter
    def DecoderFallback(self, value: DecoderFallback) -> None: ...
    @property
    def EncoderFallback(self) -> EncoderFallback:
        """"""
    @EncoderFallback.setter
    def EncoderFallback(self, value: EncoderFallback) -> None: ...
    @property
    def EncodingName(self) -> str:
        """"""
    @property
    def HeaderName(self) -> str:
        """"""
    @property
    def IsBrowserDisplay(self) -> bool:
        """"""
    @property
    def IsBrowserSave(self) -> bool:
        """"""
    @property
    def IsMailNewsDisplay(self) -> bool:
        """"""
    @property
    def IsMailNewsSave(self) -> bool:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def IsSingleByte(self) -> bool:
        """"""
    @property
    def WebName(self) -> str:
        """"""
    @property
    def WindowsCodePage(self) -> int:
        """"""
    def Clone(self) -> object:
        """"""
    def Equals(self, value: object) -> bool:
        """"""
    @overload
    def GetByteCount(self, chars: Array[Char]) -> int:
        """"""
    @overload
    def GetByteCount(self, chars: Array[Char], index: int, count: int) -> int:
        """"""
    @overload
    def GetByteCount(self, chars: Char, count: int) -> int:
        """"""
    @overload
    def GetByteCount(self, chars: str) -> int:
        """"""
    @overload
    def GetBytes(self, chars: Array[Char]) -> Array[int]:
        """"""
    @overload
    def GetBytes(self, chars: Array[Char], index: int, count: int) -> Array[int]:
        """"""
    @overload
    def GetBytes(
        self, chars: Array[Char], charIndex: int, charCount: int, bytes: Array[int], byteIndex: int
    ) -> int:
        """"""
    @overload
    def GetBytes(self, chars: Char, charCount: int, bytes: int, byteCount: int) -> int:
        """"""
    @overload
    def GetBytes(self, s: str) -> Array[int]:
        """"""
    @overload
    def GetBytes(
        self, chars: str, charIndex: int, charCount: int, bytes: Array[int], byteIndex: int
    ) -> int:
        """"""
    @overload
    def GetCharCount(self, bytes: Array[int]) -> int:
        """"""
    @overload
    def GetCharCount(self, bytes: Array[int], index: int, count: int) -> int:
        """"""
    @overload
    def GetCharCount(self, bytes: int, count: int) -> int:
        """"""
    @overload
    def GetChars(self, bytes: Array[int]) -> Array[Char]:
        """"""
    @overload
    def GetChars(self, bytes: Array[int], index: int, count: int) -> Array[Char]:
        """"""
    @overload
    def GetChars(
        self, bytes: Array[int], byteIndex: int, byteCount: int, chars: Array[Char], charIndex: int
    ) -> int:
        """"""
    @overload
    def GetChars(self, bytes: int, byteCount: int, chars: Char, charCount: int) -> int:
        """"""
    def GetDecoder(self) -> Decoder:
        """"""
    def GetEncoder(self) -> Encoder:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetMaxByteCount(self, charCount: int) -> int:
        """"""
    def GetMaxCharCount(self, byteCount: int) -> int:
        """"""
    def GetPreamble(self) -> Array[int]:
        """"""
    @overload
    def GetString(self, bytes: Array[int]) -> str:
        """"""
    @overload
    def GetString(self, bytes: Array[int], byteIndex: int, byteCount: int) -> str:
        """"""
    @overload
    def GetString(self, bytes: int, byteCount: int) -> str:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IsAlwaysNormalized(self) -> bool:
        """"""
    @overload
    def IsAlwaysNormalized(self, form: NormalizationForm) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

class BaseCodePageEncoding(ABC, EncodingNLS, ISerializable, ICloneable):
    """"""
    @property
    def BodyName(self) -> str:
        """"""
    @property
    def CodePage(self) -> int:
        """"""
    @property
    def DecoderFallback(self) -> DecoderFallback:
        """"""
    @DecoderFallback.setter
    def DecoderFallback(self, value: DecoderFallback) -> None: ...
    @property
    def EncoderFallback(self) -> EncoderFallback:
        """"""
    @EncoderFallback.setter
    def EncoderFallback(self, value: EncoderFallback) -> None: ...
    @property
    def EncodingName(self) -> str:
        """"""
    @property
    def HeaderName(self) -> str:
        """"""
    @property
    def IsBrowserDisplay(self) -> bool:
        """"""
    @property
    def IsBrowserSave(self) -> bool:
        """"""
    @property
    def IsMailNewsDisplay(self) -> bool:
        """"""
    @property
    def IsMailNewsSave(self) -> bool:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def IsSingleByte(self) -> bool:
        """"""
    @property
    def WebName(self) -> str:
        """"""
    @property
    def WindowsCodePage(self) -> int:
        """"""
    def Clone(self) -> object:
        """"""
    def Equals(self, value: object) -> bool:
        """"""
    @overload
    def GetByteCount(self, chars: Array[Char]) -> int:
        """"""
    @overload
    def GetByteCount(self, chars: Array[Char], index: int, count: int) -> int:
        """"""
    @overload
    def GetByteCount(self, chars: Char, count: int) -> int:
        """"""
    @overload
    def GetByteCount(self, s: str) -> int:
        """"""
    @overload
    def GetBytes(self, chars: Array[Char]) -> Array[int]:
        """"""
    @overload
    def GetBytes(self, chars: Array[Char], index: int, count: int) -> Array[int]:
        """"""
    @overload
    def GetBytes(
        self, chars: Array[Char], charIndex: int, charCount: int, bytes: Array[int], byteIndex: int
    ) -> int:
        """"""
    @overload
    def GetBytes(self, chars: Char, charCount: int, bytes: int, byteCount: int) -> int:
        """"""
    @overload
    def GetBytes(self, s: str) -> Array[int]:
        """"""
    @overload
    def GetBytes(
        self, s: str, charIndex: int, charCount: int, bytes: Array[int], byteIndex: int
    ) -> int:
        """"""
    @overload
    def GetCharCount(self, bytes: Array[int]) -> int:
        """"""
    @overload
    def GetCharCount(self, bytes: Array[int], index: int, count: int) -> int:
        """"""
    @overload
    def GetCharCount(self, bytes: int, count: int) -> int:
        """"""
    @overload
    def GetChars(self, bytes: Array[int]) -> Array[Char]:
        """"""
    @overload
    def GetChars(self, bytes: Array[int], index: int, count: int) -> Array[Char]:
        """"""
    @overload
    def GetChars(
        self, bytes: Array[int], byteIndex: int, byteCount: int, chars: Array[Char], charIndex: int
    ) -> int:
        """"""
    @overload
    def GetChars(self, bytes: int, byteCount: int, chars: Char, charCount: int) -> int:
        """"""
    def GetDecoder(self) -> Decoder:
        """"""
    def GetEncoder(self) -> Encoder:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetMaxByteCount(self, charCount: int) -> int:
        """"""
    def GetMaxCharCount(self, byteCount: int) -> int:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetPreamble(self) -> Array[int]:
        """"""
    @overload
    def GetString(self, bytes: Array[int]) -> str:
        """"""
    @overload
    def GetString(self, bytes: Array[int], index: int, count: int) -> str:
        """"""
    @overload
    def GetString(self, bytes: int, byteCount: int) -> str:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IsAlwaysNormalized(self) -> bool:
        """"""
    @overload
    def IsAlwaysNormalized(self, form: NormalizationForm) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

class CodePageEncoding(Object, IObjectReference, ISerializable):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetRealObject(self, context: StreamingContext) -> object:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class DBCSCodePageEncoding(BaseCodePageEncoding, ISerializable, ICloneable):
    """"""
    def __init__(self, codePage: int) -> None:
        """"""
    @property
    def BodyName(self) -> str:
        """"""
    @property
    def CodePage(self) -> int:
        """"""
    @property
    def DecoderFallback(self) -> DecoderFallback:
        """"""
    @DecoderFallback.setter
    def DecoderFallback(self, value: DecoderFallback) -> None: ...
    @property
    def EncoderFallback(self) -> EncoderFallback:
        """"""
    @EncoderFallback.setter
    def EncoderFallback(self, value: EncoderFallback) -> None: ...
    @property
    def EncodingName(self) -> str:
        """"""
    @property
    def HeaderName(self) -> str:
        """"""
    @property
    def IsBrowserDisplay(self) -> bool:
        """"""
    @property
    def IsBrowserSave(self) -> bool:
        """"""
    @property
    def IsMailNewsDisplay(self) -> bool:
        """"""
    @property
    def IsMailNewsSave(self) -> bool:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def IsSingleByte(self) -> bool:
        """"""
    @property
    def WebName(self) -> str:
        """"""
    @property
    def WindowsCodePage(self) -> int:
        """"""
    def Clone(self) -> object:
        """"""
    def Equals(self, value: object) -> bool:
        """"""
    @overload
    def GetByteCount(self, chars: Array[Char]) -> int:
        """"""
    @overload
    def GetByteCount(self, chars: Array[Char], index: int, count: int) -> int:
        """"""
    @overload
    def GetByteCount(self, chars: Char, count: int) -> int:
        """"""
    @overload
    def GetByteCount(self, s: str) -> int:
        """"""
    @overload
    def GetBytes(self, chars: Array[Char]) -> Array[int]:
        """"""
    @overload
    def GetBytes(self, chars: Array[Char], index: int, count: int) -> Array[int]:
        """"""
    @overload
    def GetBytes(
        self, chars: Array[Char], charIndex: int, charCount: int, bytes: Array[int], byteIndex: int
    ) -> int:
        """"""
    @overload
    def GetBytes(self, chars: Char, charCount: int, bytes: int, byteCount: int) -> int:
        """"""
    @overload
    def GetBytes(self, s: str) -> Array[int]:
        """"""
    @overload
    def GetBytes(
        self, s: str, charIndex: int, charCount: int, bytes: Array[int], byteIndex: int
    ) -> int:
        """"""
    @overload
    def GetCharCount(self, bytes: Array[int]) -> int:
        """"""
    @overload
    def GetCharCount(self, bytes: Array[int], index: int, count: int) -> int:
        """"""
    @overload
    def GetCharCount(self, bytes: int, count: int) -> int:
        """"""
    @overload
    def GetChars(self, bytes: Array[int]) -> Array[Char]:
        """"""
    @overload
    def GetChars(self, bytes: Array[int], index: int, count: int) -> Array[Char]:
        """"""
    @overload
    def GetChars(
        self, bytes: Array[int], byteIndex: int, byteCount: int, chars: Array[Char], charIndex: int
    ) -> int:
        """"""
    @overload
    def GetChars(self, bytes: int, byteCount: int, chars: Char, charCount: int) -> int:
        """"""
    def GetDecoder(self) -> Decoder:
        """"""
    def GetEncoder(self) -> Encoder:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetMaxByteCount(self, charCount: int) -> int:
        """"""
    def GetMaxCharCount(self, byteCount: int) -> int:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetPreamble(self) -> Array[int]:
        """"""
    @overload
    def GetString(self, bytes: Array[int]) -> str:
        """"""
    @overload
    def GetString(self, bytes: Array[int], index: int, count: int) -> str:
        """"""
    @overload
    def GetString(self, bytes: int, byteCount: int) -> str:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IsAlwaysNormalized(self) -> bool:
        """"""
    @overload
    def IsAlwaysNormalized(self, form: NormalizationForm) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

class Decoder(ABC, Object):
    """"""
    @property
    def Fallback(self) -> DecoderFallback:
        """"""
    @Fallback.setter
    def Fallback(self, value: DecoderFallback) -> None: ...
    @property
    def FallbackBuffer(self) -> DecoderFallbackBuffer:
        """"""
    @overload
    def Convert(
        self,
        bytes: Array[int],
        byteIndex: int,
        byteCount: int,
        chars: Array[Char],
        charIndex: int,
        charCount: int,
        flush: bool,
        bytesUsed: Int32,
        charsUsed: Int32,
        completed: Boolean,
    ) -> tuple[None, Int32, Int32, Boolean]:
        """"""
    @overload
    def Convert(
        self,
        bytes: int,
        byteCount: int,
        chars: Char,
        charCount: int,
        flush: bool,
        bytesUsed: Int32,
        charsUsed: Int32,
        completed: Boolean,
    ) -> tuple[None, Int32, Int32, Boolean]:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetCharCount(self, bytes: Array[int], index: int, count: int) -> int:
        """"""
    @overload
    def GetCharCount(self, bytes: Array[int], index: int, count: int, flush: bool) -> int:
        """"""
    @overload
    def GetCharCount(self, bytes: int, count: int, flush: bool) -> int:
        """"""
    @overload
    def GetChars(
        self, bytes: Array[int], byteIndex: int, byteCount: int, chars: Array[Char], charIndex: int
    ) -> int:
        """"""
    @overload
    def GetChars(
        self,
        bytes: Array[int],
        byteIndex: int,
        byteCount: int,
        chars: Array[Char],
        charIndex: int,
        flush: bool,
    ) -> int:
        """"""
    @overload
    def GetChars(self, bytes: int, byteCount: int, chars: Char, charCount: int, flush: bool) -> int:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class DecoderExceptionFallback(DecoderFallback):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def MaxCharCount(self) -> int:
        """"""
    def CreateFallbackBuffer(self) -> DecoderFallbackBuffer:
        """"""
    def Equals(self, value: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class DecoderExceptionFallbackBuffer(DecoderFallbackBuffer):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Remaining(self) -> int:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Fallback(self, bytesUnknown: Array[int], index: int) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetNextChar(self) -> Char:
        """"""
    def GetType(self) -> Type:
        """"""
    def MovePrevious(self) -> bool:
        """"""
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class DecoderFallback(ABC, Object):
    """"""
    @classmethod
    @property
    def ExceptionFallback(cls) -> DecoderFallback:
        """"""
    @property
    def MaxCharCount(self) -> int:
        """"""
    @classmethod
    @property
    def ReplacementFallback(cls) -> DecoderFallback:
        """"""
    def CreateFallbackBuffer(self) -> DecoderFallbackBuffer:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class DecoderFallbackBuffer(ABC, Object):
    """"""
    @property
    def Remaining(self) -> int:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Fallback(self, bytesUnknown: Array[int], index: int) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetNextChar(self) -> Char:
        """"""
    def GetType(self) -> Type:
        """"""
    def MovePrevious(self) -> bool:
        """"""
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class DecoderFallbackException(ArgumentException, _Exception, ISerializable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, message: str) -> None:
        """"""
    @overload
    def __init__(self, message: str, innerException: Exception) -> None:
        """"""
    @overload
    def __init__(self, message: str, bytesUnknown: Array[int], index: int) -> None:
        """"""
    @property
    def BytesUnknown(self) -> Array[int]:
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
    def Index(self) -> int:
        """"""
    @property
    def InnerException(self) -> Exception:
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

class DecoderNLS(Decoder, ISerializable):
    """"""
    @property
    def Fallback(self) -> DecoderFallback:
        """"""
    @Fallback.setter
    def Fallback(self, value: DecoderFallback) -> None: ...
    @property
    def FallbackBuffer(self) -> DecoderFallbackBuffer:
        """"""
    @property
    def MustFlush(self) -> bool:
        """"""
    @overload
    def Convert(
        self,
        bytes: Array[int],
        byteIndex: int,
        byteCount: int,
        chars: Array[Char],
        charIndex: int,
        charCount: int,
        flush: bool,
        bytesUsed: Int32,
        charsUsed: Int32,
        completed: Boolean,
    ) -> tuple[None, Int32, Int32, Boolean]:
        """"""
    @overload
    def Convert(
        self,
        bytes: int,
        byteCount: int,
        chars: Char,
        charCount: int,
        flush: bool,
        bytesUsed: Int32,
        charsUsed: Int32,
        completed: Boolean,
    ) -> tuple[None, Int32, Int32, Boolean]:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetCharCount(self, bytes: Array[int], index: int, count: int) -> int:
        """"""
    @overload
    def GetCharCount(self, bytes: Array[int], index: int, count: int, flush: bool) -> int:
        """"""
    @overload
    def GetCharCount(self, bytes: int, count: int, flush: bool) -> int:
        """"""
    @overload
    def GetChars(
        self, bytes: Array[int], byteIndex: int, byteCount: int, chars: Array[Char], charIndex: int
    ) -> int:
        """"""
    @overload
    def GetChars(
        self,
        bytes: Array[int],
        byteIndex: int,
        byteCount: int,
        chars: Array[Char],
        charIndex: int,
        flush: bool,
    ) -> int:
        """"""
    @overload
    def GetChars(self, bytes: int, byteCount: int, chars: Char, charCount: int, flush: bool) -> int:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class DecoderReplacementFallback(DecoderFallback):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, replacement: str) -> None:
        """"""
    @property
    def DefaultString(self) -> str:
        """"""
    @property
    def MaxCharCount(self) -> int:
        """"""
    def CreateFallbackBuffer(self) -> DecoderFallbackBuffer:
        """"""
    def Equals(self, value: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class DecoderReplacementFallbackBuffer(DecoderFallbackBuffer):
    """"""
    def __init__(self, fallback: DecoderReplacementFallback) -> None:
        """"""
    @property
    def Remaining(self) -> int:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Fallback(self, bytesUnknown: Array[int], index: int) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetNextChar(self) -> Char:
        """"""
    def GetType(self) -> Type:
        """"""
    def MovePrevious(self) -> bool:
        """"""
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class EUCJPEncoding(DBCSCodePageEncoding, ISerializable, ICloneable):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def BodyName(self) -> str:
        """"""
    @property
    def CodePage(self) -> int:
        """"""
    @property
    def DecoderFallback(self) -> DecoderFallback:
        """"""
    @DecoderFallback.setter
    def DecoderFallback(self, value: DecoderFallback) -> None: ...
    @property
    def EncoderFallback(self) -> EncoderFallback:
        """"""
    @EncoderFallback.setter
    def EncoderFallback(self, value: EncoderFallback) -> None: ...
    @property
    def EncodingName(self) -> str:
        """"""
    @property
    def HeaderName(self) -> str:
        """"""
    @property
    def IsBrowserDisplay(self) -> bool:
        """"""
    @property
    def IsBrowserSave(self) -> bool:
        """"""
    @property
    def IsMailNewsDisplay(self) -> bool:
        """"""
    @property
    def IsMailNewsSave(self) -> bool:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def IsSingleByte(self) -> bool:
        """"""
    @property
    def WebName(self) -> str:
        """"""
    @property
    def WindowsCodePage(self) -> int:
        """"""
    def Clone(self) -> object:
        """"""
    def Equals(self, value: object) -> bool:
        """"""
    @overload
    def GetByteCount(self, chars: Array[Char]) -> int:
        """"""
    @overload
    def GetByteCount(self, chars: Array[Char], index: int, count: int) -> int:
        """"""
    @overload
    def GetByteCount(self, chars: Char, count: int) -> int:
        """"""
    @overload
    def GetByteCount(self, s: str) -> int:
        """"""
    @overload
    def GetBytes(self, chars: Array[Char]) -> Array[int]:
        """"""
    @overload
    def GetBytes(self, chars: Array[Char], index: int, count: int) -> Array[int]:
        """"""
    @overload
    def GetBytes(
        self, chars: Array[Char], charIndex: int, charCount: int, bytes: Array[int], byteIndex: int
    ) -> int:
        """"""
    @overload
    def GetBytes(self, chars: Char, charCount: int, bytes: int, byteCount: int) -> int:
        """"""
    @overload
    def GetBytes(self, s: str) -> Array[int]:
        """"""
    @overload
    def GetBytes(
        self, s: str, charIndex: int, charCount: int, bytes: Array[int], byteIndex: int
    ) -> int:
        """"""
    @overload
    def GetCharCount(self, bytes: Array[int]) -> int:
        """"""
    @overload
    def GetCharCount(self, bytes: Array[int], index: int, count: int) -> int:
        """"""
    @overload
    def GetCharCount(self, bytes: int, count: int) -> int:
        """"""
    @overload
    def GetChars(self, bytes: Array[int]) -> Array[Char]:
        """"""
    @overload
    def GetChars(self, bytes: Array[int], index: int, count: int) -> Array[Char]:
        """"""
    @overload
    def GetChars(
        self, bytes: Array[int], byteIndex: int, byteCount: int, chars: Array[Char], charIndex: int
    ) -> int:
        """"""
    @overload
    def GetChars(self, bytes: int, byteCount: int, chars: Char, charCount: int) -> int:
        """"""
    def GetDecoder(self) -> Decoder:
        """"""
    def GetEncoder(self) -> Encoder:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetMaxByteCount(self, charCount: int) -> int:
        """"""
    def GetMaxCharCount(self, byteCount: int) -> int:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetPreamble(self) -> Array[int]:
        """"""
    @overload
    def GetString(self, bytes: Array[int]) -> str:
        """"""
    @overload
    def GetString(self, bytes: Array[int], index: int, count: int) -> str:
        """"""
    @overload
    def GetString(self, bytes: int, byteCount: int) -> str:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IsAlwaysNormalized(self) -> bool:
        """"""
    @overload
    def IsAlwaysNormalized(self, form: NormalizationForm) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

class Encoder(ABC, Object):
    """"""
    @property
    def Fallback(self) -> EncoderFallback:
        """"""
    @Fallback.setter
    def Fallback(self, value: EncoderFallback) -> None: ...
    @property
    def FallbackBuffer(self) -> EncoderFallbackBuffer:
        """"""
    @overload
    def Convert(
        self,
        chars: Array[Char],
        charIndex: int,
        charCount: int,
        bytes: Array[int],
        byteIndex: int,
        byteCount: int,
        flush: bool,
        charsUsed: Int32,
        bytesUsed: Int32,
        completed: Boolean,
    ) -> tuple[None, Int32, Int32, Boolean]:
        """"""
    @overload
    def Convert(
        self,
        chars: Char,
        charCount: int,
        bytes: int,
        byteCount: int,
        flush: bool,
        charsUsed: Int32,
        bytesUsed: Int32,
        completed: Boolean,
    ) -> tuple[None, Int32, Int32, Boolean]:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetByteCount(self, chars: Array[Char], index: int, count: int, flush: bool) -> int:
        """"""
    @overload
    def GetByteCount(self, chars: Char, count: int, flush: bool) -> int:
        """"""
    @overload
    def GetBytes(
        self,
        chars: Array[Char],
        charIndex: int,
        charCount: int,
        bytes: Array[int],
        byteIndex: int,
        flush: bool,
    ) -> int:
        """"""
    @overload
    def GetBytes(self, chars: Char, charCount: int, bytes: int, byteCount: int, flush: bool) -> int:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class EncoderExceptionFallback(EncoderFallback):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def MaxCharCount(self) -> int:
        """"""
    def CreateFallbackBuffer(self) -> EncoderFallbackBuffer:
        """"""
    def Equals(self, value: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class EncoderExceptionFallbackBuffer(EncoderFallbackBuffer):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Remaining(self) -> int:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Fallback(self, charUnknownHigh: Char, charUnknownLow: Char, index: int) -> bool:
        """"""
    @overload
    def Fallback(self, charUnknown: Char, index: int) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetNextChar(self) -> Char:
        """"""
    def GetType(self) -> Type:
        """"""
    def MovePrevious(self) -> bool:
        """"""
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class EncoderFallback(ABC, Object):
    """"""
    @classmethod
    @property
    def ExceptionFallback(cls) -> EncoderFallback:
        """"""
    @property
    def MaxCharCount(self) -> int:
        """"""
    @classmethod
    @property
    def ReplacementFallback(cls) -> EncoderFallback:
        """"""
    def CreateFallbackBuffer(self) -> EncoderFallbackBuffer:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class EncoderFallbackBuffer(ABC, Object):
    """"""
    @property
    def Remaining(self) -> int:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Fallback(self, charUnknownHigh: Char, charUnknownLow: Char, index: int) -> bool:
        """"""
    @overload
    def Fallback(self, charUnknown: Char, index: int) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetNextChar(self) -> Char:
        """"""
    def GetType(self) -> Type:
        """"""
    def MovePrevious(self) -> bool:
        """"""
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class EncoderFallbackException(ArgumentException, _Exception, ISerializable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, message: str) -> None:
        """"""
    @overload
    def __init__(self, message: str, innerException: Exception) -> None:
        """"""
    @property
    def CharUnknown(self) -> Char:
        """"""
    @property
    def CharUnknownHigh(self) -> Char:
        """"""
    @property
    def CharUnknownLow(self) -> Char:
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
    def Index(self) -> int:
        """"""
    @property
    def InnerException(self) -> Exception:
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
    def IsUnknownSurrogate(self) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

class EncoderNLS(Encoder, ISerializable):
    """"""
    @property
    def Encoding(self) -> Encoding:
        """"""
    @property
    def Fallback(self) -> EncoderFallback:
        """"""
    @Fallback.setter
    def Fallback(self, value: EncoderFallback) -> None: ...
    @property
    def FallbackBuffer(self) -> EncoderFallbackBuffer:
        """"""
    @property
    def MustFlush(self) -> bool:
        """"""
    @overload
    def Convert(
        self,
        chars: Array[Char],
        charIndex: int,
        charCount: int,
        bytes: Array[int],
        byteIndex: int,
        byteCount: int,
        flush: bool,
        charsUsed: Int32,
        bytesUsed: Int32,
        completed: Boolean,
    ) -> tuple[None, Int32, Int32, Boolean]:
        """"""
    @overload
    def Convert(
        self,
        chars: Char,
        charCount: int,
        bytes: int,
        byteCount: int,
        flush: bool,
        charsUsed: Int32,
        bytesUsed: Int32,
        completed: Boolean,
    ) -> tuple[None, Int32, Int32, Boolean]:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetByteCount(self, chars: Array[Char], index: int, count: int, flush: bool) -> int:
        """"""
    @overload
    def GetByteCount(self, chars: Char, count: int, flush: bool) -> int:
        """"""
    @overload
    def GetBytes(
        self,
        chars: Array[Char],
        charIndex: int,
        charCount: int,
        bytes: Array[int],
        byteIndex: int,
        flush: bool,
    ) -> int:
        """"""
    @overload
    def GetBytes(self, chars: Char, charCount: int, bytes: int, byteCount: int, flush: bool) -> int:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class EncoderReplacementFallback(EncoderFallback):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, replacement: str) -> None:
        """"""
    @property
    def DefaultString(self) -> str:
        """"""
    @property
    def MaxCharCount(self) -> int:
        """"""
    def CreateFallbackBuffer(self) -> EncoderFallbackBuffer:
        """"""
    def Equals(self, value: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class EncoderReplacementFallbackBuffer(EncoderFallbackBuffer):
    """"""
    def __init__(self, fallback: EncoderReplacementFallback) -> None:
        """"""
    @property
    def Remaining(self) -> int:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Fallback(self, charUnknownHigh: Char, charUnknownLow: Char, index: int) -> bool:
        """"""
    @overload
    def Fallback(self, charUnknown: Char, index: int) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetNextChar(self) -> Char:
        """"""
    def GetType(self) -> Type:
        """"""
    def MovePrevious(self) -> bool:
        """"""
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class Encoding(ABC, Object, ICloneable):
    """"""
    @classmethod
    @property
    def ASCII(cls) -> Encoding:
        """"""
    @classmethod
    @property
    def BigEndianUnicode(cls) -> Encoding:
        """"""
    @property
    def BodyName(self) -> str:
        """"""
    @property
    def CodePage(self) -> int:
        """"""
    @property
    def DecoderFallback(self) -> DecoderFallback:
        """"""
    @DecoderFallback.setter
    def DecoderFallback(self, value: DecoderFallback) -> None: ...
    @classmethod
    @property
    def Default(cls) -> Encoding:
        """"""
    @property
    def EncoderFallback(self) -> EncoderFallback:
        """"""
    @EncoderFallback.setter
    def EncoderFallback(self, value: EncoderFallback) -> None: ...
    @property
    def EncodingName(self) -> str:
        """"""
    @property
    def HeaderName(self) -> str:
        """"""
    @property
    def IsBrowserDisplay(self) -> bool:
        """"""
    @property
    def IsBrowserSave(self) -> bool:
        """"""
    @property
    def IsMailNewsDisplay(self) -> bool:
        """"""
    @property
    def IsMailNewsSave(self) -> bool:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def IsSingleByte(self) -> bool:
        """"""
    @classmethod
    @property
    def UTF32(cls) -> Encoding:
        """"""
    @classmethod
    @property
    def UTF7(cls) -> Encoding:
        """"""
    @classmethod
    @property
    def UTF8(cls) -> Encoding:
        """"""
    @classmethod
    @property
    def Unicode(cls) -> Encoding:
        """"""
    @property
    def WebName(self) -> str:
        """"""
    @property
    def WindowsCodePage(self) -> int:
        """"""
    def Clone(self) -> object:
        """"""
    @classmethod
    @overload
    def Convert(cls, srcEncoding: Encoding, dstEncoding: Encoding, bytes: Array[int]) -> Array[int]:
        """"""
    @classmethod
    @overload
    def Convert(
        cls, srcEncoding: Encoding, dstEncoding: Encoding, bytes: Array[int], index: int, count: int
    ) -> Array[int]:
        """"""
    def Equals(self, value: object) -> bool:
        """"""
    @overload
    def GetByteCount(self, chars: Array[Char]) -> int:
        """"""
    @overload
    def GetByteCount(self, chars: Array[Char], index: int, count: int) -> int:
        """"""
    @overload
    def GetByteCount(self, chars: Char, count: int) -> int:
        """"""
    @overload
    def GetByteCount(self, s: str) -> int:
        """"""
    @overload
    def GetBytes(self, chars: Array[Char]) -> Array[int]:
        """"""
    @overload
    def GetBytes(self, chars: Array[Char], index: int, count: int) -> Array[int]:
        """"""
    @overload
    def GetBytes(
        self, chars: Array[Char], charIndex: int, charCount: int, bytes: Array[int], byteIndex: int
    ) -> int:
        """"""
    @overload
    def GetBytes(self, chars: Char, charCount: int, bytes: int, byteCount: int) -> int:
        """"""
    @overload
    def GetBytes(self, s: str) -> Array[int]:
        """"""
    @overload
    def GetBytes(
        self, s: str, charIndex: int, charCount: int, bytes: Array[int], byteIndex: int
    ) -> int:
        """"""
    @overload
    def GetCharCount(self, bytes: Array[int]) -> int:
        """"""
    @overload
    def GetCharCount(self, bytes: Array[int], index: int, count: int) -> int:
        """"""
    @overload
    def GetCharCount(self, bytes: int, count: int) -> int:
        """"""
    @overload
    def GetChars(self, bytes: Array[int]) -> Array[Char]:
        """"""
    @overload
    def GetChars(self, bytes: Array[int], index: int, count: int) -> Array[Char]:
        """"""
    @overload
    def GetChars(
        self, bytes: Array[int], byteIndex: int, byteCount: int, chars: Array[Char], charIndex: int
    ) -> int:
        """"""
    @overload
    def GetChars(self, bytes: int, byteCount: int, chars: Char, charCount: int) -> int:
        """"""
    def GetDecoder(self) -> Decoder:
        """"""
    def GetEncoder(self) -> Encoder:
        """"""
    @classmethod
    @overload
    def GetEncoding(cls, codepage: int) -> Encoding:
        """"""
    @classmethod
    @overload
    def GetEncoding(
        cls, codepage: int, encoderFallback: EncoderFallback, decoderFallback: DecoderFallback
    ) -> Encoding:
        """"""
    @classmethod
    @overload
    def GetEncoding(cls, name: str) -> Encoding:
        """"""
    @classmethod
    @overload
    def GetEncoding(
        cls, name: str, encoderFallback: EncoderFallback, decoderFallback: DecoderFallback
    ) -> Encoding:
        """"""
    @classmethod
    def GetEncodings(cls) -> Array[EncodingInfo]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetMaxByteCount(self, charCount: int) -> int:
        """"""
    def GetMaxCharCount(self, byteCount: int) -> int:
        """"""
    def GetPreamble(self) -> Array[int]:
        """"""
    @overload
    def GetString(self, bytes: Array[int]) -> str:
        """"""
    @overload
    def GetString(self, bytes: Array[int], index: int, count: int) -> str:
        """"""
    @overload
    def GetString(self, bytes: int, byteCount: int) -> str:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IsAlwaysNormalized(self) -> bool:
        """"""
    @overload
    def IsAlwaysNormalized(self, form: NormalizationForm) -> bool:
        """"""
    @classmethod
    def RegisterProvider(cls, provider: EncodingProvider) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class EncodingInfo(Object):
    """"""
    @property
    def CodePage(self) -> int:
        """"""
    @property
    def DisplayName(self) -> str:
        """"""
    @property
    def Name(self) -> str:
        """"""
    def Equals(self, value: object) -> bool:
        """"""
    def GetEncoding(self) -> Encoding:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class EncodingNLS(ABC, Encoding, ICloneable):
    """"""
    @property
    def BodyName(self) -> str:
        """"""
    @property
    def CodePage(self) -> int:
        """"""
    @property
    def DecoderFallback(self) -> DecoderFallback:
        """"""
    @DecoderFallback.setter
    def DecoderFallback(self, value: DecoderFallback) -> None: ...
    @property
    def EncoderFallback(self) -> EncoderFallback:
        """"""
    @EncoderFallback.setter
    def EncoderFallback(self, value: EncoderFallback) -> None: ...
    @property
    def EncodingName(self) -> str:
        """"""
    @property
    def HeaderName(self) -> str:
        """"""
    @property
    def IsBrowserDisplay(self) -> bool:
        """"""
    @property
    def IsBrowserSave(self) -> bool:
        """"""
    @property
    def IsMailNewsDisplay(self) -> bool:
        """"""
    @property
    def IsMailNewsSave(self) -> bool:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def IsSingleByte(self) -> bool:
        """"""
    @property
    def WebName(self) -> str:
        """"""
    @property
    def WindowsCodePage(self) -> int:
        """"""
    def Clone(self) -> object:
        """"""
    def Equals(self, value: object) -> bool:
        """"""
    @overload
    def GetByteCount(self, chars: Array[Char]) -> int:
        """"""
    @overload
    def GetByteCount(self, chars: Array[Char], index: int, count: int) -> int:
        """"""
    @overload
    def GetByteCount(self, chars: Char, count: int) -> int:
        """"""
    @overload
    def GetByteCount(self, s: str) -> int:
        """"""
    @overload
    def GetBytes(self, chars: Array[Char]) -> Array[int]:
        """"""
    @overload
    def GetBytes(self, chars: Array[Char], index: int, count: int) -> Array[int]:
        """"""
    @overload
    def GetBytes(
        self, chars: Array[Char], charIndex: int, charCount: int, bytes: Array[int], byteIndex: int
    ) -> int:
        """"""
    @overload
    def GetBytes(self, chars: Char, charCount: int, bytes: int, byteCount: int) -> int:
        """"""
    @overload
    def GetBytes(self, s: str) -> Array[int]:
        """"""
    @overload
    def GetBytes(
        self, s: str, charIndex: int, charCount: int, bytes: Array[int], byteIndex: int
    ) -> int:
        """"""
    @overload
    def GetCharCount(self, bytes: Array[int]) -> int:
        """"""
    @overload
    def GetCharCount(self, bytes: Array[int], index: int, count: int) -> int:
        """"""
    @overload
    def GetCharCount(self, bytes: int, count: int) -> int:
        """"""
    @overload
    def GetChars(self, bytes: Array[int]) -> Array[Char]:
        """"""
    @overload
    def GetChars(self, bytes: Array[int], index: int, count: int) -> Array[Char]:
        """"""
    @overload
    def GetChars(
        self, bytes: Array[int], byteIndex: int, byteCount: int, chars: Array[Char], charIndex: int
    ) -> int:
        """"""
    @overload
    def GetChars(self, bytes: int, byteCount: int, chars: Char, charCount: int) -> int:
        """"""
    def GetDecoder(self) -> Decoder:
        """"""
    def GetEncoder(self) -> Encoder:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetMaxByteCount(self, charCount: int) -> int:
        """"""
    def GetMaxCharCount(self, byteCount: int) -> int:
        """"""
    def GetPreamble(self) -> Array[int]:
        """"""
    @overload
    def GetString(self, bytes: Array[int]) -> str:
        """"""
    @overload
    def GetString(self, bytes: Array[int], index: int, count: int) -> str:
        """"""
    @overload
    def GetString(self, bytes: int, byteCount: int) -> str:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IsAlwaysNormalized(self) -> bool:
        """"""
    @overload
    def IsAlwaysNormalized(self, form: NormalizationForm) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

class EncodingProvider(ABC, Object):
    """"""
    def __init__(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetEncoding(self, codepage: int) -> Encoding:
        """"""
    @overload
    def GetEncoding(
        self, codepage: int, encoderFallback: EncoderFallback, decoderFallback: DecoderFallback
    ) -> Encoding:
        """"""
    @overload
    def GetEncoding(self, name: str) -> Encoding:
        """"""
    @overload
    def GetEncoding(
        self, name: str, encoderFallback: EncoderFallback, decoderFallback: DecoderFallback
    ) -> Encoding:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ExtendedNormalizationForms(Enum):
    """"""

    FormC: ExtendedNormalizationForms = ...
    """"""
    FormD: ExtendedNormalizationForms = ...
    """"""
    FormKC: ExtendedNormalizationForms = ...
    """"""
    FormKD: ExtendedNormalizationForms = ...
    """"""
    FormIdna: ExtendedNormalizationForms = ...
    """"""
    FormCDisallowUnassigned: ExtendedNormalizationForms = ...
    """"""
    FormDDisallowUnassigned: ExtendedNormalizationForms = ...
    """"""
    FormKCDisallowUnassigned: ExtendedNormalizationForms = ...
    """"""
    FormKDDisallowUnassigned: ExtendedNormalizationForms = ...
    """"""
    FormIdnaDisallowUnassigned: ExtendedNormalizationForms = ...
    """"""

class GB18030Encoding(DBCSCodePageEncoding, ISerializable, ICloneable):
    """"""
    @property
    def BodyName(self) -> str:
        """"""
    @property
    def CodePage(self) -> int:
        """"""
    @property
    def DecoderFallback(self) -> DecoderFallback:
        """"""
    @DecoderFallback.setter
    def DecoderFallback(self, value: DecoderFallback) -> None: ...
    @property
    def EncoderFallback(self) -> EncoderFallback:
        """"""
    @EncoderFallback.setter
    def EncoderFallback(self, value: EncoderFallback) -> None: ...
    @property
    def EncodingName(self) -> str:
        """"""
    @property
    def HeaderName(self) -> str:
        """"""
    @property
    def IsBrowserDisplay(self) -> bool:
        """"""
    @property
    def IsBrowserSave(self) -> bool:
        """"""
    @property
    def IsMailNewsDisplay(self) -> bool:
        """"""
    @property
    def IsMailNewsSave(self) -> bool:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def IsSingleByte(self) -> bool:
        """"""
    @property
    def WebName(self) -> str:
        """"""
    @property
    def WindowsCodePage(self) -> int:
        """"""
    def Clone(self) -> object:
        """"""
    def Equals(self, value: object) -> bool:
        """"""
    @overload
    def GetByteCount(self, chars: Array[Char]) -> int:
        """"""
    @overload
    def GetByteCount(self, chars: Array[Char], index: int, count: int) -> int:
        """"""
    @overload
    def GetByteCount(self, chars: Char, count: int) -> int:
        """"""
    @overload
    def GetByteCount(self, s: str) -> int:
        """"""
    @overload
    def GetBytes(self, chars: Array[Char]) -> Array[int]:
        """"""
    @overload
    def GetBytes(self, chars: Array[Char], index: int, count: int) -> Array[int]:
        """"""
    @overload
    def GetBytes(
        self, chars: Array[Char], charIndex: int, charCount: int, bytes: Array[int], byteIndex: int
    ) -> int:
        """"""
    @overload
    def GetBytes(self, chars: Char, charCount: int, bytes: int, byteCount: int) -> int:
        """"""
    @overload
    def GetBytes(self, s: str) -> Array[int]:
        """"""
    @overload
    def GetBytes(
        self, s: str, charIndex: int, charCount: int, bytes: Array[int], byteIndex: int
    ) -> int:
        """"""
    @overload
    def GetCharCount(self, bytes: Array[int]) -> int:
        """"""
    @overload
    def GetCharCount(self, bytes: Array[int], index: int, count: int) -> int:
        """"""
    @overload
    def GetCharCount(self, bytes: int, count: int) -> int:
        """"""
    @overload
    def GetChars(self, bytes: Array[int]) -> Array[Char]:
        """"""
    @overload
    def GetChars(self, bytes: Array[int], index: int, count: int) -> Array[Char]:
        """"""
    @overload
    def GetChars(
        self, bytes: Array[int], byteIndex: int, byteCount: int, chars: Array[Char], charIndex: int
    ) -> int:
        """"""
    @overload
    def GetChars(self, bytes: int, byteCount: int, chars: Char, charCount: int) -> int:
        """"""
    def GetDecoder(self) -> Decoder:
        """"""
    def GetEncoder(self) -> Encoder:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetMaxByteCount(self, charCount: int) -> int:
        """"""
    def GetMaxCharCount(self, byteCount: int) -> int:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetPreamble(self) -> Array[int]:
        """"""
    @overload
    def GetString(self, bytes: Array[int]) -> str:
        """"""
    @overload
    def GetString(self, bytes: Array[int], index: int, count: int) -> str:
        """"""
    @overload
    def GetString(self, bytes: int, byteCount: int) -> str:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IsAlwaysNormalized(self) -> bool:
        """"""
    @overload
    def IsAlwaysNormalized(self, form: NormalizationForm) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

class ISCIIEncoding(EncodingNLS, ISerializable, ICloneable):
    """"""
    def __init__(self, codePage: int) -> None:
        """"""
    @property
    def BodyName(self) -> str:
        """"""
    @property
    def CodePage(self) -> int:
        """"""
    @property
    def DecoderFallback(self) -> DecoderFallback:
        """"""
    @DecoderFallback.setter
    def DecoderFallback(self, value: DecoderFallback) -> None: ...
    @property
    def EncoderFallback(self) -> EncoderFallback:
        """"""
    @EncoderFallback.setter
    def EncoderFallback(self, value: EncoderFallback) -> None: ...
    @property
    def EncodingName(self) -> str:
        """"""
    @property
    def HeaderName(self) -> str:
        """"""
    @property
    def IsBrowserDisplay(self) -> bool:
        """"""
    @property
    def IsBrowserSave(self) -> bool:
        """"""
    @property
    def IsMailNewsDisplay(self) -> bool:
        """"""
    @property
    def IsMailNewsSave(self) -> bool:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def IsSingleByte(self) -> bool:
        """"""
    @property
    def WebName(self) -> str:
        """"""
    @property
    def WindowsCodePage(self) -> int:
        """"""
    def Clone(self) -> object:
        """"""
    def Equals(self, value: object) -> bool:
        """"""
    @overload
    def GetByteCount(self, chars: Array[Char]) -> int:
        """"""
    @overload
    def GetByteCount(self, chars: Array[Char], index: int, count: int) -> int:
        """"""
    @overload
    def GetByteCount(self, chars: Char, count: int) -> int:
        """"""
    @overload
    def GetByteCount(self, s: str) -> int:
        """"""
    @overload
    def GetBytes(self, chars: Array[Char]) -> Array[int]:
        """"""
    @overload
    def GetBytes(self, chars: Array[Char], index: int, count: int) -> Array[int]:
        """"""
    @overload
    def GetBytes(
        self, chars: Array[Char], charIndex: int, charCount: int, bytes: Array[int], byteIndex: int
    ) -> int:
        """"""
    @overload
    def GetBytes(self, chars: Char, charCount: int, bytes: int, byteCount: int) -> int:
        """"""
    @overload
    def GetBytes(self, s: str) -> Array[int]:
        """"""
    @overload
    def GetBytes(
        self, s: str, charIndex: int, charCount: int, bytes: Array[int], byteIndex: int
    ) -> int:
        """"""
    @overload
    def GetCharCount(self, bytes: Array[int]) -> int:
        """"""
    @overload
    def GetCharCount(self, bytes: Array[int], index: int, count: int) -> int:
        """"""
    @overload
    def GetCharCount(self, bytes: int, count: int) -> int:
        """"""
    @overload
    def GetChars(self, bytes: Array[int]) -> Array[Char]:
        """"""
    @overload
    def GetChars(self, bytes: Array[int], index: int, count: int) -> Array[Char]:
        """"""
    @overload
    def GetChars(
        self, bytes: Array[int], byteIndex: int, byteCount: int, chars: Array[Char], charIndex: int
    ) -> int:
        """"""
    @overload
    def GetChars(self, bytes: int, byteCount: int, chars: Char, charCount: int) -> int:
        """"""
    def GetDecoder(self) -> Decoder:
        """"""
    def GetEncoder(self) -> Encoder:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetMaxByteCount(self, charCount: int) -> int:
        """"""
    def GetMaxCharCount(self, byteCount: int) -> int:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetPreamble(self) -> Array[int]:
        """"""
    @overload
    def GetString(self, bytes: Array[int]) -> str:
        """"""
    @overload
    def GetString(self, bytes: Array[int], index: int, count: int) -> str:
        """"""
    @overload
    def GetString(self, bytes: int, byteCount: int) -> str:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IsAlwaysNormalized(self) -> bool:
        """"""
    @overload
    def IsAlwaysNormalized(self, form: NormalizationForm) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

class ISO2022Encoding(DBCSCodePageEncoding, ISerializable, ICloneable):
    """"""
    @property
    def BodyName(self) -> str:
        """"""
    @property
    def CodePage(self) -> int:
        """"""
    @property
    def DecoderFallback(self) -> DecoderFallback:
        """"""
    @DecoderFallback.setter
    def DecoderFallback(self, value: DecoderFallback) -> None: ...
    @property
    def EncoderFallback(self) -> EncoderFallback:
        """"""
    @EncoderFallback.setter
    def EncoderFallback(self, value: EncoderFallback) -> None: ...
    @property
    def EncodingName(self) -> str:
        """"""
    @property
    def HeaderName(self) -> str:
        """"""
    @property
    def IsBrowserDisplay(self) -> bool:
        """"""
    @property
    def IsBrowserSave(self) -> bool:
        """"""
    @property
    def IsMailNewsDisplay(self) -> bool:
        """"""
    @property
    def IsMailNewsSave(self) -> bool:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def IsSingleByte(self) -> bool:
        """"""
    @property
    def WebName(self) -> str:
        """"""
    @property
    def WindowsCodePage(self) -> int:
        """"""
    def Clone(self) -> object:
        """"""
    def Equals(self, value: object) -> bool:
        """"""
    @overload
    def GetByteCount(self, chars: Array[Char]) -> int:
        """"""
    @overload
    def GetByteCount(self, chars: Array[Char], index: int, count: int) -> int:
        """"""
    @overload
    def GetByteCount(self, chars: Char, count: int) -> int:
        """"""
    @overload
    def GetByteCount(self, s: str) -> int:
        """"""
    @overload
    def GetBytes(self, chars: Array[Char]) -> Array[int]:
        """"""
    @overload
    def GetBytes(self, chars: Array[Char], index: int, count: int) -> Array[int]:
        """"""
    @overload
    def GetBytes(
        self, chars: Array[Char], charIndex: int, charCount: int, bytes: Array[int], byteIndex: int
    ) -> int:
        """"""
    @overload
    def GetBytes(self, chars: Char, charCount: int, bytes: int, byteCount: int) -> int:
        """"""
    @overload
    def GetBytes(self, s: str) -> Array[int]:
        """"""
    @overload
    def GetBytes(
        self, s: str, charIndex: int, charCount: int, bytes: Array[int], byteIndex: int
    ) -> int:
        """"""
    @overload
    def GetCharCount(self, bytes: Array[int]) -> int:
        """"""
    @overload
    def GetCharCount(self, bytes: Array[int], index: int, count: int) -> int:
        """"""
    @overload
    def GetCharCount(self, bytes: int, count: int) -> int:
        """"""
    @overload
    def GetChars(self, bytes: Array[int]) -> Array[Char]:
        """"""
    @overload
    def GetChars(self, bytes: Array[int], index: int, count: int) -> Array[Char]:
        """"""
    @overload
    def GetChars(
        self, bytes: Array[int], byteIndex: int, byteCount: int, chars: Array[Char], charIndex: int
    ) -> int:
        """"""
    @overload
    def GetChars(self, bytes: int, byteCount: int, chars: Char, charCount: int) -> int:
        """"""
    def GetDecoder(self) -> Decoder:
        """"""
    def GetEncoder(self) -> Encoder:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetMaxByteCount(self, charCount: int) -> int:
        """"""
    def GetMaxCharCount(self, byteCount: int) -> int:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetPreamble(self) -> Array[int]:
        """"""
    @overload
    def GetString(self, bytes: Array[int]) -> str:
        """"""
    @overload
    def GetString(self, bytes: Array[int], index: int, count: int) -> str:
        """"""
    @overload
    def GetString(self, bytes: int, byteCount: int) -> str:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IsAlwaysNormalized(self) -> bool:
        """"""
    @overload
    def IsAlwaysNormalized(self, form: NormalizationForm) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

class InternalDecoderBestFitFallback(DecoderFallback):
    """"""
    @property
    def MaxCharCount(self) -> int:
        """"""
    def CreateFallbackBuffer(self) -> DecoderFallbackBuffer:
        """"""
    def Equals(self, value: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class InternalDecoderBestFitFallbackBuffer(DecoderFallbackBuffer):
    """"""
    def __init__(self, fallback: InternalDecoderBestFitFallback) -> None:
        """"""
    @property
    def Remaining(self) -> int:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Fallback(self, bytesUnknown: Array[int], index: int) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetNextChar(self) -> Char:
        """"""
    def GetType(self) -> Type:
        """"""
    def MovePrevious(self) -> bool:
        """"""
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class InternalEncoderBestFitFallback(EncoderFallback):
    """"""
    @property
    def MaxCharCount(self) -> int:
        """"""
    def CreateFallbackBuffer(self) -> EncoderFallbackBuffer:
        """"""
    def Equals(self, value: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class InternalEncoderBestFitFallbackBuffer(EncoderFallbackBuffer):
    """"""
    def __init__(self, fallback: InternalEncoderBestFitFallback) -> None:
        """"""
    @property
    def Remaining(self) -> int:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Fallback(self, charUnknownHigh: Char, charUnknownLow: Char, index: int) -> bool:
        """"""
    @overload
    def Fallback(self, charUnknown: Char, index: int) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetNextChar(self) -> Char:
        """"""
    def GetType(self) -> Type:
        """"""
    def MovePrevious(self) -> bool:
        """"""
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class Latin1Encoding(EncodingNLS, ISerializable, ICloneable):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def BodyName(self) -> str:
        """"""
    @property
    def CodePage(self) -> int:
        """"""
    @property
    def DecoderFallback(self) -> DecoderFallback:
        """"""
    @DecoderFallback.setter
    def DecoderFallback(self, value: DecoderFallback) -> None: ...
    @property
    def EncoderFallback(self) -> EncoderFallback:
        """"""
    @EncoderFallback.setter
    def EncoderFallback(self, value: EncoderFallback) -> None: ...
    @property
    def EncodingName(self) -> str:
        """"""
    @property
    def HeaderName(self) -> str:
        """"""
    @property
    def IsBrowserDisplay(self) -> bool:
        """"""
    @property
    def IsBrowserSave(self) -> bool:
        """"""
    @property
    def IsMailNewsDisplay(self) -> bool:
        """"""
    @property
    def IsMailNewsSave(self) -> bool:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def IsSingleByte(self) -> bool:
        """"""
    @property
    def WebName(self) -> str:
        """"""
    @property
    def WindowsCodePage(self) -> int:
        """"""
    def Clone(self) -> object:
        """"""
    def Equals(self, value: object) -> bool:
        """"""
    @overload
    def GetByteCount(self, chars: Array[Char]) -> int:
        """"""
    @overload
    def GetByteCount(self, chars: Array[Char], index: int, count: int) -> int:
        """"""
    @overload
    def GetByteCount(self, chars: Char, count: int) -> int:
        """"""
    @overload
    def GetByteCount(self, s: str) -> int:
        """"""
    @overload
    def GetBytes(self, chars: Array[Char]) -> Array[int]:
        """"""
    @overload
    def GetBytes(self, chars: Array[Char], index: int, count: int) -> Array[int]:
        """"""
    @overload
    def GetBytes(
        self, chars: Array[Char], charIndex: int, charCount: int, bytes: Array[int], byteIndex: int
    ) -> int:
        """"""
    @overload
    def GetBytes(self, chars: Char, charCount: int, bytes: int, byteCount: int) -> int:
        """"""
    @overload
    def GetBytes(self, s: str) -> Array[int]:
        """"""
    @overload
    def GetBytes(
        self, s: str, charIndex: int, charCount: int, bytes: Array[int], byteIndex: int
    ) -> int:
        """"""
    @overload
    def GetCharCount(self, bytes: Array[int]) -> int:
        """"""
    @overload
    def GetCharCount(self, bytes: Array[int], index: int, count: int) -> int:
        """"""
    @overload
    def GetCharCount(self, bytes: int, count: int) -> int:
        """"""
    @overload
    def GetChars(self, bytes: Array[int]) -> Array[Char]:
        """"""
    @overload
    def GetChars(self, bytes: Array[int], index: int, count: int) -> Array[Char]:
        """"""
    @overload
    def GetChars(
        self, bytes: Array[int], byteIndex: int, byteCount: int, chars: Array[Char], charIndex: int
    ) -> int:
        """"""
    @overload
    def GetChars(self, bytes: int, byteCount: int, chars: Char, charCount: int) -> int:
        """"""
    def GetDecoder(self) -> Decoder:
        """"""
    def GetEncoder(self) -> Encoder:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetMaxByteCount(self, charCount: int) -> int:
        """"""
    def GetMaxCharCount(self, byteCount: int) -> int:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetPreamble(self) -> Array[int]:
        """"""
    @overload
    def GetString(self, bytes: Array[int]) -> str:
        """"""
    @overload
    def GetString(self, bytes: Array[int], index: int, count: int) -> str:
        """"""
    @overload
    def GetString(self, bytes: int, byteCount: int) -> str:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IsAlwaysNormalized(self) -> bool:
        """"""
    @overload
    def IsAlwaysNormalized(self, form: NormalizationForm) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

class MLangCodePageEncoding(Object, IObjectReference, ISerializable):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetRealObject(self, context: StreamingContext) -> object:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class Normalization(Object):
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

class NormalizationForm(Enum):
    """"""

    FormC: NormalizationForm = ...
    """"""
    FormD: NormalizationForm = ...
    """"""
    FormKC: NormalizationForm = ...
    """"""
    FormKD: NormalizationForm = ...
    """"""

class SBCSCodePageEncoding(BaseCodePageEncoding, ISerializable, ICloneable):
    """"""
    def __init__(self, codePage: int) -> None:
        """"""
    @property
    def BodyName(self) -> str:
        """"""
    @property
    def CodePage(self) -> int:
        """"""
    @property
    def DecoderFallback(self) -> DecoderFallback:
        """"""
    @DecoderFallback.setter
    def DecoderFallback(self, value: DecoderFallback) -> None: ...
    @property
    def EncoderFallback(self) -> EncoderFallback:
        """"""
    @EncoderFallback.setter
    def EncoderFallback(self, value: EncoderFallback) -> None: ...
    @property
    def EncodingName(self) -> str:
        """"""
    @property
    def HeaderName(self) -> str:
        """"""
    @property
    def IsBrowserDisplay(self) -> bool:
        """"""
    @property
    def IsBrowserSave(self) -> bool:
        """"""
    @property
    def IsMailNewsDisplay(self) -> bool:
        """"""
    @property
    def IsMailNewsSave(self) -> bool:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def IsSingleByte(self) -> bool:
        """"""
    @property
    def WebName(self) -> str:
        """"""
    @property
    def WindowsCodePage(self) -> int:
        """"""
    def Clone(self) -> object:
        """"""
    def Equals(self, value: object) -> bool:
        """"""
    @overload
    def GetByteCount(self, chars: Array[Char]) -> int:
        """"""
    @overload
    def GetByteCount(self, chars: Array[Char], index: int, count: int) -> int:
        """"""
    @overload
    def GetByteCount(self, chars: Char, count: int) -> int:
        """"""
    @overload
    def GetByteCount(self, s: str) -> int:
        """"""
    @overload
    def GetBytes(self, chars: Array[Char]) -> Array[int]:
        """"""
    @overload
    def GetBytes(self, chars: Array[Char], index: int, count: int) -> Array[int]:
        """"""
    @overload
    def GetBytes(
        self, chars: Array[Char], charIndex: int, charCount: int, bytes: Array[int], byteIndex: int
    ) -> int:
        """"""
    @overload
    def GetBytes(self, chars: Char, charCount: int, bytes: int, byteCount: int) -> int:
        """"""
    @overload
    def GetBytes(self, s: str) -> Array[int]:
        """"""
    @overload
    def GetBytes(
        self, s: str, charIndex: int, charCount: int, bytes: Array[int], byteIndex: int
    ) -> int:
        """"""
    @overload
    def GetCharCount(self, bytes: Array[int]) -> int:
        """"""
    @overload
    def GetCharCount(self, bytes: Array[int], index: int, count: int) -> int:
        """"""
    @overload
    def GetCharCount(self, bytes: int, count: int) -> int:
        """"""
    @overload
    def GetChars(self, bytes: Array[int]) -> Array[Char]:
        """"""
    @overload
    def GetChars(self, bytes: Array[int], index: int, count: int) -> Array[Char]:
        """"""
    @overload
    def GetChars(
        self, bytes: Array[int], byteIndex: int, byteCount: int, chars: Array[Char], charIndex: int
    ) -> int:
        """"""
    @overload
    def GetChars(self, bytes: int, byteCount: int, chars: Char, charCount: int) -> int:
        """"""
    def GetDecoder(self) -> Decoder:
        """"""
    def GetEncoder(self) -> Encoder:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetMaxByteCount(self, charCount: int) -> int:
        """"""
    def GetMaxCharCount(self, byteCount: int) -> int:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetPreamble(self) -> Array[int]:
        """"""
    @overload
    def GetString(self, bytes: Array[int]) -> str:
        """"""
    @overload
    def GetString(self, bytes: Array[int], index: int, count: int) -> str:
        """"""
    @overload
    def GetString(self, bytes: int, byteCount: int) -> str:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IsAlwaysNormalized(self) -> bool:
        """"""
    @overload
    def IsAlwaysNormalized(self, form: NormalizationForm) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

class StringBuilder(Object, ISerializable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, capacity: int) -> None:
        """"""
    @overload
    def __init__(self, value: str) -> None:
        """"""
    @overload
    def __init__(self, value: str, capacity: int) -> None:
        """"""
    @overload
    def __init__(self, value: str, startIndex: int, length: int, capacity: int) -> None:
        """"""
    @overload
    def __init__(self, capacity: int, maxCapacity: int) -> None:
        """"""
    @property
    def Capacity(self) -> int:
        """"""
    @Capacity.setter
    def Capacity(self, value: int) -> None: ...
    @property
    def Chars(self) -> Char:
        """"""
    @Chars.setter
    def Chars(self, value: Char) -> None: ...
    @property
    def Length(self) -> int:
        """"""
    @Length.setter
    def Length(self, value: int) -> None: ...
    @property
    def MaxCapacity(self) -> int:
        """"""
    @overload
    def Append(self, value: Array[Char]) -> StringBuilder:
        """"""
    @overload
    def Append(self, value: Array[Char], startIndex: int, charCount: int) -> StringBuilder:
        """"""
    @overload
    def Append(self, value: bool) -> StringBuilder:
        """"""
    @overload
    def Append(self, value: int) -> StringBuilder:
        """"""
    @overload
    def Append(self, value: Char) -> StringBuilder:
        """"""
    @overload
    def Append(self, value: Char, valueCount: int) -> StringBuilder:
        """"""
    @overload
    def Append(self, value: Decimal) -> StringBuilder:
        """"""
    @overload
    def Append(self, value: float) -> StringBuilder:
        """"""
    @overload
    def Append(self, value: int) -> StringBuilder:
        """"""
    @overload
    def Append(self, value: int) -> StringBuilder:
        """"""
    @overload
    def Append(self, value: int) -> StringBuilder:
        """"""
    @overload
    def Append(self, value: object) -> StringBuilder:
        """"""
    @overload
    def Append(self, value: int) -> StringBuilder:
        """"""
    @overload
    def Append(self, value: float) -> StringBuilder:
        """"""
    @overload
    def Append(self, value: str) -> StringBuilder:
        """"""
    @overload
    def Append(self, value: str, startIndex: int, count: int) -> StringBuilder:
        """"""
    @overload
    def Append(self, value: int) -> StringBuilder:
        """"""
    @overload
    def Append(self, value: int) -> StringBuilder:
        """"""
    @overload
    def Append(self, value: int) -> StringBuilder:
        """"""
    @overload
    def AppendFormat(
        self, provider: IFormatProvider, format: str, args: Array[object]
    ) -> StringBuilder:
        """"""
    @overload
    def AppendFormat(self, provider: IFormatProvider, format: str, arg0: object) -> StringBuilder:
        """"""
    @overload
    def AppendFormat(
        self, provider: IFormatProvider, format: str, arg0: object, arg1: object
    ) -> StringBuilder:
        """"""
    @overload
    def AppendFormat(
        self, provider: IFormatProvider, format: str, arg0: object, arg1: object, arg2: object
    ) -> StringBuilder:
        """"""
    @overload
    def AppendFormat(self, format: str, args: Array[object]) -> StringBuilder:
        """"""
    @overload
    def AppendFormat(self, format: str, arg0: object) -> StringBuilder:
        """"""
    @overload
    def AppendFormat(self, format: str, arg0: object, arg1: object) -> StringBuilder:
        """"""
    @overload
    def AppendFormat(self, format: str, arg0: object, arg1: object, arg2: object) -> StringBuilder:
        """"""
    @overload
    def AppendLine(self) -> StringBuilder:
        """"""
    @overload
    def AppendLine(self, value: str) -> StringBuilder:
        """"""
    def Clear(self) -> StringBuilder:
        """"""
    def CopyTo(
        self, sourceIndex: int, destination: Array[Char], destinationIndex: int, count: int
    ) -> None:
        """"""
    def EnsureCapacity(self, capacity: int) -> int:
        """"""
    @overload
    def Equals(self, sb: StringBuilder) -> bool:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def Insert(self, index: int, value: Array[Char]) -> StringBuilder:
        """"""
    @overload
    def Insert(
        self, index: int, value: Array[Char], startIndex: int, charCount: int
    ) -> StringBuilder:
        """"""
    @overload
    def Insert(self, index: int, value: bool) -> StringBuilder:
        """"""
    @overload
    def Insert(self, index: int, value: int) -> StringBuilder:
        """"""
    @overload
    def Insert(self, index: int, value: Char) -> StringBuilder:
        """"""
    @overload
    def Insert(self, index: int, value: Decimal) -> StringBuilder:
        """"""
    @overload
    def Insert(self, index: int, value: float) -> StringBuilder:
        """"""
    @overload
    def Insert(self, index: int, value: int) -> StringBuilder:
        """"""
    @overload
    def Insert(self, index: int, value: int) -> StringBuilder:
        """"""
    @overload
    def Insert(self, index: int, value: int) -> StringBuilder:
        """"""
    @overload
    def Insert(self, index: int, value: object) -> StringBuilder:
        """"""
    @overload
    def Insert(self, index: int, value: int) -> StringBuilder:
        """"""
    @overload
    def Insert(self, index: int, value: float) -> StringBuilder:
        """"""
    @overload
    def Insert(self, index: int, value: str) -> StringBuilder:
        """"""
    @overload
    def Insert(self, index: int, value: str, count: int) -> StringBuilder:
        """"""
    @overload
    def Insert(self, index: int, value: int) -> StringBuilder:
        """"""
    @overload
    def Insert(self, index: int, value: int) -> StringBuilder:
        """"""
    @overload
    def Insert(self, index: int, value: int) -> StringBuilder:
        """"""
    def Remove(self, startIndex: int, length: int) -> StringBuilder:
        """"""
    @overload
    def Replace(self, oldChar: Char, newChar: Char) -> StringBuilder:
        """"""
    @overload
    def Replace(self, oldChar: Char, newChar: Char, startIndex: int, count: int) -> StringBuilder:
        """"""
    @overload
    def Replace(self, oldValue: str, newValue: str) -> StringBuilder:
        """"""
    @overload
    def Replace(self, oldValue: str, newValue: str, startIndex: int, count: int) -> StringBuilder:
        """"""
    @overload
    def ToString(self) -> str:
        """"""
    @overload
    def ToString(self, startIndex: int, length: int) -> str:
        """"""
    def __delitem__(self, startIndex: int, length: int) -> StringBuilder:
        """"""

class StringBuilderCache(ABC, Object):
    """"""
    @classmethod
    def Acquire(cls, capacity: int = ...) -> StringBuilder:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @classmethod
    def GetStringAndRelease(cls, sb: StringBuilder) -> str:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def Release(cls, sb: StringBuilder) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class SurrogateEncoder(Object, IObjectReference, ISerializable):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetRealObject(self, context: StreamingContext) -> object:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class UTF32Encoding(Encoding, ICloneable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, bigEndian: bool, byteOrderMark: bool) -> None:
        """"""
    @overload
    def __init__(
        self, bigEndian: bool, byteOrderMark: bool, throwOnInvalidCharacters: bool
    ) -> None:
        """"""
    @property
    def BodyName(self) -> str:
        """"""
    @property
    def CodePage(self) -> int:
        """"""
    @property
    def DecoderFallback(self) -> DecoderFallback:
        """"""
    @DecoderFallback.setter
    def DecoderFallback(self, value: DecoderFallback) -> None: ...
    @property
    def EncoderFallback(self) -> EncoderFallback:
        """"""
    @EncoderFallback.setter
    def EncoderFallback(self, value: EncoderFallback) -> None: ...
    @property
    def EncodingName(self) -> str:
        """"""
    @property
    def HeaderName(self) -> str:
        """"""
    @property
    def IsBrowserDisplay(self) -> bool:
        """"""
    @property
    def IsBrowserSave(self) -> bool:
        """"""
    @property
    def IsMailNewsDisplay(self) -> bool:
        """"""
    @property
    def IsMailNewsSave(self) -> bool:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def IsSingleByte(self) -> bool:
        """"""
    @property
    def WebName(self) -> str:
        """"""
    @property
    def WindowsCodePage(self) -> int:
        """"""
    def Clone(self) -> object:
        """"""
    def Equals(self, value: object) -> bool:
        """"""
    @overload
    def GetByteCount(self, chars: Array[Char]) -> int:
        """"""
    @overload
    def GetByteCount(self, chars: Array[Char], index: int, count: int) -> int:
        """"""
    @overload
    def GetByteCount(self, chars: Char, count: int) -> int:
        """"""
    @overload
    def GetByteCount(self, s: str) -> int:
        """"""
    @overload
    def GetBytes(self, chars: Array[Char]) -> Array[int]:
        """"""
    @overload
    def GetBytes(self, chars: Array[Char], index: int, count: int) -> Array[int]:
        """"""
    @overload
    def GetBytes(
        self, chars: Array[Char], charIndex: int, charCount: int, bytes: Array[int], byteIndex: int
    ) -> int:
        """"""
    @overload
    def GetBytes(self, chars: Char, charCount: int, bytes: int, byteCount: int) -> int:
        """"""
    @overload
    def GetBytes(self, s: str) -> Array[int]:
        """"""
    @overload
    def GetBytes(
        self, s: str, charIndex: int, charCount: int, bytes: Array[int], byteIndex: int
    ) -> int:
        """"""
    @overload
    def GetCharCount(self, bytes: Array[int]) -> int:
        """"""
    @overload
    def GetCharCount(self, bytes: Array[int], index: int, count: int) -> int:
        """"""
    @overload
    def GetCharCount(self, bytes: int, count: int) -> int:
        """"""
    @overload
    def GetChars(self, bytes: Array[int]) -> Array[Char]:
        """"""
    @overload
    def GetChars(self, bytes: Array[int], index: int, count: int) -> Array[Char]:
        """"""
    @overload
    def GetChars(
        self, bytes: Array[int], byteIndex: int, byteCount: int, chars: Array[Char], charIndex: int
    ) -> int:
        """"""
    @overload
    def GetChars(self, bytes: int, byteCount: int, chars: Char, charCount: int) -> int:
        """"""
    def GetDecoder(self) -> Decoder:
        """"""
    def GetEncoder(self) -> Encoder:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetMaxByteCount(self, charCount: int) -> int:
        """"""
    def GetMaxCharCount(self, byteCount: int) -> int:
        """"""
    def GetPreamble(self) -> Array[int]:
        """"""
    @overload
    def GetString(self, bytes: Array[int]) -> str:
        """"""
    @overload
    def GetString(self, bytes: Array[int], index: int, count: int) -> str:
        """"""
    @overload
    def GetString(self, bytes: int, byteCount: int) -> str:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IsAlwaysNormalized(self) -> bool:
        """"""
    @overload
    def IsAlwaysNormalized(self, form: NormalizationForm) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

class UTF7Encoding(Encoding, ICloneable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, allowOptionals: bool) -> None:
        """"""
    @property
    def BodyName(self) -> str:
        """"""
    @property
    def CodePage(self) -> int:
        """"""
    @property
    def DecoderFallback(self) -> DecoderFallback:
        """"""
    @DecoderFallback.setter
    def DecoderFallback(self, value: DecoderFallback) -> None: ...
    @property
    def EncoderFallback(self) -> EncoderFallback:
        """"""
    @EncoderFallback.setter
    def EncoderFallback(self, value: EncoderFallback) -> None: ...
    @property
    def EncodingName(self) -> str:
        """"""
    @property
    def HeaderName(self) -> str:
        """"""
    @property
    def IsBrowserDisplay(self) -> bool:
        """"""
    @property
    def IsBrowserSave(self) -> bool:
        """"""
    @property
    def IsMailNewsDisplay(self) -> bool:
        """"""
    @property
    def IsMailNewsSave(self) -> bool:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def IsSingleByte(self) -> bool:
        """"""
    @property
    def WebName(self) -> str:
        """"""
    @property
    def WindowsCodePage(self) -> int:
        """"""
    def Clone(self) -> object:
        """"""
    def Equals(self, value: object) -> bool:
        """"""
    @overload
    def GetByteCount(self, chars: Array[Char]) -> int:
        """"""
    @overload
    def GetByteCount(self, chars: Array[Char], index: int, count: int) -> int:
        """"""
    @overload
    def GetByteCount(self, chars: Char, count: int) -> int:
        """"""
    @overload
    def GetByteCount(self, s: str) -> int:
        """"""
    @overload
    def GetBytes(self, chars: Array[Char]) -> Array[int]:
        """"""
    @overload
    def GetBytes(self, chars: Array[Char], index: int, count: int) -> Array[int]:
        """"""
    @overload
    def GetBytes(
        self, chars: Array[Char], charIndex: int, charCount: int, bytes: Array[int], byteIndex: int
    ) -> int:
        """"""
    @overload
    def GetBytes(self, chars: Char, charCount: int, bytes: int, byteCount: int) -> int:
        """"""
    @overload
    def GetBytes(self, s: str) -> Array[int]:
        """"""
    @overload
    def GetBytes(
        self, s: str, charIndex: int, charCount: int, bytes: Array[int], byteIndex: int
    ) -> int:
        """"""
    @overload
    def GetCharCount(self, bytes: Array[int]) -> int:
        """"""
    @overload
    def GetCharCount(self, bytes: Array[int], index: int, count: int) -> int:
        """"""
    @overload
    def GetCharCount(self, bytes: int, count: int) -> int:
        """"""
    @overload
    def GetChars(self, bytes: Array[int]) -> Array[Char]:
        """"""
    @overload
    def GetChars(self, bytes: Array[int], index: int, count: int) -> Array[Char]:
        """"""
    @overload
    def GetChars(
        self, bytes: Array[int], byteIndex: int, byteCount: int, chars: Array[Char], charIndex: int
    ) -> int:
        """"""
    @overload
    def GetChars(self, bytes: int, byteCount: int, chars: Char, charCount: int) -> int:
        """"""
    def GetDecoder(self) -> Decoder:
        """"""
    def GetEncoder(self) -> Encoder:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetMaxByteCount(self, charCount: int) -> int:
        """"""
    def GetMaxCharCount(self, byteCount: int) -> int:
        """"""
    def GetPreamble(self) -> Array[int]:
        """"""
    @overload
    def GetString(self, bytes: Array[int]) -> str:
        """"""
    @overload
    def GetString(self, bytes: Array[int], index: int, count: int) -> str:
        """"""
    @overload
    def GetString(self, bytes: int, byteCount: int) -> str:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IsAlwaysNormalized(self) -> bool:
        """"""
    @overload
    def IsAlwaysNormalized(self, form: NormalizationForm) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

class UTF8Encoding(Encoding, ICloneable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, encoderShouldEmitUTF8Identifier: bool) -> None:
        """"""
    @overload
    def __init__(self, encoderShouldEmitUTF8Identifier: bool, throwOnInvalidBytes: bool) -> None:
        """"""
    @property
    def BodyName(self) -> str:
        """"""
    @property
    def CodePage(self) -> int:
        """"""
    @property
    def DecoderFallback(self) -> DecoderFallback:
        """"""
    @DecoderFallback.setter
    def DecoderFallback(self, value: DecoderFallback) -> None: ...
    @property
    def EncoderFallback(self) -> EncoderFallback:
        """"""
    @EncoderFallback.setter
    def EncoderFallback(self, value: EncoderFallback) -> None: ...
    @property
    def EncodingName(self) -> str:
        """"""
    @property
    def HeaderName(self) -> str:
        """"""
    @property
    def IsBrowserDisplay(self) -> bool:
        """"""
    @property
    def IsBrowserSave(self) -> bool:
        """"""
    @property
    def IsMailNewsDisplay(self) -> bool:
        """"""
    @property
    def IsMailNewsSave(self) -> bool:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def IsSingleByte(self) -> bool:
        """"""
    @property
    def WebName(self) -> str:
        """"""
    @property
    def WindowsCodePage(self) -> int:
        """"""
    def Clone(self) -> object:
        """"""
    def Equals(self, value: object) -> bool:
        """"""
    @overload
    def GetByteCount(self, chars: Array[Char]) -> int:
        """"""
    @overload
    def GetByteCount(self, chars: Array[Char], index: int, count: int) -> int:
        """"""
    @overload
    def GetByteCount(self, chars: Char, count: int) -> int:
        """"""
    @overload
    def GetByteCount(self, chars: str) -> int:
        """"""
    @overload
    def GetBytes(self, chars: Array[Char]) -> Array[int]:
        """"""
    @overload
    def GetBytes(self, chars: Array[Char], index: int, count: int) -> Array[int]:
        """"""
    @overload
    def GetBytes(
        self, chars: Array[Char], charIndex: int, charCount: int, bytes: Array[int], byteIndex: int
    ) -> int:
        """"""
    @overload
    def GetBytes(self, chars: Char, charCount: int, bytes: int, byteCount: int) -> int:
        """"""
    @overload
    def GetBytes(self, s: str) -> Array[int]:
        """"""
    @overload
    def GetBytes(
        self, s: str, charIndex: int, charCount: int, bytes: Array[int], byteIndex: int
    ) -> int:
        """"""
    @overload
    def GetCharCount(self, bytes: Array[int]) -> int:
        """"""
    @overload
    def GetCharCount(self, bytes: Array[int], index: int, count: int) -> int:
        """"""
    @overload
    def GetCharCount(self, bytes: int, count: int) -> int:
        """"""
    @overload
    def GetChars(self, bytes: Array[int]) -> Array[Char]:
        """"""
    @overload
    def GetChars(self, bytes: Array[int], index: int, count: int) -> Array[Char]:
        """"""
    @overload
    def GetChars(
        self, bytes: Array[int], byteIndex: int, byteCount: int, chars: Array[Char], charIndex: int
    ) -> int:
        """"""
    @overload
    def GetChars(self, bytes: int, byteCount: int, chars: Char, charCount: int) -> int:
        """"""
    def GetDecoder(self) -> Decoder:
        """"""
    def GetEncoder(self) -> Encoder:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetMaxByteCount(self, charCount: int) -> int:
        """"""
    def GetMaxCharCount(self, byteCount: int) -> int:
        """"""
    def GetPreamble(self) -> Array[int]:
        """"""
    @overload
    def GetString(self, bytes: Array[int]) -> str:
        """"""
    @overload
    def GetString(self, bytes: Array[int], index: int, count: int) -> str:
        """"""
    @overload
    def GetString(self, bytes: int, byteCount: int) -> str:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IsAlwaysNormalized(self) -> bool:
        """"""
    @overload
    def IsAlwaysNormalized(self, form: NormalizationForm) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

class UnicodeEncoding(Encoding, ICloneable):
    """"""

    CharSize: ClassVar[int]
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, bigEndian: bool, byteOrderMark: bool) -> None:
        """"""
    @overload
    def __init__(self, bigEndian: bool, byteOrderMark: bool, throwOnInvalidBytes: bool) -> None:
        """"""
    @property
    def BodyName(self) -> str:
        """"""
    @property
    def CodePage(self) -> int:
        """"""
    @property
    def DecoderFallback(self) -> DecoderFallback:
        """"""
    @DecoderFallback.setter
    def DecoderFallback(self, value: DecoderFallback) -> None: ...
    @property
    def EncoderFallback(self) -> EncoderFallback:
        """"""
    @EncoderFallback.setter
    def EncoderFallback(self, value: EncoderFallback) -> None: ...
    @property
    def EncodingName(self) -> str:
        """"""
    @property
    def HeaderName(self) -> str:
        """"""
    @property
    def IsBrowserDisplay(self) -> bool:
        """"""
    @property
    def IsBrowserSave(self) -> bool:
        """"""
    @property
    def IsMailNewsDisplay(self) -> bool:
        """"""
    @property
    def IsMailNewsSave(self) -> bool:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def IsSingleByte(self) -> bool:
        """"""
    @property
    def WebName(self) -> str:
        """"""
    @property
    def WindowsCodePage(self) -> int:
        """"""
    def Clone(self) -> object:
        """"""
    def Equals(self, value: object) -> bool:
        """"""
    @overload
    def GetByteCount(self, chars: Array[Char]) -> int:
        """"""
    @overload
    def GetByteCount(self, chars: Array[Char], index: int, count: int) -> int:
        """"""
    @overload
    def GetByteCount(self, chars: Char, count: int) -> int:
        """"""
    @overload
    def GetByteCount(self, s: str) -> int:
        """"""
    @overload
    def GetBytes(self, chars: Array[Char]) -> Array[int]:
        """"""
    @overload
    def GetBytes(self, chars: Array[Char], index: int, count: int) -> Array[int]:
        """"""
    @overload
    def GetBytes(
        self, chars: Array[Char], charIndex: int, charCount: int, bytes: Array[int], byteIndex: int
    ) -> int:
        """"""
    @overload
    def GetBytes(self, chars: Char, charCount: int, bytes: int, byteCount: int) -> int:
        """"""
    @overload
    def GetBytes(self, s: str) -> Array[int]:
        """"""
    @overload
    def GetBytes(
        self, s: str, charIndex: int, charCount: int, bytes: Array[int], byteIndex: int
    ) -> int:
        """"""
    @overload
    def GetCharCount(self, bytes: Array[int]) -> int:
        """"""
    @overload
    def GetCharCount(self, bytes: Array[int], index: int, count: int) -> int:
        """"""
    @overload
    def GetCharCount(self, bytes: int, count: int) -> int:
        """"""
    @overload
    def GetChars(self, bytes: Array[int]) -> Array[Char]:
        """"""
    @overload
    def GetChars(self, bytes: Array[int], index: int, count: int) -> Array[Char]:
        """"""
    @overload
    def GetChars(
        self, bytes: Array[int], byteIndex: int, byteCount: int, chars: Array[Char], charIndex: int
    ) -> int:
        """"""
    @overload
    def GetChars(self, bytes: int, byteCount: int, chars: Char, charCount: int) -> int:
        """"""
    def GetDecoder(self) -> Decoder:
        """"""
    def GetEncoder(self) -> Encoder:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetMaxByteCount(self, charCount: int) -> int:
        """"""
    def GetMaxCharCount(self, byteCount: int) -> int:
        """"""
    def GetPreamble(self) -> Array[int]:
        """"""
    @overload
    def GetString(self, bytes: Array[int]) -> str:
        """"""
    @overload
    def GetString(self, bytes: Array[int], index: int, count: int) -> str:
        """"""
    @overload
    def GetString(self, bytes: int, byteCount: int) -> str:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IsAlwaysNormalized(self) -> bool:
        """"""
    @overload
    def IsAlwaysNormalized(self, form: NormalizationForm) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
