from __future__ import annotations

from abc import ABC
from typing import Tuple

from System import Array
from System import Enum
from System import Exception
from System import Guid
from System import IntPtr
from System import MarshalByRefObject
from System import Object
from System import Type
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

class ActivationAttributeStack(Object):
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

class ActivationListener(MarshalByRefObject, IActivator):
    """"""

    def __init__(self):
        """"""
    @property
    def Level(self) -> ActivatorLevel:
        """

        :return:
        """
    @property
    def NextActivator(self) -> IActivator:
        """

        :return:
        """
    @NextActivator.setter
    def NextActivator(self, value: IActivator) -> None: ...
    def Activate(self, msg: IConstructionCallMessage) -> IConstructionReturnMessage:
        """

        :param msg:
        :return:
        """
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """

        :param requestedType:
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
    def GetLifetimeService(self) -> object:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def InitializeLifetimeService(self) -> object:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class ActivationServices(ABC, Object):
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

class AppDomainLevelActivator(Object, IActivator):
    """"""

    @property
    def Level(self) -> ActivatorLevel:
        """

        :return:
        """
    @property
    def NextActivator(self) -> IActivator:
        """

        :return:
        """
    @NextActivator.setter
    def NextActivator(self, value: IActivator) -> None: ...
    def Activate(self, msg: IConstructionCallMessage) -> IConstructionReturnMessage:
        """

        :param msg:
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

class ConstructionLevelActivator(Object, IActivator):
    """"""

    @property
    def Level(self) -> ActivatorLevel:
        """

        :return:
        """
    @property
    def NextActivator(self) -> IActivator:
        """

        :return:
        """
    @NextActivator.setter
    def NextActivator(self, value: IActivator) -> None: ...
    def Activate(self, msg: IConstructionCallMessage) -> IConstructionReturnMessage:
        """

        :param msg:
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

class ContextLevelActivator(Object, IActivator):
    """"""

    @property
    def Level(self) -> ActivatorLevel:
        """

        :return:
        """
    @property
    def NextActivator(self) -> IActivator:
        """

        :return:
        """
    @NextActivator.setter
    def NextActivator(self, value: IActivator) -> None: ...
    def Activate(self, msg: IConstructionCallMessage) -> IConstructionReturnMessage:
        """

        :param msg:
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

class IActivator:
    """"""

    @property
    def Level(self) -> ActivatorLevel:
        """

        :return:
        """
    @property
    def NextActivator(self) -> IActivator:
        """

        :return:
        """
    @NextActivator.setter
    def NextActivator(self, value: IActivator) -> None: ...
    def Activate(self, msg: IConstructionCallMessage) -> IConstructionReturnMessage:
        """

        :param msg:
        :return:
        """

class IConstructionCallMessage(IMessage, IMethodCallMessage, IMethodMessage):
    """"""

    @property
    def ActivationType(self) -> Type:
        """

        :return:
        """
    @property
    def ActivationTypeName(self) -> str:
        """

        :return:
        """
    @property
    def Activator(self) -> IActivator:
        """

        :return:
        """
    @Activator.setter
    def Activator(self, value: IActivator) -> None: ...
    @property
    def ArgCount(self) -> int:
        """

        :return:
        """
    @property
    def Args(self) -> Array[object]:
        """

        :return:
        """
    @property
    def CallSiteActivationAttributes(self) -> Array[object]:
        """

        :return:
        """
    @property
    def ContextProperties(self) -> IList:
        """

        :return:
        """
    @property
    def HasVarArgs(self) -> bool:
        """

        :return:
        """
    @property
    def InArgCount(self) -> int:
        """

        :return:
        """
    @property
    def InArgs(self) -> Array[object]:
        """

        :return:
        """
    @property
    def LogicalCallContext(self) -> LogicalCallContext:
        """

        :return:
        """
    @property
    def MethodBase(self) -> MethodBase:
        """

        :return:
        """
    @property
    def MethodName(self) -> str:
        """

        :return:
        """
    @property
    def MethodSignature(self) -> object:
        """

        :return:
        """
    @property
    def Properties(self) -> IDictionary:
        """

        :return:
        """
    @property
    def TypeName(self) -> str:
        """

        :return:
        """
    @property
    def Uri(self) -> str:
        """

        :return:
        """
    def GetArg(self, argNum: int) -> object:
        """

        :param argNum:
        :return:
        """
    def GetArgName(self, index: int) -> str:
        """

        :param index:
        :return:
        """
    def GetInArg(self, argNum: int) -> object:
        """

        :param argNum:
        :return:
        """
    def GetInArgName(self, index: int) -> str:
        """

        :param index:
        :return:
        """

