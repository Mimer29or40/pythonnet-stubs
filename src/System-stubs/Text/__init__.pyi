from __future__ import annotations

from abc import ABC
from typing import ClassVar
from typing import Final
from typing import Tuple
from typing import overload

from System import ArgumentException
from System import Array
from System import Char
from System import Decimal
from System import Enum
from System import Exception
from System import ICloneable
from System import IFormatProvider
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

    def __init__(self):
        """"""
    @classmethod
    @property
    def ASCII(cls) -> Encoding:
        """

        :return:
        """
    @classmethod
    @property
    def BigEndianUnicode(cls) -> Encoding:
        """

        :return:
        """
    @property
    def BodyName(self) -> str:
        """

        :return:
        """
    @property
    def CodePage(self) -> int:
        """

        :return:
        """
    @property
    def DecoderFallback(self) -> DecoderFallback:
        """

        :return:
        """
    @DecoderFallback.setter
    def DecoderFallback(self, value: DecoderFallback) -> None: ...
    @classmethod
    @property
    def Default(cls) -> Encoding:
        """

        :return:
        """
    @property
    def EncoderFallback(self) -> EncoderFallback:
        """

        :return:
        """
    @EncoderFallback.setter
    def EncoderFallback(self, value: EncoderFallback) -> None: ...
    @property
    def EncodingName(self) -> str:
        """

        :return:
        """
    @property
    def HeaderName(self) -> str:
        """

        :return:
        """
    @property
    def IsBrowserDisplay(self) -> bool:
        """

        :return:
        """
    @property
    def IsBrowserSave(self) -> bool:
        """

        :return:
        """
    @property
    def IsMailNewsDisplay(self) -> bool:
        """

        :return:
        """
    @property
    def IsMailNewsSave(self) -> bool:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def IsSingleByte(self) -> bool:
        """

        :return:
        """
    @classmethod
    @property
    def UTF32(cls) -> Encoding:
        """

        :return:
        """
    @classmethod
    @property
    def UTF7(cls) -> Encoding:
        """

        :return:
        """
    @classmethod
    @property
    def UTF8(cls) -> Encoding:
        """

        :return:
        """
    @classmethod
    @property
    def Unicode(cls) -> Encoding:
        """

        :return:
        """
    @property
    def WebName(self) -> str:
        """

        :return:
        """
    @property
    def WindowsCodePage(self) -> int:
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
    @overload
    def GetByteCount(self, chars: Array[Char]) -> int:
        """

        :param chars:
        :return:
        """
    @overload
    def GetByteCount(self, s: str) -> int:
        """

        :param s:
        :return:
        """
    @overload
    def GetByteCount(self, chars: Char, count: int) -> int:
        """

        :param chars:
        :param count:
        :return:
        """
    @overload
    def GetByteCount(self, chars: Array[Char], index: int, count: int) -> int:
        """

        :param chars:
        :param index:
        :param count:
        :return:
        """
    @overload
    def GetBytes(self, chars: Array[Char]) -> Array[int]:
        """

        :param chars:
        :return:
        """
    @overload
    def GetBytes(self, s: str) -> Array[int]:
        """

        :param s:
        :return:
        """
    @overload
    def GetBytes(self, chars: Array[Char], index: int, count: int) -> Array[int]:
        """

        :param chars:
        :param index:
        :param count:
        :return:
        """
    @overload
    def GetBytes(self, chars: Char, charCount: int, bytes: int, byteCount: int) -> int:
        """

        :param chars:
        :param charCount:
        :param bytes:
        :param byteCount:
        :return:
        """
    @overload
    def GetBytes(
        self, chars: Array[Char], charIndex: int, charCount: int, bytes: Array[int], byteIndex: int
    ) -> int:
        """

        :param chars:
        :param charIndex:
        :param charCount:
        :param bytes:
        :param byteIndex:
        :return:
        """
    @overload
    def GetBytes(
        self, s: str, charIndex: int, charCount: int, bytes: Array[int], byteIndex: int
    ) -> int:
        """

        :param s:
        :param charIndex:
        :param charCount:
        :param bytes:
        :param byteIndex:
        :return:
        """
    @overload
    def GetCharCount(self, bytes: Array[int]) -> int:
        """

        :param bytes:
        :return:
        """
    @overload
    def GetCharCount(self, bytes: int, count: int) -> int:
        """

        :param bytes:
        :param count:
        :return:
        """
    @overload
    def GetCharCount(self, bytes: Array[int], index: int, count: int) -> int:
        """

        :param bytes:
        :param index:
        :param count:
        :return:
        """
    @overload
    def GetChars(self, bytes: Array[int]) -> Array[Char]:
        """

        :param bytes:
        :return:
        """
    @overload
    def GetChars(self, bytes: Array[int], index: int, count: int) -> Array[Char]:
        """

        :param bytes:
        :param index:
        :param count:
        :return:
        """
    @overload
    def GetChars(self, bytes: int, byteCount: int, chars: Char, charCount: int) -> int:
        """

        :param bytes:
        :param byteCount:
        :param chars:
        :param charCount:
        :return:
        """
    @overload
    def GetChars(
        self, bytes: Array[int], byteIndex: int, byteCount: int, chars: Array[Char], charIndex: int
    ) -> int:
        """

        :param bytes:
        :param byteIndex:
        :param byteCount:
        :param chars:
        :param charIndex:
        :return:
        """
    def GetDecoder(self) -> Decoder:
        """

        :return:
        """
    def GetEncoder(self) -> Encoder:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetMaxByteCount(self, charCount: int) -> int:
        """

        :param charCount:
        :return:
        """
    def GetMaxCharCount(self, byteCount: int) -> int:
        """

        :param byteCount:
        :return:
        """
    def GetPreamble(self) -> Array[int]:
        """

        :return:
        """
    @overload
    def GetString(self, bytes: Array[int]) -> str:
        """

        :param bytes:
        :return:
        """
    @overload
    def GetString(self, bytes: int, byteCount: int) -> str:
        """

        :param bytes:
        :param byteCount:
        :return:
        """
    @overload
    def GetString(self, bytes: Array[int], index: int, count: int) -> str:
        """

        :param bytes:
        :param index:
        :param count:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def IsAlwaysNormalized(self) -> bool:
        """

        :return:
        """
    @overload
    def IsAlwaysNormalized(self, form: NormalizationForm) -> bool:
        """

        :param form:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class BaseCodePageEncoding(ABC, EncodingNLS, ISerializable, ICloneable):
    """"""

    @classmethod
    @property
    def ASCII(cls) -> Encoding:
        """

        :return:
        """
    @classmethod
    @property
    def BigEndianUnicode(cls) -> Encoding:
        """

        :return:
        """
    @property
    def BodyName(self) -> str:
        """

        :return:
        """
    @property
    def CodePage(self) -> int:
        """

        :return:
        """
    @property
    def DecoderFallback(self) -> DecoderFallback:
        """

        :return:
        """
    @DecoderFallback.setter
    def DecoderFallback(self, value: DecoderFallback) -> None: ...
    @classmethod
    @property
    def Default(cls) -> Encoding:
        """

        :return:
        """
    @property
    def EncoderFallback(self) -> EncoderFallback:
        """

        :return:
        """
    @EncoderFallback.setter
    def EncoderFallback(self, value: EncoderFallback) -> None: ...
    @property
    def EncodingName(self) -> str:
        """

        :return:
        """
    @property
    def HeaderName(self) -> str:
        """

        :return:
        """
    @property
    def IsBrowserDisplay(self) -> bool:
        """

        :return:
        """
    @property
    def IsBrowserSave(self) -> bool:
        """

        :return:
        """
    @property
    def IsMailNewsDisplay(self) -> bool:
        """

        :return:
        """
    @property
    def IsMailNewsSave(self) -> bool:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def IsSingleByte(self) -> bool:
        """

        :return:
        """
    @classmethod
    @property
    def UTF32(cls) -> Encoding:
        """

        :return:
        """
    @classmethod
    @property
    def UTF7(cls) -> Encoding:
        """

        :return:
        """
    @classmethod
    @property
    def UTF8(cls) -> Encoding:
        """

        :return:
        """
    @classmethod
    @property
    def Unicode(cls) -> Encoding:
        """

        :return:
        """
    @property
    def WebName(self) -> str:
        """

        :return:
        """
    @property
    def WindowsCodePage(self) -> int:
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
    @overload
    def GetByteCount(self, chars: Array[Char]) -> int:
        """

        :param chars:
        :return:
        """
    @overload
    def GetByteCount(self, s: str) -> int:
        """

        :param s:
        :return:
        """
    @overload
    def GetByteCount(self, chars: Char, count: int) -> int:
        """

        :param chars:
        :param count:
        :return:
        """
    @overload
    def GetByteCount(self, chars: Array[Char], index: int, count: int) -> int:
        """

        :param chars:
        :param index:
        :param count:
        :return:
        """
    @overload
    def GetBytes(self, chars: Array[Char]) -> Array[int]:
        """

        :param chars:
        :return:
        """
    @overload
    def GetBytes(self, s: str) -> Array[int]:
        """

        :param s:
        :return:
        """
    @overload
    def GetBytes(self, chars: Array[Char], index: int, count: int) -> Array[int]:
        """

        :param chars:
        :param index:
        :param count:
        :return:
        """
    @overload
    def GetBytes(self, chars: Char, charCount: int, bytes: int, byteCount: int) -> int:
        """

        :param chars:
        :param charCount:
        :param bytes:
        :param byteCount:
        :return:
        """
    @overload
    def GetBytes(
        self, chars: Array[Char], charIndex: int, charCount: int, bytes: Array[int], byteIndex: int
    ) -> int:
        """

        :param chars:
        :param charIndex:
        :param charCount:
        :param bytes:
        :param byteIndex:
        :return:
        """
    @overload
    def GetBytes(
        self, s: str, charIndex: int, charCount: int, bytes: Array[int], byteIndex: int
    ) -> int:
        """

        :param s:
        :param charIndex:
        :param charCount:
        :param bytes:
        :param byteIndex:
        :return:
        """
    @overload
    def GetCharCount(self, bytes: Array[int]) -> int:
        """

        :param bytes:
        :return:
        """
    @overload
    def GetCharCount(self, bytes: int, count: int) -> int:
        """

        :param bytes:
        :param count:
        :return:
        """
    @overload
    def GetCharCount(self, bytes: Array[int], index: int, count: int) -> int:
        """

        :param bytes:
        :param index:
        :param count:
        :return:
        """
    @overload
    def GetChars(self, bytes: Array[int]) -> Array[Char]:
        """

        :param bytes:
        :return:
        """
    @overload
    def GetChars(self, bytes: Array[int], index: int, count: int) -> Array[Char]:
        """

        :param bytes:
        :param index:
        :param count:
        :return:
        """
    @overload
    def GetChars(self, bytes: int, byteCount: int, chars: Char, charCount: int) -> int:
        """

        :param bytes:
        :param byteCount:
        :param chars:
        :param charCount:
        :return:
        """
    @overload
    def GetChars(
        self, bytes: Array[int], byteIndex: int, byteCount: int, chars: Array[Char], charIndex: int
    ) -> int:
        """

        :param bytes:
        :param byteIndex:
        :param byteCount:
        :param chars:
        :param charIndex:
        :return:
        """
    def GetDecoder(self) -> Decoder:
        """

        :return:
        """
    def GetEncoder(self) -> Encoder:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetMaxByteCount(self, charCount: int) -> int:
        """

        :param charCount:
        :return:
        """
    def GetMaxCharCount(self, byteCount: int) -> int:
        """

        :param byteCount:
        :return:
        """
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    def GetPreamble(self) -> Array[int]:
        """

        :return:
        """
    @overload
    def GetString(self, bytes: Array[int]) -> str:
        """

        :param bytes:
        :return:
        """
    @overload
    def GetString(self, bytes: int, byteCount: int) -> str:
        """

        :param bytes:
        :param byteCount:
        :return:
        """
    @overload
    def GetString(self, bytes: Array[int], index: int, count: int) -> str:
        """

        :param bytes:
        :param index:
        :param count:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def IsAlwaysNormalized(self) -> bool:
        """

        :return:
        """
    @overload
    def IsAlwaysNormalized(self, form: NormalizationForm) -> bool:
        """

        :param form:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CodePageEncoding(Object, IObjectReference, ISerializable):
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
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    def GetRealObject(self, context: StreamingContext) -> object:
        """

        :param context:
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

class DBCSCodePageEncoding(BaseCodePageEncoding, ISerializable, ICloneable):
    """"""

    def __init__(self, codePage: int):
        """

        :param codePage:
        """
    @classmethod
    @property
    def ASCII(cls) -> Encoding:
        """

        :return:
        """
    @classmethod
    @property
    def BigEndianUnicode(cls) -> Encoding:
        """

        :return:
        """
    @property
    def BodyName(self) -> str:
        """

        :return:
        """
    @property
    def CodePage(self) -> int:
        """

        :return:
        """
    @property
    def DecoderFallback(self) -> DecoderFallback:
        """

        :return:
        """
    @DecoderFallback.setter
    def DecoderFallback(self, value: DecoderFallback) -> None: ...
    @classmethod
    @property
    def Default(cls) -> Encoding:
        """

        :return:
        """
    @property
    def EncoderFallback(self) -> EncoderFallback:
        """

        :return:
        """
    @EncoderFallback.setter
    def EncoderFallback(self, value: EncoderFallback) -> None: ...
    @property
    def EncodingName(self) -> str:
        """

        :return:
        """
    @property
    def HeaderName(self) -> str:
        """

        :return:
        """
    @property
    def IsBrowserDisplay(self) -> bool:
        """

        :return:
        """
    @property
    def IsBrowserSave(self) -> bool:
        """

        :return:
        """
    @property
    def IsMailNewsDisplay(self) -> bool:
        """

        :return:
        """
    @property
    def IsMailNewsSave(self) -> bool:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def IsSingleByte(self) -> bool:
        """

        :return:
        """
    @classmethod
    @property
    def UTF32(cls) -> Encoding:
        """

        :return:
        """
    @classmethod
    @property
    def UTF7(cls) -> Encoding:
        """

        :return:
        """
    @classmethod
    @property
    def UTF8(cls) -> Encoding:
        """

        :return:
        """
    @classmethod
    @property
    def Unicode(cls) -> Encoding:
        """

        :return:
        """
    @property
    def WebName(self) -> str:
        """

        :return:
        """
    @property
    def WindowsCodePage(self) -> int:
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
    @overload
    def GetByteCount(self, chars: Array[Char]) -> int:
        """

        :param chars:
        :return:
        """
    @overload
    def GetByteCount(self, s: str) -> int:
        """

        :param s:
        :return:
        """
    @overload
    def GetByteCount(self, chars: Char, count: int) -> int:
        """

        :param chars:
        :param count:
        :return:
        """
    @overload
    def GetByteCount(self, chars: Array[Char], index: int, count: int) -> int:
        """

        :param chars:
        :param index:
        :param count:
        :return:
        """
    @overload
    def GetBytes(self, chars: Array[Char]) -> Array[int]:
        """

        :param chars:
        :return:
        """
    @overload
    def GetBytes(self, s: str) -> Array[int]:
        """

        :param s:
        :return:
        """
    @overload
    def GetBytes(self, chars: Array[Char], index: int, count: int) -> Array[int]:
        """

        :param chars:
        :param index:
        :param count:
        :return:
        """
    @overload
    def GetBytes(self, chars: Char, charCount: int, bytes: int, byteCount: int) -> int:
        """

        :param chars:
        :param charCount:
        :param bytes:
        :param byteCount:
        :return:
        """
    @overload
    def GetBytes(
        self, chars: Array[Char], charIndex: int, charCount: int, bytes: Array[int], byteIndex: int
    ) -> int:
        """

        :param chars:
        :param charIndex:
        :param charCount:
        :param bytes:
        :param byteIndex:
        :return:
        """
    @overload
    def GetBytes(
        self, s: str, charIndex: int, charCount: int, bytes: Array[int], byteIndex: int
    ) -> int:
        """

        :param s:
        :param charIndex:
        :param charCount:
        :param bytes:
        :param byteIndex:
        :return:
        """
    @overload
    def GetCharCount(self, bytes: Array[int]) -> int:
        """

        :param bytes:
        :return:
        """
    @overload
    def GetCharCount(self, bytes: int, count: int) -> int:
        """

        :param bytes:
        :param count:
        :return:
        """
    @overload
    def GetCharCount(self, bytes: Array[int], index: int, count: int) -> int:
        """

        :param bytes:
        :param index:
        :param count:
        :return:
        """
    @overload
    def GetChars(self, bytes: Array[int]) -> Array[Char]:
        """

        :param bytes:
        :return:
        """
    @overload
    def GetChars(self, bytes: Array[int], index: int, count: int) -> Array[Char]:
        """

        :param bytes:
        :param index:
        :param count:
        :return:
        """
    @overload
    def GetChars(self, bytes: int, byteCount: int, chars: Char, charCount: int) -> int:
        """

        :param bytes:
        :param byteCount:
        :param chars:
        :param charCount:
        :return:
        """
    @overload
    def GetChars(
        self, bytes: Array[int], byteIndex: int, byteCount: int, chars: Array[Char], charIndex: int
    ) -> int:
        """

        :param bytes:
        :param byteIndex:
        :param byteCount:
        :param chars:
        :param charIndex:
        :return:
        """
    def GetDecoder(self) -> Decoder:
        """

        :return:
        """
    def GetEncoder(self) -> Encoder:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetMaxByteCount(self, charCount: int) -> int:
        """

        :param charCount:
        :return:
        """
    def GetMaxCharCount(self, byteCount: int) -> int:
        """

        :param byteCount:
        :return:
        """
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    def GetPreamble(self) -> Array[int]:
        """

        :return:
        """
    @overload
    def GetString(self, bytes: Array[int]) -> str:
        """

        :param bytes:
        :return:
        """
    @overload
    def GetString(self, bytes: int, byteCount: int) -> str:
        """

        :param bytes:
        :param byteCount:
        :return:
        """
    @overload
    def GetString(self, bytes: Array[int], index: int, count: int) -> str:
        """

        :param bytes:
        :param index:
        :param count:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def IsAlwaysNormalized(self) -> bool:
        """

        :return:
        """
    @overload
    def IsAlwaysNormalized(self, form: NormalizationForm) -> bool:
        """

        :param form:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class Decoder(ABC, Object):
    """"""

    @property
    def Fallback(self) -> DecoderFallback:
        """

        :return:
        """
    @Fallback.setter
    def Fallback(self, value: DecoderFallback) -> None: ...
    @property
    def FallbackBuffer(self) -> DecoderFallbackBuffer:
        """

        :return:
        """
    @overload
    def Convert(
        self,
        bytes: int,
        byteCount: int,
        chars: Char,
        charCount: int,
        flush: bool,
        bytesUsed: int,
        charsUsed: int,
        completed: bool,
    ) -> Tuple[None, int, int, bool]:
        """

        :param bytes:
        :param byteCount:
        :param chars:
        :param charCount:
        :param flush:
        :param bytesUsed:
        :param charsUsed:
        :param completed:
        """
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
        bytesUsed: int,
        charsUsed: int,
        completed: bool,
    ) -> Tuple[None, int, int, bool]:
        """

        :param bytes:
        :param byteIndex:
        :param byteCount:
        :param chars:
        :param charIndex:
        :param charCount:
        :param flush:
        :param bytesUsed:
        :param charsUsed:
        :param completed:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetCharCount(self, bytes: Array[int], index: int, count: int) -> int:
        """

        :param bytes:
        :param index:
        :param count:
        :return:
        """
    @overload
    def GetCharCount(self, bytes: int, count: int, flush: bool) -> int:
        """

        :param bytes:
        :param count:
        :param flush:
        :return:
        """
    @overload
    def GetCharCount(self, bytes: Array[int], index: int, count: int, flush: bool) -> int:
        """

        :param bytes:
        :param index:
        :param count:
        :param flush:
        :return:
        """
    @overload
    def GetChars(
        self, bytes: Array[int], byteIndex: int, byteCount: int, chars: Array[Char], charIndex: int
    ) -> int:
        """

        :param bytes:
        :param byteIndex:
        :param byteCount:
        :param chars:
        :param charIndex:
        :return:
        """
    @overload
    def GetChars(self, bytes: int, byteCount: int, chars: Char, charCount: int, flush: bool) -> int:
        """

        :param bytes:
        :param byteCount:
        :param chars:
        :param charCount:
        :param flush:
        :return:
        """
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
        """

        :param bytes:
        :param byteIndex:
        :param byteCount:
        :param chars:
        :param charIndex:
        :param flush:
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
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class DecoderExceptionFallback(DecoderFallback):
    """"""

    def __init__(self):
        """"""
    @classmethod
    @property
    def ExceptionFallback(cls) -> DecoderFallback:
        """

        :return:
        """
    @property
    def MaxCharCount(self) -> int:
        """

        :return:
        """
    @classmethod
    @property
    def ReplacementFallback(cls) -> DecoderFallback:
        """

        :return:
        """
    def CreateFallbackBuffer(self) -> DecoderFallbackBuffer:
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

class DecoderExceptionFallbackBuffer(DecoderFallbackBuffer):
    """"""

    def __init__(self):
        """"""
    @property
    def Remaining(self) -> int:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def Fallback(self, bytesUnknown: Array[int], index: int) -> bool:
        """

        :param bytesUnknown:
        :param index:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetNextChar(self) -> Char:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def MovePrevious(self) -> bool:
        """

        :return:
        """
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class DecoderFallback(ABC, Object):
    """"""

    @classmethod
    @property
    def ExceptionFallback(cls) -> DecoderFallback:
        """

        :return:
        """
    @property
    def MaxCharCount(self) -> int:
        """

        :return:
        """
    @classmethod
    @property
    def ReplacementFallback(cls) -> DecoderFallback:
        """

        :return:
        """
    def CreateFallbackBuffer(self) -> DecoderFallbackBuffer:
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

