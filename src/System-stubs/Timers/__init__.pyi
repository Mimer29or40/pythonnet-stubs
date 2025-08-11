"""Automatically generated stubs for C# namespace: System.Timers."""

from collections.abc import Callable
from typing import Self
from typing import overload

from System import DateTime
from System import EventArgs
from System import EventHandler
from System import Guid
from System import IDisposable
from System import IntPtr
from System import Type
from System import UInt32
from System.ComponentModel import Component
from System.ComponentModel import DescriptionAttribute
from System.ComponentModel import IComponent
from System.ComponentModel import IContainer
from System.ComponentModel import ISite
from System.ComponentModel import ISupportInitialize
from System.ComponentModel import ISynchronizeInvoke
from System.Runtime.InteropServices import _Attribute
from System.Runtime.Remoting import ObjRef

class EventType[T]:
    def __iadd__(self, other: T) -> Self: ...
    def __isub__(self, other: T) -> Self: ...

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ElapsedEventArgs(EventArgs):
    """"""
    @property
    def SignalTime(self) -> DateTime:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

type ElapsedEventHandler = Callable[[object, ElapsedEventArgs], None]
""""""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class Timer(Component, IComponent, ISupportInitialize, IDisposable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, interval: float) -> None:
        """"""
    @property
    def AutoReset(self) -> bool:
        """"""
    @AutoReset.setter
    def AutoReset(self, value: bool) -> None: ...
    @property
    def Container(self) -> IContainer:
        """"""
    @property
    def Enabled(self) -> bool:
        """"""
    @Enabled.setter
    def Enabled(self, value: bool) -> None: ...
    @property
    def Interval(self) -> float:
        """"""
    @Interval.setter
    def Interval(self, value: float) -> None: ...
    @property
    def Site(self) -> ISite:
        """"""
    @Site.setter
    def Site(self, value: ISite) -> None: ...
    @property
    def SynchronizingObject(self) -> ISynchronizeInvoke:
        """"""
    @SynchronizingObject.setter
    def SynchronizingObject(self, value: ISynchronizeInvoke) -> None: ...
    def BeginInit(self) -> None:
        """"""
    def Close(self) -> None:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    def Dispose(self) -> None:
        """"""
    def EndInit(self) -> None:
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
    def Start(self) -> None:
        """"""
    def Stop(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    Disposed: EventType[EventHandler] = ...
    """"""
    Elapsed: EventType[ElapsedEventHandler] = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class TimersDescriptionAttribute(DescriptionAttribute, _Attribute):
    """"""
    def __init__(self, description: str) -> None:
        """"""
    @property
    def Description(self) -> str:
        """"""
    @property
    def TypeId(self) -> object:
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
