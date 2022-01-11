from __future__ import annotations

from abc import ABC
from typing import Generic, List, Protocol, Tuple, TypeVar, Union, overload

from System import Action, Array, Boolean, Delegate, Enum, Func, Guid, Int32, Object, String, Type, Void
from System.Collections import IEnumerable
from System.Collections.Generic import ICollection, IEnumerable, IEnumerator, IList
from System.Collections.ObjectModel import ReadOnlyCollection
from System.ComponentModel import CategoryAttribute, DescriptionAttribute
from System.Reflection import ConstructorInfo, FieldInfo, MemberInfo, MethodInfo, PropertyInfo
from System.Reflection.Emit import MethodBuilder
from System.Resources import ResourceManager
from System.Runtime.CompilerServices import CallSiteBinder, DebugInfoGenerator
from System.Runtime.InteropServices import _Attribute

# ---------- Types ---------- #

R = TypeVar('R')
T = TypeVar('T')
T1 = TypeVar('T1')
T2 = TypeVar('T2')
T3 = TypeVar('T3')
TDelegate = TypeVar('TDelegate')

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
IntType = Union[int, Int32]
ObjectType = Object
StringType = Union[str, String]
TypeType = Union[type, Type]
VoidType = Union[None, Void]


# ---------- Classes ---------- #

class ArgumentProviderOps(ABC, ObjectType):
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


