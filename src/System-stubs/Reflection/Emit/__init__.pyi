from __future__ import annotations

from typing import List, Tuple, Union, overload

from System import Array, Boolean, Byte, Delegate, Double, Enum, Guid, IEquatable, Int16, Int32, Int64, IntPtr, Object, Resolver, RuntimeFieldHandle, RuntimeMethodHandle, RuntimeTypeHandle, SByte, Single, String, Type, TypedReference, ValueType, Version, Void
from System.Collections.Generic import IEnumerable, IList
from System.Diagnostics.SymbolStore import ISymbolDocumentWriter, ISymbolWriter
from System.Globalization import CultureInfo
from System.IO import FileStream, Stream
from System.Reflection import Assembly, AssemblyName, Binder, BindingFlags, CallingConventions, ConstructorInfo, CustomAttributeData, EventAttributes, EventInfo, ExceptionHandlingClauseOptions, FieldAttributes, FieldInfo, GenericParameterAttributes, ICustomAttributeProvider, IReflect, IReflectableType, ImageFileMachine, InterfaceMapping, LocalVariableInfo, ManifestResourceInfo, MemberInfo, MemberTypes, MethodAttributes, MethodBase, MethodImplAttributes, MethodInfo, Module, ParameterAttributes, ParameterInfo, ParameterModifier, PortableExecutableKinds, PropertyAttributes, PropertyInfo, ResourceAttributes, RuntimeAssembly, RuntimeModule, TypeAttributes, TypeInfo
from System.Resources import IResourceWriter
from System.Runtime.InteropServices import CallingConvention, CharSet, ICustomQueryInterface, UnmanagedType, _Assembly, _AssemblyBuilder, _ConstructorBuilder, _ConstructorInfo, _CustomAttributeBuilder, _EnumBuilder, _EventBuilder, _FieldBuilder, _FieldInfo, _ILGenerator, _LocalBuilder, _MemberInfo, _MethodBase, _MethodBuilder, _MethodInfo, _MethodRental, _Module, _ModuleBuilder, _ParameterBuilder, _PropertyBuilder, _PropertyInfo, _SignatureHelper, _Type, _TypeBuilder
from System.Runtime.Serialization import ISerializable
from System.Security import IEvidenceFactory, PermissionSet, SecurityRuleSet
from System.Security.Cryptography.X509Certificates import X509Certificate
from System.Security.Permissions import SecurityAction
from System.Security.Policy import Evidence

# ---------- Types ---------- #

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
ByteType = Union[int, Byte]
DoubleType = Union[float, Double]
FloatType = Union[float, Single]
IntType = Union[int, Int32]
LongType = Union[int, Int64]
NIntType = Union[int, IntPtr]
ObjectType = Object
SByteType = Union[int, SByte]
ShortType = Union[int, Int16]
StringType = Union[str, String]
TypeType = Union[type, Type]
VoidType = Union[None, Void]


# ---------- Classes ---------- #

class AssemblyBuilder(Assembly, _Assembly, IEvidenceFactory, ICustomAttributeProvider, ISerializable, _AssemblyBuilder):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def CodeBase(self) -> StringType: ...
    
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
    def AddResourceFile(self, name: StringType, fileName: StringType) -> VoidType: ...
    
    @overload
    def AddResourceFile(self, name: StringType, fileName: StringType, attribute: ResourceAttributes) -> VoidType: ...
    
    @staticmethod
    @overload
    def DefineDynamicAssembly(name: AssemblyName, access: AssemblyBuilderAccess) -> AssemblyBuilder: ...
    
    @staticmethod
    @overload
    def DefineDynamicAssembly(name: AssemblyName, access: AssemblyBuilderAccess, assemblyAttributes: IEnumerable[CustomAttributeBuilder]) -> AssemblyBuilder: ...
    
    @overload
    def DefineDynamicModule(self, name: StringType) -> ModuleBuilder: ...
    
    @overload
    def DefineDynamicModule(self, name: StringType, emitSymbolInfo: BooleanType) -> ModuleBuilder: ...
    
    @overload
    def DefineDynamicModule(self, name: StringType, fileName: StringType) -> ModuleBuilder: ...
    
    @overload
    def DefineDynamicModule(self, name: StringType, fileName: StringType, emitSymbolInfo: BooleanType) -> ModuleBuilder: ...
    
    @overload
    def DefineResource(self, name: StringType, description: StringType, fileName: StringType) -> IResourceWriter: ...
    
    @overload
    def DefineResource(self, name: StringType, description: StringType, fileName: StringType, attribute: ResourceAttributes) -> IResourceWriter: ...
    
    @overload
    def DefineUnmanagedResource(self, resource: ArrayType[ByteType]) -> VoidType: ...
    
    @overload
    def DefineUnmanagedResource(self, resourceFileName: StringType) -> VoidType: ...
    
    @overload
    def DefineVersionInfoResource(self, product: StringType, productVersion: StringType, company: StringType, copyright: StringType, trademark: StringType) -> VoidType: ...
    
    @overload
    def DefineVersionInfoResource(self) -> VoidType: ...
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @overload
    def GetCustomAttributes(self, inherit: BooleanType) -> ArrayType[ObjectType]: ...
    
    @overload
    def GetCustomAttributes(self, attributeType: TypeType, inherit: BooleanType) -> ArrayType[ObjectType]: ...
    
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]: ...
    
    def GetDynamicModule(self, name: StringType) -> ModuleBuilder: ...
    
    def GetExportedTypes(self) -> ArrayType[TypeType]: ...
    
    def GetFile(self, name: StringType) -> FileStream: ...
    
    @overload
    def GetFiles(self, getResourceModules: BooleanType) -> ArrayType[FileStream]: ...
    
    def GetHashCode(self) -> IntType: ...
    
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
    
    def GetReferencedAssemblies(self) -> ArrayType[AssemblyName]: ...
    
    @overload
    def GetSatelliteAssembly(self, culture: CultureInfo) -> Assembly: ...
    
    @overload
    def GetSatelliteAssembly(self, culture: CultureInfo, version: Version) -> Assembly: ...
    
    @overload
    def GetType(self, name: StringType, throwOnError: BooleanType, ignoreCase: BooleanType) -> TypeType: ...
    
    def IsDefined(self, attributeType: TypeType, inherit: BooleanType) -> BooleanType: ...
    
    @overload
    def Save(self, assemblyFileName: StringType) -> VoidType: ...
    
    @overload
    def Save(self, assemblyFileName: StringType, portableExecutableKind: PortableExecutableKinds, imageFileMachine: ImageFileMachine) -> VoidType: ...
    
    @overload
    def SetCustomAttribute(self, customBuilder: CustomAttributeBuilder) -> VoidType: ...
    
    @overload
    def SetCustomAttribute(self, con: ConstructorInfo, binaryAttribute: ArrayType[ByteType]) -> VoidType: ...
    
    @overload
    def SetEntryPoint(self, entryMethod: MethodInfo) -> VoidType: ...
    
    @overload
    def SetEntryPoint(self, entryMethod: MethodInfo, fileKind: PEFileKinds) -> VoidType: ...
    
    def get_CodeBase(self) -> StringType: ...
    
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
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AssemblyBuilderData(ObjectType):
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


