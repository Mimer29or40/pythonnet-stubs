from __future__ import annotations

from abc import ABC
from typing import ClassVar
from typing import Final
from typing import Generic
from typing import Iterator
from typing import Optional
from typing import Tuple
from typing import TypeVar
from typing import overload

from System import Action
from System import Array
from System import Decimal
from System import Enum
from System import Exception
from System import Func
from System import Guid
from System import IntPtr
from System import Object
from System import Type
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

class AggregationMinMaxHelpers(ABC, Generic[T], Object):
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

class Buffer(Generic[TElement], ValueType):
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

class EmptyEnumerable(Generic[TElement], Object):
    """"""

    Instance: Final[ClassVar[Array[TElement]]] = ...
    """
    
    :return: 
    """
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

class Enumerable(ABC, Object):
    """"""

    @classmethod
    @overload
    def Aggregate(
        cls, source: IEnumerable[TSource], func: Func[TSource, TSource, TSource]
    ) -> TSource:
        """

        :param source:
        :param func:
        :return:
        """
    @classmethod
    @overload
    def Aggregate(
        cls,
        source: IEnumerable[TSource],
        seed: TAccumulate,
        func: Func[TAccumulate, TSource, TAccumulate],
    ) -> TAccumulate:
        """

        :param source:
        :param seed:
        :param func:
        :return:
        """
    @classmethod
    @overload
    def Aggregate(
        cls,
        source: IEnumerable[TSource],
        seed: TAccumulate,
        func: Func[TAccumulate, TSource, TAccumulate],
        resultSelector: Func[TAccumulate, TResult],
    ) -> TResult:
        """

        :param source:
        :param seed:
        :param func:
        :param resultSelector:
        :return:
        """
    @classmethod
    def All(cls, source: IEnumerable[TSource], predicate: Func[TSource, bool]) -> bool:
        """

        :param source:
        :param predicate:
        :return:
        """
    @classmethod
    @overload
    def Any(cls, source: IEnumerable[TSource]) -> bool:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Any(cls, source: IEnumerable[TSource], predicate: Func[TSource, bool]) -> bool:
        """

        :param source:
        :param predicate:
        :return:
        """
    @classmethod
    def Append(cls, source: IEnumerable[TSource], element: TSource) -> IEnumerable[TSource]:
        """

        :param source:
        :param element:
        :return:
        """
    @classmethod
    def AsEnumerable(cls, source: IEnumerable[TSource]) -> IEnumerable[TSource]:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Average(cls, source: IEnumerable[Optional[Decimal]]) -> Optional[Decimal]:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Average(cls, source: IEnumerable[Decimal]) -> Decimal:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Average(cls, source: IEnumerable[Optional[float]]) -> Optional[float]:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Average(cls, source: IEnumerable[float]) -> float:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Average(cls, source: IEnumerable[Optional[int]]) -> Optional[float]:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Average(cls, source: IEnumerable[int]) -> float:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Average(cls, source: IEnumerable[Optional[int]]) -> Optional[float]:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Average(cls, source: IEnumerable[int]) -> float:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Average(cls, source: IEnumerable[Optional[float]]) -> Optional[float]:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Average(cls, source: IEnumerable[float]) -> float:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Average(
        cls, source: IEnumerable[TSource], selector: Func[TSource, Optional[Decimal]]
    ) -> Optional[Decimal]:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    @overload
    def Average(cls, source: IEnumerable[TSource], selector: Func[TSource, Decimal]) -> Decimal:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    @overload
    def Average(
        cls, source: IEnumerable[TSource], selector: Func[TSource, Optional[float]]
    ) -> Optional[float]:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    @overload
    def Average(cls, source: IEnumerable[TSource], selector: Func[TSource, float]) -> float:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    @overload
    def Average(
        cls, source: IEnumerable[TSource], selector: Func[TSource, Optional[int]]
    ) -> Optional[float]:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    @overload
    def Average(cls, source: IEnumerable[TSource], selector: Func[TSource, int]) -> float:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    @overload
    def Average(
        cls, source: IEnumerable[TSource], selector: Func[TSource, Optional[int]]
    ) -> Optional[float]:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    @overload
    def Average(cls, source: IEnumerable[TSource], selector: Func[TSource, int]) -> float:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    @overload
    def Average(
        cls, source: IEnumerable[TSource], selector: Func[TSource, Optional[float]]
    ) -> Optional[float]:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    @overload
    def Average(cls, source: IEnumerable[TSource], selector: Func[TSource, float]) -> float:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    def Cast(cls, source: IEnumerable) -> IEnumerable[TResult]:
        """

        :param source:
        :return:
        """
    @classmethod
    def Concat(
        cls, first: IEnumerable[TSource], second: IEnumerable[TSource]
    ) -> IEnumerable[TSource]:
        """

        :param first:
        :param second:
        :return:
        """
    @classmethod
    @overload
    def Contains(cls, source: IEnumerable[TSource], value: TSource) -> bool:
        """

        :param source:
        :param value:
        :return:
        """
    @classmethod
    @overload
    def Contains(
        cls, source: IEnumerable[TSource], value: TSource, comparer: IEqualityComparer[TSource]
    ) -> bool:
        """

        :param source:
        :param value:
        :param comparer:
        :return:
        """
    @classmethod
    @overload
    def Count(cls, source: IEnumerable[TSource]) -> int:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Count(cls, source: IEnumerable[TSource], predicate: Func[TSource, bool]) -> int:
        """

        :param source:
        :param predicate:
        :return:
        """
    @classmethod
    @overload
    def DefaultIfEmpty(cls, source: IEnumerable[TSource]) -> IEnumerable[TSource]:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def DefaultIfEmpty(
        cls, source: IEnumerable[TSource], defaultValue: TSource
    ) -> IEnumerable[TSource]:
        """

        :param source:
        :param defaultValue:
        :return:
        """
    @classmethod
    @overload
    def Distinct(cls, source: IEnumerable[TSource]) -> IEnumerable[TSource]:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Distinct(
        cls, source: IEnumerable[TSource], comparer: IEqualityComparer[TSource]
    ) -> IEnumerable[TSource]:
        """

        :param source:
        :param comparer:
        :return:
        """
    @classmethod
    def ElementAt(cls, source: IEnumerable[TSource], index: int) -> TSource:
        """

        :param source:
        :param index:
        :return:
        """
    @classmethod
    def ElementAtOrDefault(cls, source: IEnumerable[TSource], index: int) -> TSource:
        """

        :param source:
        :param index:
        :return:
        """
    @classmethod
    def Empty(cls) -> IEnumerable[TResult]:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @classmethod
    @overload
    def Except(
        cls, first: IEnumerable[TSource], second: IEnumerable[TSource]
    ) -> IEnumerable[TSource]:
        """

        :param first:
        :param second:
        :return:
        """
    @classmethod
    @overload
    def Except(
        cls,
        first: IEnumerable[TSource],
        second: IEnumerable[TSource],
        comparer: IEqualityComparer[TSource],
    ) -> IEnumerable[TSource]:
        """

        :param first:
        :param second:
        :param comparer:
        :return:
        """
    @classmethod
    @overload
    def First(cls, source: IEnumerable[TSource]) -> TSource:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def First(cls, source: IEnumerable[TSource], predicate: Func[TSource, bool]) -> TSource:
        """

        :param source:
        :param predicate:
        :return:
        """
    @classmethod
    @overload
    def FirstOrDefault(cls, source: IEnumerable[TSource]) -> TSource:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def FirstOrDefault(
        cls, source: IEnumerable[TSource], predicate: Func[TSource, bool]
    ) -> TSource:
        """

        :param source:
        :param predicate:
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
    @overload
    def GroupBy(
        cls, source: IEnumerable[TSource], keySelector: Func[TSource, TKey]
    ) -> IEnumerable[IGrouping, TSource]:
        """

        :param source:
        :param keySelector:
        :return:
        """
    @classmethod
    @overload
    def GroupBy(
        cls,
        source: IEnumerable[TSource],
        keySelector: Func[TSource, TKey],
        comparer: IEqualityComparer[TKey],
    ) -> IEnumerable[IGrouping, TSource]:
        """

        :param source:
        :param keySelector:
        :param comparer:
        :return:
        """
    @classmethod
    @overload
    def GroupBy(
        cls,
        source: IEnumerable[TSource],
        keySelector: Func[TSource, TKey],
        resultSelector: Func[TKey, IEnumerable[TSource], TResult],
    ) -> IEnumerable[TResult]:
        """

        :param source:
        :param keySelector:
        :param resultSelector:
        :return:
        """
    @classmethod
    @overload
    def GroupBy(
        cls,
        source: IEnumerable[TSource],
        keySelector: Func[TSource, TKey],
        elementSelector: Func[TSource, TElement],
    ) -> IEnumerable[IGrouping, TElement]:
        """

        :param source:
        :param keySelector:
        :param elementSelector:
        :return:
        """
    @classmethod
    @overload
    def GroupBy(
        cls,
        source: IEnumerable[TSource],
        keySelector: Func[TSource, TKey],
        resultSelector: Func[TKey, IEnumerable[TSource], TResult],
        comparer: IEqualityComparer[TKey],
    ) -> IEnumerable[TResult]:
        """

        :param source:
        :param keySelector:
        :param resultSelector:
        :param comparer:
        :return:
        """
    @classmethod
    @overload
    def GroupBy(
        cls,
        source: IEnumerable[TSource],
        keySelector: Func[TSource, TKey],
        elementSelector: Func[TSource, TElement],
        comparer: IEqualityComparer[TKey],
    ) -> IEnumerable[IGrouping, TElement]:
        """

        :param source:
        :param keySelector:
        :param elementSelector:
        :param comparer:
        :return:
        """
    @classmethod
    @overload
    def GroupBy(
        cls,
        source: IEnumerable[TSource],
        keySelector: Func[TSource, TKey],
        elementSelector: Func[TSource, TElement],
        resultSelector: Func[TKey, IEnumerable[TElement], TResult],
    ) -> IEnumerable[TResult]:
        """

        :param source:
        :param keySelector:
        :param elementSelector:
        :param resultSelector:
        :return:
        """
    @classmethod
    @overload
    def GroupBy(
        cls,
        source: IEnumerable[TSource],
        keySelector: Func[TSource, TKey],
        elementSelector: Func[TSource, TElement],
        resultSelector: Func[TKey, IEnumerable[TElement], TResult],
        comparer: IEqualityComparer[TKey],
    ) -> IEnumerable[TResult]:
        """

        :param source:
        :param keySelector:
        :param elementSelector:
        :param resultSelector:
        :param comparer:
        :return:
        """
    @classmethod
    @overload
    def GroupJoin(
        cls,
        outer: IEnumerable[TOuter],
        inner: IEnumerable[TInner],
        outerKeySelector: Func[TOuter, TKey],
        innerKeySelector: Func[TInner, TKey],
        resultSelector: Func[TOuter, IEnumerable[TInner], TResult],
    ) -> IEnumerable[TResult]:
        """

        :param outer:
        :param inner:
        :param outerKeySelector:
        :param innerKeySelector:
        :param resultSelector:
        :return:
        """
    @classmethod
    @overload
    def GroupJoin(
        cls,
        outer: IEnumerable[TOuter],
        inner: IEnumerable[TInner],
        outerKeySelector: Func[TOuter, TKey],
        innerKeySelector: Func[TInner, TKey],
        resultSelector: Func[TOuter, IEnumerable[TInner], TResult],
        comparer: IEqualityComparer[TKey],
    ) -> IEnumerable[TResult]:
        """

        :param outer:
        :param inner:
        :param outerKeySelector:
        :param innerKeySelector:
        :param resultSelector:
        :param comparer:
        :return:
        """
    @classmethod
    @overload
    def Intersect(
        cls, first: IEnumerable[TSource], second: IEnumerable[TSource]
    ) -> IEnumerable[TSource]:
        """

        :param first:
        :param second:
        :return:
        """
    @classmethod
    @overload
    def Intersect(
        cls,
        first: IEnumerable[TSource],
        second: IEnumerable[TSource],
        comparer: IEqualityComparer[TSource],
    ) -> IEnumerable[TSource]:
        """

        :param first:
        :param second:
        :param comparer:
        :return:
        """
    @classmethod
    @overload
    def Join(
        cls,
        outer: IEnumerable[TOuter],
        inner: IEnumerable[TInner],
        outerKeySelector: Func[TOuter, TKey],
        innerKeySelector: Func[TInner, TKey],
        resultSelector: Func[TOuter, TInner, TResult],
    ) -> IEnumerable[TResult]:
        """

        :param outer:
        :param inner:
        :param outerKeySelector:
        :param innerKeySelector:
        :param resultSelector:
        :return:
        """
    @classmethod
    @overload
    def Join(
        cls,
        outer: IEnumerable[TOuter],
        inner: IEnumerable[TInner],
        outerKeySelector: Func[TOuter, TKey],
        innerKeySelector: Func[TInner, TKey],
        resultSelector: Func[TOuter, TInner, TResult],
        comparer: IEqualityComparer[TKey],
    ) -> IEnumerable[TResult]:
        """

        :param outer:
        :param inner:
        :param outerKeySelector:
        :param innerKeySelector:
        :param resultSelector:
        :param comparer:
        :return:
        """
    @classmethod
    @overload
    def Last(cls, source: IEnumerable[TSource]) -> TSource:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Last(cls, source: IEnumerable[TSource], predicate: Func[TSource, bool]) -> TSource:
        """

        :param source:
        :param predicate:
        :return:
        """
    @classmethod
    @overload
    def LastOrDefault(cls, source: IEnumerable[TSource]) -> TSource:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def LastOrDefault(cls, source: IEnumerable[TSource], predicate: Func[TSource, bool]) -> TSource:
        """

        :param source:
        :param predicate:
        :return:
        """
    @classmethod
    @overload
    def LongCount(cls, source: IEnumerable[TSource]) -> int:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def LongCount(cls, source: IEnumerable[TSource], predicate: Func[TSource, bool]) -> int:
        """

        :param source:
        :param predicate:
        :return:
        """
    @classmethod
    @overload
    def Max(cls, source: IEnumerable[TSource]) -> TSource:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Max(cls, source: IEnumerable[Optional[Decimal]]) -> Optional[Decimal]:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Max(cls, source: IEnumerable[Decimal]) -> Decimal:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Max(cls, source: IEnumerable[Optional[float]]) -> Optional[float]:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Max(cls, source: IEnumerable[float]) -> float:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Max(cls, source: IEnumerable[Optional[int]]) -> Optional[int]:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Max(cls, source: IEnumerable[int]) -> int:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Max(cls, source: IEnumerable[Optional[int]]) -> Optional[int]:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Max(cls, source: IEnumerable[int]) -> int:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Max(cls, source: IEnumerable[Optional[float]]) -> Optional[float]:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Max(cls, source: IEnumerable[float]) -> float:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Max(cls, source: IEnumerable[TSource], selector: Func[TSource, TResult]) -> TResult:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    @overload
    def Max(
        cls, source: IEnumerable[TSource], selector: Func[TSource, Optional[Decimal]]
    ) -> Optional[Decimal]:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    @overload
    def Max(cls, source: IEnumerable[TSource], selector: Func[TSource, Decimal]) -> Decimal:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    @overload
    def Max(
        cls, source: IEnumerable[TSource], selector: Func[TSource, Optional[float]]
    ) -> Optional[float]:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    @overload
    def Max(cls, source: IEnumerable[TSource], selector: Func[TSource, float]) -> float:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    @overload
    def Max(
        cls, source: IEnumerable[TSource], selector: Func[TSource, Optional[int]]
    ) -> Optional[int]:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    @overload
    def Max(cls, source: IEnumerable[TSource], selector: Func[TSource, int]) -> int:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    @overload
    def Max(
        cls, source: IEnumerable[TSource], selector: Func[TSource, Optional[int]]
    ) -> Optional[int]:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    @overload
    def Max(cls, source: IEnumerable[TSource], selector: Func[TSource, int]) -> int:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    @overload
    def Max(
        cls, source: IEnumerable[TSource], selector: Func[TSource, Optional[float]]
    ) -> Optional[float]:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    @overload
    def Max(cls, source: IEnumerable[TSource], selector: Func[TSource, float]) -> float:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    @overload
    def Min(cls, source: IEnumerable[TSource]) -> TSource:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Min(cls, source: IEnumerable[Optional[Decimal]]) -> Optional[Decimal]:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Min(cls, source: IEnumerable[Decimal]) -> Decimal:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Min(cls, source: IEnumerable[Optional[float]]) -> Optional[float]:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Min(cls, source: IEnumerable[float]) -> float:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Min(cls, source: IEnumerable[Optional[int]]) -> Optional[int]:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Min(cls, source: IEnumerable[int]) -> int:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Min(cls, source: IEnumerable[Optional[int]]) -> Optional[int]:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Min(cls, source: IEnumerable[int]) -> int:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Min(cls, source: IEnumerable[Optional[float]]) -> Optional[float]:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Min(cls, source: IEnumerable[float]) -> float:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Min(cls, source: IEnumerable[TSource], selector: Func[TSource, TResult]) -> TResult:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    @overload
    def Min(
        cls, source: IEnumerable[TSource], selector: Func[TSource, Optional[Decimal]]
    ) -> Optional[Decimal]:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    @overload
    def Min(cls, source: IEnumerable[TSource], selector: Func[TSource, Decimal]) -> Decimal:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    @overload
    def Min(
        cls, source: IEnumerable[TSource], selector: Func[TSource, Optional[float]]
    ) -> Optional[float]:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    @overload
    def Min(cls, source: IEnumerable[TSource], selector: Func[TSource, float]) -> float:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    @overload
    def Min(
        cls, source: IEnumerable[TSource], selector: Func[TSource, Optional[int]]
    ) -> Optional[int]:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    @overload
    def Min(cls, source: IEnumerable[TSource], selector: Func[TSource, int]) -> int:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    @overload
    def Min(
        cls, source: IEnumerable[TSource], selector: Func[TSource, Optional[int]]
    ) -> Optional[int]:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    @overload
    def Min(cls, source: IEnumerable[TSource], selector: Func[TSource, int]) -> int:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    @overload
    def Min(
        cls, source: IEnumerable[TSource], selector: Func[TSource, Optional[float]]
    ) -> Optional[float]:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    @overload
    def Min(cls, source: IEnumerable[TSource], selector: Func[TSource, float]) -> float:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    def OfType(cls, source: IEnumerable) -> IEnumerable[TResult]:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def OrderBy(
        cls, source: IEnumerable[TSource], keySelector: Func[TSource, TKey]
    ) -> IOrderedEnumerable[TSource]:
        """

        :param source:
        :param keySelector:
        :return:
        """
    @classmethod
    @overload
    def OrderBy(
        cls,
        source: IEnumerable[TSource],
        keySelector: Func[TSource, TKey],
        comparer: IComparer[TKey],
    ) -> IOrderedEnumerable[TSource]:
        """

        :param source:
        :param keySelector:
        :param comparer:
        :return:
        """
    @classmethod
    @overload
    def OrderByDescending(
        cls, source: IEnumerable[TSource], keySelector: Func[TSource, TKey]
    ) -> IOrderedEnumerable[TSource]:
        """

        :param source:
        :param keySelector:
        :return:
        """
    @classmethod
    @overload
    def OrderByDescending(
        cls,
        source: IEnumerable[TSource],
        keySelector: Func[TSource, TKey],
        comparer: IComparer[TKey],
    ) -> IOrderedEnumerable[TSource]:
        """

        :param source:
        :param keySelector:
        :param comparer:
        :return:
        """
    @classmethod
    def Prepend(cls, source: IEnumerable[TSource], element: TSource) -> IEnumerable[TSource]:
        """

        :param source:
        :param element:
        :return:
        """
    @classmethod
    def Range(cls, start: int, count: int) -> IEnumerable[int]:
        """

        :param start:
        :param count:
        :return:
        """
    @classmethod
    def Repeat(cls, element: TResult, count: int) -> IEnumerable[TResult]:
        """

        :param element:
        :param count:
        :return:
        """
    @classmethod
    def Reverse(cls, source: IEnumerable[TSource]) -> IEnumerable[TSource]:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Select(
        cls, source: IEnumerable[TSource], selector: Func[TSource, TResult]
    ) -> IEnumerable[TResult]:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    @overload
    def Select(
        cls, source: IEnumerable[TSource], selector: Func[TSource, int, TResult]
    ) -> IEnumerable[TResult]:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    @overload
    def SelectMany(
        cls, source: IEnumerable[TSource], selector: Func[TSource, IEnumerable[TResult]]
    ) -> IEnumerable[TResult]:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    @overload
    def SelectMany(
        cls, source: IEnumerable[TSource], selector: Func[TSource, int, IEnumerable[TResult]]
    ) -> IEnumerable[TResult]:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    @overload
    def SelectMany(
        cls,
        source: IEnumerable[TSource],
        collectionSelector: Func[TSource, IEnumerable[TCollection]],
        resultSelector: Func[TSource, TCollection, TResult],
    ) -> IEnumerable[TResult]:
        """

        :param source:
        :param collectionSelector:
        :param resultSelector:
        :return:
        """
    @classmethod
    @overload
    def SelectMany(
        cls,
        source: IEnumerable[TSource],
        collectionSelector: Func[TSource, int, IEnumerable[TCollection]],
        resultSelector: Func[TSource, TCollection, TResult],
    ) -> IEnumerable[TResult]:
        """

        :param source:
        :param collectionSelector:
        :param resultSelector:
        :return:
        """
    @classmethod
    @overload
    def SequenceEqual(cls, first: IEnumerable[TSource], second: IEnumerable[TSource]) -> bool:
        """

        :param first:
        :param second:
        :return:
        """
    @classmethod
    @overload
    def SequenceEqual(
        cls,
        first: IEnumerable[TSource],
        second: IEnumerable[TSource],
        comparer: IEqualityComparer[TSource],
    ) -> bool:
        """

        :param first:
        :param second:
        :param comparer:
        :return:
        """
    @classmethod
    @overload
    def Single(cls, source: IEnumerable[TSource]) -> TSource:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Single(cls, source: IEnumerable[TSource], predicate: Func[TSource, bool]) -> TSource:
        """

        :param source:
        :param predicate:
        :return:
        """
    @classmethod
    @overload
    def SingleOrDefault(cls, source: IEnumerable[TSource]) -> TSource:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def SingleOrDefault(
        cls, source: IEnumerable[TSource], predicate: Func[TSource, bool]
    ) -> TSource:
        """

        :param source:
        :param predicate:
        :return:
        """
    @classmethod
    def Skip(cls, source: IEnumerable[TSource], count: int) -> IEnumerable[TSource]:
        """

        :param source:
        :param count:
        :return:
        """
    @classmethod
    @overload
    def SkipWhile(
        cls, source: IEnumerable[TSource], predicate: Func[TSource, bool]
    ) -> IEnumerable[TSource]:
        """

        :param source:
        :param predicate:
        :return:
        """
    @classmethod
    @overload
    def SkipWhile(
        cls, source: IEnumerable[TSource], predicate: Func[TSource, int, bool]
    ) -> IEnumerable[TSource]:
        """

        :param source:
        :param predicate:
        :return:
        """
    @classmethod
    @overload
    def Sum(cls, source: IEnumerable[Optional[Decimal]]) -> Optional[Decimal]:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Sum(cls, source: IEnumerable[Decimal]) -> Decimal:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Sum(cls, source: IEnumerable[Optional[float]]) -> Optional[float]:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Sum(cls, source: IEnumerable[float]) -> float:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Sum(cls, source: IEnumerable[Optional[int]]) -> Optional[int]:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Sum(cls, source: IEnumerable[int]) -> int:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Sum(cls, source: IEnumerable[Optional[int]]) -> Optional[int]:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Sum(cls, source: IEnumerable[int]) -> int:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Sum(cls, source: IEnumerable[Optional[float]]) -> Optional[float]:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Sum(cls, source: IEnumerable[float]) -> float:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Sum(
        cls, source: IEnumerable[TSource], selector: Func[TSource, Optional[Decimal]]
    ) -> Optional[Decimal]:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    @overload
    def Sum(cls, source: IEnumerable[TSource], selector: Func[TSource, Decimal]) -> Decimal:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    @overload
    def Sum(
        cls, source: IEnumerable[TSource], selector: Func[TSource, Optional[float]]
    ) -> Optional[float]:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    @overload
    def Sum(cls, source: IEnumerable[TSource], selector: Func[TSource, float]) -> float:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    @overload
    def Sum(
        cls, source: IEnumerable[TSource], selector: Func[TSource, Optional[int]]
    ) -> Optional[int]:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    @overload
    def Sum(cls, source: IEnumerable[TSource], selector: Func[TSource, int]) -> int:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    @overload
    def Sum(
        cls, source: IEnumerable[TSource], selector: Func[TSource, Optional[int]]
    ) -> Optional[int]:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    @overload
    def Sum(cls, source: IEnumerable[TSource], selector: Func[TSource, int]) -> int:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    @overload
    def Sum(
        cls, source: IEnumerable[TSource], selector: Func[TSource, Optional[float]]
    ) -> Optional[float]:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    @overload
    def Sum(cls, source: IEnumerable[TSource], selector: Func[TSource, float]) -> float:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    def Take(cls, source: IEnumerable[TSource], count: int) -> IEnumerable[TSource]:
        """

        :param source:
        :param count:
        :return:
        """
    @classmethod
    @overload
    def TakeWhile(
        cls, source: IEnumerable[TSource], predicate: Func[TSource, bool]
    ) -> IEnumerable[TSource]:
        """

        :param source:
        :param predicate:
        :return:
        """
    @classmethod
    @overload
    def TakeWhile(
        cls, source: IEnumerable[TSource], predicate: Func[TSource, int, bool]
    ) -> IEnumerable[TSource]:
        """

        :param source:
        :param predicate:
        :return:
        """
    @classmethod
    @overload
    def ThenBy(
        cls, source: IOrderedEnumerable[TSource], keySelector: Func[TSource, TKey]
    ) -> IOrderedEnumerable[TSource]:
        """

        :param source:
        :param keySelector:
        :return:
        """
    @classmethod
    @overload
    def ThenBy(
        cls,
        source: IOrderedEnumerable[TSource],
        keySelector: Func[TSource, TKey],
        comparer: IComparer[TKey],
    ) -> IOrderedEnumerable[TSource]:
        """

        :param source:
        :param keySelector:
        :param comparer:
        :return:
        """
    @classmethod
    @overload
    def ThenByDescending(
        cls, source: IOrderedEnumerable[TSource], keySelector: Func[TSource, TKey]
    ) -> IOrderedEnumerable[TSource]:
        """

        :param source:
        :param keySelector:
        :return:
        """
    @classmethod
    @overload
    def ThenByDescending(
        cls,
        source: IOrderedEnumerable[TSource],
        keySelector: Func[TSource, TKey],
        comparer: IComparer[TKey],
    ) -> IOrderedEnumerable[TSource]:
        """

        :param source:
        :param keySelector:
        :param comparer:
        :return:
        """
    @classmethod
    def ToArray(cls, source: IEnumerable[TSource]) -> Array[TSource]:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def ToDictionary(
        cls, source: IEnumerable[TSource], keySelector: Func[TSource, TKey]
    ) -> Dictionary[TKey, TSource]:
        """

        :param source:
        :param keySelector:
        :return:
        """
    @classmethod
    @overload
    def ToDictionary(
        cls,
        source: IEnumerable[TSource],
        keySelector: Func[TSource, TKey],
        comparer: IEqualityComparer[TKey],
    ) -> Dictionary[TKey, TSource]:
        """

        :param source:
        :param keySelector:
        :param comparer:
        :return:
        """
    @classmethod
    @overload
    def ToDictionary(
        cls,
        source: IEnumerable[TSource],
        keySelector: Func[TSource, TKey],
        elementSelector: Func[TSource, TElement],
    ) -> Dictionary[TKey, TElement]:
        """

        :param source:
        :param keySelector:
        :param elementSelector:
        :return:
        """
    @classmethod
    @overload
    def ToDictionary(
        cls,
        source: IEnumerable[TSource],
        keySelector: Func[TSource, TKey],
        elementSelector: Func[TSource, TElement],
        comparer: IEqualityComparer[TKey],
    ) -> Dictionary[TKey, TElement]:
        """

        :param source:
        :param keySelector:
        :param elementSelector:
        :param comparer:
        :return:
        """
    @classmethod
    @overload
    def ToHashSet(cls, source: IEnumerable[TSource]) -> HashSet[TSource]:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def ToHashSet(
        cls, source: IEnumerable[TSource], comparer: IEqualityComparer[TSource]
    ) -> HashSet[TSource]:
        """

        :param source:
        :param comparer:
        :return:
        """
    @classmethod
    def ToList(cls, source: IEnumerable[TSource]) -> List[TSource]:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def ToLookup(
        cls, source: IEnumerable[TSource], keySelector: Func[TSource, TKey]
    ) -> ILookup[TKey, TSource]:
        """

        :param source:
        :param keySelector:
        :return:
        """
    @classmethod
    @overload
    def ToLookup(
        cls,
        source: IEnumerable[TSource],
        keySelector: Func[TSource, TKey],
        comparer: IEqualityComparer[TKey],
    ) -> ILookup[TKey, TSource]:
        """

        :param source:
        :param keySelector:
        :param comparer:
        :return:
        """
    @classmethod
    @overload
    def ToLookup(
        cls,
        source: IEnumerable[TSource],
        keySelector: Func[TSource, TKey],
        elementSelector: Func[TSource, TElement],
    ) -> ILookup[TKey, TElement]:
        """

        :param source:
        :param keySelector:
        :param elementSelector:
        :return:
        """
    @classmethod
    @overload
    def ToLookup(
        cls,
        source: IEnumerable[TSource],
        keySelector: Func[TSource, TKey],
        elementSelector: Func[TSource, TElement],
        comparer: IEqualityComparer[TKey],
    ) -> ILookup[TKey, TElement]:
        """

        :param source:
        :param keySelector:
        :param elementSelector:
        :param comparer:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @classmethod
    @overload
    def Union(
        cls, first: IEnumerable[TSource], second: IEnumerable[TSource]
    ) -> IEnumerable[TSource]:
        """

        :param first:
        :param second:
        :return:
        """
    @classmethod
    @overload
    def Union(
        cls,
        first: IEnumerable[TSource],
        second: IEnumerable[TSource],
        comparer: IEqualityComparer[TSource],
    ) -> IEnumerable[TSource]:
        """

        :param first:
        :param second:
        :param comparer:
        :return:
        """
    @classmethod
    @overload
    def Where(
        cls, source: IEnumerable[TSource], predicate: Func[TSource, bool]
    ) -> IEnumerable[TSource]:
        """

        :param source:
        :param predicate:
        :return:
        """
    @classmethod
    @overload
    def Where(
        cls, source: IEnumerable[TSource], predicate: Func[TSource, int, bool]
    ) -> IEnumerable[TSource]:
        """

        :param source:
        :param predicate:
        :return:
        """
    @classmethod
    def Zip(
        cls,
        first: IEnumerable[TFirst],
        second: IEnumerable[TSecond],
        resultSelector: Func[TFirst, TSecond, TResult],
    ) -> IEnumerable[TResult]:
        """

        :param first:
        :param second:
        :param resultSelector:
        :return:
        """

