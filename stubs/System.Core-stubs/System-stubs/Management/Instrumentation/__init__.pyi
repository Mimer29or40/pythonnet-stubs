from __future__ import annotations

from abc import ABC
from typing import Union, overload

from System import Attribute, Boolean, Enum, Exception, Int32, String, Type, Void
from System.Runtime.InteropServices import _Attribute, _Exception
from System.Runtime.Serialization import ISerializable

# ---------- Types ---------- #

BooleanType = Union[bool, Boolean]
IntType = Union[int, Int32]
StringType = Union[str, String]
TypeType = Union[type, Type]
VoidType = Union[None, Void]

# ---------- Classes ---------- #

class InstanceNotFoundException(InstrumentationException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class InstanceNotFoundException(InstrumentationException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class InstrumentationBaseException(Exception, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class InstrumentationBaseException(Exception, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class InstrumentationException(InstrumentationBaseException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, innerException: Exception): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class InstrumentationException(InstrumentationBaseException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, innerException: Exception): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ManagementBindAttribute(ManagementNewInstanceAttribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Schema(self) -> TypeType: ...
    
    @Schema.setter
    def Schema(self, value: TypeType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Schema(self) -> TypeType: ...
    
    def set_Schema(self, value: TypeType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ManagementBindAttribute(ManagementNewInstanceAttribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Schema(self) -> TypeType: ...
    
    @Schema.setter
    def Schema(self, value: TypeType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Schema(self) -> TypeType: ...
    
    def set_Schema(self, value: TypeType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ManagementCommitAttribute(ManagementMemberAttribute, _Attribute):
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


class ManagementCommitAttribute(ManagementMemberAttribute, _Attribute):
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


class ManagementConfigurationAttribute(ManagementMemberAttribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Mode(self) -> ManagementConfigurationType: ...
    
    @Mode.setter
    def Mode(self, value: ManagementConfigurationType) -> None: ...
    
    @property
    def Schema(self) -> TypeType: ...
    
    @Schema.setter
    def Schema(self, value: TypeType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Mode(self) -> ManagementConfigurationType: ...
    
    def get_Schema(self) -> TypeType: ...
    
    def set_Mode(self, value: ManagementConfigurationType) -> VoidType: ...
    
    def set_Schema(self, value: TypeType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ManagementConfigurationAttribute(ManagementMemberAttribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Mode(self) -> ManagementConfigurationType: ...
    
    @Mode.setter
    def Mode(self, value: ManagementConfigurationType) -> None: ...
    
    @property
    def Schema(self) -> TypeType: ...
    
    @Schema.setter
    def Schema(self, value: TypeType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Mode(self) -> ManagementConfigurationType: ...
    
    def get_Schema(self) -> TypeType: ...
    
    def set_Mode(self, value: ManagementConfigurationType) -> VoidType: ...
    
    def set_Schema(self, value: TypeType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ManagementCreateAttribute(ManagementNewInstanceAttribute, _Attribute):
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


class ManagementCreateAttribute(ManagementNewInstanceAttribute, _Attribute):
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


class ManagementEntityAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def External(self) -> BooleanType: ...
    
    @External.setter
    def External(self, value: BooleanType) -> None: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @Name.setter
    def Name(self, value: StringType) -> None: ...
    
    @property
    def Singleton(self) -> BooleanType: ...
    
    @Singleton.setter
    def Singleton(self, value: BooleanType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_External(self) -> BooleanType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_Singleton(self) -> BooleanType: ...
    
    def set_External(self, value: BooleanType) -> VoidType: ...
    
    def set_Name(self, value: StringType) -> VoidType: ...
    
    def set_Singleton(self, value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ManagementEntityAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def External(self) -> BooleanType: ...
    
    @External.setter
    def External(self, value: BooleanType) -> None: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @Name.setter
    def Name(self, value: StringType) -> None: ...
    
    @property
    def Singleton(self) -> BooleanType: ...
    
    @Singleton.setter
    def Singleton(self, value: BooleanType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_External(self) -> BooleanType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_Singleton(self) -> BooleanType: ...
    
    def set_External(self, value: BooleanType) -> VoidType: ...
    
    def set_Name(self, value: StringType) -> VoidType: ...
    
    def set_Singleton(self, value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ManagementEnumeratorAttribute(ManagementNewInstanceAttribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Schema(self) -> TypeType: ...
    
    @Schema.setter
    def Schema(self, value: TypeType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Schema(self) -> TypeType: ...
    
    def set_Schema(self, value: TypeType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ManagementEnumeratorAttribute(ManagementNewInstanceAttribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Schema(self) -> TypeType: ...
    
    @Schema.setter
    def Schema(self, value: TypeType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Schema(self) -> TypeType: ...
    
    def set_Schema(self, value: TypeType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ManagementKeyAttribute(ManagementMemberAttribute, _Attribute):
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


class ManagementKeyAttribute(ManagementMemberAttribute, _Attribute):
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


class ManagementMemberAttribute(ABC, Attribute, _Attribute):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Name(self) -> StringType: ...
    
    @Name.setter
    def Name(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Name(self) -> StringType: ...
    
    def set_Name(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ManagementMemberAttribute(ABC, Attribute, _Attribute):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Name(self) -> StringType: ...
    
    @Name.setter
    def Name(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Name(self) -> StringType: ...
    
    def set_Name(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ManagementNameAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, name: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Name(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_Name(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ManagementNameAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, name: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Name(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_Name(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ManagementNewInstanceAttribute(ABC, ManagementMemberAttribute, _Attribute):
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


class ManagementNewInstanceAttribute(ABC, ManagementMemberAttribute, _Attribute):
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


class ManagementProbeAttribute(ManagementMemberAttribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Schema(self) -> TypeType: ...
    
    @Schema.setter
    def Schema(self, value: TypeType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Schema(self) -> TypeType: ...
    
    def set_Schema(self, value: TypeType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ManagementProbeAttribute(ManagementMemberAttribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Schema(self) -> TypeType: ...
    
    @Schema.setter
    def Schema(self, value: TypeType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Schema(self) -> TypeType: ...
    
    def set_Schema(self, value: TypeType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ManagementReferenceAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Type(self) -> StringType: ...
    
    @Type.setter
    def Type(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Type(self) -> StringType: ...
    
    def set_Type(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ManagementReferenceAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Type(self) -> StringType: ...
    
    @Type.setter
    def Type(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Type(self) -> StringType: ...
    
    def set_Type(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ManagementRemoveAttribute(ManagementMemberAttribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Schema(self) -> TypeType: ...
    
    @Schema.setter
    def Schema(self, value: TypeType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Schema(self) -> TypeType: ...
    
    def set_Schema(self, value: TypeType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ManagementRemoveAttribute(ManagementMemberAttribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Schema(self) -> TypeType: ...
    
    @Schema.setter
    def Schema(self, value: TypeType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Schema(self) -> TypeType: ...
    
    def set_Schema(self, value: TypeType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ManagementTaskAttribute(ManagementMemberAttribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Schema(self) -> TypeType: ...
    
    @Schema.setter
    def Schema(self, value: TypeType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Schema(self) -> TypeType: ...
    
    def set_Schema(self, value: TypeType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ManagementTaskAttribute(ManagementMemberAttribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Schema(self) -> TypeType: ...
    
    @Schema.setter
    def Schema(self, value: TypeType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Schema(self) -> TypeType: ...
    
    def set_Schema(self, value: TypeType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class WmiConfigurationAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, scope: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def HostingGroup(self) -> StringType: ...
    
    @HostingGroup.setter
    def HostingGroup(self, value: StringType) -> None: ...
    
    @property
    def HostingModel(self) -> ManagementHostingModel: ...
    
    @HostingModel.setter
    def HostingModel(self, value: ManagementHostingModel) -> None: ...
    
    @property
    def IdentifyLevel(self) -> BooleanType: ...
    
    @IdentifyLevel.setter
    def IdentifyLevel(self, value: BooleanType) -> None: ...
    
    @property
    def NamespaceSecurity(self) -> StringType: ...
    
    @NamespaceSecurity.setter
    def NamespaceSecurity(self, value: StringType) -> None: ...
    
    @property
    def Scope(self) -> StringType: ...
    
    @property
    def SecurityRestriction(self) -> StringType: ...
    
    @SecurityRestriction.setter
    def SecurityRestriction(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_HostingGroup(self) -> StringType: ...
    
    def get_HostingModel(self) -> ManagementHostingModel: ...
    
    def get_IdentifyLevel(self) -> BooleanType: ...
    
    def get_NamespaceSecurity(self) -> StringType: ...
    
    def get_Scope(self) -> StringType: ...
    
    def get_SecurityRestriction(self) -> StringType: ...
    
    def set_HostingGroup(self, value: StringType) -> VoidType: ...
    
    def set_HostingModel(self, value: ManagementHostingModel) -> VoidType: ...
    
    def set_IdentifyLevel(self, value: BooleanType) -> VoidType: ...
    
    def set_NamespaceSecurity(self, value: StringType) -> VoidType: ...
    
    def set_SecurityRestriction(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class WmiConfigurationAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, scope: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def HostingGroup(self) -> StringType: ...
    
    @HostingGroup.setter
    def HostingGroup(self, value: StringType) -> None: ...
    
    @property
    def HostingModel(self) -> ManagementHostingModel: ...
    
    @HostingModel.setter
    def HostingModel(self, value: ManagementHostingModel) -> None: ...
    
    @property
    def IdentifyLevel(self) -> BooleanType: ...
    
    @IdentifyLevel.setter
    def IdentifyLevel(self, value: BooleanType) -> None: ...
    
    @property
    def NamespaceSecurity(self) -> StringType: ...
    
    @NamespaceSecurity.setter
    def NamespaceSecurity(self, value: StringType) -> None: ...
    
    @property
    def Scope(self) -> StringType: ...
    
    @property
    def SecurityRestriction(self) -> StringType: ...
    
    @SecurityRestriction.setter
    def SecurityRestriction(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_HostingGroup(self) -> StringType: ...
    
    def get_HostingModel(self) -> ManagementHostingModel: ...
    
    def get_IdentifyLevel(self) -> BooleanType: ...
    
    def get_NamespaceSecurity(self) -> StringType: ...
    
    def get_Scope(self) -> StringType: ...
    
    def get_SecurityRestriction(self) -> StringType: ...
    
    def set_HostingGroup(self, value: StringType) -> VoidType: ...
    
    def set_HostingModel(self, value: ManagementHostingModel) -> VoidType: ...
    
    def set_IdentifyLevel(self, value: BooleanType) -> VoidType: ...
    
    def set_NamespaceSecurity(self, value: StringType) -> VoidType: ...
    
    def set_SecurityRestriction(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# No Structs

# No Interfaces

# ---------- Enums ---------- #

class ManagementConfigurationType(Enum):
    Apply: IntType = 0
    OnCommit: IntType = 1


class ManagementConfigurationType(Enum):
    Apply: IntType = 0
    OnCommit: IntType = 1


class ManagementHostingModel(Enum):
    Decoupled: IntType = 0
    NetworkService: IntType = 1
    LocalService: IntType = 2
    LocalSystem: IntType = 3


class ManagementHostingModel(Enum):
    Decoupled: IntType = 0
    NetworkService: IntType = 1
    LocalService: IntType = 2
    LocalSystem: IntType = 3


# No Delegates

__all__ = [
    InstanceNotFoundException,
    InstrumentationBaseException,
    InstrumentationException,
    ManagementBindAttribute,
    ManagementCommitAttribute,
    ManagementConfigurationAttribute,
    ManagementCreateAttribute,
    ManagementEntityAttribute,
    ManagementEnumeratorAttribute,
    ManagementKeyAttribute,
    ManagementMemberAttribute,
    ManagementNameAttribute,
    ManagementNewInstanceAttribute,
    ManagementProbeAttribute,
    ManagementReferenceAttribute,
    ManagementRemoveAttribute,
    ManagementTaskAttribute,
    WmiConfigurationAttribute,
    ManagementConfigurationType,
    ManagementHostingModel,
]