class IConstructionReturnMessage(IMessage, IMethodMessage, IMethodReturnMessage):
    """"""

    @property
    def ArgCount(self) -> int:
        """

        :return:
        """
    @property
    def Args(self) -> Array[object]:
        """

        :return:
        """
    @property
    def Exception(self) -> Exception:
        """

        :return:
        """
    @property
    def HasVarArgs(self) -> bool:
        """

        :return:
        """
    @property
    def LogicalCallContext(self) -> LogicalCallContext:
        """

        :return:
        """
    @property
    def MethodBase(self) -> MethodBase:
        """

        :return:
        """
    @property
    def MethodName(self) -> str:
        """

        :return:
        """
    @property
    def MethodSignature(self) -> object:
        """

        :return:
        """
    @property
    def OutArgCount(self) -> int:
        """

        :return:
        """
    @property
    def OutArgs(self) -> Array[object]:
        """

        :return:
        """
    @property
    def Properties(self) -> IDictionary:
        """

        :return:
        """
    @property
    def ReturnValue(self) -> object:
        """

        :return:
        """
    @property
    def TypeName(self) -> str:
        """

        :return:
        """
    @property
    def Uri(self) -> str:
        """

        :return:
        """
    def GetArg(self, argNum: int) -> object:
        """

        :param argNum:
        :return:
        """
    def GetArgName(self, index: int) -> str:
        """

        :param index:
        :return:
        """
    def GetOutArg(self, argNum: int) -> object:
        """

        :param argNum:
        :return:
        """
    def GetOutArgName(self, index: int) -> str:
        """

        :param index:
        :return:
        """

class LocalActivator(ContextAttribute, _Attribute, IActivator, IContextAttribute, IContextProperty):
    """"""

    @property
    def Level(self) -> ActivatorLevel:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def NextActivator(self) -> IActivator:
        """

        :return:
        """
    @NextActivator.setter
    def NextActivator(self, value: IActivator) -> None: ...
    @property
    def TypeId(self) -> object:
        """

        :return:
        """
    def Activate(self, msg: IConstructionCallMessage) -> IConstructionReturnMessage:
        """

        :param msg:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def Freeze(self, newContext: Context) -> None:
        """

        :param newContext:
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
    def GetPropertiesForNewContext(self, msg: IConstructionCallMessage) -> None:
        """

        :param msg:
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
    def IsContextOK(self, ctx: Context, msg: IConstructionCallMessage) -> bool:
        """

        :param ctx:
        :param msg:
        :return:
        """
    def IsDefaultAttribute(self) -> bool:
        """

        :return:
        """
    def IsNewContextOK(self, newCtx: Context) -> bool:
        """

        :param newCtx:
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

class RemotePropertyHolderAttribute(Object, IContextAttribute):
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
    def GetPropertiesForNewContext(self, msg: IConstructionCallMessage) -> None:
        """

        :param msg:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def IsContextOK(self, ctx: Context, msg: IConstructionCallMessage) -> bool:
        """

        :param ctx:
        :param msg:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class RemotingXmlConfigFileData(Object):
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

class RemotingXmlConfigFileParser(ABC, Object):
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
    @classmethod
    def ParseConfigFile(cls, filename: str) -> RemotingXmlConfigFileData:
        """

        :param filename:
        :return:
        """
    @classmethod
    def ParseDefaultConfiguration(cls) -> RemotingXmlConfigFileData:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class UrlAttribute(ContextAttribute, _Attribute, IContextAttribute, IContextProperty):
    """"""

    def __init__(self, callsiteURL: str):
        """

        :param callsiteURL:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def TypeId(self) -> object:
        """

        :return:
        """
    @property
    def UrlValue(self) -> str:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def Freeze(self, newContext: Context) -> None:
        """

        :param newContext:
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
    def GetPropertiesForNewContext(self, msg: IConstructionCallMessage) -> None:
        """

        :param msg:
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
    def IsContextOK(self, ctx: Context, msg: IConstructionCallMessage) -> bool:
        """

        :param ctx:
        :param msg:
        :return:
        """
    def IsDefaultAttribute(self) -> bool:
        """

        :return:
        """
    def IsNewContextOK(self, newCtx: Context) -> bool:
        """

        :param newCtx:
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
