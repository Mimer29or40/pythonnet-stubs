"""Automatically generated stubs for C# namespace: System.Security.Policy."""

from abc import ABC
from collections.abc import Iterator
from typing import ClassVar
from typing import overload

from System import ActivationContext
from System import ApplicationId
from System import ApplicationIdentity
from System import Array
from System import Enum
from System import Exception
from System import Object
from System import SystemException
from System import Type
from System import Version
from System.Collections import DictionaryEntry
from System.Collections import ICollection
from System.Collections import IDictionary
from System.Collections import IEnumerable
from System.Collections import IEnumerator
from System.Collections import IList
from System.Collections.Generic import IEnumerable
from System.Collections.Generic import IEnumerator
from System.Collections.Generic import IList
from System.Reflection import Assembly
from System.Reflection import MethodBase
from System.Runtime.InteropServices import _Exception
from System.Runtime.Serialization import IDeserializationCallback
from System.Runtime.Serialization import ISerializable
from System.Runtime.Serialization import SerializationInfo
from System.Runtime.Serialization import StreamingContext
from System.Security import IEvidenceFactory
from System.Security import IPermission
from System.Security import ISecurityEncodable
from System.Security import ISecurityPolicyEncodable
from System.Security import NamedPermissionSet
from System.Security import PermissionSet
from System.Security import PolicyLevelType
from System.Security import SecurityElement
from System.Security import SecurityZone
from System.Security.Cryptography import HashAlgorithm
from System.Security.Cryptography.X509Certificates import X509Certificate
from System.Security.Permissions import FileIOPermissionAccess
from System.Security.Permissions import StrongNamePublicKeyBlob

class AllMembershipCondition(
    Object,
    IConstantMembershipCondition,
    IMembershipCondition,
    IReportMatchMembershipCondition,
    ISecurityEncodable,
    ISecurityPolicyEncodable,
):
    """"""
    def __init__(self) -> None:
        """"""
    @overload
    def Check(self, evidence: Evidence) -> bool:
        """"""
    @overload
    def Check(self, evidence: Evidence, usedEvidence: Object) -> tuple[bool, Object]:
        """"""
    def Copy(self) -> IMembershipCondition:
        """"""
    def Equals(self, o: object) -> bool:
        """"""
    @overload
    def FromXml(self, e: SecurityElement) -> None:
        """"""
    @overload
    def FromXml(self, e: SecurityElement, level: PolicyLevel) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def ToXml(self) -> SecurityElement:
        """"""
    @overload
    def ToXml(self, level: PolicyLevel) -> SecurityElement:
        """"""

