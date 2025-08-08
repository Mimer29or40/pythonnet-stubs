"""Automatically generated stubs for C# namespace: System.Linq.Expressions."""

from abc import ABC
from collections.abc import Iterator
from typing import overload

from System import Action
from System import Array
from System import Boolean
from System import Delegate
from System import Enum
from System import Func
from System import Guid
from System import IntPtr
from System import Object
from System import Type
from System import UInt32
from System.Collections import IEnumerable
from System.Collections.Generic import ICollection
from System.Collections.Generic import IEnumerable
from System.Collections.Generic import IEnumerator
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
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class AssignBinaryExpression(BinaryExpression):
    """"""
    @property
    def CanReduce(self) -> bool:
        """"""
    @property
    def Conversion(self) -> LambdaExpression:
        """"""
    @property
    def IsLifted(self) -> bool:
        """"""
    @property
    def IsLiftedToNull(self) -> bool:
        """"""
    @property
    def Left(self) -> Expression:
        """"""
    @property
    def Method(self) -> MethodInfo:
        """"""
    @property
    def NodeType(self) -> ExpressionType:
        """"""
    @property
    def Right(self) -> Expression:
        """"""
    @property
    def Type(self) -> Type:
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
        self, left: Expression, conversion: LambdaExpression, right: Expression
    ) -> BinaryExpression:
        """"""

class BinaryExpression(Expression):
    """"""
    @property
    def CanReduce(self) -> bool:
        """"""
    @property
    def Conversion(self) -> LambdaExpression:
        """"""
    @property
    def IsLifted(self) -> bool:
        """"""
    @property
    def IsLiftedToNull(self) -> bool:
        """"""
    @property
    def Left(self) -> Expression:
        """"""
    @property
    def Method(self) -> MethodInfo:
        """"""
    @property
    def NodeType(self) -> ExpressionType:
        """"""
    @property
    def Right(self) -> Expression:
        """"""
    @property
    def Type(self) -> Type:
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
        self, left: Expression, conversion: LambdaExpression, right: Expression
    ) -> BinaryExpression:
        """"""

class Block2(BlockExpression):
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

class Block3(BlockExpression):
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

class Block4(BlockExpression):
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

class Block5(BlockExpression):
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

class BlockExpression(Expression):
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

