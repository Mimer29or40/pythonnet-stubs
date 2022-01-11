from __future__ import annotations

from abc import ABC
from typing import Union

from System import Attribute, Boolean, Enum, Int32, Object, String, Void
from System.Runtime.InteropServices import _Attribute

# ---------- Types ---------- #

BooleanType = Union[bool, Boolean]
IntType = Union[int, Int32]
ObjectType = Object
StringType = Union[str, String]
VoidType = Union[None, Void]


# ---------- Classes ---------- #

class RemotingCachedData(ABC, ObjectType):
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


class RemotingFieldCachedData(RemotingCachedData):
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


class RemotingMethodCachedData(RemotingCachedData):
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


class RemotingParameterCachedData(RemotingCachedData):
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


class RemotingTypeCachedData(RemotingCachedData):
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


class SoapAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Embedded(self) -> BooleanType: ...
    
    @Embedded.setter
    def Embedded(self, value: BooleanType) -> None: ...
    
    @property
    def UseAttribute(self) -> BooleanType: ...
    
    @UseAttribute.setter
    def UseAttribute(self, value: BooleanType) -> None: ...
    
    @property
    def XmlNamespace(self) -> StringType: ...
    
    @XmlNamespace.setter
    def XmlNamespace(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Embedded(self) -> BooleanType: ...
    
    def get_UseAttribute(self) -> BooleanType: ...
    
    def get_XmlNamespace(self) -> StringType: ...
    
    def set_Embedded(self, value: BooleanType) -> VoidType: ...
    
    def set_UseAttribute(self, value: BooleanType) -> VoidType: ...
    
    def set_XmlNamespace(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapFieldAttribute(SoapAttribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Order(self) -> IntType: ...
    
    @Order.setter
    def Order(self, value: IntType) -> None: ...
    
    @property
    def XmlElementName(self) -> StringType: ...
    
    @XmlElementName.setter
    def XmlElementName(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def IsInteropXmlElement(self) -> BooleanType: ...
    
    def get_Order(self) -> IntType: ...
    
    def get_XmlElementName(self) -> StringType: ...
    
    def set_Order(self, value: IntType) -> VoidType: ...
    
    def set_XmlElementName(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapMethodAttribute(SoapAttribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ResponseXmlElementName(self) -> StringType: ...
    
    @ResponseXmlElementName.setter
    def ResponseXmlElementName(self, value: StringType) -> None: ...
    
    @property
    def ResponseXmlNamespace(self) -> StringType: ...
    
    @ResponseXmlNamespace.setter
    def ResponseXmlNamespace(self, value: StringType) -> None: ...
    
    @property
    def ReturnXmlElementName(self) -> StringType: ...
    
    @ReturnXmlElementName.setter
    def ReturnXmlElementName(self, value: StringType) -> None: ...
    
    @property
    def SoapAction(self) -> StringType: ...
    
    @SoapAction.setter
    def SoapAction(self, value: StringType) -> None: ...
    
    @property
    def UseAttribute(self) -> BooleanType: ...
    
    @UseAttribute.setter
    def UseAttribute(self, value: BooleanType) -> None: ...
    
    @property
    def XmlNamespace(self) -> StringType: ...
    
    @XmlNamespace.setter
    def XmlNamespace(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_ResponseXmlElementName(self) -> StringType: ...
    
    def get_ResponseXmlNamespace(self) -> StringType: ...
    
    def get_ReturnXmlElementName(self) -> StringType: ...
    
    def get_SoapAction(self) -> StringType: ...
    
    def get_UseAttribute(self) -> BooleanType: ...
    
    def get_XmlNamespace(self) -> StringType: ...
    
    def set_ResponseXmlElementName(self, value: StringType) -> VoidType: ...
    
    def set_ResponseXmlNamespace(self, value: StringType) -> VoidType: ...
    
    def set_ReturnXmlElementName(self, value: StringType) -> VoidType: ...
    
    def set_SoapAction(self, value: StringType) -> VoidType: ...
    
    def set_UseAttribute(self, value: BooleanType) -> VoidType: ...
    
    def set_XmlNamespace(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapParameterAttribute(SoapAttribute, _Attribute):
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


class SoapTypeAttribute(SoapAttribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def SoapOptions(self) -> SoapOption: ...
    
    @SoapOptions.setter
    def SoapOptions(self, value: SoapOption) -> None: ...
    
    @property
    def UseAttribute(self) -> BooleanType: ...
    
    @UseAttribute.setter
    def UseAttribute(self, value: BooleanType) -> None: ...
    
    @property
    def XmlElementName(self) -> StringType: ...
    
    @XmlElementName.setter
    def XmlElementName(self, value: StringType) -> None: ...
    
    @property
    def XmlFieldOrder(self) -> XmlFieldOrderOption: ...
    
    @XmlFieldOrder.setter
    def XmlFieldOrder(self, value: XmlFieldOrderOption) -> None: ...
    
    @property
    def XmlNamespace(self) -> StringType: ...
    
    @XmlNamespace.setter
    def XmlNamespace(self, value: StringType) -> None: ...
    
    @property
    def XmlTypeName(self) -> StringType: ...
    
    @XmlTypeName.setter
    def XmlTypeName(self, value: StringType) -> None: ...
    
    @property
    def XmlTypeNamespace(self) -> StringType: ...
    
    @XmlTypeNamespace.setter
    def XmlTypeNamespace(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_SoapOptions(self) -> SoapOption: ...
    
    def get_UseAttribute(self) -> BooleanType: ...
    
    def get_XmlElementName(self) -> StringType: ...
    
    def get_XmlFieldOrder(self) -> XmlFieldOrderOption: ...
    
    def get_XmlNamespace(self) -> StringType: ...
    
    def get_XmlTypeName(self) -> StringType: ...
    
    def get_XmlTypeNamespace(self) -> StringType: ...
    
    def set_SoapOptions(self, value: SoapOption) -> VoidType: ...
    
    def set_UseAttribute(self, value: BooleanType) -> VoidType: ...
    
    def set_XmlElementName(self, value: StringType) -> VoidType: ...
    
    def set_XmlFieldOrder(self, value: XmlFieldOrderOption) -> VoidType: ...
    
    def set_XmlNamespace(self, value: StringType) -> VoidType: ...
    
    def set_XmlTypeName(self, value: StringType) -> VoidType: ...
    
    def set_XmlTypeNamespace(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# No Structs

# No Interfaces

# ---------- Enums ---------- #

class SoapOption(Enum):
    #None: IntType = 0
    AlwaysIncludeTypes: IntType = 1
    XsdString: IntType = 2
    EmbedAll: IntType = 4
    Option1: IntType = 8
    Option2: IntType = 16


class XmlFieldOrderOption(Enum):
    All: IntType = 0
    Sequence: IntType = 1
    Choice: IntType = 2


# No Delegates

__all__ = [
    RemotingCachedData,
    RemotingFieldCachedData,
    RemotingMethodCachedData,
    RemotingParameterCachedData,
    RemotingTypeCachedData,
    SoapAttribute,
    SoapFieldAttribute,
    SoapMethodAttribute,
    SoapParameterAttribute,
    SoapTypeAttribute,
    SoapOption,
    XmlFieldOrderOption,
]