class AppDomainEvidenceFactory(Object, IRuntimeEvidenceFactory):
    """"""
    @property
    def Target(self) -> IEvidenceFactory:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GenerateEvidence(self, evidenceType: Type) -> EvidenceBase:
        """"""
    def GetFactorySuppliedEvidence(self) -> IEnumerable[EvidenceBase]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ApplicationDirectory(EvidenceBase):
    """"""
    def __init__(self, name: str) -> None:
        """"""
    @property
    def Directory(self) -> str:
        """"""
    def Clone(self) -> EvidenceBase:
        """"""
    def Copy(self) -> object:
        """"""
    def Equals(self, o: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ApplicationDirectoryMembershipCondition(
    Object,
    IConstantMembershipCondition,
    IMembershipCondition,
    IReportMatchMembershipCondition,
    ISecurityEncodable,
    ISecurityPolicyEncodable,
):
    """"""
    def __init__(self) -> None:
        """"""
    @overload
    def Check(self, evidence: Evidence) -> bool:
        """"""
    @overload
    def Check(self, evidence: Evidence, usedEvidence: Object) -> tuple[bool, Object]:
        """"""
    def Copy(self) -> IMembershipCondition:
        """"""
    def Equals(self, o: object) -> bool:
        """"""
    @overload
    def FromXml(self, e: SecurityElement) -> None:
        """"""
    @overload
    def FromXml(self, e: SecurityElement, level: PolicyLevel) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def ToXml(self) -> SecurityElement:
        """"""
    @overload
    def ToXml(self, level: PolicyLevel) -> SecurityElement:
        """"""

class ApplicationSecurityInfo(Object):
    """"""
    def __init__(self, activationContext: ActivationContext) -> None:
        """"""
    @property
    def ApplicationEvidence(self) -> Evidence:
        """"""
    @ApplicationEvidence.setter
    def ApplicationEvidence(self, value: Evidence) -> None: ...
    @property
    def ApplicationId(self) -> ApplicationId:
        """"""
    @ApplicationId.setter
    def ApplicationId(self, value: ApplicationId) -> None: ...
    @property
    def DefaultRequestSet(self) -> PermissionSet:
        """"""
    @DefaultRequestSet.setter
    def DefaultRequestSet(self, value: PermissionSet) -> None: ...
    @property
    def DeploymentId(self) -> ApplicationId:
        """"""
    @DeploymentId.setter
    def DeploymentId(self, value: ApplicationId) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ApplicationSecurityManager(ABC, Object):
    """"""
    @classmethod
    @property
    def ApplicationTrustManager(cls) -> IApplicationTrustManager:
        """"""
    @classmethod
    @property
    def UserApplicationTrusts(cls) -> ApplicationTrustCollection:
        """"""
    @classmethod
    def DetermineApplicationTrust(
        cls, activationContext: ActivationContext, context: TrustManagerContext
    ) -> bool:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ApplicationTrust(EvidenceBase, ISecurityEncodable):
    """"""
    @overload
    def __init__(self, applicationIdentity: ApplicationIdentity) -> None:
        """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(
        self, defaultGrantSet: PermissionSet, fullTrustAssemblies: IEnumerable[StrongName]
    ) -> None:
        """"""
    @property
    def ApplicationIdentity(self) -> ApplicationIdentity:
        """"""
    @ApplicationIdentity.setter
    def ApplicationIdentity(self, value: ApplicationIdentity) -> None: ...
    @property
    def DefaultGrantSet(self) -> PolicyStatement:
        """"""
    @DefaultGrantSet.setter
    def DefaultGrantSet(self, value: PolicyStatement) -> None: ...
    @property
    def ExtraInfo(self) -> object:
        """"""
    @ExtraInfo.setter
    def ExtraInfo(self, value: object) -> None: ...
    @property
    def FullTrustAssemblies(self) -> IList[StrongName]:
        """"""
    @property
    def IsApplicationTrustedToRun(self) -> bool:
        """"""
    @IsApplicationTrustedToRun.setter
    def IsApplicationTrustedToRun(self, value: bool) -> None: ...
    @property
    def Persist(self) -> bool:
        """"""
    @Persist.setter
    def Persist(self, value: bool) -> None: ...
    def Clone(self) -> EvidenceBase:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def FromXml(self, element: SecurityElement) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def ToXml(self) -> SecurityElement:
        """"""

class ApplicationTrustCollection(Object, ICollection, IEnumerable):
    """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def Item(self) -> ApplicationTrust:
        """"""
    @property
    def SyncRoot(self) -> object:
        """"""
    def Add(self, trust: ApplicationTrust) -> int:
        """"""
    @overload
    def AddRange(self, trusts: ApplicationTrustCollection) -> None:
        """"""
    @overload
    def AddRange(self, trusts: Array[ApplicationTrust]) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array[ApplicationTrust], index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Find(
        self, applicationIdentity: ApplicationIdentity, versionMatch: ApplicationVersionMatch
    ) -> ApplicationTrustCollection:
        """"""
    def GetEnumerator(self) -> ApplicationTrustEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def Remove(self, trust: ApplicationTrust) -> None:
        """"""
    @overload
    def Remove(
        self, applicationIdentity: ApplicationIdentity, versionMatch: ApplicationVersionMatch
    ) -> None:
        """"""
    @overload
    def RemoveRange(self, trusts: ApplicationTrustCollection) -> None:
        """"""
    @overload
    def RemoveRange(self, trusts: Array[ApplicationTrust]) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    @overload
    def __delitem__(self, trust: ApplicationTrust) -> None:
        """"""
    @overload
    def __delitem__(
        self, applicationIdentity: ApplicationIdentity, versionMatch: ApplicationVersionMatch
    ) -> None:
        """"""
    def __len__(self) -> int:
        """"""
    @overload
    def __getitem__(self, index: int) -> ApplicationTrust:
        """"""
    @overload
    def __getitem__(self, appFullName: str) -> ApplicationTrust:
        """"""

class ApplicationTrustEnumerator(Object, IEnumerator):
    """"""
    @property
    def Current(self) -> ApplicationTrust:
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

class ApplicationVersionMatch(Enum):
    """"""

    MatchExactVersion: ApplicationVersionMatch = ...
    """"""
    MatchAllVersions: ApplicationVersionMatch = ...
    """"""

class AssemblyEvidenceFactory(Object, IRuntimeEvidenceFactory):
    """"""
    @property
    def Target(self) -> IEvidenceFactory:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GenerateEvidence(self, evidenceType: Type) -> EvidenceBase:
        """"""
    def GetFactorySuppliedEvidence(self) -> IEnumerable[EvidenceBase]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class CodeConnectAccess(Object):
    """"""

    AnyScheme: ClassVar[str]
    """"""
    DefaultPort: ClassVar[int]
    """"""
    OriginPort: ClassVar[int]
    """"""
    OriginScheme: ClassVar[str]
    """"""
    def __init__(self, allowScheme: str, allowPort: int) -> None:
        """"""
    @property
    def Port(self) -> int:
        """"""
    @property
    def Scheme(self) -> str:
        """"""
    @classmethod
    def CreateAnySchemeAccess(cls, allowPort: int) -> CodeConnectAccess:
        """"""
    @classmethod
    def CreateOriginSchemeAccess(cls, allowPort: int) -> CodeConnectAccess:
        """"""
    def Equals(self, o: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class CodeGroup(ABC, Object):
    """"""
    @property
    def AttributeString(self) -> str:
        """"""
    @property
    def Children(self) -> IList:
        """"""
    @Children.setter
    def Children(self, value: IList) -> None: ...
    @property
    def Description(self) -> str:
        """"""
    @Description.setter
    def Description(self, value: str) -> None: ...
    @property
    def MembershipCondition(self) -> IMembershipCondition:
        """"""
    @MembershipCondition.setter
    def MembershipCondition(self, value: IMembershipCondition) -> None: ...
    @property
    def MergeLogic(self) -> str:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def PermissionSetName(self) -> str:
        """"""
    @property
    def PolicyStatement(self) -> PolicyStatement:
        """"""
    @PolicyStatement.setter
    def PolicyStatement(self, value: PolicyStatement) -> None: ...
    def AddChild(self, group: CodeGroup) -> None:
        """"""
    def Copy(self) -> CodeGroup:
        """"""
    @overload
    def Equals(self, cg: CodeGroup, compareChildren: bool) -> bool:
        """"""
    @overload
    def Equals(self, o: object) -> bool:
        """"""
    @overload
    def FromXml(self, e: SecurityElement) -> None:
        """"""
    @overload
    def FromXml(self, e: SecurityElement, level: PolicyLevel) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def RemoveChild(self, group: CodeGroup) -> None:
        """"""
    def Resolve(self, evidence: Evidence) -> PolicyStatement:
        """"""
    def ResolveMatchingCodeGroups(self, evidence: Evidence) -> CodeGroup:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def ToXml(self) -> SecurityElement:
        """"""
    @overload
    def ToXml(self, level: PolicyLevel) -> SecurityElement:
        """"""

class CodeGroupPositionMarker(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class CodeGroupStack(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class CodeGroupStackFrame(Object):
    """"""
    def __init__(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ConfigId(Enum):
    """"""

    _None: ConfigId = ...
    """"""
    MachinePolicyLevel: ConfigId = ...
    """"""
    UserPolicyLevel: ConfigId = ...
    """"""
    EnterprisePolicyLevel: ConfigId = ...
    """"""

class Evidence(Object, ICollection, IEnumerable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, evidence: Evidence) -> None:
        """"""
    @overload
    def __init__(self, hostEvidence: Array[object], assemblyEvidence: Array[object]) -> None:
        """"""
    @overload
    def __init__(
        self, hostEvidence: Array[EvidenceBase], assemblyEvidence: Array[EvidenceBase]
    ) -> None:
        """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def Locked(self) -> bool:
        """"""
    @Locked.setter
    def Locked(self, value: bool) -> None: ...
    @property
    def SyncRoot(self) -> object:
        """"""
    def AddAssembly(self, id: object) -> None:
        """"""
    def AddAssemblyEvidence[T](self, evidence: T) -> None:
        """"""
    def AddHost(self, id: object) -> None:
        """"""
    def AddHostEvidence[T](self, evidence: T) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    def Clone(self) -> Evidence:
        """"""
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetAssemblyEnumerator(self) -> IEnumerator:
        """"""
    def GetAssemblyEvidence[T](self) -> T:
        """"""
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetHostEnumerator(self) -> IEnumerator:
        """"""
    def GetHostEvidence[T](self) -> T:
        """"""
    def GetType(self) -> Type:
        """"""
    def Merge(self, evidence: Evidence) -> None:
        """"""
    def RemoveType(self, t: Type) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    def __len__(self) -> int:
        """"""

class EvidenceBase(ABC, Object):
    """"""
    def Clone(self) -> EvidenceBase:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class EvidenceTypeDescriptor(Object):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def AssemblyEvidence(self) -> EvidenceBase:
        """"""
    @AssemblyEvidence.setter
    def AssemblyEvidence(self, value: EvidenceBase) -> None: ...
    @property
    def Generated(self) -> bool:
        """"""
    @Generated.setter
    def Generated(self, value: bool) -> None: ...
    @property
    def HostCanGenerate(self) -> bool:
        """"""
    @HostCanGenerate.setter
    def HostCanGenerate(self, value: bool) -> None: ...
    @property
    def HostEvidence(self) -> EvidenceBase:
        """"""
    @HostEvidence.setter
    def HostEvidence(self, value: EvidenceBase) -> None: ...
    def Clone(self) -> EvidenceTypeDescriptor:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class EvidenceTypeGenerated(Enum):
    """"""

    AssemblySupplied: EvidenceTypeGenerated = ...
    """"""
    Gac: EvidenceTypeGenerated = ...
    """"""
    Hash: EvidenceTypeGenerated = ...
    """"""
    PermissionRequest: EvidenceTypeGenerated = ...
    """"""
    Publisher: EvidenceTypeGenerated = ...
    """"""
    Site: EvidenceTypeGenerated = ...
    """"""
    StrongName: EvidenceTypeGenerated = ...
    """"""
    Url: EvidenceTypeGenerated = ...
    """"""
    Zone: EvidenceTypeGenerated = ...
    """"""

class FileCodeGroup(CodeGroup, IUnionSemanticCodeGroup):
    """"""
    def __init__(
        self, membershipCondition: IMembershipCondition, access: FileIOPermissionAccess
    ) -> None:
        """"""
    @property
    def AttributeString(self) -> str:
        """"""
    @property
    def Children(self) -> IList:
        """"""
    @Children.setter
    def Children(self, value: IList) -> None: ...
    @property
    def Description(self) -> str:
        """"""
    @Description.setter
    def Description(self, value: str) -> None: ...
    @property
    def MembershipCondition(self) -> IMembershipCondition:
        """"""
    @MembershipCondition.setter
    def MembershipCondition(self, value: IMembershipCondition) -> None: ...
    @property
    def MergeLogic(self) -> str:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def PermissionSetName(self) -> str:
        """"""
    @property
    def PolicyStatement(self) -> PolicyStatement:
        """"""
    @PolicyStatement.setter
    def PolicyStatement(self, value: PolicyStatement) -> None: ...
    def AddChild(self, group: CodeGroup) -> None:
        """"""
    def Copy(self) -> CodeGroup:
        """"""
    @overload
    def Equals(self, cg: CodeGroup, compareChildren: bool) -> bool:
        """"""
    @overload
    def Equals(self, o: object) -> bool:
        """"""
    @overload
    def FromXml(self, e: SecurityElement) -> None:
        """"""
    @overload
    def FromXml(self, e: SecurityElement, level: PolicyLevel) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def InternalResolve(self, evidence: Evidence) -> PolicyStatement:
        """"""
    def RemoveChild(self, group: CodeGroup) -> None:
        """"""
    def Resolve(self, evidence: Evidence) -> PolicyStatement:
        """"""
    def ResolveMatchingCodeGroups(self, evidence: Evidence) -> CodeGroup:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def ToXml(self) -> SecurityElement:
        """"""
    @overload
    def ToXml(self, level: PolicyLevel) -> SecurityElement:
        """"""

class FirstMatchCodeGroup(CodeGroup):
    """"""
    def __init__(self, membershipCondition: IMembershipCondition, policy: PolicyStatement) -> None:
        """"""
    @property
    def AttributeString(self) -> str:
        """"""
    @property
    def Children(self) -> IList:
        """"""
    @Children.setter
    def Children(self, value: IList) -> None: ...
    @property
    def Description(self) -> str:
        """"""
    @Description.setter
    def Description(self, value: str) -> None: ...
    @property
    def MembershipCondition(self) -> IMembershipCondition:
        """"""
    @MembershipCondition.setter
    def MembershipCondition(self, value: IMembershipCondition) -> None: ...
    @property
    def MergeLogic(self) -> str:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def PermissionSetName(self) -> str:
        """"""
    @property
    def PolicyStatement(self) -> PolicyStatement:
        """"""
    @PolicyStatement.setter
    def PolicyStatement(self, value: PolicyStatement) -> None: ...
    def AddChild(self, group: CodeGroup) -> None:
        """"""
    def Copy(self) -> CodeGroup:
        """"""
    @overload
    def Equals(self, cg: CodeGroup, compareChildren: bool) -> bool:
        """"""
    @overload
    def Equals(self, o: object) -> bool:
        """"""
    @overload
    def FromXml(self, e: SecurityElement) -> None:
        """"""
    @overload
    def FromXml(self, e: SecurityElement, level: PolicyLevel) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def RemoveChild(self, group: CodeGroup) -> None:
        """"""
    def Resolve(self, evidence: Evidence) -> PolicyStatement:
        """"""
    def ResolveMatchingCodeGroups(self, evidence: Evidence) -> CodeGroup:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def ToXml(self) -> SecurityElement:
        """"""
    @overload
    def ToXml(self, level: PolicyLevel) -> SecurityElement:
        """"""

class GacInstalled(EvidenceBase, IIdentityPermissionFactory):
    """"""
    def __init__(self) -> None:
        """"""
    def Clone(self) -> EvidenceBase:
        """"""
    def Copy(self) -> object:
        """"""
    def CreateIdentityPermission(self, evidence: Evidence) -> IPermission:
        """"""
    def Equals(self, o: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class GacMembershipCondition(
    Object,
    IConstantMembershipCondition,
    IMembershipCondition,
    IReportMatchMembershipCondition,
    ISecurityEncodable,
    ISecurityPolicyEncodable,
):
    """"""
    def __init__(self) -> None:
        """"""
    @overload
    def Check(self, evidence: Evidence) -> bool:
        """"""
    @overload
    def Check(self, evidence: Evidence, usedEvidence: Object) -> tuple[bool, Object]:
        """"""
    def Copy(self) -> IMembershipCondition:
        """"""
    def Equals(self, o: object) -> bool:
        """"""
    @overload
    def FromXml(self, e: SecurityElement) -> None:
        """"""
    @overload
    def FromXml(self, e: SecurityElement, level: PolicyLevel) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def ToXml(self) -> SecurityElement:
        """"""
    @overload
    def ToXml(self, level: PolicyLevel) -> SecurityElement:
        """"""

class Hash(EvidenceBase, ISerializable):
    """"""
    def __init__(self, assembly: Assembly) -> None:
        """"""
    @property
    def MD5(self) -> Array[int]:
        """"""
    @property
    def SHA1(self) -> Array[int]:
        """"""
    @property
    def SHA256(self) -> Array[int]:
        """"""
    def Clone(self) -> EvidenceBase:
        """"""
    @classmethod
    def CreateMD5(cls, md5: Array[int]) -> Hash:
        """"""
    @classmethod
    def CreateSHA1(cls, sha1: Array[int]) -> Hash:
        """"""
    @classmethod
    def CreateSHA256(cls, sha256: Array[int]) -> Hash:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GenerateHash(self, hashAlg: HashAlgorithm) -> Array[int]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class HashMembershipCondition(
    Object,
    IDeserializationCallback,
    ISerializable,
    IMembershipCondition,
    IReportMatchMembershipCondition,
    ISecurityEncodable,
    ISecurityPolicyEncodable,
):
    """"""
    def __init__(self, hashAlg: HashAlgorithm, value: Array[int]) -> None:
        """"""
    @property
    def HashAlgorithm(self) -> HashAlgorithm:
        """"""
    @HashAlgorithm.setter
    def HashAlgorithm(self, value: HashAlgorithm) -> None: ...
    @property
    def HashValue(self) -> Array[int]:
        """"""
    @HashValue.setter
    def HashValue(self, value: Array[int]) -> None: ...
    @overload
    def Check(self, evidence: Evidence) -> bool:
        """"""
    @overload
    def Check(self, evidence: Evidence, usedEvidence: Object) -> tuple[bool, Object]:
        """"""
    def Copy(self) -> IMembershipCondition:
        """"""
    def Equals(self, o: object) -> bool:
        """"""
    @overload
    def FromXml(self, e: SecurityElement) -> None:
        """"""
    @overload
    def FromXml(self, e: SecurityElement, level: PolicyLevel) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def OnDeserialization(self, sender: object) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def ToXml(self) -> SecurityElement:
        """"""
    @overload
    def ToXml(self, level: PolicyLevel) -> SecurityElement:
        """"""

class IApplicationTrustManager(ISecurityEncodable):
    """"""
    def DetermineApplicationTrust(
        self, activationContext: ActivationContext, context: TrustManagerContext
    ) -> ApplicationTrust:
        """"""
    def FromXml(self, e: SecurityElement) -> None:
        """"""
    def ToXml(self) -> SecurityElement:
        """"""

class IConstantMembershipCondition:
    """"""

class IDelayEvaluatedEvidence:
    """"""
    @property
    def IsVerified(self) -> bool:
        """"""
    @property
    def WasUsed(self) -> bool:
        """"""
    def MarkUsed(self) -> None:
        """"""

class IIdentityPermissionFactory:
    """"""
    def CreateIdentityPermission(self, evidence: Evidence) -> IPermission:
        """"""

class ILegacyEvidenceAdapter:
    """"""
    @property
    def EvidenceObject(self) -> object:
        """"""
    @property
    def EvidenceType(self) -> Type:
        """"""

class IMembershipCondition(ISecurityEncodable, ISecurityPolicyEncodable):
    """"""
    def Check(self, evidence: Evidence) -> bool:
        """"""
    def Copy(self) -> IMembershipCondition:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def FromXml(self, e: SecurityElement) -> None:
        """"""
    @overload
    def FromXml(self, e: SecurityElement, level: PolicyLevel) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def ToXml(self) -> SecurityElement:
        """"""
    @overload
    def ToXml(self, level: PolicyLevel) -> SecurityElement:
        """"""

class IReportMatchMembershipCondition(
    IMembershipCondition, ISecurityEncodable, ISecurityPolicyEncodable
):
    """"""
    @overload
    def Check(self, evidence: Evidence) -> bool:
        """"""
    @overload
    def Check(self, evidence: Evidence, usedEvidence: Object) -> tuple[bool, Object]:
        """"""
    def Copy(self) -> IMembershipCondition:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def FromXml(self, e: SecurityElement) -> None:
        """"""
    @overload
    def FromXml(self, e: SecurityElement, level: PolicyLevel) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def ToXml(self) -> SecurityElement:
        """"""
    @overload
    def ToXml(self, level: PolicyLevel) -> SecurityElement:
        """"""

class IRuntimeEvidenceFactory:
    """"""
    @property
    def Target(self) -> IEvidenceFactory:
        """"""
    def GenerateEvidence(self, evidenceType: Type) -> EvidenceBase:
        """"""
    def GetFactorySuppliedEvidence(self) -> IEnumerable[EvidenceBase]:
        """"""

class IUnionSemanticCodeGroup:
    """"""
    def InternalResolve(self, evidence: Evidence) -> PolicyStatement:
        """"""

class LegacyEvidenceList(
    EvidenceBase, IEnumerable[EvidenceBase], IEnumerable, ILegacyEvidenceAdapter
):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def EvidenceObject(self) -> object:
        """"""
    @property
    def EvidenceType(self) -> Type:
        """"""
    def Add(self, evidence: EvidenceBase) -> None:
        """"""
    def Clone(self) -> EvidenceBase:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator[EvidenceBase]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def __iter__(self) -> Iterator[EvidenceBase]:
        """"""

class LegacyEvidenceWrapper(EvidenceBase, ILegacyEvidenceAdapter):
    """"""
    @property
    def EvidenceObject(self) -> object:
        """"""
    @property
    def EvidenceType(self) -> Type:
        """"""
    def Clone(self) -> EvidenceBase:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class NetCodeGroup(CodeGroup, IUnionSemanticCodeGroup):
    """"""

    AbsentOriginScheme: ClassVar[str]
    """"""
    AnyOtherOriginScheme: ClassVar[str]
    """"""
    def __init__(self, membershipCondition: IMembershipCondition) -> None:
        """"""
    @property
    def AttributeString(self) -> str:
        """"""
    @property
    def Children(self) -> IList:
        """"""
    @Children.setter
    def Children(self, value: IList) -> None: ...
    @property
    def Description(self) -> str:
        """"""
    @Description.setter
    def Description(self, value: str) -> None: ...
    @property
    def MembershipCondition(self) -> IMembershipCondition:
        """"""
    @MembershipCondition.setter
    def MembershipCondition(self, value: IMembershipCondition) -> None: ...
    @property
    def MergeLogic(self) -> str:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def PermissionSetName(self) -> str:
        """"""
    @property
    def PolicyStatement(self) -> PolicyStatement:
        """"""
    @PolicyStatement.setter
    def PolicyStatement(self, value: PolicyStatement) -> None: ...
    def AddChild(self, group: CodeGroup) -> None:
        """"""
    def AddConnectAccess(self, originScheme: str, connectAccess: CodeConnectAccess) -> None:
        """"""
    def Copy(self) -> CodeGroup:
        """"""
    @overload
    def Equals(self, cg: CodeGroup, compareChildren: bool) -> bool:
        """"""
    @overload
    def Equals(self, o: object) -> bool:
        """"""
    @overload
    def FromXml(self, e: SecurityElement) -> None:
        """"""
    @overload
    def FromXml(self, e: SecurityElement, level: PolicyLevel) -> None:
        """"""
    def GetConnectAccessRules(self) -> Array[DictionaryEntry]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def InternalResolve(self, evidence: Evidence) -> PolicyStatement:
        """"""
    def RemoveChild(self, group: CodeGroup) -> None:
        """"""
    def ResetConnectAccess(self) -> None:
        """"""
    def Resolve(self, evidence: Evidence) -> PolicyStatement:
        """"""
    def ResolveMatchingCodeGroups(self, evidence: Evidence) -> CodeGroup:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def ToXml(self) -> SecurityElement:
        """"""
    @overload
    def ToXml(self, level: PolicyLevel) -> SecurityElement:
        """"""

class PEFileEvidenceFactory(Object, IRuntimeEvidenceFactory):
    """"""
    @property
    def Target(self) -> IEvidenceFactory:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GenerateEvidence(self, evidenceType: Type) -> EvidenceBase:
        """"""
    def GetFactorySuppliedEvidence(self) -> IEnumerable[EvidenceBase]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class PermissionRequestEvidence(EvidenceBase):
    """"""
    def __init__(
        self, request: PermissionSet, optional: PermissionSet, denied: PermissionSet
    ) -> None:
        """"""
    @property
    def DeniedPermissions(self) -> PermissionSet:
        """"""
    @property
    def OptionalPermissions(self) -> PermissionSet:
        """"""
    @property
    def RequestedPermissions(self) -> PermissionSet:
        """"""
    def Clone(self) -> EvidenceBase:
        """"""
    def Copy(self) -> PermissionRequestEvidence:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class PolicyException(SystemException, _Exception, ISerializable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, message: str) -> None:
        """"""
    @overload
    def __init__(self, message: str, exception: Exception) -> None:
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

class PolicyLevel(Object):
    """"""
    @property
    def FullTrustAssemblies(self) -> IList:
        """"""
    @property
    def Label(self) -> str:
        """"""
    @property
    def NamedPermissionSets(self) -> IList:
        """"""
    @property
    def RootCodeGroup(self) -> CodeGroup:
        """"""
    @RootCodeGroup.setter
    def RootCodeGroup(self, value: CodeGroup) -> None: ...
    @property
    def StoreLocation(self) -> str:
        """"""
    @property
    def Type(self) -> PolicyLevelType:
        """"""
    @overload
    def AddFullTrustAssembly(self, sn: StrongName) -> None:
        """"""
    @overload
    def AddFullTrustAssembly(self, snMC: StrongNameMembershipCondition) -> None:
        """"""
    def AddNamedPermissionSet(self, permSet: NamedPermissionSet) -> None:
        """"""
    def ChangeNamedPermissionSet(self, name: str, pSet: PermissionSet) -> NamedPermissionSet:
        """"""
    @classmethod
    def CreateAppDomainLevel(cls) -> PolicyLevel:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def FromXml(self, e: SecurityElement) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetNamedPermissionSet(self, name: str) -> NamedPermissionSet:
        """"""
    def GetType(self) -> Type:
        """"""
    def Recover(self) -> None:
        """"""
    @overload
    def RemoveFullTrustAssembly(self, sn: StrongName) -> None:
        """"""
    @overload
    def RemoveFullTrustAssembly(self, snMC: StrongNameMembershipCondition) -> None:
        """"""
    @overload
    def RemoveNamedPermissionSet(self, permSet: NamedPermissionSet) -> NamedPermissionSet:
        """"""
    @overload
    def RemoveNamedPermissionSet(self, name: str) -> NamedPermissionSet:
        """"""
    def Reset(self) -> None:
        """"""
    def Resolve(self, evidence: Evidence) -> PolicyStatement:
        """"""
    def ResolveMatchingCodeGroups(self, evidence: Evidence) -> CodeGroup:
        """"""
    def ToString(self) -> str:
        """"""
    def ToXml(self) -> SecurityElement:
        """"""

class PolicyStatement(Object, ISecurityEncodable, ISecurityPolicyEncodable):
    """"""
    @overload
    def __init__(self, permSet: PermissionSet) -> None:
        """"""
    @overload
    def __init__(self, permSet: PermissionSet, attributes: PolicyStatementAttribute) -> None:
        """"""
    @property
    def AttributeString(self) -> str:
        """"""
    @property
    def Attributes(self) -> PolicyStatementAttribute:
        """"""
    @Attributes.setter
    def Attributes(self, value: PolicyStatementAttribute) -> None: ...
    @property
    def PermissionSet(self) -> PermissionSet:
        """"""
    @PermissionSet.setter
    def PermissionSet(self, value: PermissionSet) -> None: ...
    def Copy(self) -> PolicyStatement:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def FromXml(self, et: SecurityElement) -> None:
        """"""
    @overload
    def FromXml(self, et: SecurityElement, level: PolicyLevel) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def ToXml(self) -> SecurityElement:
        """"""
    @overload
    def ToXml(self, level: PolicyLevel) -> SecurityElement:
        """"""

class PolicyStatementAttribute(Enum):
    """"""

    Nothing: PolicyStatementAttribute = ...
    """"""
    Exclusive: PolicyStatementAttribute = ...
    """"""
    LevelFinal: PolicyStatementAttribute = ...
    """"""
    All: PolicyStatementAttribute = ...
    """"""

class Publisher(EvidenceBase, IIdentityPermissionFactory):
    """"""
    def __init__(self, cert: X509Certificate) -> None:
        """"""
    @property
    def Certificate(self) -> X509Certificate:
        """"""
    def Clone(self) -> EvidenceBase:
        """"""
    def Copy(self) -> object:
        """"""
    def CreateIdentityPermission(self, evidence: Evidence) -> IPermission:
        """"""
    def Equals(self, o: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class PublisherMembershipCondition(
    Object,
    IConstantMembershipCondition,
    IMembershipCondition,
    IReportMatchMembershipCondition,
    ISecurityEncodable,
    ISecurityPolicyEncodable,
):
    """"""
    def __init__(self, certificate: X509Certificate) -> None:
        """"""
    @property
    def Certificate(self) -> X509Certificate:
        """"""
    @Certificate.setter
    def Certificate(self, value: X509Certificate) -> None: ...
    @overload
    def Check(self, evidence: Evidence) -> bool:
        """"""
    @overload
    def Check(self, evidence: Evidence, usedEvidence: Object) -> tuple[bool, Object]:
        """"""
    def Copy(self) -> IMembershipCondition:
        """"""
    def Equals(self, o: object) -> bool:
        """"""
    @overload
    def FromXml(self, e: SecurityElement) -> None:
        """"""
    @overload
    def FromXml(self, e: SecurityElement, level: PolicyLevel) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def ToXml(self) -> SecurityElement:
        """"""
    @overload
    def ToXml(self, level: PolicyLevel) -> SecurityElement:
        """"""

class Site(EvidenceBase, IIdentityPermissionFactory):
    """"""
    def __init__(self, name: str) -> None:
        """"""
    @property
    def Name(self) -> str:
        """"""
    def Clone(self) -> EvidenceBase:
        """"""
    def Copy(self) -> object:
        """"""
    @classmethod
    def CreateFromUrl(cls, url: str) -> Site:
        """"""
    def CreateIdentityPermission(self, evidence: Evidence) -> IPermission:
        """"""
    def Equals(self, o: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SiteMembershipCondition(
    Object,
    IConstantMembershipCondition,
    IMembershipCondition,
    IReportMatchMembershipCondition,
    ISecurityEncodable,
    ISecurityPolicyEncodable,
):
    """"""
    def __init__(self, site: str) -> None:
        """"""
    @property
    def Site(self) -> str:
        """"""
    @Site.setter
    def Site(self, value: str) -> None: ...
    @overload
    def Check(self, evidence: Evidence) -> bool:
        """"""
    @overload
    def Check(self, evidence: Evidence, usedEvidence: Object) -> tuple[bool, Object]:
        """"""
    def Copy(self) -> IMembershipCondition:
        """"""
    def Equals(self, o: object) -> bool:
        """"""
    @overload
    def FromXml(self, e: SecurityElement) -> None:
        """"""
    @overload
    def FromXml(self, e: SecurityElement, level: PolicyLevel) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def ToXml(self) -> SecurityElement:
        """"""
    @overload
    def ToXml(self, level: PolicyLevel) -> SecurityElement:
        """"""

class StrongName(EvidenceBase, IDelayEvaluatedEvidence, IIdentityPermissionFactory):
    """"""
    def __init__(self, blob: StrongNamePublicKeyBlob, name: str, version: Version) -> None:
        """"""
    @property
    def IsVerified(self) -> bool:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def PublicKey(self) -> StrongNamePublicKeyBlob:
        """"""
    @property
    def Version(self) -> Version:
        """"""
    @property
    def WasUsed(self) -> bool:
        """"""
    def Clone(self) -> EvidenceBase:
        """"""
    def Copy(self) -> object:
        """"""
    def CreateIdentityPermission(self, evidence: Evidence) -> IPermission:
        """"""
    def Equals(self, o: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def MarkUsed(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class StrongNameMembershipCondition(
    Object,
    IConstantMembershipCondition,
    IMembershipCondition,
    IReportMatchMembershipCondition,
    ISecurityEncodable,
    ISecurityPolicyEncodable,
):
    """"""
    def __init__(self, blob: StrongNamePublicKeyBlob, name: str, version: Version) -> None:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def PublicKey(self) -> StrongNamePublicKeyBlob:
        """"""
    @PublicKey.setter
    def PublicKey(self, value: StrongNamePublicKeyBlob) -> None: ...
    @property
    def Version(self) -> Version:
        """"""
    @Version.setter
    def Version(self, value: Version) -> None: ...
    @overload
    def Check(self, evidence: Evidence) -> bool:
        """"""
    @overload
    def Check(self, evidence: Evidence, usedEvidence: Object) -> tuple[bool, Object]:
        """"""
    def Copy(self) -> IMembershipCondition:
        """"""
    def Equals(self, o: object) -> bool:
        """"""
    @overload
    def FromXml(self, e: SecurityElement) -> None:
        """"""
    @overload
    def FromXml(self, e: SecurityElement, level: PolicyLevel) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def ToXml(self) -> SecurityElement:
        """"""
    @overload
    def ToXml(self, level: PolicyLevel) -> SecurityElement:
        """"""

class TrustManagerContext(Object):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, uiContext: TrustManagerUIContext) -> None:
        """"""
    @property
    def IgnorePersistedDecision(self) -> bool:
        """"""
    @IgnorePersistedDecision.setter
    def IgnorePersistedDecision(self, value: bool) -> None: ...
    @property
    def KeepAlive(self) -> bool:
        """"""
    @KeepAlive.setter
    def KeepAlive(self, value: bool) -> None: ...
    @property
    def NoPrompt(self) -> bool:
        """"""
    @NoPrompt.setter
    def NoPrompt(self, value: bool) -> None: ...
    @property
    def Persist(self) -> bool:
        """"""
    @Persist.setter
    def Persist(self, value: bool) -> None: ...
    @property
    def PreviousApplicationIdentity(self) -> ApplicationIdentity:
        """"""
    @PreviousApplicationIdentity.setter
    def PreviousApplicationIdentity(self, value: ApplicationIdentity) -> None: ...
    @property
    def UIContext(self) -> TrustManagerUIContext:
        """"""
    @UIContext.setter
    def UIContext(self, value: TrustManagerUIContext) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class TrustManagerUIContext(Enum):
    """"""

    Install: TrustManagerUIContext = ...
    """"""
    Upgrade: TrustManagerUIContext = ...
    """"""
    Run: TrustManagerUIContext = ...
    """"""

class UnionCodeGroup(CodeGroup, IUnionSemanticCodeGroup):
    """"""
    def __init__(self, membershipCondition: IMembershipCondition, policy: PolicyStatement) -> None:
        """"""
    @property
    def AttributeString(self) -> str:
        """"""
    @property
    def Children(self) -> IList:
        """"""
    @Children.setter
    def Children(self, value: IList) -> None: ...
    @property
    def Description(self) -> str:
        """"""
    @Description.setter
    def Description(self, value: str) -> None: ...
    @property
    def MembershipCondition(self) -> IMembershipCondition:
        """"""
    @MembershipCondition.setter
    def MembershipCondition(self, value: IMembershipCondition) -> None: ...
    @property
    def MergeLogic(self) -> str:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def PermissionSetName(self) -> str:
        """"""
    @property
    def PolicyStatement(self) -> PolicyStatement:
        """"""
    @PolicyStatement.setter
    def PolicyStatement(self, value: PolicyStatement) -> None: ...
    def AddChild(self, group: CodeGroup) -> None:
        """"""
    def Copy(self) -> CodeGroup:
        """"""
    @overload
    def Equals(self, cg: CodeGroup, compareChildren: bool) -> bool:
        """"""
    @overload
    def Equals(self, o: object) -> bool:
        """"""
    @overload
    def FromXml(self, e: SecurityElement) -> None:
        """"""
    @overload
    def FromXml(self, e: SecurityElement, level: PolicyLevel) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def InternalResolve(self, evidence: Evidence) -> PolicyStatement:
        """"""
    def RemoveChild(self, group: CodeGroup) -> None:
        """"""
    def Resolve(self, evidence: Evidence) -> PolicyStatement:
        """"""
    def ResolveMatchingCodeGroups(self, evidence: Evidence) -> CodeGroup:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def ToXml(self) -> SecurityElement:
        """"""
    @overload
    def ToXml(self, level: PolicyLevel) -> SecurityElement:
        """"""

class Url(EvidenceBase, IIdentityPermissionFactory):
    """"""
    def __init__(self, name: str) -> None:
        """"""
    @property
    def Value(self) -> str:
        """"""
    def Clone(self) -> EvidenceBase:
        """"""
    def Copy(self) -> object:
        """"""
    def CreateIdentityPermission(self, evidence: Evidence) -> IPermission:
        """"""
    def Equals(self, o: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class UrlMembershipCondition(
    Object,
    IConstantMembershipCondition,
    IMembershipCondition,
    IReportMatchMembershipCondition,
    ISecurityEncodable,
    ISecurityPolicyEncodable,
):
    """"""
    def __init__(self, url: str) -> None:
        """"""
    @property
    def Url(self) -> str:
        """"""
    @Url.setter
    def Url(self, value: str) -> None: ...
    @overload
    def Check(self, evidence: Evidence) -> bool:
        """"""
    @overload
    def Check(self, evidence: Evidence, usedEvidence: Object) -> tuple[bool, Object]:
        """"""
    def Copy(self) -> IMembershipCondition:
        """"""
    def Equals(self, o: object) -> bool:
        """"""
    @overload
    def FromXml(self, e: SecurityElement) -> None:
        """"""
    @overload
    def FromXml(self, e: SecurityElement, level: PolicyLevel) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def ToXml(self) -> SecurityElement:
        """"""
    @overload
    def ToXml(self, level: PolicyLevel) -> SecurityElement:
        """"""

class Zone(EvidenceBase, IIdentityPermissionFactory):
    """"""
    def __init__(self, zone: SecurityZone) -> None:
        """"""
    @property
    def SecurityZone(self) -> SecurityZone:
        """"""
    def Clone(self) -> EvidenceBase:
        """"""
    def Copy(self) -> object:
        """"""
    @classmethod
    def CreateFromUrl(cls, url: str) -> Zone:
        """"""
    def CreateIdentityPermission(self, evidence: Evidence) -> IPermission:
        """"""
    def Equals(self, o: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ZoneMembershipCondition(
    Object,
    IConstantMembershipCondition,
    IMembershipCondition,
    IReportMatchMembershipCondition,
    ISecurityEncodable,
    ISecurityPolicyEncodable,
):
    """"""
    def __init__(self, zone: SecurityZone) -> None:
        """"""
    @property
    def SecurityZone(self) -> SecurityZone:
        """"""
    @SecurityZone.setter
    def SecurityZone(self, value: SecurityZone) -> None: ...
    @overload
    def Check(self, evidence: Evidence) -> bool:
        """"""
    @overload
    def Check(self, evidence: Evidence, usedEvidence: Object) -> tuple[bool, Object]:
        """"""
    def Copy(self) -> IMembershipCondition:
        """"""
    def Equals(self, o: object) -> bool:
        """"""
    @overload
    def FromXml(self, e: SecurityElement) -> None:
        """"""
    @overload
    def FromXml(self, e: SecurityElement, level: PolicyLevel) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def ToXml(self) -> SecurityElement:
        """"""
    @overload
    def ToXml(self, level: PolicyLevel) -> SecurityElement:
        """"""