class EnumerableExecutor(ABC, Object):
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

class EnumerableExecutor(Generic[T], EnumerableExecutor):
    """"""

    def __init__(self, expression: Expression):
        """

        :param expression:
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

class EnumerableQuery(ABC, Object):
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

class EnumerableQuery(
    Generic[T],
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
    def __init__(self, enumerable: IEnumerable[T]):
        """

        :param enumerable:
        """
    @overload
    def __init__(self, expression: Expression):
        """

        :param expression:
        """
    @property
    def ElementType(self) -> Type:
        """

        :return:
        """
    @property
    def Expression(self) -> Expression:
        """

        :return:
        """
    @property
    def Provider(self) -> IQueryProvider:
        """

        :return:
        """
    def CreateQuery(self, expression: Expression) -> IQueryable[TElement]:
        """

        :param expression:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def Execute(self, expression: Expression) -> TResult:
        """

        :param expression:
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

class EnumerableRewriter(OldExpressionVisitor):
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

class EnumerableSorter(ABC, Generic[TElement], Object):
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

class EnumerableSorter(Generic[TElement, TKey], EnumerableSorter[TElement]):
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

class Error(ABC, Object):
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

class GroupedEnumerable(
    Generic[TSource, TKey, TElement, TResult], Object, IEnumerable[TResult], IEnumerable
):
    """"""

    def __init__(
        self,
        source: IEnumerable[TSource],
        keySelector: Func[TSource, TKey],
        elementSelector: Func[TSource, TElement],
        resultSelector: Func[TKey, IEnumerable[TElement], TResult],
        comparer: IEqualityComparer[TKey],
    ):
        """

        :param source:
        :param keySelector:
        :param elementSelector:
        :param resultSelector:
        :param comparer:
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
    def __iter__(self) -> Iterator[TResult]:
        """

        :return:
        """