class DecoderFallbackBuffer(ABC, Object):
    """"""

    @property
    def Remaining(self) -> int:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def Fallback(self, bytesUnknown: Array[int], index: int) -> bool:
        """

        :param bytesUnknown:
        :param index:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetNextChar(self) -> Char:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def MovePrevious(self) -> bool:
        """

        :return:
        """
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class DecoderFallbackException(ArgumentException, _Exception, ISerializable):
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
    def __init__(self, message: str, bytesUnknown: Array[int], index: int):
        """

        :param message:
        :param bytesUnknown:
        :param index:
        """
    @property
    def BytesUnknown(self) -> Array[int]:
        """

        :return:
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
    def Index(self) -> int:
        """

        :return:
        """
    @property
    def InnerException(self) -> Exception:
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

class DecoderNLS(Decoder, ISerializable):
    """"""

    @property
    def Fallback(self) -> DecoderFallback:
        """

        :return:
        """
    @Fallback.setter
    def Fallback(self, value: DecoderFallback) -> None: ...
    @property
    def FallbackBuffer(self) -> DecoderFallbackBuffer:
        """

        :return:
        """
    @property
    def MustFlush(self) -> bool:
        """

        :return:
        """
    @overload
    def Convert(
        self,
        bytes: int,
        byteCount: int,
        chars: Char,
        charCount: int,
        flush: bool,
        bytesUsed: int,
        charsUsed: int,
        completed: bool,
    ) -> Tuple[None, int, int, bool]:
        """

        :param bytes:
        :param byteCount:
        :param chars:
        :param charCount:
        :param flush:
        :param bytesUsed:
        :param charsUsed:
        :param completed:
        """
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
        bytesUsed: int,
        charsUsed: int,
        completed: bool,
    ) -> Tuple[None, int, int, bool]:
        """

        :param bytes:
        :param byteIndex:
        :param byteCount:
        :param chars:
        :param charIndex:
        :param charCount:
        :param flush:
        :param bytesUsed:
        :param charsUsed:
        :param completed:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetCharCount(self, bytes: Array[int], index: int, count: int) -> int:
        """

        :param bytes:
        :param index:
        :param count:
        :return:
        """
    @overload
    def GetCharCount(self, bytes: int, count: int, flush: bool) -> int:
        """

        :param bytes:
        :param count:
        :param flush:
        :return:
        """
    @overload
    def GetCharCount(self, bytes: Array[int], index: int, count: int, flush: bool) -> int:
        """

        :param bytes:
        :param index:
        :param count:
        :param flush:
        :return:
        """
    @overload
    def GetChars(
        self, bytes: Array[int], byteIndex: int, byteCount: int, chars: Array[Char], charIndex: int
    ) -> int:
        """

        :param bytes:
        :param byteIndex:
        :param byteCount:
        :param chars:
        :param charIndex:
        :return:
        """
    @overload
    def GetChars(self, bytes: int, byteCount: int, chars: Char, charCount: int, flush: bool) -> int:
        """

        :param bytes:
        :param byteCount:
        :param chars:
        :param charCount:
        :param flush:
        :return:
        """
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
        """

        :param bytes:
        :param byteIndex:
        :param byteCount:
        :param chars:
        :param charIndex:
        :param flush:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class DecoderReplacementFallback(DecoderFallback):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, replacement: str):
        """

        :param replacement:
        """
    @property
    def DefaultString(self) -> str:
        """

        :return:
        """
    @classmethod
    @property
    def ExceptionFallback(cls) -> DecoderFallback:
        """

        :return:
        """
    @property
    def MaxCharCount(self) -> int:
        """

        :return:
        """
    @classmethod
    @property
    def ReplacementFallback(cls) -> DecoderFallback:
        """

        :return:
        """
    def CreateFallbackBuffer(self) -> DecoderFallbackBuffer:
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

