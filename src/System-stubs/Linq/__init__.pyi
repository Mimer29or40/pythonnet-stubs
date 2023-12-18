from __future__ import annotations

from abc import ABC
from typing import Generic
from typing import List
from typing import Optional
from typing import Protocol
from typing import Tuple
from typing import TypeVar
from typing import Union
from typing import overload

from System import Action
from System import Array
from System import Boolean
from System import Decimal
from System import Double
from System import Enum
from System import Exception
from System import Func
from System import Int32
from System import Int64
from System import Nullable
from System import Object
from System import Single
from System import String
from System import Type
from System import ValueType
from System import Void
from System.Collections import IEnumerable
from System.Collections.Concurrent import Partitioner
from System.Collections.Generic import Dictionary
from System.Collections.Generic import HashSet
from System.Collections.Generic import IComparer
from System.Collections.Generic import IEnumerable
from System.Collections.Generic import IEnumerator
from System.Collections.Generic import IEqualityComparer
from System.Collections.Generic import List
from System.ComponentModel import CategoryAttribute
from System.ComponentModel import DescriptionAttribute
from System.Linq.Expressions import Expression
from System.Linq.Expressions import OldExpressionVisitor
from System.Resources import ResourceManager
from System.Runtime.InteropServices import _Attribute
from System.Runtime.InteropServices import _Exception
from System.Runtime.Serialization import ISerializable
from System.Threading import CancellationToken

# ---------- Types ---------- #

T = TypeVar("T")
TAccumulate = TypeVar("TAccumulate")
TCollection = TypeVar("TCollection")
TElement = TypeVar("TElement")
TFirst = TypeVar("TFirst")
TInner = TypeVar("TInner")
TKey = TypeVar("TKey")
TOuter = TypeVar("TOuter")
TResult = TypeVar("TResult")
TSecond = TypeVar("TSecond")
TSource = TypeVar("TSource")

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
DecimalType = Union[float, Decimal]
DoubleType = Union[float, Double]
FloatType = Union[float, Single]
IntType = Union[int, Int32]
LongType = Union[int, Int64]
NullableType = Union[Optional, Nullable]
ObjectType = Object
StringType = Union[str, String]
TypeType = Union[type, Type]
VoidType = Union[None, Void]

# ---------- Classes ---------- #

class AggregationMinMaxHelpers(Protocol[T], ObjectType):
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

