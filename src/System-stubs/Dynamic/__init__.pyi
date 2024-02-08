from __future__ import annotations

from abc import ABC
from typing import ClassVar
from typing import Final
from typing import Generic
from typing import Iterator
from typing import Tuple
from typing import TypeVar
from typing import overload

from System import Array
from System import Object
from System import String
from System import Type
from System.Collections import IEnumerable
from System.Collections import IEnumerator
from System.Collections.Generic import ICollection
from System.Collections.Generic import IDictionary
from System.Collections.Generic import IEnumerable
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

T = TypeVar("T")

class EventType(Generic[T]):
    def __iadd__(self, other: T): ...
    def __isub__(self, other: T): ...

class BinaryOperationBinder(ABC, DynamicMetaObjectBinder):
    """"""

    @property
    def Operation(self) -> ExpressionType:
        """

        :return:
        """
    @property
    def ReturnType(self) -> Type:
        """

        :return:
        """
    @classmethod
    @property
    def UpdateLabel(cls) -> LabelTarget:
        """

        :return:
        """
    @overload
    def Bind(self, target: DynamicMetaObject, args: Array[DynamicMetaObject]) -> DynamicMetaObject:
        """

        :param target:
        :param args:
        :return:
        """
    @overload
    def Bind(
        self,
        args: Array[object],
        parameters: ReadOnlyCollection[ParameterExpression],
        returnLabel: LabelTarget,
    ) -> Expression:
        """

        :param args:
        :param parameters:
        :param returnLabel:
        :return:
        """
    def BindDelegate(self, site: CallSite[T], args: Array[object]) -> T:
        """

        :param site:
        :param args:
        :return:
        """
    @overload
    def Defer(self, args: Array[DynamicMetaObject]) -> DynamicMetaObject:
        """

        :param args:
        :return:
        """
    @overload
    def Defer(self, target: DynamicMetaObject, args: Array[DynamicMetaObject]) -> DynamicMetaObject:
        """

        :param target:
        :param args:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def FallbackBinaryOperation(
        self, target: DynamicMetaObject, arg: DynamicMetaObject
    ) -> DynamicMetaObject:
        """

        :param target:
        :param arg:
        :return:
        """
    @overload
    def FallbackBinaryOperation(
        self, target: DynamicMetaObject, arg: DynamicMetaObject, errorSuggestion: DynamicMetaObject
    ) -> DynamicMetaObject:
        """

        :param target:
        :param arg:
        :param errorSuggestion:
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
    def GetUpdateExpression(self, type: Type) -> Expression:
        """

        :param type:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class BindingRestrictions(ABC, Object):
    """"""

    Empty: Final[ClassVar[BindingRestrictions]] = ...
    """
    
    :return: 
    """
    @classmethod
    def Combine(cls, contributingObjects: IList[DynamicMetaObject]) -> BindingRestrictions:
        """

        :param contributingObjects:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @classmethod
    def GetExpressionRestriction(cls, expression: Expression) -> BindingRestrictions:
        """

        :param expression:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @classmethod
    def GetInstanceRestriction(
        cls, expression: Expression, instance: object
    ) -> BindingRestrictions:
        """

        :param expression:
        :param instance:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @classmethod
    def GetTypeRestriction(cls, expression: Expression, type: Type) -> BindingRestrictions:
        """

        :param expression:
        :param type:
        :return:
        """
    def Merge(self, restrictions: BindingRestrictions) -> BindingRestrictions:
        """

        :param restrictions:
        :return:
        """
    def ToExpression(self) -> Expression:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CallInfo(Object):
    """"""

    @overload
    def __init__(self, argCount: int, argNames: IEnumerable[str]):
        """

        :param argCount:
        :param argNames:
        """
    @overload
    def __init__(self, argCount: int, argNames: Array[str]):
        """

        :param argCount:
        :param argNames:
        """
    @property
    def ArgumentCount(self) -> int:
        """

        :return:
        """
    @property
    def ArgumentNames(self) -> ReadOnlyCollection[str]:
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

