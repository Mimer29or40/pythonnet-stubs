from __future__ import annotations

from abc import ABC
from typing import Generic
from typing import Iterator
from typing import Tuple
from typing import TypeVar
from typing import overload

from System import Action
from System import Array
from System import Delegate
from System import Enum
from System import Func
from System import Guid
from System import IntPtr
from System import Object
from System import Type
from System.Collections import IEnumerable
from System.Collections import IEnumerator
from System.Collections.Generic import ICollection
from System.Collections.Generic import IEnumerable
from System.Collections.Generic import IList
from System.Collections.ObjectModel import ReadOnlyCollection
from System.ComponentModel import CategoryAttribute
from System.ComponentModel import DescriptionAttribute
from System.Reflection import ConstructorInfo
from System.Reflection import FieldInfo
from System.Reflection import MemberInfo
from System.Reflection import MethodInfo
from System.Reflection import PropertyInfo
from System.Reflection.Emit import MethodBuilder
from System.Resources import ResourceManager
from System.Runtime.CompilerServices import CallSiteBinder
from System.Runtime.CompilerServices import DebugInfoGenerator
from System.Runtime.InteropServices import _Attribute

R = TypeVar("R")
T = TypeVar("T")
T1 = TypeVar("T1")
T2 = TypeVar("T2")
T3 = TypeVar("T3")
TDelegate = TypeVar("TDelegate")

class AnalyzeTypeIsResult(Enum):
    """"""

    KnownFalse: AnalyzeTypeIsResult = ...
    """"""
    KnownTrue: AnalyzeTypeIsResult = ...
    """"""
    KnownAssignable: AnalyzeTypeIsResult = ...
    """"""
    Unknown: AnalyzeTypeIsResult = ...
    """"""

class ArgumentProviderOps(ABC, Object):
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

class AssignBinaryExpression(BinaryExpression):
    """"""

    @property
    def CanReduce(self) -> bool:
        """

        :return:
        """
    @property
    def Conversion(self) -> LambdaExpression:
        """

        :return:
        """
    @property
    def IsLifted(self) -> bool:
        """

        :return:
        """
    @property
    def IsLiftedToNull(self) -> bool:
        """

        :return:
        """
    @property
    def Left(self) -> Expression:
        """

        :return:
        """
    @property
    def Method(self) -> MethodInfo:
        """

        :return:
        """
    @property
    def NodeType(self) -> ExpressionType:
        """

        :return:
        """
    @property
    def Right(self) -> Expression:
        """

        :return:
        """
    @property
    def Type(self) -> Type:
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
    def Reduce(self) -> Expression:
        """

        :return:
        """
    def ReduceAndCheck(self) -> Expression:
        """

        :return:
        """
    def ReduceExtensions(self) -> Expression:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Update(
        self, left: Expression, conversion: LambdaExpression, right: Expression
    ) -> BinaryExpression:
        """

        :param left:
        :param conversion:
        :param right:
        :return:
        """

class BinaryExpression(Expression):
    """"""

    @property
    def CanReduce(self) -> bool:
        """

        :return:
        """
    @property
    def Conversion(self) -> LambdaExpression:
        """

        :return:
        """
    @property
    def IsLifted(self) -> bool:
        """

        :return:
        """
    @property
    def IsLiftedToNull(self) -> bool:
        """

        :return:
        """
    @property
    def Left(self) -> Expression:
        """

        :return:
        """
    @property
    def Method(self) -> MethodInfo:
        """

        :return:
        """
    @property
    def NodeType(self) -> ExpressionType:
        """

        :return:
        """
    @property
    def Right(self) -> Expression:
        """

        :return:
        """
    @property
    def Type(self) -> Type:
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
    def Reduce(self) -> Expression:
        """

        :return:
        """
    def ReduceAndCheck(self) -> Expression:
        """

        :return:
        """
    def ReduceExtensions(self) -> Expression:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Update(
        self, left: Expression, conversion: LambdaExpression, right: Expression
    ) -> BinaryExpression:
        """

        :param left:
        :param conversion:
        :param right:
        :return:
        """

class Block2(BlockExpression):
    """"""

    @property
    def CanReduce(self) -> bool:
        """

        :return:
        """
    @property
    def Expressions(self) -> ReadOnlyCollection[Expression]:
        """

        :return:
        """
    @property
    def NodeType(self) -> ExpressionType:
        """

        :return:
        """
    @property
    def Result(self) -> Expression:
        """

        :return:
        """
    @property
    def Type(self) -> Type:
        """

        :return:
        """
    @property
    def Variables(self) -> ReadOnlyCollection[ParameterExpression]:
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
    def Reduce(self) -> Expression:
        """

        :return:
        """
    def ReduceAndCheck(self) -> Expression:
        """

        :return:
        """
    def ReduceExtensions(self) -> Expression:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Update(
        self, variables: IEnumerable[ParameterExpression], expressions: IEnumerable[Expression]
    ) -> BlockExpression:
        """

        :param variables:
        :param expressions:
        :return:
        """

class Block3(BlockExpression):
    """"""

    @property
    def CanReduce(self) -> bool:
        """

        :return:
        """
    @property
    def Expressions(self) -> ReadOnlyCollection[Expression]:
        """

        :return:
        """
    @property
    def NodeType(self) -> ExpressionType:
        """

        :return:
        """
    @property
    def Result(self) -> Expression:
        """

        :return:
        """
    @property
    def Type(self) -> Type:
        """

        :return:
        """
    @property
    def Variables(self) -> ReadOnlyCollection[ParameterExpression]:
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
    def Reduce(self) -> Expression:
        """

        :return:
        """
    def ReduceAndCheck(self) -> Expression:
        """

        :return:
        """
    def ReduceExtensions(self) -> Expression:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Update(
        self, variables: IEnumerable[ParameterExpression], expressions: IEnumerable[Expression]
    ) -> BlockExpression:
        """

        :param variables:
        :param expressions:
        :return:
        """

class Block4(BlockExpression):
    """"""

    @property
    def CanReduce(self) -> bool:
        """

        :return:
        """
    @property
    def Expressions(self) -> ReadOnlyCollection[Expression]:
        """

        :return:
        """
    @property
    def NodeType(self) -> ExpressionType:
        """

        :return:
        """
    @property
    def Result(self) -> Expression:
        """

        :return:
        """
    @property
    def Type(self) -> Type:
        """

        :return:
        """
    @property
    def Variables(self) -> ReadOnlyCollection[ParameterExpression]:
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
    def Reduce(self) -> Expression:
        """

        :return:
        """
    def ReduceAndCheck(self) -> Expression:
        """

        :return:
        """
    def ReduceExtensions(self) -> Expression:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Update(
        self, variables: IEnumerable[ParameterExpression], expressions: IEnumerable[Expression]
    ) -> BlockExpression:
        """

        :param variables:
        :param expressions:
        :return:
        """

class Block5(BlockExpression):
    """"""

    @property
    def CanReduce(self) -> bool:
        """

        :return:
        """
    @property
    def Expressions(self) -> ReadOnlyCollection[Expression]:
        """

        :return:
        """
    @property
    def NodeType(self) -> ExpressionType:
        """

        :return:
        """
    @property
    def Result(self) -> Expression:
        """

        :return:
        """
    @property
    def Type(self) -> Type:
        """

        :return:
        """
    @property
    def Variables(self) -> ReadOnlyCollection[ParameterExpression]:
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
    def Reduce(self) -> Expression:
        """

        :return:
        """
    def ReduceAndCheck(self) -> Expression:
        """

        :return:
        """
    def ReduceExtensions(self) -> Expression:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Update(
        self, variables: IEnumerable[ParameterExpression], expressions: IEnumerable[Expression]
    ) -> BlockExpression:
        """

        :param variables:
        :param expressions:
        :return:
        """

class BlockExpression(Expression):
    """"""

    @property
    def CanReduce(self) -> bool:
        """

        :return:
        """
    @property
    def Expressions(self) -> ReadOnlyCollection[Expression]:
        """

        :return:
        """
    @property
    def NodeType(self) -> ExpressionType:
        """

        :return:
        """
    @property
    def Result(self) -> Expression:
        """

        :return:
        """
    @property
    def Type(self) -> Type:
        """

        :return:
        """
    @property
    def Variables(self) -> ReadOnlyCollection[ParameterExpression]:
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
    def Reduce(self) -> Expression:
        """

        :return:
        """
    def ReduceAndCheck(self) -> Expression:
        """

        :return:
        """
    def ReduceExtensions(self) -> Expression:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Update(
        self, variables: IEnumerable[ParameterExpression], expressions: IEnumerable[Expression]
    ) -> BlockExpression:
        """

        :param variables:
        :param expressions:
        :return:
        """