class ConstructorBuilder(ConstructorInfo, ICustomAttributeProvider, _MemberInfo, _MethodBase, _ConstructorInfo, _ConstructorBuilder):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Attributes(self) -> MethodAttributes: ...
    
    @property
    def CallingConvention(self) -> CallingConventions: ...
    
    @property
    def DeclaringType(self) -> TypeType: ...
    
    @property
    def InitLocals(self) -> BooleanType: ...
    
    @InitLocals.setter
    def InitLocals(self, value: BooleanType) -> None: ...
    
    @property
    def MethodHandle(self) -> RuntimeMethodHandle: ...
    
    @property
    def Module(self) -> Module: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def ReflectedType(self) -> TypeType: ...
    
    @property
    def ReturnType(self) -> TypeType: ...
    
    @property
    def Signature(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def AddDeclarativeSecurity(self, action: SecurityAction, pset: PermissionSet) -> VoidType: ...
    
    def DefineParameter(self, iSequence: IntType, attributes: ParameterAttributes, strParamName: StringType) -> ParameterBuilder: ...
    
    @overload
    def GetCustomAttributes(self, inherit: BooleanType) -> ArrayType[ObjectType]: ...
    
    @overload
    def GetCustomAttributes(self, attributeType: TypeType, inherit: BooleanType) -> ArrayType[ObjectType]: ...
    
    @overload
    def GetILGenerator(self) -> ILGenerator: ...
    
    @overload
    def GetILGenerator(self, streamSize: IntType) -> ILGenerator: ...
    
    def GetMethodImplementationFlags(self) -> MethodImplAttributes: ...
    
    def GetModule(self) -> Module: ...
    
    def GetParameters(self) -> ArrayType[ParameterInfo]: ...
    
    def GetToken(self) -> MethodToken: ...
    
    @overload
    def Invoke(self, obj: ObjectType, invokeAttr: BindingFlags, binder: Binder, parameters: ArrayType[ObjectType], culture: CultureInfo) -> ObjectType: ...
    
    @overload
    def Invoke(self, invokeAttr: BindingFlags, binder: Binder, parameters: ArrayType[ObjectType], culture: CultureInfo) -> ObjectType: ...
    
    def IsDefined(self, attributeType: TypeType, inherit: BooleanType) -> BooleanType: ...
    
    @overload
    def SetCustomAttribute(self, con: ConstructorInfo, binaryAttribute: ArrayType[ByteType]) -> VoidType: ...
    
    @overload
    def SetCustomAttribute(self, customBuilder: CustomAttributeBuilder) -> VoidType: ...
    
    def SetImplementationFlags(self, attributes: MethodImplAttributes) -> VoidType: ...
    
    def SetMethodBody(self, il: ArrayType[ByteType], maxStack: IntType, localSignature: ArrayType[ByteType], exceptionHandlers: IEnumerable[ExceptionHandler], tokenFixups: IEnumerable[IntType]) -> VoidType: ...
    
    def SetSymCustomAttribute(self, name: StringType, data: ArrayType[ByteType]) -> VoidType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Attributes(self) -> MethodAttributes: ...
    
    def get_CallingConvention(self) -> CallingConventions: ...
    
    def get_DeclaringType(self) -> TypeType: ...
    
    def get_InitLocals(self) -> BooleanType: ...
    
    def get_MethodHandle(self) -> RuntimeMethodHandle: ...
    
    def get_Module(self) -> Module: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_ReflectedType(self) -> TypeType: ...
    
    def get_ReturnType(self) -> TypeType: ...
    
    def get_Signature(self) -> StringType: ...
    
    def set_InitLocals(self, value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ConstructorOnTypeBuilderInstantiation(ConstructorInfo, ICustomAttributeProvider, _MemberInfo, _MethodBase, _ConstructorInfo):
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
    def MemberType(self) -> MemberTypes: ...
    
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
    
    def GetGenericArguments(self) -> ArrayType[TypeType]: ...
    
    def GetMethodImplementationFlags(self) -> MethodImplAttributes: ...
    
    def GetParameters(self) -> ArrayType[ParameterInfo]: ...
    
    @overload
    def GetType(self) -> TypeType: ...
    
    @overload
    def Invoke(self, obj: ObjectType, invokeAttr: BindingFlags, binder: Binder, parameters: ArrayType[ObjectType], culture: CultureInfo) -> ObjectType: ...
    
    @overload
    def Invoke(self, invokeAttr: BindingFlags, binder: Binder, parameters: ArrayType[ObjectType], culture: CultureInfo) -> ObjectType: ...
    
    def IsDefined(self, attributeType: TypeType, inherit: BooleanType) -> BooleanType: ...
    
    def get_Attributes(self) -> MethodAttributes: ...
    
    def get_CallingConvention(self) -> CallingConventions: ...
    
    def get_ContainsGenericParameters(self) -> BooleanType: ...
    
    def get_DeclaringType(self) -> TypeType: ...
    
    def get_IsGenericMethod(self) -> BooleanType: ...
    
    def get_IsGenericMethodDefinition(self) -> BooleanType: ...
    
    def get_MemberType(self) -> MemberTypes: ...
    
    def get_MethodHandle(self) -> RuntimeMethodHandle: ...
    
    def get_Module(self) -> Module: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_ReflectedType(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CustomAttributeBuilder(ObjectType, _CustomAttributeBuilder):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, con: ConstructorInfo, constructorArgs: ArrayType[ObjectType]): ...
    
    @overload
    def __init__(self, con: ConstructorInfo, constructorArgs: ArrayType[ObjectType], namedProperties: ArrayType[PropertyInfo], propertyValues: ArrayType[ObjectType]): ...
    
    @overload
    def __init__(self, con: ConstructorInfo, constructorArgs: ArrayType[ObjectType], namedFields: ArrayType[FieldInfo], fieldValues: ArrayType[ObjectType]): ...
    
    @overload
    def __init__(self, con: ConstructorInfo, constructorArgs: ArrayType[ObjectType], namedProperties: ArrayType[PropertyInfo], propertyValues: ArrayType[ObjectType], namedFields: ArrayType[FieldInfo], fieldValues: ArrayType[ObjectType]): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DynamicILGenerator(ILGenerator, _ILGenerator):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginCatchBlock(self, exceptionType: TypeType) -> VoidType: ...
    
    def BeginExceptFilterBlock(self) -> VoidType: ...
    
    def BeginExceptionBlock(self) -> Label: ...
    
    def BeginFaultBlock(self) -> VoidType: ...
    
    def BeginFinallyBlock(self) -> VoidType: ...
    
    def BeginScope(self) -> VoidType: ...
    
    @overload
    def DeclareLocal(self, localType: TypeType, pinned: BooleanType) -> LocalBuilder: ...
    
    @overload
    def Emit(self, opcode: OpCode, meth: MethodInfo) -> VoidType: ...
    
    @overload
    def Emit(self, opcode: OpCode, con: ConstructorInfo) -> VoidType: ...
    
    @overload
    def Emit(self, opcode: OpCode, type: TypeType) -> VoidType: ...
    
    @overload
    def Emit(self, opcode: OpCode, field: FieldInfo) -> VoidType: ...
    
    @overload
    def Emit(self, opcode: OpCode, str: StringType) -> VoidType: ...
    
    @overload
    def Emit(self, opcode: OpCode, signature: SignatureHelper) -> VoidType: ...
    
    def EmitCall(self, opcode: OpCode, methodInfo: MethodInfo, optionalParameterTypes: ArrayType[TypeType]) -> VoidType: ...
    
    @overload
    def EmitCalli(self, opcode: OpCode, callingConvention: CallingConventions, returnType: TypeType, parameterTypes: ArrayType[TypeType], optionalParameterTypes: ArrayType[TypeType]) -> VoidType: ...
    
    @overload
    def EmitCalli(self, opcode: OpCode, unmanagedCallConv: CallingConvention, returnType: TypeType, parameterTypes: ArrayType[TypeType]) -> VoidType: ...
    
    def EndExceptionBlock(self) -> VoidType: ...
    
    def EndScope(self) -> VoidType: ...
    
    def MarkSequencePoint(self, document: ISymbolDocumentWriter, startLine: IntType, startColumn: IntType, endLine: IntType, endColumn: IntType) -> VoidType: ...
    
    def UsingNamespace(self, ns: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DynamicILInfo(ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def DynamicMethod(self) -> DynamicMethod: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def GetTokenFor(self, method: RuntimeMethodHandle) -> IntType: ...
    
    @overload
    def GetTokenFor(self, method: DynamicMethod) -> IntType: ...
    
    @overload
    def GetTokenFor(self, method: RuntimeMethodHandle, contextType: RuntimeTypeHandle) -> IntType: ...
    
    @overload
    def GetTokenFor(self, field: RuntimeFieldHandle) -> IntType: ...
    
    @overload
    def GetTokenFor(self, field: RuntimeFieldHandle, contextType: RuntimeTypeHandle) -> IntType: ...
    
    @overload
    def GetTokenFor(self, type: RuntimeTypeHandle) -> IntType: ...
    
    @overload
    def GetTokenFor(self, literal: StringType) -> IntType: ...
    
    @overload
    def GetTokenFor(self, signature: ArrayType[ByteType]) -> IntType: ...
    
    @overload
    def SetCode(self, code: ArrayType[ByteType], maxStackSize: IntType) -> VoidType: ...
    
    @overload
    def SetCode(self, code: ByteType, codeSize: IntType, maxStackSize: IntType) -> VoidType: ...
    
    @overload
    def SetExceptions(self, exceptions: ArrayType[ByteType]) -> VoidType: ...
    
    @overload
    def SetExceptions(self, exceptions: ByteType, exceptionsSize: IntType) -> VoidType: ...
    
    @overload
    def SetLocalSignature(self, localSignature: ArrayType[ByteType]) -> VoidType: ...
    
    @overload
    def SetLocalSignature(self, localSignature: ByteType, signatureSize: IntType) -> VoidType: ...
    
    def get_DynamicMethod(self) -> DynamicMethod: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DynamicMethod(MethodInfo, ICustomAttributeProvider, _MemberInfo, _MethodBase, _MethodInfo):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, name: StringType, returnType: TypeType, parameterTypes: ArrayType[TypeType]): ...
    
    @overload
    def __init__(self, name: StringType, returnType: TypeType, parameterTypes: ArrayType[TypeType], restrictedSkipVisibility: BooleanType): ...
    
    @overload
    def __init__(self, name: StringType, returnType: TypeType, parameterTypes: ArrayType[TypeType], m: Module): ...
    
    @overload
    def __init__(self, name: StringType, returnType: TypeType, parameterTypes: ArrayType[TypeType], m: Module, skipVisibility: BooleanType): ...
    
    @overload
    def __init__(self, name: StringType, attributes: MethodAttributes, callingConvention: CallingConventions, returnType: TypeType, parameterTypes: ArrayType[TypeType], m: Module, skipVisibility: BooleanType): ...
    
    @overload
    def __init__(self, name: StringType, returnType: TypeType, parameterTypes: ArrayType[TypeType], owner: TypeType): ...
    
    @overload
    def __init__(self, name: StringType, returnType: TypeType, parameterTypes: ArrayType[TypeType], owner: TypeType, skipVisibility: BooleanType): ...
    
    @overload
    def __init__(self, name: StringType, attributes: MethodAttributes, callingConvention: CallingConventions, returnType: TypeType, parameterTypes: ArrayType[TypeType], owner: TypeType, skipVisibility: BooleanType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Attributes(self) -> MethodAttributes: ...
    
    @property
    def CallingConvention(self) -> CallingConventions: ...
    
    @property
    def DeclaringType(self) -> TypeType: ...
    
    @property
    def InitLocals(self) -> BooleanType: ...
    
    @InitLocals.setter
    def InitLocals(self, value: BooleanType) -> None: ...
    
    @property
    def IsSecurityCritical(self) -> BooleanType: ...
    
    @property
    def IsSecuritySafeCritical(self) -> BooleanType: ...
    
    @property
    def IsSecurityTransparent(self) -> BooleanType: ...
    
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
    
    def DefineParameter(self, position: IntType, attributes: ParameterAttributes, parameterName: StringType) -> ParameterBuilder: ...
    
    def GetBaseDefinition(self) -> MethodInfo: ...
    
    @overload
    def GetCustomAttributes(self, attributeType: TypeType, inherit: BooleanType) -> ArrayType[ObjectType]: ...
    
    @overload
    def GetCustomAttributes(self, inherit: BooleanType) -> ArrayType[ObjectType]: ...
    
    def GetDynamicILInfo(self) -> DynamicILInfo: ...
    
    @overload
    def GetILGenerator(self) -> ILGenerator: ...
    
    @overload
    def GetILGenerator(self, streamSize: IntType) -> ILGenerator: ...
    
    def GetMethodImplementationFlags(self) -> MethodImplAttributes: ...
    
    def GetParameters(self) -> ArrayType[ParameterInfo]: ...
    
    @overload
    def Invoke(self, obj: ObjectType, invokeAttr: BindingFlags, binder: Binder, parameters: ArrayType[ObjectType], culture: CultureInfo) -> ObjectType: ...
    
    def IsDefined(self, attributeType: TypeType, inherit: BooleanType) -> BooleanType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Attributes(self) -> MethodAttributes: ...
    
    def get_CallingConvention(self) -> CallingConventions: ...
    
    def get_DeclaringType(self) -> TypeType: ...
    
    def get_InitLocals(self) -> BooleanType: ...
    
    def get_IsSecurityCritical(self) -> BooleanType: ...
    
    def get_IsSecuritySafeCritical(self) -> BooleanType: ...
    
    def get_IsSecurityTransparent(self) -> BooleanType: ...
    
    def get_MethodHandle(self) -> RuntimeMethodHandle: ...
    
    def get_Module(self) -> Module: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_ReflectedType(self) -> TypeType: ...
    
    def get_ReturnParameter(self) -> ParameterInfo: ...
    
    def get_ReturnType(self) -> TypeType: ...
    
    def get_ReturnTypeCustomAttributes(self) -> ICustomAttributeProvider: ...
    
    def set_InitLocals(self, value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DynamicResolver(Resolver):
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


class DynamicScope(ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def GetTokenFor(self, method: RuntimeMethodHandle) -> IntType: ...
    
    @overload
    def GetTokenFor(self, method: RuntimeMethodHandle, typeContext: RuntimeTypeHandle) -> IntType: ...
    
    @overload
    def GetTokenFor(self, method: DynamicMethod) -> IntType: ...
    
    @overload
    def GetTokenFor(self, field: RuntimeFieldHandle) -> IntType: ...
    
    @overload
    def GetTokenFor(self, field: RuntimeFieldHandle, typeContext: RuntimeTypeHandle) -> IntType: ...
    
    @overload
    def GetTokenFor(self, type: RuntimeTypeHandle) -> IntType: ...
    
    @overload
    def GetTokenFor(self, literal: StringType) -> IntType: ...
    
    @overload
    def GetTokenFor(self, signature: ArrayType[ByteType]) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EnumBuilder(TypeInfo, ICustomAttributeProvider, _MemberInfo, _Type, IReflect, IReflectableType, _EnumBuilder):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Assembly(self) -> Assembly: ...
    
    @property
    def AssemblyQualifiedName(self) -> StringType: ...
    
    @property
    def BaseType(self) -> TypeType: ...
    
    @property
    def DeclaringType(self) -> TypeType: ...
    
    @property
    def FullName(self) -> StringType: ...
    
    @property
    def GUID(self) -> Guid: ...
    
    @property
    def IsConstructedGenericType(self) -> BooleanType: ...
    
    @property
    def Module(self) -> Module: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def Namespace(self) -> StringType: ...
    
    @property
    def ReflectedType(self) -> TypeType: ...
    
    @property
    def TypeHandle(self) -> RuntimeTypeHandle: ...
    
    @property
    def TypeToken(self) -> TypeToken: ...
    
    @property
    def UnderlyingField(self) -> FieldBuilder: ...
    
    @property
    def UnderlyingSystemType(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def CreateType(self) -> TypeType: ...
    
    def CreateTypeInfo(self) -> TypeInfo: ...
    
    def DefineLiteral(self, literalName: StringType, literalValue: ObjectType) -> FieldBuilder: ...
    
    @overload
    def GetConstructors(self, bindingAttr: BindingFlags) -> ArrayType[ConstructorInfo]: ...
    
    @overload
    def GetCustomAttributes(self, inherit: BooleanType) -> ArrayType[ObjectType]: ...
    
    @overload
    def GetCustomAttributes(self, attributeType: TypeType, inherit: BooleanType) -> ArrayType[ObjectType]: ...
    
    def GetElementType(self) -> TypeType: ...
    
    def GetEnumUnderlyingType(self) -> TypeType: ...
    
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
    
    @overload
    def MakeArrayType(self) -> TypeType: ...
    
    @overload
    def MakeArrayType(self, rank: IntType) -> TypeType: ...
    
    def MakeByRefType(self) -> TypeType: ...
    
    def MakePointerType(self) -> TypeType: ...
    
    @overload
    def SetCustomAttribute(self, con: ConstructorInfo, binaryAttribute: ArrayType[ByteType]) -> VoidType: ...
    
    @overload
    def SetCustomAttribute(self, customBuilder: CustomAttributeBuilder) -> VoidType: ...
    
    def get_Assembly(self) -> Assembly: ...
    
    def get_AssemblyQualifiedName(self) -> StringType: ...
    
    def get_BaseType(self) -> TypeType: ...
    
    def get_DeclaringType(self) -> TypeType: ...
    
    def get_FullName(self) -> StringType: ...
    
    def get_GUID(self) -> Guid: ...
    
    def get_IsConstructedGenericType(self) -> BooleanType: ...
    
    @overload
    def get_Module(self) -> Module: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_Namespace(self) -> StringType: ...
    
    def get_ReflectedType(self) -> TypeType: ...
    
    def get_TypeHandle(self) -> RuntimeTypeHandle: ...
    
    def get_TypeToken(self) -> TypeToken: ...
    
    def get_UnderlyingField(self) -> FieldBuilder: ...
    
    def get_UnderlyingSystemType(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EventBuilder(ObjectType, _EventBuilder):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def AddOtherMethod(self, mdBuilder: MethodBuilder) -> VoidType: ...
    
    def GetEventToken(self) -> EventToken: ...
    
    def SetAddOnMethod(self, mdBuilder: MethodBuilder) -> VoidType: ...
    
    @overload
    def SetCustomAttribute(self, con: ConstructorInfo, binaryAttribute: ArrayType[ByteType]) -> VoidType: ...
    
    @overload
    def SetCustomAttribute(self, customBuilder: CustomAttributeBuilder) -> VoidType: ...
    
    def SetRaiseMethod(self, mdBuilder: MethodBuilder) -> VoidType: ...
    
    def SetRemoveOnMethod(self, mdBuilder: MethodBuilder) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class FieldBuilder(FieldInfo, ICustomAttributeProvider, _MemberInfo, _FieldInfo, _FieldBuilder):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Attributes(self) -> FieldAttributes: ...
    
    @property
    def DeclaringType(self) -> TypeType: ...
    
    @property
    def FieldHandle(self) -> RuntimeFieldHandle: ...
    
    @property
    def FieldType(self) -> TypeType: ...
    
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
    
    def GetToken(self) -> FieldToken: ...
    
    def GetValue(self, obj: ObjectType) -> ObjectType: ...
    
    def IsDefined(self, attributeType: TypeType, inherit: BooleanType) -> BooleanType: ...
    
    def SetConstant(self, defaultValue: ObjectType) -> VoidType: ...
    
    @overload
    def SetCustomAttribute(self, con: ConstructorInfo, binaryAttribute: ArrayType[ByteType]) -> VoidType: ...
    
    @overload
    def SetCustomAttribute(self, customBuilder: CustomAttributeBuilder) -> VoidType: ...
    
    def SetMarshal(self, unmanagedMarshal: UnmanagedMarshal) -> VoidType: ...
    
    def SetOffset(self, iOffset: IntType) -> VoidType: ...
    
    @overload
    def SetValue(self, obj: ObjectType, val: ObjectType, invokeAttr: BindingFlags, binder: Binder, culture: CultureInfo) -> VoidType: ...
    
    def get_Attributes(self) -> FieldAttributes: ...
    
    def get_DeclaringType(self) -> TypeType: ...
    
    def get_FieldHandle(self) -> RuntimeFieldHandle: ...
    
    def get_FieldType(self) -> TypeType: ...
    
    def get_Module(self) -> Module: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_ReflectedType(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class FieldOnTypeBuilderInstantiation(FieldInfo, ICustomAttributeProvider, _MemberInfo, _FieldInfo):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Attributes(self) -> FieldAttributes: ...
    
    @property
    def DeclaringType(self) -> TypeType: ...
    
    @property
    def FieldHandle(self) -> RuntimeFieldHandle: ...
    
    @property
    def FieldType(self) -> TypeType: ...
    
    @property
    def MemberType(self) -> MemberTypes: ...
    
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
    
    def GetOptionalCustomModifiers(self) -> ArrayType[TypeType]: ...
    
    def GetRequiredCustomModifiers(self) -> ArrayType[TypeType]: ...
    
    @overload
    def GetType(self) -> TypeType: ...
    
    def GetValue(self, obj: ObjectType) -> ObjectType: ...
    
    def GetValueDirect(self, obj: TypedReference) -> ObjectType: ...
    
    def IsDefined(self, attributeType: TypeType, inherit: BooleanType) -> BooleanType: ...
    
    @overload
    def SetValue(self, obj: ObjectType, value: ObjectType, invokeAttr: BindingFlags, binder: Binder, culture: CultureInfo) -> VoidType: ...
    
    def SetValueDirect(self, obj: TypedReference, value: ObjectType) -> VoidType: ...
    
    def get_Attributes(self) -> FieldAttributes: ...
    
    def get_DeclaringType(self) -> TypeType: ...
    
    def get_FieldHandle(self) -> RuntimeFieldHandle: ...
    
    def get_FieldType(self) -> TypeType: ...
    
    def get_MemberType(self) -> MemberTypes: ...
    
    def get_Module(self) -> Module: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_ReflectedType(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class GenericFieldInfo(ObjectType):
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


class GenericMethodInfo(ObjectType):
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


class GenericTypeParameterBuilder(TypeInfo, ICustomAttributeProvider, _MemberInfo, _Type, IReflect, IReflectableType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Assembly(self) -> Assembly: ...
    
    @property
    def AssemblyQualifiedName(self) -> StringType: ...
    
    @property
    def BaseType(self) -> TypeType: ...
    
    @property
    def ContainsGenericParameters(self) -> BooleanType: ...
    
    @property
    def DeclaringMethod(self) -> MethodBase: ...
    
    @property
    def DeclaringType(self) -> TypeType: ...
    
    @property
    def FullName(self) -> StringType: ...
    
    @property
    def GUID(self) -> Guid: ...
    
    @property
    def GenericParameterAttributes(self) -> GenericParameterAttributes: ...
    
    @property
    def GenericParameterPosition(self) -> IntType: ...
    
    @property
    def IsConstructedGenericType(self) -> BooleanType: ...
    
    @property
    def IsGenericParameter(self) -> BooleanType: ...
    
    @property
    def IsGenericType(self) -> BooleanType: ...
    
    @property
    def IsGenericTypeDefinition(self) -> BooleanType: ...
    
    @property
    def Module(self) -> Module: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def Namespace(self) -> StringType: ...
    
    @property
    def ReflectedType(self) -> TypeType: ...
    
    @property
    def TypeHandle(self) -> RuntimeTypeHandle: ...
    
    @property
    def UnderlyingSystemType(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
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
    
    def GetGenericArguments(self) -> ArrayType[TypeType]: ...
    
    def GetGenericTypeDefinition(self) -> TypeType: ...
    
    def GetHashCode(self) -> IntType: ...
    
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
    
    @overload
    def IsAssignableFrom(self, c: TypeType) -> BooleanType: ...
    
    def IsDefined(self, attributeType: TypeType, inherit: BooleanType) -> BooleanType: ...
    
    def IsSubclassOf(self, c: TypeType) -> BooleanType: ...
    
    @overload
    def MakeArrayType(self) -> TypeType: ...
    
    @overload
    def MakeArrayType(self, rank: IntType) -> TypeType: ...
    
    def MakeByRefType(self) -> TypeType: ...
    
    def MakeGenericType(self, typeArguments: ArrayType[TypeType]) -> TypeType: ...
    
    def MakePointerType(self) -> TypeType: ...
    
    def SetBaseTypeConstraint(self, baseTypeConstraint: TypeType) -> VoidType: ...
    
    @overload
    def SetCustomAttribute(self, con: ConstructorInfo, binaryAttribute: ArrayType[ByteType]) -> VoidType: ...
    
    @overload
    def SetCustomAttribute(self, customBuilder: CustomAttributeBuilder) -> VoidType: ...
    
    def SetGenericParameterAttributes(self, genericParameterAttributes: GenericParameterAttributes) -> VoidType: ...
    
    def SetInterfaceConstraints(self, interfaceConstraints: ArrayType[TypeType]) -> VoidType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Assembly(self) -> Assembly: ...
    
    def get_AssemblyQualifiedName(self) -> StringType: ...
    
    def get_BaseType(self) -> TypeType: ...
    
    def get_ContainsGenericParameters(self) -> BooleanType: ...
    
    def get_DeclaringMethod(self) -> MethodBase: ...
    
    def get_DeclaringType(self) -> TypeType: ...
    
    def get_FullName(self) -> StringType: ...
    
    def get_GUID(self) -> Guid: ...
    
    def get_GenericParameterAttributes(self) -> GenericParameterAttributes: ...
    
    def get_GenericParameterPosition(self) -> IntType: ...
    
    def get_IsConstructedGenericType(self) -> BooleanType: ...
    
    def get_IsGenericParameter(self) -> BooleanType: ...
    
    def get_IsGenericType(self) -> BooleanType: ...
    
    def get_IsGenericTypeDefinition(self) -> BooleanType: ...
    
    @overload
    def get_Module(self) -> Module: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_Namespace(self) -> StringType: ...
    
    def get_ReflectedType(self) -> TypeType: ...
    
    def get_TypeHandle(self) -> RuntimeTypeHandle: ...
    
    def get_UnderlyingSystemType(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ILGenerator(ObjectType, _ILGenerator):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def ILOffset(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def BeginCatchBlock(self, exceptionType: TypeType) -> VoidType: ...
    
    def BeginExceptFilterBlock(self) -> VoidType: ...
    
    def BeginExceptionBlock(self) -> Label: ...
    
    def BeginFaultBlock(self) -> VoidType: ...
    
    def BeginFinallyBlock(self) -> VoidType: ...
    
    def BeginScope(self) -> VoidType: ...
    
    @overload
    def DeclareLocal(self, localType: TypeType) -> LocalBuilder: ...
    
    @overload
    def DeclareLocal(self, localType: TypeType, pinned: BooleanType) -> LocalBuilder: ...
    
    def DefineLabel(self) -> Label: ...
    
    @overload
    def Emit(self, opcode: OpCode) -> VoidType: ...
    
    @overload
    def Emit(self, opcode: OpCode, arg: ByteType) -> VoidType: ...
    
    @overload
    def Emit(self, opcode: OpCode, arg: SByteType) -> VoidType: ...
    
    @overload
    def Emit(self, opcode: OpCode, arg: ShortType) -> VoidType: ...
    
    @overload
    def Emit(self, opcode: OpCode, arg: IntType) -> VoidType: ...
    
    @overload
    def Emit(self, opcode: OpCode, meth: MethodInfo) -> VoidType: ...
    
    @overload
    def Emit(self, opcode: OpCode, signature: SignatureHelper) -> VoidType: ...
    
    @overload
    def Emit(self, opcode: OpCode, con: ConstructorInfo) -> VoidType: ...
    
    @overload
    def Emit(self, opcode: OpCode, cls: TypeType) -> VoidType: ...
    
    @overload
    def Emit(self, opcode: OpCode, arg: LongType) -> VoidType: ...
    
    @overload
    def Emit(self, opcode: OpCode, arg: FloatType) -> VoidType: ...
    
    @overload
    def Emit(self, opcode: OpCode, arg: DoubleType) -> VoidType: ...
    
    @overload
    def Emit(self, opcode: OpCode, label: Label) -> VoidType: ...
    
    @overload
    def Emit(self, opcode: OpCode, labels: ArrayType[Label]) -> VoidType: ...
    
    @overload
    def Emit(self, opcode: OpCode, field: FieldInfo) -> VoidType: ...
    
    @overload
    def Emit(self, opcode: OpCode, str: StringType) -> VoidType: ...
    
    @overload
    def Emit(self, opcode: OpCode, local: LocalBuilder) -> VoidType: ...
    
    def EmitCall(self, opcode: OpCode, methodInfo: MethodInfo, optionalParameterTypes: ArrayType[TypeType]) -> VoidType: ...
    
    @overload
    def EmitCalli(self, opcode: OpCode, callingConvention: CallingConventions, returnType: TypeType, parameterTypes: ArrayType[TypeType], optionalParameterTypes: ArrayType[TypeType]) -> VoidType: ...
    
    @overload
    def EmitCalli(self, opcode: OpCode, unmanagedCallConv: CallingConvention, returnType: TypeType, parameterTypes: ArrayType[TypeType]) -> VoidType: ...
    
    @overload
    def EmitWriteLine(self, value: StringType) -> VoidType: ...
    
    @overload
    def EmitWriteLine(self, localBuilder: LocalBuilder) -> VoidType: ...
    
    @overload
    def EmitWriteLine(self, fld: FieldInfo) -> VoidType: ...
    
    def EndExceptionBlock(self) -> VoidType: ...
    
    def EndScope(self) -> VoidType: ...
    
    def MarkLabel(self, loc: Label) -> VoidType: ...
    
    def MarkSequencePoint(self, document: ISymbolDocumentWriter, startLine: IntType, startColumn: IntType, endLine: IntType, endColumn: IntType) -> VoidType: ...
    
    def ThrowException(self, excType: TypeType) -> VoidType: ...
    
    def UsingNamespace(self, usingNamespace: StringType) -> VoidType: ...
    
    def get_ILOffset(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class InternalAssemblyBuilder(RuntimeAssembly, _Assembly, IEvidenceFactory, ICustomAttributeProvider, ISerializable, ICustomQueryInterface):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def CodeBase(self) -> StringType: ...
    
    @property
    def ImageRuntimeVersion(self) -> StringType: ...
    
    @property
    def Location(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetExportedTypes(self) -> ArrayType[TypeType]: ...
    
    def GetFile(self, name: StringType) -> FileStream: ...
    
    @overload
    def GetFiles(self, getResourceModules: BooleanType) -> ArrayType[FileStream]: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def GetManifestResourceInfo(self, resourceName: StringType) -> ManifestResourceInfo: ...
    
    def GetManifestResourceNames(self) -> ArrayType[StringType]: ...
    
    @overload
    def GetManifestResourceStream(self, type: TypeType, name: StringType) -> Stream: ...
    
    @overload
    def GetManifestResourceStream(self, name: StringType) -> Stream: ...
    
    def get_CodeBase(self) -> StringType: ...
    
    def get_ImageRuntimeVersion(self) -> StringType: ...
    
    def get_Location(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class InternalModuleBuilder(RuntimeModule, _Module, ISerializable, ICustomAttributeProvider):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class LineNumberInfo(ObjectType):
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


class LocalBuilder(LocalVariableInfo, _LocalBuilder):
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
    
    @overload
    def SetLocalSymInfo(self, name: StringType) -> VoidType: ...
    
    @overload
    def SetLocalSymInfo(self, name: StringType, startOffset: IntType, endOffset: IntType) -> VoidType: ...
    
    def get_IsPinned(self) -> BooleanType: ...
    
    def get_LocalIndex(self) -> IntType: ...
    
    def get_LocalType(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class LocalSymInfo(ObjectType):
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


class MethodBuilder(MethodInfo, ICustomAttributeProvider, _MemberInfo, _MethodBase, _MethodInfo, _MethodBuilder):
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
    def InitLocals(self) -> BooleanType: ...
    
    @InitLocals.setter
    def InitLocals(self, value: BooleanType) -> None: ...
    
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
    
    @property
    def Signature(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def AddDeclarativeSecurity(self, action: SecurityAction, pset: PermissionSet) -> VoidType: ...
    
    def CreateMethodBody(self, il: ArrayType[ByteType], count: IntType) -> VoidType: ...
    
    def DefineGenericParameters(self, names: ArrayType[StringType]) -> ArrayType[GenericTypeParameterBuilder]: ...
    
    def DefineParameter(self, position: IntType, attributes: ParameterAttributes, strParamName: StringType) -> ParameterBuilder: ...
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetBaseDefinition(self) -> MethodInfo: ...
    
    @overload
    def GetCustomAttributes(self, inherit: BooleanType) -> ArrayType[ObjectType]: ...
    
    @overload
    def GetCustomAttributes(self, attributeType: TypeType, inherit: BooleanType) -> ArrayType[ObjectType]: ...
    
    def GetGenericArguments(self) -> ArrayType[TypeType]: ...
    
    def GetGenericMethodDefinition(self) -> MethodInfo: ...
    
    def GetHashCode(self) -> IntType: ...
    
    @overload
    def GetILGenerator(self) -> ILGenerator: ...
    
    @overload
    def GetILGenerator(self, size: IntType) -> ILGenerator: ...
    
    def GetMethodImplementationFlags(self) -> MethodImplAttributes: ...
    
    def GetModule(self) -> Module: ...
    
    def GetParameters(self) -> ArrayType[ParameterInfo]: ...
    
    def GetToken(self) -> MethodToken: ...
    
    @overload
    def Invoke(self, obj: ObjectType, invokeAttr: BindingFlags, binder: Binder, parameters: ArrayType[ObjectType], culture: CultureInfo) -> ObjectType: ...
    
    def IsDefined(self, attributeType: TypeType, inherit: BooleanType) -> BooleanType: ...
    
    def MakeGenericMethod(self, typeArguments: ArrayType[TypeType]) -> MethodInfo: ...
    
    @overload
    def SetCustomAttribute(self, con: ConstructorInfo, binaryAttribute: ArrayType[ByteType]) -> VoidType: ...
    
    @overload
    def SetCustomAttribute(self, customBuilder: CustomAttributeBuilder) -> VoidType: ...
    
    def SetImplementationFlags(self, attributes: MethodImplAttributes) -> VoidType: ...
    
    def SetMarshal(self, unmanagedMarshal: UnmanagedMarshal) -> VoidType: ...
    
    def SetMethodBody(self, il: ArrayType[ByteType], maxStack: IntType, localSignature: ArrayType[ByteType], exceptionHandlers: IEnumerable[ExceptionHandler], tokenFixups: IEnumerable[IntType]) -> VoidType: ...
    
    def SetParameters(self, parameterTypes: ArrayType[TypeType]) -> VoidType: ...
    
    def SetReturnType(self, returnType: TypeType) -> VoidType: ...
    
    def SetSignature(self, returnType: TypeType, returnTypeRequiredCustomModifiers: ArrayType[TypeType], returnTypeOptionalCustomModifiers: ArrayType[TypeType], parameterTypes: ArrayType[TypeType], parameterTypeRequiredCustomModifiers: ArrayType[TypeType], parameterTypeOptionalCustomModifiers: ArrayType[TypeType]) -> VoidType: ...
    
    def SetSymCustomAttribute(self, name: StringType, data: ArrayType[ByteType]) -> VoidType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Attributes(self) -> MethodAttributes: ...
    
    def get_CallingConvention(self) -> CallingConventions: ...
    
    def get_ContainsGenericParameters(self) -> BooleanType: ...
    
    def get_DeclaringType(self) -> TypeType: ...
    
    def get_InitLocals(self) -> BooleanType: ...
    
    def get_IsGenericMethod(self) -> BooleanType: ...
    
    def get_IsGenericMethodDefinition(self) -> BooleanType: ...
    
    def get_IsSecurityCritical(self) -> BooleanType: ...
    
    def get_IsSecuritySafeCritical(self) -> BooleanType: ...
    
    def get_IsSecurityTransparent(self) -> BooleanType: ...
    
    def get_MethodHandle(self) -> RuntimeMethodHandle: ...
    
    def get_Module(self) -> Module: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_ReflectedType(self) -> TypeType: ...
    
    def get_ReturnParameter(self) -> ParameterInfo: ...
    
    def get_ReturnType(self) -> TypeType: ...
    
    def get_ReturnTypeCustomAttributes(self) -> ICustomAttributeProvider: ...
    
    def get_Signature(self) -> StringType: ...
    
    def set_InitLocals(self, value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MethodBuilderInstantiation(MethodInfo, ICustomAttributeProvider, _MemberInfo, _MethodBase, _MethodInfo):
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
    def MemberType(self) -> MemberTypes: ...
    
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
    
    def GetBaseDefinition(self) -> MethodInfo: ...
    
    @overload
    def GetCustomAttributes(self, inherit: BooleanType) -> ArrayType[ObjectType]: ...
    
    @overload
    def GetCustomAttributes(self, attributeType: TypeType, inherit: BooleanType) -> ArrayType[ObjectType]: ...
    
    def GetGenericArguments(self) -> ArrayType[TypeType]: ...
    
    def GetGenericMethodDefinition(self) -> MethodInfo: ...
    
    def GetMethodImplementationFlags(self) -> MethodImplAttributes: ...
    
    def GetParameters(self) -> ArrayType[ParameterInfo]: ...
    
    @overload
    def GetType(self) -> TypeType: ...
    
    @overload
    def Invoke(self, obj: ObjectType, invokeAttr: BindingFlags, binder: Binder, parameters: ArrayType[ObjectType], culture: CultureInfo) -> ObjectType: ...
    
    def IsDefined(self, attributeType: TypeType, inherit: BooleanType) -> BooleanType: ...
    
    def MakeGenericMethod(self, arguments: ArrayType[TypeType]) -> MethodInfo: ...
    
    def get_Attributes(self) -> MethodAttributes: ...
    
    def get_CallingConvention(self) -> CallingConventions: ...
    
    def get_ContainsGenericParameters(self) -> BooleanType: ...
    
    def get_DeclaringType(self) -> TypeType: ...
    
    def get_IsGenericMethod(self) -> BooleanType: ...
    
    def get_IsGenericMethodDefinition(self) -> BooleanType: ...
    
    def get_MemberType(self) -> MemberTypes: ...
    
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


class MethodOnTypeBuilderInstantiation(MethodInfo, ICustomAttributeProvider, _MemberInfo, _MethodBase, _MethodInfo):
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
    def MemberType(self) -> MemberTypes: ...
    
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
    
    def GetBaseDefinition(self) -> MethodInfo: ...
    
    @overload
    def GetCustomAttributes(self, inherit: BooleanType) -> ArrayType[ObjectType]: ...
    
    @overload
    def GetCustomAttributes(self, attributeType: TypeType, inherit: BooleanType) -> ArrayType[ObjectType]: ...
    
    def GetGenericArguments(self) -> ArrayType[TypeType]: ...
    
    def GetGenericMethodDefinition(self) -> MethodInfo: ...
    
    def GetMethodImplementationFlags(self) -> MethodImplAttributes: ...
    
    def GetParameters(self) -> ArrayType[ParameterInfo]: ...
    
    @overload
    def GetType(self) -> TypeType: ...
    
    @overload
    def Invoke(self, obj: ObjectType, invokeAttr: BindingFlags, binder: Binder, parameters: ArrayType[ObjectType], culture: CultureInfo) -> ObjectType: ...
    
    def IsDefined(self, attributeType: TypeType, inherit: BooleanType) -> BooleanType: ...
    
    def MakeGenericMethod(self, typeArgs: ArrayType[TypeType]) -> MethodInfo: ...
    
    def get_Attributes(self) -> MethodAttributes: ...
    
    def get_CallingConvention(self) -> CallingConventions: ...
    
    def get_ContainsGenericParameters(self) -> BooleanType: ...
    
    def get_DeclaringType(self) -> TypeType: ...
    
    def get_IsGenericMethod(self) -> BooleanType: ...
    
    def get_IsGenericMethodDefinition(self) -> BooleanType: ...
    
    def get_MemberType(self) -> MemberTypes: ...
    
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


class MethodRental(ObjectType, _MethodRental):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def JitImmediate() -> IntType: ...
    
    @staticmethod
    @property
    def JitOnDemand() -> IntType: ...
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def SwapMethodBody(cls: TypeType, methodtoken: IntType, rgIL: NIntType, methodSize: IntType, flags: IntType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ModuleBuilder(Module, _Module, ISerializable, ICustomAttributeProvider, _ModuleBuilder):
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
    
    def CreateGlobalFunctions(self) -> VoidType: ...
    
    def DefineDocument(self, url: StringType, language: Guid, languageVendor: Guid, documentType: Guid) -> ISymbolDocumentWriter: ...
    
    def DefineEnum(self, name: StringType, visibility: TypeAttributes, underlyingType: TypeType) -> EnumBuilder: ...
    
    @overload
    def DefineGlobalMethod(self, name: StringType, attributes: MethodAttributes, returnType: TypeType, parameterTypes: ArrayType[TypeType]) -> MethodBuilder: ...
    
    @overload
    def DefineGlobalMethod(self, name: StringType, attributes: MethodAttributes, callingConvention: CallingConventions, returnType: TypeType, parameterTypes: ArrayType[TypeType]) -> MethodBuilder: ...
    
    @overload
    def DefineGlobalMethod(self, name: StringType, attributes: MethodAttributes, callingConvention: CallingConventions, returnType: TypeType, requiredReturnTypeCustomModifiers: ArrayType[TypeType], optionalReturnTypeCustomModifiers: ArrayType[TypeType], parameterTypes: ArrayType[TypeType], requiredParameterTypeCustomModifiers: ArrayType[TypeType], optionalParameterTypeCustomModifiers: ArrayType[TypeType]) -> MethodBuilder: ...
    
    def DefineInitializedData(self, name: StringType, data: ArrayType[ByteType], attributes: FieldAttributes) -> FieldBuilder: ...
    
    def DefineManifestResource(self, name: StringType, stream: Stream, attribute: ResourceAttributes) -> VoidType: ...
    
    @overload
    def DefinePInvokeMethod(self, name: StringType, dllName: StringType, attributes: MethodAttributes, callingConvention: CallingConventions, returnType: TypeType, parameterTypes: ArrayType[TypeType], nativeCallConv: CallingConvention, nativeCharSet: CharSet) -> MethodBuilder: ...
    
    @overload
    def DefinePInvokeMethod(self, name: StringType, dllName: StringType, entryName: StringType, attributes: MethodAttributes, callingConvention: CallingConventions, returnType: TypeType, parameterTypes: ArrayType[TypeType], nativeCallConv: CallingConvention, nativeCharSet: CharSet) -> MethodBuilder: ...
    
    @overload
    def DefineResource(self, name: StringType, description: StringType) -> IResourceWriter: ...
    
    @overload
    def DefineResource(self, name: StringType, description: StringType, attribute: ResourceAttributes) -> IResourceWriter: ...
    
    @overload
    def DefineType(self, name: StringType, attr: TypeAttributes, parent: TypeType, interfaces: ArrayType[TypeType]) -> TypeBuilder: ...
    
    @overload
    def DefineType(self, name: StringType) -> TypeBuilder: ...
    
    @overload
    def DefineType(self, name: StringType, attr: TypeAttributes) -> TypeBuilder: ...
    
    @overload
    def DefineType(self, name: StringType, attr: TypeAttributes, parent: TypeType) -> TypeBuilder: ...
    
    @overload
    def DefineType(self, name: StringType, attr: TypeAttributes, parent: TypeType, typesize: IntType) -> TypeBuilder: ...
    
    @overload
    def DefineType(self, name: StringType, attr: TypeAttributes, parent: TypeType, packingSize: PackingSize, typesize: IntType) -> TypeBuilder: ...
    
    @overload
    def DefineType(self, name: StringType, attr: TypeAttributes, parent: TypeType, packsize: PackingSize) -> TypeBuilder: ...
    
    def DefineUninitializedData(self, name: StringType, size: IntType, attributes: FieldAttributes) -> FieldBuilder: ...
    
    @overload
    def DefineUnmanagedResource(self, resource: ArrayType[ByteType]) -> VoidType: ...
    
    @overload
    def DefineUnmanagedResource(self, resourceFileName: StringType) -> VoidType: ...
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetArrayMethod(self, arrayClass: TypeType, methodName: StringType, callingConvention: CallingConventions, returnType: TypeType, parameterTypes: ArrayType[TypeType]) -> MethodInfo: ...
    
    def GetArrayMethodToken(self, arrayClass: TypeType, methodName: StringType, callingConvention: CallingConventions, returnType: TypeType, parameterTypes: ArrayType[TypeType]) -> MethodToken: ...
    
    @overload
    def GetConstructorToken(self, constructor: ConstructorInfo, optionalParameterTypes: IEnumerable[TypeType]) -> MethodToken: ...
    
    @overload
    def GetConstructorToken(self, con: ConstructorInfo) -> MethodToken: ...
    
    @overload
    def GetCustomAttributes(self, inherit: BooleanType) -> ArrayType[ObjectType]: ...
    
    @overload
    def GetCustomAttributes(self, attributeType: TypeType, inherit: BooleanType) -> ArrayType[ObjectType]: ...
    
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]: ...
    
    @overload
    def GetField(self, name: StringType, bindingAttr: BindingFlags) -> FieldInfo: ...
    
    def GetFieldToken(self, field: FieldInfo) -> FieldToken: ...
    
    @overload
    def GetFields(self, bindingFlags: BindingFlags) -> ArrayType[FieldInfo]: ...
    
    def GetHashCode(self) -> IntType: ...
    
    @overload
    def GetMethodToken(self, method: MethodInfo) -> MethodToken: ...
    
    @overload
    def GetMethodToken(self, method: MethodInfo, optionalParameterTypes: IEnumerable[TypeType]) -> MethodToken: ...
    
    @overload
    def GetMethods(self, bindingFlags: BindingFlags) -> ArrayType[MethodInfo]: ...
    
    def GetPEKind(self, peKind: PortableExecutableKinds, machine: ImageFileMachine) -> Tuple[VoidType, PortableExecutableKinds, ImageFileMachine]: ...
    
    @overload
    def GetSignatureToken(self, sigHelper: SignatureHelper) -> SignatureToken: ...
    
    @overload
    def GetSignatureToken(self, sigBytes: ArrayType[ByteType], sigLength: IntType) -> SignatureToken: ...
    
    def GetSignerCertificate(self) -> X509Certificate: ...
    
    def GetStringConstant(self, str: StringType) -> StringToken: ...
    
    def GetSymWriter(self) -> ISymbolWriter: ...
    
    @overload
    def GetType(self, className: StringType) -> TypeType: ...
    
    @overload
    def GetType(self, className: StringType, ignoreCase: BooleanType) -> TypeType: ...
    
    @overload
    def GetType(self, className: StringType, throwOnError: BooleanType, ignoreCase: BooleanType) -> TypeType: ...
    
    @overload
    def GetTypeToken(self, type: TypeType) -> TypeToken: ...
    
    @overload
    def GetTypeToken(self, name: StringType) -> TypeToken: ...
    
    def GetTypes(self) -> ArrayType[TypeType]: ...
    
    def IsDefined(self, attributeType: TypeType, inherit: BooleanType) -> BooleanType: ...
    
    def IsResource(self) -> BooleanType: ...
    
    def IsTransient(self) -> BooleanType: ...
    
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
    
    @overload
    def SetCustomAttribute(self, con: ConstructorInfo, binaryAttribute: ArrayType[ByteType]) -> VoidType: ...
    
    @overload
    def SetCustomAttribute(self, customBuilder: CustomAttributeBuilder) -> VoidType: ...
    
    def SetSymCustomAttribute(self, name: StringType, data: ArrayType[ByteType]) -> VoidType: ...
    
    def SetUserEntryPoint(self, entryPoint: MethodInfo) -> VoidType: ...
    
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


class ModuleBuilderData(ObjectType):
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


class NativeVersionInfo(ObjectType):
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


class OpCodes(ObjectType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Add() -> OpCode: ...
    
    @staticmethod
    @property
    def Add_Ovf() -> OpCode: ...
    
    @staticmethod
    @property
    def Add_Ovf_Un() -> OpCode: ...
    
    @staticmethod
    @property
    def And() -> OpCode: ...
    
    @staticmethod
    @property
    def Arglist() -> OpCode: ...
    
    @staticmethod
    @property
    def Beq() -> OpCode: ...
    
    @staticmethod
    @property
    def Beq_S() -> OpCode: ...
    
    @staticmethod
    @property
    def Bge() -> OpCode: ...
    
    @staticmethod
    @property
    def Bge_S() -> OpCode: ...
    
    @staticmethod
    @property
    def Bge_Un() -> OpCode: ...
    
    @staticmethod
    @property
    def Bge_Un_S() -> OpCode: ...
    
    @staticmethod
    @property
    def Bgt() -> OpCode: ...
    
    @staticmethod
    @property
    def Bgt_S() -> OpCode: ...
    
    @staticmethod
    @property
    def Bgt_Un() -> OpCode: ...
    
    @staticmethod
    @property
    def Bgt_Un_S() -> OpCode: ...
    
    @staticmethod
    @property
    def Ble() -> OpCode: ...
    
    @staticmethod
    @property
    def Ble_S() -> OpCode: ...
    
    @staticmethod
    @property
    def Ble_Un() -> OpCode: ...
    
    @staticmethod
    @property
    def Ble_Un_S() -> OpCode: ...
    
    @staticmethod
    @property
    def Blt() -> OpCode: ...
    
    @staticmethod
    @property
    def Blt_S() -> OpCode: ...
    
    @staticmethod
    @property
    def Blt_Un() -> OpCode: ...
    
    @staticmethod
    @property
    def Blt_Un_S() -> OpCode: ...
    
    @staticmethod
    @property
    def Bne_Un() -> OpCode: ...
    
    @staticmethod
    @property
    def Bne_Un_S() -> OpCode: ...
    
    @staticmethod
    @property
    def Box() -> OpCode: ...
    
    @staticmethod
    @property
    def Br() -> OpCode: ...
    
    @staticmethod
    @property
    def Br_S() -> OpCode: ...
    
    @staticmethod
    @property
    def Break() -> OpCode: ...
    
    @staticmethod
    @property
    def Brfalse() -> OpCode: ...
    
    @staticmethod
    @property
    def Brfalse_S() -> OpCode: ...
    
    @staticmethod
    @property
    def Brtrue() -> OpCode: ...
    
    @staticmethod
    @property
    def Brtrue_S() -> OpCode: ...
    
    @staticmethod
    @property
    def Call() -> OpCode: ...
    
    @staticmethod
    @property
    def Calli() -> OpCode: ...
    
    @staticmethod
    @property
    def Callvirt() -> OpCode: ...
    
    @staticmethod
    @property
    def Castclass() -> OpCode: ...
    
    @staticmethod
    @property
    def Ceq() -> OpCode: ...
    
    @staticmethod
    @property
    def Cgt() -> OpCode: ...
    
    @staticmethod
    @property
    def Cgt_Un() -> OpCode: ...
    
    @staticmethod
    @property
    def Ckfinite() -> OpCode: ...
    
    @staticmethod
    @property
    def Clt() -> OpCode: ...
    
    @staticmethod
    @property
    def Clt_Un() -> OpCode: ...
    
    @staticmethod
    @property
    def Constrained() -> OpCode: ...
    
    @staticmethod
    @property
    def Conv_I() -> OpCode: ...
    
    @staticmethod
    @property
    def Conv_I1() -> OpCode: ...
    
    @staticmethod
    @property
    def Conv_I2() -> OpCode: ...
    
    @staticmethod
    @property
    def Conv_I4() -> OpCode: ...
    
    @staticmethod
    @property
    def Conv_I8() -> OpCode: ...
    
    @staticmethod
    @property
    def Conv_Ovf_I() -> OpCode: ...
    
    @staticmethod
    @property
    def Conv_Ovf_I1() -> OpCode: ...
    
    @staticmethod
    @property
    def Conv_Ovf_I1_Un() -> OpCode: ...
    
    @staticmethod
    @property
    def Conv_Ovf_I2() -> OpCode: ...
    
    @staticmethod
    @property
    def Conv_Ovf_I2_Un() -> OpCode: ...
    
    @staticmethod
    @property
    def Conv_Ovf_I4() -> OpCode: ...
    
    @staticmethod
    @property
    def Conv_Ovf_I4_Un() -> OpCode: ...
    
    @staticmethod
    @property
    def Conv_Ovf_I8() -> OpCode: ...
    
    @staticmethod
    @property
    def Conv_Ovf_I8_Un() -> OpCode: ...
    
    @staticmethod
    @property
    def Conv_Ovf_I_Un() -> OpCode: ...
    
    @staticmethod
    @property
    def Conv_Ovf_U() -> OpCode: ...
    
    @staticmethod
    @property
    def Conv_Ovf_U1() -> OpCode: ...
    
    @staticmethod
    @property
    def Conv_Ovf_U1_Un() -> OpCode: ...
    
    @staticmethod
    @property
    def Conv_Ovf_U2() -> OpCode: ...
    
    @staticmethod
    @property
    def Conv_Ovf_U2_Un() -> OpCode: ...
    
    @staticmethod
    @property
    def Conv_Ovf_U4() -> OpCode: ...
    
    @staticmethod
    @property
    def Conv_Ovf_U4_Un() -> OpCode: ...
    
    @staticmethod
    @property
    def Conv_Ovf_U8() -> OpCode: ...
    
    @staticmethod
    @property
    def Conv_Ovf_U8_Un() -> OpCode: ...
    
    @staticmethod
    @property
    def Conv_Ovf_U_Un() -> OpCode: ...
    
    @staticmethod
    @property
    def Conv_R4() -> OpCode: ...
    
    @staticmethod
    @property
    def Conv_R8() -> OpCode: ...
    
    @staticmethod
    @property
    def Conv_R_Un() -> OpCode: ...
    
    @staticmethod
    @property
    def Conv_U() -> OpCode: ...
    
    @staticmethod
    @property
    def Conv_U1() -> OpCode: ...
    
    @staticmethod
    @property
    def Conv_U2() -> OpCode: ...
    
    @staticmethod
    @property
    def Conv_U4() -> OpCode: ...
    
    @staticmethod
    @property
    def Conv_U8() -> OpCode: ...
    
    @staticmethod
    @property
    def Cpblk() -> OpCode: ...
    
    @staticmethod
    @property
    def Cpobj() -> OpCode: ...
    
    @staticmethod
    @property
    def Div() -> OpCode: ...
    
    @staticmethod
    @property
    def Div_Un() -> OpCode: ...
    
    @staticmethod
    @property
    def Dup() -> OpCode: ...
    
    @staticmethod
    @property
    def Endfilter() -> OpCode: ...
    
    @staticmethod
    @property
    def Endfinally() -> OpCode: ...
    
    @staticmethod
    @property
    def Initblk() -> OpCode: ...
    
    @staticmethod
    @property
    def Initobj() -> OpCode: ...
    
    @staticmethod
    @property
    def Isinst() -> OpCode: ...
    
    @staticmethod
    @property
    def Jmp() -> OpCode: ...
    
    @staticmethod
    @property
    def Ldarg() -> OpCode: ...
    
    @staticmethod
    @property
    def Ldarg_0() -> OpCode: ...
    
    @staticmethod
    @property
    def Ldarg_1() -> OpCode: ...
    
    @staticmethod
    @property
    def Ldarg_2() -> OpCode: ...
    
    @staticmethod
    @property
    def Ldarg_3() -> OpCode: ...
    
    @staticmethod
    @property
    def Ldarg_S() -> OpCode: ...
    
    @staticmethod
    @property
    def Ldarga() -> OpCode: ...
    
    @staticmethod
    @property
    def Ldarga_S() -> OpCode: ...
    
    @staticmethod
    @property
    def Ldc_I4() -> OpCode: ...
    
    @staticmethod
    @property
    def Ldc_I4_0() -> OpCode: ...
    
    @staticmethod
    @property
    def Ldc_I4_1() -> OpCode: ...
    
    @staticmethod
    @property
    def Ldc_I4_2() -> OpCode: ...
    
    @staticmethod
    @property
    def Ldc_I4_3() -> OpCode: ...
    
    @staticmethod
    @property
    def Ldc_I4_4() -> OpCode: ...
    
    @staticmethod
    @property
    def Ldc_I4_5() -> OpCode: ...
    
    @staticmethod
    @property
    def Ldc_I4_6() -> OpCode: ...
    
    @staticmethod
    @property
    def Ldc_I4_7() -> OpCode: ...
    
    @staticmethod
    @property
    def Ldc_I4_8() -> OpCode: ...
    
    @staticmethod
    @property
    def Ldc_I4_M1() -> OpCode: ...
    
    @staticmethod
    @property
    def Ldc_I4_S() -> OpCode: ...
    
    @staticmethod
    @property
    def Ldc_I8() -> OpCode: ...
    
    @staticmethod
    @property
    def Ldc_R4() -> OpCode: ...
    
    @staticmethod
    @property
    def Ldc_R8() -> OpCode: ...
    
    @staticmethod
    @property
    def Ldelem() -> OpCode: ...
    
    @staticmethod
    @property
    def Ldelem_I() -> OpCode: ...
    
    @staticmethod
    @property
    def Ldelem_I1() -> OpCode: ...
    
    @staticmethod
    @property
    def Ldelem_I2() -> OpCode: ...
    
    @staticmethod
    @property
    def Ldelem_I4() -> OpCode: ...
    
    @staticmethod
    @property
    def Ldelem_I8() -> OpCode: ...
    
    @staticmethod
    @property
    def Ldelem_R4() -> OpCode: ...
    
    @staticmethod
    @property
    def Ldelem_R8() -> OpCode: ...
    
    @staticmethod
    @property
    def Ldelem_Ref() -> OpCode: ...
    
    @staticmethod
    @property
    def Ldelem_U1() -> OpCode: ...
    
    @staticmethod
    @property
    def Ldelem_U2() -> OpCode: ...
    
    @staticmethod
    @property
    def Ldelem_U4() -> OpCode: ...
    
    @staticmethod
    @property
    def Ldelema() -> OpCode: ...
    
    @staticmethod
    @property
    def Ldfld() -> OpCode: ...
    
    @staticmethod
    @property
    def Ldflda() -> OpCode: ...
    
    @staticmethod
    @property
    def Ldftn() -> OpCode: ...
    
    @staticmethod
    @property
    def Ldind_I() -> OpCode: ...
    
    @staticmethod
    @property
    def Ldind_I1() -> OpCode: ...
    
    @staticmethod
    @property
    def Ldind_I2() -> OpCode: ...
    
    @staticmethod
    @property
    def Ldind_I4() -> OpCode: ...
    
    @staticmethod
    @property
    def Ldind_I8() -> OpCode: ...
    
    @staticmethod
    @property
    def Ldind_R4() -> OpCode: ...
    
    @staticmethod
    @property
    def Ldind_R8() -> OpCode: ...
    
    @staticmethod
    @property
    def Ldind_Ref() -> OpCode: ...
    
    @staticmethod
    @property
    def Ldind_U1() -> OpCode: ...
    
    @staticmethod
    @property
    def Ldind_U2() -> OpCode: ...
    
    @staticmethod
    @property
    def Ldind_U4() -> OpCode: ...
    
    @staticmethod
    @property
    def Ldlen() -> OpCode: ...
    
    @staticmethod
    @property
    def Ldloc() -> OpCode: ...
    
    @staticmethod
    @property
    def Ldloc_0() -> OpCode: ...
    
    @staticmethod
    @property
    def Ldloc_1() -> OpCode: ...
    
    @staticmethod
    @property
    def Ldloc_2() -> OpCode: ...
    
    @staticmethod
    @property
    def Ldloc_3() -> OpCode: ...
    
    @staticmethod
    @property
    def Ldloc_S() -> OpCode: ...
    
    @staticmethod
    @property
    def Ldloca() -> OpCode: ...
    
    @staticmethod
    @property
    def Ldloca_S() -> OpCode: ...
    
    @staticmethod
    @property
    def Ldnull() -> OpCode: ...
    
    @staticmethod
    @property
    def Ldobj() -> OpCode: ...
    
    @staticmethod
    @property
    def Ldsfld() -> OpCode: ...
    
    @staticmethod
    @property
    def Ldsflda() -> OpCode: ...
    
    @staticmethod
    @property
    def Ldstr() -> OpCode: ...
    
    @staticmethod
    @property
    def Ldtoken() -> OpCode: ...
    
    @staticmethod
    @property
    def Ldvirtftn() -> OpCode: ...
    
    @staticmethod
    @property
    def Leave() -> OpCode: ...
    
    @staticmethod
    @property
    def Leave_S() -> OpCode: ...
    
    @staticmethod
    @property
    def Localloc() -> OpCode: ...
    
    @staticmethod
    @property
    def Mkrefany() -> OpCode: ...
    
    @staticmethod
    @property
    def Mul() -> OpCode: ...
    
    @staticmethod
    @property
    def Mul_Ovf() -> OpCode: ...
    
    @staticmethod
    @property
    def Mul_Ovf_Un() -> OpCode: ...
    
    @staticmethod
    @property
    def Neg() -> OpCode: ...
    
    @staticmethod
    @property
    def Newarr() -> OpCode: ...
    
    @staticmethod
    @property
    def Newobj() -> OpCode: ...
    
    @staticmethod
    @property
    def Nop() -> OpCode: ...
    
    @staticmethod
    @property
    def Not() -> OpCode: ...
    
    @staticmethod
    @property
    def Or() -> OpCode: ...
    
    @staticmethod
    @property
    def Pop() -> OpCode: ...
    
    @staticmethod
    @property
    def Prefix1() -> OpCode: ...
    
    @staticmethod
    @property
    def Prefix2() -> OpCode: ...
    
    @staticmethod
    @property
    def Prefix3() -> OpCode: ...
    
    @staticmethod
    @property
    def Prefix4() -> OpCode: ...
    
    @staticmethod
    @property
    def Prefix5() -> OpCode: ...
    
    @staticmethod
    @property
    def Prefix6() -> OpCode: ...
    
    @staticmethod
    @property
    def Prefix7() -> OpCode: ...
    
    @staticmethod
    @property
    def Prefixref() -> OpCode: ...
    
    @staticmethod
    @property
    def Readonly() -> OpCode: ...
    
    @staticmethod
    @property
    def Refanytype() -> OpCode: ...
    
    @staticmethod
    @property
    def Refanyval() -> OpCode: ...
    
    @staticmethod
    @property
    def Rem() -> OpCode: ...
    
    @staticmethod
    @property
    def Rem_Un() -> OpCode: ...
    
    @staticmethod
    @property
    def Ret() -> OpCode: ...
    
    @staticmethod
    @property
    def Rethrow() -> OpCode: ...
    
    @staticmethod
    @property
    def Shl() -> OpCode: ...
    
    @staticmethod
    @property
    def Shr() -> OpCode: ...
    
    @staticmethod
    @property
    def Shr_Un() -> OpCode: ...
    
    @staticmethod
    @property
    def Sizeof() -> OpCode: ...
    
    @staticmethod
    @property
    def Starg() -> OpCode: ...
    
    @staticmethod
    @property
    def Starg_S() -> OpCode: ...
    
    @staticmethod
    @property
    def Stelem() -> OpCode: ...
    
    @staticmethod
    @property
    def Stelem_I() -> OpCode: ...
    
    @staticmethod
    @property
    def Stelem_I1() -> OpCode: ...
    
    @staticmethod
    @property
    def Stelem_I2() -> OpCode: ...
    
    @staticmethod
    @property
    def Stelem_I4() -> OpCode: ...
    
    @staticmethod
    @property
    def Stelem_I8() -> OpCode: ...
    
    @staticmethod
    @property
    def Stelem_R4() -> OpCode: ...
    
    @staticmethod
    @property
    def Stelem_R8() -> OpCode: ...
    
    @staticmethod
    @property
    def Stelem_Ref() -> OpCode: ...
    
    @staticmethod
    @property
    def Stfld() -> OpCode: ...
    
    @staticmethod
    @property
    def Stind_I() -> OpCode: ...
    
    @staticmethod
    @property
    def Stind_I1() -> OpCode: ...
    
    @staticmethod
    @property
    def Stind_I2() -> OpCode: ...
    
    @staticmethod
    @property
    def Stind_I4() -> OpCode: ...
    
    @staticmethod
    @property
    def Stind_I8() -> OpCode: ...
    
    @staticmethod
    @property
    def Stind_R4() -> OpCode: ...
    
    @staticmethod
    @property
    def Stind_R8() -> OpCode: ...
    
    @staticmethod
    @property
    def Stind_Ref() -> OpCode: ...
    
    @staticmethod
    @property
    def Stloc() -> OpCode: ...
    
    @staticmethod
    @property
    def Stloc_0() -> OpCode: ...
    
    @staticmethod
    @property
    def Stloc_1() -> OpCode: ...
    
    @staticmethod
    @property
    def Stloc_2() -> OpCode: ...
    
    @staticmethod
    @property
    def Stloc_3() -> OpCode: ...
    
    @staticmethod
    @property
    def Stloc_S() -> OpCode: ...
    
    @staticmethod
    @property
    def Stobj() -> OpCode: ...
    
    @staticmethod
    @property
    def Stsfld() -> OpCode: ...
    
    @staticmethod
    @property
    def Sub() -> OpCode: ...
    
    @staticmethod
    @property
    def Sub_Ovf() -> OpCode: ...
    
    @staticmethod
    @property
    def Sub_Ovf_Un() -> OpCode: ...
    
    @staticmethod
    @property
    def Switch() -> OpCode: ...
    
    @staticmethod
    @property
    def Tailcall() -> OpCode: ...
    
    @staticmethod
    @property
    def Throw() -> OpCode: ...
    
    @staticmethod
    @property
    def Unaligned() -> OpCode: ...
    
    @staticmethod
    @property
    def Unbox() -> OpCode: ...
    
    @staticmethod
    @property
    def Unbox_Any() -> OpCode: ...
    
    @staticmethod
    @property
    def Volatile() -> OpCode: ...
    
    @staticmethod
    @property
    def Xor() -> OpCode: ...
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def TakesSingleByteArgument(inst: OpCode) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ParameterBuilder(ObjectType, _ParameterBuilder):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Attributes(self) -> IntType: ...
    
    @property
    def IsIn(self) -> BooleanType: ...
    
    @property
    def IsOptional(self) -> BooleanType: ...
    
    @property
    def IsOut(self) -> BooleanType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def Position(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def GetToken(self) -> ParameterToken: ...
    
    def SetConstant(self, defaultValue: ObjectType) -> VoidType: ...
    
    @overload
    def SetCustomAttribute(self, con: ConstructorInfo, binaryAttribute: ArrayType[ByteType]) -> VoidType: ...
    
    @overload
    def SetCustomAttribute(self, customBuilder: CustomAttributeBuilder) -> VoidType: ...
    
    def SetMarshal(self, unmanagedMarshal: UnmanagedMarshal) -> VoidType: ...
    
    def get_Attributes(self) -> IntType: ...
    
    def get_IsIn(self) -> BooleanType: ...
    
    def get_IsOptional(self) -> BooleanType: ...
    
    def get_IsOut(self) -> BooleanType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_Position(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PropertyBuilder(PropertyInfo, ICustomAttributeProvider, _MemberInfo, _PropertyInfo, _PropertyBuilder):
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
    def Module(self) -> Module: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def PropertyToken(self) -> PropertyToken: ...
    
    @property
    def PropertyType(self) -> TypeType: ...
    
    @property
    def ReflectedType(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def AddOtherMethod(self, mdBuilder: MethodBuilder) -> VoidType: ...
    
    @overload
    def GetAccessors(self, nonPublic: BooleanType) -> ArrayType[MethodInfo]: ...
    
    @overload
    def GetCustomAttributes(self, inherit: BooleanType) -> ArrayType[ObjectType]: ...
    
    @overload
    def GetCustomAttributes(self, attributeType: TypeType, inherit: BooleanType) -> ArrayType[ObjectType]: ...
    
    @overload
    def GetGetMethod(self, nonPublic: BooleanType) -> MethodInfo: ...
    
    def GetIndexParameters(self) -> ArrayType[ParameterInfo]: ...
    
    @overload
    def GetSetMethod(self, nonPublic: BooleanType) -> MethodInfo: ...
    
    @overload
    def GetValue(self, obj: ObjectType, index: ArrayType[ObjectType]) -> ObjectType: ...
    
    @overload
    def GetValue(self, obj: ObjectType, invokeAttr: BindingFlags, binder: Binder, index: ArrayType[ObjectType], culture: CultureInfo) -> ObjectType: ...
    
    def IsDefined(self, attributeType: TypeType, inherit: BooleanType) -> BooleanType: ...
    
    def SetConstant(self, defaultValue: ObjectType) -> VoidType: ...
    
    @overload
    def SetCustomAttribute(self, con: ConstructorInfo, binaryAttribute: ArrayType[ByteType]) -> VoidType: ...
    
    @overload
    def SetCustomAttribute(self, customBuilder: CustomAttributeBuilder) -> VoidType: ...
    
    def SetGetMethod(self, mdBuilder: MethodBuilder) -> VoidType: ...
    
    def SetSetMethod(self, mdBuilder: MethodBuilder) -> VoidType: ...
    
    @overload
    def SetValue(self, obj: ObjectType, value: ObjectType, index: ArrayType[ObjectType]) -> VoidType: ...
    
    @overload
    def SetValue(self, obj: ObjectType, value: ObjectType, invokeAttr: BindingFlags, binder: Binder, index: ArrayType[ObjectType], culture: CultureInfo) -> VoidType: ...
    
    def get_Attributes(self) -> PropertyAttributes: ...
    
    def get_CanRead(self) -> BooleanType: ...
    
    def get_CanWrite(self) -> BooleanType: ...
    
    def get_DeclaringType(self) -> TypeType: ...
    
    def get_Module(self) -> Module: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_PropertyToken(self) -> PropertyToken: ...
    
    def get_PropertyType(self) -> TypeType: ...
    
    def get_ReflectedType(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class REDocument(ObjectType):
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


class ResWriterData(ObjectType):
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


class ScopeTree(ObjectType):
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


class SignatureHelper(ObjectType, _SignatureHelper):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def AddArgument(self, clsArgument: TypeType) -> VoidType: ...
    
    @overload
    def AddArgument(self, argument: TypeType, pinned: BooleanType) -> VoidType: ...
    
    @overload
    def AddArgument(self, argument: TypeType, requiredCustomModifiers: ArrayType[TypeType], optionalCustomModifiers: ArrayType[TypeType]) -> VoidType: ...
    
    def AddArguments(self, arguments: ArrayType[TypeType], requiredCustomModifiers: ArrayType[TypeType], optionalCustomModifiers: ArrayType[TypeType]) -> VoidType: ...
    
    def AddSentinel(self) -> VoidType: ...
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @staticmethod
    def GetFieldSigHelper(mod: Module) -> SignatureHelper: ...
    
    def GetHashCode(self) -> IntType: ...
    
    @staticmethod
    @overload
    def GetLocalVarSigHelper() -> SignatureHelper: ...
    
    @staticmethod
    @overload
    def GetLocalVarSigHelper(mod: Module) -> SignatureHelper: ...
    
    @staticmethod
    @overload
    def GetMethodSigHelper(mod: Module, returnType: TypeType, parameterTypes: ArrayType[TypeType]) -> SignatureHelper: ...
    
    @staticmethod
    @overload
    def GetMethodSigHelper(mod: Module, callingConvention: CallingConventions, returnType: TypeType) -> SignatureHelper: ...
    
    @staticmethod
    @overload
    def GetMethodSigHelper(mod: Module, unmanagedCallConv: CallingConvention, returnType: TypeType) -> SignatureHelper: ...
    
    @staticmethod
    @overload
    def GetMethodSigHelper(callingConvention: CallingConventions, returnType: TypeType) -> SignatureHelper: ...
    
    @staticmethod
    @overload
    def GetMethodSigHelper(unmanagedCallingConvention: CallingConvention, returnType: TypeType) -> SignatureHelper: ...
    
    @staticmethod
    @overload
    def GetPropertySigHelper(mod: Module, returnType: TypeType, parameterTypes: ArrayType[TypeType]) -> SignatureHelper: ...
    
    @staticmethod
    @overload
    def GetPropertySigHelper(mod: Module, returnType: TypeType, requiredReturnTypeCustomModifiers: ArrayType[TypeType], optionalReturnTypeCustomModifiers: ArrayType[TypeType], parameterTypes: ArrayType[TypeType], requiredParameterTypeCustomModifiers: ArrayType[TypeType], optionalParameterTypeCustomModifiers: ArrayType[TypeType]) -> SignatureHelper: ...
    
    @staticmethod
    @overload
    def GetPropertySigHelper(mod: Module, callingConvention: CallingConventions, returnType: TypeType, requiredReturnTypeCustomModifiers: ArrayType[TypeType], optionalReturnTypeCustomModifiers: ArrayType[TypeType], parameterTypes: ArrayType[TypeType], requiredParameterTypeCustomModifiers: ArrayType[TypeType], optionalParameterTypeCustomModifiers: ArrayType[TypeType]) -> SignatureHelper: ...
    
    def GetSignature(self) -> ArrayType[ByteType]: ...
    
    def ToString(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SymbolMethod(MethodInfo, ICustomAttributeProvider, _MemberInfo, _MethodBase, _MethodInfo):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Attributes(self) -> MethodAttributes: ...
    
    @property
    def CallingConvention(self) -> CallingConventions: ...
    
    @property
    def DeclaringType(self) -> TypeType: ...
    
    @property
    def MethodHandle(self) -> RuntimeMethodHandle: ...
    
    @property
    def Module(self) -> Module: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def ReflectedType(self) -> TypeType: ...
    
    @property
    def ReturnType(self) -> TypeType: ...
    
    @property
    def ReturnTypeCustomAttributes(self) -> ICustomAttributeProvider: ...
    
    # ---------- Methods ---------- #
    
    def GetBaseDefinition(self) -> MethodInfo: ...
    
    @overload
    def GetCustomAttributes(self, inherit: BooleanType) -> ArrayType[ObjectType]: ...
    
    @overload
    def GetCustomAttributes(self, attributeType: TypeType, inherit: BooleanType) -> ArrayType[ObjectType]: ...
    
    def GetMethodImplementationFlags(self) -> MethodImplAttributes: ...
    
    def GetModule(self) -> Module: ...
    
    def GetParameters(self) -> ArrayType[ParameterInfo]: ...
    
    def GetToken(self) -> MethodToken: ...
    
    @overload
    def Invoke(self, obj: ObjectType, invokeAttr: BindingFlags, binder: Binder, parameters: ArrayType[ObjectType], culture: CultureInfo) -> ObjectType: ...
    
    def IsDefined(self, attributeType: TypeType, inherit: BooleanType) -> BooleanType: ...
    
    def get_Attributes(self) -> MethodAttributes: ...
    
    def get_CallingConvention(self) -> CallingConventions: ...
    
    def get_DeclaringType(self) -> TypeType: ...
    
    def get_MethodHandle(self) -> RuntimeMethodHandle: ...
    
    def get_Module(self) -> Module: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_ReflectedType(self) -> TypeType: ...
    
    def get_ReturnType(self) -> TypeType: ...
    
    def get_ReturnTypeCustomAttributes(self) -> ICustomAttributeProvider: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SymbolType(TypeInfo, ICustomAttributeProvider, _MemberInfo, _Type, IReflect, IReflectableType):
    # No Fields
    
    # No Constructors
    
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
    
    def GetArrayRank(self) -> IntType: ...
    
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
    
    @overload
    def MakeArrayType(self) -> TypeType: ...
    
    @overload
    def MakeArrayType(self, rank: IntType) -> TypeType: ...
    
    def MakeByRefType(self) -> TypeType: ...
    
    def MakePointerType(self) -> TypeType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Assembly(self) -> Assembly: ...
    
    def get_AssemblyQualifiedName(self) -> StringType: ...
    
    def get_BaseType(self) -> TypeType: ...
    
    def get_FullName(self) -> StringType: ...
    
    def get_GUID(self) -> Guid: ...
    
    def get_IsConstructedGenericType(self) -> BooleanType: ...
    
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


class TypeBuilder(TypeInfo, ICustomAttributeProvider, _MemberInfo, _Type, IReflect, IReflectableType, _TypeBuilder):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def UnspecifiedTypeSize() -> IntType: ...
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Assembly(self) -> Assembly: ...
    
    @property
    def AssemblyQualifiedName(self) -> StringType: ...
    
    @property
    def BaseType(self) -> TypeType: ...
    
    @property
    def DeclaringMethod(self) -> MethodBase: ...
    
    @property
    def DeclaringType(self) -> TypeType: ...
    
    @property
    def FullName(self) -> StringType: ...
    
    @property
    def GUID(self) -> Guid: ...
    
    @property
    def GenericParameterAttributes(self) -> GenericParameterAttributes: ...
    
    @property
    def GenericParameterPosition(self) -> IntType: ...
    
    @property
    def IsConstructedGenericType(self) -> BooleanType: ...
    
    @property
    def IsGenericParameter(self) -> BooleanType: ...
    
    @property
    def IsGenericType(self) -> BooleanType: ...
    
    @property
    def IsGenericTypeDefinition(self) -> BooleanType: ...
    
    @property
    def IsSecurityCritical(self) -> BooleanType: ...
    
    @property
    def IsSecuritySafeCritical(self) -> BooleanType: ...
    
    @property
    def IsSecurityTransparent(self) -> BooleanType: ...
    
    @property
    def Module(self) -> Module: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def Namespace(self) -> StringType: ...
    
    @property
    def PackingSize(self) -> PackingSize: ...
    
    @property
    def ReflectedType(self) -> TypeType: ...
    
    @property
    def Size(self) -> IntType: ...
    
    @property
    def TypeHandle(self) -> RuntimeTypeHandle: ...
    
    @property
    def TypeToken(self) -> TypeToken: ...
    
    @property
    def UnderlyingSystemType(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def AddDeclarativeSecurity(self, action: SecurityAction, pset: PermissionSet) -> VoidType: ...
    
    def AddInterfaceImplementation(self, interfaceType: TypeType) -> VoidType: ...
    
    def CreateType(self) -> TypeType: ...
    
    def CreateTypeInfo(self) -> TypeInfo: ...
    
    @overload
    def DefineConstructor(self, attributes: MethodAttributes, callingConvention: CallingConventions, parameterTypes: ArrayType[TypeType]) -> ConstructorBuilder: ...
    
    @overload
    def DefineConstructor(self, attributes: MethodAttributes, callingConvention: CallingConventions, parameterTypes: ArrayType[TypeType], requiredCustomModifiers: ArrayType[TypeType], optionalCustomModifiers: ArrayType[TypeType]) -> ConstructorBuilder: ...
    
    def DefineDefaultConstructor(self, attributes: MethodAttributes) -> ConstructorBuilder: ...
    
    def DefineEvent(self, name: StringType, attributes: EventAttributes, eventtype: TypeType) -> EventBuilder: ...
    
    @overload
    def DefineField(self, fieldName: StringType, type: TypeType, requiredCustomModifiers: ArrayType[TypeType], optionalCustomModifiers: ArrayType[TypeType], attributes: FieldAttributes) -> FieldBuilder: ...
    
    @overload
    def DefineField(self, fieldName: StringType, type: TypeType, attributes: FieldAttributes) -> FieldBuilder: ...
    
    def DefineGenericParameters(self, names: ArrayType[StringType]) -> ArrayType[GenericTypeParameterBuilder]: ...
    
    def DefineInitializedData(self, name: StringType, data: ArrayType[ByteType], attributes: FieldAttributes) -> FieldBuilder: ...
    
    @overload
    def DefineMethod(self, name: StringType, attributes: MethodAttributes, callingConvention: CallingConventions, returnType: TypeType, returnTypeRequiredCustomModifiers: ArrayType[TypeType], returnTypeOptionalCustomModifiers: ArrayType[TypeType], parameterTypes: ArrayType[TypeType], parameterTypeRequiredCustomModifiers: ArrayType[TypeType], parameterTypeOptionalCustomModifiers: ArrayType[TypeType]) -> MethodBuilder: ...
    
    @overload
    def DefineMethod(self, name: StringType, attributes: MethodAttributes, returnType: TypeType, parameterTypes: ArrayType[TypeType]) -> MethodBuilder: ...
    
    @overload
    def DefineMethod(self, name: StringType, attributes: MethodAttributes) -> MethodBuilder: ...
    
    @overload
    def DefineMethod(self, name: StringType, attributes: MethodAttributes, callingConvention: CallingConventions) -> MethodBuilder: ...
    
    @overload
    def DefineMethod(self, name: StringType, attributes: MethodAttributes, callingConvention: CallingConventions, returnType: TypeType, parameterTypes: ArrayType[TypeType]) -> MethodBuilder: ...
    
    def DefineMethodOverride(self, methodInfoBody: MethodInfo, methodInfoDeclaration: MethodInfo) -> VoidType: ...
    
    @overload
    def DefineNestedType(self, name: StringType) -> TypeBuilder: ...
    
    @overload
    def DefineNestedType(self, name: StringType, attr: TypeAttributes, parent: TypeType, interfaces: ArrayType[TypeType]) -> TypeBuilder: ...
    
    @overload
    def DefineNestedType(self, name: StringType, attr: TypeAttributes, parent: TypeType) -> TypeBuilder: ...
    
    @overload
    def DefineNestedType(self, name: StringType, attr: TypeAttributes) -> TypeBuilder: ...
    
    @overload
    def DefineNestedType(self, name: StringType, attr: TypeAttributes, parent: TypeType, typeSize: IntType) -> TypeBuilder: ...
    
    @overload
    def DefineNestedType(self, name: StringType, attr: TypeAttributes, parent: TypeType, packSize: PackingSize) -> TypeBuilder: ...
    
    @overload
    def DefineNestedType(self, name: StringType, attr: TypeAttributes, parent: TypeType, packSize: PackingSize, typeSize: IntType) -> TypeBuilder: ...
    
    @overload
    def DefinePInvokeMethod(self, name: StringType, dllName: StringType, attributes: MethodAttributes, callingConvention: CallingConventions, returnType: TypeType, parameterTypes: ArrayType[TypeType], nativeCallConv: CallingConvention, nativeCharSet: CharSet) -> MethodBuilder: ...
    
    @overload
    def DefinePInvokeMethod(self, name: StringType, dllName: StringType, entryName: StringType, attributes: MethodAttributes, callingConvention: CallingConventions, returnType: TypeType, parameterTypes: ArrayType[TypeType], nativeCallConv: CallingConvention, nativeCharSet: CharSet) -> MethodBuilder: ...
    
    @overload
    def DefinePInvokeMethod(self, name: StringType, dllName: StringType, entryName: StringType, attributes: MethodAttributes, callingConvention: CallingConventions, returnType: TypeType, returnTypeRequiredCustomModifiers: ArrayType[TypeType], returnTypeOptionalCustomModifiers: ArrayType[TypeType], parameterTypes: ArrayType[TypeType], parameterTypeRequiredCustomModifiers: ArrayType[TypeType], parameterTypeOptionalCustomModifiers: ArrayType[TypeType], nativeCallConv: CallingConvention, nativeCharSet: CharSet) -> MethodBuilder: ...
    
    @overload
    def DefineProperty(self, name: StringType, attributes: PropertyAttributes, callingConvention: CallingConventions, returnType: TypeType, returnTypeRequiredCustomModifiers: ArrayType[TypeType], returnTypeOptionalCustomModifiers: ArrayType[TypeType], parameterTypes: ArrayType[TypeType], parameterTypeRequiredCustomModifiers: ArrayType[TypeType], parameterTypeOptionalCustomModifiers: ArrayType[TypeType]) -> PropertyBuilder: ...
    
    @overload
    def DefineProperty(self, name: StringType, attributes: PropertyAttributes, returnType: TypeType, parameterTypes: ArrayType[TypeType]) -> PropertyBuilder: ...
    
    @overload
    def DefineProperty(self, name: StringType, attributes: PropertyAttributes, callingConvention: CallingConventions, returnType: TypeType, parameterTypes: ArrayType[TypeType]) -> PropertyBuilder: ...
    
    @overload
    def DefineProperty(self, name: StringType, attributes: PropertyAttributes, returnType: TypeType, returnTypeRequiredCustomModifiers: ArrayType[TypeType], returnTypeOptionalCustomModifiers: ArrayType[TypeType], parameterTypes: ArrayType[TypeType], parameterTypeRequiredCustomModifiers: ArrayType[TypeType], parameterTypeOptionalCustomModifiers: ArrayType[TypeType]) -> PropertyBuilder: ...
    
    def DefineTypeInitializer(self) -> ConstructorBuilder: ...
    
    def DefineUninitializedData(self, name: StringType, size: IntType, attributes: FieldAttributes) -> FieldBuilder: ...
    
    @staticmethod
    @overload
    def GetConstructor(type: TypeType, constructor: ConstructorInfo) -> ConstructorInfo: ...
    
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
    
    @staticmethod
    @overload
    def GetField(type: TypeType, field: FieldInfo) -> FieldInfo: ...
    
    @overload
    def GetField(self, name: StringType, bindingAttr: BindingFlags) -> FieldInfo: ...
    
    @overload
    def GetFields(self, bindingAttr: BindingFlags) -> ArrayType[FieldInfo]: ...
    
    def GetGenericArguments(self) -> ArrayType[TypeType]: ...
    
    def GetGenericTypeDefinition(self) -> TypeType: ...
    
    @overload
    def GetInterface(self, name: StringType, ignoreCase: BooleanType) -> TypeType: ...
    
    def GetInterfaceMap(self, interfaceType: TypeType) -> InterfaceMapping: ...
    
    def GetInterfaces(self) -> ArrayType[TypeType]: ...
    
    @overload
    def GetMember(self, name: StringType, type: MemberTypes, bindingAttr: BindingFlags) -> ArrayType[MemberInfo]: ...
    
    @overload
    def GetMembers(self, bindingAttr: BindingFlags) -> ArrayType[MemberInfo]: ...
    
    @staticmethod
    @overload
    def GetMethod(type: TypeType, method: MethodInfo) -> MethodInfo: ...
    
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
    
    @overload
    def IsAssignableFrom(self, c: TypeType) -> BooleanType: ...
    
    def IsCreated(self) -> BooleanType: ...
    
    def IsDefined(self, attributeType: TypeType, inherit: BooleanType) -> BooleanType: ...
    
    def IsSubclassOf(self, c: TypeType) -> BooleanType: ...
    
    @overload
    def MakeArrayType(self) -> TypeType: ...
    
    @overload
    def MakeArrayType(self, rank: IntType) -> TypeType: ...
    
    def MakeByRefType(self) -> TypeType: ...
    
    def MakeGenericType(self, typeArguments: ArrayType[TypeType]) -> TypeType: ...
    
    def MakePointerType(self) -> TypeType: ...
    
    @overload
    def SetCustomAttribute(self, con: ConstructorInfo, binaryAttribute: ArrayType[ByteType]) -> VoidType: ...
    
    @overload
    def SetCustomAttribute(self, customBuilder: CustomAttributeBuilder) -> VoidType: ...
    
    def SetParent(self, parent: TypeType) -> VoidType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Assembly(self) -> Assembly: ...
    
    def get_AssemblyQualifiedName(self) -> StringType: ...
    
    def get_BaseType(self) -> TypeType: ...
    
    def get_DeclaringMethod(self) -> MethodBase: ...
    
    def get_DeclaringType(self) -> TypeType: ...
    
    def get_FullName(self) -> StringType: ...
    
    def get_GUID(self) -> Guid: ...
    
    def get_GenericParameterAttributes(self) -> GenericParameterAttributes: ...
    
    def get_GenericParameterPosition(self) -> IntType: ...
    
    def get_IsConstructedGenericType(self) -> BooleanType: ...
    
    def get_IsGenericParameter(self) -> BooleanType: ...
    
    def get_IsGenericType(self) -> BooleanType: ...
    
    def get_IsGenericTypeDefinition(self) -> BooleanType: ...
    
    def get_IsSecurityCritical(self) -> BooleanType: ...
    
    def get_IsSecuritySafeCritical(self) -> BooleanType: ...
    
    def get_IsSecurityTransparent(self) -> BooleanType: ...
    
    @overload
    def get_Module(self) -> Module: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_Namespace(self) -> StringType: ...
    
    def get_PackingSize(self) -> PackingSize: ...
    
    def get_ReflectedType(self) -> TypeType: ...
    
    def get_Size(self) -> IntType: ...
    
    def get_TypeHandle(self) -> RuntimeTypeHandle: ...
    
    def get_TypeToken(self) -> TypeToken: ...
    
    def get_UnderlyingSystemType(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TypeBuilderInstantiation(TypeInfo, ICustomAttributeProvider, _MemberInfo, _Type, IReflect, IReflectableType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Assembly(self) -> Assembly: ...
    
    @property
    def AssemblyQualifiedName(self) -> StringType: ...
    
    @property
    def BaseType(self) -> TypeType: ...
    
    @property
    def ContainsGenericParameters(self) -> BooleanType: ...
    
    @property
    def DeclaringMethod(self) -> MethodBase: ...
    
    @property
    def DeclaringType(self) -> TypeType: ...
    
    @property
    def FullName(self) -> StringType: ...
    
    @property
    def GUID(self) -> Guid: ...
    
    @property
    def GenericParameterPosition(self) -> IntType: ...
    
    @property
    def IsConstructedGenericType(self) -> BooleanType: ...
    
    @property
    def IsGenericParameter(self) -> BooleanType: ...
    
    @property
    def IsGenericType(self) -> BooleanType: ...
    
    @property
    def IsGenericTypeDefinition(self) -> BooleanType: ...
    
    @property
    def Module(self) -> Module: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def Namespace(self) -> StringType: ...
    
    @property
    def ReflectedType(self) -> TypeType: ...
    
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
    
    def GetGenericArguments(self) -> ArrayType[TypeType]: ...
    
    def GetGenericTypeDefinition(self) -> TypeType: ...
    
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
    
    @overload
    def IsAssignableFrom(self, c: TypeType) -> BooleanType: ...
    
    def IsDefined(self, attributeType: TypeType, inherit: BooleanType) -> BooleanType: ...
    
    def IsSubclassOf(self, c: TypeType) -> BooleanType: ...
    
    @overload
    def MakeArrayType(self) -> TypeType: ...
    
    @overload
    def MakeArrayType(self, rank: IntType) -> TypeType: ...
    
    def MakeByRefType(self) -> TypeType: ...
    
    def MakeGenericType(self, inst: ArrayType[TypeType]) -> TypeType: ...
    
    def MakePointerType(self) -> TypeType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Assembly(self) -> Assembly: ...
    
    def get_AssemblyQualifiedName(self) -> StringType: ...
    
    def get_BaseType(self) -> TypeType: ...
    
    def get_ContainsGenericParameters(self) -> BooleanType: ...
    
    def get_DeclaringMethod(self) -> MethodBase: ...
    
    def get_DeclaringType(self) -> TypeType: ...
    
    def get_FullName(self) -> StringType: ...
    
    def get_GUID(self) -> Guid: ...
    
    def get_GenericParameterPosition(self) -> IntType: ...
    
    def get_IsConstructedGenericType(self) -> BooleanType: ...
    
    def get_IsGenericParameter(self) -> BooleanType: ...
    
    def get_IsGenericType(self) -> BooleanType: ...
    
    def get_IsGenericTypeDefinition(self) -> BooleanType: ...
    
    @overload
    def get_Module(self) -> Module: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_Namespace(self) -> StringType: ...
    
    def get_ReflectedType(self) -> TypeType: ...
    
    def get_TypeHandle(self) -> RuntimeTypeHandle: ...
    
    def get_UnderlyingSystemType(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TypeNameBuilder(ObjectType):
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


class UnmanagedMarshal(ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def BaseType(self) -> UnmanagedType: ...
    
    @property
    def ElementCount(self) -> IntType: ...
    
    @property
    def GetUnmanagedType(self) -> UnmanagedType: ...
    
    @property
    def IIDGuid(self) -> Guid: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def DefineByValArray(elemCount: IntType) -> UnmanagedMarshal: ...
    
    @staticmethod
    def DefineByValTStr(elemCount: IntType) -> UnmanagedMarshal: ...
    
    @staticmethod
    def DefineLPArray(elemType: UnmanagedType) -> UnmanagedMarshal: ...
    
    @staticmethod
    def DefineSafeArray(elemType: UnmanagedType) -> UnmanagedMarshal: ...
    
    @staticmethod
    def DefineUnmanagedMarshal(unmanagedType: UnmanagedType) -> UnmanagedMarshal: ...
    
    def get_BaseType(self) -> UnmanagedType: ...
    
    def get_ElementCount(self) -> IntType: ...
    
    def get_GetUnmanagedType(self) -> UnmanagedType: ...
    
    def get_IIDGuid(self) -> Guid: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class VarArgMethod(ObjectType):
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


class __ExceptionInfo(ObjectType):
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


# ---------- Structs ---------- #

class EventToken(ValueType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Empty() -> EventToken: ...
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Token(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, obj: EventToken) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def get_Token(self) -> IntType: ...
    
    @staticmethod
    def op_Equality(a: EventToken, b: EventToken) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(a: EventToken, b: EventToken) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ExceptionHandler(ValueType, IEquatable[ExceptionHandler]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, tryOffset: IntType, tryLength: IntType, filterOffset: IntType, handlerOffset: IntType, handlerLength: IntType, kind: ExceptionHandlingClauseOptions, exceptionTypeToken: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ExceptionTypeToken(self) -> IntType: ...
    
    @property
    def FilterOffset(self) -> IntType: ...
    
    @property
    def HandlerLength(self) -> IntType: ...
    
    @property
    def HandlerOffset(self) -> IntType: ...
    
    @property
    def Kind(self) -> ExceptionHandlingClauseOptions: ...
    
    @property
    def TryLength(self) -> IntType: ...
    
    @property
    def TryOffset(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, other: ExceptionHandler) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def get_ExceptionTypeToken(self) -> IntType: ...
    
    def get_FilterOffset(self) -> IntType: ...
    
    def get_HandlerLength(self) -> IntType: ...
    
    def get_HandlerOffset(self) -> IntType: ...
    
    def get_Kind(self) -> ExceptionHandlingClauseOptions: ...
    
    def get_TryLength(self) -> IntType: ...
    
    def get_TryOffset(self) -> IntType: ...
    
    @staticmethod
    def op_Equality(left: ExceptionHandler, right: ExceptionHandler) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(left: ExceptionHandler, right: ExceptionHandler) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class FieldToken(ValueType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Empty() -> FieldToken: ...
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Token(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, obj: FieldToken) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def get_Token(self) -> IntType: ...
    
    @staticmethod
    def op_Equality(a: FieldToken, b: FieldToken) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(a: FieldToken, b: FieldToken) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Label(ValueType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def Equals(self, obj: Label) -> BooleanType: ...
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    @staticmethod
    def op_Equality(a: Label, b: Label) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(a: Label, b: Label) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MethodToken(ValueType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Empty() -> MethodToken: ...
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Token(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, obj: MethodToken) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def get_Token(self) -> IntType: ...
    
    @staticmethod
    def op_Equality(a: MethodToken, b: MethodToken) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(a: MethodToken, b: MethodToken) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class OpCode(ValueType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def FlowControl(self) -> FlowControl: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def OpCodeType(self) -> OpCodeType: ...
    
    @property
    def OperandType(self) -> OperandType: ...
    
    @property
    def Size(self) -> IntType: ...
    
    @property
    def StackBehaviourPop(self) -> StackBehaviour: ...
    
    @property
    def StackBehaviourPush(self) -> StackBehaviour: ...
    
    @property
    def Value(self) -> ShortType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Equals(self, obj: OpCode) -> BooleanType: ...
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_FlowControl(self) -> FlowControl: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_OpCodeType(self) -> OpCodeType: ...
    
    def get_OperandType(self) -> OperandType: ...
    
    def get_Size(self) -> IntType: ...
    
    def get_StackBehaviourPop(self) -> StackBehaviour: ...
    
    def get_StackBehaviourPush(self) -> StackBehaviour: ...
    
    def get_Value(self) -> ShortType: ...
    
    @staticmethod
    def op_Equality(a: OpCode, b: OpCode) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(a: OpCode, b: OpCode) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ParameterToken(ValueType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Empty() -> ParameterToken: ...
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Token(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, obj: ParameterToken) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def get_Token(self) -> IntType: ...
    
    @staticmethod
    def op_Equality(a: ParameterToken, b: ParameterToken) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(a: ParameterToken, b: ParameterToken) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PropertyToken(ValueType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Empty() -> PropertyToken: ...
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Token(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, obj: PropertyToken) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def get_Token(self) -> IntType: ...
    
    @staticmethod
    def op_Equality(a: PropertyToken, b: PropertyToken) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(a: PropertyToken, b: PropertyToken) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SignatureToken(ValueType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Empty() -> SignatureToken: ...
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Token(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, obj: SignatureToken) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def get_Token(self) -> IntType: ...
    
    @staticmethod
    def op_Equality(a: SignatureToken, b: SignatureToken) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(a: SignatureToken, b: SignatureToken) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class StringToken(ValueType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Token(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, obj: StringToken) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def get_Token(self) -> IntType: ...
    
    @staticmethod
    def op_Equality(a: StringToken, b: StringToken) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(a: StringToken, b: StringToken) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TypeToken(ValueType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Empty() -> TypeToken: ...
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Token(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, obj: TypeToken) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def get_Token(self) -> IntType: ...
    
    @staticmethod
    def op_Equality(a: TypeToken, b: TypeToken) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(a: TypeToken, b: TypeToken) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class __FixupData(ValueType):
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


# No Interfaces

# ---------- Enums ---------- #

class AssemblyBuilderAccess(Enum):
    Run = 1
    Save = 2
    RunAndSave = 3
    ReflectionOnly = 6
    RunAndCollect = 9


class DynamicAssemblyFlags(Enum):
    #None = 0
    AllCritical = 1
    Aptca = 2
    Critical = 4
    Transparent = 8
    TreatAsSafe = 16


class FlowControl(Enum):
    Branch = 0
    Break = 1
    Call = 2
    Cond_Branch = 3
    Meta = 4
    Next = 5
    Phi = 6
    Return = 7
    Throw = 8


class OpCodeType(Enum):
    Annotation = 0
    Macro = 1
    Nternal = 2
    Objmodel = 3
    Prefix = 4
    Primitive = 5


class OpCodeValues(Enum):
    Nop = 0
    Break = 1
    Ldarg_0 = 2
    Ldarg_1 = 3
    Ldarg_2 = 4
    Ldarg_3 = 5
    Ldloc_0 = 6
    Ldloc_1 = 7
    Ldloc_2 = 8
    Ldloc_3 = 9
    Stloc_0 = 10
    Stloc_1 = 11
    Stloc_2 = 12
    Stloc_3 = 13
    Ldarg_S = 14
    Ldarga_S = 15
    Starg_S = 16
    Ldloc_S = 17
    Ldloca_S = 18
    Stloc_S = 19
    Ldnull = 20
    Ldc_I4_M1 = 21
    Ldc_I4_0 = 22
    Ldc_I4_1 = 23
    Ldc_I4_2 = 24
    Ldc_I4_3 = 25
    Ldc_I4_4 = 26
    Ldc_I4_5 = 27
    Ldc_I4_6 = 28
    Ldc_I4_7 = 29
    Ldc_I4_8 = 30
    Ldc_I4_S = 31
    Ldc_I4 = 32
    Ldc_I8 = 33
    Ldc_R4 = 34
    Ldc_R8 = 35
    Dup = 37
    Pop = 38
    Jmp = 39
    Call = 40
    Calli = 41
    Ret = 42
    Br_S = 43
    Brfalse_S = 44
    Brtrue_S = 45
    Beq_S = 46
    Bge_S = 47
    Bgt_S = 48
    Ble_S = 49
    Blt_S = 50
    Bne_Un_S = 51
    Bge_Un_S = 52
    Bgt_Un_S = 53
    Ble_Un_S = 54
    Blt_Un_S = 55
    Br = 56
    Brfalse = 57
    Brtrue = 58
    Beq = 59
    Bge = 60
    Bgt = 61
    Ble = 62
    Blt = 63
    Bne_Un = 64
    Bge_Un = 65
    Bgt_Un = 66
    Ble_Un = 67
    Blt_Un = 68
    Switch = 69
    Ldind_I1 = 70
    Ldind_U1 = 71
    Ldind_I2 = 72
    Ldind_U2 = 73
    Ldind_I4 = 74
    Ldind_U4 = 75
    Ldind_I8 = 76
    Ldind_I = 77
    Ldind_R4 = 78
    Ldind_R8 = 79
    Ldind_Ref = 80
    Stind_Ref = 81
    Stind_I1 = 82
    Stind_I2 = 83
    Stind_I4 = 84
    Stind_I8 = 85
    Stind_R4 = 86
    Stind_R8 = 87
    Add = 88
    Sub = 89
    Mul = 90
    Div = 91
    Div_Un = 92
    Rem = 93
    Rem_Un = 94
    And = 95
    Or = 96
    Xor = 97
    Shl = 98
    Shr = 99
    Shr_Un = 100
    Neg = 101
    Not = 102
    Conv_I1 = 103
    Conv_I2 = 104
    Conv_I4 = 105
    Conv_I8 = 106
    Conv_R4 = 107
    Conv_R8 = 108
    Conv_U4 = 109
    Conv_U8 = 110
    Callvirt = 111
    Cpobj = 112
    Ldobj = 113
    Ldstr = 114
    Newobj = 115
    Castclass = 116
    Isinst = 117
    Conv_R_Un = 118
    Unbox = 121
    Throw = 122
    Ldfld = 123
    Ldflda = 124
    Stfld = 125
    Ldsfld = 126
    Ldsflda = 127
    Stsfld = 128
    Stobj = 129
    Conv_Ovf_I1_Un = 130
    Conv_Ovf_I2_Un = 131
    Conv_Ovf_I4_Un = 132
    Conv_Ovf_I8_Un = 133
    Conv_Ovf_U1_Un = 134
    Conv_Ovf_U2_Un = 135
    Conv_Ovf_U4_Un = 136
    Conv_Ovf_U8_Un = 137
    Conv_Ovf_I_Un = 138
    Conv_Ovf_U_Un = 139
    Box = 140
    Newarr = 141
    Ldlen = 142
    Ldelema = 143
    Ldelem_I1 = 144
    Ldelem_U1 = 145
    Ldelem_I2 = 146
    Ldelem_U2 = 147
    Ldelem_I4 = 148
    Ldelem_U4 = 149
    Ldelem_I8 = 150
    Ldelem_I = 151
    Ldelem_R4 = 152
    Ldelem_R8 = 153
    Ldelem_Ref = 154
    Stelem_I = 155
    Stelem_I1 = 156
    Stelem_I2 = 157
    Stelem_I4 = 158
    Stelem_I8 = 159
    Stelem_R4 = 160
    Stelem_R8 = 161
    Stelem_Ref = 162
    Ldelem = 163
    Stelem = 164
    Unbox_Any = 165
    Conv_Ovf_I1 = 179
    Conv_Ovf_U1 = 180
    Conv_Ovf_I2 = 181
    Conv_Ovf_U2 = 182
    Conv_Ovf_I4 = 183
    Conv_Ovf_U4 = 184
    Conv_Ovf_I8 = 185
    Conv_Ovf_U8 = 186
    Refanyval = 194
    Ckfinite = 195
    Mkrefany = 198
    Ldtoken = 208
    Conv_U2 = 209
    Conv_U1 = 210
    Conv_I = 211
    Conv_Ovf_I = 212
    Conv_Ovf_U = 213
    Add_Ovf = 214
    Add_Ovf_Un = 215
    Mul_Ovf = 216
    Mul_Ovf_Un = 217
    Sub_Ovf = 218
    Sub_Ovf_Un = 219
    Endfinally = 220
    Leave = 221
    Leave_S = 222
    Stind_I = 223
    Conv_U = 224
    Prefix7 = 248
    Prefix6 = 249
    Prefix5 = 250
    Prefix4 = 251
    Prefix3 = 252
    Prefix2 = 253
    Prefix1 = 254
    Prefixref = 255
    Arglist = 65024
    Ceq = 65025
    Cgt = 65026
    Cgt_Un = 65027
    Clt = 65028
    Clt_Un = 65029
    Ldftn = 65030
    Ldvirtftn = 65031
    Ldarg = 65033
    Ldarga = 65034
    Starg = 65035
    Ldloc = 65036
    Ldloca = 65037
    Stloc = 65038
    Localloc = 65039
    Endfilter = 65041
    Unaligned_ = 65042
    Volatile_ = 65043
    Tail_ = 65044
    Initobj = 65045
    Constrained_ = 65046
    Cpblk = 65047
    Initblk = 65048
    Rethrow = 65050
    Sizeof = 65052
    Refanytype = 65053
    Readonly_ = 65054


class OperandType(Enum):
    InlineBrTarget = 0
    InlineField = 1
    InlineI = 2
    InlineI8 = 3
    InlineMethod = 4
    InlineNone = 5
    InlinePhi = 6
    InlineR = 7
    InlineSig = 9
    InlineString = 10
    InlineSwitch = 11
    InlineTok = 12
    InlineType = 13
    InlineVar = 14
    ShortInlineBrTarget = 15
    ShortInlineI = 16
    ShortInlineR = 17
    ShortInlineVar = 18


class PEFileKinds(Enum):
    Dll = 1
    ConsoleApplication = 2
    WindowApplication = 3


class PackingSize(Enum):
    Unspecified = 0
    Size1 = 1
    Size2 = 2
    Size4 = 4
    Size8 = 8
    Size16 = 16
    Size32 = 32
    Size64 = 64
    Size128 = 128


class ScopeAction(Enum):
    Open = 0
    Close = 1


class StackBehaviour(Enum):
    Pop0 = 0
    Pop1 = 1
    Pop1_pop1 = 2
    Popi = 3
    Popi_pop1 = 4
    Popi_popi = 5
    Popi_popi8 = 6
    Popi_popi_popi = 7
    Popi_popr4 = 8
    Popi_popr8 = 9
    Popref = 10
    Popref_pop1 = 11
    Popref_popi = 12
    Popref_popi_popi = 13
    Popref_popi_popi8 = 14
    Popref_popi_popr4 = 15
    Popref_popi_popr8 = 16
    Popref_popi_popref = 17
    Push0 = 18
    Push1 = 19
    Push1_push1 = 20
    Pushi = 21
    Pushi8 = 22
    Pushr4 = 23
    Pushr8 = 24
    Pushref = 25
    Varpop = 26
    Varpush = 27
    Popref_popi_pop1 = 28


class TypeKind(Enum):
    IsArray = 1
    IsPointer = 2
    IsByRef = 3


# No Delegates

__all__ = [
    AssemblyBuilder,
    AssemblyBuilderData,
    ConstructorBuilder,
    ConstructorOnTypeBuilderInstantiation,
    CustomAttributeBuilder,
    DynamicILGenerator,
    DynamicILInfo,
    DynamicMethod,
    DynamicResolver,
    DynamicScope,
    EnumBuilder,
    EventBuilder,
    FieldBuilder,
    FieldOnTypeBuilderInstantiation,
    GenericFieldInfo,
    GenericMethodInfo,
    GenericTypeParameterBuilder,
    ILGenerator,
    InternalAssemblyBuilder,
    InternalModuleBuilder,
    LineNumberInfo,
    LocalBuilder,
    LocalSymInfo,
    MethodBuilder,
    MethodBuilderInstantiation,
    MethodOnTypeBuilderInstantiation,
    MethodRental,
    ModuleBuilder,
    ModuleBuilderData,
    NativeVersionInfo,
    OpCodes,
    ParameterBuilder,
    PropertyBuilder,
    REDocument,
    ResWriterData,
    ScopeTree,
    SignatureHelper,
    SymbolMethod,
    SymbolType,
    TypeBuilder,
    TypeBuilderInstantiation,
    TypeNameBuilder,
    UnmanagedMarshal,
    VarArgMethod,
    __ExceptionInfo,
    EventToken,
    ExceptionHandler,
    FieldToken,
    Label,
    MethodToken,
    OpCode,
    ParameterToken,
    PropertyToken,
    SignatureToken,
    StringToken,
    TypeToken,
    __FixupData,
    AssemblyBuilderAccess,
    DynamicAssemblyFlags,
    FlowControl,
    OpCodeType,
    OpCodeValues,
    OperandType,
    PEFileKinds,
    PackingSize,
    ScopeAction,
    StackBehaviour,
    TypeKind,
]
