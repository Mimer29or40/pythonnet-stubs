from __future__ import annotations

from abc import ABC
from typing import ClassVar
from typing import Final
from typing import Iterator
from typing import Tuple
from typing import TypeVar
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

T = TypeVar("T")

class AllMembershipCondition(
    Object,
    IConstantMembershipCondition,
    IMembershipCondition,
    IReportMatchMembershipCondition,
    ISecurityEncodable,
    ISecurityPolicyEncodable,
):
    """"""

    def __init__(self):
        """"""
    @overload
    def Check(self, evidence: Evidence) -> bool:
        """

        :param evidence:
        :return:
        """
    @overload
    def Check(self, evidence: Evidence, usedEvidence: object) -> Tuple[bool, object]:
        """

        :param evidence:
        :param usedEvidence:
        :return:
        """
    def Copy(self) -> IMembershipCondition:
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
    @overload
    def FromXml(self, e: SecurityElement) -> None:
        """

        :param e:
        """
    @overload
    def FromXml(self, e: SecurityElement, level: PolicyLevel) -> None:
        """

        :param e:
        :param level:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
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
    @overload
    def ToXml(self) -> SecurityElement:
        """

        :return:
        """
    @overload
    def ToXml(self, level: PolicyLevel) -> SecurityElement:
        """

        :param level:
        :return:
        """

class AppDomainEvidenceFactory(Object, IRuntimeEvidenceFactory):
    """"""

    @property
    def Target(self) -> IEvidenceFactory:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GenerateEvidence(self, evidenceType: Type) -> EvidenceBase:
        """

        :param evidenceType:
        :return:
        """
    def GetFactorySuppliedEvidence(self) -> IEnumerable[EvidenceBase]:
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

class ApplicationDirectory(EvidenceBase):
    """"""

    def __init__(self, name: str):
        """

        :param name:
        """
    @property
    def Directory(self) -> str:
        """

        :return:
        """
    def Clone(self) -> EvidenceBase:
        """

        :return:
        """
    def Copy(self) -> object:
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

class ApplicationDirectoryMembershipCondition(
    Object,
    IConstantMembershipCondition,
    IMembershipCondition,
    IReportMatchMembershipCondition,
    ISecurityEncodable,
    ISecurityPolicyEncodable,
):
    """"""

    def __init__(self):
        """"""
    @overload
    def Check(self, evidence: Evidence) -> bool:
        """

        :param evidence:
        :return:
        """
    @overload
    def Check(self, evidence: Evidence, usedEvidence: object) -> Tuple[bool, object]:
        """

        :param evidence:
        :param usedEvidence:
        :return:
        """
    def Copy(self) -> IMembershipCondition:
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
    @overload
    def FromXml(self, e: SecurityElement) -> None:
        """

        :param e:
        """
    @overload
    def FromXml(self, e: SecurityElement, level: PolicyLevel) -> None:
        """

        :param e:
        :param level:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
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
    @overload
    def ToXml(self) -> SecurityElement:
        """

        :return:
        """
    @overload
    def ToXml(self, level: PolicyLevel) -> SecurityElement:
        """

        :param level:
        :return:
        """

class ApplicationSecurityInfo(Object):
    """"""

    def __init__(self, activationContext: ActivationContext):
        """

        :param activationContext:
        """
    @property
    def ApplicationEvidence(self) -> Evidence:
        """

        :return:
        """
    @ApplicationEvidence.setter
    def ApplicationEvidence(self, value: Evidence) -> None: ...
    @property
    def ApplicationId(self) -> ApplicationId:
        """

        :return:
        """
    @ApplicationId.setter
    def ApplicationId(self, value: ApplicationId) -> None: ...
    @property
    def DefaultRequestSet(self) -> PermissionSet:
        """

        :return:
        """
    @DefaultRequestSet.setter
    def DefaultRequestSet(self, value: PermissionSet) -> None: ...
    @property
    def DeploymentId(self) -> ApplicationId:
        """

        :return:
        """
    @DeploymentId.setter
    def DeploymentId(self, value: ApplicationId) -> None: ...
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

class ApplicationSecurityManager(ABC, Object):
    """"""

    @classmethod
    @property
    def ApplicationTrustManager(cls) -> IApplicationTrustManager:
        """

        :return:
        """
    @classmethod
    @property
    def UserApplicationTrusts(cls) -> ApplicationTrustCollection:
        """

        :return:
        """
    @classmethod
    def DetermineApplicationTrust(
        cls, activationContext: ActivationContext, context: TrustManagerContext
    ) -> bool:
        """

        :param activationContext:
        :param context:
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

class ApplicationTrust(EvidenceBase, ISecurityEncodable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, applicationIdentity: ApplicationIdentity):
        """

        :param applicationIdentity:
        """
    @overload
    def __init__(
        self, defaultGrantSet: PermissionSet, fullTrustAssemblies: IEnumerable[StrongName]
    ):
        """

        :param defaultGrantSet:
        :param fullTrustAssemblies:
        """
    @property
    def ApplicationIdentity(self) -> ApplicationIdentity:
        """

        :return:
        """
    @ApplicationIdentity.setter
    def ApplicationIdentity(self, value: ApplicationIdentity) -> None: ...
    @property
    def DefaultGrantSet(self) -> PolicyStatement:
        """

        :return:
        """
    @DefaultGrantSet.setter
    def DefaultGrantSet(self, value: PolicyStatement) -> None: ...
    @property
    def ExtraInfo(self) -> object:
        """

        :return:
        """
    @ExtraInfo.setter
    def ExtraInfo(self, value: object) -> None: ...
    @property
    def FullTrustAssemblies(self) -> IList[StrongName]:
        """

        :return:
        """
    @property
    def IsApplicationTrustedToRun(self) -> bool:
        """

        :return:
        """
    @IsApplicationTrustedToRun.setter
    def IsApplicationTrustedToRun(self, value: bool) -> None: ...
    @property
    def Persist(self) -> bool:
        """

        :return:
        """
    @Persist.setter
    def Persist(self, value: bool) -> None: ...
    def Clone(self) -> EvidenceBase:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def FromXml(self, e: SecurityElement) -> None:
        """

        :param e:
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
    def ToXml(self) -> SecurityElement:
        """

        :return:
        """

