"""Automatically generated stubs for C# namespace: System.Linq.Expressions.Compiler."""

from abc import ABC
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

class AnalyzedTree(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class AssemblyGen(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class BoundConstants(Object):
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

class CompilerScope(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class DelegateHelpers(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class HoistedLocals(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ILGen(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class KeyedQueue[K, V](Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class LabelInfo(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class LabelScopeInfo(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

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
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SpilledExpressionBlock(BlockN):
    """"""
    @property
    def CanReduce(self) -> bool:
        """"""
    @property
    def Expressions(self) -> ReadOnlyCollection[Expression]:
        """"""
    @property
    def NodeType(self) -> ExpressionType:
        """"""
    @property
    def Result(self) -> Expression:
        """"""
    @property
    def Type(self) -> Type:
        """"""
    @property
    def Variables(self) -> ReadOnlyCollection[ParameterExpression]:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Reduce(self) -> Expression:
        """"""
    def ReduceAndCheck(self) -> Expression:
        """"""
    def ReduceExtensions(self) -> Expression:
        """"""
    def ToString(self) -> str:
        """"""
    def Update(
        self, variables: IEnumerable[ParameterExpression], expressions: IEnumerable[Expression]
    ) -> BlockExpression:
        """"""

class StackSpiller(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SymbolGuids(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class VariableBinder(ExpressionVisitor):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def Visit(self, nodes: ReadOnlyCollection[Expression]) -> ReadOnlyCollection[Expression]:
        """"""
    @overload
    def Visit(self, node: Expression) -> Expression:
        """"""
    @overload
    def VisitAndConvert[T, T](self, node: T, callerName: str) -> T:
        """"""
    @overload
    def VisitAndConvert(
        self, nodes: ReadOnlyCollection[T], callerName: str
    ) -> ReadOnlyCollection[T]:
        """"""

class VariableStorageKind(Enum):
    """"""

    Local: VariableStorageKind = ...
    """"""
    Hoisted: VariableStorageKind = ...
    """"""
