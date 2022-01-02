__all__ = [
    'BinaryOperationBinder',
    'BindingRestrictions',
    'CallInfo',
    'ConvertBinder',
    'CreateInstanceBinder',
    'DeleteIndexBinder',
    'DeleteMemberBinder',
    'DynamicMetaObject',
    'DynamicMetaObjectBinder',
    'DynamicObject',
    'ExpandoObject',
    'GetIndexBinder',
    'GetMemberBinder',
    'InvokeBinder',
    'InvokeMemberBinder',
    'SetIndexBinder',
    'SetMemberBinder',
    'UnaryOperationBinder',
    'IDynamicMetaObjectProvider',
    'IInvokeOnGetBinder',
]


# TODO

# ---------- CLASSES ---------- #

class BinaryOperationBinder:
    """Represents the binary dynamic operation at the call site, providing the binding semantic and the details about the operation."""

class BindingRestrictions:
    """Represents a set of binding restrictions on the DynamicMetaObject under which the dynamic binding is valid."""

class CallInfo:
    """Describes arguments in the dynamic binding process."""

class ConvertBinder:
    """Represents the convert dynamic operation at the call site, providing the binding semantic and the details about the operation."""

class CreateInstanceBinder:
    """Represents the dynamic create operation at the call site, providing the binding semantic and the details about the operation."""

class DeleteIndexBinder:
    """Represents the dynamic delete index operation at the call site, providing the binding semantic and the details about the operation."""

class DeleteMemberBinder:
    """Represents the dynamic delete member operation at the call site, providing the binding semantic and the details about the operation."""

class DynamicMetaObject:
    """Represents the dynamic binding and a binding logic of an object participating in the dynamic binding."""

class DynamicMetaObjectBinder:
    """The dynamic call site binder that participates in the DynamicMetaObject binding protocol."""

class DynamicObject:
    """Provides a base class for specifying dynamic behavior at run time. This class must be inherited from; you cannot instantiate it directly."""

class ExpandoObject:
    """Represents an object whose members can be dynamically added and removed at run time."""

class GetIndexBinder:
    """Represents the dynamic get index operation at the call site, providing the binding semantic and the details about the operation."""

class GetMemberBinder:
    """Represents the dynamic get member operation at the call site, providing the binding semantic and the details about the operation."""

class InvokeBinder:
    """Represents the invoke dynamic operation at the call site, providing the binding semantic and the details about the operation."""

class InvokeMemberBinder:
    """Represents the invoke member dynamic operation at the call site, providing the binding semantic and the details about the operation."""

class SetIndexBinder:
    """Represents the dynamic set index operation at the call site, providing the binding semantic and the details about the operation."""

class SetMemberBinder:
    """Represents the dynamic set member operation at the call site, providing the binding semantic and the details about the operation."""

class UnaryOperationBinder:
    """Represents the unary dynamic operation at the call site, providing the binding semantic and the details about the operation."""


# ---------- INTERFACES ---------- #

class IDynamicMetaObjectProvider:
    """Represents a dynamic object, that can have its operations bound at runtime."""

class IInvokeOnGetBinder:
    """Represents information about a dynamic get member operation that indicates if the get member should invoke properties when they perform the get operation."""
