__all__ = [
    'AmbiguousMatchException',
    'Assembly',
    'AssemblyAlgorithmIdAttribute',
    'AssemblyCompanyAttribute',
    'AssemblyConfigurationAttribute',
    'AssemblyCopyrightAttribute',
    'AssemblyCultureAttribute',
    'AssemblyDefaultAliasAttribute',
    'AssemblyDelaySignAttribute',
    'AssemblyDescriptionAttribute',
    'AssemblyExtensions',
    'AssemblyFileVersionAttribute',
    'AssemblyFlagsAttribute',
    'AssemblyInformationalVersionAttribute',
    'AssemblyKeyFileAttribute',
    'AssemblyKeyNameAttribute',
    'AssemblyMetadataAttribute',
    'AssemblyName',
    'AssemblyNameProxy',
    'AssemblyProductAttribute',
    'AssemblySignatureKeyAttribute',
    'AssemblyTitleAttribute',
    'AssemblyTrademarkAttribute',
    'AssemblyVersionAttribute',
    'Binder',
    'ConstructorInfo',
    'CustomAttributeData',
    'CustomAttributeExtensions',
    'CustomAttributeFormatException',
    'DefaultMemberAttribute',
    'DispatchProxy',
    'EventInfo',
    'EventInfoExtensions',
    'ExceptionHandlingClause',
    'FieldInfo',
    'IntrospectionExtensions',
    'InvalidFilterCriteriaException',
    'LocalVariableInfo',
    'ManifestResourceInfo',
    'MemberInfo',
    'MemberInfoExtensions',
    'MethodBase',
    'MethodBody',
    'MethodInfo',
    'MethodInfoExtensions',
    'Missing',
    'Module',
    'ModuleExtensions',
    'NullabilityInfo',
    'NullabilityInfoContext',
    'ObfuscateAssemblyAttribute',
    'ObfuscationAttribute',
    'ParameterInfo',
    'Pointer',
    'PropertyInfo',
    'PropertyInfoExtensions',
    'ReflectionContext',
    'ReflectionTypeLoadException',
    'RuntimeReflectionExtensions',
    'StrongNameKeyPair',
    'TargetException',
    'TargetInvocationException',
    'TargetParameterCountException',
    'TypeDelegator',
    'TypeExtensions',
    'TypeInfo',
    'CustomAttributeNamedArgument',
    'CustomAttributeTypedArgument',
    'InterfaceMapping',
    'ParameterModifier',
    'ICustomAttributeProvider',
    'ICustomTypeProvider',
    'IReflect',
    'IReflectableType',
    'AssemblyContentType',
    'AssemblyFlags',
    'AssemblyHashAlgorithm',
    'AssemblyNameFlags',
    'BindingFlags',
    'CallingConventions',
    'DeclarativeSecurityAction',
    'EventAttributes',
    'ExceptionHandlingClauseOptions',
    'FieldAttributes',
    'GenericParameterAttributes',
    'ImageFileMachine',
    'ManifestResourceAttributes',
    'MemberTypes',
    'MethodAttributes',
    'MethodImplAttributes',
    'MethodImportAttributes',
    'MethodSemanticsAttributes',
    'NullabilityState',
    'ParameterAttributes',
    'PortableExecutableKinds',
    'ProcessorArchitecture',
    'PropertyAttributes',
    'ResourceAttributes',
    'ResourceLocation',
    'TypeAttributes',
    'MemberFilter',
    'ModuleResolveEventHandler',
    'TypeFilter',
]

from typing import TypeVar

T = TypeVar('T')


# TAttribute = TypeVar('TAttribute', bound=Attribute)

# TODO


