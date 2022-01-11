from __future__ import annotations

from abc import ABC
from typing import List, Union

from System import ActivationContext, ApplicationIdentity, Array, Boolean, Byte, Object, Void

# ---------- Types ---------- #

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
ByteType = Union[int, Byte]
ObjectType = Object
VoidType = Union[None, Void]


# ---------- Classes ---------- #

class InternalActivationContextHelper(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def GetActivationContextData(appInfo: ActivationContext) -> ObjectType: ...
    
    @staticmethod
    def GetApplicationComponentManifest(appInfo: ActivationContext) -> ObjectType: ...
    
    @staticmethod
    def GetApplicationManifestBytes(appInfo: ActivationContext) -> ArrayType[ByteType]: ...
    
    @staticmethod
    def GetDeploymentComponentManifest(appInfo: ActivationContext) -> ObjectType: ...
    
    @staticmethod
    def GetDeploymentManifestBytes(appInfo: ActivationContext) -> ArrayType[ByteType]: ...
    
    @staticmethod
    def IsFirstRun(appInfo: ActivationContext) -> BooleanType: ...
    
    @staticmethod
    def PrepareForExecution(appInfo: ActivationContext) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class InternalApplicationIdentityHelper(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def GetInternalAppId(id: ApplicationIdentity) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# No Structs

# No Interfaces

# No Enums

# No Delegates

__all__ = [
    InternalActivationContextHelper,
    InternalApplicationIdentityHelper,
]
