from __future__ import annotations

from abc import ABC
from typing import List
from typing import Protocol
from typing import Union

from System import Array
from System import Boolean
from System import Enum
from System import Int32
from System import MarshalByRefObject
from System import Object
from System import String
from System import Type
from System import Void
from System.Collections import IList
from System.Runtime.InteropServices import _Attribute
from System.Runtime.Remoting.Contexts import Context
from System.Runtime.Remoting.Contexts import ContextAttribute
from System.Runtime.Remoting.Contexts import IContextAttribute
from System.Runtime.Remoting.Contexts import IContextProperty
from System.Runtime.Remoting.Messaging import IMessage
from System.Runtime.Remoting.Messaging import IMethodCallMessage
from System.Runtime.Remoting.Messaging import IMethodMessage
from System.Runtime.Remoting.Messaging import IMethodReturnMessage

# ---------- Types ---------- #

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
IntType = Union[int, Int32]
ObjectType = Object
StringType = Union[str, String]
TypeType = Union[type, Type]
VoidType = Union[None, Void]

# ---------- Classes ---------- #

class ActivationAttributeStack(ObjectType):
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

class ActivationListener(MarshalByRefObject, IActivator):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # ---------- Properties ---------- #

    @property
    def Level(self) -> ActivatorLevel: ...
    @property
    def NextActivator(self) -> IActivator: ...
    @NextActivator.setter
    def NextActivator(self, value: IActivator) -> None: ...

    # ---------- Methods ---------- #

    def Activate(self, ctorMsg: IConstructionCallMessage) -> IConstructionReturnMessage: ...
    def InitializeLifetimeService(self) -> ObjectType: ...
    def get_Level(self) -> ActivatorLevel: ...
    def get_NextActivator(self) -> IActivator: ...
    def set_NextActivator(self, value: IActivator) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ActivationServices(ABC, ObjectType):
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

class AppDomainLevelActivator(ObjectType, IActivator):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def Level(self) -> ActivatorLevel: ...
    @property
    def NextActivator(self) -> IActivator: ...
    @NextActivator.setter
    def NextActivator(self, value: IActivator) -> None: ...

    # ---------- Methods ---------- #

    def Activate(self, ctorMsg: IConstructionCallMessage) -> IConstructionReturnMessage: ...
    def get_Level(self) -> ActivatorLevel: ...
    def get_NextActivator(self) -> IActivator: ...
    def set_NextActivator(self, value: IActivator) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ConstructionLevelActivator(ObjectType, IActivator):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def Level(self) -> ActivatorLevel: ...
    @property
    def NextActivator(self) -> IActivator: ...
    @NextActivator.setter
    def NextActivator(self, value: IActivator) -> None: ...

    # ---------- Methods ---------- #

    def Activate(self, ctorMsg: IConstructionCallMessage) -> IConstructionReturnMessage: ...
    def get_Level(self) -> ActivatorLevel: ...
    def get_NextActivator(self) -> IActivator: ...
    def set_NextActivator(self, value: IActivator) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ContextLevelActivator(ObjectType, IActivator):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def Level(self) -> ActivatorLevel: ...
    @property
    def NextActivator(self) -> IActivator: ...
    @NextActivator.setter
    def NextActivator(self, value: IActivator) -> None: ...

    # ---------- Methods ---------- #

    def Activate(self, ctorMsg: IConstructionCallMessage) -> IConstructionReturnMessage: ...
    def get_Level(self) -> ActivatorLevel: ...
    def get_NextActivator(self) -> IActivator: ...
    def set_NextActivator(self, value: IActivator) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class LocalActivator(ContextAttribute, _Attribute, IContextAttribute, IContextProperty, IActivator):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def Level(self) -> ActivatorLevel: ...
    @property
    def NextActivator(self) -> IActivator: ...
    @NextActivator.setter
    def NextActivator(self, value: IActivator) -> None: ...

    # ---------- Methods ---------- #

    def Activate(self, ctorMsg: IConstructionCallMessage) -> IConstructionReturnMessage: ...
    def GetPropertiesForNewContext(self, ctorMsg: IConstructionCallMessage) -> VoidType: ...
    def IsContextOK(self, ctx: Context, ctorMsg: IConstructionCallMessage) -> BooleanType: ...
    def get_Level(self) -> ActivatorLevel: ...
    def get_NextActivator(self) -> IActivator: ...
    def set_NextActivator(self, value: IActivator) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class RemotePropertyHolderAttribute(ObjectType, IContextAttribute):
    # No Fields

    # No Constructors

    # No Properties

    # ---------- Methods ---------- #

    def GetPropertiesForNewContext(self, ctorMsg: IConstructionCallMessage) -> VoidType: ...
    def IsContextOK(self, ctx: Context, msg: IConstructionCallMessage) -> BooleanType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class RemotingXmlConfigFileData(ObjectType):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # No Properties

    # No Methods

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class RemotingXmlConfigFileParser(ABC, ObjectType):
    # No Fields

    # No Constructors

    # No Properties

    # ---------- Methods ---------- #

    @staticmethod
    def ParseConfigFile(filename: StringType) -> RemotingXmlConfigFileData: ...
    @staticmethod
    def ParseDefaultConfiguration() -> RemotingXmlConfigFileData: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class UrlAttribute(ContextAttribute, _Attribute, IContextAttribute, IContextProperty):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, callsiteURL: StringType): ...

    # ---------- Properties ---------- #

    @property
    def UrlValue(self) -> StringType: ...

    # ---------- Methods ---------- #

    def Equals(self, o: ObjectType) -> BooleanType: ...
    def GetHashCode(self) -> IntType: ...
    def GetPropertiesForNewContext(self, ctorMsg: IConstructionCallMessage) -> VoidType: ...
    def IsContextOK(self, ctx: Context, msg: IConstructionCallMessage) -> BooleanType: ...
    def get_UrlValue(self) -> StringType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

