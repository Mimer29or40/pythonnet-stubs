from __future__ import annotations

from abc import ABC
from typing import Generic
from typing import List
from typing import Optional
from typing import Protocol
from typing import TypeVar
from typing import Union
from typing import overload

from System import Array
from System import Boolean
from System import Byte
from System import Decimal
from System import Double
from System import Enum
from System import IDisposable
from System import Int32
from System import Int64
from System import Nullable
from System import Object
from System import Single
from System import ValueType
from System import Void
from System.Collections import IEnumerable
from System.Collections import IEnumerator
from System.Collections.Generic import ICollection
from System.Collections.Generic import IComparer
from System.Collections.Generic import IEnumerable
from System.Collections.Generic import IEnumerator
from System.Collections.Generic import IEqualityComparer
from System.Collections.Generic import IList
from System.Collections.Generic import Queue
from System.Diagnostics.Tracing import EventSource
from System.Diagnostics.Tracing import EventTask
from System.Linq import IGrouping
from System.Linq import ILookup
from System.Linq import IOrderedEnumerable
from System.Linq import ParallelMergeOptions
from System.Linq import ParallelQuery
from System.Threading import ManualResetEventSlim
from System.Threading.Tasks import TaskScheduler

# ---------- Types ---------- #

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

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
ByteType = Union[int, Byte]
DecimalType = Union[float, Decimal]
DoubleType = Union[float, Double]
FloatType = Union[float, Single]
IntType = Union[int, Int32]
LongType = Union[int, Int64]
NullableType = Union[Optional, Nullable]
ObjectType = Object
VoidType = Union[None, Void]

# ---------- Classes ---------- #

class AnyAllSearchOperator(
    Generic[TInput], UnaryQueryOperator[TInput, BooleanType], IEnumerable, IEnumerable[BooleanType]
):
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

class ArrayMergeHelper(Generic[TInputOutput], ObjectType, IMergeHelper[TInputOutput]):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, settings: QuerySettings, queryResults: QueryResults[TInputOutput]): ...

    # No Properties

    # ---------- Methods ---------- #

    def Execute(self) -> VoidType: ...
    def GetEnumerator(self) -> IEnumerator[TInputOutput]: ...
    def GetResultsAsArray(self) -> ArrayType[TInputOutput]: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class AssociativeAggregationOperator(
    Generic[TInput, TIntermediate, TOutput],
    UnaryQueryOperator[TInput, TIntermediate],
    IEnumerable,
    IEnumerable[TIntermediate],
):
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

class AsynchronousChannel(Generic[T], ObjectType, IDisposable):
    # No Fields

    # No Constructors

    # No Properties

    # ---------- Methods ---------- #

    def Dispose(self) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class AsynchronousChannelMergeEnumerator(
    Generic[T], MergeEnumerator[T], IEnumerator[T], IDisposable, IEnumerator
):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def Current(self) -> T: ...

    # ---------- Methods ---------- #

    def Dispose(self) -> VoidType: ...
    def MoveNext(self) -> BooleanType: ...
    def get_Current(self) -> T: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class BinaryQueryOperator(
    Protocol[TLeftInput, TRightInput, TOutput],
    QueryOperator[TOutput],
    IEnumerable,
    IEnumerable[TOutput],
):
    # No Fields

    # No Constructors

    # No Properties

    # ---------- Methods ---------- #

    def WrapPartitionedStream(
        self,
        leftPartitionedStream: PartitionedStream[TLeftInput, TLeftKey],
        rightPartitionedStream: PartitionedStream[TRightInput, TRightKey],
        outputRecipient: IPartitionedStreamRecipient[TOutput],
        preferStriping: BooleanType,
        settings: QuerySettings,
    ) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class CancellableEnumerable(ABC, ObjectType):
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

class CancellationState(ObjectType):
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

class ConcatQueryOperator(
    Generic[TSource],
    BinaryQueryOperator[TSource, TSource, TSource],
    IEnumerable,
    IEnumerable[TSource],
):
    # No Fields

    # No Constructors

    # No Properties

    # ---------- Methods ---------- #

    def WrapPartitionedStream(
        self,
        leftStream: PartitionedStream[TSource, TLeftKey],
        rightStream: PartitionedStream[TSource, TRightKey],
        outputRecipient: IPartitionedStreamRecipient[TSource],
        preferStriping: BooleanType,
        settings: QuerySettings,
    ) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ContainsSearchOperator(
    Generic[TInput], UnaryQueryOperator[TInput, BooleanType], IEnumerable, IEnumerable[BooleanType]
):
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

class CountAggregationOperator(
    Generic[TSource],
    InlinedAggregationOperator[TSource, IntType, IntType],
    IEnumerable,
    IEnumerable[IntType],
):
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

class DecimalAverageAggregationOperator(
    InlinedAggregationOperator[DecimalType, Pair[DecimalType, LongType], DecimalType],
    IEnumerable,
    IEnumerable[Pair[DecimalType, LongType]],
):
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

class DecimalMinMaxAggregationOperator(
    InlinedAggregationOperator[DecimalType, DecimalType, DecimalType],
    IEnumerable,
    IEnumerable[DecimalType],
):
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

class DecimalSumAggregationOperator(
    InlinedAggregationOperator[DecimalType, DecimalType, DecimalType],
    IEnumerable,
    IEnumerable[DecimalType],
):
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

class DefaultIfEmptyQueryOperator(
    Generic[TSource], UnaryQueryOperator[TSource, TSource], IEnumerable, IEnumerable[TSource]
):
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