class ConvertBinder(ABC, DynamicMetaObjectBinder):
    """"""

    @property
    def Explicit(self) -> bool:
        """

        :return:
        """
    @property
    def ReturnType(self) -> Type:
        """

        :return:
        """
    @property
    def Type(self) -> Type:
        """

        :return:
        """
    @classmethod
    @property
    def UpdateLabel(cls) -> LabelTarget:
        """

        :return:
        """
    @overload
    def Bind(self, target: DynamicMetaObject, args: Array[DynamicMetaObject]) -> DynamicMetaObject:
        """

        :param target:
        :param args:
        :return:
        """
    @overload
    def Bind(
        self,
        args: Array[object],
        parameters: ReadOnlyCollection[ParameterExpression],
        returnLabel: LabelTarget,
    ) -> Expression:
        """

        :param args:
        :param parameters:
        :param returnLabel:
        :return:
        """
    def BindDelegate(self, site: CallSite[T], args: Array[object]) -> T:
        """

        :param site:
        :param args:
        :return:
        """
    @overload
    def Defer(self, args: Array[DynamicMetaObject]) -> DynamicMetaObject:
        """

        :param args:
        :return:
        """
    @overload
    def Defer(self, target: DynamicMetaObject, args: Array[DynamicMetaObject]) -> DynamicMetaObject:
        """

        :param target:
        :param args:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def FallbackConvert(self, target: DynamicMetaObject) -> DynamicMetaObject:
        """

        :param target:
        :return:
        """
    @overload
    def FallbackConvert(
        self, target: DynamicMetaObject, errorSuggestion: DynamicMetaObject
    ) -> DynamicMetaObject:
        """

        :param target:
        :param errorSuggestion:
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
    def GetUpdateExpression(self, type: Type) -> Expression:
        """

        :param type:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CreateInstanceBinder(ABC, DynamicMetaObjectBinder):
    """"""

    @property
    def CallInfo(self) -> CallInfo:
        """

        :return:
        """
    @property
    def ReturnType(self) -> Type:
        """

        :return:
        """
    @classmethod
    @property
    def UpdateLabel(cls) -> LabelTarget:
        """

        :return:
        """
    @overload
    def Bind(self, target: DynamicMetaObject, args: Array[DynamicMetaObject]) -> DynamicMetaObject:
        """

        :param target:
        :param args:
        :return:
        """
    @overload
    def Bind(
        self,
        args: Array[object],
        parameters: ReadOnlyCollection[ParameterExpression],
        returnLabel: LabelTarget,
    ) -> Expression:
        """

        :param args:
        :param parameters:
        :param returnLabel:
        :return:
        """
    def BindDelegate(self, site: CallSite[T], args: Array[object]) -> T:
        """

        :param site:
        :param args:
        :return:
        """
    @overload
    def Defer(self, args: Array[DynamicMetaObject]) -> DynamicMetaObject:
        """

        :param args:
        :return:
        """
    @overload
    def Defer(self, target: DynamicMetaObject, args: Array[DynamicMetaObject]) -> DynamicMetaObject:
        """

        :param target:
        :param args:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def FallbackCreateInstance(
        self, target: DynamicMetaObject, args: Array[DynamicMetaObject]
    ) -> DynamicMetaObject:
        """

        :param target:
        :param args:
        :return:
        """
    @overload
    def FallbackCreateInstance(
        self,
        target: DynamicMetaObject,
        args: Array[DynamicMetaObject],
        errorSuggestion: DynamicMetaObject,
    ) -> DynamicMetaObject:
        """

        :param target:
        :param args:
        :param errorSuggestion:
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
    def GetUpdateExpression(self, type: Type) -> Expression:
        """

        :param type:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class DeleteIndexBinder(ABC, DynamicMetaObjectBinder):
    """"""

    @property
    def CallInfo(self) -> CallInfo:
        """

        :return:
        """
    @property
    def ReturnType(self) -> Type:
        """

        :return:
        """
    @classmethod
    @property
    def UpdateLabel(cls) -> LabelTarget:
        """

        :return:
        """
    @overload
    def Bind(self, target: DynamicMetaObject, args: Array[DynamicMetaObject]) -> DynamicMetaObject:
        """

        :param target:
        :param args:
        :return:
        """
    @overload
    def Bind(
        self,
        args: Array[object],
        parameters: ReadOnlyCollection[ParameterExpression],
        returnLabel: LabelTarget,
    ) -> Expression:
        """

        :param args:
        :param parameters:
        :param returnLabel:
        :return:
        """
    def BindDelegate(self, site: CallSite[T], args: Array[object]) -> T:
        """

        :param site:
        :param args:
        :return:
        """
    @overload
    def Defer(self, args: Array[DynamicMetaObject]) -> DynamicMetaObject:
        """

        :param args:
        :return:
        """
    @overload
    def Defer(self, target: DynamicMetaObject, args: Array[DynamicMetaObject]) -> DynamicMetaObject:
        """

        :param target:
        :param args:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def FallbackDeleteIndex(
        self, target: DynamicMetaObject, indexes: Array[DynamicMetaObject]
    ) -> DynamicMetaObject:
        """

        :param target:
        :param indexes:
        :return:
        """
    @overload
    def FallbackDeleteIndex(
        self,
        target: DynamicMetaObject,
        indexes: Array[DynamicMetaObject],
        errorSuggestion: DynamicMetaObject,
    ) -> DynamicMetaObject:
        """

        :param target:
        :param indexes:
        :param errorSuggestion:
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
    def GetUpdateExpression(self, type: Type) -> Expression:
        """

        :param type:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class DeleteMemberBinder(ABC, DynamicMetaObjectBinder):
    """"""

    @property
    def IgnoreCase(self) -> bool:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def ReturnType(self) -> Type:
        """

        :return:
        """
    @classmethod
    @property
    def UpdateLabel(cls) -> LabelTarget:
        """

        :return:
        """
    @overload
    def Bind(self, target: DynamicMetaObject, args: Array[DynamicMetaObject]) -> DynamicMetaObject:
        """

        :param target:
        :param args:
        :return:
        """
    @overload
    def Bind(
        self,
        args: Array[object],
        parameters: ReadOnlyCollection[ParameterExpression],
        returnLabel: LabelTarget,
    ) -> Expression:
        """

        :param args:
        :param parameters:
        :param returnLabel:
        :return:
        """
    def BindDelegate(self, site: CallSite[T], args: Array[object]) -> T:
        """

        :param site:
        :param args:
        :return:
        """
    @overload
    def Defer(self, args: Array[DynamicMetaObject]) -> DynamicMetaObject:
        """

        :param args:
        :return:
        """
    @overload
    def Defer(self, target: DynamicMetaObject, args: Array[DynamicMetaObject]) -> DynamicMetaObject:
        """

        :param target:
        :param args:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def FallbackDeleteMember(self, target: DynamicMetaObject) -> DynamicMetaObject:
        """

        :param target:
        :return:
        """
    @overload
    def FallbackDeleteMember(
        self, target: DynamicMetaObject, errorSuggestion: DynamicMetaObject
    ) -> DynamicMetaObject:
        """

        :param target:
        :param errorSuggestion:
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
    def GetUpdateExpression(self, type: Type) -> Expression:
        """

        :param type:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class DynamicMetaObject(Object):
    """"""

    EmptyMetaObjects: Final[ClassVar[Array[DynamicMetaObject]]] = ...
    """
    
    :return: 
    """
    @overload
    def __init__(self, expression: Expression, restrictions: BindingRestrictions):
        """

        :param expression:
        :param restrictions:
        """
    @overload
    def __init__(self, expression: Expression, restrictions: BindingRestrictions, value: object):
        """

        :param expression:
        :param restrictions:
        :param value:
        """
    @property
    def Expression(self) -> Expression:
        """

        :return:
        """
    @property
    def HasValue(self) -> bool:
        """

        :return:
        """
    @property
    def LimitType(self) -> Type:
        """

        :return:
        """
    @property
    def Restrictions(self) -> BindingRestrictions:
        """

        :return:
        """
    @property
    def RuntimeType(self) -> Type:
        """

        :return:
        """
    @property
    def Value(self) -> object:
        """

        :return:
        """
    def BindBinaryOperation(
        self, binder: BinaryOperationBinder, arg: DynamicMetaObject
    ) -> DynamicMetaObject:
        """

        :param binder:
        :param arg:
        :return:
        """
    def BindConvert(self, binder: ConvertBinder) -> DynamicMetaObject:
        """

        :param binder:
        :return:
        """
    def BindCreateInstance(
        self, binder: CreateInstanceBinder, args: Array[DynamicMetaObject]
    ) -> DynamicMetaObject:
        """

        :param binder:
        :param args:
        :return:
        """
    def BindDeleteIndex(
        self, binder: DeleteIndexBinder, indexes: Array[DynamicMetaObject]
    ) -> DynamicMetaObject:
        """

        :param binder:
        :param indexes:
        :return:
        """
    def BindDeleteMember(self, binder: DeleteMemberBinder) -> DynamicMetaObject:
        """

        :param binder:
        :return:
        """
    def BindGetIndex(
        self, binder: GetIndexBinder, indexes: Array[DynamicMetaObject]
    ) -> DynamicMetaObject:
        """

        :param binder:
        :param indexes:
        :return:
        """
    def BindGetMember(self, binder: GetMemberBinder) -> DynamicMetaObject:
        """

        :param binder:
        :return:
        """
    def BindInvoke(self, binder: InvokeBinder, args: Array[DynamicMetaObject]) -> DynamicMetaObject:
        """

        :param binder:
        :param args:
        :return:
        """
    def BindInvokeMember(
        self, binder: InvokeMemberBinder, args: Array[DynamicMetaObject]
    ) -> DynamicMetaObject:
        """

        :param binder:
        :param args:
        :return:
        """
    def BindSetIndex(
        self, binder: SetIndexBinder, indexes: Array[DynamicMetaObject], value: DynamicMetaObject
    ) -> DynamicMetaObject:
        """

        :param binder:
        :param indexes:
        :param value:
        :return:
        """
    def BindSetMember(self, binder: SetMemberBinder, value: DynamicMetaObject) -> DynamicMetaObject:
        """

        :param binder:
        :param value:
        :return:
        """
    def BindUnaryOperation(self, binder: UnaryOperationBinder) -> DynamicMetaObject:
        """

        :param binder:
        :return:
        """
    @classmethod
    def Create(cls, value: object, expression: Expression) -> DynamicMetaObject:
        """

        :param value:
        :param expression:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetDynamicMemberNames(self) -> IEnumerable[str]:
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

class DynamicMetaObjectBinder(ABC, CallSiteBinder):
    """"""

    @property
    def ReturnType(self) -> Type:
        """

        :return:
        """
    @classmethod
    @property
    def UpdateLabel(cls) -> LabelTarget:
        """

        :return:
        """
    @overload
    def Bind(self, target: DynamicMetaObject, args: Array[DynamicMetaObject]) -> DynamicMetaObject:
        """

        :param target:
        :param args:
        :return:
        """
    @overload
    def Bind(
        self,
        args: Array[object],
        parameters: ReadOnlyCollection[ParameterExpression],
        returnLabel: LabelTarget,
    ) -> Expression:
        """

        :param args:
        :param parameters:
        :param returnLabel:
        :return:
        """
    def BindDelegate(self, site: CallSite[T], args: Array[object]) -> T:
        """

        :param site:
        :param args:
        :return:
        """
    @overload
    def Defer(self, args: Array[DynamicMetaObject]) -> DynamicMetaObject:
        """

        :param args:
        :return:
        """
    @overload
    def Defer(self, target: DynamicMetaObject, args: Array[DynamicMetaObject]) -> DynamicMetaObject:
        """

        :param target:
        :param args:
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
    def GetUpdateExpression(self, type: Type) -> Expression:
        """

        :param type:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class DynamicObject(Object, IDynamicMetaObjectProvider):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetDynamicMemberNames(self) -> IEnumerable[str]:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetMetaObject(self, parameter: Expression) -> DynamicMetaObject:
        """

        :param parameter:
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
    def TryBinaryOperation(
        self, binder: BinaryOperationBinder, arg: object, result: object
    ) -> Tuple[bool, object]:
        """

        :param binder:
        :param arg:
        :param result:
        :return:
        """
    def TryConvert(self, binder: ConvertBinder, result: object) -> Tuple[bool, object]:
        """

        :param binder:
        :param result:
        :return:
        """
    def TryCreateInstance(
        self, binder: CreateInstanceBinder, args: Array[object], result: object
    ) -> Tuple[bool, object]:
        """

        :param binder:
        :param args:
        :param result:
        :return:
        """
    def TryDeleteIndex(self, binder: DeleteIndexBinder, indexes: Array[object]) -> bool:
        """

        :param binder:
        :param indexes:
        :return:
        """
    def TryDeleteMember(self, binder: DeleteMemberBinder) -> bool:
        """

        :param binder:
        :return:
        """
    def TryGetIndex(
        self, binder: GetIndexBinder, indexes: Array[object], result: object
    ) -> Tuple[bool, object]:
        """

        :param binder:
        :param indexes:
        :param result:
        :return:
        """
    def TryGetMember(self, binder: GetMemberBinder, result: object) -> Tuple[bool, object]:
        """

        :param binder:
        :param result:
        :return:
        """
    def TryInvoke(
        self, binder: InvokeBinder, args: Array[object], result: object
    ) -> Tuple[bool, object]:
        """

        :param binder:
        :param args:
        :param result:
        :return:
        """
    def TryInvokeMember(
        self, binder: InvokeMemberBinder, args: Array[object], result: object
    ) -> Tuple[bool, object]:
        """

        :param binder:
        :param args:
        :param result:
        :return:
        """
    def TrySetIndex(self, binder: SetIndexBinder, indexes: Array[object], value: object) -> bool:
        """

        :param binder:
        :param indexes:
        :param value:
        :return:
        """
    def TrySetMember(self, binder: SetMemberBinder, value: object) -> bool:
        """

        :param binder:
        :param value:
        :return:
        """
    def TryUnaryOperation(
        self, binder: UnaryOperationBinder, result: object
    ) -> Tuple[bool, object]:
        """

        :param binder:
        :param result:
        :return:
        """

