from __future__ import annotations

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

    Codebase: Final[str] = ...
    """
    
    :return: 
    """
    Description: Final[str] = ...
    """
    
    :return: 
    """
    Flags: Final[int] = ...
    """
    
    :return: 
    """
    Group: Final[str] = ...
    """
    
    :return: 
    """
    HashAlgorithm: Final[int] = ...
    """
    
    :return: 
    """
    HashElements: Final[ISection] = ...
    """
    
    :return: 
    """
    HashValue: Final[IntPtr] = ...
    """
    
    :return: 
    """
    HashValueSize: Final[int] = ...
    """
    
    :return: 
    """
    ResourceFallbackCulture: Final[str] = ...
    """
    
    :return: 
    """
    Size: Final[int] = ...
    """
    
    :return: 
    """
    SupportUrl: Final[str] = ...
    """
    
    :return: 
    """
    def __init__(self):
        """"""
    @overload
    def Dispose(self) -> None:
        """"""
    @overload
    def Dispose(self, fDisposing: bool) -> None:
        """

        :param fDisposing:
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
    AssemblyReferenceDependentAssembly_HashValueSize: AssemblyReferenceDependentAssemblyEntryFieldId = (
        ...
    )
    """"""
    AssemblyReferenceDependentAssembly_HashAlgorithm: AssemblyReferenceDependentAssemblyEntryFieldId = (
        ...
    )
    """"""
    AssemblyReferenceDependentAssembly_Flags: AssemblyReferenceDependentAssemblyEntryFieldId = ...
    """"""
    AssemblyReferenceDependentAssembly_ResourceFallbackCulture: AssemblyReferenceDependentAssemblyEntryFieldId = (
        ...
    )
    """"""
    AssemblyReferenceDependentAssembly_Description: AssemblyReferenceDependentAssemblyEntryFieldId = (
        ...
    )
    """"""
    AssemblyReferenceDependentAssembly_SupportUrl: AssemblyReferenceDependentAssemblyEntryFieldId = (
        ...
    )
    """"""
    AssemblyReferenceDependentAssembly_HashElements: AssemblyReferenceDependentAssemblyEntryFieldId = (
        ...
    )
    """"""

class AssemblyReferenceEntry(Object):
    """"""

    DependentAssembly: Final[AssemblyReferenceDependentAssemblyEntry] = ...
    """
    
    :return: 
    """
    Flags: Final[int] = ...
    """
    
    :return: 
    """
    ReferenceIdentity: Final[IReferenceIdentity] = ...
    """
    
    :return: 
    """
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

class AssemblyReferenceEntryFieldId(Enum):
    """"""

    AssemblyReference_Flags: AssemblyReferenceEntryFieldId = ...
    """"""
    AssemblyReference_DependentAssembly: AssemblyReferenceEntryFieldId = ...
    """"""

class AssemblyRequestEntry(Object):
    """"""

    Name: Final[str] = ...
    """
    
    :return: 
    """
    permissionSetID: Final[str] = ...
    """
    
    :return: 
    """
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

class AssemblyRequestEntryFieldId(Enum):
    """"""

    AssemblyRequest_permissionSetID: AssemblyRequestEntryFieldId = ...
    """"""

class CLRSurrogateEntry(Object):
    """"""

    ClassName: Final[str] = ...
    """
    
    :return: 
    """
    Clsid: Final[Guid] = ...
    """
    
    :return: 
    """
    RuntimeVersion: Final[str] = ...
    """
    
    :return: 
    """
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

    CMS_ASSEMBLY_REFERENCE_DEPENDENT_ASSEMBLY_FLAG_OPTIONAL: CMS_ASSEMBLY_REFERENCE_DEPENDENT_ASSEMBLY_FLAG = (
        ...
    )
    """"""
    CMS_ASSEMBLY_REFERENCE_DEPENDENT_ASSEMBLY_FLAG_VISIBLE: CMS_ASSEMBLY_REFERENCE_DEPENDENT_ASSEMBLY_FLAG = (
        ...
    )
    """"""
    CMS_ASSEMBLY_REFERENCE_DEPENDENT_ASSEMBLY_FLAG_PREREQUISITE: CMS_ASSEMBLY_REFERENCE_DEPENDENT_ASSEMBLY_FLAG = (
        ...
    )
    """"""
    CMS_ASSEMBLY_REFERENCE_DEPENDENT_ASSEMBLY_FLAG_RESOURCE_FALLBACK_CULTURE_INTERNAL: CMS_ASSEMBLY_REFERENCE_DEPENDENT_ASSEMBLY_FLAG = (
        ...
    )
    """"""
    CMS_ASSEMBLY_REFERENCE_DEPENDENT_ASSEMBLY_FLAG_INSTALL: CMS_ASSEMBLY_REFERENCE_DEPENDENT_ASSEMBLY_FLAG = (
        ...
    )
    """"""
    CMS_ASSEMBLY_REFERENCE_DEPENDENT_ASSEMBLY_FLAG_ALLOW_DELAYED_BINDING: CMS_ASSEMBLY_REFERENCE_DEPENDENT_ASSEMBLY_FLAG = (
        ...
    )
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

    Clsid: Final[Guid] = ...
    """
    
    :return: 
    """
    ConfiguredGuid: Final[Guid] = ...
    """
    
    :return: 
    """
    Flags: Final[int] = ...
    """
    
    :return: 
    """
    HostFile: Final[str] = ...
    """
    
    :return: 
    """
    ImplementedClsid: Final[Guid] = ...
    """
    
    :return: 
    """
    RuntimeVersion: Final[str] = ...
    """
    
    :return: 
    """
    ThreadingModel: Final[int] = ...
    """
    
    :return: 
    """
    TypeLibrary: Final[Guid] = ...
    """
    
    :return: 
    """
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

    Description: Final[str] = ...
    """
    
    :return: 
    """
    Xml: Final[str] = ...
    """
    
    :return: 
    """
    index: Final[int] = ...
    """
    
    :return: 
    """
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

class CategoryMembershipDataEntryFieldId(Enum):
    """"""

    CategoryMembershipData_Xml: CategoryMembershipDataEntryFieldId = ...
    """"""
    CategoryMembershipData_Description: CategoryMembershipDataEntryFieldId = ...
    """"""

class CategoryMembershipEntry(Object):
    """"""

    Identity: Final[IDefinitionIdentity] = ...
    """
    
    :return: 
    """
    SubcategoryMembership: Final[ISection] = ...
    """
    
    :return: 
    """
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

class CategoryMembershipEntryFieldId(Enum):
    """"""

    CategoryMembership_SubcategoryMembership: CategoryMembershipEntryFieldId = ...
    """"""

class CmsUtils(ABC, Object):
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

class CompatibleFrameworksMetadataEntry(Object):
    """"""

    SupportUrl: Final[str] = ...
    """
    
    :return: 
    """
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

class CompatibleFrameworksMetadataEntryFieldId(Enum):
    """"""

    CompatibleFrameworksMetadata_SupportUrl: CompatibleFrameworksMetadataEntryFieldId = ...
    """"""

class DependentOSMetadataEntry(Object):
    """"""

    BuildNumber: Final[int] = ...
    """
    
    :return: 
    """
    Description: Final[str] = ...
    """
    
    :return: 
    """
    MajorVersion: Final[int] = ...
    """
    
    :return: 
    """
    MinorVersion: Final[int] = ...
    """
    
    :return: 
    """
    ServicePackMajor: Final[int] = ...
    """
    
    :return: 
    """
    ServicePackMinor: Final[int] = ...
    """
    
    :return: 
    """
    SupportUrl: Final[str] = ...
    """
    
    :return: 
    """
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

    DeploymentFlags: Final[int] = ...
    """
    
    :return: 
    """
    DeploymentProviderCodebase: Final[str] = ...
    """
    
    :return: 
    """
    MaximumAge: Final[int] = ...
    """
    
    :return: 
    """
    MaximumAge_Unit: Final[int] = ...
    """
    
    :return: 
    """
    MinimumRequiredVersion: Final[str] = ...
    """
    
    :return: 
    """
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

    ErrorReportUrl: Final[str] = ...
    """
    
    :return: 
    """
    IconFile: Final[str] = ...
    """
    
    :return: 
    """
    Product: Final[str] = ...
    """
    
    :return: 
    """
    Publisher: Final[str] = ...
    """
    
    :return: 
    """
    SuiteName: Final[str] = ...
    """
    
    :return: 
    """
    SupportUrl: Final[str] = ...
    """
    
    :return: 
    """
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

    CommandLine_File: Final[str] = ...
    """
    
    :return: 
    """
    CommandLine_Parameters: Final[str] = ...
    """
    
    :return: 
    """
    Flags: Final[int] = ...
    """
    
    :return: 
    """
    Identity: Final[IReferenceIdentity] = ...
    """
    
    :return: 
    """
    Name: Final[str] = ...
    """
    
    :return: 
    """
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

    DefaultIcon: Final[str] = ...
    """
    
    :return: 
    """
    Description: Final[str] = ...
    """
    
    :return: 
    """
    Extension: Final[str] = ...
    """
    
    :return: 
    """
    Parameter: Final[str] = ...
    """
    
    :return: 
    """
    ProgID: Final[str] = ...
    """
    
    :return: 
    """
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

    Flags: Final[int] = ...
    """
    
    :return: 
    """
    Group: Final[str] = ...
    """
    
    :return: 
    """
    HashAlgorithm: Final[int] = ...
    """
    
    :return: 
    """
    HashElements: Final[ISection] = ...
    """
    
    :return: 
    """
    HashValue: Final[IntPtr] = ...
    """
    
    :return: 
    """
    HashValueSize: Final[int] = ...
    """
    
    :return: 
    """
    ImportPath: Final[str] = ...
    """
    
    :return: 
    """
    LoadFrom: Final[str] = ...
    """
    
    :return: 
    """
    Location: Final[str] = ...
    """
    
    :return: 
    """
    MuiMapping: Final[MuiResourceMapEntry] = ...
    """
    
    :return: 
    """
    Name: Final[str] = ...
    """
    
    :return: 
    """
    Size: Final[int] = ...
    """
    
    :return: 
    """
    SourceName: Final[str] = ...
    """
    
    :return: 
    """
    SourcePath: Final[str] = ...
    """
    
    :return: 
    """
    WritableType: Final[int] = ...
    """
    
    :return: 
    """
    def __init__(self):
        """"""
    @overload
    def Dispose(self) -> None:
        """"""
    @overload
    def Dispose(self, fDisposing: bool) -> None:
        """

        :param fDisposing:
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

    DigestMethod: Final[int] = ...
    """
    
    :return: 
    """
    DigestValue: Final[IntPtr] = ...
    """
    
    :return: 
    """
    DigestValueSize: Final[int] = ...
    """
    
    :return: 
    """
    Transform: Final[int] = ...
    """
    
    :return: 
    """
    TransformMetadata: Final[IntPtr] = ...
    """
    
    :return: 
    """
    TransformMetadataSize: Final[int] = ...
    """
    
    :return: 
    """
    Xml: Final[str] = ...
    """
    
    :return: 
    """
    index: Final[int] = ...
    """
    
    :return: 
    """
    def __init__(self):
        """"""
    @overload
    def Dispose(self) -> None:
        """"""
    @overload
    def Dispose(self, fDisposing: bool) -> None:
        """

        :param fDisposing:
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
        """

        :return:
        """
    @property
    def Codebase(self) -> str:
        """

        :return:
        """
    @property
    def Description(self) -> str:
        """

        :return:
        """
    @property
    def Flags(self) -> int:
        """

        :return:
        """
    @property
    def Group(self) -> str:
        """

        :return:
        """
    @property
    def HashAlgorithm(self) -> int:
        """

        :return:
        """
    @property
    def HashElements(self) -> ISection:
        """

        :return:
        """
    @property
    def HashValue(self) -> object:
        """

        :return:
        """
    @property
    def ResourceFallbackCulture(self) -> str:
        """

        :return:
        """
    @property
    def Size(self) -> int:
        """

        :return:
        """
    @property
    def SupportUrl(self) -> str:
        """

        :return:
        """

class IAssemblyReferenceEntry:
    """"""

    @property
    def AllData(self) -> AssemblyReferenceEntry:
        """

        :return:
        """
    @property
    def DependentAssembly(self) -> IAssemblyReferenceDependentAssemblyEntry:
        """

        :return:
        """
    @property
    def Flags(self) -> int:
        """

        :return:
        """
    @property
    def ReferenceIdentity(self) -> IReferenceIdentity:
        """

        :return:
        """

class IAssemblyRequestEntry:
    """"""

    @property
    def AllData(self) -> AssemblyRequestEntry:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def permissionSetID(self) -> str:
        """

        :return:
        """

class ICLRSurrogateEntry:
    """"""

    @property
    def AllData(self) -> CLRSurrogateEntry:
        """

        :return:
        """
    @property
    def ClassName(self) -> str:
        """

        :return:
        """
    @property
    def Clsid(self) -> Guid:
        """

        :return:
        """
    @property
    def RuntimeVersion(self) -> str:
        """

        :return:
        """

class ICMS:
    """"""

    @property
    def AssemblyReferenceSection(self) -> ISection:
        """

        :return:
        """
    @property
    def AssemblyRequestSection(self) -> ISection:
        """

        :return:
        """
    @property
    def CLRSurrogateSection(self) -> ISection:
        """

        :return:
        """
    @property
    def COMRedirectionSection(self) -> ISection:
        """

        :return:
        """
    @property
    def CategoryMembershipSection(self) -> ISection:
        """

        :return:
        """
    @property
    def CompatibleFrameworksSection(self) -> ISection:
        """

        :return:
        """
    @property
    def CounterSection(self) -> ISection:
        """

        :return:
        """
    @property
    def CounterSetSection(self) -> ISection:
        """

        :return:
        """
    @property
    def DirectorySection(self) -> ISection:
        """

        :return:
        """
    @property
    def EntryPointSection(self) -> ISection:
        """

        :return:
        """
    @property
    def EventMapSection(self) -> ISection:
        """

        :return:
        """
    @property
    def EventSection(self) -> ISection:
        """

        :return:
        """
    @property
    def EventTagSection(self) -> ISection:
        """

        :return:
        """
    @property
    def FileAssociationSection(self) -> ISection:
        """

        :return:
        """
    @property
    def FileSection(self) -> ISection:
        """

        :return:
        """
    @property
    def Identity(self) -> IDefinitionIdentity:
        """

        :return:
        """
    @property
    def MetadataSectionEntry(self) -> ISectionEntry:
        """

        :return:
        """
    @property
    def PermissionSetSection(self) -> ISection:
        """

        :return:
        """
    @property
    def ProgIdRedirectionSection(self) -> ISection:
        """

        :return:
        """
    @property
    def RegistryKeySection(self) -> ISection:
        """

        :return:
        """
    @property
    def StringSection(self) -> ISection:
        """

        :return:
        """
    @property
    def WindowClassSection(self) -> ISection:
        """

        :return:
        """

class ICOMServerEntry:
    """"""

    @property
    def AllData(self) -> COMServerEntry:
        """

        :return:
        """
    @property
    def Clsid(self) -> Guid:
        """

        :return:
        """
    @property
    def ConfiguredGuid(self) -> Guid:
        """

        :return:
        """
    @property
    def Flags(self) -> int:
        """

        :return:
        """
    @property
    def HostFile(self) -> str:
        """

        :return:
        """
    @property
    def ImplementedClsid(self) -> Guid:
        """

        :return:
        """
    @property
    def RuntimeVersion(self) -> str:
        """

        :return:
        """
    @property
    def ThreadingModel(self) -> int:
        """

        :return:
        """
    @property
    def TypeLibrary(self) -> Guid:
        """

        :return:
        """

class ICategoryMembershipDataEntry:
    """"""

    @property
    def AllData(self) -> CategoryMembershipDataEntry:
        """

        :return:
        """
    @property
    def Description(self) -> str:
        """

        :return:
        """
    @property
    def Xml(self) -> str:
        """

        :return:
        """
    @property
    def index(self) -> int:
        """

        :return:
        """

class ICategoryMembershipEntry:
    """"""

    @property
    def AllData(self) -> CategoryMembershipEntry:
        """

        :return:
        """
    @property
    def Identity(self) -> IDefinitionIdentity:
        """

        :return:
        """
    @property
    def SubcategoryMembership(self) -> ISection:
        """

        :return:
        """

class ICompatibleFrameworksMetadataEntry:
    """"""

    @property
    def AllData(self) -> CompatibleFrameworksMetadataEntry:
        """

        :return:
        """
    @property
    def SupportUrl(self) -> str:
        """

        :return:
        """

class IDependentOSMetadataEntry:
    """"""

    @property
    def AllData(self) -> DependentOSMetadataEntry:
        """

        :return:
        """
    @property
    def BuildNumber(self) -> int:
        """

        :return:
        """
    @property
    def Description(self) -> str:
        """

        :return:
        """
    @property
    def MajorVersion(self) -> int:
        """

        :return:
        """
    @property
    def MinorVersion(self) -> int:
        """

        :return:
        """
    @property
    def ServicePackMajor(self) -> int:
        """

        :return:
        """
    @property
    def ServicePackMinor(self) -> int:
        """

        :return:
        """
    @property
    def SupportUrl(self) -> str:
        """

        :return:
        """

class IDeploymentMetadataEntry:
    """"""

    @property
    def AllData(self) -> DeploymentMetadataEntry:
        """

        :return:
        """
    @property
    def DeploymentFlags(self) -> int:
        """

        :return:
        """
    @property
    def DeploymentProviderCodebase(self) -> str:
        """

        :return:
        """
    @property
    def MaximumAge(self) -> int:
        """

        :return:
        """
    @property
    def MaximumAge_Unit(self) -> int:
        """

        :return:
        """
    @property
    def MinimumRequiredVersion(self) -> str:
        """

        :return:
        """

class IDescriptionMetadataEntry:
    """"""

    @property
    def AllData(self) -> DescriptionMetadataEntry:
        """

        :return:
        """
    @property
    def ErrorReportUrl(self) -> str:
        """

        :return:
        """
    @property
    def IconFile(self) -> str:
        """

        :return:
        """
    @property
    def Product(self) -> str:
        """

        :return:
        """
    @property
    def Publisher(self) -> str:
        """

        :return:
        """
    @property
    def SuiteName(self) -> str:
        """

        :return:
        """
    @property
    def SupportUrl(self) -> str:
        """

        :return:
        """

class IEntryPointEntry:
    """"""

    @property
    def AllData(self) -> EntryPointEntry:
        """

        :return:
        """
    @property
    def CommandLine_File(self) -> str:
        """

        :return:
        """
    @property
    def CommandLine_Parameters(self) -> str:
        """

        :return:
        """
    @property
    def Flags(self) -> int:
        """

        :return:
        """
    @property
    def Identity(self) -> IReferenceIdentity:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """

