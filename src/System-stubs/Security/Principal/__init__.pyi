"""Automatically generated stubs for C# namespace: System.Security.Principal."""

from abc import ABC
from collections.abc import Iterator
from typing import ClassVar
from typing import overload

from Microsoft.Win32.SafeHandles import SafeAccessTokenHandle
from System import Action
from System import Array
from System import Enum
from System import Exception
from System import Func
from System import IComparable
from System import IDisposable
from System import IntPtr
from System import Object
from System import Predicate
from System import SystemException
from System import Type
from System.Collections import IDictionary
from System.Collections import IEnumerable
from System.Collections import IEnumerator
from System.Collections.Generic import ICollection
from System.Collections.Generic import IEnumerable
from System.Collections.Generic import IEnumerator
from System.IO import BinaryWriter
from System.Reflection import MethodBase
from System.Runtime.InteropServices import _Exception
from System.Runtime.Serialization import IDeserializationCallback
from System.Runtime.Serialization import ISerializable
from System.Runtime.Serialization import SerializationInfo
from System.Runtime.Serialization import StreamingContext
from System.Security.Claims import Claim
from System.Security.Claims import ClaimsIdentity
from System.Security.Claims import ClaimsPrincipal

class GenericIdentity(ClaimsIdentity, IIdentity):
    """"""
    @overload
    def __init__(self, name: str) -> None:
        """"""
    @overload
    def __init__(self, name: str, type: str) -> None:
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

class GenericPrincipal(ClaimsPrincipal, IPrincipal):
    """"""
    def __init__(self, identity: IIdentity, roles: Array[str]) -> None:
        """"""
    @property
    def Claims(self) -> IEnumerable[Claim]:
        """"""
    @property
    def Identities(self) -> IEnumerable[ClaimsIdentity]:
        """"""
    @property
    def Identity(self) -> IIdentity:
        """"""
    def AddIdentities(self, identities: IEnumerable[ClaimsIdentity]) -> None:
        """"""
    def AddIdentity(self, identity: ClaimsIdentity) -> None:
        """"""
    def Clone(self) -> ClaimsPrincipal:
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
    def IsInRole(self, role: str) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    def WriteTo(self, writer: BinaryWriter) -> None:
        """"""

class IIdentity:
    """"""
    @property
    def AuthenticationType(self) -> str:
        """"""
    @property
    def IsAuthenticated(self) -> bool:
        """"""
    @property
    def Name(self) -> str:
        """"""

class IPrincipal:
    """"""
    @property
    def Identity(self) -> IIdentity:
        """"""
    def IsInRole(self, role: str) -> bool:
        """"""

class IdentifierAuthority(Enum):
    """"""

    NullAuthority: IdentifierAuthority = ...
    """"""
    WorldAuthority: IdentifierAuthority = ...
    """"""
    LocalAuthority: IdentifierAuthority = ...
    """"""
    CreatorAuthority: IdentifierAuthority = ...
    """"""
    NonUniqueAuthority: IdentifierAuthority = ...
    """"""
    NTAuthority: IdentifierAuthority = ...
    """"""
    SiteServerAuthority: IdentifierAuthority = ...
    """"""
    InternetSiteAuthority: IdentifierAuthority = ...
    """"""
    ExchangeAuthority: IdentifierAuthority = ...
    """"""
    ResourceManagerAuthority: IdentifierAuthority = ...
    """"""

class IdentityNotMappedException(SystemException, _Exception, ISerializable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, message: str) -> None:
        """"""
    @overload
    def __init__(self, message: str, inner: Exception) -> None:
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
    @property
    def UnmappedIdentities(self) -> IdentityReferenceCollection:
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

