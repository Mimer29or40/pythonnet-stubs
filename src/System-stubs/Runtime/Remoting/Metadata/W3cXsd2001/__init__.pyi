"""Automatically generated stubs for C# namespace: System.Runtime.Remoting.Metadata.W3cXsd2001."""

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
        """"""

class SoapAnyUri(Object, ISoapXsd):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, value: str) -> None:
        """"""
    @property
    def Value(self) -> str:
        """"""
    @Value.setter
    def Value(self, value: str) -> None: ...
    @classmethod
    @property
    def XsdType(cls) -> str:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetXsdType(self) -> str:
        """"""
    @classmethod
    def Parse(cls, value: str) -> SoapAnyUri:
        """"""
    def ToString(self) -> str:
        """"""

class SoapBase64Binary(Object, ISoapXsd):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, value: Array[int]) -> None:
        """"""
    @property
    def Value(self) -> Array[int]:
        """"""
    @Value.setter
    def Value(self, value: Array[int]) -> None: ...
    @classmethod
    @property
    def XsdType(cls) -> str:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetXsdType(self) -> str:
        """"""
    @classmethod
    def Parse(cls, value: str) -> SoapBase64Binary:
        """"""
    def ToString(self) -> str:
        """"""

class SoapDate(Object, ISoapXsd):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, value: DateTime) -> None:
        """"""
    @overload
    def __init__(self, value: DateTime, sign: int) -> None:
        """"""
    @property
    def Sign(self) -> int:
        """"""
    @Sign.setter
    def Sign(self, value: int) -> None: ...
    @property
    def Value(self) -> DateTime:
        """"""
    @Value.setter
    def Value(self, value: DateTime) -> None: ...
    @classmethod
    @property
    def XsdType(cls) -> str:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetXsdType(self) -> str:
        """"""
    @classmethod
    def Parse(cls, value: str) -> SoapDate:
        """"""
    def ToString(self) -> str:
        """"""

class SoapDateTime(Object):
    """"""
    def __init__(self) -> None:
        """"""
    @classmethod
    @property
    def XsdType(cls) -> str:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def Parse(cls, value: str) -> DateTime:
        """"""
    @overload
    def ToString(self) -> str:
        """"""
    @classmethod
    @overload
    def ToString(cls, value: DateTime) -> str:
        """"""

class SoapDay(Object, ISoapXsd):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, value: DateTime) -> None:
        """"""
    @property
    def Value(self) -> DateTime:
        """"""
    @Value.setter
    def Value(self, value: DateTime) -> None: ...
    @classmethod
    @property
    def XsdType(cls) -> str:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetXsdType(self) -> str:
        """"""
    @classmethod
    def Parse(cls, value: str) -> SoapDay:
        """"""
    def ToString(self) -> str:
        """"""

class SoapDuration(Object):
    """"""
    def __init__(self) -> None:
        """"""
    @classmethod
    @property
    def XsdType(cls) -> str:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def Parse(cls, value: str) -> TimeSpan:
        """"""
    @overload
    def ToString(self) -> str:
        """"""
    @classmethod
    @overload
    def ToString(cls, timeSpan: TimeSpan) -> str:
        """"""

class SoapEntities(Object, ISoapXsd):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, value: str) -> None:
        """"""
    @property
    def Value(self) -> str:
        """"""
    @Value.setter
    def Value(self, value: str) -> None: ...
    @classmethod
    @property
    def XsdType(cls) -> str:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetXsdType(self) -> str:
        """"""
    @classmethod
    def Parse(cls, value: str) -> SoapEntities:
        """"""
    def ToString(self) -> str:
        """"""

class SoapEntity(Object, ISoapXsd):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, value: str) -> None:
        """"""
    @property
    def Value(self) -> str:
        """"""
    @Value.setter
    def Value(self, value: str) -> None: ...
    @classmethod
    @property
    def XsdType(cls) -> str:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetXsdType(self) -> str:
        """"""
    @classmethod
    def Parse(cls, value: str) -> SoapEntity:
        """"""
    def ToString(self) -> str:
        """"""

