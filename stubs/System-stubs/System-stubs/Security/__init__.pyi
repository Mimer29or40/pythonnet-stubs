from __future__ import annotations

from abc import ABC
from typing import Union

from System import IntPtr, Object
from System.Security import SecureString

# ---------- Types ---------- #

NIntType = Union[int, IntPtr]
ObjectType = Object

# ---------- Classes ---------- #

class SecureStringMarshal(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def SecureStringToCoTaskMemAnsi(s: SecureString) -> NIntType: ...
    
    @staticmethod
    def SecureStringToCoTaskMemUnicode(s: SecureString) -> NIntType: ...
    
    @staticmethod
    def SecureStringToGlobalAllocAnsi(s: SecureString) -> NIntType: ...
    
    @staticmethod
    def SecureStringToGlobalAllocUnicode(s: SecureString) -> NIntType: ...
    
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
    SecureStringMarshal,
]
