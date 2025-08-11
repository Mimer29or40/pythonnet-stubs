"""Automatically generated stubs for C# namespace: System.Diagnostics.PerformanceData."""

from abc import ABC
from typing import overload

from System import Enum
from System import Guid
from System import IDisposable
from System import Object
from System import Type

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CounterData(Object):
    """"""
    @property
    def RawValue(self) -> int:
        """"""
    @RawValue.setter
    def RawValue(self, value: int) -> None: ...
    @property
    def Value(self) -> int:
        """"""
    @Value.setter
    def Value(self, value: int) -> None: ...
    def Decrement(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Increment(self) -> None:
        """"""
    def IncrementBy(self, value: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CounterSet(Object, IDisposable):
    """"""
    def __init__(
        self, providerGuid: Guid, counterSetGuid: Guid, instanceType: CounterSetInstanceType
    ) -> None:
        """"""
    @overload
    def AddCounter(self, counterId: int, counterType: CounterType) -> None:
        """"""
    @overload
    def AddCounter(self, counterId: int, counterType: CounterType, counterName: str) -> None:
        """"""
    def CreateCounterSetInstance(self, instanceName: str) -> CounterSetInstance:
        """"""
    def Dispose(self) -> None:
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
class CounterSetInstance(Object, IDisposable):
    """"""
    @property
    def Counters(self) -> CounterSetInstanceCounterDataSet:
        """"""
    def Dispose(self) -> None:
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
class CounterSetInstanceCounterDataSet(Object, IDisposable):
    """"""
    @property
    def Item(self) -> CounterData:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __getitem__(self, counterId: int) -> CounterData:
        """"""
    @overload
    def __getitem__(self, counterName: str) -> CounterData:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class CounterSetInstanceType(Enum):
    """"""

    Single: CounterSetInstanceType = ...
    """"""
    Multiple: CounterSetInstanceType = ...
    """"""
    GlobalAggregate: CounterSetInstanceType = ...
    """"""
    MultipleAggregate: CounterSetInstanceType = ...
    """"""
    GlobalAggregateWithHistory: CounterSetInstanceType = ...
    """"""
    InstanceAggregate: CounterSetInstanceType = ...
    """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class CounterType(Enum):
    """"""

    RawDataHex32: CounterType = ...
    """"""
    RawDataHex64: CounterType = ...
    """"""
    RawData32: CounterType = ...
    """"""
    RawData64: CounterType = ...
    """"""
    Delta32: CounterType = ...
    """"""
    Delta64: CounterType = ...
    """"""
    SampleCounter: CounterType = ...
    """"""
    QueueLength: CounterType = ...
    """"""
    LargeQueueLength: CounterType = ...
    """"""
    QueueLength100Ns: CounterType = ...
    """"""
    QueueLengthObjectTime: CounterType = ...
    """"""
    RateOfCountPerSecond32: CounterType = ...
    """"""
    RateOfCountPerSecond64: CounterType = ...
    """"""
    RawFraction32: CounterType = ...
    """"""
    RawFraction64: CounterType = ...
    """"""
    PercentageActive: CounterType = ...
    """"""
    PrecisionSystemTimer: CounterType = ...
    """"""
    PercentageActive100Ns: CounterType = ...
    """"""
    PrecisionTimer100Ns: CounterType = ...
    """"""
    ObjectSpecificTimer: CounterType = ...
    """"""
    PrecisionObjectSpecificTimer: CounterType = ...
    """"""
    SampleFraction: CounterType = ...
    """"""
    PercentageNotActive: CounterType = ...
    """"""
    PercentageNotActive100Ns: CounterType = ...
    """"""
    MultiTimerPercentageActive: CounterType = ...
    """"""
    MultiTimerPercentageActive100Ns: CounterType = ...
    """"""
    MultiTimerPercentageNotActive: CounterType = ...
    """"""
    MultiTimerPercentageNotActive100Ns: CounterType = ...
    """"""
    AverageTimer32: CounterType = ...
    """"""
    ElapsedTime: CounterType = ...
    """"""
    AverageCount64: CounterType = ...
    """"""
    SampleBase: CounterType = ...
    """"""
    AverageBase: CounterType = ...
    """"""
    RawBase32: CounterType = ...
    """"""
    RawBase64: CounterType = ...
    """"""
    MultiTimerBase: CounterType = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class PerfProvider(Object):
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
class PerfProviderCollection(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
