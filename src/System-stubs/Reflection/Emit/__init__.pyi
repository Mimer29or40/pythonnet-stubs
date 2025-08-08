"""Automatically generated stubs for C# namespace: System.Reflection.Emit."""

from typing import ClassVar
from typing import Self
from typing import overload

from System import Array
from System import Delegate
from System import Enum
from System import Guid
from System import IEquatable
from System import IntPtr
from System import ModuleHandle
from System import Object
from System import Resolver
from System import RuntimeFieldHandle
from System import RuntimeMethodHandle
from System import RuntimeTypeHandle
from System import Type
from System import TypedReference
from System import UInt32
from System import ValueType
from System import Version
from System.Collections.Generic import IEnumerable
from System.Collections.Generic import IList
from System.Diagnostics.SymbolStore import ISymbolDocumentWriter
from System.Diagnostics.SymbolStore import ISymbolWriter
from System.Globalization import CultureInfo
from System.IO import FileStream
from System.IO import Stream
from System.Reflection import Assembly
from System.Reflection import AssemblyName
from System.Reflection import Binder
from System.Reflection import BindingFlags
from System.Reflection import CallingConventions
from System.Reflection import ConstructorInfo
from System.Reflection import CustomAttributeData
from System.Reflection import EventAttributes
from System.Reflection import EventInfo
from System.Reflection import ExceptionHandlingClauseOptions
from System.Reflection import FieldAttributes
from System.Reflection import FieldInfo
from System.Reflection import GenericParameterAttributes
from System.Reflection import ICustomAttributeProvider
from System.Reflection import ImageFileMachine
from System.Reflection import InterfaceMapping
from System.Reflection import IReflect
from System.Reflection import IReflectableType
from System.Reflection import LocalVariableInfo
from System.Reflection import ManifestResourceInfo
from System.Reflection import MemberFilter
from System.Reflection import MemberInfo
from System.Reflection import MemberTypes
from System.Reflection import MethodAttributes
from System.Reflection import MethodBase
from System.Reflection import MethodBody
from System.Reflection import MethodImplAttributes
from System.Reflection import MethodInfo
from System.Reflection import Module
from System.Reflection import ModuleResolveEventHandler
from System.Reflection import ParameterAttributes
from System.Reflection import ParameterInfo
from System.Reflection import ParameterModifier
from System.Reflection import PortableExecutableKinds
from System.Reflection import PropertyAttributes
from System.Reflection import PropertyInfo
from System.Reflection import ResourceAttributes
from System.Reflection import RuntimeAssembly
from System.Reflection import RuntimeModule
from System.Reflection import TypeAttributes
from System.Reflection import TypeFilter
from System.Reflection import TypeInfo
from System.Resources import IResourceWriter
from System.Runtime.InteropServices import CallingConvention
from System.Runtime.InteropServices import CharSet
from System.Runtime.InteropServices import CustomQueryInterfaceResult
from System.Runtime.InteropServices import ICustomQueryInterface
from System.Runtime.InteropServices import StructLayoutAttribute
from System.Runtime.InteropServices import UnmanagedType
from System.Runtime.InteropServices import _Assembly
from System.Runtime.InteropServices import _AssemblyBuilder
from System.Runtime.InteropServices import _ConstructorBuilder
from System.Runtime.InteropServices import _ConstructorInfo
from System.Runtime.InteropServices import _CustomAttributeBuilder
from System.Runtime.InteropServices import _EnumBuilder
from System.Runtime.InteropServices import _EventBuilder
from System.Runtime.InteropServices import _FieldBuilder
from System.Runtime.InteropServices import _FieldInfo
from System.Runtime.InteropServices import _ILGenerator
from System.Runtime.InteropServices import _LocalBuilder
from System.Runtime.InteropServices import _MemberInfo
from System.Runtime.InteropServices import _MethodBase
from System.Runtime.InteropServices import _MethodBuilder
from System.Runtime.InteropServices import _MethodInfo
from System.Runtime.InteropServices import _MethodRental
from System.Runtime.InteropServices import _Module
from System.Runtime.InteropServices import _ModuleBuilder
from System.Runtime.InteropServices import _ParameterBuilder
from System.Runtime.InteropServices import _PropertyBuilder
from System.Runtime.InteropServices import _PropertyInfo
from System.Runtime.InteropServices import _SignatureHelper
from System.Runtime.InteropServices import _Type
from System.Runtime.InteropServices import _TypeBuilder
from System.Runtime.Serialization import ISerializable
from System.Runtime.Serialization import SerializationInfo
from System.Runtime.Serialization import StreamingContext
from System.Security import IEvidenceFactory
from System.Security import PermissionSet
from System.Security import SecurityRuleSet
from System.Security.Cryptography.X509Certificates import X509Certificate
from System.Security.Permissions import SecurityAction
from System.Security.Policy import Evidence

class EventType[T]:
    def __iadd__(self, other: T) -> Self: ...
    def __isub__(self, other: T) -> Self: ...

