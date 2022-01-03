__all__ = [
    'AuthenticationManager',
    'Authorization',
    'Cookie',
    'CookieCollection',
    'CookieContainer',
    'CookieException',
    'CredentialCache',
    'Dns',
    'DnsEndPoint',
    'DownloadDataCompletedEventArgs',
    'DownloadProgressChangedEventArgs',
    'DownloadStringCompletedEventArgs',
    'EndPoint',
    'FileWebRequest',
    'FileWebResponse',
    'FtpWebRequest',
    'FtpWebResponse',
    'GlobalProxySelection',
    'HttpListenerBasicIdentity',
    'HttpListenerContext',
    'HttpListenerException',
    'HttpListenerPrefixCollection',
    'HttpListenerRequest',
    'HttpListenerResponse',
    'HttpListenerTimeoutManager',
    'HttpVersion',
    'HttpWebRequest',
    'HttpWebResponse',
    'IPAddress',
    'IPEndPoint',
    'IPHostEntry',
    'NetworkCredential',
    'OpenReadCompletedEventArgs',
    'OpenWriteCompletedEventArgs',
    'ProtocolViolationException',
    'ServicePoint',
    'ServicePointManager',
    'SocketAddress',
    'TransportContext',
    'UploadDataCompletedEventArgs',
    'UploadFileCompletedEventArgs',
    'UploadProgressChangedEventArgs',
    'UploadStringCompletedEventArgs',
    'UploadValuesCompletedEventArgs',
    'WebClient',
    'WebException',
    'WebHeaderCollection',
    'WebProxy',
    'WebRequest',
    'WebRequestMethods',
    'WebResponse',
    'WebUtility',
    'WriteStreamClosedEventArgs',
    'IAuthenticationModule',
    'ICredentialPolicy',
    'ICredentials',
    'ICredentialsByHost',
    'IWebProxy',
    'IWebProxyScript',
    'IWebRequestCreate',
    'AuthenticationSchemes',
    'DecompressionMethods',
    'FtpStatusCode',
    'HttpRequestHeader',
    'HttpResponseHeader',
    'HttpStatusCode',
    'SecurityProtocolType',
    'WebExceptionStatus',
    'AuthenticationSchemeSelector',
    'BindIPEndPoint',
    'DownloadDataCompletedEventHandler',
    'DownloadProgressChangedEventHandler',
    'DownloadStringCompletedEventHandler',
    'HttpContinueDelegate',
    'OpenReadCompletedEventHandler',
    'OpenWriteCompletedEventHandler',
    'UploadDataCompletedEventHandler',
    'UploadFileCompletedEventHandler',
    'UploadProgressChangedEventHandler',
    'UploadStringCompletedEventHandler',
    'UploadValuesCompletedEventHandler',
    'WriteStreamClosedEventHandler',
]


# TODO

# ---------- CLASSES ---------- #

class AuthenticationManager:
    """Manages the authentication modules called during the client authentication process."""


class Authorization:
    """Contains an authentication message for an Internet server."""


class Cookie:
    """Provides a set of properties and methods that are used to manage cookies. This class cannot be inherited."""


class CookieCollection:
    """Provides a collection container for instances of the Cookie class."""


class CookieContainer:
    """Provides a container for a collection of CookieCollection objects."""


class CookieException:
    """The exception that is thrown when an error is made adding a Cookie to a CookieContainer."""


class CredentialCache:
    """Provides storage for multiple credentials."""


class Dns:
    """Provides simple domain name resolution functionality."""


class DnsEndPoint:
    """Represents a network endpoint as a host name or a string representation of an IP address and a port number."""


class DownloadDataCompletedEventArgs:
    """Provides data for the DownloadDataCompleted event."""


class DownloadProgressChangedEventArgs:
    """Provides data for the DownloadProgressChanged event of a WebClient."""


class DownloadStringCompletedEventArgs:
    """Provides data for the DownloadStringCompleted event."""