class BlockExpressionList(
    Object, ICollection[Expression], IEnumerable[Expression], IList[Expression], IEnumerable
):
    """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def Item(self) -> Expression:
        """"""
    @Item.setter
    def Item(self, value: Expression) -> None: ...
    def Add(self, item: Expression) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    def Contains(self, item: Expression) -> bool:
        """"""
    def CopyTo(self, array: Array[Expression], arrayIndex: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator[Expression]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def IndexOf(self, item: Expression) -> int:
        """"""
    def Insert(self, index: int, item: Expression) -> None:
        """"""
    def Remove(self, item: Expression) -> bool:
        """"""
    def RemoveAt(self, index: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def __contains__(self, item: Expression) -> bool:
        """"""
    def __iter__(self) -> Iterator[Expression]:
        """"""
    def __delitem__(self, item: Expression) -> bool:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, index: int) -> Expression:
        """"""
    def __setitem__(self, index: int, value: Expression) -> None:
        """"""

class BlockN(BlockExpression):
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

class ByRefParameterExpression(TypedParameterExpression):
    """"""
    @property
    def CanReduce(self) -> bool:
        """"""
    @property
    def IsByRef(self) -> bool:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def NodeType(self) -> ExpressionType:
        """"""
    @property
    def Type(self) -> Type:
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

class CatchBlock(Object):
    """"""
    @property
    def Body(self) -> Expression:
        """"""
    @property
    def Filter(self) -> Expression:
        """"""
    @property
    def Test(self) -> Type:
        """"""
    @property
    def Variable(self) -> ParameterExpression:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def Update(
        self, variable: ParameterExpression, filter: Expression, body: Expression
    ) -> CatchBlock:
        """"""

class ClearDebugInfoExpression(DebugInfoExpression):
    """"""
    @property
    def CanReduce(self) -> bool:
        """"""
    @property
    def Document(self) -> SymbolDocumentInfo:
        """"""
    @property
    def EndColumn(self) -> int:
        """"""
    @property
    def EndLine(self) -> int:
        """"""
    @property
    def IsClear(self) -> bool:
        """"""
    @property
    def NodeType(self) -> ExpressionType:
        """"""
    @property
    def StartColumn(self) -> int:
        """"""
    @property
    def StartLine(self) -> int:
        """"""
    @property
    def Type(self) -> Type:
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

class CoalesceConversionBinaryExpression(BinaryExpression):
    """"""
    @property
    def CanReduce(self) -> bool:
        """"""
    @property
    def Conversion(self) -> LambdaExpression:
        """"""
    @property
    def IsLifted(self) -> bool:
        """"""
    @property
    def IsLiftedToNull(self) -> bool:
        """"""
    @property
    def Left(self) -> Expression:
        """"""
    @property
    def Method(self) -> MethodInfo:
        """"""
    @property
    def NodeType(self) -> ExpressionType:
        """"""
    @property
    def Right(self) -> Expression:
        """"""
    @property
    def Type(self) -> Type:
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
        self, left: Expression, conversion: LambdaExpression, right: Expression
    ) -> BinaryExpression:
        """"""

class ConditionalExpression(Expression):
    """"""
    @property
    def CanReduce(self) -> bool:
        """"""
    @property
    def IfFalse(self) -> Expression:
        """"""
    @property
    def IfTrue(self) -> Expression:
        """"""
    @property
    def NodeType(self) -> ExpressionType:
        """"""
    @property
    def Test(self) -> Expression:
        """"""
    @property
    def Type(self) -> Type:
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
        self, test: Expression, ifTrue: Expression, ifFalse: Expression
    ) -> ConditionalExpression:
        """"""

class ConstantCheck(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ConstantExpression(Expression):
    """"""
    @property
    def CanReduce(self) -> bool:
        """"""
    @property
    def NodeType(self) -> ExpressionType:
        """"""
    @property
    def Type(self) -> Type:
        """"""
    @property
    def Value(self) -> object:
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

class DebugInfoExpression(Expression):
    """"""
    @property
    def CanReduce(self) -> bool:
        """"""
    @property
    def Document(self) -> SymbolDocumentInfo:
        """"""
    @property
    def EndColumn(self) -> int:
        """"""
    @property
    def EndLine(self) -> int:
        """"""
    @property
    def IsClear(self) -> bool:
        """"""
    @property
    def NodeType(self) -> ExpressionType:
        """"""
    @property
    def StartColumn(self) -> int:
        """"""
    @property
    def StartLine(self) -> int:
        """"""
    @property
    def Type(self) -> Type:
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

class DebugViewWriter(ExpressionVisitor):
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
    def VisitAndConvert[T](self, node: T, callerName: str) -> T:
        """"""
    @overload
    def VisitAndConvert[T](
        self, nodes: ReadOnlyCollection[T], callerName: str
    ) -> ReadOnlyCollection[T]:
        """"""

class DefaultExpression(Expression):
    """"""
    @property
    def CanReduce(self) -> bool:
        """"""
    @property
    def NodeType(self) -> ExpressionType:
        """"""
    @property
    def Type(self) -> Type:
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

class DynamicExpression(Expression, IArgumentProvider, IDynamicExpression):
    """"""
    @property
    def ArgumentCount(self) -> int:
        """"""
    @property
    def Arguments(self) -> ReadOnlyCollection[Expression]:
        """"""
    @property
    def Binder(self) -> CallSiteBinder:
        """"""
    @property
    def CanReduce(self) -> bool:
        """"""
    @property
    def DelegateType(self) -> Type:
        """"""
    @property
    def NodeType(self) -> ExpressionType:
        """"""
    @property
    def Type(self) -> Type:
        """"""
    def CreateCallSite(self) -> object:
        """"""
    @classmethod
    @overload
    def Dynamic(
        cls, binder: CallSiteBinder, returnType: Type, arguments: IEnumerable[Expression]
    ) -> DynamicExpression:
        """"""
    @classmethod
    @overload
    def Dynamic(
        cls, binder: CallSiteBinder, returnType: Type, arg0: Expression
    ) -> DynamicExpression:
        """"""
    @classmethod
    @overload
    def Dynamic(
        cls, binder: CallSiteBinder, returnType: Type, arg0: Expression, arg1: Expression
    ) -> DynamicExpression:
        """"""
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
        """"""
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
        """"""
    @classmethod
    @overload
    def Dynamic(
        cls, binder: CallSiteBinder, returnType: Type, arguments: Array[Expression]
    ) -> DynamicExpression:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetArgument(self, index: int) -> Expression:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    @overload
    def MakeDynamic(
        cls, delegateType: Type, binder: CallSiteBinder, arguments: IEnumerable[Expression]
    ) -> DynamicExpression:
        """"""
    @classmethod
    @overload
    def MakeDynamic(
        cls, delegateType: Type, binder: CallSiteBinder, arg0: Expression
    ) -> DynamicExpression:
        """"""
    @classmethod
    @overload
    def MakeDynamic(
        cls, delegateType: Type, binder: CallSiteBinder, arg0: Expression, arg1: Expression
    ) -> DynamicExpression:
        """"""
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
        """"""
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
        """"""
    @classmethod
    @overload
    def MakeDynamic(
        cls, delegateType: Type, binder: CallSiteBinder, arguments: Array[Expression]
    ) -> DynamicExpression:
        """"""
    def Reduce(self) -> Expression:
        """"""
    def ReduceAndCheck(self) -> Expression:
        """"""
    def ReduceExtensions(self) -> Expression:
        """"""
    def Rewrite(self, args: Array[Expression]) -> Expression:
        """"""
    def ToString(self) -> str:
        """"""
    def Update(self, arguments: IEnumerable[Expression]) -> DynamicExpression:
        """"""

class DynamicExpression1(DynamicExpression, IArgumentProvider, IDynamicExpression):
    """"""
    @property
    def ArgumentCount(self) -> int:
        """"""
    @property
    def Arguments(self) -> ReadOnlyCollection[Expression]:
        """"""
    @property
    def Binder(self) -> CallSiteBinder:
        """"""
    @property
    def CanReduce(self) -> bool:
        """"""
    @property
    def DelegateType(self) -> Type:
        """"""
    @property
    def NodeType(self) -> ExpressionType:
        """"""
    @property
    def Type(self) -> Type:
        """"""
    def CreateCallSite(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetArgument(self, index: int) -> Expression:
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
    def Rewrite(self, args: Array[Expression]) -> Expression:
        """"""
    def ToString(self) -> str:
        """"""
    def Update(self, arguments: IEnumerable[Expression]) -> DynamicExpression:
        """"""

class DynamicExpression2(DynamicExpression, IArgumentProvider, IDynamicExpression):
    """"""
    @property
    def ArgumentCount(self) -> int:
        """"""
    @property
    def Arguments(self) -> ReadOnlyCollection[Expression]:
        """"""
    @property
    def Binder(self) -> CallSiteBinder:
        """"""
    @property
    def CanReduce(self) -> bool:
        """"""
    @property
    def DelegateType(self) -> Type:
        """"""
    @property
    def NodeType(self) -> ExpressionType:
        """"""
    @property
    def Type(self) -> Type:
        """"""
    def CreateCallSite(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetArgument(self, index: int) -> Expression:
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
    def Rewrite(self, args: Array[Expression]) -> Expression:
        """"""
    def ToString(self) -> str:
        """"""
    def Update(self, arguments: IEnumerable[Expression]) -> DynamicExpression:
        """"""

class DynamicExpression3(DynamicExpression, IArgumentProvider, IDynamicExpression):
    """"""
    @property
    def ArgumentCount(self) -> int:
        """"""
    @property
    def Arguments(self) -> ReadOnlyCollection[Expression]:
        """"""
    @property
    def Binder(self) -> CallSiteBinder:
        """"""
    @property
    def CanReduce(self) -> bool:
        """"""
    @property
    def DelegateType(self) -> Type:
        """"""
    @property
    def NodeType(self) -> ExpressionType:
        """"""
    @property
    def Type(self) -> Type:
        """"""
    def CreateCallSite(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetArgument(self, index: int) -> Expression:
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
    def Rewrite(self, args: Array[Expression]) -> Expression:
        """"""
    def ToString(self) -> str:
        """"""
    def Update(self, arguments: IEnumerable[Expression]) -> DynamicExpression:
        """"""

class DynamicExpression4(DynamicExpression, IArgumentProvider, IDynamicExpression):
    """"""
    @property
    def ArgumentCount(self) -> int:
        """"""
    @property
    def Arguments(self) -> ReadOnlyCollection[Expression]:
        """"""
    @property
    def Binder(self) -> CallSiteBinder:
        """"""
    @property
    def CanReduce(self) -> bool:
        """"""
    @property
    def DelegateType(self) -> Type:
        """"""
    @property
    def NodeType(self) -> ExpressionType:
        """"""
    @property
    def Type(self) -> Type:
        """"""
    def CreateCallSite(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetArgument(self, index: int) -> Expression:
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
    def Rewrite(self, args: Array[Expression]) -> Expression:
        """"""
    def ToString(self) -> str:
        """"""
    def Update(self, arguments: IEnumerable[Expression]) -> DynamicExpression:
        """"""

class DynamicExpressionN(DynamicExpression, IArgumentProvider, IDynamicExpression):
    """"""
    @property
    def ArgumentCount(self) -> int:
        """"""
    @property
    def Arguments(self) -> ReadOnlyCollection[Expression]:
        """"""
    @property
    def Binder(self) -> CallSiteBinder:
        """"""
    @property
    def CanReduce(self) -> bool:
        """"""
    @property
    def DelegateType(self) -> Type:
        """"""
    @property
    def NodeType(self) -> ExpressionType:
        """"""
    @property
    def Type(self) -> Type:
        """"""
    def CreateCallSite(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetArgument(self, index: int) -> Expression:
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
    def Rewrite(self, args: Array[Expression]) -> Expression:
        """"""
    def ToString(self) -> str:
        """"""
    def Update(self, arguments: IEnumerable[Expression]) -> DynamicExpression:
        """"""

class DynamicExpressionVisitor(ABC, ExpressionVisitor):
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
    def VisitAndConvert[T](self, node: T, callerName: str) -> T:
        """"""
    @overload
    def VisitAndConvert[T](
        self, nodes: ReadOnlyCollection[T], callerName: str
    ) -> ReadOnlyCollection[T]:
        """"""

class ElementInit(Object, IArgumentProvider):
    """"""
    @property
    def AddMethod(self) -> MethodInfo:
        """"""
    @property
    def ArgumentCount(self) -> int:
        """"""
    @property
    def Arguments(self) -> ReadOnlyCollection[Expression]:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetArgument(self, index: int) -> Expression:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def Update(self, arguments: IEnumerable[Expression]) -> ElementInit:
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

class Expression(ABC, Object):
    """"""
    @property
    def CanReduce(self) -> bool:
        """"""
    @property
    def NodeType(self) -> ExpressionType:
        """"""
    @property
    def Type(self) -> Type:
        """"""
    @classmethod
    @overload
    def Add(cls, left: Expression, right: Expression) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def Add(cls, left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def AddAssign(cls, left: Expression, right: Expression) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def AddAssign(cls, left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def AddAssign(
        cls, left: Expression, right: Expression, method: MethodInfo, conversion: LambdaExpression
    ) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def AddAssignChecked(cls, left: Expression, right: Expression) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def AddAssignChecked(
        cls, left: Expression, right: Expression, method: MethodInfo
    ) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def AddAssignChecked(
        cls, left: Expression, right: Expression, method: MethodInfo, conversion: LambdaExpression
    ) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def AddChecked(cls, left: Expression, right: Expression) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def AddChecked(
        cls, left: Expression, right: Expression, method: MethodInfo
    ) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def And(cls, left: Expression, right: Expression) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def And(cls, left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def AndAlso(cls, left: Expression, right: Expression) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def AndAlso(cls, left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def AndAssign(cls, left: Expression, right: Expression) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def AndAssign(cls, left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def AndAssign(
        cls, left: Expression, right: Expression, method: MethodInfo, conversion: LambdaExpression
    ) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def ArrayAccess(cls, array: Expression, indexes: IEnumerable[Expression]) -> IndexExpression:
        """"""
    @classmethod
    @overload
    def ArrayAccess(cls, array: Expression, indexes: Array[Expression]) -> IndexExpression:
        """"""
    @classmethod
    @overload
    def ArrayIndex(
        cls, array: Expression, indexes: IEnumerable[Expression]
    ) -> MethodCallExpression:
        """"""
    @classmethod
    @overload
    def ArrayIndex(cls, array: Expression, index: Expression) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def ArrayIndex(cls, array: Expression, indexes: Array[Expression]) -> MethodCallExpression:
        """"""
    @classmethod
    def ArrayLength(cls, array: Expression) -> UnaryExpression:
        """"""
    @classmethod
    def Assign(cls, left: Expression, right: Expression) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def Bind(cls, member: MemberInfo, expression: Expression) -> MemberAssignment:
        """"""
    @classmethod
    @overload
    def Bind(cls, propertyAccessor: MethodInfo, expression: Expression) -> MemberAssignment:
        """"""
    @classmethod
    @overload
    def Block(cls, expressions: IEnumerable[Expression]) -> BlockExpression:
        """"""
    @classmethod
    @overload
    def Block(
        cls, variables: IEnumerable[ParameterExpression], expressions: IEnumerable[Expression]
    ) -> BlockExpression:
        """"""
    @classmethod
    @overload
    def Block(
        cls, variables: IEnumerable[ParameterExpression], expressions: Array[Expression]
    ) -> BlockExpression:
        """"""
    @classmethod
    @overload
    def Block(cls, arg0: Expression, arg1: Expression) -> BlockExpression:
        """"""
    @classmethod
    @overload
    def Block(cls, arg0: Expression, arg1: Expression, arg2: Expression) -> BlockExpression:
        """"""
    @classmethod
    @overload
    def Block(
        cls, arg0: Expression, arg1: Expression, arg2: Expression, arg3: Expression
    ) -> BlockExpression:
        """"""
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
        """"""
    @classmethod
    @overload
    def Block(cls, expressions: Array[Expression]) -> BlockExpression:
        """"""
    @classmethod
    @overload
    def Block(cls, type: Type, expressions: IEnumerable[Expression]) -> BlockExpression:
        """"""
    @classmethod
    @overload
    def Block(
        cls,
        type: Type,
        variables: IEnumerable[ParameterExpression],
        expressions: IEnumerable[Expression],
    ) -> BlockExpression:
        """"""
    @classmethod
    @overload
    def Block(
        cls, type: Type, variables: IEnumerable[ParameterExpression], expressions: Array[Expression]
    ) -> BlockExpression:
        """"""
    @classmethod
    @overload
    def Block(cls, type: Type, expressions: Array[Expression]) -> BlockExpression:
        """"""
    @classmethod
    @overload
    def Break(cls, target: LabelTarget) -> GotoExpression:
        """"""
    @classmethod
    @overload
    def Break(cls, target: LabelTarget, value: Expression) -> GotoExpression:
        """"""
    @classmethod
    @overload
    def Break(cls, target: LabelTarget, value: Expression, type: Type) -> GotoExpression:
        """"""
    @classmethod
    @overload
    def Break(cls, target: LabelTarget, type: Type) -> GotoExpression:
        """"""
    @classmethod
    @overload
    def Call(cls, instance: Expression, method: MethodInfo) -> MethodCallExpression:
        """"""
    @classmethod
    @overload
    def Call(
        cls, instance: Expression, method: MethodInfo, arguments: IEnumerable[Expression]
    ) -> MethodCallExpression:
        """"""
    @classmethod
    @overload
    def Call(
        cls, instance: Expression, method: MethodInfo, arg0: Expression, arg1: Expression
    ) -> MethodCallExpression:
        """"""
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
        """"""
    @classmethod
    @overload
    def Call(
        cls, instance: Expression, method: MethodInfo, arguments: Array[Expression]
    ) -> MethodCallExpression:
        """"""
    @classmethod
    @overload
    def Call(
        cls,
        instance: Expression,
        methodName: str,
        typeArguments: Array[Type],
        arguments: Array[Expression],
    ) -> MethodCallExpression:
        """"""
    @classmethod
    @overload
    def Call(cls, method: MethodInfo, arguments: IEnumerable[Expression]) -> MethodCallExpression:
        """"""
    @classmethod
    @overload
    def Call(cls, method: MethodInfo, arg0: Expression) -> MethodCallExpression:
        """"""
    @classmethod
    @overload
    def Call(cls, method: MethodInfo, arg0: Expression, arg1: Expression) -> MethodCallExpression:
        """"""
    @classmethod
    @overload
    def Call(
        cls, method: MethodInfo, arg0: Expression, arg1: Expression, arg2: Expression
    ) -> MethodCallExpression:
        """"""
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
        """"""
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
        """"""
    @classmethod
    @overload
    def Call(cls, method: MethodInfo, arguments: Array[Expression]) -> MethodCallExpression:
        """"""
    @classmethod
    @overload
    def Call(
        cls, type: Type, methodName: str, typeArguments: Array[Type], arguments: Array[Expression]
    ) -> MethodCallExpression:
        """"""
    @classmethod
    @overload
    def Catch(cls, variable: ParameterExpression, body: Expression) -> CatchBlock:
        """"""
    @classmethod
    @overload
    def Catch(
        cls, variable: ParameterExpression, body: Expression, filter: Expression
    ) -> CatchBlock:
        """"""
    @classmethod
    @overload
    def Catch(cls, type: Type, body: Expression) -> CatchBlock:
        """"""
    @classmethod
    @overload
    def Catch(cls, type: Type, body: Expression, filter: Expression) -> CatchBlock:
        """"""
    @classmethod
    def ClearDebugInfo(cls, document: SymbolDocumentInfo) -> DebugInfoExpression:
        """"""
    @classmethod
    @overload
    def Coalesce(cls, left: Expression, right: Expression) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def Coalesce(
        cls, left: Expression, right: Expression, conversion: LambdaExpression
    ) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def Condition(
        cls, test: Expression, ifTrue: Expression, ifFalse: Expression
    ) -> ConditionalExpression:
        """"""
    @classmethod
    @overload
    def Condition(
        cls, test: Expression, ifTrue: Expression, ifFalse: Expression, type: Type
    ) -> ConditionalExpression:
        """"""
    @classmethod
    @overload
    def Constant(cls, value: object) -> ConstantExpression:
        """"""
    @classmethod
    @overload
    def Constant(cls, value: object, type: Type) -> ConstantExpression:
        """"""
    @classmethod
    @overload
    def Continue(cls, target: LabelTarget) -> GotoExpression:
        """"""
    @classmethod
    @overload
    def Continue(cls, target: LabelTarget, type: Type) -> GotoExpression:
        """"""
    @classmethod
    @overload
    def Convert(cls, expression: Expression, type: Type) -> UnaryExpression:
        """"""
    @classmethod
    @overload
    def Convert(cls, expression: Expression, type: Type, method: MethodInfo) -> UnaryExpression:
        """"""
    @classmethod
    @overload
    def ConvertChecked(cls, expression: Expression, type: Type) -> UnaryExpression:
        """"""
    @classmethod
    @overload
    def ConvertChecked(
        cls, expression: Expression, type: Type, method: MethodInfo
    ) -> UnaryExpression:
        """"""
    @classmethod
    def DebugInfo(
        cls,
        document: SymbolDocumentInfo,
        startLine: int,
        startColumn: int,
        endLine: int,
        endColumn: int,
    ) -> DebugInfoExpression:
        """"""
    @classmethod
    @overload
    def Decrement(cls, expression: Expression) -> UnaryExpression:
        """"""
    @classmethod
    @overload
    def Decrement(cls, expression: Expression, method: MethodInfo) -> UnaryExpression:
        """"""
    @classmethod
    def Default(cls, type: Type) -> DefaultExpression:
        """"""
    @classmethod
    @overload
    def Divide(cls, left: Expression, right: Expression) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def Divide(cls, left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def DivideAssign(cls, left: Expression, right: Expression) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def DivideAssign(
        cls, left: Expression, right: Expression, method: MethodInfo
    ) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def DivideAssign(
        cls, left: Expression, right: Expression, method: MethodInfo, conversion: LambdaExpression
    ) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def Dynamic(
        cls, binder: CallSiteBinder, returnType: Type, arguments: IEnumerable[Expression]
    ) -> DynamicExpression:
        """"""
    @classmethod
    @overload
    def Dynamic(
        cls, binder: CallSiteBinder, returnType: Type, arg0: Expression
    ) -> DynamicExpression:
        """"""
    @classmethod
    @overload
    def Dynamic(
        cls, binder: CallSiteBinder, returnType: Type, arg0: Expression, arg1: Expression
    ) -> DynamicExpression:
        """"""
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
        """"""
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
        """"""
    @classmethod
    @overload
    def Dynamic(
        cls, binder: CallSiteBinder, returnType: Type, arguments: Array[Expression]
    ) -> DynamicExpression:
        """"""
    @classmethod
    @overload
    def ElementInit(cls, addMethod: MethodInfo, arguments: IEnumerable[Expression]) -> ElementInit:
        """"""
    @classmethod
    @overload
    def ElementInit(cls, addMethod: MethodInfo, arguments: Array[Expression]) -> ElementInit:
        """"""
    @classmethod
    def Empty(cls) -> DefaultExpression:
        """"""
    @classmethod
    @overload
    def Equal(cls, left: Expression, right: Expression) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def Equal(
        cls, left: Expression, right: Expression, liftToNull: bool, method: MethodInfo
    ) -> BinaryExpression:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    @overload
    def ExclusiveOr(cls, left: Expression, right: Expression) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def ExclusiveOr(
        cls, left: Expression, right: Expression, method: MethodInfo
    ) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def ExclusiveOrAssign(cls, left: Expression, right: Expression) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def ExclusiveOrAssign(
        cls, left: Expression, right: Expression, method: MethodInfo
    ) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def ExclusiveOrAssign(
        cls, left: Expression, right: Expression, method: MethodInfo, conversion: LambdaExpression
    ) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def Field(cls, expression: Expression, field: FieldInfo) -> MemberExpression:
        """"""
    @classmethod
    @overload
    def Field(cls, expression: Expression, fieldName: str) -> MemberExpression:
        """"""
    @classmethod
    @overload
    def Field(cls, expression: Expression, type: Type, fieldName: str) -> MemberExpression:
        """"""
    @classmethod
    def GetActionType(cls, typeArgs: Array[Type]) -> Type:
        """"""
    @classmethod
    def GetDelegateType(cls, typeArgs: Array[Type]) -> Type:
        """"""
    @classmethod
    def GetFuncType(cls, typeArgs: Array[Type]) -> Type:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    @overload
    def Goto(cls, target: LabelTarget) -> GotoExpression:
        """"""
    @classmethod
    @overload
    def Goto(cls, target: LabelTarget, value: Expression) -> GotoExpression:
        """"""
    @classmethod
    @overload
    def Goto(cls, target: LabelTarget, value: Expression, type: Type) -> GotoExpression:
        """"""
    @classmethod
    @overload
    def Goto(cls, target: LabelTarget, type: Type) -> GotoExpression:
        """"""
    @classmethod
    @overload
    def GreaterThan(cls, left: Expression, right: Expression) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def GreaterThan(
        cls, left: Expression, right: Expression, liftToNull: bool, method: MethodInfo
    ) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def GreaterThanOrEqual(cls, left: Expression, right: Expression) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def GreaterThanOrEqual(
        cls, left: Expression, right: Expression, liftToNull: bool, method: MethodInfo
    ) -> BinaryExpression:
        """"""
    @classmethod
    def IfThen(cls, test: Expression, ifTrue: Expression) -> ConditionalExpression:
        """"""
    @classmethod
    def IfThenElse(
        cls, test: Expression, ifTrue: Expression, ifFalse: Expression
    ) -> ConditionalExpression:
        """"""
    @classmethod
    @overload
    def Increment(cls, expression: Expression) -> UnaryExpression:
        """"""
    @classmethod
    @overload
    def Increment(cls, expression: Expression, method: MethodInfo) -> UnaryExpression:
        """"""
    @classmethod
    @overload
    def Invoke(
        cls, expression: Expression, arguments: IEnumerable[Expression]
    ) -> InvocationExpression:
        """"""
    @classmethod
    @overload
    def Invoke(cls, expression: Expression, arguments: Array[Expression]) -> InvocationExpression:
        """"""
    @classmethod
    @overload
    def IsFalse(cls, expression: Expression) -> UnaryExpression:
        """"""
    @classmethod
    @overload
    def IsFalse(cls, expression: Expression, method: MethodInfo) -> UnaryExpression:
        """"""
    @classmethod
    @overload
    def IsTrue(cls, expression: Expression) -> UnaryExpression:
        """"""
    @classmethod
    @overload
    def IsTrue(cls, expression: Expression, method: MethodInfo) -> UnaryExpression:
        """"""
    @classmethod
    @overload
    def Label(cls) -> LabelTarget:
        """"""
    @classmethod
    @overload
    def Label(cls, target: LabelTarget) -> LabelExpression:
        """"""
    @classmethod
    @overload
    def Label(cls, target: LabelTarget, defaultValue: Expression) -> LabelExpression:
        """"""
    @classmethod
    @overload
    def Label(cls, name: str) -> LabelTarget:
        """"""
    @classmethod
    @overload
    def Label(cls, type: Type) -> LabelTarget:
        """"""
    @classmethod
    @overload
    def Label(cls, type: Type, name: str) -> LabelTarget:
        """"""
    @classmethod
    @overload
    def Lambda[TDelegate](
        cls, body: Expression, parameters: IEnumerable[ParameterExpression]
    ) -> Expression[TDelegate]:
        """"""
    @classmethod
    @overload
    def Lambda[TDelegate](
        cls, body: Expression, parameters: Array[ParameterExpression]
    ) -> Expression[TDelegate]:
        """"""
    @classmethod
    @overload
    def Lambda[TDelegate](
        cls, body: Expression, tailCall: bool, parameters: IEnumerable[ParameterExpression]
    ) -> Expression[TDelegate]:
        """"""
    @classmethod
    @overload
    def Lambda[TDelegate](
        cls, body: Expression, tailCall: bool, parameters: Array[ParameterExpression]
    ) -> Expression[TDelegate]:
        """"""
    @classmethod
    @overload
    def Lambda[TDelegate](
        cls, body: Expression, name: str, parameters: IEnumerable[ParameterExpression]
    ) -> Expression[TDelegate]:
        """"""
    @classmethod
    @overload
    def Lambda(
        cls,
        body: Expression,
        name: str,
        tailCall: bool,
        parameters: IEnumerable[ParameterExpression],
    ) -> LambdaExpression:
        """"""
    @classmethod
    @overload
    def Lambda(
        cls, delegateType: Type, body: Expression, parameters: IEnumerable[ParameterExpression]
    ) -> LambdaExpression:
        """"""
    @classmethod
    @overload
    def Lambda(
        cls, delegateType: Type, body: Expression, parameters: Array[ParameterExpression]
    ) -> LambdaExpression:
        """"""
    @classmethod
    @overload
    def Lambda(
        cls,
        delegateType: Type,
        body: Expression,
        tailCall: bool,
        parameters: IEnumerable[ParameterExpression],
    ) -> LambdaExpression:
        """"""
    @classmethod
    @overload
    def Lambda(
        cls,
        delegateType: Type,
        body: Expression,
        tailCall: bool,
        parameters: Array[ParameterExpression],
    ) -> LambdaExpression:
        """"""
    @classmethod
    @overload
    def Lambda(
        cls,
        delegateType: Type,
        body: Expression,
        name: str,
        parameters: IEnumerable[ParameterExpression],
    ) -> LambdaExpression:
        """"""
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
        """"""
    @classmethod
    @overload
    def LeftShift(cls, left: Expression, right: Expression) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def LeftShift(cls, left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def LeftShiftAssign(cls, left: Expression, right: Expression) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def LeftShiftAssign(
        cls, left: Expression, right: Expression, method: MethodInfo
    ) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def LeftShiftAssign(
        cls, left: Expression, right: Expression, method: MethodInfo, conversion: LambdaExpression
    ) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def LessThan(cls, left: Expression, right: Expression) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def LessThan(
        cls, left: Expression, right: Expression, liftToNull: bool, method: MethodInfo
    ) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def LessThanOrEqual(cls, left: Expression, right: Expression) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def LessThanOrEqual(
        cls, left: Expression, right: Expression, liftToNull: bool, method: MethodInfo
    ) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def ListBind(
        cls, member: MemberInfo, initializers: IEnumerable[ElementInit]
    ) -> MemberListBinding:
        """"""
    @classmethod
    @overload
    def ListBind(cls, member: MemberInfo, initializers: Array[ElementInit]) -> MemberListBinding:
        """"""
    @classmethod
    @overload
    def ListBind(
        cls, propertyAccessor: MethodInfo, initializers: IEnumerable[ElementInit]
    ) -> MemberListBinding:
        """"""
    @classmethod
    @overload
    def ListBind(
        cls, propertyAccessor: MethodInfo, initializers: Array[ElementInit]
    ) -> MemberListBinding:
        """"""
    @classmethod
    @overload
    def ListInit(
        cls, newExpression: NewExpression, initializers: IEnumerable[ElementInit]
    ) -> ListInitExpression:
        """"""
    @classmethod
    @overload
    def ListInit(
        cls, newExpression: NewExpression, initializers: IEnumerable[Expression]
    ) -> ListInitExpression:
        """"""
    @classmethod
    @overload
    def ListInit(
        cls,
        newExpression: NewExpression,
        addMethod: MethodInfo,
        initializers: IEnumerable[Expression],
    ) -> ListInitExpression:
        """"""
    @classmethod
    @overload
    def ListInit(
        cls, newExpression: NewExpression, addMethod: MethodInfo, initializers: Array[Expression]
    ) -> ListInitExpression:
        """"""
    @classmethod
    @overload
    def ListInit(
        cls, newExpression: NewExpression, initializers: Array[ElementInit]
    ) -> ListInitExpression:
        """"""
    @classmethod
    @overload
    def ListInit(
        cls, newExpression: NewExpression, initializers: Array[Expression]
    ) -> ListInitExpression:
        """"""
    @classmethod
    @overload
    def Loop(cls, body: Expression) -> LoopExpression:
        """"""
    @classmethod
    @overload
    def Loop(cls, body: Expression, _break: LabelTarget) -> LoopExpression:
        """"""
    @classmethod
    @overload
    def Loop(cls, body: Expression, _break: LabelTarget, _continue: LabelTarget) -> LoopExpression:
        """"""
    @classmethod
    @overload
    def MakeBinary(
        cls, binaryType: ExpressionType, left: Expression, right: Expression
    ) -> BinaryExpression:
        """"""
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
        """"""
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
        """"""
    @classmethod
    def MakeCatchBlock(
        cls, type: Type, variable: ParameterExpression, body: Expression, filter: Expression
    ) -> CatchBlock:
        """"""
    @classmethod
    @overload
    def MakeDynamic(
        cls, delegateType: Type, binder: CallSiteBinder, arguments: IEnumerable[Expression]
    ) -> DynamicExpression:
        """"""
    @classmethod
    @overload
    def MakeDynamic(
        cls, delegateType: Type, binder: CallSiteBinder, arg0: Expression
    ) -> DynamicExpression:
        """"""
    @classmethod
    @overload
    def MakeDynamic(
        cls, delegateType: Type, binder: CallSiteBinder, arg0: Expression, arg1: Expression
    ) -> DynamicExpression:
        """"""
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
        """"""
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
        """"""
    @classmethod
    @overload
    def MakeDynamic(
        cls, delegateType: Type, binder: CallSiteBinder, arguments: Array[Expression]
    ) -> DynamicExpression:
        """"""
    @classmethod
    def MakeGoto(
        cls, kind: GotoExpressionKind, target: LabelTarget, value: Expression, type: Type
    ) -> GotoExpression:
        """"""
    @classmethod
    def MakeIndex(
        cls, instance: Expression, indexer: PropertyInfo, arguments: IEnumerable[Expression]
    ) -> IndexExpression:
        """"""
    @classmethod
    def MakeMemberAccess(cls, expression: Expression, member: MemberInfo) -> MemberExpression:
        """"""
    @classmethod
    def MakeTry(
        cls,
        type: Type,
        body: Expression,
        _finally: Expression,
        fault: Expression,
        handlers: IEnumerable[CatchBlock],
    ) -> TryExpression:
        """"""
    @classmethod
    @overload
    def MakeUnary(
        cls, unaryType: ExpressionType, operand: Expression, type: Type
    ) -> UnaryExpression:
        """"""
    @classmethod
    @overload
    def MakeUnary(
        cls, unaryType: ExpressionType, operand: Expression, type: Type, method: MethodInfo
    ) -> UnaryExpression:
        """"""
    @classmethod
    @overload
    def MemberBind(
        cls, member: MemberInfo, bindings: IEnumerable[MemberBinding]
    ) -> MemberMemberBinding:
        """"""
    @classmethod
    @overload
    def MemberBind(cls, member: MemberInfo, bindings: Array[MemberBinding]) -> MemberMemberBinding:
        """"""
    @classmethod
    @overload
    def MemberBind(
        cls, propertyAccessor: MethodInfo, bindings: IEnumerable[MemberBinding]
    ) -> MemberMemberBinding:
        """"""
    @classmethod
    @overload
    def MemberBind(
        cls, propertyAccessor: MethodInfo, bindings: Array[MemberBinding]
    ) -> MemberMemberBinding:
        """"""
    @classmethod
    @overload
    def MemberInit(
        cls, newExpression: NewExpression, bindings: IEnumerable[MemberBinding]
    ) -> MemberInitExpression:
        """"""
    @classmethod
    @overload
    def MemberInit(
        cls, newExpression: NewExpression, bindings: Array[MemberBinding]
    ) -> MemberInitExpression:
        """"""
    @classmethod
    @overload
    def Modulo(cls, left: Expression, right: Expression) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def Modulo(cls, left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def ModuloAssign(cls, left: Expression, right: Expression) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def ModuloAssign(
        cls, left: Expression, right: Expression, method: MethodInfo
    ) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def ModuloAssign(
        cls, left: Expression, right: Expression, method: MethodInfo, conversion: LambdaExpression
    ) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def Multiply(cls, left: Expression, right: Expression) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def Multiply(cls, left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def MultiplyAssign(cls, left: Expression, right: Expression) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def MultiplyAssign(
        cls, left: Expression, right: Expression, method: MethodInfo
    ) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def MultiplyAssign(
        cls, left: Expression, right: Expression, method: MethodInfo, conversion: LambdaExpression
    ) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def MultiplyAssignChecked(cls, left: Expression, right: Expression) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def MultiplyAssignChecked(
        cls, left: Expression, right: Expression, method: MethodInfo
    ) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def MultiplyAssignChecked(
        cls, left: Expression, right: Expression, method: MethodInfo, conversion: LambdaExpression
    ) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def MultiplyChecked(cls, left: Expression, right: Expression) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def MultiplyChecked(
        cls, left: Expression, right: Expression, method: MethodInfo
    ) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def Negate(cls, expression: Expression) -> UnaryExpression:
        """"""
    @classmethod
    @overload
    def Negate(cls, expression: Expression, method: MethodInfo) -> UnaryExpression:
        """"""
    @classmethod
    @overload
    def NegateChecked(cls, expression: Expression) -> UnaryExpression:
        """"""
    @classmethod
    @overload
    def NegateChecked(cls, expression: Expression, method: MethodInfo) -> UnaryExpression:
        """"""
    @classmethod
    @overload
    def New(cls, constructor: ConstructorInfo) -> NewExpression:
        """"""
    @classmethod
    @overload
    def New(cls, constructor: ConstructorInfo, arguments: IEnumerable[Expression]) -> NewExpression:
        """"""
    @classmethod
    @overload
    def New(
        cls,
        constructor: ConstructorInfo,
        arguments: IEnumerable[Expression],
        members: IEnumerable[MemberInfo],
    ) -> NewExpression:
        """"""
    @classmethod
    @overload
    def New(
        cls,
        constructor: ConstructorInfo,
        arguments: IEnumerable[Expression],
        members: Array[MemberInfo],
    ) -> NewExpression:
        """"""
    @classmethod
    @overload
    def New(cls, constructor: ConstructorInfo, arguments: Array[Expression]) -> NewExpression:
        """"""
    @classmethod
    @overload
    def New(cls, type: Type) -> NewExpression:
        """"""
    @classmethod
    @overload
    def NewArrayBounds(cls, type: Type, bounds: IEnumerable[Expression]) -> NewArrayExpression:
        """"""
    @classmethod
    @overload
    def NewArrayBounds(cls, type: Type, bounds: Array[Expression]) -> NewArrayExpression:
        """"""
    @classmethod
    @overload
    def NewArrayInit(cls, type: Type, initializers: IEnumerable[Expression]) -> NewArrayExpression:
        """"""
    @classmethod
    @overload
    def NewArrayInit(cls, type: Type, initializers: Array[Expression]) -> NewArrayExpression:
        """"""
    @classmethod
    @overload
    def Not(cls, expression: Expression) -> UnaryExpression:
        """"""
    @classmethod
    @overload
    def Not(cls, expression: Expression, method: MethodInfo) -> UnaryExpression:
        """"""
    @classmethod
    @overload
    def NotEqual(cls, left: Expression, right: Expression) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def NotEqual(
        cls, left: Expression, right: Expression, liftToNull: bool, method: MethodInfo
    ) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def OnesComplement(cls, expression: Expression) -> UnaryExpression:
        """"""
    @classmethod
    @overload
    def OnesComplement(cls, expression: Expression, method: MethodInfo) -> UnaryExpression:
        """"""
    @classmethod
    @overload
    def Or(cls, left: Expression, right: Expression) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def Or(cls, left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def OrAssign(cls, left: Expression, right: Expression) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def OrAssign(cls, left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def OrAssign(
        cls, left: Expression, right: Expression, method: MethodInfo, conversion: LambdaExpression
    ) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def OrElse(cls, left: Expression, right: Expression) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def OrElse(cls, left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def Parameter(cls, type: Type) -> ParameterExpression:
        """"""
    @classmethod
    @overload
    def Parameter(cls, type: Type, name: str) -> ParameterExpression:
        """"""
    @classmethod
    @overload
    def PostDecrementAssign(cls, expression: Expression) -> UnaryExpression:
        """"""
    @classmethod
    @overload
    def PostDecrementAssign(cls, expression: Expression, method: MethodInfo) -> UnaryExpression:
        """"""
    @classmethod
    @overload
    def PostIncrementAssign(cls, expression: Expression) -> UnaryExpression:
        """"""
    @classmethod
    @overload
    def PostIncrementAssign(cls, expression: Expression, method: MethodInfo) -> UnaryExpression:
        """"""
    @classmethod
    @overload
    def Power(cls, left: Expression, right: Expression) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def Power(cls, left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def PowerAssign(cls, left: Expression, right: Expression) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def PowerAssign(
        cls, left: Expression, right: Expression, method: MethodInfo
    ) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def PowerAssign(
        cls, left: Expression, right: Expression, method: MethodInfo, conversion: LambdaExpression
    ) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def PreDecrementAssign(cls, expression: Expression) -> UnaryExpression:
        """"""
    @classmethod
    @overload
    def PreDecrementAssign(cls, expression: Expression, method: MethodInfo) -> UnaryExpression:
        """"""
    @classmethod
    @overload
    def PreIncrementAssign(cls, expression: Expression) -> UnaryExpression:
        """"""
    @classmethod
    @overload
    def PreIncrementAssign(cls, expression: Expression, method: MethodInfo) -> UnaryExpression:
        """"""
    @classmethod
    @overload
    def Property(cls, expression: Expression, propertyAccessor: MethodInfo) -> MemberExpression:
        """"""
    @classmethod
    @overload
    def Property(cls, expression: Expression, property: PropertyInfo) -> MemberExpression:
        """"""
    @classmethod
    @overload
    def Property(
        cls, instance: Expression, indexer: PropertyInfo, arguments: IEnumerable[Expression]
    ) -> IndexExpression:
        """"""
    @classmethod
    @overload
    def Property(
        cls, instance: Expression, indexer: PropertyInfo, arguments: Array[Expression]
    ) -> IndexExpression:
        """"""
    @classmethod
    @overload
    def Property(cls, expression: Expression, propertyName: str) -> MemberExpression:
        """"""
    @classmethod
    @overload
    def Property(
        cls, instance: Expression, propertyName: str, arguments: Array[Expression]
    ) -> IndexExpression:
        """"""
    @classmethod
    @overload
    def Property(cls, expression: Expression, type: Type, propertyName: str) -> MemberExpression:
        """"""
    @classmethod
    def PropertyOrField(cls, expression: Expression, propertyOrFieldName: str) -> MemberExpression:
        """"""
    @classmethod
    def Quote(cls, expression: Expression) -> UnaryExpression:
        """"""
    def Reduce(self) -> Expression:
        """"""
    def ReduceAndCheck(self) -> Expression:
        """"""
    def ReduceExtensions(self) -> Expression:
        """"""
    @classmethod
    def ReferenceEqual(cls, left: Expression, right: Expression) -> BinaryExpression:
        """"""
    @classmethod
    def ReferenceNotEqual(cls, left: Expression, right: Expression) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def Rethrow(cls) -> UnaryExpression:
        """"""
    @classmethod
    @overload
    def Rethrow(cls, type: Type) -> UnaryExpression:
        """"""
    @classmethod
    @overload
    def Return(cls, target: LabelTarget) -> GotoExpression:
        """"""
    @classmethod
    @overload
    def Return(cls, target: LabelTarget, value: Expression) -> GotoExpression:
        """"""
    @classmethod
    @overload
    def Return(cls, target: LabelTarget, value: Expression, type: Type) -> GotoExpression:
        """"""
    @classmethod
    @overload
    def Return(cls, target: LabelTarget, type: Type) -> GotoExpression:
        """"""
    @classmethod
    @overload
    def RightShift(cls, left: Expression, right: Expression) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def RightShift(
        cls, left: Expression, right: Expression, method: MethodInfo
    ) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def RightShiftAssign(cls, left: Expression, right: Expression) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def RightShiftAssign(
        cls, left: Expression, right: Expression, method: MethodInfo
    ) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def RightShiftAssign(
        cls, left: Expression, right: Expression, method: MethodInfo, conversion: LambdaExpression
    ) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def RuntimeVariables(
        cls, variables: IEnumerable[ParameterExpression]
    ) -> RuntimeVariablesExpression:
        """"""
    @classmethod
    @overload
    def RuntimeVariables(cls, variables: Array[ParameterExpression]) -> RuntimeVariablesExpression:
        """"""
    @classmethod
    @overload
    def Subtract(cls, left: Expression, right: Expression) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def Subtract(cls, left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def SubtractAssign(cls, left: Expression, right: Expression) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def SubtractAssign(
        cls, left: Expression, right: Expression, method: MethodInfo
    ) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def SubtractAssign(
        cls, left: Expression, right: Expression, method: MethodInfo, conversion: LambdaExpression
    ) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def SubtractAssignChecked(cls, left: Expression, right: Expression) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def SubtractAssignChecked(
        cls, left: Expression, right: Expression, method: MethodInfo
    ) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def SubtractAssignChecked(
        cls, left: Expression, right: Expression, method: MethodInfo, conversion: LambdaExpression
    ) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def SubtractChecked(cls, left: Expression, right: Expression) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def SubtractChecked(
        cls, left: Expression, right: Expression, method: MethodInfo
    ) -> BinaryExpression:
        """"""
    @classmethod
    @overload
    def Switch(
        cls,
        switchValue: Expression,
        defaultBody: Expression,
        comparison: MethodInfo,
        cases: IEnumerable[SwitchCase],
    ) -> SwitchExpression:
        """"""
    @classmethod
    @overload
    def Switch(
        cls,
        switchValue: Expression,
        defaultBody: Expression,
        comparison: MethodInfo,
        cases: Array[SwitchCase],
    ) -> SwitchExpression:
        """"""
    @classmethod
    @overload
    def Switch(
        cls, switchValue: Expression, defaultBody: Expression, cases: Array[SwitchCase]
    ) -> SwitchExpression:
        """"""
    @classmethod
    @overload
    def Switch(cls, switchValue: Expression, cases: Array[SwitchCase]) -> SwitchExpression:
        """"""
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
        """"""
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
        """"""
    @classmethod
    @overload
    def SwitchCase(cls, body: Expression, testValues: IEnumerable[Expression]) -> SwitchCase:
        """"""
    @classmethod
    @overload
    def SwitchCase(cls, body: Expression, testValues: Array[Expression]) -> SwitchCase:
        """"""
    @classmethod
    @overload
    def SymbolDocument(cls, fileName: str) -> SymbolDocumentInfo:
        """"""
    @classmethod
    @overload
    def SymbolDocument(cls, fileName: str, language: Guid) -> SymbolDocumentInfo:
        """"""
    @classmethod
    @overload
    def SymbolDocument(
        cls, fileName: str, language: Guid, languageVendor: Guid
    ) -> SymbolDocumentInfo:
        """"""
    @classmethod
    @overload
    def SymbolDocument(
        cls, fileName: str, language: Guid, languageVendor: Guid, documentType: Guid
    ) -> SymbolDocumentInfo:
        """"""
    @classmethod
    @overload
    def Throw(cls, value: Expression) -> UnaryExpression:
        """"""
    @classmethod
    @overload
    def Throw(cls, value: Expression, type: Type) -> UnaryExpression:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def TryCatch(cls, body: Expression, handlers: Array[CatchBlock]) -> TryExpression:
        """"""
    @classmethod
    def TryCatchFinally(
        cls, body: Expression, _finally: Expression, handlers: Array[CatchBlock]
    ) -> TryExpression:
        """"""
    @classmethod
    def TryFault(cls, body: Expression, fault: Expression) -> TryExpression:
        """"""
    @classmethod
    def TryFinally(cls, body: Expression, _finally: Expression) -> TryExpression:
        """"""
    @classmethod
    def TryGetActionType(cls, typeArgs: Array[Type], actionType: Type) -> tuple[bool, Type]:
        """"""
    @classmethod
    def TryGetFuncType(cls, typeArgs: Array[Type], funcType: Type) -> tuple[bool, Type]:
        """"""
    @classmethod
    def TypeAs(cls, expression: Expression, type: Type) -> UnaryExpression:
        """"""
    @classmethod
    def TypeEqual(cls, expression: Expression, type: Type) -> TypeBinaryExpression:
        """"""
    @classmethod
    def TypeIs(cls, expression: Expression, type: Type) -> TypeBinaryExpression:
        """"""
    @classmethod
    @overload
    def UnaryPlus(cls, expression: Expression) -> UnaryExpression:
        """"""
    @classmethod
    @overload
    def UnaryPlus(cls, expression: Expression, method: MethodInfo) -> UnaryExpression:
        """"""
    @classmethod
    def Unbox(cls, expression: Expression, type: Type) -> UnaryExpression:
        """"""
    @classmethod
    @overload
    def Variable(cls, type: Type) -> ParameterExpression:
        """"""
    @classmethod
    @overload
    def Variable(cls, type: Type, name: str) -> ParameterExpression:
        """"""

class ExpressionStringBuilder(ExpressionVisitor):
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
    def VisitAndConvert[T](self, node: T, callerName: str) -> T:
        """"""
    @overload
    def VisitAndConvert[T](
        self, nodes: ReadOnlyCollection[T], callerName: str
    ) -> ReadOnlyCollection[T]:
        """"""

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
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    @overload
    def Visit[T](
        cls, nodes: ReadOnlyCollection[T], elementVisitor: Func[T, T]
    ) -> ReadOnlyCollection[T]:
        """"""
    @overload
    def Visit(self, nodes: ReadOnlyCollection[Expression]) -> ReadOnlyCollection[Expression]:
        """"""
    @overload
    def Visit(self, node: Expression) -> Expression:
        """"""
    @overload
    def VisitAndConvert[T](self, node: T, callerName: str) -> T:
        """"""
    @overload
    def VisitAndConvert[T](
        self, nodes: ReadOnlyCollection[T], callerName: str
    ) -> ReadOnlyCollection[T]:
        """"""

class Expression[TDelegate](LambdaExpression):
    """"""
    @property
    def Body(self) -> Expression:
        """"""
    @property
    def CanReduce(self) -> bool:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def NodeType(self) -> ExpressionType:
        """"""
    @property
    def Parameters(self) -> ReadOnlyCollection[ParameterExpression]:
        """"""
    @property
    def ReturnType(self) -> Type:
        """"""
    @property
    def TailCall(self) -> bool:
        """"""
    @property
    def Type(self) -> Type:
        """"""
    @overload
    def Compile(self) -> Delegate:
        """"""
    @overload
    def Compile(self, debugInfoGenerator: DebugInfoGenerator) -> Delegate:
        """"""
    @overload
    def Compile(self, preferInterpretation: bool) -> Delegate:
        """"""
    @overload
    def CompileToMethod(self, method: MethodBuilder) -> None:
        """"""
    @overload
    def CompileToMethod(
        self, method: MethodBuilder, debugInfoGenerator: DebugInfoGenerator
    ) -> None:
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
        self, body: Expression, parameters: IEnumerable[ParameterExpression]
    ) -> Expression[TDelegate]:
        """"""

class FieldExpression(MemberExpression):
    """"""
    def __init__(self, expression: Expression, member: FieldInfo) -> None:
        """"""
    @property
    def CanReduce(self) -> bool:
        """"""
    @property
    def Expression(self) -> Expression:
        """"""
    @property
    def Member(self) -> MemberInfo:
        """"""
    @property
    def NodeType(self) -> ExpressionType:
        """"""
    @property
    def Type(self) -> Type:
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
    def Update(self, expression: Expression) -> MemberExpression:
        """"""

class FullConditionalExpression(ConditionalExpression):
    """"""
    @property
    def CanReduce(self) -> bool:
        """"""
    @property
    def IfFalse(self) -> Expression:
        """"""
    @property
    def IfTrue(self) -> Expression:
        """"""
    @property
    def NodeType(self) -> ExpressionType:
        """"""
    @property
    def Test(self) -> Expression:
        """"""
    @property
    def Type(self) -> Type:
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
        self, test: Expression, ifTrue: Expression, ifFalse: Expression
    ) -> ConditionalExpression:
        """"""

class FullConditionalExpressionWithType(FullConditionalExpression):
    """"""
    @property
    def CanReduce(self) -> bool:
        """"""
    @property
    def IfFalse(self) -> Expression:
        """"""
    @property
    def IfTrue(self) -> Expression:
        """"""
    @property
    def NodeType(self) -> ExpressionType:
        """"""
    @property
    def Test(self) -> Expression:
        """"""
    @property
    def Type(self) -> Type:
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
        self, test: Expression, ifTrue: Expression, ifFalse: Expression
    ) -> ConditionalExpression:
        """"""

class GotoExpression(Expression):
    """"""
    @property
    def CanReduce(self) -> bool:
        """"""
    @property
    def Kind(self) -> GotoExpressionKind:
        """"""
    @property
    def NodeType(self) -> ExpressionType:
        """"""
    @property
    def Target(self) -> LabelTarget:
        """"""
    @property
    def Type(self) -> Type:
        """"""
    @property
    def Value(self) -> Expression:
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
    def Update(self, target: LabelTarget, value: Expression) -> GotoExpression:
        """"""

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

class IArgumentProvider(ABC):
    """"""
    @property
    def ArgumentCount(self) -> int:
        """"""
    def GetArgument(self, index: int) -> Expression:
        """"""

class IDynamicExpression(ABC, IArgumentProvider):
    """"""
    @property
    def ArgumentCount(self) -> int:
        """"""
    @property
    def DelegateType(self) -> Type:
        """"""
    def CreateCallSite(self) -> object:
        """"""
    def GetArgument(self, index: int) -> Expression:
        """"""
    def Rewrite(self, args: Array[Expression]) -> Expression:
        """"""

class IndexExpression(Expression, IArgumentProvider):
    """"""
    @property
    def ArgumentCount(self) -> int:
        """"""
    @property
    def Arguments(self) -> ReadOnlyCollection[Expression]:
        """"""
    @property
    def CanReduce(self) -> bool:
        """"""
    @property
    def Indexer(self) -> PropertyInfo:
        """"""
    @property
    def NodeType(self) -> ExpressionType:
        """"""
    @property
    def Object(self) -> Expression:
        """"""
    @property
    def Type(self) -> Type:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetArgument(self, index: int) -> Expression:
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
    def Update(self, object: Expression, arguments: IEnumerable[Expression]) -> IndexExpression:
        """"""

class InstanceMethodCallExpression2(MethodCallExpression, IArgumentProvider):
    """"""
    def __init__(
        self, method: MethodInfo, instance: Expression, arg0: Expression, arg1: Expression
    ) -> None:
        """"""
    @property
    def ArgumentCount(self) -> int:
        """"""
    @property
    def Arguments(self) -> ReadOnlyCollection[Expression]:
        """"""
    @property
    def CanReduce(self) -> bool:
        """"""
    @property
    def Method(self) -> MethodInfo:
        """"""
    @property
    def NodeType(self) -> ExpressionType:
        """"""
    @property
    def Object(self) -> Expression:
        """"""
    @property
    def Type(self) -> Type:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetArgument(self, index: int) -> Expression:
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
        self, object: Expression, arguments: IEnumerable[Expression]
    ) -> MethodCallExpression:
        """"""

class InstanceMethodCallExpression3(MethodCallExpression, IArgumentProvider):
    """"""
    def __init__(
        self,
        method: MethodInfo,
        instance: Expression,
        arg0: Expression,
        arg1: Expression,
        arg2: Expression,
    ) -> None:
        """"""
    @property
    def ArgumentCount(self) -> int:
        """"""
    @property
    def Arguments(self) -> ReadOnlyCollection[Expression]:
        """"""
    @property
    def CanReduce(self) -> bool:
        """"""
    @property
    def Method(self) -> MethodInfo:
        """"""
    @property
    def NodeType(self) -> ExpressionType:
        """"""
    @property
    def Object(self) -> Expression:
        """"""
    @property
    def Type(self) -> Type:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetArgument(self, index: int) -> Expression:
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
        self, object: Expression, arguments: IEnumerable[Expression]
    ) -> MethodCallExpression:
        """"""

class InstanceMethodCallExpressionN(MethodCallExpression, IArgumentProvider):
    """"""
    def __init__(self, method: MethodInfo, instance: Expression, args: IList[Expression]) -> None:
        """"""
    @property
    def ArgumentCount(self) -> int:
        """"""
    @property
    def Arguments(self) -> ReadOnlyCollection[Expression]:
        """"""
    @property
    def CanReduce(self) -> bool:
        """"""
    @property
    def Method(self) -> MethodInfo:
        """"""
    @property
    def NodeType(self) -> ExpressionType:
        """"""
    @property
    def Object(self) -> Expression:
        """"""
    @property
    def Type(self) -> Type:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetArgument(self, index: int) -> Expression:
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
        self, object: Expression, arguments: IEnumerable[Expression]
    ) -> MethodCallExpression:
        """"""

class InvocationExpression(Expression, IArgumentProvider):
    """"""
    @property
    def ArgumentCount(self) -> int:
        """"""
    @property
    def Arguments(self) -> ReadOnlyCollection[Expression]:
        """"""
    @property
    def CanReduce(self) -> bool:
        """"""
    @property
    def Expression(self) -> Expression:
        """"""
    @property
    def NodeType(self) -> ExpressionType:
        """"""
    @property
    def Type(self) -> Type:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetArgument(self, index: int) -> Expression:
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
        self, expression: Expression, arguments: IEnumerable[Expression]
    ) -> InvocationExpression:
        """"""

class LabelExpression(Expression):
    """"""
    @property
    def CanReduce(self) -> bool:
        """"""
    @property
    def DefaultValue(self) -> Expression:
        """"""
    @property
    def NodeType(self) -> ExpressionType:
        """"""
    @property
    def Target(self) -> LabelTarget:
        """"""
    @property
    def Type(self) -> Type:
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
    def Update(self, target: LabelTarget, defaultValue: Expression) -> LabelExpression:
        """"""

class LabelTarget(Object):
    """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def Type(self) -> Type:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class LambdaExpression(ABC, Expression):
    """"""
    @property
    def Body(self) -> Expression:
        """"""
    @property
    def CanReduce(self) -> bool:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def NodeType(self) -> ExpressionType:
        """"""
    @property
    def Parameters(self) -> ReadOnlyCollection[ParameterExpression]:
        """"""
    @property
    def ReturnType(self) -> Type:
        """"""
    @property
    def TailCall(self) -> bool:
        """"""
    @property
    def Type(self) -> Type:
        """"""
    @overload
    def Compile(self) -> Delegate:
        """"""
    @overload
    def Compile(self, debugInfoGenerator: DebugInfoGenerator) -> Delegate:
        """"""
    @overload
    def Compile(self, preferInterpretation: bool) -> Delegate:
        """"""
    @overload
    def CompileToMethod(self, method: MethodBuilder) -> None:
        """"""
    @overload
    def CompileToMethod(
        self, method: MethodBuilder, debugInfoGenerator: DebugInfoGenerator
    ) -> None:
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

