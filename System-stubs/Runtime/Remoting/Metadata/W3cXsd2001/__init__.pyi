from __future__ import annotations

from abc import ABC
from typing import List, Protocol, Union, overload

from System import Array, Byte, DateTime, Decimal, Int32, Object, String, TimeSpan, Void

# ---------- Types ---------- #

ArrayType = Union[List, Array]
ByteType = Union[int, Byte]
DecimalType = Union[float, Decimal]
IntType = Union[int, Int32]
ObjectType = Object
StringType = Union[str, String]
VoidType = Union[None, Void]

# ---------- Classes ---------- #

class SoapAnyUri(ObjectType, ISoapXsd):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> StringType: ...
    
    @Value.setter
    def Value(self, value: StringType) -> None: ...
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    @staticmethod
    def Parse(value: StringType) -> SoapAnyUri: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Value(self) -> StringType: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    def set_Value(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapAnyUri(ObjectType, ISoapXsd):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> StringType: ...
    
    @Value.setter
    def Value(self, value: StringType) -> None: ...
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    @staticmethod
    def Parse(value: StringType) -> SoapAnyUri: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Value(self) -> StringType: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    def set_Value(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapAnyUri(ObjectType, ISoapXsd):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> StringType: ...
    
    @Value.setter
    def Value(self, value: StringType) -> None: ...
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    @staticmethod
    def Parse(value: StringType) -> SoapAnyUri: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Value(self) -> StringType: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    def set_Value(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapBase64Binary(ObjectType, ISoapXsd):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: ArrayType[ByteType]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> ArrayType[ByteType]: ...
    
    @Value.setter
    def Value(self, value: ArrayType[ByteType]) -> None: ...
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    @staticmethod
    def Parse(value: StringType) -> SoapBase64Binary: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Value(self) -> ArrayType[ByteType]: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    def set_Value(self, value: ArrayType[ByteType]) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapBase64Binary(ObjectType, ISoapXsd):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: ArrayType[ByteType]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> ArrayType[ByteType]: ...
    
    @Value.setter
    def Value(self, value: ArrayType[ByteType]) -> None: ...
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    @staticmethod
    def Parse(value: StringType) -> SoapBase64Binary: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Value(self) -> ArrayType[ByteType]: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    def set_Value(self, value: ArrayType[ByteType]) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapBase64Binary(ObjectType, ISoapXsd):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: ArrayType[ByteType]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> ArrayType[ByteType]: ...
    
    @Value.setter
    def Value(self, value: ArrayType[ByteType]) -> None: ...
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    @staticmethod
    def Parse(value: StringType) -> SoapBase64Binary: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Value(self) -> ArrayType[ByteType]: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    def set_Value(self, value: ArrayType[ByteType]) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapDate(ObjectType, ISoapXsd):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: DateTime): ...
    
    @overload
    def __init__(self, value: DateTime, sign: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Sign(self) -> IntType: ...
    
    @Sign.setter
    def Sign(self, value: IntType) -> None: ...
    
    @property
    def Value(self) -> DateTime: ...
    
    @Value.setter
    def Value(self, value: DateTime) -> None: ...
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    @staticmethod
    def Parse(value: StringType) -> SoapDate: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Sign(self) -> IntType: ...
    
    def get_Value(self) -> DateTime: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    def set_Sign(self, value: IntType) -> VoidType: ...
    
    def set_Value(self, value: DateTime) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapDate(ObjectType, ISoapXsd):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: DateTime): ...
    
    @overload
    def __init__(self, value: DateTime, sign: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Sign(self) -> IntType: ...
    
    @Sign.setter
    def Sign(self, value: IntType) -> None: ...
    
    @property
    def Value(self) -> DateTime: ...
    
    @Value.setter
    def Value(self, value: DateTime) -> None: ...
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    @staticmethod
    def Parse(value: StringType) -> SoapDate: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Sign(self) -> IntType: ...
    
    def get_Value(self) -> DateTime: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    def set_Sign(self, value: IntType) -> VoidType: ...
    
    def set_Value(self, value: DateTime) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapDate(ObjectType, ISoapXsd):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: DateTime): ...
    
    @overload
    def __init__(self, value: DateTime, sign: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Sign(self) -> IntType: ...
    
    @Sign.setter
    def Sign(self, value: IntType) -> None: ...
    
    @property
    def Value(self) -> DateTime: ...
    
    @Value.setter
    def Value(self, value: DateTime) -> None: ...
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    @staticmethod
    def Parse(value: StringType) -> SoapDate: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Sign(self) -> IntType: ...
    
    def get_Value(self) -> DateTime: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    def set_Sign(self, value: IntType) -> VoidType: ...
    
    def set_Value(self, value: DateTime) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapDateTime(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def Parse(value: StringType) -> DateTime: ...
    
    @staticmethod
    @overload
    def ToString(value: DateTime) -> StringType: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapDateTime(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def Parse(value: StringType) -> DateTime: ...
    
    @staticmethod
    @overload
    def ToString(value: DateTime) -> StringType: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapDateTime(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def Parse(value: StringType) -> DateTime: ...
    
    @staticmethod
    @overload
    def ToString(value: DateTime) -> StringType: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapDay(ObjectType, ISoapXsd):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: DateTime): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> DateTime: ...
    
    @Value.setter
    def Value(self, value: DateTime) -> None: ...
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    @staticmethod
    def Parse(value: StringType) -> SoapDay: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Value(self) -> DateTime: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    def set_Value(self, value: DateTime) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapDay(ObjectType, ISoapXsd):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: DateTime): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> DateTime: ...
    
    @Value.setter
    def Value(self, value: DateTime) -> None: ...
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    @staticmethod
    def Parse(value: StringType) -> SoapDay: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Value(self) -> DateTime: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    def set_Value(self, value: DateTime) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapDay(ObjectType, ISoapXsd):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: DateTime): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> DateTime: ...
    
    @Value.setter
    def Value(self, value: DateTime) -> None: ...
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    @staticmethod
    def Parse(value: StringType) -> SoapDay: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Value(self) -> DateTime: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    def set_Value(self, value: DateTime) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapDuration(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def Parse(value: StringType) -> TimeSpan: ...
    
    @staticmethod
    @overload
    def ToString(timeSpan: TimeSpan) -> StringType: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapDuration(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def Parse(value: StringType) -> TimeSpan: ...
    
    @staticmethod
    @overload
    def ToString(timeSpan: TimeSpan) -> StringType: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapDuration(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def Parse(value: StringType) -> TimeSpan: ...
    
    @staticmethod
    @overload
    def ToString(timeSpan: TimeSpan) -> StringType: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapEntities(ObjectType, ISoapXsd):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> StringType: ...
    
    @Value.setter
    def Value(self, value: StringType) -> None: ...
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    @staticmethod
    def Parse(value: StringType) -> SoapEntities: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Value(self) -> StringType: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    def set_Value(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapEntities(ObjectType, ISoapXsd):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> StringType: ...
    
    @Value.setter
    def Value(self, value: StringType) -> None: ...
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    @staticmethod
    def Parse(value: StringType) -> SoapEntities: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Value(self) -> StringType: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    def set_Value(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapEntities(ObjectType, ISoapXsd):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> StringType: ...
    
    @Value.setter
    def Value(self, value: StringType) -> None: ...
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    @staticmethod
    def Parse(value: StringType) -> SoapEntities: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Value(self) -> StringType: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    def set_Value(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapEntity(ObjectType, ISoapXsd):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> StringType: ...
    
    @Value.setter
    def Value(self, value: StringType) -> None: ...
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    @staticmethod
    def Parse(value: StringType) -> SoapEntity: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Value(self) -> StringType: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    def set_Value(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapEntity(ObjectType, ISoapXsd):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> StringType: ...
    
    @Value.setter
    def Value(self, value: StringType) -> None: ...
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    @staticmethod
    def Parse(value: StringType) -> SoapEntity: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Value(self) -> StringType: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    def set_Value(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapEntity(ObjectType, ISoapXsd):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> StringType: ...
    
    @Value.setter
    def Value(self, value: StringType) -> None: ...
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    @staticmethod
    def Parse(value: StringType) -> SoapEntity: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Value(self) -> StringType: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    def set_Value(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapHexBinary(ObjectType, ISoapXsd):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: ArrayType[ByteType]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> ArrayType[ByteType]: ...
    
    @Value.setter
    def Value(self, value: ArrayType[ByteType]) -> None: ...
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    @staticmethod
    def Parse(value: StringType) -> SoapHexBinary: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Value(self) -> ArrayType[ByteType]: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    def set_Value(self, value: ArrayType[ByteType]) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapHexBinary(ObjectType, ISoapXsd):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: ArrayType[ByteType]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> ArrayType[ByteType]: ...
    
    @Value.setter
    def Value(self, value: ArrayType[ByteType]) -> None: ...
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    @staticmethod
    def Parse(value: StringType) -> SoapHexBinary: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Value(self) -> ArrayType[ByteType]: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    def set_Value(self, value: ArrayType[ByteType]) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapHexBinary(ObjectType, ISoapXsd):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: ArrayType[ByteType]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> ArrayType[ByteType]: ...
    
    @Value.setter
    def Value(self, value: ArrayType[ByteType]) -> None: ...
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    @staticmethod
    def Parse(value: StringType) -> SoapHexBinary: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Value(self) -> ArrayType[ByteType]: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    def set_Value(self, value: ArrayType[ByteType]) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapId(ObjectType, ISoapXsd):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> StringType: ...
    
    @Value.setter
    def Value(self, value: StringType) -> None: ...
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    @staticmethod
    def Parse(value: StringType) -> SoapId: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Value(self) -> StringType: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    def set_Value(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapId(ObjectType, ISoapXsd):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> StringType: ...
    
    @Value.setter
    def Value(self, value: StringType) -> None: ...
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    @staticmethod
    def Parse(value: StringType) -> SoapId: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Value(self) -> StringType: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    def set_Value(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapId(ObjectType, ISoapXsd):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> StringType: ...
    
    @Value.setter
    def Value(self, value: StringType) -> None: ...
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    @staticmethod
    def Parse(value: StringType) -> SoapId: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Value(self) -> StringType: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    def set_Value(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapIdref(ObjectType, ISoapXsd):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> StringType: ...
    
    @Value.setter
    def Value(self, value: StringType) -> None: ...
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    @staticmethod
    def Parse(value: StringType) -> SoapIdref: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Value(self) -> StringType: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    def set_Value(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapIdref(ObjectType, ISoapXsd):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> StringType: ...
    
    @Value.setter
    def Value(self, value: StringType) -> None: ...
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    @staticmethod
    def Parse(value: StringType) -> SoapIdref: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Value(self) -> StringType: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    def set_Value(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapIdref(ObjectType, ISoapXsd):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> StringType: ...
    
    @Value.setter
    def Value(self, value: StringType) -> None: ...
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    @staticmethod
    def Parse(value: StringType) -> SoapIdref: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Value(self) -> StringType: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    def set_Value(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapIdrefs(ObjectType, ISoapXsd):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> StringType: ...
    
    @Value.setter
    def Value(self, value: StringType) -> None: ...
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    @staticmethod
    def Parse(value: StringType) -> SoapIdrefs: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Value(self) -> StringType: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    def set_Value(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapIdrefs(ObjectType, ISoapXsd):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> StringType: ...
    
    @Value.setter
    def Value(self, value: StringType) -> None: ...
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    @staticmethod
    def Parse(value: StringType) -> SoapIdrefs: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Value(self) -> StringType: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    def set_Value(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapIdrefs(ObjectType, ISoapXsd):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> StringType: ...
    
    @Value.setter
    def Value(self, value: StringType) -> None: ...
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    @staticmethod
    def Parse(value: StringType) -> SoapIdrefs: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Value(self) -> StringType: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    def set_Value(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapInteger(ObjectType, ISoapXsd):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: DecimalType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> DecimalType: ...
    
    @Value.setter
    def Value(self, value: DecimalType) -> None: ...
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    @staticmethod
    def Parse(value: StringType) -> SoapInteger: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Value(self) -> DecimalType: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    def set_Value(self, value: DecimalType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapInteger(ObjectType, ISoapXsd):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: DecimalType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> DecimalType: ...
    
    @Value.setter
    def Value(self, value: DecimalType) -> None: ...
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    @staticmethod
    def Parse(value: StringType) -> SoapInteger: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Value(self) -> DecimalType: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    def set_Value(self, value: DecimalType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapInteger(ObjectType, ISoapXsd):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: DecimalType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> DecimalType: ...
    
    @Value.setter
    def Value(self, value: DecimalType) -> None: ...
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    @staticmethod
    def Parse(value: StringType) -> SoapInteger: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Value(self) -> DecimalType: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    def set_Value(self, value: DecimalType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapLanguage(ObjectType, ISoapXsd):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> StringType: ...
    
    @Value.setter
    def Value(self, value: StringType) -> None: ...
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    @staticmethod
    def Parse(value: StringType) -> SoapLanguage: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Value(self) -> StringType: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    def set_Value(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapLanguage(ObjectType, ISoapXsd):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> StringType: ...
    
    @Value.setter
    def Value(self, value: StringType) -> None: ...
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    @staticmethod
    def Parse(value: StringType) -> SoapLanguage: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Value(self) -> StringType: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    def set_Value(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapLanguage(ObjectType, ISoapXsd):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> StringType: ...
    
    @Value.setter
    def Value(self, value: StringType) -> None: ...
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    @staticmethod
    def Parse(value: StringType) -> SoapLanguage: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Value(self) -> StringType: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    def set_Value(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapMonth(ObjectType, ISoapXsd):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: DateTime): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> DateTime: ...
    
    @Value.setter
    def Value(self, value: DateTime) -> None: ...
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    @staticmethod
    def Parse(value: StringType) -> SoapMonth: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Value(self) -> DateTime: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    def set_Value(self, value: DateTime) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapMonth(ObjectType, ISoapXsd):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: DateTime): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> DateTime: ...
    
    @Value.setter
    def Value(self, value: DateTime) -> None: ...
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    @staticmethod
    def Parse(value: StringType) -> SoapMonth: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Value(self) -> DateTime: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    def set_Value(self, value: DateTime) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapMonth(ObjectType, ISoapXsd):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: DateTime): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> DateTime: ...
    
    @Value.setter
    def Value(self, value: DateTime) -> None: ...
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    @staticmethod
    def Parse(value: StringType) -> SoapMonth: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Value(self) -> DateTime: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    def set_Value(self, value: DateTime) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapMonthDay(ObjectType, ISoapXsd):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: DateTime): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> DateTime: ...
    
    @Value.setter
    def Value(self, value: DateTime) -> None: ...
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    @staticmethod
    def Parse(value: StringType) -> SoapMonthDay: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Value(self) -> DateTime: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    def set_Value(self, value: DateTime) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapMonthDay(ObjectType, ISoapXsd):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: DateTime): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> DateTime: ...
    
    @Value.setter
    def Value(self, value: DateTime) -> None: ...
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    @staticmethod
    def Parse(value: StringType) -> SoapMonthDay: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Value(self) -> DateTime: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    def set_Value(self, value: DateTime) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapMonthDay(ObjectType, ISoapXsd):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: DateTime): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> DateTime: ...
    
    @Value.setter
    def Value(self, value: DateTime) -> None: ...
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    @staticmethod
    def Parse(value: StringType) -> SoapMonthDay: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Value(self) -> DateTime: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    def set_Value(self, value: DateTime) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapName(ObjectType, ISoapXsd):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> StringType: ...
    
    @Value.setter
    def Value(self, value: StringType) -> None: ...
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    @staticmethod
    def Parse(value: StringType) -> SoapName: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Value(self) -> StringType: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    def set_Value(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapName(ObjectType, ISoapXsd):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> StringType: ...
    
    @Value.setter
    def Value(self, value: StringType) -> None: ...
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    @staticmethod
    def Parse(value: StringType) -> SoapName: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Value(self) -> StringType: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    def set_Value(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapName(ObjectType, ISoapXsd):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> StringType: ...
    
    @Value.setter
    def Value(self, value: StringType) -> None: ...
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    @staticmethod
    def Parse(value: StringType) -> SoapName: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Value(self) -> StringType: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    def set_Value(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapNcName(ObjectType, ISoapXsd):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> StringType: ...
    
    @Value.setter
    def Value(self, value: StringType) -> None: ...
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    @staticmethod
    def Parse(value: StringType) -> SoapNcName: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Value(self) -> StringType: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    def set_Value(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapNcName(ObjectType, ISoapXsd):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> StringType: ...
    
    @Value.setter
    def Value(self, value: StringType) -> None: ...
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    @staticmethod
    def Parse(value: StringType) -> SoapNcName: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Value(self) -> StringType: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    def set_Value(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapNcName(ObjectType, ISoapXsd):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> StringType: ...
    
    @Value.setter
    def Value(self, value: StringType) -> None: ...
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    @staticmethod
    def Parse(value: StringType) -> SoapNcName: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Value(self) -> StringType: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    def set_Value(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapNegativeInteger(ObjectType, ISoapXsd):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: DecimalType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> DecimalType: ...
    
    @Value.setter
    def Value(self, value: DecimalType) -> None: ...
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    @staticmethod
    def Parse(value: StringType) -> SoapNegativeInteger: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Value(self) -> DecimalType: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    def set_Value(self, value: DecimalType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapNegativeInteger(ObjectType, ISoapXsd):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: DecimalType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> DecimalType: ...
    
    @Value.setter
    def Value(self, value: DecimalType) -> None: ...
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    @staticmethod
    def Parse(value: StringType) -> SoapNegativeInteger: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Value(self) -> DecimalType: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    def set_Value(self, value: DecimalType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapNegativeInteger(ObjectType, ISoapXsd):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: DecimalType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> DecimalType: ...
    
    @Value.setter
    def Value(self, value: DecimalType) -> None: ...
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    @staticmethod
    def Parse(value: StringType) -> SoapNegativeInteger: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Value(self) -> DecimalType: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    def set_Value(self, value: DecimalType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapNmtoken(ObjectType, ISoapXsd):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> StringType: ...
    
    @Value.setter
    def Value(self, value: StringType) -> None: ...
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    @staticmethod
    def Parse(value: StringType) -> SoapNmtoken: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Value(self) -> StringType: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    def set_Value(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapNmtoken(ObjectType, ISoapXsd):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> StringType: ...
    
    @Value.setter
    def Value(self, value: StringType) -> None: ...
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    @staticmethod
    def Parse(value: StringType) -> SoapNmtoken: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Value(self) -> StringType: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    def set_Value(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapNmtoken(ObjectType, ISoapXsd):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> StringType: ...
    
    @Value.setter
    def Value(self, value: StringType) -> None: ...
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    @staticmethod
    def Parse(value: StringType) -> SoapNmtoken: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Value(self) -> StringType: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    def set_Value(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapNmtokens(ObjectType, ISoapXsd):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> StringType: ...
    
    @Value.setter
    def Value(self, value: StringType) -> None: ...
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    @staticmethod
    def Parse(value: StringType) -> SoapNmtokens: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Value(self) -> StringType: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    def set_Value(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapNmtokens(ObjectType, ISoapXsd):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> StringType: ...
    
    @Value.setter
    def Value(self, value: StringType) -> None: ...
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    @staticmethod
    def Parse(value: StringType) -> SoapNmtokens: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Value(self) -> StringType: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    def set_Value(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapNmtokens(ObjectType, ISoapXsd):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> StringType: ...
    
    @Value.setter
    def Value(self, value: StringType) -> None: ...
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    @staticmethod
    def Parse(value: StringType) -> SoapNmtokens: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Value(self) -> StringType: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    def set_Value(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapNonNegativeInteger(ObjectType, ISoapXsd):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: DecimalType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> DecimalType: ...
    
    @Value.setter
    def Value(self, value: DecimalType) -> None: ...
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    @staticmethod
    def Parse(value: StringType) -> SoapNonNegativeInteger: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Value(self) -> DecimalType: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    def set_Value(self, value: DecimalType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapNonNegativeInteger(ObjectType, ISoapXsd):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: DecimalType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> DecimalType: ...
    
    @Value.setter
    def Value(self, value: DecimalType) -> None: ...
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    @staticmethod
    def Parse(value: StringType) -> SoapNonNegativeInteger: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Value(self) -> DecimalType: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    def set_Value(self, value: DecimalType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapNonNegativeInteger(ObjectType, ISoapXsd):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: DecimalType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> DecimalType: ...
    
    @Value.setter
    def Value(self, value: DecimalType) -> None: ...
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    @staticmethod
    def Parse(value: StringType) -> SoapNonNegativeInteger: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Value(self) -> DecimalType: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    def set_Value(self, value: DecimalType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapNonPositiveInteger(ObjectType, ISoapXsd):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: DecimalType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> DecimalType: ...
    
    @Value.setter
    def Value(self, value: DecimalType) -> None: ...
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    @staticmethod
    def Parse(value: StringType) -> SoapNonPositiveInteger: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Value(self) -> DecimalType: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    def set_Value(self, value: DecimalType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapNonPositiveInteger(ObjectType, ISoapXsd):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: DecimalType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> DecimalType: ...
    
    @Value.setter
    def Value(self, value: DecimalType) -> None: ...
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    @staticmethod
    def Parse(value: StringType) -> SoapNonPositiveInteger: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Value(self) -> DecimalType: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    def set_Value(self, value: DecimalType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapNonPositiveInteger(ObjectType, ISoapXsd):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: DecimalType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> DecimalType: ...
    
    @Value.setter
    def Value(self, value: DecimalType) -> None: ...
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    @staticmethod
    def Parse(value: StringType) -> SoapNonPositiveInteger: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Value(self) -> DecimalType: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    def set_Value(self, value: DecimalType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapNormalizedString(ObjectType, ISoapXsd):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> StringType: ...
    
    @Value.setter
    def Value(self, value: StringType) -> None: ...
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    @staticmethod
    def Parse(value: StringType) -> SoapNormalizedString: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Value(self) -> StringType: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    def set_Value(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapNormalizedString(ObjectType, ISoapXsd):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> StringType: ...
    
    @Value.setter
    def Value(self, value: StringType) -> None: ...
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    @staticmethod
    def Parse(value: StringType) -> SoapNormalizedString: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Value(self) -> StringType: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    def set_Value(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapNormalizedString(ObjectType, ISoapXsd):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> StringType: ...
    
    @Value.setter
    def Value(self, value: StringType) -> None: ...
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    @staticmethod
    def Parse(value: StringType) -> SoapNormalizedString: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Value(self) -> StringType: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    def set_Value(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapNotation(ObjectType, ISoapXsd):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> StringType: ...
    
    @Value.setter
    def Value(self, value: StringType) -> None: ...
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    @staticmethod
    def Parse(value: StringType) -> SoapNotation: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Value(self) -> StringType: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    def set_Value(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapNotation(ObjectType, ISoapXsd):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> StringType: ...
    
    @Value.setter
    def Value(self, value: StringType) -> None: ...
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    @staticmethod
    def Parse(value: StringType) -> SoapNotation: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Value(self) -> StringType: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    def set_Value(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapNotation(ObjectType, ISoapXsd):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> StringType: ...
    
    @Value.setter
    def Value(self, value: StringType) -> None: ...
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    @staticmethod
    def Parse(value: StringType) -> SoapNotation: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Value(self) -> StringType: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    def set_Value(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapPositiveInteger(ObjectType, ISoapXsd):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: DecimalType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> DecimalType: ...
    
    @Value.setter
    def Value(self, value: DecimalType) -> None: ...
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    @staticmethod
    def Parse(value: StringType) -> SoapPositiveInteger: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Value(self) -> DecimalType: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    def set_Value(self, value: DecimalType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapPositiveInteger(ObjectType, ISoapXsd):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: DecimalType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> DecimalType: ...
    
    @Value.setter
    def Value(self, value: DecimalType) -> None: ...
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    @staticmethod
    def Parse(value: StringType) -> SoapPositiveInteger: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Value(self) -> DecimalType: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    def set_Value(self, value: DecimalType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapPositiveInteger(ObjectType, ISoapXsd):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: DecimalType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> DecimalType: ...
    
    @Value.setter
    def Value(self, value: DecimalType) -> None: ...
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    @staticmethod
    def Parse(value: StringType) -> SoapPositiveInteger: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Value(self) -> DecimalType: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    def set_Value(self, value: DecimalType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapQName(ObjectType, ISoapXsd):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: StringType): ...
    
    @overload
    def __init__(self, key: StringType, name: StringType): ...
    
    @overload
    def __init__(self, key: StringType, name: StringType, namespaceValue: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Key(self) -> StringType: ...
    
    @Key.setter
    def Key(self, value: StringType) -> None: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @Name.setter
    def Name(self, value: StringType) -> None: ...
    
    @property
    def Namespace(self) -> StringType: ...
    
    @Namespace.setter
    def Namespace(self, value: StringType) -> None: ...
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    @staticmethod
    def Parse(value: StringType) -> SoapQName: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Key(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_Namespace(self) -> StringType: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    def set_Key(self, value: StringType) -> VoidType: ...
    
    def set_Name(self, value: StringType) -> VoidType: ...
    
    def set_Namespace(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapQName(ObjectType, ISoapXsd):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: StringType): ...
    
    @overload
    def __init__(self, key: StringType, name: StringType): ...
    
    @overload
    def __init__(self, key: StringType, name: StringType, namespaceValue: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Key(self) -> StringType: ...
    
    @Key.setter
    def Key(self, value: StringType) -> None: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @Name.setter
    def Name(self, value: StringType) -> None: ...
    
    @property
    def Namespace(self) -> StringType: ...
    
    @Namespace.setter
    def Namespace(self, value: StringType) -> None: ...
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    @staticmethod
    def Parse(value: StringType) -> SoapQName: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Key(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_Namespace(self) -> StringType: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    def set_Key(self, value: StringType) -> VoidType: ...
    
    def set_Name(self, value: StringType) -> VoidType: ...
    
    def set_Namespace(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapQName(ObjectType, ISoapXsd):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: StringType): ...
    
    @overload
    def __init__(self, key: StringType, name: StringType): ...
    
    @overload
    def __init__(self, key: StringType, name: StringType, namespaceValue: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Key(self) -> StringType: ...
    
    @Key.setter
    def Key(self, value: StringType) -> None: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @Name.setter
    def Name(self, value: StringType) -> None: ...
    
    @property
    def Namespace(self) -> StringType: ...
    
    @Namespace.setter
    def Namespace(self, value: StringType) -> None: ...
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    @staticmethod
    def Parse(value: StringType) -> SoapQName: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Key(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_Namespace(self) -> StringType: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    def set_Key(self, value: StringType) -> VoidType: ...
    
    def set_Name(self, value: StringType) -> VoidType: ...
    
    def set_Namespace(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapTime(ObjectType, ISoapXsd):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: DateTime): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> DateTime: ...
    
    @Value.setter
    def Value(self, value: DateTime) -> None: ...
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    @staticmethod
    def Parse(value: StringType) -> SoapTime: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Value(self) -> DateTime: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    def set_Value(self, value: DateTime) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapTime(ObjectType, ISoapXsd):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: DateTime): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> DateTime: ...
    
    @Value.setter
    def Value(self, value: DateTime) -> None: ...
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    @staticmethod
    def Parse(value: StringType) -> SoapTime: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Value(self) -> DateTime: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    def set_Value(self, value: DateTime) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapTime(ObjectType, ISoapXsd):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: DateTime): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> DateTime: ...
    
    @Value.setter
    def Value(self, value: DateTime) -> None: ...
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    @staticmethod
    def Parse(value: StringType) -> SoapTime: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Value(self) -> DateTime: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    def set_Value(self, value: DateTime) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapToken(ObjectType, ISoapXsd):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> StringType: ...
    
    @Value.setter
    def Value(self, value: StringType) -> None: ...
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    @staticmethod
    def Parse(value: StringType) -> SoapToken: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Value(self) -> StringType: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    def set_Value(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapToken(ObjectType, ISoapXsd):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> StringType: ...
    
    @Value.setter
    def Value(self, value: StringType) -> None: ...
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    @staticmethod
    def Parse(value: StringType) -> SoapToken: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Value(self) -> StringType: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    def set_Value(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapToken(ObjectType, ISoapXsd):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> StringType: ...
    
    @Value.setter
    def Value(self, value: StringType) -> None: ...
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    @staticmethod
    def Parse(value: StringType) -> SoapToken: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Value(self) -> StringType: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    def set_Value(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapType(ABC, ObjectType):
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


class SoapType(ABC, ObjectType):
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


class SoapType(ABC, ObjectType):
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


class SoapYear(ObjectType, ISoapXsd):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: DateTime): ...
    
    @overload
    def __init__(self, value: DateTime, sign: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Sign(self) -> IntType: ...
    
    @Sign.setter
    def Sign(self, value: IntType) -> None: ...
    
    @property
    def Value(self) -> DateTime: ...
    
    @Value.setter
    def Value(self, value: DateTime) -> None: ...
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    @staticmethod
    def Parse(value: StringType) -> SoapYear: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Sign(self) -> IntType: ...
    
    def get_Value(self) -> DateTime: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    def set_Sign(self, value: IntType) -> VoidType: ...
    
    def set_Value(self, value: DateTime) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapYear(ObjectType, ISoapXsd):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: DateTime): ...
    
    @overload
    def __init__(self, value: DateTime, sign: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Sign(self) -> IntType: ...
    
    @Sign.setter
    def Sign(self, value: IntType) -> None: ...
    
    @property
    def Value(self) -> DateTime: ...
    
    @Value.setter
    def Value(self, value: DateTime) -> None: ...
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    @staticmethod
    def Parse(value: StringType) -> SoapYear: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Sign(self) -> IntType: ...
    
    def get_Value(self) -> DateTime: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    def set_Sign(self, value: IntType) -> VoidType: ...
    
    def set_Value(self, value: DateTime) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapYear(ObjectType, ISoapXsd):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: DateTime): ...
    
    @overload
    def __init__(self, value: DateTime, sign: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Sign(self) -> IntType: ...
    
    @Sign.setter
    def Sign(self, value: IntType) -> None: ...
    
    @property
    def Value(self) -> DateTime: ...
    
    @Value.setter
    def Value(self, value: DateTime) -> None: ...
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    @staticmethod
    def Parse(value: StringType) -> SoapYear: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Sign(self) -> IntType: ...
    
    def get_Value(self) -> DateTime: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    def set_Sign(self, value: IntType) -> VoidType: ...
    
    def set_Value(self, value: DateTime) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapYearMonth(ObjectType, ISoapXsd):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: DateTime): ...
    
    @overload
    def __init__(self, value: DateTime, sign: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Sign(self) -> IntType: ...
    
    @Sign.setter
    def Sign(self, value: IntType) -> None: ...
    
    @property
    def Value(self) -> DateTime: ...
    
    @Value.setter
    def Value(self, value: DateTime) -> None: ...
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    @staticmethod
    def Parse(value: StringType) -> SoapYearMonth: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Sign(self) -> IntType: ...
    
    def get_Value(self) -> DateTime: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    def set_Sign(self, value: IntType) -> VoidType: ...
    
    def set_Value(self, value: DateTime) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapYearMonth(ObjectType, ISoapXsd):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: DateTime): ...
    
    @overload
    def __init__(self, value: DateTime, sign: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Sign(self) -> IntType: ...
    
    @Sign.setter
    def Sign(self, value: IntType) -> None: ...
    
    @property
    def Value(self) -> DateTime: ...
    
    @Value.setter
    def Value(self, value: DateTime) -> None: ...
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    @staticmethod
    def Parse(value: StringType) -> SoapYearMonth: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Sign(self) -> IntType: ...
    
    def get_Value(self) -> DateTime: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    def set_Sign(self, value: IntType) -> VoidType: ...
    
    def set_Value(self, value: DateTime) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapYearMonth(ObjectType, ISoapXsd):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: DateTime): ...
    
    @overload
    def __init__(self, value: DateTime, sign: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Sign(self) -> IntType: ...
    
    @Sign.setter
    def Sign(self, value: IntType) -> None: ...
    
    @property
    def Value(self) -> DateTime: ...
    
    @Value.setter
    def Value(self, value: DateTime) -> None: ...
    
    @staticmethod
    @property
    def XsdType() -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    @staticmethod
    def Parse(value: StringType) -> SoapYearMonth: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Sign(self) -> IntType: ...
    
    def get_Value(self) -> DateTime: ...
    
    @staticmethod
    def get_XsdType() -> StringType: ...
    
    def set_Sign(self, value: IntType) -> VoidType: ...
    
    def set_Value(self, value: DateTime) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# No Structs

# ---------- Interfaces ---------- #

class ISoapXsd(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    # No Events


class ISoapXsd(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    # No Events


class ISoapXsd(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetXsdType(self) -> StringType: ...
    
    # No Events


# No Enums

# No Delegates

__all__ = [
    SoapAnyUri,
    SoapBase64Binary,
    SoapDate,
    SoapDateTime,
    SoapDay,
    SoapDuration,
    SoapEntities,
    SoapEntity,
    SoapHexBinary,
    SoapId,
    SoapIdref,
    SoapIdrefs,
    SoapInteger,
    SoapLanguage,
    SoapMonth,
    SoapMonthDay,
    SoapName,
    SoapNcName,
    SoapNegativeInteger,
    SoapNmtoken,
    SoapNmtokens,
    SoapNonNegativeInteger,
    SoapNonPositiveInteger,
    SoapNormalizedString,
    SoapNotation,
    SoapPositiveInteger,
    SoapQName,
    SoapTime,
    SoapToken,
    SoapType,
    SoapYear,
    SoapYearMonth,
    ISoapXsd,
]