class ApplicationTrustCollection(Object, ICollection, IEnumerable):
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
    def Item(self) -> ApplicationTrust:
        """

        :return:
        """
    @property
    def SyncRoot(self) -> object:
        """

        :return:
        """
    def Add(self, trust: ApplicationTrust) -> int:
        """

        :param trust:
        :return:
        """
    @overload
    def AddRange(self, trusts: ApplicationTrustCollection) -> None:
        """

        :param trusts:
        """
    @overload
    def AddRange(self, trusts: Array[ApplicationTrust]) -> None:
        """

        :param trusts:
        """
    def Clear(self) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    @overload
    def CopyTo(self, array: Array[ApplicationTrust], index: int) -> None:
        """

        :param array:
        :param index:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def Find(
        self, applicationIdentity: ApplicationIdentity, versionMatch: ApplicationVersionMatch
    ) -> ApplicationTrustCollection:
        """

        :param applicationIdentity:
        :param versionMatch:
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
    @overload
    def Remove(self, trust: ApplicationTrust) -> None:
        """

        :param trust:
        """
    @overload
    def Remove(
        self, applicationIdentity: ApplicationIdentity, versionMatch: ApplicationVersionMatch
    ) -> None:
        """

        :param applicationIdentity:
        :param versionMatch:
        """
    @overload
    def RemoveRange(self, trusts: ApplicationTrustCollection) -> None:
        """

        :param trusts:
        """
    @overload
    def RemoveRange(self, trusts: Array[ApplicationTrust]) -> None:
        """

        :param trusts:
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
    @overload
    def __getitem__(self, index: int) -> ApplicationTrust:
        """

        :param index:
        :return:
        """
    @overload
    def __getitem__(self, appFullName: str) -> ApplicationTrust:
        """

        :param appFullName:
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

class ApplicationTrustEnumerator(Object, IEnumerator):
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
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GenerateEvidence(self, evidenceType: Type) -> EvidenceBase:
        """

        :param evidenceType:
        :return:
        """
    def GetFactorySuppliedEvidence(self) -> IEnumerable[EvidenceBase]:
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

