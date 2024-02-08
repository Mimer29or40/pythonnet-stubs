from __future__ import annotations

from abc import ABC
from typing import ClassVar
from typing import Final
from typing import Tuple
from typing import overload

from System import Array
from System import Char
from System import DateTime
from System import Enum
from System import Guid
from System import IDisposable
from System import IntPtr
from System import Object
from System import Type
from System import UIntPtr
from System import ValueType
from System.Collections import IEnumerator
from System.Deployment.Internal.Isolation.Manifest import ICMS
from System.Deployment.Internal.Isolation.Store import EnumApplicationPrivateFiles
from System.Deployment.Internal.Isolation.Store import EnumAssembliesFlags
from System.Deployment.Internal.Isolation.Store import EnumAssemblyFilesFlags
from System.Deployment.Internal.Isolation.Store import EnumAssemblyInstallReferenceFlags
from System.Deployment.Internal.Isolation.Store import EnumCategoriesFlags
from System.Deployment.Internal.Isolation.Store import EnumCategoryInstancesFlags
from System.Deployment.Internal.Isolation.Store import EnumSubcategoriesFlags
from System.Deployment.Internal.Isolation.Store import GetPackagePropertyFlags
from System.Deployment.Internal.Isolation.Store import IPathLock
from System.Deployment.Internal.Isolation.StoreApplicationReference import RefFlags
from System.Deployment.Internal.Isolation.StoreOperationInstallDeployment import OpFlags
from System.Deployment.Internal.Isolation.StoreOperationPinDeployment import OpFlags
from System.Deployment.Internal.Isolation.StoreOperationScavenge import OpFlags
from System.Deployment.Internal.Isolation.StoreOperationSetCanonicalizationContext import OpFlags
from System.Deployment.Internal.Isolation.StoreOperationSetDeploymentMetadata import OpFlags
from System.Deployment.Internal.Isolation.StoreOperationStageComponent import OpFlags
from System.Deployment.Internal.Isolation.StoreOperationStageComponentFile import OpFlags
from System.Deployment.Internal.Isolation.StoreOperationUninstallDeployment import OpFlags
from System.Deployment.Internal.Isolation.StoreOperationUnpinDeployment import OpFlags

class BLOB(ValueType, IDisposable):
    """"""

    BlobData: Final[IntPtr] = ...
    """
    
    :return: 
    """
    Size: Final[int] = ...
    """
    
    :return: 
    """
    def Dispose(self) -> None:
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

class CATEGORY(ValueType):
    """"""

    DefinitionIdentity: Final[IDefinitionIdentity] = ...
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

class CATEGORY_INSTANCE(ValueType):
    """"""

    DefinitionAppId_Application: Final[IDefinitionAppId] = ...
    """
    
    :return: 
    """
    XMLSnippet: Final[str] = ...
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

class CATEGORY_SUBCATEGORY(ValueType):
    """"""

    Subcategory: Final[str] = ...
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

class IAPPIDAUTHORITY_ARE_DEFINITIONS_EQUAL_FLAGS(Enum):
    """"""

    IAPPIDAUTHORITY_ARE_DEFINITIONS_EQUAL_FLAG_IGNORE_VERSION: IAPPIDAUTHORITY_ARE_DEFINITIONS_EQUAL_FLAGS = (
        ...
    )
    """"""

class IAPPIDAUTHORITY_ARE_REFERENCES_EQUAL_FLAGS(Enum):
    """"""

    IAPPIDAUTHORITY_ARE_REFERENCES_EQUAL_FLAG_IGNORE_VERSION: IAPPIDAUTHORITY_ARE_REFERENCES_EQUAL_FLAGS = (
        ...
    )
    """"""

class IActContext:
    """"""

    def ApplicationBasePath(self, Flags: int, ApplicationPath: str) -> Tuple[None, str]:
        """

        :param Flags:
        :param ApplicationPath:
        """
    def CreateActContextFromCategoryInstance(
        self, dwFlags: int, CategoryInstance: CATEGORY_INSTANCE, ppCreatedAppContext: object
    ) -> Tuple[None, object]:
        """

        :param dwFlags:
        :param CategoryInstance:
        :param ppCreatedAppContext:
        """
    def EnumCategories(
        self, Flags: int, CategoryToMatch: IReferenceIdentity, riid: Guid, EnumOut: object
    ) -> Tuple[None, object]:
        """

        :param Flags:
        :param CategoryToMatch:
        :param riid:
        :param EnumOut:
        """
    def EnumCategoryInstances(
        self,
        Flags: int,
        CategoryId: IDefinitionIdentity,
        Subcategory: str,
        riid: Guid,
        EnumOut: object,
    ) -> Tuple[None, object]:
        """

        :param Flags:
        :param CategoryId:
        :param Subcategory:
        :param riid:
        :param EnumOut:
        """
    def EnumComponents(self, dwFlags: int, ppIdentityEnum: object) -> Tuple[None, object]:
        """

        :param dwFlags:
        :param ppIdentityEnum:
        """
    def EnumSubcategories(
        self,
        Flags: int,
        CategoryId: IDefinitionIdentity,
        SubcategoryPattern: str,
        riid: Guid,
        EnumOut: object,
    ) -> Tuple[None, object]:
        """

        :param Flags:
        :param CategoryId:
        :param SubcategoryPattern:
        :param riid:
        :param EnumOut:
        """
    def FindComponentsByDefinition(
        self,
        dwFlags: int,
        ComponentCount: UIntPtr,
        Components: Array[IDefinitionIdentity],
        Indicies: Array[UIntPtr],
        Dispositions: Array[int],
    ) -> Tuple[None, Array[UIntPtr], Array[int]]:
        """

        :param dwFlags:
        :param ComponentCount:
        :param Components:
        :param Indicies:
        :param Dispositions:
        """
    def FindComponentsByReference(
        self,
        dwFlags: int,
        Components: UIntPtr,
        References: Array[IReferenceIdentity],
        Indicies: Array[UIntPtr],
        Dispositions: Array[int],
    ) -> Tuple[None, Array[UIntPtr], Array[int]]:
        """

        :param dwFlags:
        :param Components:
        :param References:
        :param Indicies:
        :param Dispositions:
        """
    def FindReferenceInContext(
        self, dwFlags: int, Reference: IReferenceIdentity, MatchedDefinition: object
    ) -> Tuple[None, object]:
        """

        :param dwFlags:
        :param Reference:
        :param MatchedDefinition:
        """
    def GetAppId(self, AppId: object) -> Tuple[None, object]:
        """

        :param AppId:
        """
    def GetApplicationProperties(
        self,
        Flags: int,
        cProperties: UIntPtr,
        PropertyNames: Array[str],
        PropertyValues: str,
        ComponentIndicies: UIntPtr,
    ) -> Tuple[None, str, UIntPtr]:
        """

        :param Flags:
        :param cProperties:
        :param PropertyNames:
        :param PropertyValues:
        :param ComponentIndicies:
        """
    def GetApplicationStateFilesystemLocation(
        self, dwFlags: int, Component: UIntPtr, pCoordinateList: IntPtr, ppszPath: str
    ) -> Tuple[None, str]:
        """

        :param dwFlags:
        :param Component:
        :param pCoordinateList:
        :param ppszPath:
        """
    def GetComponentManifest(
        self, Flags: int, ComponentId: IDefinitionIdentity, riid: Guid, ManifestInteface: object
    ) -> Tuple[None, object]:
        """

        :param Flags:
        :param ComponentId:
        :param riid:
        :param ManifestInteface:
        """
    def GetComponentPayloadPath(
        self, Flags: int, ComponentId: IDefinitionIdentity, PayloadPath: str
    ) -> Tuple[None, str]:
        """

        :param Flags:
        :param ComponentId:
        :param PayloadPath:
        """
    def GetComponentStringTableStrings(
        self,
        Flags: int,
        ComponentIndex: IntPtr,
        StringCount: IntPtr,
        SourceStrings: Array[str],
        DestinationStrings: str,
        CultureFallbacks: IntPtr,
    ) -> Tuple[None, Array[str], str]:
        """

        :param Flags:
        :param ComponentIndex:
        :param StringCount:
        :param SourceStrings:
        :param DestinationStrings:
        :param CultureFallbacks:
        """
    def PrepareForExecution(self, Inputs: IntPtr, Outputs: IntPtr) -> None:
        """

        :param Inputs:
        :param Outputs:
        """
    def ReplaceStringMacros(
        self, Flags: int, Culture: str, ReplacementPattern: str, Replaced: str
    ) -> Tuple[None, str]:
        """

        :param Flags:
        :param Culture:
        :param ReplacementPattern:
        :param Replaced:
        """
    def SetApplicationRunningState(
        self, dwFlags: int, ulState: int, ulDisposition: int
    ) -> Tuple[None, int]:
        """

        :param dwFlags:
        :param ulState:
        :param ulDisposition:
        """

