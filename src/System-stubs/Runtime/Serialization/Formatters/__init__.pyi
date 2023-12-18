from __future__ import annotations

from abc import ABC
from typing import List
from typing import Protocol
from typing import Union
from typing import overload

from System import Array
from System import Boolean
from System import Enum
from System import Int32
from System import Object
from System import String
from System import Type
from System import Void
from System.Reflection import Assembly
from System.Reflection import FieldInfo
from System.Runtime.Remoting.Messaging import Header
from System.Runtime.Serialization import ISerializable
from System.Runtime.Serialization import SerializationInfo
from System.Runtime.Serialization import StreamingContext

# ---------- Types ---------- #

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
IntType = Union[int, Int32]
ObjectType = Object
StringType = Union[str, String]
TypeType = Union[type, Type]
VoidType = Union[None, Void]

# ---------- Classes ---------- #

class InternalRM(ObjectType):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # No Properties

    # ---------- Methods ---------- #

    @staticmethod
    def InfoSoap(messages: ArrayType[ObjectType]) -> VoidType: ...
    @staticmethod
    def SoapCheckEnabled() -> BooleanType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class InternalST(ObjectType):
    # No Fields

    # No Constructors

    # No Properties

    # ---------- Methods ---------- #

    @staticmethod
    def InfoSoap(messages: ArrayType[ObjectType]) -> VoidType: ...
    @staticmethod
    def LoadAssemblyFromString(assemblyString: StringType) -> Assembly: ...
    @staticmethod
    def SerializationSetValue(fi: FieldInfo, target: ObjectType, value: ObjectType) -> VoidType: ...
    @staticmethod
    def Soap(messages: ArrayType[ObjectType]) -> VoidType: ...
    @staticmethod
    def SoapAssert(condition: BooleanType, message: StringType) -> VoidType: ...
    @staticmethod
    def SoapCheckEnabled() -> BooleanType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class SerTrace(ABC, ObjectType):
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

