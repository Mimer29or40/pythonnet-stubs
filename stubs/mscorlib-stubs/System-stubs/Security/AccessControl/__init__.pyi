from __future__ import annotations

from abc import ABC
from typing import Generic, List, Protocol, Tuple, TypeVar, Union, overload

from System import Array, Boolean, Byte, Enum, Exception, Guid, Int32, Object, String, Type, UnauthorizedAccessException, ValueType, Void
from System.Collections import ICollection, IEnumerable, IEnumerator, ReadOnlyCollectionBase
from System.Runtime.InteropServices import _Exception
from System.Runtime.Serialization import ISerializable, SerializationInfo, StreamingContext
from System.Security.Principal import IdentityReference, SecurityIdentifier

# ---------- Types ---------- #

T = TypeVar('T', bound=ValueType)

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
ByteType = Union[int, Byte]
IntType = Union[int, Int32]
ObjectType = Object
StringType = Union[str, String]
TypeType = Union[type, Type]
VoidType = Union[None, Void]

# ---------- Classes ---------- #

class AccessRule(Generic[T], AccessRule):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, identity: IdentityReference, rights: T, type: AccessControlType): ...
    
    @overload
    def __init__(self, identity: StringType, rights: T, type: AccessControlType): ...
    
    @overload
    def __init__(self, identity: IdentityReference, rights: T, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, type: AccessControlType): ...
    
    @overload
    def __init__(self, identity: StringType, rights: T, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, type: AccessControlType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Rights(self) -> T: ...
    
    # ---------- Methods ---------- #
    
    def get_Rights(self) -> T: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AccessRule(ABC, AuthorizationRule):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def AccessControlType(self) -> AccessControlType: ...
    
    # ---------- Methods ---------- #
    
    def get_AccessControlType(self) -> AccessControlType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AceEnumerator(ObjectType, IEnumerator):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Current(self) -> GenericAce: ...
    
    # ---------- Methods ---------- #
    
    def MoveNext(self) -> BooleanType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Current(self) -> GenericAce: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AuditRule(Generic[T], AuditRule):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, identity: IdentityReference, rights: T, flags: AuditFlags): ...
    
    @overload
    def __init__(self, identity: IdentityReference, rights: T, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, flags: AuditFlags): ...
    
    @overload
    def __init__(self, identity: StringType, rights: T, flags: AuditFlags): ...
    
    @overload
    def __init__(self, identity: StringType, rights: T, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, flags: AuditFlags): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Rights(self) -> T: ...
    
    # ---------- Methods ---------- #
    
    def get_Rights(self) -> T: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AuditRule(ABC, AuthorizationRule):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def AuditFlags(self) -> AuditFlags: ...
    
    # ---------- Methods ---------- #
    
    def get_AuditFlags(self) -> AuditFlags: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AuthorizationRule(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def IdentityReference(self) -> IdentityReference: ...
    
    @property
    def InheritanceFlags(self) -> InheritanceFlags: ...
    
    @property
    def IsInherited(self) -> BooleanType: ...
    
    @property
    def PropagationFlags(self) -> PropagationFlags: ...
    
    # ---------- Methods ---------- #
    
    def get_IdentityReference(self) -> IdentityReference: ...
    
    def get_InheritanceFlags(self) -> InheritanceFlags: ...
    
    def get_IsInherited(self) -> BooleanType: ...
    
    def get_PropagationFlags(self) -> PropagationFlags: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AuthorizationRuleCollection(ReadOnlyCollectionBase, ICollection, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Item(self) -> AuthorizationRule: ...
    
    # ---------- Methods ---------- #
    
    def AddRule(self, rule: AuthorizationRule) -> VoidType: ...
    
    def CopyTo(self, rules: ArrayType[AuthorizationRule], index: IntType) -> VoidType: ...
    
    def get_Item(self, index: IntType) -> AuthorizationRule: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CommonAce(QualifiedAce):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, flags: AceFlags, qualifier: AceQualifier, accessMask: IntType, sid: SecurityIdentifier, isCallback: BooleanType, opaque: ArrayType[ByteType]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def BinaryLength(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def GetBinaryForm(self, binaryForm: ArrayType[ByteType], offset: IntType) -> VoidType: ...
    
    @staticmethod
    def MaxOpaqueLength(isCallback: BooleanType) -> IntType: ...
    
    def get_BinaryLength(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CommonAcl(ABC, GenericAcl, ICollection, IEnumerable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def BinaryLength(self) -> IntType: ...
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def IsCanonical(self) -> BooleanType: ...
    
    @property
    def IsContainer(self) -> BooleanType: ...
    
    @property
    def IsDS(self) -> BooleanType: ...
    
    @property
    def Item(self) -> GenericAce: ...
    
    @Item.setter
    def Item(self, value: GenericAce) -> None: ...
    
    @property
    def Revision(self) -> ByteType: ...
    
    # ---------- Methods ---------- #
    
    def GetBinaryForm(self, binaryForm: ArrayType[ByteType], offset: IntType) -> VoidType: ...
    
    def Purge(self, sid: SecurityIdentifier) -> VoidType: ...
    
    def RemoveInheritedAces(self) -> VoidType: ...
    
    def get_BinaryLength(self) -> IntType: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_IsCanonical(self) -> BooleanType: ...
    
    def get_IsContainer(self) -> BooleanType: ...
    
    def get_IsDS(self) -> BooleanType: ...
    
    def get_Item(self, index: IntType) -> GenericAce: ...
    
    def get_Revision(self) -> ByteType: ...
    
    def set_Item(self, index: IntType, value: GenericAce) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CommonObjectSecurity(ABC, ObjectSecurity):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetAccessRules(self, includeExplicit: BooleanType, includeInherited: BooleanType, targetType: TypeType) -> AuthorizationRuleCollection: ...
    
    def GetAuditRules(self, includeExplicit: BooleanType, includeInherited: BooleanType, targetType: TypeType) -> AuthorizationRuleCollection: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CommonSecurityDescriptor(GenericSecurityDescriptor):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, isContainer: BooleanType, isDS: BooleanType, flags: ControlFlags, owner: SecurityIdentifier, group: SecurityIdentifier, systemAcl: SystemAcl, discretionaryAcl: DiscretionaryAcl): ...
    
    @overload
    def __init__(self, isContainer: BooleanType, isDS: BooleanType, rawSecurityDescriptor: RawSecurityDescriptor): ...
    
    @overload
    def __init__(self, isContainer: BooleanType, isDS: BooleanType, sddlForm: StringType): ...
    
    @overload
    def __init__(self, isContainer: BooleanType, isDS: BooleanType, binaryForm: ArrayType[ByteType], offset: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ControlFlags(self) -> ControlFlags: ...
    
    @property
    def DiscretionaryAcl(self) -> DiscretionaryAcl: ...
    
    @DiscretionaryAcl.setter
    def DiscretionaryAcl(self, value: DiscretionaryAcl) -> None: ...
    
    @property
    def Group(self) -> SecurityIdentifier: ...
    
    @Group.setter
    def Group(self, value: SecurityIdentifier) -> None: ...
    
    @property
    def IsContainer(self) -> BooleanType: ...
    
    @property
    def IsDS(self) -> BooleanType: ...
    
    @property
    def IsDiscretionaryAclCanonical(self) -> BooleanType: ...
    
    @property
    def IsSystemAclCanonical(self) -> BooleanType: ...
    
    @property
    def Owner(self) -> SecurityIdentifier: ...
    
    @Owner.setter
    def Owner(self, value: SecurityIdentifier) -> None: ...
    
    @property
    def SystemAcl(self) -> SystemAcl: ...
    
    @SystemAcl.setter
    def SystemAcl(self, value: SystemAcl) -> None: ...
    
    # ---------- Methods ---------- #
    
    def AddDiscretionaryAcl(self, revision: ByteType, trusted: IntType) -> VoidType: ...
    
    def AddSystemAcl(self, revision: ByteType, trusted: IntType) -> VoidType: ...
    
    def PurgeAccessControl(self, sid: SecurityIdentifier) -> VoidType: ...
    
    def PurgeAudit(self, sid: SecurityIdentifier) -> VoidType: ...
    
    def SetDiscretionaryAclProtection(self, isProtected: BooleanType, preserveInheritance: BooleanType) -> VoidType: ...
    
    def SetSystemAclProtection(self, isProtected: BooleanType, preserveInheritance: BooleanType) -> VoidType: ...
    
    def get_ControlFlags(self) -> ControlFlags: ...
    
    def get_DiscretionaryAcl(self) -> DiscretionaryAcl: ...
    
    def get_Group(self) -> SecurityIdentifier: ...
    
    def get_IsContainer(self) -> BooleanType: ...
    
    def get_IsDS(self) -> BooleanType: ...
    
    def get_IsDiscretionaryAclCanonical(self) -> BooleanType: ...
    
    def get_IsSystemAclCanonical(self) -> BooleanType: ...
    
    def get_Owner(self) -> SecurityIdentifier: ...
    
    def get_SystemAcl(self) -> SystemAcl: ...
    
    def set_DiscretionaryAcl(self, value: DiscretionaryAcl) -> VoidType: ...
    
    def set_Group(self, value: SecurityIdentifier) -> VoidType: ...
    
    def set_Owner(self, value: SecurityIdentifier) -> VoidType: ...
    
    def set_SystemAcl(self, value: SystemAcl) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CompoundAce(KnownAce):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, flags: AceFlags, accessMask: IntType, compoundAceType: CompoundAceType, sid: SecurityIdentifier): ...
    
    # ---------- Properties ---------- #
    
    @property
    def BinaryLength(self) -> IntType: ...
    
    @property
    def CompoundAceType(self) -> CompoundAceType: ...
    
    @CompoundAceType.setter
    def CompoundAceType(self, value: CompoundAceType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def GetBinaryForm(self, binaryForm: ArrayType[ByteType], offset: IntType) -> VoidType: ...
    
    def get_BinaryLength(self) -> IntType: ...
    
    def get_CompoundAceType(self) -> CompoundAceType: ...
    
    def set_CompoundAceType(self, value: CompoundAceType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CryptoKeyAccessRule(AccessRule):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, identity: IdentityReference, cryptoKeyRights: CryptoKeyRights, type: AccessControlType): ...
    
    @overload
    def __init__(self, identity: StringType, cryptoKeyRights: CryptoKeyRights, type: AccessControlType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CryptoKeyRights(self) -> CryptoKeyRights: ...
    
    # ---------- Methods ---------- #
    
    def get_CryptoKeyRights(self) -> CryptoKeyRights: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CryptoKeyAuditRule(AuditRule):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, identity: IdentityReference, cryptoKeyRights: CryptoKeyRights, flags: AuditFlags): ...
    
    @overload
    def __init__(self, identity: StringType, cryptoKeyRights: CryptoKeyRights, flags: AuditFlags): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CryptoKeyRights(self) -> CryptoKeyRights: ...
    
    # ---------- Methods ---------- #
    
    def get_CryptoKeyRights(self) -> CryptoKeyRights: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CryptoKeySecurity(NativeObjectSecurity):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, securityDescriptor: CommonSecurityDescriptor): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AccessRightType(self) -> TypeType: ...
    
    @property
    def AccessRuleType(self) -> TypeType: ...
    
    @property
    def AuditRuleType(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def AccessRuleFactory(self, identityReference: IdentityReference, accessMask: IntType, isInherited: BooleanType, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, type: AccessControlType) -> AccessRule: ...
    
    def AddAccessRule(self, rule: CryptoKeyAccessRule) -> VoidType: ...
    
    def AddAuditRule(self, rule: CryptoKeyAuditRule) -> VoidType: ...
    
    def AuditRuleFactory(self, identityReference: IdentityReference, accessMask: IntType, isInherited: BooleanType, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, flags: AuditFlags) -> AuditRule: ...
    
    def RemoveAccessRule(self, rule: CryptoKeyAccessRule) -> BooleanType: ...
    
    def RemoveAccessRuleAll(self, rule: CryptoKeyAccessRule) -> VoidType: ...
    
    def RemoveAccessRuleSpecific(self, rule: CryptoKeyAccessRule) -> VoidType: ...
    
    def RemoveAuditRule(self, rule: CryptoKeyAuditRule) -> BooleanType: ...
    
    def RemoveAuditRuleAll(self, rule: CryptoKeyAuditRule) -> VoidType: ...
    
    def RemoveAuditRuleSpecific(self, rule: CryptoKeyAuditRule) -> VoidType: ...
    
    def ResetAccessRule(self, rule: CryptoKeyAccessRule) -> VoidType: ...
    
    def SetAccessRule(self, rule: CryptoKeyAccessRule) -> VoidType: ...
    
    def SetAuditRule(self, rule: CryptoKeyAuditRule) -> VoidType: ...
    
    def get_AccessRightType(self) -> TypeType: ...
    
    def get_AccessRuleType(self) -> TypeType: ...
    
    def get_AuditRuleType(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CustomAce(GenericAce):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def MaxOpaqueLength() -> IntType: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self, type: AceType, flags: AceFlags, opaque: ArrayType[ByteType]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def BinaryLength(self) -> IntType: ...
    
    @property
    def OpaqueLength(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def GetBinaryForm(self, binaryForm: ArrayType[ByteType], offset: IntType) -> VoidType: ...
    
    def GetOpaque(self) -> ArrayType[ByteType]: ...
    
    def SetOpaque(self, opaque: ArrayType[ByteType]) -> VoidType: ...
    
    def get_BinaryLength(self) -> IntType: ...
    
    def get_OpaqueLength(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DirectoryObjectSecurity(ABC, ObjectSecurity):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def AccessRuleFactory(self, identityReference: IdentityReference, accessMask: IntType, isInherited: BooleanType, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, type: AccessControlType, objectType: Guid, inheritedObjectType: Guid) -> AccessRule: ...
    
    @overload
    def AuditRuleFactory(self, identityReference: IdentityReference, accessMask: IntType, isInherited: BooleanType, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, flags: AuditFlags, objectType: Guid, inheritedObjectType: Guid) -> AuditRule: ...
    
    def GetAccessRules(self, includeExplicit: BooleanType, includeInherited: BooleanType, targetType: TypeType) -> AuthorizationRuleCollection: ...
    
    def GetAuditRules(self, includeExplicit: BooleanType, includeInherited: BooleanType, targetType: TypeType) -> AuthorizationRuleCollection: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DirectorySecurity(FileSystemSecurity):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, name: StringType, includeSections: AccessControlSections): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DiscretionaryAcl(CommonAcl, ICollection, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, isContainer: BooleanType, isDS: BooleanType, capacity: IntType): ...
    
    @overload
    def __init__(self, isContainer: BooleanType, isDS: BooleanType, revision: ByteType, capacity: IntType): ...
    
    @overload
    def __init__(self, isContainer: BooleanType, isDS: BooleanType, rawAcl: RawAcl): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def AddAccess(self, accessType: AccessControlType, sid: SecurityIdentifier, accessMask: IntType, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags) -> VoidType: ...
    
    @overload
    def AddAccess(self, accessType: AccessControlType, sid: SecurityIdentifier, rule: ObjectAccessRule) -> VoidType: ...
    
    @overload
    def AddAccess(self, accessType: AccessControlType, sid: SecurityIdentifier, accessMask: IntType, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, objectFlags: ObjectAceFlags, objectType: Guid, inheritedObjectType: Guid) -> VoidType: ...
    
    @overload
    def RemoveAccess(self, accessType: AccessControlType, sid: SecurityIdentifier, accessMask: IntType, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags) -> BooleanType: ...
    
    @overload
    def RemoveAccess(self, accessType: AccessControlType, sid: SecurityIdentifier, rule: ObjectAccessRule) -> BooleanType: ...
    
    @overload
    def RemoveAccess(self, accessType: AccessControlType, sid: SecurityIdentifier, accessMask: IntType, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, objectFlags: ObjectAceFlags, objectType: Guid, inheritedObjectType: Guid) -> BooleanType: ...
    
    @overload
    def RemoveAccessSpecific(self, accessType: AccessControlType, sid: SecurityIdentifier, accessMask: IntType, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags) -> VoidType: ...
    
    @overload
    def RemoveAccessSpecific(self, accessType: AccessControlType, sid: SecurityIdentifier, rule: ObjectAccessRule) -> VoidType: ...
    
    @overload
    def RemoveAccessSpecific(self, accessType: AccessControlType, sid: SecurityIdentifier, accessMask: IntType, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, objectFlags: ObjectAceFlags, objectType: Guid, inheritedObjectType: Guid) -> VoidType: ...
    
    @overload
    def SetAccess(self, accessType: AccessControlType, sid: SecurityIdentifier, accessMask: IntType, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags) -> VoidType: ...
    
    @overload
    def SetAccess(self, accessType: AccessControlType, sid: SecurityIdentifier, rule: ObjectAccessRule) -> VoidType: ...
    
    @overload
    def SetAccess(self, accessType: AccessControlType, sid: SecurityIdentifier, accessMask: IntType, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, objectFlags: ObjectAceFlags, objectType: Guid, inheritedObjectType: Guid) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EventWaitHandleAccessRule(AccessRule):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, identity: IdentityReference, eventRights: EventWaitHandleRights, type: AccessControlType): ...
    
    @overload
    def __init__(self, identity: StringType, eventRights: EventWaitHandleRights, type: AccessControlType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def EventWaitHandleRights(self) -> EventWaitHandleRights: ...
    
    # ---------- Methods ---------- #
    
    def get_EventWaitHandleRights(self) -> EventWaitHandleRights: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EventWaitHandleAuditRule(AuditRule):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, identity: IdentityReference, eventRights: EventWaitHandleRights, flags: AuditFlags): ...
    
    # ---------- Properties ---------- #
    
    @property
    def EventWaitHandleRights(self) -> EventWaitHandleRights: ...
    
    # ---------- Methods ---------- #
    
    def get_EventWaitHandleRights(self) -> EventWaitHandleRights: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EventWaitHandleSecurity(NativeObjectSecurity):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AccessRightType(self) -> TypeType: ...
    
    @property
    def AccessRuleType(self) -> TypeType: ...
    
    @property
    def AuditRuleType(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def AccessRuleFactory(self, identityReference: IdentityReference, accessMask: IntType, isInherited: BooleanType, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, type: AccessControlType) -> AccessRule: ...
    
    def AddAccessRule(self, rule: EventWaitHandleAccessRule) -> VoidType: ...
    
    def AddAuditRule(self, rule: EventWaitHandleAuditRule) -> VoidType: ...
    
    def AuditRuleFactory(self, identityReference: IdentityReference, accessMask: IntType, isInherited: BooleanType, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, flags: AuditFlags) -> AuditRule: ...
    
    def RemoveAccessRule(self, rule: EventWaitHandleAccessRule) -> BooleanType: ...
    
    def RemoveAccessRuleAll(self, rule: EventWaitHandleAccessRule) -> VoidType: ...
    
    def RemoveAccessRuleSpecific(self, rule: EventWaitHandleAccessRule) -> VoidType: ...
    
    def RemoveAuditRule(self, rule: EventWaitHandleAuditRule) -> BooleanType: ...
    
    def RemoveAuditRuleAll(self, rule: EventWaitHandleAuditRule) -> VoidType: ...
    
    def RemoveAuditRuleSpecific(self, rule: EventWaitHandleAuditRule) -> VoidType: ...
    
    def ResetAccessRule(self, rule: EventWaitHandleAccessRule) -> VoidType: ...
    
    def SetAccessRule(self, rule: EventWaitHandleAccessRule) -> VoidType: ...
    
    def SetAuditRule(self, rule: EventWaitHandleAuditRule) -> VoidType: ...
    
    def get_AccessRightType(self) -> TypeType: ...
    
    def get_AccessRuleType(self) -> TypeType: ...
    
    def get_AuditRuleType(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class FileSecurity(FileSystemSecurity):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, fileName: StringType, includeSections: AccessControlSections): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class FileSystemAccessRule(AccessRule):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, identity: IdentityReference, fileSystemRights: FileSystemRights, type: AccessControlType): ...
    
    @overload
    def __init__(self, identity: StringType, fileSystemRights: FileSystemRights, type: AccessControlType): ...
    
    @overload
    def __init__(self, identity: IdentityReference, fileSystemRights: FileSystemRights, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, type: AccessControlType): ...
    
    @overload
    def __init__(self, identity: StringType, fileSystemRights: FileSystemRights, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, type: AccessControlType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def FileSystemRights(self) -> FileSystemRights: ...
    
    # ---------- Methods ---------- #
    
    def get_FileSystemRights(self) -> FileSystemRights: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class FileSystemAuditRule(AuditRule):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, identity: IdentityReference, fileSystemRights: FileSystemRights, flags: AuditFlags): ...
    
    @overload
    def __init__(self, identity: IdentityReference, fileSystemRights: FileSystemRights, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, flags: AuditFlags): ...
    
    @overload
    def __init__(self, identity: StringType, fileSystemRights: FileSystemRights, flags: AuditFlags): ...
    
    @overload
    def __init__(self, identity: StringType, fileSystemRights: FileSystemRights, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, flags: AuditFlags): ...
    
    # ---------- Properties ---------- #
    
    @property
    def FileSystemRights(self) -> FileSystemRights: ...
    
    # ---------- Methods ---------- #
    
    def get_FileSystemRights(self) -> FileSystemRights: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class FileSystemSecurity(ABC, NativeObjectSecurity):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def AccessRightType(self) -> TypeType: ...
    
    @property
    def AccessRuleType(self) -> TypeType: ...
    
    @property
    def AuditRuleType(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def AccessRuleFactory(self, identityReference: IdentityReference, accessMask: IntType, isInherited: BooleanType, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, type: AccessControlType) -> AccessRule: ...
    
    def AddAccessRule(self, rule: FileSystemAccessRule) -> VoidType: ...
    
    def AddAuditRule(self, rule: FileSystemAuditRule) -> VoidType: ...
    
    def AuditRuleFactory(self, identityReference: IdentityReference, accessMask: IntType, isInherited: BooleanType, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, flags: AuditFlags) -> AuditRule: ...
    
    def RemoveAccessRule(self, rule: FileSystemAccessRule) -> BooleanType: ...
    
    def RemoveAccessRuleAll(self, rule: FileSystemAccessRule) -> VoidType: ...
    
    def RemoveAccessRuleSpecific(self, rule: FileSystemAccessRule) -> VoidType: ...
    
    def RemoveAuditRule(self, rule: FileSystemAuditRule) -> BooleanType: ...
    
    def RemoveAuditRuleAll(self, rule: FileSystemAuditRule) -> VoidType: ...
    
    def RemoveAuditRuleSpecific(self, rule: FileSystemAuditRule) -> VoidType: ...
    
    def ResetAccessRule(self, rule: FileSystemAccessRule) -> VoidType: ...
    
    def SetAccessRule(self, rule: FileSystemAccessRule) -> VoidType: ...
    
    def SetAuditRule(self, rule: FileSystemAuditRule) -> VoidType: ...
    
    def get_AccessRightType(self) -> TypeType: ...
    
    def get_AccessRuleType(self) -> TypeType: ...
    
    def get_AuditRuleType(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class GenericAce(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def AceFlags(self) -> AceFlags: ...
    
    @AceFlags.setter
    def AceFlags(self, value: AceFlags) -> None: ...
    
    @property
    def AceType(self) -> AceType: ...
    
    @property
    def AuditFlags(self) -> AuditFlags: ...
    
    @property
    def BinaryLength(self) -> IntType: ...
    
    @property
    def InheritanceFlags(self) -> InheritanceFlags: ...
    
    @property
    def IsInherited(self) -> BooleanType: ...
    
    @property
    def PropagationFlags(self) -> PropagationFlags: ...
    
    # ---------- Methods ---------- #
    
    def Copy(self) -> GenericAce: ...
    
    @staticmethod
    def CreateFromBinaryForm(binaryForm: ArrayType[ByteType], offset: IntType) -> GenericAce: ...
    
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    def GetBinaryForm(self, binaryForm: ArrayType[ByteType], offset: IntType) -> VoidType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def get_AceFlags(self) -> AceFlags: ...
    
    def get_AceType(self) -> AceType: ...
    
    def get_AuditFlags(self) -> AuditFlags: ...
    
    def get_BinaryLength(self) -> IntType: ...
    
    def get_InheritanceFlags(self) -> InheritanceFlags: ...
    
    def get_IsInherited(self) -> BooleanType: ...
    
    def get_PropagationFlags(self) -> PropagationFlags: ...
    
    @staticmethod
    def op_Equality(left: GenericAce, right: GenericAce) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(left: GenericAce, right: GenericAce) -> BooleanType: ...
    
    def set_AceFlags(self, value: AceFlags) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class GenericAcl(ABC, ObjectType, ICollection, IEnumerable):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def AclRevision() -> ByteType: ...
    
    @staticmethod
    @property
    def AclRevisionDS() -> ByteType: ...
    
    @staticmethod
    @property
    def MaxBinaryLength() -> IntType: ...
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def BinaryLength(self) -> IntType: ...
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def IsSynchronized(self) -> BooleanType: ...
    
    @property
    def Item(self) -> GenericAce: ...
    
    @Item.setter
    def Item(self, value: GenericAce) -> None: ...
    
    @property
    def Revision(self) -> ByteType: ...
    
    @property
    def SyncRoot(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def CopyTo(self, array: ArrayType[GenericAce], index: IntType) -> VoidType: ...
    
    def GetBinaryForm(self, binaryForm: ArrayType[ByteType], offset: IntType) -> VoidType: ...
    
    def GetEnumerator(self) -> AceEnumerator: ...
    
    def get_BinaryLength(self) -> IntType: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_IsSynchronized(self) -> BooleanType: ...
    
    def get_Item(self, index: IntType) -> GenericAce: ...
    
    def get_Revision(self) -> ByteType: ...
    
    def get_SyncRoot(self) -> ObjectType: ...
    
    def set_Item(self, index: IntType, value: GenericAce) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class GenericSecurityDescriptor(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def BinaryLength(self) -> IntType: ...
    
    @property
    def ControlFlags(self) -> ControlFlags: ...
    
    @property
    def Group(self) -> SecurityIdentifier: ...
    
    @Group.setter
    def Group(self, value: SecurityIdentifier) -> None: ...
    
    @property
    def Owner(self) -> SecurityIdentifier: ...
    
    @Owner.setter
    def Owner(self, value: SecurityIdentifier) -> None: ...
    
    @staticmethod
    @property
    def Revision() -> ByteType: ...
    
    # ---------- Methods ---------- #
    
    def GetBinaryForm(self, binaryForm: ArrayType[ByteType], offset: IntType) -> VoidType: ...
    
    def GetSddlForm(self, includeSections: AccessControlSections) -> StringType: ...
    
    @staticmethod
    def IsSddlConversionSupported() -> BooleanType: ...
    
    def get_BinaryLength(self) -> IntType: ...
    
    def get_ControlFlags(self) -> ControlFlags: ...
    
    def get_Group(self) -> SecurityIdentifier: ...
    
    def get_Owner(self) -> SecurityIdentifier: ...
    
    @staticmethod
    def get_Revision() -> ByteType: ...
    
    def set_Group(self, value: SecurityIdentifier) -> VoidType: ...
    
    def set_Owner(self, value: SecurityIdentifier) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class KnownAce(ABC, GenericAce):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def AccessMask(self) -> IntType: ...
    
    @AccessMask.setter
    def AccessMask(self, value: IntType) -> None: ...
    
    @property
    def SecurityIdentifier(self) -> SecurityIdentifier: ...
    
    @SecurityIdentifier.setter
    def SecurityIdentifier(self, value: SecurityIdentifier) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_AccessMask(self) -> IntType: ...
    
    def get_SecurityIdentifier(self) -> SecurityIdentifier: ...
    
    def set_AccessMask(self, value: IntType) -> VoidType: ...
    
    def set_SecurityIdentifier(self, value: SecurityIdentifier) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MutexAccessRule(AccessRule):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, identity: IdentityReference, eventRights: MutexRights, type: AccessControlType): ...
    
    @overload
    def __init__(self, identity: StringType, eventRights: MutexRights, type: AccessControlType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def MutexRights(self) -> MutexRights: ...
    
    # ---------- Methods ---------- #
    
    def get_MutexRights(self) -> MutexRights: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MutexAuditRule(AuditRule):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, identity: IdentityReference, eventRights: MutexRights, flags: AuditFlags): ...
    
    # ---------- Properties ---------- #
    
    @property
    def MutexRights(self) -> MutexRights: ...
    
    # ---------- Methods ---------- #
    
    def get_MutexRights(self) -> MutexRights: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MutexSecurity(NativeObjectSecurity):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, name: StringType, includeSections: AccessControlSections): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AccessRightType(self) -> TypeType: ...
    
    @property
    def AccessRuleType(self) -> TypeType: ...
    
    @property
    def AuditRuleType(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def AccessRuleFactory(self, identityReference: IdentityReference, accessMask: IntType, isInherited: BooleanType, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, type: AccessControlType) -> AccessRule: ...
    
    def AddAccessRule(self, rule: MutexAccessRule) -> VoidType: ...
    
    def AddAuditRule(self, rule: MutexAuditRule) -> VoidType: ...
    
    def AuditRuleFactory(self, identityReference: IdentityReference, accessMask: IntType, isInherited: BooleanType, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, flags: AuditFlags) -> AuditRule: ...
    
    def RemoveAccessRule(self, rule: MutexAccessRule) -> BooleanType: ...
    
    def RemoveAccessRuleAll(self, rule: MutexAccessRule) -> VoidType: ...
    
    def RemoveAccessRuleSpecific(self, rule: MutexAccessRule) -> VoidType: ...
    
    def RemoveAuditRule(self, rule: MutexAuditRule) -> BooleanType: ...
    
    def RemoveAuditRuleAll(self, rule: MutexAuditRule) -> VoidType: ...
    
    def RemoveAuditRuleSpecific(self, rule: MutexAuditRule) -> VoidType: ...
    
    def ResetAccessRule(self, rule: MutexAccessRule) -> VoidType: ...
    
    def SetAccessRule(self, rule: MutexAccessRule) -> VoidType: ...
    
    def SetAuditRule(self, rule: MutexAuditRule) -> VoidType: ...
    
    def get_AccessRightType(self) -> TypeType: ...
    
    def get_AccessRuleType(self) -> TypeType: ...
    
    def get_AuditRuleType(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class NativeObjectSecurity(ABC, CommonObjectSecurity):
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


class ObjectAccessRule(ABC, AccessRule):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def InheritedObjectType(self) -> Guid: ...
    
    @property
    def ObjectFlags(self) -> ObjectAceFlags: ...
    
    @property
    def ObjectType(self) -> Guid: ...
    
    # ---------- Methods ---------- #
    
    def get_InheritedObjectType(self) -> Guid: ...
    
    def get_ObjectFlags(self) -> ObjectAceFlags: ...
    
    def get_ObjectType(self) -> Guid: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ObjectAce(QualifiedAce):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, aceFlags: AceFlags, qualifier: AceQualifier, accessMask: IntType, sid: SecurityIdentifier, flags: ObjectAceFlags, type: Guid, inheritedType: Guid, isCallback: BooleanType, opaque: ArrayType[ByteType]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def BinaryLength(self) -> IntType: ...
    
    @property
    def InheritedObjectAceType(self) -> Guid: ...
    
    @InheritedObjectAceType.setter
    def InheritedObjectAceType(self, value: Guid) -> None: ...
    
    @property
    def ObjectAceFlags(self) -> ObjectAceFlags: ...
    
    @ObjectAceFlags.setter
    def ObjectAceFlags(self, value: ObjectAceFlags) -> None: ...
    
    @property
    def ObjectAceType(self) -> Guid: ...
    
    @ObjectAceType.setter
    def ObjectAceType(self, value: Guid) -> None: ...
    
    # ---------- Methods ---------- #
    
    def GetBinaryForm(self, binaryForm: ArrayType[ByteType], offset: IntType) -> VoidType: ...
    
    @staticmethod
    def MaxOpaqueLength(isCallback: BooleanType) -> IntType: ...
    
    def get_BinaryLength(self) -> IntType: ...
    
    def get_InheritedObjectAceType(self) -> Guid: ...
    
    def get_ObjectAceFlags(self) -> ObjectAceFlags: ...
    
    def get_ObjectAceType(self) -> Guid: ...
    
    def set_InheritedObjectAceType(self, value: Guid) -> VoidType: ...
    
    def set_ObjectAceFlags(self, value: ObjectAceFlags) -> VoidType: ...
    
    def set_ObjectAceType(self, value: Guid) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ObjectAuditRule(ABC, AuditRule):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def InheritedObjectType(self) -> Guid: ...
    
    @property
    def ObjectFlags(self) -> ObjectAceFlags: ...
    
    @property
    def ObjectType(self) -> Guid: ...
    
    # ---------- Methods ---------- #
    
    def get_InheritedObjectType(self) -> Guid: ...
    
    def get_ObjectFlags(self) -> ObjectAceFlags: ...
    
    def get_ObjectType(self) -> Guid: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ObjectSecurity(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def AccessRightType(self) -> TypeType: ...
    
    @property
    def AccessRuleType(self) -> TypeType: ...
    
    @property
    def AreAccessRulesCanonical(self) -> BooleanType: ...
    
    @property
    def AreAccessRulesProtected(self) -> BooleanType: ...
    
    @property
    def AreAuditRulesCanonical(self) -> BooleanType: ...
    
    @property
    def AreAuditRulesProtected(self) -> BooleanType: ...
    
    @property
    def AuditRuleType(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def AccessRuleFactory(self, identityReference: IdentityReference, accessMask: IntType, isInherited: BooleanType, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, type: AccessControlType) -> AccessRule: ...
    
    def AuditRuleFactory(self, identityReference: IdentityReference, accessMask: IntType, isInherited: BooleanType, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, flags: AuditFlags) -> AuditRule: ...
    
    def GetGroup(self, targetType: TypeType) -> IdentityReference: ...
    
    def GetOwner(self, targetType: TypeType) -> IdentityReference: ...
    
    def GetSecurityDescriptorBinaryForm(self) -> ArrayType[ByteType]: ...
    
    def GetSecurityDescriptorSddlForm(self, includeSections: AccessControlSections) -> StringType: ...
    
    @staticmethod
    def IsSddlConversionSupported() -> BooleanType: ...
    
    def ModifyAccessRule(self, modification: AccessControlModification, rule: AccessRule, modified: BooleanType) -> Tuple[BooleanType, BooleanType]: ...
    
    def ModifyAuditRule(self, modification: AccessControlModification, rule: AuditRule, modified: BooleanType) -> Tuple[BooleanType, BooleanType]: ...
    
    def PurgeAccessRules(self, identity: IdentityReference) -> VoidType: ...
    
    def PurgeAuditRules(self, identity: IdentityReference) -> VoidType: ...
    
    def SetAccessRuleProtection(self, isProtected: BooleanType, preserveInheritance: BooleanType) -> VoidType: ...
    
    def SetAuditRuleProtection(self, isProtected: BooleanType, preserveInheritance: BooleanType) -> VoidType: ...
    
    def SetGroup(self, identity: IdentityReference) -> VoidType: ...
    
    def SetOwner(self, identity: IdentityReference) -> VoidType: ...
    
    @overload
    def SetSecurityDescriptorBinaryForm(self, binaryForm: ArrayType[ByteType]) -> VoidType: ...
    
    @overload
    def SetSecurityDescriptorBinaryForm(self, binaryForm: ArrayType[ByteType], includeSections: AccessControlSections) -> VoidType: ...
    
    @overload
    def SetSecurityDescriptorSddlForm(self, sddlForm: StringType) -> VoidType: ...
    
    @overload
    def SetSecurityDescriptorSddlForm(self, sddlForm: StringType, includeSections: AccessControlSections) -> VoidType: ...
    
    def get_AccessRightType(self) -> TypeType: ...
    
    def get_AccessRuleType(self) -> TypeType: ...
    
    def get_AreAccessRulesCanonical(self) -> BooleanType: ...
    
    def get_AreAccessRulesProtected(self) -> BooleanType: ...
    
    def get_AreAuditRulesCanonical(self) -> BooleanType: ...
    
    def get_AreAuditRulesProtected(self) -> BooleanType: ...
    
    def get_AuditRuleType(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ObjectSecurity(Protocol[T], NativeObjectSecurity):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def AccessRightType(self) -> TypeType: ...
    
    @property
    def AccessRuleType(self) -> TypeType: ...
    
    @property
    def AuditRuleType(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def AccessRuleFactory(self, identityReference: IdentityReference, accessMask: IntType, isInherited: BooleanType, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, type: AccessControlType) -> AccessRule: ...
    
    def AddAccessRule(self, rule: AccessRule[T]) -> VoidType: ...
    
    def AddAuditRule(self, rule: AuditRule[T]) -> VoidType: ...
    
    def AuditRuleFactory(self, identityReference: IdentityReference, accessMask: IntType, isInherited: BooleanType, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, flags: AuditFlags) -> AuditRule: ...
    
    def RemoveAccessRule(self, rule: AccessRule[T]) -> BooleanType: ...
    
    def RemoveAccessRuleAll(self, rule: AccessRule[T]) -> VoidType: ...
    
    def RemoveAccessRuleSpecific(self, rule: AccessRule[T]) -> VoidType: ...
    
    def RemoveAuditRule(self, rule: AuditRule[T]) -> BooleanType: ...
    
    def RemoveAuditRuleAll(self, rule: AuditRule[T]) -> VoidType: ...
    
    def RemoveAuditRuleSpecific(self, rule: AuditRule[T]) -> VoidType: ...
    
    def ResetAccessRule(self, rule: AccessRule[T]) -> VoidType: ...
    
    def SetAccessRule(self, rule: AccessRule[T]) -> VoidType: ...
    
    def SetAuditRule(self, rule: AuditRule[T]) -> VoidType: ...
    
    def get_AccessRightType(self) -> TypeType: ...
    
    def get_AccessRuleType(self) -> TypeType: ...
    
    def get_AuditRuleType(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Privilege(ObjectType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def AssignPrimaryToken() -> StringType: ...
    
    @staticmethod
    @property
    def Audit() -> StringType: ...
    
    @staticmethod
    @property
    def Backup() -> StringType: ...
    
    @staticmethod
    @property
    def ChangeNotify() -> StringType: ...
    
    @staticmethod
    @property
    def CreateGlobal() -> StringType: ...
    
    @staticmethod
    @property
    def CreatePageFile() -> StringType: ...
    
    @staticmethod
    @property
    def CreatePermanent() -> StringType: ...
    
    @staticmethod
    @property
    def CreateToken() -> StringType: ...
    
    @staticmethod
    @property
    def Debug() -> StringType: ...
    
    @staticmethod
    @property
    def EnableDelegation() -> StringType: ...
    
    @staticmethod
    @property
    def Impersonate() -> StringType: ...
    
    @staticmethod
    @property
    def IncreaseBasePriority() -> StringType: ...
    
    @staticmethod
    @property
    def IncreaseQuota() -> StringType: ...
    
    @staticmethod
    @property
    def LoadDriver() -> StringType: ...
    
    @staticmethod
    @property
    def LockMemory() -> StringType: ...
    
    @staticmethod
    @property
    def MachineAccount() -> StringType: ...
    
    @staticmethod
    @property
    def ManageVolume() -> StringType: ...
    
    @staticmethod
    @property
    def ProfileSingleProcess() -> StringType: ...
    
    @staticmethod
    @property
    def RemoteShutdown() -> StringType: ...
    
    @staticmethod
    @property
    def ReserveProcessor() -> StringType: ...
    
    @staticmethod
    @property
    def Restore() -> StringType: ...
    
    @staticmethod
    @property
    def Security() -> StringType: ...
    
    @staticmethod
    @property
    def Shutdown() -> StringType: ...
    
    @staticmethod
    @property
    def SyncAgent() -> StringType: ...
    
    @staticmethod
    @property
    def SystemEnvironment() -> StringType: ...
    
    @staticmethod
    @property
    def SystemProfile() -> StringType: ...
    
    @staticmethod
    @property
    def SystemTime() -> StringType: ...
    
    @staticmethod
    @property
    def TakeOwnership() -> StringType: ...
    
    @staticmethod
    @property
    def TrustedComputingBase() -> StringType: ...
    
    @staticmethod
    @property
    def TrustedCredentialManagerAccess() -> StringType: ...
    
    @staticmethod
    @property
    def Undock() -> StringType: ...
    
    @staticmethod
    @property
    def UnsolicitedInput() -> StringType: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self, privilegeName: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def NeedToRevert(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def Enable(self) -> VoidType: ...
    
    def Revert(self) -> VoidType: ...
    
    def get_NeedToRevert(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PrivilegeNotHeldException(UnauthorizedAccessException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, privilege: StringType): ...
    
    @overload
    def __init__(self, privilege: StringType, inner: Exception): ...
    
    # ---------- Properties ---------- #
    
    @property
    def PrivilegeName(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    
    def get_PrivilegeName(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class QualifiedAce(ABC, KnownAce):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def AceQualifier(self) -> AceQualifier: ...
    
    @property
    def IsCallback(self) -> BooleanType: ...
    
    @property
    def OpaqueLength(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def GetOpaque(self) -> ArrayType[ByteType]: ...
    
    def SetOpaque(self, opaque: ArrayType[ByteType]) -> VoidType: ...
    
    def get_AceQualifier(self) -> AceQualifier: ...
    
    def get_IsCallback(self) -> BooleanType: ...
    
    def get_OpaqueLength(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RawAcl(GenericAcl, ICollection, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, revision: ByteType, capacity: IntType): ...
    
    @overload
    def __init__(self, binaryForm: ArrayType[ByteType], offset: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def BinaryLength(self) -> IntType: ...
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def Item(self) -> GenericAce: ...
    
    @Item.setter
    def Item(self, value: GenericAce) -> None: ...
    
    @property
    def Revision(self) -> ByteType: ...
    
    # ---------- Methods ---------- #
    
    def GetBinaryForm(self, binaryForm: ArrayType[ByteType], offset: IntType) -> VoidType: ...
    
    def InsertAce(self, index: IntType, ace: GenericAce) -> VoidType: ...
    
    def RemoveAce(self, index: IntType) -> VoidType: ...
    
    def get_BinaryLength(self) -> IntType: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_Item(self, index: IntType) -> GenericAce: ...
    
    def get_Revision(self) -> ByteType: ...
    
    def set_Item(self, index: IntType, value: GenericAce) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RawSecurityDescriptor(GenericSecurityDescriptor):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, flags: ControlFlags, owner: SecurityIdentifier, group: SecurityIdentifier, systemAcl: RawAcl, discretionaryAcl: RawAcl): ...
    
    @overload
    def __init__(self, sddlForm: StringType): ...
    
    @overload
    def __init__(self, binaryForm: ArrayType[ByteType], offset: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ControlFlags(self) -> ControlFlags: ...
    
    @property
    def DiscretionaryAcl(self) -> RawAcl: ...
    
    @DiscretionaryAcl.setter
    def DiscretionaryAcl(self, value: RawAcl) -> None: ...
    
    @property
    def Group(self) -> SecurityIdentifier: ...
    
    @Group.setter
    def Group(self, value: SecurityIdentifier) -> None: ...
    
    @property
    def Owner(self) -> SecurityIdentifier: ...
    
    @Owner.setter
    def Owner(self, value: SecurityIdentifier) -> None: ...
    
    @property
    def ResourceManagerControl(self) -> ByteType: ...
    
    @ResourceManagerControl.setter
    def ResourceManagerControl(self, value: ByteType) -> None: ...
    
    @property
    def SystemAcl(self) -> RawAcl: ...
    
    @SystemAcl.setter
    def SystemAcl(self, value: RawAcl) -> None: ...
    
    # ---------- Methods ---------- #
    
    def SetFlags(self, flags: ControlFlags) -> VoidType: ...
    
    def get_ControlFlags(self) -> ControlFlags: ...
    
    def get_DiscretionaryAcl(self) -> RawAcl: ...
    
    def get_Group(self) -> SecurityIdentifier: ...
    
    def get_Owner(self) -> SecurityIdentifier: ...
    
    def get_ResourceManagerControl(self) -> ByteType: ...
    
    def get_SystemAcl(self) -> RawAcl: ...
    
    def set_DiscretionaryAcl(self, value: RawAcl) -> VoidType: ...
    
    def set_Group(self, value: SecurityIdentifier) -> VoidType: ...
    
    def set_Owner(self, value: SecurityIdentifier) -> VoidType: ...
    
    def set_ResourceManagerControl(self, value: ByteType) -> VoidType: ...
    
    def set_SystemAcl(self, value: RawAcl) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RegistryAccessRule(AccessRule):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, identity: IdentityReference, registryRights: RegistryRights, type: AccessControlType): ...
    
    @overload
    def __init__(self, identity: StringType, registryRights: RegistryRights, type: AccessControlType): ...
    
    @overload
    def __init__(self, identity: IdentityReference, registryRights: RegistryRights, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, type: AccessControlType): ...
    
    @overload
    def __init__(self, identity: StringType, registryRights: RegistryRights, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, type: AccessControlType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def RegistryRights(self) -> RegistryRights: ...
    
    # ---------- Methods ---------- #
    
    def get_RegistryRights(self) -> RegistryRights: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RegistryAuditRule(AuditRule):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, identity: IdentityReference, registryRights: RegistryRights, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, flags: AuditFlags): ...
    
    @overload
    def __init__(self, identity: StringType, registryRights: RegistryRights, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, flags: AuditFlags): ...
    
    # ---------- Properties ---------- #
    
    @property
    def RegistryRights(self) -> RegistryRights: ...
    
    # ---------- Methods ---------- #
    
    def get_RegistryRights(self) -> RegistryRights: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RegistrySecurity(NativeObjectSecurity):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AccessRightType(self) -> TypeType: ...
    
    @property
    def AccessRuleType(self) -> TypeType: ...
    
    @property
    def AuditRuleType(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def AccessRuleFactory(self, identityReference: IdentityReference, accessMask: IntType, isInherited: BooleanType, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, type: AccessControlType) -> AccessRule: ...
    
    def AddAccessRule(self, rule: RegistryAccessRule) -> VoidType: ...
    
    def AddAuditRule(self, rule: RegistryAuditRule) -> VoidType: ...
    
    def AuditRuleFactory(self, identityReference: IdentityReference, accessMask: IntType, isInherited: BooleanType, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, flags: AuditFlags) -> AuditRule: ...
    
    def RemoveAccessRule(self, rule: RegistryAccessRule) -> BooleanType: ...
    
    def RemoveAccessRuleAll(self, rule: RegistryAccessRule) -> VoidType: ...
    
    def RemoveAccessRuleSpecific(self, rule: RegistryAccessRule) -> VoidType: ...
    
    def RemoveAuditRule(self, rule: RegistryAuditRule) -> BooleanType: ...
    
    def RemoveAuditRuleAll(self, rule: RegistryAuditRule) -> VoidType: ...
    
    def RemoveAuditRuleSpecific(self, rule: RegistryAuditRule) -> VoidType: ...
    
    def ResetAccessRule(self, rule: RegistryAccessRule) -> VoidType: ...
    
    def SetAccessRule(self, rule: RegistryAccessRule) -> VoidType: ...
    
    def SetAuditRule(self, rule: RegistryAuditRule) -> VoidType: ...
    
    def get_AccessRightType(self) -> TypeType: ...
    
    def get_AccessRuleType(self) -> TypeType: ...
    
    def get_AuditRuleType(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SystemAcl(CommonAcl, ICollection, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, isContainer: BooleanType, isDS: BooleanType, capacity: IntType): ...
    
    @overload
    def __init__(self, isContainer: BooleanType, isDS: BooleanType, revision: ByteType, capacity: IntType): ...
    
    @overload
    def __init__(self, isContainer: BooleanType, isDS: BooleanType, rawAcl: RawAcl): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def AddAudit(self, auditFlags: AuditFlags, sid: SecurityIdentifier, accessMask: IntType, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags) -> VoidType: ...
    
    @overload
    def AddAudit(self, sid: SecurityIdentifier, rule: ObjectAuditRule) -> VoidType: ...
    
    @overload
    def AddAudit(self, auditFlags: AuditFlags, sid: SecurityIdentifier, accessMask: IntType, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, objectFlags: ObjectAceFlags, objectType: Guid, inheritedObjectType: Guid) -> VoidType: ...
    
    @overload
    def RemoveAudit(self, auditFlags: AuditFlags, sid: SecurityIdentifier, accessMask: IntType, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags) -> BooleanType: ...
    
    @overload
    def RemoveAudit(self, sid: SecurityIdentifier, rule: ObjectAuditRule) -> BooleanType: ...
    
    @overload
    def RemoveAudit(self, auditFlags: AuditFlags, sid: SecurityIdentifier, accessMask: IntType, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, objectFlags: ObjectAceFlags, objectType: Guid, inheritedObjectType: Guid) -> BooleanType: ...
    
    @overload
    def RemoveAuditSpecific(self, auditFlags: AuditFlags, sid: SecurityIdentifier, accessMask: IntType, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags) -> VoidType: ...
    
    @overload
    def RemoveAuditSpecific(self, sid: SecurityIdentifier, rule: ObjectAuditRule) -> VoidType: ...
    
    @overload
    def RemoveAuditSpecific(self, auditFlags: AuditFlags, sid: SecurityIdentifier, accessMask: IntType, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, objectFlags: ObjectAceFlags, objectType: Guid, inheritedObjectType: Guid) -> VoidType: ...
    
    @overload
    def SetAudit(self, auditFlags: AuditFlags, sid: SecurityIdentifier, accessMask: IntType, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags) -> VoidType: ...
    
    @overload
    def SetAudit(self, sid: SecurityIdentifier, rule: ObjectAuditRule) -> VoidType: ...
    
    @overload
    def SetAudit(self, auditFlags: AuditFlags, sid: SecurityIdentifier, accessMask: IntType, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, objectFlags: ObjectAceFlags, objectType: Guid, inheritedObjectType: Guid) -> VoidType: ...
    
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


# No Structs

# No Interfaces

# ---------- Enums ---------- #

class AccessControlActions(Enum):
    #None: IntType = 0
    View: IntType = 1
    Change: IntType = 2


class AccessControlModification(Enum):
    Add: IntType = 0
    Set: IntType = 1
    Reset: IntType = 2
    Remove: IntType = 3
    RemoveAll: IntType = 4
    RemoveSpecific: IntType = 5


class AccessControlSections(Enum):
    #None: IntType = 0
    Audit: IntType = 1
    Access: IntType = 2
    Owner: IntType = 4
    Group: IntType = 8
    All: IntType = 15


class AccessControlType(Enum):
    Allow: IntType = 0
    Deny: IntType = 1


class AceFlags(Enum):
    #None: ByteType = 0
    ObjectInherit: ByteType = 1
    ContainerInherit: ByteType = 2
    NoPropagateInherit: ByteType = 4
    InheritOnly: ByteType = 8
    InheritanceFlags: ByteType = 15
    Inherited: ByteType = 16
    SuccessfulAccess: ByteType = 64
    FailedAccess: ByteType = 128
    AuditFlags: ByteType = 192


class AceQualifier(Enum):
    AccessAllowed: IntType = 0
    AccessDenied: IntType = 1
    SystemAudit: IntType = 2
    SystemAlarm: IntType = 3


class AceType(Enum):
    AccessAllowed: ByteType = 0
    AccessDenied: ByteType = 1
    SystemAudit: ByteType = 2
    SystemAlarm: ByteType = 3
    AccessAllowedCompound: ByteType = 4
    AccessAllowedObject: ByteType = 5
    AccessDeniedObject: ByteType = 6
    SystemAuditObject: ByteType = 7
    SystemAlarmObject: ByteType = 8
    AccessAllowedCallback: ByteType = 9
    AccessDeniedCallback: ByteType = 10
    AccessAllowedCallbackObject: ByteType = 11
    AccessDeniedCallbackObject: ByteType = 12
    SystemAuditCallback: ByteType = 13
    SystemAlarmCallback: ByteType = 14
    SystemAuditCallbackObject: ByteType = 15
    SystemAlarmCallbackObject: ByteType = 16
    MaxDefinedAceType: ByteType = 16


class AuditFlags(Enum):
    #None: IntType = 0
    Success: IntType = 1
    Failure: IntType = 2


class CompoundAceType(Enum):
    Impersonation: IntType = 1


class ControlFlags(Enum):
    #None: IntType = 0
    OwnerDefaulted: IntType = 1
    GroupDefaulted: IntType = 2
    DiscretionaryAclPresent: IntType = 4
    DiscretionaryAclDefaulted: IntType = 8
    SystemAclPresent: IntType = 16
    SystemAclDefaulted: IntType = 32
    DiscretionaryAclUntrusted: IntType = 64
    ServerSecurity: IntType = 128
    DiscretionaryAclAutoInheritRequired: IntType = 256
    SystemAclAutoInheritRequired: IntType = 512
    DiscretionaryAclAutoInherited: IntType = 1024
    SystemAclAutoInherited: IntType = 2048
    DiscretionaryAclProtected: IntType = 4096
    SystemAclProtected: IntType = 8192
    RMControlValid: IntType = 16384
    SelfRelative: IntType = 32768


class CryptoKeyRights(Enum):
    GenericRead: IntType = -2147483648
    ReadData: IntType = 1
    WriteData: IntType = 2
    ReadExtendedAttributes: IntType = 8
    WriteExtendedAttributes: IntType = 16
    ReadAttributes: IntType = 128
    WriteAttributes: IntType = 256
    Delete: IntType = 65536
    ReadPermissions: IntType = 131072
    ChangePermissions: IntType = 262144
    TakeOwnership: IntType = 524288
    Synchronize: IntType = 1048576
    FullControl: IntType = 2032027
    GenericAll: IntType = 268435456
    GenericExecute: IntType = 536870912
    GenericWrite: IntType = 1073741824


class EventWaitHandleRights(Enum):
    Modify: IntType = 2
    Delete: IntType = 65536
    ReadPermissions: IntType = 131072
    ChangePermissions: IntType = 262144
    TakeOwnership: IntType = 524288
    Synchronize: IntType = 1048576
    FullControl: IntType = 2031619


class FileSystemRights(Enum):
    ListDirectory: IntType = 1
    ReadData: IntType = 1
    WriteData: IntType = 2
    CreateFiles: IntType = 2
    CreateDirectories: IntType = 4
    AppendData: IntType = 4
    ReadExtendedAttributes: IntType = 8
    WriteExtendedAttributes: IntType = 16
    Traverse: IntType = 32
    ExecuteFile: IntType = 32
    DeleteSubdirectoriesAndFiles: IntType = 64
    ReadAttributes: IntType = 128
    WriteAttributes: IntType = 256
    Write: IntType = 278
    Delete: IntType = 65536
    ReadPermissions: IntType = 131072
    Read: IntType = 131209
    ReadAndExecute: IntType = 131241
    Modify: IntType = 197055
    ChangePermissions: IntType = 262144
    TakeOwnership: IntType = 524288
    Synchronize: IntType = 1048576
    FullControl: IntType = 2032127


class InheritanceFlags(Enum):
    #None: IntType = 0
    ContainerInherit: IntType = 1
    ObjectInherit: IntType = 2


class MutexRights(Enum):
    Modify: IntType = 1
    Delete: IntType = 65536
    ReadPermissions: IntType = 131072
    ChangePermissions: IntType = 262144
    TakeOwnership: IntType = 524288
    Synchronize: IntType = 1048576
    FullControl: IntType = 2031617


class ObjectAceFlags(Enum):
    #None: IntType = 0
    ObjectAceTypePresent: IntType = 1
    InheritedObjectAceTypePresent: IntType = 2


class PropagationFlags(Enum):
    #None: IntType = 0
    NoPropagateInherit: IntType = 1
    InheritOnly: IntType = 2


class RegistryRights(Enum):
    QueryValues: IntType = 1
    SetValue: IntType = 2
    CreateSubKey: IntType = 4
    EnumerateSubKeys: IntType = 8
    Notify: IntType = 16
    CreateLink: IntType = 32
    Delete: IntType = 65536
    ReadPermissions: IntType = 131072
    WriteKey: IntType = 131078
    ExecuteKey: IntType = 131097
    ReadKey: IntType = 131097
    ChangePermissions: IntType = 262144
    TakeOwnership: IntType = 524288
    FullControl: IntType = 983103


class ResourceType(Enum):
    Unknown: IntType = 0
    FileObject: IntType = 1
    Service: IntType = 2
    Printer: IntType = 3
    RegistryKey: IntType = 4
    LMShare: IntType = 5
    KernelObject: IntType = 6
    WindowObject: IntType = 7
    DSObject: IntType = 8
    DSObjectAll: IntType = 9
    ProviderDefined: IntType = 10
    WmiGuidObject: IntType = 11
    RegistryWow6432Key: IntType = 12


class SecurityInfos(Enum):
    Owner: IntType = 1
    Group: IntType = 2
    DiscretionaryAcl: IntType = 4
    SystemAcl: IntType = 8


# No Delegates

__all__ = [
    AccessRule,
    AceEnumerator,
    AuditRule,
    AuthorizationRule,
    AuthorizationRuleCollection,
    CommonAce,
    CommonAcl,
    CommonObjectSecurity,
    CommonSecurityDescriptor,
    CompoundAce,
    CryptoKeyAccessRule,
    CryptoKeyAuditRule,
    CryptoKeySecurity,
    CustomAce,
    DirectoryObjectSecurity,
    DirectorySecurity,
    DiscretionaryAcl,
    EventWaitHandleAccessRule,
    EventWaitHandleAuditRule,
    EventWaitHandleSecurity,
    FileSecurity,
    FileSystemAccessRule,
    FileSystemAuditRule,
    FileSystemSecurity,
    GenericAce,
    GenericAcl,
    GenericSecurityDescriptor,
    KnownAce,
    MutexAccessRule,
    MutexAuditRule,
    MutexSecurity,
    NativeObjectSecurity,
    ObjectAccessRule,
    ObjectAce,
    ObjectAuditRule,
    ObjectSecurity,
    Privilege,
    PrivilegeNotHeldException,
    QualifiedAce,
    RawAcl,
    RawSecurityDescriptor,
    RegistryAccessRule,
    RegistryAuditRule,
    RegistrySecurity,
    SystemAcl,
    Win32,
    AccessControlActions,
    AccessControlModification,
    AccessControlSections,
    AccessControlType,
    AceFlags,
    AceQualifier,
    AceType,
    AuditFlags,
    CompoundAceType,
    ControlFlags,
    CryptoKeyRights,
    EventWaitHandleRights,
    FileSystemRights,
    InheritanceFlags,
    MutexRights,
    ObjectAceFlags,
    PropagationFlags,
    RegistryRights,
    ResourceType,
    SecurityInfos,
]
