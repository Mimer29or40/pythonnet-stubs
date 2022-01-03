__all__ = [
    'AllowReversePInvokeCallsAttribute',
    'AutomationProxyAttribute',
    'BestFitMappingAttribute',
    'BStrWrapper',
    'ClassInterfaceAttribute',
    'CoClassAttribute',
    'CollectionsMarshal',
    'ComAliasNameAttribute',
    'ComAwareEventInfo',
    'ComCompatibleVersionAttribute',
    'ComConversionLossAttribute',
    'ComDefaultInterfaceAttribute',
    'ComEventInterfaceAttribute',
    'ComEventsHelper',
    'COMException',
    'ComImportAttribute',
    'ComRegisterFunctionAttribute',
    'ComSourceInterfacesAttribute',
    'ComUnregisterFunctionAttribute',
    'ComVisibleAttribute',
    'ComWrappers',
    'CriticalHandle',
    'CurrencyWrapper',
    'DefaultCharSetAttribute',
    'DefaultDllImportSearchPathsAttribute',
    'DefaultParameterValueAttribute',
    'DispatchWrapper',
    'DispIdAttribute',
    'DllImportAttribute',
    'DynamicInterfaceCastableImplementationAttribute',
    'ErrorWrapper',
    'ExternalException',
    'FieldOffsetAttribute',
    'GuidAttribute',
    'HandleCollector',
    'ImportedFromTypeLibAttribute',
    'InAttribute',
    'InterfaceTypeAttribute',
    'InvalidComObjectException',
    'InvalidOleVariantTypeException',
    'LCIDConversionAttribute',
    'ManagedToNativeComInteropStubAttribute',
    'Marshal',
    'MarshalAsAttribute',
    'MarshalDirectiveException',
    'MemoryMarshal',
    'NativeLibrary',
    'NativeMemory',
    'OptionalAttribute',
    'OutAttribute',
    'PosixSignalContext',
    'PosixSignalRegistration',
    'PreserveSigAttribute',
    'PrimaryInteropAssemblyAttribute',
    'ProgIdAttribute',
    'RuntimeEnvironment',
    'RuntimeInformation',
    'SafeArrayRankMismatchException',
    'SafeArrayTypeMismatchException',
    'SafeBuffer',
    'SafeHandle',
    'SEHException',
    'SequenceMarshal',
    'StandardOleMarshalObject',
    'StructLayoutAttribute',
    'SuppressGCTransitionAttribute',
    'TypeIdentifierAttribute',
    'TypeLibFuncAttribute',
    'TypeLibImportClassAttribute',
    'TypeLibTypeAttribute',
    'TypeLibVarAttribute',
    'TypeLibVersionAttribute',
    'UnknownWrapper',
    'UnmanagedCallConvAttribute',
    'UnmanagedCallersOnlyAttribute',
    'UnmanagedFunctionPointerAttribute',
    'VariantWrapper',
    'ArrayWithOffset',
    'CLong',
    'ComWrappers',
    'ComWrappers',
    'CULong',
    'GCHandle',
    'HandleRef',
    'NFloat',
    'OSPlatform',
    'ICustomAdapter',
    'ICustomFactory',
    'ICustomMarshaler',
    'ICustomQueryInterface',
    'IDynamicInterfaceCastable',
    'Architecture',
    'CallingConvention',
    'CharSet',
    'ClassInterfaceType',
    'ComInterfaceType',
    'ComMemberType',
    'CreateComInterfaceFlags',
    'CreateObjectFlags',
    'CustomQueryInterfaceMode',
    'CustomQueryInterfaceResult',
    'DllImportSearchPath',
    'GCHandleType',
    'LayoutKind',
    'PosixSignal',
    'TypeLibFuncFlags',
    'TypeLibTypeFlags',
    'TypeLibVarFlags',
    'UnmanagedType',
    'VarEnum',
    'DllImportResolver',
]


# TODO

# ---------- CLASSES ---------- #

class AllowReversePInvokeCallsAttribute:
    """Allows an unmanaged method to call a managed method."""


class AutomationProxyAttribute:
    """Specifies whether the type should be marshaled using the Automation marshaler or a custom proxy and stub."""


class BestFitMappingAttribute:
    """Controls whether Unicode characters are converted to the closest matching ANSI characters."""


class BStrWrapper:
    """Marshals data of type VT_BSTR from managed to unmanaged code. This class cannot be inherited."""


