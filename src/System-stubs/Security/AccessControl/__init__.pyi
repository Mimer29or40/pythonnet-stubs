from __future__ import annotations

from abc import ABC
from typing import ClassVar
from typing import Final
from typing import Generic
from typing import Iterator
from typing import Tuple
from typing import TypeVar
from typing import overload

from System import Array
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

T = TypeVar("T")

class AccessControlActions(Enum):
    """"""

    _None: AccessControlActions = ...
    """"""
    View: AccessControlActions = ...
    """"""
    Change: AccessControlActions = ...
    """"""

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

class AccessControlType(Enum):
    """"""

    Allow: AccessControlType = ...
    """"""
    Deny: AccessControlType = ...
    """"""

class AccessRule(ABC, AuthorizationRule):
    """"""

    @property
    def AccessControlType(self) -> AccessControlType:
        """

        :return:
        """
    @property
    def IdentityReference(self) -> IdentityReference:
        """

        :return:
        """
    @property
    def InheritanceFlags(self) -> InheritanceFlags:
        """

        :return:
        """
    @property
    def IsInherited(self) -> bool:
        """

        :return:
        """
    @property
    def PropagationFlags(self) -> PropagationFlags:
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

class AccessRule(Generic[T], AccessRule):
    """"""

    @overload
    def __init__(self, identity: IdentityReference, rights: T, type: AccessControlType):
        """

        :param identity:
        :param rights:
        :param type:
        """
    @overload
    def __init__(self, identity: str, rights: T, type: AccessControlType):
        """

        :param identity:
        :param rights:
        :param type:
        """
    @overload
    def __init__(
        self,
        identity: IdentityReference,
        rights: T,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
        type: AccessControlType,
    ):
        """

        :param identity:
        :param rights:
        :param inheritanceFlags:
        :param propagationFlags:
        :param type:
        """
    @overload
    def __init__(
        self,
        identity: str,
        rights: T,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
        type: AccessControlType,
    ):
        """

        :param identity:
        :param rights:
        :param inheritanceFlags:
        :param propagationFlags:
        :param type:
        """
    @property
    def AccessControlType(self) -> AccessControlType:
        """

        :return:
        """
    @property
    def IdentityReference(self) -> IdentityReference:
        """

        :return:
        """
    @property
    def InheritanceFlags(self) -> InheritanceFlags:
        """

        :return:
        """
    @property
    def IsInherited(self) -> bool:
        """

        :return:
        """
    @property
    def PropagationFlags(self) -> PropagationFlags:
        """

        :return:
        """
    @property
    def Rights(self) -> T:
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

class AceEnumerator(Object, IEnumerator):
    """"""

    @property
    def Current(self) -> object:
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

class AuditFlags(Enum):
    """"""

    _None: AuditFlags = ...
    """"""
    Success: AuditFlags = ...
    """"""
    Failure: AuditFlags = ...
    """"""

class AuditRule(ABC, AuthorizationRule):
    """"""

    @property
    def AuditFlags(self) -> AuditFlags:
        """

        :return:
        """
    @property
    def IdentityReference(self) -> IdentityReference:
        """

        :return:
        """
    @property
    def InheritanceFlags(self) -> InheritanceFlags:
        """

        :return:
        """
    @property
    def IsInherited(self) -> bool:
        """

        :return:
        """
    @property
    def PropagationFlags(self) -> PropagationFlags:
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

class AuditRule(Generic[T], AuditRule):
    """"""

    @overload
    def __init__(self, identity: IdentityReference, rights: T, flags: AuditFlags):
        """

        :param identity:
        :param rights:
        :param flags:
        """
    @overload
    def __init__(self, identity: str, rights: T, flags: AuditFlags):
        """

        :param identity:
        :param rights:
        :param flags:
        """
    @overload
    def __init__(
        self,
        identity: IdentityReference,
        rights: T,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
        flags: AuditFlags,
    ):
        """

        :param identity:
        :param rights:
        :param inheritanceFlags:
        :param propagationFlags:
        :param flags:
        """
    @overload
    def __init__(
        self,
        identity: str,
        rights: T,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
        flags: AuditFlags,
    ):
        """

        :param identity:
        :param rights:
        :param inheritanceFlags:
        :param propagationFlags:
        :param flags:
        """
    @property
    def AuditFlags(self) -> AuditFlags:
        """

        :return:
        """
    @property
    def IdentityReference(self) -> IdentityReference:
        """

        :return:
        """
    @property
    def InheritanceFlags(self) -> InheritanceFlags:
        """

        :return:
        """
    @property
    def IsInherited(self) -> bool:
        """

        :return:
        """
    @property
    def PropagationFlags(self) -> PropagationFlags:
        """

        :return:
        """
    @property
    def Rights(self) -> T:
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

class AuthorizationRule(ABC, Object):
    """"""

    @property
    def IdentityReference(self) -> IdentityReference:
        """

        :return:
        """
    @property
    def InheritanceFlags(self) -> InheritanceFlags:
        """

        :return:
        """
    @property
    def IsInherited(self) -> bool:
        """

        :return:
        """
    @property
    def PropagationFlags(self) -> PropagationFlags:
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

class AuthorizationRuleCollection(ReadOnlyCollectionBase, ICollection, IEnumerable):
    """"""

    def __init__(self):
        """"""
    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def IsSynchronized(self) -> bool:
        """

        :return:
        """
    @property
    def Item(self) -> AuthorizationRule:
        """

        :return:
        """
    @property
    def SyncRoot(self) -> object:
        """

        :return:
        """
    def AddRule(self, rule: AuthorizationRule) -> None:
        """

        :param rule:
        """
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    @overload
    def CopyTo(self, rules: Array[AuthorizationRule], index: int) -> None:
        """

        :param rules:
        :param index:
        """
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
    def ToString(self) -> str:
        """

        :return:
        """
    def __contains__(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    def __getitem__(self, index: int) -> AuthorizationRule:
        """

        :param index:
        :return:
        """
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    def __len__(self) -> int:
        """

        :return:
        """

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
    ):
        """

        :param flags:
        :param qualifier:
        :param accessMask:
        :param sid:
        :param isCallback:
        :param opaque:
        """
    @property
    def AccessMask(self) -> int:
        """

        :return:
        """
    @AccessMask.setter
    def AccessMask(self, value: int) -> None: ...
    @property
    def AceFlags(self) -> AceFlags:
        """

        :return:
        """
    @AceFlags.setter
    def AceFlags(self, value: AceFlags) -> None: ...
    @property
    def AceQualifier(self) -> AceQualifier:
        """

        :return:
        """
    @property
    def AceType(self) -> AceType:
        """

        :return:
        """
    @property
    def AuditFlags(self) -> AuditFlags:
        """

        :return:
        """
    @property
    def BinaryLength(self) -> int:
        """

        :return:
        """
    @property
    def InheritanceFlags(self) -> InheritanceFlags:
        """

        :return:
        """
    @property
    def IsCallback(self) -> bool:
        """

        :return:
        """
    @property
    def IsInherited(self) -> bool:
        """

        :return:
        """
    @property
    def OpaqueLength(self) -> int:
        """

        :return:
        """
    @property
    def PropagationFlags(self) -> PropagationFlags:
        """

        :return:
        """
    @property
    def SecurityIdentifier(self) -> SecurityIdentifier:
        """

        :return:
        """
    @SecurityIdentifier.setter
    def SecurityIdentifier(self, value: SecurityIdentifier) -> None: ...
    def Copy(self) -> GenericAce:
        """

        :return:
        """
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
    def GetOpaque(self) -> Array[int]:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @classmethod
    def MaxOpaqueLength(cls, isCallback: bool) -> int:
        """

        :param isCallback:
        :return:
        """
    def SetOpaque(self, opaque: Array[int]) -> None:
        """

        :param opaque:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CommonAcl(ABC, GenericAcl, ICollection, IEnumerable):
    """"""

    @property
    def BinaryLength(self) -> int:
        """

        :return:
        """
    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def IsCanonical(self) -> bool:
        """

        :return:
        """
    @property
    def IsContainer(self) -> bool:
        """

        :return:
        """
    @property
    def IsDS(self) -> bool:
        """

        :return:
        """
    @property
    def IsSynchronized(self) -> bool:
        """

        :return:
        """
    @property
    def Item(self) -> GenericAce:
        """

        :return:
        """
    @Item.setter
    def Item(self, value: GenericAce) -> None: ...
    @property
    def Revision(self) -> int:
        """

        :return:
        """
    @property
    def SyncRoot(self) -> object:
        """

        :return:
        """
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    @overload
    def CopyTo(self, array: Array[GenericAce], index: int) -> None:
        """

        :param array:
        :param index:
        """
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
    def Purge(self, sid: SecurityIdentifier) -> None:
        """

        :param sid:
        """
    def RemoveInheritedAces(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """
    def __contains__(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    def __getitem__(self, index: int) -> GenericAce:
        """

        :param index:
        :return:
        """
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    def __len__(self) -> int:
        """

        :return:
        """
    def __setitem__(self, index: int, value: GenericAce) -> None:
        """

        :param index:
        :param value:
        """

class CommonObjectSecurity(ABC, ObjectSecurity):
    """"""

    @property
    def AccessRightType(self) -> Type:
        """

        :return:
        """
    @property
    def AccessRuleType(self) -> Type:
        """

        :return:
        """
    @property
    def AreAccessRulesCanonical(self) -> bool:
        """

        :return:
        """
    @property
    def AreAccessRulesProtected(self) -> bool:
        """

        :return:
        """
    @property
    def AreAuditRulesCanonical(self) -> bool:
        """

        :return:
        """
    @property
    def AreAuditRulesProtected(self) -> bool:
        """

        :return:
        """
    @property
    def AuditRuleType(self) -> Type:
        """

        :return:
        """
    def AccessRuleFactory(
        self,
        identityReference: IdentityReference,
        accessMask: int,
        isInherited: bool,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
        type: AccessControlType,
    ) -> AccessRule:
        """

        :param identityReference:
        :param accessMask:
        :param isInherited:
        :param inheritanceFlags:
        :param propagationFlags:
        :param type:
        :return:
        """
    def AuditRuleFactory(
        self,
        identityReference: IdentityReference,
        accessMask: int,
        isInherited: bool,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
        flags: AuditFlags,
    ) -> AuditRule:
        """

        :param identityReference:
        :param accessMask:
        :param isInherited:
        :param inheritanceFlags:
        :param propagationFlags:
        :param flags:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetAccessRules(
        self, includeExplicit: bool, includeInherited: bool, targetType: Type
    ) -> AuthorizationRuleCollection:
        """

        :param includeExplicit:
        :param includeInherited:
        :param targetType:
        :return:
        """
    def GetAuditRules(
        self, includeExplicit: bool, includeInherited: bool, targetType: Type
    ) -> AuthorizationRuleCollection:
        """

        :param includeExplicit:
        :param includeInherited:
        :param targetType:
        :return:
        """
    def GetGroup(self, targetType: Type) -> IdentityReference:
        """

        :param targetType:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetOwner(self, targetType: Type) -> IdentityReference:
        """

        :param targetType:
        :return:
        """
    def GetSecurityDescriptorBinaryForm(self) -> Array[int]:
        """

        :return:
        """
    def GetSecurityDescriptorSddlForm(self, includeSections: AccessControlSections) -> str:
        """

        :param includeSections:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ModifyAccessRule(
        self, modification: AccessControlModification, rule: AccessRule, modified: bool
    ) -> Tuple[bool, bool]:
        """

        :param modification:
        :param rule:
        :param modified:
        :return:
        """
    def ModifyAuditRule(
        self, modification: AccessControlModification, rule: AuditRule, modified: bool
    ) -> Tuple[bool, bool]:
        """

        :param modification:
        :param rule:
        :param modified:
        :return:
        """
    def PurgeAccessRules(self, identity: IdentityReference) -> None:
        """

        :param identity:
        """
    def PurgeAuditRules(self, identity: IdentityReference) -> None:
        """

        :param identity:
        """
    def SetAccessRuleProtection(self, isProtected: bool, preserveInheritance: bool) -> None:
        """

        :param isProtected:
        :param preserveInheritance:
        """
    def SetAuditRuleProtection(self, isProtected: bool, preserveInheritance: bool) -> None:
        """

        :param isProtected:
        :param preserveInheritance:
        """
    def SetGroup(self, identity: IdentityReference) -> None:
        """

        :param identity:
        """
    def SetOwner(self, identity: IdentityReference) -> None:
        """

        :param identity:
        """
    @overload
    def SetSecurityDescriptorBinaryForm(self, binaryForm: Array[int]) -> None:
        """

        :param binaryForm:
        """
    @overload
    def SetSecurityDescriptorBinaryForm(
        self, binaryForm: Array[int], includeSections: AccessControlSections
    ) -> None:
        """

        :param binaryForm:
        :param includeSections:
        """
    @overload
    def SetSecurityDescriptorSddlForm(self, sddlForm: str) -> None:
        """

        :param sddlForm:
        """
    @overload
    def SetSecurityDescriptorSddlForm(
        self, sddlForm: str, includeSections: AccessControlSections
    ) -> None:
        """

        :param sddlForm:
        :param includeSections:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CommonSecurityDescriptor(GenericSecurityDescriptor):
    """"""

    @overload
    def __init__(self, isContainer: bool, isDS: bool, rawSecurityDescriptor: RawSecurityDescriptor):
        """

        :param isContainer:
        :param isDS:
        :param rawSecurityDescriptor:
        """
    @overload
    def __init__(self, isContainer: bool, isDS: bool, sddlForm: str):
        """

        :param isContainer:
        :param isDS:
        :param sddlForm:
        """
    @overload
    def __init__(self, isContainer: bool, isDS: bool, binaryForm: Array[int], offset: int):
        """

        :param isContainer:
        :param isDS:
        :param binaryForm:
        :param offset:
        """
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
    ):
        """

        :param isContainer:
        :param isDS:
        :param flags:
        :param owner:
        :param group:
        :param systemAcl:
        :param discretionaryAcl:
        """
    @property
    def BinaryLength(self) -> int:
        """

        :return:
        """
    @property
    def ControlFlags(self) -> ControlFlags:
        """

        :return:
        """
    @property
    def DiscretionaryAcl(self) -> DiscretionaryAcl:
        """

        :return:
        """
    @DiscretionaryAcl.setter
    def DiscretionaryAcl(self, value: DiscretionaryAcl) -> None: ...
    @property
    def Group(self) -> SecurityIdentifier:
        """

        :return:
        """
    @Group.setter
    def Group(self, value: SecurityIdentifier) -> None: ...
    @property
    def IsContainer(self) -> bool:
        """

        :return:
        """
    @property
    def IsDS(self) -> bool:
        """

        :return:
        """
    @property
    def IsDiscretionaryAclCanonical(self) -> bool:
        """

        :return:
        """
    @property
    def IsSystemAclCanonical(self) -> bool:
        """

        :return:
        """
    @property
    def Owner(self) -> SecurityIdentifier:
        """

        :return:
        """
    @Owner.setter
    def Owner(self, value: SecurityIdentifier) -> None: ...
    @classmethod
    @property
    def Revision(cls) -> int:
        """

        :return:
        """
    @property
    def SystemAcl(self) -> SystemAcl:
        """

        :return:
        """
    @SystemAcl.setter
    def SystemAcl(self, value: SystemAcl) -> None: ...
    def AddDiscretionaryAcl(self, revision: int, trusted: int) -> None:
        """

        :param revision:
        :param trusted:
        """
    def AddSystemAcl(self, revision: int, trusted: int) -> None:
        """

        :param revision:
        :param trusted:
        """
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
    def GetSddlForm(self, includeSections: AccessControlSections) -> str:
        """

        :param includeSections:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def PurgeAccessControl(self, sid: SecurityIdentifier) -> None:
        """

        :param sid:
        """
    def PurgeAudit(self, sid: SecurityIdentifier) -> None:
        """

        :param sid:
        """
    def SetDiscretionaryAclProtection(self, isProtected: bool, preserveInheritance: bool) -> None:
        """

        :param isProtected:
        :param preserveInheritance:
        """
    def SetSystemAclProtection(self, isProtected: bool, preserveInheritance: bool) -> None:
        """

        :param isProtected:
        :param preserveInheritance:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CompoundAce(KnownAce):
    """"""

    def __init__(
        self,
        flags: AceFlags,
        accessMask: int,
        compoundAceType: CompoundAceType,
        sid: SecurityIdentifier,
    ):
        """

        :param flags:
        :param accessMask:
        :param compoundAceType:
        :param sid:
        """
    @property
    def AccessMask(self) -> int:
        """

        :return:
        """
    @AccessMask.setter
    def AccessMask(self, value: int) -> None: ...
    @property
    def AceFlags(self) -> AceFlags:
        """

        :return:
        """
    @AceFlags.setter
    def AceFlags(self, value: AceFlags) -> None: ...
    @property
    def AceType(self) -> AceType:
        """

        :return:
        """
    @property
    def AuditFlags(self) -> AuditFlags:
        """

        :return:
        """
    @property
    def BinaryLength(self) -> int:
        """

        :return:
        """
    @property
    def CompoundAceType(self) -> CompoundAceType:
        """

        :return:
        """
    @CompoundAceType.setter
    def CompoundAceType(self, value: CompoundAceType) -> None: ...
    @property
    def InheritanceFlags(self) -> InheritanceFlags:
        """

        :return:
        """
    @property
    def IsInherited(self) -> bool:
        """

        :return:
        """
    @property
    def PropagationFlags(self) -> PropagationFlags:
        """

        :return:
        """
    @property
    def SecurityIdentifier(self) -> SecurityIdentifier:
        """

        :return:
        """
    @SecurityIdentifier.setter
    def SecurityIdentifier(self, value: SecurityIdentifier) -> None: ...
    def Copy(self) -> GenericAce:
        """

        :return:
        """
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
    def ToString(self) -> str:
        """

        :return:
        """

