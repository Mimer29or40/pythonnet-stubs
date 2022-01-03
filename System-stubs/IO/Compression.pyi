__all__ = [
    'BrotliStream',
    'DeflateStream',
    'GZipStream',
    'ZipArchive',
    'ZipArchiveEntry',
    'ZipFile',
    'ZipFileExtensions',
    'ZLibStream',
    'BrotliDecoder',
    'BrotliEncoder',
    'CompressionLevel',
    'CompressionMode',
    'ZipArchiveMode',
]


# TODO

# ---------- CLASSES ---------- #

class BrotliStream:
    """Provides methods and properties used to compress and decompress streams by using the Brotli data format specification."""


class DeflateStream:
    """Provides methods and properties for compressing and decompressing streams by using the Deflate algorithm."""


class GZipStream:
    """Provides methods and properties used to compress and decompress streams by using the GZip data format specification."""


class ZipArchive:
    """Represents a package of compressed files in the zip archive format."""


class ZipArchiveEntry:
    """Represents a compressed file within a zip archive."""


class ZipFile:
    """Provides static methods for creating, extracting, and opening zip archives."""


class ZipFileExtensions:
    """Provides extension methods for the ZipArchive and ZipArchiveEntry classes."""


class ZLibStream:
    """Provides methods and properties used to compress and decompress streams by using the zlib data format specification."""


# ---------- STRUCTS ---------- #

class BrotliDecoder:
    """Provides non-allocating, performant Brotli decompression methods. The methods decompress in a single pass without using a BrotliStream instance."""


class BrotliEncoder:
    """Provides methods and static methods to encode and decode data in a streamless, non-allocating, and performant manner using the Brotli data format specification."""


# ---------- ENUMS ---------- #

class CompressionLevel:
    """Specifies values that indicate whether a compression operation emphasizes speed or compression size."""


class CompressionMode:
    """Specifies whether to compress or decompress the underlying stream."""


class ZipArchiveMode:
    """Specifies values for interacting with zip archive entries."""