class IAppIdAuthority:
    """"""

    def AreDefinitionsEqual(
        self, Flags: int, Definition1: IDefinitionAppId, Definition2: IDefinitionAppId
    ) -> bool:
        """

        :param Flags:
        :param Definition1:
        :param Definition2:
        :return:
        """
    def AreReferencesEqual(
        self, Flags: int, Reference1: IReferenceAppId, Reference2: IReferenceAppId
    ) -> bool:
        """

        :param Flags:
        :param Reference1:
        :param Reference2:
        :return:
        """
    def AreTextualDefinitionsEqual(self, Flags: int, AppIdLeft: str, AppIdRight: str) -> bool:
        """

        :param Flags:
        :param AppIdLeft:
        :param AppIdRight:
        :return:
        """
    def AreTextualReferencesEqual(self, Flags: int, AppIdLeft: str, AppIdRight: str) -> bool:
        """

        :param Flags:
        :param AppIdLeft:
        :param AppIdRight:
        :return:
        """
    def CreateDefinition(self) -> IDefinitionAppId:
        """

        :return:
        """
    def CreateReference(self) -> IReferenceAppId:
        """

        :return:
        """
    def DefinitionToText(self, Flags: int, DefinitionAppId: IDefinitionAppId) -> str:
        """

        :param Flags:
        :param DefinitionAppId:
        :return:
        """
    def DoesDefinitionMatchReference(
        self, Flags: int, DefinitionIdentity: IDefinitionAppId, ReferenceIdentity: IReferenceAppId
    ) -> bool:
        """

        :param Flags:
        :param DefinitionIdentity:
        :param ReferenceIdentity:
        :return:
        """
    def DoesTextualDefinitionMatchTextualReference(
        self, Flags: int, Definition: str, Reference: str
    ) -> bool:
        """

        :param Flags:
        :param Definition:
        :param Reference:
        :return:
        """
    def GenerateDefinitionKey(self, Flags: int, DefinitionIdentity: IDefinitionAppId) -> str:
        """

        :param Flags:
        :param DefinitionIdentity:
        :return:
        """
    def GenerateReferenceKey(self, Flags: int, ReferenceIdentity: IReferenceAppId) -> str:
        """

        :param Flags:
        :param ReferenceIdentity:
        :return:
        """
    def HashDefinition(self, Flags: int, DefinitionIdentity: IDefinitionAppId) -> int:
        """

        :param Flags:
        :param DefinitionIdentity:
        :return:
        """
    def HashReference(self, Flags: int, ReferenceIdentity: IReferenceAppId) -> int:
        """

        :param Flags:
        :param ReferenceIdentity:
        :return:
        """
    def ReferenceToText(self, Flags: int, ReferenceAppId: IReferenceAppId) -> str:
        """

        :param Flags:
        :param ReferenceAppId:
        :return:
        """
    def TextToDefinition(self, Flags: int, Identity: str) -> IDefinitionAppId:
        """

        :param Flags:
        :param Identity:
        :return:
        """
    def TextToReference(self, Flags: int, Identity: str) -> IReferenceAppId:
        """

        :param Flags:
        :param Identity:
        :return:
        """

class ICDF:
    """"""

    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def _NewEnum(self) -> object:
        """

        :return:
        """
    def GetItem(self, SectionId: int) -> object:
        """

        :param SectionId:
        :return:
        """
    def GetRootSection(self, SectionId: int) -> ISection:
        """

        :param SectionId:
        :return:
        """
    def GetRootSectionEntry(self, SectionId: int) -> ISectionEntry:
        """

        :param SectionId:
        :return:
        """

class IDENTITY_ATTRIBUTE(ValueType):
    """"""

    Name: Final[str] = ...
    """
    
    :return: 
    """
    Namespace: Final[str] = ...
    """
    
    :return: 
    """
    Value: Final[str] = ...
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

class IDefinitionAppId:
    """"""

    def EnumAppPath(self) -> IEnumDefinitionIdentity:
        """

        :return:
        """
    def SetAppPath(
        self, cIDefinitionIdentity: int, DefinitionIdentity: Array[IDefinitionIdentity]
    ) -> None:
        """

        :param cIDefinitionIdentity:
        :param DefinitionIdentity:
        """
    def put_Codebase(self, CodeBase: str) -> None:
        """

        :param CodeBase:
        """
    def put_SubscriptionId(self, Subscription: str) -> None:
        """

        :param Subscription:
        """

class IDefinitionIdentity:
    """"""

    def Clone(self, cDeltas: IntPtr, Deltas: Array[IDENTITY_ATTRIBUTE]) -> IDefinitionIdentity:
        """

        :param cDeltas:
        :param Deltas:
        :return:
        """
    def EnumAttributes(self) -> IEnumIDENTITY_ATTRIBUTE:
        """

        :return:
        """
    def GetAttribute(self, Namespace: str, Name: str) -> str:
        """

        :param Namespace:
        :param Name:
        :return:
        """
    def SetAttribute(self, Namespace: str, Name: str, Value: str) -> None:
        """

        :param Namespace:
        :param Name:
        :param Value:
        """

class IEnumDefinitionIdentity:
    """"""

    def Clone(self) -> IEnumDefinitionIdentity:
        """

        :return:
        """
    def Next(
        self, celt: int, DefinitionIdentity: Array[IDefinitionIdentity]
    ) -> Tuple[int, Array[IDefinitionIdentity]]:
        """

        :param celt:
        :param DefinitionIdentity:
        :return:
        """
    def Reset(self) -> None:
        """"""
    def Skip(self, celt: int) -> None:
        """

        :param celt:
        """

class IEnumIDENTITY_ATTRIBUTE:
    """"""

    def Clone(self) -> IEnumIDENTITY_ATTRIBUTE:
        """

        :return:
        """
    def CurrentIntoBuffer(self, Available: IntPtr, Data: Array[int]) -> Tuple[IntPtr, Array[int]]:
        """

        :param Available:
        :param Data:
        :return:
        """
    def Next(
        self, celt: int, rgAttributes: Array[IDENTITY_ATTRIBUTE]
    ) -> Tuple[int, Array[IDENTITY_ATTRIBUTE]]:
        """

        :param celt:
        :param rgAttributes:
        :return:
        """
    def Reset(self) -> None:
        """"""
    def Skip(self, celt: int) -> None:
        """

        :param celt:
        """

class IEnumReferenceIdentity:
    """"""

    def Clone(self) -> IEnumReferenceIdentity:
        """

        :return:
        """
    def Next(
        self, celt: int, ReferenceIdentity: Array[IReferenceIdentity]
    ) -> Tuple[int, Array[IReferenceIdentity]]:
        """

        :param celt:
        :param ReferenceIdentity:
        :return:
        """
    def Reset(self) -> None:
        """"""
    def Skip(self, celt: int) -> None:
        """

        :param celt:
        """

class IEnumSTORE_ASSEMBLY:
    """"""

    def Clone(self) -> IEnumSTORE_ASSEMBLY:
        """

        :return:
        """
    def Next(self, celt: int, rgelt: Array[STORE_ASSEMBLY]) -> Tuple[int, Array[STORE_ASSEMBLY]]:
        """

        :param celt:
        :param rgelt:
        :return:
        """
    def Reset(self) -> None:
        """"""
    def Skip(self, celt: int) -> None:
        """

        :param celt:
        """

class IEnumSTORE_ASSEMBLY_FILE:
    """"""

    def Clone(self) -> IEnumSTORE_ASSEMBLY_FILE:
        """

        :return:
        """
    def Next(
        self, celt: int, rgelt: Array[STORE_ASSEMBLY_FILE]
    ) -> Tuple[int, Array[STORE_ASSEMBLY_FILE]]:
        """

        :param celt:
        :param rgelt:
        :return:
        """
    def Reset(self) -> None:
        """"""
    def Skip(self, celt: int) -> None:
        """

        :param celt:
        """