class ListArgumentProvider(
    Object, ICollection[Expression], IEnumerable[Expression], IList[Expression], IEnumerable
):
    """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def Item(self) -> Expression:
        """"""
    @Item.setter
    def Item(self, value: Expression) -> None: ...
    def Add(self, item: Expression) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    def Contains(self, item: Expression) -> bool:
        """"""
    def CopyTo(self, array: Array[Expression], arrayIndex: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator[Expression]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def IndexOf(self, item: Expression) -> int:
        """"""
    def Insert(self, index: int, item: Expression) -> None:
        """"""
    def Remove(self, item: Expression) -> bool:
        """"""
    def RemoveAt(self, index: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def __contains__(self, item: Expression) -> bool:
        """"""
    def __iter__(self) -> Iterator[Expression]:
        """"""
    def __delitem__(self, item: Expression) -> bool:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, index: int) -> Expression:
        """"""
    def __setitem__(self, index: int, value: Expression) -> None:
        """"""

class ListInitExpression(Expression):
    """"""
    @property
    def CanReduce(self) -> bool:
        """"""
    @property
    def Initializers(self) -> ReadOnlyCollection[ElementInit]:
        """"""
    @property
    def NewExpression(self) -> NewExpression:
        """"""
    @property
    def NodeType(self) -> ExpressionType:
        """"""
    @property
    def Type(self) -> Type:
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
        self, newExpression: NewExpression, initializers: IEnumerable[ElementInit]
    ) -> ListInitExpression:
        """"""

class LogicalBinaryExpression(BinaryExpression):
    """"""
    @property
    def CanReduce(self) -> bool:
        """"""
    @property
    def Conversion(self) -> LambdaExpression:
        """"""
    @property
    def IsLifted(self) -> bool:
        """"""
    @property
    def IsLiftedToNull(self) -> bool:
        """"""
    @property
    def Left(self) -> Expression:
        """"""
    @property
    def Method(self) -> MethodInfo:
        """"""
    @property
    def NodeType(self) -> ExpressionType:
        """"""
    @property
    def Right(self) -> Expression:
        """"""
    @property
    def Type(self) -> Type:
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
        self, left: Expression, conversion: LambdaExpression, right: Expression
    ) -> BinaryExpression:
        """"""

class LoopExpression(Expression):
    """"""
    @property
    def Body(self) -> Expression:
        """"""
    @property
    def BreakLabel(self) -> LabelTarget:
        """"""
    @property
    def CanReduce(self) -> bool:
        """"""
    @property
    def ContinueLabel(self) -> LabelTarget:
        """"""
    @property
    def NodeType(self) -> ExpressionType:
        """"""
    @property
    def Type(self) -> Type:
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
        self, breakLabel: LabelTarget, continueLabel: LabelTarget, body: Expression
    ) -> LoopExpression:
        """"""

class MemberAssignment(MemberBinding):
    """"""
    @property
    def BindingType(self) -> MemberBindingType:
        """"""
    @property
    def Expression(self) -> Expression:
        """"""
    @property
    def Member(self) -> MemberInfo:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def Update(self, expression: Expression) -> MemberAssignment:
        """"""

class MemberBinding(ABC, Object):
    """"""
    @property
    def BindingType(self) -> MemberBindingType:
        """"""
    @property
    def Member(self) -> MemberInfo:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

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
        """"""
    @property
    def Expression(self) -> Expression:
        """"""
    @property
    def Member(self) -> MemberInfo:
        """"""
    @property
    def NodeType(self) -> ExpressionType:
        """"""
    @property
    def Type(self) -> Type:
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
    def Update(self, expression: Expression) -> MemberExpression:
        """"""

class MemberInitExpression(Expression):
    """"""
    @property
    def Bindings(self) -> ReadOnlyCollection[MemberBinding]:
        """"""
    @property
    def CanReduce(self) -> bool:
        """"""
    @property
    def NewExpression(self) -> NewExpression:
        """"""
    @property
    def NodeType(self) -> ExpressionType:
        """"""
    @property
    def Type(self) -> Type:
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
        self, newExpression: NewExpression, bindings: IEnumerable[MemberBinding]
    ) -> MemberInitExpression:
        """"""

class MemberListBinding(MemberBinding):
    """"""
    @property
    def BindingType(self) -> MemberBindingType:
        """"""
    @property
    def Initializers(self) -> ReadOnlyCollection[ElementInit]:
        """"""
    @property
    def Member(self) -> MemberInfo:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def Update(self, initializers: IEnumerable[ElementInit]) -> MemberListBinding:
        """"""

class MemberMemberBinding(MemberBinding):
    """"""
    @property
    def BindingType(self) -> MemberBindingType:
        """"""
    @property
    def Bindings(self) -> ReadOnlyCollection[MemberBinding]:
        """"""
    @property
    def Member(self) -> MemberInfo:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def Update(self, bindings: IEnumerable[MemberBinding]) -> MemberMemberBinding:
        """"""

class MethodBinaryExpression(SimpleBinaryExpression):
    """"""
    @property
    def CanReduce(self) -> bool:
        """"""
    @property
    def Conversion(self) -> LambdaExpression:
        """"""
    @property
    def IsLifted(self) -> bool:
        """"""
    @property
    def IsLiftedToNull(self) -> bool:
        """"""
    @property
    def Left(self) -> Expression:
        """"""
    @property
    def Method(self) -> MethodInfo:
        """"""
    @property
    def NodeType(self) -> ExpressionType:
        """"""
    @property
    def Right(self) -> Expression:
        """"""
    @property
    def Type(self) -> Type:
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
        self, left: Expression, conversion: LambdaExpression, right: Expression
    ) -> BinaryExpression:
        """"""

class MethodCallExpression(Expression, IArgumentProvider):
    """"""
    @property
    def ArgumentCount(self) -> int:
        """"""
    @property
    def Arguments(self) -> ReadOnlyCollection[Expression]:
        """"""
    @property
    def CanReduce(self) -> bool:
        """"""
    @property
    def Method(self) -> MethodInfo:
        """"""
    @property
    def NodeType(self) -> ExpressionType:
        """"""
    @property
    def Object(self) -> Expression:
        """"""
    @property
    def Type(self) -> Type:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetArgument(self, index: int) -> Expression:
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
        self, object: Expression, arguments: IEnumerable[Expression]
    ) -> MethodCallExpression:
        """"""

class MethodCallExpression1(MethodCallExpression, IArgumentProvider):
    """"""
    def __init__(self, method: MethodInfo, arg0: Expression) -> None:
        """"""
    @property
    def ArgumentCount(self) -> int:
        """"""
    @property
    def Arguments(self) -> ReadOnlyCollection[Expression]:
        """"""
    @property
    def CanReduce(self) -> bool:
        """"""
    @property
    def Method(self) -> MethodInfo:
        """"""
    @property
    def NodeType(self) -> ExpressionType:
        """"""
    @property
    def Object(self) -> Expression:
        """"""
    @property
    def Type(self) -> Type:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetArgument(self, index: int) -> Expression:
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
        self, object: Expression, arguments: IEnumerable[Expression]
    ) -> MethodCallExpression:
        """"""

class MethodCallExpression2(MethodCallExpression, IArgumentProvider):
    """"""
    def __init__(self, method: MethodInfo, arg0: Expression, arg1: Expression) -> None:
        """"""
    @property
    def ArgumentCount(self) -> int:
        """"""
    @property
    def Arguments(self) -> ReadOnlyCollection[Expression]:
        """"""
    @property
    def CanReduce(self) -> bool:
        """"""
    @property
    def Method(self) -> MethodInfo:
        """"""
    @property
    def NodeType(self) -> ExpressionType:
        """"""
    @property
    def Object(self) -> Expression:
        """"""
    @property
    def Type(self) -> Type:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetArgument(self, index: int) -> Expression:
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
        self, object: Expression, arguments: IEnumerable[Expression]
    ) -> MethodCallExpression:
        """"""

class MethodCallExpression3(MethodCallExpression, IArgumentProvider):
    """"""
    def __init__(
        self, method: MethodInfo, arg0: Expression, arg1: Expression, arg2: Expression
    ) -> None:
        """"""
    @property
    def ArgumentCount(self) -> int:
        """"""
    @property
    def Arguments(self) -> ReadOnlyCollection[Expression]:
        """"""
    @property
    def CanReduce(self) -> bool:
        """"""
    @property
    def Method(self) -> MethodInfo:
        """"""
    @property
    def NodeType(self) -> ExpressionType:
        """"""
    @property
    def Object(self) -> Expression:
        """"""
    @property
    def Type(self) -> Type:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetArgument(self, index: int) -> Expression:
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
        self, object: Expression, arguments: IEnumerable[Expression]
    ) -> MethodCallExpression:
        """"""

class MethodCallExpression4(MethodCallExpression, IArgumentProvider):
    """"""
    def __init__(
        self,
        method: MethodInfo,
        arg0: Expression,
        arg1: Expression,
        arg2: Expression,
        arg3: Expression,
    ) -> None:
        """"""
    @property
    def ArgumentCount(self) -> int:
        """"""
    @property
    def Arguments(self) -> ReadOnlyCollection[Expression]:
        """"""
    @property
    def CanReduce(self) -> bool:
        """"""
    @property
    def Method(self) -> MethodInfo:
        """"""
    @property
    def NodeType(self) -> ExpressionType:
        """"""
    @property
    def Object(self) -> Expression:
        """"""
    @property
    def Type(self) -> Type:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetArgument(self, index: int) -> Expression:
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
        self, object: Expression, arguments: IEnumerable[Expression]
    ) -> MethodCallExpression:
        """"""

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
    ) -> None:
        """"""
    @property
    def ArgumentCount(self) -> int:
        """"""
    @property
    def Arguments(self) -> ReadOnlyCollection[Expression]:
        """"""
    @property
    def CanReduce(self) -> bool:
        """"""
    @property
    def Method(self) -> MethodInfo:
        """"""
    @property
    def NodeType(self) -> ExpressionType:
        """"""
    @property
    def Object(self) -> Expression:
        """"""
    @property
    def Type(self) -> Type:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetArgument(self, index: int) -> Expression:
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
        self, object: Expression, arguments: IEnumerable[Expression]
    ) -> MethodCallExpression:
        """"""

class MethodCallExpressionN(MethodCallExpression, IArgumentProvider):
    """"""
    def __init__(self, method: MethodInfo, args: IList[Expression]) -> None:
        """"""
    @property
    def ArgumentCount(self) -> int:
        """"""
    @property
    def Arguments(self) -> ReadOnlyCollection[Expression]:
        """"""
    @property
    def CanReduce(self) -> bool:
        """"""
    @property
    def Method(self) -> MethodInfo:
        """"""
    @property
    def NodeType(self) -> ExpressionType:
        """"""
    @property
    def Object(self) -> Expression:
        """"""
    @property
    def Type(self) -> Type:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetArgument(self, index: int) -> Expression:
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
        self, object: Expression, arguments: IEnumerable[Expression]
    ) -> MethodCallExpression:
        """"""

class NewArrayBoundsExpression(NewArrayExpression):
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
    def Type(self) -> Type:
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
    def Update(self, expressions: IEnumerable[Expression]) -> NewArrayExpression:
        """"""

class NewArrayExpression(Expression):
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
    def Type(self) -> Type:
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
    def Update(self, expressions: IEnumerable[Expression]) -> NewArrayExpression:
        """"""

class NewArrayInitExpression(NewArrayExpression):
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
    def Type(self) -> Type:
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
    def Update(self, expressions: IEnumerable[Expression]) -> NewArrayExpression:
        """"""

class NewExpression(Expression, IArgumentProvider):
    """"""
    @property
    def ArgumentCount(self) -> int:
        """"""
    @property
    def Arguments(self) -> ReadOnlyCollection[Expression]:
        """"""
    @property
    def CanReduce(self) -> bool:
        """"""
    @property
    def Constructor(self) -> ConstructorInfo:
        """"""
    @property
    def Members(self) -> ReadOnlyCollection[MemberInfo]:
        """"""
    @property
    def NodeType(self) -> ExpressionType:
        """"""
    @property
    def Type(self) -> Type:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetArgument(self, index: int) -> Expression:
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
    def Update(self, arguments: IEnumerable[Expression]) -> NewExpression:
        """"""

class NewValueTypeExpression(NewExpression, IArgumentProvider):
    """"""
    @property
    def ArgumentCount(self) -> int:
        """"""
    @property
    def Arguments(self) -> ReadOnlyCollection[Expression]:
        """"""
    @property
    def CanReduce(self) -> bool:
        """"""
    @property
    def Constructor(self) -> ConstructorInfo:
        """"""
    @property
    def Members(self) -> ReadOnlyCollection[MemberInfo]:
        """"""
    @property
    def NodeType(self) -> ExpressionType:
        """"""
    @property
    def Type(self) -> Type:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetArgument(self, index: int) -> Expression:
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
    def Update(self, arguments: IEnumerable[Expression]) -> NewExpression:
        """"""

class OldExpressionVisitor(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class OpAssignMethodConversionBinaryExpression(MethodBinaryExpression):
    """"""
    @property
    def CanReduce(self) -> bool:
        """"""
    @property
    def Conversion(self) -> LambdaExpression:
        """"""
    @property
    def IsLifted(self) -> bool:
        """"""
    @property
    def IsLiftedToNull(self) -> bool:
        """"""
    @property
    def Left(self) -> Expression:
        """"""
    @property
    def Method(self) -> MethodInfo:
        """"""
    @property
    def NodeType(self) -> ExpressionType:
        """"""
    @property
    def Right(self) -> Expression:
        """"""
    @property
    def Type(self) -> Type:
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
        self, left: Expression, conversion: LambdaExpression, right: Expression
    ) -> BinaryExpression:
        """"""

class ParameterExpression(Expression):
    """"""
    @property
    def CanReduce(self) -> bool:
        """"""
    @property
    def IsByRef(self) -> bool:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def NodeType(self) -> ExpressionType:
        """"""
    @property
    def Type(self) -> Type:
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

class PrimitiveParameterExpression[T](ParameterExpression):
    """"""
    @property
    def CanReduce(self) -> bool:
        """"""
    @property
    def IsByRef(self) -> bool:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def NodeType(self) -> ExpressionType:
        """"""
    @property
    def Type(self) -> Type:
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

class PropertyExpression(MemberExpression):
    """"""
    def __init__(self, expression: Expression, member: PropertyInfo) -> None:
        """"""
    @property
    def CanReduce(self) -> bool:
        """"""
    @property
    def Expression(self) -> Expression:
        """"""
    @property
    def Member(self) -> MemberInfo:
        """"""
    @property
    def NodeType(self) -> ExpressionType:
        """"""
    @property
    def Type(self) -> Type:
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
    def Update(self, expression: Expression) -> MemberExpression:
        """"""

class ReadOnlyCollectionExtensions(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class RuntimeVariablesExpression(Expression):
    """"""
    @property
    def CanReduce(self) -> bool:
        """"""
    @property
    def NodeType(self) -> ExpressionType:
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
    def Update(self, variables: IEnumerable[ParameterExpression]) -> RuntimeVariablesExpression:
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

class Scope1(ScopeExpression):
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

class ScopeExpression(BlockExpression):
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

class ScopeN(ScopeExpression):
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

class ScopeWithType(ScopeN):
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

class Set[T](Object, ICollection[T], IEnumerable[T], IEnumerable):
    """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
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
    def Remove(self, item: T) -> bool:
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

