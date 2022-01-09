from __future__ import annotations

from abc import ABC
from typing import List, Union, overload

from System import Array, Boolean, Enum, Int32, Object, String, Void
from System.Runtime.InteropServices import _Attribute
from System.Security import CodeAccessPermission, IPermission, ISecurityEncodable, IStackWalk, SecurityElement
from System.Security.Permissions import CodeAccessSecurityAttribute, IUnrestrictedPermission, PermissionState, SecurityAction

# ---------- Types ---------- #

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
IntType = Union[int, Int32]
ObjectType = Object
StringType = Union[str, String]
VoidType = Union[None, Void]

# ---------- Classes ---------- #

class ResourcePermissionBase(ABC, CodeAccessPermission, IPermission, ISecurityEncodable, IStackWalk, IUnrestrictedPermission):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Any() -> StringType: ...
    
    @staticmethod
    @property
    def Local() -> StringType: ...
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Copy(self) -> IPermission: ...
    
    def FromXml(self, securityElement: SecurityElement) -> VoidType: ...
    
    def Intersect(self, target: IPermission) -> IPermission: ...
    
    def IsSubsetOf(self, target: IPermission) -> BooleanType: ...
    
    def IsUnrestricted(self) -> BooleanType: ...
    
    def ToXml(self) -> SecurityElement: ...
    
    def Union(self, target: IPermission) -> IPermission: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ResourcePermissionBaseEntry(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, permissionAccess: IntType, permissionAccessPath: ArrayType[StringType]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def PermissionAccess(self) -> IntType: ...
    
    @property
    def PermissionAccessPath(self) -> ArrayType[StringType]: ...
    
    # ---------- Methods ---------- #
    
    def get_PermissionAccess(self) -> IntType: ...
    
    def get_PermissionAccessPath(self) -> ArrayType[StringType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class StorePermission(CodeAccessPermission, IPermission, ISecurityEncodable, IStackWalk, IUnrestrictedPermission):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, state: PermissionState): ...
    
    @overload
    def __init__(self, flag: StorePermissionFlags): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Flags(self) -> StorePermissionFlags: ...
    
    @Flags.setter
    def Flags(self, value: StorePermissionFlags) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Copy(self) -> IPermission: ...
    
    def FromXml(self, securityElement: SecurityElement) -> VoidType: ...
    
    def Intersect(self, target: IPermission) -> IPermission: ...
    
    def IsSubsetOf(self, target: IPermission) -> BooleanType: ...
    
    def IsUnrestricted(self) -> BooleanType: ...
    
    def ToXml(self) -> SecurityElement: ...
    
    def Union(self, target: IPermission) -> IPermission: ...
    
    def get_Flags(self) -> StorePermissionFlags: ...
    
    def set_Flags(self, value: StorePermissionFlags) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class StorePermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, action: SecurityAction): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AddToStore(self) -> BooleanType: ...
    
    @AddToStore.setter
    def AddToStore(self, value: BooleanType) -> None: ...
    
    @property
    def CreateStore(self) -> BooleanType: ...
    
    @CreateStore.setter
    def CreateStore(self, value: BooleanType) -> None: ...
    
    @property
    def DeleteStore(self) -> BooleanType: ...
    
    @DeleteStore.setter
    def DeleteStore(self, value: BooleanType) -> None: ...
    
    @property
    def EnumerateCertificates(self) -> BooleanType: ...
    
    @EnumerateCertificates.setter
    def EnumerateCertificates(self, value: BooleanType) -> None: ...
    
    @property
    def EnumerateStores(self) -> BooleanType: ...
    
    @EnumerateStores.setter
    def EnumerateStores(self, value: BooleanType) -> None: ...
    
    @property
    def Flags(self) -> StorePermissionFlags: ...
    
    @Flags.setter
    def Flags(self, value: StorePermissionFlags) -> None: ...
    
    @property
    def OpenStore(self) -> BooleanType: ...
    
    @OpenStore.setter
    def OpenStore(self, value: BooleanType) -> None: ...
    
    @property
    def RemoveFromStore(self) -> BooleanType: ...
    
    @RemoveFromStore.setter
    def RemoveFromStore(self, value: BooleanType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def CreatePermission(self) -> IPermission: ...
    
    def get_AddToStore(self) -> BooleanType: ...
    
    def get_CreateStore(self) -> BooleanType: ...
    
    def get_DeleteStore(self) -> BooleanType: ...
    
    def get_EnumerateCertificates(self) -> BooleanType: ...
    
    def get_EnumerateStores(self) -> BooleanType: ...
    
    def get_Flags(self) -> StorePermissionFlags: ...
    
    def get_OpenStore(self) -> BooleanType: ...
    
    def get_RemoveFromStore(self) -> BooleanType: ...
    
    def set_AddToStore(self, value: BooleanType) -> VoidType: ...
    
    def set_CreateStore(self, value: BooleanType) -> VoidType: ...
    
    def set_DeleteStore(self, value: BooleanType) -> VoidType: ...
    
    def set_EnumerateCertificates(self, value: BooleanType) -> VoidType: ...
    
    def set_EnumerateStores(self, value: BooleanType) -> VoidType: ...
    
    def set_Flags(self, value: StorePermissionFlags) -> VoidType: ...
    
    def set_OpenStore(self, value: BooleanType) -> VoidType: ...
    
    def set_RemoveFromStore(self, value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TypeDescriptorPermission(CodeAccessPermission, IPermission, ISecurityEncodable, IStackWalk, IUnrestrictedPermission):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, state: PermissionState): ...
    
    @overload
    def __init__(self, flag: TypeDescriptorPermissionFlags): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Flags(self) -> TypeDescriptorPermissionFlags: ...
    
    @Flags.setter
    def Flags(self, value: TypeDescriptorPermissionFlags) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Copy(self) -> IPermission: ...
    
    def FromXml(self, securityElement: SecurityElement) -> VoidType: ...
    
    def Intersect(self, target: IPermission) -> IPermission: ...
    
    def IsSubsetOf(self, target: IPermission) -> BooleanType: ...
    
    def IsUnrestricted(self) -> BooleanType: ...
    
    def ToXml(self) -> SecurityElement: ...
    
    def Union(self, target: IPermission) -> IPermission: ...
    
    def get_Flags(self) -> TypeDescriptorPermissionFlags: ...
    
    def set_Flags(self, value: TypeDescriptorPermissionFlags) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TypeDescriptorPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, action: SecurityAction): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Flags(self) -> TypeDescriptorPermissionFlags: ...
    
    @Flags.setter
    def Flags(self, value: TypeDescriptorPermissionFlags) -> None: ...
    
    @property
    def RestrictedRegistrationAccess(self) -> BooleanType: ...
    
    @RestrictedRegistrationAccess.setter
    def RestrictedRegistrationAccess(self, value: BooleanType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def CreatePermission(self) -> IPermission: ...
    
    def get_Flags(self) -> TypeDescriptorPermissionFlags: ...
    
    def get_RestrictedRegistrationAccess(self) -> BooleanType: ...
    
    def set_Flags(self, value: TypeDescriptorPermissionFlags) -> VoidType: ...
    
    def set_RestrictedRegistrationAccess(self, value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# No Structs

# No Interfaces

# ---------- Enums ---------- #

class StorePermissionFlags(Enum):
    NoFlags: IntType = 0
    CreateStore: IntType = 1
    DeleteStore: IntType = 2
    EnumerateStores: IntType = 4
    OpenStore: IntType = 16
    AddToStore: IntType = 32
    RemoveFromStore: IntType = 64
    EnumerateCertificates: IntType = 128
    AllFlags: IntType = 247


class TypeDescriptorPermissionFlags(Enum):
    NoFlags: IntType = 0
    RestrictedRegistrationAccess: IntType = 1


# No Delegates

__all__ = [
    ResourcePermissionBase,
    ResourcePermissionBaseEntry,
    StorePermission,
    StorePermissionAttribute,
    TypeDescriptorPermission,
    TypeDescriptorPermissionAttribute,
    StorePermissionFlags,
    TypeDescriptorPermissionFlags,
]
