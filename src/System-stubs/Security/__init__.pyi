from abc import ABC
from collections.abc import Iterator
from typing import TypeVar
from typing import overload

from System import Array
from System import Attribute
from System import Char
from System import Enum
from System import Exception
from System import Guid
from System import IDisposable
from System import IntPtr
from System import Object
from System import SystemException
from System import Type
from System import ValueType
from System.Collections import ArrayList
from System.Collections import Hashtable
from System.Collections import ICollection
from System.Collections import IDictionary
from System.Collections import IEnumerable
from System.Collections import IEnumerator
from System.Collections import IEqualityComparer
from System.Reflection import Assembly
from System.Reflection import AssemblyName
from System.Reflection import MethodBase
from System.Reflection import MethodInfo
from System.Reflection.Emit import DynamicResolver
from System.Runtime.InteropServices import SafeBuffer
from System.Runtime.InteropServices import T
from System.Runtime.InteropServices import _Attribute
from System.Runtime.InteropServices import _Exception
from System.Runtime.Serialization import IDeserializationCallback
from System.Runtime.Serialization import ISerializable
from System.Runtime.Serialization import SerializationInfo
from System.Runtime.Serialization import StreamingContext
from System.Security.Permissions import HostProtectionResource
from System.Security.Permissions import PermissionState
from System.Security.Permissions import SecurityAction
from System.Security.Policy import ApplicationTrust
from System.Security.Policy import Evidence
from System.Security.Policy import EvidenceBase
from System.Security.Policy import PolicyLevel
from System.Security.Policy import TrustManagerContext
from System.Threading import AsyncFlowControl
from System.Threading import ContextCallback

T = TypeVar("T")

class AllowPartiallyTrustedCallersAttribute(Attribute, _Attribute):
    """"""

    def __init__(self):
        """"""
    @property
    def PartialTrustVisibilityLevel(self) -> PartialTrustVisibilityLevel:
        """:return:"""
    @PartialTrustVisibilityLevel.setter
    def PartialTrustVisibilityLevel(self, value: PartialTrustVisibilityLevel) -> None: ...
    @property
    def TypeId(self) -> object:
        """:return:"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """:param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """:return:"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """:param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> tuple[None, int]:
        """:param pcTInfo:"""
    def Invoke(
        self,
        dispIdMember: int,
        riid: Guid,
        lcid: int,
        wFlags: int,
        pDispParams: IntPtr,
        pVarResult: IntPtr,
        pExcepInfo: IntPtr,
        puArgErr: IntPtr,
    ) -> None:
        """:param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """:return:"""
    def Match(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def ToString(self) -> str:
        """:return:"""

class BuiltInPermissionSets(ABC, Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class CodeAccessPermission(ABC, Object, IPermission, ISecurityEncodable, IStackWalk):
    """"""

    def Assert(self) -> None:
        """"""
    def Copy(self) -> IPermission:
        """:return:"""
    @overload
    def Demand(self) -> None:
        """"""
    @overload
    def Demand(self) -> None:
        """"""
    def Deny(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def FromXml(self, e: SecurityElement) -> None:
        """:param e:"""
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def Intersect(self, target: IPermission) -> IPermission:
        """:param target:
        :return:
        """
    def IsSubsetOf(self, target: IPermission) -> bool:
        """:param target:
        :return:
        """
    def PermitOnly(self) -> None:
        """"""
    @classmethod
    def RevertAll(cls) -> None:
        """"""
    @classmethod
    def RevertAssert(cls) -> None:
        """"""
    @classmethod
    def RevertDeny(cls) -> None:
        """"""
    @classmethod
    def RevertPermitOnly(cls) -> None:
        """"""
    def ToString(self) -> str:
        """:return:"""
    def ToXml(self) -> SecurityElement:
        """:return:"""
    def Union(self, target: IPermission) -> IPermission:
        """:param target:
        :return:
        """

class CodeAccessSecurityEngine(ABC, Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class DynamicSecurityMethodAttribute(Attribute, _Attribute):
    """"""

    def __init__(self):
        """"""
    @property
    def TypeId(self) -> object:
        """:return:"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """:param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """:return:"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """:param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> tuple[None, int]:
        """:param pcTInfo:"""
    def Invoke(
        self,
        dispIdMember: int,
        riid: Guid,
        lcid: int,
        wFlags: int,
        pDispParams: IntPtr,
        pVarResult: IntPtr,
        pExcepInfo: IntPtr,
        puArgErr: IntPtr,
    ) -> None:
        """:param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """:return:"""
    def Match(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def ToString(self) -> str:
        """:return:"""

class FrameSecurityDescriptor(Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class FrameSecurityDescriptorWithResolver(FrameSecurityDescriptor):
    """"""

    def __init__(self):
        """"""
    @property
    def Resolver(self) -> DynamicResolver:
        """:return:"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class HostProtectionException(SystemException, _Exception, ISerializable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, message: str):
        """:param message:"""
    @overload
    def __init__(self, message: str, e: Exception):
        """:param message:
        :param e:
        """
    @overload
    def __init__(
        self,
        message: str,
        protectedResources: HostProtectionResource,
        demandedResources: HostProtectionResource,
    ):
        """:param message:
        :param protectedResources:
        :param demandedResources:
        """
    @property
    def Data(self) -> IDictionary:
        """:return:"""
    @property
    def DemandedResources(self) -> HostProtectionResource:
        """:return:"""
    @property
    def HResult(self) -> int:
        """:return:"""
    @property
    def HelpLink(self) -> str:
        """:return:"""
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """:return:"""
    @property
    def Message(self) -> str:
        """:return:"""
    @property
    def ProtectedResources(self) -> HostProtectionResource:
        """:return:"""
    @property
    def Source(self) -> str:
        """:return:"""
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """:return:"""
    @property
    def TargetSite(self) -> MethodBase:
        """:return:"""
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetBaseException(self) -> Exception:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""