class ExpandoClass(Object):
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

class ExpandoObject(
    Object,
    ICollection[KeyValuePair, Object],
    IDictionary[String, Object],
    IEnumerable[KeyValuePair, Object],
    IEnumerable,
    INotifyPropertyChanged,
    IDynamicMetaObjectProvider,
):
    """"""

    def __init__(self):
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
    def Item(self) -> object:
        """

        :return:
        """
    @Item.setter
    def Item(self, value: object) -> None: ...
    @property
    def Keys(self) -> ICollection[str]:
        """

        :return:
        """
    @property
    def Values(self) -> ICollection[object]:
        """

        :return:
        """
    @overload
    def Add(self, item: KeyValuePair[str, object]) -> None:
        """

        :param item:
        """
    @overload
    def Add(self, key: str, value: object) -> None:
        """

        :param key:
        :param value:
        """
    def Clear(self) -> None:
        """"""
    def Contains(self, item: KeyValuePair[str, object]) -> bool:
        """

        :param item:
        :return:
        """
    def ContainsKey(self, key: str) -> bool:
        """

        :param key:
        :return:
        """
    def CopyTo(self, array: Array[KeyValuePair, object], arrayIndex: int) -> None:
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
    def GetMetaObject(self, parameter: Expression) -> DynamicMetaObject:
        """

        :param parameter:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def Remove(self, item: KeyValuePair[str, object]) -> bool:
        """

        :param item:
        :return:
        """
    @overload
    def Remove(self, key: str) -> bool:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """
    def TryGetValue(self, key: str, value: object) -> Tuple[bool, object]:
        """"""
    def __contains__(self, value: KeyValuePair[str, object]) -> bool:
        """

        :param value:
        :return:
        """
    def __getitem__(self, key: str) -> object:
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
    def __iter__(self) -> Iterator[KeyValuePair, object]:
        """

        :return:
        """
    def __len__(self) -> int:
        """

        :return:
        """
    def __setitem__(self, key: str, value: object) -> None:
        """

        :param key:
        :param value:
        """
    PropertyChanged: EventType[PropertyChangedEventHandler] = ...
    """"""