class AssemblyBuilder(
    Assembly, ICustomAttributeProvider, _Assembly, _AssemblyBuilder, ISerializable, IEvidenceFactory
):
    """"""
    @property
    def CodeBase(self) -> str:
        """"""
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
        """"""
    @property
    def DefinedTypes(self) -> IEnumerable[TypeInfo]:
        """"""
    @property
    def EntryPoint(self) -> MethodInfo:
        """"""
    @property
    def EscapedCodeBase(self) -> str:
        """"""
    @property
    def Evidence(self) -> Evidence:
        """"""
    @property
    def ExportedTypes(self) -> IEnumerable[Type]:
        """"""
    @property
    def FullName(self) -> str:
        """"""
    @property
    def GlobalAssemblyCache(self) -> bool:
        """"""
    @property
    def HostContext(self) -> int:
        """"""
    @property
    def ImageRuntimeVersion(self) -> str:
        """"""
    @property
    def IsDynamic(self) -> bool:
        """"""
    @property
    def IsFullyTrusted(self) -> bool:
        """"""
    @property
    def Location(self) -> str:
        """"""
    @property
    def ManifestModule(self) -> Module:
        """"""
    @property
    def Modules(self) -> IEnumerable[Module]:
        """"""
    @property
    def PermissionSet(self) -> PermissionSet:
        """"""
    @property
    def ReflectionOnly(self) -> bool:
        """"""
    @property
    def SecurityRuleSet(self) -> SecurityRuleSet:
        """"""
    @overload
    def AddResourceFile(self, name: str, fileName: str) -> None:
        """"""
    @overload
    def AddResourceFile(self, name: str, fileName: str, attribute: ResourceAttributes) -> None:
        """"""
    @overload
    def CreateInstance(self, typeName: str) -> object:
        """"""
    @overload
    def CreateInstance(self, typeName: str, ignoreCase: bool) -> object:
        """"""
    @overload
    def CreateInstance(
        self,
        typeName: str,
        ignoreCase: bool,
        bindingAttr: BindingFlags,
        binder: Binder,
        args: Array[object],
        culture: CultureInfo,
        activationAttributes: Array[object],
    ) -> object:
        """"""
    @classmethod
    @overload
    def DefineDynamicAssembly(
        cls, name: AssemblyName, access: AssemblyBuilderAccess
    ) -> AssemblyBuilder:
        """"""
    @classmethod
    @overload
    def DefineDynamicAssembly(
        cls,
        name: AssemblyName,
        access: AssemblyBuilderAccess,
        assemblyAttributes: IEnumerable[CustomAttributeBuilder],
    ) -> AssemblyBuilder:
        """"""
    @overload
    def DefineDynamicModule(self, name: str) -> ModuleBuilder:
        """"""
    @overload
    def DefineDynamicModule(self, name: str, emitSymbolInfo: bool) -> ModuleBuilder:
        """"""
    @overload
    def DefineDynamicModule(self, name: str, fileName: str) -> ModuleBuilder:
        """"""
    @overload
    def DefineDynamicModule(self, name: str, fileName: str, emitSymbolInfo: bool) -> ModuleBuilder:
        """"""
    @overload
    def DefineResource(self, name: str, description: str, fileName: str) -> IResourceWriter:
        """"""
    @overload
    def DefineResource(
        self, name: str, description: str, fileName: str, attribute: ResourceAttributes
    ) -> IResourceWriter:
        """"""
    @overload
    def DefineUnmanagedResource(self, resource: Array[int]) -> None:
        """"""
    @overload
    def DefineUnmanagedResource(self, resourceFileName: str) -> None:
        """"""
    @overload
    def DefineVersionInfoResource(self) -> None:
        """"""
    @overload
    def DefineVersionInfoResource(
        self, product: str, productVersion: str, company: str, copyright: str, trademark: str
    ) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """"""
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """"""
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]:
        """"""
    def GetDynamicModule(self, name: str) -> ModuleBuilder:
        """"""
    def GetExportedTypes(self) -> Array[Type]:
        """"""
    def GetFile(self, name: str) -> FileStream:
        """"""
    @overload
    def GetFiles(self) -> Array[FileStream]:
        """"""
    @overload
    def GetFiles(self, getResourceModules: bool) -> Array[FileStream]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    @overload
    def GetLoadedModules(self) -> Array[Module]:
        """"""
    @overload
    def GetLoadedModules(self, getResourceModules: bool) -> Array[Module]:
        """"""
    def GetManifestResourceInfo(self, resourceName: str) -> ManifestResourceInfo:
        """"""
    def GetManifestResourceNames(self) -> Array[str]:
        """"""
    @overload
    def GetManifestResourceStream(self, name: str) -> Stream:
        """"""
    @overload
    def GetManifestResourceStream(self, type: Type, name: str) -> Stream:
        """"""
    def GetModule(self, name: str) -> Module:
        """"""
    @overload
    def GetModules(self) -> Array[Module]:
        """"""
    @overload
    def GetModules(self, getResourceModules: bool) -> Array[Module]:
        """"""
    @overload
    def GetName(self) -> AssemblyName:
        """"""
    @overload
    def GetName(self, copiedName: bool) -> AssemblyName:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetReferencedAssemblies(self) -> Array[AssemblyName]:
        """"""
    @overload
    def GetSatelliteAssembly(self, culture: CultureInfo) -> Assembly:
        """"""
    @overload
    def GetSatelliteAssembly(self, culture: CultureInfo, version: Version) -> Assembly:
        """"""
    @overload
    def GetType(self) -> Type:
        """"""
    @overload
    def GetType(self, name: str) -> Type:
        """"""
    @overload
    def GetType(self, name: str, throwOnError: bool) -> Type:
        """"""
    @overload
    def GetType(self, name: str, throwOnError: bool, ignoreCase: bool) -> Type:
        """"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """"""
    def GetTypeInfoCount(self, pcTInfo: UInt32) -> tuple[None, UInt32]:
        """"""
    def GetTypes(self) -> Array[Type]:
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
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """"""
    @overload
    def LoadModule(self, moduleName: str, rawModule: Array[int]) -> Module:
        """"""
    @overload
    def LoadModule(
        self, moduleName: str, rawModule: Array[int], rawSymbolStore: Array[int]
    ) -> Module:
        """"""
    @overload
    def Save(self, assemblyFileName: str) -> None:
        """"""
    @overload
    def Save(
        self,
        assemblyFileName: str,
        portableExecutableKind: PortableExecutableKinds,
        imageFileMachine: ImageFileMachine,
    ) -> None:
        """"""
    @overload
    def SetCustomAttribute(self, customBuilder: CustomAttributeBuilder) -> None:
        """"""
    @overload
    def SetCustomAttribute(self, con: ConstructorInfo, binaryAttribute: Array[int]) -> None:
        """"""
    @overload
    def SetEntryPoint(self, entryMethod: MethodInfo) -> None:
        """"""
    @overload
    def SetEntryPoint(self, entryMethod: MethodInfo, fileKind: PEFileKinds) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    ModuleResolve: EventType[ModuleResolveEventHandler] = ...
    """"""

class AssemblyBuilderAccess(Enum):
    """"""

    Run: AssemblyBuilderAccess = ...
    """"""
    Save: AssemblyBuilderAccess = ...
    """"""
    RunAndSave: AssemblyBuilderAccess = ...
    """"""
    ReflectionOnly: AssemblyBuilderAccess = ...
    """"""
    RunAndCollect: AssemblyBuilderAccess = ...
    """"""

class AssemblyBuilderData(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ConstructorBuilder(
    ConstructorInfo,
    ICustomAttributeProvider,
    _ConstructorBuilder,
    _ConstructorInfo,
    _MemberInfo,
    _MethodBase,
):
    """"""
    @property
    def Attributes(self) -> MethodAttributes:
        """"""
    @property
    def CallingConvention(self) -> CallingConventions:
        """"""
    @property
    def ContainsGenericParameters(self) -> bool:
        """"""
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
        """"""
    @property
    def DeclaringType(self) -> Type:
        """"""
    @property
    def InitLocals(self) -> bool:
        """"""
    @InitLocals.setter
    def InitLocals(self, value: bool) -> None: ...
    @property
    def IsAbstract(self) -> bool:
        """"""
    @property
    def IsAssembly(self) -> bool:
        """"""
    @property
    def IsConstructor(self) -> bool:
        """"""
    @property
    def IsFamily(self) -> bool:
        """"""
    @property
    def IsFamilyAndAssembly(self) -> bool:
        """"""
    @property
    def IsFamilyOrAssembly(self) -> bool:
        """"""
    @property
    def IsFinal(self) -> bool:
        """"""
    @property
    def IsGenericMethod(self) -> bool:
        """"""
    @property
    def IsGenericMethodDefinition(self) -> bool:
        """"""
    @property
    def IsHideBySig(self) -> bool:
        """"""
    @property
    def IsPrivate(self) -> bool:
        """"""
    @property
    def IsPublic(self) -> bool:
        """"""
    @property
    def IsSecurityCritical(self) -> bool:
        """"""
    @property
    def IsSecuritySafeCritical(self) -> bool:
        """"""
    @property
    def IsSecurityTransparent(self) -> bool:
        """"""
    @property
    def IsSpecialName(self) -> bool:
        """"""
    @property
    def IsStatic(self) -> bool:
        """"""
    @property
    def IsVirtual(self) -> bool:
        """"""
    @property
    def MemberType(self) -> MemberTypes:
        """"""
    @property
    def MetadataToken(self) -> int:
        """"""
    @property
    def MethodHandle(self) -> RuntimeMethodHandle:
        """"""
    @property
    def MethodImplementationFlags(self) -> MethodImplAttributes:
        """"""
    @property
    def Module(self) -> Module:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def ReflectedType(self) -> Type:
        """"""
    @property
    def ReturnType(self) -> Type:
        """"""
    @property
    def Signature(self) -> str:
        """"""
    def AddDeclarativeSecurity(self, action: SecurityAction, pset: PermissionSet) -> None:
        """"""
    def DefineParameter(
        self, iSequence: int, attributes: ParameterAttributes, strParamName: str
    ) -> ParameterBuilder:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """"""
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """"""
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]:
        """"""
    def GetGenericArguments(self) -> Array[Type]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    @overload
    def GetILGenerator(self) -> ILGenerator:
        """"""
    @overload
    def GetILGenerator(self, streamSize: int) -> ILGenerator:
        """"""
    def GetMethodBody(self) -> MethodBody:
        """"""
    def GetMethodImplementationFlags(self) -> MethodImplAttributes:
        """"""
    def GetModule(self) -> Module:
        """"""
    def GetParameters(self) -> Array[ParameterInfo]:
        """"""
    def GetToken(self) -> MethodToken:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """"""
    def GetTypeInfoCount(self, pcTInfo: UInt32) -> tuple[None, UInt32]:
        """"""
    @overload
    def Invoke(
        self,
        invokeAttr: BindingFlags,
        binder: Binder,
        parameters: Array[object],
        culture: CultureInfo,
    ) -> object:
        """"""
    @overload
    def Invoke(self, parameters: Array[object]) -> object:
        """"""
    @overload
    def Invoke(
        self,
        obj: object,
        invokeAttr: BindingFlags,
        binder: Binder,
        parameters: Array[object],
        culture: CultureInfo,
    ) -> object:
        """"""
    @overload
    def Invoke(self, obj: object, parameters: Array[object]) -> object:
        """"""
    @overload
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
    def Invoke_2(
        self,
        obj: object,
        invokeAttr: BindingFlags,
        binder: Binder,
        parameters: Array[object],
        culture: CultureInfo,
    ) -> object:
        """"""
    def Invoke_3(self, obj: object, parameters: Array[object]) -> object:
        """"""
    def Invoke_4(
        self,
        invokeAttr: BindingFlags,
        binder: Binder,
        parameters: Array[object],
        culture: CultureInfo,
    ) -> object:
        """"""
    def Invoke_5(self, parameters: Array[object]) -> object:
        """"""
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """"""
    @overload
    def SetCustomAttribute(self, customBuilder: CustomAttributeBuilder) -> None:
        """"""
    @overload
    def SetCustomAttribute(self, con: ConstructorInfo, binaryAttribute: Array[int]) -> None:
        """"""
    def SetImplementationFlags(self, attributes: MethodImplAttributes) -> None:
        """"""
    def SetMethodBody(
        self,
        il: Array[int],
        maxStack: int,
        localSignature: Array[int],
        exceptionHandlers: IEnumerable[ExceptionHandler],
        tokenFixups: IEnumerable[int],
    ) -> None:
        """"""
    def SetSymCustomAttribute(self, name: str, data: Array[int]) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class ConstructorOnTypeBuilderInstantiation(
    ConstructorInfo, ICustomAttributeProvider, _ConstructorInfo, _MemberInfo, _MethodBase
):
    """"""
    @property
    def Attributes(self) -> MethodAttributes:
        """"""
    @property
    def CallingConvention(self) -> CallingConventions:
        """"""
    @property
    def ContainsGenericParameters(self) -> bool:
        """"""
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
        """"""
    @property
    def DeclaringType(self) -> Type:
        """"""
    @property
    def IsAbstract(self) -> bool:
        """"""
    @property
    def IsAssembly(self) -> bool:
        """"""
    @property
    def IsConstructor(self) -> bool:
        """"""
    @property
    def IsFamily(self) -> bool:
        """"""
    @property
    def IsFamilyAndAssembly(self) -> bool:
        """"""
    @property
    def IsFamilyOrAssembly(self) -> bool:
        """"""
    @property
    def IsFinal(self) -> bool:
        """"""
    @property
    def IsGenericMethod(self) -> bool:
        """"""
    @property
    def IsGenericMethodDefinition(self) -> bool:
        """"""
    @property
    def IsHideBySig(self) -> bool:
        """"""
    @property
    def IsPrivate(self) -> bool:
        """"""
    @property
    def IsPublic(self) -> bool:
        """"""
    @property
    def IsSecurityCritical(self) -> bool:
        """"""
    @property
    def IsSecuritySafeCritical(self) -> bool:
        """"""
    @property
    def IsSecurityTransparent(self) -> bool:
        """"""
    @property
    def IsSpecialName(self) -> bool:
        """"""
    @property
    def IsStatic(self) -> bool:
        """"""
    @property
    def IsVirtual(self) -> bool:
        """"""
    @property
    def MemberType(self) -> MemberTypes:
        """"""
    @property
    def MetadataToken(self) -> int:
        """"""
    @property
    def MethodHandle(self) -> RuntimeMethodHandle:
        """"""
    @property
    def MethodImplementationFlags(self) -> MethodImplAttributes:
        """"""
    @property
    def Module(self) -> Module:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def ReflectedType(self) -> Type:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """"""
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """"""
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]:
        """"""
    def GetGenericArguments(self) -> Array[Type]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    def GetMethodBody(self) -> MethodBody:
        """"""
    def GetMethodImplementationFlags(self) -> MethodImplAttributes:
        """"""
    def GetParameters(self) -> Array[ParameterInfo]:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """"""
    def GetTypeInfoCount(self, pcTInfo: UInt32) -> tuple[None, UInt32]:
        """"""
    @overload
    def Invoke(
        self,
        invokeAttr: BindingFlags,
        binder: Binder,
        parameters: Array[object],
        culture: CultureInfo,
    ) -> object:
        """"""
    @overload
    def Invoke(self, parameters: Array[object]) -> object:
        """"""
    @overload
    def Invoke(
        self,
        obj: object,
        invokeAttr: BindingFlags,
        binder: Binder,
        parameters: Array[object],
        culture: CultureInfo,
    ) -> object:
        """"""
    @overload
    def Invoke(self, obj: object, parameters: Array[object]) -> object:
        """"""
    @overload
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
    def Invoke_2(
        self,
        obj: object,
        invokeAttr: BindingFlags,
        binder: Binder,
        parameters: Array[object],
        culture: CultureInfo,
    ) -> object:
        """"""
    def Invoke_3(self, obj: object, parameters: Array[object]) -> object:
        """"""
    def Invoke_4(
        self,
        invokeAttr: BindingFlags,
        binder: Binder,
        parameters: Array[object],
        culture: CultureInfo,
    ) -> object:
        """"""
    def Invoke_5(self, parameters: Array[object]) -> object:
        """"""
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

class CustomAttributeBuilder(Object, _CustomAttributeBuilder):
    """"""
    @overload
    def __init__(self, con: ConstructorInfo, constructorArgs: Array[object]) -> None:
        """"""
    @overload
    def __init__(
        self,
        con: ConstructorInfo,
        constructorArgs: Array[object],
        namedProperties: Array[PropertyInfo],
        propertyValues: Array[object],
    ) -> None:
        """"""
    @overload
    def __init__(
        self,
        con: ConstructorInfo,
        constructorArgs: Array[object],
        namedFields: Array[FieldInfo],
        fieldValues: Array[object],
    ) -> None:
        """"""
    @overload
    def __init__(
        self,
        con: ConstructorInfo,
        constructorArgs: Array[object],
        namedProperties: Array[PropertyInfo],
        propertyValues: Array[object],
        namedFields: Array[FieldInfo],
        fieldValues: Array[object],
    ) -> None:
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
    def ToString(self) -> str:
        """"""

class DynamicAssemblyFlags(Enum):
    """"""

    _None: DynamicAssemblyFlags = ...
    """"""
    AllCritical: DynamicAssemblyFlags = ...
    """"""
    Aptca: DynamicAssemblyFlags = ...
    """"""
    Critical: DynamicAssemblyFlags = ...
    """"""
    Transparent: DynamicAssemblyFlags = ...
    """"""
    TreatAsSafe: DynamicAssemblyFlags = ...
    """"""

class DynamicILGenerator(ILGenerator, _ILGenerator):
    """"""
    @property
    def ILOffset(self) -> int:
        """"""
    def BeginCatchBlock(self, exceptionType: Type) -> None:
        """"""
    def BeginExceptFilterBlock(self) -> None:
        """"""
    def BeginExceptionBlock(self) -> Label:
        """"""
    def BeginFaultBlock(self) -> None:
        """"""
    def BeginFinallyBlock(self) -> None:
        """"""
    def BeginScope(self) -> None:
        """"""
    @overload
    def DeclareLocal(self, localType: Type) -> LocalBuilder:
        """"""
    @overload
    def DeclareLocal(self, localType: Type, pinned: bool) -> LocalBuilder:
        """"""
    def DefineLabel(self) -> Label:
        """"""
    @overload
    def Emit(self, opcode: OpCode) -> None:
        """"""
    @overload
    def Emit(self, opcode: OpCode, label: Label) -> None:
        """"""
    @overload
    def Emit(self, opcode: OpCode, local: LocalBuilder) -> None:
        """"""
    @overload
    def Emit(self, opcode: OpCode, signature: SignatureHelper) -> None:
        """"""
    @overload
    def Emit(self, opcode: OpCode, con: ConstructorInfo) -> None:
        """"""
    @overload
    def Emit(self, opcode: OpCode, field: FieldInfo) -> None:
        """"""
    @overload
    def Emit(self, opcode: OpCode, meth: MethodInfo) -> None:
        """"""
    @overload
    def Emit(self, opcode: OpCode, labels: Array[Label]) -> None:
        """"""
    @overload
    def Emit(self, opcode: OpCode, arg: int) -> None:
        """"""
    @overload
    def Emit(self, opcode: OpCode, arg: float) -> None:
        """"""
    @overload
    def Emit(self, opcode: OpCode, arg: int) -> None:
        """"""
    @overload
    def Emit(self, opcode: OpCode, arg: int) -> None:
        """"""
    @overload
    def Emit(self, opcode: OpCode, arg: int) -> None:
        """"""
    @overload
    def Emit(self, opcode: OpCode, arg: int) -> None:
        """"""
    @overload
    def Emit(self, opcode: OpCode, arg: float) -> None:
        """"""
    @overload
    def Emit(self, opcode: OpCode, str: str) -> None:
        """"""
    @overload
    def Emit(self, opcode: OpCode, type: Type) -> None:
        """"""
    def EmitCall(
        self, opcode: OpCode, methodInfo: MethodInfo, optionalParameterTypes: Array[Type]
    ) -> None:
        """"""
    @overload
    def EmitCalli(
        self,
        opcode: OpCode,
        callingConvention: CallingConventions,
        returnType: Type,
        parameterTypes: Array[Type],
        optionalParameterTypes: Array[Type],
    ) -> None:
        """"""
    @overload
    def EmitCalli(
        self,
        opcode: OpCode,
        unmanagedCallConv: CallingConvention,
        returnType: Type,
        parameterTypes: Array[Type],
    ) -> None:
        """"""
    @overload
    def EmitWriteLine(self, localBuilder: LocalBuilder) -> None:
        """"""
    @overload
    def EmitWriteLine(self, fld: FieldInfo) -> None:
        """"""
    @overload
    def EmitWriteLine(self, value: str) -> None:
        """"""
    def EndExceptionBlock(self) -> None:
        """"""
    def EndScope(self) -> None:
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
    def MarkLabel(self, loc: Label) -> None:
        """"""
    def MarkSequencePoint(
        self,
        document: ISymbolDocumentWriter,
        startLine: int,
        startColumn: int,
        endLine: int,
        endColumn: int,
    ) -> None:
        """"""
    def ThrowException(self, excType: Type) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def UsingNamespace(self, ns: str) -> None:
        """"""

class DynamicILInfo(Object):
    """"""
    @property
    def DynamicMethod(self) -> DynamicMethod:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetTokenFor(self, method: DynamicMethod) -> int:
        """"""
    @overload
    def GetTokenFor(self, signature: Array[int]) -> int:
        """"""
    @overload
    def GetTokenFor(self, field: RuntimeFieldHandle) -> int:
        """"""
    @overload
    def GetTokenFor(self, field: RuntimeFieldHandle, contextType: RuntimeTypeHandle) -> int:
        """"""
    @overload
    def GetTokenFor(self, method: RuntimeMethodHandle) -> int:
        """"""
    @overload
    def GetTokenFor(self, method: RuntimeMethodHandle, contextType: RuntimeTypeHandle) -> int:
        """"""
    @overload
    def GetTokenFor(self, type: RuntimeTypeHandle) -> int:
        """"""
    @overload
    def GetTokenFor(self, literal: str) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def SetCode(self, code: Array[int], maxStackSize: int) -> None:
        """"""
    @overload
    def SetCode(self, code: int, codeSize: int, maxStackSize: int) -> None:
        """"""
    @overload
    def SetExceptions(self, exceptions: Array[int]) -> None:
        """"""
    @overload
    def SetExceptions(self, exceptions: int, exceptionsSize: int) -> None:
        """"""
    @overload
    def SetLocalSignature(self, localSignature: Array[int]) -> None:
        """"""
    @overload
    def SetLocalSignature(self, localSignature: int, signatureSize: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class DynamicMethod(MethodInfo, ICustomAttributeProvider, _MemberInfo, _MethodBase, _MethodInfo):
    """"""
    @overload
    def __init__(self, name: str, returnType: Type, parameterTypes: Array[Type]) -> None:
        """"""
    @overload
    def __init__(
        self,
        name: str,
        returnType: Type,
        parameterTypes: Array[Type],
        restrictedSkipVisibility: bool,
    ) -> None:
        """"""
    @overload
    def __init__(self, name: str, returnType: Type, parameterTypes: Array[Type], m: Module) -> None:
        """"""
    @overload
    def __init__(
        self,
        name: str,
        returnType: Type,
        parameterTypes: Array[Type],
        m: Module,
        skipVisibility: bool,
    ) -> None:
        """"""
    @overload
    def __init__(
        self,
        name: str,
        attributes: MethodAttributes,
        callingConvention: CallingConventions,
        returnType: Type,
        parameterTypes: Array[Type],
        m: Module,
        skipVisibility: bool,
    ) -> None:
        """"""
    @overload
    def __init__(
        self, name: str, returnType: Type, parameterTypes: Array[Type], owner: Type
    ) -> None:
        """"""
    @overload
    def __init__(
        self,
        name: str,
        returnType: Type,
        parameterTypes: Array[Type],
        owner: Type,
        skipVisibility: bool,
    ) -> None:
        """"""
    @overload
    def __init__(
        self,
        name: str,
        attributes: MethodAttributes,
        callingConvention: CallingConventions,
        returnType: Type,
        parameterTypes: Array[Type],
        owner: Type,
        skipVisibility: bool,
    ) -> None:
        """"""
    @property
    def Attributes(self) -> MethodAttributes:
        """"""
    @property
    def CallingConvention(self) -> CallingConventions:
        """"""
    @property
    def ContainsGenericParameters(self) -> bool:
        """"""
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
        """"""
    @property
    def DeclaringType(self) -> Type:
        """"""
    @property
    def InitLocals(self) -> bool:
        """"""
    @InitLocals.setter
    def InitLocals(self, value: bool) -> None: ...
    @property
    def IsAbstract(self) -> bool:
        """"""
    @property
    def IsAssembly(self) -> bool:
        """"""
    @property
    def IsConstructor(self) -> bool:
        """"""
    @property
    def IsFamily(self) -> bool:
        """"""
    @property
    def IsFamilyAndAssembly(self) -> bool:
        """"""
    @property
    def IsFamilyOrAssembly(self) -> bool:
        """"""
    @property
    def IsFinal(self) -> bool:
        """"""
    @property
    def IsGenericMethod(self) -> bool:
        """"""
    @property
    def IsGenericMethodDefinition(self) -> bool:
        """"""
    @property
    def IsHideBySig(self) -> bool:
        """"""
    @property
    def IsPrivate(self) -> bool:
        """"""
    @property
    def IsPublic(self) -> bool:
        """"""
    @property
    def IsSecurityCritical(self) -> bool:
        """"""
    @property
    def IsSecuritySafeCritical(self) -> bool:
        """"""
    @property
    def IsSecurityTransparent(self) -> bool:
        """"""
    @property
    def IsSpecialName(self) -> bool:
        """"""
    @property
    def IsStatic(self) -> bool:
        """"""
    @property
    def IsVirtual(self) -> bool:
        """"""
    @property
    def MemberType(self) -> MemberTypes:
        """"""
    @property
    def MetadataToken(self) -> int:
        """"""
    @property
    def MethodHandle(self) -> RuntimeMethodHandle:
        """"""
    @property
    def MethodImplementationFlags(self) -> MethodImplAttributes:
        """"""
    @property
    def Module(self) -> Module:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def ReflectedType(self) -> Type:
        """"""
    @property
    def ReturnParameter(self) -> ParameterInfo:
        """"""
    @property
    def ReturnType(self) -> Type:
        """"""
    @property
    def ReturnTypeCustomAttributes(self) -> ICustomAttributeProvider:
        """"""
    @overload
    def CreateDelegate(self, delegateType: Type) -> Delegate:
        """"""
    @overload
    def CreateDelegate(self, delegateType: Type, target: object) -> Delegate:
        """"""
    def DefineParameter(
        self, position: int, attributes: ParameterAttributes, parameterName: str
    ) -> ParameterBuilder:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetBaseDefinition(self) -> MethodInfo:
        """"""
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """"""
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """"""
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]:
        """"""
    def GetDynamicILInfo(self) -> DynamicILInfo:
        """"""
    def GetGenericArguments(self) -> Array[Type]:
        """"""
    def GetGenericMethodDefinition(self) -> MethodInfo:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    @overload
    def GetILGenerator(self) -> ILGenerator:
        """"""
    @overload
    def GetILGenerator(self, streamSize: int) -> ILGenerator:
        """"""
    def GetMethodBody(self) -> MethodBody:
        """"""
    def GetMethodImplementationFlags(self) -> MethodImplAttributes:
        """"""
    def GetParameters(self) -> Array[ParameterInfo]:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """"""
    def GetTypeInfoCount(self, pcTInfo: UInt32) -> tuple[None, UInt32]:
        """"""
    @overload
    def Invoke(
        self,
        obj: object,
        invokeAttr: BindingFlags,
        binder: Binder,
        parameters: Array[object],
        culture: CultureInfo,
    ) -> object:
        """"""
    @overload
    def Invoke(self, obj: object, parameters: Array[object]) -> object:
        """"""
    @overload
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
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """"""
    def MakeGenericMethod(self, typeArguments: Array[Type]) -> MethodInfo:
        """"""
    def ToString(self) -> str:
        """"""

class DynamicResolver(Resolver):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class DynamicScope(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetTokenFor(self, method: DynamicMethod) -> int:
        """"""
    @overload
    def GetTokenFor(self, signature: Array[int]) -> int:
        """"""
    @overload
    def GetTokenFor(self, field: RuntimeFieldHandle) -> int:
        """"""
    @overload
    def GetTokenFor(self, field: RuntimeFieldHandle, typeContext: RuntimeTypeHandle) -> int:
        """"""
    @overload
    def GetTokenFor(self, method: RuntimeMethodHandle) -> int:
        """"""
    @overload
    def GetTokenFor(self, method: RuntimeMethodHandle, typeContext: RuntimeTypeHandle) -> int:
        """"""
    @overload
    def GetTokenFor(self, type: RuntimeTypeHandle) -> int:
        """"""
    @overload
    def GetTokenFor(self, literal: str) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class EnumBuilder(
    TypeInfo, ICustomAttributeProvider, IReflect, IReflectableType, _EnumBuilder, _MemberInfo, _Type
):
    """"""
    @property
    def Assembly(self) -> Assembly:
        """"""
    @property
    def AssemblyQualifiedName(self) -> str:
        """"""
    @property
    def Attributes(self) -> TypeAttributes:
        """"""
    @property
    def BaseType(self) -> Type:
        """"""
    @property
    def ContainsGenericParameters(self) -> bool:
        """"""
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
        """"""
    @property
    def DeclaredConstructors(self) -> IEnumerable[ConstructorInfo]:
        """"""
    @property
    def DeclaredEvents(self) -> IEnumerable[EventInfo]:
        """"""
    @property
    def DeclaredFields(self) -> IEnumerable[FieldInfo]:
        """"""
    @property
    def DeclaredMembers(self) -> IEnumerable[MemberInfo]:
        """"""
    @property
    def DeclaredMethods(self) -> IEnumerable[MethodInfo]:
        """"""
    @property
    def DeclaredNestedTypes(self) -> IEnumerable[TypeInfo]:
        """"""
    @property
    def DeclaredProperties(self) -> IEnumerable[PropertyInfo]:
        """"""
    @property
    def DeclaringMethod(self) -> MethodBase:
        """"""
    @property
    def DeclaringType(self) -> Type:
        """"""
    @property
    def FullName(self) -> str:
        """"""
    @property
    def GUID(self) -> Guid:
        """"""
    @property
    def GenericParameterAttributes(self) -> GenericParameterAttributes:
        """"""
    @property
    def GenericParameterPosition(self) -> int:
        """"""
    @property
    def GenericTypeArguments(self) -> Array[Type]:
        """"""
    @property
    def GenericTypeParameters(self) -> Array[Type]:
        """"""
    @property
    def HasElementType(self) -> bool:
        """"""
    @property
    def ImplementedInterfaces(self) -> IEnumerable[Type]:
        """"""
    @property
    def IsAbstract(self) -> bool:
        """"""
    @property
    def IsAnsiClass(self) -> bool:
        """"""
    @property
    def IsArray(self) -> bool:
        """"""
    @property
    def IsAutoClass(self) -> bool:
        """"""
    @property
    def IsAutoLayout(self) -> bool:
        """"""
    @property
    def IsByRef(self) -> bool:
        """"""
    @property
    def IsCOMObject(self) -> bool:
        """"""
    @property
    def IsClass(self) -> bool:
        """"""
    @property
    def IsConstructedGenericType(self) -> bool:
        """"""
    @property
    def IsContextful(self) -> bool:
        """"""
    @property
    def IsEnum(self) -> bool:
        """"""
    @property
    def IsExplicitLayout(self) -> bool:
        """"""
    @property
    def IsGenericParameter(self) -> bool:
        """"""
    @property
    def IsGenericType(self) -> bool:
        """"""
    @property
    def IsGenericTypeDefinition(self) -> bool:
        """"""
    @property
    def IsImport(self) -> bool:
        """"""
    @property
    def IsInterface(self) -> bool:
        """"""
    @property
    def IsLayoutSequential(self) -> bool:
        """"""
    @property
    def IsMarshalByRef(self) -> bool:
        """"""
    @property
    def IsNested(self) -> bool:
        """"""
    @property
    def IsNestedAssembly(self) -> bool:
        """"""
    @property
    def IsNestedFamANDAssem(self) -> bool:
        """"""
    @property
    def IsNestedFamORAssem(self) -> bool:
        """"""
    @property
    def IsNestedFamily(self) -> bool:
        """"""
    @property
    def IsNestedPrivate(self) -> bool:
        """"""
    @property
    def IsNestedPublic(self) -> bool:
        """"""
    @property
    def IsNotPublic(self) -> bool:
        """"""
    @property
    def IsPointer(self) -> bool:
        """"""
    @property
    def IsPrimitive(self) -> bool:
        """"""
    @property
    def IsPublic(self) -> bool:
        """"""
    @property
    def IsSealed(self) -> bool:
        """"""
    @property
    def IsSecurityCritical(self) -> bool:
        """"""
    @property
    def IsSecuritySafeCritical(self) -> bool:
        """"""
    @property
    def IsSecurityTransparent(self) -> bool:
        """"""
    @property
    def IsSerializable(self) -> bool:
        """"""
    @property
    def IsSpecialName(self) -> bool:
        """"""
    @property
    def IsUnicodeClass(self) -> bool:
        """"""
    @property
    def IsValueType(self) -> bool:
        """"""
    @property
    def IsVisible(self) -> bool:
        """"""
    @property
    def MemberType(self) -> MemberTypes:
        """"""
    @property
    def MetadataToken(self) -> int:
        """"""
    @property
    def Module(self) -> Module:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def Namespace(self) -> str:
        """"""
    @property
    def ReflectedType(self) -> Type:
        """"""
    @property
    def StructLayoutAttribute(self) -> StructLayoutAttribute:
        """"""
    @property
    def TypeHandle(self) -> RuntimeTypeHandle:
        """"""
    @property
    def TypeInitializer(self) -> ConstructorInfo:
        """"""
    @property
    def TypeToken(self) -> TypeToken:
        """"""
    @property
    def UnderlyingField(self) -> FieldBuilder:
        """"""
    @property
    def UnderlyingSystemType(self) -> Type:
        """"""
    def AsType(self) -> Type:
        """"""
    def CreateType(self) -> Type:
        """"""
    def CreateTypeInfo(self) -> TypeInfo:
        """"""
    def DefineLiteral(self, literalName: str, literalValue: object) -> FieldBuilder:
        """"""
    @overload
    def Equals(self, o: object) -> bool:
        """"""
    @overload
    def Equals(self, o: Type) -> bool:
        """"""
    def FindInterfaces(self, filter: TypeFilter, filterCriteria: object) -> Array[Type]:
        """"""
    def FindMembers(
        self,
        memberType: MemberTypes,
        bindingAttr: BindingFlags,
        filter: MemberFilter,
        filterCriteria: object,
    ) -> Array[MemberInfo]:
        """"""
    def GetArrayRank(self) -> int:
        """"""
    @overload
    def GetConstructor(
        self,
        bindingAttr: BindingFlags,
        binder: Binder,
        callConvention: CallingConventions,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> ConstructorInfo:
        """"""
    @overload
    def GetConstructor(
        self,
        bindingAttr: BindingFlags,
        binder: Binder,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> ConstructorInfo:
        """"""
    @overload
    def GetConstructor(self, types: Array[Type]) -> ConstructorInfo:
        """"""
    @overload
    def GetConstructors(self) -> Array[ConstructorInfo]:
        """"""
    @overload
    def GetConstructors(self, bindingAttr: BindingFlags) -> Array[ConstructorInfo]:
        """"""
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """"""
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """"""
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]:
        """"""
    def GetDeclaredEvent(self, name: str) -> EventInfo:
        """"""
    def GetDeclaredField(self, name: str) -> FieldInfo:
        """"""
    def GetDeclaredMethod(self, name: str) -> MethodInfo:
        """"""
    def GetDeclaredMethods(self, name: str) -> IEnumerable[MethodInfo]:
        """"""
    def GetDeclaredNestedType(self, name: str) -> TypeInfo:
        """"""
    def GetDeclaredProperty(self, name: str) -> PropertyInfo:
        """"""
    def GetDefaultMembers(self) -> Array[MemberInfo]:
        """"""
    def GetElementType(self) -> Type:
        """"""
    def GetEnumName(self, value: object) -> str:
        """"""
    def GetEnumNames(self) -> Array[str]:
        """"""
    def GetEnumUnderlyingType(self) -> Type:
        """"""
    def GetEnumValues(self) -> Array:
        """"""
    @overload
    def GetEvent(self, name: str) -> EventInfo:
        """"""
    @overload
    def GetEvent(self, name: str, bindingAttr: BindingFlags) -> EventInfo:
        """"""
    @overload
    def GetEvents(self) -> Array[EventInfo]:
        """"""
    @overload
    def GetEvents(self, bindingAttr: BindingFlags) -> Array[EventInfo]:
        """"""
    @overload
    def GetField(self, name: str) -> FieldInfo:
        """"""
    @overload
    def GetField(self, name: str, bindingAttr: BindingFlags) -> FieldInfo:
        """"""
    @overload
    def GetFields(self) -> Array[FieldInfo]:
        """"""
    @overload
    def GetFields(self, bindingAttr: BindingFlags) -> Array[FieldInfo]:
        """"""
    def GetGenericArguments(self) -> Array[Type]:
        """"""
    def GetGenericParameterConstraints(self) -> Array[Type]:
        """"""
    def GetGenericTypeDefinition(self) -> Type:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    @overload
    def GetInterface(self, name: str) -> Type:
        """"""
    @overload
    def GetInterface(self, name: str, ignoreCase: bool) -> Type:
        """"""
    def GetInterfaceMap(self, interfaceType: Type) -> InterfaceMapping:
        """"""
    def GetInterfaces(self) -> Array[Type]:
        """"""
    @overload
    def GetMember(self, name: str) -> Array[MemberInfo]:
        """"""
    @overload
    def GetMember(self, name: str, bindingAttr: BindingFlags) -> Array[MemberInfo]:
        """"""
    @overload
    def GetMember(
        self, name: str, type: MemberTypes, bindingAttr: BindingFlags
    ) -> Array[MemberInfo]:
        """"""
    @overload
    def GetMembers(self) -> Array[MemberInfo]:
        """"""
    @overload
    def GetMembers(self, bindingAttr: BindingFlags) -> Array[MemberInfo]:
        """"""
    @overload
    def GetMethod(self, name: str) -> MethodInfo:
        """"""
    @overload
    def GetMethod(self, name: str, bindingAttr: BindingFlags) -> MethodInfo:
        """"""
    @overload
    def GetMethod(
        self,
        name: str,
        bindingAttr: BindingFlags,
        binder: Binder,
        callConvention: CallingConventions,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> MethodInfo:
        """"""
    @overload
    def GetMethod(
        self,
        name: str,
        bindingAttr: BindingFlags,
        binder: Binder,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> MethodInfo:
        """"""
    @overload
    def GetMethod(self, name: str, types: Array[Type]) -> MethodInfo:
        """"""
    @overload
    def GetMethod(
        self, name: str, types: Array[Type], modifiers: Array[ParameterModifier]
    ) -> MethodInfo:
        """"""
    @overload
    def GetMethods(self) -> Array[MethodInfo]:
        """"""
    @overload
    def GetMethods(self, bindingAttr: BindingFlags) -> Array[MethodInfo]:
        """"""
    @overload
    def GetNestedType(self, name: str) -> Type:
        """"""
    @overload
    def GetNestedType(self, name: str, bindingAttr: BindingFlags) -> Type:
        """"""
    @overload
    def GetNestedTypes(self) -> Array[Type]:
        """"""
    @overload
    def GetNestedTypes(self, bindingAttr: BindingFlags) -> Array[Type]:
        """"""
    @overload
    def GetProperties(self) -> Array[PropertyInfo]:
        """"""
    @overload
    def GetProperties(self, bindingAttr: BindingFlags) -> Array[PropertyInfo]:
        """"""
    @overload
    def GetProperty(self, name: str) -> PropertyInfo:
        """"""
    @overload
    def GetProperty(self, name: str, bindingAttr: BindingFlags) -> PropertyInfo:
        """"""
    @overload
    def GetProperty(
        self,
        name: str,
        bindingAttr: BindingFlags,
        binder: Binder,
        returnType: Type,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> PropertyInfo:
        """"""
    @overload
    def GetProperty(self, name: str, types: Array[Type]) -> PropertyInfo:
        """"""
    @overload
    def GetProperty(self, name: str, returnType: Type) -> PropertyInfo:
        """"""
    @overload
    def GetProperty(self, name: str, returnType: Type, types: Array[Type]) -> PropertyInfo:
        """"""
    @overload
    def GetProperty(
        self, name: str, returnType: Type, types: Array[Type], modifiers: Array[ParameterModifier]
    ) -> PropertyInfo:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def GetTypeInfo(self) -> TypeInfo:
        """"""
    @overload
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
    @overload
    def InvokeMember(
        self,
        name: str,
        invokeAttr: BindingFlags,
        binder: Binder,
        target: object,
        args: Array[object],
    ) -> object:
        """"""
    @overload
    def InvokeMember(
        self,
        name: str,
        invokeAttr: BindingFlags,
        binder: Binder,
        target: object,
        args: Array[object],
        culture: CultureInfo,
    ) -> object:
        """"""
    @overload
    def InvokeMember(
        self,
        name: str,
        invokeAttr: BindingFlags,
        binder: Binder,
        target: object,
        args: Array[object],
        modifiers: Array[ParameterModifier],
        culture: CultureInfo,
        namedParameters: Array[str],
    ) -> object:
        """"""
    @overload
    def IsAssignableFrom(self, typeInfo: TypeInfo) -> bool:
        """"""
    @overload
    def IsAssignableFrom(self, c: Type) -> bool:
        """"""
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """"""
    def IsEnumDefined(self, value: object) -> bool:
        """"""
    def IsEquivalentTo(self, other: Type) -> bool:
        """"""
    def IsInstanceOfType(self, o: object) -> bool:
        """"""
    def IsSubclassOf(self, c: Type) -> bool:
        """"""
    @overload
    def MakeArrayType(self) -> Type:
        """"""
    @overload
    def MakeArrayType(self, rank: int) -> Type:
        """"""
    def MakeByRefType(self) -> Type:
        """"""
    def MakeGenericType(self, typeArguments: Array[Type]) -> Type:
        """"""
    def MakePointerType(self) -> Type:
        """"""
    @overload
    def SetCustomAttribute(self, customBuilder: CustomAttributeBuilder) -> None:
        """"""
    @overload
    def SetCustomAttribute(self, con: ConstructorInfo, binaryAttribute: Array[int]) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class EventBuilder(Object, _EventBuilder):
    """"""
    def AddOtherMethod(self, mdBuilder: MethodBuilder) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEventToken(self) -> EventToken:
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
    def SetAddOnMethod(self, mdBuilder: MethodBuilder) -> None:
        """"""
    @overload
    def SetCustomAttribute(self, customBuilder: CustomAttributeBuilder) -> None:
        """"""
    @overload
    def SetCustomAttribute(self, con: ConstructorInfo, binaryAttribute: Array[int]) -> None:
        """"""
    def SetRaiseMethod(self, mdBuilder: MethodBuilder) -> None:
        """"""
    def SetRemoveOnMethod(self, mdBuilder: MethodBuilder) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class EventToken(ValueType):
    """"""

    Empty: ClassVar[EventToken]
    """"""
    @property
    def Token(self) -> int:
        """"""
    @overload
    def Equals(self, obj: EventToken) -> bool:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def op_Equality(cls, a: EventToken, b: EventToken) -> bool:
        """"""
    @classmethod
    def op_Inequality(cls, a: EventToken, b: EventToken) -> bool:
        """"""
    def __eq__(self, other: EventToken) -> bool:
        """"""
    def __ne__(self, other: EventToken) -> bool:
        """"""

class ExceptionHandler(ValueType, IEquatable[ExceptionHandler]):
    """"""
    def __init__(
        self,
        tryOffset: int,
        tryLength: int,
        filterOffset: int,
        handlerOffset: int,
        handlerLength: int,
        kind: ExceptionHandlingClauseOptions,
        exceptionTypeToken: int,
    ) -> None:
        """"""
    @property
    def ExceptionTypeToken(self) -> int:
        """"""
    @property
    def FilterOffset(self) -> int:
        """"""
    @property
    def HandlerLength(self) -> int:
        """"""
    @property
    def HandlerOffset(self) -> int:
        """"""
    @property
    def Kind(self) -> ExceptionHandlingClauseOptions:
        """"""
    @property
    def TryLength(self) -> int:
        """"""
    @property
    def TryOffset(self) -> int:
        """"""
    @overload
    def Equals(self, other: ExceptionHandler) -> bool:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def op_Equality(cls, left: ExceptionHandler, right: ExceptionHandler) -> bool:
        """"""
    @classmethod
    def op_Inequality(cls, left: ExceptionHandler, right: ExceptionHandler) -> bool:
        """"""
    def __eq__(self, other: ExceptionHandler) -> bool:
        """"""
    def __ne__(self, other: ExceptionHandler) -> bool:
        """"""

class FieldBuilder(FieldInfo, ICustomAttributeProvider, _FieldBuilder, _FieldInfo, _MemberInfo):
    """"""
    @property
    def Attributes(self) -> FieldAttributes:
        """"""
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
        """"""
    @property
    def DeclaringType(self) -> Type:
        """"""
    @property
    def FieldHandle(self) -> RuntimeFieldHandle:
        """"""
    @property
    def FieldType(self) -> Type:
        """"""
    @property
    def IsAssembly(self) -> bool:
        """"""
    @property
    def IsFamily(self) -> bool:
        """"""
    @property
    def IsFamilyAndAssembly(self) -> bool:
        """"""
    @property
    def IsFamilyOrAssembly(self) -> bool:
        """"""
    @property
    def IsInitOnly(self) -> bool:
        """"""
    @property
    def IsLiteral(self) -> bool:
        """"""
    @property
    def IsNotSerialized(self) -> bool:
        """"""
    @property
    def IsPinvokeImpl(self) -> bool:
        """"""
    @property
    def IsPrivate(self) -> bool:
        """"""
    @property
    def IsPublic(self) -> bool:
        """"""
    @property
    def IsSecurityCritical(self) -> bool:
        """"""
    @property
    def IsSecuritySafeCritical(self) -> bool:
        """"""
    @property
    def IsSecurityTransparent(self) -> bool:
        """"""
    @property
    def IsSpecialName(self) -> bool:
        """"""
    @property
    def IsStatic(self) -> bool:
        """"""
    @property
    def MemberType(self) -> MemberTypes:
        """"""
    @property
    def MetadataToken(self) -> int:
        """"""
    @property
    def Module(self) -> Module:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def ReflectedType(self) -> Type:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """"""
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """"""
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    def GetOptionalCustomModifiers(self) -> Array[Type]:
        """"""
    def GetRawConstantValue(self) -> object:
        """"""
    def GetRequiredCustomModifiers(self) -> Array[Type]:
        """"""
    def GetToken(self) -> FieldToken:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """"""
    def GetTypeInfoCount(self, pcTInfo: UInt32) -> tuple[None, UInt32]:
        """"""
    def GetValue(self, obj: object) -> object:
        """"""
    def GetValueDirect(self, obj: TypedReference) -> object:
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
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """"""
    def SetConstant(self, defaultValue: object) -> None:
        """"""
    @overload
    def SetCustomAttribute(self, customBuilder: CustomAttributeBuilder) -> None:
        """"""
    @overload
    def SetCustomAttribute(self, con: ConstructorInfo, binaryAttribute: Array[int]) -> None:
        """"""
    def SetMarshal(self, unmanagedMarshal: UnmanagedMarshal) -> None:
        """"""
    def SetOffset(self, iOffset: int) -> None:
        """"""
    @overload
    def SetValue(self, obj: object, value: object) -> None:
        """"""
    @overload
    def SetValue(
        self,
        obj: object,
        val: object,
        invokeAttr: BindingFlags,
        binder: Binder,
        culture: CultureInfo,
    ) -> None:
        """"""
    def SetValueDirect(self, obj: TypedReference, value: object) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class FieldOnTypeBuilderInstantiation(FieldInfo, ICustomAttributeProvider, _FieldInfo, _MemberInfo):
    """"""
    @property
    def Attributes(self) -> FieldAttributes:
        """"""
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
        """"""
    @property
    def DeclaringType(self) -> Type:
        """"""
    @property
    def FieldHandle(self) -> RuntimeFieldHandle:
        """"""
    @property
    def FieldType(self) -> Type:
        """"""
    @property
    def IsAssembly(self) -> bool:
        """"""
    @property
    def IsFamily(self) -> bool:
        """"""
    @property
    def IsFamilyAndAssembly(self) -> bool:
        """"""
    @property
    def IsFamilyOrAssembly(self) -> bool:
        """"""
    @property
    def IsInitOnly(self) -> bool:
        """"""
    @property
    def IsLiteral(self) -> bool:
        """"""
    @property
    def IsNotSerialized(self) -> bool:
        """"""
    @property
    def IsPinvokeImpl(self) -> bool:
        """"""
    @property
    def IsPrivate(self) -> bool:
        """"""
    @property
    def IsPublic(self) -> bool:
        """"""
    @property
    def IsSecurityCritical(self) -> bool:
        """"""
    @property
    def IsSecuritySafeCritical(self) -> bool:
        """"""
    @property
    def IsSecurityTransparent(self) -> bool:
        """"""
    @property
    def IsSpecialName(self) -> bool:
        """"""
    @property
    def IsStatic(self) -> bool:
        """"""
    @property
    def MemberType(self) -> MemberTypes:
        """"""
    @property
    def MetadataToken(self) -> int:
        """"""
    @property
    def Module(self) -> Module:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def ReflectedType(self) -> Type:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """"""
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """"""
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    def GetOptionalCustomModifiers(self) -> Array[Type]:
        """"""
    def GetRawConstantValue(self) -> object:
        """"""
    def GetRequiredCustomModifiers(self) -> Array[Type]:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """"""
    def GetTypeInfoCount(self, pcTInfo: UInt32) -> tuple[None, UInt32]:
        """"""
    def GetValue(self, obj: object) -> object:
        """"""
    def GetValueDirect(self, obj: TypedReference) -> object:
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
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """"""
    @overload
    def SetValue(self, obj: object, value: object) -> None:
        """"""
    @overload
    def SetValue(
        self,
        obj: object,
        value: object,
        invokeAttr: BindingFlags,
        binder: Binder,
        culture: CultureInfo,
    ) -> None:
        """"""
    def SetValueDirect(self, obj: TypedReference, value: object) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class FieldToken(ValueType):
    """"""

    Empty: ClassVar[FieldToken]
    """"""
    @property
    def Token(self) -> int:
        """"""
    @overload
    def Equals(self, obj: FieldToken) -> bool:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def op_Equality(cls, a: FieldToken, b: FieldToken) -> bool:
        """"""
    @classmethod
    def op_Inequality(cls, a: FieldToken, b: FieldToken) -> bool:
        """"""
    def __eq__(self, other: FieldToken) -> bool:
        """"""
    def __ne__(self, other: FieldToken) -> bool:
        """"""

class FlowControl(Enum):
    """"""

    Branch: FlowControl = ...
    """"""
    Break: FlowControl = ...
    """"""
    Call: FlowControl = ...
    """"""
    Cond_Branch: FlowControl = ...
    """"""
    Meta: FlowControl = ...
    """"""
    Next: FlowControl = ...
    """"""
    Phi: FlowControl = ...
    """"""
    Return: FlowControl = ...
    """"""
    Throw: FlowControl = ...
    """"""

class GenericFieldInfo(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class GenericMethodInfo(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class GenericTypeParameterBuilder(
    TypeInfo, ICustomAttributeProvider, IReflect, IReflectableType, _MemberInfo, _Type
):
    """"""
    @property
    def Assembly(self) -> Assembly:
        """"""
    @property
    def AssemblyQualifiedName(self) -> str:
        """"""
    @property
    def Attributes(self) -> TypeAttributes:
        """"""
    @property
    def BaseType(self) -> Type:
        """"""
    @property
    def ContainsGenericParameters(self) -> bool:
        """"""
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
        """"""
    @property
    def DeclaredConstructors(self) -> IEnumerable[ConstructorInfo]:
        """"""
    @property
    def DeclaredEvents(self) -> IEnumerable[EventInfo]:
        """"""
    @property
    def DeclaredFields(self) -> IEnumerable[FieldInfo]:
        """"""
    @property
    def DeclaredMembers(self) -> IEnumerable[MemberInfo]:
        """"""
    @property
    def DeclaredMethods(self) -> IEnumerable[MethodInfo]:
        """"""
    @property
    def DeclaredNestedTypes(self) -> IEnumerable[TypeInfo]:
        """"""
    @property
    def DeclaredProperties(self) -> IEnumerable[PropertyInfo]:
        """"""
    @property
    def DeclaringMethod(self) -> MethodBase:
        """"""
    @property
    def DeclaringType(self) -> Type:
        """"""
    @property
    def FullName(self) -> str:
        """"""
    @property
    def GUID(self) -> Guid:
        """"""
    @property
    def GenericParameterAttributes(self) -> GenericParameterAttributes:
        """"""
    @property
    def GenericParameterPosition(self) -> int:
        """"""
    @property
    def GenericTypeArguments(self) -> Array[Type]:
        """"""
    @property
    def GenericTypeParameters(self) -> Array[Type]:
        """"""
    @property
    def HasElementType(self) -> bool:
        """"""
    @property
    def ImplementedInterfaces(self) -> IEnumerable[Type]:
        """"""
    @property
    def IsAbstract(self) -> bool:
        """"""
    @property
    def IsAnsiClass(self) -> bool:
        """"""
    @property
    def IsArray(self) -> bool:
        """"""
    @property
    def IsAutoClass(self) -> bool:
        """"""
    @property
    def IsAutoLayout(self) -> bool:
        """"""
    @property
    def IsByRef(self) -> bool:
        """"""
    @property
    def IsCOMObject(self) -> bool:
        """"""
    @property
    def IsClass(self) -> bool:
        """"""
    @property
    def IsConstructedGenericType(self) -> bool:
        """"""
    @property
    def IsContextful(self) -> bool:
        """"""
    @property
    def IsEnum(self) -> bool:
        """"""
    @property
    def IsExplicitLayout(self) -> bool:
        """"""
    @property
    def IsGenericParameter(self) -> bool:
        """"""
    @property
    def IsGenericType(self) -> bool:
        """"""
    @property
    def IsGenericTypeDefinition(self) -> bool:
        """"""
    @property
    def IsImport(self) -> bool:
        """"""
    @property
    def IsInterface(self) -> bool:
        """"""
    @property
    def IsLayoutSequential(self) -> bool:
        """"""
    @property
    def IsMarshalByRef(self) -> bool:
        """"""
    @property
    def IsNested(self) -> bool:
        """"""
    @property
    def IsNestedAssembly(self) -> bool:
        """"""
    @property
    def IsNestedFamANDAssem(self) -> bool:
        """"""
    @property
    def IsNestedFamORAssem(self) -> bool:
        """"""
    @property
    def IsNestedFamily(self) -> bool:
        """"""
    @property
    def IsNestedPrivate(self) -> bool:
        """"""
    @property
    def IsNestedPublic(self) -> bool:
        """"""
    @property
    def IsNotPublic(self) -> bool:
        """"""
    @property
    def IsPointer(self) -> bool:
        """"""
    @property
    def IsPrimitive(self) -> bool:
        """"""
    @property
    def IsPublic(self) -> bool:
        """"""
    @property
    def IsSealed(self) -> bool:
        """"""
    @property
    def IsSecurityCritical(self) -> bool:
        """"""
    @property
    def IsSecuritySafeCritical(self) -> bool:
        """"""
    @property
    def IsSecurityTransparent(self) -> bool:
        """"""
    @property
    def IsSerializable(self) -> bool:
        """"""
    @property
    def IsSpecialName(self) -> bool:
        """"""
    @property
    def IsUnicodeClass(self) -> bool:
        """"""
    @property
    def IsValueType(self) -> bool:
        """"""
    @property
    def IsVisible(self) -> bool:
        """"""
    @property
    def MemberType(self) -> MemberTypes:
        """"""
    @property
    def MetadataToken(self) -> int:
        """"""
    @property
    def Module(self) -> Module:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def Namespace(self) -> str:
        """"""
    @property
    def ReflectedType(self) -> Type:
        """"""
    @property
    def StructLayoutAttribute(self) -> StructLayoutAttribute:
        """"""
    @property
    def TypeHandle(self) -> RuntimeTypeHandle:
        """"""
    @property
    def TypeInitializer(self) -> ConstructorInfo:
        """"""
    @property
    def UnderlyingSystemType(self) -> Type:
        """"""
    def AsType(self) -> Type:
        """"""
    @overload
    def Equals(self, o: object) -> bool:
        """"""
    @overload
    def Equals(self, o: Type) -> bool:
        """"""
    def FindInterfaces(self, filter: TypeFilter, filterCriteria: object) -> Array[Type]:
        """"""
    def FindMembers(
        self,
        memberType: MemberTypes,
        bindingAttr: BindingFlags,
        filter: MemberFilter,
        filterCriteria: object,
    ) -> Array[MemberInfo]:
        """"""
    def GetArrayRank(self) -> int:
        """"""
    @overload
    def GetConstructor(
        self,
        bindingAttr: BindingFlags,
        binder: Binder,
        callConvention: CallingConventions,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> ConstructorInfo:
        """"""
    @overload
    def GetConstructor(
        self,
        bindingAttr: BindingFlags,
        binder: Binder,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> ConstructorInfo:
        """"""
    @overload
    def GetConstructor(self, types: Array[Type]) -> ConstructorInfo:
        """"""
    @overload
    def GetConstructors(self) -> Array[ConstructorInfo]:
        """"""
    @overload
    def GetConstructors(self, bindingAttr: BindingFlags) -> Array[ConstructorInfo]:
        """"""
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """"""
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """"""
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]:
        """"""
    def GetDeclaredEvent(self, name: str) -> EventInfo:
        """"""
    def GetDeclaredField(self, name: str) -> FieldInfo:
        """"""
    def GetDeclaredMethod(self, name: str) -> MethodInfo:
        """"""
    def GetDeclaredMethods(self, name: str) -> IEnumerable[MethodInfo]:
        """"""
    def GetDeclaredNestedType(self, name: str) -> TypeInfo:
        """"""
    def GetDeclaredProperty(self, name: str) -> PropertyInfo:
        """"""
    def GetDefaultMembers(self) -> Array[MemberInfo]:
        """"""
    def GetElementType(self) -> Type:
        """"""
    def GetEnumName(self, value: object) -> str:
        """"""
    def GetEnumNames(self) -> Array[str]:
        """"""
    def GetEnumUnderlyingType(self) -> Type:
        """"""
    def GetEnumValues(self) -> Array:
        """"""
    @overload
    def GetEvent(self, name: str) -> EventInfo:
        """"""
    @overload
    def GetEvent(self, name: str, bindingAttr: BindingFlags) -> EventInfo:
        """"""
    @overload
    def GetEvents(self) -> Array[EventInfo]:
        """"""
    @overload
    def GetEvents(self, bindingAttr: BindingFlags) -> Array[EventInfo]:
        """"""
    @overload
    def GetField(self, name: str) -> FieldInfo:
        """"""
    @overload
    def GetField(self, name: str, bindingAttr: BindingFlags) -> FieldInfo:
        """"""
    @overload
    def GetFields(self) -> Array[FieldInfo]:
        """"""
    @overload
    def GetFields(self, bindingAttr: BindingFlags) -> Array[FieldInfo]:
        """"""
    def GetGenericArguments(self) -> Array[Type]:
        """"""
    def GetGenericParameterConstraints(self) -> Array[Type]:
        """"""
    def GetGenericTypeDefinition(self) -> Type:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    @overload
    def GetInterface(self, name: str) -> Type:
        """"""
    @overload
    def GetInterface(self, name: str, ignoreCase: bool) -> Type:
        """"""
    def GetInterfaceMap(self, interfaceType: Type) -> InterfaceMapping:
        """"""
    def GetInterfaces(self) -> Array[Type]:
        """"""
    @overload
    def GetMember(self, name: str) -> Array[MemberInfo]:
        """"""
    @overload
    def GetMember(self, name: str, bindingAttr: BindingFlags) -> Array[MemberInfo]:
        """"""
    @overload
    def GetMember(
        self, name: str, type: MemberTypes, bindingAttr: BindingFlags
    ) -> Array[MemberInfo]:
        """"""
    @overload
    def GetMembers(self) -> Array[MemberInfo]:
        """"""
    @overload
    def GetMembers(self, bindingAttr: BindingFlags) -> Array[MemberInfo]:
        """"""
    @overload
    def GetMethod(self, name: str) -> MethodInfo:
        """"""
    @overload
    def GetMethod(self, name: str, bindingAttr: BindingFlags) -> MethodInfo:
        """"""
    @overload
    def GetMethod(
        self,
        name: str,
        bindingAttr: BindingFlags,
        binder: Binder,
        callConvention: CallingConventions,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> MethodInfo:
        """"""
    @overload
    def GetMethod(
        self,
        name: str,
        bindingAttr: BindingFlags,
        binder: Binder,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> MethodInfo:
        """"""
    @overload
    def GetMethod(self, name: str, types: Array[Type]) -> MethodInfo:
        """"""
    @overload
    def GetMethod(
        self, name: str, types: Array[Type], modifiers: Array[ParameterModifier]
    ) -> MethodInfo:
        """"""
    @overload
    def GetMethods(self) -> Array[MethodInfo]:
        """"""
    @overload
    def GetMethods(self, bindingAttr: BindingFlags) -> Array[MethodInfo]:
        """"""
    @overload
    def GetNestedType(self, name: str) -> Type:
        """"""
    @overload
    def GetNestedType(self, name: str, bindingAttr: BindingFlags) -> Type:
        """"""
    @overload
    def GetNestedTypes(self) -> Array[Type]:
        """"""
    @overload
    def GetNestedTypes(self, bindingAttr: BindingFlags) -> Array[Type]:
        """"""
    @overload
    def GetProperties(self) -> Array[PropertyInfo]:
        """"""
    @overload
    def GetProperties(self, bindingAttr: BindingFlags) -> Array[PropertyInfo]:
        """"""
    @overload
    def GetProperty(self, name: str) -> PropertyInfo:
        """"""
    @overload
    def GetProperty(self, name: str, bindingAttr: BindingFlags) -> PropertyInfo:
        """"""
    @overload
    def GetProperty(
        self,
        name: str,
        bindingAttr: BindingFlags,
        binder: Binder,
        returnType: Type,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> PropertyInfo:
        """"""
    @overload
    def GetProperty(self, name: str, types: Array[Type]) -> PropertyInfo:
        """"""
    @overload
    def GetProperty(self, name: str, returnType: Type) -> PropertyInfo:
        """"""
    @overload
    def GetProperty(self, name: str, returnType: Type, types: Array[Type]) -> PropertyInfo:
        """"""
    @overload
    def GetProperty(
        self, name: str, returnType: Type, types: Array[Type], modifiers: Array[ParameterModifier]
    ) -> PropertyInfo:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def GetTypeInfo(self) -> TypeInfo:
        """"""
    @overload
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
    @overload
    def InvokeMember(
        self,
        name: str,
        invokeAttr: BindingFlags,
        binder: Binder,
        target: object,
        args: Array[object],
    ) -> object:
        """"""
    @overload
    def InvokeMember(
        self,
        name: str,
        invokeAttr: BindingFlags,
        binder: Binder,
        target: object,
        args: Array[object],
        culture: CultureInfo,
    ) -> object:
        """"""
    @overload
    def InvokeMember(
        self,
        name: str,
        invokeAttr: BindingFlags,
        binder: Binder,
        target: object,
        args: Array[object],
        modifiers: Array[ParameterModifier],
        culture: CultureInfo,
        namedParameters: Array[str],
    ) -> object:
        """"""
    @overload
    def IsAssignableFrom(self, typeInfo: TypeInfo) -> bool:
        """"""
    @overload
    def IsAssignableFrom(self, c: Type) -> bool:
        """"""
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """"""
    def IsEnumDefined(self, value: object) -> bool:
        """"""
    def IsEquivalentTo(self, other: Type) -> bool:
        """"""
    def IsInstanceOfType(self, o: object) -> bool:
        """"""
    def IsSubclassOf(self, c: Type) -> bool:
        """"""
    @overload
    def MakeArrayType(self) -> Type:
        """"""
    @overload
    def MakeArrayType(self, rank: int) -> Type:
        """"""
    def MakeByRefType(self) -> Type:
        """"""
    def MakeGenericType(self, typeArguments: Array[Type]) -> Type:
        """"""
    def MakePointerType(self) -> Type:
        """"""
    def SetBaseTypeConstraint(self, baseTypeConstraint: Type) -> None:
        """"""
    @overload
    def SetCustomAttribute(self, customBuilder: CustomAttributeBuilder) -> None:
        """"""
    @overload
    def SetCustomAttribute(self, con: ConstructorInfo, binaryAttribute: Array[int]) -> None:
        """"""
    def SetGenericParameterAttributes(
        self, genericParameterAttributes: GenericParameterAttributes
    ) -> None:
        """"""
    def SetInterfaceConstraints(self, interfaceConstraints: Array[Type]) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class ILGenerator(Object, _ILGenerator):
    """"""
    @property
    def ILOffset(self) -> int:
        """"""
    def BeginCatchBlock(self, exceptionType: Type) -> None:
        """"""
    def BeginExceptFilterBlock(self) -> None:
        """"""
    def BeginExceptionBlock(self) -> Label:
        """"""
    def BeginFaultBlock(self) -> None:
        """"""
    def BeginFinallyBlock(self) -> None:
        """"""
    def BeginScope(self) -> None:
        """"""
    @overload
    def DeclareLocal(self, localType: Type) -> LocalBuilder:
        """"""
    @overload
    def DeclareLocal(self, localType: Type, pinned: bool) -> LocalBuilder:
        """"""
    def DefineLabel(self) -> Label:
        """"""
    @overload
    def Emit(self, opcode: OpCode) -> None:
        """"""
    @overload
    def Emit(self, opcode: OpCode, label: Label) -> None:
        """"""
    @overload
    def Emit(self, opcode: OpCode, local: LocalBuilder) -> None:
        """"""
    @overload
    def Emit(self, opcode: OpCode, signature: SignatureHelper) -> None:
        """"""
    @overload
    def Emit(self, opcode: OpCode, con: ConstructorInfo) -> None:
        """"""
    @overload
    def Emit(self, opcode: OpCode, field: FieldInfo) -> None:
        """"""
    @overload
    def Emit(self, opcode: OpCode, meth: MethodInfo) -> None:
        """"""
    @overload
    def Emit(self, opcode: OpCode, labels: Array[Label]) -> None:
        """"""
    @overload
    def Emit(self, opcode: OpCode, arg: int) -> None:
        """"""
    @overload
    def Emit(self, opcode: OpCode, arg: float) -> None:
        """"""
    @overload
    def Emit(self, opcode: OpCode, arg: int) -> None:
        """"""
    @overload
    def Emit(self, opcode: OpCode, arg: int) -> None:
        """"""
    @overload
    def Emit(self, opcode: OpCode, arg: int) -> None:
        """"""
    @overload
    def Emit(self, opcode: OpCode, arg: int) -> None:
        """"""
    @overload
    def Emit(self, opcode: OpCode, arg: float) -> None:
        """"""
    @overload
    def Emit(self, opcode: OpCode, str: str) -> None:
        """"""
    @overload
    def Emit(self, opcode: OpCode, cls: Type) -> None:
        """"""
    def EmitCall(
        self, opcode: OpCode, methodInfo: MethodInfo, optionalParameterTypes: Array[Type]
    ) -> None:
        """"""
    @overload
    def EmitCalli(
        self,
        opcode: OpCode,
        callingConvention: CallingConventions,
        returnType: Type,
        parameterTypes: Array[Type],
        optionalParameterTypes: Array[Type],
    ) -> None:
        """"""
    @overload
    def EmitCalli(
        self,
        opcode: OpCode,
        unmanagedCallConv: CallingConvention,
        returnType: Type,
        parameterTypes: Array[Type],
    ) -> None:
        """"""
    @overload
    def EmitWriteLine(self, localBuilder: LocalBuilder) -> None:
        """"""
    @overload
    def EmitWriteLine(self, fld: FieldInfo) -> None:
        """"""
    @overload
    def EmitWriteLine(self, value: str) -> None:
        """"""
    def EndExceptionBlock(self) -> None:
        """"""
    def EndScope(self) -> None:
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
    def MarkLabel(self, loc: Label) -> None:
        """"""
    def MarkSequencePoint(
        self,
        document: ISymbolDocumentWriter,
        startLine: int,
        startColumn: int,
        endLine: int,
        endColumn: int,
    ) -> None:
        """"""
    def ThrowException(self, excType: Type) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def UsingNamespace(self, usingNamespace: str) -> None:
        """"""

class InternalAssemblyBuilder(
    RuntimeAssembly,
    ICustomAttributeProvider,
    ICustomQueryInterface,
    _Assembly,
    ISerializable,
    IEvidenceFactory,
):
    """"""
    @property
    def CodeBase(self) -> str:
        """"""
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
        """"""
    @property
    def DefinedTypes(self) -> IEnumerable[TypeInfo]:
        """"""
    @property
    def EntryPoint(self) -> MethodInfo:
        """"""
    @property
    def EscapedCodeBase(self) -> str:
        """"""
    @property
    def Evidence(self) -> Evidence:
        """"""
    @property
    def ExportedTypes(self) -> IEnumerable[Type]:
        """"""
    @property
    def FullName(self) -> str:
        """"""
    @property
    def GlobalAssemblyCache(self) -> bool:
        """"""
    @property
    def HostContext(self) -> int:
        """"""
    @property
    def ImageRuntimeVersion(self) -> str:
        """"""
    @property
    def IsDynamic(self) -> bool:
        """"""
    @property
    def IsFullyTrusted(self) -> bool:
        """"""
    @property
    def Location(self) -> str:
        """"""
    @property
    def ManifestModule(self) -> Module:
        """"""
    @property
    def Modules(self) -> IEnumerable[Module]:
        """"""
    @property
    def PermissionSet(self) -> PermissionSet:
        """"""
    @property
    def ReflectionOnly(self) -> bool:
        """"""
    @property
    def SecurityRuleSet(self) -> SecurityRuleSet:
        """"""
    @overload
    def CreateInstance(self, typeName: str) -> object:
        """"""
    @overload
    def CreateInstance(self, typeName: str, ignoreCase: bool) -> object:
        """"""
    @overload
    def CreateInstance(
        self,
        typeName: str,
        ignoreCase: bool,
        bindingAttr: BindingFlags,
        binder: Binder,
        args: Array[object],
        culture: CultureInfo,
        activationAttributes: Array[object],
    ) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """"""
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """"""
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]:
        """"""
    def GetExportedTypes(self) -> Array[Type]:
        """"""
    def GetFile(self, name: str) -> FileStream:
        """"""
    @overload
    def GetFiles(self) -> Array[FileStream]:
        """"""
    @overload
    def GetFiles(self, getResourceModules: bool) -> Array[FileStream]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetInterface(self, iid: Guid, ppv: IntPtr) -> tuple[CustomQueryInterfaceResult, IntPtr]:
        """"""
    @overload
    def GetLoadedModules(self) -> Array[Module]:
        """"""
    @overload
    def GetLoadedModules(self, getResourceModules: bool) -> Array[Module]:
        """"""
    def GetManifestResourceInfo(self, resourceName: str) -> ManifestResourceInfo:
        """"""
    def GetManifestResourceNames(self) -> Array[str]:
        """"""
    @overload
    def GetManifestResourceStream(self, name: str) -> Stream:
        """"""
    @overload
    def GetManifestResourceStream(self, type: Type, name: str) -> Stream:
        """"""
    def GetModule(self, name: str) -> Module:
        """"""
    @overload
    def GetModules(self) -> Array[Module]:
        """"""
    @overload
    def GetModules(self, getResourceModules: bool) -> Array[Module]:
        """"""
    @overload
    def GetName(self) -> AssemblyName:
        """"""
    @overload
    def GetName(self, copiedName: bool) -> AssemblyName:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetReferencedAssemblies(self) -> Array[AssemblyName]:
        """"""
    @overload
    def GetSatelliteAssembly(self, culture: CultureInfo) -> Assembly:
        """"""
    @overload
    def GetSatelliteAssembly(self, culture: CultureInfo, version: Version) -> Assembly:
        """"""
    @overload
    def GetType(self) -> Type:
        """"""
    @overload
    def GetType(self, name: str) -> Type:
        """"""
    @overload
    def GetType(self, name: str, throwOnError: bool) -> Type:
        """"""
    @overload
    def GetType(self, name: str, throwOnError: bool, ignoreCase: bool) -> Type:
        """"""
    def GetTypes(self) -> Array[Type]:
        """"""
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """"""
    @overload
    def LoadModule(self, moduleName: str, rawModule: Array[int]) -> Module:
        """"""
    @overload
    def LoadModule(
        self, moduleName: str, rawModule: Array[int], rawSymbolStore: Array[int]
    ) -> Module:
        """"""
    def ToString(self) -> str:
        """"""
    ModuleResolve: EventType[ModuleResolveEventHandler] = ...
    """"""

class InternalModuleBuilder(RuntimeModule, ICustomAttributeProvider, _Module, ISerializable):
    """"""
    @property
    def Assembly(self) -> Assembly:
        """"""
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
        """"""
    @property
    def FullyQualifiedName(self) -> str:
        """"""
    @property
    def MDStreamVersion(self) -> int:
        """"""
    @property
    def MetadataToken(self) -> int:
        """"""
    @property
    def ModuleHandle(self) -> ModuleHandle:
        """"""
    @property
    def ModuleVersionId(self) -> Guid:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def ScopeName(self) -> str:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def FindTypes(self, filter: TypeFilter, filterCriteria: object) -> Array[Type]:
        """"""
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """"""
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """"""
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]:
        """"""
    @overload
    def GetField(self, name: str) -> FieldInfo:
        """"""
    @overload
    def GetField(self, name: str, bindingAttr: BindingFlags) -> FieldInfo:
        """"""
    @overload
    def GetFields(self) -> Array[FieldInfo]:
        """"""
    @overload
    def GetFields(self, bindingFlags: BindingFlags) -> Array[FieldInfo]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    @overload
    def GetMethod(self, name: str) -> MethodInfo:
        """"""
    @overload
    def GetMethod(
        self,
        name: str,
        bindingAttr: BindingFlags,
        binder: Binder,
        callConvention: CallingConventions,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> MethodInfo:
        """"""
    @overload
    def GetMethod(self, name: str, types: Array[Type]) -> MethodInfo:
        """"""
    @overload
    def GetMethods(self) -> Array[MethodInfo]:
        """"""
    @overload
    def GetMethods(self, bindingFlags: BindingFlags) -> Array[MethodInfo]:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetPEKind(
        self, peKind: PortableExecutableKinds, machine: ImageFileMachine
    ) -> tuple[None, PortableExecutableKinds, ImageFileMachine]:
        """"""
    def GetSignerCertificate(self) -> X509Certificate:
        """"""
    @overload
    def GetType(self) -> Type:
        """"""
    @overload
    def GetType(self, className: str) -> Type:
        """"""
    @overload
    def GetType(self, className: str, ignoreCase: bool) -> Type:
        """"""
    @overload
    def GetType(self, className: str, throwOnError: bool, ignoreCase: bool) -> Type:
        """"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """"""
    def GetTypeInfoCount(self, pcTInfo: UInt32) -> tuple[None, UInt32]:
        """"""
    def GetTypes(self) -> Array[Type]:
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
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """"""
    def IsResource(self) -> bool:
        """"""
    @overload
    def ResolveField(self, metadataToken: int) -> FieldInfo:
        """"""
    @overload
    def ResolveField(
        self,
        metadataToken: int,
        genericTypeArguments: Array[Type],
        genericMethodArguments: Array[Type],
    ) -> FieldInfo:
        """"""
    @overload
    def ResolveMember(self, metadataToken: int) -> MemberInfo:
        """"""
    @overload
    def ResolveMember(
        self,
        metadataToken: int,
        genericTypeArguments: Array[Type],
        genericMethodArguments: Array[Type],
    ) -> MemberInfo:
        """"""
    @overload
    def ResolveMethod(self, metadataToken: int) -> MethodBase:
        """"""
    @overload
    def ResolveMethod(
        self,
        metadataToken: int,
        genericTypeArguments: Array[Type],
        genericMethodArguments: Array[Type],
    ) -> MethodBase:
        """"""
    def ResolveSignature(self, metadataToken: int) -> Array[int]:
        """"""
    def ResolveString(self, metadataToken: int) -> str:
        """"""
    @overload
    def ResolveType(self, metadataToken: int) -> Type:
        """"""
    @overload
    def ResolveType(
        self,
        metadataToken: int,
        genericTypeArguments: Array[Type],
        genericMethodArguments: Array[Type],
    ) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class Label(ValueType):
    """"""
    @overload
    def Equals(self, obj: Label) -> bool:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def op_Equality(cls, a: Label, b: Label) -> bool:
        """"""
    @classmethod
    def op_Inequality(cls, a: Label, b: Label) -> bool:
        """"""
    def __eq__(self, other: Label) -> bool:
        """"""
    def __ne__(self, other: Label) -> bool:
        """"""

class LineNumberInfo(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class LocalBuilder(LocalVariableInfo, _LocalBuilder):
    """"""
    @property
    def IsPinned(self) -> bool:
        """"""
    @property
    def LocalIndex(self) -> int:
        """"""
    @property
    def LocalType(self) -> Type:
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
    @overload
    def SetLocalSymInfo(self, name: str) -> None:
        """"""
    @overload
    def SetLocalSymInfo(self, name: str, startOffset: int, endOffset: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class LocalSymInfo(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class MethodBuilder(
    MethodInfo, ICustomAttributeProvider, _MemberInfo, _MethodBase, _MethodBuilder, _MethodInfo
):
    """"""
    @property
    def Attributes(self) -> MethodAttributes:
        """"""
    @property
    def CallingConvention(self) -> CallingConventions:
        """"""
    @property
    def ContainsGenericParameters(self) -> bool:
        """"""
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
        """"""
    @property
    def DeclaringType(self) -> Type:
        """"""
    @property
    def InitLocals(self) -> bool:
        """"""
    @InitLocals.setter
    def InitLocals(self, value: bool) -> None: ...
    @property
    def IsAbstract(self) -> bool:
        """"""
    @property
    def IsAssembly(self) -> bool:
        """"""
    @property
    def IsConstructor(self) -> bool:
        """"""
    @property
    def IsFamily(self) -> bool:
        """"""
    @property
    def IsFamilyAndAssembly(self) -> bool:
        """"""
    @property
    def IsFamilyOrAssembly(self) -> bool:
        """"""
    @property
    def IsFinal(self) -> bool:
        """"""
    @property
    def IsGenericMethod(self) -> bool:
        """"""
    @property
    def IsGenericMethodDefinition(self) -> bool:
        """"""
    @property
    def IsHideBySig(self) -> bool:
        """"""
    @property
    def IsPrivate(self) -> bool:
        """"""
    @property
    def IsPublic(self) -> bool:
        """"""
    @property
    def IsSecurityCritical(self) -> bool:
        """"""
    @property
    def IsSecuritySafeCritical(self) -> bool:
        """"""
    @property
    def IsSecurityTransparent(self) -> bool:
        """"""
    @property
    def IsSpecialName(self) -> bool:
        """"""
    @property
    def IsStatic(self) -> bool:
        """"""
    @property
    def IsVirtual(self) -> bool:
        """"""
    @property
    def MemberType(self) -> MemberTypes:
        """"""
    @property
    def MetadataToken(self) -> int:
        """"""
    @property
    def MethodHandle(self) -> RuntimeMethodHandle:
        """"""
    @property
    def MethodImplementationFlags(self) -> MethodImplAttributes:
        """"""
    @property
    def Module(self) -> Module:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def ReflectedType(self) -> Type:
        """"""
    @property
    def ReturnParameter(self) -> ParameterInfo:
        """"""
    @property
    def ReturnType(self) -> Type:
        """"""
    @property
    def ReturnTypeCustomAttributes(self) -> ICustomAttributeProvider:
        """"""
    @property
    def Signature(self) -> str:
        """"""
    def AddDeclarativeSecurity(self, action: SecurityAction, pset: PermissionSet) -> None:
        """"""
    @overload
    def CreateDelegate(self, delegateType: Type) -> Delegate:
        """"""
    @overload
    def CreateDelegate(self, delegateType: Type, target: object) -> Delegate:
        """"""
    def CreateMethodBody(self, il: Array[int], count: int) -> None:
        """"""
    def DefineGenericParameters(self, names: Array[str]) -> Array[GenericTypeParameterBuilder]:
        """"""
    def DefineParameter(
        self, position: int, attributes: ParameterAttributes, strParamName: str
    ) -> ParameterBuilder:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetBaseDefinition(self) -> MethodInfo:
        """"""
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """"""
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """"""
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]:
        """"""
    def GetGenericArguments(self) -> Array[Type]:
        """"""
    def GetGenericMethodDefinition(self) -> MethodInfo:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    @overload
    def GetILGenerator(self) -> ILGenerator:
        """"""
    @overload
    def GetILGenerator(self, size: int) -> ILGenerator:
        """"""
    def GetMethodBody(self) -> MethodBody:
        """"""
    def GetMethodImplementationFlags(self) -> MethodImplAttributes:
        """"""
    def GetModule(self) -> Module:
        """"""
    def GetParameters(self) -> Array[ParameterInfo]:
        """"""
    def GetToken(self) -> MethodToken:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """"""
    def GetTypeInfoCount(self, pcTInfo: UInt32) -> tuple[None, UInt32]:
        """"""
    @overload
    def Invoke(
        self,
        obj: object,
        invokeAttr: BindingFlags,
        binder: Binder,
        parameters: Array[object],
        culture: CultureInfo,
    ) -> object:
        """"""
    @overload
    def Invoke(self, obj: object, parameters: Array[object]) -> object:
        """"""
    @overload
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
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """"""
    def MakeGenericMethod(self, typeArguments: Array[Type]) -> MethodInfo:
        """"""
    @overload
    def SetCustomAttribute(self, customBuilder: CustomAttributeBuilder) -> None:
        """"""
    @overload
    def SetCustomAttribute(self, con: ConstructorInfo, binaryAttribute: Array[int]) -> None:
        """"""
    def SetImplementationFlags(self, attributes: MethodImplAttributes) -> None:
        """"""
    def SetMarshal(self, unmanagedMarshal: UnmanagedMarshal) -> None:
        """"""
    def SetMethodBody(
        self,
        il: Array[int],
        maxStack: int,
        localSignature: Array[int],
        exceptionHandlers: IEnumerable[ExceptionHandler],
        tokenFixups: IEnumerable[int],
    ) -> None:
        """"""
    def SetParameters(self, parameterTypes: Array[Type]) -> None:
        """"""
    def SetReturnType(self, returnType: Type) -> None:
        """"""
    def SetSignature(
        self,
        returnType: Type,
        returnTypeRequiredCustomModifiers: Array[Type],
        returnTypeOptionalCustomModifiers: Array[Type],
        parameterTypes: Array[Type],
        parameterTypeRequiredCustomModifiers: Array[Array[Type]],
        parameterTypeOptionalCustomModifiers: Array[Array[Type]],
    ) -> None:
        """"""
    def SetSymCustomAttribute(self, name: str, data: Array[int]) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class MethodBuilderInstantiation(
    MethodInfo, ICustomAttributeProvider, _MemberInfo, _MethodBase, _MethodInfo
):
    """"""
    @property
    def Attributes(self) -> MethodAttributes:
        """"""
    @property
    def CallingConvention(self) -> CallingConventions:
        """"""
    @property
    def ContainsGenericParameters(self) -> bool:
        """"""
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
        """"""
    @property
    def DeclaringType(self) -> Type:
        """"""
    @property
    def IsAbstract(self) -> bool:
        """"""
    @property
    def IsAssembly(self) -> bool:
        """"""
    @property
    def IsConstructor(self) -> bool:
        """"""
    @property
    def IsFamily(self) -> bool:
        """"""
    @property
    def IsFamilyAndAssembly(self) -> bool:
        """"""
    @property
    def IsFamilyOrAssembly(self) -> bool:
        """"""
    @property
    def IsFinal(self) -> bool:
        """"""
    @property
    def IsGenericMethod(self) -> bool:
        """"""
    @property
    def IsGenericMethodDefinition(self) -> bool:
        """"""
    @property
    def IsHideBySig(self) -> bool:
        """"""
    @property
    def IsPrivate(self) -> bool:
        """"""
    @property
    def IsPublic(self) -> bool:
        """"""
    @property
    def IsSecurityCritical(self) -> bool:
        """"""
    @property
    def IsSecuritySafeCritical(self) -> bool:
        """"""
    @property
    def IsSecurityTransparent(self) -> bool:
        """"""
    @property
    def IsSpecialName(self) -> bool:
        """"""
    @property
    def IsStatic(self) -> bool:
        """"""
    @property
    def IsVirtual(self) -> bool:
        """"""
    @property
    def MemberType(self) -> MemberTypes:
        """"""
    @property
    def MetadataToken(self) -> int:
        """"""
    @property
    def MethodHandle(self) -> RuntimeMethodHandle:
        """"""
    @property
    def MethodImplementationFlags(self) -> MethodImplAttributes:
        """"""
    @property
    def Module(self) -> Module:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def ReflectedType(self) -> Type:
        """"""
    @property
    def ReturnParameter(self) -> ParameterInfo:
        """"""
    @property
    def ReturnType(self) -> Type:
        """"""
    @property
    def ReturnTypeCustomAttributes(self) -> ICustomAttributeProvider:
        """"""
    @overload
    def CreateDelegate(self, delegateType: Type) -> Delegate:
        """"""
    @overload
    def CreateDelegate(self, delegateType: Type, target: object) -> Delegate:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetBaseDefinition(self) -> MethodInfo:
        """"""
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """"""
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """"""
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]:
        """"""
    def GetGenericArguments(self) -> Array[Type]:
        """"""
    def GetGenericMethodDefinition(self) -> MethodInfo:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    def GetMethodBody(self) -> MethodBody:
        """"""
    def GetMethodImplementationFlags(self) -> MethodImplAttributes:
        """"""
    def GetParameters(self) -> Array[ParameterInfo]:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """"""
    def GetTypeInfoCount(self, pcTInfo: UInt32) -> tuple[None, UInt32]:
        """"""
    @overload
    def Invoke(
        self,
        obj: object,
        invokeAttr: BindingFlags,
        binder: Binder,
        parameters: Array[object],
        culture: CultureInfo,
    ) -> object:
        """"""
    @overload
    def Invoke(self, obj: object, parameters: Array[object]) -> object:
        """"""
    @overload
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
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """"""
    def MakeGenericMethod(self, arguments: Array[Type]) -> MethodInfo:
        """"""
    def ToString(self) -> str:
        """"""

class MethodOnTypeBuilderInstantiation(
    MethodInfo, ICustomAttributeProvider, _MemberInfo, _MethodBase, _MethodInfo
):
    """"""
    @property
    def Attributes(self) -> MethodAttributes:
        """"""
    @property
    def CallingConvention(self) -> CallingConventions:
        """"""
    @property
    def ContainsGenericParameters(self) -> bool:
        """"""
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
        """"""
    @property
    def DeclaringType(self) -> Type:
        """"""
    @property
    def IsAbstract(self) -> bool:
        """"""
    @property
    def IsAssembly(self) -> bool:
        """"""
    @property
    def IsConstructor(self) -> bool:
        """"""
    @property
    def IsFamily(self) -> bool:
        """"""
    @property
    def IsFamilyAndAssembly(self) -> bool:
        """"""
    @property
    def IsFamilyOrAssembly(self) -> bool:
        """"""
    @property
    def IsFinal(self) -> bool:
        """"""
    @property
    def IsGenericMethod(self) -> bool:
        """"""
    @property
    def IsGenericMethodDefinition(self) -> bool:
        """"""
    @property
    def IsHideBySig(self) -> bool:
        """"""
    @property
    def IsPrivate(self) -> bool:
        """"""
    @property
    def IsPublic(self) -> bool:
        """"""
    @property
    def IsSecurityCritical(self) -> bool:
        """"""
    @property
    def IsSecuritySafeCritical(self) -> bool:
        """"""
    @property
    def IsSecurityTransparent(self) -> bool:
        """"""
    @property
    def IsSpecialName(self) -> bool:
        """"""
    @property
    def IsStatic(self) -> bool:
        """"""
    @property
    def IsVirtual(self) -> bool:
        """"""
    @property
    def MemberType(self) -> MemberTypes:
        """"""
    @property
    def MetadataToken(self) -> int:
        """"""
    @property
    def MethodHandle(self) -> RuntimeMethodHandle:
        """"""
    @property
    def MethodImplementationFlags(self) -> MethodImplAttributes:
        """"""
    @property
    def Module(self) -> Module:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def ReflectedType(self) -> Type:
        """"""
    @property
    def ReturnParameter(self) -> ParameterInfo:
        """"""
    @property
    def ReturnType(self) -> Type:
        """"""
    @property
    def ReturnTypeCustomAttributes(self) -> ICustomAttributeProvider:
        """"""
    @overload
    def CreateDelegate(self, delegateType: Type) -> Delegate:
        """"""
    @overload
    def CreateDelegate(self, delegateType: Type, target: object) -> Delegate:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetBaseDefinition(self) -> MethodInfo:
        """"""
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """"""
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """"""
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]:
        """"""
    def GetGenericArguments(self) -> Array[Type]:
        """"""
    def GetGenericMethodDefinition(self) -> MethodInfo:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    def GetMethodBody(self) -> MethodBody:
        """"""
    def GetMethodImplementationFlags(self) -> MethodImplAttributes:
        """"""
    def GetParameters(self) -> Array[ParameterInfo]:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """"""
    def GetTypeInfoCount(self, pcTInfo: UInt32) -> tuple[None, UInt32]:
        """"""
    @overload
    def Invoke(
        self,
        obj: object,
        invokeAttr: BindingFlags,
        binder: Binder,
        parameters: Array[object],
        culture: CultureInfo,
    ) -> object:
        """"""
    @overload
    def Invoke(self, obj: object, parameters: Array[object]) -> object:
        """"""
    @overload
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
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """"""
    def MakeGenericMethod(self, typeArgs: Array[Type]) -> MethodInfo:
        """"""
    def ToString(self) -> str:
        """"""

class MethodRental(Object, _MethodRental):
    """"""

    JitImmediate: ClassVar[int]
    """"""
    JitOnDemand: ClassVar[int]
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
    @classmethod
    def SwapMethodBody(
        cls, cls: Type, methodtoken: int, rgIL: IntPtr, methodSize: int, flags: int
    ) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class MethodToken(ValueType):
    """"""

    Empty: ClassVar[MethodToken]
    """"""
    @property
    def Token(self) -> int:
        """"""
    @overload
    def Equals(self, obj: MethodToken) -> bool:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def op_Equality(cls, a: MethodToken, b: MethodToken) -> bool:
        """"""
    @classmethod
    def op_Inequality(cls, a: MethodToken, b: MethodToken) -> bool:
        """"""
    def __eq__(self, other: MethodToken) -> bool:
        """"""
    def __ne__(self, other: MethodToken) -> bool:
        """"""

class ModuleBuilder(Module, ICustomAttributeProvider, _Module, _ModuleBuilder, ISerializable):
    """"""
    @property
    def Assembly(self) -> Assembly:
        """"""
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
        """"""
    @property
    def FullyQualifiedName(self) -> str:
        """"""
    @property
    def MDStreamVersion(self) -> int:
        """"""
    @property
    def MetadataToken(self) -> int:
        """"""
    @property
    def ModuleHandle(self) -> ModuleHandle:
        """"""
    @property
    def ModuleVersionId(self) -> Guid:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def ScopeName(self) -> str:
        """"""
    def CreateGlobalFunctions(self) -> None:
        """"""
    def DefineDocument(
        self, url: str, language: Guid, languageVendor: Guid, documentType: Guid
    ) -> ISymbolDocumentWriter:
        """"""
    def DefineEnum(
        self, name: str, visibility: TypeAttributes, underlyingType: Type
    ) -> EnumBuilder:
        """"""
    @overload
    def DefineGlobalMethod(
        self,
        name: str,
        attributes: MethodAttributes,
        callingConvention: CallingConventions,
        returnType: Type,
        parameterTypes: Array[Type],
    ) -> MethodBuilder:
        """"""
    @overload
    def DefineGlobalMethod(
        self,
        name: str,
        attributes: MethodAttributes,
        callingConvention: CallingConventions,
        returnType: Type,
        requiredReturnTypeCustomModifiers: Array[Type],
        optionalReturnTypeCustomModifiers: Array[Type],
        parameterTypes: Array[Type],
        requiredParameterTypeCustomModifiers: Array[Array[Type]],
        optionalParameterTypeCustomModifiers: Array[Array[Type]],
    ) -> MethodBuilder:
        """"""
    @overload
    def DefineGlobalMethod(
        self, name: str, attributes: MethodAttributes, returnType: Type, parameterTypes: Array[Type]
    ) -> MethodBuilder:
        """"""
    def DefineInitializedData(
        self, name: str, data: Array[int], attributes: FieldAttributes
    ) -> FieldBuilder:
        """"""
    def DefineManifestResource(
        self, name: str, stream: Stream, attribute: ResourceAttributes
    ) -> None:
        """"""
    @overload
    def DefinePInvokeMethod(
        self,
        name: str,
        dllName: str,
        attributes: MethodAttributes,
        callingConvention: CallingConventions,
        returnType: Type,
        parameterTypes: Array[Type],
        nativeCallConv: CallingConvention,
        nativeCharSet: CharSet,
    ) -> MethodBuilder:
        """"""
    @overload
    def DefinePInvokeMethod(
        self,
        name: str,
        dllName: str,
        entryName: str,
        attributes: MethodAttributes,
        callingConvention: CallingConventions,
        returnType: Type,
        parameterTypes: Array[Type],
        nativeCallConv: CallingConvention,
        nativeCharSet: CharSet,
    ) -> MethodBuilder:
        """"""
    @overload
    def DefineResource(self, name: str, description: str) -> IResourceWriter:
        """"""
    @overload
    def DefineResource(
        self, name: str, description: str, attribute: ResourceAttributes
    ) -> IResourceWriter:
        """"""
    @overload
    def DefineType(self, name: str) -> TypeBuilder:
        """"""
    @overload
    def DefineType(self, name: str, attr: TypeAttributes) -> TypeBuilder:
        """"""
    @overload
    def DefineType(self, name: str, attr: TypeAttributes, parent: Type) -> TypeBuilder:
        """"""
    @overload
    def DefineType(
        self, name: str, attr: TypeAttributes, parent: Type, packsize: PackingSize
    ) -> TypeBuilder:
        """"""
    @overload
    def DefineType(
        self, name: str, attr: TypeAttributes, parent: Type, packingSize: PackingSize, typesize: int
    ) -> TypeBuilder:
        """"""
    @overload
    def DefineType(
        self, name: str, attr: TypeAttributes, parent: Type, interfaces: Array[Type]
    ) -> TypeBuilder:
        """"""
    @overload
    def DefineType(
        self, name: str, attr: TypeAttributes, parent: Type, typesize: int
    ) -> TypeBuilder:
        """"""
    def DefineUninitializedData(
        self, name: str, size: int, attributes: FieldAttributes
    ) -> FieldBuilder:
        """"""
    @overload
    def DefineUnmanagedResource(self, resource: Array[int]) -> None:
        """"""
    @overload
    def DefineUnmanagedResource(self, resourceFileName: str) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def FindTypes(self, filter: TypeFilter, filterCriteria: object) -> Array[Type]:
        """"""
    def GetArrayMethod(
        self,
        arrayClass: Type,
        methodName: str,
        callingConvention: CallingConventions,
        returnType: Type,
        parameterTypes: Array[Type],
    ) -> MethodInfo:
        """"""
    def GetArrayMethodToken(
        self,
        arrayClass: Type,
        methodName: str,
        callingConvention: CallingConventions,
        returnType: Type,
        parameterTypes: Array[Type],
    ) -> MethodToken:
        """"""
    @overload
    def GetConstructorToken(self, con: ConstructorInfo) -> MethodToken:
        """"""
    @overload
    def GetConstructorToken(
        self, constructor: ConstructorInfo, optionalParameterTypes: IEnumerable[Type]
    ) -> MethodToken:
        """"""
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """"""
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """"""
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]:
        """"""
    @overload
    def GetField(self, name: str) -> FieldInfo:
        """"""
    @overload
    def GetField(self, name: str, bindingAttr: BindingFlags) -> FieldInfo:
        """"""
    def GetFieldToken(self, field: FieldInfo) -> FieldToken:
        """"""
    @overload
    def GetFields(self) -> Array[FieldInfo]:
        """"""
    @overload
    def GetFields(self, bindingFlags: BindingFlags) -> Array[FieldInfo]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    @overload
    def GetMethod(self, name: str) -> MethodInfo:
        """"""
    @overload
    def GetMethod(
        self,
        name: str,
        bindingAttr: BindingFlags,
        binder: Binder,
        callConvention: CallingConventions,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> MethodInfo:
        """"""
    @overload
    def GetMethod(self, name: str, types: Array[Type]) -> MethodInfo:
        """"""
    @overload
    def GetMethodToken(self, method: MethodInfo) -> MethodToken:
        """"""
    @overload
    def GetMethodToken(
        self, method: MethodInfo, optionalParameterTypes: IEnumerable[Type]
    ) -> MethodToken:
        """"""
    @overload
    def GetMethods(self) -> Array[MethodInfo]:
        """"""
    @overload
    def GetMethods(self, bindingFlags: BindingFlags) -> Array[MethodInfo]:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetPEKind(
        self, peKind: PortableExecutableKinds, machine: ImageFileMachine
    ) -> tuple[None, PortableExecutableKinds, ImageFileMachine]:
        """"""
    @overload
    def GetSignatureToken(self, sigHelper: SignatureHelper) -> SignatureToken:
        """"""
    @overload
    def GetSignatureToken(self, sigBytes: Array[int], sigLength: int) -> SignatureToken:
        """"""
    def GetSignerCertificate(self) -> X509Certificate:
        """"""
    def GetStringConstant(self, str: str) -> StringToken:
        """"""
    def GetSymWriter(self) -> ISymbolWriter:
        """"""
    @overload
    def GetType(self) -> Type:
        """"""
    @overload
    def GetType(self, className: str) -> Type:
        """"""
    @overload
    def GetType(self, className: str, ignoreCase: bool) -> Type:
        """"""
    @overload
    def GetType(self, className: str, throwOnError: bool, ignoreCase: bool) -> Type:
        """"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """"""
    def GetTypeInfoCount(self, pcTInfo: UInt32) -> tuple[None, UInt32]:
        """"""
    @overload
    def GetTypeToken(self, name: str) -> TypeToken:
        """"""
    @overload
    def GetTypeToken(self, type: Type) -> TypeToken:
        """"""
    def GetTypes(self) -> Array[Type]:
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
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """"""
    def IsResource(self) -> bool:
        """"""
    def IsTransient(self) -> bool:
        """"""
    @overload
    def ResolveField(self, metadataToken: int) -> FieldInfo:
        """"""
    @overload
    def ResolveField(
        self,
        metadataToken: int,
        genericTypeArguments: Array[Type],
        genericMethodArguments: Array[Type],
    ) -> FieldInfo:
        """"""
    @overload
    def ResolveMember(self, metadataToken: int) -> MemberInfo:
        """"""
    @overload
    def ResolveMember(
        self,
        metadataToken: int,
        genericTypeArguments: Array[Type],
        genericMethodArguments: Array[Type],
    ) -> MemberInfo:
        """"""
    @overload
    def ResolveMethod(self, metadataToken: int) -> MethodBase:
        """"""
    @overload
    def ResolveMethod(
        self,
        metadataToken: int,
        genericTypeArguments: Array[Type],
        genericMethodArguments: Array[Type],
    ) -> MethodBase:
        """"""
    def ResolveSignature(self, metadataToken: int) -> Array[int]:
        """"""
    def ResolveString(self, metadataToken: int) -> str:
        """"""
    @overload
    def ResolveType(self, metadataToken: int) -> Type:
        """"""
    @overload
    def ResolveType(
        self,
        metadataToken: int,
        genericTypeArguments: Array[Type],
        genericMethodArguments: Array[Type],
    ) -> Type:
        """"""
    @overload
    def SetCustomAttribute(self, customBuilder: CustomAttributeBuilder) -> None:
        """"""
    @overload
    def SetCustomAttribute(self, con: ConstructorInfo, binaryAttribute: Array[int]) -> None:
        """"""
    def SetSymCustomAttribute(self, name: str, data: Array[int]) -> None:
        """"""
    def SetUserEntryPoint(self, entryPoint: MethodInfo) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class ModuleBuilderData(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class NativeVersionInfo(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class OpCode(ValueType):
    """"""
    @property
    def FlowControl(self) -> FlowControl:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def OpCodeType(self) -> OpCodeType:
        """"""
    @property
    def OperandType(self) -> OperandType:
        """"""
    @property
    def Size(self) -> int:
        """"""
    @property
    def StackBehaviourPop(self) -> StackBehaviour:
        """"""
    @property
    def StackBehaviourPush(self) -> StackBehaviour:
        """"""
    @property
    def Value(self) -> int:
        """"""
    @overload
    def Equals(self, obj: OpCode) -> bool:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def op_Equality(cls, a: OpCode, b: OpCode) -> bool:
        """"""
    @classmethod
    def op_Inequality(cls, a: OpCode, b: OpCode) -> bool:
        """"""
    def __eq__(self, other: OpCode) -> bool:
        """"""
    def __ne__(self, other: OpCode) -> bool:
        """"""

class OpCodeType(Enum):
    """"""

    Annotation: OpCodeType = ...
    """"""
    Macro: OpCodeType = ...
    """"""
    Nternal: OpCodeType = ...
    """"""
    Objmodel: OpCodeType = ...
    """"""
    Prefix: OpCodeType = ...
    """"""
    Primitive: OpCodeType = ...
    """"""

class OpCodeValues(Enum):
    """"""

    Nop: OpCodeValues = ...
    """"""
    Break: OpCodeValues = ...
    """"""
    Ldarg_0: OpCodeValues = ...
    """"""
    Ldarg_1: OpCodeValues = ...
    """"""
    Ldarg_2: OpCodeValues = ...
    """"""
    Ldarg_3: OpCodeValues = ...
    """"""
    Ldloc_0: OpCodeValues = ...
    """"""
    Ldloc_1: OpCodeValues = ...
    """"""
    Ldloc_2: OpCodeValues = ...
    """"""
    Ldloc_3: OpCodeValues = ...
    """"""
    Stloc_0: OpCodeValues = ...
    """"""
    Stloc_1: OpCodeValues = ...
    """"""
    Stloc_2: OpCodeValues = ...
    """"""
    Stloc_3: OpCodeValues = ...
    """"""
    Ldarg_S: OpCodeValues = ...
    """"""
    Ldarga_S: OpCodeValues = ...
    """"""
    Starg_S: OpCodeValues = ...
    """"""
    Ldloc_S: OpCodeValues = ...
    """"""
    Ldloca_S: OpCodeValues = ...
    """"""
    Stloc_S: OpCodeValues = ...
    """"""
    Ldnull: OpCodeValues = ...
    """"""
    Ldc_I4_M1: OpCodeValues = ...
    """"""
    Ldc_I4_0: OpCodeValues = ...
    """"""
    Ldc_I4_1: OpCodeValues = ...
    """"""
    Ldc_I4_2: OpCodeValues = ...
    """"""
    Ldc_I4_3: OpCodeValues = ...
    """"""
    Ldc_I4_4: OpCodeValues = ...
    """"""
    Ldc_I4_5: OpCodeValues = ...
    """"""
    Ldc_I4_6: OpCodeValues = ...
    """"""
    Ldc_I4_7: OpCodeValues = ...
    """"""
    Ldc_I4_8: OpCodeValues = ...
    """"""
    Ldc_I4_S: OpCodeValues = ...
    """"""
    Ldc_I4: OpCodeValues = ...
    """"""
    Ldc_I8: OpCodeValues = ...
    """"""
    Ldc_R4: OpCodeValues = ...
    """"""
    Ldc_R8: OpCodeValues = ...
    """"""
    Dup: OpCodeValues = ...
    """"""
    Pop: OpCodeValues = ...
    """"""
    Jmp: OpCodeValues = ...
    """"""
    Call: OpCodeValues = ...
    """"""
    Calli: OpCodeValues = ...
    """"""
    Ret: OpCodeValues = ...
    """"""
    Br_S: OpCodeValues = ...
    """"""
    Brfalse_S: OpCodeValues = ...
    """"""
    Brtrue_S: OpCodeValues = ...
    """"""
    Beq_S: OpCodeValues = ...
    """"""
    Bge_S: OpCodeValues = ...
    """"""
    Bgt_S: OpCodeValues = ...
    """"""
    Ble_S: OpCodeValues = ...
    """"""
    Blt_S: OpCodeValues = ...
    """"""
    Bne_Un_S: OpCodeValues = ...
    """"""
    Bge_Un_S: OpCodeValues = ...
    """"""
    Bgt_Un_S: OpCodeValues = ...
    """"""
    Ble_Un_S: OpCodeValues = ...
    """"""
    Blt_Un_S: OpCodeValues = ...
    """"""
    Br: OpCodeValues = ...
    """"""
    Brfalse: OpCodeValues = ...
    """"""
    Brtrue: OpCodeValues = ...
    """"""
    Beq: OpCodeValues = ...
    """"""
    Bge: OpCodeValues = ...
    """"""
    Bgt: OpCodeValues = ...
    """"""
    Ble: OpCodeValues = ...
    """"""
    Blt: OpCodeValues = ...
    """"""
    Bne_Un: OpCodeValues = ...
    """"""
    Bge_Un: OpCodeValues = ...
    """"""
    Bgt_Un: OpCodeValues = ...
    """"""
    Ble_Un: OpCodeValues = ...
    """"""
    Blt_Un: OpCodeValues = ...
    """"""
    Switch: OpCodeValues = ...
    """"""
    Ldind_I1: OpCodeValues = ...
    """"""
    Ldind_U1: OpCodeValues = ...
    """"""
    Ldind_I2: OpCodeValues = ...
    """"""
    Ldind_U2: OpCodeValues = ...
    """"""
    Ldind_I4: OpCodeValues = ...
    """"""
    Ldind_U4: OpCodeValues = ...
    """"""
    Ldind_I8: OpCodeValues = ...
    """"""
    Ldind_I: OpCodeValues = ...
    """"""
    Ldind_R4: OpCodeValues = ...
    """"""
    Ldind_R8: OpCodeValues = ...
    """"""
    Ldind_Ref: OpCodeValues = ...
    """"""
    Stind_Ref: OpCodeValues = ...
    """"""
    Stind_I1: OpCodeValues = ...
    """"""
    Stind_I2: OpCodeValues = ...
    """"""
    Stind_I4: OpCodeValues = ...
    """"""
    Stind_I8: OpCodeValues = ...
    """"""
    Stind_R4: OpCodeValues = ...
    """"""
    Stind_R8: OpCodeValues = ...
    """"""
    Add: OpCodeValues = ...
    """"""
    Sub: OpCodeValues = ...
    """"""
    Mul: OpCodeValues = ...
    """"""
    Div: OpCodeValues = ...
    """"""
    Div_Un: OpCodeValues = ...
    """"""
    Rem: OpCodeValues = ...
    """"""
    Rem_Un: OpCodeValues = ...
    """"""
    And: OpCodeValues = ...
    """"""
    Or: OpCodeValues = ...
    """"""
    Xor: OpCodeValues = ...
    """"""
    Shl: OpCodeValues = ...
    """"""
    Shr: OpCodeValues = ...
    """"""
    Shr_Un: OpCodeValues = ...
    """"""
    Neg: OpCodeValues = ...
    """"""
    Not: OpCodeValues = ...
    """"""
    Conv_I1: OpCodeValues = ...
    """"""
    Conv_I2: OpCodeValues = ...
    """"""
    Conv_I4: OpCodeValues = ...
    """"""
    Conv_I8: OpCodeValues = ...
    """"""
    Conv_R4: OpCodeValues = ...
    """"""
    Conv_R8: OpCodeValues = ...
    """"""
    Conv_U4: OpCodeValues = ...
    """"""
    Conv_U8: OpCodeValues = ...
    """"""
    Callvirt: OpCodeValues = ...
    """"""
    Cpobj: OpCodeValues = ...
    """"""
    Ldobj: OpCodeValues = ...
    """"""
    Ldstr: OpCodeValues = ...
    """"""
    Newobj: OpCodeValues = ...
    """"""
    Castclass: OpCodeValues = ...
    """"""
    Isinst: OpCodeValues = ...
    """"""
    Conv_R_Un: OpCodeValues = ...
    """"""
    Unbox: OpCodeValues = ...
    """"""
    Throw: OpCodeValues = ...
    """"""
    Ldfld: OpCodeValues = ...
    """"""
    Ldflda: OpCodeValues = ...
    """"""
    Stfld: OpCodeValues = ...
    """"""
    Ldsfld: OpCodeValues = ...
    """"""
    Ldsflda: OpCodeValues = ...
    """"""
    Stsfld: OpCodeValues = ...
    """"""
    Stobj: OpCodeValues = ...
    """"""
    Conv_Ovf_I1_Un: OpCodeValues = ...
    """"""
    Conv_Ovf_I2_Un: OpCodeValues = ...
    """"""
    Conv_Ovf_I4_Un: OpCodeValues = ...
    """"""
    Conv_Ovf_I8_Un: OpCodeValues = ...
    """"""
    Conv_Ovf_U1_Un: OpCodeValues = ...
    """"""
    Conv_Ovf_U2_Un: OpCodeValues = ...
    """"""
    Conv_Ovf_U4_Un: OpCodeValues = ...
    """"""
    Conv_Ovf_U8_Un: OpCodeValues = ...
    """"""
    Conv_Ovf_I_Un: OpCodeValues = ...
    """"""
    Conv_Ovf_U_Un: OpCodeValues = ...
    """"""
    Box: OpCodeValues = ...
    """"""
    Newarr: OpCodeValues = ...
    """"""
    Ldlen: OpCodeValues = ...
    """"""
    Ldelema: OpCodeValues = ...
    """"""
    Ldelem_I1: OpCodeValues = ...
    """"""
    Ldelem_U1: OpCodeValues = ...
    """"""
    Ldelem_I2: OpCodeValues = ...
    """"""
    Ldelem_U2: OpCodeValues = ...
    """"""
    Ldelem_I4: OpCodeValues = ...
    """"""
    Ldelem_U4: OpCodeValues = ...
    """"""
    Ldelem_I8: OpCodeValues = ...
    """"""
    Ldelem_I: OpCodeValues = ...
    """"""
    Ldelem_R4: OpCodeValues = ...
    """"""
    Ldelem_R8: OpCodeValues = ...
    """"""
    Ldelem_Ref: OpCodeValues = ...
    """"""
    Stelem_I: OpCodeValues = ...
    """"""
    Stelem_I1: OpCodeValues = ...
    """"""
    Stelem_I2: OpCodeValues = ...
    """"""
    Stelem_I4: OpCodeValues = ...
    """"""
    Stelem_I8: OpCodeValues = ...
    """"""
    Stelem_R4: OpCodeValues = ...
    """"""
    Stelem_R8: OpCodeValues = ...
    """"""
    Stelem_Ref: OpCodeValues = ...
    """"""
    Ldelem: OpCodeValues = ...
    """"""
    Stelem: OpCodeValues = ...
    """"""
    Unbox_Any: OpCodeValues = ...
    """"""
    Conv_Ovf_I1: OpCodeValues = ...
    """"""
    Conv_Ovf_U1: OpCodeValues = ...
    """"""
    Conv_Ovf_I2: OpCodeValues = ...
    """"""
    Conv_Ovf_U2: OpCodeValues = ...
    """"""
    Conv_Ovf_I4: OpCodeValues = ...
    """"""
    Conv_Ovf_U4: OpCodeValues = ...
    """"""
    Conv_Ovf_I8: OpCodeValues = ...
    """"""
    Conv_Ovf_U8: OpCodeValues = ...
    """"""
    Refanyval: OpCodeValues = ...
    """"""
    Ckfinite: OpCodeValues = ...
    """"""
    Mkrefany: OpCodeValues = ...
    """"""
    Ldtoken: OpCodeValues = ...
    """"""
    Conv_U2: OpCodeValues = ...
    """"""
    Conv_U1: OpCodeValues = ...
    """"""
    Conv_I: OpCodeValues = ...
    """"""
    Conv_Ovf_I: OpCodeValues = ...
    """"""
    Conv_Ovf_U: OpCodeValues = ...
    """"""
    Add_Ovf: OpCodeValues = ...
    """"""
    Add_Ovf_Un: OpCodeValues = ...
    """"""
    Mul_Ovf: OpCodeValues = ...
    """"""
    Mul_Ovf_Un: OpCodeValues = ...
    """"""
    Sub_Ovf: OpCodeValues = ...
    """"""
    Sub_Ovf_Un: OpCodeValues = ...
    """"""
    Endfinally: OpCodeValues = ...
    """"""
    Leave: OpCodeValues = ...
    """"""
    Leave_S: OpCodeValues = ...
    """"""
    Stind_I: OpCodeValues = ...
    """"""
    Conv_U: OpCodeValues = ...
    """"""
    Prefix7: OpCodeValues = ...
    """"""
    Prefix6: OpCodeValues = ...
    """"""
    Prefix5: OpCodeValues = ...
    """"""
    Prefix4: OpCodeValues = ...
    """"""
    Prefix3: OpCodeValues = ...
    """"""
    Prefix2: OpCodeValues = ...
    """"""
    Prefix1: OpCodeValues = ...
    """"""
    Prefixref: OpCodeValues = ...
    """"""
    Arglist: OpCodeValues = ...
    """"""
    Ceq: OpCodeValues = ...
    """"""
    Cgt: OpCodeValues = ...
    """"""
    Cgt_Un: OpCodeValues = ...
    """"""
    Clt: OpCodeValues = ...
    """"""
    Clt_Un: OpCodeValues = ...
    """"""
    Ldftn: OpCodeValues = ...
    """"""
    Ldvirtftn: OpCodeValues = ...
    """"""
    Ldarg: OpCodeValues = ...
    """"""
    Ldarga: OpCodeValues = ...
    """"""
    Starg: OpCodeValues = ...
    """"""
    Ldloc: OpCodeValues = ...
    """"""
    Ldloca: OpCodeValues = ...
    """"""
    Stloc: OpCodeValues = ...
    """"""
    Localloc: OpCodeValues = ...
    """"""
    Endfilter: OpCodeValues = ...
    """"""
    Unaligned_: OpCodeValues = ...
    """"""
    Volatile_: OpCodeValues = ...
    """"""
    Tail_: OpCodeValues = ...
    """"""
    Initobj: OpCodeValues = ...
    """"""
    Constrained_: OpCodeValues = ...
    """"""
    Cpblk: OpCodeValues = ...
    """"""
    Initblk: OpCodeValues = ...
    """"""
    Rethrow: OpCodeValues = ...
    """"""
    Sizeof: OpCodeValues = ...
    """"""
    Refanytype: OpCodeValues = ...
    """"""
    Readonly_: OpCodeValues = ...
    """"""

class OpCodes(Object):
    """"""

    Add: ClassVar[OpCode]
    """"""
    Add_Ovf: ClassVar[OpCode]
    """"""
    Add_Ovf_Un: ClassVar[OpCode]
    """"""
    And: ClassVar[OpCode]
    """"""
    Arglist: ClassVar[OpCode]
    """"""
    Beq: ClassVar[OpCode]
    """"""
    Beq_S: ClassVar[OpCode]
    """"""
    Bge: ClassVar[OpCode]
    """"""
    Bge_S: ClassVar[OpCode]
    """"""
    Bge_Un: ClassVar[OpCode]
    """"""
    Bge_Un_S: ClassVar[OpCode]
    """"""
    Bgt: ClassVar[OpCode]
    """"""
    Bgt_S: ClassVar[OpCode]
    """"""
    Bgt_Un: ClassVar[OpCode]
    """"""
    Bgt_Un_S: ClassVar[OpCode]
    """"""
    Ble: ClassVar[OpCode]
    """"""
    Ble_S: ClassVar[OpCode]
    """"""
    Ble_Un: ClassVar[OpCode]
    """"""
    Ble_Un_S: ClassVar[OpCode]
    """"""
    Blt: ClassVar[OpCode]
    """"""
    Blt_S: ClassVar[OpCode]
    """"""
    Blt_Un: ClassVar[OpCode]
    """"""
    Blt_Un_S: ClassVar[OpCode]
    """"""
    Bne_Un: ClassVar[OpCode]
    """"""
    Bne_Un_S: ClassVar[OpCode]
    """"""
    Box: ClassVar[OpCode]
    """"""
    Br: ClassVar[OpCode]
    """"""
    Br_S: ClassVar[OpCode]
    """"""
    Break: ClassVar[OpCode]
    """"""
    Brfalse: ClassVar[OpCode]
    """"""
    Brfalse_S: ClassVar[OpCode]
    """"""
    Brtrue: ClassVar[OpCode]
    """"""
    Brtrue_S: ClassVar[OpCode]
    """"""
    Call: ClassVar[OpCode]
    """"""
    Calli: ClassVar[OpCode]
    """"""
    Callvirt: ClassVar[OpCode]
    """"""
    Castclass: ClassVar[OpCode]
    """"""
    Ceq: ClassVar[OpCode]
    """"""
    Cgt: ClassVar[OpCode]
    """"""
    Cgt_Un: ClassVar[OpCode]
    """"""
    Ckfinite: ClassVar[OpCode]
    """"""
    Clt: ClassVar[OpCode]
    """"""
    Clt_Un: ClassVar[OpCode]
    """"""
    Constrained: ClassVar[OpCode]
    """"""
    Conv_I: ClassVar[OpCode]
    """"""
    Conv_I1: ClassVar[OpCode]
    """"""
    Conv_I2: ClassVar[OpCode]
    """"""
    Conv_I4: ClassVar[OpCode]
    """"""
    Conv_I8: ClassVar[OpCode]
    """"""
    Conv_Ovf_I: ClassVar[OpCode]
    """"""
    Conv_Ovf_I1: ClassVar[OpCode]
    """"""
    Conv_Ovf_I1_Un: ClassVar[OpCode]
    """"""
    Conv_Ovf_I2: ClassVar[OpCode]
    """"""
    Conv_Ovf_I2_Un: ClassVar[OpCode]
    """"""
    Conv_Ovf_I4: ClassVar[OpCode]
    """"""
    Conv_Ovf_I4_Un: ClassVar[OpCode]
    """"""
    Conv_Ovf_I8: ClassVar[OpCode]
    """"""
    Conv_Ovf_I8_Un: ClassVar[OpCode]
    """"""
    Conv_Ovf_I_Un: ClassVar[OpCode]
    """"""
    Conv_Ovf_U: ClassVar[OpCode]
    """"""
    Conv_Ovf_U1: ClassVar[OpCode]
    """"""
    Conv_Ovf_U1_Un: ClassVar[OpCode]
    """"""
    Conv_Ovf_U2: ClassVar[OpCode]
    """"""
    Conv_Ovf_U2_Un: ClassVar[OpCode]
    """"""
    Conv_Ovf_U4: ClassVar[OpCode]
    """"""
    Conv_Ovf_U4_Un: ClassVar[OpCode]
    """"""
    Conv_Ovf_U8: ClassVar[OpCode]
    """"""
    Conv_Ovf_U8_Un: ClassVar[OpCode]
    """"""
    Conv_Ovf_U_Un: ClassVar[OpCode]
    """"""
    Conv_R4: ClassVar[OpCode]
    """"""
    Conv_R8: ClassVar[OpCode]
    """"""
    Conv_R_Un: ClassVar[OpCode]
    """"""
    Conv_U: ClassVar[OpCode]
    """"""
    Conv_U1: ClassVar[OpCode]
    """"""
    Conv_U2: ClassVar[OpCode]
    """"""
    Conv_U4: ClassVar[OpCode]
    """"""
    Conv_U8: ClassVar[OpCode]
    """"""
    Cpblk: ClassVar[OpCode]
    """"""
    Cpobj: ClassVar[OpCode]
    """"""
    Div: ClassVar[OpCode]
    """"""
    Div_Un: ClassVar[OpCode]
    """"""
    Dup: ClassVar[OpCode]
    """"""
    Endfilter: ClassVar[OpCode]
    """"""
    Endfinally: ClassVar[OpCode]
    """"""
    Initblk: ClassVar[OpCode]
    """"""
    Initobj: ClassVar[OpCode]
    """"""
    Isinst: ClassVar[OpCode]
    """"""
    Jmp: ClassVar[OpCode]
    """"""
    Ldarg: ClassVar[OpCode]
    """"""
    Ldarg_0: ClassVar[OpCode]
    """"""
    Ldarg_1: ClassVar[OpCode]
    """"""
    Ldarg_2: ClassVar[OpCode]
    """"""
    Ldarg_3: ClassVar[OpCode]
    """"""
    Ldarg_S: ClassVar[OpCode]
    """"""
    Ldarga: ClassVar[OpCode]
    """"""
    Ldarga_S: ClassVar[OpCode]
    """"""
    Ldc_I4: ClassVar[OpCode]
    """"""
    Ldc_I4_0: ClassVar[OpCode]
    """"""
    Ldc_I4_1: ClassVar[OpCode]
    """"""
    Ldc_I4_2: ClassVar[OpCode]
    """"""
    Ldc_I4_3: ClassVar[OpCode]
    """"""
    Ldc_I4_4: ClassVar[OpCode]
    """"""
    Ldc_I4_5: ClassVar[OpCode]
    """"""
    Ldc_I4_6: ClassVar[OpCode]
    """"""
    Ldc_I4_7: ClassVar[OpCode]
    """"""
    Ldc_I4_8: ClassVar[OpCode]
    """"""
    Ldc_I4_M1: ClassVar[OpCode]
    """"""
    Ldc_I4_S: ClassVar[OpCode]
    """"""
    Ldc_I8: ClassVar[OpCode]
    """"""
    Ldc_R4: ClassVar[OpCode]
    """"""
    Ldc_R8: ClassVar[OpCode]
    """"""
    Ldelem: ClassVar[OpCode]
    """"""
    Ldelem_I: ClassVar[OpCode]
    """"""
    Ldelem_I1: ClassVar[OpCode]
    """"""
    Ldelem_I2: ClassVar[OpCode]
    """"""
    Ldelem_I4: ClassVar[OpCode]
    """"""
    Ldelem_I8: ClassVar[OpCode]
    """"""
    Ldelem_R4: ClassVar[OpCode]
    """"""
    Ldelem_R8: ClassVar[OpCode]
    """"""
    Ldelem_Ref: ClassVar[OpCode]
    """"""
    Ldelem_U1: ClassVar[OpCode]
    """"""
    Ldelem_U2: ClassVar[OpCode]
    """"""
    Ldelem_U4: ClassVar[OpCode]
    """"""
    Ldelema: ClassVar[OpCode]
    """"""
    Ldfld: ClassVar[OpCode]
    """"""
    Ldflda: ClassVar[OpCode]
    """"""
    Ldftn: ClassVar[OpCode]
    """"""
    Ldind_I: ClassVar[OpCode]
    """"""
    Ldind_I1: ClassVar[OpCode]
    """"""
    Ldind_I2: ClassVar[OpCode]
    """"""
    Ldind_I4: ClassVar[OpCode]
    """"""
    Ldind_I8: ClassVar[OpCode]
    """"""
    Ldind_R4: ClassVar[OpCode]
    """"""
    Ldind_R8: ClassVar[OpCode]
    """"""
    Ldind_Ref: ClassVar[OpCode]
    """"""
    Ldind_U1: ClassVar[OpCode]
    """"""
    Ldind_U2: ClassVar[OpCode]
    """"""
    Ldind_U4: ClassVar[OpCode]
    """"""
    Ldlen: ClassVar[OpCode]
    """"""
    Ldloc: ClassVar[OpCode]
    """"""
    Ldloc_0: ClassVar[OpCode]
    """"""
    Ldloc_1: ClassVar[OpCode]
    """"""
    Ldloc_2: ClassVar[OpCode]
    """"""
    Ldloc_3: ClassVar[OpCode]
    """"""
    Ldloc_S: ClassVar[OpCode]
    """"""
    Ldloca: ClassVar[OpCode]
    """"""
    Ldloca_S: ClassVar[OpCode]
    """"""
    Ldnull: ClassVar[OpCode]
    """"""
    Ldobj: ClassVar[OpCode]
    """"""
    Ldsfld: ClassVar[OpCode]
    """"""
    Ldsflda: ClassVar[OpCode]
    """"""
    Ldstr: ClassVar[OpCode]
    """"""
    Ldtoken: ClassVar[OpCode]
    """"""
    Ldvirtftn: ClassVar[OpCode]
    """"""
    Leave: ClassVar[OpCode]
    """"""
    Leave_S: ClassVar[OpCode]
    """"""
    Localloc: ClassVar[OpCode]
    """"""
    Mkrefany: ClassVar[OpCode]
    """"""
    Mul: ClassVar[OpCode]
    """"""
    Mul_Ovf: ClassVar[OpCode]
    """"""
    Mul_Ovf_Un: ClassVar[OpCode]
    """"""
    Neg: ClassVar[OpCode]
    """"""
    Newarr: ClassVar[OpCode]
    """"""
    Newobj: ClassVar[OpCode]
    """"""
    Nop: ClassVar[OpCode]
    """"""
    Not: ClassVar[OpCode]
    """"""
    Or: ClassVar[OpCode]
    """"""
    Pop: ClassVar[OpCode]
    """"""
    Prefix1: ClassVar[OpCode]
    """"""
    Prefix2: ClassVar[OpCode]
    """"""
    Prefix3: ClassVar[OpCode]
    """"""
    Prefix4: ClassVar[OpCode]
    """"""
    Prefix5: ClassVar[OpCode]
    """"""
    Prefix6: ClassVar[OpCode]
    """"""
    Prefix7: ClassVar[OpCode]
    """"""
    Prefixref: ClassVar[OpCode]
    """"""
    Readonly: ClassVar[OpCode]
    """"""
    Refanytype: ClassVar[OpCode]
    """"""
    Refanyval: ClassVar[OpCode]
    """"""
    Rem: ClassVar[OpCode]
    """"""
    Rem_Un: ClassVar[OpCode]
    """"""
    Ret: ClassVar[OpCode]
    """"""
    Rethrow: ClassVar[OpCode]
    """"""
    Shl: ClassVar[OpCode]
    """"""
    Shr: ClassVar[OpCode]
    """"""
    Shr_Un: ClassVar[OpCode]
    """"""
    Sizeof: ClassVar[OpCode]
    """"""
    Starg: ClassVar[OpCode]
    """"""
    Starg_S: ClassVar[OpCode]
    """"""
    Stelem: ClassVar[OpCode]
    """"""
    Stelem_I: ClassVar[OpCode]
    """"""
    Stelem_I1: ClassVar[OpCode]
    """"""
    Stelem_I2: ClassVar[OpCode]
    """"""
    Stelem_I4: ClassVar[OpCode]
    """"""
    Stelem_I8: ClassVar[OpCode]
    """"""
    Stelem_R4: ClassVar[OpCode]
    """"""
    Stelem_R8: ClassVar[OpCode]
    """"""
    Stelem_Ref: ClassVar[OpCode]
    """"""
    Stfld: ClassVar[OpCode]
    """"""
    Stind_I: ClassVar[OpCode]
    """"""
    Stind_I1: ClassVar[OpCode]
    """"""
    Stind_I2: ClassVar[OpCode]
    """"""
    Stind_I4: ClassVar[OpCode]
    """"""
    Stind_I8: ClassVar[OpCode]
    """"""
    Stind_R4: ClassVar[OpCode]
    """"""
    Stind_R8: ClassVar[OpCode]
    """"""
    Stind_Ref: ClassVar[OpCode]
    """"""
    Stloc: ClassVar[OpCode]
    """"""
    Stloc_0: ClassVar[OpCode]
    """"""
    Stloc_1: ClassVar[OpCode]
    """"""
    Stloc_2: ClassVar[OpCode]
    """"""
    Stloc_3: ClassVar[OpCode]
    """"""
    Stloc_S: ClassVar[OpCode]
    """"""
    Stobj: ClassVar[OpCode]
    """"""
    Stsfld: ClassVar[OpCode]
    """"""
    Sub: ClassVar[OpCode]
    """"""
    Sub_Ovf: ClassVar[OpCode]
    """"""
    Sub_Ovf_Un: ClassVar[OpCode]
    """"""
    Switch: ClassVar[OpCode]
    """"""
    Tailcall: ClassVar[OpCode]
    """"""
    Throw: ClassVar[OpCode]
    """"""
    Unaligned: ClassVar[OpCode]
    """"""
    Unbox: ClassVar[OpCode]
    """"""
    Unbox_Any: ClassVar[OpCode]
    """"""
    Volatile: ClassVar[OpCode]
    """"""
    Xor: ClassVar[OpCode]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def TakesSingleByteArgument(cls, inst: OpCode) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

class OperandType(Enum):
    """"""

    InlineBrTarget: OperandType = ...
    """"""
    InlineField: OperandType = ...
    """"""
    InlineI: OperandType = ...
    """"""
    InlineI8: OperandType = ...
    """"""
    InlineMethod: OperandType = ...
    """"""
    InlineNone: OperandType = ...
    """"""
    InlinePhi: OperandType = ...
    """"""
    InlineR: OperandType = ...
    """"""
    InlineSig: OperandType = ...
    """"""
    InlineString: OperandType = ...
    """"""
    InlineSwitch: OperandType = ...
    """"""
    InlineTok: OperandType = ...
    """"""
    InlineType: OperandType = ...
    """"""
    InlineVar: OperandType = ...
    """"""
    ShortInlineBrTarget: OperandType = ...
    """"""
    ShortInlineI: OperandType = ...
    """"""
    ShortInlineR: OperandType = ...
    """"""
    ShortInlineVar: OperandType = ...
    """"""

class PEFileKinds(Enum):
    """"""

    Dll: PEFileKinds = ...
    """"""
    ConsoleApplication: PEFileKinds = ...
    """"""
    WindowApplication: PEFileKinds = ...
    """"""

class PackingSize(Enum):
    """"""

    Unspecified: PackingSize = ...
    """"""
    Size1: PackingSize = ...
    """"""
    Size2: PackingSize = ...
    """"""
    Size4: PackingSize = ...
    """"""
    Size8: PackingSize = ...
    """"""
    Size16: PackingSize = ...
    """"""
    Size32: PackingSize = ...
    """"""
    Size64: PackingSize = ...
    """"""
    Size128: PackingSize = ...
    """"""

class ParameterBuilder(Object, _ParameterBuilder):
    """"""
    @property
    def Attributes(self) -> int:
        """"""
    @property
    def IsIn(self) -> bool:
        """"""
    @property
    def IsOptional(self) -> bool:
        """"""
    @property
    def IsOut(self) -> bool:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def Position(self) -> int:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    def GetToken(self) -> ParameterToken:
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
    def SetConstant(self, defaultValue: object) -> None:
        """"""
    @overload
    def SetCustomAttribute(self, customBuilder: CustomAttributeBuilder) -> None:
        """"""
    @overload
    def SetCustomAttribute(self, con: ConstructorInfo, binaryAttribute: Array[int]) -> None:
        """"""
    def SetMarshal(self, unmanagedMarshal: UnmanagedMarshal) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class ParameterToken(ValueType):
    """"""

    Empty: ClassVar[ParameterToken]
    """"""
    @property
    def Token(self) -> int:
        """"""
    @overload
    def Equals(self, obj: ParameterToken) -> bool:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def op_Equality(cls, a: ParameterToken, b: ParameterToken) -> bool:
        """"""
    @classmethod
    def op_Inequality(cls, a: ParameterToken, b: ParameterToken) -> bool:
        """"""
    def __eq__(self, other: ParameterToken) -> bool:
        """"""
    def __ne__(self, other: ParameterToken) -> bool:
        """"""

class PropertyBuilder(
    PropertyInfo, ICustomAttributeProvider, _MemberInfo, _PropertyBuilder, _PropertyInfo
):
    """"""
    @property
    def Attributes(self) -> PropertyAttributes:
        """"""
    @property
    def CanRead(self) -> bool:
        """"""
    @property
    def CanWrite(self) -> bool:
        """"""
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
        """"""
    @property
    def DeclaringType(self) -> Type:
        """"""
    @property
    def GetMethod(self) -> MethodInfo:
        """"""
    @property
    def IsSpecialName(self) -> bool:
        """"""
    @property
    def MemberType(self) -> MemberTypes:
        """"""
    @property
    def MetadataToken(self) -> int:
        """"""
    @property
    def Module(self) -> Module:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def PropertyToken(self) -> PropertyToken:
        """"""
    @property
    def PropertyType(self) -> Type:
        """"""
    @property
    def ReflectedType(self) -> Type:
        """"""
    @property
    def SetMethod(self) -> MethodInfo:
        """"""
    def AddOtherMethod(self, mdBuilder: MethodBuilder) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetAccessors(self) -> Array[MethodInfo]:
        """"""
    @overload
    def GetAccessors(self, nonPublic: bool) -> Array[MethodInfo]:
        """"""
    def GetConstantValue(self) -> object:
        """"""
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """"""
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """"""
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]:
        """"""
    @overload
    def GetGetMethod(self) -> MethodInfo:
        """"""
    @overload
    def GetGetMethod(self, nonPublic: bool) -> MethodInfo:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    def GetIndexParameters(self) -> Array[ParameterInfo]:
        """"""
    def GetOptionalCustomModifiers(self) -> Array[Type]:
        """"""
    def GetRawConstantValue(self) -> object:
        """"""
    def GetRequiredCustomModifiers(self) -> Array[Type]:
        """"""
    @overload
    def GetSetMethod(self) -> MethodInfo:
        """"""
    @overload
    def GetSetMethod(self, nonPublic: bool) -> MethodInfo:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """"""
    def GetTypeInfoCount(self, pcTInfo: UInt32) -> tuple[None, UInt32]:
        """"""
    @overload
    def GetValue(self, obj: object) -> object:
        """"""
    @overload
    def GetValue(
        self,
        obj: object,
        invokeAttr: BindingFlags,
        binder: Binder,
        index: Array[object],
        culture: CultureInfo,
    ) -> object:
        """"""
    @overload
    def GetValue(self, obj: object, index: Array[object]) -> object:
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
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """"""
    def SetConstant(self, defaultValue: object) -> None:
        """"""
    @overload
    def SetCustomAttribute(self, customBuilder: CustomAttributeBuilder) -> None:
        """"""
    @overload
    def SetCustomAttribute(self, con: ConstructorInfo, binaryAttribute: Array[int]) -> None:
        """"""
    def SetGetMethod(self, mdBuilder: MethodBuilder) -> None:
        """"""
    def SetSetMethod(self, mdBuilder: MethodBuilder) -> None:
        """"""
    @overload
    def SetValue(self, obj: object, value: object) -> None:
        """"""
    @overload
    def SetValue(
        self,
        obj: object,
        value: object,
        invokeAttr: BindingFlags,
        binder: Binder,
        index: Array[object],
        culture: CultureInfo,
    ) -> None:
        """"""
    @overload
    def SetValue(self, obj: object, value: object, index: Array[object]) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class PropertyToken(ValueType):
    """"""

    Empty: ClassVar[PropertyToken]
    """"""
    @property
    def Token(self) -> int:
        """"""
    @overload
    def Equals(self, obj: PropertyToken) -> bool:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def op_Equality(cls, a: PropertyToken, b: PropertyToken) -> bool:
        """"""
    @classmethod
    def op_Inequality(cls, a: PropertyToken, b: PropertyToken) -> bool:
        """"""
    def __eq__(self, other: PropertyToken) -> bool:
        """"""
    def __ne__(self, other: PropertyToken) -> bool:
        """"""

class REDocument(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ResWriterData(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ScopeAction(Enum):
    """"""

    Open: ScopeAction = ...
    """"""
    Close: ScopeAction = ...
    """"""

class ScopeTree(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SignatureHelper(Object, _SignatureHelper):
    """"""
    @overload
    def AddArgument(self, clsArgument: Type) -> None:
        """"""
    @overload
    def AddArgument(
        self,
        argument: Type,
        requiredCustomModifiers: Array[Type],
        optionalCustomModifiers: Array[Type],
    ) -> None:
        """"""
    @overload
    def AddArgument(self, argument: Type, pinned: bool) -> None:
        """"""
    def AddArguments(
        self,
        arguments: Array[Type],
        requiredCustomModifiers: Array[Array[Type]],
        optionalCustomModifiers: Array[Array[Type]],
    ) -> None:
        """"""
    def AddSentinel(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def GetFieldSigHelper(cls, mod: Module) -> SignatureHelper:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    @classmethod
    @overload
    def GetLocalVarSigHelper(cls) -> SignatureHelper:
        """"""
    @classmethod
    @overload
    def GetLocalVarSigHelper(cls, mod: Module) -> SignatureHelper:
        """"""
    @classmethod
    @overload
    def GetMethodSigHelper(
        cls, callingConvention: CallingConventions, returnType: Type
    ) -> SignatureHelper:
        """"""
    @classmethod
    @overload
    def GetMethodSigHelper(
        cls, mod: Module, callingConvention: CallingConventions, returnType: Type
    ) -> SignatureHelper:
        """"""
    @classmethod
    @overload
    def GetMethodSigHelper(
        cls, mod: Module, unmanagedCallConv: CallingConvention, returnType: Type
    ) -> SignatureHelper:
        """"""
    @classmethod
    @overload
    def GetMethodSigHelper(
        cls, mod: Module, returnType: Type, parameterTypes: Array[Type]
    ) -> SignatureHelper:
        """"""
    @classmethod
    @overload
    def GetMethodSigHelper(
        cls, unmanagedCallingConvention: CallingConvention, returnType: Type
    ) -> SignatureHelper:
        """"""
    @classmethod
    @overload
    def GetPropertySigHelper(
        cls,
        mod: Module,
        callingConvention: CallingConventions,
        returnType: Type,
        requiredReturnTypeCustomModifiers: Array[Type],
        optionalReturnTypeCustomModifiers: Array[Type],
        parameterTypes: Array[Type],
        requiredParameterTypeCustomModifiers: Array[Array[Type]],
        optionalParameterTypeCustomModifiers: Array[Array[Type]],
    ) -> SignatureHelper:
        """"""
    @classmethod
    @overload
    def GetPropertySigHelper(
        cls, mod: Module, returnType: Type, parameterTypes: Array[Type]
    ) -> SignatureHelper:
        """"""
    @classmethod
    @overload
    def GetPropertySigHelper(
        cls,
        mod: Module,
        returnType: Type,
        requiredReturnTypeCustomModifiers: Array[Type],
        optionalReturnTypeCustomModifiers: Array[Type],
        parameterTypes: Array[Type],
        requiredParameterTypeCustomModifiers: Array[Array[Type]],
        optionalParameterTypeCustomModifiers: Array[Array[Type]],
    ) -> SignatureHelper:
        """"""
    def GetSignature(self) -> Array[int]:
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
    def ToString(self) -> str:
        """"""

class SignatureToken(ValueType):
    """"""

    Empty: ClassVar[SignatureToken]
    """"""
    @property
    def Token(self) -> int:
        """"""
    @overload
    def Equals(self, obj: SignatureToken) -> bool:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def op_Equality(cls, a: SignatureToken, b: SignatureToken) -> bool:
        """"""
    @classmethod
    def op_Inequality(cls, a: SignatureToken, b: SignatureToken) -> bool:
        """"""
    def __eq__(self, other: SignatureToken) -> bool:
        """"""
    def __ne__(self, other: SignatureToken) -> bool:
        """"""

class StackBehaviour(Enum):
    """"""

    Pop0: StackBehaviour = ...
    """"""
    Pop1: StackBehaviour = ...
    """"""
    Pop1_pop1: StackBehaviour = ...
    """"""
    Popi: StackBehaviour = ...
    """"""
    Popi_pop1: StackBehaviour = ...
    """"""
    Popi_popi: StackBehaviour = ...
    """"""
    Popi_popi8: StackBehaviour = ...
    """"""
    Popi_popi_popi: StackBehaviour = ...
    """"""
    Popi_popr4: StackBehaviour = ...
    """"""
    Popi_popr8: StackBehaviour = ...
    """"""
    Popref: StackBehaviour = ...
    """"""
    Popref_pop1: StackBehaviour = ...
    """"""
    Popref_popi: StackBehaviour = ...
    """"""
    Popref_popi_popi: StackBehaviour = ...
    """"""
    Popref_popi_popi8: StackBehaviour = ...
    """"""
    Popref_popi_popr4: StackBehaviour = ...
    """"""
    Popref_popi_popr8: StackBehaviour = ...
    """"""
    Popref_popi_popref: StackBehaviour = ...
    """"""
    Push0: StackBehaviour = ...
    """"""
    Push1: StackBehaviour = ...
    """"""
    Push1_push1: StackBehaviour = ...
    """"""
    Pushi: StackBehaviour = ...
    """"""
    Pushi8: StackBehaviour = ...
    """"""
    Pushr4: StackBehaviour = ...
    """"""
    Pushr8: StackBehaviour = ...
    """"""
    Pushref: StackBehaviour = ...
    """"""
    Varpop: StackBehaviour = ...
    """"""
    Varpush: StackBehaviour = ...
    """"""
    Popref_popi_pop1: StackBehaviour = ...
    """"""

class StringToken(ValueType):
    """"""
    @property
    def Token(self) -> int:
        """"""
    @overload
    def Equals(self, obj: StringToken) -> bool:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def op_Equality(cls, a: StringToken, b: StringToken) -> bool:
        """"""
    @classmethod
    def op_Inequality(cls, a: StringToken, b: StringToken) -> bool:
        """"""
    def __eq__(self, other: StringToken) -> bool:
        """"""
    def __ne__(self, other: StringToken) -> bool:
        """"""

class SymbolMethod(MethodInfo, ICustomAttributeProvider, _MemberInfo, _MethodBase, _MethodInfo):
    """"""
    @property
    def Attributes(self) -> MethodAttributes:
        """"""
    @property
    def CallingConvention(self) -> CallingConventions:
        """"""
    @property
    def ContainsGenericParameters(self) -> bool:
        """"""
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
        """"""
    @property
    def DeclaringType(self) -> Type:
        """"""
    @property
    def IsAbstract(self) -> bool:
        """"""
    @property
    def IsAssembly(self) -> bool:
        """"""
    @property
    def IsConstructor(self) -> bool:
        """"""
    @property
    def IsFamily(self) -> bool:
        """"""
    @property
    def IsFamilyAndAssembly(self) -> bool:
        """"""
    @property
    def IsFamilyOrAssembly(self) -> bool:
        """"""
    @property
    def IsFinal(self) -> bool:
        """"""
    @property
    def IsGenericMethod(self) -> bool:
        """"""
    @property
    def IsGenericMethodDefinition(self) -> bool:
        """"""
    @property
    def IsHideBySig(self) -> bool:
        """"""
    @property
    def IsPrivate(self) -> bool:
        """"""
    @property
    def IsPublic(self) -> bool:
        """"""
    @property
    def IsSecurityCritical(self) -> bool:
        """"""
    @property
    def IsSecuritySafeCritical(self) -> bool:
        """"""
    @property
    def IsSecurityTransparent(self) -> bool:
        """"""
    @property
    def IsSpecialName(self) -> bool:
        """"""
    @property
    def IsStatic(self) -> bool:
        """"""
    @property
    def IsVirtual(self) -> bool:
        """"""
    @property
    def MemberType(self) -> MemberTypes:
        """"""
    @property
    def MetadataToken(self) -> int:
        """"""
    @property
    def MethodHandle(self) -> RuntimeMethodHandle:
        """"""
    @property
    def MethodImplementationFlags(self) -> MethodImplAttributes:
        """"""
    @property
    def Module(self) -> Module:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def ReflectedType(self) -> Type:
        """"""
    @property
    def ReturnParameter(self) -> ParameterInfo:
        """"""
    @property
    def ReturnType(self) -> Type:
        """"""
    @property
    def ReturnTypeCustomAttributes(self) -> ICustomAttributeProvider:
        """"""
    @overload
    def CreateDelegate(self, delegateType: Type) -> Delegate:
        """"""
    @overload
    def CreateDelegate(self, delegateType: Type, target: object) -> Delegate:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetBaseDefinition(self) -> MethodInfo:
        """"""
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """"""
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """"""
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]:
        """"""
    def GetGenericArguments(self) -> Array[Type]:
        """"""
    def GetGenericMethodDefinition(self) -> MethodInfo:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    def GetMethodBody(self) -> MethodBody:
        """"""
    def GetMethodImplementationFlags(self) -> MethodImplAttributes:
        """"""
    def GetModule(self) -> Module:
        """"""
    def GetParameters(self) -> Array[ParameterInfo]:
        """"""
    def GetToken(self) -> MethodToken:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """"""
    def GetTypeInfoCount(self, pcTInfo: UInt32) -> tuple[None, UInt32]:
        """"""
    @overload
    def Invoke(
        self,
        obj: object,
        invokeAttr: BindingFlags,
        binder: Binder,
        parameters: Array[object],
        culture: CultureInfo,
    ) -> object:
        """"""
    @overload
    def Invoke(self, obj: object, parameters: Array[object]) -> object:
        """"""
    @overload
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
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """"""
    def MakeGenericMethod(self, typeArguments: Array[Type]) -> MethodInfo:
        """"""
    def ToString(self) -> str:
        """"""

class SymbolType(
    TypeInfo, ICustomAttributeProvider, IReflect, IReflectableType, _MemberInfo, _Type
):
    """"""
    @property
    def Assembly(self) -> Assembly:
        """"""
    @property
    def AssemblyQualifiedName(self) -> str:
        """"""
    @property
    def Attributes(self) -> TypeAttributes:
        """"""
    @property
    def BaseType(self) -> Type:
        """"""
    @property
    def ContainsGenericParameters(self) -> bool:
        """"""
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
        """"""
    @property
    def DeclaredConstructors(self) -> IEnumerable[ConstructorInfo]:
        """"""
    @property
    def DeclaredEvents(self) -> IEnumerable[EventInfo]:
        """"""
    @property
    def DeclaredFields(self) -> IEnumerable[FieldInfo]:
        """"""
    @property
    def DeclaredMembers(self) -> IEnumerable[MemberInfo]:
        """"""
    @property
    def DeclaredMethods(self) -> IEnumerable[MethodInfo]:
        """"""
    @property
    def DeclaredNestedTypes(self) -> IEnumerable[TypeInfo]:
        """"""
    @property
    def DeclaredProperties(self) -> IEnumerable[PropertyInfo]:
        """"""
    @property
    def DeclaringMethod(self) -> MethodBase:
        """"""
    @property
    def DeclaringType(self) -> Type:
        """"""
    @property
    def FullName(self) -> str:
        """"""
    @property
    def GUID(self) -> Guid:
        """"""
    @property
    def GenericParameterAttributes(self) -> GenericParameterAttributes:
        """"""
    @property
    def GenericParameterPosition(self) -> int:
        """"""
    @property
    def GenericTypeArguments(self) -> Array[Type]:
        """"""
    @property
    def GenericTypeParameters(self) -> Array[Type]:
        """"""
    @property
    def HasElementType(self) -> bool:
        """"""
    @property
    def ImplementedInterfaces(self) -> IEnumerable[Type]:
        """"""
    @property
    def IsAbstract(self) -> bool:
        """"""
    @property
    def IsAnsiClass(self) -> bool:
        """"""
    @property
    def IsArray(self) -> bool:
        """"""
    @property
    def IsAutoClass(self) -> bool:
        """"""
    @property
    def IsAutoLayout(self) -> bool:
        """"""
    @property
    def IsByRef(self) -> bool:
        """"""
    @property
    def IsCOMObject(self) -> bool:
        """"""
    @property
    def IsClass(self) -> bool:
        """"""
    @property
    def IsConstructedGenericType(self) -> bool:
        """"""
    @property
    def IsContextful(self) -> bool:
        """"""
    @property
    def IsEnum(self) -> bool:
        """"""
    @property
    def IsExplicitLayout(self) -> bool:
        """"""
    @property
    def IsGenericParameter(self) -> bool:
        """"""
    @property
    def IsGenericType(self) -> bool:
        """"""
    @property
    def IsGenericTypeDefinition(self) -> bool:
        """"""
    @property
    def IsImport(self) -> bool:
        """"""
    @property
    def IsInterface(self) -> bool:
        """"""
    @property
    def IsLayoutSequential(self) -> bool:
        """"""
    @property
    def IsMarshalByRef(self) -> bool:
        """"""
    @property
    def IsNested(self) -> bool:
        """"""
    @property
    def IsNestedAssembly(self) -> bool:
        """"""
    @property
    def IsNestedFamANDAssem(self) -> bool:
        """"""
    @property
    def IsNestedFamORAssem(self) -> bool:
        """"""
    @property
    def IsNestedFamily(self) -> bool:
        """"""
    @property
    def IsNestedPrivate(self) -> bool:
        """"""
    @property
    def IsNestedPublic(self) -> bool:
        """"""
    @property
    def IsNotPublic(self) -> bool:
        """"""
    @property
    def IsPointer(self) -> bool:
        """"""
    @property
    def IsPrimitive(self) -> bool:
        """"""
    @property
    def IsPublic(self) -> bool:
        """"""
    @property
    def IsSealed(self) -> bool:
        """"""
    @property
    def IsSecurityCritical(self) -> bool:
        """"""
    @property
    def IsSecuritySafeCritical(self) -> bool:
        """"""
    @property
    def IsSecurityTransparent(self) -> bool:
        """"""
    @property
    def IsSerializable(self) -> bool:
        """"""
    @property
    def IsSpecialName(self) -> bool:
        """"""
    @property
    def IsUnicodeClass(self) -> bool:
        """"""
    @property
    def IsValueType(self) -> bool:
        """"""
    @property
    def IsVisible(self) -> bool:
        """"""
    @property
    def MemberType(self) -> MemberTypes:
        """"""
    @property
    def MetadataToken(self) -> int:
        """"""
    @property
    def Module(self) -> Module:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def Namespace(self) -> str:
        """"""
    @property
    def ReflectedType(self) -> Type:
        """"""
    @property
    def StructLayoutAttribute(self) -> StructLayoutAttribute:
        """"""
    @property
    def TypeHandle(self) -> RuntimeTypeHandle:
        """"""
    @property
    def TypeInitializer(self) -> ConstructorInfo:
        """"""
    @property
    def UnderlyingSystemType(self) -> Type:
        """"""
    def AsType(self) -> Type:
        """"""
    @overload
    def Equals(self, o: object) -> bool:
        """"""
    @overload
    def Equals(self, o: Type) -> bool:
        """"""
    def FindInterfaces(self, filter: TypeFilter, filterCriteria: object) -> Array[Type]:
        """"""
    def FindMembers(
        self,
        memberType: MemberTypes,
        bindingAttr: BindingFlags,
        filter: MemberFilter,
        filterCriteria: object,
    ) -> Array[MemberInfo]:
        """"""
    def GetArrayRank(self) -> int:
        """"""
    @overload
    def GetConstructor(
        self,
        bindingAttr: BindingFlags,
        binder: Binder,
        callConvention: CallingConventions,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> ConstructorInfo:
        """"""
    @overload
    def GetConstructor(
        self,
        bindingAttr: BindingFlags,
        binder: Binder,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> ConstructorInfo:
        """"""
    @overload
    def GetConstructor(self, types: Array[Type]) -> ConstructorInfo:
        """"""
    @overload
    def GetConstructors(self) -> Array[ConstructorInfo]:
        """"""
    @overload
    def GetConstructors(self, bindingAttr: BindingFlags) -> Array[ConstructorInfo]:
        """"""
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """"""
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """"""
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]:
        """"""
    def GetDeclaredEvent(self, name: str) -> EventInfo:
        """"""
    def GetDeclaredField(self, name: str) -> FieldInfo:
        """"""
    def GetDeclaredMethod(self, name: str) -> MethodInfo:
        """"""
    def GetDeclaredMethods(self, name: str) -> IEnumerable[MethodInfo]:
        """"""
    def GetDeclaredNestedType(self, name: str) -> TypeInfo:
        """"""
    def GetDeclaredProperty(self, name: str) -> PropertyInfo:
        """"""
    def GetDefaultMembers(self) -> Array[MemberInfo]:
        """"""
    def GetElementType(self) -> Type:
        """"""
    def GetEnumName(self, value: object) -> str:
        """"""
    def GetEnumNames(self) -> Array[str]:
        """"""
    def GetEnumUnderlyingType(self) -> Type:
        """"""
    def GetEnumValues(self) -> Array:
        """"""
    @overload
    def GetEvent(self, name: str) -> EventInfo:
        """"""
    @overload
    def GetEvent(self, name: str, bindingAttr: BindingFlags) -> EventInfo:
        """"""
    @overload
    def GetEvents(self) -> Array[EventInfo]:
        """"""
    @overload
    def GetEvents(self, bindingAttr: BindingFlags) -> Array[EventInfo]:
        """"""
    @overload
    def GetField(self, name: str) -> FieldInfo:
        """"""
    @overload
    def GetField(self, name: str, bindingAttr: BindingFlags) -> FieldInfo:
        """"""
    @overload
    def GetFields(self) -> Array[FieldInfo]:
        """"""
    @overload
    def GetFields(self, bindingAttr: BindingFlags) -> Array[FieldInfo]:
        """"""
    def GetGenericArguments(self) -> Array[Type]:
        """"""
    def GetGenericParameterConstraints(self) -> Array[Type]:
        """"""
    def GetGenericTypeDefinition(self) -> Type:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    @overload
    def GetInterface(self, name: str) -> Type:
        """"""
    @overload
    def GetInterface(self, name: str, ignoreCase: bool) -> Type:
        """"""
    def GetInterfaceMap(self, interfaceType: Type) -> InterfaceMapping:
        """"""
    def GetInterfaces(self) -> Array[Type]:
        """"""
    @overload
    def GetMember(self, name: str) -> Array[MemberInfo]:
        """"""
    @overload
    def GetMember(self, name: str, bindingAttr: BindingFlags) -> Array[MemberInfo]:
        """"""
    @overload
    def GetMember(
        self, name: str, type: MemberTypes, bindingAttr: BindingFlags
    ) -> Array[MemberInfo]:
        """"""
    @overload
    def GetMembers(self) -> Array[MemberInfo]:
        """"""
    @overload
    def GetMembers(self, bindingAttr: BindingFlags) -> Array[MemberInfo]:
        """"""
    @overload
    def GetMethod(self, name: str) -> MethodInfo:
        """"""
    @overload
    def GetMethod(self, name: str, bindingAttr: BindingFlags) -> MethodInfo:
        """"""
    @overload
    def GetMethod(
        self,
        name: str,
        bindingAttr: BindingFlags,
        binder: Binder,
        callConvention: CallingConventions,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> MethodInfo:
        """"""
    @overload
    def GetMethod(
        self,
        name: str,
        bindingAttr: BindingFlags,
        binder: Binder,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> MethodInfo:
        """"""
    @overload
    def GetMethod(self, name: str, types: Array[Type]) -> MethodInfo:
        """"""
    @overload
    def GetMethod(
        self, name: str, types: Array[Type], modifiers: Array[ParameterModifier]
    ) -> MethodInfo:
        """"""
    @overload
    def GetMethods(self) -> Array[MethodInfo]:
        """"""
    @overload
    def GetMethods(self, bindingAttr: BindingFlags) -> Array[MethodInfo]:
        """"""
    @overload
    def GetNestedType(self, name: str) -> Type:
        """"""
    @overload
    def GetNestedType(self, name: str, bindingAttr: BindingFlags) -> Type:
        """"""
    @overload
    def GetNestedTypes(self) -> Array[Type]:
        """"""
    @overload
    def GetNestedTypes(self, bindingAttr: BindingFlags) -> Array[Type]:
        """"""
    @overload
    def GetProperties(self) -> Array[PropertyInfo]:
        """"""
    @overload
    def GetProperties(self, bindingAttr: BindingFlags) -> Array[PropertyInfo]:
        """"""
    @overload
    def GetProperty(self, name: str) -> PropertyInfo:
        """"""
    @overload
    def GetProperty(self, name: str, bindingAttr: BindingFlags) -> PropertyInfo:
        """"""
    @overload
    def GetProperty(
        self,
        name: str,
        bindingAttr: BindingFlags,
        binder: Binder,
        returnType: Type,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> PropertyInfo:
        """"""
    @overload
    def GetProperty(self, name: str, types: Array[Type]) -> PropertyInfo:
        """"""
    @overload
    def GetProperty(self, name: str, returnType: Type) -> PropertyInfo:
        """"""
    @overload
    def GetProperty(self, name: str, returnType: Type, types: Array[Type]) -> PropertyInfo:
        """"""
    @overload
    def GetProperty(
        self, name: str, returnType: Type, types: Array[Type], modifiers: Array[ParameterModifier]
    ) -> PropertyInfo:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def GetTypeInfo(self) -> TypeInfo:
        """"""
    @overload
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
    @overload
    def InvokeMember(
        self,
        name: str,
        invokeAttr: BindingFlags,
        binder: Binder,
        target: object,
        args: Array[object],
    ) -> object:
        """"""
    @overload
    def InvokeMember(
        self,
        name: str,
        invokeAttr: BindingFlags,
        binder: Binder,
        target: object,
        args: Array[object],
        culture: CultureInfo,
    ) -> object:
        """"""
    @overload
    def InvokeMember(
        self,
        name: str,
        invokeAttr: BindingFlags,
        binder: Binder,
        target: object,
        args: Array[object],
        modifiers: Array[ParameterModifier],
        culture: CultureInfo,
        namedParameters: Array[str],
    ) -> object:
        """"""
    @overload
    def IsAssignableFrom(self, typeInfo: TypeInfo) -> bool:
        """"""
    @overload
    def IsAssignableFrom(self, c: Type) -> bool:
        """"""
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """"""
    def IsEnumDefined(self, value: object) -> bool:
        """"""
    def IsEquivalentTo(self, other: Type) -> bool:
        """"""
    def IsInstanceOfType(self, o: object) -> bool:
        """"""
    def IsSubclassOf(self, c: Type) -> bool:
        """"""
    @overload
    def MakeArrayType(self) -> Type:
        """"""
    @overload
    def MakeArrayType(self, rank: int) -> Type:
        """"""
    def MakeByRefType(self) -> Type:
        """"""
    def MakeGenericType(self, typeArguments: Array[Type]) -> Type:
        """"""
    def MakePointerType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class TypeBuilder(
    TypeInfo, ICustomAttributeProvider, IReflect, IReflectableType, _MemberInfo, _Type, _TypeBuilder
):
    """"""

    UnspecifiedTypeSize: ClassVar[int]
    """"""
    @property
    def Assembly(self) -> Assembly:
        """"""
    @property
    def AssemblyQualifiedName(self) -> str:
        """"""
    @property
    def Attributes(self) -> TypeAttributes:
        """"""
    @property
    def BaseType(self) -> Type:
        """"""
    @property
    def ContainsGenericParameters(self) -> bool:
        """"""
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
        """"""
    @property
    def DeclaredConstructors(self) -> IEnumerable[ConstructorInfo]:
        """"""
    @property
    def DeclaredEvents(self) -> IEnumerable[EventInfo]:
        """"""
    @property
    def DeclaredFields(self) -> IEnumerable[FieldInfo]:
        """"""
    @property
    def DeclaredMembers(self) -> IEnumerable[MemberInfo]:
        """"""
    @property
    def DeclaredMethods(self) -> IEnumerable[MethodInfo]:
        """"""
    @property
    def DeclaredNestedTypes(self) -> IEnumerable[TypeInfo]:
        """"""
    @property
    def DeclaredProperties(self) -> IEnumerable[PropertyInfo]:
        """"""
    @property
    def DeclaringMethod(self) -> MethodBase:
        """"""
    @property
    def DeclaringType(self) -> Type:
        """"""
    @property
    def FullName(self) -> str:
        """"""
    @property
    def GUID(self) -> Guid:
        """"""
    @property
    def GenericParameterAttributes(self) -> GenericParameterAttributes:
        """"""
    @property
    def GenericParameterPosition(self) -> int:
        """"""
    @property
    def GenericTypeArguments(self) -> Array[Type]:
        """"""
    @property
    def GenericTypeParameters(self) -> Array[Type]:
        """"""
    @property
    def HasElementType(self) -> bool:
        """"""
    @property
    def ImplementedInterfaces(self) -> IEnumerable[Type]:
        """"""
    @property
    def IsAbstract(self) -> bool:
        """"""
    @property
    def IsAnsiClass(self) -> bool:
        """"""
    @property
    def IsArray(self) -> bool:
        """"""
    @property
    def IsAutoClass(self) -> bool:
        """"""
    @property
    def IsAutoLayout(self) -> bool:
        """"""
    @property
    def IsByRef(self) -> bool:
        """"""
    @property
    def IsCOMObject(self) -> bool:
        """"""
    @property
    def IsClass(self) -> bool:
        """"""
    @property
    def IsConstructedGenericType(self) -> bool:
        """"""
    @property
    def IsContextful(self) -> bool:
        """"""
    @property
    def IsEnum(self) -> bool:
        """"""
    @property
    def IsExplicitLayout(self) -> bool:
        """"""
    @property
    def IsGenericParameter(self) -> bool:
        """"""
    @property
    def IsGenericType(self) -> bool:
        """"""
    @property
    def IsGenericTypeDefinition(self) -> bool:
        """"""
    @property
    def IsImport(self) -> bool:
        """"""
    @property
    def IsInterface(self) -> bool:
        """"""
    @property
    def IsLayoutSequential(self) -> bool:
        """"""
    @property
    def IsMarshalByRef(self) -> bool:
        """"""
    @property
    def IsNested(self) -> bool:
        """"""
    @property
    def IsNestedAssembly(self) -> bool:
        """"""
    @property
    def IsNestedFamANDAssem(self) -> bool:
        """"""
    @property
    def IsNestedFamORAssem(self) -> bool:
        """"""
    @property
    def IsNestedFamily(self) -> bool:
        """"""
    @property
    def IsNestedPrivate(self) -> bool:
        """"""
    @property
    def IsNestedPublic(self) -> bool:
        """"""
    @property
    def IsNotPublic(self) -> bool:
        """"""
    @property
    def IsPointer(self) -> bool:
        """"""
    @property
    def IsPrimitive(self) -> bool:
        """"""
    @property
    def IsPublic(self) -> bool:
        """"""
    @property
    def IsSealed(self) -> bool:
        """"""
    @property
    def IsSecurityCritical(self) -> bool:
        """"""
    @property
    def IsSecuritySafeCritical(self) -> bool:
        """"""
    @property
    def IsSecurityTransparent(self) -> bool:
        """"""
    @property
    def IsSerializable(self) -> bool:
        """"""
    @property
    def IsSpecialName(self) -> bool:
        """"""
    @property
    def IsUnicodeClass(self) -> bool:
        """"""
    @property
    def IsValueType(self) -> bool:
        """"""
    @property
    def IsVisible(self) -> bool:
        """"""
    @property
    def MemberType(self) -> MemberTypes:
        """"""
    @property
    def MetadataToken(self) -> int:
        """"""
    @property
    def Module(self) -> Module:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def Namespace(self) -> str:
        """"""
    @property
    def PackingSize(self) -> PackingSize:
        """"""
    @property
    def ReflectedType(self) -> Type:
        """"""
    @property
    def Size(self) -> int:
        """"""
    @property
    def StructLayoutAttribute(self) -> StructLayoutAttribute:
        """"""
    @property
    def TypeHandle(self) -> RuntimeTypeHandle:
        """"""
    @property
    def TypeInitializer(self) -> ConstructorInfo:
        """"""
    @property
    def TypeToken(self) -> TypeToken:
        """"""
    @property
    def UnderlyingSystemType(self) -> Type:
        """"""
    def AddDeclarativeSecurity(self, action: SecurityAction, pset: PermissionSet) -> None:
        """"""
    def AddInterfaceImplementation(self, interfaceType: Type) -> None:
        """"""
    def AsType(self) -> Type:
        """"""
    def CreateType(self) -> Type:
        """"""
    def CreateTypeInfo(self) -> TypeInfo:
        """"""
    @overload
    def DefineConstructor(
        self,
        attributes: MethodAttributes,
        callingConvention: CallingConventions,
        parameterTypes: Array[Type],
    ) -> ConstructorBuilder:
        """"""
    @overload
    def DefineConstructor(
        self,
        attributes: MethodAttributes,
        callingConvention: CallingConventions,
        parameterTypes: Array[Type],
        requiredCustomModifiers: Array[Array[Type]],
        optionalCustomModifiers: Array[Array[Type]],
    ) -> ConstructorBuilder:
        """"""
    def DefineDefaultConstructor(self, attributes: MethodAttributes) -> ConstructorBuilder:
        """"""
    def DefineEvent(self, name: str, attributes: EventAttributes, eventtype: Type) -> EventBuilder:
        """"""
    @overload
    def DefineField(self, fieldName: str, type: Type, attributes: FieldAttributes) -> FieldBuilder:
        """"""
    @overload
    def DefineField(
        self,
        fieldName: str,
        type: Type,
        requiredCustomModifiers: Array[Type],
        optionalCustomModifiers: Array[Type],
        attributes: FieldAttributes,
    ) -> FieldBuilder:
        """"""
    def DefineGenericParameters(self, names: Array[str]) -> Array[GenericTypeParameterBuilder]:
        """"""
    def DefineInitializedData(
        self, name: str, data: Array[int], attributes: FieldAttributes
    ) -> FieldBuilder:
        """"""
    @overload
    def DefineMethod(self, name: str, attributes: MethodAttributes) -> MethodBuilder:
        """"""
    @overload
    def DefineMethod(
        self, name: str, attributes: MethodAttributes, callingConvention: CallingConventions
    ) -> MethodBuilder:
        """"""
    @overload
    def DefineMethod(
        self,
        name: str,
        attributes: MethodAttributes,
        callingConvention: CallingConventions,
        returnType: Type,
        parameterTypes: Array[Type],
    ) -> MethodBuilder:
        """"""
    @overload
    def DefineMethod(
        self,
        name: str,
        attributes: MethodAttributes,
        callingConvention: CallingConventions,
        returnType: Type,
        returnTypeRequiredCustomModifiers: Array[Type],
        returnTypeOptionalCustomModifiers: Array[Type],
        parameterTypes: Array[Type],
        parameterTypeRequiredCustomModifiers: Array[Array[Type]],
        parameterTypeOptionalCustomModifiers: Array[Array[Type]],
    ) -> MethodBuilder:
        """"""
    @overload
    def DefineMethod(
        self, name: str, attributes: MethodAttributes, returnType: Type, parameterTypes: Array[Type]
    ) -> MethodBuilder:
        """"""
    def DefineMethodOverride(
        self, methodInfoBody: MethodInfo, methodInfoDeclaration: MethodInfo
    ) -> None:
        """"""
    @overload
    def DefineNestedType(self, name: str) -> TypeBuilder:
        """"""
    @overload
    def DefineNestedType(self, name: str, attr: TypeAttributes) -> TypeBuilder:
        """"""
    @overload
    def DefineNestedType(self, name: str, attr: TypeAttributes, parent: Type) -> TypeBuilder:
        """"""
    @overload
    def DefineNestedType(
        self, name: str, attr: TypeAttributes, parent: Type, packSize: PackingSize
    ) -> TypeBuilder:
        """"""
    @overload
    def DefineNestedType(
        self, name: str, attr: TypeAttributes, parent: Type, packSize: PackingSize, typeSize: int
    ) -> TypeBuilder:
        """"""
    @overload
    def DefineNestedType(
        self, name: str, attr: TypeAttributes, parent: Type, interfaces: Array[Type]
    ) -> TypeBuilder:
        """"""
    @overload
    def DefineNestedType(
        self, name: str, attr: TypeAttributes, parent: Type, typeSize: int
    ) -> TypeBuilder:
        """"""
    @overload
    def DefinePInvokeMethod(
        self,
        name: str,
        dllName: str,
        attributes: MethodAttributes,
        callingConvention: CallingConventions,
        returnType: Type,
        parameterTypes: Array[Type],
        nativeCallConv: CallingConvention,
        nativeCharSet: CharSet,
    ) -> MethodBuilder:
        """"""
    @overload
    def DefinePInvokeMethod(
        self,
        name: str,
        dllName: str,
        entryName: str,
        attributes: MethodAttributes,
        callingConvention: CallingConventions,
        returnType: Type,
        parameterTypes: Array[Type],
        nativeCallConv: CallingConvention,
        nativeCharSet: CharSet,
    ) -> MethodBuilder:
        """"""
    @overload
    def DefinePInvokeMethod(
        self,
        name: str,
        dllName: str,
        entryName: str,
        attributes: MethodAttributes,
        callingConvention: CallingConventions,
        returnType: Type,
        returnTypeRequiredCustomModifiers: Array[Type],
        returnTypeOptionalCustomModifiers: Array[Type],
        parameterTypes: Array[Type],
        parameterTypeRequiredCustomModifiers: Array[Array[Type]],
        parameterTypeOptionalCustomModifiers: Array[Array[Type]],
        nativeCallConv: CallingConvention,
        nativeCharSet: CharSet,
    ) -> MethodBuilder:
        """"""
    @overload
    def DefineProperty(
        self,
        name: str,
        attributes: PropertyAttributes,
        callingConvention: CallingConventions,
        returnType: Type,
        parameterTypes: Array[Type],
    ) -> PropertyBuilder:
        """"""
    @overload
    def DefineProperty(
        self,
        name: str,
        attributes: PropertyAttributes,
        callingConvention: CallingConventions,
        returnType: Type,
        returnTypeRequiredCustomModifiers: Array[Type],
        returnTypeOptionalCustomModifiers: Array[Type],
        parameterTypes: Array[Type],
        parameterTypeRequiredCustomModifiers: Array[Array[Type]],
        parameterTypeOptionalCustomModifiers: Array[Array[Type]],
    ) -> PropertyBuilder:
        """"""
    @overload
    def DefineProperty(
        self,
        name: str,
        attributes: PropertyAttributes,
        returnType: Type,
        parameterTypes: Array[Type],
    ) -> PropertyBuilder:
        """"""
    @overload
    def DefineProperty(
        self,
        name: str,
        attributes: PropertyAttributes,
        returnType: Type,
        returnTypeRequiredCustomModifiers: Array[Type],
        returnTypeOptionalCustomModifiers: Array[Type],
        parameterTypes: Array[Type],
        parameterTypeRequiredCustomModifiers: Array[Array[Type]],
        parameterTypeOptionalCustomModifiers: Array[Array[Type]],
    ) -> PropertyBuilder:
        """"""
    def DefineTypeInitializer(self) -> ConstructorBuilder:
        """"""
    def DefineUninitializedData(
        self, name: str, size: int, attributes: FieldAttributes
    ) -> FieldBuilder:
        """"""
    @overload
    def Equals(self, o: object) -> bool:
        """"""
    @overload
    def Equals(self, o: Type) -> bool:
        """"""
    def FindInterfaces(self, filter: TypeFilter, filterCriteria: object) -> Array[Type]:
        """"""
    def FindMembers(
        self,
        memberType: MemberTypes,
        bindingAttr: BindingFlags,
        filter: MemberFilter,
        filterCriteria: object,
    ) -> Array[MemberInfo]:
        """"""
    def GetArrayRank(self) -> int:
        """"""
    @overload
    def GetConstructor(
        self,
        bindingAttr: BindingFlags,
        binder: Binder,
        callConvention: CallingConventions,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> ConstructorInfo:
        """"""
    @overload
    def GetConstructor(
        self,
        bindingAttr: BindingFlags,
        binder: Binder,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> ConstructorInfo:
        """"""
    @overload
    def GetConstructor(self, types: Array[Type]) -> ConstructorInfo:
        """"""
    @classmethod
    @overload
    def GetConstructor(cls, type: Type, constructor: ConstructorInfo) -> ConstructorInfo:
        """"""
    @overload
    def GetConstructors(self) -> Array[ConstructorInfo]:
        """"""
    @overload
    def GetConstructors(self, bindingAttr: BindingFlags) -> Array[ConstructorInfo]:
        """"""
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """"""
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """"""
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]:
        """"""
    def GetDeclaredEvent(self, name: str) -> EventInfo:
        """"""
    def GetDeclaredField(self, name: str) -> FieldInfo:
        """"""
    def GetDeclaredMethod(self, name: str) -> MethodInfo:
        """"""
    def GetDeclaredMethods(self, name: str) -> IEnumerable[MethodInfo]:
        """"""
    def GetDeclaredNestedType(self, name: str) -> TypeInfo:
        """"""
    def GetDeclaredProperty(self, name: str) -> PropertyInfo:
        """"""
    def GetDefaultMembers(self) -> Array[MemberInfo]:
        """"""
    def GetElementType(self) -> Type:
        """"""
    def GetEnumName(self, value: object) -> str:
        """"""
    def GetEnumNames(self) -> Array[str]:
        """"""
    def GetEnumUnderlyingType(self) -> Type:
        """"""
    def GetEnumValues(self) -> Array:
        """"""
    @overload
    def GetEvent(self, name: str) -> EventInfo:
        """"""
    @overload
    def GetEvent(self, name: str, bindingAttr: BindingFlags) -> EventInfo:
        """"""
    @overload
    def GetEvents(self) -> Array[EventInfo]:
        """"""
    @overload
    def GetEvents(self, bindingAttr: BindingFlags) -> Array[EventInfo]:
        """"""
    @overload
    def GetField(self, name: str) -> FieldInfo:
        """"""
    @overload
    def GetField(self, name: str, bindingAttr: BindingFlags) -> FieldInfo:
        """"""
    @classmethod
    @overload
    def GetField(cls, type: Type, field: FieldInfo) -> FieldInfo:
        """"""
    @overload
    def GetFields(self) -> Array[FieldInfo]:
        """"""
    @overload
    def GetFields(self, bindingAttr: BindingFlags) -> Array[FieldInfo]:
        """"""
    def GetGenericArguments(self) -> Array[Type]:
        """"""
    def GetGenericParameterConstraints(self) -> Array[Type]:
        """"""
    def GetGenericTypeDefinition(self) -> Type:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    @overload
    def GetInterface(self, name: str) -> Type:
        """"""
    @overload
    def GetInterface(self, name: str, ignoreCase: bool) -> Type:
        """"""
    def GetInterfaceMap(self, interfaceType: Type) -> InterfaceMapping:
        """"""
    def GetInterfaces(self) -> Array[Type]:
        """"""
    @overload
    def GetMember(self, name: str) -> Array[MemberInfo]:
        """"""
    @overload
    def GetMember(self, name: str, bindingAttr: BindingFlags) -> Array[MemberInfo]:
        """"""
    @overload
    def GetMember(
        self, name: str, type: MemberTypes, bindingAttr: BindingFlags
    ) -> Array[MemberInfo]:
        """"""
    @overload
    def GetMembers(self) -> Array[MemberInfo]:
        """"""
    @overload
    def GetMembers(self, bindingAttr: BindingFlags) -> Array[MemberInfo]:
        """"""
    @overload
    def GetMethod(self, name: str) -> MethodInfo:
        """"""
    @overload
    def GetMethod(self, name: str, bindingAttr: BindingFlags) -> MethodInfo:
        """"""
    @overload
    def GetMethod(
        self,
        name: str,
        bindingAttr: BindingFlags,
        binder: Binder,
        callConvention: CallingConventions,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> MethodInfo:
        """"""
    @overload
    def GetMethod(
        self,
        name: str,
        bindingAttr: BindingFlags,
        binder: Binder,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> MethodInfo:
        """"""
    @overload
    def GetMethod(self, name: str, types: Array[Type]) -> MethodInfo:
        """"""
    @overload
    def GetMethod(
        self, name: str, types: Array[Type], modifiers: Array[ParameterModifier]
    ) -> MethodInfo:
        """"""
    @classmethod
    @overload
    def GetMethod(cls, type: Type, method: MethodInfo) -> MethodInfo:
        """"""
    @overload
    def GetMethods(self) -> Array[MethodInfo]:
        """"""
    @overload
    def GetMethods(self, bindingAttr: BindingFlags) -> Array[MethodInfo]:
        """"""
    @overload
    def GetNestedType(self, name: str) -> Type:
        """"""
    @overload
    def GetNestedType(self, name: str, bindingAttr: BindingFlags) -> Type:
        """"""
    @overload
    def GetNestedTypes(self) -> Array[Type]:
        """"""
    @overload
    def GetNestedTypes(self, bindingAttr: BindingFlags) -> Array[Type]:
        """"""
    @overload
    def GetProperties(self) -> Array[PropertyInfo]:
        """"""
    @overload
    def GetProperties(self, bindingAttr: BindingFlags) -> Array[PropertyInfo]:
        """"""
    @overload
    def GetProperty(self, name: str) -> PropertyInfo:
        """"""
    @overload
    def GetProperty(self, name: str, bindingAttr: BindingFlags) -> PropertyInfo:
        """"""
    @overload
    def GetProperty(
        self,
        name: str,
        bindingAttr: BindingFlags,
        binder: Binder,
        returnType: Type,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> PropertyInfo:
        """"""
    @overload
    def GetProperty(self, name: str, types: Array[Type]) -> PropertyInfo:
        """"""
    @overload
    def GetProperty(self, name: str, returnType: Type) -> PropertyInfo:
        """"""
    @overload
    def GetProperty(self, name: str, returnType: Type, types: Array[Type]) -> PropertyInfo:
        """"""
    @overload
    def GetProperty(
        self, name: str, returnType: Type, types: Array[Type], modifiers: Array[ParameterModifier]
    ) -> PropertyInfo:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def GetTypeInfo(self) -> TypeInfo:
        """"""
    @overload
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
    @overload
    def InvokeMember(
        self,
        name: str,
        invokeAttr: BindingFlags,
        binder: Binder,
        target: object,
        args: Array[object],
    ) -> object:
        """"""
    @overload
    def InvokeMember(
        self,
        name: str,
        invokeAttr: BindingFlags,
        binder: Binder,
        target: object,
        args: Array[object],
        culture: CultureInfo,
    ) -> object:
        """"""
    @overload
    def InvokeMember(
        self,
        name: str,
        invokeAttr: BindingFlags,
        binder: Binder,
        target: object,
        args: Array[object],
        modifiers: Array[ParameterModifier],
        culture: CultureInfo,
        namedParameters: Array[str],
    ) -> object:
        """"""
    @overload
    def IsAssignableFrom(self, typeInfo: TypeInfo) -> bool:
        """"""
    @overload
    def IsAssignableFrom(self, c: Type) -> bool:
        """"""
    def IsCreated(self) -> bool:
        """"""
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """"""
    def IsEnumDefined(self, value: object) -> bool:
        """"""
    def IsEquivalentTo(self, other: Type) -> bool:
        """"""
    def IsInstanceOfType(self, o: object) -> bool:
        """"""
    def IsSubclassOf(self, c: Type) -> bool:
        """"""
    @overload
    def MakeArrayType(self) -> Type:
        """"""
    @overload
    def MakeArrayType(self, rank: int) -> Type:
        """"""
    def MakeByRefType(self) -> Type:
        """"""
    def MakeGenericType(self, typeArguments: Array[Type]) -> Type:
        """"""
    def MakePointerType(self) -> Type:
        """"""
    @overload
    def SetCustomAttribute(self, customBuilder: CustomAttributeBuilder) -> None:
        """"""
    @overload
    def SetCustomAttribute(self, con: ConstructorInfo, binaryAttribute: Array[int]) -> None:
        """"""
    def SetParent(self, parent: Type) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class TypeBuilderInstantiation(
    TypeInfo, ICustomAttributeProvider, IReflect, IReflectableType, _MemberInfo, _Type
):
    """"""
    @property
    def Assembly(self) -> Assembly:
        """"""
    @property
    def AssemblyQualifiedName(self) -> str:
        """"""
    @property
    def Attributes(self) -> TypeAttributes:
        """"""
    @property
    def BaseType(self) -> Type:
        """"""
    @property
    def ContainsGenericParameters(self) -> bool:
        """"""
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
        """"""
    @property
    def DeclaredConstructors(self) -> IEnumerable[ConstructorInfo]:
        """"""
    @property
    def DeclaredEvents(self) -> IEnumerable[EventInfo]:
        """"""
    @property
    def DeclaredFields(self) -> IEnumerable[FieldInfo]:
        """"""
    @property
    def DeclaredMembers(self) -> IEnumerable[MemberInfo]:
        """"""
    @property
    def DeclaredMethods(self) -> IEnumerable[MethodInfo]:
        """"""
    @property
    def DeclaredNestedTypes(self) -> IEnumerable[TypeInfo]:
        """"""
    @property
    def DeclaredProperties(self) -> IEnumerable[PropertyInfo]:
        """"""
    @property
    def DeclaringMethod(self) -> MethodBase:
        """"""
    @property
    def DeclaringType(self) -> Type:
        """"""
    @property
    def FullName(self) -> str:
        """"""
    @property
    def GUID(self) -> Guid:
        """"""
    @property
    def GenericParameterAttributes(self) -> GenericParameterAttributes:
        """"""
    @property
    def GenericParameterPosition(self) -> int:
        """"""
    @property
    def GenericTypeArguments(self) -> Array[Type]:
        """"""
    @property
    def GenericTypeParameters(self) -> Array[Type]:
        """"""
    @property
    def HasElementType(self) -> bool:
        """"""
    @property
    def ImplementedInterfaces(self) -> IEnumerable[Type]:
        """"""
    @property
    def IsAbstract(self) -> bool:
        """"""
    @property
    def IsAnsiClass(self) -> bool:
        """"""
    @property
    def IsArray(self) -> bool:
        """"""
    @property
    def IsAutoClass(self) -> bool:
        """"""
    @property
    def IsAutoLayout(self) -> bool:
        """"""
    @property
    def IsByRef(self) -> bool:
        """"""
    @property
    def IsCOMObject(self) -> bool:
        """"""
    @property
    def IsClass(self) -> bool:
        """"""
    @property
    def IsConstructedGenericType(self) -> bool:
        """"""
    @property
    def IsContextful(self) -> bool:
        """"""
    @property
    def IsEnum(self) -> bool:
        """"""
    @property
    def IsExplicitLayout(self) -> bool:
        """"""
    @property
    def IsGenericParameter(self) -> bool:
        """"""
    @property
    def IsGenericType(self) -> bool:
        """"""
    @property
    def IsGenericTypeDefinition(self) -> bool:
        """"""
    @property
    def IsImport(self) -> bool:
        """"""
    @property
    def IsInterface(self) -> bool:
        """"""
    @property
    def IsLayoutSequential(self) -> bool:
        """"""
    @property
    def IsMarshalByRef(self) -> bool:
        """"""
    @property
    def IsNested(self) -> bool:
        """"""
    @property
    def IsNestedAssembly(self) -> bool:
        """"""
    @property
    def IsNestedFamANDAssem(self) -> bool:
        """"""
    @property
    def IsNestedFamORAssem(self) -> bool:
        """"""
    @property
    def IsNestedFamily(self) -> bool:
        """"""
    @property
    def IsNestedPrivate(self) -> bool:
        """"""
    @property
    def IsNestedPublic(self) -> bool:
        """"""
    @property
    def IsNotPublic(self) -> bool:
        """"""
    @property
    def IsPointer(self) -> bool:
        """"""
    @property
    def IsPrimitive(self) -> bool:
        """"""
    @property
    def IsPublic(self) -> bool:
        """"""
    @property
    def IsSealed(self) -> bool:
        """"""
    @property
    def IsSecurityCritical(self) -> bool:
        """"""
    @property
    def IsSecuritySafeCritical(self) -> bool:
        """"""
    @property
    def IsSecurityTransparent(self) -> bool:
        """"""
    @property
    def IsSerializable(self) -> bool:
        """"""
    @property
    def IsSpecialName(self) -> bool:
        """"""
    @property
    def IsUnicodeClass(self) -> bool:
        """"""
    @property
    def IsValueType(self) -> bool:
        """"""
    @property
    def IsVisible(self) -> bool:
        """"""
    @property
    def MemberType(self) -> MemberTypes:
        """"""
    @property
    def MetadataToken(self) -> int:
        """"""
    @property
    def Module(self) -> Module:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def Namespace(self) -> str:
        """"""
    @property
    def ReflectedType(self) -> Type:
        """"""
    @property
    def StructLayoutAttribute(self) -> StructLayoutAttribute:
        """"""
    @property
    def TypeHandle(self) -> RuntimeTypeHandle:
        """"""
    @property
    def TypeInitializer(self) -> ConstructorInfo:
        """"""
    @property
    def UnderlyingSystemType(self) -> Type:
        """"""
    def AsType(self) -> Type:
        """"""
    @overload
    def Equals(self, o: object) -> bool:
        """"""
    @overload
    def Equals(self, o: Type) -> bool:
        """"""
    def FindInterfaces(self, filter: TypeFilter, filterCriteria: object) -> Array[Type]:
        """"""
    def FindMembers(
        self,
        memberType: MemberTypes,
        bindingAttr: BindingFlags,
        filter: MemberFilter,
        filterCriteria: object,
    ) -> Array[MemberInfo]:
        """"""
    def GetArrayRank(self) -> int:
        """"""
    @overload
    def GetConstructor(
        self,
        bindingAttr: BindingFlags,
        binder: Binder,
        callConvention: CallingConventions,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> ConstructorInfo:
        """"""
    @overload
    def GetConstructor(
        self,
        bindingAttr: BindingFlags,
        binder: Binder,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> ConstructorInfo:
        """"""
    @overload
    def GetConstructor(self, types: Array[Type]) -> ConstructorInfo:
        """"""
    @overload
    def GetConstructors(self) -> Array[ConstructorInfo]:
        """"""
    @overload
    def GetConstructors(self, bindingAttr: BindingFlags) -> Array[ConstructorInfo]:
        """"""
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """"""
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """"""
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]:
        """"""
    def GetDeclaredEvent(self, name: str) -> EventInfo:
        """"""
    def GetDeclaredField(self, name: str) -> FieldInfo:
        """"""
    def GetDeclaredMethod(self, name: str) -> MethodInfo:
        """"""
    def GetDeclaredMethods(self, name: str) -> IEnumerable[MethodInfo]:
        """"""
    def GetDeclaredNestedType(self, name: str) -> TypeInfo:
        """"""
    def GetDeclaredProperty(self, name: str) -> PropertyInfo:
        """"""
    def GetDefaultMembers(self) -> Array[MemberInfo]:
        """"""
    def GetElementType(self) -> Type:
        """"""
    def GetEnumName(self, value: object) -> str:
        """"""
    def GetEnumNames(self) -> Array[str]:
        """"""
    def GetEnumUnderlyingType(self) -> Type:
        """"""
    def GetEnumValues(self) -> Array:
        """"""
    @overload
    def GetEvent(self, name: str) -> EventInfo:
        """"""
    @overload
    def GetEvent(self, name: str, bindingAttr: BindingFlags) -> EventInfo:
        """"""
    @overload
    def GetEvents(self) -> Array[EventInfo]:
        """"""
    @overload
    def GetEvents(self, bindingAttr: BindingFlags) -> Array[EventInfo]:
        """"""
    @overload
    def GetField(self, name: str) -> FieldInfo:
        """"""
    @overload
    def GetField(self, name: str, bindingAttr: BindingFlags) -> FieldInfo:
        """"""
    @overload
    def GetFields(self) -> Array[FieldInfo]:
        """"""
    @overload
    def GetFields(self, bindingAttr: BindingFlags) -> Array[FieldInfo]:
        """"""
    def GetGenericArguments(self) -> Array[Type]:
        """"""
    def GetGenericParameterConstraints(self) -> Array[Type]:
        """"""
    def GetGenericTypeDefinition(self) -> Type:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    @overload
    def GetInterface(self, name: str) -> Type:
        """"""
    @overload
    def GetInterface(self, name: str, ignoreCase: bool) -> Type:
        """"""
    def GetInterfaceMap(self, interfaceType: Type) -> InterfaceMapping:
        """"""
    def GetInterfaces(self) -> Array[Type]:
        """"""
    @overload
    def GetMember(self, name: str) -> Array[MemberInfo]:
        """"""
    @overload
    def GetMember(self, name: str, bindingAttr: BindingFlags) -> Array[MemberInfo]:
        """"""
    @overload
    def GetMember(
        self, name: str, type: MemberTypes, bindingAttr: BindingFlags
    ) -> Array[MemberInfo]:
        """"""
    @overload
    def GetMembers(self) -> Array[MemberInfo]:
        """"""
    @overload
    def GetMembers(self, bindingAttr: BindingFlags) -> Array[MemberInfo]:
        """"""
    @overload
    def GetMethod(self, name: str) -> MethodInfo:
        """"""
    @overload
    def GetMethod(self, name: str, bindingAttr: BindingFlags) -> MethodInfo:
        """"""
    @overload
    def GetMethod(
        self,
        name: str,
        bindingAttr: BindingFlags,
        binder: Binder,
        callConvention: CallingConventions,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> MethodInfo:
        """"""
    @overload
    def GetMethod(
        self,
        name: str,
        bindingAttr: BindingFlags,
        binder: Binder,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> MethodInfo:
        """"""
    @overload
    def GetMethod(self, name: str, types: Array[Type]) -> MethodInfo:
        """"""
    @overload
    def GetMethod(
        self, name: str, types: Array[Type], modifiers: Array[ParameterModifier]
    ) -> MethodInfo:
        """"""
    @overload
    def GetMethods(self) -> Array[MethodInfo]:
        """"""
    @overload
    def GetMethods(self, bindingAttr: BindingFlags) -> Array[MethodInfo]:
        """"""
    @overload
    def GetNestedType(self, name: str) -> Type:
        """"""
    @overload
    def GetNestedType(self, name: str, bindingAttr: BindingFlags) -> Type:
        """"""
    @overload
    def GetNestedTypes(self) -> Array[Type]:
        """"""
    @overload
    def GetNestedTypes(self, bindingAttr: BindingFlags) -> Array[Type]:
        """"""
    @overload
    def GetProperties(self) -> Array[PropertyInfo]:
        """"""
    @overload
    def GetProperties(self, bindingAttr: BindingFlags) -> Array[PropertyInfo]:
        """"""
    @overload
    def GetProperty(self, name: str) -> PropertyInfo:
        """"""
    @overload
    def GetProperty(self, name: str, bindingAttr: BindingFlags) -> PropertyInfo:
        """"""
    @overload
    def GetProperty(
        self,
        name: str,
        bindingAttr: BindingFlags,
        binder: Binder,
        returnType: Type,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> PropertyInfo:
        """"""
    @overload
    def GetProperty(self, name: str, types: Array[Type]) -> PropertyInfo:
        """"""
    @overload
    def GetProperty(self, name: str, returnType: Type) -> PropertyInfo:
        """"""
    @overload
    def GetProperty(self, name: str, returnType: Type, types: Array[Type]) -> PropertyInfo:
        """"""
    @overload
    def GetProperty(
        self, name: str, returnType: Type, types: Array[Type], modifiers: Array[ParameterModifier]
    ) -> PropertyInfo:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def GetTypeInfo(self) -> TypeInfo:
        """"""
    @overload
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
    @overload
    def InvokeMember(
        self,
        name: str,
        invokeAttr: BindingFlags,
        binder: Binder,
        target: object,
        args: Array[object],
    ) -> object:
        """"""
    @overload
    def InvokeMember(
        self,
        name: str,
        invokeAttr: BindingFlags,
        binder: Binder,
        target: object,
        args: Array[object],
        culture: CultureInfo,
    ) -> object:
        """"""
    @overload
    def InvokeMember(
        self,
        name: str,
        invokeAttr: BindingFlags,
        binder: Binder,
        target: object,
        args: Array[object],
        modifiers: Array[ParameterModifier],
        culture: CultureInfo,
        namedParameters: Array[str],
    ) -> object:
        """"""
    @overload
    def IsAssignableFrom(self, typeInfo: TypeInfo) -> bool:
        """"""
    @overload
    def IsAssignableFrom(self, c: Type) -> bool:
        """"""
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """"""
    def IsEnumDefined(self, value: object) -> bool:
        """"""
    def IsEquivalentTo(self, other: Type) -> bool:
        """"""
    def IsInstanceOfType(self, o: object) -> bool:
        """"""
    def IsSubclassOf(self, c: Type) -> bool:
        """"""
    @overload
    def MakeArrayType(self) -> Type:
        """"""
    @overload
    def MakeArrayType(self, rank: int) -> Type:
        """"""
    def MakeByRefType(self) -> Type:
        """"""
    def MakeGenericType(self, inst: Array[Type]) -> Type:
        """"""
    def MakePointerType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class TypeKind(Enum):
    """"""

    IsArray: TypeKind = ...
    """"""
    IsPointer: TypeKind = ...
    """"""
    IsByRef: TypeKind = ...
    """"""

class TypeNameBuilder(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class TypeToken(ValueType):
    """"""

    Empty: ClassVar[TypeToken]
    """"""
    @property
    def Token(self) -> int:
        """"""
    @overload
    def Equals(self, obj: TypeToken) -> bool:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def op_Equality(cls, a: TypeToken, b: TypeToken) -> bool:
        """"""
    @classmethod
    def op_Inequality(cls, a: TypeToken, b: TypeToken) -> bool:
        """"""
    def __eq__(self, other: TypeToken) -> bool:
        """"""
    def __ne__(self, other: TypeToken) -> bool:
        """"""

class UnmanagedMarshal(Object):
    """"""
    @property
    def BaseType(self) -> UnmanagedType:
        """"""
    @property
    def ElementCount(self) -> int:
        """"""
    @property
    def GetUnmanagedType(self) -> UnmanagedType:
        """"""
    @property
    def IIDGuid(self) -> Guid:
        """"""
    @classmethod
    def DefineByValArray(cls, elemCount: int) -> UnmanagedMarshal:
        """"""
    @classmethod
    def DefineByValTStr(cls, elemCount: int) -> UnmanagedMarshal:
        """"""
    @classmethod
    def DefineLPArray(cls, elemType: UnmanagedType) -> UnmanagedMarshal:
        """"""
    @classmethod
    def DefineSafeArray(cls, elemType: UnmanagedType) -> UnmanagedMarshal:
        """"""
    @classmethod
    def DefineUnmanagedMarshal(cls, unmanagedType: UnmanagedType) -> UnmanagedMarshal:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class VarArgMethod(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class __ExceptionInfo(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class __FixupData(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
