from __future__ import annotations

from abc import ABC
from typing import ClassVar
from typing import Final
from typing import Generic
from typing import Iterator
from typing import Optional
from typing import TypeVar
from typing import overload

from System import Array
from System import Boolean
from System import Decimal
from System import Double
from System import Enum
from System import EventHandler
from System import Exception
from System import Func
from System import Guid
from System import IDisposable
from System import Int32
from System import Int64
from System import Object
from System import Single
from System import TimeSpan
from System import Type
from System import ValueType
from System.Collections import IEnumerable
from System.Collections import IEnumerator
from System.Collections.Generic import ICollection
from System.Collections.Generic import IComparer
from System.Collections.Generic import IEnumerable
from System.Collections.Generic import IEnumerator
from System.Collections.Generic import IEqualityComparer
from System.Collections.Generic import IList
from System.Collections.Generic import Queue
from System.Diagnostics.Tracing import EventChannel
from System.Diagnostics.Tracing import EventCommandEventArgs
from System.Diagnostics.Tracing import EventKeywords
from System.Diagnostics.Tracing import EventLevel
from System.Diagnostics.Tracing import EventSource
from System.Diagnostics.Tracing import EventSourceOptions
from System.Diagnostics.Tracing import EventSourceSettings
from System.Diagnostics.Tracing import EventTask
from System.Diagnostics.Tracing import T
from System.Linq import IGrouping
from System.Linq import ILookup
from System.Linq import IOrderedEnumerable
from System.Linq import ParallelMergeOptions
from System.Linq import ParallelQuery
from System.Threading import CancellationToken
from System.Threading import ManualResetEventSlim
from System.Threading import WaitHandle
from System.Threading.Tasks import TaskScheduler

T = TypeVar("T")
TElement = TypeVar("TElement")
TGroupKey = TypeVar("TGroupKey")
THashKey = TypeVar("THashKey")
TIgnoreKey = TypeVar("TIgnoreKey")
TInput = TypeVar("TInput")
TInputOutput = TypeVar("TInputOutput")
TIntermediate = TypeVar("TIntermediate")
TKey = TypeVar("TKey")
TLeftInput = TypeVar("TLeftInput")
TLeftKey = TypeVar("TLeftKey")
TOrderKey = TypeVar("TOrderKey")
TOutput = TypeVar("TOutput")
TResult = TypeVar("TResult")
TRightInput = TypeVar("TRightInput")
TRightKey = TypeVar("TRightKey")
TSortKey = TypeVar("TSortKey")
TSource = TypeVar("TSource")
TValue = TypeVar("TValue")
U = TypeVar("U")

class EventType(Generic[T]):
    def __iadd__(self, other: T): ...
    def __isub__(self, other: T): ...

class AnyAllSearchOperator(
    Generic[TInput], UnaryQueryOperator[TInput, Boolean], IEnumerable[Boolean], IEnumerable
):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    @overload
    def GetEnumerator(self, mergeOptions: Optional[ParallelMergeOptions]) -> IEnumerator[bool]:
        """

        :param mergeOptions:
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
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[bool]:
        """

        :return:
        """

class ArrayMergeHelper(Generic[TInputOutput], Object, IMergeHelper[TInputOutput]):
    """"""

    def __init__(self, settings: QuerySettings, queryResults: QueryResults[TInputOutput]):
        """

        :param settings:
        :param queryResults:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def Execute(self) -> None:
        """"""
    def GetEnumerator(self) -> IEnumerator[TInputOutput]:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetResultsAsArray(self) -> Array[TInputOutput]:
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

class AssociativeAggregationOperator(
    Generic[TInput, TIntermediate, TOutput],
    UnaryQueryOperator[TInput, TIntermediate],
    IEnumerable[TIntermediate],
    IEnumerable,
):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    @overload
    def GetEnumerator(
        self, mergeOptions: Optional[ParallelMergeOptions]
    ) -> IEnumerator[TIntermediate]:
        """

        :param mergeOptions:
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
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[TIntermediate]:
        """

        :return:
        """

class AsynchronousChannel(Generic[T], Object, IDisposable):
    """"""

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

class AsynchronousChannelMergeEnumerator(
    Generic[T], MergeEnumerator[T], IEnumerator[T], IEnumerator, IDisposable
):
    """"""

    @property
    def Current(self) -> object:
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
    def MoveNext(self) -> bool:
        """

        :return:
        """
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class BinaryQueryOperator(
    ABC,
    Generic[TLeftInput, TRightInput, TOutput],
    QueryOperator[TOutput],
    IEnumerable[TOutput],
    IEnumerable,
):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    @overload
    def GetEnumerator(self, mergeOptions: Optional[ParallelMergeOptions]) -> IEnumerator[TOutput]:
        """

        :param mergeOptions:
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
    def WrapPartitionedStream(
        self,
        leftPartitionedStream: PartitionedStream[TLeftInput, TLeftKey],
        rightPartitionedStream: PartitionedStream[TRightInput, TRightKey],
        outputRecipient: IPartitionedStreamRecipient[TOutput],
        preferStriping: bool,
        settings: QuerySettings,
    ) -> None:
        """

        :param leftPartitionedStream:
        :param rightPartitionedStream:
        :param outputRecipient:
        :param preferStriping:
        :param settings:
        """
    @overload
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[TOutput]:
        """

        :return:
        """

class CancellableEnumerable(ABC, Object):
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

class CancellationState(Object):
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

class ConcatKey(Generic[TLeftKey, TRightKey], ValueType):
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

class ConcatQueryOperator(
    Generic[TSource],
    BinaryQueryOperator[TSource, TSource, TSource],
    IEnumerable[TSource],
    IEnumerable,
):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    @overload
    def GetEnumerator(self, mergeOptions: Optional[ParallelMergeOptions]) -> IEnumerator[TSource]:
        """

        :param mergeOptions:
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
    def WrapPartitionedStream(
        self,
        leftPartitionedStream: PartitionedStream[TSource, TLeftKey],
        rightPartitionedStream: PartitionedStream[TSource, TRightKey],
        outputRecipient: IPartitionedStreamRecipient[TSource],
        preferStriping: bool,
        settings: QuerySettings,
    ) -> None:
        """

        :param leftPartitionedStream:
        :param rightPartitionedStream:
        :param outputRecipient:
        :param preferStriping:
        :param settings:
        """
    @overload
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[TSource]:
        """

        :return:
        """

class ContainsSearchOperator(
    Generic[TInput], UnaryQueryOperator[TInput, Boolean], IEnumerable[Boolean], IEnumerable
):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    @overload
    def GetEnumerator(self, mergeOptions: Optional[ParallelMergeOptions]) -> IEnumerator[bool]:
        """

        :param mergeOptions:
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
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[bool]:
        """

        :return:
        """