class CompoundAceType(Enum):
    """"""

    Impersonation: CompoundAceType = ...
    """"""

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

class CryptoKeyAccessRule(AccessRule):
    """"""

    @overload
    def __init__(
        self, identity: IdentityReference, cryptoKeyRights: CryptoKeyRights, type: AccessControlType
    ):
        """

        :param identity:
        :param cryptoKeyRights:
        :param type:
        """
    @overload
    def __init__(self, identity: str, cryptoKeyRights: CryptoKeyRights, type: AccessControlType):
        """

        :param identity:
        :param cryptoKeyRights:
        :param type:
        """
    @property
    def AccessControlType(self) -> AccessControlType:
        """

        :return:
        """
    @property
    def CryptoKeyRights(self) -> CryptoKeyRights:
        """

        :return:
        """
    @property
    def IdentityReference(self) -> IdentityReference:
        """

        :return:
        """
    @property
    def InheritanceFlags(self) -> InheritanceFlags:
        """

        :return:
        """
    @property
    def IsInherited(self) -> bool:
        """

        :return:
        """
    @property
    def PropagationFlags(self) -> PropagationFlags:
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

class CryptoKeyAuditRule(AuditRule):
    """"""

    @overload
    def __init__(
        self, identity: IdentityReference, cryptoKeyRights: CryptoKeyRights, flags: AuditFlags
    ):
        """

        :param identity:
        :param cryptoKeyRights:
        :param flags:
        """
    @overload
    def __init__(self, identity: str, cryptoKeyRights: CryptoKeyRights, flags: AuditFlags):
        """

        :param identity:
        :param cryptoKeyRights:
        :param flags:
        """
    @property
    def AuditFlags(self) -> AuditFlags:
        """

        :return:
        """
    @property
    def CryptoKeyRights(self) -> CryptoKeyRights:
        """

        :return:
        """
    @property
    def IdentityReference(self) -> IdentityReference:
        """

        :return:
        """
    @property
    def InheritanceFlags(self) -> InheritanceFlags:
        """

        :return:
        """
    @property
    def IsInherited(self) -> bool:
        """

        :return:
        """
    @property
    def PropagationFlags(self) -> PropagationFlags:
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

