from __future__ import annotations

from typing import Protocol, Union

from System import Type

# ---------- Types ---------- #

TypeType = Union[type, Type]

# No Classes

# No Structs

# ---------- Interfaces ---------- #

class ICustomTypeProvider(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetCustomType(self) -> TypeType: ...
    
    # No Events


# No Enums

# No Delegates

__all__ = [
    ICustomTypeProvider,
]
