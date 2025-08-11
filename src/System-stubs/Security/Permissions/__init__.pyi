"""Automatically generated stubs for C# namespace: System.Security.Permissions."""

from abc import ABC
from collections.abc import Iterator
from typing import ClassVar
from typing import Final
from typing import overload

from System import Array
from System import Attribute
from System import Enum
from System import Guid
from System import IntPtr
from System import Object
from System import Type
from System import UInt32
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

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class BuiltInPermissionIndex(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CodeAccessSecurityAttribute(ABC, SecurityAttribute, _Attribute):
    """"""
    @property
    def Action(self) -> SecurityAction:
        """"""
    @Action.setter
    def Action(self, value: SecurityAction) -> None: ...
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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
    def __init__(self, state: PermissionState) -> None:
        """"""
    @overload
    def __init__(self, flag: EnvironmentPermissionAccess, pathList: str) -> None:
        """"""
    def AddPathList(self, flag: EnvironmentPermissionAccess, pathList: str) -> None:
        """"""
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
    def FromXml(self, esd: SecurityElement) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetPathList(self, flag: EnvironmentPermissionAccess) -> str:
        """"""
    def GetTokenIndex(self) -> int:
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
    def SetPathList(self, flag: EnvironmentPermissionAccess, pathList: str) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def ToXml(self) -> SecurityElement:
        """"""
    def Union(self, other: IPermission) -> IPermission:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class EnvironmentPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    """"""
    def __init__(self, action: SecurityAction) -> None:
        """"""
    @property
    def Action(self) -> SecurityAction:
        """"""
    @Action.setter
    def Action(self, value: SecurityAction) -> None: ...
    @property
    def All(self) -> str:
        """"""
    @All.setter
    def All(self, value: str) -> None: ...
    @property
    def Read(self) -> str:
        """"""
    @Read.setter
    def Read(self, value: str) -> None: ...
    @property
    def TypeId(self) -> object:
        """"""
    @property
    def Unrestricted(self) -> bool:
        """"""
    @Unrestricted.setter
    def Unrestricted(self, value: bool) -> None: ...
    @property
    def Write(self) -> str:
        """"""
    @Write.setter
    def Write(self, value: str) -> None: ...
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class EnvironmentStringExpressionSet(StringExpressionSet):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, str: str) -> None:
        """"""
    @overload
    def AddExpressions(self, exprArrayList: ArrayList, checkForDuplicates: bool) -> None:
        """"""
    @overload
    def AddExpressions(self, str: Array[str], checkForDuplicates: bool, needFullPath: bool) -> None:
        """"""
    @overload
    def AddExpressions(self, str: str) -> None:
        """"""
    def Copy(self) -> StringExpressionSet:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Intersect(self, ses: StringExpressionSet) -> StringExpressionSet:
        """"""
    def IsEmpty(self) -> bool:
        """"""
    def IsSubsetOf(self, ses: StringExpressionSet) -> bool:
        """"""
    def IsSubsetOfPathDiscovery(self, ses: StringExpressionSet) -> bool:
        """"""
    def SetThrowOnRelative(self, throwOnRelative: bool) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def Union(self, ses: StringExpressionSet) -> StringExpressionSet:
        """"""
    def UnsafeToString(self) -> str:
        """"""
    def UnsafeToStringArray(self) -> Array[str]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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
    def __init__(self, state: PermissionState) -> None:
        """"""
    @overload
    def __init__(self, access: FileDialogPermissionAccess) -> None:
        """"""
    @property
    def Access(self) -> FileDialogPermissionAccess:
        """"""
    @Access.setter
    def Access(self, value: FileDialogPermissionAccess) -> None: ...
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
    def FromXml(self, esd: SecurityElement) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetTokenIndex(self) -> int:
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

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class FileDialogPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    """"""
    def __init__(self, action: SecurityAction) -> None:
        """"""
    @property
    def Action(self) -> SecurityAction:
        """"""
    @Action.setter
    def Action(self, value: SecurityAction) -> None: ...
    @property
    def Open(self) -> bool:
        """"""
    @Open.setter
    def Open(self, value: bool) -> None: ...
    @property
    def Save(self) -> bool:
        """"""
    @Save.setter
    def Save(self, value: bool) -> None: ...
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class FileIOAccess(Object):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, pathDiscovery: bool) -> None:
        """"""
    @overload
    def __init__(self, value: str) -> None:
        """"""
    @overload
    def __init__(self, allFiles: bool, allLocalFiles: bool, pathDiscovery: bool) -> None:
        """"""
    @overload
    def __init__(
        self, set: StringExpressionSet, allFiles: bool, allLocalFiles: bool, pathDiscovery: bool
    ) -> None:
        """"""
    @property
    def AllFiles(self) -> bool:
        """"""
    @AllFiles.setter
    def AllFiles(self, value: bool) -> None: ...
    @property
    def AllLocalFiles(self) -> bool:
        """"""
    @AllLocalFiles.setter
    def AllLocalFiles(self, value: bool) -> None: ...
    @property
    def PathDiscovery(self) -> bool:
        """"""
    @PathDiscovery.setter
    def PathDiscovery(self, value: bool) -> None: ...
    def AddExpressions(self, values: ArrayList, checkForDuplicates: bool) -> None:
        """"""
    def Copy(self) -> FileIOAccess:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Intersect(self, operand: FileIOAccess) -> FileIOAccess:
        """"""
    def IsEmpty(self) -> bool:
        """"""
    def IsSubsetOf(self, operand: FileIOAccess) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    def ToStringArray(self) -> Array[str]:
        """"""
    def Union(self, operand: FileIOAccess) -> FileIOAccess:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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
    def __init__(self, state: PermissionState) -> None:
        """"""
    @overload
    def __init__(self, access: FileIOPermissionAccess, path: str) -> None:
        """"""
    @overload
    def __init__(self, access: FileIOPermissionAccess, pathList: Array[str]) -> None:
        """"""
    @overload
    def __init__(
        self, access: FileIOPermissionAccess, control: AccessControlActions, path: str
    ) -> None:
        """"""
    @overload
    def __init__(
        self, access: FileIOPermissionAccess, control: AccessControlActions, pathList: Array[str]
    ) -> None:
        """"""
    @property
    def AllFiles(self) -> FileIOPermissionAccess:
        """"""
    @AllFiles.setter
    def AllFiles(self, value: FileIOPermissionAccess) -> None: ...
    @property
    def AllLocalFiles(self) -> FileIOPermissionAccess:
        """"""
    @AllLocalFiles.setter
    def AllLocalFiles(self, value: FileIOPermissionAccess) -> None: ...
    @overload
    def AddPathList(self, access: FileIOPermissionAccess, pathList: Array[str]) -> None:
        """"""
    @overload
    def AddPathList(self, access: FileIOPermissionAccess, path: str) -> None:
        """"""
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
    def FromXml(self, esd: SecurityElement) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetPathList(self, access: FileIOPermissionAccess) -> Array[str]:
        """"""
    def GetTokenIndex(self) -> int:
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
    @overload
    def SetPathList(self, access: FileIOPermissionAccess, pathList: Array[str]) -> None:
        """"""
    @overload
    def SetPathList(self, access: FileIOPermissionAccess, path: str) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def ToXml(self) -> SecurityElement:
        """"""
    def Union(self, other: IPermission) -> IPermission:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class FileIOPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    """"""
    def __init__(self, action: SecurityAction) -> None:
        """"""
    @property
    def Action(self) -> SecurityAction:
        """"""
    @Action.setter
    def Action(self, value: SecurityAction) -> None: ...
    @property
    def All(self) -> str:
        """"""
    @All.setter
    def All(self, value: str) -> None: ...
    @property
    def AllFiles(self) -> FileIOPermissionAccess:
        """"""
    @AllFiles.setter
    def AllFiles(self, value: FileIOPermissionAccess) -> None: ...
    @property
    def AllLocalFiles(self) -> FileIOPermissionAccess:
        """"""
    @AllLocalFiles.setter
    def AllLocalFiles(self, value: FileIOPermissionAccess) -> None: ...
    @property
    def Append(self) -> str:
        """"""
    @Append.setter
    def Append(self, value: str) -> None: ...
    @property
    def ChangeAccessControl(self) -> str:
        """"""
    @ChangeAccessControl.setter
    def ChangeAccessControl(self, value: str) -> None: ...
    @property
    def PathDiscovery(self) -> str:
        """"""
    @PathDiscovery.setter
    def PathDiscovery(self, value: str) -> None: ...
    @property
    def Read(self) -> str:
        """"""
    @Read.setter
    def Read(self, value: str) -> None: ...
    @property
    def TypeId(self) -> object:
        """"""
    @property
    def Unrestricted(self) -> bool:
        """"""
    @Unrestricted.setter
    def Unrestricted(self, value: bool) -> None: ...
    @property
    def ViewAccessControl(self) -> str:
        """"""
    @ViewAccessControl.setter
    def ViewAccessControl(self, value: str) -> None: ...
    @property
    def ViewAndModify(self) -> str:
        """"""
    @ViewAndModify.setter
    def ViewAndModify(self, value: str) -> None: ...
    @property
    def Write(self) -> str:
        """"""
    @Write.setter
    def Write(self, value: str) -> None: ...
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class GacIdentityPermission(
    CodeAccessPermission, IBuiltInPermission, IPermission, ISecurityEncodable, IStackWalk
):
    """"""
    @overload
    def __init__(self, state: PermissionState) -> None:
        """"""
    @overload
    def __init__(self) -> None:
        """"""
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
    def GetTokenIndex(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Intersect(self, target: IPermission) -> IPermission:
        """"""
    def IsSubsetOf(self, target: IPermission) -> bool:
        """"""
    def PermitOnly(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def ToXml(self) -> SecurityElement:
        """"""
    def Union(self, target: IPermission) -> IPermission:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class GacIdentityPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    """"""
    def __init__(self, action: SecurityAction) -> None:
        """"""
    @property
    def Action(self) -> SecurityAction:
        """"""
    @Action.setter
    def Action(self, value: SecurityAction) -> None: ...
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class HostProtectionAttribute(CodeAccessSecurityAttribute, _Attribute):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, action: SecurityAction) -> None:
        """"""
    @property
    def Action(self) -> SecurityAction:
        """"""
    @Action.setter
    def Action(self, value: SecurityAction) -> None: ...
    @property
    def ExternalProcessMgmt(self) -> bool:
        """"""
    @ExternalProcessMgmt.setter
    def ExternalProcessMgmt(self, value: bool) -> None: ...
    @property
    def ExternalThreading(self) -> bool:
        """"""
    @ExternalThreading.setter
    def ExternalThreading(self, value: bool) -> None: ...
    @property
    def MayLeakOnAbort(self) -> bool:
        """"""
    @MayLeakOnAbort.setter
    def MayLeakOnAbort(self, value: bool) -> None: ...
    @property
    def Resources(self) -> HostProtectionResource:
        """"""
    @Resources.setter
    def Resources(self, value: HostProtectionResource) -> None: ...
    @property
    def SecurityInfrastructure(self) -> bool:
        """"""
    @SecurityInfrastructure.setter
    def SecurityInfrastructure(self, value: bool) -> None: ...
    @property
    def SelfAffectingProcessMgmt(self) -> bool:
        """"""
    @SelfAffectingProcessMgmt.setter
    def SelfAffectingProcessMgmt(self, value: bool) -> None: ...
    @property
    def SelfAffectingThreading(self) -> bool:
        """"""
    @SelfAffectingThreading.setter
    def SelfAffectingThreading(self, value: bool) -> None: ...
    @property
    def SharedState(self) -> bool:
        """"""
    @SharedState.setter
    def SharedState(self, value: bool) -> None: ...
    @property
    def Synchronization(self) -> bool:
        """"""
    @Synchronization.setter
    def Synchronization(self, value: bool) -> None: ...
    @property
    def TypeId(self) -> object:
        """"""
    @property
    def UI(self) -> bool:
        """"""
    @UI.setter
    def UI(self, value: bool) -> None: ...
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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
    def __init__(self, state: PermissionState) -> None:
        """"""
    @overload
    def __init__(self, resources: HostProtectionResource) -> None:
        """"""
    @property
    def Resources(self) -> HostProtectionResource:
        """"""
    @Resources.setter
    def Resources(self, value: HostProtectionResource) -> None: ...
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
    def FromXml(self, esd: SecurityElement) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetTokenIndex(self) -> int:
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

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IBuiltInPermission(ABC):
    """"""
    def GetTokenIndex(self) -> int:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IDRole(Object):
    """"""
    def __init__(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IUnrestrictedPermission(ABC):
    """"""
    def IsUnrestricted(self) -> bool:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IsolatedStorageFilePermission(
    IsolatedStoragePermission,
    IBuiltInPermission,
    IUnrestrictedPermission,
    IPermission,
    ISecurityEncodable,
    IStackWalk,
):
    """"""
    def __init__(self, state: PermissionState) -> None:
        """"""
    @property
    def UsageAllowed(self) -> IsolatedStorageContainment:
        """"""
    @UsageAllowed.setter
    def UsageAllowed(self, value: IsolatedStorageContainment) -> None: ...
    @property
    def UserQuota(self) -> int:
        """"""
    @UserQuota.setter
    def UserQuota(self, value: int) -> None: ...
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
    def FromXml(self, esd: SecurityElement) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetTokenIndex(self) -> int:
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IsolatedStorageFilePermissionAttribute(IsolatedStoragePermissionAttribute, _Attribute):
    """"""
    def __init__(self, action: SecurityAction) -> None:
        """"""
    @property
    def Action(self) -> SecurityAction:
        """"""
    @Action.setter
    def Action(self, value: SecurityAction) -> None: ...
    @property
    def TypeId(self) -> object:
        """"""
    @property
    def Unrestricted(self) -> bool:
        """"""
    @Unrestricted.setter
    def Unrestricted(self, value: bool) -> None: ...
    @property
    def UsageAllowed(self) -> IsolatedStorageContainment:
        """"""
    @UsageAllowed.setter
    def UsageAllowed(self, value: IsolatedStorageContainment) -> None: ...
    @property
    def UserQuota(self) -> int:
        """"""
    @UserQuota.setter
    def UserQuota(self, value: int) -> None: ...
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IsolatedStoragePermission(
    ABC, CodeAccessPermission, IUnrestrictedPermission, IPermission, ISecurityEncodable, IStackWalk
):
    """"""
    @property
    def UsageAllowed(self) -> IsolatedStorageContainment:
        """"""
    @UsageAllowed.setter
    def UsageAllowed(self, value: IsolatedStorageContainment) -> None: ...
    @property
    def UserQuota(self) -> int:
        """"""
    @UserQuota.setter
    def UserQuota(self, value: int) -> None: ...
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
    def FromXml(self, esd: SecurityElement) -> None:
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
    def Union(self, other: IPermission) -> IPermission:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IsolatedStoragePermissionAttribute(ABC, CodeAccessSecurityAttribute, _Attribute):
    """"""
    @property
    def Action(self) -> SecurityAction:
        """"""
    @Action.setter
    def Action(self, value: SecurityAction) -> None: ...
    @property
    def TypeId(self) -> object:
        """"""
    @property
    def Unrestricted(self) -> bool:
        """"""
    @Unrestricted.setter
    def Unrestricted(self, value: bool) -> None: ...
    @property
    def UsageAllowed(self) -> IsolatedStorageContainment:
        """"""
    @UsageAllowed.setter
    def UsageAllowed(self, value: IsolatedStorageContainment) -> None: ...
    @property
    def UserQuota(self) -> int:
        """"""
    @UserQuota.setter
    def UserQuota(self, value: int) -> None: ...
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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
    def __init__(self, state: PermissionState) -> None:
        """"""
    @overload
    def __init__(self, flags: KeyContainerPermissionFlags) -> None:
        """"""
    @overload
    def __init__(
        self,
        flags: KeyContainerPermissionFlags,
        accessList: Array[KeyContainerPermissionAccessEntry],
    ) -> None:
        """"""
    @property
    def AccessEntries(self) -> KeyContainerPermissionAccessEntryCollection:
        """"""
    @property
    def Flags(self) -> KeyContainerPermissionFlags:
        """"""
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
    def GetTokenIndex(self) -> int:
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class KeyContainerPermissionAccessEntry(Object):
    """"""
    @overload
    def __init__(self, keyContainerName: str, flags: KeyContainerPermissionFlags) -> None:
        """"""
    @overload
    def __init__(self, parameters: CspParameters, flags: KeyContainerPermissionFlags) -> None:
        """"""
    @overload
    def __init__(
        self,
        keyStore: str,
        providerName: str,
        providerType: int,
        keyContainerName: str,
        keySpec: int,
        flags: KeyContainerPermissionFlags,
    ) -> None:
        """"""
    @property
    def Flags(self) -> KeyContainerPermissionFlags:
        """"""
    @Flags.setter
    def Flags(self, value: KeyContainerPermissionFlags) -> None: ...
    @property
    def KeyContainerName(self) -> str:
        """"""
    @KeyContainerName.setter
    def KeyContainerName(self, value: str) -> None: ...
    @property
    def KeySpec(self) -> int:
        """"""
    @KeySpec.setter
    def KeySpec(self, value: int) -> None: ...
    @property
    def KeyStore(self) -> str:
        """"""
    @KeyStore.setter
    def KeyStore(self, value: str) -> None: ...
    @property
    def ProviderName(self) -> str:
        """"""
    @ProviderName.setter
    def ProviderName(self, value: str) -> None: ...
    @property
    def ProviderType(self) -> int:
        """"""
    @ProviderType.setter
    def ProviderType(self, value: int) -> None: ...
    def Equals(self, o: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class KeyContainerPermissionAccessEntryCollection(Object, ICollection, IEnumerable):
    """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def Item(self) -> KeyContainerPermissionAccessEntry:
        """"""
    @property
    def SyncRoot(self) -> object:
        """"""
    def Add(self, accessEntry: KeyContainerPermissionAccessEntry) -> int:
        """"""
    def Clear(self) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array[KeyContainerPermissionAccessEntry], index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> KeyContainerPermissionAccessEntryEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def IndexOf(self, accessEntry: KeyContainerPermissionAccessEntry) -> int:
        """"""
    def Remove(self, accessEntry: KeyContainerPermissionAccessEntry) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    def __delitem__(self, accessEntry: KeyContainerPermissionAccessEntry) -> None:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, index: int) -> KeyContainerPermissionAccessEntry:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class KeyContainerPermissionAccessEntryEnumerator(Object, IEnumerator):
    """"""
    @property
    def Current(self) -> KeyContainerPermissionAccessEntry:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def MoveNext(self) -> bool:
        """"""
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class KeyContainerPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    """"""
    def __init__(self, action: SecurityAction) -> None:
        """"""
    @property
    def Action(self) -> SecurityAction:
        """"""
    @Action.setter
    def Action(self, value: SecurityAction) -> None: ...
    @property
    def Flags(self) -> KeyContainerPermissionFlags:
        """"""
    @Flags.setter
    def Flags(self, value: KeyContainerPermissionFlags) -> None: ...
    @property
    def KeyContainerName(self) -> str:
        """"""
    @KeyContainerName.setter
    def KeyContainerName(self, value: str) -> None: ...
    @property
    def KeySpec(self) -> int:
        """"""
    @KeySpec.setter
    def KeySpec(self, value: int) -> None: ...
    @property
    def KeyStore(self) -> str:
        """"""
    @KeyStore.setter
    def KeyStore(self, value: str) -> None: ...
    @property
    def ProviderName(self) -> str:
        """"""
    @ProviderName.setter
    def ProviderName(self, value: str) -> None: ...
    @property
    def ProviderType(self) -> int:
        """"""
    @ProviderType.setter
    def ProviderType(self, value: int) -> None: ...
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

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class PermissionSetAttribute(CodeAccessSecurityAttribute, _Attribute):
    """"""
    def __init__(self, action: SecurityAction) -> None:
        """"""
    @property
    def Action(self) -> SecurityAction:
        """"""
    @Action.setter
    def Action(self, value: SecurityAction) -> None: ...
    @property
    def File(self) -> str:
        """"""
    @File.setter
    def File(self, value: str) -> None: ...
    @property
    def Hex(self) -> str:
        """"""
    @Hex.setter
    def Hex(self, value: str) -> None: ...
    @property
    def Name(self) -> str:
        """"""
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def TypeId(self) -> object:
        """"""
    @property
    def UnicodeEncoded(self) -> bool:
        """"""
    @UnicodeEncoded.setter
    def UnicodeEncoded(self, value: bool) -> None: ...
    @property
    def Unrestricted(self) -> bool:
        """"""
    @Unrestricted.setter
    def Unrestricted(self, value: bool) -> None: ...
    @property
    def XML(self) -> str:
        """"""
    @XML.setter
    def XML(self, value: str) -> None: ...
    def CreatePermission(self) -> IPermission:
        """"""
    def CreatePermissionSet(self) -> PermissionSet:
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

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class PermissionState(Enum):
    """"""

    _None: PermissionState = ...
    """"""
    Unrestricted: PermissionState = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class PrincipalPermission(
    Object, IBuiltInPermission, IUnrestrictedPermission, IPermission, ISecurityEncodable
):
    """"""
    @overload
    def __init__(self, state: PermissionState) -> None:
        """"""
    @overload
    def __init__(self, name: str, role: str) -> None:
        """"""
    @overload
    def __init__(self, name: str, role: str, isAuthenticated: bool) -> None:
        """"""
    def Copy(self) -> IPermission:
        """"""
    def Demand(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def FromXml(self, elem: SecurityElement) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetTokenIndex(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Intersect(self, target: IPermission) -> IPermission:
        """"""
    def IsSubsetOf(self, target: IPermission) -> bool:
        """"""
    def IsUnrestricted(self) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    def ToXml(self) -> SecurityElement:
        """"""
    def Union(self, other: IPermission) -> IPermission:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class PrincipalPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    """"""
    def __init__(self, action: SecurityAction) -> None:
        """"""
    @property
    def Action(self) -> SecurityAction:
        """"""
    @Action.setter
    def Action(self, value: SecurityAction) -> None: ...
    @property
    def Authenticated(self) -> bool:
        """"""
    @Authenticated.setter
    def Authenticated(self, value: bool) -> None: ...
    @property
    def Name(self) -> str:
        """"""
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def Role(self) -> str:
        """"""
    @Role.setter
    def Role(self, value: str) -> None: ...
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class PublisherIdentityPermission(
    CodeAccessPermission, IBuiltInPermission, IPermission, ISecurityEncodable, IStackWalk
):
    """"""
    @overload
    def __init__(self, state: PermissionState) -> None:
        """"""
    @overload
    def __init__(self, certificate: X509Certificate) -> None:
        """"""
    @property
    def Certificate(self) -> X509Certificate:
        """"""
    @Certificate.setter
    def Certificate(self, value: X509Certificate) -> None: ...
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
    def FromXml(self, esd: SecurityElement) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetTokenIndex(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Intersect(self, target: IPermission) -> IPermission:
        """"""
    def IsSubsetOf(self, target: IPermission) -> bool:
        """"""
    def PermitOnly(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def ToXml(self) -> SecurityElement:
        """"""
    def Union(self, target: IPermission) -> IPermission:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class PublisherIdentityPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    """"""
    def __init__(self, action: SecurityAction) -> None:
        """"""
    @property
    def Action(self) -> SecurityAction:
        """"""
    @Action.setter
    def Action(self, value: SecurityAction) -> None: ...
    @property
    def CertFile(self) -> str:
        """"""
    @CertFile.setter
    def CertFile(self, value: str) -> None: ...
    @property
    def SignedFile(self) -> str:
        """"""
    @SignedFile.setter
    def SignedFile(self, value: str) -> None: ...
    @property
    def TypeId(self) -> object:
        """"""
    @property
    def Unrestricted(self) -> bool:
        """"""
    @Unrestricted.setter
    def Unrestricted(self, value: bool) -> None: ...
    @property
    def X509Certificate(self) -> str:
        """"""
    @X509Certificate.setter
    def X509Certificate(self, value: str) -> None: ...
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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
    def __init__(self, state: PermissionState) -> None:
        """"""
    @overload
    def __init__(self, flag: ReflectionPermissionFlag) -> None:
        """"""
    @property
    def Flags(self) -> ReflectionPermissionFlag:
        """"""
    @Flags.setter
    def Flags(self, value: ReflectionPermissionFlag) -> None: ...
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
    def FromXml(self, esd: SecurityElement) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetTokenIndex(self) -> int:
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
    def Union(self, other: IPermission) -> IPermission:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ReflectionPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    """"""
    def __init__(self, action: SecurityAction) -> None:
        """"""
    @property
    def Action(self) -> SecurityAction:
        """"""
    @Action.setter
    def Action(self, value: SecurityAction) -> None: ...
    @property
    def Flags(self) -> ReflectionPermissionFlag:
        """"""
    @Flags.setter
    def Flags(self, value: ReflectionPermissionFlag) -> None: ...
    @property
    def MemberAccess(self) -> bool:
        """"""
    @MemberAccess.setter
    def MemberAccess(self, value: bool) -> None: ...
    @property
    def ReflectionEmit(self) -> bool:
        """"""
    @ReflectionEmit.setter
    def ReflectionEmit(self, value: bool) -> None: ...
    @property
    def RestrictedMemberAccess(self) -> bool:
        """"""
    @RestrictedMemberAccess.setter
    def RestrictedMemberAccess(self, value: bool) -> None: ...
    @property
    def TypeId(self) -> object:
        """"""
    @property
    def TypeInformation(self) -> bool:
        """"""
    @TypeInformation.setter
    def TypeInformation(self, value: bool) -> None: ...
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

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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
    def __init__(self, state: PermissionState) -> None:
        """"""
    @overload
    def __init__(self, access: RegistryPermissionAccess, pathList: str) -> None:
        """"""
    @overload
    def __init__(
        self, access: RegistryPermissionAccess, control: AccessControlActions, pathList: str
    ) -> None:
        """"""
    @overload
    def AddPathList(
        self, access: RegistryPermissionAccess, control: AccessControlActions, pathList: str
    ) -> None:
        """"""
    @overload
    def AddPathList(self, access: RegistryPermissionAccess, pathList: str) -> None:
        """"""
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
    def FromXml(self, esd: SecurityElement) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetPathList(self, access: RegistryPermissionAccess) -> str:
        """"""
    def GetTokenIndex(self) -> int:
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
    def SetPathList(self, access: RegistryPermissionAccess, pathList: str) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def ToXml(self) -> SecurityElement:
        """"""
    def Union(self, other: IPermission) -> IPermission:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class RegistryPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    """"""
    def __init__(self, action: SecurityAction) -> None:
        """"""
    @property
    def Action(self) -> SecurityAction:
        """"""
    @Action.setter
    def Action(self, value: SecurityAction) -> None: ...
    @property
    def All(self) -> str:
        """"""
    @All.setter
    def All(self, value: str) -> None: ...
    @property
    def ChangeAccessControl(self) -> str:
        """"""
    @ChangeAccessControl.setter
    def ChangeAccessControl(self, value: str) -> None: ...
    @property
    def Create(self) -> str:
        """"""
    @Create.setter
    def Create(self, value: str) -> None: ...
    @property
    def Read(self) -> str:
        """"""
    @Read.setter
    def Read(self, value: str) -> None: ...
    @property
    def TypeId(self) -> object:
        """"""
    @property
    def Unrestricted(self) -> bool:
        """"""
    @Unrestricted.setter
    def Unrestricted(self, value: bool) -> None: ...
    @property
    def ViewAccessControl(self) -> str:
        """"""
    @ViewAccessControl.setter
    def ViewAccessControl(self, value: str) -> None: ...
    @property
    def ViewAndModify(self) -> str:
        """"""
    @ViewAndModify.setter
    def ViewAndModify(self, value: str) -> None: ...
    @property
    def Write(self) -> str:
        """"""
    @Write.setter
    def Write(self, value: str) -> None: ...
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ResourcePermissionBase(
    ABC, CodeAccessPermission, IUnrestrictedPermission, IPermission, ISecurityEncodable, IStackWalk
):
    """"""

    Any: ClassVar[str]
    """"""
    Local: ClassVar[str]
    """"""
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ResourcePermissionBaseEntry(Object):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, permissionAccess: int, permissionAccessPath: Array[str]) -> None:
        """"""
    @property
    def PermissionAccess(self) -> int:
        """"""
    @property
    def PermissionAccessPath(self) -> Array[str]:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SecurityAttribute(ABC, Attribute, _Attribute):
    """"""
    @property
    def Action(self) -> SecurityAction:
        """"""
    @Action.setter
    def Action(self, value: SecurityAction) -> None: ...
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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
    def __init__(self, state: PermissionState) -> None:
        """"""
    @overload
    def __init__(self, flag: SecurityPermissionFlag) -> None:
        """"""
    @property
    def Flags(self) -> SecurityPermissionFlag:
        """"""
    @Flags.setter
    def Flags(self, value: SecurityPermissionFlag) -> None: ...
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
    def FromXml(self, esd: SecurityElement) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetTokenIndex(self) -> int:
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SecurityPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    """"""
    def __init__(self, action: SecurityAction) -> None:
        """"""
    @property
    def Action(self) -> SecurityAction:
        """"""
    @Action.setter
    def Action(self, value: SecurityAction) -> None: ...
    @property
    def Assertion(self) -> bool:
        """"""
    @Assertion.setter
    def Assertion(self, value: bool) -> None: ...
    @property
    def BindingRedirects(self) -> bool:
        """"""
    @BindingRedirects.setter
    def BindingRedirects(self, value: bool) -> None: ...
    @property
    def ControlAppDomain(self) -> bool:
        """"""
    @ControlAppDomain.setter
    def ControlAppDomain(self, value: bool) -> None: ...
    @property
    def ControlDomainPolicy(self) -> bool:
        """"""
    @ControlDomainPolicy.setter
    def ControlDomainPolicy(self, value: bool) -> None: ...
    @property
    def ControlEvidence(self) -> bool:
        """"""
    @ControlEvidence.setter
    def ControlEvidence(self, value: bool) -> None: ...
    @property
    def ControlPolicy(self) -> bool:
        """"""
    @ControlPolicy.setter
    def ControlPolicy(self, value: bool) -> None: ...
    @property
    def ControlPrincipal(self) -> bool:
        """"""
    @ControlPrincipal.setter
    def ControlPrincipal(self, value: bool) -> None: ...
    @property
    def ControlThread(self) -> bool:
        """"""
    @ControlThread.setter
    def ControlThread(self, value: bool) -> None: ...
    @property
    def Execution(self) -> bool:
        """"""
    @Execution.setter
    def Execution(self, value: bool) -> None: ...
    @property
    def Flags(self) -> SecurityPermissionFlag:
        """"""
    @Flags.setter
    def Flags(self, value: SecurityPermissionFlag) -> None: ...
    @property
    def Infrastructure(self) -> bool:
        """"""
    @Infrastructure.setter
    def Infrastructure(self, value: bool) -> None: ...
    @property
    def RemotingConfiguration(self) -> bool:
        """"""
    @RemotingConfiguration.setter
    def RemotingConfiguration(self, value: bool) -> None: ...
    @property
    def SerializationFormatter(self) -> bool:
        """"""
    @SerializationFormatter.setter
    def SerializationFormatter(self, value: bool) -> None: ...
    @property
    def SkipVerification(self) -> bool:
        """"""
    @SkipVerification.setter
    def SkipVerification(self, value: bool) -> None: ...
    @property
    def TypeId(self) -> object:
        """"""
    @property
    def UnmanagedCode(self) -> bool:
        """"""
    @UnmanagedCode.setter
    def UnmanagedCode(self, value: bool) -> None: ...
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

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SiteIdentityPermission(
    CodeAccessPermission, IBuiltInPermission, IPermission, ISecurityEncodable, IStackWalk
):
    """"""
    @overload
    def __init__(self, state: PermissionState) -> None:
        """"""
    @overload
    def __init__(self, site: str) -> None:
        """"""
    @property
    def Site(self) -> str:
        """"""
    @Site.setter
    def Site(self, value: str) -> None: ...
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
    def FromXml(self, esd: SecurityElement) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetTokenIndex(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Intersect(self, target: IPermission) -> IPermission:
        """"""
    def IsSubsetOf(self, target: IPermission) -> bool:
        """"""
    def PermitOnly(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def ToXml(self) -> SecurityElement:
        """"""
    def Union(self, target: IPermission) -> IPermission:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SiteIdentityPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    """"""
    def __init__(self, action: SecurityAction) -> None:
        """"""
    @property
    def Action(self) -> SecurityAction:
        """"""
    @Action.setter
    def Action(self, value: SecurityAction) -> None: ...
    @property
    def Site(self) -> str:
        """"""
    @Site.setter
    def Site(self, value: str) -> None: ...
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class StorePermission(
    CodeAccessPermission, IUnrestrictedPermission, IPermission, ISecurityEncodable, IStackWalk
):
    """"""
    @overload
    def __init__(self, state: PermissionState) -> None:
        """"""
    @overload
    def __init__(self, flag: StorePermissionFlags) -> None:
        """"""
    @property
    def Flags(self) -> StorePermissionFlags:
        """"""
    @Flags.setter
    def Flags(self, value: StorePermissionFlags) -> None: ...
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class StorePermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    """"""
    def __init__(self, action: SecurityAction) -> None:
        """"""
    @property
    def Action(self) -> SecurityAction:
        """"""
    @Action.setter
    def Action(self, value: SecurityAction) -> None: ...
    @property
    def AddToStore(self) -> bool:
        """"""
    @AddToStore.setter
    def AddToStore(self, value: bool) -> None: ...
    @property
    def CreateStore(self) -> bool:
        """"""
    @CreateStore.setter
    def CreateStore(self, value: bool) -> None: ...
    @property
    def DeleteStore(self) -> bool:
        """"""
    @DeleteStore.setter
    def DeleteStore(self, value: bool) -> None: ...
    @property
    def EnumerateCertificates(self) -> bool:
        """"""
    @EnumerateCertificates.setter
    def EnumerateCertificates(self, value: bool) -> None: ...
    @property
    def EnumerateStores(self) -> bool:
        """"""
    @EnumerateStores.setter
    def EnumerateStores(self, value: bool) -> None: ...
    @property
    def Flags(self) -> StorePermissionFlags:
        """"""
    @Flags.setter
    def Flags(self, value: StorePermissionFlags) -> None: ...
    @property
    def OpenStore(self) -> bool:
        """"""
    @OpenStore.setter
    def OpenStore(self, value: bool) -> None: ...
    @property
    def RemoveFromStore(self) -> bool:
        """"""
    @RemoveFromStore.setter
    def RemoveFromStore(self, value: bool) -> None: ...
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

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class StrongName2(Object):
    """"""

    m_name: Final[str]
    """"""
    m_publicKeyBlob: Final[StrongNamePublicKeyBlob]
    """"""
    m_version: Final[Version]
    """"""
    def __init__(self, publicKeyBlob: StrongNamePublicKeyBlob, name: str, version: Version) -> None:
        """"""
    def Copy(self) -> StrongName2:
        """"""
    @overload
    def Equals(self, target: StrongName2) -> bool:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Intersect(self, target: StrongName2) -> StrongName2:
        """"""
    def IsSubsetOf(self, target: StrongName2) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class StrongNameIdentityPermission(
    CodeAccessPermission, IBuiltInPermission, IPermission, ISecurityEncodable, IStackWalk
):
    """"""
    @overload
    def __init__(self, state: PermissionState) -> None:
        """"""
    @overload
    def __init__(self, blob: StrongNamePublicKeyBlob, name: str, version: Version) -> None:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def PublicKey(self) -> StrongNamePublicKeyBlob:
        """"""
    @PublicKey.setter
    def PublicKey(self, value: StrongNamePublicKeyBlob) -> None: ...
    @property
    def Version(self) -> Version:
        """"""
    @Version.setter
    def Version(self, value: Version) -> None: ...
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
    def FromXml(self, e: SecurityElement) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetTokenIndex(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Intersect(self, target: IPermission) -> IPermission:
        """"""
    def IsSubsetOf(self, target: IPermission) -> bool:
        """"""
    def PermitOnly(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def ToXml(self) -> SecurityElement:
        """"""
    def Union(self, target: IPermission) -> IPermission:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class StrongNameIdentityPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    """"""
    def __init__(self, action: SecurityAction) -> None:
        """"""
    @property
    def Action(self) -> SecurityAction:
        """"""
    @Action.setter
    def Action(self, value: SecurityAction) -> None: ...
    @property
    def Name(self) -> str:
        """"""
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def PublicKey(self) -> str:
        """"""
    @PublicKey.setter
    def PublicKey(self, value: str) -> None: ...
    @property
    def TypeId(self) -> object:
        """"""
    @property
    def Unrestricted(self) -> bool:
        """"""
    @Unrestricted.setter
    def Unrestricted(self, value: bool) -> None: ...
    @property
    def Version(self) -> str:
        """"""
    @Version.setter
    def Version(self, value: str) -> None: ...
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class StrongNamePublicKeyBlob(Object):
    """"""
    def __init__(self, publicKey: Array[int]) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class TypeDescriptorPermission(
    CodeAccessPermission, IUnrestrictedPermission, IPermission, ISecurityEncodable, IStackWalk
):
    """"""
    @overload
    def __init__(self, state: PermissionState) -> None:
        """"""
    @overload
    def __init__(self, flag: TypeDescriptorPermissionFlags) -> None:
        """"""
    @property
    def Flags(self) -> TypeDescriptorPermissionFlags:
        """"""
    @Flags.setter
    def Flags(self, value: TypeDescriptorPermissionFlags) -> None: ...
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class TypeDescriptorPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    """"""
    def __init__(self, action: SecurityAction) -> None:
        """"""
    @property
    def Action(self) -> SecurityAction:
        """"""
    @Action.setter
    def Action(self, value: SecurityAction) -> None: ...
    @property
    def Flags(self) -> TypeDescriptorPermissionFlags:
        """"""
    @Flags.setter
    def Flags(self, value: TypeDescriptorPermissionFlags) -> None: ...
    @property
    def RestrictedRegistrationAccess(self) -> bool:
        """"""
    @RestrictedRegistrationAccess.setter
    def RestrictedRegistrationAccess(self, value: bool) -> None: ...
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

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class TypeDescriptorPermissionFlags(Enum):
    """"""

    NoFlags: TypeDescriptorPermissionFlags = ...
    """"""
    RestrictedRegistrationAccess: TypeDescriptorPermissionFlags = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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
    def __init__(self, state: PermissionState) -> None:
        """"""
    @overload
    def __init__(
        self, windowFlag: UIPermissionWindow, clipboardFlag: UIPermissionClipboard
    ) -> None:
        """"""
    @overload
    def __init__(self, windowFlag: UIPermissionWindow) -> None:
        """"""
    @overload
    def __init__(self, clipboardFlag: UIPermissionClipboard) -> None:
        """"""
    @property
    def Clipboard(self) -> UIPermissionClipboard:
        """"""
    @Clipboard.setter
    def Clipboard(self, value: UIPermissionClipboard) -> None: ...
    @property
    def Window(self) -> UIPermissionWindow:
        """"""
    @Window.setter
    def Window(self, value: UIPermissionWindow) -> None: ...
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
    def FromXml(self, esd: SecurityElement) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetTokenIndex(self) -> int:
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class UIPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    """"""
    def __init__(self, action: SecurityAction) -> None:
        """"""
    @property
    def Action(self) -> SecurityAction:
        """"""
    @Action.setter
    def Action(self, value: SecurityAction) -> None: ...
    @property
    def Clipboard(self) -> UIPermissionClipboard:
        """"""
    @Clipboard.setter
    def Clipboard(self, value: UIPermissionClipboard) -> None: ...
    @property
    def TypeId(self) -> object:
        """"""
    @property
    def Unrestricted(self) -> bool:
        """"""
    @Unrestricted.setter
    def Unrestricted(self, value: bool) -> None: ...
    @property
    def Window(self) -> UIPermissionWindow:
        """"""
    @Window.setter
    def Window(self, value: UIPermissionWindow) -> None: ...
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

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class UIPermissionClipboard(Enum):
    """"""

    NoClipboard: UIPermissionClipboard = ...
    """"""
    OwnClipboard: UIPermissionClipboard = ...
    """"""
    AllClipboard: UIPermissionClipboard = ...
    """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class UrlIdentityPermission(
    CodeAccessPermission, IBuiltInPermission, IPermission, ISecurityEncodable, IStackWalk
):
    """"""
    @overload
    def __init__(self, state: PermissionState) -> None:
        """"""
    @overload
    def __init__(self, site: str) -> None:
        """"""
    @property
    def Url(self) -> str:
        """"""
    @Url.setter
    def Url(self, value: str) -> None: ...
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
    def FromXml(self, esd: SecurityElement) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetTokenIndex(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Intersect(self, target: IPermission) -> IPermission:
        """"""
    def IsSubsetOf(self, target: IPermission) -> bool:
        """"""
    def PermitOnly(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def ToXml(self) -> SecurityElement:
        """"""
    def Union(self, target: IPermission) -> IPermission:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class UrlIdentityPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    """"""
    def __init__(self, action: SecurityAction) -> None:
        """"""
    @property
    def Action(self) -> SecurityAction:
        """"""
    @Action.setter
    def Action(self, value: SecurityAction) -> None: ...
    @property
    def TypeId(self) -> object:
        """"""
    @property
    def Unrestricted(self) -> bool:
        """"""
    @Unrestricted.setter
    def Unrestricted(self, value: bool) -> None: ...
    @property
    def Url(self) -> str:
        """"""
    @Url.setter
    def Url(self, value: str) -> None: ...
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ZoneIdentityPermission(
    CodeAccessPermission, IBuiltInPermission, IPermission, ISecurityEncodable, IStackWalk
):
    """"""
    @overload
    def __init__(self, state: PermissionState) -> None:
        """"""
    @overload
    def __init__(self, zone: SecurityZone) -> None:
        """"""
    @property
    def SecurityZone(self) -> SecurityZone:
        """"""
    @SecurityZone.setter
    def SecurityZone(self, value: SecurityZone) -> None: ...
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
    def FromXml(self, esd: SecurityElement) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetTokenIndex(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Intersect(self, target: IPermission) -> IPermission:
        """"""
    def IsSubsetOf(self, target: IPermission) -> bool:
        """"""
    def PermitOnly(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def ToXml(self) -> SecurityElement:
        """"""
    def Union(self, target: IPermission) -> IPermission:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ZoneIdentityPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    """"""
    def __init__(self, action: SecurityAction) -> None:
        """"""
    @property
    def Action(self) -> SecurityAction:
        """"""
    @Action.setter
    def Action(self, value: SecurityAction) -> None: ...
    @property
    def TypeId(self) -> object:
        """"""
    @property
    def Unrestricted(self) -> bool:
        """"""
    @Unrestricted.setter
    def Unrestricted(self, value: bool) -> None: ...
    @property
    def Zone(self) -> SecurityZone:
        """"""
    @Zone.setter
    def Zone(self, value: SecurityZone) -> None: ...
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