class CryptoKeySecurity(NativeObjectSecurity):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, securityDescriptor: CommonSecurityDescriptor):
        """

        :param securityDescriptor:
        """
    @property
    def AccessRightType(self) -> Type:
        """

        :return:
        """
    @property
    def AccessRuleType(self) -> Type:
        """

        :return:
        """
    @property
    def AreAccessRulesCanonical(self) -> bool:
        """

        :return:
        """
    @property
    def AreAccessRulesProtected(self) -> bool:
        """

        :return:
        """
    @property
    def AreAuditRulesCanonical(self) -> bool:
        """

        :return:
        """
    @property
    def AreAuditRulesProtected(self) -> bool:
        """

        :return:
        """
    @property
    def AuditRuleType(self) -> Type:
        """

        :return:
        """
    def AccessRuleFactory(
        self,
        identityReference: IdentityReference,
        accessMask: int,
        isInherited: bool,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
        type: AccessControlType,
    ) -> AccessRule:
        """

        :param identityReference:
        :param accessMask:
        :param isInherited:
        :param inheritanceFlags:
        :param propagationFlags:
        :param type:
        :return:
        """
    def AddAccessRule(self, rule: CryptoKeyAccessRule) -> None:
        """

        :param rule:
        """
    def AddAuditRule(self, rule: CryptoKeyAuditRule) -> None:
        """

        :param rule:
        """
    def AuditRuleFactory(
        self,
        identityReference: IdentityReference,
        accessMask: int,
        isInherited: bool,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
        flags: AuditFlags,
    ) -> AuditRule:
        """

        :param identityReference:
        :param accessMask:
        :param isInherited:
        :param inheritanceFlags:
        :param propagationFlags:
        :param flags:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetAccessRules(
        self, includeExplicit: bool, includeInherited: bool, targetType: Type
    ) -> AuthorizationRuleCollection:
        """

        :param includeExplicit:
        :param includeInherited:
        :param targetType:
        :return:
        """
    def GetAuditRules(
        self, includeExplicit: bool, includeInherited: bool, targetType: Type
    ) -> AuthorizationRuleCollection:
        """

        :param includeExplicit:
        :param includeInherited:
        :param targetType:
        :return:
        """
    def GetGroup(self, targetType: Type) -> IdentityReference:
        """

        :param targetType:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetOwner(self, targetType: Type) -> IdentityReference:
        """

        :param targetType:
        :return:
        """
    def GetSecurityDescriptorBinaryForm(self) -> Array[int]:
        """

        :return:
        """
    def GetSecurityDescriptorSddlForm(self, includeSections: AccessControlSections) -> str:
        """

        :param includeSections:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ModifyAccessRule(
        self, modification: AccessControlModification, rule: AccessRule, modified: bool
    ) -> Tuple[bool, bool]:
        """

        :param modification:
        :param rule:
        :param modified:
        :return:
        """
    def ModifyAuditRule(
        self, modification: AccessControlModification, rule: AuditRule, modified: bool
    ) -> Tuple[bool, bool]:
        """

        :param modification:
        :param rule:
        :param modified:
        :return:
        """
    def PurgeAccessRules(self, identity: IdentityReference) -> None:
        """

        :param identity:
        """
    def PurgeAuditRules(self, identity: IdentityReference) -> None:
        """

        :param identity:
        """
    def RemoveAccessRule(self, rule: CryptoKeyAccessRule) -> bool:
        """

        :param rule:
        :return:
        """
    def RemoveAccessRuleAll(self, rule: CryptoKeyAccessRule) -> None:
        """

        :param rule:
        """
    def RemoveAccessRuleSpecific(self, rule: CryptoKeyAccessRule) -> None:
        """

        :param rule:
        """
    def RemoveAuditRule(self, rule: CryptoKeyAuditRule) -> bool:
        """

        :param rule:
        :return:
        """
    def RemoveAuditRuleAll(self, rule: CryptoKeyAuditRule) -> None:
        """

        :param rule:
        """
    def RemoveAuditRuleSpecific(self, rule: CryptoKeyAuditRule) -> None:
        """

        :param rule:
        """
    def ResetAccessRule(self, rule: CryptoKeyAccessRule) -> None:
        """

        :param rule:
        """
    def SetAccessRule(self, rule: CryptoKeyAccessRule) -> None:
        """

        :param rule:
        """
    def SetAccessRuleProtection(self, isProtected: bool, preserveInheritance: bool) -> None:
        """

        :param isProtected:
        :param preserveInheritance:
        """
    def SetAuditRule(self, rule: CryptoKeyAuditRule) -> None:
        """

        :param rule:
        """
    def SetAuditRuleProtection(self, isProtected: bool, preserveInheritance: bool) -> None:
        """

        :param isProtected:
        :param preserveInheritance:
        """
    def SetGroup(self, identity: IdentityReference) -> None:
        """

        :param identity:
        """
    def SetOwner(self, identity: IdentityReference) -> None:
        """

        :param identity:
        """
    @overload
    def SetSecurityDescriptorBinaryForm(self, binaryForm: Array[int]) -> None:
        """

        :param binaryForm:
        """
    @overload
    def SetSecurityDescriptorBinaryForm(
        self, binaryForm: Array[int], includeSections: AccessControlSections
    ) -> None:
        """

        :param binaryForm:
        :param includeSections:
        """
    @overload
    def SetSecurityDescriptorSddlForm(self, sddlForm: str) -> None:
        """

        :param sddlForm:
        """
    @overload
    def SetSecurityDescriptorSddlForm(
        self, sddlForm: str, includeSections: AccessControlSections
    ) -> None:
        """

        :param sddlForm:
        :param includeSections:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CustomAce(GenericAce):
    """"""

    MaxOpaqueLength: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    def __init__(self, type: AceType, flags: AceFlags, opaque: Array[int]):
        """

        :param type:
        :param flags:
        :param opaque:
        """
    @property
    def AceFlags(self) -> AceFlags:
        """

        :return:
        """
    @AceFlags.setter
    def AceFlags(self, value: AceFlags) -> None: ...
    @property
    def AceType(self) -> AceType:
        """

        :return:
        """
    @property
    def AuditFlags(self) -> AuditFlags:
        """

        :return:
        """
    @property
    def BinaryLength(self) -> int:
        """

        :return:
        """
    @property
    def InheritanceFlags(self) -> InheritanceFlags:
        """

        :return:
        """
    @property
    def IsInherited(self) -> bool:
        """

        :return:
        """
    @property
    def OpaqueLength(self) -> int:
        """

        :return:
        """
    @property
    def PropagationFlags(self) -> PropagationFlags:
        """

        :return:
        """
    def Copy(self) -> GenericAce:
        """

        :return:
        """
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
    def GetOpaque(self) -> Array[int]:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def SetOpaque(self, opaque: Array[int]) -> None:
        """

        :param opaque:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class DirectoryObjectSecurity(ABC, ObjectSecurity):
    """"""

    @property
    def AccessRightType(self) -> Type:
        """

        :return:
        """
    @property
    def AccessRuleType(self) -> Type:
        """

        :return:
        """
    @property
    def AreAccessRulesCanonical(self) -> bool:
        """

        :return:
        """
    @property
    def AreAccessRulesProtected(self) -> bool:
        """

        :return:
        """
    @property
    def AreAuditRulesCanonical(self) -> bool:
        """

        :return:
        """
    @property
    def AreAuditRulesProtected(self) -> bool:
        """

        :return:
        """
    @property
    def AuditRuleType(self) -> Type:
        """

        :return:
        """
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
        """

        :param identityReference:
        :param accessMask:
        :param isInherited:
        :param inheritanceFlags:
        :param propagationFlags:
        :param type:
        :return:
        """
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
        """

        :param identityReference:
        :param accessMask:
        :param isInherited:
        :param inheritanceFlags:
        :param propagationFlags:
        :param type:
        :param objectType:
        :param inheritedObjectType:
        :return:
        """
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
        """

        :param identityReference:
        :param accessMask:
        :param isInherited:
        :param inheritanceFlags:
        :param propagationFlags:
        :param flags:
        :return:
        """
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
        """

        :param identityReference:
        :param accessMask:
        :param isInherited:
        :param inheritanceFlags:
        :param propagationFlags:
        :param flags:
        :param objectType:
        :param inheritedObjectType:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetAccessRules(
        self, includeExplicit: bool, includeInherited: bool, targetType: Type
    ) -> AuthorizationRuleCollection:
        """

        :param includeExplicit:
        :param includeInherited:
        :param targetType:
        :return:
        """
    def GetAuditRules(
        self, includeExplicit: bool, includeInherited: bool, targetType: Type
    ) -> AuthorizationRuleCollection:
        """

        :param includeExplicit:
        :param includeInherited:
        :param targetType:
        :return:
        """
    def GetGroup(self, targetType: Type) -> IdentityReference:
        """

        :param targetType:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetOwner(self, targetType: Type) -> IdentityReference:
        """

        :param targetType:
        :return:
        """
    def GetSecurityDescriptorBinaryForm(self) -> Array[int]:
        """

        :return:
        """
    def GetSecurityDescriptorSddlForm(self, includeSections: AccessControlSections) -> str:
        """

        :param includeSections:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ModifyAccessRule(
        self, modification: AccessControlModification, rule: AccessRule, modified: bool
    ) -> Tuple[bool, bool]:
        """

        :param modification:
        :param rule:
        :param modified:
        :return:
        """
    def ModifyAuditRule(
        self, modification: AccessControlModification, rule: AuditRule, modified: bool
    ) -> Tuple[bool, bool]:
        """

        :param modification:
        :param rule:
        :param modified:
        :return:
        """
    def PurgeAccessRules(self, identity: IdentityReference) -> None:
        """

        :param identity:
        """
    def PurgeAuditRules(self, identity: IdentityReference) -> None:
        """

        :param identity:
        """
    def SetAccessRuleProtection(self, isProtected: bool, preserveInheritance: bool) -> None:
        """

        :param isProtected:
        :param preserveInheritance:
        """
    def SetAuditRuleProtection(self, isProtected: bool, preserveInheritance: bool) -> None:
        """

        :param isProtected:
        :param preserveInheritance:
        """
    def SetGroup(self, identity: IdentityReference) -> None:
        """

        :param identity:
        """
    def SetOwner(self, identity: IdentityReference) -> None:
        """

        :param identity:
        """
    @overload
    def SetSecurityDescriptorBinaryForm(self, binaryForm: Array[int]) -> None:
        """

        :param binaryForm:
        """
    @overload
    def SetSecurityDescriptorBinaryForm(
        self, binaryForm: Array[int], includeSections: AccessControlSections
    ) -> None:
        """

        :param binaryForm:
        :param includeSections:
        """
    @overload
    def SetSecurityDescriptorSddlForm(self, sddlForm: str) -> None:
        """

        :param sddlForm:
        """
    @overload
    def SetSecurityDescriptorSddlForm(
        self, sddlForm: str, includeSections: AccessControlSections
    ) -> None:
        """

        :param sddlForm:
        :param includeSections:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class DirectorySecurity(FileSystemSecurity):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, name: str, includeSections: AccessControlSections):
        """

        :param name:
        :param includeSections:
        """
    @property
    def AccessRightType(self) -> Type:
        """

        :return:
        """
    @property
    def AccessRuleType(self) -> Type:
        """

        :return:
        """
    @property
    def AreAccessRulesCanonical(self) -> bool:
        """

        :return:
        """
    @property
    def AreAccessRulesProtected(self) -> bool:
        """

        :return:
        """
    @property
    def AreAuditRulesCanonical(self) -> bool:
        """

        :return:
        """
    @property
    def AreAuditRulesProtected(self) -> bool:
        """

        :return:
        """
    @property
    def AuditRuleType(self) -> Type:
        """

        :return:
        """
    def AccessRuleFactory(
        self,
        identityReference: IdentityReference,
        accessMask: int,
        isInherited: bool,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
        type: AccessControlType,
    ) -> AccessRule:
        """

        :param identityReference:
        :param accessMask:
        :param isInherited:
        :param inheritanceFlags:
        :param propagationFlags:
        :param type:
        :return:
        """
    def AddAccessRule(self, rule: FileSystemAccessRule) -> None:
        """

        :param rule:
        """
    def AddAuditRule(self, rule: FileSystemAuditRule) -> None:
        """

        :param rule:
        """
    def AuditRuleFactory(
        self,
        identityReference: IdentityReference,
        accessMask: int,
        isInherited: bool,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
        flags: AuditFlags,
    ) -> AuditRule:
        """

        :param identityReference:
        :param accessMask:
        :param isInherited:
        :param inheritanceFlags:
        :param propagationFlags:
        :param flags:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetAccessRules(
        self, includeExplicit: bool, includeInherited: bool, targetType: Type
    ) -> AuthorizationRuleCollection:
        """

        :param includeExplicit:
        :param includeInherited:
        :param targetType:
        :return:
        """
    def GetAuditRules(
        self, includeExplicit: bool, includeInherited: bool, targetType: Type
    ) -> AuthorizationRuleCollection:
        """

        :param includeExplicit:
        :param includeInherited:
        :param targetType:
        :return:
        """
    def GetGroup(self, targetType: Type) -> IdentityReference:
        """

        :param targetType:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetOwner(self, targetType: Type) -> IdentityReference:
        """

        :param targetType:
        :return:
        """
    def GetSecurityDescriptorBinaryForm(self) -> Array[int]:
        """

        :return:
        """
    def GetSecurityDescriptorSddlForm(self, includeSections: AccessControlSections) -> str:
        """

        :param includeSections:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ModifyAccessRule(
        self, modification: AccessControlModification, rule: AccessRule, modified: bool
    ) -> Tuple[bool, bool]:
        """

        :param modification:
        :param rule:
        :param modified:
        :return:
        """
    def ModifyAuditRule(
        self, modification: AccessControlModification, rule: AuditRule, modified: bool
    ) -> Tuple[bool, bool]:
        """

        :param modification:
        :param rule:
        :param modified:
        :return:
        """
    def PurgeAccessRules(self, identity: IdentityReference) -> None:
        """

        :param identity:
        """
    def PurgeAuditRules(self, identity: IdentityReference) -> None:
        """

        :param identity:
        """
    def RemoveAccessRule(self, rule: FileSystemAccessRule) -> bool:
        """

        :param rule:
        :return:
        """
    def RemoveAccessRuleAll(self, rule: FileSystemAccessRule) -> None:
        """

        :param rule:
        """
    def RemoveAccessRuleSpecific(self, rule: FileSystemAccessRule) -> None:
        """

        :param rule:
        """
    def RemoveAuditRule(self, rule: FileSystemAuditRule) -> bool:
        """

        :param rule:
        :return:
        """
    def RemoveAuditRuleAll(self, rule: FileSystemAuditRule) -> None:
        """

        :param rule:
        """
    def RemoveAuditRuleSpecific(self, rule: FileSystemAuditRule) -> None:
        """

        :param rule:
        """
    def ResetAccessRule(self, rule: FileSystemAccessRule) -> None:
        """

        :param rule:
        """
    def SetAccessRule(self, rule: FileSystemAccessRule) -> None:
        """

        :param rule:
        """
    def SetAccessRuleProtection(self, isProtected: bool, preserveInheritance: bool) -> None:
        """

        :param isProtected:
        :param preserveInheritance:
        """
    def SetAuditRule(self, rule: FileSystemAuditRule) -> None:
        """

        :param rule:
        """
    def SetAuditRuleProtection(self, isProtected: bool, preserveInheritance: bool) -> None:
        """

        :param isProtected:
        :param preserveInheritance:
        """
    def SetGroup(self, identity: IdentityReference) -> None:
        """

        :param identity:
        """
    def SetOwner(self, identity: IdentityReference) -> None:
        """

        :param identity:
        """
    @overload
    def SetSecurityDescriptorBinaryForm(self, binaryForm: Array[int]) -> None:
        """

        :param binaryForm:
        """
    @overload
    def SetSecurityDescriptorBinaryForm(
        self, binaryForm: Array[int], includeSections: AccessControlSections
    ) -> None:
        """

        :param binaryForm:
        :param includeSections:
        """
    @overload
    def SetSecurityDescriptorSddlForm(self, sddlForm: str) -> None:
        """

        :param sddlForm:
        """
    @overload
    def SetSecurityDescriptorSddlForm(
        self, sddlForm: str, includeSections: AccessControlSections
    ) -> None:
        """

        :param sddlForm:
        :param includeSections:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class DiscretionaryAcl(CommonAcl, ICollection, IEnumerable):
    """"""

    @overload
    def __init__(self, isContainer: bool, isDS: bool, rawAcl: RawAcl):
        """

        :param isContainer:
        :param isDS:
        :param rawAcl:
        """
    @overload
    def __init__(self, isContainer: bool, isDS: bool, capacity: int):
        """

        :param isContainer:
        :param isDS:
        :param capacity:
        """
    @overload
    def __init__(self, isContainer: bool, isDS: bool, revision: int, capacity: int):
        """

        :param isContainer:
        :param isDS:
        :param revision:
        :param capacity:
        """
    @property
    def BinaryLength(self) -> int:
        """

        :return:
        """
    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def IsCanonical(self) -> bool:
        """

        :return:
        """
    @property
    def IsContainer(self) -> bool:
        """

        :return:
        """
    @property
    def IsDS(self) -> bool:
        """

        :return:
        """
    @property
    def IsSynchronized(self) -> bool:
        """

        :return:
        """
    @property
    def Item(self) -> GenericAce:
        """

        :return:
        """
    @Item.setter
    def Item(self, value: GenericAce) -> None: ...
    @property
    def Revision(self) -> int:
        """

        :return:
        """
    @property
    def SyncRoot(self) -> object:
        """

        :return:
        """
    @overload
    def AddAccess(
        self, accessType: AccessControlType, sid: SecurityIdentifier, rule: ObjectAccessRule
    ) -> None:
        """

        :param accessType:
        :param sid:
        :param rule:
        """
    @overload
    def AddAccess(
        self,
        accessType: AccessControlType,
        sid: SecurityIdentifier,
        accessMask: int,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
    ) -> None:
        """

        :param accessType:
        :param sid:
        :param accessMask:
        :param inheritanceFlags:
        :param propagationFlags:
        """
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
        """

        :param accessType:
        :param sid:
        :param accessMask:
        :param inheritanceFlags:
        :param propagationFlags:
        :param objectFlags:
        :param objectType:
        :param inheritedObjectType:
        """
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    @overload
    def CopyTo(self, array: Array[GenericAce], index: int) -> None:
        """

        :param array:
        :param index:
        """
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
    def Purge(self, sid: SecurityIdentifier) -> None:
        """

        :param sid:
        """
    @overload
    def RemoveAccess(
        self, accessType: AccessControlType, sid: SecurityIdentifier, rule: ObjectAccessRule
    ) -> bool:
        """

        :param accessType:
        :param sid:
        :param rule:
        :return:
        """
    @overload
    def RemoveAccess(
        self,
        accessType: AccessControlType,
        sid: SecurityIdentifier,
        accessMask: int,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
    ) -> bool:
        """

        :param accessType:
        :param sid:
        :param accessMask:
        :param inheritanceFlags:
        :param propagationFlags:
        :return:
        """
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
        """

        :param accessType:
        :param sid:
        :param accessMask:
        :param inheritanceFlags:
        :param propagationFlags:
        :param objectFlags:
        :param objectType:
        :param inheritedObjectType:
        :return:
        """
    @overload
    def RemoveAccessSpecific(
        self, accessType: AccessControlType, sid: SecurityIdentifier, rule: ObjectAccessRule
    ) -> None:
        """

        :param accessType:
        :param sid:
        :param rule:
        """
    @overload
    def RemoveAccessSpecific(
        self,
        accessType: AccessControlType,
        sid: SecurityIdentifier,
        accessMask: int,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
    ) -> None:
        """

        :param accessType:
        :param sid:
        :param accessMask:
        :param inheritanceFlags:
        :param propagationFlags:
        """
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
        """

        :param accessType:
        :param sid:
        :param accessMask:
        :param inheritanceFlags:
        :param propagationFlags:
        :param objectFlags:
        :param objectType:
        :param inheritedObjectType:
        """
    def RemoveInheritedAces(self) -> None:
        """"""
    @overload
    def SetAccess(
        self, accessType: AccessControlType, sid: SecurityIdentifier, rule: ObjectAccessRule
    ) -> None:
        """

        :param accessType:
        :param sid:
        :param rule:
        """
    @overload
    def SetAccess(
        self,
        accessType: AccessControlType,
        sid: SecurityIdentifier,
        accessMask: int,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
    ) -> None:
        """

        :param accessType:
        :param sid:
        :param accessMask:
        :param inheritanceFlags:
        :param propagationFlags:
        """
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
        """

        :param accessType:
        :param sid:
        :param accessMask:
        :param inheritanceFlags:
        :param propagationFlags:
        :param objectFlags:
        :param objectType:
        :param inheritedObjectType:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def __contains__(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    def __getitem__(self, index: int) -> GenericAce:
        """

        :param index:
        :return:
        """
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    def __len__(self) -> int:
        """

        :return:
        """
    def __setitem__(self, index: int, value: GenericAce) -> None:
        """

        :param index:
        :param value:
        """

class EventWaitHandleAccessRule(AccessRule):
    """"""

    @overload
    def __init__(
        self,
        identity: IdentityReference,
        eventRights: EventWaitHandleRights,
        type: AccessControlType,
    ):
        """

        :param identity:
        :param eventRights:
        :param type:
        """
    @overload
    def __init__(self, identity: str, eventRights: EventWaitHandleRights, type: AccessControlType):
        """

        :param identity:
        :param eventRights:
        :param type:
        """
    @property
    def AccessControlType(self) -> AccessControlType:
        """

        :return:
        """
    @property
    def EventWaitHandleRights(self) -> EventWaitHandleRights:
        """

        :return:
        """
    @property
    def IdentityReference(self) -> IdentityReference:
        """

        :return:
        """
    @property
    def InheritanceFlags(self) -> InheritanceFlags:
        """

        :return:
        """
    @property
    def IsInherited(self) -> bool:
        """

        :return:
        """
    @property
    def PropagationFlags(self) -> PropagationFlags:
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

class EventWaitHandleAuditRule(AuditRule):
    """"""

    def __init__(
        self, identity: IdentityReference, eventRights: EventWaitHandleRights, flags: AuditFlags
    ):
        """

        :param identity:
        :param eventRights:
        :param flags:
        """
    @property
    def AuditFlags(self) -> AuditFlags:
        """

        :return:
        """
    @property
    def EventWaitHandleRights(self) -> EventWaitHandleRights:
        """

        :return:
        """
    @property
    def IdentityReference(self) -> IdentityReference:
        """

        :return:
        """
    @property
    def InheritanceFlags(self) -> InheritanceFlags:
        """

        :return:
        """
    @property
    def IsInherited(self) -> bool:
        """

        :return:
        """
    @property
    def PropagationFlags(self) -> PropagationFlags:
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

class EventWaitHandleSecurity(NativeObjectSecurity):
    """"""

    def __init__(self):
        """"""
    @property
    def AccessRightType(self) -> Type:
        """

        :return:
        """
    @property
    def AccessRuleType(self) -> Type:
        """

        :return:
        """
    @property
    def AreAccessRulesCanonical(self) -> bool:
        """

        :return:
        """
    @property
    def AreAccessRulesProtected(self) -> bool:
        """

        :return:
        """
    @property
    def AreAuditRulesCanonical(self) -> bool:
        """

        :return:
        """
    @property
    def AreAuditRulesProtected(self) -> bool:
        """

        :return:
        """
    @property
    def AuditRuleType(self) -> Type:
        """

        :return:
        """
    def AccessRuleFactory(
        self,
        identityReference: IdentityReference,
        accessMask: int,
        isInherited: bool,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
        type: AccessControlType,
    ) -> AccessRule:
        """

        :param identityReference:
        :param accessMask:
        :param isInherited:
        :param inheritanceFlags:
        :param propagationFlags:
        :param type:
        :return:
        """
    def AddAccessRule(self, rule: EventWaitHandleAccessRule) -> None:
        """

        :param rule:
        """
    def AddAuditRule(self, rule: EventWaitHandleAuditRule) -> None:
        """

        :param rule:
        """
    def AuditRuleFactory(
        self,
        identityReference: IdentityReference,
        accessMask: int,
        isInherited: bool,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
        flags: AuditFlags,
    ) -> AuditRule:
        """

        :param identityReference:
        :param accessMask:
        :param isInherited:
        :param inheritanceFlags:
        :param propagationFlags:
        :param flags:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetAccessRules(
        self, includeExplicit: bool, includeInherited: bool, targetType: Type
    ) -> AuthorizationRuleCollection:
        """

        :param includeExplicit:
        :param includeInherited:
        :param targetType:
        :return:
        """
    def GetAuditRules(
        self, includeExplicit: bool, includeInherited: bool, targetType: Type
    ) -> AuthorizationRuleCollection:
        """

        :param includeExplicit:
        :param includeInherited:
        :param targetType:
        :return:
        """
    def GetGroup(self, targetType: Type) -> IdentityReference:
        """

        :param targetType:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetOwner(self, targetType: Type) -> IdentityReference:
        """

        :param targetType:
        :return:
        """
    def GetSecurityDescriptorBinaryForm(self) -> Array[int]:
        """

        :return:
        """
    def GetSecurityDescriptorSddlForm(self, includeSections: AccessControlSections) -> str:
        """

        :param includeSections:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ModifyAccessRule(
        self, modification: AccessControlModification, rule: AccessRule, modified: bool
    ) -> Tuple[bool, bool]:
        """

        :param modification:
        :param rule:
        :param modified:
        :return:
        """
    def ModifyAuditRule(
        self, modification: AccessControlModification, rule: AuditRule, modified: bool
    ) -> Tuple[bool, bool]:
        """

        :param modification:
        :param rule:
        :param modified:
        :return:
        """
    def PurgeAccessRules(self, identity: IdentityReference) -> None:
        """

        :param identity:
        """
    def PurgeAuditRules(self, identity: IdentityReference) -> None:
        """

        :param identity:
        """
    def RemoveAccessRule(self, rule: EventWaitHandleAccessRule) -> bool:
        """

        :param rule:
        :return:
        """
    def RemoveAccessRuleAll(self, rule: EventWaitHandleAccessRule) -> None:
        """

        :param rule:
        """
    def RemoveAccessRuleSpecific(self, rule: EventWaitHandleAccessRule) -> None:
        """

        :param rule:
        """
    def RemoveAuditRule(self, rule: EventWaitHandleAuditRule) -> bool:
        """

        :param rule:
        :return:
        """
    def RemoveAuditRuleAll(self, rule: EventWaitHandleAuditRule) -> None:
        """

        :param rule:
        """
    def RemoveAuditRuleSpecific(self, rule: EventWaitHandleAuditRule) -> None:
        """

        :param rule:
        """
    def ResetAccessRule(self, rule: EventWaitHandleAccessRule) -> None:
        """

        :param rule:
        """
    def SetAccessRule(self, rule: EventWaitHandleAccessRule) -> None:
        """

        :param rule:
        """
    def SetAccessRuleProtection(self, isProtected: bool, preserveInheritance: bool) -> None:
        """

        :param isProtected:
        :param preserveInheritance:
        """
    def SetAuditRule(self, rule: EventWaitHandleAuditRule) -> None:
        """

        :param rule:
        """
    def SetAuditRuleProtection(self, isProtected: bool, preserveInheritance: bool) -> None:
        """

        :param isProtected:
        :param preserveInheritance:
        """
    def SetGroup(self, identity: IdentityReference) -> None:
        """

        :param identity:
        """
    def SetOwner(self, identity: IdentityReference) -> None:
        """

        :param identity:
        """
    @overload
    def SetSecurityDescriptorBinaryForm(self, binaryForm: Array[int]) -> None:
        """

        :param binaryForm:
        """
    @overload
    def SetSecurityDescriptorBinaryForm(
        self, binaryForm: Array[int], includeSections: AccessControlSections
    ) -> None:
        """

        :param binaryForm:
        :param includeSections:
        """
    @overload
    def SetSecurityDescriptorSddlForm(self, sddlForm: str) -> None:
        """

        :param sddlForm:
        """
    @overload
    def SetSecurityDescriptorSddlForm(
        self, sddlForm: str, includeSections: AccessControlSections
    ) -> None:
        """

        :param sddlForm:
        :param includeSections:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class FileSecurity(FileSystemSecurity):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, fileName: str, includeSections: AccessControlSections):
        """

        :param fileName:
        :param includeSections:
        """
    @property
    def AccessRightType(self) -> Type:
        """

        :return:
        """
    @property
    def AccessRuleType(self) -> Type:
        """

        :return:
        """
    @property
    def AreAccessRulesCanonical(self) -> bool:
        """

        :return:
        """
    @property
    def AreAccessRulesProtected(self) -> bool:
        """

        :return:
        """
    @property
    def AreAuditRulesCanonical(self) -> bool:
        """

        :return:
        """
    @property
    def AreAuditRulesProtected(self) -> bool:
        """

        :return:
        """
    @property
    def AuditRuleType(self) -> Type:
        """

        :return:
        """
    def AccessRuleFactory(
        self,
        identityReference: IdentityReference,
        accessMask: int,
        isInherited: bool,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
        type: AccessControlType,
    ) -> AccessRule:
        """

        :param identityReference:
        :param accessMask:
        :param isInherited:
        :param inheritanceFlags:
        :param propagationFlags:
        :param type:
        :return:
        """
    def AddAccessRule(self, rule: FileSystemAccessRule) -> None:
        """

        :param rule:
        """
    def AddAuditRule(self, rule: FileSystemAuditRule) -> None:
        """

        :param rule:
        """
    def AuditRuleFactory(
        self,
        identityReference: IdentityReference,
        accessMask: int,
        isInherited: bool,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
        flags: AuditFlags,
    ) -> AuditRule:
        """

        :param identityReference:
        :param accessMask:
        :param isInherited:
        :param inheritanceFlags:
        :param propagationFlags:
        :param flags:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetAccessRules(
        self, includeExplicit: bool, includeInherited: bool, targetType: Type
    ) -> AuthorizationRuleCollection:
        """

        :param includeExplicit:
        :param includeInherited:
        :param targetType:
        :return:
        """
    def GetAuditRules(
        self, includeExplicit: bool, includeInherited: bool, targetType: Type
    ) -> AuthorizationRuleCollection:
        """

        :param includeExplicit:
        :param includeInherited:
        :param targetType:
        :return:
        """
    def GetGroup(self, targetType: Type) -> IdentityReference:
        """

        :param targetType:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetOwner(self, targetType: Type) -> IdentityReference:
        """

        :param targetType:
        :return:
        """
    def GetSecurityDescriptorBinaryForm(self) -> Array[int]:
        """

        :return:
        """
    def GetSecurityDescriptorSddlForm(self, includeSections: AccessControlSections) -> str:
        """

        :param includeSections:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ModifyAccessRule(
        self, modification: AccessControlModification, rule: AccessRule, modified: bool
    ) -> Tuple[bool, bool]:
        """

        :param modification:
        :param rule:
        :param modified:
        :return:
        """
    def ModifyAuditRule(
        self, modification: AccessControlModification, rule: AuditRule, modified: bool
    ) -> Tuple[bool, bool]:
        """

        :param modification:
        :param rule:
        :param modified:
        :return:
        """
    def PurgeAccessRules(self, identity: IdentityReference) -> None:
        """

        :param identity:
        """
    def PurgeAuditRules(self, identity: IdentityReference) -> None:
        """

        :param identity:
        """
    def RemoveAccessRule(self, rule: FileSystemAccessRule) -> bool:
        """

        :param rule:
        :return:
        """
    def RemoveAccessRuleAll(self, rule: FileSystemAccessRule) -> None:
        """

        :param rule:
        """
    def RemoveAccessRuleSpecific(self, rule: FileSystemAccessRule) -> None:
        """

        :param rule:
        """
    def RemoveAuditRule(self, rule: FileSystemAuditRule) -> bool:
        """

        :param rule:
        :return:
        """
    def RemoveAuditRuleAll(self, rule: FileSystemAuditRule) -> None:
        """

        :param rule:
        """
    def RemoveAuditRuleSpecific(self, rule: FileSystemAuditRule) -> None:
        """

        :param rule:
        """
    def ResetAccessRule(self, rule: FileSystemAccessRule) -> None:
        """

        :param rule:
        """
    def SetAccessRule(self, rule: FileSystemAccessRule) -> None:
        """

        :param rule:
        """
    def SetAccessRuleProtection(self, isProtected: bool, preserveInheritance: bool) -> None:
        """

        :param isProtected:
        :param preserveInheritance:
        """
    def SetAuditRule(self, rule: FileSystemAuditRule) -> None:
        """

        :param rule:
        """
    def SetAuditRuleProtection(self, isProtected: bool, preserveInheritance: bool) -> None:
        """

        :param isProtected:
        :param preserveInheritance:
        """
    def SetGroup(self, identity: IdentityReference) -> None:
        """

        :param identity:
        """
    def SetOwner(self, identity: IdentityReference) -> None:
        """

        :param identity:
        """
    @overload
    def SetSecurityDescriptorBinaryForm(self, binaryForm: Array[int]) -> None:
        """

        :param binaryForm:
        """
    @overload
    def SetSecurityDescriptorBinaryForm(
        self, binaryForm: Array[int], includeSections: AccessControlSections
    ) -> None:
        """

        :param binaryForm:
        :param includeSections:
        """
    @overload
    def SetSecurityDescriptorSddlForm(self, sddlForm: str) -> None:
        """

        :param sddlForm:
        """
    @overload
    def SetSecurityDescriptorSddlForm(
        self, sddlForm: str, includeSections: AccessControlSections
    ) -> None:
        """

        :param sddlForm:
        :param includeSections:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class FileSystemAccessRule(AccessRule):
    """"""

    @overload
    def __init__(
        self,
        identity: IdentityReference,
        fileSystemRights: FileSystemRights,
        type: AccessControlType,
    ):
        """

        :param identity:
        :param fileSystemRights:
        :param type:
        """
    @overload
    def __init__(self, identity: str, fileSystemRights: FileSystemRights, type: AccessControlType):
        """

        :param identity:
        :param fileSystemRights:
        :param type:
        """
    @overload
    def __init__(
        self,
        identity: IdentityReference,
        fileSystemRights: FileSystemRights,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
        type: AccessControlType,
    ):
        """

        :param identity:
        :param fileSystemRights:
        :param inheritanceFlags:
        :param propagationFlags:
        :param type:
        """
    @overload
    def __init__(
        self,
        identity: str,
        fileSystemRights: FileSystemRights,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
        type: AccessControlType,
    ):
        """

        :param identity:
        :param fileSystemRights:
        :param inheritanceFlags:
        :param propagationFlags:
        :param type:
        """
    @property
    def AccessControlType(self) -> AccessControlType:
        """

        :return:
        """
    @property
    def FileSystemRights(self) -> FileSystemRights:
        """

        :return:
        """
    @property
    def IdentityReference(self) -> IdentityReference:
        """

        :return:
        """
    @property
    def InheritanceFlags(self) -> InheritanceFlags:
        """

        :return:
        """
    @property
    def IsInherited(self) -> bool:
        """

        :return:
        """
    @property
    def PropagationFlags(self) -> PropagationFlags:
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

