from __future__ import annotations

from abc import ABC
from typing import Callable
from typing import Iterator
from typing import Tuple
from typing import overload

from System import Array
from System import Attribute
from System import Char
from System import DateTime
from System import Decimal
from System import Enum
from System import EventArgs
from System import Exception
from System import Guid
from System import ICloneable
from System import IntPtr
from System import Object
from System import RuntimeFieldHandle
from System import SystemException
from System import Type
from System import TypeCode
from System import TypedReference
from System import ValueType
from System.Collections import Hashtable
from System.Collections import ICollection
from System.Collections import IDictionary
from System.Collections import IEnumerable
from System.Collections import IEnumerator
from System.Collections.Generic import IEnumerable
from System.Collections.Generic import IList
from System.Globalization import CultureInfo
from System.IO import Stream
from System.Reflection import Assembly
from System.Reflection import Binder
from System.Reflection import BindingFlags
from System.Reflection import CustomAttributeData
from System.Reflection import FieldAttributes
from System.Reflection import FieldInfo
from System.Reflection import ICustomAttributeProvider
from System.Reflection import MemberInfo
from System.Reflection import MemberTypes
from System.Reflection import MethodBase
from System.Reflection import Module
from System.Runtime.InteropServices import _Attribute
from System.Runtime.InteropServices import _Exception
from System.Runtime.InteropServices import _FieldInfo
from System.Runtime.InteropServices import _MemberInfo
from System.Runtime.Serialization.Formatters import TypeFilterLevel

DeserializationEventHandler: Callable[[object], None] = ...
"""

:param sender: 
"""

class FixupHolder(Object):
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

class FixupHolderList(Object):
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