class GetIndexBinder(ABC, DynamicMetaObjectBinder):
    """"""

    @property
    def CallInfo(self) -> CallInfo:
        """

        :return:
        """
    @property
    def ReturnType(self) -> Type:
        """

        :return:
        """
    @classmethod
    @property
    def UpdateLabel(cls) -> LabelTarget:
        """

        :return:
        """
    @overload
    def Bind(self, target: DynamicMetaObject, args: Array[DynamicMetaObject]) -> DynamicMetaObject:
        """

        :param target:
        :param args:
        :return:
        """
    @overload
    def Bind(
        self,
        args: Array[object],
        parameters: ReadOnlyCollection[ParameterExpression],
        returnLabel: LabelTarget,
    ) -> Expression:
        """

        :param args:
        :param parameters:
        :param returnLabel:
        :return:
        """
    def BindDelegate(self, site: CallSite[T], args: Array[object]) -> T:
        """

        :param site:
        :param args:
        :return:
        """
    @overload
    def Defer(self, args: Array[DynamicMetaObject]) -> DynamicMetaObject:
        """

        :param args:
        :return:
        """
    @overload
    def Defer(self, target: DynamicMetaObject, args: Array[DynamicMetaObject]) -> DynamicMetaObject:
        """

        :param target:
        :param args:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def FallbackGetIndex(
        self, target: DynamicMetaObject, indexes: Array[DynamicMetaObject]
    ) -> DynamicMetaObject:
        """

        :param target:
        :param indexes:
        :return:
        """
    @overload
    def FallbackGetIndex(
        self,
        target: DynamicMetaObject,
        indexes: Array[DynamicMetaObject],
        errorSuggestion: DynamicMetaObject,
    ) -> DynamicMetaObject:
        """

        :param target:
        :param indexes:
        :param errorSuggestion:
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
    def GetUpdateExpression(self, type: Type) -> Expression:
        """

        :param type:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class GetMemberBinder(ABC, DynamicMetaObjectBinder):
    """"""

    @property
    def IgnoreCase(self) -> bool:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def ReturnType(self) -> Type:
        """

        :return:
        """
    @classmethod
    @property
    def UpdateLabel(cls) -> LabelTarget:
        """

        :return:
        """
    @overload
    def Bind(self, target: DynamicMetaObject, args: Array[DynamicMetaObject]) -> DynamicMetaObject:
        """

        :param target:
        :param args:
        :return:
        """
    @overload
    def Bind(
        self,
        args: Array[object],
        parameters: ReadOnlyCollection[ParameterExpression],
        returnLabel: LabelTarget,
    ) -> Expression:
        """

        :param args:
        :param parameters:
        :param returnLabel:
        :return:
        """
    def BindDelegate(self, site: CallSite[T], args: Array[object]) -> T:
        """

        :param site:
        :param args:
        :return:
        """
    @overload
    def Defer(self, args: Array[DynamicMetaObject]) -> DynamicMetaObject:
        """

        :param args:
        :return:
        """
    @overload
    def Defer(self, target: DynamicMetaObject, args: Array[DynamicMetaObject]) -> DynamicMetaObject:
        """

        :param target:
        :param args:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def FallbackGetMember(self, target: DynamicMetaObject) -> DynamicMetaObject:
        """

        :param target:
        :return:
        """
    @overload
    def FallbackGetMember(
        self, target: DynamicMetaObject, errorSuggestion: DynamicMetaObject
    ) -> DynamicMetaObject:
        """

        :param target:
        :param errorSuggestion:
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
    def GetUpdateExpression(self, type: Type) -> Expression:
        """

        :param type:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class IDynamicMetaObjectProvider:
    """"""

    def GetMetaObject(self, parameter: Expression) -> DynamicMetaObject:
        """

        :param parameter:
        :return:
        """

