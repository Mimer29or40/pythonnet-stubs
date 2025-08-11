"""Automatically generated stubs for C# namespace: System.Linq.Parallel."""

from abc import ABC
from collections.abc import Iterator
from typing import ClassVar
from typing import Self
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
from System.Linq import IGrouping
from System.Linq import ILookup
from System.Linq import IOrderedEnumerable
from System.Linq import ParallelMergeOptions
from System.Linq import ParallelQuery
from System.Threading import CancellationToken
from System.Threading import ManualResetEventSlim
from System.Threading import WaitHandle
from System.Threading.Tasks import TaskScheduler

class EventType[T]:
    def __iadd__(self, other: T) -> Self: ...
    def __isub__(self, other: T) -> Self: ...

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class AnyAllSearchOperator[TInput](
    UnaryQueryOperator[TInput, Boolean], IEnumerable[Boolean], IEnumerable
):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetEnumerator(self) -> IEnumerator[bool]:
        """"""
    @overload
    def GetEnumerator(self, mergeOptions: ParallelMergeOptions | None) -> IEnumerator[bool]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __iter__(self) -> Iterator[bool]:
        """"""
    @overload
    def __iter__(self, mergeOptions: ParallelMergeOptions | None) -> Iterator[bool]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ArrayMergeHelper[TInputOutput](Object, IMergeHelper[TInputOutput]):
    """"""
    def __init__(self, settings: QuerySettings, queryResults: QueryResults[TInputOutput]) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Execute(self) -> None:
        """"""
    def GetEnumerator(self) -> IEnumerator[TInputOutput]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetResultsAsArray(self) -> Array[TInputOutput]:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def __iter__(self) -> Iterator[TInputOutput]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class AssociativeAggregationOperator[TInput, TIntermediate, TOutput](
    UnaryQueryOperator[TInput, TIntermediate], IEnumerable[TIntermediate], IEnumerable
):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetEnumerator[TIntermediate](self) -> IEnumerator[TIntermediate]:
        """"""
    @overload
    def GetEnumerator[TIntermediate](
        self, mergeOptions: ParallelMergeOptions | None
    ) -> IEnumerator[TIntermediate]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __iter__[TIntermediate](self) -> Iterator[TIntermediate]:
        """"""
    @overload
    def __iter__[TIntermediate](
        self, mergeOptions: ParallelMergeOptions | None
    ) -> Iterator[TIntermediate]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class AsynchronousChannelMergeEnumerator[T](
    MergeEnumerator[T], IEnumerator[T], IEnumerator, IDisposable
):
    """"""
    @property
    def Current(self) -> T:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def MoveNext(self) -> bool:
        """"""
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class AsynchronousChannel[T](Object, IDisposable):
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
class BinaryQueryOperator[TLeftInput, TRightInput, TOutput](
    ABC, QueryOperator[TOutput], IEnumerable[TOutput], IEnumerable
):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetEnumerator[TOutput](self) -> IEnumerator[TOutput]:
        """"""
    @overload
    def GetEnumerator(self, mergeOptions: ParallelMergeOptions | None) -> IEnumerator[TOutput]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def WrapPartitionedStream[TLeftKey, TRightKey](
        self,
        leftPartitionedStream: PartitionedStream[TLeftInput, TLeftKey],
        rightPartitionedStream: PartitionedStream[TRightInput, TRightKey],
        outputRecipient: IPartitionedStreamRecipient[TOutput],
        preferStriping: bool,
        settings: QuerySettings,
    ) -> None:
        """"""
    @overload
    def __iter__[TOutput](self) -> Iterator[TOutput]:
        """"""
    @overload
    def __iter__(self, mergeOptions: ParallelMergeOptions | None) -> Iterator[TOutput]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CancellableEnumerable(ABC, Object):
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
class CancellationState(Object):
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
class ConcatKey[TLeftKey, TRightKey](ValueType):
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
class ConcatQueryOperator[TSource](
    BinaryQueryOperator[TSource, TSource, TSource], IEnumerable[TSource], IEnumerable
):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetEnumerator[TSource](self) -> IEnumerator[TSource]:
        """"""
    @overload
    def GetEnumerator[TSource](
        self, mergeOptions: ParallelMergeOptions | None
    ) -> IEnumerator[TSource]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def WrapPartitionedStream[TSource, TLeftKey, TRightKey](
        self,
        leftStream: PartitionedStream[TSource, TLeftKey],
        rightStream: PartitionedStream[TSource, TRightKey],
        outputRecipient: IPartitionedStreamRecipient[TSource],
        preferStriping: bool,
        settings: QuerySettings,
    ) -> None:
        """"""
    @overload
    def __iter__[TSource](self) -> Iterator[TSource]:
        """"""
    @overload
    def __iter__[TSource](self, mergeOptions: ParallelMergeOptions | None) -> Iterator[TSource]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ContainsSearchOperator[TInput](
    UnaryQueryOperator[TInput, Boolean], IEnumerable[Boolean], IEnumerable
):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetEnumerator(self) -> IEnumerator[bool]:
        """"""
    @overload
    def GetEnumerator(self, mergeOptions: ParallelMergeOptions | None) -> IEnumerator[bool]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __iter__(self) -> Iterator[bool]:
        """"""
    @overload
    def __iter__(self, mergeOptions: ParallelMergeOptions | None) -> Iterator[bool]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CountAggregationOperator[TSource](
    InlinedAggregationOperator[TSource, Int32, Int32], IEnumerable[Int32], IEnumerable
):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetEnumerator(self) -> IEnumerator[int]:
        """"""
    @overload
    def GetEnumerator(self, mergeOptions: ParallelMergeOptions | None) -> IEnumerator[int]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __iter__(self) -> Iterator[int]:
        """"""
    @overload
    def __iter__(self, mergeOptions: ParallelMergeOptions | None) -> Iterator[int]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class DecimalAverageAggregationOperator(
    InlinedAggregationOperator[Decimal, Pair[Decimal, Int64], Decimal],
    IEnumerable[Pair[Decimal, Int64]],
    IEnumerable,
):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetEnumerator(self) -> IEnumerator[Pair[Decimal, int]]:
        """"""
    @overload
    def GetEnumerator(
        self, mergeOptions: ParallelMergeOptions | None
    ) -> IEnumerator[Pair[Decimal, int]]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __iter__(self) -> Iterator[Pair[Decimal, int]]:
        """"""
    @overload
    def __iter__(self, mergeOptions: ParallelMergeOptions | None) -> Iterator[Pair[Decimal, int]]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class DecimalMinMaxAggregationOperator(
    InlinedAggregationOperator[Decimal, Decimal, Decimal], IEnumerable[Decimal], IEnumerable
):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetEnumerator(self) -> IEnumerator[Decimal]:
        """"""
    @overload
    def GetEnumerator(self, mergeOptions: ParallelMergeOptions | None) -> IEnumerator[Decimal]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __iter__(self) -> Iterator[Decimal]:
        """"""
    @overload
    def __iter__(self, mergeOptions: ParallelMergeOptions | None) -> Iterator[Decimal]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class DecimalSumAggregationOperator(
    InlinedAggregationOperator[Decimal, Decimal, Decimal], IEnumerable[Decimal], IEnumerable
):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetEnumerator(self) -> IEnumerator[Decimal]:
        """"""
    @overload
    def GetEnumerator(self, mergeOptions: ParallelMergeOptions | None) -> IEnumerator[Decimal]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __iter__(self) -> Iterator[Decimal]:
        """"""
    @overload
    def __iter__(self, mergeOptions: ParallelMergeOptions | None) -> Iterator[Decimal]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class DefaultIfEmptyQueryOperator[TSource](
    UnaryQueryOperator[TSource, TSource], IEnumerable[TSource], IEnumerable
):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetEnumerator[TSource](self) -> IEnumerator[TSource]:
        """"""
    @overload
    def GetEnumerator[TSource](
        self, mergeOptions: ParallelMergeOptions | None
    ) -> IEnumerator[TSource]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __iter__[TSource](self) -> Iterator[TSource]:
        """"""
    @overload
    def __iter__[TSource](self, mergeOptions: ParallelMergeOptions | None) -> Iterator[TSource]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class DefaultMergeHelper[TInputOutput, TIgnoreKey](Object, IMergeHelper[TInputOutput]):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Execute(self) -> None:
        """"""
    def GetEnumerator(self) -> IEnumerator[TInputOutput]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetResultsAsArray(self) -> Array[TInputOutput]:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def __iter__(self) -> Iterator[TInputOutput]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class DistinctQueryOperator[TInputOutput](
    UnaryQueryOperator[TInputOutput, TInputOutput], IEnumerable[TInputOutput], IEnumerable
):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetEnumerator[TInputOutput](self) -> IEnumerator[TInputOutput]:
        """"""
    @overload
    def GetEnumerator[TInputOutput](
        self, mergeOptions: ParallelMergeOptions | None
    ) -> IEnumerator[TInputOutput]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __iter__[TInputOutput](self) -> Iterator[TInputOutput]:
        """"""
    @overload
    def __iter__[TInputOutput](
        self, mergeOptions: ParallelMergeOptions | None
    ) -> Iterator[TInputOutput]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class DoubleAverageAggregationOperator(
    InlinedAggregationOperator[Double, Pair[Double, Int64], Double],
    IEnumerable[Pair[Double, Int64]],
    IEnumerable,
):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetEnumerator(self) -> IEnumerator[Pair[float, int]]:
        """"""
    @overload
    def GetEnumerator(
        self, mergeOptions: ParallelMergeOptions | None
    ) -> IEnumerator[Pair[float, int]]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __iter__(self) -> Iterator[Pair[float, int]]:
        """"""
    @overload
    def __iter__(self, mergeOptions: ParallelMergeOptions | None) -> Iterator[Pair[float, int]]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class DoubleMinMaxAggregationOperator(
    InlinedAggregationOperator[Double, Double, Double], IEnumerable[Double], IEnumerable
):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetEnumerator(self) -> IEnumerator[float]:
        """"""
    @overload
    def GetEnumerator(self, mergeOptions: ParallelMergeOptions | None) -> IEnumerator[float]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __iter__(self) -> Iterator[float]:
        """"""
    @overload
    def __iter__(self, mergeOptions: ParallelMergeOptions | None) -> Iterator[float]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class DoubleSumAggregationOperator(
    InlinedAggregationOperator[Double, Double, Double], IEnumerable[Double], IEnumerable
):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetEnumerator(self) -> IEnumerator[float]:
        """"""
    @overload
    def GetEnumerator(self, mergeOptions: ParallelMergeOptions | None) -> IEnumerator[float]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __iter__(self) -> Iterator[float]:
        """"""
    @overload
    def __iter__(self, mergeOptions: ParallelMergeOptions | None) -> Iterator[float]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ElementAtQueryOperator[TSource](
    UnaryQueryOperator[TSource, TSource], IEnumerable[TSource], IEnumerable
):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetEnumerator[TSource](self) -> IEnumerator[TSource]:
        """"""
    @overload
    def GetEnumerator[TSource](
        self, mergeOptions: ParallelMergeOptions | None
    ) -> IEnumerator[TSource]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __iter__[TSource](self) -> Iterator[TSource]:
        """"""
    @overload
    def __iter__[TSource](self, mergeOptions: ParallelMergeOptions | None) -> Iterator[TSource]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class EmptyEnumerable[T](ParallelQuery[T], IEnumerable[T], IEnumerable):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator[T](self) -> IEnumerator[T]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def __iter__[T](self) -> Iterator[T]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class EmptyEnumerator[T](
    QueryOperatorEnumerator[T, Int32], IEnumerator[T], IEnumerator, IDisposable
):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Current(self) -> T:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def MoveNext(self) -> bool:
        """"""
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class EnumerableWrapperWeakToStrong(Object, IEnumerable[Object], IEnumerable):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator[object]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def __iter__(self) -> Iterator[object]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ExceptQueryOperator[TInputOutput](
    BinaryQueryOperator[TInputOutput, TInputOutput, TInputOutput],
    IEnumerable[TInputOutput],
    IEnumerable,
):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetEnumerator[TInputOutput](self) -> IEnumerator[TInputOutput]:
        """"""
    @overload
    def GetEnumerator[TInputOutput](
        self, mergeOptions: ParallelMergeOptions | None
    ) -> IEnumerator[TInputOutput]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def WrapPartitionedStream[TInputOutput, TLeftKey, TRightKey](
        self,
        leftStream: PartitionedStream[TInputOutput, TLeftKey],
        rightStream: PartitionedStream[TInputOutput, TRightKey],
        outputRecipient: IPartitionedStreamRecipient[TInputOutput],
        preferStriping: bool,
        settings: QuerySettings,
    ) -> None:
        """"""
    @overload
    def __iter__[TInputOutput](self) -> Iterator[TInputOutput]:
        """"""
    @overload
    def __iter__[TInputOutput](
        self, mergeOptions: ParallelMergeOptions | None
    ) -> Iterator[TInputOutput]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ExceptionAggregator(ABC, Object):
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
class ExchangeUtilities(ABC, Object):
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
class FirstQueryOperator[TSource](
    UnaryQueryOperator[TSource, TSource], IEnumerable[TSource], IEnumerable
):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetEnumerator[TSource](self) -> IEnumerator[TSource]:
        """"""
    @overload
    def GetEnumerator[TSource](
        self, mergeOptions: ParallelMergeOptions | None
    ) -> IEnumerator[TSource]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __iter__[TSource](self) -> Iterator[TSource]:
        """"""
    @overload
    def __iter__[TSource](self, mergeOptions: ParallelMergeOptions | None) -> Iterator[TSource]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class FixedMaxHeap[TElement](Object):
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
class FloatAverageAggregationOperator(
    InlinedAggregationOperator[Single, Pair[Double, Int64], Single],
    IEnumerable[Pair[Double, Int64]],
    IEnumerable,
):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetEnumerator(self) -> IEnumerator[Pair[float, int]]:
        """"""
    @overload
    def GetEnumerator(
        self, mergeOptions: ParallelMergeOptions | None
    ) -> IEnumerator[Pair[float, int]]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __iter__(self) -> Iterator[Pair[float, int]]:
        """"""
    @overload
    def __iter__(self, mergeOptions: ParallelMergeOptions | None) -> Iterator[Pair[float, int]]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class FloatMinMaxAggregationOperator(
    InlinedAggregationOperator[Single, Single, Single], IEnumerable[Single], IEnumerable
):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetEnumerator(self) -> IEnumerator[float]:
        """"""
    @overload
    def GetEnumerator(self, mergeOptions: ParallelMergeOptions | None) -> IEnumerator[float]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __iter__(self) -> Iterator[float]:
        """"""
    @overload
    def __iter__(self, mergeOptions: ParallelMergeOptions | None) -> Iterator[float]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class FloatSumAggregationOperator(
    InlinedAggregationOperator[Single, Double, Single], IEnumerable[Double], IEnumerable
):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetEnumerator(self) -> IEnumerator[float]:
        """"""
    @overload
    def GetEnumerator(self, mergeOptions: ParallelMergeOptions | None) -> IEnumerator[float]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __iter__(self) -> Iterator[float]:
        """"""
    @overload
    def __iter__(self, mergeOptions: ParallelMergeOptions | None) -> Iterator[float]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ForAllOperator[TInput](UnaryQueryOperator[TInput, TInput], IEnumerable[TInput], IEnumerable):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetEnumerator[TInput](self) -> IEnumerator[TInput]:
        """"""
    @overload
    def GetEnumerator[TInput](
        self, mergeOptions: ParallelMergeOptions | None
    ) -> IEnumerator[TInput]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __iter__[TInput](self) -> Iterator[TInput]:
        """"""
    @overload
    def __iter__[TInput](self, mergeOptions: ParallelMergeOptions | None) -> Iterator[TInput]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ForAllSpoolingTask[TInputOutput, TIgnoreKey](SpoolingTaskBase):
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
class GroupByElementSelectorQueryOperatorEnumerator[TSource, TGroupKey, TElement, TOrderKey](
    GroupByQueryOperatorEnumerator[TSource, TGroupKey, TElement, TOrderKey]
):
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
class GroupByGrouping[TGroupKey, TElement](
    Object, IEnumerable[TElement], IEnumerable, IGrouping[TGroupKey, TElement]
):
    """"""
    @property
    def Key(self) -> TGroupKey:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator[TElement](self) -> IEnumerator[TElement]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def __iter__[TElement](self) -> Iterator[TElement]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class GroupByIdentityQueryOperatorEnumerator[TSource, TGroupKey, TOrderKey](
    GroupByQueryOperatorEnumerator[TSource, TGroupKey, TSource, TOrderKey]
):
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
class GroupByQueryOperatorEnumerator[TSource, TGroupKey, TElement, TOrderKey](
    ABC, QueryOperatorEnumerator[IGrouping[TGroupKey, TElement], TOrderKey]
):
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
class GroupByQueryOperator[TSource, TGroupKey, TElement](
    UnaryQueryOperator[TSource, IGrouping[TGroupKey, TElement]],
    IEnumerable[IGrouping[TGroupKey, TElement]],
    IEnumerable,
):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetEnumerator[TGroupKey, TElement](self) -> IEnumerator[IGrouping[TGroupKey, TElement]]:
        """"""
    @overload
    def GetEnumerator[TGroupKey, TElement](
        self, mergeOptions: ParallelMergeOptions | None
    ) -> IEnumerator[IGrouping[TGroupKey, TElement]]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __iter__[TGroupKey, TElement](self) -> Iterator[IGrouping[TGroupKey, TElement]]:
        """"""
    @overload
    def __iter__[TGroupKey, TElement](
        self, mergeOptions: ParallelMergeOptions | None
    ) -> Iterator[IGrouping[TGroupKey, TElement]]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class GroupJoinQueryOperator[TLeftInput, TRightInput, TKey, TOutput](
    BinaryQueryOperator[TLeftInput, TRightInput, TOutput], IEnumerable[TOutput], IEnumerable
):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetEnumerator[TOutput](self) -> IEnumerator[TOutput]:
        """"""
    @overload
    def GetEnumerator(self, mergeOptions: ParallelMergeOptions | None) -> IEnumerator[TOutput]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def WrapPartitionedStream[TLeftKey, TRightKey](
        self,
        leftStream: PartitionedStream[TLeftInput, TLeftKey],
        rightStream: PartitionedStream[TRightInput, TRightKey],
        outputRecipient: IPartitionedStreamRecipient[TOutput],
        preferStriping: bool,
        settings: QuerySettings,
    ) -> None:
        """"""
    @overload
    def __iter__[TOutput](self) -> Iterator[TOutput]:
        """"""
    @overload
    def __iter__(self, mergeOptions: ParallelMergeOptions | None) -> Iterator[TOutput]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class GrowingArray[T](Object):
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
class HashJoinQueryOperatorEnumerator[TLeftInput, TLeftKey, TRightInput, THashKey, TOutput](
    QueryOperatorEnumerator[TOutput, TLeftKey]
):
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
class HashLookup[TKey, TValue](Object):
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
class HashRepartitionEnumerator[TInputOutput, THashKey, TIgnoreKey](
    QueryOperatorEnumerator[Pair[TInputOutput, THashKey], Int32]
):
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
class HashRepartitionStream[TInputOutput, THashKey, TOrderKey](
    ABC, PartitionedStream[Pair[TInputOutput, THashKey], TOrderKey]
):
    """"""
    @property
    def PartitionCount(self) -> int:
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
class IMergeHelper[TInputOutput](ABC):
    """"""
    def Execute(self) -> None:
        """"""
    def GetEnumerator(self) -> IEnumerator[TInputOutput]:
        """"""
    def GetResultsAsArray(self) -> Array[TInputOutput]:
        """"""
    def __iter__(self) -> Iterator[TInputOutput]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IParallelPartitionable[T](ABC):
    """"""
    def GetPartitions(self, partitionCount: int) -> Array[QueryOperatorEnumerator[T, int]]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IPartitionedStreamRecipient[TElement](ABC):
    """"""
    def Receive[TKey](self, partitionedStream: PartitionedStream[TElement, TKey]) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IndexedSelectQueryOperator[TInput, TOutput](
    UnaryQueryOperator[TInput, TOutput], IEnumerable[TOutput], IEnumerable
):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetEnumerator[TOutput](self) -> IEnumerator[TOutput]:
        """"""
    @overload
    def GetEnumerator(self, mergeOptions: ParallelMergeOptions | None) -> IEnumerator[TOutput]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __iter__[TOutput](self) -> Iterator[TOutput]:
        """"""
    @overload
    def __iter__(self, mergeOptions: ParallelMergeOptions | None) -> Iterator[TOutput]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IndexedWhereQueryOperator[TInputOutput](
    UnaryQueryOperator[TInputOutput, TInputOutput], IEnumerable[TInputOutput], IEnumerable
):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetEnumerator[TInputOutput](self) -> IEnumerator[TInputOutput]:
        """"""
    @overload
    def GetEnumerator[TInputOutput](
        self, mergeOptions: ParallelMergeOptions | None
    ) -> IEnumerator[TInputOutput]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __iter__[TInputOutput](self) -> Iterator[TInputOutput]:
        """"""
    @overload
    def __iter__[TInputOutput](
        self, mergeOptions: ParallelMergeOptions | None
    ) -> Iterator[TInputOutput]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class InlinedAggregationOperatorEnumerator[TIntermediate](
    ABC, QueryOperatorEnumerator[TIntermediate, Int32]
):
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
class InlinedAggregationOperator[TSource, TIntermediate, TResult](
    ABC, UnaryQueryOperator[TSource, TIntermediate], IEnumerable[TIntermediate], IEnumerable
):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetEnumerator[TIntermediate](self) -> IEnumerator[TIntermediate]:
        """"""
    @overload
    def GetEnumerator[TIntermediate](
        self, mergeOptions: ParallelMergeOptions | None
    ) -> IEnumerator[TIntermediate]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __iter__[TIntermediate](self) -> Iterator[TIntermediate]:
        """"""
    @overload
    def __iter__[TIntermediate](
        self, mergeOptions: ParallelMergeOptions | None
    ) -> Iterator[TIntermediate]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IntAverageAggregationOperator(
    InlinedAggregationOperator[Int32, Pair[Int64, Int64], Double],
    IEnumerable[Pair[Int64, Int64]],
    IEnumerable,
):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetEnumerator(self) -> IEnumerator[Pair[int, int]]:
        """"""
    @overload
    def GetEnumerator(
        self, mergeOptions: ParallelMergeOptions | None
    ) -> IEnumerator[Pair[int, int]]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __iter__(self) -> Iterator[Pair[int, int]]:
        """"""
    @overload
    def __iter__(self, mergeOptions: ParallelMergeOptions | None) -> Iterator[Pair[int, int]]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IntMinMaxAggregationOperator(
    InlinedAggregationOperator[Int32, Int32, Int32], IEnumerable[Int32], IEnumerable
):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetEnumerator(self) -> IEnumerator[int]:
        """"""
    @overload
    def GetEnumerator(self, mergeOptions: ParallelMergeOptions | None) -> IEnumerator[int]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __iter__(self) -> Iterator[int]:
        """"""
    @overload
    def __iter__(self, mergeOptions: ParallelMergeOptions | None) -> Iterator[int]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IntSumAggregationOperator(
    InlinedAggregationOperator[Int32, Int32, Int32], IEnumerable[Int32], IEnumerable
):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetEnumerator(self) -> IEnumerator[int]:
        """"""
    @overload
    def GetEnumerator(self, mergeOptions: ParallelMergeOptions | None) -> IEnumerator[int]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __iter__(self) -> Iterator[int]:
        """"""
    @overload
    def __iter__(self, mergeOptions: ParallelMergeOptions | None) -> Iterator[int]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IntValueEvent(ManualResetEventSlim, IDisposable):
    """"""
    @property
    def IsSet(self) -> bool:
        """"""
    @property
    def SpinCount(self) -> int:
        """"""
    @property
    def WaitHandle(self) -> WaitHandle:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Reset(self) -> None:
        """"""
    def Set(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def Wait(self) -> None:
        """"""
    @overload
    def Wait(self, cancellationToken: CancellationToken) -> None:
        """"""
    @overload
    def Wait(self, millisecondsTimeout: int) -> bool:
        """"""
    @overload
    def Wait(self, millisecondsTimeout: int, cancellationToken: CancellationToken) -> bool:
        """"""
    @overload
    def Wait(self, timeout: TimeSpan) -> bool:
        """"""
    @overload
    def Wait(self, timeout: TimeSpan, cancellationToken: CancellationToken) -> bool:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IntersectQueryOperator[TInputOutput](
    BinaryQueryOperator[TInputOutput, TInputOutput, TInputOutput],
    IEnumerable[TInputOutput],
    IEnumerable,
):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetEnumerator[TInputOutput](self) -> IEnumerator[TInputOutput]:
        """"""
    @overload
    def GetEnumerator[TInputOutput](
        self, mergeOptions: ParallelMergeOptions | None
    ) -> IEnumerator[TInputOutput]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def WrapPartitionedStream[TInputOutput, TLeftKey, TRightKey](
        self,
        leftPartitionedStream: PartitionedStream[TInputOutput, TLeftKey],
        rightPartitionedStream: PartitionedStream[TInputOutput, TRightKey],
        outputRecipient: IPartitionedStreamRecipient[TInputOutput],
        preferStriping: bool,
        settings: QuerySettings,
    ) -> None:
        """"""
    @overload
    def __iter__[TInputOutput](self) -> Iterator[TInputOutput]:
        """"""
    @overload
    def __iter__[TInputOutput](
        self, mergeOptions: ParallelMergeOptions | None
    ) -> Iterator[TInputOutput]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class JoinQueryOperator[TLeftInput, TRightInput, TKey, TOutput](
    BinaryQueryOperator[TLeftInput, TRightInput, TOutput], IEnumerable[TOutput], IEnumerable
):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetEnumerator[TOutput](self) -> IEnumerator[TOutput]:
        """"""
    @overload
    def GetEnumerator(self, mergeOptions: ParallelMergeOptions | None) -> IEnumerator[TOutput]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def WrapPartitionedStream[TLeftKey, TRightKey](
        self,
        leftStream: PartitionedStream[TLeftInput, TLeftKey],
        rightStream: PartitionedStream[TRightInput, TRightKey],
        outputRecipient: IPartitionedStreamRecipient[TOutput],
        preferStriping: bool,
        settings: QuerySettings,
    ) -> None:
        """"""
    @overload
    def __iter__[TOutput](self) -> Iterator[TOutput]:
        """"""
    @overload
    def __iter__(self, mergeOptions: ParallelMergeOptions | None) -> Iterator[TOutput]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class LastQueryOperator[TSource](
    UnaryQueryOperator[TSource, TSource], IEnumerable[TSource], IEnumerable
):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetEnumerator[TSource](self) -> IEnumerator[TSource]:
        """"""
    @overload
    def GetEnumerator[TSource](
        self, mergeOptions: ParallelMergeOptions | None
    ) -> IEnumerator[TSource]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __iter__[TSource](self) -> Iterator[TSource]:
        """"""
    @overload
    def __iter__[TSource](self, mergeOptions: ParallelMergeOptions | None) -> Iterator[TSource]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ListChunk[TInputOutput](Object, IEnumerable[TInputOutput], IEnumerable):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator[TInputOutput](self) -> IEnumerator[TInputOutput]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def __iter__[TInputOutput](self) -> Iterator[TInputOutput]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ListQueryResults[T](QueryResults[T], ICollection[T], IEnumerable[T], IList[T], IEnumerable):
    """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def Item(self) -> T:
        """"""
    @Item.setter
    def Item(self, value: T) -> None: ...
    def Add(self, item: T) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    def Contains(self, item: T) -> bool:
        """"""
    def CopyTo(self, array: Array[T], arrayIndex: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator[T](self) -> IEnumerator[T]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def IndexOf(self, item: T) -> int:
        """"""
    def Insert(self, index: int, item: T) -> None:
        """"""
    def Remove(self, item: T) -> bool:
        """"""
    def RemoveAt(self, index: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def __contains__(self, item: T) -> bool:
        """"""
    def __iter__[T](self) -> Iterator[T]:
        """"""
    def __delitem__(self, item: T) -> bool:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, index: int) -> T:
        """"""
    def __setitem__(self, index: int, value: T) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class LongAverageAggregationOperator(
    InlinedAggregationOperator[Int64, Pair[Int64, Int64], Double],
    IEnumerable[Pair[Int64, Int64]],
    IEnumerable,
):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetEnumerator(self) -> IEnumerator[Pair[int, int]]:
        """"""
    @overload
    def GetEnumerator(
        self, mergeOptions: ParallelMergeOptions | None
    ) -> IEnumerator[Pair[int, int]]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __iter__(self) -> Iterator[Pair[int, int]]:
        """"""
    @overload
    def __iter__(self, mergeOptions: ParallelMergeOptions | None) -> Iterator[Pair[int, int]]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class LongCountAggregationOperator[TSource](
    InlinedAggregationOperator[TSource, Int64, Int64], IEnumerable[Int64], IEnumerable
):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetEnumerator(self) -> IEnumerator[int]:
        """"""
    @overload
    def GetEnumerator(self, mergeOptions: ParallelMergeOptions | None) -> IEnumerator[int]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __iter__(self) -> Iterator[int]:
        """"""
    @overload
    def __iter__(self, mergeOptions: ParallelMergeOptions | None) -> Iterator[int]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class LongMinMaxAggregationOperator(
    InlinedAggregationOperator[Int64, Int64, Int64], IEnumerable[Int64], IEnumerable
):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetEnumerator(self) -> IEnumerator[int]:
        """"""
    @overload
    def GetEnumerator(self, mergeOptions: ParallelMergeOptions | None) -> IEnumerator[int]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __iter__(self) -> Iterator[int]:
        """"""
    @overload
    def __iter__(self, mergeOptions: ParallelMergeOptions | None) -> Iterator[int]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class LongSumAggregationOperator(
    InlinedAggregationOperator[Int64, Int64, Int64], IEnumerable[Int64], IEnumerable
):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetEnumerator(self) -> IEnumerator[int]:
        """"""
    @overload
    def GetEnumerator(self, mergeOptions: ParallelMergeOptions | None) -> IEnumerator[int]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __iter__(self) -> Iterator[int]:
        """"""
    @overload
    def __iter__(self, mergeOptions: ParallelMergeOptions | None) -> Iterator[int]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class Lookup[TKey, TElement](
    Object, IEnumerable[IGrouping[TKey, TElement]], IEnumerable, ILookup[TKey, TElement]
):
    """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def Item(self) -> IEnumerable[TElement]:
        """"""
    def Contains(self, key: TKey) -> bool:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator[TKey, TElement](self) -> IEnumerator[IGrouping[TKey, TElement]]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def __contains__(self, key: TKey) -> bool:
        """"""
    def __iter__[TKey, TElement](self) -> Iterator[IGrouping[TKey, TElement]]:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, key: TKey) -> IEnumerable[TElement]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class MergeEnumerator[TInputOutput](
    ABC, Object, IEnumerator[TInputOutput], IEnumerator, IDisposable
):
    """"""
    @property
    def Current(self) -> TInputOutput:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def MoveNext(self) -> bool:
        """"""
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class MergeExecutor[TInputOutput](Object, IEnumerable[TInputOutput], IEnumerable):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator[TInputOutput](self) -> IEnumerator[TInputOutput]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def __iter__[TInputOutput](self) -> Iterator[TInputOutput]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class NoKeyMemoizationRequired(ValueType):
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
class NullableDecimalAverageAggregationOperator(
    InlinedAggregationOperator[Decimal | None, Pair[Decimal, Int64], Decimal | None],
    IEnumerable[Pair[Decimal, Int64]],
    IEnumerable,
):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetEnumerator(self) -> IEnumerator[Pair[Decimal, int]]:
        """"""
    @overload
    def GetEnumerator(
        self, mergeOptions: ParallelMergeOptions | None
    ) -> IEnumerator[Pair[Decimal, int]]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __iter__(self) -> Iterator[Pair[Decimal, int]]:
        """"""
    @overload
    def __iter__(self, mergeOptions: ParallelMergeOptions | None) -> Iterator[Pair[Decimal, int]]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class NullableDecimalMinMaxAggregationOperator(
    InlinedAggregationOperator[Decimal | None, Decimal | None, Decimal | None],
    IEnumerable[Decimal | None],
    IEnumerable,
):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetEnumerator(self) -> IEnumerator[Decimal | None]:
        """"""
    @overload
    def GetEnumerator(
        self, mergeOptions: ParallelMergeOptions | None
    ) -> IEnumerator[Decimal | None]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __iter__(self) -> Iterator[Decimal | None]:
        """"""
    @overload
    def __iter__(self, mergeOptions: ParallelMergeOptions | None) -> Iterator[Decimal | None]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class NullableDecimalSumAggregationOperator(
    InlinedAggregationOperator[Decimal | None, Decimal | None, Decimal | None],
    IEnumerable[Decimal | None],
    IEnumerable,
):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetEnumerator(self) -> IEnumerator[Decimal | None]:
        """"""
    @overload
    def GetEnumerator(
        self, mergeOptions: ParallelMergeOptions | None
    ) -> IEnumerator[Decimal | None]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __iter__(self) -> Iterator[Decimal | None]:
        """"""
    @overload
    def __iter__(self, mergeOptions: ParallelMergeOptions | None) -> Iterator[Decimal | None]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class NullableDoubleAverageAggregationOperator(
    InlinedAggregationOperator[Double | None, Pair[Double, Int64], Double | None],
    IEnumerable[Pair[Double, Int64]],
    IEnumerable,
):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetEnumerator(self) -> IEnumerator[Pair[float, int]]:
        """"""
    @overload
    def GetEnumerator(
        self, mergeOptions: ParallelMergeOptions | None
    ) -> IEnumerator[Pair[float, int]]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __iter__(self) -> Iterator[Pair[float, int]]:
        """"""
    @overload
    def __iter__(self, mergeOptions: ParallelMergeOptions | None) -> Iterator[Pair[float, int]]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class NullableDoubleMinMaxAggregationOperator(
    InlinedAggregationOperator[Double | None, Double | None, Double | None],
    IEnumerable[Double | None],
    IEnumerable,
):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetEnumerator(self) -> IEnumerator[float | None]:
        """"""
    @overload
    def GetEnumerator(self, mergeOptions: ParallelMergeOptions | None) -> IEnumerator[float | None]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __iter__(self) -> Iterator[float | None]:
        """"""
    @overload
    def __iter__(self, mergeOptions: ParallelMergeOptions | None) -> Iterator[float | None]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class NullableDoubleSumAggregationOperator(
    InlinedAggregationOperator[Double | None, Double | None, Double | None],
    IEnumerable[Double | None],
    IEnumerable,
):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetEnumerator(self) -> IEnumerator[float | None]:
        """"""
    @overload
    def GetEnumerator(self, mergeOptions: ParallelMergeOptions | None) -> IEnumerator[float | None]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __iter__(self) -> Iterator[float | None]:
        """"""
    @overload
    def __iter__(self, mergeOptions: ParallelMergeOptions | None) -> Iterator[float | None]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class NullableFloatAverageAggregationOperator(
    InlinedAggregationOperator[Single | None, Pair[Double, Int64], Single | None],
    IEnumerable[Pair[Double, Int64]],
    IEnumerable,
):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetEnumerator(self) -> IEnumerator[Pair[float, int]]:
        """"""
    @overload
    def GetEnumerator(
        self, mergeOptions: ParallelMergeOptions | None
    ) -> IEnumerator[Pair[float, int]]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __iter__(self) -> Iterator[Pair[float, int]]:
        """"""
    @overload
    def __iter__(self, mergeOptions: ParallelMergeOptions | None) -> Iterator[Pair[float, int]]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class NullableFloatMinMaxAggregationOperator(
    InlinedAggregationOperator[Single | None, Single | None, Single | None],
    IEnumerable[Single | None],
    IEnumerable,
):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetEnumerator(self) -> IEnumerator[float | None]:
        """"""
    @overload
    def GetEnumerator(self, mergeOptions: ParallelMergeOptions | None) -> IEnumerator[float | None]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __iter__(self) -> Iterator[float | None]:
        """"""
    @overload
    def __iter__(self, mergeOptions: ParallelMergeOptions | None) -> Iterator[float | None]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class NullableFloatSumAggregationOperator(
    InlinedAggregationOperator[Single | None, Double | None, Single | None],
    IEnumerable[Double | None],
    IEnumerable,
):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetEnumerator(self) -> IEnumerator[float | None]:
        """"""
    @overload
    def GetEnumerator(self, mergeOptions: ParallelMergeOptions | None) -> IEnumerator[float | None]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __iter__(self) -> Iterator[float | None]:
        """"""
    @overload
    def __iter__(self, mergeOptions: ParallelMergeOptions | None) -> Iterator[float | None]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class NullableIntAverageAggregationOperator(
    InlinedAggregationOperator[Int32 | None, Pair[Int64, Int64], Double | None],
    IEnumerable[Pair[Int64, Int64]],
    IEnumerable,
):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetEnumerator(self) -> IEnumerator[Pair[int, int]]:
        """"""
    @overload
    def GetEnumerator(
        self, mergeOptions: ParallelMergeOptions | None
    ) -> IEnumerator[Pair[int, int]]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __iter__(self) -> Iterator[Pair[int, int]]:
        """"""
    @overload
    def __iter__(self, mergeOptions: ParallelMergeOptions | None) -> Iterator[Pair[int, int]]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class NullableIntMinMaxAggregationOperator(
    InlinedAggregationOperator[Int32 | None, Int32 | None, Int32 | None],
    IEnumerable[Int32 | None],
    IEnumerable,
):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetEnumerator(self) -> IEnumerator[int | None]:
        """"""
    @overload
    def GetEnumerator(self, mergeOptions: ParallelMergeOptions | None) -> IEnumerator[int | None]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __iter__(self) -> Iterator[int | None]:
        """"""
    @overload
    def __iter__(self, mergeOptions: ParallelMergeOptions | None) -> Iterator[int | None]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class NullableIntSumAggregationOperator(
    InlinedAggregationOperator[Int32 | None, Int32 | None, Int32 | None],
    IEnumerable[Int32 | None],
    IEnumerable,
):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetEnumerator(self) -> IEnumerator[int | None]:
        """"""
    @overload
    def GetEnumerator(self, mergeOptions: ParallelMergeOptions | None) -> IEnumerator[int | None]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __iter__(self) -> Iterator[int | None]:
        """"""
    @overload
    def __iter__(self, mergeOptions: ParallelMergeOptions | None) -> Iterator[int | None]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class NullableLongAverageAggregationOperator(
    InlinedAggregationOperator[Int64 | None, Pair[Int64, Int64], Double | None],
    IEnumerable[Pair[Int64, Int64]],
    IEnumerable,
):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetEnumerator(self) -> IEnumerator[Pair[int, int]]:
        """"""
    @overload
    def GetEnumerator(
        self, mergeOptions: ParallelMergeOptions | None
    ) -> IEnumerator[Pair[int, int]]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __iter__(self) -> Iterator[Pair[int, int]]:
        """"""
    @overload
    def __iter__(self, mergeOptions: ParallelMergeOptions | None) -> Iterator[Pair[int, int]]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class NullableLongMinMaxAggregationOperator(
    InlinedAggregationOperator[Int64 | None, Int64 | None, Int64 | None],
    IEnumerable[Int64 | None],
    IEnumerable,
):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetEnumerator(self) -> IEnumerator[int | None]:
        """"""
    @overload
    def GetEnumerator(self, mergeOptions: ParallelMergeOptions | None) -> IEnumerator[int | None]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __iter__(self) -> Iterator[int | None]:
        """"""
    @overload
    def __iter__(self, mergeOptions: ParallelMergeOptions | None) -> Iterator[int | None]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class NullableLongSumAggregationOperator(
    InlinedAggregationOperator[Int64 | None, Int64 | None, Int64 | None],
    IEnumerable[Int64 | None],
    IEnumerable,
):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetEnumerator(self) -> IEnumerator[int | None]:
        """"""
    @overload
    def GetEnumerator(self, mergeOptions: ParallelMergeOptions | None) -> IEnumerator[int | None]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __iter__(self) -> Iterator[int | None]:
        """"""
    @overload
    def __iter__(self, mergeOptions: ParallelMergeOptions | None) -> Iterator[int | None]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class OrderPreservingMergeHelper[TInputOutput, TKey](Object, IMergeHelper[TInputOutput]):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Execute(self) -> None:
        """"""
    def GetEnumerator(self) -> IEnumerator[TInputOutput]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetResultsAsArray(self) -> Array[TInputOutput]:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def __iter__(self) -> Iterator[TInputOutput]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class OrderPreservingPipeliningMergeHelper[TOutput, TKey](Object, IMergeHelper[TOutput]):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Execute(self) -> None:
        """"""
    def GetEnumerator[TOutput](self) -> IEnumerator[TOutput]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetResultsAsArray[TOutput](self) -> Array[TOutput]:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def __iter__[TOutput](self) -> Iterator[TOutput]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class OrderPreservingPipeliningSpoolingTask[TOutput, TKey](SpoolingTaskBase):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def Spool(
        cls,
        groupState: QueryTaskGroupState,
        partitions: PartitionedStream[TOutput, TKey],
        consumerWaiting: Array[bool],
        producerWaiting: Array[bool],
        producerDone: Array[bool],
        buffers: Array[Queue[Pair[TKey, TOutput]]],
        bufferLocks: Array[object],
        taskScheduler: TaskScheduler,
        autoBuffered: bool,
    ) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class OrderPreservingSpoolingTask[TInputOutput, TKey](SpoolingTaskBase):
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
class OrderedGroupByElementSelectorQueryOperatorEnumerator[TSource, TGroupKey, TElement, TOrderKey](
    OrderedGroupByQueryOperatorEnumerator[TSource, TGroupKey, TElement, TOrderKey]
):
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
class OrderedGroupByGrouping[TGroupKey, TOrderKey, TElement](
    Object, IEnumerable[TElement], IEnumerable, IGrouping[TGroupKey, TElement]
):
    """"""
    @property
    def Key(self) -> TGroupKey:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator[TElement](self) -> IEnumerator[TElement]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def __iter__[TElement](self) -> Iterator[TElement]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class OrderedGroupByIdentityQueryOperatorEnumerator[TSource, TGroupKey, TOrderKey](
    OrderedGroupByQueryOperatorEnumerator[TSource, TGroupKey, TSource, TOrderKey]
):
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
class OrderedGroupByQueryOperatorEnumerator[TSource, TGroupKey, TElement, TOrderKey](
    ABC, QueryOperatorEnumerator[IGrouping[TGroupKey, TElement], TOrderKey]
):
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
class OrderedHashRepartitionEnumerator[TInputOutput, THashKey, TOrderKey](
    QueryOperatorEnumerator[Pair[TInputOutput, THashKey], TOrderKey]
):
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
class OrderedHashRepartitionStream[TInputOutput, THashKey, TOrderKey](
    HashRepartitionStream[TInputOutput, THashKey, TOrderKey]
):
    """"""
    @property
    def PartitionCount(self) -> int:
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
class OrderingQueryOperator[TSource](QueryOperator[TSource], IEnumerable[TSource], IEnumerable):
    """"""
    def __init__(self, child: QueryOperator[TSource], orderOn: bool) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetEnumerator[TSource](self) -> IEnumerator[TSource]:
        """"""
    @overload
    def GetEnumerator[TSource](
        self, mergeOptions: ParallelMergeOptions | None
    ) -> IEnumerator[TSource]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __iter__[TSource](self) -> Iterator[TSource]:
        """"""
    @overload
    def __iter__[TSource](self, mergeOptions: ParallelMergeOptions | None) -> Iterator[TSource]:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class PairComparer[T, U](Object, IComparer[Pair[T, U]]):
    """"""
    def __init__(self, comparer1: IComparer[T], comparer2: IComparer[U]) -> None:
        """"""
    def Compare[U](self, x: Pair[T, U], y: Pair[T, U]) -> int:
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
class Pair[T, U](ValueType):
    """"""
    def __init__(self, first: T, second: U) -> None:
        """"""
    @property
    def First(self) -> T:
        """"""
    @First.setter
    def First(self, value: T) -> None: ...
    @property
    def Second(self) -> U:
        """"""
    @Second.setter
    def Second(self, value: U) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ParallelEnumerableWrapper(ParallelQuery[Object], IEnumerable[Object], IEnumerable):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator[object]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def __iter__(self) -> Iterator[object]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ParallelEnumerableWrapper[T](ParallelQuery[T], IEnumerable[T], IEnumerable):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator[T](self) -> IEnumerator[T]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def __iter__[T](self) -> Iterator[T]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class PartitionedDataSource[T](PartitionedStream[T, Int32]):
    """"""
    @property
    def PartitionCount(self) -> int:
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
class PartitionedStreamMerger[TOutput](Object, IPartitionedStreamRecipient[TOutput]):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Receive[TOutput, TKey](self, partitionedStream: PartitionedStream[TOutput, TKey]) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class PartitionedStream[TElement, TKey](Object):
    """"""
    @property
    def PartitionCount(self) -> int:
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
class PartitionerQueryOperator[TElement](
    QueryOperator[TElement], IEnumerable[TElement], IEnumerable
):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetEnumerator[TElement](self) -> IEnumerator[TElement]:
        """"""
    @overload
    def GetEnumerator[TElement](
        self, mergeOptions: ParallelMergeOptions | None
    ) -> IEnumerator[TElement]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __iter__[TElement](self) -> Iterator[TElement]:
        """"""
    @overload
    def __iter__[TElement](self, mergeOptions: ParallelMergeOptions | None) -> Iterator[TElement]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class PipelineSpoolingTask[TInputOutput, TIgnoreKey](SpoolingTaskBase):
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
class PlinqEtwProvider(EventSource, IDisposable):
    """"""
    @property
    def ConstructionException(self) -> Exception:
        """"""
    @property
    def Guid(self) -> Guid:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def Settings(self) -> EventSourceSettings:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetTrait(self, key: str) -> str:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IsEnabled(self) -> bool:
        """"""
    @overload
    def IsEnabled(self, level: EventLevel, keywords: EventKeywords) -> bool:
        """"""
    @overload
    def IsEnabled(self, level: EventLevel, keywords: EventKeywords, channel: EventChannel) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def Write(self, eventName: str) -> None:
        """"""
    @overload
    def Write[T](self, eventName: str, data: T) -> None:
        """"""
    @overload
    def Write(self, eventName: str, options: EventSourceOptions, data: T) -> None:
        """"""
    @overload
    def Write(
        self,
        eventName: str,
        options: EventSourceOptions,
        activityId: Guid,
        relatedActivityId: Guid,
        data: T,
    ) -> None:
        """"""
    @overload
    def Write(self, eventName: str, options: EventSourceOptions) -> None:
        """"""
    @overload
    def Write[T](self, eventName: str, options: EventSourceOptions, data: T) -> None:
        """"""
    EventCommandExecuted: EventType[EventHandler[EventCommandEventArgs]] = ...
    """"""
    # noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
    class Tasks(Object):
        """"""

        ForkJoin: ClassVar[EventTask]
        """"""
        Query: ClassVar[EventTask]
        """"""
        def __init__(self) -> None:
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
class ProducerComparerInt(Object, IComparer[Producer[Int32]]):
    """"""
    def __init__(self) -> None:
        """"""
    def Compare(self, x: Producer[int], y: Producer[int]) -> int:
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
class Producer[TKey](ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class QueryExecutionOption[TSource](QueryOperator[TSource], IEnumerable[TSource], IEnumerable):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetEnumerator[TSource](self) -> IEnumerator[TSource]:
        """"""
    @overload
    def GetEnumerator[TSource](
        self, mergeOptions: ParallelMergeOptions | None
    ) -> IEnumerator[TSource]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __iter__[TSource](self) -> Iterator[TSource]:
        """"""
    @overload
    def __iter__[TSource](self, mergeOptions: ParallelMergeOptions | None) -> Iterator[TSource]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class QueryLifecycle(ABC, Object):
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
class QueryOpeningEnumerator[TOutput](Object, IEnumerator[TOutput], IEnumerator, IDisposable):
    """"""
    @property
    def Current(self) -> TOutput:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def MoveNext(self) -> bool:
        """"""
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class QueryOperatorEnumerator[TElement, TKey](ABC, Object):
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
class QueryOperator[TOutput](ABC, ParallelQuery[TOutput], IEnumerable[TOutput], IEnumerable):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetEnumerator[TOutput](self) -> IEnumerator[TOutput]:
        """"""
    @overload
    def GetEnumerator(self, mergeOptions: ParallelMergeOptions | None) -> IEnumerator[TOutput]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __iter__[TOutput](self) -> Iterator[TOutput]:
        """"""
    @overload
    def __iter__(self, mergeOptions: ParallelMergeOptions | None) -> Iterator[TOutput]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class QueryResults[T](ABC, Object, ICollection[T], IEnumerable[T], IList[T], IEnumerable):
    """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def Item(self) -> T:
        """"""
    @Item.setter
    def Item(self, value: T) -> None: ...
    def Add(self, item: T) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    def Contains(self, item: T) -> bool:
        """"""
    def CopyTo(self, array: Array[T], arrayIndex: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator[T](self) -> IEnumerator[T]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def IndexOf(self, item: T) -> int:
        """"""
    def Insert(self, index: int, item: T) -> None:
        """"""
    def Remove(self, item: T) -> bool:
        """"""
    def RemoveAt(self, index: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def __contains__(self, item: T) -> bool:
        """"""
    def __iter__[T](self) -> Iterator[T]:
        """"""
    def __delitem__(self, item: T) -> bool:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, index: int) -> T:
        """"""
    def __setitem__(self, index: int, value: T) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class QuerySettings(ValueType):
    """"""
    def CleanStateAtQueryEnd(self) -> None:
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
class QueryTask(ABC, Object):
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
class QueryTaskGroupState(Object):
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
class RangeEnumerable(
    ParallelQuery[Int32], IEnumerable[Int32], IEnumerable, IParallelPartitionable[Int32]
):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator[int]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetPartitions(self, partitionCount: int) -> Array[QueryOperatorEnumerator[int, int]]:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def __iter__(self) -> Iterator[int]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class RepeatEnumerable[TResult](
    ParallelQuery[TResult], IEnumerable[TResult], IEnumerable, IParallelPartitionable[TResult]
):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator[TResult](self) -> IEnumerator[TResult]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetPartitions[TResult](
        self, partitionCount: int
    ) -> Array[QueryOperatorEnumerator[TResult, int]]:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def __iter__[TResult](self) -> Iterator[TResult]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ReverseComparer[T](Object, IComparer[T]):
    """"""
    def Compare(self, x: T, y: T) -> int:
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
class ReverseQueryOperator[TSource](
    UnaryQueryOperator[TSource, TSource], IEnumerable[TSource], IEnumerable
):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetEnumerator[TSource](self) -> IEnumerator[TSource]:
        """"""
    @overload
    def GetEnumerator[TSource](
        self, mergeOptions: ParallelMergeOptions | None
    ) -> IEnumerator[TSource]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __iter__[TSource](self) -> Iterator[TSource]:
        """"""
    @overload
    def __iter__[TSource](self, mergeOptions: ParallelMergeOptions | None) -> Iterator[TSource]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ScanQueryOperator[TElement](QueryOperator[TElement], IEnumerable[TElement], IEnumerable):
    """"""
    @property
    def Data(self) -> IEnumerable[TElement]:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetEnumerator[TElement](self) -> IEnumerator[TElement]:
        """"""
    @overload
    def GetEnumerator[TElement](
        self, mergeOptions: ParallelMergeOptions | None
    ) -> IEnumerator[TElement]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __iter__[TElement](self) -> Iterator[TElement]:
        """"""
    @overload
    def __iter__[TElement](self, mergeOptions: ParallelMergeOptions | None) -> Iterator[TElement]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class Scheduling(ABC, Object):
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
class SelectManyQueryOperator[TLeftInput, TRightInput, TOutput](
    UnaryQueryOperator[TLeftInput, TOutput], IEnumerable[TOutput], IEnumerable
):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetEnumerator[TOutput](self) -> IEnumerator[TOutput]:
        """"""
    @overload
    def GetEnumerator(self, mergeOptions: ParallelMergeOptions | None) -> IEnumerator[TOutput]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __iter__[TOutput](self) -> Iterator[TOutput]:
        """"""
    @overload
    def __iter__(self, mergeOptions: ParallelMergeOptions | None) -> Iterator[TOutput]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SelectQueryOperator[TInput, TOutput](
    UnaryQueryOperator[TInput, TOutput], IEnumerable[TOutput], IEnumerable
):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetEnumerator[TOutput](self) -> IEnumerator[TOutput]:
        """"""
    @overload
    def GetEnumerator(self, mergeOptions: ParallelMergeOptions | None) -> IEnumerator[TOutput]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __iter__[TOutput](self) -> Iterator[TOutput]:
        """"""
    @overload
    def __iter__(self, mergeOptions: ParallelMergeOptions | None) -> Iterator[TOutput]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class Shared[T](Object):
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
class SingleQueryOperator[TSource](
    UnaryQueryOperator[TSource, TSource], IEnumerable[TSource], IEnumerable
):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetEnumerator[TSource](self) -> IEnumerator[TSource]:
        """"""
    @overload
    def GetEnumerator[TSource](
        self, mergeOptions: ParallelMergeOptions | None
    ) -> IEnumerator[TSource]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __iter__[TSource](self) -> Iterator[TSource]:
        """"""
    @overload
    def __iter__[TSource](self, mergeOptions: ParallelMergeOptions | None) -> Iterator[TSource]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SortHelper[TInputOutput, TKey](SortHelper[TInputOutput], IDisposable):
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
class SortHelper[TInputOutput](ABC, Object):
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
class SortQueryOperatorEnumerator[TInputOutput, TKey, TSortKey](
    QueryOperatorEnumerator[TInputOutput, TSortKey]
):
    """"""
    @property
    def KeyComparer(self) -> IComparer[TSortKey]:
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
class SortQueryOperatorResults[TInputOutput, TSortKey](
    QueryResults[TInputOutput],
    ICollection[TInputOutput],
    IEnumerable[TInputOutput],
    IList[TInputOutput],
    IEnumerable,
):
    """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def Item(self) -> TInputOutput:
        """"""
    @Item.setter
    def Item(self, value: TInputOutput) -> None: ...
    def Add[TInputOutput](self, item: TInputOutput) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    def Contains[TInputOutput](self, item: TInputOutput) -> bool:
        """"""
    def CopyTo[TInputOutput](self, array: Array[TInputOutput], arrayIndex: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator[TInputOutput](self) -> IEnumerator[TInputOutput]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def IndexOf[TInputOutput](self, item: TInputOutput) -> int:
        """"""
    def Insert[TInputOutput](self, index: int, item: TInputOutput) -> None:
        """"""
    def Remove[TInputOutput](self, item: TInputOutput) -> bool:
        """"""
    def RemoveAt(self, index: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def __contains__[TInputOutput](self, item: TInputOutput) -> bool:
        """"""
    def __iter__[TInputOutput](self) -> Iterator[TInputOutput]:
        """"""
    def __delitem__[TInputOutput](self, item: TInputOutput) -> bool:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__[TInputOutput](self, index: int) -> TInputOutput:
        """"""
    def __setitem__[TInputOutput](self, index: int, value: TInputOutput) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SortQueryOperator[TInputOutput, TSortKey](
    UnaryQueryOperator[TInputOutput, TInputOutput],
    IEnumerable[TInputOutput],
    IEnumerable,
    IOrderedEnumerable[TInputOutput],
):
    """"""
    def CreateOrderedEnumerable[TInputOutput, TKey](
        self, keySelector: Func[TInputOutput, TKey], comparer: IComparer[TKey], descending: bool
    ) -> IOrderedEnumerable[TInputOutput]:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetEnumerator[TInputOutput](self) -> IEnumerator[TInputOutput]:
        """"""
    @overload
    def GetEnumerator[TInputOutput](
        self, mergeOptions: ParallelMergeOptions | None
    ) -> IEnumerator[TInputOutput]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __iter__[TInputOutput](self) -> Iterator[TInputOutput]:
        """"""
    @overload
    def __iter__[TInputOutput](
        self, mergeOptions: ParallelMergeOptions | None
    ) -> Iterator[TInputOutput]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SpoolingTask(ABC, Object):
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
class SpoolingTaskBase(ABC, QueryTask):
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
class StopAndGoSpoolingTask[TInputOutput, TIgnoreKey](SpoolingTaskBase):
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
class SynchronousChannelMergeEnumerator[T](
    MergeEnumerator[T], IEnumerator[T], IEnumerator, IDisposable
):
    """"""
    @property
    def Current(self) -> T:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def MoveNext(self) -> bool:
        """"""
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SynchronousChannel[T](Object):
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
class TakeOrSkipQueryOperator[TResult](
    UnaryQueryOperator[TResult, TResult], IEnumerable[TResult], IEnumerable
):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetEnumerator[TResult](self) -> IEnumerator[TResult]:
        """"""
    @overload
    def GetEnumerator[TResult](
        self, mergeOptions: ParallelMergeOptions | None
    ) -> IEnumerator[TResult]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __iter__[TResult](self) -> Iterator[TResult]:
        """"""
    @overload
    def __iter__[TResult](self, mergeOptions: ParallelMergeOptions | None) -> Iterator[TResult]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class TakeOrSkipWhileQueryOperator[TResult](
    UnaryQueryOperator[TResult, TResult], IEnumerable[TResult], IEnumerable
):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetEnumerator[TResult](self) -> IEnumerator[TResult]:
        """"""
    @overload
    def GetEnumerator[TResult](
        self, mergeOptions: ParallelMergeOptions | None
    ) -> IEnumerator[TResult]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __iter__[TResult](self) -> Iterator[TResult]:
        """"""
    @overload
    def __iter__[TResult](self, mergeOptions: ParallelMergeOptions | None) -> Iterator[TResult]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class TraceHelpers(ABC, Object):
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
class UnaryQueryOperator[TInput, TOutput](
    ABC, QueryOperator[TOutput], IEnumerable[TOutput], IEnumerable
):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetEnumerator[TOutput](self) -> IEnumerator[TOutput]:
        """"""
    @overload
    def GetEnumerator(self, mergeOptions: ParallelMergeOptions | None) -> IEnumerator[TOutput]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __iter__[TOutput](self) -> Iterator[TOutput]:
        """"""
    @overload
    def __iter__(self, mergeOptions: ParallelMergeOptions | None) -> Iterator[TOutput]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class UnionQueryOperator[TInputOutput](
    BinaryQueryOperator[TInputOutput, TInputOutput, TInputOutput],
    IEnumerable[TInputOutput],
    IEnumerable,
):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetEnumerator[TInputOutput](self) -> IEnumerator[TInputOutput]:
        """"""
    @overload
    def GetEnumerator[TInputOutput](
        self, mergeOptions: ParallelMergeOptions | None
    ) -> IEnumerator[TInputOutput]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def WrapPartitionedStream[TInputOutput, TLeftKey, TRightKey](
        self,
        leftStream: PartitionedStream[TInputOutput, TLeftKey],
        rightStream: PartitionedStream[TInputOutput, TRightKey],
        outputRecipient: IPartitionedStreamRecipient[TInputOutput],
        preferStriping: bool,
        settings: QuerySettings,
    ) -> None:
        """"""
    @overload
    def __iter__[TInputOutput](self) -> Iterator[TInputOutput]:
        """"""
    @overload
    def __iter__[TInputOutput](
        self, mergeOptions: ParallelMergeOptions | None
    ) -> Iterator[TInputOutput]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class UnorderedHashRepartitionStream[TInputOutput, THashKey, TIgnoreKey](
    HashRepartitionStream[TInputOutput, THashKey, Int32]
):
    """"""
    @property
    def PartitionCount(self) -> int:
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
class Util(ABC, Object):
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
class WhereQueryOperator[TInputOutput](
    UnaryQueryOperator[TInputOutput, TInputOutput], IEnumerable[TInputOutput], IEnumerable
):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetEnumerator[TInputOutput](self) -> IEnumerator[TInputOutput]:
        """"""
    @overload
    def GetEnumerator[TInputOutput](
        self, mergeOptions: ParallelMergeOptions | None
    ) -> IEnumerator[TInputOutput]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __iter__[TInputOutput](self) -> Iterator[TInputOutput]:
        """"""
    @overload
    def __iter__[TInputOutput](
        self, mergeOptions: ParallelMergeOptions | None
    ) -> Iterator[TInputOutput]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class WrapperEqualityComparer[T](ValueType, IEqualityComparer[Wrapper[T]]):
    """"""
    @overload
    def Equals(self, x: Wrapper[T], y: Wrapper[T]) -> bool:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetHashCode(self, x: Wrapper[T]) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class Wrapper[T](ValueType):
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
class ZipQueryOperator[TLeftInput, TRightInput, TOutput](
    QueryOperator[TOutput], IEnumerable[TOutput], IEnumerable
):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetEnumerator[TOutput](self) -> IEnumerator[TOutput]:
        """"""
    @overload
    def GetEnumerator(self, mergeOptions: ParallelMergeOptions | None) -> IEnumerator[TOutput]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __iter__[TOutput](self) -> Iterator[TOutput]:
        """"""
    @overload
    def __iter__(self, mergeOptions: ParallelMergeOptions | None) -> Iterator[TOutput]:
        """"""