class ClassInterfaceAttribute:
    """Indicates the type of class interface to be generated for a class exposed to COM, if an interface is generated at all."""


class CoClassAttribute:
    """Specifies the class identifier of a coclass imported from a type library."""


class CollectionsMarshal:
    """An unsafe class that provides a set of methods to access the underlying data representations of collections."""


class ComAliasNameAttribute:
    """Indicates the COM alias for a parameter or field type."""


class ComAwareEventInfo:
    """Permits late-bound registration of an event handler."""


class ComCompatibleVersionAttribute:
    """Indicates to a COM client that all classes in the current version of an assembly are compatible with classes in an earlier version of the assembly."""


class ComConversionLossAttribute:
    """Indicates that information was lost about a class or interface when it was imported from a type library to an assembly."""


class ComDefaultInterfaceAttribute:
    """Specifies a default interface to expose to COM. This class cannot be inherited."""


class ComEventInterfaceAttribute:
    """Identifies the source interface and the class that implements the methods of the event interface that is generated when a coclass is imported from a COM type library."""


class ComEventsHelper:
    """Provides methods that enable .NET delegates that handle events to be added and removed from COM objects."""


class COMException:
    """The exception that is thrown when an unrecognized HRESULT is returned from a COM method call."""


class ComImportAttribute:
    """Indicates that the attributed type was previously defined in COM."""


class ComRegisterFunctionAttribute:
    """Specifies the method to call when you register an assembly for use from COM; this enables the execution of user-written code during the registration process."""


class ComSourceInterfacesAttribute:
    """Identifies a list of interfaces that are exposed as COM event sources for the attributed class."""


class ComUnregisterFunctionAttribute:
    """Specifies the method to call when you unregister an assembly for use from COM; this allows for the execution of user-written code during the unregistration process."""


class ComVisibleAttribute:
    """Controls accessibility of an individual managed type or member, or of all types within an assembly, to COM."""


class ComWrappers:
    """Class for managing wrappers of COM IUnknown types."""
    
    # ---------- STRUCTS ---------- #
    
    class ComInterfaceDispatch:
        """An application binary interface for function dispatch of a COM interface."""
    
    class ComInterfaceEntry:
        """Interface type and pointer to targeted VTable."""


class CriticalHandle:
    """Represents a wrapper class for handle resources."""


class CurrencyWrapper:
    """Wraps objects the marshaler should marshal as a VT_CY."""


class DefaultCharSetAttribute:
    """Specifies the value of the CharSet enumeration. This class cannot be inherited."""


class DefaultDllImportSearchPathsAttribute:
    """Specifies the paths that are used to search for DLLs that provide functions for platform invokes."""


class DefaultParameterValueAttribute:
    """Sets the default value of a parameter when called from a language that supports default parameters. This class cannot be inherited."""


class DispatchWrapper:
    """Wraps objects the marshaler should marshal as a VT_DISPATCH."""


class DispIdAttribute:
    """Specifies the COM dispatch identifier (DISPID) of a method, field, or property."""


class DllImportAttribute:
    """Indicates that the attributed method is exposed by an unmanaged dynamic-link library (DLL) as a static entry point."""


class DynamicInterfaceCastableImplementationAttribute:
    """Attribute required by any type that is returned by GetInterfaceImplementation(RuntimeTypeHandle)."""


class ErrorWrapper:
    """Wraps objects the marshaler should marshal as a VT_ERROR."""


class ExternalException:
    """The base exception type for all COM interop exceptions and structured exception handling (SEH) exceptions."""


class FieldOffsetAttribute:
    """Indicates the physical position of fields within the unmanaged representation of a class or structure."""


class GuidAttribute:
    """Supplies an explicit Guid when an automatic GUID is undesirable."""


class HandleCollector:
    """Tracks outstanding handles and forces a garbage collection when the specified threshold is reached."""


class ImportedFromTypeLibAttribute:
    """Indicates that the types defined within an assembly were originally defined in a type library."""


class InAttribute:
    """Indicates that data should be marshaled from the caller to the callee, but not back to the caller."""


class InterfaceTypeAttribute:
    """Indicates whether a managed interface is dual, dispatch-only, or IUnknown -only when exposed to COM."""


class InvalidComObjectException:
    """The exception thrown when an invalid COM object is used."""


