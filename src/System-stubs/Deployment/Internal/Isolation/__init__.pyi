from __future__ import annotations

from abc import ABC
from typing import List
from typing import Protocol
from typing import Tuple
from typing import Union
from typing import overload

from System import Array
from System import Boolean
from System import Byte
from System import Char
from System import DateTime
from System import Enum
from System import Guid
from System import IDisposable
from System import Int32
from System import Int64
from System import IntPtr
from System import Object
from System import String
from System import UInt16
from System import UInt32
from System import UInt64
from System import UIntPtr
from System import ValueType
from System import Void
from System.Collections import IEnumerator
from System.Deployment.Internal.Isolation.Manifest import ICMS

# ---------- Types ---------- #

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
ByteType = Union[int, Byte]
CharType = Union[str, Char]
IntType = Union[int, Int32]
LongType = Union[int, Int64]
NIntType = Union[int, IntPtr]
NUIntType = Union[int, UIntPtr]
ObjectType = Object
StringType = Union[str, String]
UIntType = Union[int, UInt32]
ULongType = Union[int, UInt64]
UShortType = Union[int, UInt16]
VoidType = Union[None, Void]

# ---------- Classes ---------- #

class IsolationInterop(ABC, ObjectType):
    # ---------- Fields ---------- #

    @staticmethod
    @property
    def GUID_SXS_INSTALL_REFERENCE_SCHEME_OPAQUESTRING() -> Guid: ...
    @staticmethod
    @GUID_SXS_INSTALL_REFERENCE_SCHEME_OPAQUESTRING.setter
    def GUID_SXS_INSTALL_REFERENCE_SCHEME_OPAQUESTRING(value: Guid) -> None: ...
    @staticmethod
    @property
    def IID_ICMS() -> Guid: ...
    @staticmethod
    @IID_ICMS.setter
    def IID_ICMS(value: Guid) -> None: ...
    @staticmethod
    @property
    def IID_IDefinitionIdentity() -> Guid: ...
    @staticmethod
    @IID_IDefinitionIdentity.setter
    def IID_IDefinitionIdentity(value: Guid) -> None: ...
    @staticmethod
    @property
    def IID_IEnumSTORE_ASSEMBLY() -> Guid: ...
    @staticmethod
    @IID_IEnumSTORE_ASSEMBLY.setter
    def IID_IEnumSTORE_ASSEMBLY(value: Guid) -> None: ...
    @staticmethod
    @property
    def IID_IEnumSTORE_ASSEMBLY_FILE() -> Guid: ...
    @staticmethod
    @IID_IEnumSTORE_ASSEMBLY_FILE.setter
    def IID_IEnumSTORE_ASSEMBLY_FILE(value: Guid) -> None: ...
    @staticmethod
    @property
    def IID_IEnumSTORE_CATEGORY() -> Guid: ...
    @staticmethod
    @IID_IEnumSTORE_CATEGORY.setter
    def IID_IEnumSTORE_CATEGORY(value: Guid) -> None: ...
    @staticmethod
    @property
    def IID_IEnumSTORE_CATEGORY_INSTANCE() -> Guid: ...
    @staticmethod
    @IID_IEnumSTORE_CATEGORY_INSTANCE.setter
    def IID_IEnumSTORE_CATEGORY_INSTANCE(value: Guid) -> None: ...
    @staticmethod
    @property
    def IID_IEnumSTORE_DEPLOYMENT_METADATA() -> Guid: ...
    @staticmethod
    @IID_IEnumSTORE_DEPLOYMENT_METADATA.setter
    def IID_IEnumSTORE_DEPLOYMENT_METADATA(value: Guid) -> None: ...
    @staticmethod
    @property
    def IID_IEnumSTORE_DEPLOYMENT_METADATA_PROPERTY() -> Guid: ...
    @staticmethod
    @IID_IEnumSTORE_DEPLOYMENT_METADATA_PROPERTY.setter
    def IID_IEnumSTORE_DEPLOYMENT_METADATA_PROPERTY(value: Guid) -> None: ...
    @staticmethod
    @property
    def IID_IManifestInformation() -> Guid: ...
    @staticmethod
    @IID_IManifestInformation.setter
    def IID_IManifestInformation(value: Guid) -> None: ...
    @staticmethod
    @property
    def IID_IStore() -> Guid: ...
    @staticmethod
    @IID_IStore.setter
    def IID_IStore(value: Guid) -> None: ...
    @staticmethod
    @property
    def IsolationDllName() -> StringType: ...
    @staticmethod
    @property
    def SXS_INSTALL_REFERENCE_SCHEME_SXS_STRONGNAME_SIGNED_PRIVATE_ASSEMBLY() -> Guid: ...
    @staticmethod
    @SXS_INSTALL_REFERENCE_SCHEME_SXS_STRONGNAME_SIGNED_PRIVATE_ASSEMBLY.setter
    def SXS_INSTALL_REFERENCE_SCHEME_SXS_STRONGNAME_SIGNED_PRIVATE_ASSEMBLY(
        value: Guid,
    ) -> None: ...

    # No Constructors

    # ---------- Properties ---------- #

    @staticmethod
    @property
    def AppIdAuthority() -> IAppIdAuthority: ...
    @staticmethod
    @property
    def IdentityAuthority() -> IIdentityAuthority: ...

    # ---------- Methods ---------- #

    @staticmethod
    def GetUserStore() -> Store: ...
    @staticmethod
    def get_AppIdAuthority() -> IAppIdAuthority: ...
    @staticmethod
    def get_IdentityAuthority() -> IIdentityAuthority: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class Store(ObjectType):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, pStore: IStore): ...

    # ---------- Properties ---------- #

    @property
    def InternalStore(self) -> IStore: ...

    # ---------- Methods ---------- #

    def BindReferenceToAssemblyIdentity(
        self,
        Flags: UIntType,
        ReferenceIdentity: IReferenceIdentity,
        cDeploymentsToIgnore: UIntType,
        DefinitionIdentity_DeploymentsToIgnore: ArrayType[IDefinitionIdentity],
    ) -> IDefinitionIdentity: ...
    def BindReferenceToAssemblyManifest(
        self,
        Flags: UIntType,
        ReferenceIdentity: IReferenceIdentity,
        cDeploymentsToIgnore: UIntType,
        DefinitionIdentity_DeploymentsToIgnore: ArrayType[IDefinitionIdentity],
    ) -> ICMS: ...
    def CalculateDelimiterOfDeploymentsBasedOnQuota(
        self,
        dwFlags: UIntType,
        cDeployments: UIntType,
        rgpIDefinitionAppId_Deployments: ArrayType[IDefinitionAppId],
        InstallerReference: StoreApplicationReference,
        ulonglongQuota: ULongType,
        Delimiter: UIntType,
        SizeSharedWithExternalDeployment: ULongType,
        SizeConsumedByInputDeploymentArray: ULongType,
    ) -> Tuple[VoidType, StoreApplicationReference, UIntType, ULongType, ULongType]: ...
    @overload
    def EnumAssemblies(self, Flags: EnumAssembliesFlags) -> StoreAssemblyEnumeration: ...
    @overload
    def EnumAssemblies(
        self, Flags: EnumAssembliesFlags, refToMatch: IReferenceIdentity
    ) -> StoreAssemblyEnumeration: ...
    def EnumCategories(
        self, Flags: EnumCategoriesFlags, CategoryMatch: IReferenceIdentity
    ) -> StoreCategoryEnumeration: ...
    def EnumCategoryInstances(
        self, Flags: EnumCategoryInstancesFlags, Category: IDefinitionIdentity, SubCat: StringType
    ) -> StoreCategoryInstanceEnumeration: ...
    def EnumFiles(
        self, Flags: EnumAssemblyFilesFlags, Assembly: IDefinitionIdentity
    ) -> StoreAssemblyFileEnumeration: ...
    def EnumInstallationReferences(
        self, Flags: EnumAssemblyInstallReferenceFlags, Assembly: IDefinitionIdentity
    ) -> IEnumSTORE_ASSEMBLY_INSTALLATION_REFERENCE: ...
    def EnumInstallerDeploymentProperties(
        self,
        InstallerId: Guid,
        InstallerName: StringType,
        InstallerMetadata: StringType,
        Deployment: IDefinitionAppId,
    ) -> StoreDeploymentMetadataPropertyEnumeration: ...
    def EnumInstallerDeployments(
        self,
        InstallerId: Guid,
        InstallerName: StringType,
        InstallerMetadata: StringType,
        DeploymentFilter: IReferenceAppId,
    ) -> StoreDeploymentMetadataEnumeration: ...
    def EnumPrivateFiles(
        self,
        Flags: EnumApplicationPrivateFiles,
        Application: IDefinitionAppId,
        Assembly: IDefinitionIdentity,
    ) -> StoreAssemblyFileEnumeration: ...
    @overload
    def EnumSubcategories(
        self, Flags: EnumSubcategoriesFlags, CategoryMatch: IDefinitionIdentity
    ) -> StoreSubcategoryEnumeration: ...
    @overload
    def EnumSubcategories(
        self,
        Flags: EnumSubcategoriesFlags,
        Category: IDefinitionIdentity,
        SearchPattern: StringType,
    ) -> StoreSubcategoryEnumeration: ...
    def GetAssemblyIdentity(
        self, Flags: UIntType, DefinitionIdentity: IDefinitionIdentity
    ) -> IDefinitionIdentity: ...
    def GetAssemblyManifest(
        self, Flags: UIntType, DefinitionIdentity: IDefinitionIdentity
    ) -> ICMS: ...
    def GetDeploymentProperty(
        self,
        Flags: GetPackagePropertyFlags,
        Deployment: IDefinitionAppId,
        Reference: StoreApplicationReference,
        PropertySet: Guid,
        PropertyName: StringType,
    ) -> ArrayType[ByteType]: ...
    def LockApplicationPath(self, app: IDefinitionAppId) -> IPathLock: ...
    def LockAssemblyPath(self, asm: IDefinitionIdentity) -> IPathLock: ...
    def QueryChangeID(self, asm: IDefinitionIdentity) -> ULongType: ...
    def Transact(self, operations: ArrayType[StoreTransactionOperation]) -> ArrayType[UIntType]: ...
    def get_InternalStore(self) -> IStore: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # ---------- Sub Interfaces ---------- #

    # ---------- Sub Enums ---------- #

    class EnumAssembliesFlags(Enum):
        Nothing = 0
        VisibleOnly = 1
        MatchServicing = 2
        ForceLibrarySemantics = 4

    class EnumAssemblyFilesFlags(Enum):
        Nothing = 0
        IncludeInstalled = 1
        IncludeMissing = 2

    class EnumApplicationPrivateFiles(Enum):
        Nothing = 0
        IncludeInstalled = 1
        IncludeMissing = 2

    class EnumAssemblyInstallReferenceFlags(Enum):
        Nothing = 0

    class EnumCategoriesFlags(Enum):
        Nothing = 0

    class EnumSubcategoriesFlags(Enum):
        Nothing = 0

    class EnumCategoryInstancesFlags(Enum):
        Nothing = 0

    class GetPackagePropertyFlags(Enum):
        Nothing = 0