class IEnumSTORE_ASSEMBLY_INSTALLATION_REFERENCE:
    """"""

    def Clone(self) -> IEnumSTORE_ASSEMBLY_INSTALLATION_REFERENCE:
        """

        :return:
        """
    def Next(
        self, celt: int, rgelt: Array[StoreApplicationReference]
    ) -> Tuple[int, Array[StoreApplicationReference]]:
        """

        :param celt:
        :param rgelt:
        :return:
        """
    def Reset(self) -> None:
        """"""
    def Skip(self, celt: int) -> None:
        """

        :param celt:
        """

class IEnumSTORE_CATEGORY:
    """"""

    def Clone(self) -> IEnumSTORE_CATEGORY:
        """

        :return:
        """
    def Next(
        self, celt: int, rgElements: Array[STORE_CATEGORY]
    ) -> Tuple[int, Array[STORE_CATEGORY]]:
        """

        :param celt:
        :param rgElements:
        :return:
        """
    def Reset(self) -> None:
        """"""
    def Skip(self, ulElements: int) -> None:
        """

        :param ulElements:
        """

class IEnumSTORE_CATEGORY_INSTANCE:
    """"""

    def Clone(self) -> IEnumSTORE_CATEGORY_INSTANCE:
        """

        :return:
        """
    def Next(
        self, ulElements: int, rgInstances: Array[STORE_CATEGORY_INSTANCE]
    ) -> Tuple[int, Array[STORE_CATEGORY_INSTANCE]]:
        """

        :param ulElements:
        :param rgInstances:
        :return:
        """
    def Reset(self) -> None:
        """"""
    def Skip(self, ulElements: int) -> None:
        """

        :param ulElements:
        """

class IEnumSTORE_CATEGORY_SUBCATEGORY:
    """"""

    def Clone(self) -> IEnumSTORE_CATEGORY_SUBCATEGORY:
        """

        :return:
        """
    def Next(
        self, celt: int, rgElements: Array[STORE_CATEGORY_SUBCATEGORY]
    ) -> Tuple[int, Array[STORE_CATEGORY_SUBCATEGORY]]:
        """

        :param celt:
        :param rgElements:
        :return:
        """
    def Reset(self) -> None:
        """"""
    def Skip(self, ulElements: int) -> None:
        """

        :param ulElements:
        """

class IEnumSTORE_DEPLOYMENT_METADATA:
    """"""

    def Clone(self) -> IEnumSTORE_DEPLOYMENT_METADATA:
        """

        :return:
        """
    def Next(
        self, celt: int, AppIds: Array[IDefinitionAppId]
    ) -> Tuple[int, Array[IDefinitionAppId]]:
        """

        :param celt:
        :param AppIds:
        :return:
        """
    def Reset(self) -> None:
        """"""
    def Skip(self, celt: int) -> None:
        """

        :param celt:
        """

class IEnumSTORE_DEPLOYMENT_METADATA_PROPERTY:
    """"""

    def Clone(self) -> IEnumSTORE_DEPLOYMENT_METADATA_PROPERTY:
        """

        :return:
        """
    def Next(
        self, celt: int, AppIds: Array[StoreOperationMetadataProperty]
    ) -> Tuple[int, Array[StoreOperationMetadataProperty]]:
        """

        :param celt:
        :param AppIds:
        :return:
        """
    def Reset(self) -> None:
        """"""
    def Skip(self, celt: int) -> None:
        """

        :param celt:
        """

class IEnumUnknown:
    """"""

    def Clone(self, enumUnknown: IEnumUnknown) -> Tuple[int, IEnumUnknown]:
        """

        :param enumUnknown:
        :return:
        """
    def Next(self, celt: int, rgelt: Array[object], celtFetched: int) -> Tuple[int, Array[object]]:
        """

        :param celt:
        :param rgelt:
        :param celtFetched:
        :return:
        """
    def Reset(self) -> int:
        """

        :return:
        """
    def Skip(self, celt: int) -> int:
        """

        :param celt:
        :return:
        """

class IIDENTITYAUTHORITY_DEFINITION_IDENTITY_TO_TEXT_FLAGS(Enum):
    """"""

    IIDENTITYAUTHORITY_DEFINITION_IDENTITY_TO_TEXT_FLAG_CANONICAL: IIDENTITYAUTHORITY_DEFINITION_IDENTITY_TO_TEXT_FLAGS = (
        ...
    )
    """"""

class IIDENTITYAUTHORITY_DOES_DEFINITION_MATCH_REFERENCE_FLAGS(Enum):
    """"""

    IIDENTITYAUTHORITY_DOES_DEFINITION_MATCH_REFERENCE_FLAG_EXACT_MATCH_REQUIRED: IIDENTITYAUTHORITY_DOES_DEFINITION_MATCH_REFERENCE_FLAGS = (
        ...
    )
    """"""

class IIDENTITYAUTHORITY_REFERENCE_IDENTITY_TO_TEXT_FLAGS(Enum):
    """"""

    IIDENTITYAUTHORITY_REFERENCE_IDENTITY_TO_TEXT_FLAG_CANONICAL: IIDENTITYAUTHORITY_REFERENCE_IDENTITY_TO_TEXT_FLAGS = (
        ...
    )
    """"""

class IIdentityAuthority:
    """"""

    def AreDefinitionsEqual(
        self, Flags: int, Definition1: IDefinitionIdentity, Definition2: IDefinitionIdentity
    ) -> bool:
        """

        :param Flags:
        :param Definition1:
        :param Definition2:
        :return:
        """
    def AreReferencesEqual(
        self, Flags: int, Reference1: IReferenceIdentity, Reference2: IReferenceIdentity
    ) -> bool:
        """

        :param Flags:
        :param Reference1:
        :param Reference2:
        :return:
        """
    def AreTextualDefinitionsEqual(self, Flags: int, IdentityLeft: str, IdentityRight: str) -> bool:
        """

        :param Flags:
        :param IdentityLeft:
        :param IdentityRight:
        :return:
        """
    def AreTextualReferencesEqual(self, Flags: int, IdentityLeft: str, IdentityRight: str) -> bool:
        """

        :param Flags:
        :param IdentityLeft:
        :param IdentityRight:
        :return:
        """
    def CreateDefinition(self) -> IDefinitionIdentity:
        """

        :return:
        """
    def CreateReference(self) -> IReferenceIdentity:
        """

        :return:
        """
    def DefinitionToText(self, Flags: int, DefinitionIdentity: IDefinitionIdentity) -> str:
        """

        :param Flags:
        :param DefinitionIdentity:
        :return:
        """
    def DefinitionToTextBuffer(
        self,
        Flags: int,
        DefinitionIdentity: IDefinitionIdentity,
        BufferSize: int,
        Buffer: Array[Char],
    ) -> Tuple[int, Array[Char]]:
        """

        :param Flags:
        :param DefinitionIdentity:
        :param BufferSize:
        :param Buffer:
        :return:
        """
    def DoesDefinitionMatchReference(
        self,
        Flags: int,
        DefinitionIdentity: IDefinitionIdentity,
        ReferenceIdentity: IReferenceIdentity,
    ) -> bool:
        """

        :param Flags:
        :param DefinitionIdentity:
        :param ReferenceIdentity:
        :return:
        """
    def DoesTextualDefinitionMatchTextualReference(
        self, Flags: int, Definition: str, Reference: str
    ) -> bool:
        """

        :param Flags:
        :param Definition:
        :param Reference:
        :return:
        """
    def GenerateDefinitionKey(self, Flags: int, DefinitionIdentity: IDefinitionIdentity) -> str:
        """

        :param Flags:
        :param DefinitionIdentity:
        :return:
        """
    def GenerateReferenceKey(self, Flags: int, ReferenceIdentity: IReferenceIdentity) -> str:
        """

        :param Flags:
        :param ReferenceIdentity:
        :return:
        """
    def HashDefinition(self, Flags: int, DefinitionIdentity: IDefinitionIdentity) -> int:
        """

        :param Flags:
        :param DefinitionIdentity:
        :return:
        """
    def HashReference(self, Flags: int, ReferenceIdentity: IReferenceIdentity) -> int:
        """

        :param Flags:
        :param ReferenceIdentity:
        :return:
        """
    def ReferenceToText(self, Flags: int, ReferenceIdentity: IReferenceIdentity) -> str:
        """

        :param Flags:
        :param ReferenceIdentity:
        :return:
        """
    def ReferenceToTextBuffer(
        self,
        Flags: int,
        ReferenceIdentity: IReferenceIdentity,
        BufferSize: int,
        Buffer: Array[Char],
    ) -> Tuple[int, Array[Char]]:
        """

        :param Flags:
        :param ReferenceIdentity:
        :param BufferSize:
        :param Buffer:
        :return:
        """
    def TextToDefinition(self, Flags: int, Identity: str) -> IDefinitionIdentity:
        """

        :param Flags:
        :param Identity:
        :return:
        """
    def TextToReference(self, Flags: int, Identity: str) -> IReferenceIdentity:
        """

        :param Flags:
        :param Identity:
        :return:
        """