class CodeConnectAccess(Object):
    """"""

    AnyScheme: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    DefaultPort: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    OriginPort: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    OriginScheme: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    def __init__(self, allowScheme: str, allowPort: int):
        """

        :param allowScheme:
        :param allowPort:
        """
    @property
    def Port(self) -> int:
        """

        :return:
        """
    @property
    def Scheme(self) -> str:
        """

        :return:
        """
    @classmethod
    def CreateAnySchemeAccess(cls, allowPort: int) -> CodeConnectAccess:
        """

        :param allowPort:
        :return:
        """
    @classmethod
    def CreateOriginSchemeAccess(cls, allowPort: int) -> CodeConnectAccess:
        """

        :param allowPort:
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

class CodeGroup(ABC, Object):
    """"""

    @property
    def AttributeString(self) -> str:
        """

        :return:
        """
    @property
    def Children(self) -> IList:
        """

        :return:
        """
    @Children.setter
    def Children(self, value: IList) -> None: ...
    @property
    def Description(self) -> str:
        """

        :return:
        """
    @Description.setter
    def Description(self, value: str) -> None: ...
    @property
    def MembershipCondition(self) -> IMembershipCondition:
        """

        :return:
        """
    @MembershipCondition.setter
    def MembershipCondition(self, value: IMembershipCondition) -> None: ...
    @property
    def MergeLogic(self) -> str:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def PermissionSetName(self) -> str:
        """

        :return:
        """
    @property
    def PolicyStatement(self) -> PolicyStatement:
        """

        :return:
        """
    @PolicyStatement.setter
    def PolicyStatement(self, value: PolicyStatement) -> None: ...
    def AddChild(self, group: CodeGroup) -> None:
        """

        :param group:
        """
    def Copy(self) -> CodeGroup:
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
    def Equals(self, cg: CodeGroup, compareChildren: bool) -> bool:
        """

        :param cg:
        :param compareChildren:
        :return:
        """
    @overload
    def FromXml(self, e: SecurityElement) -> None:
        """

        :param e:
        """
    @overload
    def FromXml(self, e: SecurityElement, level: PolicyLevel) -> None:
        """

        :param e:
        :param level:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def RemoveChild(self, group: CodeGroup) -> None:
        """

        :param group:
        """
    def Resolve(self, evidence: Evidence) -> PolicyStatement:
        """

        :param evidence:
        :return:
        """
    def ResolveMatchingCodeGroups(self, evidence: Evidence) -> CodeGroup:
        """

        :param evidence:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def ToXml(self) -> SecurityElement:
        """

        :return:
        """
    @overload
    def ToXml(self, level: PolicyLevel) -> SecurityElement:
        """

        :param level:
        :return:
        """

class CodeGroupPositionMarker(Object):
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

class CodeGroupStack(Object):
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

class CodeGroupStackFrame(Object):
    """"""

    def __init__(self):
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
    def __init__(self):
        """"""
    @overload
    def __init__(self, evidence: Evidence):
        """

        :param evidence:
        """
    @overload
    def __init__(self, hostEvidence: Array[EvidenceBase], assemblyEvidence: Array[EvidenceBase]):
        """

        :param hostEvidence:
        :param assemblyEvidence:
        """
    @overload
    def __init__(self, hostEvidence: Array[object], assemblyEvidence: Array[object]):
        """

        :param hostEvidence:
        :param assemblyEvidence:
        """
    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def IsSynchronized(self) -> bool:
        """

        :return:
        """
    @property
    def Locked(self) -> bool:
        """

        :return:
        """
    @Locked.setter
    def Locked(self, value: bool) -> None: ...
    @property
    def SyncRoot(self) -> object:
        """

        :return:
        """
    def AddAssembly(self, id: object) -> None:
        """

        :param id:
        """
    def AddAssemblyEvidence(self, evidence: T) -> None:
        """

        :param evidence:
        """
    def AddHost(self, id: object) -> None:
        """

        :param id:
        """
    def AddHostEvidence(self, evidence: T) -> None:
        """

        :param evidence:
        """
    def Clear(self) -> None:
        """"""
    def Clone(self) -> Evidence:
        """

        :return:
        """
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetAssemblyEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    def GetAssemblyEvidence(self) -> T:
        """

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
    def GetHostEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    def GetHostEvidence(self) -> T:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def Merge(self, evidence: Evidence) -> None:
        """

        :param evidence:
        """
    def RemoveType(self, t: Type) -> None:
        """

        :param t:
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
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    def __len__(self) -> int:
        """

        :return:
        """

class EvidenceBase(ABC, Object):
    """"""

    def Clone(self) -> EvidenceBase:
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

class EvidenceTypeDescriptor(Object):
    """"""

    def __init__(self):
        """"""
    @property
    def AssemblyEvidence(self) -> EvidenceBase:
        """

        :return:
        """
    @AssemblyEvidence.setter
    def AssemblyEvidence(self, value: EvidenceBase) -> None: ...
    @property
    def Generated(self) -> bool:
        """

        :return:
        """
    @Generated.setter
    def Generated(self, value: bool) -> None: ...
    @property
    def HostCanGenerate(self) -> bool:
        """

        :return:
        """
    @HostCanGenerate.setter
    def HostCanGenerate(self, value: bool) -> None: ...
    @property
    def HostEvidence(self) -> EvidenceBase:
        """

        :return:
        """
    @HostEvidence.setter
    def HostEvidence(self, value: EvidenceBase) -> None: ...
    def Clone(self) -> EvidenceTypeDescriptor:
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

    def __init__(self, membershipCondition: IMembershipCondition, access: FileIOPermissionAccess):
        """

        :param membershipCondition:
        :param access:
        """
    @property
    def AttributeString(self) -> str:
        """

        :return:
        """
    @property
    def Children(self) -> IList:
        """

        :return:
        """
    @Children.setter
    def Children(self, value: IList) -> None: ...
    @property
    def Description(self) -> str:
        """

        :return:
        """
    @Description.setter
    def Description(self, value: str) -> None: ...
    @property
    def MembershipCondition(self) -> IMembershipCondition:
        """

        :return:
        """
    @MembershipCondition.setter
    def MembershipCondition(self, value: IMembershipCondition) -> None: ...
    @property
    def MergeLogic(self) -> str:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def PermissionSetName(self) -> str:
        """

        :return:
        """
    @property
    def PolicyStatement(self) -> PolicyStatement:
        """

        :return:
        """
    @PolicyStatement.setter
    def PolicyStatement(self, value: PolicyStatement) -> None: ...
    def AddChild(self, group: CodeGroup) -> None:
        """

        :param group:
        """
    def Copy(self) -> CodeGroup:
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
    def Equals(self, cg: CodeGroup, compareChildren: bool) -> bool:
        """

        :param cg:
        :param compareChildren:
        :return:
        """
    @overload
    def FromXml(self, e: SecurityElement) -> None:
        """

        :param e:
        """
    @overload
    def FromXml(self, e: SecurityElement, level: PolicyLevel) -> None:
        """

        :param e:
        :param level:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def InternalResolve(self, evidence: Evidence) -> PolicyStatement:
        """

        :param evidence:
        :return:
        """
    def RemoveChild(self, group: CodeGroup) -> None:
        """

        :param group:
        """
    def Resolve(self, evidence: Evidence) -> PolicyStatement:
        """

        :param evidence:
        :return:
        """
    def ResolveMatchingCodeGroups(self, evidence: Evidence) -> CodeGroup:
        """

        :param evidence:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def ToXml(self) -> SecurityElement:
        """

        :return:
        """
    @overload
    def ToXml(self, level: PolicyLevel) -> SecurityElement:
        """

        :param level:
        :return:
        """

class FirstMatchCodeGroup(CodeGroup):
    """"""

    def __init__(self, membershipCondition: IMembershipCondition, policy: PolicyStatement):
        """

        :param membershipCondition:
        :param policy:
        """
    @property
    def AttributeString(self) -> str:
        """

        :return:
        """
    @property
    def Children(self) -> IList:
        """

        :return:
        """
    @Children.setter
    def Children(self, value: IList) -> None: ...
    @property
    def Description(self) -> str:
        """

        :return:
        """
    @Description.setter
    def Description(self, value: str) -> None: ...
    @property
    def MembershipCondition(self) -> IMembershipCondition:
        """

        :return:
        """
    @MembershipCondition.setter
    def MembershipCondition(self, value: IMembershipCondition) -> None: ...
    @property
    def MergeLogic(self) -> str:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def PermissionSetName(self) -> str:
        """

        :return:
        """
    @property
    def PolicyStatement(self) -> PolicyStatement:
        """

        :return:
        """
    @PolicyStatement.setter
    def PolicyStatement(self, value: PolicyStatement) -> None: ...
    def AddChild(self, group: CodeGroup) -> None:
        """

        :param group:
        """
    def Copy(self) -> CodeGroup:
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
    def Equals(self, cg: CodeGroup, compareChildren: bool) -> bool:
        """

        :param cg:
        :param compareChildren:
        :return:
        """
    @overload
    def FromXml(self, e: SecurityElement) -> None:
        """

        :param e:
        """
    @overload
    def FromXml(self, e: SecurityElement, level: PolicyLevel) -> None:
        """

        :param e:
        :param level:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def RemoveChild(self, group: CodeGroup) -> None:
        """

        :param group:
        """
    def Resolve(self, evidence: Evidence) -> PolicyStatement:
        """

        :param evidence:
        :return:
        """
    def ResolveMatchingCodeGroups(self, evidence: Evidence) -> CodeGroup:
        """

        :param evidence:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def ToXml(self) -> SecurityElement:
        """

        :return:
        """
    @overload
    def ToXml(self, level: PolicyLevel) -> SecurityElement:
        """

        :param level:
        :return:
        """

class GacInstalled(EvidenceBase, IIdentityPermissionFactory):
    """"""

    def __init__(self):
        """"""
    def Clone(self) -> EvidenceBase:
        """

        :return:
        """
    def Copy(self) -> object:
        """

        :return:
        """
    def CreateIdentityPermission(self, evidence: Evidence) -> IPermission:
        """

        :param evidence:
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