# class MemberInfo(Object, ICustomAttributeProvider):
#     """Obtains information about the attributes of a member and provides access to member metadata."""
#
#     def __init__(self):
#         """Initializes a new instance of the MemberInfo class."""
#
#     @property
#     def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
#         """Gets a collection that contains this member's custom attributes."""
#
#     @property
#     def DeclaringType(self) -> Optional[Type]:
#         """Gets the class that declares this member."""
#
#     @property
#     def IsCollectible(self) -> bool:
#         """Gets a value that indicates whether this MemberInfo object is part of an assembly held in a collectible AssemblyLoadContext."""
#
#     @property
#     def MemberType(self) -> MemberTypes:
#         """When overridden in a derived class, gets a MemberTypes value indicating the type of the member - method, constructor, event, and so on."""
#
#     @property
#     def MetadataToken(self) -> int:
#         """Gets a value that identifies a metadata element."""
#
#     @property
#     def Module(self) -> Module:
#         """Gets the module in which the type that declares the member represented by the current MemberInfo is defined."""
#
#     @property
#     def Name(self) -> str:
#         """Gets the name of the current member."""
#
#     @property
#     def ReflectedType(self) -> Optional[Type]:
#         """Gets the class object that was used to obtain this instance of MemberInfo."""
#
#     def GetCustomAttributesData(self) -> IList[CustomAttributeData]:
#         """Returns a list of CustomAttributeData objects representing data about the attributes that have been applied to the target member."""
#
#     def HasSameMetadataDefinitionAs(self, other: MemberInfo) -> bool:
#         """"""
#
#     @staticmethod
#     def Equality(left: MemberInfo, right: MemberInfo) -> bool:
#         """Indicates whether two MemberInfo objects are equal."""
#
#     __eq__ = Equality
#
#     @staticmethod
#     def Inequality(left: MemberInfo, right: MemberInfo) -> bool:
#         """Indicates whether two MemberInfo objects are not equal."""
#
#     __ne__ = Inequality
#
#     @staticmethod
#     @overload
#     def GetCustomAttribute(element: MemberInfo, attributeType: Type) -> Optional[Attribute]:
#         """Retrieves a custom attribute of a specified type that is applied to a specified member."""
#
#     @staticmethod
#     @overload
#     def GetCustomAttribute(element: MemberInfo, attributeType: Type, inherit: bool) -> Optional[Attribute]:
#         """Retrieves a custom attribute of a specified type that is applied to a specified member, and optionally inspects the ancestors of that member."""
#
#     @staticmethod
#     @overload
#     def GetCustomAttribute(element: MemberInfo) -> Optional[TAttribute]:
#         """Retrieves a custom attribute of a specified type that is applied to a specified member."""
#
#     @staticmethod
#     @overload
#     def GetCustomAttribute(element: MemberInfo, inherit: bool) -> Optional[TAttribute]:
#         """Retrieves a custom attribute of a specified type that is applied to a specified member, and optionally inspects the ancestors of that member."""
#
#     @staticmethod
#     @overload
#     def GetCustomAttributes(element: MemberInfo) -> IEnumerable[Attribute]:
#         """Retrieves a collection of custom attributes that are applied to a specified member."""
#
#     @staticmethod
#     @overload
#     def GetCustomAttributes(element: MemberInfo, inherit: bool) -> IEnumerable[Attribute]:
#         """Retrieves a collection of custom attributes that are applied to a specified member, and optionally inspects the ancestors of that member."""
#
#     @staticmethod
#     @overload
#     def GetCustomAttributes(element: MemberInfo, attributeType: Type) -> IEnumerable[Attribute]:
#         """Retrieves a collection of custom attributes of a specified type that are applied to a specified member."""
#
#     @staticmethod
#     @overload
#     def GetCustomAttributes(element: MemberInfo, attributeType: Type, inherit: bool) -> IEnumerable[Attribute]:
#         """Retrieves a collection of custom attributes of a specified type that are applied to a specified member, and optionally inspects the ancestors of that member."""
#
#     @staticmethod
#     @overload
#     def GetCustomAttributes(element: MemberInfo) -> IEnumerable[TAttribute]:
#         """Retrieves a collection of custom attributes of a specified type that are applied to a specified member."""
#
#     @staticmethod
#     @overload
#     def GetCustomAttributes(element: MemberInfo, inherit: bool) -> IEnumerable[TAttribute]:
#         """Retrieves a collection of custom attributes of a specified type that are applied to a specified member, and optionally inspects the ancestors of that member."""
#
#     @staticmethod
#     @overload
#     def IsDefined(element: MemberInfo, attributeType: Type) -> bool:
#         """Indicates whether custom attributes of a specified type are applied to a specified member."""
#
#     @staticmethod
#     @overload
#     def IsDefined(element: MemberInfo, attributeType: Type, inherit: bool) -> bool:
#         """Indicates whether custom attributes of a specified type are applied to a specified member, and, optionally, applied to its ancestors."""
#
#     @staticmethod
#     def GetMetadataToken(member: MemberInfo) -> int:
#         """Gets a metadata token for the given member, if available."""
#
#     @staticmethod
#     def HasMetadataToken(member: MemberInfo) -> bool:
#         """Returns a value that indicates whether a metadata token is available for the specified member.`"""
#
#
# class MethodBase(MemberInfo, ABC):
#     """Provides information about methods and constructors."""
#
#     def __init__(self):
#         """Initializes a new instance of the MethodBase class."""
#
#     @property
#     def Attributes(self) -> MethodAttributes:
#         """Gets the attributes associated with this method."""
#
#     @property
#     def CallingConvention(self) -> CallingConventions:
#         """Gets a value indicating the calling conventions for this method."""
#
#     @property
#     def ContainsGenericParameters(self) -> bool:
#         """Gets a value indicating whether the generic method contains unassigned generic type parameters."""
#
#     @property
#     def IsAbstract(self) -> bool:
#         """Gets a value indicating whether the method is abstract."""
#
#     @property
#     def IsAssembly(self) -> bool:
#         """Gets a value indicating whether the potential visibility of this method or constructor is described by Assembly; that is, the method or constructor is visible at most to other types in the same assembly, and is not visible to derived types outside the assembly."""
#
#     @property
#     def IsConstructedGenericMethod(self) -> bool:
#         """"""
#
#     @property
#     def IsConstructor(self) -> bool:
#         """Gets a value indicating whether the method is a constructor."""
#
#     @property
#     def IsFamily(self) -> bool:
#         """Gets a value indicating whether the visibility of this method or constructor is described by Family; that is, the method or constructor is visible only within its class and derived classes."""
#
#     @property
#     def IsFamilyAndAssembly(self) -> bool:
#         """Gets a value indicating whether the visibility of this method or constructor is described by FamANDAssem; that is, the method or constructor can be called by derived classes, but only if they are in the same assembly."""
#
#     @property
#     def IsFamilyOrAssembly(self) -> bool:
#         """Gets a value indicating whether the potential visibility of this method or constructor is described by FamORAssem; that is, the method or constructor can be called by derived classes wherever they are, and by classes in the same assembly."""
#
#     @property
#     def IsFinal(self) -> bool:
#         """Gets a value indicating whether this method is final."""
#
#     @property
#     def IsGenericMethod(self) -> bool:
#         """Gets a value indicating whether the method is generic."""
#
#     @property
#     def IsGenericMethodDefinition(self) -> bool:
#         """Gets a value indicating whether the method is a generic method definition."""
#
#     @property
#     def IsHideBySig(self) -> bool:
#         """Gets a value indicating whether only a member of the same kind with exactly the same signature is hidden in the derived class."""
#
#     @property
#     def IsPrivate(self) -> bool:
#         """Gets a value indicating whether this member is private."""
#
#     @property
#     def IsPublic(self) -> bool:
#         """Gets a value indicating whether this is a public method."""
#
#     @property
#     def IsSecurityCritical(self) -> bool:
#         """Gets a value that indicates whether the current method or constructor is security-critical or security-safe-critical at the current trust level, and therefore can perform critical operations."""
#
#     @property
#     def IsSecuritySafeCritical(self) -> bool:
#         """Gets a value that indicates whether the current method or constructor is security-safe-critical at the current trust level; that is, whether it can perform critical operations and can be accessed by transparent code."""
#
#     @property
#     def IsSecurityTransparent(self) -> bool:
#         """Gets a value that indicates whether the current method or constructor is transparent at the current trust level, and therefore cannot perform critical operations."""
#
#     @property
#     def IsSpecialName(self) -> bool:
#         """Gets a value indicating whether this method has a special name."""
#
#     @property
#     def IsStatic(self) -> bool:
#         """Gets a value indicating whether the method is static."""
#
#     @property
#     def IsVirtual(self) -> bool:
#         """Gets a value indicating whether the method is virtual."""
#
#     @property
#     def MethodHandle(self) -> RuntimeMethodHandle:
#         """Gets a handle to the internal metadata representation of a method."""
#
#     @property
#     def MethodImplementationFlags(self):
#         """Gets the MethodImplAttributes flags that specify the attributes of a method implementation."""
#
#     # Methods
#     # METHODS
#     # Equals(Object)
#     # Returns a value that indicates whether this instance is equal to a specified object.
#     #
#     # GetCurrentMethod()
#     # Returns a MethodBase object representing the currently executing method.
#
#     # GetGenericArguments()
#     # Returns an array of Type objects that represent the type arguments of a generic method or the type parameters of a generic method definition.
#     #
#     # GetHashCode()
#     # Returns the hash code for this instance.
#     #
#     # GetMethodBody()
#     # When overridden in a derived class, gets a MethodBody object that provides access to the MSIL stream, local variables, and exceptions for the current method.
#     #
#     # GetMethodFromHandle(RuntimeMethodHandle)
#     # Gets method information by using the method's internal metadata representation (handle).
#     #
#     # GetMethodFromHandle(RuntimeMethodHandle, RuntimeTypeHandle)
#     # Gets a MethodBase object for the constructor or method represented by the specified handle, for the specified generic type.
#     #
#     # GetMethodImplementationFlags()
#     # When overridden in a derived class, returns the MethodImplAttributes flags.
#     #
#     # GetParameters()
#     # When overridden in a derived class, gets the parameters of the specified method or constructor.
#
#     # HasSameMetadataDefinitionAs(MemberInfo)	(Inherited from MemberInfo)
#
#     # Invoke(Object, BindingFlags, Binder, Object[], CultureInfo)
#     # When overridden in a derived class, invokes the reflected method or constructor with the given parameters.
#
#     # Invoke(Object, Object[])
#     # Invokes the method or constructor represented by the current instance, using the specified parameters.
#
#     # Operators
#     # OPERATORS
#     # Equality(MethodBase, MethodBase)
#     # Indicates whether two MethodBase objects are equal.
#     #
#     # Inequality(MethodBase, MethodBase)
#     # Indicates whether two MethodBase objects are not equal.
#     #
#     # EXPLICIT INTERFACE IMPLEMENTATIONS
#     # Extension Methods
#     # EXTENSION METHODS
#     # GetCustomAttribute(MemberInfo, Type)
#     # Retrieves a custom attribute of a specified type that is applied to a specified member.
#     #
#     # GetCustomAttribute(MemberInfo, Type, Boolean)
#     # Retrieves a custom attribute of a specified type that is applied to a specified member, and optionally inspects the ancestors of that member.
#     #
#     # GetCustomAttribute[T](MemberInfo)
#     # Retrieves a custom attribute of a specified type that is applied to a specified member.
#     #
#     # GetCustomAttribute[T](MemberInfo, Boolean)
#     # Retrieves a custom attribute of a specified type that is applied to a specified member, and optionally inspects the ancestors of that member.
#     #
#     # GetCustomAttributes(MemberInfo)
#     # Retrieves a collection of custom attributes that are applied to a specified member.
#     #
#     # GetCustomAttributes(MemberInfo, Boolean)
#     # Retrieves a collection of custom attributes that are applied to a specified member, and optionally inspects the ancestors of that member.
#     #
#     # GetCustomAttributes(MemberInfo, Type)
#     # Retrieves a collection of custom attributes of a specified type that are applied to a specified member.
#     #
#     # GetCustomAttributes(MemberInfo, Type, Boolean)
#     # Retrieves a collection of custom attributes of a specified type that are applied to a specified member, and optionally inspects the ancestors of that member.
#     #
#     # GetCustomAttributes[T](MemberInfo)
#     # Retrieves a collection of custom attributes of a specified type that are applied to a specified member.
#     #
#     # GetCustomAttributes[T](MemberInfo, Boolean)
#     # Retrieves a collection of custom attributes of a specified type that are applied to a specified member, and optionally inspects the ancestors of that member.
#     #
#     # IsDefined(MemberInfo, Type)
#     # Indicates whether custom attributes of a specified type are applied to a specified member.
#     #
#     # IsDefined(MemberInfo, Type, Boolean)
#     # Indicates whether custom attributes of a specified type are applied to a specified member, and, optionally, applied to its ancestors.
#     #
#     # GetMetadataToken(MemberInfo)
#     # Gets a metadata token for the given member, if available.
#     #
#     # HasMetadataToken(MemberInfo)
#     # Returns a value that indicates whether a metadata token is available for the specified member.
#
#
# class ICustomAttributeProvider(ABC):
#     """Provides custom attributes for reflection objects that support them."""
#
#     @abstractmethod
#     @overload
#     def GetCustomAttributes(self, inherit: bool) -> Array[Object]:
#         """Returns an array of all the custom attributes defined on this member, excluding named attributes, or an empty array if there are no custom attributes."""
#
#     @abstractmethod
#     @overload
#     def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[Object]:
#         """Returns an array of custom attributes defined on this member, identified by type, or an empty array if there are no custom attributes of that type."""
#
#     @abstractmethod
#     def GetCustomAttributes(self, *args, **kwargs) -> Array[Object]: ...
#
#     @abstractmethod
#     @overload
#     def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
#         """Indicates whether one or more instance of attributeType is defined on this member."""
#
#     @abstractmethod
#     def IsDefined(self, *args, **kwargs) -> bool: ...
#
#
# class IReflect(ABC):
#     """The IReflect interface is used to interoperate with the IDispatch interface.
#     IReflect defines a subset of the Type reflection methods. Implementing this
#     interface enables a type to customize its behavior when the object is being
#     accessed from COM as an IDispatch object. The ExpandoToDispatchExMarshaler
#     class can be used to marshal an object that implements IReflect or IExpando
#     as a COM IDispatch object, and vice versa.
#     """
#
#     @property
#     def UnderlyingSystemType(self) -> Type:
#         """Gets the underlying type that represents the IReflect object."""
#
#     @abstractmethod
#     def GetField(self, name: str, bindingAttr: BindingFlags) -> Optional[FieldInfo]:
#         """Returns the FieldInfo object that corresponds to the specified field and binding flag."""
#
#     @abstractmethod
#     def GetFields(self, bindingAttr: BindingFlags) -> Array[FieldInfo]:
#         """Returns an array of FieldInfo objects that correspond to all fields of the current class."""
#
#     @abstractmethod
#     def GetMember(self, name: str, bindingAttr: BindingFlags) -> Array[MemberInfo]:
#         """Retrieves an array of MemberInfo objects corresponding to all public members or to all members that match a specified name."""
#
#     @abstractmethod
#     def GetMembers(self, bindingAttr: BindingFlags) -> Array[MemberInfo]:
#         """Retrieves an array of MemberInfo objects that correspond either to all public members or to all members of the current class."""
#
#     @abstractmethod
#     @overload
#     def GetMethod(self, name: str, bindingAttr: BindingFlags) -> Optional[MethodInfo]:
#         """Retrieves a MethodInfo object that corresponds to a specified method under specified search constraints."""
#
#     @abstractmethod
#     @overload
#     def GetMethod(self, name: str, bindingAttr: BindingFlags, Binder, types: Array[Type], modifiers: Array[ParameterModifier]) -> Optional[MethodInfo]:
#         """Retrieves a MethodInfo object corresponding to a specified method, using a Type array to choose from among overloaded methods."""
#
#     @abstractmethod
#     def GetMethod(self, *args, **kwargs) -> Optional[MethodInfo]: ...
#
#     @abstractmethod
#     def GetMethods(self, bindingAttr: BindingFlags) -> Array[MemberInfo]:
#         """Retrieves an array of MethodInfo objects with all public methods or all methods of the current class."""
#
#     @abstractmethod
#     @overload
#     def GetProperty(self, name: str, bindingAttr: BindingFlags) -> Optional[PropertyInfo]:
#         """Retrieves a PropertyInfo object corresponding to a specified property under specified search constraints."""
#
#     @abstractmethod
#     @overload
#     def GetProperty(self, name: str, bindingAttr: BindingFlags, binder: Binder, returnType: Type, types: Array[Type], modifiers: Array[ParameterModifier]) -> Optional[PropertyInfo]:
#         """Retrieves a PropertyInfo object that corresponds to a specified property with specified search constraints."""
#
#     @abstractmethod
#     def GetProperty(self, *args, **kwargs) -> Optional[PropertyInfo]: ...
#
#     @abstractmethod
#     def GetProperties(self, bindingAttr: BindingFlags) -> Array[PropertyInfo]:
#         """Retrieves an array of PropertyInfo objects corresponding to all public properties or to all properties of the current class."""
#
#     @abstractmethod
#     def InvokeMember(self, name: str, invokeAttr: BindingFlags, binder: Binder, target: Object, args: Array[Object], modifiers: Array[ParameterModifier], culture: CultureInfo, namedParameters: Array[str]) -> Optional[Object]:
#         """Invokes a specified member."""