class StoreAssemblyEnumeration(ObjectType, IEnumerator):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, pI: IEnumSTORE_ASSEMBLY): ...

    # ---------- Properties ---------- #

    @property
    def Current(self) -> STORE_ASSEMBLY: ...

    # ---------- Methods ---------- #

    def GetEnumerator(self) -> IEnumerator: ...
    def MoveNext(self) -> BooleanType: ...
    def Reset(self) -> VoidType: ...
    def get_Current(self) -> STORE_ASSEMBLY: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class StoreAssemblyFileEnumeration(ObjectType, IEnumerator):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, pI: IEnumSTORE_ASSEMBLY_FILE): ...

    # ---------- Properties ---------- #

    @property
    def Current(self) -> STORE_ASSEMBLY_FILE: ...

    # ---------- Methods ---------- #

    def GetEnumerator(self) -> IEnumerator: ...
    def MoveNext(self) -> BooleanType: ...
    def Reset(self) -> VoidType: ...
    def get_Current(self) -> STORE_ASSEMBLY_FILE: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class StoreCategoryEnumeration(ObjectType, IEnumerator):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, pI: IEnumSTORE_CATEGORY): ...

    # ---------- Properties ---------- #

    @property
    def Current(self) -> STORE_CATEGORY: ...

    # ---------- Methods ---------- #

    def GetEnumerator(self) -> IEnumerator: ...
    def MoveNext(self) -> BooleanType: ...
    def Reset(self) -> VoidType: ...
    def get_Current(self) -> STORE_CATEGORY: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class StoreCategoryInstanceEnumeration(ObjectType, IEnumerator):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, pI: IEnumSTORE_CATEGORY_INSTANCE): ...

    # ---------- Properties ---------- #

    @property
    def Current(self) -> STORE_CATEGORY_INSTANCE: ...

    # ---------- Methods ---------- #

    def GetEnumerator(self) -> IEnumerator: ...
    def MoveNext(self) -> BooleanType: ...
    def Reset(self) -> VoidType: ...
    def get_Current(self) -> STORE_CATEGORY_INSTANCE: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class StoreDeploymentMetadataEnumeration(ObjectType, IEnumerator):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, pI: IEnumSTORE_DEPLOYMENT_METADATA): ...

    # ---------- Properties ---------- #

    @property
    def Current(self) -> IDefinitionAppId: ...

    # ---------- Methods ---------- #

    def GetEnumerator(self) -> IEnumerator: ...
    def MoveNext(self) -> BooleanType: ...
    def Reset(self) -> VoidType: ...
    def get_Current(self) -> IDefinitionAppId: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class StoreDeploymentMetadataPropertyEnumeration(ObjectType, IEnumerator):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, pI: IEnumSTORE_DEPLOYMENT_METADATA_PROPERTY): ...

    # ---------- Properties ---------- #

    @property
    def Current(self) -> StoreOperationMetadataProperty: ...

    # ---------- Methods ---------- #

    def GetEnumerator(self) -> IEnumerator: ...
    def MoveNext(self) -> BooleanType: ...
    def Reset(self) -> VoidType: ...
    def get_Current(self) -> StoreOperationMetadataProperty: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class StoreSubcategoryEnumeration(ObjectType, IEnumerator):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, pI: IEnumSTORE_CATEGORY_SUBCATEGORY): ...

    # ---------- Properties ---------- #

    @property
    def Current(self) -> STORE_CATEGORY_SUBCATEGORY: ...

    # ---------- Methods ---------- #

    def GetEnumerator(self) -> IEnumerator: ...
    def MoveNext(self) -> BooleanType: ...
    def Reset(self) -> VoidType: ...
    def get_Current(self) -> STORE_CATEGORY_SUBCATEGORY: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class StoreTransaction(ObjectType, IDisposable):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # ---------- Properties ---------- #

    @property
    def Operations(self) -> ArrayType[StoreTransactionOperation]: ...

    # ---------- Methods ---------- #

    @overload
    def Add(self, o: StoreOperationInstallDeployment) -> VoidType: ...
    @overload
    def Add(self, o: StoreOperationPinDeployment) -> VoidType: ...
    @overload
    def Add(self, o: StoreOperationSetCanonicalizationContext) -> VoidType: ...
    @overload
    def Add(self, o: StoreOperationSetDeploymentMetadata) -> VoidType: ...
    @overload
    def Add(self, o: StoreOperationStageComponent) -> VoidType: ...
    @overload
    def Add(self, o: StoreOperationStageComponentFile) -> VoidType: ...
    @overload
    def Add(self, o: StoreOperationUninstallDeployment) -> VoidType: ...
    @overload
    def Add(self, o: StoreOperationUnpinDeployment) -> VoidType: ...
    @overload
    def Add(self, o: StoreOperationScavenge) -> VoidType: ...
    def get_Operations(self) -> ArrayType[StoreTransactionOperation]: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

# ---------- Structs ---------- #

