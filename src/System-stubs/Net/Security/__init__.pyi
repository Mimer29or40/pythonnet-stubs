from __future__ import annotations

from abc import ABC
from typing import Callable
from typing import Tuple
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
    def IsAuthenticated(self) -> bool:
        """

        :return:
        """
    @property
    def IsEncrypted(self) -> bool:
        """

        :return:
        """
    @property
    def IsMutuallyAuthenticated(self) -> bool:
        """

        :return:
        """
    @property
    def IsServer(self) -> bool:
        """

        :return:
        """
    @property
    def IsSigned(self) -> bool:
        """

        :return:
        """
    @property
    def LeaveInnerStreamOpen(self) -> bool:
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

LocalCertSelectionCallback: Callable[
    [str, X509CertificateCollection, X509Certificate, Array[str]], X509Certificate
] = ...
"""

:param targetHost: 
:param localCertificates: 
:param remoteCertificate: 
:param acceptableIssuers: 
:return: 
"""
LocalCertificateSelectionCallback: Callable[
    [object, str, X509CertificateCollection, X509Certificate, Array[str]], X509Certificate
] = ...
"""

:param sender: 
:param targetHost: 
:param localCertificates: 
:param remoteCertificate: 
:param acceptableIssuers: 
:return: 
"""

class NegoState(Object):
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