class SoapHexBinary(Object, ISoapXsd):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, value: Array[int]) -> None:
        """"""
    @property
    def Value(self) -> Array[int]:
        """"""
    @Value.setter
    def Value(self, value: Array[int]) -> None: ...
    @classmethod
    @property
    def XsdType(cls) -> str:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetXsdType(self) -> str:
        """"""
    @classmethod
    def Parse(cls, value: str) -> SoapHexBinary:
        """"""
    def ToString(self) -> str:
        """"""

class SoapId(Object, ISoapXsd):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, value: str) -> None:
        """"""
    @property
    def Value(self) -> str:
        """"""
    @Value.setter
    def Value(self, value: str) -> None: ...
    @classmethod
    @property
    def XsdType(cls) -> str:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetXsdType(self) -> str:
        """"""
    @classmethod
    def Parse(cls, value: str) -> SoapId:
        """"""
    def ToString(self) -> str:
        """"""

class SoapIdref(Object, ISoapXsd):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, value: str) -> None:
        """"""
    @property
    def Value(self) -> str:
        """"""
    @Value.setter
    def Value(self, value: str) -> None: ...
    @classmethod
    @property
    def XsdType(cls) -> str:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetXsdType(self) -> str:
        """"""
    @classmethod
    def Parse(cls, value: str) -> SoapIdref:
        """"""
    def ToString(self) -> str:
        """"""

class SoapIdrefs(Object, ISoapXsd):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, value: str) -> None:
        """"""
    @property
    def Value(self) -> str:
        """"""
    @Value.setter
    def Value(self, value: str) -> None: ...
    @classmethod
    @property
    def XsdType(cls) -> str:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetXsdType(self) -> str:
        """"""
    @classmethod
    def Parse(cls, value: str) -> SoapIdrefs:
        """"""
    def ToString(self) -> str:
        """"""

class SoapInteger(Object, ISoapXsd):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, value: Decimal) -> None:
        """"""
    @property
    def Value(self) -> Decimal:
        """"""
    @Value.setter
    def Value(self, value: Decimal) -> None: ...
    @classmethod
    @property
    def XsdType(cls) -> str:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetXsdType(self) -> str:
        """"""
    @classmethod
    def Parse(cls, value: str) -> SoapInteger:
        """"""
    def ToString(self) -> str:
        """"""

class SoapLanguage(Object, ISoapXsd):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, value: str) -> None:
        """"""
    @property
    def Value(self) -> str:
        """"""
    @Value.setter
    def Value(self, value: str) -> None: ...
    @classmethod
    @property
    def XsdType(cls) -> str:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetXsdType(self) -> str:
        """"""
    @classmethod
    def Parse(cls, value: str) -> SoapLanguage:
        """"""
    def ToString(self) -> str:
        """"""

class SoapMonth(Object, ISoapXsd):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, value: DateTime) -> None:
        """"""
    @property
    def Value(self) -> DateTime:
        """"""
    @Value.setter
    def Value(self, value: DateTime) -> None: ...
    @classmethod
    @property
    def XsdType(cls) -> str:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetXsdType(self) -> str:
        """"""
    @classmethod
    def Parse(cls, value: str) -> SoapMonth:
        """"""
    def ToString(self) -> str:
        """"""

class SoapMonthDay(Object, ISoapXsd):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, value: DateTime) -> None:
        """"""
    @property
    def Value(self) -> DateTime:
        """"""
    @Value.setter
    def Value(self, value: DateTime) -> None: ...
    @classmethod
    @property
    def XsdType(cls) -> str:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetXsdType(self) -> str:
        """"""
    @classmethod
    def Parse(cls, value: str) -> SoapMonthDay:
        """"""
    def ToString(self) -> str:
        """"""

