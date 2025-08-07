"""Automatically generated stubs for C# namespace: System.Security.Claims."""

from abc import ABC
from typing import ClassVar
from typing import overload

from System import Array
from System import Func
from System import Object
from System import Predicate
from System import Type
from System.Collections.Generic import IDictionary
from System.Collections.Generic import IEnumerable
from System.IO import BinaryReader
from System.IO import BinaryWriter
from System.Security.Principal import IIdentity
from System.Security.Principal import IPrincipal

class Claim(Object):
    """"""
    @overload
    def __init__(self, reader: BinaryReader) -> None:
        """"""
    @overload
    def __init__(self, reader: BinaryReader, subject: ClaimsIdentity) -> None:
        """"""
    @overload
    def __init__(self, type: str, value: str) -> None:
        """"""
    @overload
    def __init__(self, type: str, value: str, valueType: str) -> None:
        """"""
    @overload
    def __init__(self, type: str, value: str, valueType: str, issuer: str) -> None:
        """"""
    @overload
    def __init__(
        self, type: str, value: str, valueType: str, issuer: str, originalIssuer: str
    ) -> None:
        """"""
    @overload
    def __init__(
        self,
        type: str,
        value: str,
        valueType: str,
        issuer: str,
        originalIssuer: str,
        subject: ClaimsIdentity,
    ) -> None:
        """"""
    @property
    def Issuer(self) -> str:
        """"""
    @property
    def OriginalIssuer(self) -> str:
        """"""
    @property
    def Properties(self) -> IDictionary[str, str]:
        """"""
    @property
    def Subject(self) -> ClaimsIdentity:
        """"""
    @property
    def Type(self) -> str:
        """"""
    @property
    def Value(self) -> str:
        """"""
    @property
    def ValueType(self) -> str:
        """"""
    @overload
    def Clone(self) -> Claim:
        """"""
    @overload
    def Clone(self, identity: ClaimsIdentity) -> Claim:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def WriteTo(self, writer: BinaryWriter) -> None:
        """"""