class FileSystemAuditRule(AuditRule):
    """"""

    @overload
    def __init__(
        self, identity: IdentityReference, fileSystemRights: FileSystemRights, flags: AuditFlags
    ):
        """

        :param identity:
        :param fileSystemRights:
        :param flags:
        """
    @overload
    def __init__(self, identity: str, fileSystemRights: FileSystemRights, flags: AuditFlags):
        """

        :param identity:
        :param fileSystemRights:
        :param flags:
        """
    @overload
    def __init__(
        self,
        identity: IdentityReference,
        fileSystemRights: FileSystemRights,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
        flags: AuditFlags,
    ):
        """

        :param identity:
        :param fileSystemRights:
        :param inheritanceFlags:
        :param propagationFlags:
        :param flags:
        """
    @overload
    def __init__(
        self,
        identity: str,
        fileSystemRights: FileSystemRights,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
        flags: AuditFlags,
    ):
        """

        :param identity:
        :param fileSystemRights:
        :param inheritanceFlags:
        :param propagationFlags:
        :param flags:
        """
    @property
    def AuditFlags(self) -> AuditFlags:
        """

        :return:
        """
    @property
    def FileSystemRights(self) -> FileSystemRights:
        """

        :return:
        """
    @property
    def IdentityReference(self) -> IdentityReference:
        """

        :return:
        """
    @property
    def InheritanceFlags(self) -> InheritanceFlags:
        """

        :return:
        """
    @property
    def IsInherited(self) -> bool:
        """

        :return:
        """
    @property
    def PropagationFlags(self) -> PropagationFlags:
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