class DefaultMergeHelper(Generic[TInputOutput, TIgnoreKey], ObjectType, IMergeHelper[TInputOutput]):
    # No Fields

    # No Constructors

    # No Properties

    # ---------- Methods ---------- #

    def GetResultsAsArray(self) -> ArrayType[TInputOutput]: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class DistinctQueryOperator(
    Generic[TInputOutput],
    UnaryQueryOperator[TInputOutput, TInputOutput],
    IEnumerable,
    IEnumerable[TInputOutput],
):
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

class DoubleAverageAggregationOperator(
    InlinedAggregationOperator[DoubleType, Pair[DoubleType, LongType], DoubleType],
    IEnumerable,
    IEnumerable[Pair[DoubleType, LongType]],
):
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

class DoubleMinMaxAggregationOperator(
    InlinedAggregationOperator[DoubleType, DoubleType, DoubleType],
    IEnumerable,
    IEnumerable[DoubleType],
):
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

class DoubleSumAggregationOperator(
    InlinedAggregationOperator[DoubleType, DoubleType, DoubleType],
    IEnumerable,
    IEnumerable[DoubleType],
):
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

class ElementAtQueryOperator(
    Generic[TSource], UnaryQueryOperator[TSource, TSource], IEnumerable, IEnumerable[TSource]
):
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

class EmptyEnumerable(Generic[T], ParallelQuery[T], IEnumerable, IEnumerable[T]):
    # No Fields

    # No Constructors

    # No Properties

    # ---------- Methods ---------- #

    def GetEnumerator(self) -> IEnumerator[T]: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class EmptyEnumerator(
    Generic[T], QueryOperatorEnumerator[T, IntType], IEnumerator[T], IDisposable, IEnumerator
):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # ---------- Properties ---------- #

    @property
    def Current(self) -> T: ...

    # ---------- Methods ---------- #

    def MoveNext(self) -> BooleanType: ...
    def get_Current(self) -> T: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class EnumerableWrapperWeakToStrong(ObjectType, IEnumerable[ObjectType], IEnumerable):
    # No Fields

    # No Constructors

    # No Properties

    # ---------- Methods ---------- #

    def GetEnumerator(self) -> IEnumerator[ObjectType]: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ExceptQueryOperator(
    Generic[TInputOutput],
    BinaryQueryOperator[TInputOutput, TInputOutput, TInputOutput],
    IEnumerable,
    IEnumerable[TInputOutput],
):
    # No Fields

    # No Constructors

    # No Properties

    # ---------- Methods ---------- #

    def WrapPartitionedStream(
        self,
        leftStream: PartitionedStream[TInputOutput, TLeftKey],
        rightStream: PartitionedStream[TInputOutput, TRightKey],
        outputRecipient: IPartitionedStreamRecipient[TInputOutput],
        preferStriping: BooleanType,
        settings: QuerySettings,
    ) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ExceptionAggregator(ABC, ObjectType):
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

class ExchangeUtilities(ABC, ObjectType):
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

class FirstQueryOperator(
    Generic[TSource], UnaryQueryOperator[TSource, TSource], IEnumerable, IEnumerable[TSource]
):
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

class FixedMaxHeap(Generic[TElement], ObjectType):
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

class FloatAverageAggregationOperator(
    InlinedAggregationOperator[FloatType, Pair[DoubleType, LongType], FloatType],
    IEnumerable,
    IEnumerable[Pair[DoubleType, LongType]],
):
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

class FloatMinMaxAggregationOperator(
    InlinedAggregationOperator[FloatType, FloatType, FloatType], IEnumerable, IEnumerable[FloatType]
):
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

class FloatSumAggregationOperator(
    InlinedAggregationOperator[FloatType, DoubleType, FloatType],
    IEnumerable,
    IEnumerable[DoubleType],
):
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

class ForAllOperator(
    Generic[TInput], UnaryQueryOperator[TInput, TInput], IEnumerable, IEnumerable[TInput]
):
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

class ForAllSpoolingTask(Generic[TInputOutput, TIgnoreKey], SpoolingTaskBase):
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

class GroupByElementSelectorQueryOperatorEnumerator(
    Generic[TSource, TGroupKey, TElement, TOrderKey],
    GroupByQueryOperatorEnumerator[TSource, TGroupKey, TElement, TOrderKey],
):
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

class GroupByGrouping(
    Generic[TGroupKey, TElement],
    ObjectType,
    IGrouping[TGroupKey, TElement],
    IEnumerable[TElement],
    IEnumerable,
):
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

class GroupByIdentityQueryOperatorEnumerator(
    Generic[TSource, TGroupKey, TOrderKey],
    GroupByQueryOperatorEnumerator[TSource, TGroupKey, TSource, TOrderKey],
):
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

class GroupByQueryOperator(
    Generic[TSource, TGroupKey, TElement],
    UnaryQueryOperator[TSource, IGrouping[TGroupKey, TElement]],
    IEnumerable,
    IEnumerable[IGrouping[TGroupKey, TElement]],
):
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

class GroupByQueryOperatorEnumerator(
    Protocol[TSource, TGroupKey, TElement, TOrderKey],
    QueryOperatorEnumerator[IGrouping[TGroupKey, TElement], TOrderKey],
):
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

