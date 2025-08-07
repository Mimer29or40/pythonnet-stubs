"""Automatically generated stubs for C# namespace: Microsoft.Reflection."""

from abc import ABC

from System import Object
from System import Type
from System import TypeCode
from System.Reflection import Assembly

class ReflectionExtensions(ABC, Object):
    """"""
    @classmethod
    def Assembly(cls, type: Type) -> Assembly:
        """"""
    @classmethod
    def BaseType(cls, type: Type) -> Type:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def GetTypeCode(cls, type: Type) -> TypeCode:
        """"""
    @classmethod
    def IsAbstract(cls, type: Type) -> bool:
        """"""
    @classmethod
    def IsEnum(cls, type: Type) -> bool:
        """"""
    @classmethod
    def IsSealed(cls, type: Type) -> bool:
        """"""
    @classmethod
    def ReflectionOnly(cls, assm: Assembly) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