# ---------- CLASSES ---------- #

class AmbiguousMatchException:
    """The exception that is thrown when binding to a member results in more than one member matching the binding criteria. This class cannot be inherited."""


class Assembly:
    """Represents an assembly, which is a reusable, versionable, and self-describing building block of a common language runtime application."""


class AssemblyAlgorithmIdAttribute:
    """Specifies an algorithm to hash all files in an assembly. This class cannot be inherited."""


class AssemblyCompanyAttribute:
    """Defines a company name custom attribute for an assembly manifest."""


class AssemblyConfigurationAttribute:
    """Specifies the build configuration, such as retail or debug, for an assembly."""


class AssemblyCopyrightAttribute:
    """Defines a copyright custom attribute for an assembly manifest."""


class AssemblyCultureAttribute:
    """Specifies which culture the assembly supports."""


class AssemblyDefaultAliasAttribute:
    """Defines a friendly default alias for an assembly manifest."""


class AssemblyDelaySignAttribute:
    """Specifies that the assembly is not fully signed when created."""


class AssemblyDescriptionAttribute:
    """Provides a text description for an assembly."""


class AssemblyExtensions:
    """"""


class AssemblyFileVersionAttribute:
    """Instructs a compiler to use a specific version number for the Win32 file version resource. The Win32 file version is not required to be the same as the assembly's version number."""


