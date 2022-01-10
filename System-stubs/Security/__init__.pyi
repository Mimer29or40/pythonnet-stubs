from __future__ import annotations

from abc import ABC
from typing import List, Protocol, Tuple, Union, overload

from System import Array, Attribute, Boolean, Byte, Char, Enum, Exception, IDisposable, Int32, IntPtr, Object, String, SystemException, Type, ValueType, Void
from System.Collections import ArrayList, Hashtable, ICollection, IEnumerable, IEnumerator, IEqualityComparer
from System.Reflection import Assembly, AssemblyName, MethodInfo
from System.Reflection.Emit import DynamicResolver
from System.Runtime.InteropServices import SafeBuffer, _Attribute, _Exception
from System.Runtime.Serialization import IDeserializationCallback, ISerializable, SerializationInfo, StreamingContext
from System.Security.Permissions import HostProtectionResource, PermissionState, SecurityAction
from System.Security.Policy import ApplicationTrust, Evidence, EvidenceBase, PolicyLevel, TrustManagerContext
from System.Threading import AsyncFlowControl, ContextCallback

# ---------- Types ---------- #

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
ByteType = Union[int, Byte]
CharType = Union[str, Char]
IntType = Union[int, Int32]
NIntType = Union[int, IntPtr]
ObjectType = Object
StringType = Union[str, String]
TypeType = Union[type, Type]
VoidType = Union[None, Void]

# ---------- Classes ---------- #

class AllowPartiallyTrustedCallersAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def PartialTrustVisibilityLevel(self) -> PartialTrustVisibilityLevel: ...
    
    @PartialTrustVisibilityLevel.setter
    def PartialTrustVisibilityLevel(self, value: PartialTrustVisibilityLevel) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_PartialTrustVisibilityLevel(self) -> PartialTrustVisibilityLevel: ...
    
    def set_PartialTrustVisibilityLevel(self, value: PartialTrustVisibilityLevel) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AllowPartiallyTrustedCallersAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def PartialTrustVisibilityLevel(self) -> PartialTrustVisibilityLevel: ...
    
    @PartialTrustVisibilityLevel.setter
    def PartialTrustVisibilityLevel(self, value: PartialTrustVisibilityLevel) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_PartialTrustVisibilityLevel(self) -> PartialTrustVisibilityLevel: ...
    
    def set_PartialTrustVisibilityLevel(self, value: PartialTrustVisibilityLevel) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AllowPartiallyTrustedCallersAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def PartialTrustVisibilityLevel(self) -> PartialTrustVisibilityLevel: ...
    
    @PartialTrustVisibilityLevel.setter
    def PartialTrustVisibilityLevel(self, value: PartialTrustVisibilityLevel) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_PartialTrustVisibilityLevel(self) -> PartialTrustVisibilityLevel: ...
    
    def set_PartialTrustVisibilityLevel(self, value: PartialTrustVisibilityLevel) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class BuiltInPermissionSets(ABC, ObjectType):
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


class BuiltInPermissionSets(ABC, ObjectType):
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


class BuiltInPermissionSets(ABC, ObjectType):
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


class CodeAccessPermission(ABC, ObjectType, IPermission, ISecurityEncodable, IStackWalk):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Assert(self) -> VoidType: ...
    
    def Copy(self) -> IPermission: ...
    
    def Demand(self) -> VoidType: ...
    
    def Deny(self) -> VoidType: ...
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def FromXml(self, elem: SecurityElement) -> VoidType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def Intersect(self, target: IPermission) -> IPermission: ...
    
    def IsSubsetOf(self, target: IPermission) -> BooleanType: ...
    
    def PermitOnly(self) -> VoidType: ...
    
    @staticmethod
    def RevertAll() -> VoidType: ...
    
    @staticmethod
    def RevertAssert() -> VoidType: ...
    
    @staticmethod
    def RevertDeny() -> VoidType: ...
    
    @staticmethod
    def RevertPermitOnly() -> VoidType: ...
    
    def ToString(self) -> StringType: ...
    
    def ToXml(self) -> SecurityElement: ...
    
    def Union(self, other: IPermission) -> IPermission: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeAccessPermission(ABC, ObjectType, IPermission, ISecurityEncodable, IStackWalk):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Assert(self) -> VoidType: ...
    
    def Copy(self) -> IPermission: ...
    
    def Demand(self) -> VoidType: ...
    
    def Deny(self) -> VoidType: ...
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def FromXml(self, elem: SecurityElement) -> VoidType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def Intersect(self, target: IPermission) -> IPermission: ...
    
    def IsSubsetOf(self, target: IPermission) -> BooleanType: ...
    
    def PermitOnly(self) -> VoidType: ...
    
    @staticmethod
    def RevertAll() -> VoidType: ...
    
    @staticmethod
    def RevertAssert() -> VoidType: ...
    
    @staticmethod
    def RevertDeny() -> VoidType: ...
    
    @staticmethod
    def RevertPermitOnly() -> VoidType: ...
    
    def ToString(self) -> StringType: ...
    
    def ToXml(self) -> SecurityElement: ...
    
    def Union(self, other: IPermission) -> IPermission: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeAccessPermission(ABC, ObjectType, IPermission, ISecurityEncodable, IStackWalk):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Assert(self) -> VoidType: ...
    
    def Copy(self) -> IPermission: ...
    
    def Demand(self) -> VoidType: ...
    
    def Deny(self) -> VoidType: ...
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def FromXml(self, elem: SecurityElement) -> VoidType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def Intersect(self, target: IPermission) -> IPermission: ...
    
    def IsSubsetOf(self, target: IPermission) -> BooleanType: ...
    
    def PermitOnly(self) -> VoidType: ...
    
    @staticmethod
    def RevertAll() -> VoidType: ...
    
    @staticmethod
    def RevertAssert() -> VoidType: ...
    
    @staticmethod
    def RevertDeny() -> VoidType: ...
    
    @staticmethod
    def RevertPermitOnly() -> VoidType: ...
    
    def ToString(self) -> StringType: ...
    
    def ToXml(self) -> SecurityElement: ...
    
    def Union(self, other: IPermission) -> IPermission: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeAccessSecurityEngine(ABC, ObjectType):
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


class CodeAccessSecurityEngine(ABC, ObjectType):
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


class CodeAccessSecurityEngine(ABC, ObjectType):
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


class DynamicSecurityMethodAttribute(Attribute, _Attribute):
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


class DynamicSecurityMethodAttribute(Attribute, _Attribute):
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


class DynamicSecurityMethodAttribute(Attribute, _Attribute):
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


class FrameSecurityDescriptor(ObjectType):
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


class FrameSecurityDescriptor(ObjectType):
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


class FrameSecurityDescriptor(ObjectType):
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


