from __future__ import annotations

from abc import ABC
from typing import Callable, Generic, List, Protocol, Tuple, TypeVar, Union, overload

from System import ApplicationException, Array, AsyncCallback, Attribute, Boolean, Byte, Delegate, Enum, Exception, FormatException, Guid, IAsyncResult, ICloneable, IRuntimeFieldInfo, IRuntimeMethodInfo, Int32, Int64, IntPtr, MarshalByRefObject, ModuleHandle, MulticastDelegate, Object, ResolveEventArgs, RuntimeFieldHandle, RuntimeMethodHandle, RuntimeType, RuntimeTypeHandle, String, SystemException, Type, TypedReference, UInt32, Utf8String, ValueType, Version, Void
from System.Collections.Generic import IEnumerable, IList
from System.Collections.Immutable import ImmutableArray
from System.Configuration.Assemblies import AssemblyHashAlgorithm, AssemblyVersionCompatibility
from System.Globalization import CultureInfo
from System.IO import FileStream, Stream
from System.Runtime.InteropServices import ICustomQueryInterface, _Assembly, _AssemblyName, _Attribute, _ConstructorInfo, _EventInfo, _Exception, _FieldInfo, _MemberInfo, _MethodBase, _MethodInfo, _Module, _ParameterInfo, _PropertyInfo, _Type
from System.Runtime.Serialization import IDeserializationCallback, IObjectReference, ISerializable, SerializationInfo, StreamingContext
from System.Security import IEvidenceFactory, PermissionSet, SecurityContextSource, SecurityRuleSet
from System.Security.Cryptography.X509Certificates import X509Certificate
from System.Security.Policy import Evidence

# ---------- Types ---------- #

K = TypeVar('K')
T = TypeVar('T')
V = TypeVar('V')

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
ByteType = Union[int, Byte]
IntType = Union[int, Int32]
LongType = Union[int, Int64]
NIntType = Union[int, IntPtr]
ObjectType = Object
StringType = Union[str, String]
TypeType = Union[type, Type]
UIntType = Union[int, UInt32]
VoidType = Union[None, Void]


class EventType(Generic[T]):
    def __iadd__(self, other: T): ...
    
    def __isub__(self, other: T): ...



# ---------- Classes ---------- #