class EndPoint:
    """Identifies a network address. This is an abstract class."""


class FileWebRequest:
    """Provides a file system implementation of the WebRequest class."""


class FileWebResponse:
    """Provides a file system implementation of the WebResponse class."""


class FtpWebRequest:
    """Implements a File Transfer Protocol (FTP) client."""


class FtpWebResponse:
    """Encapsulates a File Transfer Protocol (FTP) server's response to a request."""


class GlobalProxySelection:
    """Contains a global default proxy instance for all HTTP requests."""


class HttpListener:
    """Provides a simple, programmatically controlled HTTP protocol listener. This class cannot be inherited."""
    
    # ---------- DELEGATES ---------- #
    
    class ExtendedProtectionSelector:
        """A delegate called to determine the ExtendedProtectionPolicy to use for each HttpListener request."""


class HttpListenerBasicIdentity:
    """Holds the user name and password from a basic authentication request."""


class HttpListenerContext:
    """Provides access to the request and response objects used by the HttpListener class. This class cannot be inherited."""


class HttpListenerException:
    """The exception that is thrown when an error occurs processing an HTTP request."""


class HttpListenerPrefixCollection:
    """Represents the collection used to store Uniform Resource Identifier (URI) prefixes for HttpListener objects."""


class HttpListenerRequest:
    """Describes an incoming HTTP request to an HttpListener object. This class cannot be inherited."""


class HttpListenerResponse:
    """Represents a response to a request being handled by an HttpListener object."""


class HttpListenerTimeoutManager:
    """The timeout manager to use for an HttpListener object."""


class HttpVersion:
    """Defines the HTTP version numbers that are supported by the HttpWebRequest and HttpWebResponse classes."""


class HttpWebRequest:
    """Provides an HTTP-specific implementation of the WebRequest class."""


class HttpWebResponse:
    """Provides an HTTP-specific implementation of the WebResponse class."""


class IPAddress:
    """Provides an Internet Protocol (IP) address."""


class IPEndPoint:
    """Represents a network endpoint as an IP address and a port number."""


class IPHostEntry:
    """Provides a container class for Internet host address information."""


class NetworkCredential:
    """Provides credentials for password-based authentication schemes such as basic, digest, NTLM, and Kerberos authentication."""


class OpenReadCompletedEventArgs:
    """Provides data for the OpenReadCompleted event."""


class OpenWriteCompletedEventArgs:
    """Provides data for the OpenWriteCompleted event."""


class ProtocolViolationException:
    """The exception that is thrown when an error is made while using a network protocol."""


class ServicePoint:
    """Provides connection management for HTTP connections."""


class ServicePointManager:
    """Manages the collection of ServicePoint objects."""


class SocketAddress:
    """Stores serialized information from EndPoint derived classes."""


class TransportContext:
    """The TransportContext class provides additional context about the underlying transport layer."""


class UploadDataCompletedEventArgs:
    """Provides data for the UploadDataCompleted event."""


class UploadFileCompletedEventArgs:
    """Provides data for the UploadFileCompleted event."""


class UploadProgressChangedEventArgs:
    """Provides data for the UploadProgressChanged event of a WebClient."""


class UploadStringCompletedEventArgs:
    """Provides data for the UploadStringCompleted event."""


class UploadValuesCompletedEventArgs:
    """Provides data for the UploadValuesCompleted event."""


class WebClient:
    """Provides common methods for sending data to and receiving data from a resource identified by a URI."""


class WebException:
    """The exception that is thrown when an error occurs while accessing the network through a pluggable protocol."""


class WebHeaderCollection:
    """Contains protocol headers associated with a request or response."""


class WebProxy:
    """Contains HTTP proxy settings for the WebRequest class."""


class WebRequest:
    """Makes a request to a Uniform Resource Identifier (URI). This is an abstract class."""