class GacMembershipCondition(
    Object,
    IConstantMembershipCondition,
    IMembershipCondition,
    IReportMatchMembershipCondition,
    ISecurityEncodable,
    ISecurityPolicyEncodable,
):
    """"""

    def __init__(self):
        """"""
    @overload
    def Check(self, evidence: Evidence) -> bool:
        """

        :param evidence:
        :return:
        """
    @overload
    def Check(self, evidence: Evidence, usedEvidence: object) -> Tuple[bool, object]:
        """

        :param evidence:
        :param usedEvidence:
        :return:
        """
    def Copy(self) -> IMembershipCondition:
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
    @overload
    def FromXml(self, e: SecurityElement) -> None:
        """

        :param e:
        """
    @overload
    def FromXml(self, e: SecurityElement, level: PolicyLevel) -> None:
        """

        :param e:
        :param level:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
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
    @overload
    def ToXml(self) -> SecurityElement:
        """

        :return:
        """
    @overload
    def ToXml(self, level: PolicyLevel) -> SecurityElement:
        """

        :param level:
        :return:
        """

class Hash(EvidenceBase, ISerializable):
    """"""

    def __init__(self, assembly: Assembly):
        """

        :param assembly:
        """
    @property
    def MD5(self) -> Array[int]:
        """

        :return:
        """
    @property
    def SHA1(self) -> Array[int]:
        """

        :return:
        """
    @property
    def SHA256(self) -> Array[int]:
        """

        :return:
        """
    def Clone(self) -> EvidenceBase:
        """

        :return:
        """
    @classmethod
    def CreateMD5(cls, md5: Array[int]) -> Hash:
        """

        :param md5:
        :return:
        """
    @classmethod
    def CreateSHA1(cls, sha1: Array[int]) -> Hash:
        """

        :param sha1:
        :return:
        """
    @classmethod
    def CreateSHA256(cls, sha256: Array[int]) -> Hash:
        """

        :param sha256:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GenerateHash(self, hashAlg: HashAlgorithm) -> Array[int]:
        """

        :param hashAlg:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

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

    def __init__(self, hashAlg: HashAlgorithm, value: Array[int]):
        """

        :param hashAlg:
        :param value:
        """
    @property
    def HashAlgorithm(self) -> HashAlgorithm:
        """

        :return:
        """
    @HashAlgorithm.setter
    def HashAlgorithm(self, value: HashAlgorithm) -> None: ...
    @property
    def HashValue(self) -> Array[int]:
        """

        :return:
        """
    @HashValue.setter
    def HashValue(self, value: Array[int]) -> None: ...
    @overload
    def Check(self, evidence: Evidence) -> bool:
        """

        :param evidence:
        :return:
        """
    @overload
    def Check(self, evidence: Evidence, usedEvidence: object) -> Tuple[bool, object]:
        """

        :param evidence:
        :param usedEvidence:
        :return:
        """
    def Copy(self) -> IMembershipCondition:
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
    @overload
    def FromXml(self, e: SecurityElement) -> None:
        """

        :param e:
        """
    @overload
    def FromXml(self, e: SecurityElement, level: PolicyLevel) -> None:
        """

        :param e:
        :param level:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def OnDeserialization(self, sender: object) -> None:
        """

        :param sender:
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
    @overload
    def ToXml(self) -> SecurityElement:
        """

        :return:
        """
    @overload
    def ToXml(self, level: PolicyLevel) -> SecurityElement:
        """

        :param level:
        :return:
        """

class IApplicationTrustManager(ISecurityEncodable):
    """"""

    def DetermineApplicationTrust(
        self, activationContext: ActivationContext, context: TrustManagerContext
    ) -> ApplicationTrust:
        """

        :param activationContext:
        :param context:
        :return:
        """
    def FromXml(self, e: SecurityElement) -> None:
        """

        :param e:
        """
    def ToXml(self) -> SecurityElement:
        """

        :return:
        """

class IConstantMembershipCondition:
    """"""

class IDelayEvaluatedEvidence:
    """"""

    @property
    def IsVerified(self) -> bool:
        """

        :return:
        """
    @property
    def WasUsed(self) -> bool:
        """

        :return:
        """
    def MarkUsed(self) -> None:
        """"""

class IIdentityPermissionFactory:
    """"""

    def CreateIdentityPermission(self, evidence: Evidence) -> IPermission:
        """

        :param evidence:
        :return:
        """

class ILegacyEvidenceAdapter:
    """"""

    @property
    def EvidenceObject(self) -> object:
        """

        :return:
        """
    @property
    def EvidenceType(self) -> Type:
        """

        :return:
        """

class IMembershipCondition(ISecurityEncodable, ISecurityPolicyEncodable):
    """"""

    def Check(self, evidence: Evidence) -> bool:
        """

        :param evidence:
        :return:
        """
    def Copy(self) -> IMembershipCondition:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def FromXml(self, e: SecurityElement) -> None:
        """

        :param e:
        """
    @overload
    def FromXml(self, e: SecurityElement, level: PolicyLevel) -> None:
        """

        :param e:
        :param level:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def ToXml(self) -> SecurityElement:
        """

        :return:
        """
    @overload
    def ToXml(self, level: PolicyLevel) -> SecurityElement:
        """

        :param level:
        :return:
        """