class BLOB(ValueType, IDisposable):
    # ---------- Fields ---------- #

    @property
    def BlobData(self) -> NIntType: ...
    @BlobData.setter
    def BlobData(self, value: NIntType) -> None: ...
    @property
    def Size(self) -> UIntType: ...
    @Size.setter
    def Size(self, value: UIntType) -> None: ...

    # No Constructors

    # No Properties

    # ---------- Methods ---------- #

    def Dispose(self) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class CATEGORY(ValueType):
    # ---------- Fields ---------- #

    @property
    def DefinitionIdentity(self) -> IDefinitionIdentity: ...
    @DefinitionIdentity.setter
    def DefinitionIdentity(self, value: IDefinitionIdentity) -> None: ...

    # No Constructors

    # No Properties

    # No Methods

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class CATEGORY_INSTANCE(ValueType):
    # ---------- Fields ---------- #

    @property
    def DefinitionAppId_Application(self) -> IDefinitionAppId: ...
    @DefinitionAppId_Application.setter
    def DefinitionAppId_Application(self, value: IDefinitionAppId) -> None: ...
    @property
    def XMLSnippet(self) -> StringType: ...
    @XMLSnippet.setter
    def XMLSnippet(self, value: StringType) -> None: ...

    # No Constructors

    # No Properties

    # No Methods

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class CATEGORY_SUBCATEGORY(ValueType):
    # ---------- Fields ---------- #

    @property
    def Subcategory(self) -> StringType: ...
    @Subcategory.setter
    def Subcategory(self, value: StringType) -> None: ...

    # No Constructors

    # No Properties

    # No Methods

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class IDENTITY_ATTRIBUTE(ValueType):
    # ---------- Fields ---------- #

    @property
    def Name(self) -> StringType: ...
    @Name.setter
    def Name(self, value: StringType) -> None: ...
    @property
    def Namespace(self) -> StringType: ...
    @Namespace.setter
    def Namespace(self, value: StringType) -> None: ...
    @property
    def Value(self) -> StringType: ...
    @Value.setter
    def Value(self, value: StringType) -> None: ...

    # No Constructors

    # No Properties

    # No Methods

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class IStore_BindingResult(ValueType):
    # ---------- Fields ---------- #

    @property
    def CacheCoherencyGuid(self) -> Guid: ...
    @CacheCoherencyGuid.setter
    def CacheCoherencyGuid(self, value: Guid) -> None: ...
    @property
    def Component(self) -> IStore_BindingResult_BoundVersion: ...
    @Component.setter
    def Component(self, value: IStore_BindingResult_BoundVersion) -> None: ...
    @property
    def Disposition(self) -> UIntType: ...
    @Disposition.setter
    def Disposition(self, value: UIntType) -> None: ...
    @property
    def Flags(self) -> UIntType: ...
    @Flags.setter
    def Flags(self, value: UIntType) -> None: ...
    @property
    def Reserved(self) -> NIntType: ...
    @Reserved.setter
    def Reserved(self, value: NIntType) -> None: ...

    # No Constructors

    # No Properties

    # No Methods

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class IStore_BindingResult_BoundVersion(ValueType):
    # ---------- Fields ---------- #

    @property
    def Build(self) -> UShortType: ...
    @Build.setter
    def Build(self, value: UShortType) -> None: ...
    @property
    def Major(self) -> UShortType: ...
    @Major.setter
    def Major(self, value: UShortType) -> None: ...
    @property
    def Minor(self) -> UShortType: ...
    @Minor.setter
    def Minor(self, value: UShortType) -> None: ...
    @property
    def Revision(self) -> UShortType: ...
    @Revision.setter
    def Revision(self, value: UShortType) -> None: ...

    # No Constructors

    # No Properties

    # No Methods

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class STORE_ASSEMBLY(ValueType):
    # ---------- Fields ---------- #

    @property
    def AssemblySize(self) -> ULongType: ...
    @AssemblySize.setter
    def AssemblySize(self, value: ULongType) -> None: ...
    @property
    def ChangeId(self) -> ULongType: ...
    @ChangeId.setter
    def ChangeId(self, value: ULongType) -> None: ...
    @property
    def DefinitionIdentity(self) -> IDefinitionIdentity: ...
    @DefinitionIdentity.setter
    def DefinitionIdentity(self, value: IDefinitionIdentity) -> None: ...
    @property
    def ManifestPath(self) -> StringType: ...
    @ManifestPath.setter
    def ManifestPath(self, value: StringType) -> None: ...
    @property
    def Status(self) -> UIntType: ...
    @Status.setter
    def Status(self, value: UIntType) -> None: ...

    # No Constructors

    # No Properties

    # No Methods

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class STORE_ASSEMBLY_FILE(ValueType):
    # ---------- Fields ---------- #

    @property
    def FileName(self) -> StringType: ...
    @FileName.setter
    def FileName(self, value: StringType) -> None: ...
    @property
    def FileStatusFlags(self) -> UIntType: ...
    @FileStatusFlags.setter
    def FileStatusFlags(self, value: UIntType) -> None: ...
    @property
    def Flags(self) -> UIntType: ...
    @Flags.setter
    def Flags(self, value: UIntType) -> None: ...
    @property
    def Size(self) -> UIntType: ...
    @Size.setter
    def Size(self, value: UIntType) -> None: ...

    # No Constructors

    # No Properties

    # No Methods

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class STORE_CATEGORY(ValueType):
    # ---------- Fields ---------- #

    @property
    def DefinitionIdentity(self) -> IDefinitionIdentity: ...
    @DefinitionIdentity.setter
    def DefinitionIdentity(self, value: IDefinitionIdentity) -> None: ...

    # No Constructors

    # No Properties

    # No Methods

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class STORE_CATEGORY_INSTANCE(ValueType):
    # ---------- Fields ---------- #

    @property
    def DefinitionAppId_Application(self) -> IDefinitionAppId: ...
    @DefinitionAppId_Application.setter
    def DefinitionAppId_Application(self, value: IDefinitionAppId) -> None: ...
    @property
    def XMLSnippet(self) -> StringType: ...
    @XMLSnippet.setter
    def XMLSnippet(self, value: StringType) -> None: ...

    # No Constructors

    # No Properties

    # No Methods

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class STORE_CATEGORY_SUBCATEGORY(ValueType):
    # ---------- Fields ---------- #

    @property
    def Subcategory(self) -> StringType: ...
    @Subcategory.setter
    def Subcategory(self, value: StringType) -> None: ...

    # No Constructors

    # No Properties

    # No Methods

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class StoreApplicationReference(ValueType):
    # ---------- Fields ---------- #

    @property
    def Flags(self) -> RefFlags: ...
    @Flags.setter
    def Flags(self, value: RefFlags) -> None: ...
    @property
    def GuidScheme(self) -> Guid: ...
    @GuidScheme.setter
    def GuidScheme(self, value: Guid) -> None: ...
    @property
    def Identifier(self) -> StringType: ...
    @Identifier.setter
    def Identifier(self, value: StringType) -> None: ...
    @property
    def NonCanonicalData(self) -> StringType: ...
    @NonCanonicalData.setter
    def NonCanonicalData(self, value: StringType) -> None: ...
    @property
    def Size(self) -> UIntType: ...
    @Size.setter
    def Size(self, value: UIntType) -> None: ...

    # ---------- Constructors ---------- #

    def __init__(self, RefScheme: Guid, Id: StringType, NcData: StringType): ...

    # No Properties

    # ---------- Methods ---------- #

    @staticmethod
    def Destroy(ip: NIntType) -> VoidType: ...
    def ToIntPtr(self) -> NIntType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # ---------- Sub Enums ---------- #

    class RefFlags(Enum):
        Nothing = 0

class StoreOperationInstallDeployment(ValueType):
    # ---------- Fields ---------- #

    @property
    def Application(self) -> IDefinitionAppId: ...
    @Application.setter
    def Application(self, value: IDefinitionAppId) -> None: ...
    @property
    def Flags(self) -> OpFlags: ...
    @Flags.setter
    def Flags(self, value: OpFlags) -> None: ...
    @property
    def Reference(self) -> NIntType: ...
    @Reference.setter
    def Reference(self, value: NIntType) -> None: ...
    @property
    def Size(self) -> UIntType: ...
    @Size.setter
    def Size(self, value: UIntType) -> None: ...

    # ---------- Constructors ---------- #

    @overload
    def __init__(self, App: IDefinitionAppId, reference: StoreApplicationReference): ...
    @overload
    def __init__(
        self,
        App: IDefinitionAppId,
        UninstallOthers: BooleanType,
        reference: StoreApplicationReference,
    ): ...

    # No Properties

    # ---------- Methods ---------- #

    def Destroy(self) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # ---------- Sub Enums ---------- #

    class OpFlags(Enum):
        Nothing = 0
        UninstallOthers = 1

    class Disposition(Enum):
        Failed = 0
        AlreadyInstalled = 1
        Installed = 2

class StoreOperationMetadataProperty(ValueType):
    # ---------- Fields ---------- #

    @property
    def GuidPropertySet(self) -> Guid: ...
    @GuidPropertySet.setter
    def GuidPropertySet(self, value: Guid) -> None: ...
    @property
    def Name(self) -> StringType: ...
    @Name.setter
    def Name(self, value: StringType) -> None: ...
    @property
    def Value(self) -> StringType: ...
    @Value.setter
    def Value(self, value: StringType) -> None: ...
    @property
    def ValueSize(self) -> NIntType: ...
    @ValueSize.setter
    def ValueSize(self, value: NIntType) -> None: ...

    # ---------- Constructors ---------- #

    @overload
    def __init__(self, PropertySet: Guid, Name: StringType): ...
    @overload
    def __init__(self, PropertySet: Guid, Name: StringType, Value: StringType): ...

    # No Properties

    # No Methods

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class StoreOperationPinDeployment(ValueType):
    # ---------- Fields ---------- #

    @property
    def Application(self) -> IDefinitionAppId: ...
    @Application.setter
    def Application(self, value: IDefinitionAppId) -> None: ...
    @property
    def ExpirationTime(self) -> LongType: ...
    @ExpirationTime.setter
    def ExpirationTime(self, value: LongType) -> None: ...
    @property
    def Flags(self) -> OpFlags: ...
    @Flags.setter
    def Flags(self, value: OpFlags) -> None: ...
    @property
    def Reference(self) -> NIntType: ...
    @Reference.setter
    def Reference(self, value: NIntType) -> None: ...
    @property
    def Size(self) -> UIntType: ...
    @Size.setter
    def Size(self, value: UIntType) -> None: ...

    # ---------- Constructors ---------- #

    @overload
    def __init__(self, AppId: IDefinitionAppId, Ref: StoreApplicationReference): ...
    @overload
    def __init__(
        self, AppId: IDefinitionAppId, Expiry: DateTime, Ref: StoreApplicationReference
    ): ...

    # No Properties

    # ---------- Methods ---------- #

    def Destroy(self) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # ---------- Sub Enums ---------- #

    class OpFlags(Enum):
        Nothing = 0
        NeverExpires = 1

    class Disposition(Enum):
        Failed = 0
        Pinned = 1

