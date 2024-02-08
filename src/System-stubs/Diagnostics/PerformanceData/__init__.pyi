from __future__ import annotations

from abc import ABC
from typing import overload

from System import Enum
from System import Guid
from System import IDisposable
from System import Object
from System import Type

class CounterData(Object):
    """"""

    @property
    def RawValue(self) -> int:
        """

        :return:
        """
    @RawValue.setter
    def RawValue(self, value: int) -> None: ...
    @property
    def Value(self) -> int:
        """

        :return:
        """
    @Value.setter
    def Value(self, value: int) -> None: ...
    def Decrement(self) -> None:
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
    def Increment(self) -> None:
        """"""
    def IncrementBy(self, value: int) -> None:
        """

        :param value:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CounterSet(Object, IDisposable):
    """"""

    def __init__(
        self, providerGuid: Guid, counterSetGuid: Guid, instanceType: CounterSetInstanceType
    ):
        """

        :param providerGuid:
        :param counterSetGuid:
        :param instanceType:
        """
    @overload
    def AddCounter(self, counterId: int, counterType: CounterType) -> None:
        """

        :param counterId:
        :param counterType:
        """
    @overload
    def AddCounter(self, counterId: int, counterType: CounterType, counterName: str) -> None:
        """

        :param counterId:
        :param counterType:
        :param counterName:
        """
    def CreateCounterSetInstance(self, instanceName: str) -> CounterSetInstance:
        """

        :param instanceName:
        :return:
        """
    def Dispose(self) -> None:
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

class CounterSetInstance(Object, IDisposable):
    """"""

    @property
    def Counters(self) -> CounterSetInstanceCounterDataSet:
        """

        :return:
        """
    def Dispose(self) -> None:
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

class CounterSetInstanceCounterDataSet(Object, IDisposable):
    """"""

    @property
    def Item(self) -> CounterData:
        """

        :return:
        """
    def Dispose(self) -> None:
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
    @overload
    def __getitem__(self, counterId: int) -> CounterData:
        """

        :param counterId:
        :return:
        """
    @overload
    def __getitem__(self, counterName: str) -> CounterData:
        """

        :param counterName:
        :return:
        """

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

class PerfProvider(Object):
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

class PerfProviderCollection(ABC, Object):
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
