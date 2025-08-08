"""Automatically generated stubs for C# namespace: System.Security."""

from abc import ABC
from collections.abc import Iterator
from typing import overload

from System import Array
from System import Attribute
from System import Boolean
from System import Byte
from System import Char
from System import Enum
from System import Exception
from System import Guid
from System import IDisposable
from System import Int32
from System import IntPtr
from System import Object
from System import SystemException
from System import Type
from System import UInt32
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

class AllowPartiallyTrustedCallersAttribute(Attribute, _Attribute):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def PartialTrustVisibilityLevel(self) -> PartialTrustVisibilityLevel:
        """"""
    @PartialTrustVisibilityLevel.setter
    def PartialTrustVisibilityLevel(self, value: PartialTrustVisibilityLevel) -> None: ...
    @property
    def TypeId(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """"""
    def GetTypeInfoCount(self, pcTInfo: UInt32) -> tuple[None, UInt32]:
        """"""
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
        """"""
    def IsDefaultAttribute(self) -> bool:
        """"""
    def Match(self, obj: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

class BuiltInPermissionSets(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class CodeAccessPermission(ABC, Object, IPermission, ISecurityEncodable, IStackWalk):
    """"""
    def Assert(self) -> None:
        """"""
    def Copy(self) -> IPermission:
        """"""
    def Demand(self) -> None:
        """"""
    def Deny(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def FromXml(self, elem: SecurityElement) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Intersect(self, target: IPermission) -> IPermission:
        """"""
    def IsSubsetOf(self, target: IPermission) -> bool:
        """"""
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
        """"""
    def ToXml(self) -> SecurityElement:
        """"""
    def Union(self, other: IPermission) -> IPermission:
        """"""

class CodeAccessSecurityEngine(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class DynamicSecurityMethodAttribute(Attribute, _Attribute):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """"""
    def GetTypeInfoCount(self, pcTInfo: UInt32) -> tuple[None, UInt32]:
        """"""
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
        """"""
    def IsDefaultAttribute(self) -> bool:
        """"""
    def Match(self, obj: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

class FrameSecurityDescriptor(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class FrameSecurityDescriptorWithResolver(FrameSecurityDescriptor):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Resolver(self) -> DynamicResolver:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class HostProtectionException(SystemException, _Exception, ISerializable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, message: str) -> None:
        """"""
    @overload
    def __init__(self, message: str, e: Exception) -> None:
        """"""
    @overload
    def __init__(
        self,
        message: str,
        protectedResources: HostProtectionResource,
        demandedResources: HostProtectionResource,
    ) -> None:
        """"""
    @property
    def Data(self) -> IDictionary:
        """"""
    @property
    def DemandedResources(self) -> HostProtectionResource:
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
    def ProtectedResources(self) -> HostProtectionResource:
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

class HostSecurityManager(Object):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def DomainPolicy(self) -> PolicyLevel:
        """"""
    @property
    def Flags(self) -> HostSecurityManagerOptions:
        """"""
    def DetermineApplicationTrust(
        self,
        applicationEvidence: Evidence,
        activatorEvidence: Evidence,
        context: TrustManagerContext,
    ) -> ApplicationTrust:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GenerateAppDomainEvidence(self, evidenceType: Type) -> EvidenceBase:
        """"""
    def GenerateAssemblyEvidence(self, evidenceType: Type, assembly: Assembly) -> EvidenceBase:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetHostSuppliedAppDomainEvidenceTypes(self) -> Array[Type]:
        """"""
    def GetHostSuppliedAssemblyEvidenceTypes(self, assembly: Assembly) -> Array[Type]:
        """"""
    def GetType(self) -> Type:
        """"""
    def ProvideAppDomainEvidence(self, inputEvidence: Evidence) -> Evidence:
        """"""
    def ProvideAssemblyEvidence(
        self, loadedAssembly: Assembly, inputEvidence: Evidence
    ) -> Evidence:
        """"""
    def ResolvePolicy(self, evidence: Evidence) -> PermissionSet:
        """"""
    def ToString(self) -> str:
        """"""

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

class IEvidenceFactory(ABC):
    """"""
    @property
    def Evidence(self) -> Evidence:
        """"""

class IPermission(ABC, ISecurityEncodable):
    """"""
    def Copy(self) -> IPermission:
        """"""
    def Demand(self) -> None:
        """"""
    def FromXml(self, e: SecurityElement) -> None:
        """"""
    def Intersect(self, target: IPermission) -> IPermission:
        """"""
    def IsSubsetOf(self, target: IPermission) -> bool:
        """"""
    def ToXml(self) -> SecurityElement:
        """"""
    def Union(self, target: IPermission) -> IPermission:
        """"""

class ISecurityElementFactory(ABC):
    """"""
    def Attribute(self, attributeName: str) -> str:
        """"""
    def Copy(self) -> object:
        """"""
    def CreateSecurityElement(self) -> SecurityElement:
        """"""
    def GetTag(self) -> str:
        """"""

class ISecurityEncodable(ABC):
    """"""
    def FromXml(self, e: SecurityElement) -> None:
        """"""
    def ToXml(self) -> SecurityElement:
        """"""

class ISecurityPolicyEncodable(ABC):
    """"""
    def FromXml(self, e: SecurityElement, level: PolicyLevel) -> None:
        """"""
    def ToXml(self, level: PolicyLevel) -> SecurityElement:
        """"""

class IStackWalk(ABC):
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
    def __init__(self, name: str) -> None:
        """"""
    @overload
    def __init__(self, name: str, state: PermissionState) -> None:
        """"""
    @overload
    def __init__(self, name: str, permSet: PermissionSet) -> None:
        """"""
    @overload
    def __init__(self, permSet: NamedPermissionSet) -> None:
        """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def Description(self) -> str:
        """"""
    @Description.setter
    def Description(self, value: str) -> None: ...
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def SyncRoot(self) -> object:
        """"""
    def AddPermission(self, perm: IPermission) -> IPermission:
        """"""
    def Assert(self) -> None:
        """"""
    def ContainsNonCodeAccessPermissions(self) -> bool:
        """"""
    @overload
    def Copy(self) -> PermissionSet:
        """"""
    @overload
    def Copy(self, name: str) -> NamedPermissionSet:
        """"""
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    def Demand(self) -> None:
        """"""
    def Deny(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def FromXml(self, et: SecurityElement) -> None:
        """"""
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetPermission(self, permClass: Type) -> IPermission:
        """"""
    def GetType(self) -> Type:
        """"""
    def Intersect(self, other: PermissionSet) -> PermissionSet:
        """"""
    def IsEmpty(self) -> bool:
        """"""
    def IsSubsetOf(self, target: PermissionSet) -> bool:
        """"""
    def IsUnrestricted(self) -> bool:
        """"""
    def OnDeserialization(self, sender: object) -> None:
        """"""
    def PermitOnly(self) -> None:
        """"""
    def RemovePermission(self, permClass: Type) -> IPermission:
        """"""
    def SetPermission(self, perm: IPermission) -> IPermission:
        """"""
    def ToString(self) -> str:
        """"""
    def ToXml(self) -> SecurityElement:
        """"""
    def Union(self, other: PermissionSet) -> PermissionSet:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    def __len__(self) -> int:
        """"""

class PartialTrustVisibilityLevel(Enum):
    """"""

    VisibleToAllHosts: PartialTrustVisibilityLevel = ...
    """"""
    NotVisibleByDefault: PartialTrustVisibilityLevel = ...
    """"""

class PermissionListSet(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class PermissionSet(
    Object, ICollection, IEnumerable, IDeserializationCallback, ISecurityEncodable, IStackWalk
):
    """"""
    @overload
    def __init__(self, state: PermissionState) -> None:
        """"""
    @overload
    def __init__(self, permSet: PermissionSet) -> None:
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
    def SyncRoot(self) -> object:
        """"""
    def AddPermission(self, perm: IPermission) -> IPermission:
        """"""
    def Assert(self) -> None:
        """"""
    def ContainsNonCodeAccessPermissions(self) -> bool:
        """"""
    @classmethod
    def ConvertPermissionSet(cls, inFormat: str, inData: Array[int], outFormat: str) -> Array[int]:
        """"""
    def Copy(self) -> PermissionSet:
        """"""
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    def Demand(self) -> None:
        """"""
    def Deny(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def FromXml(self, et: SecurityElement) -> None:
        """"""
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetPermission(self, permClass: Type) -> IPermission:
        """"""
    def GetType(self) -> Type:
        """"""
    def Intersect(self, other: PermissionSet) -> PermissionSet:
        """"""
    def IsEmpty(self) -> bool:
        """"""
    def IsSubsetOf(self, target: PermissionSet) -> bool:
        """"""
    def IsUnrestricted(self) -> bool:
        """"""
    def OnDeserialization(self, sender: object) -> None:
        """"""
    def PermitOnly(self) -> None:
        """"""
    def RemovePermission(self, permClass: Type) -> IPermission:
        """"""
    @classmethod
    def RevertAssert(cls) -> None:
        """"""
    def SetPermission(self, perm: IPermission) -> IPermission:
        """"""
    def ToString(self) -> str:
        """"""
    def ToXml(self) -> SecurityElement:
        """"""
    def Union(self, other: PermissionSet) -> PermissionSet:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    def __len__(self) -> int:
        """"""

class PermissionSetEnumerator(Object, IEnumerator):
    """"""
    @property
    def Current(self) -> object:
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

class PermissionSetEnumeratorInternal(ValueType):
    """"""
    @property
    def Current(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetCurrentIndex(self) -> int:
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

class PermissionSetTriple(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class PermissionToken(Object, ISecurityEncodable):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def FindToken(cls, cls: Type) -> PermissionToken:
        """"""
    @classmethod
    def FindTokenByIndex(cls, i: int) -> PermissionToken:
        """"""
    def FromXml(self, elRoot: SecurityElement) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @classmethod
    @overload
    def GetToken(cls, perm: IPermission) -> PermissionToken:
        """"""
    @classmethod
    @overload
    def GetToken(cls, typeStr: str) -> PermissionToken:
        """"""
    @classmethod
    @overload
    def GetToken(cls, typeStr: str, bCreateMscorlib: bool) -> PermissionToken:
        """"""
    @classmethod
    @overload
    def GetToken(cls, cls: Type) -> PermissionToken:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def IsTokenProperlyAssigned(cls, perm: IPermission, token: PermissionToken) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    def ToXml(self) -> SecurityElement:
        """"""

class PermissionTokenFactory(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class PermissionTokenKeyComparer(Object, IEqualityComparer):
    """"""
    def __init__(self) -> None:
        """"""
    def Compare(self, a: object, b: object) -> int:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, a: object, b: object) -> bool:
        """"""
    @overload
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetHashCode(self, obj: object) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

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
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ReadOnlyPermissionSet(
    PermissionSet,
    ICollection,
    IEnumerable,
    IDeserializationCallback,
    ISecurityEncodable,
    IStackWalk,
):
    """"""
    def __init__(self, permissionSetXml: SecurityElement) -> None:
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
    def SyncRoot(self) -> object:
        """"""
    def AddPermission(self, perm: IPermission) -> IPermission:
        """"""
    def Assert(self) -> None:
        """"""
    def ContainsNonCodeAccessPermissions(self) -> bool:
        """"""
    def Copy(self) -> PermissionSet:
        """"""
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    def Demand(self) -> None:
        """"""
    def Deny(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def FromXml(self, et: SecurityElement) -> None:
        """"""
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetPermission(self, permClass: Type) -> IPermission:
        """"""
    def GetType(self) -> Type:
        """"""
    def Intersect(self, other: PermissionSet) -> PermissionSet:
        """"""
    def IsEmpty(self) -> bool:
        """"""
    def IsSubsetOf(self, target: PermissionSet) -> bool:
        """"""
    def IsUnrestricted(self) -> bool:
        """"""
    def OnDeserialization(self, sender: object) -> None:
        """"""
    def PermitOnly(self) -> None:
        """"""
    def RemovePermission(self, permClass: Type) -> IPermission:
        """"""
    def SetPermission(self, perm: IPermission) -> IPermission:
        """"""
    def ToString(self) -> str:
        """"""
    def ToXml(self) -> SecurityElement:
        """"""
    def Union(self, other: PermissionSet) -> PermissionSet:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    def __len__(self) -> int:
        """"""

class ReadOnlyPermissionSetEnumerator(Object, IEnumerator):
    """"""
    @property
    def Current(self) -> object:
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

class SafeBSTRHandle(SafeBuffer, IDisposable):
    """"""
    @property
    def ByteLength(self) -> int:
        """"""
    @property
    def IsClosed(self) -> bool:
        """"""
    @property
    def IsInvalid(self) -> bool:
        """"""
    def AcquirePointer(self, pointer: Byte) -> None:
        """"""
    def Close(self) -> None:
        """"""
    def DangerousAddRef(self, success: Boolean) -> None:
        """"""
    def DangerousGetHandle(self) -> IntPtr:
        """"""
    def DangerousRelease(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def Initialize(self, numElements: int) -> None:
        """"""
    @overload
    def Initialize(self, numElements: int, sizeOfEachElement: int) -> None:
        """"""
    @overload
    def Initialize(self, numBytes: int) -> None:
        """"""
    def Read[T](self, byteOffset: int) -> T:
        """"""
    def ReadArray[T](self, byteOffset: int, array: Array[T], index: int, count: int) -> None:
        """"""
    def ReleasePointer(self) -> None:
        """"""
    def SetHandleAsInvalid(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def Write[T](self, byteOffset: int, value: T) -> None:
        """"""
    def WriteArray[T](self, byteOffset: int, array: Array[T], index: int, count: int) -> None:
        """"""

class SecureString(Object, IDisposable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, value: Char, length: int) -> None:
        """"""
    @property
    def Length(self) -> int:
        """"""
    def AppendChar(self, c: Char) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    def Copy(self) -> SecureString:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def InsertAt(self, index: int, c: Char) -> None:
        """"""
    def IsReadOnly(self) -> bool:
        """"""
    def MakeReadOnly(self) -> None:
        """"""
    def RemoveAt(self, index: int) -> None:
        """"""
    def SetAt(self, index: int, c: Char) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class SecureStringMarshal(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def SecureStringToCoTaskMemAnsi(cls, s: SecureString) -> IntPtr:
        """"""
    @classmethod
    def SecureStringToCoTaskMemUnicode(cls, s: SecureString) -> IntPtr:
        """"""
    @classmethod
    def SecureStringToGlobalAllocAnsi(cls, s: SecureString) -> IntPtr:
        """"""
    @classmethod
    def SecureStringToGlobalAllocUnicode(cls, s: SecureString) -> IntPtr:
        """"""
    def ToString(self) -> str:
        """"""

class SecurityContext(Object, IDisposable):
    """"""
    @classmethod
    def Capture(cls) -> SecurityContext:
        """"""
    def CreateCopy(self) -> SecurityContext:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def IsFlowSuppressed(cls) -> bool:
        """"""
    @classmethod
    def IsWindowsIdentityFlowSuppressed(cls) -> bool:
        """"""
    @classmethod
    def RestoreFlow(cls) -> None:
        """"""
    @classmethod
    def Run(
        cls, securityContext: SecurityContext, callback: ContextCallback, state: object
    ) -> None:
        """"""
    @classmethod
    def SuppressFlow(cls) -> AsyncFlowControl:
        """"""
    @classmethod
    def SuppressFlowWindowsIdentity(cls) -> AsyncFlowControl:
        """"""
    def ToString(self) -> str:
        """"""

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
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def Undo(self) -> None:
        """"""

class SecurityCriticalAttribute(Attribute, _Attribute):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, scope: SecurityCriticalScope) -> None:
        """"""
    @property
    def Scope(self) -> SecurityCriticalScope:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """"""
    def GetTypeInfoCount(self, pcTInfo: UInt32) -> tuple[None, UInt32]:
        """"""
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
        """"""
    def IsDefaultAttribute(self) -> bool:
        """"""
    def Match(self, obj: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

class SecurityCriticalScope(Enum):
    """"""

    Explicit: SecurityCriticalScope = ...
    """"""
    Everything: SecurityCriticalScope = ...
    """"""

class SecurityDocument(Object):
    """"""
    @overload
    def __init__(self, numData: int) -> None:
        """"""
    @overload
    def __init__(self, data: Array[int]) -> None:
        """"""
    @overload
    def __init__(self, elRoot: SecurityElement) -> None:
        """"""
    def AddString(self, str: str, position: Int32) -> None:
        """"""
    def AddToken(self, b: int, position: Int32) -> None:
        """"""
    def AppendString(self, str: str, position: Int32) -> None:
        """"""
    def ConvertElement(self, elCurrent: SecurityElement, position: Int32) -> None:
        """"""
    @classmethod
    def EncodedStringSize(cls, str: str) -> int:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetAttributeForElement(self, position: int, attributeName: str) -> str:
        """"""
    def GetChildrenPositionForElement(self, position: int) -> ArrayList:
        """"""
    def GetElement(self, position: int, bCreate: bool) -> SecurityElement:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetRootElement(self) -> SecurityElement:
        """"""
    @overload
    def GetString(self, position: Int32) -> str:
        """"""
    @overload
    def GetString(self, position: Int32, bCreate: bool) -> str:
        """"""
    def GetTagForElement(self, position: int) -> str:
        """"""
    def GetType(self) -> Type:
        """"""
    def GuaranteeSize(self, size: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class SecurityDocumentElement(Object, ISecurityElementFactory):
    """"""
    def Attribute(self, attributeName: str) -> str:
        """"""
    def Copy(self) -> object:
        """"""
    def CreateSecurityElement(self) -> SecurityElement:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetTag(self) -> str:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SecurityElement(Object, ISecurityElementFactory):
    """"""
    @overload
    def __init__(self, tag: str) -> None:
        """"""
    @overload
    def __init__(self, tag: str, text: str) -> None:
        """"""
    @property
    def Attributes(self) -> Hashtable:
        """"""
    @Attributes.setter
    def Attributes(self, value: Hashtable) -> None: ...
    @property
    def Children(self) -> ArrayList:
        """"""
    @Children.setter
    def Children(self, value: ArrayList) -> None: ...
    @property
    def Tag(self) -> str:
        """"""
    @Tag.setter
    def Tag(self, value: str) -> None: ...
    @property
    def Text(self) -> str:
        """"""
    @Text.setter
    def Text(self, value: str) -> None: ...
    def AddAttribute(self, name: str, value: str) -> None:
        """"""
    def AddChild(self, child: SecurityElement) -> None:
        """"""
    def Attribute(self, name: str) -> str:
        """"""
    def Copy(self) -> SecurityElement:
        """"""
    def CreateSecurityElement(self) -> SecurityElement:
        """"""
    def Equal(self, other: SecurityElement) -> bool:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def Escape(cls, str: str) -> str:
        """"""
    @classmethod
    def FromString(cls, xml: str) -> SecurityElement:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetTag(self) -> str:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def IsValidAttributeName(cls, name: str) -> bool:
        """"""
    @classmethod
    def IsValidAttributeValue(cls, value: str) -> bool:
        """"""
    @classmethod
    def IsValidTag(cls, tag: str) -> bool:
        """"""
    @classmethod
    def IsValidText(cls, text: str) -> bool:
        """"""
    def SearchForChildByTag(self, tag: str) -> SecurityElement:
        """"""
    def SearchForTextOfTag(self, tag: str) -> str:
        """"""
    def ToString(self) -> str:
        """"""

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
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, message: str) -> None:
        """"""
    @overload
    def __init__(self, message: str, type: Type) -> None:
        """"""
    @overload
    def __init__(self, message: str, type: Type, state: str) -> None:
        """"""
    @overload
    def __init__(self, message: str, inner: Exception) -> None:
        """"""
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
    ) -> None:
        """"""
    @overload
    def __init__(
        self,
        message: str,
        deny: object,
        permitOnly: object,
        method: MethodInfo,
        demanded: object,
        permThatFailed: IPermission,
    ) -> None:
        """"""
    @property
    def Action(self) -> SecurityAction:
        """"""
    @Action.setter
    def Action(self, value: SecurityAction) -> None: ...
    @property
    def Data(self) -> IDictionary:
        """"""
    @property
    def Demanded(self) -> object:
        """"""
    @Demanded.setter
    def Demanded(self, value: object) -> None: ...
    @property
    def DenySetInstance(self) -> object:
        """"""
    @DenySetInstance.setter
    def DenySetInstance(self, value: object) -> None: ...
    @property
    def FailedAssemblyInfo(self) -> AssemblyName:
        """"""
    @FailedAssemblyInfo.setter
    def FailedAssemblyInfo(self, value: AssemblyName) -> None: ...
    @property
    def FirstPermissionThatFailed(self) -> IPermission:
        """"""
    @FirstPermissionThatFailed.setter
    def FirstPermissionThatFailed(self, value: IPermission) -> None: ...
    @property
    def GrantedSet(self) -> str:
        """"""
    @GrantedSet.setter
    def GrantedSet(self, value: str) -> None: ...
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
    def Method(self) -> MethodInfo:
        """"""
    @Method.setter
    def Method(self, value: MethodInfo) -> None: ...
    @property
    def PermissionState(self) -> str:
        """"""
    @PermissionState.setter
    def PermissionState(self, value: str) -> None: ...
    @property
    def PermissionType(self) -> Type:
        """"""
    @PermissionType.setter
    def PermissionType(self, value: Type) -> None: ...
    @property
    def PermitOnlySetInstance(self) -> object:
        """"""
    @PermitOnlySetInstance.setter
    def PermitOnlySetInstance(self, value: object) -> None: ...
    @property
    def RefusedSet(self) -> str:
        """"""
    @RefusedSet.setter
    def RefusedSet(self, value: str) -> None: ...
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
    @property
    def Url(self) -> str:
        """"""
    @Url.setter
    def Url(self, value: str) -> None: ...
    @property
    def Zone(self) -> SecurityZone:
        """"""
    @Zone.setter
    def Zone(self, value: SecurityZone) -> None: ...
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

class SecurityManager(ABC, Object):
    """"""
    @classmethod
    @property
    def CheckExecutionRights(cls) -> bool:
        """"""
    @classmethod
    @CheckExecutionRights.setter
    def CheckExecutionRights(cls, value: bool) -> None: ...
    @classmethod
    @property
    def SecurityEnabled(cls) -> bool:
        """"""
    @classmethod
    @SecurityEnabled.setter
    def SecurityEnabled(cls, value: bool) -> None: ...
    @classmethod
    def CurrentThreadRequiresSecurityContextCapture(cls) -> bool:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @classmethod
    def GetStandardSandbox(cls, evidence: Evidence) -> PermissionSet:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def GetZoneAndOrigin(
        cls, zone: ArrayList, origin: ArrayList
    ) -> tuple[None, ArrayList, ArrayList]:
        """"""
    @classmethod
    def IsGranted(cls, perm: IPermission) -> bool:
        """"""
    @classmethod
    def LoadPolicyLevelFromFile(cls, path: str, type: PolicyLevelType) -> PolicyLevel:
        """"""
    @classmethod
    def LoadPolicyLevelFromString(cls, str: str, type: PolicyLevelType) -> PolicyLevel:
        """"""
    @classmethod
    def PolicyHierarchy(cls) -> IEnumerator:
        """"""
    @classmethod
    @overload
    def ResolvePolicy(cls, evidence: Evidence) -> PermissionSet:
        """"""
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
        """"""
    @classmethod
    @overload
    def ResolvePolicy(cls, evidences: Array[Evidence]) -> PermissionSet:
        """"""
    @classmethod
    def ResolvePolicyGroups(cls, evidence: Evidence) -> IEnumerator:
        """"""
    @classmethod
    def ResolveSystemPolicy(cls, evidence: Evidence) -> PermissionSet:
        """"""
    @classmethod
    def SavePolicy(cls) -> None:
        """"""
    @classmethod
    def SavePolicyLevel(cls, level: PolicyLevel) -> None:
        """"""
    def ToString(self) -> str:
        """"""

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
    def __init__(self, ruleSet: SecurityRuleSet) -> None:
        """"""
    @property
    def RuleSet(self) -> SecurityRuleSet:
        """"""
    @property
    def SkipVerificationInFullTrust(self) -> bool:
        """"""
    @SkipVerificationInFullTrust.setter
    def SkipVerificationInFullTrust(self, value: bool) -> None: ...
    @property
    def TypeId(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """"""
    def GetTypeInfoCount(self, pcTInfo: UInt32) -> tuple[None, UInt32]:
        """"""
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
        """"""
    def IsDefaultAttribute(self) -> bool:
        """"""
    def Match(self, obj: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

class SecurityRuntime(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SecuritySafeCriticalAttribute(Attribute, _Attribute):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """"""
    def GetTypeInfoCount(self, pcTInfo: UInt32) -> tuple[None, UInt32]:
        """"""
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
        """"""
    def IsDefaultAttribute(self) -> bool:
        """"""
    def Match(self, obj: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

class SecurityState(ABC, Object):
    """"""
    def EnsureState(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def IsStateAvailable(self) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

class SecurityTransparentAttribute(Attribute, _Attribute):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """"""
    def GetTypeInfoCount(self, pcTInfo: UInt32) -> tuple[None, UInt32]:
        """"""
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
        """"""
    def IsDefaultAttribute(self) -> bool:
        """"""
    def Match(self, obj: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

class SecurityTreatAsSafeAttribute(Attribute, _Attribute):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """"""
    def GetTypeInfoCount(self, pcTInfo: UInt32) -> tuple[None, UInt32]:
        """"""
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
        """"""
    def IsDefaultAttribute(self) -> bool:
        """"""
    def Match(self, obj: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

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
    def __init__(self) -> None:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """"""
    def GetTypeInfoCount(self, pcTInfo: UInt32) -> tuple[None, UInt32]:
        """"""
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
        """"""
    def IsDefaultAttribute(self) -> bool:
        """"""
    def Match(self, obj: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

class UnverifiableCodeAttribute(Attribute, _Attribute):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """"""
    def GetTypeInfoCount(self, pcTInfo: UInt32) -> tuple[None, UInt32]:
        """"""
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
        """"""
    def IsDefaultAttribute(self) -> bool:
        """"""
    def Match(self, obj: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

class VerificationException(SystemException, _Exception, ISerializable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, message: str) -> None:
        """"""
    @overload
    def __init__(self, message: str, innerException: Exception) -> None:
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
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, message: str) -> None:
        """"""
    @overload
    def __init__(self, message: str, inner: Exception) -> None:
        """"""
    @overload
    def __init__(self, lineNumber: int) -> None:
        """"""
    @overload
    def __init__(self, lineNumber: int, message: str) -> None:
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