class AssignBinaryExpression(BinaryExpression):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def NodeType(self) -> ExpressionType: ...
    
    @property
    def Type(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def get_NodeType(self) -> ExpressionType: ...
    
    def get_Type(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class BinaryExpression(Expression):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def CanReduce(self) -> BooleanType: ...
    
    @property
    def Conversion(self) -> LambdaExpression: ...
    
    @property
    def IsLifted(self) -> BooleanType: ...
    
    @property
    def IsLiftedToNull(self) -> BooleanType: ...
    
    @property
    def Left(self) -> Expression: ...
    
    @property
    def Method(self) -> MethodInfo: ...
    
    @property
    def Right(self) -> Expression: ...
    
    # ---------- Methods ---------- #
    
    def Reduce(self) -> Expression: ...
    
    def Update(self, left: Expression, conversion: LambdaExpression, right: Expression) -> BinaryExpression: ...
    
    def get_CanReduce(self) -> BooleanType: ...
    
    def get_Conversion(self) -> LambdaExpression: ...
    
    def get_IsLifted(self) -> BooleanType: ...
    
    def get_IsLiftedToNull(self) -> BooleanType: ...
    
    def get_Left(self) -> Expression: ...
    
    def get_Method(self) -> MethodInfo: ...
    
    def get_Right(self) -> Expression: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Block2(BlockExpression):
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


class Block3(BlockExpression):
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


class Block4(BlockExpression):
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


class Block5(BlockExpression):
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


class BlockExpression(Expression):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Expressions(self) -> ReadOnlyCollection[Expression]: ...
    
    @property
    def NodeType(self) -> ExpressionType: ...
    
    @property
    def Result(self) -> Expression: ...
    
    @property
    def Type(self) -> TypeType: ...
    
    @property
    def Variables(self) -> ReadOnlyCollection[ParameterExpression]: ...
    
    # ---------- Methods ---------- #
    
    def Update(self, variables: IEnumerable[ParameterExpression], expressions: IEnumerable[Expression]) -> BlockExpression: ...
    
    def get_Expressions(self) -> ReadOnlyCollection[Expression]: ...
    
    def get_NodeType(self) -> ExpressionType: ...
    
    def get_Result(self) -> Expression: ...
    
    def get_Type(self) -> TypeType: ...
    
    def get_Variables(self) -> ReadOnlyCollection[ParameterExpression]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class BlockExpressionList(ObjectType, IList[Expression], ICollection[Expression], IEnumerable[Expression], IEnumerable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def IsReadOnly(self) -> BooleanType: ...
    
    def __getitem__(self, key: IntType) -> Expression: ...
    
    def __setitem__(self, key: IntType, value: Expression) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, item: Expression) -> VoidType: ...
    
    def Clear(self) -> VoidType: ...
    
    def Contains(self, item: Expression) -> BooleanType: ...
    
    def CopyTo(self, array: ArrayType[Expression], arrayIndex: IntType) -> VoidType: ...
    
    def GetEnumerator(self) -> IEnumerator[Expression]: ...
    
    def IndexOf(self, item: Expression) -> IntType: ...
    
    def Insert(self, index: IntType, item: Expression) -> VoidType: ...
    
    def Remove(self, item: Expression) -> BooleanType: ...
    
    def RemoveAt(self, index: IntType) -> VoidType: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_IsReadOnly(self) -> BooleanType: ...
    
    def get_Item(self, index: IntType) -> Expression: ...
    
    def set_Item(self, index: IntType, value: Expression) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class BlockN(BlockExpression):
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


class ByRefParameterExpression(TypedParameterExpression):
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


class CatchBlock(ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Body(self) -> Expression: ...
    
    @property
    def Filter(self) -> Expression: ...
    
    @property
    def Test(self) -> TypeType: ...
    
    @property
    def Variable(self) -> ParameterExpression: ...
    
    # ---------- Methods ---------- #
    
    def ToString(self) -> StringType: ...
    
    def Update(self, variable: ParameterExpression, filter: Expression, body: Expression) -> CatchBlock: ...
    
    def get_Body(self) -> Expression: ...
    
    def get_Filter(self) -> Expression: ...
    
    def get_Test(self) -> TypeType: ...
    
    def get_Variable(self) -> ParameterExpression: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ClearDebugInfoExpression(DebugInfoExpression):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def EndColumn(self) -> IntType: ...
    
    @property
    def EndLine(self) -> IntType: ...
    
    @property
    def IsClear(self) -> BooleanType: ...
    
    @property
    def StartColumn(self) -> IntType: ...
    
    @property
    def StartLine(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def get_EndColumn(self) -> IntType: ...
    
    def get_EndLine(self) -> IntType: ...
    
    def get_IsClear(self) -> BooleanType: ...
    
    def get_StartColumn(self) -> IntType: ...
    
    def get_StartLine(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CoalesceConversionBinaryExpression(BinaryExpression):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def NodeType(self) -> ExpressionType: ...
    
    @property
    def Type(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def get_NodeType(self) -> ExpressionType: ...
    
    def get_Type(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ConditionalExpression(Expression):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def IfFalse(self) -> Expression: ...
    
    @property
    def IfTrue(self) -> Expression: ...
    
    @property
    def NodeType(self) -> ExpressionType: ...
    
    @property
    def Test(self) -> Expression: ...
    
    @property
    def Type(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def Update(self, test: Expression, ifTrue: Expression, ifFalse: Expression) -> ConditionalExpression: ...
    
    def get_IfFalse(self) -> Expression: ...
    
    def get_IfTrue(self) -> Expression: ...
    
    def get_NodeType(self) -> ExpressionType: ...
    
    def get_Test(self) -> Expression: ...
    
    def get_Type(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ConstantCheck(ABC, ObjectType):
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


class ConstantExpression(Expression):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def NodeType(self) -> ExpressionType: ...
    
    @property
    def Type(self) -> TypeType: ...
    
    @property
    def Value(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def get_NodeType(self) -> ExpressionType: ...
    
    def get_Type(self) -> TypeType: ...
    
    def get_Value(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DebugInfoExpression(Expression):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Document(self) -> SymbolDocumentInfo: ...
    
    @property
    def EndColumn(self) -> IntType: ...
    
    @property
    def EndLine(self) -> IntType: ...
    
    @property
    def IsClear(self) -> BooleanType: ...
    
    @property
    def NodeType(self) -> ExpressionType: ...
    
    @property
    def StartColumn(self) -> IntType: ...
    
    @property
    def StartLine(self) -> IntType: ...
    
    @property
    def Type(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def get_Document(self) -> SymbolDocumentInfo: ...
    
    def get_EndColumn(self) -> IntType: ...
    
    def get_EndLine(self) -> IntType: ...
    
    def get_IsClear(self) -> BooleanType: ...
    
    def get_NodeType(self) -> ExpressionType: ...
    
    def get_StartColumn(self) -> IntType: ...
    
    def get_StartLine(self) -> IntType: ...
    
    def get_Type(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DebugViewWriter(ExpressionVisitor):
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


class DefaultExpression(Expression):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def NodeType(self) -> ExpressionType: ...
    
    @property
    def Type(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def get_NodeType(self) -> ExpressionType: ...
    
    def get_Type(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DynamicExpression(Expression, IDynamicExpression, IArgumentProvider):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Arguments(self) -> ReadOnlyCollection[Expression]: ...
    
    @property
    def Binder(self) -> CallSiteBinder: ...
    
    @property
    def DelegateType(self) -> TypeType: ...
    
    @property
    def NodeType(self) -> ExpressionType: ...
    
    @property
    def Type(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    @overload
    def Dynamic(binder: CallSiteBinder, returnType: TypeType, arguments: ArrayType[Expression]) -> DynamicExpression: ...
    
    @staticmethod
    @overload
    def Dynamic(binder: CallSiteBinder, returnType: TypeType, arguments: IEnumerable[Expression]) -> DynamicExpression: ...
    
    @staticmethod
    @overload
    def Dynamic(binder: CallSiteBinder, returnType: TypeType, arg0: Expression) -> DynamicExpression: ...
    
    @staticmethod
    @overload
    def Dynamic(binder: CallSiteBinder, returnType: TypeType, arg0: Expression, arg1: Expression) -> DynamicExpression: ...
    
    @staticmethod
    @overload
    def Dynamic(binder: CallSiteBinder, returnType: TypeType, arg0: Expression, arg1: Expression, arg2: Expression) -> DynamicExpression: ...
    
    @staticmethod
    @overload
    def Dynamic(binder: CallSiteBinder, returnType: TypeType, arg0: Expression, arg1: Expression, arg2: Expression, arg3: Expression) -> DynamicExpression: ...
    
    @staticmethod
    @overload
    def MakeDynamic(delegateType: TypeType, binder: CallSiteBinder, arguments: IEnumerable[Expression]) -> DynamicExpression: ...
    
    @staticmethod
    @overload
    def MakeDynamic(delegateType: TypeType, binder: CallSiteBinder, arguments: ArrayType[Expression]) -> DynamicExpression: ...
    
    @staticmethod
    @overload
    def MakeDynamic(delegateType: TypeType, binder: CallSiteBinder, arg0: Expression) -> DynamicExpression: ...
    
    @staticmethod
    @overload
    def MakeDynamic(delegateType: TypeType, binder: CallSiteBinder, arg0: Expression, arg1: Expression) -> DynamicExpression: ...
    
    @staticmethod
    @overload
    def MakeDynamic(delegateType: TypeType, binder: CallSiteBinder, arg0: Expression, arg1: Expression, arg2: Expression) -> DynamicExpression: ...
    
    @staticmethod
    @overload
    def MakeDynamic(delegateType: TypeType, binder: CallSiteBinder, arg0: Expression, arg1: Expression, arg2: Expression, arg3: Expression) -> DynamicExpression: ...
    
    def Update(self, arguments: IEnumerable[Expression]) -> DynamicExpression: ...
    
    def get_Arguments(self) -> ReadOnlyCollection[Expression]: ...
    
    def get_Binder(self) -> CallSiteBinder: ...
    
    def get_DelegateType(self) -> TypeType: ...
    
    def get_NodeType(self) -> ExpressionType: ...
    
    def get_Type(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DynamicExpression1(DynamicExpression, IDynamicExpression, IArgumentProvider):
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


class DynamicExpression2(DynamicExpression, IDynamicExpression, IArgumentProvider):
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


class DynamicExpression3(DynamicExpression, IDynamicExpression, IArgumentProvider):
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


class DynamicExpression4(DynamicExpression, IDynamicExpression, IArgumentProvider):
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


class DynamicExpressionN(DynamicExpression, IDynamicExpression, IArgumentProvider):
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


class DynamicExpressionVisitor(ABC, ExpressionVisitor):
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


class ElementInit(ObjectType, IArgumentProvider):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def AddMethod(self) -> MethodInfo: ...
    
    @property
    def Arguments(self) -> ReadOnlyCollection[Expression]: ...
    
    # ---------- Methods ---------- #
    
    def ToString(self) -> StringType: ...
    
    def Update(self, arguments: IEnumerable[Expression]) -> ElementInit: ...
    
    def get_AddMethod(self) -> MethodInfo: ...
    
    def get_Arguments(self) -> ReadOnlyCollection[Expression]: ...
    
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


class Expression(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def CanReduce(self) -> BooleanType: ...
    
    @property
    def NodeType(self) -> ExpressionType: ...
    
    @property
    def Type(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    @overload
    def Add(left: Expression, right: Expression) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def Add(left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def AddAssign(left: Expression, right: Expression) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def AddAssign(left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def AddAssign(left: Expression, right: Expression, method: MethodInfo, conversion: LambdaExpression) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def AddAssignChecked(left: Expression, right: Expression) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def AddAssignChecked(left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def AddAssignChecked(left: Expression, right: Expression, method: MethodInfo, conversion: LambdaExpression) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def AddChecked(left: Expression, right: Expression) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def AddChecked(left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def And(left: Expression, right: Expression) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def And(left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def AndAlso(left: Expression, right: Expression) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def AndAlso(left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def AndAssign(left: Expression, right: Expression) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def AndAssign(left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def AndAssign(left: Expression, right: Expression, method: MethodInfo, conversion: LambdaExpression) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def ArrayAccess(array: Expression, indexes: ArrayType[Expression]) -> IndexExpression: ...
    
    @staticmethod
    @overload
    def ArrayAccess(array: Expression, indexes: IEnumerable[Expression]) -> IndexExpression: ...
    
    @staticmethod
    @overload
    def ArrayIndex(array: Expression, indexes: ArrayType[Expression]) -> MethodCallExpression: ...
    
    @staticmethod
    @overload
    def ArrayIndex(array: Expression, index: Expression) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def ArrayIndex(array: Expression, indexes: IEnumerable[Expression]) -> MethodCallExpression: ...
    
    @staticmethod
    def ArrayLength(array: Expression) -> UnaryExpression: ...
    
    @staticmethod
    def Assign(left: Expression, right: Expression) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def Bind(propertyAccessor: MethodInfo, expression: Expression) -> MemberAssignment: ...
    
    @staticmethod
    @overload
    def Bind(member: MemberInfo, expression: Expression) -> MemberAssignment: ...
    
    @staticmethod
    @overload
    def Block(expressions: IEnumerable[Expression]) -> BlockExpression: ...
    
    @staticmethod
    @overload
    def Block(type: TypeType, expressions: ArrayType[Expression]) -> BlockExpression: ...
    
    @staticmethod
    @overload
    def Block(type: TypeType, expressions: IEnumerable[Expression]) -> BlockExpression: ...
    
    @staticmethod
    @overload
    def Block(variables: IEnumerable[ParameterExpression], expressions: ArrayType[Expression]) -> BlockExpression: ...
    
    @staticmethod
    @overload
    def Block(type: TypeType, variables: IEnumerable[ParameterExpression], expressions: ArrayType[Expression]) -> BlockExpression: ...
    
    @staticmethod
    @overload
    def Block(arg0: Expression, arg1: Expression) -> BlockExpression: ...
    
    @staticmethod
    @overload
    def Block(arg0: Expression, arg1: Expression, arg2: Expression) -> BlockExpression: ...
    
    @staticmethod
    @overload
    def Block(arg0: Expression, arg1: Expression, arg2: Expression, arg3: Expression) -> BlockExpression: ...
    
    @staticmethod
    @overload
    def Block(arg0: Expression, arg1: Expression, arg2: Expression, arg3: Expression, arg4: Expression) -> BlockExpression: ...
    
    @staticmethod
    @overload
    def Block(expressions: ArrayType[Expression]) -> BlockExpression: ...
    
    @staticmethod
    @overload
    def Block(variables: IEnumerable[ParameterExpression], expressions: IEnumerable[Expression]) -> BlockExpression: ...
    
    @staticmethod
    @overload
    def Block(type: TypeType, variables: IEnumerable[ParameterExpression], expressions: IEnumerable[Expression]) -> BlockExpression: ...
    
    @staticmethod
    @overload
    def Break(target: LabelTarget) -> GotoExpression: ...
    
    @staticmethod
    @overload
    def Break(target: LabelTarget, value: Expression) -> GotoExpression: ...
    
    @staticmethod
    @overload
    def Break(target: LabelTarget, type: TypeType) -> GotoExpression: ...
    
    @staticmethod
    @overload
    def Break(target: LabelTarget, value: Expression, type: TypeType) -> GotoExpression: ...
    
    @staticmethod
    @overload
    def Call(method: MethodInfo, arg0: Expression) -> MethodCallExpression: ...
    
    @staticmethod
    @overload
    def Call(method: MethodInfo, arg0: Expression, arg1: Expression) -> MethodCallExpression: ...
    
    @staticmethod
    @overload
    def Call(method: MethodInfo, arg0: Expression, arg1: Expression, arg2: Expression) -> MethodCallExpression: ...
    
    @staticmethod
    @overload
    def Call(method: MethodInfo, arg0: Expression, arg1: Expression, arg2: Expression, arg3: Expression) -> MethodCallExpression: ...
    
    @staticmethod
    @overload
    def Call(method: MethodInfo, arg0: Expression, arg1: Expression, arg2: Expression, arg3: Expression, arg4: Expression) -> MethodCallExpression: ...
    
    @staticmethod
    @overload
    def Call(method: MethodInfo, arguments: ArrayType[Expression]) -> MethodCallExpression: ...
    
    @staticmethod
    @overload
    def Call(method: MethodInfo, arguments: IEnumerable[Expression]) -> MethodCallExpression: ...
    
    @staticmethod
    @overload
    def Call(instance: Expression, method: MethodInfo) -> MethodCallExpression: ...
    
    @staticmethod
    @overload
    def Call(instance: Expression, method: MethodInfo, arguments: ArrayType[Expression]) -> MethodCallExpression: ...
    
    @staticmethod
    @overload
    def Call(instance: Expression, method: MethodInfo, arg0: Expression, arg1: Expression) -> MethodCallExpression: ...
    
    @staticmethod
    @overload
    def Call(instance: Expression, method: MethodInfo, arg0: Expression, arg1: Expression, arg2: Expression) -> MethodCallExpression: ...
    
    @staticmethod
    @overload
    def Call(instance: Expression, method: MethodInfo, arguments: IEnumerable[Expression]) -> MethodCallExpression: ...
    
    @staticmethod
    @overload
    def Call(instance: Expression, methodName: StringType, typeArguments: ArrayType[TypeType], arguments: ArrayType[Expression]) -> MethodCallExpression: ...
    
    @staticmethod
    @overload
    def Call(type: TypeType, methodName: StringType, typeArguments: ArrayType[TypeType], arguments: ArrayType[Expression]) -> MethodCallExpression: ...
    
    @staticmethod
    @overload
    def Catch(type: TypeType, body: Expression) -> CatchBlock: ...
    
    @staticmethod
    @overload
    def Catch(variable: ParameterExpression, body: Expression) -> CatchBlock: ...
    
    @staticmethod
    @overload
    def Catch(type: TypeType, body: Expression, filter: Expression) -> CatchBlock: ...
    
    @staticmethod
    @overload
    def Catch(variable: ParameterExpression, body: Expression, filter: Expression) -> CatchBlock: ...
    
    @staticmethod
    def ClearDebugInfo(document: SymbolDocumentInfo) -> DebugInfoExpression: ...
    
    @staticmethod
    @overload
    def Coalesce(left: Expression, right: Expression) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def Coalesce(left: Expression, right: Expression, conversion: LambdaExpression) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def Condition(test: Expression, ifTrue: Expression, ifFalse: Expression) -> ConditionalExpression: ...
    
    @staticmethod
    @overload
    def Condition(test: Expression, ifTrue: Expression, ifFalse: Expression, type: TypeType) -> ConditionalExpression: ...
    
    @staticmethod
    @overload
    def Constant(value: ObjectType) -> ConstantExpression: ...
    
    @staticmethod
    @overload
    def Constant(value: ObjectType, type: TypeType) -> ConstantExpression: ...
    
    @staticmethod
    @overload
    def Continue(target: LabelTarget) -> GotoExpression: ...
    
    @staticmethod
    @overload
    def Continue(target: LabelTarget, type: TypeType) -> GotoExpression: ...
    
    @staticmethod
    @overload
    def Convert(expression: Expression, type: TypeType) -> UnaryExpression: ...
    
    @staticmethod
    @overload
    def Convert(expression: Expression, type: TypeType, method: MethodInfo) -> UnaryExpression: ...
    
    @staticmethod
    @overload
    def ConvertChecked(expression: Expression, type: TypeType) -> UnaryExpression: ...
    
    @staticmethod
    @overload
    def ConvertChecked(expression: Expression, type: TypeType, method: MethodInfo) -> UnaryExpression: ...
    
    @staticmethod
    def DebugInfo(document: SymbolDocumentInfo, startLine: IntType, startColumn: IntType, endLine: IntType, endColumn: IntType) -> DebugInfoExpression: ...
    
    @staticmethod
    @overload
    def Decrement(expression: Expression) -> UnaryExpression: ...
    
    @staticmethod
    @overload
    def Decrement(expression: Expression, method: MethodInfo) -> UnaryExpression: ...
    
    @staticmethod
    def Default(type: TypeType) -> DefaultExpression: ...
    
    @staticmethod
    @overload
    def Divide(left: Expression, right: Expression) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def Divide(left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def DivideAssign(left: Expression, right: Expression) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def DivideAssign(left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def DivideAssign(left: Expression, right: Expression, method: MethodInfo, conversion: LambdaExpression) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def Dynamic(binder: CallSiteBinder, returnType: TypeType, arguments: ArrayType[Expression]) -> DynamicExpression: ...
    
    @staticmethod
    @overload
    def Dynamic(binder: CallSiteBinder, returnType: TypeType, arg0: Expression) -> DynamicExpression: ...
    
    @staticmethod
    @overload
    def Dynamic(binder: CallSiteBinder, returnType: TypeType, arg0: Expression, arg1: Expression) -> DynamicExpression: ...
    
    @staticmethod
    @overload
    def Dynamic(binder: CallSiteBinder, returnType: TypeType, arg0: Expression, arg1: Expression, arg2: Expression) -> DynamicExpression: ...
    
    @staticmethod
    @overload
    def Dynamic(binder: CallSiteBinder, returnType: TypeType, arg0: Expression, arg1: Expression, arg2: Expression, arg3: Expression) -> DynamicExpression: ...
    
    @staticmethod
    @overload
    def Dynamic(binder: CallSiteBinder, returnType: TypeType, arguments: IEnumerable[Expression]) -> DynamicExpression: ...
    
    @staticmethod
    @overload
    def ElementInit(addMethod: MethodInfo, arguments: ArrayType[Expression]) -> ElementInit: ...
    
    @staticmethod
    @overload
    def ElementInit(addMethod: MethodInfo, arguments: IEnumerable[Expression]) -> ElementInit: ...
    
    @staticmethod
    def Empty() -> DefaultExpression: ...
    
    @staticmethod
    @overload
    def Equal(left: Expression, right: Expression) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def Equal(left: Expression, right: Expression, liftToNull: BooleanType, method: MethodInfo) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def ExclusiveOr(left: Expression, right: Expression) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def ExclusiveOr(left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def ExclusiveOrAssign(left: Expression, right: Expression) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def ExclusiveOrAssign(left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def ExclusiveOrAssign(left: Expression, right: Expression, method: MethodInfo, conversion: LambdaExpression) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def Field(expression: Expression, type: TypeType, fieldName: StringType) -> MemberExpression: ...
    
    @staticmethod
    @overload
    def Field(expression: Expression, fieldName: StringType) -> MemberExpression: ...
    
    @staticmethod
    @overload
    def Field(expression: Expression, field: FieldInfo) -> MemberExpression: ...
    
    @staticmethod
    def GetActionType(typeArgs: ArrayType[TypeType]) -> TypeType: ...
    
    @staticmethod
    def GetDelegateType(typeArgs: ArrayType[TypeType]) -> TypeType: ...
    
    @staticmethod
    def GetFuncType(typeArgs: ArrayType[TypeType]) -> TypeType: ...
    
    @staticmethod
    @overload
    def Goto(target: LabelTarget) -> GotoExpression: ...
    
    @staticmethod
    @overload
    def Goto(target: LabelTarget, type: TypeType) -> GotoExpression: ...
    
    @staticmethod
    @overload
    def Goto(target: LabelTarget, value: Expression) -> GotoExpression: ...
    
    @staticmethod
    @overload
    def Goto(target: LabelTarget, value: Expression, type: TypeType) -> GotoExpression: ...
    
    @staticmethod
    @overload
    def GreaterThan(left: Expression, right: Expression) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def GreaterThan(left: Expression, right: Expression, liftToNull: BooleanType, method: MethodInfo) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def GreaterThanOrEqual(left: Expression, right: Expression) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def GreaterThanOrEqual(left: Expression, right: Expression, liftToNull: BooleanType, method: MethodInfo) -> BinaryExpression: ...
    
    @staticmethod
    def IfThen(test: Expression, ifTrue: Expression) -> ConditionalExpression: ...
    
    @staticmethod
    def IfThenElse(test: Expression, ifTrue: Expression, ifFalse: Expression) -> ConditionalExpression: ...
    
    @staticmethod
    @overload
    def Increment(expression: Expression) -> UnaryExpression: ...
    
    @staticmethod
    @overload
    def Increment(expression: Expression, method: MethodInfo) -> UnaryExpression: ...
    
    @staticmethod
    @overload
    def Invoke(expression: Expression, arguments: ArrayType[Expression]) -> InvocationExpression: ...
    
    @staticmethod
    @overload
    def Invoke(expression: Expression, arguments: IEnumerable[Expression]) -> InvocationExpression: ...
    
    @staticmethod
    @overload
    def IsFalse(expression: Expression) -> UnaryExpression: ...
    
    @staticmethod
    @overload
    def IsFalse(expression: Expression, method: MethodInfo) -> UnaryExpression: ...
    
    @staticmethod
    @overload
    def IsTrue(expression: Expression) -> UnaryExpression: ...
    
    @staticmethod
    @overload
    def IsTrue(expression: Expression, method: MethodInfo) -> UnaryExpression: ...
    
    @staticmethod
    @overload
    def Label(target: LabelTarget) -> LabelExpression: ...
    
    @staticmethod
    @overload
    def Label() -> LabelTarget: ...
    
    @staticmethod
    @overload
    def Label(name: StringType) -> LabelTarget: ...
    
    @staticmethod
    @overload
    def Label(type: TypeType) -> LabelTarget: ...
    
    @staticmethod
    @overload
    def Label(type: TypeType, name: StringType) -> LabelTarget: ...
    
    @staticmethod
    @overload
    def Label(target: LabelTarget, defaultValue: Expression) -> LabelExpression: ...
    
    @staticmethod
    @overload
    def Lambda(body: Expression, parameters: ArrayType[ParameterExpression]) -> LambdaExpression: ...
    
    @staticmethod
    @overload
    def Lambda(body: Expression, tailCall: BooleanType, parameters: ArrayType[ParameterExpression]) -> LambdaExpression: ...
    
    @staticmethod
    @overload
    def Lambda(body: Expression, parameters: IEnumerable[ParameterExpression]) -> LambdaExpression: ...
    
    @staticmethod
    @overload
    def Lambda(body: Expression, tailCall: BooleanType, parameters: IEnumerable[ParameterExpression]) -> LambdaExpression: ...
    
    @staticmethod
    @overload
    def Lambda(delegateType: TypeType, body: Expression, parameters: ArrayType[ParameterExpression]) -> LambdaExpression: ...
    
    @staticmethod
    @overload
    def Lambda(delegateType: TypeType, body: Expression, tailCall: BooleanType, parameters: ArrayType[ParameterExpression]) -> LambdaExpression: ...
    
    @staticmethod
    @overload
    def Lambda(delegateType: TypeType, body: Expression, parameters: IEnumerable[ParameterExpression]) -> LambdaExpression: ...
    
    @staticmethod
    @overload
    def Lambda(delegateType: TypeType, body: Expression, tailCall: BooleanType, parameters: IEnumerable[ParameterExpression]) -> LambdaExpression: ...
    
    @staticmethod
    @overload
    def Lambda(body: Expression, name: StringType, parameters: IEnumerable[ParameterExpression]) -> LambdaExpression: ...
    
    @staticmethod
    @overload
    def Lambda(delegateType: TypeType, body: Expression, name: StringType, parameters: IEnumerable[ParameterExpression]) -> LambdaExpression: ...
    
    @staticmethod
    @overload
    def Lambda(delegateType: TypeType, body: Expression, name: StringType, tailCall: BooleanType, parameters: IEnumerable[ParameterExpression]) -> LambdaExpression: ...
    
    @staticmethod
    @overload
    def Lambda(body: Expression, parameters: ArrayType[ParameterExpression]) -> Expression[TDelegate]: ...
    
    @staticmethod
    @overload
    def Lambda(body: Expression, tailCall: BooleanType, parameters: ArrayType[ParameterExpression]) -> Expression[TDelegate]: ...
    
    @staticmethod
    @overload
    def Lambda(body: Expression, parameters: IEnumerable[ParameterExpression]) -> Expression[TDelegate]: ...
    
    @staticmethod
    @overload
    def Lambda(body: Expression, tailCall: BooleanType, parameters: IEnumerable[ParameterExpression]) -> Expression[TDelegate]: ...
    
    @staticmethod
    @overload
    def Lambda(body: Expression, name: StringType, parameters: IEnumerable[ParameterExpression]) -> Expression[TDelegate]: ...
    
    @staticmethod
    @overload
    def Lambda(body: Expression, name: StringType, tailCall: BooleanType, parameters: IEnumerable[ParameterExpression]) -> Expression[TDelegate]: ...
    
    @staticmethod
    @overload
    def Lambda(body: Expression, name: StringType, tailCall: BooleanType, parameters: IEnumerable[ParameterExpression]) -> LambdaExpression: ...
    
    @staticmethod
    @overload
    def LeftShift(left: Expression, right: Expression) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def LeftShift(left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def LeftShiftAssign(left: Expression, right: Expression) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def LeftShiftAssign(left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def LeftShiftAssign(left: Expression, right: Expression, method: MethodInfo, conversion: LambdaExpression) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def LessThan(left: Expression, right: Expression) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def LessThan(left: Expression, right: Expression, liftToNull: BooleanType, method: MethodInfo) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def LessThanOrEqual(left: Expression, right: Expression) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def LessThanOrEqual(left: Expression, right: Expression, liftToNull: BooleanType, method: MethodInfo) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def ListBind(member: MemberInfo, initializers: ArrayType[ElementInit]) -> MemberListBinding: ...
    
    @staticmethod
    @overload
    def ListBind(member: MemberInfo, initializers: IEnumerable[ElementInit]) -> MemberListBinding: ...
    
    @staticmethod
    @overload
    def ListBind(propertyAccessor: MethodInfo, initializers: ArrayType[ElementInit]) -> MemberListBinding: ...
    
    @staticmethod
    @overload
    def ListBind(propertyAccessor: MethodInfo, initializers: IEnumerable[ElementInit]) -> MemberListBinding: ...
    
    @staticmethod
    @overload
    def ListInit(newExpression: NewExpression, initializers: ArrayType[Expression]) -> ListInitExpression: ...
    
    @staticmethod
    @overload
    def ListInit(newExpression: NewExpression, addMethod: MethodInfo, initializers: ArrayType[Expression]) -> ListInitExpression: ...
    
    @staticmethod
    @overload
    def ListInit(newExpression: NewExpression, initializers: ArrayType[ElementInit]) -> ListInitExpression: ...
    
    @staticmethod
    @overload
    def ListInit(newExpression: NewExpression, initializers: IEnumerable[ElementInit]) -> ListInitExpression: ...
    
    @staticmethod
    @overload
    def ListInit(newExpression: NewExpression, initializers: IEnumerable[Expression]) -> ListInitExpression: ...
    
    @staticmethod
    @overload
    def ListInit(newExpression: NewExpression, addMethod: MethodInfo, initializers: IEnumerable[Expression]) -> ListInitExpression: ...
    
    @staticmethod
    @overload
    def Loop(body: Expression) -> LoopExpression: ...
    
    @staticmethod
    @overload
    def Loop(body: Expression, _break: LabelTarget) -> LoopExpression: ...
    
    @staticmethod
    @overload
    def Loop(body: Expression, _break: LabelTarget, _continue: LabelTarget) -> LoopExpression: ...
    
    @staticmethod
    @overload
    def MakeBinary(binaryType: ExpressionType, left: Expression, right: Expression) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def MakeBinary(binaryType: ExpressionType, left: Expression, right: Expression, liftToNull: BooleanType, method: MethodInfo) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def MakeBinary(binaryType: ExpressionType, left: Expression, right: Expression, liftToNull: BooleanType, method: MethodInfo, conversion: LambdaExpression) -> BinaryExpression: ...
    
    @staticmethod
    def MakeCatchBlock(type: TypeType, variable: ParameterExpression, body: Expression, filter: Expression) -> CatchBlock: ...
    
    @staticmethod
    @overload
    def MakeDynamic(delegateType: TypeType, binder: CallSiteBinder, arguments: ArrayType[Expression]) -> DynamicExpression: ...
    
    @staticmethod
    @overload
    def MakeDynamic(delegateType: TypeType, binder: CallSiteBinder, arguments: IEnumerable[Expression]) -> DynamicExpression: ...
    
    @staticmethod
    @overload
    def MakeDynamic(delegateType: TypeType, binder: CallSiteBinder, arg0: Expression) -> DynamicExpression: ...
    
    @staticmethod
    @overload
    def MakeDynamic(delegateType: TypeType, binder: CallSiteBinder, arg0: Expression, arg1: Expression) -> DynamicExpression: ...
    
    @staticmethod
    @overload
    def MakeDynamic(delegateType: TypeType, binder: CallSiteBinder, arg0: Expression, arg1: Expression, arg2: Expression) -> DynamicExpression: ...
    
    @staticmethod
    @overload
    def MakeDynamic(delegateType: TypeType, binder: CallSiteBinder, arg0: Expression, arg1: Expression, arg2: Expression, arg3: Expression) -> DynamicExpression: ...
    
    @staticmethod
    def MakeGoto(kind: GotoExpressionKind, target: LabelTarget, value: Expression, type: TypeType) -> GotoExpression: ...
    
    @staticmethod
    def MakeIndex(instance: Expression, indexer: PropertyInfo, arguments: IEnumerable[Expression]) -> IndexExpression: ...
    
    @staticmethod
    def MakeMemberAccess(expression: Expression, member: MemberInfo) -> MemberExpression: ...
    
    @staticmethod
    def MakeTry(type: TypeType, body: Expression, _finally: Expression, fault: Expression, handlers: IEnumerable[CatchBlock]) -> TryExpression: ...
    
    @staticmethod
    @overload
    def MakeUnary(unaryType: ExpressionType, operand: Expression, type: TypeType) -> UnaryExpression: ...
    
    @staticmethod
    @overload
    def MakeUnary(unaryType: ExpressionType, operand: Expression, type: TypeType, method: MethodInfo) -> UnaryExpression: ...
    
    @staticmethod
    @overload
    def MemberBind(member: MemberInfo, bindings: ArrayType[MemberBinding]) -> MemberMemberBinding: ...
    
    @staticmethod
    @overload
    def MemberBind(member: MemberInfo, bindings: IEnumerable[MemberBinding]) -> MemberMemberBinding: ...
    
    @staticmethod
    @overload
    def MemberBind(propertyAccessor: MethodInfo, bindings: ArrayType[MemberBinding]) -> MemberMemberBinding: ...
    
    @staticmethod
    @overload
    def MemberBind(propertyAccessor: MethodInfo, bindings: IEnumerable[MemberBinding]) -> MemberMemberBinding: ...
    
    @staticmethod
    @overload
    def MemberInit(newExpression: NewExpression, bindings: ArrayType[MemberBinding]) -> MemberInitExpression: ...
    
    @staticmethod
    @overload
    def MemberInit(newExpression: NewExpression, bindings: IEnumerable[MemberBinding]) -> MemberInitExpression: ...
    
    @staticmethod
    @overload
    def Modulo(left: Expression, right: Expression) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def Modulo(left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def ModuloAssign(left: Expression, right: Expression) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def ModuloAssign(left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def ModuloAssign(left: Expression, right: Expression, method: MethodInfo, conversion: LambdaExpression) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def Multiply(left: Expression, right: Expression) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def Multiply(left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def MultiplyAssign(left: Expression, right: Expression) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def MultiplyAssign(left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def MultiplyAssign(left: Expression, right: Expression, method: MethodInfo, conversion: LambdaExpression) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def MultiplyAssignChecked(left: Expression, right: Expression) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def MultiplyAssignChecked(left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def MultiplyAssignChecked(left: Expression, right: Expression, method: MethodInfo, conversion: LambdaExpression) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def MultiplyChecked(left: Expression, right: Expression) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def MultiplyChecked(left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def Negate(expression: Expression) -> UnaryExpression: ...
    
    @staticmethod
    @overload
    def Negate(expression: Expression, method: MethodInfo) -> UnaryExpression: ...
    
    @staticmethod
    @overload
    def NegateChecked(expression: Expression) -> UnaryExpression: ...
    
    @staticmethod
    @overload
    def NegateChecked(expression: Expression, method: MethodInfo) -> UnaryExpression: ...
    
    @staticmethod
    @overload
    def New(constructor: ConstructorInfo) -> NewExpression: ...
    
    @staticmethod
    @overload
    def New(constructor: ConstructorInfo, arguments: ArrayType[Expression]) -> NewExpression: ...
    
    @staticmethod
    @overload
    def New(constructor: ConstructorInfo, arguments: IEnumerable[Expression]) -> NewExpression: ...
    
    @staticmethod
    @overload
    def New(constructor: ConstructorInfo, arguments: IEnumerable[Expression], members: IEnumerable[MemberInfo]) -> NewExpression: ...
    
    @staticmethod
    @overload
    def New(constructor: ConstructorInfo, arguments: IEnumerable[Expression], members: ArrayType[MemberInfo]) -> NewExpression: ...
    
    @staticmethod
    @overload
    def New(type: TypeType) -> NewExpression: ...
    
    @staticmethod
    @overload
    def NewArrayBounds(type: TypeType, bounds: ArrayType[Expression]) -> NewArrayExpression: ...
    
    @staticmethod
    @overload
    def NewArrayBounds(type: TypeType, bounds: IEnumerable[Expression]) -> NewArrayExpression: ...
    
    @staticmethod
    @overload
    def NewArrayInit(type: TypeType, initializers: ArrayType[Expression]) -> NewArrayExpression: ...
    
    @staticmethod
    @overload
    def NewArrayInit(type: TypeType, initializers: IEnumerable[Expression]) -> NewArrayExpression: ...
    
    @staticmethod
    @overload
    def Not(expression: Expression) -> UnaryExpression: ...
    
    @staticmethod
    @overload
    def Not(expression: Expression, method: MethodInfo) -> UnaryExpression: ...
    
    @staticmethod
    @overload
    def NotEqual(left: Expression, right: Expression) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def NotEqual(left: Expression, right: Expression, liftToNull: BooleanType, method: MethodInfo) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def OnesComplement(expression: Expression) -> UnaryExpression: ...
    
    @staticmethod
    @overload
    def OnesComplement(expression: Expression, method: MethodInfo) -> UnaryExpression: ...
    
    @staticmethod
    @overload
    def Or(left: Expression, right: Expression) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def Or(left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def OrAssign(left: Expression, right: Expression) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def OrAssign(left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def OrAssign(left: Expression, right: Expression, method: MethodInfo, conversion: LambdaExpression) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def OrElse(left: Expression, right: Expression) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def OrElse(left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def Parameter(type: TypeType) -> ParameterExpression: ...
    
    @staticmethod
    @overload
    def Parameter(type: TypeType, name: StringType) -> ParameterExpression: ...
    
    @staticmethod
    @overload
    def PostDecrementAssign(expression: Expression) -> UnaryExpression: ...
    
    @staticmethod
    @overload
    def PostDecrementAssign(expression: Expression, method: MethodInfo) -> UnaryExpression: ...
    
    @staticmethod
    @overload
    def PostIncrementAssign(expression: Expression) -> UnaryExpression: ...
    
    @staticmethod
    @overload
    def PostIncrementAssign(expression: Expression, method: MethodInfo) -> UnaryExpression: ...
    
    @staticmethod
    @overload
    def Power(left: Expression, right: Expression) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def Power(left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def PowerAssign(left: Expression, right: Expression) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def PowerAssign(left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def PowerAssign(left: Expression, right: Expression, method: MethodInfo, conversion: LambdaExpression) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def PreDecrementAssign(expression: Expression) -> UnaryExpression: ...
    
    @staticmethod
    @overload
    def PreDecrementAssign(expression: Expression, method: MethodInfo) -> UnaryExpression: ...
    
    @staticmethod
    @overload
    def PreIncrementAssign(expression: Expression) -> UnaryExpression: ...
    
    @staticmethod
    @overload
    def PreIncrementAssign(expression: Expression, method: MethodInfo) -> UnaryExpression: ...
    
    @staticmethod
    @overload
    def Property(instance: Expression, indexer: PropertyInfo, arguments: ArrayType[Expression]) -> IndexExpression: ...
    
    @staticmethod
    @overload
    def Property(instance: Expression, indexer: PropertyInfo, arguments: IEnumerable[Expression]) -> IndexExpression: ...
    
    @staticmethod
    @overload
    def Property(expression: Expression, type: TypeType, propertyName: StringType) -> MemberExpression: ...
    
    @staticmethod
    @overload
    def Property(expression: Expression, propertyAccessor: MethodInfo) -> MemberExpression: ...
    
    @staticmethod
    @overload
    def Property(instance: Expression, propertyName: StringType, arguments: ArrayType[Expression]) -> IndexExpression: ...
    
    @staticmethod
    @overload
    def Property(expression: Expression, propertyName: StringType) -> MemberExpression: ...
    
    @staticmethod
    @overload
    def Property(expression: Expression, property: PropertyInfo) -> MemberExpression: ...
    
    @staticmethod
    def PropertyOrField(expression: Expression, propertyOrFieldName: StringType) -> MemberExpression: ...
    
    @staticmethod
    def Quote(expression: Expression) -> UnaryExpression: ...
    
    def Reduce(self) -> Expression: ...
    
    def ReduceAndCheck(self) -> Expression: ...
    
    def ReduceExtensions(self) -> Expression: ...
    
    @staticmethod
    def ReferenceEqual(left: Expression, right: Expression) -> BinaryExpression: ...
    
    @staticmethod
    def ReferenceNotEqual(left: Expression, right: Expression) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def Rethrow() -> UnaryExpression: ...
    
    @staticmethod
    @overload
    def Rethrow(type: TypeType) -> UnaryExpression: ...
    
    @staticmethod
    @overload
    def Return(target: LabelTarget) -> GotoExpression: ...
    
    @staticmethod
    @overload
    def Return(target: LabelTarget, type: TypeType) -> GotoExpression: ...
    
    @staticmethod
    @overload
    def Return(target: LabelTarget, value: Expression) -> GotoExpression: ...
    
    @staticmethod
    @overload
    def Return(target: LabelTarget, value: Expression, type: TypeType) -> GotoExpression: ...
    
    @staticmethod
    @overload
    def RightShift(left: Expression, right: Expression) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def RightShift(left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def RightShiftAssign(left: Expression, right: Expression) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def RightShiftAssign(left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def RightShiftAssign(left: Expression, right: Expression, method: MethodInfo, conversion: LambdaExpression) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def RuntimeVariables(variables: ArrayType[ParameterExpression]) -> RuntimeVariablesExpression: ...
    
    @staticmethod
    @overload
    def RuntimeVariables(variables: IEnumerable[ParameterExpression]) -> RuntimeVariablesExpression: ...
    
    @staticmethod
    @overload
    def Subtract(left: Expression, right: Expression) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def Subtract(left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def SubtractAssign(left: Expression, right: Expression) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def SubtractAssign(left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def SubtractAssign(left: Expression, right: Expression, method: MethodInfo, conversion: LambdaExpression) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def SubtractAssignChecked(left: Expression, right: Expression) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def SubtractAssignChecked(left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def SubtractAssignChecked(left: Expression, right: Expression, method: MethodInfo, conversion: LambdaExpression) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def SubtractChecked(left: Expression, right: Expression) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def SubtractChecked(left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression: ...
    
    @staticmethod
    @overload
    def Switch(switchValue: Expression, cases: ArrayType[SwitchCase]) -> SwitchExpression: ...
    
    @staticmethod
    @overload
    def Switch(switchValue: Expression, defaultBody: Expression, cases: ArrayType[SwitchCase]) -> SwitchExpression: ...
    
    @staticmethod
    @overload
    def Switch(switchValue: Expression, defaultBody: Expression, comparison: MethodInfo, cases: ArrayType[SwitchCase]) -> SwitchExpression: ...
    
    @staticmethod
    @overload
    def Switch(type: TypeType, switchValue: Expression, defaultBody: Expression, comparison: MethodInfo, cases: ArrayType[SwitchCase]) -> SwitchExpression: ...
    
    @staticmethod
    @overload
    def Switch(switchValue: Expression, defaultBody: Expression, comparison: MethodInfo, cases: IEnumerable[SwitchCase]) -> SwitchExpression: ...
    
    @staticmethod
    @overload
    def Switch(type: TypeType, switchValue: Expression, defaultBody: Expression, comparison: MethodInfo, cases: IEnumerable[SwitchCase]) -> SwitchExpression: ...
    
    @staticmethod
    @overload
    def SwitchCase(body: Expression, testValues: ArrayType[Expression]) -> SwitchCase: ...
    
    @staticmethod
    @overload
    def SwitchCase(body: Expression, testValues: IEnumerable[Expression]) -> SwitchCase: ...
    
    @staticmethod
    @overload
    def SymbolDocument(fileName: StringType) -> SymbolDocumentInfo: ...
    
    @staticmethod
    @overload
    def SymbolDocument(fileName: StringType, language: Guid) -> SymbolDocumentInfo: ...
    
    @staticmethod
    @overload
    def SymbolDocument(fileName: StringType, language: Guid, languageVendor: Guid) -> SymbolDocumentInfo: ...
    
    @staticmethod
    @overload
    def SymbolDocument(fileName: StringType, language: Guid, languageVendor: Guid, documentType: Guid) -> SymbolDocumentInfo: ...
    
    @staticmethod
    @overload
    def Throw(value: Expression) -> UnaryExpression: ...
    
    @staticmethod
    @overload
    def Throw(value: Expression, type: TypeType) -> UnaryExpression: ...
    
    def ToString(self) -> StringType: ...
    
    @staticmethod
    def TryCatch(body: Expression, handlers: ArrayType[CatchBlock]) -> TryExpression: ...
    
    @staticmethod
    def TryCatchFinally(body: Expression, _finally: Expression, handlers: ArrayType[CatchBlock]) -> TryExpression: ...
    
    @staticmethod
    def TryFault(body: Expression, fault: Expression) -> TryExpression: ...
    
    @staticmethod
    def TryFinally(body: Expression, _finally: Expression) -> TryExpression: ...
    
    @staticmethod
    def TryGetActionType(typeArgs: ArrayType[TypeType], actionType: TypeType) -> Tuple[BooleanType, TypeType]: ...
    
    @staticmethod
    def TryGetFuncType(typeArgs: ArrayType[TypeType], funcType: TypeType) -> Tuple[BooleanType, TypeType]: ...
    
    @staticmethod
    def TypeAs(expression: Expression, type: TypeType) -> UnaryExpression: ...
    
    @staticmethod
    def TypeEqual(expression: Expression, type: TypeType) -> TypeBinaryExpression: ...
    
    @staticmethod
    def TypeIs(expression: Expression, type: TypeType) -> TypeBinaryExpression: ...
    
    @staticmethod
    @overload
    def UnaryPlus(expression: Expression) -> UnaryExpression: ...
    
    @staticmethod
    @overload
    def UnaryPlus(expression: Expression, method: MethodInfo) -> UnaryExpression: ...
    
    @staticmethod
    def Unbox(expression: Expression, type: TypeType) -> UnaryExpression: ...
    
    @staticmethod
    @overload
    def Variable(type: TypeType) -> ParameterExpression: ...
    
    @staticmethod
    @overload
    def Variable(type: TypeType, name: StringType) -> ParameterExpression: ...
    
    def get_CanReduce(self) -> BooleanType: ...
    
    def get_NodeType(self) -> ExpressionType: ...
    
    def get_Type(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Expression(Generic[TDelegate], LambdaExpression):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def Compile(self) -> TDelegate: ...
    
    @overload
    def Compile(self, debugInfoGenerator: DebugInfoGenerator) -> TDelegate: ...
    
    @overload
    def Compile(self, preferInterpretation: BooleanType) -> TDelegate: ...
    
    def Update(self, body: Expression, parameters: IEnumerable[ParameterExpression]) -> Expression[TDelegate]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ExpressionStringBuilder(ExpressionVisitor):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def ToString(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ExpressionVisitor(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def Visit(self, nodes: ReadOnlyCollection[Expression]) -> ReadOnlyCollection[Expression]: ...
    
    @overload
    def Visit(self, node: Expression) -> Expression: ...
    
    @staticmethod
    @overload
    def Visit(nodes: ReadOnlyCollection[T], elementVisitor: Func[T, T]) -> ReadOnlyCollection[T]: ...
    
    @overload
    def VisitAndConvert(self, node: T, callerName: StringType) -> T: ...
    
    @overload
    def VisitAndConvert(self, nodes: ReadOnlyCollection[T], callerName: StringType) -> ReadOnlyCollection[T]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class FieldExpression(MemberExpression):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, expression: Expression, member: FieldInfo): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Type(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def get_Type(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class FullConditionalExpression(ConditionalExpression):
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


class FullConditionalExpressionWithType(FullConditionalExpression):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Type(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def get_Type(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class GotoExpression(Expression):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Kind(self) -> GotoExpressionKind: ...
    
    @property
    def NodeType(self) -> ExpressionType: ...
    
    @property
    def Target(self) -> LabelTarget: ...
    
    @property
    def Type(self) -> TypeType: ...
    
    @property
    def Value(self) -> Expression: ...
    
    # ---------- Methods ---------- #
    
    def Update(self, target: LabelTarget, value: Expression) -> GotoExpression: ...
    
    def get_Kind(self) -> GotoExpressionKind: ...
    
    def get_NodeType(self) -> ExpressionType: ...
    
    def get_Target(self) -> LabelTarget: ...
    
    def get_Type(self) -> TypeType: ...
    
    def get_Value(self) -> Expression: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IndexExpression(Expression, IArgumentProvider):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Arguments(self) -> ReadOnlyCollection[Expression]: ...
    
    @property
    def Indexer(self) -> PropertyInfo: ...
    
    @property
    def NodeType(self) -> ExpressionType: ...
    
    @property
    def Object(self) -> Expression: ...
    
    @property
    def Type(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def Update(self, object: Expression, arguments: IEnumerable[Expression]) -> IndexExpression: ...
    
    def get_Arguments(self) -> ReadOnlyCollection[Expression]: ...
    
    def get_Indexer(self) -> PropertyInfo: ...
    
    def get_NodeType(self) -> ExpressionType: ...
    
    def get_Object(self) -> Expression: ...
    
    def get_Type(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class InstanceMethodCallExpression2(MethodCallExpression, IArgumentProvider):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, method: MethodInfo, instance: Expression, arg0: Expression, arg1: Expression): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class InstanceMethodCallExpression3(MethodCallExpression, IArgumentProvider):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, method: MethodInfo, instance: Expression, arg0: Expression, arg1: Expression, arg2: Expression): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class InstanceMethodCallExpressionN(MethodCallExpression, IArgumentProvider):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, method: MethodInfo, instance: Expression, args: IList[Expression]): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class InvocationExpression(Expression, IArgumentProvider):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Arguments(self) -> ReadOnlyCollection[Expression]: ...
    
    @property
    def Expression(self) -> Expression: ...
    
    @property
    def NodeType(self) -> ExpressionType: ...
    
    @property
    def Type(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def Update(self, expression: Expression, arguments: IEnumerable[Expression]) -> InvocationExpression: ...
    
    def get_Arguments(self) -> ReadOnlyCollection[Expression]: ...
    
    def get_Expression(self) -> Expression: ...
    
    def get_NodeType(self) -> ExpressionType: ...
    
    def get_Type(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class LabelExpression(Expression):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def DefaultValue(self) -> Expression: ...
    
    @property
    def NodeType(self) -> ExpressionType: ...
    
    @property
    def Target(self) -> LabelTarget: ...
    
    @property
    def Type(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def Update(self, target: LabelTarget, defaultValue: Expression) -> LabelExpression: ...
    
    def get_DefaultValue(self) -> Expression: ...
    
    def get_NodeType(self) -> ExpressionType: ...
    
    def get_Target(self) -> LabelTarget: ...
    
    def get_Type(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class LabelTarget(ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def Type(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def ToString(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_Type(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class LambdaExpression(ABC, Expression):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Body(self) -> Expression: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def NodeType(self) -> ExpressionType: ...
    
    @property
    def Parameters(self) -> ReadOnlyCollection[ParameterExpression]: ...
    
    @property
    def ReturnType(self) -> TypeType: ...
    
    @property
    def TailCall(self) -> BooleanType: ...
    
    @property
    def Type(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Compile(self) -> Delegate: ...
    
    @overload
    def Compile(self, debugInfoGenerator: DebugInfoGenerator) -> Delegate: ...
    
    @overload
    def Compile(self, preferInterpretation: BooleanType) -> Delegate: ...
    
    @overload
    def CompileToMethod(self, method: MethodBuilder) -> VoidType: ...
    
    @overload
    def CompileToMethod(self, method: MethodBuilder, debugInfoGenerator: DebugInfoGenerator) -> VoidType: ...
    
    def get_Body(self) -> Expression: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_NodeType(self) -> ExpressionType: ...
    
    def get_Parameters(self) -> ReadOnlyCollection[ParameterExpression]: ...
    
    def get_ReturnType(self) -> TypeType: ...
    
    def get_TailCall(self) -> BooleanType: ...
    
    def get_Type(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ListArgumentProvider(ObjectType, IList[Expression], ICollection[Expression], IEnumerable[Expression], IEnumerable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def IsReadOnly(self) -> BooleanType: ...
    
    def __getitem__(self, key: IntType) -> Expression: ...
    
    def __setitem__(self, key: IntType, value: Expression) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, item: Expression) -> VoidType: ...
    
    def Clear(self) -> VoidType: ...
    
    def Contains(self, item: Expression) -> BooleanType: ...
    
    def CopyTo(self, array: ArrayType[Expression], arrayIndex: IntType) -> VoidType: ...
    
    def GetEnumerator(self) -> IEnumerator[Expression]: ...
    
    def IndexOf(self, item: Expression) -> IntType: ...
    
    def Insert(self, index: IntType, item: Expression) -> VoidType: ...
    
    def Remove(self, item: Expression) -> BooleanType: ...
    
    def RemoveAt(self, index: IntType) -> VoidType: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_IsReadOnly(self) -> BooleanType: ...
    
    def get_Item(self, index: IntType) -> Expression: ...
    
    def set_Item(self, index: IntType, value: Expression) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ListInitExpression(Expression):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def CanReduce(self) -> BooleanType: ...
    
    @property
    def Initializers(self) -> ReadOnlyCollection[ElementInit]: ...
    
    @property
    def NewExpression(self) -> NewExpression: ...
    
    @property
    def NodeType(self) -> ExpressionType: ...
    
    @property
    def Type(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def Reduce(self) -> Expression: ...
    
    def Update(self, newExpression: NewExpression, initializers: IEnumerable[ElementInit]) -> ListInitExpression: ...
    
    def get_CanReduce(self) -> BooleanType: ...
    
    def get_Initializers(self) -> ReadOnlyCollection[ElementInit]: ...
    
    def get_NewExpression(self) -> NewExpression: ...
    
    def get_NodeType(self) -> ExpressionType: ...
    
    def get_Type(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class LogicalBinaryExpression(BinaryExpression):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def NodeType(self) -> ExpressionType: ...
    
    @property
    def Type(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def get_NodeType(self) -> ExpressionType: ...
    
    def get_Type(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class LoopExpression(Expression):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Body(self) -> Expression: ...
    
    @property
    def BreakLabel(self) -> LabelTarget: ...
    
    @property
    def ContinueLabel(self) -> LabelTarget: ...
    
    @property
    def NodeType(self) -> ExpressionType: ...
    
    @property
    def Type(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def Update(self, breakLabel: LabelTarget, continueLabel: LabelTarget, body: Expression) -> LoopExpression: ...
    
    def get_Body(self) -> Expression: ...
    
    def get_BreakLabel(self) -> LabelTarget: ...
    
    def get_ContinueLabel(self) -> LabelTarget: ...
    
    def get_NodeType(self) -> ExpressionType: ...
    
    def get_Type(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MemberAssignment(MemberBinding):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Expression(self) -> Expression: ...
    
    # ---------- Methods ---------- #
    
    def Update(self, expression: Expression) -> MemberAssignment: ...
    
    def get_Expression(self) -> Expression: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MemberBinding(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def BindingType(self) -> MemberBindingType: ...
    
    @property
    def Member(self) -> MemberInfo: ...
    
    # ---------- Methods ---------- #
    
    def ToString(self) -> StringType: ...
    
    def get_BindingType(self) -> MemberBindingType: ...
    
    def get_Member(self) -> MemberInfo: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MemberExpression(Expression):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Expression(self) -> Expression: ...
    
    @property
    def Member(self) -> MemberInfo: ...
    
    @property
    def NodeType(self) -> ExpressionType: ...
    
    # ---------- Methods ---------- #
    
    def Update(self, expression: Expression) -> MemberExpression: ...
    
    def get_Expression(self) -> Expression: ...
    
    def get_Member(self) -> MemberInfo: ...
    
    def get_NodeType(self) -> ExpressionType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MemberInitExpression(Expression):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Bindings(self) -> ReadOnlyCollection[MemberBinding]: ...
    
    @property
    def CanReduce(self) -> BooleanType: ...
    
    @property
    def NewExpression(self) -> NewExpression: ...
    
    @property
    def NodeType(self) -> ExpressionType: ...
    
    @property
    def Type(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def Reduce(self) -> Expression: ...
    
    def Update(self, newExpression: NewExpression, bindings: IEnumerable[MemberBinding]) -> MemberInitExpression: ...
    
    def get_Bindings(self) -> ReadOnlyCollection[MemberBinding]: ...
    
    def get_CanReduce(self) -> BooleanType: ...
    
    def get_NewExpression(self) -> NewExpression: ...
    
    def get_NodeType(self) -> ExpressionType: ...
    
    def get_Type(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MemberListBinding(MemberBinding):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Initializers(self) -> ReadOnlyCollection[ElementInit]: ...
    
    # ---------- Methods ---------- #
    
    def Update(self, initializers: IEnumerable[ElementInit]) -> MemberListBinding: ...
    
    def get_Initializers(self) -> ReadOnlyCollection[ElementInit]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MemberMemberBinding(MemberBinding):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Bindings(self) -> ReadOnlyCollection[MemberBinding]: ...
    
    # ---------- Methods ---------- #
    
    def Update(self, bindings: IEnumerable[MemberBinding]) -> MemberMemberBinding: ...
    
    def get_Bindings(self) -> ReadOnlyCollection[MemberBinding]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MethodBinaryExpression(SimpleBinaryExpression):
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


class MethodCallExpression(Expression, IArgumentProvider):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Arguments(self) -> ReadOnlyCollection[Expression]: ...
    
    @property
    def Method(self) -> MethodInfo: ...
    
    @property
    def NodeType(self) -> ExpressionType: ...
    
    @property
    def Object(self) -> Expression: ...
    
    @property
    def Type(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def Update(self, object: Expression, arguments: IEnumerable[Expression]) -> MethodCallExpression: ...
    
    def get_Arguments(self) -> ReadOnlyCollection[Expression]: ...
    
    def get_Method(self) -> MethodInfo: ...
    
    def get_NodeType(self) -> ExpressionType: ...
    
    def get_Object(self) -> Expression: ...
    
    def get_Type(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MethodCallExpression1(MethodCallExpression, IArgumentProvider):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, method: MethodInfo, arg0: Expression): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MethodCallExpression2(MethodCallExpression, IArgumentProvider):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, method: MethodInfo, arg0: Expression, arg1: Expression): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MethodCallExpression3(MethodCallExpression, IArgumentProvider):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, method: MethodInfo, arg0: Expression, arg1: Expression, arg2: Expression): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MethodCallExpression4(MethodCallExpression, IArgumentProvider):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, method: MethodInfo, arg0: Expression, arg1: Expression, arg2: Expression, arg3: Expression): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MethodCallExpression5(MethodCallExpression, IArgumentProvider):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, method: MethodInfo, arg0: Expression, arg1: Expression, arg2: Expression, arg3: Expression, arg4: Expression): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MethodCallExpressionN(MethodCallExpression, IArgumentProvider):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, method: MethodInfo, args: IList[Expression]): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class NewArrayBoundsExpression(NewArrayExpression):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def NodeType(self) -> ExpressionType: ...
    
    # ---------- Methods ---------- #
    
    def get_NodeType(self) -> ExpressionType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class NewArrayExpression(Expression):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Expressions(self) -> ReadOnlyCollection[Expression]: ...
    
    @property
    def Type(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def Update(self, expressions: IEnumerable[Expression]) -> NewArrayExpression: ...
    
    def get_Expressions(self) -> ReadOnlyCollection[Expression]: ...
    
    def get_Type(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class NewArrayInitExpression(NewArrayExpression):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def NodeType(self) -> ExpressionType: ...
    
    # ---------- Methods ---------- #
    
    def get_NodeType(self) -> ExpressionType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class NewExpression(Expression, IArgumentProvider):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Arguments(self) -> ReadOnlyCollection[Expression]: ...
    
    @property
    def Constructor(self) -> ConstructorInfo: ...
    
    @property
    def Members(self) -> ReadOnlyCollection[MemberInfo]: ...
    
    @property
    def NodeType(self) -> ExpressionType: ...
    
    @property
    def Type(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def Update(self, arguments: IEnumerable[Expression]) -> NewExpression: ...
    
    def get_Arguments(self) -> ReadOnlyCollection[Expression]: ...
    
    def get_Constructor(self) -> ConstructorInfo: ...
    
    def get_Members(self) -> ReadOnlyCollection[MemberInfo]: ...
    
    def get_NodeType(self) -> ExpressionType: ...
    
    def get_Type(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class NewValueTypeExpression(NewExpression, IArgumentProvider):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Type(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def get_Type(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class OldExpressionVisitor(ABC, ObjectType):
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


class OpAssignMethodConversionBinaryExpression(MethodBinaryExpression):
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


class ParameterExpression(Expression):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def IsByRef(self) -> BooleanType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def NodeType(self) -> ExpressionType: ...
    
    @property
    def Type(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def get_IsByRef(self) -> BooleanType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_NodeType(self) -> ExpressionType: ...
    
    def get_Type(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PrimitiveParameterExpression(Generic[T], ParameterExpression):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Type(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def get_Type(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PropertyExpression(MemberExpression):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, expression: Expression, member: PropertyInfo): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Type(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def get_Type(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ReadOnlyCollectionExtensions(ABC, ObjectType):
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


class RuntimeVariablesExpression(Expression):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def NodeType(self) -> ExpressionType: ...
    
    @property
    def Type(self) -> TypeType: ...
    
    @property
    def Variables(self) -> ReadOnlyCollection[ParameterExpression]: ...
    
    # ---------- Methods ---------- #
    
    def Update(self, variables: IEnumerable[ParameterExpression]) -> RuntimeVariablesExpression: ...
    
    def get_NodeType(self) -> ExpressionType: ...
    
    def get_Type(self) -> TypeType: ...
    
    def get_Variables(self) -> ReadOnlyCollection[ParameterExpression]: ...
    
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
    def GetString(name: StringType, usedFallback: BooleanType) -> Tuple[StringType, BooleanType]: ...
    
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


class Scope1(ScopeExpression):
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


class ScopeExpression(BlockExpression):
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


class ScopeN(ScopeExpression):
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


class ScopeWithType(ScopeN):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Type(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def get_Type(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Set(Generic[T], ObjectType, ICollection[T], IEnumerable[T], IEnumerable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def IsReadOnly(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, item: T) -> VoidType: ...
    
    def Clear(self) -> VoidType: ...
    
    def Contains(self, item: T) -> BooleanType: ...
    
    def CopyTo(self, array: ArrayType[T], arrayIndex: IntType) -> VoidType: ...
    
    def GetEnumerator(self) -> IEnumerator[T]: ...
    
    def Remove(self, item: T) -> BooleanType: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_IsReadOnly(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SimpleBinaryExpression(BinaryExpression):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def NodeType(self) -> ExpressionType: ...
    
    @property
    def Type(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def get_NodeType(self) -> ExpressionType: ...
    
    def get_Type(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SpanDebugInfoExpression(DebugInfoExpression):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def EndColumn(self) -> IntType: ...
    
    @property
    def EndLine(self) -> IntType: ...
    
    @property
    def IsClear(self) -> BooleanType: ...
    
    @property
    def StartColumn(self) -> IntType: ...
    
    @property
    def StartLine(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def get_EndColumn(self) -> IntType: ...
    
    def get_EndLine(self) -> IntType: ...
    
    def get_IsClear(self) -> BooleanType: ...
    
    def get_StartColumn(self) -> IntType: ...
    
    def get_StartLine(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class StackGuard(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def RunOnEmptyStack(self, action: Action[T1, T2], arg1: T1, arg2: T2) -> VoidType: ...
    
    @overload
    def RunOnEmptyStack(self, action: Action[T1, T2, T3], arg1: T1, arg2: T2, arg3: T3) -> VoidType: ...
    
    @overload
    def RunOnEmptyStack(self, action: Func[T1, T2, R], arg1: T1, arg2: T2) -> R: ...
    
    @overload
    def RunOnEmptyStack(self, action: Func[T1, T2, T3, R], arg1: T1, arg2: T2, arg3: T3) -> R: ...
    
    def TryEnterOnCurrentStack(self) -> BooleanType: ...
    
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


class SwitchCase(ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Body(self) -> Expression: ...
    
    @property
    def TestValues(self) -> ReadOnlyCollection[Expression]: ...
    
    # ---------- Methods ---------- #
    
    def ToString(self) -> StringType: ...
    
    def Update(self, testValues: IEnumerable[Expression], body: Expression) -> SwitchCase: ...
    
    def get_Body(self) -> Expression: ...
    
    def get_TestValues(self) -> ReadOnlyCollection[Expression]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SwitchExpression(Expression):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Cases(self) -> ReadOnlyCollection[SwitchCase]: ...
    
    @property
    def Comparison(self) -> MethodInfo: ...
    
    @property
    def DefaultBody(self) -> Expression: ...
    
    @property
    def NodeType(self) -> ExpressionType: ...
    
    @property
    def SwitchValue(self) -> Expression: ...
    
    @property
    def Type(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def Update(self, switchValue: Expression, cases: IEnumerable[SwitchCase], defaultBody: Expression) -> SwitchExpression: ...
    
    def get_Cases(self) -> ReadOnlyCollection[SwitchCase]: ...
    
    def get_Comparison(self) -> MethodInfo: ...
    
    def get_DefaultBody(self) -> Expression: ...
    
    def get_NodeType(self) -> ExpressionType: ...
    
    def get_SwitchValue(self) -> Expression: ...
    
    def get_Type(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SymbolDocumentInfo(ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def DocumentType(self) -> Guid: ...
    
    @property
    def FileName(self) -> StringType: ...
    
    @property
    def Language(self) -> Guid: ...
    
    @property
    def LanguageVendor(self) -> Guid: ...
    
    # ---------- Methods ---------- #
    
    def get_DocumentType(self) -> Guid: ...
    
    def get_FileName(self) -> StringType: ...
    
    def get_Language(self) -> Guid: ...
    
    def get_LanguageVendor(self) -> Guid: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SymbolDocumentWithGuids(SymbolDocumentInfo):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def DocumentType(self) -> Guid: ...
    
    @property
    def Language(self) -> Guid: ...
    
    @property
    def LanguageVendor(self) -> Guid: ...
    
    # ---------- Methods ---------- #
    
    def get_DocumentType(self) -> Guid: ...
    
    def get_Language(self) -> Guid: ...
    
    def get_LanguageVendor(self) -> Guid: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TryExpression(Expression):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Body(self) -> Expression: ...
    
    @property
    def Fault(self) -> Expression: ...
    
    @property
    def Finally(self) -> Expression: ...
    
    @property
    def Handlers(self) -> ReadOnlyCollection[CatchBlock]: ...
    
    @property
    def NodeType(self) -> ExpressionType: ...
    
    @property
    def Type(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def Update(self, body: Expression, handlers: IEnumerable[CatchBlock], _finally: Expression, fault: Expression) -> TryExpression: ...
    
    def get_Body(self) -> Expression: ...
    
    def get_Fault(self) -> Expression: ...
    
    def get_Finally(self) -> Expression: ...
    
    def get_Handlers(self) -> ReadOnlyCollection[CatchBlock]: ...
    
    def get_NodeType(self) -> ExpressionType: ...
    
    def get_Type(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TypeBinaryExpression(Expression):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Expression(self) -> Expression: ...
    
    @property
    def NodeType(self) -> ExpressionType: ...
    
    @property
    def Type(self) -> TypeType: ...
    
    @property
    def TypeOperand(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def Update(self, expression: Expression) -> TypeBinaryExpression: ...
    
    def get_Expression(self) -> Expression: ...
    
    def get_NodeType(self) -> ExpressionType: ...
    
    def get_Type(self) -> TypeType: ...
    
    def get_TypeOperand(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TypedConstantExpression(ConstantExpression):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Type(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def get_Type(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TypedDynamicExpression1(DynamicExpression1, IDynamicExpression, IArgumentProvider):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Type(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def get_Type(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TypedDynamicExpression2(DynamicExpression2, IDynamicExpression, IArgumentProvider):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Type(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def get_Type(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TypedDynamicExpression3(DynamicExpression3, IDynamicExpression, IArgumentProvider):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Type(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def get_Type(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TypedDynamicExpression4(DynamicExpression4, IDynamicExpression, IArgumentProvider):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Type(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def get_Type(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TypedDynamicExpressionN(DynamicExpressionN, IDynamicExpression, IArgumentProvider):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Type(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def get_Type(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TypedParameterExpression(ParameterExpression):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Type(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def get_Type(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UnaryExpression(Expression):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def CanReduce(self) -> BooleanType: ...
    
    @property
    def IsLifted(self) -> BooleanType: ...
    
    @property
    def IsLiftedToNull(self) -> BooleanType: ...
    
    @property
    def Method(self) -> MethodInfo: ...
    
    @property
    def NodeType(self) -> ExpressionType: ...
    
    @property
    def Operand(self) -> Expression: ...
    
    @property
    def Type(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def Reduce(self) -> Expression: ...
    
    def Update(self, operand: Expression) -> UnaryExpression: ...
    
    def get_CanReduce(self) -> BooleanType: ...
    
    def get_IsLifted(self) -> BooleanType: ...
    
    def get_IsLiftedToNull(self) -> BooleanType: ...
    
    def get_Method(self) -> MethodInfo: ...
    
    def get_NodeType(self) -> ExpressionType: ...
    
    def get_Operand(self) -> Expression: ...
    
    def get_Type(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# No Structs

# ---------- Interfaces ---------- #

class IArgumentProvider(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def ArgumentCount(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def GetArgument(self, index: IntType) -> Expression: ...
    
    def get_ArgumentCount(self) -> IntType: ...
    
    # No Events


class IDynamicExpression(Protocol, IArgumentProvider):
    # ---------- Properties ---------- #
    
    @property
    def DelegateType(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def CreateCallSite(self) -> ObjectType: ...
    
    def Rewrite(self, args: ArrayType[Expression]) -> Expression: ...
    
    def get_DelegateType(self) -> TypeType: ...
    
    # No Events


# ---------- Enums ---------- #

class AnalyzeTypeIsResult(Enum):
    KnownFalse: IntType = 0
    KnownTrue: IntType = 1
    KnownAssignable: IntType = 2
    Unknown: IntType = 3


class ExpressionType(Enum):
    Add: IntType = 0
    AddChecked: IntType = 1
    And: IntType = 2
    AndAlso: IntType = 3
    ArrayLength: IntType = 4
    ArrayIndex: IntType = 5
    Call: IntType = 6
    Coalesce: IntType = 7
    Conditional: IntType = 8
    Constant: IntType = 9
    Convert: IntType = 10
    ConvertChecked: IntType = 11
    Divide: IntType = 12
    Equal: IntType = 13
    ExclusiveOr: IntType = 14
    GreaterThan: IntType = 15
    GreaterThanOrEqual: IntType = 16
    Invoke: IntType = 17
    Lambda: IntType = 18
    LeftShift: IntType = 19
    LessThan: IntType = 20
    LessThanOrEqual: IntType = 21
    ListInit: IntType = 22
    MemberAccess: IntType = 23
    MemberInit: IntType = 24
    Modulo: IntType = 25
    Multiply: IntType = 26
    MultiplyChecked: IntType = 27
    Negate: IntType = 28
    UnaryPlus: IntType = 29
    NegateChecked: IntType = 30
    New: IntType = 31
    NewArrayInit: IntType = 32
    NewArrayBounds: IntType = 33
    Not: IntType = 34
    NotEqual: IntType = 35
    Or: IntType = 36
    OrElse: IntType = 37
    Parameter: IntType = 38
    Power: IntType = 39
    Quote: IntType = 40
    RightShift: IntType = 41
    Subtract: IntType = 42
    SubtractChecked: IntType = 43
    TypeAs: IntType = 44
    TypeIs: IntType = 45
    Assign: IntType = 46
    Block: IntType = 47
    DebugInfo: IntType = 48
    Decrement: IntType = 49
    Dynamic: IntType = 50
    Default: IntType = 51
    Extension: IntType = 52
    Goto: IntType = 53
    Increment: IntType = 54
    Index: IntType = 55
    Label: IntType = 56
    RuntimeVariables: IntType = 57
    Loop: IntType = 58
    Switch: IntType = 59
    Throw: IntType = 60
    Try: IntType = 61
    Unbox: IntType = 62
    AddAssign: IntType = 63
    AndAssign: IntType = 64
    DivideAssign: IntType = 65
    ExclusiveOrAssign: IntType = 66
    LeftShiftAssign: IntType = 67
    ModuloAssign: IntType = 68
    MultiplyAssign: IntType = 69
    OrAssign: IntType = 70
    PowerAssign: IntType = 71
    RightShiftAssign: IntType = 72
    SubtractAssign: IntType = 73
    AddAssignChecked: IntType = 74
    MultiplyAssignChecked: IntType = 75
    SubtractAssignChecked: IntType = 76
    PreIncrementAssign: IntType = 77
    PreDecrementAssign: IntType = 78
    PostIncrementAssign: IntType = 79
    PostDecrementAssign: IntType = 80
    TypeEqual: IntType = 81
    OnesComplement: IntType = 82
    IsTrue: IntType = 83
    IsFalse: IntType = 84


class GotoExpressionKind(Enum):
    Goto: IntType = 0
    Return: IntType = 1
    Break: IntType = 2
    Continue: IntType = 3


class MemberBindingType(Enum):
    Assignment: IntType = 0
    MemberBinding: IntType = 1
    ListBinding: IntType = 2


# No Delegates

__all__ = [
    ArgumentProviderOps,
    AssignBinaryExpression,
    BinaryExpression,
    Block2,
    Block3,
    Block4,
    Block5,
    BlockExpression,
    BlockExpressionList,
    BlockN,
    ByRefParameterExpression,
    CatchBlock,
    ClearDebugInfoExpression,
    CoalesceConversionBinaryExpression,
    ConditionalExpression,
    ConstantCheck,
    ConstantExpression,
    DebugInfoExpression,
    DebugViewWriter,
    DefaultExpression,
    DynamicExpression,
    DynamicExpression1,
    DynamicExpression2,
    DynamicExpression3,
    DynamicExpression4,
    DynamicExpressionN,
    DynamicExpressionVisitor,
    ElementInit,
    Error,
    Expression,
    ExpressionStringBuilder,
    ExpressionVisitor,
    FieldExpression,
    FullConditionalExpression,
    FullConditionalExpressionWithType,
    GotoExpression,
    IndexExpression,
    InstanceMethodCallExpression2,
    InstanceMethodCallExpression3,
    InstanceMethodCallExpressionN,
    InvocationExpression,
    LabelExpression,
    LabelTarget,
    LambdaExpression,
    ListArgumentProvider,
    ListInitExpression,
    LogicalBinaryExpression,
    LoopExpression,
    MemberAssignment,
    MemberBinding,
    MemberExpression,
    MemberInitExpression,
    MemberListBinding,
    MemberMemberBinding,
    MethodBinaryExpression,
    MethodCallExpression,
    MethodCallExpression1,
    MethodCallExpression2,
    MethodCallExpression3,
    MethodCallExpression4,
    MethodCallExpression5,
    MethodCallExpressionN,
    NewArrayBoundsExpression,
    NewArrayExpression,
    NewArrayInitExpression,
    NewExpression,
    NewValueTypeExpression,
    OldExpressionVisitor,
    OpAssignMethodConversionBinaryExpression,
    ParameterExpression,
    PrimitiveParameterExpression,
    PropertyExpression,
    ReadOnlyCollectionExtensions,
    RuntimeVariablesExpression,
    SR,
    SRCategoryAttribute,
    SRDescriptionAttribute,
    Scope1,
    ScopeExpression,
    ScopeN,
    ScopeWithType,
    Set,
    SimpleBinaryExpression,
    SpanDebugInfoExpression,
    StackGuard,
    Strings,
    SwitchCase,
    SwitchExpression,
    SymbolDocumentInfo,
    SymbolDocumentWithGuids,
    TryExpression,
    TypeBinaryExpression,
    TypedConstantExpression,
    TypedDynamicExpression1,
    TypedDynamicExpression2,
    TypedDynamicExpression3,
    TypedDynamicExpression4,
    TypedDynamicExpressionN,
    TypedParameterExpression,
    UnaryExpression,
    IArgumentProvider,
    IDynamicExpression,
    AnalyzeTypeIsResult,
    ExpressionType,
    GotoExpressionKind,
    MemberBindingType,
]
