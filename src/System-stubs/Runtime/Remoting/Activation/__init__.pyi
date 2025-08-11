"""Automatically generated stubs for C# namespace: System.Runtime.Remoting.Activation."""

from abc import ABC

from System import Array
from System import Enum
from System import Exception
from System import Guid
from System import IntPtr
from System import MarshalByRefObject
from System import Object
from System import Type
from System import UInt32
from System.Collections import IDictionary
from System.Collections import IList
from System.Reflection import MethodBase
from System.Runtime.InteropServices import _Attribute
from System.Runtime.Remoting import ObjRef
from System.Runtime.Remoting.Contexts import Context
from System.Runtime.Remoting.Contexts import ContextAttribute
from System.Runtime.Remoting.Contexts import IContextAttribute
from System.Runtime.Remoting.Contexts import IContextProperty
from System.Runtime.Remoting.Messaging import IMessage
from System.Runtime.Remoting.Messaging import IMethodCallMessage
from System.Runtime.Remoting.Messaging import IMethodMessage
from System.Runtime.Remoting.Messaging import IMethodReturnMessage
from System.Runtime.Remoting.Messaging import LogicalCallContext

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ActivationAttributeStack(Object):
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
class ActivationListener(MarshalByRefObject, IActivator):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Level(self) -> ActivatorLevel:
        """"""
    @property
    def NextActivator(self) -> IActivator:
        """"""
    @NextActivator.setter
    def NextActivator(self, value: IActivator) -> None: ...
    def Activate(self, ctorMsg: IConstructionCallMessage) -> IConstructionReturnMessage:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetLifetimeService(self) -> object:
        """"""
    def GetType(self) -> Type:
        """"""
    def InitializeLifetimeService(self) -> object:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ActivationServices(ABC, Object):
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
class ActivatorLevel(Enum):
    """"""

    Construction: ActivatorLevel = ...
    """"""
    Context: ActivatorLevel = ...
    """"""
    AppDomain: ActivatorLevel = ...
    """"""
    Process: ActivatorLevel = ...
    """"""
    Machine: ActivatorLevel = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class AppDomainLevelActivator(Object, IActivator):
    """"""
    @property
    def Level(self) -> ActivatorLevel:
        """"""
    @property
    def NextActivator(self) -> IActivator:
        """"""
    @NextActivator.setter
    def NextActivator(self, value: IActivator) -> None: ...
    def Activate(self, ctorMsg: IConstructionCallMessage) -> IConstructionReturnMessage:
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
class ConstructionLevelActivator(Object, IActivator):
    """"""
    @property
    def Level(self) -> ActivatorLevel:
        """"""
    @property
    def NextActivator(self) -> IActivator:
        """"""
    @NextActivator.setter
    def NextActivator(self, value: IActivator) -> None: ...
    def Activate(self, ctorMsg: IConstructionCallMessage) -> IConstructionReturnMessage:
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
class ContextLevelActivator(Object, IActivator):
    """"""
    @property
    def Level(self) -> ActivatorLevel:
        """"""
    @property
    def NextActivator(self) -> IActivator:
        """"""
    @NextActivator.setter
    def NextActivator(self, value: IActivator) -> None: ...
    def Activate(self, ctorMsg: IConstructionCallMessage) -> IConstructionReturnMessage:
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
class IActivator(ABC):
    """"""
    @property
    def Level(self) -> ActivatorLevel:
        """"""
    @property
    def NextActivator(self) -> IActivator:
        """"""
    @NextActivator.setter
    def NextActivator(self, value: IActivator) -> None: ...
    def Activate(self, msg: IConstructionCallMessage) -> IConstructionReturnMessage:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IConstructionCallMessage(ABC, IMessage, IMethodCallMessage, IMethodMessage):
    """"""
    @property
    def ActivationType(self) -> Type:
        """"""
    @property
    def ActivationTypeName(self) -> str:
        """"""
    @property
    def Activator(self) -> IActivator:
        """"""
    @Activator.setter
    def Activator(self, value: IActivator) -> None: ...
    @property
    def ArgCount(self) -> int:
        """"""
    @property
    def Args(self) -> Array[object]:
        """"""
    @property
    def CallSiteActivationAttributes(self) -> Array[object]:
        """"""
    @property
    def ContextProperties(self) -> IList:
        """"""
    @property
    def HasVarArgs(self) -> bool:
        """"""
    @property
    def InArgCount(self) -> int:
        """"""
    @property
    def InArgs(self) -> Array[object]:
        """"""
    @property
    def LogicalCallContext(self) -> LogicalCallContext:
        """"""
    @property
    def MethodBase(self) -> MethodBase:
        """"""
    @property
    def MethodName(self) -> str:
        """"""
    @property
    def MethodSignature(self) -> object:
        """"""
    @property
    def Properties(self) -> IDictionary:
        """"""
    @property
    def TypeName(self) -> str:
        """"""
    @property
    def Uri(self) -> str:
        """"""
    def GetArg(self, argNum: int) -> object:
        """"""
    def GetArgName(self, index: int) -> str:
        """"""
    def GetInArg(self, argNum: int) -> object:
        """"""
    def GetInArgName(self, index: int) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IConstructionReturnMessage(ABC, IMessage, IMethodMessage, IMethodReturnMessage):
    """"""
    @property
    def ArgCount(self) -> int:
        """"""
    @property
    def Args(self) -> Array[object]:
        """"""
    @property
    def Exception(self) -> Exception:
        """"""
    @property
    def HasVarArgs(self) -> bool:
        """"""
    @property
    def LogicalCallContext(self) -> LogicalCallContext:
        """"""
    @property
    def MethodBase(self) -> MethodBase:
        """"""
    @property
    def MethodName(self) -> str:
        """"""
    @property
    def MethodSignature(self) -> object:
        """"""
    @property
    def OutArgCount(self) -> int:
        """"""
    @property
    def OutArgs(self) -> Array[object]:
        """"""
    @property
    def Properties(self) -> IDictionary:
        """"""
    @property
    def ReturnValue(self) -> object:
        """"""
    @property
    def TypeName(self) -> str:
        """"""
    @property
    def Uri(self) -> str:
        """"""
    def GetArg(self, argNum: int) -> object:
        """"""
    def GetArgName(self, index: int) -> str:
        """"""
    def GetOutArg(self, argNum: int) -> object:
        """"""
    def GetOutArgName(self, index: int) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class LocalActivator(ContextAttribute, _Attribute, IActivator, IContextAttribute, IContextProperty):
    """"""
    @property
    def Level(self) -> ActivatorLevel:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def NextActivator(self) -> IActivator:
        """"""
    @NextActivator.setter
    def NextActivator(self, value: IActivator) -> None: ...
    @property
    def TypeId(self) -> object:
        """"""
    def Activate(self, ctorMsg: IConstructionCallMessage) -> IConstructionReturnMessage:
        """"""
    def Equals(self, o: object) -> bool:
        """"""
    def Freeze(self, newContext: Context) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    def GetPropertiesForNewContext(self, ctorMsg: IConstructionCallMessage) -> None:
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
    def IsContextOK(self, ctx: Context, ctorMsg: IConstructionCallMessage) -> bool:
        """"""
    def IsDefaultAttribute(self) -> bool:
        """"""
    def IsNewContextOK(self, newCtx: Context) -> bool:
        """"""
    def Match(self, obj: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class RemotePropertyHolderAttribute(Object, IContextAttribute):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetPropertiesForNewContext(self, ctorMsg: IConstructionCallMessage) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def IsContextOK(self, ctx: Context, msg: IConstructionCallMessage) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class RemotingXmlConfigFileData(Object):
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
class RemotingXmlConfigFileParser(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def ParseConfigFile(cls, filename: str) -> RemotingXmlConfigFileData:
        """"""
    @classmethod
    def ParseDefaultConfiguration(cls) -> RemotingXmlConfigFileData:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class UrlAttribute(ContextAttribute, _Attribute, IContextAttribute, IContextProperty):
    """"""
    def __init__(self, callsiteURL: str) -> None:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
    @property
    def UrlValue(self) -> str:
        """"""
    def Equals(self, o: object) -> bool:
        """"""
    def Freeze(self, newContext: Context) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    def GetPropertiesForNewContext(self, ctorMsg: IConstructionCallMessage) -> None:
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
    def IsContextOK(self, ctx: Context, msg: IConstructionCallMessage) -> bool:
        """"""
    def IsDefaultAttribute(self) -> bool:
        """"""
    def IsNewContextOK(self, newCtx: Context) -> bool:
        """"""
    def Match(self, obj: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
