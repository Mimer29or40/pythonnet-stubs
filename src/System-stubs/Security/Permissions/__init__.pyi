from __future__ import annotations

from abc import ABC
from typing import ClassVar
from typing import Final
from typing import Iterator
from typing import Tuple
from typing import overload

from System import Array
from System import Attribute
from System import Enum
from System import Guid
from System import IntPtr
from System import Object
from System import Type
from System import Version
from System.Collections import ArrayList
from System.Collections import ICollection
from System.Collections import IEnumerable
from System.Collections import IEnumerator
from System.Runtime.InteropServices import _Attribute
from System.Security import CodeAccessPermission
from System.Security import IPermission
from System.Security import ISecurityEncodable
from System.Security import IStackWalk
from System.Security import PermissionSet
from System.Security import SecurityElement
from System.Security import SecurityZone
from System.Security.AccessControl import AccessControlActions
from System.Security.Cryptography import CspParameters
from System.Security.Cryptography.X509Certificates import X509Certificate
from System.Security.Util import StringExpressionSet

class BuiltInPermissionFlag(Enum):
    """"""

    EnvironmentPermission: BuiltInPermissionFlag = ...
    """"""
    FileDialogPermission: BuiltInPermissionFlag = ...
    """"""
    FileIOPermission: BuiltInPermissionFlag = ...
    """"""
    IsolatedStorageFilePermission: BuiltInPermissionFlag = ...
    """"""
    ReflectionPermission: BuiltInPermissionFlag = ...
    """"""
    RegistryPermission: BuiltInPermissionFlag = ...
    """"""
    SecurityPermission: BuiltInPermissionFlag = ...
    """"""
    UIPermission: BuiltInPermissionFlag = ...
    """"""
    PrincipalPermission: BuiltInPermissionFlag = ...
    """"""
    PublisherIdentityPermission: BuiltInPermissionFlag = ...
    """"""
    SiteIdentityPermission: BuiltInPermissionFlag = ...
    """"""
    StrongNameIdentityPermission: BuiltInPermissionFlag = ...
    """"""
    UrlIdentityPermission: BuiltInPermissionFlag = ...
    """"""
    ZoneIdentityPermission: BuiltInPermissionFlag = ...
    """"""
    KeyContainerPermission: BuiltInPermissionFlag = ...
    """"""

class BuiltInPermissionIndex(ABC, Object):
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
    def ToString(self) -> str:
        """

        :return:
        """

