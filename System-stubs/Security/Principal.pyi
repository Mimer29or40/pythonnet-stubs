__all__ = [
    'GenericIdentity',
    'GenericPrincipal',
    'IdentityNotMappedException',
    'IdentityReference',
    'IdentityReferenceCollection',
    'NTAccount',
    'SecurityIdentifier',
    'WindowsIdentity',
    'WindowsPrincipal',
    'IIdentity',
    'IPrincipal',
    'PrincipalPolicy',
    'TokenAccessLevels',
    'TokenImpersonationLevel',
    'WellKnownSidType',
    'WindowsAccountType',
    'WindowsBuiltInRole',
]


# TODO

# ---------- CLASSES ---------- #

class GenericIdentity:
    """Represents a generic user."""


class GenericPrincipal:
    """Represents a generic principal."""


class IdentityNotMappedException:
    """Represents an exception for a principal whose identity could not be mapped to a known identity."""


class IdentityReference:
    """Represents an identity and is the base class for the NTAccount and SecurityIdentifier classes. This class does not provide a public constructor, and therefore cannot be inherited."""


class IdentityReferenceCollection:
    """Represents a collection of IdentityReference objects and provides a means of converting sets of IdentityReference-derived objects to IdentityReference-derived types."""


class NTAccount:
    """Represents a user or group account."""


class SecurityIdentifier:
    """Represents a security identifier (SID) and provides marshaling and comparison operations for SIDs."""


class WindowsIdentity:
    """Represents a Windows user."""


class WindowsPrincipal:
    """Enables code to check the Windows group membership of a Windows user."""


# ---------- INTERFACES ---------- #

class IIdentity:
    """Defines the basic functionality of an identity object."""


class IPrincipal:
    """Defines the basic functionality of a principal object."""


# ---------- ENUMS ---------- #

class PrincipalPolicy:
    """Specifies how principal and identity objects should be created for an application domain. The default is UnauthenticatedPrincipal."""


class TokenAccessLevels:
    """Defines the privileges of the user account associated with the access token."""


class TokenImpersonationLevel:
    """Defines security impersonation levels. Security impersonation levels govern the degree to which a server process can act on behalf of a client process."""


class WellKnownSidType:
    """Defines a set of commonly used security identifiers (SIDs)."""


class WindowsAccountType:
    """Specifies the type of Windows account used."""


class WindowsBuiltInRole:
    """Specifies common roles to be used with IsInRole(String)."""