class SimpleBinaryExpression(BinaryExpression):
    """"""
    @property
    def CanReduce(self) -> bool:
        """"""
    @property
    def Conversion(self) -> LambdaExpression:
        """"""
    @property
    def IsLifted(self) -> bool:
        """"""
    @property
    def IsLiftedToNull(self) -> bool:
        """"""
    @property
    def Left(self) -> Expression:
        """"""
    @property
    def Method(self) -> MethodInfo:
        """"""
    @property
    def NodeType(self) -> ExpressionType:
        """"""
    @property
    def Right(self) -> Expression:
        """"""
    @property
    def Type(self) -> Type:
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
        self, left: Expression, conversion: LambdaExpression, right: Expression
    ) -> BinaryExpression:
        """"""

class SpanDebugInfoExpression(DebugInfoExpression):
    """"""
    @property
    def CanReduce(self) -> bool:
        """"""
    @property
    def Document(self) -> SymbolDocumentInfo:
        """"""
    @property
    def EndColumn(self) -> int:
        """"""
    @property
    def EndLine(self) -> int:
        """"""
    @property
    def IsClear(self) -> bool:
        """"""
    @property
    def NodeType(self) -> ExpressionType:
        """"""
    @property
    def StartColumn(self) -> int:
        """"""
    @property
    def StartLine(self) -> int:
        """"""
    @property
    def Type(self) -> Type:
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

