__all__ = [
    'AllowPartiallyTrustedCallersAttribute',
    'PermissionSet',
    'SecureString',
    'SecureStringMarshal',
    'SecurityCriticalAttribute',
    'SecurityElement',
    'SecurityException',
    'SecurityRulesAttribute',
    'SecuritySafeCriticalAttribute',
    'SecurityTransparentAttribute',
    'SecurityTreatAsSafeAttribute',
    'SuppressUnmanagedCodeSecurityAttribute',
    'UnverifiableCodeAttribute',
    'VerificationException',
    'IPermission',
    'ISecurityEncodable',
    'IStackWalk',
    'PartialTrustVisibilityLevel',
    'SecurityCriticalScope',
    'SecurityRuleSet',
]


# TODO

# ---------- CLASSES ---------- #

class AllowPartiallyTrustedCallersAttribute:
    """Allows an assembly to be called by partially trusted code. Without this declaration, only fully trusted callers are able to use the assembly. This class cannot be inherited."""


class PermissionSet:
    """Represents a collection that can contain many different types of permissions."""


class SecureString:
    """Represents text that should be kept confidential, such as by deleting it from computer memory when no longer needed. This class cannot be inherited."""


class SecureStringMarshal:
    """Provides a collection of methods for allocating unmanaged memory and copying unmanaged memory blocks."""


class SecurityCriticalAttribute:
    """Specifies that code or an assembly performs security-critical operations."""


class SecurityElement:
    """Represents the XML object model for encoding security objects. This class cannot be inherited."""


class SecurityException:
    """The exception that is thrown when a security error is detected."""


class SecurityRulesAttribute:
    """Indicates the set of security rules the common language runtime should enforce for an assembly."""


class SecuritySafeCriticalAttribute:
    """Identifies types or members as security-critical and safely accessible by transparent code."""


class SecurityTransparentAttribute:
    """Specifies that an assembly cannot cause an elevation of privilege."""


class SecurityTreatAsSafeAttribute:
    """Identifies which of the nonpublic SecurityCriticalAttribute members are accessible by transparent code within the assembly."""


class SuppressUnmanagedCodeSecurityAttribute:
    """Allows managed code to call into unmanaged code without a stack walk. This class cannot be inherited."""


class UnverifiableCodeAttribute:
    """Marks modules containing unverifiable code. This class cannot be inherited."""


class VerificationException:
    """The exception that is thrown when the security policy requires code to be type safe and the verification process is unable to verify that the code is type safe."""


# ---------- INTERFACES ---------- #

class IPermission:
    """Defines methods implemented by permission types."""


class ISecurityEncodable:
    """Defines the methods that convert permission object state to and from XML element representation."""


class IStackWalk:
    """Manages the stack walk that determines whether all callers in the call stack have the required permissions to access a protected resource."""


# ---------- ENUMS ---------- #

class PartialTrustVisibilityLevel:
    """Specifies the default partial-trust visibility for code that is marked with the AllowPartiallyTrustedCallersAttribute (APTCA) attribute."""


class SecurityCriticalScope:
    """Specifies the scope of a SecurityCriticalAttribute."""


class SecurityRuleSet:
    """Identifies the set of security rules the common language runtime should enforce for an assembly."""