class IFileAssociationEntry:
    """"""

    @property
    def AllData(self) -> FileAssociationEntry:
        """

        :return:
        """
    @property
    def DefaultIcon(self) -> str:
        """

        :return:
        """
    @property
    def Description(self) -> str:
        """

        :return:
        """
    @property
    def Extension(self) -> str:
        """

        :return:
        """
    @property
    def Parameter(self) -> str:
        """

        :return:
        """
    @property
    def ProgID(self) -> str:
        """

        :return:
        """

class IFileEntry:
    """"""

    @property
    def AllData(self) -> FileEntry:
        """

        :return:
        """
    @property
    def Flags(self) -> int:
        """

        :return:
        """
    @property
    def Group(self) -> str:
        """

        :return:
        """
    @property
    def HashAlgorithm(self) -> int:
        """

        :return:
        """
    @property
    def HashElements(self) -> ISection:
        """

        :return:
        """
    @property
    def HashValue(self) -> object:
        """

        :return:
        """
    @property
    def ImportPath(self) -> str:
        """

        :return:
        """
    @property
    def LoadFrom(self) -> str:
        """

        :return:
        """
    @property
    def Location(self) -> str:
        """

        :return:
        """
    @property
    def MuiMapping(self) -> IMuiResourceMapEntry:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Size(self) -> int:
        """

        :return:
        """
    @property
    def SourceName(self) -> str:
        """

        :return:
        """
    @property
    def SourcePath(self) -> str:
        """

        :return:
        """
    @property
    def WritableType(self) -> int:
        """

        :return:
        """