class HostSecurityManager(Object):
    """"""

    def __init__(self):
        """"""
    @property
    def DomainPolicy(self) -> PolicyLevel:
        """:return:"""
    @property
    def Flags(self) -> HostSecurityManagerOptions:
        """:return:"""
    def DetermineApplicationTrust(
        self,
        applicationEvidence: Evidence,
        activatorEvidence: Evidence,
        context: TrustManagerContext,
    ) -> ApplicationTrust:
        """:param applicationEvidence:
        :param activatorEvidence:
        :param context:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GenerateAppDomainEvidence(self, evidenceType: Type) -> EvidenceBase:
        """:param evidenceType:
        :return:
        """
    def GenerateAssemblyEvidence(self, evidenceType: Type, assembly: Assembly) -> EvidenceBase:
        """:param evidenceType:
        :param assembly:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetHostSuppliedAppDomainEvidenceTypes(self) -> Array[Type]:
        """:return:"""
    def GetHostSuppliedAssemblyEvidenceTypes(self, assembly: Assembly) -> Array[Type]:
        """:param assembly:
        :return:
        """
    def GetType(self) -> Type:
        """:return:"""
    def ProvideAppDomainEvidence(self, inputEvidence: Evidence) -> Evidence:
        """:param inputEvidence:
        :return:
        """
    def ProvideAssemblyEvidence(
        self, loadedAssembly: Assembly, inputEvidence: Evidence
    ) -> Evidence:
        """:param loadedAssembly:
        :param inputEvidence:
        :return:
        """
    def ResolvePolicy(self, evidence: Evidence) -> PermissionSet:
        """:param evidence:
        :return:
        """
    def ToString(self) -> str:
        """:return:"""

class HostSecurityManagerOptions(Enum):
    """"""

    _None: HostSecurityManagerOptions = ...
    """"""
    HostAppDomainEvidence: HostSecurityManagerOptions = ...
    """"""
    HostPolicyLevel: HostSecurityManagerOptions = ...
    """"""
    HostAssemblyEvidence: HostSecurityManagerOptions = ...
    """"""
    HostDetermineApplicationTrust: HostSecurityManagerOptions = ...
    """"""
    HostResolvePolicy: HostSecurityManagerOptions = ...
    """"""
    AllFlags: HostSecurityManagerOptions = ...
    """"""

class IEvidenceFactory:
    """"""

    @property
    def Evidence(self) -> Evidence:
        """:return:"""

class IPermission(ISecurityEncodable):
    """"""

    def Copy(self) -> IPermission:
        """:return:"""
    def Demand(self) -> None:
        """"""
    def FromXml(self, e: SecurityElement) -> None:
        """:param e:"""
    def Intersect(self, target: IPermission) -> IPermission:
        """:param target:
        :return:
        """
    def IsSubsetOf(self, target: IPermission) -> bool:
        """:param target:
        :return:
        """
    def ToXml(self) -> SecurityElement:
        """:return:"""
    def Union(self, target: IPermission) -> IPermission:
        """:param target:
        :return:
        """

class ISecurityElementFactory:
    """"""

    def Attribute(self, attributeName: str) -> str:
        """:param attributeName:
        :return:
        """
    def Copy(self) -> object:
        """:return:"""
    def CreateSecurityElement(self) -> SecurityElement:
        """:return:"""
    def GetTag(self) -> str:
        """:return:"""

class ISecurityEncodable:
    """"""

    def FromXml(self, e: SecurityElement) -> None:
        """:param e:"""
    def ToXml(self) -> SecurityElement:
        """:return:"""

class ISecurityPolicyEncodable:
    """"""

    def FromXml(self, e: SecurityElement, level: PolicyLevel) -> None:
        """:param e:
        :param level:
        """
    def ToXml(self, level: PolicyLevel) -> SecurityElement:
        """:param level:
        :return:
        """

class IStackWalk:
    """"""

    def Assert(self) -> None:
        """"""
    def Demand(self) -> None:
        """"""
    def Deny(self) -> None:
        """"""
    def PermitOnly(self) -> None:
        """"""

class ManifestKinds(Enum):
    """"""

    _None: ManifestKinds = ...
    """"""
    Deployment: ManifestKinds = ...
    """"""
    Application: ManifestKinds = ...
    """"""
    ApplicationAndDeployment: ManifestKinds = ...
    """"""