class IManifestInformation:
    """"""

class IManifestParseErrorCallback:
    """"""

    def OnError(
        self,
        StartLine: int,
        nStartColumn: int,
        cCharacterCount: int,
        hr: int,
        ErrorStatusHostFile: str,
        ParameterCount: int,
        Parameters: Array[str],
    ) -> None:
        """

        :param StartLine:
        :param nStartColumn:
        :param cCharacterCount:
        :param hr:
        :param ErrorStatusHostFile:
        :param ParameterCount:
        :param Parameters:
        """

class IReferenceAppId:
    """"""

    def EnumAppPath(self) -> IEnumReferenceIdentity:
        """

        :return:
        """
    def put_Codebase(self, CodeBase: str) -> None:
        """

        :param CodeBase:
        """
    def put_SubscriptionId(self, Subscription: str) -> None:
        """

        :param Subscription:
        """

class IReferenceIdentity:
    """"""

    def Clone(self, cDeltas: IntPtr, Deltas: Array[IDENTITY_ATTRIBUTE]) -> IReferenceIdentity:
        """

        :param cDeltas:
        :param Deltas:
        :return:
        """
    def EnumAttributes(self) -> IEnumIDENTITY_ATTRIBUTE:
        """

        :return:
        """
    def GetAttribute(self, Namespace: str, Name: str) -> str:
        """

        :param Namespace:
        :param Name:
        :return:
        """
    def SetAttribute(self, Namespace: str, Name: str, Value: str) -> None:
        """

        :param Namespace:
        :param Name:
        :param Value:
        """

class ISTORE_BIND_REFERENCE_TO_ASSEMBLY_FLAGS(Enum):
    """"""

    ISTORE_BIND_REFERENCE_TO_ASSEMBLY_FLAG_FORCE_LIBRARY_SEMANTICS: ISTORE_BIND_REFERENCE_TO_ASSEMBLY_FLAGS = (
        ...
    )
    """"""

class ISTORE_ENUM_ASSEMBLIES_FLAGS(Enum):
    """"""

    ISTORE_ENUM_ASSEMBLIES_FLAG_LIMIT_TO_VISIBLE_ONLY: ISTORE_ENUM_ASSEMBLIES_FLAGS = ...
    """"""
    ISTORE_ENUM_ASSEMBLIES_FLAG_MATCH_SERVICING: ISTORE_ENUM_ASSEMBLIES_FLAGS = ...
    """"""
    ISTORE_ENUM_ASSEMBLIES_FLAG_FORCE_LIBRARY_SEMANTICS: ISTORE_ENUM_ASSEMBLIES_FLAGS = ...
    """"""

class ISTORE_ENUM_FILES_FLAGS(Enum):
    """"""

    ISTORE_ENUM_FILES_FLAG_INCLUDE_INSTALLED_FILES: ISTORE_ENUM_FILES_FLAGS = ...
    """"""
    ISTORE_ENUM_FILES_FLAG_INCLUDE_MISSING_FILES: ISTORE_ENUM_FILES_FLAGS = ...
    """"""

class ISection:
    """"""

    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def SectionID(self) -> int:
        """

        :return:
        """
    @property
    def SectionName(self) -> str:
        """

        :return:
        """
    @property
    def _NewEnum(self) -> object:
        """

        :return:
        """

class ISectionEntry:
    """"""

    def GetField(self, fieldId: int) -> object:
        """

        :param fieldId:
        :return:
        """
    def GetFieldName(self, fieldId: int) -> str:
        """

        :param fieldId:
        :return:
        """

class ISectionWithReferenceIdentityKey:
    """"""

    def Lookup(
        self, ReferenceIdentityKey: IReferenceIdentity, ppUnknown: object
    ) -> Tuple[None, object]:
        """

        :param ReferenceIdentityKey:
        :param ppUnknown:
        """

class ISectionWithStringKey:
    """"""

    @property
    def IsCaseInsensitive(self) -> bool:
        """

        :return:
        """
    def Lookup(self, wzStringKey: str, ppUnknown: object) -> Tuple[None, object]:
        """

        :param wzStringKey:
        :param ppUnknown:
        """

class IStateManager:
    """"""

    def GetApplicationStateFilesystemLocation(
        self,
        Flags: int,
        Appidentity: IDefinitionAppId,
        ComponentIdentity: IDefinitionIdentity,
        Coordinates: UIntPtr,
        Path: str,
    ) -> Tuple[None, str]:
        """

        :param Flags:
        :param Appidentity:
        :param ComponentIdentity:
        :param Coordinates:
        :param Path:
        """
    def PrepareApplicationState(self, Inputs: UIntPtr, Outputs: UIntPtr) -> None:
        """

        :param Inputs:
        :param Outputs:
        """
    def Scavenge(self, Flags: int, Disposition: int) -> Tuple[None, int]:
        """

        :param Flags:
        :param Disposition:
        """
    def SetApplicationRunningState(
        self, Flags: int, Context: IActContext, RunningState: int, Disposition: int
    ) -> Tuple[None, int]:
        """

        :param Flags:
        :param Context:
        :param RunningState:
        :param Disposition:
        """