class IdentityReference(ABC, Object):
    """"""
    @property
    def Value(self) -> str:
        """"""
    def Equals(self, o: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def IsValidTargetType(self, targetType: Type) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    def Translate(self, targetType: Type) -> IdentityReference:
        """"""
    @classmethod
    def op_Equality(cls, left: IdentityReference, right: IdentityReference) -> bool:
        """"""
    @classmethod
    def op_Inequality(cls, left: IdentityReference, right: IdentityReference) -> bool:
        """"""
    def __eq__(self, other: IdentityReference) -> bool:
        """"""
    def __ne__(self, other: IdentityReference) -> bool:
        """"""

class IdentityReferenceCollection(
    Object, ICollection[IdentityReference], IEnumerable[IdentityReference], IEnumerable
):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, capacity: int) -> None:
        """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def Item(self) -> IdentityReference:
        """"""
    @Item.setter
    def Item(self, value: IdentityReference) -> None: ...
    def Add(self, identity: IdentityReference) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    def Contains(self, identity: IdentityReference) -> bool:
        """"""
    def CopyTo(self, array: Array[IdentityReference], offset: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator[IdentityReference]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Remove(self, identity: IdentityReference) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def Translate(self, targetType: Type) -> IdentityReferenceCollection:
        """"""
    @overload
    def Translate(self, targetType: Type, forceSuccess: bool) -> IdentityReferenceCollection:
        """"""
    def __contains__(self, identity: IdentityReference) -> bool:
        """"""
    def __iter__(self) -> Iterator[IdentityReference]:
        """"""
    def __delitem__(self, identity: IdentityReference) -> bool:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, index: int) -> IdentityReference:
        """"""
    def __setitem__(self, index: int, value: IdentityReference) -> None:
        """"""

class IdentityReferenceEnumerator(Object, IEnumerator[IdentityReference], IEnumerator, IDisposable):
    """"""
    @property
    def Current(self) -> IdentityReference:
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

class ImpersonationQueryResult(Enum):
    """"""

    Impersonated: ImpersonationQueryResult = ...
    """"""
    NotImpersonated: ImpersonationQueryResult = ...
    """"""
    Failed: ImpersonationQueryResult = ...
    """"""

class KerbLogonSubmitType(Enum):
    """"""

    KerbInteractiveLogon: KerbLogonSubmitType = ...
    """"""
    KerbSmartCardLogon: KerbLogonSubmitType = ...
    """"""
    KerbWorkstationUnlockLogon: KerbLogonSubmitType = ...
    """"""
    KerbSmartCardUnlockLogon: KerbLogonSubmitType = ...
    """"""
    KerbProxyLogon: KerbLogonSubmitType = ...
    """"""
    KerbTicketLogon: KerbLogonSubmitType = ...
    """"""
    KerbTicketUnlockLogon: KerbLogonSubmitType = ...
    """"""
    KerbS4ULogon: KerbLogonSubmitType = ...
    """"""

class NTAccount(IdentityReference):
    """"""
    @overload
    def __init__(self, domainName: str, accountName: str) -> None:
        """"""
    @overload
    def __init__(self, name: str) -> None:
        """"""
    @property
    def Value(self) -> str:
        """"""
    def Equals(self, o: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def IsValidTargetType(self, targetType: Type) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    def Translate(self, targetType: Type) -> IdentityReference:
        """"""
    @classmethod
    def op_Equality(cls, left: NTAccount, right: NTAccount) -> bool:
        """"""
    @classmethod
    def op_Inequality(cls, left: NTAccount, right: NTAccount) -> bool:
        """"""
    def __eq__(self, other: NTAccount) -> bool:
        """"""
    def __ne__(self, other: NTAccount) -> bool:
        """"""

class PolicyRights(Enum):
    """"""

    POLICY_VIEW_LOCAL_INFORMATION: PolicyRights = ...
    """"""
    POLICY_VIEW_AUDIT_INFORMATION: PolicyRights = ...
    """"""
    POLICY_GET_PRIVATE_INFORMATION: PolicyRights = ...
    """"""
    POLICY_TRUST_ADMIN: PolicyRights = ...
    """"""
    POLICY_CREATE_ACCOUNT: PolicyRights = ...
    """"""
    POLICY_CREATE_SECRET: PolicyRights = ...
    """"""
    POLICY_CREATE_PRIVILEGE: PolicyRights = ...
    """"""
    POLICY_SET_DEFAULT_QUOTA_LIMITS: PolicyRights = ...
    """"""
    POLICY_SET_AUDIT_REQUIREMENTS: PolicyRights = ...
    """"""
    POLICY_AUDIT_LOG_ADMIN: PolicyRights = ...
    """"""
    POLICY_SERVER_ADMIN: PolicyRights = ...
    """"""
    POLICY_LOOKUP_NAMES: PolicyRights = ...
    """"""
    POLICY_NOTIFICATION: PolicyRights = ...
    """"""

class PrincipalPolicy(Enum):
    """"""

    UnauthenticatedPrincipal: PrincipalPolicy = ...
    """"""
    NoPrincipal: PrincipalPolicy = ...
    """"""
    WindowsPrincipal: PrincipalPolicy = ...
    """"""

class SecurityIdentifier(IdentityReference, IComparable[SecurityIdentifier]):
    """"""

    MaxBinaryLength: ClassVar[int]
    """"""
    MinBinaryLength: ClassVar[int]
    """"""
    @overload
    def __init__(self, sddlForm: str) -> None:
        """"""
    @overload
    def __init__(self, binaryForm: Array[int], offset: int) -> None:
        """"""
    @overload
    def __init__(self, binaryForm: IntPtr) -> None:
        """"""
    @overload
    def __init__(self, sidType: WellKnownSidType, domainSid: SecurityIdentifier) -> None:
        """"""
    @property
    def AccountDomainSid(self) -> SecurityIdentifier:
        """"""
    @property
    def BinaryLength(self) -> int:
        """"""
    @property
    def Value(self) -> str:
        """"""
    def CompareTo(self, sid: SecurityIdentifier) -> int:
        """"""
    @overload
    def Equals(self, sid: SecurityIdentifier) -> bool:
        """"""
    @overload
    def Equals(self, o: object) -> bool:
        """"""
    def GetBinaryForm(self, binaryForm: Array[int], offset: int) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def IsAccountSid(self) -> bool:
        """"""
    def IsEqualDomainSid(self, sid: SecurityIdentifier) -> bool:
        """"""
    def IsValidTargetType(self, targetType: Type) -> bool:
        """"""
    def IsWellKnown(self, type: WellKnownSidType) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    def Translate(self, targetType: Type) -> IdentityReference:
        """"""
    @classmethod
    def op_Equality(cls, left: SecurityIdentifier, right: SecurityIdentifier) -> bool:
        """"""
    @classmethod
    def op_Inequality(cls, left: SecurityIdentifier, right: SecurityIdentifier) -> bool:
        """"""
    def __eq__(self, other: SecurityIdentifier) -> bool:
        """"""
    def __ne__(self, other: SecurityIdentifier) -> bool:
        """"""

class SecurityLogonType(Enum):
    """"""

    Interactive: SecurityLogonType = ...
    """"""
    Network: SecurityLogonType = ...
    """"""
    Batch: SecurityLogonType = ...
    """"""
    Service: SecurityLogonType = ...
    """"""
    Proxy: SecurityLogonType = ...
    """"""
    Unlock: SecurityLogonType = ...
    """"""

class SidNameUse(Enum):
    """"""

    User: SidNameUse = ...
    """"""
    Group: SidNameUse = ...
    """"""
    Domain: SidNameUse = ...
    """"""
    Alias: SidNameUse = ...
    """"""
    WellKnownGroup: SidNameUse = ...
    """"""
    DeletedAccount: SidNameUse = ...
    """"""
    Invalid: SidNameUse = ...
    """"""
    Unknown: SidNameUse = ...
    """"""
    Computer: SidNameUse = ...
    """"""

class TokenAccessLevels(Enum):
    """"""

    AssignPrimary: TokenAccessLevels = ...
    """"""
    Duplicate: TokenAccessLevels = ...
    """"""
    Impersonate: TokenAccessLevels = ...
    """"""
    Query: TokenAccessLevels = ...
    """"""
    QuerySource: TokenAccessLevels = ...
    """"""
    AdjustPrivileges: TokenAccessLevels = ...
    """"""
    AdjustGroups: TokenAccessLevels = ...
    """"""
    AdjustDefault: TokenAccessLevels = ...
    """"""
    AdjustSessionId: TokenAccessLevels = ...
    """"""
    Read: TokenAccessLevels = ...
    """"""
    Write: TokenAccessLevels = ...
    """"""
    AllAccess: TokenAccessLevels = ...
    """"""
    MaximumAllowed: TokenAccessLevels = ...
    """"""

class TokenImpersonationLevel(Enum):
    """"""

    _None: TokenImpersonationLevel = ...
    """"""
    Anonymous: TokenImpersonationLevel = ...
    """"""
    Identification: TokenImpersonationLevel = ...
    """"""
    Impersonation: TokenImpersonationLevel = ...
    """"""
    Delegation: TokenImpersonationLevel = ...
    """"""

class TokenInformationClass(Enum):
    """"""

    TokenUser: TokenInformationClass = ...
    """"""
    TokenGroups: TokenInformationClass = ...
    """"""
    TokenPrivileges: TokenInformationClass = ...
    """"""
    TokenOwner: TokenInformationClass = ...
    """"""
    TokenPrimaryGroup: TokenInformationClass = ...
    """"""
    TokenDefaultDacl: TokenInformationClass = ...
    """"""
    TokenSource: TokenInformationClass = ...
    """"""
    TokenType: TokenInformationClass = ...
    """"""
    TokenImpersonationLevel: TokenInformationClass = ...
    """"""
    TokenStatistics: TokenInformationClass = ...
    """"""
    TokenRestrictedSids: TokenInformationClass = ...
    """"""
    TokenSessionId: TokenInformationClass = ...
    """"""
    TokenGroupsAndPrivileges: TokenInformationClass = ...
    """"""
    TokenSessionReference: TokenInformationClass = ...
    """"""
    TokenSandBoxInert: TokenInformationClass = ...
    """"""
    TokenAuditPolicy: TokenInformationClass = ...
    """"""
    TokenOrigin: TokenInformationClass = ...
    """"""
    TokenElevationType: TokenInformationClass = ...
    """"""
    TokenLinkedToken: TokenInformationClass = ...
    """"""
    TokenElevation: TokenInformationClass = ...
    """"""
    TokenHasRestrictions: TokenInformationClass = ...
    """"""
    TokenAccessInformation: TokenInformationClass = ...
    """"""
    TokenVirtualizationAllowed: TokenInformationClass = ...
    """"""
    TokenVirtualizationEnabled: TokenInformationClass = ...
    """"""
    TokenIntegrityLevel: TokenInformationClass = ...
    """"""
    TokenUIAccess: TokenInformationClass = ...
    """"""
    TokenMandatoryPolicy: TokenInformationClass = ...
    """"""
    TokenLogonSid: TokenInformationClass = ...
    """"""
    TokenIsAppContainer: TokenInformationClass = ...
    """"""
    TokenCapabilities: TokenInformationClass = ...
    """"""
    TokenAppContainerSid: TokenInformationClass = ...
    """"""
    TokenAppContainerNumber: TokenInformationClass = ...
    """"""
    TokenUserClaimAttributes: TokenInformationClass = ...
    """"""
    TokenDeviceClaimAttributes: TokenInformationClass = ...
    """"""
    TokenRestrictedUserClaimAttributes: TokenInformationClass = ...
    """"""
    TokenRestrictedDeviceClaimAttributes: TokenInformationClass = ...
    """"""
    TokenDeviceGroups: TokenInformationClass = ...
    """"""
    TokenRestrictedDeviceGroups: TokenInformationClass = ...
    """"""
    MaxTokenInfoClass: TokenInformationClass = ...
    """"""

class TokenType(Enum):
    """"""

    TokenPrimary: TokenType = ...
    """"""
    TokenImpersonation: TokenType = ...
    """"""

class WellKnownSidType(Enum):
    """"""

    NullSid: WellKnownSidType = ...
    """"""
    WorldSid: WellKnownSidType = ...
    """"""
    LocalSid: WellKnownSidType = ...
    """"""
    CreatorOwnerSid: WellKnownSidType = ...
    """"""
    CreatorGroupSid: WellKnownSidType = ...
    """"""
    CreatorOwnerServerSid: WellKnownSidType = ...
    """"""
    CreatorGroupServerSid: WellKnownSidType = ...
    """"""
    NTAuthoritySid: WellKnownSidType = ...
    """"""
    DialupSid: WellKnownSidType = ...
    """"""
    NetworkSid: WellKnownSidType = ...
    """"""
    BatchSid: WellKnownSidType = ...
    """"""
    InteractiveSid: WellKnownSidType = ...
    """"""
    ServiceSid: WellKnownSidType = ...
    """"""
    AnonymousSid: WellKnownSidType = ...
    """"""
    ProxySid: WellKnownSidType = ...
    """"""
    EnterpriseControllersSid: WellKnownSidType = ...
    """"""
    SelfSid: WellKnownSidType = ...
    """"""
    AuthenticatedUserSid: WellKnownSidType = ...
    """"""
    RestrictedCodeSid: WellKnownSidType = ...
    """"""
    TerminalServerSid: WellKnownSidType = ...
    """"""
    RemoteLogonIdSid: WellKnownSidType = ...
    """"""
    LogonIdsSid: WellKnownSidType = ...
    """"""
    LocalSystemSid: WellKnownSidType = ...
    """"""
    LocalServiceSid: WellKnownSidType = ...
    """"""
    NetworkServiceSid: WellKnownSidType = ...
    """"""
    BuiltinDomainSid: WellKnownSidType = ...
    """"""
    BuiltinAdministratorsSid: WellKnownSidType = ...
    """"""
    BuiltinUsersSid: WellKnownSidType = ...
    """"""
    BuiltinGuestsSid: WellKnownSidType = ...
    """"""
    BuiltinPowerUsersSid: WellKnownSidType = ...
    """"""
    BuiltinAccountOperatorsSid: WellKnownSidType = ...
    """"""
    BuiltinSystemOperatorsSid: WellKnownSidType = ...
    """"""
    BuiltinPrintOperatorsSid: WellKnownSidType = ...
    """"""
    BuiltinBackupOperatorsSid: WellKnownSidType = ...
    """"""
    BuiltinReplicatorSid: WellKnownSidType = ...
    """"""
    BuiltinPreWindows2000CompatibleAccessSid: WellKnownSidType = ...
    """"""
    BuiltinRemoteDesktopUsersSid: WellKnownSidType = ...
    """"""
    BuiltinNetworkConfigurationOperatorsSid: WellKnownSidType = ...
    """"""
    AccountAdministratorSid: WellKnownSidType = ...
    """"""
    AccountGuestSid: WellKnownSidType = ...
    """"""
    AccountKrbtgtSid: WellKnownSidType = ...
    """"""
    AccountDomainAdminsSid: WellKnownSidType = ...
    """"""
    AccountDomainUsersSid: WellKnownSidType = ...
    """"""
    AccountDomainGuestsSid: WellKnownSidType = ...
    """"""
    AccountComputersSid: WellKnownSidType = ...
    """"""
    AccountControllersSid: WellKnownSidType = ...
    """"""
    AccountCertAdminsSid: WellKnownSidType = ...
    """"""
    AccountSchemaAdminsSid: WellKnownSidType = ...
    """"""
    AccountEnterpriseAdminsSid: WellKnownSidType = ...
    """"""
    AccountPolicyAdminsSid: WellKnownSidType = ...
    """"""
    AccountRasAndIasServersSid: WellKnownSidType = ...
    """"""
    NtlmAuthenticationSid: WellKnownSidType = ...
    """"""
    DigestAuthenticationSid: WellKnownSidType = ...
    """"""
    SChannelAuthenticationSid: WellKnownSidType = ...
    """"""
    ThisOrganizationSid: WellKnownSidType = ...
    """"""
    OtherOrganizationSid: WellKnownSidType = ...
    """"""
    BuiltinIncomingForestTrustBuildersSid: WellKnownSidType = ...
    """"""
    BuiltinPerformanceMonitoringUsersSid: WellKnownSidType = ...
    """"""
    BuiltinPerformanceLoggingUsersSid: WellKnownSidType = ...
    """"""
    BuiltinAuthorizationAccessSid: WellKnownSidType = ...
    """"""
    WinBuiltinTerminalServerLicenseServersSid: WellKnownSidType = ...
    """"""
    MaxDefined: WellKnownSidType = ...
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

class WinSecurityContext(Enum):
    """"""

    Thread: WinSecurityContext = ...
    """"""
    Process: WinSecurityContext = ...
    """"""
    Both: WinSecurityContext = ...
    """"""

class WindowsAccountType(Enum):
    """"""

    Normal: WindowsAccountType = ...
    """"""
    Guest: WindowsAccountType = ...
    """"""
    System: WindowsAccountType = ...
    """"""
    Anonymous: WindowsAccountType = ...
    """"""

class WindowsBuiltInRole(Enum):
    """"""

    Administrator: WindowsBuiltInRole = ...
    """"""
    User: WindowsBuiltInRole = ...
    """"""
    Guest: WindowsBuiltInRole = ...
    """"""
    PowerUser: WindowsBuiltInRole = ...
    """"""
    AccountOperator: WindowsBuiltInRole = ...
    """"""
    SystemOperator: WindowsBuiltInRole = ...
    """"""
    PrintOperator: WindowsBuiltInRole = ...
    """"""
    BackupOperator: WindowsBuiltInRole = ...
    """"""
    Replicator: WindowsBuiltInRole = ...
    """"""

class WindowsIdentity(
    ClaimsIdentity, IDeserializationCallback, ISerializable, IIdentity, IDisposable
):
    """"""

    DefaultIssuer: ClassVar[str]
    """"""
    @overload
    def __init__(self, userToken: IntPtr) -> None:
        """"""
    @overload
    def __init__(self, userToken: IntPtr, type: str) -> None:
        """"""
    @overload
    def __init__(self, userToken: IntPtr, type: str, acctType: WindowsAccountType) -> None:
        """"""
    @overload
    def __init__(
        self, userToken: IntPtr, type: str, acctType: WindowsAccountType, isAuthenticated: bool
    ) -> None:
        """"""
    @overload
    def __init__(self, sUserPrincipalName: str) -> None:
        """"""
    @overload
    def __init__(self, sUserPrincipalName: str, type: str) -> None:
        """"""
    @overload
    def __init__(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    @property
    def AccessToken(self) -> SafeAccessTokenHandle:
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
    def DeviceClaims(self) -> IEnumerable[Claim]:
        """"""
    @property
    def Groups(self) -> IdentityReferenceCollection:
        """"""
    @property
    def ImpersonationLevel(self) -> TokenImpersonationLevel:
        """"""
    @property
    def IsAnonymous(self) -> bool:
        """"""
    @property
    def IsAuthenticated(self) -> bool:
        """"""
    @property
    def IsGuest(self) -> bool:
        """"""
    @property
    def IsSystem(self) -> bool:
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
    def Owner(self) -> SecurityIdentifier:
        """"""
    @property
    def RoleClaimType(self) -> str:
        """"""
    @property
    def Token(self) -> IntPtr:
        """"""
    @property
    def User(self) -> SecurityIdentifier:
        """"""
    @property
    def UserClaims(self) -> IEnumerable[Claim]:
        """"""
    def AddClaim(self, claim: Claim) -> None:
        """"""
    def AddClaims(self, claims: IEnumerable[Claim]) -> None:
        """"""
    def Clone(self) -> ClaimsIdentity:
        """"""
    def Dispose(self) -> None:
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
    @classmethod
    def GetAnonymous(cls) -> WindowsIdentity:
        """"""
    @classmethod
    @overload
    def GetCurrent(cls) -> WindowsIdentity:
        """"""
    @classmethod
    @overload
    def GetCurrent(cls, desiredAccess: TokenAccessLevels) -> WindowsIdentity:
        """"""
    @classmethod
    @overload
    def GetCurrent(cls, ifImpersonating: bool) -> WindowsIdentity:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def HasClaim(self, match: Predicate[Claim]) -> bool:
        """"""
    @overload
    def HasClaim(self, type: str, value: str) -> bool:
        """"""
    @overload
    def Impersonate(self) -> WindowsImpersonationContext:
        """"""
    @classmethod
    @overload
    def Impersonate(cls, userToken: IntPtr) -> WindowsImpersonationContext:
        """"""
    def OnDeserialization(self, sender: object) -> None:
        """"""
    def RemoveClaim(self, claim: Claim) -> None:
        """"""
    @classmethod
    @overload
    def RunImpersonated(cls, safeAccessTokenHandle: SafeAccessTokenHandle, action: Action) -> None:
        """"""
    @classmethod
    @overload
    def RunImpersonated[T](cls, safeAccessTokenHandle: SafeAccessTokenHandle, func: Func[T]) -> T:
        """"""
    def ToString(self) -> str:
        """"""
    def TryRemoveClaim(self, claim: Claim) -> bool:
        """"""
    def WriteTo(self, writer: BinaryWriter) -> None:
        """"""

class WindowsImpersonationContext(Object, IDisposable):
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
    def Undo(self) -> None:
        """"""

class WindowsPrincipal(ClaimsPrincipal, IPrincipal):
    """"""
    def __init__(self, ntIdentity: WindowsIdentity) -> None:
        """"""
    @property
    def Claims(self) -> IEnumerable[Claim]:
        """"""
    @property
    def DeviceClaims(self) -> IEnumerable[Claim]:
        """"""
    @property
    def Identities(self) -> IEnumerable[ClaimsIdentity]:
        """"""
    @property
    def Identity(self) -> IIdentity:
        """"""
    @property
    def UserClaims(self) -> IEnumerable[Claim]:
        """"""
    def AddIdentities(self, identities: IEnumerable[ClaimsIdentity]) -> None:
        """"""
    def AddIdentity(self, identity: ClaimsIdentity) -> None:
        """"""
    def Clone(self) -> ClaimsPrincipal:
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
    @overload
    def IsInRole(self, sid: SecurityIdentifier) -> bool:
        """"""
    @overload
    def IsInRole(self, role: WindowsBuiltInRole) -> bool:
        """"""
    @overload
    def IsInRole(self, rid: int) -> bool:
        """"""
    @overload
    def IsInRole(self, role: str) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    def WriteTo(self, writer: BinaryWriter) -> None:
        """"""