class CodeAccessSecurityAttribute(ABC, SecurityAttribute, _Attribute):
    """"""

    @property
    def Action(self) -> SecurityAction:
        """

        :return:
        """
    @Action.setter
    def Action(self, value: SecurityAction) -> None: ...
    @property
    def TypeId(self) -> object:
        """

        :return:
        """
    @property
    def Unrestricted(self) -> bool:
        """

        :return:
        """
    @Unrestricted.setter
    def Unrestricted(self, value: bool) -> None: ...
    def CreatePermission(self) -> IPermission:
        """

        :return:
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
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """

        :return:
        """
    def Match(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class EnvironmentPermission(
    CodeAccessPermission,
    IBuiltInPermission,
    IUnrestrictedPermission,
    IPermission,
    ISecurityEncodable,
    IStackWalk,
):
    """"""

    @overload
    def __init__(self, state: PermissionState):
        """

        :param state:
        """
    @overload
    def __init__(self, flag: EnvironmentPermissionAccess, pathList: str):
        """

        :param flag:
        :param pathList:
        """
    def AddPathList(self, flag: EnvironmentPermissionAccess, pathList: str) -> None:
        """

        :param flag:
        :param pathList:
        """
    def Assert(self) -> None:
        """"""
    def Copy(self) -> IPermission:
        """

        :return:
        """
    @overload
    def Demand(self) -> None:
        """"""
    @overload
    def Demand(self) -> None:
        """"""
    def Deny(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def FromXml(self, e: SecurityElement) -> None:
        """

        :param e:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetPathList(self, flag: EnvironmentPermissionAccess) -> str:
        """

        :param flag:
        :return:
        """
    def GetTokenIndex(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def Intersect(self, target: IPermission) -> IPermission:
        """

        :param target:
        :return:
        """
    def IsSubsetOf(self, target: IPermission) -> bool:
        """

        :param target:
        :return:
        """
    def IsUnrestricted(self) -> bool:
        """

        :return:
        """
    def PermitOnly(self) -> None:
        """"""
    def SetPathList(self, flag: EnvironmentPermissionAccess, pathList: str) -> None:
        """

        :param flag:
        :param pathList:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def ToXml(self) -> SecurityElement:
        """

        :return:
        """
    def Union(self, target: IPermission) -> IPermission:
        """

        :param target:
        :return:
        """

class EnvironmentPermissionAccess(Enum):
    """"""

    NoAccess: EnvironmentPermissionAccess = ...
    """"""
    Read: EnvironmentPermissionAccess = ...
    """"""
    Write: EnvironmentPermissionAccess = ...
    """"""
    AllAccess: EnvironmentPermissionAccess = ...
    """"""

class EnvironmentPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    """"""

    def __init__(self, action: SecurityAction):
        """

        :param action:
        """
    @property
    def Action(self) -> SecurityAction:
        """

        :return:
        """
    @Action.setter
    def Action(self, value: SecurityAction) -> None: ...
    @property
    def All(self) -> str:
        """

        :return:
        """
    @All.setter
    def All(self, value: str) -> None: ...
    @property
    def Read(self) -> str:
        """

        :return:
        """
    @Read.setter
    def Read(self, value: str) -> None: ...
    @property
    def TypeId(self) -> object:
        """

        :return:
        """
    @property
    def Unrestricted(self) -> bool:
        """

        :return:
        """
    @Unrestricted.setter
    def Unrestricted(self, value: bool) -> None: ...
    @property
    def Write(self) -> str:
        """

        :return:
        """
    @Write.setter
    def Write(self, value: str) -> None: ...
    def CreatePermission(self) -> IPermission:
        """

        :return:
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
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """

        :return:
        """
    def Match(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class EnvironmentStringExpressionSet(StringExpressionSet):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, str: str):
        """

        :param str:
        """
    @overload
    def AddExpressions(self, str: str) -> None:
        """

        :param str:
        """
    @overload
    def AddExpressions(self, exprArrayList: ArrayList, checkForDuplicates: bool) -> None:
        """

        :param exprArrayList:
        :param checkForDuplicates:
        """
    @overload
    def AddExpressions(self, str: Array[str], checkForDuplicates: bool, needFullPath: bool) -> None:
        """

        :param str:
        :param checkForDuplicates:
        :param needFullPath:
        """
    def Copy(self) -> StringExpressionSet:
        """

        :return:
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
    def Intersect(self, ses: StringExpressionSet) -> StringExpressionSet:
        """

        :param ses:
        :return:
        """
    def IsEmpty(self) -> bool:
        """

        :return:
        """
    def IsSubsetOf(self, ses: StringExpressionSet) -> bool:
        """

        :param ses:
        :return:
        """
    def IsSubsetOfPathDiscovery(self, ses: StringExpressionSet) -> bool:
        """

        :param ses:
        :return:
        """
    def SetThrowOnRelative(self, throwOnRelative: bool) -> None:
        """

        :param throwOnRelative:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Union(self, ses: StringExpressionSet) -> StringExpressionSet:
        """

        :param ses:
        :return:
        """
    def UnsafeToString(self) -> str:
        """

        :return:
        """
    def UnsafeToStringArray(self) -> Array[str]:
        """

        :return:
        """

class FileDialogPermission(
    CodeAccessPermission,
    IBuiltInPermission,
    IUnrestrictedPermission,
    IPermission,
    ISecurityEncodable,
    IStackWalk,
):
    """"""

    @overload
    def __init__(self, access: FileDialogPermissionAccess):
        """

        :param access:
        """
    @overload
    def __init__(self, state: PermissionState):
        """

        :param state:
        """
    @property
    def Access(self) -> FileDialogPermissionAccess:
        """

        :return:
        """
    @Access.setter
    def Access(self, value: FileDialogPermissionAccess) -> None: ...
    def Assert(self) -> None:
        """"""
    def Copy(self) -> IPermission:
        """

        :return:
        """
    @overload
    def Demand(self) -> None:
        """"""
    @overload
    def Demand(self) -> None:
        """"""
    def Deny(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def FromXml(self, e: SecurityElement) -> None:
        """

        :param e:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetTokenIndex(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def Intersect(self, target: IPermission) -> IPermission:
        """

        :param target:
        :return:
        """
    def IsSubsetOf(self, target: IPermission) -> bool:
        """

        :param target:
        :return:
        """
    def IsUnrestricted(self) -> bool:
        """

        :return:
        """
    def PermitOnly(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """
    def ToXml(self) -> SecurityElement:
        """

        :return:
        """
    def Union(self, target: IPermission) -> IPermission:
        """

        :param target:
        :return:
        """

class FileDialogPermissionAccess(Enum):
    """"""

    _None: FileDialogPermissionAccess = ...
    """"""
    Open: FileDialogPermissionAccess = ...
    """"""
    Save: FileDialogPermissionAccess = ...
    """"""
    OpenSave: FileDialogPermissionAccess = ...
    """"""

class FileDialogPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    """"""

    def __init__(self, action: SecurityAction):
        """

        :param action:
        """
    @property
    def Action(self) -> SecurityAction:
        """

        :return:
        """
    @Action.setter
    def Action(self, value: SecurityAction) -> None: ...
    @property
    def Open(self) -> bool:
        """

        :return:
        """
    @Open.setter
    def Open(self, value: bool) -> None: ...
    @property
    def Save(self) -> bool:
        """

        :return:
        """
    @Save.setter
    def Save(self, value: bool) -> None: ...
    @property
    def TypeId(self) -> object:
        """

        :return:
        """
    @property
    def Unrestricted(self) -> bool:
        """

        :return:
        """
    @Unrestricted.setter
    def Unrestricted(self, value: bool) -> None: ...
    def CreatePermission(self) -> IPermission:
        """

        :return:
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
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """

        :return:
        """
    def Match(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class FileIOAccess(Object):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, pathDiscovery: bool):
        """

        :param pathDiscovery:
        """
    @overload
    def __init__(self, value: str):
        """

        :param value:
        """
    @overload
    def __init__(self, allFiles: bool, allLocalFiles: bool, pathDiscovery: bool):
        """

        :param allFiles:
        :param allLocalFiles:
        :param pathDiscovery:
        """
    @overload
    def __init__(
        self, set: StringExpressionSet, allFiles: bool, allLocalFiles: bool, pathDiscovery: bool
    ):
        """

        :param set:
        :param allFiles:
        :param allLocalFiles:
        :param pathDiscovery:
        """
    @property
    def AllFiles(self) -> bool:
        """

        :return:
        """
    @AllFiles.setter
    def AllFiles(self, value: bool) -> None: ...
    @property
    def AllLocalFiles(self) -> bool:
        """

        :return:
        """
    @AllLocalFiles.setter
    def AllLocalFiles(self, value: bool) -> None: ...
    @property
    def PathDiscovery(self) -> bool:
        """

        :return:
        """
    @PathDiscovery.setter
    def PathDiscovery(self, value: bool) -> None: ...
    def AddExpressions(self, values: ArrayList, checkForDuplicates: bool) -> None:
        """

        :param values:
        :param checkForDuplicates:
        """
    def Copy(self) -> FileIOAccess:
        """

        :return:
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
    def Intersect(self, operand: FileIOAccess) -> FileIOAccess:
        """

        :param operand:
        :return:
        """
    def IsEmpty(self) -> bool:
        """

        :return:
        """
    def IsSubsetOf(self, operand: FileIOAccess) -> bool:
        """

        :param operand:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def ToStringArray(self) -> Array[str]:
        """

        :return:
        """
    def Union(self, operand: FileIOAccess) -> FileIOAccess:
        """

        :param operand:
        :return:
        """

class FileIOPermission(
    CodeAccessPermission,
    IBuiltInPermission,
    IUnrestrictedPermission,
    IPermission,
    ISecurityEncodable,
    IStackWalk,
):
    """"""

    @overload
    def __init__(self, state: PermissionState):
        """

        :param state:
        """
    @overload
    def __init__(self, access: FileIOPermissionAccess, pathList: Array[str]):
        """

        :param access:
        :param pathList:
        """
    @overload
    def __init__(self, access: FileIOPermissionAccess, path: str):
        """

        :param access:
        :param path:
        """
    @overload
    def __init__(
        self, access: FileIOPermissionAccess, control: AccessControlActions, pathList: Array[str]
    ):
        """

        :param access:
        :param control:
        :param pathList:
        """
    @overload
    def __init__(self, access: FileIOPermissionAccess, control: AccessControlActions, path: str):
        """

        :param access:
        :param control:
        :param path:
        """
    @property
    def AllFiles(self) -> FileIOPermissionAccess:
        """

        :return:
        """
    @AllFiles.setter
    def AllFiles(self, value: FileIOPermissionAccess) -> None: ...
    @property
    def AllLocalFiles(self) -> FileIOPermissionAccess:
        """

        :return:
        """
    @AllLocalFiles.setter
    def AllLocalFiles(self, value: FileIOPermissionAccess) -> None: ...
    @overload
    def AddPathList(self, access: FileIOPermissionAccess, pathList: Array[str]) -> None:
        """

        :param access:
        :param pathList:
        """
    @overload
    def AddPathList(self, access: FileIOPermissionAccess, path: str) -> None:
        """

        :param access:
        :param path:
        """
    def Assert(self) -> None:
        """"""
    def Copy(self) -> IPermission:
        """

        :return:
        """
    @overload
    def Demand(self) -> None:
        """"""
    @overload
    def Demand(self) -> None:
        """"""
    def Deny(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def FromXml(self, e: SecurityElement) -> None:
        """

        :param e:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetPathList(self, access: FileIOPermissionAccess) -> Array[str]:
        """

        :param access:
        :return:
        """
    def GetTokenIndex(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def Intersect(self, target: IPermission) -> IPermission:
        """

        :param target:
        :return:
        """
    def IsSubsetOf(self, target: IPermission) -> bool:
        """

        :param target:
        :return:
        """
    def IsUnrestricted(self) -> bool:
        """

        :return:
        """
    def PermitOnly(self) -> None:
        """"""
    @overload
    def SetPathList(self, access: FileIOPermissionAccess, pathList: Array[str]) -> None:
        """

        :param access:
        :param pathList:
        """
    @overload
    def SetPathList(self, access: FileIOPermissionAccess, path: str) -> None:
        """

        :param access:
        :param path:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def ToXml(self) -> SecurityElement:
        """

        :return:
        """
    def Union(self, target: IPermission) -> IPermission:
        """

        :param target:
        :return:
        """

class FileIOPermissionAccess(Enum):
    """"""

    NoAccess: FileIOPermissionAccess = ...
    """"""
    Read: FileIOPermissionAccess = ...
    """"""
    Write: FileIOPermissionAccess = ...
    """"""
    Append: FileIOPermissionAccess = ...
    """"""
    PathDiscovery: FileIOPermissionAccess = ...
    """"""
    AllAccess: FileIOPermissionAccess = ...
    """"""

class FileIOPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    """"""

    def __init__(self, action: SecurityAction):
        """

        :param action:
        """
    @property
    def Action(self) -> SecurityAction:
        """

        :return:
        """
    @Action.setter
    def Action(self, value: SecurityAction) -> None: ...
    @property
    def All(self) -> str:
        """

        :return:
        """
    @All.setter
    def All(self, value: str) -> None: ...
    @property
    def AllFiles(self) -> FileIOPermissionAccess:
        """

        :return:
        """
    @AllFiles.setter
    def AllFiles(self, value: FileIOPermissionAccess) -> None: ...
    @property
    def AllLocalFiles(self) -> FileIOPermissionAccess:
        """

        :return:
        """
    @AllLocalFiles.setter
    def AllLocalFiles(self, value: FileIOPermissionAccess) -> None: ...
    @property
    def Append(self) -> str:
        """

        :return:
        """
    @Append.setter
    def Append(self, value: str) -> None: ...
    @property
    def ChangeAccessControl(self) -> str:
        """

        :return:
        """
    @ChangeAccessControl.setter
    def ChangeAccessControl(self, value: str) -> None: ...
    @property
    def PathDiscovery(self) -> str:
        """

        :return:
        """
    @PathDiscovery.setter
    def PathDiscovery(self, value: str) -> None: ...
    @property
    def Read(self) -> str:
        """

        :return:
        """
    @Read.setter
    def Read(self, value: str) -> None: ...
    @property
    def TypeId(self) -> object:
        """

        :return:
        """
    @property
    def Unrestricted(self) -> bool:
        """

        :return:
        """
    @Unrestricted.setter
    def Unrestricted(self, value: bool) -> None: ...
    @property
    def ViewAccessControl(self) -> str:
        """

        :return:
        """
    @ViewAccessControl.setter
    def ViewAccessControl(self, value: str) -> None: ...
    @property
    def ViewAndModify(self) -> str:
        """

        :return:
        """
    @ViewAndModify.setter
    def ViewAndModify(self, value: str) -> None: ...
    @property
    def Write(self) -> str:
        """

        :return:
        """
    @Write.setter
    def Write(self, value: str) -> None: ...
    def CreatePermission(self) -> IPermission:
        """

        :return:
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
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """

        :return:
        """
    def Match(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class GacIdentityPermission(
    CodeAccessPermission, IBuiltInPermission, IPermission, ISecurityEncodable, IStackWalk
):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, state: PermissionState):
        """

        :param state:
        """
    def Assert(self) -> None:
        """"""
    def Copy(self) -> IPermission:
        """

        :return:
        """
    @overload
    def Demand(self) -> None:
        """"""
    @overload
    def Demand(self) -> None:
        """"""
    def Deny(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def FromXml(self, e: SecurityElement) -> None:
        """

        :param e:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetTokenIndex(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def Intersect(self, target: IPermission) -> IPermission:
        """

        :param target:
        :return:
        """
    def IsSubsetOf(self, target: IPermission) -> bool:
        """

        :param target:
        :return:
        """
    def PermitOnly(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """
    def ToXml(self) -> SecurityElement:
        """

        :return:
        """
    def Union(self, target: IPermission) -> IPermission:
        """

        :param target:
        :return:
        """

class GacIdentityPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    """"""

    def __init__(self, action: SecurityAction):
        """

        :param action:
        """
    @property
    def Action(self) -> SecurityAction:
        """

        :return:
        """
    @Action.setter
    def Action(self, value: SecurityAction) -> None: ...
    @property
    def TypeId(self) -> object:
        """

        :return:
        """
    @property
    def Unrestricted(self) -> bool:
        """

        :return:
        """
    @Unrestricted.setter
    def Unrestricted(self, value: bool) -> None: ...
    def CreatePermission(self) -> IPermission:
        """

        :return:
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
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """

        :return:
        """
    def Match(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class HostProtectionAttribute(CodeAccessSecurityAttribute, _Attribute):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, action: SecurityAction):
        """

        :param action:
        """
    @property
    def Action(self) -> SecurityAction:
        """

        :return:
        """
    @Action.setter
    def Action(self, value: SecurityAction) -> None: ...
    @property
    def ExternalProcessMgmt(self) -> bool:
        """

        :return:
        """
    @ExternalProcessMgmt.setter
    def ExternalProcessMgmt(self, value: bool) -> None: ...
    @property
    def ExternalThreading(self) -> bool:
        """

        :return:
        """
    @ExternalThreading.setter
    def ExternalThreading(self, value: bool) -> None: ...
    @property
    def MayLeakOnAbort(self) -> bool:
        """

        :return:
        """
    @MayLeakOnAbort.setter
    def MayLeakOnAbort(self, value: bool) -> None: ...
    @property
    def Resources(self) -> HostProtectionResource:
        """

        :return:
        """
    @Resources.setter
    def Resources(self, value: HostProtectionResource) -> None: ...
    @property
    def SecurityInfrastructure(self) -> bool:
        """

        :return:
        """
    @SecurityInfrastructure.setter
    def SecurityInfrastructure(self, value: bool) -> None: ...
    @property
    def SelfAffectingProcessMgmt(self) -> bool:
        """

        :return:
        """
    @SelfAffectingProcessMgmt.setter
    def SelfAffectingProcessMgmt(self, value: bool) -> None: ...
    @property
    def SelfAffectingThreading(self) -> bool:
        """

        :return:
        """
    @SelfAffectingThreading.setter
    def SelfAffectingThreading(self, value: bool) -> None: ...
    @property
    def SharedState(self) -> bool:
        """

        :return:
        """
    @SharedState.setter
    def SharedState(self, value: bool) -> None: ...
    @property
    def Synchronization(self) -> bool:
        """

        :return:
        """
    @Synchronization.setter
    def Synchronization(self, value: bool) -> None: ...
    @property
    def TypeId(self) -> object:
        """

        :return:
        """
    @property
    def UI(self) -> bool:
        """

        :return:
        """
    @UI.setter
    def UI(self, value: bool) -> None: ...
    @property
    def Unrestricted(self) -> bool:
        """

        :return:
        """
    @Unrestricted.setter
    def Unrestricted(self, value: bool) -> None: ...
    def CreatePermission(self) -> IPermission:
        """

        :return:
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
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """

        :return:
        """
    def Match(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class HostProtectionPermission(
    CodeAccessPermission,
    IBuiltInPermission,
    IUnrestrictedPermission,
    IPermission,
    ISecurityEncodable,
    IStackWalk,
):
    """"""

    @overload
    def __init__(self, resources: HostProtectionResource):
        """

        :param resources:
        """
    @overload
    def __init__(self, state: PermissionState):
        """

        :param state:
        """
    @property
    def Resources(self) -> HostProtectionResource:
        """

        :return:
        """
    @Resources.setter
    def Resources(self, value: HostProtectionResource) -> None: ...
    def Assert(self) -> None:
        """"""
    def Copy(self) -> IPermission:
        """

        :return:
        """
    @overload
    def Demand(self) -> None:
        """"""
    @overload
    def Demand(self) -> None:
        """"""
    def Deny(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def FromXml(self, e: SecurityElement) -> None:
        """

        :param e:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetTokenIndex(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def Intersect(self, target: IPermission) -> IPermission:
        """

        :param target:
        :return:
        """
    def IsSubsetOf(self, target: IPermission) -> bool:
        """

        :param target:
        :return:
        """
    def IsUnrestricted(self) -> bool:
        """

        :return:
        """
    def PermitOnly(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """
    def ToXml(self) -> SecurityElement:
        """

        :return:
        """
    def Union(self, target: IPermission) -> IPermission:
        """

        :param target:
        :return:
        """

class HostProtectionResource(Enum):
    """"""

    _None: HostProtectionResource = ...
    """"""
    Synchronization: HostProtectionResource = ...
    """"""
    SharedState: HostProtectionResource = ...
    """"""
    ExternalProcessMgmt: HostProtectionResource = ...
    """"""
    SelfAffectingProcessMgmt: HostProtectionResource = ...
    """"""
    ExternalThreading: HostProtectionResource = ...
    """"""
    SelfAffectingThreading: HostProtectionResource = ...
    """"""
    SecurityInfrastructure: HostProtectionResource = ...
    """"""
    UI: HostProtectionResource = ...
    """"""
    MayLeakOnAbort: HostProtectionResource = ...
    """"""
    All: HostProtectionResource = ...
    """"""

class IBuiltInPermission:
    """"""

    def GetTokenIndex(self) -> int:
        """

        :return:
        """

class IDRole(Object):
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
    def ToString(self) -> str:
        """

        :return:
        """

class IUnrestrictedPermission:
    """"""

    def IsUnrestricted(self) -> bool:
        """

        :return:
        """

class IsolatedStorageContainment(Enum):
    """"""

    _None: IsolatedStorageContainment = ...
    """"""
    DomainIsolationByUser: IsolatedStorageContainment = ...
    """"""
    ApplicationIsolationByUser: IsolatedStorageContainment = ...
    """"""
    AssemblyIsolationByUser: IsolatedStorageContainment = ...
    """"""
    DomainIsolationByMachine: IsolatedStorageContainment = ...
    """"""
    AssemblyIsolationByMachine: IsolatedStorageContainment = ...
    """"""
    ApplicationIsolationByMachine: IsolatedStorageContainment = ...
    """"""
    DomainIsolationByRoamingUser: IsolatedStorageContainment = ...
    """"""
    AssemblyIsolationByRoamingUser: IsolatedStorageContainment = ...
    """"""
    ApplicationIsolationByRoamingUser: IsolatedStorageContainment = ...
    """"""
    AdministerIsolatedStorageByUser: IsolatedStorageContainment = ...
    """"""
    UnrestrictedIsolatedStorage: IsolatedStorageContainment = ...
    """"""

class IsolatedStorageFilePermission(
    IsolatedStoragePermission,
    IBuiltInPermission,
    IUnrestrictedPermission,
    IPermission,
    ISecurityEncodable,
    IStackWalk,
):
    """"""

    def __init__(self, state: PermissionState):
        """

        :param state:
        """
    @property
    def UsageAllowed(self) -> IsolatedStorageContainment:
        """

        :return:
        """
    @UsageAllowed.setter
    def UsageAllowed(self, value: IsolatedStorageContainment) -> None: ...
    @property
    def UserQuota(self) -> int:
        """

        :return:
        """
    @UserQuota.setter
    def UserQuota(self, value: int) -> None: ...
    def Assert(self) -> None:
        """"""
    def Copy(self) -> IPermission:
        """

        :return:
        """
    @overload
    def Demand(self) -> None:
        """"""
    @overload
    def Demand(self) -> None:
        """"""
    def Deny(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def FromXml(self, e: SecurityElement) -> None:
        """

        :param e:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetTokenIndex(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def Intersect(self, target: IPermission) -> IPermission:
        """

        :param target:
        :return:
        """
    def IsSubsetOf(self, target: IPermission) -> bool:
        """

        :param target:
        :return:
        """
    def IsUnrestricted(self) -> bool:
        """

        :return:
        """
    def PermitOnly(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """
    def ToXml(self) -> SecurityElement:
        """

        :return:
        """
    def Union(self, target: IPermission) -> IPermission:
        """

        :param target:
        :return:
        """

class IsolatedStorageFilePermissionAttribute(IsolatedStoragePermissionAttribute, _Attribute):
    """"""

    def __init__(self, action: SecurityAction):
        """

        :param action:
        """
    @property
    def Action(self) -> SecurityAction:
        """

        :return:
        """
    @Action.setter
    def Action(self, value: SecurityAction) -> None: ...
    @property
    def TypeId(self) -> object:
        """

        :return:
        """
    @property
    def Unrestricted(self) -> bool:
        """

        :return:
        """
    @Unrestricted.setter
    def Unrestricted(self, value: bool) -> None: ...
    @property
    def UsageAllowed(self) -> IsolatedStorageContainment:
        """

        :return:
        """
    @UsageAllowed.setter
    def UsageAllowed(self, value: IsolatedStorageContainment) -> None: ...
    @property
    def UserQuota(self) -> int:
        """

        :return:
        """
    @UserQuota.setter
    def UserQuota(self, value: int) -> None: ...
    def CreatePermission(self) -> IPermission:
        """

        :return:
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
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """

        :return:
        """
    def Match(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class IsolatedStoragePermission(
    ABC, CodeAccessPermission, IUnrestrictedPermission, IPermission, ISecurityEncodable, IStackWalk
):
    """"""

    @property
    def UsageAllowed(self) -> IsolatedStorageContainment:
        """

        :return:
        """
    @UsageAllowed.setter
    def UsageAllowed(self, value: IsolatedStorageContainment) -> None: ...
    @property
    def UserQuota(self) -> int:
        """

        :return:
        """
    @UserQuota.setter
    def UserQuota(self, value: int) -> None: ...
    def Assert(self) -> None:
        """"""
    def Copy(self) -> IPermission:
        """

        :return:
        """
    @overload
    def Demand(self) -> None:
        """"""
    @overload
    def Demand(self) -> None:
        """"""
    def Deny(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def FromXml(self, e: SecurityElement) -> None:
        """

        :param e:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def Intersect(self, target: IPermission) -> IPermission:
        """

        :param target:
        :return:
        """
    def IsSubsetOf(self, target: IPermission) -> bool:
        """

        :param target:
        :return:
        """
    def IsUnrestricted(self) -> bool:
        """

        :return:
        """
    def PermitOnly(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """
    def ToXml(self) -> SecurityElement:
        """

        :return:
        """
    def Union(self, target: IPermission) -> IPermission:
        """

        :param target:
        :return:
        """

class IsolatedStoragePermissionAttribute(ABC, CodeAccessSecurityAttribute, _Attribute):
    """"""

    @property
    def Action(self) -> SecurityAction:
        """

        :return:
        """
    @Action.setter
    def Action(self, value: SecurityAction) -> None: ...
    @property
    def TypeId(self) -> object:
        """

        :return:
        """
    @property
    def Unrestricted(self) -> bool:
        """

        :return:
        """
    @Unrestricted.setter
    def Unrestricted(self, value: bool) -> None: ...
    @property
    def UsageAllowed(self) -> IsolatedStorageContainment:
        """

        :return:
        """
    @UsageAllowed.setter
    def UsageAllowed(self, value: IsolatedStorageContainment) -> None: ...
    @property
    def UserQuota(self) -> int:
        """

        :return:
        """
    @UserQuota.setter
    def UserQuota(self, value: int) -> None: ...
    def CreatePermission(self) -> IPermission:
        """

        :return:
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
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """

        :return:
        """
    def Match(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class KeyContainerPermission(
    CodeAccessPermission,
    IBuiltInPermission,
    IUnrestrictedPermission,
    IPermission,
    ISecurityEncodable,
    IStackWalk,
):
    """"""

    @overload
    def __init__(self, flags: KeyContainerPermissionFlags):
        """

        :param flags:
        """
    @overload
    def __init__(self, state: PermissionState):
        """

        :param state:
        """
    @overload
    def __init__(
        self,
        flags: KeyContainerPermissionFlags,
        accessList: Array[KeyContainerPermissionAccessEntry],
    ):
        """

        :param flags:
        :param accessList:
        """
    @property
    def AccessEntries(self) -> KeyContainerPermissionAccessEntryCollection:
        """

        :return:
        """
    @property
    def Flags(self) -> KeyContainerPermissionFlags:
        """

        :return:
        """
    def Assert(self) -> None:
        """"""
    def Copy(self) -> IPermission:
        """

        :return:
        """
    @overload
    def Demand(self) -> None:
        """"""
    @overload
    def Demand(self) -> None:
        """"""
    def Deny(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def FromXml(self, e: SecurityElement) -> None:
        """

        :param e:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetTokenIndex(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def Intersect(self, target: IPermission) -> IPermission:
        """

        :param target:
        :return:
        """
    def IsSubsetOf(self, target: IPermission) -> bool:
        """

        :param target:
        :return:
        """
    def IsUnrestricted(self) -> bool:
        """

        :return:
        """
    def PermitOnly(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """
    def ToXml(self) -> SecurityElement:
        """

        :return:
        """
    def Union(self, target: IPermission) -> IPermission:
        """

        :param target:
        :return:
        """

class KeyContainerPermissionAccessEntry(Object):
    """"""

    @overload
    def __init__(self, parameters: CspParameters, flags: KeyContainerPermissionFlags):
        """

        :param parameters:
        :param flags:
        """
    @overload
    def __init__(self, keyContainerName: str, flags: KeyContainerPermissionFlags):
        """

        :param keyContainerName:
        :param flags:
        """
    @overload
    def __init__(
        self,
        keyStore: str,
        providerName: str,
        providerType: int,
        keyContainerName: str,
        keySpec: int,
        flags: KeyContainerPermissionFlags,
    ):
        """

        :param keyStore:
        :param providerName:
        :param providerType:
        :param keyContainerName:
        :param keySpec:
        :param flags:
        """
    @property
    def Flags(self) -> KeyContainerPermissionFlags:
        """

        :return:
        """
    @Flags.setter
    def Flags(self, value: KeyContainerPermissionFlags) -> None: ...
    @property
    def KeyContainerName(self) -> str:
        """

        :return:
        """
    @KeyContainerName.setter
    def KeyContainerName(self, value: str) -> None: ...
    @property
    def KeySpec(self) -> int:
        """

        :return:
        """
    @KeySpec.setter
    def KeySpec(self, value: int) -> None: ...
    @property
    def KeyStore(self) -> str:
        """

        :return:
        """
    @KeyStore.setter
    def KeyStore(self, value: str) -> None: ...
    @property
    def ProviderName(self) -> str:
        """

        :return:
        """
    @ProviderName.setter
    def ProviderName(self, value: str) -> None: ...
    @property
    def ProviderType(self) -> int:
        """

        :return:
        """
    @ProviderType.setter
    def ProviderType(self, value: int) -> None: ...
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
    def ToString(self) -> str:
        """

        :return:
        """

class KeyContainerPermissionAccessEntryCollection(Object, ICollection, IEnumerable):
    """"""

    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def IsSynchronized(self) -> bool:
        """

        :return:
        """
    @property
    def Item(self) -> KeyContainerPermissionAccessEntry:
        """

        :return:
        """
    @property
    def SyncRoot(self) -> object:
        """

        :return:
        """
    def Add(self, accessEntry: KeyContainerPermissionAccessEntry) -> int:
        """

        :param accessEntry:
        :return:
        """
    def Clear(self) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    @overload
    def CopyTo(self, array: Array[KeyContainerPermissionAccessEntry], index: int) -> None:
        """

        :param array:
        :param index:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

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
    def IndexOf(self, accessEntry: KeyContainerPermissionAccessEntry) -> int:
        """

        :param accessEntry:
        :return:
        """
    def Remove(self, accessEntry: KeyContainerPermissionAccessEntry) -> None:
        """

        :param accessEntry:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def __contains__(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    def __getitem__(self, index: int) -> KeyContainerPermissionAccessEntry:
        """

        :param index:
        :return:
        """
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    def __len__(self) -> int:
        """

        :return:
        """

class KeyContainerPermissionAccessEntryEnumerator(Object, IEnumerator):
    """"""

    @property
    def Current(self) -> object:
        """

        :return:
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
    def MoveNext(self) -> bool:
        """

        :return:
        """
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class KeyContainerPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    """"""

    def __init__(self, action: SecurityAction):
        """

        :param action:
        """
    @property
    def Action(self) -> SecurityAction:
        """

        :return:
        """
    @Action.setter
    def Action(self, value: SecurityAction) -> None: ...
    @property
    def Flags(self) -> KeyContainerPermissionFlags:
        """

        :return:
        """
    @Flags.setter
    def Flags(self, value: KeyContainerPermissionFlags) -> None: ...
    @property
    def KeyContainerName(self) -> str:
        """

        :return:
        """
    @KeyContainerName.setter
    def KeyContainerName(self, value: str) -> None: ...
    @property
    def KeySpec(self) -> int:
        """

        :return:
        """
    @KeySpec.setter
    def KeySpec(self, value: int) -> None: ...
    @property
    def KeyStore(self) -> str:
        """

        :return:
        """
    @KeyStore.setter
    def KeyStore(self, value: str) -> None: ...
    @property
    def ProviderName(self) -> str:
        """

        :return:
        """
    @ProviderName.setter
    def ProviderName(self, value: str) -> None: ...
    @property
    def ProviderType(self) -> int:
        """

        :return:
        """
    @ProviderType.setter
    def ProviderType(self, value: int) -> None: ...
    @property
    def TypeId(self) -> object:
        """

        :return:
        """
    @property
    def Unrestricted(self) -> bool:
        """

        :return:
        """
    @Unrestricted.setter
    def Unrestricted(self, value: bool) -> None: ...
    def CreatePermission(self) -> IPermission:
        """

        :return:
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
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """

        :return:
        """
    def Match(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class KeyContainerPermissionFlags(Enum):
    """"""

    NoFlags: KeyContainerPermissionFlags = ...
    """"""
    Create: KeyContainerPermissionFlags = ...
    """"""
    Open: KeyContainerPermissionFlags = ...
    """"""
    Delete: KeyContainerPermissionFlags = ...
    """"""
    Import: KeyContainerPermissionFlags = ...
    """"""
    Export: KeyContainerPermissionFlags = ...
    """"""
    Sign: KeyContainerPermissionFlags = ...
    """"""
    Decrypt: KeyContainerPermissionFlags = ...
    """"""
    ViewAcl: KeyContainerPermissionFlags = ...
    """"""
    ChangeAcl: KeyContainerPermissionFlags = ...
    """"""
    AllFlags: KeyContainerPermissionFlags = ...
    """"""

class PermissionSetAttribute(CodeAccessSecurityAttribute, _Attribute):
    """"""

    def __init__(self, action: SecurityAction):
        """

        :param action:
        """
    @property
    def Action(self) -> SecurityAction:
        """

        :return:
        """
    @Action.setter
    def Action(self, value: SecurityAction) -> None: ...
    @property
    def File(self) -> str:
        """

        :return:
        """
    @File.setter
    def File(self, value: str) -> None: ...
    @property
    def Hex(self) -> str:
        """

        :return:
        """
    @Hex.setter
    def Hex(self, value: str) -> None: ...
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def TypeId(self) -> object:
        """

        :return:
        """
    @property
    def UnicodeEncoded(self) -> bool:
        """

        :return:
        """
    @UnicodeEncoded.setter
    def UnicodeEncoded(self, value: bool) -> None: ...
    @property
    def Unrestricted(self) -> bool:
        """

        :return:
        """
    @Unrestricted.setter
    def Unrestricted(self, value: bool) -> None: ...
    @property
    def XML(self) -> str:
        """

        :return:
        """
    @XML.setter
    def XML(self, value: str) -> None: ...
    def CreatePermission(self) -> IPermission:
        """

        :return:
        """
    def CreatePermissionSet(self) -> PermissionSet:
        """

        :return:
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
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """

        :return:
        """
    def Match(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class PermissionState(Enum):
    """"""

    _None: PermissionState = ...
    """"""
    Unrestricted: PermissionState = ...
    """"""

class PrincipalPermission(
    Object, IBuiltInPermission, IUnrestrictedPermission, IPermission, ISecurityEncodable
):
    """"""

    @overload
    def __init__(self, state: PermissionState):
        """

        :param state:
        """
    @overload
    def __init__(self, name: str, role: str):
        """

        :param name:
        :param role:
        """
    @overload
    def __init__(self, name: str, role: str, isAuthenticated: bool):
        """

        :param name:
        :param role:
        :param isAuthenticated:
        """
    def Copy(self) -> IPermission:
        """

        :return:
        """
    def Demand(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def FromXml(self, e: SecurityElement) -> None:
        """

        :param e:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetTokenIndex(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def Intersect(self, target: IPermission) -> IPermission:
        """

        :param target:
        :return:
        """
    def IsSubsetOf(self, target: IPermission) -> bool:
        """

        :param target:
        :return:
        """
    def IsUnrestricted(self) -> bool:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def ToXml(self) -> SecurityElement:
        """

        :return:
        """
    def Union(self, target: IPermission) -> IPermission:
        """

        :param target:
        :return:
        """

class PrincipalPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    """"""

    def __init__(self, action: SecurityAction):
        """

        :param action:
        """
    @property
    def Action(self) -> SecurityAction:
        """

        :return:
        """
    @Action.setter
    def Action(self, value: SecurityAction) -> None: ...
    @property
    def Authenticated(self) -> bool:
        """

        :return:
        """
    @Authenticated.setter
    def Authenticated(self, value: bool) -> None: ...
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def Role(self) -> str:
        """

        :return:
        """
    @Role.setter
    def Role(self, value: str) -> None: ...
    @property
    def TypeId(self) -> object:
        """

        :return:
        """
    @property
    def Unrestricted(self) -> bool:
        """

        :return:
        """
    @Unrestricted.setter
    def Unrestricted(self, value: bool) -> None: ...
    def CreatePermission(self) -> IPermission:
        """

        :return:
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
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """

        :return:
        """
    def Match(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class PublisherIdentityPermission(
    CodeAccessPermission, IBuiltInPermission, IPermission, ISecurityEncodable, IStackWalk
):
    """"""

    @overload
    def __init__(self, certificate: X509Certificate):
        """

        :param certificate:
        """
    @overload
    def __init__(self, state: PermissionState):
        """

        :param state:
        """
    @property
    def Certificate(self) -> X509Certificate:
        """

        :return:
        """
    @Certificate.setter
    def Certificate(self, value: X509Certificate) -> None: ...
    def Assert(self) -> None:
        """"""
    def Copy(self) -> IPermission:
        """

        :return:
        """
    @overload
    def Demand(self) -> None:
        """"""
    @overload
    def Demand(self) -> None:
        """"""
    def Deny(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def FromXml(self, e: SecurityElement) -> None:
        """

        :param e:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetTokenIndex(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def Intersect(self, target: IPermission) -> IPermission:
        """

        :param target:
        :return:
        """
    def IsSubsetOf(self, target: IPermission) -> bool:
        """

        :param target:
        :return:
        """
    def PermitOnly(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """
    def ToXml(self) -> SecurityElement:
        """

        :return:
        """
    def Union(self, target: IPermission) -> IPermission:
        """

        :param target:
        :return:
        """

class PublisherIdentityPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    """"""

    def __init__(self, action: SecurityAction):
        """

        :param action:
        """
    @property
    def Action(self) -> SecurityAction:
        """

        :return:
        """
    @Action.setter
    def Action(self, value: SecurityAction) -> None: ...
    @property
    def CertFile(self) -> str:
        """

        :return:
        """
    @CertFile.setter
    def CertFile(self, value: str) -> None: ...
    @property
    def SignedFile(self) -> str:
        """

        :return:
        """
    @SignedFile.setter
    def SignedFile(self, value: str) -> None: ...
    @property
    def TypeId(self) -> object:
        """

        :return:
        """
    @property
    def Unrestricted(self) -> bool:
        """

        :return:
        """
    @Unrestricted.setter
    def Unrestricted(self, value: bool) -> None: ...
    @property
    def X509Certificate(self) -> str:
        """

        :return:
        """
    @X509Certificate.setter
    def X509Certificate(self, value: str) -> None: ...
    def CreatePermission(self) -> IPermission:
        """

        :return:
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
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """

        :return:
        """
    def Match(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class ReflectionPermission(
    CodeAccessPermission,
    IBuiltInPermission,
    IUnrestrictedPermission,
    IPermission,
    ISecurityEncodable,
    IStackWalk,
):
    """"""

    @overload
    def __init__(self, state: PermissionState):
        """

        :param state:
        """
    @overload
    def __init__(self, flag: ReflectionPermissionFlag):
        """

        :param flag:
        """
    @property
    def Flags(self) -> ReflectionPermissionFlag:
        """

        :return:
        """
    @Flags.setter
    def Flags(self, value: ReflectionPermissionFlag) -> None: ...
    def Assert(self) -> None:
        """"""
    def Copy(self) -> IPermission:
        """

        :return:
        """
    @overload
    def Demand(self) -> None:
        """"""
    @overload
    def Demand(self) -> None:
        """"""
    def Deny(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def FromXml(self, e: SecurityElement) -> None:
        """

        :param e:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetTokenIndex(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def Intersect(self, target: IPermission) -> IPermission:
        """

        :param target:
        :return:
        """
    def IsSubsetOf(self, target: IPermission) -> bool:
        """

        :param target:
        :return:
        """
    def IsUnrestricted(self) -> bool:
        """

        :return:
        """
    def PermitOnly(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """
    def ToXml(self) -> SecurityElement:
        """

        :return:
        """
    def Union(self, target: IPermission) -> IPermission:
        """

        :param target:
        :return:
        """

class ReflectionPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    """"""

    def __init__(self, action: SecurityAction):
        """

        :param action:
        """
    @property
    def Action(self) -> SecurityAction:
        """

        :return:
        """
    @Action.setter
    def Action(self, value: SecurityAction) -> None: ...
    @property
    def Flags(self) -> ReflectionPermissionFlag:
        """

        :return:
        """
    @Flags.setter
    def Flags(self, value: ReflectionPermissionFlag) -> None: ...
    @property
    def MemberAccess(self) -> bool:
        """

        :return:
        """
    @MemberAccess.setter
    def MemberAccess(self, value: bool) -> None: ...
    @property
    def ReflectionEmit(self) -> bool:
        """

        :return:
        """
    @ReflectionEmit.setter
    def ReflectionEmit(self, value: bool) -> None: ...
    @property
    def RestrictedMemberAccess(self) -> bool:
        """

        :return:
        """
    @RestrictedMemberAccess.setter
    def RestrictedMemberAccess(self, value: bool) -> None: ...
    @property
    def TypeId(self) -> object:
        """

        :return:
        """
    @property
    def TypeInformation(self) -> bool:
        """

        :return:
        """
    @TypeInformation.setter
    def TypeInformation(self, value: bool) -> None: ...
    @property
    def Unrestricted(self) -> bool:
        """

        :return:
        """
    @Unrestricted.setter
    def Unrestricted(self, value: bool) -> None: ...
    def CreatePermission(self) -> IPermission:
        """

        :return:
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
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """

        :return:
        """
    def Match(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class ReflectionPermissionFlag(Enum):
    """"""

    NoFlags: ReflectionPermissionFlag = ...
    """"""
    TypeInformation: ReflectionPermissionFlag = ...
    """"""
    MemberAccess: ReflectionPermissionFlag = ...
    """"""
    ReflectionEmit: ReflectionPermissionFlag = ...
    """"""
    AllFlags: ReflectionPermissionFlag = ...
    """"""
    RestrictedMemberAccess: ReflectionPermissionFlag = ...
    """"""

class RegistryPermission(
    CodeAccessPermission,
    IBuiltInPermission,
    IUnrestrictedPermission,
    IPermission,
    ISecurityEncodable,
    IStackWalk,
):
    """"""

    @overload
    def __init__(self, state: PermissionState):
        """

        :param state:
        """
    @overload
    def __init__(self, access: RegistryPermissionAccess, pathList: str):
        """

        :param access:
        :param pathList:
        """
    @overload
    def __init__(
        self, access: RegistryPermissionAccess, control: AccessControlActions, pathList: str
    ):
        """

        :param access:
        :param control:
        :param pathList:
        """
    @overload
    def AddPathList(self, access: RegistryPermissionAccess, pathList: str) -> None:
        """

        :param access:
        :param pathList:
        """
    @overload
    def AddPathList(
        self, access: RegistryPermissionAccess, control: AccessControlActions, pathList: str
    ) -> None:
        """

        :param access:
        :param control:
        :param pathList:
        """
    def Assert(self) -> None:
        """"""
    def Copy(self) -> IPermission:
        """

        :return:
        """
    @overload
    def Demand(self) -> None:
        """"""
    @overload
    def Demand(self) -> None:
        """"""
    def Deny(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def FromXml(self, e: SecurityElement) -> None:
        """

        :param e:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetPathList(self, access: RegistryPermissionAccess) -> str:
        """

        :param access:
        :return:
        """
    def GetTokenIndex(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def Intersect(self, target: IPermission) -> IPermission:
        """

        :param target:
        :return:
        """
    def IsSubsetOf(self, target: IPermission) -> bool:
        """

        :param target:
        :return:
        """
    def IsUnrestricted(self) -> bool:
        """

        :return:
        """
    def PermitOnly(self) -> None:
        """"""
    def SetPathList(self, access: RegistryPermissionAccess, pathList: str) -> None:
        """

        :param access:
        :param pathList:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def ToXml(self) -> SecurityElement:
        """

        :return:
        """
    def Union(self, target: IPermission) -> IPermission:
        """

        :param target:
        :return:
        """

class RegistryPermissionAccess(Enum):
    """"""

    NoAccess: RegistryPermissionAccess = ...
    """"""
    Read: RegistryPermissionAccess = ...
    """"""
    Write: RegistryPermissionAccess = ...
    """"""
    Create: RegistryPermissionAccess = ...
    """"""
    AllAccess: RegistryPermissionAccess = ...
    """"""

class RegistryPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    """"""

    def __init__(self, action: SecurityAction):
        """

        :param action:
        """
    @property
    def Action(self) -> SecurityAction:
        """

        :return:
        """
    @Action.setter
    def Action(self, value: SecurityAction) -> None: ...
    @property
    def All(self) -> str:
        """

        :return:
        """
    @All.setter
    def All(self, value: str) -> None: ...
    @property
    def ChangeAccessControl(self) -> str:
        """

        :return:
        """
    @ChangeAccessControl.setter
    def ChangeAccessControl(self, value: str) -> None: ...
    @property
    def Create(self) -> str:
        """

        :return:
        """
    @Create.setter
    def Create(self, value: str) -> None: ...
    @property
    def Read(self) -> str:
        """

        :return:
        """
    @Read.setter
    def Read(self, value: str) -> None: ...
    @property
    def TypeId(self) -> object:
        """

        :return:
        """
    @property
    def Unrestricted(self) -> bool:
        """

        :return:
        """
    @Unrestricted.setter
    def Unrestricted(self, value: bool) -> None: ...
    @property
    def ViewAccessControl(self) -> str:
        """

        :return:
        """
    @ViewAccessControl.setter
    def ViewAccessControl(self, value: str) -> None: ...
    @property
    def ViewAndModify(self) -> str:
        """

        :return:
        """
    @ViewAndModify.setter
    def ViewAndModify(self, value: str) -> None: ...
    @property
    def Write(self) -> str:
        """

        :return:
        """
    @Write.setter
    def Write(self, value: str) -> None: ...
    def CreatePermission(self) -> IPermission:
        """

        :return:
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
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """

        :return:
        """
    def Match(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class ResourcePermissionBase(
    ABC, CodeAccessPermission, IUnrestrictedPermission, IPermission, ISecurityEncodable, IStackWalk
):
    """"""

    Any: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Local: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    def Assert(self) -> None:
        """"""
    def Copy(self) -> IPermission:
        """

        :return:
        """
    @overload
    def Demand(self) -> None:
        """"""
    @overload
    def Demand(self) -> None:
        """"""
    def Deny(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def FromXml(self, e: SecurityElement) -> None:
        """

        :param e:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def Intersect(self, target: IPermission) -> IPermission:
        """

        :param target:
        :return:
        """
    def IsSubsetOf(self, target: IPermission) -> bool:
        """

        :param target:
        :return:
        """
    def IsUnrestricted(self) -> bool:
        """

        :return:
        """
    def PermitOnly(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """
    def ToXml(self) -> SecurityElement:
        """

        :return:
        """
    def Union(self, target: IPermission) -> IPermission:
        """

        :param target:
        :return:
        """

class ResourcePermissionBaseEntry(Object):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, permissionAccess: int, permissionAccessPath: Array[str]):
        """

        :param permissionAccess:
        :param permissionAccessPath:
        """
    @property
    def PermissionAccess(self) -> int:
        """

        :return:
        """
    @property
    def PermissionAccessPath(self) -> Array[str]:
        """

        :return:
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
    def ToString(self) -> str:
        """

        :return:
        """

class SecurityAction(Enum):
    """"""

    Demand: SecurityAction = ...
    """"""
    Assert: SecurityAction = ...
    """"""
    Deny: SecurityAction = ...
    """"""
    PermitOnly: SecurityAction = ...
    """"""
    LinkDemand: SecurityAction = ...
    """"""
    InheritanceDemand: SecurityAction = ...
    """"""
    RequestMinimum: SecurityAction = ...
    """"""
    RequestOptional: SecurityAction = ...
    """"""
    RequestRefuse: SecurityAction = ...
    """"""

class SecurityAttribute(ABC, Attribute, _Attribute):
    """"""

    @property
    def Action(self) -> SecurityAction:
        """

        :return:
        """
    @Action.setter
    def Action(self, value: SecurityAction) -> None: ...
    @property
    def TypeId(self) -> object:
        """

        :return:
        """
    @property
    def Unrestricted(self) -> bool:
        """

        :return:
        """
    @Unrestricted.setter
    def Unrestricted(self, value: bool) -> None: ...
    def CreatePermission(self) -> IPermission:
        """

        :return:
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
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """

        :return:
        """
    def Match(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class SecurityPermission(
    CodeAccessPermission,
    IBuiltInPermission,
    IUnrestrictedPermission,
    IPermission,
    ISecurityEncodable,
    IStackWalk,
):
    """"""

    @overload
    def __init__(self, state: PermissionState):
        """

        :param state:
        """
    @overload
    def __init__(self, flag: SecurityPermissionFlag):
        """

        :param flag:
        """
    @property
    def Flags(self) -> SecurityPermissionFlag:
        """

        :return:
        """
    @Flags.setter
    def Flags(self, value: SecurityPermissionFlag) -> None: ...
    def Assert(self) -> None:
        """"""
    def Copy(self) -> IPermission:
        """

        :return:
        """
    @overload
    def Demand(self) -> None:
        """"""
    @overload
    def Demand(self) -> None:
        """"""
    def Deny(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def FromXml(self, e: SecurityElement) -> None:
        """

        :param e:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetTokenIndex(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def Intersect(self, target: IPermission) -> IPermission:
        """

        :param target:
        :return:
        """
    def IsSubsetOf(self, target: IPermission) -> bool:
        """

        :param target:
        :return:
        """
    def IsUnrestricted(self) -> bool:
        """

        :return:
        """
    def PermitOnly(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """
    def ToXml(self) -> SecurityElement:
        """

        :return:
        """
    def Union(self, target: IPermission) -> IPermission:
        """

        :param target:
        :return:
        """

class SecurityPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    """"""

    def __init__(self, action: SecurityAction):
        """

        :param action:
        """
    @property
    def Action(self) -> SecurityAction:
        """

        :return:
        """
    @Action.setter
    def Action(self, value: SecurityAction) -> None: ...
    @property
    def Assertion(self) -> bool:
        """

        :return:
        """
    @Assertion.setter
    def Assertion(self, value: bool) -> None: ...
    @property
    def BindingRedirects(self) -> bool:
        """

        :return:
        """
    @BindingRedirects.setter
    def BindingRedirects(self, value: bool) -> None: ...
    @property
    def ControlAppDomain(self) -> bool:
        """

        :return:
        """
    @ControlAppDomain.setter
    def ControlAppDomain(self, value: bool) -> None: ...
    @property
    def ControlDomainPolicy(self) -> bool:
        """

        :return:
        """
    @ControlDomainPolicy.setter
    def ControlDomainPolicy(self, value: bool) -> None: ...
    @property
    def ControlEvidence(self) -> bool:
        """

        :return:
        """
    @ControlEvidence.setter
    def ControlEvidence(self, value: bool) -> None: ...
    @property
    def ControlPolicy(self) -> bool:
        """

        :return:
        """
    @ControlPolicy.setter
    def ControlPolicy(self, value: bool) -> None: ...
    @property
    def ControlPrincipal(self) -> bool:
        """

        :return:
        """
    @ControlPrincipal.setter
    def ControlPrincipal(self, value: bool) -> None: ...
    @property
    def ControlThread(self) -> bool:
        """

        :return:
        """
    @ControlThread.setter
    def ControlThread(self, value: bool) -> None: ...
    @property
    def Execution(self) -> bool:
        """

        :return:
        """
    @Execution.setter
    def Execution(self, value: bool) -> None: ...
    @property
    def Flags(self) -> SecurityPermissionFlag:
        """

        :return:
        """
    @Flags.setter
    def Flags(self, value: SecurityPermissionFlag) -> None: ...
    @property
    def Infrastructure(self) -> bool:
        """

        :return:
        """
    @Infrastructure.setter
    def Infrastructure(self, value: bool) -> None: ...
    @property
    def RemotingConfiguration(self) -> bool:
        """

        :return:
        """
    @RemotingConfiguration.setter
    def RemotingConfiguration(self, value: bool) -> None: ...
    @property
    def SerializationFormatter(self) -> bool:
        """

        :return:
        """
    @SerializationFormatter.setter
    def SerializationFormatter(self, value: bool) -> None: ...
    @property
    def SkipVerification(self) -> bool:
        """

        :return:
        """
    @SkipVerification.setter
    def SkipVerification(self, value: bool) -> None: ...
    @property
    def TypeId(self) -> object:
        """

        :return:
        """
    @property
    def UnmanagedCode(self) -> bool:
        """

        :return:
        """
    @UnmanagedCode.setter
    def UnmanagedCode(self, value: bool) -> None: ...
    @property
    def Unrestricted(self) -> bool:
        """

        :return:
        """
    @Unrestricted.setter
    def Unrestricted(self, value: bool) -> None: ...
    def CreatePermission(self) -> IPermission:
        """

        :return:
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
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """

        :return:
        """
    def Match(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class SecurityPermissionFlag(Enum):
    """"""

    NoFlags: SecurityPermissionFlag = ...
    """"""
    Assertion: SecurityPermissionFlag = ...
    """"""
    UnmanagedCode: SecurityPermissionFlag = ...
    """"""
    SkipVerification: SecurityPermissionFlag = ...
    """"""
    Execution: SecurityPermissionFlag = ...
    """"""
    ControlThread: SecurityPermissionFlag = ...
    """"""
    ControlEvidence: SecurityPermissionFlag = ...
    """"""
    ControlPolicy: SecurityPermissionFlag = ...
    """"""
    SerializationFormatter: SecurityPermissionFlag = ...
    """"""
    ControlDomainPolicy: SecurityPermissionFlag = ...
    """"""
    ControlPrincipal: SecurityPermissionFlag = ...
    """"""
    ControlAppDomain: SecurityPermissionFlag = ...
    """"""
    RemotingConfiguration: SecurityPermissionFlag = ...
    """"""
    Infrastructure: SecurityPermissionFlag = ...
    """"""
    BindingRedirects: SecurityPermissionFlag = ...
    """"""
    AllFlags: SecurityPermissionFlag = ...
    """"""

class SiteIdentityPermission(
    CodeAccessPermission, IBuiltInPermission, IPermission, ISecurityEncodable, IStackWalk
):
    """"""

    @overload
    def __init__(self, state: PermissionState):
        """

        :param state:
        """
    @overload
    def __init__(self, site: str):
        """

        :param site:
        """
    @property
    def Site(self) -> str:
        """

        :return:
        """
    @Site.setter
    def Site(self, value: str) -> None: ...
    def Assert(self) -> None:
        """"""
    def Copy(self) -> IPermission:
        """

        :return:
        """
    @overload
    def Demand(self) -> None:
        """"""
    @overload
    def Demand(self) -> None:
        """"""
    def Deny(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def FromXml(self, e: SecurityElement) -> None:
        """

        :param e:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetTokenIndex(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def Intersect(self, target: IPermission) -> IPermission:
        """

        :param target:
        :return:
        """
    def IsSubsetOf(self, target: IPermission) -> bool:
        """

        :param target:
        :return:
        """
    def PermitOnly(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """
    def ToXml(self) -> SecurityElement:
        """

        :return:
        """
    def Union(self, target: IPermission) -> IPermission:
        """

        :param target:
        :return:
        """

class SiteIdentityPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    """"""

    def __init__(self, action: SecurityAction):
        """

        :param action:
        """
    @property
    def Action(self) -> SecurityAction:
        """

        :return:
        """
    @Action.setter
    def Action(self, value: SecurityAction) -> None: ...
    @property
    def Site(self) -> str:
        """

        :return:
        """
    @Site.setter
    def Site(self, value: str) -> None: ...
    @property
    def TypeId(self) -> object:
        """

        :return:
        """
    @property
    def Unrestricted(self) -> bool:
        """

        :return:
        """
    @Unrestricted.setter
    def Unrestricted(self, value: bool) -> None: ...
    def CreatePermission(self) -> IPermission:
        """

        :return:
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
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """

        :return:
        """
    def Match(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class StorePermission(
    CodeAccessPermission, IUnrestrictedPermission, IPermission, ISecurityEncodable, IStackWalk
):
    """"""

    @overload
    def __init__(self, state: PermissionState):
        """

        :param state:
        """
    @overload
    def __init__(self, flag: StorePermissionFlags):
        """

        :param flag:
        """
    @property
    def Flags(self) -> StorePermissionFlags:
        """

        :return:
        """
    @Flags.setter
    def Flags(self, value: StorePermissionFlags) -> None: ...
    def Assert(self) -> None:
        """"""
    def Copy(self) -> IPermission:
        """

        :return:
        """
    @overload
    def Demand(self) -> None:
        """"""
    @overload
    def Demand(self) -> None:
        """"""
    def Deny(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def FromXml(self, e: SecurityElement) -> None:
        """

        :param e:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def Intersect(self, target: IPermission) -> IPermission:
        """

        :param target:
        :return:
        """
    def IsSubsetOf(self, target: IPermission) -> bool:
        """

        :param target:
        :return:
        """
    def IsUnrestricted(self) -> bool:
        """

        :return:
        """
    def PermitOnly(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """
    def ToXml(self) -> SecurityElement:
        """

        :return:
        """
    def Union(self, target: IPermission) -> IPermission:
        """

        :param target:
        :return:
        """

class StorePermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    """"""

    def __init__(self, action: SecurityAction):
        """

        :param action:
        """
    @property
    def Action(self) -> SecurityAction:
        """

        :return:
        """
    @Action.setter
    def Action(self, value: SecurityAction) -> None: ...
    @property
    def AddToStore(self) -> bool:
        """

        :return:
        """
    @AddToStore.setter
    def AddToStore(self, value: bool) -> None: ...
    @property
    def CreateStore(self) -> bool:
        """

        :return:
        """
    @CreateStore.setter
    def CreateStore(self, value: bool) -> None: ...
    @property
    def DeleteStore(self) -> bool:
        """

        :return:
        """
    @DeleteStore.setter
    def DeleteStore(self, value: bool) -> None: ...
    @property
    def EnumerateCertificates(self) -> bool:
        """

        :return:
        """
    @EnumerateCertificates.setter
    def EnumerateCertificates(self, value: bool) -> None: ...
    @property
    def EnumerateStores(self) -> bool:
        """

        :return:
        """
    @EnumerateStores.setter
    def EnumerateStores(self, value: bool) -> None: ...
    @property
    def Flags(self) -> StorePermissionFlags:
        """

        :return:
        """
    @Flags.setter
    def Flags(self, value: StorePermissionFlags) -> None: ...
    @property
    def OpenStore(self) -> bool:
        """

        :return:
        """
    @OpenStore.setter
    def OpenStore(self, value: bool) -> None: ...
    @property
    def RemoveFromStore(self) -> bool:
        """

        :return:
        """
    @RemoveFromStore.setter
    def RemoveFromStore(self, value: bool) -> None: ...
    @property
    def TypeId(self) -> object:
        """

        :return:
        """
    @property
    def Unrestricted(self) -> bool:
        """

        :return:
        """
    @Unrestricted.setter
    def Unrestricted(self, value: bool) -> None: ...
    def CreatePermission(self) -> IPermission:
        """

        :return:
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
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """

        :return:
        """
    def Match(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class StorePermissionFlags(Enum):
    """"""

    NoFlags: StorePermissionFlags = ...
    """"""
    CreateStore: StorePermissionFlags = ...
    """"""
    DeleteStore: StorePermissionFlags = ...
    """"""
    EnumerateStores: StorePermissionFlags = ...
    """"""
    OpenStore: StorePermissionFlags = ...
    """"""
    AddToStore: StorePermissionFlags = ...
    """"""
    RemoveFromStore: StorePermissionFlags = ...
    """"""
    EnumerateCertificates: StorePermissionFlags = ...
    """"""
    AllFlags: StorePermissionFlags = ...
    """"""

class StrongName2(Object):
    """"""

    m_name: Final[str] = ...
    """
    
    :return: 
    """
    m_publicKeyBlob: Final[StrongNamePublicKeyBlob] = ...
    """
    
    :return: 
    """
    m_version: Final[Version] = ...
    """
    
    :return: 
    """
    def __init__(self, publicKeyBlob: StrongNamePublicKeyBlob, name: str, version: Version):
        """

        :param publicKeyBlob:
        :param name:
        :param version:
        """
    def Copy(self) -> StrongName2:
        """

        :return:
        """
    @overload
    def Equals(self, target: StrongName2) -> bool:
        """

        :param target:
        :return:
        """
    @overload
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
    def Intersect(self, target: StrongName2) -> StrongName2:
        """

        :param target:
        :return:
        """
    def IsSubsetOf(self, target: StrongName2) -> bool:
        """

        :param target:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class StrongNameIdentityPermission(
    CodeAccessPermission, IBuiltInPermission, IPermission, ISecurityEncodable, IStackWalk
):
    """"""

    @overload
    def __init__(self, state: PermissionState):
        """

        :param state:
        """
    @overload
    def __init__(self, blob: StrongNamePublicKeyBlob, name: str, version: Version):
        """

        :param blob:
        :param name:
        :param version:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def PublicKey(self) -> StrongNamePublicKeyBlob:
        """

        :return:
        """
    @PublicKey.setter
    def PublicKey(self, value: StrongNamePublicKeyBlob) -> None: ...
    @property
    def Version(self) -> Version:
        """

        :return:
        """
    @Version.setter
    def Version(self, value: Version) -> None: ...
    def Assert(self) -> None:
        """"""
    def Copy(self) -> IPermission:
        """

        :return:
        """
    @overload
    def Demand(self) -> None:
        """"""
    @overload
    def Demand(self) -> None:
        """"""
    def Deny(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def FromXml(self, e: SecurityElement) -> None:
        """

        :param e:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetTokenIndex(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def Intersect(self, target: IPermission) -> IPermission:
        """

        :param target:
        :return:
        """
    def IsSubsetOf(self, target: IPermission) -> bool:
        """

        :param target:
        :return:
        """
    def PermitOnly(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """
    def ToXml(self) -> SecurityElement:
        """

        :return:
        """
    def Union(self, target: IPermission) -> IPermission:
        """

        :param target:
        :return:
        """

class StrongNameIdentityPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    """"""

    def __init__(self, action: SecurityAction):
        """

        :param action:
        """
    @property
    def Action(self) -> SecurityAction:
        """

        :return:
        """
    @Action.setter
    def Action(self, value: SecurityAction) -> None: ...
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def PublicKey(self) -> str:
        """

        :return:
        """
    @PublicKey.setter
    def PublicKey(self, value: str) -> None: ...
    @property
    def TypeId(self) -> object:
        """

        :return:
        """
    @property
    def Unrestricted(self) -> bool:
        """

        :return:
        """
    @Unrestricted.setter
    def Unrestricted(self, value: bool) -> None: ...
    @property
    def Version(self) -> str:
        """

        :return:
        """
    @Version.setter
    def Version(self, value: str) -> None: ...
    def CreatePermission(self) -> IPermission:
        """

        :return:
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
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """

        :return:
        """
    def Match(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class StrongNamePublicKeyBlob(Object):
    """"""

    def __init__(self, publicKey: Array[int]):
        """

        :param publicKey:
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
    def ToString(self) -> str:
        """

        :return:
        """

class TypeDescriptorPermission(
    CodeAccessPermission, IUnrestrictedPermission, IPermission, ISecurityEncodable, IStackWalk
):
    """"""

    @overload
    def __init__(self, state: PermissionState):
        """

        :param state:
        """
    @overload
    def __init__(self, flag: TypeDescriptorPermissionFlags):
        """

        :param flag:
        """
    @property
    def Flags(self) -> TypeDescriptorPermissionFlags:
        """

        :return:
        """
    @Flags.setter
    def Flags(self, value: TypeDescriptorPermissionFlags) -> None: ...
    def Assert(self) -> None:
        """"""
    def Copy(self) -> IPermission:
        """

        :return:
        """
    @overload
    def Demand(self) -> None:
        """"""
    @overload
    def Demand(self) -> None:
        """"""
    def Deny(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def FromXml(self, e: SecurityElement) -> None:
        """

        :param e:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def Intersect(self, target: IPermission) -> IPermission:
        """

        :param target:
        :return:
        """
    def IsSubsetOf(self, target: IPermission) -> bool:
        """

        :param target:
        :return:
        """
    def IsUnrestricted(self) -> bool:
        """

        :return:
        """
    def PermitOnly(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """
    def ToXml(self) -> SecurityElement:
        """

        :return:
        """
    def Union(self, target: IPermission) -> IPermission:
        """

        :param target:
        :return:
        """

class TypeDescriptorPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    """"""

    def __init__(self, action: SecurityAction):
        """

        :param action:
        """
    @property
    def Action(self) -> SecurityAction:
        """

        :return:
        """
    @Action.setter
    def Action(self, value: SecurityAction) -> None: ...
    @property
    def Flags(self) -> TypeDescriptorPermissionFlags:
        """

        :return:
        """
    @Flags.setter
    def Flags(self, value: TypeDescriptorPermissionFlags) -> None: ...
    @property
    def RestrictedRegistrationAccess(self) -> bool:
        """

        :return:
        """
    @RestrictedRegistrationAccess.setter
    def RestrictedRegistrationAccess(self, value: bool) -> None: ...
    @property
    def TypeId(self) -> object:
        """

        :return:
        """
    @property
    def Unrestricted(self) -> bool:
        """

        :return:
        """
    @Unrestricted.setter
    def Unrestricted(self, value: bool) -> None: ...
    def CreatePermission(self) -> IPermission:
        """

        :return:
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
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """

        :return:
        """
    def Match(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class TypeDescriptorPermissionFlags(Enum):
    """"""

    NoFlags: TypeDescriptorPermissionFlags = ...
    """"""
    RestrictedRegistrationAccess: TypeDescriptorPermissionFlags = ...
    """"""

class UIPermission(
    CodeAccessPermission,
    IBuiltInPermission,
    IUnrestrictedPermission,
    IPermission,
    ISecurityEncodable,
    IStackWalk,
):
    """"""

    @overload
    def __init__(self, state: PermissionState):
        """

        :param state:
        """
    @overload
    def __init__(self, clipboardFlag: UIPermissionClipboard):
        """

        :param clipboardFlag:
        """
    @overload
    def __init__(self, windowFlag: UIPermissionWindow):
        """

        :param windowFlag:
        """
    @overload
    def __init__(self, windowFlag: UIPermissionWindow, clipboardFlag: UIPermissionClipboard):
        """

        :param windowFlag:
        :param clipboardFlag:
        """
    @property
    def Clipboard(self) -> UIPermissionClipboard:
        """

        :return:
        """
    @Clipboard.setter
    def Clipboard(self, value: UIPermissionClipboard) -> None: ...
    @property
    def Window(self) -> UIPermissionWindow:
        """

        :return:
        """
    @Window.setter
    def Window(self, value: UIPermissionWindow) -> None: ...
    def Assert(self) -> None:
        """"""
    def Copy(self) -> IPermission:
        """

        :return:
        """
    @overload
    def Demand(self) -> None:
        """"""
    @overload
    def Demand(self) -> None:
        """"""
    def Deny(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def FromXml(self, e: SecurityElement) -> None:
        """

        :param e:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetTokenIndex(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def Intersect(self, target: IPermission) -> IPermission:
        """

        :param target:
        :return:
        """
    def IsSubsetOf(self, target: IPermission) -> bool:
        """

        :param target:
        :return:
        """
    def IsUnrestricted(self) -> bool:
        """

        :return:
        """
    def PermitOnly(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """
    def ToXml(self) -> SecurityElement:
        """

        :return:
        """
    def Union(self, target: IPermission) -> IPermission:
        """

        :param target:
        :return:
        """

class UIPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    """"""

    def __init__(self, action: SecurityAction):
        """

        :param action:
        """
    @property
    def Action(self) -> SecurityAction:
        """

        :return:
        """
    @Action.setter
    def Action(self, value: SecurityAction) -> None: ...
    @property
    def Clipboard(self) -> UIPermissionClipboard:
        """

        :return:
        """
    @Clipboard.setter
    def Clipboard(self, value: UIPermissionClipboard) -> None: ...
    @property
    def TypeId(self) -> object:
        """

        :return:
        """
    @property
    def Unrestricted(self) -> bool:
        """

        :return:
        """
    @Unrestricted.setter
    def Unrestricted(self, value: bool) -> None: ...
    @property
    def Window(self) -> UIPermissionWindow:
        """

        :return:
        """
    @Window.setter
    def Window(self, value: UIPermissionWindow) -> None: ...
    def CreatePermission(self) -> IPermission:
        """

        :return:
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
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """

        :return:
        """
    def Match(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class UIPermissionClipboard(Enum):
    """"""

    NoClipboard: UIPermissionClipboard = ...
    """"""
    OwnClipboard: UIPermissionClipboard = ...
    """"""
    AllClipboard: UIPermissionClipboard = ...
    """"""

class UIPermissionWindow(Enum):
    """"""

    NoWindows: UIPermissionWindow = ...
    """"""
    SafeSubWindows: UIPermissionWindow = ...
    """"""
    SafeTopLevelWindows: UIPermissionWindow = ...
    """"""
    AllWindows: UIPermissionWindow = ...
    """"""

class UrlIdentityPermission(
    CodeAccessPermission, IBuiltInPermission, IPermission, ISecurityEncodable, IStackWalk
):
    """"""

    @overload
    def __init__(self, state: PermissionState):
        """

        :param state:
        """
    @overload
    def __init__(self, site: str):
        """

        :param site:
        """
    @property
    def Url(self) -> str:
        """

        :return:
        """
    @Url.setter
    def Url(self, value: str) -> None: ...
    def Assert(self) -> None:
        """"""
    def Copy(self) -> IPermission:
        """

        :return:
        """
    @overload
    def Demand(self) -> None:
        """"""
    @overload
    def Demand(self) -> None:
        """"""
    def Deny(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def FromXml(self, e: SecurityElement) -> None:
        """

        :param e:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetTokenIndex(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def Intersect(self, target: IPermission) -> IPermission:
        """

        :param target:
        :return:
        """
    def IsSubsetOf(self, target: IPermission) -> bool:
        """

        :param target:
        :return:
        """
    def PermitOnly(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """
    def ToXml(self) -> SecurityElement:
        """

        :return:
        """
    def Union(self, target: IPermission) -> IPermission:
        """

        :param target:
        :return:
        """

class UrlIdentityPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    """"""

    def __init__(self, action: SecurityAction):
        """

        :param action:
        """
    @property
    def Action(self) -> SecurityAction:
        """

        :return:
        """
    @Action.setter
    def Action(self, value: SecurityAction) -> None: ...
    @property
    def TypeId(self) -> object:
        """

        :return:
        """
    @property
    def Unrestricted(self) -> bool:
        """

        :return:
        """
    @Unrestricted.setter
    def Unrestricted(self, value: bool) -> None: ...
    @property
    def Url(self) -> str:
        """

        :return:
        """
    @Url.setter
    def Url(self, value: str) -> None: ...
    def CreatePermission(self) -> IPermission:
        """

        :return:
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
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """

        :return:
        """
    def Match(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class ZoneIdentityPermission(
    CodeAccessPermission, IBuiltInPermission, IPermission, ISecurityEncodable, IStackWalk
):
    """"""

    @overload
    def __init__(self, state: PermissionState):
        """

        :param state:
        """
    @overload
    def __init__(self, zone: SecurityZone):
        """

        :param zone:
        """
    @property
    def SecurityZone(self) -> SecurityZone:
        """

        :return:
        """
    @SecurityZone.setter
    def SecurityZone(self, value: SecurityZone) -> None: ...
    def Assert(self) -> None:
        """"""
    def Copy(self) -> IPermission:
        """

        :return:
        """
    @overload
    def Demand(self) -> None:
        """"""
    @overload
    def Demand(self) -> None:
        """"""
    def Deny(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def FromXml(self, e: SecurityElement) -> None:
        """

        :param e:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetTokenIndex(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def Intersect(self, target: IPermission) -> IPermission:
        """

        :param target:
        :return:
        """
    def IsSubsetOf(self, target: IPermission) -> bool:
        """

        :param target:
        :return:
        """
    def PermitOnly(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """
    def ToXml(self) -> SecurityElement:
        """

        :return:
        """
    def Union(self, target: IPermission) -> IPermission:
        """

        :param target:
        :return:
        """

class ZoneIdentityPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    """"""

    def __init__(self, action: SecurityAction):
        """

        :param action:
        """
    @property
    def Action(self) -> SecurityAction:
        """

        :return:
        """
    @Action.setter
    def Action(self, value: SecurityAction) -> None: ...
    @property
    def TypeId(self) -> object:
        """

        :return:
        """
    @property
    def Unrestricted(self) -> bool:
        """

        :return:
        """
    @Unrestricted.setter
    def Unrestricted(self, value: bool) -> None: ...
    @property
    def Zone(self) -> SecurityZone:
        """

        :return:
        """
    @Zone.setter
    def Zone(self, value: SecurityZone) -> None: ...
    def CreatePermission(self) -> IPermission:
        """

        :return:
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
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """

        :return:
        """
    def Match(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