class IStore:
    """"""

    def BindDefinitions(
        self,
        Flags: int,
        Count: IntPtr,
        DefsToBind: Array[IDefinitionIdentity],
        DeploymentsToIgnore: int,
        DefsToIgnore: Array[IDefinitionIdentity],
    ) -> IntPtr:
        """

        :param Flags:
        :param Count:
        :param DefsToBind:
        :param DeploymentsToIgnore:
        :param DefsToIgnore:
        :return:
        """
    def BindReferenceToAssembly(
        self,
        Flags: int,
        ReferenceIdentity: IReferenceIdentity,
        cDeploymentsToIgnore: int,
        DefinitionIdentity_DeploymentsToIgnore: Array[IDefinitionIdentity],
        riid: Guid,
    ) -> object:
        """

        :param Flags:
        :param ReferenceIdentity:
        :param cDeploymentsToIgnore:
        :param DefinitionIdentity_DeploymentsToIgnore:
        :param riid:
        :return:
        """
    def CalculateDelimiterOfDeploymentsBasedOnQuota(
        self,
        dwFlags: int,
        cDeployments: IntPtr,
        rgpIDefinitionAppId_Deployments: Array[IDefinitionAppId],
        InstallerReference: StoreApplicationReference,
        ulonglongQuota: int,
        Delimiter: IntPtr,
        SizeSharedWithExternalDeployment: int,
        SizeConsumedByInputDeploymentArray: int,
    ) -> Tuple[None, IntPtr, int, int]:
        """

        :param dwFlags:
        :param cDeployments:
        :param rgpIDefinitionAppId_Deployments:
        :param InstallerReference:
        :param ulonglongQuota:
        :param Delimiter:
        :param SizeSharedWithExternalDeployment:
        :param SizeConsumedByInputDeploymentArray:
        """
    def EnumAssemblies(
        self, Flags: int, ReferenceIdentity_ToMatch: IReferenceIdentity, riid: Guid
    ) -> object:
        """

        :param Flags:
        :param ReferenceIdentity_ToMatch:
        :param riid:
        :return:
        """
    def EnumCategories(
        self, Flags: int, ReferenceIdentity_ToMatch: IReferenceIdentity, riid: Guid
    ) -> object:
        """

        :param Flags:
        :param ReferenceIdentity_ToMatch:
        :param riid:
        :return:
        """
    def EnumCategoryInstances(
        self, Flags: int, CategoryId: IDefinitionIdentity, SubcategoryPath: str, riid: Guid
    ) -> object:
        """

        :param Flags:
        :param CategoryId:
        :param SubcategoryPath:
        :param riid:
        :return:
        """
    def EnumFiles(self, Flags: int, DefinitionIdentity: IDefinitionIdentity, riid: Guid) -> object:
        """

        :param Flags:
        :param DefinitionIdentity:
        :param riid:
        :return:
        """
    def EnumInstallationReferences(
        self, Flags: int, DefinitionIdentity: IDefinitionIdentity, riid: Guid
    ) -> object:
        """

        :param Flags:
        :param DefinitionIdentity:
        :param riid:
        :return:
        """
    def EnumInstallerDeploymentMetadata(
        self, Flags: int, Reference: StoreApplicationReference, Filter: IReferenceAppId, riid: Guid
    ) -> object:
        """

        :param Flags:
        :param Reference:
        :param Filter:
        :param riid:
        :return:
        """
    def EnumInstallerDeploymentMetadataProperties(
        self, Flags: int, Reference: StoreApplicationReference, Filter: IDefinitionAppId, riid: Guid
    ) -> object:
        """

        :param Flags:
        :param Reference:
        :param Filter:
        :param riid:
        :return:
        """
    def EnumPrivateFiles(
        self,
        Flags: int,
        Application: IDefinitionAppId,
        DefinitionIdentity: IDefinitionIdentity,
        riid: Guid,
    ) -> object:
        """

        :param Flags:
        :param Application:
        :param DefinitionIdentity:
        :param riid:
        :return:
        """
    def EnumSubcategories(
        self, Flags: int, CategoryId: IDefinitionIdentity, SubcategoryPathPattern: str, riid: Guid
    ) -> object:
        """

        :param Flags:
        :param CategoryId:
        :param SubcategoryPathPattern:
        :param riid:
        :return:
        """
    def GetAssemblyInformation(
        self, Flags: int, DefinitionIdentity: IDefinitionIdentity, riid: Guid
    ) -> object:
        """

        :param Flags:
        :param DefinitionIdentity:
        :param riid:
        :return:
        """
    def GetDeploymentProperty(
        self,
        Flags: int,
        DeploymentInPackage: IDefinitionAppId,
        Reference: StoreApplicationReference,
        PropertySet: Guid,
        pcwszPropertyName: str,
        blob: BLOB,
    ) -> Tuple[None, BLOB]:
        """

        :param Flags:
        :param DeploymentInPackage:
        :param Reference:
        :param PropertySet:
        :param pcwszPropertyName:
        :param blob:
        """
    def LockApplicationPath(
        self, Flags: int, ApId: IDefinitionAppId, Cookie: IntPtr
    ) -> Tuple[str, IntPtr]:
        """

        :param Flags:
        :param ApId:
        :param Cookie:
        :return:
        """
    def LockAssemblyPath(
        self, Flags: int, DefinitionIdentity: IDefinitionIdentity, Cookie: IntPtr
    ) -> Tuple[str, IntPtr]:
        """

        :param Flags:
        :param DefinitionIdentity:
        :param Cookie:
        :return:
        """
    def QueryChangeID(self, DefinitionIdentity: IDefinitionIdentity) -> int:
        """

        :param DefinitionIdentity:
        :return:
        """
    def ReleaseApplicationPath(self, Cookie: IntPtr) -> None:
        """

        :param Cookie:
        """
    def ReleaseAssemblyPath(self, Cookie: IntPtr) -> None:
        """

        :param Cookie:
        """
    def Transact(
        self,
        cOperation: IntPtr,
        rgOperations: Array[StoreTransactionOperation],
        rgDispositions: Array[int],
        rgResults: Array[int],
    ) -> Tuple[None, Array[int], Array[int]]:
        """

        :param cOperation:
        :param rgOperations:
        :param rgDispositions:
        :param rgResults:
        """

class IStore_BindingResult(ValueType):
    """"""

    CacheCoherencyGuid: Final[Guid] = ...
    """
    
    :return: 
    """
    Component: Final[IStore_BindingResult_BoundVersion] = ...
    """
    
    :return: 
    """
    Disposition: Final[int] = ...
    """
    
    :return: 
    """
    Flags: Final[int] = ...
    """
    
    :return: 
    """
    Reserved: Final[IntPtr] = ...
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

class IStore_BindingResult_BoundVersion(ValueType):
    """"""

    Build: Final[int] = ...
    """
    
    :return: 
    """
    Major: Final[int] = ...
    """
    
    :return: 
    """
    Minor: Final[int] = ...
    """
    
    :return: 
    """
    Revision: Final[int] = ...
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

class IsolationInterop(ABC, Object):
    """"""

    GUID_SXS_INSTALL_REFERENCE_SCHEME_OPAQUESTRING: Final[ClassVar[Guid]] = ...
    """
    
    :return: 
    """
    IID_ICMS: Final[ClassVar[Guid]] = ...
    """
    
    :return: 
    """
    IID_IDefinitionIdentity: Final[ClassVar[Guid]] = ...
    """
    
    :return: 
    """
    IID_IEnumSTORE_ASSEMBLY: Final[ClassVar[Guid]] = ...
    """
    
    :return: 
    """
    IID_IEnumSTORE_ASSEMBLY_FILE: Final[ClassVar[Guid]] = ...
    """
    
    :return: 
    """
    IID_IEnumSTORE_CATEGORY: Final[ClassVar[Guid]] = ...
    """
    
    :return: 
    """
    IID_IEnumSTORE_CATEGORY_INSTANCE: Final[ClassVar[Guid]] = ...
    """
    
    :return: 
    """
    IID_IEnumSTORE_DEPLOYMENT_METADATA: Final[ClassVar[Guid]] = ...
    """
    
    :return: 
    """
    IID_IEnumSTORE_DEPLOYMENT_METADATA_PROPERTY: Final[ClassVar[Guid]] = ...
    """
    
    :return: 
    """
    IID_IManifestInformation: Final[ClassVar[Guid]] = ...
    """
    
    :return: 
    """
    IID_IStore: Final[ClassVar[Guid]] = ...
    """
    
    :return: 
    """
    IsolationDllName: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    SXS_INSTALL_REFERENCE_SCHEME_SXS_STRONGNAME_SIGNED_PRIVATE_ASSEMBLY: Final[ClassVar[Guid]] = ...
    """
    
    :return: 
    """
    @classmethod
    @property
    def AppIdAuthority(cls) -> IAppIdAuthority:
        """

        :return:
        """
    @classmethod
    @property
    def IdentityAuthority(cls) -> IIdentityAuthority:
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
    @classmethod
    def GetUserStore(cls) -> Store:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class STORE_ASSEMBLY(ValueType):
    """"""

    AssemblySize: Final[int] = ...
    """
    
    :return: 
    """
    ChangeId: Final[int] = ...
    """
    
    :return: 
    """
    DefinitionIdentity: Final[IDefinitionIdentity] = ...
    """
    
    :return: 
    """
    ManifestPath: Final[str] = ...
    """
    
    :return: 
    """
    Status: Final[int] = ...
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

class STORE_ASSEMBLY_FILE(ValueType):
    """"""

    FileName: Final[str] = ...
    """
    
    :return: 
    """
    FileStatusFlags: Final[int] = ...
    """
    
    :return: 
    """
    Flags: Final[int] = ...
    """
    
    :return: 
    """
    Size: Final[int] = ...
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

class STORE_ASSEMBLY_FILE_STATUS_FLAGS(Enum):
    """"""

    STORE_ASSEMBLY_FILE_STATUS_FLAG_PRESENT: STORE_ASSEMBLY_FILE_STATUS_FLAGS = ...
    """"""

