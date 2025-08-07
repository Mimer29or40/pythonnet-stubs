"""Automatically generated stubs for C# namespace: System.Deployment.Internal.Isolation.Manifest."""

from abc import ABC
from typing import Final
from typing import overload

from System import Enum
from System import Guid
from System import IDisposable
from System import IntPtr
from System import Object
from System import Type
from System.Deployment.Internal.Isolation import IDefinitionIdentity
from System.Deployment.Internal.Isolation import IReferenceIdentity
from System.Deployment.Internal.Isolation import ISection
from System.Deployment.Internal.Isolation import ISectionEntry

class AssemblyReferenceDependentAssemblyEntry(Object, IDisposable):
    """"""

    Codebase: Final[str]
    """"""
    Description: Final[str]
    """"""
    Flags: Final[int]
    """"""
    Group: Final[str]
    """"""
    HashAlgorithm: Final[int]
    """"""
    HashElements: Final[ISection]
    """"""
    HashValue: Final[IntPtr]
    """"""
    HashValueSize: Final[int]
    """"""
    ResourceFallbackCulture: Final[str]
    """"""
    Size: Final[int]
    """"""
    SupportUrl: Final[str]
    """"""
    def __init__(self) -> None:
        """"""
    @overload
    def Dispose(self) -> None:
        """"""
    @overload
    def Dispose(self, fDisposing: bool) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class AssemblyReferenceDependentAssemblyEntryFieldId(Enum):
    """"""

    AssemblyReferenceDependentAssembly_Group: AssemblyReferenceDependentAssemblyEntryFieldId = ...
    """"""
    AssemblyReferenceDependentAssembly_Codebase: AssemblyReferenceDependentAssemblyEntryFieldId = (
        ...
    )
    """"""
    AssemblyReferenceDependentAssembly_Size: AssemblyReferenceDependentAssemblyEntryFieldId = ...
    """"""
    AssemblyReferenceDependentAssembly_HashValue: AssemblyReferenceDependentAssemblyEntryFieldId = (
        ...
    )
    """"""
    AssemblyReferenceDependentAssembly_HashValueSize: AssemblyReferenceDependentAssemblyEntryFieldId = ...
    """"""
    AssemblyReferenceDependentAssembly_HashAlgorithm: AssemblyReferenceDependentAssemblyEntryFieldId = ...
    """"""
    AssemblyReferenceDependentAssembly_Flags: AssemblyReferenceDependentAssemblyEntryFieldId = ...
    """"""
    AssemblyReferenceDependentAssembly_ResourceFallbackCulture: AssemblyReferenceDependentAssemblyEntryFieldId = ...
    """"""
    AssemblyReferenceDependentAssembly_Description: AssemblyReferenceDependentAssemblyEntryFieldId = ...
    """"""
    AssemblyReferenceDependentAssembly_SupportUrl: AssemblyReferenceDependentAssemblyEntryFieldId = ...
    """"""
    AssemblyReferenceDependentAssembly_HashElements: AssemblyReferenceDependentAssemblyEntryFieldId = ...
    """"""

class AssemblyReferenceEntry(Object):
    """"""

    DependentAssembly: Final[AssemblyReferenceDependentAssemblyEntry]
    """"""
    Flags: Final[int]
    """"""
    ReferenceIdentity: Final[IReferenceIdentity]
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

class AssemblyReferenceEntryFieldId(Enum):
    """"""

    AssemblyReference_Flags: AssemblyReferenceEntryFieldId = ...
    """"""
    AssemblyReference_DependentAssembly: AssemblyReferenceEntryFieldId = ...
    """"""

class AssemblyRequestEntry(Object):
    """"""

    Name: Final[str]
    """"""
    permissionSetID: Final[str]
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

class AssemblyRequestEntryFieldId(Enum):
    """"""

    AssemblyRequest_permissionSetID: AssemblyRequestEntryFieldId = ...
    """"""

class CLRSurrogateEntry(Object):
    """"""

    ClassName: Final[str]
    """"""
    Clsid: Final[Guid]
    """"""
    RuntimeVersion: Final[str]
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

class CLRSurrogateEntryFieldId(Enum):
    """"""

    CLRSurrogate_RuntimeVersion: CLRSurrogateEntryFieldId = ...
    """"""
    CLRSurrogate_ClassName: CLRSurrogateEntryFieldId = ...
    """"""

class CMSSECTIONID(Enum):
    """"""

    CMSSECTIONID_FILE_SECTION: CMSSECTIONID = ...
    """"""
    CMSSECTIONID_CATEGORY_INSTANCE_SECTION: CMSSECTIONID = ...
    """"""
    CMSSECTIONID_COM_REDIRECTION_SECTION: CMSSECTIONID = ...
    """"""
    CMSSECTIONID_PROGID_REDIRECTION_SECTION: CMSSECTIONID = ...
    """"""
    CMSSECTIONID_CLR_SURROGATE_SECTION: CMSSECTIONID = ...
    """"""
    CMSSECTIONID_ASSEMBLY_REFERENCE_SECTION: CMSSECTIONID = ...
    """"""
    CMSSECTIONID_WINDOW_CLASS_SECTION: CMSSECTIONID = ...
    """"""
    CMSSECTIONID_STRING_SECTION: CMSSECTIONID = ...
    """"""
    CMSSECTIONID_ENTRYPOINT_SECTION: CMSSECTIONID = ...
    """"""
    CMSSECTIONID_PERMISSION_SET_SECTION: CMSSECTIONID = ...
    """"""
    CMSSECTIONENTRYID_METADATA: CMSSECTIONID = ...
    """"""
    CMSSECTIONID_ASSEMBLY_REQUEST_SECTION: CMSSECTIONID = ...
    """"""
    CMSSECTIONID_REGISTRY_KEY_SECTION: CMSSECTIONID = ...
    """"""
    CMSSECTIONID_DIRECTORY_SECTION: CMSSECTIONID = ...
    """"""
    CMSSECTIONID_FILE_ASSOCIATION_SECTION: CMSSECTIONID = ...
    """"""
    CMSSECTIONID_COMPATIBLE_FRAMEWORKS_SECTION: CMSSECTIONID = ...
    """"""
    CMSSECTIONID_EVENT_SECTION: CMSSECTIONID = ...
    """"""
    CMSSECTIONID_EVENT_MAP_SECTION: CMSSECTIONID = ...
    """"""
    CMSSECTIONID_EVENT_TAG_SECTION: CMSSECTIONID = ...
    """"""
    CMSSECTIONID_COUNTERSET_SECTION: CMSSECTIONID = ...
    """"""
    CMSSECTIONID_COUNTER_SECTION: CMSSECTIONID = ...
    """"""