class StoreOperationScavenge(ValueType):
    # ---------- Fields ---------- #

    @property
    def ComponentCountLimit(self) -> UIntType: ...
    @ComponentCountLimit.setter
    def ComponentCountLimit(self, value: UIntType) -> None: ...
    @property
    def Flags(self) -> OpFlags: ...
    @Flags.setter
    def Flags(self, value: OpFlags) -> None: ...
    @property
    def RuntimeLimit(self) -> ULongType: ...
    @RuntimeLimit.setter
    def RuntimeLimit(self, value: ULongType) -> None: ...
    @property
    def Size(self) -> UIntType: ...
    @Size.setter
    def Size(self, value: UIntType) -> None: ...
    @property
    def SizeReclaimationLimit(self) -> ULongType: ...
    @SizeReclaimationLimit.setter
    def SizeReclaimationLimit(self, value: ULongType) -> None: ...

    # ---------- Constructors ---------- #

    @overload
    def __init__(
        self,
        Light: BooleanType,
        SizeLimit: ULongType,
        RunLimit: ULongType,
        ComponentLimit: UIntType,
    ): ...
    @overload
    def __init__(self, Light: BooleanType): ...

    # No Properties

    # ---------- Methods ---------- #

    def Destroy(self) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # ---------- Sub Enums ---------- #

    class OpFlags(Enum):
        Nothing = 0
        Light = 1
        LimitSize = 2
        LimitTime = 4
        LimitCount = 8

class StoreOperationSetCanonicalizationContext(ValueType):
    # ---------- Fields ---------- #

    @property
    def BaseAddressFilePath(self) -> StringType: ...
    @BaseAddressFilePath.setter
    def BaseAddressFilePath(self, value: StringType) -> None: ...
    @property
    def ExportsFilePath(self) -> StringType: ...
    @ExportsFilePath.setter
    def ExportsFilePath(self, value: StringType) -> None: ...
    @property
    def Flags(self) -> OpFlags: ...
    @Flags.setter
    def Flags(self, value: OpFlags) -> None: ...
    @property
    def Size(self) -> UIntType: ...
    @Size.setter
    def Size(self, value: UIntType) -> None: ...

    # ---------- Constructors ---------- #

    def __init__(self, Bases: StringType, Exports: StringType): ...

    # No Properties

    # ---------- Methods ---------- #

    def Destroy(self) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # ---------- Sub Enums ---------- #

    class OpFlags(Enum):
        Nothing = 0

class StoreOperationSetDeploymentMetadata(ValueType):
    # ---------- Fields ---------- #

    @property
    def Deployment(self) -> IDefinitionAppId: ...
    @Deployment.setter
    def Deployment(self, value: IDefinitionAppId) -> None: ...
    @property
    def Flags(self) -> OpFlags: ...
    @Flags.setter
    def Flags(self, value: OpFlags) -> None: ...
    @property
    def InstallerReference(self) -> NIntType: ...
    @InstallerReference.setter
    def InstallerReference(self, value: NIntType) -> None: ...
    @property
    def PropertiesToSet(self) -> NIntType: ...
    @PropertiesToSet.setter
    def PropertiesToSet(self, value: NIntType) -> None: ...
    @property
    def PropertiesToTest(self) -> NIntType: ...
    @PropertiesToTest.setter
    def PropertiesToTest(self, value: NIntType) -> None: ...
    @property
    def Size(self) -> UIntType: ...
    @Size.setter
    def Size(self, value: UIntType) -> None: ...
    @property
    def cPropertiesToSet(self) -> NIntType: ...
    @cPropertiesToSet.setter
    def cPropertiesToSet(self, value: NIntType) -> None: ...
    @property
    def cPropertiesToTest(self) -> NIntType: ...
    @cPropertiesToTest.setter
    def cPropertiesToTest(self, value: NIntType) -> None: ...

    # ---------- Constructors ---------- #

    @overload
    def __init__(
        self,
        Deployment: IDefinitionAppId,
        Reference: StoreApplicationReference,
        SetProperties: ArrayType[StoreOperationMetadataProperty],
    ): ...
    @overload
    def __init__(
        self,
        Deployment: IDefinitionAppId,
        Reference: StoreApplicationReference,
        SetProperties: ArrayType[StoreOperationMetadataProperty],
        TestProperties: ArrayType[StoreOperationMetadataProperty],
    ): ...

    # No Properties

    # ---------- Methods ---------- #

    def Destroy(self) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # ---------- Sub Enums ---------- #

    class OpFlags(Enum):
        Nothing = 0

    class Disposition(Enum):
        Failed = 0
        Set = 2

class StoreOperationStageComponent(ValueType):
    # ---------- Fields ---------- #

    @property
    def Application(self) -> IDefinitionAppId: ...
    @Application.setter
    def Application(self, value: IDefinitionAppId) -> None: ...
    @property
    def Component(self) -> IDefinitionIdentity: ...
    @Component.setter
    def Component(self, value: IDefinitionIdentity) -> None: ...
    @property
    def Flags(self) -> OpFlags: ...
    @Flags.setter
    def Flags(self, value: OpFlags) -> None: ...
    @property
    def ManifestPath(self) -> StringType: ...
    @ManifestPath.setter
    def ManifestPath(self, value: StringType) -> None: ...
    @property
    def Size(self) -> UIntType: ...
    @Size.setter
    def Size(self, value: UIntType) -> None: ...

    # ---------- Constructors ---------- #

    @overload
    def __init__(self, app: IDefinitionAppId, Manifest: StringType): ...
    @overload
    def __init__(self, app: IDefinitionAppId, comp: IDefinitionIdentity, Manifest: StringType): ...

    # No Properties

    # ---------- Methods ---------- #

    def Destroy(self) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # ---------- Sub Enums ---------- #

    class OpFlags(Enum):
        Nothing = 0

    class Disposition(Enum):
        Failed = 0
        Installed = 1
        Refreshed = 2
        AlreadyInstalled = 3

class StoreOperationStageComponentFile(ValueType):
    # ---------- Fields ---------- #

    @property
    def Application(self) -> IDefinitionAppId: ...
    @Application.setter
    def Application(self, value: IDefinitionAppId) -> None: ...
    @property
    def Component(self) -> IDefinitionIdentity: ...
    @Component.setter
    def Component(self, value: IDefinitionIdentity) -> None: ...
    @property
    def ComponentRelativePath(self) -> StringType: ...
    @ComponentRelativePath.setter
    def ComponentRelativePath(self, value: StringType) -> None: ...
    @property
    def Flags(self) -> OpFlags: ...
    @Flags.setter
    def Flags(self, value: OpFlags) -> None: ...
    @property
    def Size(self) -> UIntType: ...
    @Size.setter
    def Size(self, value: UIntType) -> None: ...
    @property
    def SourceFilePath(self) -> StringType: ...
    @SourceFilePath.setter
    def SourceFilePath(self, value: StringType) -> None: ...

    # ---------- Constructors ---------- #

    @overload
    def __init__(self, App: IDefinitionAppId, CompRelPath: StringType, SrcFile: StringType): ...
    @overload
    def __init__(
        self,
        App: IDefinitionAppId,
        Component: IDefinitionIdentity,
        CompRelPath: StringType,
        SrcFile: StringType,
    ): ...

    # No Properties

    # ---------- Methods ---------- #

    def Destroy(self) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # ---------- Sub Enums ---------- #

    class OpFlags(Enum):
        Nothing = 0

    class Disposition(Enum):
        Failed = 0
        Installed = 1
        Refreshed = 2
        AlreadyInstalled = 3

class StoreOperationUninstallDeployment(ValueType):
    # ---------- Fields ---------- #

    @property
    def Application(self) -> IDefinitionAppId: ...
    @Application.setter
    def Application(self, value: IDefinitionAppId) -> None: ...
    @property
    def Flags(self) -> OpFlags: ...
    @Flags.setter
    def Flags(self, value: OpFlags) -> None: ...
    @property
    def Reference(self) -> NIntType: ...
    @Reference.setter
    def Reference(self, value: NIntType) -> None: ...
    @property
    def Size(self) -> UIntType: ...
    @Size.setter
    def Size(self, value: UIntType) -> None: ...

    # ---------- Constructors ---------- #

    def __init__(self, appid: IDefinitionAppId, AppRef: StoreApplicationReference): ...

    # No Properties

    # ---------- Methods ---------- #

    def Destroy(self) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # ---------- Sub Enums ---------- #

    class OpFlags(Enum):
        Nothing = 0

    class Disposition(Enum):
        Failed = 0
        DidNotExist = 1
        Uninstalled = 2