class InvalidOleVariantTypeException:
    """The exception thrown by the marshaler when it encounters an argument of a variant type that can not be marshaled to managed code."""


class LCIDConversionAttribute:
    """Indicates that a method's unmanaged signature expects a locale identifier (LCID) parameter."""


class ManagedToNativeComInteropStubAttribute:
    """Provides support for user customization of interop stubs in managed-to-COM interop scenarios."""


class Marshal:
    """Provides a collection of methods for allocating unmanaged memory, copying unmanaged memory blocks, and converting managed to unmanaged types, as well as other miscellaneous methods used when interacting with unmanaged code."""


class MarshalAsAttribute:
    """Indicates how to marshal the data between managed and unmanaged code."""


class MarshalDirectiveException:
    """The exception that is thrown by the marshaler when it encounters a MarshalAsAttribute it does not support."""


class MemoryMarshal:
    """Provides methods to interoperate with Memory<T>, ReadOnlyMemory<T>, Span<T>, and ReadOnlySpan<T>."""


class NativeLibrary:
    """Provides APIs for managing native libraries."""


class NativeMemory:
    """This class contains methods that are mainly used to manage native memory."""


class OptionalAttribute:
    """Indicates that a parameter is optional."""


class OutAttribute:
    """Indicates that data should be marshaled from callee back to caller."""


class PosixSignalContext:
    """Provides data for a PosixSignalRegistration event."""


class PosixSignalRegistration:
    """Handles a PosixSignal."""


class PreserveSigAttribute:
    """Indicates that the HRESULT signature transformation that takes place during COM interop calls should be suppressed."""


class PrimaryInteropAssemblyAttribute:
    """Indicates that the attributed assembly is a primary interop assembly."""


class ProgIdAttribute:
    """Allows the user to specify the ProgID of a class."""


class RuntimeEnvironment:
    """Provides a collection of static methods that return information about the common language runtime environment."""


class RuntimeInformation:
    """Provides information about the .NET runtime installation."""


class SafeArrayRankMismatchException:
    """The exception thrown when the rank of an incoming SAFEARRAY does not match the rank specified in the managed signature."""


class SafeArrayTypeMismatchException:
    """The exception thrown when the type of the incoming SAFEARRAY does not match the type specified in the managed signature."""


class SafeBuffer:
    """Provides a controlled memory buffer that can be used for reading and writing. Attempts to access memory outside the controlled buffer (underruns and overruns) raise exceptions."""


class SafeHandle:
    """Represents a wrapper class for operating system handles. This class must be inherited."""


class SEHException:
    """Represents structured exception handling (SEH) errors."""


class SequenceMarshal:
    """Provides a collection of methods for interoperating with ReadOnlySequence<T>."""


class StandardOleMarshalObject:
    """Replaces the standard common language runtime (CLR) free-threaded marshaler with the standard OLE STA marshaler."""


class StructLayoutAttribute:
    """Lets you control the physical layout of the data fields of a class or structure in memory."""


class SuppressGCTransitionAttribute:
    """Indicates that a garbage collection transition should be skipped when an unmanaged function call is made."""


class TypeIdentifierAttribute:
    """Provides support for type equivalence."""


class TypeLibFuncAttribute:
    """Contains the FUNCFLAGS that were originally imported for this method from the COM type library."""


class TypeLibImportClassAttribute:
    """Specifies which Type exclusively uses an interface. This class cannot be inherited."""


class TypeLibTypeAttribute:
    """Contains the TYPEFLAGS that were originally imported for this type from the COM type library."""


class TypeLibVarAttribute:
    """Contains the VARFLAGS that were originally imported for this field from the COM type library."""


class TypeLibVersionAttribute:
    """Specifies the version number of an exported type library."""


class UnknownWrapper:
    """Wraps objects the marshaler should marshal as a VT_UNKNOWN."""


class UnmanagedCallConvAttribute:
    """Provides an equivalent to UnmanagedCallersOnlyAttribute for native functions declared in .NET."""


class UnmanagedCallersOnlyAttribute:
    """Any method marked with UnmanagedCallersOnlyAttribute can be directly called from native code. The function token can be loaded to a local variable using the address-of operator in C# and passed as a callback to a native method."""


class UnmanagedFunctionPointerAttribute:
    """Controls the marshaling behavior of a delegate signature passed as an unmanaged function pointer to or from unmanaged code. This class cannot be inherited."""


