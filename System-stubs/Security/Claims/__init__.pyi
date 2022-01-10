from __future__ import annotations

from abc import ABC
from typing import List, Union, overload

from System import Array, Boolean, Func, Object, Predicate, String, Void
from System.Collections.Generic import IDictionary, IEnumerable
from System.IO import BinaryReader, BinaryWriter
from System.Security.Principal import IIdentity, IPrincipal

# ---------- Types ---------- #

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
ObjectType = Object
StringType = Union[str, String]
VoidType = Union[None, Void]

# ---------- Classes ---------- #

class Claim(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, reader: BinaryReader): ...
    
    @overload
    def __init__(self, reader: BinaryReader, subject: ClaimsIdentity): ...
    
    @overload
    def __init__(self, type: StringType, value: StringType): ...
    
    @overload
    def __init__(self, type: StringType, value: StringType, valueType: StringType): ...
    
    @overload
    def __init__(self, type: StringType, value: StringType, valueType: StringType, issuer: StringType): ...
    
    @overload
    def __init__(self, type: StringType, value: StringType, valueType: StringType, issuer: StringType, originalIssuer: StringType): ...
    
    @overload
    def __init__(self, type: StringType, value: StringType, valueType: StringType, issuer: StringType, originalIssuer: StringType, subject: ClaimsIdentity): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Issuer(self) -> StringType: ...
    
    @property
    def OriginalIssuer(self) -> StringType: ...
    
    @property
    def Properties(self) -> IDictionary[StringType, StringType]: ...
    
    @property
    def Subject(self) -> ClaimsIdentity: ...
    
    @property
    def Type(self) -> StringType: ...
    
    @property
    def Value(self) -> StringType: ...
    
    @property
    def ValueType(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Clone(self) -> Claim: ...
    
    @overload
    def Clone(self, identity: ClaimsIdentity) -> Claim: ...
    
    def ToString(self) -> StringType: ...
    
    def WriteTo(self, writer: BinaryWriter) -> VoidType: ...
    
    def get_Issuer(self) -> StringType: ...
    
    def get_OriginalIssuer(self) -> StringType: ...
    
    def get_Properties(self) -> IDictionary[StringType, StringType]: ...
    
    def get_Subject(self) -> ClaimsIdentity: ...
    
    def get_Type(self) -> StringType: ...
    
    def get_Value(self) -> StringType: ...
    
    def get_ValueType(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Claim(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, reader: BinaryReader): ...
    
    @overload
    def __init__(self, reader: BinaryReader, subject: ClaimsIdentity): ...
    
    @overload
    def __init__(self, type: StringType, value: StringType): ...
    
    @overload
    def __init__(self, type: StringType, value: StringType, valueType: StringType): ...
    
    @overload
    def __init__(self, type: StringType, value: StringType, valueType: StringType, issuer: StringType): ...
    
    @overload
    def __init__(self, type: StringType, value: StringType, valueType: StringType, issuer: StringType, originalIssuer: StringType): ...
    
    @overload
    def __init__(self, type: StringType, value: StringType, valueType: StringType, issuer: StringType, originalIssuer: StringType, subject: ClaimsIdentity): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Issuer(self) -> StringType: ...
    
    @property
    def OriginalIssuer(self) -> StringType: ...
    
    @property
    def Properties(self) -> IDictionary[StringType, StringType]: ...
    
    @property
    def Subject(self) -> ClaimsIdentity: ...
    
    @property
    def Type(self) -> StringType: ...
    
    @property
    def Value(self) -> StringType: ...
    
    @property
    def ValueType(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Clone(self) -> Claim: ...
    
    @overload
    def Clone(self, identity: ClaimsIdentity) -> Claim: ...
    
    def ToString(self) -> StringType: ...
    
    def WriteTo(self, writer: BinaryWriter) -> VoidType: ...
    
    def get_Issuer(self) -> StringType: ...
    
    def get_OriginalIssuer(self) -> StringType: ...
    
    def get_Properties(self) -> IDictionary[StringType, StringType]: ...
    
    def get_Subject(self) -> ClaimsIdentity: ...
    
    def get_Type(self) -> StringType: ...
    
    def get_Value(self) -> StringType: ...
    
    def get_ValueType(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Claim(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, reader: BinaryReader): ...
    
    @overload
    def __init__(self, reader: BinaryReader, subject: ClaimsIdentity): ...
    
    @overload
    def __init__(self, type: StringType, value: StringType): ...
    
    @overload
    def __init__(self, type: StringType, value: StringType, valueType: StringType): ...
    
    @overload
    def __init__(self, type: StringType, value: StringType, valueType: StringType, issuer: StringType): ...
    
    @overload
    def __init__(self, type: StringType, value: StringType, valueType: StringType, issuer: StringType, originalIssuer: StringType): ...
    
    @overload
    def __init__(self, type: StringType, value: StringType, valueType: StringType, issuer: StringType, originalIssuer: StringType, subject: ClaimsIdentity): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Issuer(self) -> StringType: ...
    
    @property
    def OriginalIssuer(self) -> StringType: ...
    
    @property
    def Properties(self) -> IDictionary[StringType, StringType]: ...
    
    @property
    def Subject(self) -> ClaimsIdentity: ...
    
    @property
    def Type(self) -> StringType: ...
    
    @property
    def Value(self) -> StringType: ...
    
    @property
    def ValueType(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Clone(self) -> Claim: ...
    
    @overload
    def Clone(self, identity: ClaimsIdentity) -> Claim: ...
    
    def ToString(self) -> StringType: ...
    
    def WriteTo(self, writer: BinaryWriter) -> VoidType: ...
    
    def get_Issuer(self) -> StringType: ...
    
    def get_OriginalIssuer(self) -> StringType: ...
    
    def get_Properties(self) -> IDictionary[StringType, StringType]: ...
    
    def get_Subject(self) -> ClaimsIdentity: ...
    
    def get_Type(self) -> StringType: ...
    
    def get_Value(self) -> StringType: ...
    
    def get_ValueType(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ClaimTypes(ABC, ObjectType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Actor() -> StringType: ...
    
    @staticmethod
    @property
    def Anonymous() -> StringType: ...
    
    @staticmethod
    @property
    def Authentication() -> StringType: ...
    
    @staticmethod
    @property
    def AuthenticationInstant() -> StringType: ...
    
    @staticmethod
    @property
    def AuthenticationMethod() -> StringType: ...
    
    @staticmethod
    @property
    def AuthorizationDecision() -> StringType: ...
    
    @staticmethod
    @property
    def CookiePath() -> StringType: ...
    
    @staticmethod
    @property
    def Country() -> StringType: ...
    
    @staticmethod
    @property
    def DateOfBirth() -> StringType: ...
    
    @staticmethod
    @property
    def DenyOnlyPrimaryGroupSid() -> StringType: ...
    
    @staticmethod
    @property
    def DenyOnlyPrimarySid() -> StringType: ...
    
    @staticmethod
    @property
    def DenyOnlySid() -> StringType: ...
    
    @staticmethod
    @property
    def DenyOnlyWindowsDeviceGroup() -> StringType: ...
    
    @staticmethod
    @property
    def Dns() -> StringType: ...
    
    @staticmethod
    @property
    def Dsa() -> StringType: ...
    
    @staticmethod
    @property
    def Email() -> StringType: ...
    
    @staticmethod
    @property
    def Expiration() -> StringType: ...
    
    @staticmethod
    @property
    def Expired() -> StringType: ...
    
    @staticmethod
    @property
    def Gender() -> StringType: ...
    
    @staticmethod
    @property
    def GivenName() -> StringType: ...
    
    @staticmethod
    @property
    def GroupSid() -> StringType: ...
    
    @staticmethod
    @property
    def Hash() -> StringType: ...
    
    @staticmethod
    @property
    def HomePhone() -> StringType: ...
    
    @staticmethod
    @property
    def IsPersistent() -> StringType: ...
    
    @staticmethod
    @property
    def Locality() -> StringType: ...
    
    @staticmethod
    @property
    def MobilePhone() -> StringType: ...
    
    @staticmethod
    @property
    def Name() -> StringType: ...
    
    @staticmethod
    @property
    def NameIdentifier() -> StringType: ...
    
    @staticmethod
    @property
    def OtherPhone() -> StringType: ...
    
    @staticmethod
    @property
    def PostalCode() -> StringType: ...
    
    @staticmethod
    @property
    def PrimaryGroupSid() -> StringType: ...
    
    @staticmethod
    @property
    def PrimarySid() -> StringType: ...
    
    @staticmethod
    @property
    def Role() -> StringType: ...
    
    @staticmethod
    @property
    def Rsa() -> StringType: ...
    
    @staticmethod
    @property
    def SerialNumber() -> StringType: ...
    
    @staticmethod
    @property
    def Sid() -> StringType: ...
    
    @staticmethod
    @property
    def Spn() -> StringType: ...
    
    @staticmethod
    @property
    def StateOrProvince() -> StringType: ...
    
    @staticmethod
    @property
    def StreetAddress() -> StringType: ...
    
    @staticmethod
    @property
    def Surname() -> StringType: ...
    
    @staticmethod
    @property
    def System() -> StringType: ...
    
    @staticmethod
    @property
    def Thumbprint() -> StringType: ...
    
    @staticmethod
    @property
    def Upn() -> StringType: ...
    
    @staticmethod
    @property
    def Uri() -> StringType: ...
    
    @staticmethod
    @property
    def UserData() -> StringType: ...
    
    @staticmethod
    @property
    def Version() -> StringType: ...
    
    @staticmethod
    @property
    def Webpage() -> StringType: ...
    
    @staticmethod
    @property
    def WindowsAccountName() -> StringType: ...
    
    @staticmethod
    @property
    def WindowsDeviceClaim() -> StringType: ...
    
    @staticmethod
    @property
    def WindowsDeviceGroup() -> StringType: ...
    
    @staticmethod
    @property
    def WindowsFqbnVersion() -> StringType: ...
    
    @staticmethod
    @property
    def WindowsSubAuthority() -> StringType: ...
    
    @staticmethod
    @property
    def WindowsUserClaim() -> StringType: ...
    
    @staticmethod
    @property
    def X500DistinguishedName() -> StringType: ...
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ClaimTypes(ABC, ObjectType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Actor() -> StringType: ...
    
    @staticmethod
    @property
    def Anonymous() -> StringType: ...
    
    @staticmethod
    @property
    def Authentication() -> StringType: ...
    
    @staticmethod
    @property
    def AuthenticationInstant() -> StringType: ...
    
    @staticmethod
    @property
    def AuthenticationMethod() -> StringType: ...
    
    @staticmethod
    @property
    def AuthorizationDecision() -> StringType: ...
    
    @staticmethod
    @property
    def CookiePath() -> StringType: ...
    
    @staticmethod
    @property
    def Country() -> StringType: ...
    
    @staticmethod
    @property
    def DateOfBirth() -> StringType: ...
    
    @staticmethod
    @property
    def DenyOnlyPrimaryGroupSid() -> StringType: ...
    
    @staticmethod
    @property
    def DenyOnlyPrimarySid() -> StringType: ...
    
    @staticmethod
    @property
    def DenyOnlySid() -> StringType: ...
    
    @staticmethod
    @property
    def DenyOnlyWindowsDeviceGroup() -> StringType: ...
    
    @staticmethod
    @property
    def Dns() -> StringType: ...
    
    @staticmethod
    @property
    def Dsa() -> StringType: ...
    
    @staticmethod
    @property
    def Email() -> StringType: ...
    
    @staticmethod
    @property
    def Expiration() -> StringType: ...
    
    @staticmethod
    @property
    def Expired() -> StringType: ...
    
    @staticmethod
    @property
    def Gender() -> StringType: ...
    
    @staticmethod
    @property
    def GivenName() -> StringType: ...
    
    @staticmethod
    @property
    def GroupSid() -> StringType: ...
    
    @staticmethod
    @property
    def Hash() -> StringType: ...
    
    @staticmethod
    @property
    def HomePhone() -> StringType: ...
    
    @staticmethod
    @property
    def IsPersistent() -> StringType: ...
    
    @staticmethod
    @property
    def Locality() -> StringType: ...
    
    @staticmethod
    @property
    def MobilePhone() -> StringType: ...
    
    @staticmethod
    @property
    def Name() -> StringType: ...
    
    @staticmethod
    @property
    def NameIdentifier() -> StringType: ...
    
    @staticmethod
    @property
    def OtherPhone() -> StringType: ...
    
    @staticmethod
    @property
    def PostalCode() -> StringType: ...
    
    @staticmethod
    @property
    def PrimaryGroupSid() -> StringType: ...
    
    @staticmethod
    @property
    def PrimarySid() -> StringType: ...
    
    @staticmethod
    @property
    def Role() -> StringType: ...
    
    @staticmethod
    @property
    def Rsa() -> StringType: ...
    
    @staticmethod
    @property
    def SerialNumber() -> StringType: ...
    
    @staticmethod
    @property
    def Sid() -> StringType: ...
    
    @staticmethod
    @property
    def Spn() -> StringType: ...
    
    @staticmethod
    @property
    def StateOrProvince() -> StringType: ...
    
    @staticmethod
    @property
    def StreetAddress() -> StringType: ...
    
    @staticmethod
    @property
    def Surname() -> StringType: ...
    
    @staticmethod
    @property
    def System() -> StringType: ...
    
    @staticmethod
    @property
    def Thumbprint() -> StringType: ...
    
    @staticmethod
    @property
    def Upn() -> StringType: ...
    
    @staticmethod
    @property
    def Uri() -> StringType: ...
    
    @staticmethod
    @property
    def UserData() -> StringType: ...
    
    @staticmethod
    @property
    def Version() -> StringType: ...
    
    @staticmethod
    @property
    def Webpage() -> StringType: ...
    
    @staticmethod
    @property
    def WindowsAccountName() -> StringType: ...
    
    @staticmethod
    @property
    def WindowsDeviceClaim() -> StringType: ...
    
    @staticmethod
    @property
    def WindowsDeviceGroup() -> StringType: ...
    
    @staticmethod
    @property
    def WindowsFqbnVersion() -> StringType: ...
    
    @staticmethod
    @property
    def WindowsSubAuthority() -> StringType: ...
    
    @staticmethod
    @property
    def WindowsUserClaim() -> StringType: ...
    
    @staticmethod
    @property
    def X500DistinguishedName() -> StringType: ...
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ClaimTypes(ABC, ObjectType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Actor() -> StringType: ...
    
    @staticmethod
    @property
    def Anonymous() -> StringType: ...
    
    @staticmethod
    @property
    def Authentication() -> StringType: ...
    
    @staticmethod
    @property
    def AuthenticationInstant() -> StringType: ...
    
    @staticmethod
    @property
    def AuthenticationMethod() -> StringType: ...
    
    @staticmethod
    @property
    def AuthorizationDecision() -> StringType: ...
    
    @staticmethod
    @property
    def CookiePath() -> StringType: ...
    
    @staticmethod
    @property
    def Country() -> StringType: ...
    
    @staticmethod
    @property
    def DateOfBirth() -> StringType: ...
    
    @staticmethod
    @property
    def DenyOnlyPrimaryGroupSid() -> StringType: ...
    
    @staticmethod
    @property
    def DenyOnlyPrimarySid() -> StringType: ...
    
    @staticmethod
    @property
    def DenyOnlySid() -> StringType: ...
    
    @staticmethod
    @property
    def DenyOnlyWindowsDeviceGroup() -> StringType: ...
    
    @staticmethod
    @property
    def Dns() -> StringType: ...
    
    @staticmethod
    @property
    def Dsa() -> StringType: ...
    
    @staticmethod
    @property
    def Email() -> StringType: ...
    
    @staticmethod
    @property
    def Expiration() -> StringType: ...
    
    @staticmethod
    @property
    def Expired() -> StringType: ...
    
    @staticmethod
    @property
    def Gender() -> StringType: ...
    
    @staticmethod
    @property
    def GivenName() -> StringType: ...
    
    @staticmethod
    @property
    def GroupSid() -> StringType: ...
    
    @staticmethod
    @property
    def Hash() -> StringType: ...
    
    @staticmethod
    @property
    def HomePhone() -> StringType: ...
    
    @staticmethod
    @property
    def IsPersistent() -> StringType: ...
    
    @staticmethod
    @property
    def Locality() -> StringType: ...
    
    @staticmethod
    @property
    def MobilePhone() -> StringType: ...
    
    @staticmethod
    @property
    def Name() -> StringType: ...
    
    @staticmethod
    @property
    def NameIdentifier() -> StringType: ...
    
    @staticmethod
    @property
    def OtherPhone() -> StringType: ...
    
    @staticmethod
    @property
    def PostalCode() -> StringType: ...
    
    @staticmethod
    @property
    def PrimaryGroupSid() -> StringType: ...
    
    @staticmethod
    @property
    def PrimarySid() -> StringType: ...
    
    @staticmethod
    @property
    def Role() -> StringType: ...
    
    @staticmethod
    @property
    def Rsa() -> StringType: ...
    
    @staticmethod
    @property
    def SerialNumber() -> StringType: ...
    
    @staticmethod
    @property
    def Sid() -> StringType: ...
    
    @staticmethod
    @property
    def Spn() -> StringType: ...
    
    @staticmethod
    @property
    def StateOrProvince() -> StringType: ...
    
    @staticmethod
    @property
    def StreetAddress() -> StringType: ...
    
    @staticmethod
    @property
    def Surname() -> StringType: ...
    
    @staticmethod
    @property
    def System() -> StringType: ...
    
    @staticmethod
    @property
    def Thumbprint() -> StringType: ...
    
    @staticmethod
    @property
    def Upn() -> StringType: ...
    
    @staticmethod
    @property
    def Uri() -> StringType: ...
    
    @staticmethod
    @property
    def UserData() -> StringType: ...
    
    @staticmethod
    @property
    def Version() -> StringType: ...
    
    @staticmethod
    @property
    def Webpage() -> StringType: ...
    
    @staticmethod
    @property
    def WindowsAccountName() -> StringType: ...
    
    @staticmethod
    @property
    def WindowsDeviceClaim() -> StringType: ...
    
    @staticmethod
    @property
    def WindowsDeviceGroup() -> StringType: ...
    
    @staticmethod
    @property
    def WindowsFqbnVersion() -> StringType: ...
    
    @staticmethod
    @property
    def WindowsSubAuthority() -> StringType: ...
    
    @staticmethod
    @property
    def WindowsUserClaim() -> StringType: ...
    
    @staticmethod
    @property
    def X500DistinguishedName() -> StringType: ...
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ClaimValueTypes(ABC, ObjectType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Base64Binary() -> StringType: ...
    
    @staticmethod
    @property
    def Base64Octet() -> StringType: ...
    
    @staticmethod
    @property
    def Boolean() -> StringType: ...
    
    @staticmethod
    @property
    def Date() -> StringType: ...
    
    @staticmethod
    @property
    def DateTime() -> StringType: ...
    
    @staticmethod
    @property
    def DaytimeDuration() -> StringType: ...
    
    @staticmethod
    @property
    def DnsName() -> StringType: ...
    
    @staticmethod
    @property
    def Double() -> StringType: ...
    
    @staticmethod
    @property
    def DsaKeyValue() -> StringType: ...
    
    @staticmethod
    @property
    def Email() -> StringType: ...
    
    @staticmethod
    @property
    def Fqbn() -> StringType: ...
    
    @staticmethod
    @property
    def HexBinary() -> StringType: ...
    
    @staticmethod
    @property
    def Integer() -> StringType: ...
    
    @staticmethod
    @property
    def Integer32() -> StringType: ...
    
    @staticmethod
    @property
    def Integer64() -> StringType: ...
    
    @staticmethod
    @property
    def KeyInfo() -> StringType: ...
    
    @staticmethod
    @property
    def Rfc822Name() -> StringType: ...
    
    @staticmethod
    @property
    def Rsa() -> StringType: ...
    
    @staticmethod
    @property
    def RsaKeyValue() -> StringType: ...
    
    @staticmethod
    @property
    def Sid() -> StringType: ...
    
    @staticmethod
    @property
    def String() -> StringType: ...
    
    @staticmethod
    @property
    def Time() -> StringType: ...
    
    @staticmethod
    @property
    def UInteger32() -> StringType: ...
    
    @staticmethod
    @property
    def UInteger64() -> StringType: ...
    
    @staticmethod
    @property
    def UpnName() -> StringType: ...
    
    @staticmethod
    @property
    def X500Name() -> StringType: ...
    
    @staticmethod
    @property
    def YearMonthDuration() -> StringType: ...
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ClaimValueTypes(ABC, ObjectType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Base64Binary() -> StringType: ...
    
    @staticmethod
    @property
    def Base64Octet() -> StringType: ...
    
    @staticmethod
    @property
    def Boolean() -> StringType: ...
    
    @staticmethod
    @property
    def Date() -> StringType: ...
    
    @staticmethod
    @property
    def DateTime() -> StringType: ...
    
    @staticmethod
    @property
    def DaytimeDuration() -> StringType: ...
    
    @staticmethod
    @property
    def DnsName() -> StringType: ...
    
    @staticmethod
    @property
    def Double() -> StringType: ...
    
    @staticmethod
    @property
    def DsaKeyValue() -> StringType: ...
    
    @staticmethod
    @property
    def Email() -> StringType: ...
    
    @staticmethod
    @property
    def Fqbn() -> StringType: ...
    
    @staticmethod
    @property
    def HexBinary() -> StringType: ...
    
    @staticmethod
    @property
    def Integer() -> StringType: ...
    
    @staticmethod
    @property
    def Integer32() -> StringType: ...
    
    @staticmethod
    @property
    def Integer64() -> StringType: ...
    
    @staticmethod
    @property
    def KeyInfo() -> StringType: ...
    
    @staticmethod
    @property
    def Rfc822Name() -> StringType: ...
    
    @staticmethod
    @property
    def Rsa() -> StringType: ...
    
    @staticmethod
    @property
    def RsaKeyValue() -> StringType: ...
    
    @staticmethod
    @property
    def Sid() -> StringType: ...
    
    @staticmethod
    @property
    def String() -> StringType: ...
    
    @staticmethod
    @property
    def Time() -> StringType: ...
    
    @staticmethod
    @property
    def UInteger32() -> StringType: ...
    
    @staticmethod
    @property
    def UInteger64() -> StringType: ...
    
    @staticmethod
    @property
    def UpnName() -> StringType: ...
    
    @staticmethod
    @property
    def X500Name() -> StringType: ...
    
    @staticmethod
    @property
    def YearMonthDuration() -> StringType: ...
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ClaimValueTypes(ABC, ObjectType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Base64Binary() -> StringType: ...
    
    @staticmethod
    @property
    def Base64Octet() -> StringType: ...
    
    @staticmethod
    @property
    def Boolean() -> StringType: ...
    
    @staticmethod
    @property
    def Date() -> StringType: ...
    
    @staticmethod
    @property
    def DateTime() -> StringType: ...
    
    @staticmethod
    @property
    def DaytimeDuration() -> StringType: ...
    
    @staticmethod
    @property
    def DnsName() -> StringType: ...
    
    @staticmethod
    @property
    def Double() -> StringType: ...
    
    @staticmethod
    @property
    def DsaKeyValue() -> StringType: ...
    
    @staticmethod
    @property
    def Email() -> StringType: ...
    
    @staticmethod
    @property
    def Fqbn() -> StringType: ...
    
    @staticmethod
    @property
    def HexBinary() -> StringType: ...
    
    @staticmethod
    @property
    def Integer() -> StringType: ...
    
    @staticmethod
    @property
    def Integer32() -> StringType: ...
    
    @staticmethod
    @property
    def Integer64() -> StringType: ...
    
    @staticmethod
    @property
    def KeyInfo() -> StringType: ...
    
    @staticmethod
    @property
    def Rfc822Name() -> StringType: ...
    
    @staticmethod
    @property
    def Rsa() -> StringType: ...
    
    @staticmethod
    @property
    def RsaKeyValue() -> StringType: ...
    
    @staticmethod
    @property
    def Sid() -> StringType: ...
    
    @staticmethod
    @property
    def String() -> StringType: ...
    
    @staticmethod
    @property
    def Time() -> StringType: ...
    
    @staticmethod
    @property
    def UInteger32() -> StringType: ...
    
    @staticmethod
    @property
    def UInteger64() -> StringType: ...
    
    @staticmethod
    @property
    def UpnName() -> StringType: ...
    
    @staticmethod
    @property
    def X500Name() -> StringType: ...
    
    @staticmethod
    @property
    def YearMonthDuration() -> StringType: ...
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ClaimsIdentity(ObjectType, IIdentity):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def DefaultIssuer() -> StringType: ...
    
    @staticmethod
    @property
    def DefaultNameClaimType() -> StringType: ...
    
    @staticmethod
    @property
    def DefaultRoleClaimType() -> StringType: ...
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, identity: IIdentity): ...
    
    @overload
    def __init__(self, claims: IEnumerable[Claim]): ...
    
    @overload
    def __init__(self, authenticationType: StringType): ...
    
    @overload
    def __init__(self, claims: IEnumerable[Claim], authenticationType: StringType): ...
    
    @overload
    def __init__(self, identity: IIdentity, claims: IEnumerable[Claim]): ...
    
    @overload
    def __init__(self, authenticationType: StringType, nameType: StringType, roleType: StringType): ...
    
    @overload
    def __init__(self, claims: IEnumerable[Claim], authenticationType: StringType, nameType: StringType, roleType: StringType): ...
    
    @overload
    def __init__(self, identity: IIdentity, claims: IEnumerable[Claim], authenticationType: StringType, nameType: StringType, roleType: StringType): ...
    
    @overload
    def __init__(self, reader: BinaryReader): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Actor(self) -> ClaimsIdentity: ...
    
    @Actor.setter
    def Actor(self, value: ClaimsIdentity) -> None: ...
    
    @property
    def AuthenticationType(self) -> StringType: ...
    
    @property
    def BootstrapContext(self) -> ObjectType: ...
    
    @BootstrapContext.setter
    def BootstrapContext(self, value: ObjectType) -> None: ...
    
    @property
    def Claims(self) -> IEnumerable[Claim]: ...
    
    @property
    def IsAuthenticated(self) -> BooleanType: ...
    
    @property
    def Label(self) -> StringType: ...
    
    @Label.setter
    def Label(self, value: StringType) -> None: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def NameClaimType(self) -> StringType: ...
    
    @property
    def RoleClaimType(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def AddClaim(self, claim: Claim) -> VoidType: ...
    
    def AddClaims(self, claims: IEnumerable[Claim]) -> VoidType: ...
    
    def Clone(self) -> ClaimsIdentity: ...
    
    @overload
    def FindAll(self, match: Predicate[Claim]) -> IEnumerable[Claim]: ...
    
    @overload
    def FindAll(self, type: StringType) -> IEnumerable[Claim]: ...
    
    @overload
    def FindFirst(self, match: Predicate[Claim]) -> Claim: ...
    
    @overload
    def FindFirst(self, type: StringType) -> Claim: ...
    
    @overload
    def HasClaim(self, match: Predicate[Claim]) -> BooleanType: ...
    
    @overload
    def HasClaim(self, type: StringType, value: StringType) -> BooleanType: ...
    
    def RemoveClaim(self, claim: Claim) -> VoidType: ...
    
    def TryRemoveClaim(self, claim: Claim) -> BooleanType: ...
    
    def WriteTo(self, writer: BinaryWriter) -> VoidType: ...
    
    def get_Actor(self) -> ClaimsIdentity: ...
    
    def get_AuthenticationType(self) -> StringType: ...
    
    def get_BootstrapContext(self) -> ObjectType: ...
    
    def get_Claims(self) -> IEnumerable[Claim]: ...
    
    def get_IsAuthenticated(self) -> BooleanType: ...
    
    def get_Label(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_NameClaimType(self) -> StringType: ...
    
    def get_RoleClaimType(self) -> StringType: ...
    
    def set_Actor(self, value: ClaimsIdentity) -> VoidType: ...
    
    def set_BootstrapContext(self, value: ObjectType) -> VoidType: ...
    
    def set_Label(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ClaimsIdentity(ObjectType, IIdentity):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def DefaultIssuer() -> StringType: ...
    
    @staticmethod
    @property
    def DefaultNameClaimType() -> StringType: ...
    
    @staticmethod
    @property
    def DefaultRoleClaimType() -> StringType: ...
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, identity: IIdentity): ...
    
    @overload
    def __init__(self, claims: IEnumerable[Claim]): ...
    
    @overload
    def __init__(self, authenticationType: StringType): ...
    
    @overload
    def __init__(self, claims: IEnumerable[Claim], authenticationType: StringType): ...
    
    @overload
    def __init__(self, identity: IIdentity, claims: IEnumerable[Claim]): ...
    
    @overload
    def __init__(self, authenticationType: StringType, nameType: StringType, roleType: StringType): ...
    
    @overload
    def __init__(self, claims: IEnumerable[Claim], authenticationType: StringType, nameType: StringType, roleType: StringType): ...
    
    @overload
    def __init__(self, identity: IIdentity, claims: IEnumerable[Claim], authenticationType: StringType, nameType: StringType, roleType: StringType): ...
    
    @overload
    def __init__(self, reader: BinaryReader): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Actor(self) -> ClaimsIdentity: ...
    
    @Actor.setter
    def Actor(self, value: ClaimsIdentity) -> None: ...
    
    @property
    def AuthenticationType(self) -> StringType: ...
    
    @property
    def BootstrapContext(self) -> ObjectType: ...
    
    @BootstrapContext.setter
    def BootstrapContext(self, value: ObjectType) -> None: ...
    
    @property
    def Claims(self) -> IEnumerable[Claim]: ...
    
    @property
    def IsAuthenticated(self) -> BooleanType: ...
    
    @property
    def Label(self) -> StringType: ...
    
    @Label.setter
    def Label(self, value: StringType) -> None: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def NameClaimType(self) -> StringType: ...
    
    @property
    def RoleClaimType(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def AddClaim(self, claim: Claim) -> VoidType: ...
    
    def AddClaims(self, claims: IEnumerable[Claim]) -> VoidType: ...
    
    def Clone(self) -> ClaimsIdentity: ...
    
    @overload
    def FindAll(self, match: Predicate[Claim]) -> IEnumerable[Claim]: ...
    
    @overload
    def FindAll(self, type: StringType) -> IEnumerable[Claim]: ...
    
    @overload
    def FindFirst(self, match: Predicate[Claim]) -> Claim: ...
    
    @overload
    def FindFirst(self, type: StringType) -> Claim: ...
    
    @overload
    def HasClaim(self, match: Predicate[Claim]) -> BooleanType: ...
    
    @overload
    def HasClaim(self, type: StringType, value: StringType) -> BooleanType: ...
    
    def RemoveClaim(self, claim: Claim) -> VoidType: ...
    
    def TryRemoveClaim(self, claim: Claim) -> BooleanType: ...
    
    def WriteTo(self, writer: BinaryWriter) -> VoidType: ...
    
    def get_Actor(self) -> ClaimsIdentity: ...
    
    def get_AuthenticationType(self) -> StringType: ...
    
    def get_BootstrapContext(self) -> ObjectType: ...
    
    def get_Claims(self) -> IEnumerable[Claim]: ...
    
    def get_IsAuthenticated(self) -> BooleanType: ...
    
    def get_Label(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_NameClaimType(self) -> StringType: ...
    
    def get_RoleClaimType(self) -> StringType: ...
    
    def set_Actor(self, value: ClaimsIdentity) -> VoidType: ...
    
    def set_BootstrapContext(self, value: ObjectType) -> VoidType: ...
    
    def set_Label(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ClaimsIdentity(ObjectType, IIdentity):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def DefaultIssuer() -> StringType: ...
    
    @staticmethod
    @property
    def DefaultNameClaimType() -> StringType: ...
    
    @staticmethod
    @property
    def DefaultRoleClaimType() -> StringType: ...
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, identity: IIdentity): ...
    
    @overload
    def __init__(self, claims: IEnumerable[Claim]): ...
    
    @overload
    def __init__(self, authenticationType: StringType): ...
    
    @overload
    def __init__(self, claims: IEnumerable[Claim], authenticationType: StringType): ...
    
    @overload
    def __init__(self, identity: IIdentity, claims: IEnumerable[Claim]): ...
    
    @overload
    def __init__(self, authenticationType: StringType, nameType: StringType, roleType: StringType): ...
    
    @overload
    def __init__(self, claims: IEnumerable[Claim], authenticationType: StringType, nameType: StringType, roleType: StringType): ...
    
    @overload
    def __init__(self, identity: IIdentity, claims: IEnumerable[Claim], authenticationType: StringType, nameType: StringType, roleType: StringType): ...
    
    @overload
    def __init__(self, reader: BinaryReader): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Actor(self) -> ClaimsIdentity: ...
    
    @Actor.setter
    def Actor(self, value: ClaimsIdentity) -> None: ...
    
    @property
    def AuthenticationType(self) -> StringType: ...
    
    @property
    def BootstrapContext(self) -> ObjectType: ...
    
    @BootstrapContext.setter
    def BootstrapContext(self, value: ObjectType) -> None: ...
    
    @property
    def Claims(self) -> IEnumerable[Claim]: ...
    
    @property
    def IsAuthenticated(self) -> BooleanType: ...
    
    @property
    def Label(self) -> StringType: ...
    
    @Label.setter
    def Label(self, value: StringType) -> None: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def NameClaimType(self) -> StringType: ...
    
    @property
    def RoleClaimType(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def AddClaim(self, claim: Claim) -> VoidType: ...
    
    def AddClaims(self, claims: IEnumerable[Claim]) -> VoidType: ...
    
    def Clone(self) -> ClaimsIdentity: ...
    
    @overload
    def FindAll(self, match: Predicate[Claim]) -> IEnumerable[Claim]: ...
    
    @overload
    def FindAll(self, type: StringType) -> IEnumerable[Claim]: ...
    
    @overload
    def FindFirst(self, match: Predicate[Claim]) -> Claim: ...
    
    @overload
    def FindFirst(self, type: StringType) -> Claim: ...
    
    @overload
    def HasClaim(self, match: Predicate[Claim]) -> BooleanType: ...
    
    @overload
    def HasClaim(self, type: StringType, value: StringType) -> BooleanType: ...
    
    def RemoveClaim(self, claim: Claim) -> VoidType: ...
    
    def TryRemoveClaim(self, claim: Claim) -> BooleanType: ...
    
    def WriteTo(self, writer: BinaryWriter) -> VoidType: ...
    
    def get_Actor(self) -> ClaimsIdentity: ...
    
    def get_AuthenticationType(self) -> StringType: ...
    
    def get_BootstrapContext(self) -> ObjectType: ...
    
    def get_Claims(self) -> IEnumerable[Claim]: ...
    
    def get_IsAuthenticated(self) -> BooleanType: ...
    
    def get_Label(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_NameClaimType(self) -> StringType: ...
    
    def get_RoleClaimType(self) -> StringType: ...
    
    def set_Actor(self, value: ClaimsIdentity) -> VoidType: ...
    
    def set_BootstrapContext(self, value: ObjectType) -> VoidType: ...
    
    def set_Label(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ClaimsPrincipal(ObjectType, IPrincipal):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, identities: IEnumerable[ClaimsIdentity]): ...
    
    @overload
    def __init__(self, identity: IIdentity): ...
    
    @overload
    def __init__(self, principal: IPrincipal): ...
    
    @overload
    def __init__(self, reader: BinaryReader): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Claims(self) -> IEnumerable[Claim]: ...
    
    @staticmethod
    @property
    def ClaimsPrincipalSelector() -> Func[ClaimsPrincipal]: ...
    
    @staticmethod
    @ClaimsPrincipalSelector.setter
    def ClaimsPrincipalSelector(value: Func[ClaimsPrincipal]) -> None: ...
    
    @staticmethod
    @property
    def Current() -> ClaimsPrincipal: ...
    
    @property
    def Identities(self) -> IEnumerable[ClaimsIdentity]: ...
    
    @property
    def Identity(self) -> IIdentity: ...
    
    @staticmethod
    @property
    def PrimaryIdentitySelector() -> Func[IEnumerable[ClaimsIdentity], ClaimsIdentity]: ...
    
    @staticmethod
    @PrimaryIdentitySelector.setter
    def PrimaryIdentitySelector(value: Func[IEnumerable[ClaimsIdentity], ClaimsIdentity]) -> None: ...
    
    # ---------- Methods ---------- #
    
    def AddIdentities(self, identities: IEnumerable[ClaimsIdentity]) -> VoidType: ...
    
    def AddIdentity(self, identity: ClaimsIdentity) -> VoidType: ...
    
    def Clone(self) -> ClaimsPrincipal: ...
    
    @overload
    def FindAll(self, match: Predicate[Claim]) -> IEnumerable[Claim]: ...
    
    @overload
    def FindAll(self, type: StringType) -> IEnumerable[Claim]: ...
    
    @overload
    def FindFirst(self, match: Predicate[Claim]) -> Claim: ...
    
    @overload
    def FindFirst(self, type: StringType) -> Claim: ...
    
    @overload
    def HasClaim(self, match: Predicate[Claim]) -> BooleanType: ...
    
    @overload
    def HasClaim(self, type: StringType, value: StringType) -> BooleanType: ...
    
    def IsInRole(self, role: StringType) -> BooleanType: ...
    
    def WriteTo(self, writer: BinaryWriter) -> VoidType: ...
    
    def get_Claims(self) -> IEnumerable[Claim]: ...
    
    @staticmethod
    def get_ClaimsPrincipalSelector() -> Func[ClaimsPrincipal]: ...
    
    @staticmethod
    def get_Current() -> ClaimsPrincipal: ...
    
    def get_Identities(self) -> IEnumerable[ClaimsIdentity]: ...
    
    def get_Identity(self) -> IIdentity: ...
    
    @staticmethod
    def get_PrimaryIdentitySelector() -> Func[IEnumerable[ClaimsIdentity], ClaimsIdentity]: ...
    
    @staticmethod
    def set_ClaimsPrincipalSelector(value: Func[ClaimsPrincipal]) -> VoidType: ...
    
    @staticmethod
    def set_PrimaryIdentitySelector(value: Func[IEnumerable[ClaimsIdentity], ClaimsIdentity]) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ClaimsPrincipal(ObjectType, IPrincipal):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, identities: IEnumerable[ClaimsIdentity]): ...
    
    @overload
    def __init__(self, identity: IIdentity): ...
    
    @overload
    def __init__(self, principal: IPrincipal): ...
    
    @overload
    def __init__(self, reader: BinaryReader): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Claims(self) -> IEnumerable[Claim]: ...
    
    @staticmethod
    @property
    def ClaimsPrincipalSelector() -> Func[ClaimsPrincipal]: ...
    
    @staticmethod
    @ClaimsPrincipalSelector.setter
    def ClaimsPrincipalSelector(value: Func[ClaimsPrincipal]) -> None: ...
    
    @staticmethod
    @property
    def Current() -> ClaimsPrincipal: ...
    
    @property
    def Identities(self) -> IEnumerable[ClaimsIdentity]: ...
    
    @property
    def Identity(self) -> IIdentity: ...
    
    @staticmethod
    @property
    def PrimaryIdentitySelector() -> Func[IEnumerable[ClaimsIdentity], ClaimsIdentity]: ...
    
    @staticmethod
    @PrimaryIdentitySelector.setter
    def PrimaryIdentitySelector(value: Func[IEnumerable[ClaimsIdentity], ClaimsIdentity]) -> None: ...
    
    # ---------- Methods ---------- #
    
    def AddIdentities(self, identities: IEnumerable[ClaimsIdentity]) -> VoidType: ...
    
    def AddIdentity(self, identity: ClaimsIdentity) -> VoidType: ...
    
    def Clone(self) -> ClaimsPrincipal: ...
    
    @overload
    def FindAll(self, match: Predicate[Claim]) -> IEnumerable[Claim]: ...
    
    @overload
    def FindAll(self, type: StringType) -> IEnumerable[Claim]: ...
    
    @overload
    def FindFirst(self, match: Predicate[Claim]) -> Claim: ...
    
    @overload
    def FindFirst(self, type: StringType) -> Claim: ...
    
    @overload
    def HasClaim(self, match: Predicate[Claim]) -> BooleanType: ...
    
    @overload
    def HasClaim(self, type: StringType, value: StringType) -> BooleanType: ...
    
    def IsInRole(self, role: StringType) -> BooleanType: ...
    
    def WriteTo(self, writer: BinaryWriter) -> VoidType: ...
    
    def get_Claims(self) -> IEnumerable[Claim]: ...
    
    @staticmethod
    def get_ClaimsPrincipalSelector() -> Func[ClaimsPrincipal]: ...
    
    @staticmethod
    def get_Current() -> ClaimsPrincipal: ...
    
    def get_Identities(self) -> IEnumerable[ClaimsIdentity]: ...
    
    def get_Identity(self) -> IIdentity: ...
    
    @staticmethod
    def get_PrimaryIdentitySelector() -> Func[IEnumerable[ClaimsIdentity], ClaimsIdentity]: ...
    
    @staticmethod
    def set_ClaimsPrincipalSelector(value: Func[ClaimsPrincipal]) -> VoidType: ...
    
    @staticmethod
    def set_PrimaryIdentitySelector(value: Func[IEnumerable[ClaimsIdentity], ClaimsIdentity]) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ClaimsPrincipal(ObjectType, IPrincipal):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, identities: IEnumerable[ClaimsIdentity]): ...
    
    @overload
    def __init__(self, identity: IIdentity): ...
    
    @overload
    def __init__(self, principal: IPrincipal): ...
    
    @overload
    def __init__(self, reader: BinaryReader): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Claims(self) -> IEnumerable[Claim]: ...
    
    @staticmethod
    @property
    def ClaimsPrincipalSelector() -> Func[ClaimsPrincipal]: ...
    
    @staticmethod
    @ClaimsPrincipalSelector.setter
    def ClaimsPrincipalSelector(value: Func[ClaimsPrincipal]) -> None: ...
    
    @staticmethod
    @property
    def Current() -> ClaimsPrincipal: ...
    
    @property
    def Identities(self) -> IEnumerable[ClaimsIdentity]: ...
    
    @property
    def Identity(self) -> IIdentity: ...
    
    @staticmethod
    @property
    def PrimaryIdentitySelector() -> Func[IEnumerable[ClaimsIdentity], ClaimsIdentity]: ...
    
    @staticmethod
    @PrimaryIdentitySelector.setter
    def PrimaryIdentitySelector(value: Func[IEnumerable[ClaimsIdentity], ClaimsIdentity]) -> None: ...
    
    # ---------- Methods ---------- #
    
    def AddIdentities(self, identities: IEnumerable[ClaimsIdentity]) -> VoidType: ...
    
    def AddIdentity(self, identity: ClaimsIdentity) -> VoidType: ...
    
    def Clone(self) -> ClaimsPrincipal: ...
    
    @overload
    def FindAll(self, match: Predicate[Claim]) -> IEnumerable[Claim]: ...
    
    @overload
    def FindAll(self, type: StringType) -> IEnumerable[Claim]: ...
    
    @overload
    def FindFirst(self, match: Predicate[Claim]) -> Claim: ...
    
    @overload
    def FindFirst(self, type: StringType) -> Claim: ...
    
    @overload
    def HasClaim(self, match: Predicate[Claim]) -> BooleanType: ...
    
    @overload
    def HasClaim(self, type: StringType, value: StringType) -> BooleanType: ...
    
    def IsInRole(self, role: StringType) -> BooleanType: ...
    
    def WriteTo(self, writer: BinaryWriter) -> VoidType: ...
    
    def get_Claims(self) -> IEnumerable[Claim]: ...
    
    @staticmethod
    def get_ClaimsPrincipalSelector() -> Func[ClaimsPrincipal]: ...
    
    @staticmethod
    def get_Current() -> ClaimsPrincipal: ...
    
    def get_Identities(self) -> IEnumerable[ClaimsIdentity]: ...
    
    def get_Identity(self) -> IIdentity: ...
    
    @staticmethod
    def get_PrimaryIdentitySelector() -> Func[IEnumerable[ClaimsIdentity], ClaimsIdentity]: ...
    
    @staticmethod
    def set_ClaimsPrincipalSelector(value: Func[ClaimsPrincipal]) -> VoidType: ...
    
    @staticmethod
    def set_PrimaryIdentitySelector(value: Func[IEnumerable[ClaimsIdentity], ClaimsIdentity]) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DynamicRoleClaimProvider(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def AddDynamicRoleClaims(claimsIdentity: ClaimsIdentity, claims: IEnumerable[Claim]) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RoleClaimProvider(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, issuer: StringType, roles: ArrayType[StringType], subject: ClaimsIdentity): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Claims(self) -> IEnumerable[Claim]: ...
    
    # ---------- Methods ---------- #
    
    def get_Claims(self) -> IEnumerable[Claim]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RoleClaimProvider(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, issuer: StringType, roles: ArrayType[StringType], subject: ClaimsIdentity): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Claims(self) -> IEnumerable[Claim]: ...
    
    # ---------- Methods ---------- #
    
    def get_Claims(self) -> IEnumerable[Claim]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RoleClaimProvider(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, issuer: StringType, roles: ArrayType[StringType], subject: ClaimsIdentity): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Claims(self) -> IEnumerable[Claim]: ...
    
    # ---------- Methods ---------- #
    
    def get_Claims(self) -> IEnumerable[Claim]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# No Structs

# No Interfaces

# No Enums

# No Delegates

__all__ = [
    Claim,
    ClaimTypes,
    ClaimValueTypes,
    ClaimsIdentity,
    ClaimsPrincipal,
    DynamicRoleClaimProvider,
    RoleClaimProvider,
]