class WebRequestMethods:
    """Container class for WebRequestMethods.Ftp, WebRequestMethods.File, and WebRequestMethods.Http classes. This class cannot be inherited."""
    
    class File:
        """Represents the types of file protocol methods that can be used with a FILE request. This class cannot be inherited."""
    
    class Ftp:
        """Represents the types of FTP protocol methods that can be used with an FTP request. This class cannot be inherited."""
    
    class Http:
        """Represents the types of HTTP protocol methods that can be used with an HTTP request."""


class WebResponse:
    """Provides a response from a Uniform Resource Identifier (URI). This is an abstract class."""


class WebUtility:
    """Provides methods for encoding and decoding URLs when processing Web requests."""


class WriteStreamClosedEventArgs:
    """Provides data for the WriteStreamClosed event."""


# ---------- INTERFACES ---------- #

class IAuthenticationModule:
    """Provides the base authentication interface for Web client authentication modules."""


class ICredentialPolicy:
    """Defines the credential policy to be used for resource requests that are made using WebRequest and its derived classes."""


class ICredentials:
    """Provides the base authentication interface for retrieving credentials for Web client authentication."""


class ICredentialsByHost:
    """Provides the interface for retrieving credentials for a host, port, and authentication type."""


class IWebProxy:
    """Provides the base interface for implementation of proxy access for the WebRequest class."""


class IWebProxyScript:
    """Provides the base interface to load and execute scripts for automatic proxy detection."""


class IWebRequestCreate:
    """Provides the base interface for creating WebRequest instances."""


# ---------- ENUMS ---------- #

class AuthenticationSchemes:
    """Specifies protocols for authentication."""


class DecompressionMethods:
    """Represents the file compression and decompression encoding format to be used to compress the data received in response to an HttpWebRequest."""


class FtpStatusCode:
    """Specifies the status codes returned for a File Transfer Protocol (FTP) operation."""


class HttpRequestHeader:
    """The HTTP headers that may be specified in a client request."""


class HttpResponseHeader:
    """The HTTP headers that can be specified in a server response."""


class HttpStatusCode:
    """Contains the values of status codes defined for HTTP."""


class SecurityProtocolType:
    """Specifies the security protocols that are supported by the Schannel security package."""


class WebExceptionStatus:
    """Defines status codes for the WebException class."""


# ---------- DELEGATES ---------- #

class AuthenticationSchemeSelector:
    """Selects the authentication scheme for an HttpListener instance."""


class BindIPEndPoint:
    """Represents the method that specifies a local Internet Protocol address and port number for a ServicePoint."""


class DownloadDataCompletedEventHandler:
    """Represents the method that will handle the DownloadDataCompleted event of a WebClient."""


class DownloadProgressChangedEventHandler:
    """Represents the method that will handle the DownloadProgressChanged event of a WebClient."""


class DownloadStringCompletedEventHandler:
    """Represents the method that will handle the DownloadStringCompleted event of a WebClient."""


class HttpContinueDelegate:
    """Represents the method that notifies callers when a continue response is received by the client."""


class OpenReadCompletedEventHandler:
    """Represents the method that will handle the OpenReadCompleted event of a WebClient."""


class OpenWriteCompletedEventHandler:
    """Represents the method that will handle the OpenWriteCompleted event of a WebClient."""


class UploadDataCompletedEventHandler:
    """Represents the method that will handle the UploadDataCompleted event of a WebClient."""


class UploadFileCompletedEventHandler:
    """Represents the method that will handle the UploadFileCompleted event of a WebClient."""


class UploadProgressChangedEventHandler:
    """Represents the method that will handle the UploadProgressChanged event of a WebClient."""


class UploadStringCompletedEventHandler:
    """Represents the method that will handle the UploadStringCompleted event of a WebClient."""


class UploadValuesCompletedEventHandler:
    """Represents the method that will handle the UploadValuesCompleted event of a WebClient."""


class WriteStreamClosedEventHandler:
    """Represents the method that will handle the WriteStreamClosed event of a WebClient."""
