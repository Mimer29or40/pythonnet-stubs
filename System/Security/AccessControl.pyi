__all__ = [
    'AccessRule',
    'AccessRule',
    'AceEnumerator',
    'AuditRule',
    'AuditRule',
    'AuthorizationRule',
    'AuthorizationRuleCollection',
    'CommonAce',
    'CommonAcl',
    'CommonObjectSecurity',
    'CommonSecurityDescriptor',
    'CompoundAce',
    'CustomAce',
    'DirectoryObjectSecurity',
    'DirectorySecurity',
    'DiscretionaryAcl',
    'FileSecurity',
    'FileSystemAccessRule',
    'FileSystemAuditRule',
    'FileSystemSecurity',
    'GenericAce',
    'GenericAcl',
    'GenericSecurityDescriptor',
    'KnownAce',
    'NativeObjectSecurity',
    'ObjectAccessRule',
    'ObjectAce',
    'ObjectAuditRule',
    'ObjectSecurity',
    'ObjectSecurity',
    'PrivilegeNotHeldException',
    'QualifiedAce',
    'RawAcl',
    'RawSecurityDescriptor',
    'RegistryAccessRule',
    'RegistryAuditRule',
    'RegistrySecurity',
    'SystemAcl',
    'AccessControlActions',
    'AccessControlModification',
    'AccessControlSections',
    'AccessControlType',
    'AceFlags',
    'AceQualifier',
    'AceType',
    'AuditFlags',
    'CompoundAceType',
    'ControlFlags',
    'FileSystemRights',
    'InheritanceFlags',
    'ObjectAceFlags',
    'PropagationFlags',
    'RegistryRights',
    'ResourceType',
    'SecurityInfos',
]

from typing import TypeVar, Generic

T = TypeVar('T')


# TODO

# ---------- CLASSES ---------- #

class AccessRule:
    """Represents a combination of a user's identity, an access mask, and an access control type (allow or deny). An AccessRule object also contains information about how the rule is inherited by child objects and how that inheritance is propagated."""


class AccessRule(Generic[T]):
    """Represents a combination of a user's identity, an access mask, and an access control type (allow or deny). An AccessRule`1 object also contains information about the how the rule is inherited by child objects and how that inheritance is propagated."""


class AceEnumerator:
    """Provides the ability to iterate through the access control entries (ACEs) in an access control list (ACL)."""


class AuditRule:
    """Represents a combination of a user's identity and an access mask. An AuditRule object also contains information about how the rule is inherited by child objects, how that inheritance is propagated, and for what conditions it is audited."""


class AuditRule(Generic[T]):
    """Represents a combination of a user's identity and an access mask."""


class AuthorizationRule:
    """Determines access to securable objects. The derived classes AccessRule and AuditRule offer specializations for access and audit functionality."""


class AuthorizationRuleCollection:
    """Represents a collection of AuthorizationRule objects."""


class CommonAce:
    """Represents an access control entry (ACE)."""


class CommonAcl:
    """Represents an access control list (ACL) and is the base class for the DiscretionaryAcl and SystemAcl classes."""


class CommonObjectSecurity:
    """Controls access to objects without direct manipulation of access control lists (ACLs). This class is the abstract base class for the NativeObjectSecurity class."""


class CommonSecurityDescriptor:
    """Represents a security descriptor. A security descriptor includes an owner, a primary group, a Discretionary Access Control List (DACL), and a System Access Control List (SACL)."""


class CompoundAce:
    """Represents a compound Access Control Entry (ACE)."""


class CustomAce:
    """Represents an Access Control Entry (ACE) that is not defined by one of the members of the AceType enumeration."""


class DirectoryObjectSecurity:
    """Provides the ability to control access to directory objects without direct manipulation of Access Control Lists (ACLs)."""


class DirectorySecurity:
    """Represents the access control and audit security for a directory. This class cannot be inherited."""


class DiscretionaryAcl:
    """Represents a Discretionary Access Control List (DACL)."""


class FileSecurity:
    """Represents the access control and audit security for a file. This class cannot be inherited."""


class FileSystemAccessRule:
    """Represents an abstraction of an access control entry (ACE) that defines an access rule for a file or directory. This class cannot be inherited."""


class FileSystemAuditRule:
    """Represents an abstraction of an access control entry (ACE) that defines an audit rule for a file or directory. This class cannot be inherited."""


class FileSystemSecurity:
    """Represents the access control and audit security for a file or directory."""


class GenericAce:
    """Represents an Access Control Entry (ACE), and is the base class for all other ACE classes."""


class GenericAcl:
    """Represents an access control list (ACL) and is the base class for the CommonAcl, DiscretionaryAcl, RawAcl, and SystemAcl classes."""