class IHashElementEntry:
    """"""

    @property
    def AllData(self) -> HashElementEntry:
        """

        :return:
        """
    @property
    def DigestMethod(self) -> int:
        """

        :return:
        """
    @property
    def DigestValue(self) -> object:
        """

        :return:
        """
    @property
    def Transform(self) -> int:
        """

        :return:
        """
    @property
    def TransformMetadata(self) -> object:
        """

        :return:
        """
    @property
    def Xml(self) -> str:
        """

        :return:
        """
    @property
    def index(self) -> int:
        """

        :return:
        """

class IMetadataSectionEntry:
    """"""

    @property
    def AllData(self) -> MetadataSectionEntry:
        """

        :return:
        """
    @property
    def CdfIdentity(self) -> IDefinitionIdentity:
        """

        :return:
        """
    @property
    def CompatibleFrameworksData(self) -> ICompatibleFrameworksMetadataEntry:
        """

        :return:
        """
    @property
    def ContentType(self) -> str:
        """

        :return:
        """
    @property
    def DependentOSData(self) -> IDependentOSMetadataEntry:
        """

        :return:
        """
    @property
    def DeploymentData(self) -> IDeploymentMetadataEntry:
        """

        :return:
        """
    @property
    def DescriptionData(self) -> IDescriptionMetadataEntry:
        """

        :return:
        """
    @property
    def HashAlgorithm(self) -> int:
        """

        :return:
        """
    @property
    def KeyInfoElement(self) -> str:
        """

        :return:
        """
    @property
    def LocalPath(self) -> str:
        """

        :return:
        """
    @property
    def ManifestFlags(self) -> int:
        """

        :return:
        """
    @property
    def ManifestHash(self) -> object:
        """

        :return:
        """
    @property
    def MvidValue(self) -> object:
        """

        :return:
        """
    @property
    def RequestedExecutionLevel(self) -> str:
        """

        :return:
        """
    @property
    def RequestedExecutionLevelUIAccess(self) -> bool:
        """

        :return:
        """
    @property
    def ResourceTypeManifestResourcesDependency(self) -> IReferenceIdentity:
        """

        :return:
        """
    @property
    def ResourceTypeResourcesDependency(self) -> IReferenceIdentity:
        """

        :return:
        """
    @property
    def RuntimeImageVersion(self) -> str:
        """

        :return:
        """
    @property
    def SchemaVersion(self) -> int:
        """

        :return:
        """
    @property
    def UsagePatterns(self) -> int:
        """

        :return:
        """
    @property
    def defaultPermissionSetID(self) -> str:
        """

        :return:
        """