class GroupJoinQueryOperator(
    Generic[TLeftInput, TRightInput, TKey, TOutput],
    BinaryQueryOperator[TLeftInput, TRightInput, TOutput],
    IEnumerable,
    IEnumerable[TOutput],
):
    # No Fields

    # No Constructors

    # No Properties

    # ---------- Methods ---------- #

    def WrapPartitionedStream(
        self,
        leftStream: PartitionedStream[TLeftInput, TLeftKey],
        rightStream: PartitionedStream[TRightInput, TRightKey],
        outputRecipient: IPartitionedStreamRecipient[TOutput],
        preferStriping: BooleanType,
        settings: QuerySettings,
    ) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class GrowingArray(Generic[T], ObjectType):
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

class HashJoinQueryOperatorEnumerator(
    Generic[TLeftInput, TLeftKey, TRightInput, THashKey, TOutput],
    QueryOperatorEnumerator[TOutput, TLeftKey],
):
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

class HashLookup(Generic[TKey, TValue], ObjectType):
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

class HashRepartitionEnumerator(
    Generic[TInputOutput, THashKey, TIgnoreKey],
    QueryOperatorEnumerator[Pair[TInputOutput, THashKey], IntType],
):
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

class HashRepartitionStream(
    Protocol[TInputOutput, THashKey, TOrderKey],
    PartitionedStream[Pair[TInputOutput, THashKey], TOrderKey],
):
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

class IndexedSelectQueryOperator(
    Generic[TInput, TOutput], UnaryQueryOperator[TInput, TOutput], IEnumerable, IEnumerable[TOutput]
):
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

class IndexedWhereQueryOperator(
    Generic[TInputOutput],
    UnaryQueryOperator[TInputOutput, TInputOutput],
    IEnumerable,
    IEnumerable[TInputOutput],
):
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

class InlinedAggregationOperator(
    Protocol[TSource, TIntermediate, TResult],
    UnaryQueryOperator[TSource, TIntermediate],
    IEnumerable,
    IEnumerable[TIntermediate],
):
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

class InlinedAggregationOperatorEnumerator(
    Protocol[TIntermediate], QueryOperatorEnumerator[TIntermediate, IntType]
):
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

class IntAverageAggregationOperator(
    InlinedAggregationOperator[IntType, Pair[LongType, LongType], DoubleType],
    IEnumerable,
    IEnumerable[Pair[LongType, LongType]],
):
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

class IntMinMaxAggregationOperator(
    InlinedAggregationOperator[IntType, IntType, IntType], IEnumerable, IEnumerable[IntType]
):
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

class IntSumAggregationOperator(
    InlinedAggregationOperator[IntType, IntType, IntType], IEnumerable, IEnumerable[IntType]
):
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

class IntValueEvent(ManualResetEventSlim, IDisposable):
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

class IntersectQueryOperator(
    Generic[TInputOutput],
    BinaryQueryOperator[TInputOutput, TInputOutput, TInputOutput],
    IEnumerable,
    IEnumerable[TInputOutput],
):
    # No Fields

    # No Constructors

    # No Properties

    # ---------- Methods ---------- #

    def WrapPartitionedStream(
        self,
        leftPartitionedStream: PartitionedStream[TInputOutput, TLeftKey],
        rightPartitionedStream: PartitionedStream[TInputOutput, TRightKey],
        outputRecipient: IPartitionedStreamRecipient[TInputOutput],
        preferStriping: BooleanType,
        settings: QuerySettings,
    ) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class JoinQueryOperator(
    Generic[TLeftInput, TRightInput, TKey, TOutput],
    BinaryQueryOperator[TLeftInput, TRightInput, TOutput],
    IEnumerable,
    IEnumerable[TOutput],
):
    # No Fields

    # No Constructors

    # No Properties

    # ---------- Methods ---------- #

    def WrapPartitionedStream(
        self,
        leftStream: PartitionedStream[TLeftInput, TLeftKey],
        rightStream: PartitionedStream[TRightInput, TRightKey],
        outputRecipient: IPartitionedStreamRecipient[TOutput],
        preferStriping: BooleanType,
        settings: QuerySettings,
    ) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class LastQueryOperator(
    Generic[TSource], UnaryQueryOperator[TSource, TSource], IEnumerable, IEnumerable[TSource]
):
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

class ListChunk(Generic[TInputOutput], ObjectType, IEnumerable[TInputOutput], IEnumerable):
    # No Fields

    # No Constructors

    # No Properties

    # ---------- Methods ---------- #

    def GetEnumerator(self) -> IEnumerator[TInputOutput]: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ListQueryResults(
    Generic[T], QueryResults[T], IList[T], ICollection[T], IEnumerable[T], IEnumerable
):
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

class LongAverageAggregationOperator(
    InlinedAggregationOperator[LongType, Pair[LongType, LongType], DoubleType],
    IEnumerable,
    IEnumerable[Pair[LongType, LongType]],
):
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

class LongCountAggregationOperator(
    Generic[TSource],
    InlinedAggregationOperator[TSource, LongType, LongType],
    IEnumerable,
    IEnumerable[LongType],
):
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

class LongMinMaxAggregationOperator(
    InlinedAggregationOperator[LongType, LongType, LongType], IEnumerable, IEnumerable[LongType]
):
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

class LongSumAggregationOperator(
    InlinedAggregationOperator[LongType, LongType, LongType], IEnumerable, IEnumerable[LongType]
):
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