class AmbiguousMatchException(SystemException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, inner: Exception): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Assembly(ABC, ObjectType, _Assembly, IEvidenceFactory, ICustomAttributeProvider, ISerializable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def CodeBase(self) -> StringType: ...
    
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]: ...
    
    @property
    def DefinedTypes(self) -> IEnumerable[TypeInfo]: ...
    
    @property
    def EntryPoint(self) -> MethodInfo: ...
    
    @property
    def EscapedCodeBase(self) -> StringType: ...
    
    @property
    def Evidence(self) -> Evidence: ...
    
    @property
    def ExportedTypes(self) -> IEnumerable[TypeType]: ...
    
    @property
    def FullName(self) -> StringType: ...
    
    @property
    def GlobalAssemblyCache(self) -> BooleanType: ...
    
    @property
    def HostContext(self) -> LongType: ...
    
    @property
    def ImageRuntimeVersion(self) -> StringType: ...
    
    @property
    def IsDynamic(self) -> BooleanType: ...
    
    @property
    def IsFullyTrusted(self) -> BooleanType: ...
    
    @property
    def Location(self) -> StringType: ...
    
    @property
    def ManifestModule(self) -> Module: ...
    
    @property
    def Modules(self) -> IEnumerable[Module]: ...
    
    @property
    def PermissionSet(self) -> PermissionSet: ...
    
    @property
    def ReflectionOnly(self) -> BooleanType: ...
    
    @property
    def SecurityRuleSet(self) -> SecurityRuleSet: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def CreateInstance(self, typeName: StringType) -> ObjectType: ...
    
    @overload
    def CreateInstance(self, typeName: StringType, ignoreCase: BooleanType) -> ObjectType: ...
    
    @overload
    def CreateInstance(self, typeName: StringType, ignoreCase: BooleanType, bindingAttr: BindingFlags, binder: Binder, args: ArrayType[ObjectType], culture: CultureInfo, activationAttributes: ArrayType[ObjectType]) -> ObjectType: ...
    
    @staticmethod
    def CreateQualifiedName(assemblyName: StringType, typeName: StringType) -> StringType: ...
    
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    @staticmethod
    def GetAssembly(type: TypeType) -> Assembly: ...
    
    @staticmethod
    def GetCallingAssembly() -> Assembly: ...
    
    @overload
    def GetCustomAttributes(self, inherit: BooleanType) -> ArrayType[ObjectType]: ...
    
    @overload
    def GetCustomAttributes(self, attributeType: TypeType, inherit: BooleanType) -> ArrayType[ObjectType]: ...
    
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]: ...
    
    @staticmethod
    def GetEntryAssembly() -> Assembly: ...
    
    @staticmethod
    def GetExecutingAssembly() -> Assembly: ...
    
    def GetExportedTypes(self) -> ArrayType[TypeType]: ...
    
    def GetFile(self, name: StringType) -> FileStream: ...
    
    @overload
    def GetFiles(self) -> ArrayType[FileStream]: ...
    
    @overload
    def GetFiles(self, getResourceModules: BooleanType) -> ArrayType[FileStream]: ...
    
    def GetHashCode(self) -> IntType: ...
    
    @overload
    def GetLoadedModules(self) -> ArrayType[Module]: ...
    
    @overload
    def GetLoadedModules(self, getResourceModules: BooleanType) -> ArrayType[Module]: ...
    
    def GetManifestResourceInfo(self, resourceName: StringType) -> ManifestResourceInfo: ...
    
    def GetManifestResourceNames(self) -> ArrayType[StringType]: ...
    
    @overload
    def GetManifestResourceStream(self, type: TypeType, name: StringType) -> Stream: ...
    
    @overload
    def GetManifestResourceStream(self, name: StringType) -> Stream: ...
    
    def GetModule(self, name: StringType) -> Module: ...
    
    @overload
    def GetModules(self) -> ArrayType[Module]: ...
    
    @overload
    def GetModules(self, getResourceModules: BooleanType) -> ArrayType[Module]: ...
    
    @overload
    def GetName(self) -> AssemblyName: ...
    
    @overload
    def GetName(self, copiedName: BooleanType) -> AssemblyName: ...
    
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    
    def GetReferencedAssemblies(self) -> ArrayType[AssemblyName]: ...
    
    @overload
    def GetSatelliteAssembly(self, culture: CultureInfo) -> Assembly: ...
    
    @overload
    def GetSatelliteAssembly(self, culture: CultureInfo, version: Version) -> Assembly: ...
    
    @overload
    def GetType(self, name: StringType) -> TypeType: ...
    
    @overload
    def GetType(self, name: StringType, throwOnError: BooleanType) -> TypeType: ...
    
    @overload
    def GetType(self, name: StringType, throwOnError: BooleanType, ignoreCase: BooleanType) -> TypeType: ...
    
    def GetTypes(self) -> ArrayType[TypeType]: ...
    
    def IsDefined(self, attributeType: TypeType, inherit: BooleanType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def Load(assemblyString: StringType) -> Assembly: ...
    
    @staticmethod
    @overload
    def Load(assemblyString: StringType, assemblySecurity: Evidence) -> Assembly: ...
    
    @staticmethod
    @overload
    def Load(assemblyRef: AssemblyName) -> Assembly: ...
    
    @staticmethod
    @overload
    def Load(assemblyRef: AssemblyName, assemblySecurity: Evidence) -> Assembly: ...
    
    @staticmethod
    @overload
    def Load(rawAssembly: ArrayType[ByteType]) -> Assembly: ...
    
    @staticmethod
    @overload
    def Load(rawAssembly: ArrayType[ByteType], rawSymbolStore: ArrayType[ByteType]) -> Assembly: ...
    
    @staticmethod
    @overload
    def Load(rawAssembly: ArrayType[ByteType], rawSymbolStore: ArrayType[ByteType], securityContextSource: SecurityContextSource) -> Assembly: ...
    
    @staticmethod
    @overload
    def Load(rawAssembly: ArrayType[ByteType], rawSymbolStore: ArrayType[ByteType], securityEvidence: Evidence) -> Assembly: ...
    
    @staticmethod
    @overload
    def LoadFile(path: StringType) -> Assembly: ...
    
    @staticmethod
    @overload
    def LoadFile(path: StringType, securityEvidence: Evidence) -> Assembly: ...
    
    @staticmethod
    @overload
    def LoadFrom(assemblyFile: StringType) -> Assembly: ...
    
    @staticmethod
    @overload
    def LoadFrom(assemblyFile: StringType, securityEvidence: Evidence) -> Assembly: ...
    
    @staticmethod
    @overload
    def LoadFrom(assemblyFile: StringType, securityEvidence: Evidence, hashValue: ArrayType[ByteType], hashAlgorithm: AssemblyHashAlgorithm) -> Assembly: ...
    
    @staticmethod
    @overload
    def LoadFrom(assemblyFile: StringType, hashValue: ArrayType[ByteType], hashAlgorithm: AssemblyHashAlgorithm) -> Assembly: ...
    
    @overload
    def LoadModule(self, moduleName: StringType, rawModule: ArrayType[ByteType]) -> Module: ...
    
    @overload
    def LoadModule(self, moduleName: StringType, rawModule: ArrayType[ByteType], rawSymbolStore: ArrayType[ByteType]) -> Module: ...
    
    @staticmethod
    @overload
    def LoadWithPartialName(partialName: StringType) -> Assembly: ...
    
    @staticmethod
    @overload
    def LoadWithPartialName(partialName: StringType, securityEvidence: Evidence) -> Assembly: ...
    
    @staticmethod
    @overload
    def ReflectionOnlyLoad(assemblyString: StringType) -> Assembly: ...
    
    @staticmethod
    @overload
    def ReflectionOnlyLoad(rawAssembly: ArrayType[ByteType]) -> Assembly: ...
    
    @staticmethod
    def ReflectionOnlyLoadFrom(assemblyFile: StringType) -> Assembly: ...
    
    def ToString(self) -> StringType: ...
    
    @staticmethod
    def UnsafeLoadFrom(assemblyFile: StringType) -> Assembly: ...
    
    def add_ModuleResolve(self, value: ModuleResolveEventHandler) -> VoidType: ...
    
    def get_CodeBase(self) -> StringType: ...
    
    def get_CustomAttributes(self) -> IEnumerable[CustomAttributeData]: ...
    
    def get_DefinedTypes(self) -> IEnumerable[TypeInfo]: ...
    
    def get_EntryPoint(self) -> MethodInfo: ...
    
    def get_EscapedCodeBase(self) -> StringType: ...
    
    def get_Evidence(self) -> Evidence: ...
    
    def get_ExportedTypes(self) -> IEnumerable[TypeType]: ...
    
    def get_FullName(self) -> StringType: ...
    
    def get_GlobalAssemblyCache(self) -> BooleanType: ...
    
    def get_HostContext(self) -> LongType: ...
    
    def get_ImageRuntimeVersion(self) -> StringType: ...
    
    def get_IsDynamic(self) -> BooleanType: ...
    
    def get_IsFullyTrusted(self) -> BooleanType: ...
    
    def get_Location(self) -> StringType: ...
    
    def get_ManifestModule(self) -> Module: ...
    
    def get_Modules(self) -> IEnumerable[Module]: ...
    
    def get_PermissionSet(self) -> PermissionSet: ...
    
    def get_ReflectionOnly(self) -> BooleanType: ...
    
    def get_SecurityRuleSet(self) -> SecurityRuleSet: ...
    
    @staticmethod
    def op_Equality(left: Assembly, right: Assembly) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(left: Assembly, right: Assembly) -> BooleanType: ...
    
    def remove_ModuleResolve(self, value: ModuleResolveEventHandler) -> VoidType: ...
    
    # ---------- Events ---------- #
    
    ModuleResolve: EventType[ModuleResolveEventHandler] = ...
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AssemblyAlgorithmIdAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, algorithmId: AssemblyHashAlgorithm): ...
    
    @overload
    def __init__(self, algorithmId: UIntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AlgorithmId(self) -> UIntType: ...
    
    # ---------- Methods ---------- #
    
    def get_AlgorithmId(self) -> UIntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AssemblyCompanyAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, company: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Company(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_Company(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AssemblyConfigurationAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, configuration: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Configuration(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_Configuration(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AssemblyCopyrightAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, copyright: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Copyright(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_Copyright(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AssemblyCultureAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, culture: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Culture(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_Culture(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AssemblyDefaultAliasAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, defaultAlias: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def DefaultAlias(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_DefaultAlias(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AssemblyDelaySignAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, delaySign: BooleanType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def DelaySign(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def get_DelaySign(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AssemblyDescriptionAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, description: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Description(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_Description(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AssemblyFileVersionAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, version: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Version(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_Version(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AssemblyFlagsAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, flags: UIntType): ...
    
    @overload
    def __init__(self, assemblyFlags: IntType): ...
    
    @overload
    def __init__(self, assemblyFlags: AssemblyNameFlags): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AssemblyFlags(self) -> IntType: ...
    
    @property
    def Flags(self) -> UIntType: ...
    
    # ---------- Methods ---------- #
    
    def get_AssemblyFlags(self) -> IntType: ...
    
    def get_Flags(self) -> UIntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AssemblyInformationalVersionAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, informationalVersion: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def InformationalVersion(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_InformationalVersion(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AssemblyKeyFileAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, keyFile: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def KeyFile(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_KeyFile(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AssemblyKeyNameAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, keyName: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def KeyName(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_KeyName(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AssemblyMetadataAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, key: StringType, value: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Key(self) -> StringType: ...
    
    @property
    def Value(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_Key(self) -> StringType: ...
    
    def get_Value(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AssemblyName(ObjectType, _AssemblyName, ICloneable, ISerializable, IDeserializationCallback):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, assemblyName: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CodeBase(self) -> StringType: ...
    
    @CodeBase.setter
    def CodeBase(self, value: StringType) -> None: ...
    
    @property
    def ContentType(self) -> AssemblyContentType: ...
    
    @ContentType.setter
    def ContentType(self, value: AssemblyContentType) -> None: ...
    
    @property
    def CultureInfo(self) -> CultureInfo: ...
    
    @CultureInfo.setter
    def CultureInfo(self, value: CultureInfo) -> None: ...
    
    @property
    def CultureName(self) -> StringType: ...
    
    @CultureName.setter
    def CultureName(self, value: StringType) -> None: ...
    
    @property
    def EscapedCodeBase(self) -> StringType: ...
    
    @property
    def Flags(self) -> AssemblyNameFlags: ...
    
    @Flags.setter
    def Flags(self, value: AssemblyNameFlags) -> None: ...
    
    @property
    def FullName(self) -> StringType: ...
    
    @property
    def HashAlgorithm(self) -> AssemblyHashAlgorithm: ...
    
    @HashAlgorithm.setter
    def HashAlgorithm(self, value: AssemblyHashAlgorithm) -> None: ...
    
    @property
    def KeyPair(self) -> StrongNameKeyPair: ...
    
    @KeyPair.setter
    def KeyPair(self, value: StrongNameKeyPair) -> None: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @Name.setter
    def Name(self, value: StringType) -> None: ...
    
    @property
    def ProcessorArchitecture(self) -> ProcessorArchitecture: ...
    
    @ProcessorArchitecture.setter
    def ProcessorArchitecture(self, value: ProcessorArchitecture) -> None: ...
    
    @property
    def Version(self) -> Version: ...
    
    @Version.setter
    def Version(self, value: Version) -> None: ...
    
    @property
    def VersionCompatibility(self) -> AssemblyVersionCompatibility: ...
    
    @VersionCompatibility.setter
    def VersionCompatibility(self, value: AssemblyVersionCompatibility) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> ObjectType: ...
    
    @staticmethod
    def GetAssemblyName(assemblyFile: StringType) -> AssemblyName: ...
    
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    
    def GetPublicKey(self) -> ArrayType[ByteType]: ...
    
    def GetPublicKeyToken(self) -> ArrayType[ByteType]: ...
    
    def OnDeserialization(self, sender: ObjectType) -> VoidType: ...
    
    @staticmethod
    def ReferenceMatchesDefinition(reference: AssemblyName, definition: AssemblyName) -> BooleanType: ...
    
    def SetPublicKey(self, publicKey: ArrayType[ByteType]) -> VoidType: ...
    
    def SetPublicKeyToken(self, publicKeyToken: ArrayType[ByteType]) -> VoidType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_CodeBase(self) -> StringType: ...
    
    def get_ContentType(self) -> AssemblyContentType: ...
    
    def get_CultureInfo(self) -> CultureInfo: ...
    
    def get_CultureName(self) -> StringType: ...
    
    def get_EscapedCodeBase(self) -> StringType: ...
    
    def get_Flags(self) -> AssemblyNameFlags: ...
    
    def get_FullName(self) -> StringType: ...
    
    def get_HashAlgorithm(self) -> AssemblyHashAlgorithm: ...
    
    def get_KeyPair(self) -> StrongNameKeyPair: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_ProcessorArchitecture(self) -> ProcessorArchitecture: ...
    
    def get_Version(self) -> Version: ...
    
    def get_VersionCompatibility(self) -> AssemblyVersionCompatibility: ...
    
    def set_CodeBase(self, value: StringType) -> VoidType: ...
    
    def set_ContentType(self, value: AssemblyContentType) -> VoidType: ...
    
    def set_CultureInfo(self, value: CultureInfo) -> VoidType: ...
    
    def set_CultureName(self, value: StringType) -> VoidType: ...
    
    def set_Flags(self, value: AssemblyNameFlags) -> VoidType: ...
    
    def set_HashAlgorithm(self, value: AssemblyHashAlgorithm) -> VoidType: ...
    
    def set_KeyPair(self, value: StrongNameKeyPair) -> VoidType: ...
    
    def set_Name(self, value: StringType) -> VoidType: ...
    
    def set_ProcessorArchitecture(self, value: ProcessorArchitecture) -> VoidType: ...
    
    def set_Version(self, value: Version) -> VoidType: ...
    
    def set_VersionCompatibility(self, value: AssemblyVersionCompatibility) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AssemblyNameProxy(MarshalByRefObject):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetAssemblyName(self, assemblyFile: StringType) -> AssemblyName: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AssemblyProductAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, product: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Product(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_Product(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AssemblySignatureKeyAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, publicKey: StringType, countersignature: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Countersignature(self) -> StringType: ...
    
    @property
    def PublicKey(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_Countersignature(self) -> StringType: ...
    
    def get_PublicKey(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AssemblyTitleAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, title: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Title(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_Title(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AssemblyTrademarkAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, trademark: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Trademark(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_Trademark(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AssemblyVersionAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, version: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Version(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_Version(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Associates(ABC, ObjectType):
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


class Binder(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BindToField(self, bindingAttr: BindingFlags, match: ArrayType[FieldInfo], value: ObjectType, culture: CultureInfo) -> FieldInfo: ...
    
    def BindToMethod(self, bindingAttr: BindingFlags, match: ArrayType[MethodBase], args: ObjectType, modifiers: ArrayType[ParameterModifier], culture: CultureInfo, names: ArrayType[StringType], state: ObjectType) -> Tuple[MethodBase, ObjectType, ObjectType]: ...
    
    def ChangeType(self, value: ObjectType, type: TypeType, culture: CultureInfo) -> ObjectType: ...
    
    def ReorderArgumentArray(self, args: ObjectType, state: ObjectType) -> Tuple[VoidType, ObjectType]: ...
    
    def SelectMethod(self, bindingAttr: BindingFlags, match: ArrayType[MethodBase], types: ArrayType[TypeType], modifiers: ArrayType[ParameterModifier]) -> MethodBase: ...
    
    def SelectProperty(self, bindingAttr: BindingFlags, match: ArrayType[PropertyInfo], returnType: TypeType, indexes: ArrayType[TypeType], modifiers: ArrayType[ParameterModifier]) -> PropertyInfo: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class BlobUtilities(ABC, ObjectType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def SizeOfGuid() -> IntType: ...
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def ReadBytes(buffer: ByteType, byteCount: IntType) -> ArrayType[ByteType]: ...
    
    @staticmethod
    def ReadImmutableBytes(buffer: ByteType, byteCount: IntType) -> ImmutableArray[ByteType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ConstructorInfo(ABC, MethodBase, ICustomAttributeProvider, _MemberInfo, _MethodBase, _ConstructorInfo):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def ConstructorName() -> StringType: ...
    
    @staticmethod
    @property
    def TypeConstructorName() -> StringType: ...
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def MemberType(self) -> MemberTypes: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    @overload
    def Invoke(self, parameters: ArrayType[ObjectType]) -> ObjectType: ...
    
    @overload
    def Invoke(self, invokeAttr: BindingFlags, binder: Binder, parameters: ArrayType[ObjectType], culture: CultureInfo) -> ObjectType: ...
    
    def get_MemberType(self) -> MemberTypes: ...
    
    @staticmethod
    def op_Equality(left: ConstructorInfo, right: ConstructorInfo) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(left: ConstructorInfo, right: ConstructorInfo) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CustomAttribute(ABC, ObjectType):
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


class CustomAttributeData(ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def AttributeType(self) -> TypeType: ...
    
    @property
    def Constructor(self) -> ConstructorInfo: ...
    
    @property
    def ConstructorArguments(self) -> IList[CustomAttributeTypedArgument]: ...
    
    @property
    def NamedArguments(self) -> IList[CustomAttributeNamedArgument]: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def GetCustomAttributes(target: MemberInfo) -> IList[CustomAttributeData]: ...
    
    @staticmethod
    @overload
    def GetCustomAttributes(target: Module) -> IList[CustomAttributeData]: ...
    
    @staticmethod
    @overload
    def GetCustomAttributes(target: Assembly) -> IList[CustomAttributeData]: ...
    
    @staticmethod
    @overload
    def GetCustomAttributes(target: ParameterInfo) -> IList[CustomAttributeData]: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_AttributeType(self) -> TypeType: ...
    
    def get_Constructor(self) -> ConstructorInfo: ...
    
    def get_ConstructorArguments(self) -> IList[CustomAttributeTypedArgument]: ...
    
    def get_NamedArguments(self) -> IList[CustomAttributeNamedArgument]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CustomAttributeExtensions(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    @overload
    def GetCustomAttribute(element: Assembly, attributeType: TypeType) -> Attribute: ...
    
    @staticmethod
    @overload
    def GetCustomAttribute(element: Module, attributeType: TypeType) -> Attribute: ...
    
    @staticmethod
    @overload
    def GetCustomAttribute(element: MemberInfo, attributeType: TypeType) -> Attribute: ...
    
    @staticmethod
    @overload
    def GetCustomAttribute(element: ParameterInfo, attributeType: TypeType) -> Attribute: ...
    
    @staticmethod
    @overload
    def GetCustomAttribute(element: MemberInfo, attributeType: TypeType, inherit: BooleanType) -> Attribute: ...
    
    @staticmethod
    @overload
    def GetCustomAttribute(element: ParameterInfo, attributeType: TypeType, inherit: BooleanType) -> Attribute: ...
    
    @staticmethod
    @overload
    def GetCustomAttribute(element: Assembly) -> T: ...
    
    @staticmethod
    @overload
    def GetCustomAttribute(element: Module) -> T: ...
    
    @staticmethod
    @overload
    def GetCustomAttribute(element: MemberInfo) -> T: ...
    
    @staticmethod
    @overload
    def GetCustomAttribute(element: ParameterInfo) -> T: ...
    
    @staticmethod
    @overload
    def GetCustomAttribute(element: MemberInfo, inherit: BooleanType) -> T: ...
    
    @staticmethod
    @overload
    def GetCustomAttribute(element: ParameterInfo, inherit: BooleanType) -> T: ...
    
    @staticmethod
    @overload
    def GetCustomAttributes(element: Assembly) -> IEnumerable[Attribute]: ...
    
    @staticmethod
    @overload
    def GetCustomAttributes(element: Module) -> IEnumerable[Attribute]: ...
    
    @staticmethod
    @overload
    def GetCustomAttributes(element: MemberInfo) -> IEnumerable[Attribute]: ...
    
    @staticmethod
    @overload
    def GetCustomAttributes(element: ParameterInfo) -> IEnumerable[Attribute]: ...
    
    @staticmethod
    @overload
    def GetCustomAttributes(element: MemberInfo, inherit: BooleanType) -> IEnumerable[Attribute]: ...
    
    @staticmethod
    @overload
    def GetCustomAttributes(element: ParameterInfo, inherit: BooleanType) -> IEnumerable[Attribute]: ...
    
    @staticmethod
    @overload
    def GetCustomAttributes(element: Assembly, attributeType: TypeType) -> IEnumerable[Attribute]: ...
    
    @staticmethod
    @overload
    def GetCustomAttributes(element: Module, attributeType: TypeType) -> IEnumerable[Attribute]: ...
    
    @staticmethod
    @overload
    def GetCustomAttributes(element: MemberInfo, attributeType: TypeType) -> IEnumerable[Attribute]: ...
    
    @staticmethod
    @overload
    def GetCustomAttributes(element: ParameterInfo, attributeType: TypeType) -> IEnumerable[Attribute]: ...
    
    @staticmethod
    @overload
    def GetCustomAttributes(element: MemberInfo, attributeType: TypeType, inherit: BooleanType) -> IEnumerable[Attribute]: ...
    
    @staticmethod
    @overload
    def GetCustomAttributes(element: ParameterInfo, attributeType: TypeType, inherit: BooleanType) -> IEnumerable[Attribute]: ...
    
    @staticmethod
    @overload
    def GetCustomAttributes(element: Assembly) -> IEnumerable[T]: ...
    
    @staticmethod
    @overload
    def GetCustomAttributes(element: Module) -> IEnumerable[T]: ...
    
    @staticmethod
    @overload
    def GetCustomAttributes(element: MemberInfo) -> IEnumerable[T]: ...
    
    @staticmethod
    @overload
    def GetCustomAttributes(element: ParameterInfo) -> IEnumerable[T]: ...
    
    @staticmethod
    @overload
    def GetCustomAttributes(element: MemberInfo, inherit: BooleanType) -> IEnumerable[T]: ...
    
    @staticmethod
    @overload
    def GetCustomAttributes(element: ParameterInfo, inherit: BooleanType) -> IEnumerable[T]: ...
    
    @staticmethod
    @overload
    def IsDefined(element: Assembly, attributeType: TypeType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def IsDefined(element: Module, attributeType: TypeType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def IsDefined(element: MemberInfo, attributeType: TypeType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def IsDefined(element: ParameterInfo, attributeType: TypeType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def IsDefined(element: MemberInfo, attributeType: TypeType, inherit: BooleanType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def IsDefined(element: ParameterInfo, attributeType: TypeType, inherit: BooleanType) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CustomAttributeFormatException(FormatException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, inner: Exception): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DefaultMemberAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, memberName: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def MemberName(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_MemberName(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EventInfo(ABC, MemberInfo, ICustomAttributeProvider, _MemberInfo, _EventInfo):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def AddMethod(self) -> MethodInfo: ...
    
    @property
    def Attributes(self) -> EventAttributes: ...
    
    @property
    def EventHandlerType(self) -> TypeType: ...
    
    @property
    def IsMulticast(self) -> BooleanType: ...
    
    @property
    def IsSpecialName(self) -> BooleanType: ...
    
    @property
    def MemberType(self) -> MemberTypes: ...
    
    @property
    def RaiseMethod(self) -> MethodInfo: ...
    
    @property
    def RemoveMethod(self) -> MethodInfo: ...
    
    # ---------- Methods ---------- #
    
    def AddEventHandler(self, target: ObjectType, handler: Delegate) -> VoidType: ...
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @overload
    def GetAddMethod(self) -> MethodInfo: ...
    
    @overload
    def GetAddMethod(self, nonPublic: BooleanType) -> MethodInfo: ...
    
    def GetHashCode(self) -> IntType: ...
    
    @overload
    def GetOtherMethods(self, nonPublic: BooleanType) -> ArrayType[MethodInfo]: ...
    
    @overload
    def GetOtherMethods(self) -> ArrayType[MethodInfo]: ...
    
    @overload
    def GetRaiseMethod(self) -> MethodInfo: ...
    
    @overload
    def GetRaiseMethod(self, nonPublic: BooleanType) -> MethodInfo: ...
    
    @overload
    def GetRemoveMethod(self) -> MethodInfo: ...
    
    @overload
    def GetRemoveMethod(self, nonPublic: BooleanType) -> MethodInfo: ...
    
    def RemoveEventHandler(self, target: ObjectType, handler: Delegate) -> VoidType: ...
    
    def get_AddMethod(self) -> MethodInfo: ...
    
    def get_Attributes(self) -> EventAttributes: ...
    
    def get_EventHandlerType(self) -> TypeType: ...
    
    def get_IsMulticast(self) -> BooleanType: ...
    
    def get_IsSpecialName(self) -> BooleanType: ...
    
    def get_MemberType(self) -> MemberTypes: ...
    
    def get_RaiseMethod(self) -> MethodInfo: ...
    
    def get_RemoveMethod(self) -> MethodInfo: ...
    
    @staticmethod
    def op_Equality(left: EventInfo, right: EventInfo) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(left: EventInfo, right: EventInfo) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ExceptionHandlingClause(ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def CatchType(self) -> TypeType: ...
    
    @property
    def FilterOffset(self) -> IntType: ...
    
    @property
    def Flags(self) -> ExceptionHandlingClauseOptions: ...
    
    @property
    def HandlerLength(self) -> IntType: ...
    
    @property
    def HandlerOffset(self) -> IntType: ...
    
    @property
    def TryLength(self) -> IntType: ...
    
    @property
    def TryOffset(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def ToString(self) -> StringType: ...
    
    def get_CatchType(self) -> TypeType: ...
    
    def get_FilterOffset(self) -> IntType: ...
    
    def get_Flags(self) -> ExceptionHandlingClauseOptions: ...
    
    def get_HandlerLength(self) -> IntType: ...
    
    def get_HandlerOffset(self) -> IntType: ...
    
    def get_TryLength(self) -> IntType: ...
    
    def get_TryOffset(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class FieldInfo(ABC, MemberInfo, ICustomAttributeProvider, _MemberInfo, _FieldInfo):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Attributes(self) -> FieldAttributes: ...
    
    @property
    def FieldHandle(self) -> RuntimeFieldHandle: ...
    
    @property
    def FieldType(self) -> TypeType: ...
    
    @property
    def IsAssembly(self) -> BooleanType: ...
    
    @property
    def IsFamily(self) -> BooleanType: ...
    
    @property
    def IsFamilyAndAssembly(self) -> BooleanType: ...
    
    @property
    def IsFamilyOrAssembly(self) -> BooleanType: ...
    
    @property
    def IsInitOnly(self) -> BooleanType: ...
    
    @property
    def IsLiteral(self) -> BooleanType: ...
    
    @property
    def IsNotSerialized(self) -> BooleanType: ...
    
    @property
    def IsPinvokeImpl(self) -> BooleanType: ...
    
    @property
    def IsPrivate(self) -> BooleanType: ...
    
    @property
    def IsPublic(self) -> BooleanType: ...
    
    @property
    def IsSecurityCritical(self) -> BooleanType: ...
    
    @property
    def IsSecuritySafeCritical(self) -> BooleanType: ...
    
    @property
    def IsSecurityTransparent(self) -> BooleanType: ...
    
    @property
    def IsSpecialName(self) -> BooleanType: ...
    
    @property
    def IsStatic(self) -> BooleanType: ...
    
    @property
    def MemberType(self) -> MemberTypes: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def GetFieldFromHandle(handle: RuntimeFieldHandle) -> FieldInfo: ...
    
    @staticmethod
    @overload
    def GetFieldFromHandle(handle: RuntimeFieldHandle, declaringType: RuntimeTypeHandle) -> FieldInfo: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def GetOptionalCustomModifiers(self) -> ArrayType[TypeType]: ...
    
    def GetRawConstantValue(self) -> ObjectType: ...
    
    def GetRequiredCustomModifiers(self) -> ArrayType[TypeType]: ...
    
    def GetValue(self, obj: ObjectType) -> ObjectType: ...
    
    def GetValueDirect(self, obj: TypedReference) -> ObjectType: ...
    
    @overload
    def SetValue(self, obj: ObjectType, value: ObjectType) -> VoidType: ...
    
    @overload
    def SetValue(self, obj: ObjectType, value: ObjectType, invokeAttr: BindingFlags, binder: Binder, culture: CultureInfo) -> VoidType: ...
    
    def SetValueDirect(self, obj: TypedReference, value: ObjectType) -> VoidType: ...
    
    def get_Attributes(self) -> FieldAttributes: ...
    
    def get_FieldHandle(self) -> RuntimeFieldHandle: ...
    
    def get_FieldType(self) -> TypeType: ...
    
    def get_IsAssembly(self) -> BooleanType: ...
    
    def get_IsFamily(self) -> BooleanType: ...
    
    def get_IsFamilyAndAssembly(self) -> BooleanType: ...
    
    def get_IsFamilyOrAssembly(self) -> BooleanType: ...
    
    def get_IsInitOnly(self) -> BooleanType: ...
    
    def get_IsLiteral(self) -> BooleanType: ...
    
    def get_IsNotSerialized(self) -> BooleanType: ...
    
    def get_IsPinvokeImpl(self) -> BooleanType: ...
    
    def get_IsPrivate(self) -> BooleanType: ...
    
    def get_IsPublic(self) -> BooleanType: ...
    
    def get_IsSecurityCritical(self) -> BooleanType: ...
    
    def get_IsSecuritySafeCritical(self) -> BooleanType: ...
    
    def get_IsSecurityTransparent(self) -> BooleanType: ...
    
    def get_IsSpecialName(self) -> BooleanType: ...
    
    def get_IsStatic(self) -> BooleanType: ...
    
    def get_MemberType(self) -> MemberTypes: ...
    
    @staticmethod
    def op_Equality(left: FieldInfo, right: FieldInfo) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(left: FieldInfo, right: FieldInfo) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IntrospectionExtensions(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def GetTypeInfo(type: TypeType) -> TypeInfo: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class InvalidFilterCriteriaException(ApplicationException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, inner: Exception): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class LoaderAllocator(ObjectType):
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


class LoaderAllocatorScout(ObjectType):
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


class LocalVariableInfo(ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def IsPinned(self) -> BooleanType: ...
    
    @property
    def LocalIndex(self) -> IntType: ...
    
    @property
    def LocalType(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def ToString(self) -> StringType: ...
    
    def get_IsPinned(self) -> BooleanType: ...
    
    def get_LocalIndex(self) -> IntType: ...
    
    def get_LocalType(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ManifestResourceInfo(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, containingAssembly: Assembly, containingFileName: StringType, resourceLocation: ResourceLocation): ...
    
    # ---------- Properties ---------- #
    
    @property
    def FileName(self) -> StringType: ...
    
    @property
    def ReferencedAssembly(self) -> Assembly: ...
    
    @property
    def ResourceLocation(self) -> ResourceLocation: ...
    
    # ---------- Methods ---------- #
    
    def get_FileName(self) -> StringType: ...
    
    def get_ReferencedAssembly(self) -> Assembly: ...
    
    def get_ResourceLocation(self) -> ResourceLocation: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MdConstant(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def GetValue(scope: MetadataImport, token: IntType, fieldTypeHandle: RuntimeTypeHandle, raw: BooleanType) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MdFieldInfo(RuntimeFieldInfo, ICustomAttributeProvider, _MemberInfo, _FieldInfo, ISerializable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Attributes(self) -> FieldAttributes: ...
    
    @property
    def FieldHandle(self) -> RuntimeFieldHandle: ...
    
    @property
    def FieldType(self) -> TypeType: ...
    
    @property
    def IsSecurityCritical(self) -> BooleanType: ...
    
    @property
    def IsSecuritySafeCritical(self) -> BooleanType: ...
    
    @property
    def IsSecurityTransparent(self) -> BooleanType: ...
    
    @property
    def MetadataToken(self) -> IntType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetOptionalCustomModifiers(self) -> ArrayType[TypeType]: ...
    
    def GetRawConstantValue(self) -> ObjectType: ...
    
    def GetRequiredCustomModifiers(self) -> ArrayType[TypeType]: ...
    
    def GetValue(self, obj: ObjectType) -> ObjectType: ...
    
    def GetValueDirect(self, obj: TypedReference) -> ObjectType: ...
    
    @overload
    def SetValue(self, obj: ObjectType, value: ObjectType, invokeAttr: BindingFlags, binder: Binder, culture: CultureInfo) -> VoidType: ...
    
    def SetValueDirect(self, obj: TypedReference, value: ObjectType) -> VoidType: ...
    
    def get_Attributes(self) -> FieldAttributes: ...
    
    def get_FieldHandle(self) -> RuntimeFieldHandle: ...
    
    def get_FieldType(self) -> TypeType: ...
    
    def get_IsSecurityCritical(self) -> BooleanType: ...
    
    def get_IsSecuritySafeCritical(self) -> BooleanType: ...
    
    def get_IsSecurityTransparent(self) -> BooleanType: ...
    
    def get_MetadataToken(self) -> IntType: ...
    
    def get_Name(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MemberFilter(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, m: MemberInfo, filterCriteria: ObjectType, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> BooleanType: ...
    
    def Invoke(self, m: MemberInfo, filterCriteria: ObjectType) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MemberInfo(ABC, ObjectType, ICustomAttributeProvider, _MemberInfo):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]: ...
    
    @property
    def DeclaringType(self) -> TypeType: ...
    
    @property
    def MemberType(self) -> MemberTypes: ...
    
    @property
    def MetadataToken(self) -> IntType: ...
    
    @property
    def Module(self) -> Module: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def ReflectedType(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @overload
    def GetCustomAttributes(self, inherit: BooleanType) -> ArrayType[ObjectType]: ...
    
    @overload
    def GetCustomAttributes(self, attributeType: TypeType, inherit: BooleanType) -> ArrayType[ObjectType]: ...
    
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def IsDefined(self, attributeType: TypeType, inherit: BooleanType) -> BooleanType: ...
    
    def get_CustomAttributes(self) -> IEnumerable[CustomAttributeData]: ...
    
    def get_DeclaringType(self) -> TypeType: ...
    
    def get_MemberType(self) -> MemberTypes: ...
    
    def get_MetadataToken(self) -> IntType: ...
    
    def get_Module(self) -> Module: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_ReflectedType(self) -> TypeType: ...
    
    @staticmethod
    def op_Equality(left: MemberInfo, right: MemberInfo) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(left: MemberInfo, right: MemberInfo) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MemberInfoSerializationHolder(ObjectType, ISerializable, IObjectReference):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    
    def GetRealObject(self, context: StreamingContext) -> ObjectType: ...
    
    @staticmethod
    @overload
    def GetSerializationInfo(info: SerializationInfo, name: StringType, reflectedClass: RuntimeType, signature: StringType, type: MemberTypes) -> VoidType: ...
    
    @staticmethod
    @overload
    def GetSerializationInfo(info: SerializationInfo, name: StringType, reflectedClass: RuntimeType, signature: StringType, signature2: StringType, type: MemberTypes, genericArguments: ArrayType[TypeType]) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MetadataException(Exception, ISerializable, _Exception):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def ToString(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MethodBase(ABC, MemberInfo, ICustomAttributeProvider, _MemberInfo, _MethodBase):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Attributes(self) -> MethodAttributes: ...
    
    @property
    def CallingConvention(self) -> CallingConventions: ...
    
    @property
    def ContainsGenericParameters(self) -> BooleanType: ...
    
    @property
    def IsAbstract(self) -> BooleanType: ...
    
    @property
    def IsAssembly(self) -> BooleanType: ...
    
    @property
    def IsConstructor(self) -> BooleanType: ...
    
    @property
    def IsFamily(self) -> BooleanType: ...
    
    @property
    def IsFamilyAndAssembly(self) -> BooleanType: ...
    
    @property
    def IsFamilyOrAssembly(self) -> BooleanType: ...
    
    @property
    def IsFinal(self) -> BooleanType: ...
    
    @property
    def IsGenericMethod(self) -> BooleanType: ...
    
    @property
    def IsGenericMethodDefinition(self) -> BooleanType: ...
    
    @property
    def IsHideBySig(self) -> BooleanType: ...
    
    @property
    def IsPrivate(self) -> BooleanType: ...
    
    @property
    def IsPublic(self) -> BooleanType: ...
    
    @property
    def IsSecurityCritical(self) -> BooleanType: ...
    
    @property
    def IsSecuritySafeCritical(self) -> BooleanType: ...
    
    @property
    def IsSecurityTransparent(self) -> BooleanType: ...
    
    @property
    def IsSpecialName(self) -> BooleanType: ...
    
    @property
    def IsStatic(self) -> BooleanType: ...
    
    @property
    def IsVirtual(self) -> BooleanType: ...
    
    @property
    def MethodHandle(self) -> RuntimeMethodHandle: ...
    
    @property
    def MethodImplementationFlags(self) -> MethodImplAttributes: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @staticmethod
    def GetCurrentMethod() -> MethodBase: ...
    
    def GetGenericArguments(self) -> ArrayType[TypeType]: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def GetMethodBody(self) -> MethodBody: ...
    
    @staticmethod
    @overload
    def GetMethodFromHandle(handle: RuntimeMethodHandle) -> MethodBase: ...
    
    @staticmethod
    @overload
    def GetMethodFromHandle(handle: RuntimeMethodHandle, declaringType: RuntimeTypeHandle) -> MethodBase: ...
    
    def GetMethodImplementationFlags(self) -> MethodImplAttributes: ...
    
    def GetParameters(self) -> ArrayType[ParameterInfo]: ...
    
    @overload
    def Invoke(self, obj: ObjectType, parameters: ArrayType[ObjectType]) -> ObjectType: ...
    
    @overload
    def Invoke(self, obj: ObjectType, invokeAttr: BindingFlags, binder: Binder, parameters: ArrayType[ObjectType], culture: CultureInfo) -> ObjectType: ...
    
    def get_Attributes(self) -> MethodAttributes: ...
    
    def get_CallingConvention(self) -> CallingConventions: ...
    
    def get_ContainsGenericParameters(self) -> BooleanType: ...
    
    def get_IsAbstract(self) -> BooleanType: ...
    
    def get_IsAssembly(self) -> BooleanType: ...
    
    def get_IsConstructor(self) -> BooleanType: ...
    
    def get_IsFamily(self) -> BooleanType: ...
    
    def get_IsFamilyAndAssembly(self) -> BooleanType: ...
    
    def get_IsFamilyOrAssembly(self) -> BooleanType: ...
    
    def get_IsFinal(self) -> BooleanType: ...
    
    def get_IsGenericMethod(self) -> BooleanType: ...
    
    def get_IsGenericMethodDefinition(self) -> BooleanType: ...
    
    def get_IsHideBySig(self) -> BooleanType: ...
    
    def get_IsPrivate(self) -> BooleanType: ...
    
    def get_IsPublic(self) -> BooleanType: ...
    
    def get_IsSecurityCritical(self) -> BooleanType: ...
    
    def get_IsSecuritySafeCritical(self) -> BooleanType: ...
    
    def get_IsSecurityTransparent(self) -> BooleanType: ...
    
    def get_IsSpecialName(self) -> BooleanType: ...
    
    def get_IsStatic(self) -> BooleanType: ...
    
    def get_IsVirtual(self) -> BooleanType: ...
    
    def get_MethodHandle(self) -> RuntimeMethodHandle: ...
    
    def get_MethodImplementationFlags(self) -> MethodImplAttributes: ...
    
    @staticmethod
    def op_Equality(left: MethodBase, right: MethodBase) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(left: MethodBase, right: MethodBase) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MethodBody(ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def ExceptionHandlingClauses(self) -> IList[ExceptionHandlingClause]: ...
    
    @property
    def InitLocals(self) -> BooleanType: ...
    
    @property
    def LocalSignatureMetadataToken(self) -> IntType: ...
    
    @property
    def LocalVariables(self) -> IList[LocalVariableInfo]: ...
    
    @property
    def MaxStackSize(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def GetILAsByteArray(self) -> ArrayType[ByteType]: ...
    
    def get_ExceptionHandlingClauses(self) -> IList[ExceptionHandlingClause]: ...
    
    def get_InitLocals(self) -> BooleanType: ...
    
    def get_LocalSignatureMetadataToken(self) -> IntType: ...
    
    def get_LocalVariables(self) -> IList[LocalVariableInfo]: ...
    
    def get_MaxStackSize(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MethodInfo(ABC, MethodBase, ICustomAttributeProvider, _MemberInfo, _MethodBase, _MethodInfo):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def MemberType(self) -> MemberTypes: ...
    
    @property
    def ReturnParameter(self) -> ParameterInfo: ...
    
    @property
    def ReturnType(self) -> TypeType: ...
    
    @property
    def ReturnTypeCustomAttributes(self) -> ICustomAttributeProvider: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def CreateDelegate(self, delegateType: TypeType) -> Delegate: ...
    
    @overload
    def CreateDelegate(self, delegateType: TypeType, target: ObjectType) -> Delegate: ...
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetBaseDefinition(self) -> MethodInfo: ...
    
    def GetGenericArguments(self) -> ArrayType[TypeType]: ...
    
    def GetGenericMethodDefinition(self) -> MethodInfo: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def MakeGenericMethod(self, typeArguments: ArrayType[TypeType]) -> MethodInfo: ...
    
    def get_MemberType(self) -> MemberTypes: ...
    
    def get_ReturnParameter(self) -> ParameterInfo: ...
    
    def get_ReturnType(self) -> TypeType: ...
    
    def get_ReturnTypeCustomAttributes(self) -> ICustomAttributeProvider: ...
    
    @staticmethod
    def op_Equality(left: MethodInfo, right: MethodInfo) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(left: MethodInfo, right: MethodInfo) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Missing(ObjectType, ISerializable):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Value() -> Missing: ...
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Module(ABC, ObjectType, _Module, ISerializable, ICustomAttributeProvider):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def FilterTypeName() -> TypeFilter: ...
    
    @staticmethod
    @property
    def FilterTypeNameIgnoreCase() -> TypeFilter: ...
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Assembly(self) -> Assembly: ...
    
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]: ...
    
    @property
    def FullyQualifiedName(self) -> StringType: ...
    
    @property
    def MDStreamVersion(self) -> IntType: ...
    
    @property
    def MetadataToken(self) -> IntType: ...
    
    @property
    def ModuleHandle(self) -> ModuleHandle: ...
    
    @property
    def ModuleVersionId(self) -> Guid: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def ScopeName(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    def FindTypes(self, filter: TypeFilter, filterCriteria: ObjectType) -> ArrayType[TypeType]: ...
    
    @overload
    def GetCustomAttributes(self, inherit: BooleanType) -> ArrayType[ObjectType]: ...
    
    @overload
    def GetCustomAttributes(self, attributeType: TypeType, inherit: BooleanType) -> ArrayType[ObjectType]: ...
    
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]: ...
    
    @overload
    def GetField(self, name: StringType) -> FieldInfo: ...
    
    @overload
    def GetField(self, name: StringType, bindingAttr: BindingFlags) -> FieldInfo: ...
    
    @overload
    def GetFields(self) -> ArrayType[FieldInfo]: ...
    
    @overload
    def GetFields(self, bindingFlags: BindingFlags) -> ArrayType[FieldInfo]: ...
    
    def GetHashCode(self) -> IntType: ...
    
    @overload
    def GetMethod(self, name: StringType, bindingAttr: BindingFlags, binder: Binder, callConvention: CallingConventions, types: ArrayType[TypeType], modifiers: ArrayType[ParameterModifier]) -> MethodInfo: ...
    
    @overload
    def GetMethod(self, name: StringType, types: ArrayType[TypeType]) -> MethodInfo: ...
    
    @overload
    def GetMethod(self, name: StringType) -> MethodInfo: ...
    
    @overload
    def GetMethods(self) -> ArrayType[MethodInfo]: ...
    
    @overload
    def GetMethods(self, bindingFlags: BindingFlags) -> ArrayType[MethodInfo]: ...
    
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    
    def GetPEKind(self, peKind: PortableExecutableKinds, machine: ImageFileMachine) -> Tuple[VoidType, PortableExecutableKinds, ImageFileMachine]: ...
    
    def GetSignerCertificate(self) -> X509Certificate: ...
    
    @overload
    def GetType(self, className: StringType, ignoreCase: BooleanType) -> TypeType: ...
    
    @overload
    def GetType(self, className: StringType) -> TypeType: ...
    
    @overload
    def GetType(self, className: StringType, throwOnError: BooleanType, ignoreCase: BooleanType) -> TypeType: ...
    
    def GetTypes(self) -> ArrayType[TypeType]: ...
    
    def IsDefined(self, attributeType: TypeType, inherit: BooleanType) -> BooleanType: ...
    
    def IsResource(self) -> BooleanType: ...
    
    @overload
    def ResolveField(self, metadataToken: IntType) -> FieldInfo: ...
    
    @overload
    def ResolveField(self, metadataToken: IntType, genericTypeArguments: ArrayType[TypeType], genericMethodArguments: ArrayType[TypeType]) -> FieldInfo: ...
    
    @overload
    def ResolveMember(self, metadataToken: IntType) -> MemberInfo: ...
    
    @overload
    def ResolveMember(self, metadataToken: IntType, genericTypeArguments: ArrayType[TypeType], genericMethodArguments: ArrayType[TypeType]) -> MemberInfo: ...
    
    @overload
    def ResolveMethod(self, metadataToken: IntType) -> MethodBase: ...
    
    @overload
    def ResolveMethod(self, metadataToken: IntType, genericTypeArguments: ArrayType[TypeType], genericMethodArguments: ArrayType[TypeType]) -> MethodBase: ...
    
    def ResolveSignature(self, metadataToken: IntType) -> ArrayType[ByteType]: ...
    
    def ResolveString(self, metadataToken: IntType) -> StringType: ...
    
    @overload
    def ResolveType(self, metadataToken: IntType) -> TypeType: ...
    
    @overload
    def ResolveType(self, metadataToken: IntType, genericTypeArguments: ArrayType[TypeType], genericMethodArguments: ArrayType[TypeType]) -> TypeType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Assembly(self) -> Assembly: ...
    
    def get_CustomAttributes(self) -> IEnumerable[CustomAttributeData]: ...
    
    def get_FullyQualifiedName(self) -> StringType: ...
    
    def get_MDStreamVersion(self) -> IntType: ...
    
    def get_MetadataToken(self) -> IntType: ...
    
    def get_ModuleHandle(self) -> ModuleHandle: ...
    
    def get_ModuleVersionId(self) -> Guid: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_ScopeName(self) -> StringType: ...
    
    @staticmethod
    def op_Equality(left: Module, right: Module) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(left: Module, right: Module) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ModuleResolveEventHandler(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, sender: ObjectType, e: ResolveEventArgs, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> Module: ...
    
    def Invoke(self, sender: ObjectType, e: ResolveEventArgs) -> Module: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ObfuscateAssemblyAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, assemblyIsPrivate: BooleanType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AssemblyIsPrivate(self) -> BooleanType: ...
    
    @property
    def StripAfterObfuscation(self) -> BooleanType: ...
    
    @StripAfterObfuscation.setter
    def StripAfterObfuscation(self, value: BooleanType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_AssemblyIsPrivate(self) -> BooleanType: ...
    
    def get_StripAfterObfuscation(self) -> BooleanType: ...
    
    def set_StripAfterObfuscation(self, value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ObfuscationAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ApplyToMembers(self) -> BooleanType: ...
    
    @ApplyToMembers.setter
    def ApplyToMembers(self, value: BooleanType) -> None: ...
    
    @property
    def Exclude(self) -> BooleanType: ...
    
    @Exclude.setter
    def Exclude(self, value: BooleanType) -> None: ...
    
    @property
    def Feature(self) -> StringType: ...
    
    @Feature.setter
    def Feature(self, value: StringType) -> None: ...
    
    @property
    def StripAfterObfuscation(self) -> BooleanType: ...
    
    @StripAfterObfuscation.setter
    def StripAfterObfuscation(self, value: BooleanType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_ApplyToMembers(self) -> BooleanType: ...
    
    def get_Exclude(self) -> BooleanType: ...
    
    def get_Feature(self) -> StringType: ...
    
    def get_StripAfterObfuscation(self) -> BooleanType: ...
    
    def set_ApplyToMembers(self, value: BooleanType) -> VoidType: ...
    
    def set_Exclude(self, value: BooleanType) -> VoidType: ...
    
    def set_Feature(self, value: StringType) -> VoidType: ...
    
    def set_StripAfterObfuscation(self, value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ParameterInfo(ObjectType, _ParameterInfo, ICustomAttributeProvider, IObjectReference):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Attributes(self) -> ParameterAttributes: ...
    
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]: ...
    
    @property
    def DefaultValue(self) -> ObjectType: ...
    
    @property
    def HasDefaultValue(self) -> BooleanType: ...
    
    @property
    def IsIn(self) -> BooleanType: ...
    
    @property
    def IsLcid(self) -> BooleanType: ...
    
    @property
    def IsOptional(self) -> BooleanType: ...
    
    @property
    def IsOut(self) -> BooleanType: ...
    
    @property
    def IsRetval(self) -> BooleanType: ...
    
    @property
    def Member(self) -> MemberInfo: ...
    
    @property
    def MetadataToken(self) -> IntType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def ParameterType(self) -> TypeType: ...
    
    @property
    def Position(self) -> IntType: ...
    
    @property
    def RawDefaultValue(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def GetCustomAttributes(self, inherit: BooleanType) -> ArrayType[ObjectType]: ...
    
    @overload
    def GetCustomAttributes(self, attributeType: TypeType, inherit: BooleanType) -> ArrayType[ObjectType]: ...
    
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]: ...
    
    def GetOptionalCustomModifiers(self) -> ArrayType[TypeType]: ...
    
    def GetRealObject(self, context: StreamingContext) -> ObjectType: ...
    
    def GetRequiredCustomModifiers(self) -> ArrayType[TypeType]: ...
    
    def IsDefined(self, attributeType: TypeType, inherit: BooleanType) -> BooleanType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Attributes(self) -> ParameterAttributes: ...
    
    def get_CustomAttributes(self) -> IEnumerable[CustomAttributeData]: ...
    
    def get_DefaultValue(self) -> ObjectType: ...
    
    def get_HasDefaultValue(self) -> BooleanType: ...
    
    def get_IsIn(self) -> BooleanType: ...
    
    def get_IsLcid(self) -> BooleanType: ...
    
    def get_IsOptional(self) -> BooleanType: ...
    
    def get_IsOut(self) -> BooleanType: ...
    
    def get_IsRetval(self) -> BooleanType: ...
    
    def get_Member(self) -> MemberInfo: ...
    
    def get_MetadataToken(self) -> IntType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_ParameterType(self) -> TypeType: ...
    
    def get_Position(self) -> IntType: ...
    
    def get_RawDefaultValue(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Pointer(ObjectType, ISerializable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def Box(ptr: VoidType, type: TypeType) -> ObjectType: ...
    
    @staticmethod
    def Unbox(ptr: ObjectType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PropertyInfo(ABC, MemberInfo, ICustomAttributeProvider, _MemberInfo, _PropertyInfo):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Attributes(self) -> PropertyAttributes: ...
    
    @property
    def CanRead(self) -> BooleanType: ...
    
    @property
    def CanWrite(self) -> BooleanType: ...
    
    @property
    def GetMethod(self) -> MethodInfo: ...
    
    @property
    def IsSpecialName(self) -> BooleanType: ...
    
    @property
    def MemberType(self) -> MemberTypes: ...
    
    @property
    def PropertyType(self) -> TypeType: ...
    
    @property
    def SetMethod(self) -> MethodInfo: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @overload
    def GetAccessors(self) -> ArrayType[MethodInfo]: ...
    
    @overload
    def GetAccessors(self, nonPublic: BooleanType) -> ArrayType[MethodInfo]: ...
    
    def GetConstantValue(self) -> ObjectType: ...
    
    @overload
    def GetGetMethod(self) -> MethodInfo: ...
    
    @overload
    def GetGetMethod(self, nonPublic: BooleanType) -> MethodInfo: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def GetIndexParameters(self) -> ArrayType[ParameterInfo]: ...
    
    def GetOptionalCustomModifiers(self) -> ArrayType[TypeType]: ...
    
    def GetRawConstantValue(self) -> ObjectType: ...
    
    def GetRequiredCustomModifiers(self) -> ArrayType[TypeType]: ...
    
    @overload
    def GetSetMethod(self) -> MethodInfo: ...
    
    @overload
    def GetSetMethod(self, nonPublic: BooleanType) -> MethodInfo: ...
    
    @overload
    def GetValue(self, obj: ObjectType) -> ObjectType: ...
    
    @overload
    def GetValue(self, obj: ObjectType, index: ArrayType[ObjectType]) -> ObjectType: ...
    
    @overload
    def GetValue(self, obj: ObjectType, invokeAttr: BindingFlags, binder: Binder, index: ArrayType[ObjectType], culture: CultureInfo) -> ObjectType: ...
    
    @overload
    def SetValue(self, obj: ObjectType, value: ObjectType) -> VoidType: ...
    
    @overload
    def SetValue(self, obj: ObjectType, value: ObjectType, index: ArrayType[ObjectType]) -> VoidType: ...
    
    @overload
    def SetValue(self, obj: ObjectType, value: ObjectType, invokeAttr: BindingFlags, binder: Binder, index: ArrayType[ObjectType], culture: CultureInfo) -> VoidType: ...
    
    def get_Attributes(self) -> PropertyAttributes: ...
    
    def get_CanRead(self) -> BooleanType: ...
    
    def get_CanWrite(self) -> BooleanType: ...
    
    def get_GetMethod(self) -> MethodInfo: ...
    
    def get_IsSpecialName(self) -> BooleanType: ...
    
    def get_MemberType(self) -> MemberTypes: ...
    
    def get_PropertyType(self) -> TypeType: ...
    
    def get_SetMethod(self) -> MethodInfo: ...
    
    @staticmethod
    def op_Equality(left: PropertyInfo, right: PropertyInfo) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(left: PropertyInfo, right: PropertyInfo) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PseudoCustomAttribute(ABC, ObjectType):
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


class ReflectionContext(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetTypeForObject(self, value: ObjectType) -> TypeInfo: ...
    
    def MapAssembly(self, assembly: Assembly) -> Assembly: ...
    
    def MapType(self, type: TypeInfo) -> TypeInfo: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ReflectionTypeLoadException(SystemException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, classes: ArrayType[TypeType], exceptions: ArrayType[Exception]): ...
    
    @overload
    def __init__(self, classes: ArrayType[TypeType], exceptions: ArrayType[Exception], message: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def LoaderExceptions(self) -> ArrayType[Exception]: ...
    
    @property
    def Types(self) -> ArrayType[TypeType]: ...
    
    # ---------- Methods ---------- #
    
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    
    def get_LoaderExceptions(self) -> ArrayType[Exception]: ...
    
    def get_Types(self) -> ArrayType[TypeType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RtFieldInfo(RuntimeFieldInfo, ICustomAttributeProvider, _MemberInfo, _FieldInfo, ISerializable, IRuntimeFieldInfo):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Attributes(self) -> FieldAttributes: ...
    
    @property
    def FieldHandle(self) -> RuntimeFieldHandle: ...
    
    @property
    def FieldType(self) -> TypeType: ...
    
    @property
    def MetadataToken(self) -> IntType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetOptionalCustomModifiers(self) -> ArrayType[TypeType]: ...
    
    def GetRawConstantValue(self) -> ObjectType: ...
    
    def GetRequiredCustomModifiers(self) -> ArrayType[TypeType]: ...
    
    def GetValue(self, obj: ObjectType) -> ObjectType: ...
    
    def GetValueDirect(self, obj: TypedReference) -> ObjectType: ...
    
    @overload
    def SetValue(self, obj: ObjectType, value: ObjectType, invokeAttr: BindingFlags, binder: Binder, culture: CultureInfo) -> VoidType: ...
    
    def SetValueDirect(self, obj: TypedReference, value: ObjectType) -> VoidType: ...
    
    def get_Attributes(self) -> FieldAttributes: ...
    
    def get_FieldHandle(self) -> RuntimeFieldHandle: ...
    
    def get_FieldType(self) -> TypeType: ...
    
    def get_MetadataToken(self) -> IntType: ...
    
    def get_Name(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RuntimeAssembly(Assembly, _Assembly, IEvidenceFactory, ICustomAttributeProvider, ISerializable, ICustomQueryInterface):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def CodeBase(self) -> StringType: ...
    
    @property
    def DefinedTypes(self) -> IEnumerable[TypeInfo]: ...
    
    @property
    def EntryPoint(self) -> MethodInfo: ...
    
    @property
    def Evidence(self) -> Evidence: ...
    
    @property
    def FullName(self) -> StringType: ...
    
    @property
    def GlobalAssemblyCache(self) -> BooleanType: ...
    
    @property
    def HostContext(self) -> LongType: ...
    
    @property
    def ImageRuntimeVersion(self) -> StringType: ...
    
    @property
    def IsDynamic(self) -> BooleanType: ...
    
    @property
    def Location(self) -> StringType: ...
    
    @property
    def ManifestModule(self) -> Module: ...
    
    @property
    def PermissionSet(self) -> PermissionSet: ...
    
    @property
    def ReflectionOnly(self) -> BooleanType: ...
    
    @property
    def SecurityRuleSet(self) -> SecurityRuleSet: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def GetCustomAttributes(self, inherit: BooleanType) -> ArrayType[ObjectType]: ...
    
    @overload
    def GetCustomAttributes(self, attributeType: TypeType, inherit: BooleanType) -> ArrayType[ObjectType]: ...
    
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]: ...
    
    def GetExportedTypes(self) -> ArrayType[TypeType]: ...
    
    def GetFile(self, name: StringType) -> FileStream: ...
    
    @overload
    def GetFiles(self, getResourceModules: BooleanType) -> ArrayType[FileStream]: ...
    
    @overload
    def GetLoadedModules(self, getResourceModules: BooleanType) -> ArrayType[Module]: ...
    
    def GetManifestResourceInfo(self, resourceName: StringType) -> ManifestResourceInfo: ...
    
    def GetManifestResourceNames(self) -> ArrayType[StringType]: ...
    
    @overload
    def GetManifestResourceStream(self, type: TypeType, name: StringType) -> Stream: ...
    
    @overload
    def GetManifestResourceStream(self, name: StringType) -> Stream: ...
    
    def GetModule(self, name: StringType) -> Module: ...
    
    @overload
    def GetModules(self, getResourceModules: BooleanType) -> ArrayType[Module]: ...
    
    @overload
    def GetName(self, copiedName: BooleanType) -> AssemblyName: ...
    
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    
    def GetReferencedAssemblies(self) -> ArrayType[AssemblyName]: ...
    
    @overload
    def GetSatelliteAssembly(self, culture: CultureInfo) -> Assembly: ...
    
    @overload
    def GetSatelliteAssembly(self, culture: CultureInfo, version: Version) -> Assembly: ...
    
    @overload
    def GetType(self, name: StringType, throwOnError: BooleanType, ignoreCase: BooleanType) -> TypeType: ...
    
    def IsDefined(self, attributeType: TypeType, inherit: BooleanType) -> BooleanType: ...
    
    @overload
    def LoadModule(self, moduleName: StringType, rawModule: ArrayType[ByteType], rawSymbolStore: ArrayType[ByteType]) -> Module: ...
    
    def add_ModuleResolve(self, value: ModuleResolveEventHandler) -> VoidType: ...
    
    def get_CodeBase(self) -> StringType: ...
    
    def get_DefinedTypes(self) -> IEnumerable[TypeInfo]: ...
    
    def get_EntryPoint(self) -> MethodInfo: ...
    
    def get_Evidence(self) -> Evidence: ...
    
    def get_FullName(self) -> StringType: ...
    
    def get_GlobalAssemblyCache(self) -> BooleanType: ...
    
    def get_HostContext(self) -> LongType: ...
    
    def get_ImageRuntimeVersion(self) -> StringType: ...
    
    def get_IsDynamic(self) -> BooleanType: ...
    
    def get_Location(self) -> StringType: ...
    
    def get_ManifestModule(self) -> Module: ...
    
    def get_PermissionSet(self) -> PermissionSet: ...
    
    def get_ReflectionOnly(self) -> BooleanType: ...
    
    def get_SecurityRuleSet(self) -> SecurityRuleSet: ...
    
    def remove_ModuleResolve(self, value: ModuleResolveEventHandler) -> VoidType: ...
    
    # ---------- Events ---------- #
    
    ModuleResolve: EventType[ModuleResolveEventHandler] = ...
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RuntimeConstructorInfo(ConstructorInfo, ICustomAttributeProvider, _MemberInfo, _MethodBase, _ConstructorInfo, ISerializable, IRuntimeMethodInfo):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Attributes(self) -> MethodAttributes: ...
    
    @property
    def CallingConvention(self) -> CallingConventions: ...
    
    @property
    def ContainsGenericParameters(self) -> BooleanType: ...
    
    @property
    def DeclaringType(self) -> TypeType: ...
    
    @property
    def IsSecurityCritical(self) -> BooleanType: ...
    
    @property
    def IsSecuritySafeCritical(self) -> BooleanType: ...
    
    @property
    def IsSecurityTransparent(self) -> BooleanType: ...
    
    @property
    def MemberType(self) -> MemberTypes: ...
    
    @property
    def MetadataToken(self) -> IntType: ...
    
    @property
    def MethodHandle(self) -> RuntimeMethodHandle: ...
    
    @property
    def Module(self) -> Module: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def ReflectedType(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def GetCustomAttributes(self, inherit: BooleanType) -> ArrayType[ObjectType]: ...
    
    @overload
    def GetCustomAttributes(self, attributeType: TypeType, inherit: BooleanType) -> ArrayType[ObjectType]: ...
    
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]: ...
    
    def GetMethodBody(self) -> MethodBody: ...
    
    def GetMethodImplementationFlags(self) -> MethodImplAttributes: ...
    
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    
    def GetParameters(self) -> ArrayType[ParameterInfo]: ...
    
    @overload
    def Invoke(self, invokeAttr: BindingFlags, binder: Binder, parameters: ArrayType[ObjectType], culture: CultureInfo) -> ObjectType: ...
    
    @overload
    def Invoke(self, obj: ObjectType, invokeAttr: BindingFlags, binder: Binder, parameters: ArrayType[ObjectType], culture: CultureInfo) -> ObjectType: ...
    
    def IsDefined(self, attributeType: TypeType, inherit: BooleanType) -> BooleanType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Attributes(self) -> MethodAttributes: ...
    
    def get_CallingConvention(self) -> CallingConventions: ...
    
    def get_ContainsGenericParameters(self) -> BooleanType: ...
    
    def get_DeclaringType(self) -> TypeType: ...
    
    def get_IsSecurityCritical(self) -> BooleanType: ...
    
    def get_IsSecuritySafeCritical(self) -> BooleanType: ...
    
    def get_IsSecurityTransparent(self) -> BooleanType: ...
    
    def get_MemberType(self) -> MemberTypes: ...
    
    def get_MetadataToken(self) -> IntType: ...
    
    def get_MethodHandle(self) -> RuntimeMethodHandle: ...
    
    def get_Module(self) -> Module: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_ReflectedType(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RuntimeEventInfo(EventInfo, ICustomAttributeProvider, _MemberInfo, _EventInfo, ISerializable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Attributes(self) -> EventAttributes: ...
    
    @property
    def DeclaringType(self) -> TypeType: ...
    
    @property
    def MemberType(self) -> MemberTypes: ...
    
    @property
    def MetadataToken(self) -> IntType: ...
    
    @property
    def Module(self) -> Module: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def ReflectedType(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def GetAddMethod(self, nonPublic: BooleanType) -> MethodInfo: ...
    
    @overload
    def GetCustomAttributes(self, inherit: BooleanType) -> ArrayType[ObjectType]: ...
    
    @overload
    def GetCustomAttributes(self, attributeType: TypeType, inherit: BooleanType) -> ArrayType[ObjectType]: ...
    
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]: ...
    
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    
    @overload
    def GetOtherMethods(self, nonPublic: BooleanType) -> ArrayType[MethodInfo]: ...
    
    @overload
    def GetRaiseMethod(self, nonPublic: BooleanType) -> MethodInfo: ...
    
    @overload
    def GetRemoveMethod(self, nonPublic: BooleanType) -> MethodInfo: ...
    
    def IsDefined(self, attributeType: TypeType, inherit: BooleanType) -> BooleanType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Attributes(self) -> EventAttributes: ...
    
    def get_DeclaringType(self) -> TypeType: ...
    
    def get_MemberType(self) -> MemberTypes: ...
    
    def get_MetadataToken(self) -> IntType: ...
    
    def get_Module(self) -> Module: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_ReflectedType(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RuntimeFieldInfo(ABC, FieldInfo, ICustomAttributeProvider, _MemberInfo, _FieldInfo, ISerializable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def DeclaringType(self) -> TypeType: ...
    
    @property
    def MemberType(self) -> MemberTypes: ...
    
    @property
    def Module(self) -> Module: ...
    
    @property
    def ReflectedType(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def GetCustomAttributes(self, inherit: BooleanType) -> ArrayType[ObjectType]: ...
    
    @overload
    def GetCustomAttributes(self, attributeType: TypeType, inherit: BooleanType) -> ArrayType[ObjectType]: ...
    
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]: ...
    
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    
    def IsDefined(self, attributeType: TypeType, inherit: BooleanType) -> BooleanType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_DeclaringType(self) -> TypeType: ...
    
    def get_MemberType(self) -> MemberTypes: ...
    
    def get_Module(self) -> Module: ...
    
    def get_ReflectedType(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RuntimeMethodInfo(MethodInfo, ICustomAttributeProvider, _MemberInfo, _MethodBase, _MethodInfo, ISerializable, IRuntimeMethodInfo):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Attributes(self) -> MethodAttributes: ...
    
    @property
    def CallingConvention(self) -> CallingConventions: ...
    
    @property
    def ContainsGenericParameters(self) -> BooleanType: ...
    
    @property
    def DeclaringType(self) -> TypeType: ...
    
    @property
    def IsGenericMethod(self) -> BooleanType: ...
    
    @property
    def IsGenericMethodDefinition(self) -> BooleanType: ...
    
    @property
    def IsSecurityCritical(self) -> BooleanType: ...
    
    @property
    def IsSecuritySafeCritical(self) -> BooleanType: ...
    
    @property
    def IsSecurityTransparent(self) -> BooleanType: ...
    
    @property
    def MemberType(self) -> MemberTypes: ...
    
    @property
    def MetadataToken(self) -> IntType: ...
    
    @property
    def MethodHandle(self) -> RuntimeMethodHandle: ...
    
    @property
    def Module(self) -> Module: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def ReflectedType(self) -> TypeType: ...
    
    @property
    def ReturnParameter(self) -> ParameterInfo: ...
    
    @property
    def ReturnType(self) -> TypeType: ...
    
    @property
    def ReturnTypeCustomAttributes(self) -> ICustomAttributeProvider: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def CreateDelegate(self, delegateType: TypeType) -> Delegate: ...
    
    @overload
    def CreateDelegate(self, delegateType: TypeType, target: ObjectType) -> Delegate: ...
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetBaseDefinition(self) -> MethodInfo: ...
    
    @overload
    def GetCustomAttributes(self, inherit: BooleanType) -> ArrayType[ObjectType]: ...
    
    @overload
    def GetCustomAttributes(self, attributeType: TypeType, inherit: BooleanType) -> ArrayType[ObjectType]: ...
    
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]: ...
    
    def GetGenericArguments(self) -> ArrayType[TypeType]: ...
    
    def GetGenericMethodDefinition(self) -> MethodInfo: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def GetMethodBody(self) -> MethodBody: ...
    
    def GetMethodImplementationFlags(self) -> MethodImplAttributes: ...
    
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    
    def GetParameters(self) -> ArrayType[ParameterInfo]: ...
    
    @overload
    def Invoke(self, obj: ObjectType, invokeAttr: BindingFlags, binder: Binder, parameters: ArrayType[ObjectType], culture: CultureInfo) -> ObjectType: ...
    
    def IsDefined(self, attributeType: TypeType, inherit: BooleanType) -> BooleanType: ...
    
    def MakeGenericMethod(self, methodInstantiation: ArrayType[TypeType]) -> MethodInfo: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Attributes(self) -> MethodAttributes: ...
    
    def get_CallingConvention(self) -> CallingConventions: ...
    
    def get_ContainsGenericParameters(self) -> BooleanType: ...
    
    def get_DeclaringType(self) -> TypeType: ...
    
    def get_IsGenericMethod(self) -> BooleanType: ...
    
    def get_IsGenericMethodDefinition(self) -> BooleanType: ...
    
    def get_IsSecurityCritical(self) -> BooleanType: ...
    
    def get_IsSecuritySafeCritical(self) -> BooleanType: ...
    
    def get_IsSecurityTransparent(self) -> BooleanType: ...
    
    def get_MemberType(self) -> MemberTypes: ...
    
    def get_MetadataToken(self) -> IntType: ...
    
    def get_MethodHandle(self) -> RuntimeMethodHandle: ...
    
    def get_Module(self) -> Module: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_ReflectedType(self) -> TypeType: ...
    
    def get_ReturnParameter(self) -> ParameterInfo: ...
    
    def get_ReturnType(self) -> TypeType: ...
    
    def get_ReturnTypeCustomAttributes(self) -> ICustomAttributeProvider: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RuntimeModule(Module, _Module, ISerializable, ICustomAttributeProvider):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Assembly(self) -> Assembly: ...
    
    @property
    def FullyQualifiedName(self) -> StringType: ...
    
    @property
    def MDStreamVersion(self) -> IntType: ...
    
    @property
    def MetadataToken(self) -> IntType: ...
    
    @property
    def ModuleVersionId(self) -> Guid: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def ScopeName(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def GetCustomAttributes(self, inherit: BooleanType) -> ArrayType[ObjectType]: ...
    
    @overload
    def GetCustomAttributes(self, attributeType: TypeType, inherit: BooleanType) -> ArrayType[ObjectType]: ...
    
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]: ...
    
    @overload
    def GetField(self, name: StringType, bindingAttr: BindingFlags) -> FieldInfo: ...
    
    @overload
    def GetFields(self, bindingFlags: BindingFlags) -> ArrayType[FieldInfo]: ...
    
    @overload
    def GetMethods(self, bindingFlags: BindingFlags) -> ArrayType[MethodInfo]: ...
    
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    
    def GetPEKind(self, peKind: PortableExecutableKinds, machine: ImageFileMachine) -> Tuple[VoidType, PortableExecutableKinds, ImageFileMachine]: ...
    
    def GetSignerCertificate(self) -> X509Certificate: ...
    
    @overload
    def GetType(self, className: StringType, throwOnError: BooleanType, ignoreCase: BooleanType) -> TypeType: ...
    
    def GetTypes(self) -> ArrayType[TypeType]: ...
    
    def IsDefined(self, attributeType: TypeType, inherit: BooleanType) -> BooleanType: ...
    
    def IsResource(self) -> BooleanType: ...
    
    @overload
    def ResolveField(self, metadataToken: IntType, genericTypeArguments: ArrayType[TypeType], genericMethodArguments: ArrayType[TypeType]) -> FieldInfo: ...
    
    @overload
    def ResolveMember(self, metadataToken: IntType, genericTypeArguments: ArrayType[TypeType], genericMethodArguments: ArrayType[TypeType]) -> MemberInfo: ...
    
    @overload
    def ResolveMethod(self, metadataToken: IntType, genericTypeArguments: ArrayType[TypeType], genericMethodArguments: ArrayType[TypeType]) -> MethodBase: ...
    
    def ResolveSignature(self, metadataToken: IntType) -> ArrayType[ByteType]: ...
    
    def ResolveString(self, metadataToken: IntType) -> StringType: ...
    
    @overload
    def ResolveType(self, metadataToken: IntType, genericTypeArguments: ArrayType[TypeType], genericMethodArguments: ArrayType[TypeType]) -> TypeType: ...
    
    def get_Assembly(self) -> Assembly: ...
    
    def get_FullyQualifiedName(self) -> StringType: ...
    
    def get_MDStreamVersion(self) -> IntType: ...
    
    def get_MetadataToken(self) -> IntType: ...
    
    def get_ModuleVersionId(self) -> Guid: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_ScopeName(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RuntimeParameterInfo(ParameterInfo, _ParameterInfo, ICustomAttributeProvider, IObjectReference, ISerializable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def DefaultValue(self) -> ObjectType: ...
    
    @property
    def HasDefaultValue(self) -> BooleanType: ...
    
    @property
    def MetadataToken(self) -> IntType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def ParameterType(self) -> TypeType: ...
    
    @property
    def RawDefaultValue(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def GetCustomAttributes(self, inherit: BooleanType) -> ArrayType[ObjectType]: ...
    
    @overload
    def GetCustomAttributes(self, attributeType: TypeType, inherit: BooleanType) -> ArrayType[ObjectType]: ...
    
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]: ...
    
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    
    def GetOptionalCustomModifiers(self) -> ArrayType[TypeType]: ...
    
    def GetRequiredCustomModifiers(self) -> ArrayType[TypeType]: ...
    
    def IsDefined(self, attributeType: TypeType, inherit: BooleanType) -> BooleanType: ...
    
    def get_DefaultValue(self) -> ObjectType: ...
    
    def get_HasDefaultValue(self) -> BooleanType: ...
    
    def get_MetadataToken(self) -> IntType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_ParameterType(self) -> TypeType: ...
    
    def get_RawDefaultValue(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RuntimePropertyInfo(PropertyInfo, ICustomAttributeProvider, _MemberInfo, _PropertyInfo, ISerializable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Attributes(self) -> PropertyAttributes: ...
    
    @property
    def CanRead(self) -> BooleanType: ...
    
    @property
    def CanWrite(self) -> BooleanType: ...
    
    @property
    def DeclaringType(self) -> TypeType: ...
    
    @property
    def MemberType(self) -> MemberTypes: ...
    
    @property
    def MetadataToken(self) -> IntType: ...
    
    @property
    def Module(self) -> Module: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def PropertyType(self) -> TypeType: ...
    
    @property
    def ReflectedType(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def GetAccessors(self, nonPublic: BooleanType) -> ArrayType[MethodInfo]: ...
    
    def GetConstantValue(self) -> ObjectType: ...
    
    @overload
    def GetCustomAttributes(self, inherit: BooleanType) -> ArrayType[ObjectType]: ...
    
    @overload
    def GetCustomAttributes(self, attributeType: TypeType, inherit: BooleanType) -> ArrayType[ObjectType]: ...
    
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]: ...
    
    @overload
    def GetGetMethod(self, nonPublic: BooleanType) -> MethodInfo: ...
    
    def GetIndexParameters(self) -> ArrayType[ParameterInfo]: ...
    
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    
    def GetOptionalCustomModifiers(self) -> ArrayType[TypeType]: ...
    
    def GetRawConstantValue(self) -> ObjectType: ...
    
    def GetRequiredCustomModifiers(self) -> ArrayType[TypeType]: ...
    
    @overload
    def GetSetMethod(self, nonPublic: BooleanType) -> MethodInfo: ...
    
    @overload
    def GetValue(self, obj: ObjectType, index: ArrayType[ObjectType]) -> ObjectType: ...
    
    @overload
    def GetValue(self, obj: ObjectType, invokeAttr: BindingFlags, binder: Binder, index: ArrayType[ObjectType], culture: CultureInfo) -> ObjectType: ...
    
    def IsDefined(self, attributeType: TypeType, inherit: BooleanType) -> BooleanType: ...
    
    @overload
    def SetValue(self, obj: ObjectType, value: ObjectType, index: ArrayType[ObjectType]) -> VoidType: ...
    
    @overload
    def SetValue(self, obj: ObjectType, value: ObjectType, invokeAttr: BindingFlags, binder: Binder, index: ArrayType[ObjectType], culture: CultureInfo) -> VoidType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Attributes(self) -> PropertyAttributes: ...
    
    def get_CanRead(self) -> BooleanType: ...
    
    def get_CanWrite(self) -> BooleanType: ...
    
    def get_DeclaringType(self) -> TypeType: ...
    
    def get_MemberType(self) -> MemberTypes: ...
    
    def get_MetadataToken(self) -> IntType: ...
    
    def get_Module(self) -> Module: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_PropertyType(self) -> TypeType: ...
    
    def get_ReflectedType(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RuntimeReflectionExtensions(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def GetMethodInfo(_del: Delegate) -> MethodInfo: ...
    
    @staticmethod
    def GetRuntimeBaseDefinition(method: MethodInfo) -> MethodInfo: ...
    
    @staticmethod
    def GetRuntimeEvent(type: TypeType, name: StringType) -> EventInfo: ...
    
    @staticmethod
    def GetRuntimeEvents(type: TypeType) -> IEnumerable[EventInfo]: ...
    
    @staticmethod
    def GetRuntimeField(type: TypeType, name: StringType) -> FieldInfo: ...
    
    @staticmethod
    def GetRuntimeFields(type: TypeType) -> IEnumerable[FieldInfo]: ...
    
    @staticmethod
    def GetRuntimeInterfaceMap(typeInfo: TypeInfo, interfaceType: TypeType) -> InterfaceMapping: ...
    
    @staticmethod
    def GetRuntimeMethod(type: TypeType, name: StringType, parameters: ArrayType[TypeType]) -> MethodInfo: ...
    
    @staticmethod
    def GetRuntimeMethods(type: TypeType) -> IEnumerable[MethodInfo]: ...
    
    @staticmethod
    def GetRuntimeProperties(type: TypeType) -> IEnumerable[PropertyInfo]: ...
    
    @staticmethod
    def GetRuntimeProperty(type: TypeType, name: StringType) -> PropertyInfo: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class StrongNameKeyPair(ObjectType, IDeserializationCallback, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, keyPairFile: FileStream): ...
    
    @overload
    def __init__(self, keyPairArray: ArrayType[ByteType]): ...
    
    @overload
    def __init__(self, keyPairContainer: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def PublicKey(self) -> ArrayType[ByteType]: ...
    
    # ---------- Methods ---------- #
    
    def get_PublicKey(self) -> ArrayType[ByteType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TargetException(ApplicationException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, inner: Exception): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TargetInvocationException(ApplicationException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, inner: Exception): ...
    
    @overload
    def __init__(self, message: StringType, inner: Exception): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TargetParameterCountException(ApplicationException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, inner: Exception): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Throw(ABC, ObjectType):
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


class TypeDelegator(TypeInfo, ICustomAttributeProvider, _MemberInfo, _Type, IReflect, IReflectableType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, delegatingType: TypeType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Assembly(self) -> Assembly: ...
    
    @property
    def AssemblyQualifiedName(self) -> StringType: ...
    
    @property
    def BaseType(self) -> TypeType: ...
    
    @property
    def FullName(self) -> StringType: ...
    
    @property
    def GUID(self) -> Guid: ...
    
    @property
    def IsConstructedGenericType(self) -> BooleanType: ...
    
    @property
    def MetadataToken(self) -> IntType: ...
    
    @property
    def Module(self) -> Module: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def Namespace(self) -> StringType: ...
    
    @property
    def TypeHandle(self) -> RuntimeTypeHandle: ...
    
    @property
    def UnderlyingSystemType(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def GetConstructors(self, bindingAttr: BindingFlags) -> ArrayType[ConstructorInfo]: ...
    
    @overload
    def GetCustomAttributes(self, inherit: BooleanType) -> ArrayType[ObjectType]: ...
    
    @overload
    def GetCustomAttributes(self, attributeType: TypeType, inherit: BooleanType) -> ArrayType[ObjectType]: ...
    
    def GetElementType(self) -> TypeType: ...
    
    @overload
    def GetEvent(self, name: StringType, bindingAttr: BindingFlags) -> EventInfo: ...
    
    @overload
    def GetEvents(self) -> ArrayType[EventInfo]: ...
    
    @overload
    def GetEvents(self, bindingAttr: BindingFlags) -> ArrayType[EventInfo]: ...
    
    @overload
    def GetField(self, name: StringType, bindingAttr: BindingFlags) -> FieldInfo: ...
    
    @overload
    def GetFields(self, bindingAttr: BindingFlags) -> ArrayType[FieldInfo]: ...
    
    @overload
    def GetInterface(self, name: StringType, ignoreCase: BooleanType) -> TypeType: ...
    
    def GetInterfaceMap(self, interfaceType: TypeType) -> InterfaceMapping: ...
    
    def GetInterfaces(self) -> ArrayType[TypeType]: ...
    
    @overload
    def GetMember(self, name: StringType, type: MemberTypes, bindingAttr: BindingFlags) -> ArrayType[MemberInfo]: ...
    
    @overload
    def GetMembers(self, bindingAttr: BindingFlags) -> ArrayType[MemberInfo]: ...
    
    @overload
    def GetMethods(self, bindingAttr: BindingFlags) -> ArrayType[MethodInfo]: ...
    
    @overload
    def GetNestedType(self, name: StringType, bindingAttr: BindingFlags) -> TypeType: ...
    
    @overload
    def GetNestedTypes(self, bindingAttr: BindingFlags) -> ArrayType[TypeType]: ...
    
    @overload
    def GetProperties(self, bindingAttr: BindingFlags) -> ArrayType[PropertyInfo]: ...
    
    @overload
    def InvokeMember(self, name: StringType, invokeAttr: BindingFlags, binder: Binder, target: ObjectType, args: ArrayType[ObjectType], modifiers: ArrayType[ParameterModifier], culture: CultureInfo, namedParameters: ArrayType[StringType]) -> ObjectType: ...
    
    @overload
    def IsAssignableFrom(self, typeInfo: TypeInfo) -> BooleanType: ...
    
    def IsDefined(self, attributeType: TypeType, inherit: BooleanType) -> BooleanType: ...
    
    def get_Assembly(self) -> Assembly: ...
    
    def get_AssemblyQualifiedName(self) -> StringType: ...
    
    def get_BaseType(self) -> TypeType: ...
    
    def get_FullName(self) -> StringType: ...
    
    def get_GUID(self) -> Guid: ...
    
    def get_IsConstructedGenericType(self) -> BooleanType: ...
    
    def get_MetadataToken(self) -> IntType: ...
    
    @overload
    def get_Module(self) -> Module: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_Namespace(self) -> StringType: ...
    
    def get_TypeHandle(self) -> RuntimeTypeHandle: ...
    
    def get_UnderlyingSystemType(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TypeFilter(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, m: TypeType, filterCriteria: ObjectType, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> BooleanType: ...
    
    def Invoke(self, m: TypeType, filterCriteria: ObjectType) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TypeInfo(ABC, TypeType, ICustomAttributeProvider, _MemberInfo, _Type, IReflect, IReflectableType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def DeclaredConstructors(self) -> IEnumerable[ConstructorInfo]: ...
    
    @property
    def DeclaredEvents(self) -> IEnumerable[EventInfo]: ...
    
    @property
    def DeclaredFields(self) -> IEnumerable[FieldInfo]: ...
    
    @property
    def DeclaredMembers(self) -> IEnumerable[MemberInfo]: ...
    
    @property
    def DeclaredMethods(self) -> IEnumerable[MethodInfo]: ...
    
    @property
    def DeclaredNestedTypes(self) -> IEnumerable[TypeInfo]: ...
    
    @property
    def DeclaredProperties(self) -> IEnumerable[PropertyInfo]: ...
    
    @property
    def GenericTypeParameters(self) -> ArrayType[TypeType]: ...
    
    @property
    def ImplementedInterfaces(self) -> IEnumerable[TypeType]: ...
    
    # ---------- Methods ---------- #
    
    def AsType(self) -> TypeType: ...
    
    def GetDeclaredEvent(self, name: StringType) -> EventInfo: ...
    
    def GetDeclaredField(self, name: StringType) -> FieldInfo: ...
    
    def GetDeclaredMethod(self, name: StringType) -> MethodInfo: ...
    
    def GetDeclaredMethods(self, name: StringType) -> IEnumerable[MethodInfo]: ...
    
    def GetDeclaredNestedType(self, name: StringType) -> TypeInfo: ...
    
    def GetDeclaredProperty(self, name: StringType) -> PropertyInfo: ...
    
    @overload
    def IsAssignableFrom(self, typeInfo: TypeInfo) -> BooleanType: ...
    
    def get_DeclaredConstructors(self) -> IEnumerable[ConstructorInfo]: ...
    
    def get_DeclaredEvents(self) -> IEnumerable[EventInfo]: ...
    
    def get_DeclaredFields(self) -> IEnumerable[FieldInfo]: ...
    
    def get_DeclaredMembers(self) -> IEnumerable[MemberInfo]: ...
    
    def get_DeclaredMethods(self) -> IEnumerable[MethodInfo]: ...
    
    def get_DeclaredNestedTypes(self) -> IEnumerable[TypeInfo]: ...
    
    def get_DeclaredProperties(self) -> IEnumerable[PropertyInfo]: ...
    
    def get_GenericTypeParameters(self) -> ArrayType[TypeType]: ...
    
    def get_ImplementedInterfaces(self) -> IEnumerable[TypeType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class __Filters(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def FilterTypeName(self, cls: TypeType, filterCriteria: ObjectType) -> BooleanType: ...
    
    def FilterTypeNameIgnoreCase(self, cls: TypeType, filterCriteria: ObjectType) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# ---------- Structs ---------- #

class CerHashtable(Generic[K, V], ValueType):
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


class ConstArray(ValueType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    def __getitem__(self, key: IntType) -> ByteType: ...
    
    @property
    def Length(self) -> IntType: ...
    
    @property
    def Signature(self) -> NIntType: ...
    
    # ---------- Methods ---------- #
    
    def get_Item(self, index: IntType) -> ByteType: ...
    
    def get_Length(self) -> IntType: ...
    
    def get_Signature(self) -> NIntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CustomAttributeCtorParameter(ValueType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, type: CustomAttributeType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CustomAttributeEncodedArgument(self) -> CustomAttributeEncodedArgument: ...
    
    # ---------- Methods ---------- #
    
    def get_CustomAttributeEncodedArgument(self) -> CustomAttributeEncodedArgument: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CustomAttributeEncodedArgument(ValueType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def ArrayValue(self) -> ArrayType[CustomAttributeEncodedArgument]: ...
    
    @property
    def CustomAttributeType(self) -> CustomAttributeType: ...
    
    @property
    def PrimitiveValue(self) -> LongType: ...
    
    @property
    def StringValue(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_ArrayValue(self) -> ArrayType[CustomAttributeEncodedArgument]: ...
    
    def get_CustomAttributeType(self) -> CustomAttributeType: ...
    
    def get_PrimitiveValue(self) -> LongType: ...
    
    def get_StringValue(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CustomAttributeNamedArgument(ValueType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, memberInfo: MemberInfo, value: ObjectType): ...
    
    @overload
    def __init__(self, memberInfo: MemberInfo, typedArgument: CustomAttributeTypedArgument): ...
    
    # ---------- Properties ---------- #
    
    @property
    def IsField(self) -> BooleanType: ...
    
    @property
    def MemberInfo(self) -> MemberInfo: ...
    
    @property
    def MemberName(self) -> StringType: ...
    
    @property
    def TypedValue(self) -> CustomAttributeTypedArgument: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_IsField(self) -> BooleanType: ...
    
    def get_MemberInfo(self) -> MemberInfo: ...
    
    def get_MemberName(self) -> StringType: ...
    
    def get_TypedValue(self) -> CustomAttributeTypedArgument: ...
    
    @staticmethod
    def op_Equality(left: CustomAttributeNamedArgument, right: CustomAttributeNamedArgument) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(left: CustomAttributeNamedArgument, right: CustomAttributeNamedArgument) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CustomAttributeNamedParameter(ValueType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, argumentName: StringType, fieldOrProperty: CustomAttributeEncoding, type: CustomAttributeType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def EncodedArgument(self) -> CustomAttributeEncodedArgument: ...
    
    # ---------- Methods ---------- #
    
    def get_EncodedArgument(self) -> CustomAttributeEncodedArgument: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CustomAttributeRecord(ValueType):
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


class CustomAttributeType(ValueType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, encodedType: CustomAttributeEncoding, encodedArrayType: CustomAttributeEncoding, encodedEnumType: CustomAttributeEncoding, enumName: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def EncodedArrayType(self) -> CustomAttributeEncoding: ...
    
    @property
    def EncodedEnumType(self) -> CustomAttributeEncoding: ...
    
    @property
    def EncodedType(self) -> CustomAttributeEncoding: ...
    
    @property
    def EnumName(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_EncodedArrayType(self) -> CustomAttributeEncoding: ...
    
    def get_EncodedEnumType(self) -> CustomAttributeEncoding: ...
    
    def get_EncodedType(self) -> CustomAttributeEncoding: ...
    
    def get_EnumName(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CustomAttributeTypedArgument(ValueType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, argumentType: TypeType, value: ObjectType): ...
    
    @overload
    def __init__(self, value: ObjectType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ArgumentType(self) -> TypeType: ...
    
    @property
    def Value(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_ArgumentType(self) -> TypeType: ...
    
    def get_Value(self) -> ObjectType: ...
    
    @staticmethod
    def op_Equality(left: CustomAttributeTypedArgument, right: CustomAttributeTypedArgument) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(left: CustomAttributeTypedArgument, right: CustomAttributeTypedArgument) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class InterfaceMapping(ValueType):
    # ---------- Fields ---------- #
    
    @property
    def InterfaceMethods(self) -> ArrayType[MethodInfo]: ...
    
    @InterfaceMethods.setter
    def InterfaceMethods(self, value: ArrayType[MethodInfo]) -> None: ...
    
    @property
    def InterfaceType(self) -> TypeType: ...
    
    @InterfaceType.setter
    def InterfaceType(self, value: TypeType) -> None: ...
    
    @property
    def TargetMethods(self) -> ArrayType[MethodInfo]: ...
    
    @TargetMethods.setter
    def TargetMethods(self, value: ArrayType[MethodInfo]) -> None: ...
    
    @property
    def TargetType(self) -> TypeType: ...
    
    @TargetType.setter
    def TargetType(self, value: TypeType) -> None: ...
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MetadataEnumResult(ValueType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    def __getitem__(self, key: IntType) -> IntType: ...
    
    @property
    def Length(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def get_Item(self, index: IntType) -> IntType: ...
    
    def get_Length(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # ---------- Sub Structs ---------- #
    
    class <smallResult>e__FixedBuffer(ValueType):
        # ---------- Fields ---------- #
        
        @property
        def FixedElementField(self) -> IntType: ...
        
        @FixedElementField.setter
        def FixedElementField(self, value: IntType) -> None: ...
        
        # No Constructors
        
        # No Properties
        
        # No Methods
        
        # No Events
        
        # No Sub Classes
        
        # No Sub Structs
        
        # No Sub Interfaces
        
        # No Sub Enums
    
    
    # No Sub Interfaces
    
    # No Sub Enums


class MetadataImport(ValueType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Enum(self, type: MetadataTokenType, parent: IntType, result: MetadataEnumResult) -> Tuple[VoidType, MetadataEnumResult]: ...
    
    def EnumCustomAttributes(self, mdToken: IntType, result: MetadataEnumResult) -> Tuple[VoidType, MetadataEnumResult]: ...
    
    def EnumEvents(self, mdTypeDef: IntType, result: MetadataEnumResult) -> Tuple[VoidType, MetadataEnumResult]: ...
    
    def EnumFields(self, mdTypeDef: IntType, result: MetadataEnumResult) -> Tuple[VoidType, MetadataEnumResult]: ...
    
    def EnumNestedTypes(self, mdTypeDef: IntType, result: MetadataEnumResult) -> Tuple[VoidType, MetadataEnumResult]: ...
    
    def EnumParams(self, mdMethodDef: IntType, result: MetadataEnumResult) -> Tuple[VoidType, MetadataEnumResult]: ...
    
    def EnumProperties(self, mdTypeDef: IntType, result: MetadataEnumResult) -> Tuple[VoidType, MetadataEnumResult]: ...
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetClassLayout(self, typeTokenDef: IntType, packSize: IntType, classSize: IntType) -> Tuple[VoidType, IntType, IntType]: ...
    
    def GetCustomAttributeProps(self, customAttributeToken: IntType, constructorToken: IntType, signature: ConstArray) -> Tuple[VoidType, IntType, ConstArray]: ...
    
    def GetDefaultValue(self, mdToken: IntType, value: LongType, length: IntType, corElementType: CorElementType) -> Tuple[StringType, LongType, IntType, CorElementType]: ...
    
    def GetEventProps(self, mdToken: IntType, name: VoidType, eventAttributes: EventAttributes) -> Tuple[VoidType, VoidType, EventAttributes]: ...
    
    def GetFieldDefProps(self, mdToken: IntType, fieldAttributes: FieldAttributes) -> Tuple[VoidType, FieldAttributes]: ...
    
    def GetFieldMarshal(self, fieldToken: IntType) -> ConstArray: ...
    
    def GetFieldOffset(self, typeTokenDef: IntType, fieldTokenDef: IntType, offset: IntType) -> Tuple[BooleanType, IntType]: ...
    
    def GetGenericParamProps(self, genericParameter: IntType, attributes: GenericParameterAttributes) -> Tuple[VoidType, GenericParameterAttributes]: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def GetMemberRefProps(self, memberTokenRef: IntType) -> ConstArray: ...
    
    def GetMethodSignature(self, token: MetadataToken) -> ConstArray: ...
    
    def GetName(self, mdToken: IntType) -> Utf8String: ...
    
    def GetNamespace(self, mdToken: IntType) -> Utf8String: ...
    
    def GetPInvokeMap(self, token: IntType, attributes: PInvokeAttributes, importName: StringType, importDll: StringType) -> Tuple[VoidType, PInvokeAttributes, StringType, StringType]: ...
    
    def GetParamDefProps(self, parameterToken: IntType, sequence: IntType, attributes: ParameterAttributes) -> Tuple[VoidType, IntType, ParameterAttributes]: ...
    
    def GetParentToken(self, tkToken: IntType) -> IntType: ...
    
    def GetPropertyProps(self, mdToken: IntType, name: VoidType, propertyAttributes: PropertyAttributes, signature: ConstArray) -> Tuple[VoidType, VoidType, PropertyAttributes, ConstArray]: ...
    
    def GetScopeProps(self, mvid: Guid) -> Tuple[VoidType, Guid]: ...
    
    def GetSigOfFieldDef(self, fieldToken: IntType) -> ConstArray: ...
    
    def GetSigOfMethodDef(self, methodToken: IntType) -> ConstArray: ...
    
    def GetSignatureFromToken(self, token: IntType) -> ConstArray: ...
    
    def GetUserString(self, mdToken: IntType) -> StringType: ...
    
    def IsValidToken(self, token: IntType) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MetadataToken(ValueType):
    # ---------- Fields ---------- #
    
    @property
    def Value(self) -> IntType: ...
    
    @Value.setter
    def Value(self, value: IntType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self, token: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def IsAssembly(self) -> BooleanType: ...
    
    @property
    def IsEvent(self) -> BooleanType: ...
    
    @property
    def IsFieldDef(self) -> BooleanType: ...
    
    @property
    def IsGenericPar(self) -> BooleanType: ...
    
    @property
    def IsGlobalTypeDefToken(self) -> BooleanType: ...
    
    @property
    def IsMemberRef(self) -> BooleanType: ...
    
    @property
    def IsMethodDef(self) -> BooleanType: ...
    
    @property
    def IsMethodSpec(self) -> BooleanType: ...
    
    @property
    def IsModule(self) -> BooleanType: ...
    
    @property
    def IsParamDef(self) -> BooleanType: ...
    
    @property
    def IsProperty(self) -> BooleanType: ...
    
    @property
    def IsSignature(self) -> BooleanType: ...
    
    @property
    def IsString(self) -> BooleanType: ...
    
    @property
    def IsTypeDef(self) -> BooleanType: ...
    
    @property
    def IsTypeRef(self) -> BooleanType: ...
    
    @property
    def IsTypeSpec(self) -> BooleanType: ...
    
    @property
    def TokenType(self) -> MetadataTokenType: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def IsNullToken(token: IntType) -> BooleanType: ...
    
    @staticmethod
    def IsTokenOfType(token: IntType, types: ArrayType[MetadataTokenType]) -> BooleanType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_IsAssembly(self) -> BooleanType: ...
    
    def get_IsEvent(self) -> BooleanType: ...
    
    def get_IsFieldDef(self) -> BooleanType: ...
    
    def get_IsGenericPar(self) -> BooleanType: ...
    
    def get_IsGlobalTypeDefToken(self) -> BooleanType: ...
    
    def get_IsMemberRef(self) -> BooleanType: ...
    
    def get_IsMethodDef(self) -> BooleanType: ...
    
    def get_IsMethodSpec(self) -> BooleanType: ...
    
    def get_IsModule(self) -> BooleanType: ...
    
    def get_IsParamDef(self) -> BooleanType: ...
    
    def get_IsProperty(self) -> BooleanType: ...
    
    def get_IsSignature(self) -> BooleanType: ...
    
    def get_IsString(self) -> BooleanType: ...
    
    def get_IsTypeDef(self) -> BooleanType: ...
    
    def get_IsTypeRef(self) -> BooleanType: ...
    
    def get_IsTypeSpec(self) -> BooleanType: ...
    
    def get_TokenType(self) -> MetadataTokenType: ...
    
    @staticmethod
    @overload
    def op_Implicit(token: MetadataToken) -> IntType: ...
    
    @staticmethod
    @overload
    def op_Implicit(token: IntType) -> MetadataToken: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ParameterModifier(ValueType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, parameterCount: IntType): ...
    
    # ---------- Properties ---------- #
    
    def __getitem__(self, key: IntType) -> BooleanType: ...
    
    def __setitem__(self, key: IntType, value: BooleanType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Item(self, index: IntType) -> BooleanType: ...
    
    def set_Item(self, index: IntType, value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SecurityContextFrame(ValueType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Pop(self) -> VoidType: ...
    
    def Push(self, assembly: RuntimeAssembly) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# ---------- Interfaces ---------- #

class ICustomAttributeProvider(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def GetCustomAttributes(self, attributeType: TypeType, inherit: BooleanType) -> ArrayType[ObjectType]: ...
    
    @overload
    def GetCustomAttributes(self, inherit: BooleanType) -> ArrayType[ObjectType]: ...
    
    def IsDefined(self, attributeType: TypeType, inherit: BooleanType) -> BooleanType: ...
    
    # No Events


class ICustomTypeProvider(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetCustomType(self) -> TypeType: ...
    
    # No Events


class IReflect(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def UnderlyingSystemType(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def GetField(self, name: StringType, bindingAttr: BindingFlags) -> FieldInfo: ...
    
    def GetFields(self, bindingAttr: BindingFlags) -> ArrayType[FieldInfo]: ...
    
    def GetMember(self, name: StringType, bindingAttr: BindingFlags) -> ArrayType[MemberInfo]: ...
    
    def GetMembers(self, bindingAttr: BindingFlags) -> ArrayType[MemberInfo]: ...
    
    @overload
    def GetMethod(self, name: StringType, bindingAttr: BindingFlags, binder: Binder, types: ArrayType[TypeType], modifiers: ArrayType[ParameterModifier]) -> MethodInfo: ...
    
    @overload
    def GetMethod(self, name: StringType, bindingAttr: BindingFlags) -> MethodInfo: ...
    
    def GetMethods(self, bindingAttr: BindingFlags) -> ArrayType[MethodInfo]: ...
    
    def GetProperties(self, bindingAttr: BindingFlags) -> ArrayType[PropertyInfo]: ...
    
    @overload
    def GetProperty(self, name: StringType, bindingAttr: BindingFlags) -> PropertyInfo: ...
    
    @overload
    def GetProperty(self, name: StringType, bindingAttr: BindingFlags, binder: Binder, returnType: TypeType, types: ArrayType[TypeType], modifiers: ArrayType[ParameterModifier]) -> PropertyInfo: ...
    
    def InvokeMember(self, name: StringType, invokeAttr: BindingFlags, binder: Binder, target: ObjectType, args: ArrayType[ObjectType], modifiers: ArrayType[ParameterModifier], culture: CultureInfo, namedParameters: ArrayType[StringType]) -> ObjectType: ...
    
    def get_UnderlyingSystemType(self) -> TypeType: ...
    
    # No Events


class IReflectableType(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetTypeInfo(self) -> TypeInfo: ...
    
    # No Events


# ---------- Enums ---------- #

class AssemblyContentType(Enum):
    Default = 0
    WindowsRuntime = 1


class AssemblyNameFlags(Enum):
    #None = 0
    PublicKey = 1
    Retargetable = 256
    EnableJITcompileOptimizer = 16384
    EnableJITcompileTracking = 32768


class BindingFlags(Enum):
    Default = 0
    IgnoreCase = 1
    DeclaredOnly = 2
    Instance = 4
    Static = 8
    Public = 16
    NonPublic = 32
    FlattenHierarchy = 64
    InvokeMethod = 256
    CreateInstance = 512
    GetField = 1024
    SetField = 2048
    GetProperty = 4096
    SetProperty = 8192
    PutDispProperty = 16384
    PutRefDispProperty = 32768
    ExactBinding = 65536
    SuppressChangeType = 131072
    OptionalParamBinding = 262144
    IgnoreReturn = 16777216


class CallingConventions(Enum):
    Standard = 1
    VarArgs = 2
    Any = 3
    HasThis = 32
    ExplicitThis = 64


class CorElementType(Enum):
    End = 0
    Void = 1
    Boolean = 2
    Char = 3
    I1 = 4
    U1 = 5
    I2 = 6
    U2 = 7
    I4 = 8
    U4 = 9
    I8 = 10
    U8 = 11
    R4 = 12
    R8 = 13
    String = 14
    Ptr = 15
    ByRef = 16
    ValueType = 17
    Class = 18
    Var = 19
    Array = 20
    GenericInst = 21
    TypedByRef = 22
    I = 24
    U = 25
    FnPtr = 27
    Object = 28
    SzArray = 29
    MVar = 30
    CModReqd = 31
    CModOpt = 32
    Internal = 33
    Max = 34
    Modifier = 64
    Sentinel = 65
    Pinned = 69


class CustomAttributeEncoding(Enum):
    Undefined = 0
    Boolean = 2
    Char = 3
    SByte = 4
    Byte = 5
    Int16 = 6
    UInt16 = 7
    Int32 = 8
    UInt32 = 9
    Int64 = 10
    UInt64 = 11
    Float = 12
    Double = 13
    String = 14
    Array = 29
    Type = 80
    Object = 81
    Field = 83
    Property = 84
    Enum = 85


class EventAttributes(Enum):
    #None = 0
    SpecialName = 512
    ReservedMask = 1024
    RTSpecialName = 1024


class ExceptionHandlingClauseOptions(Enum):
    Clause = 0
    Filter = 1
    Finally = 2
    Fault = 4


class FieldAttributes(Enum):
    PrivateScope = 0
    Private = 1
    FamANDAssem = 2
    Assembly = 3
    Family = 4
    FamORAssem = 5
    Public = 6
    FieldAccessMask = 7
    Static = 16
    InitOnly = 32
    Literal = 64
    NotSerialized = 128
    HasFieldRVA = 256
    SpecialName = 512
    RTSpecialName = 1024
    HasFieldMarshal = 4096
    PinvokeImpl = 8192
    HasDefault = 32768
    ReservedMask = 38144


class GenericParameterAttributes(Enum):
    #None = 0
    Covariant = 1
    Contravariant = 2
    VarianceMask = 3
    ReferenceTypeConstraint = 4
    NotNullableValueTypeConstraint = 8
    DefaultConstructorConstraint = 16
    SpecialConstraintMask = 28


class INVOCATION_FLAGS(Enum):
    INVOCATION_FLAGS_UNKNOWN = 0
    INVOCATION_FLAGS_INITIALIZED = 1
    INVOCATION_FLAGS_NO_INVOKE = 2
    INVOCATION_FLAGS_NEED_SECURITY = 4
    INVOCATION_FLAGS_NO_CTOR_INVOKE = 8
    INVOCATION_FLAGS_IS_CTOR = 16
    INVOCATION_FLAGS_SPECIAL_FIELD = 16
    INVOCATION_FLAGS_RISKY_METHOD = 32
    INVOCATION_FLAGS_FIELD_SPECIAL_CAST = 32
    INVOCATION_FLAGS_NON_W8P_FX_API = 64
    INVOCATION_FLAGS_IS_DELEGATE_CTOR = 128
    INVOCATION_FLAGS_CONTAINS_STACK_POINTERS = 256
    INVOCATION_FLAGS_CONSTRUCTOR_INVOKE = 268435456


class ImageFileMachine(Enum):
    I386 = 332
    ARM = 452
    IA64 = 512
    AMD64 = 34404


class LoadContext(Enum):
    DEFAULT = 0
    LOADFROM = 1
    UNKNOWN = 2
    HOSTED = 3


class MdSigCallingConvention(Enum):
    Default = 0
    C = 1
    StdCall = 2
    ThisCall = 3
    FastCall = 4
    Vararg = 5
    Field = 6
    LocalSig = 7
    Property = 8
    Unmgd = 9
    GenericInst = 10
    CallConvMask = 15
    Generic = 16
    HasThis = 32
    ExplicitThis = 64


class MemberTypes(Enum):
    Constructor = 1
    Event = 2
    Field = 4
    Method = 8
    Property = 16
    TypeInfo = 32
    Custom = 64
    NestedType = 128
    All = 191


class MetadataTokenType(Enum):
    Module = 0
    TypeRef = 16777216
    TypeDef = 33554432
    FieldDef = 67108864
    MethodDef = 100663296
    ParamDef = 134217728
    InterfaceImpl = 150994944
    MemberRef = 167772160
    CustomAttribute = 201326592
    Permission = 234881024
    Signature = 285212672
    Event = 335544320
    Property = 385875968
    ModuleRef = 436207616
    TypeSpec = 452984832
    Assembly = 536870912
    AssemblyRef = 587202560
    File = 637534208
    ExportedType = 654311424
    ManifestResource = 671088640
    GenericPar = 704643072
    MethodSpec = 721420288
    String = 1879048192
    Name = 1895825408
    BaseType = 1912602624
    Invalid = 2147483647


class MethodAttributes(Enum):
    ReuseSlot = 0
    PrivateScope = 0
    Private = 1
    FamANDAssem = 2
    Assembly = 3
    Family = 4
    FamORAssem = 5
    Public = 6
    MemberAccessMask = 7
    UnmanagedExport = 8
    Static = 16
    Final = 32
    Virtual = 64
    HideBySig = 128
    NewSlot = 256
    VtableLayoutMask = 256
    CheckAccessOnOverride = 512
    Abstract = 1024
    SpecialName = 2048
    RTSpecialName = 4096
    PinvokeImpl = 8192
    HasSecurity = 16384
    RequireSecObject = 32768
    ReservedMask = 53248


class MethodImplAttributes(Enum):
    IL = 0
    Managed = 0
    Native = 1
    OPTIL = 2
    Runtime = 3
    CodeTypeMask = 3
    Unmanaged = 4
    ManagedMask = 4
    NoInlining = 8
    ForwardRef = 16
    Synchronized = 32
    NoOptimization = 64
    PreserveSig = 128
    AggressiveInlining = 256
    SecurityMitigations = 1024
    InternalCall = 4096
    MaxMethodImplVal = 65535


class MethodSemanticsAttributes(Enum):
    Setter = 1
    Getter = 2
    Other = 4
    AddOn = 8
    RemoveOn = 16
    Fire = 32


class PInvokeAttributes(Enum):
    ThrowOnUnmappableCharUseAssem = 0
    CharSetNotSpec = 0
    BestFitUseAssem = 0
    NoMangle = 1
    CharSetAnsi = 2
    CharSetUnicode = 4
    CharSetAuto = 6
    CharSetMask = 6
    BestFitEnabled = 16
    BestFitDisabled = 32
    BestFitMask = 48
    SupportsLastError = 64
    CallConvWinapi = 256
    CallConvCdecl = 512
    CallConvStdcall = 768
    CallConvThiscall = 1024
    CallConvFastcall = 1280
    CallConvMask = 1792
    ThrowOnUnmappableCharEnabled = 4096
    ThrowOnUnmappableCharDisabled = 8192
    ThrowOnUnmappableCharMask = 12288
    MaxValue = 65535


class ParameterAttributes(Enum):
    #None = 0
    In = 1
    Out = 2
    Lcid = 4
    Retval = 8
    Optional = 16
    HasDefault = 4096
    HasFieldMarshal = 8192
    Reserved3 = 16384
    Reserved4 = 32768
    ReservedMask = 61440


class PortableExecutableKinds(Enum):
    NotAPortableExecutableImage = 0
    ILOnly = 1
    Required32Bit = 2
    PE32Plus = 4
    Unmanaged32Bit = 8
    Preferred32Bit = 16


class ProcessorArchitecture(Enum):
    #None = 0
    MSIL = 1
    X86 = 2
    IA64 = 3
    Amd64 = 4
    Arm = 5


class PropertyAttributes(Enum):
    #None = 0
    SpecialName = 512
    RTSpecialName = 1024
    HasDefault = 4096
    Reserved2 = 8192
    Reserved3 = 16384
    Reserved4 = 32768
    ReservedMask = 62464


class ResourceAttributes(Enum):
    Public = 1
    Private = 2


class ResourceLocation(Enum):
    Embedded = 1
    ContainedInAnotherAssembly = 2
    ContainedInManifestFile = 4


class TypeAttributes(Enum):
    NotPublic = 0
    AutoLayout = 0
    AnsiClass = 0
    Class = 0
    Public = 1
    NestedPublic = 2
    NestedPrivate = 3
    NestedFamily = 4
    NestedAssembly = 5
    NestedFamANDAssem = 6
    NestedFamORAssem = 7
    VisibilityMask = 7
    SequentialLayout = 8
    ExplicitLayout = 16
    LayoutMask = 24
    Interface = 32
    ClassSemanticsMask = 32
    Abstract = 128
    Sealed = 256
    SpecialName = 1024
    RTSpecialName = 2048
    Import = 4096
    Serializable = 8192
    WindowsRuntime = 16384
    UnicodeClass = 65536
    AutoClass = 131072
    StringFormatMask = 196608
    CustomFormatClass = 196608
    HasSecurity = 262144
    ReservedMask = 264192
    BeforeFieldInit = 1048576
    CustomFormatMask = 12582912


# ---------- Delegates ---------- #

MemberFilter = Callable[[MemberInfo, ObjectType], BooleanType]

ModuleResolveEventHandler = Callable[[ObjectType, ResolveEventArgs], Module]

TypeFilter = Callable[[TypeType, ObjectType], BooleanType]

__all__ = [
    AmbiguousMatchException,
    Assembly,
    AssemblyAlgorithmIdAttribute,
    AssemblyCompanyAttribute,
    AssemblyConfigurationAttribute,
    AssemblyCopyrightAttribute,
    AssemblyCultureAttribute,
    AssemblyDefaultAliasAttribute,
    AssemblyDelaySignAttribute,
    AssemblyDescriptionAttribute,
    AssemblyFileVersionAttribute,
    AssemblyFlagsAttribute,
    AssemblyInformationalVersionAttribute,
    AssemblyKeyFileAttribute,
    AssemblyKeyNameAttribute,
    AssemblyMetadataAttribute,
    AssemblyName,
    AssemblyNameProxy,
    AssemblyProductAttribute,
    AssemblySignatureKeyAttribute,
    AssemblyTitleAttribute,
    AssemblyTrademarkAttribute,
    AssemblyVersionAttribute,
    Associates,
    Binder,
    BlobUtilities,
    ConstructorInfo,
    CustomAttribute,
    CustomAttributeData,
    CustomAttributeExtensions,
    CustomAttributeFormatException,
    DefaultMemberAttribute,
    EventInfo,
    ExceptionHandlingClause,
    FieldInfo,
    IntrospectionExtensions,
    InvalidFilterCriteriaException,
    LoaderAllocator,
    LoaderAllocatorScout,
    LocalVariableInfo,
    ManifestResourceInfo,
    MdConstant,
    MdFieldInfo,
    MemberFilter,
    MemberInfo,
    MemberInfoSerializationHolder,
    MetadataException,
    MethodBase,
    MethodBody,
    MethodInfo,
    Missing,
    Module,
    ModuleResolveEventHandler,
    ObfuscateAssemblyAttribute,
    ObfuscationAttribute,
    ParameterInfo,
    Pointer,
    PropertyInfo,
    PseudoCustomAttribute,
    ReflectionContext,
    ReflectionTypeLoadException,
    RtFieldInfo,
    RuntimeAssembly,
    RuntimeConstructorInfo,
    RuntimeEventInfo,
    RuntimeFieldInfo,
    RuntimeMethodInfo,
    RuntimeModule,
    RuntimeParameterInfo,
    RuntimePropertyInfo,
    RuntimeReflectionExtensions,
    StrongNameKeyPair,
    TargetException,
    TargetInvocationException,
    TargetParameterCountException,
    Throw,
    TypeDelegator,
    TypeFilter,
    TypeInfo,
    __Filters,
    CerHashtable,
    ConstArray,
    CustomAttributeCtorParameter,
    CustomAttributeEncodedArgument,
    CustomAttributeNamedArgument,
    CustomAttributeNamedParameter,
    CustomAttributeRecord,
    CustomAttributeType,
    CustomAttributeTypedArgument,
    InterfaceMapping,
    MetadataEnumResult,
    MetadataImport,
    MetadataToken,
    ParameterModifier,
    SecurityContextFrame,
    ICustomAttributeProvider,
    ICustomTypeProvider,
    IReflect,
    IReflectableType,
    AssemblyContentType,
    AssemblyNameFlags,
    BindingFlags,
    CallingConventions,
    CorElementType,
    CustomAttributeEncoding,
    EventAttributes,
    ExceptionHandlingClauseOptions,
    FieldAttributes,
    GenericParameterAttributes,
    INVOCATION_FLAGS,
    ImageFileMachine,
    LoadContext,
    MdSigCallingConvention,
    MemberTypes,
    MetadataTokenType,
    MethodAttributes,
    MethodImplAttributes,
    MethodSemanticsAttributes,
    PInvokeAttributes,
    ParameterAttributes,
    PortableExecutableKinds,
    ProcessorArchitecture,
    PropertyAttributes,
    ResourceAttributes,
    ResourceLocation,
    TypeAttributes,
    MemberFilter,
    ModuleResolveEventHandler,
    TypeFilter,
]
