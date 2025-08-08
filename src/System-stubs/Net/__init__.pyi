"""Automatically generated stubs for C# namespace: System.Net."""

from abc import ABC
from collections.abc import Callable
from collections.abc import Iterator
from typing import ClassVar
from typing import Final
from typing import Self
from typing import overload

from Microsoft.Win32.SafeHandles import CriticalHandleMinusOneIsInvalid
from Microsoft.Win32.SafeHandles import CriticalHandleZeroOrMinusOneIsInvalid
from Microsoft.Win32.SafeHandles import SafeFileHandle
from Microsoft.Win32.SafeHandles import SafeHandleMinusOneIsInvalid
from Microsoft.Win32.SafeHandles import SafeHandleZeroOrMinusOneIsInvalid
from Microsoft.Win32.SafeHandles import SafeWaitHandle
from System import Array
from System import ArraySegment
from System import AsyncCallback
from System import Boolean
from System import Byte
from System import DateTime
from System import Enum
from System import EventArgs
from System import EventHandler
from System import Exception
from System import FormatException
from System import Guid
from System import IAsyncResult
from System import IDisposable
from System import Int32
from System import IntPtr
from System import InvalidOperationException
from System import MarshalByRefObject
from System import Object
from System import Predicate
from System import String
from System import SystemException
from System import TimeSpan
from System import Type
from System import UInt32
from System import Uri
from System import ValueType
from System import Version
from System.Collections import ArrayList
from System.Collections import ICollection
from System.Collections import IComparer
from System.Collections import IDictionary
from System.Collections import IEnumerable
from System.Collections import IEnumerator
from System.Collections import IEqualityComparer
from System.Collections.Generic import ICollection
from System.Collections.Generic import IEnumerable
from System.Collections.Generic import IEnumerator
from System.Collections.Generic import IList
from System.Collections.Specialized import NameValueCollection
from System.Collections.Specialized import StringDictionary
from System.ComponentModel import AsyncCompletedEventArgs
from System.ComponentModel import AsyncCompletedEventHandler
from System.ComponentModel import Component
from System.ComponentModel import IComponent
from System.ComponentModel import IContainer
from System.ComponentModel import ISite
from System.ComponentModel import ProgressChangedEventArgs
from System.ComponentModel import Win32Exception
from System.Configuration import ConfigurationValidatorBase
from System.Globalization import CultureInfo
from System.IO import BinaryWriter
from System.IO import FileAccess
from System.IO import FileMode
from System.IO import FileShare
from System.IO import FileStream
from System.IO import MemoryStream
from System.IO import SeekOrigin
from System.IO import Stream
from System.IO import TextWriter
from System.IO.Compression import CompressionMode
from System.IO.Compression import DeflateStream
from System.IO.Compression import GZipStream
from System.Net.Cache import RequestCachePolicy
from System.Net.Mime import IEncodableStream
from System.Net.Security import AuthenticationLevel
from System.Net.Security import EncryptionPolicy
from System.Net.Security import RemoteCertificateValidationCallback
from System.Net.Security import TlsAlertMessage
from System.Net.Security import TlsAlertType
from System.Net.Sockets import AddressFamily
from System.Net.Sockets import NetworkStream
from System.Net.WebSockets import HttpListenerWebSocketContext
from System.Reflection import Binder
from System.Reflection import BindingFlags
from System.Reflection import FieldInfo
from System.Reflection import IReflect
from System.Reflection import MemberInfo
from System.Reflection import MethodBase
from System.Reflection import MethodInfo
from System.Reflection import ParameterModifier
from System.Reflection import PropertyInfo
from System.Runtime.InteropServices import SafeHandle
from System.Runtime.InteropServices import _Attribute
from System.Runtime.InteropServices import _Exception
from System.Runtime.Remoting import ObjRef
from System.Runtime.Serialization import IDeserializationCallback
from System.Runtime.Serialization import ISerializable
from System.Runtime.Serialization import SerializationInfo
from System.Runtime.Serialization import StreamingContext
from System.Security import CodeAccessPermission
from System.Security import IPermission
from System.Security import ISecurityEncodable
from System.Security import IStackWalk
from System.Security import SecureString
from System.Security import SecurityElement
from System.Security.AccessControl import FileSecurity
from System.Security.Authentication import SslProtocols
from System.Security.Authentication.ExtendedProtection import ChannelBinding
from System.Security.Authentication.ExtendedProtection import ChannelBindingKind
from System.Security.Authentication.ExtendedProtection import ExtendedProtectionPolicy
from System.Security.Authentication.ExtendedProtection import ServiceNameCollection
from System.Security.Authentication.ExtendedProtection import TokenBinding
from System.Security.Claims import Claim
from System.Security.Claims import ClaimsIdentity
from System.Security.Cryptography.X509Certificates import X509Certificate
from System.Security.Cryptography.X509Certificates import X509Certificate2
from System.Security.Cryptography.X509Certificates import X509CertificateCollection
from System.Security.Permissions import CodeAccessSecurityAttribute
from System.Security.Permissions import IUnrestrictedPermission
from System.Security.Permissions import PermissionState
from System.Security.Permissions import SecurityAction
from System.Security.Principal import GenericIdentity
from System.Security.Principal import IIdentity
from System.Security.Principal import IPrincipal
from System.Security.Principal import TokenImpersonationLevel
from System.Text import Encoding
from System.Text.RegularExpressions import Regex
from System.Threading import CancellationToken
from System.Threading import ExecutionContext
from System.Threading import WaitHandle
from System.Threading.Tasks import Task

class EventType[T]:
    def __iadd__(self, other: T) -> Self: ...
    def __isub__(self, other: T) -> Self: ...