class IReportMatchMembershipCondition(
    IMembershipCondition, ISecurityEncodable, ISecurityPolicyEncodable
):
    """"""

    @overload
    def Check(self, evidence: Evidence) -> bool:
        """

        :param evidence:
        :return:
        """
    @overload
    def Check(self, evidence: Evidence, usedEvidence: object) -> Tuple[bool, object]:
        """

        :param evidence:
        :param usedEvidence:
        :return:
        """
    def Copy(self) -> IMembershipCondition:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def FromXml(self, e: SecurityElement) -> None:
        """

        :param e:
        """
    @overload
    def FromXml(self, e: SecurityElement, level: PolicyLevel) -> None:
        """

        :param e:
        :param level:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def ToXml(self) -> SecurityElement:
        """

        :return:
        """
    @overload
    def ToXml(self, level: PolicyLevel) -> SecurityElement:
        """

        :param level:
        :return:
        """

class IRuntimeEvidenceFactory:
    """"""

    @property
    def Target(self) -> IEvidenceFactory:
        """

        :return:
        """
    def GenerateEvidence(self, evidenceType: Type) -> EvidenceBase:
        """

        :param evidenceType:
        :return:
        """
    def GetFactorySuppliedEvidence(self) -> IEnumerable[EvidenceBase]:
        """

        :return:
        """

class IUnionSemanticCodeGroup:
    """"""

    def InternalResolve(self, evidence: Evidence) -> PolicyStatement:
        """

        :param evidence:
        :return:
        """

class LegacyEvidenceList(
    EvidenceBase, IEnumerable[EvidenceBase], IEnumerable, ILegacyEvidenceAdapter
):
    """"""

    def __init__(self):
        """"""
    @property
    def EvidenceObject(self) -> object:
        """

        :return:
        """
    @property
    def EvidenceType(self) -> Type:
        """

        :return:
        """
    def Add(self, evidence: EvidenceBase) -> None:
        """

        :param evidence:
        """
    def Clone(self) -> EvidenceBase:
        """

        :return:
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
    @overload
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[EvidenceBase]:
        """

        :return:
        """

class LegacyEvidenceWrapper(EvidenceBase, ILegacyEvidenceAdapter):
    """"""

    @property
    def EvidenceObject(self) -> object:
        """

        :return:
        """
    @property
    def EvidenceType(self) -> Type:
        """

        :return:
        """
    def Clone(self) -> EvidenceBase:
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

class NetCodeGroup(CodeGroup, IUnionSemanticCodeGroup):
    """"""

    AbsentOriginScheme: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    AnyOtherOriginScheme: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    def __init__(self, membershipCondition: IMembershipCondition):
        """

        :param membershipCondition:
        """
    @property
    def AttributeString(self) -> str:
        """

        :return:
        """
    @property
    def Children(self) -> IList:
        """

        :return:
        """
    @Children.setter
    def Children(self, value: IList) -> None: ...
    @property
    def Description(self) -> str:
        """

        :return:
        """
    @Description.setter
    def Description(self, value: str) -> None: ...
    @property
    def MembershipCondition(self) -> IMembershipCondition:
        """

        :return:
        """
    @MembershipCondition.setter
    def MembershipCondition(self, value: IMembershipCondition) -> None: ...
    @property
    def MergeLogic(self) -> str:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def PermissionSetName(self) -> str:
        """

        :return:
        """
    @property
    def PolicyStatement(self) -> PolicyStatement:
        """

        :return:
        """
    @PolicyStatement.setter
    def PolicyStatement(self, value: PolicyStatement) -> None: ...
    def AddChild(self, group: CodeGroup) -> None:
        """

        :param group:
        """
    def AddConnectAccess(self, originScheme: str, connectAccess: CodeConnectAccess) -> None:
        """

        :param originScheme:
        :param connectAccess:
        """
    def Copy(self) -> CodeGroup:
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
    def Equals(self, cg: CodeGroup, compareChildren: bool) -> bool:
        """

        :param cg:
        :param compareChildren:
        :return:
        """
    @overload
    def FromXml(self, e: SecurityElement) -> None:
        """

        :param e:
        """
    @overload
    def FromXml(self, e: SecurityElement, level: PolicyLevel) -> None:
        """

        :param e:
        :param level:
        """
    def GetConnectAccessRules(self) -> Array[DictionaryEntry]:
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
    def InternalResolve(self, evidence: Evidence) -> PolicyStatement:
        """

        :param evidence:
        :return:
        """
    def RemoveChild(self, group: CodeGroup) -> None:
        """

        :param group:
        """
    def ResetConnectAccess(self) -> None:
        """"""
    def Resolve(self, evidence: Evidence) -> PolicyStatement:
        """

        :param evidence:
        :return:
        """
    def ResolveMatchingCodeGroups(self, evidence: Evidence) -> CodeGroup:
        """

        :param evidence:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def ToXml(self) -> SecurityElement:
        """

        :return:
        """
    @overload
    def ToXml(self, level: PolicyLevel) -> SecurityElement:
        """

        :param level:
        :return:
        """

class PEFileEvidenceFactory(Object, IRuntimeEvidenceFactory):
    """"""

    @property
    def Target(self) -> IEvidenceFactory:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GenerateEvidence(self, evidenceType: Type) -> EvidenceBase:
        """

        :param evidenceType:
        :return:
        """
    def GetFactorySuppliedEvidence(self) -> IEnumerable[EvidenceBase]:
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

class PermissionRequestEvidence(EvidenceBase):
    """"""

    def __init__(self, request: PermissionSet, optional: PermissionSet, denied: PermissionSet):
        """

        :param request:
        :param optional:
        :param denied:
        """
    @property
    def DeniedPermissions(self) -> PermissionSet:
        """

        :return:
        """
    @property
    def OptionalPermissions(self) -> PermissionSet:
        """

        :return:
        """
    @property
    def RequestedPermissions(self) -> PermissionSet:
        """

        :return:
        """
    def Clone(self) -> EvidenceBase:
        """

        :return:
        """
    def Copy(self) -> PermissionRequestEvidence:
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

class PolicyException(SystemException, _Exception, ISerializable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, message: str):
        """

        :param message:
        """
    @overload
    def __init__(self, message: str, exception: Exception):
        """

        :param message:
        :param exception:
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

