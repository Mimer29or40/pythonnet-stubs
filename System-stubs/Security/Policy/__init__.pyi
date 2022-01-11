from __future__ import annotations

from abc import ABC
from typing import List, Protocol, Tuple, TypeVar, Union, overload

from System import ActivationContext, ApplicationId, ApplicationIdentity, Array, Boolean, Byte, Enum, Exception, Int32, Object, String, SystemException, Type, Version, Void
from System.Collections import DictionaryEntry, ICollection, IEnumerable, IEnumerator, IList
from System.Collections.Generic import IEnumerable, IEnumerator, IList
from System.Reflection import Assembly
from System.Runtime.InteropServices import _Exception
from System.Runtime.Serialization import IDeserializationCallback, ISerializable, SerializationInfo, StreamingContext
from System.Security import IEvidenceFactory, IPermission, ISecurityEncodable, ISecurityPolicyEncodable, NamedPermissionSet, PermissionSet, PolicyLevelType, SecurityElement, SecurityZone
from System.Security.Cryptography import HashAlgorithm
from System.Security.Cryptography.X509Certificates import X509Certificate
from System.Security.Permissions import FileIOPermissionAccess, StrongNamePublicKeyBlob

# ---------- Types ---------- #

T = TypeVar('T', bound=EvidenceBase)

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
ByteType = Union[int, Byte]
IntType = Union[int, Int32]
ObjectType = Object
StringType = Union[str, String]
TypeType = Union[type, Type]
VoidType = Union[None, Void]


# ---------- Classes ---------- #

