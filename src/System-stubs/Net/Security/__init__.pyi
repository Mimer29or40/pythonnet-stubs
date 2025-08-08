"""Automatically generated stubs for C# namespace: System.Net.Security."""

from abc import ABC
from collections.abc import Callable
from typing import overload

from System import Array
from System import AsyncCallback
from System import Enum
from System import IAsyncResult
from System import IDisposable
from System import Object
from System import Type
from System.IO import SeekOrigin
from System.IO import Stream
from System.Net import NetworkCredential
from System.Net import TransportContext
from System.Runtime.Remoting import ObjRef
from System.Security.Authentication import CipherAlgorithmType
from System.Security.Authentication import ExchangeAlgorithmType
from System.Security.Authentication import HashAlgorithmType
from System.Security.Authentication import SslProtocols
from System.Security.Authentication.ExtendedProtection import ChannelBinding
from System.Security.Authentication.ExtendedProtection import ExtendedProtectionPolicy
from System.Security.Cryptography.X509Certificates import X509Certificate
from System.Security.Cryptography.X509Certificates import X509CertificateCollection
from System.Security.Cryptography.X509Certificates import X509Chain
from System.Security.Principal import IIdentity
from System.Security.Principal import TokenImpersonationLevel
from System.Threading import CancellationToken
from System.Threading.Tasks import Task

class AuthenticatedStream(ABC, Stream, IDisposable):
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
    def IsAuthenticated(self) -> bool:
        """"""
    @property
    def IsEncrypted(self) -> bool:
        """"""
    @property
    def IsMutuallyAuthenticated(self) -> bool:
        """"""
    @property
    def IsServer(self) -> bool:
        """"""
    @property
    def IsSigned(self) -> bool:
        """"""
    @property
    def LeaveInnerStreamOpen(self) -> bool:
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

class AuthenticationLevel(Enum):
    """"""

    _None: AuthenticationLevel = ...
    """"""
    MutualAuthRequested: AuthenticationLevel = ...
    """"""
    MutualAuthRequired: AuthenticationLevel = ...
    """"""

class EncryptionPolicy(Enum):
    """"""

    RequireEncryption: EncryptionPolicy = ...
    """"""
    AllowNoEncryption: EncryptionPolicy = ...
    """"""
    NoEncryption: EncryptionPolicy = ...
    """"""

type LocalCertSelectionCallback = Callable[
    [str, X509CertificateCollection, X509Certificate, Array[str]], X509Certificate
]
""""""
type LocalCertificateSelectionCallback = Callable[
    [object, str, X509CertificateCollection, X509Certificate, Array[str]], X509Certificate
]
""""""

