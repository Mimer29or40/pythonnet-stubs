"""Automatically generated stubs for C# namespace: System.Threading.NetCore."""

from typing import overload

from System import Array
from System import Object
from System import Type
from System.Threading import IThreadPoolWorkItem
from System.Threading import ThreadAbortException
from System.Threading import WaitHandle

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class TimerQueue(Object):
    """"""
    @classmethod
    @property
    def Instances(cls) -> Array[TimerQueue]:
        """"""
    def DeleteTimer(self, timer: TimerQueueTimer) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def MoveTimerToCorrectList(self, timer: TimerQueueTimer, shortList: bool) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def UpdateTimer(self, timer: TimerQueueTimer, dueTime: int, period: int) -> bool:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class TimerQueueTimer(Object, IThreadPoolWorkItem):
    """"""
    @overload
    def Close(self) -> None:
        """"""
    @overload
    def Close(self, toSignal: WaitHandle) -> bool:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def ExecuteWorkItem(self) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def MarkAborted(self, tae: ThreadAbortException) -> None:
        """"""
    def ToString(self) -> str:
        """"""
