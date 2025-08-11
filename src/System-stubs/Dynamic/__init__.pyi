"""Automatically generated stubs for C# namespace: System.Dynamic."""

from abc import ABC
from collections.abc import Iterator
from typing import ClassVar
from typing import Self
from typing import overload

from System import Array
from System import Object
from System import String
from System import Type
from System.Collections import IEnumerable
from System.Collections.Generic import ICollection
from System.Collections.Generic import IDictionary
from System.Collections.Generic import IEnumerable
from System.Collections.Generic import IEnumerator
from System.Collections.Generic import IList
from System.Collections.Generic import KeyValuePair
from System.Collections.ObjectModel import ReadOnlyCollection
from System.ComponentModel import INotifyPropertyChanged
from System.ComponentModel import PropertyChangedEventHandler
from System.Linq.Expressions import Expression
from System.Linq.Expressions import ExpressionType
from System.Linq.Expressions import LabelTarget
from System.Linq.Expressions import ParameterExpression
from System.Runtime.CompilerServices import CallSite
from System.Runtime.CompilerServices import CallSiteBinder

class EventType[T]:
    def __iadd__(self, other: T) -> Self: ...
    def __isub__(self, other: T) -> Self: ...

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class BinaryOperationBinder(ABC, DynamicMetaObjectBinder):
    """"""
    @property
    def Operation(self) -> ExpressionType:
        """"""
    @property
    def ReturnType(self) -> Type:
        """"""
    @overload
    def Bind(self, target: DynamicMetaObject, args: Array[DynamicMetaObject]) -> DynamicMetaObject:
        """"""
    @overload
    def Bind(
        self,
        args: Array[object],
        parameters: ReadOnlyCollection[ParameterExpression],
        returnLabel: LabelTarget,
    ) -> Expression:
        """"""
    def BindDelegate[T](self, site: CallSite[T], args: Array[object]) -> T:
        """"""
    @overload
    def Defer(self, target: DynamicMetaObject, args: Array[DynamicMetaObject]) -> DynamicMetaObject:
        """"""
    @overload
    def Defer(self, args: Array[DynamicMetaObject]) -> DynamicMetaObject:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def FallbackBinaryOperation(
        self, target: DynamicMetaObject, arg: DynamicMetaObject
    ) -> DynamicMetaObject:
        """"""
    @overload
    def FallbackBinaryOperation(
        self, target: DynamicMetaObject, arg: DynamicMetaObject, errorSuggestion: DynamicMetaObject
    ) -> DynamicMetaObject:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetUpdateExpression(self, type: Type) -> Expression:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class BindingRestrictions(ABC, Object):
    """"""

    Empty: ClassVar[BindingRestrictions]
    """"""
    @classmethod
    def Combine(cls, contributingObjects: IList[DynamicMetaObject]) -> BindingRestrictions:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def GetExpressionRestriction(cls, expression: Expression) -> BindingRestrictions:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @classmethod
    def GetInstanceRestriction(
        cls, expression: Expression, instance: object
    ) -> BindingRestrictions:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def GetTypeRestriction(cls, expression: Expression, type: Type) -> BindingRestrictions:
        """"""
    def Merge(self, restrictions: BindingRestrictions) -> BindingRestrictions:
        """"""
    def ToExpression(self) -> Expression:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CallInfo(Object):
    """"""
    @overload
    def __init__(self, argCount: int, argNames: Array[str]) -> None:
        """"""
    @overload
    def __init__(self, argCount: int, argNames: IEnumerable[str]) -> None:
        """"""
    @property
    def ArgumentCount(self) -> int:
        """"""
    @property
    def ArgumentNames(self) -> ReadOnlyCollection[str]:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ConvertBinder(ABC, DynamicMetaObjectBinder):
    """"""
    @property
    def Explicit(self) -> bool:
        """"""
    @property
    def ReturnType(self) -> Type:
        """"""
    @property
    def Type(self) -> Type:
        """"""
    @overload
    def Bind(self, target: DynamicMetaObject, args: Array[DynamicMetaObject]) -> DynamicMetaObject:
        """"""
    @overload
    def Bind(
        self,
        args: Array[object],
        parameters: ReadOnlyCollection[ParameterExpression],
        returnLabel: LabelTarget,
    ) -> Expression:
        """"""
    def BindDelegate[T](self, site: CallSite[T], args: Array[object]) -> T:
        """"""
    @overload
    def Defer(self, target: DynamicMetaObject, args: Array[DynamicMetaObject]) -> DynamicMetaObject:
        """"""
    @overload
    def Defer(self, args: Array[DynamicMetaObject]) -> DynamicMetaObject:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def FallbackConvert(self, target: DynamicMetaObject) -> DynamicMetaObject:
        """"""
    @overload
    def FallbackConvert(
        self, target: DynamicMetaObject, errorSuggestion: DynamicMetaObject
    ) -> DynamicMetaObject:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetUpdateExpression(self, type: Type) -> Expression:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CreateInstanceBinder(ABC, DynamicMetaObjectBinder):
    """"""
    @property
    def CallInfo(self) -> CallInfo:
        """"""
    @property
    def ReturnType(self) -> Type:
        """"""
    @overload
    def Bind(self, target: DynamicMetaObject, args: Array[DynamicMetaObject]) -> DynamicMetaObject:
        """"""
    @overload
    def Bind(
        self,
        args: Array[object],
        parameters: ReadOnlyCollection[ParameterExpression],
        returnLabel: LabelTarget,
    ) -> Expression:
        """"""
    def BindDelegate[T](self, site: CallSite[T], args: Array[object]) -> T:
        """"""
    @overload
    def Defer(self, target: DynamicMetaObject, args: Array[DynamicMetaObject]) -> DynamicMetaObject:
        """"""
    @overload
    def Defer(self, args: Array[DynamicMetaObject]) -> DynamicMetaObject:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def FallbackCreateInstance(
        self, target: DynamicMetaObject, args: Array[DynamicMetaObject]
    ) -> DynamicMetaObject:
        """"""
    @overload
    def FallbackCreateInstance(
        self,
        target: DynamicMetaObject,
        args: Array[DynamicMetaObject],
        errorSuggestion: DynamicMetaObject,
    ) -> DynamicMetaObject:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetUpdateExpression(self, type: Type) -> Expression:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class DeleteIndexBinder(ABC, DynamicMetaObjectBinder):
    """"""
    @property
    def CallInfo(self) -> CallInfo:
        """"""
    @property
    def ReturnType(self) -> Type:
        """"""
    @overload
    def Bind(self, target: DynamicMetaObject, args: Array[DynamicMetaObject]) -> DynamicMetaObject:
        """"""
    @overload
    def Bind(
        self,
        args: Array[object],
        parameters: ReadOnlyCollection[ParameterExpression],
        returnLabel: LabelTarget,
    ) -> Expression:
        """"""
    def BindDelegate[T](self, site: CallSite[T], args: Array[object]) -> T:
        """"""
    @overload
    def Defer(self, target: DynamicMetaObject, args: Array[DynamicMetaObject]) -> DynamicMetaObject:
        """"""
    @overload
    def Defer(self, args: Array[DynamicMetaObject]) -> DynamicMetaObject:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def FallbackDeleteIndex(
        self, target: DynamicMetaObject, indexes: Array[DynamicMetaObject]
    ) -> DynamicMetaObject:
        """"""
    @overload
    def FallbackDeleteIndex(
        self,
        target: DynamicMetaObject,
        indexes: Array[DynamicMetaObject],
        errorSuggestion: DynamicMetaObject,
    ) -> DynamicMetaObject:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetUpdateExpression(self, type: Type) -> Expression:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class DeleteMemberBinder(ABC, DynamicMetaObjectBinder):
    """"""
    @property
    def IgnoreCase(self) -> bool:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def ReturnType(self) -> Type:
        """"""
    @overload
    def Bind(self, target: DynamicMetaObject, args: Array[DynamicMetaObject]) -> DynamicMetaObject:
        """"""
    @overload
    def Bind(
        self,
        args: Array[object],
        parameters: ReadOnlyCollection[ParameterExpression],
        returnLabel: LabelTarget,
    ) -> Expression:
        """"""
    def BindDelegate[T](self, site: CallSite[T], args: Array[object]) -> T:
        """"""
    @overload
    def Defer(self, target: DynamicMetaObject, args: Array[DynamicMetaObject]) -> DynamicMetaObject:
        """"""
    @overload
    def Defer(self, args: Array[DynamicMetaObject]) -> DynamicMetaObject:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def FallbackDeleteMember(self, target: DynamicMetaObject) -> DynamicMetaObject:
        """"""
    @overload
    def FallbackDeleteMember(
        self, target: DynamicMetaObject, errorSuggestion: DynamicMetaObject
    ) -> DynamicMetaObject:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetUpdateExpression(self, type: Type) -> Expression:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class DynamicMetaObject(Object):
    """"""

    EmptyMetaObjects: ClassVar[Array[DynamicMetaObject]]
    """"""
    @overload
    def __init__(self, expression: Expression, restrictions: BindingRestrictions) -> None:
        """"""
    @overload
    def __init__(
        self, expression: Expression, restrictions: BindingRestrictions, value: object
    ) -> None:
        """"""
    @property
    def Expression(self) -> Expression:
        """"""
    @property
    def HasValue(self) -> bool:
        """"""
    @property
    def LimitType(self) -> Type:
        """"""
    @property
    def Restrictions(self) -> BindingRestrictions:
        """"""
    @property
    def RuntimeType(self) -> Type:
        """"""
    @property
    def Value(self) -> object:
        """"""
    def BindBinaryOperation(
        self, binder: BinaryOperationBinder, arg: DynamicMetaObject
    ) -> DynamicMetaObject:
        """"""
    def BindConvert(self, binder: ConvertBinder) -> DynamicMetaObject:
        """"""
    def BindCreateInstance(
        self, binder: CreateInstanceBinder, args: Array[DynamicMetaObject]
    ) -> DynamicMetaObject:
        """"""
    def BindDeleteIndex(
        self, binder: DeleteIndexBinder, indexes: Array[DynamicMetaObject]
    ) -> DynamicMetaObject:
        """"""
    def BindDeleteMember(self, binder: DeleteMemberBinder) -> DynamicMetaObject:
        """"""
    def BindGetIndex(
        self, binder: GetIndexBinder, indexes: Array[DynamicMetaObject]
    ) -> DynamicMetaObject:
        """"""
    def BindGetMember(self, binder: GetMemberBinder) -> DynamicMetaObject:
        """"""
    def BindInvoke(self, binder: InvokeBinder, args: Array[DynamicMetaObject]) -> DynamicMetaObject:
        """"""
    def BindInvokeMember(
        self, binder: InvokeMemberBinder, args: Array[DynamicMetaObject]
    ) -> DynamicMetaObject:
        """"""
    def BindSetIndex(
        self, binder: SetIndexBinder, indexes: Array[DynamicMetaObject], value: DynamicMetaObject
    ) -> DynamicMetaObject:
        """"""
    def BindSetMember(self, binder: SetMemberBinder, value: DynamicMetaObject) -> DynamicMetaObject:
        """"""
    def BindUnaryOperation(self, binder: UnaryOperationBinder) -> DynamicMetaObject:
        """"""
    @classmethod
    def Create(cls, value: object, expression: Expression) -> DynamicMetaObject:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetDynamicMemberNames(self) -> IEnumerable[str]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class DynamicMetaObjectBinder(ABC, CallSiteBinder):
    """"""
    @property
    def ReturnType(self) -> Type:
        """"""
    @overload
    def Bind(self, target: DynamicMetaObject, args: Array[DynamicMetaObject]) -> DynamicMetaObject:
        """"""
    @overload
    def Bind(
        self,
        args: Array[object],
        parameters: ReadOnlyCollection[ParameterExpression],
        returnLabel: LabelTarget,
    ) -> Expression:
        """"""
    def BindDelegate[T](self, site: CallSite[T], args: Array[object]) -> T:
        """"""
    @overload
    def Defer(self, target: DynamicMetaObject, args: Array[DynamicMetaObject]) -> DynamicMetaObject:
        """"""
    @overload
    def Defer(self, args: Array[DynamicMetaObject]) -> DynamicMetaObject:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetUpdateExpression(self, type: Type) -> Expression:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class DynamicObject(Object, IDynamicMetaObjectProvider):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetDynamicMemberNames(self) -> IEnumerable[str]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetMetaObject(self, parameter: Expression) -> DynamicMetaObject:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def TryBinaryOperation(
        self, binder: BinaryOperationBinder, arg: object, result: Object
    ) -> tuple[bool, Object]:
        """"""
    def TryConvert(self, binder: ConvertBinder, result: Object) -> tuple[bool, Object]:
        """"""
    def TryCreateInstance(
        self, binder: CreateInstanceBinder, args: Array[object], result: Object
    ) -> tuple[bool, Object]:
        """"""
    def TryDeleteIndex(self, binder: DeleteIndexBinder, indexes: Array[object]) -> bool:
        """"""
    def TryDeleteMember(self, binder: DeleteMemberBinder) -> bool:
        """"""
    def TryGetIndex(
        self, binder: GetIndexBinder, indexes: Array[object], result: Object
    ) -> tuple[bool, Object]:
        """"""
    def TryGetMember(self, binder: GetMemberBinder, result: Object) -> tuple[bool, Object]:
        """"""
    def TryInvoke(
        self, binder: InvokeBinder, args: Array[object], result: Object
    ) -> tuple[bool, Object]:
        """"""
    def TryInvokeMember(
        self, binder: InvokeMemberBinder, args: Array[object], result: Object
    ) -> tuple[bool, Object]:
        """"""
    def TrySetIndex(self, binder: SetIndexBinder, indexes: Array[object], value: object) -> bool:
        """"""
    def TrySetMember(self, binder: SetMemberBinder, value: object) -> bool:
        """"""
    def TryUnaryOperation(
        self, binder: UnaryOperationBinder, result: Object
    ) -> tuple[bool, Object]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ExpandoClass(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ExpandoObject(
    Object,
    ICollection[KeyValuePair[String, Object]],
    IDictionary[String, Object],
    IEnumerable[KeyValuePair[String, Object]],
    IEnumerable,
    INotifyPropertyChanged,
    IDynamicMetaObjectProvider,
):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def Item(self) -> object:
        """"""
    @Item.setter
    def Item(self, value: object) -> None: ...
    @property
    def Keys(self) -> ICollection[str]:
        """"""
    @property
    def Values(self) -> ICollection[object]:
        """"""
    @overload
    def Add(self, item: KeyValuePair[str, object]) -> None:
        """"""
    @overload
    def Add(self, key: str, value: object) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    def Contains(self, item: KeyValuePair[str, object]) -> bool:
        """"""
    def ContainsKey(self, key: str) -> bool:
        """"""
    def CopyTo(self, array: Array[KeyValuePair[str, object]], arrayIndex: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator[KeyValuePair[str, object]]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetMetaObject(self, parameter: Expression) -> DynamicMetaObject:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def Remove(self, item: KeyValuePair[str, object]) -> bool:
        """"""
    @overload
    def Remove(self, key: str) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    def TryGetValue(self, key: str, value: Object) -> tuple[bool, Object]:
        """"""
    @overload
    def __contains__(self, item: KeyValuePair[str, object]) -> bool:
        """"""
    @overload
    def __contains__(self, key: str) -> bool:
        """"""
    def __iter__(self) -> Iterator[KeyValuePair[str, object]]:
        """"""
    @overload
    def __delitem__(self, item: KeyValuePair[str, object]) -> bool:
        """"""
    @overload
    def __delitem__(self, key: str) -> bool:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, key: str) -> object:
        """"""
    def __setitem__(self, key: str, value: object) -> None:
        """"""
    PropertyChanged: EventType[PropertyChangedEventHandler] = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class GetIndexBinder(ABC, DynamicMetaObjectBinder):
    """"""
    @property
    def CallInfo(self) -> CallInfo:
        """"""
    @property
    def ReturnType(self) -> Type:
        """"""
    @overload
    def Bind(self, target: DynamicMetaObject, args: Array[DynamicMetaObject]) -> DynamicMetaObject:
        """"""
    @overload
    def Bind(
        self,
        args: Array[object],
        parameters: ReadOnlyCollection[ParameterExpression],
        returnLabel: LabelTarget,
    ) -> Expression:
        """"""
    def BindDelegate[T](self, site: CallSite[T], args: Array[object]) -> T:
        """"""
    @overload
    def Defer(self, target: DynamicMetaObject, args: Array[DynamicMetaObject]) -> DynamicMetaObject:
        """"""
    @overload
    def Defer(self, args: Array[DynamicMetaObject]) -> DynamicMetaObject:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def FallbackGetIndex(
        self, target: DynamicMetaObject, indexes: Array[DynamicMetaObject]
    ) -> DynamicMetaObject:
        """"""
    @overload
    def FallbackGetIndex(
        self,
        target: DynamicMetaObject,
        indexes: Array[DynamicMetaObject],
        errorSuggestion: DynamicMetaObject,
    ) -> DynamicMetaObject:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetUpdateExpression(self, type: Type) -> Expression:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class GetMemberBinder(ABC, DynamicMetaObjectBinder):
    """"""
    @property
    def IgnoreCase(self) -> bool:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def ReturnType(self) -> Type:
        """"""
    @overload
    def Bind(self, target: DynamicMetaObject, args: Array[DynamicMetaObject]) -> DynamicMetaObject:
        """"""
    @overload
    def Bind(
        self,
        args: Array[object],
        parameters: ReadOnlyCollection[ParameterExpression],
        returnLabel: LabelTarget,
    ) -> Expression:
        """"""
    def BindDelegate[T](self, site: CallSite[T], args: Array[object]) -> T:
        """"""
    @overload
    def Defer(self, target: DynamicMetaObject, args: Array[DynamicMetaObject]) -> DynamicMetaObject:
        """"""
    @overload
    def Defer(self, args: Array[DynamicMetaObject]) -> DynamicMetaObject:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def FallbackGetMember(self, target: DynamicMetaObject) -> DynamicMetaObject:
        """"""
    @overload
    def FallbackGetMember(
        self, target: DynamicMetaObject, errorSuggestion: DynamicMetaObject
    ) -> DynamicMetaObject:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetUpdateExpression(self, type: Type) -> Expression:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IDynamicMetaObjectProvider(ABC):
    """"""
    def GetMetaObject(self, parameter: Expression) -> DynamicMetaObject:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IInvokeOnGetBinder(ABC):
    """"""
    @property
    def InvokeOnGet(self) -> bool:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class InvokeBinder(ABC, DynamicMetaObjectBinder):
    """"""
    @property
    def CallInfo(self) -> CallInfo:
        """"""
    @property
    def ReturnType(self) -> Type:
        """"""
    @overload
    def Bind(self, target: DynamicMetaObject, args: Array[DynamicMetaObject]) -> DynamicMetaObject:
        """"""
    @overload
    def Bind(
        self,
        args: Array[object],
        parameters: ReadOnlyCollection[ParameterExpression],
        returnLabel: LabelTarget,
    ) -> Expression:
        """"""
    def BindDelegate[T](self, site: CallSite[T], args: Array[object]) -> T:
        """"""
    @overload
    def Defer(self, target: DynamicMetaObject, args: Array[DynamicMetaObject]) -> DynamicMetaObject:
        """"""
    @overload
    def Defer(self, args: Array[DynamicMetaObject]) -> DynamicMetaObject:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def FallbackInvoke(
        self, target: DynamicMetaObject, args: Array[DynamicMetaObject]
    ) -> DynamicMetaObject:
        """"""
    @overload
    def FallbackInvoke(
        self,
        target: DynamicMetaObject,
        args: Array[DynamicMetaObject],
        errorSuggestion: DynamicMetaObject,
    ) -> DynamicMetaObject:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetUpdateExpression(self, type: Type) -> Expression:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class InvokeMemberBinder(ABC, DynamicMetaObjectBinder):
    """"""
    @property
    def CallInfo(self) -> CallInfo:
        """"""
    @property
    def IgnoreCase(self) -> bool:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def ReturnType(self) -> Type:
        """"""
    @overload
    def Bind(self, target: DynamicMetaObject, args: Array[DynamicMetaObject]) -> DynamicMetaObject:
        """"""
    @overload
    def Bind(
        self,
        args: Array[object],
        parameters: ReadOnlyCollection[ParameterExpression],
        returnLabel: LabelTarget,
    ) -> Expression:
        """"""
    def BindDelegate[T](self, site: CallSite[T], args: Array[object]) -> T:
        """"""
    @overload
    def Defer(self, target: DynamicMetaObject, args: Array[DynamicMetaObject]) -> DynamicMetaObject:
        """"""
    @overload
    def Defer(self, args: Array[DynamicMetaObject]) -> DynamicMetaObject:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def FallbackInvoke(
        self,
        target: DynamicMetaObject,
        args: Array[DynamicMetaObject],
        errorSuggestion: DynamicMetaObject,
    ) -> DynamicMetaObject:
        """"""
    @overload
    def FallbackInvokeMember(
        self, target: DynamicMetaObject, args: Array[DynamicMetaObject]
    ) -> DynamicMetaObject:
        """"""
    @overload
    def FallbackInvokeMember(
        self,
        target: DynamicMetaObject,
        args: Array[DynamicMetaObject],
        errorSuggestion: DynamicMetaObject,
    ) -> DynamicMetaObject:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetUpdateExpression(self, type: Type) -> Expression:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SetIndexBinder(ABC, DynamicMetaObjectBinder):
    """"""
    @property
    def CallInfo(self) -> CallInfo:
        """"""
    @property
    def ReturnType(self) -> Type:
        """"""
    @overload
    def Bind(self, target: DynamicMetaObject, args: Array[DynamicMetaObject]) -> DynamicMetaObject:
        """"""
    @overload
    def Bind(
        self,
        args: Array[object],
        parameters: ReadOnlyCollection[ParameterExpression],
        returnLabel: LabelTarget,
    ) -> Expression:
        """"""
    def BindDelegate[T](self, site: CallSite[T], args: Array[object]) -> T:
        """"""
    @overload
    def Defer(self, target: DynamicMetaObject, args: Array[DynamicMetaObject]) -> DynamicMetaObject:
        """"""
    @overload
    def Defer(self, args: Array[DynamicMetaObject]) -> DynamicMetaObject:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def FallbackSetIndex(
        self, target: DynamicMetaObject, indexes: Array[DynamicMetaObject], value: DynamicMetaObject
    ) -> DynamicMetaObject:
        """"""
    @overload
    def FallbackSetIndex(
        self,
        target: DynamicMetaObject,
        indexes: Array[DynamicMetaObject],
        value: DynamicMetaObject,
        errorSuggestion: DynamicMetaObject,
    ) -> DynamicMetaObject:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetUpdateExpression(self, type: Type) -> Expression:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SetMemberBinder(ABC, DynamicMetaObjectBinder):
    """"""
    @property
    def IgnoreCase(self) -> bool:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def ReturnType(self) -> Type:
        """"""
    @overload
    def Bind(self, target: DynamicMetaObject, args: Array[DynamicMetaObject]) -> DynamicMetaObject:
        """"""
    @overload
    def Bind(
        self,
        args: Array[object],
        parameters: ReadOnlyCollection[ParameterExpression],
        returnLabel: LabelTarget,
    ) -> Expression:
        """"""
    def BindDelegate[T](self, site: CallSite[T], args: Array[object]) -> T:
        """"""
    @overload
    def Defer(self, target: DynamicMetaObject, args: Array[DynamicMetaObject]) -> DynamicMetaObject:
        """"""
    @overload
    def Defer(self, args: Array[DynamicMetaObject]) -> DynamicMetaObject:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def FallbackSetMember(
        self, target: DynamicMetaObject, value: DynamicMetaObject
    ) -> DynamicMetaObject:
        """"""
    @overload
    def FallbackSetMember(
        self,
        target: DynamicMetaObject,
        value: DynamicMetaObject,
        errorSuggestion: DynamicMetaObject,
    ) -> DynamicMetaObject:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetUpdateExpression(self, type: Type) -> Expression:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class UnaryOperationBinder(ABC, DynamicMetaObjectBinder):
    """"""
    @property
    def Operation(self) -> ExpressionType:
        """"""
    @property
    def ReturnType(self) -> Type:
        """"""
    @overload
    def Bind(self, target: DynamicMetaObject, args: Array[DynamicMetaObject]) -> DynamicMetaObject:
        """"""
    @overload
    def Bind(
        self,
        args: Array[object],
        parameters: ReadOnlyCollection[ParameterExpression],
        returnLabel: LabelTarget,
    ) -> Expression:
        """"""
    def BindDelegate[T](self, site: CallSite[T], args: Array[object]) -> T:
        """"""
    @overload
    def Defer(self, target: DynamicMetaObject, args: Array[DynamicMetaObject]) -> DynamicMetaObject:
        """"""
    @overload
    def Defer(self, args: Array[DynamicMetaObject]) -> DynamicMetaObject:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def FallbackUnaryOperation(self, target: DynamicMetaObject) -> DynamicMetaObject:
        """"""
    @overload
    def FallbackUnaryOperation(
        self, target: DynamicMetaObject, errorSuggestion: DynamicMetaObject
    ) -> DynamicMetaObject:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetUpdateExpression(self, type: Type) -> Expression:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class UpdateDelegates(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