class StackGuard(Object):
    """"""
    def __init__(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def RunOnEmptyStack[T1, T2, T3](
        self, action: Action[T1, T2, T3], arg1: T1, arg2: T2, arg3: T3
    ) -> None:
        """"""
    @overload
    def RunOnEmptyStack[T1, T2](self, action: Action[T1, T2], arg1: T1, arg2: T2) -> None:
        """"""
    @overload
    def RunOnEmptyStack[T1, T2, R](self, action: Func[T1, T2, R], arg1: T1, arg2: T2) -> R:
        """"""
    @overload
    def RunOnEmptyStack[T1, T2, T3, R](
        self, action: Func[T1, T2, T3, R], arg1: T1, arg2: T2, arg3: T3
    ) -> R:
        """"""
    def ToString(self) -> str:
        """"""
    def TryEnterOnCurrentStack(self) -> bool:
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

class SwitchCase(Object):
    """"""
    @property
    def Body(self) -> Expression:
        """"""
    @property
    def TestValues(self) -> ReadOnlyCollection[Expression]:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def Update(self, testValues: IEnumerable[Expression], body: Expression) -> SwitchCase:
        """"""

class SwitchExpression(Expression):
    """"""
    @property
    def CanReduce(self) -> bool:
        """"""
    @property
    def Cases(self) -> ReadOnlyCollection[SwitchCase]:
        """"""
    @property
    def Comparison(self) -> MethodInfo:
        """"""
    @property
    def DefaultBody(self) -> Expression:
        """"""
    @property
    def NodeType(self) -> ExpressionType:
        """"""
    @property
    def SwitchValue(self) -> Expression:
        """"""
    @property
    def Type(self) -> Type:
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
        self, switchValue: Expression, cases: IEnumerable[SwitchCase], defaultBody: Expression
    ) -> SwitchExpression:
        """"""