class DecoderReplacementFallbackBuffer(DecoderFallbackBuffer):
    """"""

    def __init__(self, fallback: DecoderReplacementFallback):
        """

        :param fallback:
        """
    @property
    def Remaining(self) -> int:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def Fallback(self, bytesUnknown: Array[int], index: int) -> bool:
        """

        :param bytesUnknown:
        :param index:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetNextChar(self) -> Char:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def MovePrevious(self) -> bool:
        """

        :return:
        """
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class EUCJPEncoding(DBCSCodePageEncoding, ISerializable, ICloneable):
    """"""

    def __init__(self):
        """"""
    @classmethod
    @property
    def ASCII(cls) -> Encoding:
        """

        :return:
        """
    @classmethod
    @property
    def BigEndianUnicode(cls) -> Encoding:
        """

        :return:
        """
    @property
    def BodyName(self) -> str:
        """

        :return:
        """
    @property
    def CodePage(self) -> int:
        """

        :return:
        """
    @property
    def DecoderFallback(self) -> DecoderFallback:
        """

        :return:
        """
    @DecoderFallback.setter
    def DecoderFallback(self, value: DecoderFallback) -> None: ...
    @classmethod
    @property
    def Default(cls) -> Encoding:
        """

        :return:
        """
    @property
    def EncoderFallback(self) -> EncoderFallback:
        """

        :return:
        """
    @EncoderFallback.setter
    def EncoderFallback(self, value: EncoderFallback) -> None: ...
    @property
    def EncodingName(self) -> str:
        """

        :return:
        """
    @property
    def HeaderName(self) -> str:
        """

        :return:
        """
    @property
    def IsBrowserDisplay(self) -> bool:
        """

        :return:
        """
    @property
    def IsBrowserSave(self) -> bool:
        """

        :return:
        """
    @property
    def IsMailNewsDisplay(self) -> bool:
        """

        :return:
        """
    @property
    def IsMailNewsSave(self) -> bool:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def IsSingleByte(self) -> bool:
        """

        :return:
        """
    @classmethod
    @property
    def UTF32(cls) -> Encoding:
        """

        :return:
        """
    @classmethod
    @property
    def UTF7(cls) -> Encoding:
        """

        :return:
        """
    @classmethod
    @property
    def UTF8(cls) -> Encoding:
        """

        :return:
        """
    @classmethod
    @property
    def Unicode(cls) -> Encoding:
        """

        :return:
        """
    @property
    def WebName(self) -> str:
        """

        :return:
        """
    @property
    def WindowsCodePage(self) -> int:
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
    @overload
    def GetByteCount(self, chars: Array[Char]) -> int:
        """

        :param chars:
        :return:
        """
    @overload
    def GetByteCount(self, s: str) -> int:
        """

        :param s:
        :return:
        """
    @overload
    def GetByteCount(self, chars: Char, count: int) -> int:
        """

        :param chars:
        :param count:
        :return:
        """
    @overload
    def GetByteCount(self, chars: Array[Char], index: int, count: int) -> int:
        """

        :param chars:
        :param index:
        :param count:
        :return:
        """
    @overload
    def GetBytes(self, chars: Array[Char]) -> Array[int]:
        """

        :param chars:
        :return:
        """
    @overload
    def GetBytes(self, s: str) -> Array[int]:
        """

        :param s:
        :return:
        """
    @overload
    def GetBytes(self, chars: Array[Char], index: int, count: int) -> Array[int]:
        """

        :param chars:
        :param index:
        :param count:
        :return:
        """
    @overload
    def GetBytes(self, chars: Char, charCount: int, bytes: int, byteCount: int) -> int:
        """

        :param chars:
        :param charCount:
        :param bytes:
        :param byteCount:
        :return:
        """
    @overload
    def GetBytes(
        self, chars: Array[Char], charIndex: int, charCount: int, bytes: Array[int], byteIndex: int
    ) -> int:
        """

        :param chars:
        :param charIndex:
        :param charCount:
        :param bytes:
        :param byteIndex:
        :return:
        """
    @overload
    def GetBytes(
        self, s: str, charIndex: int, charCount: int, bytes: Array[int], byteIndex: int
    ) -> int:
        """

        :param s:
        :param charIndex:
        :param charCount:
        :param bytes:
        :param byteIndex:
        :return:
        """
    @overload
    def GetCharCount(self, bytes: Array[int]) -> int:
        """

        :param bytes:
        :return:
        """
    @overload
    def GetCharCount(self, bytes: int, count: int) -> int:
        """

        :param bytes:
        :param count:
        :return:
        """
    @overload
    def GetCharCount(self, bytes: Array[int], index: int, count: int) -> int:
        """

        :param bytes:
        :param index:
        :param count:
        :return:
        """
    @overload
    def GetChars(self, bytes: Array[int]) -> Array[Char]:
        """

        :param bytes:
        :return:
        """
    @overload
    def GetChars(self, bytes: Array[int], index: int, count: int) -> Array[Char]:
        """

        :param bytes:
        :param index:
        :param count:
        :return:
        """
    @overload
    def GetChars(self, bytes: int, byteCount: int, chars: Char, charCount: int) -> int:
        """

        :param bytes:
        :param byteCount:
        :param chars:
        :param charCount:
        :return:
        """
    @overload
    def GetChars(
        self, bytes: Array[int], byteIndex: int, byteCount: int, chars: Array[Char], charIndex: int
    ) -> int:
        """

        :param bytes:
        :param byteIndex:
        :param byteCount:
        :param chars:
        :param charIndex:
        :return:
        """
    def GetDecoder(self) -> Decoder:
        """

        :return:
        """
    def GetEncoder(self) -> Encoder:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetMaxByteCount(self, charCount: int) -> int:
        """

        :param charCount:
        :return:
        """
    def GetMaxCharCount(self, byteCount: int) -> int:
        """

        :param byteCount:
        :return:
        """
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    def GetPreamble(self) -> Array[int]:
        """

        :return:
        """
    @overload
    def GetString(self, bytes: Array[int]) -> str:
        """

        :param bytes:
        :return:
        """
    @overload
    def GetString(self, bytes: int, byteCount: int) -> str:
        """

        :param bytes:
        :param byteCount:
        :return:
        """
    @overload
    def GetString(self, bytes: Array[int], index: int, count: int) -> str:
        """

        :param bytes:
        :param index:
        :param count:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def IsAlwaysNormalized(self) -> bool:
        """

        :return:
        """
    @overload
    def IsAlwaysNormalized(self, form: NormalizationForm) -> bool:
        """

        :param form:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class Encoder(ABC, Object):
    """"""

    @property
    def Fallback(self) -> EncoderFallback:
        """

        :return:
        """
    @Fallback.setter
    def Fallback(self, value: EncoderFallback) -> None: ...
    @property
    def FallbackBuffer(self) -> EncoderFallbackBuffer:
        """

        :return:
        """
    @overload
    def Convert(
        self,
        chars: Char,
        charCount: int,
        bytes: int,
        byteCount: int,
        flush: bool,
        charsUsed: int,
        bytesUsed: int,
        completed: bool,
    ) -> Tuple[None, int, int, bool]:
        """

        :param chars:
        :param charCount:
        :param bytes:
        :param byteCount:
        :param flush:
        :param charsUsed:
        :param bytesUsed:
        :param completed:
        """
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
        charsUsed: int,
        bytesUsed: int,
        completed: bool,
    ) -> Tuple[None, int, int, bool]:
        """

        :param chars:
        :param charIndex:
        :param charCount:
        :param bytes:
        :param byteIndex:
        :param byteCount:
        :param flush:
        :param charsUsed:
        :param bytesUsed:
        :param completed:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetByteCount(self, chars: Char, count: int, flush: bool) -> int:
        """

        :param chars:
        :param count:
        :param flush:
        :return:
        """
    @overload
    def GetByteCount(self, chars: Array[Char], index: int, count: int, flush: bool) -> int:
        """

        :param chars:
        :param index:
        :param count:
        :param flush:
        :return:
        """
    @overload
    def GetBytes(self, chars: Char, charCount: int, bytes: int, byteCount: int, flush: bool) -> int:
        """

        :param chars:
        :param charCount:
        :param bytes:
        :param byteCount:
        :param flush:
        :return:
        """
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
        """

        :param chars:
        :param charIndex:
        :param charCount:
        :param bytes:
        :param byteIndex:
        :param flush:
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
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class EncoderExceptionFallback(EncoderFallback):
    """"""

    def __init__(self):
        """"""
    @classmethod
    @property
    def ExceptionFallback(cls) -> EncoderFallback:
        """

        :return:
        """
    @property
    def MaxCharCount(self) -> int:
        """

        :return:
        """
    @classmethod
    @property
    def ReplacementFallback(cls) -> EncoderFallback:
        """

        :return:
        """
    def CreateFallbackBuffer(self) -> EncoderFallbackBuffer:
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

class EncoderExceptionFallbackBuffer(EncoderFallbackBuffer):
    """"""

    def __init__(self):
        """"""
    @property
    def Remaining(self) -> int:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def Fallback(self, charUnknown: Char, index: int) -> bool:
        """

        :param charUnknown:
        :param index:
        :return:
        """
    @overload
    def Fallback(self, charUnknownHigh: Char, charUnknownLow: Char, index: int) -> bool:
        """

        :param charUnknownHigh:
        :param charUnknownLow:
        :param index:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetNextChar(self) -> Char:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def MovePrevious(self) -> bool:
        """

        :return:
        """
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class EncoderFallback(ABC, Object):
    """"""

    @classmethod
    @property
    def ExceptionFallback(cls) -> EncoderFallback:
        """

        :return:
        """
    @property
    def MaxCharCount(self) -> int:
        """

        :return:
        """
    @classmethod
    @property
    def ReplacementFallback(cls) -> EncoderFallback:
        """

        :return:
        """
    def CreateFallbackBuffer(self) -> EncoderFallbackBuffer:
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

class EncoderFallbackBuffer(ABC, Object):
    """"""

    @property
    def Remaining(self) -> int:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def Fallback(self, charUnknown: Char, index: int) -> bool:
        """

        :param charUnknown:
        :param index:
        :return:
        """
    @overload
    def Fallback(self, charUnknownHigh: Char, charUnknownLow: Char, index: int) -> bool:
        """

        :param charUnknownHigh:
        :param charUnknownLow:
        :param index:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetNextChar(self) -> Char:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def MovePrevious(self) -> bool:
        """

        :return:
        """
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class EncoderFallbackException(ArgumentException, _Exception, ISerializable):
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
    @property
    def CharUnknown(self) -> Char:
        """

        :return:
        """
    @property
    def CharUnknownHigh(self) -> Char:
        """

        :return:
        """
    @property
    def CharUnknownLow(self) -> Char:
        """

        :return:
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
    def Index(self) -> int:
        """

        :return:
        """
    @property
    def InnerException(self) -> Exception:
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
    def IsUnknownSurrogate(self) -> bool:
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

class EncoderNLS(Encoder, ISerializable):
    """"""

    @property
    def Encoding(self) -> Encoding:
        """

        :return:
        """
    @property
    def Fallback(self) -> EncoderFallback:
        """

        :return:
        """
    @Fallback.setter
    def Fallback(self, value: EncoderFallback) -> None: ...
    @property
    def FallbackBuffer(self) -> EncoderFallbackBuffer:
        """

        :return:
        """
    @property
    def MustFlush(self) -> bool:
        """

        :return:
        """
    @overload
    def Convert(
        self,
        chars: Char,
        charCount: int,
        bytes: int,
        byteCount: int,
        flush: bool,
        charsUsed: int,
        bytesUsed: int,
        completed: bool,
    ) -> Tuple[None, int, int, bool]:
        """

        :param chars:
        :param charCount:
        :param bytes:
        :param byteCount:
        :param flush:
        :param charsUsed:
        :param bytesUsed:
        :param completed:
        """
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
        charsUsed: int,
        bytesUsed: int,
        completed: bool,
    ) -> Tuple[None, int, int, bool]:
        """

        :param chars:
        :param charIndex:
        :param charCount:
        :param bytes:
        :param byteIndex:
        :param byteCount:
        :param flush:
        :param charsUsed:
        :param bytesUsed:
        :param completed:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetByteCount(self, chars: Char, count: int, flush: bool) -> int:
        """

        :param chars:
        :param count:
        :param flush:
        :return:
        """
    @overload
    def GetByteCount(self, chars: Array[Char], index: int, count: int, flush: bool) -> int:
        """

        :param chars:
        :param index:
        :param count:
        :param flush:
        :return:
        """
    @overload
    def GetBytes(self, chars: Char, charCount: int, bytes: int, byteCount: int, flush: bool) -> int:
        """

        :param chars:
        :param charCount:
        :param bytes:
        :param byteCount:
        :param flush:
        :return:
        """
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
        """

        :param chars:
        :param charIndex:
        :param charCount:
        :param bytes:
        :param byteIndex:
        :param flush:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class EncoderReplacementFallback(EncoderFallback):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, replacement: str):
        """

        :param replacement:
        """
    @property
    def DefaultString(self) -> str:
        """

        :return:
        """
    @classmethod
    @property
    def ExceptionFallback(cls) -> EncoderFallback:
        """

        :return:
        """
    @property
    def MaxCharCount(self) -> int:
        """

        :return:
        """
    @classmethod
    @property
    def ReplacementFallback(cls) -> EncoderFallback:
        """

        :return:
        """
    def CreateFallbackBuffer(self) -> EncoderFallbackBuffer:
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

