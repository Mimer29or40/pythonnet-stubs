from __future__ import annotations

from typing import List, Union, overload

from System import ActivationContext, ApplicationIdentity, Array, Object, String
from System.Runtime.Remoting import ObjectHandle
from System.Security.Policy import EvidenceBase

# ---------- Types ---------- #

ArrayType = Union[List, Array]
ObjectType = Object
StringType = Union[str, String]

# ---------- Classes ---------- #

class ActivationArguments(EvidenceBase):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, applicationIdentity: ApplicationIdentity): ...
    
    @overload
    def __init__(self, applicationIdentity: ApplicationIdentity, activationData: ArrayType[StringType]): ...
    
    @overload
    def __init__(self, activationData: ActivationContext): ...
    
    @overload
    def __init__(self, activationContext: ActivationContext, activationData: ArrayType[StringType]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ActivationContext(self) -> ActivationContext: ...
    
    @property
    def ActivationData(self) -> ArrayType[StringType]: ...
    
    @property
    def ApplicationIdentity(self) -> ApplicationIdentity: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> EvidenceBase: ...
    
    def get_ActivationContext(self) -> ActivationContext: ...
    
    def get_ActivationData(self) -> ArrayType[StringType]: ...
    
    def get_ApplicationIdentity(self) -> ApplicationIdentity: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ActivationArguments(EvidenceBase):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, applicationIdentity: ApplicationIdentity): ...
    
    @overload
    def __init__(self, applicationIdentity: ApplicationIdentity, activationData: ArrayType[StringType]): ...
    
    @overload
    def __init__(self, activationData: ActivationContext): ...
    
    @overload
    def __init__(self, activationContext: ActivationContext, activationData: ArrayType[StringType]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ActivationContext(self) -> ActivationContext: ...
    
    @property
    def ActivationData(self) -> ArrayType[StringType]: ...
    
    @property
    def ApplicationIdentity(self) -> ApplicationIdentity: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> EvidenceBase: ...
    
    def get_ActivationContext(self) -> ActivationContext: ...
    
    def get_ActivationData(self) -> ArrayType[StringType]: ...
    
    def get_ApplicationIdentity(self) -> ApplicationIdentity: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ActivationArguments(EvidenceBase):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, applicationIdentity: ApplicationIdentity): ...
    
    @overload
    def __init__(self, applicationIdentity: ApplicationIdentity, activationData: ArrayType[StringType]): ...
    
    @overload
    def __init__(self, activationData: ActivationContext): ...
    
    @overload
    def __init__(self, activationContext: ActivationContext, activationData: ArrayType[StringType]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ActivationContext(self) -> ActivationContext: ...
    
    @property
    def ActivationData(self) -> ArrayType[StringType]: ...
    
    @property
    def ApplicationIdentity(self) -> ApplicationIdentity: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> EvidenceBase: ...
    
    def get_ActivationContext(self) -> ActivationContext: ...
    
    def get_ActivationData(self) -> ArrayType[StringType]: ...
    
    def get_ApplicationIdentity(self) -> ApplicationIdentity: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ApplicationActivator(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def CreateInstance(self, activationContext: ActivationContext) -> ObjectHandle: ...
    
    @overload
    def CreateInstance(self, activationContext: ActivationContext, activationCustomData: ArrayType[StringType]) -> ObjectHandle: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ApplicationActivator(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def CreateInstance(self, activationContext: ActivationContext) -> ObjectHandle: ...
    
    @overload
    def CreateInstance(self, activationContext: ActivationContext, activationCustomData: ArrayType[StringType]) -> ObjectHandle: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ApplicationActivator(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def CreateInstance(self, activationContext: ActivationContext) -> ObjectHandle: ...
    
    @overload
    def CreateInstance(self, activationContext: ActivationContext, activationCustomData: ArrayType[StringType]) -> ObjectHandle: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ManifestRunner(ObjectType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ManifestRunner(ObjectType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ManifestRunner(ObjectType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
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
    ActivationArguments,
    ApplicationActivator,
    ManifestRunner,
]
