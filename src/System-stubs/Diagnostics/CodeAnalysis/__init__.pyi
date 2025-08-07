"""Automatically generated stubs for C# namespace: System.Diagnostics.CodeAnalysis."""

from System import Attribute
from System import Guid
from System import IntPtr
from System import Type
from System import UInt32
from System.Runtime.InteropServices import _Attribute

class ExcludeFromCodeCoverageAttribute(Attribute, _Attribute):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def TypeId(self) -> object:
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

class SuppressMessageAttribute(Attribute, _Attribute):
    """"""
    def __init__(self, category: str, checkId: str) -> None:
        """"""
    @property
    def Category(self) -> str:
        """"""
    @property
    def CheckId(self) -> str:
        """"""
    @property
    def Justification(self) -> str:
        """"""
    @Justification.setter
    def Justification(self, value: str) -> None: ...
    @property
    def MessageId(self) -> str:
        """"""
    @MessageId.setter
    def MessageId(self, value: str) -> None: ...
    @property
    def Scope(self) -> str:
        """"""
    @Scope.setter
    def Scope(self, value: str) -> None: ...
    @property
    def Target(self) -> str:
        """"""
    @Target.setter
    def Target(self, value: str) -> None: ...
    @property
    def TypeId(self) -> object:
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