class ClaimTypes(ABC, Object):
    """"""

    Actor: ClassVar[str]
    """"""
    Anonymous: ClassVar[str]
    """"""
    Authentication: ClassVar[str]
    """"""
    AuthenticationInstant: ClassVar[str]
    """"""
    AuthenticationMethod: ClassVar[str]
    """"""
    AuthorizationDecision: ClassVar[str]
    """"""
    CookiePath: ClassVar[str]
    """"""
    Country: ClassVar[str]
    """"""
    DateOfBirth: ClassVar[str]
    """"""
    DenyOnlyPrimaryGroupSid: ClassVar[str]
    """"""
    DenyOnlyPrimarySid: ClassVar[str]
    """"""
    DenyOnlySid: ClassVar[str]
    """"""
    DenyOnlyWindowsDeviceGroup: ClassVar[str]
    """"""
    Dns: ClassVar[str]
    """"""
    Dsa: ClassVar[str]
    """"""
    Email: ClassVar[str]
    """"""
    Expiration: ClassVar[str]
    """"""
    Expired: ClassVar[str]
    """"""
    Gender: ClassVar[str]
    """"""
    GivenName: ClassVar[str]
    """"""
    GroupSid: ClassVar[str]
    """"""
    Hash: ClassVar[str]
    """"""
    HomePhone: ClassVar[str]
    """"""
    IsPersistent: ClassVar[str]
    """"""
    Locality: ClassVar[str]
    """"""
    MobilePhone: ClassVar[str]
    """"""
    Name: ClassVar[str]
    """"""
    NameIdentifier: ClassVar[str]
    """"""
    OtherPhone: ClassVar[str]
    """"""
    PostalCode: ClassVar[str]
    """"""
    PrimaryGroupSid: ClassVar[str]
    """"""
    PrimarySid: ClassVar[str]
    """"""
    Role: ClassVar[str]
    """"""
    Rsa: ClassVar[str]
    """"""
    SerialNumber: ClassVar[str]
    """"""
    Sid: ClassVar[str]
    """"""
    Spn: ClassVar[str]
    """"""
    StateOrProvince: ClassVar[str]
    """"""
    StreetAddress: ClassVar[str]
    """"""
    Surname: ClassVar[str]
    """"""
    System: ClassVar[str]
    """"""
    Thumbprint: ClassVar[str]
    """"""
    Upn: ClassVar[str]
    """"""
    Uri: ClassVar[str]
    """"""
    UserData: ClassVar[str]
    """"""
    Version: ClassVar[str]
    """"""
    Webpage: ClassVar[str]
    """"""
    WindowsAccountName: ClassVar[str]
    """"""
    WindowsDeviceClaim: ClassVar[str]
    """"""
    WindowsDeviceGroup: ClassVar[str]
    """"""
    WindowsFqbnVersion: ClassVar[str]
    """"""
    WindowsSubAuthority: ClassVar[str]
    """"""
    WindowsUserClaim: ClassVar[str]
    """"""
    X500DistinguishedName: ClassVar[str]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ClaimValueTypes(ABC, Object):
    """"""

    Base64Binary: ClassVar[str]
    """"""
    Base64Octet: ClassVar[str]
    """"""
    Boolean: ClassVar[str]
    """"""
    Date: ClassVar[str]
    """"""
    DateTime: ClassVar[str]
    """"""
    DaytimeDuration: ClassVar[str]
    """"""
    DnsName: ClassVar[str]
    """"""
    Double: ClassVar[str]
    """"""
    DsaKeyValue: ClassVar[str]
    """"""
    Email: ClassVar[str]
    """"""
    Fqbn: ClassVar[str]
    """"""
    HexBinary: ClassVar[str]
    """"""
    Integer: ClassVar[str]
    """"""
    Integer32: ClassVar[str]
    """"""
    Integer64: ClassVar[str]
    """"""
    KeyInfo: ClassVar[str]
    """"""
    Rfc822Name: ClassVar[str]
    """"""
    Rsa: ClassVar[str]
    """"""
    RsaKeyValue: ClassVar[str]
    """"""
    Sid: ClassVar[str]
    """"""
    String: ClassVar[str]
    """"""
    Time: ClassVar[str]
    """"""
    UInteger32: ClassVar[str]
    """"""
    UInteger64: ClassVar[str]
    """"""
    UpnName: ClassVar[str]
    """"""
    X500Name: ClassVar[str]
    """"""
    YearMonthDuration: ClassVar[str]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ClaimsIdentity(Object, IIdentity):
    """"""

    DefaultIssuer: ClassVar[str]
    """"""
    DefaultNameClaimType: ClassVar[str]
    """"""
    DefaultRoleClaimType: ClassVar[str]
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, identity: IIdentity) -> None:
        """"""
    @overload
    def __init__(self, claims: IEnumerable[Claim]) -> None:
        """"""
    @overload
    def __init__(self, authenticationType: str) -> None:
        """"""
    @overload
    def __init__(self, claims: IEnumerable[Claim], authenticationType: str) -> None:
        """"""
    @overload
    def __init__(self, identity: IIdentity, claims: IEnumerable[Claim]) -> None:
        """"""
    @overload
    def __init__(self, authenticationType: str, nameType: str, roleType: str) -> None:
        """"""
    @overload
    def __init__(
        self, claims: IEnumerable[Claim], authenticationType: str, nameType: str, roleType: str
    ) -> None:
        """"""
    @overload
    def __init__(
        self,
        identity: IIdentity,
        claims: IEnumerable[Claim],
        authenticationType: str,
        nameType: str,
        roleType: str,
    ) -> None:
        """"""
    @overload
    def __init__(self, reader: BinaryReader) -> None:
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

class ClaimsPrincipal(Object, IPrincipal):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, identities: IEnumerable[ClaimsIdentity]) -> None:
        """"""
    @overload
    def __init__(self, identity: IIdentity) -> None:
        """"""
    @overload
    def __init__(self, principal: IPrincipal) -> None:
        """"""
    @overload
    def __init__(self, reader: BinaryReader) -> None:
        """"""
    @property
    def Claims(self) -> IEnumerable[Claim]:
        """"""
    @classmethod
    @property
    def ClaimsPrincipalSelector(cls) -> Func[ClaimsPrincipal]:
        """"""
    @classmethod
    @ClaimsPrincipalSelector.setter
    def ClaimsPrincipalSelector(cls, value: Func[ClaimsPrincipal]) -> None: ...
    @classmethod
    @property
    def Current(cls) -> ClaimsPrincipal:
        """"""
    @property
    def Identities(self) -> IEnumerable[ClaimsIdentity]:
        """"""
    @property
    def Identity(self) -> IIdentity:
        """"""
    @classmethod
    @property
    def PrimaryIdentitySelector(cls) -> Func[IEnumerable[ClaimsIdentity], ClaimsIdentity]:
        """"""
    @classmethod
    @PrimaryIdentitySelector.setter
    def PrimaryIdentitySelector(
        cls, value: Func[IEnumerable[ClaimsIdentity], ClaimsIdentity]
    ) -> None: ...
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

class DynamicRoleClaimProvider(ABC, Object):
    """"""
    @classmethod
    def AddDynamicRoleClaims(
        cls, claimsIdentity: ClaimsIdentity, claims: IEnumerable[Claim]
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

class RoleClaimProvider(Object):
    """"""
    def __init__(self, issuer: str, roles: Array[str], subject: ClaimsIdentity) -> None:
        """"""
    @property
    def Claims(self) -> IEnumerable[Claim]:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
