from __future__ import annotations

from abc import ABC
from typing import List, Protocol, TypeVar, Union, overload

from Microsoft.Win32.SafeHandles import SafeAccessTokenHandle
from System import Action, Array, Boolean, Byte, Enum, Exception, Func, IComparable, IDisposable, Int32, Int64, IntPtr, Object, String, SystemException, Type, Void
from System.Collections import IEnumerable, IEnumerator
from System.Collections.Generic import ICollection, IEnumerable, IEnumerator
from System.Runtime.InteropServices import _Exception
from System.Runtime.Serialization import IDeserializationCallback, ISerializable, SerializationInfo, StreamingContext
from System.Security.Claims import Claim, ClaimsIdentity, ClaimsPrincipal

# ---------- Types ---------- #

T = TypeVar('T')

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
ByteType = Union[int, Byte]
IntType = Union[int, Int32]
LongType = Union[int, Int64]
NIntType = Union[int, IntPtr]
ObjectType = Object
StringType = Union[str, String]
TypeType = Union[type, Type]
VoidType = Union[None, Void]


# ---------- Classes ---------- #

class GenericIdentity(ClaimsIdentity, IIdentity):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, name: StringType): ...
    
    @overload
    def __init__(self, name: StringType, type: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AuthenticationType(self) -> StringType: ...
    
    @property
    def Claims(self) -> IEnumerable[Claim]: ...
    
    @property
    def IsAuthenticated(self) -> BooleanType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> ClaimsIdentity: ...
    
    def get_AuthenticationType(self) -> StringType: ...
    
    def get_Claims(self) -> IEnumerable[Claim]: ...
    
    def get_IsAuthenticated(self) -> BooleanType: ...
    
    def get_Name(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class GenericPrincipal(ClaimsPrincipal, IPrincipal):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, identity: IIdentity, roles: ArrayType[StringType]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Identity(self) -> IIdentity: ...
    
    # ---------- Methods ---------- #
    
    def IsInRole(self, role: StringType) -> BooleanType: ...
    
    def get_Identity(self) -> IIdentity: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IdentityNotMappedException(SystemException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, inner: Exception): ...
    
    # ---------- Properties ---------- #
    
    @property
    def UnmappedIdentities(self) -> IdentityReferenceCollection: ...
    
    # ---------- Methods ---------- #
    
    def GetObjectData(self, serializationInfo: SerializationInfo, streamingContext: StreamingContext) -> VoidType: ...
    
    def get_UnmappedIdentities(self) -> IdentityReferenceCollection: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IdentityReference(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def IsValidTargetType(self, targetType: TypeType) -> BooleanType: ...
    
    def ToString(self) -> StringType: ...
    
    def Translate(self, targetType: TypeType) -> IdentityReference: ...
    
    def get_Value(self) -> StringType: ...
    
    @staticmethod
    def op_Equality(left: IdentityReference, right: IdentityReference) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(left: IdentityReference, right: IdentityReference) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IdentityReferenceCollection(ObjectType, ICollection[IdentityReference], IEnumerable[IdentityReference], IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, capacity: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def IsReadOnly(self) -> BooleanType: ...
    
    def __getitem__(self, key: IntType) -> IdentityReference: ...
    
    def __setitem__(self, key: IntType, value: IdentityReference) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, identity: IdentityReference) -> VoidType: ...
    
    def Clear(self) -> VoidType: ...
    
    def Contains(self, identity: IdentityReference) -> BooleanType: ...
    
    def CopyTo(self, array: ArrayType[IdentityReference], offset: IntType) -> VoidType: ...
    
    def GetEnumerator(self) -> IEnumerator[IdentityReference]: ...
    
    def Remove(self, identity: IdentityReference) -> BooleanType: ...
    
    @overload
    def Translate(self, targetType: TypeType) -> IdentityReferenceCollection: ...
    
    @overload
    def Translate(self, targetType: TypeType, forceSuccess: BooleanType) -> IdentityReferenceCollection: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_IsReadOnly(self) -> BooleanType: ...
    
    def get_Item(self, index: IntType) -> IdentityReference: ...
    
    def set_Item(self, index: IntType, value: IdentityReference) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IdentityReferenceEnumerator(ObjectType, IEnumerator[IdentityReference], IDisposable, IEnumerator):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Current(self) -> IdentityReference: ...
    
    # ---------- Methods ---------- #
    
    def Dispose(self) -> VoidType: ...
    
    def MoveNext(self) -> BooleanType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Current(self) -> IdentityReference: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class NTAccount(IdentityReference):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, domainName: StringType, accountName: StringType): ...
    
    @overload
    def __init__(self, name: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def IsValidTargetType(self, targetType: TypeType) -> BooleanType: ...
    
    def ToString(self) -> StringType: ...
    
    def Translate(self, targetType: TypeType) -> IdentityReference: ...
    
    def get_Value(self) -> StringType: ...
    
    @staticmethod
    def op_Equality(left: NTAccount, right: NTAccount) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(left: NTAccount, right: NTAccount) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SecurityIdentifier(IdentityReference, IComparable[SecurityIdentifier]):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def MaxBinaryLength() -> IntType: ...
    
    @staticmethod
    @property
    def MinBinaryLength() -> IntType: ...
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, sddlForm: StringType): ...
    
    @overload
    def __init__(self, binaryForm: ArrayType[ByteType], offset: IntType): ...
    
    @overload
    def __init__(self, binaryForm: NIntType): ...
    
    @overload
    def __init__(self, sidType: WellKnownSidType, domainSid: SecurityIdentifier): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AccountDomainSid(self) -> SecurityIdentifier: ...
    
    @property
    def BinaryLength(self) -> IntType: ...
    
    @property
    def Value(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def CompareTo(self, sid: SecurityIdentifier) -> IntType: ...
    
    @overload
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, sid: SecurityIdentifier) -> BooleanType: ...
    
    def GetBinaryForm(self, binaryForm: ArrayType[ByteType], offset: IntType) -> VoidType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def IsAccountSid(self) -> BooleanType: ...
    
    def IsEqualDomainSid(self, sid: SecurityIdentifier) -> BooleanType: ...
    
    def IsValidTargetType(self, targetType: TypeType) -> BooleanType: ...
    
    def IsWellKnown(self, type: WellKnownSidType) -> BooleanType: ...
    
    def ToString(self) -> StringType: ...
    
    def Translate(self, targetType: TypeType) -> IdentityReference: ...
    
    def get_AccountDomainSid(self) -> SecurityIdentifier: ...
    
    def get_BinaryLength(self) -> IntType: ...
    
    def get_Value(self) -> StringType: ...
    
    @staticmethod
    def op_Equality(left: SecurityIdentifier, right: SecurityIdentifier) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(left: SecurityIdentifier, right: SecurityIdentifier) -> BooleanType: ...
    
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


class WindowsIdentity(ClaimsIdentity, IIdentity, ISerializable, IDeserializationCallback, IDisposable):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def DefaultIssuer() -> StringType: ...
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, userToken: NIntType): ...
    
    @overload
    def __init__(self, userToken: NIntType, type: StringType): ...
    
    @overload
    def __init__(self, userToken: NIntType, type: StringType, acctType: WindowsAccountType): ...
    
    @overload
    def __init__(self, userToken: NIntType, type: StringType, acctType: WindowsAccountType, isAuthenticated: BooleanType): ...
    
    @overload
    def __init__(self, sUserPrincipalName: StringType): ...
    
    @overload
    def __init__(self, sUserPrincipalName: StringType, type: StringType): ...
    
    @overload
    def __init__(self, info: SerializationInfo, context: StreamingContext): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AccessToken(self) -> SafeAccessTokenHandle: ...
    
    @property
    def AuthenticationType(self) -> StringType: ...
    
    @property
    def Claims(self) -> IEnumerable[Claim]: ...
    
    @property
    def DeviceClaims(self) -> IEnumerable[Claim]: ...
    
    @property
    def Groups(self) -> IdentityReferenceCollection: ...
    
    @property
    def ImpersonationLevel(self) -> TokenImpersonationLevel: ...
    
    @property
    def IsAnonymous(self) -> BooleanType: ...
    
    @property
    def IsAuthenticated(self) -> BooleanType: ...
    
    @property
    def IsGuest(self) -> BooleanType: ...
    
    @property
    def IsSystem(self) -> BooleanType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def Owner(self) -> SecurityIdentifier: ...
    
    @property
    def Token(self) -> NIntType: ...
    
    @property
    def User(self) -> SecurityIdentifier: ...
    
    @property
    def UserClaims(self) -> IEnumerable[Claim]: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> ClaimsIdentity: ...
    
    def Dispose(self) -> VoidType: ...
    
    @staticmethod
    def GetAnonymous() -> WindowsIdentity: ...
    
    @staticmethod
    @overload
    def GetCurrent() -> WindowsIdentity: ...
    
    @staticmethod
    @overload
    def GetCurrent(ifImpersonating: BooleanType) -> WindowsIdentity: ...
    
    @staticmethod
    @overload
    def GetCurrent(desiredAccess: TokenAccessLevels) -> WindowsIdentity: ...
    
    @overload
    def Impersonate(self) -> WindowsImpersonationContext: ...
    
    @staticmethod
    @overload
    def Impersonate(userToken: NIntType) -> WindowsImpersonationContext: ...
    
    @staticmethod
    @overload
    def RunImpersonated(safeAccessTokenHandle: SafeAccessTokenHandle, action: Action) -> VoidType: ...
    
    @staticmethod
    @overload
    def RunImpersonated(safeAccessTokenHandle: SafeAccessTokenHandle, func: Func[T]) -> T: ...
    
    def get_AccessToken(self) -> SafeAccessTokenHandle: ...
    
    def get_AuthenticationType(self) -> StringType: ...
    
    def get_Claims(self) -> IEnumerable[Claim]: ...
    
    def get_DeviceClaims(self) -> IEnumerable[Claim]: ...
    
    def get_Groups(self) -> IdentityReferenceCollection: ...
    
    def get_ImpersonationLevel(self) -> TokenImpersonationLevel: ...
    
    def get_IsAnonymous(self) -> BooleanType: ...
    
    def get_IsAuthenticated(self) -> BooleanType: ...
    
    def get_IsGuest(self) -> BooleanType: ...
    
    def get_IsSystem(self) -> BooleanType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_Owner(self) -> SecurityIdentifier: ...
    
    def get_Token(self) -> NIntType: ...
    
    def get_User(self) -> SecurityIdentifier: ...
    
    def get_UserClaims(self) -> IEnumerable[Claim]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class WindowsImpersonationContext(ObjectType, IDisposable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Dispose(self) -> VoidType: ...
    
    def Undo(self) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class WindowsPrincipal(ClaimsPrincipal, IPrincipal):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, ntIdentity: WindowsIdentity): ...
    
    # ---------- Properties ---------- #
    
    @property
    def DeviceClaims(self) -> IEnumerable[Claim]: ...
    
    @property
    def Identity(self) -> IIdentity: ...
    
    @property
    def UserClaims(self) -> IEnumerable[Claim]: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def IsInRole(self, role: StringType) -> BooleanType: ...
    
    @overload
    def IsInRole(self, role: WindowsBuiltInRole) -> BooleanType: ...
    
    @overload
    def IsInRole(self, rid: IntType) -> BooleanType: ...
    
    @overload
    def IsInRole(self, sid: SecurityIdentifier) -> BooleanType: ...
    
    def get_DeviceClaims(self) -> IEnumerable[Claim]: ...
    
    def get_Identity(self) -> IIdentity: ...
    
    def get_UserClaims(self) -> IEnumerable[Claim]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# No Structs

# ---------- Interfaces ---------- #

class IIdentity(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def AuthenticationType(self) -> StringType: ...
    
    @property
    def IsAuthenticated(self) -> BooleanType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_AuthenticationType(self) -> StringType: ...
    
    def get_IsAuthenticated(self) -> BooleanType: ...
    
    def get_Name(self) -> StringType: ...
    
    # No Events


class IPrincipal(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def Identity(self) -> IIdentity: ...
    
    # ---------- Methods ---------- #
    
    def IsInRole(self, role: StringType) -> BooleanType: ...
    
    def get_Identity(self) -> IIdentity: ...
    
    # No Events


# ---------- Enums ---------- #

class IdentifierAuthority(Enum):
    NullAuthority = 0
    WorldAuthority = 1
    LocalAuthority = 2
    CreatorAuthority = 3
    NonUniqueAuthority = 4
    NTAuthority = 5
    SiteServerAuthority = 6
    InternetSiteAuthority = 7
    ExchangeAuthority = 8
    ResourceManagerAuthority = 9


class ImpersonationQueryResult(Enum):
    Impersonated = 0
    NotImpersonated = 1
    Failed = 2


class KerbLogonSubmitType(Enum):
    KerbInteractiveLogon = 2
    KerbSmartCardLogon = 6
    KerbWorkstationUnlockLogon = 7
    KerbSmartCardUnlockLogon = 8
    KerbProxyLogon = 9
    KerbTicketLogon = 10
    KerbTicketUnlockLogon = 11
    KerbS4ULogon = 12


class PolicyRights(Enum):
    POLICY_VIEW_LOCAL_INFORMATION = 1
    POLICY_VIEW_AUDIT_INFORMATION = 2
    POLICY_GET_PRIVATE_INFORMATION = 4
    POLICY_TRUST_ADMIN = 8
    POLICY_CREATE_ACCOUNT = 16
    POLICY_CREATE_SECRET = 32
    POLICY_CREATE_PRIVILEGE = 64
    POLICY_SET_DEFAULT_QUOTA_LIMITS = 128
    POLICY_SET_AUDIT_REQUIREMENTS = 256
    POLICY_AUDIT_LOG_ADMIN = 512
    POLICY_SERVER_ADMIN = 1024
    POLICY_LOOKUP_NAMES = 2048
    POLICY_NOTIFICATION = 4096


class PrincipalPolicy(Enum):
    UnauthenticatedPrincipal = 0
    NoPrincipal = 1
    WindowsPrincipal = 2


class SecurityLogonType(Enum):
    Interactive = 2
    Network = 3
    Batch = 4
    Service = 5
    Proxy = 6
    Unlock = 7


class SidNameUse(Enum):
    User = 1
    Group = 2
    Domain = 3
    Alias = 4
    WellKnownGroup = 5
    DeletedAccount = 6
    Invalid = 7
    Unknown = 8
    Computer = 9


class TokenAccessLevels(Enum):
    AssignPrimary = 1
    Duplicate = 2
    Impersonate = 4
    Query = 8
    QuerySource = 16
    AdjustPrivileges = 32
    AdjustGroups = 64
    AdjustDefault = 128
    AdjustSessionId = 256
    Read = 131080
    Write = 131296
    AllAccess = 983551
    MaximumAllowed = 33554432


class TokenImpersonationLevel(Enum):
    #None = 0
    Anonymous = 1
    Identification = 2
    Impersonation = 3
    Delegation = 4


class TokenInformationClass(Enum):
    TokenUser = 1
    TokenGroups = 2
    TokenPrivileges = 3
    TokenOwner = 4
    TokenPrimaryGroup = 5
    TokenDefaultDacl = 6
    TokenSource = 7
    TokenType = 8
    TokenImpersonationLevel = 9
    TokenStatistics = 10
    TokenRestrictedSids = 11
    TokenSessionId = 12
    TokenGroupsAndPrivileges = 13
    TokenSessionReference = 14
    TokenSandBoxInert = 15
    TokenAuditPolicy = 16
    TokenOrigin = 17
    TokenElevationType = 18
    TokenLinkedToken = 19
    TokenElevation = 20
    TokenHasRestrictions = 21
    TokenAccessInformation = 22
    TokenVirtualizationAllowed = 23
    TokenVirtualizationEnabled = 24
    TokenIntegrityLevel = 25
    TokenUIAccess = 26
    TokenMandatoryPolicy = 27
    TokenLogonSid = 28
    TokenIsAppContainer = 29
    TokenCapabilities = 30
    TokenAppContainerSid = 31
    TokenAppContainerNumber = 32
    TokenUserClaimAttributes = 33
    TokenDeviceClaimAttributes = 34
    TokenRestrictedUserClaimAttributes = 35
    TokenRestrictedDeviceClaimAttributes = 36
    TokenDeviceGroups = 37
    TokenRestrictedDeviceGroups = 38
    MaxTokenInfoClass = 39


class TokenType(Enum):
    TokenPrimary = 1
    TokenImpersonation = 2


class WellKnownSidType(Enum):
    NullSid = 0
    WorldSid = 1
    LocalSid = 2
    CreatorOwnerSid = 3
    CreatorGroupSid = 4
    CreatorOwnerServerSid = 5
    CreatorGroupServerSid = 6
    NTAuthoritySid = 7
    DialupSid = 8
    NetworkSid = 9
    BatchSid = 10
    InteractiveSid = 11
    ServiceSid = 12
    AnonymousSid = 13
    ProxySid = 14
    EnterpriseControllersSid = 15
    SelfSid = 16
    AuthenticatedUserSid = 17
    RestrictedCodeSid = 18
    TerminalServerSid = 19
    RemoteLogonIdSid = 20
    LogonIdsSid = 21
    LocalSystemSid = 22
    LocalServiceSid = 23
    NetworkServiceSid = 24
    BuiltinDomainSid = 25
    BuiltinAdministratorsSid = 26
    BuiltinUsersSid = 27
    BuiltinGuestsSid = 28
    BuiltinPowerUsersSid = 29
    BuiltinAccountOperatorsSid = 30
    BuiltinSystemOperatorsSid = 31
    BuiltinPrintOperatorsSid = 32
    BuiltinBackupOperatorsSid = 33
    BuiltinReplicatorSid = 34
    BuiltinPreWindows2000CompatibleAccessSid = 35
    BuiltinRemoteDesktopUsersSid = 36
    BuiltinNetworkConfigurationOperatorsSid = 37
    AccountAdministratorSid = 38
    AccountGuestSid = 39
    AccountKrbtgtSid = 40
    AccountDomainAdminsSid = 41
    AccountDomainUsersSid = 42
    AccountDomainGuestsSid = 43
    AccountComputersSid = 44
    AccountControllersSid = 45
    AccountCertAdminsSid = 46
    AccountSchemaAdminsSid = 47
    AccountEnterpriseAdminsSid = 48
    AccountPolicyAdminsSid = 49
    AccountRasAndIasServersSid = 50
    NtlmAuthenticationSid = 51
    DigestAuthenticationSid = 52
    SChannelAuthenticationSid = 53
    ThisOrganizationSid = 54
    OtherOrganizationSid = 55
    BuiltinIncomingForestTrustBuildersSid = 56
    BuiltinPerformanceMonitoringUsersSid = 57
    BuiltinPerformanceLoggingUsersSid = 58
    BuiltinAuthorizationAccessSid = 59
    WinBuiltinTerminalServerLicenseServersSid = 60
    MaxDefined = 60


class WinSecurityContext(Enum):
    Thread = 1
    Process = 2
    Both = 3


class WindowsAccountType(Enum):
    Normal = 0
    Guest = 1
    System = 2
    Anonymous = 3


class WindowsBuiltInRole(Enum):
    Administrator = 544
    User = 545
    Guest = 546
    PowerUser = 547
    AccountOperator = 548
    SystemOperator = 549
    PrintOperator = 550
    BackupOperator = 551
    Replicator = 552


# No Delegates

__all__ = [
    GenericIdentity,
    GenericPrincipal,
    IdentityNotMappedException,
    IdentityReference,
    IdentityReferenceCollection,
    IdentityReferenceEnumerator,
    NTAccount,
    SecurityIdentifier,
    Win32,
    WindowsIdentity,
    WindowsImpersonationContext,
    WindowsPrincipal,
    IIdentity,
    IPrincipal,
    IdentifierAuthority,
    ImpersonationQueryResult,
    KerbLogonSubmitType,
    PolicyRights,
    PrincipalPolicy,
    SecurityLogonType,
    SidNameUse,
    TokenAccessLevels,
    TokenImpersonationLevel,
    TokenInformationClass,
    TokenType,
    WellKnownSidType,
    WinSecurityContext,
    WindowsAccountType,
    WindowsBuiltInRole,
]