class Lookup(
    Generic[TKey, TElement],
    ObjectType,
    ILookup[TKey, TElement],
    IEnumerable[IGrouping[TKey, TElement]],
    IEnumerable,
):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def Count(self) -> IntType: ...
    def __getitem__(self, key: TKey) -> IEnumerable[TElement]: ...

    # ---------- Methods ---------- #

    def Contains(self, key: TKey) -> BooleanType: ...
    def GetEnumerator(self) -> IEnumerator[IGrouping[TKey, TElement]]: ...
    def get_Count(self) -> IntType: ...
    def get_Item(self, key: TKey) -> IEnumerable[TElement]: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class MergeEnumerator(
    Protocol[TInputOutput], ObjectType, IEnumerator[TInputOutput], IDisposable, IEnumerator
):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def Current(self) -> TInputOutput: ...

    # ---------- Methods ---------- #

    def Dispose(self) -> VoidType: ...
    def MoveNext(self) -> BooleanType: ...
    def Reset(self) -> VoidType: ...
    def get_Current(self) -> TInputOutput: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class MergeExecutor(Generic[TInputOutput], ObjectType, IEnumerable[TInputOutput], IEnumerable):
    # No Fields

    # No Constructors

    # No Properties

    # ---------- Methods ---------- #

    def GetEnumerator(self) -> IEnumerator[TInputOutput]: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class NullableDecimalAverageAggregationOperator(
    InlinedAggregationOperator[
        NullableType[Nullable[DecimalType]],
        Pair[DecimalType, LongType],
        NullableType[Nullable[DecimalType]],
    ],
    IEnumerable,
    IEnumerable[Pair[DecimalType, LongType]],
):
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

class NullableDecimalMinMaxAggregationOperator(
    InlinedAggregationOperator[
        NullableType[Nullable[DecimalType]],
        NullableType[Nullable[DecimalType]],
        NullableType[Nullable[DecimalType]],
    ],
    IEnumerable,
    IEnumerable[NullableType[Nullable[DecimalType]]],
):
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

class NullableDecimalSumAggregationOperator(
    InlinedAggregationOperator[
        NullableType[Nullable[DecimalType]],
        NullableType[Nullable[DecimalType]],
        NullableType[Nullable[DecimalType]],
    ],
    IEnumerable,
    IEnumerable[NullableType[Nullable[DecimalType]]],
):
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

class NullableDoubleAverageAggregationOperator(
    InlinedAggregationOperator[
        NullableType[Nullable[DoubleType]],
        Pair[DoubleType, LongType],
        NullableType[Nullable[DoubleType]],
    ],
    IEnumerable,
    IEnumerable[Pair[DoubleType, LongType]],
):
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

class NullableDoubleMinMaxAggregationOperator(
    InlinedAggregationOperator[
        NullableType[Nullable[DoubleType]],
        NullableType[Nullable[DoubleType]],
        NullableType[Nullable[DoubleType]],
    ],
    IEnumerable,
    IEnumerable[NullableType[Nullable[DoubleType]]],
):
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

class NullableDoubleSumAggregationOperator(
    InlinedAggregationOperator[
        NullableType[Nullable[DoubleType]],
        NullableType[Nullable[DoubleType]],
        NullableType[Nullable[DoubleType]],
    ],
    IEnumerable,
    IEnumerable[NullableType[Nullable[DoubleType]]],
):
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

class NullableFloatAverageAggregationOperator(
    InlinedAggregationOperator[
        NullableType[Nullable[FloatType]],
        Pair[DoubleType, LongType],
        NullableType[Nullable[FloatType]],
    ],
    IEnumerable,
    IEnumerable[Pair[DoubleType, LongType]],
):
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

class NullableFloatMinMaxAggregationOperator(
    InlinedAggregationOperator[
        NullableType[Nullable[FloatType]],
        NullableType[Nullable[FloatType]],
        NullableType[Nullable[FloatType]],
    ],
    IEnumerable,
    IEnumerable[NullableType[Nullable[FloatType]]],
):
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

class NullableFloatSumAggregationOperator(
    InlinedAggregationOperator[
        NullableType[Nullable[FloatType]],
        NullableType[Nullable[DoubleType]],
        NullableType[Nullable[FloatType]],
    ],
    IEnumerable,
    IEnumerable[NullableType[Nullable[DoubleType]]],
):
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

class NullableIntAverageAggregationOperator(
    InlinedAggregationOperator[
        NullableType[Nullable[IntType]],
        Pair[LongType, LongType],
        NullableType[Nullable[DoubleType]],
    ],
    IEnumerable,
    IEnumerable[Pair[LongType, LongType]],
):
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

class NullableIntMinMaxAggregationOperator(
    InlinedAggregationOperator[
        NullableType[Nullable[IntType]],
        NullableType[Nullable[IntType]],
        NullableType[Nullable[IntType]],
    ],
    IEnumerable,
    IEnumerable[NullableType[Nullable[IntType]]],
):
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

class NullableIntSumAggregationOperator(
    InlinedAggregationOperator[
        NullableType[Nullable[IntType]],
        NullableType[Nullable[IntType]],
        NullableType[Nullable[IntType]],
    ],
    IEnumerable,
    IEnumerable[NullableType[Nullable[IntType]]],
):
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

class NullableLongAverageAggregationOperator(
    InlinedAggregationOperator[
        NullableType[Nullable[LongType]],
        Pair[LongType, LongType],
        NullableType[Nullable[DoubleType]],
    ],
    IEnumerable,
    IEnumerable[Pair[LongType, LongType]],
):
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