class PolicyLevel(Object):
    """"""

    @property
    def FullTrustAssemblies(self) -> IList:
        """

        :return:
        """
    @property
    def Label(self) -> str:
        """

        :return:
        """
    @property
    def NamedPermissionSets(self) -> IList:
        """

        :return:
        """
    @property
    def RootCodeGroup(self) -> CodeGroup:
        """

        :return:
        """
    @RootCodeGroup.setter
    def RootCodeGroup(self, value: CodeGroup) -> None: ...
    @property
    def StoreLocation(self) -> str:
        """

        :return:
        """
    @property
    def Type(self) -> PolicyLevelType:
        """

        :return:
        """
    @overload
    def AddFullTrustAssembly(self, sn: StrongName) -> None:
        """

        :param sn:
        """
    @overload
    def AddFullTrustAssembly(self, snMC: StrongNameMembershipCondition) -> None:
        """

        :param snMC:
        """
    def AddNamedPermissionSet(self, permSet: NamedPermissionSet) -> None:
        """

        :param permSet:
        """
    def ChangeNamedPermissionSet(self, name: str, pSet: PermissionSet) -> NamedPermissionSet:
        """

        :param name:
        :param pSet:
        :return:
        """
    @classmethod
    def CreateAppDomainLevel(cls) -> PolicyLevel:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def FromXml(self, e: SecurityElement) -> None:
        """

        :param e:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetNamedPermissionSet(self, name: str) -> NamedPermissionSet:
        """

        :param name:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def Recover(self) -> None:
        """"""
    @overload
    def RemoveFullTrustAssembly(self, sn: StrongName) -> None:
        """

        :param sn:
        """
    @overload
    def RemoveFullTrustAssembly(self, snMC: StrongNameMembershipCondition) -> None:
        """

        :param snMC:
        """
    @overload
    def RemoveNamedPermissionSet(self, permSet: NamedPermissionSet) -> NamedPermissionSet:
        """

        :param permSet:
        :return:
        """
    @overload
    def RemoveNamedPermissionSet(self, name: str) -> NamedPermissionSet:
        """

        :param name:
        :return:
        """
    def Reset(self) -> None:
        """"""
    def Resolve(self, evidence: Evidence) -> PolicyStatement:
        """

        :param evidence:
        :return:
        """
    def ResolveMatchingCodeGroups(self, evidence: Evidence) -> CodeGroup:
        """

        :param evidence:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def ToXml(self) -> SecurityElement:
        """

        :return:
        """

class PolicyStatement(Object, ISecurityEncodable, ISecurityPolicyEncodable):
    """"""

    @overload
    def __init__(self, permSet: PermissionSet):
        """

        :param permSet:
        """
    @overload
    def __init__(self, permSet: PermissionSet, attributes: PolicyStatementAttribute):
        """

        :param permSet:
        :param attributes:
        """
    @property
    def AttributeString(self) -> str:
        """

        :return:
        """
    @property
    def Attributes(self) -> PolicyStatementAttribute:
        """

        :return:
        """
    @Attributes.setter
    def Attributes(self, value: PolicyStatementAttribute) -> None: ...
    @property
    def PermissionSet(self) -> PermissionSet:
        """

        :return:
        """
    @PermissionSet.setter
    def PermissionSet(self, value: PermissionSet) -> None: ...
    def Copy(self) -> PolicyStatement:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def FromXml(self, e: SecurityElement) -> None:
        """

        :param e:
        """
    @overload
    def FromXml(self, e: SecurityElement, level: PolicyLevel) -> None:
        """

        :param e:
        :param level:
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
    @overload
    def ToXml(self) -> SecurityElement:
        """

        :return:
        """
    @overload
    def ToXml(self, level: PolicyLevel) -> SecurityElement:
        """

        :param level:
        :return:
        """

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

    def __init__(self, cert: X509Certificate):
        """

        :param cert:
        """
    @property
    def Certificate(self) -> X509Certificate:
        """

        :return:
        """
    def Clone(self) -> EvidenceBase:
        """

        :return:
        """
    def Copy(self) -> object:
        """

        :return:
        """
    def CreateIdentityPermission(self, evidence: Evidence) -> IPermission:
        """

        :param evidence:
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

class PublisherMembershipCondition(
    Object,
    IConstantMembershipCondition,
    IMembershipCondition,
    IReportMatchMembershipCondition,
    ISecurityEncodable,
    ISecurityPolicyEncodable,
):
    """"""

    def __init__(self, certificate: X509Certificate):
        """

        :param certificate:
        """
    @property
    def Certificate(self) -> X509Certificate:
        """

        :return:
        """
    @Certificate.setter
    def Certificate(self, value: X509Certificate) -> None: ...
    @overload
    def Check(self, evidence: Evidence) -> bool:
        """

        :param evidence:
        :return:
        """
    @overload
    def Check(self, evidence: Evidence, usedEvidence: object) -> Tuple[bool, object]:
        """

        :param evidence:
        :param usedEvidence:
        :return:
        """
    def Copy(self) -> IMembershipCondition:
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
    @overload
    def FromXml(self, e: SecurityElement) -> None:
        """

        :param e:
        """
    @overload
    def FromXml(self, e: SecurityElement, level: PolicyLevel) -> None:
        """

        :param e:
        :param level:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
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
    @overload
    def ToXml(self) -> SecurityElement:
        """

        :return:
        """
    @overload
    def ToXml(self, level: PolicyLevel) -> SecurityElement:
        """

        :param level:
        :return:
        """