class VariantWrapper:
    """Marshals data of type VT_VARIANT | VT_BYREF from managed to unmanaged code. This class cannot be inherited."""


# ---------- STRUCTS ---------- #

class ArrayWithOffset:
    """Encapsulates an array and an offset within the specified array."""


class CLong:
    """CLong is an immutable value type that represents the long type in C and C++. It is meant to be used as an exchange type at the managed/unmanaged boundary to accurately represent in managed code unmanaged APIs that use the long type. This type has 32-bits of storage on all Windows platforms and 32-bit Unix-based platforms. It has 64-bits of storage on 64-bit Unix platforms."""


class CULong:
    """CULong is an immutable value type that represents the unsigned long type in C and C++. It is meant to be used as an exchange type at the managed/unmanaged boundary to accurately represent in managed code unmanaged APIs that use the unsigned long type. This type has 32-bits of storage on all Windows platforms and 32-bit Unix-based platforms. It has 64-bits of storage on 64-bit Unix platforms."""


class GCHandle:
    """Provides a way to access a managed object from unmanaged memory."""


class HandleRef:
    """Wraps a managed object holding a handle to a resource that is passed to unmanaged code using platform invoke."""


class NFloat:
    """NFloat is an immutable value type that represents a floating type that has the same size as the native integer size. It is meant to be used as an exchange type at the managed/unmanaged boundary to accurately represent in managed code unmanaged APIs that use a type alias for C or C++'s float on 32-bit platforms or double on 64-bit platforms, such as the CGFloat type in libraries provided by Apple."""


class OSPlatform:
    """Represents an operating system platform."""


# ---------- INTERFACES ---------- #

class ICustomAdapter:
    """Provides a way for clients to access the actual object, rather than the adapter object handed out by a custom marshaler."""


class ICustomFactory:
    """Enables users to write activation code for managed objects that extend MarshalByRefObject."""


class ICustomMarshaler:
    """Provides custom wrappers for handling method calls."""


class ICustomQueryInterface:
    """Enables developers to provide a custom, managed implementation of the IUnknown::QueryInterface(REFIID riid, void **ppvObject) method."""


class IDynamicInterfaceCastable:
    """Interface used to participate in a type cast failure."""


# ---------- ENUMS ---------- #

class Architecture:
    """Indicates the processor architecture."""


class CallingConvention:
    """Specifies the calling convention required to call methods implemented in unmanaged code."""


class CharSet:
    """Dictates which character set marshaled strings should use."""


class ClassInterfaceType:
    """Identifies the type of class interface that is generated for a class."""


class ComInterfaceType:
    """Identifies how to expose an interface to COM."""


class ComMemberType:
    """Describes the type of a COM member."""


class CreateComInterfaceFlags:
    """Specifies flags for the GetOrCreateComInterfaceForObject(Object, CreateComInterfaceFlags) method."""


class CreateObjectFlags:
    """Specifies flags for the GetOrCreateObjectForComInstance(IntPtr, CreateObjectFlags) method."""


class CustomQueryInterfaceMode:
    """Indicates whether the GetComInterfaceForObject(Object, Type, CustomQueryInterfaceMode) method's IUnknown::QueryInterface calls can use the ICustomQueryInterface interface."""


class CustomQueryInterfaceResult:
    """Provides return values for the GetInterface(Guid, IntPtr) method."""


class DllImportSearchPath:
    """Specifies the paths that are used to search for DLLs that provide functions for platform invokes."""


class GCHandleType:
    """Represents the types of handles the GCHandle class can allocate."""


class LayoutKind:
    """Controls the layout of an object when exported to unmanaged code."""


class PosixSignal:
    """Specifies a POSIX signal number."""


class TypeLibFuncFlags:
    """Describes the original settings of the FUNCFLAGS in the COM type library from where this method was imported."""


class TypeLibTypeFlags:
    """Describes the original settings of the TYPEFLAGS in the COM type library from which the type was imported."""


class TypeLibVarFlags:
    """Describes the original settings of the VARFLAGS in the COM type library from which the variable was imported."""


class UnmanagedType:
    """Identifies how to marshal parameters or fields to unmanaged code."""


class VarEnum:
    """Indicates how to marshal the array elements when an array is marshaled from managed to unmanaged code as a SafeArray."""


# ---------- DELEGATES ---------- #

class DllImportResolver:
    """Provides a delegate used to resolve native libraries via callback."""