class SoapName(Object, ISoapXsd):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, value: str) -> None:
        """"""
    @property
    def Value(self) -> str:
        """"""
    @Value.setter
    def Value(self, value: str) -> None: ...
    @classmethod
    @property
    def XsdType(cls) -> str:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetXsdType(self) -> str:
        """"""
    @classmethod
    def Parse(cls, value: str) -> SoapName:
        """"""
    def ToString(self) -> str:
        """"""

class SoapNcName(Object, ISoapXsd):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, value: str) -> None:
        """"""
    @property
    def Value(self) -> str:
        """"""
    @Value.setter
    def Value(self, value: str) -> None: ...
    @classmethod
    @property
    def XsdType(cls) -> str:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetXsdType(self) -> str:
        """"""
    @classmethod
    def Parse(cls, value: str) -> SoapNcName:
        """"""
    def ToString(self) -> str:
        """"""

class SoapNegativeInteger(Object, ISoapXsd):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, value: Decimal) -> None:
        """"""
    @property
    def Value(self) -> Decimal:
        """"""
    @Value.setter
    def Value(self, value: Decimal) -> None: ...
    @classmethod
    @property
    def XsdType(cls) -> str:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetXsdType(self) -> str:
        """"""
    @classmethod
    def Parse(cls, value: str) -> SoapNegativeInteger:
        """"""
    def ToString(self) -> str:
        """"""

class SoapNmtoken(Object, ISoapXsd):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, value: str) -> None:
        """"""
    @property
    def Value(self) -> str:
        """"""
    @Value.setter
    def Value(self, value: str) -> None: ...
    @classmethod
    @property
    def XsdType(cls) -> str:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetXsdType(self) -> str:
        """"""
    @classmethod
    def Parse(cls, value: str) -> SoapNmtoken:
        """"""
    def ToString(self) -> str:
        """"""

class SoapNmtokens(Object, ISoapXsd):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, value: str) -> None:
        """"""
    @property
    def Value(self) -> str:
        """"""
    @Value.setter
    def Value(self, value: str) -> None: ...
    @classmethod
    @property
    def XsdType(cls) -> str:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetXsdType(self) -> str:
        """"""
    @classmethod
    def Parse(cls, value: str) -> SoapNmtokens:
        """"""
    def ToString(self) -> str:
        """"""

class SoapNonNegativeInteger(Object, ISoapXsd):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, value: Decimal) -> None:
        """"""
    @property
    def Value(self) -> Decimal:
        """"""
    @Value.setter
    def Value(self, value: Decimal) -> None: ...
    @classmethod
    @property
    def XsdType(cls) -> str:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetXsdType(self) -> str:
        """"""
    @classmethod
    def Parse(cls, value: str) -> SoapNonNegativeInteger:
        """"""
    def ToString(self) -> str:
        """"""

class SoapNonPositiveInteger(Object, ISoapXsd):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, value: Decimal) -> None:
        """"""
    @property
    def Value(self) -> Decimal:
        """"""
    @Value.setter
    def Value(self, value: Decimal) -> None: ...
    @classmethod
    @property
    def XsdType(cls) -> str:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetXsdType(self) -> str:
        """"""
    @classmethod
    def Parse(cls, value: str) -> SoapNonPositiveInteger:
        """"""
    def ToString(self) -> str:
        """"""

class SoapNormalizedString(Object, ISoapXsd):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, value: str) -> None:
        """"""
    @property
    def Value(self) -> str:
        """"""
    @Value.setter
    def Value(self, value: str) -> None: ...
    @classmethod
    @property
    def XsdType(cls) -> str:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetXsdType(self) -> str:
        """"""
    @classmethod
    def Parse(cls, value: str) -> SoapNormalizedString:
        """"""
    def ToString(self) -> str:
        """"""

