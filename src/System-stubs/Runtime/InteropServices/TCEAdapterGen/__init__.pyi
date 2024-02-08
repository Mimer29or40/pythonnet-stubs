from __future__ import annotations

from abc import ABC
from typing import ClassVar
from typing import Final

from System import Object
from System import Type
from System.Collections import ArrayList
from System.Reflection import RuntimeAssembly
from System.Reflection.Emit import ModuleBuilder

class EventItfInfo(Object):
    """"""

    def __init__(
        self,
        strEventItfName: str,
        strSrcItfName: str,
        strEventProviderName: str,
        asmImport: RuntimeAssembly,
        asmSrcItf: RuntimeAssembly,
    ):
        """

        :param strEventItfName:
        :param strSrcItfName:
        :param strEventProviderName:
        :param asmImport:
        :param asmSrcItf:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetEventItfType(self) -> Type:
        """

        :return:
        """
    def GetEventProviderName(self) -> str:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetSrcItfType(self) -> Type:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class EventProviderWriter(Object):
    """"""

    def __init__(
        self,
        OutputModule: ModuleBuilder,
        strDestTypeName: str,
        EventItfType: Type,
        SrcItfType: Type,
        SinkHelperType: Type,
    ):
        """

        :param OutputModule:
        :param strDestTypeName:
        :param EventItfType:
        :param SrcItfType:
        :param SinkHelperType:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def Perform(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class EventSinkHelperWriter(Object):
    """"""

    GeneratedTypeNamePostfix: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    def __init__(self, OutputModule: ModuleBuilder, InputType: Type, EventItfType: Type):
        """

        :param OutputModule:
        :param InputType:
        :param EventItfType:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def Perform(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class NameSpaceExtractor(ABC, Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @classmethod
    def ExtractNameSpace(cls, FullyQualifiedTypeName: str) -> str:
        """

        :param FullyQualifiedTypeName:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class TCEAdapterGenerator(Object):
    """"""

    def __init__(self):
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def Process(self, ModBldr: ModuleBuilder, EventItfList: ArrayList) -> None:
        """

        :param ModBldr:
        :param EventItfList:
        """
    def ToString(self) -> str:
        """

        :return:
        """
