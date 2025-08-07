"""Automatically generated stubs for C# namespace: System.Runtime.Remoting.Metadata."""

from abc import ABC

from System import Attribute
from System import Enum
from System import Guid
from System import IntPtr
from System import Object
from System import Type
from System import UInt32
from System.Runtime.InteropServices import _Attribute

class RemotingCachedData(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class RemotingFieldCachedData(RemotingCachedData):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class RemotingMethodCachedData(RemotingCachedData):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class RemotingParameterCachedData(RemotingCachedData):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class RemotingTypeCachedData(RemotingCachedData):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SoapAttribute(Attribute, _Attribute):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Embedded(self) -> bool:
        """"""
    @Embedded.setter
    def Embedded(self, value: bool) -> None: ...
    @property
    def TypeId(self) -> object:
        """"""
    @property
    def UseAttribute(self) -> bool:
        """"""
    @UseAttribute.setter
    def UseAttribute(self, value: bool) -> None: ...
    @property
    def XmlNamespace(self) -> str:
        """"""
    @XmlNamespace.setter
    def XmlNamespace(self, value: str) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """"""
    def GetTypeInfoCount(self, pcTInfo: UInt32) -> tuple[None, UInt32]:
        """"""
    def Invoke(
        self,
        dispIdMember: int,
        riid: Guid,
        lcid: int,
        wFlags: int,
        pDispParams: IntPtr,
        pVarResult: IntPtr,
        pExcepInfo: IntPtr,
        puArgErr: IntPtr,
    ) -> None:
        """"""
    def IsDefaultAttribute(self) -> bool:
        """"""
    def Match(self, obj: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

class SoapFieldAttribute(SoapAttribute, _Attribute):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Embedded(self) -> bool:
        """"""
    @Embedded.setter
    def Embedded(self, value: bool) -> None: ...
    @property
    def Order(self) -> int:
        """"""
    @Order.setter
    def Order(self, value: int) -> None: ...
    @property
    def TypeId(self) -> object:
        """"""
    @property
    def UseAttribute(self) -> bool:
        """"""
    @UseAttribute.setter
    def UseAttribute(self, value: bool) -> None: ...
    @property
    def XmlElementName(self) -> str:
        """"""
    @XmlElementName.setter
    def XmlElementName(self, value: str) -> None: ...
    @property
    def XmlNamespace(self) -> str:
        """"""
    @XmlNamespace.setter
    def XmlNamespace(self, value: str) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """"""
    def GetTypeInfoCount(self, pcTInfo: UInt32) -> tuple[None, UInt32]:
        """"""
    def Invoke(
        self,
        dispIdMember: int,
        riid: Guid,
        lcid: int,
        wFlags: int,
        pDispParams: IntPtr,
        pVarResult: IntPtr,
        pExcepInfo: IntPtr,
        puArgErr: IntPtr,
    ) -> None:
        """"""
    def IsDefaultAttribute(self) -> bool:
        """"""
    def IsInteropXmlElement(self) -> bool:
        """"""
    def Match(self, obj: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

class SoapMethodAttribute(SoapAttribute, _Attribute):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Embedded(self) -> bool:
        """"""
    @Embedded.setter
    def Embedded(self, value: bool) -> None: ...
    @property
    def ResponseXmlElementName(self) -> str:
        """"""
    @ResponseXmlElementName.setter
    def ResponseXmlElementName(self, value: str) -> None: ...
    @property
    def ResponseXmlNamespace(self) -> str:
        """"""
    @ResponseXmlNamespace.setter
    def ResponseXmlNamespace(self, value: str) -> None: ...
    @property
    def ReturnXmlElementName(self) -> str:
        """"""
    @ReturnXmlElementName.setter
    def ReturnXmlElementName(self, value: str) -> None: ...
    @property
    def SoapAction(self) -> str:
        """"""
    @SoapAction.setter
    def SoapAction(self, value: str) -> None: ...
    @property
    def TypeId(self) -> object:
        """"""
    @property
    def UseAttribute(self) -> bool:
        """"""
    @UseAttribute.setter
    def UseAttribute(self, value: bool) -> None: ...
    @property
    def XmlNamespace(self) -> str:
        """"""
    @XmlNamespace.setter
    def XmlNamespace(self, value: str) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """"""
    def GetTypeInfoCount(self, pcTInfo: UInt32) -> tuple[None, UInt32]:
        """"""
    def Invoke(
        self,
        dispIdMember: int,
        riid: Guid,
        lcid: int,
        wFlags: int,
        pDispParams: IntPtr,
        pVarResult: IntPtr,
        pExcepInfo: IntPtr,
        puArgErr: IntPtr,
    ) -> None:
        """"""
    def IsDefaultAttribute(self) -> bool:
        """"""
    def Match(self, obj: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

class SoapOption(Enum):
    """"""

    _None: SoapOption = ...
    """"""
    AlwaysIncludeTypes: SoapOption = ...
    """"""
    XsdString: SoapOption = ...
    """"""
    EmbedAll: SoapOption = ...
    """"""
    Option1: SoapOption = ...
    """"""
    Option2: SoapOption = ...
    """"""

class SoapParameterAttribute(SoapAttribute, _Attribute):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Embedded(self) -> bool:
        """"""
    @Embedded.setter
    def Embedded(self, value: bool) -> None: ...
    @property
    def TypeId(self) -> object:
        """"""
    @property
    def UseAttribute(self) -> bool:
        """"""
    @UseAttribute.setter
    def UseAttribute(self, value: bool) -> None: ...
    @property
    def XmlNamespace(self) -> str:
        """"""
    @XmlNamespace.setter
    def XmlNamespace(self, value: str) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """"""
    def GetTypeInfoCount(self, pcTInfo: UInt32) -> tuple[None, UInt32]:
        """"""
    def Invoke(
        self,
        dispIdMember: int,
        riid: Guid,
        lcid: int,
        wFlags: int,
        pDispParams: IntPtr,
        pVarResult: IntPtr,
        pExcepInfo: IntPtr,
        puArgErr: IntPtr,
    ) -> None:
        """"""
    def IsDefaultAttribute(self) -> bool:
        """"""
    def Match(self, obj: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

class SoapTypeAttribute(SoapAttribute, _Attribute):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Embedded(self) -> bool:
        """"""
    @Embedded.setter
    def Embedded(self, value: bool) -> None: ...
    @property
    def SoapOptions(self) -> SoapOption:
        """"""
    @SoapOptions.setter
    def SoapOptions(self, value: SoapOption) -> None: ...
    @property
    def TypeId(self) -> object:
        """"""
    @property
    def UseAttribute(self) -> bool:
        """"""
    @UseAttribute.setter
    def UseAttribute(self, value: bool) -> None: ...
    @property
    def XmlElementName(self) -> str:
        """"""
    @XmlElementName.setter
    def XmlElementName(self, value: str) -> None: ...
    @property
    def XmlFieldOrder(self) -> XmlFieldOrderOption:
        """"""
    @XmlFieldOrder.setter
    def XmlFieldOrder(self, value: XmlFieldOrderOption) -> None: ...
    @property
    def XmlNamespace(self) -> str:
        """"""
    @XmlNamespace.setter
    def XmlNamespace(self, value: str) -> None: ...
    @property
    def XmlTypeName(self) -> str:
        """"""
    @XmlTypeName.setter
    def XmlTypeName(self, value: str) -> None: ...
    @property
    def XmlTypeNamespace(self) -> str:
        """"""
    @XmlTypeNamespace.setter
    def XmlTypeNamespace(self, value: str) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """"""
    def GetTypeInfoCount(self, pcTInfo: UInt32) -> tuple[None, UInt32]:
        """"""
    def Invoke(
        self,
        dispIdMember: int,
        riid: Guid,
        lcid: int,
        wFlags: int,
        pDispParams: IntPtr,
        pVarResult: IntPtr,
        pExcepInfo: IntPtr,
        puArgErr: IntPtr,
    ) -> None:
        """"""
    def IsDefaultAttribute(self) -> bool:
        """"""
    def Match(self, obj: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

class XmlFieldOrderOption(Enum):
    """"""

    All: XmlFieldOrderOption = ...
    """"""
    Sequence: XmlFieldOrderOption = ...
    """"""
    Choice: XmlFieldOrderOption = ...
    """"""