class EmptyEnumerable(Generic[TElement], ObjectType):
    # ---------- Fields ---------- #

    @staticmethod
    @property
    def Instance() -> ArrayType[TElement]: ...

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # No Properties

    # No Methods

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class Enumerable(ABC, ObjectType):
    # No Fields

    # No Constructors

    # No Properties

    # ---------- Methods ---------- #

    @staticmethod
    @overload
    def Aggregate(
        source: IEnumerable[TSource], func: Func[TSource, TSource, TSource]
    ) -> TSource: ...
    @staticmethod
    @overload
    def Aggregate(
        source: IEnumerable[TSource],
        seed: TAccumulate,
        func: Func[TAccumulate, TSource, TAccumulate],
    ) -> TAccumulate: ...
    @staticmethod
    @overload
    def Aggregate(
        source: IEnumerable[TSource],
        seed: TAccumulate,
        func: Func[TAccumulate, TSource, TAccumulate],
        resultSelector: Func[TAccumulate, TResult],
    ) -> TResult: ...
    @staticmethod
    def All(source: IEnumerable[TSource], predicate: Func[TSource, BooleanType]) -> BooleanType: ...
    @staticmethod
    @overload
    def Any(source: IEnumerable[TSource]) -> BooleanType: ...
    @staticmethod
    @overload
    def Any(source: IEnumerable[TSource], predicate: Func[TSource, BooleanType]) -> BooleanType: ...
    @staticmethod
    def Append(source: IEnumerable[TSource], element: TSource) -> IEnumerable[TSource]: ...
    @staticmethod
    def AsEnumerable(source: IEnumerable[TSource]) -> IEnumerable[TSource]: ...
    @staticmethod
    @overload
    def Average(source: IEnumerable[IntType]) -> DoubleType: ...
    @staticmethod
    @overload
    def Average(source: IEnumerable[LongType]) -> DoubleType: ...
    @staticmethod
    @overload
    def Average(source: IEnumerable[FloatType]) -> FloatType: ...
    @staticmethod
    @overload
    def Average(source: IEnumerable[DoubleType]) -> DoubleType: ...
    @staticmethod
    @overload
    def Average(source: IEnumerable[DecimalType]) -> DecimalType: ...
    @staticmethod
    @overload
    def Average(
        source: IEnumerable[NullableType[Nullable[IntType]]],
    ) -> NullableType[Nullable[DoubleType]]: ...
    @staticmethod
    @overload
    def Average(
        source: IEnumerable[NullableType[Nullable[LongType]]],
    ) -> NullableType[Nullable[DoubleType]]: ...
    @staticmethod
    @overload
    def Average(
        source: IEnumerable[NullableType[Nullable[FloatType]]],
    ) -> NullableType[Nullable[FloatType]]: ...
    @staticmethod
    @overload
    def Average(
        source: IEnumerable[NullableType[Nullable[DoubleType]]],
    ) -> NullableType[Nullable[DoubleType]]: ...
    @staticmethod
    @overload
    def Average(
        source: IEnumerable[NullableType[Nullable[DecimalType]]],
    ) -> NullableType[Nullable[DecimalType]]: ...
    @staticmethod
    @overload
    def Average(source: IEnumerable[TSource], selector: Func[TSource, IntType]) -> DoubleType: ...
    @staticmethod
    @overload
    def Average(
        source: IEnumerable[TSource], selector: Func[TSource, NullableType[Nullable[IntType]]]
    ) -> NullableType[Nullable[DoubleType]]: ...
    @staticmethod
    @overload
    def Average(source: IEnumerable[TSource], selector: Func[TSource, LongType]) -> DoubleType: ...
    @staticmethod
    @overload
    def Average(
        source: IEnumerable[TSource], selector: Func[TSource, NullableType[Nullable[LongType]]]
    ) -> NullableType[Nullable[DoubleType]]: ...
    @staticmethod
    @overload
    def Average(source: IEnumerable[TSource], selector: Func[TSource, FloatType]) -> FloatType: ...
    @staticmethod
    @overload
    def Average(
        source: IEnumerable[TSource], selector: Func[TSource, NullableType[Nullable[FloatType]]]
    ) -> NullableType[Nullable[FloatType]]: ...
    @staticmethod
    @overload
    def Average(
        source: IEnumerable[TSource], selector: Func[TSource, DoubleType]
    ) -> DoubleType: ...
    @staticmethod
    @overload
    def Average(
        source: IEnumerable[TSource], selector: Func[TSource, NullableType[Nullable[DoubleType]]]
    ) -> NullableType[Nullable[DoubleType]]: ...
    @staticmethod
    @overload
    def Average(
        source: IEnumerable[TSource], selector: Func[TSource, DecimalType]
    ) -> DecimalType: ...
    @staticmethod
    @overload
    def Average(
        source: IEnumerable[TSource], selector: Func[TSource, NullableType[Nullable[DecimalType]]]
    ) -> NullableType[Nullable[DecimalType]]: ...
    @staticmethod
    def Cast(source: IEnumerable) -> IEnumerable[TResult]: ...
    @staticmethod
    def Concat(
        first: IEnumerable[TSource], second: IEnumerable[TSource]
    ) -> IEnumerable[TSource]: ...
    @staticmethod
    @overload
    def Contains(source: IEnumerable[TSource], value: TSource) -> BooleanType: ...
    @staticmethod
    @overload
    def Contains(
        source: IEnumerable[TSource], value: TSource, comparer: IEqualityComparer[TSource]
    ) -> BooleanType: ...
    @staticmethod
    @overload
    def Count(source: IEnumerable[TSource]) -> IntType: ...
    @staticmethod
    @overload
    def Count(source: IEnumerable[TSource], predicate: Func[TSource, BooleanType]) -> IntType: ...
    @staticmethod
    @overload
    def DefaultIfEmpty(source: IEnumerable[TSource]) -> IEnumerable[TSource]: ...
    @staticmethod
    @overload
    def DefaultIfEmpty(
        source: IEnumerable[TSource], defaultValue: TSource
    ) -> IEnumerable[TSource]: ...
    @staticmethod
    @overload
    def Distinct(source: IEnumerable[TSource]) -> IEnumerable[TSource]: ...
    @staticmethod
    @overload
    def Distinct(
        source: IEnumerable[TSource], comparer: IEqualityComparer[TSource]
    ) -> IEnumerable[TSource]: ...
    @staticmethod
    def ElementAt(source: IEnumerable[TSource], index: IntType) -> TSource: ...
    @staticmethod
    def ElementAtOrDefault(source: IEnumerable[TSource], index: IntType) -> TSource: ...
    @staticmethod
    def Empty() -> IEnumerable[TResult]: ...
    @staticmethod
    @overload
    def Except(
        first: IEnumerable[TSource], second: IEnumerable[TSource]
    ) -> IEnumerable[TSource]: ...
    @staticmethod
    @overload
    def Except(
        first: IEnumerable[TSource],
        second: IEnumerable[TSource],
        comparer: IEqualityComparer[TSource],
    ) -> IEnumerable[TSource]: ...
    @staticmethod
    @overload
    def First(source: IEnumerable[TSource]) -> TSource: ...
    @staticmethod
    @overload
    def First(source: IEnumerable[TSource], predicate: Func[TSource, BooleanType]) -> TSource: ...
    @staticmethod
    @overload
    def FirstOrDefault(source: IEnumerable[TSource]) -> TSource: ...
    @staticmethod
    @overload
    def FirstOrDefault(
        source: IEnumerable[TSource], predicate: Func[TSource, BooleanType]
    ) -> TSource: ...
    @staticmethod
    @overload
    def GroupBy(
        source: IEnumerable[TSource], keySelector: Func[TSource, TKey]
    ) -> IEnumerable[IGrouping[TKey, TSource]]: ...
    @staticmethod
    @overload
    def GroupBy(
        source: IEnumerable[TSource],
        keySelector: Func[TSource, TKey],
        comparer: IEqualityComparer[TKey],
    ) -> IEnumerable[IGrouping[TKey, TSource]]: ...
    @staticmethod
    @overload
    def GroupBy(
        source: IEnumerable[TSource],
        keySelector: Func[TSource, TKey],
        elementSelector: Func[TSource, TElement],
    ) -> IEnumerable[IGrouping[TKey, TElement]]: ...
    @staticmethod
    @overload
    def GroupBy(
        source: IEnumerable[TSource],
        keySelector: Func[TSource, TKey],
        elementSelector: Func[TSource, TElement],
        comparer: IEqualityComparer[TKey],
    ) -> IEnumerable[IGrouping[TKey, TElement]]: ...
    @staticmethod
    @overload
    def GroupBy(
        source: IEnumerable[TSource],
        keySelector: Func[TSource, TKey],
        resultSelector: Func[TKey, IEnumerable[TSource], TResult],
    ) -> IEnumerable[TResult]: ...
    @staticmethod
    @overload
    def GroupBy(
        source: IEnumerable[TSource],
        keySelector: Func[TSource, TKey],
        elementSelector: Func[TSource, TElement],
        resultSelector: Func[TKey, IEnumerable[TElement], TResult],
    ) -> IEnumerable[TResult]: ...
    @staticmethod
    @overload
    def GroupBy(
        source: IEnumerable[TSource],
        keySelector: Func[TSource, TKey],
        resultSelector: Func[TKey, IEnumerable[TSource], TResult],
        comparer: IEqualityComparer[TKey],
    ) -> IEnumerable[TResult]: ...
    @staticmethod
    @overload
    def GroupBy(
        source: IEnumerable[TSource],
        keySelector: Func[TSource, TKey],
        elementSelector: Func[TSource, TElement],
        resultSelector: Func[TKey, IEnumerable[TElement], TResult],
        comparer: IEqualityComparer[TKey],
    ) -> IEnumerable[TResult]: ...
    @staticmethod
    @overload
    def GroupJoin(
        outer: IEnumerable[TOuter],
        inner: IEnumerable[TInner],
        outerKeySelector: Func[TOuter, TKey],
        innerKeySelector: Func[TInner, TKey],
        resultSelector: Func[TOuter, IEnumerable[TInner], TResult],
    ) -> IEnumerable[TResult]: ...
    @staticmethod
    @overload
    def GroupJoin(
        outer: IEnumerable[TOuter],
        inner: IEnumerable[TInner],
        outerKeySelector: Func[TOuter, TKey],
        innerKeySelector: Func[TInner, TKey],
        resultSelector: Func[TOuter, IEnumerable[TInner], TResult],
        comparer: IEqualityComparer[TKey],
    ) -> IEnumerable[TResult]: ...
    @staticmethod
    @overload
    def Intersect(
        first: IEnumerable[TSource], second: IEnumerable[TSource]
    ) -> IEnumerable[TSource]: ...
    @staticmethod
    @overload
    def Intersect(
        first: IEnumerable[TSource],
        second: IEnumerable[TSource],
        comparer: IEqualityComparer[TSource],
    ) -> IEnumerable[TSource]: ...
    @staticmethod
    @overload
    def Join(
        outer: IEnumerable[TOuter],
        inner: IEnumerable[TInner],
        outerKeySelector: Func[TOuter, TKey],
        innerKeySelector: Func[TInner, TKey],
        resultSelector: Func[TOuter, TInner, TResult],
    ) -> IEnumerable[TResult]: ...
    @staticmethod
    @overload
    def Join(
        outer: IEnumerable[TOuter],
        inner: IEnumerable[TInner],
        outerKeySelector: Func[TOuter, TKey],
        innerKeySelector: Func[TInner, TKey],
        resultSelector: Func[TOuter, TInner, TResult],
        comparer: IEqualityComparer[TKey],
    ) -> IEnumerable[TResult]: ...
    @staticmethod
    @overload
    def Last(source: IEnumerable[TSource]) -> TSource: ...
    @staticmethod
    @overload
    def Last(source: IEnumerable[TSource], predicate: Func[TSource, BooleanType]) -> TSource: ...
    @staticmethod
    @overload
    def LastOrDefault(source: IEnumerable[TSource]) -> TSource: ...
    @staticmethod
    @overload
    def LastOrDefault(
        source: IEnumerable[TSource], predicate: Func[TSource, BooleanType]
    ) -> TSource: ...
    @staticmethod
    @overload
    def LongCount(source: IEnumerable[TSource]) -> LongType: ...
    @staticmethod
    @overload
    def LongCount(
        source: IEnumerable[TSource], predicate: Func[TSource, BooleanType]
    ) -> LongType: ...
    @staticmethod
    @overload
    def Max(source: IEnumerable[IntType]) -> IntType: ...
    @staticmethod
    @overload
    def Max(source: IEnumerable[LongType]) -> LongType: ...
    @staticmethod
    @overload
    def Max(source: IEnumerable[DoubleType]) -> DoubleType: ...
    @staticmethod
    @overload
    def Max(source: IEnumerable[FloatType]) -> FloatType: ...
    @staticmethod
    @overload
    def Max(source: IEnumerable[DecimalType]) -> DecimalType: ...
    @staticmethod
    @overload
    def Max(
        source: IEnumerable[NullableType[Nullable[IntType]]],
    ) -> NullableType[Nullable[IntType]]: ...
    @staticmethod
    @overload
    def Max(
        source: IEnumerable[NullableType[Nullable[LongType]]],
    ) -> NullableType[Nullable[LongType]]: ...
    @staticmethod
    @overload
    def Max(
        source: IEnumerable[NullableType[Nullable[DoubleType]]],
    ) -> NullableType[Nullable[DoubleType]]: ...
    @staticmethod
    @overload
    def Max(
        source: IEnumerable[NullableType[Nullable[FloatType]]],
    ) -> NullableType[Nullable[FloatType]]: ...
    @staticmethod
    @overload
    def Max(
        source: IEnumerable[NullableType[Nullable[DecimalType]]],
    ) -> NullableType[Nullable[DecimalType]]: ...
    @staticmethod
    @overload
    def Max(source: IEnumerable[TSource]) -> TSource: ...
    @staticmethod
    @overload
    def Max(source: IEnumerable[TSource], selector: Func[TSource, IntType]) -> IntType: ...
    @staticmethod
    @overload
    def Max(
        source: IEnumerable[TSource], selector: Func[TSource, NullableType[Nullable[IntType]]]
    ) -> NullableType[Nullable[IntType]]: ...
    @staticmethod
    @overload
    def Max(source: IEnumerable[TSource], selector: Func[TSource, LongType]) -> LongType: ...
    @staticmethod
    @overload
    def Max(
        source: IEnumerable[TSource], selector: Func[TSource, NullableType[Nullable[LongType]]]
    ) -> NullableType[Nullable[LongType]]: ...
    @staticmethod
    @overload
    def Max(source: IEnumerable[TSource], selector: Func[TSource, FloatType]) -> FloatType: ...
    @staticmethod
    @overload
    def Max(
        source: IEnumerable[TSource], selector: Func[TSource, NullableType[Nullable[FloatType]]]
    ) -> NullableType[Nullable[FloatType]]: ...
    @staticmethod
    @overload
    def Max(source: IEnumerable[TSource], selector: Func[TSource, DoubleType]) -> DoubleType: ...
    @staticmethod
    @overload
    def Max(
        source: IEnumerable[TSource], selector: Func[TSource, NullableType[Nullable[DoubleType]]]
    ) -> NullableType[Nullable[DoubleType]]: ...
    @staticmethod
    @overload
    def Max(source: IEnumerable[TSource], selector: Func[TSource, DecimalType]) -> DecimalType: ...
    @staticmethod
    @overload
    def Max(
        source: IEnumerable[TSource], selector: Func[TSource, NullableType[Nullable[DecimalType]]]
    ) -> NullableType[Nullable[DecimalType]]: ...
    @staticmethod
    @overload
    def Max(source: IEnumerable[TSource], selector: Func[TSource, TResult]) -> TResult: ...
    @staticmethod
    @overload
    def Min(source: IEnumerable[IntType]) -> IntType: ...
    @staticmethod
    @overload
    def Min(source: IEnumerable[LongType]) -> LongType: ...
    @staticmethod
    @overload
    def Min(source: IEnumerable[FloatType]) -> FloatType: ...
    @staticmethod
    @overload
    def Min(source: IEnumerable[DoubleType]) -> DoubleType: ...
    @staticmethod
    @overload
    def Min(source: IEnumerable[DecimalType]) -> DecimalType: ...
    @staticmethod
    @overload
    def Min(
        source: IEnumerable[NullableType[Nullable[IntType]]],
    ) -> NullableType[Nullable[IntType]]: ...
    @staticmethod
    @overload
    def Min(
        source: IEnumerable[NullableType[Nullable[LongType]]],
    ) -> NullableType[Nullable[LongType]]: ...
    @staticmethod
    @overload
    def Min(
        source: IEnumerable[NullableType[Nullable[FloatType]]],
    ) -> NullableType[Nullable[FloatType]]: ...
    @staticmethod
    @overload
    def Min(
        source: IEnumerable[NullableType[Nullable[DoubleType]]],
    ) -> NullableType[Nullable[DoubleType]]: ...
    @staticmethod
    @overload
    def Min(
        source: IEnumerable[NullableType[Nullable[DecimalType]]],
    ) -> NullableType[Nullable[DecimalType]]: ...
    @staticmethod
    @overload
    def Min(source: IEnumerable[TSource]) -> TSource: ...
    @staticmethod
    @overload
    def Min(source: IEnumerable[TSource], selector: Func[TSource, IntType]) -> IntType: ...
    @staticmethod
    @overload
    def Min(
        source: IEnumerable[TSource], selector: Func[TSource, NullableType[Nullable[IntType]]]
    ) -> NullableType[Nullable[IntType]]: ...
    @staticmethod
    @overload
    def Min(source: IEnumerable[TSource], selector: Func[TSource, LongType]) -> LongType: ...
    @staticmethod
    @overload
    def Min(
        source: IEnumerable[TSource], selector: Func[TSource, NullableType[Nullable[LongType]]]
    ) -> NullableType[Nullable[LongType]]: ...
    @staticmethod
    @overload
    def Min(source: IEnumerable[TSource], selector: Func[TSource, FloatType]) -> FloatType: ...
    @staticmethod
    @overload
    def Min(
        source: IEnumerable[TSource], selector: Func[TSource, NullableType[Nullable[FloatType]]]
    ) -> NullableType[Nullable[FloatType]]: ...
    @staticmethod
    @overload
    def Min(source: IEnumerable[TSource], selector: Func[TSource, DoubleType]) -> DoubleType: ...
    @staticmethod
    @overload
    def Min(
        source: IEnumerable[TSource], selector: Func[TSource, NullableType[Nullable[DoubleType]]]
    ) -> NullableType[Nullable[DoubleType]]: ...
    @staticmethod
    @overload
    def Min(source: IEnumerable[TSource], selector: Func[TSource, DecimalType]) -> DecimalType: ...
    @staticmethod
    @overload
    def Min(
        source: IEnumerable[TSource], selector: Func[TSource, NullableType[Nullable[DecimalType]]]
    ) -> NullableType[Nullable[DecimalType]]: ...
    @staticmethod
    @overload
    def Min(source: IEnumerable[TSource], selector: Func[TSource, TResult]) -> TResult: ...
    @staticmethod
    def OfType(source: IEnumerable) -> IEnumerable[TResult]: ...
    @staticmethod
    @overload
    def OrderBy(
        source: IEnumerable[TSource], keySelector: Func[TSource, TKey]
    ) -> IOrderedEnumerable[TSource]: ...
    @staticmethod
    @overload
    def OrderBy(
        source: IEnumerable[TSource], keySelector: Func[TSource, TKey], comparer: IComparer[TKey]
    ) -> IOrderedEnumerable[TSource]: ...
    @staticmethod
    @overload
    def OrderByDescending(
        source: IEnumerable[TSource], keySelector: Func[TSource, TKey]
    ) -> IOrderedEnumerable[TSource]: ...
    @staticmethod
    @overload
    def OrderByDescending(
        source: IEnumerable[TSource], keySelector: Func[TSource, TKey], comparer: IComparer[TKey]
    ) -> IOrderedEnumerable[TSource]: ...
    @staticmethod
    def Prepend(source: IEnumerable[TSource], element: TSource) -> IEnumerable[TSource]: ...
    @staticmethod
    def Range(start: IntType, count: IntType) -> IEnumerable[IntType]: ...
    @staticmethod
    def Repeat(element: TResult, count: IntType) -> IEnumerable[TResult]: ...
    @staticmethod
    def Reverse(source: IEnumerable[TSource]) -> IEnumerable[TSource]: ...
    @staticmethod
    @overload
    def Select(
        source: IEnumerable[TSource], selector: Func[TSource, TResult]
    ) -> IEnumerable[TResult]: ...
    @staticmethod
    @overload
    def Select(
        source: IEnumerable[TSource], selector: Func[TSource, IntType, TResult]
    ) -> IEnumerable[TResult]: ...
    @staticmethod
    @overload
    def SelectMany(
        source: IEnumerable[TSource], selector: Func[TSource, IEnumerable[TResult]]
    ) -> IEnumerable[TResult]: ...
    @staticmethod
    @overload
    def SelectMany(
        source: IEnumerable[TSource], selector: Func[TSource, IntType, IEnumerable[TResult]]
    ) -> IEnumerable[TResult]: ...
    @staticmethod
    @overload
    def SelectMany(
        source: IEnumerable[TSource],
        collectionSelector: Func[TSource, IntType, IEnumerable[TCollection]],
        resultSelector: Func[TSource, TCollection, TResult],
    ) -> IEnumerable[TResult]: ...
    @staticmethod
    @overload
    def SelectMany(
        source: IEnumerable[TSource],
        collectionSelector: Func[TSource, IEnumerable[TCollection]],
        resultSelector: Func[TSource, TCollection, TResult],
    ) -> IEnumerable[TResult]: ...
    @staticmethod
    @overload
    def SequenceEqual(first: IEnumerable[TSource], second: IEnumerable[TSource]) -> BooleanType: ...
    @staticmethod
    @overload
    def SequenceEqual(
        first: IEnumerable[TSource],
        second: IEnumerable[TSource],
        comparer: IEqualityComparer[TSource],
    ) -> BooleanType: ...
    @staticmethod
    @overload
    def Single(source: IEnumerable[TSource]) -> TSource: ...
    @staticmethod
    @overload
    def Single(source: IEnumerable[TSource], predicate: Func[TSource, BooleanType]) -> TSource: ...
    @staticmethod
    @overload
    def SingleOrDefault(source: IEnumerable[TSource]) -> TSource: ...
    @staticmethod
    @overload
    def SingleOrDefault(
        source: IEnumerable[TSource], predicate: Func[TSource, BooleanType]
    ) -> TSource: ...
    @staticmethod
    def Skip(source: IEnumerable[TSource], count: IntType) -> IEnumerable[TSource]: ...
    @staticmethod
    @overload
    def SkipWhile(
        source: IEnumerable[TSource], predicate: Func[TSource, BooleanType]
    ) -> IEnumerable[TSource]: ...
    @staticmethod
    @overload
    def SkipWhile(
        source: IEnumerable[TSource], predicate: Func[TSource, IntType, BooleanType]
    ) -> IEnumerable[TSource]: ...
    @staticmethod
    @overload
    def Sum(source: IEnumerable[IntType]) -> IntType: ...
    @staticmethod
    @overload
    def Sum(source: IEnumerable[LongType]) -> LongType: ...
    @staticmethod
    @overload
    def Sum(source: IEnumerable[FloatType]) -> FloatType: ...
    @staticmethod
    @overload
    def Sum(source: IEnumerable[DoubleType]) -> DoubleType: ...
    @staticmethod
    @overload
    def Sum(source: IEnumerable[DecimalType]) -> DecimalType: ...
    @staticmethod
    @overload
    def Sum(
        source: IEnumerable[NullableType[Nullable[IntType]]],
    ) -> NullableType[Nullable[IntType]]: ...
    @staticmethod
    @overload
    def Sum(
        source: IEnumerable[NullableType[Nullable[LongType]]],
    ) -> NullableType[Nullable[LongType]]: ...
    @staticmethod
    @overload
    def Sum(
        source: IEnumerable[NullableType[Nullable[FloatType]]],
    ) -> NullableType[Nullable[FloatType]]: ...
    @staticmethod
    @overload
    def Sum(
        source: IEnumerable[NullableType[Nullable[DoubleType]]],
    ) -> NullableType[Nullable[DoubleType]]: ...
    @staticmethod
    @overload
    def Sum(
        source: IEnumerable[NullableType[Nullable[DecimalType]]],
    ) -> NullableType[Nullable[DecimalType]]: ...
    @staticmethod
    @overload
    def Sum(source: IEnumerable[TSource], selector: Func[TSource, IntType]) -> IntType: ...
    @staticmethod
    @overload
    def Sum(
        source: IEnumerable[TSource], selector: Func[TSource, NullableType[Nullable[IntType]]]
    ) -> NullableType[Nullable[IntType]]: ...
    @staticmethod
    @overload
    def Sum(source: IEnumerable[TSource], selector: Func[TSource, LongType]) -> LongType: ...
    @staticmethod
    @overload
    def Sum(
        source: IEnumerable[TSource], selector: Func[TSource, NullableType[Nullable[LongType]]]
    ) -> NullableType[Nullable[LongType]]: ...
    @staticmethod
    @overload
    def Sum(source: IEnumerable[TSource], selector: Func[TSource, FloatType]) -> FloatType: ...
    @staticmethod
    @overload
    def Sum(
        source: IEnumerable[TSource], selector: Func[TSource, NullableType[Nullable[FloatType]]]
    ) -> NullableType[Nullable[FloatType]]: ...
    @staticmethod
    @overload
    def Sum(source: IEnumerable[TSource], selector: Func[TSource, DoubleType]) -> DoubleType: ...
    @staticmethod
    @overload
    def Sum(
        source: IEnumerable[TSource], selector: Func[TSource, NullableType[Nullable[DoubleType]]]
    ) -> NullableType[Nullable[DoubleType]]: ...
    @staticmethod
    @overload
    def Sum(source: IEnumerable[TSource], selector: Func[TSource, DecimalType]) -> DecimalType: ...
    @staticmethod
    @overload
    def Sum(
        source: IEnumerable[TSource], selector: Func[TSource, NullableType[Nullable[DecimalType]]]
    ) -> NullableType[Nullable[DecimalType]]: ...
    @staticmethod
    def Take(source: IEnumerable[TSource], count: IntType) -> IEnumerable[TSource]: ...
    @staticmethod
    @overload
    def TakeWhile(
        source: IEnumerable[TSource], predicate: Func[TSource, BooleanType]
    ) -> IEnumerable[TSource]: ...
    @staticmethod
    @overload
    def TakeWhile(
        source: IEnumerable[TSource], predicate: Func[TSource, IntType, BooleanType]
    ) -> IEnumerable[TSource]: ...
    @staticmethod
    @overload
    def ThenBy(
        source: IOrderedEnumerable[TSource], keySelector: Func[TSource, TKey]
    ) -> IOrderedEnumerable[TSource]: ...
    @staticmethod
    @overload
    def ThenBy(
        source: IOrderedEnumerable[TSource],
        keySelector: Func[TSource, TKey],
        comparer: IComparer[TKey],
    ) -> IOrderedEnumerable[TSource]: ...
    @staticmethod
    @overload
    def ThenByDescending(
        source: IOrderedEnumerable[TSource], keySelector: Func[TSource, TKey]
    ) -> IOrderedEnumerable[TSource]: ...
    @staticmethod
    @overload
    def ThenByDescending(
        source: IOrderedEnumerable[TSource],
        keySelector: Func[TSource, TKey],
        comparer: IComparer[TKey],
    ) -> IOrderedEnumerable[TSource]: ...
    @staticmethod
    def ToArray(source: IEnumerable[TSource]) -> ArrayType[TSource]: ...
    @staticmethod
    @overload
    def ToDictionary(
        source: IEnumerable[TSource], keySelector: Func[TSource, TKey]
    ) -> Dictionary[TKey, TSource]: ...
    @staticmethod
    @overload
    def ToDictionary(
        source: IEnumerable[TSource],
        keySelector: Func[TSource, TKey],
        comparer: IEqualityComparer[TKey],
    ) -> Dictionary[TKey, TSource]: ...
    @staticmethod
    @overload
    def ToDictionary(
        source: IEnumerable[TSource],
        keySelector: Func[TSource, TKey],
        elementSelector: Func[TSource, TElement],
    ) -> Dictionary[TKey, TElement]: ...
    @staticmethod
    @overload
    def ToDictionary(
        source: IEnumerable[TSource],
        keySelector: Func[TSource, TKey],
        elementSelector: Func[TSource, TElement],
        comparer: IEqualityComparer[TKey],
    ) -> Dictionary[TKey, TElement]: ...
    @staticmethod
    @overload
    def ToHashSet(source: IEnumerable[TSource]) -> HashSet[TSource]: ...
    @staticmethod
    @overload
    def ToHashSet(
        source: IEnumerable[TSource], comparer: IEqualityComparer[TSource]
    ) -> HashSet[TSource]: ...
    @staticmethod
    def ToList(source: IEnumerable[TSource]) -> List[TSource]: ...
    @staticmethod
    @overload
    def ToLookup(
        source: IEnumerable[TSource], keySelector: Func[TSource, TKey]
    ) -> ILookup[TKey, TSource]: ...
    @staticmethod
    @overload
    def ToLookup(
        source: IEnumerable[TSource],
        keySelector: Func[TSource, TKey],
        comparer: IEqualityComparer[TKey],
    ) -> ILookup[TKey, TSource]: ...
    @staticmethod
    @overload
    def ToLookup(
        source: IEnumerable[TSource],
        keySelector: Func[TSource, TKey],
        elementSelector: Func[TSource, TElement],
    ) -> ILookup[TKey, TElement]: ...
    @staticmethod
    @overload
    def ToLookup(
        source: IEnumerable[TSource],
        keySelector: Func[TSource, TKey],
        elementSelector: Func[TSource, TElement],
        comparer: IEqualityComparer[TKey],
    ) -> ILookup[TKey, TElement]: ...
    @staticmethod
    @overload
    def Union(
        first: IEnumerable[TSource], second: IEnumerable[TSource]
    ) -> IEnumerable[TSource]: ...
    @staticmethod
    @overload
    def Union(
        first: IEnumerable[TSource],
        second: IEnumerable[TSource],
        comparer: IEqualityComparer[TSource],
    ) -> IEnumerable[TSource]: ...
    @staticmethod
    @overload
    def Where(
        source: IEnumerable[TSource], predicate: Func[TSource, BooleanType]
    ) -> IEnumerable[TSource]: ...
    @staticmethod
    @overload
    def Where(
        source: IEnumerable[TSource], predicate: Func[TSource, IntType, BooleanType]
    ) -> IEnumerable[TSource]: ...
    @staticmethod
    def Zip(
        first: IEnumerable[TFirst],
        second: IEnumerable[TSecond],
        resultSelector: Func[TFirst, TSecond, TResult],
    ) -> IEnumerable[TResult]: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class EnumerableExecutor(Generic[T], EnumerableExecutor):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, expression: Expression): ...

    # No Properties

    # No Methods

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class EnumerableExecutor(ABC, ObjectType):
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

