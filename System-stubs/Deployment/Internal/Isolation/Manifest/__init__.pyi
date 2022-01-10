from __future__ import annotations

from abc import ABC
from typing import Protocol, Union

from System import Boolean, Byte, Enum, Guid, IDisposable, Int32, IntPtr, Object, String, UInt16, UInt32, UInt64, Void
from System.Deployment.Internal.Isolation import IDefinitionIdentity, IReferenceIdentity, ISection, ISectionEntry

# ---------- Types ---------- #

BooleanType = Union[bool, Boolean]
ByteType = Union[int, Byte]
IntType = Union[int, Int32]
NIntType = Union[int, IntPtr]
ObjectType = Object
StringType = Union[str, String]
UIntType = Union[int, UInt32]
ULongType = Union[int, UInt64]
UShortType = Union[int, UInt16]
VoidType = Union[None, Void]

# ---------- Classes ---------- #

class AssemblyReferenceDependentAssemblyEntry(ObjectType, IDisposable):
    # ---------- Fields ---------- #
    
    @property
    def Codebase(self) -> StringType: ...
    
    @Codebase.setter
    def Codebase(self, value: StringType) -> None: ...
    
    @property
    def Description(self) -> StringType: ...
    
    @Description.setter
    def Description(self, value: StringType) -> None: ...
    
    @property
    def Flags(self) -> UIntType: ...
    
    @Flags.setter
    def Flags(self, value: UIntType) -> None: ...
    
    @property
    def Group(self) -> StringType: ...
    
    @Group.setter
    def Group(self, value: StringType) -> None: ...
    
    @property
    def HashAlgorithm(self) -> UIntType: ...
    
    @HashAlgorithm.setter
    def HashAlgorithm(self, value: UIntType) -> None: ...
    
    @property
    def HashElements(self) -> ISection: ...
    
    @HashElements.setter
    def HashElements(self, value: ISection) -> None: ...
    
    @property
    def HashValue(self) -> NIntType: ...
    
    @HashValue.setter
    def HashValue(self, value: NIntType) -> None: ...
    
    @property
    def HashValueSize(self) -> UIntType: ...
    
    @HashValueSize.setter
    def HashValueSize(self, value: UIntType) -> None: ...
    
    @property
    def ResourceFallbackCulture(self) -> StringType: ...
    
    @ResourceFallbackCulture.setter
    def ResourceFallbackCulture(self, value: StringType) -> None: ...
    
    @property
    def Size(self) -> ULongType: ...
    
    @Size.setter
    def Size(self, value: ULongType) -> None: ...
    
    @property
    def SupportUrl(self) -> StringType: ...
    
    @SupportUrl.setter
    def SupportUrl(self, value: StringType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Dispose(self, fDisposing: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AssemblyReferenceDependentAssemblyEntry(ObjectType, IDisposable):
    # ---------- Fields ---------- #
    
    @property
    def Codebase(self) -> StringType: ...
    
    @Codebase.setter
    def Codebase(self, value: StringType) -> None: ...
    
    @property
    def Description(self) -> StringType: ...
    
    @Description.setter
    def Description(self, value: StringType) -> None: ...
    
    @property
    def Flags(self) -> UIntType: ...
    
    @Flags.setter
    def Flags(self, value: UIntType) -> None: ...
    
    @property
    def Group(self) -> StringType: ...
    
    @Group.setter
    def Group(self, value: StringType) -> None: ...
    
    @property
    def HashAlgorithm(self) -> UIntType: ...
    
    @HashAlgorithm.setter
    def HashAlgorithm(self, value: UIntType) -> None: ...
    
    @property
    def HashElements(self) -> ISection: ...
    
    @HashElements.setter
    def HashElements(self, value: ISection) -> None: ...
    
    @property
    def HashValue(self) -> NIntType: ...
    
    @HashValue.setter
    def HashValue(self, value: NIntType) -> None: ...
    
    @property
    def HashValueSize(self) -> UIntType: ...
    
    @HashValueSize.setter
    def HashValueSize(self, value: UIntType) -> None: ...
    
    @property
    def ResourceFallbackCulture(self) -> StringType: ...
    
    @ResourceFallbackCulture.setter
    def ResourceFallbackCulture(self, value: StringType) -> None: ...
    
    @property
    def Size(self) -> ULongType: ...
    
    @Size.setter
    def Size(self, value: ULongType) -> None: ...
    
    @property
    def SupportUrl(self) -> StringType: ...
    
    @SupportUrl.setter
    def SupportUrl(self, value: StringType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Dispose(self, fDisposing: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AssemblyReferenceDependentAssemblyEntry(ObjectType, IDisposable):
    # ---------- Fields ---------- #
    
    @property
    def Codebase(self) -> StringType: ...
    
    @Codebase.setter
    def Codebase(self, value: StringType) -> None: ...
    
    @property
    def Description(self) -> StringType: ...
    
    @Description.setter
    def Description(self, value: StringType) -> None: ...
    
    @property
    def Flags(self) -> UIntType: ...
    
    @Flags.setter
    def Flags(self, value: UIntType) -> None: ...
    
    @property
    def Group(self) -> StringType: ...
    
    @Group.setter
    def Group(self, value: StringType) -> None: ...
    
    @property
    def HashAlgorithm(self) -> UIntType: ...
    
    @HashAlgorithm.setter
    def HashAlgorithm(self, value: UIntType) -> None: ...
    
    @property
    def HashElements(self) -> ISection: ...
    
    @HashElements.setter
    def HashElements(self, value: ISection) -> None: ...
    
    @property
    def HashValue(self) -> NIntType: ...
    
    @HashValue.setter
    def HashValue(self, value: NIntType) -> None: ...
    
    @property
    def HashValueSize(self) -> UIntType: ...
    
    @HashValueSize.setter
    def HashValueSize(self, value: UIntType) -> None: ...
    
    @property
    def ResourceFallbackCulture(self) -> StringType: ...
    
    @ResourceFallbackCulture.setter
    def ResourceFallbackCulture(self, value: StringType) -> None: ...
    
    @property
    def Size(self) -> ULongType: ...
    
    @Size.setter
    def Size(self, value: ULongType) -> None: ...
    
    @property
    def SupportUrl(self) -> StringType: ...
    
    @SupportUrl.setter
    def SupportUrl(self, value: StringType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Dispose(self, fDisposing: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AssemblyReferenceEntry(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def DependentAssembly(self) -> AssemblyReferenceDependentAssemblyEntry: ...
    
    @DependentAssembly.setter
    def DependentAssembly(self, value: AssemblyReferenceDependentAssemblyEntry) -> None: ...
    
    @property
    def Flags(self) -> UIntType: ...
    
    @Flags.setter
    def Flags(self, value: UIntType) -> None: ...
    
    @property
    def ReferenceIdentity(self) -> IReferenceIdentity: ...
    
    @ReferenceIdentity.setter
    def ReferenceIdentity(self, value: IReferenceIdentity) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AssemblyReferenceEntry(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def DependentAssembly(self) -> AssemblyReferenceDependentAssemblyEntry: ...
    
    @DependentAssembly.setter
    def DependentAssembly(self, value: AssemblyReferenceDependentAssemblyEntry) -> None: ...
    
    @property
    def Flags(self) -> UIntType: ...
    
    @Flags.setter
    def Flags(self, value: UIntType) -> None: ...
    
    @property
    def ReferenceIdentity(self) -> IReferenceIdentity: ...
    
    @ReferenceIdentity.setter
    def ReferenceIdentity(self, value: IReferenceIdentity) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AssemblyReferenceEntry(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def DependentAssembly(self) -> AssemblyReferenceDependentAssemblyEntry: ...
    
    @DependentAssembly.setter
    def DependentAssembly(self, value: AssemblyReferenceDependentAssemblyEntry) -> None: ...
    
    @property
    def Flags(self) -> UIntType: ...
    
    @Flags.setter
    def Flags(self, value: UIntType) -> None: ...
    
    @property
    def ReferenceIdentity(self) -> IReferenceIdentity: ...
    
    @ReferenceIdentity.setter
    def ReferenceIdentity(self, value: IReferenceIdentity) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AssemblyRequestEntry(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def Name(self) -> StringType: ...
    
    @Name.setter
    def Name(self, value: StringType) -> None: ...
    
    @property
    def permissionSetID(self) -> StringType: ...
    
    @permissionSetID.setter
    def permissionSetID(self, value: StringType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AssemblyRequestEntry(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def Name(self) -> StringType: ...
    
    @Name.setter
    def Name(self, value: StringType) -> None: ...
    
    @property
    def permissionSetID(self) -> StringType: ...
    
    @permissionSetID.setter
    def permissionSetID(self, value: StringType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AssemblyRequestEntry(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def Name(self) -> StringType: ...
    
    @Name.setter
    def Name(self, value: StringType) -> None: ...
    
    @property
    def permissionSetID(self) -> StringType: ...
    
    @permissionSetID.setter
    def permissionSetID(self, value: StringType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CLRSurrogateEntry(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def ClassName(self) -> StringType: ...
    
    @ClassName.setter
    def ClassName(self, value: StringType) -> None: ...
    
    @property
    def Clsid(self) -> Guid: ...
    
    @Clsid.setter
    def Clsid(self, value: Guid) -> None: ...
    
    @property
    def RuntimeVersion(self) -> StringType: ...
    
    @RuntimeVersion.setter
    def RuntimeVersion(self, value: StringType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CLRSurrogateEntry(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def ClassName(self) -> StringType: ...
    
    @ClassName.setter
    def ClassName(self, value: StringType) -> None: ...
    
    @property
    def Clsid(self) -> Guid: ...
    
    @Clsid.setter
    def Clsid(self, value: Guid) -> None: ...
    
    @property
    def RuntimeVersion(self) -> StringType: ...
    
    @RuntimeVersion.setter
    def RuntimeVersion(self, value: StringType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CLRSurrogateEntry(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def ClassName(self) -> StringType: ...
    
    @ClassName.setter
    def ClassName(self, value: StringType) -> None: ...
    
    @property
    def Clsid(self) -> Guid: ...
    
    @Clsid.setter
    def Clsid(self, value: Guid) -> None: ...
    
    @property
    def RuntimeVersion(self) -> StringType: ...
    
    @RuntimeVersion.setter
    def RuntimeVersion(self, value: StringType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class COMServerEntry(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def Clsid(self) -> Guid: ...
    
    @Clsid.setter
    def Clsid(self, value: Guid) -> None: ...
    
    @property
    def ConfiguredGuid(self) -> Guid: ...
    
    @ConfiguredGuid.setter
    def ConfiguredGuid(self, value: Guid) -> None: ...
    
    @property
    def Flags(self) -> UIntType: ...
    
    @Flags.setter
    def Flags(self, value: UIntType) -> None: ...
    
    @property
    def HostFile(self) -> StringType: ...
    
    @HostFile.setter
    def HostFile(self, value: StringType) -> None: ...
    
    @property
    def ImplementedClsid(self) -> Guid: ...
    
    @ImplementedClsid.setter
    def ImplementedClsid(self, value: Guid) -> None: ...
    
    @property
    def RuntimeVersion(self) -> StringType: ...
    
    @RuntimeVersion.setter
    def RuntimeVersion(self, value: StringType) -> None: ...
    
    @property
    def ThreadingModel(self) -> UIntType: ...
    
    @ThreadingModel.setter
    def ThreadingModel(self, value: UIntType) -> None: ...
    
    @property
    def TypeLibrary(self) -> Guid: ...
    
    @TypeLibrary.setter
    def TypeLibrary(self, value: Guid) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class COMServerEntry(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def Clsid(self) -> Guid: ...
    
    @Clsid.setter
    def Clsid(self, value: Guid) -> None: ...
    
    @property
    def ConfiguredGuid(self) -> Guid: ...
    
    @ConfiguredGuid.setter
    def ConfiguredGuid(self, value: Guid) -> None: ...
    
    @property
    def Flags(self) -> UIntType: ...
    
    @Flags.setter
    def Flags(self, value: UIntType) -> None: ...
    
    @property
    def HostFile(self) -> StringType: ...
    
    @HostFile.setter
    def HostFile(self, value: StringType) -> None: ...
    
    @property
    def ImplementedClsid(self) -> Guid: ...
    
    @ImplementedClsid.setter
    def ImplementedClsid(self, value: Guid) -> None: ...
    
    @property
    def RuntimeVersion(self) -> StringType: ...
    
    @RuntimeVersion.setter
    def RuntimeVersion(self, value: StringType) -> None: ...
    
    @property
    def ThreadingModel(self) -> UIntType: ...
    
    @ThreadingModel.setter
    def ThreadingModel(self, value: UIntType) -> None: ...
    
    @property
    def TypeLibrary(self) -> Guid: ...
    
    @TypeLibrary.setter
    def TypeLibrary(self, value: Guid) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class COMServerEntry(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def Clsid(self) -> Guid: ...
    
    @Clsid.setter
    def Clsid(self, value: Guid) -> None: ...
    
    @property
    def ConfiguredGuid(self) -> Guid: ...
    
    @ConfiguredGuid.setter
    def ConfiguredGuid(self, value: Guid) -> None: ...
    
    @property
    def Flags(self) -> UIntType: ...
    
    @Flags.setter
    def Flags(self, value: UIntType) -> None: ...
    
    @property
    def HostFile(self) -> StringType: ...
    
    @HostFile.setter
    def HostFile(self, value: StringType) -> None: ...
    
    @property
    def ImplementedClsid(self) -> Guid: ...
    
    @ImplementedClsid.setter
    def ImplementedClsid(self, value: Guid) -> None: ...
    
    @property
    def RuntimeVersion(self) -> StringType: ...
    
    @RuntimeVersion.setter
    def RuntimeVersion(self, value: StringType) -> None: ...
    
    @property
    def ThreadingModel(self) -> UIntType: ...
    
    @ThreadingModel.setter
    def ThreadingModel(self, value: UIntType) -> None: ...
    
    @property
    def TypeLibrary(self) -> Guid: ...
    
    @TypeLibrary.setter
    def TypeLibrary(self, value: Guid) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CategoryMembershipDataEntry(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def Description(self) -> StringType: ...
    
    @Description.setter
    def Description(self, value: StringType) -> None: ...
    
    @property
    def Xml(self) -> StringType: ...
    
    @Xml.setter
    def Xml(self, value: StringType) -> None: ...
    
    @property
    def index(self) -> UIntType: ...
    
    @index.setter
    def index(self, value: UIntType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CategoryMembershipDataEntry(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def Description(self) -> StringType: ...
    
    @Description.setter
    def Description(self, value: StringType) -> None: ...
    
    @property
    def Xml(self) -> StringType: ...
    
    @Xml.setter
    def Xml(self, value: StringType) -> None: ...
    
    @property
    def index(self) -> UIntType: ...
    
    @index.setter
    def index(self, value: UIntType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CategoryMembershipDataEntry(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def Description(self) -> StringType: ...
    
    @Description.setter
    def Description(self, value: StringType) -> None: ...
    
    @property
    def Xml(self) -> StringType: ...
    
    @Xml.setter
    def Xml(self, value: StringType) -> None: ...
    
    @property
    def index(self) -> UIntType: ...
    
    @index.setter
    def index(self, value: UIntType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CategoryMembershipEntry(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def Identity(self) -> IDefinitionIdentity: ...
    
    @Identity.setter
    def Identity(self, value: IDefinitionIdentity) -> None: ...
    
    @property
    def SubcategoryMembership(self) -> ISection: ...
    
    @SubcategoryMembership.setter
    def SubcategoryMembership(self, value: ISection) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CategoryMembershipEntry(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def Identity(self) -> IDefinitionIdentity: ...
    
    @Identity.setter
    def Identity(self, value: IDefinitionIdentity) -> None: ...
    
    @property
    def SubcategoryMembership(self) -> ISection: ...
    
    @SubcategoryMembership.setter
    def SubcategoryMembership(self, value: ISection) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CategoryMembershipEntry(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def Identity(self) -> IDefinitionIdentity: ...
    
    @Identity.setter
    def Identity(self, value: IDefinitionIdentity) -> None: ...
    
    @property
    def SubcategoryMembership(self) -> ISection: ...
    
    @SubcategoryMembership.setter
    def SubcategoryMembership(self, value: ISection) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CmsUtils(ABC, ObjectType):
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


class CmsUtils(ABC, ObjectType):
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


class CmsUtils(ABC, ObjectType):
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


class CompatibleFrameworksMetadataEntry(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def SupportUrl(self) -> StringType: ...
    
    @SupportUrl.setter
    def SupportUrl(self, value: StringType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CompatibleFrameworksMetadataEntry(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def SupportUrl(self) -> StringType: ...
    
    @SupportUrl.setter
    def SupportUrl(self, value: StringType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CompatibleFrameworksMetadataEntry(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def SupportUrl(self) -> StringType: ...
    
    @SupportUrl.setter
    def SupportUrl(self, value: StringType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DependentOSMetadataEntry(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def BuildNumber(self) -> UShortType: ...
    
    @BuildNumber.setter
    def BuildNumber(self, value: UShortType) -> None: ...
    
    @property
    def Description(self) -> StringType: ...
    
    @Description.setter
    def Description(self, value: StringType) -> None: ...
    
    @property
    def MajorVersion(self) -> UShortType: ...
    
    @MajorVersion.setter
    def MajorVersion(self, value: UShortType) -> None: ...
    
    @property
    def MinorVersion(self) -> UShortType: ...
    
    @MinorVersion.setter
    def MinorVersion(self, value: UShortType) -> None: ...
    
    @property
    def ServicePackMajor(self) -> ByteType: ...
    
    @ServicePackMajor.setter
    def ServicePackMajor(self, value: ByteType) -> None: ...
    
    @property
    def ServicePackMinor(self) -> ByteType: ...
    
    @ServicePackMinor.setter
    def ServicePackMinor(self, value: ByteType) -> None: ...
    
    @property
    def SupportUrl(self) -> StringType: ...
    
    @SupportUrl.setter
    def SupportUrl(self, value: StringType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DependentOSMetadataEntry(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def BuildNumber(self) -> UShortType: ...
    
    @BuildNumber.setter
    def BuildNumber(self, value: UShortType) -> None: ...
    
    @property
    def Description(self) -> StringType: ...
    
    @Description.setter
    def Description(self, value: StringType) -> None: ...
    
    @property
    def MajorVersion(self) -> UShortType: ...
    
    @MajorVersion.setter
    def MajorVersion(self, value: UShortType) -> None: ...
    
    @property
    def MinorVersion(self) -> UShortType: ...
    
    @MinorVersion.setter
    def MinorVersion(self, value: UShortType) -> None: ...
    
    @property
    def ServicePackMajor(self) -> ByteType: ...
    
    @ServicePackMajor.setter
    def ServicePackMajor(self, value: ByteType) -> None: ...
    
    @property
    def ServicePackMinor(self) -> ByteType: ...
    
    @ServicePackMinor.setter
    def ServicePackMinor(self, value: ByteType) -> None: ...
    
    @property
    def SupportUrl(self) -> StringType: ...
    
    @SupportUrl.setter
    def SupportUrl(self, value: StringType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DependentOSMetadataEntry(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def BuildNumber(self) -> UShortType: ...
    
    @BuildNumber.setter
    def BuildNumber(self, value: UShortType) -> None: ...
    
    @property
    def Description(self) -> StringType: ...
    
    @Description.setter
    def Description(self, value: StringType) -> None: ...
    
    @property
    def MajorVersion(self) -> UShortType: ...
    
    @MajorVersion.setter
    def MajorVersion(self, value: UShortType) -> None: ...
    
    @property
    def MinorVersion(self) -> UShortType: ...
    
    @MinorVersion.setter
    def MinorVersion(self, value: UShortType) -> None: ...
    
    @property
    def ServicePackMajor(self) -> ByteType: ...
    
    @ServicePackMajor.setter
    def ServicePackMajor(self, value: ByteType) -> None: ...
    
    @property
    def ServicePackMinor(self) -> ByteType: ...
    
    @ServicePackMinor.setter
    def ServicePackMinor(self, value: ByteType) -> None: ...
    
    @property
    def SupportUrl(self) -> StringType: ...
    
    @SupportUrl.setter
    def SupportUrl(self, value: StringType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DeploymentMetadataEntry(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def DeploymentFlags(self) -> UIntType: ...
    
    @DeploymentFlags.setter
    def DeploymentFlags(self, value: UIntType) -> None: ...
    
    @property
    def DeploymentProviderCodebase(self) -> StringType: ...
    
    @DeploymentProviderCodebase.setter
    def DeploymentProviderCodebase(self, value: StringType) -> None: ...
    
    @property
    def MaximumAge(self) -> UShortType: ...
    
    @MaximumAge.setter
    def MaximumAge(self, value: UShortType) -> None: ...
    
    @property
    def MaximumAge_Unit(self) -> ByteType: ...
    
    @MaximumAge_Unit.setter
    def MaximumAge_Unit(self, value: ByteType) -> None: ...
    
    @property
    def MinimumRequiredVersion(self) -> StringType: ...
    
    @MinimumRequiredVersion.setter
    def MinimumRequiredVersion(self, value: StringType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DeploymentMetadataEntry(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def DeploymentFlags(self) -> UIntType: ...
    
    @DeploymentFlags.setter
    def DeploymentFlags(self, value: UIntType) -> None: ...
    
    @property
    def DeploymentProviderCodebase(self) -> StringType: ...
    
    @DeploymentProviderCodebase.setter
    def DeploymentProviderCodebase(self, value: StringType) -> None: ...
    
    @property
    def MaximumAge(self) -> UShortType: ...
    
    @MaximumAge.setter
    def MaximumAge(self, value: UShortType) -> None: ...
    
    @property
    def MaximumAge_Unit(self) -> ByteType: ...
    
    @MaximumAge_Unit.setter
    def MaximumAge_Unit(self, value: ByteType) -> None: ...
    
    @property
    def MinimumRequiredVersion(self) -> StringType: ...
    
    @MinimumRequiredVersion.setter
    def MinimumRequiredVersion(self, value: StringType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DeploymentMetadataEntry(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def DeploymentFlags(self) -> UIntType: ...
    
    @DeploymentFlags.setter
    def DeploymentFlags(self, value: UIntType) -> None: ...
    
    @property
    def DeploymentProviderCodebase(self) -> StringType: ...
    
    @DeploymentProviderCodebase.setter
    def DeploymentProviderCodebase(self, value: StringType) -> None: ...
    
    @property
    def MaximumAge(self) -> UShortType: ...
    
    @MaximumAge.setter
    def MaximumAge(self, value: UShortType) -> None: ...
    
    @property
    def MaximumAge_Unit(self) -> ByteType: ...
    
    @MaximumAge_Unit.setter
    def MaximumAge_Unit(self, value: ByteType) -> None: ...
    
    @property
    def MinimumRequiredVersion(self) -> StringType: ...
    
    @MinimumRequiredVersion.setter
    def MinimumRequiredVersion(self, value: StringType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DescriptionMetadataEntry(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def ErrorReportUrl(self) -> StringType: ...
    
    @ErrorReportUrl.setter
    def ErrorReportUrl(self, value: StringType) -> None: ...
    
    @property
    def IconFile(self) -> StringType: ...
    
    @IconFile.setter
    def IconFile(self, value: StringType) -> None: ...
    
    @property
    def Product(self) -> StringType: ...
    
    @Product.setter
    def Product(self, value: StringType) -> None: ...
    
    @property
    def Publisher(self) -> StringType: ...
    
    @Publisher.setter
    def Publisher(self, value: StringType) -> None: ...
    
    @property
    def SuiteName(self) -> StringType: ...
    
    @SuiteName.setter
    def SuiteName(self, value: StringType) -> None: ...
    
    @property
    def SupportUrl(self) -> StringType: ...
    
    @SupportUrl.setter
    def SupportUrl(self, value: StringType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DescriptionMetadataEntry(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def ErrorReportUrl(self) -> StringType: ...
    
    @ErrorReportUrl.setter
    def ErrorReportUrl(self, value: StringType) -> None: ...
    
    @property
    def IconFile(self) -> StringType: ...
    
    @IconFile.setter
    def IconFile(self, value: StringType) -> None: ...
    
    @property
    def Product(self) -> StringType: ...
    
    @Product.setter
    def Product(self, value: StringType) -> None: ...
    
    @property
    def Publisher(self) -> StringType: ...
    
    @Publisher.setter
    def Publisher(self, value: StringType) -> None: ...
    
    @property
    def SuiteName(self) -> StringType: ...
    
    @SuiteName.setter
    def SuiteName(self, value: StringType) -> None: ...
    
    @property
    def SupportUrl(self) -> StringType: ...
    
    @SupportUrl.setter
    def SupportUrl(self, value: StringType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DescriptionMetadataEntry(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def ErrorReportUrl(self) -> StringType: ...
    
    @ErrorReportUrl.setter
    def ErrorReportUrl(self, value: StringType) -> None: ...
    
    @property
    def IconFile(self) -> StringType: ...
    
    @IconFile.setter
    def IconFile(self, value: StringType) -> None: ...
    
    @property
    def Product(self) -> StringType: ...
    
    @Product.setter
    def Product(self, value: StringType) -> None: ...
    
    @property
    def Publisher(self) -> StringType: ...
    
    @Publisher.setter
    def Publisher(self, value: StringType) -> None: ...
    
    @property
    def SuiteName(self) -> StringType: ...
    
    @SuiteName.setter
    def SuiteName(self, value: StringType) -> None: ...
    
    @property
    def SupportUrl(self) -> StringType: ...
    
    @SupportUrl.setter
    def SupportUrl(self, value: StringType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EntryPointEntry(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def CommandLine_File(self) -> StringType: ...
    
    @CommandLine_File.setter
    def CommandLine_File(self, value: StringType) -> None: ...
    
    @property
    def CommandLine_Parameters(self) -> StringType: ...
    
    @CommandLine_Parameters.setter
    def CommandLine_Parameters(self, value: StringType) -> None: ...
    
    @property
    def Flags(self) -> UIntType: ...
    
    @Flags.setter
    def Flags(self, value: UIntType) -> None: ...
    
    @property
    def Identity(self) -> IReferenceIdentity: ...
    
    @Identity.setter
    def Identity(self, value: IReferenceIdentity) -> None: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @Name.setter
    def Name(self, value: StringType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EntryPointEntry(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def CommandLine_File(self) -> StringType: ...
    
    @CommandLine_File.setter
    def CommandLine_File(self, value: StringType) -> None: ...
    
    @property
    def CommandLine_Parameters(self) -> StringType: ...
    
    @CommandLine_Parameters.setter
    def CommandLine_Parameters(self, value: StringType) -> None: ...
    
    @property
    def Flags(self) -> UIntType: ...
    
    @Flags.setter
    def Flags(self, value: UIntType) -> None: ...
    
    @property
    def Identity(self) -> IReferenceIdentity: ...
    
    @Identity.setter
    def Identity(self, value: IReferenceIdentity) -> None: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @Name.setter
    def Name(self, value: StringType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EntryPointEntry(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def CommandLine_File(self) -> StringType: ...
    
    @CommandLine_File.setter
    def CommandLine_File(self, value: StringType) -> None: ...
    
    @property
    def CommandLine_Parameters(self) -> StringType: ...
    
    @CommandLine_Parameters.setter
    def CommandLine_Parameters(self, value: StringType) -> None: ...
    
    @property
    def Flags(self) -> UIntType: ...
    
    @Flags.setter
    def Flags(self, value: UIntType) -> None: ...
    
    @property
    def Identity(self) -> IReferenceIdentity: ...
    
    @Identity.setter
    def Identity(self, value: IReferenceIdentity) -> None: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @Name.setter
    def Name(self, value: StringType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class FileAssociationEntry(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def DefaultIcon(self) -> StringType: ...
    
    @DefaultIcon.setter
    def DefaultIcon(self, value: StringType) -> None: ...
    
    @property
    def Description(self) -> StringType: ...
    
    @Description.setter
    def Description(self, value: StringType) -> None: ...
    
    @property
    def Extension(self) -> StringType: ...
    
    @Extension.setter
    def Extension(self, value: StringType) -> None: ...
    
    @property
    def Parameter(self) -> StringType: ...
    
    @Parameter.setter
    def Parameter(self, value: StringType) -> None: ...
    
    @property
    def ProgID(self) -> StringType: ...
    
    @ProgID.setter
    def ProgID(self, value: StringType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class FileAssociationEntry(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def DefaultIcon(self) -> StringType: ...
    
    @DefaultIcon.setter
    def DefaultIcon(self, value: StringType) -> None: ...
    
    @property
    def Description(self) -> StringType: ...
    
    @Description.setter
    def Description(self, value: StringType) -> None: ...
    
    @property
    def Extension(self) -> StringType: ...
    
    @Extension.setter
    def Extension(self, value: StringType) -> None: ...
    
    @property
    def Parameter(self) -> StringType: ...
    
    @Parameter.setter
    def Parameter(self, value: StringType) -> None: ...
    
    @property
    def ProgID(self) -> StringType: ...
    
    @ProgID.setter
    def ProgID(self, value: StringType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class FileAssociationEntry(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def DefaultIcon(self) -> StringType: ...
    
    @DefaultIcon.setter
    def DefaultIcon(self, value: StringType) -> None: ...
    
    @property
    def Description(self) -> StringType: ...
    
    @Description.setter
    def Description(self, value: StringType) -> None: ...
    
    @property
    def Extension(self) -> StringType: ...
    
    @Extension.setter
    def Extension(self, value: StringType) -> None: ...
    
    @property
    def Parameter(self) -> StringType: ...
    
    @Parameter.setter
    def Parameter(self, value: StringType) -> None: ...
    
    @property
    def ProgID(self) -> StringType: ...
    
    @ProgID.setter
    def ProgID(self, value: StringType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class FileEntry(ObjectType, IDisposable):
    # ---------- Fields ---------- #
    
    @property
    def Flags(self) -> UIntType: ...
    
    @Flags.setter
    def Flags(self, value: UIntType) -> None: ...
    
    @property
    def Group(self) -> StringType: ...
    
    @Group.setter
    def Group(self, value: StringType) -> None: ...
    
    @property
    def HashAlgorithm(self) -> UIntType: ...
    
    @HashAlgorithm.setter
    def HashAlgorithm(self, value: UIntType) -> None: ...
    
    @property
    def HashElements(self) -> ISection: ...
    
    @HashElements.setter
    def HashElements(self, value: ISection) -> None: ...
    
    @property
    def HashValue(self) -> NIntType: ...
    
    @HashValue.setter
    def HashValue(self, value: NIntType) -> None: ...
    
    @property
    def HashValueSize(self) -> UIntType: ...
    
    @HashValueSize.setter
    def HashValueSize(self, value: UIntType) -> None: ...
    
    @property
    def ImportPath(self) -> StringType: ...
    
    @ImportPath.setter
    def ImportPath(self, value: StringType) -> None: ...
    
    @property
    def LoadFrom(self) -> StringType: ...
    
    @LoadFrom.setter
    def LoadFrom(self, value: StringType) -> None: ...
    
    @property
    def Location(self) -> StringType: ...
    
    @Location.setter
    def Location(self, value: StringType) -> None: ...
    
    @property
    def MuiMapping(self) -> MuiResourceMapEntry: ...
    
    @MuiMapping.setter
    def MuiMapping(self, value: MuiResourceMapEntry) -> None: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @Name.setter
    def Name(self, value: StringType) -> None: ...
    
    @property
    def Size(self) -> ULongType: ...
    
    @Size.setter
    def Size(self, value: ULongType) -> None: ...
    
    @property
    def SourceName(self) -> StringType: ...
    
    @SourceName.setter
    def SourceName(self, value: StringType) -> None: ...
    
    @property
    def SourcePath(self) -> StringType: ...
    
    @SourcePath.setter
    def SourcePath(self, value: StringType) -> None: ...
    
    @property
    def WritableType(self) -> UIntType: ...
    
    @WritableType.setter
    def WritableType(self, value: UIntType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Dispose(self, fDisposing: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class FileEntry(ObjectType, IDisposable):
    # ---------- Fields ---------- #
    
    @property
    def Flags(self) -> UIntType: ...
    
    @Flags.setter
    def Flags(self, value: UIntType) -> None: ...
    
    @property
    def Group(self) -> StringType: ...
    
    @Group.setter
    def Group(self, value: StringType) -> None: ...
    
    @property
    def HashAlgorithm(self) -> UIntType: ...
    
    @HashAlgorithm.setter
    def HashAlgorithm(self, value: UIntType) -> None: ...
    
    @property
    def HashElements(self) -> ISection: ...
    
    @HashElements.setter
    def HashElements(self, value: ISection) -> None: ...
    
    @property
    def HashValue(self) -> NIntType: ...
    
    @HashValue.setter
    def HashValue(self, value: NIntType) -> None: ...
    
    @property
    def HashValueSize(self) -> UIntType: ...
    
    @HashValueSize.setter
    def HashValueSize(self, value: UIntType) -> None: ...
    
    @property
    def ImportPath(self) -> StringType: ...
    
    @ImportPath.setter
    def ImportPath(self, value: StringType) -> None: ...
    
    @property
    def LoadFrom(self) -> StringType: ...
    
    @LoadFrom.setter
    def LoadFrom(self, value: StringType) -> None: ...
    
    @property
    def Location(self) -> StringType: ...
    
    @Location.setter
    def Location(self, value: StringType) -> None: ...
    
    @property
    def MuiMapping(self) -> MuiResourceMapEntry: ...
    
    @MuiMapping.setter
    def MuiMapping(self, value: MuiResourceMapEntry) -> None: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @Name.setter
    def Name(self, value: StringType) -> None: ...
    
    @property
    def Size(self) -> ULongType: ...
    
    @Size.setter
    def Size(self, value: ULongType) -> None: ...
    
    @property
    def SourceName(self) -> StringType: ...
    
    @SourceName.setter
    def SourceName(self, value: StringType) -> None: ...
    
    @property
    def SourcePath(self) -> StringType: ...
    
    @SourcePath.setter
    def SourcePath(self, value: StringType) -> None: ...
    
    @property
    def WritableType(self) -> UIntType: ...
    
    @WritableType.setter
    def WritableType(self, value: UIntType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Dispose(self, fDisposing: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class FileEntry(ObjectType, IDisposable):
    # ---------- Fields ---------- #
    
    @property
    def Flags(self) -> UIntType: ...
    
    @Flags.setter
    def Flags(self, value: UIntType) -> None: ...
    
    @property
    def Group(self) -> StringType: ...
    
    @Group.setter
    def Group(self, value: StringType) -> None: ...
    
    @property
    def HashAlgorithm(self) -> UIntType: ...
    
    @HashAlgorithm.setter
    def HashAlgorithm(self, value: UIntType) -> None: ...
    
    @property
    def HashElements(self) -> ISection: ...
    
    @HashElements.setter
    def HashElements(self, value: ISection) -> None: ...
    
    @property
    def HashValue(self) -> NIntType: ...
    
    @HashValue.setter
    def HashValue(self, value: NIntType) -> None: ...
    
    @property
    def HashValueSize(self) -> UIntType: ...
    
    @HashValueSize.setter
    def HashValueSize(self, value: UIntType) -> None: ...
    
    @property
    def ImportPath(self) -> StringType: ...
    
    @ImportPath.setter
    def ImportPath(self, value: StringType) -> None: ...
    
    @property
    def LoadFrom(self) -> StringType: ...
    
    @LoadFrom.setter
    def LoadFrom(self, value: StringType) -> None: ...
    
    @property
    def Location(self) -> StringType: ...
    
    @Location.setter
    def Location(self, value: StringType) -> None: ...
    
    @property
    def MuiMapping(self) -> MuiResourceMapEntry: ...
    
    @MuiMapping.setter
    def MuiMapping(self, value: MuiResourceMapEntry) -> None: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @Name.setter
    def Name(self, value: StringType) -> None: ...
    
    @property
    def Size(self) -> ULongType: ...
    
    @Size.setter
    def Size(self, value: ULongType) -> None: ...
    
    @property
    def SourceName(self) -> StringType: ...
    
    @SourceName.setter
    def SourceName(self, value: StringType) -> None: ...
    
    @property
    def SourcePath(self) -> StringType: ...
    
    @SourcePath.setter
    def SourcePath(self, value: StringType) -> None: ...
    
    @property
    def WritableType(self) -> UIntType: ...
    
    @WritableType.setter
    def WritableType(self, value: UIntType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Dispose(self, fDisposing: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class HashElementEntry(ObjectType, IDisposable):
    # ---------- Fields ---------- #
    
    @property
    def DigestMethod(self) -> ByteType: ...
    
    @DigestMethod.setter
    def DigestMethod(self, value: ByteType) -> None: ...
    
    @property
    def DigestValue(self) -> NIntType: ...
    
    @DigestValue.setter
    def DigestValue(self, value: NIntType) -> None: ...
    
    @property
    def DigestValueSize(self) -> UIntType: ...
    
    @DigestValueSize.setter
    def DigestValueSize(self, value: UIntType) -> None: ...
    
    @property
    def Transform(self) -> ByteType: ...
    
    @Transform.setter
    def Transform(self, value: ByteType) -> None: ...
    
    @property
    def TransformMetadata(self) -> NIntType: ...
    
    @TransformMetadata.setter
    def TransformMetadata(self, value: NIntType) -> None: ...
    
    @property
    def TransformMetadataSize(self) -> UIntType: ...
    
    @TransformMetadataSize.setter
    def TransformMetadataSize(self, value: UIntType) -> None: ...
    
    @property
    def Xml(self) -> StringType: ...
    
    @Xml.setter
    def Xml(self, value: StringType) -> None: ...
    
    @property
    def index(self) -> UIntType: ...
    
    @index.setter
    def index(self, value: UIntType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Dispose(self, fDisposing: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class HashElementEntry(ObjectType, IDisposable):
    # ---------- Fields ---------- #
    
    @property
    def DigestMethod(self) -> ByteType: ...
    
    @DigestMethod.setter
    def DigestMethod(self, value: ByteType) -> None: ...
    
    @property
    def DigestValue(self) -> NIntType: ...
    
    @DigestValue.setter
    def DigestValue(self, value: NIntType) -> None: ...
    
    @property
    def DigestValueSize(self) -> UIntType: ...
    
    @DigestValueSize.setter
    def DigestValueSize(self, value: UIntType) -> None: ...
    
    @property
    def Transform(self) -> ByteType: ...
    
    @Transform.setter
    def Transform(self, value: ByteType) -> None: ...
    
    @property
    def TransformMetadata(self) -> NIntType: ...
    
    @TransformMetadata.setter
    def TransformMetadata(self, value: NIntType) -> None: ...
    
    @property
    def TransformMetadataSize(self) -> UIntType: ...
    
    @TransformMetadataSize.setter
    def TransformMetadataSize(self, value: UIntType) -> None: ...
    
    @property
    def Xml(self) -> StringType: ...
    
    @Xml.setter
    def Xml(self, value: StringType) -> None: ...
    
    @property
    def index(self) -> UIntType: ...
    
    @index.setter
    def index(self, value: UIntType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Dispose(self, fDisposing: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class HashElementEntry(ObjectType, IDisposable):
    # ---------- Fields ---------- #
    
    @property
    def DigestMethod(self) -> ByteType: ...
    
    @DigestMethod.setter
    def DigestMethod(self, value: ByteType) -> None: ...
    
    @property
    def DigestValue(self) -> NIntType: ...
    
    @DigestValue.setter
    def DigestValue(self, value: NIntType) -> None: ...
    
    @property
    def DigestValueSize(self) -> UIntType: ...
    
    @DigestValueSize.setter
    def DigestValueSize(self, value: UIntType) -> None: ...
    
    @property
    def Transform(self) -> ByteType: ...
    
    @Transform.setter
    def Transform(self, value: ByteType) -> None: ...
    
    @property
    def TransformMetadata(self) -> NIntType: ...
    
    @TransformMetadata.setter
    def TransformMetadata(self, value: NIntType) -> None: ...
    
    @property
    def TransformMetadataSize(self) -> UIntType: ...
    
    @TransformMetadataSize.setter
    def TransformMetadataSize(self, value: UIntType) -> None: ...
    
    @property
    def Xml(self) -> StringType: ...
    
    @Xml.setter
    def Xml(self, value: StringType) -> None: ...
    
    @property
    def index(self) -> UIntType: ...
    
    @index.setter
    def index(self, value: UIntType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Dispose(self, fDisposing: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MetadataSectionEntry(ObjectType, IDisposable):
    # ---------- Fields ---------- #
    
    @property
    def CdfIdentity(self) -> IDefinitionIdentity: ...
    
    @CdfIdentity.setter
    def CdfIdentity(self, value: IDefinitionIdentity) -> None: ...
    
    @property
    def CompatibleFrameworksData(self) -> CompatibleFrameworksMetadataEntry: ...
    
    @CompatibleFrameworksData.setter
    def CompatibleFrameworksData(self, value: CompatibleFrameworksMetadataEntry) -> None: ...
    
    @property
    def ContentType(self) -> StringType: ...
    
    @ContentType.setter
    def ContentType(self, value: StringType) -> None: ...
    
    @property
    def DependentOSData(self) -> DependentOSMetadataEntry: ...
    
    @DependentOSData.setter
    def DependentOSData(self, value: DependentOSMetadataEntry) -> None: ...
    
    @property
    def DeploymentData(self) -> DeploymentMetadataEntry: ...
    
    @DeploymentData.setter
    def DeploymentData(self, value: DeploymentMetadataEntry) -> None: ...
    
    @property
    def DescriptionData(self) -> DescriptionMetadataEntry: ...
    
    @DescriptionData.setter
    def DescriptionData(self, value: DescriptionMetadataEntry) -> None: ...
    
    @property
    def HashAlgorithm(self) -> UIntType: ...
    
    @HashAlgorithm.setter
    def HashAlgorithm(self, value: UIntType) -> None: ...
    
    @property
    def KeyInfoElement(self) -> StringType: ...
    
    @KeyInfoElement.setter
    def KeyInfoElement(self, value: StringType) -> None: ...
    
    @property
    def LocalPath(self) -> StringType: ...
    
    @LocalPath.setter
    def LocalPath(self, value: StringType) -> None: ...
    
    @property
    def ManifestFlags(self) -> UIntType: ...
    
    @ManifestFlags.setter
    def ManifestFlags(self, value: UIntType) -> None: ...
    
    @property
    def ManifestHash(self) -> NIntType: ...
    
    @ManifestHash.setter
    def ManifestHash(self, value: NIntType) -> None: ...
    
    @property
    def ManifestHashSize(self) -> UIntType: ...
    
    @ManifestHashSize.setter
    def ManifestHashSize(self, value: UIntType) -> None: ...
    
    @property
    def MvidValue(self) -> NIntType: ...
    
    @MvidValue.setter
    def MvidValue(self, value: NIntType) -> None: ...
    
    @property
    def MvidValueSize(self) -> UIntType: ...
    
    @MvidValueSize.setter
    def MvidValueSize(self, value: UIntType) -> None: ...
    
    @property
    def RequestedExecutionLevel(self) -> StringType: ...
    
    @RequestedExecutionLevel.setter
    def RequestedExecutionLevel(self, value: StringType) -> None: ...
    
    @property
    def RequestedExecutionLevelUIAccess(self) -> BooleanType: ...
    
    @RequestedExecutionLevelUIAccess.setter
    def RequestedExecutionLevelUIAccess(self, value: BooleanType) -> None: ...
    
    @property
    def ResourceTypeManifestResourcesDependency(self) -> IReferenceIdentity: ...
    
    @ResourceTypeManifestResourcesDependency.setter
    def ResourceTypeManifestResourcesDependency(self, value: IReferenceIdentity) -> None: ...
    
    @property
    def ResourceTypeResourcesDependency(self) -> IReferenceIdentity: ...
    
    @ResourceTypeResourcesDependency.setter
    def ResourceTypeResourcesDependency(self, value: IReferenceIdentity) -> None: ...
    
    @property
    def RuntimeImageVersion(self) -> StringType: ...
    
    @RuntimeImageVersion.setter
    def RuntimeImageVersion(self, value: StringType) -> None: ...
    
    @property
    def SchemaVersion(self) -> UIntType: ...
    
    @SchemaVersion.setter
    def SchemaVersion(self, value: UIntType) -> None: ...
    
    @property
    def UsagePatterns(self) -> UIntType: ...
    
    @UsagePatterns.setter
    def UsagePatterns(self, value: UIntType) -> None: ...
    
    @property
    def defaultPermissionSetID(self) -> StringType: ...
    
    @defaultPermissionSetID.setter
    def defaultPermissionSetID(self, value: StringType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Dispose(self, fDisposing: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MetadataSectionEntry(ObjectType, IDisposable):
    # ---------- Fields ---------- #
    
    @property
    def CdfIdentity(self) -> IDefinitionIdentity: ...
    
    @CdfIdentity.setter
    def CdfIdentity(self, value: IDefinitionIdentity) -> None: ...
    
    @property
    def CompatibleFrameworksData(self) -> CompatibleFrameworksMetadataEntry: ...
    
    @CompatibleFrameworksData.setter
    def CompatibleFrameworksData(self, value: CompatibleFrameworksMetadataEntry) -> None: ...
    
    @property
    def ContentType(self) -> StringType: ...
    
    @ContentType.setter
    def ContentType(self, value: StringType) -> None: ...
    
    @property
    def DependentOSData(self) -> DependentOSMetadataEntry: ...
    
    @DependentOSData.setter
    def DependentOSData(self, value: DependentOSMetadataEntry) -> None: ...
    
    @property
    def DeploymentData(self) -> DeploymentMetadataEntry: ...
    
    @DeploymentData.setter
    def DeploymentData(self, value: DeploymentMetadataEntry) -> None: ...
    
    @property
    def DescriptionData(self) -> DescriptionMetadataEntry: ...
    
    @DescriptionData.setter
    def DescriptionData(self, value: DescriptionMetadataEntry) -> None: ...
    
    @property
    def HashAlgorithm(self) -> UIntType: ...
    
    @HashAlgorithm.setter
    def HashAlgorithm(self, value: UIntType) -> None: ...
    
    @property
    def KeyInfoElement(self) -> StringType: ...
    
    @KeyInfoElement.setter
    def KeyInfoElement(self, value: StringType) -> None: ...
    
    @property
    def LocalPath(self) -> StringType: ...
    
    @LocalPath.setter
    def LocalPath(self, value: StringType) -> None: ...
    
    @property
    def ManifestFlags(self) -> UIntType: ...
    
    @ManifestFlags.setter
    def ManifestFlags(self, value: UIntType) -> None: ...
    
    @property
    def ManifestHash(self) -> NIntType: ...
    
    @ManifestHash.setter
    def ManifestHash(self, value: NIntType) -> None: ...
    
    @property
    def ManifestHashSize(self) -> UIntType: ...
    
    @ManifestHashSize.setter
    def ManifestHashSize(self, value: UIntType) -> None: ...
    
    @property
    def MvidValue(self) -> NIntType: ...
    
    @MvidValue.setter
    def MvidValue(self, value: NIntType) -> None: ...
    
    @property
    def MvidValueSize(self) -> UIntType: ...
    
    @MvidValueSize.setter
    def MvidValueSize(self, value: UIntType) -> None: ...
    
    @property
    def RequestedExecutionLevel(self) -> StringType: ...
    
    @RequestedExecutionLevel.setter
    def RequestedExecutionLevel(self, value: StringType) -> None: ...
    
    @property
    def RequestedExecutionLevelUIAccess(self) -> BooleanType: ...
    
    @RequestedExecutionLevelUIAccess.setter
    def RequestedExecutionLevelUIAccess(self, value: BooleanType) -> None: ...
    
    @property
    def ResourceTypeManifestResourcesDependency(self) -> IReferenceIdentity: ...
    
    @ResourceTypeManifestResourcesDependency.setter
    def ResourceTypeManifestResourcesDependency(self, value: IReferenceIdentity) -> None: ...
    
    @property
    def ResourceTypeResourcesDependency(self) -> IReferenceIdentity: ...
    
    @ResourceTypeResourcesDependency.setter
    def ResourceTypeResourcesDependency(self, value: IReferenceIdentity) -> None: ...
    
    @property
    def RuntimeImageVersion(self) -> StringType: ...
    
    @RuntimeImageVersion.setter
    def RuntimeImageVersion(self, value: StringType) -> None: ...
    
    @property
    def SchemaVersion(self) -> UIntType: ...
    
    @SchemaVersion.setter
    def SchemaVersion(self, value: UIntType) -> None: ...
    
    @property
    def UsagePatterns(self) -> UIntType: ...
    
    @UsagePatterns.setter
    def UsagePatterns(self, value: UIntType) -> None: ...
    
    @property
    def defaultPermissionSetID(self) -> StringType: ...
    
    @defaultPermissionSetID.setter
    def defaultPermissionSetID(self, value: StringType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Dispose(self, fDisposing: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MetadataSectionEntry(ObjectType, IDisposable):
    # ---------- Fields ---------- #
    
    @property
    def CdfIdentity(self) -> IDefinitionIdentity: ...
    
    @CdfIdentity.setter
    def CdfIdentity(self, value: IDefinitionIdentity) -> None: ...
    
    @property
    def CompatibleFrameworksData(self) -> CompatibleFrameworksMetadataEntry: ...
    
    @CompatibleFrameworksData.setter
    def CompatibleFrameworksData(self, value: CompatibleFrameworksMetadataEntry) -> None: ...
    
    @property
    def ContentType(self) -> StringType: ...
    
    @ContentType.setter
    def ContentType(self, value: StringType) -> None: ...
    
    @property
    def DependentOSData(self) -> DependentOSMetadataEntry: ...
    
    @DependentOSData.setter
    def DependentOSData(self, value: DependentOSMetadataEntry) -> None: ...
    
    @property
    def DeploymentData(self) -> DeploymentMetadataEntry: ...
    
    @DeploymentData.setter
    def DeploymentData(self, value: DeploymentMetadataEntry) -> None: ...
    
    @property
    def DescriptionData(self) -> DescriptionMetadataEntry: ...
    
    @DescriptionData.setter
    def DescriptionData(self, value: DescriptionMetadataEntry) -> None: ...
    
    @property
    def HashAlgorithm(self) -> UIntType: ...
    
    @HashAlgorithm.setter
    def HashAlgorithm(self, value: UIntType) -> None: ...
    
    @property
    def KeyInfoElement(self) -> StringType: ...
    
    @KeyInfoElement.setter
    def KeyInfoElement(self, value: StringType) -> None: ...
    
    @property
    def LocalPath(self) -> StringType: ...
    
    @LocalPath.setter
    def LocalPath(self, value: StringType) -> None: ...
    
    @property
    def ManifestFlags(self) -> UIntType: ...
    
    @ManifestFlags.setter
    def ManifestFlags(self, value: UIntType) -> None: ...
    
    @property
    def ManifestHash(self) -> NIntType: ...
    
    @ManifestHash.setter
    def ManifestHash(self, value: NIntType) -> None: ...
    
    @property
    def ManifestHashSize(self) -> UIntType: ...
    
    @ManifestHashSize.setter
    def ManifestHashSize(self, value: UIntType) -> None: ...
    
    @property
    def MvidValue(self) -> NIntType: ...
    
    @MvidValue.setter
    def MvidValue(self, value: NIntType) -> None: ...
    
    @property
    def MvidValueSize(self) -> UIntType: ...
    
    @MvidValueSize.setter
    def MvidValueSize(self, value: UIntType) -> None: ...
    
    @property
    def RequestedExecutionLevel(self) -> StringType: ...
    
    @RequestedExecutionLevel.setter
    def RequestedExecutionLevel(self, value: StringType) -> None: ...
    
    @property
    def RequestedExecutionLevelUIAccess(self) -> BooleanType: ...
    
    @RequestedExecutionLevelUIAccess.setter
    def RequestedExecutionLevelUIAccess(self, value: BooleanType) -> None: ...
    
    @property
    def ResourceTypeManifestResourcesDependency(self) -> IReferenceIdentity: ...
    
    @ResourceTypeManifestResourcesDependency.setter
    def ResourceTypeManifestResourcesDependency(self, value: IReferenceIdentity) -> None: ...
    
    @property
    def ResourceTypeResourcesDependency(self) -> IReferenceIdentity: ...
    
    @ResourceTypeResourcesDependency.setter
    def ResourceTypeResourcesDependency(self, value: IReferenceIdentity) -> None: ...
    
    @property
    def RuntimeImageVersion(self) -> StringType: ...
    
    @RuntimeImageVersion.setter
    def RuntimeImageVersion(self, value: StringType) -> None: ...
    
    @property
    def SchemaVersion(self) -> UIntType: ...
    
    @SchemaVersion.setter
    def SchemaVersion(self, value: UIntType) -> None: ...
    
    @property
    def UsagePatterns(self) -> UIntType: ...
    
    @UsagePatterns.setter
    def UsagePatterns(self, value: UIntType) -> None: ...
    
    @property
    def defaultPermissionSetID(self) -> StringType: ...
    
    @defaultPermissionSetID.setter
    def defaultPermissionSetID(self, value: StringType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Dispose(self, fDisposing: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MuiResourceIdLookupMapEntry(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def Count(self) -> UIntType: ...
    
    @Count.setter
    def Count(self, value: UIntType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MuiResourceIdLookupMapEntry(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def Count(self) -> UIntType: ...
    
    @Count.setter
    def Count(self, value: UIntType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MuiResourceIdLookupMapEntry(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def Count(self) -> UIntType: ...
    
    @Count.setter
    def Count(self, value: UIntType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MuiResourceMapEntry(ObjectType, IDisposable):
    # ---------- Fields ---------- #
    
    @property
    def ResourceTypeIdInt(self) -> NIntType: ...
    
    @ResourceTypeIdInt.setter
    def ResourceTypeIdInt(self, value: NIntType) -> None: ...
    
    @property
    def ResourceTypeIdIntSize(self) -> UIntType: ...
    
    @ResourceTypeIdIntSize.setter
    def ResourceTypeIdIntSize(self, value: UIntType) -> None: ...
    
    @property
    def ResourceTypeIdString(self) -> NIntType: ...
    
    @ResourceTypeIdString.setter
    def ResourceTypeIdString(self, value: NIntType) -> None: ...
    
    @property
    def ResourceTypeIdStringSize(self) -> UIntType: ...
    
    @ResourceTypeIdStringSize.setter
    def ResourceTypeIdStringSize(self, value: UIntType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Dispose(self, fDisposing: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MuiResourceMapEntry(ObjectType, IDisposable):
    # ---------- Fields ---------- #
    
    @property
    def ResourceTypeIdInt(self) -> NIntType: ...
    
    @ResourceTypeIdInt.setter
    def ResourceTypeIdInt(self, value: NIntType) -> None: ...
    
    @property
    def ResourceTypeIdIntSize(self) -> UIntType: ...
    
    @ResourceTypeIdIntSize.setter
    def ResourceTypeIdIntSize(self, value: UIntType) -> None: ...
    
    @property
    def ResourceTypeIdString(self) -> NIntType: ...
    
    @ResourceTypeIdString.setter
    def ResourceTypeIdString(self, value: NIntType) -> None: ...
    
    @property
    def ResourceTypeIdStringSize(self) -> UIntType: ...
    
    @ResourceTypeIdStringSize.setter
    def ResourceTypeIdStringSize(self, value: UIntType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Dispose(self, fDisposing: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MuiResourceMapEntry(ObjectType, IDisposable):
    # ---------- Fields ---------- #
    
    @property
    def ResourceTypeIdInt(self) -> NIntType: ...
    
    @ResourceTypeIdInt.setter
    def ResourceTypeIdInt(self, value: NIntType) -> None: ...
    
    @property
    def ResourceTypeIdIntSize(self) -> UIntType: ...
    
    @ResourceTypeIdIntSize.setter
    def ResourceTypeIdIntSize(self, value: UIntType) -> None: ...
    
    @property
    def ResourceTypeIdString(self) -> NIntType: ...
    
    @ResourceTypeIdString.setter
    def ResourceTypeIdString(self, value: NIntType) -> None: ...
    
    @property
    def ResourceTypeIdStringSize(self) -> UIntType: ...
    
    @ResourceTypeIdStringSize.setter
    def ResourceTypeIdStringSize(self, value: UIntType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Dispose(self, fDisposing: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MuiResourceTypeIdIntEntry(ObjectType, IDisposable):
    # ---------- Fields ---------- #
    
    @property
    def IntegerIds(self) -> NIntType: ...
    
    @IntegerIds.setter
    def IntegerIds(self, value: NIntType) -> None: ...
    
    @property
    def IntegerIdsSize(self) -> UIntType: ...
    
    @IntegerIdsSize.setter
    def IntegerIdsSize(self, value: UIntType) -> None: ...
    
    @property
    def StringIds(self) -> NIntType: ...
    
    @StringIds.setter
    def StringIds(self, value: NIntType) -> None: ...
    
    @property
    def StringIdsSize(self) -> UIntType: ...
    
    @StringIdsSize.setter
    def StringIdsSize(self, value: UIntType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Dispose(self, fDisposing: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MuiResourceTypeIdIntEntry(ObjectType, IDisposable):
    # ---------- Fields ---------- #
    
    @property
    def IntegerIds(self) -> NIntType: ...
    
    @IntegerIds.setter
    def IntegerIds(self, value: NIntType) -> None: ...
    
    @property
    def IntegerIdsSize(self) -> UIntType: ...
    
    @IntegerIdsSize.setter
    def IntegerIdsSize(self, value: UIntType) -> None: ...
    
    @property
    def StringIds(self) -> NIntType: ...
    
    @StringIds.setter
    def StringIds(self, value: NIntType) -> None: ...
    
    @property
    def StringIdsSize(self) -> UIntType: ...
    
    @StringIdsSize.setter
    def StringIdsSize(self, value: UIntType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Dispose(self, fDisposing: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MuiResourceTypeIdIntEntry(ObjectType, IDisposable):
    # ---------- Fields ---------- #
    
    @property
    def IntegerIds(self) -> NIntType: ...
    
    @IntegerIds.setter
    def IntegerIds(self, value: NIntType) -> None: ...
    
    @property
    def IntegerIdsSize(self) -> UIntType: ...
    
    @IntegerIdsSize.setter
    def IntegerIdsSize(self, value: UIntType) -> None: ...
    
    @property
    def StringIds(self) -> NIntType: ...
    
    @StringIds.setter
    def StringIds(self, value: NIntType) -> None: ...
    
    @property
    def StringIdsSize(self) -> UIntType: ...
    
    @StringIdsSize.setter
    def StringIdsSize(self, value: UIntType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Dispose(self, fDisposing: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MuiResourceTypeIdStringEntry(ObjectType, IDisposable):
    # ---------- Fields ---------- #
    
    @property
    def IntegerIds(self) -> NIntType: ...
    
    @IntegerIds.setter
    def IntegerIds(self, value: NIntType) -> None: ...
    
    @property
    def IntegerIdsSize(self) -> UIntType: ...
    
    @IntegerIdsSize.setter
    def IntegerIdsSize(self, value: UIntType) -> None: ...
    
    @property
    def StringIds(self) -> NIntType: ...
    
    @StringIds.setter
    def StringIds(self, value: NIntType) -> None: ...
    
    @property
    def StringIdsSize(self) -> UIntType: ...
    
    @StringIdsSize.setter
    def StringIdsSize(self, value: UIntType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Dispose(self, fDisposing: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MuiResourceTypeIdStringEntry(ObjectType, IDisposable):
    # ---------- Fields ---------- #
    
    @property
    def IntegerIds(self) -> NIntType: ...
    
    @IntegerIds.setter
    def IntegerIds(self, value: NIntType) -> None: ...
    
    @property
    def IntegerIdsSize(self) -> UIntType: ...
    
    @IntegerIdsSize.setter
    def IntegerIdsSize(self, value: UIntType) -> None: ...
    
    @property
    def StringIds(self) -> NIntType: ...
    
    @StringIds.setter
    def StringIds(self, value: NIntType) -> None: ...
    
    @property
    def StringIdsSize(self) -> UIntType: ...
    
    @StringIdsSize.setter
    def StringIdsSize(self, value: UIntType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Dispose(self, fDisposing: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MuiResourceTypeIdStringEntry(ObjectType, IDisposable):
    # ---------- Fields ---------- #
    
    @property
    def IntegerIds(self) -> NIntType: ...
    
    @IntegerIds.setter
    def IntegerIds(self, value: NIntType) -> None: ...
    
    @property
    def IntegerIdsSize(self) -> UIntType: ...
    
    @IntegerIdsSize.setter
    def IntegerIdsSize(self, value: UIntType) -> None: ...
    
    @property
    def StringIds(self) -> NIntType: ...
    
    @StringIds.setter
    def StringIds(self, value: NIntType) -> None: ...
    
    @property
    def StringIdsSize(self) -> UIntType: ...
    
    @StringIdsSize.setter
    def StringIdsSize(self, value: UIntType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Dispose(self, fDisposing: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PermissionSetEntry(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def Id(self) -> StringType: ...
    
    @Id.setter
    def Id(self, value: StringType) -> None: ...
    
    @property
    def XmlSegment(self) -> StringType: ...
    
    @XmlSegment.setter
    def XmlSegment(self, value: StringType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PermissionSetEntry(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def Id(self) -> StringType: ...
    
    @Id.setter
    def Id(self, value: StringType) -> None: ...
    
    @property
    def XmlSegment(self) -> StringType: ...
    
    @XmlSegment.setter
    def XmlSegment(self, value: StringType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PermissionSetEntry(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def Id(self) -> StringType: ...
    
    @Id.setter
    def Id(self, value: StringType) -> None: ...
    
    @property
    def XmlSegment(self) -> StringType: ...
    
    @XmlSegment.setter
    def XmlSegment(self, value: StringType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ProgIdRedirectionEntry(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def ProgId(self) -> StringType: ...
    
    @ProgId.setter
    def ProgId(self, value: StringType) -> None: ...
    
    @property
    def RedirectedGuid(self) -> Guid: ...
    
    @RedirectedGuid.setter
    def RedirectedGuid(self, value: Guid) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ProgIdRedirectionEntry(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def ProgId(self) -> StringType: ...
    
    @ProgId.setter
    def ProgId(self, value: StringType) -> None: ...
    
    @property
    def RedirectedGuid(self) -> Guid: ...
    
    @RedirectedGuid.setter
    def RedirectedGuid(self, value: Guid) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ProgIdRedirectionEntry(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def ProgId(self) -> StringType: ...
    
    @ProgId.setter
    def ProgId(self, value: StringType) -> None: ...
    
    @property
    def RedirectedGuid(self) -> Guid: ...
    
    @RedirectedGuid.setter
    def RedirectedGuid(self, value: Guid) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ResourceTableMappingEntry(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def FinalStringMapped(self) -> StringType: ...
    
    @FinalStringMapped.setter
    def FinalStringMapped(self, value: StringType) -> None: ...
    
    @property
    def id(self) -> StringType: ...
    
    @id.setter
    def id(self, value: StringType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ResourceTableMappingEntry(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def FinalStringMapped(self) -> StringType: ...
    
    @FinalStringMapped.setter
    def FinalStringMapped(self, value: StringType) -> None: ...
    
    @property
    def id(self) -> StringType: ...
    
    @id.setter
    def id(self, value: StringType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ResourceTableMappingEntry(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def FinalStringMapped(self) -> StringType: ...
    
    @FinalStringMapped.setter
    def FinalStringMapped(self, value: StringType) -> None: ...
    
    @property
    def id(self) -> StringType: ...
    
    @id.setter
    def id(self, value: StringType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SubcategoryMembershipEntry(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def CategoryMembershipData(self) -> ISection: ...
    
    @CategoryMembershipData.setter
    def CategoryMembershipData(self, value: ISection) -> None: ...
    
    @property
    def Subcategory(self) -> StringType: ...
    
    @Subcategory.setter
    def Subcategory(self, value: StringType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SubcategoryMembershipEntry(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def CategoryMembershipData(self) -> ISection: ...
    
    @CategoryMembershipData.setter
    def CategoryMembershipData(self, value: ISection) -> None: ...
    
    @property
    def Subcategory(self) -> StringType: ...
    
    @Subcategory.setter
    def Subcategory(self, value: StringType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SubcategoryMembershipEntry(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def CategoryMembershipData(self) -> ISection: ...
    
    @CategoryMembershipData.setter
    def CategoryMembershipData(self, value: ISection) -> None: ...
    
    @property
    def Subcategory(self) -> StringType: ...
    
    @Subcategory.setter
    def Subcategory(self, value: StringType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class WindowClassEntry(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def ClassName(self) -> StringType: ...
    
    @ClassName.setter
    def ClassName(self, value: StringType) -> None: ...
    
    @property
    def HostDll(self) -> StringType: ...
    
    @HostDll.setter
    def HostDll(self, value: StringType) -> None: ...
    
    @property
    def fVersioned(self) -> BooleanType: ...
    
    @fVersioned.setter
    def fVersioned(self, value: BooleanType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class WindowClassEntry(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def ClassName(self) -> StringType: ...
    
    @ClassName.setter
    def ClassName(self, value: StringType) -> None: ...
    
    @property
    def HostDll(self) -> StringType: ...
    
    @HostDll.setter
    def HostDll(self, value: StringType) -> None: ...
    
    @property
    def fVersioned(self) -> BooleanType: ...
    
    @fVersioned.setter
    def fVersioned(self, value: BooleanType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class WindowClassEntry(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def ClassName(self) -> StringType: ...
    
    @ClassName.setter
    def ClassName(self, value: StringType) -> None: ...
    
    @property
    def HostDll(self) -> StringType: ...
    
    @HostDll.setter
    def HostDll(self, value: StringType) -> None: ...
    
    @property
    def fVersioned(self) -> BooleanType: ...
    
    @fVersioned.setter
    def fVersioned(self, value: BooleanType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# No Structs

# ---------- Interfaces ---------- #

class IAssemblyReferenceDependentAssemblyEntry(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def AllData(self) -> AssemblyReferenceDependentAssemblyEntry: ...
    
    @property
    def Codebase(self) -> StringType: ...
    
    @property
    def Description(self) -> StringType: ...
    
    @property
    def Flags(self) -> UIntType: ...
    
    @property
    def Group(self) -> StringType: ...
    
    @property
    def HashAlgorithm(self) -> UIntType: ...
    
    @property
    def HashElements(self) -> ISection: ...
    
    @property
    def HashValue(self) -> ObjectType: ...
    
    @property
    def ResourceFallbackCulture(self) -> StringType: ...
    
    @property
    def Size(self) -> ULongType: ...
    
    @property
    def SupportUrl(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_AllData(self) -> AssemblyReferenceDependentAssemblyEntry: ...
    
    def get_Codebase(self) -> StringType: ...
    
    def get_Description(self) -> StringType: ...
    
    def get_Flags(self) -> UIntType: ...
    
    def get_Group(self) -> StringType: ...
    
    def get_HashAlgorithm(self) -> UIntType: ...
    
    def get_HashElements(self) -> ISection: ...
    
    def get_HashValue(self) -> ObjectType: ...
    
    def get_ResourceFallbackCulture(self) -> StringType: ...
    
    def get_Size(self) -> ULongType: ...
    
    def get_SupportUrl(self) -> StringType: ...
    
    # No Events


class IAssemblyReferenceDependentAssemblyEntry(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def AllData(self) -> AssemblyReferenceDependentAssemblyEntry: ...
    
    @property
    def Codebase(self) -> StringType: ...
    
    @property
    def Description(self) -> StringType: ...
    
    @property
    def Flags(self) -> UIntType: ...
    
    @property
    def Group(self) -> StringType: ...
    
    @property
    def HashAlgorithm(self) -> UIntType: ...
    
    @property
    def HashElements(self) -> ISection: ...
    
    @property
    def HashValue(self) -> ObjectType: ...
    
    @property
    def ResourceFallbackCulture(self) -> StringType: ...
    
    @property
    def Size(self) -> ULongType: ...
    
    @property
    def SupportUrl(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_AllData(self) -> AssemblyReferenceDependentAssemblyEntry: ...
    
    def get_Codebase(self) -> StringType: ...
    
    def get_Description(self) -> StringType: ...
    
    def get_Flags(self) -> UIntType: ...
    
    def get_Group(self) -> StringType: ...
    
    def get_HashAlgorithm(self) -> UIntType: ...
    
    def get_HashElements(self) -> ISection: ...
    
    def get_HashValue(self) -> ObjectType: ...
    
    def get_ResourceFallbackCulture(self) -> StringType: ...
    
    def get_Size(self) -> ULongType: ...
    
    def get_SupportUrl(self) -> StringType: ...
    
    # No Events


class IAssemblyReferenceDependentAssemblyEntry(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def AllData(self) -> AssemblyReferenceDependentAssemblyEntry: ...
    
    @property
    def Codebase(self) -> StringType: ...
    
    @property
    def Description(self) -> StringType: ...
    
    @property
    def Flags(self) -> UIntType: ...
    
    @property
    def Group(self) -> StringType: ...
    
    @property
    def HashAlgorithm(self) -> UIntType: ...
    
    @property
    def HashElements(self) -> ISection: ...
    
    @property
    def HashValue(self) -> ObjectType: ...
    
    @property
    def ResourceFallbackCulture(self) -> StringType: ...
    
    @property
    def Size(self) -> ULongType: ...
    
    @property
    def SupportUrl(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_AllData(self) -> AssemblyReferenceDependentAssemblyEntry: ...
    
    def get_Codebase(self) -> StringType: ...
    
    def get_Description(self) -> StringType: ...
    
    def get_Flags(self) -> UIntType: ...
    
    def get_Group(self) -> StringType: ...
    
    def get_HashAlgorithm(self) -> UIntType: ...
    
    def get_HashElements(self) -> ISection: ...
    
    def get_HashValue(self) -> ObjectType: ...
    
    def get_ResourceFallbackCulture(self) -> StringType: ...
    
    def get_Size(self) -> ULongType: ...
    
    def get_SupportUrl(self) -> StringType: ...
    
    # No Events


class IAssemblyReferenceEntry(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def AllData(self) -> AssemblyReferenceEntry: ...
    
    @property
    def DependentAssembly(self) -> IAssemblyReferenceDependentAssemblyEntry: ...
    
    @property
    def Flags(self) -> UIntType: ...
    
    @property
    def ReferenceIdentity(self) -> IReferenceIdentity: ...
    
    # ---------- Methods ---------- #
    
    def get_AllData(self) -> AssemblyReferenceEntry: ...
    
    def get_DependentAssembly(self) -> IAssemblyReferenceDependentAssemblyEntry: ...
    
    def get_Flags(self) -> UIntType: ...
    
    def get_ReferenceIdentity(self) -> IReferenceIdentity: ...
    
    # No Events


class IAssemblyReferenceEntry(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def AllData(self) -> AssemblyReferenceEntry: ...
    
    @property
    def DependentAssembly(self) -> IAssemblyReferenceDependentAssemblyEntry: ...
    
    @property
    def Flags(self) -> UIntType: ...
    
    @property
    def ReferenceIdentity(self) -> IReferenceIdentity: ...
    
    # ---------- Methods ---------- #
    
    def get_AllData(self) -> AssemblyReferenceEntry: ...
    
    def get_DependentAssembly(self) -> IAssemblyReferenceDependentAssemblyEntry: ...
    
    def get_Flags(self) -> UIntType: ...
    
    def get_ReferenceIdentity(self) -> IReferenceIdentity: ...
    
    # No Events


class IAssemblyReferenceEntry(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def AllData(self) -> AssemblyReferenceEntry: ...
    
    @property
    def DependentAssembly(self) -> IAssemblyReferenceDependentAssemblyEntry: ...
    
    @property
    def Flags(self) -> UIntType: ...
    
    @property
    def ReferenceIdentity(self) -> IReferenceIdentity: ...
    
    # ---------- Methods ---------- #
    
    def get_AllData(self) -> AssemblyReferenceEntry: ...
    
    def get_DependentAssembly(self) -> IAssemblyReferenceDependentAssemblyEntry: ...
    
    def get_Flags(self) -> UIntType: ...
    
    def get_ReferenceIdentity(self) -> IReferenceIdentity: ...
    
    # No Events


class IAssemblyRequestEntry(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def AllData(self) -> AssemblyRequestEntry: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def permissionSetID(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_AllData(self) -> AssemblyRequestEntry: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_permissionSetID(self) -> StringType: ...
    
    # No Events


class IAssemblyRequestEntry(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def AllData(self) -> AssemblyRequestEntry: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def permissionSetID(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_AllData(self) -> AssemblyRequestEntry: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_permissionSetID(self) -> StringType: ...
    
    # No Events


class IAssemblyRequestEntry(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def AllData(self) -> AssemblyRequestEntry: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def permissionSetID(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_AllData(self) -> AssemblyRequestEntry: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_permissionSetID(self) -> StringType: ...
    
    # No Events


class ICLRSurrogateEntry(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def AllData(self) -> CLRSurrogateEntry: ...
    
    @property
    def ClassName(self) -> StringType: ...
    
    @property
    def Clsid(self) -> Guid: ...
    
    @property
    def RuntimeVersion(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_AllData(self) -> CLRSurrogateEntry: ...
    
    def get_ClassName(self) -> StringType: ...
    
    def get_Clsid(self) -> Guid: ...
    
    def get_RuntimeVersion(self) -> StringType: ...
    
    # No Events


class ICLRSurrogateEntry(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def AllData(self) -> CLRSurrogateEntry: ...
    
    @property
    def ClassName(self) -> StringType: ...
    
    @property
    def Clsid(self) -> Guid: ...
    
    @property
    def RuntimeVersion(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_AllData(self) -> CLRSurrogateEntry: ...
    
    def get_ClassName(self) -> StringType: ...
    
    def get_Clsid(self) -> Guid: ...
    
    def get_RuntimeVersion(self) -> StringType: ...
    
    # No Events


class ICLRSurrogateEntry(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def AllData(self) -> CLRSurrogateEntry: ...
    
    @property
    def ClassName(self) -> StringType: ...
    
    @property
    def Clsid(self) -> Guid: ...
    
    @property
    def RuntimeVersion(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_AllData(self) -> CLRSurrogateEntry: ...
    
    def get_ClassName(self) -> StringType: ...
    
    def get_Clsid(self) -> Guid: ...
    
    def get_RuntimeVersion(self) -> StringType: ...
    
    # No Events


class ICMS(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def AssemblyReferenceSection(self) -> ISection: ...
    
    @property
    def AssemblyRequestSection(self) -> ISection: ...
    
    @property
    def CLRSurrogateSection(self) -> ISection: ...
    
    @property
    def COMRedirectionSection(self) -> ISection: ...
    
    @property
    def CategoryMembershipSection(self) -> ISection: ...
    
    @property
    def CompatibleFrameworksSection(self) -> ISection: ...
    
    @property
    def CounterSection(self) -> ISection: ...
    
    @property
    def CounterSetSection(self) -> ISection: ...
    
    @property
    def DirectorySection(self) -> ISection: ...
    
    @property
    def EntryPointSection(self) -> ISection: ...
    
    @property
    def EventMapSection(self) -> ISection: ...
    
    @property
    def EventSection(self) -> ISection: ...
    
    @property
    def EventTagSection(self) -> ISection: ...
    
    @property
    def FileAssociationSection(self) -> ISection: ...
    
    @property
    def FileSection(self) -> ISection: ...
    
    @property
    def Identity(self) -> IDefinitionIdentity: ...
    
    @property
    def MetadataSectionEntry(self) -> ISectionEntry: ...
    
    @property
    def PermissionSetSection(self) -> ISection: ...
    
    @property
    def ProgIdRedirectionSection(self) -> ISection: ...
    
    @property
    def RegistryKeySection(self) -> ISection: ...
    
    @property
    def StringSection(self) -> ISection: ...
    
    @property
    def WindowClassSection(self) -> ISection: ...
    
    # ---------- Methods ---------- #
    
    def get_AssemblyReferenceSection(self) -> ISection: ...
    
    def get_AssemblyRequestSection(self) -> ISection: ...
    
    def get_CLRSurrogateSection(self) -> ISection: ...
    
    def get_COMRedirectionSection(self) -> ISection: ...
    
    def get_CategoryMembershipSection(self) -> ISection: ...
    
    def get_CompatibleFrameworksSection(self) -> ISection: ...
    
    def get_CounterSection(self) -> ISection: ...
    
    def get_CounterSetSection(self) -> ISection: ...
    
    def get_DirectorySection(self) -> ISection: ...
    
    def get_EntryPointSection(self) -> ISection: ...
    
    def get_EventMapSection(self) -> ISection: ...
    
    def get_EventSection(self) -> ISection: ...
    
    def get_EventTagSection(self) -> ISection: ...
    
    def get_FileAssociationSection(self) -> ISection: ...
    
    def get_FileSection(self) -> ISection: ...
    
    def get_Identity(self) -> IDefinitionIdentity: ...
    
    def get_MetadataSectionEntry(self) -> ISectionEntry: ...
    
    def get_PermissionSetSection(self) -> ISection: ...
    
    def get_ProgIdRedirectionSection(self) -> ISection: ...
    
    def get_RegistryKeySection(self) -> ISection: ...
    
    def get_StringSection(self) -> ISection: ...
    
    def get_WindowClassSection(self) -> ISection: ...
    
    # No Events


class ICMS(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def AssemblyReferenceSection(self) -> ISection: ...
    
    @property
    def AssemblyRequestSection(self) -> ISection: ...
    
    @property
    def CLRSurrogateSection(self) -> ISection: ...
    
    @property
    def COMRedirectionSection(self) -> ISection: ...
    
    @property
    def CategoryMembershipSection(self) -> ISection: ...
    
    @property
    def CompatibleFrameworksSection(self) -> ISection: ...
    
    @property
    def CounterSection(self) -> ISection: ...
    
    @property
    def CounterSetSection(self) -> ISection: ...
    
    @property
    def DirectorySection(self) -> ISection: ...
    
    @property
    def EntryPointSection(self) -> ISection: ...
    
    @property
    def EventMapSection(self) -> ISection: ...
    
    @property
    def EventSection(self) -> ISection: ...
    
    @property
    def EventTagSection(self) -> ISection: ...
    
    @property
    def FileAssociationSection(self) -> ISection: ...
    
    @property
    def FileSection(self) -> ISection: ...
    
    @property
    def Identity(self) -> IDefinitionIdentity: ...
    
    @property
    def MetadataSectionEntry(self) -> ISectionEntry: ...
    
    @property
    def PermissionSetSection(self) -> ISection: ...
    
    @property
    def ProgIdRedirectionSection(self) -> ISection: ...
    
    @property
    def RegistryKeySection(self) -> ISection: ...
    
    @property
    def StringSection(self) -> ISection: ...
    
    @property
    def WindowClassSection(self) -> ISection: ...
    
    # ---------- Methods ---------- #
    
    def get_AssemblyReferenceSection(self) -> ISection: ...
    
    def get_AssemblyRequestSection(self) -> ISection: ...
    
    def get_CLRSurrogateSection(self) -> ISection: ...
    
    def get_COMRedirectionSection(self) -> ISection: ...
    
    def get_CategoryMembershipSection(self) -> ISection: ...
    
    def get_CompatibleFrameworksSection(self) -> ISection: ...
    
    def get_CounterSection(self) -> ISection: ...
    
    def get_CounterSetSection(self) -> ISection: ...
    
    def get_DirectorySection(self) -> ISection: ...
    
    def get_EntryPointSection(self) -> ISection: ...
    
    def get_EventMapSection(self) -> ISection: ...
    
    def get_EventSection(self) -> ISection: ...
    
    def get_EventTagSection(self) -> ISection: ...
    
    def get_FileAssociationSection(self) -> ISection: ...
    
    def get_FileSection(self) -> ISection: ...
    
    def get_Identity(self) -> IDefinitionIdentity: ...
    
    def get_MetadataSectionEntry(self) -> ISectionEntry: ...
    
    def get_PermissionSetSection(self) -> ISection: ...
    
    def get_ProgIdRedirectionSection(self) -> ISection: ...
    
    def get_RegistryKeySection(self) -> ISection: ...
    
    def get_StringSection(self) -> ISection: ...
    
    def get_WindowClassSection(self) -> ISection: ...
    
    # No Events


class ICMS(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def AssemblyReferenceSection(self) -> ISection: ...
    
    @property
    def AssemblyRequestSection(self) -> ISection: ...
    
    @property
    def CLRSurrogateSection(self) -> ISection: ...
    
    @property
    def COMRedirectionSection(self) -> ISection: ...
    
    @property
    def CategoryMembershipSection(self) -> ISection: ...
    
    @property
    def CompatibleFrameworksSection(self) -> ISection: ...
    
    @property
    def CounterSection(self) -> ISection: ...
    
    @property
    def CounterSetSection(self) -> ISection: ...
    
    @property
    def DirectorySection(self) -> ISection: ...
    
    @property
    def EntryPointSection(self) -> ISection: ...
    
    @property
    def EventMapSection(self) -> ISection: ...
    
    @property
    def EventSection(self) -> ISection: ...
    
    @property
    def EventTagSection(self) -> ISection: ...
    
    @property
    def FileAssociationSection(self) -> ISection: ...
    
    @property
    def FileSection(self) -> ISection: ...
    
    @property
    def Identity(self) -> IDefinitionIdentity: ...
    
    @property
    def MetadataSectionEntry(self) -> ISectionEntry: ...
    
    @property
    def PermissionSetSection(self) -> ISection: ...
    
    @property
    def ProgIdRedirectionSection(self) -> ISection: ...
    
    @property
    def RegistryKeySection(self) -> ISection: ...
    
    @property
    def StringSection(self) -> ISection: ...
    
    @property
    def WindowClassSection(self) -> ISection: ...
    
    # ---------- Methods ---------- #
    
    def get_AssemblyReferenceSection(self) -> ISection: ...
    
    def get_AssemblyRequestSection(self) -> ISection: ...
    
    def get_CLRSurrogateSection(self) -> ISection: ...
    
    def get_COMRedirectionSection(self) -> ISection: ...
    
    def get_CategoryMembershipSection(self) -> ISection: ...
    
    def get_CompatibleFrameworksSection(self) -> ISection: ...
    
    def get_CounterSection(self) -> ISection: ...
    
    def get_CounterSetSection(self) -> ISection: ...
    
    def get_DirectorySection(self) -> ISection: ...
    
    def get_EntryPointSection(self) -> ISection: ...
    
    def get_EventMapSection(self) -> ISection: ...
    
    def get_EventSection(self) -> ISection: ...
    
    def get_EventTagSection(self) -> ISection: ...
    
    def get_FileAssociationSection(self) -> ISection: ...
    
    def get_FileSection(self) -> ISection: ...
    
    def get_Identity(self) -> IDefinitionIdentity: ...
    
    def get_MetadataSectionEntry(self) -> ISectionEntry: ...
    
    def get_PermissionSetSection(self) -> ISection: ...
    
    def get_ProgIdRedirectionSection(self) -> ISection: ...
    
    def get_RegistryKeySection(self) -> ISection: ...
    
    def get_StringSection(self) -> ISection: ...
    
    def get_WindowClassSection(self) -> ISection: ...
    
    # No Events


class ICOMServerEntry(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def AllData(self) -> COMServerEntry: ...
    
    @property
    def Clsid(self) -> Guid: ...
    
    @property
    def ConfiguredGuid(self) -> Guid: ...
    
    @property
    def Flags(self) -> UIntType: ...
    
    @property
    def HostFile(self) -> StringType: ...
    
    @property
    def ImplementedClsid(self) -> Guid: ...
    
    @property
    def RuntimeVersion(self) -> StringType: ...
    
    @property
    def ThreadingModel(self) -> UIntType: ...
    
    @property
    def TypeLibrary(self) -> Guid: ...
    
    # ---------- Methods ---------- #
    
    def get_AllData(self) -> COMServerEntry: ...
    
    def get_Clsid(self) -> Guid: ...
    
    def get_ConfiguredGuid(self) -> Guid: ...
    
    def get_Flags(self) -> UIntType: ...
    
    def get_HostFile(self) -> StringType: ...
    
    def get_ImplementedClsid(self) -> Guid: ...
    
    def get_RuntimeVersion(self) -> StringType: ...
    
    def get_ThreadingModel(self) -> UIntType: ...
    
    def get_TypeLibrary(self) -> Guid: ...
    
    # No Events


class ICOMServerEntry(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def AllData(self) -> COMServerEntry: ...
    
    @property
    def Clsid(self) -> Guid: ...
    
    @property
    def ConfiguredGuid(self) -> Guid: ...
    
    @property
    def Flags(self) -> UIntType: ...
    
    @property
    def HostFile(self) -> StringType: ...
    
    @property
    def ImplementedClsid(self) -> Guid: ...
    
    @property
    def RuntimeVersion(self) -> StringType: ...
    
    @property
    def ThreadingModel(self) -> UIntType: ...
    
    @property
    def TypeLibrary(self) -> Guid: ...
    
    # ---------- Methods ---------- #
    
    def get_AllData(self) -> COMServerEntry: ...
    
    def get_Clsid(self) -> Guid: ...
    
    def get_ConfiguredGuid(self) -> Guid: ...
    
    def get_Flags(self) -> UIntType: ...
    
    def get_HostFile(self) -> StringType: ...
    
    def get_ImplementedClsid(self) -> Guid: ...
    
    def get_RuntimeVersion(self) -> StringType: ...
    
    def get_ThreadingModel(self) -> UIntType: ...
    
    def get_TypeLibrary(self) -> Guid: ...
    
    # No Events


class ICOMServerEntry(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def AllData(self) -> COMServerEntry: ...
    
    @property
    def Clsid(self) -> Guid: ...
    
    @property
    def ConfiguredGuid(self) -> Guid: ...
    
    @property
    def Flags(self) -> UIntType: ...
    
    @property
    def HostFile(self) -> StringType: ...
    
    @property
    def ImplementedClsid(self) -> Guid: ...
    
    @property
    def RuntimeVersion(self) -> StringType: ...
    
    @property
    def ThreadingModel(self) -> UIntType: ...
    
    @property
    def TypeLibrary(self) -> Guid: ...
    
    # ---------- Methods ---------- #
    
    def get_AllData(self) -> COMServerEntry: ...
    
    def get_Clsid(self) -> Guid: ...
    
    def get_ConfiguredGuid(self) -> Guid: ...
    
    def get_Flags(self) -> UIntType: ...
    
    def get_HostFile(self) -> StringType: ...
    
    def get_ImplementedClsid(self) -> Guid: ...
    
    def get_RuntimeVersion(self) -> StringType: ...
    
    def get_ThreadingModel(self) -> UIntType: ...
    
    def get_TypeLibrary(self) -> Guid: ...
    
    # No Events


class ICategoryMembershipDataEntry(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def AllData(self) -> CategoryMembershipDataEntry: ...
    
    @property
    def Description(self) -> StringType: ...
    
    @property
    def Xml(self) -> StringType: ...
    
    @property
    def index(self) -> UIntType: ...
    
    # ---------- Methods ---------- #
    
    def get_AllData(self) -> CategoryMembershipDataEntry: ...
    
    def get_Description(self) -> StringType: ...
    
    def get_Xml(self) -> StringType: ...
    
    def get_index(self) -> UIntType: ...
    
    # No Events


class ICategoryMembershipDataEntry(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def AllData(self) -> CategoryMembershipDataEntry: ...
    
    @property
    def Description(self) -> StringType: ...
    
    @property
    def Xml(self) -> StringType: ...
    
    @property
    def index(self) -> UIntType: ...
    
    # ---------- Methods ---------- #
    
    def get_AllData(self) -> CategoryMembershipDataEntry: ...
    
    def get_Description(self) -> StringType: ...
    
    def get_Xml(self) -> StringType: ...
    
    def get_index(self) -> UIntType: ...
    
    # No Events


class ICategoryMembershipDataEntry(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def AllData(self) -> CategoryMembershipDataEntry: ...
    
    @property
    def Description(self) -> StringType: ...
    
    @property
    def Xml(self) -> StringType: ...
    
    @property
    def index(self) -> UIntType: ...
    
    # ---------- Methods ---------- #
    
    def get_AllData(self) -> CategoryMembershipDataEntry: ...
    
    def get_Description(self) -> StringType: ...
    
    def get_Xml(self) -> StringType: ...
    
    def get_index(self) -> UIntType: ...
    
    # No Events


class ICategoryMembershipEntry(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def AllData(self) -> CategoryMembershipEntry: ...
    
    @property
    def Identity(self) -> IDefinitionIdentity: ...
    
    @property
    def SubcategoryMembership(self) -> ISection: ...
    
    # ---------- Methods ---------- #
    
    def get_AllData(self) -> CategoryMembershipEntry: ...
    
    def get_Identity(self) -> IDefinitionIdentity: ...
    
    def get_SubcategoryMembership(self) -> ISection: ...
    
    # No Events


class ICategoryMembershipEntry(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def AllData(self) -> CategoryMembershipEntry: ...
    
    @property
    def Identity(self) -> IDefinitionIdentity: ...
    
    @property
    def SubcategoryMembership(self) -> ISection: ...
    
    # ---------- Methods ---------- #
    
    def get_AllData(self) -> CategoryMembershipEntry: ...
    
    def get_Identity(self) -> IDefinitionIdentity: ...
    
    def get_SubcategoryMembership(self) -> ISection: ...
    
    # No Events


class ICategoryMembershipEntry(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def AllData(self) -> CategoryMembershipEntry: ...
    
    @property
    def Identity(self) -> IDefinitionIdentity: ...
    
    @property
    def SubcategoryMembership(self) -> ISection: ...
    
    # ---------- Methods ---------- #
    
    def get_AllData(self) -> CategoryMembershipEntry: ...
    
    def get_Identity(self) -> IDefinitionIdentity: ...
    
    def get_SubcategoryMembership(self) -> ISection: ...
    
    # No Events


class ICompatibleFrameworksMetadataEntry(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def AllData(self) -> CompatibleFrameworksMetadataEntry: ...
    
    @property
    def SupportUrl(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_AllData(self) -> CompatibleFrameworksMetadataEntry: ...
    
    def get_SupportUrl(self) -> StringType: ...
    
    # No Events


class ICompatibleFrameworksMetadataEntry(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def AllData(self) -> CompatibleFrameworksMetadataEntry: ...
    
    @property
    def SupportUrl(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_AllData(self) -> CompatibleFrameworksMetadataEntry: ...
    
    def get_SupportUrl(self) -> StringType: ...
    
    # No Events


class ICompatibleFrameworksMetadataEntry(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def AllData(self) -> CompatibleFrameworksMetadataEntry: ...
    
    @property
    def SupportUrl(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_AllData(self) -> CompatibleFrameworksMetadataEntry: ...
    
    def get_SupportUrl(self) -> StringType: ...
    
    # No Events


class IDependentOSMetadataEntry(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def AllData(self) -> DependentOSMetadataEntry: ...
    
    @property
    def BuildNumber(self) -> UShortType: ...
    
    @property
    def Description(self) -> StringType: ...
    
    @property
    def MajorVersion(self) -> UShortType: ...
    
    @property
    def MinorVersion(self) -> UShortType: ...
    
    @property
    def ServicePackMajor(self) -> ByteType: ...
    
    @property
    def ServicePackMinor(self) -> ByteType: ...
    
    @property
    def SupportUrl(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_AllData(self) -> DependentOSMetadataEntry: ...
    
    def get_BuildNumber(self) -> UShortType: ...
    
    def get_Description(self) -> StringType: ...
    
    def get_MajorVersion(self) -> UShortType: ...
    
    def get_MinorVersion(self) -> UShortType: ...
    
    def get_ServicePackMajor(self) -> ByteType: ...
    
    def get_ServicePackMinor(self) -> ByteType: ...
    
    def get_SupportUrl(self) -> StringType: ...
    
    # No Events


class IDependentOSMetadataEntry(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def AllData(self) -> DependentOSMetadataEntry: ...
    
    @property
    def BuildNumber(self) -> UShortType: ...
    
    @property
    def Description(self) -> StringType: ...
    
    @property
    def MajorVersion(self) -> UShortType: ...
    
    @property
    def MinorVersion(self) -> UShortType: ...
    
    @property
    def ServicePackMajor(self) -> ByteType: ...
    
    @property
    def ServicePackMinor(self) -> ByteType: ...
    
    @property
    def SupportUrl(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_AllData(self) -> DependentOSMetadataEntry: ...
    
    def get_BuildNumber(self) -> UShortType: ...
    
    def get_Description(self) -> StringType: ...
    
    def get_MajorVersion(self) -> UShortType: ...
    
    def get_MinorVersion(self) -> UShortType: ...
    
    def get_ServicePackMajor(self) -> ByteType: ...
    
    def get_ServicePackMinor(self) -> ByteType: ...
    
    def get_SupportUrl(self) -> StringType: ...
    
    # No Events


class IDependentOSMetadataEntry(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def AllData(self) -> DependentOSMetadataEntry: ...
    
    @property
    def BuildNumber(self) -> UShortType: ...
    
    @property
    def Description(self) -> StringType: ...
    
    @property
    def MajorVersion(self) -> UShortType: ...
    
    @property
    def MinorVersion(self) -> UShortType: ...
    
    @property
    def ServicePackMajor(self) -> ByteType: ...
    
    @property
    def ServicePackMinor(self) -> ByteType: ...
    
    @property
    def SupportUrl(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_AllData(self) -> DependentOSMetadataEntry: ...
    
    def get_BuildNumber(self) -> UShortType: ...
    
    def get_Description(self) -> StringType: ...
    
    def get_MajorVersion(self) -> UShortType: ...
    
    def get_MinorVersion(self) -> UShortType: ...
    
    def get_ServicePackMajor(self) -> ByteType: ...
    
    def get_ServicePackMinor(self) -> ByteType: ...
    
    def get_SupportUrl(self) -> StringType: ...
    
    # No Events


class IDeploymentMetadataEntry(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def AllData(self) -> DeploymentMetadataEntry: ...
    
    @property
    def DeploymentFlags(self) -> UIntType: ...
    
    @property
    def DeploymentProviderCodebase(self) -> StringType: ...
    
    @property
    def MaximumAge(self) -> UShortType: ...
    
    @property
    def MaximumAge_Unit(self) -> ByteType: ...
    
    @property
    def MinimumRequiredVersion(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_AllData(self) -> DeploymentMetadataEntry: ...
    
    def get_DeploymentFlags(self) -> UIntType: ...
    
    def get_DeploymentProviderCodebase(self) -> StringType: ...
    
    def get_MaximumAge(self) -> UShortType: ...
    
    def get_MaximumAge_Unit(self) -> ByteType: ...
    
    def get_MinimumRequiredVersion(self) -> StringType: ...
    
    # No Events


class IDeploymentMetadataEntry(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def AllData(self) -> DeploymentMetadataEntry: ...
    
    @property
    def DeploymentFlags(self) -> UIntType: ...
    
    @property
    def DeploymentProviderCodebase(self) -> StringType: ...
    
    @property
    def MaximumAge(self) -> UShortType: ...
    
    @property
    def MaximumAge_Unit(self) -> ByteType: ...
    
    @property
    def MinimumRequiredVersion(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_AllData(self) -> DeploymentMetadataEntry: ...
    
    def get_DeploymentFlags(self) -> UIntType: ...
    
    def get_DeploymentProviderCodebase(self) -> StringType: ...
    
    def get_MaximumAge(self) -> UShortType: ...
    
    def get_MaximumAge_Unit(self) -> ByteType: ...
    
    def get_MinimumRequiredVersion(self) -> StringType: ...
    
    # No Events


class IDeploymentMetadataEntry(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def AllData(self) -> DeploymentMetadataEntry: ...
    
    @property
    def DeploymentFlags(self) -> UIntType: ...
    
    @property
    def DeploymentProviderCodebase(self) -> StringType: ...
    
    @property
    def MaximumAge(self) -> UShortType: ...
    
    @property
    def MaximumAge_Unit(self) -> ByteType: ...
    
    @property
    def MinimumRequiredVersion(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_AllData(self) -> DeploymentMetadataEntry: ...
    
    def get_DeploymentFlags(self) -> UIntType: ...
    
    def get_DeploymentProviderCodebase(self) -> StringType: ...
    
    def get_MaximumAge(self) -> UShortType: ...
    
    def get_MaximumAge_Unit(self) -> ByteType: ...
    
    def get_MinimumRequiredVersion(self) -> StringType: ...
    
    # No Events


class IDescriptionMetadataEntry(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def AllData(self) -> DescriptionMetadataEntry: ...
    
    @property
    def ErrorReportUrl(self) -> StringType: ...
    
    @property
    def IconFile(self) -> StringType: ...
    
    @property
    def Product(self) -> StringType: ...
    
    @property
    def Publisher(self) -> StringType: ...
    
    @property
    def SuiteName(self) -> StringType: ...
    
    @property
    def SupportUrl(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_AllData(self) -> DescriptionMetadataEntry: ...
    
    def get_ErrorReportUrl(self) -> StringType: ...
    
    def get_IconFile(self) -> StringType: ...
    
    def get_Product(self) -> StringType: ...
    
    def get_Publisher(self) -> StringType: ...
    
    def get_SuiteName(self) -> StringType: ...
    
    def get_SupportUrl(self) -> StringType: ...
    
    # No Events


class IDescriptionMetadataEntry(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def AllData(self) -> DescriptionMetadataEntry: ...
    
    @property
    def ErrorReportUrl(self) -> StringType: ...
    
    @property
    def IconFile(self) -> StringType: ...
    
    @property
    def Product(self) -> StringType: ...
    
    @property
    def Publisher(self) -> StringType: ...
    
    @property
    def SuiteName(self) -> StringType: ...
    
    @property
    def SupportUrl(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_AllData(self) -> DescriptionMetadataEntry: ...
    
    def get_ErrorReportUrl(self) -> StringType: ...
    
    def get_IconFile(self) -> StringType: ...
    
    def get_Product(self) -> StringType: ...
    
    def get_Publisher(self) -> StringType: ...
    
    def get_SuiteName(self) -> StringType: ...
    
    def get_SupportUrl(self) -> StringType: ...
    
    # No Events


class IDescriptionMetadataEntry(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def AllData(self) -> DescriptionMetadataEntry: ...
    
    @property
    def ErrorReportUrl(self) -> StringType: ...
    
    @property
    def IconFile(self) -> StringType: ...
    
    @property
    def Product(self) -> StringType: ...
    
    @property
    def Publisher(self) -> StringType: ...
    
    @property
    def SuiteName(self) -> StringType: ...
    
    @property
    def SupportUrl(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_AllData(self) -> DescriptionMetadataEntry: ...
    
    def get_ErrorReportUrl(self) -> StringType: ...
    
    def get_IconFile(self) -> StringType: ...
    
    def get_Product(self) -> StringType: ...
    
    def get_Publisher(self) -> StringType: ...
    
    def get_SuiteName(self) -> StringType: ...
    
    def get_SupportUrl(self) -> StringType: ...
    
    # No Events


class IEntryPointEntry(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def AllData(self) -> EntryPointEntry: ...
    
    @property
    def CommandLine_File(self) -> StringType: ...
    
    @property
    def CommandLine_Parameters(self) -> StringType: ...
    
    @property
    def Flags(self) -> UIntType: ...
    
    @property
    def Identity(self) -> IReferenceIdentity: ...
    
    @property
    def Name(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_AllData(self) -> EntryPointEntry: ...
    
    def get_CommandLine_File(self) -> StringType: ...
    
    def get_CommandLine_Parameters(self) -> StringType: ...
    
    def get_Flags(self) -> UIntType: ...
    
    def get_Identity(self) -> IReferenceIdentity: ...
    
    def get_Name(self) -> StringType: ...
    
    # No Events


class IEntryPointEntry(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def AllData(self) -> EntryPointEntry: ...
    
    @property
    def CommandLine_File(self) -> StringType: ...
    
    @property
    def CommandLine_Parameters(self) -> StringType: ...
    
    @property
    def Flags(self) -> UIntType: ...
    
    @property
    def Identity(self) -> IReferenceIdentity: ...
    
    @property
    def Name(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_AllData(self) -> EntryPointEntry: ...
    
    def get_CommandLine_File(self) -> StringType: ...
    
    def get_CommandLine_Parameters(self) -> StringType: ...
    
    def get_Flags(self) -> UIntType: ...
    
    def get_Identity(self) -> IReferenceIdentity: ...
    
    def get_Name(self) -> StringType: ...
    
    # No Events


class IEntryPointEntry(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def AllData(self) -> EntryPointEntry: ...
    
    @property
    def CommandLine_File(self) -> StringType: ...
    
    @property
    def CommandLine_Parameters(self) -> StringType: ...
    
    @property
    def Flags(self) -> UIntType: ...
    
    @property
    def Identity(self) -> IReferenceIdentity: ...
    
    @property
    def Name(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_AllData(self) -> EntryPointEntry: ...
    
    def get_CommandLine_File(self) -> StringType: ...
    
    def get_CommandLine_Parameters(self) -> StringType: ...
    
    def get_Flags(self) -> UIntType: ...
    
    def get_Identity(self) -> IReferenceIdentity: ...
    
    def get_Name(self) -> StringType: ...
    
    # No Events


class IFileAssociationEntry(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def AllData(self) -> FileAssociationEntry: ...
    
    @property
    def DefaultIcon(self) -> StringType: ...
    
    @property
    def Description(self) -> StringType: ...
    
    @property
    def Extension(self) -> StringType: ...
    
    @property
    def Parameter(self) -> StringType: ...
    
    @property
    def ProgID(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_AllData(self) -> FileAssociationEntry: ...
    
    def get_DefaultIcon(self) -> StringType: ...
    
    def get_Description(self) -> StringType: ...
    
    def get_Extension(self) -> StringType: ...
    
    def get_Parameter(self) -> StringType: ...
    
    def get_ProgID(self) -> StringType: ...
    
    # No Events


class IFileAssociationEntry(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def AllData(self) -> FileAssociationEntry: ...
    
    @property
    def DefaultIcon(self) -> StringType: ...
    
    @property
    def Description(self) -> StringType: ...
    
    @property
    def Extension(self) -> StringType: ...
    
    @property
    def Parameter(self) -> StringType: ...
    
    @property
    def ProgID(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_AllData(self) -> FileAssociationEntry: ...
    
    def get_DefaultIcon(self) -> StringType: ...
    
    def get_Description(self) -> StringType: ...
    
    def get_Extension(self) -> StringType: ...
    
    def get_Parameter(self) -> StringType: ...
    
    def get_ProgID(self) -> StringType: ...
    
    # No Events


class IFileAssociationEntry(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def AllData(self) -> FileAssociationEntry: ...
    
    @property
    def DefaultIcon(self) -> StringType: ...
    
    @property
    def Description(self) -> StringType: ...
    
    @property
    def Extension(self) -> StringType: ...
    
    @property
    def Parameter(self) -> StringType: ...
    
    @property
    def ProgID(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_AllData(self) -> FileAssociationEntry: ...
    
    def get_DefaultIcon(self) -> StringType: ...
    
    def get_Description(self) -> StringType: ...
    
    def get_Extension(self) -> StringType: ...
    
    def get_Parameter(self) -> StringType: ...
    
    def get_ProgID(self) -> StringType: ...
    
    # No Events


class IFileEntry(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def AllData(self) -> FileEntry: ...
    
    @property
    def Flags(self) -> UIntType: ...
    
    @property
    def Group(self) -> StringType: ...
    
    @property
    def HashAlgorithm(self) -> UIntType: ...
    
    @property
    def HashElements(self) -> ISection: ...
    
    @property
    def HashValue(self) -> ObjectType: ...
    
    @property
    def ImportPath(self) -> StringType: ...
    
    @property
    def LoadFrom(self) -> StringType: ...
    
    @property
    def Location(self) -> StringType: ...
    
    @property
    def MuiMapping(self) -> IMuiResourceMapEntry: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def Size(self) -> ULongType: ...
    
    @property
    def SourceName(self) -> StringType: ...
    
    @property
    def SourcePath(self) -> StringType: ...
    
    @property
    def WritableType(self) -> UIntType: ...
    
    # ---------- Methods ---------- #
    
    def get_AllData(self) -> FileEntry: ...
    
    def get_Flags(self) -> UIntType: ...
    
    def get_Group(self) -> StringType: ...
    
    def get_HashAlgorithm(self) -> UIntType: ...
    
    def get_HashElements(self) -> ISection: ...
    
    def get_HashValue(self) -> ObjectType: ...
    
    def get_ImportPath(self) -> StringType: ...
    
    def get_LoadFrom(self) -> StringType: ...
    
    def get_Location(self) -> StringType: ...
    
    def get_MuiMapping(self) -> IMuiResourceMapEntry: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_Size(self) -> ULongType: ...
    
    def get_SourceName(self) -> StringType: ...
    
    def get_SourcePath(self) -> StringType: ...
    
    def get_WritableType(self) -> UIntType: ...
    
    # No Events


class IFileEntry(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def AllData(self) -> FileEntry: ...
    
    @property
    def Flags(self) -> UIntType: ...
    
    @property
    def Group(self) -> StringType: ...
    
    @property
    def HashAlgorithm(self) -> UIntType: ...
    
    @property
    def HashElements(self) -> ISection: ...
    
    @property
    def HashValue(self) -> ObjectType: ...
    
    @property
    def ImportPath(self) -> StringType: ...
    
    @property
    def LoadFrom(self) -> StringType: ...
    
    @property
    def Location(self) -> StringType: ...
    
    @property
    def MuiMapping(self) -> IMuiResourceMapEntry: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def Size(self) -> ULongType: ...
    
    @property
    def SourceName(self) -> StringType: ...
    
    @property
    def SourcePath(self) -> StringType: ...
    
    @property
    def WritableType(self) -> UIntType: ...
    
    # ---------- Methods ---------- #
    
    def get_AllData(self) -> FileEntry: ...
    
    def get_Flags(self) -> UIntType: ...
    
    def get_Group(self) -> StringType: ...
    
    def get_HashAlgorithm(self) -> UIntType: ...
    
    def get_HashElements(self) -> ISection: ...
    
    def get_HashValue(self) -> ObjectType: ...
    
    def get_ImportPath(self) -> StringType: ...
    
    def get_LoadFrom(self) -> StringType: ...
    
    def get_Location(self) -> StringType: ...
    
    def get_MuiMapping(self) -> IMuiResourceMapEntry: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_Size(self) -> ULongType: ...
    
    def get_SourceName(self) -> StringType: ...
    
    def get_SourcePath(self) -> StringType: ...
    
    def get_WritableType(self) -> UIntType: ...
    
    # No Events


class IFileEntry(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def AllData(self) -> FileEntry: ...
    
    @property
    def Flags(self) -> UIntType: ...
    
    @property
    def Group(self) -> StringType: ...
    
    @property
    def HashAlgorithm(self) -> UIntType: ...
    
    @property
    def HashElements(self) -> ISection: ...
    
    @property
    def HashValue(self) -> ObjectType: ...
    
    @property
    def ImportPath(self) -> StringType: ...
    
    @property
    def LoadFrom(self) -> StringType: ...
    
    @property
    def Location(self) -> StringType: ...
    
    @property
    def MuiMapping(self) -> IMuiResourceMapEntry: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def Size(self) -> ULongType: ...
    
    @property
    def SourceName(self) -> StringType: ...
    
    @property
    def SourcePath(self) -> StringType: ...
    
    @property
    def WritableType(self) -> UIntType: ...
    
    # ---------- Methods ---------- #
    
    def get_AllData(self) -> FileEntry: ...
    
    def get_Flags(self) -> UIntType: ...
    
    def get_Group(self) -> StringType: ...
    
    def get_HashAlgorithm(self) -> UIntType: ...
    
    def get_HashElements(self) -> ISection: ...
    
    def get_HashValue(self) -> ObjectType: ...
    
    def get_ImportPath(self) -> StringType: ...
    
    def get_LoadFrom(self) -> StringType: ...
    
    def get_Location(self) -> StringType: ...
    
    def get_MuiMapping(self) -> IMuiResourceMapEntry: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_Size(self) -> ULongType: ...
    
    def get_SourceName(self) -> StringType: ...
    
    def get_SourcePath(self) -> StringType: ...
    
    def get_WritableType(self) -> UIntType: ...
    
    # No Events


class IHashElementEntry(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def AllData(self) -> HashElementEntry: ...
    
    @property
    def DigestMethod(self) -> ByteType: ...
    
    @property
    def DigestValue(self) -> ObjectType: ...
    
    @property
    def Transform(self) -> ByteType: ...
    
    @property
    def TransformMetadata(self) -> ObjectType: ...
    
    @property
    def Xml(self) -> StringType: ...
    
    @property
    def index(self) -> UIntType: ...
    
    # ---------- Methods ---------- #
    
    def get_AllData(self) -> HashElementEntry: ...
    
    def get_DigestMethod(self) -> ByteType: ...
    
    def get_DigestValue(self) -> ObjectType: ...
    
    def get_Transform(self) -> ByteType: ...
    
    def get_TransformMetadata(self) -> ObjectType: ...
    
    def get_Xml(self) -> StringType: ...
    
    def get_index(self) -> UIntType: ...
    
    # No Events


class IHashElementEntry(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def AllData(self) -> HashElementEntry: ...
    
    @property
    def DigestMethod(self) -> ByteType: ...
    
    @property
    def DigestValue(self) -> ObjectType: ...
    
    @property
    def Transform(self) -> ByteType: ...
    
    @property
    def TransformMetadata(self) -> ObjectType: ...
    
    @property
    def Xml(self) -> StringType: ...
    
    @property
    def index(self) -> UIntType: ...
    
    # ---------- Methods ---------- #
    
    def get_AllData(self) -> HashElementEntry: ...
    
    def get_DigestMethod(self) -> ByteType: ...
    
    def get_DigestValue(self) -> ObjectType: ...
    
    def get_Transform(self) -> ByteType: ...
    
    def get_TransformMetadata(self) -> ObjectType: ...
    
    def get_Xml(self) -> StringType: ...
    
    def get_index(self) -> UIntType: ...
    
    # No Events


class IHashElementEntry(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def AllData(self) -> HashElementEntry: ...
    
    @property
    def DigestMethod(self) -> ByteType: ...
    
    @property
    def DigestValue(self) -> ObjectType: ...
    
    @property
    def Transform(self) -> ByteType: ...
    
    @property
    def TransformMetadata(self) -> ObjectType: ...
    
    @property
    def Xml(self) -> StringType: ...
    
    @property
    def index(self) -> UIntType: ...
    
    # ---------- Methods ---------- #
    
    def get_AllData(self) -> HashElementEntry: ...
    
    def get_DigestMethod(self) -> ByteType: ...
    
    def get_DigestValue(self) -> ObjectType: ...
    
    def get_Transform(self) -> ByteType: ...
    
    def get_TransformMetadata(self) -> ObjectType: ...
    
    def get_Xml(self) -> StringType: ...
    
    def get_index(self) -> UIntType: ...
    
    # No Events


class IMetadataSectionEntry(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def AllData(self) -> MetadataSectionEntry: ...
    
    @property
    def CdfIdentity(self) -> IDefinitionIdentity: ...
    
    @property
    def CompatibleFrameworksData(self) -> ICompatibleFrameworksMetadataEntry: ...
    
    @property
    def ContentType(self) -> StringType: ...
    
    @property
    def DependentOSData(self) -> IDependentOSMetadataEntry: ...
    
    @property
    def DeploymentData(self) -> IDeploymentMetadataEntry: ...
    
    @property
    def DescriptionData(self) -> IDescriptionMetadataEntry: ...
    
    @property
    def HashAlgorithm(self) -> UIntType: ...
    
    @property
    def KeyInfoElement(self) -> StringType: ...
    
    @property
    def LocalPath(self) -> StringType: ...
    
    @property
    def ManifestFlags(self) -> UIntType: ...
    
    @property
    def ManifestHash(self) -> ObjectType: ...
    
    @property
    def MvidValue(self) -> ObjectType: ...
    
    @property
    def RequestedExecutionLevel(self) -> StringType: ...
    
    @property
    def RequestedExecutionLevelUIAccess(self) -> BooleanType: ...
    
    @property
    def ResourceTypeManifestResourcesDependency(self) -> IReferenceIdentity: ...
    
    @property
    def ResourceTypeResourcesDependency(self) -> IReferenceIdentity: ...
    
    @property
    def RuntimeImageVersion(self) -> StringType: ...
    
    @property
    def SchemaVersion(self) -> UIntType: ...
    
    @property
    def UsagePatterns(self) -> UIntType: ...
    
    @property
    def defaultPermissionSetID(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_AllData(self) -> MetadataSectionEntry: ...
    
    def get_CdfIdentity(self) -> IDefinitionIdentity: ...
    
    def get_CompatibleFrameworksData(self) -> ICompatibleFrameworksMetadataEntry: ...
    
    def get_ContentType(self) -> StringType: ...
    
    def get_DependentOSData(self) -> IDependentOSMetadataEntry: ...
    
    def get_DeploymentData(self) -> IDeploymentMetadataEntry: ...
    
    def get_DescriptionData(self) -> IDescriptionMetadataEntry: ...
    
    def get_HashAlgorithm(self) -> UIntType: ...
    
    def get_KeyInfoElement(self) -> StringType: ...
    
    def get_LocalPath(self) -> StringType: ...
    
    def get_ManifestFlags(self) -> UIntType: ...
    
    def get_ManifestHash(self) -> ObjectType: ...
    
    def get_MvidValue(self) -> ObjectType: ...
    
    def get_RequestedExecutionLevel(self) -> StringType: ...
    
    def get_RequestedExecutionLevelUIAccess(self) -> BooleanType: ...
    
    def get_ResourceTypeManifestResourcesDependency(self) -> IReferenceIdentity: ...
    
    def get_ResourceTypeResourcesDependency(self) -> IReferenceIdentity: ...
    
    def get_RuntimeImageVersion(self) -> StringType: ...
    
    def get_SchemaVersion(self) -> UIntType: ...
    
    def get_UsagePatterns(self) -> UIntType: ...
    
    def get_defaultPermissionSetID(self) -> StringType: ...
    
    # No Events


class IMetadataSectionEntry(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def AllData(self) -> MetadataSectionEntry: ...
    
    @property
    def CdfIdentity(self) -> IDefinitionIdentity: ...
    
    @property
    def CompatibleFrameworksData(self) -> ICompatibleFrameworksMetadataEntry: ...
    
    @property
    def ContentType(self) -> StringType: ...
    
    @property
    def DependentOSData(self) -> IDependentOSMetadataEntry: ...
    
    @property
    def DeploymentData(self) -> IDeploymentMetadataEntry: ...
    
    @property
    def DescriptionData(self) -> IDescriptionMetadataEntry: ...
    
    @property
    def HashAlgorithm(self) -> UIntType: ...
    
    @property
    def KeyInfoElement(self) -> StringType: ...
    
    @property
    def LocalPath(self) -> StringType: ...
    
    @property
    def ManifestFlags(self) -> UIntType: ...
    
    @property
    def ManifestHash(self) -> ObjectType: ...
    
    @property
    def MvidValue(self) -> ObjectType: ...
    
    @property
    def RequestedExecutionLevel(self) -> StringType: ...
    
    @property
    def RequestedExecutionLevelUIAccess(self) -> BooleanType: ...
    
    @property
    def ResourceTypeManifestResourcesDependency(self) -> IReferenceIdentity: ...
    
    @property
    def ResourceTypeResourcesDependency(self) -> IReferenceIdentity: ...
    
    @property
    def RuntimeImageVersion(self) -> StringType: ...
    
    @property
    def SchemaVersion(self) -> UIntType: ...
    
    @property
    def UsagePatterns(self) -> UIntType: ...
    
    @property
    def defaultPermissionSetID(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_AllData(self) -> MetadataSectionEntry: ...
    
    def get_CdfIdentity(self) -> IDefinitionIdentity: ...
    
    def get_CompatibleFrameworksData(self) -> ICompatibleFrameworksMetadataEntry: ...
    
    def get_ContentType(self) -> StringType: ...
    
    def get_DependentOSData(self) -> IDependentOSMetadataEntry: ...
    
    def get_DeploymentData(self) -> IDeploymentMetadataEntry: ...
    
    def get_DescriptionData(self) -> IDescriptionMetadataEntry: ...
    
    def get_HashAlgorithm(self) -> UIntType: ...
    
    def get_KeyInfoElement(self) -> StringType: ...
    
    def get_LocalPath(self) -> StringType: ...
    
    def get_ManifestFlags(self) -> UIntType: ...
    
    def get_ManifestHash(self) -> ObjectType: ...
    
    def get_MvidValue(self) -> ObjectType: ...
    
    def get_RequestedExecutionLevel(self) -> StringType: ...
    
    def get_RequestedExecutionLevelUIAccess(self) -> BooleanType: ...
    
    def get_ResourceTypeManifestResourcesDependency(self) -> IReferenceIdentity: ...
    
    def get_ResourceTypeResourcesDependency(self) -> IReferenceIdentity: ...
    
    def get_RuntimeImageVersion(self) -> StringType: ...
    
    def get_SchemaVersion(self) -> UIntType: ...
    
    def get_UsagePatterns(self) -> UIntType: ...
    
    def get_defaultPermissionSetID(self) -> StringType: ...
    
    # No Events


class IMetadataSectionEntry(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def AllData(self) -> MetadataSectionEntry: ...
    
    @property
    def CdfIdentity(self) -> IDefinitionIdentity: ...
    
    @property
    def CompatibleFrameworksData(self) -> ICompatibleFrameworksMetadataEntry: ...
    
    @property
    def ContentType(self) -> StringType: ...
    
    @property
    def DependentOSData(self) -> IDependentOSMetadataEntry: ...
    
    @property
    def DeploymentData(self) -> IDeploymentMetadataEntry: ...
    
    @property
    def DescriptionData(self) -> IDescriptionMetadataEntry: ...
    
    @property
    def HashAlgorithm(self) -> UIntType: ...
    
    @property
    def KeyInfoElement(self) -> StringType: ...
    
    @property
    def LocalPath(self) -> StringType: ...
    
    @property
    def ManifestFlags(self) -> UIntType: ...
    
    @property
    def ManifestHash(self) -> ObjectType: ...
    
    @property
    def MvidValue(self) -> ObjectType: ...
    
    @property
    def RequestedExecutionLevel(self) -> StringType: ...
    
    @property
    def RequestedExecutionLevelUIAccess(self) -> BooleanType: ...
    
    @property
    def ResourceTypeManifestResourcesDependency(self) -> IReferenceIdentity: ...
    
    @property
    def ResourceTypeResourcesDependency(self) -> IReferenceIdentity: ...
    
    @property
    def RuntimeImageVersion(self) -> StringType: ...
    
    @property
    def SchemaVersion(self) -> UIntType: ...
    
    @property
    def UsagePatterns(self) -> UIntType: ...
    
    @property
    def defaultPermissionSetID(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_AllData(self) -> MetadataSectionEntry: ...
    
    def get_CdfIdentity(self) -> IDefinitionIdentity: ...
    
    def get_CompatibleFrameworksData(self) -> ICompatibleFrameworksMetadataEntry: ...
    
    def get_ContentType(self) -> StringType: ...
    
    def get_DependentOSData(self) -> IDependentOSMetadataEntry: ...
    
    def get_DeploymentData(self) -> IDeploymentMetadataEntry: ...
    
    def get_DescriptionData(self) -> IDescriptionMetadataEntry: ...
    
    def get_HashAlgorithm(self) -> UIntType: ...
    
    def get_KeyInfoElement(self) -> StringType: ...
    
    def get_LocalPath(self) -> StringType: ...
    
    def get_ManifestFlags(self) -> UIntType: ...
    
    def get_ManifestHash(self) -> ObjectType: ...
    
    def get_MvidValue(self) -> ObjectType: ...
    
    def get_RequestedExecutionLevel(self) -> StringType: ...
    
    def get_RequestedExecutionLevelUIAccess(self) -> BooleanType: ...
    
    def get_ResourceTypeManifestResourcesDependency(self) -> IReferenceIdentity: ...
    
    def get_ResourceTypeResourcesDependency(self) -> IReferenceIdentity: ...
    
    def get_RuntimeImageVersion(self) -> StringType: ...
    
    def get_SchemaVersion(self) -> UIntType: ...
    
    def get_UsagePatterns(self) -> UIntType: ...
    
    def get_defaultPermissionSetID(self) -> StringType: ...
    
    # No Events


class IMuiResourceIdLookupMapEntry(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def AllData(self) -> MuiResourceIdLookupMapEntry: ...
    
    @property
    def Count(self) -> UIntType: ...
    
    # ---------- Methods ---------- #
    
    def get_AllData(self) -> MuiResourceIdLookupMapEntry: ...
    
    def get_Count(self) -> UIntType: ...
    
    # No Events


class IMuiResourceIdLookupMapEntry(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def AllData(self) -> MuiResourceIdLookupMapEntry: ...
    
    @property
    def Count(self) -> UIntType: ...
    
    # ---------- Methods ---------- #
    
    def get_AllData(self) -> MuiResourceIdLookupMapEntry: ...
    
    def get_Count(self) -> UIntType: ...
    
    # No Events


class IMuiResourceIdLookupMapEntry(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def AllData(self) -> MuiResourceIdLookupMapEntry: ...
    
    @property
    def Count(self) -> UIntType: ...
    
    # ---------- Methods ---------- #
    
    def get_AllData(self) -> MuiResourceIdLookupMapEntry: ...
    
    def get_Count(self) -> UIntType: ...
    
    # No Events


class IMuiResourceMapEntry(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def AllData(self) -> MuiResourceMapEntry: ...
    
    @property
    def ResourceTypeIdInt(self) -> ObjectType: ...
    
    @property
    def ResourceTypeIdString(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def get_AllData(self) -> MuiResourceMapEntry: ...
    
    def get_ResourceTypeIdInt(self) -> ObjectType: ...
    
    def get_ResourceTypeIdString(self) -> ObjectType: ...
    
    # No Events


class IMuiResourceMapEntry(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def AllData(self) -> MuiResourceMapEntry: ...
    
    @property
    def ResourceTypeIdInt(self) -> ObjectType: ...
    
    @property
    def ResourceTypeIdString(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def get_AllData(self) -> MuiResourceMapEntry: ...
    
    def get_ResourceTypeIdInt(self) -> ObjectType: ...
    
    def get_ResourceTypeIdString(self) -> ObjectType: ...
    
    # No Events


class IMuiResourceMapEntry(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def AllData(self) -> MuiResourceMapEntry: ...
    
    @property
    def ResourceTypeIdInt(self) -> ObjectType: ...
    
    @property
    def ResourceTypeIdString(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def get_AllData(self) -> MuiResourceMapEntry: ...
    
    def get_ResourceTypeIdInt(self) -> ObjectType: ...
    
    def get_ResourceTypeIdString(self) -> ObjectType: ...
    
    # No Events


class IMuiResourceTypeIdIntEntry(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def AllData(self) -> MuiResourceTypeIdIntEntry: ...
    
    @property
    def IntegerIds(self) -> ObjectType: ...
    
    @property
    def StringIds(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def get_AllData(self) -> MuiResourceTypeIdIntEntry: ...
    
    def get_IntegerIds(self) -> ObjectType: ...
    
    def get_StringIds(self) -> ObjectType: ...
    
    # No Events


class IMuiResourceTypeIdIntEntry(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def AllData(self) -> MuiResourceTypeIdIntEntry: ...
    
    @property
    def IntegerIds(self) -> ObjectType: ...
    
    @property
    def StringIds(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def get_AllData(self) -> MuiResourceTypeIdIntEntry: ...
    
    def get_IntegerIds(self) -> ObjectType: ...
    
    def get_StringIds(self) -> ObjectType: ...
    
    # No Events


class IMuiResourceTypeIdIntEntry(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def AllData(self) -> MuiResourceTypeIdIntEntry: ...
    
    @property
    def IntegerIds(self) -> ObjectType: ...
    
    @property
    def StringIds(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def get_AllData(self) -> MuiResourceTypeIdIntEntry: ...
    
    def get_IntegerIds(self) -> ObjectType: ...
    
    def get_StringIds(self) -> ObjectType: ...
    
    # No Events


class IMuiResourceTypeIdStringEntry(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def AllData(self) -> MuiResourceTypeIdStringEntry: ...
    
    @property
    def IntegerIds(self) -> ObjectType: ...
    
    @property
    def StringIds(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def get_AllData(self) -> MuiResourceTypeIdStringEntry: ...
    
    def get_IntegerIds(self) -> ObjectType: ...
    
    def get_StringIds(self) -> ObjectType: ...
    
    # No Events


class IMuiResourceTypeIdStringEntry(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def AllData(self) -> MuiResourceTypeIdStringEntry: ...
    
    @property
    def IntegerIds(self) -> ObjectType: ...
    
    @property
    def StringIds(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def get_AllData(self) -> MuiResourceTypeIdStringEntry: ...
    
    def get_IntegerIds(self) -> ObjectType: ...
    
    def get_StringIds(self) -> ObjectType: ...
    
    # No Events


class IMuiResourceTypeIdStringEntry(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def AllData(self) -> MuiResourceTypeIdStringEntry: ...
    
    @property
    def IntegerIds(self) -> ObjectType: ...
    
    @property
    def StringIds(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def get_AllData(self) -> MuiResourceTypeIdStringEntry: ...
    
    def get_IntegerIds(self) -> ObjectType: ...
    
    def get_StringIds(self) -> ObjectType: ...
    
    # No Events


class IPermissionSetEntry(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def AllData(self) -> PermissionSetEntry: ...
    
    @property
    def Id(self) -> StringType: ...
    
    @property
    def XmlSegment(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_AllData(self) -> PermissionSetEntry: ...
    
    def get_Id(self) -> StringType: ...
    
    def get_XmlSegment(self) -> StringType: ...
    
    # No Events


class IPermissionSetEntry(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def AllData(self) -> PermissionSetEntry: ...
    
    @property
    def Id(self) -> StringType: ...
    
    @property
    def XmlSegment(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_AllData(self) -> PermissionSetEntry: ...
    
    def get_Id(self) -> StringType: ...
    
    def get_XmlSegment(self) -> StringType: ...
    
    # No Events


class IPermissionSetEntry(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def AllData(self) -> PermissionSetEntry: ...
    
    @property
    def Id(self) -> StringType: ...
    
    @property
    def XmlSegment(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_AllData(self) -> PermissionSetEntry: ...
    
    def get_Id(self) -> StringType: ...
    
    def get_XmlSegment(self) -> StringType: ...
    
    # No Events


class IProgIdRedirectionEntry(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def AllData(self) -> ProgIdRedirectionEntry: ...
    
    @property
    def ProgId(self) -> StringType: ...
    
    @property
    def RedirectedGuid(self) -> Guid: ...
    
    # ---------- Methods ---------- #
    
    def get_AllData(self) -> ProgIdRedirectionEntry: ...
    
    def get_ProgId(self) -> StringType: ...
    
    def get_RedirectedGuid(self) -> Guid: ...
    
    # No Events


class IProgIdRedirectionEntry(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def AllData(self) -> ProgIdRedirectionEntry: ...
    
    @property
    def ProgId(self) -> StringType: ...
    
    @property
    def RedirectedGuid(self) -> Guid: ...
    
    # ---------- Methods ---------- #
    
    def get_AllData(self) -> ProgIdRedirectionEntry: ...
    
    def get_ProgId(self) -> StringType: ...
    
    def get_RedirectedGuid(self) -> Guid: ...
    
    # No Events


class IProgIdRedirectionEntry(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def AllData(self) -> ProgIdRedirectionEntry: ...
    
    @property
    def ProgId(self) -> StringType: ...
    
    @property
    def RedirectedGuid(self) -> Guid: ...
    
    # ---------- Methods ---------- #
    
    def get_AllData(self) -> ProgIdRedirectionEntry: ...
    
    def get_ProgId(self) -> StringType: ...
    
    def get_RedirectedGuid(self) -> Guid: ...
    
    # No Events


class IResourceTableMappingEntry(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def AllData(self) -> ResourceTableMappingEntry: ...
    
    @property
    def FinalStringMapped(self) -> StringType: ...
    
    @property
    def id(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_AllData(self) -> ResourceTableMappingEntry: ...
    
    def get_FinalStringMapped(self) -> StringType: ...
    
    def get_id(self) -> StringType: ...
    
    # No Events


class IResourceTableMappingEntry(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def AllData(self) -> ResourceTableMappingEntry: ...
    
    @property
    def FinalStringMapped(self) -> StringType: ...
    
    @property
    def id(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_AllData(self) -> ResourceTableMappingEntry: ...
    
    def get_FinalStringMapped(self) -> StringType: ...
    
    def get_id(self) -> StringType: ...
    
    # No Events


class IResourceTableMappingEntry(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def AllData(self) -> ResourceTableMappingEntry: ...
    
    @property
    def FinalStringMapped(self) -> StringType: ...
    
    @property
    def id(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_AllData(self) -> ResourceTableMappingEntry: ...
    
    def get_FinalStringMapped(self) -> StringType: ...
    
    def get_id(self) -> StringType: ...
    
    # No Events


class ISubcategoryMembershipEntry(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def AllData(self) -> SubcategoryMembershipEntry: ...
    
    @property
    def CategoryMembershipData(self) -> ISection: ...
    
    @property
    def Subcategory(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_AllData(self) -> SubcategoryMembershipEntry: ...
    
    def get_CategoryMembershipData(self) -> ISection: ...
    
    def get_Subcategory(self) -> StringType: ...
    
    # No Events


class ISubcategoryMembershipEntry(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def AllData(self) -> SubcategoryMembershipEntry: ...
    
    @property
    def CategoryMembershipData(self) -> ISection: ...
    
    @property
    def Subcategory(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_AllData(self) -> SubcategoryMembershipEntry: ...
    
    def get_CategoryMembershipData(self) -> ISection: ...
    
    def get_Subcategory(self) -> StringType: ...
    
    # No Events


class ISubcategoryMembershipEntry(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def AllData(self) -> SubcategoryMembershipEntry: ...
    
    @property
    def CategoryMembershipData(self) -> ISection: ...
    
    @property
    def Subcategory(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_AllData(self) -> SubcategoryMembershipEntry: ...
    
    def get_CategoryMembershipData(self) -> ISection: ...
    
    def get_Subcategory(self) -> StringType: ...
    
    # No Events


class IWindowClassEntry(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def AllData(self) -> WindowClassEntry: ...
    
    @property
    def ClassName(self) -> StringType: ...
    
    @property
    def HostDll(self) -> StringType: ...
    
    @property
    def fVersioned(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def get_AllData(self) -> WindowClassEntry: ...
    
    def get_ClassName(self) -> StringType: ...
    
    def get_HostDll(self) -> StringType: ...
    
    def get_fVersioned(self) -> BooleanType: ...
    
    # No Events


class IWindowClassEntry(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def AllData(self) -> WindowClassEntry: ...
    
    @property
    def ClassName(self) -> StringType: ...
    
    @property
    def HostDll(self) -> StringType: ...
    
    @property
    def fVersioned(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def get_AllData(self) -> WindowClassEntry: ...
    
    def get_ClassName(self) -> StringType: ...
    
    def get_HostDll(self) -> StringType: ...
    
    def get_fVersioned(self) -> BooleanType: ...
    
    # No Events


class IWindowClassEntry(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def AllData(self) -> WindowClassEntry: ...
    
    @property
    def ClassName(self) -> StringType: ...
    
    @property
    def HostDll(self) -> StringType: ...
    
    @property
    def fVersioned(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def get_AllData(self) -> WindowClassEntry: ...
    
    def get_ClassName(self) -> StringType: ...
    
    def get_HostDll(self) -> StringType: ...
    
    def get_fVersioned(self) -> BooleanType: ...
    
    # No Events


# ---------- Enums ---------- #

class AssemblyReferenceDependentAssemblyEntryFieldId(Enum):
    AssemblyReferenceDependentAssembly_Group: IntType = 0
    AssemblyReferenceDependentAssembly_Codebase: IntType = 1
    AssemblyReferenceDependentAssembly_Size: IntType = 2
    AssemblyReferenceDependentAssembly_HashValue: IntType = 3
    AssemblyReferenceDependentAssembly_HashValueSize: IntType = 4
    AssemblyReferenceDependentAssembly_HashAlgorithm: IntType = 5
    AssemblyReferenceDependentAssembly_Flags: IntType = 6
    AssemblyReferenceDependentAssembly_ResourceFallbackCulture: IntType = 7
    AssemblyReferenceDependentAssembly_Description: IntType = 8
    AssemblyReferenceDependentAssembly_SupportUrl: IntType = 9
    AssemblyReferenceDependentAssembly_HashElements: IntType = 10


class AssemblyReferenceDependentAssemblyEntryFieldId(Enum):
    AssemblyReferenceDependentAssembly_Group: IntType = 0
    AssemblyReferenceDependentAssembly_Codebase: IntType = 1
    AssemblyReferenceDependentAssembly_Size: IntType = 2
    AssemblyReferenceDependentAssembly_HashValue: IntType = 3
    AssemblyReferenceDependentAssembly_HashValueSize: IntType = 4
    AssemblyReferenceDependentAssembly_HashAlgorithm: IntType = 5
    AssemblyReferenceDependentAssembly_Flags: IntType = 6
    AssemblyReferenceDependentAssembly_ResourceFallbackCulture: IntType = 7
    AssemblyReferenceDependentAssembly_Description: IntType = 8
    AssemblyReferenceDependentAssembly_SupportUrl: IntType = 9
    AssemblyReferenceDependentAssembly_HashElements: IntType = 10


class AssemblyReferenceDependentAssemblyEntryFieldId(Enum):
    AssemblyReferenceDependentAssembly_Group: IntType = 0
    AssemblyReferenceDependentAssembly_Codebase: IntType = 1
    AssemblyReferenceDependentAssembly_Size: IntType = 2
    AssemblyReferenceDependentAssembly_HashValue: IntType = 3
    AssemblyReferenceDependentAssembly_HashValueSize: IntType = 4
    AssemblyReferenceDependentAssembly_HashAlgorithm: IntType = 5
    AssemblyReferenceDependentAssembly_Flags: IntType = 6
    AssemblyReferenceDependentAssembly_ResourceFallbackCulture: IntType = 7
    AssemblyReferenceDependentAssembly_Description: IntType = 8
    AssemblyReferenceDependentAssembly_SupportUrl: IntType = 9
    AssemblyReferenceDependentAssembly_HashElements: IntType = 10


class AssemblyReferenceEntryFieldId(Enum):
    AssemblyReference_Flags: IntType = 0
    AssemblyReference_DependentAssembly: IntType = 1


class AssemblyReferenceEntryFieldId(Enum):
    AssemblyReference_Flags: IntType = 0
    AssemblyReference_DependentAssembly: IntType = 1


class AssemblyReferenceEntryFieldId(Enum):
    AssemblyReference_Flags: IntType = 0
    AssemblyReference_DependentAssembly: IntType = 1


class AssemblyRequestEntryFieldId(Enum):
    AssemblyRequest_permissionSetID: IntType = 0


class AssemblyRequestEntryFieldId(Enum):
    AssemblyRequest_permissionSetID: IntType = 0


class AssemblyRequestEntryFieldId(Enum):
    AssemblyRequest_permissionSetID: IntType = 0


class CLRSurrogateEntryFieldId(Enum):
    CLRSurrogate_RuntimeVersion: IntType = 0
    CLRSurrogate_ClassName: IntType = 1


class CLRSurrogateEntryFieldId(Enum):
    CLRSurrogate_RuntimeVersion: IntType = 0
    CLRSurrogate_ClassName: IntType = 1


class CLRSurrogateEntryFieldId(Enum):
    CLRSurrogate_RuntimeVersion: IntType = 0
    CLRSurrogate_ClassName: IntType = 1


class CMSSECTIONID(Enum):
    CMSSECTIONID_FILE_SECTION: IntType = 1
    CMSSECTIONID_CATEGORY_INSTANCE_SECTION: IntType = 2
    CMSSECTIONID_COM_REDIRECTION_SECTION: IntType = 3
    CMSSECTIONID_PROGID_REDIRECTION_SECTION: IntType = 4
    CMSSECTIONID_CLR_SURROGATE_SECTION: IntType = 5
    CMSSECTIONID_ASSEMBLY_REFERENCE_SECTION: IntType = 6
    CMSSECTIONID_WINDOW_CLASS_SECTION: IntType = 8
    CMSSECTIONID_STRING_SECTION: IntType = 9
    CMSSECTIONID_ENTRYPOINT_SECTION: IntType = 10
    CMSSECTIONID_PERMISSION_SET_SECTION: IntType = 11
    CMSSECTIONENTRYID_METADATA: IntType = 12
    CMSSECTIONID_ASSEMBLY_REQUEST_SECTION: IntType = 13
    CMSSECTIONID_REGISTRY_KEY_SECTION: IntType = 16
    CMSSECTIONID_DIRECTORY_SECTION: IntType = 17
    CMSSECTIONID_FILE_ASSOCIATION_SECTION: IntType = 18
    CMSSECTIONID_COMPATIBLE_FRAMEWORKS_SECTION: IntType = 19
    CMSSECTIONID_EVENT_SECTION: IntType = 101
    CMSSECTIONID_EVENT_MAP_SECTION: IntType = 102
    CMSSECTIONID_EVENT_TAG_SECTION: IntType = 103
    CMSSECTIONID_COUNTERSET_SECTION: IntType = 110
    CMSSECTIONID_COUNTER_SECTION: IntType = 111


class CMSSECTIONID(Enum):
    CMSSECTIONID_FILE_SECTION: IntType = 1
    CMSSECTIONID_CATEGORY_INSTANCE_SECTION: IntType = 2
    CMSSECTIONID_COM_REDIRECTION_SECTION: IntType = 3
    CMSSECTIONID_PROGID_REDIRECTION_SECTION: IntType = 4
    CMSSECTIONID_CLR_SURROGATE_SECTION: IntType = 5
    CMSSECTIONID_ASSEMBLY_REFERENCE_SECTION: IntType = 6
    CMSSECTIONID_WINDOW_CLASS_SECTION: IntType = 8
    CMSSECTIONID_STRING_SECTION: IntType = 9
    CMSSECTIONID_ENTRYPOINT_SECTION: IntType = 10
    CMSSECTIONID_PERMISSION_SET_SECTION: IntType = 11
    CMSSECTIONENTRYID_METADATA: IntType = 12
    CMSSECTIONID_ASSEMBLY_REQUEST_SECTION: IntType = 13
    CMSSECTIONID_REGISTRY_KEY_SECTION: IntType = 16
    CMSSECTIONID_DIRECTORY_SECTION: IntType = 17
    CMSSECTIONID_FILE_ASSOCIATION_SECTION: IntType = 18
    CMSSECTIONID_COMPATIBLE_FRAMEWORKS_SECTION: IntType = 19
    CMSSECTIONID_EVENT_SECTION: IntType = 101
    CMSSECTIONID_EVENT_MAP_SECTION: IntType = 102
    CMSSECTIONID_EVENT_TAG_SECTION: IntType = 103
    CMSSECTIONID_COUNTERSET_SECTION: IntType = 110
    CMSSECTIONID_COUNTER_SECTION: IntType = 111


class CMSSECTIONID(Enum):
    CMSSECTIONID_FILE_SECTION: IntType = 1
    CMSSECTIONID_CATEGORY_INSTANCE_SECTION: IntType = 2
    CMSSECTIONID_COM_REDIRECTION_SECTION: IntType = 3
    CMSSECTIONID_PROGID_REDIRECTION_SECTION: IntType = 4
    CMSSECTIONID_CLR_SURROGATE_SECTION: IntType = 5
    CMSSECTIONID_ASSEMBLY_REFERENCE_SECTION: IntType = 6
    CMSSECTIONID_WINDOW_CLASS_SECTION: IntType = 8
    CMSSECTIONID_STRING_SECTION: IntType = 9
    CMSSECTIONID_ENTRYPOINT_SECTION: IntType = 10
    CMSSECTIONID_PERMISSION_SET_SECTION: IntType = 11
    CMSSECTIONENTRYID_METADATA: IntType = 12
    CMSSECTIONID_ASSEMBLY_REQUEST_SECTION: IntType = 13
    CMSSECTIONID_REGISTRY_KEY_SECTION: IntType = 16
    CMSSECTIONID_DIRECTORY_SECTION: IntType = 17
    CMSSECTIONID_FILE_ASSOCIATION_SECTION: IntType = 18
    CMSSECTIONID_COMPATIBLE_FRAMEWORKS_SECTION: IntType = 19
    CMSSECTIONID_EVENT_SECTION: IntType = 101
    CMSSECTIONID_EVENT_MAP_SECTION: IntType = 102
    CMSSECTIONID_EVENT_TAG_SECTION: IntType = 103
    CMSSECTIONID_COUNTERSET_SECTION: IntType = 110
    CMSSECTIONID_COUNTER_SECTION: IntType = 111


class CMS_ASSEMBLY_DEPLOYMENT_FLAG(Enum):
    CMS_ASSEMBLY_DEPLOYMENT_FLAG_BEFORE_APPLICATION_STARTUP: IntType = 4
    CMS_ASSEMBLY_DEPLOYMENT_FLAG_RUN_AFTER_INSTALL: IntType = 16
    CMS_ASSEMBLY_DEPLOYMENT_FLAG_INSTALL: IntType = 32
    CMS_ASSEMBLY_DEPLOYMENT_FLAG_TRUST_URL_PARAMETERS: IntType = 64
    CMS_ASSEMBLY_DEPLOYMENT_FLAG_DISALLOW_URL_ACTIVATION: IntType = 128
    CMS_ASSEMBLY_DEPLOYMENT_FLAG_MAP_FILE_EXTENSIONS: IntType = 256
    CMS_ASSEMBLY_DEPLOYMENT_FLAG_CREATE_DESKTOP_SHORTCUT: IntType = 512


class CMS_ASSEMBLY_DEPLOYMENT_FLAG(Enum):
    CMS_ASSEMBLY_DEPLOYMENT_FLAG_BEFORE_APPLICATION_STARTUP: IntType = 4
    CMS_ASSEMBLY_DEPLOYMENT_FLAG_RUN_AFTER_INSTALL: IntType = 16
    CMS_ASSEMBLY_DEPLOYMENT_FLAG_INSTALL: IntType = 32
    CMS_ASSEMBLY_DEPLOYMENT_FLAG_TRUST_URL_PARAMETERS: IntType = 64
    CMS_ASSEMBLY_DEPLOYMENT_FLAG_DISALLOW_URL_ACTIVATION: IntType = 128
    CMS_ASSEMBLY_DEPLOYMENT_FLAG_MAP_FILE_EXTENSIONS: IntType = 256
    CMS_ASSEMBLY_DEPLOYMENT_FLAG_CREATE_DESKTOP_SHORTCUT: IntType = 512


class CMS_ASSEMBLY_DEPLOYMENT_FLAG(Enum):
    CMS_ASSEMBLY_DEPLOYMENT_FLAG_BEFORE_APPLICATION_STARTUP: IntType = 4
    CMS_ASSEMBLY_DEPLOYMENT_FLAG_RUN_AFTER_INSTALL: IntType = 16
    CMS_ASSEMBLY_DEPLOYMENT_FLAG_INSTALL: IntType = 32
    CMS_ASSEMBLY_DEPLOYMENT_FLAG_TRUST_URL_PARAMETERS: IntType = 64
    CMS_ASSEMBLY_DEPLOYMENT_FLAG_DISALLOW_URL_ACTIVATION: IntType = 128
    CMS_ASSEMBLY_DEPLOYMENT_FLAG_MAP_FILE_EXTENSIONS: IntType = 256
    CMS_ASSEMBLY_DEPLOYMENT_FLAG_CREATE_DESKTOP_SHORTCUT: IntType = 512


class CMS_ASSEMBLY_REFERENCE_DEPENDENT_ASSEMBLY_FLAG(Enum):
    CMS_ASSEMBLY_REFERENCE_DEPENDENT_ASSEMBLY_FLAG_OPTIONAL: IntType = 1
    CMS_ASSEMBLY_REFERENCE_DEPENDENT_ASSEMBLY_FLAG_VISIBLE: IntType = 2
    CMS_ASSEMBLY_REFERENCE_DEPENDENT_ASSEMBLY_FLAG_PREREQUISITE: IntType = 4
    CMS_ASSEMBLY_REFERENCE_DEPENDENT_ASSEMBLY_FLAG_RESOURCE_FALLBACK_CULTURE_INTERNAL: IntType = 8
    CMS_ASSEMBLY_REFERENCE_DEPENDENT_ASSEMBLY_FLAG_INSTALL: IntType = 16
    CMS_ASSEMBLY_REFERENCE_DEPENDENT_ASSEMBLY_FLAG_ALLOW_DELAYED_BINDING: IntType = 32


class CMS_ASSEMBLY_REFERENCE_DEPENDENT_ASSEMBLY_FLAG(Enum):
    CMS_ASSEMBLY_REFERENCE_DEPENDENT_ASSEMBLY_FLAG_OPTIONAL: IntType = 1
    CMS_ASSEMBLY_REFERENCE_DEPENDENT_ASSEMBLY_FLAG_VISIBLE: IntType = 2
    CMS_ASSEMBLY_REFERENCE_DEPENDENT_ASSEMBLY_FLAG_PREREQUISITE: IntType = 4
    CMS_ASSEMBLY_REFERENCE_DEPENDENT_ASSEMBLY_FLAG_RESOURCE_FALLBACK_CULTURE_INTERNAL: IntType = 8
    CMS_ASSEMBLY_REFERENCE_DEPENDENT_ASSEMBLY_FLAG_INSTALL: IntType = 16
    CMS_ASSEMBLY_REFERENCE_DEPENDENT_ASSEMBLY_FLAG_ALLOW_DELAYED_BINDING: IntType = 32


class CMS_ASSEMBLY_REFERENCE_DEPENDENT_ASSEMBLY_FLAG(Enum):
    CMS_ASSEMBLY_REFERENCE_DEPENDENT_ASSEMBLY_FLAG_OPTIONAL: IntType = 1
    CMS_ASSEMBLY_REFERENCE_DEPENDENT_ASSEMBLY_FLAG_VISIBLE: IntType = 2
    CMS_ASSEMBLY_REFERENCE_DEPENDENT_ASSEMBLY_FLAG_PREREQUISITE: IntType = 4
    CMS_ASSEMBLY_REFERENCE_DEPENDENT_ASSEMBLY_FLAG_RESOURCE_FALLBACK_CULTURE_INTERNAL: IntType = 8
    CMS_ASSEMBLY_REFERENCE_DEPENDENT_ASSEMBLY_FLAG_INSTALL: IntType = 16
    CMS_ASSEMBLY_REFERENCE_DEPENDENT_ASSEMBLY_FLAG_ALLOW_DELAYED_BINDING: IntType = 32


class CMS_ASSEMBLY_REFERENCE_FLAG(Enum):
    CMS_ASSEMBLY_REFERENCE_FLAG_OPTIONAL: IntType = 1
    CMS_ASSEMBLY_REFERENCE_FLAG_VISIBLE: IntType = 2
    CMS_ASSEMBLY_REFERENCE_FLAG_FOLLOW: IntType = 4
    CMS_ASSEMBLY_REFERENCE_FLAG_IS_PLATFORM: IntType = 8
    CMS_ASSEMBLY_REFERENCE_FLAG_CULTURE_WILDCARDED: IntType = 16
    CMS_ASSEMBLY_REFERENCE_FLAG_PROCESSOR_ARCHITECTURE_WILDCARDED: IntType = 32
    CMS_ASSEMBLY_REFERENCE_FLAG_PREREQUISITE: IntType = 128


class CMS_ASSEMBLY_REFERENCE_FLAG(Enum):
    CMS_ASSEMBLY_REFERENCE_FLAG_OPTIONAL: IntType = 1
    CMS_ASSEMBLY_REFERENCE_FLAG_VISIBLE: IntType = 2
    CMS_ASSEMBLY_REFERENCE_FLAG_FOLLOW: IntType = 4
    CMS_ASSEMBLY_REFERENCE_FLAG_IS_PLATFORM: IntType = 8
    CMS_ASSEMBLY_REFERENCE_FLAG_CULTURE_WILDCARDED: IntType = 16
    CMS_ASSEMBLY_REFERENCE_FLAG_PROCESSOR_ARCHITECTURE_WILDCARDED: IntType = 32
    CMS_ASSEMBLY_REFERENCE_FLAG_PREREQUISITE: IntType = 128


class CMS_ASSEMBLY_REFERENCE_FLAG(Enum):
    CMS_ASSEMBLY_REFERENCE_FLAG_OPTIONAL: IntType = 1
    CMS_ASSEMBLY_REFERENCE_FLAG_VISIBLE: IntType = 2
    CMS_ASSEMBLY_REFERENCE_FLAG_FOLLOW: IntType = 4
    CMS_ASSEMBLY_REFERENCE_FLAG_IS_PLATFORM: IntType = 8
    CMS_ASSEMBLY_REFERENCE_FLAG_CULTURE_WILDCARDED: IntType = 16
    CMS_ASSEMBLY_REFERENCE_FLAG_PROCESSOR_ARCHITECTURE_WILDCARDED: IntType = 32
    CMS_ASSEMBLY_REFERENCE_FLAG_PREREQUISITE: IntType = 128


class CMS_COM_SERVER_FLAG(Enum):
    CMS_COM_SERVER_FLAG_IS_CLR_CLASS: IntType = 1


class CMS_COM_SERVER_FLAG(Enum):
    CMS_COM_SERVER_FLAG_IS_CLR_CLASS: IntType = 1


class CMS_COM_SERVER_FLAG(Enum):
    CMS_COM_SERVER_FLAG_IS_CLR_CLASS: IntType = 1


class CMS_ENTRY_POINT_FLAG(Enum):
    CMS_ENTRY_POINT_FLAG_HOST_IN_BROWSER: IntType = 1
    CMS_ENTRY_POINT_FLAG_CUSTOMHOSTSPECIFIED: IntType = 2
    CMS_ENTRY_POINT_FLAG_CUSTOMUX: IntType = 4


class CMS_ENTRY_POINT_FLAG(Enum):
    CMS_ENTRY_POINT_FLAG_HOST_IN_BROWSER: IntType = 1
    CMS_ENTRY_POINT_FLAG_CUSTOMHOSTSPECIFIED: IntType = 2
    CMS_ENTRY_POINT_FLAG_CUSTOMUX: IntType = 4


class CMS_ENTRY_POINT_FLAG(Enum):
    CMS_ENTRY_POINT_FLAG_HOST_IN_BROWSER: IntType = 1
    CMS_ENTRY_POINT_FLAG_CUSTOMHOSTSPECIFIED: IntType = 2
    CMS_ENTRY_POINT_FLAG_CUSTOMUX: IntType = 4


class CMS_FILE_FLAG(Enum):
    CMS_FILE_FLAG_OPTIONAL: IntType = 1


class CMS_FILE_FLAG(Enum):
    CMS_FILE_FLAG_OPTIONAL: IntType = 1


class CMS_FILE_FLAG(Enum):
    CMS_FILE_FLAG_OPTIONAL: IntType = 1


class CMS_FILE_HASH_ALGORITHM(Enum):
    CMS_FILE_HASH_ALGORITHM_SHA1: IntType = 1
    CMS_FILE_HASH_ALGORITHM_SHA256: IntType = 2
    CMS_FILE_HASH_ALGORITHM_SHA384: IntType = 3
    CMS_FILE_HASH_ALGORITHM_SHA512: IntType = 4
    CMS_FILE_HASH_ALGORITHM_MD5: IntType = 5
    CMS_FILE_HASH_ALGORITHM_MD4: IntType = 6
    CMS_FILE_HASH_ALGORITHM_MD2: IntType = 7


class CMS_FILE_HASH_ALGORITHM(Enum):
    CMS_FILE_HASH_ALGORITHM_SHA1: IntType = 1
    CMS_FILE_HASH_ALGORITHM_SHA256: IntType = 2
    CMS_FILE_HASH_ALGORITHM_SHA384: IntType = 3
    CMS_FILE_HASH_ALGORITHM_SHA512: IntType = 4
    CMS_FILE_HASH_ALGORITHM_MD5: IntType = 5
    CMS_FILE_HASH_ALGORITHM_MD4: IntType = 6
    CMS_FILE_HASH_ALGORITHM_MD2: IntType = 7


class CMS_FILE_HASH_ALGORITHM(Enum):
    CMS_FILE_HASH_ALGORITHM_SHA1: IntType = 1
    CMS_FILE_HASH_ALGORITHM_SHA256: IntType = 2
    CMS_FILE_HASH_ALGORITHM_SHA384: IntType = 3
    CMS_FILE_HASH_ALGORITHM_SHA512: IntType = 4
    CMS_FILE_HASH_ALGORITHM_MD5: IntType = 5
    CMS_FILE_HASH_ALGORITHM_MD4: IntType = 6
    CMS_FILE_HASH_ALGORITHM_MD2: IntType = 7


class CMS_FILE_WRITABLE_TYPE(Enum):
    CMS_FILE_WRITABLE_TYPE_NOT_WRITABLE: IntType = 1
    CMS_FILE_WRITABLE_TYPE_APPLICATION_DATA: IntType = 2


class CMS_FILE_WRITABLE_TYPE(Enum):
    CMS_FILE_WRITABLE_TYPE_NOT_WRITABLE: IntType = 1
    CMS_FILE_WRITABLE_TYPE_APPLICATION_DATA: IntType = 2


class CMS_FILE_WRITABLE_TYPE(Enum):
    CMS_FILE_WRITABLE_TYPE_NOT_WRITABLE: IntType = 1
    CMS_FILE_WRITABLE_TYPE_APPLICATION_DATA: IntType = 2


class CMS_HASH_DIGESTMETHOD(Enum):
    CMS_HASH_DIGESTMETHOD_SHA1: IntType = 1
    CMS_HASH_DIGESTMETHOD_SHA256: IntType = 2
    CMS_HASH_DIGESTMETHOD_SHA384: IntType = 3
    CMS_HASH_DIGESTMETHOD_SHA512: IntType = 4


class CMS_HASH_DIGESTMETHOD(Enum):
    CMS_HASH_DIGESTMETHOD_SHA1: IntType = 1
    CMS_HASH_DIGESTMETHOD_SHA256: IntType = 2
    CMS_HASH_DIGESTMETHOD_SHA384: IntType = 3
    CMS_HASH_DIGESTMETHOD_SHA512: IntType = 4


class CMS_HASH_DIGESTMETHOD(Enum):
    CMS_HASH_DIGESTMETHOD_SHA1: IntType = 1
    CMS_HASH_DIGESTMETHOD_SHA256: IntType = 2
    CMS_HASH_DIGESTMETHOD_SHA384: IntType = 3
    CMS_HASH_DIGESTMETHOD_SHA512: IntType = 4


class CMS_HASH_TRANSFORM(Enum):
    CMS_HASH_TRANSFORM_IDENTITY: IntType = 1
    CMS_HASH_TRANSFORM_MANIFESTINVARIANT: IntType = 2


class CMS_HASH_TRANSFORM(Enum):
    CMS_HASH_TRANSFORM_IDENTITY: IntType = 1
    CMS_HASH_TRANSFORM_MANIFESTINVARIANT: IntType = 2


class CMS_HASH_TRANSFORM(Enum):
    CMS_HASH_TRANSFORM_IDENTITY: IntType = 1
    CMS_HASH_TRANSFORM_MANIFESTINVARIANT: IntType = 2


class CMS_SCHEMA_VERSION(Enum):
    CMS_SCHEMA_VERSION_V1: IntType = 1


class CMS_SCHEMA_VERSION(Enum):
    CMS_SCHEMA_VERSION_V1: IntType = 1


class CMS_SCHEMA_VERSION(Enum):
    CMS_SCHEMA_VERSION_V1: IntType = 1


class CMS_TIME_UNIT_TYPE(Enum):
    CMS_TIME_UNIT_TYPE_HOURS: IntType = 1
    CMS_TIME_UNIT_TYPE_DAYS: IntType = 2
    CMS_TIME_UNIT_TYPE_WEEKS: IntType = 3
    CMS_TIME_UNIT_TYPE_MONTHS: IntType = 4


class CMS_TIME_UNIT_TYPE(Enum):
    CMS_TIME_UNIT_TYPE_HOURS: IntType = 1
    CMS_TIME_UNIT_TYPE_DAYS: IntType = 2
    CMS_TIME_UNIT_TYPE_WEEKS: IntType = 3
    CMS_TIME_UNIT_TYPE_MONTHS: IntType = 4


class CMS_TIME_UNIT_TYPE(Enum):
    CMS_TIME_UNIT_TYPE_HOURS: IntType = 1
    CMS_TIME_UNIT_TYPE_DAYS: IntType = 2
    CMS_TIME_UNIT_TYPE_WEEKS: IntType = 3
    CMS_TIME_UNIT_TYPE_MONTHS: IntType = 4


class CMS_USAGE_PATTERN(Enum):
    CMS_USAGE_PATTERN_SCOPE_APPLICATION: IntType = 1
    CMS_USAGE_PATTERN_SCOPE_PROCESS: IntType = 2
    CMS_USAGE_PATTERN_SCOPE_MACHINE: IntType = 3
    CMS_USAGE_PATTERN_SCOPE_MASK: IntType = 7


class CMS_USAGE_PATTERN(Enum):
    CMS_USAGE_PATTERN_SCOPE_APPLICATION: IntType = 1
    CMS_USAGE_PATTERN_SCOPE_PROCESS: IntType = 2
    CMS_USAGE_PATTERN_SCOPE_MACHINE: IntType = 3
    CMS_USAGE_PATTERN_SCOPE_MASK: IntType = 7


class CMS_USAGE_PATTERN(Enum):
    CMS_USAGE_PATTERN_SCOPE_APPLICATION: IntType = 1
    CMS_USAGE_PATTERN_SCOPE_PROCESS: IntType = 2
    CMS_USAGE_PATTERN_SCOPE_MACHINE: IntType = 3
    CMS_USAGE_PATTERN_SCOPE_MASK: IntType = 7


class COMServerEntryFieldId(Enum):
    COMServer_Flags: IntType = 0
    COMServer_ConfiguredGuid: IntType = 1
    COMServer_ImplementedClsid: IntType = 2
    COMServer_TypeLibrary: IntType = 3
    COMServer_ThreadingModel: IntType = 4
    COMServer_RuntimeVersion: IntType = 5
    COMServer_HostFile: IntType = 6


class COMServerEntryFieldId(Enum):
    COMServer_Flags: IntType = 0
    COMServer_ConfiguredGuid: IntType = 1
    COMServer_ImplementedClsid: IntType = 2
    COMServer_TypeLibrary: IntType = 3
    COMServer_ThreadingModel: IntType = 4
    COMServer_RuntimeVersion: IntType = 5
    COMServer_HostFile: IntType = 6


class COMServerEntryFieldId(Enum):
    COMServer_Flags: IntType = 0
    COMServer_ConfiguredGuid: IntType = 1
    COMServer_ImplementedClsid: IntType = 2
    COMServer_TypeLibrary: IntType = 3
    COMServer_ThreadingModel: IntType = 4
    COMServer_RuntimeVersion: IntType = 5
    COMServer_HostFile: IntType = 6


class CategoryMembershipDataEntryFieldId(Enum):
    CategoryMembershipData_Xml: IntType = 0
    CategoryMembershipData_Description: IntType = 1


class CategoryMembershipDataEntryFieldId(Enum):
    CategoryMembershipData_Xml: IntType = 0
    CategoryMembershipData_Description: IntType = 1


class CategoryMembershipDataEntryFieldId(Enum):
    CategoryMembershipData_Xml: IntType = 0
    CategoryMembershipData_Description: IntType = 1


class CategoryMembershipEntryFieldId(Enum):
    CategoryMembership_SubcategoryMembership: IntType = 0


class CategoryMembershipEntryFieldId(Enum):
    CategoryMembership_SubcategoryMembership: IntType = 0


class CategoryMembershipEntryFieldId(Enum):
    CategoryMembership_SubcategoryMembership: IntType = 0


class CompatibleFrameworksMetadataEntryFieldId(Enum):
    CompatibleFrameworksMetadata_SupportUrl: IntType = 0


class CompatibleFrameworksMetadataEntryFieldId(Enum):
    CompatibleFrameworksMetadata_SupportUrl: IntType = 0


class CompatibleFrameworksMetadataEntryFieldId(Enum):
    CompatibleFrameworksMetadata_SupportUrl: IntType = 0


class DependentOSMetadataEntryFieldId(Enum):
    DependentOSMetadata_SupportUrl: IntType = 0
    DependentOSMetadata_Description: IntType = 1
    DependentOSMetadata_MajorVersion: IntType = 2
    DependentOSMetadata_MinorVersion: IntType = 3
    DependentOSMetadata_BuildNumber: IntType = 4
    DependentOSMetadata_ServicePackMajor: IntType = 5
    DependentOSMetadata_ServicePackMinor: IntType = 6


class DependentOSMetadataEntryFieldId(Enum):
    DependentOSMetadata_SupportUrl: IntType = 0
    DependentOSMetadata_Description: IntType = 1
    DependentOSMetadata_MajorVersion: IntType = 2
    DependentOSMetadata_MinorVersion: IntType = 3
    DependentOSMetadata_BuildNumber: IntType = 4
    DependentOSMetadata_ServicePackMajor: IntType = 5
    DependentOSMetadata_ServicePackMinor: IntType = 6


class DependentOSMetadataEntryFieldId(Enum):
    DependentOSMetadata_SupportUrl: IntType = 0
    DependentOSMetadata_Description: IntType = 1
    DependentOSMetadata_MajorVersion: IntType = 2
    DependentOSMetadata_MinorVersion: IntType = 3
    DependentOSMetadata_BuildNumber: IntType = 4
    DependentOSMetadata_ServicePackMajor: IntType = 5
    DependentOSMetadata_ServicePackMinor: IntType = 6


class DeploymentMetadataEntryFieldId(Enum):
    DeploymentMetadata_DeploymentProviderCodebase: IntType = 0
    DeploymentMetadata_MinimumRequiredVersion: IntType = 1
    DeploymentMetadata_MaximumAge: IntType = 2
    DeploymentMetadata_MaximumAge_Unit: IntType = 3
    DeploymentMetadata_DeploymentFlags: IntType = 4


class DeploymentMetadataEntryFieldId(Enum):
    DeploymentMetadata_DeploymentProviderCodebase: IntType = 0
    DeploymentMetadata_MinimumRequiredVersion: IntType = 1
    DeploymentMetadata_MaximumAge: IntType = 2
    DeploymentMetadata_MaximumAge_Unit: IntType = 3
    DeploymentMetadata_DeploymentFlags: IntType = 4


class DeploymentMetadataEntryFieldId(Enum):
    DeploymentMetadata_DeploymentProviderCodebase: IntType = 0
    DeploymentMetadata_MinimumRequiredVersion: IntType = 1
    DeploymentMetadata_MaximumAge: IntType = 2
    DeploymentMetadata_MaximumAge_Unit: IntType = 3
    DeploymentMetadata_DeploymentFlags: IntType = 4


class DescriptionMetadataEntryFieldId(Enum):
    DescriptionMetadata_Publisher: IntType = 0
    DescriptionMetadata_Product: IntType = 1
    DescriptionMetadata_SupportUrl: IntType = 2
    DescriptionMetadata_IconFile: IntType = 3
    DescriptionMetadata_ErrorReportUrl: IntType = 4
    DescriptionMetadata_SuiteName: IntType = 5


class DescriptionMetadataEntryFieldId(Enum):
    DescriptionMetadata_Publisher: IntType = 0
    DescriptionMetadata_Product: IntType = 1
    DescriptionMetadata_SupportUrl: IntType = 2
    DescriptionMetadata_IconFile: IntType = 3
    DescriptionMetadata_ErrorReportUrl: IntType = 4
    DescriptionMetadata_SuiteName: IntType = 5


class DescriptionMetadataEntryFieldId(Enum):
    DescriptionMetadata_Publisher: IntType = 0
    DescriptionMetadata_Product: IntType = 1
    DescriptionMetadata_SupportUrl: IntType = 2
    DescriptionMetadata_IconFile: IntType = 3
    DescriptionMetadata_ErrorReportUrl: IntType = 4
    DescriptionMetadata_SuiteName: IntType = 5


class EntryPointEntryFieldId(Enum):
    EntryPoint_CommandLine_File: IntType = 0
    EntryPoint_CommandLine_Parameters: IntType = 1
    EntryPoint_Identity: IntType = 2
    EntryPoint_Flags: IntType = 3


class EntryPointEntryFieldId(Enum):
    EntryPoint_CommandLine_File: IntType = 0
    EntryPoint_CommandLine_Parameters: IntType = 1
    EntryPoint_Identity: IntType = 2
    EntryPoint_Flags: IntType = 3


class EntryPointEntryFieldId(Enum):
    EntryPoint_CommandLine_File: IntType = 0
    EntryPoint_CommandLine_Parameters: IntType = 1
    EntryPoint_Identity: IntType = 2
    EntryPoint_Flags: IntType = 3


class FileAssociationEntryFieldId(Enum):
    FileAssociation_Description: IntType = 0
    FileAssociation_ProgID: IntType = 1
    FileAssociation_DefaultIcon: IntType = 2
    FileAssociation_Parameter: IntType = 3


class FileAssociationEntryFieldId(Enum):
    FileAssociation_Description: IntType = 0
    FileAssociation_ProgID: IntType = 1
    FileAssociation_DefaultIcon: IntType = 2
    FileAssociation_Parameter: IntType = 3


class FileAssociationEntryFieldId(Enum):
    FileAssociation_Description: IntType = 0
    FileAssociation_ProgID: IntType = 1
    FileAssociation_DefaultIcon: IntType = 2
    FileAssociation_Parameter: IntType = 3


class FileEntryFieldId(Enum):
    File_HashAlgorithm: IntType = 0
    File_LoadFrom: IntType = 1
    File_SourcePath: IntType = 2
    File_ImportPath: IntType = 3
    File_SourceName: IntType = 4
    File_Location: IntType = 5
    File_HashValue: IntType = 6
    File_HashValueSize: IntType = 7
    File_Size: IntType = 8
    File_Group: IntType = 9
    File_Flags: IntType = 10
    File_MuiMapping: IntType = 11
    File_WritableType: IntType = 12
    File_HashElements: IntType = 13


class FileEntryFieldId(Enum):
    File_HashAlgorithm: IntType = 0
    File_LoadFrom: IntType = 1
    File_SourcePath: IntType = 2
    File_ImportPath: IntType = 3
    File_SourceName: IntType = 4
    File_Location: IntType = 5
    File_HashValue: IntType = 6
    File_HashValueSize: IntType = 7
    File_Size: IntType = 8
    File_Group: IntType = 9
    File_Flags: IntType = 10
    File_MuiMapping: IntType = 11
    File_WritableType: IntType = 12
    File_HashElements: IntType = 13


class FileEntryFieldId(Enum):
    File_HashAlgorithm: IntType = 0
    File_LoadFrom: IntType = 1
    File_SourcePath: IntType = 2
    File_ImportPath: IntType = 3
    File_SourceName: IntType = 4
    File_Location: IntType = 5
    File_HashValue: IntType = 6
    File_HashValueSize: IntType = 7
    File_Size: IntType = 8
    File_Group: IntType = 9
    File_Flags: IntType = 10
    File_MuiMapping: IntType = 11
    File_WritableType: IntType = 12
    File_HashElements: IntType = 13


class HashElementEntryFieldId(Enum):
    HashElement_Transform: IntType = 0
    HashElement_TransformMetadata: IntType = 1
    HashElement_TransformMetadataSize: IntType = 2
    HashElement_DigestMethod: IntType = 3
    HashElement_DigestValue: IntType = 4
    HashElement_DigestValueSize: IntType = 5
    HashElement_Xml: IntType = 6


class HashElementEntryFieldId(Enum):
    HashElement_Transform: IntType = 0
    HashElement_TransformMetadata: IntType = 1
    HashElement_TransformMetadataSize: IntType = 2
    HashElement_DigestMethod: IntType = 3
    HashElement_DigestValue: IntType = 4
    HashElement_DigestValueSize: IntType = 5
    HashElement_Xml: IntType = 6


class HashElementEntryFieldId(Enum):
    HashElement_Transform: IntType = 0
    HashElement_TransformMetadata: IntType = 1
    HashElement_TransformMetadataSize: IntType = 2
    HashElement_DigestMethod: IntType = 3
    HashElement_DigestValue: IntType = 4
    HashElement_DigestValueSize: IntType = 5
    HashElement_Xml: IntType = 6


class MetadataSectionEntryFieldId(Enum):
    MetadataSection_SchemaVersion: IntType = 0
    MetadataSection_ManifestFlags: IntType = 1
    MetadataSection_UsagePatterns: IntType = 2
    MetadataSection_CdfIdentity: IntType = 3
    MetadataSection_LocalPath: IntType = 4
    MetadataSection_HashAlgorithm: IntType = 5
    MetadataSection_ManifestHash: IntType = 6
    MetadataSection_ManifestHashSize: IntType = 7
    MetadataSection_ContentType: IntType = 8
    MetadataSection_RuntimeImageVersion: IntType = 9
    MetadataSection_MvidValue: IntType = 10
    MetadataSection_MvidValueSize: IntType = 11
    MetadataSection_DescriptionData: IntType = 12
    MetadataSection_DeploymentData: IntType = 13
    MetadataSection_DependentOSData: IntType = 14
    MetadataSection_defaultPermissionSetID: IntType = 15
    MetadataSection_RequestedExecutionLevel: IntType = 16
    MetadataSection_RequestedExecutionLevelUIAccess: IntType = 17
    MetadataSection_ResourceTypeResourcesDependency: IntType = 18
    MetadataSection_ResourceTypeManifestResourcesDependency: IntType = 19
    MetadataSection_KeyInfoElement: IntType = 20
    MetadataSection_CompatibleFrameworksData: IntType = 21


class MetadataSectionEntryFieldId(Enum):
    MetadataSection_SchemaVersion: IntType = 0
    MetadataSection_ManifestFlags: IntType = 1
    MetadataSection_UsagePatterns: IntType = 2
    MetadataSection_CdfIdentity: IntType = 3
    MetadataSection_LocalPath: IntType = 4
    MetadataSection_HashAlgorithm: IntType = 5
    MetadataSection_ManifestHash: IntType = 6
    MetadataSection_ManifestHashSize: IntType = 7
    MetadataSection_ContentType: IntType = 8
    MetadataSection_RuntimeImageVersion: IntType = 9
    MetadataSection_MvidValue: IntType = 10
    MetadataSection_MvidValueSize: IntType = 11
    MetadataSection_DescriptionData: IntType = 12
    MetadataSection_DeploymentData: IntType = 13
    MetadataSection_DependentOSData: IntType = 14
    MetadataSection_defaultPermissionSetID: IntType = 15
    MetadataSection_RequestedExecutionLevel: IntType = 16
    MetadataSection_RequestedExecutionLevelUIAccess: IntType = 17
    MetadataSection_ResourceTypeResourcesDependency: IntType = 18
    MetadataSection_ResourceTypeManifestResourcesDependency: IntType = 19
    MetadataSection_KeyInfoElement: IntType = 20
    MetadataSection_CompatibleFrameworksData: IntType = 21


class MetadataSectionEntryFieldId(Enum):
    MetadataSection_SchemaVersion: IntType = 0
    MetadataSection_ManifestFlags: IntType = 1
    MetadataSection_UsagePatterns: IntType = 2
    MetadataSection_CdfIdentity: IntType = 3
    MetadataSection_LocalPath: IntType = 4
    MetadataSection_HashAlgorithm: IntType = 5
    MetadataSection_ManifestHash: IntType = 6
    MetadataSection_ManifestHashSize: IntType = 7
    MetadataSection_ContentType: IntType = 8
    MetadataSection_RuntimeImageVersion: IntType = 9
    MetadataSection_MvidValue: IntType = 10
    MetadataSection_MvidValueSize: IntType = 11
    MetadataSection_DescriptionData: IntType = 12
    MetadataSection_DeploymentData: IntType = 13
    MetadataSection_DependentOSData: IntType = 14
    MetadataSection_defaultPermissionSetID: IntType = 15
    MetadataSection_RequestedExecutionLevel: IntType = 16
    MetadataSection_RequestedExecutionLevelUIAccess: IntType = 17
    MetadataSection_ResourceTypeResourcesDependency: IntType = 18
    MetadataSection_ResourceTypeManifestResourcesDependency: IntType = 19
    MetadataSection_KeyInfoElement: IntType = 20
    MetadataSection_CompatibleFrameworksData: IntType = 21


class MuiResourceIdLookupMapEntryFieldId(Enum):
    MuiResourceIdLookupMap_Count: IntType = 0


class MuiResourceIdLookupMapEntryFieldId(Enum):
    MuiResourceIdLookupMap_Count: IntType = 0


class MuiResourceIdLookupMapEntryFieldId(Enum):
    MuiResourceIdLookupMap_Count: IntType = 0


class MuiResourceMapEntryFieldId(Enum):
    MuiResourceMap_ResourceTypeIdInt: IntType = 0
    MuiResourceMap_ResourceTypeIdIntSize: IntType = 1
    MuiResourceMap_ResourceTypeIdString: IntType = 2
    MuiResourceMap_ResourceTypeIdStringSize: IntType = 3


class MuiResourceMapEntryFieldId(Enum):
    MuiResourceMap_ResourceTypeIdInt: IntType = 0
    MuiResourceMap_ResourceTypeIdIntSize: IntType = 1
    MuiResourceMap_ResourceTypeIdString: IntType = 2
    MuiResourceMap_ResourceTypeIdStringSize: IntType = 3


class MuiResourceMapEntryFieldId(Enum):
    MuiResourceMap_ResourceTypeIdInt: IntType = 0
    MuiResourceMap_ResourceTypeIdIntSize: IntType = 1
    MuiResourceMap_ResourceTypeIdString: IntType = 2
    MuiResourceMap_ResourceTypeIdStringSize: IntType = 3


class MuiResourceTypeIdIntEntryFieldId(Enum):
    MuiResourceTypeIdInt_StringIds: IntType = 0
    MuiResourceTypeIdInt_StringIdsSize: IntType = 1
    MuiResourceTypeIdInt_IntegerIds: IntType = 2
    MuiResourceTypeIdInt_IntegerIdsSize: IntType = 3


class MuiResourceTypeIdIntEntryFieldId(Enum):
    MuiResourceTypeIdInt_StringIds: IntType = 0
    MuiResourceTypeIdInt_StringIdsSize: IntType = 1
    MuiResourceTypeIdInt_IntegerIds: IntType = 2
    MuiResourceTypeIdInt_IntegerIdsSize: IntType = 3


class MuiResourceTypeIdIntEntryFieldId(Enum):
    MuiResourceTypeIdInt_StringIds: IntType = 0
    MuiResourceTypeIdInt_StringIdsSize: IntType = 1
    MuiResourceTypeIdInt_IntegerIds: IntType = 2
    MuiResourceTypeIdInt_IntegerIdsSize: IntType = 3


class MuiResourceTypeIdStringEntryFieldId(Enum):
    MuiResourceTypeIdString_StringIds: IntType = 0
    MuiResourceTypeIdString_StringIdsSize: IntType = 1
    MuiResourceTypeIdString_IntegerIds: IntType = 2
    MuiResourceTypeIdString_IntegerIdsSize: IntType = 3


class MuiResourceTypeIdStringEntryFieldId(Enum):
    MuiResourceTypeIdString_StringIds: IntType = 0
    MuiResourceTypeIdString_StringIdsSize: IntType = 1
    MuiResourceTypeIdString_IntegerIds: IntType = 2
    MuiResourceTypeIdString_IntegerIdsSize: IntType = 3


class MuiResourceTypeIdStringEntryFieldId(Enum):
    MuiResourceTypeIdString_StringIds: IntType = 0
    MuiResourceTypeIdString_StringIdsSize: IntType = 1
    MuiResourceTypeIdString_IntegerIds: IntType = 2
    MuiResourceTypeIdString_IntegerIdsSize: IntType = 3


class PermissionSetEntryFieldId(Enum):
    PermissionSet_XmlSegment: IntType = 0


class PermissionSetEntryFieldId(Enum):
    PermissionSet_XmlSegment: IntType = 0


class PermissionSetEntryFieldId(Enum):
    PermissionSet_XmlSegment: IntType = 0


class ProgIdRedirectionEntryFieldId(Enum):
    ProgIdRedirection_RedirectedGuid: IntType = 0


class ProgIdRedirectionEntryFieldId(Enum):
    ProgIdRedirection_RedirectedGuid: IntType = 0


class ProgIdRedirectionEntryFieldId(Enum):
    ProgIdRedirection_RedirectedGuid: IntType = 0


class ResourceTableMappingEntryFieldId(Enum):
    ResourceTableMapping_FinalStringMapped: IntType = 0


class ResourceTableMappingEntryFieldId(Enum):
    ResourceTableMapping_FinalStringMapped: IntType = 0


class ResourceTableMappingEntryFieldId(Enum):
    ResourceTableMapping_FinalStringMapped: IntType = 0


class SubcategoryMembershipEntryFieldId(Enum):
    SubcategoryMembership_CategoryMembershipData: IntType = 0


class SubcategoryMembershipEntryFieldId(Enum):
    SubcategoryMembership_CategoryMembershipData: IntType = 0


class SubcategoryMembershipEntryFieldId(Enum):
    SubcategoryMembership_CategoryMembershipData: IntType = 0


class WindowClassEntryFieldId(Enum):
    WindowClass_HostDll: IntType = 0
    WindowClass_fVersioned: IntType = 1


class WindowClassEntryFieldId(Enum):
    WindowClass_HostDll: IntType = 0
    WindowClass_fVersioned: IntType = 1


class WindowClassEntryFieldId(Enum):
    WindowClass_HostDll: IntType = 0
    WindowClass_fVersioned: IntType = 1


# No Delegates

__all__ = [
    AssemblyReferenceDependentAssemblyEntry,
    AssemblyReferenceEntry,
    AssemblyRequestEntry,
    CLRSurrogateEntry,
    COMServerEntry,
    CategoryMembershipDataEntry,
    CategoryMembershipEntry,
    CmsUtils,
    CompatibleFrameworksMetadataEntry,
    DependentOSMetadataEntry,
    DeploymentMetadataEntry,
    DescriptionMetadataEntry,
    EntryPointEntry,
    FileAssociationEntry,
    FileEntry,
    HashElementEntry,
    MetadataSectionEntry,
    MuiResourceIdLookupMapEntry,
    MuiResourceMapEntry,
    MuiResourceTypeIdIntEntry,
    MuiResourceTypeIdStringEntry,
    PermissionSetEntry,
    ProgIdRedirectionEntry,
    ResourceTableMappingEntry,
    SubcategoryMembershipEntry,
    WindowClassEntry,
    IAssemblyReferenceDependentAssemblyEntry,
    IAssemblyReferenceEntry,
    IAssemblyRequestEntry,
    ICLRSurrogateEntry,
    ICMS,
    ICOMServerEntry,
    ICategoryMembershipDataEntry,
    ICategoryMembershipEntry,
    ICompatibleFrameworksMetadataEntry,
    IDependentOSMetadataEntry,
    IDeploymentMetadataEntry,
    IDescriptionMetadataEntry,
    IEntryPointEntry,
    IFileAssociationEntry,
    IFileEntry,
    IHashElementEntry,
    IMetadataSectionEntry,
    IMuiResourceIdLookupMapEntry,
    IMuiResourceMapEntry,
    IMuiResourceTypeIdIntEntry,
    IMuiResourceTypeIdStringEntry,
    IPermissionSetEntry,
    IProgIdRedirectionEntry,
    IResourceTableMappingEntry,
    ISubcategoryMembershipEntry,
    IWindowClassEntry,
    AssemblyReferenceDependentAssemblyEntryFieldId,
    AssemblyReferenceEntryFieldId,
    AssemblyRequestEntryFieldId,
    CLRSurrogateEntryFieldId,
    CMSSECTIONID,
    CMS_ASSEMBLY_DEPLOYMENT_FLAG,
    CMS_ASSEMBLY_REFERENCE_DEPENDENT_ASSEMBLY_FLAG,
    CMS_ASSEMBLY_REFERENCE_FLAG,
    CMS_COM_SERVER_FLAG,
    CMS_ENTRY_POINT_FLAG,
    CMS_FILE_FLAG,
    CMS_FILE_HASH_ALGORITHM,
    CMS_FILE_WRITABLE_TYPE,
    CMS_HASH_DIGESTMETHOD,
    CMS_HASH_TRANSFORM,
    CMS_SCHEMA_VERSION,
    CMS_TIME_UNIT_TYPE,
    CMS_USAGE_PATTERN,
    COMServerEntryFieldId,
    CategoryMembershipDataEntryFieldId,
    CategoryMembershipEntryFieldId,
    CompatibleFrameworksMetadataEntryFieldId,
    DependentOSMetadataEntryFieldId,
    DeploymentMetadataEntryFieldId,
    DescriptionMetadataEntryFieldId,
    EntryPointEntryFieldId,
    FileAssociationEntryFieldId,
    FileEntryFieldId,
    HashElementEntryFieldId,
    MetadataSectionEntryFieldId,
    MuiResourceIdLookupMapEntryFieldId,
    MuiResourceMapEntryFieldId,
    MuiResourceTypeIdIntEntryFieldId,
    MuiResourceTypeIdStringEntryFieldId,
    PermissionSetEntryFieldId,
    ProgIdRedirectionEntryFieldId,
    ResourceTableMappingEntryFieldId,
    SubcategoryMembershipEntryFieldId,
    WindowClassEntryFieldId,
]