# No Structs

# ---------- Interfaces ---------- #

class IActivator(Protocol):
    # ---------- Properties ---------- #

    @property
    def Level(self) -> ActivatorLevel: ...
    @property
    def NextActivator(self) -> IActivator: ...
    @NextActivator.setter
    def NextActivator(self, value: IActivator) -> None: ...

    # ---------- Methods ---------- #

    def Activate(self, msg: IConstructionCallMessage) -> IConstructionReturnMessage: ...
    def get_Level(self) -> ActivatorLevel: ...
    def get_NextActivator(self) -> IActivator: ...
    def set_NextActivator(self, value: IActivator) -> VoidType: ...

    # No Events

class IConstructionCallMessage(Protocol, IMethodCallMessage, IMethodMessage, IMessage):
    # ---------- Properties ---------- #

    @property
    def ActivationType(self) -> TypeType: ...
    @property
    def ActivationTypeName(self) -> StringType: ...
    @property
    def Activator(self) -> IActivator: ...
    @Activator.setter
    def Activator(self, value: IActivator) -> None: ...
    @property
    def CallSiteActivationAttributes(self) -> ArrayType[ObjectType]: ...
    @property
    def ContextProperties(self) -> IList: ...

    # ---------- Methods ---------- #

    def get_ActivationType(self) -> TypeType: ...
    def get_ActivationTypeName(self) -> StringType: ...
    def get_Activator(self) -> IActivator: ...
    def get_CallSiteActivationAttributes(self) -> ArrayType[ObjectType]: ...
    def get_ContextProperties(self) -> IList: ...
    def set_Activator(self, value: IActivator) -> VoidType: ...

    # No Events

class IConstructionReturnMessage(Protocol, IMethodReturnMessage, IMethodMessage, IMessage):
    """"""

    # No Properties

    # No Methods

    # No Events

# ---------- Enums ---------- #

class ActivatorLevel(Enum):
    Construction = 4
    Context = 8
    AppDomain = 12
    Process = 16
    Machine = 20

# No Delegates

__all__ = [
    ActivationAttributeStack,
    ActivationListener,
    ActivationServices,
    AppDomainLevelActivator,
    ConstructionLevelActivator,
    ContextLevelActivator,
    LocalActivator,
    RemotePropertyHolderAttribute,
    RemotingXmlConfigFileData,
    RemotingXmlConfigFileParser,
    UrlAttribute,
    IActivator,
    IConstructionCallMessage,
    IConstructionReturnMessage,
    ActivatorLevel,
]
