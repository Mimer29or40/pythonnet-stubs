__all__ = [
    'AccessedThroughPropertyAttribute',
    'AsyncIteratorStateMachineAttribute',
    'AsyncMethodBuilderAttribute',
    'AsyncStateMachineAttribute',
    'CallConvCdecl',
    'CallConvFastcall',
    'CallConvMemberFunction',
    'CallConvStdcall',
    'CallConvSuppressGCTransition',
    'CallConvThiscall',
    'CallerArgumentExpressionAttribute',
    'CallerFilePathAttribute',
    'CallerLineNumberAttribute',
    'CallerMemberNameAttribute',
    'CallSite',
    'CallSite',
    'CallSiteBinder',
    'CallSiteHelpers',
    'CompilationRelaxationsAttribute',
    'CompilerGeneratedAttribute',
    'CompilerGlobalScopeAttribute',
    'CompilerMarshalOverride',
    'ConditionalWeakTable',
    'ContractHelper',
    'CppInlineNamespaceAttribute',
    'CreateNewOnMetadataUpdateAttribute',
    'CustomConstantAttribute',
    'DateTimeConstantAttribute',
    'DebugInfoGenerator',
    'DecimalConstantAttribute',
    'DefaultDependencyAttribute',
    'DependencyAttribute',
    'DisablePrivateReflectionAttribute',
    'DiscardableAttribute',
    'DynamicAttribute',
    'EnumeratorCancellationAttribute',
    'ExtensionAttribute',
    'FixedAddressValueTypeAttribute',
    'FixedBufferAttribute',
    'FormattableStringFactory',
    'HasCopySemanticsAttribute',
    'IDispatchConstantAttribute',
    'IndexerNameAttribute',
    'InternalsVisibleToAttribute',
    'InterpolatedStringHandlerArgumentAttribute',
    'InterpolatedStringHandlerAttribute',
    'IsBoxed',
    'IsByRefLikeAttribute',
    'IsByValue',
    'IsConst',
    'IsCopyConstructed',
    'IsExplicitlyDereferenced',
    'IsExternalInit',
    'IsImplicitlyDereferenced',
    'IsJitIntrinsic',
    'IsLong',
    'IsPinned',
    'IsReadOnlyAttribute',
    'IsSignUnspecifiedByte',
    'IsUdtReturn',
    'IsVolatile',
    'IteratorStateMachineAttribute',
    'IUnknownConstantAttribute',
    'MethodImplAttribute',
    'ModuleInitializerAttribute',
    'NativeCppClassAttribute',
    'PreserveBaseOverridesAttribute',
    'ReadOnlyCollectionBuilder',
    'ReferenceAssemblyAttribute',
    'RequiredAttributeAttribute',
    'RuleCache',
    'RuntimeCompatibilityAttribute',
    'RuntimeFeature',
    'RuntimeHelpers',
    'RuntimeWrappedException',
    'ScopelessEnumAttribute',
    'SkipLocalsInitAttribute',
    'SpecialNameAttribute',
    'StateMachineAttribute',
    'StringFreezingAttribute',
    'StrongBox',
    'SuppressIldasmAttribute',
    'SwitchExpressionException',
    'TupleElementNamesAttribute',
    'TypeForwardedFromAttribute',
    'TypeForwardedToAttribute',
    'Unsafe',
    'UnsafeValueTypeAttribute',
    'AsyncIteratorMethodBuilder',
    'AsyncTaskMethodBuilder',
    'AsyncTaskMethodBuilder',
    'AsyncValueTaskMethodBuilder',
    'AsyncValueTaskMethodBuilder',
    'AsyncVoidMethodBuilder',
    'ConfiguredAsyncDisposable',
    'ConfiguredCancelableAsyncEnumerable',
    'ConfiguredCancelableAsyncEnumerable',
    'ConfiguredTaskAwaitable',
    'ConfiguredTaskAwaitable',
    'ConfiguredTaskAwaitable',
    'ConfiguredTaskAwaitable',
    'ConfiguredValueTaskAwaitable',
    'ConfiguredValueTaskAwaitable',
    'ConfiguredValueTaskAwaitable',
    'ConfiguredValueTaskAwaitable',
    'DefaultInterpolatedStringHandler',
    'PoolingAsyncValueTaskMethodBuilder',
    'PoolingAsyncValueTaskMethodBuilder',
    'TaskAwaiter',
    'TaskAwaiter',
    'ValueTaskAwaiter',
    'ValueTaskAwaiter',
    'YieldAwaitable',
    'YieldAwaitable',
    'IAsyncStateMachine',
    'ICriticalNotifyCompletion',
    'INotifyCompletion',
    'IRuntimeVariables',
    'IStrongBox',
    'ITuple',
    'CompilationRelaxations',
    'LoadHint',
    'MethodCodeType',
    'MethodImplOptions',
    'ConditionalWeakTable',
    'RuntimeHelpers',
    'RuntimeHelpers',
]