class CMS_ASSEMBLY_DEPLOYMENT_FLAG(Enum):
    """"""

    CMS_ASSEMBLY_DEPLOYMENT_FLAG_BEFORE_APPLICATION_STARTUP: CMS_ASSEMBLY_DEPLOYMENT_FLAG = ...
    """"""
    CMS_ASSEMBLY_DEPLOYMENT_FLAG_RUN_AFTER_INSTALL: CMS_ASSEMBLY_DEPLOYMENT_FLAG = ...
    """"""
    CMS_ASSEMBLY_DEPLOYMENT_FLAG_INSTALL: CMS_ASSEMBLY_DEPLOYMENT_FLAG = ...
    """"""
    CMS_ASSEMBLY_DEPLOYMENT_FLAG_TRUST_URL_PARAMETERS: CMS_ASSEMBLY_DEPLOYMENT_FLAG = ...
    """"""
    CMS_ASSEMBLY_DEPLOYMENT_FLAG_DISALLOW_URL_ACTIVATION: CMS_ASSEMBLY_DEPLOYMENT_FLAG = ...
    """"""
    CMS_ASSEMBLY_DEPLOYMENT_FLAG_MAP_FILE_EXTENSIONS: CMS_ASSEMBLY_DEPLOYMENT_FLAG = ...
    """"""
    CMS_ASSEMBLY_DEPLOYMENT_FLAG_CREATE_DESKTOP_SHORTCUT: CMS_ASSEMBLY_DEPLOYMENT_FLAG = ...
    """"""

class CMS_ASSEMBLY_REFERENCE_DEPENDENT_ASSEMBLY_FLAG(Enum):
    """"""

    CMS_ASSEMBLY_REFERENCE_DEPENDENT_ASSEMBLY_FLAG_OPTIONAL: CMS_ASSEMBLY_REFERENCE_DEPENDENT_ASSEMBLY_FLAG = ...
    """"""
    CMS_ASSEMBLY_REFERENCE_DEPENDENT_ASSEMBLY_FLAG_VISIBLE: CMS_ASSEMBLY_REFERENCE_DEPENDENT_ASSEMBLY_FLAG = ...
    """"""
    CMS_ASSEMBLY_REFERENCE_DEPENDENT_ASSEMBLY_FLAG_PREREQUISITE: CMS_ASSEMBLY_REFERENCE_DEPENDENT_ASSEMBLY_FLAG = ...
    """"""
    CMS_ASSEMBLY_REFERENCE_DEPENDENT_ASSEMBLY_FLAG_RESOURCE_FALLBACK_CULTURE_INTERNAL: CMS_ASSEMBLY_REFERENCE_DEPENDENT_ASSEMBLY_FLAG = ...
    """"""
    CMS_ASSEMBLY_REFERENCE_DEPENDENT_ASSEMBLY_FLAG_INSTALL: CMS_ASSEMBLY_REFERENCE_DEPENDENT_ASSEMBLY_FLAG = ...
    """"""
    CMS_ASSEMBLY_REFERENCE_DEPENDENT_ASSEMBLY_FLAG_ALLOW_DELAYED_BINDING: CMS_ASSEMBLY_REFERENCE_DEPENDENT_ASSEMBLY_FLAG = ...
    """"""

class CMS_ASSEMBLY_REFERENCE_FLAG(Enum):
    """"""

    CMS_ASSEMBLY_REFERENCE_FLAG_OPTIONAL: CMS_ASSEMBLY_REFERENCE_FLAG = ...
    """"""
    CMS_ASSEMBLY_REFERENCE_FLAG_VISIBLE: CMS_ASSEMBLY_REFERENCE_FLAG = ...
    """"""
    CMS_ASSEMBLY_REFERENCE_FLAG_FOLLOW: CMS_ASSEMBLY_REFERENCE_FLAG = ...
    """"""
    CMS_ASSEMBLY_REFERENCE_FLAG_IS_PLATFORM: CMS_ASSEMBLY_REFERENCE_FLAG = ...
    """"""
    CMS_ASSEMBLY_REFERENCE_FLAG_CULTURE_WILDCARDED: CMS_ASSEMBLY_REFERENCE_FLAG = ...
    """"""
    CMS_ASSEMBLY_REFERENCE_FLAG_PROCESSOR_ARCHITECTURE_WILDCARDED: CMS_ASSEMBLY_REFERENCE_FLAG = ...
    """"""
    CMS_ASSEMBLY_REFERENCE_FLAG_PREREQUISITE: CMS_ASSEMBLY_REFERENCE_FLAG = ...
    """"""

class CMS_COM_SERVER_FLAG(Enum):
    """"""

    CMS_COM_SERVER_FLAG_IS_CLR_CLASS: CMS_COM_SERVER_FLAG = ...
    """"""

class CMS_ENTRY_POINT_FLAG(Enum):
    """"""

    CMS_ENTRY_POINT_FLAG_HOST_IN_BROWSER: CMS_ENTRY_POINT_FLAG = ...
    """"""
    CMS_ENTRY_POINT_FLAG_CUSTOMHOSTSPECIFIED: CMS_ENTRY_POINT_FLAG = ...
    """"""
    CMS_ENTRY_POINT_FLAG_CUSTOMUX: CMS_ENTRY_POINT_FLAG = ...
    """"""