class AddressInfo(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class AddressInfoHints(Enum):
    """"""

    AI_PASSIVE: AddressInfoHints = ...
    """"""
    AI_CANONNAME: AddressInfoHints = ...
    """"""
    AI_NUMERICHOST: AddressInfoHints = ...
    """"""
    AI_FQDN: AddressInfoHints = ...
    """"""

class Alg(Enum):
    """"""

    Any: Alg = ...
    """"""
    NameDES: Alg = ...
    """"""
    NameRC4: Alg = ...
    """"""
    NameRC2: Alg = ...
    """"""
    NameDH_Ephem: Alg = ...
    """"""
    Name3DES: Alg = ...
    """"""
    NameMD5: Alg = ...
    """"""
    NameSHA: Alg = ...
    """"""
    NameSHA256: Alg = ...
    """"""
    NameSHA384: Alg = ...
    """"""
    NameSHA512: Alg = ...
    """"""
    NameAES_128: Alg = ...
    """"""
    NameAES_192: Alg = ...
    """"""
    NameAES_256: Alg = ...
    """"""
    NameAES: Alg = ...
    """"""
    TypeRSA: Alg = ...
    """"""
    TypeBlock: Alg = ...
    """"""
    TypeStream: Alg = ...
    """"""
    TypeDH: Alg = ...
    """"""
    ClassSignture: Alg = ...
    """"""
    ClassEncrypt: Alg = ...
    """"""
    ClassHash: Alg = ...
    """"""
    ClassKeyXch: Alg = ...
    """"""

type AsyncProtocolCallback = Callable[[AsyncProtocolRequest], None]
""""""

class AsyncProtocolRequest(Object):
    """"""

    AsyncState: Final[object]
    """"""
    Buffer: Final[Array[int]]
    """"""
    Count: Final[int]
    """"""
    Offset: Final[int]
    """"""
    Result: Final[int]
    """"""
    UserAsyncResult: Final[LazyAsyncResult]
    """"""
    def __init__(self, userAsyncResult: LazyAsyncResult) -> None:
        """"""
    @property
    def MustCompleteSynchronously(self) -> bool:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def SetNextRequest(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncProtocolCallback
    ) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class AsyncRequestContext(RequestContextBase, IDisposable):
    """"""
    def Close(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class AuthIdentity(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class AuthenticationManager(Object):
    """"""
    @classmethod
    @property
    def CredentialPolicy(cls) -> ICredentialPolicy:
        """"""
    @classmethod
    @CredentialPolicy.setter
    def CredentialPolicy(cls, value: ICredentialPolicy) -> None: ...
    @classmethod
    @property
    def CustomTargetNameDictionary(cls) -> StringDictionary:
        """"""
    @classmethod
    @property
    def RegisteredModules(cls) -> IEnumerator:
        """"""
    @classmethod
    def Authenticate(
        cls, challenge: str, request: WebRequest, credentials: ICredentials
    ) -> Authorization:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def PreAuthenticate(cls, request: WebRequest, credentials: ICredentials) -> Authorization:
        """"""
    @classmethod
    def Register(cls, authenticationModule: IAuthenticationModule) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    @overload
    def Unregister(cls, authenticationModule: IAuthenticationModule) -> None:
        """"""
    @classmethod
    @overload
    def Unregister(cls, authenticationScheme: str) -> None:
        """"""

class AuthenticationManager2(AuthenticationManagerBase, IAuthenticationManager):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, maxPrefixLookupEntries: int) -> None:
        """"""
    @property
    def CredentialPolicy(self) -> ICredentialPolicy:
        """"""
    @CredentialPolicy.setter
    def CredentialPolicy(self, value: ICredentialPolicy) -> None: ...
    @property
    def CustomTargetNameDictionary(self) -> StringDictionary:
        """"""
    @property
    def OSSupportsExtendedProtection(self) -> bool:
        """"""
    @property
    def RegisteredModules(self) -> IEnumerator:
        """"""
    @property
    def SpnDictionary(self) -> SpnDictionary:
        """"""
    @property
    def SspSupportsExtendedProtection(self) -> bool:
        """"""
    def Authenticate(
        self, challenge: str, request: WebRequest, credentials: ICredentials
    ) -> Authorization:
        """"""
    def BindModule(self, uri: Uri, response: Authorization, module: IAuthenticationModule) -> None:
        """"""
    def EnsureConfigLoaded(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def PreAuthenticate(self, request: WebRequest, credentials: ICredentials) -> Authorization:
        """"""
    def Register(self, authenticationModule: IAuthenticationModule) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def Unregister(self, authenticationModule: IAuthenticationModule) -> None:
        """"""
    @overload
    def Unregister(self, authenticationScheme: str) -> None:
        """"""

class AuthenticationManagerBase(ABC, Object, IAuthenticationManager):
    """"""
    @property
    def CredentialPolicy(self) -> ICredentialPolicy:
        """"""
    @CredentialPolicy.setter
    def CredentialPolicy(self, value: ICredentialPolicy) -> None: ...
    @property
    def CustomTargetNameDictionary(self) -> StringDictionary:
        """"""
    @property
    def OSSupportsExtendedProtection(self) -> bool:
        """"""
    @property
    def RegisteredModules(self) -> IEnumerator:
        """"""
    @property
    def SpnDictionary(self) -> SpnDictionary:
        """"""
    @property
    def SspSupportsExtendedProtection(self) -> bool:
        """"""
    def Authenticate(
        self, challenge: str, request: WebRequest, credentials: ICredentials
    ) -> Authorization:
        """"""
    def BindModule(self, uri: Uri, response: Authorization, module: IAuthenticationModule) -> None:
        """"""
    def EnsureConfigLoaded(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def PreAuthenticate(self, request: WebRequest, credentials: ICredentials) -> Authorization:
        """"""
    def Register(self, authenticationModule: IAuthenticationModule) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def Unregister(self, authenticationModule: IAuthenticationModule) -> None:
        """"""
    @overload
    def Unregister(self, authenticationScheme: str) -> None:
        """"""

class AuthenticationManagerDefault(AuthenticationManagerBase, IAuthenticationManager):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def CredentialPolicy(self) -> ICredentialPolicy:
        """"""
    @CredentialPolicy.setter
    def CredentialPolicy(self, value: ICredentialPolicy) -> None: ...
    @property
    def CustomTargetNameDictionary(self) -> StringDictionary:
        """"""
    @property
    def OSSupportsExtendedProtection(self) -> bool:
        """"""
    @property
    def RegisteredModules(self) -> IEnumerator:
        """"""
    @property
    def SpnDictionary(self) -> SpnDictionary:
        """"""
    @property
    def SspSupportsExtendedProtection(self) -> bool:
        """"""
    def Authenticate(
        self, challenge: str, request: WebRequest, credentials: ICredentials
    ) -> Authorization:
        """"""
    def BindModule(self, uri: Uri, response: Authorization, module: IAuthenticationModule) -> None:
        """"""
    def EnsureConfigLoaded(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def PreAuthenticate(self, request: WebRequest, credentials: ICredentials) -> Authorization:
        """"""
    def Register(self, authenticationModule: IAuthenticationModule) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def Unregister(self, authenticationModule: IAuthenticationModule) -> None:
        """"""
    @overload
    def Unregister(self, authenticationScheme: str) -> None:
        """"""

type AuthenticationSchemeSelector = Callable[[HttpListenerRequest], AuthenticationSchemes]
""""""

class AuthenticationSchemes(Enum):
    """"""

    _None: AuthenticationSchemes = ...
    """"""
    Digest: AuthenticationSchemes = ...
    """"""
    Negotiate: AuthenticationSchemes = ...
    """"""
    Ntlm: AuthenticationSchemes = ...
    """"""
    IntegratedWindowsAuthentication: AuthenticationSchemes = ...
    """"""
    Basic: AuthenticationSchemes = ...
    """"""
    Anonymous: AuthenticationSchemes = ...
    """"""

class AuthenticationState(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class Authorization(Object):
    """"""
    @overload
    def __init__(self, token: str) -> None:
        """"""
    @overload
    def __init__(self, token: str, finished: bool) -> None:
        """"""
    @overload
    def __init__(self, token: str, finished: bool, connectionGroupId: str) -> None:
        """"""
    @property
    def Complete(self) -> bool:
        """"""
    @property
    def ConnectionGroupId(self) -> str:
        """"""
    @property
    def Message(self) -> str:
        """"""
    @property
    def MutuallyAuthenticated(self) -> bool:
        """"""
    @MutuallyAuthenticated.setter
    def MutuallyAuthenticated(self, value: bool) -> None: ...
    @property
    def ProtectionRealm(self) -> Array[str]:
        """"""
    @ProtectionRealm.setter
    def ProtectionRealm(self, value: Array[str]) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class AutoWebProxyScriptEngine(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class AutoWebProxyScriptWrapper(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class Base64Stream(DelegatedStream, IEncodableStream, IDisposable):
    """"""
    @property
    def CanRead(self) -> bool:
        """"""
    @property
    def CanSeek(self) -> bool:
        """"""
    @property
    def CanTimeout(self) -> bool:
        """"""
    @property
    def CanWrite(self) -> bool:
        """"""
    @property
    def Length(self) -> int:
        """"""
    @property
    def Position(self) -> int:
        """"""
    @Position.setter
    def Position(self, value: int) -> None: ...
    @property
    def ReadTimeout(self) -> int:
        """"""
    @ReadTimeout.setter
    def ReadTimeout(self, value: int) -> None: ...
    @property
    def WriteTimeout(self) -> int:
        """"""
    @WriteTimeout.setter
    def WriteTimeout(self, value: int) -> None: ...
    def BeginRead(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """"""
    def BeginWrite(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """"""
    def Close(self) -> None:
        """"""
    @overload
    def CopyTo(self, destination: Stream) -> None:
        """"""
    @overload
    def CopyTo(self, destination: Stream, bufferSize: int) -> None:
        """"""
    @overload
    def CopyToAsync(self, destination: Stream) -> Task:
        """"""
    @overload
    def CopyToAsync(self, destination: Stream, bufferSize: int) -> Task:
        """"""
    @overload
    def CopyToAsync(
        self, destination: Stream, bufferSize: int, cancellationToken: CancellationToken
    ) -> Task:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    def DecodeBytes(self, buffer: Array[int], offset: int, count: int) -> int:
        """"""
    def Dispose(self) -> None:
        """"""
    def EncodeBytes(self, buffer: Array[int], offset: int, count: int) -> int:
        """"""
    def EndRead(self, asyncResult: IAsyncResult) -> int:
        """"""
    def EndWrite(self, asyncResult: IAsyncResult) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Flush(self) -> None:
        """"""
    @overload
    def FlushAsync(self) -> Task:
        """"""
    @overload
    def FlushAsync(self, cancellationToken: CancellationToken) -> Task:
        """"""
    def GetEncodedString(self) -> str:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetLifetimeService(self) -> object:
        """"""
    def GetStream(self) -> Stream:
        """"""
    def GetType(self) -> Type:
        """"""
    def InitializeLifetimeService(self) -> object:
        """"""
    def Read(self, buffer: Array[int], offset: int, count: int) -> int:
        """"""
    @overload
    def ReadAsync(self, buffer: Array[int], offset: int, count: int) -> Task[int]:
        """"""
    @overload
    def ReadAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task[int]:
        """"""
    def ReadByte(self) -> int:
        """"""
    def Seek(self, offset: int, origin: SeekOrigin) -> int:
        """"""
    def SetLength(self, value: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def Write(self, buffer: Array[int], offset: int, count: int) -> None:
        """"""
    @overload
    def WriteAsync(self, buffer: Array[int], offset: int, count: int) -> Task:
        """"""
    @overload
    def WriteAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task:
        """"""
    def WriteByte(self, value: int) -> None:
        """"""

class BaseLoggingObject(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class BaseWebProxyFinder(ABC, Object, IWebProxyFinder, IDisposable):
    """"""
    def __init__(self, engine: AutoWebProxyScriptEngine) -> None:
        """"""
    @property
    def IsUnrecognizedScheme(self) -> bool:
        """"""
    @property
    def IsValid(self) -> bool:
        """"""
    def Abort(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetProxies(self, destination: Uri, proxyList: IList[str]) -> tuple[bool, IList[str]]:
        """"""
    def GetType(self) -> Type:
        """"""
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class BasicClient(Object, IAuthenticationModule):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def AuthenticationType(self) -> str:
        """"""
    @property
    def CanPreAuthenticate(self) -> bool:
        """"""
    def Authenticate(
        self, challenge: str, webRequest: WebRequest, credentials: ICredentials
    ) -> Authorization:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def PreAuthenticate(self, webRequest: WebRequest, credentials: ICredentials) -> Authorization:
        """"""
    def ToString(self) -> str:
        """"""

type BindIPEndPoint = Callable[[ServicePoint, IPEndPoint, int], IPEndPoint]
""""""

class Bindings(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class Blob(ValueType):
    """"""

    cbSize: Final[int]
    """"""
    pBlobData: Final[int]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class BoundaryType(Enum):
    """"""

    ContentLength: BoundaryType = ...
    """"""
    Chunked: BoundaryType = ...
    """"""
    Multipart: BoundaryType = ...
    """"""
    _None: BoundaryType = ...
    """"""
    Invalid: BoundaryType = ...
    """"""

class BufferAsyncResult(LazyAsyncResult, IAsyncResult):
    """"""

    Buffer: Final[Array[int]]
    """"""
    Buffers: Final[Array[BufferOffsetSize]]
    """"""
    Count: Final[int]
    """"""
    IsWrite: Final[bool]
    """"""
    Offset: Final[int]
    """"""
    @overload
    def __init__(
        self,
        asyncObject: object,
        buffers: Array[BufferOffsetSize],
        asyncState: object,
        asyncCallback: AsyncCallback,
    ) -> None:
        """"""
    @overload
    def __init__(
        self,
        asyncObject: object,
        buffer: Array[int],
        offset: int,
        count: int,
        asyncState: object,
        asyncCallback: AsyncCallback,
    ) -> None:
        """"""
    @overload
    def __init__(
        self,
        asyncObject: object,
        buffer: Array[int],
        offset: int,
        count: int,
        isWrite: bool,
        asyncState: object,
        asyncCallback: AsyncCallback,
    ) -> None:
        """"""
    @property
    def AsyncState(self) -> object:
        """"""
    @property
    def AsyncWaitHandle(self) -> WaitHandle:
        """"""
    @property
    def CompletedSynchronously(self) -> bool:
        """"""
    @property
    def IsCompleted(self) -> bool:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class BufferOffsetSize(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class BufferType(Enum):
    """"""

    Empty: BufferType = ...
    """"""
    Data: BufferType = ...
    """"""
    Token: BufferType = ...
    """"""
    Parameters: BufferType = ...
    """"""
    Missing: BufferType = ...
    """"""
    Extra: BufferType = ...
    """"""
    Trailer: BufferType = ...
    """"""
    Header: BufferType = ...
    """"""
    Padding: BufferType = ...
    """"""
    Stream: BufferType = ...
    """"""
    ChannelBindings: BufferType = ...
    """"""
    TargetHost: BufferType = ...
    """"""
    ReadOnlyWithChecksum: BufferType = ...
    """"""
    ReadOnlyFlag: BufferType = ...
    """"""

class BufferedReadStream(DelegatedStream, IDisposable):
    """"""
    @property
    def CanRead(self) -> bool:
        """"""
    @property
    def CanSeek(self) -> bool:
        """"""
    @property
    def CanTimeout(self) -> bool:
        """"""
    @property
    def CanWrite(self) -> bool:
        """"""
    @property
    def Length(self) -> int:
        """"""
    @property
    def Position(self) -> int:
        """"""
    @Position.setter
    def Position(self, value: int) -> None: ...
    @property
    def ReadTimeout(self) -> int:
        """"""
    @ReadTimeout.setter
    def ReadTimeout(self, value: int) -> None: ...
    @property
    def WriteTimeout(self) -> int:
        """"""
    @WriteTimeout.setter
    def WriteTimeout(self, value: int) -> None: ...
    def BeginRead(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """"""
    def BeginWrite(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """"""
    def Close(self) -> None:
        """"""
    @overload
    def CopyTo(self, destination: Stream) -> None:
        """"""
    @overload
    def CopyTo(self, destination: Stream, bufferSize: int) -> None:
        """"""
    @overload
    def CopyToAsync(self, destination: Stream) -> Task:
        """"""
    @overload
    def CopyToAsync(self, destination: Stream, bufferSize: int) -> Task:
        """"""
    @overload
    def CopyToAsync(
        self, destination: Stream, bufferSize: int, cancellationToken: CancellationToken
    ) -> Task:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    def Dispose(self) -> None:
        """"""
    def EndRead(self, asyncResult: IAsyncResult) -> int:
        """"""
    def EndWrite(self, asyncResult: IAsyncResult) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Flush(self) -> None:
        """"""
    @overload
    def FlushAsync(self) -> Task:
        """"""
    @overload
    def FlushAsync(self, cancellationToken: CancellationToken) -> Task:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetLifetimeService(self) -> object:
        """"""
    def GetType(self) -> Type:
        """"""
    def InitializeLifetimeService(self) -> object:
        """"""
    def Read(self, buffer: Array[int], offset: int, count: int) -> int:
        """"""
    @overload
    def ReadAsync(self, buffer: Array[int], offset: int, count: int) -> Task[int]:
        """"""
    @overload
    def ReadAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task[int]:
        """"""
    def ReadByte(self) -> int:
        """"""
    def Seek(self, offset: int, origin: SeekOrigin) -> int:
        """"""
    def SetLength(self, value: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def Write(self, buffer: Array[int], offset: int, count: int) -> None:
        """"""
    @overload
    def WriteAsync(self, buffer: Array[int], offset: int, count: int) -> Task:
        """"""
    @overload
    def WriteAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task:
        """"""
    def WriteByte(self, value: int) -> None:
        """"""

class CachedTransportContext(TransportContext):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetChannelBinding(self, kind: ChannelBindingKind) -> ChannelBinding:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetTlsTokenBindings(self) -> IEnumerable[TokenBinding]:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class CallbackClosure(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class CaseInsensitiveAscii(Object, IComparer, IEqualityComparer):
    """"""
    def __init__(self) -> None:
        """"""
    def Compare(self, firstObject: object, secondObject: object) -> int:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, firstObject: object, secondObject: object) -> bool:
        """"""
    @overload
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetHashCode(self, myObject: object) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class CertEnhKeyUse(ValueType):
    """"""

    cUsageIdentifier: Final[int]
    """"""
    rgpszUsageIdentifier: Final[None]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class CertPolicyValidationCallback(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class CertUsage(Enum):
    """"""

    MatchTypeAnd: CertUsage = ...
    """"""
    MatchTypeOr: CertUsage = ...
    """"""

class CertUsageMatch(ValueType):
    """"""

    Usage: Final[CertEnhKeyUse]
    """"""
    dwType: Final[CertUsage]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class CertificateEncoding(Enum):
    """"""

    Zero: CertificateEncoding = ...
    """"""
    X509AsnEncoding: CertificateEncoding = ...
    """"""
    X509NdrEncoding: CertificateEncoding = ...
    """"""
    Pkcs7AsnEncoding: CertificateEncoding = ...
    """"""
    AnyAsnEncoding: CertificateEncoding = ...
    """"""
    Pkcs7NdrEncoding: CertificateEncoding = ...
    """"""

class CertificateProblem(Enum):
    """"""

    OK: CertificateProblem = ...
    """"""
    CryptNOREVOCATIONCHECK: CertificateProblem = ...
    """"""
    CryptREVOCATIONOFFLINE: CertificateProblem = ...
    """"""
    TrustSYSTEMERROR: CertificateProblem = ...
    """"""
    TrustNOSIGNERCERT: CertificateProblem = ...
    """"""
    TrustCOUNTERSIGNER: CertificateProblem = ...
    """"""
    TrustCERTSIGNATURE: CertificateProblem = ...
    """"""
    TrustTIMESTAMP: CertificateProblem = ...
    """"""
    TrustBADDIGEST: CertificateProblem = ...
    """"""
    TrustBASICCONSTRAINTS: CertificateProblem = ...
    """"""
    TrustFINANCIALCRITERIA: CertificateProblem = ...
    """"""
    TrustNOSIGNATURE: CertificateProblem = ...
    """"""
    CertEXPIRED: CertificateProblem = ...
    """"""
    CertVALIDITYPERIODNESTING: CertificateProblem = ...
    """"""
    CertROLE: CertificateProblem = ...
    """"""
    CertPATHLENCONST: CertificateProblem = ...
    """"""
    CertCRITICAL: CertificateProblem = ...
    """"""
    CertPURPOSE: CertificateProblem = ...
    """"""
    CertISSUERCHAINING: CertificateProblem = ...
    """"""
    CertMALFORMED: CertificateProblem = ...
    """"""
    CertUNTRUSTEDROOT: CertificateProblem = ...
    """"""
    CertCHAINING: CertificateProblem = ...
    """"""
    CertREVOKED: CertificateProblem = ...
    """"""
    CertUNTRUSTEDTESTROOT: CertificateProblem = ...
    """"""
    CertREVOCATION_FAILURE: CertificateProblem = ...
    """"""
    CertCN_NO_MATCH: CertificateProblem = ...
    """"""
    CertWRONG_USAGE: CertificateProblem = ...
    """"""
    TrustEXPLICITDISTRUST: CertificateProblem = ...
    """"""
    CertUNTRUSTEDCA: CertificateProblem = ...
    """"""
    CertINVALIDPOLICY: CertificateProblem = ...
    """"""
    CertINVALIDNAME: CertificateProblem = ...
    """"""

class ChainParameters(ValueType):
    """"""

    BoolCheckRevocationFreshnessTime: Final[int]
    """"""
    RequestedIssuancePolicy: Final[CertUsageMatch]
    """"""
    RequestedUsage: Final[CertUsageMatch]
    """"""
    RevocationFreshnessTime: Final[int]
    """"""
    StructSize: ClassVar[int]
    """"""
    UrlRetrievalTimeout: Final[int]
    """"""
    cbSize: Final[int]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ChainPolicyParameter(ValueType):
    """"""

    StructSize: ClassVar[int]
    """"""
    cbSize: Final[int]
    """"""
    dwFlags: Final[int]
    """"""
    pvExtraPolicyPara: Final[SSL_EXTRA_CERT_CHAIN_POLICY_PARA]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ChainPolicyStatus(ValueType):
    """"""

    StructSize: ClassVar[int]
    """"""
    cbSize: Final[int]
    """"""
    dwError: Final[int]
    """"""
    lChainIndex: Final[int]
    """"""
    lElementIndex: Final[int]
    """"""
    pvExtraPolicyStatus: Final[None]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ChainPolicyType(Enum):
    """"""

    Base: ChainPolicyType = ...
    """"""
    Authenticode: ChainPolicyType = ...
    """"""
    Authenticode_TS: ChainPolicyType = ...
    """"""
    SSL: ChainPolicyType = ...
    """"""
    BasicConstraints: ChainPolicyType = ...
    """"""
    NtAuth: ChainPolicyType = ...
    """"""

class ChunkParser(Object):
    """"""
    def __init__(
        self,
        dataSource: Stream,
        internalBuffer: Array[int],
        initialBufferOffset: int,
        initialBufferCount: int,
        maxBufferLength: int,
    ) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Read(self, userBuffer: Array[int], userBufferOffset: int, userBufferCount: int) -> int:
        """"""
    def ReadAsync(
        self,
        caller: object,
        userBuffer: Array[int],
        userBufferOffset: int,
        userBufferCount: int,
        callback: AsyncCallback,
        state: object,
    ) -> IAsyncResult:
        """"""
    def ReadCallback(self, ar: IAsyncResult) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def TryGetLeftoverBytes(
        self, buffer: Byte, leftoverBufferOffset: Int32, leftoverBufferSize: Int32
    ) -> tuple[bool, Byte, Int32, Int32]:
        """"""

class ClosableStream(DelegatedStream, IDisposable):
    """"""
    @property
    def CanRead(self) -> bool:
        """"""
    @property
    def CanSeek(self) -> bool:
        """"""
    @property
    def CanTimeout(self) -> bool:
        """"""
    @property
    def CanWrite(self) -> bool:
        """"""
    @property
    def Length(self) -> int:
        """"""
    @property
    def Position(self) -> int:
        """"""
    @Position.setter
    def Position(self, value: int) -> None: ...
    @property
    def ReadTimeout(self) -> int:
        """"""
    @ReadTimeout.setter
    def ReadTimeout(self, value: int) -> None: ...
    @property
    def WriteTimeout(self) -> int:
        """"""
    @WriteTimeout.setter
    def WriteTimeout(self, value: int) -> None: ...
    def BeginRead(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """"""
    def BeginWrite(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """"""
    def Close(self) -> None:
        """"""
    @overload
    def CopyTo(self, destination: Stream) -> None:
        """"""
    @overload
    def CopyTo(self, destination: Stream, bufferSize: int) -> None:
        """"""
    @overload
    def CopyToAsync(self, destination: Stream) -> Task:
        """"""
    @overload
    def CopyToAsync(self, destination: Stream, bufferSize: int) -> Task:
        """"""
    @overload
    def CopyToAsync(
        self, destination: Stream, bufferSize: int, cancellationToken: CancellationToken
    ) -> Task:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    def Dispose(self) -> None:
        """"""
    def EndRead(self, asyncResult: IAsyncResult) -> int:
        """"""
    def EndWrite(self, asyncResult: IAsyncResult) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Flush(self) -> None:
        """"""
    @overload
    def FlushAsync(self) -> Task:
        """"""
    @overload
    def FlushAsync(self, cancellationToken: CancellationToken) -> Task:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetLifetimeService(self) -> object:
        """"""
    def GetType(self) -> Type:
        """"""
    def InitializeLifetimeService(self) -> object:
        """"""
    def Read(self, buffer: Array[int], offset: int, count: int) -> int:
        """"""
    @overload
    def ReadAsync(self, buffer: Array[int], offset: int, count: int) -> Task[int]:
        """"""
    @overload
    def ReadAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task[int]:
        """"""
    def ReadByte(self) -> int:
        """"""
    def Seek(self, offset: int, origin: SeekOrigin) -> int:
        """"""
    def SetLength(self, value: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def Write(self, buffer: Array[int], offset: int, count: int) -> None:
        """"""
    @overload
    def WriteAsync(self, buffer: Array[int], offset: int, count: int) -> Task:
        """"""
    @overload
    def WriteAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task:
        """"""
    def WriteByte(self, value: int) -> None:
        """"""

class CloseExState(Enum):
    """"""

    Normal: CloseExState = ...
    """"""
    Abort: CloseExState = ...
    """"""
    Silent: CloseExState = ...
    """"""

class ComNetOS(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class CommandStream(PooledStream, IDisposable):
    """"""
    @property
    def CanRead(self) -> bool:
        """"""
    @property
    def CanSeek(self) -> bool:
        """"""
    @property
    def CanTimeout(self) -> bool:
        """"""
    @property
    def CanWrite(self) -> bool:
        """"""
    @property
    def Length(self) -> int:
        """"""
    @property
    def Position(self) -> int:
        """"""
    @Position.setter
    def Position(self, value: int) -> None: ...
    @property
    def ReadTimeout(self) -> int:
        """"""
    @ReadTimeout.setter
    def ReadTimeout(self, value: int) -> None: ...
    @property
    def WriteTimeout(self) -> int:
        """"""
    @WriteTimeout.setter
    def WriteTimeout(self, value: int) -> None: ...
    def BeginRead(
        self, buffer: Array[int], offset: int, size: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """"""
    def BeginWrite(
        self, buffer: Array[int], offset: int, size: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """"""
    @overload
    def Close(self) -> None:
        """"""
    @overload
    def Close(self, timeout: int) -> None:
        """"""
    @overload
    def CopyTo(self, destination: Stream) -> None:
        """"""
    @overload
    def CopyTo(self, destination: Stream, bufferSize: int) -> None:
        """"""
    @overload
    def CopyToAsync(self, destination: Stream) -> Task:
        """"""
    @overload
    def CopyToAsync(self, destination: Stream, bufferSize: int) -> Task:
        """"""
    @overload
    def CopyToAsync(
        self, destination: Stream, bufferSize: int, cancellationToken: CancellationToken
    ) -> Task:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    def Dispose(self) -> None:
        """"""
    def EndRead(self, asyncResult: IAsyncResult) -> int:
        """"""
    def EndWrite(self, asyncResult: IAsyncResult) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Flush(self) -> None:
        """"""
    @overload
    def FlushAsync(self) -> Task:
        """"""
    @overload
    def FlushAsync(self, cancellationToken: CancellationToken) -> Task:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetLifetimeService(self) -> object:
        """"""
    def GetType(self) -> Type:
        """"""
    def InitializeLifetimeService(self) -> object:
        """"""
    def Read(self, buffer: Array[int], offset: int, size: int) -> int:
        """"""
    @overload
    def ReadAsync(self, buffer: Array[int], offset: int, count: int) -> Task[int]:
        """"""
    @overload
    def ReadAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task[int]:
        """"""
    def ReadByte(self) -> int:
        """"""
    def Seek(self, offset: int, origin: SeekOrigin) -> int:
        """"""
    def SetLength(self, value: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def Write(self, buffer: Array[int], offset: int, size: int) -> None:
        """"""
    @overload
    def WriteAsync(self, buffer: Array[int], offset: int, count: int) -> Task:
        """"""
    @overload
    def WriteAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task:
        """"""
    def WriteByte(self, value: int) -> None:
        """"""

class Comparer(Object, IComparer):
    """"""
    def __init__(self) -> None:
        """"""
    def Compare(self, x: object, y: object) -> int:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

type CompletionDelegate = Callable[[Array[int], Exception, object], None]
""""""

class ConnectStream(Stream, ICloseEx, IRequestLifetimeTracker, IDisposable):
    """"""
    @overload
    def __init__(self, connection: Connection, request: HttpWebRequest) -> None:
        """"""
    @overload
    def __init__(
        self,
        connection: Connection,
        buffer: Array[int],
        offset: int,
        bufferCount: int,
        readCount: int,
        chunked: bool,
        request: HttpWebRequest,
    ) -> None:
        """"""
    @property
    def CanRead(self) -> bool:
        """"""
    @property
    def CanSeek(self) -> bool:
        """"""
    @property
    def CanTimeout(self) -> bool:
        """"""
    @property
    def CanWrite(self) -> bool:
        """"""
    @property
    def Length(self) -> int:
        """"""
    @property
    def Position(self) -> int:
        """"""
    @Position.setter
    def Position(self, value: int) -> None: ...
    @property
    def ReadTimeout(self) -> int:
        """"""
    @ReadTimeout.setter
    def ReadTimeout(self, value: int) -> None: ...
    @property
    def WriteTimeout(self) -> int:
        """"""
    @WriteTimeout.setter
    def WriteTimeout(self, value: int) -> None: ...
    def BeginRead(
        self, buffer: Array[int], offset: int, size: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """"""
    def BeginWrite(
        self, buffer: Array[int], offset: int, size: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """"""
    def Close(self) -> None:
        """"""
    def CloseEx(self, closeState: CloseExState) -> None:
        """"""
    @overload
    def CopyTo(self, destination: Stream) -> None:
        """"""
    @overload
    def CopyTo(self, destination: Stream, bufferSize: int) -> None:
        """"""
    @overload
    def CopyToAsync(self, destination: Stream) -> Task:
        """"""
    @overload
    def CopyToAsync(self, destination: Stream, bufferSize: int) -> Task:
        """"""
    @overload
    def CopyToAsync(
        self, destination: Stream, bufferSize: int, cancellationToken: CancellationToken
    ) -> Task:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    def Dispose(self) -> None:
        """"""
    def EndRead(self, asyncResult: IAsyncResult) -> int:
        """"""
    def EndWrite(self, asyncResult: IAsyncResult) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Flush(self) -> None:
        """"""
    @overload
    def FlushAsync(self) -> Task:
        """"""
    @overload
    def FlushAsync(self, cancellationToken: CancellationToken) -> Task:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetLifetimeService(self) -> object:
        """"""
    def GetType(self) -> Type:
        """"""
    def InitializeLifetimeService(self) -> object:
        """"""
    def Read(self, buffer: Array[int], offset: int, size: int) -> tuple[int, Array[int]]:
        """"""
    @overload
    def ReadAsync(self, buffer: Array[int], offset: int, count: int) -> Task[int]:
        """"""
    @overload
    def ReadAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task[int]:
        """"""
    def ReadByte(self) -> int:
        """"""
    def Seek(self, offset: int, origin: SeekOrigin) -> int:
        """"""
    def SetLength(self, value: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def TrackRequestLifetime(self, requestStartTimestamp: int) -> None:
        """"""
    def Write(self, buffer: Array[int], offset: int, size: int) -> None:
        """"""
    @overload
    def WriteAsync(self, buffer: Array[int], offset: int, count: int) -> Task:
        """"""
    @overload
    def WriteAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task:
        """"""
    def WriteByte(self, value: int) -> None:
        """"""

class ConnectStreamContext(TransportContext):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetChannelBinding(self, kind: ChannelBindingKind) -> ChannelBinding:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetTlsTokenBindings(self) -> IEnumerable[TokenBinding]:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class Connection(PooledStream, IDisposable):
    """"""
    @property
    def CanRead(self) -> bool:
        """"""
    @property
    def CanSeek(self) -> bool:
        """"""
    @property
    def CanTimeout(self) -> bool:
        """"""
    @property
    def CanWrite(self) -> bool:
        """"""
    @property
    def Length(self) -> int:
        """"""
    @property
    def Position(self) -> int:
        """"""
    @Position.setter
    def Position(self, value: int) -> None: ...
    @property
    def ReadTimeout(self) -> int:
        """"""
    @ReadTimeout.setter
    def ReadTimeout(self, value: int) -> None: ...
    @property
    def WriteTimeout(self) -> int:
        """"""
    @WriteTimeout.setter
    def WriteTimeout(self, value: int) -> None: ...
    def BeginRead(
        self, buffer: Array[int], offset: int, size: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """"""
    def BeginWrite(
        self, buffer: Array[int], offset: int, size: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """"""
    @overload
    def Close(self) -> None:
        """"""
    @overload
    def Close(self, timeout: int) -> None:
        """"""
    @overload
    def CopyTo(self, destination: Stream) -> None:
        """"""
    @overload
    def CopyTo(self, destination: Stream, bufferSize: int) -> None:
        """"""
    @overload
    def CopyToAsync(self, destination: Stream) -> Task:
        """"""
    @overload
    def CopyToAsync(self, destination: Stream, bufferSize: int) -> Task:
        """"""
    @overload
    def CopyToAsync(
        self, destination: Stream, bufferSize: int, cancellationToken: CancellationToken
    ) -> Task:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    def Dispose(self) -> None:
        """"""
    def EndRead(self, asyncResult: IAsyncResult) -> int:
        """"""
    def EndWrite(self, asyncResult: IAsyncResult) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Flush(self) -> None:
        """"""
    @overload
    def FlushAsync(self) -> Task:
        """"""
    @overload
    def FlushAsync(self, cancellationToken: CancellationToken) -> Task:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetLifetimeService(self) -> object:
        """"""
    def GetType(self) -> Type:
        """"""
    def InitializeLifetimeService(self) -> object:
        """"""
    def Read(self, buffer: Array[int], offset: int, size: int) -> int:
        """"""
    @overload
    def ReadAsync(self, buffer: Array[int], offset: int, count: int) -> Task[int]:
        """"""
    @overload
    def ReadAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task[int]:
        """"""
    def ReadByte(self) -> int:
        """"""
    def Seek(self, offset: int, origin: SeekOrigin) -> int:
        """"""
    def SetLength(self, value: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def Write(self, buffer: Array[int], offset: int, size: int) -> None:
        """"""
    @overload
    def WriteAsync(self, buffer: Array[int], offset: int, count: int) -> Task:
        """"""
    @overload
    def WriteAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task:
        """"""
    def WriteByte(self, value: int) -> None:
        """"""

class ConnectionGroup(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ConnectionModes(Enum):
    """"""

    Single: ConnectionModes = ...
    """"""
    Persistent: ConnectionModes = ...
    """"""
    Pipeline: ConnectionModes = ...
    """"""
    Mux: ConnectionModes = ...
    """"""

class ConnectionPool(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ConnectionPoolManager(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ConnectionReturnResult(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ContentTypeValues(Enum):
    """"""

    ChangeCipherSpec: ContentTypeValues = ...
    """"""
    Alert: ContentTypeValues = ...
    """"""
    HandShake: ContentTypeValues = ...
    """"""
    AppData: ContentTypeValues = ...
    """"""
    Unrecognized: ContentTypeValues = ...
    """"""

class ContextAttribute(Enum):
    """"""

    Sizes: ContextAttribute = ...
    """"""
    Names: ContextAttribute = ...
    """"""
    Lifespan: ContextAttribute = ...
    """"""
    DceInfo: ContextAttribute = ...
    """"""
    StreamSizes: ContextAttribute = ...
    """"""
    Authority: ContextAttribute = ...
    """"""
    PackageInfo: ContextAttribute = ...
    """"""
    NegotiationInfo: ContextAttribute = ...
    """"""
    UniqueBindings: ContextAttribute = ...
    """"""
    EndpointBindings: ContextAttribute = ...
    """"""
    ClientSpecifiedSpn: ContextAttribute = ...
    """"""
    RemoteCertificate: ContextAttribute = ...
    """"""
    LocalCertificate: ContextAttribute = ...
    """"""
    RootStore: ContextAttribute = ...
    """"""
    IssuerListInfoEx: ContextAttribute = ...
    """"""
    ConnectionInfo: ContextAttribute = ...
    """"""
    UiInfo: ContextAttribute = ...
    """"""

class ContextAwareResult(LazyAsyncResult, IAsyncResult):
    """"""
    @property
    def AsyncState(self) -> object:
        """"""
    @property
    def AsyncWaitHandle(self) -> WaitHandle:
        """"""
    @property
    def CompletedSynchronously(self) -> bool:
        """"""
    @property
    def IsCompleted(self) -> bool:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ContextFlags(Enum):
    """"""

    Zero: ContextFlags = ...
    """"""
    Delegate: ContextFlags = ...
    """"""
    MutualAuth: ContextFlags = ...
    """"""
    ReplayDetect: ContextFlags = ...
    """"""
    SequenceDetect: ContextFlags = ...
    """"""
    Confidentiality: ContextFlags = ...
    """"""
    UseSessionKey: ContextFlags = ...
    """"""
    InitUseSuppliedCreds: ContextFlags = ...
    """"""
    AllocateMemory: ContextFlags = ...
    """"""
    Connection: ContextFlags = ...
    """"""
    InitExtendedError: ContextFlags = ...
    """"""
    AcceptExtendedError: ContextFlags = ...
    """"""
    InitStream: ContextFlags = ...
    """"""
    InitIntegrity: ContextFlags = ...
    """"""
    AcceptStream: ContextFlags = ...
    """"""
    InitIdentify: ContextFlags = ...
    """"""
    AcceptIntegrity: ContextFlags = ...
    """"""
    AcceptIdentify: ContextFlags = ...
    """"""
    InitManualCredValidation: ContextFlags = ...
    """"""
    ProxyBindings: ContextFlags = ...
    """"""
    AllowMissingBindings: ContextFlags = ...
    """"""
    UnverifiedTargetName: ContextFlags = ...
    """"""

class Cookie(Object):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, name: str, value: str) -> None:
        """"""
    @overload
    def __init__(self, name: str, value: str, path: str) -> None:
        """"""
    @overload
    def __init__(self, name: str, value: str, path: str, domain: str) -> None:
        """"""
    @property
    def Comment(self) -> str:
        """"""
    @Comment.setter
    def Comment(self, value: str) -> None: ...
    @property
    def CommentUri(self) -> Uri:
        """"""
    @CommentUri.setter
    def CommentUri(self, value: Uri) -> None: ...
    @property
    def Discard(self) -> bool:
        """"""
    @Discard.setter
    def Discard(self, value: bool) -> None: ...
    @property
    def Domain(self) -> str:
        """"""
    @Domain.setter
    def Domain(self, value: str) -> None: ...
    @property
    def Expired(self) -> bool:
        """"""
    @Expired.setter
    def Expired(self, value: bool) -> None: ...
    @property
    def Expires(self) -> DateTime:
        """"""
    @Expires.setter
    def Expires(self, value: DateTime) -> None: ...
    @property
    def HttpOnly(self) -> bool:
        """"""
    @HttpOnly.setter
    def HttpOnly(self, value: bool) -> None: ...
    @property
    def Name(self) -> str:
        """"""
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def Path(self) -> str:
        """"""
    @Path.setter
    def Path(self, value: str) -> None: ...
    @property
    def Port(self) -> str:
        """"""
    @Port.setter
    def Port(self, value: str) -> None: ...
    @property
    def Secure(self) -> bool:
        """"""
    @Secure.setter
    def Secure(self, value: bool) -> None: ...
    @property
    def TimeStamp(self) -> DateTime:
        """"""
    @property
    def Value(self) -> str:
        """"""
    @Value.setter
    def Value(self, value: str) -> None: ...
    @property
    def Version(self) -> int:
        """"""
    @Version.setter
    def Version(self, value: int) -> None: ...
    def Equals(self, comparand: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class CookieCollection(Object, ICollection, IEnumerable):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def Item(self) -> Cookie:
        """"""
    @property
    def SyncRoot(self) -> object:
        """"""
    @overload
    def Add(self, cookie: Cookie) -> None:
        """"""
    @overload
    def Add(self, cookies: CookieCollection) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array[Cookie], index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    def __len__(self) -> int:
        """"""
    @overload
    def __getitem__(self, index: int) -> Cookie:
        """"""
    @overload
    def __getitem__(self, name: str) -> Cookie:
        """"""

class CookieContainer(Object):
    """"""

    DefaultCookieLengthLimit: ClassVar[int]
    """"""
    DefaultCookieLimit: ClassVar[int]
    """"""
    DefaultPerDomainCookieLimit: ClassVar[int]
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, capacity: int) -> None:
        """"""
    @overload
    def __init__(self, capacity: int, perDomainCapacity: int, maxCookieSize: int) -> None:
        """"""
    @property
    def Capacity(self) -> int:
        """"""
    @Capacity.setter
    def Capacity(self, value: int) -> None: ...
    @property
    def Count(self) -> int:
        """"""
    @property
    def MaxCookieSize(self) -> int:
        """"""
    @MaxCookieSize.setter
    def MaxCookieSize(self, value: int) -> None: ...
    @property
    def PerDomainCapacity(self) -> int:
        """"""
    @PerDomainCapacity.setter
    def PerDomainCapacity(self, value: int) -> None: ...
    @overload
    def Add(self, cookie: Cookie) -> None:
        """"""
    @overload
    def Add(self, cookies: CookieCollection) -> None:
        """"""
    @overload
    def Add(self, uri: Uri, cookie: Cookie) -> None:
        """"""
    @overload
    def Add(self, uri: Uri, cookies: CookieCollection) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetCookieHeader(self, uri: Uri) -> str:
        """"""
    def GetCookies(self, uri: Uri) -> CookieCollection:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def SetCookies(self, uri: Uri, cookieHeader: str) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def __len__(self) -> int:
        """"""

class CookieException(FormatException, _Exception, ISerializable):
    """"""
    def __init__(self) -> None:
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
    def InnerException(self) -> Exception:
        """"""
    @property
    def Message(self) -> str:
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
    def GetObjectData(
        self, serializationInfo: SerializationInfo, streamingContext: StreamingContext
    ) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class CookieModule(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class CookieParser(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class CookieToken(Enum):
    """"""

    Nothing: CookieToken = ...
    """"""
    NameValuePair: CookieToken = ...
    """"""
    Attribute: CookieToken = ...
    """"""
    EndToken: CookieToken = ...
    """"""
    EndCookie: CookieToken = ...
    """"""
    End: CookieToken = ...
    """"""
    Equals: CookieToken = ...
    """"""
    Comment: CookieToken = ...
    """"""
    CommentUrl: CookieToken = ...
    """"""
    CookieName: CookieToken = ...
    """"""
    Discard: CookieToken = ...
    """"""
    Domain: CookieToken = ...
    """"""
    Expires: CookieToken = ...
    """"""
    MaxAge: CookieToken = ...
    """"""
    Path: CookieToken = ...
    """"""
    Port: CookieToken = ...
    """"""
    Secure: CookieToken = ...
    """"""
    HttpOnly: CookieToken = ...
    """"""
    Unknown: CookieToken = ...
    """"""
    Version: CookieToken = ...
    """"""

class CookieTokenizer(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class CookieVariant(Enum):
    """"""

    Unknown: CookieVariant = ...
    """"""
    Plain: CookieVariant = ...
    """"""
    Rfc2109: CookieVariant = ...
    """"""
    Default: CookieVariant = ...
    """"""
    Rfc2965: CookieVariant = ...
    """"""

class CoreResponseData(Object):
    """"""

    m_ConnectStream: Final[Stream]
    """"""
    m_ContentLength: Final[int]
    """"""
    m_IsVersionHttp11: Final[bool]
    """"""
    m_ResponseHeaders: Final[WebHeaderCollection]
    """"""
    m_StatusCode: Final[HttpStatusCode]
    """"""
    m_StatusDescription: Final[str]
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

type CreateConnectionDelegate = Callable[[ConnectionPool], PooledStream]
""""""

class CredentialCache(Object, IEnumerable, ICredentials, ICredentialsByHost):
    """"""
    def __init__(self) -> None:
        """"""
    @classmethod
    @property
    def DefaultCredentials(cls) -> ICredentials:
        """"""
    @classmethod
    @property
    def DefaultNetworkCredentials(cls) -> NetworkCredential:
        """"""
    @overload
    def Add(
        self, host: str, port: int, authenticationType: str, credential: NetworkCredential
    ) -> None:
        """"""
    @overload
    def Add(self, uriPrefix: Uri, authType: str, cred: NetworkCredential) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetCredential(self, host: str, port: int, authenticationType: str) -> NetworkCredential:
        """"""
    @overload
    def GetCredential(self, uriPrefix: Uri, authType: str) -> NetworkCredential:
        """"""
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def Remove(self, host: str, port: int, authenticationType: str) -> None:
        """"""
    @overload
    def Remove(self, uriPrefix: Uri, authType: str) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    @overload
    def __delitem__(self, host: str, port: int, authenticationType: str) -> None:
        """"""
    @overload
    def __delitem__(self, uriPrefix: Uri, authType: str) -> None:
        """"""

class CredentialHostKey(Object):
    """"""
    def Equals(self, comparand: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class CredentialKey(Object):
    """"""
    def Equals(self, comparand: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class CredentialUse(Enum):
    """"""

    Inbound: CredentialUse = ...
    """"""
    Outbound: CredentialUse = ...
    """"""
    Both: CredentialUse = ...
    """"""

class DataParseStatus(Enum):
    """"""

    NeedMoreData: DataParseStatus = ...
    """"""
    ContinueParsing: DataParseStatus = ...
    """"""
    Done: DataParseStatus = ...
    """"""
    Invalid: DataParseStatus = ...
    """"""
    DataTooBig: DataParseStatus = ...
    """"""

class DecompressionMethods(Enum):
    """"""

    _None: DecompressionMethods = ...
    """"""
    GZip: DecompressionMethods = ...
    """"""
    Deflate: DecompressionMethods = ...
    """"""

class DefaultCertPolicy(Object, ICertificatePolicy):
    """"""
    def __init__(self) -> None:
        """"""
    def CheckValidationResult(
        self, sp: ServicePoint, cert: X509Certificate, request: WebRequest, problem: int
    ) -> bool:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class DefaultPorts(Enum):
    """"""

    DEFAULT_FTP_PORT: DefaultPorts = ...
    """"""
    DEFAULT_TELNET_PORT: DefaultPorts = ...
    """"""
    DEFAULT_SMTP_PORT: DefaultPorts = ...
    """"""
    DEFAULT_GOPHER_PORT: DefaultPorts = ...
    """"""
    DEFAULT_HTTP_PORT: DefaultPorts = ...
    """"""
    DEFAULT_NNTP_PORT: DefaultPorts = ...
    """"""
    DEFAULT_HTTPS_PORT: DefaultPorts = ...
    """"""

class DeflateWrapperStream(DeflateStream, ICloseEx, IRequestLifetimeTracker, IDisposable):
    """"""
    def __init__(self, stream: Stream, mode: CompressionMode) -> None:
        """"""
    @property
    def BaseStream(self) -> Stream:
        """"""
    @property
    def CanRead(self) -> bool:
        """"""
    @property
    def CanSeek(self) -> bool:
        """"""
    @property
    def CanTimeout(self) -> bool:
        """"""
    @property
    def CanWrite(self) -> bool:
        """"""
    @property
    def Length(self) -> int:
        """"""
    @property
    def Position(self) -> int:
        """"""
    @Position.setter
    def Position(self, value: int) -> None: ...
    @property
    def ReadTimeout(self) -> int:
        """"""
    @ReadTimeout.setter
    def ReadTimeout(self, value: int) -> None: ...
    @property
    def WriteTimeout(self) -> int:
        """"""
    @WriteTimeout.setter
    def WriteTimeout(self, value: int) -> None: ...
    def BeginRead(
        self, buffer: Array[int], offset: int, size: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """"""
    def BeginWrite(
        self,
        array: Array[int],
        offset: int,
        count: int,
        asyncCallback: AsyncCallback,
        asyncState: object,
    ) -> IAsyncResult:
        """"""
    def Close(self) -> None:
        """"""
    def CloseEx(self, closeState: CloseExState) -> None:
        """"""
    @overload
    def CopyTo(self, destination: Stream) -> None:
        """"""
    @overload
    def CopyTo(self, destination: Stream, bufferSize: int) -> None:
        """"""
    @overload
    def CopyToAsync(self, destination: Stream) -> Task:
        """"""
    @overload
    def CopyToAsync(self, destination: Stream, bufferSize: int) -> Task:
        """"""
    @overload
    def CopyToAsync(
        self, destination: Stream, bufferSize: int, cancellationToken: CancellationToken
    ) -> Task:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    def Dispose(self) -> None:
        """"""
    def EndRead(self, asyncResult: IAsyncResult) -> int:
        """"""
    def EndWrite(self, asyncResult: IAsyncResult) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Flush(self) -> None:
        """"""
    @overload
    def FlushAsync(self) -> Task:
        """"""
    @overload
    def FlushAsync(self, cancellationToken: CancellationToken) -> Task:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetLifetimeService(self) -> object:
        """"""
    def GetType(self) -> Type:
        """"""
    def InitializeLifetimeService(self) -> object:
        """"""
    def Read(self, buffer: Array[int], offset: int, size: int) -> int:
        """"""
    @overload
    def ReadAsync(self, buffer: Array[int], offset: int, count: int) -> Task[int]:
        """"""
    @overload
    def ReadAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task[int]:
        """"""
    def ReadByte(self) -> int:
        """"""
    def Seek(self, offset: int, origin: SeekOrigin) -> int:
        """"""
    def SetLength(self, value: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def TrackRequestLifetime(self, requestStartTimestamp: int) -> None:
        """"""
    def Write(self, array: Array[int], offset: int, count: int) -> None:
        """"""
    @overload
    def WriteAsync(self, buffer: Array[int], offset: int, count: int) -> Task:
        """"""
    @overload
    def WriteAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task:
        """"""
    def WriteByte(self, value: int) -> None:
        """"""

class DelayedRegex(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class DelegatedStream(Stream, IDisposable):
    """"""
    @property
    def CanRead(self) -> bool:
        """"""
    @property
    def CanSeek(self) -> bool:
        """"""
    @property
    def CanTimeout(self) -> bool:
        """"""
    @property
    def CanWrite(self) -> bool:
        """"""
    @property
    def Length(self) -> int:
        """"""
    @property
    def Position(self) -> int:
        """"""
    @Position.setter
    def Position(self, value: int) -> None: ...
    @property
    def ReadTimeout(self) -> int:
        """"""
    @ReadTimeout.setter
    def ReadTimeout(self, value: int) -> None: ...
    @property
    def WriteTimeout(self) -> int:
        """"""
    @WriteTimeout.setter
    def WriteTimeout(self, value: int) -> None: ...
    def BeginRead(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """"""
    def BeginWrite(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """"""
    def Close(self) -> None:
        """"""
    @overload
    def CopyTo(self, destination: Stream) -> None:
        """"""
    @overload
    def CopyTo(self, destination: Stream, bufferSize: int) -> None:
        """"""
    @overload
    def CopyToAsync(self, destination: Stream) -> Task:
        """"""
    @overload
    def CopyToAsync(self, destination: Stream, bufferSize: int) -> Task:
        """"""
    @overload
    def CopyToAsync(
        self, destination: Stream, bufferSize: int, cancellationToken: CancellationToken
    ) -> Task:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    def Dispose(self) -> None:
        """"""
    def EndRead(self, asyncResult: IAsyncResult) -> int:
        """"""
    def EndWrite(self, asyncResult: IAsyncResult) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Flush(self) -> None:
        """"""
    @overload
    def FlushAsync(self) -> Task:
        """"""
    @overload
    def FlushAsync(self, cancellationToken: CancellationToken) -> Task:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetLifetimeService(self) -> object:
        """"""
    def GetType(self) -> Type:
        """"""
    def InitializeLifetimeService(self) -> object:
        """"""
    def Read(self, buffer: Array[int], offset: int, count: int) -> int:
        """"""
    @overload
    def ReadAsync(self, buffer: Array[int], offset: int, count: int) -> Task[int]:
        """"""
    @overload
    def ReadAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task[int]:
        """"""
    def ReadByte(self) -> int:
        """"""
    def Seek(self, offset: int, origin: SeekOrigin) -> int:
        """"""
    def SetLength(self, value: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def Write(self, buffer: Array[int], offset: int, count: int) -> None:
        """"""
    @overload
    def WriteAsync(self, buffer: Array[int], offset: int, count: int) -> Task:
        """"""
    @overload
    def WriteAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task:
        """"""
    def WriteByte(self, value: int) -> None:
        """"""

class DigestClient(Object, IAuthenticationModule, ISessionAuthenticationModule):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def AuthenticationType(self) -> str:
        """"""
    @property
    def CanPreAuthenticate(self) -> bool:
        """"""
    @property
    def CanUseDefaultCredentials(self) -> bool:
        """"""
    def Authenticate(
        self, challenge: str, webRequest: WebRequest, credentials: ICredentials
    ) -> Authorization:
        """"""
    def ClearSession(self, webRequest: WebRequest) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def PreAuthenticate(self, webRequest: WebRequest, credentials: ICredentials) -> Authorization:
        """"""
    def ToString(self) -> str:
        """"""
    def Update(self, challenge: str, webRequest: WebRequest) -> bool:
        """"""

class DirectProxy(ProxyChain, IEnumerable[Uri], IEnumerable, IDisposable):
    """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator[Uri]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def __iter__(self) -> Iterator[Uri]:
        """"""

class Dns(ABC, Object):
    """"""
    @classmethod
    def BeginGetHostAddresses(
        cls, hostNameOrAddress: str, requestCallback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """"""
    @classmethod
    def BeginGetHostByName(
        cls, hostName: str, requestCallback: AsyncCallback, stateObject: object
    ) -> IAsyncResult:
        """"""
    @classmethod
    @overload
    def BeginGetHostEntry(
        cls, address: IPAddress, requestCallback: AsyncCallback, stateObject: object
    ) -> IAsyncResult:
        """"""
    @classmethod
    @overload
    def BeginGetHostEntry(
        cls, hostNameOrAddress: str, requestCallback: AsyncCallback, stateObject: object
    ) -> IAsyncResult:
        """"""
    @classmethod
    def BeginResolve(
        cls, hostName: str, requestCallback: AsyncCallback, stateObject: object
    ) -> IAsyncResult:
        """"""
    @classmethod
    def EndGetHostAddresses(cls, asyncResult: IAsyncResult) -> Array[IPAddress]:
        """"""
    @classmethod
    def EndGetHostByName(cls, asyncResult: IAsyncResult) -> IPHostEntry:
        """"""
    @classmethod
    def EndGetHostEntry(cls, asyncResult: IAsyncResult) -> IPHostEntry:
        """"""
    @classmethod
    def EndResolve(cls, asyncResult: IAsyncResult) -> IPHostEntry:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @classmethod
    def GetHostAddresses(cls, hostNameOrAddress: str) -> Array[IPAddress]:
        """"""
    @classmethod
    def GetHostAddressesAsync(cls, hostNameOrAddress: str) -> Task[Array[IPAddress]]:
        """"""
    @classmethod
    @overload
    def GetHostByAddress(cls, address: IPAddress) -> IPHostEntry:
        """"""
    @classmethod
    @overload
    def GetHostByAddress(cls, address: str) -> IPHostEntry:
        """"""
    @classmethod
    def GetHostByName(cls, hostName: str) -> IPHostEntry:
        """"""
    @classmethod
    @overload
    def GetHostEntry(cls, address: IPAddress) -> IPHostEntry:
        """"""
    @classmethod
    @overload
    def GetHostEntry(cls, hostNameOrAddress: str) -> IPHostEntry:
        """"""
    @classmethod
    @overload
    def GetHostEntryAsync(cls, address: IPAddress) -> Task[IPHostEntry]:
        """"""
    @classmethod
    @overload
    def GetHostEntryAsync(cls, hostNameOrAddress: str) -> Task[IPHostEntry]:
        """"""
    @classmethod
    def GetHostName(cls) -> str:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def Resolve(cls, hostName: str) -> IPHostEntry:
        """"""
    def ToString(self) -> str:
        """"""

class DnsEndPoint(EndPoint):
    """"""
    @overload
    def __init__(self, host: str, port: int) -> None:
        """"""
    @overload
    def __init__(self, host: str, port: int, addressFamily: AddressFamily) -> None:
        """"""
    @property
    def AddressFamily(self) -> AddressFamily:
        """"""
    @property
    def Host(self) -> str:
        """"""
    @property
    def Port(self) -> int:
        """"""
    def Create(self, socketAddress: SocketAddress) -> EndPoint:
        """"""
    def Equals(self, comparand: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Serialize(self) -> SocketAddress:
        """"""
    def ToString(self) -> str:
        """"""

class DnsPermission(
    CodeAccessPermission, IUnrestrictedPermission, IPermission, ISecurityEncodable, IStackWalk
):
    """"""
    def __init__(self, state: PermissionState) -> None:
        """"""
    def Assert(self) -> None:
        """"""
    def Copy(self) -> IPermission:
        """"""
    def Demand(self) -> None:
        """"""
    def Deny(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def FromXml(self, securityElement: SecurityElement) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Intersect(self, target: IPermission) -> IPermission:
        """"""
    def IsSubsetOf(self, target: IPermission) -> bool:
        """"""
    def IsUnrestricted(self) -> bool:
        """"""
    def PermitOnly(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def ToXml(self) -> SecurityElement:
        """"""
    def Union(self, target: IPermission) -> IPermission:
        """"""

class DnsPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    """"""
    def __init__(self, action: SecurityAction) -> None:
        """"""
    @property
    def Action(self) -> SecurityAction:
        """"""
    @Action.setter
    def Action(self, value: SecurityAction) -> None: ...
    @property
    def TypeId(self) -> object:
        """"""
    @property
    def Unrestricted(self) -> bool:
        """"""
    @Unrestricted.setter
    def Unrestricted(self, value: bool) -> None: ...
    def CreatePermission(self) -> IPermission:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """"""
    def GetTypeInfoCount(self, pcTInfo: UInt32) -> tuple[None, UInt32]:
        """"""
    def Invoke(
        self,
        dispIdMember: int,
        riid: Guid,
        lcid: int,
        wFlags: int,
        pDispParams: IntPtr,
        pVarResult: IntPtr,
        pExcepInfo: IntPtr,
        puArgErr: IntPtr,
    ) -> None:
        """"""
    def IsDefaultAttribute(self) -> bool:
        """"""
    def Match(self, obj: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

class DownloadDataCompletedEventArgs(AsyncCompletedEventArgs):
    """"""
    @property
    def Cancelled(self) -> bool:
        """"""
    @property
    def Error(self) -> Exception:
        """"""
    @property
    def Result(self) -> Array[int]:
        """"""
    @property
    def UserState(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

type DownloadDataCompletedEventHandler = Callable[[object, DownloadDataCompletedEventArgs], None]
""""""

class DownloadProgressChangedEventArgs(ProgressChangedEventArgs):
    """"""
    @property
    def BytesReceived(self) -> int:
        """"""
    @property
    def ProgressPercentage(self) -> int:
        """"""
    @property
    def TotalBytesToReceive(self) -> int:
        """"""
    @property
    def UserState(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

type DownloadProgressChangedEventHandler = Callable[
    [object, DownloadProgressChangedEventArgs], None
]
""""""

class DownloadStringCompletedEventArgs(AsyncCompletedEventArgs):
    """"""
    @property
    def Cancelled(self) -> bool:
        """"""
    @property
    def Error(self) -> Exception:
        """"""
    @property
    def Result(self) -> str:
        """"""
    @property
    def UserState(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

type DownloadStringCompletedEventHandler = Callable[
    [object, DownloadStringCompletedEventArgs], None
]
""""""

class EmptyWebProxy(Object, IAutoWebProxy, IWebProxy):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Credentials(self) -> ICredentials:
        """"""
    @Credentials.setter
    def Credentials(self, value: ICredentials) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetProxies(self, destination: Uri) -> ProxyChain:
        """"""
    def GetProxy(self, uri: Uri) -> Uri:
        """"""
    def GetType(self) -> Type:
        """"""
    def IsBypassed(self, uri: Uri) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

class EndPoint(ABC, Object):
    """"""
    @property
    def AddressFamily(self) -> AddressFamily:
        """"""
    def Create(self, socketAddress: SocketAddress) -> EndPoint:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Serialize(self) -> SocketAddress:
        """"""
    def ToString(self) -> str:
        """"""

class Endianness(Enum):
    """"""

    Network: Endianness = ...
    """"""
    Native: Endianness = ...
    """"""

class EndpointPermission(Object):
    """"""
    @property
    def Hostname(self) -> str:
        """"""
    @property
    def Port(self) -> int:
        """"""
    @property
    def Transport(self) -> TransportType:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class EntitySendFormat(Enum):
    """"""

    ContentLength: EntitySendFormat = ...
    """"""
    Chunked: EntitySendFormat = ...
    """"""

class ExceptionHelper(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class FileWebRequest(WebRequest, ISerializable):
    """"""
    @property
    def AuthenticationLevel(self) -> AuthenticationLevel:
        """"""
    @AuthenticationLevel.setter
    def AuthenticationLevel(self, value: AuthenticationLevel) -> None: ...
    @property
    def CachePolicy(self) -> RequestCachePolicy:
        """"""
    @CachePolicy.setter
    def CachePolicy(self, value: RequestCachePolicy) -> None: ...
    @property
    def ConnectionGroupName(self) -> str:
        """"""
    @ConnectionGroupName.setter
    def ConnectionGroupName(self, value: str) -> None: ...
    @property
    def ContentLength(self) -> int:
        """"""
    @ContentLength.setter
    def ContentLength(self, value: int) -> None: ...
    @property
    def ContentType(self) -> str:
        """"""
    @ContentType.setter
    def ContentType(self, value: str) -> None: ...
    @property
    def CreatorInstance(self) -> IWebRequestCreate:
        """"""
    @property
    def Credentials(self) -> ICredentials:
        """"""
    @Credentials.setter
    def Credentials(self, value: ICredentials) -> None: ...
    @property
    def Headers(self) -> WebHeaderCollection:
        """"""
    @property
    def ImpersonationLevel(self) -> TokenImpersonationLevel:
        """"""
    @ImpersonationLevel.setter
    def ImpersonationLevel(self, value: TokenImpersonationLevel) -> None: ...
    @property
    def Method(self) -> str:
        """"""
    @Method.setter
    def Method(self, value: str) -> None: ...
    @property
    def PreAuthenticate(self) -> bool:
        """"""
    @PreAuthenticate.setter
    def PreAuthenticate(self, value: bool) -> None: ...
    @property
    def Proxy(self) -> IWebProxy:
        """"""
    @Proxy.setter
    def Proxy(self, value: IWebProxy) -> None: ...
    @property
    def RequestUri(self) -> Uri:
        """"""
    @property
    def Timeout(self) -> int:
        """"""
    @Timeout.setter
    def Timeout(self, value: int) -> None: ...
    @property
    def UseDefaultCredentials(self) -> bool:
        """"""
    @UseDefaultCredentials.setter
    def UseDefaultCredentials(self, value: bool) -> None: ...
    def Abort(self) -> None:
        """"""
    def BeginGetRequestStream(self, callback: AsyncCallback, state: object) -> IAsyncResult:
        """"""
    def BeginGetResponse(self, callback: AsyncCallback, state: object) -> IAsyncResult:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    def EndGetRequestStream(self, asyncResult: IAsyncResult) -> Stream:
        """"""
    def EndGetResponse(self, asyncResult: IAsyncResult) -> WebResponse:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetLifetimeService(self) -> object:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetRequestStream(self) -> Stream:
        """"""
    def GetRequestStreamAsync(self) -> Task[Stream]:
        """"""
    def GetResponse(self) -> WebResponse:
        """"""
    def GetResponseAsync(self) -> Task[WebResponse]:
        """"""
    def GetType(self) -> Type:
        """"""
    def InitializeLifetimeService(self) -> object:
        """"""
    def ToString(self) -> str:
        """"""

class FileWebRequestCreator(Object, IWebRequestCreate):
    """"""
    def Create(self, uri: Uri) -> WebRequest:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class FileWebResponse(WebResponse, ICloseEx, ISerializable, IDisposable):
    """"""
    @property
    def ContentLength(self) -> int:
        """"""
    @property
    def ContentType(self) -> str:
        """"""
    @property
    def Headers(self) -> WebHeaderCollection:
        """"""
    @property
    def IsFromCache(self) -> bool:
        """"""
    @property
    def IsMutuallyAuthenticated(self) -> bool:
        """"""
    @property
    def ResponseUri(self) -> Uri:
        """"""
    @property
    def SupportsHeaders(self) -> bool:
        """"""
    def Close(self) -> None:
        """"""
    def CloseEx(self, closeState: CloseExState) -> None:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetLifetimeService(self) -> object:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetResponseStream(self) -> Stream:
        """"""
    def GetType(self) -> Type:
        """"""
    def InitializeLifetimeService(self) -> object:
        """"""
    def ToString(self) -> str:
        """"""

class FileWebStream(FileStream, ICloseEx, IDisposable):
    """"""
    @overload
    def __init__(
        self,
        request: FileWebRequest,
        path: str,
        mode: FileMode,
        access: FileAccess,
        sharing: FileShare,
    ) -> None:
        """"""
    @overload
    def __init__(
        self,
        request: FileWebRequest,
        path: str,
        mode: FileMode,
        access: FileAccess,
        sharing: FileShare,
        length: int,
        _async: bool,
    ) -> None:
        """"""
    @property
    def CanRead(self) -> bool:
        """"""
    @property
    def CanSeek(self) -> bool:
        """"""
    @property
    def CanTimeout(self) -> bool:
        """"""
    @property
    def CanWrite(self) -> bool:
        """"""
    @property
    def Handle(self) -> IntPtr:
        """"""
    @property
    def IsAsync(self) -> bool:
        """"""
    @property
    def Length(self) -> int:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def Position(self) -> int:
        """"""
    @Position.setter
    def Position(self, value: int) -> None: ...
    @property
    def ReadTimeout(self) -> int:
        """"""
    @ReadTimeout.setter
    def ReadTimeout(self, value: int) -> None: ...
    @property
    def SafeFileHandle(self) -> SafeFileHandle:
        """"""
    @property
    def WriteTimeout(self) -> int:
        """"""
    @WriteTimeout.setter
    def WriteTimeout(self, value: int) -> None: ...
    def BeginRead(
        self, buffer: Array[int], offset: int, size: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """"""
    def BeginWrite(
        self, buffer: Array[int], offset: int, size: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """"""
    def Close(self) -> None:
        """"""
    def CloseEx(self, closeState: CloseExState) -> None:
        """"""
    @overload
    def CopyTo(self, destination: Stream) -> None:
        """"""
    @overload
    def CopyTo(self, destination: Stream, bufferSize: int) -> None:
        """"""
    @overload
    def CopyToAsync(self, destination: Stream) -> Task:
        """"""
    @overload
    def CopyToAsync(self, destination: Stream, bufferSize: int) -> Task:
        """"""
    @overload
    def CopyToAsync(
        self, destination: Stream, bufferSize: int, cancellationToken: CancellationToken
    ) -> Task:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    def Dispose(self) -> None:
        """"""
    def EndRead(self, ar: IAsyncResult) -> int:
        """"""
    def EndWrite(self, ar: IAsyncResult) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Flush(self) -> None:
        """"""
    @overload
    def Flush(self, flushToDisk: bool) -> None:
        """"""
    @overload
    def FlushAsync(self) -> Task:
        """"""
    @overload
    def FlushAsync(self, cancellationToken: CancellationToken) -> Task:
        """"""
    def GetAccessControl(self) -> FileSecurity:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetLifetimeService(self) -> object:
        """"""
    def GetType(self) -> Type:
        """"""
    def InitializeLifetimeService(self) -> object:
        """"""
    def Lock(self, position: int, length: int) -> None:
        """"""
    def Read(self, buffer: Array[int], offset: int, size: int) -> int:
        """"""
    @overload
    def ReadAsync(self, buffer: Array[int], offset: int, count: int) -> Task[int]:
        """"""
    @overload
    def ReadAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task[int]:
        """"""
    def ReadByte(self) -> int:
        """"""
    def Seek(self, offset: int, origin: SeekOrigin) -> int:
        """"""
    def SetAccessControl(self, fileSecurity: FileSecurity) -> None:
        """"""
    def SetLength(self, value: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def Unlock(self, position: int, length: int) -> None:
        """"""
    def Write(self, buffer: Array[int], offset: int, size: int) -> None:
        """"""
    @overload
    def WriteAsync(self, buffer: Array[int], offset: int, count: int) -> Task:
        """"""
    @overload
    def WriteAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task:
        """"""
    def WriteByte(self, value: int) -> None:
        """"""

class FixedSizeReader(Object):
    """"""
    def __init__(self, transport: Stream) -> None:
        """"""
    def AsyncReadPacket(self, request: AsyncProtocolRequest) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ReadPacket(self, buffer: Array[int], offset: int, count: int) -> int:
        """"""
    def ToString(self) -> str:
        """"""

class FrameHeader(Object):
    """"""

    DefaultMajorV: ClassVar[int]
    """"""
    DefaultMinorV: ClassVar[int]
    """"""
    HandshakeDoneId: ClassVar[int]
    """"""
    HandshakeErrId: ClassVar[int]
    """"""
    HandshakeId: ClassVar[int]
    """"""
    IgnoreValue: ClassVar[int]
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, messageId: int, majorV: int, minorV: int) -> None:
        """"""
    @property
    def MajorV(self) -> int:
        """"""
    @property
    def MaxMessageSize(self) -> int:
        """"""
    @property
    def MessageId(self) -> int:
        """"""
    @MessageId.setter
    def MessageId(self, value: int) -> None: ...
    @property
    def MinorV(self) -> int:
        """"""
    @property
    def PayloadSize(self) -> int:
        """"""
    @PayloadSize.setter
    def PayloadSize(self, value: int) -> None: ...
    @property
    def Size(self) -> int:
        """"""
    def CopyFrom(self, bytes: Array[int], start: int, verifier: FrameHeader) -> None:
        """"""
    def CopyTo(self, dest: Array[int], start: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class FtpControlStream(CommandStream, IDisposable):
    """"""
    @property
    def CanRead(self) -> bool:
        """"""
    @property
    def CanSeek(self) -> bool:
        """"""
    @property
    def CanTimeout(self) -> bool:
        """"""
    @property
    def CanWrite(self) -> bool:
        """"""
    @property
    def Length(self) -> int:
        """"""
    @property
    def Position(self) -> int:
        """"""
    @Position.setter
    def Position(self, value: int) -> None: ...
    @property
    def ReadTimeout(self) -> int:
        """"""
    @ReadTimeout.setter
    def ReadTimeout(self, value: int) -> None: ...
    @property
    def WriteTimeout(self) -> int:
        """"""
    @WriteTimeout.setter
    def WriteTimeout(self, value: int) -> None: ...
    def BeginRead(
        self, buffer: Array[int], offset: int, size: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """"""
    def BeginWrite(
        self, buffer: Array[int], offset: int, size: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """"""
    @overload
    def Close(self) -> None:
        """"""
    @overload
    def Close(self, timeout: int) -> None:
        """"""
    @overload
    def CopyTo(self, destination: Stream) -> None:
        """"""
    @overload
    def CopyTo(self, destination: Stream, bufferSize: int) -> None:
        """"""
    @overload
    def CopyToAsync(self, destination: Stream) -> Task:
        """"""
    @overload
    def CopyToAsync(self, destination: Stream, bufferSize: int) -> Task:
        """"""
    @overload
    def CopyToAsync(
        self, destination: Stream, bufferSize: int, cancellationToken: CancellationToken
    ) -> Task:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    def Dispose(self) -> None:
        """"""
    def EndRead(self, asyncResult: IAsyncResult) -> int:
        """"""
    def EndWrite(self, asyncResult: IAsyncResult) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Flush(self) -> None:
        """"""
    @overload
    def FlushAsync(self) -> Task:
        """"""
    @overload
    def FlushAsync(self, cancellationToken: CancellationToken) -> Task:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetLifetimeService(self) -> object:
        """"""
    def GetType(self) -> Type:
        """"""
    def InitializeLifetimeService(self) -> object:
        """"""
    def Read(self, buffer: Array[int], offset: int, size: int) -> int:
        """"""
    @overload
    def ReadAsync(self, buffer: Array[int], offset: int, count: int) -> Task[int]:
        """"""
    @overload
    def ReadAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task[int]:
        """"""
    def ReadByte(self) -> int:
        """"""
    def Seek(self, offset: int, origin: SeekOrigin) -> int:
        """"""
    def SetLength(self, value: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def Write(self, buffer: Array[int], offset: int, size: int) -> None:
        """"""
    @overload
    def WriteAsync(self, buffer: Array[int], offset: int, count: int) -> Task:
        """"""
    @overload
    def WriteAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task:
        """"""
    def WriteByte(self, value: int) -> None:
        """"""

class FtpDataStream(Stream, ICloseEx, IDisposable):
    """"""
    @property
    def CanRead(self) -> bool:
        """"""
    @property
    def CanSeek(self) -> bool:
        """"""
    @property
    def CanTimeout(self) -> bool:
        """"""
    @property
    def CanWrite(self) -> bool:
        """"""
    @property
    def Length(self) -> int:
        """"""
    @property
    def Position(self) -> int:
        """"""
    @Position.setter
    def Position(self, value: int) -> None: ...
    @property
    def ReadTimeout(self) -> int:
        """"""
    @ReadTimeout.setter
    def ReadTimeout(self, value: int) -> None: ...
    @property
    def WriteTimeout(self) -> int:
        """"""
    @WriteTimeout.setter
    def WriteTimeout(self, value: int) -> None: ...
    def BeginRead(
        self, buffer: Array[int], offset: int, size: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """"""
    def BeginWrite(
        self, buffer: Array[int], offset: int, size: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """"""
    def Close(self) -> None:
        """"""
    def CloseEx(self, closeState: CloseExState) -> None:
        """"""
    @overload
    def CopyTo(self, destination: Stream) -> None:
        """"""
    @overload
    def CopyTo(self, destination: Stream, bufferSize: int) -> None:
        """"""
    @overload
    def CopyToAsync(self, destination: Stream) -> Task:
        """"""
    @overload
    def CopyToAsync(self, destination: Stream, bufferSize: int) -> Task:
        """"""
    @overload
    def CopyToAsync(
        self, destination: Stream, bufferSize: int, cancellationToken: CancellationToken
    ) -> Task:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    def Dispose(self) -> None:
        """"""
    def EndRead(self, ar: IAsyncResult) -> int:
        """"""
    def EndWrite(self, asyncResult: IAsyncResult) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Flush(self) -> None:
        """"""
    @overload
    def FlushAsync(self) -> Task:
        """"""
    @overload
    def FlushAsync(self, cancellationToken: CancellationToken) -> Task:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetLifetimeService(self) -> object:
        """"""
    def GetType(self) -> Type:
        """"""
    def InitializeLifetimeService(self) -> object:
        """"""
    def Read(self, buffer: Array[int], offset: int, size: int) -> int:
        """"""
    @overload
    def ReadAsync(self, buffer: Array[int], offset: int, count: int) -> Task[int]:
        """"""
    @overload
    def ReadAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task[int]:
        """"""
    def ReadByte(self) -> int:
        """"""
    def Seek(self, offset: int, origin: SeekOrigin) -> int:
        """"""
    def SetLength(self, value: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def Write(self, buffer: Array[int], offset: int, size: int) -> None:
        """"""
    @overload
    def WriteAsync(self, buffer: Array[int], offset: int, count: int) -> Task:
        """"""
    @overload
    def WriteAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task:
        """"""
    def WriteByte(self, value: int) -> None:
        """"""

class FtpLoginState(Enum):
    """"""

    NotLoggedIn: FtpLoginState = ...
    """"""
    LoggedIn: FtpLoginState = ...
    """"""
    LoggedInButNeedsRelogin: FtpLoginState = ...
    """"""
    ReloginFailed: FtpLoginState = ...
    """"""

class FtpMethodFlags(Enum):
    """"""

    _None: FtpMethodFlags = ...
    """"""
    IsDownload: FtpMethodFlags = ...
    """"""
    IsUpload: FtpMethodFlags = ...
    """"""
    TakesParameter: FtpMethodFlags = ...
    """"""
    MayTakeParameter: FtpMethodFlags = ...
    """"""
    DoesNotTakeParameter: FtpMethodFlags = ...
    """"""
    ParameterIsDirectory: FtpMethodFlags = ...
    """"""
    ShouldParseForResponseUri: FtpMethodFlags = ...
    """"""
    HasHttpCommand: FtpMethodFlags = ...
    """"""
    MustChangeWorkingDirectoryToPath: FtpMethodFlags = ...
    """"""

class FtpMethodInfo(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class FtpOperation(Enum):
    """"""

    DownloadFile: FtpOperation = ...
    """"""
    ListDirectory: FtpOperation = ...
    """"""
    ListDirectoryDetails: FtpOperation = ...
    """"""
    UploadFile: FtpOperation = ...
    """"""
    UploadFileUnique: FtpOperation = ...
    """"""
    AppendFile: FtpOperation = ...
    """"""
    DeleteFile: FtpOperation = ...
    """"""
    GetDateTimestamp: FtpOperation = ...
    """"""
    GetFileSize: FtpOperation = ...
    """"""
    Rename: FtpOperation = ...
    """"""
    MakeDirectory: FtpOperation = ...
    """"""
    RemoveDirectory: FtpOperation = ...
    """"""
    PrintWorkingDirectory: FtpOperation = ...
    """"""
    Other: FtpOperation = ...
    """"""

class FtpPrimitive(Enum):
    """"""

    Upload: FtpPrimitive = ...
    """"""
    Download: FtpPrimitive = ...
    """"""
    CommandOnly: FtpPrimitive = ...
    """"""

class FtpStatusCode(Enum):
    """"""

    Undefined: FtpStatusCode = ...
    """"""
    RestartMarker: FtpStatusCode = ...
    """"""
    ServiceTemporarilyNotAvailable: FtpStatusCode = ...
    """"""
    DataAlreadyOpen: FtpStatusCode = ...
    """"""
    OpeningData: FtpStatusCode = ...
    """"""
    CommandOK: FtpStatusCode = ...
    """"""
    CommandExtraneous: FtpStatusCode = ...
    """"""
    DirectoryStatus: FtpStatusCode = ...
    """"""
    FileStatus: FtpStatusCode = ...
    """"""
    SystemType: FtpStatusCode = ...
    """"""
    SendUserCommand: FtpStatusCode = ...
    """"""
    ClosingControl: FtpStatusCode = ...
    """"""
    ClosingData: FtpStatusCode = ...
    """"""
    EnteringPassive: FtpStatusCode = ...
    """"""
    LoggedInProceed: FtpStatusCode = ...
    """"""
    ServerWantsSecureSession: FtpStatusCode = ...
    """"""
    FileActionOK: FtpStatusCode = ...
    """"""
    PathnameCreated: FtpStatusCode = ...
    """"""
    SendPasswordCommand: FtpStatusCode = ...
    """"""
    NeedLoginAccount: FtpStatusCode = ...
    """"""
    FileCommandPending: FtpStatusCode = ...
    """"""
    ServiceNotAvailable: FtpStatusCode = ...
    """"""
    CantOpenData: FtpStatusCode = ...
    """"""
    ConnectionClosed: FtpStatusCode = ...
    """"""
    ActionNotTakenFileUnavailableOrBusy: FtpStatusCode = ...
    """"""
    ActionAbortedLocalProcessingError: FtpStatusCode = ...
    """"""
    ActionNotTakenInsufficientSpace: FtpStatusCode = ...
    """"""
    CommandSyntaxError: FtpStatusCode = ...
    """"""
    ArgumentSyntaxError: FtpStatusCode = ...
    """"""
    CommandNotImplemented: FtpStatusCode = ...
    """"""
    BadCommandSequence: FtpStatusCode = ...
    """"""
    NotLoggedIn: FtpStatusCode = ...
    """"""
    AccountNeeded: FtpStatusCode = ...
    """"""
    ActionNotTakenFileUnavailable: FtpStatusCode = ...
    """"""
    ActionAbortedUnknownPageType: FtpStatusCode = ...
    """"""
    FileActionAborted: FtpStatusCode = ...
    """"""
    ActionNotTakenFilenameNotAllowed: FtpStatusCode = ...
    """"""

class FtpWebRequest(WebRequest, ISerializable):
    """"""
    @property
    def AuthenticationLevel(self) -> AuthenticationLevel:
        """"""
    @AuthenticationLevel.setter
    def AuthenticationLevel(self, value: AuthenticationLevel) -> None: ...
    @property
    def CachePolicy(self) -> RequestCachePolicy:
        """"""
    @CachePolicy.setter
    def CachePolicy(self, value: RequestCachePolicy) -> None: ...
    @property
    def ClientCertificates(self) -> X509CertificateCollection:
        """"""
    @ClientCertificates.setter
    def ClientCertificates(self, value: X509CertificateCollection) -> None: ...
    @property
    def ConnectionGroupName(self) -> str:
        """"""
    @ConnectionGroupName.setter
    def ConnectionGroupName(self, value: str) -> None: ...
    @property
    def ContentLength(self) -> int:
        """"""
    @ContentLength.setter
    def ContentLength(self, value: int) -> None: ...
    @property
    def ContentOffset(self) -> int:
        """"""
    @ContentOffset.setter
    def ContentOffset(self, value: int) -> None: ...
    @property
    def ContentType(self) -> str:
        """"""
    @ContentType.setter
    def ContentType(self, value: str) -> None: ...
    @property
    def CreatorInstance(self) -> IWebRequestCreate:
        """"""
    @property
    def Credentials(self) -> ICredentials:
        """"""
    @Credentials.setter
    def Credentials(self, value: ICredentials) -> None: ...
    @classmethod
    @property
    def DefaultCachePolicy(cls) -> RequestCachePolicy:
        """"""
    @classmethod
    @DefaultCachePolicy.setter
    def DefaultCachePolicy(cls, value: RequestCachePolicy) -> None: ...
    @property
    def EnableSsl(self) -> bool:
        """"""
    @EnableSsl.setter
    def EnableSsl(self, value: bool) -> None: ...
    @property
    def Headers(self) -> WebHeaderCollection:
        """"""
    @Headers.setter
    def Headers(self, value: WebHeaderCollection) -> None: ...
    @property
    def ImpersonationLevel(self) -> TokenImpersonationLevel:
        """"""
    @ImpersonationLevel.setter
    def ImpersonationLevel(self, value: TokenImpersonationLevel) -> None: ...
    @property
    def KeepAlive(self) -> bool:
        """"""
    @KeepAlive.setter
    def KeepAlive(self, value: bool) -> None: ...
    @property
    def Method(self) -> str:
        """"""
    @Method.setter
    def Method(self, value: str) -> None: ...
    @property
    def PreAuthenticate(self) -> bool:
        """"""
    @PreAuthenticate.setter
    def PreAuthenticate(self, value: bool) -> None: ...
    @property
    def Proxy(self) -> IWebProxy:
        """"""
    @Proxy.setter
    def Proxy(self, value: IWebProxy) -> None: ...
    @property
    def ReadWriteTimeout(self) -> int:
        """"""
    @ReadWriteTimeout.setter
    def ReadWriteTimeout(self, value: int) -> None: ...
    @property
    def RenameTo(self) -> str:
        """"""
    @RenameTo.setter
    def RenameTo(self, value: str) -> None: ...
    @property
    def RequestUri(self) -> Uri:
        """"""
    @property
    def ServicePoint(self) -> ServicePoint:
        """"""
    @property
    def Timeout(self) -> int:
        """"""
    @Timeout.setter
    def Timeout(self, value: int) -> None: ...
    @property
    def UseBinary(self) -> bool:
        """"""
    @UseBinary.setter
    def UseBinary(self, value: bool) -> None: ...
    @property
    def UseDefaultCredentials(self) -> bool:
        """"""
    @UseDefaultCredentials.setter
    def UseDefaultCredentials(self, value: bool) -> None: ...
    @property
    def UsePassive(self) -> bool:
        """"""
    @UsePassive.setter
    def UsePassive(self, value: bool) -> None: ...
    def Abort(self) -> None:
        """"""
    def BeginGetRequestStream(self, callback: AsyncCallback, state: object) -> IAsyncResult:
        """"""
    def BeginGetResponse(self, callback: AsyncCallback, state: object) -> IAsyncResult:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    def EndGetRequestStream(self, asyncResult: IAsyncResult) -> Stream:
        """"""
    def EndGetResponse(self, asyncResult: IAsyncResult) -> WebResponse:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetLifetimeService(self) -> object:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetRequestStream(self) -> Stream:
        """"""
    def GetRequestStreamAsync(self) -> Task[Stream]:
        """"""
    def GetResponse(self) -> WebResponse:
        """"""
    def GetResponseAsync(self) -> Task[WebResponse]:
        """"""
    def GetType(self) -> Type:
        """"""
    def InitializeLifetimeService(self) -> object:
        """"""
    def ToString(self) -> str:
        """"""

class FtpWebRequestCreator(Object, IWebRequestCreate):
    """"""
    def Create(self, uri: Uri) -> WebRequest:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class FtpWebResponse(WebResponse, ISerializable, IDisposable):
    """"""
    @property
    def BannerMessage(self) -> str:
        """"""
    @property
    def ContentLength(self) -> int:
        """"""
    @property
    def ContentType(self) -> str:
        """"""
    @ContentType.setter
    def ContentType(self, value: str) -> None: ...
    @property
    def ExitMessage(self) -> str:
        """"""
    @property
    def Headers(self) -> WebHeaderCollection:
        """"""
    @property
    def IsFromCache(self) -> bool:
        """"""
    @property
    def IsMutuallyAuthenticated(self) -> bool:
        """"""
    @property
    def LastModified(self) -> DateTime:
        """"""
    @property
    def ResponseUri(self) -> Uri:
        """"""
    @property
    def StatusCode(self) -> FtpStatusCode:
        """"""
    @property
    def StatusDescription(self) -> str:
        """"""
    @property
    def SupportsHeaders(self) -> bool:
        """"""
    @property
    def WelcomeMessage(self) -> str:
        """"""
    def Close(self) -> None:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetLifetimeService(self) -> object:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetResponseStream(self) -> Stream:
        """"""
    def GetType(self) -> Type:
        """"""
    def InitializeLifetimeService(self) -> object:
        """"""
    def ToString(self) -> str:
        """"""

class GZipWrapperStream(GZipStream, ICloseEx, IRequestLifetimeTracker, IDisposable):
    """"""
    def __init__(self, stream: Stream, mode: CompressionMode) -> None:
        """"""
    @property
    def BaseStream(self) -> Stream:
        """"""
    @property
    def CanRead(self) -> bool:
        """"""
    @property
    def CanSeek(self) -> bool:
        """"""
    @property
    def CanTimeout(self) -> bool:
        """"""
    @property
    def CanWrite(self) -> bool:
        """"""
    @property
    def Length(self) -> int:
        """"""
    @property
    def Position(self) -> int:
        """"""
    @Position.setter
    def Position(self, value: int) -> None: ...
    @property
    def ReadTimeout(self) -> int:
        """"""
    @ReadTimeout.setter
    def ReadTimeout(self, value: int) -> None: ...
    @property
    def WriteTimeout(self) -> int:
        """"""
    @WriteTimeout.setter
    def WriteTimeout(self, value: int) -> None: ...
    def BeginRead(
        self, buffer: Array[int], offset: int, size: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """"""
    def BeginWrite(
        self,
        array: Array[int],
        offset: int,
        count: int,
        asyncCallback: AsyncCallback,
        asyncState: object,
    ) -> IAsyncResult:
        """"""
    def Close(self) -> None:
        """"""
    def CloseEx(self, closeState: CloseExState) -> None:
        """"""
    @overload
    def CopyTo(self, destination: Stream) -> None:
        """"""
    @overload
    def CopyTo(self, destination: Stream, bufferSize: int) -> None:
        """"""
    @overload
    def CopyToAsync(self, destination: Stream) -> Task:
        """"""
    @overload
    def CopyToAsync(self, destination: Stream, bufferSize: int) -> Task:
        """"""
    @overload
    def CopyToAsync(
        self, destination: Stream, bufferSize: int, cancellationToken: CancellationToken
    ) -> Task:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    def Dispose(self) -> None:
        """"""
    def EndRead(self, asyncResult: IAsyncResult) -> int:
        """"""
    def EndWrite(self, asyncResult: IAsyncResult) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Flush(self) -> None:
        """"""
    @overload
    def FlushAsync(self) -> Task:
        """"""
    @overload
    def FlushAsync(self, cancellationToken: CancellationToken) -> Task:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetLifetimeService(self) -> object:
        """"""
    def GetType(self) -> Type:
        """"""
    def InitializeLifetimeService(self) -> object:
        """"""
    def Read(self, buffer: Array[int], offset: int, size: int) -> int:
        """"""
    @overload
    def ReadAsync(self, buffer: Array[int], offset: int, count: int) -> Task[int]:
        """"""
    @overload
    def ReadAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task[int]:
        """"""
    def ReadByte(self) -> int:
        """"""
    def Seek(self, offset: int, origin: SeekOrigin) -> int:
        """"""
    def SetLength(self, value: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def TrackRequestLifetime(self, requestStartTimestamp: int) -> None:
        """"""
    def Write(self, array: Array[int], offset: int, count: int) -> None:
        """"""
    @overload
    def WriteAsync(self, buffer: Array[int], offset: int, count: int) -> Task:
        """"""
    @overload
    def WriteAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task:
        """"""
    def WriteByte(self, value: int) -> None:
        """"""

type GeneralAsyncDelegate = Callable[[object, object], None]
""""""

class GlobalLog(ABC, Object):
    """"""
    @classmethod
    def AddToArray(cls, msg: str) -> None:
        """"""
    @classmethod
    @overload
    def Assert(cls, condition: bool, messageFormat: str, data: Array[object]) -> None:
        """"""
    @classmethod
    @overload
    def Assert(cls, message: str) -> None:
        """"""
    @classmethod
    @overload
    def Assert(cls, message: str, detailMessage: str) -> None:
        """"""
    @classmethod
    @overload
    def Dump(cls, buffer: Array[int]) -> None:
        """"""
    @classmethod
    @overload
    def Dump(cls, buffer: Array[int], length: int) -> None:
        """"""
    @classmethod
    @overload
    def Dump(cls, buffer: Array[int], offset: int, length: int) -> None:
        """"""
    @classmethod
    @overload
    def Dump(cls, buffer: IntPtr, offset: int, length: int) -> None:
        """"""
    @classmethod
    def DumpArray(cls) -> None:
        """"""
    @classmethod
    @overload
    def Enter(cls, func: str) -> None:
        """"""
    @classmethod
    @overload
    def Enter(cls, func: str, parms: str) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def Ignore(cls, msg: object) -> None:
        """"""
    @classmethod
    @overload
    def Leave(cls, func: str) -> None:
        """"""
    @classmethod
    @overload
    def Leave(cls, func: str, returnval: bool) -> None:
        """"""
    @classmethod
    @overload
    def Leave(cls, func: str, returnval: int) -> None:
        """"""
    @classmethod
    @overload
    def Leave(cls, func: str, result: str) -> None:
        """"""
    @classmethod
    def LeaveException(cls, func: str, exception: Exception) -> None:
        """"""
    @classmethod
    def Print(cls, msg: str) -> None:
        """"""
    @classmethod
    def PrintHex(cls, msg: str, value: object) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class GlobalProxySelection(Object):
    """"""
    def __init__(self) -> None:
        """"""
    @classmethod
    @property
    def Select(cls) -> IWebProxy:
        """"""
    @classmethod
    @Select.setter
    def Select(cls, value: IWebProxy) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def GetEmptyWebProxy(cls) -> IWebProxy:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class GlobalSSPI(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class HeaderInfo(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class HeaderInfoTable(Object):
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

type HeaderParser = Callable[[str], Array[str]]
""""""

class HeaderVariantInfo(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class HostHeaderString(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

type HttpAbortDelegate = Callable[[HttpWebRequest, WebException], bool]
""""""

class HttpBehaviour(Enum):
    """"""

    Unknown: HttpBehaviour = ...
    """"""
    HTTP10: HttpBehaviour = ...
    """"""
    HTTP11PartiallyCompliant: HttpBehaviour = ...
    """"""
    HTTP11: HttpBehaviour = ...
    """"""

type HttpContinueDelegate = Callable[[int, WebHeaderCollection], None]
""""""

class HttpDateParse(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def ParseHttpDate(cls, DateString: str, dtOut: DateTime) -> tuple[bool, DateTime]:
        """"""
    def ToString(self) -> str:
        """"""

class HttpDigest(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class HttpDigestChallenge(Object):
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
    def defineAttribute(self, name: str, value: str) -> bool:
        """"""

class HttpKnownHeaderNames(ABC, Object):
    """"""

    Accept: ClassVar[str]
    """"""
    AcceptCharset: ClassVar[str]
    """"""
    AcceptEncoding: ClassVar[str]
    """"""
    AcceptLanguage: ClassVar[str]
    """"""
    AcceptRanges: ClassVar[str]
    """"""
    Age: ClassVar[str]
    """"""
    Allow: ClassVar[str]
    """"""
    Authorization: ClassVar[str]
    """"""
    CacheControl: ClassVar[str]
    """"""
    Connection: ClassVar[str]
    """"""
    ContentDisposition: ClassVar[str]
    """"""
    ContentEncoding: ClassVar[str]
    """"""
    ContentLanguage: ClassVar[str]
    """"""
    ContentLength: ClassVar[str]
    """"""
    ContentLocation: ClassVar[str]
    """"""
    ContentMD5: ClassVar[str]
    """"""
    ContentRange: ClassVar[str]
    """"""
    ContentType: ClassVar[str]
    """"""
    Cookie: ClassVar[str]
    """"""
    Cookie2: ClassVar[str]
    """"""
    Date: ClassVar[str]
    """"""
    ETag: ClassVar[str]
    """"""
    Expect: ClassVar[str]
    """"""
    Expires: ClassVar[str]
    """"""
    From: ClassVar[str]
    """"""
    Host: ClassVar[str]
    """"""
    IfMatch: ClassVar[str]
    """"""
    IfModifiedSince: ClassVar[str]
    """"""
    IfNoneMatch: ClassVar[str]
    """"""
    IfRange: ClassVar[str]
    """"""
    IfUnmodifiedSince: ClassVar[str]
    """"""
    KeepAlive: ClassVar[str]
    """"""
    LastModified: ClassVar[str]
    """"""
    Location: ClassVar[str]
    """"""
    MaxForwards: ClassVar[str]
    """"""
    Origin: ClassVar[str]
    """"""
    P3P: ClassVar[str]
    """"""
    Pragma: ClassVar[str]
    """"""
    ProxyAuthenticate: ClassVar[str]
    """"""
    ProxyAuthorization: ClassVar[str]
    """"""
    ProxyConnection: ClassVar[str]
    """"""
    Range: ClassVar[str]
    """"""
    Referer: ClassVar[str]
    """"""
    RetryAfter: ClassVar[str]
    """"""
    SecWebSocketAccept: ClassVar[str]
    """"""
    SecWebSocketExtensions: ClassVar[str]
    """"""
    SecWebSocketKey: ClassVar[str]
    """"""
    SecWebSocketProtocol: ClassVar[str]
    """"""
    SecWebSocketVersion: ClassVar[str]
    """"""
    Server: ClassVar[str]
    """"""
    SetCookie: ClassVar[str]
    """"""
    SetCookie2: ClassVar[str]
    """"""
    TE: ClassVar[str]
    """"""
    Trailer: ClassVar[str]
    """"""
    TransferEncoding: ClassVar[str]
    """"""
    Upgrade: ClassVar[str]
    """"""
    UserAgent: ClassVar[str]
    """"""
    Vary: ClassVar[str]
    """"""
    Via: ClassVar[str]
    """"""
    WWWAuthenticate: ClassVar[str]
    """"""
    Warning: ClassVar[str]
    """"""
    XAspNetVersion: ClassVar[str]
    """"""
    XPoweredBy: ClassVar[str]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class HttpListener(Object, IDisposable):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def AuthenticationSchemeSelectorDelegate(self) -> AuthenticationSchemeSelector:
        """"""
    @AuthenticationSchemeSelectorDelegate.setter
    def AuthenticationSchemeSelectorDelegate(self, value: AuthenticationSchemeSelector) -> None: ...
    @property
    def AuthenticationSchemes(self) -> AuthenticationSchemes:
        """"""
    @AuthenticationSchemes.setter
    def AuthenticationSchemes(self, value: AuthenticationSchemes) -> None: ...
    @property
    def DefaultServiceNames(self) -> ServiceNameCollection:
        """"""
    @property
    def ExtendedProtectionPolicy(self) -> ExtendedProtectionPolicy:
        """"""
    @ExtendedProtectionPolicy.setter
    def ExtendedProtectionPolicy(self, value: ExtendedProtectionPolicy) -> None: ...
    @property
    def ExtendedProtectionSelectorDelegate(self) -> HttpListener.ExtendedProtectionSelector:
        """"""
    @ExtendedProtectionSelectorDelegate.setter
    def ExtendedProtectionSelectorDelegate(
        self, value: HttpListener.ExtendedProtectionSelector
    ) -> None: ...
    @property
    def IgnoreWriteExceptions(self) -> bool:
        """"""
    @IgnoreWriteExceptions.setter
    def IgnoreWriteExceptions(self, value: bool) -> None: ...
    @property
    def IsListening(self) -> bool:
        """"""
    @classmethod
    @property
    def IsSupported(cls) -> bool:
        """"""
    @property
    def Prefixes(self) -> HttpListenerPrefixCollection:
        """"""
    @property
    def Realm(self) -> str:
        """"""
    @Realm.setter
    def Realm(self, value: str) -> None: ...
    @property
    def TimeoutManager(self) -> HttpListenerTimeoutManager:
        """"""
    @property
    def UnsafeConnectionNtlmAuthentication(self) -> bool:
        """"""
    @UnsafeConnectionNtlmAuthentication.setter
    def UnsafeConnectionNtlmAuthentication(self, value: bool) -> None: ...
    def Abort(self) -> None:
        """"""
    def BeginGetContext(self, callback: AsyncCallback, state: object) -> IAsyncResult:
        """"""
    def Close(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def EndGetContext(self, asyncResult: IAsyncResult) -> HttpListenerContext:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetContext(self) -> HttpListenerContext:
        """"""
    def GetContextAsync(self) -> Task[HttpListenerContext]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Start(self) -> None:
        """"""
    def Stop(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    type ExtendedProtectionSelector = Callable[[HttpListenerRequest], ExtendedProtectionPolicy]
    """"""

class HttpListenerBasicIdentity(GenericIdentity, IIdentity):
    """"""
    def __init__(self, username: str, password: str) -> None:
        """"""
    @property
    def Actor(self) -> ClaimsIdentity:
        """"""
    @Actor.setter
    def Actor(self, value: ClaimsIdentity) -> None: ...
    @property
    def AuthenticationType(self) -> str:
        """"""
    @property
    def BootstrapContext(self) -> object:
        """"""
    @BootstrapContext.setter
    def BootstrapContext(self, value: object) -> None: ...
    @property
    def Claims(self) -> IEnumerable[Claim]:
        """"""
    @property
    def IsAuthenticated(self) -> bool:
        """"""
    @property
    def Label(self) -> str:
        """"""
    @Label.setter
    def Label(self, value: str) -> None: ...
    @property
    def Name(self) -> str:
        """"""
    @property
    def NameClaimType(self) -> str:
        """"""
    @property
    def Password(self) -> str:
        """"""
    @property
    def RoleClaimType(self) -> str:
        """"""
    def AddClaim(self, claim: Claim) -> None:
        """"""
    def AddClaims(self, claims: IEnumerable[Claim]) -> None:
        """"""
    def Clone(self) -> ClaimsIdentity:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def FindAll(self, match: Predicate[Claim]) -> IEnumerable[Claim]:
        """"""
    @overload
    def FindAll(self, type: str) -> IEnumerable[Claim]:
        """"""
    @overload
    def FindFirst(self, match: Predicate[Claim]) -> Claim:
        """"""
    @overload
    def FindFirst(self, type: str) -> Claim:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def HasClaim(self, match: Predicate[Claim]) -> bool:
        """"""
    @overload
    def HasClaim(self, type: str, value: str) -> bool:
        """"""
    def RemoveClaim(self, claim: Claim) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def TryRemoveClaim(self, claim: Claim) -> bool:
        """"""
    def WriteTo(self, writer: BinaryWriter) -> None:
        """"""

class HttpListenerContext(Object):
    """"""
    @property
    def Request(self) -> HttpListenerRequest:
        """"""
    @property
    def Response(self) -> HttpListenerResponse:
        """"""
    @property
    def User(self) -> IPrincipal:
        """"""
    @overload
    def AcceptWebSocketAsync(self, subProtocol: str) -> Task[HttpListenerWebSocketContext]:
        """"""
    @overload
    def AcceptWebSocketAsync(
        self, subProtocol: str, receiveBufferSize: int, keepAliveInterval: TimeSpan
    ) -> Task[HttpListenerWebSocketContext]:
        """"""
    @overload
    def AcceptWebSocketAsync(
        self,
        subProtocol: str,
        receiveBufferSize: int,
        keepAliveInterval: TimeSpan,
        internalBuffer: ArraySegment[int],
    ) -> Task[HttpListenerWebSocketContext]:
        """"""
    @overload
    def AcceptWebSocketAsync(
        self, subProtocol: str, keepAliveInterval: TimeSpan
    ) -> Task[HttpListenerWebSocketContext]:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class HttpListenerException(Win32Exception, _Exception, ISerializable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, errorCode: int) -> None:
        """"""
    @overload
    def __init__(self, errorCode: int, message: str) -> None:
        """"""
    @property
    def Data(self) -> IDictionary:
        """"""
    @property
    def ErrorCode(self) -> int:
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
    def InnerException(self) -> Exception:
        """"""
    @property
    def Message(self) -> str:
        """"""
    @property
    def NativeErrorCode(self) -> int:
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

class HttpListenerPrefixCollection(Object, ICollection[String], IEnumerable[String], IEnumerable):
    """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    def Add(self, uriPrefix: str) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    def Contains(self, uriPrefix: str) -> bool:
        """"""
    @overload
    def CopyTo(self, array: Array, offset: int) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array[str], offset: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator[str]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Remove(self, uriPrefix: str) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    def __contains__(self, uriPrefix: str) -> bool:
        """"""
    def __iter__(self) -> Iterator[str]:
        """"""
    def __delitem__(self, uriPrefix: str) -> bool:
        """"""
    def __len__(self) -> int:
        """"""

class HttpListenerRequest(Object):
    """"""
    @property
    def AcceptTypes(self) -> Array[str]:
        """"""
    @property
    def ClientCertificateError(self) -> int:
        """"""
    @property
    def ContentEncoding(self) -> Encoding:
        """"""
    @property
    def ContentLength64(self) -> int:
        """"""
    @property
    def ContentType(self) -> str:
        """"""
    @property
    def Cookies(self) -> CookieCollection:
        """"""
    @property
    def HasEntityBody(self) -> bool:
        """"""
    @property
    def Headers(self) -> NameValueCollection:
        """"""
    @property
    def HttpMethod(self) -> str:
        """"""
    @property
    def InputStream(self) -> Stream:
        """"""
    @property
    def IsAuthenticated(self) -> bool:
        """"""
    @property
    def IsLocal(self) -> bool:
        """"""
    @property
    def IsSecureConnection(self) -> bool:
        """"""
    @property
    def IsWebSocketRequest(self) -> bool:
        """"""
    @property
    def KeepAlive(self) -> bool:
        """"""
    @property
    def LocalEndPoint(self) -> IPEndPoint:
        """"""
    @property
    def ProtocolVersion(self) -> Version:
        """"""
    @property
    def QueryString(self) -> NameValueCollection:
        """"""
    @property
    def RawUrl(self) -> str:
        """"""
    @property
    def RemoteEndPoint(self) -> IPEndPoint:
        """"""
    @property
    def RequestTraceIdentifier(self) -> Guid:
        """"""
    @property
    def ServiceName(self) -> str:
        """"""
    @property
    def TransportContext(self) -> TransportContext:
        """"""
    @property
    def Url(self) -> Uri:
        """"""
    @property
    def UrlReferrer(self) -> Uri:
        """"""
    @property
    def UserAgent(self) -> str:
        """"""
    @property
    def UserHostAddress(self) -> str:
        """"""
    @property
    def UserHostName(self) -> str:
        """"""
    @property
    def UserLanguages(self) -> Array[str]:
        """"""
    def BeginGetClientCertificate(
        self, requestCallback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """"""
    def EndGetClientCertificate(self, asyncResult: IAsyncResult) -> X509Certificate2:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetClientCertificate(self) -> X509Certificate2:
        """"""
    def GetClientCertificateAsync(self) -> Task[X509Certificate2]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class HttpListenerRequestContext(TransportContext):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetChannelBinding(self, kind: ChannelBindingKind) -> ChannelBinding:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetTlsTokenBindings(self) -> IEnumerable[TokenBinding]:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class HttpListenerRequestUriBuilder(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @classmethod
    def GetRequestUri(
        cls,
        rawUri: str,
        cookedUriScheme: str,
        cookedUriHost: str,
        cookedUriPath: str,
        cookedUriQuery: str,
    ) -> Uri:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class HttpListenerResponse(Object, IDisposable):
    """"""
    @property
    def ContentEncoding(self) -> Encoding:
        """"""
    @ContentEncoding.setter
    def ContentEncoding(self, value: Encoding) -> None: ...
    @property
    def ContentLength64(self) -> int:
        """"""
    @ContentLength64.setter
    def ContentLength64(self, value: int) -> None: ...
    @property
    def ContentType(self) -> str:
        """"""
    @ContentType.setter
    def ContentType(self, value: str) -> None: ...
    @property
    def Cookies(self) -> CookieCollection:
        """"""
    @Cookies.setter
    def Cookies(self, value: CookieCollection) -> None: ...
    @property
    def Headers(self) -> WebHeaderCollection:
        """"""
    @Headers.setter
    def Headers(self, value: WebHeaderCollection) -> None: ...
    @property
    def KeepAlive(self) -> bool:
        """"""
    @KeepAlive.setter
    def KeepAlive(self, value: bool) -> None: ...
    @property
    def OutputStream(self) -> Stream:
        """"""
    @property
    def ProtocolVersion(self) -> Version:
        """"""
    @ProtocolVersion.setter
    def ProtocolVersion(self, value: Version) -> None: ...
    @property
    def RedirectLocation(self) -> str:
        """"""
    @RedirectLocation.setter
    def RedirectLocation(self, value: str) -> None: ...
    @property
    def SendChunked(self) -> bool:
        """"""
    @SendChunked.setter
    def SendChunked(self, value: bool) -> None: ...
    @property
    def StatusCode(self) -> int:
        """"""
    @StatusCode.setter
    def StatusCode(self, value: int) -> None: ...
    @property
    def StatusDescription(self) -> str:
        """"""
    @StatusDescription.setter
    def StatusDescription(self, value: str) -> None: ...
    def Abort(self) -> None:
        """"""
    def AddHeader(self, name: str, value: str) -> None:
        """"""
    def AppendCookie(self, cookie: Cookie) -> None:
        """"""
    def AppendHeader(self, name: str, value: str) -> None:
        """"""
    @overload
    def Close(self) -> None:
        """"""
    @overload
    def Close(self, responseEntity: Array[int], willBlock: bool) -> None:
        """"""
    def CopyFrom(self, templateResponse: HttpListenerResponse) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Redirect(self, url: str) -> None:
        """"""
    def SetCookie(self, cookie: Cookie) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class HttpListenerTimeoutManager(Object):
    """"""
    @property
    def DrainEntityBody(self) -> TimeSpan:
        """"""
    @DrainEntityBody.setter
    def DrainEntityBody(self, value: TimeSpan) -> None: ...
    @property
    def EntityBody(self) -> TimeSpan:
        """"""
    @EntityBody.setter
    def EntityBody(self, value: TimeSpan) -> None: ...
    @property
    def HeaderWait(self) -> TimeSpan:
        """"""
    @HeaderWait.setter
    def HeaderWait(self, value: TimeSpan) -> None: ...
    @property
    def IdleConnection(self) -> TimeSpan:
        """"""
    @IdleConnection.setter
    def IdleConnection(self, value: TimeSpan) -> None: ...
    @property
    def MinSendBytesPerSecond(self) -> int:
        """"""
    @MinSendBytesPerSecond.setter
    def MinSendBytesPerSecond(self, value: int) -> None: ...
    @property
    def RequestQueue(self) -> TimeSpan:
        """"""
    @RequestQueue.setter
    def RequestQueue(self, value: TimeSpan) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class HttpProcessingResult(Enum):
    """"""

    Continue: HttpProcessingResult = ...
    """"""
    ReadWait: HttpProcessingResult = ...
    """"""
    WriteWait: HttpProcessingResult = ...
    """"""

class HttpProtocolUtils(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class HttpRequestCreator(Object, IWebRequestCreate):
    """"""
    def __init__(self) -> None:
        """"""
    def Create(self, Uri: Uri) -> WebRequest:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class HttpRequestHeader(Enum):
    """"""

    CacheControl: HttpRequestHeader = ...
    """"""
    Connection: HttpRequestHeader = ...
    """"""
    Date: HttpRequestHeader = ...
    """"""
    KeepAlive: HttpRequestHeader = ...
    """"""
    Pragma: HttpRequestHeader = ...
    """"""
    Trailer: HttpRequestHeader = ...
    """"""
    TransferEncoding: HttpRequestHeader = ...
    """"""
    Upgrade: HttpRequestHeader = ...
    """"""
    Via: HttpRequestHeader = ...
    """"""
    Warning: HttpRequestHeader = ...
    """"""
    Allow: HttpRequestHeader = ...
    """"""
    ContentLength: HttpRequestHeader = ...
    """"""
    ContentType: HttpRequestHeader = ...
    """"""
    ContentEncoding: HttpRequestHeader = ...
    """"""
    ContentLanguage: HttpRequestHeader = ...
    """"""
    ContentLocation: HttpRequestHeader = ...
    """"""
    ContentMd5: HttpRequestHeader = ...
    """"""
    ContentRange: HttpRequestHeader = ...
    """"""
    Expires: HttpRequestHeader = ...
    """"""
    LastModified: HttpRequestHeader = ...
    """"""
    Accept: HttpRequestHeader = ...
    """"""
    AcceptCharset: HttpRequestHeader = ...
    """"""
    AcceptEncoding: HttpRequestHeader = ...
    """"""
    AcceptLanguage: HttpRequestHeader = ...
    """"""
    Authorization: HttpRequestHeader = ...
    """"""
    Cookie: HttpRequestHeader = ...
    """"""
    Expect: HttpRequestHeader = ...
    """"""
    From: HttpRequestHeader = ...
    """"""
    Host: HttpRequestHeader = ...
    """"""
    IfMatch: HttpRequestHeader = ...
    """"""
    IfModifiedSince: HttpRequestHeader = ...
    """"""
    IfNoneMatch: HttpRequestHeader = ...
    """"""
    IfRange: HttpRequestHeader = ...
    """"""
    IfUnmodifiedSince: HttpRequestHeader = ...
    """"""
    MaxForwards: HttpRequestHeader = ...
    """"""
    ProxyAuthorization: HttpRequestHeader = ...
    """"""
    Referer: HttpRequestHeader = ...
    """"""
    Range: HttpRequestHeader = ...
    """"""
    Te: HttpRequestHeader = ...
    """"""
    Translate: HttpRequestHeader = ...
    """"""
    UserAgent: HttpRequestHeader = ...
    """"""

class HttpRequestQueueV2Handle(CriticalHandleZeroOrMinusOneIsInvalid, IDisposable):
    """"""
    @property
    def IsClosed(self) -> bool:
        """"""
    @property
    def IsInvalid(self) -> bool:
        """"""
    def Close(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def SetHandleAsInvalid(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class HttpRequestStream(Stream, IDisposable):
    """"""
    @property
    def CanRead(self) -> bool:
        """"""
    @property
    def CanSeek(self) -> bool:
        """"""
    @property
    def CanTimeout(self) -> bool:
        """"""
    @property
    def CanWrite(self) -> bool:
        """"""
    @property
    def Length(self) -> int:
        """"""
    @property
    def Position(self) -> int:
        """"""
    @Position.setter
    def Position(self, value: int) -> None: ...
    @property
    def ReadTimeout(self) -> int:
        """"""
    @ReadTimeout.setter
    def ReadTimeout(self, value: int) -> None: ...
    @property
    def WriteTimeout(self) -> int:
        """"""
    @WriteTimeout.setter
    def WriteTimeout(self, value: int) -> None: ...
    def BeginRead(
        self, buffer: Array[int], offset: int, size: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """"""
    def BeginWrite(
        self, buffer: Array[int], offset: int, size: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """"""
    def Close(self) -> None:
        """"""
    @overload
    def CopyTo(self, destination: Stream) -> None:
        """"""
    @overload
    def CopyTo(self, destination: Stream, bufferSize: int) -> None:
        """"""
    @overload
    def CopyToAsync(self, destination: Stream) -> Task:
        """"""
    @overload
    def CopyToAsync(self, destination: Stream, bufferSize: int) -> Task:
        """"""
    @overload
    def CopyToAsync(
        self, destination: Stream, bufferSize: int, cancellationToken: CancellationToken
    ) -> Task:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    def Dispose(self) -> None:
        """"""
    def EndRead(self, asyncResult: IAsyncResult) -> int:
        """"""
    def EndWrite(self, asyncResult: IAsyncResult) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Flush(self) -> None:
        """"""
    @overload
    def FlushAsync(self) -> Task:
        """"""
    @overload
    def FlushAsync(self, cancellationToken: CancellationToken) -> Task:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetLifetimeService(self) -> object:
        """"""
    def GetType(self) -> Type:
        """"""
    def InitializeLifetimeService(self) -> object:
        """"""
    def Read(self, buffer: Array[int], offset: int, size: int) -> tuple[int, Array[int]]:
        """"""
    @overload
    def ReadAsync(self, buffer: Array[int], offset: int, count: int) -> Task[int]:
        """"""
    @overload
    def ReadAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task[int]:
        """"""
    def ReadByte(self) -> int:
        """"""
    def Seek(self, offset: int, origin: SeekOrigin) -> int:
        """"""
    def SetLength(self, value: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def Write(self, buffer: Array[int], offset: int, size: int) -> None:
        """"""
    @overload
    def WriteAsync(self, buffer: Array[int], offset: int, count: int) -> Task:
        """"""
    @overload
    def WriteAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task:
        """"""
    def WriteByte(self, value: int) -> None:
        """"""

class HttpResponseHeader(Enum):
    """"""

    CacheControl: HttpResponseHeader = ...
    """"""
    Connection: HttpResponseHeader = ...
    """"""
    Date: HttpResponseHeader = ...
    """"""
    KeepAlive: HttpResponseHeader = ...
    """"""
    Pragma: HttpResponseHeader = ...
    """"""
    Trailer: HttpResponseHeader = ...
    """"""
    TransferEncoding: HttpResponseHeader = ...
    """"""
    Upgrade: HttpResponseHeader = ...
    """"""
    Via: HttpResponseHeader = ...
    """"""
    Warning: HttpResponseHeader = ...
    """"""
    Allow: HttpResponseHeader = ...
    """"""
    ContentLength: HttpResponseHeader = ...
    """"""
    ContentType: HttpResponseHeader = ...
    """"""
    ContentEncoding: HttpResponseHeader = ...
    """"""
    ContentLanguage: HttpResponseHeader = ...
    """"""
    ContentLocation: HttpResponseHeader = ...
    """"""
    ContentMd5: HttpResponseHeader = ...
    """"""
    ContentRange: HttpResponseHeader = ...
    """"""
    Expires: HttpResponseHeader = ...
    """"""
    LastModified: HttpResponseHeader = ...
    """"""
    AcceptRanges: HttpResponseHeader = ...
    """"""
    Age: HttpResponseHeader = ...
    """"""
    ETag: HttpResponseHeader = ...
    """"""
    Location: HttpResponseHeader = ...
    """"""
    ProxyAuthenticate: HttpResponseHeader = ...
    """"""
    RetryAfter: HttpResponseHeader = ...
    """"""
    Server: HttpResponseHeader = ...
    """"""
    SetCookie: HttpResponseHeader = ...
    """"""
    Vary: HttpResponseHeader = ...
    """"""
    WwwAuthenticate: HttpResponseHeader = ...
    """"""

class HttpResponseStream(Stream, IDisposable):
    """"""
    @property
    def CanRead(self) -> bool:
        """"""
    @property
    def CanSeek(self) -> bool:
        """"""
    @property
    def CanTimeout(self) -> bool:
        """"""
    @property
    def CanWrite(self) -> bool:
        """"""
    @property
    def Length(self) -> int:
        """"""
    @property
    def Position(self) -> int:
        """"""
    @Position.setter
    def Position(self, value: int) -> None: ...
    @property
    def ReadTimeout(self) -> int:
        """"""
    @ReadTimeout.setter
    def ReadTimeout(self, value: int) -> None: ...
    @property
    def WriteTimeout(self) -> int:
        """"""
    @WriteTimeout.setter
    def WriteTimeout(self, value: int) -> None: ...
    def BeginRead(
        self, buffer: Array[int], offset: int, size: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """"""
    def BeginWrite(
        self, buffer: Array[int], offset: int, size: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """"""
    def Close(self) -> None:
        """"""
    @overload
    def CopyTo(self, destination: Stream) -> None:
        """"""
    @overload
    def CopyTo(self, destination: Stream, bufferSize: int) -> None:
        """"""
    @overload
    def CopyToAsync(self, destination: Stream) -> Task:
        """"""
    @overload
    def CopyToAsync(self, destination: Stream, bufferSize: int) -> Task:
        """"""
    @overload
    def CopyToAsync(
        self, destination: Stream, bufferSize: int, cancellationToken: CancellationToken
    ) -> Task:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    def Dispose(self) -> None:
        """"""
    def EndRead(self, asyncResult: IAsyncResult) -> int:
        """"""
    def EndWrite(self, asyncResult: IAsyncResult) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Flush(self) -> None:
        """"""
    @overload
    def FlushAsync(self) -> Task:
        """"""
    @overload
    def FlushAsync(self, cancellationToken: CancellationToken) -> Task:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetLifetimeService(self) -> object:
        """"""
    def GetType(self) -> Type:
        """"""
    def InitializeLifetimeService(self) -> object:
        """"""
    def Read(self, buffer: Array[int], offset: int, size: int) -> tuple[int, Array[int]]:
        """"""
    @overload
    def ReadAsync(self, buffer: Array[int], offset: int, count: int) -> Task[int]:
        """"""
    @overload
    def ReadAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task[int]:
        """"""
    def ReadByte(self) -> int:
        """"""
    def Seek(self, offset: int, origin: SeekOrigin) -> int:
        """"""
    def SetLength(self, value: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def Write(self, buffer: Array[int], offset: int, size: int) -> None:
        """"""
    @overload
    def WriteAsync(self, buffer: Array[int], offset: int, count: int) -> Task:
        """"""
    @overload
    def WriteAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task:
        """"""
    def WriteByte(self, value: int) -> None:
        """"""

class HttpResponseStreamAsyncResult(LazyAsyncResult, IAsyncResult):
    """"""
    @property
    def AsyncState(self) -> object:
        """"""
    @property
    def AsyncWaitHandle(self) -> WaitHandle:
        """"""
    @property
    def CompletedSynchronously(self) -> bool:
        """"""
    @property
    def IsCompleted(self) -> bool:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class HttpServerSessionHandle(CriticalHandleZeroOrMinusOneIsInvalid, IDisposable):
    """"""
    @property
    def IsClosed(self) -> bool:
        """"""
    @property
    def IsInvalid(self) -> bool:
        """"""
    def Close(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def SetHandleAsInvalid(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class HttpStatusCode(Enum):
    """"""

    Continue: HttpStatusCode = ...
    """"""
    SwitchingProtocols: HttpStatusCode = ...
    """"""
    OK: HttpStatusCode = ...
    """"""
    Created: HttpStatusCode = ...
    """"""
    Accepted: HttpStatusCode = ...
    """"""
    NonAuthoritativeInformation: HttpStatusCode = ...
    """"""
    NoContent: HttpStatusCode = ...
    """"""
    ResetContent: HttpStatusCode = ...
    """"""
    PartialContent: HttpStatusCode = ...
    """"""
    MultipleChoices: HttpStatusCode = ...
    """"""
    Ambiguous: HttpStatusCode = ...
    """"""
    MovedPermanently: HttpStatusCode = ...
    """"""
    Moved: HttpStatusCode = ...
    """"""
    Found: HttpStatusCode = ...
    """"""
    Redirect: HttpStatusCode = ...
    """"""
    SeeOther: HttpStatusCode = ...
    """"""
    RedirectMethod: HttpStatusCode = ...
    """"""
    NotModified: HttpStatusCode = ...
    """"""
    UseProxy: HttpStatusCode = ...
    """"""
    Unused: HttpStatusCode = ...
    """"""
    TemporaryRedirect: HttpStatusCode = ...
    """"""
    RedirectKeepVerb: HttpStatusCode = ...
    """"""
    BadRequest: HttpStatusCode = ...
    """"""
    Unauthorized: HttpStatusCode = ...
    """"""
    PaymentRequired: HttpStatusCode = ...
    """"""
    Forbidden: HttpStatusCode = ...
    """"""
    NotFound: HttpStatusCode = ...
    """"""
    MethodNotAllowed: HttpStatusCode = ...
    """"""
    NotAcceptable: HttpStatusCode = ...
    """"""
    ProxyAuthenticationRequired: HttpStatusCode = ...
    """"""
    RequestTimeout: HttpStatusCode = ...
    """"""
    Conflict: HttpStatusCode = ...
    """"""
    Gone: HttpStatusCode = ...
    """"""
    LengthRequired: HttpStatusCode = ...
    """"""
    PreconditionFailed: HttpStatusCode = ...
    """"""
    RequestEntityTooLarge: HttpStatusCode = ...
    """"""
    RequestUriTooLong: HttpStatusCode = ...
    """"""
    UnsupportedMediaType: HttpStatusCode = ...
    """"""
    RequestedRangeNotSatisfiable: HttpStatusCode = ...
    """"""
    ExpectationFailed: HttpStatusCode = ...
    """"""
    UpgradeRequired: HttpStatusCode = ...
    """"""
    InternalServerError: HttpStatusCode = ...
    """"""
    NotImplemented: HttpStatusCode = ...
    """"""
    BadGateway: HttpStatusCode = ...
    """"""
    ServiceUnavailable: HttpStatusCode = ...
    """"""
    GatewayTimeout: HttpStatusCode = ...
    """"""
    HttpVersionNotSupported: HttpStatusCode = ...
    """"""

class HttpStatusDescription(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class HttpSysSettings(ABC, Object):
    """"""
    @classmethod
    @property
    def EnableNonUtf8(cls) -> bool:
        """"""
    @classmethod
    @property
    def FavorUtf8(cls) -> bool:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class HttpVersion(Object):
    """"""

    Version10: ClassVar[Version]
    """"""
    Version11: ClassVar[Version]
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

class HttpWebRequest(WebRequest, ISerializable):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Accept(self) -> str:
        """"""
    @Accept.setter
    def Accept(self, value: str) -> None: ...
    @property
    def Address(self) -> Uri:
        """"""
    @property
    def AllowAutoRedirect(self) -> bool:
        """"""
    @AllowAutoRedirect.setter
    def AllowAutoRedirect(self, value: bool) -> None: ...
    @property
    def AllowReadStreamBuffering(self) -> bool:
        """"""
    @AllowReadStreamBuffering.setter
    def AllowReadStreamBuffering(self, value: bool) -> None: ...
    @property
    def AllowWriteStreamBuffering(self) -> bool:
        """"""
    @AllowWriteStreamBuffering.setter
    def AllowWriteStreamBuffering(self, value: bool) -> None: ...
    @property
    def AuthenticationLevel(self) -> AuthenticationLevel:
        """"""
    @AuthenticationLevel.setter
    def AuthenticationLevel(self, value: AuthenticationLevel) -> None: ...
    @property
    def AutomaticDecompression(self) -> DecompressionMethods:
        """"""
    @AutomaticDecompression.setter
    def AutomaticDecompression(self, value: DecompressionMethods) -> None: ...
    @property
    def CachePolicy(self) -> RequestCachePolicy:
        """"""
    @CachePolicy.setter
    def CachePolicy(self, value: RequestCachePolicy) -> None: ...
    @property
    def ClientCertificates(self) -> X509CertificateCollection:
        """"""
    @ClientCertificates.setter
    def ClientCertificates(self, value: X509CertificateCollection) -> None: ...
    @property
    def Connection(self) -> str:
        """"""
    @Connection.setter
    def Connection(self, value: str) -> None: ...
    @property
    def ConnectionGroupName(self) -> str:
        """"""
    @ConnectionGroupName.setter
    def ConnectionGroupName(self, value: str) -> None: ...
    @property
    def ContentLength(self) -> int:
        """"""
    @ContentLength.setter
    def ContentLength(self, value: int) -> None: ...
    @property
    def ContentType(self) -> str:
        """"""
    @ContentType.setter
    def ContentType(self, value: str) -> None: ...
    @property
    def ContinueDelegate(self) -> HttpContinueDelegate:
        """"""
    @ContinueDelegate.setter
    def ContinueDelegate(self, value: HttpContinueDelegate) -> None: ...
    @property
    def ContinueTimeout(self) -> int:
        """"""
    @ContinueTimeout.setter
    def ContinueTimeout(self, value: int) -> None: ...
    @property
    def CookieContainer(self) -> CookieContainer:
        """"""
    @CookieContainer.setter
    def CookieContainer(self, value: CookieContainer) -> None: ...
    @property
    def CreatorInstance(self) -> IWebRequestCreate:
        """"""
    @property
    def Credentials(self) -> ICredentials:
        """"""
    @Credentials.setter
    def Credentials(self, value: ICredentials) -> None: ...
    @property
    def Date(self) -> DateTime:
        """"""
    @Date.setter
    def Date(self, value: DateTime) -> None: ...
    @classmethod
    @property
    def DefaultCachePolicy(cls) -> RequestCachePolicy:
        """"""
    @classmethod
    @DefaultCachePolicy.setter
    def DefaultCachePolicy(cls, value: RequestCachePolicy) -> None: ...
    @classmethod
    @property
    def DefaultMaximumErrorResponseLength(cls) -> int:
        """"""
    @classmethod
    @DefaultMaximumErrorResponseLength.setter
    def DefaultMaximumErrorResponseLength(cls, value: int) -> None: ...
    @classmethod
    @property
    def DefaultMaximumResponseHeadersLength(cls) -> int:
        """"""
    @classmethod
    @DefaultMaximumResponseHeadersLength.setter
    def DefaultMaximumResponseHeadersLength(cls, value: int) -> None: ...
    @property
    def Expect(self) -> str:
        """"""
    @Expect.setter
    def Expect(self, value: str) -> None: ...
    @property
    def HaveResponse(self) -> bool:
        """"""
    @property
    def Headers(self) -> WebHeaderCollection:
        """"""
    @Headers.setter
    def Headers(self, value: WebHeaderCollection) -> None: ...
    @property
    def Host(self) -> str:
        """"""
    @Host.setter
    def Host(self, value: str) -> None: ...
    @property
    def IfModifiedSince(self) -> DateTime:
        """"""
    @IfModifiedSince.setter
    def IfModifiedSince(self, value: DateTime) -> None: ...
    @property
    def ImpersonationLevel(self) -> TokenImpersonationLevel:
        """"""
    @ImpersonationLevel.setter
    def ImpersonationLevel(self, value: TokenImpersonationLevel) -> None: ...
    @property
    def KeepAlive(self) -> bool:
        """"""
    @KeepAlive.setter
    def KeepAlive(self, value: bool) -> None: ...
    @property
    def MaximumAutomaticRedirections(self) -> int:
        """"""
    @MaximumAutomaticRedirections.setter
    def MaximumAutomaticRedirections(self, value: int) -> None: ...
    @property
    def MaximumResponseHeadersLength(self) -> int:
        """"""
    @MaximumResponseHeadersLength.setter
    def MaximumResponseHeadersLength(self, value: int) -> None: ...
    @property
    def MediaType(self) -> str:
        """"""
    @MediaType.setter
    def MediaType(self, value: str) -> None: ...
    @property
    def Method(self) -> str:
        """"""
    @Method.setter
    def Method(self, value: str) -> None: ...
    @property
    def Pipelined(self) -> bool:
        """"""
    @Pipelined.setter
    def Pipelined(self, value: bool) -> None: ...
    @property
    def PreAuthenticate(self) -> bool:
        """"""
    @PreAuthenticate.setter
    def PreAuthenticate(self, value: bool) -> None: ...
    @property
    def ProtocolVersion(self) -> Version:
        """"""
    @ProtocolVersion.setter
    def ProtocolVersion(self, value: Version) -> None: ...
    @property
    def Proxy(self) -> IWebProxy:
        """"""
    @Proxy.setter
    def Proxy(self, value: IWebProxy) -> None: ...
    @property
    def ReadWriteTimeout(self) -> int:
        """"""
    @ReadWriteTimeout.setter
    def ReadWriteTimeout(self, value: int) -> None: ...
    @property
    def Referer(self) -> str:
        """"""
    @Referer.setter
    def Referer(self, value: str) -> None: ...
    @property
    def RequestUri(self) -> Uri:
        """"""
    @property
    def SendChunked(self) -> bool:
        """"""
    @SendChunked.setter
    def SendChunked(self, value: bool) -> None: ...
    @property
    def ServerCertificateValidationCallback(self) -> RemoteCertificateValidationCallback:
        """"""
    @ServerCertificateValidationCallback.setter
    def ServerCertificateValidationCallback(
        self, value: RemoteCertificateValidationCallback
    ) -> None: ...
    @property
    def ServicePoint(self) -> ServicePoint:
        """"""
    @property
    def SupportsCookieContainer(self) -> bool:
        """"""
    @property
    def Timeout(self) -> int:
        """"""
    @Timeout.setter
    def Timeout(self, value: int) -> None: ...
    @property
    def TransferEncoding(self) -> str:
        """"""
    @TransferEncoding.setter
    def TransferEncoding(self, value: str) -> None: ...
    @property
    def UnsafeAuthenticatedConnectionSharing(self) -> bool:
        """"""
    @UnsafeAuthenticatedConnectionSharing.setter
    def UnsafeAuthenticatedConnectionSharing(self, value: bool) -> None: ...
    @property
    def UseDefaultCredentials(self) -> bool:
        """"""
    @UseDefaultCredentials.setter
    def UseDefaultCredentials(self, value: bool) -> None: ...
    @property
    def UserAgent(self) -> str:
        """"""
    @UserAgent.setter
    def UserAgent(self, value: str) -> None: ...
    def Abort(self) -> None:
        """"""
    @overload
    def AddRange(self, range: int) -> None:
        """"""
    @overload
    def AddRange(self, _from: int, to: int) -> None:
        """"""
    @overload
    def AddRange(self, range: int) -> None:
        """"""
    @overload
    def AddRange(self, _from: int, to: int) -> None:
        """"""
    @overload
    def AddRange(self, rangeSpecifier: str, range: int) -> None:
        """"""
    @overload
    def AddRange(self, rangeSpecifier: str, _from: int, to: int) -> None:
        """"""
    @overload
    def AddRange(self, rangeSpecifier: str, range: int) -> None:
        """"""
    @overload
    def AddRange(self, rangeSpecifier: str, _from: int, to: int) -> None:
        """"""
    def BeginGetRequestStream(self, callback: AsyncCallback, state: object) -> IAsyncResult:
        """"""
    def BeginGetResponse(self, callback: AsyncCallback, state: object) -> IAsyncResult:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    @overload
    def EndGetRequestStream(self, asyncResult: IAsyncResult) -> Stream:
        """"""
    @overload
    def EndGetRequestStream(
        self, asyncResult: IAsyncResult, context: TransportContext
    ) -> tuple[Stream, TransportContext]:
        """"""
    def EndGetResponse(self, asyncResult: IAsyncResult) -> WebResponse:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetLifetimeService(self) -> object:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    @overload
    def GetRequestStream(self) -> Stream:
        """"""
    @overload
    def GetRequestStream(self, context: TransportContext) -> tuple[Stream, TransportContext]:
        """"""
    def GetRequestStreamAsync(self) -> Task[Stream]:
        """"""
    def GetResponse(self) -> WebResponse:
        """"""
    def GetResponseAsync(self) -> Task[WebResponse]:
        """"""
    def GetType(self) -> Type:
        """"""
    def InitializeLifetimeService(self) -> object:
        """"""
    def ToString(self) -> str:
        """"""

class HttpWebResponse(WebResponse, ISerializable, IDisposable):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def CharacterSet(self) -> str:
        """"""
    @property
    def ContentEncoding(self) -> str:
        """"""
    @property
    def ContentLength(self) -> int:
        """"""
    @property
    def ContentType(self) -> str:
        """"""
    @property
    def Cookies(self) -> CookieCollection:
        """"""
    @Cookies.setter
    def Cookies(self, value: CookieCollection) -> None: ...
    @property
    def Headers(self) -> WebHeaderCollection:
        """"""
    @property
    def IsFromCache(self) -> bool:
        """"""
    @property
    def IsMutuallyAuthenticated(self) -> bool:
        """"""
    @property
    def LastModified(self) -> DateTime:
        """"""
    @property
    def Method(self) -> str:
        """"""
    @property
    def ProtocolVersion(self) -> Version:
        """"""
    @property
    def ResponseUri(self) -> Uri:
        """"""
    @property
    def Server(self) -> str:
        """"""
    @property
    def StatusCode(self) -> HttpStatusCode:
        """"""
    @property
    def StatusDescription(self) -> str:
        """"""
    @property
    def SupportsHeaders(self) -> bool:
        """"""
    def Close(self) -> None:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetLifetimeService(self) -> object:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetResponseHeader(self, headerName: str) -> str:
        """"""
    def GetResponseStream(self) -> Stream:
        """"""
    def GetType(self) -> Type:
        """"""
    def InitializeLifetimeService(self) -> object:
        """"""
    def ToString(self) -> str:
        """"""

class HttpWriteMode(Enum):
    """"""

    Unknown: HttpWriteMode = ...
    """"""
    ContentLength: HttpWriteMode = ...
    """"""
    Chunked: HttpWriteMode = ...
    """"""
    Buffer: HttpWriteMode = ...
    """"""
    _None: HttpWriteMode = ...
    """"""

class HybridWebProxyFinder(Object, IWebProxyFinder, IDisposable):
    """"""
    def __init__(self, engine: AutoWebProxyScriptEngine) -> None:
        """"""
    @property
    def IsValid(self) -> bool:
        """"""
    def Abort(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetProxies(self, destination: Uri, proxyList: IList[str]) -> tuple[bool, IList[str]]:
        """"""
    def GetType(self) -> Type:
        """"""
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class IAuthenticationManager(ABC):
    """"""
    @property
    def CredentialPolicy(self) -> ICredentialPolicy:
        """"""
    @CredentialPolicy.setter
    def CredentialPolicy(self, value: ICredentialPolicy) -> None: ...
    @property
    def CustomTargetNameDictionary(self) -> StringDictionary:
        """"""
    @property
    def OSSupportsExtendedProtection(self) -> bool:
        """"""
    @property
    def RegisteredModules(self) -> IEnumerator:
        """"""
    @property
    def SpnDictionary(self) -> SpnDictionary:
        """"""
    @property
    def SspSupportsExtendedProtection(self) -> bool:
        """"""
    def Authenticate(
        self, challenge: str, request: WebRequest, credentials: ICredentials
    ) -> Authorization:
        """"""
    def BindModule(self, uri: Uri, response: Authorization, module: IAuthenticationModule) -> None:
        """"""
    def EnsureConfigLoaded(self) -> None:
        """"""
    def PreAuthenticate(self, request: WebRequest, credentials: ICredentials) -> Authorization:
        """"""
    def Register(self, authenticationModule: IAuthenticationModule) -> None:
        """"""
    @overload
    def Unregister(self, authenticationModule: IAuthenticationModule) -> None:
        """"""
    @overload
    def Unregister(self, authenticationScheme: str) -> None:
        """"""

class IAuthenticationModule(ABC):
    """"""
    @property
    def AuthenticationType(self) -> str:
        """"""
    @property
    def CanPreAuthenticate(self) -> bool:
        """"""
    def Authenticate(
        self, challenge: str, request: WebRequest, credentials: ICredentials
    ) -> Authorization:
        """"""
    def PreAuthenticate(self, request: WebRequest, credentials: ICredentials) -> Authorization:
        """"""

class IAutoWebProxy(ABC, IWebProxy):
    """"""
    @property
    def Credentials(self) -> ICredentials:
        """"""
    @Credentials.setter
    def Credentials(self, value: ICredentials) -> None: ...
    def GetProxies(self, destination: Uri) -> ProxyChain:
        """"""
    def GetProxy(self, destination: Uri) -> Uri:
        """"""
    def IsBypassed(self, host: Uri) -> bool:
        """"""

class ICertificatePolicy(ABC):
    """"""
    def CheckValidationResult(
        self,
        srvPoint: ServicePoint,
        certificate: X509Certificate,
        request: WebRequest,
        certificateProblem: int,
    ) -> bool:
        """"""

class ICloseEx(ABC):
    """"""
    def CloseEx(self, closeState: CloseExState) -> None:
        """"""

class ICredentialPolicy(ABC):
    """"""
    def ShouldSendCredential(
        self,
        challengeUri: Uri,
        request: WebRequest,
        credential: NetworkCredential,
        authenticationModule: IAuthenticationModule,
    ) -> bool:
        """"""

class ICredentials(ABC):
    """"""
    def GetCredential(self, uri: Uri, authType: str) -> NetworkCredential:
        """"""

class ICredentialsByHost(ABC):
    """"""
    def GetCredential(self, host: str, port: int, authenticationType: str) -> NetworkCredential:
        """"""

class IPAddress(Object):
    """"""

    Any: ClassVar[IPAddress]
    """"""
    Broadcast: ClassVar[IPAddress]
    """"""
    IPv6Any: ClassVar[IPAddress]
    """"""
    IPv6Loopback: ClassVar[IPAddress]
    """"""
    IPv6None: ClassVar[IPAddress]
    """"""
    Loopback: ClassVar[IPAddress]
    """"""
    _None: ClassVar[IPAddress]
    """"""
    @overload
    def __init__(self, newAddress: int) -> None:
        """"""
    @overload
    def __init__(self, address: Array[int], scopeid: int) -> None:
        """"""
    @overload
    def __init__(self, address: Array[int]) -> None:
        """"""
    @property
    def Address(self) -> int:
        """"""
    @Address.setter
    def Address(self, value: int) -> None: ...
    @property
    def AddressFamily(self) -> AddressFamily:
        """"""
    @property
    def IsIPv4MappedToIPv6(self) -> bool:
        """"""
    @property
    def IsIPv6LinkLocal(self) -> bool:
        """"""
    @property
    def IsIPv6Multicast(self) -> bool:
        """"""
    @property
    def IsIPv6SiteLocal(self) -> bool:
        """"""
    @property
    def IsIPv6Teredo(self) -> bool:
        """"""
    @property
    def ScopeId(self) -> int:
        """"""
    @ScopeId.setter
    def ScopeId(self, value: int) -> None: ...
    def Equals(self, comparand: object) -> bool:
        """"""
    def GetAddressBytes(self) -> Array[int]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    @overload
    def HostToNetworkOrder(cls, host: int) -> int:
        """"""
    @classmethod
    @overload
    def HostToNetworkOrder(cls, host: int) -> int:
        """"""
    @classmethod
    @overload
    def HostToNetworkOrder(cls, host: int) -> int:
        """"""
    @classmethod
    def IsLoopback(cls, address: IPAddress) -> bool:
        """"""
    def MapToIPv4(self) -> IPAddress:
        """"""
    def MapToIPv6(self) -> IPAddress:
        """"""
    @classmethod
    @overload
    def NetworkToHostOrder(cls, network: int) -> int:
        """"""
    @classmethod
    @overload
    def NetworkToHostOrder(cls, network: int) -> int:
        """"""
    @classmethod
    @overload
    def NetworkToHostOrder(cls, network: int) -> int:
        """"""
    @classmethod
    def Parse(cls, ipString: str) -> IPAddress:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def TryParse(cls, ipString: str, address: IPAddress) -> tuple[bool, IPAddress]:
        """"""

class IPEndPoint(EndPoint):
    """"""

    MaxPort: ClassVar[int]
    """"""
    MinPort: ClassVar[int]
    """"""
    @overload
    def __init__(self, address: int, port: int) -> None:
        """"""
    @overload
    def __init__(self, address: IPAddress, port: int) -> None:
        """"""
    @property
    def Address(self) -> IPAddress:
        """"""
    @Address.setter
    def Address(self, value: IPAddress) -> None: ...
    @property
    def AddressFamily(self) -> AddressFamily:
        """"""
    @property
    def Port(self) -> int:
        """"""
    @Port.setter
    def Port(self, value: int) -> None: ...
    def Create(self, socketAddress: SocketAddress) -> EndPoint:
        """"""
    def Equals(self, comparand: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Serialize(self) -> SocketAddress:
        """"""
    def ToString(self) -> str:
        """"""

class IPHostEntry(Object):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def AddressList(self) -> Array[IPAddress]:
        """"""
    @AddressList.setter
    def AddressList(self, value: Array[IPAddress]) -> None: ...
    @property
    def Aliases(self) -> Array[str]:
        """"""
    @Aliases.setter
    def Aliases(self, value: Array[str]) -> None: ...
    @property
    def HostName(self) -> str:
        """"""
    @HostName.setter
    def HostName(self, value: str) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class IPMulticastRequest(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class IPv6MulticastRequest(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class IRequestLifetimeTracker(ABC):
    """"""
    def TrackRequestLifetime(self, requestStartTimestamp: int) -> None:
        """"""

class ISessionAuthenticationModule(ABC, IAuthenticationModule):
    """"""
    @property
    def AuthenticationType(self) -> str:
        """"""
    @property
    def CanPreAuthenticate(self) -> bool:
        """"""
    @property
    def CanUseDefaultCredentials(self) -> bool:
        """"""
    def Authenticate(
        self, challenge: str, request: WebRequest, credentials: ICredentials
    ) -> Authorization:
        """"""
    def ClearSession(self, webRequest: WebRequest) -> None:
        """"""
    def PreAuthenticate(self, request: WebRequest, credentials: ICredentials) -> Authorization:
        """"""
    def Update(self, challenge: str, webRequest: WebRequest) -> bool:
        """"""

class IWebProxy(ABC):
    """"""
    @property
    def Credentials(self) -> ICredentials:
        """"""
    @Credentials.setter
    def Credentials(self, value: ICredentials) -> None: ...
    def GetProxy(self, destination: Uri) -> Uri:
        """"""
    def IsBypassed(self, host: Uri) -> bool:
        """"""

class IWebProxyFinder(ABC, IDisposable):
    """"""
    @property
    def IsValid(self) -> bool:
        """"""
    def Abort(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def GetProxies(self, destination: Uri, proxyList: IList[str]) -> tuple[bool, IList[str]]:
        """"""
    def Reset(self) -> None:
        """"""

class IWebProxyScript(ABC):
    """"""
    def Close(self) -> None:
        """"""
    def Load(self, scriptLocation: Uri, script: str, helperType: Type) -> bool:
        """"""
    def Run(self, url: str, host: str) -> str:
        """"""

class IWebRequestCreate(ABC):
    """"""
    def Create(self, uri: Uri) -> WebRequest:
        """"""

class IgnoreCertProblem(Enum):
    """"""

    not_time_valid: IgnoreCertProblem = ...
    """"""
    ctl_not_time_valid: IgnoreCertProblem = ...
    """"""
    not_time_nested: IgnoreCertProblem = ...
    """"""
    all_not_time_valid: IgnoreCertProblem = ...
    """"""
    invalid_basic_constraints: IgnoreCertProblem = ...
    """"""
    allow_unknown_ca: IgnoreCertProblem = ...
    """"""
    wrong_usage: IgnoreCertProblem = ...
    """"""
    invalid_name: IgnoreCertProblem = ...
    """"""
    invalid_policy: IgnoreCertProblem = ...
    """"""
    end_rev_unknown: IgnoreCertProblem = ...
    """"""
    ctl_signer_rev_unknown: IgnoreCertProblem = ...
    """"""
    ca_rev_unknown: IgnoreCertProblem = ...
    """"""
    root_rev_unknown: IgnoreCertProblem = ...
    """"""
    all_rev_unknown: IgnoreCertProblem = ...
    """"""
    none: IgnoreCertProblem = ...
    """"""

class IntPtrHelper(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class InterlockedGate(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class InterlockedStack(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class InternalException(SystemException, _Exception, ISerializable):
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
    def InnerException(self) -> Exception:
        """"""
    @property
    def Message(self) -> str:
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

class IssuerListInfoEx(ValueType):
    """"""

    aIssuers: Final[SafeHandle]
    """"""
    cIssuers: Final[int]
    """"""
    def __init__(self, handle: SafeHandle, nativeBuffer: Array[int]) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class KerberosClient(Object, IAuthenticationModule, ISessionAuthenticationModule):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def AuthenticationType(self) -> str:
        """"""
    @property
    def CanPreAuthenticate(self) -> bool:
        """"""
    @property
    def CanUseDefaultCredentials(self) -> bool:
        """"""
    def Authenticate(
        self, challenge: str, webRequest: WebRequest, credentials: ICredentials
    ) -> Authorization:
        """"""
    def ClearSession(self, webRequest: WebRequest) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def PreAuthenticate(self, webRequest: WebRequest, credentials: ICredentials) -> Authorization:
        """"""
    def ToString(self) -> str:
        """"""
    def Update(self, challenge: str, webRequest: WebRequest) -> bool:
        """"""

class KnownHttpVerb(Object):
    """"""
    @overload
    def Equals(self, verb: KnownHttpVerb) -> bool:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def Parse(cls, name: str) -> KnownHttpVerb:
        """"""
    def ToString(self) -> str:
        """"""

class LazyAsyncResult(Object, IAsyncResult):
    """"""
    @property
    def AsyncState(self) -> object:
        """"""
    @property
    def AsyncWaitHandle(self) -> WaitHandle:
        """"""
    @property
    def CompletedSynchronously(self) -> bool:
        """"""
    @property
    def IsCompleted(self) -> bool:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class Linger(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ListenerAsyncResult(LazyAsyncResult, IAsyncResult):
    """"""
    @property
    def AsyncState(self) -> object:
        """"""
    @property
    def AsyncWaitHandle(self) -> WaitHandle:
        """"""
    @property
    def CompletedSynchronously(self) -> bool:
        """"""
    @property
    def IsCompleted(self) -> bool:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ListenerClientCertAsyncResult(LazyAsyncResult, IAsyncResult):
    """"""
    @property
    def AsyncState(self) -> object:
        """"""
    @property
    def AsyncWaitHandle(self) -> WaitHandle:
        """"""
    @property
    def CompletedSynchronously(self) -> bool:
        """"""
    @property
    def IsCompleted(self) -> bool:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ListenerClientCertState(Enum):
    """"""

    NotInitialized: ListenerClientCertState = ...
    """"""
    InProgress: ListenerClientCertState = ...
    """"""
    Completed: ListenerClientCertState = ...
    """"""

class ListenerPrefixEnumerator(Object, IEnumerator[String], IEnumerator, IDisposable):
    """"""
    @property
    def Current(self) -> str:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def MoveNext(self) -> bool:
        """"""
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class Logging(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class NTAuthentication(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class NameInfoFlags(Enum):
    """"""

    NI_NOFQDN: NameInfoFlags = ...
    """"""
    NI_NUMERICHOST: NameInfoFlags = ...
    """"""
    NI_NAMEREQD: NameInfoFlags = ...
    """"""
    NI_NUMERICSERV: NameInfoFlags = ...
    """"""
    NI_DGRAM: NameInfoFlags = ...
    """"""

class NclConstants(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class NclUtilities(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class NegotiateClient(Object, IAuthenticationModule, ISessionAuthenticationModule):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def AuthenticationType(self) -> str:
        """"""
    @property
    def CanPreAuthenticate(self) -> bool:
        """"""
    @property
    def CanUseDefaultCredentials(self) -> bool:
        """"""
    def Authenticate(
        self, challenge: str, webRequest: WebRequest, credentials: ICredentials
    ) -> Authorization:
        """"""
    def ClearSession(self, webRequest: WebRequest) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def PreAuthenticate(self, webRequest: WebRequest, credentials: ICredentials) -> Authorization:
        """"""
    def ToString(self) -> str:
        """"""
    def Update(self, challenge: str, webRequest: WebRequest) -> bool:
        """"""

class NegotiationInfo(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class NegotiationInfoClass(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class NestedMultipleAsyncResult(LazyAsyncResult, IAsyncResult):
    """"""
    @property
    def AsyncState(self) -> object:
        """"""
    @property
    def AsyncWaitHandle(self) -> WaitHandle:
        """"""
    @property
    def CompletedSynchronously(self) -> bool:
        """"""
    @property
    def IsCompleted(self) -> bool:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class NestedSingleAsyncResult(LazyAsyncResult, IAsyncResult):
    """"""
    @property
    def AsyncState(self) -> object:
        """"""
    @property
    def AsyncWaitHandle(self) -> WaitHandle:
        """"""
    @property
    def CompletedSynchronously(self) -> bool:
        """"""
    @property
    def IsCompleted(self) -> bool:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class NetRes(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    @overload
    def GetWebStatusCodeString(cls, statusCode: FtpStatusCode, statusDescription: str) -> str:
        """"""
    @classmethod
    @overload
    def GetWebStatusCodeString(cls, statusCode: HttpStatusCode, statusDescription: str) -> str:
        """"""
    @classmethod
    @overload
    def GetWebStatusString(cls, Status: WebExceptionStatus) -> str:
        """"""
    @classmethod
    @overload
    def GetWebStatusString(cls, Res: str, Status: WebExceptionStatus) -> str:
        """"""
    def ToString(self) -> str:
        """"""

class NetWebProxyFinder(BaseWebProxyFinder, IWebProxyFinder, IDisposable):
    """"""
    def __init__(self, engine: AutoWebProxyScriptEngine) -> None:
        """"""
    @property
    def IsUnrecognizedScheme(self) -> bool:
        """"""
    @property
    def IsValid(self) -> bool:
        """"""
    def Abort(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetProxies(self, destination: Uri, proxyList: IList[str]) -> tuple[bool, IList[str]]:
        """"""
    def GetType(self) -> Type:
        """"""
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class NetworkAccess(Enum):
    """"""

    Connect: NetworkAccess = ...
    """"""
    Accept: NetworkAccess = ...
    """"""

class NetworkAddressChangePolled(Object, IDisposable):
    """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class NetworkCredential(Object, ICredentials, ICredentialsByHost):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, userName: str, password: str) -> None:
        """"""
    @overload
    def __init__(self, userName: str, password: SecureString) -> None:
        """"""
    @overload
    def __init__(self, userName: str, password: str, domain: str) -> None:
        """"""
    @overload
    def __init__(self, userName: str, password: SecureString, domain: str) -> None:
        """"""
    @property
    def Domain(self) -> str:
        """"""
    @Domain.setter
    def Domain(self, value: str) -> None: ...
    @property
    def Password(self) -> str:
        """"""
    @Password.setter
    def Password(self, value: str) -> None: ...
    @property
    def SecurePassword(self) -> SecureString:
        """"""
    @SecurePassword.setter
    def SecurePassword(self, value: SecureString) -> None: ...
    @property
    def UserName(self) -> str:
        """"""
    @UserName.setter
    def UserName(self, value: str) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetCredential(self, host: str, port: int, authenticationType: str) -> NetworkCredential:
        """"""
    @overload
    def GetCredential(self, uri: Uri, authType: str) -> NetworkCredential:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class NetworkingPerfCounterName(Enum):
    """"""

    SocketConnectionsEstablished: NetworkingPerfCounterName = ...
    """"""
    SocketBytesReceived: NetworkingPerfCounterName = ...
    """"""
    SocketBytesSent: NetworkingPerfCounterName = ...
    """"""
    SocketDatagramsReceived: NetworkingPerfCounterName = ...
    """"""
    SocketDatagramsSent: NetworkingPerfCounterName = ...
    """"""
    HttpWebRequestCreated: NetworkingPerfCounterName = ...
    """"""
    HttpWebRequestAvgLifeTime: NetworkingPerfCounterName = ...
    """"""
    HttpWebRequestAvgLifeTimeBase: NetworkingPerfCounterName = ...
    """"""
    HttpWebRequestQueued: NetworkingPerfCounterName = ...
    """"""
    HttpWebRequestAvgQueueTime: NetworkingPerfCounterName = ...
    """"""
    HttpWebRequestAvgQueueTimeBase: NetworkingPerfCounterName = ...
    """"""
    HttpWebRequestAborted: NetworkingPerfCounterName = ...
    """"""
    HttpWebRequestFailed: NetworkingPerfCounterName = ...
    """"""

class NetworkingPerfCounters(Object):
    """"""
    @property
    def Enabled(self) -> bool:
        """"""
    @classmethod
    @property
    def Instance(cls) -> NetworkingPerfCounters:
        """"""
    @overload
    def Decrement(self, perfCounter: NetworkingPerfCounterName) -> None:
        """"""
    @overload
    def Decrement(self, perfCounter: NetworkingPerfCounterName, amount: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @classmethod
    def GetTimestamp(cls) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def Increment(self, perfCounter: NetworkingPerfCounterName) -> None:
        """"""
    @overload
    def Increment(self, perfCounter: NetworkingPerfCounterName, amount: int) -> None:
        """"""
    def IncrementAverage(self, perfCounter: NetworkingPerfCounterName, startTimestamp: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class NtlmClient(Object, IAuthenticationModule, ISessionAuthenticationModule):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def AuthenticationType(self) -> str:
        """"""
    @property
    def CanPreAuthenticate(self) -> bool:
        """"""
    @property
    def CanUseDefaultCredentials(self) -> bool:
        """"""
    def Authenticate(
        self, challenge: str, webRequest: WebRequest, credentials: ICredentials
    ) -> Authorization:
        """"""
    def ClearSession(self, webRequest: WebRequest) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def PreAuthenticate(self, webRequest: WebRequest, credentials: ICredentials) -> Authorization:
        """"""
    def ToString(self) -> str:
        """"""
    def Update(self, challenge: str, webRequest: WebRequest) -> bool:
        """"""

class OpenReadCompletedEventArgs(AsyncCompletedEventArgs):
    """"""
    @property
    def Cancelled(self) -> bool:
        """"""
    @property
    def Error(self) -> Exception:
        """"""
    @property
    def Result(self) -> Stream:
        """"""
    @property
    def UserState(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

type OpenReadCompletedEventHandler = Callable[[object, OpenReadCompletedEventArgs], None]
""""""

class OpenWriteCompletedEventArgs(AsyncCompletedEventArgs):
    """"""
    @property
    def Cancelled(self) -> bool:
        """"""
    @property
    def Error(self) -> Exception:
        """"""
    @property
    def Result(self) -> Stream:
        """"""
    @property
    def UserState(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

type OpenWriteCompletedEventHandler = Callable[[object, OpenWriteCompletedEventArgs], None]
""""""

class PathList(Object):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def Item(self) -> object:
        """"""
    @Item.setter
    def Item(self, value: object) -> None: ...
    @property
    def SyncRoot(self) -> object:
        """"""
    @property
    def Values(self) -> ICollection:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetCookiesCount(self) -> int:
        """"""
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, s: str) -> object:
        """"""
    def __setitem__(self, s: str, value: object) -> None:
        """"""

class PolicyWrapper(Object):
    """"""
    def Accept(self, Certificate: X509Certificate, CertificateProblem: int) -> bool:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class PooledStream(Stream, IDisposable):
    """"""
    @property
    def CanRead(self) -> bool:
        """"""
    @property
    def CanSeek(self) -> bool:
        """"""
    @property
    def CanTimeout(self) -> bool:
        """"""
    @property
    def CanWrite(self) -> bool:
        """"""
    @property
    def Length(self) -> int:
        """"""
    @property
    def Position(self) -> int:
        """"""
    @Position.setter
    def Position(self, value: int) -> None: ...
    @property
    def ReadTimeout(self) -> int:
        """"""
    @ReadTimeout.setter
    def ReadTimeout(self, value: int) -> None: ...
    @property
    def WriteTimeout(self) -> int:
        """"""
    @WriteTimeout.setter
    def WriteTimeout(self, value: int) -> None: ...
    def BeginRead(
        self, buffer: Array[int], offset: int, size: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """"""
    def BeginWrite(
        self, buffer: Array[int], offset: int, size: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """"""
    @overload
    def Close(self) -> None:
        """"""
    @overload
    def Close(self, timeout: int) -> None:
        """"""
    @overload
    def CopyTo(self, destination: Stream) -> None:
        """"""
    @overload
    def CopyTo(self, destination: Stream, bufferSize: int) -> None:
        """"""
    @overload
    def CopyToAsync(self, destination: Stream) -> Task:
        """"""
    @overload
    def CopyToAsync(self, destination: Stream, bufferSize: int) -> Task:
        """"""
    @overload
    def CopyToAsync(
        self, destination: Stream, bufferSize: int, cancellationToken: CancellationToken
    ) -> Task:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    def Dispose(self) -> None:
        """"""
    def EndRead(self, asyncResult: IAsyncResult) -> int:
        """"""
    def EndWrite(self, asyncResult: IAsyncResult) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Flush(self) -> None:
        """"""
    @overload
    def FlushAsync(self) -> Task:
        """"""
    @overload
    def FlushAsync(self, cancellationToken: CancellationToken) -> Task:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetLifetimeService(self) -> object:
        """"""
    def GetType(self) -> Type:
        """"""
    def InitializeLifetimeService(self) -> object:
        """"""
    def Read(self, buffer: Array[int], offset: int, size: int) -> int:
        """"""
    @overload
    def ReadAsync(self, buffer: Array[int], offset: int, count: int) -> Task[int]:
        """"""
    @overload
    def ReadAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task[int]:
        """"""
    def ReadByte(self) -> int:
        """"""
    def Seek(self, offset: int, origin: SeekOrigin) -> int:
        """"""
    def SetLength(self, value: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def Write(self, buffer: Array[int], offset: int, size: int) -> None:
        """"""
    @overload
    def WriteAsync(self, buffer: Array[int], offset: int, count: int) -> Task:
        """"""
    @overload
    def WriteAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task:
        """"""
    def WriteByte(self, value: int) -> None:
        """"""

class PrefixLookup(Object):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, capacity: int) -> None:
        """"""
    def Add(self, prefix: str, value: object) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Lookup(self, lookupKey: str) -> object:
        """"""
    def ToString(self) -> str:
        """"""

class ProtocolViolationException(InvalidOperationException, _Exception, ISerializable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, message: str) -> None:
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
    def InnerException(self) -> Exception:
        """"""
    @property
    def Message(self) -> str:
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
    def GetObjectData(
        self, serializationInfo: SerializationInfo, streamingContext: StreamingContext
    ) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ProxyChain(ABC, Object, IEnumerable[Uri], IEnumerable, IDisposable):
    """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator[Uri]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def __iter__(self) -> Iterator[Uri]:
        """"""

class ProxyScriptChain(ProxyChain, IEnumerable[Uri], IEnumerable, IDisposable):
    """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator[Uri]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def __iter__(self) -> Iterator[Uri]:
        """"""

class ReadState(Enum):
    """"""

    Start: ReadState = ...
    """"""
    StatusLine: ReadState = ...
    """"""
    Headers: ReadState = ...
    """"""
    Data: ReadState = ...
    """"""

class ReceiveState(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class RegBlobWebProxyDataBuilder(WebProxyDataBuilder):
    """"""
    def __init__(self, connectoid: str, registry: SafeRegistryHandle) -> None:
        """"""
    def Build(self) -> WebProxyData:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ReadString(self) -> str:
        """"""
    def ToString(self) -> str:
        """"""

class RegistryConfiguration(ABC, Object):
    """"""
    @classmethod
    def AppConfigReadInt(cls, configVariable: str, defaultValue: int) -> int:
        """"""
    @classmethod
    def AppConfigReadString(cls, configVariable: str, defaultValue: str) -> str:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def GlobalConfigReadInt(cls, configVariable: str, defaultValue: int) -> int:
        """"""
    @classmethod
    def GlobalConfigReadString(cls, configVariable: str, defaultValue: str) -> str:
        """"""
    def ToString(self) -> str:
        """"""

class RequestContextBase(ABC, Object, IDisposable):
    """"""
    def Close(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class RequestLifetimeSetter(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ResponseDescription(Object):
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

class RtcState(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SSL_EXTRA_CERT_CHAIN_POLICY_PARA(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SSPIAuthType(Object, SSPIInterface):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def SecurityPackages(self) -> Array[SecurityPackageInfoClass]:
        """"""
    @SecurityPackages.setter
    def SecurityPackages(self, value: Array[SecurityPackageInfoClass]) -> None: ...
    @overload
    def AcceptSecurityContext(
        self,
        credential: SafeFreeCredentials,
        context: SafeDeleteContext,
        inputBuffer: SecurityBuffer,
        inFlags: ContextFlags,
        endianness: Endianness,
        outputBuffer: SecurityBuffer,
        outFlags: ContextFlags,
    ) -> int:
        """"""
    @overload
    def AcceptSecurityContext(
        self,
        credential: SafeFreeCredentials,
        context: SafeDeleteContext,
        inputBuffers: Array[SecurityBuffer],
        inFlags: ContextFlags,
        endianness: Endianness,
        outputBuffer: SecurityBuffer,
        outFlags: ContextFlags,
    ) -> int:
        """"""
    @overload
    def AcquireCredentialsHandle(
        self,
        moduleName: str,
        usage: CredentialUse,
        authdata: AuthIdentity,
        outCredential: SafeFreeCredentials,
    ) -> tuple[int, SafeFreeCredentials]:
        """"""
    @overload
    def AcquireCredentialsHandle(
        self,
        moduleName: str,
        usage: CredentialUse,
        authdata: SafeSspiAuthDataHandle,
        outCredential: SafeFreeCredentials,
    ) -> tuple[int, SafeFreeCredentials]:
        """"""
    @overload
    def AcquireCredentialsHandle(
        self,
        moduleName: str,
        usage: CredentialUse,
        authdata: SecureCredential,
        outCredential: SafeFreeCredentials,
    ) -> tuple[int, SafeFreeCredentials]:
        """"""
    @overload
    def AcquireCredentialsHandle(
        self,
        moduleName: str,
        usage: CredentialUse,
        authdata: SecureCredential2,
        outCredential: SafeFreeCredentials,
    ) -> tuple[int, SafeFreeCredentials]:
        """"""
    def AcquireDefaultCredential(
        self, moduleName: str, usage: CredentialUse, outCredential: SafeFreeCredentials
    ) -> tuple[int, SafeFreeCredentials]:
        """"""
    def ApplyControlToken(
        self, refContext: SafeDeleteContext, inputBuffers: Array[SecurityBuffer]
    ) -> int:
        """"""
    def CompleteAuthToken(
        self, refContext: SafeDeleteContext, inputBuffers: Array[SecurityBuffer]
    ) -> int:
        """"""
    def DecryptMessage(
        self, context: SafeDeleteContext, inputOutput: SecurityBufferDescriptor, sequenceNumber: int
    ) -> int:
        """"""
    def EncryptMessage(
        self, context: SafeDeleteContext, inputOutput: SecurityBufferDescriptor, sequenceNumber: int
    ) -> int:
        """"""
    def EnumerateSecurityPackages(
        self, pkgnum: Int32, pkgArray: SafeFreeContextBuffer
    ) -> tuple[int, Int32, SafeFreeContextBuffer]:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def InitializeSecurityContext(
        self,
        credential: SafeFreeCredentials,
        context: SafeDeleteContext,
        targetName: str,
        inFlags: ContextFlags,
        endianness: Endianness,
        inputBuffer: SecurityBuffer,
        outputBuffer: SecurityBuffer,
        outFlags: ContextFlags,
    ) -> int:
        """"""
    @overload
    def InitializeSecurityContext(
        self,
        credential: SafeFreeCredentials,
        context: SafeDeleteContext,
        targetName: str,
        inFlags: ContextFlags,
        endianness: Endianness,
        inputBuffers: Array[SecurityBuffer],
        outputBuffer: SecurityBuffer,
        outFlags: ContextFlags,
    ) -> int:
        """"""
    def MakeSignature(
        self, context: SafeDeleteContext, inputOutput: SecurityBufferDescriptor, sequenceNumber: int
    ) -> int:
        """"""
    def QueryContextAttributes(
        self,
        context: SafeDeleteContext,
        attribute: ContextAttribute,
        buffer: Array[int],
        handleType: Type,
        refHandle: SafeHandle,
    ) -> tuple[int, SafeHandle]:
        """"""
    def QueryContextChannelBinding(
        self,
        context: SafeDeleteContext,
        attribute: ContextAttribute,
        binding: SafeFreeContextBufferChannelBinding,
    ) -> tuple[int, SafeFreeContextBufferChannelBinding]:
        """"""
    def QuerySecurityContextToken(
        self, phContext: SafeDeleteContext, phToken: SafeCloseHandle
    ) -> tuple[int, SafeCloseHandle]:
        """"""
    def SetContextAttributes(
        self, context: SafeDeleteContext, attribute: ContextAttribute, buffer: Array[int]
    ) -> int:
        """"""
    def ToString(self) -> str:
        """"""
    def VerifySignature(
        self, context: SafeDeleteContext, inputOutput: SecurityBufferDescriptor, sequenceNumber: int
    ) -> int:
        """"""

class SSPIHandle(ValueType):
    """"""
    @property
    def IsZero(self) -> bool:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SSPIInterface(ABC):
    """"""
    @property
    def SecurityPackages(self) -> Array[SecurityPackageInfoClass]:
        """"""
    @SecurityPackages.setter
    def SecurityPackages(self, value: Array[SecurityPackageInfoClass]) -> None: ...
    @overload
    def AcceptSecurityContext(
        self,
        credential: SafeFreeCredentials,
        context: SafeDeleteContext,
        inputBuffer: SecurityBuffer,
        inFlags: ContextFlags,
        endianness: Endianness,
        outputBuffer: SecurityBuffer,
        outFlags: ContextFlags,
    ) -> int:
        """"""
    @overload
    def AcceptSecurityContext(
        self,
        credential: SafeFreeCredentials,
        context: SafeDeleteContext,
        inputBuffers: Array[SecurityBuffer],
        inFlags: ContextFlags,
        endianness: Endianness,
        outputBuffer: SecurityBuffer,
        outFlags: ContextFlags,
    ) -> int:
        """"""
    @overload
    def AcquireCredentialsHandle(
        self,
        moduleName: str,
        usage: CredentialUse,
        authdata: AuthIdentity,
        outCredential: SafeFreeCredentials,
    ) -> tuple[int, SafeFreeCredentials]:
        """"""
    @overload
    def AcquireCredentialsHandle(
        self,
        moduleName: str,
        usage: CredentialUse,
        authdata: SafeSspiAuthDataHandle,
        outCredential: SafeFreeCredentials,
    ) -> tuple[int, SafeFreeCredentials]:
        """"""
    @overload
    def AcquireCredentialsHandle(
        self,
        moduleName: str,
        usage: CredentialUse,
        authdata: SecureCredential,
        outCredential: SafeFreeCredentials,
    ) -> tuple[int, SafeFreeCredentials]:
        """"""
    @overload
    def AcquireCredentialsHandle(
        self,
        moduleName: str,
        usage: CredentialUse,
        authdata: SecureCredential2,
        outCredential: SafeFreeCredentials,
    ) -> tuple[int, SafeFreeCredentials]:
        """"""
    def AcquireDefaultCredential(
        self, moduleName: str, usage: CredentialUse, outCredential: SafeFreeCredentials
    ) -> tuple[int, SafeFreeCredentials]:
        """"""
    def ApplyControlToken(
        self, refContext: SafeDeleteContext, inputBuffers: Array[SecurityBuffer]
    ) -> int:
        """"""
    def CompleteAuthToken(
        self, refContext: SafeDeleteContext, inputBuffers: Array[SecurityBuffer]
    ) -> int:
        """"""
    def DecryptMessage(
        self, context: SafeDeleteContext, inputOutput: SecurityBufferDescriptor, sequenceNumber: int
    ) -> int:
        """"""
    def EncryptMessage(
        self, context: SafeDeleteContext, inputOutput: SecurityBufferDescriptor, sequenceNumber: int
    ) -> int:
        """"""
    def EnumerateSecurityPackages(
        self, pkgnum: Int32, pkgArray: SafeFreeContextBuffer
    ) -> tuple[int, Int32, SafeFreeContextBuffer]:
        """"""
    @overload
    def InitializeSecurityContext(
        self,
        credential: SafeFreeCredentials,
        context: SafeDeleteContext,
        targetName: str,
        inFlags: ContextFlags,
        endianness: Endianness,
        inputBuffer: SecurityBuffer,
        outputBuffer: SecurityBuffer,
        outFlags: ContextFlags,
    ) -> int:
        """"""
    @overload
    def InitializeSecurityContext(
        self,
        credential: SafeFreeCredentials,
        context: SafeDeleteContext,
        targetName: str,
        inFlags: ContextFlags,
        endianness: Endianness,
        inputBuffers: Array[SecurityBuffer],
        outputBuffer: SecurityBuffer,
        outFlags: ContextFlags,
    ) -> int:
        """"""
    def MakeSignature(
        self, context: SafeDeleteContext, inputOutput: SecurityBufferDescriptor, sequenceNumber: int
    ) -> int:
        """"""
    def QueryContextAttributes(
        self,
        phContext: SafeDeleteContext,
        attribute: ContextAttribute,
        buffer: Array[int],
        handleType: Type,
        refHandle: SafeHandle,
    ) -> tuple[int, SafeHandle]:
        """"""
    def QueryContextChannelBinding(
        self,
        phContext: SafeDeleteContext,
        attribute: ContextAttribute,
        refHandle: SafeFreeContextBufferChannelBinding,
    ) -> tuple[int, SafeFreeContextBufferChannelBinding]:
        """"""
    def QuerySecurityContextToken(
        self, phContext: SafeDeleteContext, phToken: SafeCloseHandle
    ) -> tuple[int, SafeCloseHandle]:
        """"""
    def SetContextAttributes(
        self, phContext: SafeDeleteContext, attribute: ContextAttribute, buffer: Array[int]
    ) -> int:
        """"""
    def VerifySignature(
        self, context: SafeDeleteContext, inputOutput: SecurityBufferDescriptor, sequenceNumber: int
    ) -> int:
        """"""

class SSPISecureChannelType(Object, SSPIInterface):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def SecurityPackages(self) -> Array[SecurityPackageInfoClass]:
        """"""
    @SecurityPackages.setter
    def SecurityPackages(self, value: Array[SecurityPackageInfoClass]) -> None: ...
    @overload
    def AcceptSecurityContext(
        self,
        credential: SafeFreeCredentials,
        context: SafeDeleteContext,
        inputBuffer: SecurityBuffer,
        inFlags: ContextFlags,
        endianness: Endianness,
        outputBuffer: SecurityBuffer,
        outFlags: ContextFlags,
    ) -> int:
        """"""
    @overload
    def AcceptSecurityContext(
        self,
        credential: SafeFreeCredentials,
        context: SafeDeleteContext,
        inputBuffers: Array[SecurityBuffer],
        inFlags: ContextFlags,
        endianness: Endianness,
        outputBuffer: SecurityBuffer,
        outFlags: ContextFlags,
    ) -> int:
        """"""
    @overload
    def AcquireCredentialsHandle(
        self,
        moduleName: str,
        usage: CredentialUse,
        authdata: AuthIdentity,
        outCredential: SafeFreeCredentials,
    ) -> tuple[int, SafeFreeCredentials]:
        """"""
    @overload
    def AcquireCredentialsHandle(
        self,
        moduleName: str,
        usage: CredentialUse,
        authdata: SafeSspiAuthDataHandle,
        outCredential: SafeFreeCredentials,
    ) -> tuple[int, SafeFreeCredentials]:
        """"""
    @overload
    def AcquireCredentialsHandle(
        self,
        moduleName: str,
        usage: CredentialUse,
        authdata: SecureCredential,
        outCredential: SafeFreeCredentials,
    ) -> tuple[int, SafeFreeCredentials]:
        """"""
    @overload
    def AcquireCredentialsHandle(
        self,
        moduleName: str,
        usage: CredentialUse,
        authdata: SecureCredential2,
        outCredential: SafeFreeCredentials,
    ) -> tuple[int, SafeFreeCredentials]:
        """"""
    def AcquireDefaultCredential(
        self, moduleName: str, usage: CredentialUse, outCredential: SafeFreeCredentials
    ) -> tuple[int, SafeFreeCredentials]:
        """"""
    def ApplyControlToken(
        self, refContext: SafeDeleteContext, inputBuffers: Array[SecurityBuffer]
    ) -> int:
        """"""
    def CompleteAuthToken(
        self, refContext: SafeDeleteContext, inputBuffers: Array[SecurityBuffer]
    ) -> int:
        """"""
    def DecryptMessage(
        self, context: SafeDeleteContext, inputOutput: SecurityBufferDescriptor, sequenceNumber: int
    ) -> int:
        """"""
    def EncryptMessage(
        self, context: SafeDeleteContext, inputOutput: SecurityBufferDescriptor, sequenceNumber: int
    ) -> int:
        """"""
    def EnumerateSecurityPackages(
        self, pkgnum: Int32, pkgArray: SafeFreeContextBuffer
    ) -> tuple[int, Int32, SafeFreeContextBuffer]:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def InitializeSecurityContext(
        self,
        credential: SafeFreeCredentials,
        context: SafeDeleteContext,
        targetName: str,
        inFlags: ContextFlags,
        endianness: Endianness,
        inputBuffer: SecurityBuffer,
        outputBuffer: SecurityBuffer,
        outFlags: ContextFlags,
    ) -> int:
        """"""
    @overload
    def InitializeSecurityContext(
        self,
        credential: SafeFreeCredentials,
        context: SafeDeleteContext,
        targetName: str,
        inFlags: ContextFlags,
        endianness: Endianness,
        inputBuffers: Array[SecurityBuffer],
        outputBuffer: SecurityBuffer,
        outFlags: ContextFlags,
    ) -> int:
        """"""
    def MakeSignature(
        self, context: SafeDeleteContext, inputOutput: SecurityBufferDescriptor, sequenceNumber: int
    ) -> int:
        """"""
    def QueryContextAttributes(
        self,
        phContext: SafeDeleteContext,
        attribute: ContextAttribute,
        buffer: Array[int],
        handleType: Type,
        refHandle: SafeHandle,
    ) -> tuple[int, SafeHandle]:
        """"""
    def QueryContextChannelBinding(
        self,
        phContext: SafeDeleteContext,
        attribute: ContextAttribute,
        refHandle: SafeFreeContextBufferChannelBinding,
    ) -> tuple[int, SafeFreeContextBufferChannelBinding]:
        """"""
    def QuerySecurityContextToken(
        self, phContext: SafeDeleteContext, phToken: SafeCloseHandle
    ) -> tuple[int, SafeCloseHandle]:
        """"""
    def SetContextAttributes(
        self, phContext: SafeDeleteContext, attribute: ContextAttribute, buffer: Array[int]
    ) -> int:
        """"""
    def ToString(self) -> str:
        """"""
    def VerifySignature(
        self, context: SafeDeleteContext, inputOutput: SecurityBufferDescriptor, sequenceNumber: int
    ) -> int:
        """"""

class SSPIWrapper(ABC, Object):
    """"""
    @classmethod
    @overload
    def AcquireCredentialsHandle(
        cls, SecModule: SSPIInterface, package: str, intent: CredentialUse, authdata: AuthIdentity
    ) -> SafeFreeCredentials:
        """"""
    @classmethod
    @overload
    def AcquireCredentialsHandle(
        cls,
        SecModule: SSPIInterface,
        package: str,
        intent: CredentialUse,
        authdata: SafeSspiAuthDataHandle,
    ) -> SafeFreeCredentials:
        """"""
    @classmethod
    @overload
    def AcquireCredentialsHandle(
        cls, SecModule: SSPIInterface, package: str, intent: CredentialUse, scc: SecureCredential
    ) -> SafeFreeCredentials:
        """"""
    @classmethod
    @overload
    def AcquireCredentialsHandle(
        cls, SecModule: SSPIInterface, package: str, intent: CredentialUse, scc: SecureCredential2
    ) -> SafeFreeCredentials:
        """"""
    @classmethod
    def AcquireDefaultCredential(
        cls, SecModule: SSPIInterface, package: str, intent: CredentialUse
    ) -> SafeFreeCredentials:
        """"""
    @classmethod
    def ApplyAlertToken(
        cls,
        secModule: SSPIInterface,
        credentialsHandle: SafeFreeCredentials,
        securityContext: SafeDeleteContext,
        alertType: TlsAlertType,
        alertMessage: TlsAlertMessage,
    ) -> int:
        """"""
    @classmethod
    def ApplyShutdownToken(
        cls,
        secModule: SSPIInterface,
        credentialsHandle: SafeFreeCredentials,
        securityContext: SafeDeleteContext,
    ) -> int:
        """"""
    @classmethod
    def DecryptMessage(
        cls,
        secModule: SSPIInterface,
        context: SafeDeleteContext,
        input: Array[SecurityBuffer],
        sequenceNumber: int,
    ) -> int:
        """"""
    @classmethod
    def EncryptMessage(
        cls,
        secModule: SSPIInterface,
        context: SafeDeleteContext,
        input: Array[SecurityBuffer],
        sequenceNumber: int,
    ) -> int:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def ErrorDescription(cls, errorCode: int) -> str:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    @overload
    def QueryContextAttributes(
        cls,
        SecModule: SSPIInterface,
        securityContext: SafeDeleteContext,
        contextAttribute: ContextAttribute,
    ) -> object:
        """"""
    @classmethod
    @overload
    def QueryContextAttributes(
        cls,
        SecModule: SSPIInterface,
        securityContext: SafeDeleteContext,
        contextAttribute: ContextAttribute,
        errorCode: Int32,
    ) -> tuple[object, Int32]:
        """"""
    @classmethod
    def QueryContextChannelBinding(
        cls,
        SecModule: SSPIInterface,
        securityContext: SafeDeleteContext,
        contextAttribute: ContextAttribute,
    ) -> SafeFreeContextBufferChannelBinding:
        """"""
    @classmethod
    def QuerySecurityContextToken(
        cls, SecModule: SSPIInterface, context: SafeDeleteContext, token: SafeCloseHandle
    ) -> tuple[int, SafeCloseHandle]:
        """"""
    @classmethod
    def SetContextAttributes(
        cls,
        SecModule: SSPIInterface,
        securityContext: SafeDeleteContext,
        contextAttribute: ContextAttribute,
        value: object,
    ) -> int:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def VerifySignature(
        cls,
        secModule: SSPIInterface,
        context: SafeDeleteContext,
        input: Array[SecurityBuffer],
        sequenceNumber: int,
    ) -> int:
        """"""

class SafeCertSelectCritera(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
    """"""
    @property
    def IsClosed(self) -> bool:
        """"""
    @property
    def IsInvalid(self) -> bool:
        """"""
    def Close(self) -> None:
        """"""
    def DangerousAddRef(self, success: Boolean) -> None:
        """"""
    def DangerousGetHandle(self) -> IntPtr:
        """"""
    def DangerousRelease(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def SetHandleAsInvalid(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class SafeCloseHandle(CriticalHandleZeroOrMinusOneIsInvalid, IDisposable):
    """"""
    @property
    def IsClosed(self) -> bool:
        """"""
    @property
    def IsInvalid(self) -> bool:
        """"""
    def Close(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def SetHandleAsInvalid(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class SafeCloseIcmpHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
    """"""
    @property
    def IsClosed(self) -> bool:
        """"""
    @property
    def IsInvalid(self) -> bool:
        """"""
    def Close(self) -> None:
        """"""
    def DangerousAddRef(self, success: Boolean) -> None:
        """"""
    def DangerousGetHandle(self) -> IntPtr:
        """"""
    def DangerousRelease(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def SetHandleAsInvalid(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class SafeCloseSocket(SafeHandleMinusOneIsInvalid, IDisposable):
    """"""
    @property
    def IsClosed(self) -> bool:
        """"""
    @property
    def IsInvalid(self) -> bool:
        """"""
    def Close(self) -> None:
        """"""
    def DangerousAddRef(self, success: Boolean) -> None:
        """"""
    def DangerousGetHandle(self) -> IntPtr:
        """"""
    def DangerousRelease(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def SetHandleAsInvalid(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class SafeCloseSocketAndEvent(SafeCloseSocket, IDisposable):
    """"""
    @property
    def IsClosed(self) -> bool:
        """"""
    @property
    def IsInvalid(self) -> bool:
        """"""
    def Close(self) -> None:
        """"""
    def DangerousAddRef(self, success: Boolean) -> None:
        """"""
    def DangerousGetHandle(self) -> IntPtr:
        """"""
    def DangerousRelease(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def SetHandleAsInvalid(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class SafeCredentialReference(CriticalHandleMinusOneIsInvalid, IDisposable):
    """"""
    @property
    def IsClosed(self) -> bool:
        """"""
    @property
    def IsInvalid(self) -> bool:
        """"""
    def Close(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def SetHandleAsInvalid(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class SafeDeleteContext(ABC, SafeHandle, IDisposable):
    """"""
    @property
    def IsClosed(self) -> bool:
        """"""
    @property
    def IsInvalid(self) -> bool:
        """"""
    def Close(self) -> None:
        """"""
    def DangerousAddRef(self, success: Boolean) -> None:
        """"""
    def DangerousGetHandle(self) -> IntPtr:
        """"""
    def DangerousRelease(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def SetHandleAsInvalid(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class SafeDeleteContext_SECURITY(SafeDeleteContext, IDisposable):
    """"""
    @property
    def IsClosed(self) -> bool:
        """"""
    @property
    def IsInvalid(self) -> bool:
        """"""
    def Close(self) -> None:
        """"""
    def DangerousAddRef(self, success: Boolean) -> None:
        """"""
    def DangerousGetHandle(self) -> IntPtr:
        """"""
    def DangerousRelease(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def SetHandleAsInvalid(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class SafeFreeAddrInfo(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
    """"""
    @property
    def IsClosed(self) -> bool:
        """"""
    @property
    def IsInvalid(self) -> bool:
        """"""
    def Close(self) -> None:
        """"""
    def DangerousAddRef(self, success: Boolean) -> None:
        """"""
    def DangerousGetHandle(self) -> IntPtr:
        """"""
    def DangerousRelease(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def SetHandleAsInvalid(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class SafeFreeCertChain(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
    """"""
    @property
    def IsClosed(self) -> bool:
        """"""
    @property
    def IsInvalid(self) -> bool:
        """"""
    def Close(self) -> None:
        """"""
    def DangerousAddRef(self, success: Boolean) -> None:
        """"""
    def DangerousGetHandle(self) -> IntPtr:
        """"""
    def DangerousRelease(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def SetHandleAsInvalid(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class SafeFreeCertChainList(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
    """"""
    @property
    def IsClosed(self) -> bool:
        """"""
    @property
    def IsInvalid(self) -> bool:
        """"""
    def Close(self) -> None:
        """"""
    def DangerousAddRef(self, success: Boolean) -> None:
        """"""
    def DangerousGetHandle(self) -> IntPtr:
        """"""
    def DangerousRelease(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def SetHandleAsInvalid(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class SafeFreeCertContext(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
    """"""
    @property
    def IsClosed(self) -> bool:
        """"""
    @property
    def IsInvalid(self) -> bool:
        """"""
    def Close(self) -> None:
        """"""
    def DangerousAddRef(self, success: Boolean) -> None:
        """"""
    def DangerousGetHandle(self) -> IntPtr:
        """"""
    def DangerousRelease(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def SetHandleAsInvalid(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class SafeFreeContextBuffer(ABC, SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
    """"""
    @property
    def IsClosed(self) -> bool:
        """"""
    @property
    def IsInvalid(self) -> bool:
        """"""
    def Close(self) -> None:
        """"""
    def DangerousAddRef(self, success: Boolean) -> None:
        """"""
    def DangerousGetHandle(self) -> IntPtr:
        """"""
    def DangerousRelease(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def QueryContextAttributes(
        cls,
        dll: SecurDll,
        phContext: SafeDeleteContext,
        contextAttribute: ContextAttribute,
        buffer: int,
        refHandle: SafeHandle,
    ) -> int:
        """"""
    @classmethod
    def SetContextAttributes(
        cls,
        dll: SecurDll,
        phContext: SafeDeleteContext,
        contextAttribute: ContextAttribute,
        buffer: Array[int],
    ) -> int:
        """"""
    def SetHandleAsInvalid(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class SafeFreeContextBufferChannelBinding(ABC, ChannelBinding, IDisposable):
    """"""
    @property
    def IsClosed(self) -> bool:
        """"""
    @property
    def IsInvalid(self) -> bool:
        """"""
    @property
    def Size(self) -> int:
        """"""
    def Close(self) -> None:
        """"""
    def DangerousAddRef(self, success: Boolean) -> None:
        """"""
    def DangerousGetHandle(self) -> IntPtr:
        """"""
    def DangerousRelease(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def QueryContextChannelBinding(
        cls,
        dll: SecurDll,
        phContext: SafeDeleteContext,
        contextAttribute: ContextAttribute,
        buffer: Bindings,
        refHandle: SafeFreeContextBufferChannelBinding,
    ) -> int:
        """"""
    def SetHandleAsInvalid(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class SafeFreeContextBufferChannelBinding_SECURITY(
    SafeFreeContextBufferChannelBinding, IDisposable
):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def IsClosed(self) -> bool:
        """"""
    @property
    def IsInvalid(self) -> bool:
        """"""
    @property
    def Size(self) -> int:
        """"""
    def Close(self) -> None:
        """"""
    def DangerousAddRef(self, success: Boolean) -> None:
        """"""
    def DangerousGetHandle(self) -> IntPtr:
        """"""
    def DangerousRelease(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def SetHandleAsInvalid(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class SafeFreeContextBuffer_SECURITY(SafeFreeContextBuffer, IDisposable):
    """"""
    @property
    def IsClosed(self) -> bool:
        """"""
    @property
    def IsInvalid(self) -> bool:
        """"""
    def Close(self) -> None:
        """"""
    def DangerousAddRef(self, success: Boolean) -> None:
        """"""
    def DangerousGetHandle(self) -> IntPtr:
        """"""
    def DangerousRelease(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def SetHandleAsInvalid(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class SafeFreeCredential_SECURITY(SafeFreeCredentials, IDisposable):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def IsClosed(self) -> bool:
        """"""
    @property
    def IsInvalid(self) -> bool:
        """"""
    def Close(self) -> None:
        """"""
    def DangerousAddRef(self, success: Boolean) -> None:
        """"""
    def DangerousGetHandle(self) -> IntPtr:
        """"""
    def DangerousRelease(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def SetHandleAsInvalid(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class SafeFreeCredentials(ABC, SafeHandle, IDisposable):
    """"""
    @property
    def IsClosed(self) -> bool:
        """"""
    @property
    def IsInvalid(self) -> bool:
        """"""
    @classmethod
    @overload
    def AcquireCredentialsHandle(
        cls,
        dll: SecurDll,
        package: str,
        intent: CredentialUse,
        authdata: AuthIdentity,
        outCredential: SafeFreeCredentials,
    ) -> tuple[int, SafeFreeCredentials]:
        """"""
    @classmethod
    @overload
    def AcquireCredentialsHandle(
        cls,
        dll: SecurDll,
        package: str,
        intent: CredentialUse,
        authdata: SecureCredential,
        outCredential: SafeFreeCredentials,
    ) -> tuple[int, SafeFreeCredentials]:
        """"""
    @classmethod
    @overload
    def AcquireCredentialsHandle(
        cls,
        dll: SecurDll,
        package: str,
        intent: CredentialUse,
        authdata: SecureCredential2,
        outCredential: SafeFreeCredentials,
    ) -> tuple[int, SafeFreeCredentials]:
        """"""
    @classmethod
    @overload
    def AcquireCredentialsHandle(
        cls,
        package: str,
        intent: CredentialUse,
        authdata: SafeSspiAuthDataHandle,
        outCredential: SafeFreeCredentials,
    ) -> tuple[int, SafeFreeCredentials]:
        """"""
    @classmethod
    def AcquireDefaultCredential(
        cls, dll: SecurDll, package: str, intent: CredentialUse, outCredential: SafeFreeCredentials
    ) -> tuple[int, SafeFreeCredentials]:
        """"""
    def Close(self) -> None:
        """"""
    def DangerousAddRef(self, success: Boolean) -> None:
        """"""
    def DangerousGetHandle(self) -> IntPtr:
        """"""
    def DangerousRelease(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def SetHandleAsInvalid(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class SafeGlobalFree(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
    """"""
    @property
    def IsClosed(self) -> bool:
        """"""
    @property
    def IsInvalid(self) -> bool:
        """"""
    def Close(self) -> None:
        """"""
    def DangerousAddRef(self, success: Boolean) -> None:
        """"""
    def DangerousGetHandle(self) -> IntPtr:
        """"""
    def DangerousRelease(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def SetHandleAsInvalid(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class SafeInternetHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def IsClosed(self) -> bool:
        """"""
    @property
    def IsInvalid(self) -> bool:
        """"""
    def Close(self) -> None:
        """"""
    def DangerousAddRef(self, success: Boolean) -> None:
        """"""
    def DangerousGetHandle(self) -> IntPtr:
        """"""
    def DangerousRelease(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def SetHandleAsInvalid(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class SafeLoadLibrary(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
    """"""

    Zero: ClassVar[SafeLoadLibrary]
    """"""
    @property
    def IsClosed(self) -> bool:
        """"""
    @property
    def IsInvalid(self) -> bool:
        """"""
    def Close(self) -> None:
        """"""
    def DangerousAddRef(self, success: Boolean) -> None:
        """"""
    def DangerousGetHandle(self) -> IntPtr:
        """"""
    def DangerousRelease(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def HasFunction(self, functionName: str) -> bool:
        """"""
    @classmethod
    def LoadLibraryEx(cls, library: str) -> SafeLoadLibrary:
        """"""
    def SetHandleAsInvalid(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class SafeLocalFree(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
    """"""

    Zero: ClassVar[SafeLocalFree]
    """"""
    @property
    def IsClosed(self) -> bool:
        """"""
    @property
    def IsInvalid(self) -> bool:
        """"""
    def Close(self) -> None:
        """"""
    def DangerousAddRef(self, success: Boolean) -> None:
        """"""
    def DangerousGetHandle(self) -> IntPtr:
        """"""
    def DangerousRelease(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def LocalAlloc(cls, cb: int) -> SafeLocalFree:
        """"""
    def SetHandleAsInvalid(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class SafeLocalFreeChannelBinding(ChannelBinding, IDisposable):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def IsClosed(self) -> bool:
        """"""
    @property
    def IsInvalid(self) -> bool:
        """"""
    @property
    def Size(self) -> int:
        """"""
    def Close(self) -> None:
        """"""
    def DangerousAddRef(self, success: Boolean) -> None:
        """"""
    def DangerousGetHandle(self) -> IntPtr:
        """"""
    def DangerousRelease(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def LocalAlloc(cls, cb: int) -> SafeLocalFreeChannelBinding:
        """"""
    def SetHandleAsInvalid(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class SafeNativeOverlapped(SafeHandle, IDisposable):
    """"""
    @property
    def IsClosed(self) -> bool:
        """"""
    @property
    def IsInvalid(self) -> bool:
        """"""
    def Close(self) -> None:
        """"""
    def DangerousAddRef(self, success: Boolean) -> None:
        """"""
    def DangerousGetHandle(self) -> IntPtr:
        """"""
    def DangerousRelease(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ReinitializeNativeOverlapped(self) -> None:
        """"""
    def SetHandleAsInvalid(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class SafeNclNativeMethods(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SafeOverlappedFree(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
    """"""
    @property
    def IsClosed(self) -> bool:
        """"""
    @property
    def IsInvalid(self) -> bool:
        """"""
    @classmethod
    @overload
    def Alloc(cls) -> SafeOverlappedFree:
        """"""
    @classmethod
    @overload
    def Alloc(cls, socketHandle: SafeCloseSocket) -> SafeOverlappedFree:
        """"""
    @overload
    def Close(self) -> None:
        """"""
    @overload
    def Close(self, resetOwner: bool) -> None:
        """"""
    def DangerousAddRef(self, success: Boolean) -> None:
        """"""
    def DangerousGetHandle(self) -> IntPtr:
        """"""
    def DangerousRelease(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def SetHandleAsInvalid(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class SafeRegistryHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
    """"""
    @property
    def IsClosed(self) -> bool:
        """"""
    @property
    def IsInvalid(self) -> bool:
        """"""
    def Close(self) -> None:
        """"""
    def DangerousAddRef(self, success: Boolean) -> None:
        """"""
    def DangerousGetHandle(self) -> IntPtr:
        """"""
    def DangerousRelease(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def SetHandleAsInvalid(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class SafeSspiAuthDataHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def IsClosed(self) -> bool:
        """"""
    @property
    def IsInvalid(self) -> bool:
        """"""
    def Close(self) -> None:
        """"""
    def DangerousAddRef(self, success: Boolean) -> None:
        """"""
    def DangerousGetHandle(self) -> IntPtr:
        """"""
    def DangerousRelease(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def SetHandleAsInvalid(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class SafeUnlockUrlCacheEntryFile(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
    """"""
    @property
    def IsClosed(self) -> bool:
        """"""
    @property
    def IsInvalid(self) -> bool:
        """"""
    def Close(self) -> None:
        """"""
    def DangerousAddRef(self, success: Boolean) -> None:
        """"""
    def DangerousGetHandle(self) -> IntPtr:
        """"""
    def DangerousRelease(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def SetHandleAsInvalid(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class SafeWebSocketHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
    """"""
    @property
    def IsClosed(self) -> bool:
        """"""
    @property
    def IsInvalid(self) -> bool:
        """"""
    def Close(self) -> None:
        """"""
    def DangerousAddRef(self, success: Boolean) -> None:
        """"""
    def DangerousGetHandle(self) -> IntPtr:
        """"""
    def DangerousRelease(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def SetHandleAsInvalid(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class ScatterGatherBuffers(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SchProtocols(Enum):
    """"""

    Zero: SchProtocols = ...
    """"""
    PctServer: SchProtocols = ...
    """"""
    PctClient: SchProtocols = ...
    """"""
    Pct: SchProtocols = ...
    """"""
    Ssl2Server: SchProtocols = ...
    """"""
    Ssl2Client: SchProtocols = ...
    """"""
    Ssl2: SchProtocols = ...
    """"""
    Ssl3Server: SchProtocols = ...
    """"""
    Ssl3Client: SchProtocols = ...
    """"""
    Ssl3: SchProtocols = ...
    """"""
    Tls10Server: SchProtocols = ...
    """"""
    Tls10Client: SchProtocols = ...
    """"""
    Tls10: SchProtocols = ...
    """"""
    Ssl3Tls: SchProtocols = ...
    """"""
    Tls11Server: SchProtocols = ...
    """"""
    Tls11Client: SchProtocols = ...
    """"""
    Tls11: SchProtocols = ...
    """"""
    Tls12Server: SchProtocols = ...
    """"""
    Tls12Client: SchProtocols = ...
    """"""
    Tls12: SchProtocols = ...
    """"""
    Tls13Server: SchProtocols = ...
    """"""
    Tls13Client: SchProtocols = ...
    """"""
    Tls13: SchProtocols = ...
    """"""
    UniServer: SchProtocols = ...
    """"""
    ServerMask: SchProtocols = ...
    """"""
    UniClient: SchProtocols = ...
    """"""
    ClientMask: SchProtocols = ...
    """"""
    Unified: SchProtocols = ...
    """"""

class SecChannelBindings(Object):
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

class SecSizes(Object):
    """"""

    BlockSize: Final[int]
    """"""
    MaxSignature: Final[int]
    """"""
    MaxToken: Final[int]
    """"""
    SecurityTrailer: Final[int]
    """"""
    SizeOf: ClassVar[int]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SecurDll(Enum):
    """"""

    SECURITY: SecurDll = ...
    """"""
    SECUR32: SecurDll = ...
    """"""
    SCHANNEL: SecurDll = ...
    """"""

class SecureCredential(ValueType):
    """"""

    CurrentVersion: ClassVar[int]
    """"""
    cCreds: Final[int]
    """"""
    cMappers: Final[int]
    """"""
    cSupportedAlgs: Final[int]
    """"""
    certContextArray: Final[IntPtr]
    """"""
    dwFlags: Final[SecureCredential.Flags]
    """"""
    dwMaximumCipherStrength: Final[int]
    """"""
    dwMinimumCipherStrength: Final[int]
    """"""
    dwSessionLifespan: Final[int]
    """"""
    grbitEnabledProtocols: Final[SchProtocols]
    """"""
    reserved: Final[int]
    """"""
    version: Final[int]
    """"""
    def __init__(
        self,
        version: int,
        certificate: X509Certificate,
        flags: SecureCredential.Flags,
        protocols: SchProtocols,
        policy: EncryptionPolicy,
    ) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    class Flags(Enum):
        """"""

        Zero: SecureCredential.Flags = ...
        """"""
        NoSystemMapper: SecureCredential.Flags = ...
        """"""
        NoNameCheck: SecureCredential.Flags = ...
        """"""
        ValidateManual: SecureCredential.Flags = ...
        """"""
        NoDefaultCred: SecureCredential.Flags = ...
        """"""
        ValidateAuto: SecureCredential.Flags = ...
        """"""
        SendAuxRecord: SecureCredential.Flags = ...
        """"""
        UseStrongCrypto: SecureCredential.Flags = ...
        """"""

class SecureCredential2(ValueType):
    """"""

    CurrentVersion: ClassVar[int]
    """"""
    cCreds: Final[int]
    """"""
    cMappers: Final[int]
    """"""
    cTlsParameters: Final[int]
    """"""
    certContextArray: Final[None]
    """"""
    dwCredformat: Final[int]
    """"""
    dwFlags: Final[SecureCredential2.Flags]
    """"""
    dwSessionLifespan: Final[int]
    """"""
    pTlsParameters: Final[TlsParamaters]
    """"""
    version: Final[int]
    """"""
    def __init__(
        self, flags: SecureCredential2.Flags, protocols: SchProtocols, policy: EncryptionPolicy
    ) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    class Flags(Enum):
        """"""

        Zero: SecureCredential2.Flags = ...
        """"""
        NoSystemMapper: SecureCredential2.Flags = ...
        """"""
        NoNameCheck: SecureCredential2.Flags = ...
        """"""
        ValidateManual: SecureCredential2.Flags = ...
        """"""
        NoDefaultCred: SecureCredential2.Flags = ...
        """"""
        ValidateAuto: SecureCredential2.Flags = ...
        """"""
        SendAuxRecord: SecureCredential2.Flags = ...
        """"""
        UseStrongCrypto: SecureCredential2.Flags = ...
        """"""
        UsePresharedKeyOnly: SecureCredential2.Flags = ...
        """"""
        AllowNullEencryption: SecureCredential2.Flags = ...
        """"""

class SecurityBuffer(Object):
    """"""

    offset: Final[int]
    """"""
    size: Final[int]
    """"""
    token: Final[Array[int]]
    """"""
    type: Final[BufferType]
    """"""
    unmanagedToken: Final[SafeHandle]
    """"""
    @overload
    def __init__(self, data: Array[int], offset: int, size: int, tokentype: BufferType) -> None:
        """"""
    @overload
    def __init__(self, data: Array[int], tokentype: BufferType) -> None:
        """"""
    @overload
    def __init__(self, size: int, tokentype: BufferType) -> None:
        """"""
    @overload
    def __init__(self, binding: ChannelBinding) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SecurityBufferDescriptor(Object):
    """"""

    Count: Final[int]
    """"""
    UnmanagedPointer: Final[None]
    """"""
    Version: Final[int]
    """"""
    def __init__(self, count: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SecurityBufferStruct(ValueType):
    """"""

    Size: ClassVar[int]
    """"""
    count: Final[int]
    """"""
    token: Final[IntPtr]
    """"""
    type: Final[BufferType]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SecurityPackageInfo(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SecurityPackageInfoClass(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SecurityProtocolType(Enum):
    """"""

    SystemDefault: SecurityProtocolType = ...
    """"""
    Ssl3: SecurityProtocolType = ...
    """"""
    Tls: SecurityProtocolType = ...
    """"""
    Tls11: SecurityProtocolType = ...
    """"""
    Tls12: SecurityProtocolType = ...
    """"""
    Tls13: SecurityProtocolType = ...
    """"""

class SecurityStatus(Enum):
    """"""

    OK: SecurityStatus = ...
    """"""
    ContinueNeeded: SecurityStatus = ...
    """"""
    CompleteNeeded: SecurityStatus = ...
    """"""
    CompAndContinue: SecurityStatus = ...
    """"""
    ContextExpired: SecurityStatus = ...
    """"""
    CredentialsNeeded: SecurityStatus = ...
    """"""
    Renegotiate: SecurityStatus = ...
    """"""
    OutOfMemory: SecurityStatus = ...
    """"""
    InvalidHandle: SecurityStatus = ...
    """"""
    Unsupported: SecurityStatus = ...
    """"""
    TargetUnknown: SecurityStatus = ...
    """"""
    InternalError: SecurityStatus = ...
    """"""
    PackageNotFound: SecurityStatus = ...
    """"""
    NotOwner: SecurityStatus = ...
    """"""
    CannotInstall: SecurityStatus = ...
    """"""
    InvalidToken: SecurityStatus = ...
    """"""
    CannotPack: SecurityStatus = ...
    """"""
    QopNotSupported: SecurityStatus = ...
    """"""
    NoImpersonation: SecurityStatus = ...
    """"""
    LogonDenied: SecurityStatus = ...
    """"""
    UnknownCredentials: SecurityStatus = ...
    """"""
    NoCredentials: SecurityStatus = ...
    """"""
    MessageAltered: SecurityStatus = ...
    """"""
    OutOfSequence: SecurityStatus = ...
    """"""
    NoAuthenticatingAuthority: SecurityStatus = ...
    """"""
    IncompleteMessage: SecurityStatus = ...
    """"""
    IncompleteCredentials: SecurityStatus = ...
    """"""
    BufferNotEnough: SecurityStatus = ...
    """"""
    WrongPrincipal: SecurityStatus = ...
    """"""
    TimeSkew: SecurityStatus = ...
    """"""
    UntrustedRoot: SecurityStatus = ...
    """"""
    IllegalMessage: SecurityStatus = ...
    """"""
    CertUnknown: SecurityStatus = ...
    """"""
    CertExpired: SecurityStatus = ...
    """"""
    AlgorithmMismatch: SecurityStatus = ...
    """"""
    SecurityQosFailed: SecurityStatus = ...
    """"""
    SmartcardLogonRequired: SecurityStatus = ...
    """"""
    UnsupportedPreauth: SecurityStatus = ...
    """"""
    BadBinding: SecurityStatus = ...
    """"""

class Semaphore(WaitHandle, IDisposable):
    """"""
    @property
    def Handle(self) -> IntPtr:
        """"""
    @Handle.setter
    def Handle(self, value: IntPtr) -> None: ...
    @property
    def SafeWaitHandle(self) -> SafeWaitHandle:
        """"""
    @SafeWaitHandle.setter
    def SafeWaitHandle(self, value: SafeWaitHandle) -> None: ...
    def Close(self) -> None:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetLifetimeService(self) -> object:
        """"""
    def GetType(self) -> Type:
        """"""
    def InitializeLifetimeService(self) -> object:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def WaitOne(self) -> bool:
        """"""
    @overload
    def WaitOne(self, millisecondsTimeout: int) -> bool:
        """"""
    @overload
    def WaitOne(self, millisecondsTimeout: int, exitContext: bool) -> bool:
        """"""
    @overload
    def WaitOne(self, timeout: TimeSpan) -> bool:
        """"""
    @overload
    def WaitOne(self, timeout: TimeSpan, exitContext: bool) -> bool:
        """"""

class ServerCertValidationCallback(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ServiceNameStore(Object):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def ServiceNames(self) -> ServiceNameCollection:
        """"""
    def Add(self, uriPrefix: str) -> bool:
        """"""
    def BuildServiceNames(self, uriPrefix: str) -> Array[str]:
        """"""
    def BuildSimpleServiceName(self, uriPrefix: str) -> str:
        """"""
    def Clear(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Remove(self, uriPrefix: str) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    def __delitem__(self, uriPrefix: str) -> bool:
        """"""

class ServicePoint(Object):
    """"""
    @property
    def Address(self) -> Uri:
        """"""
    @property
    def BindIPEndPointDelegate(self) -> BindIPEndPoint:
        """"""
    @BindIPEndPointDelegate.setter
    def BindIPEndPointDelegate(self, value: BindIPEndPoint) -> None: ...
    @property
    def Certificate(self) -> X509Certificate:
        """"""
    @property
    def ClientCertificate(self) -> X509Certificate:
        """"""
    @property
    def ConnectionLeaseTimeout(self) -> int:
        """"""
    @ConnectionLeaseTimeout.setter
    def ConnectionLeaseTimeout(self, value: int) -> None: ...
    @property
    def ConnectionLimit(self) -> int:
        """"""
    @ConnectionLimit.setter
    def ConnectionLimit(self, value: int) -> None: ...
    @property
    def ConnectionName(self) -> str:
        """"""
    @property
    def CurrentConnections(self) -> int:
        """"""
    @property
    def Expect100Continue(self) -> bool:
        """"""
    @Expect100Continue.setter
    def Expect100Continue(self, value: bool) -> None: ...
    @property
    def IdleSince(self) -> DateTime:
        """"""
    @property
    def MaxIdleTime(self) -> int:
        """"""
    @MaxIdleTime.setter
    def MaxIdleTime(self, value: int) -> None: ...
    @property
    def ProtocolVersion(self) -> Version:
        """"""
    @property
    def ReceiveBufferSize(self) -> int:
        """"""
    @ReceiveBufferSize.setter
    def ReceiveBufferSize(self, value: int) -> None: ...
    @property
    def SupportsPipelining(self) -> bool:
        """"""
    @property
    def UseNagleAlgorithm(self) -> bool:
        """"""
    @UseNagleAlgorithm.setter
    def UseNagleAlgorithm(self, value: bool) -> None: ...
    def CloseConnectionGroup(self, connectionGroupName: str) -> bool:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def SetTcpKeepAlive(self, enabled: bool, keepAliveTime: int, keepAliveInterval: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class ServicePointManager(Object):
    """"""

    DefaultNonPersistentConnectionLimit: ClassVar[int]
    """"""
    DefaultPersistentConnectionLimit: ClassVar[int]
    """"""
    @classmethod
    @property
    def CertificatePolicy(cls) -> ICertificatePolicy:
        """"""
    @classmethod
    @CertificatePolicy.setter
    def CertificatePolicy(cls, value: ICertificatePolicy) -> None: ...
    @classmethod
    @property
    def CheckCertificateRevocationList(cls) -> bool:
        """"""
    @classmethod
    @CheckCertificateRevocationList.setter
    def CheckCertificateRevocationList(cls, value: bool) -> None: ...
    @classmethod
    @property
    def DefaultConnectionLimit(cls) -> int:
        """"""
    @classmethod
    @DefaultConnectionLimit.setter
    def DefaultConnectionLimit(cls, value: int) -> None: ...
    @classmethod
    @property
    def DnsRefreshTimeout(cls) -> int:
        """"""
    @classmethod
    @DnsRefreshTimeout.setter
    def DnsRefreshTimeout(cls, value: int) -> None: ...
    @classmethod
    @property
    def EnableDnsRoundRobin(cls) -> bool:
        """"""
    @classmethod
    @EnableDnsRoundRobin.setter
    def EnableDnsRoundRobin(cls, value: bool) -> None: ...
    @classmethod
    @property
    def EncryptionPolicy(cls) -> EncryptionPolicy:
        """"""
    @classmethod
    @property
    def Expect100Continue(cls) -> bool:
        """"""
    @classmethod
    @Expect100Continue.setter
    def Expect100Continue(cls, value: bool) -> None: ...
    @classmethod
    @property
    def MaxServicePointIdleTime(cls) -> int:
        """"""
    @classmethod
    @MaxServicePointIdleTime.setter
    def MaxServicePointIdleTime(cls, value: int) -> None: ...
    @classmethod
    @property
    def MaxServicePoints(cls) -> int:
        """"""
    @classmethod
    @MaxServicePoints.setter
    def MaxServicePoints(cls, value: int) -> None: ...
    @classmethod
    @property
    def ReusePort(cls) -> bool:
        """"""
    @classmethod
    @ReusePort.setter
    def ReusePort(cls, value: bool) -> None: ...
    @classmethod
    @property
    def SecurityProtocol(cls) -> SecurityProtocolType:
        """"""
    @classmethod
    @SecurityProtocol.setter
    def SecurityProtocol(cls, value: SecurityProtocolType) -> None: ...
    @classmethod
    @property
    def ServerCertificateValidationCallback(cls) -> RemoteCertificateValidationCallback:
        """"""
    @classmethod
    @ServerCertificateValidationCallback.setter
    def ServerCertificateValidationCallback(
        cls, value: RemoteCertificateValidationCallback
    ) -> None: ...
    @classmethod
    @property
    def UseNagleAlgorithm(cls) -> bool:
        """"""
    @classmethod
    @UseNagleAlgorithm.setter
    def UseNagleAlgorithm(cls, value: bool) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    @overload
    def FindServicePoint(cls, uriString: str, proxy: IWebProxy) -> ServicePoint:
        """"""
    @classmethod
    @overload
    def FindServicePoint(cls, address: Uri) -> ServicePoint:
        """"""
    @classmethod
    @overload
    def FindServicePoint(cls, address: Uri, proxy: IWebProxy) -> ServicePoint:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def SetTcpKeepAlive(cls, enabled: bool, keepAliveTime: int, keepAliveInterval: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class ShellExpression(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SocketAddress(Object):
    """"""
    @overload
    def __init__(self, family: AddressFamily) -> None:
        """"""
    @overload
    def __init__(self, family: AddressFamily, size: int) -> None:
        """"""
    @property
    def Family(self) -> AddressFamily:
        """"""
    @property
    def Item(self) -> int:
        """"""
    @Item.setter
    def Item(self, value: int) -> None: ...
    @property
    def Size(self) -> int:
        """"""
    def Equals(self, comparand: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def __getitem__(self, offset: int) -> int:
        """"""
    def __setitem__(self, offset: int, value: int) -> None:
        """"""

class SocketConstructorFlags(Enum):
    """"""

    WSA_FLAG_OVERLAPPED: SocketConstructorFlags = ...
    """"""
    WSA_FLAG_MULTIPOINT_C_ROOT: SocketConstructorFlags = ...
    """"""
    WSA_FLAG_MULTIPOINT_C_LEAF: SocketConstructorFlags = ...
    """"""
    WSA_FLAG_MULTIPOINT_D_ROOT: SocketConstructorFlags = ...
    """"""
    WSA_FLAG_MULTIPOINT_D_LEAF: SocketConstructorFlags = ...
    """"""

class SocketPermission(
    CodeAccessPermission, IUnrestrictedPermission, IPermission, ISecurityEncodable, IStackWalk
):
    """"""

    AllPorts: ClassVar[int]
    """"""
    @overload
    def __init__(self, state: PermissionState) -> None:
        """"""
    @overload
    def __init__(
        self, access: NetworkAccess, transport: TransportType, hostName: str, portNumber: int
    ) -> None:
        """"""
    @property
    def AcceptList(self) -> IEnumerator:
        """"""
    @property
    def ConnectList(self) -> IEnumerator:
        """"""
    def AddPermission(
        self, access: NetworkAccess, transport: TransportType, hostName: str, portNumber: int
    ) -> None:
        """"""
    def Assert(self) -> None:
        """"""
    def Copy(self) -> IPermission:
        """"""
    def Demand(self) -> None:
        """"""
    def Deny(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def FromXml(self, securityElement: SecurityElement) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Intersect(self, target: IPermission) -> IPermission:
        """"""
    def IsSubsetOf(self, target: IPermission) -> bool:
        """"""
    def IsUnrestricted(self) -> bool:
        """"""
    def PermitOnly(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def ToXml(self) -> SecurityElement:
        """"""
    def Union(self, target: IPermission) -> IPermission:
        """"""

class SocketPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    """"""
    def __init__(self, action: SecurityAction) -> None:
        """"""
    @property
    def Access(self) -> str:
        """"""
    @Access.setter
    def Access(self, value: str) -> None: ...
    @property
    def Action(self) -> SecurityAction:
        """"""
    @Action.setter
    def Action(self, value: SecurityAction) -> None: ...
    @property
    def Host(self) -> str:
        """"""
    @Host.setter
    def Host(self, value: str) -> None: ...
    @property
    def Port(self) -> str:
        """"""
    @Port.setter
    def Port(self, value: str) -> None: ...
    @property
    def Transport(self) -> str:
        """"""
    @Transport.setter
    def Transport(self, value: str) -> None: ...
    @property
    def TypeId(self) -> object:
        """"""
    @property
    def Unrestricted(self) -> bool:
        """"""
    @Unrestricted.setter
    def Unrestricted(self, value: bool) -> None: ...
    def CreatePermission(self) -> IPermission:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """"""
    def GetTypeInfoCount(self, pcTInfo: UInt32) -> tuple[None, UInt32]:
        """"""
    def Invoke(
        self,
        dispIdMember: int,
        riid: Guid,
        lcid: int,
        wFlags: int,
        pDispParams: IntPtr,
        pVarResult: IntPtr,
        pExcepInfo: IntPtr,
        puArgErr: IntPtr,
    ) -> None:
        """"""
    def IsDefaultAttribute(self) -> bool:
        """"""
    def Match(self, obj: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

class SplitWritesState(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SpnDictionary(StringDictionary, IEnumerable):
    """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def Item(self) -> str:
        """"""
    @Item.setter
    def Item(self, value: str) -> None: ...
    @property
    def Keys(self) -> ICollection:
        """"""
    @property
    def SyncRoot(self) -> object:
        """"""
    @property
    def Values(self) -> ICollection:
        """"""
    def Add(self, key: str, value: str) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    def ContainsKey(self, key: str) -> bool:
        """"""
    def ContainsValue(self, value: str) -> bool:
        """"""
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Remove(self, key: str) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def __contains__(self, key: str) -> bool:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    def __delitem__(self, key: str) -> None:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, key: str) -> str:
        """"""
    def __setitem__(self, key: str, value: str) -> None:
        """"""

class SpnToken(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SslConnectionInfo(Object):
    """"""

    DataCipherAlg: Final[int]
    """"""
    DataHashAlg: Final[int]
    """"""
    DataHashKeySize: Final[int]
    """"""
    DataKeySize: Final[int]
    """"""
    KeyExchKeySize: Final[int]
    """"""
    KeyExchangeAlg: Final[int]
    """"""
    Protocol: Final[int]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SslStreamContext(TransportContext):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetChannelBinding(self, kind: ChannelBindingKind) -> ChannelBinding:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetTlsTokenBindings(self) -> IEnumerable[TokenBinding]:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class StaticProxy(ProxyChain, IEnumerable[Uri], IEnumerable, IDisposable):
    """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator[Uri]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def __iter__(self) -> Iterator[Uri]:
        """"""

class StreamFramer(Object):
    """"""
    def __init__(self, Transport: Stream) -> None:
        """"""
    @property
    def ReadHeader(self) -> FrameHeader:
        """"""
    @property
    def Transport(self) -> Stream:
        """"""
    @property
    def WriteHeader(self) -> FrameHeader:
        """"""
    def BeginReadMessage(self, asyncCallback: AsyncCallback, stateObject: object) -> IAsyncResult:
        """"""
    def BeginWriteMessage(
        self, message: Array[int], asyncCallback: AsyncCallback, stateObject: object
    ) -> IAsyncResult:
        """"""
    def EndReadMessage(self, asyncResult: IAsyncResult) -> Array[int]:
        """"""
    def EndWriteMessage(self, asyncResult: IAsyncResult) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ReadMessage(self) -> Array[int]:
        """"""
    def ToString(self) -> str:
        """"""
    def WriteMessage(self, message: Array[int]) -> None:
        """"""

class StreamSizes(Object):
    """"""

    SizeOf: ClassVar[int]
    """"""
    blockSize: Final[int]
    """"""
    buffersCount: Final[int]
    """"""
    header: Final[int]
    """"""
    maximumMessage: Final[int]
    """"""
    trailer: Final[int]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SyncMemoryStream(MemoryStream, IRequestLifetimeTracker, IDisposable):
    """"""
    @property
    def CanRead(self) -> bool:
        """"""
    @property
    def CanSeek(self) -> bool:
        """"""
    @property
    def CanTimeout(self) -> bool:
        """"""
    @property
    def CanWrite(self) -> bool:
        """"""
    @property
    def Capacity(self) -> int:
        """"""
    @Capacity.setter
    def Capacity(self, value: int) -> None: ...
    @property
    def Length(self) -> int:
        """"""
    @property
    def Position(self) -> int:
        """"""
    @Position.setter
    def Position(self, value: int) -> None: ...
    @property
    def ReadTimeout(self) -> int:
        """"""
    @ReadTimeout.setter
    def ReadTimeout(self, value: int) -> None: ...
    @property
    def WriteTimeout(self) -> int:
        """"""
    @WriteTimeout.setter
    def WriteTimeout(self, value: int) -> None: ...
    def BeginRead(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """"""
    def BeginWrite(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """"""
    def Close(self) -> None:
        """"""
    @overload
    def CopyTo(self, destination: Stream) -> None:
        """"""
    @overload
    def CopyTo(self, destination: Stream, bufferSize: int) -> None:
        """"""
    @overload
    def CopyToAsync(self, destination: Stream) -> Task:
        """"""
    @overload
    def CopyToAsync(self, destination: Stream, bufferSize: int) -> Task:
        """"""
    @overload
    def CopyToAsync(
        self, destination: Stream, bufferSize: int, cancellationToken: CancellationToken
    ) -> Task:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    def Dispose(self) -> None:
        """"""
    def EndRead(self, asyncResult: IAsyncResult) -> int:
        """"""
    def EndWrite(self, asyncResult: IAsyncResult) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Flush(self) -> None:
        """"""
    @overload
    def FlushAsync(self) -> Task:
        """"""
    @overload
    def FlushAsync(self, cancellationToken: CancellationToken) -> Task:
        """"""
    def GetBuffer(self) -> Array[int]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetLifetimeService(self) -> object:
        """"""
    def GetType(self) -> Type:
        """"""
    def InitializeLifetimeService(self) -> object:
        """"""
    def Read(self, buffer: Array[int], offset: int, count: int) -> tuple[int, Array[int]]:
        """"""
    @overload
    def ReadAsync(self, buffer: Array[int], offset: int, count: int) -> Task[int]:
        """"""
    @overload
    def ReadAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task[int]:
        """"""
    def ReadByte(self) -> int:
        """"""
    def Seek(self, offset: int, loc: SeekOrigin) -> int:
        """"""
    def SetLength(self, value: int) -> None:
        """"""
    def ToArray(self) -> Array[int]:
        """"""
    def ToString(self) -> str:
        """"""
    def TrackRequestLifetime(self, requestStartTimestamp: int) -> None:
        """"""
    def TryGetBuffer(self, buffer: ArraySegment[int]) -> tuple[bool, ArraySegment[int]]:
        """"""
    def Write(self, buffer: Array[int], offset: int, count: int) -> None:
        """"""
    @overload
    def WriteAsync(self, buffer: Array[int], offset: int, count: int) -> Task:
        """"""
    @overload
    def WriteAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task:
        """"""
    def WriteByte(self, value: int) -> None:
        """"""
    def WriteTo(self, stream: Stream) -> None:
        """"""

class SyncRequestContext(RequestContextBase, IDisposable):
    """"""
    def Close(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SystemNetworkCredential(NetworkCredential, ICredentials, ICredentialsByHost):
    """"""
    @property
    def Domain(self) -> str:
        """"""
    @Domain.setter
    def Domain(self, value: str) -> None: ...
    @property
    def Password(self) -> str:
        """"""
    @Password.setter
    def Password(self, value: str) -> None: ...
    @property
    def SecurePassword(self) -> SecureString:
        """"""
    @SecurePassword.setter
    def SecurePassword(self, value: SecureString) -> None: ...
    @property
    def UserName(self) -> str:
        """"""
    @UserName.setter
    def UserName(self, value: str) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetCredential(self, host: str, port: int, authenticationType: str) -> NetworkCredential:
        """"""
    @overload
    def GetCredential(self, uri: Uri, authType: str) -> NetworkCredential:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ThreadKinds(Enum):
    """"""

    Unknown: ThreadKinds = ...
    """"""
    User: ThreadKinds = ...
    """"""
    System: ThreadKinds = ...
    """"""
    OwnerMask: ThreadKinds = ...
    """"""
    Sync: ThreadKinds = ...
    """"""
    Async: ThreadKinds = ...
    """"""
    SyncMask: ThreadKinds = ...
    """"""
    Timer: ThreadKinds = ...
    """"""
    CompletionPort: ThreadKinds = ...
    """"""
    Worker: ThreadKinds = ...
    """"""
    ThreadPool: ThreadKinds = ...
    """"""
    Finalization: ThreadKinds = ...
    """"""
    Other: ThreadKinds = ...
    """"""
    SafeSources: ThreadKinds = ...
    """"""
    SourceMask: ThreadKinds = ...
    """"""

class TimeoutValidator(ConfigurationValidatorBase):
    """"""
    def CanValidate(self, type: Type) -> bool:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def Validate(self, value: object) -> None:
        """"""

class TimerThread(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class TlsParamaters(ValueType):
    """"""

    cAlpnIds: Final[int]
    """"""
    cDisabledCrypto: Final[int]
    """"""
    dwFlags: Final[TlsParamaters.Flags]
    """"""
    grbitDisabledProtocols: Final[int]
    """"""
    pDisabledCrypto: Final[IntPtr]
    """"""
    rgstrAlpnIds: Final[IntPtr]
    """"""
    def __init__(self, protocols: SchProtocols) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    class Flags(Enum):
        """"""

        Zero: TlsParamaters.Flags = ...
        """"""
        TLS_PARAMS_OPTIONAL: TlsParamaters.Flags = ...
        """"""

class TlsStream(NetworkStream, IDisposable):
    """"""
    def __init__(
        self,
        destinationHost: str,
        networkStream: NetworkStream,
        checkCertificateRevocationList: bool,
        sslProtocols: SslProtocols,
        clientCertificates: X509CertificateCollection,
        servicePoint: ServicePoint,
        initiatingRequest: object,
        executionContext: ExecutionContext,
    ) -> None:
        """"""
    @property
    def CanRead(self) -> bool:
        """"""
    @property
    def CanSeek(self) -> bool:
        """"""
    @property
    def CanTimeout(self) -> bool:
        """"""
    @property
    def CanWrite(self) -> bool:
        """"""
    @property
    def ClientCertificate(self) -> X509Certificate:
        """"""
    @property
    def DataAvailable(self) -> bool:
        """"""
    @property
    def Length(self) -> int:
        """"""
    @property
    def Position(self) -> int:
        """"""
    @Position.setter
    def Position(self, value: int) -> None: ...
    @property
    def ReadTimeout(self) -> int:
        """"""
    @ReadTimeout.setter
    def ReadTimeout(self, value: int) -> None: ...
    @property
    def WriteTimeout(self) -> int:
        """"""
    @WriteTimeout.setter
    def WriteTimeout(self, value: int) -> None: ...
    def BeginRead(
        self,
        buffer: Array[int],
        offset: int,
        size: int,
        asyncCallback: AsyncCallback,
        asyncState: object,
    ) -> IAsyncResult:
        """"""
    def BeginWrite(
        self,
        buffer: Array[int],
        offset: int,
        size: int,
        asyncCallback: AsyncCallback,
        asyncState: object,
    ) -> IAsyncResult:
        """"""
    @overload
    def Close(self) -> None:
        """"""
    @overload
    def Close(self, timeout: int) -> None:
        """"""
    @overload
    def CopyTo(self, destination: Stream) -> None:
        """"""
    @overload
    def CopyTo(self, destination: Stream, bufferSize: int) -> None:
        """"""
    @overload
    def CopyToAsync(self, destination: Stream) -> Task:
        """"""
    @overload
    def CopyToAsync(self, destination: Stream, bufferSize: int) -> Task:
        """"""
    @overload
    def CopyToAsync(
        self, destination: Stream, bufferSize: int, cancellationToken: CancellationToken
    ) -> Task:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    def Dispose(self) -> None:
        """"""
    def EndRead(self, asyncResult: IAsyncResult) -> int:
        """"""
    def EndWrite(self, asyncResult: IAsyncResult) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Flush(self) -> None:
        """"""
    @overload
    def FlushAsync(self) -> Task:
        """"""
    @overload
    def FlushAsync(self, cancellationToken: CancellationToken) -> Task:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetLifetimeService(self) -> object:
        """"""
    def GetType(self) -> Type:
        """"""
    def InitializeLifetimeService(self) -> object:
        """"""
    def Read(self, buffer: Array[int], offset: int, size: int) -> int:
        """"""
    @overload
    def ReadAsync(self, buffer: Array[int], offset: int, count: int) -> Task[int]:
        """"""
    @overload
    def ReadAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task[int]:
        """"""
    def ReadByte(self) -> int:
        """"""
    def Seek(self, offset: int, origin: SeekOrigin) -> int:
        """"""
    def SetLength(self, value: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def Write(self, buffer: Array[int], offset: int, size: int) -> None:
        """"""
    @overload
    def WriteAsync(self, buffer: Array[int], offset: int, count: int) -> Task:
        """"""
    @overload
    def WriteAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task:
        """"""
    def WriteByte(self, value: int) -> None:
        """"""

class TrackingStringDictionary(StringDictionary, IEnumerable):
    """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def Item(self) -> str:
        """"""
    @Item.setter
    def Item(self, value: str) -> None: ...
    @property
    def Keys(self) -> ICollection:
        """"""
    @property
    def SyncRoot(self) -> object:
        """"""
    @property
    def Values(self) -> ICollection:
        """"""
    def Add(self, key: str, value: str) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    def ContainsKey(self, key: str) -> bool:
        """"""
    def ContainsValue(self, value: str) -> bool:
        """"""
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Remove(self, key: str) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def __contains__(self, key: str) -> bool:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    def __delitem__(self, key: str) -> None:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, key: str) -> str:
        """"""
    def __setitem__(self, key: str, value: str) -> None:
        """"""

class TrackingValidationObjectDictionary(StringDictionary, IEnumerable):
    """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def Item(self) -> str:
        """"""
    @Item.setter
    def Item(self, value: str) -> None: ...
    @property
    def Keys(self) -> ICollection:
        """"""
    @property
    def SyncRoot(self) -> object:
        """"""
    @property
    def Values(self) -> ICollection:
        """"""
    def Add(self, key: str, value: str) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    def ContainsKey(self, key: str) -> bool:
        """"""
    def ContainsValue(self, value: str) -> bool:
        """"""
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Remove(self, key: str) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def __contains__(self, key: str) -> bool:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    def __delitem__(self, key: str) -> None:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, key: str) -> str:
        """"""
    def __setitem__(self, key: str, value: str) -> None:
        """"""

class TransmitFileBuffers(Object):
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

class TransportContext(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetChannelBinding(self, kind: ChannelBindingKind) -> ChannelBinding:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetTlsTokenBindings(self) -> IEnumerable[TokenBinding]:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class TransportType(Enum):
    """"""

    Udp: TransportType = ...
    """"""
    Connectionless: TransportType = ...
    """"""
    Tcp: TransportType = ...
    """"""
    ConnectionOriented: TransportType = ...
    """"""
    All: TransportType = ...
    """"""

class TriState(Enum):
    """"""

    _False: TriState = ...
    """"""
    _True: TriState = ...
    """"""
    Unspecified: TriState = ...
    """"""

class TunnelStateObject(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

type UnlockConnectionDelegate = Callable[[], None]
""""""

class UnsafeNclNativeMethods(ABC, Object):
    """"""
    @classmethod
    def CoCreateInstance(
        cls, clsid: Guid, pUnkOuter: IntPtr, context: int, iid: Guid, o: Object
    ) -> tuple[None, Object]:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class UploadDataCompletedEventArgs(AsyncCompletedEventArgs):
    """"""
    @property
    def Cancelled(self) -> bool:
        """"""
    @property
    def Error(self) -> Exception:
        """"""
    @property
    def Result(self) -> Array[int]:
        """"""
    @property
    def UserState(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

type UploadDataCompletedEventHandler = Callable[[object, UploadDataCompletedEventArgs], None]
""""""

class UploadFileCompletedEventArgs(AsyncCompletedEventArgs):
    """"""
    @property
    def Cancelled(self) -> bool:
        """"""
    @property
    def Error(self) -> Exception:
        """"""
    @property
    def Result(self) -> Array[int]:
        """"""
    @property
    def UserState(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

type UploadFileCompletedEventHandler = Callable[[object, UploadFileCompletedEventArgs], None]
""""""

class UploadProgressChangedEventArgs(ProgressChangedEventArgs):
    """"""
    @property
    def BytesReceived(self) -> int:
        """"""
    @property
    def BytesSent(self) -> int:
        """"""
    @property
    def ProgressPercentage(self) -> int:
        """"""
    @property
    def TotalBytesToReceive(self) -> int:
        """"""
    @property
    def TotalBytesToSend(self) -> int:
        """"""
    @property
    def UserState(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

type UploadProgressChangedEventHandler = Callable[[object, UploadProgressChangedEventArgs], None]
""""""

class UploadStringCompletedEventArgs(AsyncCompletedEventArgs):
    """"""
    @property
    def Cancelled(self) -> bool:
        """"""
    @property
    def Error(self) -> Exception:
        """"""
    @property
    def Result(self) -> str:
        """"""
    @property
    def UserState(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

type UploadStringCompletedEventHandler = Callable[[object, UploadStringCompletedEventArgs], None]
""""""

class UploadValuesCompletedEventArgs(AsyncCompletedEventArgs):
    """"""
    @property
    def Cancelled(self) -> bool:
        """"""
    @property
    def Error(self) -> Exception:
        """"""
    @property
    def Result(self) -> Array[int]:
        """"""
    @property
    def UserState(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

type UploadValuesCompletedEventHandler = Callable[[object, UploadValuesCompletedEventArgs], None]
""""""

class ValidationHelper(ABC, Object):
    """"""

    EmptyArray: ClassVar[Array[str]]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def ExceptionMessage(cls, exception: Exception) -> str:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def HashString(cls, objectValue: object) -> str:
        """"""
    @classmethod
    def IsBlankString(cls, stringValue: str) -> bool:
        """"""
    @classmethod
    def IsInvalidHttpString(cls, stringValue: str) -> bool:
        """"""
    @classmethod
    def MakeEmptyArrayNull(cls, stringArray: Array[str]) -> Array[str]:
        """"""
    @classmethod
    def MakeStringNull(cls, stringValue: str) -> str:
        """"""
    @overload
    def ToString(self) -> str:
        """"""
    @classmethod
    @overload
    def ToString(cls, objectValue: object) -> str:
        """"""
    @classmethod
    def ValidateRange(cls, actual: int, fromAllowed: int, toAllowed: int) -> bool:
        """"""
    @classmethod
    def ValidateTcpPort(cls, port: int) -> bool:
        """"""

class WSABuffer(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class WSAData(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class WebClient(Component, IComponent, IDisposable):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def AllowReadStreamBuffering(self) -> bool:
        """"""
    @AllowReadStreamBuffering.setter
    def AllowReadStreamBuffering(self, value: bool) -> None: ...
    @property
    def AllowWriteStreamBuffering(self) -> bool:
        """"""
    @AllowWriteStreamBuffering.setter
    def AllowWriteStreamBuffering(self, value: bool) -> None: ...
    @property
    def BaseAddress(self) -> str:
        """"""
    @BaseAddress.setter
    def BaseAddress(self, value: str) -> None: ...
    @property
    def CachePolicy(self) -> RequestCachePolicy:
        """"""
    @CachePolicy.setter
    def CachePolicy(self, value: RequestCachePolicy) -> None: ...
    @property
    def Container(self) -> IContainer:
        """"""
    @property
    def Credentials(self) -> ICredentials:
        """"""
    @Credentials.setter
    def Credentials(self, value: ICredentials) -> None: ...
    @property
    def Encoding(self) -> Encoding:
        """"""
    @Encoding.setter
    def Encoding(self, value: Encoding) -> None: ...
    @property
    def Headers(self) -> WebHeaderCollection:
        """"""
    @Headers.setter
    def Headers(self, value: WebHeaderCollection) -> None: ...
    @property
    def IsBusy(self) -> bool:
        """"""
    @property
    def Proxy(self) -> IWebProxy:
        """"""
    @Proxy.setter
    def Proxy(self, value: IWebProxy) -> None: ...
    @property
    def QueryString(self) -> NameValueCollection:
        """"""
    @QueryString.setter
    def QueryString(self, value: NameValueCollection) -> None: ...
    @property
    def ResponseHeaders(self) -> WebHeaderCollection:
        """"""
    @property
    def Site(self) -> ISite:
        """"""
    @Site.setter
    def Site(self, value: ISite) -> None: ...
    @property
    def UseDefaultCredentials(self) -> bool:
        """"""
    @UseDefaultCredentials.setter
    def UseDefaultCredentials(self, value: bool) -> None: ...
    def CancelAsync(self) -> None:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    def Dispose(self) -> None:
        """"""
    @overload
    def DownloadData(self, address: str) -> Array[int]:
        """"""
    @overload
    def DownloadData(self, address: Uri) -> Array[int]:
        """"""
    @overload
    def DownloadDataAsync(self, address: Uri) -> None:
        """"""
    @overload
    def DownloadDataAsync(self, address: Uri, userToken: object) -> None:
        """"""
    @overload
    def DownloadDataTaskAsync(self, address: str) -> Task[Array[int]]:
        """"""
    @overload
    def DownloadDataTaskAsync(self, address: Uri) -> Task[Array[int]]:
        """"""
    @overload
    def DownloadFile(self, address: str, fileName: str) -> None:
        """"""
    @overload
    def DownloadFile(self, address: Uri, fileName: str) -> None:
        """"""
    @overload
    def DownloadFileAsync(self, address: Uri, fileName: str) -> None:
        """"""
    @overload
    def DownloadFileAsync(self, address: Uri, fileName: str, userToken: object) -> None:
        """"""
    @overload
    def DownloadFileTaskAsync(self, address: str, fileName: str) -> Task:
        """"""
    @overload
    def DownloadFileTaskAsync(self, address: Uri, fileName: str) -> Task:
        """"""
    @overload
    def DownloadString(self, address: str) -> str:
        """"""
    @overload
    def DownloadString(self, address: Uri) -> str:
        """"""
    @overload
    def DownloadStringAsync(self, address: Uri) -> None:
        """"""
    @overload
    def DownloadStringAsync(self, address: Uri, userToken: object) -> None:
        """"""
    @overload
    def DownloadStringTaskAsync(self, address: str) -> Task[str]:
        """"""
    @overload
    def DownloadStringTaskAsync(self, address: Uri) -> Task[str]:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetLifetimeService(self) -> object:
        """"""
    def GetType(self) -> Type:
        """"""
    def InitializeLifetimeService(self) -> object:
        """"""
    @overload
    def OpenRead(self, address: str) -> Stream:
        """"""
    @overload
    def OpenRead(self, address: Uri) -> Stream:
        """"""
    @overload
    def OpenReadAsync(self, address: Uri) -> None:
        """"""
    @overload
    def OpenReadAsync(self, address: Uri, userToken: object) -> None:
        """"""
    @overload
    def OpenReadTaskAsync(self, address: str) -> Task[Stream]:
        """"""
    @overload
    def OpenReadTaskAsync(self, address: Uri) -> Task[Stream]:
        """"""
    @overload
    def OpenWrite(self, address: str) -> Stream:
        """"""
    @overload
    def OpenWrite(self, address: str, method: str) -> Stream:
        """"""
    @overload
    def OpenWrite(self, address: Uri) -> Stream:
        """"""
    @overload
    def OpenWrite(self, address: Uri, method: str) -> Stream:
        """"""
    @overload
    def OpenWriteAsync(self, address: Uri) -> None:
        """"""
    @overload
    def OpenWriteAsync(self, address: Uri, method: str) -> None:
        """"""
    @overload
    def OpenWriteAsync(self, address: Uri, method: str, userToken: object) -> None:
        """"""
    @overload
    def OpenWriteTaskAsync(self, address: str) -> Task[Stream]:
        """"""
    @overload
    def OpenWriteTaskAsync(self, address: str, method: str) -> Task[Stream]:
        """"""
    @overload
    def OpenWriteTaskAsync(self, address: Uri) -> Task[Stream]:
        """"""
    @overload
    def OpenWriteTaskAsync(self, address: Uri, method: str) -> Task[Stream]:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def UploadData(self, address: str, data: Array[int]) -> Array[int]:
        """"""
    @overload
    def UploadData(self, address: str, method: str, data: Array[int]) -> Array[int]:
        """"""
    @overload
    def UploadData(self, address: Uri, data: Array[int]) -> Array[int]:
        """"""
    @overload
    def UploadData(self, address: Uri, method: str, data: Array[int]) -> Array[int]:
        """"""
    @overload
    def UploadDataAsync(self, address: Uri, data: Array[int]) -> None:
        """"""
    @overload
    def UploadDataAsync(self, address: Uri, method: str, data: Array[int]) -> None:
        """"""
    @overload
    def UploadDataAsync(
        self, address: Uri, method: str, data: Array[int], userToken: object
    ) -> None:
        """"""
    @overload
    def UploadDataTaskAsync(self, address: str, data: Array[int]) -> Task[Array[int]]:
        """"""
    @overload
    def UploadDataTaskAsync(self, address: str, method: str, data: Array[int]) -> Task[Array[int]]:
        """"""
    @overload
    def UploadDataTaskAsync(self, address: Uri, data: Array[int]) -> Task[Array[int]]:
        """"""
    @overload
    def UploadDataTaskAsync(self, address: Uri, method: str, data: Array[int]) -> Task[Array[int]]:
        """"""
    @overload
    def UploadFile(self, address: str, fileName: str) -> Array[int]:
        """"""
    @overload
    def UploadFile(self, address: str, method: str, fileName: str) -> Array[int]:
        """"""
    @overload
    def UploadFile(self, address: Uri, fileName: str) -> Array[int]:
        """"""
    @overload
    def UploadFile(self, address: Uri, method: str, fileName: str) -> Array[int]:
        """"""
    @overload
    def UploadFileAsync(self, address: Uri, fileName: str) -> None:
        """"""
    @overload
    def UploadFileAsync(self, address: Uri, method: str, fileName: str) -> None:
        """"""
    @overload
    def UploadFileAsync(self, address: Uri, method: str, fileName: str, userToken: object) -> None:
        """"""
    @overload
    def UploadFileTaskAsync(self, address: str, fileName: str) -> Task[Array[int]]:
        """"""
    @overload
    def UploadFileTaskAsync(self, address: str, method: str, fileName: str) -> Task[Array[int]]:
        """"""
    @overload
    def UploadFileTaskAsync(self, address: Uri, fileName: str) -> Task[Array[int]]:
        """"""
    @overload
    def UploadFileTaskAsync(self, address: Uri, method: str, fileName: str) -> Task[Array[int]]:
        """"""
    @overload
    def UploadString(self, address: str, data: str) -> str:
        """"""
    @overload
    def UploadString(self, address: str, method: str, data: str) -> str:
        """"""
    @overload
    def UploadString(self, address: Uri, data: str) -> str:
        """"""
    @overload
    def UploadString(self, address: Uri, method: str, data: str) -> str:
        """"""
    @overload
    def UploadStringAsync(self, address: Uri, data: str) -> None:
        """"""
    @overload
    def UploadStringAsync(self, address: Uri, method: str, data: str) -> None:
        """"""
    @overload
    def UploadStringAsync(self, address: Uri, method: str, data: str, userToken: object) -> None:
        """"""
    @overload
    def UploadStringTaskAsync(self, address: str, data: str) -> Task[str]:
        """"""
    @overload
    def UploadStringTaskAsync(self, address: str, method: str, data: str) -> Task[str]:
        """"""
    @overload
    def UploadStringTaskAsync(self, address: Uri, data: str) -> Task[str]:
        """"""
    @overload
    def UploadStringTaskAsync(self, address: Uri, method: str, data: str) -> Task[str]:
        """"""
    @overload
    def UploadValues(self, address: str, data: NameValueCollection) -> Array[int]:
        """"""
    @overload
    def UploadValues(self, address: str, method: str, data: NameValueCollection) -> Array[int]:
        """"""
    @overload
    def UploadValues(self, address: Uri, data: NameValueCollection) -> Array[int]:
        """"""
    @overload
    def UploadValues(self, address: Uri, method: str, data: NameValueCollection) -> Array[int]:
        """"""
    @overload
    def UploadValuesAsync(self, address: Uri, data: NameValueCollection) -> None:
        """"""
    @overload
    def UploadValuesAsync(self, address: Uri, method: str, data: NameValueCollection) -> None:
        """"""
    @overload
    def UploadValuesAsync(
        self, address: Uri, method: str, data: NameValueCollection, userToken: object
    ) -> None:
        """"""
    @overload
    def UploadValuesTaskAsync(self, address: str, data: NameValueCollection) -> Task[Array[int]]:
        """"""
    @overload
    def UploadValuesTaskAsync(
        self, address: str, method: str, data: NameValueCollection
    ) -> Task[Array[int]]:
        """"""
    @overload
    def UploadValuesTaskAsync(self, address: Uri, data: NameValueCollection) -> Task[Array[int]]:
        """"""
    @overload
    def UploadValuesTaskAsync(
        self, address: Uri, method: str, data: NameValueCollection
    ) -> Task[Array[int]]:
        """"""
    Disposed: EventType[EventHandler] = ...
    """"""
    DownloadDataCompleted: EventType[DownloadDataCompletedEventHandler] = ...
    """"""
    DownloadFileCompleted: EventType[AsyncCompletedEventHandler] = ...
    """"""
    DownloadProgressChanged: EventType[DownloadProgressChangedEventHandler] = ...
    """"""
    DownloadStringCompleted: EventType[DownloadStringCompletedEventHandler] = ...
    """"""
    OpenReadCompleted: EventType[OpenReadCompletedEventHandler] = ...
    """"""
    OpenWriteCompleted: EventType[OpenWriteCompletedEventHandler] = ...
    """"""
    UploadDataCompleted: EventType[UploadDataCompletedEventHandler] = ...
    """"""
    UploadFileCompleted: EventType[UploadFileCompletedEventHandler] = ...
    """"""
    UploadProgressChanged: EventType[UploadProgressChangedEventHandler] = ...
    """"""
    UploadStringCompleted: EventType[UploadStringCompletedEventHandler] = ...
    """"""
    UploadValuesCompleted: EventType[UploadValuesCompletedEventHandler] = ...
    """"""
    WriteStreamClosed: EventType[WriteStreamClosedEventHandler] = ...
    """"""

class WebException(InvalidOperationException, _Exception, ISerializable):
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
    def __init__(self, message: str, status: WebExceptionStatus) -> None:
        """"""
    @overload
    def __init__(
        self,
        message: str,
        innerException: Exception,
        status: WebExceptionStatus,
        response: WebResponse,
    ) -> None:
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
    def InnerException(self) -> Exception:
        """"""
    @property
    def Message(self) -> str:
        """"""
    @property
    def Response(self) -> WebResponse:
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
    def Status(self) -> WebExceptionStatus:
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
    def GetObjectData(
        self, serializationInfo: SerializationInfo, streamingContext: StreamingContext
    ) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class WebExceptionInternalStatus(Enum):
    """"""

    RequestFatal: WebExceptionInternalStatus = ...
    """"""
    ServicePointFatal: WebExceptionInternalStatus = ...
    """"""
    Recoverable: WebExceptionInternalStatus = ...
    """"""
    Isolated: WebExceptionInternalStatus = ...
    """"""

class WebExceptionMapping(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class WebExceptionStatus(Enum):
    """"""

    Success: WebExceptionStatus = ...
    """"""
    NameResolutionFailure: WebExceptionStatus = ...
    """"""
    ConnectFailure: WebExceptionStatus = ...
    """"""
    ReceiveFailure: WebExceptionStatus = ...
    """"""
    SendFailure: WebExceptionStatus = ...
    """"""
    PipelineFailure: WebExceptionStatus = ...
    """"""
    RequestCanceled: WebExceptionStatus = ...
    """"""
    ProtocolError: WebExceptionStatus = ...
    """"""
    ConnectionClosed: WebExceptionStatus = ...
    """"""
    TrustFailure: WebExceptionStatus = ...
    """"""
    SecureChannelFailure: WebExceptionStatus = ...
    """"""
    ServerProtocolViolation: WebExceptionStatus = ...
    """"""
    KeepAliveFailure: WebExceptionStatus = ...
    """"""
    Pending: WebExceptionStatus = ...
    """"""
    Timeout: WebExceptionStatus = ...
    """"""
    ProxyNameResolutionFailure: WebExceptionStatus = ...
    """"""
    UnknownError: WebExceptionStatus = ...
    """"""
    MessageLengthLimitExceeded: WebExceptionStatus = ...
    """"""
    CacheEntryNotFound: WebExceptionStatus = ...
    """"""
    RequestProhibitedByCachePolicy: WebExceptionStatus = ...
    """"""
    RequestProhibitedByProxy: WebExceptionStatus = ...
    """"""

class WebHeaderCollection(
    NameValueCollection, ICollection, IEnumerable, IDeserializationCallback, ISerializable
):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def AllKeys(self) -> Array[str]:
        """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def Item(self) -> str:
        """"""
    @property
    def Keys(self) -> NameObjectCollectionBase.KeysCollection:
        """"""
    @property
    def SyncRoot(self) -> object:
        """"""
    @overload
    def Add(self, c: NameValueCollection) -> None:
        """"""
    @overload
    def Add(self, header: HttpRequestHeader, value: str) -> None:
        """"""
    @overload
    def Add(self, header: HttpResponseHeader, value: str) -> None:
        """"""
    @overload
    def Add(self, header: str) -> None:
        """"""
    @overload
    def Add(self, name: str, value: str) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    def CopyTo(self, dest: Array, index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Get(self, index: int) -> str:
        """"""
    @overload
    def Get(self, name: str) -> str:
        """"""
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetKey(self, index: int) -> str:
        """"""
    def GetObjectData(
        self, serializationInfo: SerializationInfo, streamingContext: StreamingContext
    ) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def GetValues(self, index: int) -> Array[str]:
        """"""
    @overload
    def GetValues(self, header: str) -> Array[str]:
        """"""
    def HasKeys(self) -> bool:
        """"""
    @classmethod
    @overload
    def IsRestricted(cls, headerName: str) -> bool:
        """"""
    @classmethod
    @overload
    def IsRestricted(cls, headerName: str, response: bool) -> bool:
        """"""
    def OnDeserialization(self, sender: object) -> None:
        """"""
    @overload
    def Remove(self, header: HttpRequestHeader) -> None:
        """"""
    @overload
    def Remove(self, header: HttpResponseHeader) -> None:
        """"""
    @overload
    def Remove(self, name: str) -> None:
        """"""
    @overload
    def Set(self, header: HttpRequestHeader, value: str) -> None:
        """"""
    @overload
    def Set(self, header: HttpResponseHeader, value: str) -> None:
        """"""
    @overload
    def Set(self, name: str, value: str) -> None:
        """"""
    def ToByteArray(self) -> Array[int]:
        """"""
    def ToString(self) -> str:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    @overload
    def __delitem__(self, header: HttpRequestHeader) -> None:
        """"""
    @overload
    def __delitem__(self, header: HttpResponseHeader) -> None:
        """"""
    @overload
    def __delitem__(self, name: str) -> None:
        """"""
    def __len__(self) -> int:
        """"""
    @overload
    def __getitem__(self, header: HttpRequestHeader) -> str:
        """"""
    @overload
    def __getitem__(self, header: HttpResponseHeader) -> str:
        """"""
    @overload
    def __getitem__(self, index: int) -> str:
        """"""
    @overload
    def __getitem__(self, name: str) -> str:
        """"""
    @overload
    def __setitem__(self, header: HttpRequestHeader, value: str) -> None:
        """"""
    @overload
    def __setitem__(self, header: HttpResponseHeader, value: str) -> None:
        """"""
    @overload
    def __setitem__(self, name: str, value: str) -> None:
        """"""
    class KeysCollection(Object, ICollection, IEnumerable):
        """"""
        @property
        def Count(self) -> int:
            """"""
        @property
        def IsSynchronized(self) -> bool:
            """"""
        @property
        def Item(self) -> str:
            """"""
        @property
        def SyncRoot(self) -> object:
            """"""
        def CopyTo(self, array: Array, index: int) -> None:
            """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def Get(self, index: int) -> str:
            """"""
        def GetEnumerator(self) -> IEnumerator:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def ToString(self) -> str:
            """"""
        def __iter__(self) -> Iterator:
            """"""
        def __len__(self) -> int:
            """"""
        def __getitem__(self, index: int) -> str:
            """"""

class WebHeaderCollectionType(Enum):
    """"""

    Unknown: WebHeaderCollectionType = ...
    """"""
    WebRequest: WebHeaderCollectionType = ...
    """"""
    WebResponse: WebHeaderCollectionType = ...
    """"""
    HttpWebRequest: WebHeaderCollectionType = ...
    """"""
    HttpWebResponse: WebHeaderCollectionType = ...
    """"""
    HttpListenerRequest: WebHeaderCollectionType = ...
    """"""
    HttpListenerResponse: WebHeaderCollectionType = ...
    """"""
    FtpWebRequest: WebHeaderCollectionType = ...
    """"""
    FtpWebResponse: WebHeaderCollectionType = ...
    """"""
    FileWebRequest: WebHeaderCollectionType = ...
    """"""
    FileWebResponse: WebHeaderCollectionType = ...
    """"""

class WebParseError(ValueType):
    """"""

    Code: Final[WebParseErrorCode]
    """"""
    Section: Final[WebParseErrorSection]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class WebParseErrorCode(Enum):
    """"""

    Generic: WebParseErrorCode = ...
    """"""
    InvalidHeaderName: WebParseErrorCode = ...
    """"""
    InvalidContentLength: WebParseErrorCode = ...
    """"""
    IncompleteHeaderLine: WebParseErrorCode = ...
    """"""
    CrLfError: WebParseErrorCode = ...
    """"""
    InvalidChunkFormat: WebParseErrorCode = ...
    """"""
    UnexpectedServerResponse: WebParseErrorCode = ...
    """"""

class WebParseErrorSection(Enum):
    """"""

    Generic: WebParseErrorSection = ...
    """"""
    ResponseHeader: WebParseErrorSection = ...
    """"""
    ResponseStatusLine: WebParseErrorSection = ...
    """"""
    ResponseBody: WebParseErrorSection = ...
    """"""

class WebPermission(
    CodeAccessPermission, IUnrestrictedPermission, IPermission, ISecurityEncodable, IStackWalk
):
    """"""
    @overload
    def __init__(self, state: PermissionState) -> None:
        """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, access: NetworkAccess, uriRegex: Regex) -> None:
        """"""
    @overload
    def __init__(self, access: NetworkAccess, uriString: str) -> None:
        """"""
    @property
    def AcceptList(self) -> IEnumerator:
        """"""
    @property
    def ConnectList(self) -> IEnumerator:
        """"""
    @overload
    def AddPermission(self, access: NetworkAccess, uriRegex: Regex) -> None:
        """"""
    @overload
    def AddPermission(self, access: NetworkAccess, uriString: str) -> None:
        """"""
    def Assert(self) -> None:
        """"""
    def Copy(self) -> IPermission:
        """"""
    def Demand(self) -> None:
        """"""
    def Deny(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def FromXml(self, securityElement: SecurityElement) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Intersect(self, target: IPermission) -> IPermission:
        """"""
    def IsSubsetOf(self, target: IPermission) -> bool:
        """"""
    def IsUnrestricted(self) -> bool:
        """"""
    def PermitOnly(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def ToXml(self) -> SecurityElement:
        """"""
    def Union(self, target: IPermission) -> IPermission:
        """"""

class WebPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    """"""
    def __init__(self, action: SecurityAction) -> None:
        """"""
    @property
    def Accept(self) -> str:
        """"""
    @Accept.setter
    def Accept(self, value: str) -> None: ...
    @property
    def AcceptPattern(self) -> str:
        """"""
    @AcceptPattern.setter
    def AcceptPattern(self, value: str) -> None: ...
    @property
    def Action(self) -> SecurityAction:
        """"""
    @Action.setter
    def Action(self, value: SecurityAction) -> None: ...
    @property
    def Connect(self) -> str:
        """"""
    @Connect.setter
    def Connect(self, value: str) -> None: ...
    @property
    def ConnectPattern(self) -> str:
        """"""
    @ConnectPattern.setter
    def ConnectPattern(self, value: str) -> None: ...
    @property
    def TypeId(self) -> object:
        """"""
    @property
    def Unrestricted(self) -> bool:
        """"""
    @Unrestricted.setter
    def Unrestricted(self, value: bool) -> None: ...
    def CreatePermission(self) -> IPermission:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """"""
    def GetTypeInfoCount(self, pcTInfo: UInt32) -> tuple[None, UInt32]:
        """"""
    def Invoke(
        self,
        dispIdMember: int,
        riid: Guid,
        lcid: int,
        wFlags: int,
        pDispParams: IntPtr,
        pVarResult: IntPtr,
        pExcepInfo: IntPtr,
        puArgErr: IntPtr,
    ) -> None:
        """"""
    def IsDefaultAttribute(self) -> bool:
        """"""
    def Match(self, obj: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

class WebProxy(Object, IAutoWebProxy, IWebProxy, ISerializable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, Address: Uri) -> None:
        """"""
    @overload
    def __init__(self, Address: Uri, BypassOnLocal: bool) -> None:
        """"""
    @overload
    def __init__(self, Address: Uri, BypassOnLocal: bool, BypassList: Array[str]) -> None:
        """"""
    @overload
    def __init__(
        self, Address: Uri, BypassOnLocal: bool, BypassList: Array[str], Credentials: ICredentials
    ) -> None:
        """"""
    @overload
    def __init__(self, Host: str, Port: int) -> None:
        """"""
    @overload
    def __init__(self, Address: str) -> None:
        """"""
    @overload
    def __init__(self, Address: str, BypassOnLocal: bool) -> None:
        """"""
    @overload
    def __init__(self, Address: str, BypassOnLocal: bool, BypassList: Array[str]) -> None:
        """"""
    @overload
    def __init__(
        self, Address: str, BypassOnLocal: bool, BypassList: Array[str], Credentials: ICredentials
    ) -> None:
        """"""
    @property
    def Address(self) -> Uri:
        """"""
    @Address.setter
    def Address(self, value: Uri) -> None: ...
    @property
    def BypassArrayList(self) -> ArrayList:
        """"""
    @property
    def BypassList(self) -> Array[str]:
        """"""
    @BypassList.setter
    def BypassList(self, value: Array[str]) -> None: ...
    @property
    def BypassProxyOnLocal(self) -> bool:
        """"""
    @BypassProxyOnLocal.setter
    def BypassProxyOnLocal(self, value: bool) -> None: ...
    @property
    def Credentials(self) -> ICredentials:
        """"""
    @Credentials.setter
    def Credentials(self, value: ICredentials) -> None: ...
    @property
    def UseDefaultCredentials(self) -> bool:
        """"""
    @UseDefaultCredentials.setter
    def UseDefaultCredentials(self, value: bool) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def GetDefaultProxy(cls) -> WebProxy:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetProxies(self, destination: Uri) -> ProxyChain:
        """"""
    def GetProxy(self, destination: Uri) -> Uri:
        """"""
    def GetType(self) -> Type:
        """"""
    def IsBypassed(self, host: Uri) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

class WebProxyData(Object):
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

class WebProxyDataBuilder(ABC, Object):
    """"""
    def Build(self) -> WebProxyData:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class WebProxyScriptHelper(Object, IReflect):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def UnderlyingSystemType(self) -> Type:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetField(self, name: str, bindingAttr: BindingFlags) -> FieldInfo:
        """"""
    def GetFields(self, bindingAttr: BindingFlags) -> Array[FieldInfo]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetMember(self, name: str, bindingAttr: BindingFlags) -> Array[MemberInfo]:
        """"""
    def GetMembers(self, bindingAttr: BindingFlags) -> Array[MemberInfo]:
        """"""
    @overload
    def GetMethod(self, name: str, bindingAttr: BindingFlags) -> MethodInfo:
        """"""
    @overload
    def GetMethod(
        self,
        name: str,
        bindingAttr: BindingFlags,
        binder: Binder,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> MethodInfo:
        """"""
    def GetMethods(self, bindingAttr: BindingFlags) -> Array[MethodInfo]:
        """"""
    def GetProperties(self, bindingAttr: BindingFlags) -> Array[PropertyInfo]:
        """"""
    @overload
    def GetProperty(self, name: str, bindingAttr: BindingFlags) -> PropertyInfo:
        """"""
    @overload
    def GetProperty(
        self,
        name: str,
        bindingAttr: BindingFlags,
        binder: Binder,
        returnType: Type,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> PropertyInfo:
        """"""
    def GetType(self) -> Type:
        """"""
    def InvokeMember(
        self,
        name: str,
        invokeAttr: BindingFlags,
        binder: Binder,
        target: object,
        args: Array[object],
        modifiers: Array[ParameterModifier],
        culture: CultureInfo,
        namedParameters: Array[str],
    ) -> object:
        """"""
    def ToString(self) -> str:
        """"""
    def dnsDomainIs(self, host: str, domain: str) -> bool:
        """"""
    def dnsDomainLevels(self, host: str) -> int:
        """"""
    def dnsResolve(self, host: str) -> str:
        """"""
    def dnsResolveEx(self, host: str) -> str:
        """"""
    def getClientVersion(self) -> str:
        """"""
    def isInNet(self, host: str, pattern: str, mask: str) -> bool:
        """"""
    def isInNetEx(self, ipAddress: str, ipPrefix: str) -> bool:
        """"""
    def isPlainHostName(self, hostName: str) -> bool:
        """"""
    def isResolvable(self, host: str) -> bool:
        """"""
    def isResolvableEx(self, host: str) -> bool:
        """"""
    def localHostOrDomainIs(self, host: str, hostDom: str) -> bool:
        """"""
    def myIpAddress(self) -> str:
        """"""
    def myIpAddressEx(self) -> str:
        """"""
    def shExpMatch(self, host: str, pattern: str) -> bool:
        """"""
    def sortIpAddressList(self, IPAddressList: str) -> str:
        """"""
    def weekdayRange(self, wd1: str, wd2: object, gmt: object) -> bool:
        """"""

class WebRequest(ABC, MarshalByRefObject, ISerializable):
    """"""
    @property
    def AuthenticationLevel(self) -> AuthenticationLevel:
        """"""
    @AuthenticationLevel.setter
    def AuthenticationLevel(self, value: AuthenticationLevel) -> None: ...
    @property
    def CachePolicy(self) -> RequestCachePolicy:
        """"""
    @CachePolicy.setter
    def CachePolicy(self, value: RequestCachePolicy) -> None: ...
    @property
    def ConnectionGroupName(self) -> str:
        """"""
    @ConnectionGroupName.setter
    def ConnectionGroupName(self, value: str) -> None: ...
    @property
    def ContentLength(self) -> int:
        """"""
    @ContentLength.setter
    def ContentLength(self, value: int) -> None: ...
    @property
    def ContentType(self) -> str:
        """"""
    @ContentType.setter
    def ContentType(self, value: str) -> None: ...
    @property
    def CreatorInstance(self) -> IWebRequestCreate:
        """"""
    @property
    def Credentials(self) -> ICredentials:
        """"""
    @Credentials.setter
    def Credentials(self, value: ICredentials) -> None: ...
    @classmethod
    @property
    def DefaultCachePolicy(cls) -> RequestCachePolicy:
        """"""
    @classmethod
    @DefaultCachePolicy.setter
    def DefaultCachePolicy(cls, value: RequestCachePolicy) -> None: ...
    @classmethod
    @property
    def DefaultWebProxy(cls) -> IWebProxy:
        """"""
    @classmethod
    @DefaultWebProxy.setter
    def DefaultWebProxy(cls, value: IWebProxy) -> None: ...
    @property
    def Headers(self) -> WebHeaderCollection:
        """"""
    @Headers.setter
    def Headers(self, value: WebHeaderCollection) -> None: ...
    @property
    def ImpersonationLevel(self) -> TokenImpersonationLevel:
        """"""
    @ImpersonationLevel.setter
    def ImpersonationLevel(self, value: TokenImpersonationLevel) -> None: ...
    @property
    def Method(self) -> str:
        """"""
    @Method.setter
    def Method(self, value: str) -> None: ...
    @property
    def PreAuthenticate(self) -> bool:
        """"""
    @PreAuthenticate.setter
    def PreAuthenticate(self, value: bool) -> None: ...
    @property
    def Proxy(self) -> IWebProxy:
        """"""
    @Proxy.setter
    def Proxy(self, value: IWebProxy) -> None: ...
    @property
    def RequestUri(self) -> Uri:
        """"""
    @property
    def Timeout(self) -> int:
        """"""
    @Timeout.setter
    def Timeout(self, value: int) -> None: ...
    @property
    def UseDefaultCredentials(self) -> bool:
        """"""
    @UseDefaultCredentials.setter
    def UseDefaultCredentials(self, value: bool) -> None: ...
    def Abort(self) -> None:
        """"""
    def BeginGetRequestStream(self, callback: AsyncCallback, state: object) -> IAsyncResult:
        """"""
    def BeginGetResponse(self, callback: AsyncCallback, state: object) -> IAsyncResult:
        """"""
    @classmethod
    @overload
    def Create(cls, requestUriString: str) -> WebRequest:
        """"""
    @classmethod
    @overload
    def Create(cls, requestUri: Uri) -> WebRequest:
        """"""
    @classmethod
    def CreateDefault(cls, requestUri: Uri) -> WebRequest:
        """"""
    @classmethod
    @overload
    def CreateHttp(cls, requestUriString: str) -> HttpWebRequest:
        """"""
    @classmethod
    @overload
    def CreateHttp(cls, requestUri: Uri) -> HttpWebRequest:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    def EndGetRequestStream(self, asyncResult: IAsyncResult) -> Stream:
        """"""
    def EndGetResponse(self, asyncResult: IAsyncResult) -> WebResponse:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetLifetimeService(self) -> object:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetRequestStream(self) -> Stream:
        """"""
    def GetRequestStreamAsync(self) -> Task[Stream]:
        """"""
    def GetResponse(self) -> WebResponse:
        """"""
    def GetResponseAsync(self) -> Task[WebResponse]:
        """"""
    @classmethod
    def GetSystemWebProxy(cls) -> IWebProxy:
        """"""
    def GetType(self) -> Type:
        """"""
    def InitializeLifetimeService(self) -> object:
        """"""
    @classmethod
    def RegisterPortableWebRequestCreator(cls, creator: IWebRequestCreate) -> None:
        """"""
    @classmethod
    def RegisterPrefix(cls, prefix: str, creator: IWebRequestCreate) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

class WebRequestMethods(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    class File(ABC, Object):
        """"""

        DownloadFile: ClassVar[str]
        """"""
        UploadFile: ClassVar[str]
        """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def ToString(self) -> str:
            """"""

    class Ftp(ABC, Object):
        """"""

        AppendFile: ClassVar[str]
        """"""
        DeleteFile: ClassVar[str]
        """"""
        DownloadFile: ClassVar[str]
        """"""
        GetDateTimestamp: ClassVar[str]
        """"""
        GetFileSize: ClassVar[str]
        """"""
        ListDirectory: ClassVar[str]
        """"""
        ListDirectoryDetails: ClassVar[str]
        """"""
        MakeDirectory: ClassVar[str]
        """"""
        PrintWorkingDirectory: ClassVar[str]
        """"""
        RemoveDirectory: ClassVar[str]
        """"""
        Rename: ClassVar[str]
        """"""
        UploadFile: ClassVar[str]
        """"""
        UploadFileWithUniqueName: ClassVar[str]
        """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def ToString(self) -> str:
            """"""

    class Http(ABC, Object):
        """"""

        Connect: ClassVar[str]
        """"""
        Get: ClassVar[str]
        """"""
        Head: ClassVar[str]
        """"""
        MkCol: ClassVar[str]
        """"""
        Post: ClassVar[str]
        """"""
        Put: ClassVar[str]
        """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def ToString(self) -> str:
            """"""

class WebRequestPrefixElement(Object):
    """"""

    Prefix: Final[str]
    """"""
    @overload
    def __init__(self, P: str, creatorType: Type) -> None:
        """"""
    @overload
    def __init__(self, P: str, C: IWebRequestCreate) -> None:
        """"""
    @property
    def Creator(self) -> IWebRequestCreate:
        """"""
    @Creator.setter
    def Creator(self, value: IWebRequestCreate) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class WebResponse(ABC, MarshalByRefObject, ISerializable, IDisposable):
    """"""
    @property
    def ContentLength(self) -> int:
        """"""
    @ContentLength.setter
    def ContentLength(self, value: int) -> None: ...
    @property
    def ContentType(self) -> str:
        """"""
    @ContentType.setter
    def ContentType(self, value: str) -> None: ...
    @property
    def Headers(self) -> WebHeaderCollection:
        """"""
    @property
    def IsFromCache(self) -> bool:
        """"""
    @property
    def IsMutuallyAuthenticated(self) -> bool:
        """"""
    @property
    def ResponseUri(self) -> Uri:
        """"""
    @property
    def SupportsHeaders(self) -> bool:
        """"""
    def Close(self) -> None:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetLifetimeService(self) -> object:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetResponseStream(self) -> Stream:
        """"""
    def GetType(self) -> Type:
        """"""
    def InitializeLifetimeService(self) -> object:
        """"""
    def ToString(self) -> str:
        """"""

class WebSocketHttpRequestCreator(Object, IWebRequestCreate):
    """"""
    def __init__(self, usingHttps: bool) -> None:
        """"""
    def Create(self, Uri: Uri) -> WebRequest:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class WebUtility(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    @overload
    def HtmlDecode(cls, value: str) -> str:
        """"""
    @classmethod
    @overload
    def HtmlDecode(cls, value: str, output: TextWriter) -> None:
        """"""
    @classmethod
    @overload
    def HtmlEncode(cls, value: str) -> str:
        """"""
    @classmethod
    @overload
    def HtmlEncode(cls, value: str, output: TextWriter) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def UrlDecode(cls, encodedValue: str) -> str:
        """"""
    @classmethod
    def UrlDecodeToBytes(cls, encodedValue: Array[int], offset: int, count: int) -> Array[int]:
        """"""
    @classmethod
    def UrlEncode(cls, value: str) -> str:
        """"""
    @classmethod
    def UrlEncodeToBytes(cls, value: Array[int], offset: int, count: int) -> Array[int]:
        """"""

class Win32(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class WinHttpWebProxyBuilder(WebProxyDataBuilder):
    """"""
    def __init__(self) -> None:
        """"""
    def Build(self) -> WebProxyData:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class WinHttpWebProxyFinder(BaseWebProxyFinder, IWebProxyFinder, IDisposable):
    """"""
    def __init__(self, engine: AutoWebProxyScriptEngine) -> None:
        """"""
    @property
    def IsUnrecognizedScheme(self) -> bool:
        """"""
    @property
    def IsValid(self) -> bool:
        """"""
    def Abort(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetProxies(self, destination: Uri, proxyList: IList[str]) -> tuple[bool, IList[str]]:
        """"""
    def GetType(self) -> Type:
        """"""
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class WindowsInstallationType(Enum):
    """"""

    Unknown: WindowsInstallationType = ...
    """"""
    Client: WindowsInstallationType = ...
    """"""
    Server: WindowsInstallationType = ...
    """"""
    ServerCore: WindowsInstallationType = ...
    """"""
    Embedded: WindowsInstallationType = ...
    """"""

class WorkerAsyncResult(LazyAsyncResult, IAsyncResult):
    """"""

    Buffer: Final[Array[int]]
    """"""
    End: Final[int]
    """"""
    HandshakeDone: Final[bool]
    """"""
    HeaderDone: Final[bool]
    """"""
    IsWrite: Final[bool]
    """"""
    Offset: Final[int]
    """"""
    ParentResult: Final[WorkerAsyncResult]
    """"""
    def __init__(
        self,
        asyncObject: object,
        asyncState: object,
        savedAsyncCallback: AsyncCallback,
        buffer: Array[int],
        offset: int,
        end: int,
    ) -> None:
        """"""
    @property
    def AsyncState(self) -> object:
        """"""
    @property
    def AsyncWaitHandle(self) -> WaitHandle:
        """"""
    @property
    def CompletedSynchronously(self) -> bool:
        """"""
    @property
    def IsCompleted(self) -> bool:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class WriteBufferState(Enum):
    """"""

    Disabled: WriteBufferState = ...
    """"""
    Headers: WriteBufferState = ...
    """"""
    Buffer: WriteBufferState = ...
    """"""
    Playback: WriteBufferState = ...
    """"""

class WriteHeadersCallbackState(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class WriteStreamClosedEventArgs(EventArgs):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Error(self) -> Exception:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

type WriteStreamClosedEventHandler = Callable[[object, WriteStreamClosedEventArgs], None]
""""""

class _CERT_CHAIN_ELEMENT(ValueType):
    """"""

    cbSize: Final[int]
    """"""
    pCertContext: Final[IntPtr]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class hostent(ValueType):
    """"""

    h_addr_list: Final[IntPtr]
    """"""
    h_addrtype: Final[int]
    """"""
    h_aliases: Final[IntPtr]
    """"""
    h_length: Final[int]
    """"""
    h_name: Final[IntPtr]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