class FileSystemSecurity(ABC, NativeObjectSecurity):
    """"""

    @property
    def AccessRightType(self) -> Type:
        """

        :return:
        """
    @property
    def AccessRuleType(self) -> Type:
        """

        :return:
        """
    @property
    def AreAccessRulesCanonical(self) -> bool:
        """

        :return:
        """
    @property
    def AreAccessRulesProtected(self) -> bool:
        """

        :return:
        """
    @property
    def AreAuditRulesCanonical(self) -> bool:
        """

        :return:
        """
    @property
    def AreAuditRulesProtected(self) -> bool:
        """

        :return:
        """
    @property
    def AuditRuleType(self) -> Type:
        """

        :return:
        """
    def AccessRuleFactory(
        self,
        identityReference: IdentityReference,
        accessMask: int,
        isInherited: bool,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
        type: AccessControlType,
    ) -> AccessRule:
        """

        :param identityReference:
        :param accessMask:
        :param isInherited:
        :param inheritanceFlags:
        :param propagationFlags:
        :param type:
        :return:
        """
    def AddAccessRule(self, rule: FileSystemAccessRule) -> None:
        """

        :param rule:
        """
    def AddAuditRule(self, rule: FileSystemAuditRule) -> None:
        """

        :param rule:
        """
    def AuditRuleFactory(
        self,
        identityReference: IdentityReference,
        accessMask: int,
        isInherited: bool,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
        flags: AuditFlags,
    ) -> AuditRule:
        """

        :param identityReference:
        :param accessMask:
        :param isInherited:
        :param inheritanceFlags:
        :param propagationFlags:
        :param flags:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetAccessRules(
        self, includeExplicit: bool, includeInherited: bool, targetType: Type
    ) -> AuthorizationRuleCollection:
        """

        :param includeExplicit:
        :param includeInherited:
        :param targetType:
        :return:
        """
    def GetAuditRules(
        self, includeExplicit: bool, includeInherited: bool, targetType: Type
    ) -> AuthorizationRuleCollection:
        """

        :param includeExplicit:
        :param includeInherited:
        :param targetType:
        :return:
        """
    def GetGroup(self, targetType: Type) -> IdentityReference:
        """

        :param targetType:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetOwner(self, targetType: Type) -> IdentityReference:
        """

        :param targetType:
        :return:
        """
    def GetSecurityDescriptorBinaryForm(self) -> Array[int]:
        """

        :return:
        """
    def GetSecurityDescriptorSddlForm(self, includeSections: AccessControlSections) -> str:
        """

        :param includeSections:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ModifyAccessRule(
        self, modification: AccessControlModification, rule: AccessRule, modified: bool
    ) -> Tuple[bool, bool]:
        """

        :param modification:
        :param rule:
        :param modified:
        :return:
        """
    def ModifyAuditRule(
        self, modification: AccessControlModification, rule: AuditRule, modified: bool
    ) -> Tuple[bool, bool]:
        """

        :param modification:
        :param rule:
        :param modified:
        :return:
        """
    def PurgeAccessRules(self, identity: IdentityReference) -> None:
        """

        :param identity:
        """
    def PurgeAuditRules(self, identity: IdentityReference) -> None:
        """

        :param identity:
        """
    def RemoveAccessRule(self, rule: FileSystemAccessRule) -> bool:
        """

        :param rule:
        :return:
        """
    def RemoveAccessRuleAll(self, rule: FileSystemAccessRule) -> None:
        """

        :param rule:
        """
    def RemoveAccessRuleSpecific(self, rule: FileSystemAccessRule) -> None:
        """

        :param rule:
        """
    def RemoveAuditRule(self, rule: FileSystemAuditRule) -> bool:
        """

        :param rule:
        :return:
        """
    def RemoveAuditRuleAll(self, rule: FileSystemAuditRule) -> None:
        """

        :param rule:
        """
    def RemoveAuditRuleSpecific(self, rule: FileSystemAuditRule) -> None:
        """

        :param rule:
        """
    def ResetAccessRule(self, rule: FileSystemAccessRule) -> None:
        """

        :param rule:
        """
    def SetAccessRule(self, rule: FileSystemAccessRule) -> None:
        """

        :param rule:
        """
    def SetAccessRuleProtection(self, isProtected: bool, preserveInheritance: bool) -> None:
        """

        :param isProtected:
        :param preserveInheritance:
        """
    def SetAuditRule(self, rule: FileSystemAuditRule) -> None:
        """

        :param rule:
        """
    def SetAuditRuleProtection(self, isProtected: bool, preserveInheritance: bool) -> None:
        """

        :param isProtected:
        :param preserveInheritance:
        """
    def SetGroup(self, identity: IdentityReference) -> None:
        """

        :param identity:
        """
    def SetOwner(self, identity: IdentityReference) -> None:
        """

        :param identity:
        """
    @overload
    def SetSecurityDescriptorBinaryForm(self, binaryForm: Array[int]) -> None:
        """

        :param binaryForm:
        """
    @overload
    def SetSecurityDescriptorBinaryForm(
        self, binaryForm: Array[int], includeSections: AccessControlSections
    ) -> None:
        """

        :param binaryForm:
        :param includeSections:
        """
    @overload
    def SetSecurityDescriptorSddlForm(self, sddlForm: str) -> None:
        """

        :param sddlForm:
        """
    @overload
    def SetSecurityDescriptorSddlForm(
        self, sddlForm: str, includeSections: AccessControlSections
    ) -> None:
        """

        :param sddlForm:
        :param includeSections:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class GenericAce(ABC, Object):
    """"""

    @property
    def AceFlags(self) -> AceFlags:
        """

        :return:
        """
    @AceFlags.setter
    def AceFlags(self, value: AceFlags) -> None: ...
    @property
    def AceType(self) -> AceType:
        """

        :return:
        """
    @property
    def AuditFlags(self) -> AuditFlags:
        """

        :return:
        """
    @property
    def BinaryLength(self) -> int:
        """

        :return:
        """
    @property
    def InheritanceFlags(self) -> InheritanceFlags:
        """

        :return:
        """
    @property
    def IsInherited(self) -> bool:
        """

        :return:
        """
    @property
    def PropagationFlags(self) -> PropagationFlags:
        """

        :return:
        """
    def Copy(self) -> GenericAce:
        """

        :return:
        """
    @classmethod
    def CreateFromBinaryForm(cls, binaryForm: Array[int], offset: int) -> GenericAce:
        """

        :param binaryForm:
        :param offset:
        :return:
        """
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
    def ToString(self) -> str:
        """

        :return:
        """
    def __eq__(self, other: GenericAce) -> bool:
        """

        :param other:
        :return:
        """
    def __ne__(self, other: GenericAce) -> bool:
        """

        :param other:
        :return:
        """
    @classmethod
    def op_Equality(cls, left: GenericAce, right: GenericAce) -> bool:
        """

        :param left:
        :param right:
        :return:
        """
    @classmethod
    def op_Inequality(cls, left: GenericAce, right: GenericAce) -> bool:
        """

        :param left:
        :param right:
        :return:
        """