class SoapNotation(Object, ISoapXsd):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, value: str) -> None:
        """"""
    @property
    def Value(self) -> str:
        """"""
    @Value.setter
    def Value(self, value: str) -> None: ...
    @classmethod
    @property
    def XsdType(cls) -> str:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetXsdType(self) -> str:
        """"""
    @classmethod
    def Parse(cls, value: str) -> SoapNotation:
        """"""
    def ToString(self) -> str:
        """"""

class SoapPositiveInteger(Object, ISoapXsd):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, value: Decimal) -> None:
        """"""
    @property
    def Value(self) -> Decimal:
        """"""
    @Value.setter
    def Value(self, value: Decimal) -> None: ...
    @classmethod
    @property
    def XsdType(cls) -> str:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetXsdType(self) -> str:
        """"""
    @classmethod
    def Parse(cls, value: str) -> SoapPositiveInteger:
        """"""
    def ToString(self) -> str:
        """"""

class SoapQName(Object, ISoapXsd):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, value: str) -> None:
        """"""
    @overload
    def __init__(self, key: str, name: str) -> None:
        """"""
    @overload
    def __init__(self, key: str, name: str, namespaceValue: str) -> None:
        """"""
    @property
    def Key(self) -> str:
        """"""
    @Key.setter
    def Key(self, value: str) -> None: ...
    @property
    def Name(self) -> str:
        """"""
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def Namespace(self) -> str:
        """"""
    @Namespace.setter
    def Namespace(self, value: str) -> None: ...
    @classmethod
    @property
    def XsdType(cls) -> str:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetXsdType(self) -> str:
        """"""
    @classmethod
    def Parse(cls, value: str) -> SoapQName:
        """"""
    def ToString(self) -> str:
        """"""

class SoapTime(Object, ISoapXsd):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, value: DateTime) -> None:
        """"""
    @property
    def Value(self) -> DateTime:
        """"""
    @Value.setter
    def Value(self, value: DateTime) -> None: ...
    @classmethod
    @property
    def XsdType(cls) -> str:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetXsdType(self) -> str:
        """"""
    @classmethod
    def Parse(cls, value: str) -> SoapTime:
        """"""
    def ToString(self) -> str:
        """"""

class SoapToken(Object, ISoapXsd):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, value: str) -> None:
        """"""
    @property
    def Value(self) -> str:
        """"""
    @Value.setter
    def Value(self, value: str) -> None: ...
    @classmethod
    @property
    def XsdType(cls) -> str:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetXsdType(self) -> str:
        """"""
    @classmethod
    def Parse(cls, value: str) -> SoapToken:
        """"""
    def ToString(self) -> str:
        """"""

class SoapType(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SoapYear(Object, ISoapXsd):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, value: DateTime) -> None:
        """"""
    @overload
    def __init__(self, value: DateTime, sign: int) -> None:
        """"""
    @property
    def Sign(self) -> int:
        """"""
    @Sign.setter
    def Sign(self, value: int) -> None: ...
    @property
    def Value(self) -> DateTime:
        """"""
    @Value.setter
    def Value(self, value: DateTime) -> None: ...
    @classmethod
    @property
    def XsdType(cls) -> str:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetXsdType(self) -> str:
        """"""
    @classmethod
    def Parse(cls, value: str) -> SoapYear:
        """"""
    def ToString(self) -> str:
        """"""

class SoapYearMonth(Object, ISoapXsd):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, value: DateTime) -> None:
        """"""
    @overload
    def __init__(self, value: DateTime, sign: int) -> None:
        """"""
    @property
    def Sign(self) -> int:
        """"""
    @Sign.setter
    def Sign(self, value: int) -> None: ...
    @property
    def Value(self) -> DateTime:
        """"""
    @Value.setter
    def Value(self, value: DateTime) -> None: ...
    @classmethod
    @property
    def XsdType(cls) -> str:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetXsdType(self) -> str:
        """"""
    @classmethod
    def Parse(cls, value: str) -> SoapYearMonth:
        """"""
    def ToString(self) -> str:
        """"""
