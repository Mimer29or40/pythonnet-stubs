__all__ = [
    'Contract',
    'ContractAbbreviatorAttribute',
    'ContractArgumentValidatorAttribute',
    'ContractClassAttribute',
    'ContractClassForAttribute',
    'ContractFailedEventArgs',
    'ContractInvariantMethodAttribute',
    'ContractOptionAttribute',
    'ContractPublicPropertyNameAttribute',
    'ContractReferenceAssemblyAttribute',
    'ContractRuntimeIgnoredAttribute',
    'ContractVerificationAttribute',
    'PureAttribute',
    'ContractFailureKind',
]


# TODO

# ---------- CLASSES ---------- #

class Contract:
    """Contains static methods for representing program contracts such as preconditions, postconditions, and object invariants."""


class ContractAbbreviatorAttribute:
    """Defines abbreviations that you can use in place of the full contract syntax."""


class ContractArgumentValidatorAttribute:
    """Enables the factoring of legacy if-then-throw code into separate methods for reuse, and provides full control over thrown exceptions and arguments."""


class ContractClassAttribute:
    """Specifies that a separate type contains the code contracts for this type."""


class ContractClassForAttribute:
    """Specifies that a class is a contract for a type."""


class ContractFailedEventArgs:
    """Provides methods and data for the ContractFailed event."""


class ContractInvariantMethodAttribute:
    """Marks a method as being the invariant method for a class."""


class ContractOptionAttribute:
    """Enables you to set contract and tool options at assembly, type, or method granularity."""


class ContractPublicPropertyNameAttribute:
    """Specifies that a field can be used in method contracts when the field has less visibility than the method."""


class ContractReferenceAssemblyAttribute:
    """Specifies that an assembly is a reference assembly that contains contracts."""


class ContractRuntimeIgnoredAttribute:
    """Identifies a member that has no run-time behavior."""


class ContractVerificationAttribute:
    """Instructs analysis tools to assume the correctness of an assembly, type, or member without performing static verification."""


class PureAttribute:
    """Indicates that a type or method is pure, that is, it does not make any visible state changes."""


# ---------- ENUMS ---------- #

class ContractFailureKind:
    """Specifies the type of contract that failed."""
