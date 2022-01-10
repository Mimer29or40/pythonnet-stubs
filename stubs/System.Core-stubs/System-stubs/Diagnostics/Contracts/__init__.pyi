from __future__ import annotations

from abc import ABC
from typing import Generic, Tuple, TypeVar, Union, overload

from System import Attribute, Boolean, Enum, EventArgs, EventHandler, Exception, Int32, Object, Predicate, String, Type, Void
from System.Collections.Generic import IEnumerable
from System.Runtime.InteropServices import _Attribute, _Exception
from System.Runtime.Serialization import ISerializable, SerializationInfo, StreamingContext

# ---------- Types ---------- #

T = TypeVar('T')

BooleanType = Union[bool, Boolean]
IntType = Union[int, Int32]
ObjectType = Object
StringType = Union[str, String]
TypeType = Union[type, Type]
VoidType = Union[None, Void]


class EventType(Generic[T]):
    def __iadd__(self, other: T): ...
    
    def __isub__(self, other: T): ...


# ---------- Classes ---------- #

class Contract(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    @overload
    def Assert(condition: BooleanType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Assert(condition: BooleanType, userMessage: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Assume(condition: BooleanType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Assume(condition: BooleanType, userMessage: StringType) -> VoidType: ...
    
    @staticmethod
    def EndContractBlock() -> VoidType: ...
    
    @staticmethod
    @overload
    def Ensures(condition: BooleanType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Ensures(condition: BooleanType, userMessage: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def EnsuresOnThrow(condition: BooleanType) -> VoidType: ...
    
    @staticmethod
    @overload
    def EnsuresOnThrow(condition: BooleanType, userMessage: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Exists(fromInclusive: IntType, toExclusive: IntType, predicate: Predicate[IntType]) -> BooleanType: ...
    
    @staticmethod
    @overload
    def Exists(collection: IEnumerable[T], predicate: Predicate[T]) -> BooleanType: ...
    
    @staticmethod
    @overload
    def ForAll(fromInclusive: IntType, toExclusive: IntType, predicate: Predicate[IntType]) -> BooleanType: ...
    
    @staticmethod
    @overload
    def ForAll(collection: IEnumerable[T], predicate: Predicate[T]) -> BooleanType: ...
    
    @staticmethod
    @overload
    def Invariant(condition: BooleanType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Invariant(condition: BooleanType, userMessage: StringType) -> VoidType: ...
    
    @staticmethod
    def OldValue(value: T) -> T: ...
    
    @staticmethod
    @overload
    def Requires(condition: BooleanType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Requires(condition: BooleanType, userMessage: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Requires(condition: BooleanType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Requires(condition: BooleanType, userMessage: StringType) -> VoidType: ...
    
    @staticmethod
    def Result() -> T: ...
    
    @staticmethod
    def ValueAtReturn(value: T) -> Tuple[T, T]: ...
    
    @staticmethod
    def add_ContractFailed(value: EventHandler[ContractFailedEventArgs]) -> VoidType: ...
    
    @staticmethod
    def remove_ContractFailed(value: EventHandler[ContractFailedEventArgs]) -> VoidType: ...
    
    # ---------- Events ---------- #
    
    ContractFailed: EventType[EventHandler[ContractFailedEventArgs]] = ...
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ContractAbbreviatorAttribute(Attribute, _Attribute):
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


class ContractArgumentValidatorAttribute(Attribute, _Attribute):
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


class ContractClassAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, typeContainingContracts: TypeType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def TypeContainingContracts(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def get_TypeContainingContracts(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ContractClassForAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, typeContractsAreFor: TypeType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def TypeContractsAreFor(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def get_TypeContractsAreFor(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ContractException(Exception, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, kind: ContractFailureKind, failure: StringType, userMessage: StringType, condition: StringType, innerException: Exception): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Condition(self) -> StringType: ...
    
    @property
    def Failure(self) -> StringType: ...
    
    @property
    def Kind(self) -> ContractFailureKind: ...
    
    @property
    def UserMessage(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    
    def get_Condition(self) -> StringType: ...
    
    def get_Failure(self) -> StringType: ...
    
    def get_Kind(self) -> ContractFailureKind: ...
    
    def get_UserMessage(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ContractFailedEventArgs(EventArgs):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, failureKind: ContractFailureKind, message: StringType, condition: StringType, originalException: Exception): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Condition(self) -> StringType: ...
    
    @property
    def FailureKind(self) -> ContractFailureKind: ...
    
    @property
    def Handled(self) -> BooleanType: ...
    
    @property
    def Message(self) -> StringType: ...
    
    @property
    def OriginalException(self) -> Exception: ...
    
    @property
    def Unwind(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def SetHandled(self) -> VoidType: ...
    
    def SetUnwind(self) -> VoidType: ...
    
    def get_Condition(self) -> StringType: ...
    
    def get_FailureKind(self) -> ContractFailureKind: ...
    
    def get_Handled(self) -> BooleanType: ...
    
    def get_Message(self) -> StringType: ...
    
    def get_OriginalException(self) -> Exception: ...
    
    def get_Unwind(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ContractInvariantMethodAttribute(Attribute, _Attribute):
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


class ContractOptionAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, category: StringType, setting: StringType, enabled: BooleanType): ...
    
    @overload
    def __init__(self, category: StringType, setting: StringType, value: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Category(self) -> StringType: ...
    
    @property
    def Enabled(self) -> BooleanType: ...
    
    @property
    def Setting(self) -> StringType: ...
    
    @property
    def Value(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_Category(self) -> StringType: ...
    
    def get_Enabled(self) -> BooleanType: ...
    
    def get_Setting(self) -> StringType: ...
    
    def get_Value(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ContractPublicPropertyNameAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, name: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Name(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_Name(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ContractReferenceAssemblyAttribute(Attribute, _Attribute):
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


class ContractRuntimeIgnoredAttribute(Attribute, _Attribute):
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


class ContractVerificationAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, value: BooleanType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def get_Value(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PureAttribute(Attribute, _Attribute):
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


# No Structs

# No Interfaces

# ---------- Enums ---------- #

class ContractFailureKind(Enum):
    Precondition: IntType = 0
    Postcondition: IntType = 1
    PostconditionOnException: IntType = 2
    Invariant: IntType = 3
    Assert: IntType = 4
    Assume: IntType = 5


# No Delegates

__all__ = [
    Contract,
    ContractAbbreviatorAttribute,
    ContractArgumentValidatorAttribute,
    ContractClassAttribute,
    ContractClassForAttribute,
    ContractException,
    ContractFailedEventArgs,
    ContractInvariantMethodAttribute,
    ContractOptionAttribute,
    ContractPublicPropertyNameAttribute,
    ContractReferenceAssemblyAttribute,
    ContractRuntimeIgnoredAttribute,
    ContractVerificationAttribute,
    PureAttribute,
    ContractFailureKind,
]