class NullableLongMinMaxAggregationOperator(
    InlinedAggregationOperator[
        NullableType[Nullable[LongType]],
        NullableType[Nullable[LongType]],
        NullableType[Nullable[LongType]],
    ],
    IEnumerable,
    IEnumerable[NullableType[Nullable[LongType]]],
):
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

class NullableLongSumAggregationOperator(
    InlinedAggregationOperator[
        NullableType[Nullable[LongType]],
        NullableType[Nullable[LongType]],
        NullableType[Nullable[LongType]],
    ],
    IEnumerable,
    IEnumerable[NullableType[Nullable[LongType]]],
):
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

class OrderPreservingMergeHelper(
    Generic[TInputOutput, TKey], ObjectType, IMergeHelper[TInputOutput]
):
    # No Fields

    # No Constructors

    # No Properties

    # ---------- Methods ---------- #

    def GetResultsAsArray(self) -> ArrayType[TInputOutput]: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class OrderPreservingPipeliningMergeHelper(
    Generic[TOutput, TKey], ObjectType, IMergeHelper[TOutput]
):
    # No Fields

    # No Constructors

    # No Properties

    # ---------- Methods ---------- #

    def GetResultsAsArray(self) -> ArrayType[TOutput]: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class OrderPreservingPipeliningSpoolingTask(Generic[TOutput, TKey], SpoolingTaskBase):
    # No Fields

    # No Constructors

    # No Properties

    # ---------- Methods ---------- #

    @staticmethod
    def Spool(
        groupState: QueryTaskGroupState,
        partitions: PartitionedStream[TOutput, TKey],
        consumerWaiting: ArrayType[BooleanType],
        producerWaiting: ArrayType[BooleanType],
        producerDone: ArrayType[BooleanType],
        buffers: ArrayType[Queue[Pair[TKey, TOutput]]],
        bufferLocks: ArrayType[ObjectType],
        taskScheduler: TaskScheduler,
        autoBuffered: BooleanType,
    ) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class OrderPreservingSpoolingTask(Generic[TInputOutput, TKey], SpoolingTaskBase):
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

class OrderedGroupByElementSelectorQueryOperatorEnumerator(
    Generic[TSource, TGroupKey, TElement, TOrderKey],
    OrderedGroupByQueryOperatorEnumerator[TSource, TGroupKey, TElement, TOrderKey],
):
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

class OrderedGroupByGrouping(
    Generic[TGroupKey, TOrderKey, TElement],
    ObjectType,
    IGrouping[TGroupKey, TElement],
    IEnumerable[TElement],
    IEnumerable,
):
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

class OrderedGroupByIdentityQueryOperatorEnumerator(
    Generic[TSource, TGroupKey, TOrderKey],
    OrderedGroupByQueryOperatorEnumerator[TSource, TGroupKey, TSource, TOrderKey],
):
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

class OrderedGroupByQueryOperatorEnumerator(
    Protocol[TSource, TGroupKey, TElement, TOrderKey],
    QueryOperatorEnumerator[IGrouping[TGroupKey, TElement], TOrderKey],
):
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

class OrderedHashRepartitionEnumerator(
    Generic[TInputOutput, THashKey, TOrderKey],
    QueryOperatorEnumerator[Pair[TInputOutput, THashKey], TOrderKey],
):
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

class OrderedHashRepartitionStream(
    Generic[TInputOutput, THashKey, TOrderKey],
    HashRepartitionStream[TInputOutput, THashKey, TOrderKey],
):
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

class OrderingQueryOperator(
    Generic[TSource], QueryOperator[TSource], IEnumerable, IEnumerable[TSource]
):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, child: QueryOperator[TSource], orderOn: BooleanType): ...

    # No Properties

    # No Methods

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class PairComparer(Generic[T, U], ObjectType, IComparer[Pair[T, U]]):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, comparer1: IComparer[T], comparer2: IComparer[U]): ...

    # No Properties

    # ---------- Methods ---------- #

    def Compare(self, x: Pair[T, U], y: Pair[T, U]) -> IntType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ParallelEnumerableWrapper(ParallelQuery[ObjectType], IEnumerable, IEnumerable[ObjectType]):
    # No Fields

    # No Constructors

    # No Properties

    # ---------- Methods ---------- #

    def GetEnumerator(self) -> IEnumerator[ObjectType]: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ParallelEnumerableWrapper(Generic[T], ParallelQuery[T], IEnumerable, IEnumerable[T]):
    # No Fields

    # No Constructors

    # No Properties

    # ---------- Methods ---------- #

    def GetEnumerator(self) -> IEnumerator[T]: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class PartitionedDataSource(Generic[T], PartitionedStream[T, IntType]):
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

class PartitionedStream(Generic[TElement, TKey], ObjectType):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def PartitionCount(self) -> IntType: ...

    # ---------- Methods ---------- #

    def get_PartitionCount(self) -> IntType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class PartitionedStreamMerger(Generic[TOutput], ObjectType, IPartitionedStreamRecipient[TOutput]):
    # No Fields

    # No Constructors

    # No Properties

    # ---------- Methods ---------- #

    def Receive(self, partitionedStream: PartitionedStream[TOutput, TKey]) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class PartitionerQueryOperator(
    Generic[TElement], QueryOperator[TElement], IEnumerable, IEnumerable[TElement]
):
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

class PipelineSpoolingTask(Generic[TInputOutput, TIgnoreKey], SpoolingTaskBase):
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