from typing import TypeVar, Generic, Protocol

from .. import IntType, ObjectType
from ..util import Item

T = TypeVar('T')
TKey = TypeVar('TKey')
TValue = TypeVar('TValue')
TResult = TypeVar('TResult')


# TODO

# ---------- CLASSES ---------- #

class AccessedThroughPropertyAttribute:
    """Specifies the name of the property that accesses the attributed field."""


class AsyncIteratorStateMachineAttribute:
    """Indicates whether a method is an asynchronous iterator."""


class AsyncMethodBuilderAttribute:
    """Indicates the type of the async method builder that should be used by a language compiler to build the attributed type when used as the return type of an async method."""


class AsyncStateMachineAttribute:
    """Indicates whether a method is marked with either the Async or async modifier."""


class CallConvCdecl:
    """Indicates that a method should use the Cdecl calling convention."""


class CallConvFastcall:
    """This calling convention is not supported in this version of .NET."""


class CallConvMemberFunction:
    """Indicates that the calling convention used is the member function variant."""


class CallConvStdcall:
    """Indicates that a method should use the StdCall calling convention."""


class CallConvSuppressGCTransition:
    """Indicates that a method should suppress the GC transition as part of the calling convention."""


class CallConvThiscall:
    """Indicates that a method should use the ThisCall calling convention."""


class CallerArgumentExpressionAttribute:
    """Indicates that a parameter captures the expression passed for another parameter as a string."""


class CallerFilePathAttribute:
    """Allows you to obtain the full path of the source file that contains the caller. This is the file path at the time of compile."""


class CallerLineNumberAttribute:
    """Allows you to obtain the line number in the source file at which the method is called."""


class CallerMemberNameAttribute:
    """Allows you to obtain the method or property name of the caller to the method."""


class CallSite:
    """A dynamic call site base class. This type is used as a parameter type to the dynamic site targets."""


class CallSite(Generic[T]):
    """Dynamic site type."""


class CallSiteBinder:
    """Class responsible for runtime binding of the dynamic operations on the dynamic call site."""


class CallSiteHelpers:
    """Class that contains helper methods for DLR CallSites."""


class CompilationRelaxationsAttribute:
    """Controls the strictness of the code generated by the common language runtime's just-in-time (JIT) compiler."""


class CompilerGeneratedAttribute:
    """Distinguishes a compiler-generated element from a user-generated element. This class cannot be inherited."""


class CompilerGlobalScopeAttribute:
    """Indicates that a class should be treated as if it has global scope."""


class CompilerMarshalOverride:
    """Indicates that the modified instance of a variable differs from its true type when marshaling. This class cannot be inherited."""


class ConditionalWeakTable(Generic[TKey, TValue]):
    """Enables compilers to dynamically attach object fields to managed objects."""
    
    # ---------- DELEGATES ---------- #
    
    class CreateValueCallback:
        """Represents a method that creates a non-default value to add as part of a key/value pair to a ConditionalWeakTable<TKey,TValue> object."""


class ContractHelper:
    """Provides methods that the binary rewriter uses to handle contract failures."""


class CppInlineNamespaceAttribute:
    """Defines the inline namespace in C++/CLI."""


class CreateNewOnMetadataUpdateAttribute:
    """Indicates a type should be replaced rather than updated when applying metadata updates."""


class CustomConstantAttribute:
    """Defines a constant value that a compiler can persist for a field or method parameter."""


