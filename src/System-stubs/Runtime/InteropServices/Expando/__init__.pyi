"""Automatically generated stubs for C# namespace: System.Runtime.InteropServices.Expando."""

from typing import overload

from System import Array
from System import Delegate
from System import Type
from System.Globalization import CultureInfo
from System.Reflection import Binder
from System.Reflection import BindingFlags
from System.Reflection import FieldInfo
from System.Reflection import IReflect
from System.Reflection import MemberInfo
from System.Reflection import MethodInfo
from System.Reflection import ParameterModifier
from System.Reflection import PropertyInfo

class IExpando(IReflect):
    """"""
    @property
    def UnderlyingSystemType(self) -> Type:
        """"""
    def AddField(self, name: str) -> FieldInfo:
        """"""
    def AddMethod(self, name: str, method: Delegate) -> MethodInfo:
        """"""
    def AddProperty(self, name: str) -> PropertyInfo:
        """"""
    def GetField(self, name: str, bindingAttr: BindingFlags) -> FieldInfo:
        """"""
    def GetFields(self, bindingAttr: BindingFlags) -> Array[FieldInfo]:
        """"""
    def GetMember(self, name: str, bindingAttr: BindingFlags) -> Array[MemberInfo]:
        """"""
    def GetMembers(self, bindingAttr: BindingFlags) -> Array[MemberInfo]:
        """"""
    @overload
    def GetMethod(self, name: str, bindingAttr: BindingFlags) -> MethodInfo:
        """"""
    @overload
    def GetMethod(
        self,
        name: str,
        bindingAttr: BindingFlags,
        binder: Binder,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> MethodInfo:
        """"""
    def GetMethods(self, bindingAttr: BindingFlags) -> Array[MethodInfo]:
        """"""
    def GetProperties(self, bindingAttr: BindingFlags) -> Array[PropertyInfo]:
        """"""
    @overload
    def GetProperty(self, name: str, bindingAttr: BindingFlags) -> PropertyInfo:
        """"""
    @overload
    def GetProperty(
        self,
        name: str,
        bindingAttr: BindingFlags,
        binder: Binder,
        returnType: Type,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> PropertyInfo:
        """"""
    def InvokeMember(
        self,
        name: str,
        invokeAttr: BindingFlags,
        binder: Binder,
        target: object,
        args: Array[object],
        modifiers: Array[ParameterModifier],
        culture: CultureInfo,
        namedParameters: Array[str],
    ) -> object:
        """"""
    def RemoveMember(self, m: MemberInfo) -> None:
        """"""
