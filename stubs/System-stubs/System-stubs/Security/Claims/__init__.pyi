from __future__ import annotations

from abc import ABC
from typing import Union

from System import Object, Void
from System.Collections.Generic import IEnumerable
from System.Security.Claims import Claim, ClaimsIdentity

# ---------- Types ---------- #

ObjectType = Object
VoidType = Union[None, Void]

# ---------- Classes ---------- #

class DynamicRoleClaimProvider(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def AddDynamicRoleClaims(claimsIdentity: ClaimsIdentity, claims: IEnumerable[Claim]) -> VoidType: ...
    
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
    DynamicRoleClaimProvider,
]