class EncoderReplacementFallbackBuffer(EncoderFallbackBuffer):
    """"""

    def __init__(self, fallback: EncoderReplacementFallback):
        """

        :param fallback:
        """
    @property
    def Remaining(self) -> int:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def Fallback(self, charUnknown: Char, index: int) -> bool:
        """

        :param charUnknown:
        :param index:
        :return:
        """
    @overload
    def Fallback(self, charUnknownHigh: Char, charUnknownLow: Char, index: int) -> bool:
        """

        :param charUnknownHigh:
        :param charUnknownLow:
        :param index:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetNextChar(self) -> Char:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def MovePrevious(self) -> bool:
        """

        :return:
        """
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class Encoding(ABC, Object, ICloneable):
    """"""

    @classmethod
    @property
    def ASCII(cls) -> Encoding:
        """

        :return:
        """
    @classmethod
    @property
    def BigEndianUnicode(cls) -> Encoding:
        """

        :return:
        """
    @property
    def BodyName(self) -> str:
        """

        :return:
        """
    @property
    def CodePage(self) -> int:
        """

        :return:
        """
    @property
    def DecoderFallback(self) -> DecoderFallback:
        """

        :return:
        """
    @DecoderFallback.setter
    def DecoderFallback(self, value: DecoderFallback) -> None: ...
    @classmethod
    @property
    def Default(cls) -> Encoding:
        """

        :return:
        """
    @property
    def EncoderFallback(self) -> EncoderFallback:
        """

        :return:
        """
    @EncoderFallback.setter
    def EncoderFallback(self, value: EncoderFallback) -> None: ...
    @property
    def EncodingName(self) -> str:
        """

        :return:
        """
    @property
    def HeaderName(self) -> str:
        """

        :return:
        """
    @property
    def IsBrowserDisplay(self) -> bool:
        """

        :return:
        """
    @property
    def IsBrowserSave(self) -> bool:
        """

        :return:
        """
    @property
    def IsMailNewsDisplay(self) -> bool:
        """

        :return:
        """
    @property
    def IsMailNewsSave(self) -> bool:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def IsSingleByte(self) -> bool:
        """

        :return:
        """
    @classmethod
    @property
    def UTF32(cls) -> Encoding:
        """

        :return:
        """
    @classmethod
    @property
    def UTF7(cls) -> Encoding:
        """

        :return:
        """
    @classmethod
    @property
    def UTF8(cls) -> Encoding:
        """

        :return:
        """
    @classmethod
    @property
    def Unicode(cls) -> Encoding:
        """

        :return:
        """
    @property
    def WebName(self) -> str:
        """

        :return:
        """
    @property
    def WindowsCodePage(self) -> int:
        """

        :return:
        """
    def Clone(self) -> object:
        """

        :return:
        """
    @classmethod
    @overload
    def Convert(cls, srcEncoding: Encoding, dstEncoding: Encoding, bytes: Array[int]) -> Array[int]:
        """

        :param srcEncoding:
        :param dstEncoding:
        :param bytes:
        :return:
        """
    @classmethod
    @overload
    def Convert(
        cls, srcEncoding: Encoding, dstEncoding: Encoding, bytes: Array[int], index: int, count: int
    ) -> Array[int]:
        """

        :param srcEncoding:
        :param dstEncoding:
        :param bytes:
        :param index:
        :param count:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetByteCount(self, chars: Array[Char]) -> int:
        """

        :param chars:
        :return:
        """
    @overload
    def GetByteCount(self, s: str) -> int:
        """

        :param s:
        :return:
        """
    @overload
    def GetByteCount(self, chars: Char, count: int) -> int:
        """

        :param chars:
        :param count:
        :return:
        """
    @overload
    def GetByteCount(self, chars: Array[Char], index: int, count: int) -> int:
        """

        :param chars:
        :param index:
        :param count:
        :return:
        """
    @overload
    def GetBytes(self, chars: Array[Char]) -> Array[int]:
        """

        :param chars:
        :return:
        """
    @overload
    def GetBytes(self, s: str) -> Array[int]:
        """

        :param s:
        :return:
        """
    @overload
    def GetBytes(self, chars: Array[Char], index: int, count: int) -> Array[int]:
        """

        :param chars:
        :param index:
        :param count:
        :return:
        """
    @overload
    def GetBytes(self, chars: Char, charCount: int, bytes: int, byteCount: int) -> int:
        """

        :param chars:
        :param charCount:
        :param bytes:
        :param byteCount:
        :return:
        """
    @overload
    def GetBytes(
        self, chars: Array[Char], charIndex: int, charCount: int, bytes: Array[int], byteIndex: int
    ) -> int:
        """

        :param chars:
        :param charIndex:
        :param charCount:
        :param bytes:
        :param byteIndex:
        :return:
        """
    @overload
    def GetBytes(
        self, s: str, charIndex: int, charCount: int, bytes: Array[int], byteIndex: int
    ) -> int:
        """

        :param s:
        :param charIndex:
        :param charCount:
        :param bytes:
        :param byteIndex:
        :return:
        """
    @overload
    def GetCharCount(self, bytes: Array[int]) -> int:
        """

        :param bytes:
        :return:
        """
    @overload
    def GetCharCount(self, bytes: int, count: int) -> int:
        """

        :param bytes:
        :param count:
        :return:
        """
    @overload
    def GetCharCount(self, bytes: Array[int], index: int, count: int) -> int:
        """

        :param bytes:
        :param index:
        :param count:
        :return:
        """
    @overload
    def GetChars(self, bytes: Array[int]) -> Array[Char]:
        """

        :param bytes:
        :return:
        """
    @overload
    def GetChars(self, bytes: Array[int], index: int, count: int) -> Array[Char]:
        """

        :param bytes:
        :param index:
        :param count:
        :return:
        """
    @overload
    def GetChars(self, bytes: int, byteCount: int, chars: Char, charCount: int) -> int:
        """

        :param bytes:
        :param byteCount:
        :param chars:
        :param charCount:
        :return:
        """
    @overload
    def GetChars(
        self, bytes: Array[int], byteIndex: int, byteCount: int, chars: Array[Char], charIndex: int
    ) -> int:
        """

        :param bytes:
        :param byteIndex:
        :param byteCount:
        :param chars:
        :param charIndex:
        :return:
        """
    def GetDecoder(self) -> Decoder:
        """

        :return:
        """
    def GetEncoder(self) -> Encoder:
        """

        :return:
        """
    @classmethod
    @overload
    def GetEncoding(cls, codepage: int) -> Encoding:
        """

        :param codepage:
        :return:
        """
    @classmethod
    @overload
    def GetEncoding(cls, name: str) -> Encoding:
        """

        :param name:
        :return:
        """
    @classmethod
    @overload
    def GetEncoding(
        cls, codepage: int, encoderFallback: EncoderFallback, decoderFallback: DecoderFallback
    ) -> Encoding:
        """

        :param codepage:
        :param encoderFallback:
        :param decoderFallback:
        :return:
        """
    @classmethod
    @overload
    def GetEncoding(
        cls, name: str, encoderFallback: EncoderFallback, decoderFallback: DecoderFallback
    ) -> Encoding:
        """

        :param name:
        :param encoderFallback:
        :param decoderFallback:
        :return:
        """
    @classmethod
    def GetEncodings(cls) -> Array[EncodingInfo]:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetMaxByteCount(self, charCount: int) -> int:
        """

        :param charCount:
        :return:
        """
    def GetMaxCharCount(self, byteCount: int) -> int:
        """

        :param byteCount:
        :return:
        """
    def GetPreamble(self) -> Array[int]:
        """

        :return:
        """
    @overload
    def GetString(self, bytes: Array[int]) -> str:
        """

        :param bytes:
        :return:
        """
    @overload
    def GetString(self, bytes: int, byteCount: int) -> str:
        """

        :param bytes:
        :param byteCount:
        :return:
        """
    @overload
    def GetString(self, bytes: Array[int], index: int, count: int) -> str:
        """

        :param bytes:
        :param index:
        :param count:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def IsAlwaysNormalized(self) -> bool:
        """

        :return:
        """
    @overload
    def IsAlwaysNormalized(self, form: NormalizationForm) -> bool:
        """

        :param form:
        :return:
        """
    @classmethod
    def RegisterProvider(cls, provider: EncodingProvider) -> None:
        """

        :param provider:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class EncodingInfo(Object):
    """"""

    @property
    def CodePage(self) -> int:
        """

        :return:
        """
    @property
    def DisplayName(self) -> str:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetEncoding(self) -> Encoding:
        """

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

class EncodingNLS(ABC, Encoding, ICloneable):
    """"""

    @classmethod
    @property
    def ASCII(cls) -> Encoding:
        """

        :return:
        """
    @classmethod
    @property
    def BigEndianUnicode(cls) -> Encoding:
        """

        :return:
        """
    @property
    def BodyName(self) -> str:
        """

        :return:
        """
    @property
    def CodePage(self) -> int:
        """

        :return:
        """
    @property
    def DecoderFallback(self) -> DecoderFallback:
        """

        :return:
        """
    @DecoderFallback.setter
    def DecoderFallback(self, value: DecoderFallback) -> None: ...
    @classmethod
    @property
    def Default(cls) -> Encoding:
        """

        :return:
        """
    @property
    def EncoderFallback(self) -> EncoderFallback:
        """

        :return:
        """
    @EncoderFallback.setter
    def EncoderFallback(self, value: EncoderFallback) -> None: ...
    @property
    def EncodingName(self) -> str:
        """

        :return:
        """
    @property
    def HeaderName(self) -> str:
        """

        :return:
        """
    @property
    def IsBrowserDisplay(self) -> bool:
        """

        :return:
        """
    @property
    def IsBrowserSave(self) -> bool:
        """

        :return:
        """
    @property
    def IsMailNewsDisplay(self) -> bool:
        """

        :return:
        """
    @property
    def IsMailNewsSave(self) -> bool:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def IsSingleByte(self) -> bool:
        """

        :return:
        """
    @classmethod
    @property
    def UTF32(cls) -> Encoding:
        """

        :return:
        """
    @classmethod
    @property
    def UTF7(cls) -> Encoding:
        """

        :return:
        """
    @classmethod
    @property
    def UTF8(cls) -> Encoding:
        """

        :return:
        """
    @classmethod
    @property
    def Unicode(cls) -> Encoding:
        """

        :return:
        """
    @property
    def WebName(self) -> str:
        """

        :return:
        """
    @property
    def WindowsCodePage(self) -> int:
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
    @overload
    def GetByteCount(self, chars: Array[Char]) -> int:
        """

        :param chars:
        :return:
        """
    @overload
    def GetByteCount(self, s: str) -> int:
        """

        :param s:
        :return:
        """
    @overload
    def GetByteCount(self, chars: Char, count: int) -> int:
        """

        :param chars:
        :param count:
        :return:
        """
    @overload
    def GetByteCount(self, chars: Array[Char], index: int, count: int) -> int:
        """

        :param chars:
        :param index:
        :param count:
        :return:
        """
    @overload
    def GetBytes(self, chars: Array[Char]) -> Array[int]:
        """

        :param chars:
        :return:
        """
    @overload
    def GetBytes(self, s: str) -> Array[int]:
        """

        :param s:
        :return:
        """
    @overload
    def GetBytes(self, chars: Array[Char], index: int, count: int) -> Array[int]:
        """

        :param chars:
        :param index:
        :param count:
        :return:
        """
    @overload
    def GetBytes(self, chars: Char, charCount: int, bytes: int, byteCount: int) -> int:
        """

        :param chars:
        :param charCount:
        :param bytes:
        :param byteCount:
        :return:
        """
    @overload
    def GetBytes(
        self, chars: Array[Char], charIndex: int, charCount: int, bytes: Array[int], byteIndex: int
    ) -> int:
        """

        :param chars:
        :param charIndex:
        :param charCount:
        :param bytes:
        :param byteIndex:
        :return:
        """
    @overload
    def GetBytes(
        self, s: str, charIndex: int, charCount: int, bytes: Array[int], byteIndex: int
    ) -> int:
        """

        :param s:
        :param charIndex:
        :param charCount:
        :param bytes:
        :param byteIndex:
        :return:
        """
    @overload
    def GetCharCount(self, bytes: Array[int]) -> int:
        """

        :param bytes:
        :return:
        """
    @overload
    def GetCharCount(self, bytes: int, count: int) -> int:
        """

        :param bytes:
        :param count:
        :return:
        """
    @overload
    def GetCharCount(self, bytes: Array[int], index: int, count: int) -> int:
        """

        :param bytes:
        :param index:
        :param count:
        :return:
        """
    @overload
    def GetChars(self, bytes: Array[int]) -> Array[Char]:
        """

        :param bytes:
        :return:
        """
    @overload
    def GetChars(self, bytes: Array[int], index: int, count: int) -> Array[Char]:
        """

        :param bytes:
        :param index:
        :param count:
        :return:
        """
    @overload
    def GetChars(self, bytes: int, byteCount: int, chars: Char, charCount: int) -> int:
        """

        :param bytes:
        :param byteCount:
        :param chars:
        :param charCount:
        :return:
        """
    @overload
    def GetChars(
        self, bytes: Array[int], byteIndex: int, byteCount: int, chars: Array[Char], charIndex: int
    ) -> int:
        """

        :param bytes:
        :param byteIndex:
        :param byteCount:
        :param chars:
        :param charIndex:
        :return:
        """
    def GetDecoder(self) -> Decoder:
        """

        :return:
        """
    def GetEncoder(self) -> Encoder:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetMaxByteCount(self, charCount: int) -> int:
        """

        :param charCount:
        :return:
        """
    def GetMaxCharCount(self, byteCount: int) -> int:
        """

        :param byteCount:
        :return:
        """
    def GetPreamble(self) -> Array[int]:
        """

        :return:
        """
    @overload
    def GetString(self, bytes: Array[int]) -> str:
        """

        :param bytes:
        :return:
        """
    @overload
    def GetString(self, bytes: int, byteCount: int) -> str:
        """

        :param bytes:
        :param byteCount:
        :return:
        """
    @overload
    def GetString(self, bytes: Array[int], index: int, count: int) -> str:
        """

        :param bytes:
        :param index:
        :param count:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def IsAlwaysNormalized(self) -> bool:
        """

        :return:
        """
    @overload
    def IsAlwaysNormalized(self, form: NormalizationForm) -> bool:
        """

        :param form:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class EncodingProvider(ABC, Object):
    """"""

    def __init__(self):
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetEncoding(self, codepage: int) -> Encoding:
        """

        :param codepage:
        :return:
        """
    @overload
    def GetEncoding(self, name: str) -> Encoding:
        """

        :param name:
        :return:
        """
    @overload
    def GetEncoding(
        self, codepage: int, encoderFallback: EncoderFallback, decoderFallback: DecoderFallback
    ) -> Encoding:
        """

        :param codepage:
        :param encoderFallback:
        :param decoderFallback:
        :return:
        """
    @overload
    def GetEncoding(
        self, name: str, encoderFallback: EncoderFallback, decoderFallback: DecoderFallback
    ) -> Encoding:
        """

        :param name:
        :param encoderFallback:
        :param decoderFallback:
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

    @classmethod
    @property
    def ASCII(cls) -> Encoding:
        """

        :return:
        """
    @classmethod
    @property
    def BigEndianUnicode(cls) -> Encoding:
        """

        :return:
        """
    @property
    def BodyName(self) -> str:
        """

        :return:
        """
    @property
    def CodePage(self) -> int:
        """

        :return:
        """
    @property
    def DecoderFallback(self) -> DecoderFallback:
        """

        :return:
        """
    @DecoderFallback.setter
    def DecoderFallback(self, value: DecoderFallback) -> None: ...
    @classmethod
    @property
    def Default(cls) -> Encoding:
        """

        :return:
        """
    @property
    def EncoderFallback(self) -> EncoderFallback:
        """

        :return:
        """
    @EncoderFallback.setter
    def EncoderFallback(self, value: EncoderFallback) -> None: ...
    @property
    def EncodingName(self) -> str:
        """

        :return:
        """
    @property
    def HeaderName(self) -> str:
        """

        :return:
        """
    @property
    def IsBrowserDisplay(self) -> bool:
        """

        :return:
        """
    @property
    def IsBrowserSave(self) -> bool:
        """

        :return:
        """
    @property
    def IsMailNewsDisplay(self) -> bool:
        """

        :return:
        """
    @property
    def IsMailNewsSave(self) -> bool:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def IsSingleByte(self) -> bool:
        """

        :return:
        """
    @classmethod
    @property
    def UTF32(cls) -> Encoding:
        """

        :return:
        """
    @classmethod
    @property
    def UTF7(cls) -> Encoding:
        """

        :return:
        """
    @classmethod
    @property
    def UTF8(cls) -> Encoding:
        """

        :return:
        """
    @classmethod
    @property
    def Unicode(cls) -> Encoding:
        """

        :return:
        """
    @property
    def WebName(self) -> str:
        """

        :return:
        """
    @property
    def WindowsCodePage(self) -> int:
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
    @overload
    def GetByteCount(self, chars: Array[Char]) -> int:
        """

        :param chars:
        :return:
        """
    @overload
    def GetByteCount(self, s: str) -> int:
        """

        :param s:
        :return:
        """
    @overload
    def GetByteCount(self, chars: Char, count: int) -> int:
        """

        :param chars:
        :param count:
        :return:
        """
    @overload
    def GetByteCount(self, chars: Array[Char], index: int, count: int) -> int:
        """

        :param chars:
        :param index:
        :param count:
        :return:
        """
    @overload
    def GetBytes(self, chars: Array[Char]) -> Array[int]:
        """

        :param chars:
        :return:
        """
    @overload
    def GetBytes(self, s: str) -> Array[int]:
        """

        :param s:
        :return:
        """
    @overload
    def GetBytes(self, chars: Array[Char], index: int, count: int) -> Array[int]:
        """

        :param chars:
        :param index:
        :param count:
        :return:
        """
    @overload
    def GetBytes(self, chars: Char, charCount: int, bytes: int, byteCount: int) -> int:
        """

        :param chars:
        :param charCount:
        :param bytes:
        :param byteCount:
        :return:
        """
    @overload
    def GetBytes(
        self, chars: Array[Char], charIndex: int, charCount: int, bytes: Array[int], byteIndex: int
    ) -> int:
        """

        :param chars:
        :param charIndex:
        :param charCount:
        :param bytes:
        :param byteIndex:
        :return:
        """
    @overload
    def GetBytes(
        self, s: str, charIndex: int, charCount: int, bytes: Array[int], byteIndex: int
    ) -> int:
        """

        :param s:
        :param charIndex:
        :param charCount:
        :param bytes:
        :param byteIndex:
        :return:
        """
    @overload
    def GetCharCount(self, bytes: Array[int]) -> int:
        """

        :param bytes:
        :return:
        """
    @overload
    def GetCharCount(self, bytes: int, count: int) -> int:
        """

        :param bytes:
        :param count:
        :return:
        """
    @overload
    def GetCharCount(self, bytes: Array[int], index: int, count: int) -> int:
        """

        :param bytes:
        :param index:
        :param count:
        :return:
        """
    @overload
    def GetChars(self, bytes: Array[int]) -> Array[Char]:
        """

        :param bytes:
        :return:
        """
    @overload
    def GetChars(self, bytes: Array[int], index: int, count: int) -> Array[Char]:
        """

        :param bytes:
        :param index:
        :param count:
        :return:
        """
    @overload
    def GetChars(self, bytes: int, byteCount: int, chars: Char, charCount: int) -> int:
        """

        :param bytes:
        :param byteCount:
        :param chars:
        :param charCount:
        :return:
        """
    @overload
    def GetChars(
        self, bytes: Array[int], byteIndex: int, byteCount: int, chars: Array[Char], charIndex: int
    ) -> int:
        """

        :param bytes:
        :param byteIndex:
        :param byteCount:
        :param chars:
        :param charIndex:
        :return:
        """
    def GetDecoder(self) -> Decoder:
        """

        :return:
        """
    def GetEncoder(self) -> Encoder:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetMaxByteCount(self, charCount: int) -> int:
        """

        :param charCount:
        :return:
        """
    def GetMaxCharCount(self, byteCount: int) -> int:
        """

        :param byteCount:
        :return:
        """
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    def GetPreamble(self) -> Array[int]:
        """

        :return:
        """
    @overload
    def GetString(self, bytes: Array[int]) -> str:
        """

        :param bytes:
        :return:
        """
    @overload
    def GetString(self, bytes: int, byteCount: int) -> str:
        """

        :param bytes:
        :param byteCount:
        :return:
        """
    @overload
    def GetString(self, bytes: Array[int], index: int, count: int) -> str:
        """

        :param bytes:
        :param index:
        :param count:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def IsAlwaysNormalized(self) -> bool:
        """

        :return:
        """
    @overload
    def IsAlwaysNormalized(self, form: NormalizationForm) -> bool:
        """

        :param form:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class ISCIIEncoding(EncodingNLS, ISerializable, ICloneable):
    """"""

    def __init__(self, codePage: int):
        """

        :param codePage:
        """
    @classmethod
    @property
    def ASCII(cls) -> Encoding:
        """

        :return:
        """
    @classmethod
    @property
    def BigEndianUnicode(cls) -> Encoding:
        """

        :return:
        """
    @property
    def BodyName(self) -> str:
        """

        :return:
        """
    @property
    def CodePage(self) -> int:
        """

        :return:
        """
    @property
    def DecoderFallback(self) -> DecoderFallback:
        """

        :return:
        """
    @DecoderFallback.setter
    def DecoderFallback(self, value: DecoderFallback) -> None: ...
    @classmethod
    @property
    def Default(cls) -> Encoding:
        """

        :return:
        """
    @property
    def EncoderFallback(self) -> EncoderFallback:
        """

        :return:
        """
    @EncoderFallback.setter
    def EncoderFallback(self, value: EncoderFallback) -> None: ...
    @property
    def EncodingName(self) -> str:
        """

        :return:
        """
    @property
    def HeaderName(self) -> str:
        """

        :return:
        """
    @property
    def IsBrowserDisplay(self) -> bool:
        """

        :return:
        """
    @property
    def IsBrowserSave(self) -> bool:
        """

        :return:
        """
    @property
    def IsMailNewsDisplay(self) -> bool:
        """

        :return:
        """
    @property
    def IsMailNewsSave(self) -> bool:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def IsSingleByte(self) -> bool:
        """

        :return:
        """
    @classmethod
    @property
    def UTF32(cls) -> Encoding:
        """

        :return:
        """
    @classmethod
    @property
    def UTF7(cls) -> Encoding:
        """

        :return:
        """
    @classmethod
    @property
    def UTF8(cls) -> Encoding:
        """

        :return:
        """
    @classmethod
    @property
    def Unicode(cls) -> Encoding:
        """

        :return:
        """
    @property
    def WebName(self) -> str:
        """

        :return:
        """
    @property
    def WindowsCodePage(self) -> int:
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
    @overload
    def GetByteCount(self, chars: Array[Char]) -> int:
        """

        :param chars:
        :return:
        """
    @overload
    def GetByteCount(self, s: str) -> int:
        """

        :param s:
        :return:
        """
    @overload
    def GetByteCount(self, chars: Char, count: int) -> int:
        """

        :param chars:
        :param count:
        :return:
        """
    @overload
    def GetByteCount(self, chars: Array[Char], index: int, count: int) -> int:
        """

        :param chars:
        :param index:
        :param count:
        :return:
        """
    @overload
    def GetBytes(self, chars: Array[Char]) -> Array[int]:
        """

        :param chars:
        :return:
        """
    @overload
    def GetBytes(self, s: str) -> Array[int]:
        """

        :param s:
        :return:
        """
    @overload
    def GetBytes(self, chars: Array[Char], index: int, count: int) -> Array[int]:
        """

        :param chars:
        :param index:
        :param count:
        :return:
        """
    @overload
    def GetBytes(self, chars: Char, charCount: int, bytes: int, byteCount: int) -> int:
        """

        :param chars:
        :param charCount:
        :param bytes:
        :param byteCount:
        :return:
        """
    @overload
    def GetBytes(
        self, chars: Array[Char], charIndex: int, charCount: int, bytes: Array[int], byteIndex: int
    ) -> int:
        """

        :param chars:
        :param charIndex:
        :param charCount:
        :param bytes:
        :param byteIndex:
        :return:
        """
    @overload
    def GetBytes(
        self, s: str, charIndex: int, charCount: int, bytes: Array[int], byteIndex: int
    ) -> int:
        """

        :param s:
        :param charIndex:
        :param charCount:
        :param bytes:
        :param byteIndex:
        :return:
        """
    @overload
    def GetCharCount(self, bytes: Array[int]) -> int:
        """

        :param bytes:
        :return:
        """
    @overload
    def GetCharCount(self, bytes: int, count: int) -> int:
        """

        :param bytes:
        :param count:
        :return:
        """
    @overload
    def GetCharCount(self, bytes: Array[int], index: int, count: int) -> int:
        """

        :param bytes:
        :param index:
        :param count:
        :return:
        """
    @overload
    def GetChars(self, bytes: Array[int]) -> Array[Char]:
        """

        :param bytes:
        :return:
        """
    @overload
    def GetChars(self, bytes: Array[int], index: int, count: int) -> Array[Char]:
        """

        :param bytes:
        :param index:
        :param count:
        :return:
        """
    @overload
    def GetChars(self, bytes: int, byteCount: int, chars: Char, charCount: int) -> int:
        """

        :param bytes:
        :param byteCount:
        :param chars:
        :param charCount:
        :return:
        """
    @overload
    def GetChars(
        self, bytes: Array[int], byteIndex: int, byteCount: int, chars: Array[Char], charIndex: int
    ) -> int:
        """

        :param bytes:
        :param byteIndex:
        :param byteCount:
        :param chars:
        :param charIndex:
        :return:
        """
    def GetDecoder(self) -> Decoder:
        """

        :return:
        """
    def GetEncoder(self) -> Encoder:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetMaxByteCount(self, charCount: int) -> int:
        """

        :param charCount:
        :return:
        """
    def GetMaxCharCount(self, byteCount: int) -> int:
        """

        :param byteCount:
        :return:
        """
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    def GetPreamble(self) -> Array[int]:
        """

        :return:
        """
    @overload
    def GetString(self, bytes: Array[int]) -> str:
        """

        :param bytes:
        :return:
        """
    @overload
    def GetString(self, bytes: int, byteCount: int) -> str:
        """

        :param bytes:
        :param byteCount:
        :return:
        """
    @overload
    def GetString(self, bytes: Array[int], index: int, count: int) -> str:
        """

        :param bytes:
        :param index:
        :param count:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def IsAlwaysNormalized(self) -> bool:
        """

        :return:
        """
    @overload
    def IsAlwaysNormalized(self, form: NormalizationForm) -> bool:
        """

        :param form:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class ISO2022Encoding(DBCSCodePageEncoding, ISerializable, ICloneable):
    """"""

    @classmethod
    @property
    def ASCII(cls) -> Encoding:
        """

        :return:
        """
    @classmethod
    @property
    def BigEndianUnicode(cls) -> Encoding:
        """

        :return:
        """
    @property
    def BodyName(self) -> str:
        """

        :return:
        """
    @property
    def CodePage(self) -> int:
        """

        :return:
        """
    @property
    def DecoderFallback(self) -> DecoderFallback:
        """

        :return:
        """
    @DecoderFallback.setter
    def DecoderFallback(self, value: DecoderFallback) -> None: ...
    @classmethod
    @property
    def Default(cls) -> Encoding:
        """

        :return:
        """
    @property
    def EncoderFallback(self) -> EncoderFallback:
        """

        :return:
        """
    @EncoderFallback.setter
    def EncoderFallback(self, value: EncoderFallback) -> None: ...
    @property
    def EncodingName(self) -> str:
        """

        :return:
        """
    @property
    def HeaderName(self) -> str:
        """

        :return:
        """
    @property
    def IsBrowserDisplay(self) -> bool:
        """

        :return:
        """
    @property
    def IsBrowserSave(self) -> bool:
        """

        :return:
        """
    @property
    def IsMailNewsDisplay(self) -> bool:
        """

        :return:
        """
    @property
    def IsMailNewsSave(self) -> bool:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def IsSingleByte(self) -> bool:
        """

        :return:
        """
    @classmethod
    @property
    def UTF32(cls) -> Encoding:
        """

        :return:
        """
    @classmethod
    @property
    def UTF7(cls) -> Encoding:
        """

        :return:
        """
    @classmethod
    @property
    def UTF8(cls) -> Encoding:
        """

        :return:
        """
    @classmethod
    @property
    def Unicode(cls) -> Encoding:
        """

        :return:
        """
    @property
    def WebName(self) -> str:
        """

        :return:
        """
    @property
    def WindowsCodePage(self) -> int:
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
    @overload
    def GetByteCount(self, chars: Array[Char]) -> int:
        """

        :param chars:
        :return:
        """
    @overload
    def GetByteCount(self, s: str) -> int:
        """

        :param s:
        :return:
        """
    @overload
    def GetByteCount(self, chars: Char, count: int) -> int:
        """

        :param chars:
        :param count:
        :return:
        """
    @overload
    def GetByteCount(self, chars: Array[Char], index: int, count: int) -> int:
        """

        :param chars:
        :param index:
        :param count:
        :return:
        """
    @overload
    def GetBytes(self, chars: Array[Char]) -> Array[int]:
        """

        :param chars:
        :return:
        """
    @overload
    def GetBytes(self, s: str) -> Array[int]:
        """

        :param s:
        :return:
        """
    @overload
    def GetBytes(self, chars: Array[Char], index: int, count: int) -> Array[int]:
        """

        :param chars:
        :param index:
        :param count:
        :return:
        """
    @overload
    def GetBytes(self, chars: Char, charCount: int, bytes: int, byteCount: int) -> int:
        """

        :param chars:
        :param charCount:
        :param bytes:
        :param byteCount:
        :return:
        """
    @overload
    def GetBytes(
        self, chars: Array[Char], charIndex: int, charCount: int, bytes: Array[int], byteIndex: int
    ) -> int:
        """

        :param chars:
        :param charIndex:
        :param charCount:
        :param bytes:
        :param byteIndex:
        :return:
        """
    @overload
    def GetBytes(
        self, s: str, charIndex: int, charCount: int, bytes: Array[int], byteIndex: int
    ) -> int:
        """

        :param s:
        :param charIndex:
        :param charCount:
        :param bytes:
        :param byteIndex:
        :return:
        """
    @overload
    def GetCharCount(self, bytes: Array[int]) -> int:
        """

        :param bytes:
        :return:
        """
    @overload
    def GetCharCount(self, bytes: int, count: int) -> int:
        """

        :param bytes:
        :param count:
        :return:
        """
    @overload
    def GetCharCount(self, bytes: Array[int], index: int, count: int) -> int:
        """

        :param bytes:
        :param index:
        :param count:
        :return:
        """
    @overload
    def GetChars(self, bytes: Array[int]) -> Array[Char]:
        """

        :param bytes:
        :return:
        """
    @overload
    def GetChars(self, bytes: Array[int], index: int, count: int) -> Array[Char]:
        """

        :param bytes:
        :param index:
        :param count:
        :return:
        """
    @overload
    def GetChars(self, bytes: int, byteCount: int, chars: Char, charCount: int) -> int:
        """

        :param bytes:
        :param byteCount:
        :param chars:
        :param charCount:
        :return:
        """
    @overload
    def GetChars(
        self, bytes: Array[int], byteIndex: int, byteCount: int, chars: Array[Char], charIndex: int
    ) -> int:
        """

        :param bytes:
        :param byteIndex:
        :param byteCount:
        :param chars:
        :param charIndex:
        :return:
        """
    def GetDecoder(self) -> Decoder:
        """

        :return:
        """
    def GetEncoder(self) -> Encoder:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetMaxByteCount(self, charCount: int) -> int:
        """

        :param charCount:
        :return:
        """
    def GetMaxCharCount(self, byteCount: int) -> int:
        """

        :param byteCount:
        :return:
        """
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    def GetPreamble(self) -> Array[int]:
        """

        :return:
        """
    @overload
    def GetString(self, bytes: Array[int]) -> str:
        """

        :param bytes:
        :return:
        """
    @overload
    def GetString(self, bytes: int, byteCount: int) -> str:
        """

        :param bytes:
        :param byteCount:
        :return:
        """
    @overload
    def GetString(self, bytes: Array[int], index: int, count: int) -> str:
        """

        :param bytes:
        :param index:
        :param count:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def IsAlwaysNormalized(self) -> bool:
        """

        :return:
        """
    @overload
    def IsAlwaysNormalized(self, form: NormalizationForm) -> bool:
        """

        :param form:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class InternalDecoderBestFitFallback(DecoderFallback):
    """"""

    @classmethod
    @property
    def ExceptionFallback(cls) -> DecoderFallback:
        """

        :return:
        """
    @property
    def MaxCharCount(self) -> int:
        """

        :return:
        """
    @classmethod
    @property
    def ReplacementFallback(cls) -> DecoderFallback:
        """

        :return:
        """
    def CreateFallbackBuffer(self) -> DecoderFallbackBuffer:
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

