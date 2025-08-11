"""Automatically generated stubs for C# namespace: System.Runtime.Remoting.Contexts."""

from abc import ABC
from collections.abc import Callable
from typing import ClassVar
from typing import overload

from System import Array
from System import Attribute
from System import ContextBoundObject
from System import Guid
from System import IntPtr
from System import LocalDataStoreSlot
from System import MarshalByRefObject
from System import Object
from System import Type
from System import UInt32
from System.Runtime.InteropServices import _Attribute
from System.Runtime.Remoting.Activation import IConstructionCallMessage
from System.Runtime.Remoting.Activation import IConstructionReturnMessage
from System.Runtime.Remoting.Messaging import IMessage
from System.Runtime.Remoting.Messaging import IMessageCtrl
from System.Runtime.Remoting.Messaging import IMessageSink
from System.Runtime.Remoting.Messaging import InternalSink

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ArrayWithSize(Object):
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
class CallBackHelper(Object):
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
class Context(Object):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def ContextID(self) -> int:
        """"""
    @property
    def ContextProperties(self) -> Array[IContextProperty]:
        """"""
    @classmethod
    @property
    def DefaultContext(cls) -> Context:
        """"""
    @classmethod
    def AllocateDataSlot(cls) -> LocalDataStoreSlot:
        """"""
    @classmethod
    def AllocateNamedDataSlot(cls, name: str) -> LocalDataStoreSlot:
        """"""
    def DoCallBack(self, deleg: CrossContextDelegate) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def FreeNamedDataSlot(cls, name: str) -> None:
        """"""
    def Freeze(self) -> None:
        """"""
    @classmethod
    def GetData(cls, slot: LocalDataStoreSlot) -> object:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @classmethod
    def GetNamedDataSlot(cls, name: str) -> LocalDataStoreSlot:
        """"""
    def GetProperty(self, name: str) -> IContextProperty:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def RegisterDynamicProperty(
        cls, prop: IDynamicProperty, obj: ContextBoundObject, ctx: Context
    ) -> bool:
        """"""
    @classmethod
    def SetData(cls, slot: LocalDataStoreSlot, data: object) -> None:
        """"""
    def SetProperty(self, prop: IContextProperty) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def UnregisterDynamicProperty(cls, name: str, obj: ContextBoundObject, ctx: Context) -> bool:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ContextAttribute(Attribute, _Attribute, IContextAttribute, IContextProperty):
    """"""
    def __init__(self, name: str) -> None:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def TypeId(self) -> object:
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
class ContextProperty(Object):
    """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def Property(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

type CrossContextDelegate = Callable[[], None]
""""""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class DynamicPropertyHolder(Object):
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
class IContextAttribute(ABC):
    """"""
    def GetPropertiesForNewContext(self, msg: IConstructionCallMessage) -> None:
        """"""
    def IsContextOK(self, ctx: Context, msg: IConstructionCallMessage) -> bool:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IContextProperty(ABC):
    """"""
    @property
    def Name(self) -> str:
        """"""
    def Freeze(self, newContext: Context) -> None:
        """"""
    def IsNewContextOK(self, newCtx: Context) -> bool:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IContextPropertyActivator(ABC):
    """"""
    def CollectFromClientContext(self, msg: IConstructionCallMessage) -> None:
        """"""
    def CollectFromServerContext(self, msg: IConstructionReturnMessage) -> None:
        """"""
    def DeliverClientContextToServerContext(self, msg: IConstructionCallMessage) -> bool:
        """"""
    def DeliverServerContextToClientContext(self, msg: IConstructionReturnMessage) -> bool:
        """"""
    def IsOKToActivate(self, msg: IConstructionCallMessage) -> bool:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IContributeClientContextSink(ABC):
    """"""
    def GetClientContextSink(self, nextSink: IMessageSink) -> IMessageSink:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IContributeDynamicSink(ABC):
    """"""
    def GetDynamicSink(self) -> IDynamicMessageSink:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IContributeEnvoySink(ABC):
    """"""
    def GetEnvoySink(self, obj: MarshalByRefObject, nextSink: IMessageSink) -> IMessageSink:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IContributeObjectSink(ABC):
    """"""
    def GetObjectSink(self, obj: MarshalByRefObject, nextSink: IMessageSink) -> IMessageSink:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IContributeServerContextSink(ABC):
    """"""
    def GetServerContextSink(self, nextSink: IMessageSink) -> IMessageSink:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IDynamicMessageSink(ABC):
    """"""
    def ProcessMessageFinish(self, replyMsg: IMessage, bCliSide: bool, bAsync: bool) -> None:
        """"""
    def ProcessMessageStart(self, reqMsg: IMessage, bCliSide: bool, bAsync: bool) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IDynamicProperty(ABC):
    """"""
    @property
    def Name(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SynchronizationAttribute(
    ContextAttribute,
    _Attribute,
    IContextAttribute,
    IContextProperty,
    IContributeClientContextSink,
    IContributeServerContextSink,
):
    """"""

    NOT_SUPPORTED: ClassVar[int]
    """"""
    REQUIRED: ClassVar[int]
    """"""
    REQUIRES_NEW: ClassVar[int]
    """"""
    SUPPORTED: ClassVar[int]
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, reEntrant: bool) -> None:
        """"""
    @overload
    def __init__(self, flag: int) -> None:
        """"""
    @overload
    def __init__(self, flag: int, reEntrant: bool) -> None:
        """"""
    @property
    def IsReEntrant(self) -> bool:
        """"""
    @property
    def Locked(self) -> bool:
        """"""
    @Locked.setter
    def Locked(self, value: bool) -> None: ...
    @property
    def Name(self) -> str:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
    def Equals(self, o: object) -> bool:
        """"""
    def Freeze(self, newContext: Context) -> None:
        """"""
    def GetClientContextSink(self, nextSink: IMessageSink) -> IMessageSink:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    def GetPropertiesForNewContext(self, ctorMsg: IConstructionCallMessage) -> None:
        """"""
    def GetServerContextSink(self, nextSink: IMessageSink) -> IMessageSink:
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SynchronizedClientContextSink(InternalSink, IMessageSink):
    """"""
    @property
    def NextSink(self) -> IMessageSink:
        """"""
    def AsyncProcessMessage(self, reqMsg: IMessage, replySink: IMessageSink) -> IMessageCtrl:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def SyncProcessMessage(self, reqMsg: IMessage) -> IMessage:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SynchronizedServerContextSink(InternalSink, IMessageSink):
    """"""
    @property
    def NextSink(self) -> IMessageSink:
        """"""
    def AsyncProcessMessage(self, reqMsg: IMessage, replySink: IMessageSink) -> IMessageCtrl:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def SyncProcessMessage(self, reqMsg: IMessage) -> IMessage:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class WorkItem(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