class CountAggregationOperator(
    Generic[TSource],
    InlinedAggregationOperator[TSource, Int32, Int32],
    IEnumerable[Int32],
    IEnumerable,
):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    @overload
    def GetEnumerator(self, mergeOptions: Optional[ParallelMergeOptions]) -> IEnumerator[int]:
        """

        :param mergeOptions:
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
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[int]:
        """

        :return:
        """

class DecimalAverageAggregationOperator(
    InlinedAggregationOperator[Decimal, Pair, Int64, Decimal], IEnumerable[Pair, Int64], IEnumerable
):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    @overload
    def GetEnumerator(self, mergeOptions: Optional[ParallelMergeOptions]) -> IEnumerator[Pair, int]:
        """

        :param mergeOptions:
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
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[Pair, int]:
        """

        :return:
        """

class DecimalMinMaxAggregationOperator(
    InlinedAggregationOperator[Decimal, Decimal, Decimal], IEnumerable[Decimal], IEnumerable
):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    @overload
    def GetEnumerator(self, mergeOptions: Optional[ParallelMergeOptions]) -> IEnumerator[Decimal]:
        """

        :param mergeOptions:
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
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[Decimal]:
        """

        :return:
        """

class DecimalSumAggregationOperator(
    InlinedAggregationOperator[Decimal, Decimal, Decimal], IEnumerable[Decimal], IEnumerable
):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    @overload
    def GetEnumerator(self, mergeOptions: Optional[ParallelMergeOptions]) -> IEnumerator[Decimal]:
        """

        :param mergeOptions:
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
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[Decimal]:
        """

        :return:
        """

class DefaultIfEmptyQueryOperator(
    Generic[TSource], UnaryQueryOperator[TSource, TSource], IEnumerable[TSource], IEnumerable
):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    @overload
    def GetEnumerator(self, mergeOptions: Optional[ParallelMergeOptions]) -> IEnumerator[TSource]:
        """

        :param mergeOptions:
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
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[TSource]:
        """

        :return:
        """

class DefaultMergeHelper(Generic[TInputOutput, TIgnoreKey], Object, IMergeHelper[TInputOutput]):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def Execute(self) -> None:
        """"""
    def GetEnumerator(self) -> IEnumerator[TInputOutput]:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetResultsAsArray(self) -> Array[TInputOutput]:
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

class DistinctQueryOperator(
    Generic[TInputOutput],
    UnaryQueryOperator[TInputOutput, TInputOutput],
    IEnumerable[TInputOutput],
    IEnumerable,
):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    @overload
    def GetEnumerator(
        self, mergeOptions: Optional[ParallelMergeOptions]
    ) -> IEnumerator[TInputOutput]:
        """

        :param mergeOptions:
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
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[TInputOutput]:
        """

        :return:
        """

class DoubleAverageAggregationOperator(
    InlinedAggregationOperator[Double, Pair, Int64, Double], IEnumerable[Pair, Int64], IEnumerable
):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    @overload
    def GetEnumerator(self, mergeOptions: Optional[ParallelMergeOptions]) -> IEnumerator[Pair, int]:
        """

        :param mergeOptions:
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
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[Pair, int]:
        """

        :return:
        """

class DoubleMinMaxAggregationOperator(
    InlinedAggregationOperator[Double, Double, Double], IEnumerable[Double], IEnumerable
):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    @overload
    def GetEnumerator(self, mergeOptions: Optional[ParallelMergeOptions]) -> IEnumerator[float]:
        """

        :param mergeOptions:
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
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[float]:
        """

        :return:
        """

class DoubleSumAggregationOperator(
    InlinedAggregationOperator[Double, Double, Double], IEnumerable[Double], IEnumerable
):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    @overload
    def GetEnumerator(self, mergeOptions: Optional[ParallelMergeOptions]) -> IEnumerator[float]:
        """

        :param mergeOptions:
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
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[float]:
        """

        :return:
        """

class ElementAtQueryOperator(
    Generic[TSource], UnaryQueryOperator[TSource, TSource], IEnumerable[TSource], IEnumerable
):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    @overload
    def GetEnumerator(self, mergeOptions: Optional[ParallelMergeOptions]) -> IEnumerator[TSource]:
        """

        :param mergeOptions:
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
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[TSource]:
        """

        :return:
        """

class EmptyEnumerable(Generic[T], ParallelQuery[T], IEnumerable[T], IEnumerable):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

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
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[T]:
        """

        :return:
        """

class EmptyEnumerator(
    Generic[T], QueryOperatorEnumerator[T, Int32], IEnumerator[T], IEnumerator, IDisposable
):
    """"""

    def __init__(self):
        """"""
    @property
    def Current(self) -> object:
        """

        :return:
        """
    @overload
    def Dispose(self) -> None:
        """"""
    @overload
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
    def MoveNext(self) -> bool:
        """

        :return:
        """
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class EnumerableWrapperWeakToStrong(Object, IEnumerable[Object], IEnumerable):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

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
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """

class ExceptQueryOperator(
    Generic[TInputOutput],
    BinaryQueryOperator[TInputOutput, TInputOutput, TInputOutput],
    IEnumerable[TInputOutput],
    IEnumerable,
):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    @overload
    def GetEnumerator(
        self, mergeOptions: Optional[ParallelMergeOptions]
    ) -> IEnumerator[TInputOutput]:
        """

        :param mergeOptions:
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
    def WrapPartitionedStream(
        self,
        leftPartitionedStream: PartitionedStream[TInputOutput, TLeftKey],
        rightPartitionedStream: PartitionedStream[TInputOutput, TRightKey],
        outputRecipient: IPartitionedStreamRecipient[TInputOutput],
        preferStriping: bool,
        settings: QuerySettings,
    ) -> None:
        """

        :param leftPartitionedStream:
        :param rightPartitionedStream:
        :param outputRecipient:
        :param preferStriping:
        :param settings:
        """
    @overload
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[TInputOutput]:
        """

        :return:
        """

class ExceptionAggregator(ABC, Object):
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

class ExchangeUtilities(ABC, Object):
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

class FirstQueryOperator(
    Generic[TSource], UnaryQueryOperator[TSource, TSource], IEnumerable[TSource], IEnumerable
):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    @overload
    def GetEnumerator(self, mergeOptions: Optional[ParallelMergeOptions]) -> IEnumerator[TSource]:
        """

        :param mergeOptions:
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
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[TSource]:
        """

        :return:
        """

class FixedMaxHeap(Generic[TElement], Object):
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

class FloatAverageAggregationOperator(
    InlinedAggregationOperator[Single, Pair, Int64, Single], IEnumerable[Pair, Int64], IEnumerable
):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    @overload
    def GetEnumerator(self, mergeOptions: Optional[ParallelMergeOptions]) -> IEnumerator[Pair, int]:
        """

        :param mergeOptions:
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
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[Pair, int]:
        """

        :return:
        """

class FloatMinMaxAggregationOperator(
    InlinedAggregationOperator[Single, Single, Single], IEnumerable[Single], IEnumerable
):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    @overload
    def GetEnumerator(self, mergeOptions: Optional[ParallelMergeOptions]) -> IEnumerator[float]:
        """

        :param mergeOptions:
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
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[float]:
        """

        :return:
        """

class FloatSumAggregationOperator(
    InlinedAggregationOperator[Single, Double, Single], IEnumerable[Double], IEnumerable
):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    @overload
    def GetEnumerator(self, mergeOptions: Optional[ParallelMergeOptions]) -> IEnumerator[float]:
        """

        :param mergeOptions:
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
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[float]:
        """

        :return:
        """