class CMS_FILE_FLAG(Enum):
    """"""

    CMS_FILE_FLAG_OPTIONAL: CMS_FILE_FLAG = ...
    """"""

class CMS_FILE_HASH_ALGORITHM(Enum):
    """"""

    CMS_FILE_HASH_ALGORITHM_SHA1: CMS_FILE_HASH_ALGORITHM = ...
    """"""
    CMS_FILE_HASH_ALGORITHM_SHA256: CMS_FILE_HASH_ALGORITHM = ...
    """"""
    CMS_FILE_HASH_ALGORITHM_SHA384: CMS_FILE_HASH_ALGORITHM = ...
    """"""
    CMS_FILE_HASH_ALGORITHM_SHA512: CMS_FILE_HASH_ALGORITHM = ...
    """"""
    CMS_FILE_HASH_ALGORITHM_MD5: CMS_FILE_HASH_ALGORITHM = ...
    """"""
    CMS_FILE_HASH_ALGORITHM_MD4: CMS_FILE_HASH_ALGORITHM = ...
    """"""
    CMS_FILE_HASH_ALGORITHM_MD2: CMS_FILE_HASH_ALGORITHM = ...
    """"""

class CMS_FILE_WRITABLE_TYPE(Enum):
    """"""

    CMS_FILE_WRITABLE_TYPE_NOT_WRITABLE: CMS_FILE_WRITABLE_TYPE = ...
    """"""
    CMS_FILE_WRITABLE_TYPE_APPLICATION_DATA: CMS_FILE_WRITABLE_TYPE = ...
    """"""

class CMS_HASH_DIGESTMETHOD(Enum):
    """"""

    CMS_HASH_DIGESTMETHOD_SHA1: CMS_HASH_DIGESTMETHOD = ...
    """"""
    CMS_HASH_DIGESTMETHOD_SHA256: CMS_HASH_DIGESTMETHOD = ...
    """"""
    CMS_HASH_DIGESTMETHOD_SHA384: CMS_HASH_DIGESTMETHOD = ...
    """"""
    CMS_HASH_DIGESTMETHOD_SHA512: CMS_HASH_DIGESTMETHOD = ...
    """"""

class CMS_HASH_TRANSFORM(Enum):
    """"""

    CMS_HASH_TRANSFORM_IDENTITY: CMS_HASH_TRANSFORM = ...
    """"""
    CMS_HASH_TRANSFORM_MANIFESTINVARIANT: CMS_HASH_TRANSFORM = ...
    """"""

class CMS_SCHEMA_VERSION(Enum):
    """"""

    CMS_SCHEMA_VERSION_V1: CMS_SCHEMA_VERSION = ...
    """"""

class CMS_TIME_UNIT_TYPE(Enum):
    """"""

    CMS_TIME_UNIT_TYPE_HOURS: CMS_TIME_UNIT_TYPE = ...
    """"""
    CMS_TIME_UNIT_TYPE_DAYS: CMS_TIME_UNIT_TYPE = ...
    """"""
    CMS_TIME_UNIT_TYPE_WEEKS: CMS_TIME_UNIT_TYPE = ...
    """"""
    CMS_TIME_UNIT_TYPE_MONTHS: CMS_TIME_UNIT_TYPE = ...
    """"""

class CMS_USAGE_PATTERN(Enum):
    """"""

    CMS_USAGE_PATTERN_SCOPE_APPLICATION: CMS_USAGE_PATTERN = ...
    """"""
    CMS_USAGE_PATTERN_SCOPE_PROCESS: CMS_USAGE_PATTERN = ...
    """"""
    CMS_USAGE_PATTERN_SCOPE_MACHINE: CMS_USAGE_PATTERN = ...
    """"""
    CMS_USAGE_PATTERN_SCOPE_MASK: CMS_USAGE_PATTERN = ...
    """"""

class COMServerEntry(Object):
    """"""

    Clsid: Final[Guid]
    """"""
    ConfiguredGuid: Final[Guid]
    """"""
    Flags: Final[int]
    """"""
    HostFile: Final[str]
    """"""
    ImplementedClsid: Final[Guid]
    """"""
    RuntimeVersion: Final[str]
    """"""
    ThreadingModel: Final[int]
    """"""
    TypeLibrary: Final[Guid]
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

class COMServerEntryFieldId(Enum):
    """"""

    COMServer_Flags: COMServerEntryFieldId = ...
    """"""
    COMServer_ConfiguredGuid: COMServerEntryFieldId = ...
    """"""
    COMServer_ImplementedClsid: COMServerEntryFieldId = ...
    """"""
    COMServer_TypeLibrary: COMServerEntryFieldId = ...
    """"""
    COMServer_ThreadingModel: COMServerEntryFieldId = ...
    """"""
    COMServer_RuntimeVersion: COMServerEntryFieldId = ...
    """"""
    COMServer_HostFile: COMServerEntryFieldId = ...
    """"""

class CategoryMembershipDataEntry(Object):
    """"""

    Description: Final[str]
    """"""
    Xml: Final[str]
    """"""
    index: Final[int]
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

class CategoryMembershipDataEntryFieldId(Enum):
    """"""

    CategoryMembershipData_Xml: CategoryMembershipDataEntryFieldId = ...
    """"""
    CategoryMembershipData_Description: CategoryMembershipDataEntryFieldId = ...
    """"""

class CategoryMembershipEntry(Object):
    """"""

    Identity: Final[IDefinitionIdentity]
    """"""
    SubcategoryMembership: Final[ISection]
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

class CategoryMembershipEntryFieldId(Enum):
    """"""

    CategoryMembership_SubcategoryMembership: CategoryMembershipEntryFieldId = ...
    """"""