class NegotiateStream(AuthenticatedStream, IDisposable):
    """"""

    @overload
    def __init__(self, innerStream: Stream):
        """

        :param innerStream:
        """
    @overload
    def __init__(self, innerStream: Stream, leaveInnerStreamOpen: bool):
        """

        :param innerStream:
        :param leaveInnerStreamOpen:
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
    def ImpersonationLevel(self) -> TokenImpersonationLevel:
        """

        :return:
        """
    @property
    def IsAuthenticated(self) -> bool:
        """

        :return:
        """
    @property
    def IsEncrypted(self) -> bool:
        """

        :return:
        """
    @property
    def IsMutuallyAuthenticated(self) -> bool:
        """

        :return:
        """
    @property
    def IsServer(self) -> bool:
        """

        :return:
        """
    @property
    def IsSigned(self) -> bool:
        """

        :return:
        """
    @property
    def LeaveInnerStreamOpen(self) -> bool:
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
    def RemoteIdentity(self) -> IIdentity:
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
    @overload
    def AuthenticateAsClient(self) -> None:
        """"""
    @overload
    def AuthenticateAsClient(self, credential: NetworkCredential, targetName: str) -> None:
        """

        :param credential:
        :param targetName:
        """
    @overload
    def AuthenticateAsClient(
        self, credential: NetworkCredential, binding: ChannelBinding, targetName: str
    ) -> None:
        """

        :param credential:
        :param binding:
        :param targetName:
        """
    @overload
    def AuthenticateAsClient(
        self,
        credential: NetworkCredential,
        targetName: str,
        requiredProtectionLevel: ProtectionLevel,
        allowedImpersonationLevel: TokenImpersonationLevel,
    ) -> None:
        """

        :param credential:
        :param targetName:
        :param requiredProtectionLevel:
        :param allowedImpersonationLevel:
        """
    @overload
    def AuthenticateAsClient(
        self,
        credential: NetworkCredential,
        binding: ChannelBinding,
        targetName: str,
        requiredProtectionLevel: ProtectionLevel,
        allowedImpersonationLevel: TokenImpersonationLevel,
    ) -> None:
        """

        :param credential:
        :param binding:
        :param targetName:
        :param requiredProtectionLevel:
        :param allowedImpersonationLevel:
        """
    @overload
    def AuthenticateAsClientAsync(self) -> Task:
        """

        :return:
        """
    @overload
    def AuthenticateAsClientAsync(self, credential: NetworkCredential, targetName: str) -> Task:
        """

        :param credential:
        :param targetName:
        :return:
        """
    @overload
    def AuthenticateAsClientAsync(
        self, credential: NetworkCredential, binding: ChannelBinding, targetName: str
    ) -> Task:
        """

        :param credential:
        :param binding:
        :param targetName:
        :return:
        """
    @overload
    def AuthenticateAsClientAsync(
        self,
        credential: NetworkCredential,
        targetName: str,
        requiredProtectionLevel: ProtectionLevel,
        allowedImpersonationLevel: TokenImpersonationLevel,
    ) -> Task:
        """

        :param credential:
        :param targetName:
        :param requiredProtectionLevel:
        :param allowedImpersonationLevel:
        :return:
        """
    @overload
    def AuthenticateAsClientAsync(
        self,
        credential: NetworkCredential,
        binding: ChannelBinding,
        targetName: str,
        requiredProtectionLevel: ProtectionLevel,
        allowedImpersonationLevel: TokenImpersonationLevel,
    ) -> Task:
        """

        :param credential:
        :param binding:
        :param targetName:
        :param requiredProtectionLevel:
        :param allowedImpersonationLevel:
        :return:
        """
    @overload
    def AuthenticateAsServer(self) -> None:
        """"""
    @overload
    def AuthenticateAsServer(self, policy: ExtendedProtectionPolicy) -> None:
        """

        :param policy:
        """
    @overload
    def AuthenticateAsServer(
        self,
        credential: NetworkCredential,
        requiredProtectionLevel: ProtectionLevel,
        requiredImpersonationLevel: TokenImpersonationLevel,
    ) -> None:
        """

        :param credential:
        :param requiredProtectionLevel:
        :param requiredImpersonationLevel:
        """
    @overload
    def AuthenticateAsServer(
        self,
        credential: NetworkCredential,
        policy: ExtendedProtectionPolicy,
        requiredProtectionLevel: ProtectionLevel,
        requiredImpersonationLevel: TokenImpersonationLevel,
    ) -> None:
        """

        :param credential:
        :param policy:
        :param requiredProtectionLevel:
        :param requiredImpersonationLevel:
        """
    @overload
    def AuthenticateAsServerAsync(self) -> Task:
        """

        :return:
        """
    @overload
    def AuthenticateAsServerAsync(self, policy: ExtendedProtectionPolicy) -> Task:
        """

        :param policy:
        :return:
        """
    @overload
    def AuthenticateAsServerAsync(
        self,
        credential: NetworkCredential,
        requiredProtectionLevel: ProtectionLevel,
        requiredImpersonationLevel: TokenImpersonationLevel,
    ) -> Task:
        """

        :param credential:
        :param requiredProtectionLevel:
        :param requiredImpersonationLevel:
        :return:
        """
    @overload
    def AuthenticateAsServerAsync(
        self,
        credential: NetworkCredential,
        policy: ExtendedProtectionPolicy,
        requiredProtectionLevel: ProtectionLevel,
        requiredImpersonationLevel: TokenImpersonationLevel,
    ) -> Task:
        """

        :param credential:
        :param policy:
        :param requiredProtectionLevel:
        :param requiredImpersonationLevel:
        :return:
        """
    @overload
    def BeginAuthenticateAsClient(
        self, asyncCallback: AsyncCallback, asyncState: object
    ) -> IAsyncResult:
        """

        :param asyncCallback:
        :param asyncState:
        :return:
        """
    @overload
    def BeginAuthenticateAsClient(
        self,
        credential: NetworkCredential,
        targetName: str,
        asyncCallback: AsyncCallback,
        asyncState: object,
    ) -> IAsyncResult:
        """

        :param credential:
        :param targetName:
        :param asyncCallback:
        :param asyncState:
        :return:
        """
    @overload
    def BeginAuthenticateAsClient(
        self,
        credential: NetworkCredential,
        binding: ChannelBinding,
        targetName: str,
        asyncCallback: AsyncCallback,
        asyncState: object,
    ) -> IAsyncResult:
        """

        :param credential:
        :param binding:
        :param targetName:
        :param asyncCallback:
        :param asyncState:
        :return:
        """
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
        """

        :param credential:
        :param targetName:
        :param requiredProtectionLevel:
        :param allowedImpersonationLevel:
        :param asyncCallback:
        :param asyncState:
        :return:
        """
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
        """

        :param credential:
        :param binding:
        :param targetName:
        :param requiredProtectionLevel:
        :param allowedImpersonationLevel:
        :param asyncCallback:
        :param asyncState:
        :return:
        """
    @overload
    def BeginAuthenticateAsServer(
        self, asyncCallback: AsyncCallback, asyncState: object
    ) -> IAsyncResult:
        """

        :param asyncCallback:
        :param asyncState:
        :return:
        """
    @overload
    def BeginAuthenticateAsServer(
        self, policy: ExtendedProtectionPolicy, asyncCallback: AsyncCallback, asyncState: object
    ) -> IAsyncResult:
        """

        :param policy:
        :param asyncCallback:
        :param asyncState:
        :return:
        """
    @overload
    def BeginAuthenticateAsServer(
        self,
        credential: NetworkCredential,
        requiredProtectionLevel: ProtectionLevel,
        requiredImpersonationLevel: TokenImpersonationLevel,
        asyncCallback: AsyncCallback,
        asyncState: object,
    ) -> IAsyncResult:
        """

        :param credential:
        :param requiredProtectionLevel:
        :param requiredImpersonationLevel:
        :param asyncCallback:
        :param asyncState:
        :return:
        """
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
        """

        :param credential:
        :param policy:
        :param requiredProtectionLevel:
        :param requiredImpersonationLevel:
        :param asyncCallback:
        :param asyncState:
        :return:
        """
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
    def EndAuthenticateAsClient(self, asyncResult: IAsyncResult) -> None:
        """

        :param asyncResult:
        """
    def EndAuthenticateAsServer(self, asyncResult: IAsyncResult) -> None:
        """

        :param asyncResult:
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