class IInvokeOnGetBinder:
    """"""

    @property
    def InvokeOnGet(self) -> bool:
        """

        :return:
        """

class InvokeBinder(ABC, DynamicMetaObjectBinder):
    """"""

    @property
    def CallInfo(self) -> CallInfo:
        """

        :return:
        """
    @property
    def ReturnType(self) -> Type:
        """

        :return:
        """
    @classmethod
    @property
    def UpdateLabel(cls) -> LabelTarget:
        """

        :return:
        """
    @overload
    def Bind(self, target: DynamicMetaObject, args: Array[DynamicMetaObject]) -> DynamicMetaObject:
        """

        :param target:
        :param args:
        :return:
        """
    @overload
    def Bind(
        self,
        args: Array[object],
        parameters: ReadOnlyCollection[ParameterExpression],
        returnLabel: LabelTarget,
    ) -> Expression:
        """

        :param args:
        :param parameters:
        :param returnLabel:
        :return:
        """
    def BindDelegate(self, site: CallSite[T], args: Array[object]) -> T:
        """

        :param site:
        :param args:
        :return:
        """
    @overload
    def Defer(self, args: Array[DynamicMetaObject]) -> DynamicMetaObject:
        """

        :param args:
        :return:
        """
    @overload
    def Defer(self, target: DynamicMetaObject, args: Array[DynamicMetaObject]) -> DynamicMetaObject:
        """

        :param target:
        :param args:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def FallbackInvoke(
        self, target: DynamicMetaObject, args: Array[DynamicMetaObject]
    ) -> DynamicMetaObject:
        """

        :param target:
        :param args:
        :return:
        """
    @overload
    def FallbackInvoke(
        self,
        target: DynamicMetaObject,
        args: Array[DynamicMetaObject],
        errorSuggestion: DynamicMetaObject,
    ) -> DynamicMetaObject:
        """

        :param target:
        :param args:
        :param errorSuggestion:
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
    def GetUpdateExpression(self, type: Type) -> Expression:
        """

        :param type:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class InvokeMemberBinder(ABC, DynamicMetaObjectBinder):
    """"""

    @property
    def CallInfo(self) -> CallInfo:
        """

        :return:
        """
    @property
    def IgnoreCase(self) -> bool:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def ReturnType(self) -> Type:
        """

        :return:
        """
    @classmethod
    @property
    def UpdateLabel(cls) -> LabelTarget:
        """

        :return:
        """
    @overload
    def Bind(self, target: DynamicMetaObject, args: Array[DynamicMetaObject]) -> DynamicMetaObject:
        """

        :param target:
        :param args:
        :return:
        """
    @overload
    def Bind(
        self,
        args: Array[object],
        parameters: ReadOnlyCollection[ParameterExpression],
        returnLabel: LabelTarget,
    ) -> Expression:
        """

        :param args:
        :param parameters:
        :param returnLabel:
        :return:
        """
    def BindDelegate(self, site: CallSite[T], args: Array[object]) -> T:
        """

        :param site:
        :param args:
        :return:
        """
    @overload
    def Defer(self, args: Array[DynamicMetaObject]) -> DynamicMetaObject:
        """

        :param args:
        :return:
        """
    @overload
    def Defer(self, target: DynamicMetaObject, args: Array[DynamicMetaObject]) -> DynamicMetaObject:
        """

        :param target:
        :param args:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def FallbackInvoke(
        self,
        target: DynamicMetaObject,
        args: Array[DynamicMetaObject],
        errorSuggestion: DynamicMetaObject,
    ) -> DynamicMetaObject:
        """

        :param target:
        :param args:
        :param errorSuggestion:
        :return:
        """
    @overload
    def FallbackInvokeMember(
        self, target: DynamicMetaObject, args: Array[DynamicMetaObject]
    ) -> DynamicMetaObject:
        """

        :param target:
        :param args:
        :return:
        """
    @overload
    def FallbackInvokeMember(
        self,
        target: DynamicMetaObject,
        args: Array[DynamicMetaObject],
        errorSuggestion: DynamicMetaObject,
    ) -> DynamicMetaObject:
        """

        :param target:
        :param args:
        :param errorSuggestion:
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
    def GetUpdateExpression(self, type: Type) -> Expression:
        """

        :param type:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class SetIndexBinder(ABC, DynamicMetaObjectBinder):
    """"""

    @property
    def CallInfo(self) -> CallInfo:
        """

        :return:
        """
    @property
    def ReturnType(self) -> Type:
        """

        :return:
        """
    @classmethod
    @property
    def UpdateLabel(cls) -> LabelTarget:
        """

        :return:
        """
    @overload
    def Bind(self, target: DynamicMetaObject, args: Array[DynamicMetaObject]) -> DynamicMetaObject:
        """

        :param target:
        :param args:
        :return:
        """
    @overload
    def Bind(
        self,
        args: Array[object],
        parameters: ReadOnlyCollection[ParameterExpression],
        returnLabel: LabelTarget,
    ) -> Expression:
        """

        :param args:
        :param parameters:
        :param returnLabel:
        :return:
        """
    def BindDelegate(self, site: CallSite[T], args: Array[object]) -> T:
        """

        :param site:
        :param args:
        :return:
        """
    @overload
    def Defer(self, args: Array[DynamicMetaObject]) -> DynamicMetaObject:
        """

        :param args:
        :return:
        """
    @overload
    def Defer(self, target: DynamicMetaObject, args: Array[DynamicMetaObject]) -> DynamicMetaObject:
        """

        :param target:
        :param args:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def FallbackSetIndex(
        self, target: DynamicMetaObject, indexes: Array[DynamicMetaObject], value: DynamicMetaObject
    ) -> DynamicMetaObject:
        """

        :param target:
        :param indexes:
        :param value:
        :return:
        """
    @overload
    def FallbackSetIndex(
        self,
        target: DynamicMetaObject,
        indexes: Array[DynamicMetaObject],
        value: DynamicMetaObject,
        errorSuggestion: DynamicMetaObject,
    ) -> DynamicMetaObject:
        """

        :param target:
        :param indexes:
        :param value:
        :param errorSuggestion:
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
    def GetUpdateExpression(self, type: Type) -> Expression:
        """

        :param type:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class SetMemberBinder(ABC, DynamicMetaObjectBinder):
    """"""

    @property
    def IgnoreCase(self) -> bool:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def ReturnType(self) -> Type:
        """

        :return:
        """
    @classmethod
    @property
    def UpdateLabel(cls) -> LabelTarget:
        """

        :return:
        """
    @overload
    def Bind(self, target: DynamicMetaObject, args: Array[DynamicMetaObject]) -> DynamicMetaObject:
        """

        :param target:
        :param args:
        :return:
        """
    @overload
    def Bind(
        self,
        args: Array[object],
        parameters: ReadOnlyCollection[ParameterExpression],
        returnLabel: LabelTarget,
    ) -> Expression:
        """

        :param args:
        :param parameters:
        :param returnLabel:
        :return:
        """
    def BindDelegate(self, site: CallSite[T], args: Array[object]) -> T:
        """

        :param site:
        :param args:
        :return:
        """
    @overload
    def Defer(self, args: Array[DynamicMetaObject]) -> DynamicMetaObject:
        """

        :param args:
        :return:
        """
    @overload
    def Defer(self, target: DynamicMetaObject, args: Array[DynamicMetaObject]) -> DynamicMetaObject:
        """

        :param target:
        :param args:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def FallbackSetMember(
        self, target: DynamicMetaObject, value: DynamicMetaObject
    ) -> DynamicMetaObject:
        """

        :param target:
        :param value:
        :return:
        """
    @overload
    def FallbackSetMember(
        self,
        target: DynamicMetaObject,
        value: DynamicMetaObject,
        errorSuggestion: DynamicMetaObject,
    ) -> DynamicMetaObject:
        """

        :param target:
        :param value:
        :param errorSuggestion:
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
    def GetUpdateExpression(self, type: Type) -> Expression:
        """

        :param type:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class UnaryOperationBinder(ABC, DynamicMetaObjectBinder):
    """"""

    @property
    def Operation(self) -> ExpressionType:
        """

        :return:
        """
    @property
    def ReturnType(self) -> Type:
        """

        :return:
        """
    @classmethod
    @property
    def UpdateLabel(cls) -> LabelTarget:
        """

        :return:
        """
    @overload
    def Bind(self, target: DynamicMetaObject, args: Array[DynamicMetaObject]) -> DynamicMetaObject:
        """

        :param target:
        :param args:
        :return:
        """
    @overload
    def Bind(
        self,
        args: Array[object],
        parameters: ReadOnlyCollection[ParameterExpression],
        returnLabel: LabelTarget,
    ) -> Expression:
        """

        :param args:
        :param parameters:
        :param returnLabel:
        :return:
        """
    def BindDelegate(self, site: CallSite[T], args: Array[object]) -> T:
        """

        :param site:
        :param args:
        :return:
        """
    @overload
    def Defer(self, args: Array[DynamicMetaObject]) -> DynamicMetaObject:
        """

        :param args:
        :return:
        """
    @overload
    def Defer(self, target: DynamicMetaObject, args: Array[DynamicMetaObject]) -> DynamicMetaObject:
        """

        :param target:
        :param args:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def FallbackUnaryOperation(self, target: DynamicMetaObject) -> DynamicMetaObject:
        """

        :param target:
        :return:
        """
    @overload
    def FallbackUnaryOperation(
        self, target: DynamicMetaObject, errorSuggestion: DynamicMetaObject
    ) -> DynamicMetaObject:
        """

        :param target:
        :param errorSuggestion:
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
    def GetUpdateExpression(self, type: Type) -> Expression:
        """

        :param type:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class UpdateDelegates(ABC, Object):
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
