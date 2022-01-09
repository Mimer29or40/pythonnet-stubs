from __future__ import annotations

from abc import ABC
from typing import Generic, List, Protocol, Tuple, TypeVar, Union, overload

from System import Array, Attribute, Boolean, Delegate, Int32, Int64, Object, String, Type, Void
from System.Collections import ICollection, IEnumerable, IList
from System.Collections.Generic import ICollection, IEnumerable, IEnumerator, IList, IReadOnlyCollection, IReadOnlyList
from System.Collections.ObjectModel import ReadOnlyCollection
from System.Dynamic import ExpandoObject
from System.Linq.Expressions import DebugInfoExpression, Expression, LabelTarget, LambdaExpression, ParameterExpression
from System.Reflection import MethodBase
from System.Runtime.InteropServices import _Attribute

# ---------- Types ---------- #

T = TypeVar('T')

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
IntType = Union[int, Int32]
LongType = Union[int, Int64]
ObjectType = Object
StringType = Union[str, String]
TypeType = Union[type, Type]
VoidType = Union[None, Void]

# ---------- Classes ---------- #

class CallSite(ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Binder(self) -> CallSiteBinder: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def Create(delegateType: TypeType, binder: CallSiteBinder) -> CallSite: ...
    
    def get_Binder(self) -> CallSiteBinder: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CallSite(Generic[T], CallSite):
    # ---------- Fields ---------- #
    
    @property
    def Target(self) -> T: ...
    
    @Target.setter
    def Target(self, value: T) -> None: ...
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Update(self) -> T: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def Create(binder: CallSiteBinder) -> CallSite[T]: ...
    
    def get_Update(self) -> T: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CallSiteBinder(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def UpdateLabel() -> LabelTarget: ...
    
    # ---------- Methods ---------- #
    
    def Bind(self, args: ArrayType[ObjectType], parameters: ReadOnlyCollection[ParameterExpression], returnLabel: LabelTarget) -> Expression: ...
    
    def BindDelegate(self, site: CallSite[T], args: ArrayType[ObjectType]) -> T: ...
    
    @staticmethod
    def get_UpdateLabel() -> LabelTarget: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CallSiteHelpers(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def IsInternalFrame(mb: MethodBase) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CallSiteOps(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def AddRule(site: CallSite[T], rule: T) -> VoidType: ...
    
    @staticmethod
    def Bind(binder: CallSiteBinder, site: CallSite[T], args: ArrayType[ObjectType]) -> T: ...
    
    @staticmethod
    def ClearMatch(site: CallSite) -> VoidType: ...
    
    @staticmethod
    def CreateMatchmaker(site: CallSite[T]) -> CallSite[T]: ...
    
    @staticmethod
    def GetCachedRules(cache: RuleCache[T]) -> ArrayType[T]: ...
    
    @staticmethod
    def GetMatch(site: CallSite) -> BooleanType: ...
    
    @staticmethod
    def GetRuleCache(site: CallSite[T]) -> RuleCache[T]: ...
    
    @staticmethod
    def GetRules(site: CallSite[T]) -> ArrayType[T]: ...
    
    @staticmethod
    def MoveRule(cache: RuleCache[T], rule: T, i: IntType) -> VoidType: ...
    
    @staticmethod
    def SetNotMatched(site: CallSite) -> BooleanType: ...
    
    @staticmethod
    def UpdateRules(this: CallSite[T], matched: IntType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Closure(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def Constants(self) -> ArrayType[ObjectType]: ...
    
    @property
    def Locals(self) -> ArrayType[ObjectType]: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self, constants: ArrayType[ObjectType], locals: ArrayType[ObjectType]): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DebugInfoGenerator(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def CreatePdbGenerator() -> DebugInfoGenerator: ...
    
    def MarkSequencePoint(self, method: LambdaExpression, ilOffset: IntType, sequencePoint: DebugInfoExpression) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DynamicAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, transformFlags: ArrayType[BooleanType]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def TransformFlags(self) -> IList[BooleanType]: ...
    
    # ---------- Methods ---------- #
    
    def get_TransformFlags(self) -> IList[BooleanType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ExecutionScope(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def Globals(self) -> ArrayType[ObjectType]: ...
    
    @Globals.setter
    def Globals(self, value: ArrayType[ObjectType]) -> None: ...
    
    @property
    def Locals(self) -> ArrayType[ObjectType]: ...
    
    @Locals.setter
    def Locals(self, value: ArrayType[ObjectType]) -> None: ...
    
    @property
    def Parent(self) -> ExecutionScope: ...
    
    @Parent.setter
    def Parent(self, value: ExecutionScope) -> None: ...
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def CreateDelegate(self, indexLambda: IntType, locals: ArrayType[ObjectType]) -> Delegate: ...
    
    def CreateHoistedLocals(self) -> ArrayType[ObjectType]: ...
    
    def IsolateExpression(self, expression: Expression, locals: ArrayType[ObjectType]) -> Expression: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ReadOnlyCollectionBuilder(Generic[T], ObjectType, IList[T], ICollection[T], IEnumerable[T], IEnumerable, IList, ICollection):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, capacity: IntType): ...
    
    @overload
    def __init__(self, collection: IEnumerable[T]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Capacity(self) -> IntType: ...
    
    @Capacity.setter
    def Capacity(self, value: IntType) -> None: ...
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def Item(self) -> T: ...
    
    @Item.setter
    def Item(self, value: T) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, item: T) -> VoidType: ...
    
    def Clear(self) -> VoidType: ...
    
    def Contains(self, item: T) -> BooleanType: ...
    
    def CopyTo(self, array: ArrayType[T], arrayIndex: IntType) -> VoidType: ...
    
    def GetEnumerator(self) -> IEnumerator[T]: ...
    
    def IndexOf(self, item: T) -> IntType: ...
    
    def Insert(self, index: IntType, item: T) -> VoidType: ...
    
    def Remove(self, item: T) -> BooleanType: ...
    
    def RemoveAt(self, index: IntType) -> VoidType: ...
    
    @overload
    def Reverse(self) -> VoidType: ...
    
    @overload
    def Reverse(self, index: IntType, count: IntType) -> VoidType: ...
    
    def ToArray(self) -> ArrayType[T]: ...
    
    def ToReadOnlyCollection(self) -> ReadOnlyCollection[T]: ...
    
    def get_Capacity(self) -> IntType: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_Item(self, index: IntType) -> T: ...
    
    def set_Capacity(self, value: IntType) -> VoidType: ...
    
    def set_Item(self, index: IntType, value: T) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RuleCache(Generic[T], ObjectType):
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


class RuntimeOps(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    @overload
    def CreateRuntimeVariables(data: ArrayType[ObjectType], indexes: ArrayType[LongType]) -> IRuntimeVariables: ...
    
    @staticmethod
    @overload
    def CreateRuntimeVariables() -> IRuntimeVariables: ...
    
    @staticmethod
    def ExpandoCheckVersion(expando: ExpandoObject, version: ObjectType) -> BooleanType: ...
    
    @staticmethod
    def ExpandoPromoteClass(expando: ExpandoObject, oldClass: ObjectType, newClass: ObjectType) -> VoidType: ...
    
    @staticmethod
    def ExpandoTryDeleteValue(expando: ExpandoObject, indexClass: ObjectType, index: IntType, name: StringType, ignoreCase: BooleanType) -> BooleanType: ...
    
    @staticmethod
    def ExpandoTryGetValue(expando: ExpandoObject, indexClass: ObjectType, index: IntType, name: StringType, ignoreCase: BooleanType, value: ObjectType) -> Tuple[BooleanType, ObjectType]: ...
    
    @staticmethod
    def ExpandoTrySetValue(expando: ExpandoObject, indexClass: ObjectType, index: IntType, value: ObjectType, name: StringType, ignoreCase: BooleanType) -> ObjectType: ...
    
    @staticmethod
    def MergeRuntimeVariables(first: IRuntimeVariables, second: IRuntimeVariables, indexes: ArrayType[IntType]) -> IRuntimeVariables: ...
    
    @staticmethod
    def Quote(expression: Expression, hoistedLocals: ObjectType, locals: ArrayType[ObjectType]) -> Expression: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class StrongBox(Generic[T], ObjectType, IStrongBox):
    # ---------- Fields ---------- #
    
    @property
    def Value(self) -> T: ...
    
    @Value.setter
    def Value(self, value: T) -> None: ...
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: T): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SymbolDocumentGenerator(DebugInfoGenerator):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def MarkSequencePoint(self, method: LambdaExpression, ilOffset: IntType, sequencePoint: DebugInfoExpression) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TrueReadOnlyCollection(Generic[T], ReadOnlyCollection[T], IList[T], ICollection[T], IEnumerable[T], IEnumerable, IList, ICollection, IReadOnlyList[T], IReadOnlyCollection[T]):
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

class IRuntimeVariables(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def Item(self) -> ObjectType: ...
    
    @Item.setter
    def Item(self, value: ObjectType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Count(self) -> IntType: ...
    
    def get_Item(self, index: IntType) -> ObjectType: ...
    
    def set_Item(self, index: IntType, value: ObjectType) -> VoidType: ...
    
    # No Events


class IStrongBox(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> ObjectType: ...
    
    @Value.setter
    def Value(self, value: ObjectType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Value(self) -> ObjectType: ...
    
    def set_Value(self, value: ObjectType) -> VoidType: ...
    
    # No Events


# No Enums

# No Delegates

__all__ = [
    CallSite,
    CallSiteBinder,
    CallSiteHelpers,
    CallSiteOps,
    Closure,
    DebugInfoGenerator,
    DynamicAttribute,
    ExecutionScope,
    ReadOnlyCollectionBuilder,
    RuleCache,
    RuntimeOps,
    StrongBox,
    SymbolDocumentGenerator,
    TrueReadOnlyCollection,
    IRuntimeVariables,
    IStrongBox,
]
