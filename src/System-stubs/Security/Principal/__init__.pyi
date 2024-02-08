from __future__ import annotations

from abc import ABC
from typing import ClassVar
from typing import Final
from typing import Iterator
from typing import TypeVar
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

T = TypeVar("T")

class GenericIdentity(ClaimsIdentity, IIdentity):
    """"""

    @overload
    def __init__(self, name: str):
        """

        :param name:
        """
    @overload
    def __init__(self, name: str, type: str):
        """

        :param name:
        :param type:
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

class GenericPrincipal(ClaimsPrincipal, IPrincipal):
    """"""

    def __init__(self, identity: IIdentity, roles: Array[str]):
        """

        :param identity:
        :param roles:
        """
    @property
    def Claims(self) -> IEnumerable[Claim]:
        """

        :return:
        """
    @classmethod
    @property
    def ClaimsPrincipalSelector(cls) -> Func[ClaimsPrincipal]:
        """

        :return:
        """
    @classmethod
    @ClaimsPrincipalSelector.setter
    def ClaimsPrincipalSelector(cls, value: Func[ClaimsPrincipal]) -> None: ...
    @classmethod
    @property
    def Current(cls) -> ClaimsPrincipal:
        """

        :return:
        """
    @property
    def Identities(self) -> IEnumerable[ClaimsIdentity]:
        """

        :return:
        """
    @property
    def Identity(self) -> IIdentity:
        """

        :return:
        """
    @classmethod
    @property
    def PrimaryIdentitySelector(cls) -> Func[IEnumerable[ClaimsIdentity], ClaimsIdentity]:
        """

        :return:
        """
    @classmethod
    @PrimaryIdentitySelector.setter
    def PrimaryIdentitySelector(
        cls, value: Func[IEnumerable[ClaimsIdentity], ClaimsIdentity]
    ) -> None: ...
    def AddIdentities(self, identities: IEnumerable[ClaimsIdentity]) -> None:
        """

        :param identities:
        """
    def AddIdentity(self, identity: ClaimsIdentity) -> None:
        """

        :param identity:
        """
    def Clone(self) -> ClaimsPrincipal:
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
    def IsInRole(self, role: str) -> bool:
        """

        :param role:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def WriteTo(self, writer: BinaryWriter) -> None:
        """

        :param writer:
        """

class IIdentity:
    """"""

    @property
    def AuthenticationType(self) -> str:
        """

        :return:
        """
    @property
    def IsAuthenticated(self) -> bool:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """

class IPrincipal:
    """"""

    @property
    def Identity(self) -> IIdentity:
        """

        :return:
        """
    def IsInRole(self, role: str) -> bool:
        """

        :param role:
        :return:
        """

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
    def __init__(self):
        """"""
    @overload
    def __init__(self, message: str):
        """

        :param message:
        """
    @overload
    def __init__(self, message: str, inner: Exception):
        """

        :param message:
        :param inner:
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
    @property
    def UnmappedIdentities(self) -> IdentityReferenceCollection:
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

class IdentityReference(ABC, Object):
    """"""

    @property
    def Value(self) -> str:
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
    def IsValidTargetType(self, targetType: Type) -> bool:
        """

        :param targetType:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Translate(self, targetType: Type) -> IdentityReference:
        """

        :param targetType:
        :return:
        """
    def __eq__(self, other: IdentityReference) -> bool:
        """

        :param other:
        :return:
        """
    def __ne__(self, other: IdentityReference) -> bool:
        """

        :param other:
        :return:
        """
    @classmethod
    def op_Equality(cls, left: IdentityReference, right: IdentityReference) -> bool:
        """

        :param left:
        :param right:
        :return:
        """
    @classmethod
    def op_Inequality(cls, left: IdentityReference, right: IdentityReference) -> bool:
        """

        :param left:
        :param right:
        :return:
        """

class IdentityReferenceCollection(
    Object, ICollection[IdentityReference], IEnumerable[IdentityReference], IEnumerable
):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, capacity: int):
        """

        :param capacity:
        """
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
    def Item(self) -> IdentityReference:
        """

        :return:
        """
    @Item.setter
    def Item(self, value: IdentityReference) -> None: ...
    def Add(self, item: IdentityReference) -> None:
        """

        :param item:
        """
    def Clear(self) -> None:
        """"""
    def Contains(self, item: IdentityReference) -> bool:
        """

        :param item:
        :return:
        """
    def CopyTo(self, array: Array[IdentityReference], arrayIndex: int) -> None:
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
    def Remove(self, item: IdentityReference) -> bool:
        """

        :param item:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def Translate(self, targetType: Type) -> IdentityReferenceCollection:
        """

        :param targetType:
        :return:
        """
    @overload
    def Translate(self, targetType: Type, forceSuccess: bool) -> IdentityReferenceCollection:
        """

        :param targetType:
        :param forceSuccess:
        :return:
        """
    def __contains__(self, value: IdentityReference) -> bool:
        """

        :param value:
        :return:
        """
    def __getitem__(self, index: int) -> IdentityReference:
        """

        :param index:
        :return:
        """
    @overload
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[IdentityReference]:
        """

        :return:
        """
    def __len__(self) -> int:
        """

        :return:
        """
    def __setitem__(self, index: int, value: IdentityReference) -> None:
        """

        :param index:
        :param value:
        """