class AllMembershipCondition(ObjectType, IMembershipCondition, ISecurityEncodable, ISecurityPolicyEncodable, IConstantMembershipCondition, IReportMatchMembershipCondition):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Check(self, evidence: Evidence) -> BooleanType: ...
    
    def Copy(self) -> IMembershipCondition: ...
    
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    @overload
    def FromXml(self, e: SecurityElement, level: PolicyLevel) -> VoidType: ...
    
    @overload
    def FromXml(self, e: SecurityElement) -> VoidType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    @overload
    def ToXml(self, level: PolicyLevel) -> SecurityElement: ...
    
    @overload
    def ToXml(self) -> SecurityElement: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AllMembershipCondition(ObjectType, IMembershipCondition, ISecurityEncodable, ISecurityPolicyEncodable, IConstantMembershipCondition, IReportMatchMembershipCondition):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Check(self, evidence: Evidence) -> BooleanType: ...
    
    def Copy(self) -> IMembershipCondition: ...
    
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    @overload
    def FromXml(self, e: SecurityElement, level: PolicyLevel) -> VoidType: ...
    
    @overload
    def FromXml(self, e: SecurityElement) -> VoidType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    @overload
    def ToXml(self, level: PolicyLevel) -> SecurityElement: ...
    
    @overload
    def ToXml(self) -> SecurityElement: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AllMembershipCondition(ObjectType, IMembershipCondition, ISecurityEncodable, ISecurityPolicyEncodable, IConstantMembershipCondition, IReportMatchMembershipCondition):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Check(self, evidence: Evidence) -> BooleanType: ...
    
    def Copy(self) -> IMembershipCondition: ...
    
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    @overload
    def FromXml(self, e: SecurityElement, level: PolicyLevel) -> VoidType: ...
    
    @overload
    def FromXml(self, e: SecurityElement) -> VoidType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    @overload
    def ToXml(self, level: PolicyLevel) -> SecurityElement: ...
    
    @overload
    def ToXml(self) -> SecurityElement: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AppDomainEvidenceFactory(ObjectType, IRuntimeEvidenceFactory):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Target(self) -> IEvidenceFactory: ...
    
    # ---------- Methods ---------- #
    
    def GenerateEvidence(self, evidenceType: TypeType) -> EvidenceBase: ...
    
    def GetFactorySuppliedEvidence(self) -> IEnumerable[EvidenceBase]: ...
    
    def get_Target(self) -> IEvidenceFactory: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AppDomainEvidenceFactory(ObjectType, IRuntimeEvidenceFactory):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Target(self) -> IEvidenceFactory: ...
    
    # ---------- Methods ---------- #
    
    def GenerateEvidence(self, evidenceType: TypeType) -> EvidenceBase: ...
    
    def GetFactorySuppliedEvidence(self) -> IEnumerable[EvidenceBase]: ...
    
    def get_Target(self) -> IEvidenceFactory: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AppDomainEvidenceFactory(ObjectType, IRuntimeEvidenceFactory):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Target(self) -> IEvidenceFactory: ...
    
    # ---------- Methods ---------- #
    
    def GenerateEvidence(self, evidenceType: TypeType) -> EvidenceBase: ...
    
    def GetFactorySuppliedEvidence(self) -> IEnumerable[EvidenceBase]: ...
    
    def get_Target(self) -> IEvidenceFactory: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ApplicationDirectory(EvidenceBase):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, name: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Directory(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> EvidenceBase: ...
    
    def Copy(self) -> ObjectType: ...
    
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Directory(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ApplicationDirectory(EvidenceBase):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, name: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Directory(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> EvidenceBase: ...
    
    def Copy(self) -> ObjectType: ...
    
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Directory(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ApplicationDirectory(EvidenceBase):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, name: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Directory(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> EvidenceBase: ...
    
    def Copy(self) -> ObjectType: ...
    
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Directory(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ApplicationDirectoryMembershipCondition(ObjectType, IMembershipCondition, ISecurityEncodable, ISecurityPolicyEncodable, IConstantMembershipCondition, IReportMatchMembershipCondition):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Check(self, evidence: Evidence) -> BooleanType: ...
    
    def Copy(self) -> IMembershipCondition: ...
    
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    @overload
    def FromXml(self, e: SecurityElement) -> VoidType: ...
    
    @overload
    def FromXml(self, e: SecurityElement, level: PolicyLevel) -> VoidType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    @overload
    def ToXml(self) -> SecurityElement: ...
    
    @overload
    def ToXml(self, level: PolicyLevel) -> SecurityElement: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ApplicationDirectoryMembershipCondition(ObjectType, IMembershipCondition, ISecurityEncodable, ISecurityPolicyEncodable, IConstantMembershipCondition, IReportMatchMembershipCondition):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Check(self, evidence: Evidence) -> BooleanType: ...
    
    def Copy(self) -> IMembershipCondition: ...
    
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    @overload
    def FromXml(self, e: SecurityElement) -> VoidType: ...
    
    @overload
    def FromXml(self, e: SecurityElement, level: PolicyLevel) -> VoidType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    @overload
    def ToXml(self) -> SecurityElement: ...
    
    @overload
    def ToXml(self, level: PolicyLevel) -> SecurityElement: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ApplicationDirectoryMembershipCondition(ObjectType, IMembershipCondition, ISecurityEncodable, ISecurityPolicyEncodable, IConstantMembershipCondition, IReportMatchMembershipCondition):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Check(self, evidence: Evidence) -> BooleanType: ...
    
    def Copy(self) -> IMembershipCondition: ...
    
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    @overload
    def FromXml(self, e: SecurityElement) -> VoidType: ...
    
    @overload
    def FromXml(self, e: SecurityElement, level: PolicyLevel) -> VoidType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    @overload
    def ToXml(self) -> SecurityElement: ...
    
    @overload
    def ToXml(self, level: PolicyLevel) -> SecurityElement: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ApplicationSecurityInfo(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, activationContext: ActivationContext): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ApplicationEvidence(self) -> Evidence: ...
    
    @ApplicationEvidence.setter
    def ApplicationEvidence(self, value: Evidence) -> None: ...
    
    @property
    def ApplicationId(self) -> ApplicationId: ...
    
    @ApplicationId.setter
    def ApplicationId(self, value: ApplicationId) -> None: ...
    
    @property
    def DefaultRequestSet(self) -> PermissionSet: ...
    
    @DefaultRequestSet.setter
    def DefaultRequestSet(self, value: PermissionSet) -> None: ...
    
    @property
    def DeploymentId(self) -> ApplicationId: ...
    
    @DeploymentId.setter
    def DeploymentId(self, value: ApplicationId) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_ApplicationEvidence(self) -> Evidence: ...
    
    def get_ApplicationId(self) -> ApplicationId: ...
    
    def get_DefaultRequestSet(self) -> PermissionSet: ...
    
    def get_DeploymentId(self) -> ApplicationId: ...
    
    def set_ApplicationEvidence(self, value: Evidence) -> VoidType: ...
    
    def set_ApplicationId(self, value: ApplicationId) -> VoidType: ...
    
    def set_DefaultRequestSet(self, value: PermissionSet) -> VoidType: ...
    
    def set_DeploymentId(self, value: ApplicationId) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ApplicationSecurityInfo(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, activationContext: ActivationContext): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ApplicationEvidence(self) -> Evidence: ...
    
    @ApplicationEvidence.setter
    def ApplicationEvidence(self, value: Evidence) -> None: ...
    
    @property
    def ApplicationId(self) -> ApplicationId: ...
    
    @ApplicationId.setter
    def ApplicationId(self, value: ApplicationId) -> None: ...
    
    @property
    def DefaultRequestSet(self) -> PermissionSet: ...
    
    @DefaultRequestSet.setter
    def DefaultRequestSet(self, value: PermissionSet) -> None: ...
    
    @property
    def DeploymentId(self) -> ApplicationId: ...
    
    @DeploymentId.setter
    def DeploymentId(self, value: ApplicationId) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_ApplicationEvidence(self) -> Evidence: ...
    
    def get_ApplicationId(self) -> ApplicationId: ...
    
    def get_DefaultRequestSet(self) -> PermissionSet: ...
    
    def get_DeploymentId(self) -> ApplicationId: ...
    
    def set_ApplicationEvidence(self, value: Evidence) -> VoidType: ...
    
    def set_ApplicationId(self, value: ApplicationId) -> VoidType: ...
    
    def set_DefaultRequestSet(self, value: PermissionSet) -> VoidType: ...
    
    def set_DeploymentId(self, value: ApplicationId) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ApplicationSecurityInfo(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, activationContext: ActivationContext): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ApplicationEvidence(self) -> Evidence: ...
    
    @ApplicationEvidence.setter
    def ApplicationEvidence(self, value: Evidence) -> None: ...
    
    @property
    def ApplicationId(self) -> ApplicationId: ...
    
    @ApplicationId.setter
    def ApplicationId(self, value: ApplicationId) -> None: ...
    
    @property
    def DefaultRequestSet(self) -> PermissionSet: ...
    
    @DefaultRequestSet.setter
    def DefaultRequestSet(self, value: PermissionSet) -> None: ...
    
    @property
    def DeploymentId(self) -> ApplicationId: ...
    
    @DeploymentId.setter
    def DeploymentId(self, value: ApplicationId) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_ApplicationEvidence(self) -> Evidence: ...
    
    def get_ApplicationId(self) -> ApplicationId: ...
    
    def get_DefaultRequestSet(self) -> PermissionSet: ...
    
    def get_DeploymentId(self) -> ApplicationId: ...
    
    def set_ApplicationEvidence(self, value: Evidence) -> VoidType: ...
    
    def set_ApplicationId(self, value: ApplicationId) -> VoidType: ...
    
    def set_DefaultRequestSet(self, value: PermissionSet) -> VoidType: ...
    
    def set_DeploymentId(self, value: ApplicationId) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ApplicationSecurityManager(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def ApplicationTrustManager() -> IApplicationTrustManager: ...
    
    @staticmethod
    @property
    def UserApplicationTrusts() -> ApplicationTrustCollection: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def DetermineApplicationTrust(activationContext: ActivationContext, context: TrustManagerContext) -> BooleanType: ...
    
    @staticmethod
    def get_ApplicationTrustManager() -> IApplicationTrustManager: ...
    
    @staticmethod
    def get_UserApplicationTrusts() -> ApplicationTrustCollection: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ApplicationSecurityManager(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def ApplicationTrustManager() -> IApplicationTrustManager: ...
    
    @staticmethod
    @property
    def UserApplicationTrusts() -> ApplicationTrustCollection: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def DetermineApplicationTrust(activationContext: ActivationContext, context: TrustManagerContext) -> BooleanType: ...
    
    @staticmethod
    def get_ApplicationTrustManager() -> IApplicationTrustManager: ...
    
    @staticmethod
    def get_UserApplicationTrusts() -> ApplicationTrustCollection: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ApplicationSecurityManager(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def ApplicationTrustManager() -> IApplicationTrustManager: ...
    
    @staticmethod
    @property
    def UserApplicationTrusts() -> ApplicationTrustCollection: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def DetermineApplicationTrust(activationContext: ActivationContext, context: TrustManagerContext) -> BooleanType: ...
    
    @staticmethod
    def get_ApplicationTrustManager() -> IApplicationTrustManager: ...
    
    @staticmethod
    def get_UserApplicationTrusts() -> ApplicationTrustCollection: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ApplicationTrust(EvidenceBase, ISecurityEncodable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, applicationIdentity: ApplicationIdentity): ...
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, defaultGrantSet: PermissionSet, fullTrustAssemblies: IEnumerable[StrongName]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ApplicationIdentity(self) -> ApplicationIdentity: ...
    
    @ApplicationIdentity.setter
    def ApplicationIdentity(self, value: ApplicationIdentity) -> None: ...
    
    @property
    def DefaultGrantSet(self) -> PolicyStatement: ...
    
    @DefaultGrantSet.setter
    def DefaultGrantSet(self, value: PolicyStatement) -> None: ...
    
    @property
    def ExtraInfo(self) -> ObjectType: ...
    
    @ExtraInfo.setter
    def ExtraInfo(self, value: ObjectType) -> None: ...
    
    @property
    def FullTrustAssemblies(self) -> IList[StrongName]: ...
    
    @property
    def IsApplicationTrustedToRun(self) -> BooleanType: ...
    
    @IsApplicationTrustedToRun.setter
    def IsApplicationTrustedToRun(self, value: BooleanType) -> None: ...
    
    @property
    def Persist(self) -> BooleanType: ...
    
    @Persist.setter
    def Persist(self, value: BooleanType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> EvidenceBase: ...
    
    def FromXml(self, element: SecurityElement) -> VoidType: ...
    
    def ToXml(self) -> SecurityElement: ...
    
    def get_ApplicationIdentity(self) -> ApplicationIdentity: ...
    
    def get_DefaultGrantSet(self) -> PolicyStatement: ...
    
    def get_ExtraInfo(self) -> ObjectType: ...
    
    def get_FullTrustAssemblies(self) -> IList[StrongName]: ...
    
    def get_IsApplicationTrustedToRun(self) -> BooleanType: ...
    
    def get_Persist(self) -> BooleanType: ...
    
    def set_ApplicationIdentity(self, value: ApplicationIdentity) -> VoidType: ...
    
    def set_DefaultGrantSet(self, value: PolicyStatement) -> VoidType: ...
    
    def set_ExtraInfo(self, value: ObjectType) -> VoidType: ...
    
    def set_IsApplicationTrustedToRun(self, value: BooleanType) -> VoidType: ...
    
    def set_Persist(self, value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ApplicationTrust(EvidenceBase, ISecurityEncodable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, applicationIdentity: ApplicationIdentity): ...
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, defaultGrantSet: PermissionSet, fullTrustAssemblies: IEnumerable[StrongName]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ApplicationIdentity(self) -> ApplicationIdentity: ...
    
    @ApplicationIdentity.setter
    def ApplicationIdentity(self, value: ApplicationIdentity) -> None: ...
    
    @property
    def DefaultGrantSet(self) -> PolicyStatement: ...
    
    @DefaultGrantSet.setter
    def DefaultGrantSet(self, value: PolicyStatement) -> None: ...
    
    @property
    def ExtraInfo(self) -> ObjectType: ...
    
    @ExtraInfo.setter
    def ExtraInfo(self, value: ObjectType) -> None: ...
    
    @property
    def FullTrustAssemblies(self) -> IList[StrongName]: ...
    
    @property
    def IsApplicationTrustedToRun(self) -> BooleanType: ...
    
    @IsApplicationTrustedToRun.setter
    def IsApplicationTrustedToRun(self, value: BooleanType) -> None: ...
    
    @property
    def Persist(self) -> BooleanType: ...
    
    @Persist.setter
    def Persist(self, value: BooleanType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> EvidenceBase: ...
    
    def FromXml(self, element: SecurityElement) -> VoidType: ...
    
    def ToXml(self) -> SecurityElement: ...
    
    def get_ApplicationIdentity(self) -> ApplicationIdentity: ...
    
    def get_DefaultGrantSet(self) -> PolicyStatement: ...
    
    def get_ExtraInfo(self) -> ObjectType: ...
    
    def get_FullTrustAssemblies(self) -> IList[StrongName]: ...
    
    def get_IsApplicationTrustedToRun(self) -> BooleanType: ...
    
    def get_Persist(self) -> BooleanType: ...
    
    def set_ApplicationIdentity(self, value: ApplicationIdentity) -> VoidType: ...
    
    def set_DefaultGrantSet(self, value: PolicyStatement) -> VoidType: ...
    
    def set_ExtraInfo(self, value: ObjectType) -> VoidType: ...
    
    def set_IsApplicationTrustedToRun(self, value: BooleanType) -> VoidType: ...
    
    def set_Persist(self, value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ApplicationTrust(EvidenceBase, ISecurityEncodable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, applicationIdentity: ApplicationIdentity): ...
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, defaultGrantSet: PermissionSet, fullTrustAssemblies: IEnumerable[StrongName]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ApplicationIdentity(self) -> ApplicationIdentity: ...
    
    @ApplicationIdentity.setter
    def ApplicationIdentity(self, value: ApplicationIdentity) -> None: ...
    
    @property
    def DefaultGrantSet(self) -> PolicyStatement: ...
    
    @DefaultGrantSet.setter
    def DefaultGrantSet(self, value: PolicyStatement) -> None: ...
    
    @property
    def ExtraInfo(self) -> ObjectType: ...
    
    @ExtraInfo.setter
    def ExtraInfo(self, value: ObjectType) -> None: ...
    
    @property
    def FullTrustAssemblies(self) -> IList[StrongName]: ...
    
    @property
    def IsApplicationTrustedToRun(self) -> BooleanType: ...
    
    @IsApplicationTrustedToRun.setter
    def IsApplicationTrustedToRun(self, value: BooleanType) -> None: ...
    
    @property
    def Persist(self) -> BooleanType: ...
    
    @Persist.setter
    def Persist(self, value: BooleanType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> EvidenceBase: ...
    
    def FromXml(self, element: SecurityElement) -> VoidType: ...
    
    def ToXml(self) -> SecurityElement: ...
    
    def get_ApplicationIdentity(self) -> ApplicationIdentity: ...
    
    def get_DefaultGrantSet(self) -> PolicyStatement: ...
    
    def get_ExtraInfo(self) -> ObjectType: ...
    
    def get_FullTrustAssemblies(self) -> IList[StrongName]: ...
    
    def get_IsApplicationTrustedToRun(self) -> BooleanType: ...
    
    def get_Persist(self) -> BooleanType: ...
    
    def set_ApplicationIdentity(self, value: ApplicationIdentity) -> VoidType: ...
    
    def set_DefaultGrantSet(self, value: PolicyStatement) -> VoidType: ...
    
    def set_ExtraInfo(self, value: ObjectType) -> VoidType: ...
    
    def set_IsApplicationTrustedToRun(self, value: BooleanType) -> VoidType: ...
    
    def set_Persist(self, value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ApplicationTrustCollection(ObjectType, ICollection, IEnumerable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def IsSynchronized(self) -> BooleanType: ...
    
    def __getitem__(self, key: IntType) -> ApplicationTrust: ...
    
    def __getitem__(self, key: StringType) -> ApplicationTrust: ...
    
    @property
    def SyncRoot(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, trust: ApplicationTrust) -> IntType: ...
    
    @overload
    def AddRange(self, trusts: ArrayType[ApplicationTrust]) -> VoidType: ...
    
    @overload
    def AddRange(self, trusts: ApplicationTrustCollection) -> VoidType: ...
    
    def Clear(self) -> VoidType: ...
    
    def CopyTo(self, array: ArrayType[ApplicationTrust], index: IntType) -> VoidType: ...
    
    def Find(self, applicationIdentity: ApplicationIdentity, versionMatch: ApplicationVersionMatch) -> ApplicationTrustCollection: ...
    
    def GetEnumerator(self) -> ApplicationTrustEnumerator: ...
    
    @overload
    def Remove(self, applicationIdentity: ApplicationIdentity, versionMatch: ApplicationVersionMatch) -> VoidType: ...
    
    @overload
    def Remove(self, trust: ApplicationTrust) -> VoidType: ...
    
    @overload
    def RemoveRange(self, trusts: ArrayType[ApplicationTrust]) -> VoidType: ...
    
    @overload
    def RemoveRange(self, trusts: ApplicationTrustCollection) -> VoidType: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_IsSynchronized(self) -> BooleanType: ...
    
    @overload
    def get_Item(self, index: IntType) -> ApplicationTrust: ...
    
    @overload
    def get_Item(self, appFullName: StringType) -> ApplicationTrust: ...
    
    def get_SyncRoot(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ApplicationTrustCollection(ObjectType, ICollection, IEnumerable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def IsSynchronized(self) -> BooleanType: ...
    
    def __getitem__(self, key: IntType) -> ApplicationTrust: ...
    
    def __getitem__(self, key: StringType) -> ApplicationTrust: ...
    
    @property
    def SyncRoot(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, trust: ApplicationTrust) -> IntType: ...
    
    @overload
    def AddRange(self, trusts: ArrayType[ApplicationTrust]) -> VoidType: ...
    
    @overload
    def AddRange(self, trusts: ApplicationTrustCollection) -> VoidType: ...
    
    def Clear(self) -> VoidType: ...
    
    def CopyTo(self, array: ArrayType[ApplicationTrust], index: IntType) -> VoidType: ...
    
    def Find(self, applicationIdentity: ApplicationIdentity, versionMatch: ApplicationVersionMatch) -> ApplicationTrustCollection: ...
    
    def GetEnumerator(self) -> ApplicationTrustEnumerator: ...
    
    @overload
    def Remove(self, applicationIdentity: ApplicationIdentity, versionMatch: ApplicationVersionMatch) -> VoidType: ...
    
    @overload
    def Remove(self, trust: ApplicationTrust) -> VoidType: ...
    
    @overload
    def RemoveRange(self, trusts: ArrayType[ApplicationTrust]) -> VoidType: ...
    
    @overload
    def RemoveRange(self, trusts: ApplicationTrustCollection) -> VoidType: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_IsSynchronized(self) -> BooleanType: ...
    
    @overload
    def get_Item(self, index: IntType) -> ApplicationTrust: ...
    
    @overload
    def get_Item(self, appFullName: StringType) -> ApplicationTrust: ...
    
    def get_SyncRoot(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ApplicationTrustCollection(ObjectType, ICollection, IEnumerable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def IsSynchronized(self) -> BooleanType: ...
    
    def __getitem__(self, key: IntType) -> ApplicationTrust: ...
    
    def __getitem__(self, key: StringType) -> ApplicationTrust: ...
    
    @property
    def SyncRoot(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, trust: ApplicationTrust) -> IntType: ...
    
    @overload
    def AddRange(self, trusts: ArrayType[ApplicationTrust]) -> VoidType: ...
    
    @overload
    def AddRange(self, trusts: ApplicationTrustCollection) -> VoidType: ...
    
    def Clear(self) -> VoidType: ...
    
    def CopyTo(self, array: ArrayType[ApplicationTrust], index: IntType) -> VoidType: ...
    
    def Find(self, applicationIdentity: ApplicationIdentity, versionMatch: ApplicationVersionMatch) -> ApplicationTrustCollection: ...
    
    def GetEnumerator(self) -> ApplicationTrustEnumerator: ...
    
    @overload
    def Remove(self, applicationIdentity: ApplicationIdentity, versionMatch: ApplicationVersionMatch) -> VoidType: ...
    
    @overload
    def Remove(self, trust: ApplicationTrust) -> VoidType: ...
    
    @overload
    def RemoveRange(self, trusts: ArrayType[ApplicationTrust]) -> VoidType: ...
    
    @overload
    def RemoveRange(self, trusts: ApplicationTrustCollection) -> VoidType: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_IsSynchronized(self) -> BooleanType: ...
    
    @overload
    def get_Item(self, index: IntType) -> ApplicationTrust: ...
    
    @overload
    def get_Item(self, appFullName: StringType) -> ApplicationTrust: ...
    
    def get_SyncRoot(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ApplicationTrustEnumerator(ObjectType, IEnumerator):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Current(self) -> ApplicationTrust: ...
    
    # ---------- Methods ---------- #
    
    def MoveNext(self) -> BooleanType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Current(self) -> ApplicationTrust: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ApplicationTrustEnumerator(ObjectType, IEnumerator):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Current(self) -> ApplicationTrust: ...
    
    # ---------- Methods ---------- #
    
    def MoveNext(self) -> BooleanType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Current(self) -> ApplicationTrust: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ApplicationTrustEnumerator(ObjectType, IEnumerator):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Current(self) -> ApplicationTrust: ...
    
    # ---------- Methods ---------- #
    
    def MoveNext(self) -> BooleanType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Current(self) -> ApplicationTrust: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AssemblyEvidenceFactory(ObjectType, IRuntimeEvidenceFactory):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Target(self) -> IEvidenceFactory: ...
    
    # ---------- Methods ---------- #
    
    def GenerateEvidence(self, evidenceType: TypeType) -> EvidenceBase: ...
    
    def GetFactorySuppliedEvidence(self) -> IEnumerable[EvidenceBase]: ...
    
    def get_Target(self) -> IEvidenceFactory: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AssemblyEvidenceFactory(ObjectType, IRuntimeEvidenceFactory):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Target(self) -> IEvidenceFactory: ...
    
    # ---------- Methods ---------- #
    
    def GenerateEvidence(self, evidenceType: TypeType) -> EvidenceBase: ...
    
    def GetFactorySuppliedEvidence(self) -> IEnumerable[EvidenceBase]: ...
    
    def get_Target(self) -> IEvidenceFactory: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AssemblyEvidenceFactory(ObjectType, IRuntimeEvidenceFactory):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Target(self) -> IEvidenceFactory: ...
    
    # ---------- Methods ---------- #
    
    def GenerateEvidence(self, evidenceType: TypeType) -> EvidenceBase: ...
    
    def GetFactorySuppliedEvidence(self) -> IEnumerable[EvidenceBase]: ...
    
    def get_Target(self) -> IEvidenceFactory: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeConnectAccess(ObjectType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def AnyScheme() -> StringType: ...
    
    @staticmethod
    @property
    def DefaultPort() -> IntType: ...
    
    @staticmethod
    @property
    def OriginPort() -> IntType: ...
    
    @staticmethod
    @property
    def OriginScheme() -> StringType: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self, allowScheme: StringType, allowPort: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Port(self) -> IntType: ...
    
    @property
    def Scheme(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def CreateAnySchemeAccess(allowPort: IntType) -> CodeConnectAccess: ...
    
    @staticmethod
    def CreateOriginSchemeAccess(allowPort: IntType) -> CodeConnectAccess: ...
    
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def get_Port(self) -> IntType: ...
    
    def get_Scheme(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeConnectAccess(ObjectType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def AnyScheme() -> StringType: ...
    
    @staticmethod
    @property
    def DefaultPort() -> IntType: ...
    
    @staticmethod
    @property
    def OriginPort() -> IntType: ...
    
    @staticmethod
    @property
    def OriginScheme() -> StringType: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self, allowScheme: StringType, allowPort: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Port(self) -> IntType: ...
    
    @property
    def Scheme(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def CreateAnySchemeAccess(allowPort: IntType) -> CodeConnectAccess: ...
    
    @staticmethod
    def CreateOriginSchemeAccess(allowPort: IntType) -> CodeConnectAccess: ...
    
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def get_Port(self) -> IntType: ...
    
    def get_Scheme(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeConnectAccess(ObjectType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def AnyScheme() -> StringType: ...
    
    @staticmethod
    @property
    def DefaultPort() -> IntType: ...
    
    @staticmethod
    @property
    def OriginPort() -> IntType: ...
    
    @staticmethod
    @property
    def OriginScheme() -> StringType: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self, allowScheme: StringType, allowPort: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Port(self) -> IntType: ...
    
    @property
    def Scheme(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def CreateAnySchemeAccess(allowPort: IntType) -> CodeConnectAccess: ...
    
    @staticmethod
    def CreateOriginSchemeAccess(allowPort: IntType) -> CodeConnectAccess: ...
    
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def get_Port(self) -> IntType: ...
    
    def get_Scheme(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeGroup(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def AttributeString(self) -> StringType: ...
    
    @property
    def Children(self) -> IList: ...
    
    @Children.setter
    def Children(self, value: IList) -> None: ...
    
    @property
    def Description(self) -> StringType: ...
    
    @Description.setter
    def Description(self, value: StringType) -> None: ...
    
    @property
    def MembershipCondition(self) -> IMembershipCondition: ...
    
    @MembershipCondition.setter
    def MembershipCondition(self, value: IMembershipCondition) -> None: ...
    
    @property
    def MergeLogic(self) -> StringType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @Name.setter
    def Name(self, value: StringType) -> None: ...
    
    @property
    def PermissionSetName(self) -> StringType: ...
    
    @property
    def PolicyStatement(self) -> PolicyStatement: ...
    
    @PolicyStatement.setter
    def PolicyStatement(self, value: PolicyStatement) -> None: ...
    
    # ---------- Methods ---------- #
    
    def AddChild(self, group: CodeGroup) -> VoidType: ...
    
    def Copy(self) -> CodeGroup: ...
    
    @overload
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, cg: CodeGroup, compareChildren: BooleanType) -> BooleanType: ...
    
    @overload
    def FromXml(self, e: SecurityElement, level: PolicyLevel) -> VoidType: ...
    
    @overload
    def FromXml(self, e: SecurityElement) -> VoidType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def RemoveChild(self, group: CodeGroup) -> VoidType: ...
    
    def Resolve(self, evidence: Evidence) -> PolicyStatement: ...
    
    def ResolveMatchingCodeGroups(self, evidence: Evidence) -> CodeGroup: ...
    
    @overload
    def ToXml(self) -> SecurityElement: ...
    
    @overload
    def ToXml(self, level: PolicyLevel) -> SecurityElement: ...
    
    def get_AttributeString(self) -> StringType: ...
    
    def get_Children(self) -> IList: ...
    
    def get_Description(self) -> StringType: ...
    
    def get_MembershipCondition(self) -> IMembershipCondition: ...
    
    def get_MergeLogic(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_PermissionSetName(self) -> StringType: ...
    
    def get_PolicyStatement(self) -> PolicyStatement: ...
    
    def set_Children(self, value: IList) -> VoidType: ...
    
    def set_Description(self, value: StringType) -> VoidType: ...
    
    def set_MembershipCondition(self, value: IMembershipCondition) -> VoidType: ...
    
    def set_Name(self, value: StringType) -> VoidType: ...
    
    def set_PolicyStatement(self, value: PolicyStatement) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeGroup(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def AttributeString(self) -> StringType: ...
    
    @property
    def Children(self) -> IList: ...
    
    @Children.setter
    def Children(self, value: IList) -> None: ...
    
    @property
    def Description(self) -> StringType: ...
    
    @Description.setter
    def Description(self, value: StringType) -> None: ...
    
    @property
    def MembershipCondition(self) -> IMembershipCondition: ...
    
    @MembershipCondition.setter
    def MembershipCondition(self, value: IMembershipCondition) -> None: ...
    
    @property
    def MergeLogic(self) -> StringType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @Name.setter
    def Name(self, value: StringType) -> None: ...
    
    @property
    def PermissionSetName(self) -> StringType: ...
    
    @property
    def PolicyStatement(self) -> PolicyStatement: ...
    
    @PolicyStatement.setter
    def PolicyStatement(self, value: PolicyStatement) -> None: ...
    
    # ---------- Methods ---------- #
    
    def AddChild(self, group: CodeGroup) -> VoidType: ...
    
    def Copy(self) -> CodeGroup: ...
    
    @overload
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, cg: CodeGroup, compareChildren: BooleanType) -> BooleanType: ...
    
    @overload
    def FromXml(self, e: SecurityElement, level: PolicyLevel) -> VoidType: ...
    
    @overload
    def FromXml(self, e: SecurityElement) -> VoidType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def RemoveChild(self, group: CodeGroup) -> VoidType: ...
    
    def Resolve(self, evidence: Evidence) -> PolicyStatement: ...
    
    def ResolveMatchingCodeGroups(self, evidence: Evidence) -> CodeGroup: ...
    
    @overload
    def ToXml(self) -> SecurityElement: ...
    
    @overload
    def ToXml(self, level: PolicyLevel) -> SecurityElement: ...
    
    def get_AttributeString(self) -> StringType: ...
    
    def get_Children(self) -> IList: ...
    
    def get_Description(self) -> StringType: ...
    
    def get_MembershipCondition(self) -> IMembershipCondition: ...
    
    def get_MergeLogic(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_PermissionSetName(self) -> StringType: ...
    
    def get_PolicyStatement(self) -> PolicyStatement: ...
    
    def set_Children(self, value: IList) -> VoidType: ...
    
    def set_Description(self, value: StringType) -> VoidType: ...
    
    def set_MembershipCondition(self, value: IMembershipCondition) -> VoidType: ...
    
    def set_Name(self, value: StringType) -> VoidType: ...
    
    def set_PolicyStatement(self, value: PolicyStatement) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeGroup(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def AttributeString(self) -> StringType: ...
    
    @property
    def Children(self) -> IList: ...
    
    @Children.setter
    def Children(self, value: IList) -> None: ...
    
    @property
    def Description(self) -> StringType: ...
    
    @Description.setter
    def Description(self, value: StringType) -> None: ...
    
    @property
    def MembershipCondition(self) -> IMembershipCondition: ...
    
    @MembershipCondition.setter
    def MembershipCondition(self, value: IMembershipCondition) -> None: ...
    
    @property
    def MergeLogic(self) -> StringType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @Name.setter
    def Name(self, value: StringType) -> None: ...
    
    @property
    def PermissionSetName(self) -> StringType: ...
    
    @property
    def PolicyStatement(self) -> PolicyStatement: ...
    
    @PolicyStatement.setter
    def PolicyStatement(self, value: PolicyStatement) -> None: ...
    
    # ---------- Methods ---------- #
    
    def AddChild(self, group: CodeGroup) -> VoidType: ...
    
    def Copy(self) -> CodeGroup: ...
    
    @overload
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, cg: CodeGroup, compareChildren: BooleanType) -> BooleanType: ...
    
    @overload
    def FromXml(self, e: SecurityElement, level: PolicyLevel) -> VoidType: ...
    
    @overload
    def FromXml(self, e: SecurityElement) -> VoidType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def RemoveChild(self, group: CodeGroup) -> VoidType: ...
    
    def Resolve(self, evidence: Evidence) -> PolicyStatement: ...
    
    def ResolveMatchingCodeGroups(self, evidence: Evidence) -> CodeGroup: ...
    
    @overload
    def ToXml(self) -> SecurityElement: ...
    
    @overload
    def ToXml(self, level: PolicyLevel) -> SecurityElement: ...
    
    def get_AttributeString(self) -> StringType: ...
    
    def get_Children(self) -> IList: ...
    
    def get_Description(self) -> StringType: ...
    
    def get_MembershipCondition(self) -> IMembershipCondition: ...
    
    def get_MergeLogic(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_PermissionSetName(self) -> StringType: ...
    
    def get_PolicyStatement(self) -> PolicyStatement: ...
    
    def set_Children(self, value: IList) -> VoidType: ...
    
    def set_Description(self, value: StringType) -> VoidType: ...
    
    def set_MembershipCondition(self, value: IMembershipCondition) -> VoidType: ...
    
    def set_Name(self, value: StringType) -> VoidType: ...
    
    def set_PolicyStatement(self, value: PolicyStatement) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeGroupPositionMarker(ObjectType):
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


class CodeGroupPositionMarker(ObjectType):
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


class CodeGroupPositionMarker(ObjectType):
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


class CodeGroupStack(ObjectType):
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


class CodeGroupStack(ObjectType):
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


class CodeGroupStack(ObjectType):
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


class CodeGroupStackFrame(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeGroupStackFrame(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeGroupStackFrame(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Evidence(ObjectType, ICollection, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, evidence: Evidence): ...
    
    @overload
    def __init__(self, hostEvidence: ArrayType[ObjectType], assemblyEvidence: ArrayType[ObjectType]): ...
    
    @overload
    def __init__(self, hostEvidence: ArrayType[EvidenceBase], assemblyEvidence: ArrayType[EvidenceBase]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def IsReadOnly(self) -> BooleanType: ...
    
    @property
    def IsSynchronized(self) -> BooleanType: ...
    
    @property
    def Locked(self) -> BooleanType: ...
    
    @Locked.setter
    def Locked(self, value: BooleanType) -> None: ...
    
    @property
    def SyncRoot(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def AddAssembly(self, id: ObjectType) -> VoidType: ...
    
    def AddAssemblyEvidence(self, evidence: T) -> VoidType: ...
    
    def AddHost(self, id: ObjectType) -> VoidType: ...
    
    def AddHostEvidence(self, evidence: T) -> VoidType: ...
    
    def Clear(self) -> VoidType: ...
    
    def Clone(self) -> Evidence: ...
    
    def CopyTo(self, array: Array, index: IntType) -> VoidType: ...
    
    def GetAssemblyEnumerator(self) -> IEnumerator: ...
    
    def GetAssemblyEvidence(self) -> T: ...
    
    def GetEnumerator(self) -> IEnumerator: ...
    
    def GetHostEnumerator(self) -> IEnumerator: ...
    
    def GetHostEvidence(self) -> T: ...
    
    def Merge(self, evidence: Evidence) -> VoidType: ...
    
    def RemoveType(self, t: TypeType) -> VoidType: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_IsReadOnly(self) -> BooleanType: ...
    
    def get_IsSynchronized(self) -> BooleanType: ...
    
    def get_Locked(self) -> BooleanType: ...
    
    def get_SyncRoot(self) -> ObjectType: ...
    
    def set_Locked(self, value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Evidence(ObjectType, ICollection, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, evidence: Evidence): ...
    
    @overload
    def __init__(self, hostEvidence: ArrayType[ObjectType], assemblyEvidence: ArrayType[ObjectType]): ...
    
    @overload
    def __init__(self, hostEvidence: ArrayType[EvidenceBase], assemblyEvidence: ArrayType[EvidenceBase]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def IsReadOnly(self) -> BooleanType: ...
    
    @property
    def IsSynchronized(self) -> BooleanType: ...
    
    @property
    def Locked(self) -> BooleanType: ...
    
    @Locked.setter
    def Locked(self, value: BooleanType) -> None: ...
    
    @property
    def SyncRoot(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def AddAssembly(self, id: ObjectType) -> VoidType: ...
    
    def AddAssemblyEvidence(self, evidence: T) -> VoidType: ...
    
    def AddHost(self, id: ObjectType) -> VoidType: ...
    
    def AddHostEvidence(self, evidence: T) -> VoidType: ...
    
    def Clear(self) -> VoidType: ...
    
    def Clone(self) -> Evidence: ...
    
    def CopyTo(self, array: Array, index: IntType) -> VoidType: ...
    
    def GetAssemblyEnumerator(self) -> IEnumerator: ...
    
    def GetAssemblyEvidence(self) -> T: ...
    
    def GetEnumerator(self) -> IEnumerator: ...
    
    def GetHostEnumerator(self) -> IEnumerator: ...
    
    def GetHostEvidence(self) -> T: ...
    
    def Merge(self, evidence: Evidence) -> VoidType: ...
    
    def RemoveType(self, t: TypeType) -> VoidType: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_IsReadOnly(self) -> BooleanType: ...
    
    def get_IsSynchronized(self) -> BooleanType: ...
    
    def get_Locked(self) -> BooleanType: ...
    
    def get_SyncRoot(self) -> ObjectType: ...
    
    def set_Locked(self, value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Evidence(ObjectType, ICollection, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, evidence: Evidence): ...
    
    @overload
    def __init__(self, hostEvidence: ArrayType[ObjectType], assemblyEvidence: ArrayType[ObjectType]): ...
    
    @overload
    def __init__(self, hostEvidence: ArrayType[EvidenceBase], assemblyEvidence: ArrayType[EvidenceBase]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def IsReadOnly(self) -> BooleanType: ...
    
    @property
    def IsSynchronized(self) -> BooleanType: ...
    
    @property
    def Locked(self) -> BooleanType: ...
    
    @Locked.setter
    def Locked(self, value: BooleanType) -> None: ...
    
    @property
    def SyncRoot(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def AddAssembly(self, id: ObjectType) -> VoidType: ...
    
    def AddAssemblyEvidence(self, evidence: T) -> VoidType: ...
    
    def AddHost(self, id: ObjectType) -> VoidType: ...
    
    def AddHostEvidence(self, evidence: T) -> VoidType: ...
    
    def Clear(self) -> VoidType: ...
    
    def Clone(self) -> Evidence: ...
    
    def CopyTo(self, array: Array, index: IntType) -> VoidType: ...
    
    def GetAssemblyEnumerator(self) -> IEnumerator: ...
    
    def GetAssemblyEvidence(self) -> T: ...
    
    def GetEnumerator(self) -> IEnumerator: ...
    
    def GetHostEnumerator(self) -> IEnumerator: ...
    
    def GetHostEvidence(self) -> T: ...
    
    def Merge(self, evidence: Evidence) -> VoidType: ...
    
    def RemoveType(self, t: TypeType) -> VoidType: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_IsReadOnly(self) -> BooleanType: ...
    
    def get_IsSynchronized(self) -> BooleanType: ...
    
    def get_Locked(self) -> BooleanType: ...
    
    def get_SyncRoot(self) -> ObjectType: ...
    
    def set_Locked(self, value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EvidenceBase(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> EvidenceBase: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EvidenceBase(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> EvidenceBase: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EvidenceBase(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> EvidenceBase: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EvidenceTypeDescriptor(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AssemblyEvidence(self) -> EvidenceBase: ...
    
    @AssemblyEvidence.setter
    def AssemblyEvidence(self, value: EvidenceBase) -> None: ...
    
    @property
    def Generated(self) -> BooleanType: ...
    
    @Generated.setter
    def Generated(self, value: BooleanType) -> None: ...
    
    @property
    def HostCanGenerate(self) -> BooleanType: ...
    
    @HostCanGenerate.setter
    def HostCanGenerate(self, value: BooleanType) -> None: ...
    
    @property
    def HostEvidence(self) -> EvidenceBase: ...
    
    @HostEvidence.setter
    def HostEvidence(self, value: EvidenceBase) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> EvidenceTypeDescriptor: ...
    
    def get_AssemblyEvidence(self) -> EvidenceBase: ...
    
    def get_Generated(self) -> BooleanType: ...
    
    def get_HostCanGenerate(self) -> BooleanType: ...
    
    def get_HostEvidence(self) -> EvidenceBase: ...
    
    def set_AssemblyEvidence(self, value: EvidenceBase) -> VoidType: ...
    
    def set_Generated(self, value: BooleanType) -> VoidType: ...
    
    def set_HostCanGenerate(self, value: BooleanType) -> VoidType: ...
    
    def set_HostEvidence(self, value: EvidenceBase) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EvidenceTypeDescriptor(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AssemblyEvidence(self) -> EvidenceBase: ...
    
    @AssemblyEvidence.setter
    def AssemblyEvidence(self, value: EvidenceBase) -> None: ...
    
    @property
    def Generated(self) -> BooleanType: ...
    
    @Generated.setter
    def Generated(self, value: BooleanType) -> None: ...
    
    @property
    def HostCanGenerate(self) -> BooleanType: ...
    
    @HostCanGenerate.setter
    def HostCanGenerate(self, value: BooleanType) -> None: ...
    
    @property
    def HostEvidence(self) -> EvidenceBase: ...
    
    @HostEvidence.setter
    def HostEvidence(self, value: EvidenceBase) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> EvidenceTypeDescriptor: ...
    
    def get_AssemblyEvidence(self) -> EvidenceBase: ...
    
    def get_Generated(self) -> BooleanType: ...
    
    def get_HostCanGenerate(self) -> BooleanType: ...
    
    def get_HostEvidence(self) -> EvidenceBase: ...
    
    def set_AssemblyEvidence(self, value: EvidenceBase) -> VoidType: ...
    
    def set_Generated(self, value: BooleanType) -> VoidType: ...
    
    def set_HostCanGenerate(self, value: BooleanType) -> VoidType: ...
    
    def set_HostEvidence(self, value: EvidenceBase) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EvidenceTypeDescriptor(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AssemblyEvidence(self) -> EvidenceBase: ...
    
    @AssemblyEvidence.setter
    def AssemblyEvidence(self, value: EvidenceBase) -> None: ...
    
    @property
    def Generated(self) -> BooleanType: ...
    
    @Generated.setter
    def Generated(self, value: BooleanType) -> None: ...
    
    @property
    def HostCanGenerate(self) -> BooleanType: ...
    
    @HostCanGenerate.setter
    def HostCanGenerate(self, value: BooleanType) -> None: ...
    
    @property
    def HostEvidence(self) -> EvidenceBase: ...
    
    @HostEvidence.setter
    def HostEvidence(self, value: EvidenceBase) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> EvidenceTypeDescriptor: ...
    
    def get_AssemblyEvidence(self) -> EvidenceBase: ...
    
    def get_Generated(self) -> BooleanType: ...
    
    def get_HostCanGenerate(self) -> BooleanType: ...
    
    def get_HostEvidence(self) -> EvidenceBase: ...
    
    def set_AssemblyEvidence(self, value: EvidenceBase) -> VoidType: ...
    
    def set_Generated(self, value: BooleanType) -> VoidType: ...
    
    def set_HostCanGenerate(self, value: BooleanType) -> VoidType: ...
    
    def set_HostEvidence(self, value: EvidenceBase) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class FileCodeGroup(CodeGroup, IUnionSemanticCodeGroup):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, membershipCondition: IMembershipCondition, access: FileIOPermissionAccess): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AttributeString(self) -> StringType: ...
    
    @property
    def MergeLogic(self) -> StringType: ...
    
    @property
    def PermissionSetName(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def Copy(self) -> CodeGroup: ...
    
    @overload
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def Resolve(self, evidence: Evidence) -> PolicyStatement: ...
    
    def ResolveMatchingCodeGroups(self, evidence: Evidence) -> CodeGroup: ...
    
    def get_AttributeString(self) -> StringType: ...
    
    def get_MergeLogic(self) -> StringType: ...
    
    def get_PermissionSetName(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class FileCodeGroup(CodeGroup, IUnionSemanticCodeGroup):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, membershipCondition: IMembershipCondition, access: FileIOPermissionAccess): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AttributeString(self) -> StringType: ...
    
    @property
    def MergeLogic(self) -> StringType: ...
    
    @property
    def PermissionSetName(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def Copy(self) -> CodeGroup: ...
    
    @overload
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def Resolve(self, evidence: Evidence) -> PolicyStatement: ...
    
    def ResolveMatchingCodeGroups(self, evidence: Evidence) -> CodeGroup: ...
    
    def get_AttributeString(self) -> StringType: ...
    
    def get_MergeLogic(self) -> StringType: ...
    
    def get_PermissionSetName(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class FileCodeGroup(CodeGroup, IUnionSemanticCodeGroup):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, membershipCondition: IMembershipCondition, access: FileIOPermissionAccess): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AttributeString(self) -> StringType: ...
    
    @property
    def MergeLogic(self) -> StringType: ...
    
    @property
    def PermissionSetName(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def Copy(self) -> CodeGroup: ...
    
    @overload
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def Resolve(self, evidence: Evidence) -> PolicyStatement: ...
    
    def ResolveMatchingCodeGroups(self, evidence: Evidence) -> CodeGroup: ...
    
    def get_AttributeString(self) -> StringType: ...
    
    def get_MergeLogic(self) -> StringType: ...
    
    def get_PermissionSetName(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class FirstMatchCodeGroup(CodeGroup):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, membershipCondition: IMembershipCondition, policy: PolicyStatement): ...
    
    # ---------- Properties ---------- #
    
    @property
    def MergeLogic(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def Copy(self) -> CodeGroup: ...
    
    def Resolve(self, evidence: Evidence) -> PolicyStatement: ...
    
    def ResolveMatchingCodeGroups(self, evidence: Evidence) -> CodeGroup: ...
    
    def get_MergeLogic(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class FirstMatchCodeGroup(CodeGroup):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, membershipCondition: IMembershipCondition, policy: PolicyStatement): ...
    
    # ---------- Properties ---------- #
    
    @property
    def MergeLogic(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def Copy(self) -> CodeGroup: ...
    
    def Resolve(self, evidence: Evidence) -> PolicyStatement: ...
    
    def ResolveMatchingCodeGroups(self, evidence: Evidence) -> CodeGroup: ...
    
    def get_MergeLogic(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class FirstMatchCodeGroup(CodeGroup):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, membershipCondition: IMembershipCondition, policy: PolicyStatement): ...
    
    # ---------- Properties ---------- #
    
    @property
    def MergeLogic(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def Copy(self) -> CodeGroup: ...
    
    def Resolve(self, evidence: Evidence) -> PolicyStatement: ...
    
    def ResolveMatchingCodeGroups(self, evidence: Evidence) -> CodeGroup: ...
    
    def get_MergeLogic(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class GacInstalled(EvidenceBase, IIdentityPermissionFactory):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> EvidenceBase: ...
    
    def Copy(self) -> ObjectType: ...
    
    def CreateIdentityPermission(self, evidence: Evidence) -> IPermission: ...
    
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class GacInstalled(EvidenceBase, IIdentityPermissionFactory):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> EvidenceBase: ...
    
    def Copy(self) -> ObjectType: ...
    
    def CreateIdentityPermission(self, evidence: Evidence) -> IPermission: ...
    
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class GacInstalled(EvidenceBase, IIdentityPermissionFactory):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> EvidenceBase: ...
    
    def Copy(self) -> ObjectType: ...
    
    def CreateIdentityPermission(self, evidence: Evidence) -> IPermission: ...
    
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class GacMembershipCondition(ObjectType, IMembershipCondition, ISecurityEncodable, ISecurityPolicyEncodable, IConstantMembershipCondition, IReportMatchMembershipCondition):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Check(self, evidence: Evidence) -> BooleanType: ...
    
    def Copy(self) -> IMembershipCondition: ...
    
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    @overload
    def FromXml(self, e: SecurityElement) -> VoidType: ...
    
    @overload
    def FromXml(self, e: SecurityElement, level: PolicyLevel) -> VoidType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    @overload
    def ToXml(self) -> SecurityElement: ...
    
    @overload
    def ToXml(self, level: PolicyLevel) -> SecurityElement: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class GacMembershipCondition(ObjectType, IMembershipCondition, ISecurityEncodable, ISecurityPolicyEncodable, IConstantMembershipCondition, IReportMatchMembershipCondition):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Check(self, evidence: Evidence) -> BooleanType: ...
    
    def Copy(self) -> IMembershipCondition: ...
    
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    @overload
    def FromXml(self, e: SecurityElement) -> VoidType: ...
    
    @overload
    def FromXml(self, e: SecurityElement, level: PolicyLevel) -> VoidType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    @overload
    def ToXml(self) -> SecurityElement: ...
    
    @overload
    def ToXml(self, level: PolicyLevel) -> SecurityElement: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class GacMembershipCondition(ObjectType, IMembershipCondition, ISecurityEncodable, ISecurityPolicyEncodable, IConstantMembershipCondition, IReportMatchMembershipCondition):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Check(self, evidence: Evidence) -> BooleanType: ...
    
    def Copy(self) -> IMembershipCondition: ...
    
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    @overload
    def FromXml(self, e: SecurityElement) -> VoidType: ...
    
    @overload
    def FromXml(self, e: SecurityElement, level: PolicyLevel) -> VoidType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    @overload
    def ToXml(self) -> SecurityElement: ...
    
    @overload
    def ToXml(self, level: PolicyLevel) -> SecurityElement: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Hash(EvidenceBase, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, assembly: Assembly): ...
    
    # ---------- Properties ---------- #
    
    @property
    def MD5(self) -> ArrayType[ByteType]: ...
    
    @property
    def SHA1(self) -> ArrayType[ByteType]: ...
    
    @property
    def SHA256(self) -> ArrayType[ByteType]: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> EvidenceBase: ...
    
    @staticmethod
    def CreateMD5(md5: ArrayType[ByteType]) -> Hash: ...
    
    @staticmethod
    def CreateSHA1(sha1: ArrayType[ByteType]) -> Hash: ...
    
    @staticmethod
    def CreateSHA256(sha256: ArrayType[ByteType]) -> Hash: ...
    
    def GenerateHash(self, hashAlg: HashAlgorithm) -> ArrayType[ByteType]: ...
    
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_MD5(self) -> ArrayType[ByteType]: ...
    
    def get_SHA1(self) -> ArrayType[ByteType]: ...
    
    def get_SHA256(self) -> ArrayType[ByteType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Hash(EvidenceBase, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, assembly: Assembly): ...
    
    # ---------- Properties ---------- #
    
    @property
    def MD5(self) -> ArrayType[ByteType]: ...
    
    @property
    def SHA1(self) -> ArrayType[ByteType]: ...
    
    @property
    def SHA256(self) -> ArrayType[ByteType]: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> EvidenceBase: ...
    
    @staticmethod
    def CreateMD5(md5: ArrayType[ByteType]) -> Hash: ...
    
    @staticmethod
    def CreateSHA1(sha1: ArrayType[ByteType]) -> Hash: ...
    
    @staticmethod
    def CreateSHA256(sha256: ArrayType[ByteType]) -> Hash: ...
    
    def GenerateHash(self, hashAlg: HashAlgorithm) -> ArrayType[ByteType]: ...
    
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_MD5(self) -> ArrayType[ByteType]: ...
    
    def get_SHA1(self) -> ArrayType[ByteType]: ...
    
    def get_SHA256(self) -> ArrayType[ByteType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Hash(EvidenceBase, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, assembly: Assembly): ...
    
    # ---------- Properties ---------- #
    
    @property
    def MD5(self) -> ArrayType[ByteType]: ...
    
    @property
    def SHA1(self) -> ArrayType[ByteType]: ...
    
    @property
    def SHA256(self) -> ArrayType[ByteType]: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> EvidenceBase: ...
    
    @staticmethod
    def CreateMD5(md5: ArrayType[ByteType]) -> Hash: ...
    
    @staticmethod
    def CreateSHA1(sha1: ArrayType[ByteType]) -> Hash: ...
    
    @staticmethod
    def CreateSHA256(sha256: ArrayType[ByteType]) -> Hash: ...
    
    def GenerateHash(self, hashAlg: HashAlgorithm) -> ArrayType[ByteType]: ...
    
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_MD5(self) -> ArrayType[ByteType]: ...
    
    def get_SHA1(self) -> ArrayType[ByteType]: ...
    
    def get_SHA256(self) -> ArrayType[ByteType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class HashMembershipCondition(ObjectType, ISerializable, IDeserializationCallback, IMembershipCondition, ISecurityEncodable, ISecurityPolicyEncodable, IReportMatchMembershipCondition):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, hashAlg: HashAlgorithm, value: ArrayType[ByteType]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def HashAlgorithm(self) -> HashAlgorithm: ...
    
    @HashAlgorithm.setter
    def HashAlgorithm(self, value: HashAlgorithm) -> None: ...
    
    @property
    def HashValue(self) -> ArrayType[ByteType]: ...
    
    @HashValue.setter
    def HashValue(self, value: ArrayType[ByteType]) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Check(self, evidence: Evidence) -> BooleanType: ...
    
    def Copy(self) -> IMembershipCondition: ...
    
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    @overload
    def FromXml(self, e: SecurityElement) -> VoidType: ...
    
    @overload
    def FromXml(self, e: SecurityElement, level: PolicyLevel) -> VoidType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    @overload
    def ToXml(self) -> SecurityElement: ...
    
    @overload
    def ToXml(self, level: PolicyLevel) -> SecurityElement: ...
    
    def get_HashAlgorithm(self) -> HashAlgorithm: ...
    
    def get_HashValue(self) -> ArrayType[ByteType]: ...
    
    def set_HashAlgorithm(self, value: HashAlgorithm) -> VoidType: ...
    
    def set_HashValue(self, value: ArrayType[ByteType]) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class HashMembershipCondition(ObjectType, ISerializable, IDeserializationCallback, IMembershipCondition, ISecurityEncodable, ISecurityPolicyEncodable, IReportMatchMembershipCondition):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, hashAlg: HashAlgorithm, value: ArrayType[ByteType]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def HashAlgorithm(self) -> HashAlgorithm: ...
    
    @HashAlgorithm.setter
    def HashAlgorithm(self, value: HashAlgorithm) -> None: ...
    
    @property
    def HashValue(self) -> ArrayType[ByteType]: ...
    
    @HashValue.setter
    def HashValue(self, value: ArrayType[ByteType]) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Check(self, evidence: Evidence) -> BooleanType: ...
    
    def Copy(self) -> IMembershipCondition: ...
    
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    @overload
    def FromXml(self, e: SecurityElement) -> VoidType: ...
    
    @overload
    def FromXml(self, e: SecurityElement, level: PolicyLevel) -> VoidType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    @overload
    def ToXml(self) -> SecurityElement: ...
    
    @overload
    def ToXml(self, level: PolicyLevel) -> SecurityElement: ...
    
    def get_HashAlgorithm(self) -> HashAlgorithm: ...
    
    def get_HashValue(self) -> ArrayType[ByteType]: ...
    
    def set_HashAlgorithm(self, value: HashAlgorithm) -> VoidType: ...
    
    def set_HashValue(self, value: ArrayType[ByteType]) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class HashMembershipCondition(ObjectType, ISerializable, IDeserializationCallback, IMembershipCondition, ISecurityEncodable, ISecurityPolicyEncodable, IReportMatchMembershipCondition):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, hashAlg: HashAlgorithm, value: ArrayType[ByteType]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def HashAlgorithm(self) -> HashAlgorithm: ...
    
    @HashAlgorithm.setter
    def HashAlgorithm(self, value: HashAlgorithm) -> None: ...
    
    @property
    def HashValue(self) -> ArrayType[ByteType]: ...
    
    @HashValue.setter
    def HashValue(self, value: ArrayType[ByteType]) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Check(self, evidence: Evidence) -> BooleanType: ...
    
    def Copy(self) -> IMembershipCondition: ...
    
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    @overload
    def FromXml(self, e: SecurityElement) -> VoidType: ...
    
    @overload
    def FromXml(self, e: SecurityElement, level: PolicyLevel) -> VoidType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    @overload
    def ToXml(self) -> SecurityElement: ...
    
    @overload
    def ToXml(self, level: PolicyLevel) -> SecurityElement: ...
    
    def get_HashAlgorithm(self) -> HashAlgorithm: ...
    
    def get_HashValue(self) -> ArrayType[ByteType]: ...
    
    def set_HashAlgorithm(self, value: HashAlgorithm) -> VoidType: ...
    
    def set_HashValue(self, value: ArrayType[ByteType]) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class LegacyEvidenceList(EvidenceBase, IEnumerable[EvidenceBase], IEnumerable, ILegacyEvidenceAdapter):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def EvidenceObject(self) -> ObjectType: ...
    
    @property
    def EvidenceType(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, evidence: EvidenceBase) -> VoidType: ...
    
    def Clone(self) -> EvidenceBase: ...
    
    def GetEnumerator(self) -> IEnumerator[EvidenceBase]: ...
    
    def get_EvidenceObject(self) -> ObjectType: ...
    
    def get_EvidenceType(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class LegacyEvidenceList(EvidenceBase, IEnumerable[EvidenceBase], IEnumerable, ILegacyEvidenceAdapter):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def EvidenceObject(self) -> ObjectType: ...
    
    @property
    def EvidenceType(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, evidence: EvidenceBase) -> VoidType: ...
    
    def Clone(self) -> EvidenceBase: ...
    
    def GetEnumerator(self) -> IEnumerator[EvidenceBase]: ...
    
    def get_EvidenceObject(self) -> ObjectType: ...
    
    def get_EvidenceType(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class LegacyEvidenceList(EvidenceBase, IEnumerable[EvidenceBase], IEnumerable, ILegacyEvidenceAdapter):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def EvidenceObject(self) -> ObjectType: ...
    
    @property
    def EvidenceType(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, evidence: EvidenceBase) -> VoidType: ...
    
    def Clone(self) -> EvidenceBase: ...
    
    def GetEnumerator(self) -> IEnumerator[EvidenceBase]: ...
    
    def get_EvidenceObject(self) -> ObjectType: ...
    
    def get_EvidenceType(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class LegacyEvidenceWrapper(EvidenceBase, ILegacyEvidenceAdapter):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def EvidenceObject(self) -> ObjectType: ...
    
    @property
    def EvidenceType(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> EvidenceBase: ...
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def get_EvidenceObject(self) -> ObjectType: ...
    
    def get_EvidenceType(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class LegacyEvidenceWrapper(EvidenceBase, ILegacyEvidenceAdapter):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def EvidenceObject(self) -> ObjectType: ...
    
    @property
    def EvidenceType(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> EvidenceBase: ...
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def get_EvidenceObject(self) -> ObjectType: ...
    
    def get_EvidenceType(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class LegacyEvidenceWrapper(EvidenceBase, ILegacyEvidenceAdapter):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def EvidenceObject(self) -> ObjectType: ...
    
    @property
    def EvidenceType(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> EvidenceBase: ...
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def get_EvidenceObject(self) -> ObjectType: ...
    
    def get_EvidenceType(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class NetCodeGroup(CodeGroup, IUnionSemanticCodeGroup):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def AbsentOriginScheme() -> StringType: ...
    
    @staticmethod
    @property
    def AnyOtherOriginScheme() -> StringType: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self, membershipCondition: IMembershipCondition): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AttributeString(self) -> StringType: ...
    
    @property
    def MergeLogic(self) -> StringType: ...
    
    @property
    def PermissionSetName(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def AddConnectAccess(self, originScheme: StringType, connectAccess: CodeConnectAccess) -> VoidType: ...
    
    def Copy(self) -> CodeGroup: ...
    
    @overload
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    def GetConnectAccessRules(self) -> ArrayType[DictionaryEntry]: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ResetConnectAccess(self) -> VoidType: ...
    
    def Resolve(self, evidence: Evidence) -> PolicyStatement: ...
    
    def ResolveMatchingCodeGroups(self, evidence: Evidence) -> CodeGroup: ...
    
    def get_AttributeString(self) -> StringType: ...
    
    def get_MergeLogic(self) -> StringType: ...
    
    def get_PermissionSetName(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class NetCodeGroup(CodeGroup, IUnionSemanticCodeGroup):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def AbsentOriginScheme() -> StringType: ...
    
    @staticmethod
    @property
    def AnyOtherOriginScheme() -> StringType: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self, membershipCondition: IMembershipCondition): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AttributeString(self) -> StringType: ...
    
    @property
    def MergeLogic(self) -> StringType: ...
    
    @property
    def PermissionSetName(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def AddConnectAccess(self, originScheme: StringType, connectAccess: CodeConnectAccess) -> VoidType: ...
    
    def Copy(self) -> CodeGroup: ...
    
    @overload
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    def GetConnectAccessRules(self) -> ArrayType[DictionaryEntry]: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ResetConnectAccess(self) -> VoidType: ...
    
    def Resolve(self, evidence: Evidence) -> PolicyStatement: ...
    
    def ResolveMatchingCodeGroups(self, evidence: Evidence) -> CodeGroup: ...
    
    def get_AttributeString(self) -> StringType: ...
    
    def get_MergeLogic(self) -> StringType: ...
    
    def get_PermissionSetName(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class NetCodeGroup(CodeGroup, IUnionSemanticCodeGroup):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def AbsentOriginScheme() -> StringType: ...
    
    @staticmethod
    @property
    def AnyOtherOriginScheme() -> StringType: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self, membershipCondition: IMembershipCondition): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AttributeString(self) -> StringType: ...
    
    @property
    def MergeLogic(self) -> StringType: ...
    
    @property
    def PermissionSetName(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def AddConnectAccess(self, originScheme: StringType, connectAccess: CodeConnectAccess) -> VoidType: ...
    
    def Copy(self) -> CodeGroup: ...
    
    @overload
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    def GetConnectAccessRules(self) -> ArrayType[DictionaryEntry]: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ResetConnectAccess(self) -> VoidType: ...
    
    def Resolve(self, evidence: Evidence) -> PolicyStatement: ...
    
    def ResolveMatchingCodeGroups(self, evidence: Evidence) -> CodeGroup: ...
    
    def get_AttributeString(self) -> StringType: ...
    
    def get_MergeLogic(self) -> StringType: ...
    
    def get_PermissionSetName(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PEFileEvidenceFactory(ObjectType, IRuntimeEvidenceFactory):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Target(self) -> IEvidenceFactory: ...
    
    # ---------- Methods ---------- #
    
    def GenerateEvidence(self, evidenceType: TypeType) -> EvidenceBase: ...
    
    def GetFactorySuppliedEvidence(self) -> IEnumerable[EvidenceBase]: ...
    
    def get_Target(self) -> IEvidenceFactory: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PEFileEvidenceFactory(ObjectType, IRuntimeEvidenceFactory):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Target(self) -> IEvidenceFactory: ...
    
    # ---------- Methods ---------- #
    
    def GenerateEvidence(self, evidenceType: TypeType) -> EvidenceBase: ...
    
    def GetFactorySuppliedEvidence(self) -> IEnumerable[EvidenceBase]: ...
    
    def get_Target(self) -> IEvidenceFactory: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PEFileEvidenceFactory(ObjectType, IRuntimeEvidenceFactory):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Target(self) -> IEvidenceFactory: ...
    
    # ---------- Methods ---------- #
    
    def GenerateEvidence(self, evidenceType: TypeType) -> EvidenceBase: ...
    
    def GetFactorySuppliedEvidence(self) -> IEnumerable[EvidenceBase]: ...
    
    def get_Target(self) -> IEvidenceFactory: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PermissionRequestEvidence(EvidenceBase):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, request: PermissionSet, optional: PermissionSet, denied: PermissionSet): ...
    
    # ---------- Properties ---------- #
    
    @property
    def DeniedPermissions(self) -> PermissionSet: ...
    
    @property
    def OptionalPermissions(self) -> PermissionSet: ...
    
    @property
    def RequestedPermissions(self) -> PermissionSet: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> EvidenceBase: ...
    
    def Copy(self) -> PermissionRequestEvidence: ...
    
    def ToString(self) -> StringType: ...
    
    def get_DeniedPermissions(self) -> PermissionSet: ...
    
    def get_OptionalPermissions(self) -> PermissionSet: ...
    
    def get_RequestedPermissions(self) -> PermissionSet: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PermissionRequestEvidence(EvidenceBase):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, request: PermissionSet, optional: PermissionSet, denied: PermissionSet): ...
    
    # ---------- Properties ---------- #
    
    @property
    def DeniedPermissions(self) -> PermissionSet: ...
    
    @property
    def OptionalPermissions(self) -> PermissionSet: ...
    
    @property
    def RequestedPermissions(self) -> PermissionSet: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> EvidenceBase: ...
    
    def Copy(self) -> PermissionRequestEvidence: ...
    
    def ToString(self) -> StringType: ...
    
    def get_DeniedPermissions(self) -> PermissionSet: ...
    
    def get_OptionalPermissions(self) -> PermissionSet: ...
    
    def get_RequestedPermissions(self) -> PermissionSet: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PermissionRequestEvidence(EvidenceBase):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, request: PermissionSet, optional: PermissionSet, denied: PermissionSet): ...
    
    # ---------- Properties ---------- #
    
    @property
    def DeniedPermissions(self) -> PermissionSet: ...
    
    @property
    def OptionalPermissions(self) -> PermissionSet: ...
    
    @property
    def RequestedPermissions(self) -> PermissionSet: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> EvidenceBase: ...
    
    def Copy(self) -> PermissionRequestEvidence: ...
    
    def ToString(self) -> StringType: ...
    
    def get_DeniedPermissions(self) -> PermissionSet: ...
    
    def get_OptionalPermissions(self) -> PermissionSet: ...
    
    def get_RequestedPermissions(self) -> PermissionSet: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PolicyException(SystemException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, exception: Exception): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PolicyException(SystemException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, exception: Exception): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PolicyException(SystemException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, exception: Exception): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PolicyLevel(ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def FullTrustAssemblies(self) -> IList: ...
    
    @property
    def Label(self) -> StringType: ...
    
    @property
    def NamedPermissionSets(self) -> IList: ...
    
    @property
    def RootCodeGroup(self) -> CodeGroup: ...
    
    @RootCodeGroup.setter
    def RootCodeGroup(self, value: CodeGroup) -> None: ...
    
    @property
    def StoreLocation(self) -> StringType: ...
    
    @property
    def Type(self) -> PolicyLevelType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def AddFullTrustAssembly(self, sn: StrongName) -> VoidType: ...
    
    @overload
    def AddFullTrustAssembly(self, snMC: StrongNameMembershipCondition) -> VoidType: ...
    
    def AddNamedPermissionSet(self, permSet: NamedPermissionSet) -> VoidType: ...
    
    def ChangeNamedPermissionSet(self, name: StringType, pSet: PermissionSet) -> NamedPermissionSet: ...
    
    @staticmethod
    def CreateAppDomainLevel() -> PolicyLevel: ...
    
    def FromXml(self, e: SecurityElement) -> VoidType: ...
    
    def GetNamedPermissionSet(self, name: StringType) -> NamedPermissionSet: ...
    
    def Recover(self) -> VoidType: ...
    
    @overload
    def RemoveFullTrustAssembly(self, sn: StrongName) -> VoidType: ...
    
    @overload
    def RemoveFullTrustAssembly(self, snMC: StrongNameMembershipCondition) -> VoidType: ...
    
    @overload
    def RemoveNamedPermissionSet(self, permSet: NamedPermissionSet) -> NamedPermissionSet: ...
    
    @overload
    def RemoveNamedPermissionSet(self, name: StringType) -> NamedPermissionSet: ...
    
    def Reset(self) -> VoidType: ...
    
    def Resolve(self, evidence: Evidence) -> PolicyStatement: ...
    
    def ResolveMatchingCodeGroups(self, evidence: Evidence) -> CodeGroup: ...
    
    def ToXml(self) -> SecurityElement: ...
    
    def get_FullTrustAssemblies(self) -> IList: ...
    
    def get_Label(self) -> StringType: ...
    
    def get_NamedPermissionSets(self) -> IList: ...
    
    def get_RootCodeGroup(self) -> CodeGroup: ...
    
    def get_StoreLocation(self) -> StringType: ...
    
    def get_Type(self) -> PolicyLevelType: ...
    
    def set_RootCodeGroup(self, value: CodeGroup) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PolicyLevel(ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def FullTrustAssemblies(self) -> IList: ...
    
    @property
    def Label(self) -> StringType: ...
    
    @property
    def NamedPermissionSets(self) -> IList: ...
    
    @property
    def RootCodeGroup(self) -> CodeGroup: ...
    
    @RootCodeGroup.setter
    def RootCodeGroup(self, value: CodeGroup) -> None: ...
    
    @property
    def StoreLocation(self) -> StringType: ...
    
    @property
    def Type(self) -> PolicyLevelType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def AddFullTrustAssembly(self, sn: StrongName) -> VoidType: ...
    
    @overload
    def AddFullTrustAssembly(self, snMC: StrongNameMembershipCondition) -> VoidType: ...
    
    def AddNamedPermissionSet(self, permSet: NamedPermissionSet) -> VoidType: ...
    
    def ChangeNamedPermissionSet(self, name: StringType, pSet: PermissionSet) -> NamedPermissionSet: ...
    
    @staticmethod
    def CreateAppDomainLevel() -> PolicyLevel: ...
    
    def FromXml(self, e: SecurityElement) -> VoidType: ...
    
    def GetNamedPermissionSet(self, name: StringType) -> NamedPermissionSet: ...
    
    def Recover(self) -> VoidType: ...
    
    @overload
    def RemoveFullTrustAssembly(self, sn: StrongName) -> VoidType: ...
    
    @overload
    def RemoveFullTrustAssembly(self, snMC: StrongNameMembershipCondition) -> VoidType: ...
    
    @overload
    def RemoveNamedPermissionSet(self, permSet: NamedPermissionSet) -> NamedPermissionSet: ...
    
    @overload
    def RemoveNamedPermissionSet(self, name: StringType) -> NamedPermissionSet: ...
    
    def Reset(self) -> VoidType: ...
    
    def Resolve(self, evidence: Evidence) -> PolicyStatement: ...
    
    def ResolveMatchingCodeGroups(self, evidence: Evidence) -> CodeGroup: ...
    
    def ToXml(self) -> SecurityElement: ...
    
    def get_FullTrustAssemblies(self) -> IList: ...
    
    def get_Label(self) -> StringType: ...
    
    def get_NamedPermissionSets(self) -> IList: ...
    
    def get_RootCodeGroup(self) -> CodeGroup: ...
    
    def get_StoreLocation(self) -> StringType: ...
    
    def get_Type(self) -> PolicyLevelType: ...
    
    def set_RootCodeGroup(self, value: CodeGroup) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PolicyLevel(ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def FullTrustAssemblies(self) -> IList: ...
    
    @property
    def Label(self) -> StringType: ...
    
    @property
    def NamedPermissionSets(self) -> IList: ...
    
    @property
    def RootCodeGroup(self) -> CodeGroup: ...
    
    @RootCodeGroup.setter
    def RootCodeGroup(self, value: CodeGroup) -> None: ...
    
    @property
    def StoreLocation(self) -> StringType: ...
    
    @property
    def Type(self) -> PolicyLevelType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def AddFullTrustAssembly(self, sn: StrongName) -> VoidType: ...
    
    @overload
    def AddFullTrustAssembly(self, snMC: StrongNameMembershipCondition) -> VoidType: ...
    
    def AddNamedPermissionSet(self, permSet: NamedPermissionSet) -> VoidType: ...
    
    def ChangeNamedPermissionSet(self, name: StringType, pSet: PermissionSet) -> NamedPermissionSet: ...
    
    @staticmethod
    def CreateAppDomainLevel() -> PolicyLevel: ...
    
    def FromXml(self, e: SecurityElement) -> VoidType: ...
    
    def GetNamedPermissionSet(self, name: StringType) -> NamedPermissionSet: ...
    
    def Recover(self) -> VoidType: ...
    
    @overload
    def RemoveFullTrustAssembly(self, sn: StrongName) -> VoidType: ...
    
    @overload
    def RemoveFullTrustAssembly(self, snMC: StrongNameMembershipCondition) -> VoidType: ...
    
    @overload
    def RemoveNamedPermissionSet(self, permSet: NamedPermissionSet) -> NamedPermissionSet: ...
    
    @overload
    def RemoveNamedPermissionSet(self, name: StringType) -> NamedPermissionSet: ...
    
    def Reset(self) -> VoidType: ...
    
    def Resolve(self, evidence: Evidence) -> PolicyStatement: ...
    
    def ResolveMatchingCodeGroups(self, evidence: Evidence) -> CodeGroup: ...
    
    def ToXml(self) -> SecurityElement: ...
    
    def get_FullTrustAssemblies(self) -> IList: ...
    
    def get_Label(self) -> StringType: ...
    
    def get_NamedPermissionSets(self) -> IList: ...
    
    def get_RootCodeGroup(self) -> CodeGroup: ...
    
    def get_StoreLocation(self) -> StringType: ...
    
    def get_Type(self) -> PolicyLevelType: ...
    
    def set_RootCodeGroup(self, value: CodeGroup) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PolicyStatement(ObjectType, ISecurityPolicyEncodable, ISecurityEncodable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, permSet: PermissionSet): ...
    
    @overload
    def __init__(self, permSet: PermissionSet, attributes: PolicyStatementAttribute): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AttributeString(self) -> StringType: ...
    
    @property
    def Attributes(self) -> PolicyStatementAttribute: ...
    
    @Attributes.setter
    def Attributes(self, value: PolicyStatementAttribute) -> None: ...
    
    @property
    def PermissionSet(self) -> PermissionSet: ...
    
    @PermissionSet.setter
    def PermissionSet(self, value: PermissionSet) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Copy(self) -> PolicyStatement: ...
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @overload
    def FromXml(self, et: SecurityElement) -> VoidType: ...
    
    @overload
    def FromXml(self, et: SecurityElement, level: PolicyLevel) -> VoidType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    @overload
    def ToXml(self) -> SecurityElement: ...
    
    @overload
    def ToXml(self, level: PolicyLevel) -> SecurityElement: ...
    
    def get_AttributeString(self) -> StringType: ...
    
    def get_Attributes(self) -> PolicyStatementAttribute: ...
    
    def get_PermissionSet(self) -> PermissionSet: ...
    
    def set_Attributes(self, value: PolicyStatementAttribute) -> VoidType: ...
    
    def set_PermissionSet(self, value: PermissionSet) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PolicyStatement(ObjectType, ISecurityPolicyEncodable, ISecurityEncodable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, permSet: PermissionSet): ...
    
    @overload
    def __init__(self, permSet: PermissionSet, attributes: PolicyStatementAttribute): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AttributeString(self) -> StringType: ...
    
    @property
    def Attributes(self) -> PolicyStatementAttribute: ...
    
    @Attributes.setter
    def Attributes(self, value: PolicyStatementAttribute) -> None: ...
    
    @property
    def PermissionSet(self) -> PermissionSet: ...
    
    @PermissionSet.setter
    def PermissionSet(self, value: PermissionSet) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Copy(self) -> PolicyStatement: ...
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @overload
    def FromXml(self, et: SecurityElement) -> VoidType: ...
    
    @overload
    def FromXml(self, et: SecurityElement, level: PolicyLevel) -> VoidType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    @overload
    def ToXml(self) -> SecurityElement: ...
    
    @overload
    def ToXml(self, level: PolicyLevel) -> SecurityElement: ...
    
    def get_AttributeString(self) -> StringType: ...
    
    def get_Attributes(self) -> PolicyStatementAttribute: ...
    
    def get_PermissionSet(self) -> PermissionSet: ...
    
    def set_Attributes(self, value: PolicyStatementAttribute) -> VoidType: ...
    
    def set_PermissionSet(self, value: PermissionSet) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PolicyStatement(ObjectType, ISecurityPolicyEncodable, ISecurityEncodable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, permSet: PermissionSet): ...
    
    @overload
    def __init__(self, permSet: PermissionSet, attributes: PolicyStatementAttribute): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AttributeString(self) -> StringType: ...
    
    @property
    def Attributes(self) -> PolicyStatementAttribute: ...
    
    @Attributes.setter
    def Attributes(self, value: PolicyStatementAttribute) -> None: ...
    
    @property
    def PermissionSet(self) -> PermissionSet: ...
    
    @PermissionSet.setter
    def PermissionSet(self, value: PermissionSet) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Copy(self) -> PolicyStatement: ...
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @overload
    def FromXml(self, et: SecurityElement) -> VoidType: ...
    
    @overload
    def FromXml(self, et: SecurityElement, level: PolicyLevel) -> VoidType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    @overload
    def ToXml(self) -> SecurityElement: ...
    
    @overload
    def ToXml(self, level: PolicyLevel) -> SecurityElement: ...
    
    def get_AttributeString(self) -> StringType: ...
    
    def get_Attributes(self) -> PolicyStatementAttribute: ...
    
    def get_PermissionSet(self) -> PermissionSet: ...
    
    def set_Attributes(self, value: PolicyStatementAttribute) -> VoidType: ...
    
    def set_PermissionSet(self, value: PermissionSet) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Publisher(EvidenceBase, IIdentityPermissionFactory):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, cert: X509Certificate): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Certificate(self) -> X509Certificate: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> EvidenceBase: ...
    
    def Copy(self) -> ObjectType: ...
    
    def CreateIdentityPermission(self, evidence: Evidence) -> IPermission: ...
    
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Certificate(self) -> X509Certificate: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Publisher(EvidenceBase, IIdentityPermissionFactory):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, cert: X509Certificate): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Certificate(self) -> X509Certificate: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> EvidenceBase: ...
    
    def Copy(self) -> ObjectType: ...
    
    def CreateIdentityPermission(self, evidence: Evidence) -> IPermission: ...
    
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Certificate(self) -> X509Certificate: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Publisher(EvidenceBase, IIdentityPermissionFactory):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, cert: X509Certificate): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Certificate(self) -> X509Certificate: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> EvidenceBase: ...
    
    def Copy(self) -> ObjectType: ...
    
    def CreateIdentityPermission(self, evidence: Evidence) -> IPermission: ...
    
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Certificate(self) -> X509Certificate: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PublisherMembershipCondition(ObjectType, IMembershipCondition, ISecurityEncodable, ISecurityPolicyEncodable, IConstantMembershipCondition, IReportMatchMembershipCondition):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, certificate: X509Certificate): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Certificate(self) -> X509Certificate: ...
    
    @Certificate.setter
    def Certificate(self, value: X509Certificate) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Check(self, evidence: Evidence) -> BooleanType: ...
    
    def Copy(self) -> IMembershipCondition: ...
    
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    @overload
    def FromXml(self, e: SecurityElement) -> VoidType: ...
    
    @overload
    def FromXml(self, e: SecurityElement, level: PolicyLevel) -> VoidType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    @overload
    def ToXml(self) -> SecurityElement: ...
    
    @overload
    def ToXml(self, level: PolicyLevel) -> SecurityElement: ...
    
    def get_Certificate(self) -> X509Certificate: ...
    
    def set_Certificate(self, value: X509Certificate) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PublisherMembershipCondition(ObjectType, IMembershipCondition, ISecurityEncodable, ISecurityPolicyEncodable, IConstantMembershipCondition, IReportMatchMembershipCondition):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, certificate: X509Certificate): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Certificate(self) -> X509Certificate: ...
    
    @Certificate.setter
    def Certificate(self, value: X509Certificate) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Check(self, evidence: Evidence) -> BooleanType: ...
    
    def Copy(self) -> IMembershipCondition: ...
    
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    @overload
    def FromXml(self, e: SecurityElement) -> VoidType: ...
    
    @overload
    def FromXml(self, e: SecurityElement, level: PolicyLevel) -> VoidType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    @overload
    def ToXml(self) -> SecurityElement: ...
    
    @overload
    def ToXml(self, level: PolicyLevel) -> SecurityElement: ...
    
    def get_Certificate(self) -> X509Certificate: ...
    
    def set_Certificate(self, value: X509Certificate) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PublisherMembershipCondition(ObjectType, IMembershipCondition, ISecurityEncodable, ISecurityPolicyEncodable, IConstantMembershipCondition, IReportMatchMembershipCondition):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, certificate: X509Certificate): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Certificate(self) -> X509Certificate: ...
    
    @Certificate.setter
    def Certificate(self, value: X509Certificate) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Check(self, evidence: Evidence) -> BooleanType: ...
    
    def Copy(self) -> IMembershipCondition: ...
    
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    @overload
    def FromXml(self, e: SecurityElement) -> VoidType: ...
    
    @overload
    def FromXml(self, e: SecurityElement, level: PolicyLevel) -> VoidType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    @overload
    def ToXml(self) -> SecurityElement: ...
    
    @overload
    def ToXml(self, level: PolicyLevel) -> SecurityElement: ...
    
    def get_Certificate(self) -> X509Certificate: ...
    
    def set_Certificate(self, value: X509Certificate) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Site(EvidenceBase, IIdentityPermissionFactory):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, name: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Name(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> EvidenceBase: ...
    
    def Copy(self) -> ObjectType: ...
    
    @staticmethod
    def CreateFromUrl(url: StringType) -> Site: ...
    
    def CreateIdentityPermission(self, evidence: Evidence) -> IPermission: ...
    
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Site(EvidenceBase, IIdentityPermissionFactory):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, name: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Name(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> EvidenceBase: ...
    
    def Copy(self) -> ObjectType: ...
    
    @staticmethod
    def CreateFromUrl(url: StringType) -> Site: ...
    
    def CreateIdentityPermission(self, evidence: Evidence) -> IPermission: ...
    
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Site(EvidenceBase, IIdentityPermissionFactory):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, name: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Name(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> EvidenceBase: ...
    
    def Copy(self) -> ObjectType: ...
    
    @staticmethod
    def CreateFromUrl(url: StringType) -> Site: ...
    
    def CreateIdentityPermission(self, evidence: Evidence) -> IPermission: ...
    
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SiteMembershipCondition(ObjectType, IMembershipCondition, ISecurityEncodable, ISecurityPolicyEncodable, IConstantMembershipCondition, IReportMatchMembershipCondition):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, site: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Site(self) -> StringType: ...
    
    @Site.setter
    def Site(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Check(self, evidence: Evidence) -> BooleanType: ...
    
    def Copy(self) -> IMembershipCondition: ...
    
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    @overload
    def FromXml(self, e: SecurityElement) -> VoidType: ...
    
    @overload
    def FromXml(self, e: SecurityElement, level: PolicyLevel) -> VoidType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    @overload
    def ToXml(self) -> SecurityElement: ...
    
    @overload
    def ToXml(self, level: PolicyLevel) -> SecurityElement: ...
    
    def get_Site(self) -> StringType: ...
    
    def set_Site(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SiteMembershipCondition(ObjectType, IMembershipCondition, ISecurityEncodable, ISecurityPolicyEncodable, IConstantMembershipCondition, IReportMatchMembershipCondition):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, site: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Site(self) -> StringType: ...
    
    @Site.setter
    def Site(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Check(self, evidence: Evidence) -> BooleanType: ...
    
    def Copy(self) -> IMembershipCondition: ...
    
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    @overload
    def FromXml(self, e: SecurityElement) -> VoidType: ...
    
    @overload
    def FromXml(self, e: SecurityElement, level: PolicyLevel) -> VoidType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    @overload
    def ToXml(self) -> SecurityElement: ...
    
    @overload
    def ToXml(self, level: PolicyLevel) -> SecurityElement: ...
    
    def get_Site(self) -> StringType: ...
    
    def set_Site(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SiteMembershipCondition(ObjectType, IMembershipCondition, ISecurityEncodable, ISecurityPolicyEncodable, IConstantMembershipCondition, IReportMatchMembershipCondition):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, site: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Site(self) -> StringType: ...
    
    @Site.setter
    def Site(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Check(self, evidence: Evidence) -> BooleanType: ...
    
    def Copy(self) -> IMembershipCondition: ...
    
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    @overload
    def FromXml(self, e: SecurityElement) -> VoidType: ...
    
    @overload
    def FromXml(self, e: SecurityElement, level: PolicyLevel) -> VoidType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    @overload
    def ToXml(self) -> SecurityElement: ...
    
    @overload
    def ToXml(self, level: PolicyLevel) -> SecurityElement: ...
    
    def get_Site(self) -> StringType: ...
    
    def set_Site(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class StrongName(EvidenceBase, IIdentityPermissionFactory, IDelayEvaluatedEvidence):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, blob: StrongNamePublicKeyBlob, name: StringType, version: Version): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def PublicKey(self) -> StrongNamePublicKeyBlob: ...
    
    @property
    def Version(self) -> Version: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> EvidenceBase: ...
    
    def Copy(self) -> ObjectType: ...
    
    def CreateIdentityPermission(self, evidence: Evidence) -> IPermission: ...
    
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_PublicKey(self) -> StrongNamePublicKeyBlob: ...
    
    def get_Version(self) -> Version: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class StrongName(EvidenceBase, IIdentityPermissionFactory, IDelayEvaluatedEvidence):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, blob: StrongNamePublicKeyBlob, name: StringType, version: Version): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def PublicKey(self) -> StrongNamePublicKeyBlob: ...
    
    @property
    def Version(self) -> Version: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> EvidenceBase: ...
    
    def Copy(self) -> ObjectType: ...
    
    def CreateIdentityPermission(self, evidence: Evidence) -> IPermission: ...
    
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_PublicKey(self) -> StrongNamePublicKeyBlob: ...
    
    def get_Version(self) -> Version: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class StrongName(EvidenceBase, IIdentityPermissionFactory, IDelayEvaluatedEvidence):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, blob: StrongNamePublicKeyBlob, name: StringType, version: Version): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def PublicKey(self) -> StrongNamePublicKeyBlob: ...
    
    @property
    def Version(self) -> Version: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> EvidenceBase: ...
    
    def Copy(self) -> ObjectType: ...
    
    def CreateIdentityPermission(self, evidence: Evidence) -> IPermission: ...
    
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_PublicKey(self) -> StrongNamePublicKeyBlob: ...
    
    def get_Version(self) -> Version: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class StrongNameMembershipCondition(ObjectType, IMembershipCondition, ISecurityEncodable, ISecurityPolicyEncodable, IConstantMembershipCondition, IReportMatchMembershipCondition):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, blob: StrongNamePublicKeyBlob, name: StringType, version: Version): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Name(self) -> StringType: ...
    
    @Name.setter
    def Name(self, value: StringType) -> None: ...
    
    @property
    def PublicKey(self) -> StrongNamePublicKeyBlob: ...
    
    @PublicKey.setter
    def PublicKey(self, value: StrongNamePublicKeyBlob) -> None: ...
    
    @property
    def Version(self) -> Version: ...
    
    @Version.setter
    def Version(self, value: Version) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Check(self, evidence: Evidence) -> BooleanType: ...
    
    def Copy(self) -> IMembershipCondition: ...
    
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    @overload
    def FromXml(self, e: SecurityElement) -> VoidType: ...
    
    @overload
    def FromXml(self, e: SecurityElement, level: PolicyLevel) -> VoidType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    @overload
    def ToXml(self) -> SecurityElement: ...
    
    @overload
    def ToXml(self, level: PolicyLevel) -> SecurityElement: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_PublicKey(self) -> StrongNamePublicKeyBlob: ...
    
    def get_Version(self) -> Version: ...
    
    def set_Name(self, value: StringType) -> VoidType: ...
    
    def set_PublicKey(self, value: StrongNamePublicKeyBlob) -> VoidType: ...
    
    def set_Version(self, value: Version) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class StrongNameMembershipCondition(ObjectType, IMembershipCondition, ISecurityEncodable, ISecurityPolicyEncodable, IConstantMembershipCondition, IReportMatchMembershipCondition):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, blob: StrongNamePublicKeyBlob, name: StringType, version: Version): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Name(self) -> StringType: ...
    
    @Name.setter
    def Name(self, value: StringType) -> None: ...
    
    @property
    def PublicKey(self) -> StrongNamePublicKeyBlob: ...
    
    @PublicKey.setter
    def PublicKey(self, value: StrongNamePublicKeyBlob) -> None: ...
    
    @property
    def Version(self) -> Version: ...
    
    @Version.setter
    def Version(self, value: Version) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Check(self, evidence: Evidence) -> BooleanType: ...
    
    def Copy(self) -> IMembershipCondition: ...
    
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    @overload
    def FromXml(self, e: SecurityElement) -> VoidType: ...
    
    @overload
    def FromXml(self, e: SecurityElement, level: PolicyLevel) -> VoidType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    @overload
    def ToXml(self) -> SecurityElement: ...
    
    @overload
    def ToXml(self, level: PolicyLevel) -> SecurityElement: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_PublicKey(self) -> StrongNamePublicKeyBlob: ...
    
    def get_Version(self) -> Version: ...
    
    def set_Name(self, value: StringType) -> VoidType: ...
    
    def set_PublicKey(self, value: StrongNamePublicKeyBlob) -> VoidType: ...
    
    def set_Version(self, value: Version) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class StrongNameMembershipCondition(ObjectType, IMembershipCondition, ISecurityEncodable, ISecurityPolicyEncodable, IConstantMembershipCondition, IReportMatchMembershipCondition):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, blob: StrongNamePublicKeyBlob, name: StringType, version: Version): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Name(self) -> StringType: ...
    
    @Name.setter
    def Name(self, value: StringType) -> None: ...
    
    @property
    def PublicKey(self) -> StrongNamePublicKeyBlob: ...
    
    @PublicKey.setter
    def PublicKey(self, value: StrongNamePublicKeyBlob) -> None: ...
    
    @property
    def Version(self) -> Version: ...
    
    @Version.setter
    def Version(self, value: Version) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Check(self, evidence: Evidence) -> BooleanType: ...
    
    def Copy(self) -> IMembershipCondition: ...
    
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    @overload
    def FromXml(self, e: SecurityElement) -> VoidType: ...
    
    @overload
    def FromXml(self, e: SecurityElement, level: PolicyLevel) -> VoidType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    @overload
    def ToXml(self) -> SecurityElement: ...
    
    @overload
    def ToXml(self, level: PolicyLevel) -> SecurityElement: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_PublicKey(self) -> StrongNamePublicKeyBlob: ...
    
    def get_Version(self) -> Version: ...
    
    def set_Name(self, value: StringType) -> VoidType: ...
    
    def set_PublicKey(self, value: StrongNamePublicKeyBlob) -> VoidType: ...
    
    def set_Version(self, value: Version) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TrustManagerContext(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, uiContext: TrustManagerUIContext): ...
    
    # ---------- Properties ---------- #
    
    @property
    def IgnorePersistedDecision(self) -> BooleanType: ...
    
    @IgnorePersistedDecision.setter
    def IgnorePersistedDecision(self, value: BooleanType) -> None: ...
    
    @property
    def KeepAlive(self) -> BooleanType: ...
    
    @KeepAlive.setter
    def KeepAlive(self, value: BooleanType) -> None: ...
    
    @property
    def NoPrompt(self) -> BooleanType: ...
    
    @NoPrompt.setter
    def NoPrompt(self, value: BooleanType) -> None: ...
    
    @property
    def Persist(self) -> BooleanType: ...
    
    @Persist.setter
    def Persist(self, value: BooleanType) -> None: ...
    
    @property
    def PreviousApplicationIdentity(self) -> ApplicationIdentity: ...
    
    @PreviousApplicationIdentity.setter
    def PreviousApplicationIdentity(self, value: ApplicationIdentity) -> None: ...
    
    @property
    def UIContext(self) -> TrustManagerUIContext: ...
    
    @UIContext.setter
    def UIContext(self, value: TrustManagerUIContext) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_IgnorePersistedDecision(self) -> BooleanType: ...
    
    def get_KeepAlive(self) -> BooleanType: ...
    
    def get_NoPrompt(self) -> BooleanType: ...
    
    def get_Persist(self) -> BooleanType: ...
    
    def get_PreviousApplicationIdentity(self) -> ApplicationIdentity: ...
    
    def get_UIContext(self) -> TrustManagerUIContext: ...
    
    def set_IgnorePersistedDecision(self, value: BooleanType) -> VoidType: ...
    
    def set_KeepAlive(self, value: BooleanType) -> VoidType: ...
    
    def set_NoPrompt(self, value: BooleanType) -> VoidType: ...
    
    def set_Persist(self, value: BooleanType) -> VoidType: ...
    
    def set_PreviousApplicationIdentity(self, value: ApplicationIdentity) -> VoidType: ...
    
    def set_UIContext(self, value: TrustManagerUIContext) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TrustManagerContext(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, uiContext: TrustManagerUIContext): ...
    
    # ---------- Properties ---------- #
    
    @property
    def IgnorePersistedDecision(self) -> BooleanType: ...
    
    @IgnorePersistedDecision.setter
    def IgnorePersistedDecision(self, value: BooleanType) -> None: ...
    
    @property
    def KeepAlive(self) -> BooleanType: ...
    
    @KeepAlive.setter
    def KeepAlive(self, value: BooleanType) -> None: ...
    
    @property
    def NoPrompt(self) -> BooleanType: ...
    
    @NoPrompt.setter
    def NoPrompt(self, value: BooleanType) -> None: ...
    
    @property
    def Persist(self) -> BooleanType: ...
    
    @Persist.setter
    def Persist(self, value: BooleanType) -> None: ...
    
    @property
    def PreviousApplicationIdentity(self) -> ApplicationIdentity: ...
    
    @PreviousApplicationIdentity.setter
    def PreviousApplicationIdentity(self, value: ApplicationIdentity) -> None: ...
    
    @property
    def UIContext(self) -> TrustManagerUIContext: ...
    
    @UIContext.setter
    def UIContext(self, value: TrustManagerUIContext) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_IgnorePersistedDecision(self) -> BooleanType: ...
    
    def get_KeepAlive(self) -> BooleanType: ...
    
    def get_NoPrompt(self) -> BooleanType: ...
    
    def get_Persist(self) -> BooleanType: ...
    
    def get_PreviousApplicationIdentity(self) -> ApplicationIdentity: ...
    
    def get_UIContext(self) -> TrustManagerUIContext: ...
    
    def set_IgnorePersistedDecision(self, value: BooleanType) -> VoidType: ...
    
    def set_KeepAlive(self, value: BooleanType) -> VoidType: ...
    
    def set_NoPrompt(self, value: BooleanType) -> VoidType: ...
    
    def set_Persist(self, value: BooleanType) -> VoidType: ...
    
    def set_PreviousApplicationIdentity(self, value: ApplicationIdentity) -> VoidType: ...
    
    def set_UIContext(self, value: TrustManagerUIContext) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TrustManagerContext(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, uiContext: TrustManagerUIContext): ...
    
    # ---------- Properties ---------- #
    
    @property
    def IgnorePersistedDecision(self) -> BooleanType: ...
    
    @IgnorePersistedDecision.setter
    def IgnorePersistedDecision(self, value: BooleanType) -> None: ...
    
    @property
    def KeepAlive(self) -> BooleanType: ...
    
    @KeepAlive.setter
    def KeepAlive(self, value: BooleanType) -> None: ...
    
    @property
    def NoPrompt(self) -> BooleanType: ...
    
    @NoPrompt.setter
    def NoPrompt(self, value: BooleanType) -> None: ...
    
    @property
    def Persist(self) -> BooleanType: ...
    
    @Persist.setter
    def Persist(self, value: BooleanType) -> None: ...
    
    @property
    def PreviousApplicationIdentity(self) -> ApplicationIdentity: ...
    
    @PreviousApplicationIdentity.setter
    def PreviousApplicationIdentity(self, value: ApplicationIdentity) -> None: ...
    
    @property
    def UIContext(self) -> TrustManagerUIContext: ...
    
    @UIContext.setter
    def UIContext(self, value: TrustManagerUIContext) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_IgnorePersistedDecision(self) -> BooleanType: ...
    
    def get_KeepAlive(self) -> BooleanType: ...
    
    def get_NoPrompt(self) -> BooleanType: ...
    
    def get_Persist(self) -> BooleanType: ...
    
    def get_PreviousApplicationIdentity(self) -> ApplicationIdentity: ...
    
    def get_UIContext(self) -> TrustManagerUIContext: ...
    
    def set_IgnorePersistedDecision(self, value: BooleanType) -> VoidType: ...
    
    def set_KeepAlive(self, value: BooleanType) -> VoidType: ...
    
    def set_NoPrompt(self, value: BooleanType) -> VoidType: ...
    
    def set_Persist(self, value: BooleanType) -> VoidType: ...
    
    def set_PreviousApplicationIdentity(self, value: ApplicationIdentity) -> VoidType: ...
    
    def set_UIContext(self, value: TrustManagerUIContext) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UnionCodeGroup(CodeGroup, IUnionSemanticCodeGroup):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, membershipCondition: IMembershipCondition, policy: PolicyStatement): ...
    
    # ---------- Properties ---------- #
    
    @property
    def MergeLogic(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def Copy(self) -> CodeGroup: ...
    
    def Resolve(self, evidence: Evidence) -> PolicyStatement: ...
    
    def ResolveMatchingCodeGroups(self, evidence: Evidence) -> CodeGroup: ...
    
    def get_MergeLogic(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UnionCodeGroup(CodeGroup, IUnionSemanticCodeGroup):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, membershipCondition: IMembershipCondition, policy: PolicyStatement): ...
    
    # ---------- Properties ---------- #
    
    @property
    def MergeLogic(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def Copy(self) -> CodeGroup: ...
    
    def Resolve(self, evidence: Evidence) -> PolicyStatement: ...
    
    def ResolveMatchingCodeGroups(self, evidence: Evidence) -> CodeGroup: ...
    
    def get_MergeLogic(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UnionCodeGroup(CodeGroup, IUnionSemanticCodeGroup):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, membershipCondition: IMembershipCondition, policy: PolicyStatement): ...
    
    # ---------- Properties ---------- #
    
    @property
    def MergeLogic(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def Copy(self) -> CodeGroup: ...
    
    def Resolve(self, evidence: Evidence) -> PolicyStatement: ...
    
    def ResolveMatchingCodeGroups(self, evidence: Evidence) -> CodeGroup: ...
    
    def get_MergeLogic(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Url(EvidenceBase, IIdentityPermissionFactory):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, name: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> EvidenceBase: ...
    
    def Copy(self) -> ObjectType: ...
    
    def CreateIdentityPermission(self, evidence: Evidence) -> IPermission: ...
    
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Value(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Url(EvidenceBase, IIdentityPermissionFactory):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, name: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> EvidenceBase: ...
    
    def Copy(self) -> ObjectType: ...
    
    def CreateIdentityPermission(self, evidence: Evidence) -> IPermission: ...
    
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Value(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Url(EvidenceBase, IIdentityPermissionFactory):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, name: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> EvidenceBase: ...
    
    def Copy(self) -> ObjectType: ...
    
    def CreateIdentityPermission(self, evidence: Evidence) -> IPermission: ...
    
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Value(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UrlMembershipCondition(ObjectType, IMembershipCondition, ISecurityEncodable, ISecurityPolicyEncodable, IConstantMembershipCondition, IReportMatchMembershipCondition):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, url: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Url(self) -> StringType: ...
    
    @Url.setter
    def Url(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Check(self, evidence: Evidence) -> BooleanType: ...
    
    def Copy(self) -> IMembershipCondition: ...
    
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    @overload
    def FromXml(self, e: SecurityElement, level: PolicyLevel) -> VoidType: ...
    
    @overload
    def FromXml(self, e: SecurityElement) -> VoidType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    @overload
    def ToXml(self) -> SecurityElement: ...
    
    @overload
    def ToXml(self, level: PolicyLevel) -> SecurityElement: ...
    
    def get_Url(self) -> StringType: ...
    
    def set_Url(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UrlMembershipCondition(ObjectType, IMembershipCondition, ISecurityEncodable, ISecurityPolicyEncodable, IConstantMembershipCondition, IReportMatchMembershipCondition):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, url: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Url(self) -> StringType: ...
    
    @Url.setter
    def Url(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Check(self, evidence: Evidence) -> BooleanType: ...
    
    def Copy(self) -> IMembershipCondition: ...
    
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    @overload
    def FromXml(self, e: SecurityElement, level: PolicyLevel) -> VoidType: ...
    
    @overload
    def FromXml(self, e: SecurityElement) -> VoidType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    @overload
    def ToXml(self) -> SecurityElement: ...
    
    @overload
    def ToXml(self, level: PolicyLevel) -> SecurityElement: ...
    
    def get_Url(self) -> StringType: ...
    
    def set_Url(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UrlMembershipCondition(ObjectType, IMembershipCondition, ISecurityEncodable, ISecurityPolicyEncodable, IConstantMembershipCondition, IReportMatchMembershipCondition):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, url: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Url(self) -> StringType: ...
    
    @Url.setter
    def Url(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Check(self, evidence: Evidence) -> BooleanType: ...
    
    def Copy(self) -> IMembershipCondition: ...
    
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    @overload
    def FromXml(self, e: SecurityElement, level: PolicyLevel) -> VoidType: ...
    
    @overload
    def FromXml(self, e: SecurityElement) -> VoidType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    @overload
    def ToXml(self) -> SecurityElement: ...
    
    @overload
    def ToXml(self, level: PolicyLevel) -> SecurityElement: ...
    
    def get_Url(self) -> StringType: ...
    
    def set_Url(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Zone(EvidenceBase, IIdentityPermissionFactory):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, zone: SecurityZone): ...
    
    # ---------- Properties ---------- #
    
    @property
    def SecurityZone(self) -> SecurityZone: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> EvidenceBase: ...
    
    def Copy(self) -> ObjectType: ...
    
    @staticmethod
    def CreateFromUrl(url: StringType) -> Zone: ...
    
    def CreateIdentityPermission(self, evidence: Evidence) -> IPermission: ...
    
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_SecurityZone(self) -> SecurityZone: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Zone(EvidenceBase, IIdentityPermissionFactory):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, zone: SecurityZone): ...
    
    # ---------- Properties ---------- #
    
    @property
    def SecurityZone(self) -> SecurityZone: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> EvidenceBase: ...
    
    def Copy(self) -> ObjectType: ...
    
    @staticmethod
    def CreateFromUrl(url: StringType) -> Zone: ...
    
    def CreateIdentityPermission(self, evidence: Evidence) -> IPermission: ...
    
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_SecurityZone(self) -> SecurityZone: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Zone(EvidenceBase, IIdentityPermissionFactory):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, zone: SecurityZone): ...
    
    # ---------- Properties ---------- #
    
    @property
    def SecurityZone(self) -> SecurityZone: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> EvidenceBase: ...
    
    def Copy(self) -> ObjectType: ...
    
    @staticmethod
    def CreateFromUrl(url: StringType) -> Zone: ...
    
    def CreateIdentityPermission(self, evidence: Evidence) -> IPermission: ...
    
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_SecurityZone(self) -> SecurityZone: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ZoneMembershipCondition(ObjectType, IMembershipCondition, ISecurityEncodable, ISecurityPolicyEncodable, IConstantMembershipCondition, IReportMatchMembershipCondition):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, zone: SecurityZone): ...
    
    # ---------- Properties ---------- #
    
    @property
    def SecurityZone(self) -> SecurityZone: ...
    
    @SecurityZone.setter
    def SecurityZone(self, value: SecurityZone) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Check(self, evidence: Evidence) -> BooleanType: ...
    
    def Copy(self) -> IMembershipCondition: ...
    
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    @overload
    def FromXml(self, e: SecurityElement) -> VoidType: ...
    
    @overload
    def FromXml(self, e: SecurityElement, level: PolicyLevel) -> VoidType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    @overload
    def ToXml(self) -> SecurityElement: ...
    
    @overload
    def ToXml(self, level: PolicyLevel) -> SecurityElement: ...
    
    def get_SecurityZone(self) -> SecurityZone: ...
    
    def set_SecurityZone(self, value: SecurityZone) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ZoneMembershipCondition(ObjectType, IMembershipCondition, ISecurityEncodable, ISecurityPolicyEncodable, IConstantMembershipCondition, IReportMatchMembershipCondition):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, zone: SecurityZone): ...
    
    # ---------- Properties ---------- #
    
    @property
    def SecurityZone(self) -> SecurityZone: ...
    
    @SecurityZone.setter
    def SecurityZone(self, value: SecurityZone) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Check(self, evidence: Evidence) -> BooleanType: ...
    
    def Copy(self) -> IMembershipCondition: ...
    
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    @overload
    def FromXml(self, e: SecurityElement) -> VoidType: ...
    
    @overload
    def FromXml(self, e: SecurityElement, level: PolicyLevel) -> VoidType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    @overload
    def ToXml(self) -> SecurityElement: ...
    
    @overload
    def ToXml(self, level: PolicyLevel) -> SecurityElement: ...
    
    def get_SecurityZone(self) -> SecurityZone: ...
    
    def set_SecurityZone(self, value: SecurityZone) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ZoneMembershipCondition(ObjectType, IMembershipCondition, ISecurityEncodable, ISecurityPolicyEncodable, IConstantMembershipCondition, IReportMatchMembershipCondition):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, zone: SecurityZone): ...
    
    # ---------- Properties ---------- #
    
    @property
    def SecurityZone(self) -> SecurityZone: ...
    
    @SecurityZone.setter
    def SecurityZone(self, value: SecurityZone) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Check(self, evidence: Evidence) -> BooleanType: ...
    
    def Copy(self) -> IMembershipCondition: ...
    
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    @overload
    def FromXml(self, e: SecurityElement) -> VoidType: ...
    
    @overload
    def FromXml(self, e: SecurityElement, level: PolicyLevel) -> VoidType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    @overload
    def ToXml(self) -> SecurityElement: ...
    
    @overload
    def ToXml(self, level: PolicyLevel) -> SecurityElement: ...
    
    def get_SecurityZone(self) -> SecurityZone: ...
    
    def set_SecurityZone(self, value: SecurityZone) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# No Structs

# ---------- Interfaces ---------- #

class IApplicationTrustManager(Protocol, ISecurityEncodable):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def DetermineApplicationTrust(self, activationContext: ActivationContext, context: TrustManagerContext) -> ApplicationTrust: ...
    
    # No Events


class IApplicationTrustManager(Protocol, ISecurityEncodable):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def DetermineApplicationTrust(self, activationContext: ActivationContext, context: TrustManagerContext) -> ApplicationTrust: ...
    
    # No Events


class IApplicationTrustManager(Protocol, ISecurityEncodable):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def DetermineApplicationTrust(self, activationContext: ActivationContext, context: TrustManagerContext) -> ApplicationTrust: ...
    
    # No Events


class IConstantMembershipCondition(Protocol):
    """"""
    
    # No Properties
    
    # No Methods
    
    # No Events


class IConstantMembershipCondition(Protocol):
    """"""
    
    # No Properties
    
    # No Methods
    
    # No Events


class IConstantMembershipCondition(Protocol):
    """"""
    
    # No Properties
    
    # No Methods
    
    # No Events


class IDelayEvaluatedEvidence(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def IsVerified(self) -> BooleanType: ...
    
    @property
    def WasUsed(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def MarkUsed(self) -> VoidType: ...
    
    def get_IsVerified(self) -> BooleanType: ...
    
    def get_WasUsed(self) -> BooleanType: ...
    
    # No Events


class IDelayEvaluatedEvidence(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def IsVerified(self) -> BooleanType: ...
    
    @property
    def WasUsed(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def MarkUsed(self) -> VoidType: ...
    
    def get_IsVerified(self) -> BooleanType: ...
    
    def get_WasUsed(self) -> BooleanType: ...
    
    # No Events


class IDelayEvaluatedEvidence(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def IsVerified(self) -> BooleanType: ...
    
    @property
    def WasUsed(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def MarkUsed(self) -> VoidType: ...
    
    def get_IsVerified(self) -> BooleanType: ...
    
    def get_WasUsed(self) -> BooleanType: ...
    
    # No Events


class IIdentityPermissionFactory(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def CreateIdentityPermission(self, evidence: Evidence) -> IPermission: ...
    
    # No Events


class IIdentityPermissionFactory(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def CreateIdentityPermission(self, evidence: Evidence) -> IPermission: ...
    
    # No Events


class IIdentityPermissionFactory(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def CreateIdentityPermission(self, evidence: Evidence) -> IPermission: ...
    
    # No Events


class ILegacyEvidenceAdapter(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def EvidenceObject(self) -> ObjectType: ...
    
    @property
    def EvidenceType(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def get_EvidenceObject(self) -> ObjectType: ...
    
    def get_EvidenceType(self) -> TypeType: ...
    
    # No Events


class ILegacyEvidenceAdapter(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def EvidenceObject(self) -> ObjectType: ...
    
    @property
    def EvidenceType(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def get_EvidenceObject(self) -> ObjectType: ...
    
    def get_EvidenceType(self) -> TypeType: ...
    
    # No Events


class ILegacyEvidenceAdapter(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def EvidenceObject(self) -> ObjectType: ...
    
    @property
    def EvidenceType(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def get_EvidenceObject(self) -> ObjectType: ...
    
    def get_EvidenceType(self) -> TypeType: ...
    
    # No Events


class IMembershipCondition(Protocol, ISecurityEncodable, ISecurityPolicyEncodable):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Check(self, evidence: Evidence) -> BooleanType: ...
    
    def Copy(self) -> IMembershipCondition: ...
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def ToString(self) -> StringType: ...
    
    # No Events


class IMembershipCondition(Protocol, ISecurityEncodable, ISecurityPolicyEncodable):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Check(self, evidence: Evidence) -> BooleanType: ...
    
    def Copy(self) -> IMembershipCondition: ...
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def ToString(self) -> StringType: ...
    
    # No Events


class IMembershipCondition(Protocol, ISecurityEncodable, ISecurityPolicyEncodable):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Check(self, evidence: Evidence) -> BooleanType: ...
    
    def Copy(self) -> IMembershipCondition: ...
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def ToString(self) -> StringType: ...
    
    # No Events


class IReportMatchMembershipCondition(Protocol, IMembershipCondition, ISecurityEncodable, ISecurityPolicyEncodable):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Check(self, evidence: Evidence, usedEvidence: ObjectType) -> Tuple[BooleanType, ObjectType]: ...
    
    # No Events


class IReportMatchMembershipCondition(Protocol, IMembershipCondition, ISecurityEncodable, ISecurityPolicyEncodable):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Check(self, evidence: Evidence, usedEvidence: ObjectType) -> Tuple[BooleanType, ObjectType]: ...
    
    # No Events


class IReportMatchMembershipCondition(Protocol, IMembershipCondition, ISecurityEncodable, ISecurityPolicyEncodable):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Check(self, evidence: Evidence, usedEvidence: ObjectType) -> Tuple[BooleanType, ObjectType]: ...
    
    # No Events


class IRuntimeEvidenceFactory(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def Target(self) -> IEvidenceFactory: ...
    
    # ---------- Methods ---------- #
    
    def GenerateEvidence(self, evidenceType: TypeType) -> EvidenceBase: ...
    
    def GetFactorySuppliedEvidence(self) -> IEnumerable[EvidenceBase]: ...
    
    def get_Target(self) -> IEvidenceFactory: ...
    
    # No Events


class IRuntimeEvidenceFactory(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def Target(self) -> IEvidenceFactory: ...
    
    # ---------- Methods ---------- #
    
    def GenerateEvidence(self, evidenceType: TypeType) -> EvidenceBase: ...
    
    def GetFactorySuppliedEvidence(self) -> IEnumerable[EvidenceBase]: ...
    
    def get_Target(self) -> IEvidenceFactory: ...
    
    # No Events


class IRuntimeEvidenceFactory(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def Target(self) -> IEvidenceFactory: ...
    
    # ---------- Methods ---------- #
    
    def GenerateEvidence(self, evidenceType: TypeType) -> EvidenceBase: ...
    
    def GetFactorySuppliedEvidence(self) -> IEnumerable[EvidenceBase]: ...
    
    def get_Target(self) -> IEvidenceFactory: ...
    
    # No Events


class IUnionSemanticCodeGroup(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def InternalResolve(self, evidence: Evidence) -> PolicyStatement: ...
    
    # No Events


class IUnionSemanticCodeGroup(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def InternalResolve(self, evidence: Evidence) -> PolicyStatement: ...
    
    # No Events


class IUnionSemanticCodeGroup(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def InternalResolve(self, evidence: Evidence) -> PolicyStatement: ...
    
    # No Events


# ---------- Enums ---------- #

class ApplicationVersionMatch(Enum):
    MatchExactVersion: IntType = 0
    MatchAllVersions: IntType = 1


class ApplicationVersionMatch(Enum):
    MatchExactVersion: IntType = 0
    MatchAllVersions: IntType = 1


class ApplicationVersionMatch(Enum):
    MatchExactVersion: IntType = 0
    MatchAllVersions: IntType = 1


class ConfigId(Enum):
    #None: IntType = 0
    MachinePolicyLevel: IntType = 1
    UserPolicyLevel: IntType = 2
    EnterprisePolicyLevel: IntType = 3


class ConfigId(Enum):
    #None: IntType = 0
    MachinePolicyLevel: IntType = 1
    UserPolicyLevel: IntType = 2
    EnterprisePolicyLevel: IntType = 3


class ConfigId(Enum):
    #None: IntType = 0
    MachinePolicyLevel: IntType = 1
    UserPolicyLevel: IntType = 2
    EnterprisePolicyLevel: IntType = 3


class EvidenceTypeGenerated(Enum):
    AssemblySupplied: IntType = 0
    Gac: IntType = 1
    Hash: IntType = 2
    PermissionRequest: IntType = 3
    Publisher: IntType = 4
    Site: IntType = 5
    StrongName: IntType = 6
    Url: IntType = 7
    Zone: IntType = 8


class EvidenceTypeGenerated(Enum):
    AssemblySupplied: IntType = 0
    Gac: IntType = 1
    Hash: IntType = 2
    PermissionRequest: IntType = 3
    Publisher: IntType = 4
    Site: IntType = 5
    StrongName: IntType = 6
    Url: IntType = 7
    Zone: IntType = 8


class EvidenceTypeGenerated(Enum):
    AssemblySupplied: IntType = 0
    Gac: IntType = 1
    Hash: IntType = 2
    PermissionRequest: IntType = 3
    Publisher: IntType = 4
    Site: IntType = 5
    StrongName: IntType = 6
    Url: IntType = 7
    Zone: IntType = 8


class PolicyStatementAttribute(Enum):
    Nothing: IntType = 0
    Exclusive: IntType = 1
    LevelFinal: IntType = 2
    All: IntType = 3


class PolicyStatementAttribute(Enum):
    Nothing: IntType = 0
    Exclusive: IntType = 1
    LevelFinal: IntType = 2
    All: IntType = 3


class PolicyStatementAttribute(Enum):
    Nothing: IntType = 0
    Exclusive: IntType = 1
    LevelFinal: IntType = 2
    All: IntType = 3


class TrustManagerUIContext(Enum):
    Install: IntType = 0
    Upgrade: IntType = 1
    Run: IntType = 2


class TrustManagerUIContext(Enum):
    Install: IntType = 0
    Upgrade: IntType = 1
    Run: IntType = 2


class TrustManagerUIContext(Enum):
    Install: IntType = 0
    Upgrade: IntType = 1
    Run: IntType = 2


# No Delegates

__all__ = [
    AllMembershipCondition,
    AppDomainEvidenceFactory,
    ApplicationDirectory,
    ApplicationDirectoryMembershipCondition,
    ApplicationSecurityInfo,
    ApplicationSecurityManager,
    ApplicationTrust,
    ApplicationTrustCollection,
    ApplicationTrustEnumerator,
    AssemblyEvidenceFactory,
    CodeConnectAccess,
    CodeGroup,
    CodeGroupPositionMarker,
    CodeGroupStack,
    CodeGroupStackFrame,
    Evidence,
    EvidenceBase,
    EvidenceTypeDescriptor,
    FileCodeGroup,
    FirstMatchCodeGroup,
    GacInstalled,
    GacMembershipCondition,
    Hash,
    HashMembershipCondition,
    LegacyEvidenceList,
    LegacyEvidenceWrapper,
    NetCodeGroup,
    PEFileEvidenceFactory,
    PermissionRequestEvidence,
    PolicyException,
    PolicyLevel,
    PolicyStatement,
    Publisher,
    PublisherMembershipCondition,
    Site,
    SiteMembershipCondition,
    StrongName,
    StrongNameMembershipCondition,
    TrustManagerContext,
    UnionCodeGroup,
    Url,
    UrlMembershipCondition,
    Zone,
    ZoneMembershipCondition,
    IApplicationTrustManager,
    IConstantMembershipCondition,
    IDelayEvaluatedEvidence,
    IIdentityPermissionFactory,
    ILegacyEvidenceAdapter,
    IMembershipCondition,
    IReportMatchMembershipCondition,
    IRuntimeEvidenceFactory,
    IUnionSemanticCodeGroup,
    ApplicationVersionMatch,
    ConfigId,
    EvidenceTypeGenerated,
    PolicyStatementAttribute,
    TrustManagerUIContext,
]
