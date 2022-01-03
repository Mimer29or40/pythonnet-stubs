__all__ = [
    'ASCIIEncoding',
    'CodePagesEncodingProvider',
    'Decoder',
    'DecoderExceptionFallback',
    'DecoderExceptionFallbackBuffer',
    'DecoderFallback',
    'DecoderFallbackBuffer',
    'DecoderFallbackException',
    'DecoderReplacementFallback',
    'DecoderReplacementFallbackBuffer',
    'Encoder',
    'EncoderExceptionFallback',
    'EncoderExceptionFallbackBuffer',
    'EncoderFallback',
    'EncoderFallbackBuffer',
    'EncoderFallbackException',
    'EncoderReplacementFallback',
    'EncoderReplacementFallbackBuffer',
    'Encoding',
    'EncodingExtensions',
    'EncodingInfo',
    'EncodingProvider',
    'StringBuilder',
    'UnicodeEncoding',
    'UTF32Encoding',
    'UTF7Encoding',
    'UTF8Encoding',
    'Rune',
    'SpanLineEnumerator',
    'SpanRuneEnumerator',
    'StringRuneEnumerator',
    'NormalizationForm',
]


# TODO

# ---------- CLASSES ---------- #

class ASCIIEncoding:
    """Represents an ASCII character encoding of Unicode characters."""


class CodePagesEncodingProvider:
    """Provides access to an encoding provider for code pages that otherwise are available only in the desktop .NET Framework."""


class Decoder:
    """Converts a sequence of encoded bytes into a set of characters."""


class DecoderExceptionFallback:
    """Provides a failure-handling mechanism, called a fallback, for an encoded input byte sequence that cannot be converted to an input character. The fallback throws an exception instead of decoding the input byte sequence. This class cannot be inherited."""


class DecoderExceptionFallbackBuffer:
    """Throws DecoderFallbackException when an encoded input byte sequence cannot be converted to a decoded output character. This class cannot be inherited."""


class DecoderFallback:
    """Provides a failure-handling mechanism, called a fallback, for an encoded input byte sequence that cannot be converted to an output character."""


class DecoderFallbackBuffer:
    """Provides a buffer that allows a fallback handler to return an alternate string to a decoder when it cannot decode an input byte sequence."""


class DecoderFallbackException:
    """The exception that is thrown when a decoder fallback operation fails. This class cannot be inherited."""


class DecoderReplacementFallback:
    """Provides a failure-handling mechanism, called a fallback, for an encoded input byte sequence that cannot be converted to an output character. The fallback emits a user-specified replacement string instead of a decoded input byte sequence. This class cannot be inherited."""


class DecoderReplacementFallbackBuffer:
    """Represents a substitute output string that is emitted when the original input byte sequence cannot be decoded. This class cannot be inherited."""


class Encoder:
    """Converts a set of characters into a sequence of bytes."""


class EncoderExceptionFallback:
    """Provides a failure-handling mechanism, called a fallback, for an input character that cannot be converted to an output byte sequence. The fallback throws an exception if an input character cannot be converted to an output byte sequence. This class cannot be inherited."""


class EncoderExceptionFallbackBuffer:
    """Throws EncoderFallbackException when an input character cannot be converted to an encoded output byte sequence. This class cannot be inherited."""


class EncoderFallback:
    """Provides a failure-handling mechanism, called a fallback, for an input character that cannot be converted to an encoded output byte sequence."""


class EncoderFallbackBuffer:
    """Provides a buffer that allows a fallback handler to return an alternate string to an encoder when it cannot encode an input character."""


class EncoderFallbackException:
    """The exception that is thrown when an encoder fallback operation fails. This class cannot be inherited."""


class EncoderReplacementFallback:
    """Provides a failure handling mechanism, called a fallback, for an input character that cannot be converted to an output byte sequence. The fallback uses a user-specified replacement string instead of the original input character. This class cannot be inherited."""


class EncoderReplacementFallbackBuffer:
    """Represents a substitute input string that is used when the original input character cannot be encoded. This class cannot be inherited."""


class Encoding:
    """Represents a character encoding."""


class EncodingExtensions:
    """Provides extension methods for the encoding types, such as Encoding, Encoder, and Decoder."""


class EncodingInfo:
    """Provides basic information about an encoding."""


class EncodingProvider:
    """Provides the base class for an encoding provider, which supplies encodings that are unavailable on a particular platform."""


class StringBuilder:
    """Represents a mutable string of characters. This class cannot be inherited."""
    
    # ---------- STRUCTS ---------- #
    
    class AppendInterpolatedStringHandler:
        """Provides a handler used by the language compiler to append interpolated strings into StringBuilder instances."""
    
    class ChunkEnumerator:
        """Supports simple iteration over the chunks of a StringBuilder instance."""


class UnicodeEncoding:
    """Represents a UTF-16 encoding of Unicode characters."""


class UTF32Encoding:
    """Represents a UTF-32 encoding of Unicode characters."""


class UTF7Encoding:
    """Represents a UTF-7 encoding of Unicode characters."""


class UTF8Encoding:
    """Represents a UTF-8 encoding of Unicode characters."""


# ---------- STRUCTS ---------- #

class Rune:
    """Represents a Unicode scalar value ([ U+0000..U+D7FF ], inclusive; or [ U+E000..U+10FFFF ], inclusive)."""


class SpanLineEnumerator:
    """Enumerates the lines of a ReadOnlySpan[T]."""


class SpanRuneEnumerator:
    """Provides an enumerator for the Rune values represented by a span containing UTF-16 text."""


class StringRuneEnumerator:
    """Provides an enumerator for the Rune values represented by a string."""


# ---------- ENUMS ---------- #

class NormalizationForm:
    """Defines the type of normalization to perform."""