class InternalDecoderBestFitFallbackBuffer(DecoderFallbackBuffer):
    """"""

    def __init__(self, fallback: InternalDecoderBestFitFallback):
        """

        :param fallback:
        """
    @property
    def Remaining(self) -> int:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def Fallback(self, bytesUnknown: Array[int], index: int) -> bool:
        """

        :param bytesUnknown:
        :param index:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetNextChar(self) -> Char:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def MovePrevious(self) -> bool:
        """

        :return:
        """
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class InternalEncoderBestFitFallback(EncoderFallback):
    """"""

    @classmethod
    @property
    def ExceptionFallback(cls) -> EncoderFallback:
        """

        :return:
        """
    @property
    def MaxCharCount(self) -> int:
        """

        :return:
        """
    @classmethod
    @property
    def ReplacementFallback(cls) -> EncoderFallback:
        """

        :return:
        """
    def CreateFallbackBuffer(self) -> EncoderFallbackBuffer:
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

class InternalEncoderBestFitFallbackBuffer(EncoderFallbackBuffer):
    """"""

    def __init__(self, fallback: InternalEncoderBestFitFallback):
        """

        :param fallback:
        """
    @property
    def Remaining(self) -> int:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def Fallback(self, charUnknown: Char, index: int) -> bool:
        """

        :param charUnknown:
        :param index:
        :return:
        """
    @overload
    def Fallback(self, charUnknownHigh: Char, charUnknownLow: Char, index: int) -> bool:
        """

        :param charUnknownHigh:
        :param charUnknownLow:
        :param index:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetNextChar(self) -> Char:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def MovePrevious(self) -> bool:
        """

        :return:
        """
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class Latin1Encoding(EncodingNLS, ISerializable, ICloneable):
    """"""

    def __init__(self):
        """"""
    @classmethod
    @property
    def ASCII(cls) -> Encoding:
        """

        :return:
        """
    @classmethod
    @property
    def BigEndianUnicode(cls) -> Encoding:
        """

        :return:
        """
    @property
    def BodyName(self) -> str:
        """

        :return:
        """
    @property
    def CodePage(self) -> int:
        """

        :return:
        """
    @property
    def DecoderFallback(self) -> DecoderFallback:
        """

        :return:
        """
    @DecoderFallback.setter
    def DecoderFallback(self, value: DecoderFallback) -> None: ...
    @classmethod
    @property
    def Default(cls) -> Encoding:
        """

        :return:
        """
    @property
    def EncoderFallback(self) -> EncoderFallback:
        """

        :return:
        """
    @EncoderFallback.setter
    def EncoderFallback(self, value: EncoderFallback) -> None: ...
    @property
    def EncodingName(self) -> str:
        """

        :return:
        """
    @property
    def HeaderName(self) -> str:
        """

        :return:
        """
    @property
    def IsBrowserDisplay(self) -> bool:
        """

        :return:
        """
    @property
    def IsBrowserSave(self) -> bool:
        """

        :return:
        """
    @property
    def IsMailNewsDisplay(self) -> bool:
        """

        :return:
        """
    @property
    def IsMailNewsSave(self) -> bool:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def IsSingleByte(self) -> bool:
        """

        :return:
        """
    @classmethod
    @property
    def UTF32(cls) -> Encoding:
        """

        :return:
        """
    @classmethod
    @property
    def UTF7(cls) -> Encoding:
        """

        :return:
        """
    @classmethod
    @property
    def UTF8(cls) -> Encoding:
        """

        :return:
        """
    @classmethod
    @property
    def Unicode(cls) -> Encoding:
        """

        :return:
        """
    @property
    def WebName(self) -> str:
        """

        :return:
        """
    @property
    def WindowsCodePage(self) -> int:
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
    @overload
    def GetByteCount(self, chars: Array[Char]) -> int:
        """

        :param chars:
        :return:
        """
    @overload
    def GetByteCount(self, s: str) -> int:
        """

        :param s:
        :return:
        """
    @overload
    def GetByteCount(self, chars: Char, count: int) -> int:
        """

        :param chars:
        :param count:
        :return:
        """
    @overload
    def GetByteCount(self, chars: Array[Char], index: int, count: int) -> int:
        """

        :param chars:
        :param index:
        :param count:
        :return:
        """
    @overload
    def GetBytes(self, chars: Array[Char]) -> Array[int]:
        """

        :param chars:
        :return:
        """
    @overload
    def GetBytes(self, s: str) -> Array[int]:
        """

        :param s:
        :return:
        """
    @overload
    def GetBytes(self, chars: Array[Char], index: int, count: int) -> Array[int]:
        """

        :param chars:
        :param index:
        :param count:
        :return:
        """
    @overload
    def GetBytes(self, chars: Char, charCount: int, bytes: int, byteCount: int) -> int:
        """

        :param chars:
        :param charCount:
        :param bytes:
        :param byteCount:
        :return:
        """
    @overload
    def GetBytes(
        self, chars: Array[Char], charIndex: int, charCount: int, bytes: Array[int], byteIndex: int
    ) -> int:
        """

        :param chars:
        :param charIndex:
        :param charCount:
        :param bytes:
        :param byteIndex:
        :return:
        """
    @overload
    def GetBytes(
        self, s: str, charIndex: int, charCount: int, bytes: Array[int], byteIndex: int
    ) -> int:
        """

        :param s:
        :param charIndex:
        :param charCount:
        :param bytes:
        :param byteIndex:
        :return:
        """
    @overload
    def GetCharCount(self, bytes: Array[int]) -> int:
        """

        :param bytes:
        :return:
        """
    @overload
    def GetCharCount(self, bytes: int, count: int) -> int:
        """

        :param bytes:
        :param count:
        :return:
        """
    @overload
    def GetCharCount(self, bytes: Array[int], index: int, count: int) -> int:
        """

        :param bytes:
        :param index:
        :param count:
        :return:
        """
    @overload
    def GetChars(self, bytes: Array[int]) -> Array[Char]:
        """

        :param bytes:
        :return:
        """
    @overload
    def GetChars(self, bytes: Array[int], index: int, count: int) -> Array[Char]:
        """

        :param bytes:
        :param index:
        :param count:
        :return:
        """
    @overload
    def GetChars(self, bytes: int, byteCount: int, chars: Char, charCount: int) -> int:
        """

        :param bytes:
        :param byteCount:
        :param chars:
        :param charCount:
        :return:
        """
    @overload
    def GetChars(
        self, bytes: Array[int], byteIndex: int, byteCount: int, chars: Array[Char], charIndex: int
    ) -> int:
        """

        :param bytes:
        :param byteIndex:
        :param byteCount:
        :param chars:
        :param charIndex:
        :return:
        """
    def GetDecoder(self) -> Decoder:
        """

        :return:
        """
    def GetEncoder(self) -> Encoder:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetMaxByteCount(self, charCount: int) -> int:
        """

        :param charCount:
        :return:
        """
    def GetMaxCharCount(self, byteCount: int) -> int:
        """

        :param byteCount:
        :return:
        """
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    def GetPreamble(self) -> Array[int]:
        """

        :return:
        """
    @overload
    def GetString(self, bytes: Array[int]) -> str:
        """

        :param bytes:
        :return:
        """
    @overload
    def GetString(self, bytes: int, byteCount: int) -> str:
        """

        :param bytes:
        :param byteCount:
        :return:
        """
    @overload
    def GetString(self, bytes: Array[int], index: int, count: int) -> str:
        """

        :param bytes:
        :param index:
        :param count:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def IsAlwaysNormalized(self) -> bool:
        """

        :return:
        """
    @overload
    def IsAlwaysNormalized(self, form: NormalizationForm) -> bool:
        """

        :param form:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class MLangCodePageEncoding(Object, IObjectReference, ISerializable):
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
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    def GetRealObject(self, context: StreamingContext) -> object:
        """

        :param context:
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

class Normalization(Object):
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

    def __init__(self, codePage: int):
        """

        :param codePage:
        """
    @classmethod
    @property
    def ASCII(cls) -> Encoding:
        """

        :return:
        """
    @classmethod
    @property
    def BigEndianUnicode(cls) -> Encoding:
        """

        :return:
        """
    @property
    def BodyName(self) -> str:
        """

        :return:
        """
    @property
    def CodePage(self) -> int:
        """

        :return:
        """
    @property
    def DecoderFallback(self) -> DecoderFallback:
        """

        :return:
        """
    @DecoderFallback.setter
    def DecoderFallback(self, value: DecoderFallback) -> None: ...
    @classmethod
    @property
    def Default(cls) -> Encoding:
        """

        :return:
        """
    @property
    def EncoderFallback(self) -> EncoderFallback:
        """

        :return:
        """
    @EncoderFallback.setter
    def EncoderFallback(self, value: EncoderFallback) -> None: ...
    @property
    def EncodingName(self) -> str:
        """

        :return:
        """
    @property
    def HeaderName(self) -> str:
        """

        :return:
        """
    @property
    def IsBrowserDisplay(self) -> bool:
        """

        :return:
        """
    @property
    def IsBrowserSave(self) -> bool:
        """

        :return:
        """
    @property
    def IsMailNewsDisplay(self) -> bool:
        """

        :return:
        """
    @property
    def IsMailNewsSave(self) -> bool:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def IsSingleByte(self) -> bool:
        """

        :return:
        """
    @classmethod
    @property
    def UTF32(cls) -> Encoding:
        """

        :return:
        """
    @classmethod
    @property
    def UTF7(cls) -> Encoding:
        """

        :return:
        """
    @classmethod
    @property
    def UTF8(cls) -> Encoding:
        """

        :return:
        """
    @classmethod
    @property
    def Unicode(cls) -> Encoding:
        """

        :return:
        """
    @property
    def WebName(self) -> str:
        """

        :return:
        """
    @property
    def WindowsCodePage(self) -> int:
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
    @overload
    def GetByteCount(self, chars: Array[Char]) -> int:
        """

        :param chars:
        :return:
        """
    @overload
    def GetByteCount(self, s: str) -> int:
        """

        :param s:
        :return:
        """
    @overload
    def GetByteCount(self, chars: Char, count: int) -> int:
        """

        :param chars:
        :param count:
        :return:
        """
    @overload
    def GetByteCount(self, chars: Array[Char], index: int, count: int) -> int:
        """

        :param chars:
        :param index:
        :param count:
        :return:
        """
    @overload
    def GetBytes(self, chars: Array[Char]) -> Array[int]:
        """

        :param chars:
        :return:
        """
    @overload
    def GetBytes(self, s: str) -> Array[int]:
        """

        :param s:
        :return:
        """
    @overload
    def GetBytes(self, chars: Array[Char], index: int, count: int) -> Array[int]:
        """

        :param chars:
        :param index:
        :param count:
        :return:
        """
    @overload
    def GetBytes(self, chars: Char, charCount: int, bytes: int, byteCount: int) -> int:
        """

        :param chars:
        :param charCount:
        :param bytes:
        :param byteCount:
        :return:
        """
    @overload
    def GetBytes(
        self, chars: Array[Char], charIndex: int, charCount: int, bytes: Array[int], byteIndex: int
    ) -> int:
        """

        :param chars:
        :param charIndex:
        :param charCount:
        :param bytes:
        :param byteIndex:
        :return:
        """
    @overload
    def GetBytes(
        self, s: str, charIndex: int, charCount: int, bytes: Array[int], byteIndex: int
    ) -> int:
        """

        :param s:
        :param charIndex:
        :param charCount:
        :param bytes:
        :param byteIndex:
        :return:
        """
    @overload
    def GetCharCount(self, bytes: Array[int]) -> int:
        """

        :param bytes:
        :return:
        """
    @overload
    def GetCharCount(self, bytes: int, count: int) -> int:
        """

        :param bytes:
        :param count:
        :return:
        """
    @overload
    def GetCharCount(self, bytes: Array[int], index: int, count: int) -> int:
        """

        :param bytes:
        :param index:
        :param count:
        :return:
        """
    @overload
    def GetChars(self, bytes: Array[int]) -> Array[Char]:
        """

        :param bytes:
        :return:
        """
    @overload
    def GetChars(self, bytes: Array[int], index: int, count: int) -> Array[Char]:
        """

        :param bytes:
        :param index:
        :param count:
        :return:
        """
    @overload
    def GetChars(self, bytes: int, byteCount: int, chars: Char, charCount: int) -> int:
        """

        :param bytes:
        :param byteCount:
        :param chars:
        :param charCount:
        :return:
        """
    @overload
    def GetChars(
        self, bytes: Array[int], byteIndex: int, byteCount: int, chars: Array[Char], charIndex: int
    ) -> int:
        """

        :param bytes:
        :param byteIndex:
        :param byteCount:
        :param chars:
        :param charIndex:
        :return:
        """
    def GetDecoder(self) -> Decoder:
        """

        :return:
        """
    def GetEncoder(self) -> Encoder:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetMaxByteCount(self, charCount: int) -> int:
        """

        :param charCount:
        :return:
        """
    def GetMaxCharCount(self, byteCount: int) -> int:
        """

        :param byteCount:
        :return:
        """
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    def GetPreamble(self) -> Array[int]:
        """

        :return:
        """
    @overload
    def GetString(self, bytes: Array[int]) -> str:
        """

        :param bytes:
        :return:
        """
    @overload
    def GetString(self, bytes: int, byteCount: int) -> str:
        """

        :param bytes:
        :param byteCount:
        :return:
        """
    @overload
    def GetString(self, bytes: Array[int], index: int, count: int) -> str:
        """

        :param bytes:
        :param index:
        :param count:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def IsAlwaysNormalized(self) -> bool:
        """

        :return:
        """
    @overload
    def IsAlwaysNormalized(self, form: NormalizationForm) -> bool:
        """

        :param form:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class StringBuilder(Object, ISerializable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, capacity: int):
        """

        :param capacity:
        """
    @overload
    def __init__(self, value: str):
        """

        :param value:
        """
    @overload
    def __init__(self, capacity: int, maxCapacity: int):
        """

        :param capacity:
        :param maxCapacity:
        """
    @overload
    def __init__(self, value: str, capacity: int):
        """

        :param value:
        :param capacity:
        """
    @overload
    def __init__(self, value: str, startIndex: int, length: int, capacity: int):
        """

        :param value:
        :param startIndex:
        :param length:
        :param capacity:
        """
    @property
    def Capacity(self) -> int:
        """

        :return:
        """
    @Capacity.setter
    def Capacity(self, value: int) -> None: ...
    @property
    def Chars(self) -> Char:
        """

        :return:
        """
    @Chars.setter
    def Chars(self, value: Char) -> None: ...
    @property
    def Length(self) -> int:
        """

        :return:
        """
    @Length.setter
    def Length(self, value: int) -> None: ...
    @property
    def MaxCapacity(self) -> int:
        """

        :return:
        """
    @overload
    def Append(self, value: Array[Char]) -> StringBuilder:
        """

        :param value:
        :return:
        """
    @overload
    def Append(self, value: bool) -> StringBuilder:
        """

        :param value:
        :return:
        """
    @overload
    def Append(self, value: int) -> StringBuilder:
        """

        :param value:
        :return:
        """
    @overload
    def Append(self, value: Char) -> StringBuilder:
        """

        :param value:
        :return:
        """
    @overload
    def Append(self, value: Decimal) -> StringBuilder:
        """

        :param value:
        :return:
        """
    @overload
    def Append(self, value: float) -> StringBuilder:
        """

        :param value:
        :return:
        """
    @overload
    def Append(self, value: int) -> StringBuilder:
        """

        :param value:
        :return:
        """
    @overload
    def Append(self, value: int) -> StringBuilder:
        """

        :param value:
        :return:
        """
    @overload
    def Append(self, value: int) -> StringBuilder:
        """

        :param value:
        :return:
        """
    @overload
    def Append(self, value: object) -> StringBuilder:
        """

        :param value:
        :return:
        """
    @overload
    def Append(self, value: int) -> StringBuilder:
        """

        :param value:
        :return:
        """
    @overload
    def Append(self, value: float) -> StringBuilder:
        """

        :param value:
        :return:
        """
    @overload
    def Append(self, value: str) -> StringBuilder:
        """

        :param value:
        :return:
        """
    @overload
    def Append(self, value: int) -> StringBuilder:
        """

        :param value:
        :return:
        """
    @overload
    def Append(self, value: int) -> StringBuilder:
        """

        :param value:
        :return:
        """
    @overload
    def Append(self, value: int) -> StringBuilder:
        """

        :param value:
        :return:
        """
    @overload
    def Append(self, value: Char, valueCount: int) -> StringBuilder:
        """

        :param value:
        :param valueCount:
        :return:
        """
    @overload
    def Append(self, value: Array[Char], startIndex: int, charCount: int) -> StringBuilder:
        """

        :param value:
        :param startIndex:
        :param charCount:
        :return:
        """
    @overload
    def Append(self, value: str, startIndex: int, count: int) -> StringBuilder:
        """

        :param value:
        :param startIndex:
        :param count:
        :return:
        """
    @overload
    def AppendFormat(self, format: str, args: Array[object]) -> StringBuilder:
        """

        :param format:
        :param args:
        :return:
        """
    @overload
    def AppendFormat(self, format: str, arg0: object) -> StringBuilder:
        """

        :param format:
        :param arg0:
        :return:
        """
    @overload
    def AppendFormat(
        self, provider: IFormatProvider, format: str, args: Array[object]
    ) -> StringBuilder:
        """

        :param provider:
        :param format:
        :param args:
        :return:
        """
    @overload
    def AppendFormat(self, provider: IFormatProvider, format: str, arg0: object) -> StringBuilder:
        """

        :param provider:
        :param format:
        :param arg0:
        :return:
        """
    @overload
    def AppendFormat(self, format: str, arg0: object, arg1: object) -> StringBuilder:
        """

        :param format:
        :param arg0:
        :param arg1:
        :return:
        """
    @overload
    def AppendFormat(
        self, provider: IFormatProvider, format: str, arg0: object, arg1: object
    ) -> StringBuilder:
        """

        :param provider:
        :param format:
        :param arg0:
        :param arg1:
        :return:
        """
    @overload
    def AppendFormat(self, format: str, arg0: object, arg1: object, arg2: object) -> StringBuilder:
        """

        :param format:
        :param arg0:
        :param arg1:
        :param arg2:
        :return:
        """
    @overload
    def AppendFormat(
        self, provider: IFormatProvider, format: str, arg0: object, arg1: object, arg2: object
    ) -> StringBuilder:
        """

        :param provider:
        :param format:
        :param arg0:
        :param arg1:
        :param arg2:
        :return:
        """
    @overload
    def AppendLine(self) -> StringBuilder:
        """

        :return:
        """
    @overload
    def AppendLine(self, value: str) -> StringBuilder:
        """

        :param value:
        :return:
        """
    def Clear(self) -> StringBuilder:
        """

        :return:
        """
    def CopyTo(
        self, sourceIndex: int, destination: Array[Char], destinationIndex: int, count: int
    ) -> None:
        """

        :param sourceIndex:
        :param destination:
        :param destinationIndex:
        :param count:
        """
    def EnsureCapacity(self, capacity: int) -> int:
        """

        :param capacity:
        :return:
        """
    @overload
    def Equals(self, sb: StringBuilder) -> bool:
        """

        :param sb:
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
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def Insert(self, index: int, value: Array[Char]) -> StringBuilder:
        """

        :param index:
        :param value:
        :return:
        """
    @overload
    def Insert(self, index: int, value: bool) -> StringBuilder:
        """

        :param index:
        :param value:
        :return:
        """
    @overload
    def Insert(self, index: int, value: int) -> StringBuilder:
        """

        :param index:
        :param value:
        :return:
        """
    @overload
    def Insert(self, index: int, value: Char) -> StringBuilder:
        """

        :param index:
        :param value:
        :return:
        """
    @overload
    def Insert(self, index: int, value: Decimal) -> StringBuilder:
        """

        :param index:
        :param value:
        :return:
        """
    @overload
    def Insert(self, index: int, value: float) -> StringBuilder:
        """

        :param index:
        :param value:
        :return:
        """
    @overload
    def Insert(self, index: int, value: int) -> StringBuilder:
        """

        :param index:
        :param value:
        :return:
        """
    @overload
    def Insert(self, index: int, value: int) -> StringBuilder:
        """

        :param index:
        :param value:
        :return:
        """
    @overload
    def Insert(self, index: int, value: int) -> StringBuilder:
        """

        :param index:
        :param value:
        :return:
        """
    @overload
    def Insert(self, index: int, value: object) -> StringBuilder:
        """

        :param index:
        :param value:
        :return:
        """
    @overload
    def Insert(self, index: int, value: int) -> StringBuilder:
        """

        :param index:
        :param value:
        :return:
        """
    @overload
    def Insert(self, index: int, value: float) -> StringBuilder:
        """

        :param index:
        :param value:
        :return:
        """
    @overload
    def Insert(self, index: int, value: str) -> StringBuilder:
        """

        :param index:
        :param value:
        :return:
        """
    @overload
    def Insert(self, index: int, value: int) -> StringBuilder:
        """

        :param index:
        :param value:
        :return:
        """
    @overload
    def Insert(self, index: int, value: int) -> StringBuilder:
        """

        :param index:
        :param value:
        :return:
        """
    @overload
    def Insert(self, index: int, value: int) -> StringBuilder:
        """

        :param index:
        :param value:
        :return:
        """
    @overload
    def Insert(self, index: int, value: str, count: int) -> StringBuilder:
        """

        :param index:
        :param value:
        :param count:
        :return:
        """
    @overload
    def Insert(
        self, index: int, value: Array[Char], startIndex: int, charCount: int
    ) -> StringBuilder:
        """

        :param index:
        :param value:
        :param startIndex:
        :param charCount:
        :return:
        """
    def Remove(self, startIndex: int, length: int) -> StringBuilder:
        """

        :param startIndex:
        :param length:
        :return:
        """
    @overload
    def Replace(self, oldChar: Char, newChar: Char) -> StringBuilder:
        """

        :param oldChar:
        :param newChar:
        :return:
        """
    @overload
    def Replace(self, oldValue: str, newValue: str) -> StringBuilder:
        """

        :param oldValue:
        :param newValue:
        :return:
        """
    @overload
    def Replace(self, oldChar: Char, newChar: Char, startIndex: int, count: int) -> StringBuilder:
        """

        :param oldChar:
        :param newChar:
        :param startIndex:
        :param count:
        :return:
        """
    @overload
    def Replace(self, oldValue: str, newValue: str, startIndex: int, count: int) -> StringBuilder:
        """

        :param oldValue:
        :param newValue:
        :param startIndex:
        :param count:
        :return:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def ToString(self, startIndex: int, length: int) -> str:
        """

        :param startIndex:
        :param length:
        :return:
        """

class StringBuilderCache(ABC, Object):
    """"""

    @classmethod
    def Acquire(cls, capacity: int = ...) -> StringBuilder:
        """

        :param capacity:
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
    @classmethod
    def GetStringAndRelease(cls, sb: StringBuilder) -> str:
        """

        :param sb:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @classmethod
    def Release(cls, sb: StringBuilder) -> None:
        """

        :param sb:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class SurrogateEncoder(Object, IObjectReference, ISerializable):
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
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    def GetRealObject(self, context: StreamingContext) -> object:
        """

        :param context:
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

class UTF32Encoding(Encoding, ICloneable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, bigEndian: bool, byteOrderMark: bool):
        """

        :param bigEndian:
        :param byteOrderMark:
        """
    @overload
    def __init__(self, bigEndian: bool, byteOrderMark: bool, throwOnInvalidCharacters: bool):
        """

        :param bigEndian:
        :param byteOrderMark:
        :param throwOnInvalidCharacters:
        """
    @classmethod
    @property
    def ASCII(cls) -> Encoding:
        """

        :return:
        """
    @classmethod
    @property
    def BigEndianUnicode(cls) -> Encoding:
        """

        :return:
        """
    @property
    def BodyName(self) -> str:
        """

        :return:
        """
    @property
    def CodePage(self) -> int:
        """

        :return:
        """
    @property
    def DecoderFallback(self) -> DecoderFallback:
        """

        :return:
        """
    @DecoderFallback.setter
    def DecoderFallback(self, value: DecoderFallback) -> None: ...
    @classmethod
    @property
    def Default(cls) -> Encoding:
        """

        :return:
        """
    @property
    def EncoderFallback(self) -> EncoderFallback:
        """

        :return:
        """
    @EncoderFallback.setter
    def EncoderFallback(self, value: EncoderFallback) -> None: ...
    @property
    def EncodingName(self) -> str:
        """

        :return:
        """
    @property
    def HeaderName(self) -> str:
        """

        :return:
        """
    @property
    def IsBrowserDisplay(self) -> bool:
        """

        :return:
        """
    @property
    def IsBrowserSave(self) -> bool:
        """

        :return:
        """
    @property
    def IsMailNewsDisplay(self) -> bool:
        """

        :return:
        """
    @property
    def IsMailNewsSave(self) -> bool:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def IsSingleByte(self) -> bool:
        """

        :return:
        """
    @classmethod
    @property
    def UTF32(cls) -> Encoding:
        """

        :return:
        """
    @classmethod
    @property
    def UTF7(cls) -> Encoding:
        """

        :return:
        """
    @classmethod
    @property
    def UTF8(cls) -> Encoding:
        """

        :return:
        """
    @classmethod
    @property
    def Unicode(cls) -> Encoding:
        """

        :return:
        """
    @property
    def WebName(self) -> str:
        """

        :return:
        """
    @property
    def WindowsCodePage(self) -> int:
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
    @overload
    def GetByteCount(self, chars: Array[Char]) -> int:
        """

        :param chars:
        :return:
        """
    @overload
    def GetByteCount(self, s: str) -> int:
        """

        :param s:
        :return:
        """
    @overload
    def GetByteCount(self, chars: Char, count: int) -> int:
        """

        :param chars:
        :param count:
        :return:
        """
    @overload
    def GetByteCount(self, chars: Array[Char], index: int, count: int) -> int:
        """

        :param chars:
        :param index:
        :param count:
        :return:
        """
    @overload
    def GetBytes(self, chars: Array[Char]) -> Array[int]:
        """

        :param chars:
        :return:
        """
    @overload
    def GetBytes(self, s: str) -> Array[int]:
        """

        :param s:
        :return:
        """
    @overload
    def GetBytes(self, chars: Array[Char], index: int, count: int) -> Array[int]:
        """

        :param chars:
        :param index:
        :param count:
        :return:
        """
    @overload
    def GetBytes(self, chars: Char, charCount: int, bytes: int, byteCount: int) -> int:
        """

        :param chars:
        :param charCount:
        :param bytes:
        :param byteCount:
        :return:
        """
    @overload
    def GetBytes(
        self, chars: Array[Char], charIndex: int, charCount: int, bytes: Array[int], byteIndex: int
    ) -> int:
        """

        :param chars:
        :param charIndex:
        :param charCount:
        :param bytes:
        :param byteIndex:
        :return:
        """
    @overload
    def GetBytes(
        self, s: str, charIndex: int, charCount: int, bytes: Array[int], byteIndex: int
    ) -> int:
        """

        :param s:
        :param charIndex:
        :param charCount:
        :param bytes:
        :param byteIndex:
        :return:
        """
    @overload
    def GetCharCount(self, bytes: Array[int]) -> int:
        """

        :param bytes:
        :return:
        """
    @overload
    def GetCharCount(self, bytes: int, count: int) -> int:
        """

        :param bytes:
        :param count:
        :return:
        """
    @overload
    def GetCharCount(self, bytes: Array[int], index: int, count: int) -> int:
        """

        :param bytes:
        :param index:
        :param count:
        :return:
        """
    @overload
    def GetChars(self, bytes: Array[int]) -> Array[Char]:
        """

        :param bytes:
        :return:
        """
    @overload
    def GetChars(self, bytes: Array[int], index: int, count: int) -> Array[Char]:
        """

        :param bytes:
        :param index:
        :param count:
        :return:
        """
    @overload
    def GetChars(self, bytes: int, byteCount: int, chars: Char, charCount: int) -> int:
        """

        :param bytes:
        :param byteCount:
        :param chars:
        :param charCount:
        :return:
        """
    @overload
    def GetChars(
        self, bytes: Array[int], byteIndex: int, byteCount: int, chars: Array[Char], charIndex: int
    ) -> int:
        """

        :param bytes:
        :param byteIndex:
        :param byteCount:
        :param chars:
        :param charIndex:
        :return:
        """
    def GetDecoder(self) -> Decoder:
        """

        :return:
        """
    def GetEncoder(self) -> Encoder:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetMaxByteCount(self, charCount: int) -> int:
        """

        :param charCount:
        :return:
        """
    def GetMaxCharCount(self, byteCount: int) -> int:
        """

        :param byteCount:
        :return:
        """
    def GetPreamble(self) -> Array[int]:
        """

        :return:
        """
    @overload
    def GetString(self, bytes: Array[int]) -> str:
        """

        :param bytes:
        :return:
        """
    @overload
    def GetString(self, bytes: int, byteCount: int) -> str:
        """

        :param bytes:
        :param byteCount:
        :return:
        """
    @overload
    def GetString(self, bytes: Array[int], index: int, count: int) -> str:
        """

        :param bytes:
        :param index:
        :param count:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def IsAlwaysNormalized(self) -> bool:
        """

        :return:
        """
    @overload
    def IsAlwaysNormalized(self, form: NormalizationForm) -> bool:
        """

        :param form:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class UTF7Encoding(Encoding, ICloneable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, allowOptionals: bool):
        """

        :param allowOptionals:
        """
    @classmethod
    @property
    def ASCII(cls) -> Encoding:
        """

        :return:
        """
    @classmethod
    @property
    def BigEndianUnicode(cls) -> Encoding:
        """

        :return:
        """
    @property
    def BodyName(self) -> str:
        """

        :return:
        """
    @property
    def CodePage(self) -> int:
        """

        :return:
        """
    @property
    def DecoderFallback(self) -> DecoderFallback:
        """

        :return:
        """
    @DecoderFallback.setter
    def DecoderFallback(self, value: DecoderFallback) -> None: ...
    @classmethod
    @property
    def Default(cls) -> Encoding:
        """

        :return:
        """
    @property
    def EncoderFallback(self) -> EncoderFallback:
        """

        :return:
        """
    @EncoderFallback.setter
    def EncoderFallback(self, value: EncoderFallback) -> None: ...
    @property
    def EncodingName(self) -> str:
        """

        :return:
        """
    @property
    def HeaderName(self) -> str:
        """

        :return:
        """
    @property
    def IsBrowserDisplay(self) -> bool:
        """

        :return:
        """
    @property
    def IsBrowserSave(self) -> bool:
        """

        :return:
        """
    @property
    def IsMailNewsDisplay(self) -> bool:
        """

        :return:
        """
    @property
    def IsMailNewsSave(self) -> bool:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def IsSingleByte(self) -> bool:
        """

        :return:
        """
    @classmethod
    @property
    def UTF32(cls) -> Encoding:
        """

        :return:
        """
    @classmethod
    @property
    def UTF7(cls) -> Encoding:
        """

        :return:
        """
    @classmethod
    @property
    def UTF8(cls) -> Encoding:
        """

        :return:
        """
    @classmethod
    @property
    def Unicode(cls) -> Encoding:
        """

        :return:
        """
    @property
    def WebName(self) -> str:
        """

        :return:
        """
    @property
    def WindowsCodePage(self) -> int:
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
    @overload
    def GetByteCount(self, chars: Array[Char]) -> int:
        """

        :param chars:
        :return:
        """
    @overload
    def GetByteCount(self, s: str) -> int:
        """

        :param s:
        :return:
        """
    @overload
    def GetByteCount(self, chars: Char, count: int) -> int:
        """

        :param chars:
        :param count:
        :return:
        """
    @overload
    def GetByteCount(self, chars: Array[Char], index: int, count: int) -> int:
        """

        :param chars:
        :param index:
        :param count:
        :return:
        """
    @overload
    def GetBytes(self, chars: Array[Char]) -> Array[int]:
        """

        :param chars:
        :return:
        """
    @overload
    def GetBytes(self, s: str) -> Array[int]:
        """

        :param s:
        :return:
        """
    @overload
    def GetBytes(self, chars: Array[Char], index: int, count: int) -> Array[int]:
        """

        :param chars:
        :param index:
        :param count:
        :return:
        """
    @overload
    def GetBytes(self, chars: Char, charCount: int, bytes: int, byteCount: int) -> int:
        """

        :param chars:
        :param charCount:
        :param bytes:
        :param byteCount:
        :return:
        """
    @overload
    def GetBytes(
        self, chars: Array[Char], charIndex: int, charCount: int, bytes: Array[int], byteIndex: int
    ) -> int:
        """

        :param chars:
        :param charIndex:
        :param charCount:
        :param bytes:
        :param byteIndex:
        :return:
        """
    @overload
    def GetBytes(
        self, s: str, charIndex: int, charCount: int, bytes: Array[int], byteIndex: int
    ) -> int:
        """

        :param s:
        :param charIndex:
        :param charCount:
        :param bytes:
        :param byteIndex:
        :return:
        """
    @overload
    def GetCharCount(self, bytes: Array[int]) -> int:
        """

        :param bytes:
        :return:
        """
    @overload
    def GetCharCount(self, bytes: int, count: int) -> int:
        """

        :param bytes:
        :param count:
        :return:
        """
    @overload
    def GetCharCount(self, bytes: Array[int], index: int, count: int) -> int:
        """

        :param bytes:
        :param index:
        :param count:
        :return:
        """
    @overload
    def GetChars(self, bytes: Array[int]) -> Array[Char]:
        """

        :param bytes:
        :return:
        """
    @overload
    def GetChars(self, bytes: Array[int], index: int, count: int) -> Array[Char]:
        """

        :param bytes:
        :param index:
        :param count:
        :return:
        """
    @overload
    def GetChars(self, bytes: int, byteCount: int, chars: Char, charCount: int) -> int:
        """

        :param bytes:
        :param byteCount:
        :param chars:
        :param charCount:
        :return:
        """
    @overload
    def GetChars(
        self, bytes: Array[int], byteIndex: int, byteCount: int, chars: Array[Char], charIndex: int
    ) -> int:
        """

        :param bytes:
        :param byteIndex:
        :param byteCount:
        :param chars:
        :param charIndex:
        :return:
        """
    def GetDecoder(self) -> Decoder:
        """

        :return:
        """
    def GetEncoder(self) -> Encoder:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetMaxByteCount(self, charCount: int) -> int:
        """

        :param charCount:
        :return:
        """
    def GetMaxCharCount(self, byteCount: int) -> int:
        """

        :param byteCount:
        :return:
        """
    def GetPreamble(self) -> Array[int]:
        """

        :return:
        """
    @overload
    def GetString(self, bytes: Array[int]) -> str:
        """

        :param bytes:
        :return:
        """
    @overload
    def GetString(self, bytes: int, byteCount: int) -> str:
        """

        :param bytes:
        :param byteCount:
        :return:
        """
    @overload
    def GetString(self, bytes: Array[int], index: int, count: int) -> str:
        """

        :param bytes:
        :param index:
        :param count:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def IsAlwaysNormalized(self) -> bool:
        """

        :return:
        """
    @overload
    def IsAlwaysNormalized(self, form: NormalizationForm) -> bool:
        """

        :param form:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class UTF8Encoding(Encoding, ICloneable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, encoderShouldEmitUTF8Identifier: bool):
        """

        :param encoderShouldEmitUTF8Identifier:
        """
    @overload
    def __init__(self, encoderShouldEmitUTF8Identifier: bool, throwOnInvalidBytes: bool):
        """

        :param encoderShouldEmitUTF8Identifier:
        :param throwOnInvalidBytes:
        """
    @classmethod
    @property
    def ASCII(cls) -> Encoding:
        """

        :return:
        """
    @classmethod
    @property
    def BigEndianUnicode(cls) -> Encoding:
        """

        :return:
        """
    @property
    def BodyName(self) -> str:
        """

        :return:
        """
    @property
    def CodePage(self) -> int:
        """

        :return:
        """
    @property
    def DecoderFallback(self) -> DecoderFallback:
        """

        :return:
        """
    @DecoderFallback.setter
    def DecoderFallback(self, value: DecoderFallback) -> None: ...
    @classmethod
    @property
    def Default(cls) -> Encoding:
        """

        :return:
        """
    @property
    def EncoderFallback(self) -> EncoderFallback:
        """

        :return:
        """
    @EncoderFallback.setter
    def EncoderFallback(self, value: EncoderFallback) -> None: ...
    @property
    def EncodingName(self) -> str:
        """

        :return:
        """
    @property
    def HeaderName(self) -> str:
        """

        :return:
        """
    @property
    def IsBrowserDisplay(self) -> bool:
        """

        :return:
        """
    @property
    def IsBrowserSave(self) -> bool:
        """

        :return:
        """
    @property
    def IsMailNewsDisplay(self) -> bool:
        """

        :return:
        """
    @property
    def IsMailNewsSave(self) -> bool:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def IsSingleByte(self) -> bool:
        """

        :return:
        """
    @classmethod
    @property
    def UTF32(cls) -> Encoding:
        """

        :return:
        """
    @classmethod
    @property
    def UTF7(cls) -> Encoding:
        """

        :return:
        """
    @classmethod
    @property
    def UTF8(cls) -> Encoding:
        """

        :return:
        """
    @classmethod
    @property
    def Unicode(cls) -> Encoding:
        """

        :return:
        """
    @property
    def WebName(self) -> str:
        """

        :return:
        """
    @property
    def WindowsCodePage(self) -> int:
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
    @overload
    def GetByteCount(self, chars: Array[Char]) -> int:
        """

        :param chars:
        :return:
        """
    @overload
    def GetByteCount(self, s: str) -> int:
        """

        :param s:
        :return:
        """
    @overload
    def GetByteCount(self, chars: Char, count: int) -> int:
        """

        :param chars:
        :param count:
        :return:
        """
    @overload
    def GetByteCount(self, chars: Array[Char], index: int, count: int) -> int:
        """

        :param chars:
        :param index:
        :param count:
        :return:
        """
    @overload
    def GetBytes(self, chars: Array[Char]) -> Array[int]:
        """

        :param chars:
        :return:
        """
    @overload
    def GetBytes(self, s: str) -> Array[int]:
        """

        :param s:
        :return:
        """
    @overload
    def GetBytes(self, chars: Array[Char], index: int, count: int) -> Array[int]:
        """

        :param chars:
        :param index:
        :param count:
        :return:
        """
    @overload
    def GetBytes(self, chars: Char, charCount: int, bytes: int, byteCount: int) -> int:
        """

        :param chars:
        :param charCount:
        :param bytes:
        :param byteCount:
        :return:
        """
    @overload
    def GetBytes(
        self, chars: Array[Char], charIndex: int, charCount: int, bytes: Array[int], byteIndex: int
    ) -> int:
        """

        :param chars:
        :param charIndex:
        :param charCount:
        :param bytes:
        :param byteIndex:
        :return:
        """
    @overload
    def GetBytes(
        self, s: str, charIndex: int, charCount: int, bytes: Array[int], byteIndex: int
    ) -> int:
        """

        :param s:
        :param charIndex:
        :param charCount:
        :param bytes:
        :param byteIndex:
        :return:
        """
    @overload
    def GetCharCount(self, bytes: Array[int]) -> int:
        """

        :param bytes:
        :return:
        """
    @overload
    def GetCharCount(self, bytes: int, count: int) -> int:
        """

        :param bytes:
        :param count:
        :return:
        """
    @overload
    def GetCharCount(self, bytes: Array[int], index: int, count: int) -> int:
        """

        :param bytes:
        :param index:
        :param count:
        :return:
        """
    @overload
    def GetChars(self, bytes: Array[int]) -> Array[Char]:
        """

        :param bytes:
        :return:
        """
    @overload
    def GetChars(self, bytes: Array[int], index: int, count: int) -> Array[Char]:
        """

        :param bytes:
        :param index:
        :param count:
        :return:
        """
    @overload
    def GetChars(self, bytes: int, byteCount: int, chars: Char, charCount: int) -> int:
        """

        :param bytes:
        :param byteCount:
        :param chars:
        :param charCount:
        :return:
        """
    @overload
    def GetChars(
        self, bytes: Array[int], byteIndex: int, byteCount: int, chars: Array[Char], charIndex: int
    ) -> int:
        """

        :param bytes:
        :param byteIndex:
        :param byteCount:
        :param chars:
        :param charIndex:
        :return:
        """
    def GetDecoder(self) -> Decoder:
        """

        :return:
        """
    def GetEncoder(self) -> Encoder:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetMaxByteCount(self, charCount: int) -> int:
        """

        :param charCount:
        :return:
        """
    def GetMaxCharCount(self, byteCount: int) -> int:
        """

        :param byteCount:
        :return:
        """
    def GetPreamble(self) -> Array[int]:
        """

        :return:
        """
    @overload
    def GetString(self, bytes: Array[int]) -> str:
        """

        :param bytes:
        :return:
        """
    @overload
    def GetString(self, bytes: int, byteCount: int) -> str:
        """

        :param bytes:
        :param byteCount:
        :return:
        """
    @overload
    def GetString(self, bytes: Array[int], index: int, count: int) -> str:
        """

        :param bytes:
        :param index:
        :param count:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def IsAlwaysNormalized(self) -> bool:
        """

        :return:
        """
    @overload
    def IsAlwaysNormalized(self, form: NormalizationForm) -> bool:
        """

        :param form:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class UnicodeEncoding(Encoding, ICloneable):
    """"""

    CharSize: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, bigEndian: bool, byteOrderMark: bool):
        """

        :param bigEndian:
        :param byteOrderMark:
        """
    @overload
    def __init__(self, bigEndian: bool, byteOrderMark: bool, throwOnInvalidBytes: bool):
        """

        :param bigEndian:
        :param byteOrderMark:
        :param throwOnInvalidBytes:
        """
    @classmethod
    @property
    def ASCII(cls) -> Encoding:
        """

        :return:
        """
    @classmethod
    @property
    def BigEndianUnicode(cls) -> Encoding:
        """

        :return:
        """
    @property
    def BodyName(self) -> str:
        """

        :return:
        """
    @property
    def CodePage(self) -> int:
        """

        :return:
        """
    @property
    def DecoderFallback(self) -> DecoderFallback:
        """

        :return:
        """
    @DecoderFallback.setter
    def DecoderFallback(self, value: DecoderFallback) -> None: ...
    @classmethod
    @property
    def Default(cls) -> Encoding:
        """

        :return:
        """
    @property
    def EncoderFallback(self) -> EncoderFallback:
        """

        :return:
        """
    @EncoderFallback.setter
    def EncoderFallback(self, value: EncoderFallback) -> None: ...
    @property
    def EncodingName(self) -> str:
        """

        :return:
        """
    @property
    def HeaderName(self) -> str:
        """

        :return:
        """
    @property
    def IsBrowserDisplay(self) -> bool:
        """

        :return:
        """
    @property
    def IsBrowserSave(self) -> bool:
        """

        :return:
        """
    @property
    def IsMailNewsDisplay(self) -> bool:
        """

        :return:
        """
    @property
    def IsMailNewsSave(self) -> bool:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def IsSingleByte(self) -> bool:
        """

        :return:
        """
    @classmethod
    @property
    def UTF32(cls) -> Encoding:
        """

        :return:
        """
    @classmethod
    @property
    def UTF7(cls) -> Encoding:
        """

        :return:
        """
    @classmethod
    @property
    def UTF8(cls) -> Encoding:
        """

        :return:
        """
    @classmethod
    @property
    def Unicode(cls) -> Encoding:
        """

        :return:
        """
    @property
    def WebName(self) -> str:
        """

        :return:
        """
    @property
    def WindowsCodePage(self) -> int:
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
    @overload
    def GetByteCount(self, chars: Array[Char]) -> int:
        """

        :param chars:
        :return:
        """
    @overload
    def GetByteCount(self, s: str) -> int:
        """

        :param s:
        :return:
        """
    @overload
    def GetByteCount(self, chars: Char, count: int) -> int:
        """

        :param chars:
        :param count:
        :return:
        """
    @overload
    def GetByteCount(self, chars: Array[Char], index: int, count: int) -> int:
        """

        :param chars:
        :param index:
        :param count:
        :return:
        """
    @overload
    def GetBytes(self, chars: Array[Char]) -> Array[int]:
        """

        :param chars:
        :return:
        """
    @overload
    def GetBytes(self, s: str) -> Array[int]:
        """

        :param s:
        :return:
        """
    @overload
    def GetBytes(self, chars: Array[Char], index: int, count: int) -> Array[int]:
        """

        :param chars:
        :param index:
        :param count:
        :return:
        """
    @overload
    def GetBytes(self, chars: Char, charCount: int, bytes: int, byteCount: int) -> int:
        """

        :param chars:
        :param charCount:
        :param bytes:
        :param byteCount:
        :return:
        """
    @overload
    def GetBytes(
        self, chars: Array[Char], charIndex: int, charCount: int, bytes: Array[int], byteIndex: int
    ) -> int:
        """

        :param chars:
        :param charIndex:
        :param charCount:
        :param bytes:
        :param byteIndex:
        :return:
        """
    @overload
    def GetBytes(
        self, s: str, charIndex: int, charCount: int, bytes: Array[int], byteIndex: int
    ) -> int:
        """

        :param s:
        :param charIndex:
        :param charCount:
        :param bytes:
        :param byteIndex:
        :return:
        """
    @overload
    def GetCharCount(self, bytes: Array[int]) -> int:
        """

        :param bytes:
        :return:
        """
    @overload
    def GetCharCount(self, bytes: int, count: int) -> int:
        """

        :param bytes:
        :param count:
        :return:
        """
    @overload
    def GetCharCount(self, bytes: Array[int], index: int, count: int) -> int:
        """

        :param bytes:
        :param index:
        :param count:
        :return:
        """
    @overload
    def GetChars(self, bytes: Array[int]) -> Array[Char]:
        """

        :param bytes:
        :return:
        """
    @overload
    def GetChars(self, bytes: Array[int], index: int, count: int) -> Array[Char]:
        """

        :param bytes:
        :param index:
        :param count:
        :return:
        """
    @overload
    def GetChars(self, bytes: int, byteCount: int, chars: Char, charCount: int) -> int:
        """

        :param bytes:
        :param byteCount:
        :param chars:
        :param charCount:
        :return:
        """
    @overload
    def GetChars(
        self, bytes: Array[int], byteIndex: int, byteCount: int, chars: Array[Char], charIndex: int
    ) -> int:
        """

        :param bytes:
        :param byteIndex:
        :param byteCount:
        :param chars:
        :param charIndex:
        :return:
        """
    def GetDecoder(self) -> Decoder:
        """

        :return:
        """
    def GetEncoder(self) -> Encoder:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetMaxByteCount(self, charCount: int) -> int:
        """

        :param charCount:
        :return:
        """
    def GetMaxCharCount(self, byteCount: int) -> int:
        """

        :param byteCount:
        :return:
        """
    def GetPreamble(self) -> Array[int]:
        """

        :return:
        """
    @overload
    def GetString(self, bytes: Array[int]) -> str:
        """

        :param bytes:
        :return:
        """
    @overload
    def GetString(self, bytes: int, byteCount: int) -> str:
        """

        :param bytes:
        :param byteCount:
        :return:
        """
    @overload
    def GetString(self, bytes: Array[int], index: int, count: int) -> str:
        """

        :param bytes:
        :param index:
        :param count:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def IsAlwaysNormalized(self) -> bool:
        """

        :return:
        """
    @overload
    def IsAlwaysNormalized(self, form: NormalizationForm) -> bool:
        """

        :param form:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