class SymbolDocumentInfo(Object):
    """"""
    @property
    def DocumentType(self) -> Guid:
        """"""
    @property
    def FileName(self) -> str:
        """"""
    @property
    def Language(self) -> Guid:
        """"""
    @property
    def LanguageVendor(self) -> Guid:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SymbolDocumentWithGuids(SymbolDocumentInfo):
    """"""
    @property
    def DocumentType(self) -> Guid:
        """"""
    @property
    def FileName(self) -> str:
        """"""
    @property
    def Language(self) -> Guid:
        """"""
    @property
    def LanguageVendor(self) -> Guid:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class TryExpression(Expression):
    """"""
    @property
    def Body(self) -> Expression:
        """"""
    @property
    def CanReduce(self) -> bool:
        """"""
    @property
    def Fault(self) -> Expression:
        """"""
    @property
    def Finally(self) -> Expression:
        """"""
    @property
    def Handlers(self) -> ReadOnlyCollection[CatchBlock]:
        """"""
    @property
    def NodeType(self) -> ExpressionType:
        """"""
    @property
    def Type(self) -> Type:
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
        self,
        body: Expression,
        handlers: IEnumerable[CatchBlock],
        _finally: Expression,
        fault: Expression,
    ) -> TryExpression:
        """"""

class TypeBinaryExpression(Expression):
    """"""
    @property
    def CanReduce(self) -> bool:
        """"""
    @property
    def Expression(self) -> Expression:
        """"""
    @property
    def NodeType(self) -> ExpressionType:
        """"""
    @property
    def Type(self) -> Type:
        """"""
    @property
    def TypeOperand(self) -> Type:
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
    def Update(self, expression: Expression) -> TypeBinaryExpression:
        """"""

