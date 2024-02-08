from __future__ import annotations

from typing import Callable
from typing import Generic
from typing import Tuple
from typing import TypeVar
from typing import overload

from System import DateTime
from System import EventArgs
from System import EventHandler
from System import Guid
from System import IDisposable
from System import IntPtr
from System import Type
from System.ComponentModel import Component
from System.ComponentModel import DescriptionAttribute
from System.ComponentModel import IComponent
from System.ComponentModel import IContainer
from System.ComponentModel import ISite
from System.ComponentModel import ISupportInitialize
from System.ComponentModel import ISynchronizeInvoke
from System.Runtime.InteropServices import _Attribute
from System.Runtime.Remoting import ObjRef

T = TypeVar("T")

class EventType(Generic[T]):
    def __iadd__(self, other: T): ...
    def __isub__(self, other: T): ...

class ElapsedEventArgs(EventArgs):
    """"""

    @property
    def SignalTime(self) -> DateTime:
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

ElapsedEventHandler: Callable[[object, ElapsedEventArgs], None] = ...
"""

:param sender: 
:param e: 
"""

class Timer(Component, IComponent, ISupportInitialize, IDisposable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, interval: float):
        """

        :param interval:
        """
    @property
    def AutoReset(self) -> bool:
        """

        :return:
        """
    @AutoReset.setter
    def AutoReset(self, value: bool) -> None: ...
    @property
    def Container(self) -> IContainer:
        """

        :return:
        """
    @property
    def Enabled(self) -> bool:
        """

        :return:
        """
    @Enabled.setter
    def Enabled(self, value: bool) -> None: ...
    @property
    def Interval(self) -> float:
        """

        :return:
        """
    @Interval.setter
    def Interval(self, value: float) -> None: ...
    @property
    def Site(self) -> ISite:
        """

        :return:
        """
    @Site.setter
    def Site(self, value: ISite) -> None: ...
    @property
    def SynchronizingObject(self) -> ISynchronizeInvoke:
        """

        :return:
        """
    @SynchronizingObject.setter
    def SynchronizingObject(self, value: ISynchronizeInvoke) -> None: ...
    def BeginInit(self) -> None:
        """"""
    def Close(self) -> None:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """

        :param requestedType:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    def EndInit(self) -> None:
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
    def Start(self) -> None:
        """"""
    def Stop(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """
    Disposed: EventType[EventHandler] = ...
    """"""
    Elapsed: EventType[ElapsedEventHandler] = ...
    """"""

class TimersDescriptionAttribute(DescriptionAttribute, _Attribute):
    """"""

    def __init__(self, description: str):
        """

        :param description:
        """
    @property
    def Description(self) -> str:
        """

        :return:
        """
    @property
    def TypeId(self) -> object:
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