class GroupedEnumerable(
    Generic[TSource, TKey, TElement], Object, IEnumerable[IGrouping, TElement], IEnumerable
):
    """"""

    def __init__(
        self,
        source: IEnumerable[TSource],
        keySelector: Func[TSource, TKey],
        elementSelector: Func[TSource, TElement],
        comparer: IEqualityComparer[TKey],
    ):
        """

        :param source:
        :param keySelector:
        :param elementSelector:
        :param comparer:
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
    def __iter__(self) -> Iterator[IGrouping, TElement]:
        """

        :return:
        """

class IGrouping(Generic[TElement, TKey], IEnumerable[TElement], IEnumerable):
    """"""

    @property
    def Key(self) -> TKey:
        """

        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
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

class IIListProvider(Generic[TElement], IEnumerable[TElement], IEnumerable):
    """"""

    def GetCount(self, onlyIfCheap: bool) -> int:
        """

        :param onlyIfCheap:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    def ToArray(self) -> Array[TElement]:
        """

        :return:
        """
    def ToList(self) -> List[TElement]:
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

class ILookup(Generic[TElement, TKey], IEnumerable[IGrouping, TElement], IEnumerable):
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
    def GetEnumerator(self) -> IEnumerator:
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

class IOrderedEnumerable(Generic[TElement], IEnumerable[TElement], IEnumerable):
    """"""

    def CreateOrderedEnumerable(
        self, keySelector: Func[TElement, TKey], comparer: IComparer[TKey], descending: bool
    ) -> IOrderedEnumerable[TElement]:
        """

        :param keySelector:
        :param comparer:
        :param descending:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
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

class IOrderedQueryable(IEnumerable, IQueryable):
    """"""

    @property
    def ElementType(self) -> Type:
        """

        :return:
        """
    @property
    def Expression(self) -> Expression:
        """

        :return:
        """
    @property
    def Provider(self) -> IQueryProvider:
        """

        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """

class IOrderedQueryable(
    Generic[T], IEnumerable[T], IEnumerable, IOrderedQueryable, IQueryable, IQueryable[T]
):
    """"""

    @property
    def ElementType(self) -> Type:
        """

        :return:
        """
    @property
    def Expression(self) -> Expression:
        """

        :return:
        """
    @property
    def Provider(self) -> IQueryProvider:
        """

        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
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

class IQueryProvider:
    """"""

    def CreateQuery(self, expression: Expression) -> IQueryable[TElement]:
        """

        :param expression:
        :return:
        """
    def Execute(self, expression: Expression) -> TResult:
        """

        :param expression:
        :return:
        """

class IQueryable(IEnumerable):
    """"""

    @property
    def ElementType(self) -> Type:
        """

        :return:
        """
    @property
    def Expression(self) -> Expression:
        """

        :return:
        """
    @property
    def Provider(self) -> IQueryProvider:
        """

        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """

class IQueryable(Generic[T], IEnumerable[T], IEnumerable, IQueryable):
    """"""

    @property
    def ElementType(self) -> Type:
        """

        :return:
        """
    @property
    def Expression(self) -> Expression:
        """

        :return:
        """
    @property
    def Provider(self) -> IQueryProvider:
        """

        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
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

