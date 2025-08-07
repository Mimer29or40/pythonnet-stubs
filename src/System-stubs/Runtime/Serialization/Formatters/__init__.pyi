"""Automatically generated stubs for C# namespace: System.Runtime.Serialization.Formatters."""

from abc import ABC
from typing import overload

from System import Array
from System import Enum
from System import Object
from System import Type
from System.Reflection import Assembly
from System.Reflection import FieldInfo
from System.Runtime.Remoting.Messaging import Header
from System.Runtime.Serialization import ISerializable
from System.Runtime.Serialization import SerializationInfo
from System.Runtime.Serialization import StreamingContext

class FormatterAssemblyStyle(Enum):
    """"""

    Simple: FormatterAssemblyStyle = ...
    """"""
    Full: FormatterAssemblyStyle = ...
    """"""

class FormatterTypeStyle(Enum):
    """"""

    TypesWhenNeeded: FormatterTypeStyle = ...
    """"""
    TypesAlways: FormatterTypeStyle = ...
    """"""
    XsdString: FormatterTypeStyle = ...
    """"""

class IFieldInfo:
    """"""
    @property
    def FieldNames(self) -> Array[str]:
        """"""
    @FieldNames.setter
    def FieldNames(self, value: Array[str]) -> None: ...
    @property
    def FieldTypes(self) -> Array[Type]:
        """"""
    @FieldTypes.setter
    def FieldTypes(self, value: Array[Type]) -> None: ...

class ISoapMessage:
    """"""
    @property
    def Headers(self) -> Array[Header]:
        """"""
    @Headers.setter
    def Headers(self, value: Array[Header]) -> None: ...
    @property
    def MethodName(self) -> str:
        """"""
    @MethodName.setter
    def MethodName(self, value: str) -> None: ...
    @property
    def ParamNames(self) -> Array[str]:
        """"""
    @ParamNames.setter
    def ParamNames(self, value: Array[str]) -> None: ...
    @property
    def ParamTypes(self) -> Array[Type]:
        """"""
    @ParamTypes.setter
    def ParamTypes(self, value: Array[Type]) -> None: ...
    @property
    def ParamValues(self) -> Array[object]:
        """"""
    @ParamValues.setter
    def ParamValues(self, value: Array[object]) -> None: ...
    @property
    def XmlNameSpace(self) -> str:
        """"""
    @XmlNameSpace.setter
    def XmlNameSpace(self, value: str) -> None: ...

class InternalRM(Object):
    """"""
    def __init__(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def InfoSoap(cls, messages: Array[object]) -> None:
        """"""
    @classmethod
    def SoapCheckEnabled(cls) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

class InternalST(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def InfoSoap(cls, messages: Array[object]) -> None:
        """"""
    @classmethod
    def LoadAssemblyFromString(cls, assemblyString: str) -> Assembly:
        """"""
    @classmethod
    def SerializationSetValue(cls, fi: FieldInfo, target: object, value: object) -> None:
        """"""
    @classmethod
    def Soap(cls, messages: Array[object]) -> None:
        """"""
    @classmethod
    def SoapAssert(cls, condition: bool, message: str) -> None:
        """"""
    @classmethod
    def SoapCheckEnabled(cls) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

class SerTrace(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ServerFault(Object):
    """"""
    def __init__(self, exceptionType: str, message: str, stackTrace: str) -> None:
        """"""
    @property
    def ExceptionMessage(self) -> str:
        """"""
    @ExceptionMessage.setter
    def ExceptionMessage(self, value: str) -> None: ...
    @property
    def ExceptionType(self) -> str:
        """"""
    @ExceptionType.setter
    def ExceptionType(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """"""
    @StackTrace.setter
    def StackTrace(self, value: str) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SoapFault(Object, ISerializable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(
        self, faultCode: str, faultString: str, faultActor: str, serverFault: ServerFault
    ) -> None:
        """"""
    @property
    def Detail(self) -> object:
        """"""
    @Detail.setter
    def Detail(self, value: object) -> None: ...
    @property
    def FaultActor(self) -> str:
        """"""
    @FaultActor.setter
    def FaultActor(self, value: str) -> None: ...
    @property
    def FaultCode(self) -> str:
        """"""
    @FaultCode.setter
    def FaultCode(self, value: str) -> None: ...
    @property
    def FaultString(self) -> str:
        """"""
    @FaultString.setter
    def FaultString(self, value: str) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SoapMessage(Object, ISoapMessage):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Headers(self) -> Array[Header]:
        """"""
    @Headers.setter
    def Headers(self, value: Array[Header]) -> None: ...
    @property
    def MethodName(self) -> str:
        """"""
    @MethodName.setter
    def MethodName(self, value: str) -> None: ...
    @property
    def ParamNames(self) -> Array[str]:
        """"""
    @ParamNames.setter
    def ParamNames(self, value: Array[str]) -> None: ...
    @property
    def ParamTypes(self) -> Array[Type]:
        """"""
    @ParamTypes.setter
    def ParamTypes(self, value: Array[Type]) -> None: ...
    @property
    def ParamValues(self) -> Array[object]:
        """"""
    @ParamValues.setter
    def ParamValues(self, value: Array[object]) -> None: ...
    @property
    def XmlNameSpace(self) -> str:
        """"""
    @XmlNameSpace.setter
    def XmlNameSpace(self, value: str) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class TypeFilterLevel(Enum):
    """"""

    Low: TypeFilterLevel = ...
    """"""
    Full: TypeFilterLevel = ...
    """"""
