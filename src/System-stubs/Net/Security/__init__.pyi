from __future__ import annotations

from abc import ABC
from typing import Callable
from typing import List
from typing import Union
from typing import overload

from System import Array
from System import AsyncCallback
from System import Boolean
from System import Byte
from System import Enum
from System import IAsyncResult
from System import ICloneable
from System import IDisposable
from System import Int32
from System import Int64
from System import IntPtr
from System import MulticastDelegate
from System import Object
from System import String
from System import Void
from System.IO import SeekOrigin
from System.IO import Stream
from System.Net import NetworkCredential
from System.Net import TransportContext
from System.Runtime.Serialization import ISerializable
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
from System.Threading.Tasks import Task

# ---------- Types ---------- #

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
ByteType = Union[int, Byte]
IntType = Union[int, Int32]
LongType = Union[int, Int64]
NIntType = Union[int, IntPtr]
ObjectType = Object
StringType = Union[str, String]
VoidType = Union[None, Void]

# ---------- Classes ---------- #

class AuthenticatedStream(ABC, Stream, IDisposable):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def IsAuthenticated(self) -> BooleanType: ...
    @property
    def IsEncrypted(self) -> BooleanType: ...
    @property
    def IsMutuallyAuthenticated(self) -> BooleanType: ...
    @property
    def IsServer(self) -> BooleanType: ...
    @property
    def IsSigned(self) -> BooleanType: ...
    @property
    def LeaveInnerStreamOpen(self) -> BooleanType: ...

    # ---------- Methods ---------- #

    def get_IsAuthenticated(self) -> BooleanType: ...
    def get_IsEncrypted(self) -> BooleanType: ...
    def get_IsMutuallyAuthenticated(self) -> BooleanType: ...
    def get_IsServer(self) -> BooleanType: ...
    def get_IsSigned(self) -> BooleanType: ...
    def get_LeaveInnerStreamOpen(self) -> BooleanType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class LocalCertSelectionCallback(MulticastDelegate, ICloneable, ISerializable):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, object: ObjectType, method: NIntType): ...

    # No Properties

    # ---------- Methods ---------- #

    def BeginInvoke(
        self,
        targetHost: StringType,
        localCertificates: X509CertificateCollection,
        remoteCertificate: X509Certificate,
        acceptableIssuers: ArrayType[StringType],
        callback: AsyncCallback,
        object: ObjectType,
    ) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> X509Certificate: ...
    def Invoke(
        self,
        targetHost: StringType,
        localCertificates: X509CertificateCollection,
        remoteCertificate: X509Certificate,
        acceptableIssuers: ArrayType[StringType],
    ) -> X509Certificate: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class LocalCertificateSelectionCallback(MulticastDelegate, ICloneable, ISerializable):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, object: ObjectType, method: NIntType): ...

    # No Properties

    # ---------- Methods ---------- #

    def BeginInvoke(
        self,
        sender: ObjectType,
        targetHost: StringType,
        localCertificates: X509CertificateCollection,
        remoteCertificate: X509Certificate,
        acceptableIssuers: ArrayType[StringType],
        callback: AsyncCallback,
        object: ObjectType,
    ) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> X509Certificate: ...
    def Invoke(
        self,
        sender: ObjectType,
        targetHost: StringType,
        localCertificates: X509CertificateCollection,
        remoteCertificate: X509Certificate,
        acceptableIssuers: ArrayType[StringType],
    ) -> X509Certificate: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class NegoState(ObjectType):
    """"""

    # No Fields

    # No Constructors

    # No Properties

    # No Methods

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class NegotiateStream(AuthenticatedStream, IDisposable):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self, innerStream: Stream): ...
    @overload
    def __init__(self, innerStream: Stream, leaveInnerStreamOpen: BooleanType): ...

    # ---------- Properties ---------- #

    @property
    def CanRead(self) -> BooleanType: ...
    @property
    def CanSeek(self) -> BooleanType: ...
    @property
    def CanTimeout(self) -> BooleanType: ...
    @property
    def CanWrite(self) -> BooleanType: ...
    @property
    def ImpersonationLevel(self) -> TokenImpersonationLevel: ...
    @property
    def IsAuthenticated(self) -> BooleanType: ...
    @property
    def IsEncrypted(self) -> BooleanType: ...
    @property
    def IsMutuallyAuthenticated(self) -> BooleanType: ...
    @property
    def IsServer(self) -> BooleanType: ...
    @property
    def IsSigned(self) -> BooleanType: ...
    @property
    def Length(self) -> LongType: ...
    @property
    def Position(self) -> LongType: ...
    @Position.setter
    def Position(self, value: LongType) -> None: ...
    @property
    def ReadTimeout(self) -> IntType: ...
    @ReadTimeout.setter
    def ReadTimeout(self, value: IntType) -> None: ...
    @property
    def RemoteIdentity(self) -> IIdentity: ...
    @property
    def WriteTimeout(self) -> IntType: ...
    @WriteTimeout.setter
    def WriteTimeout(self, value: IntType) -> None: ...

    # ---------- Methods ---------- #

    @overload
    def AuthenticateAsClient(self) -> VoidType: ...
    @overload
    def AuthenticateAsClient(
        self, credential: NetworkCredential, targetName: StringType
    ) -> VoidType: ...
    @overload
    def AuthenticateAsClient(
        self, credential: NetworkCredential, binding: ChannelBinding, targetName: StringType
    ) -> VoidType: ...
    @overload
    def AuthenticateAsClient(
        self,
        credential: NetworkCredential,
        targetName: StringType,
        requiredProtectionLevel: ProtectionLevel,
        allowedImpersonationLevel: TokenImpersonationLevel,
    ) -> VoidType: ...
    @overload
    def AuthenticateAsClient(
        self,
        credential: NetworkCredential,
        binding: ChannelBinding,
        targetName: StringType,
        requiredProtectionLevel: ProtectionLevel,
        allowedImpersonationLevel: TokenImpersonationLevel,
    ) -> VoidType: ...
    @overload
    def AuthenticateAsClientAsync(self) -> Task: ...
    @overload
    def AuthenticateAsClientAsync(
        self, credential: NetworkCredential, targetName: StringType
    ) -> Task: ...
    @overload
    def AuthenticateAsClientAsync(
        self,
        credential: NetworkCredential,
        targetName: StringType,
        requiredProtectionLevel: ProtectionLevel,
        allowedImpersonationLevel: TokenImpersonationLevel,
    ) -> Task: ...
    @overload
    def AuthenticateAsClientAsync(
        self, credential: NetworkCredential, binding: ChannelBinding, targetName: StringType
    ) -> Task: ...
    @overload
    def AuthenticateAsClientAsync(
        self,
        credential: NetworkCredential,
        binding: ChannelBinding,
        targetName: StringType,
        requiredProtectionLevel: ProtectionLevel,
        allowedImpersonationLevel: TokenImpersonationLevel,
    ) -> Task: ...
    @overload
    def AuthenticateAsServer(self) -> VoidType: ...
    @overload
    def AuthenticateAsServer(self, policy: ExtendedProtectionPolicy) -> VoidType: ...
    @overload
    def AuthenticateAsServer(
        self,
        credential: NetworkCredential,
        requiredProtectionLevel: ProtectionLevel,
        requiredImpersonationLevel: TokenImpersonationLevel,
    ) -> VoidType: ...
    @overload
    def AuthenticateAsServer(
        self,
        credential: NetworkCredential,
        policy: ExtendedProtectionPolicy,
        requiredProtectionLevel: ProtectionLevel,
        requiredImpersonationLevel: TokenImpersonationLevel,
    ) -> VoidType: ...
    @overload
    def AuthenticateAsServerAsync(self) -> Task: ...
    @overload
    def AuthenticateAsServerAsync(self, policy: ExtendedProtectionPolicy) -> Task: ...
    @overload
    def AuthenticateAsServerAsync(
        self,
        credential: NetworkCredential,
        requiredProtectionLevel: ProtectionLevel,
        requiredImpersonationLevel: TokenImpersonationLevel,
    ) -> Task: ...
    @overload
    def AuthenticateAsServerAsync(
        self,
        credential: NetworkCredential,
        policy: ExtendedProtectionPolicy,
        requiredProtectionLevel: ProtectionLevel,
        requiredImpersonationLevel: TokenImpersonationLevel,
    ) -> Task: ...
    @overload
    def BeginAuthenticateAsClient(
        self, asyncCallback: AsyncCallback, asyncState: ObjectType
    ) -> IAsyncResult: ...
    @overload
    def BeginAuthenticateAsClient(
        self,
        credential: NetworkCredential,
        targetName: StringType,
        asyncCallback: AsyncCallback,
        asyncState: ObjectType,
    ) -> IAsyncResult: ...
    @overload
    def BeginAuthenticateAsClient(
        self,
        credential: NetworkCredential,
        binding: ChannelBinding,
        targetName: StringType,
        asyncCallback: AsyncCallback,
        asyncState: ObjectType,
    ) -> IAsyncResult: ...
    @overload
    def BeginAuthenticateAsClient(
        self,
        credential: NetworkCredential,
        targetName: StringType,
        requiredProtectionLevel: ProtectionLevel,
        allowedImpersonationLevel: TokenImpersonationLevel,
        asyncCallback: AsyncCallback,
        asyncState: ObjectType,
    ) -> IAsyncResult: ...
    @overload
    def BeginAuthenticateAsClient(
        self,
        credential: NetworkCredential,
        binding: ChannelBinding,
        targetName: StringType,
        requiredProtectionLevel: ProtectionLevel,
        allowedImpersonationLevel: TokenImpersonationLevel,
        asyncCallback: AsyncCallback,
        asyncState: ObjectType,
    ) -> IAsyncResult: ...
    @overload
    def BeginAuthenticateAsServer(
        self, asyncCallback: AsyncCallback, asyncState: ObjectType
    ) -> IAsyncResult: ...
    @overload
    def BeginAuthenticateAsServer(
        self, policy: ExtendedProtectionPolicy, asyncCallback: AsyncCallback, asyncState: ObjectType
    ) -> IAsyncResult: ...
    @overload
    def BeginAuthenticateAsServer(
        self,
        credential: NetworkCredential,
        requiredProtectionLevel: ProtectionLevel,
        requiredImpersonationLevel: TokenImpersonationLevel,
        asyncCallback: AsyncCallback,
        asyncState: ObjectType,
    ) -> IAsyncResult: ...
    @overload
    def BeginAuthenticateAsServer(
        self,
        credential: NetworkCredential,
        policy: ExtendedProtectionPolicy,
        requiredProtectionLevel: ProtectionLevel,
        requiredImpersonationLevel: TokenImpersonationLevel,
        asyncCallback: AsyncCallback,
        asyncState: ObjectType,
    ) -> IAsyncResult: ...
    def BeginRead(
        self,
        buffer: ArrayType[ByteType],
        offset: IntType,
        count: IntType,
        asyncCallback: AsyncCallback,
        asyncState: ObjectType,
    ) -> IAsyncResult: ...
    def BeginWrite(
        self,
        buffer: ArrayType[ByteType],
        offset: IntType,
        count: IntType,
        asyncCallback: AsyncCallback,
        asyncState: ObjectType,
    ) -> IAsyncResult: ...
    def EndAuthenticateAsClient(self, asyncResult: IAsyncResult) -> VoidType: ...
    def EndAuthenticateAsServer(self, asyncResult: IAsyncResult) -> VoidType: ...
    def EndRead(self, asyncResult: IAsyncResult) -> IntType: ...
    def EndWrite(self, asyncResult: IAsyncResult) -> VoidType: ...
    def Flush(self) -> VoidType: ...
    def Read(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType) -> IntType: ...
    def Seek(self, offset: LongType, origin: SeekOrigin) -> LongType: ...
    def SetLength(self, value: LongType) -> VoidType: ...
    def Write(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType) -> VoidType: ...
    def get_CanRead(self) -> BooleanType: ...
    def get_CanSeek(self) -> BooleanType: ...
    def get_CanTimeout(self) -> BooleanType: ...
    def get_CanWrite(self) -> BooleanType: ...
    def get_ImpersonationLevel(self) -> TokenImpersonationLevel: ...
    def get_IsAuthenticated(self) -> BooleanType: ...
    def get_IsEncrypted(self) -> BooleanType: ...
    def get_IsMutuallyAuthenticated(self) -> BooleanType: ...
    def get_IsServer(self) -> BooleanType: ...
    def get_IsSigned(self) -> BooleanType: ...
    def get_Length(self) -> LongType: ...
    def get_Position(self) -> LongType: ...
    def get_ReadTimeout(self) -> IntType: ...
    def get_RemoteIdentity(self) -> IIdentity: ...
    def get_WriteTimeout(self) -> IntType: ...
    def set_Position(self, value: LongType) -> VoidType: ...
    def set_ReadTimeout(self, value: IntType) -> VoidType: ...
    def set_WriteTimeout(self, value: IntType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ProtocolToken(ObjectType):
    """"""

    # No Fields

    # No Constructors

    # No Properties

    # No Methods

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class RemoteCertValidationCallback(MulticastDelegate, ICloneable, ISerializable):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, object: ObjectType, method: NIntType): ...

    # No Properties

    # ---------- Methods ---------- #

    def BeginInvoke(
        self,
        host: StringType,
        certificate: X509Certificate,
        chain: X509Chain,
        sslPolicyErrors: SslPolicyErrors,
        callback: AsyncCallback,
        object: ObjectType,
    ) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> BooleanType: ...
    def Invoke(
        self,
        host: StringType,
        certificate: X509Certificate,
        chain: X509Chain,
        sslPolicyErrors: SslPolicyErrors,
    ) -> BooleanType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class RemoteCertificateValidationCallback(MulticastDelegate, ICloneable, ISerializable):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, object: ObjectType, method: NIntType): ...

    # No Properties

    # ---------- Methods ---------- #

    def BeginInvoke(
        self,
        sender: ObjectType,
        certificate: X509Certificate,
        chain: X509Chain,
        sslPolicyErrors: SslPolicyErrors,
        callback: AsyncCallback,
        object: ObjectType,
    ) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> BooleanType: ...
    def Invoke(
        self,
        sender: ObjectType,
        certificate: X509Certificate,
        chain: X509Chain,
        sslPolicyErrors: SslPolicyErrors,
    ) -> BooleanType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class SSPIHandleCache(ABC, ObjectType):
    """"""

    # No Fields

    # No Constructors

    # No Properties

    # No Methods

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class SecureChannel(ObjectType):
    # No Fields

    # No Constructors

    # No Properties

    # ---------- Methods ---------- #

    def CreateFatalHandshakeAlertToken(
        self, sslPolicyErrors: SslPolicyErrors, chain: X509Chain
    ) -> ProtocolToken: ...
    def CreateShutdownToken(self) -> ProtocolToken: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class SslSessionsCache(ABC, ObjectType):
    """"""

    # No Fields

    # No Constructors

    # No Properties

    # No Methods

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class SslState(ObjectType):
    """"""

    # No Fields

    # No Constructors

    # No Properties

    # No Methods

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class SslStream(AuthenticatedStream, IDisposable):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self, innerStream: Stream): ...
    @overload
    def __init__(self, innerStream: Stream, leaveInnerStreamOpen: BooleanType): ...
    @overload
    def __init__(
        self,
        innerStream: Stream,
        leaveInnerStreamOpen: BooleanType,
        userCertificateValidationCallback: RemoteCertificateValidationCallback,
    ): ...
    @overload
    def __init__(
        self,
        innerStream: Stream,
        leaveInnerStreamOpen: BooleanType,
        userCertificateValidationCallback: RemoteCertificateValidationCallback,
        userCertificateSelectionCallback: LocalCertificateSelectionCallback,
    ): ...
    @overload
    def __init__(
        self,
        innerStream: Stream,
        leaveInnerStreamOpen: BooleanType,
        userCertificateValidationCallback: RemoteCertificateValidationCallback,
        userCertificateSelectionCallback: LocalCertificateSelectionCallback,
        encryptionPolicy: EncryptionPolicy,
    ): ...

    # ---------- Properties ---------- #

    @property
    def CanRead(self) -> BooleanType: ...
    @property
    def CanSeek(self) -> BooleanType: ...
    @property
    def CanTimeout(self) -> BooleanType: ...
    @property
    def CanWrite(self) -> BooleanType: ...
    @property
    def CheckCertRevocationStatus(self) -> BooleanType: ...
    @property
    def CipherAlgorithm(self) -> CipherAlgorithmType: ...
    @property
    def CipherStrength(self) -> IntType: ...
    @property
    def HashAlgorithm(self) -> HashAlgorithmType: ...
    @property
    def HashStrength(self) -> IntType: ...
    @property
    def IsAuthenticated(self) -> BooleanType: ...
    @property
    def IsEncrypted(self) -> BooleanType: ...
    @property
    def IsMutuallyAuthenticated(self) -> BooleanType: ...
    @property
    def IsServer(self) -> BooleanType: ...
    @property
    def IsSigned(self) -> BooleanType: ...
    @property
    def KeyExchangeAlgorithm(self) -> ExchangeAlgorithmType: ...
    @property
    def KeyExchangeStrength(self) -> IntType: ...
    @property
    def Length(self) -> LongType: ...
    @property
    def LocalCertificate(self) -> X509Certificate: ...
    @property
    def Position(self) -> LongType: ...
    @Position.setter
    def Position(self, value: LongType) -> None: ...
    @property
    def ReadTimeout(self) -> IntType: ...
    @ReadTimeout.setter
    def ReadTimeout(self, value: IntType) -> None: ...
    @property
    def RemoteCertificate(self) -> X509Certificate: ...
    @property
    def SslProtocol(self) -> SslProtocols: ...
    @property
    def TransportContext(self) -> TransportContext: ...
    @property
    def WriteTimeout(self) -> IntType: ...
    @WriteTimeout.setter
    def WriteTimeout(self, value: IntType) -> None: ...

    # ---------- Methods ---------- #

    @overload
    def AuthenticateAsClient(
        self,
        targetHost: StringType,
        clientCertificates: X509CertificateCollection,
        enabledSslProtocols: SslProtocols,
        checkCertificateRevocation: BooleanType,
    ) -> VoidType: ...
    @overload
    def AuthenticateAsClient(self, targetHost: StringType) -> VoidType: ...
    @overload
    def AuthenticateAsClient(
        self,
        targetHost: StringType,
        clientCertificates: X509CertificateCollection,
        checkCertificateRevocation: BooleanType,
    ) -> VoidType: ...
    @overload
    def AuthenticateAsClientAsync(
        self,
        targetHost: StringType,
        clientCertificates: X509CertificateCollection,
        checkCertificateRevocation: BooleanType,
    ) -> Task: ...
    @overload
    def AuthenticateAsClientAsync(self, targetHost: StringType) -> Task: ...
    @overload
    def AuthenticateAsClientAsync(
        self,
        targetHost: StringType,
        clientCertificates: X509CertificateCollection,
        enabledSslProtocols: SslProtocols,
        checkCertificateRevocation: BooleanType,
    ) -> Task: ...
    @overload
    def AuthenticateAsServer(self, serverCertificate: X509Certificate) -> VoidType: ...
    @overload
    def AuthenticateAsServer(
        self,
        serverCertificate: X509Certificate,
        clientCertificateRequired: BooleanType,
        checkCertificateRevocation: BooleanType,
    ) -> VoidType: ...
    @overload
    def AuthenticateAsServer(
        self,
        serverCertificate: X509Certificate,
        clientCertificateRequired: BooleanType,
        enabledSslProtocols: SslProtocols,
        checkCertificateRevocation: BooleanType,
    ) -> VoidType: ...
    @overload
    def AuthenticateAsServerAsync(
        self,
        serverCertificate: X509Certificate,
        clientCertificateRequired: BooleanType,
        checkCertificateRevocation: BooleanType,
    ) -> Task: ...
    @overload
    def AuthenticateAsServerAsync(self, serverCertificate: X509Certificate) -> Task: ...
    @overload
    def AuthenticateAsServerAsync(
        self,
        serverCertificate: X509Certificate,
        clientCertificateRequired: BooleanType,
        enabledSslProtocols: SslProtocols,
        checkCertificateRevocation: BooleanType,
    ) -> Task: ...
    @overload
    def BeginAuthenticateAsClient(
        self, targetHost: StringType, asyncCallback: AsyncCallback, asyncState: ObjectType
    ) -> IAsyncResult: ...
    @overload
    def BeginAuthenticateAsClient(
        self,
        targetHost: StringType,
        clientCertificates: X509CertificateCollection,
        checkCertificateRevocation: BooleanType,
        asyncCallback: AsyncCallback,
        asyncState: ObjectType,
    ) -> IAsyncResult: ...
    @overload
    def BeginAuthenticateAsClient(
        self,
        targetHost: StringType,
        clientCertificates: X509CertificateCollection,
        enabledSslProtocols: SslProtocols,
        checkCertificateRevocation: BooleanType,
        asyncCallback: AsyncCallback,
        asyncState: ObjectType,
    ) -> IAsyncResult: ...
    @overload
    def BeginAuthenticateAsServer(
        self,
        serverCertificate: X509Certificate,
        asyncCallback: AsyncCallback,
        asyncState: ObjectType,
    ) -> IAsyncResult: ...
    @overload
    def BeginAuthenticateAsServer(
        self,
        serverCertificate: X509Certificate,
        clientCertificateRequired: BooleanType,
        checkCertificateRevocation: BooleanType,
        asyncCallback: AsyncCallback,
        asyncState: ObjectType,
    ) -> IAsyncResult: ...
    @overload
    def BeginAuthenticateAsServer(
        self,
        serverCertificate: X509Certificate,
        clientCertificateRequired: BooleanType,
        enabledSslProtocols: SslProtocols,
        checkCertificateRevocation: BooleanType,
        asyncCallback: AsyncCallback,
        asyncState: ObjectType,
    ) -> IAsyncResult: ...
    def BeginRead(
        self,
        buffer: ArrayType[ByteType],
        offset: IntType,
        count: IntType,
        asyncCallback: AsyncCallback,
        asyncState: ObjectType,
    ) -> IAsyncResult: ...
    def BeginWrite(
        self,
        buffer: ArrayType[ByteType],
        offset: IntType,
        count: IntType,
        asyncCallback: AsyncCallback,
        asyncState: ObjectType,
    ) -> IAsyncResult: ...
    def EndAuthenticateAsClient(self, asyncResult: IAsyncResult) -> VoidType: ...
    def EndAuthenticateAsServer(self, asyncResult: IAsyncResult) -> VoidType: ...
    def EndRead(self, asyncResult: IAsyncResult) -> IntType: ...
    def EndWrite(self, asyncResult: IAsyncResult) -> VoidType: ...
    def Flush(self) -> VoidType: ...
    def Read(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType) -> IntType: ...
    def Seek(self, offset: LongType, origin: SeekOrigin) -> LongType: ...
    def SetLength(self, value: LongType) -> VoidType: ...
    def ShutdownAsync(self) -> Task: ...
    @overload
    def Write(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType) -> VoidType: ...
    @overload
    def Write(self, buffer: ArrayType[ByteType]) -> VoidType: ...
    def get_CanRead(self) -> BooleanType: ...
    def get_CanSeek(self) -> BooleanType: ...
    def get_CanTimeout(self) -> BooleanType: ...
    def get_CanWrite(self) -> BooleanType: ...
    def get_CheckCertRevocationStatus(self) -> BooleanType: ...
    def get_CipherAlgorithm(self) -> CipherAlgorithmType: ...
    def get_CipherStrength(self) -> IntType: ...
    def get_HashAlgorithm(self) -> HashAlgorithmType: ...
    def get_HashStrength(self) -> IntType: ...
    def get_IsAuthenticated(self) -> BooleanType: ...
    def get_IsEncrypted(self) -> BooleanType: ...
    def get_IsMutuallyAuthenticated(self) -> BooleanType: ...
    def get_IsServer(self) -> BooleanType: ...
    def get_IsSigned(self) -> BooleanType: ...
    def get_KeyExchangeAlgorithm(self) -> ExchangeAlgorithmType: ...
    def get_KeyExchangeStrength(self) -> IntType: ...
    def get_Length(self) -> LongType: ...
    def get_LocalCertificate(self) -> X509Certificate: ...
    def get_Position(self) -> LongType: ...
    def get_ReadTimeout(self) -> IntType: ...
    def get_RemoteCertificate(self) -> X509Certificate: ...
    def get_SslProtocol(self) -> SslProtocols: ...
    def get_TransportContext(self) -> TransportContext: ...
    def get_WriteTimeout(self) -> IntType: ...
    def set_Position(self, value: LongType) -> VoidType: ...
    def set_ReadTimeout(self, value: IntType) -> VoidType: ...
    def set_WriteTimeout(self, value: IntType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class _SslStream(ObjectType):
    """"""

    # No Fields

    # No Constructors

    # No Properties

    # No Methods

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

# No Structs

# No Interfaces

# ---------- Enums ---------- #

class AuthenticationLevel(Enum):
    # None = 0
    MutualAuthRequested = 1
    MutualAuthRequired = 2

class EncryptionPolicy(Enum):
    RequireEncryption = 0
    AllowNoEncryption = 1
    NoEncryption = 2

class ProtectionLevel(Enum):
    # None = 0
    Sign = 1
    EncryptAndSign = 2

class SslPolicyErrors(Enum):
    # None = 0
    RemoteCertificateNotAvailable = 1
    RemoteCertificateNameMismatch = 2
    RemoteCertificateChainErrors = 4

class TlsAlertMessage(Enum):
    CloseNotify = 0
    UnexpectedMessage = 10
    BadRecordMac = 20
    DecryptionFailed = 21
    RecordOverflow = 22
    DecompressionFail = 30
    HandshakeFailure = 40
    BadCertificate = 42
    UnsupportedCert = 43
    CertificateRevoked = 44
    CertificateExpired = 45
    CertificateUnknown = 46
    IllegalParameter = 47
    UnknownCA = 48
    AccessDenied = 49
    DecodeError = 50
    DecryptError = 51
    ExportRestriction = 60
    ProtocolVersion = 70
    InsuffientSecurity = 71
    InternalError = 80
    UserCanceled = 90
    NoRenegotiation = 100
    UnsupportedExt = 110

class TlsAlertType(Enum):
    Warning = 1
    Fatal = 2

# ---------- Delegates ---------- #

LocalCertSelectionCallback = Callable[
    [StringType, X509CertificateCollection, X509Certificate, ArrayType[StringType]], X509Certificate
]

LocalCertificateSelectionCallback = Callable[
    [ObjectType, StringType, X509CertificateCollection, X509Certificate, ArrayType[StringType]],
    X509Certificate,
]

RemoteCertValidationCallback = Callable[
    [StringType, X509Certificate, X509Chain, SslPolicyErrors], BooleanType
]

RemoteCertificateValidationCallback = Callable[
    [ObjectType, X509Certificate, X509Chain, SslPolicyErrors], BooleanType
]

__all__ = [
    AuthenticatedStream,
    LocalCertSelectionCallback,
    LocalCertificateSelectionCallback,
    NegoState,
    NegotiateStream,
    ProtocolToken,
    RemoteCertValidationCallback,
    RemoteCertificateValidationCallback,
    SSPIHandleCache,
    SecureChannel,
    SslSessionsCache,
    SslState,
    SslStream,
    _SslStream,
    AuthenticationLevel,
    EncryptionPolicy,
    ProtectionLevel,
    SslPolicyErrors,
    TlsAlertMessage,
    TlsAlertType,
    LocalCertSelectionCallback,
    LocalCertificateSelectionCallback,
    RemoteCertValidationCallback,
    RemoteCertificateValidationCallback,
]