class Formatter(ABC, Object, IFormatter):
    """"""

    @property
    def Binder(self) -> SerializationBinder:
        """

        :return:
        """
    @Binder.setter
    def Binder(self, value: SerializationBinder) -> None: ...
    @property
    def Context(self) -> StreamingContext:
        """

        :return:
        """
    @Context.setter
    def Context(self, value: StreamingContext) -> None: ...
    @property
    def SurrogateSelector(self) -> ISurrogateSelector:
        """

        :return:
        """
    @SurrogateSelector.setter
    def SurrogateSelector(self, value: ISurrogateSelector) -> None: ...
    def Deserialize(self, serializationStream: Stream) -> object:
        """

        :param serializationStream:
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
    def Serialize(self, serializationStream: Stream, graph: object) -> None:
        """

        :param serializationStream:
        :param graph:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class FormatterConverter(Object, IFormatterConverter):
    """"""

    def __init__(self):
        """"""
    @overload
    def Convert(self, value: object, type: Type) -> object:
        """

        :param value:
        :param type:
        :return:
        """
    @overload
    def Convert(self, value: object, typeCode: TypeCode) -> object:
        """

        :param value:
        :param typeCode:
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
    def ToBoolean(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    def ToByte(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    def ToChar(self, value: object) -> Char:
        """

        :param value:
        :return:
        """
    def ToDateTime(self, value: object) -> DateTime:
        """

        :param value:
        :return:
        """
    def ToDecimal(self, value: object) -> Decimal:
        """

        :param value:
        :return:
        """
    def ToDouble(self, value: object) -> float:
        """

        :param value:
        :return:
        """
    def ToInt16(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    def ToInt32(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    def ToInt64(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    def ToSByte(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    def ToSingle(self, value: object) -> float:
        """

        :param value:
        :return:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def ToString(self, value: object) -> str:
        """

        :param value:
        :return:
        """
    def ToUInt16(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    def ToUInt32(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    def ToUInt64(self, value: object) -> int:
        """

        :param value:
        :return:
        """

class FormatterServices(ABC, Object):
    """"""

    @classmethod
    def CheckTypeSecurity(cls, t: Type, securityLevel: TypeFilterLevel) -> None:
        """

        :param t:
        :param securityLevel:
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
    @classmethod
    def GetObjectData(cls, obj: object, members: Array[MemberInfo]) -> Array[object]:
        """

        :param obj:
        :param members:
        :return:
        """
    @classmethod
    def GetSafeUninitializedObject(cls, type: Type) -> object:
        """

        :param type:
        :return:
        """
    @classmethod
    @overload
    def GetSerializableMembers(cls, type: Type) -> Array[MemberInfo]:
        """

        :param type:
        :return:
        """
    @classmethod
    @overload
    def GetSerializableMembers(cls, type: Type, context: StreamingContext) -> Array[MemberInfo]:
        """

        :param type:
        :param context:
        :return:
        """
    @classmethod
    def GetSurrogateForCyclicalReference(
        cls, innerSurrogate: ISerializationSurrogate
    ) -> ISerializationSurrogate:
        """

        :param innerSurrogate:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @classmethod
    def GetTypeFromAssembly(cls, assem: Assembly, name: str) -> Type:
        """

        :param assem:
        :param name:
        :return:
        """
    @classmethod
    def GetUninitializedObject(cls, type: Type) -> object:
        """

        :param type:
        :return:
        """
    @classmethod
    def PopulateObjectMembers(
        cls, obj: object, members: Array[MemberInfo], data: Array[object]
    ) -> object:
        """

        :param obj:
        :param members:
        :param data:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class IDeserializationCallback:
    """"""

    def OnDeserialization(self, sender: object) -> None:
        """

        :param sender:
        """

class IFormatter:
    """"""

    @property
    def Binder(self) -> SerializationBinder:
        """

        :return:
        """
    @Binder.setter
    def Binder(self, value: SerializationBinder) -> None: ...
    @property
    def Context(self) -> StreamingContext:
        """

        :return:
        """
    @Context.setter
    def Context(self, value: StreamingContext) -> None: ...
    @property
    def SurrogateSelector(self) -> ISurrogateSelector:
        """

        :return:
        """
    @SurrogateSelector.setter
    def SurrogateSelector(self, value: ISurrogateSelector) -> None: ...
    def Deserialize(self, serializationStream: Stream) -> object:
        """

        :param serializationStream:
        :return:
        """
    def Serialize(self, serializationStream: Stream, graph: object) -> None:
        """

        :param serializationStream:
        :param graph:
        """

class IFormatterConverter:
    """"""

    @overload
    def Convert(self, value: object, type: Type) -> object:
        """

        :param value:
        :param type:
        :return:
        """
    @overload
    def Convert(self, value: object, typeCode: TypeCode) -> object:
        """

        :param value:
        :param typeCode:
        :return:
        """
    def ToBoolean(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    def ToByte(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    def ToChar(self, value: object) -> Char:
        """

        :param value:
        :return:
        """
    def ToDateTime(self, value: object) -> DateTime:
        """

        :param value:
        :return:
        """
    def ToDecimal(self, value: object) -> Decimal:
        """

        :param value:
        :return:
        """
    def ToDouble(self, value: object) -> float:
        """

        :param value:
        :return:
        """
    def ToInt16(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    def ToInt32(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    def ToInt64(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    def ToSByte(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    def ToSingle(self, value: object) -> float:
        """

        :param value:
        :return:
        """
    def ToString(self, value: object) -> str:
        """

        :param value:
        :return:
        """
    def ToUInt16(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    def ToUInt32(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    def ToUInt64(self, value: object) -> int:
        """

        :param value:
        :return:
        """

class IObjectReference:
    """"""

    def GetRealObject(self, context: StreamingContext) -> object:
        """

        :param context:
        :return:
        """

class ISafeSerializationData:
    """"""

    def CompleteDeserialization(self, deserialized: object) -> None:
        """

        :param deserialized:
        """

class ISerializable:
    """"""

    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """

class ISerializationSurrogate:
    """"""

    def GetObjectData(
        self, obj: object, info: SerializationInfo, context: StreamingContext
    ) -> None:
        """

        :param obj:
        :param info:
        :param context:
        """
    def SetObjectData(
        self,
        obj: object,
        info: SerializationInfo,
        context: StreamingContext,
        selector: ISurrogateSelector,
    ) -> object:
        """

        :param obj:
        :param info:
        :param context:
        :param selector:
        :return:
        """

class ISurrogateSelector:
    """"""

    def ChainSelector(self, selector: ISurrogateSelector) -> None:
        """

        :param selector:
        """
    def GetNextSelector(self) -> ISurrogateSelector:
        """

        :return:
        """
    def GetSurrogate(
        self, type: Type, context: StreamingContext, selector: ISurrogateSelector
    ) -> Tuple[ISerializationSurrogate, ISurrogateSelector]:
        """

        :param type:
        :param context:
        :param selector:
        :return:
        """

class LongList(Object):
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

class MemberHolder(Object):
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

class ObjectCloneHelper(ABC, Object):
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

class ObjectHolder(Object):
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

class ObjectHolderList(Object):
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

class ObjectHolderListEnumerator(Object):
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

class ObjectIDGenerator(Object):
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
    def GetId(self, obj: object, firstTime: bool) -> Tuple[int, bool]:
        """

        :param obj:
        :param firstTime:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def HasId(self, obj: object, firstTime: bool) -> Tuple[int, bool]:
        """

        :param obj:
        :param firstTime:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class ObjectManager(Object):
    """"""

    def __init__(self, selector: ISurrogateSelector, context: StreamingContext):
        """

        :param selector:
        :param context:
        """
    def DoFixups(self) -> None:
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
    def GetObject(self, objectID: int) -> object:
        """

        :param objectID:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def RaiseDeserializationEvent(self) -> None:
        """"""
    def RaiseOnDeserializingEvent(self, obj: object) -> None:
        """

        :param obj:
        """
    @overload
    def RecordArrayElementFixup(
        self, arrayToBeFixed: int, indices: Array[int], objectRequired: int
    ) -> None:
        """

        :param arrayToBeFixed:
        :param indices:
        :param objectRequired:
        """
    @overload
    def RecordArrayElementFixup(self, arrayToBeFixed: int, index: int, objectRequired: int) -> None:
        """

        :param arrayToBeFixed:
        :param index:
        :param objectRequired:
        """
    def RecordDelayedFixup(
        self, objectToBeFixed: int, memberName: str, objectRequired: int
    ) -> None:
        """

        :param objectToBeFixed:
        :param memberName:
        :param objectRequired:
        """
    def RecordFixup(self, objectToBeFixed: int, member: MemberInfo, objectRequired: int) -> None:
        """

        :param objectToBeFixed:
        :param member:
        :param objectRequired:
        """
    @overload
    def RegisterObject(self, obj: object, objectID: int) -> None:
        """

        :param obj:
        :param objectID:
        """
    @overload
    def RegisterObject(self, obj: object, objectID: int, info: SerializationInfo) -> None:
        """

        :param obj:
        :param objectID:
        :param info:
        """
    @overload
    def RegisterObject(
        self,
        obj: object,
        objectID: int,
        info: SerializationInfo,
        idOfContainingObj: int,
        member: MemberInfo,
    ) -> None:
        """

        :param obj:
        :param objectID:
        :param info:
        :param idOfContainingObj:
        :param member:
        """
    @overload
    def RegisterObject(
        self,
        obj: object,
        objectID: int,
        info: SerializationInfo,
        idOfContainingObj: int,
        member: MemberInfo,
        arrayIndex: Array[int],
    ) -> None:
        """

        :param obj:
        :param objectID:
        :param info:
        :param idOfContainingObj:
        :param member:
        :param arrayIndex:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class OnDeserializedAttribute(Attribute, _Attribute):
    """"""

    def __init__(self):
        """"""
    @property
    def TypeId(self) -> object:
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

class OnDeserializingAttribute(Attribute, _Attribute):
    """"""

    def __init__(self):
        """"""
    @property
    def TypeId(self) -> object:
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

class OnSerializedAttribute(Attribute, _Attribute):
    """"""

    def __init__(self):
        """"""
    @property
    def TypeId(self) -> object:
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

class OnSerializingAttribute(Attribute, _Attribute):
    """"""

    def __init__(self):
        """"""
    @property
    def TypeId(self) -> object:
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

class OptionalFieldAttribute(Attribute, _Attribute):
    """"""

    def __init__(self):
        """"""
    @property
    def TypeId(self) -> object:
        """

        :return:
        """
    @property
    def VersionAdded(self) -> int:
        """

        :return:
        """
    @VersionAdded.setter
    def VersionAdded(self, value: int) -> None: ...
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

class SafeSerializationEventArgs(EventArgs):
    """"""

    @property
    def StreamingContext(self) -> StreamingContext:
        """

        :return:
        """
    def AddSerializedState(self, serializedState: ISafeSerializationData) -> None:
        """

        :param serializedState:
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
    def ToString(self) -> str:
        """

        :return:
        """

class SafeSerializationManager(Object, IObjectReference, ISerializable):
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
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    def GetRealObject(self, context: StreamingContext) -> object:
        """

        :param context:
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

class SerializationBinder(ABC, Object):
    """"""

    def BindToName(
        self, serializedType: Type, assemblyName: str, typeName: str
    ) -> Tuple[None, str, str]:
        """

        :param serializedType:
        :param assemblyName:
        :param typeName:
        """
    def BindToType(self, assemblyName: str, typeName: str) -> Type:
        """

        :param assemblyName:
        :param typeName:
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
    def ToString(self) -> str:
        """

        :return:
        """

class SerializationEntry(ValueType):
    """"""

    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def ObjectType(self) -> Type:
        """

        :return:
        """
    @property
    def Value(self) -> object:
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
    def ToString(self) -> str:
        """

        :return:
        """

SerializationEventHandler: Callable[[StreamingContext], None] = ...
"""

:param context: 
"""

class SerializationEvents(Object):
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

class SerializationEventsCache(ABC, Object):
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

class SerializationException(SystemException, _Exception, ISerializable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, message: str):
        """

        :param message:
        """
    @overload
    def __init__(self, message: str, innerException: Exception):
        """

        :param message:
        :param innerException:
        """
    @property
    def Data(self) -> IDictionary:
        """

        :return:
        """
    @property
    def HResult(self) -> int:
        """

        :return:
        """
    @property
    def HelpLink(self) -> str:
        """

        :return:
        """
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """

        :return:
        """
    @property
    def Message(self) -> str:
        """

        :return:
        """
    @property
    def Source(self) -> str:
        """

        :return:
        """
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """

        :return:
        """
    @property
    def TargetSite(self) -> MethodBase:
        """

        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetBaseException(self) -> Exception:
        """

        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """

class SerializationFieldInfo(FieldInfo, ICustomAttributeProvider, _FieldInfo, _MemberInfo):
    """"""

    @property
    def Attributes(self) -> FieldAttributes:
        """

        :return:
        """
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
        """

        :return:
        """
    @property
    def DeclaringType(self) -> Type:
        """

        :return:
        """
    @property
    def DeclaringType(self) -> Type:
        """

        :return:
        """
    @property
    def FieldHandle(self) -> RuntimeFieldHandle:
        """

        :return:
        """
    @property
    def FieldType(self) -> Type:
        """

        :return:
        """
    @property
    def IsAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamily(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamilyAndAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamilyOrAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsInitOnly(self) -> bool:
        """

        :return:
        """
    @property
    def IsLiteral(self) -> bool:
        """

        :return:
        """
    @property
    def IsNotSerialized(self) -> bool:
        """

        :return:
        """
    @property
    def IsPinvokeImpl(self) -> bool:
        """

        :return:
        """
    @property
    def IsPrivate(self) -> bool:
        """

        :return:
        """
    @property
    def IsPublic(self) -> bool:
        """

        :return:
        """
    @property
    def IsSecurityCritical(self) -> bool:
        """

        :return:
        """
    @property
    def IsSecuritySafeCritical(self) -> bool:
        """

        :return:
        """
    @property
    def IsSecurityTransparent(self) -> bool:
        """

        :return:
        """
    @property
    def IsSpecialName(self) -> bool:
        """

        :return:
        """
    @property
    def IsStatic(self) -> bool:
        """

        :return:
        """
    @property
    def MemberType(self) -> MemberTypes:
        """

        :return:
        """
    @property
    def MemberType(self) -> MemberTypes:
        """

        :return:
        """
    @property
    def MetadataToken(self) -> int:
        """

        :return:
        """
    @property
    def Module(self) -> Module:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def ReflectedType(self) -> Type:
        """

        :return:
        """
    @property
    def ReflectedType(self) -> Type:
        """

        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def Equals(self, other: object) -> bool:
        """

        :param other:
        :return:
        """
    @overload
    def Equals(self, other: object) -> bool:
        """

        :param other:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]:
        """

        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
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
    @overload
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
    def GetOptionalCustomModifiers(self) -> Array[Type]:
        """

        :return:
        """
    def GetRawConstantValue(self) -> object:
        """

        :return:
        """
    def GetRequiredCustomModifiers(self) -> Array[Type]:
        """

        :return:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    @overload
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    @overload
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    @overload
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    def GetValue(self, obj: object) -> object:
        """

        :param obj:
        :return:
        """
    def GetValueDirect(self, obj: TypedReference) -> object:
        """

        :param obj:
        :return:
        """
    @overload
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
    @overload
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
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def SetValue(self, obj: object, value: object) -> None:
        """

        :param obj:
        :param value:
        """
    @overload
    def SetValue(
        self,
        obj: object,
        value: object,
        invokeAttr: BindingFlags,
        binder: Binder,
        culture: CultureInfo,
    ) -> None:
        """

        :param obj:
        :param value:
        :param invokeAttr:
        :param binder:
        :param culture:
        """
    def SetValueDirect(self, obj: TypedReference, value: object) -> None:
        """

        :param obj:
        :param value:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """

class SerializationInfo(Object):
    """"""

    @overload
    def __init__(self, type: Type, converter: IFormatterConverter):
        """

        :param type:
        :param converter:
        """
    @overload
    def __init__(
        self, type: Type, converter: IFormatterConverter, requireSameTokenInPartialTrust: bool
    ):
        """

        :param type:
        :param converter:
        :param requireSameTokenInPartialTrust:
        """
    @property
    def AssemblyName(self) -> str:
        """

        :return:
        """
    @AssemblyName.setter
    def AssemblyName(self, value: str) -> None: ...
    @property
    def FullTypeName(self) -> str:
        """

        :return:
        """
    @FullTypeName.setter
    def FullTypeName(self, value: str) -> None: ...
    @property
    def IsAssemblyNameSetExplicit(self) -> bool:
        """

        :return:
        """
    @property
    def IsFullTypeNameSetExplicit(self) -> bool:
        """

        :return:
        """
    @property
    def MemberCount(self) -> int:
        """

        :return:
        """
    @property
    def ObjectType(self) -> Type:
        """

        :return:
        """
    @overload
    def AddValue(self, name: str, value: bool) -> None:
        """

        :param name:
        :param value:
        """
    @overload
    def AddValue(self, name: str, value: int) -> None:
        """

        :param name:
        :param value:
        """
    @overload
    def AddValue(self, name: str, value: Char) -> None:
        """

        :param name:
        :param value:
        """
    @overload
    def AddValue(self, name: str, value: DateTime) -> None:
        """

        :param name:
        :param value:
        """
    @overload
    def AddValue(self, name: str, value: Decimal) -> None:
        """

        :param name:
        :param value:
        """
    @overload
    def AddValue(self, name: str, value: float) -> None:
        """

        :param name:
        :param value:
        """
    @overload
    def AddValue(self, name: str, value: int) -> None:
        """

        :param name:
        :param value:
        """
    @overload
    def AddValue(self, name: str, value: int) -> None:
        """

        :param name:
        :param value:
        """
    @overload
    def AddValue(self, name: str, value: int) -> None:
        """

        :param name:
        :param value:
        """
    @overload
    def AddValue(self, name: str, value: object) -> None:
        """

        :param name:
        :param value:
        """
    @overload
    def AddValue(self, name: str, value: int) -> None:
        """

        :param name:
        :param value:
        """
    @overload
    def AddValue(self, name: str, value: float) -> None:
        """

        :param name:
        :param value:
        """
    @overload
    def AddValue(self, name: str, value: int) -> None:
        """

        :param name:
        :param value:
        """
    @overload
    def AddValue(self, name: str, value: int) -> None:
        """

        :param name:
        :param value:
        """
    @overload
    def AddValue(self, name: str, value: int) -> None:
        """

        :param name:
        :param value:
        """
    @overload
    def AddValue(self, name: str, value: object, type: Type) -> None:
        """

        :param name:
        :param value:
        :param type:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetBoolean(self, name: str) -> bool:
        """

        :param name:
        :return:
        """
    def GetByte(self, name: str) -> int:
        """

        :param name:
        :return:
        """
    def GetChar(self, name: str) -> Char:
        """

        :param name:
        :return:
        """
    def GetDateTime(self, name: str) -> DateTime:
        """

        :param name:
        :return:
        """
    def GetDecimal(self, name: str) -> Decimal:
        """

        :param name:
        :return:
        """
    def GetDouble(self, name: str) -> float:
        """

        :param name:
        :return:
        """
    def GetEnumerator(self) -> SerializationInfoEnumerator:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetInt16(self, name: str) -> int:
        """

        :param name:
        :return:
        """
    def GetInt32(self, name: str) -> int:
        """

        :param name:
        :return:
        """
    def GetInt64(self, name: str) -> int:
        """

        :param name:
        :return:
        """
    def GetSByte(self, name: str) -> int:
        """

        :param name:
        :return:
        """
    def GetSingle(self, name: str) -> float:
        """

        :param name:
        :return:
        """
    def GetString(self, name: str) -> str:
        """

        :param name:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetUInt16(self, name: str) -> int:
        """

        :param name:
        :return:
        """
    def GetUInt32(self, name: str) -> int:
        """

        :param name:
        :return:
        """
    def GetUInt64(self, name: str) -> int:
        """

        :param name:
        :return:
        """
    def GetValue(self, name: str, type: Type) -> object:
        """

        :param name:
        :param type:
        :return:
        """
    def SetType(self, type: Type) -> None:
        """

        :param type:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class SerializationInfoEnumerator(Object, IEnumerator):
    """"""

    @property
    def Current(self) -> object:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def ObjectType(self) -> Type:
        """

        :return:
        """
    @property
    def Value(self) -> object:
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
    def MoveNext(self) -> bool:
        """

        :return:
        """
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class SerializationObjectManager(Object):
    """"""

    def __init__(self, context: StreamingContext):
        """

        :param context:
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
    def RaiseOnSerializedEvent(self) -> None:
        """"""
    def RegisterObject(self, obj: object) -> None:
        """

        :param obj:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class StreamingContext(ValueType):
    """"""

    @overload
    def __init__(self, state: StreamingContextStates):
        """

        :param state:
        """
    @overload
    def __init__(self, state: StreamingContextStates, additional: object):
        """

        :param state:
        :param additional:
        """
    @property
    def Context(self) -> object:
        """

        :return:
        """
    @property
    def State(self) -> StreamingContextStates:
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
    def ToString(self) -> str:
        """

        :return:
        """

class StreamingContextStates(Enum):
    """"""

    CrossProcess: StreamingContextStates = ...
    """"""
    CrossMachine: StreamingContextStates = ...
    """"""
    File: StreamingContextStates = ...
    """"""
    Persistence: StreamingContextStates = ...
    """"""
    Remoting: StreamingContextStates = ...
    """"""
    Other: StreamingContextStates = ...
    """"""
    Clone: StreamingContextStates = ...
    """"""
    CrossAppDomain: StreamingContextStates = ...
    """"""
    All: StreamingContextStates = ...
    """"""

class SurrogateForCyclicalReference(Object, ISerializationSurrogate):
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
    def GetObjectData(
        self, obj: object, info: SerializationInfo, context: StreamingContext
    ) -> None:
        """

        :param obj:
        :param info:
        :param context:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def SetObjectData(
        self,
        obj: object,
        info: SerializationInfo,
        context: StreamingContext,
        selector: ISurrogateSelector,
    ) -> object:
        """

        :param obj:
        :param info:
        :param context:
        :param selector:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class SurrogateHashtable(
    Hashtable,
    ICollection,
    IDictionary,
    IEnumerable,
    IDeserializationCallback,
    ISerializable,
    ICloneable,
):
    """"""

    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def IsFixedSize(self) -> bool:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def IsSynchronized(self) -> bool:
        """

        :return:
        """
    @property
    def Item(self) -> object:
        """

        :return:
        """
    @Item.setter
    def Item(self, value: object) -> None: ...
    @property
    def Keys(self) -> ICollection:
        """

        :return:
        """
    @property
    def SyncRoot(self) -> object:
        """

        :return:
        """
    @property
    def Values(self) -> ICollection:
        """

        :return:
        """
    def Add(self, key: object, value: object) -> None:
        """

        :param key:
        :param value:
        """
    def Clear(self) -> None:
        """"""
    def Clone(self) -> object:
        """

        :return:
        """
    def Contains(self, key: object) -> bool:
        """

        :param key:
        :return:
        """
    def ContainsKey(self, key: object) -> bool:
        """

        :param key:
        :return:
        """
    def ContainsValue(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

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
    def OnDeserialization(self, sender: object) -> None:
        """

        :param sender:
        """
    def Remove(self, key: object) -> None:
        """

        :param key:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def __contains__(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    def __getitem__(self, key: object) -> object:
        """

        :param key:
        :return:
        """
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    def __len__(self) -> int:
        """

        :return:
        """
    def __setitem__(self, key: object, value: object) -> None:
        """

        :param key:
        :param value:
        """

class SurrogateKey(Object):
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

class SurrogateSelector(Object, ISurrogateSelector):
    """"""

    def __init__(self):
        """"""
    def AddSurrogate(
        self, type: Type, context: StreamingContext, surrogate: ISerializationSurrogate
    ) -> None:
        """

        :param type:
        :param context:
        :param surrogate:
        """
    def ChainSelector(self, selector: ISurrogateSelector) -> None:
        """

        :param selector:
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
    def GetNextSelector(self) -> ISurrogateSelector:
        """

        :return:
        """
    def GetSurrogate(
        self, type: Type, context: StreamingContext, selector: ISurrogateSelector
    ) -> Tuple[ISerializationSurrogate, ISurrogateSelector]:
        """

        :param type:
        :param context:
        :param selector:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def RemoveSurrogate(self, type: Type, context: StreamingContext) -> None:
        """

        :param type:
        :param context:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class TypeLoadExceptionHolder(Object):
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

class ValueTypeFixupInfo(Object):
    """"""

    def __init__(self, containerID: int, member: FieldInfo, parentIndex: Array[int]):
        """

        :param containerID:
        :param member:
        :param parentIndex:
        """
    @property
    def ContainerID(self) -> int:
        """

        :return:
        """
    @property
    def ParentField(self) -> FieldInfo:
        """

        :return:
        """
    @property
    def ParentIndex(self) -> Array[int]:
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
    def ToString(self) -> str:
        """

        :return:
        """