class STORE_ASSEMBLY_STATUS_FLAGS(Enum):
    """"""

    STORE_ASSEMBLY_STATUS_MANIFEST_ONLY: STORE_ASSEMBLY_STATUS_FLAGS = ...
    """"""
    STORE_ASSEMBLY_STATUS_PAYLOAD_RESIDENT: STORE_ASSEMBLY_STATUS_FLAGS = ...
    """"""
    STORE_ASSEMBLY_STATUS_PARTIAL_INSTALL: STORE_ASSEMBLY_STATUS_FLAGS = ...
    """"""

class STORE_CATEGORY(ValueType):
    """"""

    DefinitionIdentity: Final[IDefinitionIdentity] = ...
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

class STORE_CATEGORY_INSTANCE(ValueType):
    """"""

    DefinitionAppId_Application: Final[IDefinitionAppId] = ...
    """
    
    :return: 
    """
    XMLSnippet: Final[str] = ...
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

class STORE_CATEGORY_SUBCATEGORY(ValueType):
    """"""

    Subcategory: Final[str] = ...
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

class StateManager_RunningState(Enum):
    """"""

    Undefined: StateManager_RunningState = ...
    """"""
    Starting: StateManager_RunningState = ...
    """"""
    Running: StateManager_RunningState = ...
    """"""

class Store(Object):
    """"""

    def __init__(self, pStore: IStore):
        """

        :param pStore:
        """
    @property
    def InternalStore(self) -> IStore:
        """

        :return:
        """
    def BindReferenceToAssemblyIdentity(
        self,
        Flags: int,
        ReferenceIdentity: IReferenceIdentity,
        cDeploymentsToIgnore: int,
        DefinitionIdentity_DeploymentsToIgnore: Array[IDefinitionIdentity],
    ) -> IDefinitionIdentity:
        """

        :param Flags:
        :param ReferenceIdentity:
        :param cDeploymentsToIgnore:
        :param DefinitionIdentity_DeploymentsToIgnore:
        :return:
        """
    def BindReferenceToAssemblyManifest(
        self,
        Flags: int,
        ReferenceIdentity: IReferenceIdentity,
        cDeploymentsToIgnore: int,
        DefinitionIdentity_DeploymentsToIgnore: Array[IDefinitionIdentity],
    ) -> ICMS:
        """

        :param Flags:
        :param ReferenceIdentity:
        :param cDeploymentsToIgnore:
        :param DefinitionIdentity_DeploymentsToIgnore:
        :return:
        """
    def CalculateDelimiterOfDeploymentsBasedOnQuota(
        self,
        dwFlags: int,
        cDeployments: int,
        rgpIDefinitionAppId_Deployments: Array[IDefinitionAppId],
        InstallerReference: StoreApplicationReference,
        ulonglongQuota: int,
        Delimiter: int,
        SizeSharedWithExternalDeployment: int,
        SizeConsumedByInputDeploymentArray: int,
    ) -> None:
        """

        :param dwFlags:
        :param cDeployments:
        :param rgpIDefinitionAppId_Deployments:
        :param InstallerReference:
        :param ulonglongQuota:
        :param Delimiter:
        :param SizeSharedWithExternalDeployment:
        :param SizeConsumedByInputDeploymentArray:
        """
    @overload
    def EnumAssemblies(self, Flags: Store.EnumAssembliesFlags) -> StoreAssemblyEnumeration:
        """

        :param Flags:
        :return:
        """
    @overload
    def EnumAssemblies(
        self, Flags: Store.EnumAssembliesFlags, refToMatch: IReferenceIdentity
    ) -> StoreAssemblyEnumeration:
        """

        :param Flags:
        :param refToMatch:
        :return:
        """
    def EnumCategories(
        self, Flags: Store.EnumCategoriesFlags, CategoryMatch: IReferenceIdentity
    ) -> StoreCategoryEnumeration:
        """

        :param Flags:
        :param CategoryMatch:
        :return:
        """
    def EnumCategoryInstances(
        self, Flags: Store.EnumCategoryInstancesFlags, Category: IDefinitionIdentity, SubCat: str
    ) -> StoreCategoryInstanceEnumeration:
        """

        :param Flags:
        :param Category:
        :param SubCat:
        :return:
        """
    def EnumFiles(
        self, Flags: Store.EnumAssemblyFilesFlags, Assembly: IDefinitionIdentity
    ) -> StoreAssemblyFileEnumeration:
        """

        :param Flags:
        :param Assembly:
        :return:
        """
    def EnumInstallationReferences(
        self, Flags: Store.EnumAssemblyInstallReferenceFlags, Assembly: IDefinitionIdentity
    ) -> IEnumSTORE_ASSEMBLY_INSTALLATION_REFERENCE:
        """

        :param Flags:
        :param Assembly:
        :return:
        """
    def EnumInstallerDeploymentProperties(
        self,
        InstallerId: Guid,
        InstallerName: str,
        InstallerMetadata: str,
        Deployment: IDefinitionAppId,
    ) -> StoreDeploymentMetadataPropertyEnumeration:
        """

        :param InstallerId:
        :param InstallerName:
        :param InstallerMetadata:
        :param Deployment:
        :return:
        """
    def EnumInstallerDeployments(
        self,
        InstallerId: Guid,
        InstallerName: str,
        InstallerMetadata: str,
        DeploymentFilter: IReferenceAppId,
    ) -> StoreDeploymentMetadataEnumeration:
        """

        :param InstallerId:
        :param InstallerName:
        :param InstallerMetadata:
        :param DeploymentFilter:
        :return:
        """
    def EnumPrivateFiles(
        self,
        Flags: Store.EnumApplicationPrivateFiles,
        Application: IDefinitionAppId,
        Assembly: IDefinitionIdentity,
    ) -> StoreAssemblyFileEnumeration:
        """

        :param Flags:
        :param Application:
        :param Assembly:
        :return:
        """
    @overload
    def EnumSubcategories(
        self, Flags: Store.EnumSubcategoriesFlags, CategoryMatch: IDefinitionIdentity
    ) -> StoreSubcategoryEnumeration:
        """

        :param Flags:
        :param CategoryMatch:
        :return:
        """
    @overload
    def EnumSubcategories(
        self, Flags: Store.EnumSubcategoriesFlags, Category: IDefinitionIdentity, SearchPattern: str
    ) -> StoreSubcategoryEnumeration:
        """

        :param Flags:
        :param Category:
        :param SearchPattern:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetAssemblyIdentity(
        self, Flags: int, DefinitionIdentity: IDefinitionIdentity
    ) -> IDefinitionIdentity:
        """

        :param Flags:
        :param DefinitionIdentity:
        :return:
        """
    def GetAssemblyManifest(self, Flags: int, DefinitionIdentity: IDefinitionIdentity) -> ICMS:
        """

        :param Flags:
        :param DefinitionIdentity:
        :return:
        """
    def GetDeploymentProperty(
        self,
        Flags: Store.GetPackagePropertyFlags,
        Deployment: IDefinitionAppId,
        Reference: StoreApplicationReference,
        PropertySet: Guid,
        PropertyName: str,
    ) -> Array[int]:
        """

        :param Flags:
        :param Deployment:
        :param Reference:
        :param PropertySet:
        :param PropertyName:
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
    def LockApplicationPath(self, app: IDefinitionAppId) -> Store.IPathLock:
        """

        :param app:
        :return:
        """
    def LockAssemblyPath(self, asm: IDefinitionIdentity) -> Store.IPathLock:
        """

        :param asm:
        :return:
        """
    def QueryChangeID(self, asm: IDefinitionIdentity) -> int:
        """

        :param asm:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Transact(self, operations: Array[StoreTransactionOperation]) -> Array[int]:
        """

        :param operations:
        :return:
        """

    class EnumApplicationPrivateFiles(Enum):
        """"""

        Nothing: EnumApplicationPrivateFiles = ...
        """"""
        IncludeInstalled: EnumApplicationPrivateFiles = ...
        """"""
        IncludeMissing: EnumApplicationPrivateFiles = ...
        """"""

    class EnumAssembliesFlags(Enum):
        """"""

        Nothing: EnumAssembliesFlags = ...
        """"""
        VisibleOnly: EnumAssembliesFlags = ...
        """"""
        MatchServicing: EnumAssembliesFlags = ...
        """"""
        ForceLibrarySemantics: EnumAssembliesFlags = ...
        """"""

    class EnumAssemblyFilesFlags(Enum):
        """"""

        Nothing: EnumAssemblyFilesFlags = ...
        """"""
        IncludeInstalled: EnumAssemblyFilesFlags = ...
        """"""
        IncludeMissing: EnumAssemblyFilesFlags = ...
        """"""

    class EnumAssemblyInstallReferenceFlags(Enum):
        """"""

        Nothing: EnumAssemblyInstallReferenceFlags = ...
        """"""

    class EnumCategoriesFlags(Enum):
        """"""

        Nothing: EnumCategoriesFlags = ...
        """"""

    class EnumCategoryInstancesFlags(Enum):
        """"""

        Nothing: EnumCategoryInstancesFlags = ...
        """"""

    class EnumSubcategoriesFlags(Enum):
        """"""

        Nothing: EnumSubcategoriesFlags = ...
        """"""

    class GetPackagePropertyFlags(Enum):
        """"""

        Nothing: GetPackagePropertyFlags = ...
        """"""

    class IPathLock(IDisposable):
        """"""

        @property
        def Path(self) -> str:
            """"""
        def Dispose(self) -> None:
            """"""

class StoreApplicationReference(ValueType):
    """"""

    Flags: Final[StoreApplicationReference.RefFlags] = ...
    """
    
    :return: 
    """
    GuidScheme: Final[Guid] = ...
    """
    
    :return: 
    """
    Identifier: Final[str] = ...
    """
    
    :return: 
    """
    NonCanonicalData: Final[str] = ...
    """
    
    :return: 
    """
    Size: Final[int] = ...
    """
    
    :return: 
    """
    def __init__(self, RefScheme: Guid, Id: str, NcData: str):
        """

        :param RefScheme:
        :param Id:
        :param NcData:
        """
    @classmethod
    def Destroy(cls, ip: IntPtr) -> None:
        """

        :param ip:
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
    def ToIntPtr(self) -> IntPtr:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

    class RefFlags(Enum):
        """"""

        Nothing: RefFlags = ...
        """"""