class GenericSecurityDescriptor:
    """Represents a security descriptor. A security descriptor includes an owner, a primary group, a Discretionary Access Control List (DACL), and a System Access Control List (SACL)."""


class KnownAce:
    """Encapsulates all Access Control Entry (ACE) types currently defined by Microsoft Corporation. All KnownAce objects contain a 32-bit access mask and a SecurityIdentifier object."""


class NativeObjectSecurity:
    """Provides the ability to control access to native objects without direct manipulation of Access Control Lists (ACLs). Native object types are defined by the ResourceType enumeration."""
    
    # ---------- DELEGATES ---------- #
    
    class ExceptionFromErrorCode:
        """Provides a way for integrators to map numeric error codes to specific exceptions that they create."""


class ObjectAccessRule:
    """Represents a combination of a user's identity, an access mask, and an access control type (allow or deny). An ObjectAccessRule object also contains information about the type of object to which the rule applies, the type of child object that can inherit the rule, how the rule is inherited by child objects, and how that inheritance is propagated."""


class ObjectAce:
    """Controls access to Directory Services objects. This class represents an Access Control Entry (ACE) associated with a directory object."""


class ObjectAuditRule:
    """Represents a combination of a user's identity, an access mask, and audit conditions. An ObjectAuditRule object also contains information about the type of object to which the rule applies, the type of child object that can inherit the rule, how the rule is inherited by child objects, and how that inheritance is propagated."""


class ObjectSecurity:
    """Provides the ability to control access to objects without direct manipulation of Access Control Lists (ACLs). This class is the abstract base class for the CommonObjectSecurity and DirectoryObjectSecurity classes."""


class ObjectSecurity(Generic[T]):
    """Provides the ability to control access to objects without direct manipulation of Access Control Lists (ACLs); also grants the ability to type-cast access rights."""


class PrivilegeNotHeldException:
    """The exception that is thrown when a method in the System.Security.AccessControl namespace attempts to enable a privilege that it does not have."""


class QualifiedAce:
    """Represents an Access Control Entry (ACE) that contains a qualifier. The qualifier, represented by an AceQualifier object, specifies whether the ACE allows access, denies access, causes system audits, or causes system alarms. The QualifiedAce class is the abstract base class for the CommonAce and ObjectAce classes."""


class RawAcl:
    """Represents an Access Control List (ACL)."""


class RawSecurityDescriptor:
    """Represents a security descriptor. A security descriptor includes an owner, a primary group, a Discretionary Access Control List (DACL), and a System Access Control List (SACL)."""


class RegistryAccessRule:
    """Represents a set of access rights allowed or denied for a user or group. This class cannot be inherited."""


class RegistryAuditRule:
    """Represents a set of access rights to be audited for a user or group. This class cannot be inherited."""


class RegistrySecurity:
    """Represents the Windows access control security for a registry key. This class cannot be inherited."""


class SystemAcl:
    """Represents a System Access Control List (SACL)."""


# ---------- ENUMS ---------- #

class AccessControlActions:
    """Specifies the actions that are permitted for securable objects."""


class AccessControlModification:
    """Specifies the type of access control modification to perform. This enumeration is used by methods of the ObjectSecurity class and its descendants."""


class AccessControlSections:
    """Specifies which sections of a security descriptor to save or load."""


class AccessControlType:
    """Specifies whether an AccessRule object is used to allow or deny access. These values are not flags, and they cannot be combined."""


class AceFlags:
    """Specifies the inheritance and auditing behavior of an access control entry (ACE)."""


class AceQualifier:
    """Specifies the function of an access control entry (ACE)."""


class AceType:
    """Defines the available access control entry (ACE) types."""


class AuditFlags:
    """Specifies the conditions for auditing attempts to access a securable object."""


class CompoundAceType:
    """Specifies the type of a CompoundAce object."""


class ControlFlags:
    """These flags affect the security descriptor behavior."""


class FileSystemRights:
    """Defines the access rights to use when creating access and audit rules."""


class InheritanceFlags:
    """Inheritance flags specify the semantics of inheritance for access control entries (ACEs)."""


class ObjectAceFlags:
    """Specifies the presence of object types for Access Control Entries (ACEs)."""


class PropagationFlags:
    """Specifies how Access Control Entries (ACEs) are propagated to child objects. These flags are significant only if inheritance flags are present."""


class RegistryRights:
    """Specifies the access control rights that can be applied to registry objects."""


class ResourceType:
    """Specifies the defined native object types."""


class SecurityInfos:
    """Specifies the section of a security descriptor to be queried or set."""
