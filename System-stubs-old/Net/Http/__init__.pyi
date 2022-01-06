__all__ = [
    'ByteArrayContent',
    'DelegatingHandler',
    'FormUrlEncodedContent',
    'HttpClient',
    'HttpClientHandler',
    'HttpContent',
    'HttpMessageHandler',
    'HttpMessageInvoker',
    'HttpMethod',
    'HttpRequestException',
    'HttpRequestMessage',
    'HttpRequestOptions',
    'HttpResponseMessage',
    'MessageProcessingHandler',
    'MultipartContent',
    'MultipartFormDataContent',
    'ReadOnlyMemoryContent',
    'SocketsHttpConnectionContext',
    'SocketsHttpHandler',
    'SocketsHttpPlaintextStreamFilterContext',
    'StreamContent',
    'StringContent',
    'HttpRequestOptionsKey',
    'ClientCertificateOption',
    'HttpCompletionOption',
    'HttpKeepAlivePingPolicy',
    'HttpVersionPolicy',
    'HeaderEncodingSelector',
]

from typing import TypeVar, Generic

TValue = TypeVar('TValue')
TContext = TypeVar('TContext')


# TODO

# ---------- CLASSES ---------- #

class ByteArrayContent:
    """Provides HTTP content based on a byte array."""


class DelegatingHandler:
    """A type for HTTP handlers that delegate the processing of HTTP response messages to another handler, called the inner handler."""


class FormUrlEncodedContent:
    """A container for name/value tuples encoded using application/x-www-form-urlencoded MIME type."""


class HttpClient:
    """Provides a class for sending HTTP requests and receiving HTTP responses from a resource identified by a URI."""


class HttpClientHandler:
    """The default message handler used by HttpClient in .NET Framework and .NET Core 2.0 and earlier."""


class HttpContent:
    """A base class representing an HTTP entity body and content headers."""


class HttpMessageHandler:
    """A base type for HTTP message handlers."""


class HttpMessageInvoker:
    """A specialty class that allows applications to call the SendAsync(HttpRequestMessage, CancellationToken) method on an HTTP handler chain."""


class HttpMethod:
    """A helper class for retrieving and comparing standard HTTP methods and for creating new HTTP methods."""


class HttpRequestException:
    """A base class for exceptions thrown by the HttpClient and HttpMessageHandler classes."""


class HttpRequestMessage:
    """Represents a HTTP request message."""


class HttpRequestOptions:
    """Represents a collection of options for an HTTP request."""


class HttpResponseMessage:
    """Represents a HTTP response message including the status code and data."""


class MessageProcessingHandler:
    """A base type for handlers which only do some small processing of request and/or response messages."""


class MultipartContent:
    """Provides a collection of HttpContent objects that get serialized using the multipart/* content type specification."""


class MultipartFormDataContent:
    """Provides a container for content encoded using multipart/form-data MIME type."""


class ReadOnlyMemoryContent:
    """Provides HTTP content based on a ReadOnlyMemory[T]."""


class SocketsHttpConnectionContext:
    """Represents the context passed to the ConnectCallback for a SocketsHttpHandler instance. ."""


class SocketsHttpHandler:
    """Provides the default message handler used by HttpClient in .NET Core 2.1 and later."""


class SocketsHttpPlaintextStreamFilterContext:
    """Represents the context passed to the PlaintextStreamFilter for a SocketsHttpHandler instance."""


class StreamContent:
    """Provides HTTP content based on a stream."""


class StringContent:
    """Provides HTTP content based on a string."""


# ---------- STRUCTS ---------- #

class HttpRequestOptionsKey(Generic[TValue]):
    """Represents a key in the options collection for an HTTP request."""


# ---------- ENUMS ---------- #

class ClientCertificateOption:
    """Specifies how client certificates are provided."""


class HttpCompletionOption:
    """Indicates if HttpClient operations should be considered completed either as soon as a response is available, or after reading the entire response message including the content."""


class HttpKeepAlivePingPolicy:
    """Specifies when the HTTP/2 ping frame is sent on an idle connection."""


class HttpVersionPolicy:
    """Specifies behaviors for selecting and negotiating the HTTP version for a request."""


# ---------- DELEGATES ---------- #

class HeaderEncodingSelector(Generic[TContext]):
    """Represents a method that specifies the encoding to use when interpreting header values."""
