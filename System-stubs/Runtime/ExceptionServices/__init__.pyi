from __future__ import annotations

from typing import Union

from System import Attribute, EventArgs, Exception, Object, Void
from System.Runtime.InteropServices import _Attribute

# ---------- Types ---------- #

ObjectType = Object
VoidType = Union[None, Void]


# ---------- Classes ---------- #

class ExceptionDispatchInfo(ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def SourceException(self) -> Exception: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def Capture(source: Exception) -> ExceptionDispatchInfo: ...
    
    def Throw(self) -> VoidType: ...
    
    def get_SourceException(self) -> Exception: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ExceptionDispatchInfo(ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def SourceException(self) -> Exception: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def Capture(source: Exception) -> ExceptionDispatchInfo: ...
    
    def Throw(self) -> VoidType: ...
    
    def get_SourceException(self) -> Exception: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ExceptionDispatchInfo(ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def SourceException(self) -> Exception: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def Capture(source: Exception) -> ExceptionDispatchInfo: ...
    
    def Throw(self) -> VoidType: ...
    
    def get_SourceException(self) -> Exception: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class FirstChanceExceptionEventArgs(EventArgs):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, exception: Exception): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Exception(self) -> Exception: ...
    
    # ---------- Methods ---------- #
    
    def get_Exception(self) -> Exception: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class FirstChanceExceptionEventArgs(EventArgs):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, exception: Exception): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Exception(self) -> Exception: ...
    
    # ---------- Methods ---------- #
    
    def get_Exception(self) -> Exception: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class FirstChanceExceptionEventArgs(EventArgs):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, exception: Exception): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Exception(self) -> Exception: ...
    
    # ---------- Methods ---------- #
    
    def get_Exception(self) -> Exception: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class HandleProcessCorruptedStateExceptionsAttribute(Attribute, _Attribute):
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


class HandleProcessCorruptedStateExceptionsAttribute(Attribute, _Attribute):
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


class HandleProcessCorruptedStateExceptionsAttribute(Attribute, _Attribute):
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


# No Structs

# No Interfaces

# No Enums

# No Delegates

__all__ = [
    ExceptionDispatchInfo,
    FirstChanceExceptionEventArgs,
    HandleProcessCorruptedStateExceptionsAttribute,
]