class EnumerableQuery(
    Generic[T],
    EnumerableQuery,
    IOrderedQueryable[T],
    IQueryable[T],
    IEnumerable[T],
    IEnumerable,
    IQueryable,
    IOrderedQueryable,
    IQueryProvider,
):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self, enumerable: IEnumerable[T]): ...
    @overload
    def __init__(self, expression: Expression): ...

    # No Properties

    # ---------- Methods ---------- #

    def ToString(self) -> StringType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class EnumerableQuery(ABC, ObjectType):
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

class EnumerableRewriter(OldExpressionVisitor):
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

class EnumerableSorter(Protocol[TElement], ObjectType):
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

class EnumerableSorter(Generic[TElement, TKey], EnumerableSorter[TElement]):
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

class Error(ABC, ObjectType):
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

class GroupedEnumerable(
    Generic[TSource, TKey, TElement],
    ObjectType,
    IEnumerable[IGrouping[TKey, TElement]],
    IEnumerable,
):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(
        self,
        source: IEnumerable[TSource],
        keySelector: Func[TSource, TKey],
        elementSelector: Func[TSource, TElement],
        comparer: IEqualityComparer[TKey],
    ): ...

    # No Properties

    # ---------- Methods ---------- #

    def GetEnumerator(self) -> IEnumerator[IGrouping[TKey, TElement]]: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class GroupedEnumerable(
    Generic[TSource, TKey, TElement, TResult], ObjectType, IEnumerable[TResult], IEnumerable
):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(
        self,
        source: IEnumerable[TSource],
        keySelector: Func[TSource, TKey],
        elementSelector: Func[TSource, TElement],
        resultSelector: Func[TKey, IEnumerable[TElement], TResult],
        comparer: IEqualityComparer[TKey],
    ): ...

    # No Properties

    # ---------- Methods ---------- #

    def GetEnumerator(self) -> IEnumerator[TResult]: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class IdentityFunction(Generic[TElement], ObjectType):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # ---------- Properties ---------- #

    @staticmethod
    @property
    def Instance() -> Func[TElement, TElement]: ...

    # ---------- Methods ---------- #

    @staticmethod
    def get_Instance() -> Func[TElement, TElement]: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class Lookup(
    Generic[TKey, TElement],
    ObjectType,
    IEnumerable[IGrouping[TKey, TElement]],
    IEnumerable,
    ILookup[TKey, TElement],
):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def Count(self) -> IntType: ...
    def __getitem__(self, key: TKey) -> IEnumerable[TElement]: ...

    # ---------- Methods ---------- #

    def ApplyResultSelector(
        self, resultSelector: Func[TKey, IEnumerable[TElement], TResult]
    ) -> IEnumerable[TResult]: ...
    def Contains(self, key: TKey) -> BooleanType: ...
    def GetEnumerator(self) -> IEnumerator[IGrouping[TKey, TElement]]: ...
    def get_Count(self) -> IntType: ...
    def get_Item(self, key: TKey) -> IEnumerable[TElement]: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class OrderedEnumerable(
    Protocol[TElement], ObjectType, IOrderedEnumerable[TElement], IEnumerable[TElement], IEnumerable
):
    # No Fields

    # No Constructors

    # No Properties

    # ---------- Methods ---------- #

    def GetEnumerator(self) -> IEnumerator[TElement]: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class OrderedEnumerable(
    Generic[TElement, TKey],
    OrderedEnumerable[TElement],
    IOrderedEnumerable[TElement],
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

class OrderedParallelQuery(
    Generic[TSource], ParallelQuery[TSource], IEnumerable, IEnumerable[TSource]
):
    # No Fields

    # No Constructors

    # No Properties

    # ---------- Methods ---------- #

    def GetEnumerator(self) -> IEnumerator[TSource]: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ParallelEnumerable(ABC, ObjectType):
    # No Fields

    # No Constructors

    # No Properties

    # ---------- Methods ---------- #

    @staticmethod
    @overload
    def Aggregate(
        source: ParallelQuery[TSource], func: Func[TSource, TSource, TSource]
    ) -> TSource: ...
    @staticmethod
    @overload
    def Aggregate(
        source: ParallelQuery[TSource],
        seed: TAccumulate,
        func: Func[TAccumulate, TSource, TAccumulate],
    ) -> TAccumulate: ...
    @staticmethod
    @overload
    def Aggregate(
        source: ParallelQuery[TSource],
        seed: TAccumulate,
        func: Func[TAccumulate, TSource, TAccumulate],
        resultSelector: Func[TAccumulate, TResult],
    ) -> TResult: ...
    @staticmethod
    @overload
    def Aggregate(
        source: ParallelQuery[TSource],
        seed: TAccumulate,
        updateAccumulatorFunc: Func[TAccumulate, TSource, TAccumulate],
        combineAccumulatorsFunc: Func[TAccumulate, TAccumulate, TAccumulate],
        resultSelector: Func[TAccumulate, TResult],
    ) -> TResult: ...
    @staticmethod
    @overload
    def Aggregate(
        source: ParallelQuery[TSource],
        seedFactory: Func[TAccumulate],
        updateAccumulatorFunc: Func[TAccumulate, TSource, TAccumulate],
        combineAccumulatorsFunc: Func[TAccumulate, TAccumulate, TAccumulate],
        resultSelector: Func[TAccumulate, TResult],
    ) -> TResult: ...
    @staticmethod
    def All(
        source: ParallelQuery[TSource], predicate: Func[TSource, BooleanType]
    ) -> BooleanType: ...
    @staticmethod
    @overload
    def Any(
        source: ParallelQuery[TSource], predicate: Func[TSource, BooleanType]
    ) -> BooleanType: ...
    @staticmethod
    @overload
    def Any(source: ParallelQuery[TSource]) -> BooleanType: ...
    @staticmethod
    def AsEnumerable(source: ParallelQuery[TSource]) -> IEnumerable[TSource]: ...
    @staticmethod
    @overload
    def AsOrdered(source: ParallelQuery[TSource]) -> ParallelQuery[TSource]: ...
    @staticmethod
    @overload
    def AsOrdered(source: ParallelQuery) -> ParallelQuery: ...
    @staticmethod
    @overload
    def AsParallel(source: IEnumerable[TSource]) -> ParallelQuery[TSource]: ...
    @staticmethod
    @overload
    def AsParallel(source: Partitioner[TSource]) -> ParallelQuery[TSource]: ...
    @staticmethod
    @overload
    def AsParallel(source: IEnumerable) -> ParallelQuery: ...
    @staticmethod
    def AsSequential(source: ParallelQuery[TSource]) -> IEnumerable[TSource]: ...
    @staticmethod
    def AsUnordered(source: ParallelQuery[TSource]) -> ParallelQuery[TSource]: ...
    @staticmethod
    @overload
    def Average(source: ParallelQuery[IntType]) -> DoubleType: ...
    @staticmethod
    @overload
    def Average(
        source: ParallelQuery[NullableType[Nullable[IntType]]],
    ) -> NullableType[Nullable[DoubleType]]: ...
    @staticmethod
    @overload
    def Average(source: ParallelQuery[LongType]) -> DoubleType: ...
    @staticmethod
    @overload
    def Average(
        source: ParallelQuery[NullableType[Nullable[LongType]]],
    ) -> NullableType[Nullable[DoubleType]]: ...
    @staticmethod
    @overload
    def Average(source: ParallelQuery[FloatType]) -> FloatType: ...
    @staticmethod
    @overload
    def Average(
        source: ParallelQuery[NullableType[Nullable[FloatType]]],
    ) -> NullableType[Nullable[FloatType]]: ...
    @staticmethod
    @overload
    def Average(source: ParallelQuery[DoubleType]) -> DoubleType: ...
    @staticmethod
    @overload
    def Average(
        source: ParallelQuery[NullableType[Nullable[DoubleType]]],
    ) -> NullableType[Nullable[DoubleType]]: ...
    @staticmethod
    @overload
    def Average(source: ParallelQuery[DecimalType]) -> DecimalType: ...
    @staticmethod
    @overload
    def Average(
        source: ParallelQuery[NullableType[Nullable[DecimalType]]],
    ) -> NullableType[Nullable[DecimalType]]: ...
    @staticmethod
    @overload
    def Average(source: ParallelQuery[TSource], selector: Func[TSource, IntType]) -> DoubleType: ...
    @staticmethod
    @overload
    def Average(
        source: ParallelQuery[TSource], selector: Func[TSource, NullableType[Nullable[IntType]]]
    ) -> NullableType[Nullable[DoubleType]]: ...
    @staticmethod
    @overload
    def Average(
        source: ParallelQuery[TSource], selector: Func[TSource, LongType]
    ) -> DoubleType: ...
    @staticmethod
    @overload
    def Average(
        source: ParallelQuery[TSource], selector: Func[TSource, NullableType[Nullable[LongType]]]
    ) -> NullableType[Nullable[DoubleType]]: ...
    @staticmethod
    @overload
    def Average(
        source: ParallelQuery[TSource], selector: Func[TSource, FloatType]
    ) -> FloatType: ...
    @staticmethod
    @overload
    def Average(
        source: ParallelQuery[TSource], selector: Func[TSource, NullableType[Nullable[FloatType]]]
    ) -> NullableType[Nullable[FloatType]]: ...
    @staticmethod
    @overload
    def Average(
        source: ParallelQuery[TSource], selector: Func[TSource, DoubleType]
    ) -> DoubleType: ...
    @staticmethod
    @overload
    def Average(
        source: ParallelQuery[TSource], selector: Func[TSource, NullableType[Nullable[DoubleType]]]
    ) -> NullableType[Nullable[DoubleType]]: ...
    @staticmethod
    @overload
    def Average(
        source: ParallelQuery[TSource], selector: Func[TSource, DecimalType]
    ) -> DecimalType: ...
    @staticmethod
    @overload
    def Average(
        source: ParallelQuery[TSource], selector: Func[TSource, NullableType[Nullable[DecimalType]]]
    ) -> NullableType[Nullable[DecimalType]]: ...
    @staticmethod
    def Cast(source: ParallelQuery) -> ParallelQuery[TResult]: ...
    @staticmethod
    @overload
    def Concat(
        first: ParallelQuery[TSource], second: ParallelQuery[TSource]
    ) -> ParallelQuery[TSource]: ...
    @staticmethod
    @overload
    def Concat(
        first: ParallelQuery[TSource], second: IEnumerable[TSource]
    ) -> ParallelQuery[TSource]: ...
    @staticmethod
    @overload
    def Contains(source: ParallelQuery[TSource], value: TSource) -> BooleanType: ...
    @staticmethod
    @overload
    def Contains(
        source: ParallelQuery[TSource], value: TSource, comparer: IEqualityComparer[TSource]
    ) -> BooleanType: ...
    @staticmethod
    @overload
    def Count(source: ParallelQuery[TSource]) -> IntType: ...
    @staticmethod
    @overload
    def Count(source: ParallelQuery[TSource], predicate: Func[TSource, BooleanType]) -> IntType: ...
    @staticmethod
    @overload
    def DefaultIfEmpty(source: ParallelQuery[TSource]) -> ParallelQuery[TSource]: ...
    @staticmethod
    @overload
    def DefaultIfEmpty(
        source: ParallelQuery[TSource], defaultValue: TSource
    ) -> ParallelQuery[TSource]: ...
    @staticmethod
    @overload
    def Distinct(source: ParallelQuery[TSource]) -> ParallelQuery[TSource]: ...
    @staticmethod
    @overload
    def Distinct(
        source: ParallelQuery[TSource], comparer: IEqualityComparer[TSource]
    ) -> ParallelQuery[TSource]: ...
    @staticmethod
    def ElementAt(source: ParallelQuery[TSource], index: IntType) -> TSource: ...
    @staticmethod
    def ElementAtOrDefault(source: ParallelQuery[TSource], index: IntType) -> TSource: ...
    @staticmethod
    def Empty() -> ParallelQuery[TResult]: ...
    @staticmethod
    @overload
    def Except(
        first: ParallelQuery[TSource], second: ParallelQuery[TSource]
    ) -> ParallelQuery[TSource]: ...
    @staticmethod
    @overload
    def Except(
        first: ParallelQuery[TSource], second: IEnumerable[TSource]
    ) -> ParallelQuery[TSource]: ...
    @staticmethod
    @overload
    def Except(
        first: ParallelQuery[TSource],
        second: ParallelQuery[TSource],
        comparer: IEqualityComparer[TSource],
    ) -> ParallelQuery[TSource]: ...
    @staticmethod
    @overload
    def Except(
        first: ParallelQuery[TSource],
        second: IEnumerable[TSource],
        comparer: IEqualityComparer[TSource],
    ) -> ParallelQuery[TSource]: ...
    @staticmethod
    @overload
    def First(source: ParallelQuery[TSource]) -> TSource: ...
    @staticmethod
    @overload
    def First(source: ParallelQuery[TSource], predicate: Func[TSource, BooleanType]) -> TSource: ...
    @staticmethod
    @overload
    def FirstOrDefault(source: ParallelQuery[TSource]) -> TSource: ...
    @staticmethod
    @overload
    def FirstOrDefault(
        source: ParallelQuery[TSource], predicate: Func[TSource, BooleanType]
    ) -> TSource: ...
    @staticmethod
    def ForAll(source: ParallelQuery[TSource], action: Action[TSource]) -> VoidType: ...
    @staticmethod
    @overload
    def GroupBy(
        source: ParallelQuery[TSource], keySelector: Func[TSource, TKey]
    ) -> ParallelQuery[IGrouping[TKey, TSource]]: ...
    @staticmethod
    @overload
    def GroupBy(
        source: ParallelQuery[TSource],
        keySelector: Func[TSource, TKey],
        comparer: IEqualityComparer[TKey],
    ) -> ParallelQuery[IGrouping[TKey, TSource]]: ...
    @staticmethod
    @overload
    def GroupBy(
        source: ParallelQuery[TSource],
        keySelector: Func[TSource, TKey],
        elementSelector: Func[TSource, TElement],
    ) -> ParallelQuery[IGrouping[TKey, TElement]]: ...
    @staticmethod
    @overload
    def GroupBy(
        source: ParallelQuery[TSource],
        keySelector: Func[TSource, TKey],
        elementSelector: Func[TSource, TElement],
        comparer: IEqualityComparer[TKey],
    ) -> ParallelQuery[IGrouping[TKey, TElement]]: ...
    @staticmethod
    @overload
    def GroupBy(
        source: ParallelQuery[TSource],
        keySelector: Func[TSource, TKey],
        resultSelector: Func[TKey, IEnumerable[TSource], TResult],
    ) -> ParallelQuery[TResult]: ...
    @staticmethod
    @overload
    def GroupBy(
        source: ParallelQuery[TSource],
        keySelector: Func[TSource, TKey],
        resultSelector: Func[TKey, IEnumerable[TSource], TResult],
        comparer: IEqualityComparer[TKey],
    ) -> ParallelQuery[TResult]: ...
    @staticmethod
    @overload
    def GroupBy(
        source: ParallelQuery[TSource],
        keySelector: Func[TSource, TKey],
        elementSelector: Func[TSource, TElement],
        resultSelector: Func[TKey, IEnumerable[TElement], TResult],
    ) -> ParallelQuery[TResult]: ...
    @staticmethod
    @overload
    def GroupBy(
        source: ParallelQuery[TSource],
        keySelector: Func[TSource, TKey],
        elementSelector: Func[TSource, TElement],
        resultSelector: Func[TKey, IEnumerable[TElement], TResult],
        comparer: IEqualityComparer[TKey],
    ) -> ParallelQuery[TResult]: ...
    @staticmethod
    @overload
    def GroupJoin(
        outer: ParallelQuery[TOuter],
        inner: ParallelQuery[TInner],
        outerKeySelector: Func[TOuter, TKey],
        innerKeySelector: Func[TInner, TKey],
        resultSelector: Func[TOuter, IEnumerable[TInner], TResult],
    ) -> ParallelQuery[TResult]: ...
    @staticmethod
    @overload
    def GroupJoin(
        outer: ParallelQuery[TOuter],
        inner: IEnumerable[TInner],
        outerKeySelector: Func[TOuter, TKey],
        innerKeySelector: Func[TInner, TKey],
        resultSelector: Func[TOuter, IEnumerable[TInner], TResult],
    ) -> ParallelQuery[TResult]: ...
    @staticmethod
    @overload
    def GroupJoin(
        outer: ParallelQuery[TOuter],
        inner: ParallelQuery[TInner],
        outerKeySelector: Func[TOuter, TKey],
        innerKeySelector: Func[TInner, TKey],
        resultSelector: Func[TOuter, IEnumerable[TInner], TResult],
        comparer: IEqualityComparer[TKey],
    ) -> ParallelQuery[TResult]: ...
    @staticmethod
    @overload
    def GroupJoin(
        outer: ParallelQuery[TOuter],
        inner: IEnumerable[TInner],
        outerKeySelector: Func[TOuter, TKey],
        innerKeySelector: Func[TInner, TKey],
        resultSelector: Func[TOuter, IEnumerable[TInner], TResult],
        comparer: IEqualityComparer[TKey],
    ) -> ParallelQuery[TResult]: ...
    @staticmethod
    @overload
    def Intersect(
        first: ParallelQuery[TSource], second: ParallelQuery[TSource]
    ) -> ParallelQuery[TSource]: ...
    @staticmethod
    @overload
    def Intersect(
        first: ParallelQuery[TSource], second: IEnumerable[TSource]
    ) -> ParallelQuery[TSource]: ...
    @staticmethod
    @overload
    def Intersect(
        first: ParallelQuery[TSource],
        second: ParallelQuery[TSource],
        comparer: IEqualityComparer[TSource],
    ) -> ParallelQuery[TSource]: ...
    @staticmethod
    @overload
    def Intersect(
        first: ParallelQuery[TSource],
        second: IEnumerable[TSource],
        comparer: IEqualityComparer[TSource],
    ) -> ParallelQuery[TSource]: ...
    @staticmethod
    @overload
    def Join(
        outer: ParallelQuery[TOuter],
        inner: ParallelQuery[TInner],
        outerKeySelector: Func[TOuter, TKey],
        innerKeySelector: Func[TInner, TKey],
        resultSelector: Func[TOuter, TInner, TResult],
    ) -> ParallelQuery[TResult]: ...
    @staticmethod
    @overload
    def Join(
        outer: ParallelQuery[TOuter],
        inner: IEnumerable[TInner],
        outerKeySelector: Func[TOuter, TKey],
        innerKeySelector: Func[TInner, TKey],
        resultSelector: Func[TOuter, TInner, TResult],
    ) -> ParallelQuery[TResult]: ...
    @staticmethod
    @overload
    def Join(
        outer: ParallelQuery[TOuter],
        inner: ParallelQuery[TInner],
        outerKeySelector: Func[TOuter, TKey],
        innerKeySelector: Func[TInner, TKey],
        resultSelector: Func[TOuter, TInner, TResult],
        comparer: IEqualityComparer[TKey],
    ) -> ParallelQuery[TResult]: ...
    @staticmethod
    @overload
    def Join(
        outer: ParallelQuery[TOuter],
        inner: IEnumerable[TInner],
        outerKeySelector: Func[TOuter, TKey],
        innerKeySelector: Func[TInner, TKey],
        resultSelector: Func[TOuter, TInner, TResult],
        comparer: IEqualityComparer[TKey],
    ) -> ParallelQuery[TResult]: ...
    @staticmethod
    @overload
    def Last(source: ParallelQuery[TSource]) -> TSource: ...
    @staticmethod
    @overload
    def Last(source: ParallelQuery[TSource], predicate: Func[TSource, BooleanType]) -> TSource: ...
    @staticmethod
    @overload
    def LastOrDefault(source: ParallelQuery[TSource]) -> TSource: ...
    @staticmethod
    @overload
    def LastOrDefault(
        source: ParallelQuery[TSource], predicate: Func[TSource, BooleanType]
    ) -> TSource: ...
    @staticmethod
    @overload
    def LongCount(source: ParallelQuery[TSource]) -> LongType: ...
    @staticmethod
    @overload
    def LongCount(
        source: ParallelQuery[TSource], predicate: Func[TSource, BooleanType]
    ) -> LongType: ...
    @staticmethod
    @overload
    def Max(source: ParallelQuery[IntType]) -> IntType: ...
    @staticmethod
    @overload
    def Max(
        source: ParallelQuery[NullableType[Nullable[IntType]]],
    ) -> NullableType[Nullable[IntType]]: ...
    @staticmethod
    @overload
    def Max(source: ParallelQuery[LongType]) -> LongType: ...
    @staticmethod
    @overload
    def Max(
        source: ParallelQuery[NullableType[Nullable[LongType]]],
    ) -> NullableType[Nullable[LongType]]: ...
    @staticmethod
    @overload
    def Max(source: ParallelQuery[FloatType]) -> FloatType: ...
    @staticmethod
    @overload
    def Max(
        source: ParallelQuery[NullableType[Nullable[FloatType]]],
    ) -> NullableType[Nullable[FloatType]]: ...
    @staticmethod
    @overload
    def Max(source: ParallelQuery[DoubleType]) -> DoubleType: ...
    @staticmethod
    @overload
    def Max(
        source: ParallelQuery[NullableType[Nullable[DoubleType]]],
    ) -> NullableType[Nullable[DoubleType]]: ...
    @staticmethod
    @overload
    def Max(source: ParallelQuery[DecimalType]) -> DecimalType: ...
    @staticmethod
    @overload
    def Max(
        source: ParallelQuery[NullableType[Nullable[DecimalType]]],
    ) -> NullableType[Nullable[DecimalType]]: ...
    @staticmethod
    @overload
    def Max(source: ParallelQuery[TSource]) -> TSource: ...
    @staticmethod
    @overload
    def Max(source: ParallelQuery[TSource], selector: Func[TSource, IntType]) -> IntType: ...
    @staticmethod
    @overload
    def Max(
        source: ParallelQuery[TSource], selector: Func[TSource, NullableType[Nullable[IntType]]]
    ) -> NullableType[Nullable[IntType]]: ...
    @staticmethod
    @overload
    def Max(source: ParallelQuery[TSource], selector: Func[TSource, LongType]) -> LongType: ...
    @staticmethod
    @overload
    def Max(
        source: ParallelQuery[TSource], selector: Func[TSource, NullableType[Nullable[LongType]]]
    ) -> NullableType[Nullable[LongType]]: ...
    @staticmethod
    @overload
    def Max(source: ParallelQuery[TSource], selector: Func[TSource, FloatType]) -> FloatType: ...
    @staticmethod
    @overload
    def Max(
        source: ParallelQuery[TSource], selector: Func[TSource, NullableType[Nullable[FloatType]]]
    ) -> NullableType[Nullable[FloatType]]: ...
    @staticmethod
    @overload
    def Max(source: ParallelQuery[TSource], selector: Func[TSource, DoubleType]) -> DoubleType: ...
    @staticmethod
    @overload
    def Max(
        source: ParallelQuery[TSource], selector: Func[TSource, NullableType[Nullable[DoubleType]]]
    ) -> NullableType[Nullable[DoubleType]]: ...
    @staticmethod
    @overload
    def Max(
        source: ParallelQuery[TSource], selector: Func[TSource, DecimalType]
    ) -> DecimalType: ...
    @staticmethod
    @overload
    def Max(
        source: ParallelQuery[TSource], selector: Func[TSource, NullableType[Nullable[DecimalType]]]
    ) -> NullableType[Nullable[DecimalType]]: ...
    @staticmethod
    @overload
    def Max(source: ParallelQuery[TSource], selector: Func[TSource, TResult]) -> TResult: ...
    @staticmethod
    @overload
    def Min(source: ParallelQuery[IntType]) -> IntType: ...
    @staticmethod
    @overload
    def Min(
        source: ParallelQuery[NullableType[Nullable[IntType]]],
    ) -> NullableType[Nullable[IntType]]: ...
    @staticmethod
    @overload
    def Min(source: ParallelQuery[LongType]) -> LongType: ...
    @staticmethod
    @overload
    def Min(
        source: ParallelQuery[NullableType[Nullable[LongType]]],
    ) -> NullableType[Nullable[LongType]]: ...
    @staticmethod
    @overload
    def Min(source: ParallelQuery[FloatType]) -> FloatType: ...
    @staticmethod
    @overload
    def Min(
        source: ParallelQuery[NullableType[Nullable[FloatType]]],
    ) -> NullableType[Nullable[FloatType]]: ...
    @staticmethod
    @overload
    def Min(source: ParallelQuery[DoubleType]) -> DoubleType: ...
    @staticmethod
    @overload
    def Min(
        source: ParallelQuery[NullableType[Nullable[DoubleType]]],
    ) -> NullableType[Nullable[DoubleType]]: ...
    @staticmethod
    @overload
    def Min(source: ParallelQuery[DecimalType]) -> DecimalType: ...
    @staticmethod
    @overload
    def Min(
        source: ParallelQuery[NullableType[Nullable[DecimalType]]],
    ) -> NullableType[Nullable[DecimalType]]: ...
    @staticmethod
    @overload
    def Min(source: ParallelQuery[TSource]) -> TSource: ...
    @staticmethod
    @overload
    def Min(source: ParallelQuery[TSource], selector: Func[TSource, IntType]) -> IntType: ...
    @staticmethod
    @overload
    def Min(
        source: ParallelQuery[TSource], selector: Func[TSource, NullableType[Nullable[IntType]]]
    ) -> NullableType[Nullable[IntType]]: ...
    @staticmethod
    @overload
    def Min(source: ParallelQuery[TSource], selector: Func[TSource, LongType]) -> LongType: ...
    @staticmethod
    @overload
    def Min(
        source: ParallelQuery[TSource], selector: Func[TSource, NullableType[Nullable[LongType]]]
    ) -> NullableType[Nullable[LongType]]: ...
    @staticmethod
    @overload
    def Min(source: ParallelQuery[TSource], selector: Func[TSource, FloatType]) -> FloatType: ...
    @staticmethod
    @overload
    def Min(
        source: ParallelQuery[TSource], selector: Func[TSource, NullableType[Nullable[FloatType]]]
    ) -> NullableType[Nullable[FloatType]]: ...
    @staticmethod
    @overload
    def Min(source: ParallelQuery[TSource], selector: Func[TSource, DoubleType]) -> DoubleType: ...
    @staticmethod
    @overload
    def Min(
        source: ParallelQuery[TSource], selector: Func[TSource, NullableType[Nullable[DoubleType]]]
    ) -> NullableType[Nullable[DoubleType]]: ...
    @staticmethod
    @overload
    def Min(
        source: ParallelQuery[TSource], selector: Func[TSource, DecimalType]
    ) -> DecimalType: ...
    @staticmethod
    @overload
    def Min(
        source: ParallelQuery[TSource], selector: Func[TSource, NullableType[Nullable[DecimalType]]]
    ) -> NullableType[Nullable[DecimalType]]: ...
    @staticmethod
    @overload
    def Min(source: ParallelQuery[TSource], selector: Func[TSource, TResult]) -> TResult: ...
    @staticmethod
    def OfType(source: ParallelQuery) -> ParallelQuery[TResult]: ...
    @staticmethod
    @overload
    def OrderBy(
        source: ParallelQuery[TSource], keySelector: Func[TSource, TKey]
    ) -> OrderedParallelQuery[TSource]: ...
    @staticmethod
    @overload
    def OrderBy(
        source: ParallelQuery[TSource], keySelector: Func[TSource, TKey], comparer: IComparer[TKey]
    ) -> OrderedParallelQuery[TSource]: ...
    @staticmethod
    @overload
    def OrderByDescending(
        source: ParallelQuery[TSource], keySelector: Func[TSource, TKey]
    ) -> OrderedParallelQuery[TSource]: ...
    @staticmethod
    @overload
    def OrderByDescending(
        source: ParallelQuery[TSource], keySelector: Func[TSource, TKey], comparer: IComparer[TKey]
    ) -> OrderedParallelQuery[TSource]: ...
    @staticmethod
    def Range(start: IntType, count: IntType) -> ParallelQuery[IntType]: ...
    @staticmethod
    def Repeat(element: TResult, count: IntType) -> ParallelQuery[TResult]: ...
    @staticmethod
    def Reverse(source: ParallelQuery[TSource]) -> ParallelQuery[TSource]: ...
    @staticmethod
    @overload
    def Select(
        source: ParallelQuery[TSource], selector: Func[TSource, TResult]
    ) -> ParallelQuery[TResult]: ...
    @staticmethod
    @overload
    def Select(
        source: ParallelQuery[TSource], selector: Func[TSource, IntType, TResult]
    ) -> ParallelQuery[TResult]: ...
    @staticmethod
    @overload
    def SelectMany(
        source: ParallelQuery[TSource], selector: Func[TSource, IEnumerable[TResult]]
    ) -> ParallelQuery[TResult]: ...
    @staticmethod
    @overload
    def SelectMany(
        source: ParallelQuery[TSource], selector: Func[TSource, IntType, IEnumerable[TResult]]
    ) -> ParallelQuery[TResult]: ...
    @staticmethod
    @overload
    def SelectMany(
        source: ParallelQuery[TSource],
        collectionSelector: Func[TSource, IEnumerable[TCollection]],
        resultSelector: Func[TSource, TCollection, TResult],
    ) -> ParallelQuery[TResult]: ...
    @staticmethod
    @overload
    def SelectMany(
        source: ParallelQuery[TSource],
        collectionSelector: Func[TSource, IntType, IEnumerable[TCollection]],
        resultSelector: Func[TSource, TCollection, TResult],
    ) -> ParallelQuery[TResult]: ...
    @staticmethod
    @overload
    def SequenceEqual(
        first: ParallelQuery[TSource], second: ParallelQuery[TSource]
    ) -> BooleanType: ...
    @staticmethod
    @overload
    def SequenceEqual(
        first: ParallelQuery[TSource], second: IEnumerable[TSource]
    ) -> BooleanType: ...
    @staticmethod
    @overload
    def SequenceEqual(
        first: ParallelQuery[TSource],
        second: ParallelQuery[TSource],
        comparer: IEqualityComparer[TSource],
    ) -> BooleanType: ...
    @staticmethod
    @overload
    def SequenceEqual(
        first: ParallelQuery[TSource],
        second: IEnumerable[TSource],
        comparer: IEqualityComparer[TSource],
    ) -> BooleanType: ...
    @staticmethod
    @overload
    def Single(source: ParallelQuery[TSource]) -> TSource: ...
    @staticmethod
    @overload
    def Single(
        source: ParallelQuery[TSource], predicate: Func[TSource, BooleanType]
    ) -> TSource: ...
    @staticmethod
    @overload
    def SingleOrDefault(source: ParallelQuery[TSource]) -> TSource: ...
    @staticmethod
    @overload
    def SingleOrDefault(
        source: ParallelQuery[TSource], predicate: Func[TSource, BooleanType]
    ) -> TSource: ...
    @staticmethod
    def Skip(source: ParallelQuery[TSource], count: IntType) -> ParallelQuery[TSource]: ...
    @staticmethod
    @overload
    def SkipWhile(
        source: ParallelQuery[TSource], predicate: Func[TSource, BooleanType]
    ) -> ParallelQuery[TSource]: ...
    @staticmethod
    @overload
    def SkipWhile(
        source: ParallelQuery[TSource], predicate: Func[TSource, IntType, BooleanType]
    ) -> ParallelQuery[TSource]: ...
    @staticmethod
    @overload
    def Sum(source: ParallelQuery[IntType]) -> IntType: ...
    @staticmethod
    @overload
    def Sum(
        source: ParallelQuery[NullableType[Nullable[IntType]]],
    ) -> NullableType[Nullable[IntType]]: ...
    @staticmethod
    @overload
    def Sum(source: ParallelQuery[LongType]) -> LongType: ...
    @staticmethod
    @overload
    def Sum(
        source: ParallelQuery[NullableType[Nullable[LongType]]],
    ) -> NullableType[Nullable[LongType]]: ...
    @staticmethod
    @overload
    def Sum(source: ParallelQuery[FloatType]) -> FloatType: ...
    @staticmethod
    @overload
    def Sum(
        source: ParallelQuery[NullableType[Nullable[FloatType]]],
    ) -> NullableType[Nullable[FloatType]]: ...
    @staticmethod
    @overload
    def Sum(source: ParallelQuery[DoubleType]) -> DoubleType: ...
    @staticmethod
    @overload
    def Sum(
        source: ParallelQuery[NullableType[Nullable[DoubleType]]],
    ) -> NullableType[Nullable[DoubleType]]: ...
    @staticmethod
    @overload
    def Sum(source: ParallelQuery[DecimalType]) -> DecimalType: ...
    @staticmethod
    @overload
    def Sum(
        source: ParallelQuery[NullableType[Nullable[DecimalType]]],
    ) -> NullableType[Nullable[DecimalType]]: ...
    @staticmethod
    @overload
    def Sum(source: ParallelQuery[TSource], selector: Func[TSource, IntType]) -> IntType: ...
    @staticmethod
    @overload
    def Sum(
        source: ParallelQuery[TSource], selector: Func[TSource, NullableType[Nullable[IntType]]]
    ) -> NullableType[Nullable[IntType]]: ...
    @staticmethod
    @overload
    def Sum(source: ParallelQuery[TSource], selector: Func[TSource, LongType]) -> LongType: ...
    @staticmethod
    @overload
    def Sum(
        source: ParallelQuery[TSource], selector: Func[TSource, NullableType[Nullable[LongType]]]
    ) -> NullableType[Nullable[LongType]]: ...
    @staticmethod
    @overload
    def Sum(source: ParallelQuery[TSource], selector: Func[TSource, FloatType]) -> FloatType: ...
    @staticmethod
    @overload
    def Sum(
        source: ParallelQuery[TSource], selector: Func[TSource, NullableType[Nullable[FloatType]]]
    ) -> NullableType[Nullable[FloatType]]: ...
    @staticmethod
    @overload
    def Sum(source: ParallelQuery[TSource], selector: Func[TSource, DoubleType]) -> DoubleType: ...
    @staticmethod
    @overload
    def Sum(
        source: ParallelQuery[TSource], selector: Func[TSource, NullableType[Nullable[DoubleType]]]
    ) -> NullableType[Nullable[DoubleType]]: ...
    @staticmethod
    @overload
    def Sum(
        source: ParallelQuery[TSource], selector: Func[TSource, DecimalType]
    ) -> DecimalType: ...
    @staticmethod
    @overload
    def Sum(
        source: ParallelQuery[TSource], selector: Func[TSource, NullableType[Nullable[DecimalType]]]
    ) -> NullableType[Nullable[DecimalType]]: ...
    @staticmethod
    def Take(source: ParallelQuery[TSource], count: IntType) -> ParallelQuery[TSource]: ...
    @staticmethod
    @overload
    def TakeWhile(
        source: ParallelQuery[TSource], predicate: Func[TSource, BooleanType]
    ) -> ParallelQuery[TSource]: ...
    @staticmethod
    @overload
    def TakeWhile(
        source: ParallelQuery[TSource], predicate: Func[TSource, IntType, BooleanType]
    ) -> ParallelQuery[TSource]: ...
    @staticmethod
    @overload
    def ThenBy(
        source: OrderedParallelQuery[TSource], keySelector: Func[TSource, TKey]
    ) -> OrderedParallelQuery[TSource]: ...
    @staticmethod
    @overload
    def ThenBy(
        source: OrderedParallelQuery[TSource],
        keySelector: Func[TSource, TKey],
        comparer: IComparer[TKey],
    ) -> OrderedParallelQuery[TSource]: ...
    @staticmethod
    @overload
    def ThenByDescending(
        source: OrderedParallelQuery[TSource], keySelector: Func[TSource, TKey]
    ) -> OrderedParallelQuery[TSource]: ...
    @staticmethod
    @overload
    def ThenByDescending(
        source: OrderedParallelQuery[TSource],
        keySelector: Func[TSource, TKey],
        comparer: IComparer[TKey],
    ) -> OrderedParallelQuery[TSource]: ...
    @staticmethod
    def ToArray(source: ParallelQuery[TSource]) -> ArrayType[TSource]: ...
    @staticmethod
    @overload
    def ToDictionary(
        source: ParallelQuery[TSource], keySelector: Func[TSource, TKey]
    ) -> Dictionary[TKey, TSource]: ...
    @staticmethod
    @overload
    def ToDictionary(
        source: ParallelQuery[TSource],
        keySelector: Func[TSource, TKey],
        comparer: IEqualityComparer[TKey],
    ) -> Dictionary[TKey, TSource]: ...
    @staticmethod
    @overload
    def ToDictionary(
        source: ParallelQuery[TSource],
        keySelector: Func[TSource, TKey],
        elementSelector: Func[TSource, TElement],
    ) -> Dictionary[TKey, TElement]: ...
    @staticmethod
    @overload
    def ToDictionary(
        source: ParallelQuery[TSource],
        keySelector: Func[TSource, TKey],
        elementSelector: Func[TSource, TElement],
        comparer: IEqualityComparer[TKey],
    ) -> Dictionary[TKey, TElement]: ...
    @staticmethod
    def ToList(source: ParallelQuery[TSource]) -> List[TSource]: ...
    @staticmethod
    @overload
    def ToLookup(
        source: ParallelQuery[TSource], keySelector: Func[TSource, TKey]
    ) -> ILookup[TKey, TSource]: ...
    @staticmethod
    @overload
    def ToLookup(
        source: ParallelQuery[TSource],
        keySelector: Func[TSource, TKey],
        comparer: IEqualityComparer[TKey],
    ) -> ILookup[TKey, TSource]: ...
    @staticmethod
    @overload
    def ToLookup(
        source: ParallelQuery[TSource],
        keySelector: Func[TSource, TKey],
        elementSelector: Func[TSource, TElement],
    ) -> ILookup[TKey, TElement]: ...
    @staticmethod
    @overload
    def ToLookup(
        source: ParallelQuery[TSource],
        keySelector: Func[TSource, TKey],
        elementSelector: Func[TSource, TElement],
        comparer: IEqualityComparer[TKey],
    ) -> ILookup[TKey, TElement]: ...
    @staticmethod
    @overload
    def Union(
        first: ParallelQuery[TSource], second: ParallelQuery[TSource]
    ) -> ParallelQuery[TSource]: ...
    @staticmethod
    @overload
    def Union(
        first: ParallelQuery[TSource], second: IEnumerable[TSource]
    ) -> ParallelQuery[TSource]: ...
    @staticmethod
    @overload
    def Union(
        first: ParallelQuery[TSource],
        second: ParallelQuery[TSource],
        comparer: IEqualityComparer[TSource],
    ) -> ParallelQuery[TSource]: ...
    @staticmethod
    @overload
    def Union(
        first: ParallelQuery[TSource],
        second: IEnumerable[TSource],
        comparer: IEqualityComparer[TSource],
    ) -> ParallelQuery[TSource]: ...
    @staticmethod
    @overload
    def Where(
        source: ParallelQuery[TSource], predicate: Func[TSource, BooleanType]
    ) -> ParallelQuery[TSource]: ...
    @staticmethod
    @overload
    def Where(
        source: ParallelQuery[TSource], predicate: Func[TSource, IntType, BooleanType]
    ) -> ParallelQuery[TSource]: ...
    @staticmethod
    def WithCancellation(
        source: ParallelQuery[TSource], cancellationToken: CancellationToken
    ) -> ParallelQuery[TSource]: ...
    @staticmethod
    def WithDegreeOfParallelism(
        source: ParallelQuery[TSource], degreeOfParallelism: IntType
    ) -> ParallelQuery[TSource]: ...
    @staticmethod
    def WithExecutionMode(
        source: ParallelQuery[TSource], executionMode: ParallelExecutionMode
    ) -> ParallelQuery[TSource]: ...
    @staticmethod
    def WithMergeOptions(
        source: ParallelQuery[TSource], mergeOptions: ParallelMergeOptions
    ) -> ParallelQuery[TSource]: ...
    @staticmethod
    @overload
    def Zip(
        first: ParallelQuery[TFirst],
        second: ParallelQuery[TSecond],
        resultSelector: Func[TFirst, TSecond, TResult],
    ) -> ParallelQuery[TResult]: ...
    @staticmethod
    @overload
    def Zip(
        first: ParallelQuery[TFirst],
        second: IEnumerable[TSecond],
        resultSelector: Func[TFirst, TSecond, TResult],
    ) -> ParallelQuery[TResult]: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ParallelQuery(ObjectType, IEnumerable):
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

class ParallelQuery(Generic[TSource], ParallelQuery, IEnumerable, IEnumerable[TSource]):
    # No Fields

    # No Constructors

    # No Properties

    # ---------- Methods ---------- #

    def GetEnumerator(self) -> IEnumerator[TSource]: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class Queryable(ABC, ObjectType):
    # No Fields

    # No Constructors

    # No Properties

    # ---------- Methods ---------- #

    @staticmethod
    @overload
    def Aggregate(
        source: IQueryable[TSource], func: Expression[Func[TSource, TSource, TSource]]
    ) -> TSource: ...
    @staticmethod
    @overload
    def Aggregate(
        source: IQueryable[TSource],
        seed: TAccumulate,
        func: Expression[Func[TAccumulate, TSource, TAccumulate]],
    ) -> TAccumulate: ...
    @staticmethod
    @overload
    def Aggregate(
        source: IQueryable[TSource],
        seed: TAccumulate,
        func: Expression[Func[TAccumulate, TSource, TAccumulate]],
        selector: Expression[Func[TAccumulate, TResult]],
    ) -> TResult: ...
    @staticmethod
    def All(
        source: IQueryable[TSource], predicate: Expression[Func[TSource, BooleanType]]
    ) -> BooleanType: ...
    @staticmethod
    @overload
    def Any(source: IQueryable[TSource]) -> BooleanType: ...
    @staticmethod
    @overload
    def Any(
        source: IQueryable[TSource], predicate: Expression[Func[TSource, BooleanType]]
    ) -> BooleanType: ...
    @staticmethod
    @overload
    def AsQueryable(source: IEnumerable) -> IQueryable: ...
    @staticmethod
    @overload
    def AsQueryable(source: IEnumerable[TElement]) -> IQueryable[TElement]: ...
    @staticmethod
    @overload
    def Average(source: IQueryable[IntType]) -> DoubleType: ...
    @staticmethod
    @overload
    def Average(
        source: IQueryable[NullableType[Nullable[IntType]]],
    ) -> NullableType[Nullable[DoubleType]]: ...
    @staticmethod
    @overload
    def Average(source: IQueryable[LongType]) -> DoubleType: ...
    @staticmethod
    @overload
    def Average(
        source: IQueryable[NullableType[Nullable[LongType]]],
    ) -> NullableType[Nullable[DoubleType]]: ...
    @staticmethod
    @overload
    def Average(source: IQueryable[FloatType]) -> FloatType: ...
    @staticmethod
    @overload
    def Average(
        source: IQueryable[NullableType[Nullable[FloatType]]],
    ) -> NullableType[Nullable[FloatType]]: ...
    @staticmethod
    @overload
    def Average(source: IQueryable[DoubleType]) -> DoubleType: ...
    @staticmethod
    @overload
    def Average(
        source: IQueryable[NullableType[Nullable[DoubleType]]],
    ) -> NullableType[Nullable[DoubleType]]: ...
    @staticmethod
    @overload
    def Average(source: IQueryable[DecimalType]) -> DecimalType: ...
    @staticmethod
    @overload
    def Average(
        source: IQueryable[NullableType[Nullable[DecimalType]]],
    ) -> NullableType[Nullable[DecimalType]]: ...
    @staticmethod
    @overload
    def Average(
        source: IQueryable[TSource], selector: Expression[Func[TSource, IntType]]
    ) -> DoubleType: ...
    @staticmethod
    @overload
    def Average(
        source: IQueryable[TSource],
        selector: Expression[Func[TSource, NullableType[Nullable[IntType]]]],
    ) -> NullableType[Nullable[DoubleType]]: ...
    @staticmethod
    @overload
    def Average(
        source: IQueryable[TSource], selector: Expression[Func[TSource, FloatType]]
    ) -> FloatType: ...
    @staticmethod
    @overload
    def Average(
        source: IQueryable[TSource],
        selector: Expression[Func[TSource, NullableType[Nullable[FloatType]]]],
    ) -> NullableType[Nullable[FloatType]]: ...
    @staticmethod
    @overload
    def Average(
        source: IQueryable[TSource], selector: Expression[Func[TSource, LongType]]
    ) -> DoubleType: ...
    @staticmethod
    @overload
    def Average(
        source: IQueryable[TSource],
        selector: Expression[Func[TSource, NullableType[Nullable[LongType]]]],
    ) -> NullableType[Nullable[DoubleType]]: ...
    @staticmethod
    @overload
    def Average(
        source: IQueryable[TSource], selector: Expression[Func[TSource, DoubleType]]
    ) -> DoubleType: ...
    @staticmethod
    @overload
    def Average(
        source: IQueryable[TSource],
        selector: Expression[Func[TSource, NullableType[Nullable[DoubleType]]]],
    ) -> NullableType[Nullable[DoubleType]]: ...
    @staticmethod
    @overload
    def Average(
        source: IQueryable[TSource], selector: Expression[Func[TSource, DecimalType]]
    ) -> DecimalType: ...
    @staticmethod
    @overload
    def Average(
        source: IQueryable[TSource],
        selector: Expression[Func[TSource, NullableType[Nullable[DecimalType]]]],
    ) -> NullableType[Nullable[DecimalType]]: ...
    @staticmethod
    def Cast(source: IQueryable) -> IQueryable[TResult]: ...
    @staticmethod
    def Concat(
        source1: IQueryable[TSource], source2: IEnumerable[TSource]
    ) -> IQueryable[TSource]: ...
    @staticmethod
    @overload
    def Contains(source: IQueryable[TSource], item: TSource) -> BooleanType: ...
    @staticmethod
    @overload
    def Contains(
        source: IQueryable[TSource], item: TSource, comparer: IEqualityComparer[TSource]
    ) -> BooleanType: ...
    @staticmethod
    @overload
    def Count(source: IQueryable[TSource]) -> IntType: ...
    @staticmethod
    @overload
    def Count(
        source: IQueryable[TSource], predicate: Expression[Func[TSource, BooleanType]]
    ) -> IntType: ...
    @staticmethod
    @overload
    def DefaultIfEmpty(source: IQueryable[TSource]) -> IQueryable[TSource]: ...
    @staticmethod
    @overload
    def DefaultIfEmpty(
        source: IQueryable[TSource], defaultValue: TSource
    ) -> IQueryable[TSource]: ...
    @staticmethod
    @overload
    def Distinct(source: IQueryable[TSource]) -> IQueryable[TSource]: ...
    @staticmethod
    @overload
    def Distinct(
        source: IQueryable[TSource], comparer: IEqualityComparer[TSource]
    ) -> IQueryable[TSource]: ...
    @staticmethod
    def ElementAt(source: IQueryable[TSource], index: IntType) -> TSource: ...
    @staticmethod
    def ElementAtOrDefault(source: IQueryable[TSource], index: IntType) -> TSource: ...
    @staticmethod
    @overload
    def Except(
        source1: IQueryable[TSource], source2: IEnumerable[TSource]
    ) -> IQueryable[TSource]: ...
    @staticmethod
    @overload
    def Except(
        source1: IQueryable[TSource],
        source2: IEnumerable[TSource],
        comparer: IEqualityComparer[TSource],
    ) -> IQueryable[TSource]: ...
    @staticmethod
    @overload
    def First(source: IQueryable[TSource]) -> TSource: ...
    @staticmethod
    @overload
    def First(
        source: IQueryable[TSource], predicate: Expression[Func[TSource, BooleanType]]
    ) -> TSource: ...
    @staticmethod
    @overload
    def FirstOrDefault(source: IQueryable[TSource]) -> TSource: ...
    @staticmethod
    @overload
    def FirstOrDefault(
        source: IQueryable[TSource], predicate: Expression[Func[TSource, BooleanType]]
    ) -> TSource: ...
    @staticmethod
    @overload
    def GroupBy(
        source: IQueryable[TSource], keySelector: Expression[Func[TSource, TKey]]
    ) -> IQueryable[IGrouping[TKey, TSource]]: ...
    @staticmethod
    @overload
    def GroupBy(
        source: IQueryable[TSource],
        keySelector: Expression[Func[TSource, TKey]],
        elementSelector: Expression[Func[TSource, TElement]],
    ) -> IQueryable[IGrouping[TKey, TElement]]: ...
    @staticmethod
    @overload
    def GroupBy(
        source: IQueryable[TSource],
        keySelector: Expression[Func[TSource, TKey]],
        comparer: IEqualityComparer[TKey],
    ) -> IQueryable[IGrouping[TKey, TSource]]: ...
    @staticmethod
    @overload
    def GroupBy(
        source: IQueryable[TSource],
        keySelector: Expression[Func[TSource, TKey]],
        elementSelector: Expression[Func[TSource, TElement]],
        comparer: IEqualityComparer[TKey],
    ) -> IQueryable[IGrouping[TKey, TElement]]: ...
    @staticmethod
    @overload
    def GroupBy(
        source: IQueryable[TSource],
        keySelector: Expression[Func[TSource, TKey]],
        elementSelector: Expression[Func[TSource, TElement]],
        resultSelector: Expression[Func[TKey, IEnumerable[TElement], TResult]],
    ) -> IQueryable[TResult]: ...
    @staticmethod
    @overload
    def GroupBy(
        source: IQueryable[TSource],
        keySelector: Expression[Func[TSource, TKey]],
        resultSelector: Expression[Func[TKey, IEnumerable[TSource], TResult]],
    ) -> IQueryable[TResult]: ...
    @staticmethod
    @overload
    def GroupBy(
        source: IQueryable[TSource],
        keySelector: Expression[Func[TSource, TKey]],
        resultSelector: Expression[Func[TKey, IEnumerable[TSource], TResult]],
        comparer: IEqualityComparer[TKey],
    ) -> IQueryable[TResult]: ...
    @staticmethod
    @overload
    def GroupBy(
        source: IQueryable[TSource],
        keySelector: Expression[Func[TSource, TKey]],
        elementSelector: Expression[Func[TSource, TElement]],
        resultSelector: Expression[Func[TKey, IEnumerable[TElement], TResult]],
        comparer: IEqualityComparer[TKey],
    ) -> IQueryable[TResult]: ...
    @staticmethod
    @overload
    def GroupJoin(
        outer: IQueryable[TOuter],
        inner: IEnumerable[TInner],
        outerKeySelector: Expression[Func[TOuter, TKey]],
        innerKeySelector: Expression[Func[TInner, TKey]],
        resultSelector: Expression[Func[TOuter, IEnumerable[TInner], TResult]],
    ) -> IQueryable[TResult]: ...
    @staticmethod
    @overload
    def GroupJoin(
        outer: IQueryable[TOuter],
        inner: IEnumerable[TInner],
        outerKeySelector: Expression[Func[TOuter, TKey]],
        innerKeySelector: Expression[Func[TInner, TKey]],
        resultSelector: Expression[Func[TOuter, IEnumerable[TInner], TResult]],
        comparer: IEqualityComparer[TKey],
    ) -> IQueryable[TResult]: ...
    @staticmethod
    @overload
    def Intersect(
        source1: IQueryable[TSource], source2: IEnumerable[TSource]
    ) -> IQueryable[TSource]: ...
    @staticmethod
    @overload
    def Intersect(
        source1: IQueryable[TSource],
        source2: IEnumerable[TSource],
        comparer: IEqualityComparer[TSource],
    ) -> IQueryable[TSource]: ...
    @staticmethod
    @overload
    def Join(
        outer: IQueryable[TOuter],
        inner: IEnumerable[TInner],
        outerKeySelector: Expression[Func[TOuter, TKey]],
        innerKeySelector: Expression[Func[TInner, TKey]],
        resultSelector: Expression[Func[TOuter, TInner, TResult]],
    ) -> IQueryable[TResult]: ...
    @staticmethod
    @overload
    def Join(
        outer: IQueryable[TOuter],
        inner: IEnumerable[TInner],
        outerKeySelector: Expression[Func[TOuter, TKey]],
        innerKeySelector: Expression[Func[TInner, TKey]],
        resultSelector: Expression[Func[TOuter, TInner, TResult]],
        comparer: IEqualityComparer[TKey],
    ) -> IQueryable[TResult]: ...
    @staticmethod
    @overload
    def Last(source: IQueryable[TSource]) -> TSource: ...
    @staticmethod
    @overload
    def Last(
        source: IQueryable[TSource], predicate: Expression[Func[TSource, BooleanType]]
    ) -> TSource: ...
    @staticmethod
    @overload
    def LastOrDefault(source: IQueryable[TSource]) -> TSource: ...
    @staticmethod
    @overload
    def LastOrDefault(
        source: IQueryable[TSource], predicate: Expression[Func[TSource, BooleanType]]
    ) -> TSource: ...
    @staticmethod
    @overload
    def LongCount(source: IQueryable[TSource]) -> LongType: ...
    @staticmethod
    @overload
    def LongCount(
        source: IQueryable[TSource], predicate: Expression[Func[TSource, BooleanType]]
    ) -> LongType: ...
    @staticmethod
    @overload
    def Max(source: IQueryable[TSource]) -> TSource: ...
    @staticmethod
    @overload
    def Max(
        source: IQueryable[TSource], selector: Expression[Func[TSource, TResult]]
    ) -> TResult: ...
    @staticmethod
    @overload
    def Min(source: IQueryable[TSource]) -> TSource: ...
    @staticmethod
    @overload
    def Min(
        source: IQueryable[TSource], selector: Expression[Func[TSource, TResult]]
    ) -> TResult: ...
    @staticmethod
    def OfType(source: IQueryable) -> IQueryable[TResult]: ...
    @staticmethod
    @overload
    def OrderBy(
        source: IQueryable[TSource], keySelector: Expression[Func[TSource, TKey]]
    ) -> IOrderedQueryable[TSource]: ...
    @staticmethod
    @overload
    def OrderBy(
        source: IQueryable[TSource],
        keySelector: Expression[Func[TSource, TKey]],
        comparer: IComparer[TKey],
    ) -> IOrderedQueryable[TSource]: ...
    @staticmethod
    @overload
    def OrderByDescending(
        source: IQueryable[TSource], keySelector: Expression[Func[TSource, TKey]]
    ) -> IOrderedQueryable[TSource]: ...
    @staticmethod
    @overload
    def OrderByDescending(
        source: IQueryable[TSource],
        keySelector: Expression[Func[TSource, TKey]],
        comparer: IComparer[TKey],
    ) -> IOrderedQueryable[TSource]: ...
    @staticmethod
    def Reverse(source: IQueryable[TSource]) -> IQueryable[TSource]: ...
    @staticmethod
    @overload
    def Select(
        source: IQueryable[TSource], selector: Expression[Func[TSource, TResult]]
    ) -> IQueryable[TResult]: ...
    @staticmethod
    @overload
    def Select(
        source: IQueryable[TSource], selector: Expression[Func[TSource, IntType, TResult]]
    ) -> IQueryable[TResult]: ...
    @staticmethod
    @overload
    def SelectMany(
        source: IQueryable[TSource], selector: Expression[Func[TSource, IEnumerable[TResult]]]
    ) -> IQueryable[TResult]: ...
    @staticmethod
    @overload
    def SelectMany(
        source: IQueryable[TSource],
        selector: Expression[Func[TSource, IntType, IEnumerable[TResult]]],
    ) -> IQueryable[TResult]: ...
    @staticmethod
    @overload
    def SelectMany(
        source: IQueryable[TSource],
        collectionSelector: Expression[Func[TSource, IntType, IEnumerable[TCollection]]],
        resultSelector: Expression[Func[TSource, TCollection, TResult]],
    ) -> IQueryable[TResult]: ...
    @staticmethod
    @overload
    def SelectMany(
        source: IQueryable[TSource],
        collectionSelector: Expression[Func[TSource, IEnumerable[TCollection]]],
        resultSelector: Expression[Func[TSource, TCollection, TResult]],
    ) -> IQueryable[TResult]: ...
    @staticmethod
    @overload
    def SequenceEqual(
        source1: IQueryable[TSource], source2: IEnumerable[TSource]
    ) -> BooleanType: ...
    @staticmethod
    @overload
    def SequenceEqual(
        source1: IQueryable[TSource],
        source2: IEnumerable[TSource],
        comparer: IEqualityComparer[TSource],
    ) -> BooleanType: ...
    @staticmethod
    @overload
    def Single(source: IQueryable[TSource]) -> TSource: ...
    @staticmethod
    @overload
    def Single(
        source: IQueryable[TSource], predicate: Expression[Func[TSource, BooleanType]]
    ) -> TSource: ...
    @staticmethod
    @overload
    def SingleOrDefault(source: IQueryable[TSource]) -> TSource: ...
    @staticmethod
    @overload
    def SingleOrDefault(
        source: IQueryable[TSource], predicate: Expression[Func[TSource, BooleanType]]
    ) -> TSource: ...
    @staticmethod
    def Skip(source: IQueryable[TSource], count: IntType) -> IQueryable[TSource]: ...
    @staticmethod
    @overload
    def SkipWhile(
        source: IQueryable[TSource], predicate: Expression[Func[TSource, BooleanType]]
    ) -> IQueryable[TSource]: ...
    @staticmethod
    @overload
    def SkipWhile(
        source: IQueryable[TSource], predicate: Expression[Func[TSource, IntType, BooleanType]]
    ) -> IQueryable[TSource]: ...
    @staticmethod
    @overload
    def Sum(source: IQueryable[IntType]) -> IntType: ...
    @staticmethod
    @overload
    def Sum(
        source: IQueryable[NullableType[Nullable[IntType]]],
    ) -> NullableType[Nullable[IntType]]: ...
    @staticmethod
    @overload
    def Sum(source: IQueryable[LongType]) -> LongType: ...
    @staticmethod
    @overload
    def Sum(
        source: IQueryable[NullableType[Nullable[LongType]]],
    ) -> NullableType[Nullable[LongType]]: ...
    @staticmethod
    @overload
    def Sum(source: IQueryable[FloatType]) -> FloatType: ...
    @staticmethod
    @overload
    def Sum(
        source: IQueryable[NullableType[Nullable[FloatType]]],
    ) -> NullableType[Nullable[FloatType]]: ...
    @staticmethod
    @overload
    def Sum(source: IQueryable[DoubleType]) -> DoubleType: ...
    @staticmethod
    @overload
    def Sum(
        source: IQueryable[NullableType[Nullable[DoubleType]]],
    ) -> NullableType[Nullable[DoubleType]]: ...
    @staticmethod
    @overload
    def Sum(source: IQueryable[DecimalType]) -> DecimalType: ...
    @staticmethod
    @overload
    def Sum(
        source: IQueryable[NullableType[Nullable[DecimalType]]],
    ) -> NullableType[Nullable[DecimalType]]: ...
    @staticmethod
    @overload
    def Sum(
        source: IQueryable[TSource], selector: Expression[Func[TSource, IntType]]
    ) -> IntType: ...
    @staticmethod
    @overload
    def Sum(
        source: IQueryable[TSource],
        selector: Expression[Func[TSource, NullableType[Nullable[IntType]]]],
    ) -> NullableType[Nullable[IntType]]: ...
    @staticmethod
    @overload
    def Sum(
        source: IQueryable[TSource], selector: Expression[Func[TSource, LongType]]
    ) -> LongType: ...
    @staticmethod
    @overload
    def Sum(
        source: IQueryable[TSource],
        selector: Expression[Func[TSource, NullableType[Nullable[LongType]]]],
    ) -> NullableType[Nullable[LongType]]: ...
    @staticmethod
    @overload
    def Sum(
        source: IQueryable[TSource], selector: Expression[Func[TSource, FloatType]]
    ) -> FloatType: ...
    @staticmethod
    @overload
    def Sum(
        source: IQueryable[TSource],
        selector: Expression[Func[TSource, NullableType[Nullable[FloatType]]]],
    ) -> NullableType[Nullable[FloatType]]: ...
    @staticmethod
    @overload
    def Sum(
        source: IQueryable[TSource], selector: Expression[Func[TSource, DoubleType]]
    ) -> DoubleType: ...
    @staticmethod
    @overload
    def Sum(
        source: IQueryable[TSource],
        selector: Expression[Func[TSource, NullableType[Nullable[DoubleType]]]],
    ) -> NullableType[Nullable[DoubleType]]: ...
    @staticmethod
    @overload
    def Sum(
        source: IQueryable[TSource], selector: Expression[Func[TSource, DecimalType]]
    ) -> DecimalType: ...
    @staticmethod
    @overload
    def Sum(
        source: IQueryable[TSource],
        selector: Expression[Func[TSource, NullableType[Nullable[DecimalType]]]],
    ) -> NullableType[Nullable[DecimalType]]: ...
    @staticmethod
    def Take(source: IQueryable[TSource], count: IntType) -> IQueryable[TSource]: ...
    @staticmethod
    @overload
    def TakeWhile(
        source: IQueryable[TSource], predicate: Expression[Func[TSource, BooleanType]]
    ) -> IQueryable[TSource]: ...
    @staticmethod
    @overload
    def TakeWhile(
        source: IQueryable[TSource], predicate: Expression[Func[TSource, IntType, BooleanType]]
    ) -> IQueryable[TSource]: ...
    @staticmethod
    @overload
    def ThenBy(
        source: IOrderedQueryable[TSource], keySelector: Expression[Func[TSource, TKey]]
    ) -> IOrderedQueryable[TSource]: ...
    @staticmethod
    @overload
    def ThenBy(
        source: IOrderedQueryable[TSource],
        keySelector: Expression[Func[TSource, TKey]],
        comparer: IComparer[TKey],
    ) -> IOrderedQueryable[TSource]: ...
    @staticmethod
    @overload
    def ThenByDescending(
        source: IOrderedQueryable[TSource], keySelector: Expression[Func[TSource, TKey]]
    ) -> IOrderedQueryable[TSource]: ...
    @staticmethod
    @overload
    def ThenByDescending(
        source: IOrderedQueryable[TSource],
        keySelector: Expression[Func[TSource, TKey]],
        comparer: IComparer[TKey],
    ) -> IOrderedQueryable[TSource]: ...
    @staticmethod
    @overload
    def Union(
        source1: IQueryable[TSource], source2: IEnumerable[TSource]
    ) -> IQueryable[TSource]: ...
    @staticmethod
    @overload
    def Union(
        source1: IQueryable[TSource],
        source2: IEnumerable[TSource],
        comparer: IEqualityComparer[TSource],
    ) -> IQueryable[TSource]: ...
    @staticmethod
    @overload
    def Where(
        source: IQueryable[TSource], predicate: Expression[Func[TSource, BooleanType]]
    ) -> IQueryable[TSource]: ...
    @staticmethod
    @overload
    def Where(
        source: IQueryable[TSource], predicate: Expression[Func[TSource, IntType, BooleanType]]
    ) -> IQueryable[TSource]: ...
    @staticmethod
    def Zip(
        source1: IQueryable[TFirst],
        source2: IEnumerable[TSecond],
        resultSelector: Expression[Func[TFirst, TSecond, TResult]],
    ) -> IQueryable[TResult]: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class SR(ObjectType):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @staticmethod
    @property
    def Resources() -> ResourceManager: ...

    # ---------- Methods ---------- #

    @staticmethod
    def GetObject(name: StringType) -> ObjectType: ...
    @staticmethod
    @overload
    def GetString(name: StringType) -> StringType: ...
    @staticmethod
    @overload
    def GetString(
        name: StringType, usedFallback: BooleanType
    ) -> Tuple[StringType, BooleanType]: ...
    @staticmethod
    @overload
    def GetString(name: StringType, args: ArrayType[ObjectType]) -> StringType: ...
    @staticmethod
    def get_Resources() -> ResourceManager: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class SRCategoryAttribute(CategoryAttribute, _Attribute):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, category: StringType): ...

    # No Properties

    # No Methods

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class SRDescriptionAttribute(DescriptionAttribute, _Attribute):
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