class NamedPermissionSet(
    PermissionSet,
    ICollection,
    IEnumerable,
    IDeserializationCallback,
    ISecurityEncodable,
    IStackWalk,
):
    """"""

    @overload
    def __init__(self, permSet: NamedPermissionSet):
        """:param permSet:"""
    @overload
    def __init__(self, name: str):
        """:param name:"""
    @overload
    def __init__(self, name: str, state: PermissionState):
        """:param name:
        :param state:
        """
    @overload
    def __init__(self, name: str, permSet: PermissionSet):
        """:param name:
        :param permSet:
        """
    @property
    def Count(self) -> int:
        """:return:"""
    @property
    def Description(self) -> str:
        """:return:"""
    @Description.setter
    def Description(self, value: str) -> None: ...
    @property
    def IsReadOnly(self) -> bool:
        """:return:"""
    @property
    def IsSynchronized(self) -> bool:
        """:return:"""
    @property
    def Name(self) -> str:
        """:return:"""
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def SyncRoot(self) -> object:
        """:return:"""
    def AddPermission(self, perm: IPermission) -> IPermission:
        """:param perm:
        :return:
        """
    def Assert(self) -> None:
        """"""
    def ContainsNonCodeAccessPermissions(self) -> bool:
        """:return:"""
    @overload
    def Copy(self) -> PermissionSet:
        """:return:"""
    @overload
    def Copy(self, name: str) -> NamedPermissionSet:
        """:param name:
        :return:
        """
    def CopyTo(self, array: Array, index: int) -> None:
        """:param array:
        :param index:
        """
    def Demand(self) -> None:
        """"""
    def Deny(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def FromXml(self, e: SecurityElement) -> None:
        """:param e:"""
    def GetEnumerator(self) -> IEnumerator:
        """:return:"""
    def GetHashCode(self) -> int:
        """:return:"""
    def GetPermission(self, permClass: Type) -> IPermission:
        """:param permClass:
        :return:
        """
    def GetType(self) -> Type:
        """:return:"""
    def Intersect(self, other: PermissionSet) -> PermissionSet:
        """:param other:
        :return:
        """
    def IsEmpty(self) -> bool:
        """:return:"""
    def IsSubsetOf(self, target: PermissionSet) -> bool:
        """:param target:
        :return:
        """
    def IsUnrestricted(self) -> bool:
        """:return:"""
    def OnDeserialization(self, sender: object) -> None:
        """:param sender:"""
    def PermitOnly(self) -> None:
        """"""
    def RemovePermission(self, permClass: Type) -> IPermission:
        """:param permClass:
        :return:
        """
    def SetPermission(self, perm: IPermission) -> IPermission:
        """:param perm:
        :return:
        """
    def ToString(self) -> str:
        """:return:"""
    def ToXml(self) -> SecurityElement:
        """:return:"""
    def Union(self, other: PermissionSet) -> PermissionSet:
        """:param other:
        :return:
        """
    def __contains__(self, value: object) -> bool:
        """:param value:
        :return:
        """
    def __iter__(self) -> Iterator[object]:
        """:return:"""
    def __len__(self) -> int:
        """:return:"""

class PartialTrustVisibilityLevel(Enum):
    """"""

    VisibleToAllHosts: PartialTrustVisibilityLevel = ...
    """"""
    NotVisibleByDefault: PartialTrustVisibilityLevel = ...
    """"""

class PermissionListSet(Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class PermissionSet(
    Object,
    ICollection,
    IEnumerable,
    IDeserializationCallback,
    ISecurityEncodable,
    IStackWalk,
):
    """"""

    @overload
    def __init__(self, state: PermissionState):
        """:param state:"""
    @overload
    def __init__(self, permSet: PermissionSet):
        """:param permSet:"""
    @property
    def Count(self) -> int:
        """:return:"""
    @property
    def IsReadOnly(self) -> bool:
        """:return:"""
    @property
    def IsSynchronized(self) -> bool:
        """:return:"""
    @property
    def SyncRoot(self) -> object:
        """:return:"""
    def AddPermission(self, perm: IPermission) -> IPermission:
        """:param perm:
        :return:
        """
    def Assert(self) -> None:
        """"""
    def ContainsNonCodeAccessPermissions(self) -> bool:
        """:return:"""
    @classmethod
    def ConvertPermissionSet(cls, inFormat: str, inData: Array[int], outFormat: str) -> Array[int]:
        """:param inFormat:
        :param inData:
        :param outFormat:
        :return:
        """
    def Copy(self) -> PermissionSet:
        """:return:"""
    def CopyTo(self, array: Array, index: int) -> None:
        """:param array:
        :param index:
        """
    def Demand(self) -> None:
        """"""
    def Deny(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def FromXml(self, e: SecurityElement) -> None:
        """:param e:"""
    def GetEnumerator(self) -> IEnumerator:
        """:return:"""
    def GetHashCode(self) -> int:
        """:return:"""
    def GetPermission(self, permClass: Type) -> IPermission:
        """:param permClass:
        :return:
        """
    def GetType(self) -> Type:
        """:return:"""
    def Intersect(self, other: PermissionSet) -> PermissionSet:
        """:param other:
        :return:
        """
    def IsEmpty(self) -> bool:
        """:return:"""
    def IsSubsetOf(self, target: PermissionSet) -> bool:
        """:param target:
        :return:
        """
    def IsUnrestricted(self) -> bool:
        """:return:"""
    def OnDeserialization(self, sender: object) -> None:
        """:param sender:"""
    def PermitOnly(self) -> None:
        """"""
    def RemovePermission(self, permClass: Type) -> IPermission:
        """:param permClass:
        :return:
        """
    @classmethod
    def RevertAssert(cls) -> None:
        """"""
    def SetPermission(self, perm: IPermission) -> IPermission:
        """:param perm:
        :return:
        """
    def ToString(self) -> str:
        """:return:"""
    def ToXml(self) -> SecurityElement:
        """:return:"""
    def Union(self, other: PermissionSet) -> PermissionSet:
        """:param other:
        :return:
        """
    def __contains__(self, value: object) -> bool:
        """:param value:
        :return:
        """
    def __iter__(self) -> Iterator[object]:
        """:return:"""
    def __len__(self) -> int:
        """:return:"""

class PermissionSetEnumerator(Object, IEnumerator):
    """"""

    @property
    def Current(self) -> object:
        """:return:"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def MoveNext(self) -> bool:
        """:return:"""
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """:return:"""

class PermissionSetEnumeratorInternal(ValueType):
    """"""

    @property
    def Current(self) -> object:
        """:return:"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetCurrentIndex(self) -> int:
        """:return:"""
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def MoveNext(self) -> bool:
        """:return:"""
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """:return:"""

class PermissionSetTriple(Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class PermissionToken(Object, ISecurityEncodable):
    """"""

    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @classmethod
    def FindToken(cls, cls: Type) -> PermissionToken:
        """:param cls:
        :return:
        """
    @classmethod
    def FindTokenByIndex(cls, i: int) -> PermissionToken:
        """:param i:
        :return:
        """
    def FromXml(self, e: SecurityElement) -> None:
        """:param e:"""
    def GetHashCode(self) -> int:
        """:return:"""
    @classmethod
    @overload
    def GetToken(cls, perm: IPermission) -> PermissionToken:
        """:param perm:
        :return:
        """
    @classmethod
    @overload
    def GetToken(cls, typeStr: str) -> PermissionToken:
        """:param typeStr:
        :return:
        """
    @classmethod
    @overload
    def GetToken(cls, cls: Type) -> PermissionToken:
        """:param cls:
        :return:
        """
    @classmethod
    @overload
    def GetToken(cls, typeStr: str, bCreateMscorlib: bool) -> PermissionToken:
        """:param typeStr:
        :param bCreateMscorlib:
        :return:
        """
    def GetType(self) -> Type:
        """:return:"""
    @classmethod
    def IsTokenProperlyAssigned(cls, perm: IPermission, token: PermissionToken) -> bool:
        """:param perm:
        :param token:
        :return:
        """
    def ToString(self) -> str:
        """:return:"""
    def ToXml(self) -> SecurityElement:
        """:return:"""

class PermissionTokenFactory(Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class PermissionTokenKeyComparer(Object, IEqualityComparer):
    """"""

    def __init__(self):
        """"""
    def Compare(self, a: object, b: object) -> int:
        """:param a:
        :param b:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, x: object, y: object) -> bool:
        """:param x:
        :param y:
        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self, obj: object) -> int:
        """:param obj:
        :return:
        """
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class PermissionTokenType(Enum):
    """"""

    Normal: PermissionTokenType = ...
    """"""
    IUnrestricted: PermissionTokenType = ...
    """"""
    DontKnow: PermissionTokenType = ...
    """"""
    BuiltIn: PermissionTokenType = ...
    """"""

class PermissionType(Enum):
    """"""

    SecurityUnmngdCodeAccess: PermissionType = ...
    """"""
    SecuritySkipVerification: PermissionType = ...
    """"""
    ReflectionTypeInfo: PermissionType = ...
    """"""
    SecurityAssert: PermissionType = ...
    """"""
    ReflectionMemberAccess: PermissionType = ...
    """"""
    SecuritySerialization: PermissionType = ...
    """"""
    ReflectionRestrictedMemberAccess: PermissionType = ...
    """"""
    FullTrust: PermissionType = ...
    """"""
    SecurityBindingRedirects: PermissionType = ...
    """"""
    UIPermission: PermissionType = ...
    """"""
    EnvironmentPermission: PermissionType = ...
    """"""
    FileDialogPermission: PermissionType = ...
    """"""
    FileIOPermission: PermissionType = ...
    """"""
    ReflectionPermission: PermissionType = ...
    """"""
    SecurityPermission: PermissionType = ...
    """"""
    SecurityControlEvidence: PermissionType = ...
    """"""
    SecurityControlPrincipal: PermissionType = ...
    """"""

class PolicyLevelType(Enum):
    """"""

    User: PolicyLevelType = ...
    """"""
    Machine: PolicyLevelType = ...
    """"""
    Enterprise: PolicyLevelType = ...
    """"""
    AppDomain: PolicyLevelType = ...
    """"""

class PolicyManager(Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class ReadOnlyPermissionSet(
    PermissionSet,
    ICollection,
    IEnumerable,
    IDeserializationCallback,
    ISecurityEncodable,
    IStackWalk,
):
    """"""

    def __init__(self, permissionSetXml: SecurityElement):
        """:param permissionSetXml:"""
    @property
    def Count(self) -> int:
        """:return:"""
    @property
    def IsReadOnly(self) -> bool:
        """:return:"""
    @property
    def IsSynchronized(self) -> bool:
        """:return:"""
    @property
    def SyncRoot(self) -> object:
        """:return:"""
    def AddPermission(self, perm: IPermission) -> IPermission:
        """:param perm:
        :return:
        """
    def Assert(self) -> None:
        """"""
    def ContainsNonCodeAccessPermissions(self) -> bool:
        """:return:"""
    def Copy(self) -> PermissionSet:
        """:return:"""
    def CopyTo(self, array: Array, index: int) -> None:
        """:param array:
        :param index:
        """
    def Demand(self) -> None:
        """"""
    def Deny(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def FromXml(self, e: SecurityElement) -> None:
        """:param e:"""
    def GetEnumerator(self) -> IEnumerator:
        """:return:"""
    def GetHashCode(self) -> int:
        """:return:"""
    def GetPermission(self, permClass: Type) -> IPermission:
        """:param permClass:
        :return:
        """
    def GetType(self) -> Type:
        """:return:"""
    def Intersect(self, other: PermissionSet) -> PermissionSet:
        """:param other:
        :return:
        """
    def IsEmpty(self) -> bool:
        """:return:"""
    def IsSubsetOf(self, target: PermissionSet) -> bool:
        """:param target:
        :return:
        """
    def IsUnrestricted(self) -> bool:
        """:return:"""
    def OnDeserialization(self, sender: object) -> None:
        """:param sender:"""
    def PermitOnly(self) -> None:
        """"""
    def RemovePermission(self, permClass: Type) -> IPermission:
        """:param permClass:
        :return:
        """
    def SetPermission(self, perm: IPermission) -> IPermission:
        """:param perm:
        :return:
        """
    def ToString(self) -> str:
        """:return:"""
    def ToXml(self) -> SecurityElement:
        """:return:"""
    def Union(self, other: PermissionSet) -> PermissionSet:
        """:param other:
        :return:
        """
    def __contains__(self, value: object) -> bool:
        """:param value:
        :return:
        """
    def __iter__(self) -> Iterator[object]:
        """:return:"""
    def __len__(self) -> int:
        """:return:"""

class ReadOnlyPermissionSetEnumerator(Object, IEnumerator):
    """"""

    @property
    def Current(self) -> object:
        """:return:"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def MoveNext(self) -> bool:
        """:return:"""
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """:return:"""

class SafeBSTRHandle(SafeBuffer, IDisposable):
    """"""

    @property
    def ByteLength(self) -> int:
        """:return:"""
    @property
    def IsClosed(self) -> bool:
        """:return:"""
    @property
    def IsInvalid(self) -> bool:
        """:return:"""
    def AcquirePointer(self, pointer: int) -> None:
        """:param pointer:"""
    def Close(self) -> None:
        """"""
    def DangerousAddRef(self, success: bool) -> None:
        """:param success:"""
    def DangerousGetHandle(self) -> IntPtr:
        """:return:"""
    def DangerousRelease(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def Initialize(self, numElements: int) -> None:
        """:param numElements:"""
    @overload
    def Initialize(self, numBytes: int) -> None:
        """:param numBytes:"""
    @overload
    def Initialize(self, numElements: int, sizeOfEachElement: int) -> None:
        """:param numElements:
        :param sizeOfEachElement:
        """
    def Read(self, byteOffset: int) -> T:
        """:param byteOffset:
        :return:
        """
    def ReadArray(self, byteOffset: int, array: Array[T], index: int, count: int) -> None:
        """:param byteOffset:
        :param array:
        :param index:
        :param count:
        """
    def ReleasePointer(self) -> None:
        """"""
    def SetHandleAsInvalid(self) -> None:
        """"""
    def ToString(self) -> str:
        """:return:"""
    def Write(self, byteOffset: int, value: T) -> None:
        """:param byteOffset:
        :param value:
        """
    def WriteArray(self, byteOffset: int, array: Array[T], index: int, count: int) -> None:
        """:param byteOffset:
        :param array:
        :param index:
        :param count:
        """

class SecureString(Object, IDisposable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, value: Char, length: int):
        """:param value:
        :param length:
        """
    @property
    def Length(self) -> int:
        """:return:"""
    def AppendChar(self, c: Char) -> None:
        """:param c:"""
    def Clear(self) -> None:
        """"""
    def Copy(self) -> SecureString:
        """:return:"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def InsertAt(self, index: int, c: Char) -> None:
        """:param index:
        :param c:
        """
    def IsReadOnly(self) -> bool:
        """:return:"""
    def MakeReadOnly(self) -> None:
        """"""
    def RemoveAt(self, index: int) -> None:
        """:param index:"""
    def SetAt(self, index: int, c: Char) -> None:
        """:param index:
        :param c:
        """
    def ToString(self) -> str:
        """:return:"""

class SecureStringMarshal(ABC, Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    @classmethod
    def SecureStringToCoTaskMemAnsi(cls, s: SecureString) -> IntPtr:
        """:param s:
        :return:
        """
    @classmethod
    def SecureStringToCoTaskMemUnicode(cls, s: SecureString) -> IntPtr:
        """:param s:
        :return:
        """
    @classmethod
    def SecureStringToGlobalAllocAnsi(cls, s: SecureString) -> IntPtr:
        """:param s:
        :return:
        """
    @classmethod
    def SecureStringToGlobalAllocUnicode(cls, s: SecureString) -> IntPtr:
        """:param s:
        :return:
        """
    def ToString(self) -> str:
        """:return:"""

class SecurityContext(Object, IDisposable):
    """"""

    @classmethod
    def Capture(cls) -> SecurityContext:
        """:return:"""
    def CreateCopy(self) -> SecurityContext:
        """:return:"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    @classmethod
    def IsFlowSuppressed(cls) -> bool:
        """:return:"""
    @classmethod
    def IsWindowsIdentityFlowSuppressed(cls) -> bool:
        """:return:"""
    @classmethod
    def RestoreFlow(cls) -> None:
        """"""
    @classmethod
    def Run(
        cls, securityContext: SecurityContext, callback: ContextCallback, state: object
    ) -> None:
        """:param securityContext:
        :param callback:
        :param state:
        """
    @classmethod
    def SuppressFlow(cls) -> AsyncFlowControl:
        """:return:"""
    @classmethod
    def SuppressFlowWindowsIdentity(cls) -> AsyncFlowControl:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class SecurityContextDisableFlow(Enum):
    """"""

    Nothing: SecurityContextDisableFlow = ...
    """"""
    WI: SecurityContextDisableFlow = ...
    """"""
    All: SecurityContextDisableFlow = ...
    """"""

class SecurityContextSource(Enum):
    """"""

    CurrentAppDomain: SecurityContextSource = ...
    """"""
    CurrentAssembly: SecurityContextSource = ...
    """"""

class SecurityContextSwitcher(ValueType, IDisposable):
    """"""

    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""
    def Undo(self) -> None:
        """"""

class SecurityCriticalAttribute(Attribute, _Attribute):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, scope: SecurityCriticalScope):
        """:param scope:"""
    @property
    def Scope(self) -> SecurityCriticalScope:
        """:return:"""
    @property
    def TypeId(self) -> object:
        """:return:"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """:param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """:return:"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """:param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> tuple[None, int]:
        """:param pcTInfo:"""
    def Invoke(
        self,
        dispIdMember: int,
        riid: Guid,
        lcid: int,
        wFlags: int,
        pDispParams: IntPtr,
        pVarResult: IntPtr,
        pExcepInfo: IntPtr,
        puArgErr: IntPtr,
    ) -> None:
        """:param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """:return:"""
    def Match(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def ToString(self) -> str:
        """:return:"""

class SecurityCriticalScope(Enum):
    """"""

    Explicit: SecurityCriticalScope = ...
    """"""
    Everything: SecurityCriticalScope = ...
    """"""

class SecurityDocument(Object):
    """"""

    @overload
    def __init__(self, elRoot: SecurityElement):
        """:param elRoot:"""
    @overload
    def __init__(self, data: Array[int]):
        """:param data:"""
    @overload
    def __init__(self, numData: int):
        """:param numData:"""
    def AddString(self, str: str, position: int) -> None:
        """:param str:
        :param position:
        """
    def AddToken(self, b: int, position: int) -> None:
        """:param b:
        :param position:
        """
    def AppendString(self, str: str, position: int) -> None:
        """:param str:
        :param position:
        """
    def ConvertElement(self, elCurrent: SecurityElement, position: int) -> None:
        """:param elCurrent:
        :param position:
        """
    @classmethod
    def EncodedStringSize(cls, str: str) -> int:
        """:param str:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetAttributeForElement(self, position: int, attributeName: str) -> str:
        """:param position:
        :param attributeName:
        :return:
        """
    def GetChildrenPositionForElement(self, position: int) -> ArrayList:
        """:param position:
        :return:
        """
    def GetElement(self, position: int, bCreate: bool) -> SecurityElement:
        """:param position:
        :param bCreate:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetRootElement(self) -> SecurityElement:
        """:return:"""
    @overload
    def GetString(self, position: int) -> str:
        """:param position:
        :return:
        """
    @overload
    def GetString(self, position: int, bCreate: bool) -> str:
        """:param position:
        :param bCreate:
        :return:
        """
    def GetTagForElement(self, position: int) -> str:
        """:param position:
        :return:
        """
    def GetType(self) -> Type:
        """:return:"""
    def GuaranteeSize(self, size: int) -> None:
        """:param size:"""
    def ToString(self) -> str:
        """:return:"""

class SecurityDocumentElement(Object, ISecurityElementFactory):
    """"""

    def Attribute(self, attributeName: str) -> str:
        """:param attributeName:
        :return:
        """
    def Copy(self) -> object:
        """:return:"""
    def CreateSecurityElement(self) -> SecurityElement:
        """:return:"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetTag(self) -> str:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class SecurityElement(Object, ISecurityElementFactory):
    """"""

    @overload
    def __init__(self, tag: str):
        """:param tag:"""
    @overload
    def __init__(self, tag: str, text: str):
        """:param tag:
        :param text:
        """
    @property
    def Attributes(self) -> Hashtable:
        """:return:"""
    @Attributes.setter
    def Attributes(self, value: Hashtable) -> None: ...
    @property
    def Children(self) -> ArrayList:
        """:return:"""
    @Children.setter
    def Children(self, value: ArrayList) -> None: ...
    @property
    def Tag(self) -> str:
        """:return:"""
    @Tag.setter
    def Tag(self, value: str) -> None: ...
    @property
    def Text(self) -> str:
        """:return:"""
    @Text.setter
    def Text(self, value: str) -> None: ...
    def AddAttribute(self, name: str, value: str) -> None:
        """:param name:
        :param value:
        """
    def AddChild(self, child: SecurityElement) -> None:
        """:param child:"""
    def Attribute(self, attributeName: str) -> str:
        """:param attributeName:
        :return:
        """
    def Copy(self) -> object:
        """:return:"""
    def CreateSecurityElement(self) -> SecurityElement:
        """:return:"""
    def Equal(self, other: SecurityElement) -> bool:
        """:param other:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @classmethod
    def Escape(cls, str: str) -> str:
        """:param str:
        :return:
        """
    @classmethod
    def FromString(cls, xml: str) -> SecurityElement:
        """:param xml:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetTag(self) -> str:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    @classmethod
    def IsValidAttributeName(cls, name: str) -> bool:
        """:param name:
        :return:
        """
    @classmethod
    def IsValidAttributeValue(cls, value: str) -> bool:
        """:param value:
        :return:
        """
    @classmethod
    def IsValidTag(cls, tag: str) -> bool:
        """:param tag:
        :return:
        """
    @classmethod
    def IsValidText(cls, text: str) -> bool:
        """:param text:
        :return:
        """
    def SearchForChildByTag(self, tag: str) -> SecurityElement:
        """:param tag:
        :return:
        """
    def SearchForTextOfTag(self, tag: str) -> str:
        """:param tag:
        :return:
        """
    def ToString(self) -> str:
        """:return:"""

class SecurityElementType(Enum):
    """"""

    Regular: SecurityElementType = ...
    """"""
    Format: SecurityElementType = ...
    """"""
    Comment: SecurityElementType = ...
    """"""

class SecurityException(SystemException, _Exception, ISerializable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, message: str):
        """:param message:"""
    @overload
    def __init__(self, message: str, inner: Exception):
        """:param message:
        :param inner:
        """
    @overload
    def __init__(self, message: str, type: Type):
        """:param message:
        :param type:
        """
    @overload
    def __init__(self, message: str, type: Type, state: str):
        """:param message:
        :param type:
        :param state:
        """
    @overload
    def __init__(
        self,
        message: str,
        deny: object,
        permitOnly: object,
        method: MethodInfo,
        demanded: object,
        permThatFailed: IPermission,
    ):
        """:param message:
        :param deny:
        :param permitOnly:
        :param method:
        :param demanded:
        :param permThatFailed:
        """
    @overload
    def __init__(
        self,
        message: str,
        assemblyName: AssemblyName,
        grant: PermissionSet,
        refused: PermissionSet,
        method: MethodInfo,
        action: SecurityAction,
        demanded: object,
        permThatFailed: IPermission,
        evidence: Evidence,
    ):
        """:param message:
        :param assemblyName:
        :param grant:
        :param refused:
        :param method:
        :param action:
        :param demanded:
        :param permThatFailed:
        :param evidence:
        """
    @property
    def Action(self) -> SecurityAction:
        """:return:"""
    @Action.setter
    def Action(self, value: SecurityAction) -> None: ...
    @property
    def Data(self) -> IDictionary:
        """:return:"""
    @property
    def Demanded(self) -> object:
        """:return:"""
    @Demanded.setter
    def Demanded(self, value: object) -> None: ...
    @property
    def DenySetInstance(self) -> object:
        """:return:"""
    @DenySetInstance.setter
    def DenySetInstance(self, value: object) -> None: ...
    @property
    def FailedAssemblyInfo(self) -> AssemblyName:
        """:return:"""
    @FailedAssemblyInfo.setter
    def FailedAssemblyInfo(self, value: AssemblyName) -> None: ...
    @property
    def FirstPermissionThatFailed(self) -> IPermission:
        """:return:"""
    @FirstPermissionThatFailed.setter
    def FirstPermissionThatFailed(self, value: IPermission) -> None: ...
    @property
    def GrantedSet(self) -> str:
        """:return:"""
    @GrantedSet.setter
    def GrantedSet(self, value: str) -> None: ...
    @property
    def HResult(self) -> int:
        """:return:"""
    @property
    def HelpLink(self) -> str:
        """:return:"""
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """:return:"""
    @property
    def Message(self) -> str:
        """:return:"""
    @property
    def Method(self) -> MethodInfo:
        """:return:"""
    @Method.setter
    def Method(self, value: MethodInfo) -> None: ...
    @property
    def PermissionState(self) -> str:
        """:return:"""
    @PermissionState.setter
    def PermissionState(self, value: str) -> None: ...
    @property
    def PermissionType(self) -> Type:
        """:return:"""
    @PermissionType.setter
    def PermissionType(self, value: Type) -> None: ...
    @property
    def PermitOnlySetInstance(self) -> object:
        """:return:"""
    @PermitOnlySetInstance.setter
    def PermitOnlySetInstance(self, value: object) -> None: ...
    @property
    def RefusedSet(self) -> str:
        """:return:"""
    @RefusedSet.setter
    def RefusedSet(self, value: str) -> None: ...
    @property
    def Source(self) -> str:
        """:return:"""
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """:return:"""
    @property
    def TargetSite(self) -> MethodBase:
        """:return:"""
    @property
    def Url(self) -> str:
        """:return:"""
    @Url.setter
    def Url(self, value: str) -> None: ...
    @property
    def Zone(self) -> SecurityZone:
        """:return:"""
    @Zone.setter
    def Zone(self, value: SecurityZone) -> None: ...
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetBaseException(self) -> Exception:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""

class SecurityManager(ABC, Object):
    """"""

    @classmethod
    @property
    def CheckExecutionRights(cls) -> bool:
        """:return:"""
    @classmethod
    @CheckExecutionRights.setter
    def CheckExecutionRights(cls, value: bool) -> None: ...
    @classmethod
    @property
    def SecurityEnabled(cls) -> bool:
        """:return:"""
    @classmethod
    @SecurityEnabled.setter
    def SecurityEnabled(cls, value: bool) -> None: ...
    @classmethod
    def CurrentThreadRequiresSecurityContextCapture(cls) -> bool:
        """:return:"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    @classmethod
    def GetStandardSandbox(cls, evidence: Evidence) -> PermissionSet:
        """:param evidence:
        :return:
        """
    def GetType(self) -> Type:
        """:return:"""
    @classmethod
    def GetZoneAndOrigin(
        cls, zone: ArrayList, origin: ArrayList
    ) -> tuple[None, ArrayList, ArrayList]:
        """:param zone:
        :param origin:
        """
    @classmethod
    def IsGranted(cls, perm: IPermission) -> bool:
        """:param perm:
        :return:
        """
    @classmethod
    def LoadPolicyLevelFromFile(cls, path: str, type: PolicyLevelType) -> PolicyLevel:
        """:param path:
        :param type:
        :return:
        """
    @classmethod
    def LoadPolicyLevelFromString(cls, str: str, type: PolicyLevelType) -> PolicyLevel:
        """:param str:
        :param type:
        :return:
        """
    @classmethod
    def PolicyHierarchy(cls) -> IEnumerator:
        """:return:"""
    @classmethod
    @overload
    def ResolvePolicy(cls, evidence: Evidence) -> PermissionSet:
        """:param evidence:
        :return:
        """
    @classmethod
    @overload
    def ResolvePolicy(cls, evidences: Array[Evidence]) -> PermissionSet:
        """:param evidences:
        :return:
        """
    @classmethod
    @overload
    def ResolvePolicy(
        cls,
        evidence: Evidence,
        reqdPset: PermissionSet,
        optPset: PermissionSet,
        denyPset: PermissionSet,
        denied: PermissionSet,
    ) -> tuple[PermissionSet, PermissionSet]:
        """:param evidence:
        :param reqdPset:
        :param optPset:
        :param denyPset:
        :param denied:
        :return:
        """
    @classmethod
    def ResolvePolicyGroups(cls, evidence: Evidence) -> IEnumerator:
        """:param evidence:
        :return:
        """
    @classmethod
    def ResolveSystemPolicy(cls, evidence: Evidence) -> PermissionSet:
        """:param evidence:
        :return:
        """
    @classmethod
    def SavePolicy(cls) -> None:
        """"""
    @classmethod
    def SavePolicyLevel(cls, level: PolicyLevel) -> None:
        """:param level:"""
    def ToString(self) -> str:
        """:return:"""

class SecurityRuleSet(Enum):
    """"""

    _None: SecurityRuleSet = ...
    """"""
    Level1: SecurityRuleSet = ...
    """"""
    Level2: SecurityRuleSet = ...
    """"""

class SecurityRulesAttribute(Attribute, _Attribute):
    """"""

    def __init__(self, ruleSet: SecurityRuleSet):
        """:param ruleSet:"""
    @property
    def RuleSet(self) -> SecurityRuleSet:
        """:return:"""
    @property
    def SkipVerificationInFullTrust(self) -> bool:
        """:return:"""
    @SkipVerificationInFullTrust.setter
    def SkipVerificationInFullTrust(self, value: bool) -> None: ...
    @property
    def TypeId(self) -> object:
        """:return:"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """:param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """:return:"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """:param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> tuple[None, int]:
        """:param pcTInfo:"""
    def Invoke(
        self,
        dispIdMember: int,
        riid: Guid,
        lcid: int,
        wFlags: int,
        pDispParams: IntPtr,
        pVarResult: IntPtr,
        pExcepInfo: IntPtr,
        puArgErr: IntPtr,
    ) -> None:
        """:param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """:return:"""
    def Match(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def ToString(self) -> str:
        """:return:"""

class SecurityRuntime(Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class SecuritySafeCriticalAttribute(Attribute, _Attribute):
    """"""

    def __init__(self):
        """"""
    @property
    def TypeId(self) -> object:
        """:return:"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """:param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """:return:"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """:param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> tuple[None, int]:
        """:param pcTInfo:"""
    def Invoke(
        self,
        dispIdMember: int,
        riid: Guid,
        lcid: int,
        wFlags: int,
        pDispParams: IntPtr,
        pVarResult: IntPtr,
        pExcepInfo: IntPtr,
        puArgErr: IntPtr,
    ) -> None:
        """:param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """:return:"""
    def Match(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def ToString(self) -> str:
        """:return:"""

class SecurityState(ABC, Object):
    """"""

    def EnsureState(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def IsStateAvailable(self) -> bool:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class SecurityTransparentAttribute(Attribute, _Attribute):
    """"""

    def __init__(self):
        """"""
    @property
    def TypeId(self) -> object:
        """:return:"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """:param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """:return:"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """:param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> tuple[None, int]:
        """:param pcTInfo:"""
    def Invoke(
        self,
        dispIdMember: int,
        riid: Guid,
        lcid: int,
        wFlags: int,
        pDispParams: IntPtr,
        pVarResult: IntPtr,
        pExcepInfo: IntPtr,
        puArgErr: IntPtr,
    ) -> None:
        """:param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """:return:"""
    def Match(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def ToString(self) -> str:
        """:return:"""

class SecurityTreatAsSafeAttribute(Attribute, _Attribute):
    """"""

    def __init__(self):
        """"""
    @property
    def TypeId(self) -> object:
        """:return:"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """:param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """:return:"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """:param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> tuple[None, int]:
        """:param pcTInfo:"""
    def Invoke(
        self,
        dispIdMember: int,
        riid: Guid,
        lcid: int,
        wFlags: int,
        pDispParams: IntPtr,
        pVarResult: IntPtr,
        pExcepInfo: IntPtr,
        puArgErr: IntPtr,
    ) -> None:
        """:param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """:return:"""
    def Match(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def ToString(self) -> str:
        """:return:"""

class SecurityZone(Enum):
    """"""

    MyComputer: SecurityZone = ...
    """"""
    Intranet: SecurityZone = ...
    """"""
    Trusted: SecurityZone = ...
    """"""
    Internet: SecurityZone = ...
    """"""
    Untrusted: SecurityZone = ...
    """"""
    NoZone: SecurityZone = ...
    """"""

class SpecialPermissionSetFlag(Enum):
    """"""

    Regular: SpecialPermissionSetFlag = ...
    """"""
    NoSet: SpecialPermissionSetFlag = ...
    """"""
    EmptySet: SpecialPermissionSetFlag = ...
    """"""
    SkipVerification: SpecialPermissionSetFlag = ...
    """"""

class SuppressUnmanagedCodeSecurityAttribute(Attribute, _Attribute):
    """"""

    def __init__(self):
        """"""
    @property
    def TypeId(self) -> object:
        """:return:"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """:param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """:return:"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """:param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> tuple[None, int]:
        """:param pcTInfo:"""
    def Invoke(
        self,
        dispIdMember: int,
        riid: Guid,
        lcid: int,
        wFlags: int,
        pDispParams: IntPtr,
        pVarResult: IntPtr,
        pExcepInfo: IntPtr,
        puArgErr: IntPtr,
    ) -> None:
        """:param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """:return:"""
    def Match(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def ToString(self) -> str:
        """:return:"""

class UnverifiableCodeAttribute(Attribute, _Attribute):
    """"""

    def __init__(self):
        """"""
    @property
    def TypeId(self) -> object:
        """:return:"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """:param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """:return:"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """:param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> tuple[None, int]:
        """:param pcTInfo:"""
    def Invoke(
        self,
        dispIdMember: int,
        riid: Guid,
        lcid: int,
        wFlags: int,
        pDispParams: IntPtr,
        pVarResult: IntPtr,
        pExcepInfo: IntPtr,
        puArgErr: IntPtr,
    ) -> None:
        """:param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """:return:"""
    def Match(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def ToString(self) -> str:
        """:return:"""

class VerificationException(SystemException, _Exception, ISerializable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, message: str):
        """:param message:"""
    @overload
    def __init__(self, message: str, innerException: Exception):
        """:param message:
        :param innerException:
        """
    @property
    def Data(self) -> IDictionary:
        """:return:"""
    @property
    def HResult(self) -> int:
        """:return:"""
    @property
    def HelpLink(self) -> str:
        """:return:"""
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """:return:"""
    @property
    def Message(self) -> str:
        """:return:"""
    @property
    def Source(self) -> str:
        """:return:"""
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """:return:"""
    @property
    def TargetSite(self) -> MethodBase:
        """:return:"""
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetBaseException(self) -> Exception:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""

class WindowsImpersonationFlowMode(Enum):
    """"""

    IMP_DEFAULT: WindowsImpersonationFlowMode = ...
    """"""
    IMP_FASTFLOW: WindowsImpersonationFlowMode = ...
    """"""
    IMP_NOFLOW: WindowsImpersonationFlowMode = ...
    """"""
    IMP_ALWAYSFLOW: WindowsImpersonationFlowMode = ...
    """"""

class XmlSyntaxException(SystemException, _Exception, ISerializable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, lineNumber: int):
        """:param lineNumber:"""
    @overload
    def __init__(self, message: str):
        """:param message:"""
    @overload
    def __init__(self, lineNumber: int, message: str):
        """:param lineNumber:
        :param message:
        """
    @overload
    def __init__(self, message: str, inner: Exception):
        """:param message:
        :param inner:
        """
    @property
    def Data(self) -> IDictionary:
        """:return:"""
    @property
    def HResult(self) -> int:
        """:return:"""
    @property
    def HelpLink(self) -> str:
        """:return:"""
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """:return:"""
    @property
    def Message(self) -> str:
        """:return:"""
    @property
    def Source(self) -> str:
        """:return:"""
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """:return:"""
    @property
    def TargetSite(self) -> MethodBase:
        """:return:"""
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetBaseException(self) -> Exception:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetHashCode(self) -> int:
        """:return:"""
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """:param info:
        :param context:
        """
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def GetType(self) -> Type:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""
    @overload
    def ToString(self) -> str:
        """:return:"""
