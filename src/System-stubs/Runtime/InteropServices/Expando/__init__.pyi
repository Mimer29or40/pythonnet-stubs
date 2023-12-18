from __future__ import annotations

from typing import Protocol
from typing import Union

from System import Delegate
from System import String
from System import Void
from System.Reflection import FieldInfo
from System.Reflection import IReflect
from System.Reflection import MemberInfo
from System.Reflection import MethodInfo
from System.Reflection import PropertyInfo

# ---------- Types ---------- #

StringType = Union[str, String]
VoidType = Union[None, Void]

# No Classes

# No Structs

# ---------- Interfaces ---------- #

class IExpando(Protocol, IReflect):
    # No Properties

    # ---------- Methods ---------- #

    def AddField(self, name: StringType) -> FieldInfo: ...
    def AddMethod(self, name: StringType, method: Delegate) -> MethodInfo: ...
    def AddProperty(self, name: StringType) -> PropertyInfo: ...
    def RemoveMember(self, m: MemberInfo) -> VoidType: ...

    # No Events

# No Enums

# No Delegates

__all__ = [
    IExpando,
]
