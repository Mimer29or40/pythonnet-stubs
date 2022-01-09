from __future__ import annotations

from typing import Union, overload

from System import Boolean, Enum, Int32, String, Type, Void
from System.Security.AccessControl import AccessControlSections, AccessControlType, AccessRule, AuditFlags, AuditRule, InheritanceFlags, NativeObjectSecurity, PropagationFlags
from System.Security.Principal import IdentityReference

# ---------- Types ---------- #

BooleanType = Union[bool, Boolean]
IntType = Union[int, Int32]
StringType = Union[str, String]
TypeType = Union[type, Type]
VoidType = Union[None, Void]

# ---------- Classes ---------- #

class SemaphoreAccessRule(AccessRule):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, identity: IdentityReference, eventRights: SemaphoreRights, type: AccessControlType): ...
    
    @overload
    def __init__(self, identity: StringType, eventRights: SemaphoreRights, type: AccessControlType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def SemaphoreRights(self) -> SemaphoreRights: ...
    
    # ---------- Methods ---------- #
    
    def get_SemaphoreRights(self) -> SemaphoreRights: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SemaphoreAuditRule(AuditRule):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, identity: IdentityReference, eventRights: SemaphoreRights, flags: AuditFlags): ...
    
    # ---------- Properties ---------- #
    
    @property
    def SemaphoreRights(self) -> SemaphoreRights: ...
    
    # ---------- Methods ---------- #
    
    def get_SemaphoreRights(self) -> SemaphoreRights: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SemaphoreSecurity(NativeObjectSecurity):
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
    
    def AddAccessRule(self, rule: SemaphoreAccessRule) -> VoidType: ...
    
    def AddAuditRule(self, rule: SemaphoreAuditRule) -> VoidType: ...
    
    def AuditRuleFactory(self, identityReference: IdentityReference, accessMask: IntType, isInherited: BooleanType, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, flags: AuditFlags) -> AuditRule: ...
    
    def RemoveAccessRule(self, rule: SemaphoreAccessRule) -> BooleanType: ...
    
    def RemoveAccessRuleAll(self, rule: SemaphoreAccessRule) -> VoidType: ...
    
    def RemoveAccessRuleSpecific(self, rule: SemaphoreAccessRule) -> VoidType: ...
    
    def RemoveAuditRule(self, rule: SemaphoreAuditRule) -> BooleanType: ...
    
    def RemoveAuditRuleAll(self, rule: SemaphoreAuditRule) -> VoidType: ...
    
    def RemoveAuditRuleSpecific(self, rule: SemaphoreAuditRule) -> VoidType: ...
    
    def ResetAccessRule(self, rule: SemaphoreAccessRule) -> VoidType: ...
    
    def SetAccessRule(self, rule: SemaphoreAccessRule) -> VoidType: ...
    
    def SetAuditRule(self, rule: SemaphoreAuditRule) -> VoidType: ...
    
    def get_AccessRightType(self) -> TypeType: ...
    
    def get_AccessRuleType(self) -> TypeType: ...
    
    def get_AuditRuleType(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# No Structs

# No Interfaces

# ---------- Enums ---------- #

class SemaphoreRights(Enum):
    Modify: IntType = 2
    Delete: IntType = 65536
    ReadPermissions: IntType = 131072
    ChangePermissions: IntType = 262144
    TakeOwnership: IntType = 524288
    Synchronize: IntType = 1048576
    FullControl: IntType = 2031619


# No Delegates

__all__ = [
    SemaphoreAccessRule,
    SemaphoreAuditRule,
    SemaphoreSecurity,
    SemaphoreRights,
]