RemoteCertValidationCallback: Callable[
    [str, X509Certificate, X509Chain, SslPolicyErrors], bool
] = ...
"""

:param host: 
:param certificate: 
:param chain: 
:param sslPolicyErrors: 
:return: 
"""
RemoteCertificateValidationCallback: Callable[
    [object, X509Certificate, X509Chain, SslPolicyErrors], bool
] = ...
"""

:param sender: 
:param certificate: 
:param chain: 
:param sslPolicyErrors: 
:return: 
"""

class SSPIHandleCache(ABC, Object):
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

class SecureChannel(Object):
    """"""

    def CreateFatalHandshakeAlertToken(
        self, sslPolicyErrors: SslPolicyErrors, chain: X509Chain
    ) -> ProtocolToken:
        """

        :param sslPolicyErrors:
        :param chain:
        :return:
        """
    def CreateShutdownToken(self) -> ProtocolToken:
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

class SslState(Object):
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

class SslStream(AuthenticatedStream, IDisposable):
    """"""

    @overload
    def __init__(self, innerStream: Stream):
        """

        :param innerStream:
        """
    @overload
    def __init__(self, innerStream: Stream, leaveInnerStreamOpen: bool):
        """

        :param innerStream:
        :param leaveInnerStreamOpen:
        """
    @overload
    def __init__(
        self,
        innerStream: Stream,
        leaveInnerStreamOpen: bool,
        userCertificateValidationCallback: RemoteCertificateValidationCallback,
    ):
        """

        :param innerStream:
        :param leaveInnerStreamOpen:
        :param userCertificateValidationCallback:
        """
    @overload
    def __init__(
        self,
        innerStream: Stream,
        leaveInnerStreamOpen: bool,
        userCertificateValidationCallback: RemoteCertificateValidationCallback,
        userCertificateSelectionCallback: LocalCertificateSelectionCallback,
    ):
        """

        :param innerStream:
        :param leaveInnerStreamOpen:
        :param userCertificateValidationCallback:
        :param userCertificateSelectionCallback:
        """
    @overload
    def __init__(
        self,
        innerStream: Stream,
        leaveInnerStreamOpen: bool,
        userCertificateValidationCallback: RemoteCertificateValidationCallback,
        userCertificateSelectionCallback: LocalCertificateSelectionCallback,
        encryptionPolicy: EncryptionPolicy,
    ):
        """

        :param innerStream:
        :param leaveInnerStreamOpen:
        :param userCertificateValidationCallback:
        :param userCertificateSelectionCallback:
        :param encryptionPolicy:
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
    def CheckCertRevocationStatus(self) -> bool:
        """

        :return:
        """
    @property
    def CipherAlgorithm(self) -> CipherAlgorithmType:
        """

        :return:
        """
    @property
    def CipherStrength(self) -> int:
        """

        :return:
        """
    @property
    def HashAlgorithm(self) -> HashAlgorithmType:
        """

        :return:
        """
    @property
    def HashStrength(self) -> int:
        """

        :return:
        """
    @property
    def IsAuthenticated(self) -> bool:
        """

        :return:
        """
    @property
    def IsEncrypted(self) -> bool:
        """

        :return:
        """
    @property
    def IsMutuallyAuthenticated(self) -> bool:
        """

        :return:
        """
    @property
    def IsServer(self) -> bool:
        """

        :return:
        """
    @property
    def IsSigned(self) -> bool:
        """

        :return:
        """
    @property
    def KeyExchangeAlgorithm(self) -> ExchangeAlgorithmType:
        """

        :return:
        """
    @property
    def KeyExchangeStrength(self) -> int:
        """

        :return:
        """
    @property
    def LeaveInnerStreamOpen(self) -> bool:
        """

        :return:
        """
    @property
    def Length(self) -> int:
        """

        :return:
        """
    @property
    def LocalCertificate(self) -> X509Certificate:
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
    def RemoteCertificate(self) -> X509Certificate:
        """

        :return:
        """
    @property
    def SslProtocol(self) -> SslProtocols:
        """

        :return:
        """
    @property
    def TransportContext(self) -> TransportContext:
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
    @overload
    def AuthenticateAsClient(self, targetHost: str) -> None:
        """

        :param targetHost:
        """
    @overload
    def AuthenticateAsClient(
        self,
        targetHost: str,
        clientCertificates: X509CertificateCollection,
        checkCertificateRevocation: bool,
    ) -> None:
        """

        :param targetHost:
        :param clientCertificates:
        :param checkCertificateRevocation:
        """
    @overload
    def AuthenticateAsClient(
        self,
        targetHost: str,
        clientCertificates: X509CertificateCollection,
        enabledSslProtocols: SslProtocols,
        checkCertificateRevocation: bool,
    ) -> None:
        """

        :param targetHost:
        :param clientCertificates:
        :param enabledSslProtocols:
        :param checkCertificateRevocation:
        """
    @overload
    def AuthenticateAsClientAsync(self, targetHost: str) -> Task:
        """

        :param targetHost:
        :return:
        """
    @overload
    def AuthenticateAsClientAsync(
        self,
        targetHost: str,
        clientCertificates: X509CertificateCollection,
        checkCertificateRevocation: bool,
    ) -> Task:
        """

        :param targetHost:
        :param clientCertificates:
        :param checkCertificateRevocation:
        :return:
        """
    @overload
    def AuthenticateAsClientAsync(
        self,
        targetHost: str,
        clientCertificates: X509CertificateCollection,
        enabledSslProtocols: SslProtocols,
        checkCertificateRevocation: bool,
    ) -> Task:
        """

        :param targetHost:
        :param clientCertificates:
        :param enabledSslProtocols:
        :param checkCertificateRevocation:
        :return:
        """
    @overload
    def AuthenticateAsServer(self, serverCertificate: X509Certificate) -> None:
        """

        :param serverCertificate:
        """
    @overload
    def AuthenticateAsServer(
        self,
        serverCertificate: X509Certificate,
        clientCertificateRequired: bool,
        checkCertificateRevocation: bool,
    ) -> None:
        """

        :param serverCertificate:
        :param clientCertificateRequired:
        :param checkCertificateRevocation:
        """
    @overload
    def AuthenticateAsServer(
        self,
        serverCertificate: X509Certificate,
        clientCertificateRequired: bool,
        enabledSslProtocols: SslProtocols,
        checkCertificateRevocation: bool,
    ) -> None:
        """

        :param serverCertificate:
        :param clientCertificateRequired:
        :param enabledSslProtocols:
        :param checkCertificateRevocation:
        """
    @overload
    def AuthenticateAsServerAsync(self, serverCertificate: X509Certificate) -> Task:
        """

        :param serverCertificate:
        :return:
        """
    @overload
    def AuthenticateAsServerAsync(
        self,
        serverCertificate: X509Certificate,
        clientCertificateRequired: bool,
        checkCertificateRevocation: bool,
    ) -> Task:
        """

        :param serverCertificate:
        :param clientCertificateRequired:
        :param checkCertificateRevocation:
        :return:
        """
    @overload
    def AuthenticateAsServerAsync(
        self,
        serverCertificate: X509Certificate,
        clientCertificateRequired: bool,
        enabledSslProtocols: SslProtocols,
        checkCertificateRevocation: bool,
    ) -> Task:
        """

        :param serverCertificate:
        :param clientCertificateRequired:
        :param enabledSslProtocols:
        :param checkCertificateRevocation:
        :return:
        """
    @overload
    def BeginAuthenticateAsClient(
        self, targetHost: str, asyncCallback: AsyncCallback, asyncState: object
    ) -> IAsyncResult:
        """

        :param targetHost:
        :param asyncCallback:
        :param asyncState:
        :return:
        """
    @overload
    def BeginAuthenticateAsClient(
        self,
        targetHost: str,
        clientCertificates: X509CertificateCollection,
        checkCertificateRevocation: bool,
        asyncCallback: AsyncCallback,
        asyncState: object,
    ) -> IAsyncResult:
        """

        :param targetHost:
        :param clientCertificates:
        :param checkCertificateRevocation:
        :param asyncCallback:
        :param asyncState:
        :return:
        """
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
        """

        :param targetHost:
        :param clientCertificates:
        :param enabledSslProtocols:
        :param checkCertificateRevocation:
        :param asyncCallback:
        :param asyncState:
        :return:
        """
    @overload
    def BeginAuthenticateAsServer(
        self, serverCertificate: X509Certificate, asyncCallback: AsyncCallback, asyncState: object
    ) -> IAsyncResult:
        """

        :param serverCertificate:
        :param asyncCallback:
        :param asyncState:
        :return:
        """
    @overload
    def BeginAuthenticateAsServer(
        self,
        serverCertificate: X509Certificate,
        clientCertificateRequired: bool,
        checkCertificateRevocation: bool,
        asyncCallback: AsyncCallback,
        asyncState: object,
    ) -> IAsyncResult:
        """

        :param serverCertificate:
        :param clientCertificateRequired:
        :param checkCertificateRevocation:
        :param asyncCallback:
        :param asyncState:
        :return:
        """
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
        """

        :param serverCertificate:
        :param clientCertificateRequired:
        :param enabledSslProtocols:
        :param checkCertificateRevocation:
        :param asyncCallback:
        :param asyncState:
        :return:
        """
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
    def EndAuthenticateAsClient(self, asyncResult: IAsyncResult) -> None:
        """

        :param asyncResult:
        """
    def EndAuthenticateAsServer(self, asyncResult: IAsyncResult) -> None:
        """

        :param asyncResult:
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
    def ShutdownAsync(self) -> Task:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def Write(self, buffer: Array[int]) -> None:
        """

        :param buffer:
        """
    @overload
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