class IdentityReferenceEnumerator(Object, IEnumerator[IdentityReference], IEnumerator, IDisposable):
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
    def __init__(self, name: str):
        """

        :param name:
        """
    @overload
    def __init__(self, domainName: str, accountName: str):
        """

        :param domainName:
        :param accountName:
        """
    @property
    def Value(self) -> str:
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
    def IsValidTargetType(self, targetType: Type) -> bool:
        """

        :param targetType:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Translate(self, targetType: Type) -> IdentityReference:
        """

        :param targetType:
        :return:
        """
    def __eq__(self, other: NTAccount) -> bool:
        """

        :param other:
        :return:
        """
    def __ne__(self, other: NTAccount) -> bool:
        """

        :param other:
        :return:
        """
    @classmethod
    def op_Equality(cls, left: NTAccount, right: NTAccount) -> bool:
        """

        :param left:
        :param right:
        :return:
        """
    @classmethod
    def op_Inequality(cls, left: NTAccount, right: NTAccount) -> bool:
        """

        :param left:
        :param right:
        :return:
        """

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

    MaxBinaryLength: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    MinBinaryLength: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    @overload
    def __init__(self, binaryForm: IntPtr):
        """

        :param binaryForm:
        """
    @overload
    def __init__(self, sddlForm: str):
        """

        :param sddlForm:
        """
    @overload
    def __init__(self, sidType: WellKnownSidType, domainSid: SecurityIdentifier):
        """

        :param sidType:
        :param domainSid:
        """
    @overload
    def __init__(self, binaryForm: Array[int], offset: int):
        """

        :param binaryForm:
        :param offset:
        """
    @property
    def AccountDomainSid(self) -> SecurityIdentifier:
        """

        :return:
        """
    @property
    def BinaryLength(self) -> int:
        """

        :return:
        """
    @property
    def Value(self) -> str:
        """

        :return:
        """
    def CompareTo(self, other: SecurityIdentifier) -> int:
        """

        :param other:
        :return:
        """
    @overload
    def Equals(self, sid: SecurityIdentifier) -> bool:
        """

        :param sid:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetBinaryForm(self, binaryForm: Array[int], offset: int) -> None:
        """

        :param binaryForm:
        :param offset:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def IsAccountSid(self) -> bool:
        """

        :return:
        """
    def IsEqualDomainSid(self, sid: SecurityIdentifier) -> bool:
        """

        :param sid:
        :return:
        """
    def IsValidTargetType(self, targetType: Type) -> bool:
        """

        :param targetType:
        :return:
        """
    def IsWellKnown(self, type: WellKnownSidType) -> bool:
        """

        :param type:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Translate(self, targetType: Type) -> IdentityReference:
        """

        :param targetType:
        :return:
        """
    def __eq__(self, other: SecurityIdentifier) -> bool:
        """

        :param other:
        :return:
        """
    def __ne__(self, other: SecurityIdentifier) -> bool:
        """

        :param other:
        :return:
        """
    @classmethod
    def op_Equality(cls, left: SecurityIdentifier, right: SecurityIdentifier) -> bool:
        """

        :param left:
        :param right:
        :return:
        """
    @classmethod
    def op_Inequality(cls, left: SecurityIdentifier, right: SecurityIdentifier) -> bool:
        """

        :param left:
        :param right:
        :return:
        """

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

    DefaultIssuer: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    @overload
    def __init__(self, userToken: IntPtr):
        """

        :param userToken:
        """
    @overload
    def __init__(self, sUserPrincipalName: str):
        """

        :param sUserPrincipalName:
        """
    @overload
    def __init__(self, info: SerializationInfo, context: StreamingContext):
        """

        :param info:
        :param context:
        """
    @overload
    def __init__(self, userToken: IntPtr, type: str):
        """

        :param userToken:
        :param type:
        """
    @overload
    def __init__(self, sUserPrincipalName: str, type: str):
        """

        :param sUserPrincipalName:
        :param type:
        """
    @overload
    def __init__(self, userToken: IntPtr, type: str, acctType: WindowsAccountType):
        """

        :param userToken:
        :param type:
        :param acctType:
        """
    @overload
    def __init__(
        self, userToken: IntPtr, type: str, acctType: WindowsAccountType, isAuthenticated: bool
    ):
        """

        :param userToken:
        :param type:
        :param acctType:
        :param isAuthenticated:
        """
    @property
    def AccessToken(self) -> SafeAccessTokenHandle:
        """

        :return:
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
    def DeviceClaims(self) -> IEnumerable[Claim]:
        """

        :return:
        """
    @property
    def Groups(self) -> IdentityReferenceCollection:
        """

        :return:
        """
    @property
    def ImpersonationLevel(self) -> TokenImpersonationLevel:
        """

        :return:
        """
    @property
    def IsAnonymous(self) -> bool:
        """

        :return:
        """
    @property
    def IsAuthenticated(self) -> bool:
        """

        :return:
        """
    @property
    def IsGuest(self) -> bool:
        """

        :return:
        """
    @property
    def IsSystem(self) -> bool:
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
    def Owner(self) -> SecurityIdentifier:
        """

        :return:
        """
    @property
    def RoleClaimType(self) -> str:
        """

        :return:
        """
    @property
    def Token(self) -> IntPtr:
        """

        :return:
        """
    @property
    def User(self) -> SecurityIdentifier:
        """

        :return:
        """
    @property
    def UserClaims(self) -> IEnumerable[Claim]:
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
    def Dispose(self) -> None:
        """"""
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
    @classmethod
    def GetAnonymous(cls) -> WindowsIdentity:
        """

        :return:
        """
    @classmethod
    @overload
    def GetCurrent(cls) -> WindowsIdentity:
        """

        :return:
        """
    @classmethod
    @overload
    def GetCurrent(cls, desiredAccess: TokenAccessLevels) -> WindowsIdentity:
        """

        :param desiredAccess:
        :return:
        """
    @classmethod
    @overload
    def GetCurrent(cls, ifImpersonating: bool) -> WindowsIdentity:
        """

        :param ifImpersonating:
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
    @overload
    def Impersonate(self) -> WindowsImpersonationContext:
        """

        :return:
        """
    @classmethod
    @overload
    def Impersonate(cls, userToken: IntPtr) -> WindowsImpersonationContext:
        """

        :param userToken:
        :return:
        """
    def OnDeserialization(self, sender: object) -> None:
        """

        :param sender:
        """
    def RemoveClaim(self, claim: Claim) -> None:
        """

        :param claim:
        """
    @classmethod
    @overload
    def RunImpersonated(cls, safeAccessTokenHandle: SafeAccessTokenHandle, action: Action) -> None:
        """

        :param safeAccessTokenHandle:
        :param action:
        """
    @classmethod
    @overload
    def RunImpersonated(cls, safeAccessTokenHandle: SafeAccessTokenHandle, func: Func[T]) -> T:
        """

        :param safeAccessTokenHandle:
        :param func:
        :return:
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

class WindowsImpersonationContext(Object, IDisposable):
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
    def Undo(self) -> None:
        """"""

class WindowsPrincipal(ClaimsPrincipal, IPrincipal):
    """"""

    def __init__(self, ntIdentity: WindowsIdentity):
        """

        :param ntIdentity:
        """
    @property
    def Claims(self) -> IEnumerable[Claim]:
        """

        :return:
        """
    @classmethod
    @property
    def ClaimsPrincipalSelector(cls) -> Func[ClaimsPrincipal]:
        """

        :return:
        """
    @classmethod
    @ClaimsPrincipalSelector.setter
    def ClaimsPrincipalSelector(cls, value: Func[ClaimsPrincipal]) -> None: ...
    @classmethod
    @property
    def Current(cls) -> ClaimsPrincipal:
        """

        :return:
        """
    @property
    def DeviceClaims(self) -> IEnumerable[Claim]:
        """

        :return:
        """
    @property
    def Identities(self) -> IEnumerable[ClaimsIdentity]:
        """

        :return:
        """
    @property
    def Identity(self) -> IIdentity:
        """

        :return:
        """
    @classmethod
    @property
    def PrimaryIdentitySelector(cls) -> Func[IEnumerable[ClaimsIdentity], ClaimsIdentity]:
        """

        :return:
        """
    @classmethod
    @PrimaryIdentitySelector.setter
    def PrimaryIdentitySelector(
        cls, value: Func[IEnumerable[ClaimsIdentity], ClaimsIdentity]
    ) -> None: ...
    @property
    def UserClaims(self) -> IEnumerable[Claim]:
        """

        :return:
        """
    def AddIdentities(self, identities: IEnumerable[ClaimsIdentity]) -> None:
        """

        :param identities:
        """
    def AddIdentity(self, identity: ClaimsIdentity) -> None:
        """

        :param identity:
        """
    def Clone(self) -> ClaimsPrincipal:
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
    @overload
    def IsInRole(self, sid: SecurityIdentifier) -> bool:
        """

        :param sid:
        :return:
        """
    @overload
    def IsInRole(self, role: WindowsBuiltInRole) -> bool:
        """

        :param role:
        :return:
        """
    @overload
    def IsInRole(self, rid: int) -> bool:
        """

        :param rid:
        :return:
        """
    @overload
    def IsInRole(self, role: str) -> bool:
        """

        :param role:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def WriteTo(self, writer: BinaryWriter) -> None:
        """

        :param writer:
        """
