from __future__ import annotations

from abc import ABC
from typing import Tuple

from System import Attribute
from System import Enum
from System import Guid
from System import IntPtr
from System import Object
from System import Type
from System.Runtime.InteropServices import _Attribute

class RemotingCachedData(ABC, Object):
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

class RemotingFieldCachedData(RemotingCachedData):
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

class RemotingMethodCachedData(RemotingCachedData):
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

class RemotingParameterCachedData(RemotingCachedData):
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

class RemotingTypeCachedData(RemotingCachedData):
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

class SoapAttribute(Attribute, _Attribute):
    """"""

    def __init__(self):
        """"""
    @property
    def Embedded(self) -> bool:
        """

        :return:
        """
    @Embedded.setter
    def Embedded(self, value: bool) -> None: ...
    @property
    def TypeId(self) -> object:
        """

        :return:
        """
    @property
    def UseAttribute(self) -> bool:
        """

        :return:
        """
    @UseAttribute.setter
    def UseAttribute(self, value: bool) -> None: ...
    @property
    def XmlNamespace(self) -> str:
        """

        :return:
        """
    @XmlNamespace.setter
    def XmlNamespace(self, value: str) -> None: ...
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """

        :return:
        """
    def Match(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class SoapFieldAttribute(SoapAttribute, _Attribute):
    """"""

    def __init__(self):
        """"""
    @property
    def Embedded(self) -> bool:
        """

        :return:
        """
    @Embedded.setter
    def Embedded(self, value: bool) -> None: ...
    @property
    def Order(self) -> int:
        """

        :return:
        """
    @Order.setter
    def Order(self, value: int) -> None: ...
    @property
    def TypeId(self) -> object:
        """

        :return:
        """
    @property
    def UseAttribute(self) -> bool:
        """

        :return:
        """
    @UseAttribute.setter
    def UseAttribute(self, value: bool) -> None: ...
    @property
    def XmlElementName(self) -> str:
        """

        :return:
        """
    @XmlElementName.setter
    def XmlElementName(self, value: str) -> None: ...
    @property
    def XmlNamespace(self) -> str:
        """

        :return:
        """
    @XmlNamespace.setter
    def XmlNamespace(self, value: str) -> None: ...
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """

        :return:
        """
    def IsInteropXmlElement(self) -> bool:
        """

        :return:
        """
    def Match(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class SoapMethodAttribute(SoapAttribute, _Attribute):
    """"""

    def __init__(self):
        """"""
    @property
    def Embedded(self) -> bool:
        """

        :return:
        """
    @Embedded.setter
    def Embedded(self, value: bool) -> None: ...
    @property
    def ResponseXmlElementName(self) -> str:
        """

        :return:
        """
    @ResponseXmlElementName.setter
    def ResponseXmlElementName(self, value: str) -> None: ...
    @property
    def ResponseXmlNamespace(self) -> str:
        """

        :return:
        """
    @ResponseXmlNamespace.setter
    def ResponseXmlNamespace(self, value: str) -> None: ...
    @property
    def ReturnXmlElementName(self) -> str:
        """

        :return:
        """
    @ReturnXmlElementName.setter
    def ReturnXmlElementName(self, value: str) -> None: ...
    @property
    def SoapAction(self) -> str:
        """

        :return:
        """
    @SoapAction.setter
    def SoapAction(self, value: str) -> None: ...
    @property
    def TypeId(self) -> object:
        """

        :return:
        """
    @property
    def UseAttribute(self) -> bool:
        """

        :return:
        """
    @UseAttribute.setter
    def UseAttribute(self, value: bool) -> None: ...
    @property
    def XmlNamespace(self) -> str:
        """

        :return:
        """
    @XmlNamespace.setter
    def XmlNamespace(self, value: str) -> None: ...
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """

        :return:
        """
    def Match(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

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

    def __init__(self):
        """"""
    @property
    def Embedded(self) -> bool:
        """

        :return:
        """
    @Embedded.setter
    def Embedded(self, value: bool) -> None: ...
    @property
    def TypeId(self) -> object:
        """

        :return:
        """
    @property
    def UseAttribute(self) -> bool:
        """

        :return:
        """
    @UseAttribute.setter
    def UseAttribute(self, value: bool) -> None: ...
    @property
    def XmlNamespace(self) -> str:
        """

        :return:
        """
    @XmlNamespace.setter
    def XmlNamespace(self, value: str) -> None: ...
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """

        :return:
        """
    def Match(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class SoapTypeAttribute(SoapAttribute, _Attribute):
    """"""

    def __init__(self):
        """"""
    @property
    def Embedded(self) -> bool:
        """

        :return:
        """
    @Embedded.setter
    def Embedded(self, value: bool) -> None: ...
    @property
    def SoapOptions(self) -> SoapOption:
        """

        :return:
        """
    @SoapOptions.setter
    def SoapOptions(self, value: SoapOption) -> None: ...
    @property
    def TypeId(self) -> object:
        """

        :return:
        """
    @property
    def UseAttribute(self) -> bool:
        """

        :return:
        """
    @UseAttribute.setter
    def UseAttribute(self, value: bool) -> None: ...
    @property
    def XmlElementName(self) -> str:
        """

        :return:
        """
    @XmlElementName.setter
    def XmlElementName(self, value: str) -> None: ...
    @property
    def XmlFieldOrder(self) -> XmlFieldOrderOption:
        """

        :return:
        """
    @XmlFieldOrder.setter
    def XmlFieldOrder(self, value: XmlFieldOrderOption) -> None: ...
    @property
    def XmlNamespace(self) -> str:
        """

        :return:
        """
    @XmlNamespace.setter
    def XmlNamespace(self, value: str) -> None: ...
    @property
    def XmlTypeName(self) -> str:
        """

        :return:
        """
    @XmlTypeName.setter
    def XmlTypeName(self, value: str) -> None: ...
    @property
    def XmlTypeNamespace(self) -> str:
        """

        :return:
        """
    @XmlTypeNamespace.setter
    def XmlTypeNamespace(self, value: str) -> None: ...
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """

        :return:
        """
    def Match(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class XmlFieldOrderOption(Enum):
    """"""

    All: XmlFieldOrderOption = ...
    """"""
    Sequence: XmlFieldOrderOption = ...
    """"""
    Choice: XmlFieldOrderOption = ...
    """"""