class IdentityFunction(Generic[TElement], Object):
    """"""

    def __init__(self):
        """"""
    @classmethod
    @property
    def Instance(cls) -> Func[TElement, TElement]:
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
    def ApplyResultSelector(
        self, resultSelector: Func[TKey, IEnumerable[TElement], TResult]
    ) -> IEnumerable[TResult]:
        """

        :param resultSelector:
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

class OrderedEnumerable(
    ABC, Generic[TElement], Object, IEnumerable[TElement], IEnumerable, IOrderedEnumerable[TElement]
):
    """"""

    def CreateOrderedEnumerable(
        self, keySelector: Func[TElement, TKey], comparer: IComparer[TKey], descending: bool
    ) -> IOrderedEnumerable[TElement]:
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

class OrderedEnumerable(
    Generic[TElement, TKey],
    OrderedEnumerable[TElement],
    IEnumerable[TElement],
    IEnumerable,
    IOrderedEnumerable[TElement],
):
    """"""

    def CreateOrderedEnumerable(
        self, keySelector: Func[TElement, TKey], comparer: IComparer[TKey], descending: bool
    ) -> IOrderedEnumerable[TElement]:
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

class OrderedParallelQuery(
    Generic[TSource], ParallelQuery[TSource], IEnumerable[TSource], IEnumerable
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

class ParallelEnumerable(ABC, Object):
    """"""

    @classmethod
    @overload
    def Aggregate(
        cls, source: ParallelQuery[TSource], func: Func[TSource, TSource, TSource]
    ) -> TSource:
        """

        :param source:
        :param func:
        :return:
        """
    @classmethod
    @overload
    def Aggregate(
        cls,
        source: ParallelQuery[TSource],
        seed: TAccumulate,
        func: Func[TAccumulate, TSource, TAccumulate],
    ) -> TAccumulate:
        """

        :param source:
        :param seed:
        :param func:
        :return:
        """
    @classmethod
    @overload
    def Aggregate(
        cls,
        source: ParallelQuery[TSource],
        seed: TAccumulate,
        func: Func[TAccumulate, TSource, TAccumulate],
        resultSelector: Func[TAccumulate, TResult],
    ) -> TResult:
        """

        :param source:
        :param seed:
        :param func:
        :param resultSelector:
        :return:
        """
    @classmethod
    @overload
    def Aggregate(
        cls,
        source: ParallelQuery[TSource],
        seed: TAccumulate,
        updateAccumulatorFunc: Func[TAccumulate, TSource, TAccumulate],
        combineAccumulatorsFunc: Func[TAccumulate, TAccumulate, TAccumulate],
        resultSelector: Func[TAccumulate, TResult],
    ) -> TResult:
        """

        :param source:
        :param seed:
        :param updateAccumulatorFunc:
        :param combineAccumulatorsFunc:
        :param resultSelector:
        :return:
        """
    @classmethod
    @overload
    def Aggregate(
        cls,
        source: ParallelQuery[TSource],
        seedFactory: Func[TAccumulate],
        updateAccumulatorFunc: Func[TAccumulate, TSource, TAccumulate],
        combineAccumulatorsFunc: Func[TAccumulate, TAccumulate, TAccumulate],
        resultSelector: Func[TAccumulate, TResult],
    ) -> TResult:
        """

        :param source:
        :param seedFactory:
        :param updateAccumulatorFunc:
        :param combineAccumulatorsFunc:
        :param resultSelector:
        :return:
        """
    @classmethod
    def All(cls, source: ParallelQuery[TSource], predicate: Func[TSource, bool]) -> bool:
        """

        :param source:
        :param predicate:
        :return:
        """
    @classmethod
    @overload
    def Any(cls, source: ParallelQuery[TSource]) -> bool:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Any(cls, source: ParallelQuery[TSource], predicate: Func[TSource, bool]) -> bool:
        """

        :param source:
        :param predicate:
        :return:
        """
    @classmethod
    def AsEnumerable(cls, source: ParallelQuery[TSource]) -> IEnumerable[TSource]:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def AsOrdered(cls, source: ParallelQuery) -> ParallelQuery:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def AsOrdered(cls, source: ParallelQuery[TSource]) -> ParallelQuery[TSource]:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def AsParallel(cls, source: Partitioner[TSource]) -> ParallelQuery[TSource]:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def AsParallel(cls, source: IEnumerable[TSource]) -> ParallelQuery[TSource]:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def AsParallel(cls, source: IEnumerable) -> ParallelQuery:
        """

        :param source:
        :return:
        """
    @classmethod
    def AsSequential(cls, source: ParallelQuery[TSource]) -> IEnumerable[TSource]:
        """

        :param source:
        :return:
        """
    @classmethod
    def AsUnordered(cls, source: ParallelQuery[TSource]) -> ParallelQuery[TSource]:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Average(cls, source: ParallelQuery[Optional[Decimal]]) -> Optional[Decimal]:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Average(cls, source: ParallelQuery[Decimal]) -> Decimal:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Average(cls, source: ParallelQuery[Optional[float]]) -> Optional[float]:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Average(cls, source: ParallelQuery[float]) -> float:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Average(cls, source: ParallelQuery[Optional[int]]) -> Optional[float]:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Average(cls, source: ParallelQuery[int]) -> float:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Average(cls, source: ParallelQuery[Optional[int]]) -> Optional[float]:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Average(cls, source: ParallelQuery[int]) -> float:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Average(cls, source: ParallelQuery[Optional[float]]) -> Optional[float]:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Average(cls, source: ParallelQuery[float]) -> float:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Average(
        cls, source: ParallelQuery[TSource], selector: Func[TSource, Optional[Decimal]]
    ) -> Optional[Decimal]:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    @overload
    def Average(cls, source: ParallelQuery[TSource], selector: Func[TSource, Decimal]) -> Decimal:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    @overload
    def Average(
        cls, source: ParallelQuery[TSource], selector: Func[TSource, Optional[float]]
    ) -> Optional[float]:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    @overload
    def Average(cls, source: ParallelQuery[TSource], selector: Func[TSource, float]) -> float:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    @overload
    def Average(
        cls, source: ParallelQuery[TSource], selector: Func[TSource, Optional[int]]
    ) -> Optional[float]:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    @overload
    def Average(cls, source: ParallelQuery[TSource], selector: Func[TSource, int]) -> float:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    @overload
    def Average(
        cls, source: ParallelQuery[TSource], selector: Func[TSource, Optional[int]]
    ) -> Optional[float]:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    @overload
    def Average(cls, source: ParallelQuery[TSource], selector: Func[TSource, int]) -> float:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    @overload
    def Average(
        cls, source: ParallelQuery[TSource], selector: Func[TSource, Optional[float]]
    ) -> Optional[float]:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    @overload
    def Average(cls, source: ParallelQuery[TSource], selector: Func[TSource, float]) -> float:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    def Cast(cls, source: ParallelQuery) -> ParallelQuery[TResult]:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Concat(
        cls, first: ParallelQuery[TSource], second: IEnumerable[TSource]
    ) -> ParallelQuery[TSource]:
        """

        :param first:
        :param second:
        :return:
        """
    @classmethod
    @overload
    def Concat(
        cls, first: ParallelQuery[TSource], second: ParallelQuery[TSource]
    ) -> ParallelQuery[TSource]:
        """

        :param first:
        :param second:
        :return:
        """
    @classmethod
    @overload
    def Contains(cls, source: ParallelQuery[TSource], value: TSource) -> bool:
        """

        :param source:
        :param value:
        :return:
        """
    @classmethod
    @overload
    def Contains(
        cls, source: ParallelQuery[TSource], value: TSource, comparer: IEqualityComparer[TSource]
    ) -> bool:
        """

        :param source:
        :param value:
        :param comparer:
        :return:
        """
    @classmethod
    @overload
    def Count(cls, source: ParallelQuery[TSource]) -> int:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Count(cls, source: ParallelQuery[TSource], predicate: Func[TSource, bool]) -> int:
        """

        :param source:
        :param predicate:
        :return:
        """
    @classmethod
    @overload
    def DefaultIfEmpty(cls, source: ParallelQuery[TSource]) -> ParallelQuery[TSource]:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def DefaultIfEmpty(
        cls, source: ParallelQuery[TSource], defaultValue: TSource
    ) -> ParallelQuery[TSource]:
        """

        :param source:
        :param defaultValue:
        :return:
        """
    @classmethod
    @overload
    def Distinct(cls, source: ParallelQuery[TSource]) -> ParallelQuery[TSource]:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Distinct(
        cls, source: ParallelQuery[TSource], comparer: IEqualityComparer[TSource]
    ) -> ParallelQuery[TSource]:
        """

        :param source:
        :param comparer:
        :return:
        """
    @classmethod
    def ElementAt(cls, source: ParallelQuery[TSource], index: int) -> TSource:
        """

        :param source:
        :param index:
        :return:
        """
    @classmethod
    def ElementAtOrDefault(cls, source: ParallelQuery[TSource], index: int) -> TSource:
        """

        :param source:
        :param index:
        :return:
        """
    @classmethod
    def Empty(cls) -> ParallelQuery[TResult]:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @classmethod
    @overload
    def Except(
        cls, first: ParallelQuery[TSource], second: IEnumerable[TSource]
    ) -> ParallelQuery[TSource]:
        """

        :param first:
        :param second:
        :return:
        """
    @classmethod
    @overload
    def Except(
        cls, first: ParallelQuery[TSource], second: ParallelQuery[TSource]
    ) -> ParallelQuery[TSource]:
        """

        :param first:
        :param second:
        :return:
        """
    @classmethod
    @overload
    def Except(
        cls,
        first: ParallelQuery[TSource],
        second: IEnumerable[TSource],
        comparer: IEqualityComparer[TSource],
    ) -> ParallelQuery[TSource]:
        """

        :param first:
        :param second:
        :param comparer:
        :return:
        """
    @classmethod
    @overload
    def Except(
        cls,
        first: ParallelQuery[TSource],
        second: ParallelQuery[TSource],
        comparer: IEqualityComparer[TSource],
    ) -> ParallelQuery[TSource]:
        """

        :param first:
        :param second:
        :param comparer:
        :return:
        """
    @classmethod
    @overload
    def First(cls, source: ParallelQuery[TSource]) -> TSource:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def First(cls, source: ParallelQuery[TSource], predicate: Func[TSource, bool]) -> TSource:
        """

        :param source:
        :param predicate:
        :return:
        """
    @classmethod
    @overload
    def FirstOrDefault(cls, source: ParallelQuery[TSource]) -> TSource:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def FirstOrDefault(
        cls, source: ParallelQuery[TSource], predicate: Func[TSource, bool]
    ) -> TSource:
        """

        :param source:
        :param predicate:
        :return:
        """
    @classmethod
    def ForAll(cls, source: ParallelQuery[TSource], action: Action[TSource]) -> None:
        """

        :param source:
        :param action:
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
    @overload
    def GroupBy(
        cls, source: ParallelQuery[TSource], keySelector: Func[TSource, TKey]
    ) -> ParallelQuery[IGrouping, TSource]:
        """

        :param source:
        :param keySelector:
        :return:
        """
    @classmethod
    @overload
    def GroupBy(
        cls,
        source: ParallelQuery[TSource],
        keySelector: Func[TSource, TKey],
        comparer: IEqualityComparer[TKey],
    ) -> ParallelQuery[IGrouping, TSource]:
        """

        :param source:
        :param keySelector:
        :param comparer:
        :return:
        """
    @classmethod
    @overload
    def GroupBy(
        cls,
        source: ParallelQuery[TSource],
        keySelector: Func[TSource, TKey],
        resultSelector: Func[TKey, IEnumerable[TSource], TResult],
    ) -> ParallelQuery[TResult]:
        """

        :param source:
        :param keySelector:
        :param resultSelector:
        :return:
        """
    @classmethod
    @overload
    def GroupBy(
        cls,
        source: ParallelQuery[TSource],
        keySelector: Func[TSource, TKey],
        elementSelector: Func[TSource, TElement],
    ) -> ParallelQuery[IGrouping, TElement]:
        """

        :param source:
        :param keySelector:
        :param elementSelector:
        :return:
        """
    @classmethod
    @overload
    def GroupBy(
        cls,
        source: ParallelQuery[TSource],
        keySelector: Func[TSource, TKey],
        resultSelector: Func[TKey, IEnumerable[TSource], TResult],
        comparer: IEqualityComparer[TKey],
    ) -> ParallelQuery[TResult]:
        """

        :param source:
        :param keySelector:
        :param resultSelector:
        :param comparer:
        :return:
        """
    @classmethod
    @overload
    def GroupBy(
        cls,
        source: ParallelQuery[TSource],
        keySelector: Func[TSource, TKey],
        elementSelector: Func[TSource, TElement],
        comparer: IEqualityComparer[TKey],
    ) -> ParallelQuery[IGrouping, TElement]:
        """

        :param source:
        :param keySelector:
        :param elementSelector:
        :param comparer:
        :return:
        """
    @classmethod
    @overload
    def GroupBy(
        cls,
        source: ParallelQuery[TSource],
        keySelector: Func[TSource, TKey],
        elementSelector: Func[TSource, TElement],
        resultSelector: Func[TKey, IEnumerable[TElement], TResult],
    ) -> ParallelQuery[TResult]:
        """

        :param source:
        :param keySelector:
        :param elementSelector:
        :param resultSelector:
        :return:
        """
    @classmethod
    @overload
    def GroupBy(
        cls,
        source: ParallelQuery[TSource],
        keySelector: Func[TSource, TKey],
        elementSelector: Func[TSource, TElement],
        resultSelector: Func[TKey, IEnumerable[TElement], TResult],
        comparer: IEqualityComparer[TKey],
    ) -> ParallelQuery[TResult]:
        """

        :param source:
        :param keySelector:
        :param elementSelector:
        :param resultSelector:
        :param comparer:
        :return:
        """
    @classmethod
    @overload
    def GroupJoin(
        cls,
        outer: ParallelQuery[TOuter],
        inner: IEnumerable[TInner],
        outerKeySelector: Func[TOuter, TKey],
        innerKeySelector: Func[TInner, TKey],
        resultSelector: Func[TOuter, IEnumerable[TInner], TResult],
    ) -> ParallelQuery[TResult]:
        """

        :param outer:
        :param inner:
        :param outerKeySelector:
        :param innerKeySelector:
        :param resultSelector:
        :return:
        """
    @classmethod
    @overload
    def GroupJoin(
        cls,
        outer: ParallelQuery[TOuter],
        inner: ParallelQuery[TInner],
        outerKeySelector: Func[TOuter, TKey],
        innerKeySelector: Func[TInner, TKey],
        resultSelector: Func[TOuter, IEnumerable[TInner], TResult],
    ) -> ParallelQuery[TResult]:
        """

        :param outer:
        :param inner:
        :param outerKeySelector:
        :param innerKeySelector:
        :param resultSelector:
        :return:
        """
    @classmethod
    @overload
    def GroupJoin(
        cls,
        outer: ParallelQuery[TOuter],
        inner: IEnumerable[TInner],
        outerKeySelector: Func[TOuter, TKey],
        innerKeySelector: Func[TInner, TKey],
        resultSelector: Func[TOuter, IEnumerable[TInner], TResult],
        comparer: IEqualityComparer[TKey],
    ) -> ParallelQuery[TResult]:
        """

        :param outer:
        :param inner:
        :param outerKeySelector:
        :param innerKeySelector:
        :param resultSelector:
        :param comparer:
        :return:
        """
    @classmethod
    @overload
    def GroupJoin(
        cls,
        outer: ParallelQuery[TOuter],
        inner: ParallelQuery[TInner],
        outerKeySelector: Func[TOuter, TKey],
        innerKeySelector: Func[TInner, TKey],
        resultSelector: Func[TOuter, IEnumerable[TInner], TResult],
        comparer: IEqualityComparer[TKey],
    ) -> ParallelQuery[TResult]:
        """

        :param outer:
        :param inner:
        :param outerKeySelector:
        :param innerKeySelector:
        :param resultSelector:
        :param comparer:
        :return:
        """
    @classmethod
    @overload
    def Intersect(
        cls, first: ParallelQuery[TSource], second: IEnumerable[TSource]
    ) -> ParallelQuery[TSource]:
        """

        :param first:
        :param second:
        :return:
        """
    @classmethod
    @overload
    def Intersect(
        cls, first: ParallelQuery[TSource], second: ParallelQuery[TSource]
    ) -> ParallelQuery[TSource]:
        """

        :param first:
        :param second:
        :return:
        """
    @classmethod
    @overload
    def Intersect(
        cls,
        first: ParallelQuery[TSource],
        second: IEnumerable[TSource],
        comparer: IEqualityComparer[TSource],
    ) -> ParallelQuery[TSource]:
        """

        :param first:
        :param second:
        :param comparer:
        :return:
        """
    @classmethod
    @overload
    def Intersect(
        cls,
        first: ParallelQuery[TSource],
        second: ParallelQuery[TSource],
        comparer: IEqualityComparer[TSource],
    ) -> ParallelQuery[TSource]:
        """

        :param first:
        :param second:
        :param comparer:
        :return:
        """
    @classmethod
    @overload
    def Join(
        cls,
        outer: ParallelQuery[TOuter],
        inner: IEnumerable[TInner],
        outerKeySelector: Func[TOuter, TKey],
        innerKeySelector: Func[TInner, TKey],
        resultSelector: Func[TOuter, TInner, TResult],
    ) -> ParallelQuery[TResult]:
        """

        :param outer:
        :param inner:
        :param outerKeySelector:
        :param innerKeySelector:
        :param resultSelector:
        :return:
        """
    @classmethod
    @overload
    def Join(
        cls,
        outer: ParallelQuery[TOuter],
        inner: ParallelQuery[TInner],
        outerKeySelector: Func[TOuter, TKey],
        innerKeySelector: Func[TInner, TKey],
        resultSelector: Func[TOuter, TInner, TResult],
    ) -> ParallelQuery[TResult]:
        """

        :param outer:
        :param inner:
        :param outerKeySelector:
        :param innerKeySelector:
        :param resultSelector:
        :return:
        """
    @classmethod
    @overload
    def Join(
        cls,
        outer: ParallelQuery[TOuter],
        inner: IEnumerable[TInner],
        outerKeySelector: Func[TOuter, TKey],
        innerKeySelector: Func[TInner, TKey],
        resultSelector: Func[TOuter, TInner, TResult],
        comparer: IEqualityComparer[TKey],
    ) -> ParallelQuery[TResult]:
        """

        :param outer:
        :param inner:
        :param outerKeySelector:
        :param innerKeySelector:
        :param resultSelector:
        :param comparer:
        :return:
        """
    @classmethod
    @overload
    def Join(
        cls,
        outer: ParallelQuery[TOuter],
        inner: ParallelQuery[TInner],
        outerKeySelector: Func[TOuter, TKey],
        innerKeySelector: Func[TInner, TKey],
        resultSelector: Func[TOuter, TInner, TResult],
        comparer: IEqualityComparer[TKey],
    ) -> ParallelQuery[TResult]:
        """

        :param outer:
        :param inner:
        :param outerKeySelector:
        :param innerKeySelector:
        :param resultSelector:
        :param comparer:
        :return:
        """
    @classmethod
    @overload
    def Last(cls, source: ParallelQuery[TSource]) -> TSource:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Last(cls, source: ParallelQuery[TSource], predicate: Func[TSource, bool]) -> TSource:
        """

        :param source:
        :param predicate:
        :return:
        """
    @classmethod
    @overload
    def LastOrDefault(cls, source: ParallelQuery[TSource]) -> TSource:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def LastOrDefault(
        cls, source: ParallelQuery[TSource], predicate: Func[TSource, bool]
    ) -> TSource:
        """

        :param source:
        :param predicate:
        :return:
        """
    @classmethod
    @overload
    def LongCount(cls, source: ParallelQuery[TSource]) -> int:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def LongCount(cls, source: ParallelQuery[TSource], predicate: Func[TSource, bool]) -> int:
        """

        :param source:
        :param predicate:
        :return:
        """
    @classmethod
    @overload
    def Max(cls, source: ParallelQuery[TSource]) -> TSource:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Max(cls, source: ParallelQuery[Optional[Decimal]]) -> Optional[Decimal]:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Max(cls, source: ParallelQuery[Decimal]) -> Decimal:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Max(cls, source: ParallelQuery[Optional[float]]) -> Optional[float]:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Max(cls, source: ParallelQuery[float]) -> float:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Max(cls, source: ParallelQuery[Optional[int]]) -> Optional[int]:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Max(cls, source: ParallelQuery[int]) -> int:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Max(cls, source: ParallelQuery[Optional[int]]) -> Optional[int]:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Max(cls, source: ParallelQuery[int]) -> int:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Max(cls, source: ParallelQuery[Optional[float]]) -> Optional[float]:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Max(cls, source: ParallelQuery[float]) -> float:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Max(cls, source: ParallelQuery[TSource], selector: Func[TSource, TResult]) -> TResult:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    @overload
    def Max(
        cls, source: ParallelQuery[TSource], selector: Func[TSource, Optional[Decimal]]
    ) -> Optional[Decimal]:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    @overload
    def Max(cls, source: ParallelQuery[TSource], selector: Func[TSource, Decimal]) -> Decimal:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    @overload
    def Max(
        cls, source: ParallelQuery[TSource], selector: Func[TSource, Optional[float]]
    ) -> Optional[float]:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    @overload
    def Max(cls, source: ParallelQuery[TSource], selector: Func[TSource, float]) -> float:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    @overload
    def Max(
        cls, source: ParallelQuery[TSource], selector: Func[TSource, Optional[int]]
    ) -> Optional[int]:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    @overload
    def Max(cls, source: ParallelQuery[TSource], selector: Func[TSource, int]) -> int:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    @overload
    def Max(
        cls, source: ParallelQuery[TSource], selector: Func[TSource, Optional[int]]
    ) -> Optional[int]:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    @overload
    def Max(cls, source: ParallelQuery[TSource], selector: Func[TSource, int]) -> int:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    @overload
    def Max(
        cls, source: ParallelQuery[TSource], selector: Func[TSource, Optional[float]]
    ) -> Optional[float]:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    @overload
    def Max(cls, source: ParallelQuery[TSource], selector: Func[TSource, float]) -> float:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    @overload
    def Min(cls, source: ParallelQuery[TSource]) -> TSource:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Min(cls, source: ParallelQuery[Optional[Decimal]]) -> Optional[Decimal]:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Min(cls, source: ParallelQuery[Decimal]) -> Decimal:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Min(cls, source: ParallelQuery[Optional[float]]) -> Optional[float]:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Min(cls, source: ParallelQuery[float]) -> float:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Min(cls, source: ParallelQuery[Optional[int]]) -> Optional[int]:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Min(cls, source: ParallelQuery[int]) -> int:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Min(cls, source: ParallelQuery[Optional[int]]) -> Optional[int]:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Min(cls, source: ParallelQuery[int]) -> int:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Min(cls, source: ParallelQuery[Optional[float]]) -> Optional[float]:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Min(cls, source: ParallelQuery[float]) -> float:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Min(cls, source: ParallelQuery[TSource], selector: Func[TSource, TResult]) -> TResult:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    @overload
    def Min(
        cls, source: ParallelQuery[TSource], selector: Func[TSource, Optional[Decimal]]
    ) -> Optional[Decimal]:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    @overload
    def Min(cls, source: ParallelQuery[TSource], selector: Func[TSource, Decimal]) -> Decimal:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    @overload
    def Min(
        cls, source: ParallelQuery[TSource], selector: Func[TSource, Optional[float]]
    ) -> Optional[float]:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    @overload
    def Min(cls, source: ParallelQuery[TSource], selector: Func[TSource, float]) -> float:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    @overload
    def Min(
        cls, source: ParallelQuery[TSource], selector: Func[TSource, Optional[int]]
    ) -> Optional[int]:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    @overload
    def Min(cls, source: ParallelQuery[TSource], selector: Func[TSource, int]) -> int:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    @overload
    def Min(
        cls, source: ParallelQuery[TSource], selector: Func[TSource, Optional[int]]
    ) -> Optional[int]:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    @overload
    def Min(cls, source: ParallelQuery[TSource], selector: Func[TSource, int]) -> int:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    @overload
    def Min(
        cls, source: ParallelQuery[TSource], selector: Func[TSource, Optional[float]]
    ) -> Optional[float]:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    @overload
    def Min(cls, source: ParallelQuery[TSource], selector: Func[TSource, float]) -> float:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    def OfType(cls, source: ParallelQuery) -> ParallelQuery[TResult]:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def OrderBy(
        cls, source: ParallelQuery[TSource], keySelector: Func[TSource, TKey]
    ) -> OrderedParallelQuery[TSource]:
        """

        :param source:
        :param keySelector:
        :return:
        """
    @classmethod
    @overload
    def OrderBy(
        cls,
        source: ParallelQuery[TSource],
        keySelector: Func[TSource, TKey],
        comparer: IComparer[TKey],
    ) -> OrderedParallelQuery[TSource]:
        """

        :param source:
        :param keySelector:
        :param comparer:
        :return:
        """
    @classmethod
    @overload
    def OrderByDescending(
        cls, source: ParallelQuery[TSource], keySelector: Func[TSource, TKey]
    ) -> OrderedParallelQuery[TSource]:
        """

        :param source:
        :param keySelector:
        :return:
        """
    @classmethod
    @overload
    def OrderByDescending(
        cls,
        source: ParallelQuery[TSource],
        keySelector: Func[TSource, TKey],
        comparer: IComparer[TKey],
    ) -> OrderedParallelQuery[TSource]:
        """

        :param source:
        :param keySelector:
        :param comparer:
        :return:
        """
    @classmethod
    def Range(cls, start: int, count: int) -> ParallelQuery[int]:
        """

        :param start:
        :param count:
        :return:
        """
    @classmethod
    def Repeat(cls, element: TResult, count: int) -> ParallelQuery[TResult]:
        """

        :param element:
        :param count:
        :return:
        """
    @classmethod
    def Reverse(cls, source: ParallelQuery[TSource]) -> ParallelQuery[TSource]:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Select(
        cls, source: ParallelQuery[TSource], selector: Func[TSource, TResult]
    ) -> ParallelQuery[TResult]:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    @overload
    def Select(
        cls, source: ParallelQuery[TSource], selector: Func[TSource, int, TResult]
    ) -> ParallelQuery[TResult]:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    @overload
    def SelectMany(
        cls, source: ParallelQuery[TSource], selector: Func[TSource, IEnumerable[TResult]]
    ) -> ParallelQuery[TResult]:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    @overload
    def SelectMany(
        cls, source: ParallelQuery[TSource], selector: Func[TSource, int, IEnumerable[TResult]]
    ) -> ParallelQuery[TResult]:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    @overload
    def SelectMany(
        cls,
        source: ParallelQuery[TSource],
        collectionSelector: Func[TSource, IEnumerable[TCollection]],
        resultSelector: Func[TSource, TCollection, TResult],
    ) -> ParallelQuery[TResult]:
        """

        :param source:
        :param collectionSelector:
        :param resultSelector:
        :return:
        """
    @classmethod
    @overload
    def SelectMany(
        cls,
        source: ParallelQuery[TSource],
        collectionSelector: Func[TSource, int, IEnumerable[TCollection]],
        resultSelector: Func[TSource, TCollection, TResult],
    ) -> ParallelQuery[TResult]:
        """

        :param source:
        :param collectionSelector:
        :param resultSelector:
        :return:
        """
    @classmethod
    @overload
    def SequenceEqual(cls, first: ParallelQuery[TSource], second: IEnumerable[TSource]) -> bool:
        """

        :param first:
        :param second:
        :return:
        """
    @classmethod
    @overload
    def SequenceEqual(cls, first: ParallelQuery[TSource], second: ParallelQuery[TSource]) -> bool:
        """

        :param first:
        :param second:
        :return:
        """
    @classmethod
    @overload
    def SequenceEqual(
        cls,
        first: ParallelQuery[TSource],
        second: IEnumerable[TSource],
        comparer: IEqualityComparer[TSource],
    ) -> bool:
        """

        :param first:
        :param second:
        :param comparer:
        :return:
        """
    @classmethod
    @overload
    def SequenceEqual(
        cls,
        first: ParallelQuery[TSource],
        second: ParallelQuery[TSource],
        comparer: IEqualityComparer[TSource],
    ) -> bool:
        """

        :param first:
        :param second:
        :param comparer:
        :return:
        """
    @classmethod
    @overload
    def Single(cls, source: ParallelQuery[TSource]) -> TSource:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Single(cls, source: ParallelQuery[TSource], predicate: Func[TSource, bool]) -> TSource:
        """

        :param source:
        :param predicate:
        :return:
        """
    @classmethod
    @overload
    def SingleOrDefault(cls, source: ParallelQuery[TSource]) -> TSource:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def SingleOrDefault(
        cls, source: ParallelQuery[TSource], predicate: Func[TSource, bool]
    ) -> TSource:
        """

        :param source:
        :param predicate:
        :return:
        """
    @classmethod
    def Skip(cls, source: ParallelQuery[TSource], count: int) -> ParallelQuery[TSource]:
        """

        :param source:
        :param count:
        :return:
        """
    @classmethod
    @overload
    def SkipWhile(
        cls, source: ParallelQuery[TSource], predicate: Func[TSource, bool]
    ) -> ParallelQuery[TSource]:
        """

        :param source:
        :param predicate:
        :return:
        """
    @classmethod
    @overload
    def SkipWhile(
        cls, source: ParallelQuery[TSource], predicate: Func[TSource, int, bool]
    ) -> ParallelQuery[TSource]:
        """

        :param source:
        :param predicate:
        :return:
        """
    @classmethod
    @overload
    def Sum(cls, source: ParallelQuery[Optional[Decimal]]) -> Optional[Decimal]:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Sum(cls, source: ParallelQuery[Decimal]) -> Decimal:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Sum(cls, source: ParallelQuery[Optional[float]]) -> Optional[float]:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Sum(cls, source: ParallelQuery[float]) -> float:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Sum(cls, source: ParallelQuery[Optional[int]]) -> Optional[int]:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Sum(cls, source: ParallelQuery[int]) -> int:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Sum(cls, source: ParallelQuery[Optional[int]]) -> Optional[int]:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Sum(cls, source: ParallelQuery[int]) -> int:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Sum(cls, source: ParallelQuery[Optional[float]]) -> Optional[float]:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Sum(cls, source: ParallelQuery[float]) -> float:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Sum(
        cls, source: ParallelQuery[TSource], selector: Func[TSource, Optional[Decimal]]
    ) -> Optional[Decimal]:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    @overload
    def Sum(cls, source: ParallelQuery[TSource], selector: Func[TSource, Decimal]) -> Decimal:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    @overload
    def Sum(
        cls, source: ParallelQuery[TSource], selector: Func[TSource, Optional[float]]
    ) -> Optional[float]:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    @overload
    def Sum(cls, source: ParallelQuery[TSource], selector: Func[TSource, float]) -> float:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    @overload
    def Sum(
        cls, source: ParallelQuery[TSource], selector: Func[TSource, Optional[int]]
    ) -> Optional[int]:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    @overload
    def Sum(cls, source: ParallelQuery[TSource], selector: Func[TSource, int]) -> int:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    @overload
    def Sum(
        cls, source: ParallelQuery[TSource], selector: Func[TSource, Optional[int]]
    ) -> Optional[int]:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    @overload
    def Sum(cls, source: ParallelQuery[TSource], selector: Func[TSource, int]) -> int:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    @overload
    def Sum(
        cls, source: ParallelQuery[TSource], selector: Func[TSource, Optional[float]]
    ) -> Optional[float]:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    @overload
    def Sum(cls, source: ParallelQuery[TSource], selector: Func[TSource, float]) -> float:
        """

        :param source:
        :param selector:
        :return:
        """
    @classmethod
    def Take(cls, source: ParallelQuery[TSource], count: int) -> ParallelQuery[TSource]:
        """

        :param source:
        :param count:
        :return:
        """
    @classmethod
    @overload
    def TakeWhile(
        cls, source: ParallelQuery[TSource], predicate: Func[TSource, bool]
    ) -> ParallelQuery[TSource]:
        """

        :param source:
        :param predicate:
        :return:
        """
    @classmethod
    @overload
    def TakeWhile(
        cls, source: ParallelQuery[TSource], predicate: Func[TSource, int, bool]
    ) -> ParallelQuery[TSource]:
        """

        :param source:
        :param predicate:
        :return:
        """
    @classmethod
    @overload
    def ThenBy(
        cls, source: OrderedParallelQuery[TSource], keySelector: Func[TSource, TKey]
    ) -> OrderedParallelQuery[TSource]:
        """

        :param source:
        :param keySelector:
        :return:
        """
    @classmethod
    @overload
    def ThenBy(
        cls,
        source: OrderedParallelQuery[TSource],
        keySelector: Func[TSource, TKey],
        comparer: IComparer[TKey],
    ) -> OrderedParallelQuery[TSource]:
        """

        :param source:
        :param keySelector:
        :param comparer:
        :return:
        """
    @classmethod
    @overload
    def ThenByDescending(
        cls, source: OrderedParallelQuery[TSource], keySelector: Func[TSource, TKey]
    ) -> OrderedParallelQuery[TSource]:
        """

        :param source:
        :param keySelector:
        :return:
        """
    @classmethod
    @overload
    def ThenByDescending(
        cls,
        source: OrderedParallelQuery[TSource],
        keySelector: Func[TSource, TKey],
        comparer: IComparer[TKey],
    ) -> OrderedParallelQuery[TSource]:
        """

        :param source:
        :param keySelector:
        :param comparer:
        :return:
        """
    @classmethod
    def ToArray(cls, source: ParallelQuery[TSource]) -> Array[TSource]:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def ToDictionary(
        cls, source: ParallelQuery[TSource], keySelector: Func[TSource, TKey]
    ) -> Dictionary[TKey, TSource]:
        """

        :param source:
        :param keySelector:
        :return:
        """
    @classmethod
    @overload
    def ToDictionary(
        cls,
        source: ParallelQuery[TSource],
        keySelector: Func[TSource, TKey],
        comparer: IEqualityComparer[TKey],
    ) -> Dictionary[TKey, TSource]:
        """

        :param source:
        :param keySelector:
        :param comparer:
        :return:
        """
    @classmethod
    @overload
    def ToDictionary(
        cls,
        source: ParallelQuery[TSource],
        keySelector: Func[TSource, TKey],
        elementSelector: Func[TSource, TElement],
    ) -> Dictionary[TKey, TElement]:
        """

        :param source:
        :param keySelector:
        :param elementSelector:
        :return:
        """
    @classmethod
    @overload
    def ToDictionary(
        cls,
        source: ParallelQuery[TSource],
        keySelector: Func[TSource, TKey],
        elementSelector: Func[TSource, TElement],
        comparer: IEqualityComparer[TKey],
    ) -> Dictionary[TKey, TElement]:
        """

        :param source:
        :param keySelector:
        :param elementSelector:
        :param comparer:
        :return:
        """
    @classmethod
    def ToList(cls, source: ParallelQuery[TSource]) -> List[TSource]:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def ToLookup(
        cls, source: ParallelQuery[TSource], keySelector: Func[TSource, TKey]
    ) -> ILookup[TKey, TSource]:
        """

        :param source:
        :param keySelector:
        :return:
        """
    @classmethod
    @overload
    def ToLookup(
        cls,
        source: ParallelQuery[TSource],
        keySelector: Func[TSource, TKey],
        comparer: IEqualityComparer[TKey],
    ) -> ILookup[TKey, TSource]:
        """

        :param source:
        :param keySelector:
        :param comparer:
        :return:
        """
    @classmethod
    @overload
    def ToLookup(
        cls,
        source: ParallelQuery[TSource],
        keySelector: Func[TSource, TKey],
        elementSelector: Func[TSource, TElement],
    ) -> ILookup[TKey, TElement]:
        """

        :param source:
        :param keySelector:
        :param elementSelector:
        :return:
        """
    @classmethod
    @overload
    def ToLookup(
        cls,
        source: ParallelQuery[TSource],
        keySelector: Func[TSource, TKey],
        elementSelector: Func[TSource, TElement],
        comparer: IEqualityComparer[TKey],
    ) -> ILookup[TKey, TElement]:
        """

        :param source:
        :param keySelector:
        :param elementSelector:
        :param comparer:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @classmethod
    @overload
    def Union(
        cls, first: ParallelQuery[TSource], second: IEnumerable[TSource]
    ) -> ParallelQuery[TSource]:
        """

        :param first:
        :param second:
        :return:
        """
    @classmethod
    @overload
    def Union(
        cls, first: ParallelQuery[TSource], second: ParallelQuery[TSource]
    ) -> ParallelQuery[TSource]:
        """

        :param first:
        :param second:
        :return:
        """
    @classmethod
    @overload
    def Union(
        cls,
        first: ParallelQuery[TSource],
        second: IEnumerable[TSource],
        comparer: IEqualityComparer[TSource],
    ) -> ParallelQuery[TSource]:
        """

        :param first:
        :param second:
        :param comparer:
        :return:
        """
    @classmethod
    @overload
    def Union(
        cls,
        first: ParallelQuery[TSource],
        second: ParallelQuery[TSource],
        comparer: IEqualityComparer[TSource],
    ) -> ParallelQuery[TSource]:
        """

        :param first:
        :param second:
        :param comparer:
        :return:
        """
    @classmethod
    @overload
    def Where(
        cls, source: ParallelQuery[TSource], predicate: Func[TSource, bool]
    ) -> ParallelQuery[TSource]:
        """

        :param source:
        :param predicate:
        :return:
        """
    @classmethod
    @overload
    def Where(
        cls, source: ParallelQuery[TSource], predicate: Func[TSource, int, bool]
    ) -> ParallelQuery[TSource]:
        """

        :param source:
        :param predicate:
        :return:
        """
    @classmethod
    def WithCancellation(
        cls, source: ParallelQuery[TSource], cancellationToken: CancellationToken
    ) -> ParallelQuery[TSource]:
        """

        :param source:
        :param cancellationToken:
        :return:
        """
    @classmethod
    def WithDegreeOfParallelism(
        cls, source: ParallelQuery[TSource], degreeOfParallelism: int
    ) -> ParallelQuery[TSource]:
        """

        :param source:
        :param degreeOfParallelism:
        :return:
        """
    @classmethod
    def WithExecutionMode(
        cls, source: ParallelQuery[TSource], executionMode: ParallelExecutionMode
    ) -> ParallelQuery[TSource]:
        """

        :param source:
        :param executionMode:
        :return:
        """
    @classmethod
    def WithMergeOptions(
        cls, source: ParallelQuery[TSource], mergeOptions: ParallelMergeOptions
    ) -> ParallelQuery[TSource]:
        """

        :param source:
        :param mergeOptions:
        :return:
        """
    @classmethod
    @overload
    def Zip(
        cls,
        first: ParallelQuery[TFirst],
        second: IEnumerable[TSecond],
        resultSelector: Func[TFirst, TSecond, TResult],
    ) -> ParallelQuery[TResult]:
        """

        :param first:
        :param second:
        :param resultSelector:
        :return:
        """
    @classmethod
    @overload
    def Zip(
        cls,
        first: ParallelQuery[TFirst],
        second: ParallelQuery[TSecond],
        resultSelector: Func[TFirst, TSecond, TResult],
    ) -> ParallelQuery[TResult]:
        """

        :param first:
        :param second:
        :param resultSelector:
        :return:
        """

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
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """

class ParallelQuery(Generic[TSource], ParallelQuery, IEnumerable[TSource], IEnumerable):
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
    def __iter__(self) -> Iterator[TSource]:
        """

        :return:
        """

class Queryable(ABC, Object):
    """"""

    @classmethod
    @overload
    def Aggregate(
        cls, source: IQueryable[TSource], func: Expression[Func, TSource, TSource]
    ) -> TSource:
        """"""
    @classmethod
    @overload
    def Aggregate(
        cls,
        source: IQueryable[TSource],
        seed: TAccumulate,
        func: Expression[Func, TSource, TAccumulate],
    ) -> TAccumulate:
        """"""
    @classmethod
    @overload
    def Aggregate(
        cls,
        source: IQueryable[TSource],
        seed: TAccumulate,
        func: Expression[Func, TSource, TAccumulate],
        selector: Expression[Func, TResult],
    ) -> TResult:
        """"""
    @classmethod
    def All(cls, source: IQueryable[TSource], predicate: Expression[Func, bool]) -> bool:
        """"""
    @classmethod
    @overload
    def Any(cls, source: IQueryable[TSource]) -> bool:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Any(cls, source: IQueryable[TSource], predicate: Expression[Func, bool]) -> bool:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def AsQueryable(cls, source: IEnumerable[TElement]) -> IQueryable[TElement]:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def AsQueryable(cls, source: IEnumerable) -> IQueryable:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Average(cls, source: IQueryable[Optional[Decimal]]) -> Optional[Decimal]:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Average(cls, source: IQueryable[Decimal]) -> Decimal:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Average(cls, source: IQueryable[Optional[float]]) -> Optional[float]:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Average(cls, source: IQueryable[float]) -> float:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Average(cls, source: IQueryable[Optional[int]]) -> Optional[float]:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Average(cls, source: IQueryable[int]) -> float:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Average(cls, source: IQueryable[Optional[int]]) -> Optional[float]:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Average(cls, source: IQueryable[int]) -> float:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Average(cls, source: IQueryable[Optional[float]]) -> Optional[float]:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Average(cls, source: IQueryable[float]) -> float:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Average(
        cls, source: IQueryable[TSource], selector: Expression[Func, Optional[Decimal]]
    ) -> Optional[Decimal]:
        """"""
    @classmethod
    @overload
    def Average(cls, source: IQueryable[TSource], selector: Expression[Func, Decimal]) -> Decimal:
        """"""
    @classmethod
    @overload
    def Average(
        cls, source: IQueryable[TSource], selector: Expression[Func, Optional[float]]
    ) -> Optional[float]:
        """"""
    @classmethod
    @overload
    def Average(cls, source: IQueryable[TSource], selector: Expression[Func, float]) -> float:
        """"""
    @classmethod
    @overload
    def Average(
        cls, source: IQueryable[TSource], selector: Expression[Func, Optional[int]]
    ) -> Optional[float]:
        """"""
    @classmethod
    @overload
    def Average(cls, source: IQueryable[TSource], selector: Expression[Func, int]) -> float:
        """"""
    @classmethod
    @overload
    def Average(
        cls, source: IQueryable[TSource], selector: Expression[Func, Optional[int]]
    ) -> Optional[float]:
        """"""
    @classmethod
    @overload
    def Average(cls, source: IQueryable[TSource], selector: Expression[Func, int]) -> float:
        """"""
    @classmethod
    @overload
    def Average(
        cls, source: IQueryable[TSource], selector: Expression[Func, Optional[float]]
    ) -> Optional[float]:
        """"""
    @classmethod
    @overload
    def Average(cls, source: IQueryable[TSource], selector: Expression[Func, float]) -> float:
        """"""
    @classmethod
    def Cast(cls, source: IQueryable) -> IQueryable[TResult]:
        """

        :param source:
        :return:
        """
    @classmethod
    def Concat(
        cls, source1: IQueryable[TSource], source2: IEnumerable[TSource]
    ) -> IQueryable[TSource]:
        """

        :param source1:
        :param source2:
        :return:
        """
    @classmethod
    @overload
    def Contains(cls, source: IQueryable[TSource], item: TSource) -> bool:
        """

        :param source:
        :param item:
        :return:
        """
    @classmethod
    @overload
    def Contains(
        cls, source: IQueryable[TSource], item: TSource, comparer: IEqualityComparer[TSource]
    ) -> bool:
        """

        :param source:
        :param item:
        :param comparer:
        :return:
        """
    @classmethod
    @overload
    def Count(cls, source: IQueryable[TSource]) -> int:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Count(cls, source: IQueryable[TSource], predicate: Expression[Func, bool]) -> int:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def DefaultIfEmpty(cls, source: IQueryable[TSource]) -> IQueryable[TSource]:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def DefaultIfEmpty(
        cls, source: IQueryable[TSource], defaultValue: TSource
    ) -> IQueryable[TSource]:
        """

        :param source:
        :param defaultValue:
        :return:
        """
    @classmethod
    @overload
    def Distinct(cls, source: IQueryable[TSource]) -> IQueryable[TSource]:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Distinct(
        cls, source: IQueryable[TSource], comparer: IEqualityComparer[TSource]
    ) -> IQueryable[TSource]:
        """

        :param source:
        :param comparer:
        :return:
        """
    @classmethod
    def ElementAt(cls, source: IQueryable[TSource], index: int) -> TSource:
        """

        :param source:
        :param index:
        :return:
        """
    @classmethod
    def ElementAtOrDefault(cls, source: IQueryable[TSource], index: int) -> TSource:
        """

        :param source:
        :param index:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @classmethod
    @overload
    def Except(
        cls, source1: IQueryable[TSource], source2: IEnumerable[TSource]
    ) -> IQueryable[TSource]:
        """

        :param source1:
        :param source2:
        :return:
        """
    @classmethod
    @overload
    def Except(
        cls,
        source1: IQueryable[TSource],
        source2: IEnumerable[TSource],
        comparer: IEqualityComparer[TSource],
    ) -> IQueryable[TSource]:
        """

        :param source1:
        :param source2:
        :param comparer:
        :return:
        """
    @classmethod
    @overload
    def First(cls, source: IQueryable[TSource]) -> TSource:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def First(cls, source: IQueryable[TSource], predicate: Expression[Func, bool]) -> TSource:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def FirstOrDefault(cls, source: IQueryable[TSource]) -> TSource:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def FirstOrDefault(
        cls, source: IQueryable[TSource], predicate: Expression[Func, bool]
    ) -> TSource:
        """

        :param source:
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
    @overload
    def GroupBy(
        cls, source: IQueryable[TSource], keySelector: Expression[Func, TKey]
    ) -> IQueryable[IGrouping, TSource]:
        """"""
    @classmethod
    @overload
    def GroupBy(
        cls,
        source: IQueryable[TSource],
        keySelector: Expression[Func, TKey],
        comparer: IEqualityComparer[TKey],
    ) -> IQueryable[IGrouping, TSource]:
        """"""
    @classmethod
    @overload
    def GroupBy(
        cls,
        source: IQueryable[TSource],
        keySelector: Expression[Func, TKey],
        resultSelector: Expression[Func, IEnumerable[TSource], TResult],
    ) -> IQueryable[TResult]:
        """"""
    @classmethod
    @overload
    def GroupBy(
        cls,
        source: IQueryable[TSource],
        keySelector: Expression[Func, TKey],
        elementSelector: Expression[Func, TElement],
    ) -> IQueryable[IGrouping, TElement]:
        """"""
    @classmethod
    @overload
    def GroupBy(
        cls,
        source: IQueryable[TSource],
        keySelector: Expression[Func, TKey],
        resultSelector: Expression[Func, IEnumerable[TSource], TResult],
        comparer: IEqualityComparer[TKey],
    ) -> IQueryable[TResult]:
        """"""
    @classmethod
    @overload
    def GroupBy(
        cls,
        source: IQueryable[TSource],
        keySelector: Expression[Func, TKey],
        elementSelector: Expression[Func, TElement],
        comparer: IEqualityComparer[TKey],
    ) -> IQueryable[IGrouping, TElement]:
        """"""
    @classmethod
    @overload
    def GroupBy(
        cls,
        source: IQueryable[TSource],
        keySelector: Expression[Func, TKey],
        elementSelector: Expression[Func, TElement],
        resultSelector: Expression[Func, IEnumerable[TElement], TResult],
    ) -> IQueryable[TResult]:
        """"""
    @classmethod
    @overload
    def GroupBy(
        cls,
        source: IQueryable[TSource],
        keySelector: Expression[Func, TKey],
        elementSelector: Expression[Func, TElement],
        resultSelector: Expression[Func, IEnumerable[TElement], TResult],
        comparer: IEqualityComparer[TKey],
    ) -> IQueryable[TResult]:
        """"""
    @classmethod
    @overload
    def GroupJoin(
        cls,
        outer: IQueryable[TOuter],
        inner: IEnumerable[TInner],
        outerKeySelector: Expression[Func, TKey],
        innerKeySelector: Expression[Func, TKey],
        resultSelector: Expression[Func, IEnumerable[TInner], TResult],
    ) -> IQueryable[TResult]:
        """"""
    @classmethod
    @overload
    def GroupJoin(
        cls,
        outer: IQueryable[TOuter],
        inner: IEnumerable[TInner],
        outerKeySelector: Expression[Func, TKey],
        innerKeySelector: Expression[Func, TKey],
        resultSelector: Expression[Func, IEnumerable[TInner], TResult],
        comparer: IEqualityComparer[TKey],
    ) -> IQueryable[TResult]:
        """"""
    @classmethod
    @overload
    def Intersect(
        cls, source1: IQueryable[TSource], source2: IEnumerable[TSource]
    ) -> IQueryable[TSource]:
        """

        :param source1:
        :param source2:
        :return:
        """
    @classmethod
    @overload
    def Intersect(
        cls,
        source1: IQueryable[TSource],
        source2: IEnumerable[TSource],
        comparer: IEqualityComparer[TSource],
    ) -> IQueryable[TSource]:
        """

        :param source1:
        :param source2:
        :param comparer:
        :return:
        """
    @classmethod
    @overload
    def Join(
        cls,
        outer: IQueryable[TOuter],
        inner: IEnumerable[TInner],
        outerKeySelector: Expression[Func, TKey],
        innerKeySelector: Expression[Func, TKey],
        resultSelector: Expression[Func, TInner, TResult],
    ) -> IQueryable[TResult]:
        """"""
    @classmethod
    @overload
    def Join(
        cls,
        outer: IQueryable[TOuter],
        inner: IEnumerable[TInner],
        outerKeySelector: Expression[Func, TKey],
        innerKeySelector: Expression[Func, TKey],
        resultSelector: Expression[Func, TInner, TResult],
        comparer: IEqualityComparer[TKey],
    ) -> IQueryable[TResult]:
        """"""
    @classmethod
    @overload
    def Last(cls, source: IQueryable[TSource]) -> TSource:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Last(cls, source: IQueryable[TSource], predicate: Expression[Func, bool]) -> TSource:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def LastOrDefault(cls, source: IQueryable[TSource]) -> TSource:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def LastOrDefault(
        cls, source: IQueryable[TSource], predicate: Expression[Func, bool]
    ) -> TSource:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def LongCount(cls, source: IQueryable[TSource]) -> int:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def LongCount(cls, source: IQueryable[TSource], predicate: Expression[Func, bool]) -> int:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Max(cls, source: IQueryable[TSource]) -> TSource:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Max(cls, source: IQueryable[TSource], selector: Expression[Func, TResult]) -> TResult:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Min(cls, source: IQueryable[TSource]) -> TSource:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Min(cls, source: IQueryable[TSource], selector: Expression[Func, TResult]) -> TResult:
        """

        :param source:
        :return:
        """
    @classmethod
    def OfType(cls, source: IQueryable) -> IQueryable[TResult]:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def OrderBy(
        cls, source: IQueryable[TSource], keySelector: Expression[Func, TKey]
    ) -> IOrderedQueryable[TSource]:
        """"""
    @classmethod
    @overload
    def OrderBy(
        cls,
        source: IQueryable[TSource],
        keySelector: Expression[Func, TKey],
        comparer: IComparer[TKey],
    ) -> IOrderedQueryable[TSource]:
        """"""
    @classmethod
    @overload
    def OrderByDescending(
        cls, source: IQueryable[TSource], keySelector: Expression[Func, TKey]
    ) -> IOrderedQueryable[TSource]:
        """"""
    @classmethod
    @overload
    def OrderByDescending(
        cls,
        source: IQueryable[TSource],
        keySelector: Expression[Func, TKey],
        comparer: IComparer[TKey],
    ) -> IOrderedQueryable[TSource]:
        """"""
    @classmethod
    def Reverse(cls, source: IQueryable[TSource]) -> IQueryable[TSource]:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Select(
        cls, source: IQueryable[TSource], selector: Expression[Func, TResult]
    ) -> IQueryable[TResult]:
        """"""
    @classmethod
    @overload
    def Select(
        cls, source: IQueryable[TSource], selector: Expression[Func, int, TResult]
    ) -> IQueryable[TResult]:
        """"""
    @classmethod
    @overload
    def SelectMany(
        cls, source: IQueryable[TSource], selector: Expression[Func, IEnumerable[TResult]]
    ) -> IQueryable[TResult]:
        """"""
    @classmethod
    @overload
    def SelectMany(
        cls, source: IQueryable[TSource], selector: Expression[Func, int, IEnumerable[TResult]]
    ) -> IQueryable[TResult]:
        """"""
    @classmethod
    @overload
    def SelectMany(
        cls,
        source: IQueryable[TSource],
        collectionSelector: Expression[Func, IEnumerable[TCollection]],
        resultSelector: Expression[Func, TCollection, TResult],
    ) -> IQueryable[TResult]:
        """"""
    @classmethod
    @overload
    def SelectMany(
        cls,
        source: IQueryable[TSource],
        collectionSelector: Expression[Func, int, IEnumerable[TCollection]],
        resultSelector: Expression[Func, TCollection, TResult],
    ) -> IQueryable[TResult]:
        """"""
    @classmethod
    @overload
    def SequenceEqual(cls, source1: IQueryable[TSource], source2: IEnumerable[TSource]) -> bool:
        """

        :param source1:
        :param source2:
        :return:
        """
    @classmethod
    @overload
    def SequenceEqual(
        cls,
        source1: IQueryable[TSource],
        source2: IEnumerable[TSource],
        comparer: IEqualityComparer[TSource],
    ) -> bool:
        """

        :param source1:
        :param source2:
        :param comparer:
        :return:
        """
    @classmethod
    @overload
    def Single(cls, source: IQueryable[TSource]) -> TSource:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Single(cls, source: IQueryable[TSource], predicate: Expression[Func, bool]) -> TSource:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def SingleOrDefault(cls, source: IQueryable[TSource]) -> TSource:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def SingleOrDefault(
        cls, source: IQueryable[TSource], predicate: Expression[Func, bool]
    ) -> TSource:
        """

        :param source:
        :return:
        """
    @classmethod
    def Skip(cls, source: IQueryable[TSource], count: int) -> IQueryable[TSource]:
        """

        :param source:
        :param count:
        :return:
        """
    @classmethod
    @overload
    def SkipWhile(
        cls, source: IQueryable[TSource], predicate: Expression[Func, bool]
    ) -> IQueryable[TSource]:
        """"""
    @classmethod
    @overload
    def SkipWhile(
        cls, source: IQueryable[TSource], predicate: Expression[Func, int, bool]
    ) -> IQueryable[TSource]:
        """"""
    @classmethod
    @overload
    def Sum(cls, source: IQueryable[Optional[Decimal]]) -> Optional[Decimal]:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Sum(cls, source: IQueryable[Decimal]) -> Decimal:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Sum(cls, source: IQueryable[Optional[float]]) -> Optional[float]:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Sum(cls, source: IQueryable[float]) -> float:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Sum(cls, source: IQueryable[Optional[int]]) -> Optional[int]:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Sum(cls, source: IQueryable[int]) -> int:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Sum(cls, source: IQueryable[Optional[int]]) -> Optional[int]:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Sum(cls, source: IQueryable[int]) -> int:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Sum(cls, source: IQueryable[Optional[float]]) -> Optional[float]:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Sum(cls, source: IQueryable[float]) -> float:
        """

        :param source:
        :return:
        """
    @classmethod
    @overload
    def Sum(
        cls, source: IQueryable[TSource], selector: Expression[Func, Optional[Decimal]]
    ) -> Optional[Decimal]:
        """"""
    @classmethod
    @overload
    def Sum(cls, source: IQueryable[TSource], selector: Expression[Func, Decimal]) -> Decimal:
        """"""
    @classmethod
    @overload
    def Sum(
        cls, source: IQueryable[TSource], selector: Expression[Func, Optional[float]]
    ) -> Optional[float]:
        """"""
    @classmethod
    @overload
    def Sum(cls, source: IQueryable[TSource], selector: Expression[Func, float]) -> float:
        """"""
    @classmethod
    @overload
    def Sum(
        cls, source: IQueryable[TSource], selector: Expression[Func, Optional[int]]
    ) -> Optional[int]:
        """"""
    @classmethod
    @overload
    def Sum(cls, source: IQueryable[TSource], selector: Expression[Func, int]) -> int:
        """"""
    @classmethod
    @overload
    def Sum(
        cls, source: IQueryable[TSource], selector: Expression[Func, Optional[int]]
    ) -> Optional[int]:
        """"""
    @classmethod
    @overload
    def Sum(cls, source: IQueryable[TSource], selector: Expression[Func, int]) -> int:
        """"""
    @classmethod
    @overload
    def Sum(
        cls, source: IQueryable[TSource], selector: Expression[Func, Optional[float]]
    ) -> Optional[float]:
        """"""
    @classmethod
    @overload
    def Sum(cls, source: IQueryable[TSource], selector: Expression[Func, float]) -> float:
        """"""
    @classmethod
    def Take(cls, source: IQueryable[TSource], count: int) -> IQueryable[TSource]:
        """

        :param source:
        :param count:
        :return:
        """
    @classmethod
    @overload
    def TakeWhile(
        cls, source: IQueryable[TSource], predicate: Expression[Func, bool]
    ) -> IQueryable[TSource]:
        """"""
    @classmethod
    @overload
    def TakeWhile(
        cls, source: IQueryable[TSource], predicate: Expression[Func, int, bool]
    ) -> IQueryable[TSource]:
        """"""
    @classmethod
    @overload
    def ThenBy(
        cls, source: IOrderedQueryable[TSource], keySelector: Expression[Func, TKey]
    ) -> IOrderedQueryable[TSource]:
        """"""
    @classmethod
    @overload
    def ThenBy(
        cls,
        source: IOrderedQueryable[TSource],
        keySelector: Expression[Func, TKey],
        comparer: IComparer[TKey],
    ) -> IOrderedQueryable[TSource]:
        """"""
    @classmethod
    @overload
    def ThenByDescending(
        cls, source: IOrderedQueryable[TSource], keySelector: Expression[Func, TKey]
    ) -> IOrderedQueryable[TSource]:
        """"""
    @classmethod
    @overload
    def ThenByDescending(
        cls,
        source: IOrderedQueryable[TSource],
        keySelector: Expression[Func, TKey],
        comparer: IComparer[TKey],
    ) -> IOrderedQueryable[TSource]:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """
    @classmethod
    @overload
    def Union(
        cls, source1: IQueryable[TSource], source2: IEnumerable[TSource]
    ) -> IQueryable[TSource]:
        """

        :param source1:
        :param source2:
        :return:
        """
    @classmethod
    @overload
    def Union(
        cls,
        source1: IQueryable[TSource],
        source2: IEnumerable[TSource],
        comparer: IEqualityComparer[TSource],
    ) -> IQueryable[TSource]:
        """

        :param source1:
        :param source2:
        :param comparer:
        :return:
        """
    @classmethod
    @overload
    def Where(
        cls, source: IQueryable[TSource], predicate: Expression[Func, bool]
    ) -> IQueryable[TSource]:
        """"""
    @classmethod
    @overload
    def Where(
        cls, source: IQueryable[TSource], predicate: Expression[Func, int, bool]
    ) -> IQueryable[TSource]:
        """"""
    @classmethod
    def Zip(
        cls,
        source1: IQueryable[TFirst],
        source2: IEnumerable[TSecond],
        resultSelector: Expression[Func, TSecond, TResult],
    ) -> IQueryable[TResult]:
        """"""

class SR(Object):
    """"""

    @classmethod
    @property
    def Resources(cls) -> ResourceManager:
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
    @classmethod
    def GetObject(cls, name: str) -> object:
        """

        :param name:
        :return:
        """
    @classmethod
    @overload
    def GetString(cls, name: str) -> str:
        """

        :param name:
        :return:
        """
    @classmethod
    @overload
    def GetString(cls, name: str, usedFallback: bool) -> Tuple[str, bool]:
        """

        :param name:
        :param usedFallback:
        :return:
        """
    @classmethod
    @overload
    def GetString(cls, name: str, args: Array[object]) -> str:
        """

        :param name:
        :param args:
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