class StoreOperationUnpinDeployment(ValueType):
    # ---------- Fields ---------- #

    @property
    def Application(self) -> IDefinitionAppId: ...
    @Application.setter
    def Application(self, value: IDefinitionAppId) -> None: ...
    @property
    def Flags(self) -> OpFlags: ...
    @Flags.setter
    def Flags(self, value: OpFlags) -> None: ...
    @property
    def Reference(self) -> NIntType: ...
    @Reference.setter
    def Reference(self, value: NIntType) -> None: ...
    @property
    def Size(self) -> UIntType: ...
    @Size.setter
    def Size(self, value: UIntType) -> None: ...

    # ---------- Constructors ---------- #

    def __init__(self, app: IDefinitionAppId, reference: StoreApplicationReference): ...

    # No Properties

    # ---------- Methods ---------- #

    def Destroy(self) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # ---------- Sub Enums ---------- #

    class OpFlags(Enum):
        Nothing = 0

    class Disposition(Enum):
        Failed = 0
        Unpinned = 1

class StoreTransactionData(ValueType):
    # ---------- Fields ---------- #

    @property
    def DataPtr(self) -> NIntType: ...
    @DataPtr.setter
    def DataPtr(self, value: NIntType) -> None: ...

    # No Constructors

    # No Properties

    # No Methods

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class StoreTransactionOperation(ValueType):
    # ---------- Fields ---------- #

    @property
    def Data(self) -> StoreTransactionData: ...
    @Data.setter
    def Data(self, value: StoreTransactionData) -> None: ...
    @property
    def Operation(self) -> StoreTransactionOperationType: ...
    @Operation.setter
    def Operation(self, value: StoreTransactionOperationType) -> None: ...

    # No Constructors

    # No Properties

    # No Methods

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

# ---------- Interfaces ---------- #

class IActContext(Protocol):
    # No Properties

    # ---------- Methods ---------- #

    def ApplicationBasePath(
        self, Flags: UIntType, ApplicationPath: StringType
    ) -> Tuple[VoidType, StringType]: ...
    def CreateActContextFromCategoryInstance(
        self,
        dwFlags: UIntType,
        CategoryInstance: CATEGORY_INSTANCE,
        ppCreatedAppContext: ObjectType,
    ) -> Tuple[VoidType, CATEGORY_INSTANCE, ObjectType]: ...
    def EnumCategories(
        self, Flags: UIntType, CategoryToMatch: IReferenceIdentity, riid: Guid, EnumOut: ObjectType
    ) -> Tuple[VoidType, Guid, ObjectType]: ...
    def EnumCategoryInstances(
        self,
        Flags: UIntType,
        CategoryId: IDefinitionIdentity,
        Subcategory: StringType,
        riid: Guid,
        EnumOut: ObjectType,
    ) -> Tuple[VoidType, Guid, ObjectType]: ...
    def EnumComponents(
        self, dwFlags: UIntType, ppIdentityEnum: ObjectType
    ) -> Tuple[VoidType, ObjectType]: ...
    def EnumSubcategories(
        self,
        Flags: UIntType,
        CategoryId: IDefinitionIdentity,
        SubcategoryPattern: StringType,
        riid: Guid,
        EnumOut: ObjectType,
    ) -> Tuple[VoidType, Guid, ObjectType]: ...
    def FindComponentsByDefinition(
        self,
        dwFlags: UIntType,
        ComponentCount: NUIntType,
        Components: ArrayType[IDefinitionIdentity],
        Indicies: ArrayType[NUIntType],
        Dispositions: ArrayType[UIntType],
    ) -> Tuple[VoidType, ArrayType[NUIntType], ArrayType[UIntType]]: ...
    def FindComponentsByReference(
        self,
        dwFlags: UIntType,
        Components: NUIntType,
        References: ArrayType[IReferenceIdentity],
        Indicies: ArrayType[NUIntType],
        Dispositions: ArrayType[UIntType],
    ) -> Tuple[VoidType, ArrayType[NUIntType], ArrayType[UIntType]]: ...
    def FindReferenceInContext(
        self, dwFlags: UIntType, Reference: IReferenceIdentity, MatchedDefinition: ObjectType
    ) -> Tuple[VoidType, ObjectType]: ...
    def GetAppId(self, AppId: ObjectType) -> Tuple[VoidType, ObjectType]: ...
    def GetApplicationProperties(
        self,
        Flags: UIntType,
        cProperties: NUIntType,
        PropertyNames: ArrayType[StringType],
        PropertyValues: StringType,
        ComponentIndicies: NUIntType,
    ) -> Tuple[VoidType, StringType, NUIntType]: ...
    def GetApplicationStateFilesystemLocation(
        self,
        dwFlags: UIntType,
        Component: NUIntType,
        pCoordinateList: NIntType,
        ppszPath: StringType,
    ) -> Tuple[VoidType, StringType]: ...
    def GetComponentManifest(
        self,
        Flags: UIntType,
        ComponentId: IDefinitionIdentity,
        riid: Guid,
        ManifestInteface: ObjectType,
    ) -> Tuple[VoidType, Guid, ObjectType]: ...
    def GetComponentPayloadPath(
        self, Flags: UIntType, ComponentId: IDefinitionIdentity, PayloadPath: StringType
    ) -> Tuple[VoidType, StringType]: ...
    def GetComponentStringTableStrings(
        self,
        Flags: UIntType,
        ComponentIndex: NIntType,
        StringCount: NIntType,
        SourceStrings: ArrayType[StringType],
        DestinationStrings: StringType,
        CultureFallbacks: NIntType,
    ) -> Tuple[VoidType, ArrayType[StringType], StringType]: ...
    def PrepareForExecution(self, Inputs: NIntType, Outputs: NIntType) -> VoidType: ...
    def ReplaceStringMacros(
        self,
        Flags: UIntType,
        Culture: StringType,
        ReplacementPattern: StringType,
        Replaced: StringType,
    ) -> Tuple[VoidType, StringType]: ...
    def SetApplicationRunningState(
        self, dwFlags: UIntType, ulState: UIntType, ulDisposition: UIntType
    ) -> Tuple[VoidType, UIntType]: ...

    # No Events

class IAppIdAuthority(Protocol):
    # No Properties

    # ---------- Methods ---------- #

    def AreDefinitionsEqual(
        self, Flags: UIntType, Definition1: IDefinitionAppId, Definition2: IDefinitionAppId
    ) -> BooleanType: ...
    def AreReferencesEqual(
        self, Flags: UIntType, Reference1: IReferenceAppId, Reference2: IReferenceAppId
    ) -> BooleanType: ...
    def AreTextualDefinitionsEqual(
        self, Flags: UIntType, AppIdLeft: StringType, AppIdRight: StringType
    ) -> BooleanType: ...
    def AreTextualReferencesEqual(
        self, Flags: UIntType, AppIdLeft: StringType, AppIdRight: StringType
    ) -> BooleanType: ...
    def CreateDefinition(self) -> IDefinitionAppId: ...
    def CreateReference(self) -> IReferenceAppId: ...
    def DefinitionToText(
        self, Flags: UIntType, DefinitionAppId: IDefinitionAppId
    ) -> StringType: ...
    def DoesDefinitionMatchReference(
        self,
        Flags: UIntType,
        DefinitionIdentity: IDefinitionAppId,
        ReferenceIdentity: IReferenceAppId,
    ) -> BooleanType: ...
    def DoesTextualDefinitionMatchTextualReference(
        self, Flags: UIntType, Definition: StringType, Reference: StringType
    ) -> BooleanType: ...
    def GenerateDefinitionKey(
        self, Flags: UIntType, DefinitionIdentity: IDefinitionAppId
    ) -> StringType: ...
    def GenerateReferenceKey(
        self, Flags: UIntType, ReferenceIdentity: IReferenceAppId
    ) -> StringType: ...
    def HashDefinition(
        self, Flags: UIntType, DefinitionIdentity: IDefinitionAppId
    ) -> ULongType: ...
    def HashReference(self, Flags: UIntType, ReferenceIdentity: IReferenceAppId) -> ULongType: ...
    def ReferenceToText(self, Flags: UIntType, ReferenceAppId: IReferenceAppId) -> StringType: ...
    def TextToDefinition(self, Flags: UIntType, Identity: StringType) -> IDefinitionAppId: ...
    def TextToReference(self, Flags: UIntType, Identity: StringType) -> IReferenceAppId: ...

    # No Events

class ICDF(Protocol):
    # ---------- Properties ---------- #

    @property
    def Count(self) -> UIntType: ...
    @property
    def _NewEnum(self) -> ObjectType: ...

    # ---------- Methods ---------- #

    def GetItem(self, SectionId: UIntType) -> ObjectType: ...
    def GetRootSection(self, SectionId: UIntType) -> ISection: ...
    def GetRootSectionEntry(self, SectionId: UIntType) -> ISectionEntry: ...
    def get_Count(self) -> UIntType: ...
    def get__NewEnum(self) -> ObjectType: ...

    # No Events

