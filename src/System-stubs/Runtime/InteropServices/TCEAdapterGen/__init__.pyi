"""Automatically generated stubs for C# namespace: System.Runtime.InteropServices.TCEAdapterGen."""

from abc import ABC
from typing import ClassVar

from System import Object
from System import Type
from System.Collections import ArrayList
from System.Reflection import RuntimeAssembly
from System.Reflection.Emit import ModuleBuilder

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class EventItfInfo(Object):
    """"""
    def __init__(
        self,
        strEventItfName: str,
        strSrcItfName: str,
        strEventProviderName: str,
        asmImport: RuntimeAssembly,
        asmSrcItf: RuntimeAssembly,
    ) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEventItfType(self) -> Type:
        """"""
    def GetEventProviderName(self) -> str:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetSrcItfType(self) -> Type:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class EventProviderWriter(Object):
    """"""
    def __init__(
        self,
        OutputModule: ModuleBuilder,
        strDestTypeName: str,
        EventItfType: Type,
        SrcItfType: Type,
        SinkHelperType: Type,
    ) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Perform(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class EventSinkHelperWriter(Object):
    """"""

    GeneratedTypeNamePostfix: ClassVar[str]
    """"""
    def __init__(self, OutputModule: ModuleBuilder, InputType: Type, EventItfType: Type) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Perform(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class NameSpaceExtractor(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def ExtractNameSpace(cls, FullyQualifiedTypeName: str) -> str:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class TCEAdapterGenerator(Object):
    """"""
    def __init__(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Process(self, ModBldr: ModuleBuilder, EventItfList: ArrayList) -> None:
        """"""
    def ToString(self) -> str:
        """"""