class PlinqEtwProvider(EventSource, IDisposable):
    # No Fields

    # No Constructors

    # No Properties

    # No Methods

    # No Events

    # ---------- Sub Classes ---------- #

    class Tasks(ObjectType):
        # ---------- Fields ---------- #

        @staticmethod
        @property
        def ForkJoin() -> EventTask: ...
        @staticmethod
        @property
        def Query() -> EventTask: ...

        # ---------- Constructors ---------- #

        def __init__(self): ...

        # No Properties

        # No Methods

        # No Events

        # No Sub Classes

        # No Sub Structs

        # No Sub Interfaces

        # No Sub Enums
    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ProducerComparerInt(ObjectType, IComparer[Producer[IntType]]):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # No Properties

    # ---------- Methods ---------- #

    def Compare(self, x: Producer[IntType], y: Producer[IntType]) -> IntType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class QueryExecutionOption(
    Generic[TSource], QueryOperator[TSource], IEnumerable, IEnumerable[TSource]
):
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

class QueryLifecycle(ABC, ObjectType):
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

class QueryOpeningEnumerator(
    Generic[TOutput], ObjectType, IEnumerator[TOutput], IDisposable, IEnumerator
):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def Current(self) -> TOutput: ...

    # ---------- Methods ---------- #

    def Dispose(self) -> VoidType: ...
    def MoveNext(self) -> BooleanType: ...
    def Reset(self) -> VoidType: ...
    def get_Current(self) -> TOutput: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class QueryOperator(Protocol[TOutput], ParallelQuery[TOutput], IEnumerable, IEnumerable[TOutput]):
    # No Fields

    # No Constructors

    # No Properties

    # ---------- Methods ---------- #

    @overload
    def GetEnumerator(self) -> IEnumerator[TOutput]: ...
    @overload
    def GetEnumerator(
        self, mergeOptions: NullableType[Nullable[ParallelMergeOptions]]
    ) -> IEnumerator[TOutput]: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class QueryOperatorEnumerator(Protocol[TElement, TKey], ObjectType):
    # No Fields

    # No Constructors

    # No Properties

    # ---------- Methods ---------- #

    def Dispose(self) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class QueryResults(Protocol[T], ObjectType, IList[T], ICollection[T], IEnumerable[T], IEnumerable):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def Count(self) -> IntType: ...
    def __getitem__(self, key: IntType) -> T: ...
    def __setitem__(self, key: IntType, value: T) -> None: ...

    # ---------- Methods ---------- #

    def get_Count(self) -> IntType: ...
    def get_Item(self, index: IntType) -> T: ...
    def set_Item(self, index: IntType, value: T) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class QueryTask(ABC, ObjectType):
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

class QueryTaskGroupState(ObjectType):
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

class RangeEnumerable(
    ParallelQuery[IntType], IEnumerable, IEnumerable[IntType], IParallelPartitionable[IntType]
):
    # No Fields

    # No Constructors

    # No Properties

    # ---------- Methods ---------- #

    def GetEnumerator(self) -> IEnumerator[IntType]: ...
    def GetPartitions(
        self, partitionCount: IntType
    ) -> ArrayType[QueryOperatorEnumerator[IntType, IntType]]: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class RepeatEnumerable(
    Generic[TResult],
    ParallelQuery[TResult],
    IEnumerable,
    IEnumerable[TResult],
    IParallelPartitionable[TResult],
):
    # No Fields

    # No Constructors

    # No Properties

    # ---------- Methods ---------- #

    def GetEnumerator(self) -> IEnumerator[TResult]: ...
    def GetPartitions(
        self, partitionCount: IntType
    ) -> ArrayType[QueryOperatorEnumerator[TResult, IntType]]: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ReverseComparer(Generic[T], ObjectType, IComparer[T]):
    # No Fields

    # No Constructors

    # No Properties

    # ---------- Methods ---------- #

    def Compare(self, x: T, y: T) -> IntType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ReverseQueryOperator(
    Generic[TSource], UnaryQueryOperator[TSource, TSource], IEnumerable, IEnumerable[TSource]
):
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

class ScanQueryOperator(
    Generic[TElement], QueryOperator[TElement], IEnumerable, IEnumerable[TElement]
):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def Data(self) -> IEnumerable[TElement]: ...

    # ---------- Methods ---------- #

    def get_Data(self) -> IEnumerable[TElement]: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class Scheduling(ABC, ObjectType):
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

class SelectManyQueryOperator(
    Generic[TLeftInput, TRightInput, TOutput],
    UnaryQueryOperator[TLeftInput, TOutput],
    IEnumerable,
    IEnumerable[TOutput],
):
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

class SelectQueryOperator(
    Generic[TInput, TOutput], UnaryQueryOperator[TInput, TOutput], IEnumerable, IEnumerable[TOutput]
):
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

class Shared(Generic[T], ObjectType):
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

class SingleQueryOperator(
    Generic[TSource], UnaryQueryOperator[TSource, TSource], IEnumerable, IEnumerable[TSource]
):
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

class SortHelper(Protocol[TInputOutput], ObjectType):
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

class SortHelper(Generic[TInputOutput, TKey], SortHelper[TInputOutput], IDisposable):
    # No Fields

    # No Constructors

    # No Properties

    # ---------- Methods ---------- #

    def Dispose(self) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class SortQueryOperator(
    Generic[TInputOutput, TSortKey],
    UnaryQueryOperator[TInputOutput, TInputOutput],
    IEnumerable,
    IEnumerable[TInputOutput],
    IOrderedEnumerable[TInputOutput],
):
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

