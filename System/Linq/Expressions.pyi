__all__ = [
    'BinaryExpression',
    'BlockExpression',
    'CatchBlock',
    'ConditionalExpression',
    'ConstantExpression',
    'DebugInfoExpression',
    'DefaultExpression',
    'DynamicExpression',
    'DynamicExpressionVisitor',
    'ElementInit',
    'Expression',
    'Expression',
    'ExpressionVisitor',
    'GotoExpression',
    'IndexExpression',
    'InvocationExpression',
    'LabelExpression',
    'LabelTarget',
    'LambdaExpression',
    'ListInitExpression',
    'LoopExpression',
    'MemberAssignment',
    'MemberBinding',
    'MemberExpression',
    'MemberInitExpression',
    'MemberListBinding',
    'MemberMemberBinding',
    'MethodCallExpression',
    'NewArrayExpression',
    'NewExpression',
    'ParameterExpression',
    'RuntimeVariablesExpression',
    'SwitchCase',
    'SwitchExpression',
    'SymbolDocumentInfo',
    'TryExpression',
    'TypeBinaryExpression',
    'UnaryExpression',
    'IArgumentProvider',
    'IDynamicExpression',
    'ExpressionType',
    'GotoExpressionKind',
    'MemberBindingType',
]

from typing import TypeVar, Generic

TDelegate = TypeVar('TDelegate')


# TODO

# ---------- CLASSES ---------- #

class BinaryExpression:
    """Represents an expression that has a binary operator."""


class BlockExpression:
    """Represents a block that contains a sequence of expressions where variables can be defined."""


class CatchBlock:
    """Represents a catch statement in a try block."""


class ConditionalExpression:
    """Represents an expression that has a conditional operator."""


class ConstantExpression:
    """Represents an expression that has a constant value."""


class DebugInfoExpression:
    """Emits or clears a sequence point for debug information. This allows the debugger to highlight the correct source code when debugging."""


class DefaultExpression:
    """Represents the default value of a type or an empty expression."""


class DynamicExpression:
    """Represents a dynamic operation."""


class DynamicExpressionVisitor:
    """Represents a visitor or rewriter for dynamic expression trees."""


class ElementInit:
    """Represents an initializer for a single element of an IEnumerable collection."""


class Expression:
    """Provides the base class from which the classes that represent expression tree nodes are derived. It also contains static (Shared in Visual Basic) factory methods to create the various node types. This is an abstract class."""


class Expression(Generic[TDelegate]):
    """Represents a strongly typed lambda expression as a data structure in the form of an expression tree. This class cannot be inherited."""


class ExpressionVisitor:
    """Represents a visitor or rewriter for expression trees."""


class GotoExpression:
    """Represents an unconditional jump. This includes return statements, break and continue statements, and other jumps."""


class IndexExpression:
    """Represents indexing a property or array."""


class InvocationExpression:
    """Represents an expression that applies a delegate or lambda expression to a list of argument expressions."""


class LabelExpression:
    """Represents a label, which can be put in any Expression context. If it is jumped to, it will get the value provided by the corresponding GotoExpression. Otherwise, it receives the value in DefaultValue. If the Type equals System.Void, no value should be provided."""


class LabelTarget:
    """Used to represent the target of a GotoExpression."""


class LambdaExpression:
    """Describes a lambda expression. This captures a block of code that is similar to a .NET method body."""


class ListInitExpression:
    """Represents a constructor call that has a collection initializer."""


class LoopExpression:
    """Represents an infinite loop. It can be exited with "break"."""


class MemberAssignment:
    """Represents assignment operation for a field or property of an object."""


class MemberBinding:
    """Provides the base class from which the classes that represent bindings that are used to initialize members of a newly created object derive."""


class MemberExpression:
    """Represents accessing a field or property."""


class MemberInitExpression:
    """Represents calling a constructor and initializing one or more members of the new object."""


class MemberListBinding:
    """Represents initializing the elements of a collection member of a newly created object."""


class MemberMemberBinding:
    """Represents initializing members of a member of a newly created object."""


class MethodCallExpression:
    """Represents a call to either static or an instance method."""


class NewArrayExpression:
    """Represents creating a new array and possibly initializing the elements of the new array."""


class NewExpression:
    """Represents a constructor call."""


class ParameterExpression:
    """Represents a named parameter expression."""


class RuntimeVariablesExpression:
    """An expression that provides runtime read/write permission for variables."""


class SwitchCase:
    """Represents one case of a SwitchExpression."""


class SwitchExpression:
    """Represents a control expression that handles multiple selections by passing control to SwitchCase."""


class SymbolDocumentInfo:
    """Stores information necessary to emit debugging symbol information for a source file, in particular the file name and unique language identifier."""


class TryExpression:
    """Represents a try/catch/finally/fault block."""


class TypeBinaryExpression:
    """Represents an operation between an expression and a type."""


class UnaryExpression:
    """Represents an expression that has a unary operator."""


# ---------- INTERFACES ---------- #

class IArgumentProvider:
    """Provides an internal interface for accessing the arguments of multiple tree nodes (DynamicExpression, ElementInit, MethodCallExpression, InvocationExpression, NewExpression, and IndexExpression). This API is for internal use only."""


class IDynamicExpression:
    """Provides an internal interface for accessing the arguments of DynamicExpression tree nodes as well as CallSite and Rewriting functionality. You should not use this API. It is only public due to DLL refactoring and exists only for internal performance optimizations."""


# ---------- ENUMS ---------- #

class ExpressionType:
    """Describes the node types for the nodes of an expression tree."""


class GotoExpressionKind:
    """Specifies what kind of jump this GotoExpression represents."""


class MemberBindingType:
    """Describes the binding types that are used in MemberInitExpression objects."""
