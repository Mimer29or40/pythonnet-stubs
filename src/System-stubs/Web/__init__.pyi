"""Automatically generated stubs for C# namespace: System.Web."""

from typing import overload

from System import Enum
from System import Guid
from System import IntPtr
from System import Type
from System import UInt32
from System.Runtime.InteropServices import _Attribute
from System.Security import CodeAccessPermission
from System.Security import IPermission
from System.Security import ISecurityEncodable
from System.Security import IStackWalk
from System.Security import SecurityElement
from System.Security.Permissions import CodeAccessSecurityAttribute
from System.Security.Permissions import IUnrestrictedPermission
from System.Security.Permissions import PermissionState
from System.Security.Permissions import SecurityAction

class AspNetHostingPermission(
    CodeAccessPermission, IUnrestrictedPermission, IPermission, ISecurityEncodable, IStackWalk
):
    """"""
    @overload
    def __init__(self, state: PermissionState) -> None:
        """"""
    @overload
    def __init__(self, level: AspNetHostingPermissionLevel) -> None:
        """"""
    @property
    def Level(self) -> AspNetHostingPermissionLevel:
        """"""
    @Level.setter
    def Level(self, value: AspNetHostingPermissionLevel) -> None: ...
    def Assert(self) -> None:
        """"""
    def Copy(self) -> IPermission:
        """"""
    def Demand(self) -> None:
        """"""
    def Deny(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def FromXml(self, securityElement: SecurityElement) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Intersect(self, target: IPermission) -> IPermission:
        """"""
    def IsSubsetOf(self, target: IPermission) -> bool:
        """"""
    def IsUnrestricted(self) -> bool:
        """"""
    def PermitOnly(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def ToXml(self) -> SecurityElement:
        """"""
    def Union(self, target: IPermission) -> IPermission:
        """"""

class AspNetHostingPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    """"""
    def __init__(self, action: SecurityAction) -> None:
        """"""
    @property
    def Action(self) -> SecurityAction:
        """"""
    @Action.setter
    def Action(self, value: SecurityAction) -> None: ...
    @property
    def Level(self) -> AspNetHostingPermissionLevel:
        """"""
    @Level.setter
    def Level(self, value: AspNetHostingPermissionLevel) -> None: ...
    @property
    def TypeId(self) -> object:
        """"""
    @property
    def Unrestricted(self) -> bool:
        """"""
    @Unrestricted.setter
    def Unrestricted(self, value: bool) -> None: ...
    def CreatePermission(self) -> IPermission:
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

class AspNetHostingPermissionLevel(Enum):
    """"""

    _None: AspNetHostingPermissionLevel = ...
    """"""
    Minimal: AspNetHostingPermissionLevel = ...
    """"""
    Low: AspNetHostingPermissionLevel = ...
    """"""
    Medium: AspNetHostingPermissionLevel = ...
    """"""
    High: AspNetHostingPermissionLevel = ...
    """"""
    Unrestricted: AspNetHostingPermissionLevel = ...
    """"""
