from __future__ import annotations

from abc import ABC
from typing import Callable, Generic, List, Protocol, Tuple, Union, overload

from Microsoft.Win32.SafeHandles import CriticalHandleMinusOneIsInvalid, CriticalHandleZeroOrMinusOneIsInvalid, SafeHandleMinusOneIsInvalid, SafeHandleZeroOrMinusOneIsInvalid
from System import Array, ArraySegment, AsyncCallback, Boolean, Byte, DateTime, Enum, EventArgs, Exception, FormatException, Guid, IAsyncResult, ICloneable, IDisposable, Int16, Int32, Int64, IntPtr, InvalidOperationException, MarshalByRefObject, MulticastDelegate, Object, String, SystemException, TimeSpan, Type, UInt16, UInt32, Uri, ValueType, Version, Void
from System.Collections import ArrayList, ICollection, IComparer, IEnumerable, IEnumerator, IEqualityComparer
from System.Collections.Generic import ICollection, IEnumerable, IEnumerator, IList
from System.Collections.Specialized import NameObjectCollectionBase, NameValueCollection, StringDictionary
from System.ComponentModel import AsyncCompletedEventArgs, AsyncCompletedEventHandler, Component, IComponent, ProgressChangedEventArgs, Win32Exception
from System.Configuration import ConfigurationValidatorBase
from System.IO import FileAccess, FileMode, FileShare, FileStream, MemoryStream, SeekOrigin, Stream, TextWriter
from System.IO.Compression import CompressionMode, DeflateStream, GZipStream
from System.Net.Cache import RequestCachePolicy
from System.Net.Mime import IEncodableStream
from System.Net.Security import AuthenticationLevel, EncryptionPolicy, RemoteCertificateValidationCallback, TlsAlertMessage, TlsAlertType
from System.Net.Sockets import AddressFamily, NetworkStream
from System.Net.WebSockets import HttpListenerWebSocketContext
from System.Reflection import IReflect
from System.Runtime.InteropServices import SafeHandle, _Attribute, _Exception
from System.Runtime.Serialization import IDeserializationCallback, ISerializable, SerializationInfo, StreamingContext
from System.Security import CodeAccessPermission, IPermission, ISecurityEncodable, IStackWalk, SecureString, SecurityElement
from System.Security.Authentication import SslProtocols
from System.Security.Authentication.ExtendedProtection import ChannelBinding, ChannelBindingKind, ExtendedProtectionPolicy, ServiceNameCollection, TokenBinding
from System.Security.Cryptography.X509Certificates import X509Certificate, X509Certificate2, X509CertificateCollection
from System.Security.Permissions import CodeAccessSecurityAttribute, IUnrestrictedPermission, PermissionState, SecurityAction
from System.Security.Principal import GenericIdentity, IIdentity, IPrincipal, TokenImpersonationLevel
from System.Text import Encoding
from System.Text.RegularExpressions import Regex
from System.Threading import CancellationToken, ExecutionContext, WaitHandle
from System.Threading.Tasks import Task

# ---------- Types ---------- #

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
ByteType = Union[int, Byte]
IntType = Union[int, Int32]
LongType = Union[int, Int64]
NIntType = Union[int, IntPtr]
ObjectType = Object
ShortType = Union[int, Int16]
StringType = Union[str, String]
TypeType = Union[type, Type]
UIntType = Union[int, UInt32]
UShortType = Union[int, UInt16]
VoidType = Union[None, Void]


class EventType(Generic[T]):
    def __iadd__(self, other: T): ...
    
    def __isub__(self, other: T): ...


# ---------- Classes ---------- #

