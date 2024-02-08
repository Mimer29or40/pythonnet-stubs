from __future__ import annotations

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
        """

        :return:
        """
    @FieldNames.setter
    def FieldNames(self, value: Array[str]) -> None: ...
    @property
    def FieldTypes(self) -> Array[Type]:
        """

        :return:
        """
    @FieldTypes.setter
    def FieldTypes(self, value: Array[Type]) -> None: ...

class ISoapMessage:
    """"""

    @property
    def Headers(self) -> Array[Header]:
        """

        :return:
        """
    @Headers.setter
    def Headers(self, value: Array[Header]) -> None: ...
    @property
    def MethodName(self) -> str:
        """

        :return:
        """
    @MethodName.setter
    def MethodName(self, value: str) -> None: ...
    @property
    def ParamNames(self) -> Array[str]:
        """

        :return:
        """
    @ParamNames.setter
    def ParamNames(self, value: Array[str]) -> None: ...
    @property
    def ParamTypes(self) -> Array[Type]:
        """

        :return:
        """
    @ParamTypes.setter
    def ParamTypes(self, value: Array[Type]) -> None: ...
    @property
    def ParamValues(self) -> Array[object]:
        """

        :return:
        """
    @ParamValues.setter
    def ParamValues(self, value: Array[object]) -> None: ...
    @property
    def XmlNameSpace(self) -> str:
        """

        :return:
        """
    @XmlNameSpace.setter
    def XmlNameSpace(self, value: str) -> None: ...

class InternalRM(Object):
    """"""

    def __init__(self):
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
    @classmethod
    def InfoSoap(cls, messages: Array[object]) -> None:
        """

        :param messages:
        """
    @classmethod
    def SoapCheckEnabled(cls) -> bool:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class InternalST(Object):
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
    @classmethod
    def InfoSoap(cls, messages: Array[object]) -> None:
        """

        :param messages:
        """
    @classmethod
    def LoadAssemblyFromString(cls, assemblyString: str) -> Assembly:
        """

        :param assemblyString:
        :return:
        """
    @classmethod
    def SerializationSetValue(cls, fi: FieldInfo, target: object, value: object) -> None:
        """

        :param fi:
        :param target:
        :param value:
        """
    @classmethod
    def Soap(cls, messages: Array[object]) -> None:
        """

        :param messages:
        """
    @classmethod
    def SoapAssert(cls, condition: bool, message: str) -> None:
        """

        :param condition:
        :param message:
        """
    @classmethod
    def SoapCheckEnabled(cls) -> bool:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class SerTrace(ABC, Object):
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

class ServerFault(Object):
    """"""

    def __init__(self, exceptionType: str, message: str, stackTrace: str):
        """

        :param exceptionType:
        :param message:
        :param stackTrace:
        """
    @property
    def ExceptionMessage(self) -> str:
        """

        :return:
        """
    @ExceptionMessage.setter
    def ExceptionMessage(self, value: str) -> None: ...
    @property
    def ExceptionType(self) -> str:
        """

        :return:
        """
    @ExceptionType.setter
    def ExceptionType(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """

        :return:
        """
    @StackTrace.setter
    def StackTrace(self, value: str) -> None: ...
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

class SoapFault(Object, ISerializable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, faultCode: str, faultString: str, faultActor: str, serverFault: ServerFault):
        """

        :param faultCode:
        :param faultString:
        :param faultActor:
        :param serverFault:
        """
    @property
    def Detail(self) -> object:
        """

        :return:
        """
    @Detail.setter
    def Detail(self, value: object) -> None: ...
    @property
    def FaultActor(self) -> str:
        """

        :return:
        """
    @FaultActor.setter
    def FaultActor(self, value: str) -> None: ...
    @property
    def FaultCode(self) -> str:
        """

        :return:
        """
    @FaultCode.setter
    def FaultCode(self, value: str) -> None: ...
    @property
    def FaultString(self) -> str:
        """

        :return:
        """
    @FaultString.setter
    def FaultString(self, value: str) -> None: ...
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class SoapMessage(Object, ISoapMessage):
    """"""

    def __init__(self):
        """"""
    @property
    def Headers(self) -> Array[Header]:
        """

        :return:
        """
    @Headers.setter
    def Headers(self, value: Array[Header]) -> None: ...
    @property
    def MethodName(self) -> str:
        """

        :return:
        """
    @MethodName.setter
    def MethodName(self, value: str) -> None: ...
    @property
    def ParamNames(self) -> Array[str]:
        """

        :return:
        """
    @ParamNames.setter
    def ParamNames(self, value: Array[str]) -> None: ...
    @property
    def ParamTypes(self) -> Array[Type]:
        """

        :return:
        """
    @ParamTypes.setter
    def ParamTypes(self, value: Array[Type]) -> None: ...
    @property
    def ParamValues(self) -> Array[object]:
        """

        :return:
        """
    @ParamValues.setter
    def ParamValues(self, value: Array[object]) -> None: ...
    @property
    def XmlNameSpace(self) -> str:
        """

        :return:
        """
    @XmlNameSpace.setter
    def XmlNameSpace(self, value: str) -> None: ...
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

class TypeFilterLevel(Enum):
    """"""

    Low: TypeFilterLevel = ...
    """"""
    Full: TypeFilterLevel = ...
    """"""