class GenericAcl(ABC, Object, ICollection, IEnumerable):
    """"""

    AclRevision: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    AclRevisionDS: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    MaxBinaryLength: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    @property
    def BinaryLength(self) -> int:
        """

        :return:
        """
    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def IsSynchronized(self) -> bool:
        """

        :return:
        """
    @property
    def Item(self) -> GenericAce:
        """

        :return:
        """
    @Item.setter
    def Item(self, value: GenericAce) -> None: ...
    @property
    def Revision(self) -> int:
        """

        :return:
        """
    @property
    def SyncRoot(self) -> object:
        """

        :return:
        """
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    @overload
    def CopyTo(self, array: Array[GenericAce], index: int) -> None:
        """

        :param array:
        :param index:
        """
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
    def ToString(self) -> str:
        """

        :return:
        """
    def __contains__(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    def __getitem__(self, index: int) -> GenericAce:
        """

        :param index:
        :return:
        """
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    def __len__(self) -> int:
        """

        :return:
        """
    def __setitem__(self, index: int, value: GenericAce) -> None:
        """

        :param index:
        :param value:
        """

class GenericSecurityDescriptor(ABC, Object):
    """"""

    @property
    def BinaryLength(self) -> int:
        """

        :return:
        """
    @property
    def ControlFlags(self) -> ControlFlags:
        """

        :return:
        """
    @property
    def Group(self) -> SecurityIdentifier:
        """

        :return:
        """
    @Group.setter
    def Group(self, value: SecurityIdentifier) -> None: ...
    @property
    def Owner(self) -> SecurityIdentifier:
        """

        :return:
        """
    @Owner.setter
    def Owner(self, value: SecurityIdentifier) -> None: ...
    @classmethod
    @property
    def Revision(cls) -> int:
        """

        :return:
        """
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
    def GetSddlForm(self, includeSections: AccessControlSections) -> str:
        """

        :param includeSections:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @classmethod
    def IsSddlConversionSupported(cls) -> bool:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class InheritanceFlags(Enum):
    """"""

    _None: InheritanceFlags = ...
    """"""
    ContainerInherit: InheritanceFlags = ...
    """"""
    ObjectInherit: InheritanceFlags = ...
    """"""

class KnownAce(ABC, GenericAce):
    """"""

    @property
    def AccessMask(self) -> int:
        """

        :return:
        """
    @AccessMask.setter
    def AccessMask(self, value: int) -> None: ...
    @property
    def AceFlags(self) -> AceFlags:
        """

        :return:
        """
    @AceFlags.setter
    def AceFlags(self, value: AceFlags) -> None: ...
    @property
    def AceType(self) -> AceType:
        """

        :return:
        """
    @property
    def AuditFlags(self) -> AuditFlags:
        """

        :return:
        """
    @property
    def BinaryLength(self) -> int:
        """

        :return:
        """
    @property
    def InheritanceFlags(self) -> InheritanceFlags:
        """

        :return:
        """
    @property
    def IsInherited(self) -> bool:
        """

        :return:
        """
    @property
    def PropagationFlags(self) -> PropagationFlags:
        """

        :return:
        """
    @property
    def SecurityIdentifier(self) -> SecurityIdentifier:
        """

        :return:
        """
    @SecurityIdentifier.setter
    def SecurityIdentifier(self, value: SecurityIdentifier) -> None: ...
    def Copy(self) -> GenericAce:
        """

        :return:
        """
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
    def ToString(self) -> str:
        """

        :return:
        """

class MutexAccessRule(AccessRule):
    """"""

    @overload
    def __init__(
        self, identity: IdentityReference, eventRights: MutexRights, type: AccessControlType
    ):
        """

        :param identity:
        :param eventRights:
        :param type:
        """
    @overload
    def __init__(self, identity: str, eventRights: MutexRights, type: AccessControlType):
        """

        :param identity:
        :param eventRights:
        :param type:
        """
    @property
    def AccessControlType(self) -> AccessControlType:
        """

        :return:
        """
    @property
    def IdentityReference(self) -> IdentityReference:
        """

        :return:
        """
    @property
    def InheritanceFlags(self) -> InheritanceFlags:
        """

        :return:
        """
    @property
    def IsInherited(self) -> bool:
        """

        :return:
        """
    @property
    def MutexRights(self) -> MutexRights:
        """

        :return:
        """
    @property
    def PropagationFlags(self) -> PropagationFlags:
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

class MutexAuditRule(AuditRule):
    """"""

    def __init__(self, identity: IdentityReference, eventRights: MutexRights, flags: AuditFlags):
        """

        :param identity:
        :param eventRights:
        :param flags:
        """
    @property
    def AuditFlags(self) -> AuditFlags:
        """

        :return:
        """
    @property
    def IdentityReference(self) -> IdentityReference:
        """

        :return:
        """
    @property
    def InheritanceFlags(self) -> InheritanceFlags:
        """

        :return:
        """
    @property
    def IsInherited(self) -> bool:
        """

        :return:
        """
    @property
    def MutexRights(self) -> MutexRights:
        """

        :return:
        """
    @property
    def PropagationFlags(self) -> PropagationFlags:
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

class MutexSecurity(NativeObjectSecurity):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, name: str, includeSections: AccessControlSections):
        """

        :param name:
        :param includeSections:
        """
    @property
    def AccessRightType(self) -> Type:
        """

        :return:
        """
    @property
    def AccessRuleType(self) -> Type:
        """

        :return:
        """
    @property
    def AreAccessRulesCanonical(self) -> bool:
        """

        :return:
        """
    @property
    def AreAccessRulesProtected(self) -> bool:
        """

        :return:
        """
    @property
    def AreAuditRulesCanonical(self) -> bool:
        """

        :return:
        """
    @property
    def AreAuditRulesProtected(self) -> bool:
        """

        :return:
        """
    @property
    def AuditRuleType(self) -> Type:
        """

        :return:
        """
    def AccessRuleFactory(
        self,
        identityReference: IdentityReference,
        accessMask: int,
        isInherited: bool,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
        type: AccessControlType,
    ) -> AccessRule:
        """

        :param identityReference:
        :param accessMask:
        :param isInherited:
        :param inheritanceFlags:
        :param propagationFlags:
        :param type:
        :return:
        """
    def AddAccessRule(self, rule: MutexAccessRule) -> None:
        """

        :param rule:
        """
    def AddAuditRule(self, rule: MutexAuditRule) -> None:
        """

        :param rule:
        """
    def AuditRuleFactory(
        self,
        identityReference: IdentityReference,
        accessMask: int,
        isInherited: bool,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
        flags: AuditFlags,
    ) -> AuditRule:
        """

        :param identityReference:
        :param accessMask:
        :param isInherited:
        :param inheritanceFlags:
        :param propagationFlags:
        :param flags:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetAccessRules(
        self, includeExplicit: bool, includeInherited: bool, targetType: Type
    ) -> AuthorizationRuleCollection:
        """

        :param includeExplicit:
        :param includeInherited:
        :param targetType:
        :return:
        """
    def GetAuditRules(
        self, includeExplicit: bool, includeInherited: bool, targetType: Type
    ) -> AuthorizationRuleCollection:
        """

        :param includeExplicit:
        :param includeInherited:
        :param targetType:
        :return:
        """
    def GetGroup(self, targetType: Type) -> IdentityReference:
        """

        :param targetType:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetOwner(self, targetType: Type) -> IdentityReference:
        """

        :param targetType:
        :return:
        """
    def GetSecurityDescriptorBinaryForm(self) -> Array[int]:
        """

        :return:
        """
    def GetSecurityDescriptorSddlForm(self, includeSections: AccessControlSections) -> str:
        """

        :param includeSections:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ModifyAccessRule(
        self, modification: AccessControlModification, rule: AccessRule, modified: bool
    ) -> Tuple[bool, bool]:
        """

        :param modification:
        :param rule:
        :param modified:
        :return:
        """
    def ModifyAuditRule(
        self, modification: AccessControlModification, rule: AuditRule, modified: bool
    ) -> Tuple[bool, bool]:
        """

        :param modification:
        :param rule:
        :param modified:
        :return:
        """
    def PurgeAccessRules(self, identity: IdentityReference) -> None:
        """

        :param identity:
        """
    def PurgeAuditRules(self, identity: IdentityReference) -> None:
        """

        :param identity:
        """
    def RemoveAccessRule(self, rule: MutexAccessRule) -> bool:
        """

        :param rule:
        :return:
        """
    def RemoveAccessRuleAll(self, rule: MutexAccessRule) -> None:
        """

        :param rule:
        """
    def RemoveAccessRuleSpecific(self, rule: MutexAccessRule) -> None:
        """

        :param rule:
        """
    def RemoveAuditRule(self, rule: MutexAuditRule) -> bool:
        """

        :param rule:
        :return:
        """
    def RemoveAuditRuleAll(self, rule: MutexAuditRule) -> None:
        """

        :param rule:
        """
    def RemoveAuditRuleSpecific(self, rule: MutexAuditRule) -> None:
        """

        :param rule:
        """
    def ResetAccessRule(self, rule: MutexAccessRule) -> None:
        """

        :param rule:
        """
    def SetAccessRule(self, rule: MutexAccessRule) -> None:
        """

        :param rule:
        """
    def SetAccessRuleProtection(self, isProtected: bool, preserveInheritance: bool) -> None:
        """

        :param isProtected:
        :param preserveInheritance:
        """
    def SetAuditRule(self, rule: MutexAuditRule) -> None:
        """

        :param rule:
        """
    def SetAuditRuleProtection(self, isProtected: bool, preserveInheritance: bool) -> None:
        """

        :param isProtected:
        :param preserveInheritance:
        """
    def SetGroup(self, identity: IdentityReference) -> None:
        """

        :param identity:
        """
    def SetOwner(self, identity: IdentityReference) -> None:
        """

        :param identity:
        """
    @overload
    def SetSecurityDescriptorBinaryForm(self, binaryForm: Array[int]) -> None:
        """

        :param binaryForm:
        """
    @overload
    def SetSecurityDescriptorBinaryForm(
        self, binaryForm: Array[int], includeSections: AccessControlSections
    ) -> None:
        """

        :param binaryForm:
        :param includeSections:
        """
    @overload
    def SetSecurityDescriptorSddlForm(self, sddlForm: str) -> None:
        """

        :param sddlForm:
        """
    @overload
    def SetSecurityDescriptorSddlForm(
        self, sddlForm: str, includeSections: AccessControlSections
    ) -> None:
        """

        :param sddlForm:
        :param includeSections:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class NativeObjectSecurity(ABC, CommonObjectSecurity):
    """"""

    @property
    def AccessRightType(self) -> Type:
        """

        :return:
        """
    @property
    def AccessRuleType(self) -> Type:
        """

        :return:
        """
    @property
    def AreAccessRulesCanonical(self) -> bool:
        """

        :return:
        """
    @property
    def AreAccessRulesProtected(self) -> bool:
        """

        :return:
        """
    @property
    def AreAuditRulesCanonical(self) -> bool:
        """

        :return:
        """
    @property
    def AreAuditRulesProtected(self) -> bool:
        """

        :return:
        """
    @property
    def AuditRuleType(self) -> Type:
        """

        :return:
        """
    def AccessRuleFactory(
        self,
        identityReference: IdentityReference,
        accessMask: int,
        isInherited: bool,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
        type: AccessControlType,
    ) -> AccessRule:
        """

        :param identityReference:
        :param accessMask:
        :param isInherited:
        :param inheritanceFlags:
        :param propagationFlags:
        :param type:
        :return:
        """
    def AuditRuleFactory(
        self,
        identityReference: IdentityReference,
        accessMask: int,
        isInherited: bool,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
        flags: AuditFlags,
    ) -> AuditRule:
        """

        :param identityReference:
        :param accessMask:
        :param isInherited:
        :param inheritanceFlags:
        :param propagationFlags:
        :param flags:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetAccessRules(
        self, includeExplicit: bool, includeInherited: bool, targetType: Type
    ) -> AuthorizationRuleCollection:
        """

        :param includeExplicit:
        :param includeInherited:
        :param targetType:
        :return:
        """
    def GetAuditRules(
        self, includeExplicit: bool, includeInherited: bool, targetType: Type
    ) -> AuthorizationRuleCollection:
        """

        :param includeExplicit:
        :param includeInherited:
        :param targetType:
        :return:
        """
    def GetGroup(self, targetType: Type) -> IdentityReference:
        """

        :param targetType:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetOwner(self, targetType: Type) -> IdentityReference:
        """

        :param targetType:
        :return:
        """
    def GetSecurityDescriptorBinaryForm(self) -> Array[int]:
        """

        :return:
        """
    def GetSecurityDescriptorSddlForm(self, includeSections: AccessControlSections) -> str:
        """

        :param includeSections:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ModifyAccessRule(
        self, modification: AccessControlModification, rule: AccessRule, modified: bool
    ) -> Tuple[bool, bool]:
        """

        :param modification:
        :param rule:
        :param modified:
        :return:
        """
    def ModifyAuditRule(
        self, modification: AccessControlModification, rule: AuditRule, modified: bool
    ) -> Tuple[bool, bool]:
        """

        :param modification:
        :param rule:
        :param modified:
        :return:
        """
    def PurgeAccessRules(self, identity: IdentityReference) -> None:
        """

        :param identity:
        """
    def PurgeAuditRules(self, identity: IdentityReference) -> None:
        """

        :param identity:
        """
    def SetAccessRuleProtection(self, isProtected: bool, preserveInheritance: bool) -> None:
        """

        :param isProtected:
        :param preserveInheritance:
        """
    def SetAuditRuleProtection(self, isProtected: bool, preserveInheritance: bool) -> None:
        """

        :param isProtected:
        :param preserveInheritance:
        """
    def SetGroup(self, identity: IdentityReference) -> None:
        """

        :param identity:
        """
    def SetOwner(self, identity: IdentityReference) -> None:
        """

        :param identity:
        """
    @overload
    def SetSecurityDescriptorBinaryForm(self, binaryForm: Array[int]) -> None:
        """

        :param binaryForm:
        """
    @overload
    def SetSecurityDescriptorBinaryForm(
        self, binaryForm: Array[int], includeSections: AccessControlSections
    ) -> None:
        """

        :param binaryForm:
        :param includeSections:
        """
    @overload
    def SetSecurityDescriptorSddlForm(self, sddlForm: str) -> None:
        """

        :param sddlForm:
        """
    @overload
    def SetSecurityDescriptorSddlForm(
        self, sddlForm: str, includeSections: AccessControlSections
    ) -> None:
        """

        :param sddlForm:
        :param includeSections:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class ObjectAccessRule(ABC, AccessRule):
    """"""

    @property
    def AccessControlType(self) -> AccessControlType:
        """

        :return:
        """
    @property
    def IdentityReference(self) -> IdentityReference:
        """

        :return:
        """
    @property
    def InheritanceFlags(self) -> InheritanceFlags:
        """

        :return:
        """
    @property
    def InheritedObjectType(self) -> Guid:
        """

        :return:
        """
    @property
    def IsInherited(self) -> bool:
        """

        :return:
        """
    @property
    def ObjectFlags(self) -> ObjectAceFlags:
        """

        :return:
        """
    @property
    def ObjectType(self) -> Guid:
        """

        :return:
        """
    @property
    def PropagationFlags(self) -> PropagationFlags:
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
    ):
        """

        :param aceFlags:
        :param qualifier:
        :param accessMask:
        :param sid:
        :param flags:
        :param type:
        :param inheritedType:
        :param isCallback:
        :param opaque:
        """
    @property
    def AccessMask(self) -> int:
        """

        :return:
        """
    @AccessMask.setter
    def AccessMask(self, value: int) -> None: ...
    @property
    def AceFlags(self) -> AceFlags:
        """

        :return:
        """
    @AceFlags.setter
    def AceFlags(self, value: AceFlags) -> None: ...
    @property
    def AceQualifier(self) -> AceQualifier:
        """

        :return:
        """
    @property
    def AceType(self) -> AceType:
        """

        :return:
        """
    @property
    def AuditFlags(self) -> AuditFlags:
        """

        :return:
        """
    @property
    def BinaryLength(self) -> int:
        """

        :return:
        """
    @property
    def InheritanceFlags(self) -> InheritanceFlags:
        """

        :return:
        """
    @property
    def InheritedObjectAceType(self) -> Guid:
        """

        :return:
        """
    @InheritedObjectAceType.setter
    def InheritedObjectAceType(self, value: Guid) -> None: ...
    @property
    def IsCallback(self) -> bool:
        """

        :return:
        """
    @property
    def IsInherited(self) -> bool:
        """

        :return:
        """
    @property
    def ObjectAceFlags(self) -> ObjectAceFlags:
        """

        :return:
        """
    @ObjectAceFlags.setter
    def ObjectAceFlags(self, value: ObjectAceFlags) -> None: ...
    @property
    def ObjectAceType(self) -> Guid:
        """

        :return:
        """
    @ObjectAceType.setter
    def ObjectAceType(self, value: Guid) -> None: ...
    @property
    def OpaqueLength(self) -> int:
        """

        :return:
        """
    @property
    def PropagationFlags(self) -> PropagationFlags:
        """

        :return:
        """
    @property
    def SecurityIdentifier(self) -> SecurityIdentifier:
        """

        :return:
        """
    @SecurityIdentifier.setter
    def SecurityIdentifier(self, value: SecurityIdentifier) -> None: ...
    def Copy(self) -> GenericAce:
        """

        :return:
        """
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
    def GetOpaque(self) -> Array[int]:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @classmethod
    def MaxOpaqueLength(cls, isCallback: bool) -> int:
        """

        :param isCallback:
        :return:
        """
    def SetOpaque(self, opaque: Array[int]) -> None:
        """

        :param opaque:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class ObjectAceFlags(Enum):
    """"""

    _None: ObjectAceFlags = ...
    """"""
    ObjectAceTypePresent: ObjectAceFlags = ...
    """"""
    InheritedObjectAceTypePresent: ObjectAceFlags = ...
    """"""

class ObjectAuditRule(ABC, AuditRule):
    """"""

    @property
    def AuditFlags(self) -> AuditFlags:
        """

        :return:
        """
    @property
    def IdentityReference(self) -> IdentityReference:
        """

        :return:
        """
    @property
    def InheritanceFlags(self) -> InheritanceFlags:
        """

        :return:
        """
    @property
    def InheritedObjectType(self) -> Guid:
        """

        :return:
        """
    @property
    def IsInherited(self) -> bool:
        """

        :return:
        """
    @property
    def ObjectFlags(self) -> ObjectAceFlags:
        """

        :return:
        """
    @property
    def ObjectType(self) -> Guid:
        """

        :return:
        """
    @property
    def PropagationFlags(self) -> PropagationFlags:
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

class ObjectSecurity(ABC, Object):
    """"""

    @property
    def AccessRightType(self) -> Type:
        """

        :return:
        """
    @property
    def AccessRuleType(self) -> Type:
        """

        :return:
        """
    @property
    def AreAccessRulesCanonical(self) -> bool:
        """

        :return:
        """
    @property
    def AreAccessRulesProtected(self) -> bool:
        """

        :return:
        """
    @property
    def AreAuditRulesCanonical(self) -> bool:
        """

        :return:
        """
    @property
    def AreAuditRulesProtected(self) -> bool:
        """

        :return:
        """
    @property
    def AuditRuleType(self) -> Type:
        """

        :return:
        """
    def AccessRuleFactory(
        self,
        identityReference: IdentityReference,
        accessMask: int,
        isInherited: bool,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
        type: AccessControlType,
    ) -> AccessRule:
        """

        :param identityReference:
        :param accessMask:
        :param isInherited:
        :param inheritanceFlags:
        :param propagationFlags:
        :param type:
        :return:
        """
    def AuditRuleFactory(
        self,
        identityReference: IdentityReference,
        accessMask: int,
        isInherited: bool,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
        flags: AuditFlags,
    ) -> AuditRule:
        """

        :param identityReference:
        :param accessMask:
        :param isInherited:
        :param inheritanceFlags:
        :param propagationFlags:
        :param flags:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetGroup(self, targetType: Type) -> IdentityReference:
        """

        :param targetType:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetOwner(self, targetType: Type) -> IdentityReference:
        """

        :param targetType:
        :return:
        """
    def GetSecurityDescriptorBinaryForm(self) -> Array[int]:
        """

        :return:
        """
    def GetSecurityDescriptorSddlForm(self, includeSections: AccessControlSections) -> str:
        """

        :param includeSections:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @classmethod
    def IsSddlConversionSupported(cls) -> bool:
        """

        :return:
        """
    def ModifyAccessRule(
        self, modification: AccessControlModification, rule: AccessRule, modified: bool
    ) -> Tuple[bool, bool]:
        """

        :param modification:
        :param rule:
        :param modified:
        :return:
        """
    def ModifyAuditRule(
        self, modification: AccessControlModification, rule: AuditRule, modified: bool
    ) -> Tuple[bool, bool]:
        """

        :param modification:
        :param rule:
        :param modified:
        :return:
        """
    def PurgeAccessRules(self, identity: IdentityReference) -> None:
        """

        :param identity:
        """
    def PurgeAuditRules(self, identity: IdentityReference) -> None:
        """

        :param identity:
        """
    def SetAccessRuleProtection(self, isProtected: bool, preserveInheritance: bool) -> None:
        """

        :param isProtected:
        :param preserveInheritance:
        """
    def SetAuditRuleProtection(self, isProtected: bool, preserveInheritance: bool) -> None:
        """

        :param isProtected:
        :param preserveInheritance:
        """
    def SetGroup(self, identity: IdentityReference) -> None:
        """

        :param identity:
        """
    def SetOwner(self, identity: IdentityReference) -> None:
        """

        :param identity:
        """
    @overload
    def SetSecurityDescriptorBinaryForm(self, binaryForm: Array[int]) -> None:
        """

        :param binaryForm:
        """
    @overload
    def SetSecurityDescriptorBinaryForm(
        self, binaryForm: Array[int], includeSections: AccessControlSections
    ) -> None:
        """

        :param binaryForm:
        :param includeSections:
        """
    @overload
    def SetSecurityDescriptorSddlForm(self, sddlForm: str) -> None:
        """

        :param sddlForm:
        """
    @overload
    def SetSecurityDescriptorSddlForm(
        self, sddlForm: str, includeSections: AccessControlSections
    ) -> None:
        """

        :param sddlForm:
        :param includeSections:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class ObjectSecurity(ABC, Generic[T], NativeObjectSecurity):
    """"""

    @property
    def AccessRightType(self) -> Type:
        """

        :return:
        """
    @property
    def AccessRuleType(self) -> Type:
        """

        :return:
        """
    @property
    def AreAccessRulesCanonical(self) -> bool:
        """

        :return:
        """
    @property
    def AreAccessRulesProtected(self) -> bool:
        """

        :return:
        """
    @property
    def AreAuditRulesCanonical(self) -> bool:
        """

        :return:
        """
    @property
    def AreAuditRulesProtected(self) -> bool:
        """

        :return:
        """
    @property
    def AuditRuleType(self) -> Type:
        """

        :return:
        """
    def AccessRuleFactory(
        self,
        identityReference: IdentityReference,
        accessMask: int,
        isInherited: bool,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
        type: AccessControlType,
    ) -> AccessRule:
        """

        :param identityReference:
        :param accessMask:
        :param isInherited:
        :param inheritanceFlags:
        :param propagationFlags:
        :param type:
        :return:
        """
    def AddAccessRule(self, rule: AccessRule[T]) -> None:
        """

        :param rule:
        """
    def AddAuditRule(self, rule: AuditRule[T]) -> None:
        """

        :param rule:
        """
    def AuditRuleFactory(
        self,
        identityReference: IdentityReference,
        accessMask: int,
        isInherited: bool,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
        flags: AuditFlags,
    ) -> AuditRule:
        """

        :param identityReference:
        :param accessMask:
        :param isInherited:
        :param inheritanceFlags:
        :param propagationFlags:
        :param flags:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetAccessRules(
        self, includeExplicit: bool, includeInherited: bool, targetType: Type
    ) -> AuthorizationRuleCollection:
        """

        :param includeExplicit:
        :param includeInherited:
        :param targetType:
        :return:
        """
    def GetAuditRules(
        self, includeExplicit: bool, includeInherited: bool, targetType: Type
    ) -> AuthorizationRuleCollection:
        """

        :param includeExplicit:
        :param includeInherited:
        :param targetType:
        :return:
        """
    def GetGroup(self, targetType: Type) -> IdentityReference:
        """

        :param targetType:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetOwner(self, targetType: Type) -> IdentityReference:
        """

        :param targetType:
        :return:
        """
    def GetSecurityDescriptorBinaryForm(self) -> Array[int]:
        """

        :return:
        """
    def GetSecurityDescriptorSddlForm(self, includeSections: AccessControlSections) -> str:
        """

        :param includeSections:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ModifyAccessRule(
        self, modification: AccessControlModification, rule: AccessRule, modified: bool
    ) -> Tuple[bool, bool]:
        """

        :param modification:
        :param rule:
        :param modified:
        :return:
        """
    def ModifyAuditRule(
        self, modification: AccessControlModification, rule: AuditRule, modified: bool
    ) -> Tuple[bool, bool]:
        """

        :param modification:
        :param rule:
        :param modified:
        :return:
        """
    def PurgeAccessRules(self, identity: IdentityReference) -> None:
        """

        :param identity:
        """
    def PurgeAuditRules(self, identity: IdentityReference) -> None:
        """

        :param identity:
        """
    def RemoveAccessRule(self, rule: AccessRule[T]) -> bool:
        """

        :param rule:
        :return:
        """
    def RemoveAccessRuleAll(self, rule: AccessRule[T]) -> None:
        """

        :param rule:
        """
    def RemoveAccessRuleSpecific(self, rule: AccessRule[T]) -> None:
        """

        :param rule:
        """
    def RemoveAuditRule(self, rule: AuditRule[T]) -> bool:
        """

        :param rule:
        :return:
        """
    def RemoveAuditRuleAll(self, rule: AuditRule[T]) -> None:
        """

        :param rule:
        """
    def RemoveAuditRuleSpecific(self, rule: AuditRule[T]) -> None:
        """

        :param rule:
        """
    def ResetAccessRule(self, rule: AccessRule[T]) -> None:
        """

        :param rule:
        """
    def SetAccessRule(self, rule: AccessRule[T]) -> None:
        """

        :param rule:
        """
    def SetAccessRuleProtection(self, isProtected: bool, preserveInheritance: bool) -> None:
        """

        :param isProtected:
        :param preserveInheritance:
        """
    def SetAuditRule(self, rule: AuditRule[T]) -> None:
        """

        :param rule:
        """
    def SetAuditRuleProtection(self, isProtected: bool, preserveInheritance: bool) -> None:
        """

        :param isProtected:
        :param preserveInheritance:
        """
    def SetGroup(self, identity: IdentityReference) -> None:
        """

        :param identity:
        """
    def SetOwner(self, identity: IdentityReference) -> None:
        """

        :param identity:
        """
    @overload
    def SetSecurityDescriptorBinaryForm(self, binaryForm: Array[int]) -> None:
        """

        :param binaryForm:
        """
    @overload
    def SetSecurityDescriptorBinaryForm(
        self, binaryForm: Array[int], includeSections: AccessControlSections
    ) -> None:
        """

        :param binaryForm:
        :param includeSections:
        """
    @overload
    def SetSecurityDescriptorSddlForm(self, sddlForm: str) -> None:
        """

        :param sddlForm:
        """
    @overload
    def SetSecurityDescriptorSddlForm(
        self, sddlForm: str, includeSections: AccessControlSections
    ) -> None:
        """

        :param sddlForm:
        :param includeSections:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class Privilege(Object):
    """"""

    AssignPrimaryToken: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Audit: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Backup: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    ChangeNotify: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    CreateGlobal: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    CreatePageFile: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    CreatePermanent: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    CreateToken: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Debug: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    EnableDelegation: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Impersonate: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    IncreaseBasePriority: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    IncreaseQuota: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    LoadDriver: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    LockMemory: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    MachineAccount: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    ManageVolume: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    ProfileSingleProcess: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    RemoteShutdown: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    ReserveProcessor: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Restore: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Security: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Shutdown: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    SyncAgent: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    SystemEnvironment: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    SystemProfile: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    SystemTime: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    TakeOwnership: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    TrustedComputingBase: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    TrustedCredentialManagerAccess: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Undock: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    UnsolicitedInput: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    def __init__(self, privilegeName: str):
        """

        :param privilegeName:
        """
    @property
    def NeedToRevert(self) -> bool:
        """

        :return:
        """
    def Enable(self) -> None:
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
    def Revert(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class PrivilegeNotHeldException(UnauthorizedAccessException, _Exception, ISerializable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, privilege: str):
        """

        :param privilege:
        """
    @overload
    def __init__(self, privilege: str, inner: Exception):
        """

        :param privilege:
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
    def PrivilegeName(self) -> str:
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

class PropagationFlags(Enum):
    """"""

    _None: PropagationFlags = ...
    """"""
    NoPropagateInherit: PropagationFlags = ...
    """"""
    InheritOnly: PropagationFlags = ...
    """"""

class QualifiedAce(ABC, KnownAce):
    """"""

    @property
    def AccessMask(self) -> int:
        """

        :return:
        """
    @AccessMask.setter
    def AccessMask(self, value: int) -> None: ...
    @property
    def AceFlags(self) -> AceFlags:
        """

        :return:
        """
    @AceFlags.setter
    def AceFlags(self, value: AceFlags) -> None: ...
    @property
    def AceQualifier(self) -> AceQualifier:
        """

        :return:
        """
    @property
    def AceType(self) -> AceType:
        """

        :return:
        """
    @property
    def AuditFlags(self) -> AuditFlags:
        """

        :return:
        """
    @property
    def BinaryLength(self) -> int:
        """

        :return:
        """
    @property
    def InheritanceFlags(self) -> InheritanceFlags:
        """

        :return:
        """
    @property
    def IsCallback(self) -> bool:
        """

        :return:
        """
    @property
    def IsInherited(self) -> bool:
        """

        :return:
        """
    @property
    def OpaqueLength(self) -> int:
        """

        :return:
        """
    @property
    def PropagationFlags(self) -> PropagationFlags:
        """

        :return:
        """
    @property
    def SecurityIdentifier(self) -> SecurityIdentifier:
        """

        :return:
        """
    @SecurityIdentifier.setter
    def SecurityIdentifier(self, value: SecurityIdentifier) -> None: ...
    def Copy(self) -> GenericAce:
        """

        :return:
        """
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
    def GetOpaque(self) -> Array[int]:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def SetOpaque(self, opaque: Array[int]) -> None:
        """

        :param opaque:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class RawAcl(GenericAcl, ICollection, IEnumerable):
    """"""

    @overload
    def __init__(self, binaryForm: Array[int], offset: int):
        """

        :param binaryForm:
        :param offset:
        """
    @overload
    def __init__(self, revision: int, capacity: int):
        """

        :param revision:
        :param capacity:
        """
    @property
    def BinaryLength(self) -> int:
        """

        :return:
        """
    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def IsSynchronized(self) -> bool:
        """

        :return:
        """
    @property
    def Item(self) -> GenericAce:
        """

        :return:
        """
    @Item.setter
    def Item(self, value: GenericAce) -> None: ...
    @property
    def Revision(self) -> int:
        """

        :return:
        """
    @property
    def SyncRoot(self) -> object:
        """

        :return:
        """
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    @overload
    def CopyTo(self, array: Array[GenericAce], index: int) -> None:
        """

        :param array:
        :param index:
        """
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
    def InsertAce(self, index: int, ace: GenericAce) -> None:
        """

        :param index:
        :param ace:
        """
    def RemoveAce(self, index: int) -> None:
        """

        :param index:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def __contains__(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    def __getitem__(self, index: int) -> GenericAce:
        """

        :param index:
        :return:
        """
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    def __len__(self) -> int:
        """

        :return:
        """
    def __setitem__(self, index: int, value: GenericAce) -> None:
        """

        :param index:
        :param value:
        """

class RawSecurityDescriptor(GenericSecurityDescriptor):
    """"""

    @overload
    def __init__(self, sddlForm: str):
        """

        :param sddlForm:
        """
    @overload
    def __init__(self, binaryForm: Array[int], offset: int):
        """

        :param binaryForm:
        :param offset:
        """
    @overload
    def __init__(
        self,
        flags: ControlFlags,
        owner: SecurityIdentifier,
        group: SecurityIdentifier,
        systemAcl: RawAcl,
        discretionaryAcl: RawAcl,
    ):
        """

        :param flags:
        :param owner:
        :param group:
        :param systemAcl:
        :param discretionaryAcl:
        """
    @property
    def BinaryLength(self) -> int:
        """

        :return:
        """
    @property
    def ControlFlags(self) -> ControlFlags:
        """

        :return:
        """
    @property
    def DiscretionaryAcl(self) -> RawAcl:
        """

        :return:
        """
    @DiscretionaryAcl.setter
    def DiscretionaryAcl(self, value: RawAcl) -> None: ...
    @property
    def Group(self) -> SecurityIdentifier:
        """

        :return:
        """
    @Group.setter
    def Group(self, value: SecurityIdentifier) -> None: ...
    @property
    def Owner(self) -> SecurityIdentifier:
        """

        :return:
        """
    @Owner.setter
    def Owner(self, value: SecurityIdentifier) -> None: ...
    @property
    def ResourceManagerControl(self) -> int:
        """

        :return:
        """
    @ResourceManagerControl.setter
    def ResourceManagerControl(self, value: int) -> None: ...
    @classmethod
    @property
    def Revision(cls) -> int:
        """

        :return:
        """
    @property
    def SystemAcl(self) -> RawAcl:
        """

        :return:
        """
    @SystemAcl.setter
    def SystemAcl(self, value: RawAcl) -> None: ...
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
    def GetSddlForm(self, includeSections: AccessControlSections) -> str:
        """

        :param includeSections:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def SetFlags(self, flags: ControlFlags) -> None:
        """

        :param flags:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class RegistryAccessRule(AccessRule):
    """"""

    @overload
    def __init__(
        self, identity: IdentityReference, registryRights: RegistryRights, type: AccessControlType
    ):
        """

        :param identity:
        :param registryRights:
        :param type:
        """
    @overload
    def __init__(self, identity: str, registryRights: RegistryRights, type: AccessControlType):
        """

        :param identity:
        :param registryRights:
        :param type:
        """
    @overload
    def __init__(
        self,
        identity: IdentityReference,
        registryRights: RegistryRights,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
        type: AccessControlType,
    ):
        """

        :param identity:
        :param registryRights:
        :param inheritanceFlags:
        :param propagationFlags:
        :param type:
        """
    @overload
    def __init__(
        self,
        identity: str,
        registryRights: RegistryRights,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
        type: AccessControlType,
    ):
        """

        :param identity:
        :param registryRights:
        :param inheritanceFlags:
        :param propagationFlags:
        :param type:
        """
    @property
    def AccessControlType(self) -> AccessControlType:
        """

        :return:
        """
    @property
    def IdentityReference(self) -> IdentityReference:
        """

        :return:
        """
    @property
    def InheritanceFlags(self) -> InheritanceFlags:
        """

        :return:
        """
    @property
    def IsInherited(self) -> bool:
        """

        :return:
        """
    @property
    def PropagationFlags(self) -> PropagationFlags:
        """

        :return:
        """
    @property
    def RegistryRights(self) -> RegistryRights:
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
    ):
        """

        :param identity:
        :param registryRights:
        :param inheritanceFlags:
        :param propagationFlags:
        :param flags:
        """
    @overload
    def __init__(
        self,
        identity: str,
        registryRights: RegistryRights,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
        flags: AuditFlags,
    ):
        """

        :param identity:
        :param registryRights:
        :param inheritanceFlags:
        :param propagationFlags:
        :param flags:
        """
    @property
    def AuditFlags(self) -> AuditFlags:
        """

        :return:
        """
    @property
    def IdentityReference(self) -> IdentityReference:
        """

        :return:
        """
    @property
    def InheritanceFlags(self) -> InheritanceFlags:
        """

        :return:
        """
    @property
    def IsInherited(self) -> bool:
        """

        :return:
        """
    @property
    def PropagationFlags(self) -> PropagationFlags:
        """

        :return:
        """
    @property
    def RegistryRights(self) -> RegistryRights:
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

class RegistrySecurity(NativeObjectSecurity):
    """"""

    def __init__(self):
        """"""
    @property
    def AccessRightType(self) -> Type:
        """

        :return:
        """
    @property
    def AccessRuleType(self) -> Type:
        """

        :return:
        """
    @property
    def AreAccessRulesCanonical(self) -> bool:
        """

        :return:
        """
    @property
    def AreAccessRulesProtected(self) -> bool:
        """

        :return:
        """
    @property
    def AreAuditRulesCanonical(self) -> bool:
        """

        :return:
        """
    @property
    def AreAuditRulesProtected(self) -> bool:
        """

        :return:
        """
    @property
    def AuditRuleType(self) -> Type:
        """

        :return:
        """
    def AccessRuleFactory(
        self,
        identityReference: IdentityReference,
        accessMask: int,
        isInherited: bool,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
        type: AccessControlType,
    ) -> AccessRule:
        """

        :param identityReference:
        :param accessMask:
        :param isInherited:
        :param inheritanceFlags:
        :param propagationFlags:
        :param type:
        :return:
        """
    def AddAccessRule(self, rule: RegistryAccessRule) -> None:
        """

        :param rule:
        """
    def AddAuditRule(self, rule: RegistryAuditRule) -> None:
        """

        :param rule:
        """
    def AuditRuleFactory(
        self,
        identityReference: IdentityReference,
        accessMask: int,
        isInherited: bool,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
        flags: AuditFlags,
    ) -> AuditRule:
        """

        :param identityReference:
        :param accessMask:
        :param isInherited:
        :param inheritanceFlags:
        :param propagationFlags:
        :param flags:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetAccessRules(
        self, includeExplicit: bool, includeInherited: bool, targetType: Type
    ) -> AuthorizationRuleCollection:
        """

        :param includeExplicit:
        :param includeInherited:
        :param targetType:
        :return:
        """
    def GetAuditRules(
        self, includeExplicit: bool, includeInherited: bool, targetType: Type
    ) -> AuthorizationRuleCollection:
        """

        :param includeExplicit:
        :param includeInherited:
        :param targetType:
        :return:
        """
    def GetGroup(self, targetType: Type) -> IdentityReference:
        """

        :param targetType:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetOwner(self, targetType: Type) -> IdentityReference:
        """

        :param targetType:
        :return:
        """
    def GetSecurityDescriptorBinaryForm(self) -> Array[int]:
        """

        :return:
        """
    def GetSecurityDescriptorSddlForm(self, includeSections: AccessControlSections) -> str:
        """

        :param includeSections:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ModifyAccessRule(
        self, modification: AccessControlModification, rule: AccessRule, modified: bool
    ) -> Tuple[bool, bool]:
        """

        :param modification:
        :param rule:
        :param modified:
        :return:
        """
    def ModifyAuditRule(
        self, modification: AccessControlModification, rule: AuditRule, modified: bool
    ) -> Tuple[bool, bool]:
        """

        :param modification:
        :param rule:
        :param modified:
        :return:
        """
    def PurgeAccessRules(self, identity: IdentityReference) -> None:
        """

        :param identity:
        """
    def PurgeAuditRules(self, identity: IdentityReference) -> None:
        """

        :param identity:
        """
    def RemoveAccessRule(self, rule: RegistryAccessRule) -> bool:
        """

        :param rule:
        :return:
        """
    def RemoveAccessRuleAll(self, rule: RegistryAccessRule) -> None:
        """

        :param rule:
        """
    def RemoveAccessRuleSpecific(self, rule: RegistryAccessRule) -> None:
        """

        :param rule:
        """
    def RemoveAuditRule(self, rule: RegistryAuditRule) -> bool:
        """

        :param rule:
        :return:
        """
    def RemoveAuditRuleAll(self, rule: RegistryAuditRule) -> None:
        """

        :param rule:
        """
    def RemoveAuditRuleSpecific(self, rule: RegistryAuditRule) -> None:
        """

        :param rule:
        """
    def ResetAccessRule(self, rule: RegistryAccessRule) -> None:
        """

        :param rule:
        """
    def SetAccessRule(self, rule: RegistryAccessRule) -> None:
        """

        :param rule:
        """
    def SetAccessRuleProtection(self, isProtected: bool, preserveInheritance: bool) -> None:
        """

        :param isProtected:
        :param preserveInheritance:
        """
    def SetAuditRule(self, rule: RegistryAuditRule) -> None:
        """

        :param rule:
        """
    def SetAuditRuleProtection(self, isProtected: bool, preserveInheritance: bool) -> None:
        """

        :param isProtected:
        :param preserveInheritance:
        """
    def SetGroup(self, identity: IdentityReference) -> None:
        """

        :param identity:
        """
    def SetOwner(self, identity: IdentityReference) -> None:
        """

        :param identity:
        """
    @overload
    def SetSecurityDescriptorBinaryForm(self, binaryForm: Array[int]) -> None:
        """

        :param binaryForm:
        """
    @overload
    def SetSecurityDescriptorBinaryForm(
        self, binaryForm: Array[int], includeSections: AccessControlSections
    ) -> None:
        """

        :param binaryForm:
        :param includeSections:
        """
    @overload
    def SetSecurityDescriptorSddlForm(self, sddlForm: str) -> None:
        """

        :param sddlForm:
        """
    @overload
    def SetSecurityDescriptorSddlForm(
        self, sddlForm: str, includeSections: AccessControlSections
    ) -> None:
        """

        :param sddlForm:
        :param includeSections:
        """
    def ToString(self) -> str:
        """

        :return:
        """

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

class SemaphoreAccessRule(AccessRule):
    """"""

    @overload
    def __init__(
        self, identity: IdentityReference, eventRights: SemaphoreRights, type: AccessControlType
    ):
        """

        :param identity:
        :param eventRights:
        :param type:
        """
    @overload
    def __init__(self, identity: str, eventRights: SemaphoreRights, type: AccessControlType):
        """

        :param identity:
        :param eventRights:
        :param type:
        """
    @property
    def AccessControlType(self) -> AccessControlType:
        """

        :return:
        """
    @property
    def IdentityReference(self) -> IdentityReference:
        """

        :return:
        """
    @property
    def InheritanceFlags(self) -> InheritanceFlags:
        """

        :return:
        """
    @property
    def IsInherited(self) -> bool:
        """

        :return:
        """
    @property
    def PropagationFlags(self) -> PropagationFlags:
        """

        :return:
        """
    @property
    def SemaphoreRights(self) -> SemaphoreRights:
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

class SemaphoreAuditRule(AuditRule):
    """"""

    def __init__(
        self, identity: IdentityReference, eventRights: SemaphoreRights, flags: AuditFlags
    ):
        """

        :param identity:
        :param eventRights:
        :param flags:
        """
    @property
    def AuditFlags(self) -> AuditFlags:
        """

        :return:
        """
    @property
    def IdentityReference(self) -> IdentityReference:
        """

        :return:
        """
    @property
    def InheritanceFlags(self) -> InheritanceFlags:
        """

        :return:
        """
    @property
    def IsInherited(self) -> bool:
        """

        :return:
        """
    @property
    def PropagationFlags(self) -> PropagationFlags:
        """

        :return:
        """
    @property
    def SemaphoreRights(self) -> SemaphoreRights:
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

class SemaphoreSecurity(NativeObjectSecurity):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, name: str, includeSections: AccessControlSections):
        """

        :param name:
        :param includeSections:
        """
    @property
    def AccessRightType(self) -> Type:
        """

        :return:
        """
    @property
    def AccessRuleType(self) -> Type:
        """

        :return:
        """
    @property
    def AreAccessRulesCanonical(self) -> bool:
        """

        :return:
        """
    @property
    def AreAccessRulesProtected(self) -> bool:
        """

        :return:
        """
    @property
    def AreAuditRulesCanonical(self) -> bool:
        """

        :return:
        """
    @property
    def AreAuditRulesProtected(self) -> bool:
        """

        :return:
        """
    @property
    def AuditRuleType(self) -> Type:
        """

        :return:
        """
    def AccessRuleFactory(
        self,
        identityReference: IdentityReference,
        accessMask: int,
        isInherited: bool,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
        type: AccessControlType,
    ) -> AccessRule:
        """

        :param identityReference:
        :param accessMask:
        :param isInherited:
        :param inheritanceFlags:
        :param propagationFlags:
        :param type:
        :return:
        """
    def AddAccessRule(self, rule: SemaphoreAccessRule) -> None:
        """

        :param rule:
        """
    def AddAuditRule(self, rule: SemaphoreAuditRule) -> None:
        """

        :param rule:
        """
    def AuditRuleFactory(
        self,
        identityReference: IdentityReference,
        accessMask: int,
        isInherited: bool,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
        flags: AuditFlags,
    ) -> AuditRule:
        """

        :param identityReference:
        :param accessMask:
        :param isInherited:
        :param inheritanceFlags:
        :param propagationFlags:
        :param flags:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetAccessRules(
        self, includeExplicit: bool, includeInherited: bool, targetType: Type
    ) -> AuthorizationRuleCollection:
        """

        :param includeExplicit:
        :param includeInherited:
        :param targetType:
        :return:
        """
    def GetAuditRules(
        self, includeExplicit: bool, includeInherited: bool, targetType: Type
    ) -> AuthorizationRuleCollection:
        """

        :param includeExplicit:
        :param includeInherited:
        :param targetType:
        :return:
        """
    def GetGroup(self, targetType: Type) -> IdentityReference:
        """

        :param targetType:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetOwner(self, targetType: Type) -> IdentityReference:
        """

        :param targetType:
        :return:
        """
    def GetSecurityDescriptorBinaryForm(self) -> Array[int]:
        """

        :return:
        """
    def GetSecurityDescriptorSddlForm(self, includeSections: AccessControlSections) -> str:
        """

        :param includeSections:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ModifyAccessRule(
        self, modification: AccessControlModification, rule: AccessRule, modified: bool
    ) -> Tuple[bool, bool]:
        """

        :param modification:
        :param rule:
        :param modified:
        :return:
        """
    def ModifyAuditRule(
        self, modification: AccessControlModification, rule: AuditRule, modified: bool
    ) -> Tuple[bool, bool]:
        """

        :param modification:
        :param rule:
        :param modified:
        :return:
        """
    def PurgeAccessRules(self, identity: IdentityReference) -> None:
        """

        :param identity:
        """
    def PurgeAuditRules(self, identity: IdentityReference) -> None:
        """

        :param identity:
        """
    def RemoveAccessRule(self, rule: SemaphoreAccessRule) -> bool:
        """

        :param rule:
        :return:
        """
    def RemoveAccessRuleAll(self, rule: SemaphoreAccessRule) -> None:
        """

        :param rule:
        """
    def RemoveAccessRuleSpecific(self, rule: SemaphoreAccessRule) -> None:
        """

        :param rule:
        """
    def RemoveAuditRule(self, rule: SemaphoreAuditRule) -> bool:
        """

        :param rule:
        :return:
        """
    def RemoveAuditRuleAll(self, rule: SemaphoreAuditRule) -> None:
        """

        :param rule:
        """
    def RemoveAuditRuleSpecific(self, rule: SemaphoreAuditRule) -> None:
        """

        :param rule:
        """
    def ResetAccessRule(self, rule: SemaphoreAccessRule) -> None:
        """

        :param rule:
        """
    def SetAccessRule(self, rule: SemaphoreAccessRule) -> None:
        """

        :param rule:
        """
    def SetAccessRuleProtection(self, isProtected: bool, preserveInheritance: bool) -> None:
        """

        :param isProtected:
        :param preserveInheritance:
        """
    def SetAuditRule(self, rule: SemaphoreAuditRule) -> None:
        """

        :param rule:
        """
    def SetAuditRuleProtection(self, isProtected: bool, preserveInheritance: bool) -> None:
        """

        :param isProtected:
        :param preserveInheritance:
        """
    def SetGroup(self, identity: IdentityReference) -> None:
        """

        :param identity:
        """
    def SetOwner(self, identity: IdentityReference) -> None:
        """

        :param identity:
        """
    @overload
    def SetSecurityDescriptorBinaryForm(self, binaryForm: Array[int]) -> None:
        """

        :param binaryForm:
        """
    @overload
    def SetSecurityDescriptorBinaryForm(
        self, binaryForm: Array[int], includeSections: AccessControlSections
    ) -> None:
        """

        :param binaryForm:
        :param includeSections:
        """
    @overload
    def SetSecurityDescriptorSddlForm(self, sddlForm: str) -> None:
        """

        :param sddlForm:
        """
    @overload
    def SetSecurityDescriptorSddlForm(
        self, sddlForm: str, includeSections: AccessControlSections
    ) -> None:
        """

        :param sddlForm:
        :param includeSections:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class SystemAcl(CommonAcl, ICollection, IEnumerable):
    """"""

    @overload
    def __init__(self, isContainer: bool, isDS: bool, rawAcl: RawAcl):
        """

        :param isContainer:
        :param isDS:
        :param rawAcl:
        """
    @overload
    def __init__(self, isContainer: bool, isDS: bool, capacity: int):
        """

        :param isContainer:
        :param isDS:
        :param capacity:
        """
    @overload
    def __init__(self, isContainer: bool, isDS: bool, revision: int, capacity: int):
        """

        :param isContainer:
        :param isDS:
        :param revision:
        :param capacity:
        """
    @property
    def BinaryLength(self) -> int:
        """

        :return:
        """
    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def IsCanonical(self) -> bool:
        """

        :return:
        """
    @property
    def IsContainer(self) -> bool:
        """

        :return:
        """
    @property
    def IsDS(self) -> bool:
        """

        :return:
        """
    @property
    def IsSynchronized(self) -> bool:
        """

        :return:
        """
    @property
    def Item(self) -> GenericAce:
        """

        :return:
        """
    @Item.setter
    def Item(self, value: GenericAce) -> None: ...
    @property
    def Revision(self) -> int:
        """

        :return:
        """
    @property
    def SyncRoot(self) -> object:
        """

        :return:
        """
    @overload
    def AddAudit(self, sid: SecurityIdentifier, rule: ObjectAuditRule) -> None:
        """

        :param sid:
        :param rule:
        """
    @overload
    def AddAudit(
        self,
        auditFlags: AuditFlags,
        sid: SecurityIdentifier,
        accessMask: int,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
    ) -> None:
        """

        :param auditFlags:
        :param sid:
        :param accessMask:
        :param inheritanceFlags:
        :param propagationFlags:
        """
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
        """

        :param auditFlags:
        :param sid:
        :param accessMask:
        :param inheritanceFlags:
        :param propagationFlags:
        :param objectFlags:
        :param objectType:
        :param inheritedObjectType:
        """
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    @overload
    def CopyTo(self, array: Array[GenericAce], index: int) -> None:
        """

        :param array:
        :param index:
        """
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
    def Purge(self, sid: SecurityIdentifier) -> None:
        """

        :param sid:
        """
    @overload
    def RemoveAudit(self, sid: SecurityIdentifier, rule: ObjectAuditRule) -> bool:
        """

        :param sid:
        :param rule:
        :return:
        """
    @overload
    def RemoveAudit(
        self,
        auditFlags: AuditFlags,
        sid: SecurityIdentifier,
        accessMask: int,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
    ) -> bool:
        """

        :param auditFlags:
        :param sid:
        :param accessMask:
        :param inheritanceFlags:
        :param propagationFlags:
        :return:
        """
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
        """

        :param auditFlags:
        :param sid:
        :param accessMask:
        :param inheritanceFlags:
        :param propagationFlags:
        :param objectFlags:
        :param objectType:
        :param inheritedObjectType:
        :return:
        """
    @overload
    def RemoveAuditSpecific(self, sid: SecurityIdentifier, rule: ObjectAuditRule) -> None:
        """

        :param sid:
        :param rule:
        """
    @overload
    def RemoveAuditSpecific(
        self,
        auditFlags: AuditFlags,
        sid: SecurityIdentifier,
        accessMask: int,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
    ) -> None:
        """

        :param auditFlags:
        :param sid:
        :param accessMask:
        :param inheritanceFlags:
        :param propagationFlags:
        """
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
        """

        :param auditFlags:
        :param sid:
        :param accessMask:
        :param inheritanceFlags:
        :param propagationFlags:
        :param objectFlags:
        :param objectType:
        :param inheritedObjectType:
        """
    def RemoveInheritedAces(self) -> None:
        """"""
    @overload
    def SetAudit(self, sid: SecurityIdentifier, rule: ObjectAuditRule) -> None:
        """

        :param sid:
        :param rule:
        """
    @overload
    def SetAudit(
        self,
        auditFlags: AuditFlags,
        sid: SecurityIdentifier,
        accessMask: int,
        inheritanceFlags: InheritanceFlags,
        propagationFlags: PropagationFlags,
    ) -> None:
        """

        :param auditFlags:
        :param sid:
        :param accessMask:
        :param inheritanceFlags:
        :param propagationFlags:
        """
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
        """

        :param auditFlags:
        :param sid:
        :param accessMask:
        :param inheritanceFlags:
        :param propagationFlags:
        :param objectFlags:
        :param objectType:
        :param inheritedObjectType:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def __contains__(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    def __getitem__(self, index: int) -> GenericAce:
        """

        :param index:
        :return:
        """
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    def __len__(self) -> int:
        """

        :return:
        """
    def __setitem__(self, index: int, value: GenericAce) -> None:
        """

        :param index:
        :param value:
        """

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