class Site(EvidenceBase, IIdentityPermissionFactory):
    """"""

    def __init__(self, name: str):
        """

        :param name:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    def Clone(self) -> EvidenceBase:
        """

        :return:
        """
    def Copy(self) -> object:
        """

        :return:
        """
    @classmethod
    def CreateFromUrl(cls, url: str) -> Site:
        """

        :param url:
        :return:
        """
    def CreateIdentityPermission(self, evidence: Evidence) -> IPermission:
        """

        :param evidence:
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

class SiteMembershipCondition(
    Object,
    IConstantMembershipCondition,
    IMembershipCondition,
    IReportMatchMembershipCondition,
    ISecurityEncodable,
    ISecurityPolicyEncodable,
):
    """"""

    def __init__(self, site: str):
        """

        :param site:
        """
    @property
    def Site(self) -> str:
        """

        :return:
        """
    @Site.setter
    def Site(self, value: str) -> None: ...
    @overload
    def Check(self, evidence: Evidence) -> bool:
        """

        :param evidence:
        :return:
        """
    @overload
    def Check(self, evidence: Evidence, usedEvidence: object) -> Tuple[bool, object]:
        """

        :param evidence:
        :param usedEvidence:
        :return:
        """
    def Copy(self) -> IMembershipCondition:
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
    @overload
    def FromXml(self, e: SecurityElement) -> None:
        """

        :param e:
        """
    @overload
    def FromXml(self, e: SecurityElement, level: PolicyLevel) -> None:
        """

        :param e:
        :param level:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
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
    @overload
    def ToXml(self) -> SecurityElement:
        """

        :return:
        """
    @overload
    def ToXml(self, level: PolicyLevel) -> SecurityElement:
        """

        :param level:
        :return:
        """

class StrongName(EvidenceBase, IDelayEvaluatedEvidence, IIdentityPermissionFactory):
    """"""

    def __init__(self, blob: StrongNamePublicKeyBlob, name: str, version: Version):
        """

        :param blob:
        :param name:
        :param version:
        """
    @property
    def IsVerified(self) -> bool:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def PublicKey(self) -> StrongNamePublicKeyBlob:
        """

        :return:
        """
    @property
    def Version(self) -> Version:
        """

        :return:
        """
    @property
    def WasUsed(self) -> bool:
        """

        :return:
        """
    def Clone(self) -> EvidenceBase:
        """

        :return:
        """
    def Copy(self) -> object:
        """

        :return:
        """
    def CreateIdentityPermission(self, evidence: Evidence) -> IPermission:
        """

        :param evidence:
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
    def MarkUsed(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class StrongNameMembershipCondition(
    Object,
    IConstantMembershipCondition,
    IMembershipCondition,
    IReportMatchMembershipCondition,
    ISecurityEncodable,
    ISecurityPolicyEncodable,
):
    """"""

    def __init__(self, blob: StrongNamePublicKeyBlob, name: str, version: Version):
        """

        :param blob:
        :param name:
        :param version:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def PublicKey(self) -> StrongNamePublicKeyBlob:
        """

        :return:
        """
    @PublicKey.setter
    def PublicKey(self, value: StrongNamePublicKeyBlob) -> None: ...
    @property
    def Version(self) -> Version:
        """

        :return:
        """
    @Version.setter
    def Version(self, value: Version) -> None: ...
    @overload
    def Check(self, evidence: Evidence) -> bool:
        """

        :param evidence:
        :return:
        """
    @overload
    def Check(self, evidence: Evidence, usedEvidence: object) -> Tuple[bool, object]:
        """

        :param evidence:
        :param usedEvidence:
        :return:
        """
    def Copy(self) -> IMembershipCondition:
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
    @overload
    def FromXml(self, e: SecurityElement) -> None:
        """

        :param e:
        """
    @overload
    def FromXml(self, e: SecurityElement, level: PolicyLevel) -> None:
        """

        :param e:
        :param level:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
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
    @overload
    def ToXml(self) -> SecurityElement:
        """

        :return:
        """
    @overload
    def ToXml(self, level: PolicyLevel) -> SecurityElement:
        """

        :param level:
        :return:
        """

class TrustManagerContext(Object):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, uiContext: TrustManagerUIContext):
        """

        :param uiContext:
        """
    @property
    def IgnorePersistedDecision(self) -> bool:
        """

        :return:
        """
    @IgnorePersistedDecision.setter
    def IgnorePersistedDecision(self, value: bool) -> None: ...
    @property
    def KeepAlive(self) -> bool:
        """

        :return:
        """
    @KeepAlive.setter
    def KeepAlive(self, value: bool) -> None: ...
    @property
    def NoPrompt(self) -> bool:
        """

        :return:
        """
    @NoPrompt.setter
    def NoPrompt(self, value: bool) -> None: ...
    @property
    def Persist(self) -> bool:
        """

        :return:
        """
    @Persist.setter
    def Persist(self, value: bool) -> None: ...
    @property
    def PreviousApplicationIdentity(self) -> ApplicationIdentity:
        """

        :return:
        """
    @PreviousApplicationIdentity.setter
    def PreviousApplicationIdentity(self, value: ApplicationIdentity) -> None: ...
    @property
    def UIContext(self) -> TrustManagerUIContext:
        """

        :return:
        """
    @UIContext.setter
    def UIContext(self, value: TrustManagerUIContext) -> None: ...
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

    def __init__(self, membershipCondition: IMembershipCondition, policy: PolicyStatement):
        """

        :param membershipCondition:
        :param policy:
        """
    @property
    def AttributeString(self) -> str:
        """

        :return:
        """
    @property
    def Children(self) -> IList:
        """

        :return:
        """
    @Children.setter
    def Children(self, value: IList) -> None: ...
    @property
    def Description(self) -> str:
        """

        :return:
        """
    @Description.setter
    def Description(self, value: str) -> None: ...
    @property
    def MembershipCondition(self) -> IMembershipCondition:
        """

        :return:
        """
    @MembershipCondition.setter
    def MembershipCondition(self, value: IMembershipCondition) -> None: ...
    @property
    def MergeLogic(self) -> str:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def PermissionSetName(self) -> str:
        """

        :return:
        """
    @property
    def PolicyStatement(self) -> PolicyStatement:
        """

        :return:
        """
    @PolicyStatement.setter
    def PolicyStatement(self, value: PolicyStatement) -> None: ...
    def AddChild(self, group: CodeGroup) -> None:
        """

        :param group:
        """
    def Copy(self) -> CodeGroup:
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
    def Equals(self, cg: CodeGroup, compareChildren: bool) -> bool:
        """

        :param cg:
        :param compareChildren:
        :return:
        """
    @overload
    def FromXml(self, e: SecurityElement) -> None:
        """

        :param e:
        """
    @overload
    def FromXml(self, e: SecurityElement, level: PolicyLevel) -> None:
        """

        :param e:
        :param level:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def InternalResolve(self, evidence: Evidence) -> PolicyStatement:
        """

        :param evidence:
        :return:
        """
    def RemoveChild(self, group: CodeGroup) -> None:
        """

        :param group:
        """
    def Resolve(self, evidence: Evidence) -> PolicyStatement:
        """

        :param evidence:
        :return:
        """
    def ResolveMatchingCodeGroups(self, evidence: Evidence) -> CodeGroup:
        """

        :param evidence:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def ToXml(self) -> SecurityElement:
        """

        :return:
        """
    @overload
    def ToXml(self, level: PolicyLevel) -> SecurityElement:
        """

        :param level:
        :return:
        """

