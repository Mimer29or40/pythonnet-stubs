from __future__ import annotations

from abc import ABC
from typing import List, Protocol, Tuple, Union, overload

from System import Array, Boolean, Int32, Object, String, Type
from System.Collections import IEnumerable
from System.Collections.Generic import ICollection, IDictionary, IEnumerable, IList, KeyValuePair
from System.Collections.ObjectModel import ReadOnlyCollection
from System.ComponentModel import INotifyPropertyChanged
from System.Linq.Expressions import Expression, ExpressionType, LabelTarget, ParameterExpression
from System.Runtime.CompilerServices import CallSiteBinder

# ---------- Types ---------- #

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
IntType = Union[int, Int32]
ObjectType = Object
StringType = Union[str, String]
TypeType = Union[type, Type]

# ---------- Classes ---------- #

class BinaryOperationBinder(ABC, DynamicMetaObjectBinder):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Operation(self) -> ExpressionType: ...
    
    @property
    def ReturnType(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Bind(self, target: DynamicMetaObject, args: ArrayType[DynamicMetaObject]) -> DynamicMetaObject: ...
    
    @overload
    def FallbackBinaryOperation(self, target: DynamicMetaObject, arg: DynamicMetaObject) -> DynamicMetaObject: ...
    
    @overload
    def FallbackBinaryOperation(self, target: DynamicMetaObject, arg: DynamicMetaObject, errorSuggestion: DynamicMetaObject) -> DynamicMetaObject: ...
    
    def get_Operation(self) -> ExpressionType: ...
    
    def get_ReturnType(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class BindingRestrictions(ABC, ObjectType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Empty() -> BindingRestrictions: ...
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def Combine(contributingObjects: IList[DynamicMetaObject]) -> BindingRestrictions: ...
    
    @staticmethod
    def GetExpressionRestriction(expression: Expression) -> BindingRestrictions: ...
    
    @staticmethod
    def GetInstanceRestriction(expression: Expression, instance: ObjectType) -> BindingRestrictions: ...
    
    @staticmethod
    def GetTypeRestriction(expression: Expression, type: TypeType) -> BindingRestrictions: ...
    
    def Merge(self, restrictions: BindingRestrictions) -> BindingRestrictions: ...
    
    def ToExpression(self) -> Expression: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CallInfo(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, argCount: IntType, argNames: ArrayType[StringType]): ...
    
    @overload
    def __init__(self, argCount: IntType, argNames: IEnumerable[StringType]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ArgumentCount(self) -> IntType: ...
    
    @property
    def ArgumentNames(self) -> ReadOnlyCollection[StringType]: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def get_ArgumentCount(self) -> IntType: ...
    
    def get_ArgumentNames(self) -> ReadOnlyCollection[StringType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ConvertBinder(ABC, DynamicMetaObjectBinder):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Explicit(self) -> BooleanType: ...
    
    @property
    def ReturnType(self) -> TypeType: ...
    
    @property
    def Type(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Bind(self, target: DynamicMetaObject, args: ArrayType[DynamicMetaObject]) -> DynamicMetaObject: ...
    
    @overload
    def FallbackConvert(self, target: DynamicMetaObject) -> DynamicMetaObject: ...
    
    @overload
    def FallbackConvert(self, target: DynamicMetaObject, errorSuggestion: DynamicMetaObject) -> DynamicMetaObject: ...
    
    def get_Explicit(self) -> BooleanType: ...
    
    def get_ReturnType(self) -> TypeType: ...
    
    def get_Type(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CreateInstanceBinder(ABC, DynamicMetaObjectBinder):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def CallInfo(self) -> CallInfo: ...
    
    @property
    def ReturnType(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Bind(self, target: DynamicMetaObject, args: ArrayType[DynamicMetaObject]) -> DynamicMetaObject: ...
    
    @overload
    def FallbackCreateInstance(self, target: DynamicMetaObject, args: ArrayType[DynamicMetaObject]) -> DynamicMetaObject: ...
    
    @overload
    def FallbackCreateInstance(self, target: DynamicMetaObject, args: ArrayType[DynamicMetaObject], errorSuggestion: DynamicMetaObject) -> DynamicMetaObject: ...
    
    def get_CallInfo(self) -> CallInfo: ...
    
    def get_ReturnType(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DeleteIndexBinder(ABC, DynamicMetaObjectBinder):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def CallInfo(self) -> CallInfo: ...
    
    @property
    def ReturnType(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Bind(self, target: DynamicMetaObject, args: ArrayType[DynamicMetaObject]) -> DynamicMetaObject: ...
    
    @overload
    def FallbackDeleteIndex(self, target: DynamicMetaObject, indexes: ArrayType[DynamicMetaObject]) -> DynamicMetaObject: ...
    
    @overload
    def FallbackDeleteIndex(self, target: DynamicMetaObject, indexes: ArrayType[DynamicMetaObject], errorSuggestion: DynamicMetaObject) -> DynamicMetaObject: ...
    
    def get_CallInfo(self) -> CallInfo: ...
    
    def get_ReturnType(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DeleteMemberBinder(ABC, DynamicMetaObjectBinder):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def IgnoreCase(self) -> BooleanType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def ReturnType(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Bind(self, target: DynamicMetaObject, args: ArrayType[DynamicMetaObject]) -> DynamicMetaObject: ...
    
    @overload
    def FallbackDeleteMember(self, target: DynamicMetaObject) -> DynamicMetaObject: ...
    
    @overload
    def FallbackDeleteMember(self, target: DynamicMetaObject, errorSuggestion: DynamicMetaObject) -> DynamicMetaObject: ...
    
    def get_IgnoreCase(self) -> BooleanType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_ReturnType(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DynamicMetaObject(ObjectType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def EmptyMetaObjects() -> ArrayType[DynamicMetaObject]: ...
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, expression: Expression, restrictions: BindingRestrictions): ...
    
    @overload
    def __init__(self, expression: Expression, restrictions: BindingRestrictions, value: ObjectType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Expression(self) -> Expression: ...
    
    @property
    def HasValue(self) -> BooleanType: ...
    
    @property
    def LimitType(self) -> TypeType: ...
    
    @property
    def Restrictions(self) -> BindingRestrictions: ...
    
    @property
    def RuntimeType(self) -> TypeType: ...
    
    @property
    def Value(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def BindBinaryOperation(self, binder: BinaryOperationBinder, arg: DynamicMetaObject) -> DynamicMetaObject: ...
    
    def BindConvert(self, binder: ConvertBinder) -> DynamicMetaObject: ...
    
    def BindCreateInstance(self, binder: CreateInstanceBinder, args: ArrayType[DynamicMetaObject]) -> DynamicMetaObject: ...
    
    def BindDeleteIndex(self, binder: DeleteIndexBinder, indexes: ArrayType[DynamicMetaObject]) -> DynamicMetaObject: ...
    
    def BindDeleteMember(self, binder: DeleteMemberBinder) -> DynamicMetaObject: ...
    
    def BindGetIndex(self, binder: GetIndexBinder, indexes: ArrayType[DynamicMetaObject]) -> DynamicMetaObject: ...
    
    def BindGetMember(self, binder: GetMemberBinder) -> DynamicMetaObject: ...
    
    def BindInvoke(self, binder: InvokeBinder, args: ArrayType[DynamicMetaObject]) -> DynamicMetaObject: ...
    
    def BindInvokeMember(self, binder: InvokeMemberBinder, args: ArrayType[DynamicMetaObject]) -> DynamicMetaObject: ...
    
    def BindSetIndex(self, binder: SetIndexBinder, indexes: ArrayType[DynamicMetaObject], value: DynamicMetaObject) -> DynamicMetaObject: ...
    
    def BindSetMember(self, binder: SetMemberBinder, value: DynamicMetaObject) -> DynamicMetaObject: ...
    
    def BindUnaryOperation(self, binder: UnaryOperationBinder) -> DynamicMetaObject: ...
    
    @staticmethod
    def Create(value: ObjectType, expression: Expression) -> DynamicMetaObject: ...
    
    def GetDynamicMemberNames(self) -> IEnumerable[StringType]: ...
    
    def get_Expression(self) -> Expression: ...
    
    def get_HasValue(self) -> BooleanType: ...
    
    def get_LimitType(self) -> TypeType: ...
    
    def get_Restrictions(self) -> BindingRestrictions: ...
    
    def get_RuntimeType(self) -> TypeType: ...
    
    def get_Value(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DynamicMetaObjectBinder(ABC, CallSiteBinder):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def ReturnType(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Bind(self, args: ArrayType[ObjectType], parameters: ReadOnlyCollection[ParameterExpression], returnLabel: LabelTarget) -> Expression: ...
    
    @overload
    def Bind(self, target: DynamicMetaObject, args: ArrayType[DynamicMetaObject]) -> DynamicMetaObject: ...
    
    @overload
    def Defer(self, args: ArrayType[DynamicMetaObject]) -> DynamicMetaObject: ...
    
    @overload
    def Defer(self, target: DynamicMetaObject, args: ArrayType[DynamicMetaObject]) -> DynamicMetaObject: ...
    
    def GetUpdateExpression(self, type: TypeType) -> Expression: ...
    
    def get_ReturnType(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DynamicObject(ObjectType, IDynamicMetaObjectProvider):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetDynamicMemberNames(self) -> IEnumerable[StringType]: ...
    
    def GetMetaObject(self, parameter: Expression) -> DynamicMetaObject: ...
    
    def TryBinaryOperation(self, binder: BinaryOperationBinder, arg: ObjectType, result: ObjectType) -> Tuple[BooleanType, ObjectType]: ...
    
    def TryConvert(self, binder: ConvertBinder, result: ObjectType) -> Tuple[BooleanType, ObjectType]: ...
    
    def TryCreateInstance(self, binder: CreateInstanceBinder, args: ArrayType[ObjectType], result: ObjectType) -> Tuple[BooleanType, ObjectType]: ...
    
    def TryDeleteIndex(self, binder: DeleteIndexBinder, indexes: ArrayType[ObjectType]) -> BooleanType: ...
    
    def TryDeleteMember(self, binder: DeleteMemberBinder) -> BooleanType: ...
    
    def TryGetIndex(self, binder: GetIndexBinder, indexes: ArrayType[ObjectType], result: ObjectType) -> Tuple[BooleanType, ObjectType]: ...
    
    def TryGetMember(self, binder: GetMemberBinder, result: ObjectType) -> Tuple[BooleanType, ObjectType]: ...
    
    def TryInvoke(self, binder: InvokeBinder, args: ArrayType[ObjectType], result: ObjectType) -> Tuple[BooleanType, ObjectType]: ...
    
    def TryInvokeMember(self, binder: InvokeMemberBinder, args: ArrayType[ObjectType], result: ObjectType) -> Tuple[BooleanType, ObjectType]: ...
    
    def TrySetIndex(self, binder: SetIndexBinder, indexes: ArrayType[ObjectType], value: ObjectType) -> BooleanType: ...
    
    def TrySetMember(self, binder: SetMemberBinder, value: ObjectType) -> BooleanType: ...
    
    def TryUnaryOperation(self, binder: UnaryOperationBinder, result: ObjectType) -> Tuple[BooleanType, ObjectType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ExpandoClass(ObjectType):
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


class ExpandoObject(ObjectType, IDynamicMetaObjectProvider, IDictionary[StringType, ObjectType], ICollection[KeyValuePair[StringType, ObjectType]], IEnumerable[KeyValuePair[StringType, ObjectType]], IEnumerable, INotifyPropertyChanged):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class GetIndexBinder(ABC, DynamicMetaObjectBinder):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def CallInfo(self) -> CallInfo: ...
    
    @property
    def ReturnType(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Bind(self, target: DynamicMetaObject, args: ArrayType[DynamicMetaObject]) -> DynamicMetaObject: ...
    
    @overload
    def FallbackGetIndex(self, target: DynamicMetaObject, indexes: ArrayType[DynamicMetaObject]) -> DynamicMetaObject: ...
    
    @overload
    def FallbackGetIndex(self, target: DynamicMetaObject, indexes: ArrayType[DynamicMetaObject], errorSuggestion: DynamicMetaObject) -> DynamicMetaObject: ...
    
    def get_CallInfo(self) -> CallInfo: ...
    
    def get_ReturnType(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class GetMemberBinder(ABC, DynamicMetaObjectBinder):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def IgnoreCase(self) -> BooleanType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def ReturnType(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Bind(self, target: DynamicMetaObject, args: ArrayType[DynamicMetaObject]) -> DynamicMetaObject: ...
    
    @overload
    def FallbackGetMember(self, target: DynamicMetaObject) -> DynamicMetaObject: ...
    
    @overload
    def FallbackGetMember(self, target: DynamicMetaObject, errorSuggestion: DynamicMetaObject) -> DynamicMetaObject: ...
    
    def get_IgnoreCase(self) -> BooleanType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_ReturnType(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class InvokeBinder(ABC, DynamicMetaObjectBinder):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def CallInfo(self) -> CallInfo: ...
    
    @property
    def ReturnType(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Bind(self, target: DynamicMetaObject, args: ArrayType[DynamicMetaObject]) -> DynamicMetaObject: ...
    
    @overload
    def FallbackInvoke(self, target: DynamicMetaObject, args: ArrayType[DynamicMetaObject]) -> DynamicMetaObject: ...
    
    @overload
    def FallbackInvoke(self, target: DynamicMetaObject, args: ArrayType[DynamicMetaObject], errorSuggestion: DynamicMetaObject) -> DynamicMetaObject: ...
    
    def get_CallInfo(self) -> CallInfo: ...
    
    def get_ReturnType(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class InvokeMemberBinder(ABC, DynamicMetaObjectBinder):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def CallInfo(self) -> CallInfo: ...
    
    @property
    def IgnoreCase(self) -> BooleanType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def ReturnType(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Bind(self, target: DynamicMetaObject, args: ArrayType[DynamicMetaObject]) -> DynamicMetaObject: ...
    
    def FallbackInvoke(self, target: DynamicMetaObject, args: ArrayType[DynamicMetaObject], errorSuggestion: DynamicMetaObject) -> DynamicMetaObject: ...
    
    @overload
    def FallbackInvokeMember(self, target: DynamicMetaObject, args: ArrayType[DynamicMetaObject]) -> DynamicMetaObject: ...
    
    @overload
    def FallbackInvokeMember(self, target: DynamicMetaObject, args: ArrayType[DynamicMetaObject], errorSuggestion: DynamicMetaObject) -> DynamicMetaObject: ...
    
    def get_CallInfo(self) -> CallInfo: ...
    
    def get_IgnoreCase(self) -> BooleanType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_ReturnType(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SetIndexBinder(ABC, DynamicMetaObjectBinder):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def CallInfo(self) -> CallInfo: ...
    
    @property
    def ReturnType(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Bind(self, target: DynamicMetaObject, args: ArrayType[DynamicMetaObject]) -> DynamicMetaObject: ...
    
    @overload
    def FallbackSetIndex(self, target: DynamicMetaObject, indexes: ArrayType[DynamicMetaObject], value: DynamicMetaObject) -> DynamicMetaObject: ...
    
    @overload
    def FallbackSetIndex(self, target: DynamicMetaObject, indexes: ArrayType[DynamicMetaObject], value: DynamicMetaObject, errorSuggestion: DynamicMetaObject) -> DynamicMetaObject: ...
    
    def get_CallInfo(self) -> CallInfo: ...
    
    def get_ReturnType(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SetMemberBinder(ABC, DynamicMetaObjectBinder):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def IgnoreCase(self) -> BooleanType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def ReturnType(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Bind(self, target: DynamicMetaObject, args: ArrayType[DynamicMetaObject]) -> DynamicMetaObject: ...
    
    @overload
    def FallbackSetMember(self, target: DynamicMetaObject, value: DynamicMetaObject) -> DynamicMetaObject: ...
    
    @overload
    def FallbackSetMember(self, target: DynamicMetaObject, value: DynamicMetaObject, errorSuggestion: DynamicMetaObject) -> DynamicMetaObject: ...
    
    def get_IgnoreCase(self) -> BooleanType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_ReturnType(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UnaryOperationBinder(ABC, DynamicMetaObjectBinder):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Operation(self) -> ExpressionType: ...
    
    @property
    def ReturnType(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Bind(self, target: DynamicMetaObject, args: ArrayType[DynamicMetaObject]) -> DynamicMetaObject: ...
    
    @overload
    def FallbackUnaryOperation(self, target: DynamicMetaObject) -> DynamicMetaObject: ...
    
    @overload
    def FallbackUnaryOperation(self, target: DynamicMetaObject, errorSuggestion: DynamicMetaObject) -> DynamicMetaObject: ...
    
    def get_Operation(self) -> ExpressionType: ...
    
    def get_ReturnType(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UpdateDelegates(ABC, ObjectType):
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


# No Structs

# ---------- Interfaces ---------- #

class IDynamicMetaObjectProvider(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetMetaObject(self, parameter: Expression) -> DynamicMetaObject: ...
    
    # No Events


class IInvokeOnGetBinder(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def InvokeOnGet(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def get_InvokeOnGet(self) -> BooleanType: ...
    
    # No Events


# No Enums

# No Delegates

__all__ = [
    BinaryOperationBinder,
    BindingRestrictions,
    CallInfo,
    ConvertBinder,
    CreateInstanceBinder,
    DeleteIndexBinder,
    DeleteMemberBinder,
    DynamicMetaObject,
    DynamicMetaObjectBinder,
    DynamicObject,
    ExpandoClass,
    ExpandoObject,
    GetIndexBinder,
    GetMemberBinder,
    InvokeBinder,
    InvokeMemberBinder,
    SetIndexBinder,
    SetMemberBinder,
    UnaryOperationBinder,
    UpdateDelegates,
    IDynamicMetaObjectProvider,
    IInvokeOnGetBinder,
]