class Set(Generic[TElement], ObjectType):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, comparer: IEqualityComparer[TElement]): ...

    # No Properties

    # ---------- Methods ---------- #

    def Add(self, value: TElement) -> BooleanType: ...
    def Contains(self, value: TElement) -> BooleanType: ...
    def Remove(self, value: TElement) -> BooleanType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class SingleLinkedNode(Generic[TSource], ObjectType):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, item: TSource): ...

    # ---------- Properties ---------- #

    @property
    def Item(self) -> TSource: ...
    @property
    def Linked(self) -> SingleLinkedNode[TSource]: ...

    # ---------- Methods ---------- #

    def Add(self, item: TSource) -> SingleLinkedNode[TSource]: ...
    def GetCount(self) -> IntType: ...
    def GetEnumerator(self, count: IntType) -> IEnumerator[TSource]: ...
    def GetNode(self, index: IntType) -> SingleLinkedNode[TSource]: ...
    def ToArray(self, count: IntType) -> ArrayType[TSource]: ...
    def get_Item(self) -> TSource: ...
    def get_Linked(self) -> SingleLinkedNode[TSource]: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class Strings(ABC, ObjectType):
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

class SystemCore_EnumerableDebugView(ObjectType):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, enumerable: IEnumerable): ...

    # ---------- Properties ---------- #

    @property
    def Items(self) -> ArrayType[ObjectType]: ...

    # ---------- Methods ---------- #

    def get_Items(self) -> ArrayType[ObjectType]: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class SystemCore_EnumerableDebugView(Generic[T], ObjectType):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, enumerable: IEnumerable[T]): ...

    # ---------- Properties ---------- #

    @property
    def Items(self) -> ArrayType[T]: ...

    # ---------- Methods ---------- #

    def get_Items(self) -> ArrayType[T]: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class SystemCore_EnumerableDebugViewEmptyException(Exception, ISerializable, _Exception):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # ---------- Properties ---------- #

    @property
    def Empty(self) -> StringType: ...

    # ---------- Methods ---------- #

    def get_Empty(self) -> StringType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class TypeHelper(ABC, ObjectType):
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