class SortQueryOperatorEnumerator(
    Generic[TInputOutput, TKey, TSortKey], QueryOperatorEnumerator[TInputOutput, TSortKey]
):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def KeyComparer(self) -> IComparer[TSortKey]: ...

    # ---------- Methods ---------- #

    def get_KeyComparer(self) -> IComparer[TSortKey]: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class SortQueryOperatorResults(
    Generic[TInputOutput, TSortKey],
    QueryResults[TInputOutput],
    IList[TInputOutput],
    ICollection[TInputOutput],
    IEnumerable[TInputOutput],
    IEnumerable,
):
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

class SpoolingTask(ABC, ObjectType):
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

class SpoolingTaskBase(ABC, QueryTask):
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

class StopAndGoSpoolingTask(Generic[TInputOutput, TIgnoreKey], SpoolingTaskBase):
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

class SynchronousChannel(Generic[T], ObjectType):
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

class SynchronousChannelMergeEnumerator(
    Generic[T], MergeEnumerator[T], IEnumerator[T], IDisposable, IEnumerator
):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def Current(self) -> T: ...

    # ---------- Methods ---------- #

    def MoveNext(self) -> BooleanType: ...
    def get_Current(self) -> T: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class TakeOrSkipQueryOperator(
    Generic[TResult], UnaryQueryOperator[TResult, TResult], IEnumerable, IEnumerable[TResult]
):
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

class TakeOrSkipWhileQueryOperator(
    Generic[TResult], UnaryQueryOperator[TResult, TResult], IEnumerable, IEnumerable[TResult]
):
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

class TraceHelpers(ABC, ObjectType):
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

class UnaryQueryOperator(
    Protocol[TInput, TOutput], QueryOperator[TOutput], IEnumerable, IEnumerable[TOutput]
):
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

class UnionQueryOperator(
    Generic[TInputOutput],
    BinaryQueryOperator[TInputOutput, TInputOutput, TInputOutput],
    IEnumerable,
    IEnumerable[TInputOutput],
):
    # No Fields

    # No Constructors

    # No Properties

    # ---------- Methods ---------- #

    def WrapPartitionedStream(
        self,
        leftStream: PartitionedStream[TInputOutput, TLeftKey],
        rightStream: PartitionedStream[TInputOutput, TRightKey],
        outputRecipient: IPartitionedStreamRecipient[TInputOutput],
        preferStriping: BooleanType,
        settings: QuerySettings,
    ) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class UnorderedHashRepartitionStream(
    Generic[TInputOutput, THashKey, TIgnoreKey],
    HashRepartitionStream[TInputOutput, THashKey, IntType],
):
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

class Util(ABC, ObjectType):
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

class WhereQueryOperator(
    Generic[TInputOutput],
    UnaryQueryOperator[TInputOutput, TInputOutput],
    IEnumerable,
    IEnumerable[TInputOutput],
):
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

class ZipQueryOperator(
    Generic[TLeftInput, TRightInput, TOutput],
    QueryOperator[TOutput],
    IEnumerable,
    IEnumerable[TOutput],
):
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

# ---------- Structs ---------- #

class ConcatKey(Generic[TLeftKey, TRightKey], ValueType):
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

class NoKeyMemoizationRequired(ValueType):
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

class Pair(Generic[T, U], ValueType):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, first: T, second: U): ...

    # ---------- Properties ---------- #

    @property
    def First(self) -> T: ...
    @First.setter
    def First(self, value: T) -> None: ...
    @property
    def Second(self) -> U: ...
    @Second.setter
    def Second(self, value: U) -> None: ...

    # ---------- Methods ---------- #

    def get_First(self) -> T: ...
    def get_Second(self) -> U: ...
    def set_First(self, value: T) -> VoidType: ...
    def set_Second(self, value: U) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class Producer(Generic[TKey], ValueType):
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

class QuerySettings(ValueType):
    # No Fields

    # No Constructors

    # No Properties

    # ---------- Methods ---------- #

    def CleanStateAtQueryEnd(self) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class Wrapper(Generic[T], ValueType):
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

class WrapperEqualityComparer(Generic[T], ValueType, IEqualityComparer[Wrapper[T]]):
    # No Fields

    # No Constructors

    # No Properties

    # ---------- Methods ---------- #

    @overload
    def Equals(self, x: Wrapper[T], y: Wrapper[T]) -> BooleanType: ...
    @overload
    def GetHashCode(self, x: Wrapper[T]) -> IntType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

# ---------- Interfaces ---------- #

class IMergeHelper(Protocol[TInputOutput]):
    # No Properties

    # ---------- Methods ---------- #

    def Execute(self) -> VoidType: ...
    def GetEnumerator(self) -> IEnumerator[TInputOutput]: ...
    def GetResultsAsArray(self) -> ArrayType[TInputOutput]: ...

    # No Events

class IParallelPartitionable(Protocol[T]):
    # No Properties

    # ---------- Methods ---------- #

    def GetPartitions(
        self, partitionCount: IntType
    ) -> ArrayType[QueryOperatorEnumerator[T, IntType]]: ...

    # No Events

class IPartitionedStreamRecipient(Protocol[TElement]):
    # No Properties

    # ---------- Methods ---------- #

    def Receive(self, partitionedStream: PartitionedStream[TElement, TKey]) -> VoidType: ...

    # No Events

# ---------- Enums ---------- #

class OrdinalIndexState(Enum):
    Indexible = 0
    Correct = 1
    Increasing = 2
    Shuffled = 3

