from __future__ import annotations

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
        """

        :return:
        """
    def AddField(self, name: str) -> FieldInfo:
        """

        :param name:
        :return:
        """
    def AddMethod(self, name: str, method: Delegate) -> MethodInfo:
        """

        :param name:
        :param method:
        :return:
        """
    def AddProperty(self, name: str) -> PropertyInfo:
        """

        :param name:
        :return:
        """
    def GetField(self, name: str, bindingAttr: BindingFlags) -> FieldInfo:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    def GetFields(self, bindingAttr: BindingFlags) -> Array[FieldInfo]:
        """

        :param bindingAttr:
        :return:
        """
    def GetMember(self, name: str, bindingAttr: BindingFlags) -> Array[MemberInfo]:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    def GetMembers(self, bindingAttr: BindingFlags) -> Array[MemberInfo]:
        """

        :param bindingAttr:
        :return:
        """
    @overload
    def GetMethod(self, name: str, bindingAttr: BindingFlags) -> MethodInfo:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetMethod(
        self,
        name: str,
        bindingAttr: BindingFlags,
        binder: Binder,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> MethodInfo:
        """

        :param name:
        :param bindingAttr:
        :param binder:
        :param types:
        :param modifiers:
        :return:
        """
    def GetMethods(self, bindingAttr: BindingFlags) -> Array[MethodInfo]:
        """

        :param bindingAttr:
        :return:
        """
    def GetProperties(self, bindingAttr: BindingFlags) -> Array[PropertyInfo]:
        """

        :param bindingAttr:
        :return:
        """
    @overload
    def GetProperty(self, name: str, bindingAttr: BindingFlags) -> PropertyInfo:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
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
        """

        :param name:
        :param bindingAttr:
        :param binder:
        :param returnType:
        :param types:
        :param modifiers:
        :return:
        """
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
        """

        :param name:
        :param invokeAttr:
        :param binder:
        :param target:
        :param args:
        :param modifiers:
        :param culture:
        :param namedParameters:
        :return:
        """
    def RemoveMember(self, m: MemberInfo) -> None:
        """

        :param m:
        """
