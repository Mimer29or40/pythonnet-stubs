from abc import ABC

from System import Object
from System import Type
from System import TypeCode
from System.Reflection import Assembly

class ReflectionExtensions(ABC, Object):
    """"""

    @classmethod
    def Assembly(cls, type: Type) -> Assembly:
        """:param type:
        :return:
        """
    @classmethod
    def BaseType(cls, type: Type) -> Type:
        """:param type:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    @classmethod
    def GetTypeCode(cls, type: Type) -> TypeCode:
        """:param type:
        :return:
        """
    @classmethod
    def IsAbstract(cls, type: Type) -> bool:
        """:param type:
        :return:
        """
    @classmethod
    def IsEnum(cls, type: Type) -> bool:
        """:param type:
        :return:
        """
    @classmethod
    def IsSealed(cls, type: Type) -> bool:
        """:param type:
        :return:
        """
    @classmethod
    def ReflectionOnly(cls, assm: Assembly) -> bool:
        """:param assm:
        :return:
        """
    def ToString(self) -> str:
        """:return:"""
