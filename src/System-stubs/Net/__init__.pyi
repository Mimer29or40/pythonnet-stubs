from __future__ import annotations

from abc import ABC
from typing import Callable
from typing import ClassVar
from typing import Final
from typing import Generic
from typing import Iterator
from typing import Tuple
from typing import TypeVar
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
from System import DateTime
from System import Enum
from System import EventArgs
from System import EventHandler
from System import Exception
from System import FormatException
from System import Guid
from System import IAsyncResult
from System import IDisposable
from System import IntPtr
from System import InvalidOperationException
from System import MarshalByRefObject
from System import Object
from System import Predicate
from System import String
from System import SystemException
from System import TimeSpan
from System import Type
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
from System.Collections.Specialized.NameObjectCollectionBase import KeysCollection
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
from System.Net.HttpListener import ExtendedProtectionSelector
from System.Net.Mime import IEncodableStream
from System.Net.SecureCredential import Flags
from System.Net.SecureCredential2 import Flags
from System.Net.Security import AuthenticationLevel
from System.Net.Security import EncryptionPolicy
from System.Net.Security import RemoteCertificateValidationCallback
from System.Net.Security import TlsAlertMessage
from System.Net.Security import TlsAlertType
from System.Net.Sockets import AddressFamily
from System.Net.Sockets import NetworkStream
from System.Net.TlsParamaters import Flags
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

T = TypeVar("T")

class EventType(Generic[T]):
    def __iadd__(self, other: T): ...
    def __isub__(self, other: T): ...

class AddressInfo(ValueType):
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

AsyncProtocolCallback: Callable[[AsyncProtocolRequest], None] = ...
"""

:param asyncRequest: 
"""

class AsyncProtocolRequest(Object):
    """"""

    AsyncState: Final[object] = ...
    """
    
    :return: 
    """
    Buffer: Final[Array[int]] = ...
    """
    
    :return: 
    """
    Count: Final[int] = ...
    """
    
    :return: 
    """
    Offset: Final[int] = ...
    """
    
    :return: 
    """
    Result: Final[int] = ...
    """
    
    :return: 
    """
    UserAsyncResult: Final[LazyAsyncResult] = ...
    """
    
    :return: 
    """
    def __init__(self, userAsyncResult: LazyAsyncResult):
        """

        :param userAsyncResult:
        """
    @property
    def MustCompleteSynchronously(self) -> bool:
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
    def SetNextRequest(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncProtocolCallback
    ) -> None:
        """

        :param buffer:
        :param offset:
        :param count:
        :param callback:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class AsyncRequestContext(RequestContextBase, IDisposable):
    """"""

    def Close(self) -> None:
        """"""
    def Dispose(self) -> None:
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

class AuthIdentity(ValueType):
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

class AuthenticationManager(Object):
    """"""

    @classmethod
    @property
    def CredentialPolicy(cls) -> ICredentialPolicy:
        """

        :return:
        """
    @classmethod
    @CredentialPolicy.setter
    def CredentialPolicy(cls, value: ICredentialPolicy) -> None: ...
    @classmethod
    @property
    def CustomTargetNameDictionary(cls) -> StringDictionary:
        """

        :return:
        """
    @classmethod
    @property
    def RegisteredModules(cls) -> IEnumerator:
        """

        :return:
        """
    @classmethod
    def Authenticate(
        cls, challenge: str, request: WebRequest, credentials: ICredentials
    ) -> Authorization:
        """

        :param challenge:
        :param request:
        :param credentials:
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
    @classmethod
    def PreAuthenticate(cls, request: WebRequest, credentials: ICredentials) -> Authorization:
        """

        :param request:
        :param credentials:
        :return:
        """
    @classmethod
    def Register(cls, authenticationModule: IAuthenticationModule) -> None:
        """

        :param authenticationModule:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @classmethod
    @overload
    def Unregister(cls, authenticationModule: IAuthenticationModule) -> None:
        """

        :param authenticationModule:
        """
    @classmethod
    @overload
    def Unregister(cls, authenticationScheme: str) -> None:
        """

        :param authenticationScheme:
        """

class AuthenticationManager2(AuthenticationManagerBase, IAuthenticationManager):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, maxPrefixLookupEntries: int):
        """

        :param maxPrefixLookupEntries:
        """
    @property
    def CredentialPolicy(self) -> ICredentialPolicy:
        """

        :return:
        """
    @CredentialPolicy.setter
    def CredentialPolicy(self, value: ICredentialPolicy) -> None: ...
    @property
    def CustomTargetNameDictionary(self) -> StringDictionary:
        """

        :return:
        """
    @property
    def OSSupportsExtendedProtection(self) -> bool:
        """

        :return:
        """
    @property
    def RegisteredModules(self) -> IEnumerator:
        """

        :return:
        """
    @property
    def SpnDictionary(self) -> SpnDictionary:
        """

        :return:
        """
    @property
    def SspSupportsExtendedProtection(self) -> bool:
        """

        :return:
        """
    def Authenticate(
        self, challenge: str, request: WebRequest, credentials: ICredentials
    ) -> Authorization:
        """

        :param challenge:
        :param request:
        :param credentials:
        :return:
        """
    def BindModule(self, uri: Uri, response: Authorization, module: IAuthenticationModule) -> None:
        """

        :param uri:
        :param response:
        :param module:
        """
    def EnsureConfigLoaded(self) -> None:
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
    def PreAuthenticate(self, request: WebRequest, credentials: ICredentials) -> Authorization:
        """

        :param request:
        :param credentials:
        :return:
        """
    def Register(self, authenticationModule: IAuthenticationModule) -> None:
        """

        :param authenticationModule:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def Unregister(self, authenticationModule: IAuthenticationModule) -> None:
        """

        :param authenticationModule:
        """
    @overload
    def Unregister(self, authenticationScheme: str) -> None:
        """

        :param authenticationScheme:
        """

class AuthenticationManagerBase(ABC, Object, IAuthenticationManager):
    """"""

    @property
    def CredentialPolicy(self) -> ICredentialPolicy:
        """

        :return:
        """
    @CredentialPolicy.setter
    def CredentialPolicy(self, value: ICredentialPolicy) -> None: ...
    @property
    def CustomTargetNameDictionary(self) -> StringDictionary:
        """

        :return:
        """
    @property
    def OSSupportsExtendedProtection(self) -> bool:
        """

        :return:
        """
    @property
    def RegisteredModules(self) -> IEnumerator:
        """

        :return:
        """
    @property
    def SpnDictionary(self) -> SpnDictionary:
        """

        :return:
        """
    @property
    def SspSupportsExtendedProtection(self) -> bool:
        """

        :return:
        """
    def Authenticate(
        self, challenge: str, request: WebRequest, credentials: ICredentials
    ) -> Authorization:
        """

        :param challenge:
        :param request:
        :param credentials:
        :return:
        """
    def BindModule(self, uri: Uri, response: Authorization, module: IAuthenticationModule) -> None:
        """

        :param uri:
        :param response:
        :param module:
        """
    def EnsureConfigLoaded(self) -> None:
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
    def PreAuthenticate(self, request: WebRequest, credentials: ICredentials) -> Authorization:
        """

        :param request:
        :param credentials:
        :return:
        """
    def Register(self, authenticationModule: IAuthenticationModule) -> None:
        """

        :param authenticationModule:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def Unregister(self, authenticationModule: IAuthenticationModule) -> None:
        """

        :param authenticationModule:
        """
    @overload
    def Unregister(self, authenticationScheme: str) -> None:
        """

        :param authenticationScheme:
        """

class AuthenticationManagerDefault(AuthenticationManagerBase, IAuthenticationManager):
    """"""

    def __init__(self):
        """"""
    @property
    def CredentialPolicy(self) -> ICredentialPolicy:
        """

        :return:
        """
    @CredentialPolicy.setter
    def CredentialPolicy(self, value: ICredentialPolicy) -> None: ...
    @property
    def CustomTargetNameDictionary(self) -> StringDictionary:
        """

        :return:
        """
    @property
    def OSSupportsExtendedProtection(self) -> bool:
        """

        :return:
        """
    @property
    def RegisteredModules(self) -> IEnumerator:
        """

        :return:
        """
    @property
    def SpnDictionary(self) -> SpnDictionary:
        """

        :return:
        """
    @property
    def SspSupportsExtendedProtection(self) -> bool:
        """

        :return:
        """
    def Authenticate(
        self, challenge: str, request: WebRequest, credentials: ICredentials
    ) -> Authorization:
        """

        :param challenge:
        :param request:
        :param credentials:
        :return:
        """
    def BindModule(self, uri: Uri, response: Authorization, module: IAuthenticationModule) -> None:
        """

        :param uri:
        :param response:
        :param module:
        """
    def EnsureConfigLoaded(self) -> None:
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
    def PreAuthenticate(self, request: WebRequest, credentials: ICredentials) -> Authorization:
        """

        :param request:
        :param credentials:
        :return:
        """
    def Register(self, authenticationModule: IAuthenticationModule) -> None:
        """

        :param authenticationModule:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def Unregister(self, authenticationModule: IAuthenticationModule) -> None:
        """

        :param authenticationModule:
        """
    @overload
    def Unregister(self, authenticationScheme: str) -> None:
        """

        :param authenticationScheme:
        """

AuthenticationSchemeSelector: Callable[[HttpListenerRequest], AuthenticationSchemes] = ...
"""

:param httpRequest: 
:return: 
"""

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

class Authorization(Object):
    """"""

    @overload
    def __init__(self, token: str):
        """

        :param token:
        """
    @overload
    def __init__(self, token: str, finished: bool):
        """

        :param token:
        :param finished:
        """
    @overload
    def __init__(self, token: str, finished: bool, connectionGroupId: str):
        """

        :param token:
        :param finished:
        :param connectionGroupId:
        """
    @property
    def Complete(self) -> bool:
        """

        :return:
        """
    @property
    def ConnectionGroupId(self) -> str:
        """

        :return:
        """
    @property
    def Message(self) -> str:
        """

        :return:
        """
    @property
    def MutuallyAuthenticated(self) -> bool:
        """

        :return:
        """
    @MutuallyAuthenticated.setter
    def MutuallyAuthenticated(self, value: bool) -> None: ...
    @property
    def ProtectionRealm(self) -> Array[str]:
        """

        :return:
        """
    @ProtectionRealm.setter
    def ProtectionRealm(self, value: Array[str]) -> None: ...
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

class AutoWebProxyScriptEngine(Object):
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

class AutoWebProxyScriptWrapper(Object):
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