class AssemblyFlagsAttribute:
    """Specifies a bitwise combination of AssemblyNameFlags flags for an assembly, describing just-in-time (JIT) compiler options, whether the assembly is retargetable, and whether it has a full or tokenized public key. This class cannot be inherited."""


class AssemblyInformationalVersionAttribute:
    """Defines additional version information for an assembly manifest."""


class AssemblyKeyFileAttribute:
    """Specifies the name of a file containing the key pair used to generate a strong name."""


class AssemblyKeyNameAttribute:
    """Specifies the name of a key container within the CSP containing the key pair used to generate a strong name."""


class AssemblyMetadataAttribute:
    """Defines a key/value metadata pair for the decorated assembly."""


class AssemblyName:
    """Describes an assembly's unique identity in full."""


class AssemblyNameProxy:
    """Provides a remotable version of the AssemblyName."""


class AssemblyProductAttribute:
    """Defines a product name custom attribute for an assembly manifest."""


class AssemblySignatureKeyAttribute:
    """Provides migration from an older, simpler strong name key to a larger key with a stronger hashing algorithm."""


class AssemblyTitleAttribute:
    """Specifies a description for an assembly."""


class AssemblyTrademarkAttribute:
    """Defines a trademark custom attribute for an assembly manifest."""


class AssemblyVersionAttribute:
    """Specifies the version of the assembly being attributed."""