class IMuiResourceIdLookupMapEntry:
    """"""

    @property
    def AllData(self) -> MuiResourceIdLookupMapEntry:
        """

        :return:
        """
    @property
    def Count(self) -> int:
        """

        :return:
        """

class IMuiResourceMapEntry:
    """"""

    @property
    def AllData(self) -> MuiResourceMapEntry:
        """

        :return:
        """
    @property
    def ResourceTypeIdInt(self) -> object:
        """

        :return:
        """
    @property
    def ResourceTypeIdString(self) -> object:
        """

        :return:
        """

class IMuiResourceTypeIdIntEntry:
    """"""

    @property
    def AllData(self) -> MuiResourceTypeIdIntEntry:
        """

        :return:
        """
    @property
    def IntegerIds(self) -> object:
        """

        :return:
        """
    @property
    def StringIds(self) -> object:
        """

        :return:
        """

class IMuiResourceTypeIdStringEntry:
    """"""

    @property
    def AllData(self) -> MuiResourceTypeIdStringEntry:
        """

        :return:
        """
    @property
    def IntegerIds(self) -> object:
        """

        :return:
        """
    @property
    def StringIds(self) -> object:
        """

        :return:
        """

class IPermissionSetEntry:
    """"""

    @property
    def AllData(self) -> PermissionSetEntry:
        """

        :return:
        """
    @property
    def Id(self) -> str:
        """

        :return:
        """
    @property
    def XmlSegment(self) -> str:
        """

        :return:
        """