class ForAllOperator(
    Generic[TInput], UnaryQueryOperator[TInput, TInput], IEnumerable[TInput], IEnumerable
):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    @overload
    def GetEnumerator(self, mergeOptions: Optional[ParallelMergeOptions]) -> IEnumerator[TInput]:
        """

        :param mergeOptions:
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
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[TInput]:
        """

        :return:
        """

class ForAllSpoolingTask(Generic[TInputOutput, TIgnoreKey], SpoolingTaskBase):
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

class GroupByElementSelectorQueryOperatorEnumerator(
    Generic[TSource, TGroupKey, TElement, TOrderKey],
    GroupByQueryOperatorEnumerator[TSource, TGroupKey, TElement, TOrderKey],
):
    """"""

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

class GroupByGrouping(
    Generic[TGroupKey, TElement],
    Object,
    IEnumerable[TElement],
    IEnumerable,
    IGrouping[TGroupKey, TElement],
):
    """"""

    @property
    def Key(self) -> TGroupKey:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

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
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[TElement]:
        """

        :return:
        """

class GroupByIdentityQueryOperatorEnumerator(
    Generic[TSource, TGroupKey, TOrderKey],
    GroupByQueryOperatorEnumerator[TSource, TGroupKey, TSource, TOrderKey],
):
    """"""

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

class GroupByQueryOperator(
    Generic[TSource, TGroupKey, TElement],
    UnaryQueryOperator[TSource, IGrouping, TElement],
    IEnumerable[IGrouping, TElement],
    IEnumerable,
):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    @overload
    def GetEnumerator(
        self, mergeOptions: Optional[ParallelMergeOptions]
    ) -> IEnumerator[IGrouping, TElement]:
        """

        :param mergeOptions:
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
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[IGrouping, TElement]:
        """

        :return:
        """

class GroupByQueryOperatorEnumerator(
    ABC,
    Generic[TSource, TGroupKey, TElement, TOrderKey],
    QueryOperatorEnumerator[IGrouping, TElement, TOrderKey],
):
    """"""

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

class GroupJoinQueryOperator(
    Generic[TLeftInput, TRightInput, TKey, TOutput],
    BinaryQueryOperator[TLeftInput, TRightInput, TOutput],
    IEnumerable[TOutput],
    IEnumerable,
):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    @overload
    def GetEnumerator(self, mergeOptions: Optional[ParallelMergeOptions]) -> IEnumerator[TOutput]:
        """

        :param mergeOptions:
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
    def WrapPartitionedStream(
        self,
        leftPartitionedStream: PartitionedStream[TLeftInput, TLeftKey],
        rightPartitionedStream: PartitionedStream[TRightInput, TRightKey],
        outputRecipient: IPartitionedStreamRecipient[TOutput],
        preferStriping: bool,
        settings: QuerySettings,
    ) -> None:
        """

        :param leftPartitionedStream:
        :param rightPartitionedStream:
        :param outputRecipient:
        :param preferStriping:
        :param settings:
        """
    @overload
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[TOutput]:
        """

        :return:
        """

class GrowingArray(Generic[T], Object):
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

class HashJoinQueryOperatorEnumerator(
    Generic[TLeftInput, TLeftKey, TRightInput, THashKey, TOutput],
    QueryOperatorEnumerator[TOutput, TLeftKey],
):
    """"""

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

class HashLookup(Generic[TKey, TValue], Object):
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

class HashRepartitionEnumerator(
    Generic[TInputOutput, THashKey, TIgnoreKey], QueryOperatorEnumerator[Pair, THashKey, Int32]
):
    """"""

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

class HashRepartitionStream(
    ABC, Generic[TInputOutput, THashKey, TOrderKey], PartitionedStream[Pair, THashKey, TOrderKey]
):
    """"""

    @property
    def PartitionCount(self) -> int:
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

class IMergeHelper(Generic[TInputOutput]):
    """"""

    def Execute(self) -> None:
        """"""
    def GetEnumerator(self) -> IEnumerator[TInputOutput]:
        """

        :return:
        """
    def GetResultsAsArray(self) -> Array[TInputOutput]:
        """

        :return:
        """

class IParallelPartitionable(Generic[T]):
    """"""

    def GetPartitions(self, partitionCount: int) -> Array[QueryOperatorEnumerator, int]:
        """

        :param partitionCount:
        :return:
        """

class IPartitionedStreamRecipient(Generic[TElement]):
    """"""

    def Receive(self, partitionedStream: PartitionedStream[TElement, TKey]) -> None:
        """

        :param partitionedStream:
        """

class IndexedSelectQueryOperator(
    Generic[TInput, TOutput], UnaryQueryOperator[TInput, TOutput], IEnumerable[TOutput], IEnumerable
):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    @overload
    def GetEnumerator(self, mergeOptions: Optional[ParallelMergeOptions]) -> IEnumerator[TOutput]:
        """

        :param mergeOptions:
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
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[TOutput]:
        """

        :return:
        """

class IndexedWhereQueryOperator(
    Generic[TInputOutput],
    UnaryQueryOperator[TInputOutput, TInputOutput],
    IEnumerable[TInputOutput],
    IEnumerable,
):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    @overload
    def GetEnumerator(
        self, mergeOptions: Optional[ParallelMergeOptions]
    ) -> IEnumerator[TInputOutput]:
        """

        :param mergeOptions:
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
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[TInputOutput]:
        """

        :return:
        """

class InlinedAggregationOperator(
    ABC,
    Generic[TSource, TIntermediate, TResult],
    UnaryQueryOperator[TSource, TIntermediate],
    IEnumerable[TIntermediate],
    IEnumerable,
):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    @overload
    def GetEnumerator(
        self, mergeOptions: Optional[ParallelMergeOptions]
    ) -> IEnumerator[TIntermediate]:
        """

        :param mergeOptions:
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
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[TIntermediate]:
        """

        :return:
        """

class InlinedAggregationOperatorEnumerator(
    ABC, Generic[TIntermediate], QueryOperatorEnumerator[TIntermediate, Int32]
):
    """"""

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

class IntAverageAggregationOperator(
    InlinedAggregationOperator[Int32, Pair, Int64, Double], IEnumerable[Pair, Int64], IEnumerable
):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    @overload
    def GetEnumerator(self, mergeOptions: Optional[ParallelMergeOptions]) -> IEnumerator[Pair, int]:
        """

        :param mergeOptions:
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
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[Pair, int]:
        """

        :return:
        """

class IntMinMaxAggregationOperator(
    InlinedAggregationOperator[Int32, Int32, Int32], IEnumerable[Int32], IEnumerable
):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    @overload
    def GetEnumerator(self, mergeOptions: Optional[ParallelMergeOptions]) -> IEnumerator[int]:
        """

        :param mergeOptions:
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
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[int]:
        """

        :return:
        """