class Binder:
    """Selects a member from a list of candidates, and performs type conversion from actual argument type to formal argument type."""


class ConstructorInfo:
    """Discovers the attributes of a class constructor and provides access to constructor metadata."""


class CustomAttributeData:
    """Provides access to custom attribute data for assemblies, modules, types, members and parameters that are loaded into the reflection-only context."""


class CustomAttributeExtensions:
    """Contains static methods for retrieving custom attributes."""


class CustomAttributeFormatException:
    """The exception that is thrown when the binary format of a custom attribute is invalid."""


class DefaultMemberAttribute:
    """Defines the member of a type that is the default member used by InvokeMember(String, BindingFlags, Binder, Object, Object[], ParameterModifier[], CultureInfo, String[])."""


class DispatchProxy:
    """Provides a mechanism for instantiating proxy objects and handling their method dispatch."""


class EventInfo:
    """Discovers the attributes of an event and provides access to event metadata."""


class EventInfoExtensions:
    """"""


class ExceptionHandlingClause:
    """Represents a clause in a structured exception-handling block."""


class FieldInfo:
    """Discovers the attributes of a field and provides access to field metadata."""


class IntrospectionExtensions:
    """Contains methods for converting Type objects."""


class InvalidFilterCriteriaException:
    """The exception that is thrown in FindMembers(MemberTypes, BindingFlags, MemberFilter, Object) when the filter criteria is not valid for the type of filter you are using."""


