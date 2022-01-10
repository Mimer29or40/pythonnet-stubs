from __future__ import annotations

from abc import ABC
from typing import Union

from System import Object, String, Void
from System.Configuration import ConfigurationSection

# ---------- Types ---------- #

ObjectType = Object
StringType = Union[str, String]
VoidType = Union[None, Void]

# ---------- Classes ---------- #

class XmlConfigurationString(ABC, ObjectType):
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


class XmlConfigurationString(ABC, ObjectType):
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


class XmlReaderSection(ConfigurationSection):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CollapseWhiteSpaceIntoEmptyStringString(self) -> StringType: ...
    
    @CollapseWhiteSpaceIntoEmptyStringString.setter
    def CollapseWhiteSpaceIntoEmptyStringString(self, value: StringType) -> None: ...
    
    @property
    def ProhibitDefaultResolverString(self) -> StringType: ...
    
    @ProhibitDefaultResolverString.setter
    def ProhibitDefaultResolverString(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_CollapseWhiteSpaceIntoEmptyStringString(self) -> StringType: ...
    
    def get_ProhibitDefaultResolverString(self) -> StringType: ...
    
    def set_CollapseWhiteSpaceIntoEmptyStringString(self, value: StringType) -> VoidType: ...
    
    def set_ProhibitDefaultResolverString(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlReaderSection(ConfigurationSection):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CollapseWhiteSpaceIntoEmptyStringString(self) -> StringType: ...
    
    @CollapseWhiteSpaceIntoEmptyStringString.setter
    def CollapseWhiteSpaceIntoEmptyStringString(self, value: StringType) -> None: ...
    
    @property
    def ProhibitDefaultResolverString(self) -> StringType: ...
    
    @ProhibitDefaultResolverString.setter
    def ProhibitDefaultResolverString(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_CollapseWhiteSpaceIntoEmptyStringString(self) -> StringType: ...
    
    def get_ProhibitDefaultResolverString(self) -> StringType: ...
    
    def set_CollapseWhiteSpaceIntoEmptyStringString(self, value: StringType) -> VoidType: ...
    
    def set_ProhibitDefaultResolverString(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XsltConfigSection(ConfigurationSection):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ProhibitDefaultResolverString(self) -> StringType: ...
    
    @ProhibitDefaultResolverString.setter
    def ProhibitDefaultResolverString(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_ProhibitDefaultResolverString(self) -> StringType: ...
    
    def set_ProhibitDefaultResolverString(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XsltConfigSection(ConfigurationSection):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ProhibitDefaultResolverString(self) -> StringType: ...
    
    @ProhibitDefaultResolverString.setter
    def ProhibitDefaultResolverString(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_ProhibitDefaultResolverString(self) -> StringType: ...
    
    def set_ProhibitDefaultResolverString(self, value: StringType) -> VoidType: ...
    
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
    XmlConfigurationString,
    XmlReaderSection,
    XsltConfigSection,
]