class Buffer(Generic[TElement], ValueType):
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

# ---------- Interfaces ---------- #

class IGrouping(Protocol[TKey, TElement], IEnumerable[TElement], IEnumerable):
    # ---------- Properties ---------- #

    @property
    def Key(self) -> TKey: ...

    # ---------- Methods ---------- #

    def get_Key(self) -> TKey: ...

    # No Events

class IIListProvider(Protocol[TElement], IEnumerable[TElement], IEnumerable):
    # No Properties

    # ---------- Methods ---------- #

    def GetCount(self, onlyIfCheap: BooleanType) -> IntType: ...
    def ToArray(self) -> ArrayType[TElement]: ...
    def ToList(self) -> List[TElement]: ...

    # No Events

class ILookup(Protocol[TKey, TElement], IEnumerable[IGrouping[TKey, TElement]], IEnumerable):
    # ---------- Properties ---------- #

    @property
    def Count(self) -> IntType: ...
    def __getitem__(self, key: TKey) -> IEnumerable[TElement]: ...

    # ---------- Methods ---------- #

    def Contains(self, key: TKey) -> BooleanType: ...
    def get_Count(self) -> IntType: ...
    def get_Item(self, key: TKey) -> IEnumerable[TElement]: ...

    # No Events

class IOrderedEnumerable(Protocol[TElement], IEnumerable[TElement], IEnumerable):
    # No Properties

    # ---------- Methods ---------- #

    def CreateOrderedEnumerable(
        self, keySelector: Func[TElement, TKey], comparer: IComparer[TKey], descending: BooleanType
    ) -> IOrderedEnumerable[TElement]: ...

    # No Events