class IDefinitionAppId(Protocol):
    # No Properties

    # ---------- Methods ---------- #

    def EnumAppPath(self) -> IEnumDefinitionIdentity: ...
    def SetAppPath(
        self, cIDefinitionIdentity: UIntType, DefinitionIdentity: ArrayType[IDefinitionIdentity]
    ) -> VoidType: ...
    def get_Codebase(self) -> StringType: ...
    def get_SubscriptionId(self) -> StringType: ...
    def put_Codebase(self, CodeBase: StringType) -> VoidType: ...
    def put_SubscriptionId(self, Subscription: StringType) -> VoidType: ...

    # No Events

class IDefinitionIdentity(Protocol):
    # No Properties

    # ---------- Methods ---------- #

    def Clone(
        self, cDeltas: NIntType, Deltas: ArrayType[IDENTITY_ATTRIBUTE]
    ) -> IDefinitionIdentity: ...
    def EnumAttributes(self) -> IEnumIDENTITY_ATTRIBUTE: ...
    def GetAttribute(self, Namespace: StringType, Name: StringType) -> StringType: ...
    def SetAttribute(
        self, Namespace: StringType, Name: StringType, Value: StringType
    ) -> VoidType: ...

    # No Events

class IEnumDefinitionIdentity(Protocol):
    # No Properties

    # ---------- Methods ---------- #

    def Clone(self) -> IEnumDefinitionIdentity: ...
    def Next(
        self, celt: UIntType, DefinitionIdentity: ArrayType[IDefinitionIdentity]
    ) -> Tuple[UIntType, ArrayType[IDefinitionIdentity]]: ...
    def Reset(self) -> VoidType: ...
    def Skip(self, celt: UIntType) -> VoidType: ...

    # No Events

class IEnumIDENTITY_ATTRIBUTE(Protocol):
    # No Properties

    # ---------- Methods ---------- #

    def Clone(self) -> IEnumIDENTITY_ATTRIBUTE: ...
    def CurrentIntoBuffer(
        self, Available: NIntType, Data: ArrayType[ByteType]
    ) -> Tuple[NIntType, ArrayType[ByteType]]: ...
    def Next(
        self, celt: UIntType, rgAttributes: ArrayType[IDENTITY_ATTRIBUTE]
    ) -> Tuple[UIntType, ArrayType[IDENTITY_ATTRIBUTE]]: ...
    def Reset(self) -> VoidType: ...
    def Skip(self, celt: UIntType) -> VoidType: ...

    # No Events

class IEnumReferenceIdentity(Protocol):
    # No Properties

    # ---------- Methods ---------- #

    def Clone(self) -> IEnumReferenceIdentity: ...
    def Next(
        self, celt: UIntType, ReferenceIdentity: ArrayType[IReferenceIdentity]
    ) -> Tuple[UIntType, ArrayType[IReferenceIdentity]]: ...
    def Reset(self) -> VoidType: ...
    def Skip(self, celt: UIntType) -> VoidType: ...

    # No Events

class IEnumSTORE_ASSEMBLY(Protocol):
    # No Properties

    # ---------- Methods ---------- #

    def Clone(self) -> IEnumSTORE_ASSEMBLY: ...
    def Next(
        self, celt: UIntType, rgelt: ArrayType[STORE_ASSEMBLY]
    ) -> Tuple[UIntType, ArrayType[STORE_ASSEMBLY]]: ...
    def Reset(self) -> VoidType: ...
    def Skip(self, celt: UIntType) -> VoidType: ...

    # No Events

class IEnumSTORE_ASSEMBLY_FILE(Protocol):
    # No Properties

    # ---------- Methods ---------- #

    def Clone(self) -> IEnumSTORE_ASSEMBLY_FILE: ...
    def Next(
        self, celt: UIntType, rgelt: ArrayType[STORE_ASSEMBLY_FILE]
    ) -> Tuple[UIntType, ArrayType[STORE_ASSEMBLY_FILE]]: ...
    def Reset(self) -> VoidType: ...
    def Skip(self, celt: UIntType) -> VoidType: ...

    # No Events

class IEnumSTORE_ASSEMBLY_INSTALLATION_REFERENCE(Protocol):
    # No Properties

    # ---------- Methods ---------- #

    def Clone(self) -> IEnumSTORE_ASSEMBLY_INSTALLATION_REFERENCE: ...
    def Next(
        self, celt: UIntType, rgelt: ArrayType[StoreApplicationReference]
    ) -> Tuple[UIntType, ArrayType[StoreApplicationReference]]: ...
    def Reset(self) -> VoidType: ...
    def Skip(self, celt: UIntType) -> VoidType: ...

    # No Events

class IEnumSTORE_CATEGORY(Protocol):
    # No Properties

    # ---------- Methods ---------- #

    def Clone(self) -> IEnumSTORE_CATEGORY: ...
    def Next(
        self, celt: UIntType, rgElements: ArrayType[STORE_CATEGORY]
    ) -> Tuple[UIntType, ArrayType[STORE_CATEGORY]]: ...
    def Reset(self) -> VoidType: ...
    def Skip(self, ulElements: UIntType) -> VoidType: ...

    # No Events

class IEnumSTORE_CATEGORY_INSTANCE(Protocol):
    # No Properties

    # ---------- Methods ---------- #

    def Clone(self) -> IEnumSTORE_CATEGORY_INSTANCE: ...
    def Next(
        self, ulElements: UIntType, rgInstances: ArrayType[STORE_CATEGORY_INSTANCE]
    ) -> Tuple[UIntType, ArrayType[STORE_CATEGORY_INSTANCE]]: ...
    def Reset(self) -> VoidType: ...
    def Skip(self, ulElements: UIntType) -> VoidType: ...

    # No Events

class IEnumSTORE_CATEGORY_SUBCATEGORY(Protocol):
    # No Properties

    # ---------- Methods ---------- #

    def Clone(self) -> IEnumSTORE_CATEGORY_SUBCATEGORY: ...
    def Next(
        self, celt: UIntType, rgElements: ArrayType[STORE_CATEGORY_SUBCATEGORY]
    ) -> Tuple[UIntType, ArrayType[STORE_CATEGORY_SUBCATEGORY]]: ...
    def Reset(self) -> VoidType: ...
    def Skip(self, ulElements: UIntType) -> VoidType: ...

    # No Events

class IEnumSTORE_DEPLOYMENT_METADATA(Protocol):
    # No Properties

    # ---------- Methods ---------- #

    def Clone(self) -> IEnumSTORE_DEPLOYMENT_METADATA: ...
    def Next(
        self, celt: UIntType, AppIds: ArrayType[IDefinitionAppId]
    ) -> Tuple[UIntType, ArrayType[IDefinitionAppId]]: ...
    def Reset(self) -> VoidType: ...
    def Skip(self, celt: UIntType) -> VoidType: ...

    # No Events

class IEnumSTORE_DEPLOYMENT_METADATA_PROPERTY(Protocol):
    # No Properties

    # ---------- Methods ---------- #

    def Clone(self) -> IEnumSTORE_DEPLOYMENT_METADATA_PROPERTY: ...
    def Next(
        self, celt: UIntType, AppIds: ArrayType[StoreOperationMetadataProperty]
    ) -> Tuple[UIntType, ArrayType[StoreOperationMetadataProperty]]: ...
    def Reset(self) -> VoidType: ...
    def Skip(self, celt: UIntType) -> VoidType: ...

    # No Events

class IEnumUnknown(Protocol):
    # No Properties

    # ---------- Methods ---------- #

    def Clone(self, enumUnknown: IEnumUnknown) -> Tuple[IntType, IEnumUnknown]: ...
    def Next(
        self, celt: UIntType, rgelt: ArrayType[ObjectType], celtFetched: UIntType
    ) -> Tuple[IntType, ArrayType[ObjectType], UIntType]: ...
    def Reset(self) -> IntType: ...
    def Skip(self, celt: UIntType) -> IntType: ...

    # No Events

