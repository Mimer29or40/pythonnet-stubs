"""Automatically generated stubs for C# namespace: System.Windows.Markup."""

from typing import overload

from System import Attribute
from System import Guid
from System import IntPtr
from System import Type
from System import UInt32
from System.Runtime.InteropServices import _Attribute

class ValueSerializerAttribute(Attribute, _Attribute):
    """"""
    @overload
    def __init__(self, valueSerializerType: Type) -> None:
        """"""
    @overload
    def __init__(self, valueSerializerTypeName: str) -> None:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
    @property
    def ValueSerializerType(self) -> Type:
        """"""
    @property
    def ValueSerializerTypeName(self) -> str:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """"""
    def GetTypeInfoCount(self, pcTInfo: UInt32) -> tuple[None, UInt32]:
        """"""
    def Invoke(
        self,
        dispIdMember: int,
        riid: Guid,
        lcid: int,
        wFlags: int,
        pDispParams: IntPtr,
        pVarResult: IntPtr,
        pExcepInfo: IntPtr,
        puArgErr: IntPtr,
    ) -> None:
        """"""
    def IsDefaultAttribute(self) -> bool:
        """"""
    def Match(self, obj: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
