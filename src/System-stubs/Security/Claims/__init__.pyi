from __future__ import annotations

from abc import ABC
from typing import ClassVar
from typing import Final
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
    def __init__(self, reader: BinaryReader):
        """

        :param reader:
        """
    @overload
    def __init__(self, reader: BinaryReader, subject: ClaimsIdentity):
        """

        :param reader:
        :param subject:
        """
    @overload
    def __init__(self, type: str, value: str):
        """

        :param type:
        :param value:
        """
    @overload
    def __init__(self, type: str, value: str, valueType: str):
        """

        :param type:
        :param value:
        :param valueType:
        """
    @overload
    def __init__(self, type: str, value: str, valueType: str, issuer: str):
        """

        :param type:
        :param value:
        :param valueType:
        :param issuer:
        """
    @overload
    def __init__(self, type: str, value: str, valueType: str, issuer: str, originalIssuer: str):
        """

        :param type:
        :param value:
        :param valueType:
        :param issuer:
        :param originalIssuer:
        """
    @overload
    def __init__(
        self,
        type: str,
        value: str,
        valueType: str,
        issuer: str,
        originalIssuer: str,
        subject: ClaimsIdentity,
    ):
        """

        :param type:
        :param value:
        :param valueType:
        :param issuer:
        :param originalIssuer:
        :param subject:
        """
    @property
    def Issuer(self) -> str:
        """

        :return:
        """
    @property
    def OriginalIssuer(self) -> str:
        """

        :return:
        """
    @property
    def Properties(self) -> IDictionary[str, str]:
        """

        :return:
        """
    @property
    def Subject(self) -> ClaimsIdentity:
        """

        :return:
        """
    @property
    def Type(self) -> str:
        """

        :return:
        """
    @property
    def Value(self) -> str:
        """

        :return:
        """
    @property
    def ValueType(self) -> str:
        """

        :return:
        """
    @overload
    def Clone(self) -> Claim:
        """

        :return:
        """
    @overload
    def Clone(self, identity: ClaimsIdentity) -> Claim:
        """

        :param identity:
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
    def WriteTo(self, writer: BinaryWriter) -> None:
        """

        :param writer:
        """

class ClaimTypes(ABC, Object):
    """"""

    Actor: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Anonymous: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Authentication: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    AuthenticationInstant: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    AuthenticationMethod: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    AuthorizationDecision: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    CookiePath: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Country: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    DateOfBirth: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    DenyOnlyPrimaryGroupSid: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    DenyOnlyPrimarySid: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    DenyOnlySid: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    DenyOnlyWindowsDeviceGroup: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Dns: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Dsa: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Email: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Expiration: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Expired: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Gender: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    GivenName: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    GroupSid: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Hash: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    HomePhone: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    IsPersistent: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Locality: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    MobilePhone: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Name: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    NameIdentifier: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    OtherPhone: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    PostalCode: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    PrimaryGroupSid: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    PrimarySid: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Role: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Rsa: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    SerialNumber: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Sid: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Spn: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    StateOrProvince: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    StreetAddress: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Surname: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    System: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Thumbprint: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Upn: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Uri: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    UserData: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Version: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Webpage: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    WindowsAccountName: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    WindowsDeviceClaim: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    WindowsDeviceGroup: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    WindowsFqbnVersion: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    WindowsSubAuthority: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    WindowsUserClaim: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    X500DistinguishedName: Final[ClassVar[str]] = ...
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

class ClaimValueTypes(ABC, Object):
    """"""

    Base64Binary: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Base64Octet: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Boolean: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Date: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    DateTime: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    DaytimeDuration: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    DnsName: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Double: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    DsaKeyValue: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Email: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Fqbn: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    HexBinary: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Integer: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Integer32: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Integer64: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    KeyInfo: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Rfc822Name: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Rsa: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    RsaKeyValue: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Sid: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    String: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Time: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    UInteger32: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    UInteger64: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    UpnName: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    X500Name: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    YearMonthDuration: Final[ClassVar[str]] = ...
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

class ClaimsIdentity(Object, IIdentity):
    """"""

    DefaultIssuer: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    DefaultNameClaimType: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    DefaultRoleClaimType: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, claims: IEnumerable[Claim]):
        """

        :param claims:
        """
    @overload
    def __init__(self, reader: BinaryReader):
        """

        :param reader:
        """
    @overload
    def __init__(self, identity: IIdentity):
        """

        :param identity:
        """
    @overload
    def __init__(self, authenticationType: str):
        """

        :param authenticationType:
        """
    @overload
    def __init__(self, claims: IEnumerable[Claim], authenticationType: str):
        """

        :param claims:
        :param authenticationType:
        """
    @overload
    def __init__(self, identity: IIdentity, claims: IEnumerable[Claim]):
        """

        :param identity:
        :param claims:
        """
    @overload
    def __init__(self, authenticationType: str, nameType: str, roleType: str):
        """

        :param authenticationType:
        :param nameType:
        :param roleType:
        """
    @overload
    def __init__(
        self, claims: IEnumerable[Claim], authenticationType: str, nameType: str, roleType: str
    ):
        """

        :param claims:
        :param authenticationType:
        :param nameType:
        :param roleType:
        """
    @overload
    def __init__(
        self,
        identity: IIdentity,
        claims: IEnumerable[Claim],
        authenticationType: str,
        nameType: str,
        roleType: str,
    ):
        """

        :param identity:
        :param claims:
        :param authenticationType:
        :param nameType:
        :param roleType:
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

class ClaimsPrincipal(Object, IPrincipal):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, identities: IEnumerable[ClaimsIdentity]):
        """

        :param identities:
        """
    @overload
    def __init__(self, reader: BinaryReader):
        """

        :param reader:
        """
    @overload
    def __init__(self, identity: IIdentity):
        """

        :param identity:
        """
    @overload
    def __init__(self, principal: IPrincipal):
        """

        :param principal:
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

class DynamicRoleClaimProvider(ABC, Object):
    """"""

    @classmethod
    def AddDynamicRoleClaims(
        cls, claimsIdentity: ClaimsIdentity, claims: IEnumerable[Claim]
    ) -> None:
        """

        :param claimsIdentity:
        :param claims:
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

class RoleClaimProvider(Object):
    """"""

    def __init__(self, issuer: str, roles: Array[str], subject: ClaimsIdentity):
        """

        :param issuer:
        :param roles:
        :param subject:
        """
    @property
    def Claims(self) -> IEnumerable[Claim]:
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