class IntSumAggregationOperator(
    InlinedAggregationOperator[Int32, Int32, Int32], IEnumerable[Int32], IEnumerable
):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    @overload
    def GetEnumerator(self, mergeOptions: Optional[ParallelMergeOptions]) -> IEnumerator[int]:
        """

        :param mergeOptions:
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
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[int]:
        """

        :return:
        """

class IntValueEvent(ManualResetEventSlim, IDisposable):
    """"""

    @property
    def IsSet(self) -> bool:
        """

        :return:
        """
    @property
    def SpinCount(self) -> int:
        """

        :return:
        """
    @property
    def WaitHandle(self) -> WaitHandle:
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
    def Reset(self) -> None:
        """"""
    def Set(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def Wait(self) -> None:
        """"""
    @overload
    def Wait(self, cancellationToken: CancellationToken) -> None:
        """

        :param cancellationToken:
        """
    @overload
    def Wait(self, millisecondsTimeout: int) -> bool:
        """

        :param millisecondsTimeout:
        :return:
        """
    @overload
    def Wait(self, timeout: TimeSpan) -> bool:
        """

        :param timeout:
        :return:
        """
    @overload
    def Wait(self, millisecondsTimeout: int, cancellationToken: CancellationToken) -> bool:
        """

        :param millisecondsTimeout:
        :param cancellationToken:
        :return:
        """
    @overload
    def Wait(self, timeout: TimeSpan, cancellationToken: CancellationToken) -> bool:
        """

        :param timeout:
        :param cancellationToken:
        :return:
        """

class IntersectQueryOperator(
    Generic[TInputOutput],
    BinaryQueryOperator[TInputOutput, TInputOutput, TInputOutput],
    IEnumerable[TInputOutput],
    IEnumerable,
):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    @overload
    def GetEnumerator(
        self, mergeOptions: Optional[ParallelMergeOptions]
    ) -> IEnumerator[TInputOutput]:
        """

        :param mergeOptions:
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
    def WrapPartitionedStream(
        self,
        leftPartitionedStream: PartitionedStream[TInputOutput, TLeftKey],
        rightPartitionedStream: PartitionedStream[TInputOutput, TRightKey],
        outputRecipient: IPartitionedStreamRecipient[TInputOutput],
        preferStriping: bool,
        settings: QuerySettings,
    ) -> None:
        """

        :param leftPartitionedStream:
        :param rightPartitionedStream:
        :param outputRecipient:
        :param preferStriping:
        :param settings:
        """
    @overload
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[TInputOutput]:
        """

        :return:
        """

class JoinQueryOperator(
    Generic[TLeftInput, TRightInput, TKey, TOutput],
    BinaryQueryOperator[TLeftInput, TRightInput, TOutput],
    IEnumerable[TOutput],
    IEnumerable,
):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    @overload
    def GetEnumerator(self, mergeOptions: Optional[ParallelMergeOptions]) -> IEnumerator[TOutput]:
        """

        :param mergeOptions:
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
    def WrapPartitionedStream(
        self,
        leftPartitionedStream: PartitionedStream[TLeftInput, TLeftKey],
        rightPartitionedStream: PartitionedStream[TRightInput, TRightKey],
        outputRecipient: IPartitionedStreamRecipient[TOutput],
        preferStriping: bool,
        settings: QuerySettings,
    ) -> None:
        """

        :param leftPartitionedStream:
        :param rightPartitionedStream:
        :param outputRecipient:
        :param preferStriping:
        :param settings:
        """
    @overload
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[TOutput]:
        """

        :return:
        """

class LastQueryOperator(
    Generic[TSource], UnaryQueryOperator[TSource, TSource], IEnumerable[TSource], IEnumerable
):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    @overload
    def GetEnumerator(self, mergeOptions: Optional[ParallelMergeOptions]) -> IEnumerator[TSource]:
        """

        :param mergeOptions:
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
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[TSource]:
        """

        :return:
        """

class ListChunk(Generic[TInputOutput], Object, IEnumerable[TInputOutput], IEnumerable):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

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
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[TInputOutput]:
        """

        :return:
        """