class TypedConstantExpression(ConstantExpression):
    """"""
    @property
    def CanReduce(self) -> bool:
        """"""
    @property
    def NodeType(self) -> ExpressionType:
        """"""
    @property
    def Type(self) -> Type:
        """"""
    @property
    def Value(self) -> object:
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

class TypedDynamicExpression1(DynamicExpression1, IArgumentProvider, IDynamicExpression):
    """"""
    @property
    def ArgumentCount(self) -> int:
        """"""
    @property
    def Arguments(self) -> ReadOnlyCollection[Expression]:
        """"""
    @property
    def Binder(self) -> CallSiteBinder:
        """"""
    @property
    def CanReduce(self) -> bool:
        """"""
    @property
    def DelegateType(self) -> Type:
        """"""
    @property
    def NodeType(self) -> ExpressionType:
        """"""
    @property
    def Type(self) -> Type:
        """"""
    def CreateCallSite(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetArgument(self, index: int) -> Expression:
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
    def Rewrite(self, args: Array[Expression]) -> Expression:
        """"""
    def ToString(self) -> str:
        """"""
    def Update(self, arguments: IEnumerable[Expression]) -> DynamicExpression:
        """"""

class TypedDynamicExpression2(DynamicExpression2, IArgumentProvider, IDynamicExpression):
    """"""
    @property
    def ArgumentCount(self) -> int:
        """"""
    @property
    def Arguments(self) -> ReadOnlyCollection[Expression]:
        """"""
    @property
    def Binder(self) -> CallSiteBinder:
        """"""
    @property
    def CanReduce(self) -> bool:
        """"""
    @property
    def DelegateType(self) -> Type:
        """"""
    @property
    def NodeType(self) -> ExpressionType:
        """"""
    @property
    def Type(self) -> Type:
        """"""
    def CreateCallSite(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetArgument(self, index: int) -> Expression:
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
    def Rewrite(self, args: Array[Expression]) -> Expression:
        """"""
    def ToString(self) -> str:
        """"""
    def Update(self, arguments: IEnumerable[Expression]) -> DynamicExpression:
        """"""

class TypedDynamicExpression3(DynamicExpression3, IArgumentProvider, IDynamicExpression):
    """"""
    @property
    def ArgumentCount(self) -> int:
        """"""
    @property
    def Arguments(self) -> ReadOnlyCollection[Expression]:
        """"""
    @property
    def Binder(self) -> CallSiteBinder:
        """"""
    @property
    def CanReduce(self) -> bool:
        """"""
    @property
    def DelegateType(self) -> Type:
        """"""
    @property
    def NodeType(self) -> ExpressionType:
        """"""
    @property
    def Type(self) -> Type:
        """"""
    def CreateCallSite(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetArgument(self, index: int) -> Expression:
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
    def Rewrite(self, args: Array[Expression]) -> Expression:
        """"""
    def ToString(self) -> str:
        """"""
    def Update(self, arguments: IEnumerable[Expression]) -> DynamicExpression:
        """"""

class TypedDynamicExpression4(DynamicExpression4, IArgumentProvider, IDynamicExpression):
    """"""
    @property
    def ArgumentCount(self) -> int:
        """"""
    @property
    def Arguments(self) -> ReadOnlyCollection[Expression]:
        """"""
    @property
    def Binder(self) -> CallSiteBinder:
        """"""
    @property
    def CanReduce(self) -> bool:
        """"""
    @property
    def DelegateType(self) -> Type:
        """"""
    @property
    def NodeType(self) -> ExpressionType:
        """"""
    @property
    def Type(self) -> Type:
        """"""
    def CreateCallSite(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetArgument(self, index: int) -> Expression:
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
    def Rewrite(self, args: Array[Expression]) -> Expression:
        """"""
    def ToString(self) -> str:
        """"""
    def Update(self, arguments: IEnumerable[Expression]) -> DynamicExpression:
        """"""

class TypedDynamicExpressionN(DynamicExpressionN, IArgumentProvider, IDynamicExpression):
    """"""
    @property
    def ArgumentCount(self) -> int:
        """"""
    @property
    def Arguments(self) -> ReadOnlyCollection[Expression]:
        """"""
    @property
    def Binder(self) -> CallSiteBinder:
        """"""
    @property
    def CanReduce(self) -> bool:
        """"""
    @property
    def DelegateType(self) -> Type:
        """"""
    @property
    def NodeType(self) -> ExpressionType:
        """"""
    @property
    def Type(self) -> Type:
        """"""
    def CreateCallSite(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetArgument(self, index: int) -> Expression:
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
    def Rewrite(self, args: Array[Expression]) -> Expression:
        """"""
    def ToString(self) -> str:
        """"""
    def Update(self, arguments: IEnumerable[Expression]) -> DynamicExpression:
        """"""

class TypedParameterExpression(ParameterExpression):
    """"""
    @property
    def CanReduce(self) -> bool:
        """"""
    @property
    def IsByRef(self) -> bool:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def NodeType(self) -> ExpressionType:
        """"""
    @property
    def Type(self) -> Type:
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

class UnaryExpression(Expression):
    """"""
    @property
    def CanReduce(self) -> bool:
        """"""
    @property
    def IsLifted(self) -> bool:
        """"""
    @property
    def IsLiftedToNull(self) -> bool:
        """"""
    @property
    def Method(self) -> MethodInfo:
        """"""
    @property
    def NodeType(self) -> ExpressionType:
        """"""
    @property
    def Operand(self) -> Expression:
        """"""
    @property
    def Type(self) -> Type:
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
    def Update(self, operand: Expression) -> UnaryExpression:
        """"""
