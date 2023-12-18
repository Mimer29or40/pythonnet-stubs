from __future__ import annotations

from abc import ABC
from typing import Union

from System import Object
from System import String
from System import Type
from System import Void
from System.Collections import ArrayList
from System.Reflection import RuntimeAssembly
from System.Reflection.Emit import ModuleBuilder

# ---------- Types ---------- #

ObjectType = Object
StringType = Union[str, String]
TypeType = Union[type, Type]
VoidType = Union[None, Void]

# ---------- Classes ---------- #

class EventItfInfo(ObjectType):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(
        self,
        strEventItfName: StringType,
        strSrcItfName: StringType,
        strEventProviderName: StringType,
        asmImport: RuntimeAssembly,
        asmSrcItf: RuntimeAssembly,
    ): ...

    # No Properties

    # ---------- Methods ---------- #

    def GetEventItfType(self) -> TypeType: ...
    def GetEventProviderName(self) -> StringType: ...
    def GetSrcItfType(self) -> TypeType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class EventProviderWriter(ObjectType):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(
        self,
        OutputModule: ModuleBuilder,
        strDestTypeName: StringType,
        EventItfType: TypeType,
        SrcItfType: TypeType,
        SinkHelperType: TypeType,
    ): ...

    # No Properties

    # ---------- Methods ---------- #

    def Perform(self) -> TypeType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class EventSinkHelperWriter(ObjectType):
    # ---------- Fields ---------- #

    @staticmethod
    @property
    def GeneratedTypeNamePostfix() -> StringType: ...

    # ---------- Constructors ---------- #

    def __init__(
        self, OutputModule: ModuleBuilder, InputType: TypeType, EventItfType: TypeType
    ): ...

    # No Properties

    # ---------- Methods ---------- #

    def Perform(self) -> TypeType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class NameSpaceExtractor(ABC, ObjectType):
    # No Fields

    # No Constructors

    # No Properties

    # ---------- Methods ---------- #

    @staticmethod
    def ExtractNameSpace(FullyQualifiedTypeName: StringType) -> StringType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class TCEAdapterGenerator(ObjectType):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # No Properties

    # ---------- Methods ---------- #

    def Process(self, ModBldr: ModuleBuilder, EventItfList: ArrayList) -> VoidType: ...

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
    EventItfInfo,
    EventProviderWriter,
    EventSinkHelperWriter,
    NameSpaceExtractor,
    TCEAdapterGenerator,
]