class IIdentityAuthority(Protocol):
    # No Properties

    # ---------- Methods ---------- #

    def AreDefinitionsEqual(
        self, Flags: UIntType, Definition1: IDefinitionIdentity, Definition2: IDefinitionIdentity
    ) -> BooleanType: ...
    def AreReferencesEqual(
        self, Flags: UIntType, Reference1: IReferenceIdentity, Reference2: IReferenceIdentity
    ) -> BooleanType: ...
    def AreTextualDefinitionsEqual(
        self, Flags: UIntType, IdentityLeft: StringType, IdentityRight: StringType
    ) -> BooleanType: ...
    def AreTextualReferencesEqual(
        self, Flags: UIntType, IdentityLeft: StringType, IdentityRight: StringType
    ) -> BooleanType: ...
    def CreateDefinition(self) -> IDefinitionIdentity: ...
    def CreateReference(self) -> IReferenceIdentity: ...
    def DefinitionToText(
        self, Flags: UIntType, DefinitionIdentity: IDefinitionIdentity
    ) -> StringType: ...
    def DefinitionToTextBuffer(
        self,
        Flags: UIntType,
        DefinitionIdentity: IDefinitionIdentity,
        BufferSize: UIntType,
        Buffer: ArrayType[CharType],
    ) -> Tuple[UIntType, ArrayType[CharType]]: ...
    def DoesDefinitionMatchReference(
        self,
        Flags: UIntType,
        DefinitionIdentity: IDefinitionIdentity,
        ReferenceIdentity: IReferenceIdentity,
    ) -> BooleanType: ...
    def DoesTextualDefinitionMatchTextualReference(
        self, Flags: UIntType, Definition: StringType, Reference: StringType
    ) -> BooleanType: ...
    def GenerateDefinitionKey(
        self, Flags: UIntType, DefinitionIdentity: IDefinitionIdentity
    ) -> StringType: ...
    def GenerateReferenceKey(
        self, Flags: UIntType, ReferenceIdentity: IReferenceIdentity
    ) -> StringType: ...
    def HashDefinition(
        self, Flags: UIntType, DefinitionIdentity: IDefinitionIdentity
    ) -> ULongType: ...
    def HashReference(
        self, Flags: UIntType, ReferenceIdentity: IReferenceIdentity
    ) -> ULongType: ...
    def ReferenceToText(
        self, Flags: UIntType, ReferenceIdentity: IReferenceIdentity
    ) -> StringType: ...
    def ReferenceToTextBuffer(
        self,
        Flags: UIntType,
        ReferenceIdentity: IReferenceIdentity,
        BufferSize: UIntType,
        Buffer: ArrayType[CharType],
    ) -> Tuple[UIntType, ArrayType[CharType]]: ...
    def TextToDefinition(self, Flags: UIntType, Identity: StringType) -> IDefinitionIdentity: ...
    def TextToReference(self, Flags: UIntType, Identity: StringType) -> IReferenceIdentity: ...

    # No Events

class IManifestInformation(Protocol):
    # No Properties

    # ---------- Methods ---------- #

    def get_FullPath(self, FullPath: StringType) -> Tuple[VoidType, StringType]: ...

    # No Events

class IManifestParseErrorCallback(Protocol):
    # No Properties

    # ---------- Methods ---------- #

    def OnError(
        self,
        StartLine: UIntType,
        nStartColumn: UIntType,
        cCharacterCount: UIntType,
        hr: IntType,
        ErrorStatusHostFile: StringType,
        ParameterCount: UIntType,
        Parameters: ArrayType[StringType],
    ) -> VoidType: ...

    # No Events

class IReferenceAppId(Protocol):
    # No Properties

    # ---------- Methods ---------- #

    def EnumAppPath(self) -> IEnumReferenceIdentity: ...
    def get_Codebase(self) -> StringType: ...
    def get_SubscriptionId(self) -> StringType: ...
    def put_Codebase(self, CodeBase: StringType) -> VoidType: ...
    def put_SubscriptionId(self, Subscription: StringType) -> VoidType: ...

    # No Events

class IReferenceIdentity(Protocol):
    # No Properties

    # ---------- Methods ---------- #

    def Clone(
        self, cDeltas: NIntType, Deltas: ArrayType[IDENTITY_ATTRIBUTE]
    ) -> IReferenceIdentity: ...
    def EnumAttributes(self) -> IEnumIDENTITY_ATTRIBUTE: ...
    def GetAttribute(self, Namespace: StringType, Name: StringType) -> StringType: ...
    def SetAttribute(
        self, Namespace: StringType, Name: StringType, Value: StringType
    ) -> VoidType: ...

    # No Events

class ISection(Protocol):
    # ---------- Properties ---------- #

    @property
    def Count(self) -> UIntType: ...
    @property
    def SectionID(self) -> UIntType: ...
    @property
    def SectionName(self) -> StringType: ...
    @property
    def _NewEnum(self) -> ObjectType: ...

    # ---------- Methods ---------- #

    def get_Count(self) -> UIntType: ...
    def get_SectionID(self) -> UIntType: ...
    def get_SectionName(self) -> StringType: ...
    def get__NewEnum(self) -> ObjectType: ...

    # No Events

class ISectionEntry(Protocol):
    # No Properties

    # ---------- Methods ---------- #

    def GetField(self, fieldId: UIntType) -> ObjectType: ...
    def GetFieldName(self, fieldId: UIntType) -> StringType: ...

    # No Events

class ISectionWithReferenceIdentityKey(Protocol):
    # No Properties

    # ---------- Methods ---------- #

    def Lookup(
        self, ReferenceIdentityKey: IReferenceIdentity, ppUnknown: ObjectType
    ) -> Tuple[VoidType, ObjectType]: ...

    # No Events

class ISectionWithStringKey(Protocol):
    # ---------- Properties ---------- #

    @property
    def IsCaseInsensitive(self) -> BooleanType: ...

    # ---------- Methods ---------- #

    def Lookup(
        self, wzStringKey: StringType, ppUnknown: ObjectType
    ) -> Tuple[VoidType, ObjectType]: ...
    def get_IsCaseInsensitive(self) -> BooleanType: ...

    # No Events

class IStateManager(Protocol):
    # No Properties

    # ---------- Methods ---------- #

    def GetApplicationStateFilesystemLocation(
        self,
        Flags: UIntType,
        Appidentity: IDefinitionAppId,
        ComponentIdentity: IDefinitionIdentity,
        Coordinates: NUIntType,
        Path: StringType,
    ) -> Tuple[VoidType, StringType]: ...
    def PrepareApplicationState(
        self, Inputs: NUIntType, Outputs: NUIntType
    ) -> Tuple[VoidType, NUIntType]: ...
    def Scavenge(self, Flags: UIntType, Disposition: UIntType) -> Tuple[VoidType, UIntType]: ...
    def SetApplicationRunningState(
        self, Flags: UIntType, Context: IActContext, RunningState: UIntType, Disposition: UIntType
    ) -> Tuple[VoidType, UIntType]: ...

    # No Events

class IStore(Protocol):
    # No Properties

    # ---------- Methods ---------- #

    def BindDefinitions(
        self,
        Flags: UIntType,
        Count: NIntType,
        DefsToBind: ArrayType[IDefinitionIdentity],
        DeploymentsToIgnore: UIntType,
        DefsToIgnore: ArrayType[IDefinitionIdentity],
    ) -> NIntType: ...
    def BindReferenceToAssembly(
        self,
        Flags: UIntType,
        ReferenceIdentity: IReferenceIdentity,
        cDeploymentsToIgnore: UIntType,
        DefinitionIdentity_DeploymentsToIgnore: ArrayType[IDefinitionIdentity],
        riid: Guid,
    ) -> Tuple[ObjectType, Guid]: ...
    def CalculateDelimiterOfDeploymentsBasedOnQuota(
        self,
        dwFlags: UIntType,
        cDeployments: NIntType,
        rgpIDefinitionAppId_Deployments: ArrayType[IDefinitionAppId],
        InstallerReference: StoreApplicationReference,
        ulonglongQuota: ULongType,
        Delimiter: NIntType,
        SizeSharedWithExternalDeployment: ULongType,
        SizeConsumedByInputDeploymentArray: ULongType,
    ) -> Tuple[VoidType, StoreApplicationReference, NIntType, ULongType, ULongType]: ...
    def EnumAssemblies(
        self, Flags: UIntType, ReferenceIdentity_ToMatch: IReferenceIdentity, riid: Guid
    ) -> Tuple[ObjectType, Guid]: ...
    def EnumCategories(
        self, Flags: UIntType, ReferenceIdentity_ToMatch: IReferenceIdentity, riid: Guid
    ) -> Tuple[ObjectType, Guid]: ...
    def EnumCategoryInstances(
        self,
        Flags: UIntType,
        CategoryId: IDefinitionIdentity,
        SubcategoryPath: StringType,
        riid: Guid,
    ) -> Tuple[ObjectType, Guid]: ...
    def EnumFiles(
        self, Flags: UIntType, DefinitionIdentity: IDefinitionIdentity, riid: Guid
    ) -> Tuple[ObjectType, Guid]: ...
    def EnumInstallationReferences(
        self, Flags: UIntType, DefinitionIdentity: IDefinitionIdentity, riid: Guid
    ) -> Tuple[ObjectType, Guid]: ...
    def EnumInstallerDeploymentMetadata(
        self,
        Flags: UIntType,
        Reference: StoreApplicationReference,
        Filter: IReferenceAppId,
        riid: Guid,
    ) -> Tuple[ObjectType, StoreApplicationReference, Guid]: ...
    def EnumInstallerDeploymentMetadataProperties(
        self,
        Flags: UIntType,
        Reference: StoreApplicationReference,
        Filter: IDefinitionAppId,
        riid: Guid,
    ) -> Tuple[ObjectType, StoreApplicationReference, Guid]: ...
    def EnumPrivateFiles(
        self,
        Flags: UIntType,
        Application: IDefinitionAppId,
        DefinitionIdentity: IDefinitionIdentity,
        riid: Guid,
    ) -> Tuple[ObjectType, Guid]: ...
    def EnumSubcategories(
        self,
        Flags: UIntType,
        CategoryId: IDefinitionIdentity,
        SubcategoryPathPattern: StringType,
        riid: Guid,
    ) -> Tuple[ObjectType, Guid]: ...
    def GetAssemblyInformation(
        self, Flags: UIntType, DefinitionIdentity: IDefinitionIdentity, riid: Guid
    ) -> Tuple[ObjectType, Guid]: ...
    def GetDeploymentProperty(
        self,
        Flags: UIntType,
        DeploymentInPackage: IDefinitionAppId,
        Reference: StoreApplicationReference,
        PropertySet: Guid,
        pcwszPropertyName: StringType,
        blob: BLOB,
    ) -> Tuple[VoidType, StoreApplicationReference, Guid, BLOB]: ...
    def LockApplicationPath(
        self, Flags: UIntType, ApId: IDefinitionAppId, Cookie: NIntType
    ) -> Tuple[StringType, NIntType]: ...
    def LockAssemblyPath(
        self, Flags: UIntType, DefinitionIdentity: IDefinitionIdentity, Cookie: NIntType
    ) -> Tuple[StringType, NIntType]: ...
    def QueryChangeID(self, DefinitionIdentity: IDefinitionIdentity) -> ULongType: ...
    def ReleaseApplicationPath(self, Cookie: NIntType) -> VoidType: ...
    def ReleaseAssemblyPath(self, Cookie: NIntType) -> VoidType: ...
    def Transact(
        self,
        cOperation: NIntType,
        rgOperations: ArrayType[StoreTransactionOperation],
        rgDispositions: ArrayType[UIntType],
        rgResults: ArrayType[IntType],
    ) -> Tuple[VoidType, ArrayType[UIntType], ArrayType[IntType]]: ...

    # No Events