class Url(EvidenceBase, IIdentityPermissionFactory):
    """"""

    def __init__(self, name: str):
        """

        :param name:
        """
    @property
    def Value(self) -> str:
        """

        :return:
        """
    def Clone(self) -> EvidenceBase:
        """

        :return:
        """
    def Copy(self) -> object:
        """

        :return:
        """
    def CreateIdentityPermission(self, evidence: Evidence) -> IPermission:
        """

        :param evidence:
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

class UrlMembershipCondition(
    Object,
    IConstantMembershipCondition,
    IMembershipCondition,
    IReportMatchMembershipCondition,
    ISecurityEncodable,
    ISecurityPolicyEncodable,
):
    """"""

    def __init__(self, url: str):
        """

        :param url:
        """
    @property
    def Url(self) -> str:
        """

        :return:
        """
    @Url.setter
    def Url(self, value: str) -> None: ...
    @overload
    def Check(self, evidence: Evidence) -> bool:
        """

        :param evidence:
        :return:
        """
    @overload
    def Check(self, evidence: Evidence, usedEvidence: object) -> Tuple[bool, object]:
        """

        :param evidence:
        :param usedEvidence:
        :return:
        """
    def Copy(self) -> IMembershipCondition:
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
    @overload
    def FromXml(self, e: SecurityElement) -> None:
        """

        :param e:
        """
    @overload
    def FromXml(self, e: SecurityElement, level: PolicyLevel) -> None:
        """

        :param e:
        :param level:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
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
    @overload
    def ToXml(self) -> SecurityElement:
        """

        :return:
        """
    @overload
    def ToXml(self, level: PolicyLevel) -> SecurityElement:
        """

        :param level:
        :return:
        """

class Zone(EvidenceBase, IIdentityPermissionFactory):
    """"""

    def __init__(self, zone: SecurityZone):
        """

        :param zone:
        """
    @property
    def SecurityZone(self) -> SecurityZone:
        """

        :return:
        """
    def Clone(self) -> EvidenceBase:
        """

        :return:
        """
    def Copy(self) -> object:
        """

        :return:
        """
    @classmethod
    def CreateFromUrl(cls, url: str) -> Zone:
        """

        :param url:
        :return:
        """
    def CreateIdentityPermission(self, evidence: Evidence) -> IPermission:
        """

        :param evidence:
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

class ZoneMembershipCondition(
    Object,
    IConstantMembershipCondition,
    IMembershipCondition,
    IReportMatchMembershipCondition,
    ISecurityEncodable,
    ISecurityPolicyEncodable,
):
    """"""

    def __init__(self, zone: SecurityZone):
        """

        :param zone:
        """
    @property
    def SecurityZone(self) -> SecurityZone:
        """

        :return:
        """
    @SecurityZone.setter
    def SecurityZone(self, value: SecurityZone) -> None: ...
    @overload
    def Check(self, evidence: Evidence) -> bool:
        """

        :param evidence:
        :return:
        """
    @overload
    def Check(self, evidence: Evidence, usedEvidence: object) -> Tuple[bool, object]:
        """

        :param evidence:
        :param usedEvidence:
        :return:
        """
    def Copy(self) -> IMembershipCondition:
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
    @overload
    def FromXml(self, e: SecurityElement) -> None:
        """

        :param e:
        """
    @overload
    def FromXml(self, e: SecurityElement, level: PolicyLevel) -> None:
        """

        :param e:
        :param level:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
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
    @overload
    def ToXml(self) -> SecurityElement:
        """

        :return:
        """
    @overload
    def ToXml(self, level: PolicyLevel) -> SecurityElement:
        """

        :param level:
        :return:
        """