class SRCategoryAttribute(CategoryAttribute, _Attribute):
    """"""

    def __init__(self, category: str):
        """

        :param category:
        """
    @classmethod
    @property
    def Action(cls) -> CategoryAttribute:
        """

        :return:
        """
    @classmethod
    @property
    def Appearance(cls) -> CategoryAttribute:
        """

        :return:
        """
    @classmethod
    @property
    def Asynchronous(cls) -> CategoryAttribute:
        """

        :return:
        """
    @classmethod
    @property
    def Behavior(cls) -> CategoryAttribute:
        """

        :return:
        """
    @property
    def Category(self) -> str:
        """

        :return:
        """
    @classmethod
    @property
    def Data(cls) -> CategoryAttribute:
        """

        :return:
        """
    @classmethod
    @property
    def Default(cls) -> CategoryAttribute:
        """

        :return:
        """
    @classmethod
    @property
    def Design(cls) -> CategoryAttribute:
        """

        :return:
        """
    @classmethod
    @property
    def DragDrop(cls) -> CategoryAttribute:
        """

        :return:
        """
    @classmethod
    @property
    def Focus(cls) -> CategoryAttribute:
        """

        :return:
        """
    @classmethod
    @property
    def Format(cls) -> CategoryAttribute:
        """

        :return:
        """
    @classmethod
    @property
    def Key(cls) -> CategoryAttribute:
        """

        :return:
        """
    @classmethod
    @property
    def Layout(cls) -> CategoryAttribute:
        """

        :return:
        """
    @classmethod
    @property
    def Mouse(cls) -> CategoryAttribute:
        """

        :return:
        """
    @property
    def TypeId(self) -> object:
        """

        :return:
        """
    @classmethod
    @property
    def WindowStyle(cls) -> CategoryAttribute:
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
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """

        :return:
        """
    def Match(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class SRDescriptionAttribute(DescriptionAttribute, _Attribute):
    """"""

    def __init__(self, description: str):
        """

        :param description:
        """
    @property
    def Description(self) -> str:
        """

        :return:
        """
    @property
    def TypeId(self) -> object:
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
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """

        :return:
        """
    def Match(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class Set(Generic[TElement], Object):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, comparer: IEqualityComparer[TElement]):
        """

        :param comparer:
        """
    def Add(self, value: TElement) -> bool:
        """

        :param value:
        :return:
        """
    def Contains(self, value: TElement) -> bool:
        """

        :param value:
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
    def Remove(self, value: TElement) -> bool:
        """

        :param value:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class SingleLinkedNode(Generic[TSource], Object):
    """"""

    def __init__(self, item: TSource):
        """

        :param item:
        """
    @property
    def Item(self) -> TSource:
        """

        :return:
        """
    @property
    def Linked(self) -> SingleLinkedNode[TSource]:
        """

        :return:
        """
    def Add(self, item: TSource) -> SingleLinkedNode[TSource]:
        """

        :param item:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetCount(self) -> int:
        """

        :return:
        """
    def GetEnumerator(self, count: int) -> IEnumerator[TSource]:
        """

        :param count:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetNode(self, index: int) -> SingleLinkedNode[TSource]:
        """

        :param index:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToArray(self, count: int) -> Array[TSource]:
        """

        :param count:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def __getitem__(self) -> TSource:
        """

        :return:
        """

class Strings(ABC, Object):
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

class SystemCore_EnumerableDebugView(Generic[T], Object):
    """"""

    def __init__(self, enumerable: IEnumerable[T]):
        """

        :param enumerable:
        """
    @property
    def Items(self) -> Array[T]:
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

class SystemCore_EnumerableDebugView(Object):
    """"""

    def __init__(self, enumerable: IEnumerable):
        """

        :param enumerable:
        """
    @property
    def Items(self) -> Array[object]:
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

class SystemCore_EnumerableDebugViewEmptyException(Exception, _Exception, ISerializable):
    """"""

    def __init__(self):
        """"""
    @property
    def Data(self) -> IDictionary:
        """

        :return:
        """
    @property
    def Empty(self) -> str:
        """

        :return:
        """
    @property
    def HResult(self) -> int:
        """

        :return:
        """
    @property
    def HelpLink(self) -> str:
        """

        :return:
        """
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """

        :return:
        """
    @property
    def Message(self) -> str:
        """

        :return:
        """
    @property
    def Source(self) -> str:
        """

        :return:
        """
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """

        :return:
        """
    @property
    def TargetSite(self) -> MethodBase:
        """

        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetBaseException(self) -> Exception:
        """

        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """

class TypeHelper(ABC, Object):
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