# ---------- Enums ---------- #

class IAPPIDAUTHORITY_ARE_DEFINITIONS_EQUAL_FLAGS(Enum):
    IAPPIDAUTHORITY_ARE_DEFINITIONS_EQUAL_FLAG_IGNORE_VERSION = 1

class IAPPIDAUTHORITY_ARE_REFERENCES_EQUAL_FLAGS(Enum):
    IAPPIDAUTHORITY_ARE_REFERENCES_EQUAL_FLAG_IGNORE_VERSION = 1

class IIDENTITYAUTHORITY_DEFINITION_IDENTITY_TO_TEXT_FLAGS(Enum):
    IIDENTITYAUTHORITY_DEFINITION_IDENTITY_TO_TEXT_FLAG_CANONICAL = 1

class IIDENTITYAUTHORITY_DOES_DEFINITION_MATCH_REFERENCE_FLAGS(Enum):
    IIDENTITYAUTHORITY_DOES_DEFINITION_MATCH_REFERENCE_FLAG_EXACT_MATCH_REQUIRED = 1

class IIDENTITYAUTHORITY_REFERENCE_IDENTITY_TO_TEXT_FLAGS(Enum):
    IIDENTITYAUTHORITY_REFERENCE_IDENTITY_TO_TEXT_FLAG_CANONICAL = 1

class ISTORE_BIND_REFERENCE_TO_ASSEMBLY_FLAGS(Enum):
    ISTORE_BIND_REFERENCE_TO_ASSEMBLY_FLAG_FORCE_LIBRARY_SEMANTICS = 1

class ISTORE_ENUM_ASSEMBLIES_FLAGS(Enum):
    ISTORE_ENUM_ASSEMBLIES_FLAG_LIMIT_TO_VISIBLE_ONLY = 1
    ISTORE_ENUM_ASSEMBLIES_FLAG_MATCH_SERVICING = 2
    ISTORE_ENUM_ASSEMBLIES_FLAG_FORCE_LIBRARY_SEMANTICS = 4

class ISTORE_ENUM_FILES_FLAGS(Enum):
    ISTORE_ENUM_FILES_FLAG_INCLUDE_INSTALLED_FILES = 1
    ISTORE_ENUM_FILES_FLAG_INCLUDE_MISSING_FILES = 2

class STORE_ASSEMBLY_FILE_STATUS_FLAGS(Enum):
    STORE_ASSEMBLY_FILE_STATUS_FLAG_PRESENT = 1

class STORE_ASSEMBLY_STATUS_FLAGS(Enum):
    STORE_ASSEMBLY_STATUS_MANIFEST_ONLY = 1
    STORE_ASSEMBLY_STATUS_PAYLOAD_RESIDENT = 2
    STORE_ASSEMBLY_STATUS_PARTIAL_INSTALL = 4

class StateManager_RunningState(Enum):
    Undefined = 0
    Starting = 1
    Running = 2

class StoreTransactionOperationType(Enum):
    Invalid = 0
    SetCanonicalizationContext = 14
    StageComponent = 20
    PinDeployment = 21
    UnpinDeployment = 22
    StageComponentFile = 23
    InstallDeployment = 24
    UninstallDeployment = 25
    SetDeploymentMetadata = 26
    Scavenge = 27

# No Delegates

__all__ = [
    IsolationInterop,
    Store,
    StoreAssemblyEnumeration,
    StoreAssemblyFileEnumeration,
    StoreCategoryEnumeration,
    StoreCategoryInstanceEnumeration,
    StoreDeploymentMetadataEnumeration,
    StoreDeploymentMetadataPropertyEnumeration,
    StoreSubcategoryEnumeration,
    StoreTransaction,
    BLOB,
    CATEGORY,
    CATEGORY_INSTANCE,
    CATEGORY_SUBCATEGORY,
    IDENTITY_ATTRIBUTE,
    IStore_BindingResult,
    IStore_BindingResult_BoundVersion,
    STORE_ASSEMBLY,
    STORE_ASSEMBLY_FILE,
    STORE_CATEGORY,
    STORE_CATEGORY_INSTANCE,
    STORE_CATEGORY_SUBCATEGORY,
    StoreApplicationReference,
    StoreOperationInstallDeployment,
    StoreOperationMetadataProperty,
    StoreOperationPinDeployment,
    StoreOperationScavenge,
    StoreOperationSetCanonicalizationContext,
    StoreOperationSetDeploymentMetadata,
    StoreOperationStageComponent,
    StoreOperationStageComponentFile,
    StoreOperationUninstallDeployment,
    StoreOperationUnpinDeployment,
    StoreTransactionData,
    StoreTransactionOperation,
    IActContext,
    IAppIdAuthority,
    ICDF,
    IDefinitionAppId,
    IDefinitionIdentity,
    IEnumDefinitionIdentity,
    IEnumIDENTITY_ATTRIBUTE,
    IEnumReferenceIdentity,
    IEnumSTORE_ASSEMBLY,
    IEnumSTORE_ASSEMBLY_FILE,
    IEnumSTORE_ASSEMBLY_INSTALLATION_REFERENCE,
    IEnumSTORE_CATEGORY,
    IEnumSTORE_CATEGORY_INSTANCE,
    IEnumSTORE_CATEGORY_SUBCATEGORY,
    IEnumSTORE_DEPLOYMENT_METADATA,
    IEnumSTORE_DEPLOYMENT_METADATA_PROPERTY,
    IEnumUnknown,
    IIdentityAuthority,
    IManifestInformation,
    IManifestParseErrorCallback,
    IReferenceAppId,
    IReferenceIdentity,
    ISection,
    ISectionEntry,
    ISectionWithReferenceIdentityKey,
    ISectionWithStringKey,
    IStateManager,
    IStore,
    IAPPIDAUTHORITY_ARE_DEFINITIONS_EQUAL_FLAGS,
    IAPPIDAUTHORITY_ARE_REFERENCES_EQUAL_FLAGS,
    IIDENTITYAUTHORITY_DEFINITION_IDENTITY_TO_TEXT_FLAGS,
    IIDENTITYAUTHORITY_DOES_DEFINITION_MATCH_REFERENCE_FLAGS,
    IIDENTITYAUTHORITY_REFERENCE_IDENTITY_TO_TEXT_FLAGS,
    ISTORE_BIND_REFERENCE_TO_ASSEMBLY_FLAGS,
    ISTORE_ENUM_ASSEMBLIES_FLAGS,
    ISTORE_ENUM_FILES_FLAGS,
    STORE_ASSEMBLY_FILE_STATUS_FLAGS,
    STORE_ASSEMBLY_STATUS_FLAGS,
    StateManager_RunningState,
    StoreTransactionOperationType,
]