class DateTimeConstantAttribute:
    """Persists an 8-byte DateTime constant for a field or parameter."""


class DebugInfoGenerator:
    """Generates debug information for lambda expressions in an expression tree."""


class DecimalConstantAttribute:
    """Stores the value of a Decimal constant in metadata. This class cannot be inherited."""


class DefaultDependencyAttribute:
    """Provides a hint to the common language runtime (CLR) indicating how likely a dependency is to be loaded. This class is used in a dependent assembly to indicate what hint should be used when the parent does not specify the DependencyAttribute attribute. This class cannot be inherited."""


class DependencyAttribute:
    """Indicates when a dependency is to be loaded by the referring assembly. This class cannot be inherited."""


class DisablePrivateReflectionAttribute:
    """Indicates that any private members contained in an assembly's types are not available to reflection."""


class DiscardableAttribute:
    """Marks a type definition as discardable."""


class DynamicAttribute:
    """Indicates that the use of Object on a member is meant to be treated as a dynamically dispatched type."""


class EnumeratorCancellationAttribute:
    """Allows users of async-enumerable methods to mark the parameter that should receive the cancellation token value from GetAsyncEnumerator(CancellationToken)."""


class ExtensionAttribute:
    """Indicates that a method is an extension method, or that a class or assembly contains extension methods."""


class FixedAddressValueTypeAttribute:
    """Fixes the address of a static value type field throughout its lifetime. This class cannot be inherited."""


class FixedBufferAttribute:
    """Indicates that a field should be treated as containing a fixed number of elements of the specified primitive type. This class cannot be inherited."""


class FormattableStringFactory:
    """Provides a static method to create a FormattableString object from a composite format string and its arguments."""


class HasCopySemanticsAttribute:
    """This class is obsolete. This class cannot be inherited."""


class IDispatchConstantAttribute:
    """Indicates that the default value for the attributed field or parameter is an instance of DispatchWrapper, where the WrappedObject is null."""


class IndexerNameAttribute:
    """Indicates the name by which an indexer is known in programming languages that do not support indexers directly."""


class InternalsVisibleToAttribute:
    """Specifies that types that are ordinarily visible only within the current assembly are visible to a specified assembly."""


class InterpolatedStringHandlerArgumentAttribute:
    """Indicates which arguments to a method involving an interpolated string handler should be passed to that handler."""


class InterpolatedStringHandlerAttribute:
    """Indicates the attributed type is to be used as an interpolated string handler."""


class IsBoxed:
    """Indicates that the modified reference type is a boxed value type. This class cannot be inherited."""


class IsByRefLikeAttribute:
    """Indicates that a structure is byref-like."""


class IsByValue:
    """Indicates that a modified method argument should be interpreted as having object passed-by-value semantics. This modifier is applied to reference types. This class cannot be inherited."""


class IsConst:
    """Indicates that the modified type has a const modifier. This class cannot be inherited."""


class IsCopyConstructed:
    """Indicates that any copying of values of this type must use the copy constructor provided by the type. This class cannot be inherited."""


class IsExplicitlyDereferenced:
    """Indicates that a managed pointer represents a pointer parameter within a method signature. This class cannot be inherited."""


class IsExternalInit:
    """Reserved to be used by the compiler for tracking metadata. This class should not be used by developers in source code."""


class IsImplicitlyDereferenced:
    """Indicates that the modified garbage collection reference represents a reference parameter within a method signature. This class cannot be inherited."""


class IsJitIntrinsic:
    """Indicates that a modified method is an intrinsic value for which the just-in-time (JIT) compiler can perform special code generation. This class cannot be inherited."""


class IsLong:
    """Indicates that a modified integer is a standard C++ long value. This class cannot be inherited."""


class IsPinned:
    """Indicates that a modified instance is pinned in memory. This class cannot be inherited."""


class IsReadOnlyAttribute:
    """Marks a program element as read-only."""


class IsSignUnspecifiedByte:
    """Indicates that a modifier is neither signed nor unsigned. This class cannot be inherited."""


class IsUdtReturn:
    """Indicates that a return type is a user-defined type. This class cannot be inherited."""