class IProgIdRedirectionEntry:
    """"""

    @property
    def AllData(self) -> ProgIdRedirectionEntry:
        """

        :return:
        """
    @property
    def ProgId(self) -> str:
        """

        :return:
        """
    @property
    def RedirectedGuid(self) -> Guid:
        """

        :return:
        """

class IResourceTableMappingEntry:
    """"""

    @property
    def AllData(self) -> ResourceTableMappingEntry:
        """

        :return:
        """
    @property
    def FinalStringMapped(self) -> str:
        """

        :return:
        """
    @property
    def id(self) -> str:
        """

        :return:
        """

class ISubcategoryMembershipEntry:
    """"""

    @property
    def AllData(self) -> SubcategoryMembershipEntry:
        """

        :return:
        """
    @property
    def CategoryMembershipData(self) -> ISection:
        """

        :return:
        """
    @property
    def Subcategory(self) -> str:
        """

        :return:
        """

class IWindowClassEntry:
    """"""

    @property
    def AllData(self) -> WindowClassEntry:
        """

        :return:
        """
    @property
    def ClassName(self) -> str:
        """

        :return:
        """
    @property
    def HostDll(self) -> str:
        """

        :return:
        """
    @property
    def fVersioned(self) -> bool:
        """

        :return:
        """

