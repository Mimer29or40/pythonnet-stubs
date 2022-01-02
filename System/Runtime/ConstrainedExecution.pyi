__all__ = [
    'CriticalFinalizerObject',
    'PrePrepareMethodAttribute',
    'ReliabilityContractAttribute',
    'Cer',
    'Consistency',
]


# TODO

# -------- CLASSES -------- #

class CriticalFinalizerObject:
    """Ensures that all finalization code in derived classes is marked as critical."""


class PrePrepareMethodAttribute:
    """Instructs the native image generation service to prepare a method for inclusion in a constrained execution region (CER)."""


class ReliabilityContractAttribute:
    """Defines a contract for reliability between the author of some code, and the developers who have a dependency on that code."""


# -------- ENUMS -------- #

class Cer:
    """Specifies a method's behavior when called within a constrained execution region."""


class Consistency:
    """Specifies a reliability contract."""