class IsVolatile:
    """Marks a field as volatile. This class cannot be inherited."""


class IteratorStateMachineAttribute:
    """Indicates whether a method in Visual Basic is marked with the Iterator modifier."""


class IUnknownConstantAttribute:
    """Indicates that the default value for the attributed field or parameter is an instance of UnknownWrapper, where the WrappedObject is null. This class cannot be inherited."""


class MethodImplAttribute:
    """Specifies the details of how a method is implemented. This class cannot be inherited."""


class ModuleInitializerAttribute:
    """Used to indicate to the compiler that a method should be called in its containing module's initializer."""


class NativeCppClassAttribute:
    """Applies metadata to an assembly that indicates that a type is an unmanaged type. This class cannot be inherited."""


class PreserveBaseOverridesAttribute:
    """Ensures that any virtual call to the method, whether it uses the base signature or derived signature of the method, executes the most derived override."""


class ReadOnlyCollectionBuilder(Generic[T]):
    """The builder for read only collection."""


class ReferenceAssemblyAttribute:
    """Identifies an assembly as a reference assembly, which contains metadata but no executable code."""


class RequiredAttributeAttribute:
    """Specifies that an importing compiler must fully understand the semantics of a type definition, or refuse to use it. This class cannot be inherited."""


class RuleCache(Generic[T]):
    """Represents a cache of runtime binding rules."""


class RuntimeCompatibilityAttribute:
    """Specifies whether to wrap exceptions that do not derive from the Exception class with a RuntimeWrappedException object. This class cannot be inherited."""


class RuntimeFeature:
    """Defines APIs to determine whether specific features are supported by the common language runtime."""


class RuntimeHelpers:
    """Provides a set of static methods and properties that provide support for compilers. This class cannot be inherited."""
    
    # ---------- DELEGATES ---------- #
    
    class CleanupCode:
        """Represents a method to run when an exception occurs."""
    
    class TryCode:
        """Represents a delegate to code that should be run in a try block."""


class RuntimeWrappedException:
    """Wraps an exception that does not derive from the Exception class. This class cannot be inherited."""


class ScopelessEnumAttribute:
    """Indicates that a native enumeration is not qualified by the enumeration type name. This class cannot be inherited."""


class SkipLocalsInitAttribute:
    """Indicates to the compiler that the .locals init flag should not be set in nested method headers when emitting to metadata."""


class SpecialNameAttribute:
    """Indicates that a type or member is treated in a special way by the runtime or tools. This class cannot be inherited."""


class StateMachineAttribute:
    """Allows you to determine whether a method is a state machine method."""


class StringFreezingAttribute:
    """Deprecated. Freezes a string literal when creating native images using the Ngen.exe (Native Image Generator). This class cannot be inherited."""


class StrongBox(Generic[T]):
    """Holds a reference to a value."""


class SuppressIldasmAttribute:
    """Prevents the Ildasm.exe (IL Disassembler) from disassembling an assembly. This class cannot be inherited."""


class SwitchExpressionException:
    """Indicates that a switch expression that was non-exhaustive failed to match its input at runtime. The exception optionally contains an object representing the unmatched value."""


class TupleElementNamesAttribute:
    """Indicates that the use of a value tuple on a member is meant to be treated as a tuple with element names."""


class TypeForwardedFromAttribute:
    """Specifies a source Type in another assembly."""


class TypeForwardedToAttribute:
    """Specifies a destination Type in another assembly."""


class Unsafe:
    """Contains generic, low-level functionality for manipulating pointers."""


class UnsafeValueTypeAttribute:
    """Specifies that a type contains an unmanaged array that might potentially overflow. This class cannot be inherited."""


# ---------- STRUCTS ---------- #

class AsyncIteratorMethodBuilder:
    """Represents a builder for asynchronous iterators."""


class AsyncTaskMethodBuilder:
    """Represents a builder for asynchronous methods that return a task."""


class AsyncTaskMethodBuilder(Generic[TResult]):
    """Represents a builder for asynchronous methods that returns a task and provides a parameter for the result."""


class AsyncValueTaskMethodBuilder:
    """Represents a builder for asynchronous methods that return a ValueTask."""