class MetadataSectionEntry(Object, IDisposable):
    """"""

    CdfIdentity: Final[IDefinitionIdentity] = ...
    """
    
    :return: 
    """
    CompatibleFrameworksData: Final[CompatibleFrameworksMetadataEntry] = ...
    """
    
    :return: 
    """
    ContentType: Final[str] = ...
    """
    
    :return: 
    """
    DependentOSData: Final[DependentOSMetadataEntry] = ...
    """
    
    :return: 
    """
    DeploymentData: Final[DeploymentMetadataEntry] = ...
    """
    
    :return: 
    """
    DescriptionData: Final[DescriptionMetadataEntry] = ...
    """
    
    :return: 
    """
    HashAlgorithm: Final[int] = ...
    """
    
    :return: 
    """
    KeyInfoElement: Final[str] = ...
    """
    
    :return: 
    """
    LocalPath: Final[str] = ...
    """
    
    :return: 
    """
    ManifestFlags: Final[int] = ...
    """
    
    :return: 
    """
    ManifestHash: Final[IntPtr] = ...
    """
    
    :return: 
    """
    ManifestHashSize: Final[int] = ...
    """
    
    :return: 
    """
    MvidValue: Final[IntPtr] = ...
    """
    
    :return: 
    """
    MvidValueSize: Final[int] = ...
    """
    
    :return: 
    """
    RequestedExecutionLevel: Final[str] = ...
    """
    
    :return: 
    """
    RequestedExecutionLevelUIAccess: Final[bool] = ...
    """
    
    :return: 
    """
    ResourceTypeManifestResourcesDependency: Final[IReferenceIdentity] = ...
    """
    
    :return: 
    """
    ResourceTypeResourcesDependency: Final[IReferenceIdentity] = ...
    """
    
    :return: 
    """
    RuntimeImageVersion: Final[str] = ...
    """
    
    :return: 
    """
    SchemaVersion: Final[int] = ...
    """
    
    :return: 
    """
    UsagePatterns: Final[int] = ...
    """
    
    :return: 
    """
    defaultPermissionSetID: Final[str] = ...
    """
    
    :return: 
    """
    def __init__(self):
        """"""
    @overload
    def Dispose(self) -> None:
        """"""
    @overload
    def Dispose(self, fDisposing: bool) -> None:
        """

        :param fDisposing:
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

    Count: Final[int] = ...
    """
    
    :return: 
    """
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

class MuiResourceIdLookupMapEntryFieldId(Enum):
    """"""

    MuiResourceIdLookupMap_Count: MuiResourceIdLookupMapEntryFieldId = ...
    """"""

class MuiResourceMapEntry(Object, IDisposable):
    """"""

    ResourceTypeIdInt: Final[IntPtr] = ...
    """
    
    :return: 
    """
    ResourceTypeIdIntSize: Final[int] = ...
    """
    
    :return: 
    """
    ResourceTypeIdString: Final[IntPtr] = ...
    """
    
    :return: 
    """
    ResourceTypeIdStringSize: Final[int] = ...
    """
    
    :return: 
    """
    def __init__(self):
        """"""
    @overload
    def Dispose(self) -> None:
        """"""
    @overload
    def Dispose(self, fDisposing: bool) -> None:
        """

        :param fDisposing:
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

    IntegerIds: Final[IntPtr] = ...
    """
    
    :return: 
    """
    IntegerIdsSize: Final[int] = ...
    """
    
    :return: 
    """
    StringIds: Final[IntPtr] = ...
    """
    
    :return: 
    """
    StringIdsSize: Final[int] = ...
    """
    
    :return: 
    """
    def __init__(self):
        """"""
    @overload
    def Dispose(self) -> None:
        """"""
    @overload
    def Dispose(self, fDisposing: bool) -> None:
        """

        :param fDisposing:
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

    IntegerIds: Final[IntPtr] = ...
    """
    
    :return: 
    """
    IntegerIdsSize: Final[int] = ...
    """
    
    :return: 
    """
    StringIds: Final[IntPtr] = ...
    """
    
    :return: 
    """
    StringIdsSize: Final[int] = ...
    """
    
    :return: 
    """
    def __init__(self):
        """"""
    @overload
    def Dispose(self) -> None:
        """"""
    @overload
    def Dispose(self, fDisposing: bool) -> None:
        """

        :param fDisposing:
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

    Id: Final[str] = ...
    """
    
    :return: 
    """
    XmlSegment: Final[str] = ...
    """
    
    :return: 
    """
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