class StoreAssemblyEnumeration(Object, IEnumerator):
    """"""

    def __init__(self, pI: IEnumSTORE_ASSEMBLY):
        """

        :param pI:
        """
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

class StoreAssemblyFileEnumeration(Object, IEnumerator):
    """"""

    def __init__(self, pI: IEnumSTORE_ASSEMBLY_FILE):
        """

        :param pI:
        """
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

class StoreCategoryEnumeration(Object, IEnumerator):
    """"""

    def __init__(self, pI: IEnumSTORE_CATEGORY):
        """

        :param pI:
        """
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

class StoreCategoryInstanceEnumeration(Object, IEnumerator):
    """"""

    def __init__(self, pI: IEnumSTORE_CATEGORY_INSTANCE):
        """

        :param pI:
        """
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

class StoreDeploymentMetadataEnumeration(Object, IEnumerator):
    """"""

    def __init__(self, pI: IEnumSTORE_DEPLOYMENT_METADATA):
        """

        :param pI:
        """
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

class StoreDeploymentMetadataPropertyEnumeration(Object, IEnumerator):
    """"""

    def __init__(self, pI: IEnumSTORE_DEPLOYMENT_METADATA_PROPERTY):
        """

        :param pI:
        """
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

class StoreOperationInstallDeployment(ValueType):
    """"""

    Application: Final[IDefinitionAppId] = ...
    """
    
    :return: 
    """
    Flags: Final[StoreOperationInstallDeployment.OpFlags] = ...
    """
    
    :return: 
    """
    Reference: Final[IntPtr] = ...
    """
    
    :return: 
    """
    Size: Final[int] = ...
    """
    
    :return: 
    """
    @overload
    def __init__(self, App: IDefinitionAppId, reference: StoreApplicationReference):
        """

        :param App:
        :param reference:
        """
    @overload
    def __init__(
        self, App: IDefinitionAppId, UninstallOthers: bool, reference: StoreApplicationReference
    ):
        """

        :param App:
        :param UninstallOthers:
        :param reference:
        """
    def Destroy(self) -> None:
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

    class Disposition(Enum):
        """"""

        Failed: Disposition = ...
        """"""
        AlreadyInstalled: Disposition = ...
        """"""
        Installed: Disposition = ...
        """"""

    class OpFlags(Enum):
        """"""

        Nothing: OpFlags = ...
        """"""
        UninstallOthers: OpFlags = ...
        """"""