class FrameSecurityDescriptorWithResolver(FrameSecurityDescriptor):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Resolver(self) -> DynamicResolver: ...
    
    # ---------- Methods ---------- #
    
    def get_Resolver(self) -> DynamicResolver: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class FrameSecurityDescriptorWithResolver(FrameSecurityDescriptor):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Resolver(self) -> DynamicResolver: ...
    
    # ---------- Methods ---------- #
    
    def get_Resolver(self) -> DynamicResolver: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class FrameSecurityDescriptorWithResolver(FrameSecurityDescriptor):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Resolver(self) -> DynamicResolver: ...
    
    # ---------- Methods ---------- #
    
    def get_Resolver(self) -> DynamicResolver: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class HostProtectionException(SystemException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, e: Exception): ...
    
    @overload
    def __init__(self, message: StringType, protectedResources: HostProtectionResource, demandedResources: HostProtectionResource): ...
    
    # ---------- Properties ---------- #
    
    @property
    def DemandedResources(self) -> HostProtectionResource: ...
    
    @property
    def ProtectedResources(self) -> HostProtectionResource: ...
    
    # ---------- Methods ---------- #
    
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_DemandedResources(self) -> HostProtectionResource: ...
    
    def get_ProtectedResources(self) -> HostProtectionResource: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class HostProtectionException(SystemException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, e: Exception): ...
    
    @overload
    def __init__(self, message: StringType, protectedResources: HostProtectionResource, demandedResources: HostProtectionResource): ...
    
    # ---------- Properties ---------- #
    
    @property
    def DemandedResources(self) -> HostProtectionResource: ...
    
    @property
    def ProtectedResources(self) -> HostProtectionResource: ...
    
    # ---------- Methods ---------- #
    
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_DemandedResources(self) -> HostProtectionResource: ...
    
    def get_ProtectedResources(self) -> HostProtectionResource: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class HostProtectionException(SystemException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, e: Exception): ...
    
    @overload
    def __init__(self, message: StringType, protectedResources: HostProtectionResource, demandedResources: HostProtectionResource): ...
    
    # ---------- Properties ---------- #
    
    @property
    def DemandedResources(self) -> HostProtectionResource: ...
    
    @property
    def ProtectedResources(self) -> HostProtectionResource: ...
    
    # ---------- Methods ---------- #
    
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_DemandedResources(self) -> HostProtectionResource: ...
    
    def get_ProtectedResources(self) -> HostProtectionResource: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class HostSecurityManager(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def DomainPolicy(self) -> PolicyLevel: ...
    
    @property
    def Flags(self) -> HostSecurityManagerOptions: ...
    
    # ---------- Methods ---------- #
    
    def DetermineApplicationTrust(self, applicationEvidence: Evidence, activatorEvidence: Evidence, context: TrustManagerContext) -> ApplicationTrust: ...
    
    def GenerateAppDomainEvidence(self, evidenceType: TypeType) -> EvidenceBase: ...
    
    def GenerateAssemblyEvidence(self, evidenceType: TypeType, assembly: Assembly) -> EvidenceBase: ...
    
    def GetHostSuppliedAppDomainEvidenceTypes(self) -> ArrayType[TypeType]: ...
    
    def GetHostSuppliedAssemblyEvidenceTypes(self, assembly: Assembly) -> ArrayType[TypeType]: ...
    
    def ProvideAppDomainEvidence(self, inputEvidence: Evidence) -> Evidence: ...
    
    def ProvideAssemblyEvidence(self, loadedAssembly: Assembly, inputEvidence: Evidence) -> Evidence: ...
    
    def ResolvePolicy(self, evidence: Evidence) -> PermissionSet: ...
    
    def get_DomainPolicy(self) -> PolicyLevel: ...
    
    def get_Flags(self) -> HostSecurityManagerOptions: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class HostSecurityManager(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def DomainPolicy(self) -> PolicyLevel: ...
    
    @property
    def Flags(self) -> HostSecurityManagerOptions: ...
    
    # ---------- Methods ---------- #
    
    def DetermineApplicationTrust(self, applicationEvidence: Evidence, activatorEvidence: Evidence, context: TrustManagerContext) -> ApplicationTrust: ...
    
    def GenerateAppDomainEvidence(self, evidenceType: TypeType) -> EvidenceBase: ...
    
    def GenerateAssemblyEvidence(self, evidenceType: TypeType, assembly: Assembly) -> EvidenceBase: ...
    
    def GetHostSuppliedAppDomainEvidenceTypes(self) -> ArrayType[TypeType]: ...
    
    def GetHostSuppliedAssemblyEvidenceTypes(self, assembly: Assembly) -> ArrayType[TypeType]: ...
    
    def ProvideAppDomainEvidence(self, inputEvidence: Evidence) -> Evidence: ...
    
    def ProvideAssemblyEvidence(self, loadedAssembly: Assembly, inputEvidence: Evidence) -> Evidence: ...
    
    def ResolvePolicy(self, evidence: Evidence) -> PermissionSet: ...
    
    def get_DomainPolicy(self) -> PolicyLevel: ...
    
    def get_Flags(self) -> HostSecurityManagerOptions: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class HostSecurityManager(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def DomainPolicy(self) -> PolicyLevel: ...
    
    @property
    def Flags(self) -> HostSecurityManagerOptions: ...
    
    # ---------- Methods ---------- #
    
    def DetermineApplicationTrust(self, applicationEvidence: Evidence, activatorEvidence: Evidence, context: TrustManagerContext) -> ApplicationTrust: ...
    
    def GenerateAppDomainEvidence(self, evidenceType: TypeType) -> EvidenceBase: ...
    
    def GenerateAssemblyEvidence(self, evidenceType: TypeType, assembly: Assembly) -> EvidenceBase: ...
    
    def GetHostSuppliedAppDomainEvidenceTypes(self) -> ArrayType[TypeType]: ...
    
    def GetHostSuppliedAssemblyEvidenceTypes(self, assembly: Assembly) -> ArrayType[TypeType]: ...
    
    def ProvideAppDomainEvidence(self, inputEvidence: Evidence) -> Evidence: ...
    
    def ProvideAssemblyEvidence(self, loadedAssembly: Assembly, inputEvidence: Evidence) -> Evidence: ...
    
    def ResolvePolicy(self, evidence: Evidence) -> PermissionSet: ...
    
    def get_DomainPolicy(self) -> PolicyLevel: ...
    
    def get_Flags(self) -> HostSecurityManagerOptions: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class NamedPermissionSet(PermissionSet, ISecurityEncodable, ICollection, IEnumerable, IStackWalk, IDeserializationCallback):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, name: StringType): ...
    
    @overload
    def __init__(self, name: StringType, state: PermissionState): ...
    
    @overload
    def __init__(self, name: StringType, permSet: PermissionSet): ...
    
    @overload
    def __init__(self, permSet: NamedPermissionSet): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Description(self) -> StringType: ...
    
    @Description.setter
    def Description(self, value: StringType) -> None: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @Name.setter
    def Name(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Copy(self) -> PermissionSet: ...
    
    @overload
    def Copy(self, name: StringType) -> NamedPermissionSet: ...
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def FromXml(self, et: SecurityElement) -> VoidType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToXml(self) -> SecurityElement: ...
    
    def get_Description(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    def set_Description(self, value: StringType) -> VoidType: ...
    
    def set_Name(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class NamedPermissionSet(PermissionSet, ISecurityEncodable, ICollection, IEnumerable, IStackWalk, IDeserializationCallback):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, name: StringType): ...
    
    @overload
    def __init__(self, name: StringType, state: PermissionState): ...
    
    @overload
    def __init__(self, name: StringType, permSet: PermissionSet): ...
    
    @overload
    def __init__(self, permSet: NamedPermissionSet): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Description(self) -> StringType: ...
    
    @Description.setter
    def Description(self, value: StringType) -> None: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @Name.setter
    def Name(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Copy(self) -> PermissionSet: ...
    
    @overload
    def Copy(self, name: StringType) -> NamedPermissionSet: ...
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def FromXml(self, et: SecurityElement) -> VoidType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToXml(self) -> SecurityElement: ...
    
    def get_Description(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    def set_Description(self, value: StringType) -> VoidType: ...
    
    def set_Name(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class NamedPermissionSet(PermissionSet, ISecurityEncodable, ICollection, IEnumerable, IStackWalk, IDeserializationCallback):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, name: StringType): ...
    
    @overload
    def __init__(self, name: StringType, state: PermissionState): ...
    
    @overload
    def __init__(self, name: StringType, permSet: PermissionSet): ...
    
    @overload
    def __init__(self, permSet: NamedPermissionSet): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Description(self) -> StringType: ...
    
    @Description.setter
    def Description(self, value: StringType) -> None: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @Name.setter
    def Name(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Copy(self) -> PermissionSet: ...
    
    @overload
    def Copy(self, name: StringType) -> NamedPermissionSet: ...
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def FromXml(self, et: SecurityElement) -> VoidType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToXml(self) -> SecurityElement: ...
    
    def get_Description(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    def set_Description(self, value: StringType) -> VoidType: ...
    
    def set_Name(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PermissionListSet(ObjectType):
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


class PermissionListSet(ObjectType):
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


class PermissionListSet(ObjectType):
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


class PermissionSet(ObjectType, ISecurityEncodable, ICollection, IEnumerable, IStackWalk, IDeserializationCallback):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, state: PermissionState): ...
    
    @overload
    def __init__(self, permSet: PermissionSet): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def IsReadOnly(self) -> BooleanType: ...
    
    @property
    def IsSynchronized(self) -> BooleanType: ...
    
    @property
    def SyncRoot(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def AddPermission(self, perm: IPermission) -> IPermission: ...
    
    def Assert(self) -> VoidType: ...
    
    def ContainsNonCodeAccessPermissions(self) -> BooleanType: ...
    
    @staticmethod
    def ConvertPermissionSet(inFormat: StringType, inData: ArrayType[ByteType], outFormat: StringType) -> ArrayType[ByteType]: ...
    
    def Copy(self) -> PermissionSet: ...
    
    def CopyTo(self, array: Array, index: IntType) -> VoidType: ...
    
    def Demand(self) -> VoidType: ...
    
    def Deny(self) -> VoidType: ...
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def FromXml(self, et: SecurityElement) -> VoidType: ...
    
    def GetEnumerator(self) -> IEnumerator: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def GetPermission(self, permClass: TypeType) -> IPermission: ...
    
    def Intersect(self, other: PermissionSet) -> PermissionSet: ...
    
    def IsEmpty(self) -> BooleanType: ...
    
    def IsSubsetOf(self, target: PermissionSet) -> BooleanType: ...
    
    def IsUnrestricted(self) -> BooleanType: ...
    
    def PermitOnly(self) -> VoidType: ...
    
    def RemovePermission(self, permClass: TypeType) -> IPermission: ...
    
    @staticmethod
    def RevertAssert() -> VoidType: ...
    
    def SetPermission(self, perm: IPermission) -> IPermission: ...
    
    def ToString(self) -> StringType: ...
    
    def ToXml(self) -> SecurityElement: ...
    
    def Union(self, other: PermissionSet) -> PermissionSet: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_IsReadOnly(self) -> BooleanType: ...
    
    def get_IsSynchronized(self) -> BooleanType: ...
    
    def get_SyncRoot(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PermissionSet(ObjectType, ISecurityEncodable, ICollection, IEnumerable, IStackWalk, IDeserializationCallback):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, state: PermissionState): ...
    
    @overload
    def __init__(self, permSet: PermissionSet): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def IsReadOnly(self) -> BooleanType: ...
    
    @property
    def IsSynchronized(self) -> BooleanType: ...
    
    @property
    def SyncRoot(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def AddPermission(self, perm: IPermission) -> IPermission: ...
    
    def Assert(self) -> VoidType: ...
    
    def ContainsNonCodeAccessPermissions(self) -> BooleanType: ...
    
    @staticmethod
    def ConvertPermissionSet(inFormat: StringType, inData: ArrayType[ByteType], outFormat: StringType) -> ArrayType[ByteType]: ...
    
    def Copy(self) -> PermissionSet: ...
    
    def CopyTo(self, array: Array, index: IntType) -> VoidType: ...
    
    def Demand(self) -> VoidType: ...
    
    def Deny(self) -> VoidType: ...
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def FromXml(self, et: SecurityElement) -> VoidType: ...
    
    def GetEnumerator(self) -> IEnumerator: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def GetPermission(self, permClass: TypeType) -> IPermission: ...
    
    def Intersect(self, other: PermissionSet) -> PermissionSet: ...
    
    def IsEmpty(self) -> BooleanType: ...
    
    def IsSubsetOf(self, target: PermissionSet) -> BooleanType: ...
    
    def IsUnrestricted(self) -> BooleanType: ...
    
    def PermitOnly(self) -> VoidType: ...
    
    def RemovePermission(self, permClass: TypeType) -> IPermission: ...
    
    @staticmethod
    def RevertAssert() -> VoidType: ...
    
    def SetPermission(self, perm: IPermission) -> IPermission: ...
    
    def ToString(self) -> StringType: ...
    
    def ToXml(self) -> SecurityElement: ...
    
    def Union(self, other: PermissionSet) -> PermissionSet: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_IsReadOnly(self) -> BooleanType: ...
    
    def get_IsSynchronized(self) -> BooleanType: ...
    
    def get_SyncRoot(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PermissionSet(ObjectType, ISecurityEncodable, ICollection, IEnumerable, IStackWalk, IDeserializationCallback):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, state: PermissionState): ...
    
    @overload
    def __init__(self, permSet: PermissionSet): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def IsReadOnly(self) -> BooleanType: ...
    
    @property
    def IsSynchronized(self) -> BooleanType: ...
    
    @property
    def SyncRoot(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def AddPermission(self, perm: IPermission) -> IPermission: ...
    
    def Assert(self) -> VoidType: ...
    
    def ContainsNonCodeAccessPermissions(self) -> BooleanType: ...
    
    @staticmethod
    def ConvertPermissionSet(inFormat: StringType, inData: ArrayType[ByteType], outFormat: StringType) -> ArrayType[ByteType]: ...
    
    def Copy(self) -> PermissionSet: ...
    
    def CopyTo(self, array: Array, index: IntType) -> VoidType: ...
    
    def Demand(self) -> VoidType: ...
    
    def Deny(self) -> VoidType: ...
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def FromXml(self, et: SecurityElement) -> VoidType: ...
    
    def GetEnumerator(self) -> IEnumerator: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def GetPermission(self, permClass: TypeType) -> IPermission: ...
    
    def Intersect(self, other: PermissionSet) -> PermissionSet: ...
    
    def IsEmpty(self) -> BooleanType: ...
    
    def IsSubsetOf(self, target: PermissionSet) -> BooleanType: ...
    
    def IsUnrestricted(self) -> BooleanType: ...
    
    def PermitOnly(self) -> VoidType: ...
    
    def RemovePermission(self, permClass: TypeType) -> IPermission: ...
    
    @staticmethod
    def RevertAssert() -> VoidType: ...
    
    def SetPermission(self, perm: IPermission) -> IPermission: ...
    
    def ToString(self) -> StringType: ...
    
    def ToXml(self) -> SecurityElement: ...
    
    def Union(self, other: PermissionSet) -> PermissionSet: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_IsReadOnly(self) -> BooleanType: ...
    
    def get_IsSynchronized(self) -> BooleanType: ...
    
    def get_SyncRoot(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PermissionSetEnumerator(ObjectType, IEnumerator):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Current(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def MoveNext(self) -> BooleanType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Current(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PermissionSetEnumerator(ObjectType, IEnumerator):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Current(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def MoveNext(self) -> BooleanType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Current(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PermissionSetEnumerator(ObjectType, IEnumerator):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Current(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def MoveNext(self) -> BooleanType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Current(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PermissionSetTriple(ObjectType):
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


class PermissionSetTriple(ObjectType):
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


class PermissionSetTriple(ObjectType):
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


class PermissionToken(ObjectType, ISecurityEncodable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def FindToken(cls: TypeType) -> PermissionToken: ...
    
    @staticmethod
    def FindTokenByIndex(i: IntType) -> PermissionToken: ...
    
    def FromXml(self, elRoot: SecurityElement) -> VoidType: ...
    
    @staticmethod
    @overload
    def GetToken(cls: TypeType) -> PermissionToken: ...
    
    @staticmethod
    @overload
    def GetToken(perm: IPermission) -> PermissionToken: ...
    
    @staticmethod
    @overload
    def GetToken(typeStr: StringType) -> PermissionToken: ...
    
    @staticmethod
    @overload
    def GetToken(typeStr: StringType, bCreateMscorlib: BooleanType) -> PermissionToken: ...
    
    @staticmethod
    def IsTokenProperlyAssigned(perm: IPermission, token: PermissionToken) -> BooleanType: ...
    
    def ToXml(self) -> SecurityElement: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PermissionToken(ObjectType, ISecurityEncodable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def FindToken(cls: TypeType) -> PermissionToken: ...
    
    @staticmethod
    def FindTokenByIndex(i: IntType) -> PermissionToken: ...
    
    def FromXml(self, elRoot: SecurityElement) -> VoidType: ...
    
    @staticmethod
    @overload
    def GetToken(cls: TypeType) -> PermissionToken: ...
    
    @staticmethod
    @overload
    def GetToken(perm: IPermission) -> PermissionToken: ...
    
    @staticmethod
    @overload
    def GetToken(typeStr: StringType) -> PermissionToken: ...
    
    @staticmethod
    @overload
    def GetToken(typeStr: StringType, bCreateMscorlib: BooleanType) -> PermissionToken: ...
    
    @staticmethod
    def IsTokenProperlyAssigned(perm: IPermission, token: PermissionToken) -> BooleanType: ...
    
    def ToXml(self) -> SecurityElement: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PermissionToken(ObjectType, ISecurityEncodable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def FindToken(cls: TypeType) -> PermissionToken: ...
    
    @staticmethod
    def FindTokenByIndex(i: IntType) -> PermissionToken: ...
    
    def FromXml(self, elRoot: SecurityElement) -> VoidType: ...
    
    @staticmethod
    @overload
    def GetToken(cls: TypeType) -> PermissionToken: ...
    
    @staticmethod
    @overload
    def GetToken(perm: IPermission) -> PermissionToken: ...
    
    @staticmethod
    @overload
    def GetToken(typeStr: StringType) -> PermissionToken: ...
    
    @staticmethod
    @overload
    def GetToken(typeStr: StringType, bCreateMscorlib: BooleanType) -> PermissionToken: ...
    
    @staticmethod
    def IsTokenProperlyAssigned(perm: IPermission, token: PermissionToken) -> BooleanType: ...
    
    def ToXml(self) -> SecurityElement: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PermissionTokenFactory(ObjectType):
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


class PermissionTokenFactory(ObjectType):
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


class PermissionTokenFactory(ObjectType):
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


class PermissionTokenKeyComparer(ObjectType, IEqualityComparer):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Compare(self, a: ObjectType, b: ObjectType) -> IntType: ...
    
    @overload
    def Equals(self, a: ObjectType, b: ObjectType) -> BooleanType: ...
    
    @overload
    def GetHashCode(self, obj: ObjectType) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PermissionTokenKeyComparer(ObjectType, IEqualityComparer):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Compare(self, a: ObjectType, b: ObjectType) -> IntType: ...
    
    @overload
    def Equals(self, a: ObjectType, b: ObjectType) -> BooleanType: ...
    
    @overload
    def GetHashCode(self, obj: ObjectType) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PermissionTokenKeyComparer(ObjectType, IEqualityComparer):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Compare(self, a: ObjectType, b: ObjectType) -> IntType: ...
    
    @overload
    def Equals(self, a: ObjectType, b: ObjectType) -> BooleanType: ...
    
    @overload
    def GetHashCode(self, obj: ObjectType) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PolicyManager(ObjectType):
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


class PolicyManager(ObjectType):
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


class PolicyManager(ObjectType):
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


class ReadOnlyPermissionSet(PermissionSet, ISecurityEncodable, ICollection, IEnumerable, IStackWalk, IDeserializationCallback):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, permissionSetXml: SecurityElement): ...
    
    # ---------- Properties ---------- #
    
    @property
    def IsReadOnly(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def Copy(self) -> PermissionSet: ...
    
    def FromXml(self, et: SecurityElement) -> VoidType: ...
    
    def ToXml(self) -> SecurityElement: ...
    
    def get_IsReadOnly(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ReadOnlyPermissionSet(PermissionSet, ISecurityEncodable, ICollection, IEnumerable, IStackWalk, IDeserializationCallback):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, permissionSetXml: SecurityElement): ...
    
    # ---------- Properties ---------- #
    
    @property
    def IsReadOnly(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def Copy(self) -> PermissionSet: ...
    
    def FromXml(self, et: SecurityElement) -> VoidType: ...
    
    def ToXml(self) -> SecurityElement: ...
    
    def get_IsReadOnly(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ReadOnlyPermissionSet(PermissionSet, ISecurityEncodable, ICollection, IEnumerable, IStackWalk, IDeserializationCallback):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, permissionSetXml: SecurityElement): ...
    
    # ---------- Properties ---------- #
    
    @property
    def IsReadOnly(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def Copy(self) -> PermissionSet: ...
    
    def FromXml(self, et: SecurityElement) -> VoidType: ...
    
    def ToXml(self) -> SecurityElement: ...
    
    def get_IsReadOnly(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ReadOnlyPermissionSetEnumerator(ObjectType, IEnumerator):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Current(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def MoveNext(self) -> BooleanType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Current(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ReadOnlyPermissionSetEnumerator(ObjectType, IEnumerator):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Current(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def MoveNext(self) -> BooleanType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Current(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ReadOnlyPermissionSetEnumerator(ObjectType, IEnumerator):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Current(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def MoveNext(self) -> BooleanType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Current(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SafeBSTRHandle(SafeBuffer, IDisposable):
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


class SafeBSTRHandle(SafeBuffer, IDisposable):
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


class SafeBSTRHandle(SafeBuffer, IDisposable):
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


class SecureString(ObjectType, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: CharType, length: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Length(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def AppendChar(self, c: CharType) -> VoidType: ...
    
    def Clear(self) -> VoidType: ...
    
    def Copy(self) -> SecureString: ...
    
    def Dispose(self) -> VoidType: ...
    
    def InsertAt(self, index: IntType, c: CharType) -> VoidType: ...
    
    def IsReadOnly(self) -> BooleanType: ...
    
    def MakeReadOnly(self) -> VoidType: ...
    
    def RemoveAt(self, index: IntType) -> VoidType: ...
    
    def SetAt(self, index: IntType, c: CharType) -> VoidType: ...
    
    def get_Length(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SecureString(ObjectType, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: CharType, length: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Length(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def AppendChar(self, c: CharType) -> VoidType: ...
    
    def Clear(self) -> VoidType: ...
    
    def Copy(self) -> SecureString: ...
    
    def Dispose(self) -> VoidType: ...
    
    def InsertAt(self, index: IntType, c: CharType) -> VoidType: ...
    
    def IsReadOnly(self) -> BooleanType: ...
    
    def MakeReadOnly(self) -> VoidType: ...
    
    def RemoveAt(self, index: IntType) -> VoidType: ...
    
    def SetAt(self, index: IntType, c: CharType) -> VoidType: ...
    
    def get_Length(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SecureString(ObjectType, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: CharType, length: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Length(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def AppendChar(self, c: CharType) -> VoidType: ...
    
    def Clear(self) -> VoidType: ...
    
    def Copy(self) -> SecureString: ...
    
    def Dispose(self) -> VoidType: ...
    
    def InsertAt(self, index: IntType, c: CharType) -> VoidType: ...
    
    def IsReadOnly(self) -> BooleanType: ...
    
    def MakeReadOnly(self) -> VoidType: ...
    
    def RemoveAt(self, index: IntType) -> VoidType: ...
    
    def SetAt(self, index: IntType, c: CharType) -> VoidType: ...
    
    def get_Length(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SecureStringMarshal(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def SecureStringToCoTaskMemAnsi(s: SecureString) -> NIntType: ...
    
    @staticmethod
    def SecureStringToCoTaskMemUnicode(s: SecureString) -> NIntType: ...
    
    @staticmethod
    def SecureStringToGlobalAllocAnsi(s: SecureString) -> NIntType: ...
    
    @staticmethod
    def SecureStringToGlobalAllocUnicode(s: SecureString) -> NIntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SecurityContext(ObjectType, IDisposable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def Capture() -> SecurityContext: ...
    
    def CreateCopy(self) -> SecurityContext: ...
    
    def Dispose(self) -> VoidType: ...
    
    @staticmethod
    def IsFlowSuppressed() -> BooleanType: ...
    
    @staticmethod
    def IsWindowsIdentityFlowSuppressed() -> BooleanType: ...
    
    @staticmethod
    def RestoreFlow() -> VoidType: ...
    
    @staticmethod
    def Run(securityContext: SecurityContext, callback: ContextCallback, state: ObjectType) -> VoidType: ...
    
    @staticmethod
    def SuppressFlow() -> AsyncFlowControl: ...
    
    @staticmethod
    def SuppressFlowWindowsIdentity() -> AsyncFlowControl: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SecurityContext(ObjectType, IDisposable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def Capture() -> SecurityContext: ...
    
    def CreateCopy(self) -> SecurityContext: ...
    
    def Dispose(self) -> VoidType: ...
    
    @staticmethod
    def IsFlowSuppressed() -> BooleanType: ...
    
    @staticmethod
    def IsWindowsIdentityFlowSuppressed() -> BooleanType: ...
    
    @staticmethod
    def RestoreFlow() -> VoidType: ...
    
    @staticmethod
    def Run(securityContext: SecurityContext, callback: ContextCallback, state: ObjectType) -> VoidType: ...
    
    @staticmethod
    def SuppressFlow() -> AsyncFlowControl: ...
    
    @staticmethod
    def SuppressFlowWindowsIdentity() -> AsyncFlowControl: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SecurityContext(ObjectType, IDisposable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def Capture() -> SecurityContext: ...
    
    def CreateCopy(self) -> SecurityContext: ...
    
    def Dispose(self) -> VoidType: ...
    
    @staticmethod
    def IsFlowSuppressed() -> BooleanType: ...
    
    @staticmethod
    def IsWindowsIdentityFlowSuppressed() -> BooleanType: ...
    
    @staticmethod
    def RestoreFlow() -> VoidType: ...
    
    @staticmethod
    def Run(securityContext: SecurityContext, callback: ContextCallback, state: ObjectType) -> VoidType: ...
    
    @staticmethod
    def SuppressFlow() -> AsyncFlowControl: ...
    
    @staticmethod
    def SuppressFlowWindowsIdentity() -> AsyncFlowControl: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SecurityCriticalAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, scope: SecurityCriticalScope): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Scope(self) -> SecurityCriticalScope: ...
    
    # ---------- Methods ---------- #
    
    def get_Scope(self) -> SecurityCriticalScope: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SecurityCriticalAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, scope: SecurityCriticalScope): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Scope(self) -> SecurityCriticalScope: ...
    
    # ---------- Methods ---------- #
    
    def get_Scope(self) -> SecurityCriticalScope: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SecurityCriticalAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, scope: SecurityCriticalScope): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Scope(self) -> SecurityCriticalScope: ...
    
    # ---------- Methods ---------- #
    
    def get_Scope(self) -> SecurityCriticalScope: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SecurityDocument(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, numData: IntType): ...
    
    @overload
    def __init__(self, data: ArrayType[ByteType]): ...
    
    @overload
    def __init__(self, elRoot: SecurityElement): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def AddString(self, str: StringType, position: IntType) -> Tuple[VoidType, IntType]: ...
    
    def AddToken(self, b: ByteType, position: IntType) -> Tuple[VoidType, IntType]: ...
    
    def AppendString(self, str: StringType, position: IntType) -> Tuple[VoidType, IntType]: ...
    
    def ConvertElement(self, elCurrent: SecurityElement, position: IntType) -> Tuple[VoidType, IntType]: ...
    
    @staticmethod
    def EncodedStringSize(str: StringType) -> IntType: ...
    
    def GetAttributeForElement(self, position: IntType, attributeName: StringType) -> StringType: ...
    
    def GetChildrenPositionForElement(self, position: IntType) -> ArrayList: ...
    
    def GetElement(self, position: IntType, bCreate: BooleanType) -> SecurityElement: ...
    
    def GetRootElement(self) -> SecurityElement: ...
    
    @overload
    def GetString(self, position: IntType) -> Tuple[StringType, IntType]: ...
    
    @overload
    def GetString(self, position: IntType, bCreate: BooleanType) -> Tuple[StringType, IntType]: ...
    
    def GetTagForElement(self, position: IntType) -> StringType: ...
    
    def GuaranteeSize(self, size: IntType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SecurityDocument(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, numData: IntType): ...
    
    @overload
    def __init__(self, data: ArrayType[ByteType]): ...
    
    @overload
    def __init__(self, elRoot: SecurityElement): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def AddString(self, str: StringType, position: IntType) -> Tuple[VoidType, IntType]: ...
    
    def AddToken(self, b: ByteType, position: IntType) -> Tuple[VoidType, IntType]: ...
    
    def AppendString(self, str: StringType, position: IntType) -> Tuple[VoidType, IntType]: ...
    
    def ConvertElement(self, elCurrent: SecurityElement, position: IntType) -> Tuple[VoidType, IntType]: ...
    
    @staticmethod
    def EncodedStringSize(str: StringType) -> IntType: ...
    
    def GetAttributeForElement(self, position: IntType, attributeName: StringType) -> StringType: ...
    
    def GetChildrenPositionForElement(self, position: IntType) -> ArrayList: ...
    
    def GetElement(self, position: IntType, bCreate: BooleanType) -> SecurityElement: ...
    
    def GetRootElement(self) -> SecurityElement: ...
    
    @overload
    def GetString(self, position: IntType) -> Tuple[StringType, IntType]: ...
    
    @overload
    def GetString(self, position: IntType, bCreate: BooleanType) -> Tuple[StringType, IntType]: ...
    
    def GetTagForElement(self, position: IntType) -> StringType: ...
    
    def GuaranteeSize(self, size: IntType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SecurityDocument(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, numData: IntType): ...
    
    @overload
    def __init__(self, data: ArrayType[ByteType]): ...
    
    @overload
    def __init__(self, elRoot: SecurityElement): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def AddString(self, str: StringType, position: IntType) -> Tuple[VoidType, IntType]: ...
    
    def AddToken(self, b: ByteType, position: IntType) -> Tuple[VoidType, IntType]: ...
    
    def AppendString(self, str: StringType, position: IntType) -> Tuple[VoidType, IntType]: ...
    
    def ConvertElement(self, elCurrent: SecurityElement, position: IntType) -> Tuple[VoidType, IntType]: ...
    
    @staticmethod
    def EncodedStringSize(str: StringType) -> IntType: ...
    
    def GetAttributeForElement(self, position: IntType, attributeName: StringType) -> StringType: ...
    
    def GetChildrenPositionForElement(self, position: IntType) -> ArrayList: ...
    
    def GetElement(self, position: IntType, bCreate: BooleanType) -> SecurityElement: ...
    
    def GetRootElement(self) -> SecurityElement: ...
    
    @overload
    def GetString(self, position: IntType) -> Tuple[StringType, IntType]: ...
    
    @overload
    def GetString(self, position: IntType, bCreate: BooleanType) -> Tuple[StringType, IntType]: ...
    
    def GetTagForElement(self, position: IntType) -> StringType: ...
    
    def GuaranteeSize(self, size: IntType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SecurityDocumentElement(ObjectType, ISecurityElementFactory):
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


class SecurityDocumentElement(ObjectType, ISecurityElementFactory):
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


class SecurityDocumentElement(ObjectType, ISecurityElementFactory):
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


class SecurityElement(ObjectType, ISecurityElementFactory):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, tag: StringType): ...
    
    @overload
    def __init__(self, tag: StringType, text: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Attributes(self) -> Hashtable: ...
    
    @Attributes.setter
    def Attributes(self, value: Hashtable) -> None: ...
    
    @property
    def Children(self) -> ArrayList: ...
    
    @Children.setter
    def Children(self, value: ArrayList) -> None: ...
    
    @property
    def Tag(self) -> StringType: ...
    
    @Tag.setter
    def Tag(self, value: StringType) -> None: ...
    
    @property
    def Text(self) -> StringType: ...
    
    @Text.setter
    def Text(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def AddAttribute(self, name: StringType, value: StringType) -> VoidType: ...
    
    def AddChild(self, child: SecurityElement) -> VoidType: ...
    
    def Attribute(self, name: StringType) -> StringType: ...
    
    def Copy(self) -> SecurityElement: ...
    
    def Equal(self, other: SecurityElement) -> BooleanType: ...
    
    @staticmethod
    def Escape(str: StringType) -> StringType: ...
    
    @staticmethod
    def FromString(xml: StringType) -> SecurityElement: ...
    
    @staticmethod
    def IsValidAttributeName(name: StringType) -> BooleanType: ...
    
    @staticmethod
    def IsValidAttributeValue(value: StringType) -> BooleanType: ...
    
    @staticmethod
    def IsValidTag(tag: StringType) -> BooleanType: ...
    
    @staticmethod
    def IsValidText(text: StringType) -> BooleanType: ...
    
    def SearchForChildByTag(self, tag: StringType) -> SecurityElement: ...
    
    def SearchForTextOfTag(self, tag: StringType) -> StringType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Attributes(self) -> Hashtable: ...
    
    def get_Children(self) -> ArrayList: ...
    
    def get_Tag(self) -> StringType: ...
    
    def get_Text(self) -> StringType: ...
    
    def set_Attributes(self, value: Hashtable) -> VoidType: ...
    
    def set_Children(self, value: ArrayList) -> VoidType: ...
    
    def set_Tag(self, value: StringType) -> VoidType: ...
    
    def set_Text(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SecurityElement(ObjectType, ISecurityElementFactory):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, tag: StringType): ...
    
    @overload
    def __init__(self, tag: StringType, text: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Attributes(self) -> Hashtable: ...
    
    @Attributes.setter
    def Attributes(self, value: Hashtable) -> None: ...
    
    @property
    def Children(self) -> ArrayList: ...
    
    @Children.setter
    def Children(self, value: ArrayList) -> None: ...
    
    @property
    def Tag(self) -> StringType: ...
    
    @Tag.setter
    def Tag(self, value: StringType) -> None: ...
    
    @property
    def Text(self) -> StringType: ...
    
    @Text.setter
    def Text(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def AddAttribute(self, name: StringType, value: StringType) -> VoidType: ...
    
    def AddChild(self, child: SecurityElement) -> VoidType: ...
    
    def Attribute(self, name: StringType) -> StringType: ...
    
    def Copy(self) -> SecurityElement: ...
    
    def Equal(self, other: SecurityElement) -> BooleanType: ...
    
    @staticmethod
    def Escape(str: StringType) -> StringType: ...
    
    @staticmethod
    def FromString(xml: StringType) -> SecurityElement: ...
    
    @staticmethod
    def IsValidAttributeName(name: StringType) -> BooleanType: ...
    
    @staticmethod
    def IsValidAttributeValue(value: StringType) -> BooleanType: ...
    
    @staticmethod
    def IsValidTag(tag: StringType) -> BooleanType: ...
    
    @staticmethod
    def IsValidText(text: StringType) -> BooleanType: ...
    
    def SearchForChildByTag(self, tag: StringType) -> SecurityElement: ...
    
    def SearchForTextOfTag(self, tag: StringType) -> StringType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Attributes(self) -> Hashtable: ...
    
    def get_Children(self) -> ArrayList: ...
    
    def get_Tag(self) -> StringType: ...
    
    def get_Text(self) -> StringType: ...
    
    def set_Attributes(self, value: Hashtable) -> VoidType: ...
    
    def set_Children(self, value: ArrayList) -> VoidType: ...
    
    def set_Tag(self, value: StringType) -> VoidType: ...
    
    def set_Text(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SecurityElement(ObjectType, ISecurityElementFactory):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, tag: StringType): ...
    
    @overload
    def __init__(self, tag: StringType, text: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Attributes(self) -> Hashtable: ...
    
    @Attributes.setter
    def Attributes(self, value: Hashtable) -> None: ...
    
    @property
    def Children(self) -> ArrayList: ...
    
    @Children.setter
    def Children(self, value: ArrayList) -> None: ...
    
    @property
    def Tag(self) -> StringType: ...
    
    @Tag.setter
    def Tag(self, value: StringType) -> None: ...
    
    @property
    def Text(self) -> StringType: ...
    
    @Text.setter
    def Text(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def AddAttribute(self, name: StringType, value: StringType) -> VoidType: ...
    
    def AddChild(self, child: SecurityElement) -> VoidType: ...
    
    def Attribute(self, name: StringType) -> StringType: ...
    
    def Copy(self) -> SecurityElement: ...
    
    def Equal(self, other: SecurityElement) -> BooleanType: ...
    
    @staticmethod
    def Escape(str: StringType) -> StringType: ...
    
    @staticmethod
    def FromString(xml: StringType) -> SecurityElement: ...
    
    @staticmethod
    def IsValidAttributeName(name: StringType) -> BooleanType: ...
    
    @staticmethod
    def IsValidAttributeValue(value: StringType) -> BooleanType: ...
    
    @staticmethod
    def IsValidTag(tag: StringType) -> BooleanType: ...
    
    @staticmethod
    def IsValidText(text: StringType) -> BooleanType: ...
    
    def SearchForChildByTag(self, tag: StringType) -> SecurityElement: ...
    
    def SearchForTextOfTag(self, tag: StringType) -> StringType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Attributes(self) -> Hashtable: ...
    
    def get_Children(self) -> ArrayList: ...
    
    def get_Tag(self) -> StringType: ...
    
    def get_Text(self) -> StringType: ...
    
    def set_Attributes(self, value: Hashtable) -> VoidType: ...
    
    def set_Children(self, value: ArrayList) -> VoidType: ...
    
    def set_Tag(self, value: StringType) -> VoidType: ...
    
    def set_Text(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SecurityException(SystemException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, type: TypeType): ...
    
    @overload
    def __init__(self, message: StringType, type: TypeType, state: StringType): ...
    
    @overload
    def __init__(self, message: StringType, inner: Exception): ...
    
    @overload
    def __init__(self, message: StringType, assemblyName: AssemblyName, grant: PermissionSet, refused: PermissionSet, method: MethodInfo, action: SecurityAction, demanded: ObjectType, permThatFailed: IPermission, evidence: Evidence): ...
    
    @overload
    def __init__(self, message: StringType, deny: ObjectType, permitOnly: ObjectType, method: MethodInfo, demanded: ObjectType, permThatFailed: IPermission): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Action(self) -> SecurityAction: ...
    
    @Action.setter
    def Action(self, value: SecurityAction) -> None: ...
    
    @property
    def Demanded(self) -> ObjectType: ...
    
    @Demanded.setter
    def Demanded(self, value: ObjectType) -> None: ...
    
    @property
    def DenySetInstance(self) -> ObjectType: ...
    
    @DenySetInstance.setter
    def DenySetInstance(self, value: ObjectType) -> None: ...
    
    @property
    def FailedAssemblyInfo(self) -> AssemblyName: ...
    
    @FailedAssemblyInfo.setter
    def FailedAssemblyInfo(self, value: AssemblyName) -> None: ...
    
    @property
    def FirstPermissionThatFailed(self) -> IPermission: ...
    
    @FirstPermissionThatFailed.setter
    def FirstPermissionThatFailed(self, value: IPermission) -> None: ...
    
    @property
    def GrantedSet(self) -> StringType: ...
    
    @GrantedSet.setter
    def GrantedSet(self, value: StringType) -> None: ...
    
    @property
    def Method(self) -> MethodInfo: ...
    
    @Method.setter
    def Method(self, value: MethodInfo) -> None: ...
    
    @property
    def PermissionState(self) -> StringType: ...
    
    @PermissionState.setter
    def PermissionState(self, value: StringType) -> None: ...
    
    @property
    def PermissionType(self) -> TypeType: ...
    
    @PermissionType.setter
    def PermissionType(self, value: TypeType) -> None: ...
    
    @property
    def PermitOnlySetInstance(self) -> ObjectType: ...
    
    @PermitOnlySetInstance.setter
    def PermitOnlySetInstance(self, value: ObjectType) -> None: ...
    
    @property
    def RefusedSet(self) -> StringType: ...
    
    @RefusedSet.setter
    def RefusedSet(self, value: StringType) -> None: ...
    
    @property
    def Url(self) -> StringType: ...
    
    @Url.setter
    def Url(self, value: StringType) -> None: ...
    
    @property
    def Zone(self) -> SecurityZone: ...
    
    @Zone.setter
    def Zone(self, value: SecurityZone) -> None: ...
    
    # ---------- Methods ---------- #
    
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Action(self) -> SecurityAction: ...
    
    def get_Demanded(self) -> ObjectType: ...
    
    def get_DenySetInstance(self) -> ObjectType: ...
    
    def get_FailedAssemblyInfo(self) -> AssemblyName: ...
    
    def get_FirstPermissionThatFailed(self) -> IPermission: ...
    
    def get_GrantedSet(self) -> StringType: ...
    
    def get_Method(self) -> MethodInfo: ...
    
    def get_PermissionState(self) -> StringType: ...
    
    def get_PermissionType(self) -> TypeType: ...
    
    def get_PermitOnlySetInstance(self) -> ObjectType: ...
    
    def get_RefusedSet(self) -> StringType: ...
    
    def get_Url(self) -> StringType: ...
    
    def get_Zone(self) -> SecurityZone: ...
    
    def set_Action(self, value: SecurityAction) -> VoidType: ...
    
    def set_Demanded(self, value: ObjectType) -> VoidType: ...
    
    def set_DenySetInstance(self, value: ObjectType) -> VoidType: ...
    
    def set_FailedAssemblyInfo(self, value: AssemblyName) -> VoidType: ...
    
    def set_FirstPermissionThatFailed(self, value: IPermission) -> VoidType: ...
    
    def set_GrantedSet(self, value: StringType) -> VoidType: ...
    
    def set_Method(self, value: MethodInfo) -> VoidType: ...
    
    def set_PermissionState(self, value: StringType) -> VoidType: ...
    
    def set_PermissionType(self, value: TypeType) -> VoidType: ...
    
    def set_PermitOnlySetInstance(self, value: ObjectType) -> VoidType: ...
    
    def set_RefusedSet(self, value: StringType) -> VoidType: ...
    
    def set_Url(self, value: StringType) -> VoidType: ...
    
    def set_Zone(self, value: SecurityZone) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SecurityException(SystemException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, type: TypeType): ...
    
    @overload
    def __init__(self, message: StringType, type: TypeType, state: StringType): ...
    
    @overload
    def __init__(self, message: StringType, inner: Exception): ...
    
    @overload
    def __init__(self, message: StringType, assemblyName: AssemblyName, grant: PermissionSet, refused: PermissionSet, method: MethodInfo, action: SecurityAction, demanded: ObjectType, permThatFailed: IPermission, evidence: Evidence): ...
    
    @overload
    def __init__(self, message: StringType, deny: ObjectType, permitOnly: ObjectType, method: MethodInfo, demanded: ObjectType, permThatFailed: IPermission): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Action(self) -> SecurityAction: ...
    
    @Action.setter
    def Action(self, value: SecurityAction) -> None: ...
    
    @property
    def Demanded(self) -> ObjectType: ...
    
    @Demanded.setter
    def Demanded(self, value: ObjectType) -> None: ...
    
    @property
    def DenySetInstance(self) -> ObjectType: ...
    
    @DenySetInstance.setter
    def DenySetInstance(self, value: ObjectType) -> None: ...
    
    @property
    def FailedAssemblyInfo(self) -> AssemblyName: ...
    
    @FailedAssemblyInfo.setter
    def FailedAssemblyInfo(self, value: AssemblyName) -> None: ...
    
    @property
    def FirstPermissionThatFailed(self) -> IPermission: ...
    
    @FirstPermissionThatFailed.setter
    def FirstPermissionThatFailed(self, value: IPermission) -> None: ...
    
    @property
    def GrantedSet(self) -> StringType: ...
    
    @GrantedSet.setter
    def GrantedSet(self, value: StringType) -> None: ...
    
    @property
    def Method(self) -> MethodInfo: ...
    
    @Method.setter
    def Method(self, value: MethodInfo) -> None: ...
    
    @property
    def PermissionState(self) -> StringType: ...
    
    @PermissionState.setter
    def PermissionState(self, value: StringType) -> None: ...
    
    @property
    def PermissionType(self) -> TypeType: ...
    
    @PermissionType.setter
    def PermissionType(self, value: TypeType) -> None: ...
    
    @property
    def PermitOnlySetInstance(self) -> ObjectType: ...
    
    @PermitOnlySetInstance.setter
    def PermitOnlySetInstance(self, value: ObjectType) -> None: ...
    
    @property
    def RefusedSet(self) -> StringType: ...
    
    @RefusedSet.setter
    def RefusedSet(self, value: StringType) -> None: ...
    
    @property
    def Url(self) -> StringType: ...
    
    @Url.setter
    def Url(self, value: StringType) -> None: ...
    
    @property
    def Zone(self) -> SecurityZone: ...
    
    @Zone.setter
    def Zone(self, value: SecurityZone) -> None: ...
    
    # ---------- Methods ---------- #
    
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Action(self) -> SecurityAction: ...
    
    def get_Demanded(self) -> ObjectType: ...
    
    def get_DenySetInstance(self) -> ObjectType: ...
    
    def get_FailedAssemblyInfo(self) -> AssemblyName: ...
    
    def get_FirstPermissionThatFailed(self) -> IPermission: ...
    
    def get_GrantedSet(self) -> StringType: ...
    
    def get_Method(self) -> MethodInfo: ...
    
    def get_PermissionState(self) -> StringType: ...
    
    def get_PermissionType(self) -> TypeType: ...
    
    def get_PermitOnlySetInstance(self) -> ObjectType: ...
    
    def get_RefusedSet(self) -> StringType: ...
    
    def get_Url(self) -> StringType: ...
    
    def get_Zone(self) -> SecurityZone: ...
    
    def set_Action(self, value: SecurityAction) -> VoidType: ...
    
    def set_Demanded(self, value: ObjectType) -> VoidType: ...
    
    def set_DenySetInstance(self, value: ObjectType) -> VoidType: ...
    
    def set_FailedAssemblyInfo(self, value: AssemblyName) -> VoidType: ...
    
    def set_FirstPermissionThatFailed(self, value: IPermission) -> VoidType: ...
    
    def set_GrantedSet(self, value: StringType) -> VoidType: ...
    
    def set_Method(self, value: MethodInfo) -> VoidType: ...
    
    def set_PermissionState(self, value: StringType) -> VoidType: ...
    
    def set_PermissionType(self, value: TypeType) -> VoidType: ...
    
    def set_PermitOnlySetInstance(self, value: ObjectType) -> VoidType: ...
    
    def set_RefusedSet(self, value: StringType) -> VoidType: ...
    
    def set_Url(self, value: StringType) -> VoidType: ...
    
    def set_Zone(self, value: SecurityZone) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SecurityException(SystemException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, type: TypeType): ...
    
    @overload
    def __init__(self, message: StringType, type: TypeType, state: StringType): ...
    
    @overload
    def __init__(self, message: StringType, inner: Exception): ...
    
    @overload
    def __init__(self, message: StringType, assemblyName: AssemblyName, grant: PermissionSet, refused: PermissionSet, method: MethodInfo, action: SecurityAction, demanded: ObjectType, permThatFailed: IPermission, evidence: Evidence): ...
    
    @overload
    def __init__(self, message: StringType, deny: ObjectType, permitOnly: ObjectType, method: MethodInfo, demanded: ObjectType, permThatFailed: IPermission): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Action(self) -> SecurityAction: ...
    
    @Action.setter
    def Action(self, value: SecurityAction) -> None: ...
    
    @property
    def Demanded(self) -> ObjectType: ...
    
    @Demanded.setter
    def Demanded(self, value: ObjectType) -> None: ...
    
    @property
    def DenySetInstance(self) -> ObjectType: ...
    
    @DenySetInstance.setter
    def DenySetInstance(self, value: ObjectType) -> None: ...
    
    @property
    def FailedAssemblyInfo(self) -> AssemblyName: ...
    
    @FailedAssemblyInfo.setter
    def FailedAssemblyInfo(self, value: AssemblyName) -> None: ...
    
    @property
    def FirstPermissionThatFailed(self) -> IPermission: ...
    
    @FirstPermissionThatFailed.setter
    def FirstPermissionThatFailed(self, value: IPermission) -> None: ...
    
    @property
    def GrantedSet(self) -> StringType: ...
    
    @GrantedSet.setter
    def GrantedSet(self, value: StringType) -> None: ...
    
    @property
    def Method(self) -> MethodInfo: ...
    
    @Method.setter
    def Method(self, value: MethodInfo) -> None: ...
    
    @property
    def PermissionState(self) -> StringType: ...
    
    @PermissionState.setter
    def PermissionState(self, value: StringType) -> None: ...
    
    @property
    def PermissionType(self) -> TypeType: ...
    
    @PermissionType.setter
    def PermissionType(self, value: TypeType) -> None: ...
    
    @property
    def PermitOnlySetInstance(self) -> ObjectType: ...
    
    @PermitOnlySetInstance.setter
    def PermitOnlySetInstance(self, value: ObjectType) -> None: ...
    
    @property
    def RefusedSet(self) -> StringType: ...
    
    @RefusedSet.setter
    def RefusedSet(self, value: StringType) -> None: ...
    
    @property
    def Url(self) -> StringType: ...
    
    @Url.setter
    def Url(self, value: StringType) -> None: ...
    
    @property
    def Zone(self) -> SecurityZone: ...
    
    @Zone.setter
    def Zone(self, value: SecurityZone) -> None: ...
    
    # ---------- Methods ---------- #
    
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Action(self) -> SecurityAction: ...
    
    def get_Demanded(self) -> ObjectType: ...
    
    def get_DenySetInstance(self) -> ObjectType: ...
    
    def get_FailedAssemblyInfo(self) -> AssemblyName: ...
    
    def get_FirstPermissionThatFailed(self) -> IPermission: ...
    
    def get_GrantedSet(self) -> StringType: ...
    
    def get_Method(self) -> MethodInfo: ...
    
    def get_PermissionState(self) -> StringType: ...
    
    def get_PermissionType(self) -> TypeType: ...
    
    def get_PermitOnlySetInstance(self) -> ObjectType: ...
    
    def get_RefusedSet(self) -> StringType: ...
    
    def get_Url(self) -> StringType: ...
    
    def get_Zone(self) -> SecurityZone: ...
    
    def set_Action(self, value: SecurityAction) -> VoidType: ...
    
    def set_Demanded(self, value: ObjectType) -> VoidType: ...
    
    def set_DenySetInstance(self, value: ObjectType) -> VoidType: ...
    
    def set_FailedAssemblyInfo(self, value: AssemblyName) -> VoidType: ...
    
    def set_FirstPermissionThatFailed(self, value: IPermission) -> VoidType: ...
    
    def set_GrantedSet(self, value: StringType) -> VoidType: ...
    
    def set_Method(self, value: MethodInfo) -> VoidType: ...
    
    def set_PermissionState(self, value: StringType) -> VoidType: ...
    
    def set_PermissionType(self, value: TypeType) -> VoidType: ...
    
    def set_PermitOnlySetInstance(self, value: ObjectType) -> VoidType: ...
    
    def set_RefusedSet(self, value: StringType) -> VoidType: ...
    
    def set_Url(self, value: StringType) -> VoidType: ...
    
    def set_Zone(self, value: SecurityZone) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SecurityManager(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def CheckExecutionRights() -> BooleanType: ...
    
    @staticmethod
    @CheckExecutionRights.setter
    def CheckExecutionRights(value: BooleanType) -> None: ...
    
    @staticmethod
    @property
    def SecurityEnabled() -> BooleanType: ...
    
    @staticmethod
    @SecurityEnabled.setter
    def SecurityEnabled(value: BooleanType) -> None: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def CurrentThreadRequiresSecurityContextCapture() -> BooleanType: ...
    
    @staticmethod
    def GetStandardSandbox(evidence: Evidence) -> PermissionSet: ...
    
    @staticmethod
    def GetZoneAndOrigin(zone: ArrayList, origin: ArrayList) -> Tuple[VoidType, ArrayList, ArrayList]: ...
    
    @staticmethod
    def IsGranted(perm: IPermission) -> BooleanType: ...
    
    @staticmethod
    def LoadPolicyLevelFromFile(path: StringType, type: PolicyLevelType) -> PolicyLevel: ...
    
    @staticmethod
    def LoadPolicyLevelFromString(str: StringType, type: PolicyLevelType) -> PolicyLevel: ...
    
    @staticmethod
    def PolicyHierarchy() -> IEnumerator: ...
    
    @staticmethod
    @overload
    def ResolvePolicy(evidence: Evidence, reqdPset: PermissionSet, optPset: PermissionSet, denyPset: PermissionSet, denied: PermissionSet) -> Tuple[PermissionSet, PermissionSet]: ...
    
    @staticmethod
    @overload
    def ResolvePolicy(evidence: Evidence) -> PermissionSet: ...
    
    @staticmethod
    @overload
    def ResolvePolicy(evidences: ArrayType[Evidence]) -> PermissionSet: ...
    
    @staticmethod
    def ResolvePolicyGroups(evidence: Evidence) -> IEnumerator: ...
    
    @staticmethod
    def ResolveSystemPolicy(evidence: Evidence) -> PermissionSet: ...
    
    @staticmethod
    def SavePolicy() -> VoidType: ...
    
    @staticmethod
    def SavePolicyLevel(level: PolicyLevel) -> VoidType: ...
    
    @staticmethod
    def get_CheckExecutionRights() -> BooleanType: ...
    
    @staticmethod
    def get_SecurityEnabled() -> BooleanType: ...
    
    @staticmethod
    def set_CheckExecutionRights(value: BooleanType) -> VoidType: ...
    
    @staticmethod
    def set_SecurityEnabled(value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SecurityManager(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def CheckExecutionRights() -> BooleanType: ...
    
    @staticmethod
    @CheckExecutionRights.setter
    def CheckExecutionRights(value: BooleanType) -> None: ...
    
    @staticmethod
    @property
    def SecurityEnabled() -> BooleanType: ...
    
    @staticmethod
    @SecurityEnabled.setter
    def SecurityEnabled(value: BooleanType) -> None: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def CurrentThreadRequiresSecurityContextCapture() -> BooleanType: ...
    
    @staticmethod
    def GetStandardSandbox(evidence: Evidence) -> PermissionSet: ...
    
    @staticmethod
    def GetZoneAndOrigin(zone: ArrayList, origin: ArrayList) -> Tuple[VoidType, ArrayList, ArrayList]: ...
    
    @staticmethod
    def IsGranted(perm: IPermission) -> BooleanType: ...
    
    @staticmethod
    def LoadPolicyLevelFromFile(path: StringType, type: PolicyLevelType) -> PolicyLevel: ...
    
    @staticmethod
    def LoadPolicyLevelFromString(str: StringType, type: PolicyLevelType) -> PolicyLevel: ...
    
    @staticmethod
    def PolicyHierarchy() -> IEnumerator: ...
    
    @staticmethod
    @overload
    def ResolvePolicy(evidence: Evidence, reqdPset: PermissionSet, optPset: PermissionSet, denyPset: PermissionSet, denied: PermissionSet) -> Tuple[PermissionSet, PermissionSet]: ...
    
    @staticmethod
    @overload
    def ResolvePolicy(evidence: Evidence) -> PermissionSet: ...
    
    @staticmethod
    @overload
    def ResolvePolicy(evidences: ArrayType[Evidence]) -> PermissionSet: ...
    
    @staticmethod
    def ResolvePolicyGroups(evidence: Evidence) -> IEnumerator: ...
    
    @staticmethod
    def ResolveSystemPolicy(evidence: Evidence) -> PermissionSet: ...
    
    @staticmethod
    def SavePolicy() -> VoidType: ...
    
    @staticmethod
    def SavePolicyLevel(level: PolicyLevel) -> VoidType: ...
    
    @staticmethod
    def get_CheckExecutionRights() -> BooleanType: ...
    
    @staticmethod
    def get_SecurityEnabled() -> BooleanType: ...
    
    @staticmethod
    def set_CheckExecutionRights(value: BooleanType) -> VoidType: ...
    
    @staticmethod
    def set_SecurityEnabled(value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SecurityManager(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def CheckExecutionRights() -> BooleanType: ...
    
    @staticmethod
    @CheckExecutionRights.setter
    def CheckExecutionRights(value: BooleanType) -> None: ...
    
    @staticmethod
    @property
    def SecurityEnabled() -> BooleanType: ...
    
    @staticmethod
    @SecurityEnabled.setter
    def SecurityEnabled(value: BooleanType) -> None: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def CurrentThreadRequiresSecurityContextCapture() -> BooleanType: ...
    
    @staticmethod
    def GetStandardSandbox(evidence: Evidence) -> PermissionSet: ...
    
    @staticmethod
    def GetZoneAndOrigin(zone: ArrayList, origin: ArrayList) -> Tuple[VoidType, ArrayList, ArrayList]: ...
    
    @staticmethod
    def IsGranted(perm: IPermission) -> BooleanType: ...
    
    @staticmethod
    def LoadPolicyLevelFromFile(path: StringType, type: PolicyLevelType) -> PolicyLevel: ...
    
    @staticmethod
    def LoadPolicyLevelFromString(str: StringType, type: PolicyLevelType) -> PolicyLevel: ...
    
    @staticmethod
    def PolicyHierarchy() -> IEnumerator: ...
    
    @staticmethod
    @overload
    def ResolvePolicy(evidence: Evidence, reqdPset: PermissionSet, optPset: PermissionSet, denyPset: PermissionSet, denied: PermissionSet) -> Tuple[PermissionSet, PermissionSet]: ...
    
    @staticmethod
    @overload
    def ResolvePolicy(evidence: Evidence) -> PermissionSet: ...
    
    @staticmethod
    @overload
    def ResolvePolicy(evidences: ArrayType[Evidence]) -> PermissionSet: ...
    
    @staticmethod
    def ResolvePolicyGroups(evidence: Evidence) -> IEnumerator: ...
    
    @staticmethod
    def ResolveSystemPolicy(evidence: Evidence) -> PermissionSet: ...
    
    @staticmethod
    def SavePolicy() -> VoidType: ...
    
    @staticmethod
    def SavePolicyLevel(level: PolicyLevel) -> VoidType: ...
    
    @staticmethod
    def get_CheckExecutionRights() -> BooleanType: ...
    
    @staticmethod
    def get_SecurityEnabled() -> BooleanType: ...
    
    @staticmethod
    def set_CheckExecutionRights(value: BooleanType) -> VoidType: ...
    
    @staticmethod
    def set_SecurityEnabled(value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SecurityResources(ABC, ObjectType):
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


class SecurityRulesAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, ruleSet: SecurityRuleSet): ...
    
    # ---------- Properties ---------- #
    
    @property
    def RuleSet(self) -> SecurityRuleSet: ...
    
    @property
    def SkipVerificationInFullTrust(self) -> BooleanType: ...
    
    @SkipVerificationInFullTrust.setter
    def SkipVerificationInFullTrust(self, value: BooleanType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_RuleSet(self) -> SecurityRuleSet: ...
    
    def get_SkipVerificationInFullTrust(self) -> BooleanType: ...
    
    def set_SkipVerificationInFullTrust(self, value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SecurityRulesAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, ruleSet: SecurityRuleSet): ...
    
    # ---------- Properties ---------- #
    
    @property
    def RuleSet(self) -> SecurityRuleSet: ...
    
    @property
    def SkipVerificationInFullTrust(self) -> BooleanType: ...
    
    @SkipVerificationInFullTrust.setter
    def SkipVerificationInFullTrust(self, value: BooleanType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_RuleSet(self) -> SecurityRuleSet: ...
    
    def get_SkipVerificationInFullTrust(self) -> BooleanType: ...
    
    def set_SkipVerificationInFullTrust(self, value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SecurityRulesAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, ruleSet: SecurityRuleSet): ...
    
    # ---------- Properties ---------- #
    
    @property
    def RuleSet(self) -> SecurityRuleSet: ...
    
    @property
    def SkipVerificationInFullTrust(self) -> BooleanType: ...
    
    @SkipVerificationInFullTrust.setter
    def SkipVerificationInFullTrust(self, value: BooleanType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_RuleSet(self) -> SecurityRuleSet: ...
    
    def get_SkipVerificationInFullTrust(self) -> BooleanType: ...
    
    def set_SkipVerificationInFullTrust(self, value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SecurityRuntime(ObjectType):
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


class SecurityRuntime(ObjectType):
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


class SecurityRuntime(ObjectType):
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


class SecuritySafeCriticalAttribute(Attribute, _Attribute):
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


class SecuritySafeCriticalAttribute(Attribute, _Attribute):
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


class SecuritySafeCriticalAttribute(Attribute, _Attribute):
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


class SecurityState(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def EnsureState(self) -> VoidType: ...
    
    def IsStateAvailable(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SecurityState(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def EnsureState(self) -> VoidType: ...
    
    def IsStateAvailable(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SecurityState(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def EnsureState(self) -> VoidType: ...
    
    def IsStateAvailable(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SecurityTransparentAttribute(Attribute, _Attribute):
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


class SecurityTransparentAttribute(Attribute, _Attribute):
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


class SecurityTransparentAttribute(Attribute, _Attribute):
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


class SecurityTreatAsSafeAttribute(Attribute, _Attribute):
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


class SecurityTreatAsSafeAttribute(Attribute, _Attribute):
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


class SecurityTreatAsSafeAttribute(Attribute, _Attribute):
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


class SuppressUnmanagedCodeSecurityAttribute(Attribute, _Attribute):
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


class SuppressUnmanagedCodeSecurityAttribute(Attribute, _Attribute):
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


class SuppressUnmanagedCodeSecurityAttribute(Attribute, _Attribute):
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


class UnverifiableCodeAttribute(Attribute, _Attribute):
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


class UnverifiableCodeAttribute(Attribute, _Attribute):
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


class UnverifiableCodeAttribute(Attribute, _Attribute):
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


class VerificationException(SystemException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class VerificationException(SystemException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class VerificationException(SystemException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSyntaxException(SystemException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, inner: Exception): ...
    
    @overload
    def __init__(self, lineNumber: IntType): ...
    
    @overload
    def __init__(self, lineNumber: IntType, message: StringType): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSyntaxException(SystemException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, inner: Exception): ...
    
    @overload
    def __init__(self, lineNumber: IntType): ...
    
    @overload
    def __init__(self, lineNumber: IntType, message: StringType): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSyntaxException(SystemException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, inner: Exception): ...
    
    @overload
    def __init__(self, lineNumber: IntType): ...
    
    @overload
    def __init__(self, lineNumber: IntType, message: StringType): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# ---------- Structs ---------- #

class PermissionSetEnumeratorInternal(ValueType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Current(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def GetCurrentIndex(self) -> IntType: ...
    
    def MoveNext(self) -> BooleanType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Current(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PermissionSetEnumeratorInternal(ValueType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Current(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def GetCurrentIndex(self) -> IntType: ...
    
    def MoveNext(self) -> BooleanType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Current(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PermissionSetEnumeratorInternal(ValueType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Current(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def GetCurrentIndex(self) -> IntType: ...
    
    def MoveNext(self) -> BooleanType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Current(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SecurityContextSwitcher(ValueType, IDisposable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Dispose(self) -> VoidType: ...
    
    def Undo(self) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SecurityContextSwitcher(ValueType, IDisposable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Dispose(self) -> VoidType: ...
    
    def Undo(self) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SecurityContextSwitcher(ValueType, IDisposable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Dispose(self) -> VoidType: ...
    
    def Undo(self) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# ---------- Interfaces ---------- #

class IEvidenceFactory(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def Evidence(self) -> Evidence: ...
    
    # ---------- Methods ---------- #
    
    def get_Evidence(self) -> Evidence: ...
    
    # No Events


class IEvidenceFactory(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def Evidence(self) -> Evidence: ...
    
    # ---------- Methods ---------- #
    
    def get_Evidence(self) -> Evidence: ...
    
    # No Events


class IEvidenceFactory(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def Evidence(self) -> Evidence: ...
    
    # ---------- Methods ---------- #
    
    def get_Evidence(self) -> Evidence: ...
    
    # No Events


class IPermission(Protocol, ISecurityEncodable):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Copy(self) -> IPermission: ...
    
    def Demand(self) -> VoidType: ...
    
    def Intersect(self, target: IPermission) -> IPermission: ...
    
    def IsSubsetOf(self, target: IPermission) -> BooleanType: ...
    
    def Union(self, target: IPermission) -> IPermission: ...
    
    # No Events


class IPermission(Protocol, ISecurityEncodable):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Copy(self) -> IPermission: ...
    
    def Demand(self) -> VoidType: ...
    
    def Intersect(self, target: IPermission) -> IPermission: ...
    
    def IsSubsetOf(self, target: IPermission) -> BooleanType: ...
    
    def Union(self, target: IPermission) -> IPermission: ...
    
    # No Events


class IPermission(Protocol, ISecurityEncodable):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Copy(self) -> IPermission: ...
    
    def Demand(self) -> VoidType: ...
    
    def Intersect(self, target: IPermission) -> IPermission: ...
    
    def IsSubsetOf(self, target: IPermission) -> BooleanType: ...
    
    def Union(self, target: IPermission) -> IPermission: ...
    
    # No Events


class ISecurityElementFactory(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Attribute(self, attributeName: StringType) -> StringType: ...
    
    def Copy(self) -> ObjectType: ...
    
    def CreateSecurityElement(self) -> SecurityElement: ...
    
    def GetTag(self) -> StringType: ...
    
    # No Events


class ISecurityElementFactory(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Attribute(self, attributeName: StringType) -> StringType: ...
    
    def Copy(self) -> ObjectType: ...
    
    def CreateSecurityElement(self) -> SecurityElement: ...
    
    def GetTag(self) -> StringType: ...
    
    # No Events


class ISecurityElementFactory(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Attribute(self, attributeName: StringType) -> StringType: ...
    
    def Copy(self) -> ObjectType: ...
    
    def CreateSecurityElement(self) -> SecurityElement: ...
    
    def GetTag(self) -> StringType: ...
    
    # No Events


class ISecurityEncodable(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def FromXml(self, e: SecurityElement) -> VoidType: ...
    
    def ToXml(self) -> SecurityElement: ...
    
    # No Events


class ISecurityEncodable(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def FromXml(self, e: SecurityElement) -> VoidType: ...
    
    def ToXml(self) -> SecurityElement: ...
    
    # No Events


class ISecurityEncodable(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def FromXml(self, e: SecurityElement) -> VoidType: ...
    
    def ToXml(self) -> SecurityElement: ...
    
    # No Events


class ISecurityPolicyEncodable(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def FromXml(self, e: SecurityElement, level: PolicyLevel) -> VoidType: ...
    
    def ToXml(self, level: PolicyLevel) -> SecurityElement: ...
    
    # No Events


class ISecurityPolicyEncodable(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def FromXml(self, e: SecurityElement, level: PolicyLevel) -> VoidType: ...
    
    def ToXml(self, level: PolicyLevel) -> SecurityElement: ...
    
    # No Events


class ISecurityPolicyEncodable(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def FromXml(self, e: SecurityElement, level: PolicyLevel) -> VoidType: ...
    
    def ToXml(self, level: PolicyLevel) -> SecurityElement: ...
    
    # No Events


class IStackWalk(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Assert(self) -> VoidType: ...
    
    def Demand(self) -> VoidType: ...
    
    def Deny(self) -> VoidType: ...
    
    def PermitOnly(self) -> VoidType: ...
    
    # No Events


class IStackWalk(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Assert(self) -> VoidType: ...
    
    def Demand(self) -> VoidType: ...
    
    def Deny(self) -> VoidType: ...
    
    def PermitOnly(self) -> VoidType: ...
    
    # No Events


class IStackWalk(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Assert(self) -> VoidType: ...
    
    def Demand(self) -> VoidType: ...
    
    def Deny(self) -> VoidType: ...
    
    def PermitOnly(self) -> VoidType: ...
    
    # No Events


# ---------- Enums ---------- #

class HostSecurityManagerOptions(Enum):
    #None: IntType = 0
    HostAppDomainEvidence: IntType = 1
    HostPolicyLevel: IntType = 2
    HostAssemblyEvidence: IntType = 4
    HostDetermineApplicationTrust: IntType = 8
    HostResolvePolicy: IntType = 16
    AllFlags: IntType = 31


class HostSecurityManagerOptions(Enum):
    #None: IntType = 0
    HostAppDomainEvidence: IntType = 1
    HostPolicyLevel: IntType = 2
    HostAssemblyEvidence: IntType = 4
    HostDetermineApplicationTrust: IntType = 8
    HostResolvePolicy: IntType = 16
    AllFlags: IntType = 31


class HostSecurityManagerOptions(Enum):
    #None: IntType = 0
    HostAppDomainEvidence: IntType = 1
    HostPolicyLevel: IntType = 2
    HostAssemblyEvidence: IntType = 4
    HostDetermineApplicationTrust: IntType = 8
    HostResolvePolicy: IntType = 16
    AllFlags: IntType = 31


class ManifestKinds(Enum):
    #None: IntType = 0
    Deployment: IntType = 1
    Application: IntType = 2
    ApplicationAndDeployment: IntType = 3


class ManifestKinds(Enum):
    #None: IntType = 0
    Deployment: IntType = 1
    Application: IntType = 2
    ApplicationAndDeployment: IntType = 3


class PartialTrustVisibilityLevel(Enum):
    VisibleToAllHosts: IntType = 0
    NotVisibleByDefault: IntType = 1


class PartialTrustVisibilityLevel(Enum):
    VisibleToAllHosts: IntType = 0
    NotVisibleByDefault: IntType = 1


class PartialTrustVisibilityLevel(Enum):
    VisibleToAllHosts: IntType = 0
    NotVisibleByDefault: IntType = 1


class PermissionTokenType(Enum):
    Normal: IntType = 1
    IUnrestricted: IntType = 2
    DontKnow: IntType = 4
    BuiltIn: IntType = 8


class PermissionTokenType(Enum):
    Normal: IntType = 1
    IUnrestricted: IntType = 2
    DontKnow: IntType = 4
    BuiltIn: IntType = 8


class PermissionTokenType(Enum):
    Normal: IntType = 1
    IUnrestricted: IntType = 2
    DontKnow: IntType = 4
    BuiltIn: IntType = 8


class PermissionType(Enum):
    SecurityUnmngdCodeAccess: IntType = 0
    SecuritySkipVerification: IntType = 1
    ReflectionTypeInfo: IntType = 2
    SecurityAssert: IntType = 3
    ReflectionMemberAccess: IntType = 4
    SecuritySerialization: IntType = 5
    ReflectionRestrictedMemberAccess: IntType = 6
    FullTrust: IntType = 7
    SecurityBindingRedirects: IntType = 8
    UIPermission: IntType = 9
    EnvironmentPermission: IntType = 10
    FileDialogPermission: IntType = 11
    FileIOPermission: IntType = 12
    ReflectionPermission: IntType = 13
    SecurityPermission: IntType = 14
    SecurityControlEvidence: IntType = 16
    SecurityControlPrincipal: IntType = 17


class PermissionType(Enum):
    SecurityUnmngdCodeAccess: IntType = 0
    SecuritySkipVerification: IntType = 1
    ReflectionTypeInfo: IntType = 2
    SecurityAssert: IntType = 3
    ReflectionMemberAccess: IntType = 4
    SecuritySerialization: IntType = 5
    ReflectionRestrictedMemberAccess: IntType = 6
    FullTrust: IntType = 7
    SecurityBindingRedirects: IntType = 8
    UIPermission: IntType = 9
    EnvironmentPermission: IntType = 10
    FileDialogPermission: IntType = 11
    FileIOPermission: IntType = 12
    ReflectionPermission: IntType = 13
    SecurityPermission: IntType = 14
    SecurityControlEvidence: IntType = 16
    SecurityControlPrincipal: IntType = 17


class PermissionType(Enum):
    SecurityUnmngdCodeAccess: IntType = 0
    SecuritySkipVerification: IntType = 1
    ReflectionTypeInfo: IntType = 2
    SecurityAssert: IntType = 3
    ReflectionMemberAccess: IntType = 4
    SecuritySerialization: IntType = 5
    ReflectionRestrictedMemberAccess: IntType = 6
    FullTrust: IntType = 7
    SecurityBindingRedirects: IntType = 8
    UIPermission: IntType = 9
    EnvironmentPermission: IntType = 10
    FileDialogPermission: IntType = 11
    FileIOPermission: IntType = 12
    ReflectionPermission: IntType = 13
    SecurityPermission: IntType = 14
    SecurityControlEvidence: IntType = 16
    SecurityControlPrincipal: IntType = 17


class PolicyLevelType(Enum):
    User: IntType = 0
    Machine: IntType = 1
    Enterprise: IntType = 2
    AppDomain: IntType = 3


class PolicyLevelType(Enum):
    User: IntType = 0
    Machine: IntType = 1
    Enterprise: IntType = 2
    AppDomain: IntType = 3


class PolicyLevelType(Enum):
    User: IntType = 0
    Machine: IntType = 1
    Enterprise: IntType = 2
    AppDomain: IntType = 3


class SecurityContextDisableFlow(Enum):
    Nothing: IntType = 0
    WI: IntType = 1
    All: IntType = 16383


class SecurityContextDisableFlow(Enum):
    Nothing: IntType = 0
    WI: IntType = 1
    All: IntType = 16383


class SecurityContextDisableFlow(Enum):
    Nothing: IntType = 0
    WI: IntType = 1
    All: IntType = 16383


class SecurityContextSource(Enum):
    CurrentAppDomain: IntType = 0
    CurrentAssembly: IntType = 1


class SecurityContextSource(Enum):
    CurrentAppDomain: IntType = 0
    CurrentAssembly: IntType = 1


class SecurityContextSource(Enum):
    CurrentAppDomain: IntType = 0
    CurrentAssembly: IntType = 1


class SecurityCriticalScope(Enum):
    Explicit: IntType = 0
    Everything: IntType = 1


class SecurityCriticalScope(Enum):
    Explicit: IntType = 0
    Everything: IntType = 1


class SecurityCriticalScope(Enum):
    Explicit: IntType = 0
    Everything: IntType = 1


class SecurityElementType(Enum):
    Regular: IntType = 0
    Format: IntType = 1
    Comment: IntType = 2


class SecurityElementType(Enum):
    Regular: IntType = 0
    Format: IntType = 1
    Comment: IntType = 2


class SecurityElementType(Enum):
    Regular: IntType = 0
    Format: IntType = 1
    Comment: IntType = 2


class SecurityRuleSet(Enum):
    #None: ByteType = 0
    Level1: ByteType = 1
    Level2: ByteType = 2


class SecurityRuleSet(Enum):
    #None: ByteType = 0
    Level1: ByteType = 1
    Level2: ByteType = 2


class SecurityRuleSet(Enum):
    #None: ByteType = 0
    Level1: ByteType = 1
    Level2: ByteType = 2


class SecurityZone(Enum):
    NoZone: IntType = -1
    MyComputer: IntType = 0
    Intranet: IntType = 1
    Trusted: IntType = 2
    Internet: IntType = 3
    Untrusted: IntType = 4


class SecurityZone(Enum):
    NoZone: IntType = -1
    MyComputer: IntType = 0
    Intranet: IntType = 1
    Trusted: IntType = 2
    Internet: IntType = 3
    Untrusted: IntType = 4


class SecurityZone(Enum):
    NoZone: IntType = -1
    MyComputer: IntType = 0
    Intranet: IntType = 1
    Trusted: IntType = 2
    Internet: IntType = 3
    Untrusted: IntType = 4


class SpecialPermissionSetFlag(Enum):
    Regular: IntType = 0
    NoSet: IntType = 1
    EmptySet: IntType = 2
    SkipVerification: IntType = 3


class SpecialPermissionSetFlag(Enum):
    Regular: IntType = 0
    NoSet: IntType = 1
    EmptySet: IntType = 2
    SkipVerification: IntType = 3


class SpecialPermissionSetFlag(Enum):
    Regular: IntType = 0
    NoSet: IntType = 1
    EmptySet: IntType = 2
    SkipVerification: IntType = 3


class WindowsImpersonationFlowMode(Enum):
    IMP_DEFAULT: IntType = 0
    IMP_FASTFLOW: IntType = 0
    IMP_NOFLOW: IntType = 1
    IMP_ALWAYSFLOW: IntType = 2


class WindowsImpersonationFlowMode(Enum):
    IMP_DEFAULT: IntType = 0
    IMP_FASTFLOW: IntType = 0
    IMP_NOFLOW: IntType = 1
    IMP_ALWAYSFLOW: IntType = 2


class WindowsImpersonationFlowMode(Enum):
    IMP_DEFAULT: IntType = 0
    IMP_FASTFLOW: IntType = 0
    IMP_NOFLOW: IntType = 1
    IMP_ALWAYSFLOW: IntType = 2


# No Delegates

__all__ = [
    AllowPartiallyTrustedCallersAttribute,
    BuiltInPermissionSets,
    CodeAccessPermission,
    CodeAccessSecurityEngine,
    DynamicSecurityMethodAttribute,
    FrameSecurityDescriptor,
    FrameSecurityDescriptorWithResolver,
    HostProtectionException,
    HostSecurityManager,
    NamedPermissionSet,
    PermissionListSet,
    PermissionSet,
    PermissionSetEnumerator,
    PermissionSetTriple,
    PermissionToken,
    PermissionTokenFactory,
    PermissionTokenKeyComparer,
    PolicyManager,
    ReadOnlyPermissionSet,
    ReadOnlyPermissionSetEnumerator,
    SafeBSTRHandle,
    SecureString,
    SecureStringMarshal,
    SecurityContext,
    SecurityCriticalAttribute,
    SecurityDocument,
    SecurityDocumentElement,
    SecurityElement,
    SecurityException,
    SecurityManager,
    SecurityResources,
    SecurityRulesAttribute,
    SecurityRuntime,
    SecuritySafeCriticalAttribute,
    SecurityState,
    SecurityTransparentAttribute,
    SecurityTreatAsSafeAttribute,
    SuppressUnmanagedCodeSecurityAttribute,
    UnverifiableCodeAttribute,
    VerificationException,
    XmlSyntaxException,
    PermissionSetEnumeratorInternal,
    SecurityContextSwitcher,
    IEvidenceFactory,
    IPermission,
    ISecurityElementFactory,
    ISecurityEncodable,
    ISecurityPolicyEncodable,
    IStackWalk,
    HostSecurityManagerOptions,
    ManifestKinds,
    PartialTrustVisibilityLevel,
    PermissionTokenType,
    PermissionType,
    PolicyLevelType,
    SecurityContextDisableFlow,
    SecurityContextSource,
    SecurityCriticalScope,
    SecurityElementType,
    SecurityRuleSet,
    SecurityZone,
    SpecialPermissionSetFlag,
    WindowsImpersonationFlowMode,
]
