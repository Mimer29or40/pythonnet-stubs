from __future__ import annotations

from abc import ABC
from typing import overload

from System import Array
from System import DateTime
from System import Decimal
from System import Object
from System import TimeSpan
from System import Type

class ISoapXsd:
    """"""

    def GetXsdType(self) -> str:
        """

        :return:
        """

class SoapAnyUri(Object, ISoapXsd):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, value: str):
        """

        :param value:
        """
    @property
    def Value(self) -> str:
        """

        :return:
        """
    @Value.setter
    def Value(self, value: str) -> None: ...
    @classmethod
    @property
    def XsdType(cls) -> str:
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
    def GetXsdType(self) -> str:
        """

        :return:
        """
    @classmethod
    def Parse(cls, value: str) -> SoapAnyUri:
        """

        :param value:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class SoapBase64Binary(Object, ISoapXsd):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, value: Array[int]):
        """

        :param value:
        """
    @property
    def Value(self) -> Array[int]:
        """

        :return:
        """
    @Value.setter
    def Value(self, value: Array[int]) -> None: ...
    @classmethod
    @property
    def XsdType(cls) -> str:
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
    def GetXsdType(self) -> str:
        """

        :return:
        """
    @classmethod
    def Parse(cls, value: str) -> SoapBase64Binary:
        """

        :param value:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class SoapDate(Object, ISoapXsd):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, value: DateTime):
        """

        :param value:
        """
    @overload
    def __init__(self, value: DateTime, sign: int):
        """

        :param value:
        :param sign:
        """
    @property
    def Sign(self) -> int:
        """

        :return:
        """
    @Sign.setter
    def Sign(self, value: int) -> None: ...
    @property
    def Value(self) -> DateTime:
        """

        :return:
        """
    @Value.setter
    def Value(self, value: DateTime) -> None: ...
    @classmethod
    @property
    def XsdType(cls) -> str:
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
    def GetXsdType(self) -> str:
        """

        :return:
        """
    @classmethod
    def Parse(cls, value: str) -> SoapDate:
        """

        :param value:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class SoapDateTime(Object):
    """"""

    def __init__(self):
        """"""
    @classmethod
    @property
    def XsdType(cls) -> str:
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
    @classmethod
    def Parse(cls, value: str) -> DateTime:
        """

        :param value:
        :return:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """
    @classmethod
    @overload
    def ToString(cls, value: DateTime) -> str:
        """

        :param value:
        :return:
        """

class SoapDay(Object, ISoapXsd):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, value: DateTime):
        """

        :param value:
        """
    @property
    def Value(self) -> DateTime:
        """

        :return:
        """
    @Value.setter
    def Value(self, value: DateTime) -> None: ...
    @classmethod
    @property
    def XsdType(cls) -> str:
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
    def GetXsdType(self) -> str:
        """

        :return:
        """
    @classmethod
    def Parse(cls, value: str) -> SoapDay:
        """

        :param value:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class SoapDuration(Object):
    """"""

    def __init__(self):
        """"""
    @classmethod
    @property
    def XsdType(cls) -> str:
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
    @classmethod
    def Parse(cls, value: str) -> TimeSpan:
        """

        :param value:
        :return:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """
    @classmethod
    @overload
    def ToString(cls, timeSpan: TimeSpan) -> str:
        """

        :param timeSpan:
        :return:
        """

