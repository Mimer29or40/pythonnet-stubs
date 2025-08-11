"""Automatically generated stubs for C# namespace: System.Security.AccessControl."""

from abc import ABC
from collections.abc import Iterator
from typing import ClassVar
from typing import overload

from System import Array
from System import Boolean
from System import Enum
from System import Exception
from System import Guid
from System import Object
from System import Type
from System import UnauthorizedAccessException
from System.Collections import ICollection
from System.Collections import IDictionary
from System.Collections import IEnumerable
from System.Collections import IEnumerator
from System.Collections import ReadOnlyCollectionBase
from System.Reflection import MethodBase
from System.Runtime.InteropServices import _Exception
from System.Runtime.Serialization import ISerializable
from System.Runtime.Serialization import SerializationInfo
from System.Runtime.Serialization import StreamingContext
from System.Security.Principal import IdentityReference
from System.Security.Principal import SecurityIdentifier

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class AccessControlActions(Enum):
    """"""

    _None: AccessControlActions = ...
    """"""
    View: AccessControlActions = ...
    """"""
    Change: AccessControlActions = ...
    """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class AccessControlModification(Enum):
    """"""

    Add: AccessControlModification = ...
    """"""
    Set: AccessControlModification = ...
    """"""
    Reset: AccessControlModification = ...
    """"""
    Remove: AccessControlModification = ...
    """"""
    RemoveAll: AccessControlModification = ...
    """"""
    RemoveSpecific: AccessControlModification = ...
    """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class AccessControlSections(Enum):
    """"""

    _None: AccessControlSections = ...
    """"""
    Audit: AccessControlSections = ...
    """"""
    Access: AccessControlSections = ...
    """"""
    Owner: AccessControlSections = ...
    """"""
    Group: AccessControlSections = ...
    """"""
    All: AccessControlSections = ...
    """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class AccessControlType(Enum):
    """"""

    Allow: AccessControlType = ...
    """"""
    Deny: AccessControlType = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class AccessRule(ABC, AuthorizationRule):
    """"""
    @property
    def AccessControlType(self) -> AccessControlType:
        """"""
    @property
    def IdentityReference(self) -> IdentityReference:
        """"""
    @property
    def InheritanceFlags(self) -> InheritanceFlags:
        """"""
    @property
    def IsInherited(self) -> bool:
        """"""
    @property
    def PropagationFlags(self) -> PropagationFlags:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class AccessRule[T](AccessRule):
    """"""
    @overload
    def __init__(self, identity: IdentityReference, rights: T, type: AccessControlType) -> None:
        """"""
    @overload
    def __init__(self, identity: str, rights: T, type: AccessControlType) -> None:
        """"""
    @overload
    def __init__(
        self,
        identity: IdentityReference,
        rights: T,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
        type: AccessControlType,
    ) -> None:
        """"""
    @overload
    def __init__(
        self,
        identity: str,
        rights: T,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
        type: AccessControlType,
    ) -> None:
        """"""
    @property
    def AccessControlType(self) -> AccessControlType:
        """"""
    @property
    def IdentityReference(self) -> IdentityReference:
        """"""
    @property
    def InheritanceFlags(self) -> InheritanceFlags:
        """"""
    @property
    def IsInherited(self) -> bool:
        """"""
    @property
    def PropagationFlags(self) -> PropagationFlags:
        """"""
    @property
    def Rights(self) -> T:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class AceEnumerator(Object, IEnumerator):
    """"""
    @property
    def Current(self) -> GenericAce:
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

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class AceFlags(Enum):
    """"""

    _None: AceFlags = ...
    """"""
    ObjectInherit: AceFlags = ...
    """"""
    ContainerInherit: AceFlags = ...
    """"""
    NoPropagateInherit: AceFlags = ...
    """"""
    InheritOnly: AceFlags = ...
    """"""
    InheritanceFlags: AceFlags = ...
    """"""
    Inherited: AceFlags = ...
    """"""
    SuccessfulAccess: AceFlags = ...
    """"""
    FailedAccess: AceFlags = ...
    """"""
    AuditFlags: AceFlags = ...
    """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class AceQualifier(Enum):
    """"""

    AccessAllowed: AceQualifier = ...
    """"""
    AccessDenied: AceQualifier = ...
    """"""
    SystemAudit: AceQualifier = ...
    """"""
    SystemAlarm: AceQualifier = ...
    """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class AceType(Enum):
    """"""

    AccessAllowed: AceType = ...
    """"""
    AccessDenied: AceType = ...
    """"""
    SystemAudit: AceType = ...
    """"""
    SystemAlarm: AceType = ...
    """"""
    AccessAllowedCompound: AceType = ...
    """"""
    AccessAllowedObject: AceType = ...
    """"""
    AccessDeniedObject: AceType = ...
    """"""
    SystemAuditObject: AceType = ...
    """"""
    SystemAlarmObject: AceType = ...
    """"""
    AccessAllowedCallback: AceType = ...
    """"""
    AccessDeniedCallback: AceType = ...
    """"""
    AccessAllowedCallbackObject: AceType = ...
    """"""
    AccessDeniedCallbackObject: AceType = ...
    """"""
    SystemAuditCallback: AceType = ...
    """"""
    SystemAlarmCallback: AceType = ...
    """"""
    SystemAuditCallbackObject: AceType = ...
    """"""
    SystemAlarmCallbackObject: AceType = ...
    """"""
    MaxDefinedAceType: AceType = ...
    """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class AuditFlags(Enum):
    """"""

    _None: AuditFlags = ...
    """"""
    Success: AuditFlags = ...
    """"""
    Failure: AuditFlags = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class AuditRule(ABC, AuthorizationRule):
    """"""
    @property
    def AuditFlags(self) -> AuditFlags:
        """"""
    @property
    def IdentityReference(self) -> IdentityReference:
        """"""
    @property
    def InheritanceFlags(self) -> InheritanceFlags:
        """"""
    @property
    def IsInherited(self) -> bool:
        """"""
    @property
    def PropagationFlags(self) -> PropagationFlags:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class AuditRule[T](AuditRule):
    """"""
    @overload
    def __init__(self, identity: IdentityReference, rights: T, flags: AuditFlags) -> None:
        """"""
    @overload
    def __init__(
        self,
        identity: IdentityReference,
        rights: T,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
        flags: AuditFlags,
    ) -> None:
        """"""
    @overload
    def __init__(self, identity: str, rights: T, flags: AuditFlags) -> None:
        """"""
    @overload
    def __init__(
        self,
        identity: str,
        rights: T,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
        flags: AuditFlags,
    ) -> None:
        """"""
    @property
    def AuditFlags(self) -> AuditFlags:
        """"""
    @property
    def IdentityReference(self) -> IdentityReference:
        """"""
    @property
    def InheritanceFlags(self) -> InheritanceFlags:
        """"""
    @property
    def IsInherited(self) -> bool:
        """"""
    @property
    def PropagationFlags(self) -> PropagationFlags:
        """"""
    @property
    def Rights(self) -> T:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class AuthorizationRule(ABC, Object):
    """"""
    @property
    def IdentityReference(self) -> IdentityReference:
        """"""
    @property
    def InheritanceFlags(self) -> InheritanceFlags:
        """"""
    @property
    def IsInherited(self) -> bool:
        """"""
    @property
    def PropagationFlags(self) -> PropagationFlags:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class AuthorizationRuleCollection(ReadOnlyCollectionBase, ICollection, IEnumerable):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def Item(self) -> AuthorizationRule:
        """"""
    @property
    def SyncRoot(self) -> object:
        """"""
    def AddRule(self, rule: AuthorizationRule) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    @overload
    def CopyTo(self, rules: Array[AuthorizationRule], index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, index: int) -> AuthorizationRule:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CommonAce(QualifiedAce):
    """"""
    def __init__(
        self,
        flags: AceFlags,
        qualifier: AceQualifier,
        accessMask: int,
        sid: SecurityIdentifier,
        isCallback: bool,
        opaque: Array[int],
    ) -> None:
        """"""
    @property
    def AccessMask(self) -> int:
        """"""
    @AccessMask.setter
    def AccessMask(self, value: int) -> None: ...
    @property
    def AceFlags(self) -> AceFlags:
        """"""
    @AceFlags.setter
    def AceFlags(self, value: AceFlags) -> None: ...
    @property
    def AceQualifier(self) -> AceQualifier:
        """"""
    @property
    def AceType(self) -> AceType:
        """"""
    @property
    def AuditFlags(self) -> AuditFlags:
        """"""
    @property
    def BinaryLength(self) -> int:
        """"""
    @property
    def InheritanceFlags(self) -> InheritanceFlags:
        """"""
    @property
    def IsCallback(self) -> bool:
        """"""
    @property
    def IsInherited(self) -> bool:
        """"""
    @property
    def OpaqueLength(self) -> int:
        """"""
    @property
    def PropagationFlags(self) -> PropagationFlags:
        """"""
    @property
    def SecurityIdentifier(self) -> SecurityIdentifier:
        """"""
    @SecurityIdentifier.setter
    def SecurityIdentifier(self, value: SecurityIdentifier) -> None: ...
    def Copy(self) -> GenericAce:
        """"""
    def Equals(self, o: object) -> bool:
        """"""
    def GetBinaryForm(self, binaryForm: Array[int], offset: int) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetOpaque(self) -> Array[int]:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def MaxOpaqueLength(cls, isCallback: bool) -> int:
        """"""
    def SetOpaque(self, opaque: Array[int]) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CommonAcl(ABC, GenericAcl, ICollection, IEnumerable):
    """"""
    @property
    def BinaryLength(self) -> int:
        """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsCanonical(self) -> bool:
        """"""
    @property
    def IsContainer(self) -> bool:
        """"""
    @property
    def IsDS(self) -> bool:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def Item(self) -> GenericAce:
        """"""
    @Item.setter
    def Item(self, value: GenericAce) -> None: ...
    @property
    def Revision(self) -> int:
        """"""
    @property
    def SyncRoot(self) -> object:
        """"""
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array[GenericAce], index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetBinaryForm(self, binaryForm: Array[int], offset: int) -> None:
        """"""
    def GetEnumerator(self) -> AceEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Purge(self, sid: SecurityIdentifier) -> None:
        """"""
    def RemoveInheritedAces(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, index: int) -> GenericAce:
        """"""
    def __setitem__(self, index: int, value: GenericAce) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CommonObjectSecurity(ABC, ObjectSecurity):
    """"""
    @property
    def AccessRightType(self) -> Type:
        """"""
    @property
    def AccessRuleType(self) -> Type:
        """"""
    @property
    def AreAccessRulesCanonical(self) -> bool:
        """"""
    @property
    def AreAccessRulesProtected(self) -> bool:
        """"""
    @property
    def AreAuditRulesCanonical(self) -> bool:
        """"""
    @property
    def AreAuditRulesProtected(self) -> bool:
        """"""
    @property
    def AuditRuleType(self) -> Type:
        """"""
    def AccessRuleFactory(
        self,
        identityReference: IdentityReference,
        accessMask: int,
        isInherited: bool,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
        type: AccessControlType,
    ) -> AccessRule:
        """"""
    def AuditRuleFactory(
        self,
        identityReference: IdentityReference,
        accessMask: int,
        isInherited: bool,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
        flags: AuditFlags,
    ) -> AuditRule:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetAccessRules(
        self, includeExplicit: bool, includeInherited: bool, targetType: Type
    ) -> AuthorizationRuleCollection:
        """"""
    def GetAuditRules(
        self, includeExplicit: bool, includeInherited: bool, targetType: Type
    ) -> AuthorizationRuleCollection:
        """"""
    def GetGroup(self, targetType: Type) -> IdentityReference:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetOwner(self, targetType: Type) -> IdentityReference:
        """"""
    def GetSecurityDescriptorBinaryForm(self) -> Array[int]:
        """"""
    def GetSecurityDescriptorSddlForm(self, includeSections: AccessControlSections) -> str:
        """"""
    def GetType(self) -> Type:
        """"""
    def ModifyAccessRule(
        self, modification: AccessControlModification, rule: AccessRule, modified: Boolean
    ) -> tuple[bool, Boolean]:
        """"""
    def ModifyAuditRule(
        self, modification: AccessControlModification, rule: AuditRule, modified: Boolean
    ) -> tuple[bool, Boolean]:
        """"""
    def PurgeAccessRules(self, identity: IdentityReference) -> None:
        """"""
    def PurgeAuditRules(self, identity: IdentityReference) -> None:
        """"""
    def SetAccessRuleProtection(self, isProtected: bool, preserveInheritance: bool) -> None:
        """"""
    def SetAuditRuleProtection(self, isProtected: bool, preserveInheritance: bool) -> None:
        """"""
    def SetGroup(self, identity: IdentityReference) -> None:
        """"""
    def SetOwner(self, identity: IdentityReference) -> None:
        """"""
    @overload
    def SetSecurityDescriptorBinaryForm(self, binaryForm: Array[int]) -> None:
        """"""
    @overload
    def SetSecurityDescriptorBinaryForm(
        self, binaryForm: Array[int], includeSections: AccessControlSections
    ) -> None:
        """"""
    @overload
    def SetSecurityDescriptorSddlForm(self, sddlForm: str) -> None:
        """"""
    @overload
    def SetSecurityDescriptorSddlForm(
        self, sddlForm: str, includeSections: AccessControlSections
    ) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CommonSecurityDescriptor(GenericSecurityDescriptor):
    """"""
    @overload
    def __init__(
        self,
        isContainer: bool,
        isDS: bool,
        flags: ControlFlags,
        owner: SecurityIdentifier,
        group: SecurityIdentifier,
        systemAcl: SystemAcl,
        discretionaryAcl: DiscretionaryAcl,
    ) -> None:
        """"""
    @overload
    def __init__(
        self, isContainer: bool, isDS: bool, rawSecurityDescriptor: RawSecurityDescriptor
    ) -> None:
        """"""
    @overload
    def __init__(self, isContainer: bool, isDS: bool, sddlForm: str) -> None:
        """"""
    @overload
    def __init__(self, isContainer: bool, isDS: bool, binaryForm: Array[int], offset: int) -> None:
        """"""
    @property
    def BinaryLength(self) -> int:
        """"""
    @property
    def ControlFlags(self) -> ControlFlags:
        """"""
    @property
    def DiscretionaryAcl(self) -> DiscretionaryAcl:
        """"""
    @DiscretionaryAcl.setter
    def DiscretionaryAcl(self, value: DiscretionaryAcl) -> None: ...
    @property
    def Group(self) -> SecurityIdentifier:
        """"""
    @Group.setter
    def Group(self, value: SecurityIdentifier) -> None: ...
    @property
    def IsContainer(self) -> bool:
        """"""
    @property
    def IsDS(self) -> bool:
        """"""
    @property
    def IsDiscretionaryAclCanonical(self) -> bool:
        """"""
    @property
    def IsSystemAclCanonical(self) -> bool:
        """"""
    @property
    def Owner(self) -> SecurityIdentifier:
        """"""
    @Owner.setter
    def Owner(self, value: SecurityIdentifier) -> None: ...
    @property
    def SystemAcl(self) -> SystemAcl:
        """"""
    @SystemAcl.setter
    def SystemAcl(self, value: SystemAcl) -> None: ...
    def AddDiscretionaryAcl(self, revision: int, trusted: int) -> None:
        """"""
    def AddSystemAcl(self, revision: int, trusted: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetBinaryForm(self, binaryForm: Array[int], offset: int) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetSddlForm(self, includeSections: AccessControlSections) -> str:
        """"""
    def GetType(self) -> Type:
        """"""
    def PurgeAccessControl(self, sid: SecurityIdentifier) -> None:
        """"""
    def PurgeAudit(self, sid: SecurityIdentifier) -> None:
        """"""
    def SetDiscretionaryAclProtection(self, isProtected: bool, preserveInheritance: bool) -> None:
        """"""
    def SetSystemAclProtection(self, isProtected: bool, preserveInheritance: bool) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CompoundAce(KnownAce):
    """"""
    def __init__(
        self,
        flags: AceFlags,
        accessMask: int,
        compoundAceType: CompoundAceType,
        sid: SecurityIdentifier,
    ) -> None:
        """"""
    @property
    def AccessMask(self) -> int:
        """"""
    @AccessMask.setter
    def AccessMask(self, value: int) -> None: ...
    @property
    def AceFlags(self) -> AceFlags:
        """"""
    @AceFlags.setter
    def AceFlags(self, value: AceFlags) -> None: ...
    @property
    def AceType(self) -> AceType:
        """"""
    @property
    def AuditFlags(self) -> AuditFlags:
        """"""
    @property
    def BinaryLength(self) -> int:
        """"""
    @property
    def CompoundAceType(self) -> CompoundAceType:
        """"""
    @CompoundAceType.setter
    def CompoundAceType(self, value: CompoundAceType) -> None: ...
    @property
    def InheritanceFlags(self) -> InheritanceFlags:
        """"""
    @property
    def IsInherited(self) -> bool:
        """"""
    @property
    def PropagationFlags(self) -> PropagationFlags:
        """"""
    @property
    def SecurityIdentifier(self) -> SecurityIdentifier:
        """"""
    @SecurityIdentifier.setter
    def SecurityIdentifier(self, value: SecurityIdentifier) -> None: ...
    def Copy(self) -> GenericAce:
        """"""
    def Equals(self, o: object) -> bool:
        """"""
    def GetBinaryForm(self, binaryForm: Array[int], offset: int) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class CompoundAceType(Enum):
    """"""

    Impersonation: CompoundAceType = ...
    """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class ControlFlags(Enum):
    """"""

    _None: ControlFlags = ...
    """"""
    OwnerDefaulted: ControlFlags = ...
    """"""
    GroupDefaulted: ControlFlags = ...
    """"""
    DiscretionaryAclPresent: ControlFlags = ...
    """"""
    DiscretionaryAclDefaulted: ControlFlags = ...
    """"""
    SystemAclPresent: ControlFlags = ...
    """"""
    SystemAclDefaulted: ControlFlags = ...
    """"""
    DiscretionaryAclUntrusted: ControlFlags = ...
    """"""
    ServerSecurity: ControlFlags = ...
    """"""
    DiscretionaryAclAutoInheritRequired: ControlFlags = ...
    """"""
    SystemAclAutoInheritRequired: ControlFlags = ...
    """"""
    DiscretionaryAclAutoInherited: ControlFlags = ...
    """"""
    SystemAclAutoInherited: ControlFlags = ...
    """"""
    DiscretionaryAclProtected: ControlFlags = ...
    """"""
    SystemAclProtected: ControlFlags = ...
    """"""
    RMControlValid: ControlFlags = ...
    """"""
    SelfRelative: ControlFlags = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CryptoKeyAccessRule(AccessRule):
    """"""
    @overload
    def __init__(
        self, identity: IdentityReference, cryptoKeyRights: CryptoKeyRights, type: AccessControlType
    ) -> None:
        """"""
    @overload
    def __init__(
        self, identity: str, cryptoKeyRights: CryptoKeyRights, type: AccessControlType
    ) -> None:
        """"""
    @property
    def AccessControlType(self) -> AccessControlType:
        """"""
    @property
    def CryptoKeyRights(self) -> CryptoKeyRights:
        """"""
    @property
    def IdentityReference(self) -> IdentityReference:
        """"""
    @property
    def InheritanceFlags(self) -> InheritanceFlags:
        """"""
    @property
    def IsInherited(self) -> bool:
        """"""
    @property
    def PropagationFlags(self) -> PropagationFlags:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CryptoKeyAuditRule(AuditRule):
    """"""
    @overload
    def __init__(
        self, identity: IdentityReference, cryptoKeyRights: CryptoKeyRights, flags: AuditFlags
    ) -> None:
        """"""
    @overload
    def __init__(self, identity: str, cryptoKeyRights: CryptoKeyRights, flags: AuditFlags) -> None:
        """"""
    @property
    def AuditFlags(self) -> AuditFlags:
        """"""
    @property
    def CryptoKeyRights(self) -> CryptoKeyRights:
        """"""
    @property
    def IdentityReference(self) -> IdentityReference:
        """"""
    @property
    def InheritanceFlags(self) -> InheritanceFlags:
        """"""
    @property
    def IsInherited(self) -> bool:
        """"""
    @property
    def PropagationFlags(self) -> PropagationFlags:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class CryptoKeyRights(Enum):
    """"""

    ReadData: CryptoKeyRights = ...
    """"""
    WriteData: CryptoKeyRights = ...
    """"""
    ReadExtendedAttributes: CryptoKeyRights = ...
    """"""
    WriteExtendedAttributes: CryptoKeyRights = ...
    """"""
    ReadAttributes: CryptoKeyRights = ...
    """"""
    WriteAttributes: CryptoKeyRights = ...
    """"""
    Delete: CryptoKeyRights = ...
    """"""
    ReadPermissions: CryptoKeyRights = ...
    """"""
    ChangePermissions: CryptoKeyRights = ...
    """"""
    TakeOwnership: CryptoKeyRights = ...
    """"""
    Synchronize: CryptoKeyRights = ...
    """"""
    FullControl: CryptoKeyRights = ...
    """"""
    GenericAll: CryptoKeyRights = ...
    """"""
    GenericExecute: CryptoKeyRights = ...
    """"""
    GenericWrite: CryptoKeyRights = ...
    """"""
    GenericRead: CryptoKeyRights = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CryptoKeySecurity(NativeObjectSecurity):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, securityDescriptor: CommonSecurityDescriptor) -> None:
        """"""
    @property
    def AccessRightType(self) -> Type:
        """"""
    @property
    def AccessRuleType(self) -> Type:
        """"""
    @property
    def AreAccessRulesCanonical(self) -> bool:
        """"""
    @property
    def AreAccessRulesProtected(self) -> bool:
        """"""
    @property
    def AreAuditRulesCanonical(self) -> bool:
        """"""
    @property
    def AreAuditRulesProtected(self) -> bool:
        """"""
    @property
    def AuditRuleType(self) -> Type:
        """"""
    def AccessRuleFactory(
        self,
        identityReference: IdentityReference,
        accessMask: int,
        isInherited: bool,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
        type: AccessControlType,
    ) -> AccessRule:
        """"""
    def AddAccessRule(self, rule: CryptoKeyAccessRule) -> None:
        """"""
    def AddAuditRule(self, rule: CryptoKeyAuditRule) -> None:
        """"""
    def AuditRuleFactory(
        self,
        identityReference: IdentityReference,
        accessMask: int,
        isInherited: bool,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
        flags: AuditFlags,
    ) -> AuditRule:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetAccessRules(
        self, includeExplicit: bool, includeInherited: bool, targetType: Type
    ) -> AuthorizationRuleCollection:
        """"""
    def GetAuditRules(
        self, includeExplicit: bool, includeInherited: bool, targetType: Type
    ) -> AuthorizationRuleCollection:
        """"""
    def GetGroup(self, targetType: Type) -> IdentityReference:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetOwner(self, targetType: Type) -> IdentityReference:
        """"""
    def GetSecurityDescriptorBinaryForm(self) -> Array[int]:
        """"""
    def GetSecurityDescriptorSddlForm(self, includeSections: AccessControlSections) -> str:
        """"""
    def GetType(self) -> Type:
        """"""
    def ModifyAccessRule(
        self, modification: AccessControlModification, rule: AccessRule, modified: Boolean
    ) -> tuple[bool, Boolean]:
        """"""
    def ModifyAuditRule(
        self, modification: AccessControlModification, rule: AuditRule, modified: Boolean
    ) -> tuple[bool, Boolean]:
        """"""
    def PurgeAccessRules(self, identity: IdentityReference) -> None:
        """"""
    def PurgeAuditRules(self, identity: IdentityReference) -> None:
        """"""
    def RemoveAccessRule(self, rule: CryptoKeyAccessRule) -> bool:
        """"""
    def RemoveAccessRuleAll(self, rule: CryptoKeyAccessRule) -> None:
        """"""
    def RemoveAccessRuleSpecific(self, rule: CryptoKeyAccessRule) -> None:
        """"""
    def RemoveAuditRule(self, rule: CryptoKeyAuditRule) -> bool:
        """"""
    def RemoveAuditRuleAll(self, rule: CryptoKeyAuditRule) -> None:
        """"""
    def RemoveAuditRuleSpecific(self, rule: CryptoKeyAuditRule) -> None:
        """"""
    def ResetAccessRule(self, rule: CryptoKeyAccessRule) -> None:
        """"""
    def SetAccessRule(self, rule: CryptoKeyAccessRule) -> None:
        """"""
    def SetAccessRuleProtection(self, isProtected: bool, preserveInheritance: bool) -> None:
        """"""
    def SetAuditRule(self, rule: CryptoKeyAuditRule) -> None:
        """"""
    def SetAuditRuleProtection(self, isProtected: bool, preserveInheritance: bool) -> None:
        """"""
    def SetGroup(self, identity: IdentityReference) -> None:
        """"""
    def SetOwner(self, identity: IdentityReference) -> None:
        """"""
    @overload
    def SetSecurityDescriptorBinaryForm(self, binaryForm: Array[int]) -> None:
        """"""
    @overload
    def SetSecurityDescriptorBinaryForm(
        self, binaryForm: Array[int], includeSections: AccessControlSections
    ) -> None:
        """"""
    @overload
    def SetSecurityDescriptorSddlForm(self, sddlForm: str) -> None:
        """"""
    @overload
    def SetSecurityDescriptorSddlForm(
        self, sddlForm: str, includeSections: AccessControlSections
    ) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CustomAce(GenericAce):
    """"""

    MaxOpaqueLength: ClassVar[int]
    """"""
    def __init__(self, type: AceType, flags: AceFlags, opaque: Array[int]) -> None:
        """"""
    @property
    def AceFlags(self) -> AceFlags:
        """"""
    @AceFlags.setter
    def AceFlags(self, value: AceFlags) -> None: ...
    @property
    def AceType(self) -> AceType:
        """"""
    @property
    def AuditFlags(self) -> AuditFlags:
        """"""
    @property
    def BinaryLength(self) -> int:
        """"""
    @property
    def InheritanceFlags(self) -> InheritanceFlags:
        """"""
    @property
    def IsInherited(self) -> bool:
        """"""
    @property
    def OpaqueLength(self) -> int:
        """"""
    @property
    def PropagationFlags(self) -> PropagationFlags:
        """"""
    def Copy(self) -> GenericAce:
        """"""
    def Equals(self, o: object) -> bool:
        """"""
    def GetBinaryForm(self, binaryForm: Array[int], offset: int) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetOpaque(self) -> Array[int]:
        """"""
    def GetType(self) -> Type:
        """"""
    def SetOpaque(self, opaque: Array[int]) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class DirectoryObjectSecurity(ABC, ObjectSecurity):
    """"""
    @property
    def AccessRightType(self) -> Type:
        """"""
    @property
    def AccessRuleType(self) -> Type:
        """"""
    @property
    def AreAccessRulesCanonical(self) -> bool:
        """"""
    @property
    def AreAccessRulesProtected(self) -> bool:
        """"""
    @property
    def AreAuditRulesCanonical(self) -> bool:
        """"""
    @property
    def AreAuditRulesProtected(self) -> bool:
        """"""
    @property
    def AuditRuleType(self) -> Type:
        """"""
    @overload
    def AccessRuleFactory(
        self,
        identityReference: IdentityReference,
        accessMask: int,
        isInherited: bool,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
        type: AccessControlType,
    ) -> AccessRule:
        """"""
    @overload
    def AccessRuleFactory(
        self,
        identityReference: IdentityReference,
        accessMask: int,
        isInherited: bool,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
        type: AccessControlType,
        objectType: Guid,
        inheritedObjectType: Guid,
    ) -> AccessRule:
        """"""
    @overload
    def AuditRuleFactory(
        self,
        identityReference: IdentityReference,
        accessMask: int,
        isInherited: bool,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
        flags: AuditFlags,
    ) -> AuditRule:
        """"""
    @overload
    def AuditRuleFactory(
        self,
        identityReference: IdentityReference,
        accessMask: int,
        isInherited: bool,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
        flags: AuditFlags,
        objectType: Guid,
        inheritedObjectType: Guid,
    ) -> AuditRule:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetAccessRules(
        self, includeExplicit: bool, includeInherited: bool, targetType: Type
    ) -> AuthorizationRuleCollection:
        """"""
    def GetAuditRules(
        self, includeExplicit: bool, includeInherited: bool, targetType: Type
    ) -> AuthorizationRuleCollection:
        """"""
    def GetGroup(self, targetType: Type) -> IdentityReference:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetOwner(self, targetType: Type) -> IdentityReference:
        """"""
    def GetSecurityDescriptorBinaryForm(self) -> Array[int]:
        """"""
    def GetSecurityDescriptorSddlForm(self, includeSections: AccessControlSections) -> str:
        """"""
    def GetType(self) -> Type:
        """"""
    def ModifyAccessRule(
        self, modification: AccessControlModification, rule: AccessRule, modified: Boolean
    ) -> tuple[bool, Boolean]:
        """"""
    def ModifyAuditRule(
        self, modification: AccessControlModification, rule: AuditRule, modified: Boolean
    ) -> tuple[bool, Boolean]:
        """"""
    def PurgeAccessRules(self, identity: IdentityReference) -> None:
        """"""
    def PurgeAuditRules(self, identity: IdentityReference) -> None:
        """"""
    def SetAccessRuleProtection(self, isProtected: bool, preserveInheritance: bool) -> None:
        """"""
    def SetAuditRuleProtection(self, isProtected: bool, preserveInheritance: bool) -> None:
        """"""
    def SetGroup(self, identity: IdentityReference) -> None:
        """"""
    def SetOwner(self, identity: IdentityReference) -> None:
        """"""
    @overload
    def SetSecurityDescriptorBinaryForm(self, binaryForm: Array[int]) -> None:
        """"""
    @overload
    def SetSecurityDescriptorBinaryForm(
        self, binaryForm: Array[int], includeSections: AccessControlSections
    ) -> None:
        """"""
    @overload
    def SetSecurityDescriptorSddlForm(self, sddlForm: str) -> None:
        """"""
    @overload
    def SetSecurityDescriptorSddlForm(
        self, sddlForm: str, includeSections: AccessControlSections
    ) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class DirectorySecurity(FileSystemSecurity):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, name: str, includeSections: AccessControlSections) -> None:
        """"""
    @property
    def AccessRightType(self) -> Type:
        """"""
    @property
    def AccessRuleType(self) -> Type:
        """"""
    @property
    def AreAccessRulesCanonical(self) -> bool:
        """"""
    @property
    def AreAccessRulesProtected(self) -> bool:
        """"""
    @property
    def AreAuditRulesCanonical(self) -> bool:
        """"""
    @property
    def AreAuditRulesProtected(self) -> bool:
        """"""
    @property
    def AuditRuleType(self) -> Type:
        """"""
    def AccessRuleFactory(
        self,
        identityReference: IdentityReference,
        accessMask: int,
        isInherited: bool,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
        type: AccessControlType,
    ) -> AccessRule:
        """"""
    def AddAccessRule(self, rule: FileSystemAccessRule) -> None:
        """"""
    def AddAuditRule(self, rule: FileSystemAuditRule) -> None:
        """"""
    def AuditRuleFactory(
        self,
        identityReference: IdentityReference,
        accessMask: int,
        isInherited: bool,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
        flags: AuditFlags,
    ) -> AuditRule:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetAccessRules(
        self, includeExplicit: bool, includeInherited: bool, targetType: Type
    ) -> AuthorizationRuleCollection:
        """"""
    def GetAuditRules(
        self, includeExplicit: bool, includeInherited: bool, targetType: Type
    ) -> AuthorizationRuleCollection:
        """"""
    def GetGroup(self, targetType: Type) -> IdentityReference:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetOwner(self, targetType: Type) -> IdentityReference:
        """"""
    def GetSecurityDescriptorBinaryForm(self) -> Array[int]:
        """"""
    def GetSecurityDescriptorSddlForm(self, includeSections: AccessControlSections) -> str:
        """"""
    def GetType(self) -> Type:
        """"""
    def ModifyAccessRule(
        self, modification: AccessControlModification, rule: AccessRule, modified: Boolean
    ) -> tuple[bool, Boolean]:
        """"""
    def ModifyAuditRule(
        self, modification: AccessControlModification, rule: AuditRule, modified: Boolean
    ) -> tuple[bool, Boolean]:
        """"""
    def PurgeAccessRules(self, identity: IdentityReference) -> None:
        """"""
    def PurgeAuditRules(self, identity: IdentityReference) -> None:
        """"""
    def RemoveAccessRule(self, rule: FileSystemAccessRule) -> bool:
        """"""
    def RemoveAccessRuleAll(self, rule: FileSystemAccessRule) -> None:
        """"""
    def RemoveAccessRuleSpecific(self, rule: FileSystemAccessRule) -> None:
        """"""
    def RemoveAuditRule(self, rule: FileSystemAuditRule) -> bool:
        """"""
    def RemoveAuditRuleAll(self, rule: FileSystemAuditRule) -> None:
        """"""
    def RemoveAuditRuleSpecific(self, rule: FileSystemAuditRule) -> None:
        """"""
    def ResetAccessRule(self, rule: FileSystemAccessRule) -> None:
        """"""
    def SetAccessRule(self, rule: FileSystemAccessRule) -> None:
        """"""
    def SetAccessRuleProtection(self, isProtected: bool, preserveInheritance: bool) -> None:
        """"""
    def SetAuditRule(self, rule: FileSystemAuditRule) -> None:
        """"""
    def SetAuditRuleProtection(self, isProtected: bool, preserveInheritance: bool) -> None:
        """"""
    def SetGroup(self, identity: IdentityReference) -> None:
        """"""
    def SetOwner(self, identity: IdentityReference) -> None:
        """"""
    @overload
    def SetSecurityDescriptorBinaryForm(self, binaryForm: Array[int]) -> None:
        """"""
    @overload
    def SetSecurityDescriptorBinaryForm(
        self, binaryForm: Array[int], includeSections: AccessControlSections
    ) -> None:
        """"""
    @overload
    def SetSecurityDescriptorSddlForm(self, sddlForm: str) -> None:
        """"""
    @overload
    def SetSecurityDescriptorSddlForm(
        self, sddlForm: str, includeSections: AccessControlSections
    ) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class DiscretionaryAcl(CommonAcl, ICollection, IEnumerable):
    """"""
    @overload
    def __init__(self, isContainer: bool, isDS: bool, capacity: int) -> None:
        """"""
    @overload
    def __init__(self, isContainer: bool, isDS: bool, revision: int, capacity: int) -> None:
        """"""
    @overload
    def __init__(self, isContainer: bool, isDS: bool, rawAcl: RawAcl) -> None:
        """"""
    @property
    def BinaryLength(self) -> int:
        """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsCanonical(self) -> bool:
        """"""
    @property
    def IsContainer(self) -> bool:
        """"""
    @property
    def IsDS(self) -> bool:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def Item(self) -> GenericAce:
        """"""
    @Item.setter
    def Item(self, value: GenericAce) -> None: ...
    @property
    def Revision(self) -> int:
        """"""
    @property
    def SyncRoot(self) -> object:
        """"""
    @overload
    def AddAccess(
        self, accessType: AccessControlType, sid: SecurityIdentifier, rule: ObjectAccessRule
    ) -> None:
        """"""
    @overload
    def AddAccess(
        self,
        accessType: AccessControlType,
        sid: SecurityIdentifier,
        accessMask: int,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
    ) -> None:
        """"""
    @overload
    def AddAccess(
        self,
        accessType: AccessControlType,
        sid: SecurityIdentifier,
        accessMask: int,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
        objectFlags: ObjectAceFlags,
        objectType: Guid,
        inheritedObjectType: Guid,
    ) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array[GenericAce], index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetBinaryForm(self, binaryForm: Array[int], offset: int) -> None:
        """"""
    def GetEnumerator(self) -> AceEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Purge(self, sid: SecurityIdentifier) -> None:
        """"""
    @overload
    def RemoveAccess(
        self, accessType: AccessControlType, sid: SecurityIdentifier, rule: ObjectAccessRule
    ) -> bool:
        """"""
    @overload
    def RemoveAccess(
        self,
        accessType: AccessControlType,
        sid: SecurityIdentifier,
        accessMask: int,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
    ) -> bool:
        """"""
    @overload
    def RemoveAccess(
        self,
        accessType: AccessControlType,
        sid: SecurityIdentifier,
        accessMask: int,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
        objectFlags: ObjectAceFlags,
        objectType: Guid,
        inheritedObjectType: Guid,
    ) -> bool:
        """"""
    @overload
    def RemoveAccessSpecific(
        self, accessType: AccessControlType, sid: SecurityIdentifier, rule: ObjectAccessRule
    ) -> None:
        """"""
    @overload
    def RemoveAccessSpecific(
        self,
        accessType: AccessControlType,
        sid: SecurityIdentifier,
        accessMask: int,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
    ) -> None:
        """"""
    @overload
    def RemoveAccessSpecific(
        self,
        accessType: AccessControlType,
        sid: SecurityIdentifier,
        accessMask: int,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
        objectFlags: ObjectAceFlags,
        objectType: Guid,
        inheritedObjectType: Guid,
    ) -> None:
        """"""
    def RemoveInheritedAces(self) -> None:
        """"""
    @overload
    def SetAccess(
        self, accessType: AccessControlType, sid: SecurityIdentifier, rule: ObjectAccessRule
    ) -> None:
        """"""
    @overload
    def SetAccess(
        self,
        accessType: AccessControlType,
        sid: SecurityIdentifier,
        accessMask: int,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
    ) -> None:
        """"""
    @overload
    def SetAccess(
        self,
        accessType: AccessControlType,
        sid: SecurityIdentifier,
        accessMask: int,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
        objectFlags: ObjectAceFlags,
        objectType: Guid,
        inheritedObjectType: Guid,
    ) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, index: int) -> GenericAce:
        """"""
    def __setitem__(self, index: int, value: GenericAce) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class EventWaitHandleAccessRule(AccessRule):
    """"""
    @overload
    def __init__(
        self,
        identity: IdentityReference,
        eventRights: EventWaitHandleRights,
        type: AccessControlType,
    ) -> None:
        """"""
    @overload
    def __init__(
        self, identity: str, eventRights: EventWaitHandleRights, type: AccessControlType
    ) -> None:
        """"""
    @property
    def AccessControlType(self) -> AccessControlType:
        """"""
    @property
    def EventWaitHandleRights(self) -> EventWaitHandleRights:
        """"""
    @property
    def IdentityReference(self) -> IdentityReference:
        """"""
    @property
    def InheritanceFlags(self) -> InheritanceFlags:
        """"""
    @property
    def IsInherited(self) -> bool:
        """"""
    @property
    def PropagationFlags(self) -> PropagationFlags:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class EventWaitHandleAuditRule(AuditRule):
    """"""
    def __init__(
        self, identity: IdentityReference, eventRights: EventWaitHandleRights, flags: AuditFlags
    ) -> None:
        """"""
    @property
    def AuditFlags(self) -> AuditFlags:
        """"""
    @property
    def EventWaitHandleRights(self) -> EventWaitHandleRights:
        """"""
    @property
    def IdentityReference(self) -> IdentityReference:
        """"""
    @property
    def InheritanceFlags(self) -> InheritanceFlags:
        """"""
    @property
    def IsInherited(self) -> bool:
        """"""
    @property
    def PropagationFlags(self) -> PropagationFlags:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class EventWaitHandleRights(Enum):
    """"""

    Modify: EventWaitHandleRights = ...
    """"""
    Delete: EventWaitHandleRights = ...
    """"""
    ReadPermissions: EventWaitHandleRights = ...
    """"""
    ChangePermissions: EventWaitHandleRights = ...
    """"""
    TakeOwnership: EventWaitHandleRights = ...
    """"""
    Synchronize: EventWaitHandleRights = ...
    """"""
    FullControl: EventWaitHandleRights = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class EventWaitHandleSecurity(NativeObjectSecurity):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def AccessRightType(self) -> Type:
        """"""
    @property
    def AccessRuleType(self) -> Type:
        """"""
    @property
    def AreAccessRulesCanonical(self) -> bool:
        """"""
    @property
    def AreAccessRulesProtected(self) -> bool:
        """"""
    @property
    def AreAuditRulesCanonical(self) -> bool:
        """"""
    @property
    def AreAuditRulesProtected(self) -> bool:
        """"""
    @property
    def AuditRuleType(self) -> Type:
        """"""
    def AccessRuleFactory(
        self,
        identityReference: IdentityReference,
        accessMask: int,
        isInherited: bool,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
        type: AccessControlType,
    ) -> AccessRule:
        """"""
    def AddAccessRule(self, rule: EventWaitHandleAccessRule) -> None:
        """"""
    def AddAuditRule(self, rule: EventWaitHandleAuditRule) -> None:
        """"""
    def AuditRuleFactory(
        self,
        identityReference: IdentityReference,
        accessMask: int,
        isInherited: bool,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
        flags: AuditFlags,
    ) -> AuditRule:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetAccessRules(
        self, includeExplicit: bool, includeInherited: bool, targetType: Type
    ) -> AuthorizationRuleCollection:
        """"""
    def GetAuditRules(
        self, includeExplicit: bool, includeInherited: bool, targetType: Type
    ) -> AuthorizationRuleCollection:
        """"""
    def GetGroup(self, targetType: Type) -> IdentityReference:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetOwner(self, targetType: Type) -> IdentityReference:
        """"""
    def GetSecurityDescriptorBinaryForm(self) -> Array[int]:
        """"""
    def GetSecurityDescriptorSddlForm(self, includeSections: AccessControlSections) -> str:
        """"""
    def GetType(self) -> Type:
        """"""
    def ModifyAccessRule(
        self, modification: AccessControlModification, rule: AccessRule, modified: Boolean
    ) -> tuple[bool, Boolean]:
        """"""
    def ModifyAuditRule(
        self, modification: AccessControlModification, rule: AuditRule, modified: Boolean
    ) -> tuple[bool, Boolean]:
        """"""
    def PurgeAccessRules(self, identity: IdentityReference) -> None:
        """"""
    def PurgeAuditRules(self, identity: IdentityReference) -> None:
        """"""
    def RemoveAccessRule(self, rule: EventWaitHandleAccessRule) -> bool:
        """"""
    def RemoveAccessRuleAll(self, rule: EventWaitHandleAccessRule) -> None:
        """"""
    def RemoveAccessRuleSpecific(self, rule: EventWaitHandleAccessRule) -> None:
        """"""
    def RemoveAuditRule(self, rule: EventWaitHandleAuditRule) -> bool:
        """"""
    def RemoveAuditRuleAll(self, rule: EventWaitHandleAuditRule) -> None:
        """"""
    def RemoveAuditRuleSpecific(self, rule: EventWaitHandleAuditRule) -> None:
        """"""
    def ResetAccessRule(self, rule: EventWaitHandleAccessRule) -> None:
        """"""
    def SetAccessRule(self, rule: EventWaitHandleAccessRule) -> None:
        """"""
    def SetAccessRuleProtection(self, isProtected: bool, preserveInheritance: bool) -> None:
        """"""
    def SetAuditRule(self, rule: EventWaitHandleAuditRule) -> None:
        """"""
    def SetAuditRuleProtection(self, isProtected: bool, preserveInheritance: bool) -> None:
        """"""
    def SetGroup(self, identity: IdentityReference) -> None:
        """"""
    def SetOwner(self, identity: IdentityReference) -> None:
        """"""
    @overload
    def SetSecurityDescriptorBinaryForm(self, binaryForm: Array[int]) -> None:
        """"""
    @overload
    def SetSecurityDescriptorBinaryForm(
        self, binaryForm: Array[int], includeSections: AccessControlSections
    ) -> None:
        """"""
    @overload
    def SetSecurityDescriptorSddlForm(self, sddlForm: str) -> None:
        """"""
    @overload
    def SetSecurityDescriptorSddlForm(
        self, sddlForm: str, includeSections: AccessControlSections
    ) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class FileSecurity(FileSystemSecurity):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, fileName: str, includeSections: AccessControlSections) -> None:
        """"""
    @property
    def AccessRightType(self) -> Type:
        """"""
    @property
    def AccessRuleType(self) -> Type:
        """"""
    @property
    def AreAccessRulesCanonical(self) -> bool:
        """"""
    @property
    def AreAccessRulesProtected(self) -> bool:
        """"""
    @property
    def AreAuditRulesCanonical(self) -> bool:
        """"""
    @property
    def AreAuditRulesProtected(self) -> bool:
        """"""
    @property
    def AuditRuleType(self) -> Type:
        """"""
    def AccessRuleFactory(
        self,
        identityReference: IdentityReference,
        accessMask: int,
        isInherited: bool,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
        type: AccessControlType,
    ) -> AccessRule:
        """"""
    def AddAccessRule(self, rule: FileSystemAccessRule) -> None:
        """"""
    def AddAuditRule(self, rule: FileSystemAuditRule) -> None:
        """"""
    def AuditRuleFactory(
        self,
        identityReference: IdentityReference,
        accessMask: int,
        isInherited: bool,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
        flags: AuditFlags,
    ) -> AuditRule:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetAccessRules(
        self, includeExplicit: bool, includeInherited: bool, targetType: Type
    ) -> AuthorizationRuleCollection:
        """"""
    def GetAuditRules(
        self, includeExplicit: bool, includeInherited: bool, targetType: Type
    ) -> AuthorizationRuleCollection:
        """"""
    def GetGroup(self, targetType: Type) -> IdentityReference:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetOwner(self, targetType: Type) -> IdentityReference:
        """"""
    def GetSecurityDescriptorBinaryForm(self) -> Array[int]:
        """"""
    def GetSecurityDescriptorSddlForm(self, includeSections: AccessControlSections) -> str:
        """"""
    def GetType(self) -> Type:
        """"""
    def ModifyAccessRule(
        self, modification: AccessControlModification, rule: AccessRule, modified: Boolean
    ) -> tuple[bool, Boolean]:
        """"""
    def ModifyAuditRule(
        self, modification: AccessControlModification, rule: AuditRule, modified: Boolean
    ) -> tuple[bool, Boolean]:
        """"""
    def PurgeAccessRules(self, identity: IdentityReference) -> None:
        """"""
    def PurgeAuditRules(self, identity: IdentityReference) -> None:
        """"""
    def RemoveAccessRule(self, rule: FileSystemAccessRule) -> bool:
        """"""
    def RemoveAccessRuleAll(self, rule: FileSystemAccessRule) -> None:
        """"""
    def RemoveAccessRuleSpecific(self, rule: FileSystemAccessRule) -> None:
        """"""
    def RemoveAuditRule(self, rule: FileSystemAuditRule) -> bool:
        """"""
    def RemoveAuditRuleAll(self, rule: FileSystemAuditRule) -> None:
        """"""
    def RemoveAuditRuleSpecific(self, rule: FileSystemAuditRule) -> None:
        """"""
    def ResetAccessRule(self, rule: FileSystemAccessRule) -> None:
        """"""
    def SetAccessRule(self, rule: FileSystemAccessRule) -> None:
        """"""
    def SetAccessRuleProtection(self, isProtected: bool, preserveInheritance: bool) -> None:
        """"""
    def SetAuditRule(self, rule: FileSystemAuditRule) -> None:
        """"""
    def SetAuditRuleProtection(self, isProtected: bool, preserveInheritance: bool) -> None:
        """"""
    def SetGroup(self, identity: IdentityReference) -> None:
        """"""
    def SetOwner(self, identity: IdentityReference) -> None:
        """"""
    @overload
    def SetSecurityDescriptorBinaryForm(self, binaryForm: Array[int]) -> None:
        """"""
    @overload
    def SetSecurityDescriptorBinaryForm(
        self, binaryForm: Array[int], includeSections: AccessControlSections
    ) -> None:
        """"""
    @overload
    def SetSecurityDescriptorSddlForm(self, sddlForm: str) -> None:
        """"""
    @overload
    def SetSecurityDescriptorSddlForm(
        self, sddlForm: str, includeSections: AccessControlSections
    ) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class FileSystemAccessRule(AccessRule):
    """"""
    @overload
    def __init__(
        self,
        identity: IdentityReference,
        fileSystemRights: FileSystemRights,
        type: AccessControlType,
    ) -> None:
        """"""
    @overload
    def __init__(
        self, identity: str, fileSystemRights: FileSystemRights, type: AccessControlType
    ) -> None:
        """"""
    @overload
    def __init__(
        self,
        identity: IdentityReference,
        fileSystemRights: FileSystemRights,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
        type: AccessControlType,
    ) -> None:
        """"""
    @overload
    def __init__(
        self,
        identity: str,
        fileSystemRights: FileSystemRights,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
        type: AccessControlType,
    ) -> None:
        """"""
    @property
    def AccessControlType(self) -> AccessControlType:
        """"""
    @property
    def FileSystemRights(self) -> FileSystemRights:
        """"""
    @property
    def IdentityReference(self) -> IdentityReference:
        """"""
    @property
    def InheritanceFlags(self) -> InheritanceFlags:
        """"""
    @property
    def IsInherited(self) -> bool:
        """"""
    @property
    def PropagationFlags(self) -> PropagationFlags:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class FileSystemAuditRule(AuditRule):
    """"""
    @overload
    def __init__(
        self, identity: IdentityReference, fileSystemRights: FileSystemRights, flags: AuditFlags
    ) -> None:
        """"""
    @overload
    def __init__(
        self,
        identity: IdentityReference,
        fileSystemRights: FileSystemRights,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
        flags: AuditFlags,
    ) -> None:
        """"""
    @overload
    def __init__(
        self, identity: str, fileSystemRights: FileSystemRights, flags: AuditFlags
    ) -> None:
        """"""
    @overload
    def __init__(
        self,
        identity: str,
        fileSystemRights: FileSystemRights,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
        flags: AuditFlags,
    ) -> None:
        """"""
    @property
    def AuditFlags(self) -> AuditFlags:
        """"""
    @property
    def FileSystemRights(self) -> FileSystemRights:
        """"""
    @property
    def IdentityReference(self) -> IdentityReference:
        """"""
    @property
    def InheritanceFlags(self) -> InheritanceFlags:
        """"""
    @property
    def IsInherited(self) -> bool:
        """"""
    @property
    def PropagationFlags(self) -> PropagationFlags:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class FileSystemRights(Enum):
    """"""

    ListDirectory: FileSystemRights = ...
    """"""
    ReadData: FileSystemRights = ...
    """"""
    WriteData: FileSystemRights = ...
    """"""
    CreateFiles: FileSystemRights = ...
    """"""
    CreateDirectories: FileSystemRights = ...
    """"""
    AppendData: FileSystemRights = ...
    """"""
    ReadExtendedAttributes: FileSystemRights = ...
    """"""
    WriteExtendedAttributes: FileSystemRights = ...
    """"""
    Traverse: FileSystemRights = ...
    """"""
    ExecuteFile: FileSystemRights = ...
    """"""
    DeleteSubdirectoriesAndFiles: FileSystemRights = ...
    """"""
    ReadAttributes: FileSystemRights = ...
    """"""
    WriteAttributes: FileSystemRights = ...
    """"""
    Write: FileSystemRights = ...
    """"""
    Delete: FileSystemRights = ...
    """"""
    ReadPermissions: FileSystemRights = ...
    """"""
    Read: FileSystemRights = ...
    """"""
    ReadAndExecute: FileSystemRights = ...
    """"""
    Modify: FileSystemRights = ...
    """"""
    ChangePermissions: FileSystemRights = ...
    """"""
    TakeOwnership: FileSystemRights = ...
    """"""
    Synchronize: FileSystemRights = ...
    """"""
    FullControl: FileSystemRights = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class FileSystemSecurity(ABC, NativeObjectSecurity):
    """"""
    @property
    def AccessRightType(self) -> Type:
        """"""
    @property
    def AccessRuleType(self) -> Type:
        """"""
    @property
    def AreAccessRulesCanonical(self) -> bool:
        """"""
    @property
    def AreAccessRulesProtected(self) -> bool:
        """"""
    @property
    def AreAuditRulesCanonical(self) -> bool:
        """"""
    @property
    def AreAuditRulesProtected(self) -> bool:
        """"""
    @property
    def AuditRuleType(self) -> Type:
        """"""
    def AccessRuleFactory(
        self,
        identityReference: IdentityReference,
        accessMask: int,
        isInherited: bool,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
        type: AccessControlType,
    ) -> AccessRule:
        """"""
    def AddAccessRule(self, rule: FileSystemAccessRule) -> None:
        """"""
    def AddAuditRule(self, rule: FileSystemAuditRule) -> None:
        """"""
    def AuditRuleFactory(
        self,
        identityReference: IdentityReference,
        accessMask: int,
        isInherited: bool,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
        flags: AuditFlags,
    ) -> AuditRule:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetAccessRules(
        self, includeExplicit: bool, includeInherited: bool, targetType: Type
    ) -> AuthorizationRuleCollection:
        """"""
    def GetAuditRules(
        self, includeExplicit: bool, includeInherited: bool, targetType: Type
    ) -> AuthorizationRuleCollection:
        """"""
    def GetGroup(self, targetType: Type) -> IdentityReference:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetOwner(self, targetType: Type) -> IdentityReference:
        """"""
    def GetSecurityDescriptorBinaryForm(self) -> Array[int]:
        """"""
    def GetSecurityDescriptorSddlForm(self, includeSections: AccessControlSections) -> str:
        """"""
    def GetType(self) -> Type:
        """"""
    def ModifyAccessRule(
        self, modification: AccessControlModification, rule: AccessRule, modified: Boolean
    ) -> tuple[bool, Boolean]:
        """"""
    def ModifyAuditRule(
        self, modification: AccessControlModification, rule: AuditRule, modified: Boolean
    ) -> tuple[bool, Boolean]:
        """"""
    def PurgeAccessRules(self, identity: IdentityReference) -> None:
        """"""
    def PurgeAuditRules(self, identity: IdentityReference) -> None:
        """"""
    def RemoveAccessRule(self, rule: FileSystemAccessRule) -> bool:
        """"""
    def RemoveAccessRuleAll(self, rule: FileSystemAccessRule) -> None:
        """"""
    def RemoveAccessRuleSpecific(self, rule: FileSystemAccessRule) -> None:
        """"""
    def RemoveAuditRule(self, rule: FileSystemAuditRule) -> bool:
        """"""
    def RemoveAuditRuleAll(self, rule: FileSystemAuditRule) -> None:
        """"""
    def RemoveAuditRuleSpecific(self, rule: FileSystemAuditRule) -> None:
        """"""
    def ResetAccessRule(self, rule: FileSystemAccessRule) -> None:
        """"""
    def SetAccessRule(self, rule: FileSystemAccessRule) -> None:
        """"""
    def SetAccessRuleProtection(self, isProtected: bool, preserveInheritance: bool) -> None:
        """"""
    def SetAuditRule(self, rule: FileSystemAuditRule) -> None:
        """"""
    def SetAuditRuleProtection(self, isProtected: bool, preserveInheritance: bool) -> None:
        """"""
    def SetGroup(self, identity: IdentityReference) -> None:
        """"""
    def SetOwner(self, identity: IdentityReference) -> None:
        """"""
    @overload
    def SetSecurityDescriptorBinaryForm(self, binaryForm: Array[int]) -> None:
        """"""
    @overload
    def SetSecurityDescriptorBinaryForm(
        self, binaryForm: Array[int], includeSections: AccessControlSections
    ) -> None:
        """"""
    @overload
    def SetSecurityDescriptorSddlForm(self, sddlForm: str) -> None:
        """"""
    @overload
    def SetSecurityDescriptorSddlForm(
        self, sddlForm: str, includeSections: AccessControlSections
    ) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class GenericAce(ABC, Object):
    """"""
    @property
    def AceFlags(self) -> AceFlags:
        """"""
    @AceFlags.setter
    def AceFlags(self, value: AceFlags) -> None: ...
    @property
    def AceType(self) -> AceType:
        """"""
    @property
    def AuditFlags(self) -> AuditFlags:
        """"""
    @property
    def BinaryLength(self) -> int:
        """"""
    @property
    def InheritanceFlags(self) -> InheritanceFlags:
        """"""
    @property
    def IsInherited(self) -> bool:
        """"""
    @property
    def PropagationFlags(self) -> PropagationFlags:
        """"""
    def Copy(self) -> GenericAce:
        """"""
    @classmethod
    def CreateFromBinaryForm(cls, binaryForm: Array[int], offset: int) -> GenericAce:
        """"""
    def Equals(self, o: object) -> bool:
        """"""
    def GetBinaryForm(self, binaryForm: Array[int], offset: int) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def op_Equality(cls, left: GenericAce, right: GenericAce) -> bool:
        """"""
    @classmethod
    def op_Inequality(cls, left: GenericAce, right: GenericAce) -> bool:
        """"""
    def __eq__(self, other: GenericAce) -> bool:
        """"""
    def __ne__(self, other: GenericAce) -> bool:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class GenericAcl(ABC, Object, ICollection, IEnumerable):
    """"""

    AclRevision: ClassVar[int]
    """"""
    AclRevisionDS: ClassVar[int]
    """"""
    MaxBinaryLength: ClassVar[int]
    """"""
    @property
    def BinaryLength(self) -> int:
        """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def Item(self) -> GenericAce:
        """"""
    @Item.setter
    def Item(self, value: GenericAce) -> None: ...
    @property
    def Revision(self) -> int:
        """"""
    @property
    def SyncRoot(self) -> object:
        """"""
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array[GenericAce], index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetBinaryForm(self, binaryForm: Array[int], offset: int) -> None:
        """"""
    def GetEnumerator(self) -> AceEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, index: int) -> GenericAce:
        """"""
    def __setitem__(self, index: int, value: GenericAce) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class GenericSecurityDescriptor(ABC, Object):
    """"""
    @property
    def BinaryLength(self) -> int:
        """"""
    @property
    def ControlFlags(self) -> ControlFlags:
        """"""
    @property
    def Group(self) -> SecurityIdentifier:
        """"""
    @Group.setter
    def Group(self, value: SecurityIdentifier) -> None: ...
    @property
    def Owner(self) -> SecurityIdentifier:
        """"""
    @Owner.setter
    def Owner(self, value: SecurityIdentifier) -> None: ...
    @classmethod
    @property
    def Revision(cls) -> int:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetBinaryForm(self, binaryForm: Array[int], offset: int) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetSddlForm(self, includeSections: AccessControlSections) -> str:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def IsSddlConversionSupported(cls) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class InheritanceFlags(Enum):
    """"""

    _None: InheritanceFlags = ...
    """"""
    ContainerInherit: InheritanceFlags = ...
    """"""
    ObjectInherit: InheritanceFlags = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class KnownAce(ABC, GenericAce):
    """"""
    @property
    def AccessMask(self) -> int:
        """"""
    @AccessMask.setter
    def AccessMask(self, value: int) -> None: ...
    @property
    def AceFlags(self) -> AceFlags:
        """"""
    @AceFlags.setter
    def AceFlags(self, value: AceFlags) -> None: ...
    @property
    def AceType(self) -> AceType:
        """"""
    @property
    def AuditFlags(self) -> AuditFlags:
        """"""
    @property
    def BinaryLength(self) -> int:
        """"""
    @property
    def InheritanceFlags(self) -> InheritanceFlags:
        """"""
    @property
    def IsInherited(self) -> bool:
        """"""
    @property
    def PropagationFlags(self) -> PropagationFlags:
        """"""
    @property
    def SecurityIdentifier(self) -> SecurityIdentifier:
        """"""
    @SecurityIdentifier.setter
    def SecurityIdentifier(self, value: SecurityIdentifier) -> None: ...
    def Copy(self) -> GenericAce:
        """"""
    def Equals(self, o: object) -> bool:
        """"""
    def GetBinaryForm(self, binaryForm: Array[int], offset: int) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class MutexAccessRule(AccessRule):
    """"""
    @overload
    def __init__(
        self, identity: IdentityReference, eventRights: MutexRights, type: AccessControlType
    ) -> None:
        """"""
    @overload
    def __init__(self, identity: str, eventRights: MutexRights, type: AccessControlType) -> None:
        """"""
    @property
    def AccessControlType(self) -> AccessControlType:
        """"""
    @property
    def IdentityReference(self) -> IdentityReference:
        """"""
    @property
    def InheritanceFlags(self) -> InheritanceFlags:
        """"""
    @property
    def IsInherited(self) -> bool:
        """"""
    @property
    def MutexRights(self) -> MutexRights:
        """"""
    @property
    def PropagationFlags(self) -> PropagationFlags:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class MutexAuditRule(AuditRule):
    """"""
    def __init__(
        self, identity: IdentityReference, eventRights: MutexRights, flags: AuditFlags
    ) -> None:
        """"""
    @property
    def AuditFlags(self) -> AuditFlags:
        """"""
    @property
    def IdentityReference(self) -> IdentityReference:
        """"""
    @property
    def InheritanceFlags(self) -> InheritanceFlags:
        """"""
    @property
    def IsInherited(self) -> bool:
        """"""
    @property
    def MutexRights(self) -> MutexRights:
        """"""
    @property
    def PropagationFlags(self) -> PropagationFlags:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class MutexRights(Enum):
    """"""

    Modify: MutexRights = ...
    """"""
    Delete: MutexRights = ...
    """"""
    ReadPermissions: MutexRights = ...
    """"""
    ChangePermissions: MutexRights = ...
    """"""
    TakeOwnership: MutexRights = ...
    """"""
    Synchronize: MutexRights = ...
    """"""
    FullControl: MutexRights = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class MutexSecurity(NativeObjectSecurity):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, name: str, includeSections: AccessControlSections) -> None:
        """"""
    @property
    def AccessRightType(self) -> Type:
        """"""
    @property
    def AccessRuleType(self) -> Type:
        """"""
    @property
    def AreAccessRulesCanonical(self) -> bool:
        """"""
    @property
    def AreAccessRulesProtected(self) -> bool:
        """"""
    @property
    def AreAuditRulesCanonical(self) -> bool:
        """"""
    @property
    def AreAuditRulesProtected(self) -> bool:
        """"""
    @property
    def AuditRuleType(self) -> Type:
        """"""
    def AccessRuleFactory(
        self,
        identityReference: IdentityReference,
        accessMask: int,
        isInherited: bool,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
        type: AccessControlType,
    ) -> AccessRule:
        """"""
    def AddAccessRule(self, rule: MutexAccessRule) -> None:
        """"""
    def AddAuditRule(self, rule: MutexAuditRule) -> None:
        """"""
    def AuditRuleFactory(
        self,
        identityReference: IdentityReference,
        accessMask: int,
        isInherited: bool,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
        flags: AuditFlags,
    ) -> AuditRule:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetAccessRules(
        self, includeExplicit: bool, includeInherited: bool, targetType: Type
    ) -> AuthorizationRuleCollection:
        """"""
    def GetAuditRules(
        self, includeExplicit: bool, includeInherited: bool, targetType: Type
    ) -> AuthorizationRuleCollection:
        """"""
    def GetGroup(self, targetType: Type) -> IdentityReference:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetOwner(self, targetType: Type) -> IdentityReference:
        """"""
    def GetSecurityDescriptorBinaryForm(self) -> Array[int]:
        """"""
    def GetSecurityDescriptorSddlForm(self, includeSections: AccessControlSections) -> str:
        """"""
    def GetType(self) -> Type:
        """"""
    def ModifyAccessRule(
        self, modification: AccessControlModification, rule: AccessRule, modified: Boolean
    ) -> tuple[bool, Boolean]:
        """"""
    def ModifyAuditRule(
        self, modification: AccessControlModification, rule: AuditRule, modified: Boolean
    ) -> tuple[bool, Boolean]:
        """"""
    def PurgeAccessRules(self, identity: IdentityReference) -> None:
        """"""
    def PurgeAuditRules(self, identity: IdentityReference) -> None:
        """"""
    def RemoveAccessRule(self, rule: MutexAccessRule) -> bool:
        """"""
    def RemoveAccessRuleAll(self, rule: MutexAccessRule) -> None:
        """"""
    def RemoveAccessRuleSpecific(self, rule: MutexAccessRule) -> None:
        """"""
    def RemoveAuditRule(self, rule: MutexAuditRule) -> bool:
        """"""
    def RemoveAuditRuleAll(self, rule: MutexAuditRule) -> None:
        """"""
    def RemoveAuditRuleSpecific(self, rule: MutexAuditRule) -> None:
        """"""
    def ResetAccessRule(self, rule: MutexAccessRule) -> None:
        """"""
    def SetAccessRule(self, rule: MutexAccessRule) -> None:
        """"""
    def SetAccessRuleProtection(self, isProtected: bool, preserveInheritance: bool) -> None:
        """"""
    def SetAuditRule(self, rule: MutexAuditRule) -> None:
        """"""
    def SetAuditRuleProtection(self, isProtected: bool, preserveInheritance: bool) -> None:
        """"""
    def SetGroup(self, identity: IdentityReference) -> None:
        """"""
    def SetOwner(self, identity: IdentityReference) -> None:
        """"""
    @overload
    def SetSecurityDescriptorBinaryForm(self, binaryForm: Array[int]) -> None:
        """"""
    @overload
    def SetSecurityDescriptorBinaryForm(
        self, binaryForm: Array[int], includeSections: AccessControlSections
    ) -> None:
        """"""
    @overload
    def SetSecurityDescriptorSddlForm(self, sddlForm: str) -> None:
        """"""
    @overload
    def SetSecurityDescriptorSddlForm(
        self, sddlForm: str, includeSections: AccessControlSections
    ) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class NativeObjectSecurity(ABC, CommonObjectSecurity):
    """"""
    @property
    def AccessRightType(self) -> Type:
        """"""
    @property
    def AccessRuleType(self) -> Type:
        """"""
    @property
    def AreAccessRulesCanonical(self) -> bool:
        """"""
    @property
    def AreAccessRulesProtected(self) -> bool:
        """"""
    @property
    def AreAuditRulesCanonical(self) -> bool:
        """"""
    @property
    def AreAuditRulesProtected(self) -> bool:
        """"""
    @property
    def AuditRuleType(self) -> Type:
        """"""
    def AccessRuleFactory(
        self,
        identityReference: IdentityReference,
        accessMask: int,
        isInherited: bool,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
        type: AccessControlType,
    ) -> AccessRule:
        """"""
    def AuditRuleFactory(
        self,
        identityReference: IdentityReference,
        accessMask: int,
        isInherited: bool,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
        flags: AuditFlags,
    ) -> AuditRule:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetAccessRules(
        self, includeExplicit: bool, includeInherited: bool, targetType: Type
    ) -> AuthorizationRuleCollection:
        """"""
    def GetAuditRules(
        self, includeExplicit: bool, includeInherited: bool, targetType: Type
    ) -> AuthorizationRuleCollection:
        """"""
    def GetGroup(self, targetType: Type) -> IdentityReference:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetOwner(self, targetType: Type) -> IdentityReference:
        """"""
    def GetSecurityDescriptorBinaryForm(self) -> Array[int]:
        """"""
    def GetSecurityDescriptorSddlForm(self, includeSections: AccessControlSections) -> str:
        """"""
    def GetType(self) -> Type:
        """"""
    def ModifyAccessRule(
        self, modification: AccessControlModification, rule: AccessRule, modified: Boolean
    ) -> tuple[bool, Boolean]:
        """"""
    def ModifyAuditRule(
        self, modification: AccessControlModification, rule: AuditRule, modified: Boolean
    ) -> tuple[bool, Boolean]:
        """"""
    def PurgeAccessRules(self, identity: IdentityReference) -> None:
        """"""
    def PurgeAuditRules(self, identity: IdentityReference) -> None:
        """"""
    def SetAccessRuleProtection(self, isProtected: bool, preserveInheritance: bool) -> None:
        """"""
    def SetAuditRuleProtection(self, isProtected: bool, preserveInheritance: bool) -> None:
        """"""
    def SetGroup(self, identity: IdentityReference) -> None:
        """"""
    def SetOwner(self, identity: IdentityReference) -> None:
        """"""
    @overload
    def SetSecurityDescriptorBinaryForm(self, binaryForm: Array[int]) -> None:
        """"""
    @overload
    def SetSecurityDescriptorBinaryForm(
        self, binaryForm: Array[int], includeSections: AccessControlSections
    ) -> None:
        """"""
    @overload
    def SetSecurityDescriptorSddlForm(self, sddlForm: str) -> None:
        """"""
    @overload
    def SetSecurityDescriptorSddlForm(
        self, sddlForm: str, includeSections: AccessControlSections
    ) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ObjectAccessRule(ABC, AccessRule):
    """"""
    @property
    def AccessControlType(self) -> AccessControlType:
        """"""
    @property
    def IdentityReference(self) -> IdentityReference:
        """"""
    @property
    def InheritanceFlags(self) -> InheritanceFlags:
        """"""
    @property
    def InheritedObjectType(self) -> Guid:
        """"""
    @property
    def IsInherited(self) -> bool:
        """"""
    @property
    def ObjectFlags(self) -> ObjectAceFlags:
        """"""
    @property
    def ObjectType(self) -> Guid:
        """"""
    @property
    def PropagationFlags(self) -> PropagationFlags:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ObjectAce(QualifiedAce):
    """"""
    def __init__(
        self,
        aceFlags: AceFlags,
        qualifier: AceQualifier,
        accessMask: int,
        sid: SecurityIdentifier,
        flags: ObjectAceFlags,
        type: Guid,
        inheritedType: Guid,
        isCallback: bool,
        opaque: Array[int],
    ) -> None:
        """"""
    @property
    def AccessMask(self) -> int:
        """"""
    @AccessMask.setter
    def AccessMask(self, value: int) -> None: ...
    @property
    def AceFlags(self) -> AceFlags:
        """"""
    @AceFlags.setter
    def AceFlags(self, value: AceFlags) -> None: ...
    @property
    def AceQualifier(self) -> AceQualifier:
        """"""
    @property
    def AceType(self) -> AceType:
        """"""
    @property
    def AuditFlags(self) -> AuditFlags:
        """"""
    @property
    def BinaryLength(self) -> int:
        """"""
    @property
    def InheritanceFlags(self) -> InheritanceFlags:
        """"""
    @property
    def InheritedObjectAceType(self) -> Guid:
        """"""
    @InheritedObjectAceType.setter
    def InheritedObjectAceType(self, value: Guid) -> None: ...
    @property
    def IsCallback(self) -> bool:
        """"""
    @property
    def IsInherited(self) -> bool:
        """"""
    @property
    def ObjectAceFlags(self) -> ObjectAceFlags:
        """"""
    @ObjectAceFlags.setter
    def ObjectAceFlags(self, value: ObjectAceFlags) -> None: ...
    @property
    def ObjectAceType(self) -> Guid:
        """"""
    @ObjectAceType.setter
    def ObjectAceType(self, value: Guid) -> None: ...
    @property
    def OpaqueLength(self) -> int:
        """"""
    @property
    def PropagationFlags(self) -> PropagationFlags:
        """"""
    @property
    def SecurityIdentifier(self) -> SecurityIdentifier:
        """"""
    @SecurityIdentifier.setter
    def SecurityIdentifier(self, value: SecurityIdentifier) -> None: ...
    def Copy(self) -> GenericAce:
        """"""
    def Equals(self, o: object) -> bool:
        """"""
    def GetBinaryForm(self, binaryForm: Array[int], offset: int) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetOpaque(self) -> Array[int]:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def MaxOpaqueLength(cls, isCallback: bool) -> int:
        """"""
    def SetOpaque(self, opaque: Array[int]) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class ObjectAceFlags(Enum):
    """"""

    _None: ObjectAceFlags = ...
    """"""
    ObjectAceTypePresent: ObjectAceFlags = ...
    """"""
    InheritedObjectAceTypePresent: ObjectAceFlags = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ObjectAuditRule(ABC, AuditRule):
    """"""
    @property
    def AuditFlags(self) -> AuditFlags:
        """"""
    @property
    def IdentityReference(self) -> IdentityReference:
        """"""
    @property
    def InheritanceFlags(self) -> InheritanceFlags:
        """"""
    @property
    def InheritedObjectType(self) -> Guid:
        """"""
    @property
    def IsInherited(self) -> bool:
        """"""
    @property
    def ObjectFlags(self) -> ObjectAceFlags:
        """"""
    @property
    def ObjectType(self) -> Guid:
        """"""
    @property
    def PropagationFlags(self) -> PropagationFlags:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ObjectSecurity(ABC, Object):
    """"""
    @property
    def AccessRightType(self) -> Type:
        """"""
    @property
    def AccessRuleType(self) -> Type:
        """"""
    @property
    def AreAccessRulesCanonical(self) -> bool:
        """"""
    @property
    def AreAccessRulesProtected(self) -> bool:
        """"""
    @property
    def AreAuditRulesCanonical(self) -> bool:
        """"""
    @property
    def AreAuditRulesProtected(self) -> bool:
        """"""
    @property
    def AuditRuleType(self) -> Type:
        """"""
    def AccessRuleFactory(
        self,
        identityReference: IdentityReference,
        accessMask: int,
        isInherited: bool,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
        type: AccessControlType,
    ) -> AccessRule:
        """"""
    def AuditRuleFactory(
        self,
        identityReference: IdentityReference,
        accessMask: int,
        isInherited: bool,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
        flags: AuditFlags,
    ) -> AuditRule:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetGroup(self, targetType: Type) -> IdentityReference:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetOwner(self, targetType: Type) -> IdentityReference:
        """"""
    def GetSecurityDescriptorBinaryForm(self) -> Array[int]:
        """"""
    def GetSecurityDescriptorSddlForm(self, includeSections: AccessControlSections) -> str:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def IsSddlConversionSupported(cls) -> bool:
        """"""
    def ModifyAccessRule(
        self, modification: AccessControlModification, rule: AccessRule, modified: Boolean
    ) -> tuple[bool, Boolean]:
        """"""
    def ModifyAuditRule(
        self, modification: AccessControlModification, rule: AuditRule, modified: Boolean
    ) -> tuple[bool, Boolean]:
        """"""
    def PurgeAccessRules(self, identity: IdentityReference) -> None:
        """"""
    def PurgeAuditRules(self, identity: IdentityReference) -> None:
        """"""
    def SetAccessRuleProtection(self, isProtected: bool, preserveInheritance: bool) -> None:
        """"""
    def SetAuditRuleProtection(self, isProtected: bool, preserveInheritance: bool) -> None:
        """"""
    def SetGroup(self, identity: IdentityReference) -> None:
        """"""
    def SetOwner(self, identity: IdentityReference) -> None:
        """"""
    @overload
    def SetSecurityDescriptorBinaryForm(self, binaryForm: Array[int]) -> None:
        """"""
    @overload
    def SetSecurityDescriptorBinaryForm(
        self, binaryForm: Array[int], includeSections: AccessControlSections
    ) -> None:
        """"""
    @overload
    def SetSecurityDescriptorSddlForm(self, sddlForm: str) -> None:
        """"""
    @overload
    def SetSecurityDescriptorSddlForm(
        self, sddlForm: str, includeSections: AccessControlSections
    ) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ObjectSecurity[T](ABC, NativeObjectSecurity):
    """"""
    @property
    def AccessRightType(self) -> Type:
        """"""
    @property
    def AccessRuleType(self) -> Type:
        """"""
    @property
    def AreAccessRulesCanonical(self) -> bool:
        """"""
    @property
    def AreAccessRulesProtected(self) -> bool:
        """"""
    @property
    def AreAuditRulesCanonical(self) -> bool:
        """"""
    @property
    def AreAuditRulesProtected(self) -> bool:
        """"""
    @property
    def AuditRuleType(self) -> Type:
        """"""
    def AccessRuleFactory(
        self,
        identityReference: IdentityReference,
        accessMask: int,
        isInherited: bool,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
        type: AccessControlType,
    ) -> AccessRule:
        """"""
    def AddAccessRule(self, rule: AccessRule[T]) -> None:
        """"""
    def AddAuditRule(self, rule: AuditRule[T]) -> None:
        """"""
    def AuditRuleFactory(
        self,
        identityReference: IdentityReference,
        accessMask: int,
        isInherited: bool,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
        flags: AuditFlags,
    ) -> AuditRule:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetAccessRules(
        self, includeExplicit: bool, includeInherited: bool, targetType: Type
    ) -> AuthorizationRuleCollection:
        """"""
    def GetAuditRules(
        self, includeExplicit: bool, includeInherited: bool, targetType: Type
    ) -> AuthorizationRuleCollection:
        """"""
    def GetGroup(self, targetType: Type) -> IdentityReference:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetOwner(self, targetType: Type) -> IdentityReference:
        """"""
    def GetSecurityDescriptorBinaryForm(self) -> Array[int]:
        """"""
    def GetSecurityDescriptorSddlForm(self, includeSections: AccessControlSections) -> str:
        """"""
    def GetType(self) -> Type:
        """"""
    def ModifyAccessRule(
        self, modification: AccessControlModification, rule: AccessRule, modified: Boolean
    ) -> tuple[bool, Boolean]:
        """"""
    def ModifyAuditRule(
        self, modification: AccessControlModification, rule: AuditRule, modified: Boolean
    ) -> tuple[bool, Boolean]:
        """"""
    def PurgeAccessRules(self, identity: IdentityReference) -> None:
        """"""
    def PurgeAuditRules(self, identity: IdentityReference) -> None:
        """"""
    def RemoveAccessRule(self, rule: AccessRule[T]) -> bool:
        """"""
    def RemoveAccessRuleAll(self, rule: AccessRule[T]) -> None:
        """"""
    def RemoveAccessRuleSpecific(self, rule: AccessRule[T]) -> None:
        """"""
    def RemoveAuditRule(self, rule: AuditRule[T]) -> bool:
        """"""
    def RemoveAuditRuleAll(self, rule: AuditRule[T]) -> None:
        """"""
    def RemoveAuditRuleSpecific(self, rule: AuditRule[T]) -> None:
        """"""
    def ResetAccessRule(self, rule: AccessRule[T]) -> None:
        """"""
    def SetAccessRule(self, rule: AccessRule[T]) -> None:
        """"""
    def SetAccessRuleProtection(self, isProtected: bool, preserveInheritance: bool) -> None:
        """"""
    def SetAuditRule(self, rule: AuditRule[T]) -> None:
        """"""
    def SetAuditRuleProtection(self, isProtected: bool, preserveInheritance: bool) -> None:
        """"""
    def SetGroup(self, identity: IdentityReference) -> None:
        """"""
    def SetOwner(self, identity: IdentityReference) -> None:
        """"""
    @overload
    def SetSecurityDescriptorBinaryForm(self, binaryForm: Array[int]) -> None:
        """"""
    @overload
    def SetSecurityDescriptorBinaryForm(
        self, binaryForm: Array[int], includeSections: AccessControlSections
    ) -> None:
        """"""
    @overload
    def SetSecurityDescriptorSddlForm(self, sddlForm: str) -> None:
        """"""
    @overload
    def SetSecurityDescriptorSddlForm(
        self, sddlForm: str, includeSections: AccessControlSections
    ) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class Privilege(Object):
    """"""

    AssignPrimaryToken: ClassVar[str]
    """"""
    Audit: ClassVar[str]
    """"""
    Backup: ClassVar[str]
    """"""
    ChangeNotify: ClassVar[str]
    """"""
    CreateGlobal: ClassVar[str]
    """"""
    CreatePageFile: ClassVar[str]
    """"""
    CreatePermanent: ClassVar[str]
    """"""
    CreateToken: ClassVar[str]
    """"""
    Debug: ClassVar[str]
    """"""
    EnableDelegation: ClassVar[str]
    """"""
    Impersonate: ClassVar[str]
    """"""
    IncreaseBasePriority: ClassVar[str]
    """"""
    IncreaseQuota: ClassVar[str]
    """"""
    LoadDriver: ClassVar[str]
    """"""
    LockMemory: ClassVar[str]
    """"""
    MachineAccount: ClassVar[str]
    """"""
    ManageVolume: ClassVar[str]
    """"""
    ProfileSingleProcess: ClassVar[str]
    """"""
    RemoteShutdown: ClassVar[str]
    """"""
    ReserveProcessor: ClassVar[str]
    """"""
    Restore: ClassVar[str]
    """"""
    Security: ClassVar[str]
    """"""
    Shutdown: ClassVar[str]
    """"""
    SyncAgent: ClassVar[str]
    """"""
    SystemEnvironment: ClassVar[str]
    """"""
    SystemProfile: ClassVar[str]
    """"""
    SystemTime: ClassVar[str]
    """"""
    TakeOwnership: ClassVar[str]
    """"""
    TrustedComputingBase: ClassVar[str]
    """"""
    TrustedCredentialManagerAccess: ClassVar[str]
    """"""
    Undock: ClassVar[str]
    """"""
    UnsolicitedInput: ClassVar[str]
    """"""
    def __init__(self, privilegeName: str) -> None:
        """"""
    @property
    def NeedToRevert(self) -> bool:
        """"""
    def Enable(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Revert(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class PrivilegeNotHeldException(UnauthorizedAccessException, _Exception, ISerializable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, privilege: str) -> None:
        """"""
    @overload
    def __init__(self, privilege: str, inner: Exception) -> None:
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
    def PrivilegeName(self) -> str:
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
    def Equals(self, obj: object) -> bool:
        """"""
    def GetBaseException(self) -> Exception:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class PropagationFlags(Enum):
    """"""

    _None: PropagationFlags = ...
    """"""
    NoPropagateInherit: PropagationFlags = ...
    """"""
    InheritOnly: PropagationFlags = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class QualifiedAce(ABC, KnownAce):
    """"""
    @property
    def AccessMask(self) -> int:
        """"""
    @AccessMask.setter
    def AccessMask(self, value: int) -> None: ...
    @property
    def AceFlags(self) -> AceFlags:
        """"""
    @AceFlags.setter
    def AceFlags(self, value: AceFlags) -> None: ...
    @property
    def AceQualifier(self) -> AceQualifier:
        """"""
    @property
    def AceType(self) -> AceType:
        """"""
    @property
    def AuditFlags(self) -> AuditFlags:
        """"""
    @property
    def BinaryLength(self) -> int:
        """"""
    @property
    def InheritanceFlags(self) -> InheritanceFlags:
        """"""
    @property
    def IsCallback(self) -> bool:
        """"""
    @property
    def IsInherited(self) -> bool:
        """"""
    @property
    def OpaqueLength(self) -> int:
        """"""
    @property
    def PropagationFlags(self) -> PropagationFlags:
        """"""
    @property
    def SecurityIdentifier(self) -> SecurityIdentifier:
        """"""
    @SecurityIdentifier.setter
    def SecurityIdentifier(self, value: SecurityIdentifier) -> None: ...
    def Copy(self) -> GenericAce:
        """"""
    def Equals(self, o: object) -> bool:
        """"""
    def GetBinaryForm(self, binaryForm: Array[int], offset: int) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetOpaque(self) -> Array[int]:
        """"""
    def GetType(self) -> Type:
        """"""
    def SetOpaque(self, opaque: Array[int]) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class RawAcl(GenericAcl, ICollection, IEnumerable):
    """"""
    @overload
    def __init__(self, revision: int, capacity: int) -> None:
        """"""
    @overload
    def __init__(self, binaryForm: Array[int], offset: int) -> None:
        """"""
    @property
    def BinaryLength(self) -> int:
        """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def Item(self) -> GenericAce:
        """"""
    @Item.setter
    def Item(self, value: GenericAce) -> None: ...
    @property
    def Revision(self) -> int:
        """"""
    @property
    def SyncRoot(self) -> object:
        """"""
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array[GenericAce], index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetBinaryForm(self, binaryForm: Array[int], offset: int) -> None:
        """"""
    def GetEnumerator(self) -> AceEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def InsertAce(self, index: int, ace: GenericAce) -> None:
        """"""
    def RemoveAce(self, index: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, index: int) -> GenericAce:
        """"""
    def __setitem__(self, index: int, value: GenericAce) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class RawSecurityDescriptor(GenericSecurityDescriptor):
    """"""
    @overload
    def __init__(
        self,
        flags: ControlFlags,
        owner: SecurityIdentifier,
        group: SecurityIdentifier,
        systemAcl: RawAcl,
        discretionaryAcl: RawAcl,
    ) -> None:
        """"""
    @overload
    def __init__(self, sddlForm: str) -> None:
        """"""
    @overload
    def __init__(self, binaryForm: Array[int], offset: int) -> None:
        """"""
    @property
    def BinaryLength(self) -> int:
        """"""
    @property
    def ControlFlags(self) -> ControlFlags:
        """"""
    @property
    def DiscretionaryAcl(self) -> RawAcl:
        """"""
    @DiscretionaryAcl.setter
    def DiscretionaryAcl(self, value: RawAcl) -> None: ...
    @property
    def Group(self) -> SecurityIdentifier:
        """"""
    @Group.setter
    def Group(self, value: SecurityIdentifier) -> None: ...
    @property
    def Owner(self) -> SecurityIdentifier:
        """"""
    @Owner.setter
    def Owner(self, value: SecurityIdentifier) -> None: ...
    @property
    def ResourceManagerControl(self) -> int:
        """"""
    @ResourceManagerControl.setter
    def ResourceManagerControl(self, value: int) -> None: ...
    @property
    def SystemAcl(self) -> RawAcl:
        """"""
    @SystemAcl.setter
    def SystemAcl(self, value: RawAcl) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetBinaryForm(self, binaryForm: Array[int], offset: int) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetSddlForm(self, includeSections: AccessControlSections) -> str:
        """"""
    def GetType(self) -> Type:
        """"""
    def SetFlags(self, flags: ControlFlags) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class RegistryAccessRule(AccessRule):
    """"""
    @overload
    def __init__(
        self, identity: IdentityReference, registryRights: RegistryRights, type: AccessControlType
    ) -> None:
        """"""
    @overload
    def __init__(
        self, identity: str, registryRights: RegistryRights, type: AccessControlType
    ) -> None:
        """"""
    @overload
    def __init__(
        self,
        identity: IdentityReference,
        registryRights: RegistryRights,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
        type: AccessControlType,
    ) -> None:
        """"""
    @overload
    def __init__(
        self,
        identity: str,
        registryRights: RegistryRights,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
        type: AccessControlType,
    ) -> None:
        """"""
    @property
    def AccessControlType(self) -> AccessControlType:
        """"""
    @property
    def IdentityReference(self) -> IdentityReference:
        """"""
    @property
    def InheritanceFlags(self) -> InheritanceFlags:
        """"""
    @property
    def IsInherited(self) -> bool:
        """"""
    @property
    def PropagationFlags(self) -> PropagationFlags:
        """"""
    @property
    def RegistryRights(self) -> RegistryRights:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class RegistryAuditRule(AuditRule):
    """"""
    @overload
    def __init__(
        self,
        identity: IdentityReference,
        registryRights: RegistryRights,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
        flags: AuditFlags,
    ) -> None:
        """"""
    @overload
    def __init__(
        self,
        identity: str,
        registryRights: RegistryRights,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
        flags: AuditFlags,
    ) -> None:
        """"""
    @property
    def AuditFlags(self) -> AuditFlags:
        """"""
    @property
    def IdentityReference(self) -> IdentityReference:
        """"""
    @property
    def InheritanceFlags(self) -> InheritanceFlags:
        """"""
    @property
    def IsInherited(self) -> bool:
        """"""
    @property
    def PropagationFlags(self) -> PropagationFlags:
        """"""
    @property
    def RegistryRights(self) -> RegistryRights:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class RegistryRights(Enum):
    """"""

    QueryValues: RegistryRights = ...
    """"""
    SetValue: RegistryRights = ...
    """"""
    CreateSubKey: RegistryRights = ...
    """"""
    EnumerateSubKeys: RegistryRights = ...
    """"""
    Notify: RegistryRights = ...
    """"""
    CreateLink: RegistryRights = ...
    """"""
    Delete: RegistryRights = ...
    """"""
    ReadPermissions: RegistryRights = ...
    """"""
    WriteKey: RegistryRights = ...
    """"""
    ExecuteKey: RegistryRights = ...
    """"""
    ReadKey: RegistryRights = ...
    """"""
    ChangePermissions: RegistryRights = ...
    """"""
    TakeOwnership: RegistryRights = ...
    """"""
    FullControl: RegistryRights = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class RegistrySecurity(NativeObjectSecurity):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def AccessRightType(self) -> Type:
        """"""
    @property
    def AccessRuleType(self) -> Type:
        """"""
    @property
    def AreAccessRulesCanonical(self) -> bool:
        """"""
    @property
    def AreAccessRulesProtected(self) -> bool:
        """"""
    @property
    def AreAuditRulesCanonical(self) -> bool:
        """"""
    @property
    def AreAuditRulesProtected(self) -> bool:
        """"""
    @property
    def AuditRuleType(self) -> Type:
        """"""
    def AccessRuleFactory(
        self,
        identityReference: IdentityReference,
        accessMask: int,
        isInherited: bool,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
        type: AccessControlType,
    ) -> AccessRule:
        """"""
    def AddAccessRule(self, rule: RegistryAccessRule) -> None:
        """"""
    def AddAuditRule(self, rule: RegistryAuditRule) -> None:
        """"""
    def AuditRuleFactory(
        self,
        identityReference: IdentityReference,
        accessMask: int,
        isInherited: bool,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
        flags: AuditFlags,
    ) -> AuditRule:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetAccessRules(
        self, includeExplicit: bool, includeInherited: bool, targetType: Type
    ) -> AuthorizationRuleCollection:
        """"""
    def GetAuditRules(
        self, includeExplicit: bool, includeInherited: bool, targetType: Type
    ) -> AuthorizationRuleCollection:
        """"""
    def GetGroup(self, targetType: Type) -> IdentityReference:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetOwner(self, targetType: Type) -> IdentityReference:
        """"""
    def GetSecurityDescriptorBinaryForm(self) -> Array[int]:
        """"""
    def GetSecurityDescriptorSddlForm(self, includeSections: AccessControlSections) -> str:
        """"""
    def GetType(self) -> Type:
        """"""
    def ModifyAccessRule(
        self, modification: AccessControlModification, rule: AccessRule, modified: Boolean
    ) -> tuple[bool, Boolean]:
        """"""
    def ModifyAuditRule(
        self, modification: AccessControlModification, rule: AuditRule, modified: Boolean
    ) -> tuple[bool, Boolean]:
        """"""
    def PurgeAccessRules(self, identity: IdentityReference) -> None:
        """"""
    def PurgeAuditRules(self, identity: IdentityReference) -> None:
        """"""
    def RemoveAccessRule(self, rule: RegistryAccessRule) -> bool:
        """"""
    def RemoveAccessRuleAll(self, rule: RegistryAccessRule) -> None:
        """"""
    def RemoveAccessRuleSpecific(self, rule: RegistryAccessRule) -> None:
        """"""
    def RemoveAuditRule(self, rule: RegistryAuditRule) -> bool:
        """"""
    def RemoveAuditRuleAll(self, rule: RegistryAuditRule) -> None:
        """"""
    def RemoveAuditRuleSpecific(self, rule: RegistryAuditRule) -> None:
        """"""
    def ResetAccessRule(self, rule: RegistryAccessRule) -> None:
        """"""
    def SetAccessRule(self, rule: RegistryAccessRule) -> None:
        """"""
    def SetAccessRuleProtection(self, isProtected: bool, preserveInheritance: bool) -> None:
        """"""
    def SetAuditRule(self, rule: RegistryAuditRule) -> None:
        """"""
    def SetAuditRuleProtection(self, isProtected: bool, preserveInheritance: bool) -> None:
        """"""
    def SetGroup(self, identity: IdentityReference) -> None:
        """"""
    def SetOwner(self, identity: IdentityReference) -> None:
        """"""
    @overload
    def SetSecurityDescriptorBinaryForm(self, binaryForm: Array[int]) -> None:
        """"""
    @overload
    def SetSecurityDescriptorBinaryForm(
        self, binaryForm: Array[int], includeSections: AccessControlSections
    ) -> None:
        """"""
    @overload
    def SetSecurityDescriptorSddlForm(self, sddlForm: str) -> None:
        """"""
    @overload
    def SetSecurityDescriptorSddlForm(
        self, sddlForm: str, includeSections: AccessControlSections
    ) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class ResourceType(Enum):
    """"""

    Unknown: ResourceType = ...
    """"""
    FileObject: ResourceType = ...
    """"""
    Service: ResourceType = ...
    """"""
    Printer: ResourceType = ...
    """"""
    RegistryKey: ResourceType = ...
    """"""
    LMShare: ResourceType = ...
    """"""
    KernelObject: ResourceType = ...
    """"""
    WindowObject: ResourceType = ...
    """"""
    DSObject: ResourceType = ...
    """"""
    DSObjectAll: ResourceType = ...
    """"""
    ProviderDefined: ResourceType = ...
    """"""
    WmiGuidObject: ResourceType = ...
    """"""
    RegistryWow6432Key: ResourceType = ...
    """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class SecurityInfos(Enum):
    """"""

    Owner: SecurityInfos = ...
    """"""
    Group: SecurityInfos = ...
    """"""
    DiscretionaryAcl: SecurityInfos = ...
    """"""
    SystemAcl: SecurityInfos = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SemaphoreAccessRule(AccessRule):
    """"""
    @overload
    def __init__(
        self, identity: IdentityReference, eventRights: SemaphoreRights, type: AccessControlType
    ) -> None:
        """"""
    @overload
    def __init__(
        self, identity: str, eventRights: SemaphoreRights, type: AccessControlType
    ) -> None:
        """"""
    @property
    def AccessControlType(self) -> AccessControlType:
        """"""
    @property
    def IdentityReference(self) -> IdentityReference:
        """"""
    @property
    def InheritanceFlags(self) -> InheritanceFlags:
        """"""
    @property
    def IsInherited(self) -> bool:
        """"""
    @property
    def PropagationFlags(self) -> PropagationFlags:
        """"""
    @property
    def SemaphoreRights(self) -> SemaphoreRights:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SemaphoreAuditRule(AuditRule):
    """"""
    def __init__(
        self, identity: IdentityReference, eventRights: SemaphoreRights, flags: AuditFlags
    ) -> None:
        """"""
    @property
    def AuditFlags(self) -> AuditFlags:
        """"""
    @property
    def IdentityReference(self) -> IdentityReference:
        """"""
    @property
    def InheritanceFlags(self) -> InheritanceFlags:
        """"""
    @property
    def IsInherited(self) -> bool:
        """"""
    @property
    def PropagationFlags(self) -> PropagationFlags:
        """"""
    @property
    def SemaphoreRights(self) -> SemaphoreRights:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class SemaphoreRights(Enum):
    """"""

    Modify: SemaphoreRights = ...
    """"""
    Delete: SemaphoreRights = ...
    """"""
    ReadPermissions: SemaphoreRights = ...
    """"""
    ChangePermissions: SemaphoreRights = ...
    """"""
    TakeOwnership: SemaphoreRights = ...
    """"""
    Synchronize: SemaphoreRights = ...
    """"""
    FullControl: SemaphoreRights = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SemaphoreSecurity(NativeObjectSecurity):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, name: str, includeSections: AccessControlSections) -> None:
        """"""
    @property
    def AccessRightType(self) -> Type:
        """"""
    @property
    def AccessRuleType(self) -> Type:
        """"""
    @property
    def AreAccessRulesCanonical(self) -> bool:
        """"""
    @property
    def AreAccessRulesProtected(self) -> bool:
        """"""
    @property
    def AreAuditRulesCanonical(self) -> bool:
        """"""
    @property
    def AreAuditRulesProtected(self) -> bool:
        """"""
    @property
    def AuditRuleType(self) -> Type:
        """"""
    def AccessRuleFactory(
        self,
        identityReference: IdentityReference,
        accessMask: int,
        isInherited: bool,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
        type: AccessControlType,
    ) -> AccessRule:
        """"""
    def AddAccessRule(self, rule: SemaphoreAccessRule) -> None:
        """"""
    def AddAuditRule(self, rule: SemaphoreAuditRule) -> None:
        """"""
    def AuditRuleFactory(
        self,
        identityReference: IdentityReference,
        accessMask: int,
        isInherited: bool,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
        flags: AuditFlags,
    ) -> AuditRule:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetAccessRules(
        self, includeExplicit: bool, includeInherited: bool, targetType: Type
    ) -> AuthorizationRuleCollection:
        """"""
    def GetAuditRules(
        self, includeExplicit: bool, includeInherited: bool, targetType: Type
    ) -> AuthorizationRuleCollection:
        """"""
    def GetGroup(self, targetType: Type) -> IdentityReference:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetOwner(self, targetType: Type) -> IdentityReference:
        """"""
    def GetSecurityDescriptorBinaryForm(self) -> Array[int]:
        """"""
    def GetSecurityDescriptorSddlForm(self, includeSections: AccessControlSections) -> str:
        """"""
    def GetType(self) -> Type:
        """"""
    def ModifyAccessRule(
        self, modification: AccessControlModification, rule: AccessRule, modified: Boolean
    ) -> tuple[bool, Boolean]:
        """"""
    def ModifyAuditRule(
        self, modification: AccessControlModification, rule: AuditRule, modified: Boolean
    ) -> tuple[bool, Boolean]:
        """"""
    def PurgeAccessRules(self, identity: IdentityReference) -> None:
        """"""
    def PurgeAuditRules(self, identity: IdentityReference) -> None:
        """"""
    def RemoveAccessRule(self, rule: SemaphoreAccessRule) -> bool:
        """"""
    def RemoveAccessRuleAll(self, rule: SemaphoreAccessRule) -> None:
        """"""
    def RemoveAccessRuleSpecific(self, rule: SemaphoreAccessRule) -> None:
        """"""
    def RemoveAuditRule(self, rule: SemaphoreAuditRule) -> bool:
        """"""
    def RemoveAuditRuleAll(self, rule: SemaphoreAuditRule) -> None:
        """"""
    def RemoveAuditRuleSpecific(self, rule: SemaphoreAuditRule) -> None:
        """"""
    def ResetAccessRule(self, rule: SemaphoreAccessRule) -> None:
        """"""
    def SetAccessRule(self, rule: SemaphoreAccessRule) -> None:
        """"""
    def SetAccessRuleProtection(self, isProtected: bool, preserveInheritance: bool) -> None:
        """"""
    def SetAuditRule(self, rule: SemaphoreAuditRule) -> None:
        """"""
    def SetAuditRuleProtection(self, isProtected: bool, preserveInheritance: bool) -> None:
        """"""
    def SetGroup(self, identity: IdentityReference) -> None:
        """"""
    def SetOwner(self, identity: IdentityReference) -> None:
        """"""
    @overload
    def SetSecurityDescriptorBinaryForm(self, binaryForm: Array[int]) -> None:
        """"""
    @overload
    def SetSecurityDescriptorBinaryForm(
        self, binaryForm: Array[int], includeSections: AccessControlSections
    ) -> None:
        """"""
    @overload
    def SetSecurityDescriptorSddlForm(self, sddlForm: str) -> None:
        """"""
    @overload
    def SetSecurityDescriptorSddlForm(
        self, sddlForm: str, includeSections: AccessControlSections
    ) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SystemAcl(CommonAcl, ICollection, IEnumerable):
    """"""
    @overload
    def __init__(self, isContainer: bool, isDS: bool, capacity: int) -> None:
        """"""
    @overload
    def __init__(self, isContainer: bool, isDS: bool, revision: int, capacity: int) -> None:
        """"""
    @overload
    def __init__(self, isContainer: bool, isDS: bool, rawAcl: RawAcl) -> None:
        """"""
    @property
    def BinaryLength(self) -> int:
        """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsCanonical(self) -> bool:
        """"""
    @property
    def IsContainer(self) -> bool:
        """"""
    @property
    def IsDS(self) -> bool:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def Item(self) -> GenericAce:
        """"""
    @Item.setter
    def Item(self, value: GenericAce) -> None: ...
    @property
    def Revision(self) -> int:
        """"""
    @property
    def SyncRoot(self) -> object:
        """"""
    @overload
    def AddAudit(
        self,
        auditFlags: AuditFlags,
        sid: SecurityIdentifier,
        accessMask: int,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
    ) -> None:
        """"""
    @overload
    def AddAudit(
        self,
        auditFlags: AuditFlags,
        sid: SecurityIdentifier,
        accessMask: int,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
        objectFlags: ObjectAceFlags,
        objectType: Guid,
        inheritedObjectType: Guid,
    ) -> None:
        """"""
    @overload
    def AddAudit(self, sid: SecurityIdentifier, rule: ObjectAuditRule) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array[GenericAce], index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetBinaryForm(self, binaryForm: Array[int], offset: int) -> None:
        """"""
    def GetEnumerator(self) -> AceEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Purge(self, sid: SecurityIdentifier) -> None:
        """"""
    @overload
    def RemoveAudit(
        self,
        auditFlags: AuditFlags,
        sid: SecurityIdentifier,
        accessMask: int,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
    ) -> bool:
        """"""
    @overload
    def RemoveAudit(
        self,
        auditFlags: AuditFlags,
        sid: SecurityIdentifier,
        accessMask: int,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
        objectFlags: ObjectAceFlags,
        objectType: Guid,
        inheritedObjectType: Guid,
    ) -> bool:
        """"""
    @overload
    def RemoveAudit(self, sid: SecurityIdentifier, rule: ObjectAuditRule) -> bool:
        """"""
    @overload
    def RemoveAuditSpecific(
        self,
        auditFlags: AuditFlags,
        sid: SecurityIdentifier,
        accessMask: int,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
    ) -> None:
        """"""
    @overload
    def RemoveAuditSpecific(
        self,
        auditFlags: AuditFlags,
        sid: SecurityIdentifier,
        accessMask: int,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
        objectFlags: ObjectAceFlags,
        objectType: Guid,
        inheritedObjectType: Guid,
    ) -> None:
        """"""
    @overload
    def RemoveAuditSpecific(self, sid: SecurityIdentifier, rule: ObjectAuditRule) -> None:
        """"""
    def RemoveInheritedAces(self) -> None:
        """"""
    @overload
    def SetAudit(
        self,
        auditFlags: AuditFlags,
        sid: SecurityIdentifier,
        accessMask: int,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
    ) -> None:
        """"""
    @overload
    def SetAudit(
        self,
        auditFlags: AuditFlags,
        sid: SecurityIdentifier,
        accessMask: int,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
        objectFlags: ObjectAceFlags,
        objectType: Guid,
        inheritedObjectType: Guid,
    ) -> None:
        """"""
    @overload
    def SetAudit(self, sid: SecurityIdentifier, rule: ObjectAuditRule) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, index: int) -> GenericAce:
        """"""
    def __setitem__(self, index: int, value: GenericAce) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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