class LocalVariableInfo:
    """Discovers the attributes of a local variable and provides access to local variable metadata."""


class ManifestResourceInfo:
    """Provides access to manifest resources, which are XML files that describe application dependencies."""


class MemberInfo:
    """Obtains information about the attributes of a member and provides access to member metadata."""


class MemberInfoExtensions:
    """"""


class MethodBase:
    """Provides information about methods and constructors."""


class MethodBody:
    """Provides access to the metadata and MSIL for the body of a method."""


class MethodInfo:
    """Discovers the attributes of a method and provides access to method metadata."""


class MethodInfoExtensions:
    """"""


class Missing:
    """Represents a missing Object. This class cannot be inherited."""


class Module:
    """Performs reflection on a module."""


class ModuleExtensions:
    """"""


class NullabilityInfo:
    """Represents nullability information."""


class NullabilityInfoContext:
    """Provides APIs for populating nullability information and context from reflection members: ParameterInfo, FieldInfo, PropertyInfo, and EventInfo."""


class ObfuscateAssemblyAttribute:
    """Instructs obfuscation tools to use their standard obfuscation rules for the appropriate assembly type."""


class ObfuscationAttribute:
    """Instructs obfuscation tools to take the specified actions for an assembly, type, or member."""


class ParameterInfo:
    """Discovers the attributes of a parameter and provides access to parameter metadata."""