class BlockExpressionList(
    Object, ICollection[Expression], IEnumerable[Expression], IList[Expression], IEnumerable
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
    def Item(self) -> Expression:
        """

        :return:
        """
    @Item.setter
    def Item(self, value: Expression) -> None: ...
    def Add(self, item: Expression) -> None:
        """

        :param item:
        """
    def Clear(self) -> None:
        """"""
    def Contains(self, item: Expression) -> bool:
        """

        :param item:
        :return:
        """
    def CopyTo(self, array: Array[Expression], arrayIndex: int) -> None:
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
    def IndexOf(self, item: Expression) -> int:
        """

        :param item:
        :return:
        """
    def Insert(self, index: int, item: Expression) -> None:
        """

        :param index:
        :param item:
        """
    def Remove(self, item: Expression) -> bool:
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
    def __contains__(self, value: Expression) -> bool:
        """

        :param value:
        :return:
        """
    def __getitem__(self, index: int) -> Expression:
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
    def __iter__(self) -> Iterator[Expression]:
        """

        :return:
        """
    def __len__(self) -> int:
        """

        :return:
        """
    def __setitem__(self, index: int, value: Expression) -> None:
        """

        :param index:
        :param value:
        """

class BlockN(BlockExpression):
    """"""

    @property
    def CanReduce(self) -> bool:
        """

        :return:
        """
    @property
    def Expressions(self) -> ReadOnlyCollection[Expression]:
        """

        :return:
        """
    @property
    def NodeType(self) -> ExpressionType:
        """

        :return:
        """
    @property
    def Result(self) -> Expression:
        """

        :return:
        """
    @property
    def Type(self) -> Type:
        """

        :return:
        """
    @property
    def Variables(self) -> ReadOnlyCollection[ParameterExpression]:
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
    def Reduce(self) -> Expression:
        """

        :return:
        """
    def ReduceAndCheck(self) -> Expression:
        """

        :return:
        """
    def ReduceExtensions(self) -> Expression:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Update(
        self, variables: IEnumerable[ParameterExpression], expressions: IEnumerable[Expression]
    ) -> BlockExpression:
        """

        :param variables:
        :param expressions:
        :return:
        """

class ByRefParameterExpression(TypedParameterExpression):
    """"""

    @property
    def CanReduce(self) -> bool:
        """

        :return:
        """
    @property
    def IsByRef(self) -> bool:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def NodeType(self) -> ExpressionType:
        """

        :return:
        """
    @property
    def Type(self) -> Type:
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
    def Reduce(self) -> Expression:
        """

        :return:
        """
    def ReduceAndCheck(self) -> Expression:
        """

        :return:
        """
    def ReduceExtensions(self) -> Expression:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CatchBlock(Object):
    """"""

    @property
    def Body(self) -> Expression:
        """

        :return:
        """
    @property
    def Filter(self) -> Expression:
        """

        :return:
        """
    @property
    def Test(self) -> Type:
        """

        :return:
        """
    @property
    def Variable(self) -> ParameterExpression:
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
    def Update(
        self, variable: ParameterExpression, filter: Expression, body: Expression
    ) -> CatchBlock:
        """

        :param variable:
        :param filter:
        :param body:
        :return:
        """

class ClearDebugInfoExpression(DebugInfoExpression):
    """"""

    @property
    def CanReduce(self) -> bool:
        """

        :return:
        """
    @property
    def Document(self) -> SymbolDocumentInfo:
        """

        :return:
        """
    @property
    def EndColumn(self) -> int:
        """

        :return:
        """
    @property
    def EndLine(self) -> int:
        """

        :return:
        """
    @property
    def IsClear(self) -> bool:
        """

        :return:
        """
    @property
    def NodeType(self) -> ExpressionType:
        """

        :return:
        """
    @property
    def StartColumn(self) -> int:
        """

        :return:
        """
    @property
    def StartLine(self) -> int:
        """

        :return:
        """
    @property
    def Type(self) -> Type:
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
    def Reduce(self) -> Expression:
        """

        :return:
        """
    def ReduceAndCheck(self) -> Expression:
        """

        :return:
        """
    def ReduceExtensions(self) -> Expression:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CoalesceConversionBinaryExpression(BinaryExpression):
    """"""

    @property
    def CanReduce(self) -> bool:
        """

        :return:
        """
    @property
    def Conversion(self) -> LambdaExpression:
        """

        :return:
        """
    @property
    def IsLifted(self) -> bool:
        """

        :return:
        """
    @property
    def IsLiftedToNull(self) -> bool:
        """

        :return:
        """
    @property
    def Left(self) -> Expression:
        """

        :return:
        """
    @property
    def Method(self) -> MethodInfo:
        """

        :return:
        """
    @property
    def NodeType(self) -> ExpressionType:
        """

        :return:
        """
    @property
    def Right(self) -> Expression:
        """

        :return:
        """
    @property
    def Type(self) -> Type:
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
    def Reduce(self) -> Expression:
        """

        :return:
        """
    def ReduceAndCheck(self) -> Expression:
        """

        :return:
        """
    def ReduceExtensions(self) -> Expression:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Update(
        self, left: Expression, conversion: LambdaExpression, right: Expression
    ) -> BinaryExpression:
        """

        :param left:
        :param conversion:
        :param right:
        :return:
        """

class ConditionalExpression(Expression):
    """"""

    @property
    def CanReduce(self) -> bool:
        """

        :return:
        """
    @property
    def IfFalse(self) -> Expression:
        """

        :return:
        """
    @property
    def IfTrue(self) -> Expression:
        """

        :return:
        """
    @property
    def NodeType(self) -> ExpressionType:
        """

        :return:
        """
    @property
    def Test(self) -> Expression:
        """

        :return:
        """
    @property
    def Type(self) -> Type:
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
    def Reduce(self) -> Expression:
        """

        :return:
        """
    def ReduceAndCheck(self) -> Expression:
        """

        :return:
        """
    def ReduceExtensions(self) -> Expression:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Update(
        self, test: Expression, ifTrue: Expression, ifFalse: Expression
    ) -> ConditionalExpression:
        """

        :param test:
        :param ifTrue:
        :param ifFalse:
        :return:
        """

class ConstantCheck(ABC, Object):
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

class ConstantExpression(Expression):
    """"""

    @property
    def CanReduce(self) -> bool:
        """

        :return:
        """
    @property
    def NodeType(self) -> ExpressionType:
        """

        :return:
        """
    @property
    def Type(self) -> Type:
        """

        :return:
        """
    @property
    def Value(self) -> object:
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
    def Reduce(self) -> Expression:
        """

        :return:
        """
    def ReduceAndCheck(self) -> Expression:
        """

        :return:
        """
    def ReduceExtensions(self) -> Expression:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class DebugInfoExpression(Expression):
    """"""

    @property
    def CanReduce(self) -> bool:
        """

        :return:
        """
    @property
    def Document(self) -> SymbolDocumentInfo:
        """

        :return:
        """
    @property
    def EndColumn(self) -> int:
        """

        :return:
        """
    @property
    def EndLine(self) -> int:
        """

        :return:
        """
    @property
    def IsClear(self) -> bool:
        """

        :return:
        """
    @property
    def NodeType(self) -> ExpressionType:
        """

        :return:
        """
    @property
    def StartColumn(self) -> int:
        """

        :return:
        """
    @property
    def StartLine(self) -> int:
        """

        :return:
        """
    @property
    def Type(self) -> Type:
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
    def Reduce(self) -> Expression:
        """

        :return:
        """
    def ReduceAndCheck(self) -> Expression:
        """

        :return:
        """
    def ReduceExtensions(self) -> Expression:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class DebugViewWriter(ExpressionVisitor):
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
    def Visit(self, nodes: ReadOnlyCollection[Expression]) -> ReadOnlyCollection[Expression]:
        """

        :param nodes:
        :return:
        """
    @overload
    def Visit(self, node: Expression) -> Expression:
        """

        :param node:
        :return:
        """
    @overload
    def VisitAndConvert(self, node: T, callerName: str) -> T:
        """

        :param node:
        :param callerName:
        :return:
        """
    @overload
    def VisitAndConvert(
        self, nodes: ReadOnlyCollection[T], callerName: str
    ) -> ReadOnlyCollection[T]:
        """

        :param nodes:
        :param callerName:
        :return:
        """

class DefaultExpression(Expression):
    """"""

    @property
    def CanReduce(self) -> bool:
        """

        :return:
        """
    @property
    def NodeType(self) -> ExpressionType:
        """

        :return:
        """
    @property
    def Type(self) -> Type:
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
    def Reduce(self) -> Expression:
        """

        :return:
        """
    def ReduceAndCheck(self) -> Expression:
        """

        :return:
        """
    def ReduceExtensions(self) -> Expression:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class DynamicExpression(Expression, IArgumentProvider, IDynamicExpression):
    """"""

    @property
    def ArgumentCount(self) -> int:
        """

        :return:
        """
    @property
    def Arguments(self) -> ReadOnlyCollection[Expression]:
        """

        :return:
        """
    @property
    def Binder(self) -> CallSiteBinder:
        """

        :return:
        """
    @property
    def CanReduce(self) -> bool:
        """

        :return:
        """
    @property
    def DelegateType(self) -> Type:
        """

        :return:
        """
    @property
    def NodeType(self) -> ExpressionType:
        """

        :return:
        """
    @property
    def Type(self) -> Type:
        """

        :return:
        """
    def CreateCallSite(self) -> object:
        """

        :return:
        """
    @classmethod
    @overload
    def Dynamic(
        cls, binder: CallSiteBinder, returnType: Type, arguments: IEnumerable[Expression]
    ) -> DynamicExpression:
        """

        :param binder:
        :param returnType:
        :param arguments:
        :return:
        """
    @classmethod
    @overload
    def Dynamic(
        cls, binder: CallSiteBinder, returnType: Type, arg0: Expression
    ) -> DynamicExpression:
        """

        :param binder:
        :param returnType:
        :param arg0:
        :return:
        """
    @classmethod
    @overload
    def Dynamic(
        cls, binder: CallSiteBinder, returnType: Type, arguments: Array[Expression]
    ) -> DynamicExpression:
        """

        :param binder:
        :param returnType:
        :param arguments:
        :return:
        """
    @classmethod
    @overload
    def Dynamic(
        cls, binder: CallSiteBinder, returnType: Type, arg0: Expression, arg1: Expression
    ) -> DynamicExpression:
        """

        :param binder:
        :param returnType:
        :param arg0:
        :param arg1:
        :return:
        """
    @classmethod
    @overload
    def Dynamic(
        cls,
        binder: CallSiteBinder,
        returnType: Type,
        arg0: Expression,
        arg1: Expression,
        arg2: Expression,
    ) -> DynamicExpression:
        """

        :param binder:
        :param returnType:
        :param arg0:
        :param arg1:
        :param arg2:
        :return:
        """
    @classmethod
    @overload
    def Dynamic(
        cls,
        binder: CallSiteBinder,
        returnType: Type,
        arg0: Expression,
        arg1: Expression,
        arg2: Expression,
        arg3: Expression,
    ) -> DynamicExpression:
        """

        :param binder:
        :param returnType:
        :param arg0:
        :param arg1:
        :param arg2:
        :param arg3:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetArgument(self, index: int) -> Expression:
        """

        :param index:
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
    def MakeDynamic(
        cls, delegateType: Type, binder: CallSiteBinder, arguments: IEnumerable[Expression]
    ) -> DynamicExpression:
        """

        :param delegateType:
        :param binder:
        :param arguments:
        :return:
        """
    @classmethod
    @overload
    def MakeDynamic(
        cls, delegateType: Type, binder: CallSiteBinder, arg0: Expression
    ) -> DynamicExpression:
        """

        :param delegateType:
        :param binder:
        :param arg0:
        :return:
        """
    @classmethod
    @overload
    def MakeDynamic(
        cls, delegateType: Type, binder: CallSiteBinder, arguments: Array[Expression]
    ) -> DynamicExpression:
        """

        :param delegateType:
        :param binder:
        :param arguments:
        :return:
        """
    @classmethod
    @overload
    def MakeDynamic(
        cls, delegateType: Type, binder: CallSiteBinder, arg0: Expression, arg1: Expression
    ) -> DynamicExpression:
        """

        :param delegateType:
        :param binder:
        :param arg0:
        :param arg1:
        :return:
        """
    @classmethod
    @overload
    def MakeDynamic(
        cls,
        delegateType: Type,
        binder: CallSiteBinder,
        arg0: Expression,
        arg1: Expression,
        arg2: Expression,
    ) -> DynamicExpression:
        """

        :param delegateType:
        :param binder:
        :param arg0:
        :param arg1:
        :param arg2:
        :return:
        """
    @classmethod
    @overload
    def MakeDynamic(
        cls,
        delegateType: Type,
        binder: CallSiteBinder,
        arg0: Expression,
        arg1: Expression,
        arg2: Expression,
        arg3: Expression,
    ) -> DynamicExpression:
        """

        :param delegateType:
        :param binder:
        :param arg0:
        :param arg1:
        :param arg2:
        :param arg3:
        :return:
        """
    def Reduce(self) -> Expression:
        """

        :return:
        """
    def ReduceAndCheck(self) -> Expression:
        """

        :return:
        """
    def ReduceExtensions(self) -> Expression:
        """

        :return:
        """
    def Rewrite(self, args: Array[Expression]) -> Expression:
        """

        :param args:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Update(self, arguments: IEnumerable[Expression]) -> DynamicExpression:
        """

        :param arguments:
        :return:
        """

class DynamicExpression1(DynamicExpression, IArgumentProvider, IDynamicExpression):
    """"""

    @property
    def ArgumentCount(self) -> int:
        """

        :return:
        """
    @property
    def Arguments(self) -> ReadOnlyCollection[Expression]:
        """

        :return:
        """
    @property
    def Binder(self) -> CallSiteBinder:
        """

        :return:
        """
    @property
    def CanReduce(self) -> bool:
        """

        :return:
        """
    @property
    def DelegateType(self) -> Type:
        """

        :return:
        """
    @property
    def NodeType(self) -> ExpressionType:
        """

        :return:
        """
    @property
    def Type(self) -> Type:
        """

        :return:
        """
    def CreateCallSite(self) -> object:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetArgument(self, index: int) -> Expression:
        """

        :param index:
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
    def Reduce(self) -> Expression:
        """

        :return:
        """
    def ReduceAndCheck(self) -> Expression:
        """

        :return:
        """
    def ReduceExtensions(self) -> Expression:
        """

        :return:
        """
    def Rewrite(self, args: Array[Expression]) -> Expression:
        """

        :param args:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Update(self, arguments: IEnumerable[Expression]) -> DynamicExpression:
        """

        :param arguments:
        :return:
        """

class DynamicExpression2(DynamicExpression, IArgumentProvider, IDynamicExpression):
    """"""

    @property
    def ArgumentCount(self) -> int:
        """

        :return:
        """
    @property
    def Arguments(self) -> ReadOnlyCollection[Expression]:
        """

        :return:
        """
    @property
    def Binder(self) -> CallSiteBinder:
        """

        :return:
        """
    @property
    def CanReduce(self) -> bool:
        """

        :return:
        """
    @property
    def DelegateType(self) -> Type:
        """

        :return:
        """
    @property
    def NodeType(self) -> ExpressionType:
        """

        :return:
        """
    @property
    def Type(self) -> Type:
        """

        :return:
        """
    def CreateCallSite(self) -> object:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetArgument(self, index: int) -> Expression:
        """

        :param index:
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
    def Reduce(self) -> Expression:
        """

        :return:
        """
    def ReduceAndCheck(self) -> Expression:
        """

        :return:
        """
    def ReduceExtensions(self) -> Expression:
        """

        :return:
        """
    def Rewrite(self, args: Array[Expression]) -> Expression:
        """

        :param args:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Update(self, arguments: IEnumerable[Expression]) -> DynamicExpression:
        """

        :param arguments:
        :return:
        """

class DynamicExpression3(DynamicExpression, IArgumentProvider, IDynamicExpression):
    """"""

    @property
    def ArgumentCount(self) -> int:
        """

        :return:
        """
    @property
    def Arguments(self) -> ReadOnlyCollection[Expression]:
        """

        :return:
        """
    @property
    def Binder(self) -> CallSiteBinder:
        """

        :return:
        """
    @property
    def CanReduce(self) -> bool:
        """

        :return:
        """
    @property
    def DelegateType(self) -> Type:
        """

        :return:
        """
    @property
    def NodeType(self) -> ExpressionType:
        """

        :return:
        """
    @property
    def Type(self) -> Type:
        """

        :return:
        """
    def CreateCallSite(self) -> object:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetArgument(self, index: int) -> Expression:
        """

        :param index:
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
    def Reduce(self) -> Expression:
        """

        :return:
        """
    def ReduceAndCheck(self) -> Expression:
        """

        :return:
        """
    def ReduceExtensions(self) -> Expression:
        """

        :return:
        """
    def Rewrite(self, args: Array[Expression]) -> Expression:
        """

        :param args:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Update(self, arguments: IEnumerable[Expression]) -> DynamicExpression:
        """

        :param arguments:
        :return:
        """

class DynamicExpression4(DynamicExpression, IArgumentProvider, IDynamicExpression):
    """"""

    @property
    def ArgumentCount(self) -> int:
        """

        :return:
        """
    @property
    def Arguments(self) -> ReadOnlyCollection[Expression]:
        """

        :return:
        """
    @property
    def Binder(self) -> CallSiteBinder:
        """

        :return:
        """
    @property
    def CanReduce(self) -> bool:
        """

        :return:
        """
    @property
    def DelegateType(self) -> Type:
        """

        :return:
        """
    @property
    def NodeType(self) -> ExpressionType:
        """

        :return:
        """
    @property
    def Type(self) -> Type:
        """

        :return:
        """
    def CreateCallSite(self) -> object:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetArgument(self, index: int) -> Expression:
        """

        :param index:
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
    def Reduce(self) -> Expression:
        """

        :return:
        """
    def ReduceAndCheck(self) -> Expression:
        """

        :return:
        """
    def ReduceExtensions(self) -> Expression:
        """

        :return:
        """
    def Rewrite(self, args: Array[Expression]) -> Expression:
        """

        :param args:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Update(self, arguments: IEnumerable[Expression]) -> DynamicExpression:
        """

        :param arguments:
        :return:
        """

class DynamicExpressionN(DynamicExpression, IArgumentProvider, IDynamicExpression):
    """"""

    @property
    def ArgumentCount(self) -> int:
        """

        :return:
        """
    @property
    def Arguments(self) -> ReadOnlyCollection[Expression]:
        """

        :return:
        """
    @property
    def Binder(self) -> CallSiteBinder:
        """

        :return:
        """
    @property
    def CanReduce(self) -> bool:
        """

        :return:
        """
    @property
    def DelegateType(self) -> Type:
        """

        :return:
        """
    @property
    def NodeType(self) -> ExpressionType:
        """

        :return:
        """
    @property
    def Type(self) -> Type:
        """

        :return:
        """
    def CreateCallSite(self) -> object:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetArgument(self, index: int) -> Expression:
        """

        :param index:
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
    def Reduce(self) -> Expression:
        """

        :return:
        """
    def ReduceAndCheck(self) -> Expression:
        """

        :return:
        """
    def ReduceExtensions(self) -> Expression:
        """

        :return:
        """
    def Rewrite(self, args: Array[Expression]) -> Expression:
        """

        :param args:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Update(self, arguments: IEnumerable[Expression]) -> DynamicExpression:
        """

        :param arguments:
        :return:
        """

class DynamicExpressionVisitor(ABC, ExpressionVisitor):
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
    def Visit(self, nodes: ReadOnlyCollection[Expression]) -> ReadOnlyCollection[Expression]:
        """

        :param nodes:
        :return:
        """
    @overload
    def Visit(self, node: Expression) -> Expression:
        """

        :param node:
        :return:
        """
    @overload
    def VisitAndConvert(self, node: T, callerName: str) -> T:
        """

        :param node:
        :param callerName:
        :return:
        """
    @overload
    def VisitAndConvert(
        self, nodes: ReadOnlyCollection[T], callerName: str
    ) -> ReadOnlyCollection[T]:
        """

        :param nodes:
        :param callerName:
        :return:
        """

class ElementInit(Object, IArgumentProvider):
    """"""

    @property
    def AddMethod(self) -> MethodInfo:
        """

        :return:
        """
    @property
    def ArgumentCount(self) -> int:
        """

        :return:
        """
    @property
    def Arguments(self) -> ReadOnlyCollection[Expression]:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetArgument(self, index: int) -> Expression:
        """

        :param index:
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
    def Update(self, arguments: IEnumerable[Expression]) -> ElementInit:
        """

        :param arguments:
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

class Expression(ABC, Object):
    """"""

    @property
    def CanReduce(self) -> bool:
        """

        :return:
        """
    @property
    def NodeType(self) -> ExpressionType:
        """

        :return:
        """
    @property
    def Type(self) -> Type:
        """

        :return:
        """
    @classmethod
    @overload
    def Add(cls, left: Expression, right: Expression) -> BinaryExpression:
        """

        :param left:
        :param right:
        :return:
        """
    @classmethod
    @overload
    def Add(cls, left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression:
        """

        :param left:
        :param right:
        :param method:
        :return:
        """
    @classmethod
    @overload
    def AddAssign(cls, left: Expression, right: Expression) -> BinaryExpression:
        """

        :param left:
        :param right:
        :return:
        """
    @classmethod
    @overload
    def AddAssign(cls, left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression:
        """

        :param left:
        :param right:
        :param method:
        :return:
        """
    @classmethod
    @overload
    def AddAssign(
        cls, left: Expression, right: Expression, method: MethodInfo, conversion: LambdaExpression
    ) -> BinaryExpression:
        """

        :param left:
        :param right:
        :param method:
        :param conversion:
        :return:
        """
    @classmethod
    @overload
    def AddAssignChecked(cls, left: Expression, right: Expression) -> BinaryExpression:
        """

        :param left:
        :param right:
        :return:
        """
    @classmethod
    @overload
    def AddAssignChecked(
        cls, left: Expression, right: Expression, method: MethodInfo
    ) -> BinaryExpression:
        """

        :param left:
        :param right:
        :param method:
        :return:
        """
    @classmethod
    @overload
    def AddAssignChecked(
        cls, left: Expression, right: Expression, method: MethodInfo, conversion: LambdaExpression
    ) -> BinaryExpression:
        """

        :param left:
        :param right:
        :param method:
        :param conversion:
        :return:
        """
    @classmethod
    @overload
    def AddChecked(cls, left: Expression, right: Expression) -> BinaryExpression:
        """

        :param left:
        :param right:
        :return:
        """
    @classmethod
    @overload
    def AddChecked(
        cls, left: Expression, right: Expression, method: MethodInfo
    ) -> BinaryExpression:
        """

        :param left:
        :param right:
        :param method:
        :return:
        """
    @classmethod
    @overload
    def And(cls, left: Expression, right: Expression) -> BinaryExpression:
        """

        :param left:
        :param right:
        :return:
        """
    @classmethod
    @overload
    def And(cls, left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression:
        """

        :param left:
        :param right:
        :param method:
        :return:
        """
    @classmethod
    @overload
    def AndAlso(cls, left: Expression, right: Expression) -> BinaryExpression:
        """

        :param left:
        :param right:
        :return:
        """
    @classmethod
    @overload
    def AndAlso(cls, left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression:
        """

        :param left:
        :param right:
        :param method:
        :return:
        """
    @classmethod
    @overload
    def AndAssign(cls, left: Expression, right: Expression) -> BinaryExpression:
        """

        :param left:
        :param right:
        :return:
        """
    @classmethod
    @overload
    def AndAssign(cls, left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression:
        """

        :param left:
        :param right:
        :param method:
        :return:
        """
    @classmethod
    @overload
    def AndAssign(
        cls, left: Expression, right: Expression, method: MethodInfo, conversion: LambdaExpression
    ) -> BinaryExpression:
        """

        :param left:
        :param right:
        :param method:
        :param conversion:
        :return:
        """
    @classmethod
    @overload
    def ArrayAccess(cls, array: Expression, indexes: IEnumerable[Expression]) -> IndexExpression:
        """

        :param array:
        :param indexes:
        :return:
        """
    @classmethod
    @overload
    def ArrayAccess(cls, array: Expression, indexes: Array[Expression]) -> IndexExpression:
        """

        :param array:
        :param indexes:
        :return:
        """
    @classmethod
    @overload
    def ArrayIndex(
        cls, array: Expression, indexes: IEnumerable[Expression]
    ) -> MethodCallExpression:
        """

        :param array:
        :param indexes:
        :return:
        """
    @classmethod
    @overload
    def ArrayIndex(cls, array: Expression, index: Expression) -> BinaryExpression:
        """

        :param array:
        :param index:
        :return:
        """
    @classmethod
    @overload
    def ArrayIndex(cls, array: Expression, indexes: Array[Expression]) -> MethodCallExpression:
        """

        :param array:
        :param indexes:
        :return:
        """
    @classmethod
    def ArrayLength(cls, array: Expression) -> UnaryExpression:
        """

        :param array:
        :return:
        """
    @classmethod
    def Assign(cls, left: Expression, right: Expression) -> BinaryExpression:
        """

        :param left:
        :param right:
        :return:
        """
    @classmethod
    @overload
    def Bind(cls, member: MemberInfo, expression: Expression) -> MemberAssignment:
        """

        :param member:
        :param expression:
        :return:
        """
    @classmethod
    @overload
    def Bind(cls, propertyAccessor: MethodInfo, expression: Expression) -> MemberAssignment:
        """

        :param propertyAccessor:
        :param expression:
        :return:
        """
    @classmethod
    @overload
    def Block(cls, expressions: IEnumerable[Expression]) -> BlockExpression:
        """

        :param expressions:
        :return:
        """
    @classmethod
    @overload
    def Block(cls, expressions: Array[Expression]) -> BlockExpression:
        """

        :param expressions:
        :return:
        """
    @classmethod
    @overload
    def Block(
        cls, variables: IEnumerable[ParameterExpression], expressions: IEnumerable[Expression]
    ) -> BlockExpression:
        """

        :param variables:
        :param expressions:
        :return:
        """
    @classmethod
    @overload
    def Block(
        cls, variables: IEnumerable[ParameterExpression], expressions: Array[Expression]
    ) -> BlockExpression:
        """

        :param variables:
        :param expressions:
        :return:
        """
    @classmethod
    @overload
    def Block(cls, arg0: Expression, arg1: Expression) -> BlockExpression:
        """

        :param arg0:
        :param arg1:
        :return:
        """
    @classmethod
    @overload
    def Block(cls, type: Type, expressions: IEnumerable[Expression]) -> BlockExpression:
        """

        :param type:
        :param expressions:
        :return:
        """
    @classmethod
    @overload
    def Block(cls, type: Type, expressions: Array[Expression]) -> BlockExpression:
        """

        :param type:
        :param expressions:
        :return:
        """
    @classmethod
    @overload
    def Block(cls, arg0: Expression, arg1: Expression, arg2: Expression) -> BlockExpression:
        """

        :param arg0:
        :param arg1:
        :param arg2:
        :return:
        """
    @classmethod
    @overload
    def Block(
        cls,
        type: Type,
        variables: IEnumerable[ParameterExpression],
        expressions: IEnumerable[Expression],
    ) -> BlockExpression:
        """

        :param type:
        :param variables:
        :param expressions:
        :return:
        """
    @classmethod
    @overload
    def Block(
        cls, type: Type, variables: IEnumerable[ParameterExpression], expressions: Array[Expression]
    ) -> BlockExpression:
        """

        :param type:
        :param variables:
        :param expressions:
        :return:
        """
    @classmethod
    @overload
    def Block(
        cls, arg0: Expression, arg1: Expression, arg2: Expression, arg3: Expression
    ) -> BlockExpression:
        """

        :param arg0:
        :param arg1:
        :param arg2:
        :param arg3:
        :return:
        """
    @classmethod
    @overload
    def Block(
        cls,
        arg0: Expression,
        arg1: Expression,
        arg2: Expression,
        arg3: Expression,
        arg4: Expression,
    ) -> BlockExpression:
        """

        :param arg0:
        :param arg1:
        :param arg2:
        :param arg3:
        :param arg4:
        :return:
        """
    @classmethod
    @overload
    def Break(cls, target: LabelTarget) -> GotoExpression:
        """

        :param target:
        :return:
        """
    @classmethod
    @overload
    def Break(cls, target: LabelTarget, value: Expression) -> GotoExpression:
        """

        :param target:
        :param value:
        :return:
        """
    @classmethod
    @overload
    def Break(cls, target: LabelTarget, type: Type) -> GotoExpression:
        """

        :param target:
        :param type:
        :return:
        """
    @classmethod
    @overload
    def Break(cls, target: LabelTarget, value: Expression, type: Type) -> GotoExpression:
        """

        :param target:
        :param value:
        :param type:
        :return:
        """
    @classmethod
    @overload
    def Call(cls, instance: Expression, method: MethodInfo) -> MethodCallExpression:
        """

        :param instance:
        :param method:
        :return:
        """
    @classmethod
    @overload
    def Call(cls, method: MethodInfo, arguments: IEnumerable[Expression]) -> MethodCallExpression:
        """

        :param method:
        :param arguments:
        :return:
        """
    @classmethod
    @overload
    def Call(cls, method: MethodInfo, arg0: Expression) -> MethodCallExpression:
        """

        :param method:
        :param arg0:
        :return:
        """
    @classmethod
    @overload
    def Call(cls, method: MethodInfo, arguments: Array[Expression]) -> MethodCallExpression:
        """

        :param method:
        :param arguments:
        :return:
        """
    @classmethod
    @overload
    def Call(
        cls, instance: Expression, method: MethodInfo, arguments: IEnumerable[Expression]
    ) -> MethodCallExpression:
        """

        :param instance:
        :param method:
        :param arguments:
        :return:
        """
    @classmethod
    @overload
    def Call(
        cls, instance: Expression, method: MethodInfo, arguments: Array[Expression]
    ) -> MethodCallExpression:
        """

        :param instance:
        :param method:
        :param arguments:
        :return:
        """
    @classmethod
    @overload
    def Call(cls, method: MethodInfo, arg0: Expression, arg1: Expression) -> MethodCallExpression:
        """

        :param method:
        :param arg0:
        :param arg1:
        :return:
        """
    @classmethod
    @overload
    def Call(
        cls, instance: Expression, method: MethodInfo, arg0: Expression, arg1: Expression
    ) -> MethodCallExpression:
        """

        :param instance:
        :param method:
        :param arg0:
        :param arg1:
        :return:
        """
    @classmethod
    @overload
    def Call(
        cls,
        instance: Expression,
        methodName: str,
        typeArguments: Array[Type],
        arguments: Array[Expression],
    ) -> MethodCallExpression:
        """

        :param instance:
        :param methodName:
        :param typeArguments:
        :param arguments:
        :return:
        """
    @classmethod
    @overload
    def Call(
        cls, method: MethodInfo, arg0: Expression, arg1: Expression, arg2: Expression
    ) -> MethodCallExpression:
        """

        :param method:
        :param arg0:
        :param arg1:
        :param arg2:
        :return:
        """
    @classmethod
    @overload
    def Call(
        cls, type: Type, methodName: str, typeArguments: Array[Type], arguments: Array[Expression]
    ) -> MethodCallExpression:
        """

        :param type:
        :param methodName:
        :param typeArguments:
        :param arguments:
        :return:
        """
    @classmethod
    @overload
    def Call(
        cls,
        instance: Expression,
        method: MethodInfo,
        arg0: Expression,
        arg1: Expression,
        arg2: Expression,
    ) -> MethodCallExpression:
        """

        :param instance:
        :param method:
        :param arg0:
        :param arg1:
        :param arg2:
        :return:
        """
    @classmethod
    @overload
    def Call(
        cls,
        method: MethodInfo,
        arg0: Expression,
        arg1: Expression,
        arg2: Expression,
        arg3: Expression,
    ) -> MethodCallExpression:
        """

        :param method:
        :param arg0:
        :param arg1:
        :param arg2:
        :param arg3:
        :return:
        """
    @classmethod
    @overload
    def Call(
        cls,
        method: MethodInfo,
        arg0: Expression,
        arg1: Expression,
        arg2: Expression,
        arg3: Expression,
        arg4: Expression,
    ) -> MethodCallExpression:
        """

        :param method:
        :param arg0:
        :param arg1:
        :param arg2:
        :param arg3:
        :param arg4:
        :return:
        """
    @classmethod
    @overload
    def Catch(cls, variable: ParameterExpression, body: Expression) -> CatchBlock:
        """

        :param variable:
        :param body:
        :return:
        """
    @classmethod
    @overload
    def Catch(cls, type: Type, body: Expression) -> CatchBlock:
        """

        :param type:
        :param body:
        :return:
        """
    @classmethod
    @overload
    def Catch(
        cls, variable: ParameterExpression, body: Expression, filter: Expression
    ) -> CatchBlock:
        """

        :param variable:
        :param body:
        :param filter:
        :return:
        """
    @classmethod
    @overload
    def Catch(cls, type: Type, body: Expression, filter: Expression) -> CatchBlock:
        """

        :param type:
        :param body:
        :param filter:
        :return:
        """
    @classmethod
    def ClearDebugInfo(cls, document: SymbolDocumentInfo) -> DebugInfoExpression:
        """

        :param document:
        :return:
        """
    @classmethod
    @overload
    def Coalesce(cls, left: Expression, right: Expression) -> BinaryExpression:
        """

        :param left:
        :param right:
        :return:
        """
    @classmethod
    @overload
    def Coalesce(
        cls, left: Expression, right: Expression, conversion: LambdaExpression
    ) -> BinaryExpression:
        """

        :param left:
        :param right:
        :param conversion:
        :return:
        """
    @classmethod
    @overload
    def Condition(
        cls, test: Expression, ifTrue: Expression, ifFalse: Expression
    ) -> ConditionalExpression:
        """

        :param test:
        :param ifTrue:
        :param ifFalse:
        :return:
        """
    @classmethod
    @overload
    def Condition(
        cls, test: Expression, ifTrue: Expression, ifFalse: Expression, type: Type
    ) -> ConditionalExpression:
        """

        :param test:
        :param ifTrue:
        :param ifFalse:
        :param type:
        :return:
        """
    @classmethod
    @overload
    def Constant(cls, value: object) -> ConstantExpression:
        """

        :param value:
        :return:
        """
    @classmethod
    @overload
    def Constant(cls, value: object, type: Type) -> ConstantExpression:
        """

        :param value:
        :param type:
        :return:
        """
    @classmethod
    @overload
    def Continue(cls, target: LabelTarget) -> GotoExpression:
        """

        :param target:
        :return:
        """
    @classmethod
    @overload
    def Continue(cls, target: LabelTarget, type: Type) -> GotoExpression:
        """

        :param target:
        :param type:
        :return:
        """
    @classmethod
    @overload
    def Convert(cls, expression: Expression, type: Type) -> UnaryExpression:
        """

        :param expression:
        :param type:
        :return:
        """
    @classmethod
    @overload
    def Convert(cls, expression: Expression, type: Type, method: MethodInfo) -> UnaryExpression:
        """

        :param expression:
        :param type:
        :param method:
        :return:
        """
    @classmethod
    @overload
    def ConvertChecked(cls, expression: Expression, type: Type) -> UnaryExpression:
        """

        :param expression:
        :param type:
        :return:
        """
    @classmethod
    @overload
    def ConvertChecked(
        cls, expression: Expression, type: Type, method: MethodInfo
    ) -> UnaryExpression:
        """

        :param expression:
        :param type:
        :param method:
        :return:
        """
    @classmethod
    def DebugInfo(
        cls,
        document: SymbolDocumentInfo,
        startLine: int,
        startColumn: int,
        endLine: int,
        endColumn: int,
    ) -> DebugInfoExpression:
        """

        :param document:
        :param startLine:
        :param startColumn:
        :param endLine:
        :param endColumn:
        :return:
        """
    @classmethod
    @overload
    def Decrement(cls, expression: Expression) -> UnaryExpression:
        """

        :param expression:
        :return:
        """
    @classmethod
    @overload
    def Decrement(cls, expression: Expression, method: MethodInfo) -> UnaryExpression:
        """

        :param expression:
        :param method:
        :return:
        """
    @classmethod
    def Default(cls, type: Type) -> DefaultExpression:
        """

        :param type:
        :return:
        """
    @classmethod
    @overload
    def Divide(cls, left: Expression, right: Expression) -> BinaryExpression:
        """

        :param left:
        :param right:
        :return:
        """
    @classmethod
    @overload
    def Divide(cls, left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression:
        """

        :param left:
        :param right:
        :param method:
        :return:
        """
    @classmethod
    @overload
    def DivideAssign(cls, left: Expression, right: Expression) -> BinaryExpression:
        """

        :param left:
        :param right:
        :return:
        """
    @classmethod
    @overload
    def DivideAssign(
        cls, left: Expression, right: Expression, method: MethodInfo
    ) -> BinaryExpression:
        """

        :param left:
        :param right:
        :param method:
        :return:
        """
    @classmethod
    @overload
    def DivideAssign(
        cls, left: Expression, right: Expression, method: MethodInfo, conversion: LambdaExpression
    ) -> BinaryExpression:
        """

        :param left:
        :param right:
        :param method:
        :param conversion:
        :return:
        """
    @classmethod
    @overload
    def Dynamic(
        cls, binder: CallSiteBinder, returnType: Type, arguments: IEnumerable[Expression]
    ) -> DynamicExpression:
        """

        :param binder:
        :param returnType:
        :param arguments:
        :return:
        """
    @classmethod
    @overload
    def Dynamic(
        cls, binder: CallSiteBinder, returnType: Type, arg0: Expression
    ) -> DynamicExpression:
        """

        :param binder:
        :param returnType:
        :param arg0:
        :return:
        """
    @classmethod
    @overload
    def Dynamic(
        cls, binder: CallSiteBinder, returnType: Type, arguments: Array[Expression]
    ) -> DynamicExpression:
        """

        :param binder:
        :param returnType:
        :param arguments:
        :return:
        """
    @classmethod
    @overload
    def Dynamic(
        cls, binder: CallSiteBinder, returnType: Type, arg0: Expression, arg1: Expression
    ) -> DynamicExpression:
        """

        :param binder:
        :param returnType:
        :param arg0:
        :param arg1:
        :return:
        """
    @classmethod
    @overload
    def Dynamic(
        cls,
        binder: CallSiteBinder,
        returnType: Type,
        arg0: Expression,
        arg1: Expression,
        arg2: Expression,
    ) -> DynamicExpression:
        """

        :param binder:
        :param returnType:
        :param arg0:
        :param arg1:
        :param arg2:
        :return:
        """
    @classmethod
    @overload
    def Dynamic(
        cls,
        binder: CallSiteBinder,
        returnType: Type,
        arg0: Expression,
        arg1: Expression,
        arg2: Expression,
        arg3: Expression,
    ) -> DynamicExpression:
        """

        :param binder:
        :param returnType:
        :param arg0:
        :param arg1:
        :param arg2:
        :param arg3:
        :return:
        """
    @classmethod
    @overload
    def ElementInit(cls, addMethod: MethodInfo, arguments: IEnumerable[Expression]) -> ElementInit:
        """

        :param addMethod:
        :param arguments:
        :return:
        """
    @classmethod
    @overload
    def ElementInit(cls, addMethod: MethodInfo, arguments: Array[Expression]) -> ElementInit:
        """

        :param addMethod:
        :param arguments:
        :return:
        """
    @classmethod
    def Empty(cls) -> DefaultExpression:
        """

        :return:
        """
    @classmethod
    @overload
    def Equal(cls, left: Expression, right: Expression) -> BinaryExpression:
        """

        :param left:
        :param right:
        :return:
        """
    @classmethod
    @overload
    def Equal(
        cls, left: Expression, right: Expression, liftToNull: bool, method: MethodInfo
    ) -> BinaryExpression:
        """

        :param left:
        :param right:
        :param liftToNull:
        :param method:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @classmethod
    @overload
    def ExclusiveOr(cls, left: Expression, right: Expression) -> BinaryExpression:
        """

        :param left:
        :param right:
        :return:
        """
    @classmethod
    @overload
    def ExclusiveOr(
        cls, left: Expression, right: Expression, method: MethodInfo
    ) -> BinaryExpression:
        """

        :param left:
        :param right:
        :param method:
        :return:
        """
    @classmethod
    @overload
    def ExclusiveOrAssign(cls, left: Expression, right: Expression) -> BinaryExpression:
        """

        :param left:
        :param right:
        :return:
        """
    @classmethod
    @overload
    def ExclusiveOrAssign(
        cls, left: Expression, right: Expression, method: MethodInfo
    ) -> BinaryExpression:
        """

        :param left:
        :param right:
        :param method:
        :return:
        """
    @classmethod
    @overload
    def ExclusiveOrAssign(
        cls, left: Expression, right: Expression, method: MethodInfo, conversion: LambdaExpression
    ) -> BinaryExpression:
        """

        :param left:
        :param right:
        :param method:
        :param conversion:
        :return:
        """
    @classmethod
    @overload
    def Field(cls, expression: Expression, field: FieldInfo) -> MemberExpression:
        """

        :param expression:
        :param field:
        :return:
        """
    @classmethod
    @overload
    def Field(cls, expression: Expression, fieldName: str) -> MemberExpression:
        """

        :param expression:
        :param fieldName:
        :return:
        """
    @classmethod
    @overload
    def Field(cls, expression: Expression, type: Type, fieldName: str) -> MemberExpression:
        """

        :param expression:
        :param type:
        :param fieldName:
        :return:
        """
    @classmethod
    def GetActionType(cls, typeArgs: Array[Type]) -> Type:
        """

        :param typeArgs:
        :return:
        """
    @classmethod
    def GetDelegateType(cls, typeArgs: Array[Type]) -> Type:
        """

        :param typeArgs:
        :return:
        """
    @classmethod
    def GetFuncType(cls, typeArgs: Array[Type]) -> Type:
        """

        :param typeArgs:
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
    def Goto(cls, target: LabelTarget) -> GotoExpression:
        """

        :param target:
        :return:
        """
    @classmethod
    @overload
    def Goto(cls, target: LabelTarget, value: Expression) -> GotoExpression:
        """

        :param target:
        :param value:
        :return:
        """
    @classmethod
    @overload
    def Goto(cls, target: LabelTarget, type: Type) -> GotoExpression:
        """

        :param target:
        :param type:
        :return:
        """
    @classmethod
    @overload
    def Goto(cls, target: LabelTarget, value: Expression, type: Type) -> GotoExpression:
        """

        :param target:
        :param value:
        :param type:
        :return:
        """
    @classmethod
    @overload
    def GreaterThan(cls, left: Expression, right: Expression) -> BinaryExpression:
        """

        :param left:
        :param right:
        :return:
        """
    @classmethod
    @overload
    def GreaterThan(
        cls, left: Expression, right: Expression, liftToNull: bool, method: MethodInfo
    ) -> BinaryExpression:
        """

        :param left:
        :param right:
        :param liftToNull:
        :param method:
        :return:
        """
    @classmethod
    @overload
    def GreaterThanOrEqual(cls, left: Expression, right: Expression) -> BinaryExpression:
        """

        :param left:
        :param right:
        :return:
        """
    @classmethod
    @overload
    def GreaterThanOrEqual(
        cls, left: Expression, right: Expression, liftToNull: bool, method: MethodInfo
    ) -> BinaryExpression:
        """

        :param left:
        :param right:
        :param liftToNull:
        :param method:
        :return:
        """
    @classmethod
    def IfThen(cls, test: Expression, ifTrue: Expression) -> ConditionalExpression:
        """

        :param test:
        :param ifTrue:
        :return:
        """
    @classmethod
    def IfThenElse(
        cls, test: Expression, ifTrue: Expression, ifFalse: Expression
    ) -> ConditionalExpression:
        """

        :param test:
        :param ifTrue:
        :param ifFalse:
        :return:
        """
    @classmethod
    @overload
    def Increment(cls, expression: Expression) -> UnaryExpression:
        """

        :param expression:
        :return:
        """
    @classmethod
    @overload
    def Increment(cls, expression: Expression, method: MethodInfo) -> UnaryExpression:
        """

        :param expression:
        :param method:
        :return:
        """
    @classmethod
    @overload
    def Invoke(
        cls, expression: Expression, arguments: IEnumerable[Expression]
    ) -> InvocationExpression:
        """

        :param expression:
        :param arguments:
        :return:
        """
    @classmethod
    @overload
    def Invoke(cls, expression: Expression, arguments: Array[Expression]) -> InvocationExpression:
        """

        :param expression:
        :param arguments:
        :return:
        """
    @classmethod
    @overload
    def IsFalse(cls, expression: Expression) -> UnaryExpression:
        """

        :param expression:
        :return:
        """
    @classmethod
    @overload
    def IsFalse(cls, expression: Expression, method: MethodInfo) -> UnaryExpression:
        """

        :param expression:
        :param method:
        :return:
        """
    @classmethod
    @overload
    def IsTrue(cls, expression: Expression) -> UnaryExpression:
        """

        :param expression:
        :return:
        """
    @classmethod
    @overload
    def IsTrue(cls, expression: Expression, method: MethodInfo) -> UnaryExpression:
        """

        :param expression:
        :param method:
        :return:
        """
    @classmethod
    @overload
    def Label(cls) -> LabelTarget:
        """

        :return:
        """
    @classmethod
    @overload
    def Label(cls, target: LabelTarget) -> LabelExpression:
        """

        :param target:
        :return:
        """
    @classmethod
    @overload
    def Label(cls, name: str) -> LabelTarget:
        """

        :param name:
        :return:
        """
    @classmethod
    @overload
    def Label(cls, type: Type) -> LabelTarget:
        """

        :param type:
        :return:
        """
    @classmethod
    @overload
    def Label(cls, target: LabelTarget, defaultValue: Expression) -> LabelExpression:
        """

        :param target:
        :param defaultValue:
        :return:
        """
    @classmethod
    @overload
    def Label(cls, type: Type, name: str) -> LabelTarget:
        """

        :param type:
        :param name:
        :return:
        """
    @classmethod
    @overload
    def Lambda(
        cls, body: Expression, parameters: IEnumerable[ParameterExpression]
    ) -> Expression[TDelegate]:
        """

        :param body:
        :param parameters:
        :return:
        """
    @classmethod
    @overload
    def Lambda(
        cls, body: Expression, parameters: Array[ParameterExpression]
    ) -> Expression[TDelegate]:
        """

        :param body:
        :param parameters:
        :return:
        """
    @classmethod
    @overload
    def Lambda(
        cls, body: Expression, tailCall: bool, parameters: IEnumerable[ParameterExpression]
    ) -> Expression[TDelegate]:
        """

        :param body:
        :param tailCall:
        :param parameters:
        :return:
        """
    @classmethod
    @overload
    def Lambda(
        cls, body: Expression, tailCall: bool, parameters: Array[ParameterExpression]
    ) -> Expression[TDelegate]:
        """

        :param body:
        :param tailCall:
        :param parameters:
        :return:
        """
    @classmethod
    @overload
    def Lambda(
        cls, body: Expression, name: str, parameters: IEnumerable[ParameterExpression]
    ) -> Expression[TDelegate]:
        """

        :param body:
        :param name:
        :param parameters:
        :return:
        """
    @classmethod
    @overload
    def Lambda(
        cls, delegateType: Type, body: Expression, parameters: IEnumerable[ParameterExpression]
    ) -> LambdaExpression:
        """

        :param delegateType:
        :param body:
        :param parameters:
        :return:
        """
    @classmethod
    @overload
    def Lambda(
        cls, delegateType: Type, body: Expression, parameters: Array[ParameterExpression]
    ) -> LambdaExpression:
        """

        :param delegateType:
        :param body:
        :param parameters:
        :return:
        """
    @classmethod
    @overload
    def Lambda(
        cls,
        body: Expression,
        name: str,
        tailCall: bool,
        parameters: IEnumerable[ParameterExpression],
    ) -> LambdaExpression:
        """

        :param body:
        :param name:
        :param tailCall:
        :param parameters:
        :return:
        """
    @classmethod
    @overload
    def Lambda(
        cls,
        delegateType: Type,
        body: Expression,
        tailCall: bool,
        parameters: IEnumerable[ParameterExpression],
    ) -> LambdaExpression:
        """

        :param delegateType:
        :param body:
        :param tailCall:
        :param parameters:
        :return:
        """
    @classmethod
    @overload
    def Lambda(
        cls,
        delegateType: Type,
        body: Expression,
        tailCall: bool,
        parameters: Array[ParameterExpression],
    ) -> LambdaExpression:
        """

        :param delegateType:
        :param body:
        :param tailCall:
        :param parameters:
        :return:
        """
    @classmethod
    @overload
    def Lambda(
        cls,
        delegateType: Type,
        body: Expression,
        name: str,
        parameters: IEnumerable[ParameterExpression],
    ) -> LambdaExpression:
        """

        :param delegateType:
        :param body:
        :param name:
        :param parameters:
        :return:
        """
    @classmethod
    @overload
    def Lambda(
        cls,
        delegateType: Type,
        body: Expression,
        name: str,
        tailCall: bool,
        parameters: IEnumerable[ParameterExpression],
    ) -> LambdaExpression:
        """

        :param delegateType:
        :param body:
        :param name:
        :param tailCall:
        :param parameters:
        :return:
        """
    @classmethod
    @overload
    def LeftShift(cls, left: Expression, right: Expression) -> BinaryExpression:
        """

        :param left:
        :param right:
        :return:
        """
    @classmethod
    @overload
    def LeftShift(cls, left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression:
        """

        :param left:
        :param right:
        :param method:
        :return:
        """
    @classmethod
    @overload
    def LeftShiftAssign(cls, left: Expression, right: Expression) -> BinaryExpression:
        """

        :param left:
        :param right:
        :return:
        """
    @classmethod
    @overload
    def LeftShiftAssign(
        cls, left: Expression, right: Expression, method: MethodInfo
    ) -> BinaryExpression:
        """

        :param left:
        :param right:
        :param method:
        :return:
        """
    @classmethod
    @overload
    def LeftShiftAssign(
        cls, left: Expression, right: Expression, method: MethodInfo, conversion: LambdaExpression
    ) -> BinaryExpression:
        """

        :param left:
        :param right:
        :param method:
        :param conversion:
        :return:
        """
    @classmethod
    @overload
    def LessThan(cls, left: Expression, right: Expression) -> BinaryExpression:
        """

        :param left:
        :param right:
        :return:
        """
    @classmethod
    @overload
    def LessThan(
        cls, left: Expression, right: Expression, liftToNull: bool, method: MethodInfo
    ) -> BinaryExpression:
        """

        :param left:
        :param right:
        :param liftToNull:
        :param method:
        :return:
        """
    @classmethod
    @overload
    def LessThanOrEqual(cls, left: Expression, right: Expression) -> BinaryExpression:
        """

        :param left:
        :param right:
        :return:
        """
    @classmethod
    @overload
    def LessThanOrEqual(
        cls, left: Expression, right: Expression, liftToNull: bool, method: MethodInfo
    ) -> BinaryExpression:
        """

        :param left:
        :param right:
        :param liftToNull:
        :param method:
        :return:
        """
    @classmethod
    @overload
    def ListBind(
        cls, member: MemberInfo, initializers: IEnumerable[ElementInit]
    ) -> MemberListBinding:
        """

        :param member:
        :param initializers:
        :return:
        """
    @classmethod
    @overload
    def ListBind(cls, member: MemberInfo, initializers: Array[ElementInit]) -> MemberListBinding:
        """

        :param member:
        :param initializers:
        :return:
        """
    @classmethod
    @overload
    def ListBind(
        cls, propertyAccessor: MethodInfo, initializers: IEnumerable[ElementInit]
    ) -> MemberListBinding:
        """

        :param propertyAccessor:
        :param initializers:
        :return:
        """
    @classmethod
    @overload
    def ListBind(
        cls, propertyAccessor: MethodInfo, initializers: Array[ElementInit]
    ) -> MemberListBinding:
        """

        :param propertyAccessor:
        :param initializers:
        :return:
        """
    @classmethod
    @overload
    def ListInit(
        cls, newExpression: NewExpression, initializers: IEnumerable[ElementInit]
    ) -> ListInitExpression:
        """

        :param newExpression:
        :param initializers:
        :return:
        """
    @classmethod
    @overload
    def ListInit(
        cls, newExpression: NewExpression, initializers: IEnumerable[Expression]
    ) -> ListInitExpression:
        """

        :param newExpression:
        :param initializers:
        :return:
        """
    @classmethod
    @overload
    def ListInit(
        cls, newExpression: NewExpression, initializers: Array[ElementInit]
    ) -> ListInitExpression:
        """

        :param newExpression:
        :param initializers:
        :return:
        """
    @classmethod
    @overload
    def ListInit(
        cls, newExpression: NewExpression, initializers: Array[Expression]
    ) -> ListInitExpression:
        """

        :param newExpression:
        :param initializers:
        :return:
        """
    @classmethod
    @overload
    def ListInit(
        cls,
        newExpression: NewExpression,
        addMethod: MethodInfo,
        initializers: IEnumerable[Expression],
    ) -> ListInitExpression:
        """

        :param newExpression:
        :param addMethod:
        :param initializers:
        :return:
        """
    @classmethod
    @overload
    def ListInit(
        cls, newExpression: NewExpression, addMethod: MethodInfo, initializers: Array[Expression]
    ) -> ListInitExpression:
        """

        :param newExpression:
        :param addMethod:
        :param initializers:
        :return:
        """
    @classmethod
    @overload
    def Loop(cls, body: Expression) -> LoopExpression:
        """

        :param body:
        :return:
        """
    @classmethod
    @overload
    def Loop(cls, body: Expression, _break: LabelTarget) -> LoopExpression:
        """

        :param body:
        :param _break:
        :return:
        """
    @classmethod
    @overload
    def Loop(cls, body: Expression, _break: LabelTarget, _continue: LabelTarget) -> LoopExpression:
        """

        :param body:
        :param _break:
        :param _continue:
        :return:
        """
    @classmethod
    @overload
    def MakeBinary(
        cls, binaryType: ExpressionType, left: Expression, right: Expression
    ) -> BinaryExpression:
        """

        :param binaryType:
        :param left:
        :param right:
        :return:
        """
    @classmethod
    @overload
    def MakeBinary(
        cls,
        binaryType: ExpressionType,
        left: Expression,
        right: Expression,
        liftToNull: bool,
        method: MethodInfo,
    ) -> BinaryExpression:
        """

        :param binaryType:
        :param left:
        :param right:
        :param liftToNull:
        :param method:
        :return:
        """
    @classmethod
    @overload
    def MakeBinary(
        cls,
        binaryType: ExpressionType,
        left: Expression,
        right: Expression,
        liftToNull: bool,
        method: MethodInfo,
        conversion: LambdaExpression,
    ) -> BinaryExpression:
        """

        :param binaryType:
        :param left:
        :param right:
        :param liftToNull:
        :param method:
        :param conversion:
        :return:
        """
    @classmethod
    def MakeCatchBlock(
        cls, type: Type, variable: ParameterExpression, body: Expression, filter: Expression
    ) -> CatchBlock:
        """

        :param type:
        :param variable:
        :param body:
        :param filter:
        :return:
        """
    @classmethod
    @overload
    def MakeDynamic(
        cls, delegateType: Type, binder: CallSiteBinder, arguments: IEnumerable[Expression]
    ) -> DynamicExpression:
        """

        :param delegateType:
        :param binder:
        :param arguments:
        :return:
        """
    @classmethod
    @overload
    def MakeDynamic(
        cls, delegateType: Type, binder: CallSiteBinder, arg0: Expression
    ) -> DynamicExpression:
        """

        :param delegateType:
        :param binder:
        :param arg0:
        :return:
        """
    @classmethod
    @overload
    def MakeDynamic(
        cls, delegateType: Type, binder: CallSiteBinder, arguments: Array[Expression]
    ) -> DynamicExpression:
        """

        :param delegateType:
        :param binder:
        :param arguments:
        :return:
        """
    @classmethod
    @overload
    def MakeDynamic(
        cls, delegateType: Type, binder: CallSiteBinder, arg0: Expression, arg1: Expression
    ) -> DynamicExpression:
        """

        :param delegateType:
        :param binder:
        :param arg0:
        :param arg1:
        :return:
        """
    @classmethod
    @overload
    def MakeDynamic(
        cls,
        delegateType: Type,
        binder: CallSiteBinder,
        arg0: Expression,
        arg1: Expression,
        arg2: Expression,
    ) -> DynamicExpression:
        """

        :param delegateType:
        :param binder:
        :param arg0:
        :param arg1:
        :param arg2:
        :return:
        """
    @classmethod
    @overload
    def MakeDynamic(
        cls,
        delegateType: Type,
        binder: CallSiteBinder,
        arg0: Expression,
        arg1: Expression,
        arg2: Expression,
        arg3: Expression,
    ) -> DynamicExpression:
        """

        :param delegateType:
        :param binder:
        :param arg0:
        :param arg1:
        :param arg2:
        :param arg3:
        :return:
        """
    @classmethod
    def MakeGoto(
        cls, kind: GotoExpressionKind, target: LabelTarget, value: Expression, type: Type
    ) -> GotoExpression:
        """

        :param kind:
        :param target:
        :param value:
        :param type:
        :return:
        """
    @classmethod
    def MakeIndex(
        cls, instance: Expression, indexer: PropertyInfo, arguments: IEnumerable[Expression]
    ) -> IndexExpression:
        """

        :param instance:
        :param indexer:
        :param arguments:
        :return:
        """
    @classmethod
    def MakeMemberAccess(cls, expression: Expression, member: MemberInfo) -> MemberExpression:
        """

        :param expression:
        :param member:
        :return:
        """
    @classmethod
    def MakeTry(
        cls,
        type: Type,
        body: Expression,
        _finally: Expression,
        fault: Expression,
        handlers: IEnumerable[CatchBlock],
    ) -> TryExpression:
        """

        :param type:
        :param body:
        :param _finally:
        :param fault:
        :param handlers:
        :return:
        """
    @classmethod
    @overload
    def MakeUnary(
        cls, unaryType: ExpressionType, operand: Expression, type: Type
    ) -> UnaryExpression:
        """

        :param unaryType:
        :param operand:
        :param type:
        :return:
        """
    @classmethod
    @overload
    def MakeUnary(
        cls, unaryType: ExpressionType, operand: Expression, type: Type, method: MethodInfo
    ) -> UnaryExpression:
        """

        :param unaryType:
        :param operand:
        :param type:
        :param method:
        :return:
        """
    @classmethod
    @overload
    def MemberBind(
        cls, member: MemberInfo, bindings: IEnumerable[MemberBinding]
    ) -> MemberMemberBinding:
        """

        :param member:
        :param bindings:
        :return:
        """
    @classmethod
    @overload
    def MemberBind(cls, member: MemberInfo, bindings: Array[MemberBinding]) -> MemberMemberBinding:
        """

        :param member:
        :param bindings:
        :return:
        """
    @classmethod
    @overload
    def MemberBind(
        cls, propertyAccessor: MethodInfo, bindings: IEnumerable[MemberBinding]
    ) -> MemberMemberBinding:
        """

        :param propertyAccessor:
        :param bindings:
        :return:
        """
    @classmethod
    @overload
    def MemberBind(
        cls, propertyAccessor: MethodInfo, bindings: Array[MemberBinding]
    ) -> MemberMemberBinding:
        """

        :param propertyAccessor:
        :param bindings:
        :return:
        """
    @classmethod
    @overload
    def MemberInit(
        cls, newExpression: NewExpression, bindings: IEnumerable[MemberBinding]
    ) -> MemberInitExpression:
        """

        :param newExpression:
        :param bindings:
        :return:
        """
    @classmethod
    @overload
    def MemberInit(
        cls, newExpression: NewExpression, bindings: Array[MemberBinding]
    ) -> MemberInitExpression:
        """

        :param newExpression:
        :param bindings:
        :return:
        """
    @classmethod
    @overload
    def Modulo(cls, left: Expression, right: Expression) -> BinaryExpression:
        """

        :param left:
        :param right:
        :return:
        """
    @classmethod
    @overload
    def Modulo(cls, left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression:
        """

        :param left:
        :param right:
        :param method:
        :return:
        """
    @classmethod
    @overload
    def ModuloAssign(cls, left: Expression, right: Expression) -> BinaryExpression:
        """

        :param left:
        :param right:
        :return:
        """
    @classmethod
    @overload
    def ModuloAssign(
        cls, left: Expression, right: Expression, method: MethodInfo
    ) -> BinaryExpression:
        """

        :param left:
        :param right:
        :param method:
        :return:
        """
    @classmethod
    @overload
    def ModuloAssign(
        cls, left: Expression, right: Expression, method: MethodInfo, conversion: LambdaExpression
    ) -> BinaryExpression:
        """

        :param left:
        :param right:
        :param method:
        :param conversion:
        :return:
        """
    @classmethod
    @overload
    def Multiply(cls, left: Expression, right: Expression) -> BinaryExpression:
        """

        :param left:
        :param right:
        :return:
        """
    @classmethod
    @overload
    def Multiply(cls, left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression:
        """

        :param left:
        :param right:
        :param method:
        :return:
        """
    @classmethod
    @overload
    def MultiplyAssign(cls, left: Expression, right: Expression) -> BinaryExpression:
        """

        :param left:
        :param right:
        :return:
        """
    @classmethod
    @overload
    def MultiplyAssign(
        cls, left: Expression, right: Expression, method: MethodInfo
    ) -> BinaryExpression:
        """

        :param left:
        :param right:
        :param method:
        :return:
        """
    @classmethod
    @overload
    def MultiplyAssign(
        cls, left: Expression, right: Expression, method: MethodInfo, conversion: LambdaExpression
    ) -> BinaryExpression:
        """

        :param left:
        :param right:
        :param method:
        :param conversion:
        :return:
        """
    @classmethod
    @overload
    def MultiplyAssignChecked(cls, left: Expression, right: Expression) -> BinaryExpression:
        """

        :param left:
        :param right:
        :return:
        """
    @classmethod
    @overload
    def MultiplyAssignChecked(
        cls, left: Expression, right: Expression, method: MethodInfo
    ) -> BinaryExpression:
        """

        :param left:
        :param right:
        :param method:
        :return:
        """
    @classmethod
    @overload
    def MultiplyAssignChecked(
        cls, left: Expression, right: Expression, method: MethodInfo, conversion: LambdaExpression
    ) -> BinaryExpression:
        """

        :param left:
        :param right:
        :param method:
        :param conversion:
        :return:
        """
    @classmethod
    @overload
    def MultiplyChecked(cls, left: Expression, right: Expression) -> BinaryExpression:
        """

        :param left:
        :param right:
        :return:
        """
    @classmethod
    @overload
    def MultiplyChecked(
        cls, left: Expression, right: Expression, method: MethodInfo
    ) -> BinaryExpression:
        """

        :param left:
        :param right:
        :param method:
        :return:
        """
    @classmethod
    @overload
    def Negate(cls, expression: Expression) -> UnaryExpression:
        """

        :param expression:
        :return:
        """
    @classmethod
    @overload
    def Negate(cls, expression: Expression, method: MethodInfo) -> UnaryExpression:
        """

        :param expression:
        :param method:
        :return:
        """
    @classmethod
    @overload
    def NegateChecked(cls, expression: Expression) -> UnaryExpression:
        """

        :param expression:
        :return:
        """
    @classmethod
    @overload
    def NegateChecked(cls, expression: Expression, method: MethodInfo) -> UnaryExpression:
        """

        :param expression:
        :param method:
        :return:
        """
    @classmethod
    @overload
    def New(cls, constructor: ConstructorInfo) -> NewExpression:
        """

        :param constructor:
        :return:
        """
    @classmethod
    @overload
    def New(cls, type: Type) -> NewExpression:
        """

        :param type:
        :return:
        """
    @classmethod
    @overload
    def New(cls, constructor: ConstructorInfo, arguments: IEnumerable[Expression]) -> NewExpression:
        """

        :param constructor:
        :param arguments:
        :return:
        """
    @classmethod
    @overload
    def New(cls, constructor: ConstructorInfo, arguments: Array[Expression]) -> NewExpression:
        """

        :param constructor:
        :param arguments:
        :return:
        """
    @classmethod
    @overload
    def New(
        cls,
        constructor: ConstructorInfo,
        arguments: IEnumerable[Expression],
        members: IEnumerable[MemberInfo],
    ) -> NewExpression:
        """

        :param constructor:
        :param arguments:
        :param members:
        :return:
        """
    @classmethod
    @overload
    def New(
        cls,
        constructor: ConstructorInfo,
        arguments: IEnumerable[Expression],
        members: Array[MemberInfo],
    ) -> NewExpression:
        """

        :param constructor:
        :param arguments:
        :param members:
        :return:
        """
    @classmethod
    @overload
    def NewArrayBounds(cls, type: Type, bounds: IEnumerable[Expression]) -> NewArrayExpression:
        """

        :param type:
        :param bounds:
        :return:
        """
    @classmethod
    @overload
    def NewArrayBounds(cls, type: Type, bounds: Array[Expression]) -> NewArrayExpression:
        """

        :param type:
        :param bounds:
        :return:
        """
    @classmethod
    @overload
    def NewArrayInit(cls, type: Type, initializers: IEnumerable[Expression]) -> NewArrayExpression:
        """

        :param type:
        :param initializers:
        :return:
        """
    @classmethod
    @overload
    def NewArrayInit(cls, type: Type, initializers: Array[Expression]) -> NewArrayExpression:
        """

        :param type:
        :param initializers:
        :return:
        """
    @classmethod
    @overload
    def Not(cls, expression: Expression) -> UnaryExpression:
        """

        :param expression:
        :return:
        """
    @classmethod
    @overload
    def Not(cls, expression: Expression, method: MethodInfo) -> UnaryExpression:
        """

        :param expression:
        :param method:
        :return:
        """
    @classmethod
    @overload
    def NotEqual(cls, left: Expression, right: Expression) -> BinaryExpression:
        """

        :param left:
        :param right:
        :return:
        """
    @classmethod
    @overload
    def NotEqual(
        cls, left: Expression, right: Expression, liftToNull: bool, method: MethodInfo
    ) -> BinaryExpression:
        """

        :param left:
        :param right:
        :param liftToNull:
        :param method:
        :return:
        """
    @classmethod
    @overload
    def OnesComplement(cls, expression: Expression) -> UnaryExpression:
        """

        :param expression:
        :return:
        """
    @classmethod
    @overload
    def OnesComplement(cls, expression: Expression, method: MethodInfo) -> UnaryExpression:
        """

        :param expression:
        :param method:
        :return:
        """
    @classmethod
    @overload
    def Or(cls, left: Expression, right: Expression) -> BinaryExpression:
        """

        :param left:
        :param right:
        :return:
        """
    @classmethod
    @overload
    def Or(cls, left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression:
        """

        :param left:
        :param right:
        :param method:
        :return:
        """
    @classmethod
    @overload
    def OrAssign(cls, left: Expression, right: Expression) -> BinaryExpression:
        """

        :param left:
        :param right:
        :return:
        """
    @classmethod
    @overload
    def OrAssign(cls, left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression:
        """

        :param left:
        :param right:
        :param method:
        :return:
        """
    @classmethod
    @overload
    def OrAssign(
        cls, left: Expression, right: Expression, method: MethodInfo, conversion: LambdaExpression
    ) -> BinaryExpression:
        """

        :param left:
        :param right:
        :param method:
        :param conversion:
        :return:
        """
    @classmethod
    @overload
    def OrElse(cls, left: Expression, right: Expression) -> BinaryExpression:
        """

        :param left:
        :param right:
        :return:
        """
    @classmethod
    @overload
    def OrElse(cls, left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression:
        """

        :param left:
        :param right:
        :param method:
        :return:
        """
    @classmethod
    @overload
    def Parameter(cls, type: Type) -> ParameterExpression:
        """

        :param type:
        :return:
        """
    @classmethod
    @overload
    def Parameter(cls, type: Type, name: str) -> ParameterExpression:
        """

        :param type:
        :param name:
        :return:
        """
    @classmethod
    @overload
    def PostDecrementAssign(cls, expression: Expression) -> UnaryExpression:
        """

        :param expression:
        :return:
        """
    @classmethod
    @overload
    def PostDecrementAssign(cls, expression: Expression, method: MethodInfo) -> UnaryExpression:
        """

        :param expression:
        :param method:
        :return:
        """
    @classmethod
    @overload
    def PostIncrementAssign(cls, expression: Expression) -> UnaryExpression:
        """

        :param expression:
        :return:
        """
    @classmethod
    @overload
    def PostIncrementAssign(cls, expression: Expression, method: MethodInfo) -> UnaryExpression:
        """

        :param expression:
        :param method:
        :return:
        """
    @classmethod
    @overload
    def Power(cls, left: Expression, right: Expression) -> BinaryExpression:
        """

        :param left:
        :param right:
        :return:
        """
    @classmethod
    @overload
    def Power(cls, left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression:
        """

        :param left:
        :param right:
        :param method:
        :return:
        """
    @classmethod
    @overload
    def PowerAssign(cls, left: Expression, right: Expression) -> BinaryExpression:
        """

        :param left:
        :param right:
        :return:
        """
    @classmethod
    @overload
    def PowerAssign(
        cls, left: Expression, right: Expression, method: MethodInfo
    ) -> BinaryExpression:
        """

        :param left:
        :param right:
        :param method:
        :return:
        """
    @classmethod
    @overload
    def PowerAssign(
        cls, left: Expression, right: Expression, method: MethodInfo, conversion: LambdaExpression
    ) -> BinaryExpression:
        """

        :param left:
        :param right:
        :param method:
        :param conversion:
        :return:
        """
    @classmethod
    @overload
    def PreDecrementAssign(cls, expression: Expression) -> UnaryExpression:
        """

        :param expression:
        :return:
        """
    @classmethod
    @overload
    def PreDecrementAssign(cls, expression: Expression, method: MethodInfo) -> UnaryExpression:
        """

        :param expression:
        :param method:
        :return:
        """
    @classmethod
    @overload
    def PreIncrementAssign(cls, expression: Expression) -> UnaryExpression:
        """

        :param expression:
        :return:
        """
    @classmethod
    @overload
    def PreIncrementAssign(cls, expression: Expression, method: MethodInfo) -> UnaryExpression:
        """

        :param expression:
        :param method:
        :return:
        """
    @classmethod
    @overload
    def Property(cls, expression: Expression, propertyAccessor: MethodInfo) -> MemberExpression:
        """

        :param expression:
        :param propertyAccessor:
        :return:
        """
    @classmethod
    @overload
    def Property(cls, expression: Expression, property: PropertyInfo) -> MemberExpression:
        """

        :param expression:
        :param property:
        :return:
        """
    @classmethod
    @overload
    def Property(cls, expression: Expression, propertyName: str) -> MemberExpression:
        """

        :param expression:
        :param propertyName:
        :return:
        """
    @classmethod
    @overload
    def Property(
        cls, instance: Expression, indexer: PropertyInfo, arguments: IEnumerable[Expression]
    ) -> IndexExpression:
        """

        :param instance:
        :param indexer:
        :param arguments:
        :return:
        """
    @classmethod
    @overload
    def Property(
        cls, instance: Expression, indexer: PropertyInfo, arguments: Array[Expression]
    ) -> IndexExpression:
        """

        :param instance:
        :param indexer:
        :param arguments:
        :return:
        """
    @classmethod
    @overload
    def Property(
        cls, instance: Expression, propertyName: str, arguments: Array[Expression]
    ) -> IndexExpression:
        """

        :param instance:
        :param propertyName:
        :param arguments:
        :return:
        """
    @classmethod
    @overload
    def Property(cls, expression: Expression, type: Type, propertyName: str) -> MemberExpression:
        """

        :param expression:
        :param type:
        :param propertyName:
        :return:
        """
    @classmethod
    def PropertyOrField(cls, expression: Expression, propertyOrFieldName: str) -> MemberExpression:
        """

        :param expression:
        :param propertyOrFieldName:
        :return:
        """
    @classmethod
    def Quote(cls, expression: Expression) -> UnaryExpression:
        """

        :param expression:
        :return:
        """
    def Reduce(self) -> Expression:
        """

        :return:
        """
    def ReduceAndCheck(self) -> Expression:
        """

        :return:
        """
    def ReduceExtensions(self) -> Expression:
        """

        :return:
        """
    @classmethod
    def ReferenceEqual(cls, left: Expression, right: Expression) -> BinaryExpression:
        """

        :param left:
        :param right:
        :return:
        """
    @classmethod
    def ReferenceNotEqual(cls, left: Expression, right: Expression) -> BinaryExpression:
        """

        :param left:
        :param right:
        :return:
        """
    @classmethod
    @overload
    def Rethrow(cls) -> UnaryExpression:
        """

        :return:
        """
    @classmethod
    @overload
    def Rethrow(cls, type: Type) -> UnaryExpression:
        """

        :param type:
        :return:
        """
    @classmethod
    @overload
    def Return(cls, target: LabelTarget) -> GotoExpression:
        """

        :param target:
        :return:
        """
    @classmethod
    @overload
    def Return(cls, target: LabelTarget, value: Expression) -> GotoExpression:
        """

        :param target:
        :param value:
        :return:
        """
    @classmethod
    @overload
    def Return(cls, target: LabelTarget, type: Type) -> GotoExpression:
        """

        :param target:
        :param type:
        :return:
        """
    @classmethod
    @overload
    def Return(cls, target: LabelTarget, value: Expression, type: Type) -> GotoExpression:
        """

        :param target:
        :param value:
        :param type:
        :return:
        """
    @classmethod
    @overload
    def RightShift(cls, left: Expression, right: Expression) -> BinaryExpression:
        """

        :param left:
        :param right:
        :return:
        """
    @classmethod
    @overload
    def RightShift(
        cls, left: Expression, right: Expression, method: MethodInfo
    ) -> BinaryExpression:
        """

        :param left:
        :param right:
        :param method:
        :return:
        """
    @classmethod
    @overload
    def RightShiftAssign(cls, left: Expression, right: Expression) -> BinaryExpression:
        """

        :param left:
        :param right:
        :return:
        """
    @classmethod
    @overload
    def RightShiftAssign(
        cls, left: Expression, right: Expression, method: MethodInfo
    ) -> BinaryExpression:
        """

        :param left:
        :param right:
        :param method:
        :return:
        """
    @classmethod
    @overload
    def RightShiftAssign(
        cls, left: Expression, right: Expression, method: MethodInfo, conversion: LambdaExpression
    ) -> BinaryExpression:
        """

        :param left:
        :param right:
        :param method:
        :param conversion:
        :return:
        """
    @classmethod
    @overload
    def RuntimeVariables(
        cls, variables: IEnumerable[ParameterExpression]
    ) -> RuntimeVariablesExpression:
        """

        :param variables:
        :return:
        """
    @classmethod
    @overload
    def RuntimeVariables(cls, variables: Array[ParameterExpression]) -> RuntimeVariablesExpression:
        """

        :param variables:
        :return:
        """
    @classmethod
    @overload
    def Subtract(cls, left: Expression, right: Expression) -> BinaryExpression:
        """

        :param left:
        :param right:
        :return:
        """
    @classmethod
    @overload
    def Subtract(cls, left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression:
        """

        :param left:
        :param right:
        :param method:
        :return:
        """
    @classmethod
    @overload
    def SubtractAssign(cls, left: Expression, right: Expression) -> BinaryExpression:
        """

        :param left:
        :param right:
        :return:
        """
    @classmethod
    @overload
    def SubtractAssign(
        cls, left: Expression, right: Expression, method: MethodInfo
    ) -> BinaryExpression:
        """

        :param left:
        :param right:
        :param method:
        :return:
        """
    @classmethod
    @overload
    def SubtractAssign(
        cls, left: Expression, right: Expression, method: MethodInfo, conversion: LambdaExpression
    ) -> BinaryExpression:
        """

        :param left:
        :param right:
        :param method:
        :param conversion:
        :return:
        """
    @classmethod
    @overload
    def SubtractAssignChecked(cls, left: Expression, right: Expression) -> BinaryExpression:
        """

        :param left:
        :param right:
        :return:
        """
    @classmethod
    @overload
    def SubtractAssignChecked(
        cls, left: Expression, right: Expression, method: MethodInfo
    ) -> BinaryExpression:
        """

        :param left:
        :param right:
        :param method:
        :return:
        """
    @classmethod
    @overload
    def SubtractAssignChecked(
        cls, left: Expression, right: Expression, method: MethodInfo, conversion: LambdaExpression
    ) -> BinaryExpression:
        """

        :param left:
        :param right:
        :param method:
        :param conversion:
        :return:
        """
    @classmethod
    @overload
    def SubtractChecked(cls, left: Expression, right: Expression) -> BinaryExpression:
        """

        :param left:
        :param right:
        :return:
        """
    @classmethod
    @overload
    def SubtractChecked(
        cls, left: Expression, right: Expression, method: MethodInfo
    ) -> BinaryExpression:
        """

        :param left:
        :param right:
        :param method:
        :return:
        """
    @classmethod
    @overload
    def Switch(cls, switchValue: Expression, cases: Array[SwitchCase]) -> SwitchExpression:
        """

        :param switchValue:
        :param cases:
        :return:
        """
    @classmethod
    @overload
    def Switch(
        cls, switchValue: Expression, defaultBody: Expression, cases: Array[SwitchCase]
    ) -> SwitchExpression:
        """

        :param switchValue:
        :param defaultBody:
        :param cases:
        :return:
        """
    @classmethod
    @overload
    def Switch(
        cls,
        switchValue: Expression,
        defaultBody: Expression,
        comparison: MethodInfo,
        cases: IEnumerable[SwitchCase],
    ) -> SwitchExpression:
        """

        :param switchValue:
        :param defaultBody:
        :param comparison:
        :param cases:
        :return:
        """
    @classmethod
    @overload
    def Switch(
        cls,
        switchValue: Expression,
        defaultBody: Expression,
        comparison: MethodInfo,
        cases: Array[SwitchCase],
    ) -> SwitchExpression:
        """

        :param switchValue:
        :param defaultBody:
        :param comparison:
        :param cases:
        :return:
        """
    @classmethod
    @overload
    def Switch(
        cls,
        type: Type,
        switchValue: Expression,
        defaultBody: Expression,
        comparison: MethodInfo,
        cases: IEnumerable[SwitchCase],
    ) -> SwitchExpression:
        """

        :param type:
        :param switchValue:
        :param defaultBody:
        :param comparison:
        :param cases:
        :return:
        """
    @classmethod
    @overload
    def Switch(
        cls,
        type: Type,
        switchValue: Expression,
        defaultBody: Expression,
        comparison: MethodInfo,
        cases: Array[SwitchCase],
    ) -> SwitchExpression:
        """

        :param type:
        :param switchValue:
        :param defaultBody:
        :param comparison:
        :param cases:
        :return:
        """
    @classmethod
    @overload
    def SwitchCase(cls, body: Expression, testValues: IEnumerable[Expression]) -> SwitchCase:
        """

        :param body:
        :param testValues:
        :return:
        """
    @classmethod
    @overload
    def SwitchCase(cls, body: Expression, testValues: Array[Expression]) -> SwitchCase:
        """

        :param body:
        :param testValues:
        :return:
        """
    @classmethod
    @overload
    def SymbolDocument(cls, fileName: str) -> SymbolDocumentInfo:
        """

        :param fileName:
        :return:
        """
    @classmethod
    @overload
    def SymbolDocument(cls, fileName: str, language: Guid) -> SymbolDocumentInfo:
        """

        :param fileName:
        :param language:
        :return:
        """
    @classmethod
    @overload
    def SymbolDocument(
        cls, fileName: str, language: Guid, languageVendor: Guid
    ) -> SymbolDocumentInfo:
        """

        :param fileName:
        :param language:
        :param languageVendor:
        :return:
        """
    @classmethod
    @overload
    def SymbolDocument(
        cls, fileName: str, language: Guid, languageVendor: Guid, documentType: Guid
    ) -> SymbolDocumentInfo:
        """

        :param fileName:
        :param language:
        :param languageVendor:
        :param documentType:
        :return:
        """
    @classmethod
    @overload
    def Throw(cls, value: Expression) -> UnaryExpression:
        """

        :param value:
        :return:
        """
    @classmethod
    @overload
    def Throw(cls, value: Expression, type: Type) -> UnaryExpression:
        """

        :param value:
        :param type:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @classmethod
    def TryCatch(cls, body: Expression, handlers: Array[CatchBlock]) -> TryExpression:
        """

        :param body:
        :param handlers:
        :return:
        """
    @classmethod
    def TryCatchFinally(
        cls, body: Expression, _finally: Expression, handlers: Array[CatchBlock]
    ) -> TryExpression:
        """

        :param body:
        :param _finally:
        :param handlers:
        :return:
        """
    @classmethod
    def TryFault(cls, body: Expression, fault: Expression) -> TryExpression:
        """

        :param body:
        :param fault:
        :return:
        """
    @classmethod
    def TryFinally(cls, body: Expression, _finally: Expression) -> TryExpression:
        """

        :param body:
        :param _finally:
        :return:
        """
    @classmethod
    def TryGetActionType(cls, typeArgs: Array[Type], actionType: Type) -> Tuple[bool, Type]:
        """

        :param typeArgs:
        :param actionType:
        :return:
        """
    @classmethod
    def TryGetFuncType(cls, typeArgs: Array[Type], funcType: Type) -> Tuple[bool, Type]:
        """

        :param typeArgs:
        :param funcType:
        :return:
        """
    @classmethod
    def TypeAs(cls, expression: Expression, type: Type) -> UnaryExpression:
        """

        :param expression:
        :param type:
        :return:
        """
    @classmethod
    def TypeEqual(cls, expression: Expression, type: Type) -> TypeBinaryExpression:
        """

        :param expression:
        :param type:
        :return:
        """
    @classmethod
    def TypeIs(cls, expression: Expression, type: Type) -> TypeBinaryExpression:
        """

        :param expression:
        :param type:
        :return:
        """
    @classmethod
    @overload
    def UnaryPlus(cls, expression: Expression) -> UnaryExpression:
        """

        :param expression:
        :return:
        """
    @classmethod
    @overload
    def UnaryPlus(cls, expression: Expression, method: MethodInfo) -> UnaryExpression:
        """

        :param expression:
        :param method:
        :return:
        """
    @classmethod
    def Unbox(cls, expression: Expression, type: Type) -> UnaryExpression:
        """

        :param expression:
        :param type:
        :return:
        """
    @classmethod
    @overload
    def Variable(cls, type: Type) -> ParameterExpression:
        """

        :param type:
        :return:
        """
    @classmethod
    @overload
    def Variable(cls, type: Type, name: str) -> ParameterExpression:
        """

        :param type:
        :param name:
        :return:
        """

class Expression(Generic[TDelegate], LambdaExpression):
    """"""

    @property
    def Body(self) -> Expression:
        """

        :return:
        """
    @property
    def CanReduce(self) -> bool:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def NodeType(self) -> ExpressionType:
        """

        :return:
        """
    @property
    def Parameters(self) -> ReadOnlyCollection[ParameterExpression]:
        """

        :return:
        """
    @property
    def ReturnType(self) -> Type:
        """

        :return:
        """
    @property
    def TailCall(self) -> bool:
        """

        :return:
        """
    @property
    def Type(self) -> Type:
        """

        :return:
        """
    @overload
    def Compile(self) -> Delegate:
        """

        :return:
        """
    @overload
    def Compile(self, debugInfoGenerator: DebugInfoGenerator) -> Delegate:
        """

        :param debugInfoGenerator:
        :return:
        """
    @overload
    def Compile(self, preferInterpretation: bool) -> Delegate:
        """

        :param preferInterpretation:
        :return:
        """
    @overload
    def CompileToMethod(self, method: MethodBuilder) -> None:
        """

        :param method:
        """
    @overload
    def CompileToMethod(
        self, method: MethodBuilder, debugInfoGenerator: DebugInfoGenerator
    ) -> None:
        """

        :param method:
        :param debugInfoGenerator:
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
    def Reduce(self) -> Expression:
        """

        :return:
        """
    def ReduceAndCheck(self) -> Expression:
        """

        :return:
        """
    def ReduceExtensions(self) -> Expression:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Update(
        self, body: Expression, parameters: IEnumerable[ParameterExpression]
    ) -> Expression[TDelegate]:
        """

        :param body:
        :param parameters:
        :return:
        """

class ExpressionStringBuilder(ExpressionVisitor):
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
    def Visit(self, nodes: ReadOnlyCollection[Expression]) -> ReadOnlyCollection[Expression]:
        """

        :param nodes:
        :return:
        """
    @overload
    def Visit(self, node: Expression) -> Expression:
        """

        :param node:
        :return:
        """
    @overload
    def VisitAndConvert(self, node: T, callerName: str) -> T:
        """

        :param node:
        :param callerName:
        :return:
        """
    @overload
    def VisitAndConvert(
        self, nodes: ReadOnlyCollection[T], callerName: str
    ) -> ReadOnlyCollection[T]:
        """

        :param nodes:
        :param callerName:
        :return:
        """

class ExpressionType(Enum):
    """"""

    Add: ExpressionType = ...
    """"""
    AddChecked: ExpressionType = ...
    """"""
    And: ExpressionType = ...
    """"""
    AndAlso: ExpressionType = ...
    """"""
    ArrayLength: ExpressionType = ...
    """"""
    ArrayIndex: ExpressionType = ...
    """"""
    Call: ExpressionType = ...
    """"""
    Coalesce: ExpressionType = ...
    """"""
    Conditional: ExpressionType = ...
    """"""
    Constant: ExpressionType = ...
    """"""
    Convert: ExpressionType = ...
    """"""
    ConvertChecked: ExpressionType = ...
    """"""
    Divide: ExpressionType = ...
    """"""
    Equal: ExpressionType = ...
    """"""
    ExclusiveOr: ExpressionType = ...
    """"""
    GreaterThan: ExpressionType = ...
    """"""
    GreaterThanOrEqual: ExpressionType = ...
    """"""
    Invoke: ExpressionType = ...
    """"""
    Lambda: ExpressionType = ...
    """"""
    LeftShift: ExpressionType = ...
    """"""
    LessThan: ExpressionType = ...
    """"""
    LessThanOrEqual: ExpressionType = ...
    """"""
    ListInit: ExpressionType = ...
    """"""
    MemberAccess: ExpressionType = ...
    """"""
    MemberInit: ExpressionType = ...
    """"""
    Modulo: ExpressionType = ...
    """"""
    Multiply: ExpressionType = ...
    """"""
    MultiplyChecked: ExpressionType = ...
    """"""
    Negate: ExpressionType = ...
    """"""
    UnaryPlus: ExpressionType = ...
    """"""
    NegateChecked: ExpressionType = ...
    """"""
    New: ExpressionType = ...
    """"""
    NewArrayInit: ExpressionType = ...
    """"""
    NewArrayBounds: ExpressionType = ...
    """"""
    Not: ExpressionType = ...
    """"""
    NotEqual: ExpressionType = ...
    """"""
    Or: ExpressionType = ...
    """"""
    OrElse: ExpressionType = ...
    """"""
    Parameter: ExpressionType = ...
    """"""
    Power: ExpressionType = ...
    """"""
    Quote: ExpressionType = ...
    """"""
    RightShift: ExpressionType = ...
    """"""
    Subtract: ExpressionType = ...
    """"""
    SubtractChecked: ExpressionType = ...
    """"""
    TypeAs: ExpressionType = ...
    """"""
    TypeIs: ExpressionType = ...
    """"""
    Assign: ExpressionType = ...
    """"""
    Block: ExpressionType = ...
    """"""
    DebugInfo: ExpressionType = ...
    """"""
    Decrement: ExpressionType = ...
    """"""
    Dynamic: ExpressionType = ...
    """"""
    Default: ExpressionType = ...
    """"""
    Extension: ExpressionType = ...
    """"""
    Goto: ExpressionType = ...
    """"""
    Increment: ExpressionType = ...
    """"""
    Index: ExpressionType = ...
    """"""
    Label: ExpressionType = ...
    """"""
    RuntimeVariables: ExpressionType = ...
    """"""
    Loop: ExpressionType = ...
    """"""
    Switch: ExpressionType = ...
    """"""
    Throw: ExpressionType = ...
    """"""
    Try: ExpressionType = ...
    """"""
    Unbox: ExpressionType = ...
    """"""
    AddAssign: ExpressionType = ...
    """"""
    AndAssign: ExpressionType = ...
    """"""
    DivideAssign: ExpressionType = ...
    """"""
    ExclusiveOrAssign: ExpressionType = ...
    """"""
    LeftShiftAssign: ExpressionType = ...
    """"""
    ModuloAssign: ExpressionType = ...
    """"""
    MultiplyAssign: ExpressionType = ...
    """"""
    OrAssign: ExpressionType = ...
    """"""
    PowerAssign: ExpressionType = ...
    """"""
    RightShiftAssign: ExpressionType = ...
    """"""
    SubtractAssign: ExpressionType = ...
    """"""
    AddAssignChecked: ExpressionType = ...
    """"""
    MultiplyAssignChecked: ExpressionType = ...
    """"""
    SubtractAssignChecked: ExpressionType = ...
    """"""
    PreIncrementAssign: ExpressionType = ...
    """"""
    PreDecrementAssign: ExpressionType = ...
    """"""
    PostIncrementAssign: ExpressionType = ...
    """"""
    PostDecrementAssign: ExpressionType = ...
    """"""
    TypeEqual: ExpressionType = ...
    """"""
    OnesComplement: ExpressionType = ...
    """"""
    IsTrue: ExpressionType = ...
    """"""
    IsFalse: ExpressionType = ...
    """"""

class ExpressionVisitor(ABC, Object):
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
    def Visit(self, nodes: ReadOnlyCollection[Expression]) -> ReadOnlyCollection[Expression]:
        """

        :param nodes:
        :return:
        """
    @overload
    def Visit(self, node: Expression) -> Expression:
        """

        :param node:
        :return:
        """
    @classmethod
    @overload
    def Visit(
        cls, nodes: ReadOnlyCollection[T], elementVisitor: Func[T, T]
    ) -> ReadOnlyCollection[T]:
        """

        :param nodes:
        :param elementVisitor:
        :return:
        """
    @overload
    def VisitAndConvert(self, node: T, callerName: str) -> T:
        """

        :param node:
        :param callerName:
        :return:
        """
    @overload
    def VisitAndConvert(
        self, nodes: ReadOnlyCollection[T], callerName: str
    ) -> ReadOnlyCollection[T]:
        """

        :param nodes:
        :param callerName:
        :return:
        """

class FieldExpression(MemberExpression):
    """"""

    def __init__(self, expression: Expression, member: FieldInfo):
        """

        :param expression:
        :param member:
        """
    @property
    def CanReduce(self) -> bool:
        """

        :return:
        """
    @property
    def Expression(self) -> Expression:
        """

        :return:
        """
    @property
    def Member(self) -> MemberInfo:
        """

        :return:
        """
    @property
    def NodeType(self) -> ExpressionType:
        """

        :return:
        """
    @property
    def Type(self) -> Type:
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
    def Reduce(self) -> Expression:
        """

        :return:
        """
    def ReduceAndCheck(self) -> Expression:
        """

        :return:
        """
    def ReduceExtensions(self) -> Expression:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Update(self, expression: Expression) -> MemberExpression:
        """

        :param expression:
        :return:
        """

class FullConditionalExpression(ConditionalExpression):
    """"""

    @property
    def CanReduce(self) -> bool:
        """

        :return:
        """
    @property
    def IfFalse(self) -> Expression:
        """

        :return:
        """
    @property
    def IfTrue(self) -> Expression:
        """

        :return:
        """
    @property
    def NodeType(self) -> ExpressionType:
        """

        :return:
        """
    @property
    def Test(self) -> Expression:
        """

        :return:
        """
    @property
    def Type(self) -> Type:
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
    def Reduce(self) -> Expression:
        """

        :return:
        """
    def ReduceAndCheck(self) -> Expression:
        """

        :return:
        """
    def ReduceExtensions(self) -> Expression:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Update(
        self, test: Expression, ifTrue: Expression, ifFalse: Expression
    ) -> ConditionalExpression:
        """

        :param test:
        :param ifTrue:
        :param ifFalse:
        :return:
        """

class FullConditionalExpressionWithType(FullConditionalExpression):
    """"""

    @property
    def CanReduce(self) -> bool:
        """

        :return:
        """
    @property
    def IfFalse(self) -> Expression:
        """

        :return:
        """
    @property
    def IfTrue(self) -> Expression:
        """

        :return:
        """
    @property
    def NodeType(self) -> ExpressionType:
        """

        :return:
        """
    @property
    def Test(self) -> Expression:
        """

        :return:
        """
    @property
    def Type(self) -> Type:
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
    def Reduce(self) -> Expression:
        """

        :return:
        """
    def ReduceAndCheck(self) -> Expression:
        """

        :return:
        """
    def ReduceExtensions(self) -> Expression:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Update(
        self, test: Expression, ifTrue: Expression, ifFalse: Expression
    ) -> ConditionalExpression:
        """

        :param test:
        :param ifTrue:
        :param ifFalse:
        :return:
        """

class GotoExpression(Expression):
    """"""

    @property
    def CanReduce(self) -> bool:
        """

        :return:
        """
    @property
    def Kind(self) -> GotoExpressionKind:
        """

        :return:
        """
    @property
    def NodeType(self) -> ExpressionType:
        """

        :return:
        """
    @property
    def Target(self) -> LabelTarget:
        """

        :return:
        """
    @property
    def Type(self) -> Type:
        """

        :return:
        """
    @property
    def Value(self) -> Expression:
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
    def Reduce(self) -> Expression:
        """

        :return:
        """
    def ReduceAndCheck(self) -> Expression:
        """

        :return:
        """
    def ReduceExtensions(self) -> Expression:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Update(self, target: LabelTarget, value: Expression) -> GotoExpression:
        """

        :param target:
        :param value:
        :return:
        """

class GotoExpressionKind(Enum):
    """"""

    Goto: GotoExpressionKind = ...
    """"""
    Return: GotoExpressionKind = ...
    """"""
    Break: GotoExpressionKind = ...
    """"""
    Continue: GotoExpressionKind = ...
    """"""

class IArgumentProvider:
    """"""

    @property
    def ArgumentCount(self) -> int:
        """

        :return:
        """
    def GetArgument(self, index: int) -> Expression:
        """

        :param index:
        :return:
        """

class IDynamicExpression(IArgumentProvider):
    """"""

    @property
    def ArgumentCount(self) -> int:
        """

        :return:
        """
    @property
    def DelegateType(self) -> Type:
        """

        :return:
        """
    def CreateCallSite(self) -> object:
        """

        :return:
        """
    def GetArgument(self, index: int) -> Expression:
        """

        :param index:
        :return:
        """
    def Rewrite(self, args: Array[Expression]) -> Expression:
        """

        :param args:
        :return:
        """

class IndexExpression(Expression, IArgumentProvider):
    """"""

    @property
    def ArgumentCount(self) -> int:
        """

        :return:
        """
    @property
    def Arguments(self) -> ReadOnlyCollection[Expression]:
        """

        :return:
        """
    @property
    def CanReduce(self) -> bool:
        """

        :return:
        """
    @property
    def Indexer(self) -> PropertyInfo:
        """

        :return:
        """
    @property
    def NodeType(self) -> ExpressionType:
        """

        :return:
        """
    @property
    def Object(self) -> Expression:
        """

        :return:
        """
    @property
    def Type(self) -> Type:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetArgument(self, index: int) -> Expression:
        """

        :param index:
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
    def Reduce(self) -> Expression:
        """

        :return:
        """
    def ReduceAndCheck(self) -> Expression:
        """

        :return:
        """
    def ReduceExtensions(self) -> Expression:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Update(self, object: Expression, arguments: IEnumerable[Expression]) -> IndexExpression:
        """

        :param object:
        :param arguments:
        :return:
        """

class InstanceMethodCallExpression2(MethodCallExpression, IArgumentProvider):
    """"""

    def __init__(
        self, method: MethodInfo, instance: Expression, arg0: Expression, arg1: Expression
    ):
        """

        :param method:
        :param instance:
        :param arg0:
        :param arg1:
        """
    @property
    def ArgumentCount(self) -> int:
        """

        :return:
        """
    @property
    def Arguments(self) -> ReadOnlyCollection[Expression]:
        """

        :return:
        """
    @property
    def CanReduce(self) -> bool:
        """

        :return:
        """
    @property
    def Method(self) -> MethodInfo:
        """

        :return:
        """
    @property
    def NodeType(self) -> ExpressionType:
        """

        :return:
        """
    @property
    def Object(self) -> Expression:
        """

        :return:
        """
    @property
    def Type(self) -> Type:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetArgument(self, index: int) -> Expression:
        """

        :param index:
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
    def Reduce(self) -> Expression:
        """

        :return:
        """
    def ReduceAndCheck(self) -> Expression:
        """

        :return:
        """
    def ReduceExtensions(self) -> Expression:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Update(
        self, object: Expression, arguments: IEnumerable[Expression]
    ) -> MethodCallExpression:
        """

        :param object:
        :param arguments:
        :return:
        """

class InstanceMethodCallExpression3(MethodCallExpression, IArgumentProvider):
    """"""

    def __init__(
        self,
        method: MethodInfo,
        instance: Expression,
        arg0: Expression,
        arg1: Expression,
        arg2: Expression,
    ):
        """

        :param method:
        :param instance:
        :param arg0:
        :param arg1:
        :param arg2:
        """
    @property
    def ArgumentCount(self) -> int:
        """

        :return:
        """
    @property
    def Arguments(self) -> ReadOnlyCollection[Expression]:
        """

        :return:
        """
    @property
    def CanReduce(self) -> bool:
        """

        :return:
        """
    @property
    def Method(self) -> MethodInfo:
        """

        :return:
        """
    @property
    def NodeType(self) -> ExpressionType:
        """

        :return:
        """
    @property
    def Object(self) -> Expression:
        """

        :return:
        """
    @property
    def Type(self) -> Type:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetArgument(self, index: int) -> Expression:
        """

        :param index:
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
    def Reduce(self) -> Expression:
        """

        :return:
        """
    def ReduceAndCheck(self) -> Expression:
        """

        :return:
        """
    def ReduceExtensions(self) -> Expression:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Update(
        self, object: Expression, arguments: IEnumerable[Expression]
    ) -> MethodCallExpression:
        """

        :param object:
        :param arguments:
        :return:
        """

class InstanceMethodCallExpressionN(MethodCallExpression, IArgumentProvider):
    """"""

    def __init__(self, method: MethodInfo, instance: Expression, args: IList[Expression]):
        """

        :param method:
        :param instance:
        :param args:
        """
    @property
    def ArgumentCount(self) -> int:
        """

        :return:
        """
    @property
    def Arguments(self) -> ReadOnlyCollection[Expression]:
        """

        :return:
        """
    @property
    def CanReduce(self) -> bool:
        """

        :return:
        """
    @property
    def Method(self) -> MethodInfo:
        """

        :return:
        """
    @property
    def NodeType(self) -> ExpressionType:
        """

        :return:
        """
    @property
    def Object(self) -> Expression:
        """

        :return:
        """
    @property
    def Type(self) -> Type:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetArgument(self, index: int) -> Expression:
        """

        :param index:
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
    def Reduce(self) -> Expression:
        """

        :return:
        """
    def ReduceAndCheck(self) -> Expression:
        """

        :return:
        """
    def ReduceExtensions(self) -> Expression:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Update(
        self, object: Expression, arguments: IEnumerable[Expression]
    ) -> MethodCallExpression:
        """

        :param object:
        :param arguments:
        :return:
        """

class InvocationExpression(Expression, IArgumentProvider):
    """"""

    @property
    def ArgumentCount(self) -> int:
        """

        :return:
        """
    @property
    def Arguments(self) -> ReadOnlyCollection[Expression]:
        """

        :return:
        """
    @property
    def CanReduce(self) -> bool:
        """

        :return:
        """
    @property
    def Expression(self) -> Expression:
        """

        :return:
        """
    @property
    def NodeType(self) -> ExpressionType:
        """

        :return:
        """
    @property
    def Type(self) -> Type:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetArgument(self, index: int) -> Expression:
        """

        :param index:
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
    def Reduce(self) -> Expression:
        """

        :return:
        """
    def ReduceAndCheck(self) -> Expression:
        """

        :return:
        """
    def ReduceExtensions(self) -> Expression:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Update(
        self, expression: Expression, arguments: IEnumerable[Expression]
    ) -> InvocationExpression:
        """

        :param expression:
        :param arguments:
        :return:
        """

class LabelExpression(Expression):
    """"""

    @property
    def CanReduce(self) -> bool:
        """

        :return:
        """
    @property
    def DefaultValue(self) -> Expression:
        """

        :return:
        """
    @property
    def NodeType(self) -> ExpressionType:
        """

        :return:
        """
    @property
    def Target(self) -> LabelTarget:
        """

        :return:
        """
    @property
    def Type(self) -> Type:
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
    def Reduce(self) -> Expression:
        """

        :return:
        """
    def ReduceAndCheck(self) -> Expression:
        """

        :return:
        """
    def ReduceExtensions(self) -> Expression:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Update(self, target: LabelTarget, defaultValue: Expression) -> LabelExpression:
        """

        :param target:
        :param defaultValue:
        :return:
        """

class LabelTarget(Object):
    """"""

    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Type(self) -> Type:
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

class LambdaExpression(ABC, Expression):
    """"""

    @property
    def Body(self) -> Expression:
        """

        :return:
        """
    @property
    def CanReduce(self) -> bool:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def NodeType(self) -> ExpressionType:
        """

        :return:
        """
    @property
    def Parameters(self) -> ReadOnlyCollection[ParameterExpression]:
        """

        :return:
        """
    @property
    def ReturnType(self) -> Type:
        """

        :return:
        """
    @property
    def TailCall(self) -> bool:
        """

        :return:
        """
    @property
    def Type(self) -> Type:
        """

        :return:
        """
    @overload
    def Compile(self) -> Delegate:
        """

        :return:
        """
    @overload
    def Compile(self, debugInfoGenerator: DebugInfoGenerator) -> Delegate:
        """

        :param debugInfoGenerator:
        :return:
        """
    @overload
    def Compile(self, preferInterpretation: bool) -> Delegate:
        """

        :param preferInterpretation:
        :return:
        """
    @overload
    def CompileToMethod(self, method: MethodBuilder) -> None:
        """

        :param method:
        """
    @overload
    def CompileToMethod(
        self, method: MethodBuilder, debugInfoGenerator: DebugInfoGenerator
    ) -> None:
        """

        :param method:
        :param debugInfoGenerator:
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
    def Reduce(self) -> Expression:
        """

        :return:
        """
    def ReduceAndCheck(self) -> Expression:
        """

        :return:
        """
    def ReduceExtensions(self) -> Expression:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class ListArgumentProvider(
    Object, ICollection[Expression], IEnumerable[Expression], IList[Expression], IEnumerable
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
    def Item(self) -> Expression:
        """

        :return:
        """
    @Item.setter
    def Item(self, value: Expression) -> None: ...
    def Add(self, item: Expression) -> None:
        """

        :param item:
        """
    def Clear(self) -> None:
        """"""
    def Contains(self, item: Expression) -> bool:
        """

        :param item:
        :return:
        """
    def CopyTo(self, array: Array[Expression], arrayIndex: int) -> None:
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
    def IndexOf(self, item: Expression) -> int:
        """

        :param item:
        :return:
        """
    def Insert(self, index: int, item: Expression) -> None:
        """

        :param index:
        :param item:
        """
    def Remove(self, item: Expression) -> bool:
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
    def __contains__(self, value: Expression) -> bool:
        """

        :param value:
        :return:
        """
    def __getitem__(self, index: int) -> Expression:
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
    def __iter__(self) -> Iterator[Expression]:
        """

        :return:
        """
    def __len__(self) -> int:
        """

        :return:
        """
    def __setitem__(self, index: int, value: Expression) -> None:
        """

        :param index:
        :param value:
        """

class ListInitExpression(Expression):
    """"""

    @property
    def CanReduce(self) -> bool:
        """

        :return:
        """
    @property
    def Initializers(self) -> ReadOnlyCollection[ElementInit]:
        """

        :return:
        """
    @property
    def NewExpression(self) -> NewExpression:
        """

        :return:
        """
    @property
    def NodeType(self) -> ExpressionType:
        """

        :return:
        """
    @property
    def Type(self) -> Type:
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
    def Reduce(self) -> Expression:
        """

        :return:
        """
    def ReduceAndCheck(self) -> Expression:
        """

        :return:
        """
    def ReduceExtensions(self) -> Expression:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Update(
        self, newExpression: NewExpression, initializers: IEnumerable[ElementInit]
    ) -> ListInitExpression:
        """

        :param newExpression:
        :param initializers:
        :return:
        """

class LogicalBinaryExpression(BinaryExpression):
    """"""

    @property
    def CanReduce(self) -> bool:
        """

        :return:
        """
    @property
    def Conversion(self) -> LambdaExpression:
        """

        :return:
        """
    @property
    def IsLifted(self) -> bool:
        """

        :return:
        """
    @property
    def IsLiftedToNull(self) -> bool:
        """

        :return:
        """
    @property
    def Left(self) -> Expression:
        """

        :return:
        """
    @property
    def Method(self) -> MethodInfo:
        """

        :return:
        """
    @property
    def NodeType(self) -> ExpressionType:
        """

        :return:
        """
    @property
    def Right(self) -> Expression:
        """

        :return:
        """
    @property
    def Type(self) -> Type:
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
    def Reduce(self) -> Expression:
        """

        :return:
        """
    def ReduceAndCheck(self) -> Expression:
        """

        :return:
        """
    def ReduceExtensions(self) -> Expression:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Update(
        self, left: Expression, conversion: LambdaExpression, right: Expression
    ) -> BinaryExpression:
        """

        :param left:
        :param conversion:
        :param right:
        :return:
        """

class LoopExpression(Expression):
    """"""

    @property
    def Body(self) -> Expression:
        """

        :return:
        """
    @property
    def BreakLabel(self) -> LabelTarget:
        """

        :return:
        """
    @property
    def CanReduce(self) -> bool:
        """

        :return:
        """
    @property
    def ContinueLabel(self) -> LabelTarget:
        """

        :return:
        """
    @property
    def NodeType(self) -> ExpressionType:
        """

        :return:
        """
    @property
    def Type(self) -> Type:
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
    def Reduce(self) -> Expression:
        """

        :return:
        """
    def ReduceAndCheck(self) -> Expression:
        """

        :return:
        """
    def ReduceExtensions(self) -> Expression:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Update(
        self, breakLabel: LabelTarget, continueLabel: LabelTarget, body: Expression
    ) -> LoopExpression:
        """

        :param breakLabel:
        :param continueLabel:
        :param body:
        :return:
        """

class MemberAssignment(MemberBinding):
    """"""

    @property
    def BindingType(self) -> MemberBindingType:
        """

        :return:
        """
    @property
    def Expression(self) -> Expression:
        """

        :return:
        """
    @property
    def Member(self) -> MemberInfo:
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
    def Update(self, expression: Expression) -> MemberAssignment:
        """

        :param expression:
        :return:
        """

class MemberBinding(ABC, Object):
    """"""

    @property
    def BindingType(self) -> MemberBindingType:
        """

        :return:
        """
    @property
    def Member(self) -> MemberInfo:
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

class MemberBindingType(Enum):
    """"""

    Assignment: MemberBindingType = ...
    """"""
    MemberBinding: MemberBindingType = ...
    """"""
    ListBinding: MemberBindingType = ...
    """"""

class MemberExpression(Expression):
    """"""

    @property
    def CanReduce(self) -> bool:
        """

        :return:
        """
    @property
    def Expression(self) -> Expression:
        """

        :return:
        """
    @property
    def Member(self) -> MemberInfo:
        """

        :return:
        """
    @property
    def NodeType(self) -> ExpressionType:
        """

        :return:
        """
    @property
    def Type(self) -> Type:
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
    def Reduce(self) -> Expression:
        """

        :return:
        """
    def ReduceAndCheck(self) -> Expression:
        """

        :return:
        """
    def ReduceExtensions(self) -> Expression:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Update(self, expression: Expression) -> MemberExpression:
        """

        :param expression:
        :return:
        """

class MemberInitExpression(Expression):
    """"""

    @property
    def Bindings(self) -> ReadOnlyCollection[MemberBinding]:
        """

        :return:
        """
    @property
    def CanReduce(self) -> bool:
        """

        :return:
        """
    @property
    def NewExpression(self) -> NewExpression:
        """

        :return:
        """
    @property
    def NodeType(self) -> ExpressionType:
        """

        :return:
        """
    @property
    def Type(self) -> Type:
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
    def Reduce(self) -> Expression:
        """

        :return:
        """
    def ReduceAndCheck(self) -> Expression:
        """

        :return:
        """
    def ReduceExtensions(self) -> Expression:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Update(
        self, newExpression: NewExpression, bindings: IEnumerable[MemberBinding]
    ) -> MemberInitExpression:
        """

        :param newExpression:
        :param bindings:
        :return:
        """

class MemberListBinding(MemberBinding):
    """"""

    @property
    def BindingType(self) -> MemberBindingType:
        """

        :return:
        """
    @property
    def Initializers(self) -> ReadOnlyCollection[ElementInit]:
        """

        :return:
        """
    @property
    def Member(self) -> MemberInfo:
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
    def Update(self, initializers: IEnumerable[ElementInit]) -> MemberListBinding:
        """

        :param initializers:
        :return:
        """

class MemberMemberBinding(MemberBinding):
    """"""

    @property
    def BindingType(self) -> MemberBindingType:
        """

        :return:
        """
    @property
    def Bindings(self) -> ReadOnlyCollection[MemberBinding]:
        """

        :return:
        """
    @property
    def Member(self) -> MemberInfo:
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
    def Update(self, bindings: IEnumerable[MemberBinding]) -> MemberMemberBinding:
        """

        :param bindings:
        :return:
        """

class MethodBinaryExpression(SimpleBinaryExpression):
    """"""

    @property
    def CanReduce(self) -> bool:
        """

        :return:
        """
    @property
    def Conversion(self) -> LambdaExpression:
        """

        :return:
        """
    @property
    def IsLifted(self) -> bool:
        """

        :return:
        """
    @property
    def IsLiftedToNull(self) -> bool:
        """

        :return:
        """
    @property
    def Left(self) -> Expression:
        """

        :return:
        """
    @property
    def Method(self) -> MethodInfo:
        """

        :return:
        """
    @property
    def NodeType(self) -> ExpressionType:
        """

        :return:
        """
    @property
    def Right(self) -> Expression:
        """

        :return:
        """
    @property
    def Type(self) -> Type:
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
    def Reduce(self) -> Expression:
        """

        :return:
        """
    def ReduceAndCheck(self) -> Expression:
        """

        :return:
        """
    def ReduceExtensions(self) -> Expression:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Update(
        self, left: Expression, conversion: LambdaExpression, right: Expression
    ) -> BinaryExpression:
        """

        :param left:
        :param conversion:
        :param right:
        :return:
        """

class MethodCallExpression(Expression, IArgumentProvider):
    """"""

    @property
    def ArgumentCount(self) -> int:
        """

        :return:
        """
    @property
    def Arguments(self) -> ReadOnlyCollection[Expression]:
        """

        :return:
        """
    @property
    def CanReduce(self) -> bool:
        """

        :return:
        """
    @property
    def Method(self) -> MethodInfo:
        """

        :return:
        """
    @property
    def NodeType(self) -> ExpressionType:
        """

        :return:
        """
    @property
    def Object(self) -> Expression:
        """

        :return:
        """
    @property
    def Type(self) -> Type:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetArgument(self, index: int) -> Expression:
        """

        :param index:
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
    def Reduce(self) -> Expression:
        """

        :return:
        """
    def ReduceAndCheck(self) -> Expression:
        """

        :return:
        """
    def ReduceExtensions(self) -> Expression:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Update(
        self, object: Expression, arguments: IEnumerable[Expression]
    ) -> MethodCallExpression:
        """

        :param object:
        :param arguments:
        :return:
        """

class MethodCallExpression1(MethodCallExpression, IArgumentProvider):
    """"""

    def __init__(self, method: MethodInfo, arg0: Expression):
        """

        :param method:
        :param arg0:
        """
    @property
    def ArgumentCount(self) -> int:
        """

        :return:
        """
    @property
    def Arguments(self) -> ReadOnlyCollection[Expression]:
        """

        :return:
        """
    @property
    def CanReduce(self) -> bool:
        """

        :return:
        """
    @property
    def Method(self) -> MethodInfo:
        """

        :return:
        """
    @property
    def NodeType(self) -> ExpressionType:
        """

        :return:
        """
    @property
    def Object(self) -> Expression:
        """

        :return:
        """
    @property
    def Type(self) -> Type:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetArgument(self, index: int) -> Expression:
        """

        :param index:
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
    def Reduce(self) -> Expression:
        """

        :return:
        """
    def ReduceAndCheck(self) -> Expression:
        """

        :return:
        """
    def ReduceExtensions(self) -> Expression:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Update(
        self, object: Expression, arguments: IEnumerable[Expression]
    ) -> MethodCallExpression:
        """

        :param object:
        :param arguments:
        :return:
        """

class MethodCallExpression2(MethodCallExpression, IArgumentProvider):
    """"""

    def __init__(self, method: MethodInfo, arg0: Expression, arg1: Expression):
        """

        :param method:
        :param arg0:
        :param arg1:
        """
    @property
    def ArgumentCount(self) -> int:
        """

        :return:
        """
    @property
    def Arguments(self) -> ReadOnlyCollection[Expression]:
        """

        :return:
        """
    @property
    def CanReduce(self) -> bool:
        """

        :return:
        """
    @property
    def Method(self) -> MethodInfo:
        """

        :return:
        """
    @property
    def NodeType(self) -> ExpressionType:
        """

        :return:
        """
    @property
    def Object(self) -> Expression:
        """

        :return:
        """
    @property
    def Type(self) -> Type:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetArgument(self, index: int) -> Expression:
        """

        :param index:
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
    def Reduce(self) -> Expression:
        """

        :return:
        """
    def ReduceAndCheck(self) -> Expression:
        """

        :return:
        """
    def ReduceExtensions(self) -> Expression:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Update(
        self, object: Expression, arguments: IEnumerable[Expression]
    ) -> MethodCallExpression:
        """

        :param object:
        :param arguments:
        :return:
        """

class MethodCallExpression3(MethodCallExpression, IArgumentProvider):
    """"""

    def __init__(self, method: MethodInfo, arg0: Expression, arg1: Expression, arg2: Expression):
        """

        :param method:
        :param arg0:
        :param arg1:
        :param arg2:
        """
    @property
    def ArgumentCount(self) -> int:
        """

        :return:
        """
    @property
    def Arguments(self) -> ReadOnlyCollection[Expression]:
        """

        :return:
        """
    @property
    def CanReduce(self) -> bool:
        """

        :return:
        """
    @property
    def Method(self) -> MethodInfo:
        """

        :return:
        """
    @property
    def NodeType(self) -> ExpressionType:
        """

        :return:
        """
    @property
    def Object(self) -> Expression:
        """

        :return:
        """
    @property
    def Type(self) -> Type:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetArgument(self, index: int) -> Expression:
        """

        :param index:
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
    def Reduce(self) -> Expression:
        """

        :return:
        """
    def ReduceAndCheck(self) -> Expression:
        """

        :return:
        """
    def ReduceExtensions(self) -> Expression:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Update(
        self, object: Expression, arguments: IEnumerable[Expression]
    ) -> MethodCallExpression:
        """

        :param object:
        :param arguments:
        :return:
        """

class MethodCallExpression4(MethodCallExpression, IArgumentProvider):
    """"""

    def __init__(
        self,
        method: MethodInfo,
        arg0: Expression,
        arg1: Expression,
        arg2: Expression,
        arg3: Expression,
    ):
        """

        :param method:
        :param arg0:
        :param arg1:
        :param arg2:
        :param arg3:
        """
    @property
    def ArgumentCount(self) -> int:
        """

        :return:
        """
    @property
    def Arguments(self) -> ReadOnlyCollection[Expression]:
        """

        :return:
        """
    @property
    def CanReduce(self) -> bool:
        """

        :return:
        """
    @property
    def Method(self) -> MethodInfo:
        """

        :return:
        """
    @property
    def NodeType(self) -> ExpressionType:
        """

        :return:
        """
    @property
    def Object(self) -> Expression:
        """

        :return:
        """
    @property
    def Type(self) -> Type:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetArgument(self, index: int) -> Expression:
        """

        :param index:
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
    def Reduce(self) -> Expression:
        """

        :return:
        """
    def ReduceAndCheck(self) -> Expression:
        """

        :return:
        """
    def ReduceExtensions(self) -> Expression:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Update(
        self, object: Expression, arguments: IEnumerable[Expression]
    ) -> MethodCallExpression:
        """

        :param object:
        :param arguments:
        :return:
        """

class MethodCallExpression5(MethodCallExpression, IArgumentProvider):
    """"""

    def __init__(
        self,
        method: MethodInfo,
        arg0: Expression,
        arg1: Expression,
        arg2: Expression,
        arg3: Expression,
        arg4: Expression,
    ):
        """

        :param method:
        :param arg0:
        :param arg1:
        :param arg2:
        :param arg3:
        :param arg4:
        """
    @property
    def ArgumentCount(self) -> int:
        """

        :return:
        """
    @property
    def Arguments(self) -> ReadOnlyCollection[Expression]:
        """

        :return:
        """
    @property
    def CanReduce(self) -> bool:
        """

        :return:
        """
    @property
    def Method(self) -> MethodInfo:
        """

        :return:
        """
    @property
    def NodeType(self) -> ExpressionType:
        """

        :return:
        """
    @property
    def Object(self) -> Expression:
        """

        :return:
        """
    @property
    def Type(self) -> Type:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetArgument(self, index: int) -> Expression:
        """

        :param index:
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
    def Reduce(self) -> Expression:
        """

        :return:
        """
    def ReduceAndCheck(self) -> Expression:
        """

        :return:
        """
    def ReduceExtensions(self) -> Expression:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Update(
        self, object: Expression, arguments: IEnumerable[Expression]
    ) -> MethodCallExpression:
        """

        :param object:
        :param arguments:
        :return:
        """

class MethodCallExpressionN(MethodCallExpression, IArgumentProvider):
    """"""

    def __init__(self, method: MethodInfo, args: IList[Expression]):
        """

        :param method:
        :param args:
        """
    @property
    def ArgumentCount(self) -> int:
        """

        :return:
        """
    @property
    def Arguments(self) -> ReadOnlyCollection[Expression]:
        """

        :return:
        """
    @property
    def CanReduce(self) -> bool:
        """

        :return:
        """
    @property
    def Method(self) -> MethodInfo:
        """

        :return:
        """
    @property
    def NodeType(self) -> ExpressionType:
        """

        :return:
        """
    @property
    def Object(self) -> Expression:
        """

        :return:
        """
    @property
    def Type(self) -> Type:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetArgument(self, index: int) -> Expression:
        """

        :param index:
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
    def Reduce(self) -> Expression:
        """

        :return:
        """
    def ReduceAndCheck(self) -> Expression:
        """

        :return:
        """
    def ReduceExtensions(self) -> Expression:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Update(
        self, object: Expression, arguments: IEnumerable[Expression]
    ) -> MethodCallExpression:
        """

        :param object:
        :param arguments:
        :return:
        """

class NewArrayBoundsExpression(NewArrayExpression):
    """"""

    @property
    def CanReduce(self) -> bool:
        """

        :return:
        """
    @property
    def Expressions(self) -> ReadOnlyCollection[Expression]:
        """

        :return:
        """
    @property
    def NodeType(self) -> ExpressionType:
        """

        :return:
        """
    @property
    def Type(self) -> Type:
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
    def Reduce(self) -> Expression:
        """

        :return:
        """
    def ReduceAndCheck(self) -> Expression:
        """

        :return:
        """
    def ReduceExtensions(self) -> Expression:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Update(self, expressions: IEnumerable[Expression]) -> NewArrayExpression:
        """

        :param expressions:
        :return:
        """

class NewArrayExpression(Expression):
    """"""

    @property
    def CanReduce(self) -> bool:
        """

        :return:
        """
    @property
    def Expressions(self) -> ReadOnlyCollection[Expression]:
        """

        :return:
        """
    @property
    def NodeType(self) -> ExpressionType:
        """

        :return:
        """
    @property
    def Type(self) -> Type:
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
    def Reduce(self) -> Expression:
        """

        :return:
        """
    def ReduceAndCheck(self) -> Expression:
        """

        :return:
        """
    def ReduceExtensions(self) -> Expression:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Update(self, expressions: IEnumerable[Expression]) -> NewArrayExpression:
        """

        :param expressions:
        :return:
        """

class NewArrayInitExpression(NewArrayExpression):
    """"""

    @property
    def CanReduce(self) -> bool:
        """

        :return:
        """
    @property
    def Expressions(self) -> ReadOnlyCollection[Expression]:
        """

        :return:
        """
    @property
    def NodeType(self) -> ExpressionType:
        """

        :return:
        """
    @property
    def Type(self) -> Type:
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
    def Reduce(self) -> Expression:
        """

        :return:
        """
    def ReduceAndCheck(self) -> Expression:
        """

        :return:
        """
    def ReduceExtensions(self) -> Expression:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Update(self, expressions: IEnumerable[Expression]) -> NewArrayExpression:
        """

        :param expressions:
        :return:
        """

class NewExpression(Expression, IArgumentProvider):
    """"""

    @property
    def ArgumentCount(self) -> int:
        """

        :return:
        """
    @property
    def Arguments(self) -> ReadOnlyCollection[Expression]:
        """

        :return:
        """
    @property
    def CanReduce(self) -> bool:
        """

        :return:
        """
    @property
    def Constructor(self) -> ConstructorInfo:
        """

        :return:
        """
    @property
    def Members(self) -> ReadOnlyCollection[MemberInfo]:
        """

        :return:
        """
    @property
    def NodeType(self) -> ExpressionType:
        """

        :return:
        """
    @property
    def Type(self) -> Type:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetArgument(self, index: int) -> Expression:
        """

        :param index:
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
    def Reduce(self) -> Expression:
        """

        :return:
        """
    def ReduceAndCheck(self) -> Expression:
        """

        :return:
        """
    def ReduceExtensions(self) -> Expression:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Update(self, arguments: IEnumerable[Expression]) -> NewExpression:
        """

        :param arguments:
        :return:
        """

class NewValueTypeExpression(NewExpression, IArgumentProvider):
    """"""

    @property
    def ArgumentCount(self) -> int:
        """

        :return:
        """
    @property
    def Arguments(self) -> ReadOnlyCollection[Expression]:
        """

        :return:
        """
    @property
    def CanReduce(self) -> bool:
        """

        :return:
        """
    @property
    def Constructor(self) -> ConstructorInfo:
        """

        :return:
        """
    @property
    def Members(self) -> ReadOnlyCollection[MemberInfo]:
        """

        :return:
        """
    @property
    def NodeType(self) -> ExpressionType:
        """

        :return:
        """
    @property
    def Type(self) -> Type:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetArgument(self, index: int) -> Expression:
        """

        :param index:
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
    def Reduce(self) -> Expression:
        """

        :return:
        """
    def ReduceAndCheck(self) -> Expression:
        """

        :return:
        """
    def ReduceExtensions(self) -> Expression:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Update(self, arguments: IEnumerable[Expression]) -> NewExpression:
        """

        :param arguments:
        :return:
        """

class OldExpressionVisitor(ABC, Object):
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

class OpAssignMethodConversionBinaryExpression(MethodBinaryExpression):
    """"""

    @property
    def CanReduce(self) -> bool:
        """

        :return:
        """
    @property
    def Conversion(self) -> LambdaExpression:
        """

        :return:
        """
    @property
    def IsLifted(self) -> bool:
        """

        :return:
        """
    @property
    def IsLiftedToNull(self) -> bool:
        """

        :return:
        """
    @property
    def Left(self) -> Expression:
        """

        :return:
        """
    @property
    def Method(self) -> MethodInfo:
        """

        :return:
        """
    @property
    def NodeType(self) -> ExpressionType:
        """

        :return:
        """
    @property
    def Right(self) -> Expression:
        """

        :return:
        """
    @property
    def Type(self) -> Type:
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
    def Reduce(self) -> Expression:
        """

        :return:
        """
    def ReduceAndCheck(self) -> Expression:
        """

        :return:
        """
    def ReduceExtensions(self) -> Expression:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Update(
        self, left: Expression, conversion: LambdaExpression, right: Expression
    ) -> BinaryExpression:
        """

        :param left:
        :param conversion:
        :param right:
        :return:
        """

class ParameterExpression(Expression):
    """"""

    @property
    def CanReduce(self) -> bool:
        """

        :return:
        """
    @property
    def IsByRef(self) -> bool:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def NodeType(self) -> ExpressionType:
        """

        :return:
        """
    @property
    def Type(self) -> Type:
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
    def Reduce(self) -> Expression:
        """

        :return:
        """
    def ReduceAndCheck(self) -> Expression:
        """

        :return:
        """
    def ReduceExtensions(self) -> Expression:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class PrimitiveParameterExpression(Generic[T], ParameterExpression):
    """"""

    @property
    def CanReduce(self) -> bool:
        """

        :return:
        """
    @property
    def IsByRef(self) -> bool:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def NodeType(self) -> ExpressionType:
        """

        :return:
        """
    @property
    def Type(self) -> Type:
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
    def Reduce(self) -> Expression:
        """

        :return:
        """
    def ReduceAndCheck(self) -> Expression:
        """

        :return:
        """
    def ReduceExtensions(self) -> Expression:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class PropertyExpression(MemberExpression):
    """"""

    def __init__(self, expression: Expression, member: PropertyInfo):
        """

        :param expression:
        :param member:
        """
    @property
    def CanReduce(self) -> bool:
        """

        :return:
        """
    @property
    def Expression(self) -> Expression:
        """

        :return:
        """
    @property
    def Member(self) -> MemberInfo:
        """

        :return:
        """
    @property
    def NodeType(self) -> ExpressionType:
        """

        :return:
        """
    @property
    def Type(self) -> Type:
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
    def Reduce(self) -> Expression:
        """

        :return:
        """
    def ReduceAndCheck(self) -> Expression:
        """

        :return:
        """
    def ReduceExtensions(self) -> Expression:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Update(self, expression: Expression) -> MemberExpression:
        """

        :param expression:
        :return:
        """

class ReadOnlyCollectionExtensions(ABC, Object):
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

class RuntimeVariablesExpression(Expression):
    """"""

    @property
    def CanReduce(self) -> bool:
        """

        :return:
        """
    @property
    def NodeType(self) -> ExpressionType:
        """

        :return:
        """
    @property
    def Type(self) -> Type:
        """

        :return:
        """
    @property
    def Variables(self) -> ReadOnlyCollection[ParameterExpression]:
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
    def Reduce(self) -> Expression:
        """

        :return:
        """
    def ReduceAndCheck(self) -> Expression:
        """

        :return:
        """
    def ReduceExtensions(self) -> Expression:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Update(self, variables: IEnumerable[ParameterExpression]) -> RuntimeVariablesExpression:
        """

        :param variables:
        :return:
        """

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

class Scope1(ScopeExpression):
    """"""

    @property
    def CanReduce(self) -> bool:
        """

        :return:
        """
    @property
    def Expressions(self) -> ReadOnlyCollection[Expression]:
        """

        :return:
        """
    @property
    def NodeType(self) -> ExpressionType:
        """

        :return:
        """
    @property
    def Result(self) -> Expression:
        """

        :return:
        """
    @property
    def Type(self) -> Type:
        """

        :return:
        """
    @property
    def Variables(self) -> ReadOnlyCollection[ParameterExpression]:
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
    def Reduce(self) -> Expression:
        """

        :return:
        """
    def ReduceAndCheck(self) -> Expression:
        """

        :return:
        """
    def ReduceExtensions(self) -> Expression:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Update(
        self, variables: IEnumerable[ParameterExpression], expressions: IEnumerable[Expression]
    ) -> BlockExpression:
        """

        :param variables:
        :param expressions:
        :return:
        """

class ScopeExpression(BlockExpression):
    """"""

    @property
    def CanReduce(self) -> bool:
        """

        :return:
        """
    @property
    def Expressions(self) -> ReadOnlyCollection[Expression]:
        """

        :return:
        """
    @property
    def NodeType(self) -> ExpressionType:
        """

        :return:
        """
    @property
    def Result(self) -> Expression:
        """

        :return:
        """
    @property
    def Type(self) -> Type:
        """

        :return:
        """
    @property
    def Variables(self) -> ReadOnlyCollection[ParameterExpression]:
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
    def Reduce(self) -> Expression:
        """

        :return:
        """
    def ReduceAndCheck(self) -> Expression:
        """

        :return:
        """
    def ReduceExtensions(self) -> Expression:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Update(
        self, variables: IEnumerable[ParameterExpression], expressions: IEnumerable[Expression]
    ) -> BlockExpression:
        """

        :param variables:
        :param expressions:
        :return:
        """

class ScopeN(ScopeExpression):
    """"""

    @property
    def CanReduce(self) -> bool:
        """

        :return:
        """
    @property
    def Expressions(self) -> ReadOnlyCollection[Expression]:
        """

        :return:
        """
    @property
    def NodeType(self) -> ExpressionType:
        """

        :return:
        """
    @property
    def Result(self) -> Expression:
        """

        :return:
        """
    @property
    def Type(self) -> Type:
        """

        :return:
        """
    @property
    def Variables(self) -> ReadOnlyCollection[ParameterExpression]:
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
    def Reduce(self) -> Expression:
        """

        :return:
        """
    def ReduceAndCheck(self) -> Expression:
        """

        :return:
        """
    def ReduceExtensions(self) -> Expression:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Update(
        self, variables: IEnumerable[ParameterExpression], expressions: IEnumerable[Expression]
    ) -> BlockExpression:
        """

        :param variables:
        :param expressions:
        :return:
        """

class ScopeWithType(ScopeN):
    """"""

    @property
    def CanReduce(self) -> bool:
        """

        :return:
        """
    @property
    def Expressions(self) -> ReadOnlyCollection[Expression]:
        """

        :return:
        """
    @property
    def NodeType(self) -> ExpressionType:
        """

        :return:
        """
    @property
    def Result(self) -> Expression:
        """

        :return:
        """
    @property
    def Type(self) -> Type:
        """

        :return:
        """
    @property
    def Variables(self) -> ReadOnlyCollection[ParameterExpression]:
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
    def Reduce(self) -> Expression:
        """

        :return:
        """
    def ReduceAndCheck(self) -> Expression:
        """

        :return:
        """
    def ReduceExtensions(self) -> Expression:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Update(
        self, variables: IEnumerable[ParameterExpression], expressions: IEnumerable[Expression]
    ) -> BlockExpression:
        """

        :param variables:
        :param expressions:
        :return:
        """

class Set(Generic[T], Object, ICollection[T], IEnumerable[T], IEnumerable):
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
    def Remove(self, item: T) -> bool:
        """

        :param item:
        :return:
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

class SimpleBinaryExpression(BinaryExpression):
    """"""

    @property
    def CanReduce(self) -> bool:
        """

        :return:
        """
    @property
    def Conversion(self) -> LambdaExpression:
        """

        :return:
        """
    @property
    def IsLifted(self) -> bool:
        """

        :return:
        """
    @property
    def IsLiftedToNull(self) -> bool:
        """

        :return:
        """
    @property
    def Left(self) -> Expression:
        """

        :return:
        """
    @property
    def Method(self) -> MethodInfo:
        """

        :return:
        """
    @property
    def NodeType(self) -> ExpressionType:
        """

        :return:
        """
    @property
    def Right(self) -> Expression:
        """

        :return:
        """
    @property
    def Type(self) -> Type:
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
    def Reduce(self) -> Expression:
        """

        :return:
        """
    def ReduceAndCheck(self) -> Expression:
        """

        :return:
        """
    def ReduceExtensions(self) -> Expression:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Update(
        self, left: Expression, conversion: LambdaExpression, right: Expression
    ) -> BinaryExpression:
        """

        :param left:
        :param conversion:
        :param right:
        :return:
        """

class SpanDebugInfoExpression(DebugInfoExpression):
    """"""

    @property
    def CanReduce(self) -> bool:
        """

        :return:
        """
    @property
    def Document(self) -> SymbolDocumentInfo:
        """

        :return:
        """
    @property
    def EndColumn(self) -> int:
        """

        :return:
        """
    @property
    def EndLine(self) -> int:
        """

        :return:
        """
    @property
    def IsClear(self) -> bool:
        """

        :return:
        """
    @property
    def NodeType(self) -> ExpressionType:
        """

        :return:
        """
    @property
    def StartColumn(self) -> int:
        """

        :return:
        """
    @property
    def StartLine(self) -> int:
        """

        :return:
        """
    @property
    def Type(self) -> Type:
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
    def Reduce(self) -> Expression:
        """

        :return:
        """
    def ReduceAndCheck(self) -> Expression:
        """

        :return:
        """
    def ReduceExtensions(self) -> Expression:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class StackGuard(Object):
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
    @overload
    def RunOnEmptyStack(self, action: Action[T1, T2], arg1: T1, arg2: T2) -> None:
        """

        :param action:
        :param arg1:
        :param arg2:
        """
    @overload
    def RunOnEmptyStack(self, action: Func[T1, T2, R], arg1: T1, arg2: T2) -> R:
        """

        :param action:
        :param arg1:
        :param arg2:
        :return:
        """
    @overload
    def RunOnEmptyStack(self, action: Action[T1, T2, T3], arg1: T1, arg2: T2, arg3: T3) -> None:
        """

        :param action:
        :param arg1:
        :param arg2:
        :param arg3:
        """
    @overload
    def RunOnEmptyStack(self, action: Func[T1, T2, T3, R], arg1: T1, arg2: T2, arg3: T3) -> R:
        """

        :param action:
        :param arg1:
        :param arg2:
        :param arg3:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def TryEnterOnCurrentStack(self) -> bool:
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

class SwitchCase(Object):
    """"""

    @property
    def Body(self) -> Expression:
        """

        :return:
        """
    @property
    def TestValues(self) -> ReadOnlyCollection[Expression]:
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
    def Update(self, testValues: IEnumerable[Expression], body: Expression) -> SwitchCase:
        """

        :param testValues:
        :param body:
        :return:
        """

class SwitchExpression(Expression):
    """"""

    @property
    def CanReduce(self) -> bool:
        """

        :return:
        """
    @property
    def Cases(self) -> ReadOnlyCollection[SwitchCase]:
        """

        :return:
        """
    @property
    def Comparison(self) -> MethodInfo:
        """

        :return:
        """
    @property
    def DefaultBody(self) -> Expression:
        """

        :return:
        """
    @property
    def NodeType(self) -> ExpressionType:
        """

        :return:
        """
    @property
    def SwitchValue(self) -> Expression:
        """

        :return:
        """
    @property
    def Type(self) -> Type:
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
    def Reduce(self) -> Expression:
        """

        :return:
        """
    def ReduceAndCheck(self) -> Expression:
        """

        :return:
        """
    def ReduceExtensions(self) -> Expression:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Update(
        self, switchValue: Expression, cases: IEnumerable[SwitchCase], defaultBody: Expression
    ) -> SwitchExpression:
        """

        :param switchValue:
        :param cases:
        :param defaultBody:
        :return:
        """

class SymbolDocumentInfo(Object):
    """"""

    @property
    def DocumentType(self) -> Guid:
        """

        :return:
        """
    @property
    def FileName(self) -> str:
        """

        :return:
        """
    @property
    def Language(self) -> Guid:
        """

        :return:
        """
    @property
    def LanguageVendor(self) -> Guid:
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

class SymbolDocumentWithGuids(SymbolDocumentInfo):
    """"""

    @property
    def DocumentType(self) -> Guid:
        """

        :return:
        """
    @property
    def FileName(self) -> str:
        """

        :return:
        """
    @property
    def Language(self) -> Guid:
        """

        :return:
        """
    @property
    def LanguageVendor(self) -> Guid:
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

class TryExpression(Expression):
    """"""

    @property
    def Body(self) -> Expression:
        """

        :return:
        """
    @property
    def CanReduce(self) -> bool:
        """

        :return:
        """
    @property
    def Fault(self) -> Expression:
        """

        :return:
        """
    @property
    def Finally(self) -> Expression:
        """

        :return:
        """
    @property
    def Handlers(self) -> ReadOnlyCollection[CatchBlock]:
        """

        :return:
        """
    @property
    def NodeType(self) -> ExpressionType:
        """

        :return:
        """
    @property
    def Type(self) -> Type:
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
    def Reduce(self) -> Expression:
        """

        :return:
        """
    def ReduceAndCheck(self) -> Expression:
        """

        :return:
        """
    def ReduceExtensions(self) -> Expression:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Update(
        self,
        body: Expression,
        handlers: IEnumerable[CatchBlock],
        _finally: Expression,
        fault: Expression,
    ) -> TryExpression:
        """

        :param body:
        :param handlers:
        :param _finally:
        :param fault:
        :return:
        """

class TypeBinaryExpression(Expression):
    """"""

    @property
    def CanReduce(self) -> bool:
        """

        :return:
        """
    @property
    def Expression(self) -> Expression:
        """

        :return:
        """
    @property
    def NodeType(self) -> ExpressionType:
        """

        :return:
        """
    @property
    def Type(self) -> Type:
        """

        :return:
        """
    @property
    def TypeOperand(self) -> Type:
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
    def Reduce(self) -> Expression:
        """

        :return:
        """
    def ReduceAndCheck(self) -> Expression:
        """

        :return:
        """
    def ReduceExtensions(self) -> Expression:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Update(self, expression: Expression) -> TypeBinaryExpression:
        """

        :param expression:
        :return:
        """

class TypedConstantExpression(ConstantExpression):
    """"""

    @property
    def CanReduce(self) -> bool:
        """

        :return:
        """
    @property
    def NodeType(self) -> ExpressionType:
        """

        :return:
        """
    @property
    def Type(self) -> Type:
        """

        :return:
        """
    @property
    def Value(self) -> object:
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
    def Reduce(self) -> Expression:
        """

        :return:
        """
    def ReduceAndCheck(self) -> Expression:
        """

        :return:
        """
    def ReduceExtensions(self) -> Expression:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class TypedDynamicExpression1(DynamicExpression1, IArgumentProvider, IDynamicExpression):
    """"""

    @property
    def ArgumentCount(self) -> int:
        """

        :return:
        """
    @property
    def Arguments(self) -> ReadOnlyCollection[Expression]:
        """

        :return:
        """
    @property
    def Binder(self) -> CallSiteBinder:
        """

        :return:
        """
    @property
    def CanReduce(self) -> bool:
        """

        :return:
        """
    @property
    def DelegateType(self) -> Type:
        """

        :return:
        """
    @property
    def NodeType(self) -> ExpressionType:
        """

        :return:
        """
    @property
    def Type(self) -> Type:
        """

        :return:
        """
    def CreateCallSite(self) -> object:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetArgument(self, index: int) -> Expression:
        """

        :param index:
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
    def Reduce(self) -> Expression:
        """

        :return:
        """
    def ReduceAndCheck(self) -> Expression:
        """

        :return:
        """
    def ReduceExtensions(self) -> Expression:
        """

        :return:
        """
    def Rewrite(self, args: Array[Expression]) -> Expression:
        """

        :param args:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Update(self, arguments: IEnumerable[Expression]) -> DynamicExpression:
        """

        :param arguments:
        :return:
        """

class TypedDynamicExpression2(DynamicExpression2, IArgumentProvider, IDynamicExpression):
    """"""

    @property
    def ArgumentCount(self) -> int:
        """

        :return:
        """
    @property
    def Arguments(self) -> ReadOnlyCollection[Expression]:
        """

        :return:
        """
    @property
    def Binder(self) -> CallSiteBinder:
        """

        :return:
        """
    @property
    def CanReduce(self) -> bool:
        """

        :return:
        """
    @property
    def DelegateType(self) -> Type:
        """

        :return:
        """
    @property
    def NodeType(self) -> ExpressionType:
        """

        :return:
        """
    @property
    def Type(self) -> Type:
        """

        :return:
        """
    def CreateCallSite(self) -> object:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetArgument(self, index: int) -> Expression:
        """

        :param index:
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
    def Reduce(self) -> Expression:
        """

        :return:
        """
    def ReduceAndCheck(self) -> Expression:
        """

        :return:
        """
    def ReduceExtensions(self) -> Expression:
        """

        :return:
        """
    def Rewrite(self, args: Array[Expression]) -> Expression:
        """

        :param args:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Update(self, arguments: IEnumerable[Expression]) -> DynamicExpression:
        """

        :param arguments:
        :return:
        """

class TypedDynamicExpression3(DynamicExpression3, IArgumentProvider, IDynamicExpression):
    """"""

    @property
    def ArgumentCount(self) -> int:
        """

        :return:
        """
    @property
    def Arguments(self) -> ReadOnlyCollection[Expression]:
        """

        :return:
        """
    @property
    def Binder(self) -> CallSiteBinder:
        """

        :return:
        """
    @property
    def CanReduce(self) -> bool:
        """

        :return:
        """
    @property
    def DelegateType(self) -> Type:
        """

        :return:
        """
    @property
    def NodeType(self) -> ExpressionType:
        """

        :return:
        """
    @property
    def Type(self) -> Type:
        """

        :return:
        """
    def CreateCallSite(self) -> object:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetArgument(self, index: int) -> Expression:
        """

        :param index:
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
    def Reduce(self) -> Expression:
        """

        :return:
        """
    def ReduceAndCheck(self) -> Expression:
        """

        :return:
        """
    def ReduceExtensions(self) -> Expression:
        """

        :return:
        """
    def Rewrite(self, args: Array[Expression]) -> Expression:
        """

        :param args:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Update(self, arguments: IEnumerable[Expression]) -> DynamicExpression:
        """

        :param arguments:
        :return:
        """

class TypedDynamicExpression4(DynamicExpression4, IArgumentProvider, IDynamicExpression):
    """"""

    @property
    def ArgumentCount(self) -> int:
        """

        :return:
        """
    @property
    def Arguments(self) -> ReadOnlyCollection[Expression]:
        """

        :return:
        """
    @property
    def Binder(self) -> CallSiteBinder:
        """

        :return:
        """
    @property
    def CanReduce(self) -> bool:
        """

        :return:
        """
    @property
    def DelegateType(self) -> Type:
        """

        :return:
        """
    @property
    def NodeType(self) -> ExpressionType:
        """

        :return:
        """
    @property
    def Type(self) -> Type:
        """

        :return:
        """
    def CreateCallSite(self) -> object:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetArgument(self, index: int) -> Expression:
        """

        :param index:
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
    def Reduce(self) -> Expression:
        """

        :return:
        """
    def ReduceAndCheck(self) -> Expression:
        """

        :return:
        """
    def ReduceExtensions(self) -> Expression:
        """

        :return:
        """
    def Rewrite(self, args: Array[Expression]) -> Expression:
        """

        :param args:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Update(self, arguments: IEnumerable[Expression]) -> DynamicExpression:
        """

        :param arguments:
        :return:
        """

class TypedDynamicExpressionN(DynamicExpressionN, IArgumentProvider, IDynamicExpression):
    """"""

    @property
    def ArgumentCount(self) -> int:
        """

        :return:
        """
    @property
    def Arguments(self) -> ReadOnlyCollection[Expression]:
        """

        :return:
        """
    @property
    def Binder(self) -> CallSiteBinder:
        """

        :return:
        """
    @property
    def CanReduce(self) -> bool:
        """

        :return:
        """
    @property
    def DelegateType(self) -> Type:
        """

        :return:
        """
    @property
    def NodeType(self) -> ExpressionType:
        """

        :return:
        """
    @property
    def Type(self) -> Type:
        """

        :return:
        """
    def CreateCallSite(self) -> object:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetArgument(self, index: int) -> Expression:
        """

        :param index:
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
    def Reduce(self) -> Expression:
        """

        :return:
        """
    def ReduceAndCheck(self) -> Expression:
        """

        :return:
        """
    def ReduceExtensions(self) -> Expression:
        """

        :return:
        """
    def Rewrite(self, args: Array[Expression]) -> Expression:
        """

        :param args:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Update(self, arguments: IEnumerable[Expression]) -> DynamicExpression:
        """

        :param arguments:
        :return:
        """

class TypedParameterExpression(ParameterExpression):
    """"""

    @property
    def CanReduce(self) -> bool:
        """

        :return:
        """
    @property
    def IsByRef(self) -> bool:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def NodeType(self) -> ExpressionType:
        """

        :return:
        """
    @property
    def Type(self) -> Type:
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
    def Reduce(self) -> Expression:
        """

        :return:
        """
    def ReduceAndCheck(self) -> Expression:
        """

        :return:
        """
    def ReduceExtensions(self) -> Expression:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class UnaryExpression(Expression):
    """"""

    @property
    def CanReduce(self) -> bool:
        """

        :return:
        """
    @property
    def IsLifted(self) -> bool:
        """

        :return:
        """
    @property
    def IsLiftedToNull(self) -> bool:
        """

        :return:
        """
    @property
    def Method(self) -> MethodInfo:
        """

        :return:
        """
    @property
    def NodeType(self) -> ExpressionType:
        """

        :return:
        """
    @property
    def Operand(self) -> Expression:
        """

        :return:
        """
    @property
    def Type(self) -> Type:
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
    def Reduce(self) -> Expression:
        """

        :return:
        """
    def ReduceAndCheck(self) -> Expression:
        """

        :return:
        """
    def ReduceExtensions(self) -> Expression:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Update(self, operand: Expression) -> UnaryExpression:
        """

        :param operand:
        :return:
        """