class SoapEntities(Object, ISoapXsd):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, value: str):
        """

        :param value:
        """
    @property
    def Value(self) -> str:
        """

        :return:
        """
    @Value.setter
    def Value(self, value: str) -> None: ...
    @classmethod
    @property
    def XsdType(cls) -> str:
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
    def GetXsdType(self) -> str:
        """

        :return:
        """
    @classmethod
    def Parse(cls, value: str) -> SoapEntities:
        """

        :param value:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class SoapEntity(Object, ISoapXsd):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, value: str):
        """

        :param value:
        """
    @property
    def Value(self) -> str:
        """

        :return:
        """
    @Value.setter
    def Value(self, value: str) -> None: ...
    @classmethod
    @property
    def XsdType(cls) -> str:
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
    def GetXsdType(self) -> str:
        """

        :return:
        """
    @classmethod
    def Parse(cls, value: str) -> SoapEntity:
        """

        :param value:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class SoapHexBinary(Object, ISoapXsd):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, value: Array[int]):
        """

        :param value:
        """
    @property
    def Value(self) -> Array[int]:
        """

        :return:
        """
    @Value.setter
    def Value(self, value: Array[int]) -> None: ...
    @classmethod
    @property
    def XsdType(cls) -> str:
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
    def GetXsdType(self) -> str:
        """

        :return:
        """
    @classmethod
    def Parse(cls, value: str) -> SoapHexBinary:
        """

        :param value:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class SoapId(Object, ISoapXsd):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, value: str):
        """

        :param value:
        """
    @property
    def Value(self) -> str:
        """

        :return:
        """
    @Value.setter
    def Value(self, value: str) -> None: ...
    @classmethod
    @property
    def XsdType(cls) -> str:
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
    def GetXsdType(self) -> str:
        """

        :return:
        """
    @classmethod
    def Parse(cls, value: str) -> SoapId:
        """

        :param value:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class SoapIdref(Object, ISoapXsd):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, value: str):
        """

        :param value:
        """
    @property
    def Value(self) -> str:
        """

        :return:
        """
    @Value.setter
    def Value(self, value: str) -> None: ...
    @classmethod
    @property
    def XsdType(cls) -> str:
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
    def GetXsdType(self) -> str:
        """

        :return:
        """
    @classmethod
    def Parse(cls, value: str) -> SoapIdref:
        """

        :param value:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class SoapIdrefs(Object, ISoapXsd):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, value: str):
        """

        :param value:
        """
    @property
    def Value(self) -> str:
        """

        :return:
        """
    @Value.setter
    def Value(self, value: str) -> None: ...
    @classmethod
    @property
    def XsdType(cls) -> str:
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
    def GetXsdType(self) -> str:
        """

        :return:
        """
    @classmethod
    def Parse(cls, value: str) -> SoapIdrefs:
        """

        :param value:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class SoapInteger(Object, ISoapXsd):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, value: Decimal):
        """

        :param value:
        """
    @property
    def Value(self) -> Decimal:
        """

        :return:
        """
    @Value.setter
    def Value(self, value: Decimal) -> None: ...
    @classmethod
    @property
    def XsdType(cls) -> str:
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
    def GetXsdType(self) -> str:
        """

        :return:
        """
    @classmethod
    def Parse(cls, value: str) -> SoapInteger:
        """

        :param value:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class SoapLanguage(Object, ISoapXsd):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, value: str):
        """

        :param value:
        """
    @property
    def Value(self) -> str:
        """

        :return:
        """
    @Value.setter
    def Value(self, value: str) -> None: ...
    @classmethod
    @property
    def XsdType(cls) -> str:
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
    def GetXsdType(self) -> str:
        """

        :return:
        """
    @classmethod
    def Parse(cls, value: str) -> SoapLanguage:
        """

        :param value:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class SoapMonth(Object, ISoapXsd):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, value: DateTime):
        """

        :param value:
        """
    @property
    def Value(self) -> DateTime:
        """

        :return:
        """
    @Value.setter
    def Value(self, value: DateTime) -> None: ...
    @classmethod
    @property
    def XsdType(cls) -> str:
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
    def GetXsdType(self) -> str:
        """

        :return:
        """
    @classmethod
    def Parse(cls, value: str) -> SoapMonth:
        """

        :param value:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class SoapMonthDay(Object, ISoapXsd):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, value: DateTime):
        """

        :param value:
        """
    @property
    def Value(self) -> DateTime:
        """

        :return:
        """
    @Value.setter
    def Value(self, value: DateTime) -> None: ...
    @classmethod
    @property
    def XsdType(cls) -> str:
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
    def GetXsdType(self) -> str:
        """

        :return:
        """
    @classmethod
    def Parse(cls, value: str) -> SoapMonthDay:
        """

        :param value:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class SoapName(Object, ISoapXsd):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, value: str):
        """

        :param value:
        """
    @property
    def Value(self) -> str:
        """

        :return:
        """
    @Value.setter
    def Value(self, value: str) -> None: ...
    @classmethod
    @property
    def XsdType(cls) -> str:
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
    def GetXsdType(self) -> str:
        """

        :return:
        """
    @classmethod
    def Parse(cls, value: str) -> SoapName:
        """

        :param value:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class SoapNcName(Object, ISoapXsd):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, value: str):
        """

        :param value:
        """
    @property
    def Value(self) -> str:
        """

        :return:
        """
    @Value.setter
    def Value(self, value: str) -> None: ...
    @classmethod
    @property
    def XsdType(cls) -> str:
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
    def GetXsdType(self) -> str:
        """

        :return:
        """
    @classmethod
    def Parse(cls, value: str) -> SoapNcName:
        """

        :param value:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class SoapNegativeInteger(Object, ISoapXsd):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, value: Decimal):
        """

        :param value:
        """
    @property
    def Value(self) -> Decimal:
        """

        :return:
        """
    @Value.setter
    def Value(self, value: Decimal) -> None: ...
    @classmethod
    @property
    def XsdType(cls) -> str:
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
    def GetXsdType(self) -> str:
        """

        :return:
        """
    @classmethod
    def Parse(cls, value: str) -> SoapNegativeInteger:
        """

        :param value:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class SoapNmtoken(Object, ISoapXsd):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, value: str):
        """

        :param value:
        """
    @property
    def Value(self) -> str:
        """

        :return:
        """
    @Value.setter
    def Value(self, value: str) -> None: ...
    @classmethod
    @property
    def XsdType(cls) -> str:
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
    def GetXsdType(self) -> str:
        """

        :return:
        """
    @classmethod
    def Parse(cls, value: str) -> SoapNmtoken:
        """

        :param value:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class SoapNmtokens(Object, ISoapXsd):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, value: str):
        """

        :param value:
        """
    @property
    def Value(self) -> str:
        """

        :return:
        """
    @Value.setter
    def Value(self, value: str) -> None: ...
    @classmethod
    @property
    def XsdType(cls) -> str:
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
    def GetXsdType(self) -> str:
        """

        :return:
        """
    @classmethod
    def Parse(cls, value: str) -> SoapNmtokens:
        """

        :param value:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class SoapNonNegativeInteger(Object, ISoapXsd):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, value: Decimal):
        """

        :param value:
        """
    @property
    def Value(self) -> Decimal:
        """

        :return:
        """
    @Value.setter
    def Value(self, value: Decimal) -> None: ...
    @classmethod
    @property
    def XsdType(cls) -> str:
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
    def GetXsdType(self) -> str:
        """

        :return:
        """
    @classmethod
    def Parse(cls, value: str) -> SoapNonNegativeInteger:
        """

        :param value:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class SoapNonPositiveInteger(Object, ISoapXsd):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, value: Decimal):
        """

        :param value:
        """
    @property
    def Value(self) -> Decimal:
        """

        :return:
        """
    @Value.setter
    def Value(self, value: Decimal) -> None: ...
    @classmethod
    @property
    def XsdType(cls) -> str:
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
    def GetXsdType(self) -> str:
        """

        :return:
        """
    @classmethod
    def Parse(cls, value: str) -> SoapNonPositiveInteger:
        """

        :param value:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class SoapNormalizedString(Object, ISoapXsd):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, value: str):
        """

        :param value:
        """
    @property
    def Value(self) -> str:
        """

        :return:
        """
    @Value.setter
    def Value(self, value: str) -> None: ...
    @classmethod
    @property
    def XsdType(cls) -> str:
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
    def GetXsdType(self) -> str:
        """

        :return:
        """
    @classmethod
    def Parse(cls, value: str) -> SoapNormalizedString:
        """

        :param value:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class SoapNotation(Object, ISoapXsd):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, value: str):
        """

        :param value:
        """
    @property
    def Value(self) -> str:
        """

        :return:
        """
    @Value.setter
    def Value(self, value: str) -> None: ...
    @classmethod
    @property
    def XsdType(cls) -> str:
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
    def GetXsdType(self) -> str:
        """

        :return:
        """
    @classmethod
    def Parse(cls, value: str) -> SoapNotation:
        """

        :param value:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class SoapPositiveInteger(Object, ISoapXsd):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, value: Decimal):
        """

        :param value:
        """
    @property
    def Value(self) -> Decimal:
        """

        :return:
        """
    @Value.setter
    def Value(self, value: Decimal) -> None: ...
    @classmethod
    @property
    def XsdType(cls) -> str:
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
    def GetXsdType(self) -> str:
        """

        :return:
        """
    @classmethod
    def Parse(cls, value: str) -> SoapPositiveInteger:
        """

        :param value:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class SoapQName(Object, ISoapXsd):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, value: str):
        """

        :param value:
        """
    @overload
    def __init__(self, key: str, name: str):
        """

        :param key:
        :param name:
        """
    @overload
    def __init__(self, key: str, name: str, namespaceValue: str):
        """

        :param key:
        :param name:
        :param namespaceValue:
        """
    @property
    def Key(self) -> str:
        """

        :return:
        """
    @Key.setter
    def Key(self, value: str) -> None: ...
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def Namespace(self) -> str:
        """

        :return:
        """
    @Namespace.setter
    def Namespace(self, value: str) -> None: ...
    @classmethod
    @property
    def XsdType(cls) -> str:
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
    def GetXsdType(self) -> str:
        """

        :return:
        """
    @classmethod
    def Parse(cls, value: str) -> SoapQName:
        """

        :param value:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class SoapTime(Object, ISoapXsd):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, value: DateTime):
        """

        :param value:
        """
    @property
    def Value(self) -> DateTime:
        """

        :return:
        """
    @Value.setter
    def Value(self, value: DateTime) -> None: ...
    @classmethod
    @property
    def XsdType(cls) -> str:
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
    def GetXsdType(self) -> str:
        """

        :return:
        """
    @classmethod
    def Parse(cls, value: str) -> SoapTime:
        """

        :param value:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class SoapToken(Object, ISoapXsd):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, value: str):
        """

        :param value:
        """
    @property
    def Value(self) -> str:
        """

        :return:
        """
    @Value.setter
    def Value(self, value: str) -> None: ...
    @classmethod
    @property
    def XsdType(cls) -> str:
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
    def GetXsdType(self) -> str:
        """

        :return:
        """
    @classmethod
    def Parse(cls, value: str) -> SoapToken:
        """

        :param value:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class SoapType(ABC, Object):
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

class SoapYear(Object, ISoapXsd):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, value: DateTime):
        """

        :param value:
        """
    @overload
    def __init__(self, value: DateTime, sign: int):
        """

        :param value:
        :param sign:
        """
    @property
    def Sign(self) -> int:
        """

        :return:
        """
    @Sign.setter
    def Sign(self, value: int) -> None: ...
    @property
    def Value(self) -> DateTime:
        """

        :return:
        """
    @Value.setter
    def Value(self, value: DateTime) -> None: ...
    @classmethod
    @property
    def XsdType(cls) -> str:
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
    def GetXsdType(self) -> str:
        """

        :return:
        """
    @classmethod
    def Parse(cls, value: str) -> SoapYear:
        """

        :param value:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class SoapYearMonth(Object, ISoapXsd):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, value: DateTime):
        """

        :param value:
        """
    @overload
    def __init__(self, value: DateTime, sign: int):
        """

        :param value:
        :param sign:
        """
    @property
    def Sign(self) -> int:
        """

        :return:
        """
    @Sign.setter
    def Sign(self, value: int) -> None: ...
    @property
    def Value(self) -> DateTime:
        """

        :return:
        """
    @Value.setter
    def Value(self, value: DateTime) -> None: ...
    @classmethod
    @property
    def XsdType(cls) -> str:
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
    def GetXsdType(self) -> str:
        """

        :return:
        """
    @classmethod
    def Parse(cls, value: str) -> SoapYearMonth:
        """

        :param value:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
