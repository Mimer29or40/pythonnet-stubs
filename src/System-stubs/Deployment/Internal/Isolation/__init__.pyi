"""Automatically generated stubs for C# namespace: System.Deployment.Internal.Isolation."""

from abc import ABC
from collections.abc import Iterator
from typing import ClassVar
from typing import Final
from typing import overload

from System import Array
from System import Char
from System import DateTime
from System import Enum
from System import Guid
from System import IDisposable
from System import IntPtr
from System import Object
from System import String
from System import Type
from System import UInt32
from System import UInt64
from System import UIntPtr
from System import ValueType
from System.Collections import IEnumerator

from .Manifest import ICMS

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class BLOB(ValueType, IDisposable):
    """"""

    BlobData: Final[IntPtr]
    """"""
    Size: Final[int]
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CATEGORY(ValueType):
    """"""

    DefinitionIdentity: Final[IDefinitionIdentity]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CATEGORY_INSTANCE(ValueType):
    """"""

    DefinitionAppId_Application: Final[IDefinitionAppId]
    """"""
    XMLSnippet: Final[str]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CATEGORY_SUBCATEGORY(ValueType):
    """"""

    Subcategory: Final[str]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class IAPPIDAUTHORITY_ARE_DEFINITIONS_EQUAL_FLAGS(Enum):
    """"""

    IAPPIDAUTHORITY_ARE_DEFINITIONS_EQUAL_FLAG_IGNORE_VERSION: IAPPIDAUTHORITY_ARE_DEFINITIONS_EQUAL_FLAGS = ...
    """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class IAPPIDAUTHORITY_ARE_REFERENCES_EQUAL_FLAGS(Enum):
    """"""

    IAPPIDAUTHORITY_ARE_REFERENCES_EQUAL_FLAG_IGNORE_VERSION: IAPPIDAUTHORITY_ARE_REFERENCES_EQUAL_FLAGS = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IActContext(ABC):
    """"""
    def ApplicationBasePath(self, Flags: int, ApplicationPath: String) -> tuple[None, String]:
        """"""
    def CreateActContextFromCategoryInstance(
        self, dwFlags: int, CategoryInstance: CATEGORY_INSTANCE, ppCreatedAppContext: Object
    ) -> tuple[None, Object]:
        """"""
    def EnumCategories(
        self, Flags: int, CategoryToMatch: IReferenceIdentity, riid: Guid, EnumOut: Object
    ) -> tuple[None, Object]:
        """"""
    def EnumCategoryInstances(
        self,
        Flags: int,
        CategoryId: IDefinitionIdentity,
        Subcategory: str,
        riid: Guid,
        EnumOut: Object,
    ) -> tuple[None, Object]:
        """"""
    def EnumComponents(self, dwFlags: int, ppIdentityEnum: Object) -> tuple[None, Object]:
        """"""
    def EnumSubcategories(
        self,
        Flags: int,
        CategoryId: IDefinitionIdentity,
        SubcategoryPattern: str,
        riid: Guid,
        EnumOut: Object,
    ) -> tuple[None, Object]:
        """"""
    def FindComponentsByDefinition(
        self,
        dwFlags: int,
        ComponentCount: UIntPtr,
        Components: Array[IDefinitionIdentity],
        Indicies: Array[UIntPtr],
        Dispositions: Array[int],
    ) -> tuple[None, Array[UIntPtr], Array[int]]:
        """"""
    def FindComponentsByReference(
        self,
        dwFlags: int,
        Components: UIntPtr,
        References: Array[IReferenceIdentity],
        Indicies: Array[UIntPtr],
        Dispositions: Array[int],
    ) -> tuple[None, Array[UIntPtr], Array[int]]:
        """"""
    def FindReferenceInContext(
        self, dwFlags: int, Reference: IReferenceIdentity, MatchedDefinition: Object
    ) -> tuple[None, Object]:
        """"""
    def GetAppId(self, AppId: Object) -> tuple[None, Object]:
        """"""
    def GetApplicationProperties(
        self,
        Flags: int,
        cProperties: UIntPtr,
        PropertyNames: Array[str],
        PropertyValues: String,
        ComponentIndicies: UIntPtr,
    ) -> tuple[None, String, UIntPtr]:
        """"""
    def GetApplicationStateFilesystemLocation(
        self, dwFlags: int, Component: UIntPtr, pCoordinateList: IntPtr, ppszPath: String
    ) -> tuple[None, String]:
        """"""
    def GetComponentManifest(
        self, Flags: int, ComponentId: IDefinitionIdentity, riid: Guid, ManifestInteface: Object
    ) -> tuple[None, Object]:
        """"""
    def GetComponentPayloadPath(
        self, Flags: int, ComponentId: IDefinitionIdentity, PayloadPath: String
    ) -> tuple[None, String]:
        """"""
    def GetComponentStringTableStrings(
        self,
        Flags: int,
        ComponentIndex: IntPtr,
        StringCount: IntPtr,
        SourceStrings: Array[str],
        DestinationStrings: String,
        CultureFallbacks: IntPtr,
    ) -> tuple[None, Array[str], String]:
        """"""
    def PrepareForExecution(self, Inputs: IntPtr, Outputs: IntPtr) -> None:
        """"""
    def ReplaceStringMacros(
        self, Flags: int, Culture: str, ReplacementPattern: str, Replaced: String
    ) -> tuple[None, String]:
        """"""
    def SetApplicationRunningState(
        self, dwFlags: int, ulState: int, ulDisposition: UInt32
    ) -> tuple[None, UInt32]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IAppIdAuthority(ABC):
    """"""
    def AreDefinitionsEqual(
        self, Flags: int, Definition1: IDefinitionAppId, Definition2: IDefinitionAppId
    ) -> bool:
        """"""
    def AreReferencesEqual(
        self, Flags: int, Reference1: IReferenceAppId, Reference2: IReferenceAppId
    ) -> bool:
        """"""
    def AreTextualDefinitionsEqual(self, Flags: int, AppIdLeft: str, AppIdRight: str) -> bool:
        """"""
    def AreTextualReferencesEqual(self, Flags: int, AppIdLeft: str, AppIdRight: str) -> bool:
        """"""
    def CreateDefinition(self) -> IDefinitionAppId:
        """"""
    def CreateReference(self) -> IReferenceAppId:
        """"""
    def DefinitionToText(self, Flags: int, DefinitionAppId: IDefinitionAppId) -> str:
        """"""
    def DoesDefinitionMatchReference(
        self, Flags: int, DefinitionIdentity: IDefinitionAppId, ReferenceIdentity: IReferenceAppId
    ) -> bool:
        """"""
    def DoesTextualDefinitionMatchTextualReference(
        self, Flags: int, Definition: str, Reference: str
    ) -> bool:
        """"""
    def GenerateDefinitionKey(self, Flags: int, DefinitionIdentity: IDefinitionAppId) -> str:
        """"""
    def GenerateReferenceKey(self, Flags: int, ReferenceIdentity: IReferenceAppId) -> str:
        """"""
    def HashDefinition(self, Flags: int, DefinitionIdentity: IDefinitionAppId) -> int:
        """"""
    def HashReference(self, Flags: int, ReferenceIdentity: IReferenceAppId) -> int:
        """"""
    def ReferenceToText(self, Flags: int, ReferenceAppId: IReferenceAppId) -> str:
        """"""
    def TextToDefinition(self, Flags: int, Identity: str) -> IDefinitionAppId:
        """"""
    def TextToReference(self, Flags: int, Identity: str) -> IReferenceAppId:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ICDF(ABC):
    """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def _NewEnum(self) -> object:
        """"""
    def GetItem(self, SectionId: int) -> object:
        """"""
    def GetRootSection(self, SectionId: int) -> ISection:
        """"""
    def GetRootSectionEntry(self, SectionId: int) -> ISectionEntry:
        """"""
    def __len__(self) -> int:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IDENTITY_ATTRIBUTE(ValueType):
    """"""

    Name: Final[str]
    """"""
    Namespace: Final[str]
    """"""
    Value: Final[str]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IDefinitionAppId(ABC):
    """"""
    def EnumAppPath(self) -> IEnumDefinitionIdentity:
        """"""
    def SetAppPath(
        self, cIDefinitionIdentity: int, DefinitionIdentity: Array[IDefinitionIdentity]
    ) -> None:
        """"""
    def put_Codebase(self, CodeBase: str) -> None:
        """"""
    def put_SubscriptionId(self, Subscription: str) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IDefinitionIdentity(ABC):
    """"""
    def Clone(self, cDeltas: IntPtr, Deltas: Array[IDENTITY_ATTRIBUTE]) -> IDefinitionIdentity:
        """"""
    def EnumAttributes(self) -> IEnumIDENTITY_ATTRIBUTE:
        """"""
    def GetAttribute(self, Namespace: str, Name: str) -> str:
        """"""
    def SetAttribute(self, Namespace: str, Name: str, Value: str) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IEnumDefinitionIdentity(ABC):
    """"""
    def Clone(self) -> IEnumDefinitionIdentity:
        """"""
    def Next(
        self, celt: int, DefinitionIdentity: Array[IDefinitionIdentity]
    ) -> tuple[int, Array[IDefinitionIdentity]]:
        """"""
    def Reset(self) -> None:
        """"""
    def Skip(self, celt: int) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IEnumIDENTITY_ATTRIBUTE(ABC):
    """"""
    def Clone(self) -> IEnumIDENTITY_ATTRIBUTE:
        """"""
    def CurrentIntoBuffer(self, Available: IntPtr, Data: Array[int]) -> tuple[IntPtr, Array[int]]:
        """"""
    def Next(
        self, celt: int, rgAttributes: Array[IDENTITY_ATTRIBUTE]
    ) -> tuple[int, Array[IDENTITY_ATTRIBUTE]]:
        """"""
    def Reset(self) -> None:
        """"""
    def Skip(self, celt: int) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IEnumReferenceIdentity(ABC):
    """"""
    def Clone(self) -> IEnumReferenceIdentity:
        """"""
    def Next(
        self, celt: int, ReferenceIdentity: Array[IReferenceIdentity]
    ) -> tuple[int, Array[IReferenceIdentity]]:
        """"""
    def Reset(self) -> None:
        """"""
    def Skip(self, celt: int) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IEnumSTORE_ASSEMBLY(ABC):
    """"""
    def Clone(self) -> IEnumSTORE_ASSEMBLY:
        """"""
    def Next(self, celt: int, rgelt: Array[STORE_ASSEMBLY]) -> tuple[int, Array[STORE_ASSEMBLY]]:
        """"""
    def Reset(self) -> None:
        """"""
    def Skip(self, celt: int) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IEnumSTORE_ASSEMBLY_FILE(ABC):
    """"""
    def Clone(self) -> IEnumSTORE_ASSEMBLY_FILE:
        """"""
    def Next(
        self, celt: int, rgelt: Array[STORE_ASSEMBLY_FILE]
    ) -> tuple[int, Array[STORE_ASSEMBLY_FILE]]:
        """"""
    def Reset(self) -> None:
        """"""
    def Skip(self, celt: int) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IEnumSTORE_ASSEMBLY_INSTALLATION_REFERENCE(ABC):
    """"""
    def Clone(self) -> IEnumSTORE_ASSEMBLY_INSTALLATION_REFERENCE:
        """"""
    def Next(
        self, celt: int, rgelt: Array[StoreApplicationReference]
    ) -> tuple[int, Array[StoreApplicationReference]]:
        """"""
    def Reset(self) -> None:
        """"""
    def Skip(self, celt: int) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IEnumSTORE_CATEGORY(ABC):
    """"""
    def Clone(self) -> IEnumSTORE_CATEGORY:
        """"""
    def Next(
        self, celt: int, rgElements: Array[STORE_CATEGORY]
    ) -> tuple[int, Array[STORE_CATEGORY]]:
        """"""
    def Reset(self) -> None:
        """"""
    def Skip(self, ulElements: int) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IEnumSTORE_CATEGORY_INSTANCE(ABC):
    """"""
    def Clone(self) -> IEnumSTORE_CATEGORY_INSTANCE:
        """"""
    def Next(
        self, ulElements: int, rgInstances: Array[STORE_CATEGORY_INSTANCE]
    ) -> tuple[int, Array[STORE_CATEGORY_INSTANCE]]:
        """"""
    def Reset(self) -> None:
        """"""
    def Skip(self, ulElements: int) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IEnumSTORE_CATEGORY_SUBCATEGORY(ABC):
    """"""
    def Clone(self) -> IEnumSTORE_CATEGORY_SUBCATEGORY:
        """"""
    def Next(
        self, celt: int, rgElements: Array[STORE_CATEGORY_SUBCATEGORY]
    ) -> tuple[int, Array[STORE_CATEGORY_SUBCATEGORY]]:
        """"""
    def Reset(self) -> None:
        """"""
    def Skip(self, ulElements: int) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IEnumSTORE_DEPLOYMENT_METADATA(ABC):
    """"""
    def Clone(self) -> IEnumSTORE_DEPLOYMENT_METADATA:
        """"""
    def Next(
        self, celt: int, AppIds: Array[IDefinitionAppId]
    ) -> tuple[int, Array[IDefinitionAppId]]:
        """"""
    def Reset(self) -> None:
        """"""
    def Skip(self, celt: int) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IEnumSTORE_DEPLOYMENT_METADATA_PROPERTY(ABC):
    """"""
    def Clone(self) -> IEnumSTORE_DEPLOYMENT_METADATA_PROPERTY:
        """"""
    def Next(
        self, celt: int, AppIds: Array[StoreOperationMetadataProperty]
    ) -> tuple[int, Array[StoreOperationMetadataProperty]]:
        """"""
    def Reset(self) -> None:
        """"""
    def Skip(self, celt: int) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IEnumUnknown(ABC):
    """"""
    def Clone(self, enumUnknown: IEnumUnknown) -> tuple[int, IEnumUnknown]:
        """"""
    def Next(
        self, celt: int, rgelt: Array[object], celtFetched: UInt32
    ) -> tuple[int, Array[object]]:
        """"""
    def Reset(self) -> int:
        """"""
    def Skip(self, celt: int) -> int:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class IIDENTITYAUTHORITY_DEFINITION_IDENTITY_TO_TEXT_FLAGS(Enum):
    """"""

    IIDENTITYAUTHORITY_DEFINITION_IDENTITY_TO_TEXT_FLAG_CANONICAL: IIDENTITYAUTHORITY_DEFINITION_IDENTITY_TO_TEXT_FLAGS = ...
    """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class IIDENTITYAUTHORITY_DOES_DEFINITION_MATCH_REFERENCE_FLAGS(Enum):
    """"""

    IIDENTITYAUTHORITY_DOES_DEFINITION_MATCH_REFERENCE_FLAG_EXACT_MATCH_REQUIRED: IIDENTITYAUTHORITY_DOES_DEFINITION_MATCH_REFERENCE_FLAGS = ...
    """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class IIDENTITYAUTHORITY_REFERENCE_IDENTITY_TO_TEXT_FLAGS(Enum):
    """"""

    IIDENTITYAUTHORITY_REFERENCE_IDENTITY_TO_TEXT_FLAG_CANONICAL: IIDENTITYAUTHORITY_REFERENCE_IDENTITY_TO_TEXT_FLAGS = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IIdentityAuthority(ABC):
    """"""
    def AreDefinitionsEqual(
        self, Flags: int, Definition1: IDefinitionIdentity, Definition2: IDefinitionIdentity
    ) -> bool:
        """"""
    def AreReferencesEqual(
        self, Flags: int, Reference1: IReferenceIdentity, Reference2: IReferenceIdentity
    ) -> bool:
        """"""
    def AreTextualDefinitionsEqual(self, Flags: int, IdentityLeft: str, IdentityRight: str) -> bool:
        """"""
    def AreTextualReferencesEqual(self, Flags: int, IdentityLeft: str, IdentityRight: str) -> bool:
        """"""
    def CreateDefinition(self) -> IDefinitionIdentity:
        """"""
    def CreateReference(self) -> IReferenceIdentity:
        """"""
    def DefinitionToText(self, Flags: int, DefinitionIdentity: IDefinitionIdentity) -> str:
        """"""
    def DefinitionToTextBuffer(
        self,
        Flags: int,
        DefinitionIdentity: IDefinitionIdentity,
        BufferSize: int,
        Buffer: Array[Char],
    ) -> tuple[int, Array[Char]]:
        """"""
    def DoesDefinitionMatchReference(
        self,
        Flags: int,
        DefinitionIdentity: IDefinitionIdentity,
        ReferenceIdentity: IReferenceIdentity,
    ) -> bool:
        """"""
    def DoesTextualDefinitionMatchTextualReference(
        self, Flags: int, Definition: str, Reference: str
    ) -> bool:
        """"""
    def GenerateDefinitionKey(self, Flags: int, DefinitionIdentity: IDefinitionIdentity) -> str:
        """"""
    def GenerateReferenceKey(self, Flags: int, ReferenceIdentity: IReferenceIdentity) -> str:
        """"""
    def HashDefinition(self, Flags: int, DefinitionIdentity: IDefinitionIdentity) -> int:
        """"""
    def HashReference(self, Flags: int, ReferenceIdentity: IReferenceIdentity) -> int:
        """"""
    def ReferenceToText(self, Flags: int, ReferenceIdentity: IReferenceIdentity) -> str:
        """"""
    def ReferenceToTextBuffer(
        self,
        Flags: int,
        ReferenceIdentity: IReferenceIdentity,
        BufferSize: int,
        Buffer: Array[Char],
    ) -> tuple[int, Array[Char]]:
        """"""
    def TextToDefinition(self, Flags: int, Identity: str) -> IDefinitionIdentity:
        """"""
    def TextToReference(self, Flags: int, Identity: str) -> IReferenceIdentity:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IManifestInformation(ABC):
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IManifestParseErrorCallback(ABC):
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
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IReferenceAppId(ABC):
    """"""
    def EnumAppPath(self) -> IEnumReferenceIdentity:
        """"""
    def put_Codebase(self, CodeBase: str) -> None:
        """"""
    def put_SubscriptionId(self, Subscription: str) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IReferenceIdentity(ABC):
    """"""
    def Clone(self, cDeltas: IntPtr, Deltas: Array[IDENTITY_ATTRIBUTE]) -> IReferenceIdentity:
        """"""
    def EnumAttributes(self) -> IEnumIDENTITY_ATTRIBUTE:
        """"""
    def GetAttribute(self, Namespace: str, Name: str) -> str:
        """"""
    def SetAttribute(self, Namespace: str, Name: str, Value: str) -> None:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class ISTORE_BIND_REFERENCE_TO_ASSEMBLY_FLAGS(Enum):
    """"""

    ISTORE_BIND_REFERENCE_TO_ASSEMBLY_FLAG_FORCE_LIBRARY_SEMANTICS: ISTORE_BIND_REFERENCE_TO_ASSEMBLY_FLAGS = ...
    """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class ISTORE_ENUM_ASSEMBLIES_FLAGS(Enum):
    """"""

    ISTORE_ENUM_ASSEMBLIES_FLAG_LIMIT_TO_VISIBLE_ONLY: ISTORE_ENUM_ASSEMBLIES_FLAGS = ...
    """"""
    ISTORE_ENUM_ASSEMBLIES_FLAG_MATCH_SERVICING: ISTORE_ENUM_ASSEMBLIES_FLAGS = ...
    """"""
    ISTORE_ENUM_ASSEMBLIES_FLAG_FORCE_LIBRARY_SEMANTICS: ISTORE_ENUM_ASSEMBLIES_FLAGS = ...
    """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class ISTORE_ENUM_FILES_FLAGS(Enum):
    """"""

    ISTORE_ENUM_FILES_FLAG_INCLUDE_INSTALLED_FILES: ISTORE_ENUM_FILES_FLAGS = ...
    """"""
    ISTORE_ENUM_FILES_FLAG_INCLUDE_MISSING_FILES: ISTORE_ENUM_FILES_FLAGS = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ISection(ABC):
    """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def SectionID(self) -> int:
        """"""
    @property
    def SectionName(self) -> str:
        """"""
    @property
    def _NewEnum(self) -> object:
        """"""
    def __len__(self) -> int:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ISectionEntry(ABC):
    """"""
    def GetField(self, fieldId: int) -> object:
        """"""
    def GetFieldName(self, fieldId: int) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ISectionWithReferenceIdentityKey(ABC):
    """"""
    def Lookup(
        self, ReferenceIdentityKey: IReferenceIdentity, ppUnknown: Object
    ) -> tuple[None, Object]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ISectionWithStringKey(ABC):
    """"""
    @property
    def IsCaseInsensitive(self) -> bool:
        """"""
    def Lookup(self, wzStringKey: str, ppUnknown: Object) -> tuple[None, Object]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IStateManager(ABC):
    """"""
    def GetApplicationStateFilesystemLocation(
        self,
        Flags: int,
        Appidentity: IDefinitionAppId,
        ComponentIdentity: IDefinitionIdentity,
        Coordinates: UIntPtr,
        Path: String,
    ) -> tuple[None, String]:
        """"""
    def PrepareApplicationState(self, Inputs: UIntPtr, Outputs: UIntPtr) -> None:
        """"""
    def Scavenge(self, Flags: int, Disposition: UInt32) -> tuple[None, UInt32]:
        """"""
    def SetApplicationRunningState(
        self, Flags: int, Context: IActContext, RunningState: int, Disposition: UInt32
    ) -> tuple[None, UInt32]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IStore(ABC):
    """"""
    def BindDefinitions(
        self,
        Flags: int,
        Count: IntPtr,
        DefsToBind: Array[IDefinitionIdentity],
        DeploymentsToIgnore: int,
        DefsToIgnore: Array[IDefinitionIdentity],
    ) -> IntPtr:
        """"""
    def BindReferenceToAssembly(
        self,
        Flags: int,
        ReferenceIdentity: IReferenceIdentity,
        cDeploymentsToIgnore: int,
        DefinitionIdentity_DeploymentsToIgnore: Array[IDefinitionIdentity],
        riid: Guid,
    ) -> object:
        """"""
    def CalculateDelimiterOfDeploymentsBasedOnQuota(
        self,
        dwFlags: int,
        cDeployments: IntPtr,
        rgpIDefinitionAppId_Deployments: Array[IDefinitionAppId],
        InstallerReference: StoreApplicationReference,
        ulonglongQuota: int,
        Delimiter: IntPtr,
        SizeSharedWithExternalDeployment: UInt64,
        SizeConsumedByInputDeploymentArray: UInt64,
    ) -> tuple[None, IntPtr, UInt64, UInt64]:
        """"""
    def EnumAssemblies(
        self, Flags: int, ReferenceIdentity_ToMatch: IReferenceIdentity, riid: Guid
    ) -> object:
        """"""
    def EnumCategories(
        self, Flags: int, ReferenceIdentity_ToMatch: IReferenceIdentity, riid: Guid
    ) -> object:
        """"""
    def EnumCategoryInstances(
        self, Flags: int, CategoryId: IDefinitionIdentity, SubcategoryPath: str, riid: Guid
    ) -> object:
        """"""
    def EnumFiles(self, Flags: int, DefinitionIdentity: IDefinitionIdentity, riid: Guid) -> object:
        """"""
    def EnumInstallationReferences(
        self, Flags: int, DefinitionIdentity: IDefinitionIdentity, riid: Guid
    ) -> object:
        """"""
    def EnumInstallerDeploymentMetadata(
        self, Flags: int, Reference: StoreApplicationReference, Filter: IReferenceAppId, riid: Guid
    ) -> object:
        """"""
    def EnumInstallerDeploymentMetadataProperties(
        self, Flags: int, Reference: StoreApplicationReference, Filter: IDefinitionAppId, riid: Guid
    ) -> object:
        """"""
    def EnumPrivateFiles(
        self,
        Flags: int,
        Application: IDefinitionAppId,
        DefinitionIdentity: IDefinitionIdentity,
        riid: Guid,
    ) -> object:
        """"""
    def EnumSubcategories(
        self, Flags: int, CategoryId: IDefinitionIdentity, SubcategoryPathPattern: str, riid: Guid
    ) -> object:
        """"""
    def GetAssemblyInformation(
        self, Flags: int, DefinitionIdentity: IDefinitionIdentity, riid: Guid
    ) -> object:
        """"""
    def GetDeploymentProperty(
        self,
        Flags: int,
        DeploymentInPackage: IDefinitionAppId,
        Reference: StoreApplicationReference,
        PropertySet: Guid,
        pcwszPropertyName: str,
        blob: BLOB,
    ) -> tuple[None, BLOB]:
        """"""
    def LockApplicationPath(
        self, Flags: int, ApId: IDefinitionAppId, Cookie: IntPtr
    ) -> tuple[str, IntPtr]:
        """"""
    def LockAssemblyPath(
        self, Flags: int, DefinitionIdentity: IDefinitionIdentity, Cookie: IntPtr
    ) -> tuple[str, IntPtr]:
        """"""
    def QueryChangeID(self, DefinitionIdentity: IDefinitionIdentity) -> int:
        """"""
    def ReleaseApplicationPath(self, Cookie: IntPtr) -> None:
        """"""
    def ReleaseAssemblyPath(self, Cookie: IntPtr) -> None:
        """"""
    def Transact(
        self,
        cOperation: IntPtr,
        rgOperations: Array[StoreTransactionOperation],
        rgDispositions: Array[int],
        rgResults: Array[int],
    ) -> tuple[None, Array[int], Array[int]]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IStore_BindingResult(ValueType):
    """"""

    CacheCoherencyGuid: Final[Guid]
    """"""
    Component: Final[IStore_BindingResult_BoundVersion]
    """"""
    Disposition: Final[int]
    """"""
    Flags: Final[int]
    """"""
    Reserved: Final[IntPtr]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IStore_BindingResult_BoundVersion(ValueType):
    """"""

    Build: Final[int]
    """"""
    Major: Final[int]
    """"""
    Minor: Final[int]
    """"""
    Revision: Final[int]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IsolationInterop(ABC, Object):
    """"""

    GUID_SXS_INSTALL_REFERENCE_SCHEME_OPAQUESTRING: ClassVar[Guid]
    """"""
    IID_ICMS: ClassVar[Guid]
    """"""
    IID_IDefinitionIdentity: ClassVar[Guid]
    """"""
    IID_IEnumSTORE_ASSEMBLY: ClassVar[Guid]
    """"""
    IID_IEnumSTORE_ASSEMBLY_FILE: ClassVar[Guid]
    """"""
    IID_IEnumSTORE_CATEGORY: ClassVar[Guid]
    """"""
    IID_IEnumSTORE_CATEGORY_INSTANCE: ClassVar[Guid]
    """"""
    IID_IEnumSTORE_DEPLOYMENT_METADATA: ClassVar[Guid]
    """"""
    IID_IEnumSTORE_DEPLOYMENT_METADATA_PROPERTY: ClassVar[Guid]
    """"""
    IID_IManifestInformation: ClassVar[Guid]
    """"""
    IID_IStore: ClassVar[Guid]
    """"""
    IsolationDllName: ClassVar[str]
    """"""
    SXS_INSTALL_REFERENCE_SCHEME_SXS_STRONGNAME_SIGNED_PRIVATE_ASSEMBLY: ClassVar[Guid]
    """"""
    @classmethod
    @property
    def AppIdAuthority(cls) -> IAppIdAuthority:
        """"""
    @classmethod
    @property
    def IdentityAuthority(cls) -> IIdentityAuthority:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def GetUserStore(cls) -> Store:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class STORE_ASSEMBLY(ValueType):
    """"""

    AssemblySize: Final[int]
    """"""
    ChangeId: Final[int]
    """"""
    DefinitionIdentity: Final[IDefinitionIdentity]
    """"""
    ManifestPath: Final[str]
    """"""
    Status: Final[int]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class STORE_ASSEMBLY_FILE(ValueType):
    """"""

    FileName: Final[str]
    """"""
    FileStatusFlags: Final[int]
    """"""
    Flags: Final[int]
    """"""
    Size: Final[int]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class STORE_ASSEMBLY_FILE_STATUS_FLAGS(Enum):
    """"""

    STORE_ASSEMBLY_FILE_STATUS_FLAG_PRESENT: STORE_ASSEMBLY_FILE_STATUS_FLAGS = ...
    """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class STORE_ASSEMBLY_STATUS_FLAGS(Enum):
    """"""

    STORE_ASSEMBLY_STATUS_MANIFEST_ONLY: STORE_ASSEMBLY_STATUS_FLAGS = ...
    """"""
    STORE_ASSEMBLY_STATUS_PAYLOAD_RESIDENT: STORE_ASSEMBLY_STATUS_FLAGS = ...
    """"""
    STORE_ASSEMBLY_STATUS_PARTIAL_INSTALL: STORE_ASSEMBLY_STATUS_FLAGS = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class STORE_CATEGORY(ValueType):
    """"""

    DefinitionIdentity: Final[IDefinitionIdentity]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class STORE_CATEGORY_INSTANCE(ValueType):
    """"""

    DefinitionAppId_Application: Final[IDefinitionAppId]
    """"""
    XMLSnippet: Final[str]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class STORE_CATEGORY_SUBCATEGORY(ValueType):
    """"""

    Subcategory: Final[str]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class StateManager_RunningState(Enum):
    """"""

    Undefined: StateManager_RunningState = ...
    """"""
    Starting: StateManager_RunningState = ...
    """"""
    Running: StateManager_RunningState = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class Store(Object):
    """"""
    def __init__(self, pStore: IStore) -> None:
        """"""
    @property
    def InternalStore(self) -> IStore:
        """"""
    def BindReferenceToAssemblyIdentity(
        self,
        Flags: int,
        ReferenceIdentity: IReferenceIdentity,
        cDeploymentsToIgnore: int,
        DefinitionIdentity_DeploymentsToIgnore: Array[IDefinitionIdentity],
    ) -> IDefinitionIdentity:
        """"""
    def BindReferenceToAssemblyManifest(
        self,
        Flags: int,
        ReferenceIdentity: IReferenceIdentity,
        cDeploymentsToIgnore: int,
        DefinitionIdentity_DeploymentsToIgnore: Array[IDefinitionIdentity],
    ) -> ICMS:
        """"""
    def CalculateDelimiterOfDeploymentsBasedOnQuota(
        self,
        dwFlags: int,
        cDeployments: int,
        rgpIDefinitionAppId_Deployments: Array[IDefinitionAppId],
        InstallerReference: StoreApplicationReference,
        ulonglongQuota: int,
        Delimiter: UInt32,
        SizeSharedWithExternalDeployment: UInt64,
        SizeConsumedByInputDeploymentArray: UInt64,
    ) -> None:
        """"""
    @overload
    def EnumAssemblies(self, Flags: Store.EnumAssembliesFlags) -> StoreAssemblyEnumeration:
        """"""
    @overload
    def EnumAssemblies(
        self, Flags: Store.EnumAssembliesFlags, refToMatch: IReferenceIdentity
    ) -> StoreAssemblyEnumeration:
        """"""
    def EnumCategories(
        self, Flags: Store.EnumCategoriesFlags, CategoryMatch: IReferenceIdentity
    ) -> StoreCategoryEnumeration:
        """"""
    def EnumCategoryInstances(
        self, Flags: Store.EnumCategoryInstancesFlags, Category: IDefinitionIdentity, SubCat: str
    ) -> StoreCategoryInstanceEnumeration:
        """"""
    def EnumFiles(
        self, Flags: Store.EnumAssemblyFilesFlags, Assembly: IDefinitionIdentity
    ) -> StoreAssemblyFileEnumeration:
        """"""
    def EnumInstallationReferences(
        self, Flags: Store.EnumAssemblyInstallReferenceFlags, Assembly: IDefinitionIdentity
    ) -> IEnumSTORE_ASSEMBLY_INSTALLATION_REFERENCE:
        """"""
    def EnumInstallerDeploymentProperties(
        self,
        InstallerId: Guid,
        InstallerName: str,
        InstallerMetadata: str,
        Deployment: IDefinitionAppId,
    ) -> StoreDeploymentMetadataPropertyEnumeration:
        """"""
    def EnumInstallerDeployments(
        self,
        InstallerId: Guid,
        InstallerName: str,
        InstallerMetadata: str,
        DeploymentFilter: IReferenceAppId,
    ) -> StoreDeploymentMetadataEnumeration:
        """"""
    def EnumPrivateFiles(
        self,
        Flags: Store.EnumApplicationPrivateFiles,
        Application: IDefinitionAppId,
        Assembly: IDefinitionIdentity,
    ) -> StoreAssemblyFileEnumeration:
        """"""
    @overload
    def EnumSubcategories(
        self, Flags: Store.EnumSubcategoriesFlags, CategoryMatch: IDefinitionIdentity
    ) -> StoreSubcategoryEnumeration:
        """"""
    @overload
    def EnumSubcategories(
        self, Flags: Store.EnumSubcategoriesFlags, Category: IDefinitionIdentity, SearchPattern: str
    ) -> StoreSubcategoryEnumeration:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetAssemblyIdentity(
        self, Flags: int, DefinitionIdentity: IDefinitionIdentity
    ) -> IDefinitionIdentity:
        """"""
    def GetAssemblyManifest(self, Flags: int, DefinitionIdentity: IDefinitionIdentity) -> ICMS:
        """"""
    def GetDeploymentProperty(
        self,
        Flags: Store.GetPackagePropertyFlags,
        Deployment: IDefinitionAppId,
        Reference: StoreApplicationReference,
        PropertySet: Guid,
        PropertyName: str,
    ) -> Array[int]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def LockApplicationPath(self, app: IDefinitionAppId) -> Store.IPathLock:
        """"""
    def LockAssemblyPath(self, asm: IDefinitionIdentity) -> Store.IPathLock:
        """"""
    def QueryChangeID(self, asm: IDefinitionIdentity) -> int:
        """"""
    def ToString(self) -> str:
        """"""
    def Transact(self, operations: Array[StoreTransactionOperation]) -> Array[int]:
        """"""
    # noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
    class EnumApplicationPrivateFiles(Enum):
        """"""

        Nothing: Store.EnumApplicationPrivateFiles = ...
        """"""
        IncludeInstalled: Store.EnumApplicationPrivateFiles = ...
        """"""
        IncludeMissing: Store.EnumApplicationPrivateFiles = ...
        """"""

    # noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
    class EnumAssembliesFlags(Enum):
        """"""

        Nothing: Store.EnumAssembliesFlags = ...
        """"""
        VisibleOnly: Store.EnumAssembliesFlags = ...
        """"""
        MatchServicing: Store.EnumAssembliesFlags = ...
        """"""
        ForceLibrarySemantics: Store.EnumAssembliesFlags = ...
        """"""

    # noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
    class EnumAssemblyFilesFlags(Enum):
        """"""

        Nothing: Store.EnumAssemblyFilesFlags = ...
        """"""
        IncludeInstalled: Store.EnumAssemblyFilesFlags = ...
        """"""
        IncludeMissing: Store.EnumAssemblyFilesFlags = ...
        """"""

    # noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
    class EnumAssemblyInstallReferenceFlags(Enum):
        """"""

        Nothing: Store.EnumAssemblyInstallReferenceFlags = ...
        """"""

    # noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
    class EnumCategoriesFlags(Enum):
        """"""

        Nothing: Store.EnumCategoriesFlags = ...
        """"""

    # noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
    class EnumCategoryInstancesFlags(Enum):
        """"""

        Nothing: Store.EnumCategoryInstancesFlags = ...
        """"""

    # noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
    class EnumSubcategoriesFlags(Enum):
        """"""

        Nothing: Store.EnumSubcategoriesFlags = ...
        """"""

    # noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
    class GetPackagePropertyFlags(Enum):
        """"""

        Nothing: Store.GetPackagePropertyFlags = ...
        """"""

    # noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
    class IPathLock(ABC, IDisposable):
        """"""
        @property
        def Path(self) -> str:
            """"""
        def Dispose(self) -> None:
            """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class StoreApplicationReference(ValueType):
    """"""

    Flags: Final[StoreApplicationReference.RefFlags]
    """"""
    GuidScheme: Final[Guid]
    """"""
    Identifier: Final[str]
    """"""
    NonCanonicalData: Final[str]
    """"""
    Size: Final[int]
    """"""
    def __init__(self, RefScheme: Guid, Id: str, NcData: str) -> None:
        """"""
    @classmethod
    def Destroy(cls, ip: IntPtr) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToIntPtr(self) -> IntPtr:
        """"""
    def ToString(self) -> str:
        """"""
    # noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
    class RefFlags(Enum):
        """"""

        Nothing: StoreApplicationReference.RefFlags = ...
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class StoreAssemblyEnumeration(Object, IEnumerator):
    """"""
    def __init__(self, pI: IEnumSTORE_ASSEMBLY) -> None:
        """"""
    @property
    def Current(self) -> STORE_ASSEMBLY:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator:
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
    def __iter__(self) -> Iterator:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class StoreAssemblyFileEnumeration(Object, IEnumerator):
    """"""
    def __init__(self, pI: IEnumSTORE_ASSEMBLY_FILE) -> None:
        """"""
    @property
    def Current(self) -> STORE_ASSEMBLY_FILE:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator:
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
    def __iter__(self) -> Iterator:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class StoreCategoryEnumeration(Object, IEnumerator):
    """"""
    def __init__(self, pI: IEnumSTORE_CATEGORY) -> None:
        """"""
    @property
    def Current(self) -> STORE_CATEGORY:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator:
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
    def __iter__(self) -> Iterator:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class StoreCategoryInstanceEnumeration(Object, IEnumerator):
    """"""
    def __init__(self, pI: IEnumSTORE_CATEGORY_INSTANCE) -> None:
        """"""
    @property
    def Current(self) -> STORE_CATEGORY_INSTANCE:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator:
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
    def __iter__(self) -> Iterator:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class StoreDeploymentMetadataEnumeration(Object, IEnumerator):
    """"""
    def __init__(self, pI: IEnumSTORE_DEPLOYMENT_METADATA) -> None:
        """"""
    @property
    def Current(self) -> IDefinitionAppId:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator:
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
    def __iter__(self) -> Iterator:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class StoreDeploymentMetadataPropertyEnumeration(Object, IEnumerator):
    """"""
    def __init__(self, pI: IEnumSTORE_DEPLOYMENT_METADATA_PROPERTY) -> None:
        """"""
    @property
    def Current(self) -> StoreOperationMetadataProperty:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator:
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
    def __iter__(self) -> Iterator:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class StoreOperationInstallDeployment(ValueType):
    """"""

    Application: Final[IDefinitionAppId]
    """"""
    Flags: Final[StoreOperationInstallDeployment.OpFlags]
    """"""
    Reference: Final[IntPtr]
    """"""
    Size: Final[int]
    """"""
    @overload
    def __init__(self, App: IDefinitionAppId, reference: StoreApplicationReference) -> None:
        """"""
    @overload
    def __init__(
        self, App: IDefinitionAppId, UninstallOthers: bool, reference: StoreApplicationReference
    ) -> None:
        """"""
    def Destroy(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    # noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
    class Disposition(Enum):
        """"""

        Failed: StoreOperationInstallDeployment.Disposition = ...
        """"""
        AlreadyInstalled: StoreOperationInstallDeployment.Disposition = ...
        """"""
        Installed: StoreOperationInstallDeployment.Disposition = ...
        """"""

    # noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
    class OpFlags(Enum):
        """"""

        Nothing: StoreOperationInstallDeployment.OpFlags = ...
        """"""
        UninstallOthers: StoreOperationInstallDeployment.OpFlags = ...
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class StoreOperationMetadataProperty(ValueType):
    """"""

    GuidPropertySet: Final[Guid]
    """"""
    Name: Final[str]
    """"""
    Value: Final[str]
    """"""
    ValueSize: Final[IntPtr]
    """"""
    @overload
    def __init__(self, PropertySet: Guid, Name: str) -> None:
        """"""
    @overload
    def __init__(self, PropertySet: Guid, Name: str, Value: str) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class StoreOperationPinDeployment(ValueType):
    """"""

    Application: Final[IDefinitionAppId]
    """"""
    ExpirationTime: Final[int]
    """"""
    Flags: Final[StoreOperationPinDeployment.OpFlags]
    """"""
    Reference: Final[IntPtr]
    """"""
    Size: Final[int]
    """"""
    @overload
    def __init__(self, AppId: IDefinitionAppId, Ref: StoreApplicationReference) -> None:
        """"""
    @overload
    def __init__(
        self, AppId: IDefinitionAppId, Expiry: DateTime, Ref: StoreApplicationReference
    ) -> None:
        """"""
    def Destroy(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    # noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
    class Disposition(Enum):
        """"""

        Failed: StoreOperationPinDeployment.Disposition = ...
        """"""
        Pinned: StoreOperationPinDeployment.Disposition = ...
        """"""

    # noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
    class OpFlags(Enum):
        """"""

        Nothing: StoreOperationPinDeployment.OpFlags = ...
        """"""
        NeverExpires: StoreOperationPinDeployment.OpFlags = ...
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class StoreOperationScavenge(ValueType):
    """"""

    ComponentCountLimit: Final[int]
    """"""
    Flags: Final[StoreOperationScavenge.OpFlags]
    """"""
    RuntimeLimit: Final[int]
    """"""
    Size: Final[int]
    """"""
    SizeReclaimationLimit: Final[int]
    """"""
    @overload
    def __init__(self, Light: bool, SizeLimit: int, RunLimit: int, ComponentLimit: int) -> None:
        """"""
    @overload
    def __init__(self, Light: bool) -> None:
        """"""
    def Destroy(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    # noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
    class OpFlags(Enum):
        """"""

        Nothing: StoreOperationScavenge.OpFlags = ...
        """"""
        Light: StoreOperationScavenge.OpFlags = ...
        """"""
        LimitSize: StoreOperationScavenge.OpFlags = ...
        """"""
        LimitTime: StoreOperationScavenge.OpFlags = ...
        """"""
        LimitCount: StoreOperationScavenge.OpFlags = ...
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class StoreOperationSetCanonicalizationContext(ValueType):
    """"""

    BaseAddressFilePath: Final[str]
    """"""
    ExportsFilePath: Final[str]
    """"""
    Flags: Final[StoreOperationSetCanonicalizationContext.OpFlags]
    """"""
    Size: Final[int]
    """"""
    def __init__(self, Bases: str, Exports: str) -> None:
        """"""
    def Destroy(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    # noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
    class OpFlags(Enum):
        """"""

        Nothing: StoreOperationSetCanonicalizationContext.OpFlags = ...
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class StoreOperationSetDeploymentMetadata(ValueType):
    """"""

    Deployment: Final[IDefinitionAppId]
    """"""
    Flags: Final[StoreOperationSetDeploymentMetadata.OpFlags]
    """"""
    InstallerReference: Final[IntPtr]
    """"""
    PropertiesToSet: Final[IntPtr]
    """"""
    PropertiesToTest: Final[IntPtr]
    """"""
    Size: Final[int]
    """"""
    cPropertiesToSet: Final[IntPtr]
    """"""
    cPropertiesToTest: Final[IntPtr]
    """"""
    @overload
    def __init__(
        self,
        Deployment: IDefinitionAppId,
        Reference: StoreApplicationReference,
        SetProperties: Array[StoreOperationMetadataProperty],
    ) -> None:
        """"""
    @overload
    def __init__(
        self,
        Deployment: IDefinitionAppId,
        Reference: StoreApplicationReference,
        SetProperties: Array[StoreOperationMetadataProperty],
        TestProperties: Array[StoreOperationMetadataProperty],
    ) -> None:
        """"""
    def Destroy(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    # noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
    class Disposition(Enum):
        """"""

        Failed: StoreOperationSetDeploymentMetadata.Disposition = ...
        """"""
        Set: StoreOperationSetDeploymentMetadata.Disposition = ...
        """"""

    # noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
    class OpFlags(Enum):
        """"""

        Nothing: StoreOperationSetDeploymentMetadata.OpFlags = ...
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class StoreOperationStageComponent(ValueType):
    """"""

    Application: Final[IDefinitionAppId]
    """"""
    Component: Final[IDefinitionIdentity]
    """"""
    Flags: Final[StoreOperationStageComponent.OpFlags]
    """"""
    ManifestPath: Final[str]
    """"""
    Size: Final[int]
    """"""
    @overload
    def __init__(self, app: IDefinitionAppId, Manifest: str) -> None:
        """"""
    @overload
    def __init__(self, app: IDefinitionAppId, comp: IDefinitionIdentity, Manifest: str) -> None:
        """"""
    def Destroy(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    # noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
    class Disposition(Enum):
        """"""

        Failed: StoreOperationStageComponent.Disposition = ...
        """"""
        Installed: StoreOperationStageComponent.Disposition = ...
        """"""
        Refreshed: StoreOperationStageComponent.Disposition = ...
        """"""
        AlreadyInstalled: StoreOperationStageComponent.Disposition = ...
        """"""

    # noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
    class OpFlags(Enum):
        """"""

        Nothing: StoreOperationStageComponent.OpFlags = ...
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class StoreOperationStageComponentFile(ValueType):
    """"""

    Application: Final[IDefinitionAppId]
    """"""
    Component: Final[IDefinitionIdentity]
    """"""
    ComponentRelativePath: Final[str]
    """"""
    Flags: Final[StoreOperationStageComponentFile.OpFlags]
    """"""
    Size: Final[int]
    """"""
    SourceFilePath: Final[str]
    """"""
    @overload
    def __init__(self, App: IDefinitionAppId, CompRelPath: str, SrcFile: str) -> None:
        """"""
    @overload
    def __init__(
        self, App: IDefinitionAppId, Component: IDefinitionIdentity, CompRelPath: str, SrcFile: str
    ) -> None:
        """"""
    def Destroy(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    # noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
    class Disposition(Enum):
        """"""

        Failed: StoreOperationStageComponentFile.Disposition = ...
        """"""
        Installed: StoreOperationStageComponentFile.Disposition = ...
        """"""
        Refreshed: StoreOperationStageComponentFile.Disposition = ...
        """"""
        AlreadyInstalled: StoreOperationStageComponentFile.Disposition = ...
        """"""

    # noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
    class OpFlags(Enum):
        """"""

        Nothing: StoreOperationStageComponentFile.OpFlags = ...
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class StoreOperationUninstallDeployment(ValueType):
    """"""

    Application: Final[IDefinitionAppId]
    """"""
    Flags: Final[StoreOperationUninstallDeployment.OpFlags]
    """"""
    Reference: Final[IntPtr]
    """"""
    Size: Final[int]
    """"""
    def __init__(self, appid: IDefinitionAppId, AppRef: StoreApplicationReference) -> None:
        """"""
    def Destroy(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    # noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
    class Disposition(Enum):
        """"""

        Failed: StoreOperationUninstallDeployment.Disposition = ...
        """"""
        DidNotExist: StoreOperationUninstallDeployment.Disposition = ...
        """"""
        Uninstalled: StoreOperationUninstallDeployment.Disposition = ...
        """"""

    # noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
    class OpFlags(Enum):
        """"""

        Nothing: StoreOperationUninstallDeployment.OpFlags = ...
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class StoreOperationUnpinDeployment(ValueType):
    """"""

    Application: Final[IDefinitionAppId]
    """"""
    Flags: Final[StoreOperationUnpinDeployment.OpFlags]
    """"""
    Reference: Final[IntPtr]
    """"""
    Size: Final[int]
    """"""
    def __init__(self, app: IDefinitionAppId, reference: StoreApplicationReference) -> None:
        """"""
    def Destroy(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    # noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
    class Disposition(Enum):
        """"""

        Failed: StoreOperationUnpinDeployment.Disposition = ...
        """"""
        Unpinned: StoreOperationUnpinDeployment.Disposition = ...
        """"""

    # noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
    class OpFlags(Enum):
        """"""

        Nothing: StoreOperationUnpinDeployment.OpFlags = ...
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class StoreSubcategoryEnumeration(Object, IEnumerator):
    """"""
    def __init__(self, pI: IEnumSTORE_CATEGORY_SUBCATEGORY) -> None:
        """"""
    @property
    def Current(self) -> STORE_CATEGORY_SUBCATEGORY:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator:
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
    def __iter__(self) -> Iterator:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class StoreTransaction(Object, IDisposable):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Operations(self) -> Array[StoreTransactionOperation]:
        """"""
    @overload
    def Add(self, o: StoreOperationInstallDeployment) -> None:
        """"""
    @overload
    def Add(self, o: StoreOperationPinDeployment) -> None:
        """"""
    @overload
    def Add(self, o: StoreOperationScavenge) -> None:
        """"""
    @overload
    def Add(self, o: StoreOperationSetCanonicalizationContext) -> None:
        """"""
    @overload
    def Add(self, o: StoreOperationSetDeploymentMetadata) -> None:
        """"""
    @overload
    def Add(self, o: StoreOperationStageComponent) -> None:
        """"""
    @overload
    def Add(self, o: StoreOperationStageComponentFile) -> None:
        """"""
    @overload
    def Add(self, o: StoreOperationUninstallDeployment) -> None:
        """"""
    @overload
    def Add(self, o: StoreOperationUnpinDeployment) -> None:
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class StoreTransactionData(ValueType):
    """"""

    DataPtr: Final[IntPtr]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class StoreTransactionOperation(ValueType):
    """"""

    Data: Final[StoreTransactionData]
    """"""
    Operation: Final[StoreTransactionOperationType]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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
