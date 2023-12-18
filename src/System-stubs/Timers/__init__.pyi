from __future__ import annotations

from typing import Callable
from typing import Generic
from typing import TypeVar
from typing import Union
from typing import overload

from System import AsyncCallback
from System import Boolean
from System import DateTime
from System import Double
from System import EventArgs
from System import IAsyncResult
from System import ICloneable
from System import IDisposable
from System import IntPtr
from System import MulticastDelegate
from System import Object
from System import String
from System import Void
from System.ComponentModel import Component
from System.ComponentModel import DescriptionAttribute
from System.ComponentModel import IComponent
from System.ComponentModel import ISite
from System.ComponentModel import ISupportInitialize
from System.ComponentModel import ISynchronizeInvoke
from System.Runtime.InteropServices import _Attribute
from System.Runtime.Serialization import ISerializable

# ---------- Types ---------- #

T = TypeVar("T")

BooleanType = Union[bool, Boolean]
DoubleType = Union[float, Double]
NIntType = Union[int, IntPtr]
ObjectType = Object
StringType = Union[str, String]
VoidType = Union[None, Void]

class EventType(Generic[T]):
    def __iadd__(self, other: T): ...
    def __isub__(self, other: T): ...

# ---------- Classes ---------- #

class ElapsedEventArgs(EventArgs):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def SignalTime(self) -> DateTime: ...

    # ---------- Methods ---------- #

    def get_SignalTime(self) -> DateTime: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ElapsedEventHandler(MulticastDelegate, ICloneable, ISerializable):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, object: ObjectType, method: NIntType): ...

    # No Properties

    # ---------- Methods ---------- #

    def BeginInvoke(
        self, sender: ObjectType, e: ElapsedEventArgs, callback: AsyncCallback, object: ObjectType
    ) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    def Invoke(self, sender: ObjectType, e: ElapsedEventArgs) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class Timer(Component, IComponent, IDisposable, ISupportInitialize):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, interval: DoubleType): ...

    # ---------- Properties ---------- #

    @property
    def AutoReset(self) -> BooleanType: ...
    @AutoReset.setter
    def AutoReset(self, value: BooleanType) -> None: ...
    @property
    def Enabled(self) -> BooleanType: ...
    @Enabled.setter
    def Enabled(self, value: BooleanType) -> None: ...
    @property
    def Interval(self) -> DoubleType: ...
    @Interval.setter
    def Interval(self, value: DoubleType) -> None: ...
    @property
    def Site(self) -> ISite: ...
    @Site.setter
    def Site(self, value: ISite) -> None: ...
    @property
    def SynchronizingObject(self) -> ISynchronizeInvoke: ...
    @SynchronizingObject.setter
    def SynchronizingObject(self, value: ISynchronizeInvoke) -> None: ...

    # ---------- Methods ---------- #

    def BeginInit(self) -> VoidType: ...
    def Close(self) -> VoidType: ...
    def EndInit(self) -> VoidType: ...
    def Start(self) -> VoidType: ...
    def Stop(self) -> VoidType: ...
    def add_Elapsed(self, value: ElapsedEventHandler) -> VoidType: ...
    def get_AutoReset(self) -> BooleanType: ...
    def get_Enabled(self) -> BooleanType: ...
    def get_Interval(self) -> DoubleType: ...
    def get_Site(self) -> ISite: ...
    def get_SynchronizingObject(self) -> ISynchronizeInvoke: ...
    def remove_Elapsed(self, value: ElapsedEventHandler) -> VoidType: ...
    def set_AutoReset(self, value: BooleanType) -> VoidType: ...
    def set_Enabled(self, value: BooleanType) -> VoidType: ...
    def set_Interval(self, value: DoubleType) -> VoidType: ...
    def set_Site(self, value: ISite) -> VoidType: ...
    def set_SynchronizingObject(self, value: ISynchronizeInvoke) -> VoidType: ...

    # ---------- Events ---------- #

    Elapsed: EventType[ElapsedEventHandler] = ...

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class TimersDescriptionAttribute(DescriptionAttribute, _Attribute):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, description: StringType): ...

    # ---------- Properties ---------- #

    @property
    def Description(self) -> StringType: ...

    # ---------- Methods ---------- #

    def get_Description(self) -> StringType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

# No Structs

# No Interfaces

# No Enums

# ---------- Delegates ---------- #

ElapsedEventHandler = Callable[[ObjectType, ElapsedEventArgs], VoidType]

__all__ = [
    ElapsedEventArgs,
    ElapsedEventHandler,
    Timer,
    TimersDescriptionAttribute,
    ElapsedEventHandler,
]
