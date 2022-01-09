from __future__ import annotations

from abc import ABC
from typing import Union, overload

from Microsoft.Win32.SafeHandles import SafeHandleZeroOrMinusOneIsInvalid
from System import Boolean, IDisposable, IntPtr
from System.Runtime.InteropServices import SafeBuffer, SafeHandle

# ---------- Types ---------- #

BooleanType = Union[bool, Boolean]
NIntType = Union[int, IntPtr]

# ---------- Classes ---------- #

class SafeAxlBufferHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SafeBCryptAlgorithmHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SafeBCryptHashHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SafeBCryptKeyHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SafeCapiHandleBase(ABC, SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SafeCapiHashHandle(SafeCapiHandleBase, IDisposable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def InvalidHandle() -> SafeCapiHashHandle: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def get_InvalidHandle() -> SafeCapiHashHandle: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SafeCapiKeyHandle(SafeCapiHandleBase, IDisposable):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SafeCspHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Duplicate(self) -> SafeCspHandle: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SafeMemoryMappedFileHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SafeMemoryMappedViewHandle(SafeBuffer, IDisposable):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SafeNCryptHandle(ABC, SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SafeNCryptKeyHandle(SafeNCryptHandle, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, handle: NIntType, parentHandle: SafeHandle): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SafeNCryptProviderHandle(SafeNCryptHandle, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SafeNCryptSecretHandle(SafeNCryptHandle, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SafePerfProviderHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SafePipeHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, preexistingHandle: NIntType, ownsHandle: BooleanType): ...
    
    # No Properties
    
    # No Methods
    
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
    SafeAxlBufferHandle,
    SafeBCryptAlgorithmHandle,
    SafeBCryptHashHandle,
    SafeBCryptKeyHandle,
    SafeCapiHandleBase,
    SafeCapiHashHandle,
    SafeCapiKeyHandle,
    SafeCspHandle,
    SafeMemoryMappedFileHandle,
    SafeMemoryMappedViewHandle,
    SafeNCryptHandle,
    SafeNCryptKeyHandle,
    SafeNCryptProviderHandle,
    SafeNCryptSecretHandle,
    SafePerfProviderHandle,
    SafePipeHandle,
]