class ListQueryResults(
    Generic[T], QueryResults[T], ICollection[T], IEnumerable[T], IList[T], IEnumerable
):
    """"""

    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def Item(self) -> T:
        """

        :return:
        """
    @Item.setter
    def Item(self, value: T) -> None: ...
    def Add(self, item: T) -> None:
        """

        :param item:
        """
    def Clear(self) -> None:
        """"""
    def Contains(self, item: T) -> bool:
        """

        :param item:
        :return:
        """
    def CopyTo(self, array: Array[T], arrayIndex: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

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
    def IndexOf(self, item: T) -> int:
        """

        :param item:
        :return:
        """
    def Insert(self, index: int, item: T) -> None:
        """

        :param index:
        :param item:
        """
    def Remove(self, item: T) -> bool:
        """

        :param item:
        :return:
        """
    def RemoveAt(self, index: int) -> None:
        """

        :param index:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def __contains__(self, value: T) -> bool:
        """

        :param value:
        :return:
        """
    def __getitem__(self, index: int) -> T:
        """

        :param index:
        :return:
        """
    @overload
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[T]:
        """

        :return:
        """
    def __len__(self) -> int:
        """

        :return:
        """
    def __setitem__(self, index: int, value: T) -> None:
        """

        :param index:
        :param value:
        """

class LongAverageAggregationOperator(
    InlinedAggregationOperator[Int64, Pair, Int64, Double], IEnumerable[Pair, Int64], IEnumerable
):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    @overload
    def GetEnumerator(self, mergeOptions: Optional[ParallelMergeOptions]) -> IEnumerator[Pair, int]:
        """

        :param mergeOptions:
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
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[Pair, int]:
        """

        :return:
        """

class LongCountAggregationOperator(
    Generic[TSource],
    InlinedAggregationOperator[TSource, Int64, Int64],
    IEnumerable[Int64],
    IEnumerable,
):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    @overload
    def GetEnumerator(self, mergeOptions: Optional[ParallelMergeOptions]) -> IEnumerator[int]:
        """

        :param mergeOptions:
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
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[int]:
        """

        :return:
        """

class LongMinMaxAggregationOperator(
    InlinedAggregationOperator[Int64, Int64, Int64], IEnumerable[Int64], IEnumerable
):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    @overload
    def GetEnumerator(self, mergeOptions: Optional[ParallelMergeOptions]) -> IEnumerator[int]:
        """

        :param mergeOptions:
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
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[int]:
        """

        :return:
        """

class LongSumAggregationOperator(
    InlinedAggregationOperator[Int64, Int64, Int64], IEnumerable[Int64], IEnumerable
):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    @overload
    def GetEnumerator(self, mergeOptions: Optional[ParallelMergeOptions]) -> IEnumerator[int]:
        """

        :param mergeOptions:
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
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[int]:
        """

        :return:
        """

class Lookup(
    Generic[TKey, TElement],
    Object,
    IEnumerable[IGrouping, TElement],
    IEnumerable,
    ILookup[TKey, TElement],
):
    """"""

    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def Item(self) -> IEnumerable[TElement]:
        """

        :return:
        """
    def Contains(self, key: TKey) -> bool:
        """

        :param key:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

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
    def __getitem__(self, key: TKey) -> IEnumerable[TElement]:
        """

        :param key:
        :return:
        """
    @overload
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[IGrouping, TElement]:
        """

        :return:
        """

class MergeEnumerator(
    ABC, Generic[TInputOutput], Object, IEnumerator[TInputOutput], IEnumerator, IDisposable
):
    """"""

    @property
    def Current(self) -> object:
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
    def MoveNext(self) -> bool:
        """

        :return:
        """
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class MergeExecutor(Generic[TInputOutput], Object, IEnumerable[TInputOutput], IEnumerable):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

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
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[TInputOutput]:
        """

        :return:
        """

class NoKeyMemoizationRequired(ValueType):
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

class NullableDecimalAverageAggregationOperator(
    InlinedAggregationOperator[Decimal, Pair, Int64, Decimal], IEnumerable[Pair, Int64], IEnumerable
):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    @overload
    def GetEnumerator(self, mergeOptions: Optional[ParallelMergeOptions]) -> IEnumerator[Pair, int]:
        """

        :param mergeOptions:
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
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[Pair, int]:
        """

        :return:
        """

class NullableDecimalMinMaxAggregationOperator(
    InlinedAggregationOperator[Decimal, Decimal, Decimal], IEnumerable[Decimal], IEnumerable
):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    @overload
    def GetEnumerator(
        self, mergeOptions: Optional[ParallelMergeOptions]
    ) -> IEnumerator[Optional[Decimal]]:
        """

        :param mergeOptions:
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
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[Optional[Decimal]]:
        """

        :return:
        """

class NullableDecimalSumAggregationOperator(
    InlinedAggregationOperator[Decimal, Decimal, Decimal], IEnumerable[Decimal], IEnumerable
):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    @overload
    def GetEnumerator(
        self, mergeOptions: Optional[ParallelMergeOptions]
    ) -> IEnumerator[Optional[Decimal]]:
        """

        :param mergeOptions:
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
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[Optional[Decimal]]:
        """

        :return:
        """

class NullableDoubleAverageAggregationOperator(
    InlinedAggregationOperator[Double, Pair, Int64, Double], IEnumerable[Pair, Int64], IEnumerable
):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    @overload
    def GetEnumerator(self, mergeOptions: Optional[ParallelMergeOptions]) -> IEnumerator[Pair, int]:
        """

        :param mergeOptions:
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
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[Pair, int]:
        """

        :return:
        """

class NullableDoubleMinMaxAggregationOperator(
    InlinedAggregationOperator[Double, Double, Double], IEnumerable[Double], IEnumerable
):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    @overload
    def GetEnumerator(
        self, mergeOptions: Optional[ParallelMergeOptions]
    ) -> IEnumerator[Optional[float]]:
        """

        :param mergeOptions:
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
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[Optional[float]]:
        """

        :return:
        """

class NullableDoubleSumAggregationOperator(
    InlinedAggregationOperator[Double, Double, Double], IEnumerable[Double], IEnumerable
):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    @overload
    def GetEnumerator(
        self, mergeOptions: Optional[ParallelMergeOptions]
    ) -> IEnumerator[Optional[float]]:
        """

        :param mergeOptions:
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
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[Optional[float]]:
        """

        :return:
        """

class NullableFloatAverageAggregationOperator(
    InlinedAggregationOperator[Single, Pair, Int64, Single], IEnumerable[Pair, Int64], IEnumerable
):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    @overload
    def GetEnumerator(self, mergeOptions: Optional[ParallelMergeOptions]) -> IEnumerator[Pair, int]:
        """

        :param mergeOptions:
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
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[Pair, int]:
        """

        :return:
        """

class NullableFloatMinMaxAggregationOperator(
    InlinedAggregationOperator[Single, Single, Single], IEnumerable[Single], IEnumerable
):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    @overload
    def GetEnumerator(
        self, mergeOptions: Optional[ParallelMergeOptions]
    ) -> IEnumerator[Optional[float]]:
        """

        :param mergeOptions:
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
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[Optional[float]]:
        """

        :return:
        """

class NullableFloatSumAggregationOperator(
    InlinedAggregationOperator[Single, Double, Single], IEnumerable[Double], IEnumerable
):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    @overload
    def GetEnumerator(
        self, mergeOptions: Optional[ParallelMergeOptions]
    ) -> IEnumerator[Optional[float]]:
        """

        :param mergeOptions:
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
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[Optional[float]]:
        """

        :return:
        """

class NullableIntAverageAggregationOperator(
    InlinedAggregationOperator[Int32, Pair, Int64, Double], IEnumerable[Pair, Int64], IEnumerable
):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    @overload
    def GetEnumerator(self, mergeOptions: Optional[ParallelMergeOptions]) -> IEnumerator[Pair, int]:
        """

        :param mergeOptions:
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
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[Pair, int]:
        """

        :return:
        """

class NullableIntMinMaxAggregationOperator(
    InlinedAggregationOperator[Int32, Int32, Int32], IEnumerable[Int32], IEnumerable
):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    @overload
    def GetEnumerator(
        self, mergeOptions: Optional[ParallelMergeOptions]
    ) -> IEnumerator[Optional[int]]:
        """

        :param mergeOptions:
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
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[Optional[int]]:
        """

        :return:
        """

class NullableIntSumAggregationOperator(
    InlinedAggregationOperator[Int32, Int32, Int32], IEnumerable[Int32], IEnumerable
):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    @overload
    def GetEnumerator(
        self, mergeOptions: Optional[ParallelMergeOptions]
    ) -> IEnumerator[Optional[int]]:
        """

        :param mergeOptions:
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
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[Optional[int]]:
        """

        :return:
        """

class NullableLongAverageAggregationOperator(
    InlinedAggregationOperator[Int64, Pair, Int64, Double], IEnumerable[Pair, Int64], IEnumerable
):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    @overload
    def GetEnumerator(self, mergeOptions: Optional[ParallelMergeOptions]) -> IEnumerator[Pair, int]:
        """

        :param mergeOptions:
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
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[Pair, int]:
        """

        :return:
        """

class NullableLongMinMaxAggregationOperator(
    InlinedAggregationOperator[Int64, Int64, Int64], IEnumerable[Int64], IEnumerable
):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    @overload
    def GetEnumerator(
        self, mergeOptions: Optional[ParallelMergeOptions]
    ) -> IEnumerator[Optional[int]]:
        """

        :param mergeOptions:
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
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[Optional[int]]:
        """

        :return:
        """

class NullableLongSumAggregationOperator(
    InlinedAggregationOperator[Int64, Int64, Int64], IEnumerable[Int64], IEnumerable
):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    @overload
    def GetEnumerator(
        self, mergeOptions: Optional[ParallelMergeOptions]
    ) -> IEnumerator[Optional[int]]:
        """

        :param mergeOptions:
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
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[Optional[int]]:
        """

        :return:
        """

class OrderPreservingMergeHelper(Generic[TInputOutput, TKey], Object, IMergeHelper[TInputOutput]):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def Execute(self) -> None:
        """"""
    def GetEnumerator(self) -> IEnumerator[TInputOutput]:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetResultsAsArray(self) -> Array[TInputOutput]:
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

class OrderPreservingPipeliningMergeHelper(Generic[TOutput, TKey], Object, IMergeHelper[TOutput]):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def Execute(self) -> None:
        """"""
    def GetEnumerator(self) -> IEnumerator[TOutput]:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetResultsAsArray(self) -> Array[TOutput]:
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

class OrderPreservingPipeliningSpoolingTask(Generic[TOutput, TKey], SpoolingTaskBase):
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
    @classmethod
    def Spool(
        cls,
        groupState: QueryTaskGroupState,
        partitions: PartitionedStream[TOutput, TKey],
        consumerWaiting: Array[bool],
        producerWaiting: Array[bool],
        producerDone: Array[bool],
        buffers: Array[Queue, TOutput],
        bufferLocks: Array[object],
        taskScheduler: TaskScheduler,
        autoBuffered: bool,
    ) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class OrderPreservingSpoolingTask(Generic[TInputOutput, TKey], SpoolingTaskBase):
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

class OrderedGroupByElementSelectorQueryOperatorEnumerator(
    Generic[TSource, TGroupKey, TElement, TOrderKey],
    OrderedGroupByQueryOperatorEnumerator[TSource, TGroupKey, TElement, TOrderKey],
):
    """"""

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

class OrderedGroupByGrouping(
    Generic[TGroupKey, TOrderKey, TElement],
    Object,
    IEnumerable[TElement],
    IEnumerable,
    IGrouping[TGroupKey, TElement],
):
    """"""

    @property
    def Key(self) -> TGroupKey:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

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
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[TElement]:
        """

        :return:
        """

class OrderedGroupByIdentityQueryOperatorEnumerator(
    Generic[TSource, TGroupKey, TOrderKey],
    OrderedGroupByQueryOperatorEnumerator[TSource, TGroupKey, TSource, TOrderKey],
):
    """"""

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

class OrderedGroupByQueryOperatorEnumerator(
    ABC,
    Generic[TSource, TGroupKey, TElement, TOrderKey],
    QueryOperatorEnumerator[IGrouping, TElement, TOrderKey],
):
    """"""

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

class OrderedHashRepartitionEnumerator(
    Generic[TInputOutput, THashKey, TOrderKey], QueryOperatorEnumerator[Pair, THashKey, TOrderKey]
):
    """"""

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

class OrderedHashRepartitionStream(
    Generic[TInputOutput, THashKey, TOrderKey],
    HashRepartitionStream[TInputOutput, THashKey, TOrderKey],
):
    """"""

    @property
    def PartitionCount(self) -> int:
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

class OrderingQueryOperator(
    Generic[TSource], QueryOperator[TSource], IEnumerable[TSource], IEnumerable
):
    """"""

    def __init__(self, child: QueryOperator[TSource], orderOn: bool):
        """

        :param child:
        :param orderOn:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    @overload
    def GetEnumerator(self, mergeOptions: Optional[ParallelMergeOptions]) -> IEnumerator[TSource]:
        """

        :param mergeOptions:
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
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[TSource]:
        """

        :return:
        """

class OrdinalIndexState(Enum):
    """"""

    Indexible: OrdinalIndexState = ...
    """"""
    Correct: OrdinalIndexState = ...
    """"""
    Increasing: OrdinalIndexState = ...
    """"""
    Shuffled: OrdinalIndexState = ...
    """"""

class Pair(Generic[T, U], ValueType):
    """"""

    def __init__(self, first: T, second: U):
        """

        :param first:
        :param second:
        """
    @property
    def First(self) -> T:
        """

        :return:
        """
    @First.setter
    def First(self, value: T) -> None: ...
    @property
    def Second(self) -> U:
        """

        :return:
        """
    @Second.setter
    def Second(self, value: U) -> None: ...
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

class PairComparer(Generic[T, U], Object, IComparer[Pair, U]):
    """"""

    def __init__(self, comparer1: IComparer[T], comparer2: IComparer[U]):
        """

        :param comparer1:
        :param comparer2:
        """
    def Compare(self, x: Pair[T, U], y: Pair[T, U]) -> int:
        """

        :param x:
        :param y:
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

class ParallelEnumerableWrapper(ParallelQuery[Object], IEnumerable[Object], IEnumerable):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

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
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """

class ParallelEnumerableWrapper(Generic[T], ParallelQuery[T], IEnumerable[T], IEnumerable):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

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
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[T]:
        """

        :return:
        """

class PartitionedDataSource(Generic[T], PartitionedStream[T, Int32]):
    """"""

    @property
    def PartitionCount(self) -> int:
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

class PartitionedStream(Generic[TElement, TKey], Object):
    """"""

    @property
    def PartitionCount(self) -> int:
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

class PartitionedStreamMerger(Generic[TOutput], Object, IPartitionedStreamRecipient[TOutput]):
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
    def Receive(self, partitionedStream: PartitionedStream[TOutput, TKey]) -> None:
        """

        :param partitionedStream:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class PartitionerQueryOperator(
    Generic[TElement], QueryOperator[TElement], IEnumerable[TElement], IEnumerable
):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    @overload
    def GetEnumerator(self, mergeOptions: Optional[ParallelMergeOptions]) -> IEnumerator[TElement]:
        """

        :param mergeOptions:
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
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[TElement]:
        """

        :return:
        """

class PipelineSpoolingTask(Generic[TInputOutput, TIgnoreKey], SpoolingTaskBase):
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

class PlinqEtwProvider(EventSource, IDisposable):
    """"""

    @property
    def ConstructionException(self) -> Exception:
        """

        :return:
        """
    @classmethod
    @property
    def CurrentThreadActivityId(cls) -> Guid:
        """

        :return:
        """
    @property
    def Guid(self) -> Guid:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Settings(self) -> EventSourceSettings:
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
    def GetTrait(self, key: str) -> str:
        """

        :param key:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def IsEnabled(self) -> bool:
        """

        :return:
        """
    @overload
    def IsEnabled(self, level: EventLevel, keywords: EventKeywords) -> bool:
        """

        :param level:
        :param keywords:
        :return:
        """
    @overload
    def IsEnabled(self, level: EventLevel, keywords: EventKeywords, channel: EventChannel) -> bool:
        """

        :param level:
        :param keywords:
        :param channel:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def Write(self, eventName: str) -> None:
        """

        :param eventName:
        """
    @overload
    def Write(self, eventName: str, data: T) -> None:
        """

        :param eventName:
        :param data:
        """
    @overload
    def Write(self, eventName: str, options: EventSourceOptions) -> None:
        """

        :param eventName:
        :param options:
        """
    @overload
    def Write(self, eventName: str, options: EventSourceOptions, data: T) -> None:
        """

        :param eventName:
        :param options:
        :param data:
        """
    @overload
    def Write(self, eventName: str, options: EventSourceOptions, data: T) -> None:
        """

        :param eventName:
        :param options:
        :param data:
        """
    @overload
    def Write(
        self,
        eventName: str,
        options: EventSourceOptions,
        activityId: Guid,
        relatedActivityId: Guid,
        data: T,
    ) -> None:
        """

        :param eventName:
        :param options:
        :param activityId:
        :param relatedActivityId:
        :param data:
        """
    EventCommandExecuted: EventType[EventHandler[EventCommandEventArgs]] = ...
    """"""

    class Tasks(Object):
        """"""

        ForkJoin: Final[ClassVar[EventTask]] = ...
        """"""
        Query: Final[ClassVar[EventTask]] = ...
        """"""
        def __init__(self):
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

class Producer(Generic[TKey], ValueType):
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

class ProducerComparerInt(Object, IComparer[Producer[Int32]]):
    """"""

    def __init__(self):
        """"""
    def Compare(self, x: Producer[int], y: Producer[int]) -> int:
        """

        :param x:
        :param y:
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

class QueryAggregationOptions(Enum):
    """"""

    _None: QueryAggregationOptions = ...
    """"""
    Associative: QueryAggregationOptions = ...
    """"""
    Commutative: QueryAggregationOptions = ...
    """"""
    AssociativeCommutative: QueryAggregationOptions = ...
    """"""

class QueryExecutionOption(
    Generic[TSource], QueryOperator[TSource], IEnumerable[TSource], IEnumerable
):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    @overload
    def GetEnumerator(self, mergeOptions: Optional[ParallelMergeOptions]) -> IEnumerator[TSource]:
        """

        :param mergeOptions:
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
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[TSource]:
        """

        :return:
        """

class QueryLifecycle(ABC, Object):
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

class QueryOpeningEnumerator(
    Generic[TOutput], Object, IEnumerator[TOutput], IEnumerator, IDisposable
):
    """"""

    @property
    def Current(self) -> object:
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
    def MoveNext(self) -> bool:
        """

        :return:
        """
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class QueryOperator(
    ABC, Generic[TOutput], ParallelQuery[TOutput], IEnumerable[TOutput], IEnumerable
):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    @overload
    def GetEnumerator(self, mergeOptions: Optional[ParallelMergeOptions]) -> IEnumerator[TOutput]:
        """

        :param mergeOptions:
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
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[TOutput]:
        """

        :return:
        """

class QueryOperatorEnumerator(ABC, Generic[TElement, TKey], Object):
    """"""

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

class QueryResults(ABC, Generic[T], Object, ICollection[T], IEnumerable[T], IList[T], IEnumerable):
    """"""

    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def Item(self) -> T:
        """

        :return:
        """
    @Item.setter
    def Item(self, value: T) -> None: ...
    def Add(self, item: T) -> None:
        """

        :param item:
        """
    def Clear(self) -> None:
        """"""
    def Contains(self, item: T) -> bool:
        """

        :param item:
        :return:
        """
    def CopyTo(self, array: Array[T], arrayIndex: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

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
    def IndexOf(self, item: T) -> int:
        """

        :param item:
        :return:
        """
    def Insert(self, index: int, item: T) -> None:
        """

        :param index:
        :param item:
        """
    def Remove(self, item: T) -> bool:
        """

        :param item:
        :return:
        """
    def RemoveAt(self, index: int) -> None:
        """

        :param index:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def __contains__(self, value: T) -> bool:
        """

        :param value:
        :return:
        """
    def __getitem__(self, index: int) -> T:
        """

        :param index:
        :return:
        """
    @overload
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[T]:
        """

        :return:
        """
    def __len__(self) -> int:
        """

        :return:
        """
    def __setitem__(self, index: int, value: T) -> None:
        """

        :param index:
        :param value:
        """

class QuerySettings(ValueType):
    """"""

    def CleanStateAtQueryEnd(self) -> None:
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

class QueryTask(ABC, Object):
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

class QueryTaskGroupState(Object):
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

class RangeEnumerable(
    ParallelQuery[Int32], IEnumerable[Int32], IEnumerable, IParallelPartitionable[Int32]
):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetPartitions(self, partitionCount: int) -> Array[QueryOperatorEnumerator, int]:
        """

        :param partitionCount:
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
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[int]:
        """

        :return:
        """

class RepeatEnumerable(
    Generic[TResult],
    ParallelQuery[TResult],
    IEnumerable[TResult],
    IEnumerable,
    IParallelPartitionable[TResult],
):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetPartitions(self, partitionCount: int) -> Array[QueryOperatorEnumerator, int]:
        """

        :param partitionCount:
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
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[TResult]:
        """

        :return:
        """

class ReverseComparer(Generic[T], Object, IComparer[T]):
    """"""

    def Compare(self, x: T, y: T) -> int:
        """

        :param x:
        :param y:
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

class ReverseQueryOperator(
    Generic[TSource], UnaryQueryOperator[TSource, TSource], IEnumerable[TSource], IEnumerable
):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    @overload
    def GetEnumerator(self, mergeOptions: Optional[ParallelMergeOptions]) -> IEnumerator[TSource]:
        """

        :param mergeOptions:
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
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[TSource]:
        """

        :return:
        """

class ScanQueryOperator(
    Generic[TElement], QueryOperator[TElement], IEnumerable[TElement], IEnumerable
):
    """"""

    @property
    def Data(self) -> IEnumerable[TElement]:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    @overload
    def GetEnumerator(self, mergeOptions: Optional[ParallelMergeOptions]) -> IEnumerator[TElement]:
        """

        :param mergeOptions:
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
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[TElement]:
        """

        :return:
        """

class Scheduling(ABC, Object):
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

class SelectManyQueryOperator(
    Generic[TLeftInput, TRightInput, TOutput],
    UnaryQueryOperator[TLeftInput, TOutput],
    IEnumerable[TOutput],
    IEnumerable,
):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    @overload
    def GetEnumerator(self, mergeOptions: Optional[ParallelMergeOptions]) -> IEnumerator[TOutput]:
        """

        :param mergeOptions:
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
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[TOutput]:
        """

        :return:
        """

class SelectQueryOperator(
    Generic[TInput, TOutput], UnaryQueryOperator[TInput, TOutput], IEnumerable[TOutput], IEnumerable
):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    @overload
    def GetEnumerator(self, mergeOptions: Optional[ParallelMergeOptions]) -> IEnumerator[TOutput]:
        """

        :param mergeOptions:
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
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[TOutput]:
        """

        :return:
        """

class Shared(Generic[T], Object):
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

class SingleQueryOperator(
    Generic[TSource], UnaryQueryOperator[TSource, TSource], IEnumerable[TSource], IEnumerable
):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    @overload
    def GetEnumerator(self, mergeOptions: Optional[ParallelMergeOptions]) -> IEnumerator[TSource]:
        """

        :param mergeOptions:
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
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[TSource]:
        """

        :return:
        """

class SortHelper(ABC, Generic[TInputOutput], Object):
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

class SortHelper(Generic[TInputOutput, TKey], SortHelper[TInputOutput], IDisposable):
    """"""

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

class SortQueryOperator(
    Generic[TInputOutput, TSortKey],
    UnaryQueryOperator[TInputOutput, TInputOutput],
    IEnumerable[TInputOutput],
    IEnumerable,
    IOrderedEnumerable[TInputOutput],
):
    """"""

    def CreateOrderedEnumerable(
        self, keySelector: Func[TInputOutput, TKey], comparer: IComparer[TKey], descending: bool
    ) -> IOrderedEnumerable[TInputOutput]:
        """

        :param keySelector:
        :param comparer:
        :param descending:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    @overload
    def GetEnumerator(
        self, mergeOptions: Optional[ParallelMergeOptions]
    ) -> IEnumerator[TInputOutput]:
        """

        :param mergeOptions:
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
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[TInputOutput]:
        """

        :return:
        """

class SortQueryOperatorEnumerator(
    Generic[TInputOutput, TKey, TSortKey], QueryOperatorEnumerator[TInputOutput, TSortKey]
):
    """"""

    @property
    def KeyComparer(self) -> IComparer[TSortKey]:
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

class SortQueryOperatorResults(
    Generic[TInputOutput, TSortKey],
    QueryResults[TInputOutput],
    ICollection[TInputOutput],
    IEnumerable[TInputOutput],
    IList[TInputOutput],
    IEnumerable,
):
    """"""

    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def Item(self) -> TInputOutput:
        """

        :return:
        """
    @Item.setter
    def Item(self, value: TInputOutput) -> None: ...
    def Add(self, item: TInputOutput) -> None:
        """

        :param item:
        """
    def Clear(self) -> None:
        """"""
    def Contains(self, item: TInputOutput) -> bool:
        """

        :param item:
        :return:
        """
    def CopyTo(self, array: Array[TInputOutput], arrayIndex: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

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
    def IndexOf(self, item: TInputOutput) -> int:
        """

        :param item:
        :return:
        """
    def Insert(self, index: int, item: TInputOutput) -> None:
        """

        :param index:
        :param item:
        """
    def Remove(self, item: TInputOutput) -> bool:
        """

        :param item:
        :return:
        """
    def RemoveAt(self, index: int) -> None:
        """

        :param index:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def __contains__(self, value: TInputOutput) -> bool:
        """

        :param value:
        :return:
        """
    def __getitem__(self, index: int) -> TInputOutput:
        """

        :param index:
        :return:
        """
    @overload
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[TInputOutput]:
        """

        :return:
        """
    def __len__(self) -> int:
        """

        :return:
        """
    def __setitem__(self, index: int, value: TInputOutput) -> None:
        """

        :param index:
        :param value:
        """

class SpoolingTask(ABC, Object):
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

class SpoolingTaskBase(ABC, QueryTask):
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

class StopAndGoSpoolingTask(Generic[TInputOutput, TIgnoreKey], SpoolingTaskBase):
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

class SynchronousChannel(Generic[T], Object):
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

class SynchronousChannelMergeEnumerator(
    Generic[T], MergeEnumerator[T], IEnumerator[T], IEnumerator, IDisposable
):
    """"""

    @property
    def Current(self) -> object:
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
    def MoveNext(self) -> bool:
        """

        :return:
        """
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class TakeOrSkipQueryOperator(
    Generic[TResult], UnaryQueryOperator[TResult, TResult], IEnumerable[TResult], IEnumerable
):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    @overload
    def GetEnumerator(self, mergeOptions: Optional[ParallelMergeOptions]) -> IEnumerator[TResult]:
        """

        :param mergeOptions:
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
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[TResult]:
        """

        :return:
        """

class TakeOrSkipWhileQueryOperator(
    Generic[TResult], UnaryQueryOperator[TResult, TResult], IEnumerable[TResult], IEnumerable
):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    @overload
    def GetEnumerator(self, mergeOptions: Optional[ParallelMergeOptions]) -> IEnumerator[TResult]:
        """

        :param mergeOptions:
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
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[TResult]:
        """

        :return:
        """

class TraceHelpers(ABC, Object):
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

class UnaryQueryOperator(
    ABC, Generic[TInput, TOutput], QueryOperator[TOutput], IEnumerable[TOutput], IEnumerable
):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    @overload
    def GetEnumerator(self, mergeOptions: Optional[ParallelMergeOptions]) -> IEnumerator[TOutput]:
        """

        :param mergeOptions:
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
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[TOutput]:
        """

        :return:
        """

class UnionQueryOperator(
    Generic[TInputOutput],
    BinaryQueryOperator[TInputOutput, TInputOutput, TInputOutput],
    IEnumerable[TInputOutput],
    IEnumerable,
):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    @overload
    def GetEnumerator(
        self, mergeOptions: Optional[ParallelMergeOptions]
    ) -> IEnumerator[TInputOutput]:
        """

        :param mergeOptions:
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
    def WrapPartitionedStream(
        self,
        leftPartitionedStream: PartitionedStream[TInputOutput, TLeftKey],
        rightPartitionedStream: PartitionedStream[TInputOutput, TRightKey],
        outputRecipient: IPartitionedStreamRecipient[TInputOutput],
        preferStriping: bool,
        settings: QuerySettings,
    ) -> None:
        """

        :param leftPartitionedStream:
        :param rightPartitionedStream:
        :param outputRecipient:
        :param preferStriping:
        :param settings:
        """
    @overload
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[TInputOutput]:
        """

        :return:
        """

class UnorderedHashRepartitionStream(
    Generic[TInputOutput, THashKey, TIgnoreKey],
    HashRepartitionStream[TInputOutput, THashKey, Int32],
):
    """"""

    @property
    def PartitionCount(self) -> int:
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

class Util(ABC, Object):
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

class WhereQueryOperator(
    Generic[TInputOutput],
    UnaryQueryOperator[TInputOutput, TInputOutput],
    IEnumerable[TInputOutput],
    IEnumerable,
):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    @overload
    def GetEnumerator(
        self, mergeOptions: Optional[ParallelMergeOptions]
    ) -> IEnumerator[TInputOutput]:
        """

        :param mergeOptions:
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
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[TInputOutput]:
        """

        :return:
        """

class Wrapper(Generic[T], ValueType):
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

class WrapperEqualityComparer(Generic[T], ValueType, IEqualityComparer[Wrapper[T]]):
    """"""

    @overload
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def Equals(self, x: Wrapper[T], y: Wrapper[T]) -> bool:
        """

        :param x:
        :param y:
        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetHashCode(self, obj: Wrapper[T]) -> int:
        """

        :param obj:
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

class ZipQueryOperator(
    Generic[TLeftInput, TRightInput, TOutput],
    QueryOperator[TOutput],
    IEnumerable[TOutput],
    IEnumerable,
):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    @overload
    def GetEnumerator(self, mergeOptions: Optional[ParallelMergeOptions]) -> IEnumerator[TOutput]:
        """

        :param mergeOptions:
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
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[TOutput]:
        """

        :return:
        """
