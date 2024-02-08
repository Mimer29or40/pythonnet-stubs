from __future__ import annotations

from typing import ClassVar
from typing import Final
from typing import Generic
from typing import Tuple
from typing import TypeVar
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

T = TypeVar("T")

class EventType(Generic[T]):
    def __iadd__(self, other: T): ...
    def __isub__(self, other: T): ...

class AssemblyBuilder(
    Assembly, ICustomAttributeProvider, _Assembly, _AssemblyBuilder, ISerializable, IEvidenceFactory
):
    """"""

    @property
    def CodeBase(self) -> str:
        """

        :return:
        """
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
        """

        :return:
        """
    @property
    def DefinedTypes(self) -> IEnumerable[TypeInfo]:
        """

        :return:
        """
    @property
    def EntryPoint(self) -> MethodInfo:
        """

        :return:
        """
    @property
    def EscapedCodeBase(self) -> str:
        """

        :return:
        """
    @property
    def Evidence(self) -> Evidence:
        """

        :return:
        """
    @property
    def Evidence(self) -> Evidence:
        """

        :return:
        """
    @property
    def ExportedTypes(self) -> IEnumerable[Type]:
        """

        :return:
        """
    @property
    def FullName(self) -> str:
        """

        :return:
        """
    @property
    def GlobalAssemblyCache(self) -> bool:
        """

        :return:
        """
    @property
    def HostContext(self) -> int:
        """

        :return:
        """
    @property
    def ImageRuntimeVersion(self) -> str:
        """

        :return:
        """
    @property
    def IsDynamic(self) -> bool:
        """

        :return:
        """
    @property
    def IsFullyTrusted(self) -> bool:
        """

        :return:
        """
    @property
    def Location(self) -> str:
        """

        :return:
        """
    @property
    def ManifestModule(self) -> Module:
        """

        :return:
        """
    @property
    def Modules(self) -> IEnumerable[Module]:
        """

        :return:
        """
    @property
    def PermissionSet(self) -> PermissionSet:
        """

        :return:
        """
    @property
    def ReflectionOnly(self) -> bool:
        """

        :return:
        """
    @property
    def SecurityRuleSet(self) -> SecurityRuleSet:
        """

        :return:
        """
    @overload
    def AddResourceFile(self, name: str, fileName: str) -> None:
        """

        :param name:
        :param fileName:
        """
    @overload
    def AddResourceFile(self, name: str, fileName: str, attribute: ResourceAttributes) -> None:
        """

        :param name:
        :param fileName:
        :param attribute:
        """
    @overload
    def CreateInstance(self, typeName: str) -> object:
        """

        :param typeName:
        :return:
        """
    @overload
    def CreateInstance(self, typeName: str, ignoreCase: bool) -> object:
        """

        :param typeName:
        :param ignoreCase:
        :return:
        """
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
        """

        :param typeName:
        :param ignoreCase:
        :param bindingAttr:
        :param binder:
        :param args:
        :param culture:
        :param activationAttributes:
        :return:
        """
    @classmethod
    @overload
    def DefineDynamicAssembly(
        cls, name: AssemblyName, access: AssemblyBuilderAccess
    ) -> AssemblyBuilder:
        """

        :param name:
        :param access:
        :return:
        """
    @classmethod
    @overload
    def DefineDynamicAssembly(
        cls,
        name: AssemblyName,
        access: AssemblyBuilderAccess,
        assemblyAttributes: IEnumerable[CustomAttributeBuilder],
    ) -> AssemblyBuilder:
        """

        :param name:
        :param access:
        :param assemblyAttributes:
        :return:
        """
    @overload
    def DefineDynamicModule(self, name: str) -> ModuleBuilder:
        """

        :param name:
        :return:
        """
    @overload
    def DefineDynamicModule(self, name: str, emitSymbolInfo: bool) -> ModuleBuilder:
        """

        :param name:
        :param emitSymbolInfo:
        :return:
        """
    @overload
    def DefineDynamicModule(self, name: str, fileName: str) -> ModuleBuilder:
        """

        :param name:
        :param fileName:
        :return:
        """
    @overload
    def DefineDynamicModule(self, name: str, fileName: str, emitSymbolInfo: bool) -> ModuleBuilder:
        """

        :param name:
        :param fileName:
        :param emitSymbolInfo:
        :return:
        """
    @overload
    def DefineResource(self, name: str, description: str, fileName: str) -> IResourceWriter:
        """

        :param name:
        :param description:
        :param fileName:
        :return:
        """
    @overload
    def DefineResource(
        self, name: str, description: str, fileName: str, attribute: ResourceAttributes
    ) -> IResourceWriter:
        """

        :param name:
        :param description:
        :param fileName:
        :param attribute:
        :return:
        """
    @overload
    def DefineUnmanagedResource(self, resource: Array[int]) -> None:
        """

        :param resource:
        """
    @overload
    def DefineUnmanagedResource(self, resourceFileName: str) -> None:
        """

        :param resourceFileName:
        """
    @overload
    def DefineVersionInfoResource(self) -> None:
        """"""
    @overload
    def DefineVersionInfoResource(
        self, product: str, productVersion: str, company: str, copyright: str, trademark: str
    ) -> None:
        """

        :param product:
        :param productVersion:
        :param company:
        :param copyright:
        :param trademark:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def Equals(self, other: object) -> bool:
        """

        :param other:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]:
        """

        :return:
        """
    def GetDynamicModule(self, name: str) -> ModuleBuilder:
        """

        :param name:
        :return:
        """
    def GetExportedTypes(self) -> Array[Type]:
        """

        :return:
        """
    def GetFile(self, name: str) -> FileStream:
        """

        :param name:
        :return:
        """
    @overload
    def GetFiles(self) -> Array[FileStream]:
        """

        :return:
        """
    @overload
    def GetFiles(self, getResourceModules: bool) -> Array[FileStream]:
        """

        :param getResourceModules:
        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    @overload
    def GetLoadedModules(self) -> Array[Module]:
        """

        :return:
        """
    @overload
    def GetLoadedModules(self, getResourceModules: bool) -> Array[Module]:
        """

        :param getResourceModules:
        :return:
        """
    def GetManifestResourceInfo(self, resourceName: str) -> ManifestResourceInfo:
        """

        :param resourceName:
        :return:
        """
    def GetManifestResourceNames(self) -> Array[str]:
        """

        :return:
        """
    @overload
    def GetManifestResourceStream(self, name: str) -> Stream:
        """

        :param name:
        :return:
        """
    @overload
    def GetManifestResourceStream(self, type: Type, name: str) -> Stream:
        """

        :param type:
        :param name:
        :return:
        """
    def GetModule(self, name: str) -> Module:
        """

        :param name:
        :return:
        """
    @overload
    def GetModules(self) -> Array[Module]:
        """

        :return:
        """
    @overload
    def GetModules(self, getResourceModules: bool) -> Array[Module]:
        """

        :param getResourceModules:
        :return:
        """
    @overload
    def GetName(self) -> AssemblyName:
        """

        :return:
        """
    @overload
    def GetName(self, copiedName: bool) -> AssemblyName:
        """

        :param copiedName:
        :return:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    def GetReferencedAssemblies(self) -> Array[AssemblyName]:
        """

        :return:
        """
    @overload
    def GetSatelliteAssembly(self, culture: CultureInfo) -> Assembly:
        """

        :param culture:
        :return:
        """
    @overload
    def GetSatelliteAssembly(self, culture: CultureInfo, version: Version) -> Assembly:
        """

        :param culture:
        :param version:
        :return:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetType(self, name: str) -> Type:
        """

        :param name:
        :return:
        """
    @overload
    def GetType(self, name: str, throwOnError: bool) -> Type:
        """

        :param name:
        :param throwOnError:
        :return:
        """
    @overload
    def GetType(self, name: str, throwOnError: bool, ignoreCase: bool) -> Type:
        """

        :param name:
        :param throwOnError:
        :param ignoreCase:
        :return:
        """
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    def GetTypes(self) -> Array[Type]:
        """

        :return:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def LoadModule(self, moduleName: str, rawModule: Array[int]) -> Module:
        """

        :param moduleName:
        :param rawModule:
        :return:
        """
    @overload
    def LoadModule(
        self, moduleName: str, rawModule: Array[int], rawSymbolStore: Array[int]
    ) -> Module:
        """

        :param moduleName:
        :param rawModule:
        :param rawSymbolStore:
        :return:
        """
    @overload
    def Save(self, assemblyFileName: str) -> None:
        """

        :param assemblyFileName:
        """
    @overload
    def Save(
        self,
        assemblyFileName: str,
        portableExecutableKind: PortableExecutableKinds,
        imageFileMachine: ImageFileMachine,
    ) -> None:
        """

        :param assemblyFileName:
        :param portableExecutableKind:
        :param imageFileMachine:
        """
    @overload
    def SetCustomAttribute(self, customBuilder: CustomAttributeBuilder) -> None:
        """

        :param customBuilder:
        """
    @overload
    def SetCustomAttribute(self, con: ConstructorInfo, binaryAttribute: Array[int]) -> None:
        """

        :param con:
        :param binaryAttribute:
        """
    @overload
    def SetEntryPoint(self, entryMethod: MethodInfo) -> None:
        """

        :param entryMethod:
        """
    @overload
    def SetEntryPoint(self, entryMethod: MethodInfo, fileKind: PEFileKinds) -> None:
        """

        :param entryMethod:
        :param fileKind:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """
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
        """

        :return:
        """
    @property
    def Attributes(self) -> MethodAttributes:
        """

        :return:
        """
    @property
    def CallingConvention(self) -> CallingConventions:
        """

        :return:
        """
    @property
    def CallingConvention(self) -> CallingConventions:
        """

        :return:
        """
    @property
    def ContainsGenericParameters(self) -> bool:
        """

        :return:
        """
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
        """

        :return:
        """
    @property
    def DeclaringType(self) -> Type:
        """

        :return:
        """
    @property
    def DeclaringType(self) -> Type:
        """

        :return:
        """
    @property
    def DeclaringType(self) -> Type:
        """

        :return:
        """
    @property
    def InitLocals(self) -> bool:
        """

        :return:
        """
    @InitLocals.setter
    def InitLocals(self, value: bool) -> None: ...
    @property
    def IsAbstract(self) -> bool:
        """

        :return:
        """
    @property
    def IsAbstract(self) -> bool:
        """

        :return:
        """
    @property
    def IsAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsConstructor(self) -> bool:
        """

        :return:
        """
    @property
    def IsConstructor(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamily(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamily(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamilyAndAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamilyAndAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamilyOrAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamilyOrAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsFinal(self) -> bool:
        """

        :return:
        """
    @property
    def IsFinal(self) -> bool:
        """

        :return:
        """
    @property
    def IsGenericMethod(self) -> bool:
        """

        :return:
        """
    @property
    def IsGenericMethodDefinition(self) -> bool:
        """

        :return:
        """
    @property
    def IsHideBySig(self) -> bool:
        """

        :return:
        """
    @property
    def IsHideBySig(self) -> bool:
        """

        :return:
        """
    @property
    def IsPrivate(self) -> bool:
        """

        :return:
        """
    @property
    def IsPrivate(self) -> bool:
        """

        :return:
        """
    @property
    def IsPublic(self) -> bool:
        """

        :return:
        """
    @property
    def IsPublic(self) -> bool:
        """

        :return:
        """
    @property
    def IsSecurityCritical(self) -> bool:
        """

        :return:
        """
    @property
    def IsSecuritySafeCritical(self) -> bool:
        """

        :return:
        """
    @property
    def IsSecurityTransparent(self) -> bool:
        """

        :return:
        """
    @property
    def IsSpecialName(self) -> bool:
        """

        :return:
        """
    @property
    def IsSpecialName(self) -> bool:
        """

        :return:
        """
    @property
    def IsStatic(self) -> bool:
        """

        :return:
        """
    @property
    def IsStatic(self) -> bool:
        """

        :return:
        """
    @property
    def IsVirtual(self) -> bool:
        """

        :return:
        """
    @property
    def IsVirtual(self) -> bool:
        """

        :return:
        """
    @property
    def MemberType(self) -> MemberTypes:
        """

        :return:
        """
    @property
    def MemberType(self) -> MemberTypes:
        """

        :return:
        """
    @property
    def MemberType(self) -> MemberTypes:
        """

        :return:
        """
    @property
    def MetadataToken(self) -> int:
        """

        :return:
        """
    @property
    def MethodHandle(self) -> RuntimeMethodHandle:
        """

        :return:
        """
    @property
    def MethodHandle(self) -> RuntimeMethodHandle:
        """

        :return:
        """
    @property
    def MethodImplementationFlags(self) -> MethodImplAttributes:
        """

        :return:
        """
    @property
    def Module(self) -> Module:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def ReflectedType(self) -> Type:
        """

        :return:
        """
    @property
    def ReflectedType(self) -> Type:
        """

        :return:
        """
    @property
    def ReflectedType(self) -> Type:
        """

        :return:
        """
    @property
    def ReturnType(self) -> Type:
        """

        :return:
        """
    @property
    def Signature(self) -> str:
        """

        :return:
        """
    def AddDeclarativeSecurity(self, action: SecurityAction, pset: PermissionSet) -> None:
        """

        :param action:
        :param pset:
        """
    def DefineParameter(
        self, iSequence: int, attributes: ParameterAttributes, strParamName: str
    ) -> ParameterBuilder:
        """

        :param iSequence:
        :param attributes:
        :param strParamName:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def Equals(self, other: object) -> bool:
        """

        :param other:
        :return:
        """
    @overload
    def Equals(self, other: object) -> bool:
        """

        :param other:
        :return:
        """
    @overload
    def Equals(self, other: object) -> bool:
        """

        :param other:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]:
        """

        :return:
        """
    def GetGenericArguments(self) -> Array[Type]:
        """

        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    @overload
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    @overload
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    @overload
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    @overload
    def GetILGenerator(self) -> ILGenerator:
        """

        :return:
        """
    @overload
    def GetILGenerator(self, streamSize: int) -> ILGenerator:
        """

        :param streamSize:
        :return:
        """
    def GetMethodBody(self) -> MethodBody:
        """

        :return:
        """
    @overload
    def GetMethodImplementationFlags(self) -> MethodImplAttributes:
        """

        :return:
        """
    @overload
    def GetMethodImplementationFlags(self) -> MethodImplAttributes:
        """

        :return:
        """
    def GetModule(self) -> Module:
        """

        :return:
        """
    @overload
    def GetParameters(self) -> Array[ParameterInfo]:
        """

        :return:
        """
    @overload
    def GetParameters(self) -> Array[ParameterInfo]:
        """

        :return:
        """
    def GetToken(self) -> MethodToken:
        """

        :return:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    @overload
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    @overload
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    @overload
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    @overload
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    @overload
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    @overload
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    @overload
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    @overload
    def Invoke(self, parameters: Array[object]) -> object:
        """

        :param parameters:
        :return:
        """
    @overload
    def Invoke(self, obj: object, parameters: Array[object]) -> object:
        """

        :param obj:
        :param parameters:
        :return:
        """
    @overload
    def Invoke(
        self,
        invokeAttr: BindingFlags,
        binder: Binder,
        parameters: Array[object],
        culture: CultureInfo,
    ) -> object:
        """

        :param invokeAttr:
        :param binder:
        :param parameters:
        :param culture:
        :return:
        """
    @overload
    def Invoke(
        self,
        obj: object,
        invokeAttr: BindingFlags,
        binder: Binder,
        parameters: Array[object],
        culture: CultureInfo,
    ) -> object:
        """

        :param obj:
        :param invokeAttr:
        :param binder:
        :param parameters:
        :param culture:
        :return:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def Invoke_2(
        self,
        obj: object,
        invokeAttr: BindingFlags,
        binder: Binder,
        parameters: Array[object],
        culture: CultureInfo,
    ) -> object:
        """

        :param obj:
        :param invokeAttr:
        :param binder:
        :param parameters:
        :param culture:
        :return:
        """
    def Invoke_3(self, obj: object, parameters: Array[object]) -> object:
        """

        :param obj:
        :param parameters:
        :return:
        """
    def Invoke_4(
        self,
        invokeAttr: BindingFlags,
        binder: Binder,
        parameters: Array[object],
        culture: CultureInfo,
    ) -> object:
        """

        :param invokeAttr:
        :param binder:
        :param parameters:
        :param culture:
        :return:
        """
    def Invoke_5(self, parameters: Array[object]) -> object:
        """

        :param parameters:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def SetCustomAttribute(self, customBuilder: CustomAttributeBuilder) -> None:
        """

        :param customBuilder:
        """
    @overload
    def SetCustomAttribute(self, con: ConstructorInfo, binaryAttribute: Array[int]) -> None:
        """

        :param con:
        :param binaryAttribute:
        """
    def SetImplementationFlags(self, attributes: MethodImplAttributes) -> None:
        """

        :param attributes:
        """
    def SetMethodBody(
        self,
        il: Array[int],
        maxStack: int,
        localSignature: Array[int],
        exceptionHandlers: IEnumerable[ExceptionHandler],
        tokenFixups: IEnumerable[int],
    ) -> None:
        """

        :param il:
        :param maxStack:
        :param localSignature:
        :param exceptionHandlers:
        :param tokenFixups:
        """
    def SetSymCustomAttribute(self, name: str, data: Array[int]) -> None:
        """

        :param name:
        :param data:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """

class ConstructorOnTypeBuilderInstantiation(
    ConstructorInfo, ICustomAttributeProvider, _ConstructorInfo, _MemberInfo, _MethodBase
):
    """"""

    @property
    def Attributes(self) -> MethodAttributes:
        """

        :return:
        """
    @property
    def Attributes(self) -> MethodAttributes:
        """

        :return:
        """
    @property
    def CallingConvention(self) -> CallingConventions:
        """

        :return:
        """
    @property
    def CallingConvention(self) -> CallingConventions:
        """

        :return:
        """
    @property
    def ContainsGenericParameters(self) -> bool:
        """

        :return:
        """
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
        """

        :return:
        """
    @property
    def DeclaringType(self) -> Type:
        """

        :return:
        """
    @property
    def DeclaringType(self) -> Type:
        """

        :return:
        """
    @property
    def DeclaringType(self) -> Type:
        """

        :return:
        """
    @property
    def IsAbstract(self) -> bool:
        """

        :return:
        """
    @property
    def IsAbstract(self) -> bool:
        """

        :return:
        """
    @property
    def IsAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsConstructor(self) -> bool:
        """

        :return:
        """
    @property
    def IsConstructor(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamily(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamily(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamilyAndAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamilyAndAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamilyOrAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamilyOrAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsFinal(self) -> bool:
        """

        :return:
        """
    @property
    def IsFinal(self) -> bool:
        """

        :return:
        """
    @property
    def IsGenericMethod(self) -> bool:
        """

        :return:
        """
    @property
    def IsGenericMethodDefinition(self) -> bool:
        """

        :return:
        """
    @property
    def IsHideBySig(self) -> bool:
        """

        :return:
        """
    @property
    def IsHideBySig(self) -> bool:
        """

        :return:
        """
    @property
    def IsPrivate(self) -> bool:
        """

        :return:
        """
    @property
    def IsPrivate(self) -> bool:
        """

        :return:
        """
    @property
    def IsPublic(self) -> bool:
        """

        :return:
        """
    @property
    def IsPublic(self) -> bool:
        """

        :return:
        """
    @property
    def IsSecurityCritical(self) -> bool:
        """

        :return:
        """
    @property
    def IsSecuritySafeCritical(self) -> bool:
        """

        :return:
        """
    @property
    def IsSecurityTransparent(self) -> bool:
        """

        :return:
        """
    @property
    def IsSpecialName(self) -> bool:
        """

        :return:
        """
    @property
    def IsSpecialName(self) -> bool:
        """

        :return:
        """
    @property
    def IsStatic(self) -> bool:
        """

        :return:
        """
    @property
    def IsStatic(self) -> bool:
        """

        :return:
        """
    @property
    def IsVirtual(self) -> bool:
        """

        :return:
        """
    @property
    def IsVirtual(self) -> bool:
        """

        :return:
        """
    @property
    def MemberType(self) -> MemberTypes:
        """

        :return:
        """
    @property
    def MemberType(self) -> MemberTypes:
        """

        :return:
        """
    @property
    def MemberType(self) -> MemberTypes:
        """

        :return:
        """
    @property
    def MetadataToken(self) -> int:
        """

        :return:
        """
    @property
    def MethodHandle(self) -> RuntimeMethodHandle:
        """

        :return:
        """
    @property
    def MethodHandle(self) -> RuntimeMethodHandle:
        """

        :return:
        """
    @property
    def MethodImplementationFlags(self) -> MethodImplAttributes:
        """

        :return:
        """
    @property
    def Module(self) -> Module:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def ReflectedType(self) -> Type:
        """

        :return:
        """
    @property
    def ReflectedType(self) -> Type:
        """

        :return:
        """
    @property
    def ReflectedType(self) -> Type:
        """

        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def Equals(self, other: object) -> bool:
        """

        :param other:
        :return:
        """
    @overload
    def Equals(self, other: object) -> bool:
        """

        :param other:
        :return:
        """
    @overload
    def Equals(self, other: object) -> bool:
        """

        :param other:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]:
        """

        :return:
        """
    def GetGenericArguments(self) -> Array[Type]:
        """

        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    @overload
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    @overload
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetMethodBody(self) -> MethodBody:
        """

        :return:
        """
    @overload
    def GetMethodImplementationFlags(self) -> MethodImplAttributes:
        """

        :return:
        """
    @overload
    def GetMethodImplementationFlags(self) -> MethodImplAttributes:
        """

        :return:
        """
    @overload
    def GetParameters(self) -> Array[ParameterInfo]:
        """

        :return:
        """
    @overload
    def GetParameters(self) -> Array[ParameterInfo]:
        """

        :return:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    @overload
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    @overload
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    @overload
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    @overload
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    @overload
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    @overload
    def Invoke(self, parameters: Array[object]) -> object:
        """

        :param parameters:
        :return:
        """
    @overload
    def Invoke(self, obj: object, parameters: Array[object]) -> object:
        """

        :param obj:
        :param parameters:
        :return:
        """
    @overload
    def Invoke(
        self,
        invokeAttr: BindingFlags,
        binder: Binder,
        parameters: Array[object],
        culture: CultureInfo,
    ) -> object:
        """

        :param invokeAttr:
        :param binder:
        :param parameters:
        :param culture:
        :return:
        """
    @overload
    def Invoke(
        self,
        obj: object,
        invokeAttr: BindingFlags,
        binder: Binder,
        parameters: Array[object],
        culture: CultureInfo,
    ) -> object:
        """

        :param obj:
        :param invokeAttr:
        :param binder:
        :param parameters:
        :param culture:
        :return:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def Invoke_2(
        self,
        obj: object,
        invokeAttr: BindingFlags,
        binder: Binder,
        parameters: Array[object],
        culture: CultureInfo,
    ) -> object:
        """

        :param obj:
        :param invokeAttr:
        :param binder:
        :param parameters:
        :param culture:
        :return:
        """
    def Invoke_3(self, obj: object, parameters: Array[object]) -> object:
        """

        :param obj:
        :param parameters:
        :return:
        """
    def Invoke_4(
        self,
        invokeAttr: BindingFlags,
        binder: Binder,
        parameters: Array[object],
        culture: CultureInfo,
    ) -> object:
        """

        :param invokeAttr:
        :param binder:
        :param parameters:
        :param culture:
        :return:
        """
    def Invoke_5(self, parameters: Array[object]) -> object:
        """

        :param parameters:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """

class CustomAttributeBuilder(Object, _CustomAttributeBuilder):
    """"""

    @overload
    def __init__(self, con: ConstructorInfo, constructorArgs: Array[object]):
        """

        :param con:
        :param constructorArgs:
        """
    @overload
    def __init__(
        self,
        con: ConstructorInfo,
        constructorArgs: Array[object],
        namedFields: Array[FieldInfo],
        fieldValues: Array[object],
    ):
        """

        :param con:
        :param constructorArgs:
        :param namedFields:
        :param fieldValues:
        """
    @overload
    def __init__(
        self,
        con: ConstructorInfo,
        constructorArgs: Array[object],
        namedProperties: Array[PropertyInfo],
        propertyValues: Array[object],
    ):
        """

        :param con:
        :param constructorArgs:
        :param namedProperties:
        :param propertyValues:
        """
    @overload
    def __init__(
        self,
        con: ConstructorInfo,
        constructorArgs: Array[object],
        namedProperties: Array[PropertyInfo],
        propertyValues: Array[object],
        namedFields: Array[FieldInfo],
        fieldValues: Array[object],
    ):
        """

        :param con:
        :param constructorArgs:
        :param namedProperties:
        :param propertyValues:
        :param namedFields:
        :param fieldValues:
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
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def ToString(self) -> str:
        """

        :return:
        """

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
        """

        :return:
        """
    def BeginCatchBlock(self, exceptionType: Type) -> None:
        """

        :param exceptionType:
        """
    def BeginExceptFilterBlock(self) -> None:
        """"""
    def BeginExceptionBlock(self) -> Label:
        """

        :return:
        """
    def BeginFaultBlock(self) -> None:
        """"""
    def BeginFinallyBlock(self) -> None:
        """"""
    def BeginScope(self) -> None:
        """"""
    @overload
    def DeclareLocal(self, localType: Type) -> LocalBuilder:
        """

        :param localType:
        :return:
        """
    @overload
    def DeclareLocal(self, localType: Type, pinned: bool) -> LocalBuilder:
        """

        :param localType:
        :param pinned:
        :return:
        """
    def DefineLabel(self) -> Label:
        """

        :return:
        """
    @overload
    def Emit(self, opcode: OpCode) -> None:
        """

        :param opcode:
        """
    @overload
    def Emit(self, opcode: OpCode, label: Label) -> None:
        """

        :param opcode:
        :param label:
        """
    @overload
    def Emit(self, opcode: OpCode, local: LocalBuilder) -> None:
        """

        :param opcode:
        :param local:
        """
    @overload
    def Emit(self, opcode: OpCode, signature: SignatureHelper) -> None:
        """

        :param opcode:
        :param signature:
        """
    @overload
    def Emit(self, opcode: OpCode, con: ConstructorInfo) -> None:
        """

        :param opcode:
        :param con:
        """
    @overload
    def Emit(self, opcode: OpCode, field: FieldInfo) -> None:
        """

        :param opcode:
        :param field:
        """
    @overload
    def Emit(self, opcode: OpCode, meth: MethodInfo) -> None:
        """

        :param opcode:
        :param meth:
        """
    @overload
    def Emit(self, opcode: OpCode, labels: Array[Label]) -> None:
        """

        :param opcode:
        :param labels:
        """
    @overload
    def Emit(self, opcode: OpCode, arg: int) -> None:
        """

        :param opcode:
        :param arg:
        """
    @overload
    def Emit(self, opcode: OpCode, arg: float) -> None:
        """

        :param opcode:
        :param arg:
        """
    @overload
    def Emit(self, opcode: OpCode, arg: int) -> None:
        """

        :param opcode:
        :param arg:
        """
    @overload
    def Emit(self, opcode: OpCode, arg: int) -> None:
        """

        :param opcode:
        :param arg:
        """
    @overload
    def Emit(self, opcode: OpCode, arg: int) -> None:
        """

        :param opcode:
        :param arg:
        """
    @overload
    def Emit(self, opcode: OpCode, arg: int) -> None:
        """

        :param opcode:
        :param arg:
        """
    @overload
    def Emit(self, opcode: OpCode, arg: float) -> None:
        """

        :param opcode:
        :param arg:
        """
    @overload
    def Emit(self, opcode: OpCode, str: str) -> None:
        """

        :param opcode:
        :param str:
        """
    @overload
    def Emit(self, opcode: OpCode, cls: Type) -> None:
        """

        :param opcode:
        :param cls:
        """
    def EmitCall(
        self, opcode: OpCode, methodInfo: MethodInfo, optionalParameterTypes: Array[Type]
    ) -> None:
        """

        :param opcode:
        :param methodInfo:
        :param optionalParameterTypes:
        """
    @overload
    def EmitCalli(
        self,
        opcode: OpCode,
        unmanagedCallConv: CallingConvention,
        returnType: Type,
        parameterTypes: Array[Type],
    ) -> None:
        """

        :param opcode:
        :param unmanagedCallConv:
        :param returnType:
        :param parameterTypes:
        """
    @overload
    def EmitCalli(
        self,
        opcode: OpCode,
        callingConvention: CallingConventions,
        returnType: Type,
        parameterTypes: Array[Type],
        optionalParameterTypes: Array[Type],
    ) -> None:
        """

        :param opcode:
        :param callingConvention:
        :param returnType:
        :param parameterTypes:
        :param optionalParameterTypes:
        """
    @overload
    def EmitWriteLine(self, localBuilder: LocalBuilder) -> None:
        """

        :param localBuilder:
        """
    @overload
    def EmitWriteLine(self, fld: FieldInfo) -> None:
        """

        :param fld:
        """
    @overload
    def EmitWriteLine(self, value: str) -> None:
        """

        :param value:
        """
    def EndExceptionBlock(self) -> None:
        """"""
    def EndScope(self) -> None:
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
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def MarkLabel(self, loc: Label) -> None:
        """

        :param loc:
        """
    def MarkSequencePoint(
        self,
        document: ISymbolDocumentWriter,
        startLine: int,
        startColumn: int,
        endLine: int,
        endColumn: int,
    ) -> None:
        """

        :param document:
        :param startLine:
        :param startColumn:
        :param endLine:
        :param endColumn:
        """
    def ThrowException(self, excType: Type) -> None:
        """

        :param excType:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def UsingNamespace(self, usingNamespace: str) -> None:
        """

        :param usingNamespace:
        """

class DynamicILInfo(Object):
    """"""

    @property
    def DynamicMethod(self) -> DynamicMethod:
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
    @overload
    def GetTokenFor(self, method: DynamicMethod) -> int:
        """

        :param method:
        :return:
        """
    @overload
    def GetTokenFor(self, signature: Array[int]) -> int:
        """

        :param signature:
        :return:
        """
    @overload
    def GetTokenFor(self, field: RuntimeFieldHandle) -> int:
        """

        :param field:
        :return:
        """
    @overload
    def GetTokenFor(self, method: RuntimeMethodHandle) -> int:
        """

        :param method:
        :return:
        """
    @overload
    def GetTokenFor(self, type: RuntimeTypeHandle) -> int:
        """

        :param type:
        :return:
        """
    @overload
    def GetTokenFor(self, literal: str) -> int:
        """

        :param literal:
        :return:
        """
    @overload
    def GetTokenFor(self, field: RuntimeFieldHandle, contextType: RuntimeTypeHandle) -> int:
        """

        :param field:
        :param contextType:
        :return:
        """
    @overload
    def GetTokenFor(self, method: RuntimeMethodHandle, contextType: RuntimeTypeHandle) -> int:
        """

        :param method:
        :param contextType:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def SetCode(self, code: Array[int], maxStackSize: int) -> None:
        """

        :param code:
        :param maxStackSize:
        """
    @overload
    def SetCode(self, code: int, codeSize: int, maxStackSize: int) -> None:
        """

        :param code:
        :param codeSize:
        :param maxStackSize:
        """
    @overload
    def SetExceptions(self, exceptions: Array[int]) -> None:
        """

        :param exceptions:
        """
    @overload
    def SetExceptions(self, exceptions: int, exceptionsSize: int) -> None:
        """

        :param exceptions:
        :param exceptionsSize:
        """
    @overload
    def SetLocalSignature(self, localSignature: Array[int]) -> None:
        """

        :param localSignature:
        """
    @overload
    def SetLocalSignature(self, localSignature: int, signatureSize: int) -> None:
        """

        :param localSignature:
        :param signatureSize:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class DynamicMethod(MethodInfo, ICustomAttributeProvider, _MemberInfo, _MethodBase, _MethodInfo):
    """"""

    @overload
    def __init__(self, name: str, returnType: Type, parameterTypes: Array[Type]):
        """

        :param name:
        :param returnType:
        :param parameterTypes:
        """
    @overload
    def __init__(self, name: str, returnType: Type, parameterTypes: Array[Type], m: Module):
        """

        :param name:
        :param returnType:
        :param parameterTypes:
        :param m:
        """
    @overload
    def __init__(
        self,
        name: str,
        returnType: Type,
        parameterTypes: Array[Type],
        restrictedSkipVisibility: bool,
    ):
        """

        :param name:
        :param returnType:
        :param parameterTypes:
        :param restrictedSkipVisibility:
        """
    @overload
    def __init__(self, name: str, returnType: Type, parameterTypes: Array[Type], owner: Type):
        """

        :param name:
        :param returnType:
        :param parameterTypes:
        :param owner:
        """
    @overload
    def __init__(
        self,
        name: str,
        returnType: Type,
        parameterTypes: Array[Type],
        m: Module,
        skipVisibility: bool,
    ):
        """

        :param name:
        :param returnType:
        :param parameterTypes:
        :param m:
        :param skipVisibility:
        """
    @overload
    def __init__(
        self,
        name: str,
        returnType: Type,
        parameterTypes: Array[Type],
        owner: Type,
        skipVisibility: bool,
    ):
        """

        :param name:
        :param returnType:
        :param parameterTypes:
        :param owner:
        :param skipVisibility:
        """
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
    ):
        """

        :param name:
        :param attributes:
        :param callingConvention:
        :param returnType:
        :param parameterTypes:
        :param m:
        :param skipVisibility:
        """
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
    ):
        """

        :param name:
        :param attributes:
        :param callingConvention:
        :param returnType:
        :param parameterTypes:
        :param owner:
        :param skipVisibility:
        """
    @property
    def Attributes(self) -> MethodAttributes:
        """

        :return:
        """
    @property
    def Attributes(self) -> MethodAttributes:
        """

        :return:
        """
    @property
    def CallingConvention(self) -> CallingConventions:
        """

        :return:
        """
    @property
    def CallingConvention(self) -> CallingConventions:
        """

        :return:
        """
    @property
    def ContainsGenericParameters(self) -> bool:
        """

        :return:
        """
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
        """

        :return:
        """
    @property
    def DeclaringType(self) -> Type:
        """

        :return:
        """
    @property
    def DeclaringType(self) -> Type:
        """

        :return:
        """
    @property
    def DeclaringType(self) -> Type:
        """

        :return:
        """
    @property
    def InitLocals(self) -> bool:
        """

        :return:
        """
    @InitLocals.setter
    def InitLocals(self, value: bool) -> None: ...
    @property
    def IsAbstract(self) -> bool:
        """

        :return:
        """
    @property
    def IsAbstract(self) -> bool:
        """

        :return:
        """
    @property
    def IsAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsConstructor(self) -> bool:
        """

        :return:
        """
    @property
    def IsConstructor(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamily(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamily(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamilyAndAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamilyAndAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamilyOrAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamilyOrAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsFinal(self) -> bool:
        """

        :return:
        """
    @property
    def IsFinal(self) -> bool:
        """

        :return:
        """
    @property
    def IsGenericMethod(self) -> bool:
        """

        :return:
        """
    @property
    def IsGenericMethodDefinition(self) -> bool:
        """

        :return:
        """
    @property
    def IsHideBySig(self) -> bool:
        """

        :return:
        """
    @property
    def IsHideBySig(self) -> bool:
        """

        :return:
        """
    @property
    def IsPrivate(self) -> bool:
        """

        :return:
        """
    @property
    def IsPrivate(self) -> bool:
        """

        :return:
        """
    @property
    def IsPublic(self) -> bool:
        """

        :return:
        """
    @property
    def IsPublic(self) -> bool:
        """

        :return:
        """
    @property
    def IsSecurityCritical(self) -> bool:
        """

        :return:
        """
    @property
    def IsSecuritySafeCritical(self) -> bool:
        """

        :return:
        """
    @property
    def IsSecurityTransparent(self) -> bool:
        """

        :return:
        """
    @property
    def IsSpecialName(self) -> bool:
        """

        :return:
        """
    @property
    def IsSpecialName(self) -> bool:
        """

        :return:
        """
    @property
    def IsStatic(self) -> bool:
        """

        :return:
        """
    @property
    def IsStatic(self) -> bool:
        """

        :return:
        """
    @property
    def IsVirtual(self) -> bool:
        """

        :return:
        """
    @property
    def IsVirtual(self) -> bool:
        """

        :return:
        """
    @property
    def MemberType(self) -> MemberTypes:
        """

        :return:
        """
    @property
    def MemberType(self) -> MemberTypes:
        """

        :return:
        """
    @property
    def MemberType(self) -> MemberTypes:
        """

        :return:
        """
    @property
    def MetadataToken(self) -> int:
        """

        :return:
        """
    @property
    def MethodHandle(self) -> RuntimeMethodHandle:
        """

        :return:
        """
    @property
    def MethodHandle(self) -> RuntimeMethodHandle:
        """

        :return:
        """
    @property
    def MethodImplementationFlags(self) -> MethodImplAttributes:
        """

        :return:
        """
    @property
    def Module(self) -> Module:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def ReflectedType(self) -> Type:
        """

        :return:
        """
    @property
    def ReflectedType(self) -> Type:
        """

        :return:
        """
    @property
    def ReflectedType(self) -> Type:
        """

        :return:
        """
    @property
    def ReturnParameter(self) -> ParameterInfo:
        """

        :return:
        """
    @property
    def ReturnType(self) -> Type:
        """

        :return:
        """
    @property
    def ReturnTypeCustomAttributes(self) -> ICustomAttributeProvider:
        """

        :return:
        """
    @overload
    def CreateDelegate(self, delegateType: Type) -> Delegate:
        """

        :param delegateType:
        :return:
        """
    @overload
    def CreateDelegate(self, delegateType: Type, target: object) -> Delegate:
        """

        :param delegateType:
        :param target:
        :return:
        """
    def DefineParameter(
        self, position: int, attributes: ParameterAttributes, parameterName: str
    ) -> ParameterBuilder:
        """

        :param position:
        :param attributes:
        :param parameterName:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def Equals(self, other: object) -> bool:
        """

        :param other:
        :return:
        """
    @overload
    def Equals(self, other: object) -> bool:
        """

        :param other:
        :return:
        """
    @overload
    def Equals(self, other: object) -> bool:
        """

        :param other:
        :return:
        """
    def GetBaseDefinition(self) -> MethodInfo:
        """

        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]:
        """

        :return:
        """
    def GetDynamicILInfo(self) -> DynamicILInfo:
        """

        :return:
        """
    def GetGenericArguments(self) -> Array[Type]:
        """

        :return:
        """
    def GetGenericMethodDefinition(self) -> MethodInfo:
        """

        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    @overload
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    @overload
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    @overload
    def GetILGenerator(self) -> ILGenerator:
        """

        :return:
        """
    @overload
    def GetILGenerator(self, streamSize: int) -> ILGenerator:
        """

        :param streamSize:
        :return:
        """
    def GetMethodBody(self) -> MethodBody:
        """

        :return:
        """
    @overload
    def GetMethodImplementationFlags(self) -> MethodImplAttributes:
        """

        :return:
        """
    @overload
    def GetMethodImplementationFlags(self) -> MethodImplAttributes:
        """

        :return:
        """
    @overload
    def GetParameters(self) -> Array[ParameterInfo]:
        """

        :return:
        """
    @overload
    def GetParameters(self) -> Array[ParameterInfo]:
        """

        :return:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    @overload
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    @overload
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    @overload
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    @overload
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    @overload
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    @overload
    def Invoke(self, obj: object, parameters: Array[object]) -> object:
        """

        :param obj:
        :param parameters:
        :return:
        """
    @overload
    def Invoke(self, obj: object, parameters: Array[object]) -> object:
        """

        :param obj:
        :param parameters:
        :return:
        """
    @overload
    def Invoke(
        self,
        obj: object,
        invokeAttr: BindingFlags,
        binder: Binder,
        parameters: Array[object],
        culture: CultureInfo,
    ) -> object:
        """

        :param obj:
        :param invokeAttr:
        :param binder:
        :param parameters:
        :param culture:
        :return:
        """
    @overload
    def Invoke(
        self,
        obj: object,
        invokeAttr: BindingFlags,
        binder: Binder,
        parameters: Array[object],
        culture: CultureInfo,
    ) -> object:
        """

        :param obj:
        :param invokeAttr:
        :param binder:
        :param parameters:
        :param culture:
        :return:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    def MakeGenericMethod(self, typeArguments: Array[Type]) -> MethodInfo:
        """

        :param typeArguments:
        :return:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """

class DynamicResolver(Resolver):
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

class DynamicScope(Object):
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
    @overload
    def GetTokenFor(self, method: DynamicMethod) -> int:
        """

        :param method:
        :return:
        """
    @overload
    def GetTokenFor(self, signature: Array[int]) -> int:
        """

        :param signature:
        :return:
        """
    @overload
    def GetTokenFor(self, field: RuntimeFieldHandle) -> int:
        """

        :param field:
        :return:
        """
    @overload
    def GetTokenFor(self, method: RuntimeMethodHandle) -> int:
        """

        :param method:
        :return:
        """
    @overload
    def GetTokenFor(self, type: RuntimeTypeHandle) -> int:
        """

        :param type:
        :return:
        """
    @overload
    def GetTokenFor(self, literal: str) -> int:
        """

        :param literal:
        :return:
        """
    @overload
    def GetTokenFor(self, field: RuntimeFieldHandle, typeContext: RuntimeTypeHandle) -> int:
        """

        :param field:
        :param typeContext:
        :return:
        """
    @overload
    def GetTokenFor(self, method: RuntimeMethodHandle, typeContext: RuntimeTypeHandle) -> int:
        """

        :param method:
        :param typeContext:
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

class EnumBuilder(
    TypeInfo, ICustomAttributeProvider, IReflect, IReflectableType, _EnumBuilder, _MemberInfo, _Type
):
    """"""

    @property
    def Assembly(self) -> Assembly:
        """

        :return:
        """
    @property
    def AssemblyQualifiedName(self) -> str:
        """

        :return:
        """
    @property
    def Attributes(self) -> TypeAttributes:
        """

        :return:
        """
    @property
    def BaseType(self) -> Type:
        """

        :return:
        """
    @property
    def ContainsGenericParameters(self) -> bool:
        """

        :return:
        """
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
        """

        :return:
        """
    @property
    def DeclaredConstructors(self) -> IEnumerable[ConstructorInfo]:
        """

        :return:
        """
    @property
    def DeclaredEvents(self) -> IEnumerable[EventInfo]:
        """

        :return:
        """
    @property
    def DeclaredFields(self) -> IEnumerable[FieldInfo]:
        """

        :return:
        """
    @property
    def DeclaredMembers(self) -> IEnumerable[MemberInfo]:
        """

        :return:
        """
    @property
    def DeclaredMethods(self) -> IEnumerable[MethodInfo]:
        """

        :return:
        """
    @property
    def DeclaredNestedTypes(self) -> IEnumerable[TypeInfo]:
        """

        :return:
        """
    @property
    def DeclaredProperties(self) -> IEnumerable[PropertyInfo]:
        """

        :return:
        """
    @property
    def DeclaringMethod(self) -> MethodBase:
        """

        :return:
        """
    @property
    def DeclaringType(self) -> Type:
        """

        :return:
        """
    @property
    def DeclaringType(self) -> Type:
        """

        :return:
        """
    @classmethod
    @property
    def DefaultBinder(cls) -> Binder:
        """

        :return:
        """
    @property
    def FullName(self) -> str:
        """

        :return:
        """
    @property
    def GUID(self) -> Guid:
        """

        :return:
        """
    @property
    def GenericParameterAttributes(self) -> GenericParameterAttributes:
        """

        :return:
        """
    @property
    def GenericParameterPosition(self) -> int:
        """

        :return:
        """
    @property
    def GenericTypeArguments(self) -> Array[Type]:
        """

        :return:
        """
    @property
    def GenericTypeParameters(self) -> Array[Type]:
        """

        :return:
        """
    @property
    def HasElementType(self) -> bool:
        """

        :return:
        """
    @property
    def ImplementedInterfaces(self) -> IEnumerable[Type]:
        """

        :return:
        """
    @property
    def IsAbstract(self) -> bool:
        """

        :return:
        """
    @property
    def IsAnsiClass(self) -> bool:
        """

        :return:
        """
    @property
    def IsArray(self) -> bool:
        """

        :return:
        """
    @property
    def IsAutoClass(self) -> bool:
        """

        :return:
        """
    @property
    def IsAutoLayout(self) -> bool:
        """

        :return:
        """
    @property
    def IsByRef(self) -> bool:
        """

        :return:
        """
    @property
    def IsCOMObject(self) -> bool:
        """

        :return:
        """
    @property
    def IsClass(self) -> bool:
        """

        :return:
        """
    @property
    def IsConstructedGenericType(self) -> bool:
        """

        :return:
        """
    @property
    def IsContextful(self) -> bool:
        """

        :return:
        """
    @property
    def IsEnum(self) -> bool:
        """

        :return:
        """
    @property
    def IsExplicitLayout(self) -> bool:
        """

        :return:
        """
    @property
    def IsGenericParameter(self) -> bool:
        """

        :return:
        """
    @property
    def IsGenericType(self) -> bool:
        """

        :return:
        """
    @property
    def IsGenericTypeDefinition(self) -> bool:
        """

        :return:
        """
    @property
    def IsImport(self) -> bool:
        """

        :return:
        """
    @property
    def IsInterface(self) -> bool:
        """

        :return:
        """
    @property
    def IsLayoutSequential(self) -> bool:
        """

        :return:
        """
    @property
    def IsMarshalByRef(self) -> bool:
        """

        :return:
        """
    @property
    def IsNested(self) -> bool:
        """

        :return:
        """
    @property
    def IsNestedAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsNestedFamANDAssem(self) -> bool:
        """

        :return:
        """
    @property
    def IsNestedFamORAssem(self) -> bool:
        """

        :return:
        """
    @property
    def IsNestedFamily(self) -> bool:
        """

        :return:
        """
    @property
    def IsNestedPrivate(self) -> bool:
        """

        :return:
        """
    @property
    def IsNestedPublic(self) -> bool:
        """

        :return:
        """
    @property
    def IsNotPublic(self) -> bool:
        """

        :return:
        """
    @property
    def IsPointer(self) -> bool:
        """

        :return:
        """
    @property
    def IsPrimitive(self) -> bool:
        """

        :return:
        """
    @property
    def IsPublic(self) -> bool:
        """

        :return:
        """
    @property
    def IsSealed(self) -> bool:
        """

        :return:
        """
    @property
    def IsSecurityCritical(self) -> bool:
        """

        :return:
        """
    @property
    def IsSecuritySafeCritical(self) -> bool:
        """

        :return:
        """
    @property
    def IsSecurityTransparent(self) -> bool:
        """

        :return:
        """
    @property
    def IsSerializable(self) -> bool:
        """

        :return:
        """
    @property
    def IsSpecialName(self) -> bool:
        """

        :return:
        """
    @property
    def IsUnicodeClass(self) -> bool:
        """

        :return:
        """
    @property
    def IsValueType(self) -> bool:
        """

        :return:
        """
    @property
    def IsVisible(self) -> bool:
        """

        :return:
        """
    @property
    def MemberType(self) -> MemberTypes:
        """

        :return:
        """
    @property
    def MemberType(self) -> MemberTypes:
        """

        :return:
        """
    @property
    def MetadataToken(self) -> int:
        """

        :return:
        """
    @property
    def Module(self) -> Module:
        """

        :return:
        """
    @property
    def Module(self) -> Module:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Namespace(self) -> str:
        """

        :return:
        """
    @property
    def ReflectedType(self) -> Type:
        """

        :return:
        """
    @property
    def ReflectedType(self) -> Type:
        """

        :return:
        """
    @property
    def StructLayoutAttribute(self) -> StructLayoutAttribute:
        """

        :return:
        """
    @property
    def TypeHandle(self) -> RuntimeTypeHandle:
        """

        :return:
        """
    @property
    def TypeInitializer(self) -> ConstructorInfo:
        """

        :return:
        """
    @property
    def TypeToken(self) -> TypeToken:
        """

        :return:
        """
    @property
    def UnderlyingField(self) -> FieldBuilder:
        """

        :return:
        """
    @property
    def UnderlyingSystemType(self) -> Type:
        """

        :return:
        """
    @property
    def UnderlyingSystemType(self) -> Type:
        """

        :return:
        """
    def AsType(self) -> Type:
        """

        :return:
        """
    def CreateType(self) -> Type:
        """

        :return:
        """
    def CreateTypeInfo(self) -> TypeInfo:
        """

        :return:
        """
    def DefineLiteral(self, literalName: str, literalValue: object) -> FieldBuilder:
        """

        :param literalName:
        :param literalValue:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def Equals(self, other: object) -> bool:
        """

        :param other:
        :return:
        """
    @overload
    def Equals(self, other: object) -> bool:
        """

        :param other:
        :return:
        """
    @overload
    def Equals(self, o: Type) -> bool:
        """

        :param o:
        :return:
        """
    def FindInterfaces(self, filter: TypeFilter, filterCriteria: object) -> Array[Type]:
        """

        :param filter:
        :param filterCriteria:
        :return:
        """
    def FindMembers(
        self,
        memberType: MemberTypes,
        bindingAttr: BindingFlags,
        filter: MemberFilter,
        filterCriteria: object,
    ) -> Array[MemberInfo]:
        """

        :param memberType:
        :param bindingAttr:
        :param filter:
        :param filterCriteria:
        :return:
        """
    def GetArrayRank(self) -> int:
        """

        :return:
        """
    @overload
    def GetConstructor(self, types: Array[Type]) -> ConstructorInfo:
        """

        :param types:
        :return:
        """
    @overload
    def GetConstructor(
        self,
        bindingAttr: BindingFlags,
        binder: Binder,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> ConstructorInfo:
        """

        :param bindingAttr:
        :param binder:
        :param types:
        :param modifiers:
        :return:
        """
    @overload
    def GetConstructor(
        self,
        bindingAttr: BindingFlags,
        binder: Binder,
        callConvention: CallingConventions,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> ConstructorInfo:
        """

        :param bindingAttr:
        :param binder:
        :param callConvention:
        :param types:
        :param modifiers:
        :return:
        """
    @overload
    def GetConstructors(self) -> Array[ConstructorInfo]:
        """

        :return:
        """
    @overload
    def GetConstructors(self, bindingAttr: BindingFlags) -> Array[ConstructorInfo]:
        """

        :param bindingAttr:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]:
        """

        :return:
        """
    def GetDeclaredEvent(self, name: str) -> EventInfo:
        """

        :param name:
        :return:
        """
    def GetDeclaredField(self, name: str) -> FieldInfo:
        """

        :param name:
        :return:
        """
    def GetDeclaredMethod(self, name: str) -> MethodInfo:
        """

        :param name:
        :return:
        """
    def GetDeclaredMethods(self, name: str) -> IEnumerable[MethodInfo]:
        """

        :param name:
        :return:
        """
    def GetDeclaredNestedType(self, name: str) -> TypeInfo:
        """

        :param name:
        :return:
        """
    def GetDeclaredProperty(self, name: str) -> PropertyInfo:
        """

        :param name:
        :return:
        """
    def GetDefaultMembers(self) -> Array[MemberInfo]:
        """

        :return:
        """
    def GetElementType(self) -> Type:
        """

        :return:
        """
    def GetEnumName(self, value: object) -> str:
        """

        :param value:
        :return:
        """
    def GetEnumNames(self) -> Array[str]:
        """

        :return:
        """
    def GetEnumUnderlyingType(self) -> Type:
        """

        :return:
        """
    def GetEnumValues(self) -> Array:
        """

        :return:
        """
    @overload
    def GetEvent(self, name: str) -> EventInfo:
        """

        :param name:
        :return:
        """
    @overload
    def GetEvent(self, name: str, bindingAttr: BindingFlags) -> EventInfo:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetEvents(self) -> Array[EventInfo]:
        """

        :return:
        """
    @overload
    def GetEvents(self, bindingAttr: BindingFlags) -> Array[EventInfo]:
        """

        :param bindingAttr:
        :return:
        """
    @overload
    def GetField(self, name: str) -> FieldInfo:
        """

        :param name:
        :return:
        """
    @overload
    def GetField(self, name: str, bindingAttr: BindingFlags) -> FieldInfo:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetField(self, name: str, bindingAttr: BindingFlags) -> FieldInfo:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetFields(self) -> Array[FieldInfo]:
        """

        :return:
        """
    @overload
    def GetFields(self, bindingAttr: BindingFlags) -> Array[FieldInfo]:
        """

        :param bindingAttr:
        :return:
        """
    @overload
    def GetFields(self, bindingAttr: BindingFlags) -> Array[FieldInfo]:
        """

        :param bindingAttr:
        :return:
        """
    def GetGenericArguments(self) -> Array[Type]:
        """

        :return:
        """
    def GetGenericParameterConstraints(self) -> Array[Type]:
        """

        :return:
        """
    def GetGenericTypeDefinition(self) -> Type:
        """

        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    @overload
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    @overload
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    @overload
    def GetInterface(self, name: str) -> Type:
        """

        :param name:
        :return:
        """
    @overload
    def GetInterface(self, name: str, ignoreCase: bool) -> Type:
        """

        :param name:
        :param ignoreCase:
        :return:
        """
    def GetInterfaceMap(self, interfaceType: Type) -> InterfaceMapping:
        """

        :param interfaceType:
        :return:
        """
    def GetInterfaces(self) -> Array[Type]:
        """

        :return:
        """
    @overload
    def GetMember(self, name: str) -> Array[MemberInfo]:
        """

        :param name:
        :return:
        """
    @overload
    def GetMember(self, name: str, bindingAttr: BindingFlags) -> Array[MemberInfo]:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetMember(self, name: str, bindingAttr: BindingFlags) -> Array[MemberInfo]:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetMember(
        self, name: str, type: MemberTypes, bindingAttr: BindingFlags
    ) -> Array[MemberInfo]:
        """

        :param name:
        :param type:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetMembers(self) -> Array[MemberInfo]:
        """

        :return:
        """
    @overload
    def GetMembers(self, bindingAttr: BindingFlags) -> Array[MemberInfo]:
        """

        :param bindingAttr:
        :return:
        """
    @overload
    def GetMembers(self, bindingAttr: BindingFlags) -> Array[MemberInfo]:
        """

        :param bindingAttr:
        :return:
        """
    @overload
    def GetMethod(self, name: str) -> MethodInfo:
        """

        :param name:
        :return:
        """
    @overload
    def GetMethod(self, name: str, bindingAttr: BindingFlags) -> MethodInfo:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetMethod(self, name: str, bindingAttr: BindingFlags) -> MethodInfo:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetMethod(self, name: str, types: Array[Type]) -> MethodInfo:
        """

        :param name:
        :param types:
        :return:
        """
    @overload
    def GetMethod(
        self, name: str, types: Array[Type], modifiers: Array[ParameterModifier]
    ) -> MethodInfo:
        """

        :param name:
        :param types:
        :param modifiers:
        :return:
        """
    @overload
    def GetMethod(
        self,
        name: str,
        bindingAttr: BindingFlags,
        binder: Binder,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> MethodInfo:
        """

        :param name:
        :param bindingAttr:
        :param binder:
        :param types:
        :param modifiers:
        :return:
        """
    @overload
    def GetMethod(
        self,
        name: str,
        bindingAttr: BindingFlags,
        binder: Binder,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> MethodInfo:
        """

        :param name:
        :param bindingAttr:
        :param binder:
        :param types:
        :param modifiers:
        :return:
        """
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
        """

        :param name:
        :param bindingAttr:
        :param binder:
        :param callConvention:
        :param types:
        :param modifiers:
        :return:
        """
    @overload
    def GetMethods(self) -> Array[MethodInfo]:
        """

        :return:
        """
    @overload
    def GetMethods(self, bindingAttr: BindingFlags) -> Array[MethodInfo]:
        """

        :param bindingAttr:
        :return:
        """
    @overload
    def GetMethods(self, bindingAttr: BindingFlags) -> Array[MethodInfo]:
        """

        :param bindingAttr:
        :return:
        """
    @overload
    def GetNestedType(self, name: str) -> Type:
        """

        :param name:
        :return:
        """
    @overload
    def GetNestedType(self, name: str, bindingAttr: BindingFlags) -> Type:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetNestedTypes(self) -> Array[Type]:
        """

        :return:
        """
    @overload
    def GetNestedTypes(self, bindingAttr: BindingFlags) -> Array[Type]:
        """

        :param bindingAttr:
        :return:
        """
    @overload
    def GetProperties(self) -> Array[PropertyInfo]:
        """

        :return:
        """
    @overload
    def GetProperties(self, bindingAttr: BindingFlags) -> Array[PropertyInfo]:
        """

        :param bindingAttr:
        :return:
        """
    @overload
    def GetProperties(self, bindingAttr: BindingFlags) -> Array[PropertyInfo]:
        """

        :param bindingAttr:
        :return:
        """
    @overload
    def GetProperty(self, name: str) -> PropertyInfo:
        """

        :param name:
        :return:
        """
    @overload
    def GetProperty(self, name: str, bindingAttr: BindingFlags) -> PropertyInfo:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetProperty(self, name: str, bindingAttr: BindingFlags) -> PropertyInfo:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetProperty(self, name: str, types: Array[Type]) -> PropertyInfo:
        """

        :param name:
        :param types:
        :return:
        """
    @overload
    def GetProperty(self, name: str, returnType: Type) -> PropertyInfo:
        """

        :param name:
        :param returnType:
        :return:
        """
    @overload
    def GetProperty(self, name: str, returnType: Type, types: Array[Type]) -> PropertyInfo:
        """

        :param name:
        :param returnType:
        :param types:
        :return:
        """
    @overload
    def GetProperty(
        self, name: str, returnType: Type, types: Array[Type], modifiers: Array[ParameterModifier]
    ) -> PropertyInfo:
        """

        :param name:
        :param returnType:
        :param types:
        :param modifiers:
        :return:
        """
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
        """

        :param name:
        :param bindingAttr:
        :param binder:
        :param returnType:
        :param types:
        :param modifiers:
        :return:
        """
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
        """

        :param name:
        :param bindingAttr:
        :param binder:
        :param returnType:
        :param types:
        :param modifiers:
        :return:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetTypeInfo(self) -> TypeInfo:
        """

        :return:
        """
    @overload
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    @overload
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    @overload
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    @overload
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    @overload
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    @overload
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    @overload
    def InvokeMember(
        self,
        name: str,
        invokeAttr: BindingFlags,
        binder: Binder,
        target: object,
        args: Array[object],
    ) -> object:
        """

        :param name:
        :param invokeAttr:
        :param binder:
        :param target:
        :param args:
        :return:
        """
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
        """

        :param name:
        :param invokeAttr:
        :param binder:
        :param target:
        :param args:
        :param culture:
        :return:
        """
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
        """

        :param name:
        :param invokeAttr:
        :param binder:
        :param target:
        :param args:
        :param modifiers:
        :param culture:
        :param namedParameters:
        :return:
        """
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
        """

        :param name:
        :param invokeAttr:
        :param binder:
        :param target:
        :param args:
        :param modifiers:
        :param culture:
        :param namedParameters:
        :return:
        """
    @overload
    def IsAssignableFrom(self, typeInfo: TypeInfo) -> bool:
        """

        :param typeInfo:
        :return:
        """
    @overload
    def IsAssignableFrom(self, c: Type) -> bool:
        """

        :param c:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    def IsEnumDefined(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    def IsEquivalentTo(self, other: Type) -> bool:
        """

        :param other:
        :return:
        """
    def IsInstanceOfType(self, o: object) -> bool:
        """

        :param o:
        :return:
        """
    def IsSubclassOf(self, c: Type) -> bool:
        """

        :param c:
        :return:
        """
    @overload
    def MakeArrayType(self) -> Type:
        """

        :return:
        """
    @overload
    def MakeArrayType(self, rank: int) -> Type:
        """

        :param rank:
        :return:
        """
    def MakeByRefType(self) -> Type:
        """

        :return:
        """
    def MakeGenericType(self, typeArguments: Array[Type]) -> Type:
        """

        :param typeArguments:
        :return:
        """
    def MakePointerType(self) -> Type:
        """

        :return:
        """
    @overload
    def SetCustomAttribute(self, customBuilder: CustomAttributeBuilder) -> None:
        """

        :param customBuilder:
        """
    @overload
    def SetCustomAttribute(self, con: ConstructorInfo, binaryAttribute: Array[int]) -> None:
        """

        :param con:
        :param binaryAttribute:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """

class EventBuilder(Object, _EventBuilder):
    """"""

    def AddOtherMethod(self, mdBuilder: MethodBuilder) -> None:
        """

        :param mdBuilder:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetEventToken(self) -> EventToken:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def SetAddOnMethod(self, mdBuilder: MethodBuilder) -> None:
        """

        :param mdBuilder:
        """
    @overload
    def SetCustomAttribute(self, customBuilder: CustomAttributeBuilder) -> None:
        """

        :param customBuilder:
        """
    @overload
    def SetCustomAttribute(self, con: ConstructorInfo, binaryAttribute: Array[int]) -> None:
        """

        :param con:
        :param binaryAttribute:
        """
    def SetRaiseMethod(self, mdBuilder: MethodBuilder) -> None:
        """

        :param mdBuilder:
        """
    def SetRemoveOnMethod(self, mdBuilder: MethodBuilder) -> None:
        """

        :param mdBuilder:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class EventToken(ValueType):
    """"""

    Empty: Final[ClassVar[EventToken]] = ...
    """
    
    :return: 
    """
    @property
    def Token(self) -> int:
        """

        :return:
        """
    @overload
    def Equals(self, obj: EventToken) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
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
    def __eq__(self, other: EventToken) -> bool:
        """

        :param other:
        :return:
        """
    def __ne__(self, other: EventToken) -> bool:
        """

        :param other:
        :return:
        """
    @classmethod
    def op_Equality(cls, a: EventToken, b: EventToken) -> bool:
        """

        :param a:
        :param b:
        :return:
        """
    @classmethod
    def op_Inequality(cls, a: EventToken, b: EventToken) -> bool:
        """

        :param a:
        :param b:
        :return:
        """

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
    ):
        """

        :param tryOffset:
        :param tryLength:
        :param filterOffset:
        :param handlerOffset:
        :param handlerLength:
        :param kind:
        :param exceptionTypeToken:
        """
    @property
    def ExceptionTypeToken(self) -> int:
        """

        :return:
        """
    @property
    def FilterOffset(self) -> int:
        """

        :return:
        """
    @property
    def HandlerLength(self) -> int:
        """

        :return:
        """
    @property
    def HandlerOffset(self) -> int:
        """

        :return:
        """
    @property
    def Kind(self) -> ExceptionHandlingClauseOptions:
        """

        :return:
        """
    @property
    def TryLength(self) -> int:
        """

        :return:
        """
    @property
    def TryOffset(self) -> int:
        """

        :return:
        """
    @overload
    def Equals(self, other: ExceptionHandler) -> bool:
        """

        :param other:
        :return:
        """
    @overload
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
    def __eq__(self, other: ExceptionHandler) -> bool:
        """

        :param other:
        :return:
        """
    def __ne__(self, other: ExceptionHandler) -> bool:
        """

        :param other:
        :return:
        """
    @classmethod
    def op_Equality(cls, left: ExceptionHandler, right: ExceptionHandler) -> bool:
        """

        :param left:
        :param right:
        :return:
        """
    @classmethod
    def op_Inequality(cls, left: ExceptionHandler, right: ExceptionHandler) -> bool:
        """

        :param left:
        :param right:
        :return:
        """

class FieldBuilder(FieldInfo, ICustomAttributeProvider, _FieldBuilder, _FieldInfo, _MemberInfo):
    """"""

    @property
    def Attributes(self) -> FieldAttributes:
        """

        :return:
        """
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
        """

        :return:
        """
    @property
    def DeclaringType(self) -> Type:
        """

        :return:
        """
    @property
    def DeclaringType(self) -> Type:
        """

        :return:
        """
    @property
    def FieldHandle(self) -> RuntimeFieldHandle:
        """

        :return:
        """
    @property
    def FieldType(self) -> Type:
        """

        :return:
        """
    @property
    def IsAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamily(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamilyAndAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamilyOrAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsInitOnly(self) -> bool:
        """

        :return:
        """
    @property
    def IsLiteral(self) -> bool:
        """

        :return:
        """
    @property
    def IsNotSerialized(self) -> bool:
        """

        :return:
        """
    @property
    def IsPinvokeImpl(self) -> bool:
        """

        :return:
        """
    @property
    def IsPrivate(self) -> bool:
        """

        :return:
        """
    @property
    def IsPublic(self) -> bool:
        """

        :return:
        """
    @property
    def IsSecurityCritical(self) -> bool:
        """

        :return:
        """
    @property
    def IsSecuritySafeCritical(self) -> bool:
        """

        :return:
        """
    @property
    def IsSecurityTransparent(self) -> bool:
        """

        :return:
        """
    @property
    def IsSpecialName(self) -> bool:
        """

        :return:
        """
    @property
    def IsStatic(self) -> bool:
        """

        :return:
        """
    @property
    def MemberType(self) -> MemberTypes:
        """

        :return:
        """
    @property
    def MemberType(self) -> MemberTypes:
        """

        :return:
        """
    @property
    def MetadataToken(self) -> int:
        """

        :return:
        """
    @property
    def Module(self) -> Module:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def ReflectedType(self) -> Type:
        """

        :return:
        """
    @property
    def ReflectedType(self) -> Type:
        """

        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def Equals(self, other: object) -> bool:
        """

        :param other:
        :return:
        """
    @overload
    def Equals(self, other: object) -> bool:
        """

        :param other:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]:
        """

        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    @overload
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    @overload
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetOptionalCustomModifiers(self) -> Array[Type]:
        """

        :return:
        """
    def GetRawConstantValue(self) -> object:
        """

        :return:
        """
    def GetRequiredCustomModifiers(self) -> Array[Type]:
        """

        :return:
        """
    def GetToken(self) -> FieldToken:
        """

        :return:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    @overload
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    @overload
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    @overload
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    @overload
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    @overload
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    def GetValue(self, obj: object) -> object:
        """

        :param obj:
        :return:
        """
    def GetValueDirect(self, obj: TypedReference) -> object:
        """

        :param obj:
        :return:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    def SetConstant(self, defaultValue: object) -> None:
        """

        :param defaultValue:
        """
    @overload
    def SetCustomAttribute(self, customBuilder: CustomAttributeBuilder) -> None:
        """

        :param customBuilder:
        """
    @overload
    def SetCustomAttribute(self, con: ConstructorInfo, binaryAttribute: Array[int]) -> None:
        """

        :param con:
        :param binaryAttribute:
        """
    def SetMarshal(self, unmanagedMarshal: UnmanagedMarshal) -> None:
        """

        :param unmanagedMarshal:
        """
    def SetOffset(self, iOffset: int) -> None:
        """

        :param iOffset:
        """
    @overload
    def SetValue(self, obj: object, value: object) -> None:
        """

        :param obj:
        :param value:
        """
    @overload
    def SetValue(
        self,
        obj: object,
        value: object,
        invokeAttr: BindingFlags,
        binder: Binder,
        culture: CultureInfo,
    ) -> None:
        """

        :param obj:
        :param value:
        :param invokeAttr:
        :param binder:
        :param culture:
        """
    def SetValueDirect(self, obj: TypedReference, value: object) -> None:
        """

        :param obj:
        :param value:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """

class FieldOnTypeBuilderInstantiation(FieldInfo, ICustomAttributeProvider, _FieldInfo, _MemberInfo):
    """"""

    @property
    def Attributes(self) -> FieldAttributes:
        """

        :return:
        """
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
        """

        :return:
        """
    @property
    def DeclaringType(self) -> Type:
        """

        :return:
        """
    @property
    def DeclaringType(self) -> Type:
        """

        :return:
        """
    @property
    def FieldHandle(self) -> RuntimeFieldHandle:
        """

        :return:
        """
    @property
    def FieldType(self) -> Type:
        """

        :return:
        """
    @property
    def IsAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamily(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamilyAndAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamilyOrAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsInitOnly(self) -> bool:
        """

        :return:
        """
    @property
    def IsLiteral(self) -> bool:
        """

        :return:
        """
    @property
    def IsNotSerialized(self) -> bool:
        """

        :return:
        """
    @property
    def IsPinvokeImpl(self) -> bool:
        """

        :return:
        """
    @property
    def IsPrivate(self) -> bool:
        """

        :return:
        """
    @property
    def IsPublic(self) -> bool:
        """

        :return:
        """
    @property
    def IsSecurityCritical(self) -> bool:
        """

        :return:
        """
    @property
    def IsSecuritySafeCritical(self) -> bool:
        """

        :return:
        """
    @property
    def IsSecurityTransparent(self) -> bool:
        """

        :return:
        """
    @property
    def IsSpecialName(self) -> bool:
        """

        :return:
        """
    @property
    def IsStatic(self) -> bool:
        """

        :return:
        """
    @property
    def MemberType(self) -> MemberTypes:
        """

        :return:
        """
    @property
    def MemberType(self) -> MemberTypes:
        """

        :return:
        """
    @property
    def MetadataToken(self) -> int:
        """

        :return:
        """
    @property
    def Module(self) -> Module:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def ReflectedType(self) -> Type:
        """

        :return:
        """
    @property
    def ReflectedType(self) -> Type:
        """

        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def Equals(self, other: object) -> bool:
        """

        :param other:
        :return:
        """
    @overload
    def Equals(self, other: object) -> bool:
        """

        :param other:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]:
        """

        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    @overload
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetOptionalCustomModifiers(self) -> Array[Type]:
        """

        :return:
        """
    def GetRawConstantValue(self) -> object:
        """

        :return:
        """
    def GetRequiredCustomModifiers(self) -> Array[Type]:
        """

        :return:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    @overload
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    @overload
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    @overload
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    def GetValue(self, obj: object) -> object:
        """

        :param obj:
        :return:
        """
    def GetValueDirect(self, obj: TypedReference) -> object:
        """

        :param obj:
        :return:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def SetValue(self, obj: object, value: object) -> None:
        """

        :param obj:
        :param value:
        """
    @overload
    def SetValue(
        self,
        obj: object,
        value: object,
        invokeAttr: BindingFlags,
        binder: Binder,
        culture: CultureInfo,
    ) -> None:
        """

        :param obj:
        :param value:
        :param invokeAttr:
        :param binder:
        :param culture:
        """
    def SetValueDirect(self, obj: TypedReference, value: object) -> None:
        """

        :param obj:
        :param value:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """

class FieldToken(ValueType):
    """"""

    Empty: Final[ClassVar[FieldToken]] = ...
    """
    
    :return: 
    """
    @property
    def Token(self) -> int:
        """

        :return:
        """
    @overload
    def Equals(self, obj: FieldToken) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
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
    def __eq__(self, other: FieldToken) -> bool:
        """

        :param other:
        :return:
        """
    def __ne__(self, other: FieldToken) -> bool:
        """

        :param other:
        :return:
        """
    @classmethod
    def op_Equality(cls, a: FieldToken, b: FieldToken) -> bool:
        """

        :param a:
        :param b:
        :return:
        """
    @classmethod
    def op_Inequality(cls, a: FieldToken, b: FieldToken) -> bool:
        """

        :param a:
        :param b:
        :return:
        """

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

class GenericMethodInfo(Object):
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

class GenericTypeParameterBuilder(
    TypeInfo, ICustomAttributeProvider, IReflect, IReflectableType, _MemberInfo, _Type
):
    """"""

    @property
    def Assembly(self) -> Assembly:
        """

        :return:
        """
    @property
    def AssemblyQualifiedName(self) -> str:
        """

        :return:
        """
    @property
    def Attributes(self) -> TypeAttributes:
        """

        :return:
        """
    @property
    def BaseType(self) -> Type:
        """

        :return:
        """
    @property
    def ContainsGenericParameters(self) -> bool:
        """

        :return:
        """
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
        """

        :return:
        """
    @property
    def DeclaredConstructors(self) -> IEnumerable[ConstructorInfo]:
        """

        :return:
        """
    @property
    def DeclaredEvents(self) -> IEnumerable[EventInfo]:
        """

        :return:
        """
    @property
    def DeclaredFields(self) -> IEnumerable[FieldInfo]:
        """

        :return:
        """
    @property
    def DeclaredMembers(self) -> IEnumerable[MemberInfo]:
        """

        :return:
        """
    @property
    def DeclaredMethods(self) -> IEnumerable[MethodInfo]:
        """

        :return:
        """
    @property
    def DeclaredNestedTypes(self) -> IEnumerable[TypeInfo]:
        """

        :return:
        """
    @property
    def DeclaredProperties(self) -> IEnumerable[PropertyInfo]:
        """

        :return:
        """
    @property
    def DeclaringMethod(self) -> MethodBase:
        """

        :return:
        """
    @property
    def DeclaringType(self) -> Type:
        """

        :return:
        """
    @property
    def DeclaringType(self) -> Type:
        """

        :return:
        """
    @classmethod
    @property
    def DefaultBinder(cls) -> Binder:
        """

        :return:
        """
    @property
    def FullName(self) -> str:
        """

        :return:
        """
    @property
    def GUID(self) -> Guid:
        """

        :return:
        """
    @property
    def GenericParameterAttributes(self) -> GenericParameterAttributes:
        """

        :return:
        """
    @property
    def GenericParameterPosition(self) -> int:
        """

        :return:
        """
    @property
    def GenericTypeArguments(self) -> Array[Type]:
        """

        :return:
        """
    @property
    def GenericTypeParameters(self) -> Array[Type]:
        """

        :return:
        """
    @property
    def HasElementType(self) -> bool:
        """

        :return:
        """
    @property
    def ImplementedInterfaces(self) -> IEnumerable[Type]:
        """

        :return:
        """
    @property
    def IsAbstract(self) -> bool:
        """

        :return:
        """
    @property
    def IsAnsiClass(self) -> bool:
        """

        :return:
        """
    @property
    def IsArray(self) -> bool:
        """

        :return:
        """
    @property
    def IsAutoClass(self) -> bool:
        """

        :return:
        """
    @property
    def IsAutoLayout(self) -> bool:
        """

        :return:
        """
    @property
    def IsByRef(self) -> bool:
        """

        :return:
        """
    @property
    def IsCOMObject(self) -> bool:
        """

        :return:
        """
    @property
    def IsClass(self) -> bool:
        """

        :return:
        """
    @property
    def IsConstructedGenericType(self) -> bool:
        """

        :return:
        """
    @property
    def IsContextful(self) -> bool:
        """

        :return:
        """
    @property
    def IsEnum(self) -> bool:
        """

        :return:
        """
    @property
    def IsExplicitLayout(self) -> bool:
        """

        :return:
        """
    @property
    def IsGenericParameter(self) -> bool:
        """

        :return:
        """
    @property
    def IsGenericType(self) -> bool:
        """

        :return:
        """
    @property
    def IsGenericTypeDefinition(self) -> bool:
        """

        :return:
        """
    @property
    def IsImport(self) -> bool:
        """

        :return:
        """
    @property
    def IsInterface(self) -> bool:
        """

        :return:
        """
    @property
    def IsLayoutSequential(self) -> bool:
        """

        :return:
        """
    @property
    def IsMarshalByRef(self) -> bool:
        """

        :return:
        """
    @property
    def IsNested(self) -> bool:
        """

        :return:
        """
    @property
    def IsNestedAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsNestedFamANDAssem(self) -> bool:
        """

        :return:
        """
    @property
    def IsNestedFamORAssem(self) -> bool:
        """

        :return:
        """
    @property
    def IsNestedFamily(self) -> bool:
        """

        :return:
        """
    @property
    def IsNestedPrivate(self) -> bool:
        """

        :return:
        """
    @property
    def IsNestedPublic(self) -> bool:
        """

        :return:
        """
    @property
    def IsNotPublic(self) -> bool:
        """

        :return:
        """
    @property
    def IsPointer(self) -> bool:
        """

        :return:
        """
    @property
    def IsPrimitive(self) -> bool:
        """

        :return:
        """
    @property
    def IsPublic(self) -> bool:
        """

        :return:
        """
    @property
    def IsSealed(self) -> bool:
        """

        :return:
        """
    @property
    def IsSecurityCritical(self) -> bool:
        """

        :return:
        """
    @property
    def IsSecuritySafeCritical(self) -> bool:
        """

        :return:
        """
    @property
    def IsSecurityTransparent(self) -> bool:
        """

        :return:
        """
    @property
    def IsSerializable(self) -> bool:
        """

        :return:
        """
    @property
    def IsSpecialName(self) -> bool:
        """

        :return:
        """
    @property
    def IsUnicodeClass(self) -> bool:
        """

        :return:
        """
    @property
    def IsValueType(self) -> bool:
        """

        :return:
        """
    @property
    def IsVisible(self) -> bool:
        """

        :return:
        """
    @property
    def MemberType(self) -> MemberTypes:
        """

        :return:
        """
    @property
    def MemberType(self) -> MemberTypes:
        """

        :return:
        """
    @property
    def MetadataToken(self) -> int:
        """

        :return:
        """
    @property
    def Module(self) -> Module:
        """

        :return:
        """
    @property
    def Module(self) -> Module:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Namespace(self) -> str:
        """

        :return:
        """
    @property
    def ReflectedType(self) -> Type:
        """

        :return:
        """
    @property
    def ReflectedType(self) -> Type:
        """

        :return:
        """
    @property
    def StructLayoutAttribute(self) -> StructLayoutAttribute:
        """

        :return:
        """
    @property
    def TypeHandle(self) -> RuntimeTypeHandle:
        """

        :return:
        """
    @property
    def TypeInitializer(self) -> ConstructorInfo:
        """

        :return:
        """
    @property
    def UnderlyingSystemType(self) -> Type:
        """

        :return:
        """
    @property
    def UnderlyingSystemType(self) -> Type:
        """

        :return:
        """
    def AsType(self) -> Type:
        """

        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def Equals(self, other: object) -> bool:
        """

        :param other:
        :return:
        """
    @overload
    def Equals(self, other: object) -> bool:
        """

        :param other:
        :return:
        """
    @overload
    def Equals(self, o: Type) -> bool:
        """

        :param o:
        :return:
        """
    def FindInterfaces(self, filter: TypeFilter, filterCriteria: object) -> Array[Type]:
        """

        :param filter:
        :param filterCriteria:
        :return:
        """
    def FindMembers(
        self,
        memberType: MemberTypes,
        bindingAttr: BindingFlags,
        filter: MemberFilter,
        filterCriteria: object,
    ) -> Array[MemberInfo]:
        """

        :param memberType:
        :param bindingAttr:
        :param filter:
        :param filterCriteria:
        :return:
        """
    def GetArrayRank(self) -> int:
        """

        :return:
        """
    @overload
    def GetConstructor(self, types: Array[Type]) -> ConstructorInfo:
        """

        :param types:
        :return:
        """
    @overload
    def GetConstructor(
        self,
        bindingAttr: BindingFlags,
        binder: Binder,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> ConstructorInfo:
        """

        :param bindingAttr:
        :param binder:
        :param types:
        :param modifiers:
        :return:
        """
    @overload
    def GetConstructor(
        self,
        bindingAttr: BindingFlags,
        binder: Binder,
        callConvention: CallingConventions,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> ConstructorInfo:
        """

        :param bindingAttr:
        :param binder:
        :param callConvention:
        :param types:
        :param modifiers:
        :return:
        """
    @overload
    def GetConstructors(self) -> Array[ConstructorInfo]:
        """

        :return:
        """
    @overload
    def GetConstructors(self, bindingAttr: BindingFlags) -> Array[ConstructorInfo]:
        """

        :param bindingAttr:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]:
        """

        :return:
        """
    def GetDeclaredEvent(self, name: str) -> EventInfo:
        """

        :param name:
        :return:
        """
    def GetDeclaredField(self, name: str) -> FieldInfo:
        """

        :param name:
        :return:
        """
    def GetDeclaredMethod(self, name: str) -> MethodInfo:
        """

        :param name:
        :return:
        """
    def GetDeclaredMethods(self, name: str) -> IEnumerable[MethodInfo]:
        """

        :param name:
        :return:
        """
    def GetDeclaredNestedType(self, name: str) -> TypeInfo:
        """

        :param name:
        :return:
        """
    def GetDeclaredProperty(self, name: str) -> PropertyInfo:
        """

        :param name:
        :return:
        """
    def GetDefaultMembers(self) -> Array[MemberInfo]:
        """

        :return:
        """
    def GetElementType(self) -> Type:
        """

        :return:
        """
    def GetEnumName(self, value: object) -> str:
        """

        :param value:
        :return:
        """
    def GetEnumNames(self) -> Array[str]:
        """

        :return:
        """
    def GetEnumUnderlyingType(self) -> Type:
        """

        :return:
        """
    def GetEnumValues(self) -> Array:
        """

        :return:
        """
    @overload
    def GetEvent(self, name: str) -> EventInfo:
        """

        :param name:
        :return:
        """
    @overload
    def GetEvent(self, name: str, bindingAttr: BindingFlags) -> EventInfo:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetEvents(self) -> Array[EventInfo]:
        """

        :return:
        """
    @overload
    def GetEvents(self, bindingAttr: BindingFlags) -> Array[EventInfo]:
        """

        :param bindingAttr:
        :return:
        """
    @overload
    def GetField(self, name: str) -> FieldInfo:
        """

        :param name:
        :return:
        """
    @overload
    def GetField(self, name: str, bindingAttr: BindingFlags) -> FieldInfo:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetField(self, name: str, bindingAttr: BindingFlags) -> FieldInfo:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetFields(self) -> Array[FieldInfo]:
        """

        :return:
        """
    @overload
    def GetFields(self, bindingAttr: BindingFlags) -> Array[FieldInfo]:
        """

        :param bindingAttr:
        :return:
        """
    @overload
    def GetFields(self, bindingAttr: BindingFlags) -> Array[FieldInfo]:
        """

        :param bindingAttr:
        :return:
        """
    def GetGenericArguments(self) -> Array[Type]:
        """

        :return:
        """
    def GetGenericParameterConstraints(self) -> Array[Type]:
        """

        :return:
        """
    def GetGenericTypeDefinition(self) -> Type:
        """

        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    @overload
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    @overload
    def GetInterface(self, name: str) -> Type:
        """

        :param name:
        :return:
        """
    @overload
    def GetInterface(self, name: str, ignoreCase: bool) -> Type:
        """

        :param name:
        :param ignoreCase:
        :return:
        """
    def GetInterfaceMap(self, interfaceType: Type) -> InterfaceMapping:
        """

        :param interfaceType:
        :return:
        """
    def GetInterfaces(self) -> Array[Type]:
        """

        :return:
        """
    @overload
    def GetMember(self, name: str) -> Array[MemberInfo]:
        """

        :param name:
        :return:
        """
    @overload
    def GetMember(self, name: str, bindingAttr: BindingFlags) -> Array[MemberInfo]:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetMember(self, name: str, bindingAttr: BindingFlags) -> Array[MemberInfo]:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetMember(
        self, name: str, type: MemberTypes, bindingAttr: BindingFlags
    ) -> Array[MemberInfo]:
        """

        :param name:
        :param type:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetMembers(self) -> Array[MemberInfo]:
        """

        :return:
        """
    @overload
    def GetMembers(self, bindingAttr: BindingFlags) -> Array[MemberInfo]:
        """

        :param bindingAttr:
        :return:
        """
    @overload
    def GetMembers(self, bindingAttr: BindingFlags) -> Array[MemberInfo]:
        """

        :param bindingAttr:
        :return:
        """
    @overload
    def GetMethod(self, name: str) -> MethodInfo:
        """

        :param name:
        :return:
        """
    @overload
    def GetMethod(self, name: str, bindingAttr: BindingFlags) -> MethodInfo:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetMethod(self, name: str, bindingAttr: BindingFlags) -> MethodInfo:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetMethod(self, name: str, types: Array[Type]) -> MethodInfo:
        """

        :param name:
        :param types:
        :return:
        """
    @overload
    def GetMethod(
        self, name: str, types: Array[Type], modifiers: Array[ParameterModifier]
    ) -> MethodInfo:
        """

        :param name:
        :param types:
        :param modifiers:
        :return:
        """
    @overload
    def GetMethod(
        self,
        name: str,
        bindingAttr: BindingFlags,
        binder: Binder,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> MethodInfo:
        """

        :param name:
        :param bindingAttr:
        :param binder:
        :param types:
        :param modifiers:
        :return:
        """
    @overload
    def GetMethod(
        self,
        name: str,
        bindingAttr: BindingFlags,
        binder: Binder,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> MethodInfo:
        """

        :param name:
        :param bindingAttr:
        :param binder:
        :param types:
        :param modifiers:
        :return:
        """
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
        """

        :param name:
        :param bindingAttr:
        :param binder:
        :param callConvention:
        :param types:
        :param modifiers:
        :return:
        """
    @overload
    def GetMethods(self) -> Array[MethodInfo]:
        """

        :return:
        """
    @overload
    def GetMethods(self, bindingAttr: BindingFlags) -> Array[MethodInfo]:
        """

        :param bindingAttr:
        :return:
        """
    @overload
    def GetMethods(self, bindingAttr: BindingFlags) -> Array[MethodInfo]:
        """

        :param bindingAttr:
        :return:
        """
    @overload
    def GetNestedType(self, name: str) -> Type:
        """

        :param name:
        :return:
        """
    @overload
    def GetNestedType(self, name: str, bindingAttr: BindingFlags) -> Type:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetNestedTypes(self) -> Array[Type]:
        """

        :return:
        """
    @overload
    def GetNestedTypes(self, bindingAttr: BindingFlags) -> Array[Type]:
        """

        :param bindingAttr:
        :return:
        """
    @overload
    def GetProperties(self) -> Array[PropertyInfo]:
        """

        :return:
        """
    @overload
    def GetProperties(self, bindingAttr: BindingFlags) -> Array[PropertyInfo]:
        """

        :param bindingAttr:
        :return:
        """
    @overload
    def GetProperties(self, bindingAttr: BindingFlags) -> Array[PropertyInfo]:
        """

        :param bindingAttr:
        :return:
        """
    @overload
    def GetProperty(self, name: str) -> PropertyInfo:
        """

        :param name:
        :return:
        """
    @overload
    def GetProperty(self, name: str, bindingAttr: BindingFlags) -> PropertyInfo:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetProperty(self, name: str, bindingAttr: BindingFlags) -> PropertyInfo:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetProperty(self, name: str, types: Array[Type]) -> PropertyInfo:
        """

        :param name:
        :param types:
        :return:
        """
    @overload
    def GetProperty(self, name: str, returnType: Type) -> PropertyInfo:
        """

        :param name:
        :param returnType:
        :return:
        """
    @overload
    def GetProperty(self, name: str, returnType: Type, types: Array[Type]) -> PropertyInfo:
        """

        :param name:
        :param returnType:
        :param types:
        :return:
        """
    @overload
    def GetProperty(
        self, name: str, returnType: Type, types: Array[Type], modifiers: Array[ParameterModifier]
    ) -> PropertyInfo:
        """

        :param name:
        :param returnType:
        :param types:
        :param modifiers:
        :return:
        """
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
        """

        :param name:
        :param bindingAttr:
        :param binder:
        :param returnType:
        :param types:
        :param modifiers:
        :return:
        """
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
        """

        :param name:
        :param bindingAttr:
        :param binder:
        :param returnType:
        :param types:
        :param modifiers:
        :return:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetTypeInfo(self) -> TypeInfo:
        """

        :return:
        """
    @overload
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    @overload
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    @overload
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    @overload
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    @overload
    def InvokeMember(
        self,
        name: str,
        invokeAttr: BindingFlags,
        binder: Binder,
        target: object,
        args: Array[object],
    ) -> object:
        """

        :param name:
        :param invokeAttr:
        :param binder:
        :param target:
        :param args:
        :return:
        """
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
        """

        :param name:
        :param invokeAttr:
        :param binder:
        :param target:
        :param args:
        :param culture:
        :return:
        """
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
        """

        :param name:
        :param invokeAttr:
        :param binder:
        :param target:
        :param args:
        :param modifiers:
        :param culture:
        :param namedParameters:
        :return:
        """
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
        """

        :param name:
        :param invokeAttr:
        :param binder:
        :param target:
        :param args:
        :param modifiers:
        :param culture:
        :param namedParameters:
        :return:
        """
    @overload
    def IsAssignableFrom(self, typeInfo: TypeInfo) -> bool:
        """

        :param typeInfo:
        :return:
        """
    @overload
    def IsAssignableFrom(self, c: Type) -> bool:
        """

        :param c:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    def IsEnumDefined(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    def IsEquivalentTo(self, other: Type) -> bool:
        """

        :param other:
        :return:
        """
    def IsInstanceOfType(self, o: object) -> bool:
        """

        :param o:
        :return:
        """
    def IsSubclassOf(self, c: Type) -> bool:
        """

        :param c:
        :return:
        """
    @overload
    def MakeArrayType(self) -> Type:
        """

        :return:
        """
    @overload
    def MakeArrayType(self, rank: int) -> Type:
        """

        :param rank:
        :return:
        """
    def MakeByRefType(self) -> Type:
        """

        :return:
        """
    def MakeGenericType(self, typeArguments: Array[Type]) -> Type:
        """

        :param typeArguments:
        :return:
        """
    def MakePointerType(self) -> Type:
        """

        :return:
        """
    def SetBaseTypeConstraint(self, baseTypeConstraint: Type) -> None:
        """

        :param baseTypeConstraint:
        """
    @overload
    def SetCustomAttribute(self, customBuilder: CustomAttributeBuilder) -> None:
        """

        :param customBuilder:
        """
    @overload
    def SetCustomAttribute(self, con: ConstructorInfo, binaryAttribute: Array[int]) -> None:
        """

        :param con:
        :param binaryAttribute:
        """
    def SetGenericParameterAttributes(
        self, genericParameterAttributes: GenericParameterAttributes
    ) -> None:
        """

        :param genericParameterAttributes:
        """
    def SetInterfaceConstraints(self, interfaceConstraints: Array[Type]) -> None:
        """

        :param interfaceConstraints:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """

class ILGenerator(Object, _ILGenerator):
    """"""

    @property
    def ILOffset(self) -> int:
        """

        :return:
        """
    def BeginCatchBlock(self, exceptionType: Type) -> None:
        """

        :param exceptionType:
        """
    def BeginExceptFilterBlock(self) -> None:
        """"""
    def BeginExceptionBlock(self) -> Label:
        """

        :return:
        """
    def BeginFaultBlock(self) -> None:
        """"""
    def BeginFinallyBlock(self) -> None:
        """"""
    def BeginScope(self) -> None:
        """"""
    @overload
    def DeclareLocal(self, localType: Type) -> LocalBuilder:
        """

        :param localType:
        :return:
        """
    @overload
    def DeclareLocal(self, localType: Type, pinned: bool) -> LocalBuilder:
        """

        :param localType:
        :param pinned:
        :return:
        """
    def DefineLabel(self) -> Label:
        """

        :return:
        """
    @overload
    def Emit(self, opcode: OpCode) -> None:
        """

        :param opcode:
        """
    @overload
    def Emit(self, opcode: OpCode, label: Label) -> None:
        """

        :param opcode:
        :param label:
        """
    @overload
    def Emit(self, opcode: OpCode, local: LocalBuilder) -> None:
        """

        :param opcode:
        :param local:
        """
    @overload
    def Emit(self, opcode: OpCode, signature: SignatureHelper) -> None:
        """

        :param opcode:
        :param signature:
        """
    @overload
    def Emit(self, opcode: OpCode, con: ConstructorInfo) -> None:
        """

        :param opcode:
        :param con:
        """
    @overload
    def Emit(self, opcode: OpCode, field: FieldInfo) -> None:
        """

        :param opcode:
        :param field:
        """
    @overload
    def Emit(self, opcode: OpCode, meth: MethodInfo) -> None:
        """

        :param opcode:
        :param meth:
        """
    @overload
    def Emit(self, opcode: OpCode, labels: Array[Label]) -> None:
        """

        :param opcode:
        :param labels:
        """
    @overload
    def Emit(self, opcode: OpCode, arg: int) -> None:
        """

        :param opcode:
        :param arg:
        """
    @overload
    def Emit(self, opcode: OpCode, arg: float) -> None:
        """

        :param opcode:
        :param arg:
        """
    @overload
    def Emit(self, opcode: OpCode, arg: int) -> None:
        """

        :param opcode:
        :param arg:
        """
    @overload
    def Emit(self, opcode: OpCode, arg: int) -> None:
        """

        :param opcode:
        :param arg:
        """
    @overload
    def Emit(self, opcode: OpCode, arg: int) -> None:
        """

        :param opcode:
        :param arg:
        """
    @overload
    def Emit(self, opcode: OpCode, arg: int) -> None:
        """

        :param opcode:
        :param arg:
        """
    @overload
    def Emit(self, opcode: OpCode, arg: float) -> None:
        """

        :param opcode:
        :param arg:
        """
    @overload
    def Emit(self, opcode: OpCode, str: str) -> None:
        """

        :param opcode:
        :param str:
        """
    @overload
    def Emit(self, opcode: OpCode, cls: Type) -> None:
        """

        :param opcode:
        :param cls:
        """
    def EmitCall(
        self, opcode: OpCode, methodInfo: MethodInfo, optionalParameterTypes: Array[Type]
    ) -> None:
        """

        :param opcode:
        :param methodInfo:
        :param optionalParameterTypes:
        """
    @overload
    def EmitCalli(
        self,
        opcode: OpCode,
        unmanagedCallConv: CallingConvention,
        returnType: Type,
        parameterTypes: Array[Type],
    ) -> None:
        """

        :param opcode:
        :param unmanagedCallConv:
        :param returnType:
        :param parameterTypes:
        """
    @overload
    def EmitCalli(
        self,
        opcode: OpCode,
        callingConvention: CallingConventions,
        returnType: Type,
        parameterTypes: Array[Type],
        optionalParameterTypes: Array[Type],
    ) -> None:
        """

        :param opcode:
        :param callingConvention:
        :param returnType:
        :param parameterTypes:
        :param optionalParameterTypes:
        """
    @overload
    def EmitWriteLine(self, localBuilder: LocalBuilder) -> None:
        """

        :param localBuilder:
        """
    @overload
    def EmitWriteLine(self, fld: FieldInfo) -> None:
        """

        :param fld:
        """
    @overload
    def EmitWriteLine(self, value: str) -> None:
        """

        :param value:
        """
    def EndExceptionBlock(self) -> None:
        """"""
    def EndScope(self) -> None:
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
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def MarkLabel(self, loc: Label) -> None:
        """

        :param loc:
        """
    def MarkSequencePoint(
        self,
        document: ISymbolDocumentWriter,
        startLine: int,
        startColumn: int,
        endLine: int,
        endColumn: int,
    ) -> None:
        """

        :param document:
        :param startLine:
        :param startColumn:
        :param endLine:
        :param endColumn:
        """
    def ThrowException(self, excType: Type) -> None:
        """

        :param excType:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def UsingNamespace(self, usingNamespace: str) -> None:
        """

        :param usingNamespace:
        """

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
        """

        :return:
        """
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
        """

        :return:
        """
    @property
    def DefinedTypes(self) -> IEnumerable[TypeInfo]:
        """

        :return:
        """
    @property
    def EntryPoint(self) -> MethodInfo:
        """

        :return:
        """
    @property
    def EscapedCodeBase(self) -> str:
        """

        :return:
        """
    @property
    def Evidence(self) -> Evidence:
        """

        :return:
        """
    @property
    def Evidence(self) -> Evidence:
        """

        :return:
        """
    @property
    def ExportedTypes(self) -> IEnumerable[Type]:
        """

        :return:
        """
    @property
    def FullName(self) -> str:
        """

        :return:
        """
    @property
    def GlobalAssemblyCache(self) -> bool:
        """

        :return:
        """
    @property
    def HostContext(self) -> int:
        """

        :return:
        """
    @property
    def ImageRuntimeVersion(self) -> str:
        """

        :return:
        """
    @property
    def IsDynamic(self) -> bool:
        """

        :return:
        """
    @property
    def IsFullyTrusted(self) -> bool:
        """

        :return:
        """
    @property
    def Location(self) -> str:
        """

        :return:
        """
    @property
    def ManifestModule(self) -> Module:
        """

        :return:
        """
    @property
    def Modules(self) -> IEnumerable[Module]:
        """

        :return:
        """
    @property
    def PermissionSet(self) -> PermissionSet:
        """

        :return:
        """
    @property
    def ReflectionOnly(self) -> bool:
        """

        :return:
        """
    @property
    def SecurityRuleSet(self) -> SecurityRuleSet:
        """

        :return:
        """
    @overload
    def CreateInstance(self, typeName: str) -> object:
        """

        :param typeName:
        :return:
        """
    @overload
    def CreateInstance(self, typeName: str, ignoreCase: bool) -> object:
        """

        :param typeName:
        :param ignoreCase:
        :return:
        """
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
        """

        :param typeName:
        :param ignoreCase:
        :param bindingAttr:
        :param binder:
        :param args:
        :param culture:
        :param activationAttributes:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def Equals(self, other: object) -> bool:
        """

        :param other:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]:
        """

        :return:
        """
    def GetExportedTypes(self) -> Array[Type]:
        """

        :return:
        """
    def GetFile(self, name: str) -> FileStream:
        """

        :param name:
        :return:
        """
    @overload
    def GetFiles(self) -> Array[FileStream]:
        """

        :return:
        """
    @overload
    def GetFiles(self, getResourceModules: bool) -> Array[FileStream]:
        """

        :param getResourceModules:
        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetInterface(self, iid: Guid, ppv: IntPtr) -> Tuple[CustomQueryInterfaceResult, IntPtr]:
        """

        :param iid:
        :param ppv:
        :return:
        """
    @overload
    def GetLoadedModules(self) -> Array[Module]:
        """

        :return:
        """
    @overload
    def GetLoadedModules(self, getResourceModules: bool) -> Array[Module]:
        """

        :param getResourceModules:
        :return:
        """
    def GetManifestResourceInfo(self, resourceName: str) -> ManifestResourceInfo:
        """

        :param resourceName:
        :return:
        """
    def GetManifestResourceNames(self) -> Array[str]:
        """

        :return:
        """
    @overload
    def GetManifestResourceStream(self, name: str) -> Stream:
        """

        :param name:
        :return:
        """
    @overload
    def GetManifestResourceStream(self, type: Type, name: str) -> Stream:
        """

        :param type:
        :param name:
        :return:
        """
    def GetModule(self, name: str) -> Module:
        """

        :param name:
        :return:
        """
    @overload
    def GetModules(self) -> Array[Module]:
        """

        :return:
        """
    @overload
    def GetModules(self, getResourceModules: bool) -> Array[Module]:
        """

        :param getResourceModules:
        :return:
        """
    @overload
    def GetName(self) -> AssemblyName:
        """

        :return:
        """
    @overload
    def GetName(self, copiedName: bool) -> AssemblyName:
        """

        :param copiedName:
        :return:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    def GetReferencedAssemblies(self) -> Array[AssemblyName]:
        """

        :return:
        """
    @overload
    def GetSatelliteAssembly(self, culture: CultureInfo) -> Assembly:
        """

        :param culture:
        :return:
        """
    @overload
    def GetSatelliteAssembly(self, culture: CultureInfo, version: Version) -> Assembly:
        """

        :param culture:
        :param version:
        :return:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetType(self, name: str) -> Type:
        """

        :param name:
        :return:
        """
    @overload
    def GetType(self, name: str, throwOnError: bool) -> Type:
        """

        :param name:
        :param throwOnError:
        :return:
        """
    @overload
    def GetType(self, name: str, throwOnError: bool, ignoreCase: bool) -> Type:
        """

        :param name:
        :param throwOnError:
        :param ignoreCase:
        :return:
        """
    def GetTypes(self) -> Array[Type]:
        """

        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def LoadModule(self, moduleName: str, rawModule: Array[int]) -> Module:
        """

        :param moduleName:
        :param rawModule:
        :return:
        """
    @overload
    def LoadModule(
        self, moduleName: str, rawModule: Array[int], rawSymbolStore: Array[int]
    ) -> Module:
        """

        :param moduleName:
        :param rawModule:
        :param rawSymbolStore:
        :return:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """
    ModuleResolve: EventType[ModuleResolveEventHandler] = ...
    """"""

class InternalModuleBuilder(RuntimeModule, ICustomAttributeProvider, _Module, ISerializable):
    """"""

    @property
    def Assembly(self) -> Assembly:
        """

        :return:
        """
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
        """

        :return:
        """
    @property
    def FullyQualifiedName(self) -> str:
        """

        :return:
        """
    @property
    def MDStreamVersion(self) -> int:
        """

        :return:
        """
    @property
    def MetadataToken(self) -> int:
        """

        :return:
        """
    @property
    def ModuleHandle(self) -> ModuleHandle:
        """

        :return:
        """
    @property
    def ModuleVersionId(self) -> Guid:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def ScopeName(self) -> str:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def FindTypes(self, filter: TypeFilter, filterCriteria: object) -> Array[Type]:
        """

        :param filter:
        :param filterCriteria:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]:
        """

        :return:
        """
    @overload
    def GetField(self, name: str) -> FieldInfo:
        """

        :param name:
        :return:
        """
    @overload
    def GetField(self, name: str, bindingAttr: BindingFlags) -> FieldInfo:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetFields(self) -> Array[FieldInfo]:
        """

        :return:
        """
    @overload
    def GetFields(self, bindingFlags: BindingFlags) -> Array[FieldInfo]:
        """

        :param bindingFlags:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    @overload
    def GetMethod(self, name: str) -> MethodInfo:
        """

        :param name:
        :return:
        """
    @overload
    def GetMethod(self, name: str, types: Array[Type]) -> MethodInfo:
        """

        :param name:
        :param types:
        :return:
        """
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
        """

        :param name:
        :param bindingAttr:
        :param binder:
        :param callConvention:
        :param types:
        :param modifiers:
        :return:
        """
    @overload
    def GetMethods(self) -> Array[MethodInfo]:
        """

        :return:
        """
    @overload
    def GetMethods(self, bindingFlags: BindingFlags) -> Array[MethodInfo]:
        """

        :param bindingFlags:
        :return:
        """
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    def GetPEKind(
        self, peKind: PortableExecutableKinds, machine: ImageFileMachine
    ) -> Tuple[None, PortableExecutableKinds, ImageFileMachine]:
        """

        :param peKind:
        :param machine:
        """
    def GetSignerCertificate(self) -> X509Certificate:
        """

        :return:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetType(self, className: str) -> Type:
        """

        :param className:
        :return:
        """
    @overload
    def GetType(self, className: str, ignoreCase: bool) -> Type:
        """

        :param className:
        :param ignoreCase:
        :return:
        """
    @overload
    def GetType(self, className: str, throwOnError: bool, ignoreCase: bool) -> Type:
        """

        :param className:
        :param throwOnError:
        :param ignoreCase:
        :return:
        """
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    def GetTypes(self) -> Array[Type]:
        """

        :return:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    def IsResource(self) -> bool:
        """

        :return:
        """
    @overload
    def ResolveField(self, metadataToken: int) -> FieldInfo:
        """

        :param metadataToken:
        :return:
        """
    @overload
    def ResolveField(
        self,
        metadataToken: int,
        genericTypeArguments: Array[Type],
        genericMethodArguments: Array[Type],
    ) -> FieldInfo:
        """

        :param metadataToken:
        :param genericTypeArguments:
        :param genericMethodArguments:
        :return:
        """
    @overload
    def ResolveMember(self, metadataToken: int) -> MemberInfo:
        """

        :param metadataToken:
        :return:
        """
    @overload
    def ResolveMember(
        self,
        metadataToken: int,
        genericTypeArguments: Array[Type],
        genericMethodArguments: Array[Type],
    ) -> MemberInfo:
        """

        :param metadataToken:
        :param genericTypeArguments:
        :param genericMethodArguments:
        :return:
        """
    @overload
    def ResolveMethod(self, metadataToken: int) -> MethodBase:
        """

        :param metadataToken:
        :return:
        """
    @overload
    def ResolveMethod(
        self,
        metadataToken: int,
        genericTypeArguments: Array[Type],
        genericMethodArguments: Array[Type],
    ) -> MethodBase:
        """

        :param metadataToken:
        :param genericTypeArguments:
        :param genericMethodArguments:
        :return:
        """
    def ResolveSignature(self, metadataToken: int) -> Array[int]:
        """

        :param metadataToken:
        :return:
        """
    def ResolveString(self, metadataToken: int) -> str:
        """

        :param metadataToken:
        :return:
        """
    @overload
    def ResolveType(self, metadataToken: int) -> Type:
        """

        :param metadataToken:
        :return:
        """
    @overload
    def ResolveType(
        self,
        metadataToken: int,
        genericTypeArguments: Array[Type],
        genericMethodArguments: Array[Type],
    ) -> Type:
        """

        :param metadataToken:
        :param genericTypeArguments:
        :param genericMethodArguments:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class Label(ValueType):
    """"""

    @overload
    def Equals(self, obj: Label) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
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
    def __eq__(self, other: Label) -> bool:
        """

        :param other:
        :return:
        """
    def __ne__(self, other: Label) -> bool:
        """

        :param other:
        :return:
        """
    @classmethod
    def op_Equality(cls, a: Label, b: Label) -> bool:
        """

        :param a:
        :param b:
        :return:
        """
    @classmethod
    def op_Inequality(cls, a: Label, b: Label) -> bool:
        """

        :param a:
        :param b:
        :return:
        """

class LineNumberInfo(Object):
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

class LocalBuilder(LocalVariableInfo, _LocalBuilder):
    """"""

    @property
    def IsPinned(self) -> bool:
        """

        :return:
        """
    @property
    def LocalIndex(self) -> int:
        """

        :return:
        """
    @property
    def LocalType(self) -> Type:
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
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    @overload
    def SetLocalSymInfo(self, name: str) -> None:
        """

        :param name:
        """
    @overload
    def SetLocalSymInfo(self, name: str, startOffset: int, endOffset: int) -> None:
        """

        :param name:
        :param startOffset:
        :param endOffset:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class LocalSymInfo(Object):
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

class MethodBuilder(
    MethodInfo, ICustomAttributeProvider, _MemberInfo, _MethodBase, _MethodBuilder, _MethodInfo
):
    """"""

    @property
    def Attributes(self) -> MethodAttributes:
        """

        :return:
        """
    @property
    def Attributes(self) -> MethodAttributes:
        """

        :return:
        """
    @property
    def CallingConvention(self) -> CallingConventions:
        """

        :return:
        """
    @property
    def CallingConvention(self) -> CallingConventions:
        """

        :return:
        """
    @property
    def ContainsGenericParameters(self) -> bool:
        """

        :return:
        """
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
        """

        :return:
        """
    @property
    def DeclaringType(self) -> Type:
        """

        :return:
        """
    @property
    def DeclaringType(self) -> Type:
        """

        :return:
        """
    @property
    def DeclaringType(self) -> Type:
        """

        :return:
        """
    @property
    def InitLocals(self) -> bool:
        """

        :return:
        """
    @InitLocals.setter
    def InitLocals(self, value: bool) -> None: ...
    @property
    def IsAbstract(self) -> bool:
        """

        :return:
        """
    @property
    def IsAbstract(self) -> bool:
        """

        :return:
        """
    @property
    def IsAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsConstructor(self) -> bool:
        """

        :return:
        """
    @property
    def IsConstructor(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamily(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamily(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamilyAndAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamilyAndAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamilyOrAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamilyOrAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsFinal(self) -> bool:
        """

        :return:
        """
    @property
    def IsFinal(self) -> bool:
        """

        :return:
        """
    @property
    def IsGenericMethod(self) -> bool:
        """

        :return:
        """
    @property
    def IsGenericMethodDefinition(self) -> bool:
        """

        :return:
        """
    @property
    def IsHideBySig(self) -> bool:
        """

        :return:
        """
    @property
    def IsHideBySig(self) -> bool:
        """

        :return:
        """
    @property
    def IsPrivate(self) -> bool:
        """

        :return:
        """
    @property
    def IsPrivate(self) -> bool:
        """

        :return:
        """
    @property
    def IsPublic(self) -> bool:
        """

        :return:
        """
    @property
    def IsPublic(self) -> bool:
        """

        :return:
        """
    @property
    def IsSecurityCritical(self) -> bool:
        """

        :return:
        """
    @property
    def IsSecuritySafeCritical(self) -> bool:
        """

        :return:
        """
    @property
    def IsSecurityTransparent(self) -> bool:
        """

        :return:
        """
    @property
    def IsSpecialName(self) -> bool:
        """

        :return:
        """
    @property
    def IsSpecialName(self) -> bool:
        """

        :return:
        """
    @property
    def IsStatic(self) -> bool:
        """

        :return:
        """
    @property
    def IsStatic(self) -> bool:
        """

        :return:
        """
    @property
    def IsVirtual(self) -> bool:
        """

        :return:
        """
    @property
    def IsVirtual(self) -> bool:
        """

        :return:
        """
    @property
    def MemberType(self) -> MemberTypes:
        """

        :return:
        """
    @property
    def MemberType(self) -> MemberTypes:
        """

        :return:
        """
    @property
    def MemberType(self) -> MemberTypes:
        """

        :return:
        """
    @property
    def MetadataToken(self) -> int:
        """

        :return:
        """
    @property
    def MethodHandle(self) -> RuntimeMethodHandle:
        """

        :return:
        """
    @property
    def MethodHandle(self) -> RuntimeMethodHandle:
        """

        :return:
        """
    @property
    def MethodImplementationFlags(self) -> MethodImplAttributes:
        """

        :return:
        """
    @property
    def Module(self) -> Module:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def ReflectedType(self) -> Type:
        """

        :return:
        """
    @property
    def ReflectedType(self) -> Type:
        """

        :return:
        """
    @property
    def ReflectedType(self) -> Type:
        """

        :return:
        """
    @property
    def ReturnParameter(self) -> ParameterInfo:
        """

        :return:
        """
    @property
    def ReturnType(self) -> Type:
        """

        :return:
        """
    @property
    def ReturnTypeCustomAttributes(self) -> ICustomAttributeProvider:
        """

        :return:
        """
    @property
    def Signature(self) -> str:
        """

        :return:
        """
    def AddDeclarativeSecurity(self, action: SecurityAction, pset: PermissionSet) -> None:
        """

        :param action:
        :param pset:
        """
    @overload
    def CreateDelegate(self, delegateType: Type) -> Delegate:
        """

        :param delegateType:
        :return:
        """
    @overload
    def CreateDelegate(self, delegateType: Type, target: object) -> Delegate:
        """

        :param delegateType:
        :param target:
        :return:
        """
    def CreateMethodBody(self, il: Array[int], count: int) -> None:
        """

        :param il:
        :param count:
        """
    def DefineGenericParameters(self, names: Array[str]) -> Array[GenericTypeParameterBuilder]:
        """

        :param names:
        :return:
        """
    def DefineParameter(
        self, position: int, attributes: ParameterAttributes, strParamName: str
    ) -> ParameterBuilder:
        """

        :param position:
        :param attributes:
        :param strParamName:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def Equals(self, other: object) -> bool:
        """

        :param other:
        :return:
        """
    @overload
    def Equals(self, other: object) -> bool:
        """

        :param other:
        :return:
        """
    @overload
    def Equals(self, other: object) -> bool:
        """

        :param other:
        :return:
        """
    def GetBaseDefinition(self) -> MethodInfo:
        """

        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]:
        """

        :return:
        """
    def GetGenericArguments(self) -> Array[Type]:
        """

        :return:
        """
    def GetGenericMethodDefinition(self) -> MethodInfo:
        """

        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    @overload
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    @overload
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    @overload
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    @overload
    def GetILGenerator(self) -> ILGenerator:
        """

        :return:
        """
    @overload
    def GetILGenerator(self, size: int) -> ILGenerator:
        """

        :param size:
        :return:
        """
    def GetMethodBody(self) -> MethodBody:
        """

        :return:
        """
    @overload
    def GetMethodImplementationFlags(self) -> MethodImplAttributes:
        """

        :return:
        """
    @overload
    def GetMethodImplementationFlags(self) -> MethodImplAttributes:
        """

        :return:
        """
    def GetModule(self) -> Module:
        """

        :return:
        """
    @overload
    def GetParameters(self) -> Array[ParameterInfo]:
        """

        :return:
        """
    @overload
    def GetParameters(self) -> Array[ParameterInfo]:
        """

        :return:
        """
    def GetToken(self) -> MethodToken:
        """

        :return:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    @overload
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    @overload
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    @overload
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    @overload
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    @overload
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    @overload
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    @overload
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    @overload
    def Invoke(self, obj: object, parameters: Array[object]) -> object:
        """

        :param obj:
        :param parameters:
        :return:
        """
    @overload
    def Invoke(self, obj: object, parameters: Array[object]) -> object:
        """

        :param obj:
        :param parameters:
        :return:
        """
    @overload
    def Invoke(
        self,
        obj: object,
        invokeAttr: BindingFlags,
        binder: Binder,
        parameters: Array[object],
        culture: CultureInfo,
    ) -> object:
        """

        :param obj:
        :param invokeAttr:
        :param binder:
        :param parameters:
        :param culture:
        :return:
        """
    @overload
    def Invoke(
        self,
        obj: object,
        invokeAttr: BindingFlags,
        binder: Binder,
        parameters: Array[object],
        culture: CultureInfo,
    ) -> object:
        """

        :param obj:
        :param invokeAttr:
        :param binder:
        :param parameters:
        :param culture:
        :return:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    def MakeGenericMethod(self, typeArguments: Array[Type]) -> MethodInfo:
        """

        :param typeArguments:
        :return:
        """
    @overload
    def SetCustomAttribute(self, customBuilder: CustomAttributeBuilder) -> None:
        """

        :param customBuilder:
        """
    @overload
    def SetCustomAttribute(self, con: ConstructorInfo, binaryAttribute: Array[int]) -> None:
        """

        :param con:
        :param binaryAttribute:
        """
    def SetImplementationFlags(self, attributes: MethodImplAttributes) -> None:
        """

        :param attributes:
        """
    def SetMarshal(self, unmanagedMarshal: UnmanagedMarshal) -> None:
        """

        :param unmanagedMarshal:
        """
    def SetMethodBody(
        self,
        il: Array[int],
        maxStack: int,
        localSignature: Array[int],
        exceptionHandlers: IEnumerable[ExceptionHandler],
        tokenFixups: IEnumerable[int],
    ) -> None:
        """

        :param il:
        :param maxStack:
        :param localSignature:
        :param exceptionHandlers:
        :param tokenFixups:
        """
    def SetParameters(self, parameterTypes: Array[Type]) -> None:
        """

        :param parameterTypes:
        """
    def SetReturnType(self, returnType: Type) -> None:
        """

        :param returnType:
        """
    def SetSignature(
        self,
        returnType: Type,
        returnTypeRequiredCustomModifiers: Array[Type],
        returnTypeOptionalCustomModifiers: Array[Type],
        parameterTypes: Array[Type],
        parameterTypeRequiredCustomModifiers: Array[Type],
        parameterTypeOptionalCustomModifiers: Array[Type],
    ) -> None:
        """

        :param returnType:
        :param returnTypeRequiredCustomModifiers:
        :param returnTypeOptionalCustomModifiers:
        :param parameterTypes:
        :param parameterTypeRequiredCustomModifiers:
        :param parameterTypeOptionalCustomModifiers:
        """
    def SetSymCustomAttribute(self, name: str, data: Array[int]) -> None:
        """

        :param name:
        :param data:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """

class MethodBuilderInstantiation(
    MethodInfo, ICustomAttributeProvider, _MemberInfo, _MethodBase, _MethodInfo
):
    """"""

    @property
    def Attributes(self) -> MethodAttributes:
        """

        :return:
        """
    @property
    def Attributes(self) -> MethodAttributes:
        """

        :return:
        """
    @property
    def CallingConvention(self) -> CallingConventions:
        """

        :return:
        """
    @property
    def CallingConvention(self) -> CallingConventions:
        """

        :return:
        """
    @property
    def ContainsGenericParameters(self) -> bool:
        """

        :return:
        """
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
        """

        :return:
        """
    @property
    def DeclaringType(self) -> Type:
        """

        :return:
        """
    @property
    def DeclaringType(self) -> Type:
        """

        :return:
        """
    @property
    def DeclaringType(self) -> Type:
        """

        :return:
        """
    @property
    def IsAbstract(self) -> bool:
        """

        :return:
        """
    @property
    def IsAbstract(self) -> bool:
        """

        :return:
        """
    @property
    def IsAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsConstructor(self) -> bool:
        """

        :return:
        """
    @property
    def IsConstructor(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamily(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamily(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamilyAndAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamilyAndAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamilyOrAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamilyOrAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsFinal(self) -> bool:
        """

        :return:
        """
    @property
    def IsFinal(self) -> bool:
        """

        :return:
        """
    @property
    def IsGenericMethod(self) -> bool:
        """

        :return:
        """
    @property
    def IsGenericMethodDefinition(self) -> bool:
        """

        :return:
        """
    @property
    def IsHideBySig(self) -> bool:
        """

        :return:
        """
    @property
    def IsHideBySig(self) -> bool:
        """

        :return:
        """
    @property
    def IsPrivate(self) -> bool:
        """

        :return:
        """
    @property
    def IsPrivate(self) -> bool:
        """

        :return:
        """
    @property
    def IsPublic(self) -> bool:
        """

        :return:
        """
    @property
    def IsPublic(self) -> bool:
        """

        :return:
        """
    @property
    def IsSecurityCritical(self) -> bool:
        """

        :return:
        """
    @property
    def IsSecuritySafeCritical(self) -> bool:
        """

        :return:
        """
    @property
    def IsSecurityTransparent(self) -> bool:
        """

        :return:
        """
    @property
    def IsSpecialName(self) -> bool:
        """

        :return:
        """
    @property
    def IsSpecialName(self) -> bool:
        """

        :return:
        """
    @property
    def IsStatic(self) -> bool:
        """

        :return:
        """
    @property
    def IsStatic(self) -> bool:
        """

        :return:
        """
    @property
    def IsVirtual(self) -> bool:
        """

        :return:
        """
    @property
    def IsVirtual(self) -> bool:
        """

        :return:
        """
    @property
    def MemberType(self) -> MemberTypes:
        """

        :return:
        """
    @property
    def MemberType(self) -> MemberTypes:
        """

        :return:
        """
    @property
    def MemberType(self) -> MemberTypes:
        """

        :return:
        """
    @property
    def MetadataToken(self) -> int:
        """

        :return:
        """
    @property
    def MethodHandle(self) -> RuntimeMethodHandle:
        """

        :return:
        """
    @property
    def MethodHandle(self) -> RuntimeMethodHandle:
        """

        :return:
        """
    @property
    def MethodImplementationFlags(self) -> MethodImplAttributes:
        """

        :return:
        """
    @property
    def Module(self) -> Module:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def ReflectedType(self) -> Type:
        """

        :return:
        """
    @property
    def ReflectedType(self) -> Type:
        """

        :return:
        """
    @property
    def ReflectedType(self) -> Type:
        """

        :return:
        """
    @property
    def ReturnParameter(self) -> ParameterInfo:
        """

        :return:
        """
    @property
    def ReturnType(self) -> Type:
        """

        :return:
        """
    @property
    def ReturnTypeCustomAttributes(self) -> ICustomAttributeProvider:
        """

        :return:
        """
    @overload
    def CreateDelegate(self, delegateType: Type) -> Delegate:
        """

        :param delegateType:
        :return:
        """
    @overload
    def CreateDelegate(self, delegateType: Type, target: object) -> Delegate:
        """

        :param delegateType:
        :param target:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def Equals(self, other: object) -> bool:
        """

        :param other:
        :return:
        """
    @overload
    def Equals(self, other: object) -> bool:
        """

        :param other:
        :return:
        """
    @overload
    def Equals(self, other: object) -> bool:
        """

        :param other:
        :return:
        """
    def GetBaseDefinition(self) -> MethodInfo:
        """

        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]:
        """

        :return:
        """
    def GetGenericArguments(self) -> Array[Type]:
        """

        :return:
        """
    def GetGenericMethodDefinition(self) -> MethodInfo:
        """

        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    @overload
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    @overload
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetMethodBody(self) -> MethodBody:
        """

        :return:
        """
    @overload
    def GetMethodImplementationFlags(self) -> MethodImplAttributes:
        """

        :return:
        """
    @overload
    def GetMethodImplementationFlags(self) -> MethodImplAttributes:
        """

        :return:
        """
    @overload
    def GetParameters(self) -> Array[ParameterInfo]:
        """

        :return:
        """
    @overload
    def GetParameters(self) -> Array[ParameterInfo]:
        """

        :return:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    @overload
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    @overload
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    @overload
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    @overload
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    @overload
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    @overload
    def Invoke(self, obj: object, parameters: Array[object]) -> object:
        """

        :param obj:
        :param parameters:
        :return:
        """
    @overload
    def Invoke(self, obj: object, parameters: Array[object]) -> object:
        """

        :param obj:
        :param parameters:
        :return:
        """
    @overload
    def Invoke(
        self,
        obj: object,
        invokeAttr: BindingFlags,
        binder: Binder,
        parameters: Array[object],
        culture: CultureInfo,
    ) -> object:
        """

        :param obj:
        :param invokeAttr:
        :param binder:
        :param parameters:
        :param culture:
        :return:
        """
    @overload
    def Invoke(
        self,
        obj: object,
        invokeAttr: BindingFlags,
        binder: Binder,
        parameters: Array[object],
        culture: CultureInfo,
    ) -> object:
        """

        :param obj:
        :param invokeAttr:
        :param binder:
        :param parameters:
        :param culture:
        :return:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    def MakeGenericMethod(self, typeArguments: Array[Type]) -> MethodInfo:
        """

        :param typeArguments:
        :return:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """

class MethodOnTypeBuilderInstantiation(
    MethodInfo, ICustomAttributeProvider, _MemberInfo, _MethodBase, _MethodInfo
):
    """"""

    @property
    def Attributes(self) -> MethodAttributes:
        """

        :return:
        """
    @property
    def Attributes(self) -> MethodAttributes:
        """

        :return:
        """
    @property
    def CallingConvention(self) -> CallingConventions:
        """

        :return:
        """
    @property
    def CallingConvention(self) -> CallingConventions:
        """

        :return:
        """
    @property
    def ContainsGenericParameters(self) -> bool:
        """

        :return:
        """
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
        """

        :return:
        """
    @property
    def DeclaringType(self) -> Type:
        """

        :return:
        """
    @property
    def DeclaringType(self) -> Type:
        """

        :return:
        """
    @property
    def DeclaringType(self) -> Type:
        """

        :return:
        """
    @property
    def IsAbstract(self) -> bool:
        """

        :return:
        """
    @property
    def IsAbstract(self) -> bool:
        """

        :return:
        """
    @property
    def IsAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsConstructor(self) -> bool:
        """

        :return:
        """
    @property
    def IsConstructor(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamily(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamily(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamilyAndAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamilyAndAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamilyOrAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamilyOrAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsFinal(self) -> bool:
        """

        :return:
        """
    @property
    def IsFinal(self) -> bool:
        """

        :return:
        """
    @property
    def IsGenericMethod(self) -> bool:
        """

        :return:
        """
    @property
    def IsGenericMethodDefinition(self) -> bool:
        """

        :return:
        """
    @property
    def IsHideBySig(self) -> bool:
        """

        :return:
        """
    @property
    def IsHideBySig(self) -> bool:
        """

        :return:
        """
    @property
    def IsPrivate(self) -> bool:
        """

        :return:
        """
    @property
    def IsPrivate(self) -> bool:
        """

        :return:
        """
    @property
    def IsPublic(self) -> bool:
        """

        :return:
        """
    @property
    def IsPublic(self) -> bool:
        """

        :return:
        """
    @property
    def IsSecurityCritical(self) -> bool:
        """

        :return:
        """
    @property
    def IsSecuritySafeCritical(self) -> bool:
        """

        :return:
        """
    @property
    def IsSecurityTransparent(self) -> bool:
        """

        :return:
        """
    @property
    def IsSpecialName(self) -> bool:
        """

        :return:
        """
    @property
    def IsSpecialName(self) -> bool:
        """

        :return:
        """
    @property
    def IsStatic(self) -> bool:
        """

        :return:
        """
    @property
    def IsStatic(self) -> bool:
        """

        :return:
        """
    @property
    def IsVirtual(self) -> bool:
        """

        :return:
        """
    @property
    def IsVirtual(self) -> bool:
        """

        :return:
        """
    @property
    def MemberType(self) -> MemberTypes:
        """

        :return:
        """
    @property
    def MemberType(self) -> MemberTypes:
        """

        :return:
        """
    @property
    def MemberType(self) -> MemberTypes:
        """

        :return:
        """
    @property
    def MetadataToken(self) -> int:
        """

        :return:
        """
    @property
    def MethodHandle(self) -> RuntimeMethodHandle:
        """

        :return:
        """
    @property
    def MethodHandle(self) -> RuntimeMethodHandle:
        """

        :return:
        """
    @property
    def MethodImplementationFlags(self) -> MethodImplAttributes:
        """

        :return:
        """
    @property
    def Module(self) -> Module:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def ReflectedType(self) -> Type:
        """

        :return:
        """
    @property
    def ReflectedType(self) -> Type:
        """

        :return:
        """
    @property
    def ReflectedType(self) -> Type:
        """

        :return:
        """
    @property
    def ReturnParameter(self) -> ParameterInfo:
        """

        :return:
        """
    @property
    def ReturnType(self) -> Type:
        """

        :return:
        """
    @property
    def ReturnTypeCustomAttributes(self) -> ICustomAttributeProvider:
        """

        :return:
        """
    @overload
    def CreateDelegate(self, delegateType: Type) -> Delegate:
        """

        :param delegateType:
        :return:
        """
    @overload
    def CreateDelegate(self, delegateType: Type, target: object) -> Delegate:
        """

        :param delegateType:
        :param target:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def Equals(self, other: object) -> bool:
        """

        :param other:
        :return:
        """
    @overload
    def Equals(self, other: object) -> bool:
        """

        :param other:
        :return:
        """
    @overload
    def Equals(self, other: object) -> bool:
        """

        :param other:
        :return:
        """
    def GetBaseDefinition(self) -> MethodInfo:
        """

        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]:
        """

        :return:
        """
    def GetGenericArguments(self) -> Array[Type]:
        """

        :return:
        """
    def GetGenericMethodDefinition(self) -> MethodInfo:
        """

        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    @overload
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    @overload
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetMethodBody(self) -> MethodBody:
        """

        :return:
        """
    @overload
    def GetMethodImplementationFlags(self) -> MethodImplAttributes:
        """

        :return:
        """
    @overload
    def GetMethodImplementationFlags(self) -> MethodImplAttributes:
        """

        :return:
        """
    @overload
    def GetParameters(self) -> Array[ParameterInfo]:
        """

        :return:
        """
    @overload
    def GetParameters(self) -> Array[ParameterInfo]:
        """

        :return:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    @overload
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    @overload
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    @overload
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    @overload
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    @overload
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    @overload
    def Invoke(self, obj: object, parameters: Array[object]) -> object:
        """

        :param obj:
        :param parameters:
        :return:
        """
    @overload
    def Invoke(self, obj: object, parameters: Array[object]) -> object:
        """

        :param obj:
        :param parameters:
        :return:
        """
    @overload
    def Invoke(
        self,
        obj: object,
        invokeAttr: BindingFlags,
        binder: Binder,
        parameters: Array[object],
        culture: CultureInfo,
    ) -> object:
        """

        :param obj:
        :param invokeAttr:
        :param binder:
        :param parameters:
        :param culture:
        :return:
        """
    @overload
    def Invoke(
        self,
        obj: object,
        invokeAttr: BindingFlags,
        binder: Binder,
        parameters: Array[object],
        culture: CultureInfo,
    ) -> object:
        """

        :param obj:
        :param invokeAttr:
        :param binder:
        :param parameters:
        :param culture:
        :return:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    def MakeGenericMethod(self, typeArguments: Array[Type]) -> MethodInfo:
        """

        :param typeArguments:
        :return:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """

class MethodRental(Object, _MethodRental):
    """"""

    JitImmediate: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    JitOnDemand: Final[ClassVar[int]] = ...
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
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    @classmethod
    def SwapMethodBody(
        cls, cls: Type, methodtoken: int, rgIL: IntPtr, methodSize: int, flags: int
    ) -> None:
        """

        :param cls:
        :param methodtoken:
        :param rgIL:
        :param methodSize:
        :param flags:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class MethodToken(ValueType):
    """"""

    Empty: Final[ClassVar[MethodToken]] = ...
    """
    
    :return: 
    """
    @property
    def Token(self) -> int:
        """

        :return:
        """
    @overload
    def Equals(self, obj: MethodToken) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
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
    def __eq__(self, other: MethodToken) -> bool:
        """

        :param other:
        :return:
        """
    def __ne__(self, other: MethodToken) -> bool:
        """

        :param other:
        :return:
        """
    @classmethod
    def op_Equality(cls, a: MethodToken, b: MethodToken) -> bool:
        """

        :param a:
        :param b:
        :return:
        """
    @classmethod
    def op_Inequality(cls, a: MethodToken, b: MethodToken) -> bool:
        """

        :param a:
        :param b:
        :return:
        """

class ModuleBuilder(Module, ICustomAttributeProvider, _Module, _ModuleBuilder, ISerializable):
    """"""

    @property
    def Assembly(self) -> Assembly:
        """

        :return:
        """
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
        """

        :return:
        """
    @property
    def FullyQualifiedName(self) -> str:
        """

        :return:
        """
    @property
    def MDStreamVersion(self) -> int:
        """

        :return:
        """
    @property
    def MetadataToken(self) -> int:
        """

        :return:
        """
    @property
    def ModuleHandle(self) -> ModuleHandle:
        """

        :return:
        """
    @property
    def ModuleVersionId(self) -> Guid:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def ScopeName(self) -> str:
        """

        :return:
        """
    def CreateGlobalFunctions(self) -> None:
        """"""
    def DefineDocument(
        self, url: str, language: Guid, languageVendor: Guid, documentType: Guid
    ) -> ISymbolDocumentWriter:
        """

        :param url:
        :param language:
        :param languageVendor:
        :param documentType:
        :return:
        """
    def DefineEnum(
        self, name: str, visibility: TypeAttributes, underlyingType: Type
    ) -> EnumBuilder:
        """

        :param name:
        :param visibility:
        :param underlyingType:
        :return:
        """
    @overload
    def DefineGlobalMethod(
        self, name: str, attributes: MethodAttributes, returnType: Type, parameterTypes: Array[Type]
    ) -> MethodBuilder:
        """

        :param name:
        :param attributes:
        :param returnType:
        :param parameterTypes:
        :return:
        """
    @overload
    def DefineGlobalMethod(
        self,
        name: str,
        attributes: MethodAttributes,
        callingConvention: CallingConventions,
        returnType: Type,
        parameterTypes: Array[Type],
    ) -> MethodBuilder:
        """

        :param name:
        :param attributes:
        :param callingConvention:
        :param returnType:
        :param parameterTypes:
        :return:
        """
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
        requiredParameterTypeCustomModifiers: Array[Type],
        optionalParameterTypeCustomModifiers: Array[Type],
    ) -> MethodBuilder:
        """

        :param name:
        :param attributes:
        :param callingConvention:
        :param returnType:
        :param requiredReturnTypeCustomModifiers:
        :param optionalReturnTypeCustomModifiers:
        :param parameterTypes:
        :param requiredParameterTypeCustomModifiers:
        :param optionalParameterTypeCustomModifiers:
        :return:
        """
    def DefineInitializedData(
        self, name: str, data: Array[int], attributes: FieldAttributes
    ) -> FieldBuilder:
        """

        :param name:
        :param data:
        :param attributes:
        :return:
        """
    def DefineManifestResource(
        self, name: str, stream: Stream, attribute: ResourceAttributes
    ) -> None:
        """

        :param name:
        :param stream:
        :param attribute:
        """
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
        """

        :param name:
        :param dllName:
        :param attributes:
        :param callingConvention:
        :param returnType:
        :param parameterTypes:
        :param nativeCallConv:
        :param nativeCharSet:
        :return:
        """
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
        """

        :param name:
        :param dllName:
        :param entryName:
        :param attributes:
        :param callingConvention:
        :param returnType:
        :param parameterTypes:
        :param nativeCallConv:
        :param nativeCharSet:
        :return:
        """
    @overload
    def DefineResource(self, name: str, description: str) -> IResourceWriter:
        """

        :param name:
        :param description:
        :return:
        """
    @overload
    def DefineResource(
        self, name: str, description: str, attribute: ResourceAttributes
    ) -> IResourceWriter:
        """

        :param name:
        :param description:
        :param attribute:
        :return:
        """
    @overload
    def DefineType(self, name: str) -> TypeBuilder:
        """

        :param name:
        :return:
        """
    @overload
    def DefineType(self, name: str, attr: TypeAttributes) -> TypeBuilder:
        """

        :param name:
        :param attr:
        :return:
        """
    @overload
    def DefineType(self, name: str, attr: TypeAttributes, parent: Type) -> TypeBuilder:
        """

        :param name:
        :param attr:
        :param parent:
        :return:
        """
    @overload
    def DefineType(
        self, name: str, attr: TypeAttributes, parent: Type, packsize: PackingSize
    ) -> TypeBuilder:
        """

        :param name:
        :param attr:
        :param parent:
        :param packsize:
        :return:
        """
    @overload
    def DefineType(
        self, name: str, attr: TypeAttributes, parent: Type, interfaces: Array[Type]
    ) -> TypeBuilder:
        """

        :param name:
        :param attr:
        :param parent:
        :param interfaces:
        :return:
        """
    @overload
    def DefineType(
        self, name: str, attr: TypeAttributes, parent: Type, typesize: int
    ) -> TypeBuilder:
        """

        :param name:
        :param attr:
        :param parent:
        :param typesize:
        :return:
        """
    @overload
    def DefineType(
        self, name: str, attr: TypeAttributes, parent: Type, packingSize: PackingSize, typesize: int
    ) -> TypeBuilder:
        """

        :param name:
        :param attr:
        :param parent:
        :param packingSize:
        :param typesize:
        :return:
        """
    def DefineUninitializedData(
        self, name: str, size: int, attributes: FieldAttributes
    ) -> FieldBuilder:
        """

        :param name:
        :param size:
        :param attributes:
        :return:
        """
    @overload
    def DefineUnmanagedResource(self, resource: Array[int]) -> None:
        """

        :param resource:
        """
    @overload
    def DefineUnmanagedResource(self, resourceFileName: str) -> None:
        """

        :param resourceFileName:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def FindTypes(self, filter: TypeFilter, filterCriteria: object) -> Array[Type]:
        """

        :param filter:
        :param filterCriteria:
        :return:
        """
    def GetArrayMethod(
        self,
        arrayClass: Type,
        methodName: str,
        callingConvention: CallingConventions,
        returnType: Type,
        parameterTypes: Array[Type],
    ) -> MethodInfo:
        """

        :param arrayClass:
        :param methodName:
        :param callingConvention:
        :param returnType:
        :param parameterTypes:
        :return:
        """
    def GetArrayMethodToken(
        self,
        arrayClass: Type,
        methodName: str,
        callingConvention: CallingConventions,
        returnType: Type,
        parameterTypes: Array[Type],
    ) -> MethodToken:
        """

        :param arrayClass:
        :param methodName:
        :param callingConvention:
        :param returnType:
        :param parameterTypes:
        :return:
        """
    @overload
    def GetConstructorToken(self, con: ConstructorInfo) -> MethodToken:
        """

        :param con:
        :return:
        """
    @overload
    def GetConstructorToken(
        self, constructor: ConstructorInfo, optionalParameterTypes: IEnumerable[Type]
    ) -> MethodToken:
        """

        :param constructor:
        :param optionalParameterTypes:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]:
        """

        :return:
        """
    @overload
    def GetField(self, name: str) -> FieldInfo:
        """

        :param name:
        :return:
        """
    @overload
    def GetField(self, name: str, bindingAttr: BindingFlags) -> FieldInfo:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    def GetFieldToken(self, field: FieldInfo) -> FieldToken:
        """

        :param field:
        :return:
        """
    @overload
    def GetFields(self) -> Array[FieldInfo]:
        """

        :return:
        """
    @overload
    def GetFields(self, bindingFlags: BindingFlags) -> Array[FieldInfo]:
        """

        :param bindingFlags:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    @overload
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    @overload
    def GetMethod(self, name: str) -> MethodInfo:
        """

        :param name:
        :return:
        """
    @overload
    def GetMethod(self, name: str, types: Array[Type]) -> MethodInfo:
        """

        :param name:
        :param types:
        :return:
        """
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
        """

        :param name:
        :param bindingAttr:
        :param binder:
        :param callConvention:
        :param types:
        :param modifiers:
        :return:
        """
    @overload
    def GetMethodToken(self, method: MethodInfo) -> MethodToken:
        """

        :param method:
        :return:
        """
    @overload
    def GetMethodToken(
        self, method: MethodInfo, optionalParameterTypes: IEnumerable[Type]
    ) -> MethodToken:
        """

        :param method:
        :param optionalParameterTypes:
        :return:
        """
    @overload
    def GetMethods(self) -> Array[MethodInfo]:
        """

        :return:
        """
    @overload
    def GetMethods(self, bindingFlags: BindingFlags) -> Array[MethodInfo]:
        """

        :param bindingFlags:
        :return:
        """
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    def GetPEKind(
        self, peKind: PortableExecutableKinds, machine: ImageFileMachine
    ) -> Tuple[None, PortableExecutableKinds, ImageFileMachine]:
        """

        :param peKind:
        :param machine:
        """
    @overload
    def GetSignatureToken(self, sigHelper: SignatureHelper) -> SignatureToken:
        """

        :param sigHelper:
        :return:
        """
    @overload
    def GetSignatureToken(self, sigBytes: Array[int], sigLength: int) -> SignatureToken:
        """

        :param sigBytes:
        :param sigLength:
        :return:
        """
    def GetSignerCertificate(self) -> X509Certificate:
        """

        :return:
        """
    def GetStringConstant(self, str: str) -> StringToken:
        """

        :param str:
        :return:
        """
    def GetSymWriter(self) -> ISymbolWriter:
        """

        :return:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetType(self, className: str) -> Type:
        """

        :param className:
        :return:
        """
    @overload
    def GetType(self, className: str, ignoreCase: bool) -> Type:
        """

        :param className:
        :param ignoreCase:
        :return:
        """
    @overload
    def GetType(self, className: str, throwOnError: bool, ignoreCase: bool) -> Type:
        """

        :param className:
        :param throwOnError:
        :param ignoreCase:
        :return:
        """
    @overload
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    @overload
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    @overload
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    @overload
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    @overload
    def GetTypeToken(self, name: str) -> TypeToken:
        """

        :param name:
        :return:
        """
    @overload
    def GetTypeToken(self, type: Type) -> TypeToken:
        """

        :param type:
        :return:
        """
    def GetTypes(self) -> Array[Type]:
        """

        :return:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    def IsResource(self) -> bool:
        """

        :return:
        """
    def IsTransient(self) -> bool:
        """

        :return:
        """
    @overload
    def ResolveField(self, metadataToken: int) -> FieldInfo:
        """

        :param metadataToken:
        :return:
        """
    @overload
    def ResolveField(
        self,
        metadataToken: int,
        genericTypeArguments: Array[Type],
        genericMethodArguments: Array[Type],
    ) -> FieldInfo:
        """

        :param metadataToken:
        :param genericTypeArguments:
        :param genericMethodArguments:
        :return:
        """
    @overload
    def ResolveMember(self, metadataToken: int) -> MemberInfo:
        """

        :param metadataToken:
        :return:
        """
    @overload
    def ResolveMember(
        self,
        metadataToken: int,
        genericTypeArguments: Array[Type],
        genericMethodArguments: Array[Type],
    ) -> MemberInfo:
        """

        :param metadataToken:
        :param genericTypeArguments:
        :param genericMethodArguments:
        :return:
        """
    @overload
    def ResolveMethod(self, metadataToken: int) -> MethodBase:
        """

        :param metadataToken:
        :return:
        """
    @overload
    def ResolveMethod(
        self,
        metadataToken: int,
        genericTypeArguments: Array[Type],
        genericMethodArguments: Array[Type],
    ) -> MethodBase:
        """

        :param metadataToken:
        :param genericTypeArguments:
        :param genericMethodArguments:
        :return:
        """
    def ResolveSignature(self, metadataToken: int) -> Array[int]:
        """

        :param metadataToken:
        :return:
        """
    def ResolveString(self, metadataToken: int) -> str:
        """

        :param metadataToken:
        :return:
        """
    @overload
    def ResolveType(self, metadataToken: int) -> Type:
        """

        :param metadataToken:
        :return:
        """
    @overload
    def ResolveType(
        self,
        metadataToken: int,
        genericTypeArguments: Array[Type],
        genericMethodArguments: Array[Type],
    ) -> Type:
        """

        :param metadataToken:
        :param genericTypeArguments:
        :param genericMethodArguments:
        :return:
        """
    @overload
    def SetCustomAttribute(self, customBuilder: CustomAttributeBuilder) -> None:
        """

        :param customBuilder:
        """
    @overload
    def SetCustomAttribute(self, con: ConstructorInfo, binaryAttribute: Array[int]) -> None:
        """

        :param con:
        :param binaryAttribute:
        """
    def SetSymCustomAttribute(self, name: str, data: Array[int]) -> None:
        """

        :param name:
        :param data:
        """
    def SetUserEntryPoint(self, entryPoint: MethodInfo) -> None:
        """

        :param entryPoint:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class ModuleBuilderData(Object):
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

class NativeVersionInfo(Object):
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

class OpCode(ValueType):
    """"""

    @property
    def FlowControl(self) -> FlowControl:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def OpCodeType(self) -> OpCodeType:
        """

        :return:
        """
    @property
    def OperandType(self) -> OperandType:
        """

        :return:
        """
    @property
    def Size(self) -> int:
        """

        :return:
        """
    @property
    def StackBehaviourPop(self) -> StackBehaviour:
        """

        :return:
        """
    @property
    def StackBehaviourPush(self) -> StackBehaviour:
        """

        :return:
        """
    @property
    def Value(self) -> int:
        """

        :return:
        """
    @overload
    def Equals(self, obj: OpCode) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
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
    def __eq__(self, other: OpCode) -> bool:
        """

        :param other:
        :return:
        """
    def __ne__(self, other: OpCode) -> bool:
        """

        :param other:
        :return:
        """
    @classmethod
    def op_Equality(cls, a: OpCode, b: OpCode) -> bool:
        """

        :param a:
        :param b:
        :return:
        """
    @classmethod
    def op_Inequality(cls, a: OpCode, b: OpCode) -> bool:
        """

        :param a:
        :param b:
        :return:
        """

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

    Add: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Add_Ovf: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Add_Ovf_Un: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    And: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Arglist: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Beq: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Beq_S: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Bge: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Bge_S: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Bge_Un: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Bge_Un_S: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Bgt: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Bgt_S: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Bgt_Un: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Bgt_Un_S: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Ble: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Ble_S: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Ble_Un: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Ble_Un_S: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Blt: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Blt_S: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Blt_Un: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Blt_Un_S: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Bne_Un: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Bne_Un_S: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Box: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Br: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Br_S: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Break: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Brfalse: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Brfalse_S: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Brtrue: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Brtrue_S: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Call: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Calli: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Callvirt: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Castclass: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Ceq: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Cgt: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Cgt_Un: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Ckfinite: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Clt: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Clt_Un: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Constrained: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Conv_I: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Conv_I1: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Conv_I2: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Conv_I4: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Conv_I8: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Conv_Ovf_I: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Conv_Ovf_I1: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Conv_Ovf_I1_Un: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Conv_Ovf_I2: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Conv_Ovf_I2_Un: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Conv_Ovf_I4: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Conv_Ovf_I4_Un: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Conv_Ovf_I8: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Conv_Ovf_I8_Un: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Conv_Ovf_I_Un: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Conv_Ovf_U: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Conv_Ovf_U1: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Conv_Ovf_U1_Un: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Conv_Ovf_U2: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Conv_Ovf_U2_Un: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Conv_Ovf_U4: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Conv_Ovf_U4_Un: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Conv_Ovf_U8: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Conv_Ovf_U8_Un: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Conv_Ovf_U_Un: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Conv_R4: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Conv_R8: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Conv_R_Un: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Conv_U: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Conv_U1: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Conv_U2: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Conv_U4: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Conv_U8: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Cpblk: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Cpobj: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Div: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Div_Un: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Dup: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Endfilter: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Endfinally: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Initblk: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Initobj: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Isinst: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Jmp: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Ldarg: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Ldarg_0: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Ldarg_1: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Ldarg_2: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Ldarg_3: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Ldarg_S: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Ldarga: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Ldarga_S: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Ldc_I4: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Ldc_I4_0: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Ldc_I4_1: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Ldc_I4_2: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Ldc_I4_3: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Ldc_I4_4: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Ldc_I4_5: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Ldc_I4_6: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Ldc_I4_7: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Ldc_I4_8: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Ldc_I4_M1: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Ldc_I4_S: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Ldc_I8: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Ldc_R4: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Ldc_R8: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Ldelem: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Ldelem_I: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Ldelem_I1: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Ldelem_I2: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Ldelem_I4: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Ldelem_I8: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Ldelem_R4: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Ldelem_R8: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Ldelem_Ref: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Ldelem_U1: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Ldelem_U2: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Ldelem_U4: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Ldelema: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Ldfld: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Ldflda: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Ldftn: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Ldind_I: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Ldind_I1: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Ldind_I2: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Ldind_I4: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Ldind_I8: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Ldind_R4: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Ldind_R8: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Ldind_Ref: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Ldind_U1: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Ldind_U2: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Ldind_U4: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Ldlen: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Ldloc: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Ldloc_0: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Ldloc_1: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Ldloc_2: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Ldloc_3: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Ldloc_S: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Ldloca: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Ldloca_S: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Ldnull: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Ldobj: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Ldsfld: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Ldsflda: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Ldstr: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Ldtoken: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Ldvirtftn: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Leave: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Leave_S: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Localloc: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Mkrefany: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Mul: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Mul_Ovf: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Mul_Ovf_Un: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Neg: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Newarr: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Newobj: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Nop: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Not: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Or: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Pop: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Prefix1: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Prefix2: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Prefix3: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Prefix4: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Prefix5: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Prefix6: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Prefix7: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Prefixref: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Readonly: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Refanytype: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Refanyval: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Rem: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Rem_Un: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Ret: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Rethrow: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Shl: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Shr: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Shr_Un: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Sizeof: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Starg: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Starg_S: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Stelem: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Stelem_I: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Stelem_I1: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Stelem_I2: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Stelem_I4: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Stelem_I8: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Stelem_R4: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Stelem_R8: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Stelem_Ref: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Stfld: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Stind_I: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Stind_I1: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Stind_I2: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Stind_I4: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Stind_I8: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Stind_R4: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Stind_R8: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Stind_Ref: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Stloc: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Stloc_0: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Stloc_1: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Stloc_2: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Stloc_3: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Stloc_S: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Stobj: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Stsfld: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Sub: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Sub_Ovf: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Sub_Ovf_Un: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Switch: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Tailcall: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Throw: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Unaligned: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Unbox: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Unbox_Any: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Volatile: Final[ClassVar[OpCode]] = ...
    """
    
    :return: 
    """
    Xor: Final[ClassVar[OpCode]] = ...
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
    def TakesSingleByteArgument(cls, inst: OpCode) -> bool:
        """

        :param inst:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

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
        """

        :return:
        """
    @property
    def IsIn(self) -> bool:
        """

        :return:
        """
    @property
    def IsOptional(self) -> bool:
        """

        :return:
        """
    @property
    def IsOut(self) -> bool:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Position(self) -> int:
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
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetToken(self) -> ParameterToken:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def SetConstant(self, defaultValue: object) -> None:
        """

        :param defaultValue:
        """
    @overload
    def SetCustomAttribute(self, customBuilder: CustomAttributeBuilder) -> None:
        """

        :param customBuilder:
        """
    @overload
    def SetCustomAttribute(self, con: ConstructorInfo, binaryAttribute: Array[int]) -> None:
        """

        :param con:
        :param binaryAttribute:
        """
    def SetMarshal(self, unmanagedMarshal: UnmanagedMarshal) -> None:
        """

        :param unmanagedMarshal:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class ParameterToken(ValueType):
    """"""

    Empty: Final[ClassVar[ParameterToken]] = ...
    """
    
    :return: 
    """
    @property
    def Token(self) -> int:
        """

        :return:
        """
    @overload
    def Equals(self, obj: ParameterToken) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
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
    def __eq__(self, other: ParameterToken) -> bool:
        """

        :param other:
        :return:
        """
    def __ne__(self, other: ParameterToken) -> bool:
        """

        :param other:
        :return:
        """
    @classmethod
    def op_Equality(cls, a: ParameterToken, b: ParameterToken) -> bool:
        """

        :param a:
        :param b:
        :return:
        """
    @classmethod
    def op_Inequality(cls, a: ParameterToken, b: ParameterToken) -> bool:
        """

        :param a:
        :param b:
        :return:
        """

class PropertyBuilder(
    PropertyInfo, ICustomAttributeProvider, _MemberInfo, _PropertyBuilder, _PropertyInfo
):
    """"""

    @property
    def Attributes(self) -> PropertyAttributes:
        """

        :return:
        """
    @property
    def CanRead(self) -> bool:
        """

        :return:
        """
    @property
    def CanWrite(self) -> bool:
        """

        :return:
        """
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
        """

        :return:
        """
    @property
    def DeclaringType(self) -> Type:
        """

        :return:
        """
    @property
    def DeclaringType(self) -> Type:
        """

        :return:
        """
    @property
    def GetMethod(self) -> MethodInfo:
        """

        :return:
        """
    @property
    def IsSpecialName(self) -> bool:
        """

        :return:
        """
    @property
    def MemberType(self) -> MemberTypes:
        """

        :return:
        """
    @property
    def MemberType(self) -> MemberTypes:
        """

        :return:
        """
    @property
    def MetadataToken(self) -> int:
        """

        :return:
        """
    @property
    def Module(self) -> Module:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def PropertyToken(self) -> PropertyToken:
        """

        :return:
        """
    @property
    def PropertyType(self) -> Type:
        """

        :return:
        """
    @property
    def ReflectedType(self) -> Type:
        """

        :return:
        """
    @property
    def ReflectedType(self) -> Type:
        """

        :return:
        """
    @property
    def SetMethod(self) -> MethodInfo:
        """

        :return:
        """
    def AddOtherMethod(self, mdBuilder: MethodBuilder) -> None:
        """

        :param mdBuilder:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def Equals(self, other: object) -> bool:
        """

        :param other:
        :return:
        """
    @overload
    def Equals(self, other: object) -> bool:
        """

        :param other:
        :return:
        """
    @overload
    def GetAccessors(self) -> Array[MethodInfo]:
        """

        :return:
        """
    @overload
    def GetAccessors(self, nonPublic: bool) -> Array[MethodInfo]:
        """

        :param nonPublic:
        :return:
        """
    def GetConstantValue(self) -> object:
        """

        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]:
        """

        :return:
        """
    @overload
    def GetGetMethod(self) -> MethodInfo:
        """

        :return:
        """
    @overload
    def GetGetMethod(self, nonPublic: bool) -> MethodInfo:
        """

        :param nonPublic:
        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    @overload
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    @overload
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetIndexParameters(self) -> Array[ParameterInfo]:
        """

        :return:
        """
    def GetOptionalCustomModifiers(self) -> Array[Type]:
        """

        :return:
        """
    def GetRawConstantValue(self) -> object:
        """

        :return:
        """
    def GetRequiredCustomModifiers(self) -> Array[Type]:
        """

        :return:
        """
    @overload
    def GetSetMethod(self) -> MethodInfo:
        """

        :return:
        """
    @overload
    def GetSetMethod(self, nonPublic: bool) -> MethodInfo:
        """

        :param nonPublic:
        :return:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    @overload
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    @overload
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    @overload
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    @overload
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    @overload
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    @overload
    def GetValue(self, obj: object) -> object:
        """

        :param obj:
        :return:
        """
    @overload
    def GetValue(self, obj: object, index: Array[object]) -> object:
        """

        :param obj:
        :param index:
        :return:
        """
    @overload
    def GetValue(
        self,
        obj: object,
        invokeAttr: BindingFlags,
        binder: Binder,
        index: Array[object],
        culture: CultureInfo,
    ) -> object:
        """

        :param obj:
        :param invokeAttr:
        :param binder:
        :param index:
        :param culture:
        :return:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    def SetConstant(self, defaultValue: object) -> None:
        """

        :param defaultValue:
        """
    @overload
    def SetCustomAttribute(self, customBuilder: CustomAttributeBuilder) -> None:
        """

        :param customBuilder:
        """
    @overload
    def SetCustomAttribute(self, con: ConstructorInfo, binaryAttribute: Array[int]) -> None:
        """

        :param con:
        :param binaryAttribute:
        """
    def SetGetMethod(self, mdBuilder: MethodBuilder) -> None:
        """

        :param mdBuilder:
        """
    def SetSetMethod(self, mdBuilder: MethodBuilder) -> None:
        """

        :param mdBuilder:
        """
    @overload
    def SetValue(self, obj: object, value: object) -> None:
        """

        :param obj:
        :param value:
        """
    @overload
    def SetValue(self, obj: object, value: object, index: Array[object]) -> None:
        """

        :param obj:
        :param value:
        :param index:
        """
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
        """

        :param obj:
        :param value:
        :param invokeAttr:
        :param binder:
        :param index:
        :param culture:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """

class PropertyToken(ValueType):
    """"""

    Empty: Final[ClassVar[PropertyToken]] = ...
    """
    
    :return: 
    """
    @property
    def Token(self) -> int:
        """

        :return:
        """
    @overload
    def Equals(self, obj: PropertyToken) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
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
    def __eq__(self, other: PropertyToken) -> bool:
        """

        :param other:
        :return:
        """
    def __ne__(self, other: PropertyToken) -> bool:
        """

        :param other:
        :return:
        """
    @classmethod
    def op_Equality(cls, a: PropertyToken, b: PropertyToken) -> bool:
        """

        :param a:
        :param b:
        :return:
        """
    @classmethod
    def op_Inequality(cls, a: PropertyToken, b: PropertyToken) -> bool:
        """

        :param a:
        :param b:
        :return:
        """

class REDocument(Object):
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

class ResWriterData(Object):
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

class ScopeAction(Enum):
    """"""

    Open: ScopeAction = ...
    """"""
    Close: ScopeAction = ...
    """"""

class ScopeTree(Object):
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

class SignatureHelper(Object, _SignatureHelper):
    """"""

    @overload
    def AddArgument(self, clsArgument: Type) -> None:
        """

        :param clsArgument:
        """
    @overload
    def AddArgument(self, argument: Type, pinned: bool) -> None:
        """

        :param argument:
        :param pinned:
        """
    @overload
    def AddArgument(
        self,
        argument: Type,
        requiredCustomModifiers: Array[Type],
        optionalCustomModifiers: Array[Type],
    ) -> None:
        """

        :param argument:
        :param requiredCustomModifiers:
        :param optionalCustomModifiers:
        """
    def AddArguments(
        self,
        arguments: Array[Type],
        requiredCustomModifiers: Array[Type],
        optionalCustomModifiers: Array[Type],
    ) -> None:
        """

        :param arguments:
        :param requiredCustomModifiers:
        :param optionalCustomModifiers:
        """
    def AddSentinel(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @classmethod
    def GetFieldSigHelper(cls, mod: Module) -> SignatureHelper:
        """

        :param mod:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    @classmethod
    @overload
    def GetLocalVarSigHelper(cls) -> SignatureHelper:
        """

        :return:
        """
    @classmethod
    @overload
    def GetLocalVarSigHelper(cls, mod: Module) -> SignatureHelper:
        """

        :param mod:
        :return:
        """
    @classmethod
    @overload
    def GetMethodSigHelper(
        cls, callingConvention: CallingConventions, returnType: Type
    ) -> SignatureHelper:
        """

        :param callingConvention:
        :param returnType:
        :return:
        """
    @classmethod
    @overload
    def GetMethodSigHelper(
        cls, unmanagedCallingConvention: CallingConvention, returnType: Type
    ) -> SignatureHelper:
        """

        :param unmanagedCallingConvention:
        :param returnType:
        :return:
        """
    @classmethod
    @overload
    def GetMethodSigHelper(
        cls, mod: Module, callingConvention: CallingConventions, returnType: Type
    ) -> SignatureHelper:
        """

        :param mod:
        :param callingConvention:
        :param returnType:
        :return:
        """
    @classmethod
    @overload
    def GetMethodSigHelper(
        cls, mod: Module, unmanagedCallConv: CallingConvention, returnType: Type
    ) -> SignatureHelper:
        """

        :param mod:
        :param unmanagedCallConv:
        :param returnType:
        :return:
        """
    @classmethod
    @overload
    def GetMethodSigHelper(
        cls, mod: Module, returnType: Type, parameterTypes: Array[Type]
    ) -> SignatureHelper:
        """

        :param mod:
        :param returnType:
        :param parameterTypes:
        :return:
        """
    @classmethod
    @overload
    def GetPropertySigHelper(
        cls, mod: Module, returnType: Type, parameterTypes: Array[Type]
    ) -> SignatureHelper:
        """

        :param mod:
        :param returnType:
        :param parameterTypes:
        :return:
        """
    @classmethod
    @overload
    def GetPropertySigHelper(
        cls,
        mod: Module,
        returnType: Type,
        requiredReturnTypeCustomModifiers: Array[Type],
        optionalReturnTypeCustomModifiers: Array[Type],
        parameterTypes: Array[Type],
        requiredParameterTypeCustomModifiers: Array[Type],
        optionalParameterTypeCustomModifiers: Array[Type],
    ) -> SignatureHelper:
        """

        :param mod:
        :param returnType:
        :param requiredReturnTypeCustomModifiers:
        :param optionalReturnTypeCustomModifiers:
        :param parameterTypes:
        :param requiredParameterTypeCustomModifiers:
        :param optionalParameterTypeCustomModifiers:
        :return:
        """
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
        requiredParameterTypeCustomModifiers: Array[Type],
        optionalParameterTypeCustomModifiers: Array[Type],
    ) -> SignatureHelper:
        """

        :param mod:
        :param callingConvention:
        :param returnType:
        :param requiredReturnTypeCustomModifiers:
        :param optionalReturnTypeCustomModifiers:
        :param parameterTypes:
        :param requiredParameterTypeCustomModifiers:
        :param optionalParameterTypeCustomModifiers:
        :return:
        """
    def GetSignature(self) -> Array[int]:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class SignatureToken(ValueType):
    """"""

    Empty: Final[ClassVar[SignatureToken]] = ...
    """
    
    :return: 
    """
    @property
    def Token(self) -> int:
        """

        :return:
        """
    @overload
    def Equals(self, obj: SignatureToken) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
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
    def __eq__(self, other: SignatureToken) -> bool:
        """

        :param other:
        :return:
        """
    def __ne__(self, other: SignatureToken) -> bool:
        """

        :param other:
        :return:
        """
    @classmethod
    def op_Equality(cls, a: SignatureToken, b: SignatureToken) -> bool:
        """

        :param a:
        :param b:
        :return:
        """
    @classmethod
    def op_Inequality(cls, a: SignatureToken, b: SignatureToken) -> bool:
        """

        :param a:
        :param b:
        :return:
        """

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
        """

        :return:
        """
    @overload
    def Equals(self, obj: StringToken) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
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
    def __eq__(self, other: StringToken) -> bool:
        """

        :param other:
        :return:
        """
    def __ne__(self, other: StringToken) -> bool:
        """

        :param other:
        :return:
        """
    @classmethod
    def op_Equality(cls, a: StringToken, b: StringToken) -> bool:
        """

        :param a:
        :param b:
        :return:
        """
    @classmethod
    def op_Inequality(cls, a: StringToken, b: StringToken) -> bool:
        """

        :param a:
        :param b:
        :return:
        """

class SymbolMethod(MethodInfo, ICustomAttributeProvider, _MemberInfo, _MethodBase, _MethodInfo):
    """"""

    @property
    def Attributes(self) -> MethodAttributes:
        """

        :return:
        """
    @property
    def Attributes(self) -> MethodAttributes:
        """

        :return:
        """
    @property
    def CallingConvention(self) -> CallingConventions:
        """

        :return:
        """
    @property
    def CallingConvention(self) -> CallingConventions:
        """

        :return:
        """
    @property
    def ContainsGenericParameters(self) -> bool:
        """

        :return:
        """
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
        """

        :return:
        """
    @property
    def DeclaringType(self) -> Type:
        """

        :return:
        """
    @property
    def DeclaringType(self) -> Type:
        """

        :return:
        """
    @property
    def DeclaringType(self) -> Type:
        """

        :return:
        """
    @property
    def IsAbstract(self) -> bool:
        """

        :return:
        """
    @property
    def IsAbstract(self) -> bool:
        """

        :return:
        """
    @property
    def IsAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsConstructor(self) -> bool:
        """

        :return:
        """
    @property
    def IsConstructor(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamily(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamily(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamilyAndAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamilyAndAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamilyOrAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamilyOrAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsFinal(self) -> bool:
        """

        :return:
        """
    @property
    def IsFinal(self) -> bool:
        """

        :return:
        """
    @property
    def IsGenericMethod(self) -> bool:
        """

        :return:
        """
    @property
    def IsGenericMethodDefinition(self) -> bool:
        """

        :return:
        """
    @property
    def IsHideBySig(self) -> bool:
        """

        :return:
        """
    @property
    def IsHideBySig(self) -> bool:
        """

        :return:
        """
    @property
    def IsPrivate(self) -> bool:
        """

        :return:
        """
    @property
    def IsPrivate(self) -> bool:
        """

        :return:
        """
    @property
    def IsPublic(self) -> bool:
        """

        :return:
        """
    @property
    def IsPublic(self) -> bool:
        """

        :return:
        """
    @property
    def IsSecurityCritical(self) -> bool:
        """

        :return:
        """
    @property
    def IsSecuritySafeCritical(self) -> bool:
        """

        :return:
        """
    @property
    def IsSecurityTransparent(self) -> bool:
        """

        :return:
        """
    @property
    def IsSpecialName(self) -> bool:
        """

        :return:
        """
    @property
    def IsSpecialName(self) -> bool:
        """

        :return:
        """
    @property
    def IsStatic(self) -> bool:
        """

        :return:
        """
    @property
    def IsStatic(self) -> bool:
        """

        :return:
        """
    @property
    def IsVirtual(self) -> bool:
        """

        :return:
        """
    @property
    def IsVirtual(self) -> bool:
        """

        :return:
        """
    @property
    def MemberType(self) -> MemberTypes:
        """

        :return:
        """
    @property
    def MemberType(self) -> MemberTypes:
        """

        :return:
        """
    @property
    def MemberType(self) -> MemberTypes:
        """

        :return:
        """
    @property
    def MetadataToken(self) -> int:
        """

        :return:
        """
    @property
    def MethodHandle(self) -> RuntimeMethodHandle:
        """

        :return:
        """
    @property
    def MethodHandle(self) -> RuntimeMethodHandle:
        """

        :return:
        """
    @property
    def MethodImplementationFlags(self) -> MethodImplAttributes:
        """

        :return:
        """
    @property
    def Module(self) -> Module:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def ReflectedType(self) -> Type:
        """

        :return:
        """
    @property
    def ReflectedType(self) -> Type:
        """

        :return:
        """
    @property
    def ReflectedType(self) -> Type:
        """

        :return:
        """
    @property
    def ReturnParameter(self) -> ParameterInfo:
        """

        :return:
        """
    @property
    def ReturnType(self) -> Type:
        """

        :return:
        """
    @property
    def ReturnTypeCustomAttributes(self) -> ICustomAttributeProvider:
        """

        :return:
        """
    @overload
    def CreateDelegate(self, delegateType: Type) -> Delegate:
        """

        :param delegateType:
        :return:
        """
    @overload
    def CreateDelegate(self, delegateType: Type, target: object) -> Delegate:
        """

        :param delegateType:
        :param target:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def Equals(self, other: object) -> bool:
        """

        :param other:
        :return:
        """
    @overload
    def Equals(self, other: object) -> bool:
        """

        :param other:
        :return:
        """
    @overload
    def Equals(self, other: object) -> bool:
        """

        :param other:
        :return:
        """
    def GetBaseDefinition(self) -> MethodInfo:
        """

        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]:
        """

        :return:
        """
    def GetGenericArguments(self) -> Array[Type]:
        """

        :return:
        """
    def GetGenericMethodDefinition(self) -> MethodInfo:
        """

        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    @overload
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    @overload
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetMethodBody(self) -> MethodBody:
        """

        :return:
        """
    @overload
    def GetMethodImplementationFlags(self) -> MethodImplAttributes:
        """

        :return:
        """
    @overload
    def GetMethodImplementationFlags(self) -> MethodImplAttributes:
        """

        :return:
        """
    def GetModule(self) -> Module:
        """

        :return:
        """
    @overload
    def GetParameters(self) -> Array[ParameterInfo]:
        """

        :return:
        """
    @overload
    def GetParameters(self) -> Array[ParameterInfo]:
        """

        :return:
        """
    def GetToken(self) -> MethodToken:
        """

        :return:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    @overload
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    @overload
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    @overload
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    @overload
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    @overload
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    @overload
    def Invoke(self, obj: object, parameters: Array[object]) -> object:
        """

        :param obj:
        :param parameters:
        :return:
        """
    @overload
    def Invoke(self, obj: object, parameters: Array[object]) -> object:
        """

        :param obj:
        :param parameters:
        :return:
        """
    @overload
    def Invoke(
        self,
        obj: object,
        invokeAttr: BindingFlags,
        binder: Binder,
        parameters: Array[object],
        culture: CultureInfo,
    ) -> object:
        """

        :param obj:
        :param invokeAttr:
        :param binder:
        :param parameters:
        :param culture:
        :return:
        """
    @overload
    def Invoke(
        self,
        obj: object,
        invokeAttr: BindingFlags,
        binder: Binder,
        parameters: Array[object],
        culture: CultureInfo,
    ) -> object:
        """

        :param obj:
        :param invokeAttr:
        :param binder:
        :param parameters:
        :param culture:
        :return:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    def MakeGenericMethod(self, typeArguments: Array[Type]) -> MethodInfo:
        """

        :param typeArguments:
        :return:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """

class SymbolType(
    TypeInfo, ICustomAttributeProvider, IReflect, IReflectableType, _MemberInfo, _Type
):
    """"""

    @property
    def Assembly(self) -> Assembly:
        """

        :return:
        """
    @property
    def AssemblyQualifiedName(self) -> str:
        """

        :return:
        """
    @property
    def Attributes(self) -> TypeAttributes:
        """

        :return:
        """
    @property
    def BaseType(self) -> Type:
        """

        :return:
        """
    @property
    def ContainsGenericParameters(self) -> bool:
        """

        :return:
        """
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
        """

        :return:
        """
    @property
    def DeclaredConstructors(self) -> IEnumerable[ConstructorInfo]:
        """

        :return:
        """
    @property
    def DeclaredEvents(self) -> IEnumerable[EventInfo]:
        """

        :return:
        """
    @property
    def DeclaredFields(self) -> IEnumerable[FieldInfo]:
        """

        :return:
        """
    @property
    def DeclaredMembers(self) -> IEnumerable[MemberInfo]:
        """

        :return:
        """
    @property
    def DeclaredMethods(self) -> IEnumerable[MethodInfo]:
        """

        :return:
        """
    @property
    def DeclaredNestedTypes(self) -> IEnumerable[TypeInfo]:
        """

        :return:
        """
    @property
    def DeclaredProperties(self) -> IEnumerable[PropertyInfo]:
        """

        :return:
        """
    @property
    def DeclaringMethod(self) -> MethodBase:
        """

        :return:
        """
    @property
    def DeclaringType(self) -> Type:
        """

        :return:
        """
    @property
    def DeclaringType(self) -> Type:
        """

        :return:
        """
    @classmethod
    @property
    def DefaultBinder(cls) -> Binder:
        """

        :return:
        """
    @property
    def FullName(self) -> str:
        """

        :return:
        """
    @property
    def GUID(self) -> Guid:
        """

        :return:
        """
    @property
    def GenericParameterAttributes(self) -> GenericParameterAttributes:
        """

        :return:
        """
    @property
    def GenericParameterPosition(self) -> int:
        """

        :return:
        """
    @property
    def GenericTypeArguments(self) -> Array[Type]:
        """

        :return:
        """
    @property
    def GenericTypeParameters(self) -> Array[Type]:
        """

        :return:
        """
    @property
    def HasElementType(self) -> bool:
        """

        :return:
        """
    @property
    def ImplementedInterfaces(self) -> IEnumerable[Type]:
        """

        :return:
        """
    @property
    def IsAbstract(self) -> bool:
        """

        :return:
        """
    @property
    def IsAnsiClass(self) -> bool:
        """

        :return:
        """
    @property
    def IsArray(self) -> bool:
        """

        :return:
        """
    @property
    def IsAutoClass(self) -> bool:
        """

        :return:
        """
    @property
    def IsAutoLayout(self) -> bool:
        """

        :return:
        """
    @property
    def IsByRef(self) -> bool:
        """

        :return:
        """
    @property
    def IsCOMObject(self) -> bool:
        """

        :return:
        """
    @property
    def IsClass(self) -> bool:
        """

        :return:
        """
    @property
    def IsConstructedGenericType(self) -> bool:
        """

        :return:
        """
    @property
    def IsContextful(self) -> bool:
        """

        :return:
        """
    @property
    def IsEnum(self) -> bool:
        """

        :return:
        """
    @property
    def IsExplicitLayout(self) -> bool:
        """

        :return:
        """
    @property
    def IsGenericParameter(self) -> bool:
        """

        :return:
        """
    @property
    def IsGenericType(self) -> bool:
        """

        :return:
        """
    @property
    def IsGenericTypeDefinition(self) -> bool:
        """

        :return:
        """
    @property
    def IsImport(self) -> bool:
        """

        :return:
        """
    @property
    def IsInterface(self) -> bool:
        """

        :return:
        """
    @property
    def IsLayoutSequential(self) -> bool:
        """

        :return:
        """
    @property
    def IsMarshalByRef(self) -> bool:
        """

        :return:
        """
    @property
    def IsNested(self) -> bool:
        """

        :return:
        """
    @property
    def IsNestedAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsNestedFamANDAssem(self) -> bool:
        """

        :return:
        """
    @property
    def IsNestedFamORAssem(self) -> bool:
        """

        :return:
        """
    @property
    def IsNestedFamily(self) -> bool:
        """

        :return:
        """
    @property
    def IsNestedPrivate(self) -> bool:
        """

        :return:
        """
    @property
    def IsNestedPublic(self) -> bool:
        """

        :return:
        """
    @property
    def IsNotPublic(self) -> bool:
        """

        :return:
        """
    @property
    def IsPointer(self) -> bool:
        """

        :return:
        """
    @property
    def IsPrimitive(self) -> bool:
        """

        :return:
        """
    @property
    def IsPublic(self) -> bool:
        """

        :return:
        """
    @property
    def IsSealed(self) -> bool:
        """

        :return:
        """
    @property
    def IsSecurityCritical(self) -> bool:
        """

        :return:
        """
    @property
    def IsSecuritySafeCritical(self) -> bool:
        """

        :return:
        """
    @property
    def IsSecurityTransparent(self) -> bool:
        """

        :return:
        """
    @property
    def IsSerializable(self) -> bool:
        """

        :return:
        """
    @property
    def IsSpecialName(self) -> bool:
        """

        :return:
        """
    @property
    def IsUnicodeClass(self) -> bool:
        """

        :return:
        """
    @property
    def IsValueType(self) -> bool:
        """

        :return:
        """
    @property
    def IsVisible(self) -> bool:
        """

        :return:
        """
    @property
    def MemberType(self) -> MemberTypes:
        """

        :return:
        """
    @property
    def MemberType(self) -> MemberTypes:
        """

        :return:
        """
    @property
    def MetadataToken(self) -> int:
        """

        :return:
        """
    @property
    def Module(self) -> Module:
        """

        :return:
        """
    @property
    def Module(self) -> Module:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Namespace(self) -> str:
        """

        :return:
        """
    @property
    def ReflectedType(self) -> Type:
        """

        :return:
        """
    @property
    def ReflectedType(self) -> Type:
        """

        :return:
        """
    @property
    def StructLayoutAttribute(self) -> StructLayoutAttribute:
        """

        :return:
        """
    @property
    def TypeHandle(self) -> RuntimeTypeHandle:
        """

        :return:
        """
    @property
    def TypeInitializer(self) -> ConstructorInfo:
        """

        :return:
        """
    @property
    def UnderlyingSystemType(self) -> Type:
        """

        :return:
        """
    @property
    def UnderlyingSystemType(self) -> Type:
        """

        :return:
        """
    def AsType(self) -> Type:
        """

        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def Equals(self, other: object) -> bool:
        """

        :param other:
        :return:
        """
    @overload
    def Equals(self, other: object) -> bool:
        """

        :param other:
        :return:
        """
    @overload
    def Equals(self, o: Type) -> bool:
        """

        :param o:
        :return:
        """
    def FindInterfaces(self, filter: TypeFilter, filterCriteria: object) -> Array[Type]:
        """

        :param filter:
        :param filterCriteria:
        :return:
        """
    def FindMembers(
        self,
        memberType: MemberTypes,
        bindingAttr: BindingFlags,
        filter: MemberFilter,
        filterCriteria: object,
    ) -> Array[MemberInfo]:
        """

        :param memberType:
        :param bindingAttr:
        :param filter:
        :param filterCriteria:
        :return:
        """
    def GetArrayRank(self) -> int:
        """

        :return:
        """
    @overload
    def GetConstructor(self, types: Array[Type]) -> ConstructorInfo:
        """

        :param types:
        :return:
        """
    @overload
    def GetConstructor(
        self,
        bindingAttr: BindingFlags,
        binder: Binder,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> ConstructorInfo:
        """

        :param bindingAttr:
        :param binder:
        :param types:
        :param modifiers:
        :return:
        """
    @overload
    def GetConstructor(
        self,
        bindingAttr: BindingFlags,
        binder: Binder,
        callConvention: CallingConventions,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> ConstructorInfo:
        """

        :param bindingAttr:
        :param binder:
        :param callConvention:
        :param types:
        :param modifiers:
        :return:
        """
    @overload
    def GetConstructors(self) -> Array[ConstructorInfo]:
        """

        :return:
        """
    @overload
    def GetConstructors(self, bindingAttr: BindingFlags) -> Array[ConstructorInfo]:
        """

        :param bindingAttr:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]:
        """

        :return:
        """
    def GetDeclaredEvent(self, name: str) -> EventInfo:
        """

        :param name:
        :return:
        """
    def GetDeclaredField(self, name: str) -> FieldInfo:
        """

        :param name:
        :return:
        """
    def GetDeclaredMethod(self, name: str) -> MethodInfo:
        """

        :param name:
        :return:
        """
    def GetDeclaredMethods(self, name: str) -> IEnumerable[MethodInfo]:
        """

        :param name:
        :return:
        """
    def GetDeclaredNestedType(self, name: str) -> TypeInfo:
        """

        :param name:
        :return:
        """
    def GetDeclaredProperty(self, name: str) -> PropertyInfo:
        """

        :param name:
        :return:
        """
    def GetDefaultMembers(self) -> Array[MemberInfo]:
        """

        :return:
        """
    def GetElementType(self) -> Type:
        """

        :return:
        """
    def GetEnumName(self, value: object) -> str:
        """

        :param value:
        :return:
        """
    def GetEnumNames(self) -> Array[str]:
        """

        :return:
        """
    def GetEnumUnderlyingType(self) -> Type:
        """

        :return:
        """
    def GetEnumValues(self) -> Array:
        """

        :return:
        """
    @overload
    def GetEvent(self, name: str) -> EventInfo:
        """

        :param name:
        :return:
        """
    @overload
    def GetEvent(self, name: str, bindingAttr: BindingFlags) -> EventInfo:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetEvents(self) -> Array[EventInfo]:
        """

        :return:
        """
    @overload
    def GetEvents(self, bindingAttr: BindingFlags) -> Array[EventInfo]:
        """

        :param bindingAttr:
        :return:
        """
    @overload
    def GetField(self, name: str) -> FieldInfo:
        """

        :param name:
        :return:
        """
    @overload
    def GetField(self, name: str, bindingAttr: BindingFlags) -> FieldInfo:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetField(self, name: str, bindingAttr: BindingFlags) -> FieldInfo:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetFields(self) -> Array[FieldInfo]:
        """

        :return:
        """
    @overload
    def GetFields(self, bindingAttr: BindingFlags) -> Array[FieldInfo]:
        """

        :param bindingAttr:
        :return:
        """
    @overload
    def GetFields(self, bindingAttr: BindingFlags) -> Array[FieldInfo]:
        """

        :param bindingAttr:
        :return:
        """
    def GetGenericArguments(self) -> Array[Type]:
        """

        :return:
        """
    def GetGenericParameterConstraints(self) -> Array[Type]:
        """

        :return:
        """
    def GetGenericTypeDefinition(self) -> Type:
        """

        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    @overload
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    @overload
    def GetInterface(self, name: str) -> Type:
        """

        :param name:
        :return:
        """
    @overload
    def GetInterface(self, name: str, ignoreCase: bool) -> Type:
        """

        :param name:
        :param ignoreCase:
        :return:
        """
    def GetInterfaceMap(self, interfaceType: Type) -> InterfaceMapping:
        """

        :param interfaceType:
        :return:
        """
    def GetInterfaces(self) -> Array[Type]:
        """

        :return:
        """
    @overload
    def GetMember(self, name: str) -> Array[MemberInfo]:
        """

        :param name:
        :return:
        """
    @overload
    def GetMember(self, name: str, bindingAttr: BindingFlags) -> Array[MemberInfo]:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetMember(self, name: str, bindingAttr: BindingFlags) -> Array[MemberInfo]:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetMember(
        self, name: str, type: MemberTypes, bindingAttr: BindingFlags
    ) -> Array[MemberInfo]:
        """

        :param name:
        :param type:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetMembers(self) -> Array[MemberInfo]:
        """

        :return:
        """
    @overload
    def GetMembers(self, bindingAttr: BindingFlags) -> Array[MemberInfo]:
        """

        :param bindingAttr:
        :return:
        """
    @overload
    def GetMembers(self, bindingAttr: BindingFlags) -> Array[MemberInfo]:
        """

        :param bindingAttr:
        :return:
        """
    @overload
    def GetMethod(self, name: str) -> MethodInfo:
        """

        :param name:
        :return:
        """
    @overload
    def GetMethod(self, name: str, bindingAttr: BindingFlags) -> MethodInfo:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetMethod(self, name: str, bindingAttr: BindingFlags) -> MethodInfo:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetMethod(self, name: str, types: Array[Type]) -> MethodInfo:
        """

        :param name:
        :param types:
        :return:
        """
    @overload
    def GetMethod(
        self, name: str, types: Array[Type], modifiers: Array[ParameterModifier]
    ) -> MethodInfo:
        """

        :param name:
        :param types:
        :param modifiers:
        :return:
        """
    @overload
    def GetMethod(
        self,
        name: str,
        bindingAttr: BindingFlags,
        binder: Binder,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> MethodInfo:
        """

        :param name:
        :param bindingAttr:
        :param binder:
        :param types:
        :param modifiers:
        :return:
        """
    @overload
    def GetMethod(
        self,
        name: str,
        bindingAttr: BindingFlags,
        binder: Binder,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> MethodInfo:
        """

        :param name:
        :param bindingAttr:
        :param binder:
        :param types:
        :param modifiers:
        :return:
        """
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
        """

        :param name:
        :param bindingAttr:
        :param binder:
        :param callConvention:
        :param types:
        :param modifiers:
        :return:
        """
    @overload
    def GetMethods(self) -> Array[MethodInfo]:
        """

        :return:
        """
    @overload
    def GetMethods(self, bindingAttr: BindingFlags) -> Array[MethodInfo]:
        """

        :param bindingAttr:
        :return:
        """
    @overload
    def GetMethods(self, bindingAttr: BindingFlags) -> Array[MethodInfo]:
        """

        :param bindingAttr:
        :return:
        """
    @overload
    def GetNestedType(self, name: str) -> Type:
        """

        :param name:
        :return:
        """
    @overload
    def GetNestedType(self, name: str, bindingAttr: BindingFlags) -> Type:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetNestedTypes(self) -> Array[Type]:
        """

        :return:
        """
    @overload
    def GetNestedTypes(self, bindingAttr: BindingFlags) -> Array[Type]:
        """

        :param bindingAttr:
        :return:
        """
    @overload
    def GetProperties(self) -> Array[PropertyInfo]:
        """

        :return:
        """
    @overload
    def GetProperties(self, bindingAttr: BindingFlags) -> Array[PropertyInfo]:
        """

        :param bindingAttr:
        :return:
        """
    @overload
    def GetProperties(self, bindingAttr: BindingFlags) -> Array[PropertyInfo]:
        """

        :param bindingAttr:
        :return:
        """
    @overload
    def GetProperty(self, name: str) -> PropertyInfo:
        """

        :param name:
        :return:
        """
    @overload
    def GetProperty(self, name: str, bindingAttr: BindingFlags) -> PropertyInfo:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetProperty(self, name: str, bindingAttr: BindingFlags) -> PropertyInfo:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetProperty(self, name: str, types: Array[Type]) -> PropertyInfo:
        """

        :param name:
        :param types:
        :return:
        """
    @overload
    def GetProperty(self, name: str, returnType: Type) -> PropertyInfo:
        """

        :param name:
        :param returnType:
        :return:
        """
    @overload
    def GetProperty(self, name: str, returnType: Type, types: Array[Type]) -> PropertyInfo:
        """

        :param name:
        :param returnType:
        :param types:
        :return:
        """
    @overload
    def GetProperty(
        self, name: str, returnType: Type, types: Array[Type], modifiers: Array[ParameterModifier]
    ) -> PropertyInfo:
        """

        :param name:
        :param returnType:
        :param types:
        :param modifiers:
        :return:
        """
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
        """

        :param name:
        :param bindingAttr:
        :param binder:
        :param returnType:
        :param types:
        :param modifiers:
        :return:
        """
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
        """

        :param name:
        :param bindingAttr:
        :param binder:
        :param returnType:
        :param types:
        :param modifiers:
        :return:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetTypeInfo(self) -> TypeInfo:
        """

        :return:
        """
    @overload
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    @overload
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    @overload
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    @overload
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    @overload
    def InvokeMember(
        self,
        name: str,
        invokeAttr: BindingFlags,
        binder: Binder,
        target: object,
        args: Array[object],
    ) -> object:
        """

        :param name:
        :param invokeAttr:
        :param binder:
        :param target:
        :param args:
        :return:
        """
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
        """

        :param name:
        :param invokeAttr:
        :param binder:
        :param target:
        :param args:
        :param culture:
        :return:
        """
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
        """

        :param name:
        :param invokeAttr:
        :param binder:
        :param target:
        :param args:
        :param modifiers:
        :param culture:
        :param namedParameters:
        :return:
        """
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
        """

        :param name:
        :param invokeAttr:
        :param binder:
        :param target:
        :param args:
        :param modifiers:
        :param culture:
        :param namedParameters:
        :return:
        """
    @overload
    def IsAssignableFrom(self, typeInfo: TypeInfo) -> bool:
        """

        :param typeInfo:
        :return:
        """
    @overload
    def IsAssignableFrom(self, c: Type) -> bool:
        """

        :param c:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    def IsEnumDefined(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    def IsEquivalentTo(self, other: Type) -> bool:
        """

        :param other:
        :return:
        """
    def IsInstanceOfType(self, o: object) -> bool:
        """

        :param o:
        :return:
        """
    def IsSubclassOf(self, c: Type) -> bool:
        """

        :param c:
        :return:
        """
    @overload
    def MakeArrayType(self) -> Type:
        """

        :return:
        """
    @overload
    def MakeArrayType(self, rank: int) -> Type:
        """

        :param rank:
        :return:
        """
    def MakeByRefType(self) -> Type:
        """

        :return:
        """
    def MakeGenericType(self, typeArguments: Array[Type]) -> Type:
        """

        :param typeArguments:
        :return:
        """
    def MakePointerType(self) -> Type:
        """

        :return:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """

class TypeBuilder(
    TypeInfo, ICustomAttributeProvider, IReflect, IReflectableType, _MemberInfo, _Type, _TypeBuilder
):
    """"""

    UnspecifiedTypeSize: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    @property
    def Assembly(self) -> Assembly:
        """

        :return:
        """
    @property
    def AssemblyQualifiedName(self) -> str:
        """

        :return:
        """
    @property
    def Attributes(self) -> TypeAttributes:
        """

        :return:
        """
    @property
    def BaseType(self) -> Type:
        """

        :return:
        """
    @property
    def ContainsGenericParameters(self) -> bool:
        """

        :return:
        """
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
        """

        :return:
        """
    @property
    def DeclaredConstructors(self) -> IEnumerable[ConstructorInfo]:
        """

        :return:
        """
    @property
    def DeclaredEvents(self) -> IEnumerable[EventInfo]:
        """

        :return:
        """
    @property
    def DeclaredFields(self) -> IEnumerable[FieldInfo]:
        """

        :return:
        """
    @property
    def DeclaredMembers(self) -> IEnumerable[MemberInfo]:
        """

        :return:
        """
    @property
    def DeclaredMethods(self) -> IEnumerable[MethodInfo]:
        """

        :return:
        """
    @property
    def DeclaredNestedTypes(self) -> IEnumerable[TypeInfo]:
        """

        :return:
        """
    @property
    def DeclaredProperties(self) -> IEnumerable[PropertyInfo]:
        """

        :return:
        """
    @property
    def DeclaringMethod(self) -> MethodBase:
        """

        :return:
        """
    @property
    def DeclaringType(self) -> Type:
        """

        :return:
        """
    @property
    def DeclaringType(self) -> Type:
        """

        :return:
        """
    @classmethod
    @property
    def DefaultBinder(cls) -> Binder:
        """

        :return:
        """
    @property
    def FullName(self) -> str:
        """

        :return:
        """
    @property
    def GUID(self) -> Guid:
        """

        :return:
        """
    @property
    def GenericParameterAttributes(self) -> GenericParameterAttributes:
        """

        :return:
        """
    @property
    def GenericParameterPosition(self) -> int:
        """

        :return:
        """
    @property
    def GenericTypeArguments(self) -> Array[Type]:
        """

        :return:
        """
    @property
    def GenericTypeParameters(self) -> Array[Type]:
        """

        :return:
        """
    @property
    def HasElementType(self) -> bool:
        """

        :return:
        """
    @property
    def ImplementedInterfaces(self) -> IEnumerable[Type]:
        """

        :return:
        """
    @property
    def IsAbstract(self) -> bool:
        """

        :return:
        """
    @property
    def IsAnsiClass(self) -> bool:
        """

        :return:
        """
    @property
    def IsArray(self) -> bool:
        """

        :return:
        """
    @property
    def IsAutoClass(self) -> bool:
        """

        :return:
        """
    @property
    def IsAutoLayout(self) -> bool:
        """

        :return:
        """
    @property
    def IsByRef(self) -> bool:
        """

        :return:
        """
    @property
    def IsCOMObject(self) -> bool:
        """

        :return:
        """
    @property
    def IsClass(self) -> bool:
        """

        :return:
        """
    @property
    def IsConstructedGenericType(self) -> bool:
        """

        :return:
        """
    @property
    def IsContextful(self) -> bool:
        """

        :return:
        """
    @property
    def IsEnum(self) -> bool:
        """

        :return:
        """
    @property
    def IsExplicitLayout(self) -> bool:
        """

        :return:
        """
    @property
    def IsGenericParameter(self) -> bool:
        """

        :return:
        """
    @property
    def IsGenericType(self) -> bool:
        """

        :return:
        """
    @property
    def IsGenericTypeDefinition(self) -> bool:
        """

        :return:
        """
    @property
    def IsImport(self) -> bool:
        """

        :return:
        """
    @property
    def IsInterface(self) -> bool:
        """

        :return:
        """
    @property
    def IsLayoutSequential(self) -> bool:
        """

        :return:
        """
    @property
    def IsMarshalByRef(self) -> bool:
        """

        :return:
        """
    @property
    def IsNested(self) -> bool:
        """

        :return:
        """
    @property
    def IsNestedAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsNestedFamANDAssem(self) -> bool:
        """

        :return:
        """
    @property
    def IsNestedFamORAssem(self) -> bool:
        """

        :return:
        """
    @property
    def IsNestedFamily(self) -> bool:
        """

        :return:
        """
    @property
    def IsNestedPrivate(self) -> bool:
        """

        :return:
        """
    @property
    def IsNestedPublic(self) -> bool:
        """

        :return:
        """
    @property
    def IsNotPublic(self) -> bool:
        """

        :return:
        """
    @property
    def IsPointer(self) -> bool:
        """

        :return:
        """
    @property
    def IsPrimitive(self) -> bool:
        """

        :return:
        """
    @property
    def IsPublic(self) -> bool:
        """

        :return:
        """
    @property
    def IsSealed(self) -> bool:
        """

        :return:
        """
    @property
    def IsSecurityCritical(self) -> bool:
        """

        :return:
        """
    @property
    def IsSecuritySafeCritical(self) -> bool:
        """

        :return:
        """
    @property
    def IsSecurityTransparent(self) -> bool:
        """

        :return:
        """
    @property
    def IsSerializable(self) -> bool:
        """

        :return:
        """
    @property
    def IsSpecialName(self) -> bool:
        """

        :return:
        """
    @property
    def IsUnicodeClass(self) -> bool:
        """

        :return:
        """
    @property
    def IsValueType(self) -> bool:
        """

        :return:
        """
    @property
    def IsVisible(self) -> bool:
        """

        :return:
        """
    @property
    def MemberType(self) -> MemberTypes:
        """

        :return:
        """
    @property
    def MemberType(self) -> MemberTypes:
        """

        :return:
        """
    @property
    def MetadataToken(self) -> int:
        """

        :return:
        """
    @property
    def Module(self) -> Module:
        """

        :return:
        """
    @property
    def Module(self) -> Module:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Namespace(self) -> str:
        """

        :return:
        """
    @property
    def PackingSize(self) -> PackingSize:
        """

        :return:
        """
    @property
    def ReflectedType(self) -> Type:
        """

        :return:
        """
    @property
    def ReflectedType(self) -> Type:
        """

        :return:
        """
    @property
    def Size(self) -> int:
        """

        :return:
        """
    @property
    def StructLayoutAttribute(self) -> StructLayoutAttribute:
        """

        :return:
        """
    @property
    def TypeHandle(self) -> RuntimeTypeHandle:
        """

        :return:
        """
    @property
    def TypeInitializer(self) -> ConstructorInfo:
        """

        :return:
        """
    @property
    def TypeToken(self) -> TypeToken:
        """

        :return:
        """
    @property
    def UnderlyingSystemType(self) -> Type:
        """

        :return:
        """
    @property
    def UnderlyingSystemType(self) -> Type:
        """

        :return:
        """
    def AddDeclarativeSecurity(self, action: SecurityAction, pset: PermissionSet) -> None:
        """

        :param action:
        :param pset:
        """
    def AddInterfaceImplementation(self, interfaceType: Type) -> None:
        """

        :param interfaceType:
        """
    def AsType(self) -> Type:
        """

        :return:
        """
    def CreateType(self) -> Type:
        """

        :return:
        """
    def CreateTypeInfo(self) -> TypeInfo:
        """

        :return:
        """
    @overload
    def DefineConstructor(
        self,
        attributes: MethodAttributes,
        callingConvention: CallingConventions,
        parameterTypes: Array[Type],
    ) -> ConstructorBuilder:
        """

        :param attributes:
        :param callingConvention:
        :param parameterTypes:
        :return:
        """
    @overload
    def DefineConstructor(
        self,
        attributes: MethodAttributes,
        callingConvention: CallingConventions,
        parameterTypes: Array[Type],
        requiredCustomModifiers: Array[Type],
        optionalCustomModifiers: Array[Type],
    ) -> ConstructorBuilder:
        """

        :param attributes:
        :param callingConvention:
        :param parameterTypes:
        :param requiredCustomModifiers:
        :param optionalCustomModifiers:
        :return:
        """
    def DefineDefaultConstructor(self, attributes: MethodAttributes) -> ConstructorBuilder:
        """

        :param attributes:
        :return:
        """
    def DefineEvent(self, name: str, attributes: EventAttributes, eventtype: Type) -> EventBuilder:
        """

        :param name:
        :param attributes:
        :param eventtype:
        :return:
        """
    @overload
    def DefineField(self, fieldName: str, type: Type, attributes: FieldAttributes) -> FieldBuilder:
        """

        :param fieldName:
        :param type:
        :param attributes:
        :return:
        """
    @overload
    def DefineField(
        self,
        fieldName: str,
        type: Type,
        requiredCustomModifiers: Array[Type],
        optionalCustomModifiers: Array[Type],
        attributes: FieldAttributes,
    ) -> FieldBuilder:
        """

        :param fieldName:
        :param type:
        :param requiredCustomModifiers:
        :param optionalCustomModifiers:
        :param attributes:
        :return:
        """
    def DefineGenericParameters(self, names: Array[str]) -> Array[GenericTypeParameterBuilder]:
        """

        :param names:
        :return:
        """
    def DefineInitializedData(
        self, name: str, data: Array[int], attributes: FieldAttributes
    ) -> FieldBuilder:
        """

        :param name:
        :param data:
        :param attributes:
        :return:
        """
    @overload
    def DefineMethod(self, name: str, attributes: MethodAttributes) -> MethodBuilder:
        """

        :param name:
        :param attributes:
        :return:
        """
    @overload
    def DefineMethod(
        self, name: str, attributes: MethodAttributes, callingConvention: CallingConventions
    ) -> MethodBuilder:
        """

        :param name:
        :param attributes:
        :param callingConvention:
        :return:
        """
    @overload
    def DefineMethod(
        self, name: str, attributes: MethodAttributes, returnType: Type, parameterTypes: Array[Type]
    ) -> MethodBuilder:
        """

        :param name:
        :param attributes:
        :param returnType:
        :param parameterTypes:
        :return:
        """
    @overload
    def DefineMethod(
        self,
        name: str,
        attributes: MethodAttributes,
        callingConvention: CallingConventions,
        returnType: Type,
        parameterTypes: Array[Type],
    ) -> MethodBuilder:
        """

        :param name:
        :param attributes:
        :param callingConvention:
        :param returnType:
        :param parameterTypes:
        :return:
        """
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
        parameterTypeRequiredCustomModifiers: Array[Type],
        parameterTypeOptionalCustomModifiers: Array[Type],
    ) -> MethodBuilder:
        """

        :param name:
        :param attributes:
        :param callingConvention:
        :param returnType:
        :param returnTypeRequiredCustomModifiers:
        :param returnTypeOptionalCustomModifiers:
        :param parameterTypes:
        :param parameterTypeRequiredCustomModifiers:
        :param parameterTypeOptionalCustomModifiers:
        :return:
        """
    def DefineMethodOverride(
        self, methodInfoBody: MethodInfo, methodInfoDeclaration: MethodInfo
    ) -> None:
        """

        :param methodInfoBody:
        :param methodInfoDeclaration:
        """
    @overload
    def DefineNestedType(self, name: str) -> TypeBuilder:
        """

        :param name:
        :return:
        """
    @overload
    def DefineNestedType(self, name: str, attr: TypeAttributes) -> TypeBuilder:
        """

        :param name:
        :param attr:
        :return:
        """
    @overload
    def DefineNestedType(self, name: str, attr: TypeAttributes, parent: Type) -> TypeBuilder:
        """

        :param name:
        :param attr:
        :param parent:
        :return:
        """
    @overload
    def DefineNestedType(
        self, name: str, attr: TypeAttributes, parent: Type, packSize: PackingSize
    ) -> TypeBuilder:
        """

        :param name:
        :param attr:
        :param parent:
        :param packSize:
        :return:
        """
    @overload
    def DefineNestedType(
        self, name: str, attr: TypeAttributes, parent: Type, interfaces: Array[Type]
    ) -> TypeBuilder:
        """

        :param name:
        :param attr:
        :param parent:
        :param interfaces:
        :return:
        """
    @overload
    def DefineNestedType(
        self, name: str, attr: TypeAttributes, parent: Type, typeSize: int
    ) -> TypeBuilder:
        """

        :param name:
        :param attr:
        :param parent:
        :param typeSize:
        :return:
        """
    @overload
    def DefineNestedType(
        self, name: str, attr: TypeAttributes, parent: Type, packSize: PackingSize, typeSize: int
    ) -> TypeBuilder:
        """

        :param name:
        :param attr:
        :param parent:
        :param packSize:
        :param typeSize:
        :return:
        """
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
        """

        :param name:
        :param dllName:
        :param attributes:
        :param callingConvention:
        :param returnType:
        :param parameterTypes:
        :param nativeCallConv:
        :param nativeCharSet:
        :return:
        """
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
        """

        :param name:
        :param dllName:
        :param entryName:
        :param attributes:
        :param callingConvention:
        :param returnType:
        :param parameterTypes:
        :param nativeCallConv:
        :param nativeCharSet:
        :return:
        """
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
        parameterTypeRequiredCustomModifiers: Array[Type],
        parameterTypeOptionalCustomModifiers: Array[Type],
        nativeCallConv: CallingConvention,
        nativeCharSet: CharSet,
    ) -> MethodBuilder:
        """

        :param name:
        :param dllName:
        :param entryName:
        :param attributes:
        :param callingConvention:
        :param returnType:
        :param returnTypeRequiredCustomModifiers:
        :param returnTypeOptionalCustomModifiers:
        :param parameterTypes:
        :param parameterTypeRequiredCustomModifiers:
        :param parameterTypeOptionalCustomModifiers:
        :param nativeCallConv:
        :param nativeCharSet:
        :return:
        """
    @overload
    def DefineProperty(
        self,
        name: str,
        attributes: PropertyAttributes,
        returnType: Type,
        parameterTypes: Array[Type],
    ) -> PropertyBuilder:
        """

        :param name:
        :param attributes:
        :param returnType:
        :param parameterTypes:
        :return:
        """
    @overload
    def DefineProperty(
        self,
        name: str,
        attributes: PropertyAttributes,
        callingConvention: CallingConventions,
        returnType: Type,
        parameterTypes: Array[Type],
    ) -> PropertyBuilder:
        """

        :param name:
        :param attributes:
        :param callingConvention:
        :param returnType:
        :param parameterTypes:
        :return:
        """
    @overload
    def DefineProperty(
        self,
        name: str,
        attributes: PropertyAttributes,
        returnType: Type,
        returnTypeRequiredCustomModifiers: Array[Type],
        returnTypeOptionalCustomModifiers: Array[Type],
        parameterTypes: Array[Type],
        parameterTypeRequiredCustomModifiers: Array[Type],
        parameterTypeOptionalCustomModifiers: Array[Type],
    ) -> PropertyBuilder:
        """

        :param name:
        :param attributes:
        :param returnType:
        :param returnTypeRequiredCustomModifiers:
        :param returnTypeOptionalCustomModifiers:
        :param parameterTypes:
        :param parameterTypeRequiredCustomModifiers:
        :param parameterTypeOptionalCustomModifiers:
        :return:
        """
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
        parameterTypeRequiredCustomModifiers: Array[Type],
        parameterTypeOptionalCustomModifiers: Array[Type],
    ) -> PropertyBuilder:
        """

        :param name:
        :param attributes:
        :param callingConvention:
        :param returnType:
        :param returnTypeRequiredCustomModifiers:
        :param returnTypeOptionalCustomModifiers:
        :param parameterTypes:
        :param parameterTypeRequiredCustomModifiers:
        :param parameterTypeOptionalCustomModifiers:
        :return:
        """
    def DefineTypeInitializer(self) -> ConstructorBuilder:
        """

        :return:
        """
    def DefineUninitializedData(
        self, name: str, size: int, attributes: FieldAttributes
    ) -> FieldBuilder:
        """

        :param name:
        :param size:
        :param attributes:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def Equals(self, other: object) -> bool:
        """

        :param other:
        :return:
        """
    @overload
    def Equals(self, other: object) -> bool:
        """

        :param other:
        :return:
        """
    @overload
    def Equals(self, o: Type) -> bool:
        """

        :param o:
        :return:
        """
    def FindInterfaces(self, filter: TypeFilter, filterCriteria: object) -> Array[Type]:
        """

        :param filter:
        :param filterCriteria:
        :return:
        """
    def FindMembers(
        self,
        memberType: MemberTypes,
        bindingAttr: BindingFlags,
        filter: MemberFilter,
        filterCriteria: object,
    ) -> Array[MemberInfo]:
        """

        :param memberType:
        :param bindingAttr:
        :param filter:
        :param filterCriteria:
        :return:
        """
    def GetArrayRank(self) -> int:
        """

        :return:
        """
    @overload
    def GetConstructor(self, types: Array[Type]) -> ConstructorInfo:
        """

        :param types:
        :return:
        """
    @classmethod
    @overload
    def GetConstructor(cls, type: Type, constructor: ConstructorInfo) -> ConstructorInfo:
        """

        :param type:
        :param constructor:
        :return:
        """
    @overload
    def GetConstructor(
        self,
        bindingAttr: BindingFlags,
        binder: Binder,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> ConstructorInfo:
        """

        :param bindingAttr:
        :param binder:
        :param types:
        :param modifiers:
        :return:
        """
    @overload
    def GetConstructor(
        self,
        bindingAttr: BindingFlags,
        binder: Binder,
        callConvention: CallingConventions,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> ConstructorInfo:
        """

        :param bindingAttr:
        :param binder:
        :param callConvention:
        :param types:
        :param modifiers:
        :return:
        """
    @overload
    def GetConstructors(self) -> Array[ConstructorInfo]:
        """

        :return:
        """
    @overload
    def GetConstructors(self, bindingAttr: BindingFlags) -> Array[ConstructorInfo]:
        """

        :param bindingAttr:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]:
        """

        :return:
        """
    def GetDeclaredEvent(self, name: str) -> EventInfo:
        """

        :param name:
        :return:
        """
    def GetDeclaredField(self, name: str) -> FieldInfo:
        """

        :param name:
        :return:
        """
    def GetDeclaredMethod(self, name: str) -> MethodInfo:
        """

        :param name:
        :return:
        """
    def GetDeclaredMethods(self, name: str) -> IEnumerable[MethodInfo]:
        """

        :param name:
        :return:
        """
    def GetDeclaredNestedType(self, name: str) -> TypeInfo:
        """

        :param name:
        :return:
        """
    def GetDeclaredProperty(self, name: str) -> PropertyInfo:
        """

        :param name:
        :return:
        """
    def GetDefaultMembers(self) -> Array[MemberInfo]:
        """

        :return:
        """
    def GetElementType(self) -> Type:
        """

        :return:
        """
    def GetEnumName(self, value: object) -> str:
        """

        :param value:
        :return:
        """
    def GetEnumNames(self) -> Array[str]:
        """

        :return:
        """
    def GetEnumUnderlyingType(self) -> Type:
        """

        :return:
        """
    def GetEnumValues(self) -> Array:
        """

        :return:
        """
    @overload
    def GetEvent(self, name: str) -> EventInfo:
        """

        :param name:
        :return:
        """
    @overload
    def GetEvent(self, name: str, bindingAttr: BindingFlags) -> EventInfo:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetEvents(self) -> Array[EventInfo]:
        """

        :return:
        """
    @overload
    def GetEvents(self, bindingAttr: BindingFlags) -> Array[EventInfo]:
        """

        :param bindingAttr:
        :return:
        """
    @overload
    def GetField(self, name: str) -> FieldInfo:
        """

        :param name:
        :return:
        """
    @overload
    def GetField(self, name: str, bindingAttr: BindingFlags) -> FieldInfo:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetField(self, name: str, bindingAttr: BindingFlags) -> FieldInfo:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    @classmethod
    @overload
    def GetField(cls, type: Type, field: FieldInfo) -> FieldInfo:
        """

        :param type:
        :param field:
        :return:
        """
    @overload
    def GetFields(self) -> Array[FieldInfo]:
        """

        :return:
        """
    @overload
    def GetFields(self, bindingAttr: BindingFlags) -> Array[FieldInfo]:
        """

        :param bindingAttr:
        :return:
        """
    @overload
    def GetFields(self, bindingAttr: BindingFlags) -> Array[FieldInfo]:
        """

        :param bindingAttr:
        :return:
        """
    def GetGenericArguments(self) -> Array[Type]:
        """

        :return:
        """
    def GetGenericParameterConstraints(self) -> Array[Type]:
        """

        :return:
        """
    def GetGenericTypeDefinition(self) -> Type:
        """

        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    @overload
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    @overload
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    @overload
    def GetInterface(self, name: str) -> Type:
        """

        :param name:
        :return:
        """
    @overload
    def GetInterface(self, name: str, ignoreCase: bool) -> Type:
        """

        :param name:
        :param ignoreCase:
        :return:
        """
    def GetInterfaceMap(self, interfaceType: Type) -> InterfaceMapping:
        """

        :param interfaceType:
        :return:
        """
    def GetInterfaces(self) -> Array[Type]:
        """

        :return:
        """
    @overload
    def GetMember(self, name: str) -> Array[MemberInfo]:
        """

        :param name:
        :return:
        """
    @overload
    def GetMember(self, name: str, bindingAttr: BindingFlags) -> Array[MemberInfo]:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetMember(self, name: str, bindingAttr: BindingFlags) -> Array[MemberInfo]:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetMember(
        self, name: str, type: MemberTypes, bindingAttr: BindingFlags
    ) -> Array[MemberInfo]:
        """

        :param name:
        :param type:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetMembers(self) -> Array[MemberInfo]:
        """

        :return:
        """
    @overload
    def GetMembers(self, bindingAttr: BindingFlags) -> Array[MemberInfo]:
        """

        :param bindingAttr:
        :return:
        """
    @overload
    def GetMembers(self, bindingAttr: BindingFlags) -> Array[MemberInfo]:
        """

        :param bindingAttr:
        :return:
        """
    @overload
    def GetMethod(self, name: str) -> MethodInfo:
        """

        :param name:
        :return:
        """
    @overload
    def GetMethod(self, name: str, bindingAttr: BindingFlags) -> MethodInfo:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetMethod(self, name: str, bindingAttr: BindingFlags) -> MethodInfo:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetMethod(self, name: str, types: Array[Type]) -> MethodInfo:
        """

        :param name:
        :param types:
        :return:
        """
    @classmethod
    @overload
    def GetMethod(cls, type: Type, method: MethodInfo) -> MethodInfo:
        """

        :param type:
        :param method:
        :return:
        """
    @overload
    def GetMethod(
        self, name: str, types: Array[Type], modifiers: Array[ParameterModifier]
    ) -> MethodInfo:
        """

        :param name:
        :param types:
        :param modifiers:
        :return:
        """
    @overload
    def GetMethod(
        self,
        name: str,
        bindingAttr: BindingFlags,
        binder: Binder,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> MethodInfo:
        """

        :param name:
        :param bindingAttr:
        :param binder:
        :param types:
        :param modifiers:
        :return:
        """
    @overload
    def GetMethod(
        self,
        name: str,
        bindingAttr: BindingFlags,
        binder: Binder,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> MethodInfo:
        """

        :param name:
        :param bindingAttr:
        :param binder:
        :param types:
        :param modifiers:
        :return:
        """
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
        """

        :param name:
        :param bindingAttr:
        :param binder:
        :param callConvention:
        :param types:
        :param modifiers:
        :return:
        """
    @overload
    def GetMethods(self) -> Array[MethodInfo]:
        """

        :return:
        """
    @overload
    def GetMethods(self, bindingAttr: BindingFlags) -> Array[MethodInfo]:
        """

        :param bindingAttr:
        :return:
        """
    @overload
    def GetMethods(self, bindingAttr: BindingFlags) -> Array[MethodInfo]:
        """

        :param bindingAttr:
        :return:
        """
    @overload
    def GetNestedType(self, name: str) -> Type:
        """

        :param name:
        :return:
        """
    @overload
    def GetNestedType(self, name: str, bindingAttr: BindingFlags) -> Type:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetNestedTypes(self) -> Array[Type]:
        """

        :return:
        """
    @overload
    def GetNestedTypes(self, bindingAttr: BindingFlags) -> Array[Type]:
        """

        :param bindingAttr:
        :return:
        """
    @overload
    def GetProperties(self) -> Array[PropertyInfo]:
        """

        :return:
        """
    @overload
    def GetProperties(self, bindingAttr: BindingFlags) -> Array[PropertyInfo]:
        """

        :param bindingAttr:
        :return:
        """
    @overload
    def GetProperties(self, bindingAttr: BindingFlags) -> Array[PropertyInfo]:
        """

        :param bindingAttr:
        :return:
        """
    @overload
    def GetProperty(self, name: str) -> PropertyInfo:
        """

        :param name:
        :return:
        """
    @overload
    def GetProperty(self, name: str, bindingAttr: BindingFlags) -> PropertyInfo:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetProperty(self, name: str, bindingAttr: BindingFlags) -> PropertyInfo:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetProperty(self, name: str, types: Array[Type]) -> PropertyInfo:
        """

        :param name:
        :param types:
        :return:
        """
    @overload
    def GetProperty(self, name: str, returnType: Type) -> PropertyInfo:
        """

        :param name:
        :param returnType:
        :return:
        """
    @overload
    def GetProperty(self, name: str, returnType: Type, types: Array[Type]) -> PropertyInfo:
        """

        :param name:
        :param returnType:
        :param types:
        :return:
        """
    @overload
    def GetProperty(
        self, name: str, returnType: Type, types: Array[Type], modifiers: Array[ParameterModifier]
    ) -> PropertyInfo:
        """

        :param name:
        :param returnType:
        :param types:
        :param modifiers:
        :return:
        """
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
        """

        :param name:
        :param bindingAttr:
        :param binder:
        :param returnType:
        :param types:
        :param modifiers:
        :return:
        """
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
        """

        :param name:
        :param bindingAttr:
        :param binder:
        :param returnType:
        :param types:
        :param modifiers:
        :return:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetTypeInfo(self) -> TypeInfo:
        """

        :return:
        """
    @overload
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    @overload
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    @overload
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    @overload
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    @overload
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    @overload
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    @overload
    def InvokeMember(
        self,
        name: str,
        invokeAttr: BindingFlags,
        binder: Binder,
        target: object,
        args: Array[object],
    ) -> object:
        """

        :param name:
        :param invokeAttr:
        :param binder:
        :param target:
        :param args:
        :return:
        """
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
        """

        :param name:
        :param invokeAttr:
        :param binder:
        :param target:
        :param args:
        :param culture:
        :return:
        """
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
        """

        :param name:
        :param invokeAttr:
        :param binder:
        :param target:
        :param args:
        :param modifiers:
        :param culture:
        :param namedParameters:
        :return:
        """
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
        """

        :param name:
        :param invokeAttr:
        :param binder:
        :param target:
        :param args:
        :param modifiers:
        :param culture:
        :param namedParameters:
        :return:
        """
    @overload
    def IsAssignableFrom(self, typeInfo: TypeInfo) -> bool:
        """

        :param typeInfo:
        :return:
        """
    @overload
    def IsAssignableFrom(self, c: Type) -> bool:
        """

        :param c:
        :return:
        """
    def IsCreated(self) -> bool:
        """

        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    def IsEnumDefined(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    def IsEquivalentTo(self, other: Type) -> bool:
        """

        :param other:
        :return:
        """
    def IsInstanceOfType(self, o: object) -> bool:
        """

        :param o:
        :return:
        """
    def IsSubclassOf(self, c: Type) -> bool:
        """

        :param c:
        :return:
        """
    @overload
    def MakeArrayType(self) -> Type:
        """

        :return:
        """
    @overload
    def MakeArrayType(self, rank: int) -> Type:
        """

        :param rank:
        :return:
        """
    def MakeByRefType(self) -> Type:
        """

        :return:
        """
    def MakeGenericType(self, typeArguments: Array[Type]) -> Type:
        """

        :param typeArguments:
        :return:
        """
    def MakePointerType(self) -> Type:
        """

        :return:
        """
    @overload
    def SetCustomAttribute(self, customBuilder: CustomAttributeBuilder) -> None:
        """

        :param customBuilder:
        """
    @overload
    def SetCustomAttribute(self, con: ConstructorInfo, binaryAttribute: Array[int]) -> None:
        """

        :param con:
        :param binaryAttribute:
        """
    def SetParent(self, parent: Type) -> None:
        """

        :param parent:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """

class TypeBuilderInstantiation(
    TypeInfo, ICustomAttributeProvider, IReflect, IReflectableType, _MemberInfo, _Type
):
    """"""

    @property
    def Assembly(self) -> Assembly:
        """

        :return:
        """
    @property
    def AssemblyQualifiedName(self) -> str:
        """

        :return:
        """
    @property
    def Attributes(self) -> TypeAttributes:
        """

        :return:
        """
    @property
    def BaseType(self) -> Type:
        """

        :return:
        """
    @property
    def ContainsGenericParameters(self) -> bool:
        """

        :return:
        """
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
        """

        :return:
        """
    @property
    def DeclaredConstructors(self) -> IEnumerable[ConstructorInfo]:
        """

        :return:
        """
    @property
    def DeclaredEvents(self) -> IEnumerable[EventInfo]:
        """

        :return:
        """
    @property
    def DeclaredFields(self) -> IEnumerable[FieldInfo]:
        """

        :return:
        """
    @property
    def DeclaredMembers(self) -> IEnumerable[MemberInfo]:
        """

        :return:
        """
    @property
    def DeclaredMethods(self) -> IEnumerable[MethodInfo]:
        """

        :return:
        """
    @property
    def DeclaredNestedTypes(self) -> IEnumerable[TypeInfo]:
        """

        :return:
        """
    @property
    def DeclaredProperties(self) -> IEnumerable[PropertyInfo]:
        """

        :return:
        """
    @property
    def DeclaringMethod(self) -> MethodBase:
        """

        :return:
        """
    @property
    def DeclaringType(self) -> Type:
        """

        :return:
        """
    @property
    def DeclaringType(self) -> Type:
        """

        :return:
        """
    @classmethod
    @property
    def DefaultBinder(cls) -> Binder:
        """

        :return:
        """
    @property
    def FullName(self) -> str:
        """

        :return:
        """
    @property
    def GUID(self) -> Guid:
        """

        :return:
        """
    @property
    def GenericParameterAttributes(self) -> GenericParameterAttributes:
        """

        :return:
        """
    @property
    def GenericParameterPosition(self) -> int:
        """

        :return:
        """
    @property
    def GenericTypeArguments(self) -> Array[Type]:
        """

        :return:
        """
    @property
    def GenericTypeParameters(self) -> Array[Type]:
        """

        :return:
        """
    @property
    def HasElementType(self) -> bool:
        """

        :return:
        """
    @property
    def ImplementedInterfaces(self) -> IEnumerable[Type]:
        """

        :return:
        """
    @property
    def IsAbstract(self) -> bool:
        """

        :return:
        """
    @property
    def IsAnsiClass(self) -> bool:
        """

        :return:
        """
    @property
    def IsArray(self) -> bool:
        """

        :return:
        """
    @property
    def IsAutoClass(self) -> bool:
        """

        :return:
        """
    @property
    def IsAutoLayout(self) -> bool:
        """

        :return:
        """
    @property
    def IsByRef(self) -> bool:
        """

        :return:
        """
    @property
    def IsCOMObject(self) -> bool:
        """

        :return:
        """
    @property
    def IsClass(self) -> bool:
        """

        :return:
        """
    @property
    def IsConstructedGenericType(self) -> bool:
        """

        :return:
        """
    @property
    def IsContextful(self) -> bool:
        """

        :return:
        """
    @property
    def IsEnum(self) -> bool:
        """

        :return:
        """
    @property
    def IsExplicitLayout(self) -> bool:
        """

        :return:
        """
    @property
    def IsGenericParameter(self) -> bool:
        """

        :return:
        """
    @property
    def IsGenericType(self) -> bool:
        """

        :return:
        """
    @property
    def IsGenericTypeDefinition(self) -> bool:
        """

        :return:
        """
    @property
    def IsImport(self) -> bool:
        """

        :return:
        """
    @property
    def IsInterface(self) -> bool:
        """

        :return:
        """
    @property
    def IsLayoutSequential(self) -> bool:
        """

        :return:
        """
    @property
    def IsMarshalByRef(self) -> bool:
        """

        :return:
        """
    @property
    def IsNested(self) -> bool:
        """

        :return:
        """
    @property
    def IsNestedAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsNestedFamANDAssem(self) -> bool:
        """

        :return:
        """
    @property
    def IsNestedFamORAssem(self) -> bool:
        """

        :return:
        """
    @property
    def IsNestedFamily(self) -> bool:
        """

        :return:
        """
    @property
    def IsNestedPrivate(self) -> bool:
        """

        :return:
        """
    @property
    def IsNestedPublic(self) -> bool:
        """

        :return:
        """
    @property
    def IsNotPublic(self) -> bool:
        """

        :return:
        """
    @property
    def IsPointer(self) -> bool:
        """

        :return:
        """
    @property
    def IsPrimitive(self) -> bool:
        """

        :return:
        """
    @property
    def IsPublic(self) -> bool:
        """

        :return:
        """
    @property
    def IsSealed(self) -> bool:
        """

        :return:
        """
    @property
    def IsSecurityCritical(self) -> bool:
        """

        :return:
        """
    @property
    def IsSecuritySafeCritical(self) -> bool:
        """

        :return:
        """
    @property
    def IsSecurityTransparent(self) -> bool:
        """

        :return:
        """
    @property
    def IsSerializable(self) -> bool:
        """

        :return:
        """
    @property
    def IsSpecialName(self) -> bool:
        """

        :return:
        """
    @property
    def IsUnicodeClass(self) -> bool:
        """

        :return:
        """
    @property
    def IsValueType(self) -> bool:
        """

        :return:
        """
    @property
    def IsVisible(self) -> bool:
        """

        :return:
        """
    @property
    def MemberType(self) -> MemberTypes:
        """

        :return:
        """
    @property
    def MemberType(self) -> MemberTypes:
        """

        :return:
        """
    @property
    def MetadataToken(self) -> int:
        """

        :return:
        """
    @property
    def Module(self) -> Module:
        """

        :return:
        """
    @property
    def Module(self) -> Module:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Namespace(self) -> str:
        """

        :return:
        """
    @property
    def ReflectedType(self) -> Type:
        """

        :return:
        """
    @property
    def ReflectedType(self) -> Type:
        """

        :return:
        """
    @property
    def StructLayoutAttribute(self) -> StructLayoutAttribute:
        """

        :return:
        """
    @property
    def TypeHandle(self) -> RuntimeTypeHandle:
        """

        :return:
        """
    @property
    def TypeInitializer(self) -> ConstructorInfo:
        """

        :return:
        """
    @property
    def UnderlyingSystemType(self) -> Type:
        """

        :return:
        """
    @property
    def UnderlyingSystemType(self) -> Type:
        """

        :return:
        """
    def AsType(self) -> Type:
        """

        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def Equals(self, other: object) -> bool:
        """

        :param other:
        :return:
        """
    @overload
    def Equals(self, other: object) -> bool:
        """

        :param other:
        :return:
        """
    @overload
    def Equals(self, o: Type) -> bool:
        """

        :param o:
        :return:
        """
    def FindInterfaces(self, filter: TypeFilter, filterCriteria: object) -> Array[Type]:
        """

        :param filter:
        :param filterCriteria:
        :return:
        """
    def FindMembers(
        self,
        memberType: MemberTypes,
        bindingAttr: BindingFlags,
        filter: MemberFilter,
        filterCriteria: object,
    ) -> Array[MemberInfo]:
        """

        :param memberType:
        :param bindingAttr:
        :param filter:
        :param filterCriteria:
        :return:
        """
    def GetArrayRank(self) -> int:
        """

        :return:
        """
    @overload
    def GetConstructor(self, types: Array[Type]) -> ConstructorInfo:
        """

        :param types:
        :return:
        """
    @overload
    def GetConstructor(
        self,
        bindingAttr: BindingFlags,
        binder: Binder,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> ConstructorInfo:
        """

        :param bindingAttr:
        :param binder:
        :param types:
        :param modifiers:
        :return:
        """
    @overload
    def GetConstructor(
        self,
        bindingAttr: BindingFlags,
        binder: Binder,
        callConvention: CallingConventions,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> ConstructorInfo:
        """

        :param bindingAttr:
        :param binder:
        :param callConvention:
        :param types:
        :param modifiers:
        :return:
        """
    @overload
    def GetConstructors(self) -> Array[ConstructorInfo]:
        """

        :return:
        """
    @overload
    def GetConstructors(self, bindingAttr: BindingFlags) -> Array[ConstructorInfo]:
        """

        :param bindingAttr:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]:
        """

        :return:
        """
    def GetDeclaredEvent(self, name: str) -> EventInfo:
        """

        :param name:
        :return:
        """
    def GetDeclaredField(self, name: str) -> FieldInfo:
        """

        :param name:
        :return:
        """
    def GetDeclaredMethod(self, name: str) -> MethodInfo:
        """

        :param name:
        :return:
        """
    def GetDeclaredMethods(self, name: str) -> IEnumerable[MethodInfo]:
        """

        :param name:
        :return:
        """
    def GetDeclaredNestedType(self, name: str) -> TypeInfo:
        """

        :param name:
        :return:
        """
    def GetDeclaredProperty(self, name: str) -> PropertyInfo:
        """

        :param name:
        :return:
        """
    def GetDefaultMembers(self) -> Array[MemberInfo]:
        """

        :return:
        """
    def GetElementType(self) -> Type:
        """

        :return:
        """
    def GetEnumName(self, value: object) -> str:
        """

        :param value:
        :return:
        """
    def GetEnumNames(self) -> Array[str]:
        """

        :return:
        """
    def GetEnumUnderlyingType(self) -> Type:
        """

        :return:
        """
    def GetEnumValues(self) -> Array:
        """

        :return:
        """
    @overload
    def GetEvent(self, name: str) -> EventInfo:
        """

        :param name:
        :return:
        """
    @overload
    def GetEvent(self, name: str, bindingAttr: BindingFlags) -> EventInfo:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetEvents(self) -> Array[EventInfo]:
        """

        :return:
        """
    @overload
    def GetEvents(self, bindingAttr: BindingFlags) -> Array[EventInfo]:
        """

        :param bindingAttr:
        :return:
        """
    @overload
    def GetField(self, name: str) -> FieldInfo:
        """

        :param name:
        :return:
        """
    @overload
    def GetField(self, name: str, bindingAttr: BindingFlags) -> FieldInfo:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetField(self, name: str, bindingAttr: BindingFlags) -> FieldInfo:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetFields(self) -> Array[FieldInfo]:
        """

        :return:
        """
    @overload
    def GetFields(self, bindingAttr: BindingFlags) -> Array[FieldInfo]:
        """

        :param bindingAttr:
        :return:
        """
    @overload
    def GetFields(self, bindingAttr: BindingFlags) -> Array[FieldInfo]:
        """

        :param bindingAttr:
        :return:
        """
    def GetGenericArguments(self) -> Array[Type]:
        """

        :return:
        """
    def GetGenericParameterConstraints(self) -> Array[Type]:
        """

        :return:
        """
    def GetGenericTypeDefinition(self) -> Type:
        """

        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    @overload
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    @overload
    def GetInterface(self, name: str) -> Type:
        """

        :param name:
        :return:
        """
    @overload
    def GetInterface(self, name: str, ignoreCase: bool) -> Type:
        """

        :param name:
        :param ignoreCase:
        :return:
        """
    def GetInterfaceMap(self, interfaceType: Type) -> InterfaceMapping:
        """

        :param interfaceType:
        :return:
        """
    def GetInterfaces(self) -> Array[Type]:
        """

        :return:
        """
    @overload
    def GetMember(self, name: str) -> Array[MemberInfo]:
        """

        :param name:
        :return:
        """
    @overload
    def GetMember(self, name: str, bindingAttr: BindingFlags) -> Array[MemberInfo]:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetMember(self, name: str, bindingAttr: BindingFlags) -> Array[MemberInfo]:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetMember(
        self, name: str, type: MemberTypes, bindingAttr: BindingFlags
    ) -> Array[MemberInfo]:
        """

        :param name:
        :param type:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetMembers(self) -> Array[MemberInfo]:
        """

        :return:
        """
    @overload
    def GetMembers(self, bindingAttr: BindingFlags) -> Array[MemberInfo]:
        """

        :param bindingAttr:
        :return:
        """
    @overload
    def GetMembers(self, bindingAttr: BindingFlags) -> Array[MemberInfo]:
        """

        :param bindingAttr:
        :return:
        """
    @overload
    def GetMethod(self, name: str) -> MethodInfo:
        """

        :param name:
        :return:
        """
    @overload
    def GetMethod(self, name: str, bindingAttr: BindingFlags) -> MethodInfo:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetMethod(self, name: str, bindingAttr: BindingFlags) -> MethodInfo:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetMethod(self, name: str, types: Array[Type]) -> MethodInfo:
        """

        :param name:
        :param types:
        :return:
        """
    @overload
    def GetMethod(
        self, name: str, types: Array[Type], modifiers: Array[ParameterModifier]
    ) -> MethodInfo:
        """

        :param name:
        :param types:
        :param modifiers:
        :return:
        """
    @overload
    def GetMethod(
        self,
        name: str,
        bindingAttr: BindingFlags,
        binder: Binder,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> MethodInfo:
        """

        :param name:
        :param bindingAttr:
        :param binder:
        :param types:
        :param modifiers:
        :return:
        """
    @overload
    def GetMethod(
        self,
        name: str,
        bindingAttr: BindingFlags,
        binder: Binder,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> MethodInfo:
        """

        :param name:
        :param bindingAttr:
        :param binder:
        :param types:
        :param modifiers:
        :return:
        """
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
        """

        :param name:
        :param bindingAttr:
        :param binder:
        :param callConvention:
        :param types:
        :param modifiers:
        :return:
        """
    @overload
    def GetMethods(self) -> Array[MethodInfo]:
        """

        :return:
        """
    @overload
    def GetMethods(self, bindingAttr: BindingFlags) -> Array[MethodInfo]:
        """

        :param bindingAttr:
        :return:
        """
    @overload
    def GetMethods(self, bindingAttr: BindingFlags) -> Array[MethodInfo]:
        """

        :param bindingAttr:
        :return:
        """
    @overload
    def GetNestedType(self, name: str) -> Type:
        """

        :param name:
        :return:
        """
    @overload
    def GetNestedType(self, name: str, bindingAttr: BindingFlags) -> Type:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetNestedTypes(self) -> Array[Type]:
        """

        :return:
        """
    @overload
    def GetNestedTypes(self, bindingAttr: BindingFlags) -> Array[Type]:
        """

        :param bindingAttr:
        :return:
        """
    @overload
    def GetProperties(self) -> Array[PropertyInfo]:
        """

        :return:
        """
    @overload
    def GetProperties(self, bindingAttr: BindingFlags) -> Array[PropertyInfo]:
        """

        :param bindingAttr:
        :return:
        """
    @overload
    def GetProperties(self, bindingAttr: BindingFlags) -> Array[PropertyInfo]:
        """

        :param bindingAttr:
        :return:
        """
    @overload
    def GetProperty(self, name: str) -> PropertyInfo:
        """

        :param name:
        :return:
        """
    @overload
    def GetProperty(self, name: str, bindingAttr: BindingFlags) -> PropertyInfo:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetProperty(self, name: str, bindingAttr: BindingFlags) -> PropertyInfo:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetProperty(self, name: str, types: Array[Type]) -> PropertyInfo:
        """

        :param name:
        :param types:
        :return:
        """
    @overload
    def GetProperty(self, name: str, returnType: Type) -> PropertyInfo:
        """

        :param name:
        :param returnType:
        :return:
        """
    @overload
    def GetProperty(self, name: str, returnType: Type, types: Array[Type]) -> PropertyInfo:
        """

        :param name:
        :param returnType:
        :param types:
        :return:
        """
    @overload
    def GetProperty(
        self, name: str, returnType: Type, types: Array[Type], modifiers: Array[ParameterModifier]
    ) -> PropertyInfo:
        """

        :param name:
        :param returnType:
        :param types:
        :param modifiers:
        :return:
        """
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
        """

        :param name:
        :param bindingAttr:
        :param binder:
        :param returnType:
        :param types:
        :param modifiers:
        :return:
        """
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
        """

        :param name:
        :param bindingAttr:
        :param binder:
        :param returnType:
        :param types:
        :param modifiers:
        :return:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetTypeInfo(self) -> TypeInfo:
        """

        :return:
        """
    @overload
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    @overload
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    @overload
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    @overload
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    @overload
    def InvokeMember(
        self,
        name: str,
        invokeAttr: BindingFlags,
        binder: Binder,
        target: object,
        args: Array[object],
    ) -> object:
        """

        :param name:
        :param invokeAttr:
        :param binder:
        :param target:
        :param args:
        :return:
        """
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
        """

        :param name:
        :param invokeAttr:
        :param binder:
        :param target:
        :param args:
        :param culture:
        :return:
        """
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
        """

        :param name:
        :param invokeAttr:
        :param binder:
        :param target:
        :param args:
        :param modifiers:
        :param culture:
        :param namedParameters:
        :return:
        """
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
        """

        :param name:
        :param invokeAttr:
        :param binder:
        :param target:
        :param args:
        :param modifiers:
        :param culture:
        :param namedParameters:
        :return:
        """
    @overload
    def IsAssignableFrom(self, typeInfo: TypeInfo) -> bool:
        """

        :param typeInfo:
        :return:
        """
    @overload
    def IsAssignableFrom(self, c: Type) -> bool:
        """

        :param c:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    def IsEnumDefined(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    def IsEquivalentTo(self, other: Type) -> bool:
        """

        :param other:
        :return:
        """
    def IsInstanceOfType(self, o: object) -> bool:
        """

        :param o:
        :return:
        """
    def IsSubclassOf(self, c: Type) -> bool:
        """

        :param c:
        :return:
        """
    @overload
    def MakeArrayType(self) -> Type:
        """

        :return:
        """
    @overload
    def MakeArrayType(self, rank: int) -> Type:
        """

        :param rank:
        :return:
        """
    def MakeByRefType(self) -> Type:
        """

        :return:
        """
    def MakeGenericType(self, typeArguments: Array[Type]) -> Type:
        """

        :param typeArguments:
        :return:
        """
    def MakePointerType(self) -> Type:
        """

        :return:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """

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

class TypeToken(ValueType):
    """"""

    Empty: Final[ClassVar[TypeToken]] = ...
    """
    
    :return: 
    """
    @property
    def Token(self) -> int:
        """

        :return:
        """
    @overload
    def Equals(self, obj: TypeToken) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
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
    def __eq__(self, other: TypeToken) -> bool:
        """

        :param other:
        :return:
        """
    def __ne__(self, other: TypeToken) -> bool:
        """

        :param other:
        :return:
        """
    @classmethod
    def op_Equality(cls, a: TypeToken, b: TypeToken) -> bool:
        """

        :param a:
        :param b:
        :return:
        """
    @classmethod
    def op_Inequality(cls, a: TypeToken, b: TypeToken) -> bool:
        """

        :param a:
        :param b:
        :return:
        """

class UnmanagedMarshal(Object):
    """"""

    @property
    def BaseType(self) -> UnmanagedType:
        """

        :return:
        """
    @property
    def ElementCount(self) -> int:
        """

        :return:
        """
    @property
    def GetUnmanagedType(self) -> UnmanagedType:
        """

        :return:
        """
    @property
    def IIDGuid(self) -> Guid:
        """

        :return:
        """
    @classmethod
    def DefineByValArray(cls, elemCount: int) -> UnmanagedMarshal:
        """

        :param elemCount:
        :return:
        """
    @classmethod
    def DefineByValTStr(cls, elemCount: int) -> UnmanagedMarshal:
        """

        :param elemCount:
        :return:
        """
    @classmethod
    def DefineLPArray(cls, elemType: UnmanagedType) -> UnmanagedMarshal:
        """

        :param elemType:
        :return:
        """
    @classmethod
    def DefineSafeArray(cls, elemType: UnmanagedType) -> UnmanagedMarshal:
        """

        :param elemType:
        :return:
        """
    @classmethod
    def DefineUnmanagedMarshal(cls, unmanagedType: UnmanagedType) -> UnmanagedMarshal:
        """

        :param unmanagedType:
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

class VarArgMethod(Object):
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

class __ExceptionInfo(Object):
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

class __FixupData(ValueType):
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
