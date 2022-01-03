__all__ = [
    'AuthenticationHeaderValue',
    'CacheControlHeaderValue',
    'ContentDispositionHeaderValue',
    'ContentRangeHeaderValue',
    'EntityTagHeaderValue',
    'HttpContentHeaders',
    'HttpHeaders',
    'HttpHeaderValueCollection',
    'HttpRequestHeaders',
    'HttpResponseHeaders',
    'MediaTypeHeaderValue',
    'MediaTypeWithQualityHeaderValue',
    'NameValueHeaderValue',
    'NameValueWithParametersHeaderValue',
    'ProductHeaderValue',
    'ProductInfoHeaderValue',
    'RangeConditionHeaderValue',
    'RangeHeaderValue',
    'RangeItemHeaderValue',
    'RetryConditionHeaderValue',
    'StringWithQualityHeaderValue',
    'TransferCodingHeaderValue',
    'TransferCodingWithQualityHeaderValue',
    'ViaHeaderValue',
    'WarningHeaderValue',
    'HeaderStringValues',
    'HttpHeadersNonValidated',
]

from typing import TypeVar, Generic

T = TypeVar('T')


# TODO

# ---------- CLASSES ---------- #

class AuthenticationHeaderValue:
    """Represents authentication information in Authorization, ProxyAuthorization, WWW-Authenticate, and Proxy-Authenticate header values."""


class CacheControlHeaderValue:
    """Represents the value of the Cache-Control header."""


class ContentDispositionHeaderValue:
    """Represents the value of the Content-Disposition header."""


class ContentRangeHeaderValue:
    """Represents the value of the Content-Range header."""


class EntityTagHeaderValue:
    """Represents an entity-tag header value."""


class HttpContentHeaders:
    """Represents the collection of Content Headers as defined in RFC 2616."""


class HttpHeaders:
    """A collection of headers and their values as defined in RFC 2616."""


class HttpHeaderValueCollection(Generic[T]):
    """Represents a collection of header values."""


class HttpRequestHeaders:
    """Represents the collection of Request Headers as defined in RFC 2616."""


class HttpResponseHeaders:
    """Represents the collection of Response Headers as defined in RFC 2616."""


class MediaTypeHeaderValue:
    """Represents a media type used in a Content-Type header as defined in the RFC 2616."""


class MediaTypeWithQualityHeaderValue:
    """Represents a media type with an additional quality factor used in a Content-Type header."""


class NameValueHeaderValue:
    """Represents a name/value pair used in various headers as defined in RFC 2616."""


class NameValueWithParametersHeaderValue:
    """Represents a name/value pair with parameters used in various headers as defined in RFC 2616."""


class ProductHeaderValue:
    """Represents a product token value in a User-Agent header."""


class ProductInfoHeaderValue:
    """Represents a value which can either be a product or a comment in a User-Agent header."""


class RangeConditionHeaderValue:
    """Represents an If-Range header value which can either be a date/time or an entity-tag value."""


class RangeHeaderValue:
    """Represents a Range header value."""


class RangeItemHeaderValue:
    """Represents a byte range in a Range header value."""


class RetryConditionHeaderValue:
    """Represents a Retry-After header value which can either be a date/time or a timespan value."""


class StringWithQualityHeaderValue:
    """Represents a string header value with an optional quality."""


class TransferCodingHeaderValue:
    """Represents an accept-encoding header value."""


class TransferCodingWithQualityHeaderValue:
    """Represents an Accept-Encoding header value with optional quality factor."""


class ViaHeaderValue:
    """Represents the value of a Via header."""


class WarningHeaderValue:
    """Represents a warning value used by the Warning header."""


# ---------- STRUCTS ---------- #

class HeaderStringValues:
    """Provides a collection of header string values."""
    
    class Enumerator:
        """Enumerates the elements of a HeaderStringValues."""


class HttpHeadersNonValidated:
    """Provides a view on top of a HttpHeaders collection that avoids forcing validation or parsing on its contents."""
    
    class Enumerator:
        """Enumerates the elements of a HttpHeadersNonValidated."""