class Pointer:
    """Provides a wrapper class for pointers."""


class PropertyInfo:
    """Discovers the attributes of a property and provides access to property metadata."""


class PropertyInfoExtensions:
    """"""


class ReflectionContext:
    """Represents a context that can provide reflection objects."""


class ReflectionTypeLoadException:
    """The exception that is thrown by the GetTypes() method if any of the classes in a module cannot be loaded. This class cannot be inherited."""


class RuntimeReflectionExtensions:
    """Provides methods that retrieve information about types at run time."""


class StrongNameKeyPair:
    """Encapsulates access to a public or private key pair used to sign strong name assemblies."""


class TargetException:
    """Represents the exception that is thrown when an attempt is made to invoke an invalid target."""


class TargetInvocationException:
    """The exception that is thrown by methods invoked through reflection. This class cannot be inherited."""


class TargetParameterCountException:
    """The exception that is thrown when the number of parameters for an invocation does not match the number expected. This class cannot be inherited."""


class TypeDelegator:
    """Wraps a Type object and delegates methods to that Type."""


class TypeExtensions:
    """"""


class TypeInfo:
    """Represents type declarations for class types, interface types, array types, value types, enumeration types, type parameters, generic type definitions, and open or closed constructed generic types."""


# ---------- STRUCTS ---------- #

