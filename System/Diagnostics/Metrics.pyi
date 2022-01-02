__all__ = [
    'Counter',
    'Histogram',
    'Instrument',
    'Instrument',
    'Meter',
    'MeterListener',
    'ObservableCounter',
    'ObservableGauge',
    'ObservableInstrument',
    'Measurement',
    'MeasurementCallback',
]

from typing import TypeVar, Generic

T = TypeVar('T')


# TODO

# ---------- CLASSES ---------- #

class Counter(Generic[T]):
    """Represents an instrument that supports adding non-negative values. For example, you might call counter.Add(1) each time a request is processed to track the total number of requests. Most metric viewers display counters using a rate (requests/sec), by default, but can also display a cumulative total."""


class Histogram(Generic[T]):
    """Represents a metrics instrument that can be used to report arbitrary values that are likely to be statistically meaningful, for example, the request duration. Call CreateHistogram<T>(String, String, String) to create a Histogram object."""


class Instrument:
    """Base class of all Metrics Instrument classes"""


class Instrument(Generic[T]):
    """The base class for all non-observable instruments."""


class Meter:
    """Meter is the class responsible for creating and tracking the Instruments."""


class MeterListener:
    """MeterListener is class used to listen to the metrics instrument measurements recording."""


class ObservableCounter(Generic[T]):
    """Represents a metrics-observable instrument that reports monotonically increasing values when the instrument is being observed, for example, CPU time (for different processes, threads, user mode, or kernel mode). Call CreateObservableCounter to create the observable counter object."""


class ObservableGauge(Generic[T]):
    """Represents an observable instrument that reports non-additive values when the instrument is being observed, for example, the current room temperature. Call CreateObservableGauge to create the observable counter object."""


class ObservableInstrument(Generic[T]):
    """ObservableInstrument{T} is the base class from which all metrics observable instruments will inherit from."""


# ---------- STRUCTS ---------- #

class Measurement(Generic[T]):
    """Stores one observed metrics value and its associated tags. This type is used by an Observable instrument's Observe() method when reporting current measurements. with the associated tags."""


# ---------- DELEGATES ---------- #

class MeasurementCallback(Generic[T]):
    """A delegate to represent the Meterlistener callbacks used in measurements recording operation."""
