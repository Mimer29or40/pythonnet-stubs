from __future__ import annotations

from typing import overload

from System import Array
from System import Object
from System import Type
from System.Threading import IThreadPoolWorkItem
from System.Threading import ThreadAbortException
from System.Threading import WaitHandle

class TimerQueue(Object):
    """"""

    @classmethod
    @property
    def Instances(cls) -> Array[TimerQueue]:
        """

        :return:
        """
    def DeleteTimer(self, timer: TimerQueueTimer) -> None:
        """

        :param timer:
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
    def MoveTimerToCorrectList(self, timer: TimerQueueTimer, shortList: bool) -> None:
        """

        :param timer:
        :param shortList:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def UpdateTimer(self, timer: TimerQueueTimer, dueTime: int, period: int) -> bool:
        """

        :param timer:
        :param dueTime:
        :param period:
        :return:
        """

class TimerQueueTimer(Object, IThreadPoolWorkItem):
    """"""

    @overload
    def Close(self) -> None:
        """"""
    @overload
    def Close(self, toSignal: WaitHandle) -> bool:
        """

        :param toSignal:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ExecuteWorkItem(self) -> None:
        """"""
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def MarkAborted(self, tae: ThreadAbortException) -> None:
        """

        :param tae:
        """
    def ToString(self) -> str:
        """

        :return:
        """