class CustomAttributeNamedArgument:
    """Represents a named argument of a custom attribute in the reflection-only context."""


class CustomAttributeTypedArgument:
    """Represents an argument of a custom attribute in the reflection-only context, or an element of an array argument."""


class InterfaceMapping:
    """Retrieves the mapping of an interface into the actual methods on a class that implements that interface."""


class ParameterModifier:
    """Attaches a modifier to parameters so that binding can work with parameter signatures in which the types have been modified."""


# ---------- INTERFACES ---------- #

class ICustomAttributeProvider:
    """Provides custom attributes for reflection objects that support them."""


class ICustomTypeProvider:
    """Represents an object that provides a custom type."""


class IReflect:
    """Interoperates with the IDispatch interface."""


class IReflectableType:
    """Represents a type that you can reflect over."""


# ---------- ENUMS ---------- #

class AssemblyContentType:
    """Provides information about the type of code contained in an assembly."""


class AssemblyFlags:
    """"""


class AssemblyHashAlgorithm:
    """Specifies the hash algorithms used for hashing assembly files and for generating the strong name."""


class AssemblyNameFlags:
    """Provides information about an Assembly reference."""


class BindingFlags:
    """Specifies flags that control binding and the way in which the search for members and types is conducted by reflection."""


class CallingConventions:
    """Defines the valid calling conventions for a method."""


class DeclarativeSecurityAction:
    """Specifies the security actions that can be performed using declarative security."""


class EventAttributes:
    """Specifies the attributes of an event."""


class ExceptionHandlingClauseOptions:
    """Identifies kinds of exception-handling clauses."""


class FieldAttributes:
    """Specifies flags that describe the attributes of a field."""


class GenericParameterAttributes:
    """Describes the constraints on a generic type parameter of a generic type or method."""


class ImageFileMachine:
    """Identifies the platform targeted by an executable."""


class ManifestResourceAttributes:
    """"""


class MemberTypes:
    """Marks each type of member that is defined as a derived class of MemberInfo."""


class MethodAttributes:
    """Specifies flags for method attributes. These flags are defined in the corhdr.h file."""


class MethodImplAttributes:
    """Specifies flags for the attributes of a method implementation."""


class MethodImportAttributes:
    """Specifies flags for the unmanaged method import attributes."""


class MethodSemanticsAttributes:
    """"""


class NullabilityState:
    """Describes nullability states."""


class ParameterAttributes:
    """Defines the attributes that can be associated with a parameter. These are defined in CorHdr.h."""


class PortableExecutableKinds:
    """Identifies the nature of the code in an executable file."""


class ProcessorArchitecture:
    """Identifies the processor and bits-per-word of the platform targeted by an executable."""


class PropertyAttributes:
    """Defines the attributes that can be associated with a property. These attribute values are defined in corhdr.h."""


class ResourceAttributes:
    """Specifies the attributes for a manifest resource."""


class ResourceLocation:
    """Specifies the resource location."""


class TypeAttributes:
    """Specifies type attributes."""


# ---------- DELEGATES #####

class MemberFilter:
    """Represents a delegate that is used to filter a list of members represented in an array of MemberInfo objects."""


class ModuleResolveEventHandler:
    """Represents the method that will handle the ModuleResolve event of an Assembly."""


class TypeFilter:
    """Filters the classes represented in an array of Type objects."""