class CmsUtils(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class CompatibleFrameworksMetadataEntry(Object):
    """"""

    SupportUrl: Final[str]
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

class CompatibleFrameworksMetadataEntryFieldId(Enum):
    """"""

    CompatibleFrameworksMetadata_SupportUrl: CompatibleFrameworksMetadataEntryFieldId = ...
    """"""

class DependentOSMetadataEntry(Object):
    """"""

    BuildNumber: Final[int]
    """"""
    Description: Final[str]
    """"""
    MajorVersion: Final[int]
    """"""
    MinorVersion: Final[int]
    """"""
    ServicePackMajor: Final[int]
    """"""
    ServicePackMinor: Final[int]
    """"""
    SupportUrl: Final[str]
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

class DependentOSMetadataEntryFieldId(Enum):
    """"""

    DependentOSMetadata_SupportUrl: DependentOSMetadataEntryFieldId = ...
    """"""
    DependentOSMetadata_Description: DependentOSMetadataEntryFieldId = ...
    """"""
    DependentOSMetadata_MajorVersion: DependentOSMetadataEntryFieldId = ...
    """"""
    DependentOSMetadata_MinorVersion: DependentOSMetadataEntryFieldId = ...
    """"""
    DependentOSMetadata_BuildNumber: DependentOSMetadataEntryFieldId = ...
    """"""
    DependentOSMetadata_ServicePackMajor: DependentOSMetadataEntryFieldId = ...
    """"""
    DependentOSMetadata_ServicePackMinor: DependentOSMetadataEntryFieldId = ...
    """"""

class DeploymentMetadataEntry(Object):
    """"""

    DeploymentFlags: Final[int]
    """"""
    DeploymentProviderCodebase: Final[str]
    """"""
    MaximumAge: Final[int]
    """"""
    MaximumAge_Unit: Final[int]
    """"""
    MinimumRequiredVersion: Final[str]
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

class DeploymentMetadataEntryFieldId(Enum):
    """"""

    DeploymentMetadata_DeploymentProviderCodebase: DeploymentMetadataEntryFieldId = ...
    """"""
    DeploymentMetadata_MinimumRequiredVersion: DeploymentMetadataEntryFieldId = ...
    """"""
    DeploymentMetadata_MaximumAge: DeploymentMetadataEntryFieldId = ...
    """"""
    DeploymentMetadata_MaximumAge_Unit: DeploymentMetadataEntryFieldId = ...
    """"""
    DeploymentMetadata_DeploymentFlags: DeploymentMetadataEntryFieldId = ...
    """"""

class DescriptionMetadataEntry(Object):
    """"""

    ErrorReportUrl: Final[str]
    """"""
    IconFile: Final[str]
    """"""
    Product: Final[str]
    """"""
    Publisher: Final[str]
    """"""
    SuiteName: Final[str]
    """"""
    SupportUrl: Final[str]
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

class DescriptionMetadataEntryFieldId(Enum):
    """"""

    DescriptionMetadata_Publisher: DescriptionMetadataEntryFieldId = ...
    """"""
    DescriptionMetadata_Product: DescriptionMetadataEntryFieldId = ...
    """"""
    DescriptionMetadata_SupportUrl: DescriptionMetadataEntryFieldId = ...
    """"""
    DescriptionMetadata_IconFile: DescriptionMetadataEntryFieldId = ...
    """"""
    DescriptionMetadata_ErrorReportUrl: DescriptionMetadataEntryFieldId = ...
    """"""
    DescriptionMetadata_SuiteName: DescriptionMetadataEntryFieldId = ...
    """"""

class EntryPointEntry(Object):
    """"""

    CommandLine_File: Final[str]
    """"""
    CommandLine_Parameters: Final[str]
    """"""
    Flags: Final[int]
    """"""
    Identity: Final[IReferenceIdentity]
    """"""
    Name: Final[str]
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

class EntryPointEntryFieldId(Enum):
    """"""

    EntryPoint_CommandLine_File: EntryPointEntryFieldId = ...
    """"""
    EntryPoint_CommandLine_Parameters: EntryPointEntryFieldId = ...
    """"""
    EntryPoint_Identity: EntryPointEntryFieldId = ...
    """"""
    EntryPoint_Flags: EntryPointEntryFieldId = ...
    """"""

class FileAssociationEntry(Object):
    """"""

    DefaultIcon: Final[str]
    """"""
    Description: Final[str]
    """"""
    Extension: Final[str]
    """"""
    Parameter: Final[str]
    """"""
    ProgID: Final[str]
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

class FileAssociationEntryFieldId(Enum):
    """"""

    FileAssociation_Description: FileAssociationEntryFieldId = ...
    """"""
    FileAssociation_ProgID: FileAssociationEntryFieldId = ...
    """"""
    FileAssociation_DefaultIcon: FileAssociationEntryFieldId = ...
    """"""
    FileAssociation_Parameter: FileAssociationEntryFieldId = ...
    """"""

class FileEntry(Object, IDisposable):
    """"""

    Flags: Final[int]
    """"""
    Group: Final[str]
    """"""
    HashAlgorithm: Final[int]
    """"""
    HashElements: Final[ISection]
    """"""
    HashValue: Final[IntPtr]
    """"""
    HashValueSize: Final[int]
    """"""
    ImportPath: Final[str]
    """"""
    LoadFrom: Final[str]
    """"""
    Location: Final[str]
    """"""
    MuiMapping: Final[MuiResourceMapEntry]
    """"""
    Name: Final[str]
    """"""
    Size: Final[int]
    """"""
    SourceName: Final[str]
    """"""
    SourcePath: Final[str]
    """"""
    WritableType: Final[int]
    """"""
    def __init__(self) -> None:
        """"""
    @overload
    def Dispose(self) -> None:
        """"""
    @overload
    def Dispose(self, fDisposing: bool) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class FileEntryFieldId(Enum):
    """"""

    File_HashAlgorithm: FileEntryFieldId = ...
    """"""
    File_LoadFrom: FileEntryFieldId = ...
    """"""
    File_SourcePath: FileEntryFieldId = ...
    """"""
    File_ImportPath: FileEntryFieldId = ...
    """"""
    File_SourceName: FileEntryFieldId = ...
    """"""
    File_Location: FileEntryFieldId = ...
    """"""
    File_HashValue: FileEntryFieldId = ...
    """"""
    File_HashValueSize: FileEntryFieldId = ...
    """"""
    File_Size: FileEntryFieldId = ...
    """"""
    File_Group: FileEntryFieldId = ...
    """"""
    File_Flags: FileEntryFieldId = ...
    """"""
    File_MuiMapping: FileEntryFieldId = ...
    """"""
    File_WritableType: FileEntryFieldId = ...
    """"""
    File_HashElements: FileEntryFieldId = ...
    """"""

class HashElementEntry(Object, IDisposable):
    """"""

    DigestMethod: Final[int]
    """"""
    DigestValue: Final[IntPtr]
    """"""
    DigestValueSize: Final[int]
    """"""
    Transform: Final[int]
    """"""
    TransformMetadata: Final[IntPtr]
    """"""
    TransformMetadataSize: Final[int]
    """"""
    Xml: Final[str]
    """"""
    index: Final[int]
    """"""
    def __init__(self) -> None:
        """"""
    @overload
    def Dispose(self) -> None:
        """"""
    @overload
    def Dispose(self, fDisposing: bool) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class HashElementEntryFieldId(Enum):
    """"""

    HashElement_Transform: HashElementEntryFieldId = ...
    """"""
    HashElement_TransformMetadata: HashElementEntryFieldId = ...
    """"""
    HashElement_TransformMetadataSize: HashElementEntryFieldId = ...
    """"""
    HashElement_DigestMethod: HashElementEntryFieldId = ...
    """"""
    HashElement_DigestValue: HashElementEntryFieldId = ...
    """"""
    HashElement_DigestValueSize: HashElementEntryFieldId = ...
    """"""
    HashElement_Xml: HashElementEntryFieldId = ...
    """"""

class IAssemblyReferenceDependentAssemblyEntry:
    """"""
    @property
    def AllData(self) -> AssemblyReferenceDependentAssemblyEntry:
        """"""
    @property
    def Codebase(self) -> str:
        """"""
    @property
    def Description(self) -> str:
        """"""
    @property
    def Flags(self) -> int:
        """"""
    @property
    def Group(self) -> str:
        """"""
    @property
    def HashAlgorithm(self) -> int:
        """"""
    @property
    def HashElements(self) -> ISection:
        """"""
    @property
    def HashValue(self) -> object:
        """"""
    @property
    def ResourceFallbackCulture(self) -> str:
        """"""
    @property
    def Size(self) -> int:
        """"""
    @property
    def SupportUrl(self) -> str:
        """"""

class IAssemblyReferenceEntry:
    """"""
    @property
    def AllData(self) -> AssemblyReferenceEntry:
        """"""
    @property
    def DependentAssembly(self) -> IAssemblyReferenceDependentAssemblyEntry:
        """"""
    @property
    def Flags(self) -> int:
        """"""
    @property
    def ReferenceIdentity(self) -> IReferenceIdentity:
        """"""

class IAssemblyRequestEntry:
    """"""
    @property
    def AllData(self) -> AssemblyRequestEntry:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def permissionSetID(self) -> str:
        """"""

class ICLRSurrogateEntry:
    """"""
    @property
    def AllData(self) -> CLRSurrogateEntry:
        """"""
    @property
    def ClassName(self) -> str:
        """"""
    @property
    def Clsid(self) -> Guid:
        """"""
    @property
    def RuntimeVersion(self) -> str:
        """"""

class ICMS:
    """"""
    @property
    def AssemblyReferenceSection(self) -> ISection:
        """"""
    @property
    def AssemblyRequestSection(self) -> ISection:
        """"""
    @property
    def CLRSurrogateSection(self) -> ISection:
        """"""
    @property
    def COMRedirectionSection(self) -> ISection:
        """"""
    @property
    def CategoryMembershipSection(self) -> ISection:
        """"""
    @property
    def CompatibleFrameworksSection(self) -> ISection:
        """"""
    @property
    def CounterSection(self) -> ISection:
        """"""
    @property
    def CounterSetSection(self) -> ISection:
        """"""
    @property
    def DirectorySection(self) -> ISection:
        """"""
    @property
    def EntryPointSection(self) -> ISection:
        """"""
    @property
    def EventMapSection(self) -> ISection:
        """"""
    @property
    def EventSection(self) -> ISection:
        """"""
    @property
    def EventTagSection(self) -> ISection:
        """"""
    @property
    def FileAssociationSection(self) -> ISection:
        """"""
    @property
    def FileSection(self) -> ISection:
        """"""
    @property
    def Identity(self) -> IDefinitionIdentity:
        """"""
    @property
    def MetadataSectionEntry(self) -> ISectionEntry:
        """"""
    @property
    def PermissionSetSection(self) -> ISection:
        """"""
    @property
    def ProgIdRedirectionSection(self) -> ISection:
        """"""
    @property
    def RegistryKeySection(self) -> ISection:
        """"""
    @property
    def StringSection(self) -> ISection:
        """"""
    @property
    def WindowClassSection(self) -> ISection:
        """"""

class ICOMServerEntry:
    """"""
    @property
    def AllData(self) -> COMServerEntry:
        """"""
    @property
    def Clsid(self) -> Guid:
        """"""
    @property
    def ConfiguredGuid(self) -> Guid:
        """"""
    @property
    def Flags(self) -> int:
        """"""
    @property
    def HostFile(self) -> str:
        """"""
    @property
    def ImplementedClsid(self) -> Guid:
        """"""
    @property
    def RuntimeVersion(self) -> str:
        """"""
    @property
    def ThreadingModel(self) -> int:
        """"""
    @property
    def TypeLibrary(self) -> Guid:
        """"""

class ICategoryMembershipDataEntry:
    """"""
    @property
    def AllData(self) -> CategoryMembershipDataEntry:
        """"""
    @property
    def Description(self) -> str:
        """"""
    @property
    def Xml(self) -> str:
        """"""
    @property
    def index(self) -> int:
        """"""

class ICategoryMembershipEntry:
    """"""
    @property
    def AllData(self) -> CategoryMembershipEntry:
        """"""
    @property
    def Identity(self) -> IDefinitionIdentity:
        """"""
    @property
    def SubcategoryMembership(self) -> ISection:
        """"""

class ICompatibleFrameworksMetadataEntry:
    """"""
    @property
    def AllData(self) -> CompatibleFrameworksMetadataEntry:
        """"""
    @property
    def SupportUrl(self) -> str:
        """"""

class IDependentOSMetadataEntry:
    """"""
    @property
    def AllData(self) -> DependentOSMetadataEntry:
        """"""
    @property
    def BuildNumber(self) -> int:
        """"""
    @property
    def Description(self) -> str:
        """"""
    @property
    def MajorVersion(self) -> int:
        """"""
    @property
    def MinorVersion(self) -> int:
        """"""
    @property
    def ServicePackMajor(self) -> int:
        """"""
    @property
    def ServicePackMinor(self) -> int:
        """"""
    @property
    def SupportUrl(self) -> str:
        """"""

class IDeploymentMetadataEntry:
    """"""
    @property
    def AllData(self) -> DeploymentMetadataEntry:
        """"""
    @property
    def DeploymentFlags(self) -> int:
        """"""
    @property
    def DeploymentProviderCodebase(self) -> str:
        """"""
    @property
    def MaximumAge(self) -> int:
        """"""
    @property
    def MaximumAge_Unit(self) -> int:
        """"""
    @property
    def MinimumRequiredVersion(self) -> str:
        """"""

class IDescriptionMetadataEntry:
    """"""
    @property
    def AllData(self) -> DescriptionMetadataEntry:
        """"""
    @property
    def ErrorReportUrl(self) -> str:
        """"""
    @property
    def IconFile(self) -> str:
        """"""
    @property
    def Product(self) -> str:
        """"""
    @property
    def Publisher(self) -> str:
        """"""
    @property
    def SuiteName(self) -> str:
        """"""
    @property
    def SupportUrl(self) -> str:
        """"""

class IEntryPointEntry:
    """"""
    @property
    def AllData(self) -> EntryPointEntry:
        """"""
    @property
    def CommandLine_File(self) -> str:
        """"""
    @property
    def CommandLine_Parameters(self) -> str:
        """"""
    @property
    def Flags(self) -> int:
        """"""
    @property
    def Identity(self) -> IReferenceIdentity:
        """"""
    @property
    def Name(self) -> str:
        """"""

class IFileAssociationEntry:
    """"""
    @property
    def AllData(self) -> FileAssociationEntry:
        """"""
    @property
    def DefaultIcon(self) -> str:
        """"""
    @property
    def Description(self) -> str:
        """"""
    @property
    def Extension(self) -> str:
        """"""
    @property
    def Parameter(self) -> str:
        """"""
    @property
    def ProgID(self) -> str:
        """"""

class IFileEntry:
    """"""
    @property
    def AllData(self) -> FileEntry:
        """"""
    @property
    def Flags(self) -> int:
        """"""
    @property
    def Group(self) -> str:
        """"""
    @property
    def HashAlgorithm(self) -> int:
        """"""
    @property
    def HashElements(self) -> ISection:
        """"""
    @property
    def HashValue(self) -> object:
        """"""
    @property
    def ImportPath(self) -> str:
        """"""
    @property
    def LoadFrom(self) -> str:
        """"""
    @property
    def Location(self) -> str:
        """"""
    @property
    def MuiMapping(self) -> IMuiResourceMapEntry:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def Size(self) -> int:
        """"""
    @property
    def SourceName(self) -> str:
        """"""
    @property
    def SourcePath(self) -> str:
        """"""
    @property
    def WritableType(self) -> int:
        """"""

class IHashElementEntry:
    """"""
    @property
    def AllData(self) -> HashElementEntry:
        """"""
    @property
    def DigestMethod(self) -> int:
        """"""
    @property
    def DigestValue(self) -> object:
        """"""
    @property
    def Transform(self) -> int:
        """"""
    @property
    def TransformMetadata(self) -> object:
        """"""
    @property
    def Xml(self) -> str:
        """"""
    @property
    def index(self) -> int:
        """"""

class IMetadataSectionEntry:
    """"""
    @property
    def AllData(self) -> MetadataSectionEntry:
        """"""
    @property
    def CdfIdentity(self) -> IDefinitionIdentity:
        """"""
    @property
    def CompatibleFrameworksData(self) -> ICompatibleFrameworksMetadataEntry:
        """"""
    @property
    def ContentType(self) -> str:
        """"""
    @property
    def DependentOSData(self) -> IDependentOSMetadataEntry:
        """"""
    @property
    def DeploymentData(self) -> IDeploymentMetadataEntry:
        """"""
    @property
    def DescriptionData(self) -> IDescriptionMetadataEntry:
        """"""
    @property
    def HashAlgorithm(self) -> int:
        """"""
    @property
    def KeyInfoElement(self) -> str:
        """"""
    @property
    def LocalPath(self) -> str:
        """"""
    @property
    def ManifestFlags(self) -> int:
        """"""
    @property
    def ManifestHash(self) -> object:
        """"""
    @property
    def MvidValue(self) -> object:
        """"""
    @property
    def RequestedExecutionLevel(self) -> str:
        """"""
    @property
    def RequestedExecutionLevelUIAccess(self) -> bool:
        """"""
    @property
    def ResourceTypeManifestResourcesDependency(self) -> IReferenceIdentity:
        """"""
    @property
    def ResourceTypeResourcesDependency(self) -> IReferenceIdentity:
        """"""
    @property
    def RuntimeImageVersion(self) -> str:
        """"""
    @property
    def SchemaVersion(self) -> int:
        """"""
    @property
    def UsagePatterns(self) -> int:
        """"""
    @property
    def defaultPermissionSetID(self) -> str:
        """"""

class IMuiResourceIdLookupMapEntry:
    """"""
    @property
    def AllData(self) -> MuiResourceIdLookupMapEntry:
        """"""
    @property
    def Count(self) -> int:
        """"""
    def __len__(self) -> int:
        """"""

class IMuiResourceMapEntry:
    """"""
    @property
    def AllData(self) -> MuiResourceMapEntry:
        """"""
    @property
    def ResourceTypeIdInt(self) -> object:
        """"""
    @property
    def ResourceTypeIdString(self) -> object:
        """"""

class IMuiResourceTypeIdIntEntry:
    """"""
    @property
    def AllData(self) -> MuiResourceTypeIdIntEntry:
        """"""
    @property
    def IntegerIds(self) -> object:
        """"""
    @property
    def StringIds(self) -> object:
        """"""

class IMuiResourceTypeIdStringEntry:
    """"""
    @property
    def AllData(self) -> MuiResourceTypeIdStringEntry:
        """"""
    @property
    def IntegerIds(self) -> object:
        """"""
    @property
    def StringIds(self) -> object:
        """"""

class IPermissionSetEntry:
    """"""
    @property
    def AllData(self) -> PermissionSetEntry:
        """"""
    @property
    def Id(self) -> str:
        """"""
    @property
    def XmlSegment(self) -> str:
        """"""

class IProgIdRedirectionEntry:
    """"""
    @property
    def AllData(self) -> ProgIdRedirectionEntry:
        """"""
    @property
    def ProgId(self) -> str:
        """"""
    @property
    def RedirectedGuid(self) -> Guid:
        """"""

class IResourceTableMappingEntry:
    """"""
    @property
    def AllData(self) -> ResourceTableMappingEntry:
        """"""
    @property
    def FinalStringMapped(self) -> str:
        """"""
    @property
    def id(self) -> str:
        """"""

class ISubcategoryMembershipEntry:
    """"""
    @property
    def AllData(self) -> SubcategoryMembershipEntry:
        """"""
    @property
    def CategoryMembershipData(self) -> ISection:
        """"""
    @property
    def Subcategory(self) -> str:
        """"""

class IWindowClassEntry:
    """"""
    @property
    def AllData(self) -> WindowClassEntry:
        """"""
    @property
    def ClassName(self) -> str:
        """"""
    @property
    def HostDll(self) -> str:
        """"""
    @property
    def fVersioned(self) -> bool:
        """"""

class MetadataSectionEntry(Object, IDisposable):
    """"""

    CdfIdentity: Final[IDefinitionIdentity]
    """"""
    CompatibleFrameworksData: Final[CompatibleFrameworksMetadataEntry]
    """"""
    ContentType: Final[str]
    """"""
    DependentOSData: Final[DependentOSMetadataEntry]
    """"""
    DeploymentData: Final[DeploymentMetadataEntry]
    """"""
    DescriptionData: Final[DescriptionMetadataEntry]
    """"""
    HashAlgorithm: Final[int]
    """"""
    KeyInfoElement: Final[str]
    """"""
    LocalPath: Final[str]
    """"""
    ManifestFlags: Final[int]
    """"""
    ManifestHash: Final[IntPtr]
    """"""
    ManifestHashSize: Final[int]
    """"""
    MvidValue: Final[IntPtr]
    """"""
    MvidValueSize: Final[int]
    """"""
    RequestedExecutionLevel: Final[str]
    """"""
    RequestedExecutionLevelUIAccess: Final[bool]
    """"""
    ResourceTypeManifestResourcesDependency: Final[IReferenceIdentity]
    """"""
    ResourceTypeResourcesDependency: Final[IReferenceIdentity]
    """"""
    RuntimeImageVersion: Final[str]
    """"""
    SchemaVersion: Final[int]
    """"""
    UsagePatterns: Final[int]
    """"""
    defaultPermissionSetID: Final[str]
    """"""
    def __init__(self) -> None:
        """"""
    @overload
    def Dispose(self) -> None:
        """"""
    @overload
    def Dispose(self, fDisposing: bool) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class MetadataSectionEntryFieldId(Enum):
    """"""

    MetadataSection_SchemaVersion: MetadataSectionEntryFieldId = ...
    """"""
    MetadataSection_ManifestFlags: MetadataSectionEntryFieldId = ...
    """"""
    MetadataSection_UsagePatterns: MetadataSectionEntryFieldId = ...
    """"""
    MetadataSection_CdfIdentity: MetadataSectionEntryFieldId = ...
    """"""
    MetadataSection_LocalPath: MetadataSectionEntryFieldId = ...
    """"""
    MetadataSection_HashAlgorithm: MetadataSectionEntryFieldId = ...
    """"""
    MetadataSection_ManifestHash: MetadataSectionEntryFieldId = ...
    """"""
    MetadataSection_ManifestHashSize: MetadataSectionEntryFieldId = ...
    """"""
    MetadataSection_ContentType: MetadataSectionEntryFieldId = ...
    """"""
    MetadataSection_RuntimeImageVersion: MetadataSectionEntryFieldId = ...
    """"""
    MetadataSection_MvidValue: MetadataSectionEntryFieldId = ...
    """"""
    MetadataSection_MvidValueSize: MetadataSectionEntryFieldId = ...
    """"""
    MetadataSection_DescriptionData: MetadataSectionEntryFieldId = ...
    """"""
    MetadataSection_DeploymentData: MetadataSectionEntryFieldId = ...
    """"""
    MetadataSection_DependentOSData: MetadataSectionEntryFieldId = ...
    """"""
    MetadataSection_defaultPermissionSetID: MetadataSectionEntryFieldId = ...
    """"""
    MetadataSection_RequestedExecutionLevel: MetadataSectionEntryFieldId = ...
    """"""
    MetadataSection_RequestedExecutionLevelUIAccess: MetadataSectionEntryFieldId = ...
    """"""
    MetadataSection_ResourceTypeResourcesDependency: MetadataSectionEntryFieldId = ...
    """"""
    MetadataSection_ResourceTypeManifestResourcesDependency: MetadataSectionEntryFieldId = ...
    """"""
    MetadataSection_KeyInfoElement: MetadataSectionEntryFieldId = ...
    """"""
    MetadataSection_CompatibleFrameworksData: MetadataSectionEntryFieldId = ...
    """"""

class MuiResourceIdLookupMapEntry(Object):
    """"""

    Count: Final[int]
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

class MuiResourceIdLookupMapEntryFieldId(Enum):
    """"""

    MuiResourceIdLookupMap_Count: MuiResourceIdLookupMapEntryFieldId = ...
    """"""

class MuiResourceMapEntry(Object, IDisposable):
    """"""

    ResourceTypeIdInt: Final[IntPtr]
    """"""
    ResourceTypeIdIntSize: Final[int]
    """"""
    ResourceTypeIdString: Final[IntPtr]
    """"""
    ResourceTypeIdStringSize: Final[int]
    """"""
    def __init__(self) -> None:
        """"""
    @overload
    def Dispose(self) -> None:
        """"""
    @overload
    def Dispose(self, fDisposing: bool) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class MuiResourceMapEntryFieldId(Enum):
    """"""

    MuiResourceMap_ResourceTypeIdInt: MuiResourceMapEntryFieldId = ...
    """"""
    MuiResourceMap_ResourceTypeIdIntSize: MuiResourceMapEntryFieldId = ...
    """"""
    MuiResourceMap_ResourceTypeIdString: MuiResourceMapEntryFieldId = ...
    """"""
    MuiResourceMap_ResourceTypeIdStringSize: MuiResourceMapEntryFieldId = ...
    """"""

class MuiResourceTypeIdIntEntry(Object, IDisposable):
    """"""

    IntegerIds: Final[IntPtr]
    """"""
    IntegerIdsSize: Final[int]
    """"""
    StringIds: Final[IntPtr]
    """"""
    StringIdsSize: Final[int]
    """"""
    def __init__(self) -> None:
        """"""
    @overload
    def Dispose(self) -> None:
        """"""
    @overload
    def Dispose(self, fDisposing: bool) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class MuiResourceTypeIdIntEntryFieldId(Enum):
    """"""

    MuiResourceTypeIdInt_StringIds: MuiResourceTypeIdIntEntryFieldId = ...
    """"""
    MuiResourceTypeIdInt_StringIdsSize: MuiResourceTypeIdIntEntryFieldId = ...
    """"""
    MuiResourceTypeIdInt_IntegerIds: MuiResourceTypeIdIntEntryFieldId = ...
    """"""
    MuiResourceTypeIdInt_IntegerIdsSize: MuiResourceTypeIdIntEntryFieldId = ...
    """"""

class MuiResourceTypeIdStringEntry(Object, IDisposable):
    """"""

    IntegerIds: Final[IntPtr]
    """"""
    IntegerIdsSize: Final[int]
    """"""
    StringIds: Final[IntPtr]
    """"""
    StringIdsSize: Final[int]
    """"""
    def __init__(self) -> None:
        """"""
    @overload
    def Dispose(self) -> None:
        """"""
    @overload
    def Dispose(self, fDisposing: bool) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class MuiResourceTypeIdStringEntryFieldId(Enum):
    """"""

    MuiResourceTypeIdString_StringIds: MuiResourceTypeIdStringEntryFieldId = ...
    """"""
    MuiResourceTypeIdString_StringIdsSize: MuiResourceTypeIdStringEntryFieldId = ...
    """"""
    MuiResourceTypeIdString_IntegerIds: MuiResourceTypeIdStringEntryFieldId = ...
    """"""
    MuiResourceTypeIdString_IntegerIdsSize: MuiResourceTypeIdStringEntryFieldId = ...
    """"""

class PermissionSetEntry(Object):
    """"""

    Id: Final[str]
    """"""
    XmlSegment: Final[str]
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

class PermissionSetEntryFieldId(Enum):
    """"""

    PermissionSet_XmlSegment: PermissionSetEntryFieldId = ...
    """"""

class ProgIdRedirectionEntry(Object):
    """"""

    ProgId: Final[str]
    """"""
    RedirectedGuid: Final[Guid]
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

class ProgIdRedirectionEntryFieldId(Enum):
    """"""

    ProgIdRedirection_RedirectedGuid: ProgIdRedirectionEntryFieldId = ...
    """"""

class ResourceTableMappingEntry(Object):
    """"""

    FinalStringMapped: Final[str]
    """"""
    id: Final[str]
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

class ResourceTableMappingEntryFieldId(Enum):
    """"""

    ResourceTableMapping_FinalStringMapped: ResourceTableMappingEntryFieldId = ...
    """"""

class SubcategoryMembershipEntry(Object):
    """"""

    CategoryMembershipData: Final[ISection]
    """"""
    Subcategory: Final[str]
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

class SubcategoryMembershipEntryFieldId(Enum):
    """"""

    SubcategoryMembership_CategoryMembershipData: SubcategoryMembershipEntryFieldId = ...
    """"""

class WindowClassEntry(Object):
    """"""

    ClassName: Final[str]
    """"""
    HostDll: Final[str]
    """"""
    fVersioned: Final[bool]
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

class WindowClassEntryFieldId(Enum):
    """"""

    WindowClass_HostDll: WindowClassEntryFieldId = ...
    """"""
    WindowClass_fVersioned: WindowClassEntryFieldId = ...
    """"""
