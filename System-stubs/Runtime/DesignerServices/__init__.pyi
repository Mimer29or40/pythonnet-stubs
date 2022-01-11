from __future__ import annotations

from typing import Union, overload

from System import Object, String, Type, Void
from System.Collections.Generic import IEnumerable
from System.Reflection import Assembly

# ---------- Types ---------- #

ObjectType = Object
StringType = Union[str, String]
TypeType = Union[type, Type]
VoidType = Union[None, Void]


# ---------- Classes ---------- #

class WindowsRuntimeDesignerContext(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, paths: IEnumerable[StringType], name: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Name(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetAssembly(self, assemblyName: StringType) -> Assembly: ...
    
    @overload
    def GetType(self, typeName: StringType) -> TypeType: ...
    
    @staticmethod
    def InitializeSharedContext(paths: IEnumerable[StringType]) -> VoidType: ...
    
    @staticmethod
    def SetIterationContext(context: WindowsRuntimeDesignerContext) -> VoidType: ...
    
    def get_Name(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class WindowsRuntimeDesignerContext(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, paths: IEnumerable[StringType], name: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Name(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetAssembly(self, assemblyName: StringType) -> Assembly: ...
    
    @overload
    def GetType(self, typeName: StringType) -> TypeType: ...
    
    @staticmethod
    def InitializeSharedContext(paths: IEnumerable[StringType]) -> VoidType: ...
    
    @staticmethod
    def SetIterationContext(context: WindowsRuntimeDesignerContext) -> VoidType: ...
    
    def get_Name(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class WindowsRuntimeDesignerContext(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, paths: IEnumerable[StringType], name: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Name(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetAssembly(self, assemblyName: StringType) -> Assembly: ...
    
    @overload
    def GetType(self, typeName: StringType) -> TypeType: ...
    
    @staticmethod
    def InitializeSharedContext(paths: IEnumerable[StringType]) -> VoidType: ...
    
    @staticmethod
    def SetIterationContext(context: WindowsRuntimeDesignerContext) -> VoidType: ...
    
    def get_Name(self) -> StringType: ...
    
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
    WindowsRuntimeDesignerContext,
]