class StoreOperationMetadataProperty(ValueType):
    """"""

    GuidPropertySet: Final[Guid] = ...
    """
    
    :return: 
    """
    Name: Final[str] = ...
    """
    
    :return: 
    """
    Value: Final[str] = ...
    """
    
    :return: 
    """
    ValueSize: Final[IntPtr] = ...
    """
    
    :return: 
    """
    @overload
    def __init__(self, PropertySet: Guid, Name: str):
        """

        :param PropertySet:
        :param Name:
        """
    @overload
    def __init__(self, PropertySet: Guid, Name: str, Value: str):
        """

        :param PropertySet:
        :param Name:
        :param Value:
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

class StoreOperationPinDeployment(ValueType):
    """"""

    Application: Final[IDefinitionAppId] = ...
    """
    
    :return: 
    """
    ExpirationTime: Final[int] = ...
    """
    
    :return: 
    """
    Flags: Final[StoreOperationPinDeployment.OpFlags] = ...
    """
    
    :return: 
    """
    Reference: Final[IntPtr] = ...
    """
    
    :return: 
    """
    Size: Final[int] = ...
    """
    
    :return: 
    """
    @overload
    def __init__(self, AppId: IDefinitionAppId, Ref: StoreApplicationReference):
        """

        :param AppId:
        :param Ref:
        """
    @overload
    def __init__(self, AppId: IDefinitionAppId, Expiry: DateTime, Ref: StoreApplicationReference):
        """

        :param AppId:
        :param Expiry:
        :param Ref:
        """
    def Destroy(self) -> None:
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

    class Disposition(Enum):
        """"""

        Failed: Disposition = ...
        """"""
        Pinned: Disposition = ...
        """"""

    class OpFlags(Enum):
        """"""

        Nothing: OpFlags = ...
        """"""
        NeverExpires: OpFlags = ...
        """"""

class StoreOperationScavenge(ValueType):
    """"""

    ComponentCountLimit: Final[int] = ...
    """
    
    :return: 
    """
    Flags: Final[StoreOperationScavenge.OpFlags] = ...
    """
    
    :return: 
    """
    RuntimeLimit: Final[int] = ...
    """
    
    :return: 
    """
    Size: Final[int] = ...
    """
    
    :return: 
    """
    SizeReclaimationLimit: Final[int] = ...
    """
    
    :return: 
    """
    @overload
    def __init__(self, Light: bool):
        """

        :param Light:
        """
    @overload
    def __init__(self, Light: bool, SizeLimit: int, RunLimit: int, ComponentLimit: int):
        """

        :param Light:
        :param SizeLimit:
        :param RunLimit:
        :param ComponentLimit:
        """
    def Destroy(self) -> None:
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

    class OpFlags(Enum):
        """"""

        Nothing: OpFlags = ...
        """"""
        Light: OpFlags = ...
        """"""
        LimitSize: OpFlags = ...
        """"""
        LimitTime: OpFlags = ...
        """"""
        LimitCount: OpFlags = ...
        """"""

class StoreOperationSetCanonicalizationContext(ValueType):
    """"""

    BaseAddressFilePath: Final[str] = ...
    """
    
    :return: 
    """
    ExportsFilePath: Final[str] = ...
    """
    
    :return: 
    """
    Flags: Final[StoreOperationSetCanonicalizationContext.OpFlags] = ...
    """
    
    :return: 
    """
    Size: Final[int] = ...
    """
    
    :return: 
    """
    def __init__(self, Bases: str, Exports: str):
        """

        :param Bases:
        :param Exports:
        """
    def Destroy(self) -> None:
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

    class OpFlags(Enum):
        """"""

        Nothing: OpFlags = ...
        """"""

class StoreOperationSetDeploymentMetadata(ValueType):
    """"""

    Deployment: Final[IDefinitionAppId] = ...
    """
    
    :return: 
    """
    Flags: Final[StoreOperationSetDeploymentMetadata.OpFlags] = ...
    """
    
    :return: 
    """
    InstallerReference: Final[IntPtr] = ...
    """
    
    :return: 
    """
    PropertiesToSet: Final[IntPtr] = ...
    """
    
    :return: 
    """
    PropertiesToTest: Final[IntPtr] = ...
    """
    
    :return: 
    """
    Size: Final[int] = ...
    """
    
    :return: 
    """
    cPropertiesToSet: Final[IntPtr] = ...
    """
    
    :return: 
    """
    cPropertiesToTest: Final[IntPtr] = ...
    """
    
    :return: 
    """
    @overload
    def __init__(
        self,
        Deployment: IDefinitionAppId,
        Reference: StoreApplicationReference,
        SetProperties: Array[StoreOperationMetadataProperty],
    ):
        """

        :param Deployment:
        :param Reference:
        :param SetProperties:
        """
    @overload
    def __init__(
        self,
        Deployment: IDefinitionAppId,
        Reference: StoreApplicationReference,
        SetProperties: Array[StoreOperationMetadataProperty],
        TestProperties: Array[StoreOperationMetadataProperty],
    ):
        """

        :param Deployment:
        :param Reference:
        :param SetProperties:
        :param TestProperties:
        """
    def Destroy(self) -> None:
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

    class Disposition(Enum):
        """"""

        Failed: Disposition = ...
        """"""
        Set: Disposition = ...
        """"""

    class OpFlags(Enum):
        """"""

        Nothing: OpFlags = ...
        """"""

class StoreOperationStageComponent(ValueType):
    """"""

    Application: Final[IDefinitionAppId] = ...
    """
    
    :return: 
    """
    Component: Final[IDefinitionIdentity] = ...
    """
    
    :return: 
    """
    Flags: Final[StoreOperationStageComponent.OpFlags] = ...
    """
    
    :return: 
    """
    ManifestPath: Final[str] = ...
    """
    
    :return: 
    """
    Size: Final[int] = ...
    """
    
    :return: 
    """
    @overload
    def __init__(self, app: IDefinitionAppId, Manifest: str):
        """

        :param app:
        :param Manifest:
        """
    @overload
    def __init__(self, app: IDefinitionAppId, comp: IDefinitionIdentity, Manifest: str):
        """

        :param app:
        :param comp:
        :param Manifest:
        """
    def Destroy(self) -> None:
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

    class Disposition(Enum):
        """"""

        Failed: Disposition = ...
        """"""
        Installed: Disposition = ...
        """"""
        Refreshed: Disposition = ...
        """"""
        AlreadyInstalled: Disposition = ...
        """"""

    class OpFlags(Enum):
        """"""

        Nothing: OpFlags = ...
        """"""

class StoreOperationStageComponentFile(ValueType):
    """"""

    Application: Final[IDefinitionAppId] = ...
    """
    
    :return: 
    """
    Component: Final[IDefinitionIdentity] = ...
    """
    
    :return: 
    """
    ComponentRelativePath: Final[str] = ...
    """
    
    :return: 
    """
    Flags: Final[StoreOperationStageComponentFile.OpFlags] = ...
    """
    
    :return: 
    """
    Size: Final[int] = ...
    """
    
    :return: 
    """
    SourceFilePath: Final[str] = ...
    """
    
    :return: 
    """
    @overload
    def __init__(self, App: IDefinitionAppId, CompRelPath: str, SrcFile: str):
        """

        :param App:
        :param CompRelPath:
        :param SrcFile:
        """
    @overload
    def __init__(
        self, App: IDefinitionAppId, Component: IDefinitionIdentity, CompRelPath: str, SrcFile: str
    ):
        """

        :param App:
        :param Component:
        :param CompRelPath:
        :param SrcFile:
        """
    def Destroy(self) -> None:
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

    class Disposition(Enum):
        """"""

        Failed: Disposition = ...
        """"""
        Installed: Disposition = ...
        """"""
        Refreshed: Disposition = ...
        """"""
        AlreadyInstalled: Disposition = ...
        """"""

    class OpFlags(Enum):
        """"""

        Nothing: OpFlags = ...
        """"""

class StoreOperationUninstallDeployment(ValueType):
    """"""

    Application: Final[IDefinitionAppId] = ...
    """
    
    :return: 
    """
    Flags: Final[StoreOperationUninstallDeployment.OpFlags] = ...
    """
    
    :return: 
    """
    Reference: Final[IntPtr] = ...
    """
    
    :return: 
    """
    Size: Final[int] = ...
    """
    
    :return: 
    """
    def __init__(self, appid: IDefinitionAppId, AppRef: StoreApplicationReference):
        """

        :param appid:
        :param AppRef:
        """
    def Destroy(self) -> None:
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

    class Disposition(Enum):
        """"""

        Failed: Disposition = ...
        """"""
        DidNotExist: Disposition = ...
        """"""
        Uninstalled: Disposition = ...
        """"""

    class OpFlags(Enum):
        """"""

        Nothing: OpFlags = ...
        """"""

class StoreOperationUnpinDeployment(ValueType):
    """"""

    Application: Final[IDefinitionAppId] = ...
    """
    
    :return: 
    """
    Flags: Final[StoreOperationUnpinDeployment.OpFlags] = ...
    """
    
    :return: 
    """
    Reference: Final[IntPtr] = ...
    """
    
    :return: 
    """
    Size: Final[int] = ...
    """
    
    :return: 
    """
    def __init__(self, app: IDefinitionAppId, reference: StoreApplicationReference):
        """

        :param app:
        :param reference:
        """
    def Destroy(self) -> None:
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

    class Disposition(Enum):
        """"""

        Failed: Disposition = ...
        """"""
        Unpinned: Disposition = ...
        """"""

    class OpFlags(Enum):
        """"""

        Nothing: OpFlags = ...
        """"""

class StoreSubcategoryEnumeration(Object, IEnumerator):
    """"""

    def __init__(self, pI: IEnumSTORE_CATEGORY_SUBCATEGORY):
        """

        :param pI:
        """
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

class StoreTransaction(Object, IDisposable):
    """"""

    def __init__(self):
        """"""
    @property
    def Operations(self) -> Array[StoreTransactionOperation]:
        """

        :return:
        """
    @overload
    def Add(self, o: StoreOperationInstallDeployment) -> None:
        """

        :param o:
        """
    @overload
    def Add(self, o: StoreOperationPinDeployment) -> None:
        """

        :param o:
        """
    @overload
    def Add(self, o: StoreOperationScavenge) -> None:
        """

        :param o:
        """
    @overload
    def Add(self, o: StoreOperationSetCanonicalizationContext) -> None:
        """

        :param o:
        """
    @overload
    def Add(self, o: StoreOperationSetDeploymentMetadata) -> None:
        """

        :param o:
        """
    @overload
    def Add(self, o: StoreOperationStageComponent) -> None:
        """

        :param o:
        """
    @overload
    def Add(self, o: StoreOperationStageComponentFile) -> None:
        """

        :param o:
        """
    @overload
    def Add(self, o: StoreOperationUninstallDeployment) -> None:
        """

        :param o:
        """
    @overload
    def Add(self, o: StoreOperationUnpinDeployment) -> None:
        """

        :param o:
        """
    def Dispose(self) -> None:
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

class StoreTransactionData(ValueType):
    """"""

    DataPtr: Final[IntPtr] = ...
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

class StoreTransactionOperation(ValueType):
    """"""

    Data: Final[StoreTransactionData] = ...
    """
    
    :return: 
    """
    Operation: Final[StoreTransactionOperationType] = ...
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

class StoreTransactionOperationType(Enum):
    """"""

    Invalid: StoreTransactionOperationType = ...
    """"""
    SetCanonicalizationContext: StoreTransactionOperationType = ...
    """"""
    StageComponent: StoreTransactionOperationType = ...
    """"""
    PinDeployment: StoreTransactionOperationType = ...
    """"""
    UnpinDeployment: StoreTransactionOperationType = ...
    """"""
    StageComponentFile: StoreTransactionOperationType = ...
    """"""
    InstallDeployment: StoreTransactionOperationType = ...
    """"""
    UninstallDeployment: StoreTransactionOperationType = ...
    """"""
    SetDeploymentMetadata: StoreTransactionOperationType = ...
    """"""
    Scavenge: StoreTransactionOperationType = ...
    """"""
