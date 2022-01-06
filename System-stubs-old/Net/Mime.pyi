__all__ = [
    'ContentDisposition',
    'ContentType',
    'DispositionTypeNames',
    'MediaTypeNames',
    'TransferEncoding',
]


# TODO

# ---------- CLASSES ---------- #

class ContentDisposition:
    """Represents a MIME protocol Content-Disposition header."""


class ContentType:
    """Represents a MIME protocol Content-Type header."""


class DispositionTypeNames:
    """Supplies the strings used to specify the disposition type for an email attachment."""


class MediaTypeNames:
    """Specifies the media type information for an email message attachment."""
    
    class Application:
        """Specifies the kind of application data in an email message attachment."""
    
    class Image:
        """Specifies the type of image data in an email message attachment."""
    
    class Text:
        """Specifies the type of text data in an email message attachment."""


# ---------- ENUMS ---------- #

class TransferEncoding:
    """Specifies the Content-Transfer-Encoding header information for an email message attachment."""
