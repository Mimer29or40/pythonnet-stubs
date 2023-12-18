from __future__ import annotations

from typing import List
from typing import Union
from typing import overload

from System import Array
from System import Boolean
from System import Object
from System import UInt32
from System import Void
from System.Threading import IThreadPoolWorkItem
from System.Threading import WaitHandle

# ---------- Types ---------- #

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
ObjectType = Object
UIntType = Union[int, UInt32]
VoidType = Union[None, Void]

# ---------- Classes ---------- #

class TimerQueue(ObjectType):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @staticmethod
    @property
    def Instances() -> ArrayType[TimerQueue]: ...

    # ---------- Methods ---------- #

    def DeleteTimer(self, timer: TimerQueueTimer) -> VoidType: ...
    def MoveTimerToCorrectList(
        self, timer: TimerQueueTimer, shortList: BooleanType
    ) -> VoidType: ...
    def UpdateTimer(
        self, timer: TimerQueueTimer, dueTime: UIntType, period: UIntType
    ) -> BooleanType: ...
    @staticmethod
    def get_Instances() -> ArrayType[TimerQueue]: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class TimerQueueTimer(ObjectType, IThreadPoolWorkItem):
    # No Fields

    # No Constructors

    # No Properties

    # ---------- Methods ---------- #

    @overload
    def Close(self) -> VoidType: ...
    @overload
    def Close(self, toSignal: WaitHandle) -> BooleanType: ...

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
    TimerQueue,
    TimerQueueTimer,
]