class QueryAggregationOptions(Enum):
    # None = 0
    Associative = 1
    Commutative = 2
    AssociativeCommutative = 3

# No Delegates

__all__ = [
    AnyAllSearchOperator,
    ArrayMergeHelper,
    AssociativeAggregationOperator,
    AsynchronousChannel,
    AsynchronousChannelMergeEnumerator,
    BinaryQueryOperator,
    CancellableEnumerable,
    CancellationState,
    ConcatQueryOperator,
    ContainsSearchOperator,
    CountAggregationOperator,
    DecimalAverageAggregationOperator,
    DecimalMinMaxAggregationOperator,
    DecimalSumAggregationOperator,
    DefaultIfEmptyQueryOperator,
    DefaultMergeHelper,
    DistinctQueryOperator,
    DoubleAverageAggregationOperator,
    DoubleMinMaxAggregationOperator,
    DoubleSumAggregationOperator,
    ElementAtQueryOperator,
    EmptyEnumerable,
    EmptyEnumerator,
    EnumerableWrapperWeakToStrong,
    ExceptQueryOperator,
    ExceptionAggregator,
    ExchangeUtilities,
    FirstQueryOperator,
    FixedMaxHeap,
    FloatAverageAggregationOperator,
    FloatMinMaxAggregationOperator,
    FloatSumAggregationOperator,
    ForAllOperator,
    ForAllSpoolingTask,
    GroupByElementSelectorQueryOperatorEnumerator,
    GroupByGrouping,
    GroupByIdentityQueryOperatorEnumerator,
    GroupByQueryOperator,
    GroupByQueryOperatorEnumerator,
    GroupJoinQueryOperator,
    GrowingArray,
    HashJoinQueryOperatorEnumerator,
    HashLookup,
    HashRepartitionEnumerator,
    HashRepartitionStream,
    IndexedSelectQueryOperator,
    IndexedWhereQueryOperator,
    InlinedAggregationOperator,
    InlinedAggregationOperatorEnumerator,
    IntAverageAggregationOperator,
    IntMinMaxAggregationOperator,
    IntSumAggregationOperator,
    IntValueEvent,
    IntersectQueryOperator,
    JoinQueryOperator,
    LastQueryOperator,
    ListChunk,
    ListQueryResults,
    LongAverageAggregationOperator,
    LongCountAggregationOperator,
    LongMinMaxAggregationOperator,
    LongSumAggregationOperator,
    Lookup,
    MergeEnumerator,
    MergeExecutor,
    NullableDecimalAverageAggregationOperator,
    NullableDecimalMinMaxAggregationOperator,
    NullableDecimalSumAggregationOperator,
    NullableDoubleAverageAggregationOperator,
    NullableDoubleMinMaxAggregationOperator,
    NullableDoubleSumAggregationOperator,
    NullableFloatAverageAggregationOperator,
    NullableFloatMinMaxAggregationOperator,
    NullableFloatSumAggregationOperator,
    NullableIntAverageAggregationOperator,
    NullableIntMinMaxAggregationOperator,
    NullableIntSumAggregationOperator,
    NullableLongAverageAggregationOperator,
    NullableLongMinMaxAggregationOperator,
    NullableLongSumAggregationOperator,
    OrderPreservingMergeHelper,
    OrderPreservingPipeliningMergeHelper,
    OrderPreservingPipeliningSpoolingTask,
    OrderPreservingSpoolingTask,
    OrderedGroupByElementSelectorQueryOperatorEnumerator,
    OrderedGroupByGrouping,
    OrderedGroupByIdentityQueryOperatorEnumerator,
    OrderedGroupByQueryOperatorEnumerator,
    OrderedHashRepartitionEnumerator,
    OrderedHashRepartitionStream,
    OrderingQueryOperator,
    PairComparer,
    ParallelEnumerableWrapper,
    PartitionedDataSource,
    PartitionedStream,
    PartitionedStreamMerger,
    PartitionerQueryOperator,
    PipelineSpoolingTask,
    PlinqEtwProvider,
    ProducerComparerInt,
    QueryExecutionOption,
    QueryLifecycle,
    QueryOpeningEnumerator,
    QueryOperator,
    QueryOperatorEnumerator,
    QueryResults,
    QueryTask,
    QueryTaskGroupState,
    RangeEnumerable,
    RepeatEnumerable,
    ReverseComparer,
    ReverseQueryOperator,
    ScanQueryOperator,
    Scheduling,
    SelectManyQueryOperator,
    SelectQueryOperator,
    Shared,
    SingleQueryOperator,
    SortHelper,
    SortQueryOperator,
    SortQueryOperatorEnumerator,
    SortQueryOperatorResults,
    SpoolingTask,
    SpoolingTaskBase,
    StopAndGoSpoolingTask,
    SynchronousChannel,
    SynchronousChannelMergeEnumerator,
    TakeOrSkipQueryOperator,
    TakeOrSkipWhileQueryOperator,
    TraceHelpers,
    UnaryQueryOperator,
    UnionQueryOperator,
    UnorderedHashRepartitionStream,
    Util,
    WhereQueryOperator,
    ZipQueryOperator,
    ConcatKey,
    NoKeyMemoizationRequired,
    Pair,
    Producer,
    QuerySettings,
    Wrapper,
    WrapperEqualityComparer,
    IMergeHelper,
    IParallelPartitionable,
    IPartitionedStreamRecipient,
    OrdinalIndexState,
    QueryAggregationOptions,
]