class PermissionSetEntryFieldId(Enum):
    """"""

    PermissionSet_XmlSegment: PermissionSetEntryFieldId = ...
    """"""

class ProgIdRedirectionEntry(Object):
    """"""

    ProgId: Final[str] = ...
    """
    
    :return: 
    """
    RedirectedGuid: Final[Guid] = ...
    """
    
    :return: 
    """
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

class ProgIdRedirectionEntryFieldId(Enum):
    """"""

    ProgIdRedirection_RedirectedGuid: ProgIdRedirectionEntryFieldId = ...
    """"""

class ResourceTableMappingEntry(Object):
    """"""

    FinalStringMapped: Final[str] = ...
    """
    
    :return: 
    """
    id: Final[str] = ...
    """
    
    :return: 
    """
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

class ResourceTableMappingEntryFieldId(Enum):
    """"""

    ResourceTableMapping_FinalStringMapped: ResourceTableMappingEntryFieldId = ...
    """"""

class SubcategoryMembershipEntry(Object):
    """"""

    CategoryMembershipData: Final[ISection] = ...
    """
    
    :return: 
    """
    Subcategory: Final[str] = ...
    """
    
    :return: 
    """
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

class SubcategoryMembershipEntryFieldId(Enum):
    """"""

    SubcategoryMembership_CategoryMembershipData: SubcategoryMembershipEntryFieldId = ...
    """"""

class WindowClassEntry(Object):
    """"""

    ClassName: Final[str] = ...
    """
    
    :return: 
    """
    HostDll: Final[str] = ...
    """
    
    :return: 
    """
    fVersioned: Final[bool] = ...
    """
    
    :return: 
    """
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

class WindowClassEntryFieldId(Enum):
    """"""

    WindowClass_HostDll: WindowClassEntryFieldId = ...
    """"""
    WindowClass_fVersioned: WindowClassEntryFieldId = ...
    """"""