class AsyncProtocolCallback(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, asyncRequest: AsyncProtocolRequest, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, asyncRequest: AsyncProtocolRequest) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AsyncProtocolRequest(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def AsyncState(self) -> ObjectType: ...
    
    @AsyncState.setter
    def AsyncState(self, value: ObjectType) -> None: ...
    
    @property
    def Buffer(self) -> ArrayType[ByteType]: ...
    
    @Buffer.setter
    def Buffer(self, value: ArrayType[ByteType]) -> None: ...
    
    @property
    def Count(self) -> IntType: ...
    
    @Count.setter
    def Count(self, value: IntType) -> None: ...
    
    @property
    def Offset(self) -> IntType: ...
    
    @Offset.setter
    def Offset(self, value: IntType) -> None: ...
    
    @property
    def Result(self) -> IntType: ...
    
    @Result.setter
    def Result(self, value: IntType) -> None: ...
    
    @property
    def UserAsyncResult(self) -> LazyAsyncResult: ...
    
    @UserAsyncResult.setter
    def UserAsyncResult(self, value: LazyAsyncResult) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self, userAsyncResult: LazyAsyncResult): ...
    
    # ---------- Properties ---------- #
    
    @property
    def MustCompleteSynchronously(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def SetNextRequest(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType, callback: AsyncProtocolCallback) -> VoidType: ...
    
    def get_MustCompleteSynchronously(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AsyncRequestContext(RequestContextBase, IDisposable):
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


class AuthenticationManager(ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def CredentialPolicy() -> ICredentialPolicy: ...
    
    @staticmethod
    @CredentialPolicy.setter
    def CredentialPolicy(value: ICredentialPolicy) -> None: ...
    
    @staticmethod
    @property
    def CustomTargetNameDictionary() -> StringDictionary: ...
    
    @staticmethod
    @property
    def RegisteredModules() -> IEnumerator: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def Authenticate(challenge: StringType, request: WebRequest, credentials: ICredentials) -> Authorization: ...
    
    @staticmethod
    def PreAuthenticate(request: WebRequest, credentials: ICredentials) -> Authorization: ...
    
    @staticmethod
    def Register(authenticationModule: IAuthenticationModule) -> VoidType: ...
    
    @staticmethod
    @overload
    def Unregister(authenticationModule: IAuthenticationModule) -> VoidType: ...
    
    @staticmethod
    @overload
    def Unregister(authenticationScheme: StringType) -> VoidType: ...
    
    @staticmethod
    def get_CredentialPolicy() -> ICredentialPolicy: ...
    
    @staticmethod
    def get_CustomTargetNameDictionary() -> StringDictionary: ...
    
    @staticmethod
    def get_RegisteredModules() -> IEnumerator: ...
    
    @staticmethod
    def set_CredentialPolicy(value: ICredentialPolicy) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AuthenticationManager2(AuthenticationManagerBase, IAuthenticationManager):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, maxPrefixLookupEntries: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def RegisteredModules(self) -> IEnumerator: ...
    
    # ---------- Methods ---------- #
    
    def Authenticate(self, challenge: StringType, request: WebRequest, credentials: ICredentials) -> Authorization: ...
    
    def BindModule(self, uri: Uri, response: Authorization, module: IAuthenticationModule) -> VoidType: ...
    
    def PreAuthenticate(self, request: WebRequest, credentials: ICredentials) -> Authorization: ...
    
    def Register(self, authenticationModule: IAuthenticationModule) -> VoidType: ...
    
    @overload
    def Unregister(self, authenticationModule: IAuthenticationModule) -> VoidType: ...
    
    @overload
    def Unregister(self, authenticationScheme: StringType) -> VoidType: ...
    
    def get_RegisteredModules(self) -> IEnumerator: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AuthenticationManagerBase(ABC, ObjectType, IAuthenticationManager):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def CredentialPolicy(self) -> ICredentialPolicy: ...
    
    @CredentialPolicy.setter
    def CredentialPolicy(self, value: ICredentialPolicy) -> None: ...
    
    @property
    def CustomTargetNameDictionary(self) -> StringDictionary: ...
    
    @property
    def OSSupportsExtendedProtection(self) -> BooleanType: ...
    
    @property
    def RegisteredModules(self) -> IEnumerator: ...
    
    @property
    def SpnDictionary(self) -> SpnDictionary: ...
    
    @property
    def SspSupportsExtendedProtection(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def Authenticate(self, challenge: StringType, request: WebRequest, credentials: ICredentials) -> Authorization: ...
    
    def BindModule(self, uri: Uri, response: Authorization, module: IAuthenticationModule) -> VoidType: ...
    
    def EnsureConfigLoaded(self) -> VoidType: ...
    
    def PreAuthenticate(self, request: WebRequest, credentials: ICredentials) -> Authorization: ...
    
    def Register(self, authenticationModule: IAuthenticationModule) -> VoidType: ...
    
    @overload
    def Unregister(self, authenticationModule: IAuthenticationModule) -> VoidType: ...
    
    @overload
    def Unregister(self, authenticationScheme: StringType) -> VoidType: ...
    
    def get_CredentialPolicy(self) -> ICredentialPolicy: ...
    
    def get_CustomTargetNameDictionary(self) -> StringDictionary: ...
    
    def get_OSSupportsExtendedProtection(self) -> BooleanType: ...
    
    def get_RegisteredModules(self) -> IEnumerator: ...
    
    def get_SpnDictionary(self) -> SpnDictionary: ...
    
    def get_SspSupportsExtendedProtection(self) -> BooleanType: ...
    
    def set_CredentialPolicy(self, value: ICredentialPolicy) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AuthenticationManagerDefault(AuthenticationManagerBase, IAuthenticationManager):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def RegisteredModules(self) -> IEnumerator: ...
    
    # ---------- Methods ---------- #
    
    def Authenticate(self, challenge: StringType, request: WebRequest, credentials: ICredentials) -> Authorization: ...
    
    def BindModule(self, uri: Uri, response: Authorization, module: IAuthenticationModule) -> VoidType: ...
    
    def EnsureConfigLoaded(self) -> VoidType: ...
    
    def PreAuthenticate(self, request: WebRequest, credentials: ICredentials) -> Authorization: ...
    
    def Register(self, authenticationModule: IAuthenticationModule) -> VoidType: ...
    
    @overload
    def Unregister(self, authenticationModule: IAuthenticationModule) -> VoidType: ...
    
    @overload
    def Unregister(self, authenticationScheme: StringType) -> VoidType: ...
    
    def get_RegisteredModules(self) -> IEnumerator: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AuthenticationSchemeSelector(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, httpRequest: HttpListenerRequest, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> AuthenticationSchemes: ...
    
    def Invoke(self, httpRequest: HttpListenerRequest) -> AuthenticationSchemes: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AuthenticationState(ObjectType):
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


class Authorization(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, token: StringType): ...
    
    @overload
    def __init__(self, token: StringType, finished: BooleanType): ...
    
    @overload
    def __init__(self, token: StringType, finished: BooleanType, connectionGroupId: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Complete(self) -> BooleanType: ...
    
    @property
    def ConnectionGroupId(self) -> StringType: ...
    
    @property
    def Message(self) -> StringType: ...
    
    @property
    def MutuallyAuthenticated(self) -> BooleanType: ...
    
    @MutuallyAuthenticated.setter
    def MutuallyAuthenticated(self, value: BooleanType) -> None: ...
    
    @property
    def ProtectionRealm(self) -> ArrayType[StringType]: ...
    
    @ProtectionRealm.setter
    def ProtectionRealm(self, value: ArrayType[StringType]) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Complete(self) -> BooleanType: ...
    
    def get_ConnectionGroupId(self) -> StringType: ...
    
    def get_Message(self) -> StringType: ...
    
    def get_MutuallyAuthenticated(self) -> BooleanType: ...
    
    def get_ProtectionRealm(self) -> ArrayType[StringType]: ...
    
    def set_MutuallyAuthenticated(self, value: BooleanType) -> VoidType: ...
    
    def set_ProtectionRealm(self, value: ArrayType[StringType]) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AutoWebProxyScriptEngine(ObjectType):
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


class AutoWebProxyScriptWrapper(ObjectType):
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


class Base64Stream(DelegatedStream, IDisposable, IEncodableStream):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def CanWrite(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def BeginRead(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType, callback: AsyncCallback, state: ObjectType) -> IAsyncResult: ...
    
    def BeginWrite(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType, callback: AsyncCallback, state: ObjectType) -> IAsyncResult: ...
    
    def Close(self) -> VoidType: ...
    
    def DecodeBytes(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType) -> IntType: ...
    
    def EncodeBytes(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType) -> IntType: ...
    
    def EndRead(self, asyncResult: IAsyncResult) -> IntType: ...
    
    def EndWrite(self, asyncResult: IAsyncResult) -> VoidType: ...
    
    def Flush(self) -> VoidType: ...
    
    def GetEncodedString(self) -> StringType: ...
    
    def GetStream(self) -> Stream: ...
    
    def Read(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType) -> IntType: ...
    
    def Write(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType) -> VoidType: ...
    
    def get_CanWrite(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class BaseLoggingObject(ObjectType):
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


class BaseWebProxyFinder(ABC, ObjectType, IWebProxyFinder, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, engine: AutoWebProxyScriptEngine): ...
    
    # ---------- Properties ---------- #
    
    @property
    def IsUnrecognizedScheme(self) -> BooleanType: ...
    
    @property
    def IsValid(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def Abort(self) -> VoidType: ...
    
    def Dispose(self) -> VoidType: ...
    
    def GetProxies(self, destination: Uri, proxyList: IList[StringType]) -> Tuple[BooleanType, IList[StringType]]: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_IsUnrecognizedScheme(self) -> BooleanType: ...
    
    def get_IsValid(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class BasicClient(ObjectType, IAuthenticationModule):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AuthenticationType(self) -> StringType: ...
    
    @property
    def CanPreAuthenticate(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def Authenticate(self, challenge: StringType, webRequest: WebRequest, credentials: ICredentials) -> Authorization: ...
    
    def PreAuthenticate(self, webRequest: WebRequest, credentials: ICredentials) -> Authorization: ...
    
    def get_AuthenticationType(self) -> StringType: ...
    
    def get_CanPreAuthenticate(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class BindIPEndPoint(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, servicePoint: ServicePoint, remoteEndPoint: IPEndPoint, retryCount: IntType, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> IPEndPoint: ...
    
    def Invoke(self, servicePoint: ServicePoint, remoteEndPoint: IPEndPoint, retryCount: IntType) -> IPEndPoint: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class BufferAsyncResult(LazyAsyncResult, IAsyncResult):
    # ---------- Fields ---------- #
    
    @property
    def Buffer(self) -> ArrayType[ByteType]: ...
    
    @Buffer.setter
    def Buffer(self, value: ArrayType[ByteType]) -> None: ...
    
    @property
    def Buffers(self) -> ArrayType[BufferOffsetSize]: ...
    
    @Buffers.setter
    def Buffers(self, value: ArrayType[BufferOffsetSize]) -> None: ...
    
    @property
    def Count(self) -> IntType: ...
    
    @Count.setter
    def Count(self, value: IntType) -> None: ...
    
    @property
    def IsWrite(self) -> BooleanType: ...
    
    @IsWrite.setter
    def IsWrite(self, value: BooleanType) -> None: ...
    
    @property
    def Offset(self) -> IntType: ...
    
    @Offset.setter
    def Offset(self, value: IntType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, asyncObject: ObjectType, buffers: ArrayType[BufferOffsetSize], asyncState: ObjectType, asyncCallback: AsyncCallback): ...
    
    @overload
    def __init__(self, asyncObject: ObjectType, buffer: ArrayType[ByteType], offset: IntType, count: IntType, asyncState: ObjectType, asyncCallback: AsyncCallback): ...
    
    @overload
    def __init__(self, asyncObject: ObjectType, buffer: ArrayType[ByteType], offset: IntType, count: IntType, isWrite: BooleanType, asyncState: ObjectType, asyncCallback: AsyncCallback): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class BufferOffsetSize(ObjectType):
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


class BufferedReadStream(DelegatedStream, IDisposable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def CanSeek(self) -> BooleanType: ...
    
    @property
    def CanWrite(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def BeginRead(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType, callback: AsyncCallback, state: ObjectType) -> IAsyncResult: ...
    
    def EndRead(self, asyncResult: IAsyncResult) -> IntType: ...
    
    def Read(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType) -> IntType: ...
    
    @overload
    def ReadAsync(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType, cancellationToken: CancellationToken) -> Task[IntType]: ...
    
    def ReadByte(self) -> IntType: ...
    
    def get_CanSeek(self) -> BooleanType: ...
    
    def get_CanWrite(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CachedTransportContext(TransportContext):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetChannelBinding(self, kind: ChannelBindingKind) -> ChannelBinding: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CallbackClosure(ObjectType):
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


class CaseInsensitiveAscii(ObjectType, IEqualityComparer, IComparer):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Compare(self, firstObject: ObjectType, secondObject: ObjectType) -> IntType: ...
    
    @overload
    def Equals(self, firstObject: ObjectType, secondObject: ObjectType) -> BooleanType: ...
    
    @overload
    def GetHashCode(self, myObject: ObjectType) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CertPolicyValidationCallback(ObjectType):
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


class ChunkParser(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, dataSource: Stream, internalBuffer: ArrayType[ByteType], initialBufferOffset: IntType, initialBufferCount: IntType, maxBufferLength: IntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Read(self, userBuffer: ArrayType[ByteType], userBufferOffset: IntType, userBufferCount: IntType) -> IntType: ...
    
    def ReadAsync(self, caller: ObjectType, userBuffer: ArrayType[ByteType], userBufferOffset: IntType, userBufferCount: IntType, callback: AsyncCallback, state: ObjectType) -> IAsyncResult: ...
    
    def ReadCallback(self, ar: IAsyncResult) -> VoidType: ...
    
    def TryGetLeftoverBytes(self, buffer: ByteType, leftoverBufferOffset: IntType, leftoverBufferSize: IntType) -> Tuple[BooleanType, ByteType, IntType, IntType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ClosableStream(DelegatedStream, IDisposable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ComNetOS(ABC, ObjectType):
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


class CommandStream(PooledStream, IDisposable):
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


class Comparer(ObjectType, IComparer):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CompletionDelegate(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, responseBytes: ArrayType[ByteType], exception: Exception, State: ObjectType, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, responseBytes: ArrayType[ByteType], exception: Exception, State: ObjectType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ConnectStream(Stream, IDisposable, ICloseEx, IRequestLifetimeTracker):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, connection: Connection, request: HttpWebRequest): ...
    
    @overload
    def __init__(self, connection: Connection, buffer: ArrayType[ByteType], offset: IntType, bufferCount: IntType, readCount: LongType, chunked: BooleanType, request: HttpWebRequest): ...
    
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
    def WriteTimeout(self) -> IntType: ...
    
    @WriteTimeout.setter
    def WriteTimeout(self, value: IntType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def BeginRead(self, buffer: ArrayType[ByteType], offset: IntType, size: IntType, callback: AsyncCallback, state: ObjectType) -> IAsyncResult: ...
    
    def BeginWrite(self, buffer: ArrayType[ByteType], offset: IntType, size: IntType, callback: AsyncCallback, state: ObjectType) -> IAsyncResult: ...
    
    def EndRead(self, asyncResult: IAsyncResult) -> IntType: ...
    
    def EndWrite(self, asyncResult: IAsyncResult) -> VoidType: ...
    
    def Flush(self) -> VoidType: ...
    
    @overload
    def FlushAsync(self, cancellationToken: CancellationToken) -> Task: ...
    
    def Read(self, buffer: ArrayType[ByteType], offset: IntType, size: IntType) -> Tuple[IntType, ArrayType[ByteType]]: ...
    
    def Seek(self, offset: LongType, origin: SeekOrigin) -> LongType: ...
    
    def SetLength(self, value: LongType) -> VoidType: ...
    
    def Write(self, buffer: ArrayType[ByteType], offset: IntType, size: IntType) -> VoidType: ...
    
    def get_CanRead(self) -> BooleanType: ...
    
    def get_CanSeek(self) -> BooleanType: ...
    
    def get_CanTimeout(self) -> BooleanType: ...
    
    def get_CanWrite(self) -> BooleanType: ...
    
    def get_Length(self) -> LongType: ...
    
    def get_Position(self) -> LongType: ...
    
    def get_ReadTimeout(self) -> IntType: ...
    
    def get_WriteTimeout(self) -> IntType: ...
    
    def set_Position(self, value: LongType) -> VoidType: ...
    
    def set_ReadTimeout(self, value: IntType) -> VoidType: ...
    
    def set_WriteTimeout(self, value: IntType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ConnectStreamContext(TransportContext):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetChannelBinding(self, kind: ChannelBindingKind) -> ChannelBinding: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Connection(PooledStream, IDisposable):
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


class ConnectionGroup(ObjectType):
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


class ConnectionPool(ObjectType):
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


class ConnectionPoolManager(ObjectType):
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


class ConnectionReturnResult(ObjectType):
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


class ContextAwareResult(LazyAsyncResult, IAsyncResult):
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


class Cookie(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, name: StringType, value: StringType): ...
    
    @overload
    def __init__(self, name: StringType, value: StringType, path: StringType): ...
    
    @overload
    def __init__(self, name: StringType, value: StringType, path: StringType, domain: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Comment(self) -> StringType: ...
    
    @Comment.setter
    def Comment(self, value: StringType) -> None: ...
    
    @property
    def CommentUri(self) -> Uri: ...
    
    @CommentUri.setter
    def CommentUri(self, value: Uri) -> None: ...
    
    @property
    def Discard(self) -> BooleanType: ...
    
    @Discard.setter
    def Discard(self, value: BooleanType) -> None: ...
    
    @property
    def Domain(self) -> StringType: ...
    
    @Domain.setter
    def Domain(self, value: StringType) -> None: ...
    
    @property
    def Expired(self) -> BooleanType: ...
    
    @Expired.setter
    def Expired(self, value: BooleanType) -> None: ...
    
    @property
    def Expires(self) -> DateTime: ...
    
    @Expires.setter
    def Expires(self, value: DateTime) -> None: ...
    
    @property
    def HttpOnly(self) -> BooleanType: ...
    
    @HttpOnly.setter
    def HttpOnly(self, value: BooleanType) -> None: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @Name.setter
    def Name(self, value: StringType) -> None: ...
    
    @property
    def Path(self) -> StringType: ...
    
    @Path.setter
    def Path(self, value: StringType) -> None: ...
    
    @property
    def Port(self) -> StringType: ...
    
    @Port.setter
    def Port(self, value: StringType) -> None: ...
    
    @property
    def Secure(self) -> BooleanType: ...
    
    @Secure.setter
    def Secure(self, value: BooleanType) -> None: ...
    
    @property
    def TimeStamp(self) -> DateTime: ...
    
    @property
    def Value(self) -> StringType: ...
    
    @Value.setter
    def Value(self, value: StringType) -> None: ...
    
    @property
    def Version(self) -> IntType: ...
    
    @Version.setter
    def Version(self, value: IntType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, comparand: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Comment(self) -> StringType: ...
    
    def get_CommentUri(self) -> Uri: ...
    
    def get_Discard(self) -> BooleanType: ...
    
    def get_Domain(self) -> StringType: ...
    
    def get_Expired(self) -> BooleanType: ...
    
    def get_Expires(self) -> DateTime: ...
    
    def get_HttpOnly(self) -> BooleanType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_Path(self) -> StringType: ...
    
    def get_Port(self) -> StringType: ...
    
    def get_Secure(self) -> BooleanType: ...
    
    def get_TimeStamp(self) -> DateTime: ...
    
    def get_Value(self) -> StringType: ...
    
    def get_Version(self) -> IntType: ...
    
    def set_Comment(self, value: StringType) -> VoidType: ...
    
    def set_CommentUri(self, value: Uri) -> VoidType: ...
    
    def set_Discard(self, value: BooleanType) -> VoidType: ...
    
    def set_Domain(self, value: StringType) -> VoidType: ...
    
    def set_Expired(self, value: BooleanType) -> VoidType: ...
    
    def set_Expires(self, value: DateTime) -> VoidType: ...
    
    def set_HttpOnly(self, value: BooleanType) -> VoidType: ...
    
    def set_Name(self, value: StringType) -> VoidType: ...
    
    def set_Path(self, value: StringType) -> VoidType: ...
    
    def set_Port(self, value: StringType) -> VoidType: ...
    
    def set_Secure(self, value: BooleanType) -> VoidType: ...
    
    def set_Value(self, value: StringType) -> VoidType: ...
    
    def set_Version(self, value: IntType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CookieCollection(ObjectType, ICollection, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def IsReadOnly(self) -> BooleanType: ...
    
    @property
    def IsSynchronized(self) -> BooleanType: ...
    
    @property
    def Item(self) -> Cookie: ...
    
    @property
    def Item(self) -> Cookie: ...
    
    @property
    def SyncRoot(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Add(self, cookie: Cookie) -> VoidType: ...
    
    @overload
    def Add(self, cookies: CookieCollection) -> VoidType: ...
    
    @overload
    def CopyTo(self, array: Array, index: IntType) -> VoidType: ...
    
    @overload
    def CopyTo(self, array: ArrayType[Cookie], index: IntType) -> VoidType: ...
    
    def GetEnumerator(self) -> IEnumerator: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_IsReadOnly(self) -> BooleanType: ...
    
    def get_IsSynchronized(self) -> BooleanType: ...
    
    @overload
    def get_Item(self, index: IntType) -> Cookie: ...
    
    @overload
    def get_Item(self, name: StringType) -> Cookie: ...
    
    def get_SyncRoot(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CookieContainer(ObjectType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def DefaultCookieLengthLimit() -> IntType: ...
    
    @staticmethod
    @property
    def DefaultCookieLimit() -> IntType: ...
    
    @staticmethod
    @property
    def DefaultPerDomainCookieLimit() -> IntType: ...
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, capacity: IntType): ...
    
    @overload
    def __init__(self, capacity: IntType, perDomainCapacity: IntType, maxCookieSize: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Capacity(self) -> IntType: ...
    
    @Capacity.setter
    def Capacity(self, value: IntType) -> None: ...
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def MaxCookieSize(self) -> IntType: ...
    
    @MaxCookieSize.setter
    def MaxCookieSize(self, value: IntType) -> None: ...
    
    @property
    def PerDomainCapacity(self) -> IntType: ...
    
    @PerDomainCapacity.setter
    def PerDomainCapacity(self, value: IntType) -> None: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Add(self, cookies: CookieCollection) -> VoidType: ...
    
    @overload
    def Add(self, uri: Uri, cookie: Cookie) -> VoidType: ...
    
    @overload
    def Add(self, uri: Uri, cookies: CookieCollection) -> VoidType: ...
    
    @overload
    def Add(self, cookie: Cookie) -> VoidType: ...
    
    def GetCookieHeader(self, uri: Uri) -> StringType: ...
    
    def GetCookies(self, uri: Uri) -> CookieCollection: ...
    
    def SetCookies(self, uri: Uri, cookieHeader: StringType) -> VoidType: ...
    
    def get_Capacity(self) -> IntType: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_MaxCookieSize(self) -> IntType: ...
    
    def get_PerDomainCapacity(self) -> IntType: ...
    
    def set_Capacity(self, value: IntType) -> VoidType: ...
    
    def set_MaxCookieSize(self, value: IntType) -> VoidType: ...
    
    def set_PerDomainCapacity(self, value: IntType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CookieException(FormatException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetObjectData(self, serializationInfo: SerializationInfo, streamingContext: StreamingContext) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CookieModule(ABC, ObjectType):
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


class CookieParser(ObjectType):
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


class CookieTokenizer(ObjectType):
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


class CoreResponseData(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def m_ConnectStream(self) -> Stream: ...
    
    @m_ConnectStream.setter
    def m_ConnectStream(self, value: Stream) -> None: ...
    
    @property
    def m_ContentLength(self) -> LongType: ...
    
    @m_ContentLength.setter
    def m_ContentLength(self, value: LongType) -> None: ...
    
    @property
    def m_IsVersionHttp11(self) -> BooleanType: ...
    
    @m_IsVersionHttp11.setter
    def m_IsVersionHttp11(self, value: BooleanType) -> None: ...
    
    @property
    def m_ResponseHeaders(self) -> WebHeaderCollection: ...
    
    @m_ResponseHeaders.setter
    def m_ResponseHeaders(self, value: WebHeaderCollection) -> None: ...
    
    @property
    def m_StatusCode(self) -> HttpStatusCode: ...
    
    @m_StatusCode.setter
    def m_StatusCode(self, value: HttpStatusCode) -> None: ...
    
    @property
    def m_StatusDescription(self) -> StringType: ...
    
    @m_StatusDescription.setter
    def m_StatusDescription(self, value: StringType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CreateConnectionDelegate(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, pool: ConnectionPool, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> PooledStream: ...
    
    def Invoke(self, pool: ConnectionPool) -> PooledStream: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CredentialCache(ObjectType, ICredentials, ICredentialsByHost, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def DefaultCredentials() -> ICredentials: ...
    
    @staticmethod
    @property
    def DefaultNetworkCredentials() -> NetworkCredential: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Add(self, uriPrefix: Uri, authType: StringType, cred: NetworkCredential) -> VoidType: ...
    
    @overload
    def Add(self, host: StringType, port: IntType, authenticationType: StringType, credential: NetworkCredential) -> VoidType: ...
    
    @overload
    def GetCredential(self, uriPrefix: Uri, authType: StringType) -> NetworkCredential: ...
    
    @overload
    def GetCredential(self, host: StringType, port: IntType, authenticationType: StringType) -> NetworkCredential: ...
    
    def GetEnumerator(self) -> IEnumerator: ...
    
    @overload
    def Remove(self, uriPrefix: Uri, authType: StringType) -> VoidType: ...
    
    @overload
    def Remove(self, host: StringType, port: IntType, authenticationType: StringType) -> VoidType: ...
    
    @staticmethod
    def get_DefaultCredentials() -> ICredentials: ...
    
    @staticmethod
    def get_DefaultNetworkCredentials() -> NetworkCredential: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CredentialHostKey(ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Equals(self, comparand: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CredentialKey(ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Equals(self, comparand: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DefaultCertPolicy(ObjectType, ICertificatePolicy):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def CheckValidationResult(self, sp: ServicePoint, cert: X509Certificate, request: WebRequest, problem: IntType) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DeflateWrapperStream(DeflateStream, IDisposable, ICloseEx, IRequestLifetimeTracker):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, stream: Stream, mode: CompressionMode): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginRead(self, buffer: ArrayType[ByteType], offset: IntType, size: IntType, callback: AsyncCallback, state: ObjectType) -> IAsyncResult: ...
    
    def EndRead(self, asyncResult: IAsyncResult) -> IntType: ...
    
    def Read(self, buffer: ArrayType[ByteType], offset: IntType, size: IntType) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DelayedRegex(ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def ToString(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DelegatedStream(Stream, IDisposable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def CanRead(self) -> BooleanType: ...
    
    @property
    def CanSeek(self) -> BooleanType: ...
    
    @property
    def CanWrite(self) -> BooleanType: ...
    
    @property
    def Length(self) -> LongType: ...
    
    @property
    def Position(self) -> LongType: ...
    
    @Position.setter
    def Position(self, value: LongType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def BeginRead(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType, callback: AsyncCallback, state: ObjectType) -> IAsyncResult: ...
    
    def BeginWrite(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType, callback: AsyncCallback, state: ObjectType) -> IAsyncResult: ...
    
    def Close(self) -> VoidType: ...
    
    def EndRead(self, asyncResult: IAsyncResult) -> IntType: ...
    
    def EndWrite(self, asyncResult: IAsyncResult) -> VoidType: ...
    
    def Flush(self) -> VoidType: ...
    
    @overload
    def FlushAsync(self, cancellationToken: CancellationToken) -> Task: ...
    
    def Read(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType) -> IntType: ...
    
    @overload
    def ReadAsync(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType, cancellationToken: CancellationToken) -> Task[IntType]: ...
    
    def Seek(self, offset: LongType, origin: SeekOrigin) -> LongType: ...
    
    def SetLength(self, value: LongType) -> VoidType: ...
    
    def Write(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType) -> VoidType: ...
    
    @overload
    def WriteAsync(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType, cancellationToken: CancellationToken) -> Task: ...
    
    def get_CanRead(self) -> BooleanType: ...
    
    def get_CanSeek(self) -> BooleanType: ...
    
    def get_CanWrite(self) -> BooleanType: ...
    
    def get_Length(self) -> LongType: ...
    
    def get_Position(self) -> LongType: ...
    
    def set_Position(self, value: LongType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DigestClient(ObjectType, ISessionAuthenticationModule, IAuthenticationModule):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AuthenticationType(self) -> StringType: ...
    
    @property
    def CanPreAuthenticate(self) -> BooleanType: ...
    
    @property
    def CanUseDefaultCredentials(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def Authenticate(self, challenge: StringType, webRequest: WebRequest, credentials: ICredentials) -> Authorization: ...
    
    def ClearSession(self, webRequest: WebRequest) -> VoidType: ...
    
    def PreAuthenticate(self, webRequest: WebRequest, credentials: ICredentials) -> Authorization: ...
    
    def Update(self, challenge: StringType, webRequest: WebRequest) -> BooleanType: ...
    
    def get_AuthenticationType(self) -> StringType: ...
    
    def get_CanPreAuthenticate(self) -> BooleanType: ...
    
    def get_CanUseDefaultCredentials(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DirectProxy(ProxyChain, IEnumerable[Uri], IEnumerable, IDisposable):
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


class Dns(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def BeginGetHostAddresses(hostNameOrAddress: StringType, requestCallback: AsyncCallback, state: ObjectType) -> IAsyncResult: ...
    
    @staticmethod
    def BeginGetHostByName(hostName: StringType, requestCallback: AsyncCallback, stateObject: ObjectType) -> IAsyncResult: ...
    
    @staticmethod
    @overload
    def BeginGetHostEntry(hostNameOrAddress: StringType, requestCallback: AsyncCallback, stateObject: ObjectType) -> IAsyncResult: ...
    
    @staticmethod
    @overload
    def BeginGetHostEntry(address: IPAddress, requestCallback: AsyncCallback, stateObject: ObjectType) -> IAsyncResult: ...
    
    @staticmethod
    def BeginResolve(hostName: StringType, requestCallback: AsyncCallback, stateObject: ObjectType) -> IAsyncResult: ...
    
    @staticmethod
    def EndGetHostAddresses(asyncResult: IAsyncResult) -> ArrayType[IPAddress]: ...
    
    @staticmethod
    def EndGetHostByName(asyncResult: IAsyncResult) -> IPHostEntry: ...
    
    @staticmethod
    def EndGetHostEntry(asyncResult: IAsyncResult) -> IPHostEntry: ...
    
    @staticmethod
    def EndResolve(asyncResult: IAsyncResult) -> IPHostEntry: ...
    
    @staticmethod
    def GetHostAddresses(hostNameOrAddress: StringType) -> ArrayType[IPAddress]: ...
    
    @staticmethod
    def GetHostAddressesAsync(hostNameOrAddress: StringType) -> Task[ArrayType[IPAddress]]: ...
    
    @staticmethod
    @overload
    def GetHostByAddress(address: StringType) -> IPHostEntry: ...
    
    @staticmethod
    @overload
    def GetHostByAddress(address: IPAddress) -> IPHostEntry: ...
    
    @staticmethod
    def GetHostByName(hostName: StringType) -> IPHostEntry: ...
    
    @staticmethod
    @overload
    def GetHostEntry(address: IPAddress) -> IPHostEntry: ...
    
    @staticmethod
    @overload
    def GetHostEntry(hostNameOrAddress: StringType) -> IPHostEntry: ...
    
    @staticmethod
    @overload
    def GetHostEntryAsync(address: IPAddress) -> Task[IPHostEntry]: ...
    
    @staticmethod
    @overload
    def GetHostEntryAsync(hostNameOrAddress: StringType) -> Task[IPHostEntry]: ...
    
    @staticmethod
    def GetHostName() -> StringType: ...
    
    @staticmethod
    def Resolve(hostName: StringType) -> IPHostEntry: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DnsEndPoint(EndPoint):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, host: StringType, port: IntType): ...
    
    @overload
    def __init__(self, host: StringType, port: IntType, addressFamily: AddressFamily): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AddressFamily(self) -> AddressFamily: ...
    
    @property
    def Host(self) -> StringType: ...
    
    @property
    def Port(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, comparand: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_AddressFamily(self) -> AddressFamily: ...
    
    def get_Host(self) -> StringType: ...
    
    def get_Port(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DnsPermission(CodeAccessPermission, IPermission, ISecurityEncodable, IStackWalk, IUnrestrictedPermission):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, state: PermissionState): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Copy(self) -> IPermission: ...
    
    def FromXml(self, securityElement: SecurityElement) -> VoidType: ...
    
    def Intersect(self, target: IPermission) -> IPermission: ...
    
    def IsSubsetOf(self, target: IPermission) -> BooleanType: ...
    
    def IsUnrestricted(self) -> BooleanType: ...
    
    def ToXml(self) -> SecurityElement: ...
    
    def Union(self, target: IPermission) -> IPermission: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DnsPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, action: SecurityAction): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def CreatePermission(self) -> IPermission: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DownloadDataCompletedEventArgs(AsyncCompletedEventArgs):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Result(self) -> ArrayType[ByteType]: ...
    
    # ---------- Methods ---------- #
    
    def get_Result(self) -> ArrayType[ByteType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DownloadDataCompletedEventHandler(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, sender: ObjectType, e: DownloadDataCompletedEventArgs, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, sender: ObjectType, e: DownloadDataCompletedEventArgs) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DownloadProgressChangedEventArgs(ProgressChangedEventArgs):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def BytesReceived(self) -> LongType: ...
    
    @property
    def TotalBytesToReceive(self) -> LongType: ...
    
    # ---------- Methods ---------- #
    
    def get_BytesReceived(self) -> LongType: ...
    
    def get_TotalBytesToReceive(self) -> LongType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DownloadProgressChangedEventHandler(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, sender: ObjectType, e: DownloadProgressChangedEventArgs, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, sender: ObjectType, e: DownloadProgressChangedEventArgs) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DownloadStringCompletedEventArgs(AsyncCompletedEventArgs):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Result(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_Result(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DownloadStringCompletedEventHandler(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, sender: ObjectType, e: DownloadStringCompletedEventArgs, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, sender: ObjectType, e: DownloadStringCompletedEventArgs) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EmptyWebProxy(ObjectType, IAutoWebProxy, IWebProxy):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Credentials(self) -> ICredentials: ...
    
    @Credentials.setter
    def Credentials(self, value: ICredentials) -> None: ...
    
    # ---------- Methods ---------- #
    
    def GetProxy(self, uri: Uri) -> Uri: ...
    
    def IsBypassed(self, uri: Uri) -> BooleanType: ...
    
    def get_Credentials(self) -> ICredentials: ...
    
    def set_Credentials(self, value: ICredentials) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EndPoint(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def AddressFamily(self) -> AddressFamily: ...
    
    # ---------- Methods ---------- #
    
    def Create(self, socketAddress: SocketAddress) -> EndPoint: ...
    
    def Serialize(self) -> SocketAddress: ...
    
    def get_AddressFamily(self) -> AddressFamily: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EndpointPermission(ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Hostname(self) -> StringType: ...
    
    @property
    def Port(self) -> IntType: ...
    
    @property
    def Transport(self) -> TransportType: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Hostname(self) -> StringType: ...
    
    def get_Port(self) -> IntType: ...
    
    def get_Transport(self) -> TransportType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ExceptionHelper(ABC, ObjectType):
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


class FileWebRequest(WebRequest, ISerializable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def ConnectionGroupName(self) -> StringType: ...
    
    @ConnectionGroupName.setter
    def ConnectionGroupName(self, value: StringType) -> None: ...
    
    @property
    def ContentLength(self) -> LongType: ...
    
    @ContentLength.setter
    def ContentLength(self, value: LongType) -> None: ...
    
    @property
    def ContentType(self) -> StringType: ...
    
    @ContentType.setter
    def ContentType(self, value: StringType) -> None: ...
    
    @property
    def Credentials(self) -> ICredentials: ...
    
    @Credentials.setter
    def Credentials(self, value: ICredentials) -> None: ...
    
    @property
    def Headers(self) -> WebHeaderCollection: ...
    
    @property
    def Method(self) -> StringType: ...
    
    @Method.setter
    def Method(self, value: StringType) -> None: ...
    
    @property
    def PreAuthenticate(self) -> BooleanType: ...
    
    @PreAuthenticate.setter
    def PreAuthenticate(self, value: BooleanType) -> None: ...
    
    @property
    def Proxy(self) -> IWebProxy: ...
    
    @Proxy.setter
    def Proxy(self, value: IWebProxy) -> None: ...
    
    @property
    def RequestUri(self) -> Uri: ...
    
    @property
    def Timeout(self) -> IntType: ...
    
    @Timeout.setter
    def Timeout(self, value: IntType) -> None: ...
    
    @property
    def UseDefaultCredentials(self) -> BooleanType: ...
    
    @UseDefaultCredentials.setter
    def UseDefaultCredentials(self, value: BooleanType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Abort(self) -> VoidType: ...
    
    def BeginGetRequestStream(self, callback: AsyncCallback, state: ObjectType) -> IAsyncResult: ...
    
    def BeginGetResponse(self, callback: AsyncCallback, state: ObjectType) -> IAsyncResult: ...
    
    def EndGetRequestStream(self, asyncResult: IAsyncResult) -> Stream: ...
    
    def EndGetResponse(self, asyncResult: IAsyncResult) -> WebResponse: ...
    
    def GetRequestStream(self) -> Stream: ...
    
    def GetResponse(self) -> WebResponse: ...
    
    def get_ConnectionGroupName(self) -> StringType: ...
    
    def get_ContentLength(self) -> LongType: ...
    
    def get_ContentType(self) -> StringType: ...
    
    def get_Credentials(self) -> ICredentials: ...
    
    def get_Headers(self) -> WebHeaderCollection: ...
    
    def get_Method(self) -> StringType: ...
    
    def get_PreAuthenticate(self) -> BooleanType: ...
    
    def get_Proxy(self) -> IWebProxy: ...
    
    def get_RequestUri(self) -> Uri: ...
    
    def get_Timeout(self) -> IntType: ...
    
    def get_UseDefaultCredentials(self) -> BooleanType: ...
    
    def set_ConnectionGroupName(self, value: StringType) -> VoidType: ...
    
    def set_ContentLength(self, value: LongType) -> VoidType: ...
    
    def set_ContentType(self, value: StringType) -> VoidType: ...
    
    def set_Credentials(self, value: ICredentials) -> VoidType: ...
    
    def set_Method(self, value: StringType) -> VoidType: ...
    
    def set_PreAuthenticate(self, value: BooleanType) -> VoidType: ...
    
    def set_Proxy(self, value: IWebProxy) -> VoidType: ...
    
    def set_Timeout(self, value: IntType) -> VoidType: ...
    
    def set_UseDefaultCredentials(self, value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class FileWebRequestCreator(ObjectType, IWebRequestCreate):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Create(self, uri: Uri) -> WebRequest: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class FileWebResponse(WebResponse, ISerializable, IDisposable, ICloseEx):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def ContentLength(self) -> LongType: ...
    
    @property
    def ContentType(self) -> StringType: ...
    
    @property
    def Headers(self) -> WebHeaderCollection: ...
    
    @property
    def ResponseUri(self) -> Uri: ...
    
    @property
    def SupportsHeaders(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    def GetResponseStream(self) -> Stream: ...
    
    def get_ContentLength(self) -> LongType: ...
    
    def get_ContentType(self) -> StringType: ...
    
    def get_Headers(self) -> WebHeaderCollection: ...
    
    def get_ResponseUri(self) -> Uri: ...
    
    def get_SupportsHeaders(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class FileWebStream(FileStream, IDisposable, ICloseEx):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, request: FileWebRequest, path: StringType, mode: FileMode, access: FileAccess, sharing: FileShare): ...
    
    @overload
    def __init__(self, request: FileWebRequest, path: StringType, mode: FileMode, access: FileAccess, sharing: FileShare, length: IntType, async: BooleanType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginRead(self, buffer: ArrayType[ByteType], offset: IntType, size: IntType, callback: AsyncCallback, state: ObjectType) -> IAsyncResult: ...
    
    def BeginWrite(self, buffer: ArrayType[ByteType], offset: IntType, size: IntType, callback: AsyncCallback, state: ObjectType) -> IAsyncResult: ...
    
    def EndRead(self, ar: IAsyncResult) -> IntType: ...
    
    def EndWrite(self, ar: IAsyncResult) -> VoidType: ...
    
    def Read(self, buffer: ArrayType[ByteType], offset: IntType, size: IntType) -> IntType: ...
    
    def Write(self, buffer: ArrayType[ByteType], offset: IntType, size: IntType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class FixedSizeReader(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, transport: Stream): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def AsyncReadPacket(self, request: AsyncProtocolRequest) -> VoidType: ...
    
    def ReadPacket(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class FrameHeader(ObjectType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def DefaultMajorV() -> IntType: ...
    
    @staticmethod
    @property
    def DefaultMinorV() -> IntType: ...
    
    @staticmethod
    @property
    def HandshakeDoneId() -> IntType: ...
    
    @staticmethod
    @property
    def HandshakeErrId() -> IntType: ...
    
    @staticmethod
    @property
    def HandshakeId() -> IntType: ...
    
    @staticmethod
    @property
    def IgnoreValue() -> IntType: ...
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, messageId: IntType, majorV: IntType, minorV: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def MajorV(self) -> IntType: ...
    
    @property
    def MaxMessageSize(self) -> IntType: ...
    
    @property
    def MessageId(self) -> IntType: ...
    
    @MessageId.setter
    def MessageId(self, value: IntType) -> None: ...
    
    @property
    def MinorV(self) -> IntType: ...
    
    @property
    def PayloadSize(self) -> IntType: ...
    
    @PayloadSize.setter
    def PayloadSize(self, value: IntType) -> None: ...
    
    @property
    def Size(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def CopyFrom(self, bytes: ArrayType[ByteType], start: IntType, verifier: FrameHeader) -> VoidType: ...
    
    def CopyTo(self, dest: ArrayType[ByteType], start: IntType) -> VoidType: ...
    
    def get_MajorV(self) -> IntType: ...
    
    def get_MaxMessageSize(self) -> IntType: ...
    
    def get_MessageId(self) -> IntType: ...
    
    def get_MinorV(self) -> IntType: ...
    
    def get_PayloadSize(self) -> IntType: ...
    
    def get_Size(self) -> IntType: ...
    
    def set_MessageId(self, value: IntType) -> VoidType: ...
    
    def set_PayloadSize(self, value: IntType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class FtpControlStream(CommandStream, IDisposable):
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


class FtpDataStream(Stream, IDisposable, ICloseEx):
    # No Fields
    
    # No Constructors
    
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
    def WriteTimeout(self) -> IntType: ...
    
    @WriteTimeout.setter
    def WriteTimeout(self, value: IntType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def BeginRead(self, buffer: ArrayType[ByteType], offset: IntType, size: IntType, callback: AsyncCallback, state: ObjectType) -> IAsyncResult: ...
    
    def BeginWrite(self, buffer: ArrayType[ByteType], offset: IntType, size: IntType, callback: AsyncCallback, state: ObjectType) -> IAsyncResult: ...
    
    def EndRead(self, ar: IAsyncResult) -> IntType: ...
    
    def EndWrite(self, asyncResult: IAsyncResult) -> VoidType: ...
    
    def Flush(self) -> VoidType: ...
    
    def Read(self, buffer: ArrayType[ByteType], offset: IntType, size: IntType) -> IntType: ...
    
    def Seek(self, offset: LongType, origin: SeekOrigin) -> LongType: ...
    
    def SetLength(self, value: LongType) -> VoidType: ...
    
    def Write(self, buffer: ArrayType[ByteType], offset: IntType, size: IntType) -> VoidType: ...
    
    def get_CanRead(self) -> BooleanType: ...
    
    def get_CanSeek(self) -> BooleanType: ...
    
    def get_CanTimeout(self) -> BooleanType: ...
    
    def get_CanWrite(self) -> BooleanType: ...
    
    def get_Length(self) -> LongType: ...
    
    def get_Position(self) -> LongType: ...
    
    def get_ReadTimeout(self) -> IntType: ...
    
    def get_WriteTimeout(self) -> IntType: ...
    
    def set_Position(self, value: LongType) -> VoidType: ...
    
    def set_ReadTimeout(self, value: IntType) -> VoidType: ...
    
    def set_WriteTimeout(self, value: IntType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class FtpMethodInfo(ObjectType):
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


class FtpWebRequest(WebRequest, ISerializable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def ClientCertificates(self) -> X509CertificateCollection: ...
    
    @ClientCertificates.setter
    def ClientCertificates(self, value: X509CertificateCollection) -> None: ...
    
    @property
    def ConnectionGroupName(self) -> StringType: ...
    
    @ConnectionGroupName.setter
    def ConnectionGroupName(self, value: StringType) -> None: ...
    
    @property
    def ContentLength(self) -> LongType: ...
    
    @ContentLength.setter
    def ContentLength(self, value: LongType) -> None: ...
    
    @property
    def ContentOffset(self) -> LongType: ...
    
    @ContentOffset.setter
    def ContentOffset(self, value: LongType) -> None: ...
    
    @property
    def ContentType(self) -> StringType: ...
    
    @ContentType.setter
    def ContentType(self, value: StringType) -> None: ...
    
    @property
    def Credentials(self) -> ICredentials: ...
    
    @Credentials.setter
    def Credentials(self, value: ICredentials) -> None: ...
    
    @staticmethod
    @property
    def DefaultCachePolicy() -> RequestCachePolicy: ...
    
    @staticmethod
    @DefaultCachePolicy.setter
    def DefaultCachePolicy(value: RequestCachePolicy) -> None: ...
    
    @property
    def EnableSsl(self) -> BooleanType: ...
    
    @EnableSsl.setter
    def EnableSsl(self, value: BooleanType) -> None: ...
    
    @property
    def Headers(self) -> WebHeaderCollection: ...
    
    @Headers.setter
    def Headers(self, value: WebHeaderCollection) -> None: ...
    
    @property
    def KeepAlive(self) -> BooleanType: ...
    
    @KeepAlive.setter
    def KeepAlive(self, value: BooleanType) -> None: ...
    
    @property
    def Method(self) -> StringType: ...
    
    @Method.setter
    def Method(self, value: StringType) -> None: ...
    
    @property
    def PreAuthenticate(self) -> BooleanType: ...
    
    @PreAuthenticate.setter
    def PreAuthenticate(self, value: BooleanType) -> None: ...
    
    @property
    def Proxy(self) -> IWebProxy: ...
    
    @Proxy.setter
    def Proxy(self, value: IWebProxy) -> None: ...
    
    @property
    def ReadWriteTimeout(self) -> IntType: ...
    
    @ReadWriteTimeout.setter
    def ReadWriteTimeout(self, value: IntType) -> None: ...
    
    @property
    def RenameTo(self) -> StringType: ...
    
    @RenameTo.setter
    def RenameTo(self, value: StringType) -> None: ...
    
    @property
    def RequestUri(self) -> Uri: ...
    
    @property
    def ServicePoint(self) -> ServicePoint: ...
    
    @property
    def Timeout(self) -> IntType: ...
    
    @Timeout.setter
    def Timeout(self, value: IntType) -> None: ...
    
    @property
    def UseBinary(self) -> BooleanType: ...
    
    @UseBinary.setter
    def UseBinary(self, value: BooleanType) -> None: ...
    
    @property
    def UseDefaultCredentials(self) -> BooleanType: ...
    
    @UseDefaultCredentials.setter
    def UseDefaultCredentials(self, value: BooleanType) -> None: ...
    
    @property
    def UsePassive(self) -> BooleanType: ...
    
    @UsePassive.setter
    def UsePassive(self, value: BooleanType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Abort(self) -> VoidType: ...
    
    def BeginGetRequestStream(self, callback: AsyncCallback, state: ObjectType) -> IAsyncResult: ...
    
    def BeginGetResponse(self, callback: AsyncCallback, state: ObjectType) -> IAsyncResult: ...
    
    def EndGetRequestStream(self, asyncResult: IAsyncResult) -> Stream: ...
    
    def EndGetResponse(self, asyncResult: IAsyncResult) -> WebResponse: ...
    
    def GetRequestStream(self) -> Stream: ...
    
    def GetResponse(self) -> WebResponse: ...
    
    def get_ClientCertificates(self) -> X509CertificateCollection: ...
    
    def get_ConnectionGroupName(self) -> StringType: ...
    
    def get_ContentLength(self) -> LongType: ...
    
    def get_ContentOffset(self) -> LongType: ...
    
    def get_ContentType(self) -> StringType: ...
    
    def get_Credentials(self) -> ICredentials: ...
    
    @staticmethod
    def get_DefaultCachePolicy() -> RequestCachePolicy: ...
    
    def get_EnableSsl(self) -> BooleanType: ...
    
    def get_Headers(self) -> WebHeaderCollection: ...
    
    def get_KeepAlive(self) -> BooleanType: ...
    
    def get_Method(self) -> StringType: ...
    
    def get_PreAuthenticate(self) -> BooleanType: ...
    
    def get_Proxy(self) -> IWebProxy: ...
    
    def get_ReadWriteTimeout(self) -> IntType: ...
    
    def get_RenameTo(self) -> StringType: ...
    
    def get_RequestUri(self) -> Uri: ...
    
    def get_ServicePoint(self) -> ServicePoint: ...
    
    def get_Timeout(self) -> IntType: ...
    
    def get_UseBinary(self) -> BooleanType: ...
    
    def get_UseDefaultCredentials(self) -> BooleanType: ...
    
    def get_UsePassive(self) -> BooleanType: ...
    
    def set_ClientCertificates(self, value: X509CertificateCollection) -> VoidType: ...
    
    def set_ConnectionGroupName(self, value: StringType) -> VoidType: ...
    
    def set_ContentLength(self, value: LongType) -> VoidType: ...
    
    def set_ContentOffset(self, value: LongType) -> VoidType: ...
    
    def set_ContentType(self, value: StringType) -> VoidType: ...
    
    def set_Credentials(self, value: ICredentials) -> VoidType: ...
    
    @staticmethod
    def set_DefaultCachePolicy(value: RequestCachePolicy) -> VoidType: ...
    
    def set_EnableSsl(self, value: BooleanType) -> VoidType: ...
    
    def set_Headers(self, value: WebHeaderCollection) -> VoidType: ...
    
    def set_KeepAlive(self, value: BooleanType) -> VoidType: ...
    
    def set_Method(self, value: StringType) -> VoidType: ...
    
    def set_PreAuthenticate(self, value: BooleanType) -> VoidType: ...
    
    def set_Proxy(self, value: IWebProxy) -> VoidType: ...
    
    def set_ReadWriteTimeout(self, value: IntType) -> VoidType: ...
    
    def set_RenameTo(self, value: StringType) -> VoidType: ...
    
    def set_Timeout(self, value: IntType) -> VoidType: ...
    
    def set_UseBinary(self, value: BooleanType) -> VoidType: ...
    
    def set_UseDefaultCredentials(self, value: BooleanType) -> VoidType: ...
    
    def set_UsePassive(self, value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class FtpWebRequestCreator(ObjectType, IWebRequestCreate):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Create(self, uri: Uri) -> WebRequest: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class FtpWebResponse(WebResponse, ISerializable, IDisposable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def BannerMessage(self) -> StringType: ...
    
    @property
    def ContentLength(self) -> LongType: ...
    
    @property
    def ExitMessage(self) -> StringType: ...
    
    @property
    def Headers(self) -> WebHeaderCollection: ...
    
    @property
    def LastModified(self) -> DateTime: ...
    
    @property
    def ResponseUri(self) -> Uri: ...
    
    @property
    def StatusCode(self) -> FtpStatusCode: ...
    
    @property
    def StatusDescription(self) -> StringType: ...
    
    @property
    def SupportsHeaders(self) -> BooleanType: ...
    
    @property
    def WelcomeMessage(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    def GetResponseStream(self) -> Stream: ...
    
    def get_BannerMessage(self) -> StringType: ...
    
    def get_ContentLength(self) -> LongType: ...
    
    def get_ExitMessage(self) -> StringType: ...
    
    def get_Headers(self) -> WebHeaderCollection: ...
    
    def get_LastModified(self) -> DateTime: ...
    
    def get_ResponseUri(self) -> Uri: ...
    
    def get_StatusCode(self) -> FtpStatusCode: ...
    
    def get_StatusDescription(self) -> StringType: ...
    
    def get_SupportsHeaders(self) -> BooleanType: ...
    
    def get_WelcomeMessage(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class GZipWrapperStream(GZipStream, IDisposable, ICloseEx, IRequestLifetimeTracker):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, stream: Stream, mode: CompressionMode): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginRead(self, buffer: ArrayType[ByteType], offset: IntType, size: IntType, callback: AsyncCallback, state: ObjectType) -> IAsyncResult: ...
    
    def EndRead(self, asyncResult: IAsyncResult) -> IntType: ...
    
    def Read(self, buffer: ArrayType[ByteType], offset: IntType, size: IntType) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class GeneralAsyncDelegate(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, request: ObjectType, state: ObjectType, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, request: ObjectType, state: ObjectType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class GlobalLog(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def AddToArray(msg: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Assert(condition: BooleanType, messageFormat: StringType, data: ArrayType[ObjectType]) -> VoidType: ...
    
    @staticmethod
    @overload
    def Assert(message: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Assert(message: StringType, detailMessage: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Dump(buffer: ArrayType[ByteType]) -> VoidType: ...
    
    @staticmethod
    @overload
    def Dump(buffer: ArrayType[ByteType], length: IntType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Dump(buffer: ArrayType[ByteType], offset: IntType, length: IntType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Dump(buffer: NIntType, offset: IntType, length: IntType) -> VoidType: ...
    
    @staticmethod
    def DumpArray() -> VoidType: ...
    
    @staticmethod
    @overload
    def Enter(func: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Enter(func: StringType, parms: StringType) -> VoidType: ...
    
    @staticmethod
    def Ignore(msg: ObjectType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Leave(func: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Leave(func: StringType, result: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Leave(func: StringType, returnval: IntType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Leave(func: StringType, returnval: BooleanType) -> VoidType: ...
    
    @staticmethod
    def LeaveException(func: StringType, exception: Exception) -> VoidType: ...
    
    @staticmethod
    def Print(msg: StringType) -> VoidType: ...
    
    @staticmethod
    def PrintHex(msg: StringType, value: ObjectType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class GlobalProxySelection(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def Select() -> IWebProxy: ...
    
    @staticmethod
    @Select.setter
    def Select(value: IWebProxy) -> None: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def GetEmptyWebProxy() -> IWebProxy: ...
    
    @staticmethod
    def get_Select() -> IWebProxy: ...
    
    @staticmethod
    def set_Select(value: IWebProxy) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class GlobalSSPI(ABC, ObjectType):
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


class HeaderInfo(ObjectType):
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


class HeaderInfoTable(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class HeaderParser(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, value: StringType, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> ArrayType[StringType]: ...
    
    def Invoke(self, value: StringType) -> ArrayType[StringType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class HostHeaderString(ObjectType):
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


class HttpAbortDelegate(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, request: HttpWebRequest, webException: WebException, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> BooleanType: ...
    
    def Invoke(self, request: HttpWebRequest, webException: WebException) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class HttpContinueDelegate(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, StatusCode: IntType, httpHeaders: WebHeaderCollection, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, StatusCode: IntType, httpHeaders: WebHeaderCollection) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class HttpDateParse(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def ParseHttpDate(DateString: StringType, dtOut: DateTime) -> Tuple[BooleanType, DateTime]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class HttpDigest(ABC, ObjectType):
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


class HttpDigestChallenge(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def defineAttribute(self, name: StringType, value: StringType) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class HttpKnownHeaderNames(ABC, ObjectType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Accept() -> StringType: ...
    
    @staticmethod
    @property
    def AcceptCharset() -> StringType: ...
    
    @staticmethod
    @property
    def AcceptEncoding() -> StringType: ...
    
    @staticmethod
    @property
    def AcceptLanguage() -> StringType: ...
    
    @staticmethod
    @property
    def AcceptRanges() -> StringType: ...
    
    @staticmethod
    @property
    def Age() -> StringType: ...
    
    @staticmethod
    @property
    def Allow() -> StringType: ...
    
    @staticmethod
    @property
    def Authorization() -> StringType: ...
    
    @staticmethod
    @property
    def CacheControl() -> StringType: ...
    
    @staticmethod
    @property
    def Connection() -> StringType: ...
    
    @staticmethod
    @property
    def ContentDisposition() -> StringType: ...
    
    @staticmethod
    @property
    def ContentEncoding() -> StringType: ...
    
    @staticmethod
    @property
    def ContentLanguage() -> StringType: ...
    
    @staticmethod
    @property
    def ContentLength() -> StringType: ...
    
    @staticmethod
    @property
    def ContentLocation() -> StringType: ...
    
    @staticmethod
    @property
    def ContentMD5() -> StringType: ...
    
    @staticmethod
    @property
    def ContentRange() -> StringType: ...
    
    @staticmethod
    @property
    def ContentType() -> StringType: ...
    
    @staticmethod
    @property
    def Cookie() -> StringType: ...
    
    @staticmethod
    @property
    def Cookie2() -> StringType: ...
    
    @staticmethod
    @property
    def Date() -> StringType: ...
    
    @staticmethod
    @property
    def ETag() -> StringType: ...
    
    @staticmethod
    @property
    def Expect() -> StringType: ...
    
    @staticmethod
    @property
    def Expires() -> StringType: ...
    
    @staticmethod
    @property
    def From() -> StringType: ...
    
    @staticmethod
    @property
    def Host() -> StringType: ...
    
    @staticmethod
    @property
    def IfMatch() -> StringType: ...
    
    @staticmethod
    @property
    def IfModifiedSince() -> StringType: ...
    
    @staticmethod
    @property
    def IfNoneMatch() -> StringType: ...
    
    @staticmethod
    @property
    def IfRange() -> StringType: ...
    
    @staticmethod
    @property
    def IfUnmodifiedSince() -> StringType: ...
    
    @staticmethod
    @property
    def KeepAlive() -> StringType: ...
    
    @staticmethod
    @property
    def LastModified() -> StringType: ...
    
    @staticmethod
    @property
    def Location() -> StringType: ...
    
    @staticmethod
    @property
    def MaxForwards() -> StringType: ...
    
    @staticmethod
    @property
    def Origin() -> StringType: ...
    
    @staticmethod
    @property
    def P3P() -> StringType: ...
    
    @staticmethod
    @property
    def Pragma() -> StringType: ...
    
    @staticmethod
    @property
    def ProxyAuthenticate() -> StringType: ...
    
    @staticmethod
    @property
    def ProxyAuthorization() -> StringType: ...
    
    @staticmethod
    @property
    def ProxyConnection() -> StringType: ...
    
    @staticmethod
    @property
    def Range() -> StringType: ...
    
    @staticmethod
    @property
    def Referer() -> StringType: ...
    
    @staticmethod
    @property
    def RetryAfter() -> StringType: ...
    
    @staticmethod
    @property
    def SecWebSocketAccept() -> StringType: ...
    
    @staticmethod
    @property
    def SecWebSocketExtensions() -> StringType: ...
    
    @staticmethod
    @property
    def SecWebSocketKey() -> StringType: ...
    
    @staticmethod
    @property
    def SecWebSocketProtocol() -> StringType: ...
    
    @staticmethod
    @property
    def SecWebSocketVersion() -> StringType: ...
    
    @staticmethod
    @property
    def Server() -> StringType: ...
    
    @staticmethod
    @property
    def SetCookie() -> StringType: ...
    
    @staticmethod
    @property
    def SetCookie2() -> StringType: ...
    
    @staticmethod
    @property
    def TE() -> StringType: ...
    
    @staticmethod
    @property
    def Trailer() -> StringType: ...
    
    @staticmethod
    @property
    def TransferEncoding() -> StringType: ...
    
    @staticmethod
    @property
    def Upgrade() -> StringType: ...
    
    @staticmethod
    @property
    def UserAgent() -> StringType: ...
    
    @staticmethod
    @property
    def Vary() -> StringType: ...
    
    @staticmethod
    @property
    def Via() -> StringType: ...
    
    @staticmethod
    @property
    def WWWAuthenticate() -> StringType: ...
    
    @staticmethod
    @property
    def Warning() -> StringType: ...
    
    @staticmethod
    @property
    def XAspNetVersion() -> StringType: ...
    
    @staticmethod
    @property
    def XPoweredBy() -> StringType: ...
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class HttpListener(ObjectType, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AuthenticationSchemeSelectorDelegate(self) -> AuthenticationSchemeSelector: ...
    
    @AuthenticationSchemeSelectorDelegate.setter
    def AuthenticationSchemeSelectorDelegate(self, value: AuthenticationSchemeSelector) -> None: ...
    
    @property
    def AuthenticationSchemes(self) -> AuthenticationSchemes: ...
    
    @AuthenticationSchemes.setter
    def AuthenticationSchemes(self, value: AuthenticationSchemes) -> None: ...
    
    @property
    def DefaultServiceNames(self) -> ServiceNameCollection: ...
    
    @property
    def ExtendedProtectionPolicy(self) -> ExtendedProtectionPolicy: ...
    
    @ExtendedProtectionPolicy.setter
    def ExtendedProtectionPolicy(self, value: ExtendedProtectionPolicy) -> None: ...
    
    @property
    def ExtendedProtectionSelectorDelegate(self) -> ExtendedProtectionSelector: ...
    
    @ExtendedProtectionSelectorDelegate.setter
    def ExtendedProtectionSelectorDelegate(self, value: ExtendedProtectionSelector) -> None: ...
    
    @property
    def IgnoreWriteExceptions(self) -> BooleanType: ...
    
    @IgnoreWriteExceptions.setter
    def IgnoreWriteExceptions(self, value: BooleanType) -> None: ...
    
    @property
    def IsListening(self) -> BooleanType: ...
    
    @staticmethod
    @property
    def IsSupported() -> BooleanType: ...
    
    @property
    def Prefixes(self) -> HttpListenerPrefixCollection: ...
    
    @property
    def Realm(self) -> StringType: ...
    
    @Realm.setter
    def Realm(self, value: StringType) -> None: ...
    
    @property
    def TimeoutManager(self) -> HttpListenerTimeoutManager: ...
    
    @property
    def UnsafeConnectionNtlmAuthentication(self) -> BooleanType: ...
    
    @UnsafeConnectionNtlmAuthentication.setter
    def UnsafeConnectionNtlmAuthentication(self, value: BooleanType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Abort(self) -> VoidType: ...
    
    def BeginGetContext(self, callback: AsyncCallback, state: ObjectType) -> IAsyncResult: ...
    
    def Close(self) -> VoidType: ...
    
    def EndGetContext(self, asyncResult: IAsyncResult) -> HttpListenerContext: ...
    
    def GetContext(self) -> HttpListenerContext: ...
    
    def GetContextAsync(self) -> Task[HttpListenerContext]: ...
    
    def Start(self) -> VoidType: ...
    
    def Stop(self) -> VoidType: ...
    
    def get_AuthenticationSchemeSelectorDelegate(self) -> AuthenticationSchemeSelector: ...
    
    def get_AuthenticationSchemes(self) -> AuthenticationSchemes: ...
    
    def get_DefaultServiceNames(self) -> ServiceNameCollection: ...
    
    def get_ExtendedProtectionPolicy(self) -> ExtendedProtectionPolicy: ...
    
    def get_ExtendedProtectionSelectorDelegate(self) -> ExtendedProtectionSelector: ...
    
    def get_IgnoreWriteExceptions(self) -> BooleanType: ...
    
    def get_IsListening(self) -> BooleanType: ...
    
    @staticmethod
    def get_IsSupported() -> BooleanType: ...
    
    def get_Prefixes(self) -> HttpListenerPrefixCollection: ...
    
    def get_Realm(self) -> StringType: ...
    
    def get_TimeoutManager(self) -> HttpListenerTimeoutManager: ...
    
    def get_UnsafeConnectionNtlmAuthentication(self) -> BooleanType: ...
    
    def set_AuthenticationSchemeSelectorDelegate(self, value: AuthenticationSchemeSelector) -> VoidType: ...
    
    def set_AuthenticationSchemes(self, value: AuthenticationSchemes) -> VoidType: ...
    
    def set_ExtendedProtectionPolicy(self, value: ExtendedProtectionPolicy) -> VoidType: ...
    
    def set_ExtendedProtectionSelectorDelegate(self, value: ExtendedProtectionSelector) -> VoidType: ...
    
    def set_IgnoreWriteExceptions(self, value: BooleanType) -> VoidType: ...
    
    def set_Realm(self, value: StringType) -> VoidType: ...
    
    def set_UnsafeConnectionNtlmAuthentication(self, value: BooleanType) -> VoidType: ...
    
    # No Events
    
    
    # ---------- Sub Classes ---------- #
    
    class ExtendedProtectionSelector(MulticastDelegate, ICloneable, ISerializable):
        # No Fields
        
        # ---------- Constructors ---------- #
        
        def __init__(self, object: ObjectType, method: NIntType): ...
        
        # No Properties
        
        # ---------- Methods ---------- #
        
        def BeginInvoke(self, request: HttpListenerRequest, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
        
        def EndInvoke(self, result: IAsyncResult) -> ExtendedProtectionPolicy: ...
        
        def Invoke(self, request: HttpListenerRequest) -> ExtendedProtectionPolicy: ...
        
        # No Events
        
        # No Sub Classes
        
        # No Sub Structs
        
        # No Sub Interfaces
        
        # No Sub Enums
    
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class HttpListenerBasicIdentity(GenericIdentity, IIdentity):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, username: StringType, password: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Password(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_Password(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class HttpListenerContext(ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Request(self) -> HttpListenerRequest: ...
    
    @property
    def Response(self) -> HttpListenerResponse: ...
    
    @property
    def User(self) -> IPrincipal: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def AcceptWebSocketAsync(self, subProtocol: StringType) -> Task[HttpListenerWebSocketContext]: ...
    
    @overload
    def AcceptWebSocketAsync(self, subProtocol: StringType, keepAliveInterval: TimeSpan) -> Task[HttpListenerWebSocketContext]: ...
    
    @overload
    def AcceptWebSocketAsync(self, subProtocol: StringType, receiveBufferSize: IntType, keepAliveInterval: TimeSpan) -> Task[HttpListenerWebSocketContext]: ...
    
    @overload
    def AcceptWebSocketAsync(self, subProtocol: StringType, receiveBufferSize: IntType, keepAliveInterval: TimeSpan, internalBuffer: ArraySegment[ByteType]) -> Task[HttpListenerWebSocketContext]: ...
    
    def get_Request(self) -> HttpListenerRequest: ...
    
    def get_Response(self) -> HttpListenerResponse: ...
    
    def get_User(self) -> IPrincipal: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class HttpListenerException(Win32Exception, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, errorCode: IntType): ...
    
    @overload
    def __init__(self, errorCode: IntType, message: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ErrorCode(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def get_ErrorCode(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class HttpListenerPrefixCollection(ObjectType, ICollection[StringType], IEnumerable[StringType], IEnumerable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def IsReadOnly(self) -> BooleanType: ...
    
    @property
    def IsSynchronized(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, uriPrefix: StringType) -> VoidType: ...
    
    def Clear(self) -> VoidType: ...
    
    def Contains(self, uriPrefix: StringType) -> BooleanType: ...
    
    @overload
    def CopyTo(self, array: Array, offset: IntType) -> VoidType: ...
    
    @overload
    def CopyTo(self, array: ArrayType[StringType], offset: IntType) -> VoidType: ...
    
    def GetEnumerator(self) -> IEnumerator[StringType]: ...
    
    def Remove(self, uriPrefix: StringType) -> BooleanType: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_IsReadOnly(self) -> BooleanType: ...
    
    def get_IsSynchronized(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class HttpListenerRequest(ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def AcceptTypes(self) -> ArrayType[StringType]: ...
    
    @property
    def ClientCertificateError(self) -> IntType: ...
    
    @property
    def ContentEncoding(self) -> Encoding: ...
    
    @property
    def ContentLength64(self) -> LongType: ...
    
    @property
    def ContentType(self) -> StringType: ...
    
    @property
    def Cookies(self) -> CookieCollection: ...
    
    @property
    def HasEntityBody(self) -> BooleanType: ...
    
    @property
    def Headers(self) -> NameValueCollection: ...
    
    @property
    def HttpMethod(self) -> StringType: ...
    
    @property
    def InputStream(self) -> Stream: ...
    
    @property
    def IsAuthenticated(self) -> BooleanType: ...
    
    @property
    def IsLocal(self) -> BooleanType: ...
    
    @property
    def IsSecureConnection(self) -> BooleanType: ...
    
    @property
    def IsWebSocketRequest(self) -> BooleanType: ...
    
    @property
    def KeepAlive(self) -> BooleanType: ...
    
    @property
    def LocalEndPoint(self) -> IPEndPoint: ...
    
    @property
    def ProtocolVersion(self) -> Version: ...
    
    @property
    def QueryString(self) -> NameValueCollection: ...
    
    @property
    def RawUrl(self) -> StringType: ...
    
    @property
    def RemoteEndPoint(self) -> IPEndPoint: ...
    
    @property
    def RequestTraceIdentifier(self) -> Guid: ...
    
    @property
    def ServiceName(self) -> StringType: ...
    
    @property
    def TransportContext(self) -> TransportContext: ...
    
    @property
    def Url(self) -> Uri: ...
    
    @property
    def UrlReferrer(self) -> Uri: ...
    
    @property
    def UserAgent(self) -> StringType: ...
    
    @property
    def UserHostAddress(self) -> StringType: ...
    
    @property
    def UserHostName(self) -> StringType: ...
    
    @property
    def UserLanguages(self) -> ArrayType[StringType]: ...
    
    # ---------- Methods ---------- #
    
    def BeginGetClientCertificate(self, requestCallback: AsyncCallback, state: ObjectType) -> IAsyncResult: ...
    
    def EndGetClientCertificate(self, asyncResult: IAsyncResult) -> X509Certificate2: ...
    
    def GetClientCertificate(self) -> X509Certificate2: ...
    
    def GetClientCertificateAsync(self) -> Task[X509Certificate2]: ...
    
    def get_AcceptTypes(self) -> ArrayType[StringType]: ...
    
    def get_ClientCertificateError(self) -> IntType: ...
    
    def get_ContentEncoding(self) -> Encoding: ...
    
    def get_ContentLength64(self) -> LongType: ...
    
    def get_ContentType(self) -> StringType: ...
    
    def get_Cookies(self) -> CookieCollection: ...
    
    def get_HasEntityBody(self) -> BooleanType: ...
    
    def get_Headers(self) -> NameValueCollection: ...
    
    def get_HttpMethod(self) -> StringType: ...
    
    def get_InputStream(self) -> Stream: ...
    
    def get_IsAuthenticated(self) -> BooleanType: ...
    
    def get_IsLocal(self) -> BooleanType: ...
    
    def get_IsSecureConnection(self) -> BooleanType: ...
    
    def get_IsWebSocketRequest(self) -> BooleanType: ...
    
    def get_KeepAlive(self) -> BooleanType: ...
    
    def get_LocalEndPoint(self) -> IPEndPoint: ...
    
    def get_ProtocolVersion(self) -> Version: ...
    
    def get_QueryString(self) -> NameValueCollection: ...
    
    def get_RawUrl(self) -> StringType: ...
    
    def get_RemoteEndPoint(self) -> IPEndPoint: ...
    
    def get_RequestTraceIdentifier(self) -> Guid: ...
    
    def get_ServiceName(self) -> StringType: ...
    
    def get_TransportContext(self) -> TransportContext: ...
    
    def get_Url(self) -> Uri: ...
    
    def get_UrlReferrer(self) -> Uri: ...
    
    def get_UserAgent(self) -> StringType: ...
    
    def get_UserHostAddress(self) -> StringType: ...
    
    def get_UserHostName(self) -> StringType: ...
    
    def get_UserLanguages(self) -> ArrayType[StringType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class HttpListenerRequestContext(TransportContext):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetChannelBinding(self, kind: ChannelBindingKind) -> ChannelBinding: ...
    
    def GetTlsTokenBindings(self) -> IEnumerable[TokenBinding]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class HttpListenerRequestUriBuilder(ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def GetRequestUri(rawUri: StringType, cookedUriScheme: StringType, cookedUriHost: StringType, cookedUriPath: StringType, cookedUriQuery: StringType) -> Uri: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class HttpListenerResponse(ObjectType, IDisposable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def ContentEncoding(self) -> Encoding: ...
    
    @ContentEncoding.setter
    def ContentEncoding(self, value: Encoding) -> None: ...
    
    @property
    def ContentLength64(self) -> LongType: ...
    
    @ContentLength64.setter
    def ContentLength64(self, value: LongType) -> None: ...
    
    @property
    def ContentType(self) -> StringType: ...
    
    @ContentType.setter
    def ContentType(self, value: StringType) -> None: ...
    
    @property
    def Cookies(self) -> CookieCollection: ...
    
    @Cookies.setter
    def Cookies(self, value: CookieCollection) -> None: ...
    
    @property
    def Headers(self) -> WebHeaderCollection: ...
    
    @Headers.setter
    def Headers(self, value: WebHeaderCollection) -> None: ...
    
    @property
    def KeepAlive(self) -> BooleanType: ...
    
    @KeepAlive.setter
    def KeepAlive(self, value: BooleanType) -> None: ...
    
    @property
    def OutputStream(self) -> Stream: ...
    
    @property
    def ProtocolVersion(self) -> Version: ...
    
    @ProtocolVersion.setter
    def ProtocolVersion(self, value: Version) -> None: ...
    
    @property
    def RedirectLocation(self) -> StringType: ...
    
    @RedirectLocation.setter
    def RedirectLocation(self, value: StringType) -> None: ...
    
    @property
    def SendChunked(self) -> BooleanType: ...
    
    @SendChunked.setter
    def SendChunked(self, value: BooleanType) -> None: ...
    
    @property
    def StatusCode(self) -> IntType: ...
    
    @StatusCode.setter
    def StatusCode(self, value: IntType) -> None: ...
    
    @property
    def StatusDescription(self) -> StringType: ...
    
    @StatusDescription.setter
    def StatusDescription(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Abort(self) -> VoidType: ...
    
    def AddHeader(self, name: StringType, value: StringType) -> VoidType: ...
    
    def AppendCookie(self, cookie: Cookie) -> VoidType: ...
    
    def AppendHeader(self, name: StringType, value: StringType) -> VoidType: ...
    
    @overload
    def Close(self, responseEntity: ArrayType[ByteType], willBlock: BooleanType) -> VoidType: ...
    
    @overload
    def Close(self) -> VoidType: ...
    
    def CopyFrom(self, templateResponse: HttpListenerResponse) -> VoidType: ...
    
    def Redirect(self, url: StringType) -> VoidType: ...
    
    def SetCookie(self, cookie: Cookie) -> VoidType: ...
    
    def get_ContentEncoding(self) -> Encoding: ...
    
    def get_ContentLength64(self) -> LongType: ...
    
    def get_ContentType(self) -> StringType: ...
    
    def get_Cookies(self) -> CookieCollection: ...
    
    def get_Headers(self) -> WebHeaderCollection: ...
    
    def get_KeepAlive(self) -> BooleanType: ...
    
    def get_OutputStream(self) -> Stream: ...
    
    def get_ProtocolVersion(self) -> Version: ...
    
    def get_RedirectLocation(self) -> StringType: ...
    
    def get_SendChunked(self) -> BooleanType: ...
    
    def get_StatusCode(self) -> IntType: ...
    
    def get_StatusDescription(self) -> StringType: ...
    
    def set_ContentEncoding(self, value: Encoding) -> VoidType: ...
    
    def set_ContentLength64(self, value: LongType) -> VoidType: ...
    
    def set_ContentType(self, value: StringType) -> VoidType: ...
    
    def set_Cookies(self, value: CookieCollection) -> VoidType: ...
    
    def set_Headers(self, value: WebHeaderCollection) -> VoidType: ...
    
    def set_KeepAlive(self, value: BooleanType) -> VoidType: ...
    
    def set_ProtocolVersion(self, value: Version) -> VoidType: ...
    
    def set_RedirectLocation(self, value: StringType) -> VoidType: ...
    
    def set_SendChunked(self, value: BooleanType) -> VoidType: ...
    
    def set_StatusCode(self, value: IntType) -> VoidType: ...
    
    def set_StatusDescription(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class HttpListenerTimeoutManager(ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def DrainEntityBody(self) -> TimeSpan: ...
    
    @DrainEntityBody.setter
    def DrainEntityBody(self, value: TimeSpan) -> None: ...
    
    @property
    def EntityBody(self) -> TimeSpan: ...
    
    @EntityBody.setter
    def EntityBody(self, value: TimeSpan) -> None: ...
    
    @property
    def HeaderWait(self) -> TimeSpan: ...
    
    @HeaderWait.setter
    def HeaderWait(self, value: TimeSpan) -> None: ...
    
    @property
    def IdleConnection(self) -> TimeSpan: ...
    
    @IdleConnection.setter
    def IdleConnection(self, value: TimeSpan) -> None: ...
    
    @property
    def MinSendBytesPerSecond(self) -> LongType: ...
    
    @MinSendBytesPerSecond.setter
    def MinSendBytesPerSecond(self, value: LongType) -> None: ...
    
    @property
    def RequestQueue(self) -> TimeSpan: ...
    
    @RequestQueue.setter
    def RequestQueue(self, value: TimeSpan) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_DrainEntityBody(self) -> TimeSpan: ...
    
    def get_EntityBody(self) -> TimeSpan: ...
    
    def get_HeaderWait(self) -> TimeSpan: ...
    
    def get_IdleConnection(self) -> TimeSpan: ...
    
    def get_MinSendBytesPerSecond(self) -> LongType: ...
    
    def get_RequestQueue(self) -> TimeSpan: ...
    
    def set_DrainEntityBody(self, value: TimeSpan) -> VoidType: ...
    
    def set_EntityBody(self, value: TimeSpan) -> VoidType: ...
    
    def set_HeaderWait(self, value: TimeSpan) -> VoidType: ...
    
    def set_IdleConnection(self, value: TimeSpan) -> VoidType: ...
    
    def set_MinSendBytesPerSecond(self, value: LongType) -> VoidType: ...
    
    def set_RequestQueue(self, value: TimeSpan) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class HttpProtocolUtils(ObjectType):
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


class HttpRequestCreator(ObjectType, IWebRequestCreate):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Create(self, Uri: Uri) -> WebRequest: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class HttpRequestQueueV2Handle(CriticalHandleZeroOrMinusOneIsInvalid, IDisposable):
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


class HttpRequestStream(Stream, IDisposable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def CanRead(self) -> BooleanType: ...
    
    @property
    def CanSeek(self) -> BooleanType: ...
    
    @property
    def CanWrite(self) -> BooleanType: ...
    
    @property
    def Length(self) -> LongType: ...
    
    @property
    def Position(self) -> LongType: ...
    
    @Position.setter
    def Position(self, value: LongType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def BeginRead(self, buffer: ArrayType[ByteType], offset: IntType, size: IntType, callback: AsyncCallback, state: ObjectType) -> IAsyncResult: ...
    
    def BeginWrite(self, buffer: ArrayType[ByteType], offset: IntType, size: IntType, callback: AsyncCallback, state: ObjectType) -> IAsyncResult: ...
    
    def EndRead(self, asyncResult: IAsyncResult) -> IntType: ...
    
    def EndWrite(self, asyncResult: IAsyncResult) -> VoidType: ...
    
    def Flush(self) -> VoidType: ...
    
    @overload
    def FlushAsync(self, cancellationToken: CancellationToken) -> Task: ...
    
    def Read(self, buffer: ArrayType[ByteType], offset: IntType, size: IntType) -> Tuple[IntType, ArrayType[ByteType]]: ...
    
    def Seek(self, offset: LongType, origin: SeekOrigin) -> LongType: ...
    
    def SetLength(self, value: LongType) -> VoidType: ...
    
    def Write(self, buffer: ArrayType[ByteType], offset: IntType, size: IntType) -> VoidType: ...
    
    def get_CanRead(self) -> BooleanType: ...
    
    def get_CanSeek(self) -> BooleanType: ...
    
    def get_CanWrite(self) -> BooleanType: ...
    
    def get_Length(self) -> LongType: ...
    
    def get_Position(self) -> LongType: ...
    
    def set_Position(self, value: LongType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class HttpResponseStream(Stream, IDisposable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def CanRead(self) -> BooleanType: ...
    
    @property
    def CanSeek(self) -> BooleanType: ...
    
    @property
    def CanWrite(self) -> BooleanType: ...
    
    @property
    def Length(self) -> LongType: ...
    
    @property
    def Position(self) -> LongType: ...
    
    @Position.setter
    def Position(self, value: LongType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def BeginRead(self, buffer: ArrayType[ByteType], offset: IntType, size: IntType, callback: AsyncCallback, state: ObjectType) -> IAsyncResult: ...
    
    def BeginWrite(self, buffer: ArrayType[ByteType], offset: IntType, size: IntType, callback: AsyncCallback, state: ObjectType) -> IAsyncResult: ...
    
    def EndRead(self, asyncResult: IAsyncResult) -> IntType: ...
    
    def EndWrite(self, asyncResult: IAsyncResult) -> VoidType: ...
    
    def Flush(self) -> VoidType: ...
    
    @overload
    def FlushAsync(self, cancellationToken: CancellationToken) -> Task: ...
    
    def Read(self, buffer: ArrayType[ByteType], offset: IntType, size: IntType) -> Tuple[IntType, ArrayType[ByteType]]: ...
    
    def Seek(self, offset: LongType, origin: SeekOrigin) -> LongType: ...
    
    def SetLength(self, value: LongType) -> VoidType: ...
    
    def Write(self, buffer: ArrayType[ByteType], offset: IntType, size: IntType) -> VoidType: ...
    
    def get_CanRead(self) -> BooleanType: ...
    
    def get_CanSeek(self) -> BooleanType: ...
    
    def get_CanWrite(self) -> BooleanType: ...
    
    def get_Length(self) -> LongType: ...
    
    def get_Position(self) -> LongType: ...
    
    def set_Position(self, value: LongType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class HttpResponseStreamAsyncResult(LazyAsyncResult, IAsyncResult):
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


class HttpServerSessionHandle(CriticalHandleZeroOrMinusOneIsInvalid, IDisposable):
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


class HttpStatusDescription(ABC, ObjectType):
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


class HttpSysSettings(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def EnableNonUtf8() -> BooleanType: ...
    
    @staticmethod
    @property
    def FavorUtf8() -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def get_EnableNonUtf8() -> BooleanType: ...
    
    @staticmethod
    def get_FavorUtf8() -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class HttpVersion(ObjectType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Version10() -> Version: ...
    
    @staticmethod
    @property
    def Version11() -> Version: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class HttpWebRequest(WebRequest, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Accept(self) -> StringType: ...
    
    @Accept.setter
    def Accept(self, value: StringType) -> None: ...
    
    @property
    def Address(self) -> Uri: ...
    
    @property
    def AllowAutoRedirect(self) -> BooleanType: ...
    
    @AllowAutoRedirect.setter
    def AllowAutoRedirect(self, value: BooleanType) -> None: ...
    
    @property
    def AllowReadStreamBuffering(self) -> BooleanType: ...
    
    @AllowReadStreamBuffering.setter
    def AllowReadStreamBuffering(self, value: BooleanType) -> None: ...
    
    @property
    def AllowWriteStreamBuffering(self) -> BooleanType: ...
    
    @AllowWriteStreamBuffering.setter
    def AllowWriteStreamBuffering(self, value: BooleanType) -> None: ...
    
    @property
    def AutomaticDecompression(self) -> DecompressionMethods: ...
    
    @AutomaticDecompression.setter
    def AutomaticDecompression(self, value: DecompressionMethods) -> None: ...
    
    @property
    def ClientCertificates(self) -> X509CertificateCollection: ...
    
    @ClientCertificates.setter
    def ClientCertificates(self, value: X509CertificateCollection) -> None: ...
    
    @property
    def Connection(self) -> StringType: ...
    
    @Connection.setter
    def Connection(self, value: StringType) -> None: ...
    
    @property
    def ConnectionGroupName(self) -> StringType: ...
    
    @ConnectionGroupName.setter
    def ConnectionGroupName(self, value: StringType) -> None: ...
    
    @property
    def ContentLength(self) -> LongType: ...
    
    @ContentLength.setter
    def ContentLength(self, value: LongType) -> None: ...
    
    @property
    def ContentType(self) -> StringType: ...
    
    @ContentType.setter
    def ContentType(self, value: StringType) -> None: ...
    
    @property
    def ContinueDelegate(self) -> HttpContinueDelegate: ...
    
    @ContinueDelegate.setter
    def ContinueDelegate(self, value: HttpContinueDelegate) -> None: ...
    
    @property
    def ContinueTimeout(self) -> IntType: ...
    
    @ContinueTimeout.setter
    def ContinueTimeout(self, value: IntType) -> None: ...
    
    @property
    def CookieContainer(self) -> CookieContainer: ...
    
    @CookieContainer.setter
    def CookieContainer(self, value: CookieContainer) -> None: ...
    
    @property
    def Credentials(self) -> ICredentials: ...
    
    @Credentials.setter
    def Credentials(self, value: ICredentials) -> None: ...
    
    @property
    def Date(self) -> DateTime: ...
    
    @Date.setter
    def Date(self, value: DateTime) -> None: ...
    
    @staticmethod
    @property
    def DefaultCachePolicy() -> RequestCachePolicy: ...
    
    @staticmethod
    @DefaultCachePolicy.setter
    def DefaultCachePolicy(value: RequestCachePolicy) -> None: ...
    
    @staticmethod
    @property
    def DefaultMaximumErrorResponseLength() -> IntType: ...
    
    @staticmethod
    @DefaultMaximumErrorResponseLength.setter
    def DefaultMaximumErrorResponseLength(value: IntType) -> None: ...
    
    @staticmethod
    @property
    def DefaultMaximumResponseHeadersLength() -> IntType: ...
    
    @staticmethod
    @DefaultMaximumResponseHeadersLength.setter
    def DefaultMaximumResponseHeadersLength(value: IntType) -> None: ...
    
    @property
    def Expect(self) -> StringType: ...
    
    @Expect.setter
    def Expect(self, value: StringType) -> None: ...
    
    @property
    def HaveResponse(self) -> BooleanType: ...
    
    @property
    def Headers(self) -> WebHeaderCollection: ...
    
    @Headers.setter
    def Headers(self, value: WebHeaderCollection) -> None: ...
    
    @property
    def Host(self) -> StringType: ...
    
    @Host.setter
    def Host(self, value: StringType) -> None: ...
    
    @property
    def IfModifiedSince(self) -> DateTime: ...
    
    @IfModifiedSince.setter
    def IfModifiedSince(self, value: DateTime) -> None: ...
    
    @property
    def KeepAlive(self) -> BooleanType: ...
    
    @KeepAlive.setter
    def KeepAlive(self, value: BooleanType) -> None: ...
    
    @property
    def MaximumAutomaticRedirections(self) -> IntType: ...
    
    @MaximumAutomaticRedirections.setter
    def MaximumAutomaticRedirections(self, value: IntType) -> None: ...
    
    @property
    def MaximumResponseHeadersLength(self) -> IntType: ...
    
    @MaximumResponseHeadersLength.setter
    def MaximumResponseHeadersLength(self, value: IntType) -> None: ...
    
    @property
    def MediaType(self) -> StringType: ...
    
    @MediaType.setter
    def MediaType(self, value: StringType) -> None: ...
    
    @property
    def Method(self) -> StringType: ...
    
    @Method.setter
    def Method(self, value: StringType) -> None: ...
    
    @property
    def Pipelined(self) -> BooleanType: ...
    
    @Pipelined.setter
    def Pipelined(self, value: BooleanType) -> None: ...
    
    @property
    def PreAuthenticate(self) -> BooleanType: ...
    
    @PreAuthenticate.setter
    def PreAuthenticate(self, value: BooleanType) -> None: ...
    
    @property
    def ProtocolVersion(self) -> Version: ...
    
    @ProtocolVersion.setter
    def ProtocolVersion(self, value: Version) -> None: ...
    
    @property
    def Proxy(self) -> IWebProxy: ...
    
    @Proxy.setter
    def Proxy(self, value: IWebProxy) -> None: ...
    
    @property
    def ReadWriteTimeout(self) -> IntType: ...
    
    @ReadWriteTimeout.setter
    def ReadWriteTimeout(self, value: IntType) -> None: ...
    
    @property
    def Referer(self) -> StringType: ...
    
    @Referer.setter
    def Referer(self, value: StringType) -> None: ...
    
    @property
    def RequestUri(self) -> Uri: ...
    
    @property
    def SendChunked(self) -> BooleanType: ...
    
    @SendChunked.setter
    def SendChunked(self, value: BooleanType) -> None: ...
    
    @property
    def ServerCertificateValidationCallback(self) -> RemoteCertificateValidationCallback: ...
    
    @ServerCertificateValidationCallback.setter
    def ServerCertificateValidationCallback(self, value: RemoteCertificateValidationCallback) -> None: ...
    
    @property
    def ServicePoint(self) -> ServicePoint: ...
    
    @property
    def SupportsCookieContainer(self) -> BooleanType: ...
    
    @property
    def Timeout(self) -> IntType: ...
    
    @Timeout.setter
    def Timeout(self, value: IntType) -> None: ...
    
    @property
    def TransferEncoding(self) -> StringType: ...
    
    @TransferEncoding.setter
    def TransferEncoding(self, value: StringType) -> None: ...
    
    @property
    def UnsafeAuthenticatedConnectionSharing(self) -> BooleanType: ...
    
    @UnsafeAuthenticatedConnectionSharing.setter
    def UnsafeAuthenticatedConnectionSharing(self, value: BooleanType) -> None: ...
    
    @property
    def UseDefaultCredentials(self) -> BooleanType: ...
    
    @UseDefaultCredentials.setter
    def UseDefaultCredentials(self, value: BooleanType) -> None: ...
    
    @property
    def UserAgent(self) -> StringType: ...
    
    @UserAgent.setter
    def UserAgent(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Abort(self) -> VoidType: ...
    
    @overload
    def AddRange(self, from: IntType, to: IntType) -> VoidType: ...
    
    @overload
    def AddRange(self, from: LongType, to: LongType) -> VoidType: ...
    
    @overload
    def AddRange(self, range: IntType) -> VoidType: ...
    
    @overload
    def AddRange(self, range: LongType) -> VoidType: ...
    
    @overload
    def AddRange(self, rangeSpecifier: StringType, from: IntType, to: IntType) -> VoidType: ...
    
    @overload
    def AddRange(self, rangeSpecifier: StringType, from: LongType, to: LongType) -> VoidType: ...
    
    @overload
    def AddRange(self, rangeSpecifier: StringType, range: IntType) -> VoidType: ...
    
    @overload
    def AddRange(self, rangeSpecifier: StringType, range: LongType) -> VoidType: ...
    
    def BeginGetRequestStream(self, callback: AsyncCallback, state: ObjectType) -> IAsyncResult: ...
    
    def BeginGetResponse(self, callback: AsyncCallback, state: ObjectType) -> IAsyncResult: ...
    
    @overload
    def EndGetRequestStream(self, asyncResult: IAsyncResult) -> Stream: ...
    
    @overload
    def EndGetRequestStream(self, asyncResult: IAsyncResult, context: TransportContext) -> Tuple[Stream, TransportContext]: ...
    
    def EndGetResponse(self, asyncResult: IAsyncResult) -> WebResponse: ...
    
    @overload
    def GetRequestStream(self) -> Stream: ...
    
    @overload
    def GetRequestStream(self, context: TransportContext) -> Tuple[Stream, TransportContext]: ...
    
    def GetResponse(self) -> WebResponse: ...
    
    def get_Accept(self) -> StringType: ...
    
    def get_Address(self) -> Uri: ...
    
    def get_AllowAutoRedirect(self) -> BooleanType: ...
    
    def get_AllowReadStreamBuffering(self) -> BooleanType: ...
    
    def get_AllowWriteStreamBuffering(self) -> BooleanType: ...
    
    def get_AutomaticDecompression(self) -> DecompressionMethods: ...
    
    def get_ClientCertificates(self) -> X509CertificateCollection: ...
    
    def get_Connection(self) -> StringType: ...
    
    def get_ConnectionGroupName(self) -> StringType: ...
    
    def get_ContentLength(self) -> LongType: ...
    
    def get_ContentType(self) -> StringType: ...
    
    def get_ContinueDelegate(self) -> HttpContinueDelegate: ...
    
    def get_ContinueTimeout(self) -> IntType: ...
    
    def get_CookieContainer(self) -> CookieContainer: ...
    
    def get_Credentials(self) -> ICredentials: ...
    
    def get_Date(self) -> DateTime: ...
    
    @staticmethod
    def get_DefaultCachePolicy() -> RequestCachePolicy: ...
    
    @staticmethod
    def get_DefaultMaximumErrorResponseLength() -> IntType: ...
    
    @staticmethod
    def get_DefaultMaximumResponseHeadersLength() -> IntType: ...
    
    def get_Expect(self) -> StringType: ...
    
    def get_HaveResponse(self) -> BooleanType: ...
    
    def get_Headers(self) -> WebHeaderCollection: ...
    
    def get_Host(self) -> StringType: ...
    
    def get_IfModifiedSince(self) -> DateTime: ...
    
    def get_KeepAlive(self) -> BooleanType: ...
    
    def get_MaximumAutomaticRedirections(self) -> IntType: ...
    
    def get_MaximumResponseHeadersLength(self) -> IntType: ...
    
    def get_MediaType(self) -> StringType: ...
    
    def get_Method(self) -> StringType: ...
    
    def get_Pipelined(self) -> BooleanType: ...
    
    def get_PreAuthenticate(self) -> BooleanType: ...
    
    def get_ProtocolVersion(self) -> Version: ...
    
    def get_Proxy(self) -> IWebProxy: ...
    
    def get_ReadWriteTimeout(self) -> IntType: ...
    
    def get_Referer(self) -> StringType: ...
    
    def get_RequestUri(self) -> Uri: ...
    
    def get_SendChunked(self) -> BooleanType: ...
    
    def get_ServerCertificateValidationCallback(self) -> RemoteCertificateValidationCallback: ...
    
    def get_ServicePoint(self) -> ServicePoint: ...
    
    def get_SupportsCookieContainer(self) -> BooleanType: ...
    
    def get_Timeout(self) -> IntType: ...
    
    def get_TransferEncoding(self) -> StringType: ...
    
    def get_UnsafeAuthenticatedConnectionSharing(self) -> BooleanType: ...
    
    def get_UseDefaultCredentials(self) -> BooleanType: ...
    
    def get_UserAgent(self) -> StringType: ...
    
    def set_Accept(self, value: StringType) -> VoidType: ...
    
    def set_AllowAutoRedirect(self, value: BooleanType) -> VoidType: ...
    
    def set_AllowReadStreamBuffering(self, value: BooleanType) -> VoidType: ...
    
    def set_AllowWriteStreamBuffering(self, value: BooleanType) -> VoidType: ...
    
    def set_AutomaticDecompression(self, value: DecompressionMethods) -> VoidType: ...
    
    def set_ClientCertificates(self, value: X509CertificateCollection) -> VoidType: ...
    
    def set_Connection(self, value: StringType) -> VoidType: ...
    
    def set_ConnectionGroupName(self, value: StringType) -> VoidType: ...
    
    def set_ContentLength(self, value: LongType) -> VoidType: ...
    
    def set_ContentType(self, value: StringType) -> VoidType: ...
    
    def set_ContinueDelegate(self, value: HttpContinueDelegate) -> VoidType: ...
    
    def set_ContinueTimeout(self, value: IntType) -> VoidType: ...
    
    def set_CookieContainer(self, value: CookieContainer) -> VoidType: ...
    
    def set_Credentials(self, value: ICredentials) -> VoidType: ...
    
    def set_Date(self, value: DateTime) -> VoidType: ...
    
    @staticmethod
    def set_DefaultCachePolicy(value: RequestCachePolicy) -> VoidType: ...
    
    @staticmethod
    def set_DefaultMaximumErrorResponseLength(value: IntType) -> VoidType: ...
    
    @staticmethod
    def set_DefaultMaximumResponseHeadersLength(value: IntType) -> VoidType: ...
    
    def set_Expect(self, value: StringType) -> VoidType: ...
    
    def set_Headers(self, value: WebHeaderCollection) -> VoidType: ...
    
    def set_Host(self, value: StringType) -> VoidType: ...
    
    def set_IfModifiedSince(self, value: DateTime) -> VoidType: ...
    
    def set_KeepAlive(self, value: BooleanType) -> VoidType: ...
    
    def set_MaximumAutomaticRedirections(self, value: IntType) -> VoidType: ...
    
    def set_MaximumResponseHeadersLength(self, value: IntType) -> VoidType: ...
    
    def set_MediaType(self, value: StringType) -> VoidType: ...
    
    def set_Method(self, value: StringType) -> VoidType: ...
    
    def set_Pipelined(self, value: BooleanType) -> VoidType: ...
    
    def set_PreAuthenticate(self, value: BooleanType) -> VoidType: ...
    
    def set_ProtocolVersion(self, value: Version) -> VoidType: ...
    
    def set_Proxy(self, value: IWebProxy) -> VoidType: ...
    
    def set_ReadWriteTimeout(self, value: IntType) -> VoidType: ...
    
    def set_Referer(self, value: StringType) -> VoidType: ...
    
    def set_SendChunked(self, value: BooleanType) -> VoidType: ...
    
    def set_ServerCertificateValidationCallback(self, value: RemoteCertificateValidationCallback) -> VoidType: ...
    
    def set_Timeout(self, value: IntType) -> VoidType: ...
    
    def set_TransferEncoding(self, value: StringType) -> VoidType: ...
    
    def set_UnsafeAuthenticatedConnectionSharing(self, value: BooleanType) -> VoidType: ...
    
    def set_UseDefaultCredentials(self, value: BooleanType) -> VoidType: ...
    
    def set_UserAgent(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class HttpWebResponse(WebResponse, ISerializable, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CharacterSet(self) -> StringType: ...
    
    @property
    def ContentEncoding(self) -> StringType: ...
    
    @property
    def ContentLength(self) -> LongType: ...
    
    @property
    def ContentType(self) -> StringType: ...
    
    @property
    def Cookies(self) -> CookieCollection: ...
    
    @Cookies.setter
    def Cookies(self, value: CookieCollection) -> None: ...
    
    @property
    def Headers(self) -> WebHeaderCollection: ...
    
    @property
    def IsMutuallyAuthenticated(self) -> BooleanType: ...
    
    @property
    def LastModified(self) -> DateTime: ...
    
    @property
    def Method(self) -> StringType: ...
    
    @property
    def ProtocolVersion(self) -> Version: ...
    
    @property
    def ResponseUri(self) -> Uri: ...
    
    @property
    def Server(self) -> StringType: ...
    
    @property
    def StatusCode(self) -> HttpStatusCode: ...
    
    @property
    def StatusDescription(self) -> StringType: ...
    
    @property
    def SupportsHeaders(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    def GetResponseHeader(self, headerName: StringType) -> StringType: ...
    
    def GetResponseStream(self) -> Stream: ...
    
    def get_CharacterSet(self) -> StringType: ...
    
    def get_ContentEncoding(self) -> StringType: ...
    
    def get_ContentLength(self) -> LongType: ...
    
    def get_ContentType(self) -> StringType: ...
    
    def get_Cookies(self) -> CookieCollection: ...
    
    def get_Headers(self) -> WebHeaderCollection: ...
    
    def get_IsMutuallyAuthenticated(self) -> BooleanType: ...
    
    def get_LastModified(self) -> DateTime: ...
    
    def get_Method(self) -> StringType: ...
    
    def get_ProtocolVersion(self) -> Version: ...
    
    def get_ResponseUri(self) -> Uri: ...
    
    def get_Server(self) -> StringType: ...
    
    def get_StatusCode(self) -> HttpStatusCode: ...
    
    def get_StatusDescription(self) -> StringType: ...
    
    def get_SupportsHeaders(self) -> BooleanType: ...
    
    def set_Cookies(self, value: CookieCollection) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class HybridWebProxyFinder(ObjectType, IWebProxyFinder, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, engine: AutoWebProxyScriptEngine): ...
    
    # ---------- Properties ---------- #
    
    @property
    def IsValid(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def Abort(self) -> VoidType: ...
    
    def Dispose(self) -> VoidType: ...
    
    def GetProxies(self, destination: Uri, proxyList: IList[StringType]) -> Tuple[BooleanType, IList[StringType]]: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_IsValid(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IPAddress(ObjectType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Any() -> IPAddress: ...
    
    @staticmethod
    @property
    def Broadcast() -> IPAddress: ...
    
    @staticmethod
    @property
    def IPv6Any() -> IPAddress: ...
    
    @staticmethod
    @property
    def IPv6Loopback() -> IPAddress: ...
    
    @staticmethod
    @property
    def IPv6None() -> IPAddress: ...
    
    @staticmethod
    @property
    def Loopback() -> IPAddress: ...
    
    @staticmethod
    @property
    def None() -> IPAddress: ...
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, newAddress: LongType): ...
    
    @overload
    def __init__(self, address: ArrayType[ByteType], scopeid: LongType): ...
    
    @overload
    def __init__(self, address: ArrayType[ByteType]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Address(self) -> LongType: ...
    
    @Address.setter
    def Address(self, value: LongType) -> None: ...
    
    @property
    def AddressFamily(self) -> AddressFamily: ...
    
    @property
    def IsIPv4MappedToIPv6(self) -> BooleanType: ...
    
    @property
    def IsIPv6LinkLocal(self) -> BooleanType: ...
    
    @property
    def IsIPv6Multicast(self) -> BooleanType: ...
    
    @property
    def IsIPv6SiteLocal(self) -> BooleanType: ...
    
    @property
    def IsIPv6Teredo(self) -> BooleanType: ...
    
    @property
    def ScopeId(self) -> LongType: ...
    
    @ScopeId.setter
    def ScopeId(self, value: LongType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, comparand: ObjectType) -> BooleanType: ...
    
    def GetAddressBytes(self) -> ArrayType[ByteType]: ...
    
    def GetHashCode(self) -> IntType: ...
    
    @staticmethod
    @overload
    def HostToNetworkOrder(host: LongType) -> LongType: ...
    
    @staticmethod
    @overload
    def HostToNetworkOrder(host: IntType) -> IntType: ...
    
    @staticmethod
    @overload
    def HostToNetworkOrder(host: ShortType) -> ShortType: ...
    
    @staticmethod
    def IsLoopback(address: IPAddress) -> BooleanType: ...
    
    def MapToIPv4(self) -> IPAddress: ...
    
    def MapToIPv6(self) -> IPAddress: ...
    
    @staticmethod
    @overload
    def NetworkToHostOrder(network: LongType) -> LongType: ...
    
    @staticmethod
    @overload
    def NetworkToHostOrder(network: IntType) -> IntType: ...
    
    @staticmethod
    @overload
    def NetworkToHostOrder(network: ShortType) -> ShortType: ...
    
    @staticmethod
    def Parse(ipString: StringType) -> IPAddress: ...
    
    def ToString(self) -> StringType: ...
    
    @staticmethod
    def TryParse(ipString: StringType, address: IPAddress) -> Tuple[BooleanType, IPAddress]: ...
    
    def get_Address(self) -> LongType: ...
    
    def get_AddressFamily(self) -> AddressFamily: ...
    
    def get_IsIPv4MappedToIPv6(self) -> BooleanType: ...
    
    def get_IsIPv6LinkLocal(self) -> BooleanType: ...
    
    def get_IsIPv6Multicast(self) -> BooleanType: ...
    
    def get_IsIPv6SiteLocal(self) -> BooleanType: ...
    
    def get_IsIPv6Teredo(self) -> BooleanType: ...
    
    def get_ScopeId(self) -> LongType: ...
    
    def set_Address(self, value: LongType) -> VoidType: ...
    
    def set_ScopeId(self, value: LongType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IPEndPoint(EndPoint):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def MaxPort() -> IntType: ...
    
    @staticmethod
    @property
    def MinPort() -> IntType: ...
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, address: LongType, port: IntType): ...
    
    @overload
    def __init__(self, address: IPAddress, port: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Address(self) -> IPAddress: ...
    
    @Address.setter
    def Address(self, value: IPAddress) -> None: ...
    
    @property
    def AddressFamily(self) -> AddressFamily: ...
    
    @property
    def Port(self) -> IntType: ...
    
    @Port.setter
    def Port(self, value: IntType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Create(self, socketAddress: SocketAddress) -> EndPoint: ...
    
    def Equals(self, comparand: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def Serialize(self) -> SocketAddress: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Address(self) -> IPAddress: ...
    
    def get_AddressFamily(self) -> AddressFamily: ...
    
    def get_Port(self) -> IntType: ...
    
    def set_Address(self, value: IPAddress) -> VoidType: ...
    
    def set_Port(self, value: IntType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IPHostEntry(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AddressList(self) -> ArrayType[IPAddress]: ...
    
    @AddressList.setter
    def AddressList(self, value: ArrayType[IPAddress]) -> None: ...
    
    @property
    def Aliases(self) -> ArrayType[StringType]: ...
    
    @Aliases.setter
    def Aliases(self, value: ArrayType[StringType]) -> None: ...
    
    @property
    def HostName(self) -> StringType: ...
    
    @HostName.setter
    def HostName(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_AddressList(self) -> ArrayType[IPAddress]: ...
    
    def get_Aliases(self) -> ArrayType[StringType]: ...
    
    def get_HostName(self) -> StringType: ...
    
    def set_AddressList(self, value: ArrayType[IPAddress]) -> VoidType: ...
    
    def set_Aliases(self, value: ArrayType[StringType]) -> VoidType: ...
    
    def set_HostName(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IntPtrHelper(ABC, ObjectType):
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


class InterlockedStack(ObjectType):
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


class InternalException(SystemException, ISerializable, _Exception):
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


class KerberosClient(ObjectType, ISessionAuthenticationModule, IAuthenticationModule):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AuthenticationType(self) -> StringType: ...
    
    @property
    def CanPreAuthenticate(self) -> BooleanType: ...
    
    @property
    def CanUseDefaultCredentials(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def Authenticate(self, challenge: StringType, webRequest: WebRequest, credentials: ICredentials) -> Authorization: ...
    
    def ClearSession(self, webRequest: WebRequest) -> VoidType: ...
    
    def PreAuthenticate(self, webRequest: WebRequest, credentials: ICredentials) -> Authorization: ...
    
    def Update(self, challenge: StringType, webRequest: WebRequest) -> BooleanType: ...
    
    def get_AuthenticationType(self) -> StringType: ...
    
    def get_CanPreAuthenticate(self) -> BooleanType: ...
    
    def get_CanUseDefaultCredentials(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class KnownHttpVerb(ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def Equals(self, verb: KnownHttpVerb) -> BooleanType: ...
    
    @staticmethod
    def Parse(name: StringType) -> KnownHttpVerb: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class LazyAsyncResult(ObjectType, IAsyncResult):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def AsyncState(self) -> ObjectType: ...
    
    @property
    def AsyncWaitHandle(self) -> WaitHandle: ...
    
    @property
    def CompletedSynchronously(self) -> BooleanType: ...
    
    @property
    def IsCompleted(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def get_AsyncState(self) -> ObjectType: ...
    
    def get_AsyncWaitHandle(self) -> WaitHandle: ...
    
    def get_CompletedSynchronously(self) -> BooleanType: ...
    
    def get_IsCompleted(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ListenerAsyncResult(LazyAsyncResult, IAsyncResult):
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


class ListenerClientCertAsyncResult(LazyAsyncResult, IAsyncResult):
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


class ListenerPrefixEnumerator(ObjectType, IEnumerator[StringType], IDisposable, IEnumerator):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Current(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def Dispose(self) -> VoidType: ...
    
    def MoveNext(self) -> BooleanType: ...
    
    def get_Current(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Logging(ObjectType):
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


class NTAuthentication(ObjectType):
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


class NclConstants(ABC, ObjectType):
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


class NclUtilities(ABC, ObjectType):
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


class NegotiateClient(ObjectType, ISessionAuthenticationModule, IAuthenticationModule):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AuthenticationType(self) -> StringType: ...
    
    @property
    def CanPreAuthenticate(self) -> BooleanType: ...
    
    @property
    def CanUseDefaultCredentials(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def Authenticate(self, challenge: StringType, webRequest: WebRequest, credentials: ICredentials) -> Authorization: ...
    
    def ClearSession(self, webRequest: WebRequest) -> VoidType: ...
    
    def PreAuthenticate(self, webRequest: WebRequest, credentials: ICredentials) -> Authorization: ...
    
    def Update(self, challenge: StringType, webRequest: WebRequest) -> BooleanType: ...
    
    def get_AuthenticationType(self) -> StringType: ...
    
    def get_CanPreAuthenticate(self) -> BooleanType: ...
    
    def get_CanUseDefaultCredentials(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class NegotiationInfoClass(ObjectType):
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


class NestedMultipleAsyncResult(LazyAsyncResult, IAsyncResult):
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


class NestedSingleAsyncResult(LazyAsyncResult, IAsyncResult):
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


class NetRes(ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    @overload
    def GetWebStatusCodeString(statusCode: HttpStatusCode, statusDescription: StringType) -> StringType: ...
    
    @staticmethod
    @overload
    def GetWebStatusCodeString(statusCode: FtpStatusCode, statusDescription: StringType) -> StringType: ...
    
    @staticmethod
    @overload
    def GetWebStatusString(Res: StringType, Status: WebExceptionStatus) -> StringType: ...
    
    @staticmethod
    @overload
    def GetWebStatusString(Status: WebExceptionStatus) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class NetWebProxyFinder(BaseWebProxyFinder, IWebProxyFinder, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, engine: AutoWebProxyScriptEngine): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Abort(self) -> VoidType: ...
    
    def GetProxies(self, destination: Uri, proxyList: IList[StringType]) -> Tuple[BooleanType, IList[StringType]]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class NetworkAddressChangePolled(ObjectType, IDisposable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Dispose(self) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class NetworkCredential(ObjectType, ICredentials, ICredentialsByHost):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, userName: StringType, password: StringType): ...
    
    @overload
    def __init__(self, userName: StringType, password: SecureString): ...
    
    @overload
    def __init__(self, userName: StringType, password: StringType, domain: StringType): ...
    
    @overload
    def __init__(self, userName: StringType, password: SecureString, domain: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Domain(self) -> StringType: ...
    
    @Domain.setter
    def Domain(self, value: StringType) -> None: ...
    
    @property
    def Password(self) -> StringType: ...
    
    @Password.setter
    def Password(self, value: StringType) -> None: ...
    
    @property
    def SecurePassword(self) -> SecureString: ...
    
    @SecurePassword.setter
    def SecurePassword(self, value: SecureString) -> None: ...
    
    @property
    def UserName(self) -> StringType: ...
    
    @UserName.setter
    def UserName(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def GetCredential(self, uri: Uri, authType: StringType) -> NetworkCredential: ...
    
    @overload
    def GetCredential(self, host: StringType, port: IntType, authenticationType: StringType) -> NetworkCredential: ...
    
    def get_Domain(self) -> StringType: ...
    
    def get_Password(self) -> StringType: ...
    
    def get_SecurePassword(self) -> SecureString: ...
    
    def get_UserName(self) -> StringType: ...
    
    def set_Domain(self, value: StringType) -> VoidType: ...
    
    def set_Password(self, value: StringType) -> VoidType: ...
    
    def set_SecurePassword(self, value: SecureString) -> VoidType: ...
    
    def set_UserName(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class NetworkingPerfCounters(ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Enabled(self) -> BooleanType: ...
    
    @staticmethod
    @property
    def Instance() -> NetworkingPerfCounters: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Decrement(self, perfCounter: NetworkingPerfCounterName) -> VoidType: ...
    
    @overload
    def Decrement(self, perfCounter: NetworkingPerfCounterName, amount: LongType) -> VoidType: ...
    
    @staticmethod
    def GetTimestamp() -> LongType: ...
    
    @overload
    def Increment(self, perfCounter: NetworkingPerfCounterName, amount: LongType) -> VoidType: ...
    
    @overload
    def Increment(self, perfCounter: NetworkingPerfCounterName) -> VoidType: ...
    
    def IncrementAverage(self, perfCounter: NetworkingPerfCounterName, startTimestamp: LongType) -> VoidType: ...
    
    def get_Enabled(self) -> BooleanType: ...
    
    @staticmethod
    def get_Instance() -> NetworkingPerfCounters: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class NtlmClient(ObjectType, ISessionAuthenticationModule, IAuthenticationModule):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AuthenticationType(self) -> StringType: ...
    
    @property
    def CanPreAuthenticate(self) -> BooleanType: ...
    
    @property
    def CanUseDefaultCredentials(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def Authenticate(self, challenge: StringType, webRequest: WebRequest, credentials: ICredentials) -> Authorization: ...
    
    def ClearSession(self, webRequest: WebRequest) -> VoidType: ...
    
    def PreAuthenticate(self, webRequest: WebRequest, credentials: ICredentials) -> Authorization: ...
    
    def Update(self, challenge: StringType, webRequest: WebRequest) -> BooleanType: ...
    
    def get_AuthenticationType(self) -> StringType: ...
    
    def get_CanPreAuthenticate(self) -> BooleanType: ...
    
    def get_CanUseDefaultCredentials(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class OpenReadCompletedEventArgs(AsyncCompletedEventArgs):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Result(self) -> Stream: ...
    
    # ---------- Methods ---------- #
    
    def get_Result(self) -> Stream: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class OpenReadCompletedEventHandler(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, sender: ObjectType, e: OpenReadCompletedEventArgs, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, sender: ObjectType, e: OpenReadCompletedEventArgs) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class OpenWriteCompletedEventArgs(AsyncCompletedEventArgs):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Result(self) -> Stream: ...
    
    # ---------- Methods ---------- #
    
    def get_Result(self) -> Stream: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class OpenWriteCompletedEventHandler(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, sender: ObjectType, e: OpenWriteCompletedEventArgs, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, sender: ObjectType, e: OpenWriteCompletedEventArgs) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PathList(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def Item(self) -> ObjectType: ...
    
    @Item.setter
    def Item(self, value: ObjectType) -> None: ...
    
    @property
    def SyncRoot(self) -> ObjectType: ...
    
    @property
    def Values(self) -> ICollection: ...
    
    # ---------- Methods ---------- #
    
    def GetCookiesCount(self) -> IntType: ...
    
    def GetEnumerator(self) -> IEnumerator: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_Item(self, s: StringType) -> ObjectType: ...
    
    def get_SyncRoot(self) -> ObjectType: ...
    
    def get_Values(self) -> ICollection: ...
    
    def set_Item(self, s: StringType, value: ObjectType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PolicyWrapper(ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Accept(self, Certificate: X509Certificate, CertificateProblem: IntType) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PooledStream(Stream, IDisposable):
    # No Fields
    
    # No Constructors
    
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
    def WriteTimeout(self) -> IntType: ...
    
    @WriteTimeout.setter
    def WriteTimeout(self, value: IntType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def BeginRead(self, buffer: ArrayType[ByteType], offset: IntType, size: IntType, callback: AsyncCallback, state: ObjectType) -> IAsyncResult: ...
    
    def BeginWrite(self, buffer: ArrayType[ByteType], offset: IntType, size: IntType, callback: AsyncCallback, state: ObjectType) -> IAsyncResult: ...
    
    @overload
    def Close(self, timeout: IntType) -> VoidType: ...
    
    def EndRead(self, asyncResult: IAsyncResult) -> IntType: ...
    
    def EndWrite(self, asyncResult: IAsyncResult) -> VoidType: ...
    
    def Flush(self) -> VoidType: ...
    
    @overload
    def FlushAsync(self, cancellationToken: CancellationToken) -> Task: ...
    
    def Read(self, buffer: ArrayType[ByteType], offset: IntType, size: IntType) -> IntType: ...
    
    def Seek(self, offset: LongType, origin: SeekOrigin) -> LongType: ...
    
    def SetLength(self, value: LongType) -> VoidType: ...
    
    def Write(self, buffer: ArrayType[ByteType], offset: IntType, size: IntType) -> VoidType: ...
    
    def get_CanRead(self) -> BooleanType: ...
    
    def get_CanSeek(self) -> BooleanType: ...
    
    def get_CanTimeout(self) -> BooleanType: ...
    
    def get_CanWrite(self) -> BooleanType: ...
    
    def get_Length(self) -> LongType: ...
    
    def get_Position(self) -> LongType: ...
    
    def get_ReadTimeout(self) -> IntType: ...
    
    def get_WriteTimeout(self) -> IntType: ...
    
    def set_Position(self, value: LongType) -> VoidType: ...
    
    def set_ReadTimeout(self, value: IntType) -> VoidType: ...
    
    def set_WriteTimeout(self, value: IntType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PrefixLookup(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, capacity: IntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Add(self, prefix: StringType, value: ObjectType) -> VoidType: ...
    
    def Lookup(self, lookupKey: StringType) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ProtocolViolationException(InvalidOperationException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetObjectData(self, serializationInfo: SerializationInfo, streamingContext: StreamingContext) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ProxyChain(ABC, ObjectType, IEnumerable[Uri], IEnumerable, IDisposable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Dispose(self) -> VoidType: ...
    
    def GetEnumerator(self) -> IEnumerator[Uri]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ProxyScriptChain(ProxyChain, IEnumerable[Uri], IEnumerable, IDisposable):
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


class ReceiveState(ObjectType):
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


class RegBlobWebProxyDataBuilder(WebProxyDataBuilder):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, connectoid: StringType, registry: SafeRegistryHandle): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def ReadString(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RegistryConfiguration(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def AppConfigReadInt(configVariable: StringType, defaultValue: IntType) -> IntType: ...
    
    @staticmethod
    def AppConfigReadString(configVariable: StringType, defaultValue: StringType) -> StringType: ...
    
    @staticmethod
    def GlobalConfigReadInt(configVariable: StringType, defaultValue: IntType) -> IntType: ...
    
    @staticmethod
    def GlobalConfigReadString(configVariable: StringType, defaultValue: StringType) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RequestContextBase(ABC, ObjectType, IDisposable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    def Dispose(self) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RequestLifetimeSetter(ObjectType):
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


class ResponseDescription(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RtcState(ObjectType):
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


class SSPIAuthType(ObjectType, SSPIInterface):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def SecurityPackages(self) -> ArrayType[SecurityPackageInfoClass]: ...
    
    @SecurityPackages.setter
    def SecurityPackages(self, value: ArrayType[SecurityPackageInfoClass]) -> None: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def AcceptSecurityContext(self, credential: SafeFreeCredentials, context: SafeDeleteContext, inputBuffer: SecurityBuffer, inFlags: ContextFlags, endianness: Endianness, outputBuffer: SecurityBuffer, outFlags: ContextFlags) -> Tuple[IntType, SafeFreeCredentials, SafeDeleteContext, ContextFlags]: ...
    
    @overload
    def AcceptSecurityContext(self, credential: SafeFreeCredentials, context: SafeDeleteContext, inputBuffers: ArrayType[SecurityBuffer], inFlags: ContextFlags, endianness: Endianness, outputBuffer: SecurityBuffer, outFlags: ContextFlags) -> Tuple[IntType, SafeDeleteContext, ContextFlags]: ...
    
    @overload
    def AcquireCredentialsHandle(self, moduleName: StringType, usage: CredentialUse, authdata: AuthIdentity, outCredential: SafeFreeCredentials) -> Tuple[IntType, AuthIdentity, SafeFreeCredentials]: ...
    
    @overload
    def AcquireCredentialsHandle(self, moduleName: StringType, usage: CredentialUse, authdata: SafeSspiAuthDataHandle, outCredential: SafeFreeCredentials) -> Tuple[IntType, SafeSspiAuthDataHandle, SafeFreeCredentials]: ...
    
    @overload
    def AcquireCredentialsHandle(self, moduleName: StringType, usage: CredentialUse, authdata: SecureCredential, outCredential: SafeFreeCredentials) -> Tuple[IntType, SecureCredential, SafeFreeCredentials]: ...
    
    @overload
    def AcquireCredentialsHandle(self, moduleName: StringType, usage: CredentialUse, authdata: SecureCredential2, outCredential: SafeFreeCredentials) -> Tuple[IntType, SecureCredential2, SafeFreeCredentials]: ...
    
    def AcquireDefaultCredential(self, moduleName: StringType, usage: CredentialUse, outCredential: SafeFreeCredentials) -> Tuple[IntType, SafeFreeCredentials]: ...
    
    def ApplyControlToken(self, refContext: SafeDeleteContext, inputBuffers: ArrayType[SecurityBuffer]) -> Tuple[IntType, SafeDeleteContext]: ...
    
    def CompleteAuthToken(self, refContext: SafeDeleteContext, inputBuffers: ArrayType[SecurityBuffer]) -> Tuple[IntType, SafeDeleteContext]: ...
    
    def DecryptMessage(self, context: SafeDeleteContext, inputOutput: SecurityBufferDescriptor, sequenceNumber: UIntType) -> IntType: ...
    
    def EncryptMessage(self, context: SafeDeleteContext, inputOutput: SecurityBufferDescriptor, sequenceNumber: UIntType) -> IntType: ...
    
    def EnumerateSecurityPackages(self, pkgnum: IntType, pkgArray: SafeFreeContextBuffer) -> Tuple[IntType, IntType, SafeFreeContextBuffer]: ...
    
    @overload
    def InitializeSecurityContext(self, credential: SafeFreeCredentials, context: SafeDeleteContext, targetName: StringType, inFlags: ContextFlags, endianness: Endianness, inputBuffer: SecurityBuffer, outputBuffer: SecurityBuffer, outFlags: ContextFlags) -> Tuple[IntType, SafeFreeCredentials, SafeDeleteContext, ContextFlags]: ...
    
    @overload
    def InitializeSecurityContext(self, credential: SafeFreeCredentials, context: SafeDeleteContext, targetName: StringType, inFlags: ContextFlags, endianness: Endianness, inputBuffers: ArrayType[SecurityBuffer], outputBuffer: SecurityBuffer, outFlags: ContextFlags) -> Tuple[IntType, SafeDeleteContext, ContextFlags]: ...
    
    def MakeSignature(self, context: SafeDeleteContext, inputOutput: SecurityBufferDescriptor, sequenceNumber: UIntType) -> IntType: ...
    
    def QueryContextAttributes(self, context: SafeDeleteContext, attribute: ContextAttribute, buffer: ArrayType[ByteType], handleType: TypeType, refHandle: SafeHandle) -> Tuple[IntType, SafeHandle]: ...
    
    def QueryContextChannelBinding(self, context: SafeDeleteContext, attribute: ContextAttribute, binding: SafeFreeContextBufferChannelBinding) -> Tuple[IntType, SafeFreeContextBufferChannelBinding]: ...
    
    def QuerySecurityContextToken(self, phContext: SafeDeleteContext, phToken: SafeCloseHandle) -> Tuple[IntType, SafeCloseHandle]: ...
    
    def SetContextAttributes(self, context: SafeDeleteContext, attribute: ContextAttribute, buffer: ArrayType[ByteType]) -> IntType: ...
    
    def VerifySignature(self, context: SafeDeleteContext, inputOutput: SecurityBufferDescriptor, sequenceNumber: UIntType) -> IntType: ...
    
    def get_SecurityPackages(self) -> ArrayType[SecurityPackageInfoClass]: ...
    
    def set_SecurityPackages(self, value: ArrayType[SecurityPackageInfoClass]) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SSPISecureChannelType(ObjectType, SSPIInterface):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def SecurityPackages(self) -> ArrayType[SecurityPackageInfoClass]: ...
    
    @SecurityPackages.setter
    def SecurityPackages(self, value: ArrayType[SecurityPackageInfoClass]) -> None: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def AcceptSecurityContext(self, credential: SafeFreeCredentials, context: SafeDeleteContext, inputBuffer: SecurityBuffer, inFlags: ContextFlags, endianness: Endianness, outputBuffer: SecurityBuffer, outFlags: ContextFlags) -> Tuple[IntType, SafeFreeCredentials, SafeDeleteContext, ContextFlags]: ...
    
    @overload
    def AcceptSecurityContext(self, credential: SafeFreeCredentials, context: SafeDeleteContext, inputBuffers: ArrayType[SecurityBuffer], inFlags: ContextFlags, endianness: Endianness, outputBuffer: SecurityBuffer, outFlags: ContextFlags) -> Tuple[IntType, SafeDeleteContext, ContextFlags]: ...
    
    @overload
    def AcquireCredentialsHandle(self, moduleName: StringType, usage: CredentialUse, authdata: AuthIdentity, outCredential: SafeFreeCredentials) -> Tuple[IntType, AuthIdentity, SafeFreeCredentials]: ...
    
    @overload
    def AcquireCredentialsHandle(self, moduleName: StringType, usage: CredentialUse, authdata: SafeSspiAuthDataHandle, outCredential: SafeFreeCredentials) -> Tuple[IntType, SafeSspiAuthDataHandle, SafeFreeCredentials]: ...
    
    @overload
    def AcquireCredentialsHandle(self, moduleName: StringType, usage: CredentialUse, authdata: SecureCredential, outCredential: SafeFreeCredentials) -> Tuple[IntType, SecureCredential, SafeFreeCredentials]: ...
    
    @overload
    def AcquireCredentialsHandle(self, moduleName: StringType, usage: CredentialUse, authdata: SecureCredential2, outCredential: SafeFreeCredentials) -> Tuple[IntType, SecureCredential2, SafeFreeCredentials]: ...
    
    def AcquireDefaultCredential(self, moduleName: StringType, usage: CredentialUse, outCredential: SafeFreeCredentials) -> Tuple[IntType, SafeFreeCredentials]: ...
    
    def ApplyControlToken(self, refContext: SafeDeleteContext, inputBuffers: ArrayType[SecurityBuffer]) -> Tuple[IntType, SafeDeleteContext]: ...
    
    def CompleteAuthToken(self, refContext: SafeDeleteContext, inputBuffers: ArrayType[SecurityBuffer]) -> Tuple[IntType, SafeDeleteContext]: ...
    
    def DecryptMessage(self, context: SafeDeleteContext, inputOutput: SecurityBufferDescriptor, sequenceNumber: UIntType) -> IntType: ...
    
    def EncryptMessage(self, context: SafeDeleteContext, inputOutput: SecurityBufferDescriptor, sequenceNumber: UIntType) -> IntType: ...
    
    def EnumerateSecurityPackages(self, pkgnum: IntType, pkgArray: SafeFreeContextBuffer) -> Tuple[IntType, IntType, SafeFreeContextBuffer]: ...
    
    @overload
    def InitializeSecurityContext(self, credential: SafeFreeCredentials, context: SafeDeleteContext, targetName: StringType, inFlags: ContextFlags, endianness: Endianness, inputBuffer: SecurityBuffer, outputBuffer: SecurityBuffer, outFlags: ContextFlags) -> Tuple[IntType, SafeFreeCredentials, SafeDeleteContext, ContextFlags]: ...
    
    @overload
    def InitializeSecurityContext(self, credential: SafeFreeCredentials, context: SafeDeleteContext, targetName: StringType, inFlags: ContextFlags, endianness: Endianness, inputBuffers: ArrayType[SecurityBuffer], outputBuffer: SecurityBuffer, outFlags: ContextFlags) -> Tuple[IntType, SafeDeleteContext, ContextFlags]: ...
    
    def MakeSignature(self, context: SafeDeleteContext, inputOutput: SecurityBufferDescriptor, sequenceNumber: UIntType) -> IntType: ...
    
    def QueryContextAttributes(self, phContext: SafeDeleteContext, attribute: ContextAttribute, buffer: ArrayType[ByteType], handleType: TypeType, refHandle: SafeHandle) -> Tuple[IntType, SafeHandle]: ...
    
    def QueryContextChannelBinding(self, phContext: SafeDeleteContext, attribute: ContextAttribute, refHandle: SafeFreeContextBufferChannelBinding) -> Tuple[IntType, SafeFreeContextBufferChannelBinding]: ...
    
    def QuerySecurityContextToken(self, phContext: SafeDeleteContext, phToken: SafeCloseHandle) -> Tuple[IntType, SafeCloseHandle]: ...
    
    def SetContextAttributes(self, phContext: SafeDeleteContext, attribute: ContextAttribute, buffer: ArrayType[ByteType]) -> IntType: ...
    
    def VerifySignature(self, context: SafeDeleteContext, inputOutput: SecurityBufferDescriptor, sequenceNumber: UIntType) -> IntType: ...
    
    def get_SecurityPackages(self) -> ArrayType[SecurityPackageInfoClass]: ...
    
    def set_SecurityPackages(self, value: ArrayType[SecurityPackageInfoClass]) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SSPIWrapper(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    @overload
    def AcquireCredentialsHandle(SecModule: SSPIInterface, package: StringType, intent: CredentialUse, scc: SecureCredential) -> SafeFreeCredentials: ...
    
    @staticmethod
    @overload
    def AcquireCredentialsHandle(SecModule: SSPIInterface, package: StringType, intent: CredentialUse, authdata: AuthIdentity) -> Tuple[SafeFreeCredentials, AuthIdentity]: ...
    
    @staticmethod
    @overload
    def AcquireCredentialsHandle(SecModule: SSPIInterface, package: StringType, intent: CredentialUse, authdata: SafeSspiAuthDataHandle) -> Tuple[SafeFreeCredentials, SafeSspiAuthDataHandle]: ...
    
    @staticmethod
    @overload
    def AcquireCredentialsHandle(SecModule: SSPIInterface, package: StringType, intent: CredentialUse, scc: SecureCredential2) -> SafeFreeCredentials: ...
    
    @staticmethod
    def AcquireDefaultCredential(SecModule: SSPIInterface, package: StringType, intent: CredentialUse) -> SafeFreeCredentials: ...
    
    @staticmethod
    def ApplyAlertToken(secModule: SSPIInterface, credentialsHandle: SafeFreeCredentials, securityContext: SafeDeleteContext, alertType: TlsAlertType, alertMessage: TlsAlertMessage) -> Tuple[IntType, SafeFreeCredentials]: ...
    
    @staticmethod
    def ApplyShutdownToken(secModule: SSPIInterface, credentialsHandle: SafeFreeCredentials, securityContext: SafeDeleteContext) -> Tuple[IntType, SafeFreeCredentials]: ...
    
    @staticmethod
    def DecryptMessage(secModule: SSPIInterface, context: SafeDeleteContext, input: ArrayType[SecurityBuffer], sequenceNumber: UIntType) -> IntType: ...
    
    @staticmethod
    def EncryptMessage(secModule: SSPIInterface, context: SafeDeleteContext, input: ArrayType[SecurityBuffer], sequenceNumber: UIntType) -> IntType: ...
    
    @staticmethod
    def ErrorDescription(errorCode: IntType) -> StringType: ...
    
    @staticmethod
    @overload
    def QueryContextAttributes(SecModule: SSPIInterface, securityContext: SafeDeleteContext, contextAttribute: ContextAttribute, errorCode: IntType) -> Tuple[ObjectType, IntType]: ...
    
    @staticmethod
    @overload
    def QueryContextAttributes(SecModule: SSPIInterface, securityContext: SafeDeleteContext, contextAttribute: ContextAttribute) -> ObjectType: ...
    
    @staticmethod
    def QueryContextChannelBinding(SecModule: SSPIInterface, securityContext: SafeDeleteContext, contextAttribute: ContextAttribute) -> SafeFreeContextBufferChannelBinding: ...
    
    @staticmethod
    def QuerySecurityContextToken(SecModule: SSPIInterface, context: SafeDeleteContext, token: SafeCloseHandle) -> Tuple[IntType, SafeCloseHandle]: ...
    
    @staticmethod
    def SetContextAttributes(SecModule: SSPIInterface, securityContext: SafeDeleteContext, contextAttribute: ContextAttribute, value: ObjectType) -> IntType: ...
    
    @staticmethod
    def VerifySignature(secModule: SSPIInterface, context: SafeDeleteContext, input: ArrayType[SecurityBuffer], sequenceNumber: UIntType) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SafeCertSelectCritera(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def ToString(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SafeCloseHandle(CriticalHandleZeroOrMinusOneIsInvalid, IDisposable):
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


class SafeCloseIcmpHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
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


class SafeCloseSocket(SafeHandleMinusOneIsInvalid, IDisposable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def IsInvalid(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def get_IsInvalid(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SafeCloseSocketAndEvent(SafeCloseSocket, IDisposable):
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


class SafeCredentialReference(CriticalHandleMinusOneIsInvalid, IDisposable):
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


class SafeDeleteContext(ABC, SafeHandle, IDisposable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def IsInvalid(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def ToString(self) -> StringType: ...
    
    def get_IsInvalid(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SafeDeleteContext_SECURITY(SafeDeleteContext, IDisposable):
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


class SafeFreeAddrInfo(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
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


class SafeFreeCertChain(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def ToString(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SafeFreeCertChainList(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def ToString(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SafeFreeCertContext(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
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


class SafeFreeContextBuffer(ABC, SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def QueryContextAttributes(dll: SecurDll, phContext: SafeDeleteContext, contextAttribute: ContextAttribute, buffer: ByteType, refHandle: SafeHandle) -> IntType: ...
    
    @staticmethod
    def SetContextAttributes(dll: SecurDll, phContext: SafeDeleteContext, contextAttribute: ContextAttribute, buffer: ArrayType[ByteType]) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SafeFreeContextBufferChannelBinding(ABC, ChannelBinding, IDisposable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Size(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def QueryContextChannelBinding(dll: SecurDll, phContext: SafeDeleteContext, contextAttribute: ContextAttribute, buffer: Bindings, refHandle: SafeFreeContextBufferChannelBinding) -> IntType: ...
    
    def get_Size(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SafeFreeContextBufferChannelBinding_SECURITY(SafeFreeContextBufferChannelBinding, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SafeFreeContextBuffer_SECURITY(SafeFreeContextBuffer, IDisposable):
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


class SafeFreeCredential_SECURITY(SafeFreeCredentials, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SafeFreeCredentials(ABC, SafeHandle, IDisposable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def IsInvalid(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    @overload
    def AcquireCredentialsHandle(dll: SecurDll, package: StringType, intent: CredentialUse, authdata: SecureCredential, outCredential: SafeFreeCredentials) -> Tuple[IntType, SecureCredential, SafeFreeCredentials]: ...
    
    @staticmethod
    @overload
    def AcquireCredentialsHandle(dll: SecurDll, package: StringType, intent: CredentialUse, authdata: AuthIdentity, outCredential: SafeFreeCredentials) -> Tuple[IntType, AuthIdentity, SafeFreeCredentials]: ...
    
    @staticmethod
    @overload
    def AcquireCredentialsHandle(package: StringType, intent: CredentialUse, authdata: SafeSspiAuthDataHandle, outCredential: SafeFreeCredentials) -> Tuple[IntType, SafeSspiAuthDataHandle, SafeFreeCredentials]: ...
    
    @staticmethod
    @overload
    def AcquireCredentialsHandle(dll: SecurDll, package: StringType, intent: CredentialUse, authdata: SecureCredential2, outCredential: SafeFreeCredentials) -> Tuple[IntType, SecureCredential2, SafeFreeCredentials]: ...
    
    @staticmethod
    def AcquireDefaultCredential(dll: SecurDll, package: StringType, intent: CredentialUse, outCredential: SafeFreeCredentials) -> Tuple[IntType, SafeFreeCredentials]: ...
    
    def get_IsInvalid(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SafeGlobalFree(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
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


class SafeInternetHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SafeLoadLibrary(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Zero() -> SafeLoadLibrary: ...
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def HasFunction(self, functionName: StringType) -> BooleanType: ...
    
    @staticmethod
    def LoadLibraryEx(library: StringType) -> SafeLoadLibrary: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SafeLocalFree(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Zero() -> SafeLocalFree: ...
    
    @staticmethod
    @Zero.setter
    def Zero(value: SafeLocalFree) -> None: ...
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def LocalAlloc(cb: IntType) -> SafeLocalFree: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SafeLocalFreeChannelBinding(ChannelBinding, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Size(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def LocalAlloc(cb: IntType) -> SafeLocalFreeChannelBinding: ...
    
    def get_Size(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SafeNativeOverlapped(SafeHandle, IDisposable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def IsInvalid(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def ReinitializeNativeOverlapped(self) -> VoidType: ...
    
    def get_IsInvalid(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SafeNclNativeMethods(ABC, ObjectType):
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


class SafeOverlappedFree(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    @overload
    def Alloc() -> SafeOverlappedFree: ...
    
    @staticmethod
    @overload
    def Alloc(socketHandle: SafeCloseSocket) -> SafeOverlappedFree: ...
    
    @overload
    def Close(self, resetOwner: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SafeRegistryHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
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


class SafeSspiAuthDataHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SafeUnlockUrlCacheEntryFile(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
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


class SafeWebSocketHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
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


class ScatterGatherBuffers(ObjectType):
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


class SecChannelBindings(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SecSizes(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def BlockSize(self) -> IntType: ...
    
    @property
    def MaxSignature(self) -> IntType: ...
    
    @property
    def MaxToken(self) -> IntType: ...
    
    @property
    def SecurityTrailer(self) -> IntType: ...
    
    @staticmethod
    @property
    def SizeOf() -> IntType: ...
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SecurityBuffer(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def offset(self) -> IntType: ...
    
    @offset.setter
    def offset(self, value: IntType) -> None: ...
    
    @property
    def size(self) -> IntType: ...
    
    @size.setter
    def size(self, value: IntType) -> None: ...
    
    @property
    def token(self) -> ArrayType[ByteType]: ...
    
    @token.setter
    def token(self, value: ArrayType[ByteType]) -> None: ...
    
    @property
    def type(self) -> BufferType: ...
    
    @type.setter
    def type(self, value: BufferType) -> None: ...
    
    @property
    def unmanagedToken(self) -> SafeHandle: ...
    
    @unmanagedToken.setter
    def unmanagedToken(self, value: SafeHandle) -> None: ...
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, data: ArrayType[ByteType], offset: IntType, size: IntType, tokentype: BufferType): ...
    
    @overload
    def __init__(self, data: ArrayType[ByteType], tokentype: BufferType): ...
    
    @overload
    def __init__(self, size: IntType, tokentype: BufferType): ...
    
    @overload
    def __init__(self, binding: ChannelBinding): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SecurityBufferDescriptor(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def UnmanagedPointer(self) -> VoidType: ...
    
    @UnmanagedPointer.setter
    def UnmanagedPointer(self, value: VoidType) -> None: ...
    
    @property
    def Version(self) -> IntType: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self, count: IntType): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SecurityPackageInfoClass(ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def ToString(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Semaphore(WaitHandle, IDisposable):
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


class ServerCertValidationCallback(ObjectType):
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


class ServiceNameStore(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ServiceNames(self) -> ServiceNameCollection: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, uriPrefix: StringType) -> BooleanType: ...
    
    def BuildServiceNames(self, uriPrefix: StringType) -> ArrayType[StringType]: ...
    
    def BuildSimpleServiceName(self, uriPrefix: StringType) -> StringType: ...
    
    def Clear(self) -> VoidType: ...
    
    def Remove(self, uriPrefix: StringType) -> BooleanType: ...
    
    def get_ServiceNames(self) -> ServiceNameCollection: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ServicePoint(ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Address(self) -> Uri: ...
    
    @property
    def BindIPEndPointDelegate(self) -> BindIPEndPoint: ...
    
    @BindIPEndPointDelegate.setter
    def BindIPEndPointDelegate(self, value: BindIPEndPoint) -> None: ...
    
    @property
    def Certificate(self) -> X509Certificate: ...
    
    @property
    def ClientCertificate(self) -> X509Certificate: ...
    
    @property
    def ConnectionLeaseTimeout(self) -> IntType: ...
    
    @ConnectionLeaseTimeout.setter
    def ConnectionLeaseTimeout(self, value: IntType) -> None: ...
    
    @property
    def ConnectionLimit(self) -> IntType: ...
    
    @ConnectionLimit.setter
    def ConnectionLimit(self, value: IntType) -> None: ...
    
    @property
    def ConnectionName(self) -> StringType: ...
    
    @property
    def CurrentConnections(self) -> IntType: ...
    
    @property
    def Expect100Continue(self) -> BooleanType: ...
    
    @Expect100Continue.setter
    def Expect100Continue(self, value: BooleanType) -> None: ...
    
    @property
    def IdleSince(self) -> DateTime: ...
    
    @property
    def MaxIdleTime(self) -> IntType: ...
    
    @MaxIdleTime.setter
    def MaxIdleTime(self, value: IntType) -> None: ...
    
    @property
    def ProtocolVersion(self) -> Version: ...
    
    @property
    def ReceiveBufferSize(self) -> IntType: ...
    
    @ReceiveBufferSize.setter
    def ReceiveBufferSize(self, value: IntType) -> None: ...
    
    @property
    def SupportsPipelining(self) -> BooleanType: ...
    
    @property
    def UseNagleAlgorithm(self) -> BooleanType: ...
    
    @UseNagleAlgorithm.setter
    def UseNagleAlgorithm(self, value: BooleanType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def CloseConnectionGroup(self, connectionGroupName: StringType) -> BooleanType: ...
    
    def SetTcpKeepAlive(self, enabled: BooleanType, keepAliveTime: IntType, keepAliveInterval: IntType) -> VoidType: ...
    
    def get_Address(self) -> Uri: ...
    
    def get_BindIPEndPointDelegate(self) -> BindIPEndPoint: ...
    
    def get_Certificate(self) -> X509Certificate: ...
    
    def get_ClientCertificate(self) -> X509Certificate: ...
    
    def get_ConnectionLeaseTimeout(self) -> IntType: ...
    
    def get_ConnectionLimit(self) -> IntType: ...
    
    def get_ConnectionName(self) -> StringType: ...
    
    def get_CurrentConnections(self) -> IntType: ...
    
    def get_Expect100Continue(self) -> BooleanType: ...
    
    def get_IdleSince(self) -> DateTime: ...
    
    def get_MaxIdleTime(self) -> IntType: ...
    
    def get_ProtocolVersion(self) -> Version: ...
    
    def get_ReceiveBufferSize(self) -> IntType: ...
    
    def get_SupportsPipelining(self) -> BooleanType: ...
    
    def get_UseNagleAlgorithm(self) -> BooleanType: ...
    
    def set_BindIPEndPointDelegate(self, value: BindIPEndPoint) -> VoidType: ...
    
    def set_ConnectionLeaseTimeout(self, value: IntType) -> VoidType: ...
    
    def set_ConnectionLimit(self, value: IntType) -> VoidType: ...
    
    def set_Expect100Continue(self, value: BooleanType) -> VoidType: ...
    
    def set_MaxIdleTime(self, value: IntType) -> VoidType: ...
    
    def set_ReceiveBufferSize(self, value: IntType) -> VoidType: ...
    
    def set_UseNagleAlgorithm(self, value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ServicePointManager(ObjectType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def DefaultNonPersistentConnectionLimit() -> IntType: ...
    
    @staticmethod
    @property
    def DefaultPersistentConnectionLimit() -> IntType: ...
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def CertificatePolicy() -> ICertificatePolicy: ...
    
    @staticmethod
    @CertificatePolicy.setter
    def CertificatePolicy(value: ICertificatePolicy) -> None: ...
    
    @staticmethod
    @property
    def CheckCertificateRevocationList() -> BooleanType: ...
    
    @staticmethod
    @CheckCertificateRevocationList.setter
    def CheckCertificateRevocationList(value: BooleanType) -> None: ...
    
    @staticmethod
    @property
    def DefaultConnectionLimit() -> IntType: ...
    
    @staticmethod
    @DefaultConnectionLimit.setter
    def DefaultConnectionLimit(value: IntType) -> None: ...
    
    @staticmethod
    @property
    def DnsRefreshTimeout() -> IntType: ...
    
    @staticmethod
    @DnsRefreshTimeout.setter
    def DnsRefreshTimeout(value: IntType) -> None: ...
    
    @staticmethod
    @property
    def EnableDnsRoundRobin() -> BooleanType: ...
    
    @staticmethod
    @EnableDnsRoundRobin.setter
    def EnableDnsRoundRobin(value: BooleanType) -> None: ...
    
    @staticmethod
    @property
    def EncryptionPolicy() -> EncryptionPolicy: ...
    
    @staticmethod
    @property
    def Expect100Continue() -> BooleanType: ...
    
    @staticmethod
    @Expect100Continue.setter
    def Expect100Continue(value: BooleanType) -> None: ...
    
    @staticmethod
    @property
    def MaxServicePointIdleTime() -> IntType: ...
    
    @staticmethod
    @MaxServicePointIdleTime.setter
    def MaxServicePointIdleTime(value: IntType) -> None: ...
    
    @staticmethod
    @property
    def MaxServicePoints() -> IntType: ...
    
    @staticmethod
    @MaxServicePoints.setter
    def MaxServicePoints(value: IntType) -> None: ...
    
    @staticmethod
    @property
    def ReusePort() -> BooleanType: ...
    
    @staticmethod
    @ReusePort.setter
    def ReusePort(value: BooleanType) -> None: ...
    
    @staticmethod
    @property
    def SecurityProtocol() -> SecurityProtocolType: ...
    
    @staticmethod
    @SecurityProtocol.setter
    def SecurityProtocol(value: SecurityProtocolType) -> None: ...
    
    @staticmethod
    @property
    def ServerCertificateValidationCallback() -> RemoteCertificateValidationCallback: ...
    
    @staticmethod
    @ServerCertificateValidationCallback.setter
    def ServerCertificateValidationCallback(value: RemoteCertificateValidationCallback) -> None: ...
    
    @staticmethod
    @property
    def UseNagleAlgorithm() -> BooleanType: ...
    
    @staticmethod
    @UseNagleAlgorithm.setter
    def UseNagleAlgorithm(value: BooleanType) -> None: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    @overload
    def FindServicePoint(address: Uri) -> ServicePoint: ...
    
    @staticmethod
    @overload
    def FindServicePoint(uriString: StringType, proxy: IWebProxy) -> ServicePoint: ...
    
    @staticmethod
    @overload
    def FindServicePoint(address: Uri, proxy: IWebProxy) -> ServicePoint: ...
    
    @staticmethod
    def SetTcpKeepAlive(enabled: BooleanType, keepAliveTime: IntType, keepAliveInterval: IntType) -> VoidType: ...
    
    @staticmethod
    def get_CertificatePolicy() -> ICertificatePolicy: ...
    
    @staticmethod
    def get_CheckCertificateRevocationList() -> BooleanType: ...
    
    @staticmethod
    def get_DefaultConnectionLimit() -> IntType: ...
    
    @staticmethod
    def get_DnsRefreshTimeout() -> IntType: ...
    
    @staticmethod
    def get_EnableDnsRoundRobin() -> BooleanType: ...
    
    @staticmethod
    def get_EncryptionPolicy() -> EncryptionPolicy: ...
    
    @staticmethod
    def get_Expect100Continue() -> BooleanType: ...
    
    @staticmethod
    def get_MaxServicePointIdleTime() -> IntType: ...
    
    @staticmethod
    def get_MaxServicePoints() -> IntType: ...
    
    @staticmethod
    def get_ReusePort() -> BooleanType: ...
    
    @staticmethod
    def get_SecurityProtocol() -> SecurityProtocolType: ...
    
    @staticmethod
    def get_ServerCertificateValidationCallback() -> RemoteCertificateValidationCallback: ...
    
    @staticmethod
    def get_UseNagleAlgorithm() -> BooleanType: ...
    
    @staticmethod
    def set_CertificatePolicy(value: ICertificatePolicy) -> VoidType: ...
    
    @staticmethod
    def set_CheckCertificateRevocationList(value: BooleanType) -> VoidType: ...
    
    @staticmethod
    def set_DefaultConnectionLimit(value: IntType) -> VoidType: ...
    
    @staticmethod
    def set_DnsRefreshTimeout(value: IntType) -> VoidType: ...
    
    @staticmethod
    def set_EnableDnsRoundRobin(value: BooleanType) -> VoidType: ...
    
    @staticmethod
    def set_Expect100Continue(value: BooleanType) -> VoidType: ...
    
    @staticmethod
    def set_MaxServicePointIdleTime(value: IntType) -> VoidType: ...
    
    @staticmethod
    def set_MaxServicePoints(value: IntType) -> VoidType: ...
    
    @staticmethod
    def set_ReusePort(value: BooleanType) -> VoidType: ...
    
    @staticmethod
    def set_SecurityProtocol(value: SecurityProtocolType) -> VoidType: ...
    
    @staticmethod
    def set_ServerCertificateValidationCallback(value: RemoteCertificateValidationCallback) -> VoidType: ...
    
    @staticmethod
    def set_UseNagleAlgorithm(value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SocketAddress(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, family: AddressFamily): ...
    
    @overload
    def __init__(self, family: AddressFamily, size: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Family(self) -> AddressFamily: ...
    
    @property
    def Item(self) -> ByteType: ...
    
    @Item.setter
    def Item(self, value: ByteType) -> None: ...
    
    @property
    def Size(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, comparand: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Family(self) -> AddressFamily: ...
    
    def get_Item(self, offset: IntType) -> ByteType: ...
    
    def get_Size(self) -> IntType: ...
    
    def set_Item(self, offset: IntType, value: ByteType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SocketPermission(CodeAccessPermission, IPermission, ISecurityEncodable, IStackWalk, IUnrestrictedPermission):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def AllPorts() -> IntType: ...
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, state: PermissionState): ...
    
    @overload
    def __init__(self, access: NetworkAccess, transport: TransportType, hostName: StringType, portNumber: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AcceptList(self) -> IEnumerator: ...
    
    @property
    def ConnectList(self) -> IEnumerator: ...
    
    # ---------- Methods ---------- #
    
    def AddPermission(self, access: NetworkAccess, transport: TransportType, hostName: StringType, portNumber: IntType) -> VoidType: ...
    
    def Copy(self) -> IPermission: ...
    
    def FromXml(self, securityElement: SecurityElement) -> VoidType: ...
    
    def Intersect(self, target: IPermission) -> IPermission: ...
    
    def IsSubsetOf(self, target: IPermission) -> BooleanType: ...
    
    def IsUnrestricted(self) -> BooleanType: ...
    
    def ToXml(self) -> SecurityElement: ...
    
    def Union(self, target: IPermission) -> IPermission: ...
    
    def get_AcceptList(self) -> IEnumerator: ...
    
    def get_ConnectList(self) -> IEnumerator: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SocketPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, action: SecurityAction): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Access(self) -> StringType: ...
    
    @Access.setter
    def Access(self, value: StringType) -> None: ...
    
    @property
    def Host(self) -> StringType: ...
    
    @Host.setter
    def Host(self, value: StringType) -> None: ...
    
    @property
    def Port(self) -> StringType: ...
    
    @Port.setter
    def Port(self, value: StringType) -> None: ...
    
    @property
    def Transport(self) -> StringType: ...
    
    @Transport.setter
    def Transport(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def CreatePermission(self) -> IPermission: ...
    
    def get_Access(self) -> StringType: ...
    
    def get_Host(self) -> StringType: ...
    
    def get_Port(self) -> StringType: ...
    
    def get_Transport(self) -> StringType: ...
    
    def set_Access(self, value: StringType) -> VoidType: ...
    
    def set_Host(self, value: StringType) -> VoidType: ...
    
    def set_Port(self, value: StringType) -> VoidType: ...
    
    def set_Transport(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SplitWritesState(ObjectType):
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


class SpnDictionary(StringDictionary, IEnumerable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def IsSynchronized(self) -> BooleanType: ...
    
    @property
    def Item(self) -> StringType: ...
    
    @Item.setter
    def Item(self, value: StringType) -> None: ...
    
    @property
    def Keys(self) -> ICollection: ...
    
    @property
    def SyncRoot(self) -> ObjectType: ...
    
    @property
    def Values(self) -> ICollection: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, key: StringType, value: StringType) -> VoidType: ...
    
    def Clear(self) -> VoidType: ...
    
    def ContainsKey(self, key: StringType) -> BooleanType: ...
    
    def ContainsValue(self, value: StringType) -> BooleanType: ...
    
    def CopyTo(self, array: Array, index: IntType) -> VoidType: ...
    
    def GetEnumerator(self) -> IEnumerator: ...
    
    def Remove(self, key: StringType) -> VoidType: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_IsSynchronized(self) -> BooleanType: ...
    
    def get_Item(self, key: StringType) -> StringType: ...
    
    def get_Keys(self) -> ICollection: ...
    
    def get_SyncRoot(self) -> ObjectType: ...
    
    def get_Values(self) -> ICollection: ...
    
    def set_Item(self, key: StringType, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SpnToken(ObjectType):
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


class SslConnectionInfo(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def DataCipherAlg(self) -> IntType: ...
    
    @property
    def DataHashAlg(self) -> IntType: ...
    
    @property
    def DataHashKeySize(self) -> IntType: ...
    
    @property
    def DataKeySize(self) -> IntType: ...
    
    @property
    def KeyExchKeySize(self) -> IntType: ...
    
    @property
    def KeyExchangeAlg(self) -> IntType: ...
    
    @property
    def Protocol(self) -> IntType: ...
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SslStreamContext(TransportContext):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetChannelBinding(self, kind: ChannelBindingKind) -> ChannelBinding: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class StaticProxy(ProxyChain, IEnumerable[Uri], IEnumerable, IDisposable):
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


class StreamFramer(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, Transport: Stream): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ReadHeader(self) -> FrameHeader: ...
    
    @property
    def Transport(self) -> Stream: ...
    
    @property
    def WriteHeader(self) -> FrameHeader: ...
    
    # ---------- Methods ---------- #
    
    def BeginReadMessage(self, asyncCallback: AsyncCallback, stateObject: ObjectType) -> IAsyncResult: ...
    
    def BeginWriteMessage(self, message: ArrayType[ByteType], asyncCallback: AsyncCallback, stateObject: ObjectType) -> IAsyncResult: ...
    
    def EndReadMessage(self, asyncResult: IAsyncResult) -> ArrayType[ByteType]: ...
    
    def EndWriteMessage(self, asyncResult: IAsyncResult) -> VoidType: ...
    
    def ReadMessage(self) -> ArrayType[ByteType]: ...
    
    def WriteMessage(self, message: ArrayType[ByteType]) -> VoidType: ...
    
    def get_ReadHeader(self) -> FrameHeader: ...
    
    def get_Transport(self) -> Stream: ...
    
    def get_WriteHeader(self) -> FrameHeader: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class StreamSizes(ObjectType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def SizeOf() -> IntType: ...
    
    @property
    def blockSize(self) -> IntType: ...
    
    @blockSize.setter
    def blockSize(self, value: IntType) -> None: ...
    
    @property
    def buffersCount(self) -> IntType: ...
    
    @buffersCount.setter
    def buffersCount(self, value: IntType) -> None: ...
    
    @property
    def header(self) -> IntType: ...
    
    @header.setter
    def header(self, value: IntType) -> None: ...
    
    @property
    def maximumMessage(self) -> IntType: ...
    
    @maximumMessage.setter
    def maximumMessage(self, value: IntType) -> None: ...
    
    @property
    def trailer(self) -> IntType: ...
    
    @trailer.setter
    def trailer(self, value: IntType) -> None: ...
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SyncMemoryStream(MemoryStream, IDisposable, IRequestLifetimeTracker):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def CanTimeout(self) -> BooleanType: ...
    
    @property
    def ReadTimeout(self) -> IntType: ...
    
    @ReadTimeout.setter
    def ReadTimeout(self, value: IntType) -> None: ...
    
    @property
    def WriteTimeout(self) -> IntType: ...
    
    @WriteTimeout.setter
    def WriteTimeout(self, value: IntType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def BeginRead(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType, callback: AsyncCallback, state: ObjectType) -> IAsyncResult: ...
    
    def BeginWrite(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType, callback: AsyncCallback, state: ObjectType) -> IAsyncResult: ...
    
    def EndRead(self, asyncResult: IAsyncResult) -> IntType: ...
    
    def EndWrite(self, asyncResult: IAsyncResult) -> VoidType: ...
    
    def TrackRequestLifetime(self, requestStartTimestamp: LongType) -> VoidType: ...
    
    def get_CanTimeout(self) -> BooleanType: ...
    
    def get_ReadTimeout(self) -> IntType: ...
    
    def get_WriteTimeout(self) -> IntType: ...
    
    def set_ReadTimeout(self, value: IntType) -> VoidType: ...
    
    def set_WriteTimeout(self, value: IntType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SyncRequestContext(RequestContextBase, IDisposable):
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


class SystemNetworkCredential(NetworkCredential, ICredentials, ICredentialsByHost):
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


class TimeoutValidator(ConfigurationValidatorBase):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def CanValidate(self, type: TypeType) -> BooleanType: ...
    
    def Validate(self, value: ObjectType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TimerThread(ABC, ObjectType):
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


class TlsStream(NetworkStream, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, destinationHost: StringType, networkStream: NetworkStream, checkCertificateRevocationList: BooleanType, sslProtocols: SslProtocols, clientCertificates: X509CertificateCollection, servicePoint: ServicePoint, initiatingRequest: ObjectType, executionContext: ExecutionContext): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ClientCertificate(self) -> X509Certificate: ...
    
    @property
    def DataAvailable(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def BeginRead(self, buffer: ArrayType[ByteType], offset: IntType, size: IntType, asyncCallback: AsyncCallback, asyncState: ObjectType) -> IAsyncResult: ...
    
    def BeginWrite(self, buffer: ArrayType[ByteType], offset: IntType, size: IntType, asyncCallback: AsyncCallback, asyncState: ObjectType) -> IAsyncResult: ...
    
    def EndRead(self, asyncResult: IAsyncResult) -> IntType: ...
    
    def EndWrite(self, asyncResult: IAsyncResult) -> VoidType: ...
    
    def Read(self, buffer: ArrayType[ByteType], offset: IntType, size: IntType) -> IntType: ...
    
    def Write(self, buffer: ArrayType[ByteType], offset: IntType, size: IntType) -> VoidType: ...
    
    def get_ClientCertificate(self) -> X509Certificate: ...
    
    def get_DataAvailable(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TrackingStringDictionary(StringDictionary, IEnumerable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Item(self) -> StringType: ...
    
    @Item.setter
    def Item(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, key: StringType, value: StringType) -> VoidType: ...
    
    def Clear(self) -> VoidType: ...
    
    def Remove(self, key: StringType) -> VoidType: ...
    
    def get_Item(self, key: StringType) -> StringType: ...
    
    def set_Item(self, key: StringType, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TrackingValidationObjectDictionary(StringDictionary, IEnumerable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Item(self) -> StringType: ...
    
    @Item.setter
    def Item(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, key: StringType, value: StringType) -> VoidType: ...
    
    def Clear(self) -> VoidType: ...
    
    def Remove(self, key: StringType) -> VoidType: ...
    
    def get_Item(self, key: StringType) -> StringType: ...
    
    def set_Item(self, key: StringType, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TransmitFileBuffers(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TransportContext(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetChannelBinding(self, kind: ChannelBindingKind) -> ChannelBinding: ...
    
    def GetTlsTokenBindings(self) -> IEnumerable[TokenBinding]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UnlockConnectionDelegate(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UnsafeNclNativeMethods(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def CoCreateInstance(clsid: Guid, pUnkOuter: NIntType, context: IntType, iid: Guid, o: ObjectType) -> Tuple[VoidType, Guid, Guid, ObjectType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UploadDataCompletedEventArgs(AsyncCompletedEventArgs):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Result(self) -> ArrayType[ByteType]: ...
    
    # ---------- Methods ---------- #
    
    def get_Result(self) -> ArrayType[ByteType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UploadDataCompletedEventHandler(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, sender: ObjectType, e: UploadDataCompletedEventArgs, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, sender: ObjectType, e: UploadDataCompletedEventArgs) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UploadFileCompletedEventArgs(AsyncCompletedEventArgs):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Result(self) -> ArrayType[ByteType]: ...
    
    # ---------- Methods ---------- #
    
    def get_Result(self) -> ArrayType[ByteType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UploadFileCompletedEventHandler(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, sender: ObjectType, e: UploadFileCompletedEventArgs, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, sender: ObjectType, e: UploadFileCompletedEventArgs) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UploadProgressChangedEventArgs(ProgressChangedEventArgs):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def BytesReceived(self) -> LongType: ...
    
    @property
    def BytesSent(self) -> LongType: ...
    
    @property
    def TotalBytesToReceive(self) -> LongType: ...
    
    @property
    def TotalBytesToSend(self) -> LongType: ...
    
    # ---------- Methods ---------- #
    
    def get_BytesReceived(self) -> LongType: ...
    
    def get_BytesSent(self) -> LongType: ...
    
    def get_TotalBytesToReceive(self) -> LongType: ...
    
    def get_TotalBytesToSend(self) -> LongType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UploadProgressChangedEventHandler(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, sender: ObjectType, e: UploadProgressChangedEventArgs, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, sender: ObjectType, e: UploadProgressChangedEventArgs) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UploadStringCompletedEventArgs(AsyncCompletedEventArgs):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Result(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_Result(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UploadStringCompletedEventHandler(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, sender: ObjectType, e: UploadStringCompletedEventArgs, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, sender: ObjectType, e: UploadStringCompletedEventArgs) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UploadValuesCompletedEventArgs(AsyncCompletedEventArgs):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Result(self) -> ArrayType[ByteType]: ...
    
    # ---------- Methods ---------- #
    
    def get_Result(self) -> ArrayType[ByteType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UploadValuesCompletedEventHandler(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, sender: ObjectType, e: UploadValuesCompletedEventArgs, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, sender: ObjectType, e: UploadValuesCompletedEventArgs) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ValidationHelper(ABC, ObjectType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def EmptyArray() -> ArrayType[StringType]: ...
    
    @staticmethod
    @EmptyArray.setter
    def EmptyArray(value: ArrayType[StringType]) -> None: ...
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def ExceptionMessage(exception: Exception) -> StringType: ...
    
    @staticmethod
    def HashString(objectValue: ObjectType) -> StringType: ...
    
    @staticmethod
    def IsBlankString(stringValue: StringType) -> BooleanType: ...
    
    @staticmethod
    def IsInvalidHttpString(stringValue: StringType) -> BooleanType: ...
    
    @staticmethod
    def MakeEmptyArrayNull(stringArray: ArrayType[StringType]) -> ArrayType[StringType]: ...
    
    @staticmethod
    def MakeStringNull(stringValue: StringType) -> StringType: ...
    
    @staticmethod
    @overload
    def ToString(objectValue: ObjectType) -> StringType: ...
    
    @staticmethod
    def ValidateRange(actual: IntType, fromAllowed: IntType, toAllowed: IntType) -> BooleanType: ...
    
    @staticmethod
    def ValidateTcpPort(port: IntType) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class WebClient(Component, IComponent, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AllowReadStreamBuffering(self) -> BooleanType: ...
    
    @AllowReadStreamBuffering.setter
    def AllowReadStreamBuffering(self, value: BooleanType) -> None: ...
    
    @property
    def AllowWriteStreamBuffering(self) -> BooleanType: ...
    
    @AllowWriteStreamBuffering.setter
    def AllowWriteStreamBuffering(self, value: BooleanType) -> None: ...
    
    @property
    def BaseAddress(self) -> StringType: ...
    
    @BaseAddress.setter
    def BaseAddress(self, value: StringType) -> None: ...
    
    @property
    def CachePolicy(self) -> RequestCachePolicy: ...
    
    @CachePolicy.setter
    def CachePolicy(self, value: RequestCachePolicy) -> None: ...
    
    @property
    def Credentials(self) -> ICredentials: ...
    
    @Credentials.setter
    def Credentials(self, value: ICredentials) -> None: ...
    
    @property
    def Encoding(self) -> Encoding: ...
    
    @Encoding.setter
    def Encoding(self, value: Encoding) -> None: ...
    
    @property
    def Headers(self) -> WebHeaderCollection: ...
    
    @Headers.setter
    def Headers(self, value: WebHeaderCollection) -> None: ...
    
    @property
    def IsBusy(self) -> BooleanType: ...
    
    @property
    def Proxy(self) -> IWebProxy: ...
    
    @Proxy.setter
    def Proxy(self, value: IWebProxy) -> None: ...
    
    @property
    def QueryString(self) -> NameValueCollection: ...
    
    @QueryString.setter
    def QueryString(self, value: NameValueCollection) -> None: ...
    
    @property
    def ResponseHeaders(self) -> WebHeaderCollection: ...
    
    @property
    def UseDefaultCredentials(self) -> BooleanType: ...
    
    @UseDefaultCredentials.setter
    def UseDefaultCredentials(self, value: BooleanType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def CancelAsync(self) -> VoidType: ...
    
    @overload
    def DownloadData(self, address: StringType) -> ArrayType[ByteType]: ...
    
    @overload
    def DownloadData(self, address: Uri) -> ArrayType[ByteType]: ...
    
    @overload
    def DownloadDataAsync(self, address: Uri) -> VoidType: ...
    
    @overload
    def DownloadDataAsync(self, address: Uri, userToken: ObjectType) -> VoidType: ...
    
    @overload
    def DownloadDataTaskAsync(self, address: StringType) -> Task[ArrayType[ByteType]]: ...
    
    @overload
    def DownloadDataTaskAsync(self, address: Uri) -> Task[ArrayType[ByteType]]: ...
    
    @overload
    def DownloadFile(self, address: StringType, fileName: StringType) -> VoidType: ...
    
    @overload
    def DownloadFile(self, address: Uri, fileName: StringType) -> VoidType: ...
    
    @overload
    def DownloadFileAsync(self, address: Uri, fileName: StringType) -> VoidType: ...
    
    @overload
    def DownloadFileAsync(self, address: Uri, fileName: StringType, userToken: ObjectType) -> VoidType: ...
    
    @overload
    def DownloadFileTaskAsync(self, address: StringType, fileName: StringType) -> Task: ...
    
    @overload
    def DownloadFileTaskAsync(self, address: Uri, fileName: StringType) -> Task: ...
    
    @overload
    def DownloadString(self, address: StringType) -> StringType: ...
    
    @overload
    def DownloadString(self, address: Uri) -> StringType: ...
    
    @overload
    def DownloadStringAsync(self, address: Uri) -> VoidType: ...
    
    @overload
    def DownloadStringAsync(self, address: Uri, userToken: ObjectType) -> VoidType: ...
    
    @overload
    def DownloadStringTaskAsync(self, address: StringType) -> Task[StringType]: ...
    
    @overload
    def DownloadStringTaskAsync(self, address: Uri) -> Task[StringType]: ...
    
    @overload
    def OpenRead(self, address: StringType) -> Stream: ...
    
    @overload
    def OpenRead(self, address: Uri) -> Stream: ...
    
    @overload
    def OpenReadAsync(self, address: Uri) -> VoidType: ...
    
    @overload
    def OpenReadAsync(self, address: Uri, userToken: ObjectType) -> VoidType: ...
    
    @overload
    def OpenReadTaskAsync(self, address: StringType) -> Task[Stream]: ...
    
    @overload
    def OpenReadTaskAsync(self, address: Uri) -> Task[Stream]: ...
    
    @overload
    def OpenWrite(self, address: StringType) -> Stream: ...
    
    @overload
    def OpenWrite(self, address: Uri) -> Stream: ...
    
    @overload
    def OpenWrite(self, address: StringType, method: StringType) -> Stream: ...
    
    @overload
    def OpenWrite(self, address: Uri, method: StringType) -> Stream: ...
    
    @overload
    def OpenWriteAsync(self, address: Uri) -> VoidType: ...
    
    @overload
    def OpenWriteAsync(self, address: Uri, method: StringType) -> VoidType: ...
    
    @overload
    def OpenWriteAsync(self, address: Uri, method: StringType, userToken: ObjectType) -> VoidType: ...
    
    @overload
    def OpenWriteTaskAsync(self, address: StringType) -> Task[Stream]: ...
    
    @overload
    def OpenWriteTaskAsync(self, address: Uri) -> Task[Stream]: ...
    
    @overload
    def OpenWriteTaskAsync(self, address: StringType, method: StringType) -> Task[Stream]: ...
    
    @overload
    def OpenWriteTaskAsync(self, address: Uri, method: StringType) -> Task[Stream]: ...
    
    @overload
    def UploadData(self, address: StringType, data: ArrayType[ByteType]) -> ArrayType[ByteType]: ...
    
    @overload
    def UploadData(self, address: Uri, data: ArrayType[ByteType]) -> ArrayType[ByteType]: ...
    
    @overload
    def UploadData(self, address: StringType, method: StringType, data: ArrayType[ByteType]) -> ArrayType[ByteType]: ...
    
    @overload
    def UploadData(self, address: Uri, method: StringType, data: ArrayType[ByteType]) -> ArrayType[ByteType]: ...
    
    @overload
    def UploadDataAsync(self, address: Uri, data: ArrayType[ByteType]) -> VoidType: ...
    
    @overload
    def UploadDataAsync(self, address: Uri, method: StringType, data: ArrayType[ByteType]) -> VoidType: ...
    
    @overload
    def UploadDataAsync(self, address: Uri, method: StringType, data: ArrayType[ByteType], userToken: ObjectType) -> VoidType: ...
    
    @overload
    def UploadDataTaskAsync(self, address: StringType, data: ArrayType[ByteType]) -> Task[ArrayType[ByteType]]: ...
    
    @overload
    def UploadDataTaskAsync(self, address: Uri, data: ArrayType[ByteType]) -> Task[ArrayType[ByteType]]: ...
    
    @overload
    def UploadDataTaskAsync(self, address: StringType, method: StringType, data: ArrayType[ByteType]) -> Task[ArrayType[ByteType]]: ...
    
    @overload
    def UploadDataTaskAsync(self, address: Uri, method: StringType, data: ArrayType[ByteType]) -> Task[ArrayType[ByteType]]: ...
    
    @overload
    def UploadFile(self, address: StringType, fileName: StringType) -> ArrayType[ByteType]: ...
    
    @overload
    def UploadFile(self, address: Uri, fileName: StringType) -> ArrayType[ByteType]: ...
    
    @overload
    def UploadFile(self, address: StringType, method: StringType, fileName: StringType) -> ArrayType[ByteType]: ...
    
    @overload
    def UploadFile(self, address: Uri, method: StringType, fileName: StringType) -> ArrayType[ByteType]: ...
    
    @overload
    def UploadFileAsync(self, address: Uri, fileName: StringType) -> VoidType: ...
    
    @overload
    def UploadFileAsync(self, address: Uri, method: StringType, fileName: StringType) -> VoidType: ...
    
    @overload
    def UploadFileAsync(self, address: Uri, method: StringType, fileName: StringType, userToken: ObjectType) -> VoidType: ...
    
    @overload
    def UploadFileTaskAsync(self, address: StringType, fileName: StringType) -> Task[ArrayType[ByteType]]: ...
    
    @overload
    def UploadFileTaskAsync(self, address: Uri, fileName: StringType) -> Task[ArrayType[ByteType]]: ...
    
    @overload
    def UploadFileTaskAsync(self, address: StringType, method: StringType, fileName: StringType) -> Task[ArrayType[ByteType]]: ...
    
    @overload
    def UploadFileTaskAsync(self, address: Uri, method: StringType, fileName: StringType) -> Task[ArrayType[ByteType]]: ...
    
    @overload
    def UploadString(self, address: StringType, data: StringType) -> StringType: ...
    
    @overload
    def UploadString(self, address: Uri, data: StringType) -> StringType: ...
    
    @overload
    def UploadString(self, address: StringType, method: StringType, data: StringType) -> StringType: ...
    
    @overload
    def UploadString(self, address: Uri, method: StringType, data: StringType) -> StringType: ...
    
    @overload
    def UploadStringAsync(self, address: Uri, data: StringType) -> VoidType: ...
    
    @overload
    def UploadStringAsync(self, address: Uri, method: StringType, data: StringType) -> VoidType: ...
    
    @overload
    def UploadStringAsync(self, address: Uri, method: StringType, data: StringType, userToken: ObjectType) -> VoidType: ...
    
    @overload
    def UploadStringTaskAsync(self, address: StringType, data: StringType) -> Task[StringType]: ...
    
    @overload
    def UploadStringTaskAsync(self, address: Uri, data: StringType) -> Task[StringType]: ...
    
    @overload
    def UploadStringTaskAsync(self, address: StringType, method: StringType, data: StringType) -> Task[StringType]: ...
    
    @overload
    def UploadStringTaskAsync(self, address: Uri, method: StringType, data: StringType) -> Task[StringType]: ...
    
    @overload
    def UploadValues(self, address: StringType, data: NameValueCollection) -> ArrayType[ByteType]: ...
    
    @overload
    def UploadValues(self, address: Uri, data: NameValueCollection) -> ArrayType[ByteType]: ...
    
    @overload
    def UploadValues(self, address: StringType, method: StringType, data: NameValueCollection) -> ArrayType[ByteType]: ...
    
    @overload
    def UploadValues(self, address: Uri, method: StringType, data: NameValueCollection) -> ArrayType[ByteType]: ...
    
    @overload
    def UploadValuesAsync(self, address: Uri, data: NameValueCollection) -> VoidType: ...
    
    @overload
    def UploadValuesAsync(self, address: Uri, method: StringType, data: NameValueCollection) -> VoidType: ...
    
    @overload
    def UploadValuesAsync(self, address: Uri, method: StringType, data: NameValueCollection, userToken: ObjectType) -> VoidType: ...
    
    @overload
    def UploadValuesTaskAsync(self, address: StringType, data: NameValueCollection) -> Task[ArrayType[ByteType]]: ...
    
    @overload
    def UploadValuesTaskAsync(self, address: StringType, method: StringType, data: NameValueCollection) -> Task[ArrayType[ByteType]]: ...
    
    @overload
    def UploadValuesTaskAsync(self, address: Uri, data: NameValueCollection) -> Task[ArrayType[ByteType]]: ...
    
    @overload
    def UploadValuesTaskAsync(self, address: Uri, method: StringType, data: NameValueCollection) -> Task[ArrayType[ByteType]]: ...
    
    def add_DownloadDataCompleted(self, value: DownloadDataCompletedEventHandler) -> VoidType: ...
    
    def add_DownloadFileCompleted(self, value: AsyncCompletedEventHandler) -> VoidType: ...
    
    def add_DownloadProgressChanged(self, value: DownloadProgressChangedEventHandler) -> VoidType: ...
    
    def add_DownloadStringCompleted(self, value: DownloadStringCompletedEventHandler) -> VoidType: ...
    
    def add_OpenReadCompleted(self, value: OpenReadCompletedEventHandler) -> VoidType: ...
    
    def add_OpenWriteCompleted(self, value: OpenWriteCompletedEventHandler) -> VoidType: ...
    
    def add_UploadDataCompleted(self, value: UploadDataCompletedEventHandler) -> VoidType: ...
    
    def add_UploadFileCompleted(self, value: UploadFileCompletedEventHandler) -> VoidType: ...
    
    def add_UploadProgressChanged(self, value: UploadProgressChangedEventHandler) -> VoidType: ...
    
    def add_UploadStringCompleted(self, value: UploadStringCompletedEventHandler) -> VoidType: ...
    
    def add_UploadValuesCompleted(self, value: UploadValuesCompletedEventHandler) -> VoidType: ...
    
    def add_WriteStreamClosed(self, value: WriteStreamClosedEventHandler) -> VoidType: ...
    
    def get_AllowReadStreamBuffering(self) -> BooleanType: ...
    
    def get_AllowWriteStreamBuffering(self) -> BooleanType: ...
    
    def get_BaseAddress(self) -> StringType: ...
    
    def get_CachePolicy(self) -> RequestCachePolicy: ...
    
    def get_Credentials(self) -> ICredentials: ...
    
    def get_Encoding(self) -> Encoding: ...
    
    def get_Headers(self) -> WebHeaderCollection: ...
    
    def get_IsBusy(self) -> BooleanType: ...
    
    def get_Proxy(self) -> IWebProxy: ...
    
    def get_QueryString(self) -> NameValueCollection: ...
    
    def get_ResponseHeaders(self) -> WebHeaderCollection: ...
    
    def get_UseDefaultCredentials(self) -> BooleanType: ...
    
    def remove_DownloadDataCompleted(self, value: DownloadDataCompletedEventHandler) -> VoidType: ...
    
    def remove_DownloadFileCompleted(self, value: AsyncCompletedEventHandler) -> VoidType: ...
    
    def remove_DownloadProgressChanged(self, value: DownloadProgressChangedEventHandler) -> VoidType: ...
    
    def remove_DownloadStringCompleted(self, value: DownloadStringCompletedEventHandler) -> VoidType: ...
    
    def remove_OpenReadCompleted(self, value: OpenReadCompletedEventHandler) -> VoidType: ...
    
    def remove_OpenWriteCompleted(self, value: OpenWriteCompletedEventHandler) -> VoidType: ...
    
    def remove_UploadDataCompleted(self, value: UploadDataCompletedEventHandler) -> VoidType: ...
    
    def remove_UploadFileCompleted(self, value: UploadFileCompletedEventHandler) -> VoidType: ...
    
    def remove_UploadProgressChanged(self, value: UploadProgressChangedEventHandler) -> VoidType: ...
    
    def remove_UploadStringCompleted(self, value: UploadStringCompletedEventHandler) -> VoidType: ...
    
    def remove_UploadValuesCompleted(self, value: UploadValuesCompletedEventHandler) -> VoidType: ...
    
    def remove_WriteStreamClosed(self, value: WriteStreamClosedEventHandler) -> VoidType: ...
    
    def set_AllowReadStreamBuffering(self, value: BooleanType) -> VoidType: ...
    
    def set_AllowWriteStreamBuffering(self, value: BooleanType) -> VoidType: ...
    
    def set_BaseAddress(self, value: StringType) -> VoidType: ...
    
    def set_CachePolicy(self, value: RequestCachePolicy) -> VoidType: ...
    
    def set_Credentials(self, value: ICredentials) -> VoidType: ...
    
    def set_Encoding(self, value: Encoding) -> VoidType: ...
    
    def set_Headers(self, value: WebHeaderCollection) -> VoidType: ...
    
    def set_Proxy(self, value: IWebProxy) -> VoidType: ...
    
    def set_QueryString(self, value: NameValueCollection) -> VoidType: ...
    
    def set_UseDefaultCredentials(self, value: BooleanType) -> VoidType: ...
    
    # ---------- Events ---------- #
    
    DownloadDataCompleted: EventType[DownloadDataCompletedEventHandler] = ...
    
    DownloadFileCompleted: EventType[AsyncCompletedEventHandler] = ...
    
    DownloadProgressChanged: EventType[DownloadProgressChangedEventHandler] = ...
    
    DownloadStringCompleted: EventType[DownloadStringCompletedEventHandler] = ...
    
    OpenReadCompleted: EventType[OpenReadCompletedEventHandler] = ...
    
    OpenWriteCompleted: EventType[OpenWriteCompletedEventHandler] = ...
    
    UploadDataCompleted: EventType[UploadDataCompletedEventHandler] = ...
    
    UploadFileCompleted: EventType[UploadFileCompletedEventHandler] = ...
    
    UploadProgressChanged: EventType[UploadProgressChangedEventHandler] = ...
    
    UploadStringCompleted: EventType[UploadStringCompletedEventHandler] = ...
    
    UploadValuesCompleted: EventType[UploadValuesCompletedEventHandler] = ...
    
    WriteStreamClosed: EventType[WriteStreamClosedEventHandler] = ...
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class WebException(InvalidOperationException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    @overload
    def __init__(self, message: StringType, status: WebExceptionStatus): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception, status: WebExceptionStatus, response: WebResponse): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Response(self) -> WebResponse: ...
    
    @property
    def Status(self) -> WebExceptionStatus: ...
    
    # ---------- Methods ---------- #
    
    def GetObjectData(self, serializationInfo: SerializationInfo, streamingContext: StreamingContext) -> VoidType: ...
    
    def get_Response(self) -> WebResponse: ...
    
    def get_Status(self) -> WebExceptionStatus: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class WebExceptionMapping(ABC, ObjectType):
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


class WebHeaderCollection(NameValueCollection, ICollection, IEnumerable, ISerializable, IDeserializationCallback):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AllKeys(self) -> ArrayType[StringType]: ...
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def Item(self) -> StringType: ...
    
    @Item.setter
    def Item(self, value: StringType) -> None: ...
    
    @property
    def Item(self) -> StringType: ...
    
    @Item.setter
    def Item(self, value: StringType) -> None: ...
    
    @property
    def Keys(self) -> KeysCollection: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Add(self, header: HttpRequestHeader, value: StringType) -> VoidType: ...
    
    @overload
    def Add(self, header: HttpResponseHeader, value: StringType) -> VoidType: ...
    
    @overload
    def Add(self, name: StringType, value: StringType) -> VoidType: ...
    
    @overload
    def Add(self, header: StringType) -> VoidType: ...
    
    def Clear(self) -> VoidType: ...
    
    @overload
    def Get(self, name: StringType) -> StringType: ...
    
    @overload
    def Get(self, index: IntType) -> StringType: ...
    
    def GetEnumerator(self) -> IEnumerator: ...
    
    def GetKey(self, index: IntType) -> StringType: ...
    
    def GetObjectData(self, serializationInfo: SerializationInfo, streamingContext: StreamingContext) -> VoidType: ...
    
    @overload
    def GetValues(self, index: IntType) -> ArrayType[StringType]: ...
    
    @overload
    def GetValues(self, header: StringType) -> ArrayType[StringType]: ...
    
    @staticmethod
    @overload
    def IsRestricted(headerName: StringType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def IsRestricted(headerName: StringType, response: BooleanType) -> BooleanType: ...
    
    def OnDeserialization(self, sender: ObjectType) -> VoidType: ...
    
    @overload
    def Remove(self, header: HttpRequestHeader) -> VoidType: ...
    
    @overload
    def Remove(self, header: HttpResponseHeader) -> VoidType: ...
    
    @overload
    def Remove(self, name: StringType) -> VoidType: ...
    
    @overload
    def Set(self, header: HttpRequestHeader, value: StringType) -> VoidType: ...
    
    @overload
    def Set(self, header: HttpResponseHeader, value: StringType) -> VoidType: ...
    
    @overload
    def Set(self, name: StringType, value: StringType) -> VoidType: ...
    
    def ToByteArray(self) -> ArrayType[ByteType]: ...
    
    def ToString(self) -> StringType: ...
    
    def get_AllKeys(self) -> ArrayType[StringType]: ...
    
    def get_Count(self) -> IntType: ...
    
    @overload
    def get_Item(self, header: HttpRequestHeader) -> StringType: ...
    
    @overload
    def get_Item(self, header: HttpResponseHeader) -> StringType: ...
    
    def get_Keys(self) -> KeysCollection: ...
    
    @overload
    def set_Item(self, header: HttpRequestHeader, value: StringType) -> VoidType: ...
    
    @overload
    def set_Item(self, header: HttpResponseHeader, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class WebPermission(CodeAccessPermission, IPermission, ISecurityEncodable, IStackWalk, IUnrestrictedPermission):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, state: PermissionState): ...
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, access: NetworkAccess, uriRegex: Regex): ...
    
    @overload
    def __init__(self, access: NetworkAccess, uriString: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AcceptList(self) -> IEnumerator: ...
    
    @property
    def ConnectList(self) -> IEnumerator: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def AddPermission(self, access: NetworkAccess, uriString: StringType) -> VoidType: ...
    
    @overload
    def AddPermission(self, access: NetworkAccess, uriRegex: Regex) -> VoidType: ...
    
    def Copy(self) -> IPermission: ...
    
    def FromXml(self, securityElement: SecurityElement) -> VoidType: ...
    
    def Intersect(self, target: IPermission) -> IPermission: ...
    
    def IsSubsetOf(self, target: IPermission) -> BooleanType: ...
    
    def IsUnrestricted(self) -> BooleanType: ...
    
    def ToXml(self) -> SecurityElement: ...
    
    def Union(self, target: IPermission) -> IPermission: ...
    
    def get_AcceptList(self) -> IEnumerator: ...
    
    def get_ConnectList(self) -> IEnumerator: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class WebPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, action: SecurityAction): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Accept(self) -> StringType: ...
    
    @Accept.setter
    def Accept(self, value: StringType) -> None: ...
    
    @property
    def AcceptPattern(self) -> StringType: ...
    
    @AcceptPattern.setter
    def AcceptPattern(self, value: StringType) -> None: ...
    
    @property
    def Connect(self) -> StringType: ...
    
    @Connect.setter
    def Connect(self, value: StringType) -> None: ...
    
    @property
    def ConnectPattern(self) -> StringType: ...
    
    @ConnectPattern.setter
    def ConnectPattern(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def CreatePermission(self) -> IPermission: ...
    
    def get_Accept(self) -> StringType: ...
    
    def get_AcceptPattern(self) -> StringType: ...
    
    def get_Connect(self) -> StringType: ...
    
    def get_ConnectPattern(self) -> StringType: ...
    
    def set_Accept(self, value: StringType) -> VoidType: ...
    
    def set_AcceptPattern(self, value: StringType) -> VoidType: ...
    
    def set_Connect(self, value: StringType) -> VoidType: ...
    
    def set_ConnectPattern(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class WebProxy(ObjectType, IAutoWebProxy, IWebProxy, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, Address: Uri): ...
    
    @overload
    def __init__(self, Address: Uri, BypassOnLocal: BooleanType): ...
    
    @overload
    def __init__(self, Address: Uri, BypassOnLocal: BooleanType, BypassList: ArrayType[StringType]): ...
    
    @overload
    def __init__(self, Address: Uri, BypassOnLocal: BooleanType, BypassList: ArrayType[StringType], Credentials: ICredentials): ...
    
    @overload
    def __init__(self, Host: StringType, Port: IntType): ...
    
    @overload
    def __init__(self, Address: StringType): ...
    
    @overload
    def __init__(self, Address: StringType, BypassOnLocal: BooleanType): ...
    
    @overload
    def __init__(self, Address: StringType, BypassOnLocal: BooleanType, BypassList: ArrayType[StringType]): ...
    
    @overload
    def __init__(self, Address: StringType, BypassOnLocal: BooleanType, BypassList: ArrayType[StringType], Credentials: ICredentials): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Address(self) -> Uri: ...
    
    @Address.setter
    def Address(self, value: Uri) -> None: ...
    
    @property
    def BypassArrayList(self) -> ArrayList: ...
    
    @property
    def BypassList(self) -> ArrayType[StringType]: ...
    
    @BypassList.setter
    def BypassList(self, value: ArrayType[StringType]) -> None: ...
    
    @property
    def BypassProxyOnLocal(self) -> BooleanType: ...
    
    @BypassProxyOnLocal.setter
    def BypassProxyOnLocal(self, value: BooleanType) -> None: ...
    
    @property
    def Credentials(self) -> ICredentials: ...
    
    @Credentials.setter
    def Credentials(self, value: ICredentials) -> None: ...
    
    @property
    def UseDefaultCredentials(self) -> BooleanType: ...
    
    @UseDefaultCredentials.setter
    def UseDefaultCredentials(self, value: BooleanType) -> None: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def GetDefaultProxy() -> WebProxy: ...
    
    def GetProxy(self, destination: Uri) -> Uri: ...
    
    def IsBypassed(self, host: Uri) -> BooleanType: ...
    
    def get_Address(self) -> Uri: ...
    
    def get_BypassArrayList(self) -> ArrayList: ...
    
    def get_BypassList(self) -> ArrayType[StringType]: ...
    
    def get_BypassProxyOnLocal(self) -> BooleanType: ...
    
    def get_Credentials(self) -> ICredentials: ...
    
    def get_UseDefaultCredentials(self) -> BooleanType: ...
    
    def set_Address(self, value: Uri) -> VoidType: ...
    
    def set_BypassList(self, value: ArrayType[StringType]) -> VoidType: ...
    
    def set_BypassProxyOnLocal(self, value: BooleanType) -> VoidType: ...
    
    def set_Credentials(self, value: ICredentials) -> VoidType: ...
    
    def set_UseDefaultCredentials(self, value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class WebProxyData(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class WebProxyDataBuilder(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Build(self) -> WebProxyData: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class WebProxyScriptHelper(ObjectType, IReflect):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def dnsDomainIs(self, host: StringType, domain: StringType) -> BooleanType: ...
    
    def dnsDomainLevels(self, host: StringType) -> IntType: ...
    
    def dnsResolve(self, host: StringType) -> StringType: ...
    
    def dnsResolveEx(self, host: StringType) -> StringType: ...
    
    def getClientVersion(self) -> StringType: ...
    
    def isInNet(self, host: StringType, pattern: StringType, mask: StringType) -> BooleanType: ...
    
    def isInNetEx(self, ipAddress: StringType, ipPrefix: StringType) -> BooleanType: ...
    
    def isPlainHostName(self, hostName: StringType) -> BooleanType: ...
    
    def isResolvable(self, host: StringType) -> BooleanType: ...
    
    def isResolvableEx(self, host: StringType) -> BooleanType: ...
    
    def localHostOrDomainIs(self, host: StringType, hostDom: StringType) -> BooleanType: ...
    
    def myIpAddress(self) -> StringType: ...
    
    def myIpAddressEx(self) -> StringType: ...
    
    def shExpMatch(self, host: StringType, pattern: StringType) -> BooleanType: ...
    
    def sortIpAddressList(self, IPAddressList: StringType) -> StringType: ...
    
    def weekdayRange(self, wd1: StringType, wd2: ObjectType = System.Reflection.Missing, gmt: ObjectType = System.Reflection.Missing) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class WebRequest(ABC, MarshalByRefObject, ISerializable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def AuthenticationLevel(self) -> AuthenticationLevel: ...
    
    @AuthenticationLevel.setter
    def AuthenticationLevel(self, value: AuthenticationLevel) -> None: ...
    
    @property
    def CachePolicy(self) -> RequestCachePolicy: ...
    
    @CachePolicy.setter
    def CachePolicy(self, value: RequestCachePolicy) -> None: ...
    
    @property
    def ConnectionGroupName(self) -> StringType: ...
    
    @ConnectionGroupName.setter
    def ConnectionGroupName(self, value: StringType) -> None: ...
    
    @property
    def ContentLength(self) -> LongType: ...
    
    @ContentLength.setter
    def ContentLength(self, value: LongType) -> None: ...
    
    @property
    def ContentType(self) -> StringType: ...
    
    @ContentType.setter
    def ContentType(self, value: StringType) -> None: ...
    
    @property
    def CreatorInstance(self) -> IWebRequestCreate: ...
    
    @property
    def Credentials(self) -> ICredentials: ...
    
    @Credentials.setter
    def Credentials(self, value: ICredentials) -> None: ...
    
    @staticmethod
    @property
    def DefaultCachePolicy() -> RequestCachePolicy: ...
    
    @staticmethod
    @DefaultCachePolicy.setter
    def DefaultCachePolicy(value: RequestCachePolicy) -> None: ...
    
    @staticmethod
    @property
    def DefaultWebProxy() -> IWebProxy: ...
    
    @staticmethod
    @DefaultWebProxy.setter
    def DefaultWebProxy(value: IWebProxy) -> None: ...
    
    @property
    def Headers(self) -> WebHeaderCollection: ...
    
    @Headers.setter
    def Headers(self, value: WebHeaderCollection) -> None: ...
    
    @property
    def ImpersonationLevel(self) -> TokenImpersonationLevel: ...
    
    @ImpersonationLevel.setter
    def ImpersonationLevel(self, value: TokenImpersonationLevel) -> None: ...
    
    @property
    def Method(self) -> StringType: ...
    
    @Method.setter
    def Method(self, value: StringType) -> None: ...
    
    @property
    def PreAuthenticate(self) -> BooleanType: ...
    
    @PreAuthenticate.setter
    def PreAuthenticate(self, value: BooleanType) -> None: ...
    
    @property
    def Proxy(self) -> IWebProxy: ...
    
    @Proxy.setter
    def Proxy(self, value: IWebProxy) -> None: ...
    
    @property
    def RequestUri(self) -> Uri: ...
    
    @property
    def Timeout(self) -> IntType: ...
    
    @Timeout.setter
    def Timeout(self, value: IntType) -> None: ...
    
    @property
    def UseDefaultCredentials(self) -> BooleanType: ...
    
    @UseDefaultCredentials.setter
    def UseDefaultCredentials(self, value: BooleanType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Abort(self) -> VoidType: ...
    
    def BeginGetRequestStream(self, callback: AsyncCallback, state: ObjectType) -> IAsyncResult: ...
    
    def BeginGetResponse(self, callback: AsyncCallback, state: ObjectType) -> IAsyncResult: ...
    
    @staticmethod
    @overload
    def Create(requestUriString: StringType) -> WebRequest: ...
    
    @staticmethod
    @overload
    def Create(requestUri: Uri) -> WebRequest: ...
    
    @staticmethod
    def CreateDefault(requestUri: Uri) -> WebRequest: ...
    
    @staticmethod
    @overload
    def CreateHttp(requestUriString: StringType) -> HttpWebRequest: ...
    
    @staticmethod
    @overload
    def CreateHttp(requestUri: Uri) -> HttpWebRequest: ...
    
    def EndGetRequestStream(self, asyncResult: IAsyncResult) -> Stream: ...
    
    def EndGetResponse(self, asyncResult: IAsyncResult) -> WebResponse: ...
    
    def GetRequestStream(self) -> Stream: ...
    
    def GetRequestStreamAsync(self) -> Task[Stream]: ...
    
    def GetResponse(self) -> WebResponse: ...
    
    def GetResponseAsync(self) -> Task[WebResponse]: ...
    
    @staticmethod
    def GetSystemWebProxy() -> IWebProxy: ...
    
    @staticmethod
    def RegisterPortableWebRequestCreator(creator: IWebRequestCreate) -> VoidType: ...
    
    @staticmethod
    def RegisterPrefix(prefix: StringType, creator: IWebRequestCreate) -> BooleanType: ...
    
    def get_AuthenticationLevel(self) -> AuthenticationLevel: ...
    
    def get_CachePolicy(self) -> RequestCachePolicy: ...
    
    def get_ConnectionGroupName(self) -> StringType: ...
    
    def get_ContentLength(self) -> LongType: ...
    
    def get_ContentType(self) -> StringType: ...
    
    def get_CreatorInstance(self) -> IWebRequestCreate: ...
    
    def get_Credentials(self) -> ICredentials: ...
    
    @staticmethod
    def get_DefaultCachePolicy() -> RequestCachePolicy: ...
    
    @staticmethod
    def get_DefaultWebProxy() -> IWebProxy: ...
    
    def get_Headers(self) -> WebHeaderCollection: ...
    
    def get_ImpersonationLevel(self) -> TokenImpersonationLevel: ...
    
    def get_Method(self) -> StringType: ...
    
    def get_PreAuthenticate(self) -> BooleanType: ...
    
    def get_Proxy(self) -> IWebProxy: ...
    
    def get_RequestUri(self) -> Uri: ...
    
    def get_Timeout(self) -> IntType: ...
    
    def get_UseDefaultCredentials(self) -> BooleanType: ...
    
    def set_AuthenticationLevel(self, value: AuthenticationLevel) -> VoidType: ...
    
    def set_CachePolicy(self, value: RequestCachePolicy) -> VoidType: ...
    
    def set_ConnectionGroupName(self, value: StringType) -> VoidType: ...
    
    def set_ContentLength(self, value: LongType) -> VoidType: ...
    
    def set_ContentType(self, value: StringType) -> VoidType: ...
    
    def set_Credentials(self, value: ICredentials) -> VoidType: ...
    
    @staticmethod
    def set_DefaultCachePolicy(value: RequestCachePolicy) -> VoidType: ...
    
    @staticmethod
    def set_DefaultWebProxy(value: IWebProxy) -> VoidType: ...
    
    def set_Headers(self, value: WebHeaderCollection) -> VoidType: ...
    
    def set_ImpersonationLevel(self, value: TokenImpersonationLevel) -> VoidType: ...
    
    def set_Method(self, value: StringType) -> VoidType: ...
    
    def set_PreAuthenticate(self, value: BooleanType) -> VoidType: ...
    
    def set_Proxy(self, value: IWebProxy) -> VoidType: ...
    
    def set_Timeout(self, value: IntType) -> VoidType: ...
    
    def set_UseDefaultCredentials(self, value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class WebRequestMethods(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    
    # ---------- Sub Classes ---------- #
    
    class Ftp(ABC, ObjectType):
        # ---------- Fields ---------- #
        
        @staticmethod
        @property
        def AppendFile() -> StringType: ...
        
        @staticmethod
        @property
        def DeleteFile() -> StringType: ...
        
        @staticmethod
        @property
        def DownloadFile() -> StringType: ...
        
        @staticmethod
        @property
        def GetDateTimestamp() -> StringType: ...
        
        @staticmethod
        @property
        def GetFileSize() -> StringType: ...
        
        @staticmethod
        @property
        def ListDirectory() -> StringType: ...
        
        @staticmethod
        @property
        def ListDirectoryDetails() -> StringType: ...
        
        @staticmethod
        @property
        def MakeDirectory() -> StringType: ...
        
        @staticmethod
        @property
        def PrintWorkingDirectory() -> StringType: ...
        
        @staticmethod
        @property
        def RemoveDirectory() -> StringType: ...
        
        @staticmethod
        @property
        def Rename() -> StringType: ...
        
        @staticmethod
        @property
        def UploadFile() -> StringType: ...
        
        @staticmethod
        @property
        def UploadFileWithUniqueName() -> StringType: ...
        
        # No Constructors
        
        # No Properties
        
        # No Methods
        
        # No Events
        
        # No Sub Classes
        
        # No Sub Structs
        
        # No Sub Interfaces
        
        # No Sub Enums
    
    
    class Http(ABC, ObjectType):
        # ---------- Fields ---------- #
        
        @staticmethod
        @property
        def Connect() -> StringType: ...
        
        @staticmethod
        @property
        def Get() -> StringType: ...
        
        @staticmethod
        @property
        def Head() -> StringType: ...
        
        @staticmethod
        @property
        def MkCol() -> StringType: ...
        
        @staticmethod
        @property
        def Post() -> StringType: ...
        
        @staticmethod
        @property
        def Put() -> StringType: ...
        
        # No Constructors
        
        # No Properties
        
        # No Methods
        
        # No Events
        
        # No Sub Classes
        
        # No Sub Structs
        
        # No Sub Interfaces
        
        # No Sub Enums
    
    
    class File(ABC, ObjectType):
        # ---------- Fields ---------- #
        
        @staticmethod
        @property
        def DownloadFile() -> StringType: ...
        
        @staticmethod
        @property
        def UploadFile() -> StringType: ...
        
        # No Constructors
        
        # No Properties
        
        # No Methods
        
        # No Events
        
        # No Sub Classes
        
        # No Sub Structs
        
        # No Sub Interfaces
        
        # No Sub Enums
    
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class WebRequestPrefixElement(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def Prefix(self) -> StringType: ...
    
    @Prefix.setter
    def Prefix(self, value: StringType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, P: StringType, creatorType: TypeType): ...
    
    @overload
    def __init__(self, P: StringType, C: IWebRequestCreate): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Creator(self) -> IWebRequestCreate: ...
    
    @Creator.setter
    def Creator(self, value: IWebRequestCreate) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Creator(self) -> IWebRequestCreate: ...
    
    def set_Creator(self, value: IWebRequestCreate) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class WebResponse(ABC, MarshalByRefObject, ISerializable, IDisposable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def ContentLength(self) -> LongType: ...
    
    @ContentLength.setter
    def ContentLength(self, value: LongType) -> None: ...
    
    @property
    def ContentType(self) -> StringType: ...
    
    @ContentType.setter
    def ContentType(self, value: StringType) -> None: ...
    
    @property
    def Headers(self) -> WebHeaderCollection: ...
    
    @property
    def IsFromCache(self) -> BooleanType: ...
    
    @property
    def IsMutuallyAuthenticated(self) -> BooleanType: ...
    
    @property
    def ResponseUri(self) -> Uri: ...
    
    @property
    def SupportsHeaders(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    def Dispose(self) -> VoidType: ...
    
    def GetResponseStream(self) -> Stream: ...
    
    def get_ContentLength(self) -> LongType: ...
    
    def get_ContentType(self) -> StringType: ...
    
    def get_Headers(self) -> WebHeaderCollection: ...
    
    def get_IsFromCache(self) -> BooleanType: ...
    
    def get_IsMutuallyAuthenticated(self) -> BooleanType: ...
    
    def get_ResponseUri(self) -> Uri: ...
    
    def get_SupportsHeaders(self) -> BooleanType: ...
    
    def set_ContentLength(self, value: LongType) -> VoidType: ...
    
    def set_ContentType(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class WebSocketHttpRequestCreator(ObjectType, IWebRequestCreate):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, usingHttps: BooleanType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Create(self, Uri: Uri) -> WebRequest: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class WebUtility(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    @overload
    def HtmlDecode(value: StringType) -> StringType: ...
    
    @staticmethod
    @overload
    def HtmlDecode(value: StringType, output: TextWriter) -> VoidType: ...
    
    @staticmethod
    @overload
    def HtmlEncode(value: StringType) -> StringType: ...
    
    @staticmethod
    @overload
    def HtmlEncode(value: StringType, output: TextWriter) -> VoidType: ...
    
    @staticmethod
    def UrlDecode(encodedValue: StringType) -> StringType: ...
    
    @staticmethod
    def UrlDecodeToBytes(encodedValue: ArrayType[ByteType], offset: IntType, count: IntType) -> ArrayType[ByteType]: ...
    
    @staticmethod
    def UrlEncode(value: StringType) -> StringType: ...
    
    @staticmethod
    def UrlEncodeToBytes(value: ArrayType[ByteType], offset: IntType, count: IntType) -> ArrayType[ByteType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Win32(ABC, ObjectType):
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


class WinHttpWebProxyBuilder(WebProxyDataBuilder):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class WinHttpWebProxyFinder(BaseWebProxyFinder, IWebProxyFinder, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, engine: AutoWebProxyScriptEngine): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Abort(self) -> VoidType: ...
    
    def GetProxies(self, destination: Uri, proxyList: IList[StringType]) -> Tuple[BooleanType, IList[StringType]]: ...
    
    def Reset(self) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class WorkerAsyncResult(LazyAsyncResult, IAsyncResult):
    # ---------- Fields ---------- #
    
    @property
    def Buffer(self) -> ArrayType[ByteType]: ...
    
    @Buffer.setter
    def Buffer(self, value: ArrayType[ByteType]) -> None: ...
    
    @property
    def End(self) -> IntType: ...
    
    @End.setter
    def End(self, value: IntType) -> None: ...
    
    @property
    def HandshakeDone(self) -> BooleanType: ...
    
    @HandshakeDone.setter
    def HandshakeDone(self, value: BooleanType) -> None: ...
    
    @property
    def HeaderDone(self) -> BooleanType: ...
    
    @HeaderDone.setter
    def HeaderDone(self, value: BooleanType) -> None: ...
    
    @property
    def IsWrite(self) -> BooleanType: ...
    
    @IsWrite.setter
    def IsWrite(self, value: BooleanType) -> None: ...
    
    @property
    def Offset(self) -> IntType: ...
    
    @Offset.setter
    def Offset(self, value: IntType) -> None: ...
    
    @property
    def ParentResult(self) -> WorkerAsyncResult: ...
    
    @ParentResult.setter
    def ParentResult(self, value: WorkerAsyncResult) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self, asyncObject: ObjectType, asyncState: ObjectType, savedAsyncCallback: AsyncCallback, buffer: ArrayType[ByteType], offset: IntType, end: IntType): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class WriteStreamClosedEventArgs(EventArgs):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Error(self) -> Exception: ...
    
    # ---------- Methods ---------- #
    
    def get_Error(self) -> Exception: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class WriteStreamClosedEventHandler(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, sender: ObjectType, e: WriteStreamClosedEventArgs, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, sender: ObjectType, e: WriteStreamClosedEventArgs) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# ---------- Structs ---------- #

class AddressInfo(ValueType):
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


class AuthIdentity(ValueType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def ToString(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Bindings(ValueType):
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


class Blob(ValueType):
    # ---------- Fields ---------- #
    
    @property
    def cbSize(self) -> IntType: ...
    
    @cbSize.setter
    def cbSize(self, value: IntType) -> None: ...
    
    @property
    def pBlobData(self) -> IntType: ...
    
    @pBlobData.setter
    def pBlobData(self, value: IntType) -> None: ...
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CertEnhKeyUse(ValueType):
    # ---------- Fields ---------- #
    
    @property
    def cUsageIdentifier(self) -> UIntType: ...
    
    @cUsageIdentifier.setter
    def cUsageIdentifier(self, value: UIntType) -> None: ...
    
    @property
    def rgpszUsageIdentifier(self) -> VoidType: ...
    
    @rgpszUsageIdentifier.setter
    def rgpszUsageIdentifier(self, value: VoidType) -> None: ...
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CertUsageMatch(ValueType):
    # ---------- Fields ---------- #
    
    @property
    def Usage(self) -> CertEnhKeyUse: ...
    
    @Usage.setter
    def Usage(self, value: CertEnhKeyUse) -> None: ...
    
    @property
    def dwType(self) -> CertUsage: ...
    
    @dwType.setter
    def dwType(self, value: CertUsage) -> None: ...
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ChainParameters(ValueType):
    # ---------- Fields ---------- #
    
    @property
    def BoolCheckRevocationFreshnessTime(self) -> IntType: ...
    
    @BoolCheckRevocationFreshnessTime.setter
    def BoolCheckRevocationFreshnessTime(self, value: IntType) -> None: ...
    
    @property
    def RequestedIssuancePolicy(self) -> CertUsageMatch: ...
    
    @RequestedIssuancePolicy.setter
    def RequestedIssuancePolicy(self, value: CertUsageMatch) -> None: ...
    
    @property
    def RequestedUsage(self) -> CertUsageMatch: ...
    
    @RequestedUsage.setter
    def RequestedUsage(self, value: CertUsageMatch) -> None: ...
    
    @property
    def RevocationFreshnessTime(self) -> UIntType: ...
    
    @RevocationFreshnessTime.setter
    def RevocationFreshnessTime(self, value: UIntType) -> None: ...
    
    @staticmethod
    @property
    def StructSize() -> UIntType: ...
    
    @property
    def UrlRetrievalTimeout(self) -> UIntType: ...
    
    @UrlRetrievalTimeout.setter
    def UrlRetrievalTimeout(self, value: UIntType) -> None: ...
    
    @property
    def cbSize(self) -> UIntType: ...
    
    @cbSize.setter
    def cbSize(self, value: UIntType) -> None: ...
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ChainPolicyParameter(ValueType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def StructSize() -> UIntType: ...
    
    @property
    def cbSize(self) -> UIntType: ...
    
    @cbSize.setter
    def cbSize(self, value: UIntType) -> None: ...
    
    @property
    def dwFlags(self) -> UIntType: ...
    
    @dwFlags.setter
    def dwFlags(self, value: UIntType) -> None: ...
    
    @property
    def pvExtraPolicyPara(self) -> SSL_EXTRA_CERT_CHAIN_POLICY_PARA: ...
    
    @pvExtraPolicyPara.setter
    def pvExtraPolicyPara(self, value: SSL_EXTRA_CERT_CHAIN_POLICY_PARA) -> None: ...
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ChainPolicyStatus(ValueType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def StructSize() -> UIntType: ...
    
    @property
    def cbSize(self) -> UIntType: ...
    
    @cbSize.setter
    def cbSize(self, value: UIntType) -> None: ...
    
    @property
    def dwError(self) -> UIntType: ...
    
    @dwError.setter
    def dwError(self, value: UIntType) -> None: ...
    
    @property
    def lChainIndex(self) -> UIntType: ...
    
    @lChainIndex.setter
    def lChainIndex(self, value: UIntType) -> None: ...
    
    @property
    def lElementIndex(self) -> UIntType: ...
    
    @lElementIndex.setter
    def lElementIndex(self, value: UIntType) -> None: ...
    
    @property
    def pvExtraPolicyStatus(self) -> VoidType: ...
    
    @pvExtraPolicyStatus.setter
    def pvExtraPolicyStatus(self, value: VoidType) -> None: ...
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class HeaderVariantInfo(ValueType):
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


class IPMulticastRequest(ValueType):
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


class IPv6MulticastRequest(ValueType):
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


class InterlockedGate(ValueType):
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


class IssuerListInfoEx(ValueType):
    # ---------- Fields ---------- #
    
    @property
    def aIssuers(self) -> SafeHandle: ...
    
    @aIssuers.setter
    def aIssuers(self, value: SafeHandle) -> None: ...
    
    @property
    def cIssuers(self) -> UIntType: ...
    
    @cIssuers.setter
    def cIssuers(self, value: UIntType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self, handle: SafeHandle, nativeBuffer: ArrayType[ByteType]): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Linger(ValueType):
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


class NegotiationInfo(ValueType):
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


class SSL_EXTRA_CERT_CHAIN_POLICY_PARA(ValueType):
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


class SSPIHandle(ValueType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def IsZero(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def ToString(self) -> StringType: ...
    
    def get_IsZero(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SecureCredential(ValueType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def CurrentVersion() -> IntType: ...
    
    @property
    def cCreds(self) -> IntType: ...
    
    @cCreds.setter
    def cCreds(self, value: IntType) -> None: ...
    
    @property
    def cMappers(self) -> IntType: ...
    
    @cMappers.setter
    def cMappers(self, value: IntType) -> None: ...
    
    @property
    def cSupportedAlgs(self) -> IntType: ...
    
    @cSupportedAlgs.setter
    def cSupportedAlgs(self, value: IntType) -> None: ...
    
    @property
    def certContextArray(self) -> NIntType: ...
    
    @certContextArray.setter
    def certContextArray(self, value: NIntType) -> None: ...
    
    @property
    def dwFlags(self) -> Flags: ...
    
    @dwFlags.setter
    def dwFlags(self, value: Flags) -> None: ...
    
    @property
    def dwMaximumCipherStrength(self) -> IntType: ...
    
    @dwMaximumCipherStrength.setter
    def dwMaximumCipherStrength(self, value: IntType) -> None: ...
    
    @property
    def dwMinimumCipherStrength(self) -> IntType: ...
    
    @dwMinimumCipherStrength.setter
    def dwMinimumCipherStrength(self, value: IntType) -> None: ...
    
    @property
    def dwSessionLifespan(self) -> IntType: ...
    
    @dwSessionLifespan.setter
    def dwSessionLifespan(self, value: IntType) -> None: ...
    
    @property
    def grbitEnabledProtocols(self) -> SchProtocols: ...
    
    @grbitEnabledProtocols.setter
    def grbitEnabledProtocols(self, value: SchProtocols) -> None: ...
    
    @property
    def reserved(self) -> IntType: ...
    
    @reserved.setter
    def reserved(self, value: IntType) -> None: ...
    
    @property
    def version(self) -> IntType: ...
    
    @version.setter
    def version(self, value: IntType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self, version: IntType, certificate: X509Certificate, flags: Flags, protocols: SchProtocols, policy: EncryptionPolicy): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # ---------- Sub Enums ---------- #
    
    class Flags(Enum):
        Zero: IntType = 0
        NoSystemMapper: IntType = 2
        NoNameCheck: IntType = 4
        ValidateManual: IntType = 8
        NoDefaultCred: IntType = 16
        ValidateAuto: IntType = 32
        SendAuxRecord: IntType = 2097152
        UseStrongCrypto: IntType = 4194304
    


class SecureCredential2(ValueType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def CurrentVersion() -> IntType: ...
    
    @property
    def cCreds(self) -> IntType: ...
    
    @cCreds.setter
    def cCreds(self, value: IntType) -> None: ...
    
    @property
    def cMappers(self) -> IntType: ...
    
    @cMappers.setter
    def cMappers(self, value: IntType) -> None: ...
    
    @property
    def cTlsParameters(self) -> IntType: ...
    
    @cTlsParameters.setter
    def cTlsParameters(self, value: IntType) -> None: ...
    
    @property
    def certContextArray(self) -> VoidType: ...
    
    @certContextArray.setter
    def certContextArray(self, value: VoidType) -> None: ...
    
    @property
    def dwCredformat(self) -> IntType: ...
    
    @dwCredformat.setter
    def dwCredformat(self, value: IntType) -> None: ...
    
    @property
    def dwFlags(self) -> Flags: ...
    
    @dwFlags.setter
    def dwFlags(self, value: Flags) -> None: ...
    
    @property
    def dwSessionLifespan(self) -> IntType: ...
    
    @dwSessionLifespan.setter
    def dwSessionLifespan(self, value: IntType) -> None: ...
    
    @property
    def pTlsParameters(self) -> TlsParamaters: ...
    
    @pTlsParameters.setter
    def pTlsParameters(self, value: TlsParamaters) -> None: ...
    
    @property
    def version(self) -> IntType: ...
    
    @version.setter
    def version(self, value: IntType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self, flags: Flags, protocols: SchProtocols, policy: EncryptionPolicy): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # ---------- Sub Enums ---------- #
    
    class Flags(Enum):
        Zero: IntType = 0
        NoSystemMapper: IntType = 2
        NoNameCheck: IntType = 4
        ValidateManual: IntType = 8
        NoDefaultCred: IntType = 16
        ValidateAuto: IntType = 32
        SendAuxRecord: IntType = 2097152
        UseStrongCrypto: IntType = 4194304
        UsePresharedKeyOnly: IntType = 8388608
        AllowNullEencryption: IntType = 33554432
    


class SecurityBufferStruct(ValueType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Size() -> IntType: ...
    
    @property
    def count(self) -> IntType: ...
    
    @count.setter
    def count(self, value: IntType) -> None: ...
    
    @property
    def token(self) -> NIntType: ...
    
    @token.setter
    def token(self, value: NIntType) -> None: ...
    
    @property
    def type(self) -> BufferType: ...
    
    @type.setter
    def type(self, value: BufferType) -> None: ...
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SecurityPackageInfo(ValueType):
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


class ShellExpression(ValueType):
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


class TlsParamaters(ValueType):
    # ---------- Fields ---------- #
    
    @property
    def cAlpnIds(self) -> IntType: ...
    
    @cAlpnIds.setter
    def cAlpnIds(self, value: IntType) -> None: ...
    
    @property
    def cDisabledCrypto(self) -> IntType: ...
    
    @cDisabledCrypto.setter
    def cDisabledCrypto(self, value: IntType) -> None: ...
    
    @property
    def dwFlags(self) -> Flags: ...
    
    @dwFlags.setter
    def dwFlags(self, value: Flags) -> None: ...
    
    @property
    def grbitDisabledProtocols(self) -> UIntType: ...
    
    @grbitDisabledProtocols.setter
    def grbitDisabledProtocols(self, value: UIntType) -> None: ...
    
    @property
    def pDisabledCrypto(self) -> NIntType: ...
    
    @pDisabledCrypto.setter
    def pDisabledCrypto(self, value: NIntType) -> None: ...
    
    @property
    def rgstrAlpnIds(self) -> NIntType: ...
    
    @rgstrAlpnIds.setter
    def rgstrAlpnIds(self, value: NIntType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self, protocols: SchProtocols): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # ---------- Sub Enums ---------- #
    
    class Flags(Enum):
        Zero: IntType = 0
        TLS_PARAMS_OPTIONAL: IntType = 1
    


class TunnelStateObject(ValueType):
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


class WSABuffer(ValueType):
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


class WSAData(ValueType):
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


class WebParseError(ValueType):
    # ---------- Fields ---------- #
    
    @property
    def Code(self) -> WebParseErrorCode: ...
    
    @Code.setter
    def Code(self, value: WebParseErrorCode) -> None: ...
    
    @property
    def Section(self) -> WebParseErrorSection: ...
    
    @Section.setter
    def Section(self, value: WebParseErrorSection) -> None: ...
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class WriteHeadersCallbackState(ValueType):
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


class _CERT_CHAIN_ELEMENT(ValueType):
    # ---------- Fields ---------- #
    
    @property
    def cbSize(self) -> UIntType: ...
    
    @cbSize.setter
    def cbSize(self, value: UIntType) -> None: ...
    
    @property
    def pCertContext(self) -> NIntType: ...
    
    @pCertContext.setter
    def pCertContext(self, value: NIntType) -> None: ...
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class hostent(ValueType):
    # ---------- Fields ---------- #
    
    @property
    def h_addr_list(self) -> NIntType: ...
    
    @h_addr_list.setter
    def h_addr_list(self, value: NIntType) -> None: ...
    
    @property
    def h_addrtype(self) -> ShortType: ...
    
    @h_addrtype.setter
    def h_addrtype(self, value: ShortType) -> None: ...
    
    @property
    def h_aliases(self) -> NIntType: ...
    
    @h_aliases.setter
    def h_aliases(self, value: NIntType) -> None: ...
    
    @property
    def h_length(self) -> ShortType: ...
    
    @h_length.setter
    def h_length(self, value: ShortType) -> None: ...
    
    @property
    def h_name(self) -> NIntType: ...
    
    @h_name.setter
    def h_name(self, value: NIntType) -> None: ...
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# ---------- Interfaces ---------- #

class IAuthenticationManager(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def CredentialPolicy(self) -> ICredentialPolicy: ...
    
    @CredentialPolicy.setter
    def CredentialPolicy(self, value: ICredentialPolicy) -> None: ...
    
    @property
    def CustomTargetNameDictionary(self) -> StringDictionary: ...
    
    @property
    def OSSupportsExtendedProtection(self) -> BooleanType: ...
    
    @property
    def RegisteredModules(self) -> IEnumerator: ...
    
    @property
    def SpnDictionary(self) -> SpnDictionary: ...
    
    @property
    def SspSupportsExtendedProtection(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def Authenticate(self, challenge: StringType, request: WebRequest, credentials: ICredentials) -> Authorization: ...
    
    def BindModule(self, uri: Uri, response: Authorization, module: IAuthenticationModule) -> VoidType: ...
    
    def EnsureConfigLoaded(self) -> VoidType: ...
    
    def PreAuthenticate(self, request: WebRequest, credentials: ICredentials) -> Authorization: ...
    
    def Register(self, authenticationModule: IAuthenticationModule) -> VoidType: ...
    
    @overload
    def Unregister(self, authenticationModule: IAuthenticationModule) -> VoidType: ...
    
    @overload
    def Unregister(self, authenticationScheme: StringType) -> VoidType: ...
    
    def get_CredentialPolicy(self) -> ICredentialPolicy: ...
    
    def get_CustomTargetNameDictionary(self) -> StringDictionary: ...
    
    def get_OSSupportsExtendedProtection(self) -> BooleanType: ...
    
    def get_RegisteredModules(self) -> IEnumerator: ...
    
    def get_SpnDictionary(self) -> SpnDictionary: ...
    
    def get_SspSupportsExtendedProtection(self) -> BooleanType: ...
    
    def set_CredentialPolicy(self, value: ICredentialPolicy) -> VoidType: ...
    
    # No Events


class IAuthenticationModule(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def AuthenticationType(self) -> StringType: ...
    
    @property
    def CanPreAuthenticate(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def Authenticate(self, challenge: StringType, request: WebRequest, credentials: ICredentials) -> Authorization: ...
    
    def PreAuthenticate(self, request: WebRequest, credentials: ICredentials) -> Authorization: ...
    
    def get_AuthenticationType(self) -> StringType: ...
    
    def get_CanPreAuthenticate(self) -> BooleanType: ...
    
    # No Events


class IAutoWebProxy(Protocol, IWebProxy):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetProxies(self, destination: Uri) -> ProxyChain: ...
    
    # No Events


class ICertificatePolicy(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def CheckValidationResult(self, srvPoint: ServicePoint, certificate: X509Certificate, request: WebRequest, certificateProblem: IntType) -> BooleanType: ...
    
    # No Events


class ICloseEx(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def CloseEx(self, closeState: CloseExState) -> VoidType: ...
    
    # No Events


class ICredentialPolicy(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def ShouldSendCredential(self, challengeUri: Uri, request: WebRequest, credential: NetworkCredential, authenticationModule: IAuthenticationModule) -> BooleanType: ...
    
    # No Events


class ICredentials(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetCredential(self, uri: Uri, authType: StringType) -> NetworkCredential: ...
    
    # No Events


class ICredentialsByHost(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetCredential(self, host: StringType, port: IntType, authenticationType: StringType) -> NetworkCredential: ...
    
    # No Events


class IRequestLifetimeTracker(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def TrackRequestLifetime(self, requestStartTimestamp: LongType) -> VoidType: ...
    
    # No Events


class ISessionAuthenticationModule(Protocol, IAuthenticationModule):
    # ---------- Properties ---------- #
    
    @property
    def CanUseDefaultCredentials(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def ClearSession(self, webRequest: WebRequest) -> VoidType: ...
    
    def Update(self, challenge: StringType, webRequest: WebRequest) -> BooleanType: ...
    
    def get_CanUseDefaultCredentials(self) -> BooleanType: ...
    
    # No Events


class IWebProxy(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def Credentials(self) -> ICredentials: ...
    
    @Credentials.setter
    def Credentials(self, value: ICredentials) -> None: ...
    
    # ---------- Methods ---------- #
    
    def GetProxy(self, destination: Uri) -> Uri: ...
    
    def IsBypassed(self, host: Uri) -> BooleanType: ...
    
    def get_Credentials(self) -> ICredentials: ...
    
    def set_Credentials(self, value: ICredentials) -> VoidType: ...
    
    # No Events


class IWebProxyFinder(Protocol, IDisposable):
    # ---------- Properties ---------- #
    
    @property
    def IsValid(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def Abort(self) -> VoidType: ...
    
    def GetProxies(self, destination: Uri, proxyList: IList[StringType]) -> Tuple[BooleanType, IList[StringType]]: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_IsValid(self) -> BooleanType: ...
    
    # No Events


class IWebProxyScript(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    def Load(self, scriptLocation: Uri, script: StringType, helperType: TypeType) -> BooleanType: ...
    
    def Run(self, url: StringType, host: StringType) -> StringType: ...
    
    # No Events


class IWebRequestCreate(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Create(self, uri: Uri) -> WebRequest: ...
    
    # No Events


class SSPIInterface(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def SecurityPackages(self) -> ArrayType[SecurityPackageInfoClass]: ...
    
    @SecurityPackages.setter
    def SecurityPackages(self, value: ArrayType[SecurityPackageInfoClass]) -> None: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def AcceptSecurityContext(self, credential: SafeFreeCredentials, context: SafeDeleteContext, inputBuffer: SecurityBuffer, inFlags: ContextFlags, endianness: Endianness, outputBuffer: SecurityBuffer, outFlags: ContextFlags) -> Tuple[IntType, SafeFreeCredentials, SafeDeleteContext, ContextFlags]: ...
    
    @overload
    def AcceptSecurityContext(self, credential: SafeFreeCredentials, context: SafeDeleteContext, inputBuffers: ArrayType[SecurityBuffer], inFlags: ContextFlags, endianness: Endianness, outputBuffer: SecurityBuffer, outFlags: ContextFlags) -> Tuple[IntType, SafeDeleteContext, ContextFlags]: ...
    
    @overload
    def AcquireCredentialsHandle(self, moduleName: StringType, usage: CredentialUse, authdata: AuthIdentity, outCredential: SafeFreeCredentials) -> Tuple[IntType, AuthIdentity, SafeFreeCredentials]: ...
    
    @overload
    def AcquireCredentialsHandle(self, moduleName: StringType, usage: CredentialUse, authdata: SafeSspiAuthDataHandle, outCredential: SafeFreeCredentials) -> Tuple[IntType, SafeSspiAuthDataHandle, SafeFreeCredentials]: ...
    
    @overload
    def AcquireCredentialsHandle(self, moduleName: StringType, usage: CredentialUse, authdata: SecureCredential, outCredential: SafeFreeCredentials) -> Tuple[IntType, SecureCredential, SafeFreeCredentials]: ...
    
    @overload
    def AcquireCredentialsHandle(self, moduleName: StringType, usage: CredentialUse, authdata: SecureCredential2, outCredential: SafeFreeCredentials) -> Tuple[IntType, SecureCredential2, SafeFreeCredentials]: ...
    
    def AcquireDefaultCredential(self, moduleName: StringType, usage: CredentialUse, outCredential: SafeFreeCredentials) -> Tuple[IntType, SafeFreeCredentials]: ...
    
    def ApplyControlToken(self, refContext: SafeDeleteContext, inputBuffers: ArrayType[SecurityBuffer]) -> Tuple[IntType, SafeDeleteContext]: ...
    
    def CompleteAuthToken(self, refContext: SafeDeleteContext, inputBuffers: ArrayType[SecurityBuffer]) -> Tuple[IntType, SafeDeleteContext]: ...
    
    def DecryptMessage(self, context: SafeDeleteContext, inputOutput: SecurityBufferDescriptor, sequenceNumber: UIntType) -> IntType: ...
    
    def EncryptMessage(self, context: SafeDeleteContext, inputOutput: SecurityBufferDescriptor, sequenceNumber: UIntType) -> IntType: ...
    
    def EnumerateSecurityPackages(self, pkgnum: IntType, pkgArray: SafeFreeContextBuffer) -> Tuple[IntType, IntType, SafeFreeContextBuffer]: ...
    
    @overload
    def InitializeSecurityContext(self, credential: SafeFreeCredentials, context: SafeDeleteContext, targetName: StringType, inFlags: ContextFlags, endianness: Endianness, inputBuffer: SecurityBuffer, outputBuffer: SecurityBuffer, outFlags: ContextFlags) -> Tuple[IntType, SafeFreeCredentials, SafeDeleteContext, ContextFlags]: ...
    
    @overload
    def InitializeSecurityContext(self, credential: SafeFreeCredentials, context: SafeDeleteContext, targetName: StringType, inFlags: ContextFlags, endianness: Endianness, inputBuffers: ArrayType[SecurityBuffer], outputBuffer: SecurityBuffer, outFlags: ContextFlags) -> Tuple[IntType, SafeDeleteContext, ContextFlags]: ...
    
    def MakeSignature(self, context: SafeDeleteContext, inputOutput: SecurityBufferDescriptor, sequenceNumber: UIntType) -> IntType: ...
    
    def QueryContextAttributes(self, phContext: SafeDeleteContext, attribute: ContextAttribute, buffer: ArrayType[ByteType], handleType: TypeType, refHandle: SafeHandle) -> Tuple[IntType, SafeHandle]: ...
    
    def QueryContextChannelBinding(self, phContext: SafeDeleteContext, attribute: ContextAttribute, refHandle: SafeFreeContextBufferChannelBinding) -> Tuple[IntType, SafeFreeContextBufferChannelBinding]: ...
    
    def QuerySecurityContextToken(self, phContext: SafeDeleteContext, phToken: SafeCloseHandle) -> Tuple[IntType, SafeCloseHandle]: ...
    
    def SetContextAttributes(self, phContext: SafeDeleteContext, attribute: ContextAttribute, buffer: ArrayType[ByteType]) -> IntType: ...
    
    def VerifySignature(self, context: SafeDeleteContext, inputOutput: SecurityBufferDescriptor, sequenceNumber: UIntType) -> IntType: ...
    
    def get_SecurityPackages(self) -> ArrayType[SecurityPackageInfoClass]: ...
    
    def set_SecurityPackages(self, value: ArrayType[SecurityPackageInfoClass]) -> VoidType: ...
    
    # No Events


# ---------- Enums ---------- #

class AddressInfoHints(Enum):
    AI_PASSIVE: IntType = 1
    AI_CANONNAME: IntType = 2
    AI_NUMERICHOST: IntType = 4
    AI_FQDN: IntType = 131072


class Alg(Enum):
    Any: IntType = 0
    NameDES: IntType = 1
    NameRC4: IntType = 1
    NameRC2: IntType = 2
    NameDH_Ephem: IntType = 2
    Name3DES: IntType = 3
    NameMD5: IntType = 3
    NameSHA: IntType = 4
    NameSHA256: IntType = 12
    NameSHA384: IntType = 13
    NameSHA512: IntType = 14
    NameAES_128: IntType = 14
    NameAES_192: IntType = 15
    NameAES_256: IntType = 16
    NameAES: IntType = 17
    TypeRSA: IntType = 1024
    TypeBlock: IntType = 1536
    TypeStream: IntType = 2048
    TypeDH: IntType = 2560
    ClassSignture: IntType = 8192
    ClassEncrypt: IntType = 24576
    ClassHash: IntType = 32768
    ClassKeyXch: IntType = 40960


class AuthenticationSchemes(Enum):
    #None: IntType = 0
    Digest: IntType = 1
    Negotiate: IntType = 2
    Ntlm: IntType = 4
    IntegratedWindowsAuthentication: IntType = 6
    Basic: IntType = 8
    Anonymous: IntType = 32768


class BoundaryType(Enum):
    ContentLength: IntType = 0
    Chunked: IntType = 1
    Multipart: IntType = 3
    #None: IntType = 4
    Invalid: IntType = 5


class BufferType(Enum):
    ReadOnlyFlag: IntType = -2147483648
    Empty: IntType = 0
    Data: IntType = 1
    Token: IntType = 2
    Parameters: IntType = 3
    Missing: IntType = 4
    Extra: IntType = 5
    Trailer: IntType = 6
    Header: IntType = 7
    Padding: IntType = 9
    Stream: IntType = 10
    ChannelBindings: IntType = 14
    TargetHost: IntType = 16
    ReadOnlyWithChecksum: IntType = 268435456


class CertUsage(Enum):
    MatchTypeAnd: IntType = 0
    MatchTypeOr: IntType = 1


class CertificateEncoding(Enum):
    Zero: IntType = 0
    X509AsnEncoding: IntType = 1
    X509NdrEncoding: IntType = 2
    Pkcs7AsnEncoding: IntType = 65536
    AnyAsnEncoding: IntType = 65537
    Pkcs7NdrEncoding: IntType = 131072


class CertificateProblem(Enum):
    CryptNOREVOCATIONCHECK: IntType = -2146885614
    CryptREVOCATIONOFFLINE: IntType = -2146885613
    TrustSYSTEMERROR: IntType = -2146869247
    TrustNOSIGNERCERT: IntType = -2146869246
    TrustCOUNTERSIGNER: IntType = -2146869245
    TrustCERTSIGNATURE: IntType = -2146869244
    TrustTIMESTAMP: IntType = -2146869243
    TrustBADDIGEST: IntType = -2146869232
    TrustBASICCONSTRAINTS: IntType = -2146869223
    TrustFINANCIALCRITERIA: IntType = -2146869218
    TrustNOSIGNATURE: IntType = -2146762496
    CertEXPIRED: IntType = -2146762495
    CertVALIDITYPERIODNESTING: IntType = -2146762494
    CertROLE: IntType = -2146762493
    CertPATHLENCONST: IntType = -2146762492
    CertCRITICAL: IntType = -2146762491
    CertPURPOSE: IntType = -2146762490
    CertISSUERCHAINING: IntType = -2146762489
    CertMALFORMED: IntType = -2146762488
    CertUNTRUSTEDROOT: IntType = -2146762487
    CertCHAINING: IntType = -2146762486
    CertREVOKED: IntType = -2146762484
    CertUNTRUSTEDTESTROOT: IntType = -2146762483
    CertREVOCATION_FAILURE: IntType = -2146762482
    CertCN_NO_MATCH: IntType = -2146762481
    CertWRONG_USAGE: IntType = -2146762480
    TrustEXPLICITDISTRUST: IntType = -2146762479
    CertUNTRUSTEDCA: IntType = -2146762478
    CertINVALIDPOLICY: IntType = -2146762477
    CertINVALIDNAME: IntType = -2146762476
    OK: IntType = 0


class ChainPolicyType(Enum):
    Base: IntType = 1
    Authenticode: IntType = 2
    Authenticode_TS: IntType = 3
    SSL: IntType = 4
    BasicConstraints: IntType = 5
    NtAuth: IntType = 6


class CloseExState(Enum):
    Normal: IntType = 0
    Abort: IntType = 1
    Silent: IntType = 2


class ConnectionModes(Enum):
    Single: IntType = 0
    Persistent: IntType = 1
    Pipeline: IntType = 2
    Mux: IntType = 3


class ContentTypeValues(Enum):
    ChangeCipherSpec: IntType = 20
    Alert: IntType = 21
    HandShake: IntType = 22
    AppData: IntType = 23
    Unrecognized: IntType = 255


class ContextAttribute(Enum):
    Sizes: IntType = 0
    Names: IntType = 1
    Lifespan: IntType = 2
    DceInfo: IntType = 3
    StreamSizes: IntType = 4
    Authority: IntType = 6
    PackageInfo: IntType = 10
    NegotiationInfo: IntType = 12
    UniqueBindings: IntType = 25
    EndpointBindings: IntType = 26
    ClientSpecifiedSpn: IntType = 27
    RemoteCertificate: IntType = 83
    LocalCertificate: IntType = 84
    RootStore: IntType = 85
    IssuerListInfoEx: IntType = 89
    ConnectionInfo: IntType = 90
    UiInfo: IntType = 104


class ContextFlags(Enum):
    Zero: IntType = 0
    Delegate: IntType = 1
    MutualAuth: IntType = 2
    ReplayDetect: IntType = 4
    SequenceDetect: IntType = 8
    Confidentiality: IntType = 16
    UseSessionKey: IntType = 32
    InitUseSuppliedCreds: IntType = 128
    AllocateMemory: IntType = 256
    Connection: IntType = 2048
    InitExtendedError: IntType = 16384
    AcceptExtendedError: IntType = 32768
    InitStream: IntType = 32768
    InitIntegrity: IntType = 65536
    AcceptStream: IntType = 65536
    InitIdentify: IntType = 131072
    AcceptIntegrity: IntType = 131072
    AcceptIdentify: IntType = 524288
    InitManualCredValidation: IntType = 524288
    ProxyBindings: IntType = 67108864
    AllowMissingBindings: IntType = 268435456
    UnverifiedTargetName: IntType = 536870912


class CookieToken(Enum):
    Nothing: IntType = 0
    NameValuePair: IntType = 1
    Attribute: IntType = 2
    EndToken: IntType = 3
    EndCookie: IntType = 4
    End: IntType = 5
    Equals: IntType = 6
    Comment: IntType = 7
    CommentUrl: IntType = 8
    CookieName: IntType = 9
    Discard: IntType = 10
    Domain: IntType = 11
    Expires: IntType = 12
    MaxAge: IntType = 13
    Path: IntType = 14
    Port: IntType = 15
    Secure: IntType = 16
    HttpOnly: IntType = 17
    Unknown: IntType = 18
    Version: IntType = 19


class CookieVariant(Enum):
    Unknown: IntType = 0
    Plain: IntType = 1
    Rfc2109: IntType = 2
    Default: IntType = 2
    Rfc2965: IntType = 3


class CredentialUse(Enum):
    Inbound: IntType = 1
    Outbound: IntType = 2
    Both: IntType = 3


class DataParseStatus(Enum):
    NeedMoreData: IntType = 0
    ContinueParsing: IntType = 1
    Done: IntType = 2
    Invalid: IntType = 3
    DataTooBig: IntType = 4


class DecompressionMethods(Enum):
    #None: IntType = 0
    GZip: IntType = 1
    Deflate: IntType = 2


class DefaultPorts(Enum):
    DEFAULT_FTP_PORT: IntType = 21
    DEFAULT_TELNET_PORT: IntType = 23
    DEFAULT_SMTP_PORT: IntType = 25
    DEFAULT_GOPHER_PORT: IntType = 70
    DEFAULT_HTTP_PORT: IntType = 80
    DEFAULT_NNTP_PORT: IntType = 119
    DEFAULT_HTTPS_PORT: IntType = 443


class Endianness(Enum):
    Network: IntType = 0
    Native: IntType = 16


class EntitySendFormat(Enum):
    ContentLength: IntType = 0
    Chunked: IntType = 1


class FtpLoginState(Enum):
    NotLoggedIn: ByteType = 0
    LoggedIn: ByteType = 1
    LoggedInButNeedsRelogin: ByteType = 2
    ReloginFailed: ByteType = 3


class FtpMethodFlags(Enum):
    #None: IntType = 0
    IsDownload: IntType = 1
    IsUpload: IntType = 2
    TakesParameter: IntType = 4
    MayTakeParameter: IntType = 8
    DoesNotTakeParameter: IntType = 16
    ParameterIsDirectory: IntType = 32
    ShouldParseForResponseUri: IntType = 64
    HasHttpCommand: IntType = 128
    MustChangeWorkingDirectoryToPath: IntType = 256


class FtpOperation(Enum):
    DownloadFile: IntType = 0
    ListDirectory: IntType = 1
    ListDirectoryDetails: IntType = 2
    UploadFile: IntType = 3
    UploadFileUnique: IntType = 4
    AppendFile: IntType = 5
    DeleteFile: IntType = 6
    GetDateTimestamp: IntType = 7
    GetFileSize: IntType = 8
    Rename: IntType = 9
    MakeDirectory: IntType = 10
    RemoveDirectory: IntType = 11
    PrintWorkingDirectory: IntType = 12
    Other: IntType = 13


class FtpPrimitive(Enum):
    Upload: IntType = 0
    Download: IntType = 1
    CommandOnly: IntType = 2


class FtpStatusCode(Enum):
    Undefined: IntType = 0
    RestartMarker: IntType = 110
    ServiceTemporarilyNotAvailable: IntType = 120
    DataAlreadyOpen: IntType = 125
    OpeningData: IntType = 150
    CommandOK: IntType = 200
    CommandExtraneous: IntType = 202
    DirectoryStatus: IntType = 212
    FileStatus: IntType = 213
    SystemType: IntType = 215
    SendUserCommand: IntType = 220
    ClosingControl: IntType = 221
    ClosingData: IntType = 226
    EnteringPassive: IntType = 227
    LoggedInProceed: IntType = 230
    ServerWantsSecureSession: IntType = 234
    FileActionOK: IntType = 250
    PathnameCreated: IntType = 257
    SendPasswordCommand: IntType = 331
    NeedLoginAccount: IntType = 332
    FileCommandPending: IntType = 350
    ServiceNotAvailable: IntType = 421
    CantOpenData: IntType = 425
    ConnectionClosed: IntType = 426
    ActionNotTakenFileUnavailableOrBusy: IntType = 450
    ActionAbortedLocalProcessingError: IntType = 451
    ActionNotTakenInsufficientSpace: IntType = 452
    CommandSyntaxError: IntType = 500
    ArgumentSyntaxError: IntType = 501
    CommandNotImplemented: IntType = 502
    BadCommandSequence: IntType = 503
    NotLoggedIn: IntType = 530
    AccountNeeded: IntType = 532
    ActionNotTakenFileUnavailable: IntType = 550
    ActionAbortedUnknownPageType: IntType = 551
    FileActionAborted: IntType = 552
    ActionNotTakenFilenameNotAllowed: IntType = 553


class HttpBehaviour(Enum):
    Unknown: ByteType = 0
    HTTP10: ByteType = 1
    HTTP11PartiallyCompliant: ByteType = 2
    HTTP11: ByteType = 3


class HttpProcessingResult(Enum):
    Continue: IntType = 0
    ReadWait: IntType = 1
    WriteWait: IntType = 2


class HttpRequestHeader(Enum):
    CacheControl: IntType = 0
    Connection: IntType = 1
    Date: IntType = 2
    KeepAlive: IntType = 3
    Pragma: IntType = 4
    Trailer: IntType = 5
    TransferEncoding: IntType = 6
    Upgrade: IntType = 7
    Via: IntType = 8
    Warning: IntType = 9
    Allow: IntType = 10
    ContentLength: IntType = 11
    ContentType: IntType = 12
    ContentEncoding: IntType = 13
    ContentLanguage: IntType = 14
    ContentLocation: IntType = 15
    ContentMd5: IntType = 16
    ContentRange: IntType = 17
    Expires: IntType = 18
    LastModified: IntType = 19
    Accept: IntType = 20
    AcceptCharset: IntType = 21
    AcceptEncoding: IntType = 22
    AcceptLanguage: IntType = 23
    Authorization: IntType = 24
    Cookie: IntType = 25
    Expect: IntType = 26
    From: IntType = 27
    Host: IntType = 28
    IfMatch: IntType = 29
    IfModifiedSince: IntType = 30
    IfNoneMatch: IntType = 31
    IfRange: IntType = 32
    IfUnmodifiedSince: IntType = 33
    MaxForwards: IntType = 34
    ProxyAuthorization: IntType = 35
    Referer: IntType = 36
    Range: IntType = 37
    Te: IntType = 38
    Translate: IntType = 39
    UserAgent: IntType = 40


class HttpResponseHeader(Enum):
    CacheControl: IntType = 0
    Connection: IntType = 1
    Date: IntType = 2
    KeepAlive: IntType = 3
    Pragma: IntType = 4
    Trailer: IntType = 5
    TransferEncoding: IntType = 6
    Upgrade: IntType = 7
    Via: IntType = 8
    Warning: IntType = 9
    Allow: IntType = 10
    ContentLength: IntType = 11
    ContentType: IntType = 12
    ContentEncoding: IntType = 13
    ContentLanguage: IntType = 14
    ContentLocation: IntType = 15
    ContentMd5: IntType = 16
    ContentRange: IntType = 17
    Expires: IntType = 18
    LastModified: IntType = 19
    AcceptRanges: IntType = 20
    Age: IntType = 21
    ETag: IntType = 22
    Location: IntType = 23
    ProxyAuthenticate: IntType = 24
    RetryAfter: IntType = 25
    Server: IntType = 26
    SetCookie: IntType = 27
    Vary: IntType = 28
    WwwAuthenticate: IntType = 29


class HttpStatusCode(Enum):
    Continue: IntType = 100
    SwitchingProtocols: IntType = 101
    OK: IntType = 200
    Created: IntType = 201
    Accepted: IntType = 202
    NonAuthoritativeInformation: IntType = 203
    NoContent: IntType = 204
    ResetContent: IntType = 205
    PartialContent: IntType = 206
    MultipleChoices: IntType = 300
    Ambiguous: IntType = 300
    MovedPermanently: IntType = 301
    Moved: IntType = 301
    Found: IntType = 302
    Redirect: IntType = 302
    SeeOther: IntType = 303
    RedirectMethod: IntType = 303
    NotModified: IntType = 304
    UseProxy: IntType = 305
    Unused: IntType = 306
    TemporaryRedirect: IntType = 307
    RedirectKeepVerb: IntType = 307
    BadRequest: IntType = 400
    Unauthorized: IntType = 401
    PaymentRequired: IntType = 402
    Forbidden: IntType = 403
    NotFound: IntType = 404
    MethodNotAllowed: IntType = 405
    NotAcceptable: IntType = 406
    ProxyAuthenticationRequired: IntType = 407
    RequestTimeout: IntType = 408
    Conflict: IntType = 409
    Gone: IntType = 410
    LengthRequired: IntType = 411
    PreconditionFailed: IntType = 412
    RequestEntityTooLarge: IntType = 413
    RequestUriTooLong: IntType = 414
    UnsupportedMediaType: IntType = 415
    RequestedRangeNotSatisfiable: IntType = 416
    ExpectationFailed: IntType = 417
    UpgradeRequired: IntType = 426
    InternalServerError: IntType = 500
    NotImplemented: IntType = 501
    BadGateway: IntType = 502
    ServiceUnavailable: IntType = 503
    GatewayTimeout: IntType = 504
    HttpVersionNotSupported: IntType = 505


class HttpWriteMode(Enum):
    Unknown: IntType = 0
    ContentLength: IntType = 1
    Chunked: IntType = 2
    Buffer: IntType = 3
    #None: IntType = 4


class IgnoreCertProblem(Enum):
    not_time_valid: IntType = 1
    ctl_not_time_valid: IntType = 2
    not_time_nested: IntType = 4
    all_not_time_valid: IntType = 7
    invalid_basic_constraints: IntType = 8
    allow_unknown_ca: IntType = 16
    wrong_usage: IntType = 32
    invalid_name: IntType = 64
    invalid_policy: IntType = 128
    end_rev_unknown: IntType = 256
    ctl_signer_rev_unknown: IntType = 512
    ca_rev_unknown: IntType = 1024
    root_rev_unknown: IntType = 2048
    all_rev_unknown: IntType = 3840
    none: IntType = 4095


class ListenerClientCertState(Enum):
    NotInitialized: IntType = 0
    InProgress: IntType = 1
    Completed: IntType = 2


class NameInfoFlags(Enum):
    NI_NOFQDN: IntType = 1
    NI_NUMERICHOST: IntType = 2
    NI_NAMEREQD: IntType = 4
    NI_NUMERICSERV: IntType = 8
    NI_DGRAM: IntType = 16


class NetworkAccess(Enum):
    Connect: IntType = 64
    Accept: IntType = 128


class NetworkingPerfCounterName(Enum):
    SocketConnectionsEstablished: IntType = 0
    SocketBytesReceived: IntType = 1
    SocketBytesSent: IntType = 2
    SocketDatagramsReceived: IntType = 3
    SocketDatagramsSent: IntType = 4
    HttpWebRequestCreated: IntType = 5
    HttpWebRequestAvgLifeTime: IntType = 6
    HttpWebRequestAvgLifeTimeBase: IntType = 7
    HttpWebRequestQueued: IntType = 8
    HttpWebRequestAvgQueueTime: IntType = 9
    HttpWebRequestAvgQueueTimeBase: IntType = 10
    HttpWebRequestAborted: IntType = 11
    HttpWebRequestFailed: IntType = 12


class ReadState(Enum):
    Start: IntType = 0
    StatusLine: IntType = 1
    Headers: IntType = 2
    Data: IntType = 3


class SchProtocols(Enum):
    UniClient: IntType = -2147483648
    ClientMask: IntType = -2147472726
    Unified: IntType = -1073741824
    Zero: IntType = 0
    PctServer: IntType = 1
    PctClient: IntType = 2
    Pct: IntType = 3
    Ssl2Server: IntType = 4
    Ssl2Client: IntType = 8
    Ssl2: IntType = 12
    Ssl3Server: IntType = 16
    Ssl3Client: IntType = 32
    Ssl3: IntType = 48
    Tls10Server: IntType = 64
    Tls10Client: IntType = 128
    Tls10: IntType = 192
    Ssl3Tls: IntType = 240
    Tls11Server: IntType = 256
    Tls11Client: IntType = 512
    Tls11: IntType = 768
    Tls12Server: IntType = 1024
    Tls12Client: IntType = 2048
    Tls12: IntType = 3072
    Tls13Server: IntType = 4096
    Tls13Client: IntType = 8192
    Tls13: IntType = 12288
    UniServer: IntType = 1073741824
    ServerMask: IntType = 1073747285


class SecurDll(Enum):
    SECURITY: IntType = 0
    SECUR32: IntType = 1
    SCHANNEL: IntType = 2


class SecurityProtocolType(Enum):
    SystemDefault: IntType = 0
    Ssl3: IntType = 48
    Tls: IntType = 192
    Tls11: IntType = 768
    Tls12: IntType = 3072
    Tls13: IntType = 12288


class SecurityStatus(Enum):
    OutOfMemory: IntType = -2146893056
    InvalidHandle: IntType = -2146893055
    Unsupported: IntType = -2146893054
    TargetUnknown: IntType = -2146893053
    InternalError: IntType = -2146893052
    PackageNotFound: IntType = -2146893051
    NotOwner: IntType = -2146893050
    CannotInstall: IntType = -2146893049
    InvalidToken: IntType = -2146893048
    CannotPack: IntType = -2146893047
    QopNotSupported: IntType = -2146893046
    NoImpersonation: IntType = -2146893045
    LogonDenied: IntType = -2146893044
    UnknownCredentials: IntType = -2146893043
    NoCredentials: IntType = -2146893042
    MessageAltered: IntType = -2146893041
    OutOfSequence: IntType = -2146893040
    NoAuthenticatingAuthority: IntType = -2146893039
    IncompleteMessage: IntType = -2146893032
    IncompleteCredentials: IntType = -2146893024
    BufferNotEnough: IntType = -2146893023
    WrongPrincipal: IntType = -2146893022
    TimeSkew: IntType = -2146893020
    UntrustedRoot: IntType = -2146893019
    IllegalMessage: IntType = -2146893018
    CertUnknown: IntType = -2146893017
    CertExpired: IntType = -2146893016
    AlgorithmMismatch: IntType = -2146893007
    SecurityQosFailed: IntType = -2146893006
    SmartcardLogonRequired: IntType = -2146892994
    UnsupportedPreauth: IntType = -2146892989
    BadBinding: IntType = -2146892986
    OK: IntType = 0
    ContinueNeeded: IntType = 590610
    CompleteNeeded: IntType = 590611
    CompAndContinue: IntType = 590612
    ContextExpired: IntType = 590615
    CredentialsNeeded: IntType = 590624
    Renegotiate: IntType = 590625


class SocketConstructorFlags(Enum):
    WSA_FLAG_OVERLAPPED: IntType = 1
    WSA_FLAG_MULTIPOINT_C_ROOT: IntType = 2
    WSA_FLAG_MULTIPOINT_C_LEAF: IntType = 4
    WSA_FLAG_MULTIPOINT_D_ROOT: IntType = 8
    WSA_FLAG_MULTIPOINT_D_LEAF: IntType = 16


class ThreadKinds(Enum):
    Unknown: IntType = 0
    User: IntType = 1
    System: IntType = 2
    OwnerMask: IntType = 3
    Sync: IntType = 4
    Async: IntType = 8
    SyncMask: IntType = 12
    Timer: IntType = 16
    CompletionPort: IntType = 32
    Worker: IntType = 64
    ThreadPool: IntType = 96
    Finalization: IntType = 128
    Other: IntType = 256
    SafeSources: IntType = 352
    SourceMask: IntType = 496


class TransportType(Enum):
    Udp: IntType = 1
    Connectionless: IntType = 1
    Tcp: IntType = 2
    ConnectionOriented: IntType = 2
    All: IntType = 3


class TriState(Enum):
    Unspecified: IntType = -1
    False: IntType = 0
    True: IntType = 1


class WebExceptionInternalStatus(Enum):
    RequestFatal: IntType = 0
    ServicePointFatal: IntType = 1
    Recoverable: IntType = 2
    Isolated: IntType = 3


class WebExceptionStatus(Enum):
    Success: IntType = 0
    NameResolutionFailure: IntType = 1
    ConnectFailure: IntType = 2
    ReceiveFailure: IntType = 3
    SendFailure: IntType = 4
    PipelineFailure: IntType = 5
    RequestCanceled: IntType = 6
    ProtocolError: IntType = 7
    ConnectionClosed: IntType = 8
    TrustFailure: IntType = 9
    SecureChannelFailure: IntType = 10
    ServerProtocolViolation: IntType = 11
    KeepAliveFailure: IntType = 12
    Pending: IntType = 13
    Timeout: IntType = 14
    ProxyNameResolutionFailure: IntType = 15
    UnknownError: IntType = 16
    MessageLengthLimitExceeded: IntType = 17
    CacheEntryNotFound: IntType = 18
    RequestProhibitedByCachePolicy: IntType = 19
    RequestProhibitedByProxy: IntType = 20


class WebHeaderCollectionType(Enum):
    Unknown: UShortType = 0
    WebRequest: UShortType = 1
    WebResponse: UShortType = 2
    HttpWebRequest: UShortType = 3
    HttpWebResponse: UShortType = 4
    HttpListenerRequest: UShortType = 5
    HttpListenerResponse: UShortType = 6
    FtpWebRequest: UShortType = 7
    FtpWebResponse: UShortType = 8
    FileWebRequest: UShortType = 9
    FileWebResponse: UShortType = 10


class WebParseErrorCode(Enum):
    Generic: IntType = 0
    InvalidHeaderName: IntType = 1
    InvalidContentLength: IntType = 2
    IncompleteHeaderLine: IntType = 3
    CrLfError: IntType = 4
    InvalidChunkFormat: IntType = 5
    UnexpectedServerResponse: IntType = 6


class WebParseErrorSection(Enum):
    Generic: IntType = 0
    ResponseHeader: IntType = 1
    ResponseStatusLine: IntType = 2
    ResponseBody: IntType = 3


class WindowsInstallationType(Enum):
    Unknown: IntType = 0
    Client: IntType = 1
    Server: IntType = 2
    ServerCore: IntType = 3
    Embedded: IntType = 4


class WriteBufferState(Enum):
    Disabled: IntType = 0
    Headers: IntType = 1
    Buffer: IntType = 2
    Playback: IntType = 3


# ---------- Delegates ---------- #

AsyncProtocolCallback = Callable[[AsyncProtocolRequest], VoidType]

AuthenticationSchemeSelector = Callable[[HttpListenerRequest], AuthenticationSchemes]

BindIPEndPoint = Callable[[ServicePoint, IPEndPoint, IntType], IPEndPoint]

CompletionDelegate = Callable[[ArrayType[ByteType], Exception, ObjectType], VoidType]

CreateConnectionDelegate = Callable[[ConnectionPool], PooledStream]

DownloadDataCompletedEventHandler = Callable[[ObjectType, DownloadDataCompletedEventArgs], VoidType]

DownloadProgressChangedEventHandler = Callable[[ObjectType, DownloadProgressChangedEventArgs], VoidType]

DownloadStringCompletedEventHandler = Callable[[ObjectType, DownloadStringCompletedEventArgs], VoidType]

GeneralAsyncDelegate = Callable[[ObjectType, ObjectType], VoidType]

HeaderParser = Callable[[StringType], ArrayType[StringType]]

HttpAbortDelegate = Callable[[HttpWebRequest, WebException], BooleanType]

HttpContinueDelegate = Callable[[IntType, WebHeaderCollection], VoidType]

OpenReadCompletedEventHandler = Callable[[ObjectType, OpenReadCompletedEventArgs], VoidType]

OpenWriteCompletedEventHandler = Callable[[ObjectType, OpenWriteCompletedEventArgs], VoidType]

UnlockConnectionDelegate = Callable[[], VoidType]

UploadDataCompletedEventHandler = Callable[[ObjectType, UploadDataCompletedEventArgs], VoidType]

UploadFileCompletedEventHandler = Callable[[ObjectType, UploadFileCompletedEventArgs], VoidType]

UploadProgressChangedEventHandler = Callable[[ObjectType, UploadProgressChangedEventArgs], VoidType]

UploadStringCompletedEventHandler = Callable[[ObjectType, UploadStringCompletedEventArgs], VoidType]

UploadValuesCompletedEventHandler = Callable[[ObjectType, UploadValuesCompletedEventArgs], VoidType]

WriteStreamClosedEventHandler = Callable[[ObjectType, WriteStreamClosedEventArgs], VoidType]

__all__ = [
    AsyncProtocolCallback,
    AsyncProtocolRequest,
    AsyncRequestContext,
    AuthenticationManager,
    AuthenticationManager2,
    AuthenticationManagerBase,
    AuthenticationManagerDefault,
    AuthenticationSchemeSelector,
    AuthenticationState,
    Authorization,
    AutoWebProxyScriptEngine,
    AutoWebProxyScriptWrapper,
    Base64Stream,
    BaseLoggingObject,
    BaseWebProxyFinder,
    BasicClient,
    BindIPEndPoint,
    BufferAsyncResult,
    BufferOffsetSize,
    BufferedReadStream,
    CachedTransportContext,
    CallbackClosure,
    CaseInsensitiveAscii,
    CertPolicyValidationCallback,
    ChunkParser,
    ClosableStream,
    ComNetOS,
    CommandStream,
    Comparer,
    CompletionDelegate,
    ConnectStream,
    ConnectStreamContext,
    Connection,
    ConnectionGroup,
    ConnectionPool,
    ConnectionPoolManager,
    ConnectionReturnResult,
    ContextAwareResult,
    Cookie,
    CookieCollection,
    CookieContainer,
    CookieException,
    CookieModule,
    CookieParser,
    CookieTokenizer,
    CoreResponseData,
    CreateConnectionDelegate,
    CredentialCache,
    CredentialHostKey,
    CredentialKey,
    DefaultCertPolicy,
    DeflateWrapperStream,
    DelayedRegex,
    DelegatedStream,
    DigestClient,
    DirectProxy,
    Dns,
    DnsEndPoint,
    DnsPermission,
    DnsPermissionAttribute,
    DownloadDataCompletedEventArgs,
    DownloadDataCompletedEventHandler,
    DownloadProgressChangedEventArgs,
    DownloadProgressChangedEventHandler,
    DownloadStringCompletedEventArgs,
    DownloadStringCompletedEventHandler,
    EmptyWebProxy,
    EndPoint,
    EndpointPermission,
    ExceptionHelper,
    FileWebRequest,
    FileWebRequestCreator,
    FileWebResponse,
    FileWebStream,
    FixedSizeReader,
    FrameHeader,
    FtpControlStream,
    FtpDataStream,
    FtpMethodInfo,
    FtpWebRequest,
    FtpWebRequestCreator,
    FtpWebResponse,
    GZipWrapperStream,
    GeneralAsyncDelegate,
    GlobalLog,
    GlobalProxySelection,
    GlobalSSPI,
    HeaderInfo,
    HeaderInfoTable,
    HeaderParser,
    HostHeaderString,
    HttpAbortDelegate,
    HttpContinueDelegate,
    HttpDateParse,
    HttpDigest,
    HttpDigestChallenge,
    HttpKnownHeaderNames,
    HttpListener,
    HttpListenerBasicIdentity,
    HttpListenerContext,
    HttpListenerException,
    HttpListenerPrefixCollection,
    HttpListenerRequest,
    HttpListenerRequestContext,
    HttpListenerRequestUriBuilder,
    HttpListenerResponse,
    HttpListenerTimeoutManager,
    HttpProtocolUtils,
    HttpRequestCreator,
    HttpRequestQueueV2Handle,
    HttpRequestStream,
    HttpResponseStream,
    HttpResponseStreamAsyncResult,
    HttpServerSessionHandle,
    HttpStatusDescription,
    HttpSysSettings,
    HttpVersion,
    HttpWebRequest,
    HttpWebResponse,
    HybridWebProxyFinder,
    IPAddress,
    IPEndPoint,
    IPHostEntry,
    IntPtrHelper,
    InterlockedStack,
    InternalException,
    KerberosClient,
    KnownHttpVerb,
    LazyAsyncResult,
    ListenerAsyncResult,
    ListenerClientCertAsyncResult,
    ListenerPrefixEnumerator,
    Logging,
    NTAuthentication,
    NclConstants,
    NclUtilities,
    NegotiateClient,
    NegotiationInfoClass,
    NestedMultipleAsyncResult,
    NestedSingleAsyncResult,
    NetRes,
    NetWebProxyFinder,
    NetworkAddressChangePolled,
    NetworkCredential,
    NetworkingPerfCounters,
    NtlmClient,
    OpenReadCompletedEventArgs,
    OpenReadCompletedEventHandler,
    OpenWriteCompletedEventArgs,
    OpenWriteCompletedEventHandler,
    PathList,
    PolicyWrapper,
    PooledStream,
    PrefixLookup,
    ProtocolViolationException,
    ProxyChain,
    ProxyScriptChain,
    ReceiveState,
    RegBlobWebProxyDataBuilder,
    RegistryConfiguration,
    RequestContextBase,
    RequestLifetimeSetter,
    ResponseDescription,
    RtcState,
    SSPIAuthType,
    SSPISecureChannelType,
    SSPIWrapper,
    SafeCertSelectCritera,
    SafeCloseHandle,
    SafeCloseIcmpHandle,
    SafeCloseSocket,
    SafeCloseSocketAndEvent,
    SafeCredentialReference,
    SafeDeleteContext,
    SafeDeleteContext_SECURITY,
    SafeFreeAddrInfo,
    SafeFreeCertChain,
    SafeFreeCertChainList,
    SafeFreeCertContext,
    SafeFreeContextBuffer,
    SafeFreeContextBufferChannelBinding,
    SafeFreeContextBufferChannelBinding_SECURITY,
    SafeFreeContextBuffer_SECURITY,
    SafeFreeCredential_SECURITY,
    SafeFreeCredentials,
    SafeGlobalFree,
    SafeInternetHandle,
    SafeLoadLibrary,
    SafeLocalFree,
    SafeLocalFreeChannelBinding,
    SafeNativeOverlapped,
    SafeNclNativeMethods,
    SafeOverlappedFree,
    SafeRegistryHandle,
    SafeSspiAuthDataHandle,
    SafeUnlockUrlCacheEntryFile,
    SafeWebSocketHandle,
    ScatterGatherBuffers,
    SecChannelBindings,
    SecSizes,
    SecurityBuffer,
    SecurityBufferDescriptor,
    SecurityPackageInfoClass,
    Semaphore,
    ServerCertValidationCallback,
    ServiceNameStore,
    ServicePoint,
    ServicePointManager,
    SocketAddress,
    SocketPermission,
    SocketPermissionAttribute,
    SplitWritesState,
    SpnDictionary,
    SpnToken,
    SslConnectionInfo,
    SslStreamContext,
    StaticProxy,
    StreamFramer,
    StreamSizes,
    SyncMemoryStream,
    SyncRequestContext,
    SystemNetworkCredential,
    TimeoutValidator,
    TimerThread,
    TlsStream,
    TrackingStringDictionary,
    TrackingValidationObjectDictionary,
    TransmitFileBuffers,
    TransportContext,
    UnlockConnectionDelegate,
    UnsafeNclNativeMethods,
    UploadDataCompletedEventArgs,
    UploadDataCompletedEventHandler,
    UploadFileCompletedEventArgs,
    UploadFileCompletedEventHandler,
    UploadProgressChangedEventArgs,
    UploadProgressChangedEventHandler,
    UploadStringCompletedEventArgs,
    UploadStringCompletedEventHandler,
    UploadValuesCompletedEventArgs,
    UploadValuesCompletedEventHandler,
    ValidationHelper,
    WebClient,
    WebException,
    WebExceptionMapping,
    WebHeaderCollection,
    WebPermission,
    WebPermissionAttribute,
    WebProxy,
    WebProxyData,
    WebProxyDataBuilder,
    WebProxyScriptHelper,
    WebRequest,
    WebRequestMethods,
    WebRequestPrefixElement,
    WebResponse,
    WebSocketHttpRequestCreator,
    WebUtility,
    Win32,
    WinHttpWebProxyBuilder,
    WinHttpWebProxyFinder,
    WorkerAsyncResult,
    WriteStreamClosedEventArgs,
    WriteStreamClosedEventHandler,
    AddressInfo,
    AuthIdentity,
    Bindings,
    Blob,
    CertEnhKeyUse,
    CertUsageMatch,
    ChainParameters,
    ChainPolicyParameter,
    ChainPolicyStatus,
    HeaderVariantInfo,
    IPMulticastRequest,
    IPv6MulticastRequest,
    InterlockedGate,
    IssuerListInfoEx,
    Linger,
    NegotiationInfo,
    SSL_EXTRA_CERT_CHAIN_POLICY_PARA,
    SSPIHandle,
    SecureCredential,
    SecureCredential2,
    SecurityBufferStruct,
    SecurityPackageInfo,
    ShellExpression,
    TlsParamaters,
    TunnelStateObject,
    WSABuffer,
    WSAData,
    WebParseError,
    WriteHeadersCallbackState,
    _CERT_CHAIN_ELEMENT,
    hostent,
    IAuthenticationManager,
    IAuthenticationModule,
    IAutoWebProxy,
    ICertificatePolicy,
    ICloseEx,
    ICredentialPolicy,
    ICredentials,
    ICredentialsByHost,
    IRequestLifetimeTracker,
    ISessionAuthenticationModule,
    IWebProxy,
    IWebProxyFinder,
    IWebProxyScript,
    IWebRequestCreate,
    SSPIInterface,
    AddressInfoHints,
    Alg,
    AuthenticationSchemes,
    BoundaryType,
    BufferType,
    CertUsage,
    CertificateEncoding,
    CertificateProblem,
    ChainPolicyType,
    CloseExState,
    ConnectionModes,
    ContentTypeValues,
    ContextAttribute,
    ContextFlags,
    CookieToken,
    CookieVariant,
    CredentialUse,
    DataParseStatus,
    DecompressionMethods,
    DefaultPorts,
    Endianness,
    EntitySendFormat,
    FtpLoginState,
    FtpMethodFlags,
    FtpOperation,
    FtpPrimitive,
    FtpStatusCode,
    HttpBehaviour,
    HttpProcessingResult,
    HttpRequestHeader,
    HttpResponseHeader,
    HttpStatusCode,
    HttpWriteMode,
    IgnoreCertProblem,
    ListenerClientCertState,
    NameInfoFlags,
    NetworkAccess,
    NetworkingPerfCounterName,
    ReadState,
    SchProtocols,
    SecurDll,
    SecurityProtocolType,
    SecurityStatus,
    SocketConstructorFlags,
    ThreadKinds,
    TransportType,
    TriState,
    WebExceptionInternalStatus,
    WebExceptionStatus,
    WebHeaderCollectionType,
    WebParseErrorCode,
    WebParseErrorSection,
    WindowsInstallationType,
    WriteBufferState,
    AsyncProtocolCallback,
    AuthenticationSchemeSelector,
    BindIPEndPoint,
    CompletionDelegate,
    CreateConnectionDelegate,
    DownloadDataCompletedEventHandler,
    DownloadProgressChangedEventHandler,
    DownloadStringCompletedEventHandler,
    GeneralAsyncDelegate,
    HeaderParser,
    HttpAbortDelegate,
    HttpContinueDelegate,
    OpenReadCompletedEventHandler,
    OpenWriteCompletedEventHandler,
    UnlockConnectionDelegate,
    UploadDataCompletedEventHandler,
    UploadFileCompletedEventHandler,
    UploadProgressChangedEventHandler,
    UploadStringCompletedEventHandler,
    UploadValuesCompletedEventHandler,
    WriteStreamClosedEventHandler,
]
