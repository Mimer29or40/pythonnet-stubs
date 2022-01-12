from __future__ import annotations

from abc import ABC
from typing import Union

from System import Exception, Object, String, Void
from System.Diagnostics.Contracts import ContractFailureKind

# ---------- Types ---------- #

ObjectType = Object
StringType = Union[str, String]
VoidType = Union[None, Void]


# ---------- Classes ---------- #

class ContractHelper(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def RaiseContractFailedEvent(failureKind: ContractFailureKind, userMessage: StringType, conditionText: StringType, innerException: Exception) -> StringType: ...
    
    @staticmethod
    def TriggerFailure(kind: ContractFailureKind, displayMessage: StringType, userMessage: StringType, conditionText: StringType, innerException: Exception) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# No Structs

# No Interfaces

# No Enums

# No Delegates

__all__ = [
    ContractHelper,
]
