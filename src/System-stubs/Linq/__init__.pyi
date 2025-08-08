"""Automatically generated stubs for C# namespace: System.Linq."""

from abc import ABC
from collections.abc import Iterator
from typing import ClassVar
from typing import overload

from System import Action
from System import Array
from System import Boolean
from System import Decimal
from System import Enum
from System import Exception
from System import Func
from System import Guid
from System import IntPtr
from System import Object
from System import Type
from System import UInt32
from System import ValueType
from System.Collections import IDictionary
from System.Collections import IEnumerable
from System.Collections import IEnumerator
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
from System.Reflection import MethodBase
from System.Resources import ResourceManager
from System.Runtime.InteropServices import _Attribute
from System.Runtime.InteropServices import _Exception
from System.Runtime.Serialization import ISerializable
from System.Runtime.Serialization import SerializationInfo
from System.Runtime.Serialization import StreamingContext
from System.Threading import CancellationToken

class AggregationMinMaxHelpers[T](ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class Buffer[TElement](ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class EmptyEnumerable[TElement](Object):
    """"""

    Instance: ClassVar[Array[TElement]]
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

class Enumerable(ABC, Object):
    """"""
    @classmethod
    @overload
    def Aggregate[TSource, TAccumulate](
        cls,
        source: IEnumerable[TSource],
        seed: TAccumulate,
        func: Func[TAccumulate, TSource, TAccumulate],
    ) -> TAccumulate:
        """"""
    @classmethod
    @overload
    def Aggregate[TSource, TAccumulate, TResult](
        cls,
        source: IEnumerable[TSource],
        seed: TAccumulate,
        func: Func[TAccumulate, TSource, TAccumulate],
        resultSelector: Func[TAccumulate, TResult],
    ) -> TResult:
        """"""
    @classmethod
    @overload
    def Aggregate[TSource](
        cls, source: IEnumerable[TSource], func: Func[TSource, TSource, TSource]
    ) -> TSource:
        """"""
    @classmethod
    def All[TSource](cls, source: IEnumerable[TSource], predicate: Func[TSource, bool]) -> bool:
        """"""
    @classmethod
    @overload
    def Any[TSource](cls, source: IEnumerable[TSource]) -> bool:
        """"""
    @classmethod
    @overload
    def Any[TSource](cls, source: IEnumerable[TSource], predicate: Func[TSource, bool]) -> bool:
        """"""
    @classmethod
    def Append[TSource](
        cls, source: IEnumerable[TSource], element: TSource
    ) -> IEnumerable[TSource]:
        """"""
    @classmethod
    def AsEnumerable[TSource](cls, source: IEnumerable[TSource]) -> IEnumerable[TSource]:
        """"""
    @classmethod
    @overload
    def Average[TSource](
        cls, source: IEnumerable[TSource], selector: Func[TSource, Decimal | None]
    ) -> Decimal | None:
        """"""
    @classmethod
    @overload
    def Average[TSource](
        cls, source: IEnumerable[TSource], selector: Func[TSource, Decimal]
    ) -> Decimal:
        """"""
    @classmethod
    @overload
    def Average[TSource](
        cls, source: IEnumerable[TSource], selector: Func[TSource, float | None]
    ) -> float | None:
        """"""
    @classmethod
    @overload
    def Average[TSource](
        cls, source: IEnumerable[TSource], selector: Func[TSource, float]
    ) -> float:
        """"""
    @classmethod
    @overload
    def Average[TSource](
        cls, source: IEnumerable[TSource], selector: Func[TSource, int | None]
    ) -> float | None:
        """"""
    @classmethod
    @overload
    def Average[TSource](cls, source: IEnumerable[TSource], selector: Func[TSource, int]) -> float:
        """"""
    @classmethod
    @overload
    def Average[TSource](
        cls, source: IEnumerable[TSource], selector: Func[TSource, int | None]
    ) -> float | None:
        """"""
    @classmethod
    @overload
    def Average[TSource](cls, source: IEnumerable[TSource], selector: Func[TSource, int]) -> float:
        """"""
    @classmethod
    @overload
    def Average[TSource](
        cls, source: IEnumerable[TSource], selector: Func[TSource, float | None]
    ) -> float | None:
        """"""
    @classmethod
    @overload
    def Average[TSource](
        cls, source: IEnumerable[TSource], selector: Func[TSource, float]
    ) -> float:
        """"""
    @classmethod
    @overload
    def Average(cls, source: IEnumerable[Decimal | None]) -> Decimal | None:
        """"""
    @classmethod
    @overload
    def Average(cls, source: IEnumerable[Decimal]) -> Decimal:
        """"""
    @classmethod
    @overload
    def Average(cls, source: IEnumerable[float | None]) -> float | None:
        """"""
    @classmethod
    @overload
    def Average(cls, source: IEnumerable[float]) -> float:
        """"""
    @classmethod
    @overload
    def Average(cls, source: IEnumerable[int | None]) -> float | None:
        """"""
    @classmethod
    @overload
    def Average(cls, source: IEnumerable[int]) -> float:
        """"""
    @classmethod
    @overload
    def Average(cls, source: IEnumerable[int | None]) -> float | None:
        """"""
    @classmethod
    @overload
    def Average(cls, source: IEnumerable[int]) -> float:
        """"""
    @classmethod
    @overload
    def Average(cls, source: IEnumerable[float | None]) -> float | None:
        """"""
    @classmethod
    @overload
    def Average(cls, source: IEnumerable[float]) -> float:
        """"""
    @classmethod
    def Cast[TResult](cls, source: IEnumerable) -> IEnumerable[TResult]:
        """"""
    @classmethod
    def Concat[TSource](
        cls, first: IEnumerable[TSource], second: IEnumerable[TSource]
    ) -> IEnumerable[TSource]:
        """"""
    @classmethod
    @overload
    def Contains[TSource](cls, source: IEnumerable[TSource], value: TSource) -> bool:
        """"""
    @classmethod
    @overload
    def Contains[TSource](
        cls, source: IEnumerable[TSource], value: TSource, comparer: IEqualityComparer[TSource]
    ) -> bool:
        """"""
    @classmethod
    @overload
    def Count[TSource](cls, source: IEnumerable[TSource]) -> int:
        """"""
    @classmethod
    @overload
    def Count[TSource](cls, source: IEnumerable[TSource], predicate: Func[TSource, bool]) -> int:
        """"""
    @classmethod
    @overload
    def DefaultIfEmpty[TSource](cls, source: IEnumerable[TSource]) -> IEnumerable[TSource]:
        """"""
    @classmethod
    @overload
    def DefaultIfEmpty[TSource](
        cls, source: IEnumerable[TSource], defaultValue: TSource
    ) -> IEnumerable[TSource]:
        """"""
    @classmethod
    @overload
    def Distinct[TSource](cls, source: IEnumerable[TSource]) -> IEnumerable[TSource]:
        """"""
    @classmethod
    @overload
    def Distinct[TSource](
        cls, source: IEnumerable[TSource], comparer: IEqualityComparer[TSource]
    ) -> IEnumerable[TSource]:
        """"""
    @classmethod
    def ElementAt[TSource](cls, source: IEnumerable[TSource], index: int) -> TSource:
        """"""
    @classmethod
    def ElementAtOrDefault[TSource](cls, source: IEnumerable[TSource], index: int) -> TSource:
        """"""
    @classmethod
    def Empty[TResult](cls) -> IEnumerable[TResult]:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    @overload
    def Except[TSource](
        cls, first: IEnumerable[TSource], second: IEnumerable[TSource]
    ) -> IEnumerable[TSource]:
        """"""
    @classmethod
    @overload
    def Except[TSource](
        cls,
        first: IEnumerable[TSource],
        second: IEnumerable[TSource],
        comparer: IEqualityComparer[TSource],
    ) -> IEnumerable[TSource]:
        """"""
    @classmethod
    @overload
    def First[TSource](cls, source: IEnumerable[TSource]) -> TSource:
        """"""
    @classmethod
    @overload
    def First[TSource](
        cls, source: IEnumerable[TSource], predicate: Func[TSource, bool]
    ) -> TSource:
        """"""
    @classmethod
    @overload
    def FirstOrDefault[TSource](cls, source: IEnumerable[TSource]) -> TSource:
        """"""
    @classmethod
    @overload
    def FirstOrDefault[TSource](
        cls, source: IEnumerable[TSource], predicate: Func[TSource, bool]
    ) -> TSource:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    @overload
    def GroupBy[TSource, TKey](
        cls, source: IEnumerable[TSource], keySelector: Func[TSource, TKey]
    ) -> IEnumerable[IGrouping[TKey, TSource]]:
        """"""
    @classmethod
    @overload
    def GroupBy[TSource, TKey](
        cls,
        source: IEnumerable[TSource],
        keySelector: Func[TSource, TKey],
        comparer: IEqualityComparer[TKey],
    ) -> IEnumerable[IGrouping[TKey, TSource]]:
        """"""
    @classmethod
    @overload
    def GroupBy[TSource, TKey, TResult](
        cls,
        source: IEnumerable[TSource],
        keySelector: Func[TSource, TKey],
        resultSelector: Func[TKey, IEnumerable[TSource], TResult],
    ) -> IEnumerable[TResult]:
        """"""
    @classmethod
    @overload
    def GroupBy[TSource, TKey, TResult](
        cls,
        source: IEnumerable[TSource],
        keySelector: Func[TSource, TKey],
        resultSelector: Func[TKey, IEnumerable[TSource], TResult],
        comparer: IEqualityComparer[TKey],
    ) -> IEnumerable[TResult]:
        """"""
    @classmethod
    @overload
    def GroupBy[TSource, TKey, TElement](
        cls,
        source: IEnumerable[TSource],
        keySelector: Func[TSource, TKey],
        elementSelector: Func[TSource, TElement],
    ) -> IEnumerable[IGrouping[TKey, TElement]]:
        """"""
    @classmethod
    @overload
    def GroupBy[TSource, TKey, TElement](
        cls,
        source: IEnumerable[TSource],
        keySelector: Func[TSource, TKey],
        elementSelector: Func[TSource, TElement],
        comparer: IEqualityComparer[TKey],
    ) -> IEnumerable[IGrouping[TKey, TElement]]:
        """"""
    @classmethod
    @overload
    def GroupBy[TSource, TKey, TElement, TResult](
        cls,
        source: IEnumerable[TSource],
        keySelector: Func[TSource, TKey],
        elementSelector: Func[TSource, TElement],
        resultSelector: Func[TKey, IEnumerable[TElement], TResult],
    ) -> IEnumerable[TResult]:
        """"""
    @classmethod
    @overload
    def GroupBy[TSource, TKey, TElement, TResult](
        cls,
        source: IEnumerable[TSource],
        keySelector: Func[TSource, TKey],
        elementSelector: Func[TSource, TElement],
        resultSelector: Func[TKey, IEnumerable[TElement], TResult],
        comparer: IEqualityComparer[TKey],
    ) -> IEnumerable[TResult]:
        """"""
    @classmethod
    @overload
    def GroupJoin[TOuter, TInner, TKey, TResult](
        cls,
        outer: IEnumerable[TOuter],
        inner: IEnumerable[TInner],
        outerKeySelector: Func[TOuter, TKey],
        innerKeySelector: Func[TInner, TKey],
        resultSelector: Func[TOuter, IEnumerable[TInner], TResult],
    ) -> IEnumerable[TResult]:
        """"""
    @classmethod
    @overload
    def GroupJoin[TOuter, TInner, TKey, TResult](
        cls,
        outer: IEnumerable[TOuter],
        inner: IEnumerable[TInner],
        outerKeySelector: Func[TOuter, TKey],
        innerKeySelector: Func[TInner, TKey],
        resultSelector: Func[TOuter, IEnumerable[TInner], TResult],
        comparer: IEqualityComparer[TKey],
    ) -> IEnumerable[TResult]:
        """"""
    @classmethod
    @overload
    def Intersect[TSource](
        cls, first: IEnumerable[TSource], second: IEnumerable[TSource]
    ) -> IEnumerable[TSource]:
        """"""
    @classmethod
    @overload
    def Intersect[TSource](
        cls,
        first: IEnumerable[TSource],
        second: IEnumerable[TSource],
        comparer: IEqualityComparer[TSource],
    ) -> IEnumerable[TSource]:
        """"""
    @classmethod
    @overload
    def Join[TOuter, TInner, TKey, TResult](
        cls,
        outer: IEnumerable[TOuter],
        inner: IEnumerable[TInner],
        outerKeySelector: Func[TOuter, TKey],
        innerKeySelector: Func[TInner, TKey],
        resultSelector: Func[TOuter, TInner, TResult],
    ) -> IEnumerable[TResult]:
        """"""
    @classmethod
    @overload
    def Join[TOuter, TInner, TKey, TResult](
        cls,
        outer: IEnumerable[TOuter],
        inner: IEnumerable[TInner],
        outerKeySelector: Func[TOuter, TKey],
        innerKeySelector: Func[TInner, TKey],
        resultSelector: Func[TOuter, TInner, TResult],
        comparer: IEqualityComparer[TKey],
    ) -> IEnumerable[TResult]:
        """"""
    @classmethod
    @overload
    def Last[TSource](cls, source: IEnumerable[TSource]) -> TSource:
        """"""
    @classmethod
    @overload
    def Last[TSource](cls, source: IEnumerable[TSource], predicate: Func[TSource, bool]) -> TSource:
        """"""
    @classmethod
    @overload
    def LastOrDefault[TSource](cls, source: IEnumerable[TSource]) -> TSource:
        """"""
    @classmethod
    @overload
    def LastOrDefault[TSource](
        cls, source: IEnumerable[TSource], predicate: Func[TSource, bool]
    ) -> TSource:
        """"""
    @classmethod
    @overload
    def LongCount[TSource](cls, source: IEnumerable[TSource]) -> int:
        """"""
    @classmethod
    @overload
    def LongCount[TSource](
        cls, source: IEnumerable[TSource], predicate: Func[TSource, bool]
    ) -> int:
        """"""
    @classmethod
    @overload
    def Max[TSource](cls, source: IEnumerable[TSource]) -> TSource:
        """"""
    @classmethod
    @overload
    def Max[TSource, TResult](
        cls, source: IEnumerable[TSource], selector: Func[TSource, TResult]
    ) -> TResult:
        """"""
    @classmethod
    @overload
    def Max[TSource](
        cls, source: IEnumerable[TSource], selector: Func[TSource, Decimal | None]
    ) -> Decimal | None:
        """"""
    @classmethod
    @overload
    def Max[TSource](
        cls, source: IEnumerable[TSource], selector: Func[TSource, Decimal]
    ) -> Decimal:
        """"""
    @classmethod
    @overload
    def Max[TSource](
        cls, source: IEnumerable[TSource], selector: Func[TSource, float | None]
    ) -> float | None:
        """"""
    @classmethod
    @overload
    def Max[TSource](cls, source: IEnumerable[TSource], selector: Func[TSource, float]) -> float:
        """"""
    @classmethod
    @overload
    def Max[TSource](
        cls, source: IEnumerable[TSource], selector: Func[TSource, int | None]
    ) -> int | None:
        """"""
    @classmethod
    @overload
    def Max[TSource](cls, source: IEnumerable[TSource], selector: Func[TSource, int]) -> int:
        """"""
    @classmethod
    @overload
    def Max[TSource](
        cls, source: IEnumerable[TSource], selector: Func[TSource, int | None]
    ) -> int | None:
        """"""
    @classmethod
    @overload
    def Max[TSource](cls, source: IEnumerable[TSource], selector: Func[TSource, int]) -> int:
        """"""
    @classmethod
    @overload
    def Max[TSource](
        cls, source: IEnumerable[TSource], selector: Func[TSource, float | None]
    ) -> float | None:
        """"""
    @classmethod
    @overload
    def Max[TSource](cls, source: IEnumerable[TSource], selector: Func[TSource, float]) -> float:
        """"""
    @classmethod
    @overload
    def Max(cls, source: IEnumerable[Decimal | None]) -> Decimal | None:
        """"""
    @classmethod
    @overload
    def Max(cls, source: IEnumerable[Decimal]) -> Decimal:
        """"""
    @classmethod
    @overload
    def Max(cls, source: IEnumerable[float | None]) -> float | None:
        """"""
    @classmethod
    @overload
    def Max(cls, source: IEnumerable[float]) -> float:
        """"""
    @classmethod
    @overload
    def Max(cls, source: IEnumerable[int | None]) -> int | None:
        """"""
    @classmethod
    @overload
    def Max(cls, source: IEnumerable[int]) -> int:
        """"""
    @classmethod
    @overload
    def Max(cls, source: IEnumerable[int | None]) -> int | None:
        """"""
    @classmethod
    @overload
    def Max(cls, source: IEnumerable[int]) -> int:
        """"""
    @classmethod
    @overload
    def Max(cls, source: IEnumerable[float | None]) -> float | None:
        """"""
    @classmethod
    @overload
    def Max(cls, source: IEnumerable[float]) -> float:
        """"""
    @classmethod
    @overload
    def Min[TSource](cls, source: IEnumerable[TSource]) -> TSource:
        """"""
    @classmethod
    @overload
    def Min[TSource, TResult](
        cls, source: IEnumerable[TSource], selector: Func[TSource, TResult]
    ) -> TResult:
        """"""
    @classmethod
    @overload
    def Min[TSource](
        cls, source: IEnumerable[TSource], selector: Func[TSource, Decimal | None]
    ) -> Decimal | None:
        """"""
    @classmethod
    @overload
    def Min[TSource](
        cls, source: IEnumerable[TSource], selector: Func[TSource, Decimal]
    ) -> Decimal:
        """"""
    @classmethod
    @overload
    def Min[TSource](
        cls, source: IEnumerable[TSource], selector: Func[TSource, float | None]
    ) -> float | None:
        """"""
    @classmethod
    @overload
    def Min[TSource](cls, source: IEnumerable[TSource], selector: Func[TSource, float]) -> float:
        """"""
    @classmethod
    @overload
    def Min[TSource](
        cls, source: IEnumerable[TSource], selector: Func[TSource, int | None]
    ) -> int | None:
        """"""
    @classmethod
    @overload
    def Min[TSource](cls, source: IEnumerable[TSource], selector: Func[TSource, int]) -> int:
        """"""
    @classmethod
    @overload
    def Min[TSource](
        cls, source: IEnumerable[TSource], selector: Func[TSource, int | None]
    ) -> int | None:
        """"""
    @classmethod
    @overload
    def Min[TSource](cls, source: IEnumerable[TSource], selector: Func[TSource, int]) -> int:
        """"""
    @classmethod
    @overload
    def Min[TSource](
        cls, source: IEnumerable[TSource], selector: Func[TSource, float | None]
    ) -> float | None:
        """"""
    @classmethod
    @overload
    def Min[TSource](cls, source: IEnumerable[TSource], selector: Func[TSource, float]) -> float:
        """"""
    @classmethod
    @overload
    def Min(cls, source: IEnumerable[Decimal | None]) -> Decimal | None:
        """"""
    @classmethod
    @overload
    def Min(cls, source: IEnumerable[Decimal]) -> Decimal:
        """"""
    @classmethod
    @overload
    def Min(cls, source: IEnumerable[float | None]) -> float | None:
        """"""
    @classmethod
    @overload
    def Min(cls, source: IEnumerable[float]) -> float:
        """"""
    @classmethod
    @overload
    def Min(cls, source: IEnumerable[int | None]) -> int | None:
        """"""
    @classmethod
    @overload
    def Min(cls, source: IEnumerable[int]) -> int:
        """"""
    @classmethod
    @overload
    def Min(cls, source: IEnumerable[int | None]) -> int | None:
        """"""
    @classmethod
    @overload
    def Min(cls, source: IEnumerable[int]) -> int:
        """"""
    @classmethod
    @overload
    def Min(cls, source: IEnumerable[float | None]) -> float | None:
        """"""
    @classmethod
    @overload
    def Min(cls, source: IEnumerable[float]) -> float:
        """"""
    @classmethod
    def OfType[TResult](cls, source: IEnumerable) -> IEnumerable[TResult]:
        """"""
    @classmethod
    @overload
    def OrderBy[TSource, TKey](
        cls, source: IEnumerable[TSource], keySelector: Func[TSource, TKey]
    ) -> IOrderedEnumerable[TSource]:
        """"""
    @classmethod
    @overload
    def OrderBy[TSource, TKey](
        cls,
        source: IEnumerable[TSource],
        keySelector: Func[TSource, TKey],
        comparer: IComparer[TKey],
    ) -> IOrderedEnumerable[TSource]:
        """"""
    @classmethod
    @overload
    def OrderByDescending[TSource, TKey](
        cls, source: IEnumerable[TSource], keySelector: Func[TSource, TKey]
    ) -> IOrderedEnumerable[TSource]:
        """"""
    @classmethod
    @overload
    def OrderByDescending[TSource, TKey](
        cls,
        source: IEnumerable[TSource],
        keySelector: Func[TSource, TKey],
        comparer: IComparer[TKey],
    ) -> IOrderedEnumerable[TSource]:
        """"""
    @classmethod
    def Prepend[TSource](
        cls, source: IEnumerable[TSource], element: TSource
    ) -> IEnumerable[TSource]:
        """"""
    @classmethod
    def Range(cls, start: int, count: int) -> IEnumerable[int]:
        """"""
    @classmethod
    def Repeat[TResult](cls, element: TResult, count: int) -> IEnumerable[TResult]:
        """"""
    @classmethod
    def Reverse[TSource](cls, source: IEnumerable[TSource]) -> IEnumerable[TSource]:
        """"""
    @classmethod
    @overload
    def Select[TSource, TResult](
        cls, source: IEnumerable[TSource], selector: Func[TSource, TResult]
    ) -> IEnumerable[TResult]:
        """"""
    @classmethod
    @overload
    def Select[TSource, TResult](
        cls, source: IEnumerable[TSource], selector: Func[TSource, int, TResult]
    ) -> IEnumerable[TResult]:
        """"""
    @classmethod
    @overload
    def SelectMany[TSource, TCollection, TResult](
        cls,
        source: IEnumerable[TSource],
        collectionSelector: Func[TSource, IEnumerable[TCollection]],
        resultSelector: Func[TSource, TCollection, TResult],
    ) -> IEnumerable[TResult]:
        """"""
    @classmethod
    @overload
    def SelectMany[TSource, TResult](
        cls, source: IEnumerable[TSource], selector: Func[TSource, IEnumerable[TResult]]
    ) -> IEnumerable[TResult]:
        """"""
    @classmethod
    @overload
    def SelectMany[TSource, TCollection, TResult](
        cls,
        source: IEnumerable[TSource],
        collectionSelector: Func[TSource, int, IEnumerable[TCollection]],
        resultSelector: Func[TSource, TCollection, TResult],
    ) -> IEnumerable[TResult]:
        """"""
    @classmethod
    @overload
    def SelectMany[TSource, TResult](
        cls, source: IEnumerable[TSource], selector: Func[TSource, int, IEnumerable[TResult]]
    ) -> IEnumerable[TResult]:
        """"""
    @classmethod
    @overload
    def SequenceEqual[TSource](
        cls, first: IEnumerable[TSource], second: IEnumerable[TSource]
    ) -> bool:
        """"""
    @classmethod
    @overload
    def SequenceEqual[TSource](
        cls,
        first: IEnumerable[TSource],
        second: IEnumerable[TSource],
        comparer: IEqualityComparer[TSource],
    ) -> bool:
        """"""
    @classmethod
    @overload
    def Single[TSource](cls, source: IEnumerable[TSource]) -> TSource:
        """"""
    @classmethod
    @overload
    def Single[TSource](
        cls, source: IEnumerable[TSource], predicate: Func[TSource, bool]
    ) -> TSource:
        """"""
    @classmethod
    @overload
    def SingleOrDefault[TSource](cls, source: IEnumerable[TSource]) -> TSource:
        """"""
    @classmethod
    @overload
    def SingleOrDefault[TSource](
        cls, source: IEnumerable[TSource], predicate: Func[TSource, bool]
    ) -> TSource:
        """"""
    @classmethod
    def Skip[TSource](cls, source: IEnumerable[TSource], count: int) -> IEnumerable[TSource]:
        """"""
    @classmethod
    @overload
    def SkipWhile[TSource](
        cls, source: IEnumerable[TSource], predicate: Func[TSource, bool]
    ) -> IEnumerable[TSource]:
        """"""
    @classmethod
    @overload
    def SkipWhile[TSource](
        cls, source: IEnumerable[TSource], predicate: Func[TSource, int, bool]
    ) -> IEnumerable[TSource]:
        """"""
    @classmethod
    @overload
    def Sum[TSource](
        cls, source: IEnumerable[TSource], selector: Func[TSource, Decimal | None]
    ) -> Decimal | None:
        """"""
    @classmethod
    @overload
    def Sum[TSource](
        cls, source: IEnumerable[TSource], selector: Func[TSource, Decimal]
    ) -> Decimal:
        """"""
    @classmethod
    @overload
    def Sum[TSource](
        cls, source: IEnumerable[TSource], selector: Func[TSource, float | None]
    ) -> float | None:
        """"""
    @classmethod
    @overload
    def Sum[TSource](cls, source: IEnumerable[TSource], selector: Func[TSource, float]) -> float:
        """"""
    @classmethod
    @overload
    def Sum[TSource](
        cls, source: IEnumerable[TSource], selector: Func[TSource, int | None]
    ) -> int | None:
        """"""
    @classmethod
    @overload
    def Sum[TSource](cls, source: IEnumerable[TSource], selector: Func[TSource, int]) -> int:
        """"""
    @classmethod
    @overload
    def Sum[TSource](
        cls, source: IEnumerable[TSource], selector: Func[TSource, int | None]
    ) -> int | None:
        """"""
    @classmethod
    @overload
    def Sum[TSource](cls, source: IEnumerable[TSource], selector: Func[TSource, int]) -> int:
        """"""
    @classmethod
    @overload
    def Sum[TSource](
        cls, source: IEnumerable[TSource], selector: Func[TSource, float | None]
    ) -> float | None:
        """"""
    @classmethod
    @overload
    def Sum[TSource](cls, source: IEnumerable[TSource], selector: Func[TSource, float]) -> float:
        """"""
    @classmethod
    @overload
    def Sum(cls, source: IEnumerable[Decimal | None]) -> Decimal | None:
        """"""
    @classmethod
    @overload
    def Sum(cls, source: IEnumerable[Decimal]) -> Decimal:
        """"""
    @classmethod
    @overload
    def Sum(cls, source: IEnumerable[float | None]) -> float | None:
        """"""
    @classmethod
    @overload
    def Sum(cls, source: IEnumerable[float]) -> float:
        """"""
    @classmethod
    @overload
    def Sum(cls, source: IEnumerable[int | None]) -> int | None:
        """"""
    @classmethod
    @overload
    def Sum(cls, source: IEnumerable[int]) -> int:
        """"""
    @classmethod
    @overload
    def Sum(cls, source: IEnumerable[int | None]) -> int | None:
        """"""
    @classmethod
    @overload
    def Sum(cls, source: IEnumerable[int]) -> int:
        """"""
    @classmethod
    @overload
    def Sum(cls, source: IEnumerable[float | None]) -> float | None:
        """"""
    @classmethod
    @overload
    def Sum(cls, source: IEnumerable[float]) -> float:
        """"""
    @classmethod
    def Take[TSource](cls, source: IEnumerable[TSource], count: int) -> IEnumerable[TSource]:
        """"""
    @classmethod
    @overload
    def TakeWhile[TSource](
        cls, source: IEnumerable[TSource], predicate: Func[TSource, bool]
    ) -> IEnumerable[TSource]:
        """"""
    @classmethod
    @overload
    def TakeWhile[TSource](
        cls, source: IEnumerable[TSource], predicate: Func[TSource, int, bool]
    ) -> IEnumerable[TSource]:
        """"""
    @classmethod
    @overload
    def ThenBy[TSource, TKey](
        cls, source: IOrderedEnumerable[TSource], keySelector: Func[TSource, TKey]
    ) -> IOrderedEnumerable[TSource]:
        """"""
    @classmethod
    @overload
    def ThenBy[TSource, TKey](
        cls,
        source: IOrderedEnumerable[TSource],
        keySelector: Func[TSource, TKey],
        comparer: IComparer[TKey],
    ) -> IOrderedEnumerable[TSource]:
        """"""
    @classmethod
    @overload
    def ThenByDescending[TSource, TKey](
        cls, source: IOrderedEnumerable[TSource], keySelector: Func[TSource, TKey]
    ) -> IOrderedEnumerable[TSource]:
        """"""
    @classmethod
    @overload
    def ThenByDescending[TSource, TKey](
        cls,
        source: IOrderedEnumerable[TSource],
        keySelector: Func[TSource, TKey],
        comparer: IComparer[TKey],
    ) -> IOrderedEnumerable[TSource]:
        """"""
    @classmethod
    def ToArray[TSource](cls, source: IEnumerable[TSource]) -> Array[TSource]:
        """"""
    @classmethod
    @overload
    def ToDictionary[TSource, TKey](
        cls, source: IEnumerable[TSource], keySelector: Func[TSource, TKey]
    ) -> Dictionary[TKey, TSource]:
        """"""
    @classmethod
    @overload
    def ToDictionary[TSource, TKey](
        cls,
        source: IEnumerable[TSource],
        keySelector: Func[TSource, TKey],
        comparer: IEqualityComparer[TKey],
    ) -> Dictionary[TKey, TSource]:
        """"""
    @classmethod
    @overload
    def ToDictionary[TSource, TKey, TElement](
        cls,
        source: IEnumerable[TSource],
        keySelector: Func[TSource, TKey],
        elementSelector: Func[TSource, TElement],
    ) -> Dictionary[TKey, TElement]:
        """"""
    @classmethod
    @overload
    def ToDictionary[TSource, TKey, TElement](
        cls,
        source: IEnumerable[TSource],
        keySelector: Func[TSource, TKey],
        elementSelector: Func[TSource, TElement],
        comparer: IEqualityComparer[TKey],
    ) -> Dictionary[TKey, TElement]:
        """"""
    @classmethod
    @overload
    def ToHashSet[TSource](cls, source: IEnumerable[TSource]) -> HashSet[TSource]:
        """"""
    @classmethod
    @overload
    def ToHashSet[TSource](
        cls, source: IEnumerable[TSource], comparer: IEqualityComparer[TSource]
    ) -> HashSet[TSource]:
        """"""
    @classmethod
    def ToList[TSource](cls, source: IEnumerable[TSource]) -> List[TSource]:
        """"""
    @classmethod
    @overload
    def ToLookup[TSource, TKey](
        cls, source: IEnumerable[TSource], keySelector: Func[TSource, TKey]
    ) -> ILookup[TKey, TSource]:
        """"""
    @classmethod
    @overload
    def ToLookup[TSource, TKey](
        cls,
        source: IEnumerable[TSource],
        keySelector: Func[TSource, TKey],
        comparer: IEqualityComparer[TKey],
    ) -> ILookup[TKey, TSource]:
        """"""
    @classmethod
    @overload
    def ToLookup[TSource, TKey, TElement](
        cls,
        source: IEnumerable[TSource],
        keySelector: Func[TSource, TKey],
        elementSelector: Func[TSource, TElement],
    ) -> ILookup[TKey, TElement]:
        """"""
    @classmethod
    @overload
    def ToLookup[TSource, TKey, TElement](
        cls,
        source: IEnumerable[TSource],
        keySelector: Func[TSource, TKey],
        elementSelector: Func[TSource, TElement],
        comparer: IEqualityComparer[TKey],
    ) -> ILookup[TKey, TElement]:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    @overload
    def Union[TSource](
        cls, first: IEnumerable[TSource], second: IEnumerable[TSource]
    ) -> IEnumerable[TSource]:
        """"""
    @classmethod
    @overload
    def Union[TSource](
        cls,
        first: IEnumerable[TSource],
        second: IEnumerable[TSource],
        comparer: IEqualityComparer[TSource],
    ) -> IEnumerable[TSource]:
        """"""
    @classmethod
    @overload
    def Where[TSource](
        cls, source: IEnumerable[TSource], predicate: Func[TSource, bool]
    ) -> IEnumerable[TSource]:
        """"""
    @classmethod
    @overload
    def Where[TSource](
        cls, source: IEnumerable[TSource], predicate: Func[TSource, int, bool]
    ) -> IEnumerable[TSource]:
        """"""
    @classmethod
    def Zip[TFirst, TSecond, TResult](
        cls,
        first: IEnumerable[TFirst],
        second: IEnumerable[TSecond],
        resultSelector: Func[TFirst, TSecond, TResult],
    ) -> IEnumerable[TResult]:
        """"""
    @overload
    def __contains__[TSource](self, source: IEnumerable[TSource], value: TSource) -> bool:
        """"""
    @overload
    def __contains__[TSource](
        self, source: IEnumerable[TSource], value: TSource, comparer: IEqualityComparer[TSource]
    ) -> bool:
        """"""

class EnumerableExecutor(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class EnumerableExecutor[T](EnumerableExecutor):
    """"""
    def __init__(self, expression: Expression) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class EnumerableQuery(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class EnumerableQuery[T](
    EnumerableQuery,
    IEnumerable[T],
    IEnumerable,
    IOrderedQueryable,
    IOrderedQueryable[T],
    IQueryProvider,
    IQueryable,
    IQueryable[T],
):
    """"""
    @overload
    def __init__(self, enumerable: IEnumerable[T]) -> None:
        """"""
    @overload
    def __init__(self, expression: Expression) -> None:
        """"""
    @property
    def ElementType(self) -> Type:
        """"""
    @property
    def Expression(self) -> Expression:
        """"""
    @property
    def Provider(self) -> IQueryProvider:
        """"""
    def CreateQuery(self, expression: Expression) -> IQueryable:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Execute(self, expression: Expression) -> object:
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

class EnumerableRewriter(OldExpressionVisitor):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class EnumerableSorter[TElement, TKey](EnumerableSorter[TElement]):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class EnumerableSorter[TElement](ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class Error(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class GroupedEnumerable[TSource, TKey, TElement, TResult](
    Object, IEnumerable[TResult], IEnumerable
):
    """"""
    def __init__(
        self,
        source: IEnumerable[TSource],
        keySelector: Func[TSource, TKey],
        elementSelector: Func[TSource, TElement],
        resultSelector: Func[TKey, IEnumerable[TElement], TResult],
        comparer: IEqualityComparer[TKey],
    ) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator[TResult](self) -> IEnumerator[TResult]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def __iter__[TResult](self) -> Iterator[TResult]:
        """"""

class GroupedEnumerable[TSource, TKey, TElement](
    Object, IEnumerable[IGrouping[TKey, TElement]], IEnumerable
):
    """"""
    def __init__(
        self,
        source: IEnumerable[TSource],
        keySelector: Func[TSource, TKey],
        elementSelector: Func[TSource, TElement],
        comparer: IEqualityComparer[TKey],
    ) -> None:
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
    def __iter__[TKey, TElement](self) -> Iterator[IGrouping[TKey, TElement]]:
        """"""

class IGrouping[TKey, TElement](ABC, IEnumerable[TElement], IEnumerable):
    """"""
    @property
    def Key(self) -> TKey:
        """"""
    def GetEnumerator[TElement](self) -> IEnumerator[TElement]:
        """"""
    def __iter__[TElement](self) -> Iterator[TElement]:
        """"""

class IIListProvider[TElement](ABC, IEnumerable[TElement], IEnumerable):
    """"""
    def GetCount(self, onlyIfCheap: bool) -> int:
        """"""
    def GetEnumerator[TElement](self) -> IEnumerator[TElement]:
        """"""
    def ToArray(self) -> Array[TElement]:
        """"""
    def ToList(self) -> List[TElement]:
        """"""
    def __iter__[TElement](self) -> Iterator[TElement]:
        """"""

class ILookup[TKey, TElement](ABC, IEnumerable[IGrouping[TKey, TElement]], IEnumerable):
    """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def Item(self) -> IEnumerable[TElement]:
        """"""
    def Contains(self, key: TKey) -> bool:
        """"""
    def GetEnumerator[TKey, TElement](self) -> IEnumerator[IGrouping[TKey, TElement]]:
        """"""
    def __contains__(self, key: TKey) -> bool:
        """"""
    def __iter__[TKey, TElement](self) -> Iterator[IGrouping[TKey, TElement]]:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, key: TKey) -> IEnumerable[TElement]:
        """"""

class IOrderedEnumerable[TElement](ABC, IEnumerable[TElement], IEnumerable):
    """"""
    def CreateOrderedEnumerable[TKey](
        self, keySelector: Func[TElement, TKey], comparer: IComparer[TKey], descending: bool
    ) -> IOrderedEnumerable[TElement]:
        """"""
    def GetEnumerator[TElement](self) -> IEnumerator[TElement]:
        """"""
    def __iter__[TElement](self) -> Iterator[TElement]:
        """"""

class IOrderedQueryable(ABC, IEnumerable, IQueryable):
    """"""
    @property
    def ElementType(self) -> Type:
        """"""
    @property
    def Expression(self) -> Expression:
        """"""
    @property
    def Provider(self) -> IQueryProvider:
        """"""
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def __iter__(self) -> Iterator:
        """"""

class IOrderedQueryable[T](
    ABC, IEnumerable[T], IEnumerable, IOrderedQueryable, IQueryable, IQueryable[T]
):
    """"""
    @property
    def ElementType(self) -> Type:
        """"""
    @property
    def Expression(self) -> Expression:
        """"""
    @property
    def Provider(self) -> IQueryProvider:
        """"""
    def GetEnumerator[T](self) -> IEnumerator[T]:
        """"""
    def __iter__[T](self) -> Iterator[T]:
        """"""

class IQueryProvider(ABC):
    """"""
    def CreateQuery[TElement](self, expression: Expression) -> IQueryable[TElement]:
        """"""
    def Execute[TResult](self, expression: Expression) -> TResult:
        """"""

class IQueryable(ABC, IEnumerable):
    """"""
    @property
    def ElementType(self) -> Type:
        """"""
    @property
    def Expression(self) -> Expression:
        """"""
    @property
    def Provider(self) -> IQueryProvider:
        """"""
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def __iter__(self) -> Iterator:
        """"""

class IQueryable[T](ABC, IEnumerable[T], IEnumerable, IQueryable):
    """"""
    @property
    def ElementType(self) -> Type:
        """"""
    @property
    def Expression(self) -> Expression:
        """"""
    @property
    def Provider(self) -> IQueryProvider:
        """"""
    def GetEnumerator[T](self) -> IEnumerator[T]:
        """"""
    def __iter__[T](self) -> Iterator[T]:
        """"""

class IdentityFunction[TElement](Object):
    """"""
    def __init__(self) -> None:
        """"""
    @classmethod
    @property
    def Instance(cls) -> Func[TElement, TElement]:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

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
    def ApplyResultSelector[TResult](
        self, resultSelector: Func[TKey, IEnumerable[TElement], TResult]
    ) -> IEnumerable[TResult]:
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

class OrderedEnumerable[TElement, TKey](
    OrderedEnumerable[TElement], IEnumerable[TElement], IEnumerable, IOrderedEnumerable[TElement]
):
    """"""
    def CreateOrderedEnumerable[TKey](
        self, keySelector: Func[TElement, TKey], comparer: IComparer[TKey], descending: bool
    ) -> IOrderedEnumerable[TElement]:
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

class OrderedEnumerable[TElement](
    ABC, Object, IEnumerable[TElement], IEnumerable, IOrderedEnumerable[TElement]
):
    """"""
    def CreateOrderedEnumerable[TKey](
        self, keySelector: Func[TElement, TKey], comparer: IComparer[TKey], descending: bool
    ) -> IOrderedEnumerable[TElement]:
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

class OrderedParallelQuery[TSource](ParallelQuery[TSource], IEnumerable[TSource], IEnumerable):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator[TSource](self) -> IEnumerator[TSource]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def __iter__[TSource](self) -> Iterator[TSource]:
        """"""

class ParallelEnumerable(ABC, Object):
    """"""
    @classmethod
    @overload
    def Aggregate[TSource, TAccumulate](
        cls,
        source: ParallelQuery[TSource],
        seed: TAccumulate,
        func: Func[TAccumulate, TSource, TAccumulate],
    ) -> TAccumulate:
        """"""
    @classmethod
    @overload
    def Aggregate[TSource, TAccumulate, TResult](
        cls,
        source: ParallelQuery[TSource],
        seed: TAccumulate,
        updateAccumulatorFunc: Func[TAccumulate, TSource, TAccumulate],
        combineAccumulatorsFunc: Func[TAccumulate, TAccumulate, TAccumulate],
        resultSelector: Func[TAccumulate, TResult],
    ) -> TResult:
        """"""
    @classmethod
    @overload
    def Aggregate[TSource, TAccumulate, TResult](
        cls,
        source: ParallelQuery[TSource],
        seed: TAccumulate,
        func: Func[TAccumulate, TSource, TAccumulate],
        resultSelector: Func[TAccumulate, TResult],
    ) -> TResult:
        """"""
    @classmethod
    @overload
    def Aggregate[TSource, TAccumulate, TResult](
        cls,
        source: ParallelQuery[TSource],
        seedFactory: Func[TAccumulate],
        updateAccumulatorFunc: Func[TAccumulate, TSource, TAccumulate],
        combineAccumulatorsFunc: Func[TAccumulate, TAccumulate, TAccumulate],
        resultSelector: Func[TAccumulate, TResult],
    ) -> TResult:
        """"""
    @classmethod
    @overload
    def Aggregate[TSource](
        cls, source: ParallelQuery[TSource], func: Func[TSource, TSource, TSource]
    ) -> TSource:
        """"""
    @classmethod
    def All[TSource](cls, source: ParallelQuery[TSource], predicate: Func[TSource, bool]) -> bool:
        """"""
    @classmethod
    @overload
    def Any[TSource](cls, source: ParallelQuery[TSource]) -> bool:
        """"""
    @classmethod
    @overload
    def Any[TSource](cls, source: ParallelQuery[TSource], predicate: Func[TSource, bool]) -> bool:
        """"""
    @classmethod
    def AsEnumerable[TSource](cls, source: ParallelQuery[TSource]) -> IEnumerable[TSource]:
        """"""
    @classmethod
    @overload
    def AsOrdered(cls, source: ParallelQuery) -> ParallelQuery:
        """"""
    @classmethod
    @overload
    def AsOrdered[TSource](cls, source: ParallelQuery[TSource]) -> ParallelQuery[TSource]:
        """"""
    @classmethod
    @overload
    def AsParallel[TSource](cls, source: Partitioner[TSource]) -> ParallelQuery[TSource]:
        """"""
    @classmethod
    @overload
    def AsParallel[TSource](cls, source: IEnumerable[TSource]) -> ParallelQuery[TSource]:
        """"""
    @classmethod
    @overload
    def AsParallel(cls, source: IEnumerable) -> ParallelQuery:
        """"""
    @classmethod
    def AsSequential[TSource](cls, source: ParallelQuery[TSource]) -> IEnumerable[TSource]:
        """"""
    @classmethod
    def AsUnordered[TSource](cls, source: ParallelQuery[TSource]) -> ParallelQuery[TSource]:
        """"""
    @classmethod
    @overload
    def Average[TSource](
        cls, source: ParallelQuery[TSource], selector: Func[TSource, Decimal | None]
    ) -> Decimal | None:
        """"""
    @classmethod
    @overload
    def Average[TSource](
        cls, source: ParallelQuery[TSource], selector: Func[TSource, Decimal]
    ) -> Decimal:
        """"""
    @classmethod
    @overload
    def Average[TSource](
        cls, source: ParallelQuery[TSource], selector: Func[TSource, float | None]
    ) -> float | None:
        """"""
    @classmethod
    @overload
    def Average[TSource](
        cls, source: ParallelQuery[TSource], selector: Func[TSource, float]
    ) -> float:
        """"""
    @classmethod
    @overload
    def Average[TSource](
        cls, source: ParallelQuery[TSource], selector: Func[TSource, int | None]
    ) -> float | None:
        """"""
    @classmethod
    @overload
    def Average[TSource](
        cls, source: ParallelQuery[TSource], selector: Func[TSource, int]
    ) -> float:
        """"""
    @classmethod
    @overload
    def Average[TSource](
        cls, source: ParallelQuery[TSource], selector: Func[TSource, int | None]
    ) -> float | None:
        """"""
    @classmethod
    @overload
    def Average[TSource](
        cls, source: ParallelQuery[TSource], selector: Func[TSource, int]
    ) -> float:
        """"""
    @classmethod
    @overload
    def Average[TSource](
        cls, source: ParallelQuery[TSource], selector: Func[TSource, float | None]
    ) -> float | None:
        """"""
    @classmethod
    @overload
    def Average[TSource](
        cls, source: ParallelQuery[TSource], selector: Func[TSource, float]
    ) -> float:
        """"""
    @classmethod
    @overload
    def Average(cls, source: ParallelQuery[Decimal | None]) -> Decimal | None:
        """"""
    @classmethod
    @overload
    def Average(cls, source: ParallelQuery[Decimal]) -> Decimal:
        """"""
    @classmethod
    @overload
    def Average(cls, source: ParallelQuery[float | None]) -> float | None:
        """"""
    @classmethod
    @overload
    def Average(cls, source: ParallelQuery[float]) -> float:
        """"""
    @classmethod
    @overload
    def Average(cls, source: ParallelQuery[int | None]) -> float | None:
        """"""
    @classmethod
    @overload
    def Average(cls, source: ParallelQuery[int]) -> float:
        """"""
    @classmethod
    @overload
    def Average(cls, source: ParallelQuery[int | None]) -> float | None:
        """"""
    @classmethod
    @overload
    def Average(cls, source: ParallelQuery[int]) -> float:
        """"""
    @classmethod
    @overload
    def Average(cls, source: ParallelQuery[float | None]) -> float | None:
        """"""
    @classmethod
    @overload
    def Average(cls, source: ParallelQuery[float]) -> float:
        """"""
    @classmethod
    def Cast[TResult](cls, source: ParallelQuery) -> ParallelQuery[TResult]:
        """"""
    @classmethod
    @overload
    def Concat[TSource](
        cls, first: ParallelQuery[TSource], second: IEnumerable[TSource]
    ) -> ParallelQuery[TSource]:
        """"""
    @classmethod
    @overload
    def Concat[TSource](
        cls, first: ParallelQuery[TSource], second: ParallelQuery[TSource]
    ) -> ParallelQuery[TSource]:
        """"""
    @classmethod
    @overload
    def Contains[TSource](cls, source: ParallelQuery[TSource], value: TSource) -> bool:
        """"""
    @classmethod
    @overload
    def Contains[TSource](
        cls, source: ParallelQuery[TSource], value: TSource, comparer: IEqualityComparer[TSource]
    ) -> bool:
        """"""
    @classmethod
    @overload
    def Count[TSource](cls, source: ParallelQuery[TSource]) -> int:
        """"""
    @classmethod
    @overload
    def Count[TSource](cls, source: ParallelQuery[TSource], predicate: Func[TSource, bool]) -> int:
        """"""
    @classmethod
    @overload
    def DefaultIfEmpty[TSource](cls, source: ParallelQuery[TSource]) -> ParallelQuery[TSource]:
        """"""
    @classmethod
    @overload
    def DefaultIfEmpty[TSource](
        cls, source: ParallelQuery[TSource], defaultValue: TSource
    ) -> ParallelQuery[TSource]:
        """"""
    @classmethod
    @overload
    def Distinct[TSource](cls, source: ParallelQuery[TSource]) -> ParallelQuery[TSource]:
        """"""
    @classmethod
    @overload
    def Distinct[TSource](
        cls, source: ParallelQuery[TSource], comparer: IEqualityComparer[TSource]
    ) -> ParallelQuery[TSource]:
        """"""
    @classmethod
    def ElementAt[TSource](cls, source: ParallelQuery[TSource], index: int) -> TSource:
        """"""
    @classmethod
    def ElementAtOrDefault[TSource](cls, source: ParallelQuery[TSource], index: int) -> TSource:
        """"""
    @classmethod
    def Empty[TResult](cls) -> ParallelQuery[TResult]:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    @overload
    def Except[TSource](
        cls, first: ParallelQuery[TSource], second: IEnumerable[TSource]
    ) -> ParallelQuery[TSource]:
        """"""
    @classmethod
    @overload
    def Except[TSource](
        cls,
        first: ParallelQuery[TSource],
        second: IEnumerable[TSource],
        comparer: IEqualityComparer[TSource],
    ) -> ParallelQuery[TSource]:
        """"""
    @classmethod
    @overload
    def Except[TSource](
        cls, first: ParallelQuery[TSource], second: ParallelQuery[TSource]
    ) -> ParallelQuery[TSource]:
        """"""
    @classmethod
    @overload
    def Except[TSource](
        cls,
        first: ParallelQuery[TSource],
        second: ParallelQuery[TSource],
        comparer: IEqualityComparer[TSource],
    ) -> ParallelQuery[TSource]:
        """"""
    @classmethod
    @overload
    def First[TSource](cls, source: ParallelQuery[TSource]) -> TSource:
        """"""
    @classmethod
    @overload
    def First[TSource](
        cls, source: ParallelQuery[TSource], predicate: Func[TSource, bool]
    ) -> TSource:
        """"""
    @classmethod
    @overload
    def FirstOrDefault[TSource](cls, source: ParallelQuery[TSource]) -> TSource:
        """"""
    @classmethod
    @overload
    def FirstOrDefault[TSource](
        cls, source: ParallelQuery[TSource], predicate: Func[TSource, bool]
    ) -> TSource:
        """"""
    @classmethod
    def ForAll[TSource](cls, source: ParallelQuery[TSource], action: Action[TSource]) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    @overload
    def GroupBy[TSource, TKey](
        cls, source: ParallelQuery[TSource], keySelector: Func[TSource, TKey]
    ) -> ParallelQuery[IGrouping[TKey, TSource]]:
        """"""
    @classmethod
    @overload
    def GroupBy[TSource, TKey](
        cls,
        source: ParallelQuery[TSource],
        keySelector: Func[TSource, TKey],
        comparer: IEqualityComparer[TKey],
    ) -> ParallelQuery[IGrouping[TKey, TSource]]:
        """"""
    @classmethod
    @overload
    def GroupBy[TSource, TKey, TResult](
        cls,
        source: ParallelQuery[TSource],
        keySelector: Func[TSource, TKey],
        resultSelector: Func[TKey, IEnumerable[TSource], TResult],
    ) -> ParallelQuery[TResult]:
        """"""
    @classmethod
    @overload
    def GroupBy[TSource, TKey, TResult](
        cls,
        source: ParallelQuery[TSource],
        keySelector: Func[TSource, TKey],
        resultSelector: Func[TKey, IEnumerable[TSource], TResult],
        comparer: IEqualityComparer[TKey],
    ) -> ParallelQuery[TResult]:
        """"""
    @classmethod
    @overload
    def GroupBy[TSource, TKey, TElement](
        cls,
        source: ParallelQuery[TSource],
        keySelector: Func[TSource, TKey],
        elementSelector: Func[TSource, TElement],
    ) -> ParallelQuery[IGrouping[TKey, TElement]]:
        """"""
    @classmethod
    @overload
    def GroupBy[TSource, TKey, TElement](
        cls,
        source: ParallelQuery[TSource],
        keySelector: Func[TSource, TKey],
        elementSelector: Func[TSource, TElement],
        comparer: IEqualityComparer[TKey],
    ) -> ParallelQuery[IGrouping[TKey, TElement]]:
        """"""
    @classmethod
    @overload
    def GroupBy[TSource, TKey, TElement, TResult](
        cls,
        source: ParallelQuery[TSource],
        keySelector: Func[TSource, TKey],
        elementSelector: Func[TSource, TElement],
        resultSelector: Func[TKey, IEnumerable[TElement], TResult],
    ) -> ParallelQuery[TResult]:
        """"""
    @classmethod
    @overload
    def GroupBy[TSource, TKey, TElement, TResult](
        cls,
        source: ParallelQuery[TSource],
        keySelector: Func[TSource, TKey],
        elementSelector: Func[TSource, TElement],
        resultSelector: Func[TKey, IEnumerable[TElement], TResult],
        comparer: IEqualityComparer[TKey],
    ) -> ParallelQuery[TResult]:
        """"""
    @classmethod
    @overload
    def GroupJoin[TOuter, TInner, TKey, TResult](
        cls,
        outer: ParallelQuery[TOuter],
        inner: IEnumerable[TInner],
        outerKeySelector: Func[TOuter, TKey],
        innerKeySelector: Func[TInner, TKey],
        resultSelector: Func[TOuter, IEnumerable[TInner], TResult],
    ) -> ParallelQuery[TResult]:
        """"""
    @classmethod
    @overload
    def GroupJoin[TOuter, TInner, TKey, TResult](
        cls,
        outer: ParallelQuery[TOuter],
        inner: IEnumerable[TInner],
        outerKeySelector: Func[TOuter, TKey],
        innerKeySelector: Func[TInner, TKey],
        resultSelector: Func[TOuter, IEnumerable[TInner], TResult],
        comparer: IEqualityComparer[TKey],
    ) -> ParallelQuery[TResult]:
        """"""
    @classmethod
    @overload
    def GroupJoin[TOuter, TInner, TKey, TResult](
        cls,
        outer: ParallelQuery[TOuter],
        inner: ParallelQuery[TInner],
        outerKeySelector: Func[TOuter, TKey],
        innerKeySelector: Func[TInner, TKey],
        resultSelector: Func[TOuter, IEnumerable[TInner], TResult],
    ) -> ParallelQuery[TResult]:
        """"""
    @classmethod
    @overload
    def GroupJoin[TOuter, TInner, TKey, TResult](
        cls,
        outer: ParallelQuery[TOuter],
        inner: ParallelQuery[TInner],
        outerKeySelector: Func[TOuter, TKey],
        innerKeySelector: Func[TInner, TKey],
        resultSelector: Func[TOuter, IEnumerable[TInner], TResult],
        comparer: IEqualityComparer[TKey],
    ) -> ParallelQuery[TResult]:
        """"""
    @classmethod
    @overload
    def Intersect[TSource](
        cls, first: ParallelQuery[TSource], second: IEnumerable[TSource]
    ) -> ParallelQuery[TSource]:
        """"""
    @classmethod
    @overload
    def Intersect[TSource](
        cls,
        first: ParallelQuery[TSource],
        second: IEnumerable[TSource],
        comparer: IEqualityComparer[TSource],
    ) -> ParallelQuery[TSource]:
        """"""
    @classmethod
    @overload
    def Intersect[TSource](
        cls, first: ParallelQuery[TSource], second: ParallelQuery[TSource]
    ) -> ParallelQuery[TSource]:
        """"""
    @classmethod
    @overload
    def Intersect[TSource](
        cls,
        first: ParallelQuery[TSource],
        second: ParallelQuery[TSource],
        comparer: IEqualityComparer[TSource],
    ) -> ParallelQuery[TSource]:
        """"""
    @classmethod
    @overload
    def Join[TOuter, TInner, TKey, TResult](
        cls,
        outer: ParallelQuery[TOuter],
        inner: IEnumerable[TInner],
        outerKeySelector: Func[TOuter, TKey],
        innerKeySelector: Func[TInner, TKey],
        resultSelector: Func[TOuter, TInner, TResult],
    ) -> ParallelQuery[TResult]:
        """"""
    @classmethod
    @overload
    def Join[TOuter, TInner, TKey, TResult](
        cls,
        outer: ParallelQuery[TOuter],
        inner: IEnumerable[TInner],
        outerKeySelector: Func[TOuter, TKey],
        innerKeySelector: Func[TInner, TKey],
        resultSelector: Func[TOuter, TInner, TResult],
        comparer: IEqualityComparer[TKey],
    ) -> ParallelQuery[TResult]:
        """"""
    @classmethod
    @overload
    def Join[TOuter, TInner, TKey, TResult](
        cls,
        outer: ParallelQuery[TOuter],
        inner: ParallelQuery[TInner],
        outerKeySelector: Func[TOuter, TKey],
        innerKeySelector: Func[TInner, TKey],
        resultSelector: Func[TOuter, TInner, TResult],
    ) -> ParallelQuery[TResult]:
        """"""
    @classmethod
    @overload
    def Join[TOuter, TInner, TKey, TResult](
        cls,
        outer: ParallelQuery[TOuter],
        inner: ParallelQuery[TInner],
        outerKeySelector: Func[TOuter, TKey],
        innerKeySelector: Func[TInner, TKey],
        resultSelector: Func[TOuter, TInner, TResult],
        comparer: IEqualityComparer[TKey],
    ) -> ParallelQuery[TResult]:
        """"""
    @classmethod
    @overload
    def Last[TSource](cls, source: ParallelQuery[TSource]) -> TSource:
        """"""
    @classmethod
    @overload
    def Last[TSource](
        cls, source: ParallelQuery[TSource], predicate: Func[TSource, bool]
    ) -> TSource:
        """"""
    @classmethod
    @overload
    def LastOrDefault[TSource](cls, source: ParallelQuery[TSource]) -> TSource:
        """"""
    @classmethod
    @overload
    def LastOrDefault[TSource](
        cls, source: ParallelQuery[TSource], predicate: Func[TSource, bool]
    ) -> TSource:
        """"""
    @classmethod
    @overload
    def LongCount[TSource](cls, source: ParallelQuery[TSource]) -> int:
        """"""
    @classmethod
    @overload
    def LongCount[TSource](
        cls, source: ParallelQuery[TSource], predicate: Func[TSource, bool]
    ) -> int:
        """"""
    @classmethod
    @overload
    def Max[TSource](cls, source: ParallelQuery[TSource]) -> TSource:
        """"""
    @classmethod
    @overload
    def Max[TSource, TResult](
        cls, source: ParallelQuery[TSource], selector: Func[TSource, TResult]
    ) -> TResult:
        """"""
    @classmethod
    @overload
    def Max[TSource](
        cls, source: ParallelQuery[TSource], selector: Func[TSource, Decimal | None]
    ) -> Decimal | None:
        """"""
    @classmethod
    @overload
    def Max[TSource](
        cls, source: ParallelQuery[TSource], selector: Func[TSource, Decimal]
    ) -> Decimal:
        """"""
    @classmethod
    @overload
    def Max[TSource](
        cls, source: ParallelQuery[TSource], selector: Func[TSource, float | None]
    ) -> float | None:
        """"""
    @classmethod
    @overload
    def Max[TSource](cls, source: ParallelQuery[TSource], selector: Func[TSource, float]) -> float:
        """"""
    @classmethod
    @overload
    def Max[TSource](
        cls, source: ParallelQuery[TSource], selector: Func[TSource, int | None]
    ) -> int | None:
        """"""
    @classmethod
    @overload
    def Max[TSource](cls, source: ParallelQuery[TSource], selector: Func[TSource, int]) -> int:
        """"""
    @classmethod
    @overload
    def Max[TSource](
        cls, source: ParallelQuery[TSource], selector: Func[TSource, int | None]
    ) -> int | None:
        """"""
    @classmethod
    @overload
    def Max[TSource](cls, source: ParallelQuery[TSource], selector: Func[TSource, int]) -> int:
        """"""
    @classmethod
    @overload
    def Max[TSource](
        cls, source: ParallelQuery[TSource], selector: Func[TSource, float | None]
    ) -> float | None:
        """"""
    @classmethod
    @overload
    def Max[TSource](cls, source: ParallelQuery[TSource], selector: Func[TSource, float]) -> float:
        """"""
    @classmethod
    @overload
    def Max(cls, source: ParallelQuery[Decimal | None]) -> Decimal | None:
        """"""
    @classmethod
    @overload
    def Max(cls, source: ParallelQuery[Decimal]) -> Decimal:
        """"""
    @classmethod
    @overload
    def Max(cls, source: ParallelQuery[float | None]) -> float | None:
        """"""
    @classmethod
    @overload
    def Max(cls, source: ParallelQuery[float]) -> float:
        """"""
    @classmethod
    @overload
    def Max(cls, source: ParallelQuery[int | None]) -> int | None:
        """"""
    @classmethod
    @overload
    def Max(cls, source: ParallelQuery[int]) -> int:
        """"""
    @classmethod
    @overload
    def Max(cls, source: ParallelQuery[int | None]) -> int | None:
        """"""
    @classmethod
    @overload
    def Max(cls, source: ParallelQuery[int]) -> int:
        """"""
    @classmethod
    @overload
    def Max(cls, source: ParallelQuery[float | None]) -> float | None:
        """"""
    @classmethod
    @overload
    def Max(cls, source: ParallelQuery[float]) -> float:
        """"""
    @classmethod
    @overload
    def Min[TSource](cls, source: ParallelQuery[TSource]) -> TSource:
        """"""
    @classmethod
    @overload
    def Min[TSource, TResult](
        cls, source: ParallelQuery[TSource], selector: Func[TSource, TResult]
    ) -> TResult:
        """"""
    @classmethod
    @overload
    def Min[TSource](
        cls, source: ParallelQuery[TSource], selector: Func[TSource, Decimal | None]
    ) -> Decimal | None:
        """"""
    @classmethod
    @overload
    def Min[TSource](
        cls, source: ParallelQuery[TSource], selector: Func[TSource, Decimal]
    ) -> Decimal:
        """"""
    @classmethod
    @overload
    def Min[TSource](
        cls, source: ParallelQuery[TSource], selector: Func[TSource, float | None]
    ) -> float | None:
        """"""
    @classmethod
    @overload
    def Min[TSource](cls, source: ParallelQuery[TSource], selector: Func[TSource, float]) -> float:
        """"""
    @classmethod
    @overload
    def Min[TSource](
        cls, source: ParallelQuery[TSource], selector: Func[TSource, int | None]
    ) -> int | None:
        """"""
    @classmethod
    @overload
    def Min[TSource](cls, source: ParallelQuery[TSource], selector: Func[TSource, int]) -> int:
        """"""
    @classmethod
    @overload
    def Min[TSource](
        cls, source: ParallelQuery[TSource], selector: Func[TSource, int | None]
    ) -> int | None:
        """"""
    @classmethod
    @overload
    def Min[TSource](cls, source: ParallelQuery[TSource], selector: Func[TSource, int]) -> int:
        """"""
    @classmethod
    @overload
    def Min[TSource](
        cls, source: ParallelQuery[TSource], selector: Func[TSource, float | None]
    ) -> float | None:
        """"""
    @classmethod
    @overload
    def Min[TSource](cls, source: ParallelQuery[TSource], selector: Func[TSource, float]) -> float:
        """"""
    @classmethod
    @overload
    def Min(cls, source: ParallelQuery[Decimal | None]) -> Decimal | None:
        """"""
    @classmethod
    @overload
    def Min(cls, source: ParallelQuery[Decimal]) -> Decimal:
        """"""
    @classmethod
    @overload
    def Min(cls, source: ParallelQuery[float | None]) -> float | None:
        """"""
    @classmethod
    @overload
    def Min(cls, source: ParallelQuery[float]) -> float:
        """"""
    @classmethod
    @overload
    def Min(cls, source: ParallelQuery[int | None]) -> int | None:
        """"""
    @classmethod
    @overload
    def Min(cls, source: ParallelQuery[int]) -> int:
        """"""
    @classmethod
    @overload
    def Min(cls, source: ParallelQuery[int | None]) -> int | None:
        """"""
    @classmethod
    @overload
    def Min(cls, source: ParallelQuery[int]) -> int:
        """"""
    @classmethod
    @overload
    def Min(cls, source: ParallelQuery[float | None]) -> float | None:
        """"""
    @classmethod
    @overload
    def Min(cls, source: ParallelQuery[float]) -> float:
        """"""
    @classmethod
    def OfType[TResult](cls, source: ParallelQuery) -> ParallelQuery[TResult]:
        """"""
    @classmethod
    @overload
    def OrderBy[TSource, TKey](
        cls, source: ParallelQuery[TSource], keySelector: Func[TSource, TKey]
    ) -> OrderedParallelQuery[TSource]:
        """"""
    @classmethod
    @overload
    def OrderBy[TSource, TKey](
        cls,
        source: ParallelQuery[TSource],
        keySelector: Func[TSource, TKey],
        comparer: IComparer[TKey],
    ) -> OrderedParallelQuery[TSource]:
        """"""
    @classmethod
    @overload
    def OrderByDescending[TSource, TKey](
        cls, source: ParallelQuery[TSource], keySelector: Func[TSource, TKey]
    ) -> OrderedParallelQuery[TSource]:
        """"""
    @classmethod
    @overload
    def OrderByDescending[TSource, TKey](
        cls,
        source: ParallelQuery[TSource],
        keySelector: Func[TSource, TKey],
        comparer: IComparer[TKey],
    ) -> OrderedParallelQuery[TSource]:
        """"""
    @classmethod
    def Range(cls, start: int, count: int) -> ParallelQuery[int]:
        """"""
    @classmethod
    def Repeat[TResult](cls, element: TResult, count: int) -> ParallelQuery[TResult]:
        """"""
    @classmethod
    def Reverse[TSource](cls, source: ParallelQuery[TSource]) -> ParallelQuery[TSource]:
        """"""
    @classmethod
    @overload
    def Select[TSource, TResult](
        cls, source: ParallelQuery[TSource], selector: Func[TSource, TResult]
    ) -> ParallelQuery[TResult]:
        """"""
    @classmethod
    @overload
    def Select[TSource, TResult](
        cls, source: ParallelQuery[TSource], selector: Func[TSource, int, TResult]
    ) -> ParallelQuery[TResult]:
        """"""
    @classmethod
    @overload
    def SelectMany[TSource, TCollection, TResult](
        cls,
        source: ParallelQuery[TSource],
        collectionSelector: Func[TSource, IEnumerable[TCollection]],
        resultSelector: Func[TSource, TCollection, TResult],
    ) -> ParallelQuery[TResult]:
        """"""
    @classmethod
    @overload
    def SelectMany[TSource, TResult](
        cls, source: ParallelQuery[TSource], selector: Func[TSource, IEnumerable[TResult]]
    ) -> ParallelQuery[TResult]:
        """"""
    @classmethod
    @overload
    def SelectMany[TSource, TCollection, TResult](
        cls,
        source: ParallelQuery[TSource],
        collectionSelector: Func[TSource, int, IEnumerable[TCollection]],
        resultSelector: Func[TSource, TCollection, TResult],
    ) -> ParallelQuery[TResult]:
        """"""
    @classmethod
    @overload
    def SelectMany[TSource, TResult](
        cls, source: ParallelQuery[TSource], selector: Func[TSource, int, IEnumerable[TResult]]
    ) -> ParallelQuery[TResult]:
        """"""
    @classmethod
    @overload
    def SequenceEqual[TSource](
        cls, first: ParallelQuery[TSource], second: IEnumerable[TSource]
    ) -> bool:
        """"""
    @classmethod
    @overload
    def SequenceEqual[TSource](
        cls,
        first: ParallelQuery[TSource],
        second: IEnumerable[TSource],
        comparer: IEqualityComparer[TSource],
    ) -> bool:
        """"""
    @classmethod
    @overload
    def SequenceEqual[TSource](
        cls, first: ParallelQuery[TSource], second: ParallelQuery[TSource]
    ) -> bool:
        """"""
    @classmethod
    @overload
    def SequenceEqual[TSource](
        cls,
        first: ParallelQuery[TSource],
        second: ParallelQuery[TSource],
        comparer: IEqualityComparer[TSource],
    ) -> bool:
        """"""
    @classmethod
    @overload
    def Single[TSource](cls, source: ParallelQuery[TSource]) -> TSource:
        """"""
    @classmethod
    @overload
    def Single[TSource](
        cls, source: ParallelQuery[TSource], predicate: Func[TSource, bool]
    ) -> TSource:
        """"""
    @classmethod
    @overload
    def SingleOrDefault[TSource](cls, source: ParallelQuery[TSource]) -> TSource:
        """"""
    @classmethod
    @overload
    def SingleOrDefault[TSource](
        cls, source: ParallelQuery[TSource], predicate: Func[TSource, bool]
    ) -> TSource:
        """"""
    @classmethod
    def Skip[TSource](cls, source: ParallelQuery[TSource], count: int) -> ParallelQuery[TSource]:
        """"""
    @classmethod
    @overload
    def SkipWhile[TSource](
        cls, source: ParallelQuery[TSource], predicate: Func[TSource, bool]
    ) -> ParallelQuery[TSource]:
        """"""
    @classmethod
    @overload
    def SkipWhile[TSource](
        cls, source: ParallelQuery[TSource], predicate: Func[TSource, int, bool]
    ) -> ParallelQuery[TSource]:
        """"""
    @classmethod
    @overload
    def Sum[TSource](
        cls, source: ParallelQuery[TSource], selector: Func[TSource, Decimal | None]
    ) -> Decimal | None:
        """"""
    @classmethod
    @overload
    def Sum[TSource](
        cls, source: ParallelQuery[TSource], selector: Func[TSource, Decimal]
    ) -> Decimal:
        """"""
    @classmethod
    @overload
    def Sum[TSource](
        cls, source: ParallelQuery[TSource], selector: Func[TSource, float | None]
    ) -> float | None:
        """"""
    @classmethod
    @overload
    def Sum[TSource](cls, source: ParallelQuery[TSource], selector: Func[TSource, float]) -> float:
        """"""
    @classmethod
    @overload
    def Sum[TSource](
        cls, source: ParallelQuery[TSource], selector: Func[TSource, int | None]
    ) -> int | None:
        """"""
    @classmethod
    @overload
    def Sum[TSource](cls, source: ParallelQuery[TSource], selector: Func[TSource, int]) -> int:
        """"""
    @classmethod
    @overload
    def Sum[TSource](
        cls, source: ParallelQuery[TSource], selector: Func[TSource, int | None]
    ) -> int | None:
        """"""
    @classmethod
    @overload
    def Sum[TSource](cls, source: ParallelQuery[TSource], selector: Func[TSource, int]) -> int:
        """"""
    @classmethod
    @overload
    def Sum[TSource](
        cls, source: ParallelQuery[TSource], selector: Func[TSource, float | None]
    ) -> float | None:
        """"""
    @classmethod
    @overload
    def Sum[TSource](cls, source: ParallelQuery[TSource], selector: Func[TSource, float]) -> float:
        """"""
    @classmethod
    @overload
    def Sum(cls, source: ParallelQuery[Decimal | None]) -> Decimal | None:
        """"""
    @classmethod
    @overload
    def Sum(cls, source: ParallelQuery[Decimal]) -> Decimal:
        """"""
    @classmethod
    @overload
    def Sum(cls, source: ParallelQuery[float | None]) -> float | None:
        """"""
    @classmethod
    @overload
    def Sum(cls, source: ParallelQuery[float]) -> float:
        """"""
    @classmethod
    @overload
    def Sum(cls, source: ParallelQuery[int | None]) -> int | None:
        """"""
    @classmethod
    @overload
    def Sum(cls, source: ParallelQuery[int]) -> int:
        """"""
    @classmethod
    @overload
    def Sum(cls, source: ParallelQuery[int | None]) -> int | None:
        """"""
    @classmethod
    @overload
    def Sum(cls, source: ParallelQuery[int]) -> int:
        """"""
    @classmethod
    @overload
    def Sum(cls, source: ParallelQuery[float | None]) -> float | None:
        """"""
    @classmethod
    @overload
    def Sum(cls, source: ParallelQuery[float]) -> float:
        """"""
    @classmethod
    def Take[TSource](cls, source: ParallelQuery[TSource], count: int) -> ParallelQuery[TSource]:
        """"""
    @classmethod
    @overload
    def TakeWhile[TSource](
        cls, source: ParallelQuery[TSource], predicate: Func[TSource, bool]
    ) -> ParallelQuery[TSource]:
        """"""
    @classmethod
    @overload
    def TakeWhile[TSource](
        cls, source: ParallelQuery[TSource], predicate: Func[TSource, int, bool]
    ) -> ParallelQuery[TSource]:
        """"""
    @classmethod
    @overload
    def ThenBy[TSource, TKey](
        cls, source: OrderedParallelQuery[TSource], keySelector: Func[TSource, TKey]
    ) -> OrderedParallelQuery[TSource]:
        """"""
    @classmethod
    @overload
    def ThenBy[TSource, TKey](
        cls,
        source: OrderedParallelQuery[TSource],
        keySelector: Func[TSource, TKey],
        comparer: IComparer[TKey],
    ) -> OrderedParallelQuery[TSource]:
        """"""
    @classmethod
    @overload
    def ThenByDescending[TSource, TKey](
        cls, source: OrderedParallelQuery[TSource], keySelector: Func[TSource, TKey]
    ) -> OrderedParallelQuery[TSource]:
        """"""
    @classmethod
    @overload
    def ThenByDescending[TSource, TKey](
        cls,
        source: OrderedParallelQuery[TSource],
        keySelector: Func[TSource, TKey],
        comparer: IComparer[TKey],
    ) -> OrderedParallelQuery[TSource]:
        """"""
    @classmethod
    def ToArray[TSource](cls, source: ParallelQuery[TSource]) -> Array[TSource]:
        """"""
    @classmethod
    @overload
    def ToDictionary[TSource, TKey](
        cls, source: ParallelQuery[TSource], keySelector: Func[TSource, TKey]
    ) -> Dictionary[TKey, TSource]:
        """"""
    @classmethod
    @overload
    def ToDictionary[TSource, TKey](
        cls,
        source: ParallelQuery[TSource],
        keySelector: Func[TSource, TKey],
        comparer: IEqualityComparer[TKey],
    ) -> Dictionary[TKey, TSource]:
        """"""
    @classmethod
    @overload
    def ToDictionary[TSource, TKey, TElement](
        cls,
        source: ParallelQuery[TSource],
        keySelector: Func[TSource, TKey],
        elementSelector: Func[TSource, TElement],
    ) -> Dictionary[TKey, TElement]:
        """"""
    @classmethod
    @overload
    def ToDictionary[TSource, TKey, TElement](
        cls,
        source: ParallelQuery[TSource],
        keySelector: Func[TSource, TKey],
        elementSelector: Func[TSource, TElement],
        comparer: IEqualityComparer[TKey],
    ) -> Dictionary[TKey, TElement]:
        """"""
    @classmethod
    def ToList[TSource](cls, source: ParallelQuery[TSource]) -> List[TSource]:
        """"""
    @classmethod
    @overload
    def ToLookup[TSource, TKey](
        cls, source: ParallelQuery[TSource], keySelector: Func[TSource, TKey]
    ) -> ILookup[TKey, TSource]:
        """"""
    @classmethod
    @overload
    def ToLookup[TSource, TKey](
        cls,
        source: ParallelQuery[TSource],
        keySelector: Func[TSource, TKey],
        comparer: IEqualityComparer[TKey],
    ) -> ILookup[TKey, TSource]:
        """"""
    @classmethod
    @overload
    def ToLookup[TSource, TKey, TElement](
        cls,
        source: ParallelQuery[TSource],
        keySelector: Func[TSource, TKey],
        elementSelector: Func[TSource, TElement],
    ) -> ILookup[TKey, TElement]:
        """"""
    @classmethod
    @overload
    def ToLookup[TSource, TKey, TElement](
        cls,
        source: ParallelQuery[TSource],
        keySelector: Func[TSource, TKey],
        elementSelector: Func[TSource, TElement],
        comparer: IEqualityComparer[TKey],
    ) -> ILookup[TKey, TElement]:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    @overload
    def Union[TSource](
        cls, first: ParallelQuery[TSource], second: IEnumerable[TSource]
    ) -> ParallelQuery[TSource]:
        """"""
    @classmethod
    @overload
    def Union[TSource](
        cls,
        first: ParallelQuery[TSource],
        second: IEnumerable[TSource],
        comparer: IEqualityComparer[TSource],
    ) -> ParallelQuery[TSource]:
        """"""
    @classmethod
    @overload
    def Union[TSource](
        cls, first: ParallelQuery[TSource], second: ParallelQuery[TSource]
    ) -> ParallelQuery[TSource]:
        """"""
    @classmethod
    @overload
    def Union[TSource](
        cls,
        first: ParallelQuery[TSource],
        second: ParallelQuery[TSource],
        comparer: IEqualityComparer[TSource],
    ) -> ParallelQuery[TSource]:
        """"""
    @classmethod
    @overload
    def Where[TSource](
        cls, source: ParallelQuery[TSource], predicate: Func[TSource, bool]
    ) -> ParallelQuery[TSource]:
        """"""
    @classmethod
    @overload
    def Where[TSource](
        cls, source: ParallelQuery[TSource], predicate: Func[TSource, int, bool]
    ) -> ParallelQuery[TSource]:
        """"""
    @classmethod
    def WithCancellation[TSource](
        cls, source: ParallelQuery[TSource], cancellationToken: CancellationToken
    ) -> ParallelQuery[TSource]:
        """"""
    @classmethod
    def WithDegreeOfParallelism[TSource](
        cls, source: ParallelQuery[TSource], degreeOfParallelism: int
    ) -> ParallelQuery[TSource]:
        """"""
    @classmethod
    def WithExecutionMode[TSource](
        cls, source: ParallelQuery[TSource], executionMode: ParallelExecutionMode
    ) -> ParallelQuery[TSource]:
        """"""
    @classmethod
    def WithMergeOptions[TSource](
        cls, source: ParallelQuery[TSource], mergeOptions: ParallelMergeOptions
    ) -> ParallelQuery[TSource]:
        """"""
    @classmethod
    @overload
    def Zip[TFirst, TSecond, TResult](
        cls,
        first: ParallelQuery[TFirst],
        second: IEnumerable[TSecond],
        resultSelector: Func[TFirst, TSecond, TResult],
    ) -> ParallelQuery[TResult]:
        """"""
    @classmethod
    @overload
    def Zip[TFirst, TSecond, TResult](
        cls,
        first: ParallelQuery[TFirst],
        second: ParallelQuery[TSecond],
        resultSelector: Func[TFirst, TSecond, TResult],
    ) -> ParallelQuery[TResult]:
        """"""
    @overload
    def __contains__[TSource](self, source: ParallelQuery[TSource], value: TSource) -> bool:
        """"""
    @overload
    def __contains__[TSource](
        self, source: ParallelQuery[TSource], value: TSource, comparer: IEqualityComparer[TSource]
    ) -> bool:
        """"""

class ParallelExecutionMode(Enum):
    """"""

    Default: ParallelExecutionMode = ...
    """"""
    ForceParallelism: ParallelExecutionMode = ...
    """"""

class ParallelMergeOptions(Enum):
    """"""

    Default: ParallelMergeOptions = ...
    """"""
    NotBuffered: ParallelMergeOptions = ...
    """"""
    AutoBuffered: ParallelMergeOptions = ...
    """"""
    FullyBuffered: ParallelMergeOptions = ...
    """"""

class ParallelQuery(Object, IEnumerable):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def __iter__(self) -> Iterator:
        """"""

class ParallelQuery[TSource](ParallelQuery, IEnumerable[TSource], IEnumerable):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator[TSource](self) -> IEnumerator[TSource]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def __iter__[TSource](self) -> Iterator[TSource]:
        """"""

class Queryable(ABC, Object):
    """"""
    @classmethod
    @overload
    def Aggregate[TSource, TAccumulate](
        cls,
        source: IQueryable[TSource],
        seed: TAccumulate,
        func: Expression[Func[TAccumulate, TSource, TAccumulate]],
    ) -> TAccumulate:
        """"""
    @classmethod
    @overload
    def Aggregate[TSource, TAccumulate, TResult](
        cls,
        source: IQueryable[TSource],
        seed: TAccumulate,
        func: Expression[Func[TAccumulate, TSource, TAccumulate]],
        selector: Expression[Func[TAccumulate, TResult]],
    ) -> TResult:
        """"""
    @classmethod
    @overload
    def Aggregate[TSource](
        cls, source: IQueryable[TSource], func: Expression[Func[TSource, TSource, TSource]]
    ) -> TSource:
        """"""
    @classmethod
    def All[TSource](
        cls, source: IQueryable[TSource], predicate: Expression[Func[TSource, bool]]
    ) -> bool:
        """"""
    @classmethod
    @overload
    def Any[TSource](cls, source: IQueryable[TSource]) -> bool:
        """"""
    @classmethod
    @overload
    def Any[TSource](
        cls, source: IQueryable[TSource], predicate: Expression[Func[TSource, bool]]
    ) -> bool:
        """"""
    @classmethod
    @overload
    def AsQueryable[TElement](cls, source: IEnumerable[TElement]) -> IQueryable[TElement]:
        """"""
    @classmethod
    @overload
    def AsQueryable(cls, source: IEnumerable) -> IQueryable:
        """"""
    @classmethod
    @overload
    def Average[TSource](
        cls, source: IQueryable[TSource], selector: Expression[Func[TSource, Decimal | None]]
    ) -> Decimal | None:
        """"""
    @classmethod
    @overload
    def Average[TSource](
        cls, source: IQueryable[TSource], selector: Expression[Func[TSource, Decimal]]
    ) -> Decimal:
        """"""
    @classmethod
    @overload
    def Average[TSource](
        cls, source: IQueryable[TSource], selector: Expression[Func[TSource, float | None]]
    ) -> float | None:
        """"""
    @classmethod
    @overload
    def Average[TSource](
        cls, source: IQueryable[TSource], selector: Expression[Func[TSource, float]]
    ) -> float:
        """"""
    @classmethod
    @overload
    def Average[TSource](
        cls, source: IQueryable[TSource], selector: Expression[Func[TSource, int | None]]
    ) -> float | None:
        """"""
    @classmethod
    @overload
    def Average[TSource](
        cls, source: IQueryable[TSource], selector: Expression[Func[TSource, int]]
    ) -> float:
        """"""
    @classmethod
    @overload
    def Average[TSource](
        cls, source: IQueryable[TSource], selector: Expression[Func[TSource, int | None]]
    ) -> float | None:
        """"""
    @classmethod
    @overload
    def Average[TSource](
        cls, source: IQueryable[TSource], selector: Expression[Func[TSource, int]]
    ) -> float:
        """"""
    @classmethod
    @overload
    def Average[TSource](
        cls, source: IQueryable[TSource], selector: Expression[Func[TSource, float | None]]
    ) -> float | None:
        """"""
    @classmethod
    @overload
    def Average[TSource](
        cls, source: IQueryable[TSource], selector: Expression[Func[TSource, float]]
    ) -> float:
        """"""
    @classmethod
    @overload
    def Average(cls, source: IQueryable[Decimal | None]) -> Decimal | None:
        """"""
    @classmethod
    @overload
    def Average(cls, source: IQueryable[Decimal]) -> Decimal:
        """"""
    @classmethod
    @overload
    def Average(cls, source: IQueryable[float | None]) -> float | None:
        """"""
    @classmethod
    @overload
    def Average(cls, source: IQueryable[float]) -> float:
        """"""
    @classmethod
    @overload
    def Average(cls, source: IQueryable[int | None]) -> float | None:
        """"""
    @classmethod
    @overload
    def Average(cls, source: IQueryable[int]) -> float:
        """"""
    @classmethod
    @overload
    def Average(cls, source: IQueryable[int | None]) -> float | None:
        """"""
    @classmethod
    @overload
    def Average(cls, source: IQueryable[int]) -> float:
        """"""
    @classmethod
    @overload
    def Average(cls, source: IQueryable[float | None]) -> float | None:
        """"""
    @classmethod
    @overload
    def Average(cls, source: IQueryable[float]) -> float:
        """"""
    @classmethod
    def Cast[TResult](cls, source: IQueryable) -> IQueryable[TResult]:
        """"""
    @classmethod
    def Concat[TSource](
        cls, source1: IQueryable[TSource], source2: IEnumerable[TSource]
    ) -> IQueryable[TSource]:
        """"""
    @classmethod
    @overload
    def Contains[TSource](cls, source: IQueryable[TSource], item: TSource) -> bool:
        """"""
    @classmethod
    @overload
    def Contains[TSource](
        cls, source: IQueryable[TSource], item: TSource, comparer: IEqualityComparer[TSource]
    ) -> bool:
        """"""
    @classmethod
    @overload
    def Count[TSource](cls, source: IQueryable[TSource]) -> int:
        """"""
    @classmethod
    @overload
    def Count[TSource](
        cls, source: IQueryable[TSource], predicate: Expression[Func[TSource, bool]]
    ) -> int:
        """"""
    @classmethod
    @overload
    def DefaultIfEmpty[TSource](cls, source: IQueryable[TSource]) -> IQueryable[TSource]:
        """"""
    @classmethod
    @overload
    def DefaultIfEmpty[TSource](
        cls, source: IQueryable[TSource], defaultValue: TSource
    ) -> IQueryable[TSource]:
        """"""
    @classmethod
    @overload
    def Distinct[TSource](cls, source: IQueryable[TSource]) -> IQueryable[TSource]:
        """"""
    @classmethod
    @overload
    def Distinct[TSource](
        cls, source: IQueryable[TSource], comparer: IEqualityComparer[TSource]
    ) -> IQueryable[TSource]:
        """"""
    @classmethod
    def ElementAt[TSource](cls, source: IQueryable[TSource], index: int) -> TSource:
        """"""
    @classmethod
    def ElementAtOrDefault[TSource](cls, source: IQueryable[TSource], index: int) -> TSource:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    @overload
    def Except[TSource](
        cls, source1: IQueryable[TSource], source2: IEnumerable[TSource]
    ) -> IQueryable[TSource]:
        """"""
    @classmethod
    @overload
    def Except[TSource](
        cls,
        source1: IQueryable[TSource],
        source2: IEnumerable[TSource],
        comparer: IEqualityComparer[TSource],
    ) -> IQueryable[TSource]:
        """"""
    @classmethod
    @overload
    def First[TSource](cls, source: IQueryable[TSource]) -> TSource:
        """"""
    @classmethod
    @overload
    def First[TSource](
        cls, source: IQueryable[TSource], predicate: Expression[Func[TSource, bool]]
    ) -> TSource:
        """"""
    @classmethod
    @overload
    def FirstOrDefault[TSource](cls, source: IQueryable[TSource]) -> TSource:
        """"""
    @classmethod
    @overload
    def FirstOrDefault[TSource](
        cls, source: IQueryable[TSource], predicate: Expression[Func[TSource, bool]]
    ) -> TSource:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    @overload
    def GroupBy[TSource, TKey](
        cls, source: IQueryable[TSource], keySelector: Expression[Func[TSource, TKey]]
    ) -> IQueryable[IGrouping[TKey, TSource]]:
        """"""
    @classmethod
    @overload
    def GroupBy[TSource, TKey](
        cls,
        source: IQueryable[TSource],
        keySelector: Expression[Func[TSource, TKey]],
        comparer: IEqualityComparer[TKey],
    ) -> IQueryable[IGrouping[TKey, TSource]]:
        """"""
    @classmethod
    @overload
    def GroupBy[TSource, TKey, TResult](
        cls,
        source: IQueryable[TSource],
        keySelector: Expression[Func[TSource, TKey]],
        resultSelector: Expression[Func, IEnumerable[TSource, TResult]],
    ) -> IQueryable[TResult]:
        """"""
    @classmethod
    @overload
    def GroupBy[TSource, TKey, TResult](
        cls,
        source: IQueryable[TSource],
        keySelector: Expression[Func[TSource, TKey]],
        resultSelector: Expression[Func, IEnumerable[TSource, TResult]],
        comparer: IEqualityComparer[TKey],
    ) -> IQueryable[TResult]:
        """"""
    @classmethod
    @overload
    def GroupBy[TSource, TKey, TElement](
        cls,
        source: IQueryable[TSource],
        keySelector: Expression[Func[TSource, TKey]],
        elementSelector: Expression[Func[TSource, TElement]],
    ) -> IQueryable[IGrouping[TKey, TElement]]:
        """"""
    @classmethod
    @overload
    def GroupBy[TSource, TKey, TElement](
        cls,
        source: IQueryable[TSource],
        keySelector: Expression[Func[TSource, TKey]],
        elementSelector: Expression[Func[TSource, TElement]],
        comparer: IEqualityComparer[TKey],
    ) -> IQueryable[IGrouping[TKey, TElement]]:
        """"""
    @classmethod
    @overload
    def GroupBy[TSource, TKey, TElement, TResult](
        cls,
        source: IQueryable[TSource],
        keySelector: Expression[Func[TSource, TKey]],
        elementSelector: Expression[Func[TSource, TElement]],
        resultSelector: Expression[Func, IEnumerable[TElement, TResult]],
    ) -> IQueryable[TResult]:
        """"""
    @classmethod
    @overload
    def GroupBy[TSource, TKey, TElement, TResult](
        cls,
        source: IQueryable[TSource],
        keySelector: Expression[Func[TSource, TKey]],
        elementSelector: Expression[Func[TSource, TElement]],
        resultSelector: Expression[Func, IEnumerable[TElement, TResult]],
        comparer: IEqualityComparer[TKey],
    ) -> IQueryable[TResult]:
        """"""
    @classmethod
    @overload
    def GroupJoin[TOuter, TInner, TKey, TResult](
        cls,
        outer: IQueryable[TOuter],
        inner: IEnumerable[TInner],
        outerKeySelector: Expression[Func[TOuter, TKey]],
        innerKeySelector: Expression[Func[TInner, TKey]],
        resultSelector: Expression[Func, IEnumerable[TInner, TResult]],
    ) -> IQueryable[TResult]:
        """"""
    @classmethod
    @overload
    def GroupJoin[TOuter, TInner, TKey, TResult](
        cls,
        outer: IQueryable[TOuter],
        inner: IEnumerable[TInner],
        outerKeySelector: Expression[Func[TOuter, TKey]],
        innerKeySelector: Expression[Func[TInner, TKey]],
        resultSelector: Expression[Func, IEnumerable[TInner, TResult]],
        comparer: IEqualityComparer[TKey],
    ) -> IQueryable[TResult]:
        """"""
    @classmethod
    @overload
    def Intersect[TSource](
        cls, source1: IQueryable[TSource], source2: IEnumerable[TSource]
    ) -> IQueryable[TSource]:
        """"""
    @classmethod
    @overload
    def Intersect[TSource](
        cls,
        source1: IQueryable[TSource],
        source2: IEnumerable[TSource],
        comparer: IEqualityComparer[TSource],
    ) -> IQueryable[TSource]:
        """"""
    @classmethod
    @overload
    def Join[TOuter, TInner, TKey, TResult](
        cls,
        outer: IQueryable[TOuter],
        inner: IEnumerable[TInner],
        outerKeySelector: Expression[Func[TOuter, TKey]],
        innerKeySelector: Expression[Func[TInner, TKey]],
        resultSelector: Expression[Func[TOuter, TInner, TResult]],
    ) -> IQueryable[TResult]:
        """"""
    @classmethod
    @overload
    def Join[TOuter, TInner, TKey, TResult](
        cls,
        outer: IQueryable[TOuter],
        inner: IEnumerable[TInner],
        outerKeySelector: Expression[Func[TOuter, TKey]],
        innerKeySelector: Expression[Func[TInner, TKey]],
        resultSelector: Expression[Func[TOuter, TInner, TResult]],
        comparer: IEqualityComparer[TKey],
    ) -> IQueryable[TResult]:
        """"""
    @classmethod
    @overload
    def Last[TSource](cls, source: IQueryable[TSource]) -> TSource:
        """"""
    @classmethod
    @overload
    def Last[TSource](
        cls, source: IQueryable[TSource], predicate: Expression[Func[TSource, bool]]
    ) -> TSource:
        """"""
    @classmethod
    @overload
    def LastOrDefault[TSource](cls, source: IQueryable[TSource]) -> TSource:
        """"""
    @classmethod
    @overload
    def LastOrDefault[TSource](
        cls, source: IQueryable[TSource], predicate: Expression[Func[TSource, bool]]
    ) -> TSource:
        """"""
    @classmethod
    @overload
    def LongCount[TSource](cls, source: IQueryable[TSource]) -> int:
        """"""
    @classmethod
    @overload
    def LongCount[TSource](
        cls, source: IQueryable[TSource], predicate: Expression[Func[TSource, bool]]
    ) -> int:
        """"""
    @classmethod
    @overload
    def Max[TSource](cls, source: IQueryable[TSource]) -> TSource:
        """"""
    @classmethod
    @overload
    def Max[TSource, TResult](
        cls, source: IQueryable[TSource], selector: Expression[Func[TSource, TResult]]
    ) -> TResult:
        """"""
    @classmethod
    @overload
    def Min[TSource](cls, source: IQueryable[TSource]) -> TSource:
        """"""
    @classmethod
    @overload
    def Min[TSource, TResult](
        cls, source: IQueryable[TSource], selector: Expression[Func[TSource, TResult]]
    ) -> TResult:
        """"""
    @classmethod
    def OfType[TResult](cls, source: IQueryable) -> IQueryable[TResult]:
        """"""
    @classmethod
    @overload
    def OrderBy[TSource, TKey](
        cls, source: IQueryable[TSource], keySelector: Expression[Func[TSource, TKey]]
    ) -> IOrderedQueryable[TSource]:
        """"""
    @classmethod
    @overload
    def OrderBy[TSource, TKey](
        cls,
        source: IQueryable[TSource],
        keySelector: Expression[Func[TSource, TKey]],
        comparer: IComparer[TKey],
    ) -> IOrderedQueryable[TSource]:
        """"""
    @classmethod
    @overload
    def OrderByDescending[TSource, TKey](
        cls, source: IQueryable[TSource], keySelector: Expression[Func[TSource, TKey]]
    ) -> IOrderedQueryable[TSource]:
        """"""
    @classmethod
    @overload
    def OrderByDescending[TSource, TKey](
        cls,
        source: IQueryable[TSource],
        keySelector: Expression[Func[TSource, TKey]],
        comparer: IComparer[TKey],
    ) -> IOrderedQueryable[TSource]:
        """"""
    @classmethod
    def Reverse[TSource](cls, source: IQueryable[TSource]) -> IQueryable[TSource]:
        """"""
    @classmethod
    @overload
    def Select[TSource, TResult](
        cls, source: IQueryable[TSource], selector: Expression[Func[TSource, TResult]]
    ) -> IQueryable[TResult]:
        """"""
    @classmethod
    @overload
    def Select[TSource, TResult](
        cls, source: IQueryable[TSource], selector: Expression[Func[TSource, int, TResult]]
    ) -> IQueryable[TResult]:
        """"""
    @classmethod
    @overload
    def SelectMany[TSource, TCollection, TResult](
        cls,
        source: IQueryable[TSource],
        collectionSelector: Expression[Func, IEnumerable[TCollection]],
        resultSelector: Expression[Func[TSource, TCollection, TResult]],
    ) -> IQueryable[TResult]:
        """"""
    @classmethod
    @overload
    def SelectMany[TSource, TResult](
        cls, source: IQueryable[TSource], selector: Expression[Func, IEnumerable[TResult]]
    ) -> IQueryable[TResult]:
        """"""
    @classmethod
    @overload
    def SelectMany[TSource, TCollection, TResult](
        cls,
        source: IQueryable[TSource],
        collectionSelector: Expression[Func, int, IEnumerable[TCollection]],
        resultSelector: Expression[Func[TSource, TCollection, TResult]],
    ) -> IQueryable[TResult]:
        """"""
    @classmethod
    @overload
    def SelectMany[TSource, TResult](
        cls, source: IQueryable[TSource], selector: Expression[Func, int, IEnumerable[TResult]]
    ) -> IQueryable[TResult]:
        """"""
    @classmethod
    @overload
    def SequenceEqual[TSource](
        cls, source1: IQueryable[TSource], source2: IEnumerable[TSource]
    ) -> bool:
        """"""
    @classmethod
    @overload
    def SequenceEqual[TSource](
        cls,
        source1: IQueryable[TSource],
        source2: IEnumerable[TSource],
        comparer: IEqualityComparer[TSource],
    ) -> bool:
        """"""
    @classmethod
    @overload
    def Single[TSource](cls, source: IQueryable[TSource]) -> TSource:
        """"""
    @classmethod
    @overload
    def Single[TSource](
        cls, source: IQueryable[TSource], predicate: Expression[Func[TSource, bool]]
    ) -> TSource:
        """"""
    @classmethod
    @overload
    def SingleOrDefault[TSource](cls, source: IQueryable[TSource]) -> TSource:
        """"""
    @classmethod
    @overload
    def SingleOrDefault[TSource](
        cls, source: IQueryable[TSource], predicate: Expression[Func[TSource, bool]]
    ) -> TSource:
        """"""
    @classmethod
    def Skip[TSource](cls, source: IQueryable[TSource], count: int) -> IQueryable[TSource]:
        """"""
    @classmethod
    @overload
    def SkipWhile[TSource](
        cls, source: IQueryable[TSource], predicate: Expression[Func[TSource, bool]]
    ) -> IQueryable[TSource]:
        """"""
    @classmethod
    @overload
    def SkipWhile[TSource](
        cls, source: IQueryable[TSource], predicate: Expression[Func[TSource, int, bool]]
    ) -> IQueryable[TSource]:
        """"""
    @classmethod
    @overload
    def Sum[TSource](
        cls, source: IQueryable[TSource], selector: Expression[Func[TSource, Decimal | None]]
    ) -> Decimal | None:
        """"""
    @classmethod
    @overload
    def Sum[TSource](
        cls, source: IQueryable[TSource], selector: Expression[Func[TSource, Decimal]]
    ) -> Decimal:
        """"""
    @classmethod
    @overload
    def Sum[TSource](
        cls, source: IQueryable[TSource], selector: Expression[Func[TSource, float | None]]
    ) -> float | None:
        """"""
    @classmethod
    @overload
    def Sum[TSource](
        cls, source: IQueryable[TSource], selector: Expression[Func[TSource, float]]
    ) -> float:
        """"""
    @classmethod
    @overload
    def Sum[TSource](
        cls, source: IQueryable[TSource], selector: Expression[Func[TSource, int | None]]
    ) -> int | None:
        """"""
    @classmethod
    @overload
    def Sum[TSource](
        cls, source: IQueryable[TSource], selector: Expression[Func[TSource, int]]
    ) -> int:
        """"""
    @classmethod
    @overload
    def Sum[TSource](
        cls, source: IQueryable[TSource], selector: Expression[Func[TSource, int | None]]
    ) -> int | None:
        """"""
    @classmethod
    @overload
    def Sum[TSource](
        cls, source: IQueryable[TSource], selector: Expression[Func[TSource, int]]
    ) -> int:
        """"""
    @classmethod
    @overload
    def Sum[TSource](
        cls, source: IQueryable[TSource], selector: Expression[Func[TSource, float | None]]
    ) -> float | None:
        """"""
    @classmethod
    @overload
    def Sum[TSource](
        cls, source: IQueryable[TSource], selector: Expression[Func[TSource, float]]
    ) -> float:
        """"""
    @classmethod
    @overload
    def Sum(cls, source: IQueryable[Decimal | None]) -> Decimal | None:
        """"""
    @classmethod
    @overload
    def Sum(cls, source: IQueryable[Decimal]) -> Decimal:
        """"""
    @classmethod
    @overload
    def Sum(cls, source: IQueryable[float | None]) -> float | None:
        """"""
    @classmethod
    @overload
    def Sum(cls, source: IQueryable[float]) -> float:
        """"""
    @classmethod
    @overload
    def Sum(cls, source: IQueryable[int | None]) -> int | None:
        """"""
    @classmethod
    @overload
    def Sum(cls, source: IQueryable[int]) -> int:
        """"""
    @classmethod
    @overload
    def Sum(cls, source: IQueryable[int | None]) -> int | None:
        """"""
    @classmethod
    @overload
    def Sum(cls, source: IQueryable[int]) -> int:
        """"""
    @classmethod
    @overload
    def Sum(cls, source: IQueryable[float | None]) -> float | None:
        """"""
    @classmethod
    @overload
    def Sum(cls, source: IQueryable[float]) -> float:
        """"""
    @classmethod
    def Take[TSource](cls, source: IQueryable[TSource], count: int) -> IQueryable[TSource]:
        """"""
    @classmethod
    @overload
    def TakeWhile[TSource](
        cls, source: IQueryable[TSource], predicate: Expression[Func[TSource, bool]]
    ) -> IQueryable[TSource]:
        """"""
    @classmethod
    @overload
    def TakeWhile[TSource](
        cls, source: IQueryable[TSource], predicate: Expression[Func[TSource, int, bool]]
    ) -> IQueryable[TSource]:
        """"""
    @classmethod
    @overload
    def ThenBy[TSource, TKey](
        cls, source: IOrderedQueryable[TSource], keySelector: Expression[Func[TSource, TKey]]
    ) -> IOrderedQueryable[TSource]:
        """"""
    @classmethod
    @overload
    def ThenBy[TSource, TKey](
        cls,
        source: IOrderedQueryable[TSource],
        keySelector: Expression[Func[TSource, TKey]],
        comparer: IComparer[TKey],
    ) -> IOrderedQueryable[TSource]:
        """"""
    @classmethod
    @overload
    def ThenByDescending[TSource, TKey](
        cls, source: IOrderedQueryable[TSource], keySelector: Expression[Func[TSource, TKey]]
    ) -> IOrderedQueryable[TSource]:
        """"""
    @classmethod
    @overload
    def ThenByDescending[TSource, TKey](
        cls,
        source: IOrderedQueryable[TSource],
        keySelector: Expression[Func[TSource, TKey]],
        comparer: IComparer[TKey],
    ) -> IOrderedQueryable[TSource]:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    @overload
    def Union[TSource](
        cls, source1: IQueryable[TSource], source2: IEnumerable[TSource]
    ) -> IQueryable[TSource]:
        """"""
    @classmethod
    @overload
    def Union[TSource](
        cls,
        source1: IQueryable[TSource],
        source2: IEnumerable[TSource],
        comparer: IEqualityComparer[TSource],
    ) -> IQueryable[TSource]:
        """"""
    @classmethod
    @overload
    def Where[TSource](
        cls, source: IQueryable[TSource], predicate: Expression[Func[TSource, bool]]
    ) -> IQueryable[TSource]:
        """"""
    @classmethod
    @overload
    def Where[TSource](
        cls, source: IQueryable[TSource], predicate: Expression[Func[TSource, int, bool]]
    ) -> IQueryable[TSource]:
        """"""
    @classmethod
    def Zip[TFirst, TSecond, TResult](
        cls,
        source1: IQueryable[TFirst],
        source2: IEnumerable[TSecond],
        resultSelector: Expression[Func[TFirst, TSecond, TResult]],
    ) -> IQueryable[TResult]:
        """"""
    @overload
    def __contains__[TSource](self, source: IQueryable[TSource], item: TSource) -> bool:
        """"""
    @overload
    def __contains__[TSource](
        self, source: IQueryable[TSource], item: TSource, comparer: IEqualityComparer[TSource]
    ) -> bool:
        """"""

class SR(Object):
    """"""
    @classmethod
    @property
    def Resources(cls) -> ResourceManager:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @classmethod
    def GetObject(cls, name: str) -> object:
        """"""
    @classmethod
    @overload
    def GetString(cls, name: str) -> str:
        """"""
    @classmethod
    @overload
    def GetString(cls, name: str, usedFallback: Boolean) -> tuple[str, Boolean]:
        """"""
    @classmethod
    @overload
    def GetString(cls, name: str, args: Array[object]) -> str:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SRCategoryAttribute(CategoryAttribute, _Attribute):
    """"""
    def __init__(self, category: str) -> None:
        """"""
    @property
    def Category(self) -> str:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """"""
    def GetTypeInfoCount(self, pcTInfo: UInt32) -> tuple[None, UInt32]:
        """"""
    def Invoke(
        self,
        dispIdMember: int,
        riid: Guid,
        lcid: int,
        wFlags: int,
        pDispParams: IntPtr,
        pVarResult: IntPtr,
        pExcepInfo: IntPtr,
        puArgErr: IntPtr,
    ) -> None:
        """"""
    def IsDefaultAttribute(self) -> bool:
        """"""
    def Match(self, obj: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

class SRDescriptionAttribute(DescriptionAttribute, _Attribute):
    """"""
    def __init__(self, description: str) -> None:
        """"""
    @property
    def Description(self) -> str:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """"""
    def GetTypeInfoCount(self, pcTInfo: UInt32) -> tuple[None, UInt32]:
        """"""
    def Invoke(
        self,
        dispIdMember: int,
        riid: Guid,
        lcid: int,
        wFlags: int,
        pDispParams: IntPtr,
        pVarResult: IntPtr,
        pExcepInfo: IntPtr,
        puArgErr: IntPtr,
    ) -> None:
        """"""
    def IsDefaultAttribute(self) -> bool:
        """"""
    def Match(self, obj: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

class Set[TElement](Object):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, comparer: IEqualityComparer[TElement]) -> None:
        """"""
    def Add(self, value: TElement) -> bool:
        """"""
    def Contains(self, value: TElement) -> bool:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Remove(self, value: TElement) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    def __contains__(self, value: TElement) -> bool:
        """"""
    def __delitem__(self, value: TElement) -> bool:
        """"""

class SingleLinkedNode[TSource](Object):
    """"""
    def __init__(self, item: TSource) -> None:
        """"""
    @property
    def Item(self) -> TSource:
        """"""
    @property
    def Linked(self) -> SingleLinkedNode[TSource]:
        """"""
    def Add(self, item: TSource) -> SingleLinkedNode[TSource]:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetCount(self) -> int:
        """"""
    def GetEnumerator(self, count: int) -> IEnumerator[TSource]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetNode(self, index: int) -> SingleLinkedNode[TSource]:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToArray(self, count: int) -> Array[TSource]:
        """"""
    def ToString(self) -> str:
        """"""
    def __iter__(self, count: int) -> Iterator[TSource]:
        """"""
    def __getitem__(self) -> TSource:
        """"""

class Strings(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SystemCore_EnumerableDebugView(Object):
    """"""
    def __init__(self, enumerable: IEnumerable) -> None:
        """"""
    @property
    def Items(self) -> Array[object]:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SystemCore_EnumerableDebugViewEmptyException(Exception, _Exception, ISerializable):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Data(self) -> IDictionary:
        """"""
    @property
    def Empty(self) -> str:
        """"""
    @property
    def HResult(self) -> int:
        """"""
    @property
    def HelpLink(self) -> str:
        """"""
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """"""
    @property
    def Message(self) -> str:
        """"""
    @property
    def Source(self) -> str:
        """"""
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """"""
    @property
    def TargetSite(self) -> MethodBase:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetBaseException(self) -> Exception:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SystemCore_EnumerableDebugView[T](Object):
    """"""
    def __init__(self, enumerable: IEnumerable[T]) -> None:
        """"""
    @property
    def Items(self) -> Array[T]:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class TypeHelper(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