class AsyncValueTaskMethodBuilder(Generic[TResult]):
    """Represents a builder for asynchronous methods that returns a ValueTask<TResult>."""


class AsyncVoidMethodBuilder:
    """Represents a builder for asynchronous methods that do not return a value."""


class ConfiguredAsyncDisposable:
    """Provides a type that can be used to configure how awaits on an IAsyncDisposable are performed."""


class ConfiguredCancelableAsyncEnumerable(Generic[T]):
    """Provides an awaitable async enumerable that enables cancelable iteration and configured awaits."""
    
    class Enumerator:
        """Provides an awaitable async enumerator that enables cancelable iteration and configured awaits."""


class ConfiguredTaskAwaitable:
    """Provides an awaitable object that enables configured awaits on a task."""
    
    class ConfiguredTaskAwaiter:
        """Provides an awaiter for an awaitable (ConfiguredTaskAwaitable) object."""


class ConfiguredTaskAwaitable(Generic[TResult]):
    """Provides an awaitable object that enables configured awaits on a task."""
    
    class ConfiguredTaskAwaiter:
        """Provides an awaiter for an awaitable object(ConfiguredTaskAwaitable<TResult>)."""


class ConfiguredValueTaskAwaitable:
    """Provides an awaitable type that enables configured awaits on a ValueTask."""
    
    class ConfiguredValueTaskAwaiter:
        """Provides an awaiter for a ConfiguredValueTaskAwaitable."""


class ConfiguredValueTaskAwaitable(Generic[TResult]):
    """Provides an awaitable type that enables configured awaits on a ValueTask<TResult>."""
    
    class ConfiguredValueTaskAwaiter:
        """Provides an awaiter for a ConfiguredValueTaskAwaitable<TResult>."""


class DefaultInterpolatedStringHandler:
    """Provides a handler used by the language compiler to process interpolated strings into String instances."""


class PoolingAsyncValueTaskMethodBuilder:
    """Represents a builder for asynchronous methods that return a ValueTask."""


class PoolingAsyncValueTaskMethodBuilder(Generic[TResult]):
    """Represents a builder for asynchronous methods that returns a ValueTask<TResult>."""


class TaskAwaiter:
    """Provides an object that waits for the completion of an asynchronous task."""


class TaskAwaiter(Generic[TResult]):
    """Represents an object that waits for the completion of an asynchronous task and provides a parameter for the result."""


class ValueTaskAwaiter:
    """Provides an awaiter for a ValueTask."""


class ValueTaskAwaiter(Generic[TResult]):
    """Provides an awaiter for a ValueTask<TResult>."""


class YieldAwaitable:
    """Provides the context for waiting when asynchronously switching into a target environment."""
    
    class YieldAwaiter:
        """Provides an awaiter for switching into a target environment."""


# ---------- INTERFACES ---------- #

class IAsyncStateMachine:
    """Represents state machines that are generated for asynchronous methods. This type is intended for compiler use only."""


class ICriticalNotifyCompletion:
    """Represents an awaiter that schedules continuations when an await operation completes."""


class INotifyCompletion:
    """Represents an operation that schedules continuations when it completes."""


class IRuntimeVariables:
    """Represents the values of run-time variables."""


class IStrongBox:
    """Defines a property for accessing the value that an object references."""


class ITuple(Protocol):
    """Defines a general-purpose Tuple implementation that allows access to
    Tuple instance members without knowing the underlying Tuple type."""
    
    @property
    def Item(self) -> Item[IntType, ObjectType]:
        """Returns the value of the specified Tuple element."""
    
    def __getitem__(self, key: IntType) -> ObjectType: ...

    def __setitem__(self, key: IntType, value: ObjectType) -> None: ...
    
    @property
    def Length(self) -> IntType:
        """Gets the number of elements in this Tuple instance."""


# ---------- ENUMS ---------- #

class CompilationRelaxations:
    """Specifies parameters that control the strictness of the code generated by the common language runtime's just-in-time (JIT) compiler."""


class LoadHint:
    """Specifies the preferred default binding for a dependent assembly."""


class MethodCodeType:
    """Defines how a method is implemented."""


class MethodImplOptions:
    """Specifies constants that define the details of how a method is implemented."""