class IOrderedQueryable(
    Protocol[T], IQueryable[T], IEnumerable[T], IEnumerable, IQueryable, IOrderedQueryable
):
    """"""

    # No Properties

    # No Methods

    # No Events

class IOrderedQueryable(Protocol, IQueryable, IEnumerable):
    """"""

    # No Properties

    # No Methods

    # No Events

class IQueryProvider(Protocol):
    # No Properties

    # ---------- Methods ---------- #

    @overload
    def CreateQuery(self, expression: Expression) -> IQueryable: ...
    @overload
    def CreateQuery(self, expression: Expression) -> IQueryable[TElement]: ...
    @overload
    def Execute(self, expression: Expression) -> ObjectType: ...
    @overload
    def Execute(self, expression: Expression) -> TResult: ...

    # No Events

class IQueryable(Protocol[T], IEnumerable[T], IEnumerable, IQueryable):
    """"""

    # No Properties

    # No Methods

    # No Events

class IQueryable(Protocol, IEnumerable):
    # ---------- Properties ---------- #

    @property
    def ElementType(self) -> TypeType: ...
    @property
    def Expression(self) -> Expression: ...
    @property
    def Provider(self) -> IQueryProvider: ...

    # ---------- Methods ---------- #

    def get_ElementType(self) -> TypeType: ...
    def get_Expression(self) -> Expression: ...
    def get_Provider(self) -> IQueryProvider: ...

    # No Events

# ---------- Enums ---------- #

class ParallelExecutionMode(Enum):
    Default = 0
    ForceParallelism = 1

class ParallelMergeOptions(Enum):
    Default = 0
    NotBuffered = 1
    AutoBuffered = 2
    FullyBuffered = 3

# No Delegates

__all__ = [
    AggregationMinMaxHelpers,
    EmptyEnumerable,
    Enumerable,
    EnumerableExecutor,
    EnumerableQuery,
    EnumerableRewriter,
    EnumerableSorter,
    Error,
    GroupedEnumerable,
    IdentityFunction,
    Lookup,
    OrderedEnumerable,
    OrderedParallelQuery,
    ParallelEnumerable,
    ParallelQuery,
    Queryable,
    SR,
    SRCategoryAttribute,
    SRDescriptionAttribute,
    Set,
    SingleLinkedNode,
    Strings,
    SystemCore_EnumerableDebugView,
    SystemCore_EnumerableDebugViewEmptyException,
    TypeHelper,
    Buffer,
    IGrouping,
    IIListProvider,
    ILookup,
    IOrderedEnumerable,
    IOrderedQueryable,
    IQueryProvider,
    IQueryable,
    ParallelExecutionMode,
    ParallelMergeOptions,
]
