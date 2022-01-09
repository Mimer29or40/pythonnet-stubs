from __future__ import annotations

from typing import Union

from System import Enum, Int32

# ---------- Types ---------- #

IntType = Union[int, Int32]

# No Classes

# No Structs

# No Interfaces

# ---------- Enums ---------- #

class ManifestKinds(Enum):
    #None: IntType = 0
    Deployment: IntType = 1
    Application: IntType = 2
    ApplicationAndDeployment: IntType = 3


# No Delegates

__all__ = [
    ManifestKinds,
]