class NegoState(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class NegotiateStream(AuthenticatedStream, IDisposable):
    """"""
    @overload
    def __init__(self, innerStream: Stream) -> None:
        """"""
    @overload
    def __init__(self, innerStream: Stream, leaveInnerStreamOpen: bool) -> None:
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
    def ImpersonationLevel(self) -> TokenImpersonationLevel:
        """"""
    @property
    def IsAuthenticated(self) -> bool:
        """"""
    @property
    def IsEncrypted(self) -> bool:
        """"""
    @property
    def IsMutuallyAuthenticated(self) -> bool:
        """"""
    @property
    def IsServer(self) -> bool:
        """"""
    @property
    def IsSigned(self) -> bool:
        """"""
    @property
    def LeaveInnerStreamOpen(self) -> bool:
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
    def RemoteIdentity(self) -> IIdentity:
        """"""
    @property
    def WriteTimeout(self) -> int:
        """"""
    @WriteTimeout.setter
    def WriteTimeout(self, value: int) -> None: ...
    @overload
    def AuthenticateAsClient(self) -> None:
        """"""
    @overload
    def AuthenticateAsClient(
        self, credential: NetworkCredential, binding: ChannelBinding, targetName: str
    ) -> None:
        """"""
    @overload
    def AuthenticateAsClient(
        self,
        credential: NetworkCredential,
        binding: ChannelBinding,
        targetName: str,
        requiredProtectionLevel: ProtectionLevel,
        allowedImpersonationLevel: TokenImpersonationLevel,
    ) -> None:
        """"""
    @overload
    def AuthenticateAsClient(self, credential: NetworkCredential, targetName: str) -> None:
        """"""
    @overload
    def AuthenticateAsClient(
        self,
        credential: NetworkCredential,
        targetName: str,
        requiredProtectionLevel: ProtectionLevel,
        allowedImpersonationLevel: TokenImpersonationLevel,
    ) -> None:
        """"""
    @overload
    def AuthenticateAsClientAsync(self) -> Task:
        """"""
    @overload
    def AuthenticateAsClientAsync(
        self, credential: NetworkCredential, binding: ChannelBinding, targetName: str
    ) -> Task:
        """"""
    @overload
    def AuthenticateAsClientAsync(
        self,
        credential: NetworkCredential,
        binding: ChannelBinding,
        targetName: str,
        requiredProtectionLevel: ProtectionLevel,
        allowedImpersonationLevel: TokenImpersonationLevel,
    ) -> Task:
        """"""
    @overload
    def AuthenticateAsClientAsync(self, credential: NetworkCredential, targetName: str) -> Task:
        """"""
    @overload
    def AuthenticateAsClientAsync(
        self,
        credential: NetworkCredential,
        targetName: str,
        requiredProtectionLevel: ProtectionLevel,
        allowedImpersonationLevel: TokenImpersonationLevel,
    ) -> Task:
        """"""
    @overload
    def AuthenticateAsServer(self) -> None:
        """"""
    @overload
    def AuthenticateAsServer(
        self,
        credential: NetworkCredential,
        requiredProtectionLevel: ProtectionLevel,
        requiredImpersonationLevel: TokenImpersonationLevel,
    ) -> None:
        """"""
    @overload
    def AuthenticateAsServer(
        self,
        credential: NetworkCredential,
        policy: ExtendedProtectionPolicy,
        requiredProtectionLevel: ProtectionLevel,
        requiredImpersonationLevel: TokenImpersonationLevel,
    ) -> None:
        """"""
    @overload
    def AuthenticateAsServer(self, policy: ExtendedProtectionPolicy) -> None:
        """"""
    @overload
    def AuthenticateAsServerAsync(self) -> Task:
        """"""
    @overload
    def AuthenticateAsServerAsync(
        self,
        credential: NetworkCredential,
        requiredProtectionLevel: ProtectionLevel,
        requiredImpersonationLevel: TokenImpersonationLevel,
    ) -> Task:
        """"""
    @overload
    def AuthenticateAsServerAsync(
        self,
        credential: NetworkCredential,
        policy: ExtendedProtectionPolicy,
        requiredProtectionLevel: ProtectionLevel,
        requiredImpersonationLevel: TokenImpersonationLevel,
    ) -> Task:
        """"""
    @overload
    def AuthenticateAsServerAsync(self, policy: ExtendedProtectionPolicy) -> Task:
        """"""
    @overload
    def BeginAuthenticateAsClient(
        self,
        credential: NetworkCredential,
        binding: ChannelBinding,
        targetName: str,
        requiredProtectionLevel: ProtectionLevel,
        allowedImpersonationLevel: TokenImpersonationLevel,
        asyncCallback: AsyncCallback,
        asyncState: object,
    ) -> IAsyncResult:
        """"""
    @overload
    def BeginAuthenticateAsClient(
        self,
        credential: NetworkCredential,
        binding: ChannelBinding,
        targetName: str,
        asyncCallback: AsyncCallback,
        asyncState: object,
    ) -> IAsyncResult:
        """"""
    @overload
    def BeginAuthenticateAsClient(
        self,
        credential: NetworkCredential,
        targetName: str,
        requiredProtectionLevel: ProtectionLevel,
        allowedImpersonationLevel: TokenImpersonationLevel,
        asyncCallback: AsyncCallback,
        asyncState: object,
    ) -> IAsyncResult:
        """"""
    @overload
    def BeginAuthenticateAsClient(
        self,
        credential: NetworkCredential,
        targetName: str,
        asyncCallback: AsyncCallback,
        asyncState: object,
    ) -> IAsyncResult:
        """"""
    @overload
    def BeginAuthenticateAsClient(
        self, asyncCallback: AsyncCallback, asyncState: object
    ) -> IAsyncResult:
        """"""
    @overload
    def BeginAuthenticateAsServer(
        self,
        credential: NetworkCredential,
        requiredProtectionLevel: ProtectionLevel,
        requiredImpersonationLevel: TokenImpersonationLevel,
        asyncCallback: AsyncCallback,
        asyncState: object,
    ) -> IAsyncResult:
        """"""
    @overload
    def BeginAuthenticateAsServer(
        self,
        credential: NetworkCredential,
        policy: ExtendedProtectionPolicy,
        requiredProtectionLevel: ProtectionLevel,
        requiredImpersonationLevel: TokenImpersonationLevel,
        asyncCallback: AsyncCallback,
        asyncState: object,
    ) -> IAsyncResult:
        """"""
    @overload
    def BeginAuthenticateAsServer(
        self, policy: ExtendedProtectionPolicy, asyncCallback: AsyncCallback, asyncState: object
    ) -> IAsyncResult:
        """"""
    @overload
    def BeginAuthenticateAsServer(
        self, asyncCallback: AsyncCallback, asyncState: object
    ) -> IAsyncResult:
        """"""
    def BeginRead(
        self,
        buffer: Array[int],
        offset: int,
        count: int,
        asyncCallback: AsyncCallback,
        asyncState: object,
    ) -> IAsyncResult:
        """"""
    def BeginWrite(
        self,
        buffer: Array[int],
        offset: int,
        count: int,
        asyncCallback: AsyncCallback,
        asyncState: object,
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
    def EndAuthenticateAsClient(self, asyncResult: IAsyncResult) -> None:
        """"""
    def EndAuthenticateAsServer(self, asyncResult: IAsyncResult) -> None:
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

class ProtectionLevel(Enum):
    """"""

    _None: ProtectionLevel = ...
    """"""
    Sign: ProtectionLevel = ...
    """"""
    EncryptAndSign: ProtectionLevel = ...
    """"""

class ProtocolToken(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

type RemoteCertValidationCallback = Callable[
    [str, X509Certificate, X509Chain, SslPolicyErrors], bool
]
""""""
type RemoteCertificateValidationCallback = Callable[
    [object, X509Certificate, X509Chain, SslPolicyErrors], bool
]
""""""

class SSPIHandleCache(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SecureChannel(Object):
    """"""
    def CreateFatalHandshakeAlertToken(
        self, sslPolicyErrors: SslPolicyErrors, chain: X509Chain
    ) -> ProtocolToken:
        """"""
    def CreateShutdownToken(self) -> ProtocolToken:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SslPolicyErrors(Enum):
    """"""

    _None: SslPolicyErrors = ...
    """"""
    RemoteCertificateNotAvailable: SslPolicyErrors = ...
    """"""
    RemoteCertificateNameMismatch: SslPolicyErrors = ...
    """"""
    RemoteCertificateChainErrors: SslPolicyErrors = ...
    """"""

class SslSessionsCache(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SslState(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SslStream(AuthenticatedStream, IDisposable):
    """"""
    @overload
    def __init__(self, innerStream: Stream) -> None:
        """"""
    @overload
    def __init__(self, innerStream: Stream, leaveInnerStreamOpen: bool) -> None:
        """"""
    @overload
    def __init__(
        self,
        innerStream: Stream,
        leaveInnerStreamOpen: bool,
        userCertificateValidationCallback: RemoteCertificateValidationCallback,
    ) -> None:
        """"""
    @overload
    def __init__(
        self,
        innerStream: Stream,
        leaveInnerStreamOpen: bool,
        userCertificateValidationCallback: RemoteCertificateValidationCallback,
        userCertificateSelectionCallback: LocalCertificateSelectionCallback,
    ) -> None:
        """"""
    @overload
    def __init__(
        self,
        innerStream: Stream,
        leaveInnerStreamOpen: bool,
        userCertificateValidationCallback: RemoteCertificateValidationCallback,
        userCertificateSelectionCallback: LocalCertificateSelectionCallback,
        encryptionPolicy: EncryptionPolicy,
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
    def CheckCertRevocationStatus(self) -> bool:
        """"""
    @property
    def CipherAlgorithm(self) -> CipherAlgorithmType:
        """"""
    @property
    def CipherStrength(self) -> int:
        """"""
    @property
    def HashAlgorithm(self) -> HashAlgorithmType:
        """"""
    @property
    def HashStrength(self) -> int:
        """"""
    @property
    def IsAuthenticated(self) -> bool:
        """"""
    @property
    def IsEncrypted(self) -> bool:
        """"""
    @property
    def IsMutuallyAuthenticated(self) -> bool:
        """"""
    @property
    def IsServer(self) -> bool:
        """"""
    @property
    def IsSigned(self) -> bool:
        """"""
    @property
    def KeyExchangeAlgorithm(self) -> ExchangeAlgorithmType:
        """"""
    @property
    def KeyExchangeStrength(self) -> int:
        """"""
    @property
    def LeaveInnerStreamOpen(self) -> bool:
        """"""
    @property
    def Length(self) -> int:
        """"""
    @property
    def LocalCertificate(self) -> X509Certificate:
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
    def RemoteCertificate(self) -> X509Certificate:
        """"""
    @property
    def SslProtocol(self) -> SslProtocols:
        """"""
    @property
    def TransportContext(self) -> TransportContext:
        """"""
    @property
    def WriteTimeout(self) -> int:
        """"""
    @WriteTimeout.setter
    def WriteTimeout(self, value: int) -> None: ...
    @overload
    def AuthenticateAsClient(self, targetHost: str) -> None:
        """"""
    @overload
    def AuthenticateAsClient(
        self,
        targetHost: str,
        clientCertificates: X509CertificateCollection,
        enabledSslProtocols: SslProtocols,
        checkCertificateRevocation: bool,
    ) -> None:
        """"""
    @overload
    def AuthenticateAsClient(
        self,
        targetHost: str,
        clientCertificates: X509CertificateCollection,
        checkCertificateRevocation: bool,
    ) -> None:
        """"""
    @overload
    def AuthenticateAsClientAsync(self, targetHost: str) -> Task:
        """"""
    @overload
    def AuthenticateAsClientAsync(
        self,
        targetHost: str,
        clientCertificates: X509CertificateCollection,
        enabledSslProtocols: SslProtocols,
        checkCertificateRevocation: bool,
    ) -> Task:
        """"""
    @overload
    def AuthenticateAsClientAsync(
        self,
        targetHost: str,
        clientCertificates: X509CertificateCollection,
        checkCertificateRevocation: bool,
    ) -> Task:
        """"""
    @overload
    def AuthenticateAsServer(self, serverCertificate: X509Certificate) -> None:
        """"""
    @overload
    def AuthenticateAsServer(
        self,
        serverCertificate: X509Certificate,
        clientCertificateRequired: bool,
        enabledSslProtocols: SslProtocols,
        checkCertificateRevocation: bool,
    ) -> None:
        """"""
    @overload
    def AuthenticateAsServer(
        self,
        serverCertificate: X509Certificate,
        clientCertificateRequired: bool,
        checkCertificateRevocation: bool,
    ) -> None:
        """"""
    @overload
    def AuthenticateAsServerAsync(self, serverCertificate: X509Certificate) -> Task:
        """"""
    @overload
    def AuthenticateAsServerAsync(
        self,
        serverCertificate: X509Certificate,
        clientCertificateRequired: bool,
        enabledSslProtocols: SslProtocols,
        checkCertificateRevocation: bool,
    ) -> Task:
        """"""
    @overload
    def AuthenticateAsServerAsync(
        self,
        serverCertificate: X509Certificate,
        clientCertificateRequired: bool,
        checkCertificateRevocation: bool,
    ) -> Task:
        """"""
    @overload
    def BeginAuthenticateAsClient(
        self,
        targetHost: str,
        clientCertificates: X509CertificateCollection,
        enabledSslProtocols: SslProtocols,
        checkCertificateRevocation: bool,
        asyncCallback: AsyncCallback,
        asyncState: object,
    ) -> IAsyncResult:
        """"""
    @overload
    def BeginAuthenticateAsClient(
        self,
        targetHost: str,
        clientCertificates: X509CertificateCollection,
        checkCertificateRevocation: bool,
        asyncCallback: AsyncCallback,
        asyncState: object,
    ) -> IAsyncResult:
        """"""
    @overload
    def BeginAuthenticateAsClient(
        self, targetHost: str, asyncCallback: AsyncCallback, asyncState: object
    ) -> IAsyncResult:
        """"""
    @overload
    def BeginAuthenticateAsServer(
        self, serverCertificate: X509Certificate, asyncCallback: AsyncCallback, asyncState: object
    ) -> IAsyncResult:
        """"""
    @overload
    def BeginAuthenticateAsServer(
        self,
        serverCertificate: X509Certificate,
        clientCertificateRequired: bool,
        enabledSslProtocols: SslProtocols,
        checkCertificateRevocation: bool,
        asyncCallback: AsyncCallback,
        asyncState: object,
    ) -> IAsyncResult:
        """"""
    @overload
    def BeginAuthenticateAsServer(
        self,
        serverCertificate: X509Certificate,
        clientCertificateRequired: bool,
        checkCertificateRevocation: bool,
        asyncCallback: AsyncCallback,
        asyncState: object,
    ) -> IAsyncResult:
        """"""
    def BeginRead(
        self,
        buffer: Array[int],
        offset: int,
        count: int,
        asyncCallback: AsyncCallback,
        asyncState: object,
    ) -> IAsyncResult:
        """"""
    def BeginWrite(
        self,
        buffer: Array[int],
        offset: int,
        count: int,
        asyncCallback: AsyncCallback,
        asyncState: object,
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
    def EndAuthenticateAsClient(self, asyncResult: IAsyncResult) -> None:
        """"""
    def EndAuthenticateAsServer(self, asyncResult: IAsyncResult) -> None:
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
    def ShutdownAsync(self) -> Task:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def Write(self, buffer: Array[int]) -> None:
        """"""
    @overload
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

class TlsAlertMessage(Enum):
    """"""

    CloseNotify: TlsAlertMessage = ...
    """"""
    UnexpectedMessage: TlsAlertMessage = ...
    """"""
    BadRecordMac: TlsAlertMessage = ...
    """"""
    DecryptionFailed: TlsAlertMessage = ...
    """"""
    RecordOverflow: TlsAlertMessage = ...
    """"""
    DecompressionFail: TlsAlertMessage = ...
    """"""
    HandshakeFailure: TlsAlertMessage = ...
    """"""
    BadCertificate: TlsAlertMessage = ...
    """"""
    UnsupportedCert: TlsAlertMessage = ...
    """"""
    CertificateRevoked: TlsAlertMessage = ...
    """"""
    CertificateExpired: TlsAlertMessage = ...
    """"""
    CertificateUnknown: TlsAlertMessage = ...
    """"""
    IllegalParameter: TlsAlertMessage = ...
    """"""
    UnknownCA: TlsAlertMessage = ...
    """"""
    AccessDenied: TlsAlertMessage = ...
    """"""
    DecodeError: TlsAlertMessage = ...
    """"""
    DecryptError: TlsAlertMessage = ...
    """"""
    ExportRestriction: TlsAlertMessage = ...
    """"""
    ProtocolVersion: TlsAlertMessage = ...
    """"""
    InsuffientSecurity: TlsAlertMessage = ...
    """"""
    InternalError: TlsAlertMessage = ...
    """"""
    UserCanceled: TlsAlertMessage = ...
    """"""
    NoRenegotiation: TlsAlertMessage = ...
    """"""
    UnsupportedExt: TlsAlertMessage = ...
    """"""

class TlsAlertType(Enum):
    """"""

    Warning: TlsAlertType = ...
    """"""
    Fatal: TlsAlertType = ...
    """"""

class _SslStream(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