class Base64Stream(DelegatedStream, IEncodableStream, IDisposable):
    """"""

    @property
    def CanRead(self) -> bool:
        """

        :return:
        """
    @property
    def CanSeek(self) -> bool:
        """

        :return:
        """
    @property
    def CanTimeout(self) -> bool:
        """

        :return:
        """
    @property
    def CanWrite(self) -> bool:
        """

        :return:
        """
    @property
    def Length(self) -> int:
        """

        :return:
        """
    @property
    def Position(self) -> int:
        """

        :return:
        """
    @Position.setter
    def Position(self, value: int) -> None: ...
    @property
    def ReadTimeout(self) -> int:
        """

        :return:
        """
    @ReadTimeout.setter
    def ReadTimeout(self, value: int) -> None: ...
    @property
    def WriteTimeout(self) -> int:
        """

        :return:
        """
    @WriteTimeout.setter
    def WriteTimeout(self, value: int) -> None: ...
    def BeginRead(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """

        :param buffer:
        :param offset:
        :param count:
        :param callback:
        :param state:
        :return:
        """
    def BeginWrite(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """

        :param buffer:
        :param offset:
        :param count:
        :param callback:
        :param state:
        :return:
        """
    def Close(self) -> None:
        """"""
    @overload
    def CopyTo(self, destination: Stream) -> None:
        """

        :param destination:
        """
    @overload
    def CopyTo(self, destination: Stream, bufferSize: int) -> None:
        """

        :param destination:
        :param bufferSize:
        """
    @overload
    def CopyToAsync(self, destination: Stream) -> Task:
        """

        :param destination:
        :return:
        """
    @overload
    def CopyToAsync(self, destination: Stream, bufferSize: int) -> Task:
        """

        :param destination:
        :param bufferSize:
        :return:
        """
    @overload
    def CopyToAsync(
        self, destination: Stream, bufferSize: int, cancellationToken: CancellationToken
    ) -> Task:
        """

        :param destination:
        :param bufferSize:
        :param cancellationToken:
        :return:
        """
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """

        :param requestedType:
        :return:
        """
    def DecodeBytes(self, buffer: Array[int], offset: int, count: int) -> int:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    def EncodeBytes(self, buffer: Array[int], offset: int, count: int) -> int:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    def EndRead(self, asyncResult: IAsyncResult) -> int:
        """

        :param asyncResult:
        :return:
        """
    def EndWrite(self, asyncResult: IAsyncResult) -> None:
        """

        :param asyncResult:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def Flush(self) -> None:
        """"""
    @overload
    def FlushAsync(self) -> Task:
        """

        :return:
        """
    @overload
    def FlushAsync(self, cancellationToken: CancellationToken) -> Task:
        """

        :param cancellationToken:
        :return:
        """
    def GetEncodedString(self) -> str:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetLifetimeService(self) -> object:
        """

        :return:
        """
    def GetStream(self) -> Stream:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def InitializeLifetimeService(self) -> object:
        """

        :return:
        """
    def Read(self, buffer: Array[int], offset: int, count: int) -> Tuple[int, Array[int]]:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def ReadAsync(self, buffer: Array[int], offset: int, count: int) -> Task[int]:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def ReadAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task[int]:
        """

        :param buffer:
        :param offset:
        :param count:
        :param cancellationToken:
        :return:
        """
    def ReadByte(self) -> int:
        """

        :return:
        """
    def Seek(self, offset: int, origin: SeekOrigin) -> int:
        """

        :param offset:
        :param origin:
        :return:
        """
    def SetLength(self, value: int) -> None:
        """

        :param value:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Write(self, buffer: Array[int], offset: int, count: int) -> None:
        """

        :param buffer:
        :param offset:
        :param count:
        """
    @overload
    def WriteAsync(self, buffer: Array[int], offset: int, count: int) -> Task:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def WriteAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task:
        """

        :param buffer:
        :param offset:
        :param count:
        :param cancellationToken:
        :return:
        """
    def WriteByte(self, value: int) -> None:
        """

        :param value:
        """

class BaseLoggingObject(Object):
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

class BaseWebProxyFinder(ABC, Object, IWebProxyFinder, IDisposable):
    """"""

    def __init__(self, engine: AutoWebProxyScriptEngine):
        """

        :param engine:
        """
    @property
    def IsUnrecognizedScheme(self) -> bool:
        """

        :return:
        """
    @property
    def IsValid(self) -> bool:
        """

        :return:
        """
    def Abort(self) -> None:
        """"""
    def Dispose(self) -> None:
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
    def GetProxies(self, destination: Uri, proxyList: IList[str]) -> Tuple[bool, IList[str]]:
        """

        :param destination:
        :param proxyList:
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

class BasicClient(Object, IAuthenticationModule):
    """"""

    def __init__(self):
        """"""
    @property
    def AuthenticationType(self) -> str:
        """

        :return:
        """
    @property
    def CanPreAuthenticate(self) -> bool:
        """

        :return:
        """
    def Authenticate(
        self, challenge: str, request: WebRequest, credentials: ICredentials
    ) -> Authorization:
        """

        :param challenge:
        :param request:
        :param credentials:
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
    def PreAuthenticate(self, request: WebRequest, credentials: ICredentials) -> Authorization:
        """

        :param request:
        :param credentials:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

BindIPEndPoint: Callable[[ServicePoint, IPEndPoint, int], IPEndPoint] = ...
"""

:param servicePoint: 
:param remoteEndPoint: 
:param retryCount: 
:return: 
"""

class Bindings(ValueType):
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

class Blob(ValueType):
    """"""

    cbSize: Final[int] = ...
    """
    
    :return: 
    """
    pBlobData: Final[int] = ...
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

    Buffer: Final[Array[int]] = ...
    """
    
    :return: 
    """
    Buffers: Final[Array[BufferOffsetSize]] = ...
    """
    
    :return: 
    """
    Count: Final[int] = ...
    """
    
    :return: 
    """
    IsWrite: Final[bool] = ...
    """
    
    :return: 
    """
    Offset: Final[int] = ...
    """
    
    :return: 
    """
    @overload
    def __init__(
        self,
        asyncObject: object,
        buffers: Array[BufferOffsetSize],
        asyncState: object,
        asyncCallback: AsyncCallback,
    ):
        """

        :param asyncObject:
        :param buffers:
        :param asyncState:
        :param asyncCallback:
        """
    @overload
    def __init__(
        self,
        asyncObject: object,
        buffer: Array[int],
        offset: int,
        count: int,
        asyncState: object,
        asyncCallback: AsyncCallback,
    ):
        """

        :param asyncObject:
        :param buffer:
        :param offset:
        :param count:
        :param asyncState:
        :param asyncCallback:
        """
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
    ):
        """

        :param asyncObject:
        :param buffer:
        :param offset:
        :param count:
        :param isWrite:
        :param asyncState:
        :param asyncCallback:
        """
    @property
    def AsyncState(self) -> object:
        """

        :return:
        """
    @property
    def AsyncWaitHandle(self) -> WaitHandle:
        """

        :return:
        """
    @property
    def CompletedSynchronously(self) -> bool:
        """

        :return:
        """
    @property
    def IsCompleted(self) -> bool:
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

class BufferOffsetSize(Object):
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
        """

        :return:
        """
    @property
    def CanSeek(self) -> bool:
        """

        :return:
        """
    @property
    def CanTimeout(self) -> bool:
        """

        :return:
        """
    @property
    def CanWrite(self) -> bool:
        """

        :return:
        """
    @property
    def Length(self) -> int:
        """

        :return:
        """
    @property
    def Position(self) -> int:
        """

        :return:
        """
    @Position.setter
    def Position(self, value: int) -> None: ...
    @property
    def ReadTimeout(self) -> int:
        """

        :return:
        """
    @ReadTimeout.setter
    def ReadTimeout(self, value: int) -> None: ...
    @property
    def WriteTimeout(self) -> int:
        """

        :return:
        """
    @WriteTimeout.setter
    def WriteTimeout(self, value: int) -> None: ...
    def BeginRead(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """

        :param buffer:
        :param offset:
        :param count:
        :param callback:
        :param state:
        :return:
        """
    def BeginWrite(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """

        :param buffer:
        :param offset:
        :param count:
        :param callback:
        :param state:
        :return:
        """
    def Close(self) -> None:
        """"""
    @overload
    def CopyTo(self, destination: Stream) -> None:
        """

        :param destination:
        """
    @overload
    def CopyTo(self, destination: Stream, bufferSize: int) -> None:
        """

        :param destination:
        :param bufferSize:
        """
    @overload
    def CopyToAsync(self, destination: Stream) -> Task:
        """

        :param destination:
        :return:
        """
    @overload
    def CopyToAsync(self, destination: Stream, bufferSize: int) -> Task:
        """

        :param destination:
        :param bufferSize:
        :return:
        """
    @overload
    def CopyToAsync(
        self, destination: Stream, bufferSize: int, cancellationToken: CancellationToken
    ) -> Task:
        """

        :param destination:
        :param bufferSize:
        :param cancellationToken:
        :return:
        """
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """

        :param requestedType:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    def EndRead(self, asyncResult: IAsyncResult) -> int:
        """

        :param asyncResult:
        :return:
        """
    def EndWrite(self, asyncResult: IAsyncResult) -> None:
        """

        :param asyncResult:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def Flush(self) -> None:
        """"""
    @overload
    def FlushAsync(self) -> Task:
        """

        :return:
        """
    @overload
    def FlushAsync(self, cancellationToken: CancellationToken) -> Task:
        """

        :param cancellationToken:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetLifetimeService(self) -> object:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def InitializeLifetimeService(self) -> object:
        """

        :return:
        """
    def Read(self, buffer: Array[int], offset: int, count: int) -> Tuple[int, Array[int]]:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def ReadAsync(self, buffer: Array[int], offset: int, count: int) -> Task[int]:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def ReadAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task[int]:
        """

        :param buffer:
        :param offset:
        :param count:
        :param cancellationToken:
        :return:
        """
    def ReadByte(self) -> int:
        """

        :return:
        """
    def Seek(self, offset: int, origin: SeekOrigin) -> int:
        """

        :param offset:
        :param origin:
        :return:
        """
    def SetLength(self, value: int) -> None:
        """

        :param value:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Write(self, buffer: Array[int], offset: int, count: int) -> None:
        """

        :param buffer:
        :param offset:
        :param count:
        """
    @overload
    def WriteAsync(self, buffer: Array[int], offset: int, count: int) -> Task:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def WriteAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task:
        """

        :param buffer:
        :param offset:
        :param count:
        :param cancellationToken:
        :return:
        """
    def WriteByte(self, value: int) -> None:
        """

        :param value:
        """

class CachedTransportContext(TransportContext):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetChannelBinding(self, kind: ChannelBindingKind) -> ChannelBinding:
        """

        :param kind:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetTlsTokenBindings(self) -> IEnumerable[TokenBinding]:
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

class CallbackClosure(Object):
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

class CaseInsensitiveAscii(Object, IComparer, IEqualityComparer):
    """"""

    def __init__(self):
        """"""
    def Compare(self, x: object, y: object) -> int:
        """

        :param x:
        :param y:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def Equals(self, x: object, y: object) -> bool:
        """

        :param x:
        :param y:
        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetHashCode(self, obj: object) -> int:
        """

        :param obj:
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

class CertEnhKeyUse(ValueType):
    """"""

    cUsageIdentifier: Final[int] = ...
    """
    
    :return: 
    """
    rgpszUsageIdentifier: Final[None] = ...
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

class CertPolicyValidationCallback(Object):
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

class CertUsage(Enum):
    """"""

    MatchTypeAnd: CertUsage = ...
    """"""
    MatchTypeOr: CertUsage = ...
    """"""

class CertUsageMatch(ValueType):
    """"""

    Usage: Final[CertEnhKeyUse] = ...
    """
    
    :return: 
    """
    dwType: Final[CertUsage] = ...
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

    BoolCheckRevocationFreshnessTime: Final[int] = ...
    """
    
    :return: 
    """
    RequestedIssuancePolicy: Final[CertUsageMatch] = ...
    """
    
    :return: 
    """
    RequestedUsage: Final[CertUsageMatch] = ...
    """
    
    :return: 
    """
    RevocationFreshnessTime: Final[int] = ...
    """
    
    :return: 
    """
    StructSize: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    UrlRetrievalTimeout: Final[int] = ...
    """
    
    :return: 
    """
    cbSize: Final[int] = ...
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

class ChainPolicyParameter(ValueType):
    """"""

    StructSize: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    cbSize: Final[int] = ...
    """
    
    :return: 
    """
    dwFlags: Final[int] = ...
    """
    
    :return: 
    """
    pvExtraPolicyPara: Final[SSL_EXTRA_CERT_CHAIN_POLICY_PARA] = ...
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

class ChainPolicyStatus(ValueType):
    """"""

    StructSize: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    cbSize: Final[int] = ...
    """
    
    :return: 
    """
    dwError: Final[int] = ...
    """
    
    :return: 
    """
    lChainIndex: Final[int] = ...
    """
    
    :return: 
    """
    lElementIndex: Final[int] = ...
    """
    
    :return: 
    """
    pvExtraPolicyStatus: Final[None] = ...
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
    ):
        """

        :param dataSource:
        :param internalBuffer:
        :param initialBufferOffset:
        :param initialBufferCount:
        :param maxBufferLength:
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
    def Read(self, userBuffer: Array[int], userBufferOffset: int, userBufferCount: int) -> int:
        """

        :param userBuffer:
        :param userBufferOffset:
        :param userBufferCount:
        :return:
        """
    def ReadAsync(
        self,
        caller: object,
        userBuffer: Array[int],
        userBufferOffset: int,
        userBufferCount: int,
        callback: AsyncCallback,
        state: object,
    ) -> IAsyncResult:
        """

        :param caller:
        :param userBuffer:
        :param userBufferOffset:
        :param userBufferCount:
        :param callback:
        :param state:
        :return:
        """
    def ReadCallback(self, ar: IAsyncResult) -> None:
        """

        :param ar:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def TryGetLeftoverBytes(
        self, buffer: int, leftoverBufferOffset: int, leftoverBufferSize: int
    ) -> Tuple[bool, int, int, int]:
        """

        :param buffer:
        :param leftoverBufferOffset:
        :param leftoverBufferSize:
        :return:
        """

class ClosableStream(DelegatedStream, IDisposable):
    """"""

    @property
    def CanRead(self) -> bool:
        """

        :return:
        """
    @property
    def CanSeek(self) -> bool:
        """

        :return:
        """
    @property
    def CanTimeout(self) -> bool:
        """

        :return:
        """
    @property
    def CanWrite(self) -> bool:
        """

        :return:
        """
    @property
    def Length(self) -> int:
        """

        :return:
        """
    @property
    def Position(self) -> int:
        """

        :return:
        """
    @Position.setter
    def Position(self, value: int) -> None: ...
    @property
    def ReadTimeout(self) -> int:
        """

        :return:
        """
    @ReadTimeout.setter
    def ReadTimeout(self, value: int) -> None: ...
    @property
    def WriteTimeout(self) -> int:
        """

        :return:
        """
    @WriteTimeout.setter
    def WriteTimeout(self, value: int) -> None: ...
    def BeginRead(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """

        :param buffer:
        :param offset:
        :param count:
        :param callback:
        :param state:
        :return:
        """
    def BeginWrite(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """

        :param buffer:
        :param offset:
        :param count:
        :param callback:
        :param state:
        :return:
        """
    def Close(self) -> None:
        """"""
    @overload
    def CopyTo(self, destination: Stream) -> None:
        """

        :param destination:
        """
    @overload
    def CopyTo(self, destination: Stream, bufferSize: int) -> None:
        """

        :param destination:
        :param bufferSize:
        """
    @overload
    def CopyToAsync(self, destination: Stream) -> Task:
        """

        :param destination:
        :return:
        """
    @overload
    def CopyToAsync(self, destination: Stream, bufferSize: int) -> Task:
        """

        :param destination:
        :param bufferSize:
        :return:
        """
    @overload
    def CopyToAsync(
        self, destination: Stream, bufferSize: int, cancellationToken: CancellationToken
    ) -> Task:
        """

        :param destination:
        :param bufferSize:
        :param cancellationToken:
        :return:
        """
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """

        :param requestedType:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    def EndRead(self, asyncResult: IAsyncResult) -> int:
        """

        :param asyncResult:
        :return:
        """
    def EndWrite(self, asyncResult: IAsyncResult) -> None:
        """

        :param asyncResult:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def Flush(self) -> None:
        """"""
    @overload
    def FlushAsync(self) -> Task:
        """

        :return:
        """
    @overload
    def FlushAsync(self, cancellationToken: CancellationToken) -> Task:
        """

        :param cancellationToken:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetLifetimeService(self) -> object:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def InitializeLifetimeService(self) -> object:
        """

        :return:
        """
    def Read(self, buffer: Array[int], offset: int, count: int) -> Tuple[int, Array[int]]:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def ReadAsync(self, buffer: Array[int], offset: int, count: int) -> Task[int]:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def ReadAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task[int]:
        """

        :param buffer:
        :param offset:
        :param count:
        :param cancellationToken:
        :return:
        """
    def ReadByte(self) -> int:
        """

        :return:
        """
    def Seek(self, offset: int, origin: SeekOrigin) -> int:
        """

        :param offset:
        :param origin:
        :return:
        """
    def SetLength(self, value: int) -> None:
        """

        :param value:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Write(self, buffer: Array[int], offset: int, count: int) -> None:
        """

        :param buffer:
        :param offset:
        :param count:
        """
    @overload
    def WriteAsync(self, buffer: Array[int], offset: int, count: int) -> Task:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def WriteAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task:
        """

        :param buffer:
        :param offset:
        :param count:
        :param cancellationToken:
        :return:
        """
    def WriteByte(self, value: int) -> None:
        """

        :param value:
        """

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

class CommandStream(PooledStream, IDisposable):
    """"""

    @property
    def CanRead(self) -> bool:
        """

        :return:
        """
    @property
    def CanSeek(self) -> bool:
        """

        :return:
        """
    @property
    def CanTimeout(self) -> bool:
        """

        :return:
        """
    @property
    def CanWrite(self) -> bool:
        """

        :return:
        """
    @property
    def Length(self) -> int:
        """

        :return:
        """
    @property
    def Position(self) -> int:
        """

        :return:
        """
    @Position.setter
    def Position(self, value: int) -> None: ...
    @property
    def ReadTimeout(self) -> int:
        """

        :return:
        """
    @ReadTimeout.setter
    def ReadTimeout(self, value: int) -> None: ...
    @property
    def WriteTimeout(self) -> int:
        """

        :return:
        """
    @WriteTimeout.setter
    def WriteTimeout(self, value: int) -> None: ...
    def BeginRead(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """

        :param buffer:
        :param offset:
        :param count:
        :param callback:
        :param state:
        :return:
        """
    def BeginWrite(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """

        :param buffer:
        :param offset:
        :param count:
        :param callback:
        :param state:
        :return:
        """
    @overload
    def Close(self) -> None:
        """"""
    @overload
    def Close(self, timeout: int) -> None:
        """

        :param timeout:
        """
    @overload
    def CopyTo(self, destination: Stream) -> None:
        """

        :param destination:
        """
    @overload
    def CopyTo(self, destination: Stream, bufferSize: int) -> None:
        """

        :param destination:
        :param bufferSize:
        """
    @overload
    def CopyToAsync(self, destination: Stream) -> Task:
        """

        :param destination:
        :return:
        """
    @overload
    def CopyToAsync(self, destination: Stream, bufferSize: int) -> Task:
        """

        :param destination:
        :param bufferSize:
        :return:
        """
    @overload
    def CopyToAsync(
        self, destination: Stream, bufferSize: int, cancellationToken: CancellationToken
    ) -> Task:
        """

        :param destination:
        :param bufferSize:
        :param cancellationToken:
        :return:
        """
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """

        :param requestedType:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    def EndRead(self, asyncResult: IAsyncResult) -> int:
        """

        :param asyncResult:
        :return:
        """
    def EndWrite(self, asyncResult: IAsyncResult) -> None:
        """

        :param asyncResult:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def Flush(self) -> None:
        """"""
    @overload
    def FlushAsync(self) -> Task:
        """

        :return:
        """
    @overload
    def FlushAsync(self, cancellationToken: CancellationToken) -> Task:
        """

        :param cancellationToken:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetLifetimeService(self) -> object:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def InitializeLifetimeService(self) -> object:
        """

        :return:
        """
    def Read(self, buffer: Array[int], offset: int, count: int) -> Tuple[int, Array[int]]:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def ReadAsync(self, buffer: Array[int], offset: int, count: int) -> Task[int]:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def ReadAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task[int]:
        """

        :param buffer:
        :param offset:
        :param count:
        :param cancellationToken:
        :return:
        """
    def ReadByte(self) -> int:
        """

        :return:
        """
    def Seek(self, offset: int, origin: SeekOrigin) -> int:
        """

        :param offset:
        :param origin:
        :return:
        """
    def SetLength(self, value: int) -> None:
        """

        :param value:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Write(self, buffer: Array[int], offset: int, count: int) -> None:
        """

        :param buffer:
        :param offset:
        :param count:
        """
    @overload
    def WriteAsync(self, buffer: Array[int], offset: int, count: int) -> Task:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def WriteAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task:
        """

        :param buffer:
        :param offset:
        :param count:
        :param cancellationToken:
        :return:
        """
    def WriteByte(self, value: int) -> None:
        """

        :param value:
        """

class Comparer(Object, IComparer):
    """"""

    def __init__(self):
        """"""
    def Compare(self, x: object, y: object) -> int:
        """

        :param x:
        :param y:
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

CompletionDelegate: Callable[[Array[int], Exception, object], None] = ...
"""

:param responseBytes: 
:param exception: 
:param State: 
"""

class ConnectStream(Stream, ICloseEx, IRequestLifetimeTracker, IDisposable):
    """"""

    @overload
    def __init__(self, connection: Connection, request: HttpWebRequest):
        """

        :param connection:
        :param request:
        """
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
    ):
        """

        :param connection:
        :param buffer:
        :param offset:
        :param bufferCount:
        :param readCount:
        :param chunked:
        :param request:
        """
    @property
    def CanRead(self) -> bool:
        """

        :return:
        """
    @property
    def CanSeek(self) -> bool:
        """

        :return:
        """
    @property
    def CanTimeout(self) -> bool:
        """

        :return:
        """
    @property
    def CanWrite(self) -> bool:
        """

        :return:
        """
    @property
    def Length(self) -> int:
        """

        :return:
        """
    @property
    def Position(self) -> int:
        """

        :return:
        """
    @Position.setter
    def Position(self, value: int) -> None: ...
    @property
    def ReadTimeout(self) -> int:
        """

        :return:
        """
    @ReadTimeout.setter
    def ReadTimeout(self, value: int) -> None: ...
    @property
    def WriteTimeout(self) -> int:
        """

        :return:
        """
    @WriteTimeout.setter
    def WriteTimeout(self, value: int) -> None: ...
    def BeginRead(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """

        :param buffer:
        :param offset:
        :param count:
        :param callback:
        :param state:
        :return:
        """
    def BeginWrite(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """

        :param buffer:
        :param offset:
        :param count:
        :param callback:
        :param state:
        :return:
        """
    def Close(self) -> None:
        """"""
    def CloseEx(self, closeState: CloseExState) -> None:
        """

        :param closeState:
        """
    @overload
    def CopyTo(self, destination: Stream) -> None:
        """

        :param destination:
        """
    @overload
    def CopyTo(self, destination: Stream, bufferSize: int) -> None:
        """

        :param destination:
        :param bufferSize:
        """
    @overload
    def CopyToAsync(self, destination: Stream) -> Task:
        """

        :param destination:
        :return:
        """
    @overload
    def CopyToAsync(self, destination: Stream, bufferSize: int) -> Task:
        """

        :param destination:
        :param bufferSize:
        :return:
        """
    @overload
    def CopyToAsync(
        self, destination: Stream, bufferSize: int, cancellationToken: CancellationToken
    ) -> Task:
        """

        :param destination:
        :param bufferSize:
        :param cancellationToken:
        :return:
        """
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """

        :param requestedType:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    def EndRead(self, asyncResult: IAsyncResult) -> int:
        """

        :param asyncResult:
        :return:
        """
    def EndWrite(self, asyncResult: IAsyncResult) -> None:
        """

        :param asyncResult:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def Flush(self) -> None:
        """"""
    @overload
    def FlushAsync(self) -> Task:
        """

        :return:
        """
    @overload
    def FlushAsync(self, cancellationToken: CancellationToken) -> Task:
        """

        :param cancellationToken:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetLifetimeService(self) -> object:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def InitializeLifetimeService(self) -> object:
        """

        :return:
        """
    def Read(self, buffer: Array[int], offset: int, count: int) -> Tuple[int, Array[int]]:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def ReadAsync(self, buffer: Array[int], offset: int, count: int) -> Task[int]:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def ReadAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task[int]:
        """

        :param buffer:
        :param offset:
        :param count:
        :param cancellationToken:
        :return:
        """
    def ReadByte(self) -> int:
        """

        :return:
        """
    def Seek(self, offset: int, origin: SeekOrigin) -> int:
        """

        :param offset:
        :param origin:
        :return:
        """
    def SetLength(self, value: int) -> None:
        """

        :param value:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def TrackRequestLifetime(self, requestStartTimestamp: int) -> None:
        """

        :param requestStartTimestamp:
        """
    def Write(self, buffer: Array[int], offset: int, count: int) -> None:
        """

        :param buffer:
        :param offset:
        :param count:
        """
    @overload
    def WriteAsync(self, buffer: Array[int], offset: int, count: int) -> Task:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def WriteAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task:
        """

        :param buffer:
        :param offset:
        :param count:
        :param cancellationToken:
        :return:
        """
    def WriteByte(self, value: int) -> None:
        """

        :param value:
        """

class ConnectStreamContext(TransportContext):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetChannelBinding(self, kind: ChannelBindingKind) -> ChannelBinding:
        """

        :param kind:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetTlsTokenBindings(self) -> IEnumerable[TokenBinding]:
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

class Connection(PooledStream, IDisposable):
    """"""

    @property
    def CanRead(self) -> bool:
        """

        :return:
        """
    @property
    def CanSeek(self) -> bool:
        """

        :return:
        """
    @property
    def CanTimeout(self) -> bool:
        """

        :return:
        """
    @property
    def CanWrite(self) -> bool:
        """

        :return:
        """
    @property
    def Length(self) -> int:
        """

        :return:
        """
    @property
    def Position(self) -> int:
        """

        :return:
        """
    @Position.setter
    def Position(self, value: int) -> None: ...
    @property
    def ReadTimeout(self) -> int:
        """

        :return:
        """
    @ReadTimeout.setter
    def ReadTimeout(self, value: int) -> None: ...
    @property
    def WriteTimeout(self) -> int:
        """

        :return:
        """
    @WriteTimeout.setter
    def WriteTimeout(self, value: int) -> None: ...
    def BeginRead(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """

        :param buffer:
        :param offset:
        :param count:
        :param callback:
        :param state:
        :return:
        """
    def BeginWrite(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """

        :param buffer:
        :param offset:
        :param count:
        :param callback:
        :param state:
        :return:
        """
    @overload
    def Close(self) -> None:
        """"""
    @overload
    def Close(self, timeout: int) -> None:
        """

        :param timeout:
        """
    @overload
    def CopyTo(self, destination: Stream) -> None:
        """

        :param destination:
        """
    @overload
    def CopyTo(self, destination: Stream, bufferSize: int) -> None:
        """

        :param destination:
        :param bufferSize:
        """
    @overload
    def CopyToAsync(self, destination: Stream) -> Task:
        """

        :param destination:
        :return:
        """
    @overload
    def CopyToAsync(self, destination: Stream, bufferSize: int) -> Task:
        """

        :param destination:
        :param bufferSize:
        :return:
        """
    @overload
    def CopyToAsync(
        self, destination: Stream, bufferSize: int, cancellationToken: CancellationToken
    ) -> Task:
        """

        :param destination:
        :param bufferSize:
        :param cancellationToken:
        :return:
        """
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """

        :param requestedType:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    def EndRead(self, asyncResult: IAsyncResult) -> int:
        """

        :param asyncResult:
        :return:
        """
    def EndWrite(self, asyncResult: IAsyncResult) -> None:
        """

        :param asyncResult:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def Flush(self) -> None:
        """"""
    @overload
    def FlushAsync(self) -> Task:
        """

        :return:
        """
    @overload
    def FlushAsync(self, cancellationToken: CancellationToken) -> Task:
        """

        :param cancellationToken:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetLifetimeService(self) -> object:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def InitializeLifetimeService(self) -> object:
        """

        :return:
        """
    def Read(self, buffer: Array[int], offset: int, count: int) -> Tuple[int, Array[int]]:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def ReadAsync(self, buffer: Array[int], offset: int, count: int) -> Task[int]:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def ReadAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task[int]:
        """

        :param buffer:
        :param offset:
        :param count:
        :param cancellationToken:
        :return:
        """
    def ReadByte(self) -> int:
        """

        :return:
        """
    def Seek(self, offset: int, origin: SeekOrigin) -> int:
        """

        :param offset:
        :param origin:
        :return:
        """
    def SetLength(self, value: int) -> None:
        """

        :param value:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Write(self, buffer: Array[int], offset: int, count: int) -> None:
        """

        :param buffer:
        :param offset:
        :param count:
        """
    @overload
    def WriteAsync(self, buffer: Array[int], offset: int, count: int) -> Task:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def WriteAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task:
        """

        :param buffer:
        :param offset:
        :param count:
        :param cancellationToken:
        :return:
        """
    def WriteByte(self, value: int) -> None:
        """

        :param value:
        """

class ConnectionGroup(Object):
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

class ConnectionPoolManager(Object):
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

class ConnectionReturnResult(Object):
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
        """

        :return:
        """
    @property
    def AsyncWaitHandle(self) -> WaitHandle:
        """

        :return:
        """
    @property
    def CompletedSynchronously(self) -> bool:
        """

        :return:
        """
    @property
    def IsCompleted(self) -> bool:
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
    def __init__(self):
        """"""
    @overload
    def __init__(self, name: str, value: str):
        """

        :param name:
        :param value:
        """
    @overload
    def __init__(self, name: str, value: str, path: str):
        """

        :param name:
        :param value:
        :param path:
        """
    @overload
    def __init__(self, name: str, value: str, path: str, domain: str):
        """

        :param name:
        :param value:
        :param path:
        :param domain:
        """
    @property
    def Comment(self) -> str:
        """

        :return:
        """
    @Comment.setter
    def Comment(self, value: str) -> None: ...
    @property
    def CommentUri(self) -> Uri:
        """

        :return:
        """
    @CommentUri.setter
    def CommentUri(self, value: Uri) -> None: ...
    @property
    def Discard(self) -> bool:
        """

        :return:
        """
    @Discard.setter
    def Discard(self, value: bool) -> None: ...
    @property
    def Domain(self) -> str:
        """

        :return:
        """
    @Domain.setter
    def Domain(self, value: str) -> None: ...
    @property
    def Expired(self) -> bool:
        """

        :return:
        """
    @Expired.setter
    def Expired(self, value: bool) -> None: ...
    @property
    def Expires(self) -> DateTime:
        """

        :return:
        """
    @Expires.setter
    def Expires(self, value: DateTime) -> None: ...
    @property
    def HttpOnly(self) -> bool:
        """

        :return:
        """
    @HttpOnly.setter
    def HttpOnly(self, value: bool) -> None: ...
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def Path(self) -> str:
        """

        :return:
        """
    @Path.setter
    def Path(self, value: str) -> None: ...
    @property
    def Port(self) -> str:
        """

        :return:
        """
    @Port.setter
    def Port(self, value: str) -> None: ...
    @property
    def Secure(self) -> bool:
        """

        :return:
        """
    @Secure.setter
    def Secure(self, value: bool) -> None: ...
    @property
    def TimeStamp(self) -> DateTime:
        """

        :return:
        """
    @property
    def Value(self) -> str:
        """

        :return:
        """
    @Value.setter
    def Value(self, value: str) -> None: ...
    @property
    def Version(self) -> int:
        """

        :return:
        """
    @Version.setter
    def Version(self, value: int) -> None: ...
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

class CookieCollection(Object, ICollection, IEnumerable):
    """"""

    def __init__(self):
        """"""
    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def IsSynchronized(self) -> bool:
        """

        :return:
        """
    @property
    def Item(self) -> Cookie:
        """

        :return:
        """
    @property
    def SyncRoot(self) -> object:
        """

        :return:
        """
    @overload
    def Add(self, cookie: Cookie) -> None:
        """

        :param cookie:
        """
    @overload
    def Add(self, cookies: CookieCollection) -> None:
        """

        :param cookies:
        """
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    @overload
    def CopyTo(self, array: Array[Cookie], index: int) -> None:
        """

        :param array:
        :param index:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
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
    def __contains__(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def __getitem__(self, index: int) -> Cookie:
        """

        :param index:
        :return:
        """
    @overload
    def __getitem__(self, name: str) -> Cookie:
        """

        :param name:
        :return:
        """
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    def __len__(self) -> int:
        """

        :return:
        """

class CookieContainer(Object):
    """"""

    DefaultCookieLengthLimit: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    DefaultCookieLimit: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    DefaultPerDomainCookieLimit: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, capacity: int):
        """

        :param capacity:
        """
    @overload
    def __init__(self, capacity: int, perDomainCapacity: int, maxCookieSize: int):
        """

        :param capacity:
        :param perDomainCapacity:
        :param maxCookieSize:
        """
    @property
    def Capacity(self) -> int:
        """

        :return:
        """
    @Capacity.setter
    def Capacity(self, value: int) -> None: ...
    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def MaxCookieSize(self) -> int:
        """

        :return:
        """
    @MaxCookieSize.setter
    def MaxCookieSize(self, value: int) -> None: ...
    @property
    def PerDomainCapacity(self) -> int:
        """

        :return:
        """
    @PerDomainCapacity.setter
    def PerDomainCapacity(self, value: int) -> None: ...
    @overload
    def Add(self, cookie: Cookie) -> None:
        """

        :param cookie:
        """
    @overload
    def Add(self, cookies: CookieCollection) -> None:
        """

        :param cookies:
        """
    @overload
    def Add(self, uri: Uri, cookie: Cookie) -> None:
        """

        :param uri:
        :param cookie:
        """
    @overload
    def Add(self, uri: Uri, cookies: CookieCollection) -> None:
        """

        :param uri:
        :param cookies:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetCookieHeader(self, uri: Uri) -> str:
        """

        :param uri:
        :return:
        """
    def GetCookies(self, uri: Uri) -> CookieCollection:
        """

        :param uri:
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
    def SetCookies(self, uri: Uri, cookieHeader: str) -> None:
        """

        :param uri:
        :param cookieHeader:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CookieException(FormatException, _Exception, ISerializable):
    """"""

    def __init__(self):
        """"""
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

class CookieModule(ABC, Object):
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

class CookieParser(Object):
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

    m_ConnectStream: Final[Stream] = ...
    """
    
    :return: 
    """
    m_ContentLength: Final[int] = ...
    """
    
    :return: 
    """
    m_IsVersionHttp11: Final[bool] = ...
    """
    
    :return: 
    """
    m_ResponseHeaders: Final[WebHeaderCollection] = ...
    """
    
    :return: 
    """
    m_StatusCode: Final[HttpStatusCode] = ...
    """
    
    :return: 
    """
    m_StatusDescription: Final[str] = ...
    """
    
    :return: 
    """
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

CreateConnectionDelegate: Callable[[ConnectionPool], PooledStream] = ...
"""

:param pool: 
:return: 
"""

class CredentialCache(Object, IEnumerable, ICredentials, ICredentialsByHost):
    """"""

    def __init__(self):
        """"""
    @classmethod
    @property
    def DefaultCredentials(cls) -> ICredentials:
        """

        :return:
        """
    @classmethod
    @property
    def DefaultNetworkCredentials(cls) -> NetworkCredential:
        """

        :return:
        """
    @overload
    def Add(self, uriPrefix: Uri, authType: str, cred: NetworkCredential) -> None:
        """

        :param uriPrefix:
        :param authType:
        :param cred:
        """
    @overload
    def Add(
        self, host: str, port: int, authenticationType: str, credential: NetworkCredential
    ) -> None:
        """

        :param host:
        :param port:
        :param authenticationType:
        :param credential:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetCredential(self, uri: Uri, authType: str) -> NetworkCredential:
        """

        :param uri:
        :param authType:
        :return:
        """
    @overload
    def GetCredential(self, host: str, port: int, authenticationType: str) -> NetworkCredential:
        """

        :param host:
        :param port:
        :param authenticationType:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
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
    @overload
    def Remove(self, uriPrefix: Uri, authType: str) -> None:
        """

        :param uriPrefix:
        :param authType:
        """
    @overload
    def Remove(self, host: str, port: int, authenticationType: str) -> None:
        """

        :param host:
        :param port:
        :param authenticationType:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """

class CredentialHostKey(Object):
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

class CredentialKey(Object):
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

    def __init__(self):
        """"""
    def CheckValidationResult(
        self,
        srvPoint: ServicePoint,
        certificate: X509Certificate,
        request: WebRequest,
        certificateProblem: int,
    ) -> bool:
        """

        :param srvPoint:
        :param certificate:
        :param request:
        :param certificateProblem:
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

    def __init__(self, stream: Stream, mode: CompressionMode):
        """

        :param stream:
        :param mode:
        """
    @property
    def BaseStream(self) -> Stream:
        """

        :return:
        """
    @property
    def CanRead(self) -> bool:
        """

        :return:
        """
    @property
    def CanSeek(self) -> bool:
        """

        :return:
        """
    @property
    def CanTimeout(self) -> bool:
        """

        :return:
        """
    @property
    def CanWrite(self) -> bool:
        """

        :return:
        """
    @property
    def Length(self) -> int:
        """

        :return:
        """
    @property
    def Position(self) -> int:
        """

        :return:
        """
    @Position.setter
    def Position(self, value: int) -> None: ...
    @property
    def ReadTimeout(self) -> int:
        """

        :return:
        """
    @ReadTimeout.setter
    def ReadTimeout(self, value: int) -> None: ...
    @property
    def WriteTimeout(self) -> int:
        """

        :return:
        """
    @WriteTimeout.setter
    def WriteTimeout(self, value: int) -> None: ...
    def BeginRead(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """

        :param buffer:
        :param offset:
        :param count:
        :param callback:
        :param state:
        :return:
        """
    def BeginWrite(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """

        :param buffer:
        :param offset:
        :param count:
        :param callback:
        :param state:
        :return:
        """
    def Close(self) -> None:
        """"""
    def CloseEx(self, closeState: CloseExState) -> None:
        """

        :param closeState:
        """
    @overload
    def CopyTo(self, destination: Stream) -> None:
        """

        :param destination:
        """
    @overload
    def CopyTo(self, destination: Stream, bufferSize: int) -> None:
        """

        :param destination:
        :param bufferSize:
        """
    @overload
    def CopyToAsync(self, destination: Stream) -> Task:
        """

        :param destination:
        :return:
        """
    @overload
    def CopyToAsync(self, destination: Stream, bufferSize: int) -> Task:
        """

        :param destination:
        :param bufferSize:
        :return:
        """
    @overload
    def CopyToAsync(
        self, destination: Stream, bufferSize: int, cancellationToken: CancellationToken
    ) -> Task:
        """

        :param destination:
        :param bufferSize:
        :param cancellationToken:
        :return:
        """
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """

        :param requestedType:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    def EndRead(self, asyncResult: IAsyncResult) -> int:
        """

        :param asyncResult:
        :return:
        """
    def EndWrite(self, asyncResult: IAsyncResult) -> None:
        """

        :param asyncResult:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def Flush(self) -> None:
        """"""
    @overload
    def FlushAsync(self) -> Task:
        """

        :return:
        """
    @overload
    def FlushAsync(self, cancellationToken: CancellationToken) -> Task:
        """

        :param cancellationToken:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetLifetimeService(self) -> object:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def InitializeLifetimeService(self) -> object:
        """

        :return:
        """
    def Read(self, buffer: Array[int], offset: int, count: int) -> Tuple[int, Array[int]]:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def ReadAsync(self, buffer: Array[int], offset: int, count: int) -> Task[int]:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def ReadAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task[int]:
        """

        :param buffer:
        :param offset:
        :param count:
        :param cancellationToken:
        :return:
        """
    def ReadByte(self) -> int:
        """

        :return:
        """
    def Seek(self, offset: int, origin: SeekOrigin) -> int:
        """

        :param offset:
        :param origin:
        :return:
        """
    def SetLength(self, value: int) -> None:
        """

        :param value:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def TrackRequestLifetime(self, requestStartTimestamp: int) -> None:
        """

        :param requestStartTimestamp:
        """
    def Write(self, buffer: Array[int], offset: int, count: int) -> None:
        """

        :param buffer:
        :param offset:
        :param count:
        """
    @overload
    def WriteAsync(self, buffer: Array[int], offset: int, count: int) -> Task:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def WriteAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task:
        """

        :param buffer:
        :param offset:
        :param count:
        :param cancellationToken:
        :return:
        """
    def WriteByte(self, value: int) -> None:
        """

        :param value:
        """

class DelayedRegex(Object):
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

class DelegatedStream(Stream, IDisposable):
    """"""

    @property
    def CanRead(self) -> bool:
        """

        :return:
        """
    @property
    def CanSeek(self) -> bool:
        """

        :return:
        """
    @property
    def CanTimeout(self) -> bool:
        """

        :return:
        """
    @property
    def CanWrite(self) -> bool:
        """

        :return:
        """
    @property
    def Length(self) -> int:
        """

        :return:
        """
    @property
    def Position(self) -> int:
        """

        :return:
        """
    @Position.setter
    def Position(self, value: int) -> None: ...
    @property
    def ReadTimeout(self) -> int:
        """

        :return:
        """
    @ReadTimeout.setter
    def ReadTimeout(self, value: int) -> None: ...
    @property
    def WriteTimeout(self) -> int:
        """

        :return:
        """
    @WriteTimeout.setter
    def WriteTimeout(self, value: int) -> None: ...
    def BeginRead(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """

        :param buffer:
        :param offset:
        :param count:
        :param callback:
        :param state:
        :return:
        """
    def BeginWrite(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """

        :param buffer:
        :param offset:
        :param count:
        :param callback:
        :param state:
        :return:
        """
    def Close(self) -> None:
        """"""
    @overload
    def CopyTo(self, destination: Stream) -> None:
        """

        :param destination:
        """
    @overload
    def CopyTo(self, destination: Stream, bufferSize: int) -> None:
        """

        :param destination:
        :param bufferSize:
        """
    @overload
    def CopyToAsync(self, destination: Stream) -> Task:
        """

        :param destination:
        :return:
        """
    @overload
    def CopyToAsync(self, destination: Stream, bufferSize: int) -> Task:
        """

        :param destination:
        :param bufferSize:
        :return:
        """
    @overload
    def CopyToAsync(
        self, destination: Stream, bufferSize: int, cancellationToken: CancellationToken
    ) -> Task:
        """

        :param destination:
        :param bufferSize:
        :param cancellationToken:
        :return:
        """
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """

        :param requestedType:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    def EndRead(self, asyncResult: IAsyncResult) -> int:
        """

        :param asyncResult:
        :return:
        """
    def EndWrite(self, asyncResult: IAsyncResult) -> None:
        """

        :param asyncResult:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def Flush(self) -> None:
        """"""
    @overload
    def FlushAsync(self) -> Task:
        """

        :return:
        """
    @overload
    def FlushAsync(self, cancellationToken: CancellationToken) -> Task:
        """

        :param cancellationToken:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetLifetimeService(self) -> object:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def InitializeLifetimeService(self) -> object:
        """

        :return:
        """
    def Read(self, buffer: Array[int], offset: int, count: int) -> Tuple[int, Array[int]]:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def ReadAsync(self, buffer: Array[int], offset: int, count: int) -> Task[int]:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def ReadAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task[int]:
        """

        :param buffer:
        :param offset:
        :param count:
        :param cancellationToken:
        :return:
        """
    def ReadByte(self) -> int:
        """

        :return:
        """
    def Seek(self, offset: int, origin: SeekOrigin) -> int:
        """

        :param offset:
        :param origin:
        :return:
        """
    def SetLength(self, value: int) -> None:
        """

        :param value:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Write(self, buffer: Array[int], offset: int, count: int) -> None:
        """

        :param buffer:
        :param offset:
        :param count:
        """
    @overload
    def WriteAsync(self, buffer: Array[int], offset: int, count: int) -> Task:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def WriteAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task:
        """

        :param buffer:
        :param offset:
        :param count:
        :param cancellationToken:
        :return:
        """
    def WriteByte(self, value: int) -> None:
        """

        :param value:
        """

class DigestClient(Object, IAuthenticationModule, ISessionAuthenticationModule):
    """"""

    def __init__(self):
        """"""
    @property
    def AuthenticationType(self) -> str:
        """

        :return:
        """
    @property
    def CanPreAuthenticate(self) -> bool:
        """

        :return:
        """
    @property
    def CanUseDefaultCredentials(self) -> bool:
        """

        :return:
        """
    def Authenticate(
        self, challenge: str, request: WebRequest, credentials: ICredentials
    ) -> Authorization:
        """

        :param challenge:
        :param request:
        :param credentials:
        :return:
        """
    def ClearSession(self, webRequest: WebRequest) -> None:
        """

        :param webRequest:
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
    def PreAuthenticate(self, request: WebRequest, credentials: ICredentials) -> Authorization:
        """

        :param request:
        :param credentials:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Update(self, challenge: str, webRequest: WebRequest) -> bool:
        """

        :param challenge:
        :param webRequest:
        :return:
        """

class DirectProxy(ProxyChain, IEnumerable[Uri], IEnumerable, IDisposable):
    """"""

    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
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
    @overload
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[Uri]:
        """

        :return:
        """

class Dns(ABC, Object):
    """"""

    @classmethod
    def BeginGetHostAddresses(
        cls, hostNameOrAddress: str, requestCallback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """

        :param hostNameOrAddress:
        :param requestCallback:
        :param state:
        :return:
        """
    @classmethod
    def BeginGetHostByName(
        cls, hostName: str, requestCallback: AsyncCallback, stateObject: object
    ) -> IAsyncResult:
        """

        :param hostName:
        :param requestCallback:
        :param stateObject:
        :return:
        """
    @classmethod
    @overload
    def BeginGetHostEntry(
        cls, address: IPAddress, requestCallback: AsyncCallback, stateObject: object
    ) -> IAsyncResult:
        """

        :param address:
        :param requestCallback:
        :param stateObject:
        :return:
        """
    @classmethod
    @overload
    def BeginGetHostEntry(
        cls, hostNameOrAddress: str, requestCallback: AsyncCallback, stateObject: object
    ) -> IAsyncResult:
        """

        :param hostNameOrAddress:
        :param requestCallback:
        :param stateObject:
        :return:
        """
    @classmethod
    def BeginResolve(
        cls, hostName: str, requestCallback: AsyncCallback, stateObject: object
    ) -> IAsyncResult:
        """

        :param hostName:
        :param requestCallback:
        :param stateObject:
        :return:
        """
    @classmethod
    def EndGetHostAddresses(cls, asyncResult: IAsyncResult) -> Array[IPAddress]:
        """

        :param asyncResult:
        :return:
        """
    @classmethod
    def EndGetHostByName(cls, asyncResult: IAsyncResult) -> IPHostEntry:
        """

        :param asyncResult:
        :return:
        """
    @classmethod
    def EndGetHostEntry(cls, asyncResult: IAsyncResult) -> IPHostEntry:
        """

        :param asyncResult:
        :return:
        """
    @classmethod
    def EndResolve(cls, asyncResult: IAsyncResult) -> IPHostEntry:
        """

        :param asyncResult:
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
    def GetHostAddresses(cls, hostNameOrAddress: str) -> Array[IPAddress]:
        """

        :param hostNameOrAddress:
        :return:
        """
    @classmethod
    def GetHostAddressesAsync(cls, hostNameOrAddress: str) -> Task[Array[IPAddress]]:
        """

        :param hostNameOrAddress:
        :return:
        """
    @classmethod
    @overload
    def GetHostByAddress(cls, address: IPAddress) -> IPHostEntry:
        """

        :param address:
        :return:
        """
    @classmethod
    @overload
    def GetHostByAddress(cls, address: str) -> IPHostEntry:
        """

        :param address:
        :return:
        """
    @classmethod
    def GetHostByName(cls, hostName: str) -> IPHostEntry:
        """

        :param hostName:
        :return:
        """
    @classmethod
    @overload
    def GetHostEntry(cls, address: IPAddress) -> IPHostEntry:
        """

        :param address:
        :return:
        """
    @classmethod
    @overload
    def GetHostEntry(cls, hostNameOrAddress: str) -> IPHostEntry:
        """

        :param hostNameOrAddress:
        :return:
        """
    @classmethod
    @overload
    def GetHostEntryAsync(cls, address: IPAddress) -> Task[IPHostEntry]:
        """

        :param address:
        :return:
        """
    @classmethod
    @overload
    def GetHostEntryAsync(cls, hostNameOrAddress: str) -> Task[IPHostEntry]:
        """

        :param hostNameOrAddress:
        :return:
        """
    @classmethod
    def GetHostName(cls) -> str:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @classmethod
    def Resolve(cls, hostName: str) -> IPHostEntry:
        """

        :param hostName:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class DnsEndPoint(EndPoint):
    """"""

    @overload
    def __init__(self, host: str, port: int):
        """

        :param host:
        :param port:
        """
    @overload
    def __init__(self, host: str, port: int, addressFamily: AddressFamily):
        """

        :param host:
        :param port:
        :param addressFamily:
        """
    @property
    def AddressFamily(self) -> AddressFamily:
        """

        :return:
        """
    @property
    def Host(self) -> str:
        """

        :return:
        """
    @property
    def Port(self) -> int:
        """

        :return:
        """
    def Create(self, socketAddress: SocketAddress) -> EndPoint:
        """

        :param socketAddress:
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
    def Serialize(self) -> SocketAddress:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class DnsPermission(
    CodeAccessPermission, IUnrestrictedPermission, IPermission, ISecurityEncodable, IStackWalk
):
    """"""

    def __init__(self, state: PermissionState):
        """

        :param state:
        """
    def Assert(self) -> None:
        """"""
    def Copy(self) -> IPermission:
        """

        :return:
        """
    @overload
    def Demand(self) -> None:
        """"""
    @overload
    def Demand(self) -> None:
        """"""
    def Deny(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def FromXml(self, e: SecurityElement) -> None:
        """

        :param e:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def Intersect(self, target: IPermission) -> IPermission:
        """

        :param target:
        :return:
        """
    def IsSubsetOf(self, target: IPermission) -> bool:
        """

        :param target:
        :return:
        """
    def IsUnrestricted(self) -> bool:
        """

        :return:
        """
    def PermitOnly(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """
    def ToXml(self) -> SecurityElement:
        """

        :return:
        """
    def Union(self, target: IPermission) -> IPermission:
        """

        :param target:
        :return:
        """

class DnsPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    """"""

    def __init__(self, action: SecurityAction):
        """

        :param action:
        """
    @property
    def Action(self) -> SecurityAction:
        """

        :return:
        """
    @Action.setter
    def Action(self, value: SecurityAction) -> None: ...
    @property
    def TypeId(self) -> object:
        """

        :return:
        """
    @property
    def Unrestricted(self) -> bool:
        """

        :return:
        """
    @Unrestricted.setter
    def Unrestricted(self, value: bool) -> None: ...
    def CreatePermission(self) -> IPermission:
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
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """

        :return:
        """
    def Match(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class DownloadDataCompletedEventArgs(AsyncCompletedEventArgs):
    """"""

    @property
    def Cancelled(self) -> bool:
        """

        :return:
        """
    @property
    def Error(self) -> Exception:
        """

        :return:
        """
    @property
    def Result(self) -> Array[int]:
        """

        :return:
        """
    @property
    def UserState(self) -> object:
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

DownloadDataCompletedEventHandler: Callable[[object, DownloadDataCompletedEventArgs], None] = ...
"""

:param sender: 
:param e: 
"""

class DownloadProgressChangedEventArgs(ProgressChangedEventArgs):
    """"""

    @property
    def BytesReceived(self) -> int:
        """

        :return:
        """
    @property
    def ProgressPercentage(self) -> int:
        """

        :return:
        """
    @property
    def TotalBytesToReceive(self) -> int:
        """

        :return:
        """
    @property
    def UserState(self) -> object:
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

DownloadProgressChangedEventHandler: Callable[
    [object, DownloadProgressChangedEventArgs], None
] = ...
"""

:param sender: 
:param e: 
"""

class DownloadStringCompletedEventArgs(AsyncCompletedEventArgs):
    """"""

    @property
    def Cancelled(self) -> bool:
        """

        :return:
        """
    @property
    def Error(self) -> Exception:
        """

        :return:
        """
    @property
    def Result(self) -> str:
        """

        :return:
        """
    @property
    def UserState(self) -> object:
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

DownloadStringCompletedEventHandler: Callable[
    [object, DownloadStringCompletedEventArgs], None
] = ...
"""

:param sender: 
:param e: 
"""

class EmptyWebProxy(Object, IAutoWebProxy, IWebProxy):
    """"""

    def __init__(self):
        """"""
    @property
    def Credentials(self) -> ICredentials:
        """

        :return:
        """
    @Credentials.setter
    def Credentials(self, value: ICredentials) -> None: ...
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetProxies(self, destination: Uri) -> ProxyChain:
        """

        :param destination:
        :return:
        """
    def GetProxy(self, destination: Uri) -> Uri:
        """

        :param destination:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def IsBypassed(self, host: Uri) -> bool:
        """

        :param host:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class EndPoint(ABC, Object):
    """"""

    @property
    def AddressFamily(self) -> AddressFamily:
        """

        :return:
        """
    def Create(self, socketAddress: SocketAddress) -> EndPoint:
        """

        :param socketAddress:
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
    def Serialize(self) -> SocketAddress:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

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
        """

        :return:
        """
    @property
    def Port(self) -> int:
        """

        :return:
        """
    @property
    def Transport(self) -> TransportType:
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

class EntitySendFormat(Enum):
    """"""

    ContentLength: EntitySendFormat = ...
    """"""
    Chunked: EntitySendFormat = ...
    """"""

class ExceptionHelper(ABC, Object):
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

class FileWebRequest(WebRequest, ISerializable):
    """"""

    @property
    def AuthenticationLevel(self) -> AuthenticationLevel:
        """

        :return:
        """
    @AuthenticationLevel.setter
    def AuthenticationLevel(self, value: AuthenticationLevel) -> None: ...
    @property
    def CachePolicy(self) -> RequestCachePolicy:
        """

        :return:
        """
    @CachePolicy.setter
    def CachePolicy(self, value: RequestCachePolicy) -> None: ...
    @property
    def ConnectionGroupName(self) -> str:
        """

        :return:
        """
    @ConnectionGroupName.setter
    def ConnectionGroupName(self, value: str) -> None: ...
    @property
    def ContentLength(self) -> int:
        """

        :return:
        """
    @ContentLength.setter
    def ContentLength(self, value: int) -> None: ...
    @property
    def ContentType(self) -> str:
        """

        :return:
        """
    @ContentType.setter
    def ContentType(self, value: str) -> None: ...
    @property
    def CreatorInstance(self) -> IWebRequestCreate:
        """

        :return:
        """
    @property
    def Credentials(self) -> ICredentials:
        """

        :return:
        """
    @Credentials.setter
    def Credentials(self, value: ICredentials) -> None: ...
    @classmethod
    @property
    def DefaultCachePolicy(cls) -> RequestCachePolicy:
        """

        :return:
        """
    @classmethod
    @DefaultCachePolicy.setter
    def DefaultCachePolicy(cls, value: RequestCachePolicy) -> None: ...
    @classmethod
    @property
    def DefaultWebProxy(cls) -> IWebProxy:
        """

        :return:
        """
    @classmethod
    @DefaultWebProxy.setter
    def DefaultWebProxy(cls, value: IWebProxy) -> None: ...
    @property
    def Headers(self) -> WebHeaderCollection:
        """

        :return:
        """
    @Headers.setter
    def Headers(self, value: WebHeaderCollection) -> None: ...
    @property
    def ImpersonationLevel(self) -> TokenImpersonationLevel:
        """

        :return:
        """
    @ImpersonationLevel.setter
    def ImpersonationLevel(self, value: TokenImpersonationLevel) -> None: ...
    @property
    def Method(self) -> str:
        """

        :return:
        """
    @Method.setter
    def Method(self, value: str) -> None: ...
    @property
    def PreAuthenticate(self) -> bool:
        """

        :return:
        """
    @PreAuthenticate.setter
    def PreAuthenticate(self, value: bool) -> None: ...
    @property
    def Proxy(self) -> IWebProxy:
        """

        :return:
        """
    @Proxy.setter
    def Proxy(self, value: IWebProxy) -> None: ...
    @property
    def RequestUri(self) -> Uri:
        """

        :return:
        """
    @property
    def Timeout(self) -> int:
        """

        :return:
        """
    @Timeout.setter
    def Timeout(self, value: int) -> None: ...
    @property
    def UseDefaultCredentials(self) -> bool:
        """

        :return:
        """
    @UseDefaultCredentials.setter
    def UseDefaultCredentials(self, value: bool) -> None: ...
    def Abort(self) -> None:
        """"""
    def BeginGetRequestStream(self, callback: AsyncCallback, state: object) -> IAsyncResult:
        """

        :param callback:
        :param state:
        :return:
        """
    def BeginGetResponse(self, callback: AsyncCallback, state: object) -> IAsyncResult:
        """

        :param callback:
        :param state:
        :return:
        """
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """

        :param requestedType:
        :return:
        """
    def EndGetRequestStream(self, asyncResult: IAsyncResult) -> Stream:
        """

        :param asyncResult:
        :return:
        """
    def EndGetResponse(self, asyncResult: IAsyncResult) -> WebResponse:
        """

        :param asyncResult:
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
    def GetLifetimeService(self) -> object:
        """

        :return:
        """
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    def GetRequestStream(self) -> Stream:
        """

        :return:
        """
    def GetRequestStreamAsync(self) -> Task[Stream]:
        """

        :return:
        """
    def GetResponse(self) -> WebResponse:
        """

        :return:
        """
    def GetResponseAsync(self) -> Task[WebResponse]:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def InitializeLifetimeService(self) -> object:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class FileWebRequestCreator(Object, IWebRequestCreate):
    """"""

    def Create(self, uri: Uri) -> WebRequest:
        """

        :param uri:
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

class FileWebResponse(WebResponse, ICloseEx, ISerializable, IDisposable):
    """"""

    @property
    def ContentLength(self) -> int:
        """

        :return:
        """
    @ContentLength.setter
    def ContentLength(self, value: int) -> None: ...
    @property
    def ContentType(self) -> str:
        """

        :return:
        """
    @ContentType.setter
    def ContentType(self, value: str) -> None: ...
    @property
    def Headers(self) -> WebHeaderCollection:
        """

        :return:
        """
    @property
    def IsFromCache(self) -> bool:
        """

        :return:
        """
    @property
    def IsMutuallyAuthenticated(self) -> bool:
        """

        :return:
        """
    @property
    def ResponseUri(self) -> Uri:
        """

        :return:
        """
    @property
    def SupportsHeaders(self) -> bool:
        """

        :return:
        """
    def Close(self) -> None:
        """"""
    def CloseEx(self, closeState: CloseExState) -> None:
        """

        :param closeState:
        """
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """

        :param requestedType:
        :return:
        """
    def Dispose(self) -> None:
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
    def GetLifetimeService(self) -> object:
        """

        :return:
        """
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    def GetResponseStream(self) -> Stream:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def InitializeLifetimeService(self) -> object:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

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
    ):
        """

        :param request:
        :param path:
        :param mode:
        :param access:
        :param sharing:
        """
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
    ):
        """

        :param request:
        :param path:
        :param mode:
        :param access:
        :param sharing:
        :param length:
        :param _async:
        """
    @property
    def CanRead(self) -> bool:
        """

        :return:
        """
    @property
    def CanSeek(self) -> bool:
        """

        :return:
        """
    @property
    def CanTimeout(self) -> bool:
        """

        :return:
        """
    @property
    def CanWrite(self) -> bool:
        """

        :return:
        """
    @property
    def Handle(self) -> IntPtr:
        """

        :return:
        """
    @property
    def IsAsync(self) -> bool:
        """

        :return:
        """
    @property
    def Length(self) -> int:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Position(self) -> int:
        """

        :return:
        """
    @Position.setter
    def Position(self, value: int) -> None: ...
    @property
    def ReadTimeout(self) -> int:
        """

        :return:
        """
    @ReadTimeout.setter
    def ReadTimeout(self, value: int) -> None: ...
    @property
    def SafeFileHandle(self) -> SafeFileHandle:
        """

        :return:
        """
    @property
    def WriteTimeout(self) -> int:
        """

        :return:
        """
    @WriteTimeout.setter
    def WriteTimeout(self, value: int) -> None: ...
    def BeginRead(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """

        :param buffer:
        :param offset:
        :param count:
        :param callback:
        :param state:
        :return:
        """
    def BeginWrite(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """

        :param buffer:
        :param offset:
        :param count:
        :param callback:
        :param state:
        :return:
        """
    def Close(self) -> None:
        """"""
    def CloseEx(self, closeState: CloseExState) -> None:
        """

        :param closeState:
        """
    @overload
    def CopyTo(self, destination: Stream) -> None:
        """

        :param destination:
        """
    @overload
    def CopyTo(self, destination: Stream, bufferSize: int) -> None:
        """

        :param destination:
        :param bufferSize:
        """
    @overload
    def CopyToAsync(self, destination: Stream) -> Task:
        """

        :param destination:
        :return:
        """
    @overload
    def CopyToAsync(self, destination: Stream, bufferSize: int) -> Task:
        """

        :param destination:
        :param bufferSize:
        :return:
        """
    @overload
    def CopyToAsync(
        self, destination: Stream, bufferSize: int, cancellationToken: CancellationToken
    ) -> Task:
        """

        :param destination:
        :param bufferSize:
        :param cancellationToken:
        :return:
        """
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """

        :param requestedType:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    def EndRead(self, asyncResult: IAsyncResult) -> int:
        """

        :param asyncResult:
        :return:
        """
    def EndWrite(self, asyncResult: IAsyncResult) -> None:
        """

        :param asyncResult:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def Flush(self) -> None:
        """"""
    @overload
    def Flush(self, flushToDisk: bool) -> None:
        """

        :param flushToDisk:
        """
    @overload
    def FlushAsync(self) -> Task:
        """

        :return:
        """
    @overload
    def FlushAsync(self, cancellationToken: CancellationToken) -> Task:
        """

        :param cancellationToken:
        :return:
        """
    def GetAccessControl(self) -> FileSecurity:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetLifetimeService(self) -> object:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def InitializeLifetimeService(self) -> object:
        """

        :return:
        """
    def Lock(self, position: int, length: int) -> None:
        """

        :param position:
        :param length:
        """
    def Read(self, buffer: Array[int], offset: int, count: int) -> Tuple[int, Array[int]]:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def ReadAsync(self, buffer: Array[int], offset: int, count: int) -> Task[int]:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def ReadAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task[int]:
        """

        :param buffer:
        :param offset:
        :param count:
        :param cancellationToken:
        :return:
        """
    def ReadByte(self) -> int:
        """

        :return:
        """
    def Seek(self, offset: int, origin: SeekOrigin) -> int:
        """

        :param offset:
        :param origin:
        :return:
        """
    def SetAccessControl(self, fileSecurity: FileSecurity) -> None:
        """

        :param fileSecurity:
        """
    def SetLength(self, value: int) -> None:
        """

        :param value:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Unlock(self, position: int, length: int) -> None:
        """

        :param position:
        :param length:
        """
    def Write(self, buffer: Array[int], offset: int, count: int) -> None:
        """

        :param buffer:
        :param offset:
        :param count:
        """
    @overload
    def WriteAsync(self, buffer: Array[int], offset: int, count: int) -> Task:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def WriteAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task:
        """

        :param buffer:
        :param offset:
        :param count:
        :param cancellationToken:
        :return:
        """
    def WriteByte(self, value: int) -> None:
        """

        :param value:
        """

class FixedSizeReader(Object):
    """"""

    def __init__(self, transport: Stream):
        """

        :param transport:
        """
    def AsyncReadPacket(self, request: AsyncProtocolRequest) -> None:
        """

        :param request:
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
    def ReadPacket(self, buffer: Array[int], offset: int, count: int) -> int:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class FrameHeader(Object):
    """"""

    DefaultMajorV: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    DefaultMinorV: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    HandshakeDoneId: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    HandshakeErrId: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    HandshakeId: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    IgnoreValue: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, messageId: int, majorV: int, minorV: int):
        """

        :param messageId:
        :param majorV:
        :param minorV:
        """
    @property
    def MajorV(self) -> int:
        """

        :return:
        """
    @property
    def MaxMessageSize(self) -> int:
        """

        :return:
        """
    @property
    def MessageId(self) -> int:
        """

        :return:
        """
    @MessageId.setter
    def MessageId(self, value: int) -> None: ...
    @property
    def MinorV(self) -> int:
        """

        :return:
        """
    @property
    def PayloadSize(self) -> int:
        """

        :return:
        """
    @PayloadSize.setter
    def PayloadSize(self, value: int) -> None: ...
    @property
    def Size(self) -> int:
        """

        :return:
        """
    def CopyFrom(self, bytes: Array[int], start: int, verifier: FrameHeader) -> None:
        """

        :param bytes:
        :param start:
        :param verifier:
        """
    def CopyTo(self, dest: Array[int], start: int) -> None:
        """

        :param dest:
        :param start:
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

class FtpControlStream(CommandStream, IDisposable):
    """"""

    @property
    def CanRead(self) -> bool:
        """

        :return:
        """
    @property
    def CanSeek(self) -> bool:
        """

        :return:
        """
    @property
    def CanTimeout(self) -> bool:
        """

        :return:
        """
    @property
    def CanWrite(self) -> bool:
        """

        :return:
        """
    @property
    def Length(self) -> int:
        """

        :return:
        """
    @property
    def Position(self) -> int:
        """

        :return:
        """
    @Position.setter
    def Position(self, value: int) -> None: ...
    @property
    def ReadTimeout(self) -> int:
        """

        :return:
        """
    @ReadTimeout.setter
    def ReadTimeout(self, value: int) -> None: ...
    @property
    def WriteTimeout(self) -> int:
        """

        :return:
        """
    @WriteTimeout.setter
    def WriteTimeout(self, value: int) -> None: ...
    def BeginRead(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """

        :param buffer:
        :param offset:
        :param count:
        :param callback:
        :param state:
        :return:
        """
    def BeginWrite(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """

        :param buffer:
        :param offset:
        :param count:
        :param callback:
        :param state:
        :return:
        """
    @overload
    def Close(self) -> None:
        """"""
    @overload
    def Close(self, timeout: int) -> None:
        """

        :param timeout:
        """
    @overload
    def CopyTo(self, destination: Stream) -> None:
        """

        :param destination:
        """
    @overload
    def CopyTo(self, destination: Stream, bufferSize: int) -> None:
        """

        :param destination:
        :param bufferSize:
        """
    @overload
    def CopyToAsync(self, destination: Stream) -> Task:
        """

        :param destination:
        :return:
        """
    @overload
    def CopyToAsync(self, destination: Stream, bufferSize: int) -> Task:
        """

        :param destination:
        :param bufferSize:
        :return:
        """
    @overload
    def CopyToAsync(
        self, destination: Stream, bufferSize: int, cancellationToken: CancellationToken
    ) -> Task:
        """

        :param destination:
        :param bufferSize:
        :param cancellationToken:
        :return:
        """
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """

        :param requestedType:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    def EndRead(self, asyncResult: IAsyncResult) -> int:
        """

        :param asyncResult:
        :return:
        """
    def EndWrite(self, asyncResult: IAsyncResult) -> None:
        """

        :param asyncResult:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def Flush(self) -> None:
        """"""
    @overload
    def FlushAsync(self) -> Task:
        """

        :return:
        """
    @overload
    def FlushAsync(self, cancellationToken: CancellationToken) -> Task:
        """

        :param cancellationToken:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetLifetimeService(self) -> object:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def InitializeLifetimeService(self) -> object:
        """

        :return:
        """
    def Read(self, buffer: Array[int], offset: int, count: int) -> Tuple[int, Array[int]]:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def ReadAsync(self, buffer: Array[int], offset: int, count: int) -> Task[int]:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def ReadAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task[int]:
        """

        :param buffer:
        :param offset:
        :param count:
        :param cancellationToken:
        :return:
        """
    def ReadByte(self) -> int:
        """

        :return:
        """
    def Seek(self, offset: int, origin: SeekOrigin) -> int:
        """

        :param offset:
        :param origin:
        :return:
        """
    def SetLength(self, value: int) -> None:
        """

        :param value:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Write(self, buffer: Array[int], offset: int, count: int) -> None:
        """

        :param buffer:
        :param offset:
        :param count:
        """
    @overload
    def WriteAsync(self, buffer: Array[int], offset: int, count: int) -> Task:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def WriteAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task:
        """

        :param buffer:
        :param offset:
        :param count:
        :param cancellationToken:
        :return:
        """
    def WriteByte(self, value: int) -> None:
        """

        :param value:
        """

class FtpDataStream(Stream, ICloseEx, IDisposable):
    """"""

    @property
    def CanRead(self) -> bool:
        """

        :return:
        """
    @property
    def CanSeek(self) -> bool:
        """

        :return:
        """
    @property
    def CanTimeout(self) -> bool:
        """

        :return:
        """
    @property
    def CanWrite(self) -> bool:
        """

        :return:
        """
    @property
    def Length(self) -> int:
        """

        :return:
        """
    @property
    def Position(self) -> int:
        """

        :return:
        """
    @Position.setter
    def Position(self, value: int) -> None: ...
    @property
    def ReadTimeout(self) -> int:
        """

        :return:
        """
    @ReadTimeout.setter
    def ReadTimeout(self, value: int) -> None: ...
    @property
    def WriteTimeout(self) -> int:
        """

        :return:
        """
    @WriteTimeout.setter
    def WriteTimeout(self, value: int) -> None: ...
    def BeginRead(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """

        :param buffer:
        :param offset:
        :param count:
        :param callback:
        :param state:
        :return:
        """
    def BeginWrite(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """

        :param buffer:
        :param offset:
        :param count:
        :param callback:
        :param state:
        :return:
        """
    def Close(self) -> None:
        """"""
    def CloseEx(self, closeState: CloseExState) -> None:
        """

        :param closeState:
        """
    @overload
    def CopyTo(self, destination: Stream) -> None:
        """

        :param destination:
        """
    @overload
    def CopyTo(self, destination: Stream, bufferSize: int) -> None:
        """

        :param destination:
        :param bufferSize:
        """
    @overload
    def CopyToAsync(self, destination: Stream) -> Task:
        """

        :param destination:
        :return:
        """
    @overload
    def CopyToAsync(self, destination: Stream, bufferSize: int) -> Task:
        """

        :param destination:
        :param bufferSize:
        :return:
        """
    @overload
    def CopyToAsync(
        self, destination: Stream, bufferSize: int, cancellationToken: CancellationToken
    ) -> Task:
        """

        :param destination:
        :param bufferSize:
        :param cancellationToken:
        :return:
        """
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """

        :param requestedType:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    def EndRead(self, asyncResult: IAsyncResult) -> int:
        """

        :param asyncResult:
        :return:
        """
    def EndWrite(self, asyncResult: IAsyncResult) -> None:
        """

        :param asyncResult:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def Flush(self) -> None:
        """"""
    @overload
    def FlushAsync(self) -> Task:
        """

        :return:
        """
    @overload
    def FlushAsync(self, cancellationToken: CancellationToken) -> Task:
        """

        :param cancellationToken:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetLifetimeService(self) -> object:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def InitializeLifetimeService(self) -> object:
        """

        :return:
        """
    def Read(self, buffer: Array[int], offset: int, count: int) -> Tuple[int, Array[int]]:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def ReadAsync(self, buffer: Array[int], offset: int, count: int) -> Task[int]:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def ReadAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task[int]:
        """

        :param buffer:
        :param offset:
        :param count:
        :param cancellationToken:
        :return:
        """
    def ReadByte(self) -> int:
        """

        :return:
        """
    def Seek(self, offset: int, origin: SeekOrigin) -> int:
        """

        :param offset:
        :param origin:
        :return:
        """
    def SetLength(self, value: int) -> None:
        """

        :param value:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Write(self, buffer: Array[int], offset: int, count: int) -> None:
        """

        :param buffer:
        :param offset:
        :param count:
        """
    @overload
    def WriteAsync(self, buffer: Array[int], offset: int, count: int) -> Task:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def WriteAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task:
        """

        :param buffer:
        :param offset:
        :param count:
        :param cancellationToken:
        :return:
        """
    def WriteByte(self, value: int) -> None:
        """

        :param value:
        """

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
        """

        :return:
        """
    @AuthenticationLevel.setter
    def AuthenticationLevel(self, value: AuthenticationLevel) -> None: ...
    @property
    def CachePolicy(self) -> RequestCachePolicy:
        """

        :return:
        """
    @CachePolicy.setter
    def CachePolicy(self, value: RequestCachePolicy) -> None: ...
    @property
    def ClientCertificates(self) -> X509CertificateCollection:
        """

        :return:
        """
    @ClientCertificates.setter
    def ClientCertificates(self, value: X509CertificateCollection) -> None: ...
    @property
    def ConnectionGroupName(self) -> str:
        """

        :return:
        """
    @ConnectionGroupName.setter
    def ConnectionGroupName(self, value: str) -> None: ...
    @property
    def ContentLength(self) -> int:
        """

        :return:
        """
    @ContentLength.setter
    def ContentLength(self, value: int) -> None: ...
    @property
    def ContentOffset(self) -> int:
        """

        :return:
        """
    @ContentOffset.setter
    def ContentOffset(self, value: int) -> None: ...
    @property
    def ContentType(self) -> str:
        """

        :return:
        """
    @ContentType.setter
    def ContentType(self, value: str) -> None: ...
    @property
    def CreatorInstance(self) -> IWebRequestCreate:
        """

        :return:
        """
    @property
    def Credentials(self) -> ICredentials:
        """

        :return:
        """
    @Credentials.setter
    def Credentials(self, value: ICredentials) -> None: ...
    @classmethod
    @property
    def DefaultCachePolicy(cls) -> RequestCachePolicy:
        """

        :return:
        """
    @classmethod
    @DefaultCachePolicy.setter
    def DefaultCachePolicy(cls, value: RequestCachePolicy) -> None: ...
    @classmethod
    @property
    def DefaultWebProxy(cls) -> IWebProxy:
        """

        :return:
        """
    @classmethod
    @DefaultWebProxy.setter
    def DefaultWebProxy(cls, value: IWebProxy) -> None: ...
    @property
    def EnableSsl(self) -> bool:
        """

        :return:
        """
    @EnableSsl.setter
    def EnableSsl(self, value: bool) -> None: ...
    @property
    def Headers(self) -> WebHeaderCollection:
        """

        :return:
        """
    @Headers.setter
    def Headers(self, value: WebHeaderCollection) -> None: ...
    @property
    def ImpersonationLevel(self) -> TokenImpersonationLevel:
        """

        :return:
        """
    @ImpersonationLevel.setter
    def ImpersonationLevel(self, value: TokenImpersonationLevel) -> None: ...
    @property
    def KeepAlive(self) -> bool:
        """

        :return:
        """
    @KeepAlive.setter
    def KeepAlive(self, value: bool) -> None: ...
    @property
    def Method(self) -> str:
        """

        :return:
        """
    @Method.setter
    def Method(self, value: str) -> None: ...
    @property
    def PreAuthenticate(self) -> bool:
        """

        :return:
        """
    @PreAuthenticate.setter
    def PreAuthenticate(self, value: bool) -> None: ...
    @property
    def Proxy(self) -> IWebProxy:
        """

        :return:
        """
    @Proxy.setter
    def Proxy(self, value: IWebProxy) -> None: ...
    @property
    def ReadWriteTimeout(self) -> int:
        """

        :return:
        """
    @ReadWriteTimeout.setter
    def ReadWriteTimeout(self, value: int) -> None: ...
    @property
    def RenameTo(self) -> str:
        """

        :return:
        """
    @RenameTo.setter
    def RenameTo(self, value: str) -> None: ...
    @property
    def RequestUri(self) -> Uri:
        """

        :return:
        """
    @property
    def ServicePoint(self) -> ServicePoint:
        """

        :return:
        """
    @property
    def Timeout(self) -> int:
        """

        :return:
        """
    @Timeout.setter
    def Timeout(self, value: int) -> None: ...
    @property
    def UseBinary(self) -> bool:
        """

        :return:
        """
    @UseBinary.setter
    def UseBinary(self, value: bool) -> None: ...
    @property
    def UseDefaultCredentials(self) -> bool:
        """

        :return:
        """
    @UseDefaultCredentials.setter
    def UseDefaultCredentials(self, value: bool) -> None: ...
    @property
    def UsePassive(self) -> bool:
        """

        :return:
        """
    @UsePassive.setter
    def UsePassive(self, value: bool) -> None: ...
    def Abort(self) -> None:
        """"""
    def BeginGetRequestStream(self, callback: AsyncCallback, state: object) -> IAsyncResult:
        """

        :param callback:
        :param state:
        :return:
        """
    def BeginGetResponse(self, callback: AsyncCallback, state: object) -> IAsyncResult:
        """

        :param callback:
        :param state:
        :return:
        """
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """

        :param requestedType:
        :return:
        """
    def EndGetRequestStream(self, asyncResult: IAsyncResult) -> Stream:
        """

        :param asyncResult:
        :return:
        """
    def EndGetResponse(self, asyncResult: IAsyncResult) -> WebResponse:
        """

        :param asyncResult:
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
    def GetLifetimeService(self) -> object:
        """

        :return:
        """
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    def GetRequestStream(self) -> Stream:
        """

        :return:
        """
    def GetRequestStreamAsync(self) -> Task[Stream]:
        """

        :return:
        """
    def GetResponse(self) -> WebResponse:
        """

        :return:
        """
    def GetResponseAsync(self) -> Task[WebResponse]:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def InitializeLifetimeService(self) -> object:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class FtpWebRequestCreator(Object, IWebRequestCreate):
    """"""

    def Create(self, uri: Uri) -> WebRequest:
        """

        :param uri:
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

class FtpWebResponse(WebResponse, ISerializable, IDisposable):
    """"""

    @property
    def BannerMessage(self) -> str:
        """

        :return:
        """
    @property
    def ContentLength(self) -> int:
        """

        :return:
        """
    @ContentLength.setter
    def ContentLength(self, value: int) -> None: ...
    @property
    def ContentType(self) -> str:
        """

        :return:
        """
    @ContentType.setter
    def ContentType(self, value: str) -> None: ...
    @property
    def ExitMessage(self) -> str:
        """

        :return:
        """
    @property
    def Headers(self) -> WebHeaderCollection:
        """

        :return:
        """
    @property
    def IsFromCache(self) -> bool:
        """

        :return:
        """
    @property
    def IsMutuallyAuthenticated(self) -> bool:
        """

        :return:
        """
    @property
    def LastModified(self) -> DateTime:
        """

        :return:
        """
    @property
    def ResponseUri(self) -> Uri:
        """

        :return:
        """
    @property
    def StatusCode(self) -> FtpStatusCode:
        """

        :return:
        """
    @property
    def StatusDescription(self) -> str:
        """

        :return:
        """
    @property
    def SupportsHeaders(self) -> bool:
        """

        :return:
        """
    @property
    def WelcomeMessage(self) -> str:
        """

        :return:
        """
    def Close(self) -> None:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """

        :param requestedType:
        :return:
        """
    def Dispose(self) -> None:
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
    def GetLifetimeService(self) -> object:
        """

        :return:
        """
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    def GetResponseStream(self) -> Stream:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def InitializeLifetimeService(self) -> object:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class GZipWrapperStream(GZipStream, ICloseEx, IRequestLifetimeTracker, IDisposable):
    """"""

    def __init__(self, stream: Stream, mode: CompressionMode):
        """

        :param stream:
        :param mode:
        """
    @property
    def BaseStream(self) -> Stream:
        """

        :return:
        """
    @property
    def CanRead(self) -> bool:
        """

        :return:
        """
    @property
    def CanSeek(self) -> bool:
        """

        :return:
        """
    @property
    def CanTimeout(self) -> bool:
        """

        :return:
        """
    @property
    def CanWrite(self) -> bool:
        """

        :return:
        """
    @property
    def Length(self) -> int:
        """

        :return:
        """
    @property
    def Position(self) -> int:
        """

        :return:
        """
    @Position.setter
    def Position(self, value: int) -> None: ...
    @property
    def ReadTimeout(self) -> int:
        """

        :return:
        """
    @ReadTimeout.setter
    def ReadTimeout(self, value: int) -> None: ...
    @property
    def WriteTimeout(self) -> int:
        """

        :return:
        """
    @WriteTimeout.setter
    def WriteTimeout(self, value: int) -> None: ...
    def BeginRead(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """

        :param buffer:
        :param offset:
        :param count:
        :param callback:
        :param state:
        :return:
        """
    def BeginWrite(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """

        :param buffer:
        :param offset:
        :param count:
        :param callback:
        :param state:
        :return:
        """
    def Close(self) -> None:
        """"""
    def CloseEx(self, closeState: CloseExState) -> None:
        """

        :param closeState:
        """
    @overload
    def CopyTo(self, destination: Stream) -> None:
        """

        :param destination:
        """
    @overload
    def CopyTo(self, destination: Stream, bufferSize: int) -> None:
        """

        :param destination:
        :param bufferSize:
        """
    @overload
    def CopyToAsync(self, destination: Stream) -> Task:
        """

        :param destination:
        :return:
        """
    @overload
    def CopyToAsync(self, destination: Stream, bufferSize: int) -> Task:
        """

        :param destination:
        :param bufferSize:
        :return:
        """
    @overload
    def CopyToAsync(
        self, destination: Stream, bufferSize: int, cancellationToken: CancellationToken
    ) -> Task:
        """

        :param destination:
        :param bufferSize:
        :param cancellationToken:
        :return:
        """
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """

        :param requestedType:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    def EndRead(self, asyncResult: IAsyncResult) -> int:
        """

        :param asyncResult:
        :return:
        """
    def EndWrite(self, asyncResult: IAsyncResult) -> None:
        """

        :param asyncResult:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def Flush(self) -> None:
        """"""
    @overload
    def FlushAsync(self) -> Task:
        """

        :return:
        """
    @overload
    def FlushAsync(self, cancellationToken: CancellationToken) -> Task:
        """

        :param cancellationToken:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetLifetimeService(self) -> object:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def InitializeLifetimeService(self) -> object:
        """

        :return:
        """
    def Read(self, buffer: Array[int], offset: int, count: int) -> Tuple[int, Array[int]]:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def ReadAsync(self, buffer: Array[int], offset: int, count: int) -> Task[int]:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def ReadAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task[int]:
        """

        :param buffer:
        :param offset:
        :param count:
        :param cancellationToken:
        :return:
        """
    def ReadByte(self) -> int:
        """

        :return:
        """
    def Seek(self, offset: int, origin: SeekOrigin) -> int:
        """

        :param offset:
        :param origin:
        :return:
        """
    def SetLength(self, value: int) -> None:
        """

        :param value:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def TrackRequestLifetime(self, requestStartTimestamp: int) -> None:
        """

        :param requestStartTimestamp:
        """
    def Write(self, buffer: Array[int], offset: int, count: int) -> None:
        """

        :param buffer:
        :param offset:
        :param count:
        """
    @overload
    def WriteAsync(self, buffer: Array[int], offset: int, count: int) -> Task:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def WriteAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task:
        """

        :param buffer:
        :param offset:
        :param count:
        :param cancellationToken:
        :return:
        """
    def WriteByte(self, value: int) -> None:
        """

        :param value:
        """

GeneralAsyncDelegate: Callable[[object, object], None] = ...
"""

:param request: 
:param state: 
"""

class GlobalLog(ABC, Object):
    """"""

    @classmethod
    def AddToArray(cls, msg: str) -> None:
        """

        :param msg:
        """
    @classmethod
    @overload
    def Assert(cls, message: str) -> None:
        """

        :param message:
        """
    @classmethod
    @overload
    def Assert(cls, message: str, detailMessage: str) -> None:
        """

        :param message:
        :param detailMessage:
        """
    @classmethod
    @overload
    def Assert(cls, condition: bool, messageFormat: str, data: Array[object]) -> None:
        """

        :param condition:
        :param messageFormat:
        :param data:
        """
    @classmethod
    @overload
    def Dump(cls, buffer: Array[int]) -> None:
        """

        :param buffer:
        """
    @classmethod
    @overload
    def Dump(cls, buffer: Array[int], length: int) -> None:
        """

        :param buffer:
        :param length:
        """
    @classmethod
    @overload
    def Dump(cls, buffer: Array[int], offset: int, length: int) -> None:
        """

        :param buffer:
        :param offset:
        :param length:
        """
    @classmethod
    @overload
    def Dump(cls, buffer: IntPtr, offset: int, length: int) -> None:
        """

        :param buffer:
        :param offset:
        :param length:
        """
    @classmethod
    def DumpArray(cls) -> None:
        """"""
    @classmethod
    @overload
    def Enter(cls, func: str) -> None:
        """

        :param func:
        """
    @classmethod
    @overload
    def Enter(cls, func: str, parms: str) -> None:
        """

        :param func:
        :param parms:
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
    @classmethod
    def Ignore(cls, msg: object) -> None:
        """

        :param msg:
        """
    @classmethod
    @overload
    def Leave(cls, func: str) -> None:
        """

        :param func:
        """
    @classmethod
    @overload
    def Leave(cls, func: str, returnval: bool) -> None:
        """

        :param func:
        :param returnval:
        """
    @classmethod
    @overload
    def Leave(cls, func: str, returnval: int) -> None:
        """

        :param func:
        :param returnval:
        """
    @classmethod
    @overload
    def Leave(cls, func: str, result: str) -> None:
        """

        :param func:
        :param result:
        """
    @classmethod
    def LeaveException(cls, func: str, exception: Exception) -> None:
        """

        :param func:
        :param exception:
        """
    @classmethod
    def Print(cls, msg: str) -> None:
        """

        :param msg:
        """
    @classmethod
    def PrintHex(cls, msg: str, value: object) -> None:
        """

        :param msg:
        :param value:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class GlobalProxySelection(Object):
    """"""

    def __init__(self):
        """"""
    @classmethod
    @property
    def Select(cls) -> IWebProxy:
        """

        :return:
        """
    @classmethod
    @Select.setter
    def Select(cls, value: IWebProxy) -> None: ...
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @classmethod
    def GetEmptyWebProxy(cls) -> IWebProxy:
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

class GlobalSSPI(ABC, Object):
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

class HeaderInfo(Object):
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

class HeaderInfoTable(Object):
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

HeaderParser: Callable[[str], Array[str]] = ...
"""

:param value: 
:return: 
"""

class HeaderVariantInfo(ValueType):
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

class HostHeaderString(Object):
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

HttpAbortDelegate: Callable[[HttpWebRequest, WebException], bool] = ...
"""

:param request: 
:param webException: 
:return: 
"""

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

HttpContinueDelegate: Callable[[int, WebHeaderCollection], None] = ...
"""

:param StatusCode: 
:param httpHeaders: 
"""

class HttpDateParse(ABC, Object):
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
    @classmethod
    def ParseHttpDate(cls, DateString: str, dtOut: DateTime) -> Tuple[bool, DateTime]:
        """

        :param DateString:
        :param dtOut:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class HttpDigest(ABC, Object):
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

class HttpDigestChallenge(Object):
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
    def defineAttribute(self, name: str, value: str) -> bool:
        """

        :param name:
        :param value:
        :return:
        """

class HttpKnownHeaderNames(ABC, Object):
    """"""

    Accept: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    AcceptCharset: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    AcceptEncoding: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    AcceptLanguage: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    AcceptRanges: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Age: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Allow: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Authorization: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    CacheControl: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Connection: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    ContentDisposition: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    ContentEncoding: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    ContentLanguage: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    ContentLength: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    ContentLocation: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    ContentMD5: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    ContentRange: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    ContentType: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Cookie: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Cookie2: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Date: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    ETag: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Expect: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Expires: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    From: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Host: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    IfMatch: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    IfModifiedSince: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    IfNoneMatch: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    IfRange: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    IfUnmodifiedSince: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    KeepAlive: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    LastModified: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Location: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    MaxForwards: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Origin: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    P3P: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Pragma: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    ProxyAuthenticate: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    ProxyAuthorization: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    ProxyConnection: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Range: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Referer: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    RetryAfter: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    SecWebSocketAccept: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    SecWebSocketExtensions: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    SecWebSocketKey: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    SecWebSocketProtocol: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    SecWebSocketVersion: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Server: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    SetCookie: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    SetCookie2: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    TE: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Trailer: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    TransferEncoding: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Upgrade: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    UserAgent: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Vary: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Via: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    WWWAuthenticate: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Warning: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    XAspNetVersion: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    XPoweredBy: Final[ClassVar[str]] = ...
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

class HttpListener(Object, IDisposable):
    """"""

    def __init__(self):
        """"""
    @property
    def AuthenticationSchemeSelectorDelegate(self) -> AuthenticationSchemeSelector:
        """

        :return:
        """
    @AuthenticationSchemeSelectorDelegate.setter
    def AuthenticationSchemeSelectorDelegate(self, value: AuthenticationSchemeSelector) -> None: ...
    @property
    def AuthenticationSchemes(self) -> AuthenticationSchemes:
        """

        :return:
        """
    @AuthenticationSchemes.setter
    def AuthenticationSchemes(self, value: AuthenticationSchemes) -> None: ...
    @property
    def DefaultServiceNames(self) -> ServiceNameCollection:
        """

        :return:
        """
    @property
    def ExtendedProtectionPolicy(self) -> ExtendedProtectionPolicy:
        """

        :return:
        """
    @ExtendedProtectionPolicy.setter
    def ExtendedProtectionPolicy(self, value: ExtendedProtectionPolicy) -> None: ...
    @property
    def ExtendedProtectionSelectorDelegate(self) -> HttpListener.ExtendedProtectionSelector:
        """

        :return:
        """
    @ExtendedProtectionSelectorDelegate.setter
    def ExtendedProtectionSelectorDelegate(
        self, value: HttpListener.ExtendedProtectionSelector
    ) -> None: ...
    @property
    def IgnoreWriteExceptions(self) -> bool:
        """

        :return:
        """
    @IgnoreWriteExceptions.setter
    def IgnoreWriteExceptions(self, value: bool) -> None: ...
    @property
    def IsListening(self) -> bool:
        """

        :return:
        """
    @classmethod
    @property
    def IsSupported(cls) -> bool:
        """

        :return:
        """
    @property
    def Prefixes(self) -> HttpListenerPrefixCollection:
        """

        :return:
        """
    @property
    def Realm(self) -> str:
        """

        :return:
        """
    @Realm.setter
    def Realm(self, value: str) -> None: ...
    @property
    def TimeoutManager(self) -> HttpListenerTimeoutManager:
        """

        :return:
        """
    @property
    def UnsafeConnectionNtlmAuthentication(self) -> bool:
        """

        :return:
        """
    @UnsafeConnectionNtlmAuthentication.setter
    def UnsafeConnectionNtlmAuthentication(self, value: bool) -> None: ...
    def Abort(self) -> None:
        """"""
    def BeginGetContext(self, callback: AsyncCallback, state: object) -> IAsyncResult:
        """

        :param callback:
        :param state:
        :return:
        """
    def Close(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def EndGetContext(self, asyncResult: IAsyncResult) -> HttpListenerContext:
        """

        :param asyncResult:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetContext(self) -> HttpListenerContext:
        """

        :return:
        """
    def GetContextAsync(self) -> Task[HttpListenerContext]:
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
    def Start(self) -> None:
        """"""
    def Stop(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """
    ExtendedProtectionSelector: Callable[[HttpListenerRequest], ExtendedProtectionPolicy] = ...
    """
    
    :param request: 
    :return: 
    """

class HttpListenerBasicIdentity(GenericIdentity, IIdentity):
    """"""

    def __init__(self, username: str, password: str):
        """

        :param username:
        :param password:
        """
    @property
    def Actor(self) -> ClaimsIdentity:
        """

        :return:
        """
    @Actor.setter
    def Actor(self, value: ClaimsIdentity) -> None: ...
    @property
    def AuthenticationType(self) -> str:
        """

        :return:
        """
    @property
    def BootstrapContext(self) -> object:
        """

        :return:
        """
    @BootstrapContext.setter
    def BootstrapContext(self, value: object) -> None: ...
    @property
    def Claims(self) -> IEnumerable[Claim]:
        """

        :return:
        """
    @property
    def IsAuthenticated(self) -> bool:
        """

        :return:
        """
    @property
    def Label(self) -> str:
        """

        :return:
        """
    @Label.setter
    def Label(self, value: str) -> None: ...
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def NameClaimType(self) -> str:
        """

        :return:
        """
    @property
    def Password(self) -> str:
        """

        :return:
        """
    @property
    def RoleClaimType(self) -> str:
        """

        :return:
        """
    def AddClaim(self, claim: Claim) -> None:
        """

        :param claim:
        """
    def AddClaims(self, claims: IEnumerable[Claim]) -> None:
        """

        :param claims:
        """
    def Clone(self) -> ClaimsIdentity:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def FindAll(self, match: Predicate[Claim]) -> IEnumerable[Claim]:
        """

        :param match:
        :return:
        """
    @overload
    def FindAll(self, type: str) -> IEnumerable[Claim]:
        """

        :param type:
        :return:
        """
    @overload
    def FindFirst(self, match: Predicate[Claim]) -> Claim:
        """

        :param match:
        :return:
        """
    @overload
    def FindFirst(self, type: str) -> Claim:
        """

        :param type:
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
    @overload
    def HasClaim(self, match: Predicate[Claim]) -> bool:
        """

        :param match:
        :return:
        """
    @overload
    def HasClaim(self, type: str, value: str) -> bool:
        """

        :param type:
        :param value:
        :return:
        """
    def RemoveClaim(self, claim: Claim) -> None:
        """

        :param claim:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def TryRemoveClaim(self, claim: Claim) -> bool:
        """

        :param claim:
        :return:
        """
    def WriteTo(self, writer: BinaryWriter) -> None:
        """

        :param writer:
        """

class HttpListenerContext(Object):
    """"""

    @property
    def Request(self) -> HttpListenerRequest:
        """

        :return:
        """
    @property
    def Response(self) -> HttpListenerResponse:
        """

        :return:
        """
    @property
    def User(self) -> IPrincipal:
        """

        :return:
        """
    @overload
    def AcceptWebSocketAsync(self, subProtocol: str) -> Task[HttpListenerWebSocketContext]:
        """

        :param subProtocol:
        :return:
        """
    @overload
    def AcceptWebSocketAsync(
        self, subProtocol: str, keepAliveInterval: TimeSpan
    ) -> Task[HttpListenerWebSocketContext]:
        """

        :param subProtocol:
        :param keepAliveInterval:
        :return:
        """
    @overload
    def AcceptWebSocketAsync(
        self, subProtocol: str, receiveBufferSize: int, keepAliveInterval: TimeSpan
    ) -> Task[HttpListenerWebSocketContext]:
        """

        :param subProtocol:
        :param receiveBufferSize:
        :param keepAliveInterval:
        :return:
        """
    @overload
    def AcceptWebSocketAsync(
        self,
        subProtocol: str,
        receiveBufferSize: int,
        keepAliveInterval: TimeSpan,
        internalBuffer: ArraySegment[int],
    ) -> Task[HttpListenerWebSocketContext]:
        """

        :param subProtocol:
        :param receiveBufferSize:
        :param keepAliveInterval:
        :param internalBuffer:
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

class HttpListenerException(Win32Exception, _Exception, ISerializable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, errorCode: int):
        """

        :param errorCode:
        """
    @overload
    def __init__(self, errorCode: int, message: str):
        """

        :param errorCode:
        :param message:
        """
    @property
    def Data(self) -> IDictionary:
        """

        :return:
        """
    @property
    def ErrorCode(self) -> int:
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
    def NativeErrorCode(self) -> int:
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

class HttpListenerPrefixCollection(Object, ICollection[String], IEnumerable[String], IEnumerable):
    """"""

    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def IsSynchronized(self) -> bool:
        """

        :return:
        """
    def Add(self, item: str) -> None:
        """

        :param item:
        """
    def Clear(self) -> None:
        """"""
    def Contains(self, item: str) -> bool:
        """

        :param item:
        :return:
        """
    @overload
    def CopyTo(self, array: Array, offset: int) -> None:
        """

        :param array:
        :param offset:
        """
    @overload
    def CopyTo(self, array: Array[str], arrayIndex: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
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
    def Remove(self, item: str) -> bool:
        """

        :param item:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def __contains__(self, value: str) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[str]:
        """

        :return:
        """
    def __len__(self) -> int:
        """

        :return:
        """

class HttpListenerRequest(Object):
    """"""

    @property
    def AcceptTypes(self) -> Array[str]:
        """

        :return:
        """
    @property
    def ClientCertificateError(self) -> int:
        """

        :return:
        """
    @property
    def ContentEncoding(self) -> Encoding:
        """

        :return:
        """
    @property
    def ContentLength64(self) -> int:
        """

        :return:
        """
    @property
    def ContentType(self) -> str:
        """

        :return:
        """
    @property
    def Cookies(self) -> CookieCollection:
        """

        :return:
        """
    @property
    def HasEntityBody(self) -> bool:
        """

        :return:
        """
    @property
    def Headers(self) -> NameValueCollection:
        """

        :return:
        """
    @property
    def HttpMethod(self) -> str:
        """

        :return:
        """
    @property
    def InputStream(self) -> Stream:
        """

        :return:
        """
    @property
    def IsAuthenticated(self) -> bool:
        """

        :return:
        """
    @property
    def IsLocal(self) -> bool:
        """

        :return:
        """
    @property
    def IsSecureConnection(self) -> bool:
        """

        :return:
        """
    @property
    def IsWebSocketRequest(self) -> bool:
        """

        :return:
        """
    @property
    def KeepAlive(self) -> bool:
        """

        :return:
        """
    @property
    def LocalEndPoint(self) -> IPEndPoint:
        """

        :return:
        """
    @property
    def ProtocolVersion(self) -> Version:
        """

        :return:
        """
    @property
    def QueryString(self) -> NameValueCollection:
        """

        :return:
        """
    @property
    def RawUrl(self) -> str:
        """

        :return:
        """
    @property
    def RemoteEndPoint(self) -> IPEndPoint:
        """

        :return:
        """
    @property
    def RequestTraceIdentifier(self) -> Guid:
        """

        :return:
        """
    @property
    def ServiceName(self) -> str:
        """

        :return:
        """
    @property
    def TransportContext(self) -> TransportContext:
        """

        :return:
        """
    @property
    def Url(self) -> Uri:
        """

        :return:
        """
    @property
    def UrlReferrer(self) -> Uri:
        """

        :return:
        """
    @property
    def UserAgent(self) -> str:
        """

        :return:
        """
    @property
    def UserHostAddress(self) -> str:
        """

        :return:
        """
    @property
    def UserHostName(self) -> str:
        """

        :return:
        """
    @property
    def UserLanguages(self) -> Array[str]:
        """

        :return:
        """
    def BeginGetClientCertificate(
        self, requestCallback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """

        :param requestCallback:
        :param state:
        :return:
        """
    def EndGetClientCertificate(self, asyncResult: IAsyncResult) -> X509Certificate2:
        """

        :param asyncResult:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetClientCertificate(self) -> X509Certificate2:
        """

        :return:
        """
    def GetClientCertificateAsync(self) -> Task[X509Certificate2]:
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

class HttpListenerRequestContext(TransportContext):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetChannelBinding(self, kind: ChannelBindingKind) -> ChannelBinding:
        """

        :param kind:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetTlsTokenBindings(self) -> IEnumerable[TokenBinding]:
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

class HttpListenerRequestUriBuilder(Object):
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
    @classmethod
    def GetRequestUri(
        cls,
        rawUri: str,
        cookedUriScheme: str,
        cookedUriHost: str,
        cookedUriPath: str,
        cookedUriQuery: str,
    ) -> Uri:
        """

        :param rawUri:
        :param cookedUriScheme:
        :param cookedUriHost:
        :param cookedUriPath:
        :param cookedUriQuery:
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

class HttpListenerResponse(Object, IDisposable):
    """"""

    @property
    def ContentEncoding(self) -> Encoding:
        """

        :return:
        """
    @ContentEncoding.setter
    def ContentEncoding(self, value: Encoding) -> None: ...
    @property
    def ContentLength64(self) -> int:
        """

        :return:
        """
    @ContentLength64.setter
    def ContentLength64(self, value: int) -> None: ...
    @property
    def ContentType(self) -> str:
        """

        :return:
        """
    @ContentType.setter
    def ContentType(self, value: str) -> None: ...
    @property
    def Cookies(self) -> CookieCollection:
        """

        :return:
        """
    @Cookies.setter
    def Cookies(self, value: CookieCollection) -> None: ...
    @property
    def Headers(self) -> WebHeaderCollection:
        """

        :return:
        """
    @Headers.setter
    def Headers(self, value: WebHeaderCollection) -> None: ...
    @property
    def KeepAlive(self) -> bool:
        """

        :return:
        """
    @KeepAlive.setter
    def KeepAlive(self, value: bool) -> None: ...
    @property
    def OutputStream(self) -> Stream:
        """

        :return:
        """
    @property
    def ProtocolVersion(self) -> Version:
        """

        :return:
        """
    @ProtocolVersion.setter
    def ProtocolVersion(self, value: Version) -> None: ...
    @property
    def RedirectLocation(self) -> str:
        """

        :return:
        """
    @RedirectLocation.setter
    def RedirectLocation(self, value: str) -> None: ...
    @property
    def SendChunked(self) -> bool:
        """

        :return:
        """
    @SendChunked.setter
    def SendChunked(self, value: bool) -> None: ...
    @property
    def StatusCode(self) -> int:
        """

        :return:
        """
    @StatusCode.setter
    def StatusCode(self, value: int) -> None: ...
    @property
    def StatusDescription(self) -> str:
        """

        :return:
        """
    @StatusDescription.setter
    def StatusDescription(self, value: str) -> None: ...
    def Abort(self) -> None:
        """"""
    def AddHeader(self, name: str, value: str) -> None:
        """

        :param name:
        :param value:
        """
    def AppendCookie(self, cookie: Cookie) -> None:
        """

        :param cookie:
        """
    def AppendHeader(self, name: str, value: str) -> None:
        """

        :param name:
        :param value:
        """
    @overload
    def Close(self) -> None:
        """"""
    @overload
    def Close(self, responseEntity: Array[int], willBlock: bool) -> None:
        """

        :param responseEntity:
        :param willBlock:
        """
    def CopyFrom(self, templateResponse: HttpListenerResponse) -> None:
        """

        :param templateResponse:
        """
    def Dispose(self) -> None:
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
    def Redirect(self, url: str) -> None:
        """

        :param url:
        """
    def SetCookie(self, cookie: Cookie) -> None:
        """

        :param cookie:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class HttpListenerTimeoutManager(Object):
    """"""

    @property
    def DrainEntityBody(self) -> TimeSpan:
        """

        :return:
        """
    @DrainEntityBody.setter
    def DrainEntityBody(self, value: TimeSpan) -> None: ...
    @property
    def EntityBody(self) -> TimeSpan:
        """

        :return:
        """
    @EntityBody.setter
    def EntityBody(self, value: TimeSpan) -> None: ...
    @property
    def HeaderWait(self) -> TimeSpan:
        """

        :return:
        """
    @HeaderWait.setter
    def HeaderWait(self, value: TimeSpan) -> None: ...
    @property
    def IdleConnection(self) -> TimeSpan:
        """

        :return:
        """
    @IdleConnection.setter
    def IdleConnection(self, value: TimeSpan) -> None: ...
    @property
    def MinSendBytesPerSecond(self) -> int:
        """

        :return:
        """
    @MinSendBytesPerSecond.setter
    def MinSendBytesPerSecond(self, value: int) -> None: ...
    @property
    def RequestQueue(self) -> TimeSpan:
        """

        :return:
        """
    @RequestQueue.setter
    def RequestQueue(self, value: TimeSpan) -> None: ...
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

class HttpRequestCreator(Object, IWebRequestCreate):
    """"""

    def __init__(self):
        """"""
    def Create(self, uri: Uri) -> WebRequest:
        """

        :param uri:
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
        """

        :return:
        """
    @property
    def IsInvalid(self) -> bool:
        """

        :return:
        """
    def Close(self) -> None:
        """"""
    def Dispose(self) -> None:
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
    def SetHandleAsInvalid(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class HttpRequestStream(Stream, IDisposable):
    """"""

    @property
    def CanRead(self) -> bool:
        """

        :return:
        """
    @property
    def CanSeek(self) -> bool:
        """

        :return:
        """
    @property
    def CanTimeout(self) -> bool:
        """

        :return:
        """
    @property
    def CanWrite(self) -> bool:
        """

        :return:
        """
    @property
    def Length(self) -> int:
        """

        :return:
        """
    @property
    def Position(self) -> int:
        """

        :return:
        """
    @Position.setter
    def Position(self, value: int) -> None: ...
    @property
    def ReadTimeout(self) -> int:
        """

        :return:
        """
    @ReadTimeout.setter
    def ReadTimeout(self, value: int) -> None: ...
    @property
    def WriteTimeout(self) -> int:
        """

        :return:
        """
    @WriteTimeout.setter
    def WriteTimeout(self, value: int) -> None: ...
    def BeginRead(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """

        :param buffer:
        :param offset:
        :param count:
        :param callback:
        :param state:
        :return:
        """
    def BeginWrite(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """

        :param buffer:
        :param offset:
        :param count:
        :param callback:
        :param state:
        :return:
        """
    def Close(self) -> None:
        """"""
    @overload
    def CopyTo(self, destination: Stream) -> None:
        """

        :param destination:
        """
    @overload
    def CopyTo(self, destination: Stream, bufferSize: int) -> None:
        """

        :param destination:
        :param bufferSize:
        """
    @overload
    def CopyToAsync(self, destination: Stream) -> Task:
        """

        :param destination:
        :return:
        """
    @overload
    def CopyToAsync(self, destination: Stream, bufferSize: int) -> Task:
        """

        :param destination:
        :param bufferSize:
        :return:
        """
    @overload
    def CopyToAsync(
        self, destination: Stream, bufferSize: int, cancellationToken: CancellationToken
    ) -> Task:
        """

        :param destination:
        :param bufferSize:
        :param cancellationToken:
        :return:
        """
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """

        :param requestedType:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    def EndRead(self, asyncResult: IAsyncResult) -> int:
        """

        :param asyncResult:
        :return:
        """
    def EndWrite(self, asyncResult: IAsyncResult) -> None:
        """

        :param asyncResult:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def Flush(self) -> None:
        """"""
    @overload
    def FlushAsync(self) -> Task:
        """

        :return:
        """
    @overload
    def FlushAsync(self, cancellationToken: CancellationToken) -> Task:
        """

        :param cancellationToken:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetLifetimeService(self) -> object:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def InitializeLifetimeService(self) -> object:
        """

        :return:
        """
    def Read(self, buffer: Array[int], offset: int, count: int) -> Tuple[int, Array[int]]:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def ReadAsync(self, buffer: Array[int], offset: int, count: int) -> Task[int]:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def ReadAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task[int]:
        """

        :param buffer:
        :param offset:
        :param count:
        :param cancellationToken:
        :return:
        """
    def ReadByte(self) -> int:
        """

        :return:
        """
    def Seek(self, offset: int, origin: SeekOrigin) -> int:
        """

        :param offset:
        :param origin:
        :return:
        """
    def SetLength(self, value: int) -> None:
        """

        :param value:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Write(self, buffer: Array[int], offset: int, count: int) -> None:
        """

        :param buffer:
        :param offset:
        :param count:
        """
    @overload
    def WriteAsync(self, buffer: Array[int], offset: int, count: int) -> Task:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def WriteAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task:
        """

        :param buffer:
        :param offset:
        :param count:
        :param cancellationToken:
        :return:
        """
    def WriteByte(self, value: int) -> None:
        """

        :param value:
        """

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
        """

        :return:
        """
    @property
    def CanSeek(self) -> bool:
        """

        :return:
        """
    @property
    def CanTimeout(self) -> bool:
        """

        :return:
        """
    @property
    def CanWrite(self) -> bool:
        """

        :return:
        """
    @property
    def Length(self) -> int:
        """

        :return:
        """
    @property
    def Position(self) -> int:
        """

        :return:
        """
    @Position.setter
    def Position(self, value: int) -> None: ...
    @property
    def ReadTimeout(self) -> int:
        """

        :return:
        """
    @ReadTimeout.setter
    def ReadTimeout(self, value: int) -> None: ...
    @property
    def WriteTimeout(self) -> int:
        """

        :return:
        """
    @WriteTimeout.setter
    def WriteTimeout(self, value: int) -> None: ...
    def BeginRead(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """

        :param buffer:
        :param offset:
        :param count:
        :param callback:
        :param state:
        :return:
        """
    def BeginWrite(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """

        :param buffer:
        :param offset:
        :param count:
        :param callback:
        :param state:
        :return:
        """
    def Close(self) -> None:
        """"""
    @overload
    def CopyTo(self, destination: Stream) -> None:
        """

        :param destination:
        """
    @overload
    def CopyTo(self, destination: Stream, bufferSize: int) -> None:
        """

        :param destination:
        :param bufferSize:
        """
    @overload
    def CopyToAsync(self, destination: Stream) -> Task:
        """

        :param destination:
        :return:
        """
    @overload
    def CopyToAsync(self, destination: Stream, bufferSize: int) -> Task:
        """

        :param destination:
        :param bufferSize:
        :return:
        """
    @overload
    def CopyToAsync(
        self, destination: Stream, bufferSize: int, cancellationToken: CancellationToken
    ) -> Task:
        """

        :param destination:
        :param bufferSize:
        :param cancellationToken:
        :return:
        """
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """

        :param requestedType:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    def EndRead(self, asyncResult: IAsyncResult) -> int:
        """

        :param asyncResult:
        :return:
        """
    def EndWrite(self, asyncResult: IAsyncResult) -> None:
        """

        :param asyncResult:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def Flush(self) -> None:
        """"""
    @overload
    def FlushAsync(self) -> Task:
        """

        :return:
        """
    @overload
    def FlushAsync(self, cancellationToken: CancellationToken) -> Task:
        """

        :param cancellationToken:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetLifetimeService(self) -> object:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def InitializeLifetimeService(self) -> object:
        """

        :return:
        """
    def Read(self, buffer: Array[int], offset: int, count: int) -> Tuple[int, Array[int]]:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def ReadAsync(self, buffer: Array[int], offset: int, count: int) -> Task[int]:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def ReadAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task[int]:
        """

        :param buffer:
        :param offset:
        :param count:
        :param cancellationToken:
        :return:
        """
    def ReadByte(self) -> int:
        """

        :return:
        """
    def Seek(self, offset: int, origin: SeekOrigin) -> int:
        """

        :param offset:
        :param origin:
        :return:
        """
    def SetLength(self, value: int) -> None:
        """

        :param value:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Write(self, buffer: Array[int], offset: int, count: int) -> None:
        """

        :param buffer:
        :param offset:
        :param count:
        """
    @overload
    def WriteAsync(self, buffer: Array[int], offset: int, count: int) -> Task:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def WriteAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task:
        """

        :param buffer:
        :param offset:
        :param count:
        :param cancellationToken:
        :return:
        """
    def WriteByte(self, value: int) -> None:
        """

        :param value:
        """

class HttpResponseStreamAsyncResult(LazyAsyncResult, IAsyncResult):
    """"""

    @property
    def AsyncState(self) -> object:
        """

        :return:
        """
    @property
    def AsyncWaitHandle(self) -> WaitHandle:
        """

        :return:
        """
    @property
    def CompletedSynchronously(self) -> bool:
        """

        :return:
        """
    @property
    def IsCompleted(self) -> bool:
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

class HttpServerSessionHandle(CriticalHandleZeroOrMinusOneIsInvalid, IDisposable):
    """"""

    @property
    def IsClosed(self) -> bool:
        """

        :return:
        """
    @property
    def IsInvalid(self) -> bool:
        """

        :return:
        """
    def Close(self) -> None:
        """"""
    def Dispose(self) -> None:
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
    def SetHandleAsInvalid(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

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

class HttpSysSettings(ABC, Object):
    """"""

    @classmethod
    @property
    def EnableNonUtf8(cls) -> bool:
        """

        :return:
        """
    @classmethod
    @property
    def FavorUtf8(cls) -> bool:
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

class HttpVersion(Object):
    """"""

    Version10: Final[ClassVar[Version]] = ...
    """
    
    :return: 
    """
    Version11: Final[ClassVar[Version]] = ...
    """
    
    :return: 
    """
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

class HttpWebRequest(WebRequest, ISerializable):
    """"""

    def __init__(self):
        """"""
    @property
    def Accept(self) -> str:
        """

        :return:
        """
    @Accept.setter
    def Accept(self, value: str) -> None: ...
    @property
    def Address(self) -> Uri:
        """

        :return:
        """
    @property
    def AllowAutoRedirect(self) -> bool:
        """

        :return:
        """
    @AllowAutoRedirect.setter
    def AllowAutoRedirect(self, value: bool) -> None: ...
    @property
    def AllowReadStreamBuffering(self) -> bool:
        """

        :return:
        """
    @AllowReadStreamBuffering.setter
    def AllowReadStreamBuffering(self, value: bool) -> None: ...
    @property
    def AllowWriteStreamBuffering(self) -> bool:
        """

        :return:
        """
    @AllowWriteStreamBuffering.setter
    def AllowWriteStreamBuffering(self, value: bool) -> None: ...
    @property
    def AuthenticationLevel(self) -> AuthenticationLevel:
        """

        :return:
        """
    @AuthenticationLevel.setter
    def AuthenticationLevel(self, value: AuthenticationLevel) -> None: ...
    @property
    def AutomaticDecompression(self) -> DecompressionMethods:
        """

        :return:
        """
    @AutomaticDecompression.setter
    def AutomaticDecompression(self, value: DecompressionMethods) -> None: ...
    @property
    def CachePolicy(self) -> RequestCachePolicy:
        """

        :return:
        """
    @CachePolicy.setter
    def CachePolicy(self, value: RequestCachePolicy) -> None: ...
    @property
    def ClientCertificates(self) -> X509CertificateCollection:
        """

        :return:
        """
    @ClientCertificates.setter
    def ClientCertificates(self, value: X509CertificateCollection) -> None: ...
    @property
    def Connection(self) -> str:
        """

        :return:
        """
    @Connection.setter
    def Connection(self, value: str) -> None: ...
    @property
    def ConnectionGroupName(self) -> str:
        """

        :return:
        """
    @ConnectionGroupName.setter
    def ConnectionGroupName(self, value: str) -> None: ...
    @property
    def ContentLength(self) -> int:
        """

        :return:
        """
    @ContentLength.setter
    def ContentLength(self, value: int) -> None: ...
    @property
    def ContentType(self) -> str:
        """

        :return:
        """
    @ContentType.setter
    def ContentType(self, value: str) -> None: ...
    @property
    def ContinueDelegate(self) -> HttpContinueDelegate:
        """

        :return:
        """
    @ContinueDelegate.setter
    def ContinueDelegate(self, value: HttpContinueDelegate) -> None: ...
    @property
    def ContinueTimeout(self) -> int:
        """

        :return:
        """
    @ContinueTimeout.setter
    def ContinueTimeout(self, value: int) -> None: ...
    @property
    def CookieContainer(self) -> CookieContainer:
        """

        :return:
        """
    @CookieContainer.setter
    def CookieContainer(self, value: CookieContainer) -> None: ...
    @property
    def CreatorInstance(self) -> IWebRequestCreate:
        """

        :return:
        """
    @property
    def Credentials(self) -> ICredentials:
        """

        :return:
        """
    @Credentials.setter
    def Credentials(self, value: ICredentials) -> None: ...
    @property
    def Date(self) -> DateTime:
        """

        :return:
        """
    @Date.setter
    def Date(self, value: DateTime) -> None: ...
    @classmethod
    @property
    def DefaultCachePolicy(cls) -> RequestCachePolicy:
        """

        :return:
        """
    @classmethod
    @DefaultCachePolicy.setter
    def DefaultCachePolicy(cls, value: RequestCachePolicy) -> None: ...
    @classmethod
    @property
    def DefaultMaximumErrorResponseLength(cls) -> int:
        """

        :return:
        """
    @classmethod
    @DefaultMaximumErrorResponseLength.setter
    def DefaultMaximumErrorResponseLength(cls, value: int) -> None: ...
    @classmethod
    @property
    def DefaultMaximumResponseHeadersLength(cls) -> int:
        """

        :return:
        """
    @classmethod
    @DefaultMaximumResponseHeadersLength.setter
    def DefaultMaximumResponseHeadersLength(cls, value: int) -> None: ...
    @classmethod
    @property
    def DefaultWebProxy(cls) -> IWebProxy:
        """

        :return:
        """
    @classmethod
    @DefaultWebProxy.setter
    def DefaultWebProxy(cls, value: IWebProxy) -> None: ...
    @property
    def Expect(self) -> str:
        """

        :return:
        """
    @Expect.setter
    def Expect(self, value: str) -> None: ...
    @property
    def HaveResponse(self) -> bool:
        """

        :return:
        """
    @property
    def Headers(self) -> WebHeaderCollection:
        """

        :return:
        """
    @Headers.setter
    def Headers(self, value: WebHeaderCollection) -> None: ...
    @property
    def Host(self) -> str:
        """

        :return:
        """
    @Host.setter
    def Host(self, value: str) -> None: ...
    @property
    def IfModifiedSince(self) -> DateTime:
        """

        :return:
        """
    @IfModifiedSince.setter
    def IfModifiedSince(self, value: DateTime) -> None: ...
    @property
    def ImpersonationLevel(self) -> TokenImpersonationLevel:
        """

        :return:
        """
    @ImpersonationLevel.setter
    def ImpersonationLevel(self, value: TokenImpersonationLevel) -> None: ...
    @property
    def KeepAlive(self) -> bool:
        """

        :return:
        """
    @KeepAlive.setter
    def KeepAlive(self, value: bool) -> None: ...
    @property
    def MaximumAutomaticRedirections(self) -> int:
        """

        :return:
        """
    @MaximumAutomaticRedirections.setter
    def MaximumAutomaticRedirections(self, value: int) -> None: ...
    @property
    def MaximumResponseHeadersLength(self) -> int:
        """

        :return:
        """
    @MaximumResponseHeadersLength.setter
    def MaximumResponseHeadersLength(self, value: int) -> None: ...
    @property
    def MediaType(self) -> str:
        """

        :return:
        """
    @MediaType.setter
    def MediaType(self, value: str) -> None: ...
    @property
    def Method(self) -> str:
        """

        :return:
        """
    @Method.setter
    def Method(self, value: str) -> None: ...
    @property
    def Pipelined(self) -> bool:
        """

        :return:
        """
    @Pipelined.setter
    def Pipelined(self, value: bool) -> None: ...
    @property
    def PreAuthenticate(self) -> bool:
        """

        :return:
        """
    @PreAuthenticate.setter
    def PreAuthenticate(self, value: bool) -> None: ...
    @property
    def ProtocolVersion(self) -> Version:
        """

        :return:
        """
    @ProtocolVersion.setter
    def ProtocolVersion(self, value: Version) -> None: ...
    @property
    def Proxy(self) -> IWebProxy:
        """

        :return:
        """
    @Proxy.setter
    def Proxy(self, value: IWebProxy) -> None: ...
    @property
    def ReadWriteTimeout(self) -> int:
        """

        :return:
        """
    @ReadWriteTimeout.setter
    def ReadWriteTimeout(self, value: int) -> None: ...
    @property
    def Referer(self) -> str:
        """

        :return:
        """
    @Referer.setter
    def Referer(self, value: str) -> None: ...
    @property
    def RequestUri(self) -> Uri:
        """

        :return:
        """
    @property
    def SendChunked(self) -> bool:
        """

        :return:
        """
    @SendChunked.setter
    def SendChunked(self, value: bool) -> None: ...
    @property
    def ServerCertificateValidationCallback(self) -> RemoteCertificateValidationCallback:
        """

        :return:
        """
    @ServerCertificateValidationCallback.setter
    def ServerCertificateValidationCallback(
        self, value: RemoteCertificateValidationCallback
    ) -> None: ...
    @property
    def ServicePoint(self) -> ServicePoint:
        """

        :return:
        """
    @property
    def SupportsCookieContainer(self) -> bool:
        """

        :return:
        """
    @property
    def Timeout(self) -> int:
        """

        :return:
        """
    @Timeout.setter
    def Timeout(self, value: int) -> None: ...
    @property
    def TransferEncoding(self) -> str:
        """

        :return:
        """
    @TransferEncoding.setter
    def TransferEncoding(self, value: str) -> None: ...
    @property
    def UnsafeAuthenticatedConnectionSharing(self) -> bool:
        """

        :return:
        """
    @UnsafeAuthenticatedConnectionSharing.setter
    def UnsafeAuthenticatedConnectionSharing(self, value: bool) -> None: ...
    @property
    def UseDefaultCredentials(self) -> bool:
        """

        :return:
        """
    @UseDefaultCredentials.setter
    def UseDefaultCredentials(self, value: bool) -> None: ...
    @property
    def UserAgent(self) -> str:
        """

        :return:
        """
    @UserAgent.setter
    def UserAgent(self, value: str) -> None: ...
    def Abort(self) -> None:
        """"""
    @overload
    def AddRange(self, range: int) -> None:
        """

        :param range:
        """
    @overload
    def AddRange(self, range: int) -> None:
        """

        :param range:
        """
    @overload
    def AddRange(self, _from: int, to: int) -> None:
        """

        :param _from:
        :param to:
        """
    @overload
    def AddRange(self, _from: int, to: int) -> None:
        """

        :param _from:
        :param to:
        """
    @overload
    def AddRange(self, rangeSpecifier: str, range: int) -> None:
        """

        :param rangeSpecifier:
        :param range:
        """
    @overload
    def AddRange(self, rangeSpecifier: str, range: int) -> None:
        """

        :param rangeSpecifier:
        :param range:
        """
    @overload
    def AddRange(self, rangeSpecifier: str, _from: int, to: int) -> None:
        """

        :param rangeSpecifier:
        :param _from:
        :param to:
        """
    @overload
    def AddRange(self, rangeSpecifier: str, _from: int, to: int) -> None:
        """

        :param rangeSpecifier:
        :param _from:
        :param to:
        """
    def BeginGetRequestStream(self, callback: AsyncCallback, state: object) -> IAsyncResult:
        """

        :param callback:
        :param state:
        :return:
        """
    def BeginGetResponse(self, callback: AsyncCallback, state: object) -> IAsyncResult:
        """

        :param callback:
        :param state:
        :return:
        """
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """

        :param requestedType:
        :return:
        """
    @overload
    def EndGetRequestStream(self, asyncResult: IAsyncResult) -> Stream:
        """

        :param asyncResult:
        :return:
        """
    @overload
    def EndGetRequestStream(
        self, asyncResult: IAsyncResult, context: TransportContext
    ) -> Tuple[Stream, TransportContext]:
        """

        :param asyncResult:
        :param context:
        :return:
        """
    def EndGetResponse(self, asyncResult: IAsyncResult) -> WebResponse:
        """

        :param asyncResult:
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
    def GetLifetimeService(self) -> object:
        """

        :return:
        """
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    @overload
    def GetRequestStream(self) -> Stream:
        """

        :return:
        """
    @overload
    def GetRequestStream(self, context: TransportContext) -> Tuple[Stream, TransportContext]:
        """

        :param context:
        :return:
        """
    def GetRequestStreamAsync(self) -> Task[Stream]:
        """

        :return:
        """
    def GetResponse(self) -> WebResponse:
        """

        :return:
        """
    def GetResponseAsync(self) -> Task[WebResponse]:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def InitializeLifetimeService(self) -> object:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class HttpWebResponse(WebResponse, ISerializable, IDisposable):
    """"""

    def __init__(self):
        """"""
    @property
    def CharacterSet(self) -> str:
        """

        :return:
        """
    @property
    def ContentEncoding(self) -> str:
        """

        :return:
        """
    @property
    def ContentLength(self) -> int:
        """

        :return:
        """
    @ContentLength.setter
    def ContentLength(self, value: int) -> None: ...
    @property
    def ContentType(self) -> str:
        """

        :return:
        """
    @ContentType.setter
    def ContentType(self, value: str) -> None: ...
    @property
    def Cookies(self) -> CookieCollection:
        """

        :return:
        """
    @Cookies.setter
    def Cookies(self, value: CookieCollection) -> None: ...
    @property
    def Headers(self) -> WebHeaderCollection:
        """

        :return:
        """
    @property
    def IsFromCache(self) -> bool:
        """

        :return:
        """
    @property
    def IsMutuallyAuthenticated(self) -> bool:
        """

        :return:
        """
    @property
    def LastModified(self) -> DateTime:
        """

        :return:
        """
    @property
    def Method(self) -> str:
        """

        :return:
        """
    @property
    def ProtocolVersion(self) -> Version:
        """

        :return:
        """
    @property
    def ResponseUri(self) -> Uri:
        """

        :return:
        """
    @property
    def Server(self) -> str:
        """

        :return:
        """
    @property
    def StatusCode(self) -> HttpStatusCode:
        """

        :return:
        """
    @property
    def StatusDescription(self) -> str:
        """

        :return:
        """
    @property
    def SupportsHeaders(self) -> bool:
        """

        :return:
        """
    def Close(self) -> None:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """

        :param requestedType:
        :return:
        """
    def Dispose(self) -> None:
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
    def GetLifetimeService(self) -> object:
        """

        :return:
        """
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    def GetResponseHeader(self, headerName: str) -> str:
        """

        :param headerName:
        :return:
        """
    def GetResponseStream(self) -> Stream:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def InitializeLifetimeService(self) -> object:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

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

    def __init__(self, engine: AutoWebProxyScriptEngine):
        """

        :param engine:
        """
    @property
    def IsValid(self) -> bool:
        """

        :return:
        """
    def Abort(self) -> None:
        """"""
    def Dispose(self) -> None:
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
    def GetProxies(self, destination: Uri, proxyList: IList[str]) -> Tuple[bool, IList[str]]:
        """

        :param destination:
        :param proxyList:
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

class IAuthenticationManager:
    """"""

    @property
    def CredentialPolicy(self) -> ICredentialPolicy:
        """

        :return:
        """
    @CredentialPolicy.setter
    def CredentialPolicy(self, value: ICredentialPolicy) -> None: ...
    @property
    def CustomTargetNameDictionary(self) -> StringDictionary:
        """

        :return:
        """
    @property
    def OSSupportsExtendedProtection(self) -> bool:
        """

        :return:
        """
    @property
    def RegisteredModules(self) -> IEnumerator:
        """

        :return:
        """
    @property
    def SpnDictionary(self) -> SpnDictionary:
        """

        :return:
        """
    @property
    def SspSupportsExtendedProtection(self) -> bool:
        """

        :return:
        """
    def Authenticate(
        self, challenge: str, request: WebRequest, credentials: ICredentials
    ) -> Authorization:
        """

        :param challenge:
        :param request:
        :param credentials:
        :return:
        """
    def BindModule(self, uri: Uri, response: Authorization, module: IAuthenticationModule) -> None:
        """

        :param uri:
        :param response:
        :param module:
        """
    def EnsureConfigLoaded(self) -> None:
        """"""
    def PreAuthenticate(self, request: WebRequest, credentials: ICredentials) -> Authorization:
        """

        :param request:
        :param credentials:
        :return:
        """
    def Register(self, authenticationModule: IAuthenticationModule) -> None:
        """

        :param authenticationModule:
        """
    @overload
    def Unregister(self, authenticationModule: IAuthenticationModule) -> None:
        """

        :param authenticationModule:
        """
    @overload
    def Unregister(self, authenticationScheme: str) -> None:
        """

        :param authenticationScheme:
        """

class IAuthenticationModule:
    """"""

    @property
    def AuthenticationType(self) -> str:
        """

        :return:
        """
    @property
    def CanPreAuthenticate(self) -> bool:
        """

        :return:
        """
    def Authenticate(
        self, challenge: str, request: WebRequest, credentials: ICredentials
    ) -> Authorization:
        """

        :param challenge:
        :param request:
        :param credentials:
        :return:
        """
    def PreAuthenticate(self, request: WebRequest, credentials: ICredentials) -> Authorization:
        """

        :param request:
        :param credentials:
        :return:
        """

class IAutoWebProxy(IWebProxy):
    """"""

    @property
    def Credentials(self) -> ICredentials:
        """

        :return:
        """
    @Credentials.setter
    def Credentials(self, value: ICredentials) -> None: ...
    def GetProxies(self, destination: Uri) -> ProxyChain:
        """

        :param destination:
        :return:
        """
    def GetProxy(self, destination: Uri) -> Uri:
        """

        :param destination:
        :return:
        """
    def IsBypassed(self, host: Uri) -> bool:
        """

        :param host:
        :return:
        """

class ICertificatePolicy:
    """"""

    def CheckValidationResult(
        self,
        srvPoint: ServicePoint,
        certificate: X509Certificate,
        request: WebRequest,
        certificateProblem: int,
    ) -> bool:
        """

        :param srvPoint:
        :param certificate:
        :param request:
        :param certificateProblem:
        :return:
        """

class ICloseEx:
    """"""

    def CloseEx(self, closeState: CloseExState) -> None:
        """

        :param closeState:
        """

class ICredentialPolicy:
    """"""

    def ShouldSendCredential(
        self,
        challengeUri: Uri,
        request: WebRequest,
        credential: NetworkCredential,
        authenticationModule: IAuthenticationModule,
    ) -> bool:
        """

        :param challengeUri:
        :param request:
        :param credential:
        :param authenticationModule:
        :return:
        """

class ICredentials:
    """"""

    def GetCredential(self, uri: Uri, authType: str) -> NetworkCredential:
        """

        :param uri:
        :param authType:
        :return:
        """

class ICredentialsByHost:
    """"""

    def GetCredential(self, host: str, port: int, authenticationType: str) -> NetworkCredential:
        """

        :param host:
        :param port:
        :param authenticationType:
        :return:
        """

class IPAddress(Object):
    """"""

    Any: Final[ClassVar[IPAddress]] = ...
    """
    
    :return: 
    """
    Broadcast: Final[ClassVar[IPAddress]] = ...
    """
    
    :return: 
    """
    IPv6Any: Final[ClassVar[IPAddress]] = ...
    """
    
    :return: 
    """
    IPv6Loopback: Final[ClassVar[IPAddress]] = ...
    """
    
    :return: 
    """
    IPv6None: Final[ClassVar[IPAddress]] = ...
    """
    
    :return: 
    """
    Loopback: Final[ClassVar[IPAddress]] = ...
    """
    
    :return: 
    """
    _None: Final[ClassVar[IPAddress]] = ...
    """
    
    :return: 
    """
    @overload
    def __init__(self, address: Array[int]):
        """

        :param address:
        """
    @overload
    def __init__(self, newAddress: int):
        """

        :param newAddress:
        """
    @overload
    def __init__(self, address: Array[int], scopeid: int):
        """

        :param address:
        :param scopeid:
        """
    @property
    def Address(self) -> int:
        """

        :return:
        """
    @Address.setter
    def Address(self, value: int) -> None: ...
    @property
    def AddressFamily(self) -> AddressFamily:
        """

        :return:
        """
    @property
    def IsIPv4MappedToIPv6(self) -> bool:
        """

        :return:
        """
    @property
    def IsIPv6LinkLocal(self) -> bool:
        """

        :return:
        """
    @property
    def IsIPv6Multicast(self) -> bool:
        """

        :return:
        """
    @property
    def IsIPv6SiteLocal(self) -> bool:
        """

        :return:
        """
    @property
    def IsIPv6Teredo(self) -> bool:
        """

        :return:
        """
    @property
    def ScopeId(self) -> int:
        """

        :return:
        """
    @ScopeId.setter
    def ScopeId(self, value: int) -> None: ...
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetAddressBytes(self) -> Array[int]:
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
    @classmethod
    @overload
    def HostToNetworkOrder(cls, host: int) -> int:
        """

        :param host:
        :return:
        """
    @classmethod
    @overload
    def HostToNetworkOrder(cls, host: int) -> int:
        """

        :param host:
        :return:
        """
    @classmethod
    @overload
    def HostToNetworkOrder(cls, host: int) -> int:
        """

        :param host:
        :return:
        """
    @classmethod
    def IsLoopback(cls, address: IPAddress) -> bool:
        """

        :param address:
        :return:
        """
    def MapToIPv4(self) -> IPAddress:
        """

        :return:
        """
    def MapToIPv6(self) -> IPAddress:
        """

        :return:
        """
    @classmethod
    @overload
    def NetworkToHostOrder(cls, network: int) -> int:
        """

        :param network:
        :return:
        """
    @classmethod
    @overload
    def NetworkToHostOrder(cls, network: int) -> int:
        """

        :param network:
        :return:
        """
    @classmethod
    @overload
    def NetworkToHostOrder(cls, network: int) -> int:
        """

        :param network:
        :return:
        """
    @classmethod
    def Parse(cls, ipString: str) -> IPAddress:
        """

        :param ipString:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @classmethod
    def TryParse(cls, ipString: str, address: IPAddress) -> Tuple[bool, IPAddress]:
        """

        :param ipString:
        :param address:
        :return:
        """

class IPEndPoint(EndPoint):
    """"""

    MaxPort: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    MinPort: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    @overload
    def __init__(self, address: IPAddress, port: int):
        """

        :param address:
        :param port:
        """
    @overload
    def __init__(self, address: int, port: int):
        """

        :param address:
        :param port:
        """
    @property
    def Address(self) -> IPAddress:
        """

        :return:
        """
    @Address.setter
    def Address(self, value: IPAddress) -> None: ...
    @property
    def AddressFamily(self) -> AddressFamily:
        """

        :return:
        """
    @property
    def Port(self) -> int:
        """

        :return:
        """
    @Port.setter
    def Port(self, value: int) -> None: ...
    def Create(self, socketAddress: SocketAddress) -> EndPoint:
        """

        :param socketAddress:
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
    def Serialize(self) -> SocketAddress:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class IPHostEntry(Object):
    """"""

    def __init__(self):
        """"""
    @property
    def AddressList(self) -> Array[IPAddress]:
        """

        :return:
        """
    @AddressList.setter
    def AddressList(self, value: Array[IPAddress]) -> None: ...
    @property
    def Aliases(self) -> Array[str]:
        """

        :return:
        """
    @Aliases.setter
    def Aliases(self, value: Array[str]) -> None: ...
    @property
    def HostName(self) -> str:
        """

        :return:
        """
    @HostName.setter
    def HostName(self, value: str) -> None: ...
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

class IPMulticastRequest(ValueType):
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

class IPv6MulticastRequest(ValueType):
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

class IRequestLifetimeTracker:
    """"""

    def TrackRequestLifetime(self, requestStartTimestamp: int) -> None:
        """

        :param requestStartTimestamp:
        """

class ISessionAuthenticationModule(IAuthenticationModule):
    """"""

    @property
    def AuthenticationType(self) -> str:
        """

        :return:
        """
    @property
    def CanPreAuthenticate(self) -> bool:
        """

        :return:
        """
    @property
    def CanUseDefaultCredentials(self) -> bool:
        """

        :return:
        """
    def Authenticate(
        self, challenge: str, request: WebRequest, credentials: ICredentials
    ) -> Authorization:
        """

        :param challenge:
        :param request:
        :param credentials:
        :return:
        """
    def ClearSession(self, webRequest: WebRequest) -> None:
        """

        :param webRequest:
        """
    def PreAuthenticate(self, request: WebRequest, credentials: ICredentials) -> Authorization:
        """

        :param request:
        :param credentials:
        :return:
        """
    def Update(self, challenge: str, webRequest: WebRequest) -> bool:
        """

        :param challenge:
        :param webRequest:
        :return:
        """

class IWebProxy:
    """"""

    @property
    def Credentials(self) -> ICredentials:
        """

        :return:
        """
    @Credentials.setter
    def Credentials(self, value: ICredentials) -> None: ...
    def GetProxy(self, destination: Uri) -> Uri:
        """

        :param destination:
        :return:
        """
    def IsBypassed(self, host: Uri) -> bool:
        """

        :param host:
        :return:
        """

class IWebProxyFinder(IDisposable):
    """"""

    @property
    def IsValid(self) -> bool:
        """

        :return:
        """
    def Abort(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def GetProxies(self, destination: Uri, proxyList: IList[str]) -> Tuple[bool, IList[str]]:
        """

        :param destination:
        :param proxyList:
        :return:
        """
    def Reset(self) -> None:
        """"""

class IWebProxyScript:
    """"""

    def Close(self) -> None:
        """"""
    def Load(self, scriptLocation: Uri, script: str, helperType: Type) -> bool:
        """

        :param scriptLocation:
        :param script:
        :param helperType:
        :return:
        """
    def Run(self, url: str, host: str) -> str:
        """

        :param url:
        :param host:
        :return:
        """

class IWebRequestCreate:
    """"""

    def Create(self, uri: Uri) -> WebRequest:
        """

        :param uri:
        :return:
        """

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

class InterlockedGate(ValueType):
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

class InterlockedStack(Object):
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

class InternalException(SystemException, _Exception, ISerializable):
    """"""

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

class IssuerListInfoEx(ValueType):
    """"""

    aIssuers: Final[SafeHandle] = ...
    """
    
    :return: 
    """
    cIssuers: Final[int] = ...
    """
    
    :return: 
    """
    def __init__(self, handle: SafeHandle, nativeBuffer: Array[int]):
        """

        :param handle:
        :param nativeBuffer:
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

class KerberosClient(Object, IAuthenticationModule, ISessionAuthenticationModule):
    """"""

    def __init__(self):
        """"""
    @property
    def AuthenticationType(self) -> str:
        """

        :return:
        """
    @property
    def CanPreAuthenticate(self) -> bool:
        """

        :return:
        """
    @property
    def CanUseDefaultCredentials(self) -> bool:
        """

        :return:
        """
    def Authenticate(
        self, challenge: str, request: WebRequest, credentials: ICredentials
    ) -> Authorization:
        """

        :param challenge:
        :param request:
        :param credentials:
        :return:
        """
    def ClearSession(self, webRequest: WebRequest) -> None:
        """

        :param webRequest:
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
    def PreAuthenticate(self, request: WebRequest, credentials: ICredentials) -> Authorization:
        """

        :param request:
        :param credentials:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Update(self, challenge: str, webRequest: WebRequest) -> bool:
        """

        :param challenge:
        :param webRequest:
        :return:
        """

class KnownHttpVerb(Object):
    """"""

    @overload
    def Equals(self, verb: KnownHttpVerb) -> bool:
        """

        :param verb:
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
    def GetType(self) -> Type:
        """

        :return:
        """
    @classmethod
    def Parse(cls, name: str) -> KnownHttpVerb:
        """

        :param name:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class LazyAsyncResult(Object, IAsyncResult):
    """"""

    @property
    def AsyncState(self) -> object:
        """

        :return:
        """
    @property
    def AsyncWaitHandle(self) -> WaitHandle:
        """

        :return:
        """
    @property
    def CompletedSynchronously(self) -> bool:
        """

        :return:
        """
    @property
    def IsCompleted(self) -> bool:
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

class Linger(ValueType):
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

class ListenerAsyncResult(LazyAsyncResult, IAsyncResult):
    """"""

    @property
    def AsyncState(self) -> object:
        """

        :return:
        """
    @property
    def AsyncWaitHandle(self) -> WaitHandle:
        """

        :return:
        """
    @property
    def CompletedSynchronously(self) -> bool:
        """

        :return:
        """
    @property
    def IsCompleted(self) -> bool:
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

class ListenerClientCertAsyncResult(LazyAsyncResult, IAsyncResult):
    """"""

    @property
    def AsyncState(self) -> object:
        """

        :return:
        """
    @property
    def AsyncWaitHandle(self) -> WaitHandle:
        """

        :return:
        """
    @property
    def CompletedSynchronously(self) -> bool:
        """

        :return:
        """
    @property
    def IsCompleted(self) -> bool:
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
    def Current(self) -> object:
        """

        :return:
        """
    def Dispose(self) -> None:
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
    def MoveNext(self) -> bool:
        """

        :return:
        """
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class Logging(Object):
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

class NTAuthentication(Object):
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

class NclUtilities(ABC, Object):
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

class NegotiateClient(Object, IAuthenticationModule, ISessionAuthenticationModule):
    """"""

    def __init__(self):
        """"""
    @property
    def AuthenticationType(self) -> str:
        """

        :return:
        """
    @property
    def CanPreAuthenticate(self) -> bool:
        """

        :return:
        """
    @property
    def CanUseDefaultCredentials(self) -> bool:
        """

        :return:
        """
    def Authenticate(
        self, challenge: str, request: WebRequest, credentials: ICredentials
    ) -> Authorization:
        """

        :param challenge:
        :param request:
        :param credentials:
        :return:
        """
    def ClearSession(self, webRequest: WebRequest) -> None:
        """

        :param webRequest:
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
    def PreAuthenticate(self, request: WebRequest, credentials: ICredentials) -> Authorization:
        """

        :param request:
        :param credentials:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Update(self, challenge: str, webRequest: WebRequest) -> bool:
        """

        :param challenge:
        :param webRequest:
        :return:
        """

class NegotiationInfo(ValueType):
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

class NegotiationInfoClass(Object):
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

class NestedMultipleAsyncResult(LazyAsyncResult, IAsyncResult):
    """"""

    @property
    def AsyncState(self) -> object:
        """

        :return:
        """
    @property
    def AsyncWaitHandle(self) -> WaitHandle:
        """

        :return:
        """
    @property
    def CompletedSynchronously(self) -> bool:
        """

        :return:
        """
    @property
    def IsCompleted(self) -> bool:
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

class NestedSingleAsyncResult(LazyAsyncResult, IAsyncResult):
    """"""

    @property
    def AsyncState(self) -> object:
        """

        :return:
        """
    @property
    def AsyncWaitHandle(self) -> WaitHandle:
        """

        :return:
        """
    @property
    def CompletedSynchronously(self) -> bool:
        """

        :return:
        """
    @property
    def IsCompleted(self) -> bool:
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

class NetRes(Object):
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
    @classmethod
    @overload
    def GetWebStatusCodeString(cls, statusCode: FtpStatusCode, statusDescription: str) -> str:
        """

        :param statusCode:
        :param statusDescription:
        :return:
        """
    @classmethod
    @overload
    def GetWebStatusCodeString(cls, statusCode: HttpStatusCode, statusDescription: str) -> str:
        """

        :param statusCode:
        :param statusDescription:
        :return:
        """
    @classmethod
    @overload
    def GetWebStatusString(cls, Status: WebExceptionStatus) -> str:
        """

        :param Status:
        :return:
        """
    @classmethod
    @overload
    def GetWebStatusString(cls, Res: str, Status: WebExceptionStatus) -> str:
        """

        :param Res:
        :param Status:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class NetWebProxyFinder(BaseWebProxyFinder, IWebProxyFinder, IDisposable):
    """"""

    def __init__(self, engine: AutoWebProxyScriptEngine):
        """

        :param engine:
        """
    @property
    def IsUnrecognizedScheme(self) -> bool:
        """

        :return:
        """
    @property
    def IsValid(self) -> bool:
        """

        :return:
        """
    def Abort(self) -> None:
        """"""
    def Dispose(self) -> None:
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
    def GetProxies(self, destination: Uri, proxyList: IList[str]) -> Tuple[bool, IList[str]]:
        """

        :param destination:
        :param proxyList:
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

class NetworkCredential(Object, ICredentials, ICredentialsByHost):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, userName: str, password: SecureString):
        """

        :param userName:
        :param password:
        """
    @overload
    def __init__(self, userName: str, password: str):
        """

        :param userName:
        :param password:
        """
    @overload
    def __init__(self, userName: str, password: SecureString, domain: str):
        """

        :param userName:
        :param password:
        :param domain:
        """
    @overload
    def __init__(self, userName: str, password: str, domain: str):
        """

        :param userName:
        :param password:
        :param domain:
        """
    @property
    def Domain(self) -> str:
        """

        :return:
        """
    @Domain.setter
    def Domain(self, value: str) -> None: ...
    @property
    def Password(self) -> str:
        """

        :return:
        """
    @Password.setter
    def Password(self, value: str) -> None: ...
    @property
    def SecurePassword(self) -> SecureString:
        """

        :return:
        """
    @SecurePassword.setter
    def SecurePassword(self, value: SecureString) -> None: ...
    @property
    def UserName(self) -> str:
        """

        :return:
        """
    @UserName.setter
    def UserName(self, value: str) -> None: ...
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetCredential(self, uri: Uri, authType: str) -> NetworkCredential:
        """

        :param uri:
        :param authType:
        :return:
        """
    @overload
    def GetCredential(self, host: str, port: int, authenticationType: str) -> NetworkCredential:
        """

        :param host:
        :param port:
        :param authenticationType:
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
        """

        :return:
        """
    @classmethod
    @property
    def Instance(cls) -> NetworkingPerfCounters:
        """

        :return:
        """
    @overload
    def Decrement(self, perfCounter: NetworkingPerfCounterName) -> None:
        """

        :param perfCounter:
        """
    @overload
    def Decrement(self, perfCounter: NetworkingPerfCounterName, amount: int) -> None:
        """

        :param perfCounter:
        :param amount:
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
    def GetTimestamp(cls) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def Increment(self, perfCounter: NetworkingPerfCounterName) -> None:
        """

        :param perfCounter:
        """
    @overload
    def Increment(self, perfCounter: NetworkingPerfCounterName, amount: int) -> None:
        """

        :param perfCounter:
        :param amount:
        """
    def IncrementAverage(self, perfCounter: NetworkingPerfCounterName, startTimestamp: int) -> None:
        """

        :param perfCounter:
        :param startTimestamp:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class NtlmClient(Object, IAuthenticationModule, ISessionAuthenticationModule):
    """"""

    def __init__(self):
        """"""
    @property
    def AuthenticationType(self) -> str:
        """

        :return:
        """
    @property
    def CanPreAuthenticate(self) -> bool:
        """

        :return:
        """
    @property
    def CanUseDefaultCredentials(self) -> bool:
        """

        :return:
        """
    def Authenticate(
        self, challenge: str, request: WebRequest, credentials: ICredentials
    ) -> Authorization:
        """

        :param challenge:
        :param request:
        :param credentials:
        :return:
        """
    def ClearSession(self, webRequest: WebRequest) -> None:
        """

        :param webRequest:
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
    def PreAuthenticate(self, request: WebRequest, credentials: ICredentials) -> Authorization:
        """

        :param request:
        :param credentials:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Update(self, challenge: str, webRequest: WebRequest) -> bool:
        """

        :param challenge:
        :param webRequest:
        :return:
        """

class OpenReadCompletedEventArgs(AsyncCompletedEventArgs):
    """"""

    @property
    def Cancelled(self) -> bool:
        """

        :return:
        """
    @property
    def Error(self) -> Exception:
        """

        :return:
        """
    @property
    def Result(self) -> Stream:
        """

        :return:
        """
    @property
    def UserState(self) -> object:
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

OpenReadCompletedEventHandler: Callable[[object, OpenReadCompletedEventArgs], None] = ...
"""

:param sender: 
:param e: 
"""

class OpenWriteCompletedEventArgs(AsyncCompletedEventArgs):
    """"""

    @property
    def Cancelled(self) -> bool:
        """

        :return:
        """
    @property
    def Error(self) -> Exception:
        """

        :return:
        """
    @property
    def Result(self) -> Stream:
        """

        :return:
        """
    @property
    def UserState(self) -> object:
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

OpenWriteCompletedEventHandler: Callable[[object, OpenWriteCompletedEventArgs], None] = ...
"""

:param sender: 
:param e: 
"""

class PathList(Object):
    """"""

    def __init__(self):
        """"""
    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def Item(self) -> object:
        """

        :return:
        """
    @Item.setter
    def Item(self, value: object) -> None: ...
    @property
    def SyncRoot(self) -> object:
        """

        :return:
        """
    @property
    def Values(self) -> ICollection:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetCookiesCount(self) -> int:
        """

        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
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
    def __getitem__(self, s: str) -> object:
        """

        :param s:
        :return:
        """
    def __setitem__(self, s: str, value: object) -> None:
        """

        :param s:
        :param value:
        """

class PolicyWrapper(Object):
    """"""

    def Accept(self, Certificate: X509Certificate, CertificateProblem: int) -> bool:
        """

        :param Certificate:
        :param CertificateProblem:
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

class PooledStream(Stream, IDisposable):
    """"""

    @property
    def CanRead(self) -> bool:
        """

        :return:
        """
    @property
    def CanSeek(self) -> bool:
        """

        :return:
        """
    @property
    def CanTimeout(self) -> bool:
        """

        :return:
        """
    @property
    def CanWrite(self) -> bool:
        """

        :return:
        """
    @property
    def Length(self) -> int:
        """

        :return:
        """
    @property
    def Position(self) -> int:
        """

        :return:
        """
    @Position.setter
    def Position(self, value: int) -> None: ...
    @property
    def ReadTimeout(self) -> int:
        """

        :return:
        """
    @ReadTimeout.setter
    def ReadTimeout(self, value: int) -> None: ...
    @property
    def WriteTimeout(self) -> int:
        """

        :return:
        """
    @WriteTimeout.setter
    def WriteTimeout(self, value: int) -> None: ...
    def BeginRead(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """

        :param buffer:
        :param offset:
        :param count:
        :param callback:
        :param state:
        :return:
        """
    def BeginWrite(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """

        :param buffer:
        :param offset:
        :param count:
        :param callback:
        :param state:
        :return:
        """
    @overload
    def Close(self) -> None:
        """"""
    @overload
    def Close(self, timeout: int) -> None:
        """

        :param timeout:
        """
    @overload
    def CopyTo(self, destination: Stream) -> None:
        """

        :param destination:
        """
    @overload
    def CopyTo(self, destination: Stream, bufferSize: int) -> None:
        """

        :param destination:
        :param bufferSize:
        """
    @overload
    def CopyToAsync(self, destination: Stream) -> Task:
        """

        :param destination:
        :return:
        """
    @overload
    def CopyToAsync(self, destination: Stream, bufferSize: int) -> Task:
        """

        :param destination:
        :param bufferSize:
        :return:
        """
    @overload
    def CopyToAsync(
        self, destination: Stream, bufferSize: int, cancellationToken: CancellationToken
    ) -> Task:
        """

        :param destination:
        :param bufferSize:
        :param cancellationToken:
        :return:
        """
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """

        :param requestedType:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    def EndRead(self, asyncResult: IAsyncResult) -> int:
        """

        :param asyncResult:
        :return:
        """
    def EndWrite(self, asyncResult: IAsyncResult) -> None:
        """

        :param asyncResult:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def Flush(self) -> None:
        """"""
    @overload
    def FlushAsync(self) -> Task:
        """

        :return:
        """
    @overload
    def FlushAsync(self, cancellationToken: CancellationToken) -> Task:
        """

        :param cancellationToken:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetLifetimeService(self) -> object:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def InitializeLifetimeService(self) -> object:
        """

        :return:
        """
    def Read(self, buffer: Array[int], offset: int, count: int) -> Tuple[int, Array[int]]:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def ReadAsync(self, buffer: Array[int], offset: int, count: int) -> Task[int]:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def ReadAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task[int]:
        """

        :param buffer:
        :param offset:
        :param count:
        :param cancellationToken:
        :return:
        """
    def ReadByte(self) -> int:
        """

        :return:
        """
    def Seek(self, offset: int, origin: SeekOrigin) -> int:
        """

        :param offset:
        :param origin:
        :return:
        """
    def SetLength(self, value: int) -> None:
        """

        :param value:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Write(self, buffer: Array[int], offset: int, count: int) -> None:
        """

        :param buffer:
        :param offset:
        :param count:
        """
    @overload
    def WriteAsync(self, buffer: Array[int], offset: int, count: int) -> Task:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def WriteAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task:
        """

        :param buffer:
        :param offset:
        :param count:
        :param cancellationToken:
        :return:
        """
    def WriteByte(self, value: int) -> None:
        """

        :param value:
        """

class PrefixLookup(Object):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, capacity: int):
        """

        :param capacity:
        """
    def Add(self, prefix: str, value: object) -> None:
        """

        :param prefix:
        :param value:
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
    def Lookup(self, lookupKey: str) -> object:
        """

        :param lookupKey:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class ProtocolViolationException(InvalidOperationException, _Exception, ISerializable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, message: str):
        """

        :param message:
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

class ProxyChain(ABC, Object, IEnumerable[Uri], IEnumerable, IDisposable):
    """"""

    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
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
    @overload
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[Uri]:
        """

        :return:
        """

class ProxyScriptChain(ProxyChain, IEnumerable[Uri], IEnumerable, IDisposable):
    """"""

    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
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
    @overload
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[Uri]:
        """

        :return:
        """

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

class RegBlobWebProxyDataBuilder(WebProxyDataBuilder):
    """"""

    def __init__(self, connectoid: str, registry: SafeRegistryHandle):
        """

        :param connectoid:
        :param registry:
        """
    def Build(self) -> WebProxyData:
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
    def ReadString(self) -> str:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class RegistryConfiguration(ABC, Object):
    """"""

    @classmethod
    def AppConfigReadInt(cls, configVariable: str, defaultValue: int) -> int:
        """

        :param configVariable:
        :param defaultValue:
        :return:
        """
    @classmethod
    def AppConfigReadString(cls, configVariable: str, defaultValue: str) -> str:
        """

        :param configVariable:
        :param defaultValue:
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
    @classmethod
    def GlobalConfigReadInt(cls, configVariable: str, defaultValue: int) -> int:
        """

        :param configVariable:
        :param defaultValue:
        :return:
        """
    @classmethod
    def GlobalConfigReadString(cls, configVariable: str, defaultValue: str) -> str:
        """

        :param configVariable:
        :param defaultValue:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class RequestContextBase(ABC, Object, IDisposable):
    """"""

    def Close(self) -> None:
        """"""
    def Dispose(self) -> None:
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

class RequestLifetimeSetter(Object):
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

class ResponseDescription(Object):
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

class RtcState(Object):
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

class SSL_EXTRA_CERT_CHAIN_POLICY_PARA(ValueType):
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

class SSPIAuthType(Object, SSPIInterface):
    """"""

    def __init__(self):
        """"""
    @property
    def SecurityPackages(self) -> Array[SecurityPackageInfoClass]:
        """

        :return:
        """
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
        """

        :param credential:
        :param context:
        :param inputBuffer:
        :param inFlags:
        :param endianness:
        :param outputBuffer:
        :param outFlags:
        :return:
        """
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
        """

        :param credential:
        :param context:
        :param inputBuffers:
        :param inFlags:
        :param endianness:
        :param outputBuffer:
        :param outFlags:
        :return:
        """
    @overload
    def AcquireCredentialsHandle(
        self,
        moduleName: str,
        usage: CredentialUse,
        authdata: AuthIdentity,
        outCredential: SafeFreeCredentials,
    ) -> Tuple[int, SafeFreeCredentials]:
        """

        :param moduleName:
        :param usage:
        :param authdata:
        :param outCredential:
        :return:
        """
    @overload
    def AcquireCredentialsHandle(
        self,
        moduleName: str,
        usage: CredentialUse,
        authdata: SafeSspiAuthDataHandle,
        outCredential: SafeFreeCredentials,
    ) -> Tuple[int, SafeFreeCredentials]:
        """

        :param moduleName:
        :param usage:
        :param authdata:
        :param outCredential:
        :return:
        """
    @overload
    def AcquireCredentialsHandle(
        self,
        moduleName: str,
        usage: CredentialUse,
        authdata: SecureCredential,
        outCredential: SafeFreeCredentials,
    ) -> Tuple[int, SafeFreeCredentials]:
        """

        :param moduleName:
        :param usage:
        :param authdata:
        :param outCredential:
        :return:
        """
    @overload
    def AcquireCredentialsHandle(
        self,
        moduleName: str,
        usage: CredentialUse,
        authdata: SecureCredential2,
        outCredential: SafeFreeCredentials,
    ) -> Tuple[int, SafeFreeCredentials]:
        """

        :param moduleName:
        :param usage:
        :param authdata:
        :param outCredential:
        :return:
        """
    def AcquireDefaultCredential(
        self, moduleName: str, usage: CredentialUse, outCredential: SafeFreeCredentials
    ) -> Tuple[int, SafeFreeCredentials]:
        """

        :param moduleName:
        :param usage:
        :param outCredential:
        :return:
        """
    def ApplyControlToken(
        self, refContext: SafeDeleteContext, inputBuffers: Array[SecurityBuffer]
    ) -> int:
        """

        :param refContext:
        :param inputBuffers:
        :return:
        """
    def CompleteAuthToken(
        self, refContext: SafeDeleteContext, inputBuffers: Array[SecurityBuffer]
    ) -> int:
        """

        :param refContext:
        :param inputBuffers:
        :return:
        """
    def DecryptMessage(
        self, context: SafeDeleteContext, inputOutput: SecurityBufferDescriptor, sequenceNumber: int
    ) -> int:
        """

        :param context:
        :param inputOutput:
        :param sequenceNumber:
        :return:
        """
    def EncryptMessage(
        self, context: SafeDeleteContext, inputOutput: SecurityBufferDescriptor, sequenceNumber: int
    ) -> int:
        """

        :param context:
        :param inputOutput:
        :param sequenceNumber:
        :return:
        """
    def EnumerateSecurityPackages(
        self, pkgnum: int, pkgArray: SafeFreeContextBuffer
    ) -> Tuple[int, int, SafeFreeContextBuffer]:
        """

        :param pkgnum:
        :param pkgArray:
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
        """

        :param credential:
        :param context:
        :param targetName:
        :param inFlags:
        :param endianness:
        :param inputBuffer:
        :param outputBuffer:
        :param outFlags:
        :return:
        """
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
        """

        :param credential:
        :param context:
        :param targetName:
        :param inFlags:
        :param endianness:
        :param inputBuffers:
        :param outputBuffer:
        :param outFlags:
        :return:
        """
    def MakeSignature(
        self, context: SafeDeleteContext, inputOutput: SecurityBufferDescriptor, sequenceNumber: int
    ) -> int:
        """

        :param context:
        :param inputOutput:
        :param sequenceNumber:
        :return:
        """
    def QueryContextAttributes(
        self,
        phContext: SafeDeleteContext,
        attribute: ContextAttribute,
        buffer: Array[int],
        handleType: Type,
        refHandle: SafeHandle,
    ) -> Tuple[int, SafeHandle]:
        """

        :param phContext:
        :param attribute:
        :param buffer:
        :param handleType:
        :param refHandle:
        :return:
        """
    def QueryContextChannelBinding(
        self,
        phContext: SafeDeleteContext,
        attribute: ContextAttribute,
        refHandle: SafeFreeContextBufferChannelBinding,
    ) -> Tuple[int, SafeFreeContextBufferChannelBinding]:
        """

        :param phContext:
        :param attribute:
        :param refHandle:
        :return:
        """
    def QuerySecurityContextToken(
        self, phContext: SafeDeleteContext, phToken: SafeCloseHandle
    ) -> Tuple[int, SafeCloseHandle]:
        """

        :param phContext:
        :param phToken:
        :return:
        """
    def SetContextAttributes(
        self, phContext: SafeDeleteContext, attribute: ContextAttribute, buffer: Array[int]
    ) -> int:
        """

        :param phContext:
        :param attribute:
        :param buffer:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def VerifySignature(
        self, context: SafeDeleteContext, inputOutput: SecurityBufferDescriptor, sequenceNumber: int
    ) -> int:
        """

        :param context:
        :param inputOutput:
        :param sequenceNumber:
        :return:
        """

class SSPIHandle(ValueType):
    """"""

    @property
    def IsZero(self) -> bool:
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

class SSPIInterface:
    """"""

    @property
    def SecurityPackages(self) -> Array[SecurityPackageInfoClass]:
        """

        :return:
        """
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
        """

        :param credential:
        :param context:
        :param inputBuffer:
        :param inFlags:
        :param endianness:
        :param outputBuffer:
        :param outFlags:
        :return:
        """
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
        """

        :param credential:
        :param context:
        :param inputBuffers:
        :param inFlags:
        :param endianness:
        :param outputBuffer:
        :param outFlags:
        :return:
        """
    @overload
    def AcquireCredentialsHandle(
        self,
        moduleName: str,
        usage: CredentialUse,
        authdata: AuthIdentity,
        outCredential: SafeFreeCredentials,
    ) -> Tuple[int, SafeFreeCredentials]:
        """

        :param moduleName:
        :param usage:
        :param authdata:
        :param outCredential:
        :return:
        """
    @overload
    def AcquireCredentialsHandle(
        self,
        moduleName: str,
        usage: CredentialUse,
        authdata: SafeSspiAuthDataHandle,
        outCredential: SafeFreeCredentials,
    ) -> Tuple[int, SafeFreeCredentials]:
        """

        :param moduleName:
        :param usage:
        :param authdata:
        :param outCredential:
        :return:
        """
    @overload
    def AcquireCredentialsHandle(
        self,
        moduleName: str,
        usage: CredentialUse,
        authdata: SecureCredential,
        outCredential: SafeFreeCredentials,
    ) -> Tuple[int, SafeFreeCredentials]:
        """

        :param moduleName:
        :param usage:
        :param authdata:
        :param outCredential:
        :return:
        """
    @overload
    def AcquireCredentialsHandle(
        self,
        moduleName: str,
        usage: CredentialUse,
        authdata: SecureCredential2,
        outCredential: SafeFreeCredentials,
    ) -> Tuple[int, SafeFreeCredentials]:
        """

        :param moduleName:
        :param usage:
        :param authdata:
        :param outCredential:
        :return:
        """
    def AcquireDefaultCredential(
        self, moduleName: str, usage: CredentialUse, outCredential: SafeFreeCredentials
    ) -> Tuple[int, SafeFreeCredentials]:
        """

        :param moduleName:
        :param usage:
        :param outCredential:
        :return:
        """
    def ApplyControlToken(
        self, refContext: SafeDeleteContext, inputBuffers: Array[SecurityBuffer]
    ) -> int:
        """

        :param refContext:
        :param inputBuffers:
        :return:
        """
    def CompleteAuthToken(
        self, refContext: SafeDeleteContext, inputBuffers: Array[SecurityBuffer]
    ) -> int:
        """

        :param refContext:
        :param inputBuffers:
        :return:
        """
    def DecryptMessage(
        self, context: SafeDeleteContext, inputOutput: SecurityBufferDescriptor, sequenceNumber: int
    ) -> int:
        """

        :param context:
        :param inputOutput:
        :param sequenceNumber:
        :return:
        """
    def EncryptMessage(
        self, context: SafeDeleteContext, inputOutput: SecurityBufferDescriptor, sequenceNumber: int
    ) -> int:
        """

        :param context:
        :param inputOutput:
        :param sequenceNumber:
        :return:
        """
    def EnumerateSecurityPackages(
        self, pkgnum: int, pkgArray: SafeFreeContextBuffer
    ) -> Tuple[int, int, SafeFreeContextBuffer]:
        """

        :param pkgnum:
        :param pkgArray:
        :return:
        """
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
        """

        :param credential:
        :param context:
        :param targetName:
        :param inFlags:
        :param endianness:
        :param inputBuffer:
        :param outputBuffer:
        :param outFlags:
        :return:
        """
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
        """

        :param credential:
        :param context:
        :param targetName:
        :param inFlags:
        :param endianness:
        :param inputBuffers:
        :param outputBuffer:
        :param outFlags:
        :return:
        """
    def MakeSignature(
        self, context: SafeDeleteContext, inputOutput: SecurityBufferDescriptor, sequenceNumber: int
    ) -> int:
        """

        :param context:
        :param inputOutput:
        :param sequenceNumber:
        :return:
        """
    def QueryContextAttributes(
        self,
        phContext: SafeDeleteContext,
        attribute: ContextAttribute,
        buffer: Array[int],
        handleType: Type,
        refHandle: SafeHandle,
    ) -> Tuple[int, SafeHandle]:
        """

        :param phContext:
        :param attribute:
        :param buffer:
        :param handleType:
        :param refHandle:
        :return:
        """
    def QueryContextChannelBinding(
        self,
        phContext: SafeDeleteContext,
        attribute: ContextAttribute,
        refHandle: SafeFreeContextBufferChannelBinding,
    ) -> Tuple[int, SafeFreeContextBufferChannelBinding]:
        """

        :param phContext:
        :param attribute:
        :param refHandle:
        :return:
        """
    def QuerySecurityContextToken(
        self, phContext: SafeDeleteContext, phToken: SafeCloseHandle
    ) -> Tuple[int, SafeCloseHandle]:
        """

        :param phContext:
        :param phToken:
        :return:
        """
    def SetContextAttributes(
        self, phContext: SafeDeleteContext, attribute: ContextAttribute, buffer: Array[int]
    ) -> int:
        """

        :param phContext:
        :param attribute:
        :param buffer:
        :return:
        """
    def VerifySignature(
        self, context: SafeDeleteContext, inputOutput: SecurityBufferDescriptor, sequenceNumber: int
    ) -> int:
        """

        :param context:
        :param inputOutput:
        :param sequenceNumber:
        :return:
        """

class SSPISecureChannelType(Object, SSPIInterface):
    """"""

    def __init__(self):
        """"""
    @property
    def SecurityPackages(self) -> Array[SecurityPackageInfoClass]:
        """

        :return:
        """
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
        """

        :param credential:
        :param context:
        :param inputBuffer:
        :param inFlags:
        :param endianness:
        :param outputBuffer:
        :param outFlags:
        :return:
        """
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
        """

        :param credential:
        :param context:
        :param inputBuffers:
        :param inFlags:
        :param endianness:
        :param outputBuffer:
        :param outFlags:
        :return:
        """
    @overload
    def AcquireCredentialsHandle(
        self,
        moduleName: str,
        usage: CredentialUse,
        authdata: AuthIdentity,
        outCredential: SafeFreeCredentials,
    ) -> Tuple[int, SafeFreeCredentials]:
        """

        :param moduleName:
        :param usage:
        :param authdata:
        :param outCredential:
        :return:
        """
    @overload
    def AcquireCredentialsHandle(
        self,
        moduleName: str,
        usage: CredentialUse,
        authdata: SafeSspiAuthDataHandle,
        outCredential: SafeFreeCredentials,
    ) -> Tuple[int, SafeFreeCredentials]:
        """

        :param moduleName:
        :param usage:
        :param authdata:
        :param outCredential:
        :return:
        """
    @overload
    def AcquireCredentialsHandle(
        self,
        moduleName: str,
        usage: CredentialUse,
        authdata: SecureCredential,
        outCredential: SafeFreeCredentials,
    ) -> Tuple[int, SafeFreeCredentials]:
        """

        :param moduleName:
        :param usage:
        :param authdata:
        :param outCredential:
        :return:
        """
    @overload
    def AcquireCredentialsHandle(
        self,
        moduleName: str,
        usage: CredentialUse,
        authdata: SecureCredential2,
        outCredential: SafeFreeCredentials,
    ) -> Tuple[int, SafeFreeCredentials]:
        """

        :param moduleName:
        :param usage:
        :param authdata:
        :param outCredential:
        :return:
        """
    def AcquireDefaultCredential(
        self, moduleName: str, usage: CredentialUse, outCredential: SafeFreeCredentials
    ) -> Tuple[int, SafeFreeCredentials]:
        """

        :param moduleName:
        :param usage:
        :param outCredential:
        :return:
        """
    def ApplyControlToken(
        self, refContext: SafeDeleteContext, inputBuffers: Array[SecurityBuffer]
    ) -> int:
        """

        :param refContext:
        :param inputBuffers:
        :return:
        """
    def CompleteAuthToken(
        self, refContext: SafeDeleteContext, inputBuffers: Array[SecurityBuffer]
    ) -> int:
        """

        :param refContext:
        :param inputBuffers:
        :return:
        """
    def DecryptMessage(
        self, context: SafeDeleteContext, inputOutput: SecurityBufferDescriptor, sequenceNumber: int
    ) -> int:
        """

        :param context:
        :param inputOutput:
        :param sequenceNumber:
        :return:
        """
    def EncryptMessage(
        self, context: SafeDeleteContext, inputOutput: SecurityBufferDescriptor, sequenceNumber: int
    ) -> int:
        """

        :param context:
        :param inputOutput:
        :param sequenceNumber:
        :return:
        """
    def EnumerateSecurityPackages(
        self, pkgnum: int, pkgArray: SafeFreeContextBuffer
    ) -> Tuple[int, int, SafeFreeContextBuffer]:
        """

        :param pkgnum:
        :param pkgArray:
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
        """

        :param credential:
        :param context:
        :param targetName:
        :param inFlags:
        :param endianness:
        :param inputBuffer:
        :param outputBuffer:
        :param outFlags:
        :return:
        """
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
        """

        :param credential:
        :param context:
        :param targetName:
        :param inFlags:
        :param endianness:
        :param inputBuffers:
        :param outputBuffer:
        :param outFlags:
        :return:
        """
    def MakeSignature(
        self, context: SafeDeleteContext, inputOutput: SecurityBufferDescriptor, sequenceNumber: int
    ) -> int:
        """

        :param context:
        :param inputOutput:
        :param sequenceNumber:
        :return:
        """
    def QueryContextAttributes(
        self,
        phContext: SafeDeleteContext,
        attribute: ContextAttribute,
        buffer: Array[int],
        handleType: Type,
        refHandle: SafeHandle,
    ) -> Tuple[int, SafeHandle]:
        """

        :param phContext:
        :param attribute:
        :param buffer:
        :param handleType:
        :param refHandle:
        :return:
        """
    def QueryContextChannelBinding(
        self,
        phContext: SafeDeleteContext,
        attribute: ContextAttribute,
        refHandle: SafeFreeContextBufferChannelBinding,
    ) -> Tuple[int, SafeFreeContextBufferChannelBinding]:
        """

        :param phContext:
        :param attribute:
        :param refHandle:
        :return:
        """
    def QuerySecurityContextToken(
        self, phContext: SafeDeleteContext, phToken: SafeCloseHandle
    ) -> Tuple[int, SafeCloseHandle]:
        """

        :param phContext:
        :param phToken:
        :return:
        """
    def SetContextAttributes(
        self, phContext: SafeDeleteContext, attribute: ContextAttribute, buffer: Array[int]
    ) -> int:
        """

        :param phContext:
        :param attribute:
        :param buffer:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def VerifySignature(
        self, context: SafeDeleteContext, inputOutput: SecurityBufferDescriptor, sequenceNumber: int
    ) -> int:
        """

        :param context:
        :param inputOutput:
        :param sequenceNumber:
        :return:
        """

class SSPIWrapper(ABC, Object):
    """"""

    @classmethod
    @overload
    def AcquireCredentialsHandle(
        cls, SecModule: SSPIInterface, package: str, intent: CredentialUse, authdata: AuthIdentity
    ) -> SafeFreeCredentials:
        """

        :param SecModule:
        :param package:
        :param intent:
        :param authdata:
        :return:
        """
    @classmethod
    @overload
    def AcquireCredentialsHandle(
        cls,
        SecModule: SSPIInterface,
        package: str,
        intent: CredentialUse,
        authdata: SafeSspiAuthDataHandle,
    ) -> SafeFreeCredentials:
        """

        :param SecModule:
        :param package:
        :param intent:
        :param authdata:
        :return:
        """
    @classmethod
    @overload
    def AcquireCredentialsHandle(
        cls, SecModule: SSPIInterface, package: str, intent: CredentialUse, scc: SecureCredential
    ) -> SafeFreeCredentials:
        """

        :param SecModule:
        :param package:
        :param intent:
        :param scc:
        :return:
        """
    @classmethod
    @overload
    def AcquireCredentialsHandle(
        cls, SecModule: SSPIInterface, package: str, intent: CredentialUse, scc: SecureCredential2
    ) -> SafeFreeCredentials:
        """

        :param SecModule:
        :param package:
        :param intent:
        :param scc:
        :return:
        """
    @classmethod
    def AcquireDefaultCredential(
        cls, SecModule: SSPIInterface, package: str, intent: CredentialUse
    ) -> SafeFreeCredentials:
        """

        :param SecModule:
        :param package:
        :param intent:
        :return:
        """
    @classmethod
    def ApplyAlertToken(
        cls,
        secModule: SSPIInterface,
        credentialsHandle: SafeFreeCredentials,
        securityContext: SafeDeleteContext,
        alertType: TlsAlertType,
        alertMessage: TlsAlertMessage,
    ) -> int:
        """

        :param secModule:
        :param credentialsHandle:
        :param securityContext:
        :param alertType:
        :param alertMessage:
        :return:
        """
    @classmethod
    def ApplyShutdownToken(
        cls,
        secModule: SSPIInterface,
        credentialsHandle: SafeFreeCredentials,
        securityContext: SafeDeleteContext,
    ) -> int:
        """

        :param secModule:
        :param credentialsHandle:
        :param securityContext:
        :return:
        """
    @classmethod
    def DecryptMessage(
        cls,
        secModule: SSPIInterface,
        context: SafeDeleteContext,
        input: Array[SecurityBuffer],
        sequenceNumber: int,
    ) -> int:
        """

        :param secModule:
        :param context:
        :param input:
        :param sequenceNumber:
        :return:
        """
    @classmethod
    def EncryptMessage(
        cls,
        secModule: SSPIInterface,
        context: SafeDeleteContext,
        input: Array[SecurityBuffer],
        sequenceNumber: int,
    ) -> int:
        """

        :param secModule:
        :param context:
        :param input:
        :param sequenceNumber:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @classmethod
    def ErrorDescription(cls, errorCode: int) -> str:
        """

        :param errorCode:
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
    @classmethod
    @overload
    def QueryContextAttributes(
        cls,
        SecModule: SSPIInterface,
        securityContext: SafeDeleteContext,
        contextAttribute: ContextAttribute,
    ) -> object:
        """

        :param SecModule:
        :param securityContext:
        :param contextAttribute:
        :return:
        """
    @classmethod
    @overload
    def QueryContextAttributes(
        cls,
        SecModule: SSPIInterface,
        securityContext: SafeDeleteContext,
        contextAttribute: ContextAttribute,
        errorCode: int,
    ) -> Tuple[object, int]:
        """

        :param SecModule:
        :param securityContext:
        :param contextAttribute:
        :param errorCode:
        :return:
        """
    @classmethod
    def QueryContextChannelBinding(
        cls,
        SecModule: SSPIInterface,
        securityContext: SafeDeleteContext,
        contextAttribute: ContextAttribute,
    ) -> SafeFreeContextBufferChannelBinding:
        """

        :param SecModule:
        :param securityContext:
        :param contextAttribute:
        :return:
        """
    @classmethod
    def QuerySecurityContextToken(
        cls, SecModule: SSPIInterface, context: SafeDeleteContext, token: SafeCloseHandle
    ) -> Tuple[int, SafeCloseHandle]:
        """

        :param SecModule:
        :param context:
        :param token:
        :return:
        """
    @classmethod
    def SetContextAttributes(
        cls,
        SecModule: SSPIInterface,
        securityContext: SafeDeleteContext,
        contextAttribute: ContextAttribute,
        value: object,
    ) -> int:
        """

        :param SecModule:
        :param securityContext:
        :param contextAttribute:
        :param value:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @classmethod
    def VerifySignature(
        cls,
        secModule: SSPIInterface,
        context: SafeDeleteContext,
        input: Array[SecurityBuffer],
        sequenceNumber: int,
    ) -> int:
        """

        :param secModule:
        :param context:
        :param input:
        :param sequenceNumber:
        :return:
        """

class SafeCertSelectCritera(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
    """"""

    @property
    def IsClosed(self) -> bool:
        """

        :return:
        """
    @property
    def IsInvalid(self) -> bool:
        """

        :return:
        """
    def Close(self) -> None:
        """"""
    def DangerousAddRef(self, success: bool) -> None:
        """

        :param success:
        """
    def DangerousGetHandle(self) -> IntPtr:
        """

        :return:
        """
    def DangerousRelease(self) -> None:
        """"""
    def Dispose(self) -> None:
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
    def SetHandleAsInvalid(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class SafeCloseHandle(CriticalHandleZeroOrMinusOneIsInvalid, IDisposable):
    """"""

    @property
    def IsClosed(self) -> bool:
        """

        :return:
        """
    @property
    def IsInvalid(self) -> bool:
        """

        :return:
        """
    def Close(self) -> None:
        """"""
    def Dispose(self) -> None:
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
    def SetHandleAsInvalid(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class SafeCloseIcmpHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
    """"""

    @property
    def IsClosed(self) -> bool:
        """

        :return:
        """
    @property
    def IsInvalid(self) -> bool:
        """

        :return:
        """
    def Close(self) -> None:
        """"""
    def DangerousAddRef(self, success: bool) -> None:
        """

        :param success:
        """
    def DangerousGetHandle(self) -> IntPtr:
        """

        :return:
        """
    def DangerousRelease(self) -> None:
        """"""
    def Dispose(self) -> None:
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
    def SetHandleAsInvalid(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class SafeCloseSocket(SafeHandleMinusOneIsInvalid, IDisposable):
    """"""

    @property
    def IsClosed(self) -> bool:
        """

        :return:
        """
    @property
    def IsInvalid(self) -> bool:
        """

        :return:
        """
    def Close(self) -> None:
        """"""
    def DangerousAddRef(self, success: bool) -> None:
        """

        :param success:
        """
    def DangerousGetHandle(self) -> IntPtr:
        """

        :return:
        """
    def DangerousRelease(self) -> None:
        """"""
    def Dispose(self) -> None:
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
    def SetHandleAsInvalid(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class SafeCloseSocketAndEvent(SafeCloseSocket, IDisposable):
    """"""

    @property
    def IsClosed(self) -> bool:
        """

        :return:
        """
    @property
    def IsInvalid(self) -> bool:
        """

        :return:
        """
    def Close(self) -> None:
        """"""
    def DangerousAddRef(self, success: bool) -> None:
        """

        :param success:
        """
    def DangerousGetHandle(self) -> IntPtr:
        """

        :return:
        """
    def DangerousRelease(self) -> None:
        """"""
    def Dispose(self) -> None:
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
    def SetHandleAsInvalid(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class SafeCredentialReference(CriticalHandleMinusOneIsInvalid, IDisposable):
    """"""

    @property
    def IsClosed(self) -> bool:
        """

        :return:
        """
    @property
    def IsInvalid(self) -> bool:
        """

        :return:
        """
    def Close(self) -> None:
        """"""
    def Dispose(self) -> None:
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
    def SetHandleAsInvalid(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class SafeDeleteContext(ABC, SafeHandle, IDisposable):
    """"""

    @property
    def IsClosed(self) -> bool:
        """

        :return:
        """
    @property
    def IsInvalid(self) -> bool:
        """

        :return:
        """
    def Close(self) -> None:
        """"""
    def DangerousAddRef(self, success: bool) -> None:
        """

        :param success:
        """
    def DangerousGetHandle(self) -> IntPtr:
        """

        :return:
        """
    def DangerousRelease(self) -> None:
        """"""
    def Dispose(self) -> None:
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
    def SetHandleAsInvalid(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class SafeDeleteContext_SECURITY(SafeDeleteContext, IDisposable):
    """"""

    @property
    def IsClosed(self) -> bool:
        """

        :return:
        """
    @property
    def IsInvalid(self) -> bool:
        """

        :return:
        """
    def Close(self) -> None:
        """"""
    def DangerousAddRef(self, success: bool) -> None:
        """

        :param success:
        """
    def DangerousGetHandle(self) -> IntPtr:
        """

        :return:
        """
    def DangerousRelease(self) -> None:
        """"""
    def Dispose(self) -> None:
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
    def SetHandleAsInvalid(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class SafeFreeAddrInfo(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
    """"""

    @property
    def IsClosed(self) -> bool:
        """

        :return:
        """
    @property
    def IsInvalid(self) -> bool:
        """

        :return:
        """
    def Close(self) -> None:
        """"""
    def DangerousAddRef(self, success: bool) -> None:
        """

        :param success:
        """
    def DangerousGetHandle(self) -> IntPtr:
        """

        :return:
        """
    def DangerousRelease(self) -> None:
        """"""
    def Dispose(self) -> None:
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
    def SetHandleAsInvalid(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class SafeFreeCertChain(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
    """"""

    @property
    def IsClosed(self) -> bool:
        """

        :return:
        """
    @property
    def IsInvalid(self) -> bool:
        """

        :return:
        """
    def Close(self) -> None:
        """"""
    def DangerousAddRef(self, success: bool) -> None:
        """

        :param success:
        """
    def DangerousGetHandle(self) -> IntPtr:
        """

        :return:
        """
    def DangerousRelease(self) -> None:
        """"""
    def Dispose(self) -> None:
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
    def SetHandleAsInvalid(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class SafeFreeCertChainList(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
    """"""

    @property
    def IsClosed(self) -> bool:
        """

        :return:
        """
    @property
    def IsInvalid(self) -> bool:
        """

        :return:
        """
    def Close(self) -> None:
        """"""
    def DangerousAddRef(self, success: bool) -> None:
        """

        :param success:
        """
    def DangerousGetHandle(self) -> IntPtr:
        """

        :return:
        """
    def DangerousRelease(self) -> None:
        """"""
    def Dispose(self) -> None:
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
    def SetHandleAsInvalid(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class SafeFreeCertContext(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
    """"""

    @property
    def IsClosed(self) -> bool:
        """

        :return:
        """
    @property
    def IsInvalid(self) -> bool:
        """

        :return:
        """
    def Close(self) -> None:
        """"""
    def DangerousAddRef(self, success: bool) -> None:
        """

        :param success:
        """
    def DangerousGetHandle(self) -> IntPtr:
        """

        :return:
        """
    def DangerousRelease(self) -> None:
        """"""
    def Dispose(self) -> None:
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
    def SetHandleAsInvalid(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class SafeFreeContextBuffer(ABC, SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
    """"""

    @property
    def IsClosed(self) -> bool:
        """

        :return:
        """
    @property
    def IsInvalid(self) -> bool:
        """

        :return:
        """
    def Close(self) -> None:
        """"""
    def DangerousAddRef(self, success: bool) -> None:
        """

        :param success:
        """
    def DangerousGetHandle(self) -> IntPtr:
        """

        :return:
        """
    def DangerousRelease(self) -> None:
        """"""
    def Dispose(self) -> None:
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
    @classmethod
    def QueryContextAttributes(
        cls,
        dll: SecurDll,
        phContext: SafeDeleteContext,
        contextAttribute: ContextAttribute,
        buffer: int,
        refHandle: SafeHandle,
    ) -> int:
        """

        :param dll:
        :param phContext:
        :param contextAttribute:
        :param buffer:
        :param refHandle:
        :return:
        """
    @classmethod
    def SetContextAttributes(
        cls,
        dll: SecurDll,
        phContext: SafeDeleteContext,
        contextAttribute: ContextAttribute,
        buffer: Array[int],
    ) -> int:
        """

        :param dll:
        :param phContext:
        :param contextAttribute:
        :param buffer:
        :return:
        """
    def SetHandleAsInvalid(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class SafeFreeContextBufferChannelBinding(ABC, ChannelBinding, IDisposable):
    """"""

    @property
    def IsClosed(self) -> bool:
        """

        :return:
        """
    @property
    def IsInvalid(self) -> bool:
        """

        :return:
        """
    @property
    def Size(self) -> int:
        """

        :return:
        """
    def Close(self) -> None:
        """"""
    def DangerousAddRef(self, success: bool) -> None:
        """

        :param success:
        """
    def DangerousGetHandle(self) -> IntPtr:
        """

        :return:
        """
    def DangerousRelease(self) -> None:
        """"""
    def Dispose(self) -> None:
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
    @classmethod
    def QueryContextChannelBinding(
        cls,
        dll: SecurDll,
        phContext: SafeDeleteContext,
        contextAttribute: ContextAttribute,
        buffer: Bindings,
        refHandle: SafeFreeContextBufferChannelBinding,
    ) -> int:
        """

        :param dll:
        :param phContext:
        :param contextAttribute:
        :param buffer:
        :param refHandle:
        :return:
        """
    def SetHandleAsInvalid(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class SafeFreeContextBufferChannelBinding_SECURITY(
    SafeFreeContextBufferChannelBinding, IDisposable
):
    """"""

    def __init__(self):
        """"""
    @property
    def IsClosed(self) -> bool:
        """

        :return:
        """
    @property
    def IsInvalid(self) -> bool:
        """

        :return:
        """
    @property
    def Size(self) -> int:
        """

        :return:
        """
    def Close(self) -> None:
        """"""
    def DangerousAddRef(self, success: bool) -> None:
        """

        :param success:
        """
    def DangerousGetHandle(self) -> IntPtr:
        """

        :return:
        """
    def DangerousRelease(self) -> None:
        """"""
    def Dispose(self) -> None:
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
    def SetHandleAsInvalid(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class SafeFreeContextBuffer_SECURITY(SafeFreeContextBuffer, IDisposable):
    """"""

    @property
    def IsClosed(self) -> bool:
        """

        :return:
        """
    @property
    def IsInvalid(self) -> bool:
        """

        :return:
        """
    def Close(self) -> None:
        """"""
    def DangerousAddRef(self, success: bool) -> None:
        """

        :param success:
        """
    def DangerousGetHandle(self) -> IntPtr:
        """

        :return:
        """
    def DangerousRelease(self) -> None:
        """"""
    def Dispose(self) -> None:
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
    def SetHandleAsInvalid(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class SafeFreeCredential_SECURITY(SafeFreeCredentials, IDisposable):
    """"""

    def __init__(self):
        """"""
    @property
    def IsClosed(self) -> bool:
        """

        :return:
        """
    @property
    def IsInvalid(self) -> bool:
        """

        :return:
        """
    def Close(self) -> None:
        """"""
    def DangerousAddRef(self, success: bool) -> None:
        """

        :param success:
        """
    def DangerousGetHandle(self) -> IntPtr:
        """

        :return:
        """
    def DangerousRelease(self) -> None:
        """"""
    def Dispose(self) -> None:
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
    def SetHandleAsInvalid(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class SafeFreeCredentials(ABC, SafeHandle, IDisposable):
    """"""

    @property
    def IsClosed(self) -> bool:
        """

        :return:
        """
    @property
    def IsInvalid(self) -> bool:
        """

        :return:
        """
    @classmethod
    @overload
    def AcquireCredentialsHandle(
        cls,
        package: str,
        intent: CredentialUse,
        authdata: SafeSspiAuthDataHandle,
        outCredential: SafeFreeCredentials,
    ) -> Tuple[int, SafeFreeCredentials]:
        """

        :param package:
        :param intent:
        :param authdata:
        :param outCredential:
        :return:
        """
    @classmethod
    @overload
    def AcquireCredentialsHandle(
        cls,
        dll: SecurDll,
        package: str,
        intent: CredentialUse,
        authdata: AuthIdentity,
        outCredential: SafeFreeCredentials,
    ) -> Tuple[int, SafeFreeCredentials]:
        """

        :param dll:
        :param package:
        :param intent:
        :param authdata:
        :param outCredential:
        :return:
        """
    @classmethod
    @overload
    def AcquireCredentialsHandle(
        cls,
        dll: SecurDll,
        package: str,
        intent: CredentialUse,
        authdata: SecureCredential,
        outCredential: SafeFreeCredentials,
    ) -> Tuple[int, SafeFreeCredentials]:
        """

        :param dll:
        :param package:
        :param intent:
        :param authdata:
        :param outCredential:
        :return:
        """
    @classmethod
    @overload
    def AcquireCredentialsHandle(
        cls,
        dll: SecurDll,
        package: str,
        intent: CredentialUse,
        authdata: SecureCredential2,
        outCredential: SafeFreeCredentials,
    ) -> Tuple[int, SafeFreeCredentials]:
        """

        :param dll:
        :param package:
        :param intent:
        :param authdata:
        :param outCredential:
        :return:
        """
    @classmethod
    def AcquireDefaultCredential(
        cls, dll: SecurDll, package: str, intent: CredentialUse, outCredential: SafeFreeCredentials
    ) -> Tuple[int, SafeFreeCredentials]:
        """

        :param dll:
        :param package:
        :param intent:
        :param outCredential:
        :return:
        """
    def Close(self) -> None:
        """"""
    def DangerousAddRef(self, success: bool) -> None:
        """

        :param success:
        """
    def DangerousGetHandle(self) -> IntPtr:
        """

        :return:
        """
    def DangerousRelease(self) -> None:
        """"""
    def Dispose(self) -> None:
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
    def SetHandleAsInvalid(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class SafeGlobalFree(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
    """"""

    @property
    def IsClosed(self) -> bool:
        """

        :return:
        """
    @property
    def IsInvalid(self) -> bool:
        """

        :return:
        """
    def Close(self) -> None:
        """"""
    def DangerousAddRef(self, success: bool) -> None:
        """

        :param success:
        """
    def DangerousGetHandle(self) -> IntPtr:
        """

        :return:
        """
    def DangerousRelease(self) -> None:
        """"""
    def Dispose(self) -> None:
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
    def SetHandleAsInvalid(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class SafeInternetHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
    """"""

    def __init__(self):
        """"""
    @property
    def IsClosed(self) -> bool:
        """

        :return:
        """
    @property
    def IsInvalid(self) -> bool:
        """

        :return:
        """
    def Close(self) -> None:
        """"""
    def DangerousAddRef(self, success: bool) -> None:
        """

        :param success:
        """
    def DangerousGetHandle(self) -> IntPtr:
        """

        :return:
        """
    def DangerousRelease(self) -> None:
        """"""
    def Dispose(self) -> None:
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
    def SetHandleAsInvalid(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class SafeLoadLibrary(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
    """"""

    Zero: Final[ClassVar[SafeLoadLibrary]] = ...
    """
    
    :return: 
    """
    @property
    def IsClosed(self) -> bool:
        """

        :return:
        """
    @property
    def IsInvalid(self) -> bool:
        """

        :return:
        """
    def Close(self) -> None:
        """"""
    def DangerousAddRef(self, success: bool) -> None:
        """

        :param success:
        """
    def DangerousGetHandle(self) -> IntPtr:
        """

        :return:
        """
    def DangerousRelease(self) -> None:
        """"""
    def Dispose(self) -> None:
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
    def HasFunction(self, functionName: str) -> bool:
        """

        :param functionName:
        :return:
        """
    @classmethod
    def LoadLibraryEx(cls, library: str) -> SafeLoadLibrary:
        """

        :param library:
        :return:
        """
    def SetHandleAsInvalid(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class SafeLocalFree(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
    """"""

    Zero: Final[ClassVar[SafeLocalFree]] = ...
    """
    
    :return: 
    """
    @property
    def IsClosed(self) -> bool:
        """

        :return:
        """
    @property
    def IsInvalid(self) -> bool:
        """

        :return:
        """
    def Close(self) -> None:
        """"""
    def DangerousAddRef(self, success: bool) -> None:
        """

        :param success:
        """
    def DangerousGetHandle(self) -> IntPtr:
        """

        :return:
        """
    def DangerousRelease(self) -> None:
        """"""
    def Dispose(self) -> None:
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
    @classmethod
    def LocalAlloc(cls, cb: int) -> SafeLocalFree:
        """

        :param cb:
        :return:
        """
    def SetHandleAsInvalid(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class SafeLocalFreeChannelBinding(ChannelBinding, IDisposable):
    """"""

    def __init__(self):
        """"""
    @property
    def IsClosed(self) -> bool:
        """

        :return:
        """
    @property
    def IsInvalid(self) -> bool:
        """

        :return:
        """
    @property
    def Size(self) -> int:
        """

        :return:
        """
    def Close(self) -> None:
        """"""
    def DangerousAddRef(self, success: bool) -> None:
        """

        :param success:
        """
    def DangerousGetHandle(self) -> IntPtr:
        """

        :return:
        """
    def DangerousRelease(self) -> None:
        """"""
    def Dispose(self) -> None:
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
    @classmethod
    def LocalAlloc(cls, cb: int) -> SafeLocalFreeChannelBinding:
        """

        :param cb:
        :return:
        """
    def SetHandleAsInvalid(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class SafeNativeOverlapped(SafeHandle, IDisposable):
    """"""

    @property
    def IsClosed(self) -> bool:
        """

        :return:
        """
    @property
    def IsInvalid(self) -> bool:
        """

        :return:
        """
    def Close(self) -> None:
        """"""
    def DangerousAddRef(self, success: bool) -> None:
        """

        :param success:
        """
    def DangerousGetHandle(self) -> IntPtr:
        """

        :return:
        """
    def DangerousRelease(self) -> None:
        """"""
    def Dispose(self) -> None:
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
    def ReinitializeNativeOverlapped(self) -> None:
        """"""
    def SetHandleAsInvalid(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class SafeNclNativeMethods(ABC, Object):
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

class SafeOverlappedFree(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
    """"""

    @property
    def IsClosed(self) -> bool:
        """

        :return:
        """
    @property
    def IsInvalid(self) -> bool:
        """

        :return:
        """
    @classmethod
    @overload
    def Alloc(cls) -> SafeOverlappedFree:
        """

        :return:
        """
    @classmethod
    @overload
    def Alloc(cls, socketHandle: SafeCloseSocket) -> SafeOverlappedFree:
        """

        :param socketHandle:
        :return:
        """
    @overload
    def Close(self) -> None:
        """"""
    @overload
    def Close(self, resetOwner: bool) -> None:
        """

        :param resetOwner:
        """
    def DangerousAddRef(self, success: bool) -> None:
        """

        :param success:
        """
    def DangerousGetHandle(self) -> IntPtr:
        """

        :return:
        """
    def DangerousRelease(self) -> None:
        """"""
    def Dispose(self) -> None:
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
    def SetHandleAsInvalid(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class SafeRegistryHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
    """"""

    @property
    def IsClosed(self) -> bool:
        """

        :return:
        """
    @property
    def IsInvalid(self) -> bool:
        """

        :return:
        """
    def Close(self) -> None:
        """"""
    def DangerousAddRef(self, success: bool) -> None:
        """

        :param success:
        """
    def DangerousGetHandle(self) -> IntPtr:
        """

        :return:
        """
    def DangerousRelease(self) -> None:
        """"""
    def Dispose(self) -> None:
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
    def SetHandleAsInvalid(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class SafeSspiAuthDataHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
    """"""

    def __init__(self):
        """"""
    @property
    def IsClosed(self) -> bool:
        """

        :return:
        """
    @property
    def IsInvalid(self) -> bool:
        """

        :return:
        """
    def Close(self) -> None:
        """"""
    def DangerousAddRef(self, success: bool) -> None:
        """

        :param success:
        """
    def DangerousGetHandle(self) -> IntPtr:
        """

        :return:
        """
    def DangerousRelease(self) -> None:
        """"""
    def Dispose(self) -> None:
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
    def SetHandleAsInvalid(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class SafeUnlockUrlCacheEntryFile(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
    """"""

    @property
    def IsClosed(self) -> bool:
        """

        :return:
        """
    @property
    def IsInvalid(self) -> bool:
        """

        :return:
        """
    def Close(self) -> None:
        """"""
    def DangerousAddRef(self, success: bool) -> None:
        """

        :param success:
        """
    def DangerousGetHandle(self) -> IntPtr:
        """

        :return:
        """
    def DangerousRelease(self) -> None:
        """"""
    def Dispose(self) -> None:
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
    def SetHandleAsInvalid(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class SafeWebSocketHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
    """"""

    @property
    def IsClosed(self) -> bool:
        """

        :return:
        """
    @property
    def IsInvalid(self) -> bool:
        """

        :return:
        """
    def Close(self) -> None:
        """"""
    def DangerousAddRef(self, success: bool) -> None:
        """

        :param success:
        """
    def DangerousGetHandle(self) -> IntPtr:
        """

        :return:
        """
    def DangerousRelease(self) -> None:
        """"""
    def Dispose(self) -> None:
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
    def SetHandleAsInvalid(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class ScatterGatherBuffers(Object):
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

class SecSizes(Object):
    """"""

    BlockSize: Final[int] = ...
    """
    
    :return: 
    """
    MaxSignature: Final[int] = ...
    """
    
    :return: 
    """
    MaxToken: Final[int] = ...
    """
    
    :return: 
    """
    SecurityTrailer: Final[int] = ...
    """
    
    :return: 
    """
    SizeOf: Final[ClassVar[int]] = ...
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

    CurrentVersion: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    cCreds: Final[int] = ...
    """
    
    :return: 
    """
    cMappers: Final[int] = ...
    """
    
    :return: 
    """
    cSupportedAlgs: Final[int] = ...
    """
    
    :return: 
    """
    certContextArray: Final[IntPtr] = ...
    """
    
    :return: 
    """
    dwFlags: Final[SecureCredential.Flags] = ...
    """
    
    :return: 
    """
    dwMaximumCipherStrength: Final[int] = ...
    """
    
    :return: 
    """
    dwMinimumCipherStrength: Final[int] = ...
    """
    
    :return: 
    """
    dwSessionLifespan: Final[int] = ...
    """
    
    :return: 
    """
    grbitEnabledProtocols: Final[SchProtocols] = ...
    """
    
    :return: 
    """
    reserved: Final[int] = ...
    """
    
    :return: 
    """
    version: Final[int] = ...
    """
    
    :return: 
    """
    def __init__(
        self,
        version: int,
        certificate: X509Certificate,
        flags: SecureCredential.Flags,
        protocols: SchProtocols,
        policy: EncryptionPolicy,
    ):
        """

        :param version:
        :param certificate:
        :param flags:
        :param protocols:
        :param policy:
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

    class Flags(Enum):
        """"""

        Zero: Flags = ...
        """"""
        NoSystemMapper: Flags = ...
        """"""
        NoNameCheck: Flags = ...
        """"""
        ValidateManual: Flags = ...
        """"""
        NoDefaultCred: Flags = ...
        """"""
        ValidateAuto: Flags = ...
        """"""
        SendAuxRecord: Flags = ...
        """"""
        UseStrongCrypto: Flags = ...
        """"""

class SecureCredential2(ValueType):
    """"""

    CurrentVersion: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    cCreds: Final[int] = ...
    """
    
    :return: 
    """
    cMappers: Final[int] = ...
    """
    
    :return: 
    """
    cTlsParameters: Final[int] = ...
    """
    
    :return: 
    """
    certContextArray: Final[None] = ...
    """"""
    dwCredformat: Final[int] = ...
    """
    
    :return: 
    """
    dwFlags: Final[SecureCredential2.Flags] = ...
    """
    
    :return: 
    """
    dwSessionLifespan: Final[int] = ...
    """
    
    :return: 
    """
    pTlsParameters: Final[TlsParamaters] = ...
    """
    
    :return: 
    """
    version: Final[int] = ...
    """
    
    :return: 
    """
    def __init__(
        self, flags: SecureCredential2.Flags, protocols: SchProtocols, policy: EncryptionPolicy
    ):
        """

        :param flags:
        :param protocols:
        :param policy:
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

    class Flags(Enum):
        """"""

        Zero: Flags = ...
        """"""
        NoSystemMapper: Flags = ...
        """"""
        NoNameCheck: Flags = ...
        """"""
        ValidateManual: Flags = ...
        """"""
        NoDefaultCred: Flags = ...
        """"""
        ValidateAuto: Flags = ...
        """"""
        SendAuxRecord: Flags = ...
        """"""
        UseStrongCrypto: Flags = ...
        """"""
        UsePresharedKeyOnly: Flags = ...
        """"""
        AllowNullEencryption: Flags = ...
        """"""

class SecurityBuffer(Object):
    """"""

    offset: Final[int] = ...
    """
    
    :return: 
    """
    size: Final[int] = ...
    """
    
    :return: 
    """
    token: Final[Array[int]] = ...
    """
    
    :return: 
    """
    type: Final[BufferType] = ...
    """
    
    :return: 
    """
    unmanagedToken: Final[SafeHandle] = ...
    """
    
    :return: 
    """
    @overload
    def __init__(self, binding: ChannelBinding):
        """

        :param binding:
        """
    @overload
    def __init__(self, data: Array[int], tokentype: BufferType):
        """

        :param data:
        :param tokentype:
        """
    @overload
    def __init__(self, size: int, tokentype: BufferType):
        """

        :param size:
        :param tokentype:
        """
    @overload
    def __init__(self, data: Array[int], offset: int, size: int, tokentype: BufferType):
        """

        :param data:
        :param offset:
        :param size:
        :param tokentype:
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

class SecurityBufferDescriptor(Object):
    """"""

    Count: Final[int] = ...
    """
    
    :return: 
    """
    UnmanagedPointer: Final[None] = ...
    """"""
    Version: Final[int] = ...
    """
    
    :return: 
    """
    def __init__(self, count: int):
        """

        :param count:
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

class SecurityBufferStruct(ValueType):
    """"""

    Size: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    count: Final[int] = ...
    """
    
    :return: 
    """
    token: Final[IntPtr] = ...
    """
    
    :return: 
    """
    type: Final[BufferType] = ...
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

class SecurityPackageInfo(ValueType):
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

class SecurityPackageInfoClass(Object):
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
        """

        :return:
        """
    @Handle.setter
    def Handle(self, value: IntPtr) -> None: ...
    @property
    def SafeWaitHandle(self) -> SafeWaitHandle:
        """

        :return:
        """
    @SafeWaitHandle.setter
    def SafeWaitHandle(self, value: SafeWaitHandle) -> None: ...
    def Close(self) -> None:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """

        :param requestedType:
        :return:
        """
    def Dispose(self) -> None:
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
    def GetLifetimeService(self) -> object:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def InitializeLifetimeService(self) -> object:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def WaitOne(self) -> bool:
        """

        :return:
        """
    @overload
    def WaitOne(self, millisecondsTimeout: int) -> bool:
        """

        :param millisecondsTimeout:
        :return:
        """
    @overload
    def WaitOne(self, timeout: TimeSpan) -> bool:
        """

        :param timeout:
        :return:
        """
    @overload
    def WaitOne(self, millisecondsTimeout: int, exitContext: bool) -> bool:
        """

        :param millisecondsTimeout:
        :param exitContext:
        :return:
        """
    @overload
    def WaitOne(self, timeout: TimeSpan, exitContext: bool) -> bool:
        """

        :param timeout:
        :param exitContext:
        :return:
        """

class ServerCertValidationCallback(Object):
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

class ServiceNameStore(Object):
    """"""

    def __init__(self):
        """"""
    @property
    def ServiceNames(self) -> ServiceNameCollection:
        """

        :return:
        """
    def Add(self, uriPrefix: str) -> bool:
        """

        :param uriPrefix:
        :return:
        """
    def BuildServiceNames(self, uriPrefix: str) -> Array[str]:
        """

        :param uriPrefix:
        :return:
        """
    def BuildSimpleServiceName(self, uriPrefix: str) -> str:
        """

        :param uriPrefix:
        :return:
        """
    def Clear(self) -> None:
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
    def Remove(self, uriPrefix: str) -> bool:
        """

        :param uriPrefix:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class ServicePoint(Object):
    """"""

    @property
    def Address(self) -> Uri:
        """

        :return:
        """
    @property
    def BindIPEndPointDelegate(self) -> BindIPEndPoint:
        """

        :return:
        """
    @BindIPEndPointDelegate.setter
    def BindIPEndPointDelegate(self, value: BindIPEndPoint) -> None: ...
    @property
    def Certificate(self) -> X509Certificate:
        """

        :return:
        """
    @property
    def ClientCertificate(self) -> X509Certificate:
        """

        :return:
        """
    @property
    def ConnectionLeaseTimeout(self) -> int:
        """

        :return:
        """
    @ConnectionLeaseTimeout.setter
    def ConnectionLeaseTimeout(self, value: int) -> None: ...
    @property
    def ConnectionLimit(self) -> int:
        """

        :return:
        """
    @ConnectionLimit.setter
    def ConnectionLimit(self, value: int) -> None: ...
    @property
    def ConnectionName(self) -> str:
        """

        :return:
        """
    @property
    def CurrentConnections(self) -> int:
        """

        :return:
        """
    @property
    def Expect100Continue(self) -> bool:
        """

        :return:
        """
    @Expect100Continue.setter
    def Expect100Continue(self, value: bool) -> None: ...
    @property
    def IdleSince(self) -> DateTime:
        """

        :return:
        """
    @property
    def MaxIdleTime(self) -> int:
        """

        :return:
        """
    @MaxIdleTime.setter
    def MaxIdleTime(self, value: int) -> None: ...
    @property
    def ProtocolVersion(self) -> Version:
        """

        :return:
        """
    @property
    def ReceiveBufferSize(self) -> int:
        """

        :return:
        """
    @ReceiveBufferSize.setter
    def ReceiveBufferSize(self, value: int) -> None: ...
    @property
    def SupportsPipelining(self) -> bool:
        """

        :return:
        """
    @property
    def UseNagleAlgorithm(self) -> bool:
        """

        :return:
        """
    @UseNagleAlgorithm.setter
    def UseNagleAlgorithm(self, value: bool) -> None: ...
    def CloseConnectionGroup(self, connectionGroupName: str) -> bool:
        """

        :param connectionGroupName:
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
    def SetTcpKeepAlive(self, enabled: bool, keepAliveTime: int, keepAliveInterval: int) -> None:
        """

        :param enabled:
        :param keepAliveTime:
        :param keepAliveInterval:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class ServicePointManager(Object):
    """"""

    DefaultNonPersistentConnectionLimit: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    DefaultPersistentConnectionLimit: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    @classmethod
    @property
    def CertificatePolicy(cls) -> ICertificatePolicy:
        """

        :return:
        """
    @classmethod
    @CertificatePolicy.setter
    def CertificatePolicy(cls, value: ICertificatePolicy) -> None: ...
    @classmethod
    @property
    def CheckCertificateRevocationList(cls) -> bool:
        """

        :return:
        """
    @classmethod
    @CheckCertificateRevocationList.setter
    def CheckCertificateRevocationList(cls, value: bool) -> None: ...
    @classmethod
    @property
    def DefaultConnectionLimit(cls) -> int:
        """

        :return:
        """
    @classmethod
    @DefaultConnectionLimit.setter
    def DefaultConnectionLimit(cls, value: int) -> None: ...
    @classmethod
    @property
    def DnsRefreshTimeout(cls) -> int:
        """

        :return:
        """
    @classmethod
    @DnsRefreshTimeout.setter
    def DnsRefreshTimeout(cls, value: int) -> None: ...
    @classmethod
    @property
    def EnableDnsRoundRobin(cls) -> bool:
        """

        :return:
        """
    @classmethod
    @EnableDnsRoundRobin.setter
    def EnableDnsRoundRobin(cls, value: bool) -> None: ...
    @classmethod
    @property
    def EncryptionPolicy(cls) -> EncryptionPolicy:
        """

        :return:
        """
    @classmethod
    @property
    def Expect100Continue(cls) -> bool:
        """

        :return:
        """
    @classmethod
    @Expect100Continue.setter
    def Expect100Continue(cls, value: bool) -> None: ...
    @classmethod
    @property
    def MaxServicePointIdleTime(cls) -> int:
        """

        :return:
        """
    @classmethod
    @MaxServicePointIdleTime.setter
    def MaxServicePointIdleTime(cls, value: int) -> None: ...
    @classmethod
    @property
    def MaxServicePoints(cls) -> int:
        """

        :return:
        """
    @classmethod
    @MaxServicePoints.setter
    def MaxServicePoints(cls, value: int) -> None: ...
    @classmethod
    @property
    def ReusePort(cls) -> bool:
        """

        :return:
        """
    @classmethod
    @ReusePort.setter
    def ReusePort(cls, value: bool) -> None: ...
    @classmethod
    @property
    def SecurityProtocol(cls) -> SecurityProtocolType:
        """

        :return:
        """
    @classmethod
    @SecurityProtocol.setter
    def SecurityProtocol(cls, value: SecurityProtocolType) -> None: ...
    @classmethod
    @property
    def ServerCertificateValidationCallback(cls) -> RemoteCertificateValidationCallback:
        """

        :return:
        """
    @classmethod
    @ServerCertificateValidationCallback.setter
    def ServerCertificateValidationCallback(
        cls, value: RemoteCertificateValidationCallback
    ) -> None: ...
    @classmethod
    @property
    def UseNagleAlgorithm(cls) -> bool:
        """

        :return:
        """
    @classmethod
    @UseNagleAlgorithm.setter
    def UseNagleAlgorithm(cls, value: bool) -> None: ...
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @classmethod
    @overload
    def FindServicePoint(cls, address: Uri) -> ServicePoint:
        """

        :param address:
        :return:
        """
    @classmethod
    @overload
    def FindServicePoint(cls, uriString: str, proxy: IWebProxy) -> ServicePoint:
        """

        :param uriString:
        :param proxy:
        :return:
        """
    @classmethod
    @overload
    def FindServicePoint(cls, address: Uri, proxy: IWebProxy) -> ServicePoint:
        """

        :param address:
        :param proxy:
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
    @classmethod
    def SetTcpKeepAlive(cls, enabled: bool, keepAliveTime: int, keepAliveInterval: int) -> None:
        """

        :param enabled:
        :param keepAliveTime:
        :param keepAliveInterval:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class ShellExpression(ValueType):
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

class SocketAddress(Object):
    """"""

    @overload
    def __init__(self, family: AddressFamily):
        """

        :param family:
        """
    @overload
    def __init__(self, family: AddressFamily, size: int):
        """

        :param family:
        :param size:
        """
    @property
    def Family(self) -> AddressFamily:
        """

        :return:
        """
    @property
    def Item(self) -> int:
        """

        :return:
        """
    @Item.setter
    def Item(self, value: int) -> None: ...
    @property
    def Size(self) -> int:
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
    def __getitem__(self, offset: int) -> int:
        """

        :param offset:
        :return:
        """
    def __setitem__(self, offset: int, value: int) -> None:
        """

        :param offset:
        :param value:
        """

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

    AllPorts: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    @overload
    def __init__(self, state: PermissionState):
        """

        :param state:
        """
    @overload
    def __init__(
        self, access: NetworkAccess, transport: TransportType, hostName: str, portNumber: int
    ):
        """

        :param access:
        :param transport:
        :param hostName:
        :param portNumber:
        """
    @property
    def AcceptList(self) -> IEnumerator:
        """

        :return:
        """
    @property
    def ConnectList(self) -> IEnumerator:
        """

        :return:
        """
    def AddPermission(
        self, access: NetworkAccess, transport: TransportType, hostName: str, portNumber: int
    ) -> None:
        """

        :param access:
        :param transport:
        :param hostName:
        :param portNumber:
        """
    def Assert(self) -> None:
        """"""
    def Copy(self) -> IPermission:
        """

        :return:
        """
    @overload
    def Demand(self) -> None:
        """"""
    @overload
    def Demand(self) -> None:
        """"""
    def Deny(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def FromXml(self, e: SecurityElement) -> None:
        """

        :param e:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def Intersect(self, target: IPermission) -> IPermission:
        """

        :param target:
        :return:
        """
    def IsSubsetOf(self, target: IPermission) -> bool:
        """

        :param target:
        :return:
        """
    def IsUnrestricted(self) -> bool:
        """

        :return:
        """
    def PermitOnly(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """
    def ToXml(self) -> SecurityElement:
        """

        :return:
        """
    def Union(self, target: IPermission) -> IPermission:
        """

        :param target:
        :return:
        """

class SocketPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    """"""

    def __init__(self, action: SecurityAction):
        """

        :param action:
        """
    @property
    def Access(self) -> str:
        """

        :return:
        """
    @Access.setter
    def Access(self, value: str) -> None: ...
    @property
    def Action(self) -> SecurityAction:
        """

        :return:
        """
    @Action.setter
    def Action(self, value: SecurityAction) -> None: ...
    @property
    def Host(self) -> str:
        """

        :return:
        """
    @Host.setter
    def Host(self, value: str) -> None: ...
    @property
    def Port(self) -> str:
        """

        :return:
        """
    @Port.setter
    def Port(self, value: str) -> None: ...
    @property
    def Transport(self) -> str:
        """

        :return:
        """
    @Transport.setter
    def Transport(self, value: str) -> None: ...
    @property
    def TypeId(self) -> object:
        """

        :return:
        """
    @property
    def Unrestricted(self) -> bool:
        """

        :return:
        """
    @Unrestricted.setter
    def Unrestricted(self, value: bool) -> None: ...
    def CreatePermission(self) -> IPermission:
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
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """

        :return:
        """
    def Match(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class SplitWritesState(Object):
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

class SpnDictionary(StringDictionary, IEnumerable):
    """"""

    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def IsSynchronized(self) -> bool:
        """

        :return:
        """
    @property
    def Item(self) -> str:
        """

        :return:
        """
    @Item.setter
    def Item(self, value: str) -> None: ...
    @property
    def Keys(self) -> ICollection:
        """

        :return:
        """
    @property
    def SyncRoot(self) -> object:
        """

        :return:
        """
    @property
    def Values(self) -> ICollection:
        """

        :return:
        """
    def Add(self, key: str, value: str) -> None:
        """

        :param key:
        :param value:
        """
    def Clear(self) -> None:
        """"""
    def ContainsKey(self, key: str) -> bool:
        """

        :param key:
        :return:
        """
    def ContainsValue(self, value: str) -> bool:
        """

        :param value:
        :return:
        """
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
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
    def Remove(self, key: str) -> None:
        """

        :param key:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def __getitem__(self, key: str) -> str:
        """

        :param key:
        :return:
        """
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    def __setitem__(self, key: str, value: str) -> None:
        """

        :param key:
        :param value:
        """

class SpnToken(Object):
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

class SslConnectionInfo(Object):
    """"""

    DataCipherAlg: Final[int] = ...
    """
    
    :return: 
    """
    DataHashAlg: Final[int] = ...
    """
    
    :return: 
    """
    DataHashKeySize: Final[int] = ...
    """
    
    :return: 
    """
    DataKeySize: Final[int] = ...
    """
    
    :return: 
    """
    KeyExchKeySize: Final[int] = ...
    """
    
    :return: 
    """
    KeyExchangeAlg: Final[int] = ...
    """
    
    :return: 
    """
    Protocol: Final[int] = ...
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

class SslStreamContext(TransportContext):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetChannelBinding(self, kind: ChannelBindingKind) -> ChannelBinding:
        """

        :param kind:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetTlsTokenBindings(self) -> IEnumerable[TokenBinding]:
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

class StaticProxy(ProxyChain, IEnumerable[Uri], IEnumerable, IDisposable):
    """"""

    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
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
    @overload
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[Uri]:
        """

        :return:
        """

class StreamFramer(Object):
    """"""

    def __init__(self, Transport: Stream):
        """

        :param Transport:
        """
    @property
    def ReadHeader(self) -> FrameHeader:
        """

        :return:
        """
    @property
    def Transport(self) -> Stream:
        """

        :return:
        """
    @property
    def WriteHeader(self) -> FrameHeader:
        """

        :return:
        """
    def BeginReadMessage(self, asyncCallback: AsyncCallback, stateObject: object) -> IAsyncResult:
        """

        :param asyncCallback:
        :param stateObject:
        :return:
        """
    def BeginWriteMessage(
        self, message: Array[int], asyncCallback: AsyncCallback, stateObject: object
    ) -> IAsyncResult:
        """

        :param message:
        :param asyncCallback:
        :param stateObject:
        :return:
        """
    def EndReadMessage(self, asyncResult: IAsyncResult) -> Array[int]:
        """

        :param asyncResult:
        :return:
        """
    def EndWriteMessage(self, asyncResult: IAsyncResult) -> None:
        """

        :param asyncResult:
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
    def ReadMessage(self) -> Array[int]:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def WriteMessage(self, message: Array[int]) -> None:
        """

        :param message:
        """

class StreamSizes(Object):
    """"""

    SizeOf: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    blockSize: Final[int] = ...
    """
    
    :return: 
    """
    buffersCount: Final[int] = ...
    """
    
    :return: 
    """
    header: Final[int] = ...
    """
    
    :return: 
    """
    maximumMessage: Final[int] = ...
    """
    
    :return: 
    """
    trailer: Final[int] = ...
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

class SyncMemoryStream(MemoryStream, IRequestLifetimeTracker, IDisposable):
    """"""

    @property
    def CanRead(self) -> bool:
        """

        :return:
        """
    @property
    def CanSeek(self) -> bool:
        """

        :return:
        """
    @property
    def CanTimeout(self) -> bool:
        """

        :return:
        """
    @property
    def CanWrite(self) -> bool:
        """

        :return:
        """
    @property
    def Capacity(self) -> int:
        """

        :return:
        """
    @Capacity.setter
    def Capacity(self, value: int) -> None: ...
    @property
    def Length(self) -> int:
        """

        :return:
        """
    @property
    def Position(self) -> int:
        """

        :return:
        """
    @Position.setter
    def Position(self, value: int) -> None: ...
    @property
    def ReadTimeout(self) -> int:
        """

        :return:
        """
    @ReadTimeout.setter
    def ReadTimeout(self, value: int) -> None: ...
    @property
    def WriteTimeout(self) -> int:
        """

        :return:
        """
    @WriteTimeout.setter
    def WriteTimeout(self, value: int) -> None: ...
    def BeginRead(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """

        :param buffer:
        :param offset:
        :param count:
        :param callback:
        :param state:
        :return:
        """
    def BeginWrite(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """

        :param buffer:
        :param offset:
        :param count:
        :param callback:
        :param state:
        :return:
        """
    def Close(self) -> None:
        """"""
    @overload
    def CopyTo(self, destination: Stream) -> None:
        """

        :param destination:
        """
    @overload
    def CopyTo(self, destination: Stream, bufferSize: int) -> None:
        """

        :param destination:
        :param bufferSize:
        """
    @overload
    def CopyToAsync(self, destination: Stream) -> Task:
        """

        :param destination:
        :return:
        """
    @overload
    def CopyToAsync(self, destination: Stream, bufferSize: int) -> Task:
        """

        :param destination:
        :param bufferSize:
        :return:
        """
    @overload
    def CopyToAsync(
        self, destination: Stream, bufferSize: int, cancellationToken: CancellationToken
    ) -> Task:
        """

        :param destination:
        :param bufferSize:
        :param cancellationToken:
        :return:
        """
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """

        :param requestedType:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    def EndRead(self, asyncResult: IAsyncResult) -> int:
        """

        :param asyncResult:
        :return:
        """
    def EndWrite(self, asyncResult: IAsyncResult) -> None:
        """

        :param asyncResult:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def Flush(self) -> None:
        """"""
    @overload
    def FlushAsync(self) -> Task:
        """

        :return:
        """
    @overload
    def FlushAsync(self, cancellationToken: CancellationToken) -> Task:
        """

        :param cancellationToken:
        :return:
        """
    def GetBuffer(self) -> Array[int]:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetLifetimeService(self) -> object:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def InitializeLifetimeService(self) -> object:
        """

        :return:
        """
    def Read(self, buffer: Array[int], offset: int, count: int) -> Tuple[int, Array[int]]:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def ReadAsync(self, buffer: Array[int], offset: int, count: int) -> Task[int]:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def ReadAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task[int]:
        """

        :param buffer:
        :param offset:
        :param count:
        :param cancellationToken:
        :return:
        """
    def ReadByte(self) -> int:
        """

        :return:
        """
    def Seek(self, offset: int, origin: SeekOrigin) -> int:
        """

        :param offset:
        :param origin:
        :return:
        """
    def SetLength(self, value: int) -> None:
        """

        :param value:
        """
    def ToArray(self) -> Array[int]:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def TrackRequestLifetime(self, requestStartTimestamp: int) -> None:
        """

        :param requestStartTimestamp:
        """
    def TryGetBuffer(self, buffer: ArraySegment[int]) -> Tuple[bool, ArraySegment[int]]:
        """

        :param buffer:
        :return:
        """
    def Write(self, buffer: Array[int], offset: int, count: int) -> None:
        """

        :param buffer:
        :param offset:
        :param count:
        """
    @overload
    def WriteAsync(self, buffer: Array[int], offset: int, count: int) -> Task:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def WriteAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task:
        """

        :param buffer:
        :param offset:
        :param count:
        :param cancellationToken:
        :return:
        """
    def WriteByte(self, value: int) -> None:
        """

        :param value:
        """
    def WriteTo(self, stream: Stream) -> None:
        """

        :param stream:
        """

class SyncRequestContext(RequestContextBase, IDisposable):
    """"""

    def Close(self) -> None:
        """"""
    def Dispose(self) -> None:
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

class SystemNetworkCredential(NetworkCredential, ICredentials, ICredentialsByHost):
    """"""

    @property
    def Domain(self) -> str:
        """

        :return:
        """
    @Domain.setter
    def Domain(self, value: str) -> None: ...
    @property
    def Password(self) -> str:
        """

        :return:
        """
    @Password.setter
    def Password(self, value: str) -> None: ...
    @property
    def SecurePassword(self) -> SecureString:
        """

        :return:
        """
    @SecurePassword.setter
    def SecurePassword(self, value: SecureString) -> None: ...
    @property
    def UserName(self) -> str:
        """

        :return:
        """
    @UserName.setter
    def UserName(self, value: str) -> None: ...
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetCredential(self, uri: Uri, authType: str) -> NetworkCredential:
        """

        :param uri:
        :param authType:
        :return:
        """
    @overload
    def GetCredential(self, host: str, port: int, authenticationType: str) -> NetworkCredential:
        """

        :param host:
        :param port:
        :param authenticationType:
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
    def Validate(self, value: object) -> None:
        """"""

class TimerThread(ABC, Object):
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

class TlsParamaters(ValueType):
    """"""

    cAlpnIds: Final[int] = ...
    """
    
    :return: 
    """
    cDisabledCrypto: Final[int] = ...
    """
    
    :return: 
    """
    dwFlags: Final[TlsParamaters.Flags] = ...
    """
    
    :return: 
    """
    grbitDisabledProtocols: Final[int] = ...
    """
    
    :return: 
    """
    pDisabledCrypto: Final[IntPtr] = ...
    """
    
    :return: 
    """
    rgstrAlpnIds: Final[IntPtr] = ...
    """
    
    :return: 
    """
    def __init__(self, protocols: SchProtocols):
        """

        :param protocols:
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

    class Flags(Enum):
        """"""

        Zero: Flags = ...
        """"""
        TLS_PARAMS_OPTIONAL: Flags = ...
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
    ):
        """

        :param destinationHost:
        :param networkStream:
        :param checkCertificateRevocationList:
        :param sslProtocols:
        :param clientCertificates:
        :param servicePoint:
        :param initiatingRequest:
        :param executionContext:
        """
    @property
    def CanRead(self) -> bool:
        """

        :return:
        """
    @property
    def CanSeek(self) -> bool:
        """

        :return:
        """
    @property
    def CanTimeout(self) -> bool:
        """

        :return:
        """
    @property
    def CanWrite(self) -> bool:
        """

        :return:
        """
    @property
    def ClientCertificate(self) -> X509Certificate:
        """

        :return:
        """
    @property
    def DataAvailable(self) -> bool:
        """

        :return:
        """
    @property
    def Length(self) -> int:
        """

        :return:
        """
    @property
    def Position(self) -> int:
        """

        :return:
        """
    @Position.setter
    def Position(self, value: int) -> None: ...
    @property
    def ReadTimeout(self) -> int:
        """

        :return:
        """
    @ReadTimeout.setter
    def ReadTimeout(self, value: int) -> None: ...
    @property
    def WriteTimeout(self) -> int:
        """

        :return:
        """
    @WriteTimeout.setter
    def WriteTimeout(self, value: int) -> None: ...
    def BeginRead(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """

        :param buffer:
        :param offset:
        :param count:
        :param callback:
        :param state:
        :return:
        """
    def BeginWrite(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """

        :param buffer:
        :param offset:
        :param count:
        :param callback:
        :param state:
        :return:
        """
    @overload
    def Close(self) -> None:
        """"""
    @overload
    def Close(self, timeout: int) -> None:
        """

        :param timeout:
        """
    @overload
    def CopyTo(self, destination: Stream) -> None:
        """

        :param destination:
        """
    @overload
    def CopyTo(self, destination: Stream, bufferSize: int) -> None:
        """

        :param destination:
        :param bufferSize:
        """
    @overload
    def CopyToAsync(self, destination: Stream) -> Task:
        """

        :param destination:
        :return:
        """
    @overload
    def CopyToAsync(self, destination: Stream, bufferSize: int) -> Task:
        """

        :param destination:
        :param bufferSize:
        :return:
        """
    @overload
    def CopyToAsync(
        self, destination: Stream, bufferSize: int, cancellationToken: CancellationToken
    ) -> Task:
        """

        :param destination:
        :param bufferSize:
        :param cancellationToken:
        :return:
        """
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """

        :param requestedType:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    def EndRead(self, asyncResult: IAsyncResult) -> int:
        """

        :param asyncResult:
        :return:
        """
    def EndWrite(self, asyncResult: IAsyncResult) -> None:
        """

        :param asyncResult:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def Flush(self) -> None:
        """"""
    @overload
    def FlushAsync(self) -> Task:
        """

        :return:
        """
    @overload
    def FlushAsync(self, cancellationToken: CancellationToken) -> Task:
        """

        :param cancellationToken:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetLifetimeService(self) -> object:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def InitializeLifetimeService(self) -> object:
        """

        :return:
        """
    def Read(self, buffer: Array[int], offset: int, count: int) -> Tuple[int, Array[int]]:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def ReadAsync(self, buffer: Array[int], offset: int, count: int) -> Task[int]:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def ReadAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task[int]:
        """

        :param buffer:
        :param offset:
        :param count:
        :param cancellationToken:
        :return:
        """
    def ReadByte(self) -> int:
        """

        :return:
        """
    def Seek(self, offset: int, origin: SeekOrigin) -> int:
        """

        :param offset:
        :param origin:
        :return:
        """
    def SetLength(self, value: int) -> None:
        """

        :param value:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Write(self, buffer: Array[int], offset: int, count: int) -> None:
        """

        :param buffer:
        :param offset:
        :param count:
        """
    @overload
    def WriteAsync(self, buffer: Array[int], offset: int, count: int) -> Task:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def WriteAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task:
        """

        :param buffer:
        :param offset:
        :param count:
        :param cancellationToken:
        :return:
        """
    def WriteByte(self, value: int) -> None:
        """

        :param value:
        """

class TrackingStringDictionary(StringDictionary, IEnumerable):
    """"""

    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def IsSynchronized(self) -> bool:
        """

        :return:
        """
    @property
    def Item(self) -> str:
        """

        :return:
        """
    @Item.setter
    def Item(self, value: str) -> None: ...
    @property
    def Keys(self) -> ICollection:
        """

        :return:
        """
    @property
    def SyncRoot(self) -> object:
        """

        :return:
        """
    @property
    def Values(self) -> ICollection:
        """

        :return:
        """
    def Add(self, key: str, value: str) -> None:
        """

        :param key:
        :param value:
        """
    def Clear(self) -> None:
        """"""
    def ContainsKey(self, key: str) -> bool:
        """

        :param key:
        :return:
        """
    def ContainsValue(self, value: str) -> bool:
        """

        :param value:
        :return:
        """
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
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
    def Remove(self, key: str) -> None:
        """

        :param key:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def __getitem__(self, key: str) -> str:
        """

        :param key:
        :return:
        """
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    def __setitem__(self, key: str, value: str) -> None:
        """

        :param key:
        :param value:
        """

class TrackingValidationObjectDictionary(StringDictionary, IEnumerable):
    """"""

    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def IsSynchronized(self) -> bool:
        """

        :return:
        """
    @property
    def Item(self) -> str:
        """

        :return:
        """
    @Item.setter
    def Item(self, value: str) -> None: ...
    @property
    def Keys(self) -> ICollection:
        """

        :return:
        """
    @property
    def SyncRoot(self) -> object:
        """

        :return:
        """
    @property
    def Values(self) -> ICollection:
        """

        :return:
        """
    def Add(self, key: str, value: str) -> None:
        """

        :param key:
        :param value:
        """
    def Clear(self) -> None:
        """"""
    def ContainsKey(self, key: str) -> bool:
        """

        :param key:
        :return:
        """
    def ContainsValue(self, value: str) -> bool:
        """

        :param value:
        :return:
        """
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
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
    def Remove(self, key: str) -> None:
        """

        :param key:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def __getitem__(self, key: str) -> str:
        """

        :param key:
        :return:
        """
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    def __setitem__(self, key: str, value: str) -> None:
        """

        :param key:
        :param value:
        """

class TransmitFileBuffers(Object):
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

class TransportContext(ABC, Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetChannelBinding(self, kind: ChannelBindingKind) -> ChannelBinding:
        """

        :param kind:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetTlsTokenBindings(self) -> IEnumerable[TokenBinding]:
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

UnlockConnectionDelegate: Callable[[], None] = ...
""""""

class UnsafeNclNativeMethods(ABC, Object):
    """"""

    @classmethod
    def CoCreateInstance(
        cls, clsid: Guid, pUnkOuter: IntPtr, context: int, iid: Guid, o: object
    ) -> Tuple[None, object]:
        """

        :param clsid:
        :param pUnkOuter:
        :param context:
        :param iid:
        :param o:
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

class UploadDataCompletedEventArgs(AsyncCompletedEventArgs):
    """"""

    @property
    def Cancelled(self) -> bool:
        """

        :return:
        """
    @property
    def Error(self) -> Exception:
        """

        :return:
        """
    @property
    def Result(self) -> Array[int]:
        """

        :return:
        """
    @property
    def UserState(self) -> object:
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

UploadDataCompletedEventHandler: Callable[[object, UploadDataCompletedEventArgs], None] = ...
"""

:param sender: 
:param e: 
"""

class UploadFileCompletedEventArgs(AsyncCompletedEventArgs):
    """"""

    @property
    def Cancelled(self) -> bool:
        """

        :return:
        """
    @property
    def Error(self) -> Exception:
        """

        :return:
        """
    @property
    def Result(self) -> Array[int]:
        """

        :return:
        """
    @property
    def UserState(self) -> object:
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

UploadFileCompletedEventHandler: Callable[[object, UploadFileCompletedEventArgs], None] = ...
"""

:param sender: 
:param e: 
"""

class UploadProgressChangedEventArgs(ProgressChangedEventArgs):
    """"""

    @property
    def BytesReceived(self) -> int:
        """

        :return:
        """
    @property
    def BytesSent(self) -> int:
        """

        :return:
        """
    @property
    def ProgressPercentage(self) -> int:
        """

        :return:
        """
    @property
    def TotalBytesToReceive(self) -> int:
        """

        :return:
        """
    @property
    def TotalBytesToSend(self) -> int:
        """

        :return:
        """
    @property
    def UserState(self) -> object:
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

UploadProgressChangedEventHandler: Callable[[object, UploadProgressChangedEventArgs], None] = ...
"""

:param sender: 
:param e: 
"""

class UploadStringCompletedEventArgs(AsyncCompletedEventArgs):
    """"""

    @property
    def Cancelled(self) -> bool:
        """

        :return:
        """
    @property
    def Error(self) -> Exception:
        """

        :return:
        """
    @property
    def Result(self) -> str:
        """

        :return:
        """
    @property
    def UserState(self) -> object:
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

UploadStringCompletedEventHandler: Callable[[object, UploadStringCompletedEventArgs], None] = ...
"""

:param sender: 
:param e: 
"""

class UploadValuesCompletedEventArgs(AsyncCompletedEventArgs):
    """"""

    @property
    def Cancelled(self) -> bool:
        """

        :return:
        """
    @property
    def Error(self) -> Exception:
        """

        :return:
        """
    @property
    def Result(self) -> Array[int]:
        """

        :return:
        """
    @property
    def UserState(self) -> object:
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

UploadValuesCompletedEventHandler: Callable[[object, UploadValuesCompletedEventArgs], None] = ...
"""

:param sender: 
:param e: 
"""

class ValidationHelper(ABC, Object):
    """"""

    EmptyArray: Final[ClassVar[Array[str]]] = ...
    """
    
    :return: 
    """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @classmethod
    def ExceptionMessage(cls, exception: Exception) -> str:
        """

        :param exception:
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
    @classmethod
    def HashString(cls, objectValue: object) -> str:
        """

        :param objectValue:
        :return:
        """
    @classmethod
    def IsBlankString(cls, stringValue: str) -> bool:
        """

        :param stringValue:
        :return:
        """
    @classmethod
    def IsInvalidHttpString(cls, stringValue: str) -> bool:
        """

        :param stringValue:
        :return:
        """
    @classmethod
    def MakeEmptyArrayNull(cls, stringArray: Array[str]) -> Array[str]:
        """

        :param stringArray:
        :return:
        """
    @classmethod
    def MakeStringNull(cls, stringValue: str) -> str:
        """

        :param stringValue:
        :return:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """
    @classmethod
    @overload
    def ToString(cls, objectValue: object) -> str:
        """

        :param objectValue:
        :return:
        """
    @classmethod
    def ValidateRange(cls, actual: int, fromAllowed: int, toAllowed: int) -> bool:
        """

        :param actual:
        :param fromAllowed:
        :param toAllowed:
        :return:
        """
    @classmethod
    def ValidateTcpPort(cls, port: int) -> bool:
        """

        :param port:
        :return:
        """

class WSABuffer(ValueType):
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

class WSAData(ValueType):
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

class WebClient(Component, IComponent, IDisposable):
    """"""

    def __init__(self):
        """"""
    @property
    def AllowReadStreamBuffering(self) -> bool:
        """

        :return:
        """
    @AllowReadStreamBuffering.setter
    def AllowReadStreamBuffering(self, value: bool) -> None: ...
    @property
    def AllowWriteStreamBuffering(self) -> bool:
        """

        :return:
        """
    @AllowWriteStreamBuffering.setter
    def AllowWriteStreamBuffering(self, value: bool) -> None: ...
    @property
    def BaseAddress(self) -> str:
        """

        :return:
        """
    @BaseAddress.setter
    def BaseAddress(self, value: str) -> None: ...
    @property
    def CachePolicy(self) -> RequestCachePolicy:
        """

        :return:
        """
    @CachePolicy.setter
    def CachePolicy(self, value: RequestCachePolicy) -> None: ...
    @property
    def Container(self) -> IContainer:
        """

        :return:
        """
    @property
    def Credentials(self) -> ICredentials:
        """

        :return:
        """
    @Credentials.setter
    def Credentials(self, value: ICredentials) -> None: ...
    @property
    def Encoding(self) -> Encoding:
        """

        :return:
        """
    @Encoding.setter
    def Encoding(self, value: Encoding) -> None: ...
    @property
    def Headers(self) -> WebHeaderCollection:
        """

        :return:
        """
    @Headers.setter
    def Headers(self, value: WebHeaderCollection) -> None: ...
    @property
    def IsBusy(self) -> bool:
        """

        :return:
        """
    @property
    def Proxy(self) -> IWebProxy:
        """

        :return:
        """
    @Proxy.setter
    def Proxy(self, value: IWebProxy) -> None: ...
    @property
    def QueryString(self) -> NameValueCollection:
        """

        :return:
        """
    @QueryString.setter
    def QueryString(self, value: NameValueCollection) -> None: ...
    @property
    def ResponseHeaders(self) -> WebHeaderCollection:
        """

        :return:
        """
    @property
    def Site(self) -> ISite:
        """

        :return:
        """
    @Site.setter
    def Site(self, value: ISite) -> None: ...
    @property
    def UseDefaultCredentials(self) -> bool:
        """

        :return:
        """
    @UseDefaultCredentials.setter
    def UseDefaultCredentials(self, value: bool) -> None: ...
    def CancelAsync(self) -> None:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """

        :param requestedType:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    @overload
    def DownloadData(self, address: str) -> Array[int]:
        """

        :param address:
        :return:
        """
    @overload
    def DownloadData(self, address: Uri) -> Array[int]:
        """

        :param address:
        :return:
        """
    @overload
    def DownloadDataAsync(self, address: Uri) -> None:
        """

        :param address:
        """
    @overload
    def DownloadDataAsync(self, address: Uri, userToken: object) -> None:
        """

        :param address:
        :param userToken:
        """
    @overload
    def DownloadDataTaskAsync(self, address: str) -> Task[Array[int]]:
        """

        :param address:
        :return:
        """
    @overload
    def DownloadDataTaskAsync(self, address: Uri) -> Task[Array[int]]:
        """

        :param address:
        :return:
        """
    @overload
    def DownloadFile(self, address: str, fileName: str) -> None:
        """

        :param address:
        :param fileName:
        """
    @overload
    def DownloadFile(self, address: Uri, fileName: str) -> None:
        """

        :param address:
        :param fileName:
        """
    @overload
    def DownloadFileAsync(self, address: Uri, fileName: str) -> None:
        """

        :param address:
        :param fileName:
        """
    @overload
    def DownloadFileAsync(self, address: Uri, fileName: str, userToken: object) -> None:
        """

        :param address:
        :param fileName:
        :param userToken:
        """
    @overload
    def DownloadFileTaskAsync(self, address: str, fileName: str) -> Task:
        """

        :param address:
        :param fileName:
        :return:
        """
    @overload
    def DownloadFileTaskAsync(self, address: Uri, fileName: str) -> Task:
        """

        :param address:
        :param fileName:
        :return:
        """
    @overload
    def DownloadString(self, address: str) -> str:
        """

        :param address:
        :return:
        """
    @overload
    def DownloadString(self, address: Uri) -> str:
        """

        :param address:
        :return:
        """
    @overload
    def DownloadStringAsync(self, address: Uri) -> None:
        """

        :param address:
        """
    @overload
    def DownloadStringAsync(self, address: Uri, userToken: object) -> None:
        """

        :param address:
        :param userToken:
        """
    @overload
    def DownloadStringTaskAsync(self, address: str) -> Task[str]:
        """

        :param address:
        :return:
        """
    @overload
    def DownloadStringTaskAsync(self, address: Uri) -> Task[str]:
        """

        :param address:
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
    def GetLifetimeService(self) -> object:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def InitializeLifetimeService(self) -> object:
        """

        :return:
        """
    @overload
    def OpenRead(self, address: str) -> Stream:
        """

        :param address:
        :return:
        """
    @overload
    def OpenRead(self, address: Uri) -> Stream:
        """

        :param address:
        :return:
        """
    @overload
    def OpenReadAsync(self, address: Uri) -> None:
        """

        :param address:
        """
    @overload
    def OpenReadAsync(self, address: Uri, userToken: object) -> None:
        """

        :param address:
        :param userToken:
        """
    @overload
    def OpenReadTaskAsync(self, address: str) -> Task[Stream]:
        """

        :param address:
        :return:
        """
    @overload
    def OpenReadTaskAsync(self, address: Uri) -> Task[Stream]:
        """

        :param address:
        :return:
        """
    @overload
    def OpenWrite(self, address: str) -> Stream:
        """

        :param address:
        :return:
        """
    @overload
    def OpenWrite(self, address: Uri) -> Stream:
        """

        :param address:
        :return:
        """
    @overload
    def OpenWrite(self, address: str, method: str) -> Stream:
        """

        :param address:
        :param method:
        :return:
        """
    @overload
    def OpenWrite(self, address: Uri, method: str) -> Stream:
        """

        :param address:
        :param method:
        :return:
        """
    @overload
    def OpenWriteAsync(self, address: Uri) -> None:
        """

        :param address:
        """
    @overload
    def OpenWriteAsync(self, address: Uri, method: str) -> None:
        """

        :param address:
        :param method:
        """
    @overload
    def OpenWriteAsync(self, address: Uri, method: str, userToken: object) -> None:
        """

        :param address:
        :param method:
        :param userToken:
        """
    @overload
    def OpenWriteTaskAsync(self, address: str) -> Task[Stream]:
        """

        :param address:
        :return:
        """
    @overload
    def OpenWriteTaskAsync(self, address: Uri) -> Task[Stream]:
        """

        :param address:
        :return:
        """
    @overload
    def OpenWriteTaskAsync(self, address: str, method: str) -> Task[Stream]:
        """

        :param address:
        :param method:
        :return:
        """
    @overload
    def OpenWriteTaskAsync(self, address: Uri, method: str) -> Task[Stream]:
        """

        :param address:
        :param method:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def UploadData(self, address: str, data: Array[int]) -> Array[int]:
        """

        :param address:
        :param data:
        :return:
        """
    @overload
    def UploadData(self, address: Uri, data: Array[int]) -> Array[int]:
        """

        :param address:
        :param data:
        :return:
        """
    @overload
    def UploadData(self, address: str, method: str, data: Array[int]) -> Array[int]:
        """

        :param address:
        :param method:
        :param data:
        :return:
        """
    @overload
    def UploadData(self, address: Uri, method: str, data: Array[int]) -> Array[int]:
        """

        :param address:
        :param method:
        :param data:
        :return:
        """
    @overload
    def UploadDataAsync(self, address: Uri, data: Array[int]) -> None:
        """

        :param address:
        :param data:
        """
    @overload
    def UploadDataAsync(self, address: Uri, method: str, data: Array[int]) -> None:
        """

        :param address:
        :param method:
        :param data:
        """
    @overload
    def UploadDataAsync(
        self, address: Uri, method: str, data: Array[int], userToken: object
    ) -> None:
        """

        :param address:
        :param method:
        :param data:
        :param userToken:
        """
    @overload
    def UploadDataTaskAsync(self, address: str, data: Array[int]) -> Task[Array[int]]:
        """

        :param address:
        :param data:
        :return:
        """
    @overload
    def UploadDataTaskAsync(self, address: Uri, data: Array[int]) -> Task[Array[int]]:
        """

        :param address:
        :param data:
        :return:
        """
    @overload
    def UploadDataTaskAsync(self, address: str, method: str, data: Array[int]) -> Task[Array[int]]:
        """

        :param address:
        :param method:
        :param data:
        :return:
        """
    @overload
    def UploadDataTaskAsync(self, address: Uri, method: str, data: Array[int]) -> Task[Array[int]]:
        """

        :param address:
        :param method:
        :param data:
        :return:
        """
    @overload
    def UploadFile(self, address: str, fileName: str) -> Array[int]:
        """

        :param address:
        :param fileName:
        :return:
        """
    @overload
    def UploadFile(self, address: Uri, fileName: str) -> Array[int]:
        """

        :param address:
        :param fileName:
        :return:
        """
    @overload
    def UploadFile(self, address: str, method: str, fileName: str) -> Array[int]:
        """

        :param address:
        :param method:
        :param fileName:
        :return:
        """
    @overload
    def UploadFile(self, address: Uri, method: str, fileName: str) -> Array[int]:
        """

        :param address:
        :param method:
        :param fileName:
        :return:
        """
    @overload
    def UploadFileAsync(self, address: Uri, fileName: str) -> None:
        """

        :param address:
        :param fileName:
        """
    @overload
    def UploadFileAsync(self, address: Uri, method: str, fileName: str) -> None:
        """

        :param address:
        :param method:
        :param fileName:
        """
    @overload
    def UploadFileAsync(self, address: Uri, method: str, fileName: str, userToken: object) -> None:
        """

        :param address:
        :param method:
        :param fileName:
        :param userToken:
        """
    @overload
    def UploadFileTaskAsync(self, address: str, fileName: str) -> Task[Array[int]]:
        """

        :param address:
        :param fileName:
        :return:
        """
    @overload
    def UploadFileTaskAsync(self, address: Uri, fileName: str) -> Task[Array[int]]:
        """

        :param address:
        :param fileName:
        :return:
        """
    @overload
    def UploadFileTaskAsync(self, address: str, method: str, fileName: str) -> Task[Array[int]]:
        """

        :param address:
        :param method:
        :param fileName:
        :return:
        """
    @overload
    def UploadFileTaskAsync(self, address: Uri, method: str, fileName: str) -> Task[Array[int]]:
        """

        :param address:
        :param method:
        :param fileName:
        :return:
        """
    @overload
    def UploadString(self, address: str, data: str) -> str:
        """

        :param address:
        :param data:
        :return:
        """
    @overload
    def UploadString(self, address: Uri, data: str) -> str:
        """

        :param address:
        :param data:
        :return:
        """
    @overload
    def UploadString(self, address: str, method: str, data: str) -> str:
        """

        :param address:
        :param method:
        :param data:
        :return:
        """
    @overload
    def UploadString(self, address: Uri, method: str, data: str) -> str:
        """

        :param address:
        :param method:
        :param data:
        :return:
        """
    @overload
    def UploadStringAsync(self, address: Uri, data: str) -> None:
        """

        :param address:
        :param data:
        """
    @overload
    def UploadStringAsync(self, address: Uri, method: str, data: str) -> None:
        """

        :param address:
        :param method:
        :param data:
        """
    @overload
    def UploadStringAsync(self, address: Uri, method: str, data: str, userToken: object) -> None:
        """

        :param address:
        :param method:
        :param data:
        :param userToken:
        """
    @overload
    def UploadStringTaskAsync(self, address: str, data: str) -> Task[str]:
        """

        :param address:
        :param data:
        :return:
        """
    @overload
    def UploadStringTaskAsync(self, address: Uri, data: str) -> Task[str]:
        """

        :param address:
        :param data:
        :return:
        """
    @overload
    def UploadStringTaskAsync(self, address: str, method: str, data: str) -> Task[str]:
        """

        :param address:
        :param method:
        :param data:
        :return:
        """
    @overload
    def UploadStringTaskAsync(self, address: Uri, method: str, data: str) -> Task[str]:
        """

        :param address:
        :param method:
        :param data:
        :return:
        """
    @overload
    def UploadValues(self, address: str, data: NameValueCollection) -> Array[int]:
        """

        :param address:
        :param data:
        :return:
        """
    @overload
    def UploadValues(self, address: Uri, data: NameValueCollection) -> Array[int]:
        """

        :param address:
        :param data:
        :return:
        """
    @overload
    def UploadValues(self, address: str, method: str, data: NameValueCollection) -> Array[int]:
        """

        :param address:
        :param method:
        :param data:
        :return:
        """
    @overload
    def UploadValues(self, address: Uri, method: str, data: NameValueCollection) -> Array[int]:
        """

        :param address:
        :param method:
        :param data:
        :return:
        """
    @overload
    def UploadValuesAsync(self, address: Uri, data: NameValueCollection) -> None:
        """

        :param address:
        :param data:
        """
    @overload
    def UploadValuesAsync(self, address: Uri, method: str, data: NameValueCollection) -> None:
        """

        :param address:
        :param method:
        :param data:
        """
    @overload
    def UploadValuesAsync(
        self, address: Uri, method: str, data: NameValueCollection, userToken: object
    ) -> None:
        """

        :param address:
        :param method:
        :param data:
        :param userToken:
        """
    @overload
    def UploadValuesTaskAsync(self, address: str, data: NameValueCollection) -> Task[Array[int]]:
        """

        :param address:
        :param data:
        :return:
        """
    @overload
    def UploadValuesTaskAsync(self, address: Uri, data: NameValueCollection) -> Task[Array[int]]:
        """

        :param address:
        :param data:
        :return:
        """
    @overload
    def UploadValuesTaskAsync(
        self, address: str, method: str, data: NameValueCollection
    ) -> Task[Array[int]]:
        """

        :param address:
        :param method:
        :param data:
        :return:
        """
    @overload
    def UploadValuesTaskAsync(
        self, address: Uri, method: str, data: NameValueCollection
    ) -> Task[Array[int]]:
        """

        :param address:
        :param method:
        :param data:
        :return:
        """
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
    def __init__(self):
        """"""
    @overload
    def __init__(self, message: str):
        """

        :param message:
        """
    @overload
    def __init__(self, message: str, status: WebExceptionStatus):
        """

        :param message:
        :param status:
        """
    @overload
    def __init__(self, message: str, innerException: Exception):
        """

        :param message:
        :param innerException:
        """
    @overload
    def __init__(
        self,
        message: str,
        innerException: Exception,
        status: WebExceptionStatus,
        response: WebResponse,
    ):
        """

        :param message:
        :param innerException:
        :param status:
        :param response:
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
    def Response(self) -> WebResponse:
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
    def Status(self) -> WebExceptionStatus:
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

    def __init__(self):
        """"""
    @property
    def AllKeys(self) -> Array[str]:
        """

        :return:
        """
    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def IsSynchronized(self) -> bool:
        """

        :return:
        """
    @property
    def Item(self) -> str:
        """

        :return:
        """
    @Item.setter
    def Item(self, value: str) -> None: ...
    @property
    def Keys(self) -> NameObjectCollectionBase.KeysCollection:
        """

        :return:
        """
    @property
    def SyncRoot(self) -> object:
        """

        :return:
        """
    @overload
    def Add(self, c: NameValueCollection) -> None:
        """

        :param c:
        """
    @overload
    def Add(self, header: str) -> None:
        """

        :param header:
        """
    @overload
    def Add(self, header: HttpRequestHeader, value: str) -> None:
        """

        :param header:
        :param value:
        """
    @overload
    def Add(self, header: HttpResponseHeader, value: str) -> None:
        """

        :param header:
        :param value:
        """
    @overload
    def Add(self, name: str, value: str) -> None:
        """

        :param name:
        :param value:
        """
    def Clear(self) -> None:
        """"""
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def Get(self, index: int) -> str:
        """

        :param index:
        :return:
        """
    @overload
    def Get(self, name: str) -> str:
        """

        :param name:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetKey(self, index: int) -> str:
        """

        :param index:
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
    def GetValues(self, index: int) -> Array[str]:
        """

        :param index:
        :return:
        """
    @overload
    def GetValues(self, name: str) -> Array[str]:
        """

        :param name:
        :return:
        """
    def HasKeys(self) -> bool:
        """

        :return:
        """
    @classmethod
    @overload
    def IsRestricted(cls, headerName: str) -> bool:
        """

        :param headerName:
        :return:
        """
    @classmethod
    @overload
    def IsRestricted(cls, headerName: str, response: bool) -> bool:
        """

        :param headerName:
        :param response:
        :return:
        """
    def OnDeserialization(self, sender: object) -> None:
        """

        :param sender:
        """
    @overload
    def Remove(self, header: HttpRequestHeader) -> None:
        """

        :param header:
        """
    @overload
    def Remove(self, header: HttpResponseHeader) -> None:
        """

        :param header:
        """
    @overload
    def Remove(self, name: str) -> None:
        """

        :param name:
        """
    @overload
    def Set(self, header: HttpRequestHeader, value: str) -> None:
        """

        :param header:
        :param value:
        """
    @overload
    def Set(self, header: HttpResponseHeader, value: str) -> None:
        """

        :param header:
        :param value:
        """
    @overload
    def Set(self, name: str, value: str) -> None:
        """

        :param name:
        :param value:
        """
    def ToByteArray(self) -> Array[int]:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def __contains__(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def __getitem__(self, header: HttpRequestHeader) -> str:
        """

        :param header:
        :return:
        """
    @overload
    def __getitem__(self, header: HttpResponseHeader) -> str:
        """

        :param header:
        :return:
        """
    @overload
    def __getitem__(self, index: int) -> str:
        """

        :param index:
        :return:
        """
    @overload
    def __getitem__(self, name: str) -> str:
        """

        :param name:
        :return:
        """
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    def __len__(self) -> int:
        """

        :return:
        """
    @overload
    def __setitem__(self, header: HttpRequestHeader, value: str) -> None:
        """

        :param header:
        :param value:
        """
    @overload
    def __setitem__(self, header: HttpResponseHeader, value: str) -> None:
        """

        :param header:
        :param value:
        """
    @overload
    def __setitem__(self, name: str, value: str) -> None:
        """

        :param name:
        :param value:
        """

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

    Code: Final[WebParseErrorCode] = ...
    """
    
    :return: 
    """
    Section: Final[WebParseErrorSection] = ...
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
    def __init__(self):
        """"""
    @overload
    def __init__(self, state: PermissionState):
        """

        :param state:
        """
    @overload
    def __init__(self, access: NetworkAccess, uriRegex: Regex):
        """

        :param access:
        :param uriRegex:
        """
    @overload
    def __init__(self, access: NetworkAccess, uriString: str):
        """

        :param access:
        :param uriString:
        """
    @property
    def AcceptList(self) -> IEnumerator:
        """

        :return:
        """
    @property
    def ConnectList(self) -> IEnumerator:
        """

        :return:
        """
    @overload
    def AddPermission(self, access: NetworkAccess, uriRegex: Regex) -> None:
        """

        :param access:
        :param uriRegex:
        """
    @overload
    def AddPermission(self, access: NetworkAccess, uriString: str) -> None:
        """

        :param access:
        :param uriString:
        """
    def Assert(self) -> None:
        """"""
    def Copy(self) -> IPermission:
        """

        :return:
        """
    @overload
    def Demand(self) -> None:
        """"""
    @overload
    def Demand(self) -> None:
        """"""
    def Deny(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def FromXml(self, e: SecurityElement) -> None:
        """

        :param e:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def Intersect(self, target: IPermission) -> IPermission:
        """

        :param target:
        :return:
        """
    def IsSubsetOf(self, target: IPermission) -> bool:
        """

        :param target:
        :return:
        """
    def IsUnrestricted(self) -> bool:
        """

        :return:
        """
    def PermitOnly(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """
    def ToXml(self) -> SecurityElement:
        """

        :return:
        """
    def Union(self, target: IPermission) -> IPermission:
        """

        :param target:
        :return:
        """

class WebPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    """"""

    def __init__(self, action: SecurityAction):
        """

        :param action:
        """
    @property
    def Accept(self) -> str:
        """

        :return:
        """
    @Accept.setter
    def Accept(self, value: str) -> None: ...
    @property
    def AcceptPattern(self) -> str:
        """

        :return:
        """
    @AcceptPattern.setter
    def AcceptPattern(self, value: str) -> None: ...
    @property
    def Action(self) -> SecurityAction:
        """

        :return:
        """
    @Action.setter
    def Action(self, value: SecurityAction) -> None: ...
    @property
    def Connect(self) -> str:
        """

        :return:
        """
    @Connect.setter
    def Connect(self, value: str) -> None: ...
    @property
    def ConnectPattern(self) -> str:
        """

        :return:
        """
    @ConnectPattern.setter
    def ConnectPattern(self, value: str) -> None: ...
    @property
    def TypeId(self) -> object:
        """

        :return:
        """
    @property
    def Unrestricted(self) -> bool:
        """

        :return:
        """
    @Unrestricted.setter
    def Unrestricted(self, value: bool) -> None: ...
    def CreatePermission(self) -> IPermission:
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
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """

        :return:
        """
    def Match(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class WebProxy(Object, IAutoWebProxy, IWebProxy, ISerializable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, Address: str):
        """

        :param Address:
        """
    @overload
    def __init__(self, Address: Uri):
        """

        :param Address:
        """
    @overload
    def __init__(self, Address: str, BypassOnLocal: bool):
        """

        :param Address:
        :param BypassOnLocal:
        """
    @overload
    def __init__(self, Host: str, Port: int):
        """

        :param Host:
        :param Port:
        """
    @overload
    def __init__(self, Address: Uri, BypassOnLocal: bool):
        """

        :param Address:
        :param BypassOnLocal:
        """
    @overload
    def __init__(self, Address: str, BypassOnLocal: bool, BypassList: Array[str]):
        """

        :param Address:
        :param BypassOnLocal:
        :param BypassList:
        """
    @overload
    def __init__(self, Address: Uri, BypassOnLocal: bool, BypassList: Array[str]):
        """

        :param Address:
        :param BypassOnLocal:
        :param BypassList:
        """
    @overload
    def __init__(
        self, Address: str, BypassOnLocal: bool, BypassList: Array[str], Credentials: ICredentials
    ):
        """

        :param Address:
        :param BypassOnLocal:
        :param BypassList:
        :param Credentials:
        """
    @overload
    def __init__(
        self, Address: Uri, BypassOnLocal: bool, BypassList: Array[str], Credentials: ICredentials
    ):
        """

        :param Address:
        :param BypassOnLocal:
        :param BypassList:
        :param Credentials:
        """
    @property
    def Address(self) -> Uri:
        """

        :return:
        """
    @Address.setter
    def Address(self, value: Uri) -> None: ...
    @property
    def BypassArrayList(self) -> ArrayList:
        """

        :return:
        """
    @property
    def BypassList(self) -> Array[str]:
        """

        :return:
        """
    @BypassList.setter
    def BypassList(self, value: Array[str]) -> None: ...
    @property
    def BypassProxyOnLocal(self) -> bool:
        """

        :return:
        """
    @BypassProxyOnLocal.setter
    def BypassProxyOnLocal(self, value: bool) -> None: ...
    @property
    def Credentials(self) -> ICredentials:
        """

        :return:
        """
    @Credentials.setter
    def Credentials(self, value: ICredentials) -> None: ...
    @property
    def UseDefaultCredentials(self) -> bool:
        """

        :return:
        """
    @UseDefaultCredentials.setter
    def UseDefaultCredentials(self, value: bool) -> None: ...
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @classmethod
    def GetDefaultProxy(cls) -> WebProxy:
        """

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
    def GetProxies(self, destination: Uri) -> ProxyChain:
        """

        :param destination:
        :return:
        """
    def GetProxy(self, destination: Uri) -> Uri:
        """

        :param destination:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def IsBypassed(self, host: Uri) -> bool:
        """

        :param host:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class WebProxyData(Object):
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

class WebProxyDataBuilder(ABC, Object):
    """"""

    def Build(self) -> WebProxyData:
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

class WebProxyScriptHelper(Object, IReflect):
    """"""

    def __init__(self):
        """"""
    @property
    def UnderlyingSystemType(self) -> Type:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetField(self, name: str, bindingAttr: BindingFlags) -> FieldInfo:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    def GetFields(self, bindingAttr: BindingFlags) -> Array[FieldInfo]:
        """

        :param bindingAttr:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetMember(self, name: str, bindingAttr: BindingFlags) -> Array[MemberInfo]:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    def GetMembers(self, bindingAttr: BindingFlags) -> Array[MemberInfo]:
        """

        :param bindingAttr:
        :return:
        """
    @overload
    def GetMethod(self, name: str, bindingAttr: BindingFlags) -> MethodInfo:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetMethod(
        self,
        name: str,
        bindingAttr: BindingFlags,
        binder: Binder,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> MethodInfo:
        """

        :param name:
        :param bindingAttr:
        :param binder:
        :param types:
        :param modifiers:
        :return:
        """
    def GetMethods(self, bindingAttr: BindingFlags) -> Array[MethodInfo]:
        """

        :param bindingAttr:
        :return:
        """
    def GetProperties(self, bindingAttr: BindingFlags) -> Array[PropertyInfo]:
        """

        :param bindingAttr:
        :return:
        """
    @overload
    def GetProperty(self, name: str, bindingAttr: BindingFlags) -> PropertyInfo:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
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
        """

        :param name:
        :param bindingAttr:
        :param binder:
        :param returnType:
        :param types:
        :param modifiers:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
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
        """

        :param name:
        :param invokeAttr:
        :param binder:
        :param target:
        :param args:
        :param modifiers:
        :param culture:
        :param namedParameters:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def dnsDomainIs(self, host: str, domain: str) -> bool:
        """

        :param host:
        :param domain:
        :return:
        """
    def dnsDomainLevels(self, host: str) -> int:
        """

        :param host:
        :return:
        """
    def dnsResolve(self, host: str) -> str:
        """

        :param host:
        :return:
        """
    def dnsResolveEx(self, host: str) -> str:
        """

        :param host:
        :return:
        """
    def getClientVersion(self) -> str:
        """

        :return:
        """
    def isInNet(self, host: str, pattern: str, mask: str) -> bool:
        """

        :param host:
        :param pattern:
        :param mask:
        :return:
        """
    def isInNetEx(self, ipAddress: str, ipPrefix: str) -> bool:
        """

        :param ipAddress:
        :param ipPrefix:
        :return:
        """
    def isPlainHostName(self, hostName: str) -> bool:
        """

        :param hostName:
        :return:
        """
    def isResolvable(self, host: str) -> bool:
        """

        :param host:
        :return:
        """
    def isResolvableEx(self, host: str) -> bool:
        """

        :param host:
        :return:
        """
    def localHostOrDomainIs(self, host: str, hostDom: str) -> bool:
        """

        :param host:
        :param hostDom:
        :return:
        """
    def myIpAddress(self) -> str:
        """

        :return:
        """
    def myIpAddressEx(self) -> str:
        """

        :return:
        """
    def shExpMatch(self, host: str, pattern: str) -> bool:
        """

        :param host:
        :param pattern:
        :return:
        """
    def sortIpAddressList(self, IPAddressList: str) -> str:
        """

        :param IPAddressList:
        :return:
        """
    def weekdayRange(self, wd1: str, wd2: object, gmt: object) -> bool:
        """

        :param wd1:
        :param wd2:
        :param gmt:
        :return:
        """

class WebRequest(ABC, MarshalByRefObject, ISerializable):
    """"""

    @property
    def AuthenticationLevel(self) -> AuthenticationLevel:
        """

        :return:
        """
    @AuthenticationLevel.setter
    def AuthenticationLevel(self, value: AuthenticationLevel) -> None: ...
    @property
    def CachePolicy(self) -> RequestCachePolicy:
        """

        :return:
        """
    @CachePolicy.setter
    def CachePolicy(self, value: RequestCachePolicy) -> None: ...
    @property
    def ConnectionGroupName(self) -> str:
        """

        :return:
        """
    @ConnectionGroupName.setter
    def ConnectionGroupName(self, value: str) -> None: ...
    @property
    def ContentLength(self) -> int:
        """

        :return:
        """
    @ContentLength.setter
    def ContentLength(self, value: int) -> None: ...
    @property
    def ContentType(self) -> str:
        """

        :return:
        """
    @ContentType.setter
    def ContentType(self, value: str) -> None: ...
    @property
    def CreatorInstance(self) -> IWebRequestCreate:
        """

        :return:
        """
    @property
    def Credentials(self) -> ICredentials:
        """

        :return:
        """
    @Credentials.setter
    def Credentials(self, value: ICredentials) -> None: ...
    @classmethod
    @property
    def DefaultCachePolicy(cls) -> RequestCachePolicy:
        """

        :return:
        """
    @classmethod
    @DefaultCachePolicy.setter
    def DefaultCachePolicy(cls, value: RequestCachePolicy) -> None: ...
    @classmethod
    @property
    def DefaultWebProxy(cls) -> IWebProxy:
        """

        :return:
        """
    @classmethod
    @DefaultWebProxy.setter
    def DefaultWebProxy(cls, value: IWebProxy) -> None: ...
    @property
    def Headers(self) -> WebHeaderCollection:
        """

        :return:
        """
    @Headers.setter
    def Headers(self, value: WebHeaderCollection) -> None: ...
    @property
    def ImpersonationLevel(self) -> TokenImpersonationLevel:
        """

        :return:
        """
    @ImpersonationLevel.setter
    def ImpersonationLevel(self, value: TokenImpersonationLevel) -> None: ...
    @property
    def Method(self) -> str:
        """

        :return:
        """
    @Method.setter
    def Method(self, value: str) -> None: ...
    @property
    def PreAuthenticate(self) -> bool:
        """

        :return:
        """
    @PreAuthenticate.setter
    def PreAuthenticate(self, value: bool) -> None: ...
    @property
    def Proxy(self) -> IWebProxy:
        """

        :return:
        """
    @Proxy.setter
    def Proxy(self, value: IWebProxy) -> None: ...
    @property
    def RequestUri(self) -> Uri:
        """

        :return:
        """
    @property
    def Timeout(self) -> int:
        """

        :return:
        """
    @Timeout.setter
    def Timeout(self, value: int) -> None: ...
    @property
    def UseDefaultCredentials(self) -> bool:
        """

        :return:
        """
    @UseDefaultCredentials.setter
    def UseDefaultCredentials(self, value: bool) -> None: ...
    def Abort(self) -> None:
        """"""
    def BeginGetRequestStream(self, callback: AsyncCallback, state: object) -> IAsyncResult:
        """

        :param callback:
        :param state:
        :return:
        """
    def BeginGetResponse(self, callback: AsyncCallback, state: object) -> IAsyncResult:
        """

        :param callback:
        :param state:
        :return:
        """
    @classmethod
    @overload
    def Create(cls, requestUriString: str) -> WebRequest:
        """

        :param requestUriString:
        :return:
        """
    @classmethod
    @overload
    def Create(cls, requestUri: Uri) -> WebRequest:
        """

        :param requestUri:
        :return:
        """
    @classmethod
    def CreateDefault(cls, requestUri: Uri) -> WebRequest:
        """

        :param requestUri:
        :return:
        """
    @classmethod
    @overload
    def CreateHttp(cls, requestUriString: str) -> HttpWebRequest:
        """

        :param requestUriString:
        :return:
        """
    @classmethod
    @overload
    def CreateHttp(cls, requestUri: Uri) -> HttpWebRequest:
        """

        :param requestUri:
        :return:
        """
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """

        :param requestedType:
        :return:
        """
    def EndGetRequestStream(self, asyncResult: IAsyncResult) -> Stream:
        """

        :param asyncResult:
        :return:
        """
    def EndGetResponse(self, asyncResult: IAsyncResult) -> WebResponse:
        """

        :param asyncResult:
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
    def GetLifetimeService(self) -> object:
        """

        :return:
        """
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    def GetRequestStream(self) -> Stream:
        """

        :return:
        """
    def GetRequestStreamAsync(self) -> Task[Stream]:
        """

        :return:
        """
    def GetResponse(self) -> WebResponse:
        """

        :return:
        """
    def GetResponseAsync(self) -> Task[WebResponse]:
        """

        :return:
        """
    @classmethod
    def GetSystemWebProxy(cls) -> IWebProxy:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def InitializeLifetimeService(self) -> object:
        """

        :return:
        """
    @classmethod
    def RegisterPortableWebRequestCreator(cls, creator: IWebRequestCreate) -> None:
        """

        :param creator:
        """
    @classmethod
    def RegisterPrefix(cls, prefix: str, creator: IWebRequestCreate) -> bool:
        """

        :param prefix:
        :param creator:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class WebRequestMethods(ABC, Object):
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

    class File(ABC, Object):
        """"""

        DownloadFile: Final[ClassVar[str]] = ...
        """"""
        UploadFile: Final[ClassVar[str]] = ...
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

    class Ftp(ABC, Object):
        """"""

        AppendFile: Final[ClassVar[str]] = ...
        """"""
        DeleteFile: Final[ClassVar[str]] = ...
        """"""
        DownloadFile: Final[ClassVar[str]] = ...
        """"""
        GetDateTimestamp: Final[ClassVar[str]] = ...
        """"""
        GetFileSize: Final[ClassVar[str]] = ...
        """"""
        ListDirectory: Final[ClassVar[str]] = ...
        """"""
        ListDirectoryDetails: Final[ClassVar[str]] = ...
        """"""
        MakeDirectory: Final[ClassVar[str]] = ...
        """"""
        PrintWorkingDirectory: Final[ClassVar[str]] = ...
        """"""
        RemoveDirectory: Final[ClassVar[str]] = ...
        """"""
        Rename: Final[ClassVar[str]] = ...
        """"""
        UploadFile: Final[ClassVar[str]] = ...
        """"""
        UploadFileWithUniqueName: Final[ClassVar[str]] = ...
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

    class Http(ABC, Object):
        """"""

        Connect: Final[ClassVar[str]] = ...
        """"""
        Get: Final[ClassVar[str]] = ...
        """"""
        Head: Final[ClassVar[str]] = ...
        """"""
        MkCol: Final[ClassVar[str]] = ...
        """"""
        Post: Final[ClassVar[str]] = ...
        """"""
        Put: Final[ClassVar[str]] = ...
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

class WebRequestPrefixElement(Object):
    """"""

    Prefix: Final[str] = ...
    """
    
    :return: 
    """
    @overload
    def __init__(self, P: str, C: IWebRequestCreate):
        """

        :param P:
        :param C:
        """
    @overload
    def __init__(self, P: str, creatorType: Type):
        """

        :param P:
        :param creatorType:
        """
    @property
    def Creator(self) -> IWebRequestCreate:
        """

        :return:
        """
    @Creator.setter
    def Creator(self, value: IWebRequestCreate) -> None: ...
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

class WebResponse(ABC, MarshalByRefObject, ISerializable, IDisposable):
    """"""

    @property
    def ContentLength(self) -> int:
        """

        :return:
        """
    @ContentLength.setter
    def ContentLength(self, value: int) -> None: ...
    @property
    def ContentType(self) -> str:
        """

        :return:
        """
    @ContentType.setter
    def ContentType(self, value: str) -> None: ...
    @property
    def Headers(self) -> WebHeaderCollection:
        """

        :return:
        """
    @property
    def IsFromCache(self) -> bool:
        """

        :return:
        """
    @property
    def IsMutuallyAuthenticated(self) -> bool:
        """

        :return:
        """
    @property
    def ResponseUri(self) -> Uri:
        """

        :return:
        """
    @property
    def SupportsHeaders(self) -> bool:
        """

        :return:
        """
    def Close(self) -> None:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """

        :param requestedType:
        :return:
        """
    def Dispose(self) -> None:
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
    def GetLifetimeService(self) -> object:
        """

        :return:
        """
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    def GetResponseStream(self) -> Stream:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def InitializeLifetimeService(self) -> object:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class WebSocketHttpRequestCreator(Object, IWebRequestCreate):
    """"""

    def __init__(self, usingHttps: bool):
        """

        :param usingHttps:
        """
    def Create(self, uri: Uri) -> WebRequest:
        """

        :param uri:
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

class WebUtility(ABC, Object):
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
    @classmethod
    @overload
    def HtmlDecode(cls, value: str) -> str:
        """

        :param value:
        :return:
        """
    @classmethod
    @overload
    def HtmlDecode(cls, value: str, output: TextWriter) -> None:
        """

        :param value:
        :param output:
        """
    @classmethod
    @overload
    def HtmlEncode(cls, value: str) -> str:
        """

        :param value:
        :return:
        """
    @classmethod
    @overload
    def HtmlEncode(cls, value: str, output: TextWriter) -> None:
        """

        :param value:
        :param output:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @classmethod
    def UrlDecode(cls, encodedValue: str) -> str:
        """

        :param encodedValue:
        :return:
        """
    @classmethod
    def UrlDecodeToBytes(cls, encodedValue: Array[int], offset: int, count: int) -> Array[int]:
        """

        :param encodedValue:
        :param offset:
        :param count:
        :return:
        """
    @classmethod
    def UrlEncode(cls, value: str) -> str:
        """

        :param value:
        :return:
        """
    @classmethod
    def UrlEncodeToBytes(cls, value: Array[int], offset: int, count: int) -> Array[int]:
        """

        :param value:
        :param offset:
        :param count:
        :return:
        """

class Win32(ABC, Object):
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

class WinHttpWebProxyBuilder(WebProxyDataBuilder):
    """"""

    def __init__(self):
        """"""
    def Build(self) -> WebProxyData:
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

class WinHttpWebProxyFinder(BaseWebProxyFinder, IWebProxyFinder, IDisposable):
    """"""

    def __init__(self, engine: AutoWebProxyScriptEngine):
        """

        :param engine:
        """
    @property
    def IsUnrecognizedScheme(self) -> bool:
        """

        :return:
        """
    @property
    def IsValid(self) -> bool:
        """

        :return:
        """
    def Abort(self) -> None:
        """"""
    def Dispose(self) -> None:
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
    def GetProxies(self, destination: Uri, proxyList: IList[str]) -> Tuple[bool, IList[str]]:
        """

        :param destination:
        :param proxyList:
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

    Buffer: Final[Array[int]] = ...
    """
    
    :return: 
    """
    End: Final[int] = ...
    """
    
    :return: 
    """
    HandshakeDone: Final[bool] = ...
    """
    
    :return: 
    """
    HeaderDone: Final[bool] = ...
    """
    
    :return: 
    """
    IsWrite: Final[bool] = ...
    """
    
    :return: 
    """
    Offset: Final[int] = ...
    """
    
    :return: 
    """
    ParentResult: Final[WorkerAsyncResult] = ...
    """
    
    :return: 
    """
    def __init__(
        self,
        asyncObject: object,
        asyncState: object,
        savedAsyncCallback: AsyncCallback,
        buffer: Array[int],
        offset: int,
        end: int,
    ):
        """

        :param asyncObject:
        :param asyncState:
        :param savedAsyncCallback:
        :param buffer:
        :param offset:
        :param end:
        """
    @property
    def AsyncState(self) -> object:
        """

        :return:
        """
    @property
    def AsyncWaitHandle(self) -> WaitHandle:
        """

        :return:
        """
    @property
    def CompletedSynchronously(self) -> bool:
        """

        :return:
        """
    @property
    def IsCompleted(self) -> bool:
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

class WriteStreamClosedEventArgs(EventArgs):
    """"""

    def __init__(self):
        """"""
    @property
    def Error(self) -> Exception:
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

WriteStreamClosedEventHandler: Callable[[object, WriteStreamClosedEventArgs], None] = ...
"""

:param sender: 
:param e: 
"""

class _CERT_CHAIN_ELEMENT(ValueType):
    """"""

    cbSize: Final[int] = ...
    """
    
    :return: 
    """
    pCertContext: Final[IntPtr] = ...
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

class hostent(ValueType):
    """"""

    h_addr_list: Final[IntPtr] = ...
    """
    
    :return: 
    """
    h_addrtype: Final[int] = ...
    """
    
    :return: 
    """
    h_aliases: Final[IntPtr] = ...
    """
    
    :return: 
    """
    h_length: Final[int] = ...
    """
    
    :return: 
    """
    h_name: Final[IntPtr] = ...
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
