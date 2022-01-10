from __future__ import annotations

from typing import Union

from System import Attribute, String, Void
from System.Runtime.InteropServices import _Attribute

# ---------- Types ---------- #

StringType = Union[str, String]
VoidType = Union[None, Void]

# ---------- Classes ---------- #

class ExcludeFromCodeCoverageAttribute(Attribute, _Attribute):
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


class SuppressMessageAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, category: StringType, checkId: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Category(self) -> StringType: ...
    
    @property
    def CheckId(self) -> StringType: ...
    
    @property
    def Justification(self) -> StringType: ...
    
    @Justification.setter
    def Justification(self, value: StringType) -> None: ...
    
    @property
    def MessageId(self) -> StringType: ...
    
    @MessageId.setter
    def MessageId(self, value: StringType) -> None: ...
    
    @property
    def Scope(self) -> StringType: ...
    
    @Scope.setter
    def Scope(self, value: StringType) -> None: ...
    
    @property
    def Target(self) -> StringType: ...
    
    @Target.setter
    def Target(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Category(self) -> StringType: ...
    
    def get_CheckId(self) -> StringType: ...
    
    def get_Justification(self) -> StringType: ...
    
    def get_MessageId(self) -> StringType: ...
    
    def get_Scope(self) -> StringType: ...
    
    def get_Target(self) -> StringType: ...
    
    def set_Justification(self, value: StringType) -> VoidType: ...
    
    def set_MessageId(self, value: StringType) -> VoidType: ...
    
    def set_Scope(self, value: StringType) -> VoidType: ...
    
    def set_Target(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SuppressMessageAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, category: StringType, checkId: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Category(self) -> StringType: ...
    
    @property
    def CheckId(self) -> StringType: ...
    
    @property
    def Justification(self) -> StringType: ...
    
    @Justification.setter
    def Justification(self, value: StringType) -> None: ...
    
    @property
    def MessageId(self) -> StringType: ...
    
    @MessageId.setter
    def MessageId(self, value: StringType) -> None: ...
    
    @property
    def Scope(self) -> StringType: ...
    
    @Scope.setter
    def Scope(self, value: StringType) -> None: ...
    
    @property
    def Target(self) -> StringType: ...
    
    @Target.setter
    def Target(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Category(self) -> StringType: ...
    
    def get_CheckId(self) -> StringType: ...
    
    def get_Justification(self) -> StringType: ...
    
    def get_MessageId(self) -> StringType: ...
    
    def get_Scope(self) -> StringType: ...
    
    def get_Target(self) -> StringType: ...
    
    def set_Justification(self, value: StringType) -> VoidType: ...
    
    def set_MessageId(self, value: StringType) -> VoidType: ...
    
    def set_Scope(self, value: StringType) -> VoidType: ...
    
    def set_Target(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SuppressMessageAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, category: StringType, checkId: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Category(self) -> StringType: ...
    
    @property
    def CheckId(self) -> StringType: ...
    
    @property
    def Justification(self) -> StringType: ...
    
    @Justification.setter
    def Justification(self, value: StringType) -> None: ...
    
    @property
    def MessageId(self) -> StringType: ...
    
    @MessageId.setter
    def MessageId(self, value: StringType) -> None: ...
    
    @property
    def Scope(self) -> StringType: ...
    
    @Scope.setter
    def Scope(self, value: StringType) -> None: ...
    
    @property
    def Target(self) -> StringType: ...
    
    @Target.setter
    def Target(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Category(self) -> StringType: ...
    
    def get_CheckId(self) -> StringType: ...
    
    def get_Justification(self) -> StringType: ...
    
    def get_MessageId(self) -> StringType: ...
    
    def get_Scope(self) -> StringType: ...
    
    def get_Target(self) -> StringType: ...
    
    def set_Justification(self, value: StringType) -> VoidType: ...
    
    def set_MessageId(self, value: StringType) -> VoidType: ...
    
    def set_Scope(self, value: StringType) -> VoidType: ...
    
    def set_Target(self, value: StringType) -> VoidType: ...
    
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
    ExcludeFromCodeCoverageAttribute,
    SuppressMessageAttribute,
]
