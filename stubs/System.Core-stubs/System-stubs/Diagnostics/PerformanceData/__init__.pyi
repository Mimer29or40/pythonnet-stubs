from __future__ import annotations

from abc import ABC
from typing import Union, overload

from System import Enum, Guid, IDisposable, Int32, Int64, Object, String, Void

# ---------- Types ---------- #

IntType = Union[int, Int32]
LongType = Union[int, Int64]
ObjectType = Object
StringType = Union[str, String]
VoidType = Union[None, Void]

# ---------- Classes ---------- #

class CounterData(ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def RawValue(self) -> LongType: ...
    
    @RawValue.setter
    def RawValue(self, value: LongType) -> None: ...
    
    @property
    def Value(self) -> LongType: ...
    
    @Value.setter
    def Value(self, value: LongType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Decrement(self) -> VoidType: ...
    
    def Increment(self) -> VoidType: ...
    
    def IncrementBy(self, value: LongType) -> VoidType: ...
    
    def get_RawValue(self) -> LongType: ...
    
    def get_Value(self) -> LongType: ...
    
    def set_RawValue(self, value: LongType) -> VoidType: ...
    
    def set_Value(self, value: LongType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CounterSet(ObjectType, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, providerGuid: Guid, counterSetGuid: Guid, instanceType: CounterSetInstanceType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def AddCounter(self, counterId: IntType, counterType: CounterType) -> VoidType: ...
    
    @overload
    def AddCounter(self, counterId: IntType, counterType: CounterType, counterName: StringType) -> VoidType: ...
    
    def CreateCounterSetInstance(self, instanceName: StringType) -> CounterSetInstance: ...
    
    def Dispose(self) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CounterSetInstance(ObjectType, IDisposable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Counters(self) -> CounterSetInstanceCounterDataSet: ...
    
    # ---------- Methods ---------- #
    
    def Dispose(self) -> VoidType: ...
    
    def get_Counters(self) -> CounterSetInstanceCounterDataSet: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CounterSetInstanceCounterDataSet(ObjectType, IDisposable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Item(self) -> CounterData: ...
    
    @property
    def Item(self) -> CounterData: ...
    
    # ---------- Methods ---------- #
    
    def Dispose(self) -> VoidType: ...
    
    @overload
    def get_Item(self, counterId: IntType) -> CounterData: ...
    
    @overload
    def get_Item(self, counterName: StringType) -> CounterData: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PerfProvider(ObjectType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PerfProviderCollection(ABC, ObjectType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# No Structs

# No Interfaces

# ---------- Enums ---------- #

class CounterSetInstanceType(Enum):
    Single: IntType = 0
    Multiple: IntType = 2
    GlobalAggregate: IntType = 4
    MultipleAggregate: IntType = 6
    GlobalAggregateWithHistory: IntType = 11
    InstanceAggregate: IntType = 22


class CounterType(Enum):
    RawDataHex32: IntType = 0
    RawDataHex64: IntType = 256
    RawData32: IntType = 65536
    RawData64: IntType = 65792
    Delta32: IntType = 4195328
    Delta64: IntType = 4195584
    SampleCounter: IntType = 4260864
    QueueLength: IntType = 4523008
    LargeQueueLength: IntType = 4523264
    QueueLength100Ns: IntType = 5571840
    QueueLengthObjectTime: IntType = 6620416
    RateOfCountPerSecond32: IntType = 272696320
    RateOfCountPerSecond64: IntType = 272696576
    RawFraction32: IntType = 537003008
    RawFraction64: IntType = 537003264
    PercentageActive: IntType = 541132032
    PrecisionSystemTimer: IntType = 541525248
    PercentageActive100Ns: IntType = 542180608
    PrecisionTimer100Ns: IntType = 542573824
    ObjectSpecificTimer: IntType = 543229184
    PrecisionObjectSpecificTimer: IntType = 543622400
    SampleFraction: IntType = 549585920
    PercentageNotActive: IntType = 557909248
    PercentageNotActive100Ns: IntType = 558957824
    MultiTimerPercentageActive: IntType = 574686464
    MultiTimerPercentageActive100Ns: IntType = 575735040
    MultiTimerPercentageNotActive: IntType = 591463680
    MultiTimerPercentageNotActive100Ns: IntType = 592512256
    AverageTimer32: IntType = 805438464
    ElapsedTime: IntType = 807666944
    AverageCount64: IntType = 1073874176
    SampleBase: IntType = 1073939457
    AverageBase: IntType = 1073939458
    RawBase32: IntType = 1073939459
    RawBase64: IntType = 1073939712
    MultiTimerBase: IntType = 1107494144


# No Delegates

__all__ = [
    CounterData,
    CounterSet,
    CounterSetInstance,
    CounterSetInstanceCounterDataSet,
    PerfProvider,
    PerfProviderCollection,
    CounterSetInstanceType,
    CounterType,
]
