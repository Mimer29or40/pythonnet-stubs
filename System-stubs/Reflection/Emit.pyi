__all__ = [
    'AssemblyBuilder',
    'ConstructorBuilder',
    'CustomAttributeBuilder',
    'DynamicILInfo',
    'DynamicMethod',
    'EnumBuilder',
    'EventBuilder',
    'FieldBuilder',
    'GenericTypeParameterBuilder',
    'ILGenerator',
    'LocalBuilder',
    'MethodBuilder',
    'ModuleBuilder',
    'OpCodes',
    'ParameterBuilder',
    'PropertyBuilder',
    'SignatureHelper',
    'TypeBuilder',
    'Label',
    'OpCode',
    'AssemblyBuilderAccess',
    'FlowControl',
    'OpCodeType',
    'OperandType',
    'PackingSize',
    'StackBehaviour',
]


# TODO

# ---------- CLASSES ---------- #

class AssemblyBuilder:
    """Defines and represents a dynamic assembly."""


class ConstructorBuilder:
    """Defines and represents a constructor of a dynamic class."""


class CustomAttributeBuilder:
    """Helps build custom attributes."""


class DynamicILInfo:
    """Provides support for alternative ways to generate the Microsoft intermediate language (MSIL) and metadata for a dynamic method, including methods for creating tokens and for inserting the code, exception handling, and local variable signature blobs."""


class DynamicMethod:
    """Defines and represents a dynamic method that can be compiled, executed, and discarded. Discarded methods are available for garbage collection."""


class EnumBuilder:
    """Describes and represents an enumeration type."""


class EventBuilder:
    """Defines events for a class."""


class FieldBuilder:
    """Defines and represents a field. This class cannot be inherited."""


class GenericTypeParameterBuilder:
    """Defines and creates generic type parameters for dynamically defined generic types and methods. This class cannot be inherited."""


class ILGenerator:
    """Generates Microsoft intermediate language (MSIL) instructions."""


class LocalBuilder:
    """Represents a local variable within a method or constructor."""


class MethodBuilder:
    """Defines and represents a method (or constructor) on a dynamic class."""


class ModuleBuilder:
    """Defines and represents a module in a dynamic assembly."""


class OpCodes:
    """Provides field representations of the Microsoft Intermediate Language (MSIL) instructions for emission by the ILGenerator class members (such as Emit(OpCode))."""


class ParameterBuilder:
    """Creates or associates parameter information."""


class PropertyBuilder:
    """Defines the properties for a type."""


class SignatureHelper:
    """Provides methods for building signatures."""


class TypeBuilder:
    """Defines and creates new instances of classes during run time."""


# ---------- STRUCTS ---------- #

class Label:
    """Represents a label in the instruction stream. Label is used in conjunction with the ILGenerator class."""


class OpCode:
    """Describes an intermediate language (IL) instruction."""


# ---------- ENUMS ---------- #

class AssemblyBuilderAccess:
    """Defines the access modes for a dynamic assembly."""


class FlowControl:
    """Describes how an instruction alters the flow of control."""


class OpCodeType:
    """Describes the types of the Microsoft intermediate language (MSIL) instructions."""


class OperandType:
    """Describes the operand type of Microsoft intermediate language (MSIL) instruction."""


class PackingSize:
    """Specifies one of two factors that determine the memory alignment of fields when a type is marshaled."""


class StackBehaviour:
    """Describes how values are pushed onto a stack or popped off a stack."""