class ServerFault(ObjectType):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, exceptionType: StringType, message: StringType, stackTrace: StringType): ...

    # ---------- Properties ---------- #

    @property
    def ExceptionMessage(self) -> StringType: ...
    @ExceptionMessage.setter
    def ExceptionMessage(self, value: StringType) -> None: ...
    @property
    def ExceptionType(self) -> StringType: ...
    @ExceptionType.setter
    def ExceptionType(self, value: StringType) -> None: ...
    @property
    def StackTrace(self) -> StringType: ...
    @StackTrace.setter
    def StackTrace(self, value: StringType) -> None: ...

    # ---------- Methods ---------- #

    def get_ExceptionMessage(self) -> StringType: ...
    def get_ExceptionType(self) -> StringType: ...
    def get_StackTrace(self) -> StringType: ...
    def set_ExceptionMessage(self, value: StringType) -> VoidType: ...
    def set_ExceptionType(self, value: StringType) -> VoidType: ...
    def set_StackTrace(self, value: StringType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class SoapFault(ObjectType, ISerializable):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self): ...
    @overload
    def __init__(
        self,
        faultCode: StringType,
        faultString: StringType,
        faultActor: StringType,
        serverFault: ServerFault,
    ): ...

    # ---------- Properties ---------- #

    @property
    def Detail(self) -> ObjectType: ...
    @Detail.setter
    def Detail(self, value: ObjectType) -> None: ...
    @property
    def FaultActor(self) -> StringType: ...
    @FaultActor.setter
    def FaultActor(self, value: StringType) -> None: ...
    @property
    def FaultCode(self) -> StringType: ...
    @FaultCode.setter
    def FaultCode(self, value: StringType) -> None: ...
    @property
    def FaultString(self) -> StringType: ...
    @FaultString.setter
    def FaultString(self, value: StringType) -> None: ...

    # ---------- Methods ---------- #

    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    def get_Detail(self) -> ObjectType: ...
    def get_FaultActor(self) -> StringType: ...
    def get_FaultCode(self) -> StringType: ...
    def get_FaultString(self) -> StringType: ...
    def set_Detail(self, value: ObjectType) -> VoidType: ...
    def set_FaultActor(self, value: StringType) -> VoidType: ...
    def set_FaultCode(self, value: StringType) -> VoidType: ...
    def set_FaultString(self, value: StringType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class SoapMessage(ObjectType, ISoapMessage):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # ---------- Properties ---------- #

    @property
    def Headers(self) -> ArrayType[Header]: ...
    @Headers.setter
    def Headers(self, value: ArrayType[Header]) -> None: ...
    @property
    def MethodName(self) -> StringType: ...
    @MethodName.setter
    def MethodName(self, value: StringType) -> None: ...
    @property
    def ParamNames(self) -> ArrayType[StringType]: ...
    @ParamNames.setter
    def ParamNames(self, value: ArrayType[StringType]) -> None: ...
    @property
    def ParamTypes(self) -> ArrayType[TypeType]: ...
    @ParamTypes.setter
    def ParamTypes(self, value: ArrayType[TypeType]) -> None: ...
    @property
    def ParamValues(self) -> ArrayType[ObjectType]: ...
    @ParamValues.setter
    def ParamValues(self, value: ArrayType[ObjectType]) -> None: ...
    @property
    def XmlNameSpace(self) -> StringType: ...
    @XmlNameSpace.setter
    def XmlNameSpace(self, value: StringType) -> None: ...

    # ---------- Methods ---------- #

    def get_Headers(self) -> ArrayType[Header]: ...
    def get_MethodName(self) -> StringType: ...
    def get_ParamNames(self) -> ArrayType[StringType]: ...
    def get_ParamTypes(self) -> ArrayType[TypeType]: ...
    def get_ParamValues(self) -> ArrayType[ObjectType]: ...
    def get_XmlNameSpace(self) -> StringType: ...
    def set_Headers(self, value: ArrayType[Header]) -> VoidType: ...
    def set_MethodName(self, value: StringType) -> VoidType: ...
    def set_ParamNames(self, value: ArrayType[StringType]) -> VoidType: ...
    def set_ParamTypes(self, value: ArrayType[TypeType]) -> VoidType: ...
    def set_ParamValues(self, value: ArrayType[ObjectType]) -> VoidType: ...
    def set_XmlNameSpace(self, value: StringType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

# No Structs

# ---------- Interfaces ---------- #

class IFieldInfo(Protocol):
    # ---------- Properties ---------- #

    @property
    def FieldNames(self) -> ArrayType[StringType]: ...
    @FieldNames.setter
    def FieldNames(self, value: ArrayType[StringType]) -> None: ...
    @property
    def FieldTypes(self) -> ArrayType[TypeType]: ...
    @FieldTypes.setter
    def FieldTypes(self, value: ArrayType[TypeType]) -> None: ...

    # ---------- Methods ---------- #

    def get_FieldNames(self) -> ArrayType[StringType]: ...
    def get_FieldTypes(self) -> ArrayType[TypeType]: ...
    def set_FieldNames(self, value: ArrayType[StringType]) -> VoidType: ...
    def set_FieldTypes(self, value: ArrayType[TypeType]) -> VoidType: ...

    # No Events

class ISoapMessage(Protocol):
    # ---------- Properties ---------- #

    @property
    def Headers(self) -> ArrayType[Header]: ...
    @Headers.setter
    def Headers(self, value: ArrayType[Header]) -> None: ...
    @property
    def MethodName(self) -> StringType: ...
    @MethodName.setter
    def MethodName(self, value: StringType) -> None: ...
    @property
    def ParamNames(self) -> ArrayType[StringType]: ...
    @ParamNames.setter
    def ParamNames(self, value: ArrayType[StringType]) -> None: ...
    @property
    def ParamTypes(self) -> ArrayType[TypeType]: ...
    @ParamTypes.setter
    def ParamTypes(self, value: ArrayType[TypeType]) -> None: ...
    @property
    def ParamValues(self) -> ArrayType[ObjectType]: ...
    @ParamValues.setter
    def ParamValues(self, value: ArrayType[ObjectType]) -> None: ...
    @property
    def XmlNameSpace(self) -> StringType: ...
    @XmlNameSpace.setter
    def XmlNameSpace(self, value: StringType) -> None: ...

    # ---------- Methods ---------- #

    def get_Headers(self) -> ArrayType[Header]: ...
    def get_MethodName(self) -> StringType: ...
    def get_ParamNames(self) -> ArrayType[StringType]: ...
    def get_ParamTypes(self) -> ArrayType[TypeType]: ...
    def get_ParamValues(self) -> ArrayType[ObjectType]: ...
    def get_XmlNameSpace(self) -> StringType: ...
    def set_Headers(self, value: ArrayType[Header]) -> VoidType: ...
    def set_MethodName(self, value: StringType) -> VoidType: ...
    def set_ParamNames(self, value: ArrayType[StringType]) -> VoidType: ...
    def set_ParamTypes(self, value: ArrayType[TypeType]) -> VoidType: ...
    def set_ParamValues(self, value: ArrayType[ObjectType]) -> VoidType: ...
    def set_XmlNameSpace(self, value: StringType) -> VoidType: ...

    # No Events

# ---------- Enums ---------- #

class FormatterAssemblyStyle(Enum):
    Simple = 0
    Full = 1

class FormatterTypeStyle(Enum):
    TypesWhenNeeded = 0
    TypesAlways = 1
    XsdString = 2

class TypeFilterLevel(Enum):
    Low = 2
    Full = 3

# No Delegates

__all__ = [
    InternalRM,
    InternalST,
    SerTrace,
    ServerFault,
    SoapFault,
    SoapMessage,
    IFieldInfo,
    ISoapMessage,
    FormatterAssemblyStyle,
    FormatterTypeStyle,
    TypeFilterLevel,
]
