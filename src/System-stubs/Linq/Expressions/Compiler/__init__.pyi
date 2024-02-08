from __future__ import annotations

from abc import ABC
from typing import Generic
from typing import TypeVar
from typing import overload

from System import Enum
from System import Object
from System import Type
from System.Collections.Generic import IEnumerable
from System.Collections.ObjectModel import ReadOnlyCollection
from System.Linq.Expressions import BlockExpression
from System.Linq.Expressions import BlockN
from System.Linq.Expressions import Expression
from System.Linq.Expressions import ExpressionType
from System.Linq.Expressions import ExpressionVisitor
from System.Linq.Expressions import ParameterExpression

K = TypeVar("K")
T = TypeVar("T")
V = TypeVar("V")

class AnalyzedTree(Object):
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

class AssemblyGen(Object):
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

class BoundConstants(Object):
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

class CompilerScope(Object):
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

class DelegateHelpers(ABC, Object):
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

class HoistedLocals(Object):
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

class ILGen(ABC, Object):
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

class KeyedQueue(Generic[K, V], Object):
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

class LabelInfo(Object):
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

class LabelScopeInfo(Object):
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

class LabelScopeKind(Enum):
    """"""

    Statement: LabelScopeKind = ...
    """"""
    Block: LabelScopeKind = ...
    """"""
    Switch: LabelScopeKind = ...
    """"""
    Lambda: LabelScopeKind = ...
    """"""
    Try: LabelScopeKind = ...
    """"""
    Catch: LabelScopeKind = ...
    """"""
    Finally: LabelScopeKind = ...
    """"""
    Filter: LabelScopeKind = ...
    """"""
    Expression: LabelScopeKind = ...
    """"""

class LambdaCompiler(Object):
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

class SpilledExpressionBlock(BlockN):
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

class StackSpiller(Object):
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

class SymbolGuids(ABC, Object):
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

class VariableBinder(ExpressionVisitor):
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

class VariableStorageKind(Enum):
    """"""

    Local: VariableStorageKind = ...
    """"""
    Hoisted: VariableStorageKind = ...
    """"""
