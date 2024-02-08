from __future__ import annotations

from abc import ABC
from typing import Callable
from typing import ClassVar
from typing import Final
from typing import Generic
from typing import Iterator
from typing import Tuple
from typing import TypeVar
from typing import overload

from System import ArgumentException
from System import Array
from System import Attribute
from System import Char
from System import Delegate
from System import Enum
from System import EventArgs
from System import EventHandler
from System import Exception
from System import Guid
from System import IAsyncResult
from System import ICloneable
from System import IDisposable
from System import IntPtr
from System import IServiceProvider
from System import MarshalByRefObject
from System import Object
from System import SystemException
from System import Type
from System.Collections import Hashtable
from System.Collections import ICollection
from System.Collections import IComparer
from System.Collections import IDictionary
from System.Collections import IEnumerable
from System.Collections import IEnumerator
from System.Collections import IList
from System.Collections import ReadOnlyCollectionBase
from System.Collections.Generic import ICollection
from System.Collections.Generic import IEnumerable
from System.Collections.Generic import IList
from System.Collections.Generic import IReadOnlyCollection
from System.Collections.Generic import IReadOnlyList
from System.Collections.ObjectModel import Collection
from System.ComponentModel.Design import IDesigner
from System.ComponentModel.TypeConverter import StandardValuesCollection
from System.Diagnostics import BooleanSwitch
from System.Diagnostics import TraceSwitch
from System.Globalization import CultureInfo
from System.IO import UnmanagedMemoryStream
from System.Reflection import Assembly
from System.Reflection import EventInfo
from System.Reflection import MethodBase
from System.Reflection import MethodInfo
from System.Reflection import Module
from System.Reflection import PropertyInfo
from System.Resources import ResourceManager
from System.Resources import ResourceSet
from System.Runtime.InteropServices import ExternalException
from System.Runtime.InteropServices import _Attribute
from System.Runtime.InteropServices import _Exception
from System.Runtime.Remoting import ObjRef
from System.Runtime.Serialization import IDeserializationCallback
from System.Runtime.Serialization import ISerializable
from System.Runtime.Serialization import SerializationInfo
from System.Runtime.Serialization import StreamingContext
from System.Security import CodeAccessPermission
from System.Threading import SendOrPostCallback
from System.Threading import SynchronizationContext

T = TypeVar("T")

class EventType(Generic[T]):
    def __iadd__(self, other: T): ...
    def __isub__(self, other: T): ...

class AddingNewEventArgs(EventArgs):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, newObject: object):
        """

        :param newObject:
        """
    @property
    def NewObject(self) -> object:
        """

        :return:
        """
    @NewObject.setter
    def NewObject(self, value: object) -> None: ...
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

AddingNewEventHandler: Callable[[object, AddingNewEventArgs], None] = ...
"""

:param sender: 
:param e: 
"""

class AmbientValueAttribute(Attribute, _Attribute):
    """"""

    @overload
    def __init__(self, value: bool):
        """

        :param value:
        """
    @overload
    def __init__(self, value: int):
        """

        :param value:
        """
    @overload
    def __init__(self, value: Char):
        """

        :param value:
        """
    @overload
    def __init__(self, value: float):
        """

        :param value:
        """
    @overload
    def __init__(self, value: int):
        """

        :param value:
        """
    @overload
    def __init__(self, value: int):
        """

        :param value:
        """
    @overload
    def __init__(self, value: int):
        """

        :param value:
        """
    @overload
    def __init__(self, value: object):
        """

        :param value:
        """
    @overload
    def __init__(self, value: float):
        """

        :param value:
        """
    @overload
    def __init__(self, value: str):
        """

        :param value:
        """
    @overload
    def __init__(self, type: Type, value: str):
        """

        :param type:
        :param value:
        """
    @property
    def TypeId(self) -> object:
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

class ArrayConverter(CollectionConverter):
    """"""

    def __init__(self):
        """"""
    @overload
    def CanConvertFrom(self, sourceType: Type) -> bool:
        """

        :param sourceType:
        :return:
        """
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool:
        """

        :param context:
        :param sourceType:
        :return:
        """
    @overload
    def CanConvertTo(self, destinationType: Type) -> bool:
        """

        :param destinationType:
        :return:
        """
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, destinationType: Type) -> bool:
        """

        :param context:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertFrom(self, value: object) -> object:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertFrom(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> object:
        """

        :param context:
        :param culture:
        :param value:
        :return:
        """
    @overload
    def ConvertFromInvariantString(self, text: str) -> object:
        """

        :param text:
        :return:
        """
    @overload
    def ConvertFromInvariantString(self, context: ITypeDescriptorContext, text: str) -> object:
        """

        :param context:
        :param text:
        :return:
        """
    @overload
    def ConvertFromString(self, text: str) -> object:
        """

        :param text:
        :return:
        """
    @overload
    def ConvertFromString(self, context: ITypeDescriptorContext, text: str) -> object:
        """

        :param context:
        :param text:
        :return:
        """
    @overload
    def ConvertFromString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, text: str
    ) -> object:
        """

        :param context:
        :param culture:
        :param text:
        :return:
        """
    @overload
    def ConvertTo(self, value: object, destinationType: Type) -> object:
        """

        :param value:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertTo(
        self,
        context: ITypeDescriptorContext,
        culture: CultureInfo,
        value: object,
        destinationType: Type,
    ) -> object:
        """

        :param context:
        :param culture:
        :param value:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertToInvariantString(self, value: object) -> str:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertToInvariantString(self, context: ITypeDescriptorContext, value: object) -> str:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def ConvertToString(self, value: object) -> str:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertToString(self, context: ITypeDescriptorContext, value: object) -> str:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def ConvertToString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> str:
        """

        :param context:
        :param culture:
        :param value:
        :return:
        """
    @overload
    def CreateInstance(self, propertyValues: IDictionary) -> object:
        """

        :param propertyValues:
        :return:
        """
    @overload
    def CreateInstance(
        self, context: ITypeDescriptorContext, propertyValues: IDictionary
    ) -> object:
        """

        :param context:
        :param propertyValues:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetCreateInstanceSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetCreateInstanceSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetProperties(self, value: object) -> PropertyDescriptorCollection:
        """

        :param value:
        :return:
        """
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object
    ) -> PropertyDescriptorCollection:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]
    ) -> PropertyDescriptorCollection:
        """

        :param context:
        :param value:
        :param attributes:
        :return:
        """
    @overload
    def GetPropertiesSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetPropertiesSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValues(self) -> ICollection:
        """

        :return:
        """
    @overload
    def GetStandardValues(
        self, context: ITypeDescriptorContext
    ) -> TypeConverter.StandardValuesCollection:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValuesExclusive(self) -> bool:
        """

        :return:
        """
    @overload
    def GetStandardValuesExclusive(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValuesSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetStandardValuesSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def IsValid(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def IsValid(self, context: ITypeDescriptorContext, value: object) -> bool:
        """

        :param context:
        :param value:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class ArraySubsetEnumerator(Object, IEnumerator):
    """"""

    def __init__(self, array: Array, count: int):
        """

        :param array:
        :param count:
        """
    @property
    def Current(self) -> object:
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

class AsyncCompletedEventArgs(EventArgs):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, error: Exception, cancelled: bool, userState: object):
        """

        :param error:
        :param cancelled:
        :param userState:
        """
    @property
    def Cancelled(self) -> bool:
        """

        :return:
        """
    @property
    def Error(self) -> Exception:
        """

        :return:
        """
    @property
    def UserState(self) -> object:
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

AsyncCompletedEventHandler: Callable[[object, AsyncCompletedEventArgs], None] = ...
"""

:param sender: 
:param e: 
"""

class AsyncOperation(Object):
    """"""

    @property
    def SynchronizationContext(self) -> SynchronizationContext:
        """

        :return:
        """
    @property
    def UserSuppliedState(self) -> object:
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
    def OperationCompleted(self) -> None:
        """"""
    def Post(self, d: SendOrPostCallback, arg: object) -> None:
        """

        :param d:
        :param arg:
        """
    def PostOperationCompleted(self, d: SendOrPostCallback, arg: object) -> None:
        """

        :param d:
        :param arg:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class AsyncOperationManager(ABC, Object):
    """"""

    @classmethod
    @property
    def SynchronizationContext(cls) -> SynchronizationContext:
        """

        :return:
        """
    @classmethod
    @SynchronizationContext.setter
    def SynchronizationContext(cls, value: SynchronizationContext) -> None: ...
    @classmethod
    def CreateOperation(cls, userSuppliedState: object) -> AsyncOperation:
        """

        :param userSuppliedState:
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

class AttributeCollection(Object, ICollection, IEnumerable):
    """"""

    Empty: Final[ClassVar[AttributeCollection]] = ...
    """
    
    :return: 
    """
    def __init__(self, attributes: Array[Attribute]):
        """

        :param attributes:
        """
    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def IsSynchronized(self) -> bool:
        """

        :return:
        """
    @property
    def Item(self) -> Attribute:
        """

        :return:
        """
    @property
    def SyncRoot(self) -> object:
        """

        :return:
        """
    @overload
    def Contains(self, attributes: Array[Attribute]) -> bool:
        """

        :param attributes:
        :return:
        """
    @overload
    def Contains(self, attribute: Attribute) -> bool:
        """

        :param attribute:
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
    @classmethod
    def FromExisting(
        cls, existing: AttributeCollection, newAttributes: Array[Attribute]
    ) -> AttributeCollection:
        """

        :param existing:
        :param newAttributes:
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
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def Matches(self, attributes: Array[Attribute]) -> bool:
        """

        :param attributes:
        :return:
        """
    @overload
    def Matches(self, attribute: Attribute) -> bool:
        """

        :param attribute:
        :return:
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
    @overload
    def __getitem__(self, index: int) -> Attribute:
        """

        :param index:
        :return:
        """
    @overload
    def __getitem__(self, attributeType: Type) -> Attribute:
        """

        :param attributeType:
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

class AttributeProviderAttribute(Attribute, _Attribute):
    """"""

    @overload
    def __init__(self, typeName: str):
        """

        :param typeName:
        """
    @overload
    def __init__(self, type: Type):
        """

        :param type:
        """
    @overload
    def __init__(self, typeName: str, propertyName: str):
        """

        :param typeName:
        :param propertyName:
        """
    @property
    def PropertyName(self) -> str:
        """

        :return:
        """
    @property
    def TypeId(self) -> object:
        """

        :return:
        """
    @property
    def TypeName(self) -> str:
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

class BackgroundWorker(Component, IComponent, IDisposable):
    """"""

    def __init__(self):
        """"""
    @property
    def CancellationPending(self) -> bool:
        """

        :return:
        """
    @property
    def Container(self) -> IContainer:
        """

        :return:
        """
    @property
    def IsBusy(self) -> bool:
        """

        :return:
        """
    @property
    def Site(self) -> ISite:
        """

        :return:
        """
    @Site.setter
    def Site(self, value: ISite) -> None: ...
    @property
    def WorkerReportsProgress(self) -> bool:
        """

        :return:
        """
    @WorkerReportsProgress.setter
    def WorkerReportsProgress(self, value: bool) -> None: ...
    @property
    def WorkerSupportsCancellation(self) -> bool:
        """

        :return:
        """
    @WorkerSupportsCancellation.setter
    def WorkerSupportsCancellation(self, value: bool) -> None: ...
    def CancelAsync(self) -> None:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """

        :param requestedType:
        :return:
        """
    def Dispose(self) -> None:
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
    def GetLifetimeService(self) -> object:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def InitializeLifetimeService(self) -> object:
        """

        :return:
        """
    @overload
    def ReportProgress(self, percentProgress: int) -> None:
        """

        :param percentProgress:
        """
    @overload
    def ReportProgress(self, percentProgress: int, userState: object) -> None:
        """

        :param percentProgress:
        :param userState:
        """
    @overload
    def RunWorkerAsync(self) -> None:
        """"""
    @overload
    def RunWorkerAsync(self, argument: object) -> None:
        """

        :param argument:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    Disposed: EventType[EventHandler] = ...
    """"""
    DoWork: EventType[DoWorkEventHandler] = ...
    """"""
    ProgressChanged: EventType[ProgressChangedEventHandler] = ...
    """"""
    RunWorkerCompleted: EventType[RunWorkerCompletedEventHandler] = ...
    """"""

class BaseNumberConverter(ABC, TypeConverter):
    """"""

    @overload
    def CanConvertFrom(self, sourceType: Type) -> bool:
        """

        :param sourceType:
        :return:
        """
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool:
        """

        :param context:
        :param sourceType:
        :return:
        """
    @overload
    def CanConvertTo(self, destinationType: Type) -> bool:
        """

        :param destinationType:
        :return:
        """
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, destinationType: Type) -> bool:
        """

        :param context:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertFrom(self, value: object) -> object:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertFrom(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> object:
        """

        :param context:
        :param culture:
        :param value:
        :return:
        """
    @overload
    def ConvertFromInvariantString(self, text: str) -> object:
        """

        :param text:
        :return:
        """
    @overload
    def ConvertFromInvariantString(self, context: ITypeDescriptorContext, text: str) -> object:
        """

        :param context:
        :param text:
        :return:
        """
    @overload
    def ConvertFromString(self, text: str) -> object:
        """

        :param text:
        :return:
        """
    @overload
    def ConvertFromString(self, context: ITypeDescriptorContext, text: str) -> object:
        """

        :param context:
        :param text:
        :return:
        """
    @overload
    def ConvertFromString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, text: str
    ) -> object:
        """

        :param context:
        :param culture:
        :param text:
        :return:
        """
    @overload
    def ConvertTo(self, value: object, destinationType: Type) -> object:
        """

        :param value:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertTo(
        self,
        context: ITypeDescriptorContext,
        culture: CultureInfo,
        value: object,
        destinationType: Type,
    ) -> object:
        """

        :param context:
        :param culture:
        :param value:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertToInvariantString(self, value: object) -> str:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertToInvariantString(self, context: ITypeDescriptorContext, value: object) -> str:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def ConvertToString(self, value: object) -> str:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertToString(self, context: ITypeDescriptorContext, value: object) -> str:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def ConvertToString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> str:
        """

        :param context:
        :param culture:
        :param value:
        :return:
        """
    @overload
    def CreateInstance(self, propertyValues: IDictionary) -> object:
        """

        :param propertyValues:
        :return:
        """
    @overload
    def CreateInstance(
        self, context: ITypeDescriptorContext, propertyValues: IDictionary
    ) -> object:
        """

        :param context:
        :param propertyValues:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetCreateInstanceSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetCreateInstanceSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetProperties(self, value: object) -> PropertyDescriptorCollection:
        """

        :param value:
        :return:
        """
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object
    ) -> PropertyDescriptorCollection:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]
    ) -> PropertyDescriptorCollection:
        """

        :param context:
        :param value:
        :param attributes:
        :return:
        """
    @overload
    def GetPropertiesSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetPropertiesSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValues(self) -> ICollection:
        """

        :return:
        """
    @overload
    def GetStandardValues(
        self, context: ITypeDescriptorContext
    ) -> TypeConverter.StandardValuesCollection:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValuesExclusive(self) -> bool:
        """

        :return:
        """
    @overload
    def GetStandardValuesExclusive(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValuesSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetStandardValuesSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def IsValid(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def IsValid(self, context: ITypeDescriptorContext, value: object) -> bool:
        """

        :param context:
        :param value:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class BindableAttribute(Attribute, _Attribute):
    """"""

    Default: Final[ClassVar[BindableAttribute]] = ...
    """
    
    :return: 
    """
    No: Final[ClassVar[BindableAttribute]] = ...
    """
    
    :return: 
    """
    Yes: Final[ClassVar[BindableAttribute]] = ...
    """
    
    :return: 
    """
    @overload
    def __init__(self, flags: BindableSupport):
        """

        :param flags:
        """
    @overload
    def __init__(self, bindable: bool):
        """

        :param bindable:
        """
    @overload
    def __init__(self, flags: BindableSupport, direction: BindingDirection):
        """

        :param flags:
        :param direction:
        """
    @overload
    def __init__(self, bindable: bool, direction: BindingDirection):
        """

        :param bindable:
        :param direction:
        """
    @property
    def Bindable(self) -> bool:
        """

        :return:
        """
    @property
    def Direction(self) -> BindingDirection:
        """

        :return:
        """
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

class BindableSupport(Enum):
    """"""

    No: BindableSupport = ...
    """"""
    Yes: BindableSupport = ...
    """"""
    Default: BindableSupport = ...
    """"""

class BindingDirection(Enum):
    """"""

    OneWay: BindingDirection = ...
    """"""
    TwoWay: BindingDirection = ...
    """"""

class BindingList(
    Generic[T],
    Collection[T],
    ICollection[T],
    IEnumerable[T],
    IList[T],
    IReadOnlyCollection[T],
    IReadOnlyList[T],
    ICollection,
    IEnumerable,
    IList,
    IBindingList,
    ICancelAddNew,
    IRaiseItemChangedEvents,
):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, list: IList[T]):
        """

        :param list:
        """
    @property
    def AllowEdit(self) -> bool:
        """

        :return:
        """
    @property
    def AllowNew(self) -> bool:
        """

        :return:
        """
    @property
    def AllowRemove(self) -> bool:
        """

        :return:
        """
    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def Count(self) -> int:
        """

        :return:
        """
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
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def IsSorted(self) -> bool:
        """

        :return:
        """
    @property
    def IsSynchronized(self) -> bool:
        """

        :return:
        """
    @property
    def Item(self) -> T:
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
    def Item(self) -> T:
        """

        :return:
        """
    @Item.setter
    def Item(self, value: T) -> None: ...
    @property
    def RaiseListChangedEvents(self) -> bool:
        """

        :return:
        """
    @RaiseListChangedEvents.setter
    def RaiseListChangedEvents(self, value: bool) -> None: ...
    @property
    def RaisesItemChangedEvents(self) -> bool:
        """

        :return:
        """
    @property
    def SortDirection(self) -> ListSortDirection:
        """

        :return:
        """
    @property
    def SortProperty(self) -> PropertyDescriptor:
        """

        :return:
        """
    @property
    def SupportsChangeNotification(self) -> bool:
        """

        :return:
        """
    @property
    def SupportsSearching(self) -> bool:
        """

        :return:
        """
    @property
    def SupportsSorting(self) -> bool:
        """

        :return:
        """
    @property
    def SyncRoot(self) -> object:
        """

        :return:
        """
    @overload
    def Add(self, item: T) -> None:
        """

        :param item:
        """
    @overload
    def Add(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    def AddIndex(self, property: PropertyDescriptor) -> None:
        """

        :param property:
        """
    def AddNew(self) -> object:
        """

        :return:
        """
    def ApplySort(self, property: PropertyDescriptor, direction: ListSortDirection) -> None:
        """

        :param property:
        :param direction:
        """
    def CancelNew(self, itemIndex: int) -> None:
        """

        :param itemIndex:
        """
    @overload
    def Clear(self) -> None:
        """"""
    @overload
    def Clear(self) -> None:
        """"""
    @overload
    def Contains(self, item: T) -> bool:
        """

        :param item:
        :return:
        """
    @overload
    def Contains(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    @overload
    def CopyTo(self, array: Array[T], arrayIndex: int) -> None:
        """"""
    def EndNew(self, itemIndex: int) -> None:
        """

        :param itemIndex:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def Find(self, property: PropertyDescriptor, key: object) -> int:
        """

        :param property:
        :param key:
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
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def IndexOf(self, item: T) -> int:
        """

        :param item:
        :return:
        """
    @overload
    def IndexOf(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def Insert(self, index: int, item: T) -> None:
        """

        :param index:
        :param item:
        """
    @overload
    def Insert(self, index: int, value: object) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def Remove(self, item: T) -> bool:
        """

        :param item:
        :return:
        """
    @overload
    def Remove(self, value: object) -> None:
        """

        :param value:
        """
    @overload
    def RemoveAt(self, index: int) -> None:
        """

        :param index:
        """
    @overload
    def RemoveAt(self, index: int) -> None:
        """

        :param index:
        """
    def RemoveIndex(self, property: PropertyDescriptor) -> None:
        """

        :param property:
        """
    def RemoveSort(self) -> None:
        """"""
    def ResetBindings(self) -> None:
        """"""
    def ResetItem(self, position: int) -> None:
        """

        :param position:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def __contains__(self, value: T) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def __contains__(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def __getitem__(self, index: int) -> T:
        """

        :param index:
        :return:
        """
    @overload
    def __getitem__(self, index: int) -> object:
        """

        :param index:
        :return:
        """
    @overload
    def __getitem__(self, index: int) -> T:
        """

        :param index:
        :return:
        """
    @overload
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[T]:
        """

        :return:
        """
    @overload
    def __len__(self) -> int:
        """

        :return:
        """
    @overload
    def __len__(self) -> int:
        """

        :return:
        """
    @overload
    def __setitem__(self, index: int, value: T) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def __setitem__(self, index: int, value: object) -> None:
        """

        :param index:
        :param value:
        """
    AddingNew: EventType[AddingNewEventHandler] = ...
    """"""
    ListChanged: EventType[ListChangedEventHandler] = ...
    """"""

class BooleanConverter(TypeConverter):
    """"""

    def __init__(self):
        """"""
    @overload
    def CanConvertFrom(self, sourceType: Type) -> bool:
        """

        :param sourceType:
        :return:
        """
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool:
        """

        :param context:
        :param sourceType:
        :return:
        """
    @overload
    def CanConvertTo(self, destinationType: Type) -> bool:
        """

        :param destinationType:
        :return:
        """
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, destinationType: Type) -> bool:
        """

        :param context:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertFrom(self, value: object) -> object:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertFrom(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> object:
        """

        :param context:
        :param culture:
        :param value:
        :return:
        """
    @overload
    def ConvertFromInvariantString(self, text: str) -> object:
        """

        :param text:
        :return:
        """
    @overload
    def ConvertFromInvariantString(self, context: ITypeDescriptorContext, text: str) -> object:
        """

        :param context:
        :param text:
        :return:
        """
    @overload
    def ConvertFromString(self, text: str) -> object:
        """

        :param text:
        :return:
        """
    @overload
    def ConvertFromString(self, context: ITypeDescriptorContext, text: str) -> object:
        """

        :param context:
        :param text:
        :return:
        """
    @overload
    def ConvertFromString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, text: str
    ) -> object:
        """

        :param context:
        :param culture:
        :param text:
        :return:
        """
    @overload
    def ConvertTo(self, value: object, destinationType: Type) -> object:
        """

        :param value:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertTo(
        self,
        context: ITypeDescriptorContext,
        culture: CultureInfo,
        value: object,
        destinationType: Type,
    ) -> object:
        """

        :param context:
        :param culture:
        :param value:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertToInvariantString(self, value: object) -> str:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertToInvariantString(self, context: ITypeDescriptorContext, value: object) -> str:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def ConvertToString(self, value: object) -> str:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertToString(self, context: ITypeDescriptorContext, value: object) -> str:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def ConvertToString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> str:
        """

        :param context:
        :param culture:
        :param value:
        :return:
        """
    @overload
    def CreateInstance(self, propertyValues: IDictionary) -> object:
        """

        :param propertyValues:
        :return:
        """
    @overload
    def CreateInstance(
        self, context: ITypeDescriptorContext, propertyValues: IDictionary
    ) -> object:
        """

        :param context:
        :param propertyValues:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetCreateInstanceSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetCreateInstanceSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetProperties(self, value: object) -> PropertyDescriptorCollection:
        """

        :param value:
        :return:
        """
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object
    ) -> PropertyDescriptorCollection:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]
    ) -> PropertyDescriptorCollection:
        """

        :param context:
        :param value:
        :param attributes:
        :return:
        """
    @overload
    def GetPropertiesSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetPropertiesSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValues(self) -> ICollection:
        """

        :return:
        """
    @overload
    def GetStandardValues(
        self, context: ITypeDescriptorContext
    ) -> TypeConverter.StandardValuesCollection:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValuesExclusive(self) -> bool:
        """

        :return:
        """
    @overload
    def GetStandardValuesExclusive(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValuesSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetStandardValuesSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def IsValid(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def IsValid(self, context: ITypeDescriptorContext, value: object) -> bool:
        """

        :param context:
        :param value:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class BrowsableAttribute(Attribute, _Attribute):
    """"""

    Default: Final[ClassVar[BrowsableAttribute]] = ...
    """
    
    :return: 
    """
    No: Final[ClassVar[BrowsableAttribute]] = ...
    """
    
    :return: 
    """
    Yes: Final[ClassVar[BrowsableAttribute]] = ...
    """
    
    :return: 
    """
    def __init__(self, browsable: bool):
        """

        :param browsable:
        """
    @property
    def Browsable(self) -> bool:
        """

        :return:
        """
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

class ByteConverter(BaseNumberConverter):
    """"""

    def __init__(self):
        """"""
    @overload
    def CanConvertFrom(self, sourceType: Type) -> bool:
        """

        :param sourceType:
        :return:
        """
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool:
        """

        :param context:
        :param sourceType:
        :return:
        """
    @overload
    def CanConvertTo(self, destinationType: Type) -> bool:
        """

        :param destinationType:
        :return:
        """
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, destinationType: Type) -> bool:
        """

        :param context:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertFrom(self, value: object) -> object:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertFrom(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> object:
        """

        :param context:
        :param culture:
        :param value:
        :return:
        """
    @overload
    def ConvertFromInvariantString(self, text: str) -> object:
        """

        :param text:
        :return:
        """
    @overload
    def ConvertFromInvariantString(self, context: ITypeDescriptorContext, text: str) -> object:
        """

        :param context:
        :param text:
        :return:
        """
    @overload
    def ConvertFromString(self, text: str) -> object:
        """

        :param text:
        :return:
        """
    @overload
    def ConvertFromString(self, context: ITypeDescriptorContext, text: str) -> object:
        """

        :param context:
        :param text:
        :return:
        """
    @overload
    def ConvertFromString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, text: str
    ) -> object:
        """

        :param context:
        :param culture:
        :param text:
        :return:
        """
    @overload
    def ConvertTo(self, value: object, destinationType: Type) -> object:
        """

        :param value:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertTo(
        self,
        context: ITypeDescriptorContext,
        culture: CultureInfo,
        value: object,
        destinationType: Type,
    ) -> object:
        """

        :param context:
        :param culture:
        :param value:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertToInvariantString(self, value: object) -> str:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertToInvariantString(self, context: ITypeDescriptorContext, value: object) -> str:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def ConvertToString(self, value: object) -> str:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertToString(self, context: ITypeDescriptorContext, value: object) -> str:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def ConvertToString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> str:
        """

        :param context:
        :param culture:
        :param value:
        :return:
        """
    @overload
    def CreateInstance(self, propertyValues: IDictionary) -> object:
        """

        :param propertyValues:
        :return:
        """
    @overload
    def CreateInstance(
        self, context: ITypeDescriptorContext, propertyValues: IDictionary
    ) -> object:
        """

        :param context:
        :param propertyValues:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetCreateInstanceSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetCreateInstanceSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetProperties(self, value: object) -> PropertyDescriptorCollection:
        """

        :param value:
        :return:
        """
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object
    ) -> PropertyDescriptorCollection:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]
    ) -> PropertyDescriptorCollection:
        """

        :param context:
        :param value:
        :param attributes:
        :return:
        """
    @overload
    def GetPropertiesSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetPropertiesSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValues(self) -> ICollection:
        """

        :return:
        """
    @overload
    def GetStandardValues(
        self, context: ITypeDescriptorContext
    ) -> TypeConverter.StandardValuesCollection:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValuesExclusive(self) -> bool:
        """

        :return:
        """
    @overload
    def GetStandardValuesExclusive(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValuesSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetStandardValuesSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def IsValid(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def IsValid(self, context: ITypeDescriptorContext, value: object) -> bool:
        """

        :param context:
        :param value:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CancelEventArgs(EventArgs):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, cancel: bool):
        """

        :param cancel:
        """
    @property
    def Cancel(self) -> bool:
        """

        :return:
        """
    @Cancel.setter
    def Cancel(self, value: bool) -> None: ...
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

CancelEventHandler: Callable[[object, CancelEventArgs], None] = ...
"""

:param sender: 
:param e: 
"""

class CategoryAttribute(Attribute, _Attribute):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, category: str):
        """

        :param category:
        """
    @classmethod
    @property
    def Action(cls) -> CategoryAttribute:
        """

        :return:
        """
    @classmethod
    @property
    def Appearance(cls) -> CategoryAttribute:
        """

        :return:
        """
    @classmethod
    @property
    def Asynchronous(cls) -> CategoryAttribute:
        """

        :return:
        """
    @classmethod
    @property
    def Behavior(cls) -> CategoryAttribute:
        """

        :return:
        """
    @property
    def Category(self) -> str:
        """

        :return:
        """
    @classmethod
    @property
    def Data(cls) -> CategoryAttribute:
        """

        :return:
        """
    @classmethod
    @property
    def Default(cls) -> CategoryAttribute:
        """

        :return:
        """
    @classmethod
    @property
    def Design(cls) -> CategoryAttribute:
        """

        :return:
        """
    @classmethod
    @property
    def DragDrop(cls) -> CategoryAttribute:
        """

        :return:
        """
    @classmethod
    @property
    def Focus(cls) -> CategoryAttribute:
        """

        :return:
        """
    @classmethod
    @property
    def Format(cls) -> CategoryAttribute:
        """

        :return:
        """
    @classmethod
    @property
    def Key(cls) -> CategoryAttribute:
        """

        :return:
        """
    @classmethod
    @property
    def Layout(cls) -> CategoryAttribute:
        """

        :return:
        """
    @classmethod
    @property
    def Mouse(cls) -> CategoryAttribute:
        """

        :return:
        """
    @property
    def TypeId(self) -> object:
        """

        :return:
        """
    @classmethod
    @property
    def WindowStyle(cls) -> CategoryAttribute:
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

class CharConverter(TypeConverter):
    """"""

    def __init__(self):
        """"""
    @overload
    def CanConvertFrom(self, sourceType: Type) -> bool:
        """

        :param sourceType:
        :return:
        """
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool:
        """

        :param context:
        :param sourceType:
        :return:
        """
    @overload
    def CanConvertTo(self, destinationType: Type) -> bool:
        """

        :param destinationType:
        :return:
        """
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, destinationType: Type) -> bool:
        """

        :param context:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertFrom(self, value: object) -> object:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertFrom(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> object:
        """

        :param context:
        :param culture:
        :param value:
        :return:
        """
    @overload
    def ConvertFromInvariantString(self, text: str) -> object:
        """

        :param text:
        :return:
        """
    @overload
    def ConvertFromInvariantString(self, context: ITypeDescriptorContext, text: str) -> object:
        """

        :param context:
        :param text:
        :return:
        """
    @overload
    def ConvertFromString(self, text: str) -> object:
        """

        :param text:
        :return:
        """
    @overload
    def ConvertFromString(self, context: ITypeDescriptorContext, text: str) -> object:
        """

        :param context:
        :param text:
        :return:
        """
    @overload
    def ConvertFromString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, text: str
    ) -> object:
        """

        :param context:
        :param culture:
        :param text:
        :return:
        """
    @overload
    def ConvertTo(self, value: object, destinationType: Type) -> object:
        """

        :param value:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertTo(
        self,
        context: ITypeDescriptorContext,
        culture: CultureInfo,
        value: object,
        destinationType: Type,
    ) -> object:
        """

        :param context:
        :param culture:
        :param value:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertToInvariantString(self, value: object) -> str:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertToInvariantString(self, context: ITypeDescriptorContext, value: object) -> str:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def ConvertToString(self, value: object) -> str:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertToString(self, context: ITypeDescriptorContext, value: object) -> str:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def ConvertToString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> str:
        """

        :param context:
        :param culture:
        :param value:
        :return:
        """
    @overload
    def CreateInstance(self, propertyValues: IDictionary) -> object:
        """

        :param propertyValues:
        :return:
        """
    @overload
    def CreateInstance(
        self, context: ITypeDescriptorContext, propertyValues: IDictionary
    ) -> object:
        """

        :param context:
        :param propertyValues:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetCreateInstanceSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetCreateInstanceSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetProperties(self, value: object) -> PropertyDescriptorCollection:
        """

        :param value:
        :return:
        """
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object
    ) -> PropertyDescriptorCollection:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]
    ) -> PropertyDescriptorCollection:
        """

        :param context:
        :param value:
        :param attributes:
        :return:
        """
    @overload
    def GetPropertiesSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetPropertiesSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValues(self) -> ICollection:
        """

        :return:
        """
    @overload
    def GetStandardValues(
        self, context: ITypeDescriptorContext
    ) -> TypeConverter.StandardValuesCollection:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValuesExclusive(self) -> bool:
        """

        :return:
        """
    @overload
    def GetStandardValuesExclusive(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValuesSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetStandardValuesSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def IsValid(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def IsValid(self, context: ITypeDescriptorContext, value: object) -> bool:
        """

        :param context:
        :param value:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CollectionChangeAction(Enum):
    """"""

    Add: CollectionChangeAction = ...
    """"""
    Remove: CollectionChangeAction = ...
    """"""
    Refresh: CollectionChangeAction = ...
    """"""

class CollectionChangeEventArgs(EventArgs):
    """"""

    def __init__(self, action: CollectionChangeAction, element: object):
        """

        :param action:
        :param element:
        """
    @property
    def Action(self) -> CollectionChangeAction:
        """

        :return:
        """
    @property
    def Element(self) -> object:
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

CollectionChangeEventHandler: Callable[[object, CollectionChangeEventArgs], None] = ...
"""

:param sender: 
:param e: 
"""

class CollectionConverter(TypeConverter):
    """"""

    def __init__(self):
        """"""
    @overload
    def CanConvertFrom(self, sourceType: Type) -> bool:
        """

        :param sourceType:
        :return:
        """
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool:
        """

        :param context:
        :param sourceType:
        :return:
        """
    @overload
    def CanConvertTo(self, destinationType: Type) -> bool:
        """

        :param destinationType:
        :return:
        """
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, destinationType: Type) -> bool:
        """

        :param context:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertFrom(self, value: object) -> object:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertFrom(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> object:
        """

        :param context:
        :param culture:
        :param value:
        :return:
        """
    @overload
    def ConvertFromInvariantString(self, text: str) -> object:
        """

        :param text:
        :return:
        """
    @overload
    def ConvertFromInvariantString(self, context: ITypeDescriptorContext, text: str) -> object:
        """

        :param context:
        :param text:
        :return:
        """
    @overload
    def ConvertFromString(self, text: str) -> object:
        """

        :param text:
        :return:
        """
    @overload
    def ConvertFromString(self, context: ITypeDescriptorContext, text: str) -> object:
        """

        :param context:
        :param text:
        :return:
        """
    @overload
    def ConvertFromString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, text: str
    ) -> object:
        """

        :param context:
        :param culture:
        :param text:
        :return:
        """
    @overload
    def ConvertTo(self, value: object, destinationType: Type) -> object:
        """

        :param value:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertTo(
        self,
        context: ITypeDescriptorContext,
        culture: CultureInfo,
        value: object,
        destinationType: Type,
    ) -> object:
        """

        :param context:
        :param culture:
        :param value:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertToInvariantString(self, value: object) -> str:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertToInvariantString(self, context: ITypeDescriptorContext, value: object) -> str:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def ConvertToString(self, value: object) -> str:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertToString(self, context: ITypeDescriptorContext, value: object) -> str:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def ConvertToString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> str:
        """

        :param context:
        :param culture:
        :param value:
        :return:
        """
    @overload
    def CreateInstance(self, propertyValues: IDictionary) -> object:
        """

        :param propertyValues:
        :return:
        """
    @overload
    def CreateInstance(
        self, context: ITypeDescriptorContext, propertyValues: IDictionary
    ) -> object:
        """

        :param context:
        :param propertyValues:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetCreateInstanceSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetCreateInstanceSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetProperties(self, value: object) -> PropertyDescriptorCollection:
        """

        :param value:
        :return:
        """
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object
    ) -> PropertyDescriptorCollection:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]
    ) -> PropertyDescriptorCollection:
        """

        :param context:
        :param value:
        :param attributes:
        :return:
        """
    @overload
    def GetPropertiesSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetPropertiesSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValues(self) -> ICollection:
        """

        :return:
        """
    @overload
    def GetStandardValues(
        self, context: ITypeDescriptorContext
    ) -> TypeConverter.StandardValuesCollection:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValuesExclusive(self) -> bool:
        """

        :return:
        """
    @overload
    def GetStandardValuesExclusive(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValuesSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetStandardValuesSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def IsValid(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def IsValid(self, context: ITypeDescriptorContext, value: object) -> bool:
        """

        :param context:
        :param value:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CompModSwitches(ABC, Object):
    """"""

    @classmethod
    @property
    def CommonDesignerServices(cls) -> BooleanSwitch:
        """

        :return:
        """
    @classmethod
    @property
    def EventLog(cls) -> TraceSwitch:
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

class ComplexBindingPropertiesAttribute(Attribute, _Attribute):
    """"""

    Default: Final[ClassVar[ComplexBindingPropertiesAttribute]] = ...
    """
    
    :return: 
    """
    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, dataSource: str):
        """

        :param dataSource:
        """
    @overload
    def __init__(self, dataSource: str, dataMember: str):
        """

        :param dataSource:
        :param dataMember:
        """
    @property
    def DataMember(self) -> str:
        """

        :return:
        """
    @property
    def DataSource(self) -> str:
        """

        :return:
        """
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

class Component(MarshalByRefObject, IComponent, IDisposable):
    """"""

    def __init__(self):
        """"""
    @property
    def Container(self) -> IContainer:
        """

        :return:
        """
    @property
    def Site(self) -> ISite:
        """

        :return:
        """
    @Site.setter
    def Site(self, value: ISite) -> None: ...
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """

        :param requestedType:
        :return:
        """
    def Dispose(self) -> None:
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
    def GetLifetimeService(self) -> object:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def InitializeLifetimeService(self) -> object:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    Disposed: EventType[EventHandler] = ...
    """"""

class ComponentCollection(ReadOnlyCollectionBase, ICollection, IEnumerable):
    """"""

    def __init__(self, components: Array[IComponent]):
        """

        :param components:
        """
    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def IsSynchronized(self) -> bool:
        """

        :return:
        """
    @property
    def Item(self) -> IComponent:
        """

        :return:
        """
    @property
    def SyncRoot(self) -> object:
        """

        :return:
        """
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    @overload
    def CopyTo(self, array: Array[IComponent], index: int) -> None:
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
    def GetType(self) -> Type:
        """

        :return:
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
    @overload
    def __getitem__(self, index: int) -> IComponent:
        """

        :param index:
        :return:
        """
    @overload
    def __getitem__(self, name: str) -> IComponent:
        """

        :param name:
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

class ComponentConverter(ReferenceConverter):
    """"""

    def __init__(self, type: Type):
        """

        :param type:
        """
    @overload
    def CanConvertFrom(self, sourceType: Type) -> bool:
        """

        :param sourceType:
        :return:
        """
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool:
        """

        :param context:
        :param sourceType:
        :return:
        """
    @overload
    def CanConvertTo(self, destinationType: Type) -> bool:
        """

        :param destinationType:
        :return:
        """
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, destinationType: Type) -> bool:
        """

        :param context:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertFrom(self, value: object) -> object:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertFrom(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> object:
        """

        :param context:
        :param culture:
        :param value:
        :return:
        """
    @overload
    def ConvertFromInvariantString(self, text: str) -> object:
        """

        :param text:
        :return:
        """
    @overload
    def ConvertFromInvariantString(self, context: ITypeDescriptorContext, text: str) -> object:
        """

        :param context:
        :param text:
        :return:
        """
    @overload
    def ConvertFromString(self, text: str) -> object:
        """

        :param text:
        :return:
        """
    @overload
    def ConvertFromString(self, context: ITypeDescriptorContext, text: str) -> object:
        """

        :param context:
        :param text:
        :return:
        """
    @overload
    def ConvertFromString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, text: str
    ) -> object:
        """

        :param context:
        :param culture:
        :param text:
        :return:
        """
    @overload
    def ConvertTo(self, value: object, destinationType: Type) -> object:
        """

        :param value:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertTo(
        self,
        context: ITypeDescriptorContext,
        culture: CultureInfo,
        value: object,
        destinationType: Type,
    ) -> object:
        """

        :param context:
        :param culture:
        :param value:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertToInvariantString(self, value: object) -> str:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertToInvariantString(self, context: ITypeDescriptorContext, value: object) -> str:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def ConvertToString(self, value: object) -> str:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertToString(self, context: ITypeDescriptorContext, value: object) -> str:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def ConvertToString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> str:
        """

        :param context:
        :param culture:
        :param value:
        :return:
        """
    @overload
    def CreateInstance(self, propertyValues: IDictionary) -> object:
        """

        :param propertyValues:
        :return:
        """
    @overload
    def CreateInstance(
        self, context: ITypeDescriptorContext, propertyValues: IDictionary
    ) -> object:
        """

        :param context:
        :param propertyValues:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetCreateInstanceSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetCreateInstanceSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetProperties(self, value: object) -> PropertyDescriptorCollection:
        """

        :param value:
        :return:
        """
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object
    ) -> PropertyDescriptorCollection:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]
    ) -> PropertyDescriptorCollection:
        """

        :param context:
        :param value:
        :param attributes:
        :return:
        """
    @overload
    def GetPropertiesSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetPropertiesSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValues(self) -> ICollection:
        """

        :return:
        """
    @overload
    def GetStandardValues(
        self, context: ITypeDescriptorContext
    ) -> TypeConverter.StandardValuesCollection:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValuesExclusive(self) -> bool:
        """

        :return:
        """
    @overload
    def GetStandardValuesExclusive(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValuesSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetStandardValuesSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def IsValid(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def IsValid(self, context: ITypeDescriptorContext, value: object) -> bool:
        """

        :param context:
        :param value:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class ComponentEditor(ABC, Object):
    """"""

    @overload
    def EditComponent(self, component: object) -> bool:
        """

        :param component:
        :return:
        """
    @overload
    def EditComponent(self, context: ITypeDescriptorContext, component: object) -> bool:
        """

        :param context:
        :param component:
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

class ComponentResourceManager(ResourceManager):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, t: Type):
        """

        :param t:
        """
    @property
    def BaseName(self) -> str:
        """

        :return:
        """
    @property
    def IgnoreCase(self) -> bool:
        """

        :return:
        """
    @IgnoreCase.setter
    def IgnoreCase(self, value: bool) -> None: ...
    @property
    def ResourceSetType(self) -> Type:
        """

        :return:
        """
    @overload
    def ApplyResources(self, value: object, objectName: str) -> None:
        """

        :param value:
        :param objectName:
        """
    @overload
    def ApplyResources(self, value: object, objectName: str, culture: CultureInfo) -> None:
        """

        :param value:
        :param objectName:
        :param culture:
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
    @overload
    def GetObject(self, name: str) -> object:
        """

        :param name:
        :return:
        """
    @overload
    def GetObject(self, name: str, culture: CultureInfo) -> object:
        """

        :param name:
        :param culture:
        :return:
        """
    def GetResourceSet(
        self, culture: CultureInfo, createIfNotExists: bool, tryParents: bool
    ) -> ResourceSet:
        """

        :param culture:
        :param createIfNotExists:
        :param tryParents:
        :return:
        """
    @overload
    def GetStream(self, name: str) -> UnmanagedMemoryStream:
        """

        :param name:
        :return:
        """
    @overload
    def GetStream(self, name: str, culture: CultureInfo) -> UnmanagedMemoryStream:
        """

        :param name:
        :param culture:
        :return:
        """
    @overload
    def GetString(self, name: str) -> str:
        """

        :param name:
        :return:
        """
    @overload
    def GetString(self, name: str, culture: CultureInfo) -> str:
        """

        :param name:
        :param culture:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ReleaseAllResources(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class Container(Object, IContainer, IDisposable):
    """"""

    def __init__(self):
        """"""
    @property
    def Components(self) -> ComponentCollection:
        """

        :return:
        """
    @overload
    def Add(self, component: IComponent) -> None:
        """

        :param component:
        """
    @overload
    def Add(self, component: IComponent, name: str) -> None:
        """

        :param component:
        :param name:
        """
    def Dispose(self) -> None:
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
    def Remove(self, component: IComponent) -> None:
        """

        :param component:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class ContainerFilterService(ABC, Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def FilterComponents(self, components: ComponentCollection) -> ComponentCollection:
        """

        :param components:
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

class CultureInfoConverter(TypeConverter):
    """"""

    def __init__(self):
        """"""
    @overload
    def CanConvertFrom(self, sourceType: Type) -> bool:
        """

        :param sourceType:
        :return:
        """
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool:
        """

        :param context:
        :param sourceType:
        :return:
        """
    @overload
    def CanConvertTo(self, destinationType: Type) -> bool:
        """

        :param destinationType:
        :return:
        """
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, destinationType: Type) -> bool:
        """

        :param context:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertFrom(self, value: object) -> object:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertFrom(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> object:
        """

        :param context:
        :param culture:
        :param value:
        :return:
        """
    @overload
    def ConvertFromInvariantString(self, text: str) -> object:
        """

        :param text:
        :return:
        """
    @overload
    def ConvertFromInvariantString(self, context: ITypeDescriptorContext, text: str) -> object:
        """

        :param context:
        :param text:
        :return:
        """
    @overload
    def ConvertFromString(self, text: str) -> object:
        """

        :param text:
        :return:
        """
    @overload
    def ConvertFromString(self, context: ITypeDescriptorContext, text: str) -> object:
        """

        :param context:
        :param text:
        :return:
        """
    @overload
    def ConvertFromString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, text: str
    ) -> object:
        """

        :param context:
        :param culture:
        :param text:
        :return:
        """
    @overload
    def ConvertTo(self, value: object, destinationType: Type) -> object:
        """

        :param value:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertTo(
        self,
        context: ITypeDescriptorContext,
        culture: CultureInfo,
        value: object,
        destinationType: Type,
    ) -> object:
        """

        :param context:
        :param culture:
        :param value:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertToInvariantString(self, value: object) -> str:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertToInvariantString(self, context: ITypeDescriptorContext, value: object) -> str:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def ConvertToString(self, value: object) -> str:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertToString(self, context: ITypeDescriptorContext, value: object) -> str:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def ConvertToString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> str:
        """

        :param context:
        :param culture:
        :param value:
        :return:
        """
    @overload
    def CreateInstance(self, propertyValues: IDictionary) -> object:
        """

        :param propertyValues:
        :return:
        """
    @overload
    def CreateInstance(
        self, context: ITypeDescriptorContext, propertyValues: IDictionary
    ) -> object:
        """

        :param context:
        :param propertyValues:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetCreateInstanceSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetCreateInstanceSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetProperties(self, value: object) -> PropertyDescriptorCollection:
        """

        :param value:
        :return:
        """
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object
    ) -> PropertyDescriptorCollection:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]
    ) -> PropertyDescriptorCollection:
        """

        :param context:
        :param value:
        :param attributes:
        :return:
        """
    @overload
    def GetPropertiesSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetPropertiesSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValues(self) -> ICollection:
        """

        :return:
        """
    @overload
    def GetStandardValues(
        self, context: ITypeDescriptorContext
    ) -> TypeConverter.StandardValuesCollection:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValuesExclusive(self) -> bool:
        """

        :return:
        """
    @overload
    def GetStandardValuesExclusive(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValuesSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetStandardValuesSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def IsValid(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def IsValid(self, context: ITypeDescriptorContext, value: object) -> bool:
        """

        :param context:
        :param value:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CustomTypeDescriptor(ABC, Object, ICustomTypeDescriptor):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetAttributes(self) -> AttributeCollection:
        """

        :return:
        """
    def GetClassName(self) -> str:
        """

        :return:
        """
    def GetComponentName(self) -> str:
        """

        :return:
        """
    def GetConverter(self) -> TypeConverter:
        """

        :return:
        """
    def GetDefaultEvent(self) -> EventDescriptor:
        """

        :return:
        """
    def GetDefaultProperty(self) -> PropertyDescriptor:
        """

        :return:
        """
    def GetEditor(self, editorBaseType: Type) -> object:
        """

        :param editorBaseType:
        :return:
        """
    @overload
    def GetEvents(self) -> EventDescriptorCollection:
        """

        :return:
        """
    @overload
    def GetEvents(self, attributes: Array[Attribute]) -> EventDescriptorCollection:
        """

        :param attributes:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetProperties(self) -> PropertyDescriptorCollection:
        """

        :return:
        """
    @overload
    def GetProperties(self, attributes: Array[Attribute]) -> PropertyDescriptorCollection:
        """

        :param attributes:
        :return:
        """
    def GetPropertyOwner(self, pd: PropertyDescriptor) -> object:
        """

        :param pd:
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

class DataErrorsChangedEventArgs(EventArgs):
    """"""

    def __init__(self, propertyName: str):
        """

        :param propertyName:
        """
    @property
    def PropertyName(self) -> str:
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

class DataObjectAttribute(Attribute, _Attribute):
    """"""

    DataObject: Final[ClassVar[DataObjectAttribute]] = ...
    """
    
    :return: 
    """
    Default: Final[ClassVar[DataObjectAttribute]] = ...
    """
    
    :return: 
    """
    NonDataObject: Final[ClassVar[DataObjectAttribute]] = ...
    """
    
    :return: 
    """
    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, isDataObject: bool):
        """

        :param isDataObject:
        """
    @property
    def IsDataObject(self) -> bool:
        """

        :return:
        """
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

class DataObjectFieldAttribute(Attribute, _Attribute):
    """"""

    @overload
    def __init__(self, primaryKey: bool):
        """

        :param primaryKey:
        """
    @overload
    def __init__(self, primaryKey: bool, isIdentity: bool):
        """

        :param primaryKey:
        :param isIdentity:
        """
    @overload
    def __init__(self, primaryKey: bool, isIdentity: bool, isNullable: bool):
        """

        :param primaryKey:
        :param isIdentity:
        :param isNullable:
        """
    @overload
    def __init__(self, primaryKey: bool, isIdentity: bool, isNullable: bool, length: int):
        """

        :param primaryKey:
        :param isIdentity:
        :param isNullable:
        :param length:
        """
    @property
    def IsIdentity(self) -> bool:
        """

        :return:
        """
    @property
    def IsNullable(self) -> bool:
        """

        :return:
        """
    @property
    def Length(self) -> int:
        """

        :return:
        """
    @property
    def PrimaryKey(self) -> bool:
        """

        :return:
        """
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

class DataObjectMethodAttribute(Attribute, _Attribute):
    """"""

    @overload
    def __init__(self, methodType: DataObjectMethodType):
        """

        :param methodType:
        """
    @overload
    def __init__(self, methodType: DataObjectMethodType, isDefault: bool):
        """

        :param methodType:
        :param isDefault:
        """
    @property
    def IsDefault(self) -> bool:
        """

        :return:
        """
    @property
    def MethodType(self) -> DataObjectMethodType:
        """

        :return:
        """
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

class DataObjectMethodType(Enum):
    """"""

    Fill: DataObjectMethodType = ...
    """"""
    Select: DataObjectMethodType = ...
    """"""
    Update: DataObjectMethodType = ...
    """"""
    Insert: DataObjectMethodType = ...
    """"""
    Delete: DataObjectMethodType = ...
    """"""

class DateTimeConverter(TypeConverter):
    """"""

    def __init__(self):
        """"""
    @overload
    def CanConvertFrom(self, sourceType: Type) -> bool:
        """

        :param sourceType:
        :return:
        """
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool:
        """

        :param context:
        :param sourceType:
        :return:
        """
    @overload
    def CanConvertTo(self, destinationType: Type) -> bool:
        """

        :param destinationType:
        :return:
        """
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, destinationType: Type) -> bool:
        """

        :param context:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertFrom(self, value: object) -> object:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertFrom(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> object:
        """

        :param context:
        :param culture:
        :param value:
        :return:
        """
    @overload
    def ConvertFromInvariantString(self, text: str) -> object:
        """

        :param text:
        :return:
        """
    @overload
    def ConvertFromInvariantString(self, context: ITypeDescriptorContext, text: str) -> object:
        """

        :param context:
        :param text:
        :return:
        """
    @overload
    def ConvertFromString(self, text: str) -> object:
        """

        :param text:
        :return:
        """
    @overload
    def ConvertFromString(self, context: ITypeDescriptorContext, text: str) -> object:
        """

        :param context:
        :param text:
        :return:
        """
    @overload
    def ConvertFromString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, text: str
    ) -> object:
        """

        :param context:
        :param culture:
        :param text:
        :return:
        """
    @overload
    def ConvertTo(self, value: object, destinationType: Type) -> object:
        """

        :param value:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertTo(
        self,
        context: ITypeDescriptorContext,
        culture: CultureInfo,
        value: object,
        destinationType: Type,
    ) -> object:
        """

        :param context:
        :param culture:
        :param value:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertToInvariantString(self, value: object) -> str:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertToInvariantString(self, context: ITypeDescriptorContext, value: object) -> str:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def ConvertToString(self, value: object) -> str:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertToString(self, context: ITypeDescriptorContext, value: object) -> str:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def ConvertToString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> str:
        """

        :param context:
        :param culture:
        :param value:
        :return:
        """
    @overload
    def CreateInstance(self, propertyValues: IDictionary) -> object:
        """

        :param propertyValues:
        :return:
        """
    @overload
    def CreateInstance(
        self, context: ITypeDescriptorContext, propertyValues: IDictionary
    ) -> object:
        """

        :param context:
        :param propertyValues:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetCreateInstanceSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetCreateInstanceSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetProperties(self, value: object) -> PropertyDescriptorCollection:
        """

        :param value:
        :return:
        """
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object
    ) -> PropertyDescriptorCollection:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]
    ) -> PropertyDescriptorCollection:
        """

        :param context:
        :param value:
        :param attributes:
        :return:
        """
    @overload
    def GetPropertiesSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetPropertiesSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValues(self) -> ICollection:
        """

        :return:
        """
    @overload
    def GetStandardValues(
        self, context: ITypeDescriptorContext
    ) -> TypeConverter.StandardValuesCollection:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValuesExclusive(self) -> bool:
        """

        :return:
        """
    @overload
    def GetStandardValuesExclusive(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValuesSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetStandardValuesSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def IsValid(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def IsValid(self, context: ITypeDescriptorContext, value: object) -> bool:
        """

        :param context:
        :param value:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class DateTimeOffsetConverter(TypeConverter):
    """"""

    def __init__(self):
        """"""
    @overload
    def CanConvertFrom(self, sourceType: Type) -> bool:
        """

        :param sourceType:
        :return:
        """
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool:
        """

        :param context:
        :param sourceType:
        :return:
        """
    @overload
    def CanConvertTo(self, destinationType: Type) -> bool:
        """

        :param destinationType:
        :return:
        """
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, destinationType: Type) -> bool:
        """

        :param context:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertFrom(self, value: object) -> object:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertFrom(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> object:
        """

        :param context:
        :param culture:
        :param value:
        :return:
        """
    @overload
    def ConvertFromInvariantString(self, text: str) -> object:
        """

        :param text:
        :return:
        """
    @overload
    def ConvertFromInvariantString(self, context: ITypeDescriptorContext, text: str) -> object:
        """

        :param context:
        :param text:
        :return:
        """
    @overload
    def ConvertFromString(self, text: str) -> object:
        """

        :param text:
        :return:
        """
    @overload
    def ConvertFromString(self, context: ITypeDescriptorContext, text: str) -> object:
        """

        :param context:
        :param text:
        :return:
        """
    @overload
    def ConvertFromString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, text: str
    ) -> object:
        """

        :param context:
        :param culture:
        :param text:
        :return:
        """
    @overload
    def ConvertTo(self, value: object, destinationType: Type) -> object:
        """

        :param value:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertTo(
        self,
        context: ITypeDescriptorContext,
        culture: CultureInfo,
        value: object,
        destinationType: Type,
    ) -> object:
        """

        :param context:
        :param culture:
        :param value:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertToInvariantString(self, value: object) -> str:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertToInvariantString(self, context: ITypeDescriptorContext, value: object) -> str:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def ConvertToString(self, value: object) -> str:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertToString(self, context: ITypeDescriptorContext, value: object) -> str:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def ConvertToString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> str:
        """

        :param context:
        :param culture:
        :param value:
        :return:
        """
    @overload
    def CreateInstance(self, propertyValues: IDictionary) -> object:
        """

        :param propertyValues:
        :return:
        """
    @overload
    def CreateInstance(
        self, context: ITypeDescriptorContext, propertyValues: IDictionary
    ) -> object:
        """

        :param context:
        :param propertyValues:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetCreateInstanceSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetCreateInstanceSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetProperties(self, value: object) -> PropertyDescriptorCollection:
        """

        :param value:
        :return:
        """
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object
    ) -> PropertyDescriptorCollection:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]
    ) -> PropertyDescriptorCollection:
        """

        :param context:
        :param value:
        :param attributes:
        :return:
        """
    @overload
    def GetPropertiesSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetPropertiesSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValues(self) -> ICollection:
        """

        :return:
        """
    @overload
    def GetStandardValues(
        self, context: ITypeDescriptorContext
    ) -> TypeConverter.StandardValuesCollection:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValuesExclusive(self) -> bool:
        """

        :return:
        """
    @overload
    def GetStandardValuesExclusive(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValuesSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetStandardValuesSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def IsValid(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def IsValid(self, context: ITypeDescriptorContext, value: object) -> bool:
        """

        :param context:
        :param value:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class DecimalConverter(BaseNumberConverter):
    """"""

    def __init__(self):
        """"""
    @overload
    def CanConvertFrom(self, sourceType: Type) -> bool:
        """

        :param sourceType:
        :return:
        """
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool:
        """

        :param context:
        :param sourceType:
        :return:
        """
    @overload
    def CanConvertTo(self, destinationType: Type) -> bool:
        """

        :param destinationType:
        :return:
        """
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, destinationType: Type) -> bool:
        """

        :param context:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertFrom(self, value: object) -> object:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertFrom(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> object:
        """

        :param context:
        :param culture:
        :param value:
        :return:
        """
    @overload
    def ConvertFromInvariantString(self, text: str) -> object:
        """

        :param text:
        :return:
        """
    @overload
    def ConvertFromInvariantString(self, context: ITypeDescriptorContext, text: str) -> object:
        """

        :param context:
        :param text:
        :return:
        """
    @overload
    def ConvertFromString(self, text: str) -> object:
        """

        :param text:
        :return:
        """
    @overload
    def ConvertFromString(self, context: ITypeDescriptorContext, text: str) -> object:
        """

        :param context:
        :param text:
        :return:
        """
    @overload
    def ConvertFromString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, text: str
    ) -> object:
        """

        :param context:
        :param culture:
        :param text:
        :return:
        """
    @overload
    def ConvertTo(self, value: object, destinationType: Type) -> object:
        """

        :param value:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertTo(
        self,
        context: ITypeDescriptorContext,
        culture: CultureInfo,
        value: object,
        destinationType: Type,
    ) -> object:
        """

        :param context:
        :param culture:
        :param value:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertToInvariantString(self, value: object) -> str:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertToInvariantString(self, context: ITypeDescriptorContext, value: object) -> str:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def ConvertToString(self, value: object) -> str:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertToString(self, context: ITypeDescriptorContext, value: object) -> str:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def ConvertToString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> str:
        """

        :param context:
        :param culture:
        :param value:
        :return:
        """
    @overload
    def CreateInstance(self, propertyValues: IDictionary) -> object:
        """

        :param propertyValues:
        :return:
        """
    @overload
    def CreateInstance(
        self, context: ITypeDescriptorContext, propertyValues: IDictionary
    ) -> object:
        """

        :param context:
        :param propertyValues:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetCreateInstanceSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetCreateInstanceSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetProperties(self, value: object) -> PropertyDescriptorCollection:
        """

        :param value:
        :return:
        """
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object
    ) -> PropertyDescriptorCollection:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]
    ) -> PropertyDescriptorCollection:
        """

        :param context:
        :param value:
        :param attributes:
        :return:
        """
    @overload
    def GetPropertiesSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetPropertiesSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValues(self) -> ICollection:
        """

        :return:
        """
    @overload
    def GetStandardValues(
        self, context: ITypeDescriptorContext
    ) -> TypeConverter.StandardValuesCollection:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValuesExclusive(self) -> bool:
        """

        :return:
        """
    @overload
    def GetStandardValuesExclusive(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValuesSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetStandardValuesSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def IsValid(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def IsValid(self, context: ITypeDescriptorContext, value: object) -> bool:
        """

        :param context:
        :param value:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class DefaultBindingPropertyAttribute(Attribute, _Attribute):
    """"""

    Default: Final[ClassVar[DefaultBindingPropertyAttribute]] = ...
    """
    
    :return: 
    """
    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, name: str):
        """

        :param name:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
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

class DefaultEventAttribute(Attribute, _Attribute):
    """"""

    Default: Final[ClassVar[DefaultEventAttribute]] = ...
    """
    
    :return: 
    """
    def __init__(self, name: str):
        """

        :param name:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
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

class DefaultPropertyAttribute(Attribute, _Attribute):
    """"""

    Default: Final[ClassVar[DefaultPropertyAttribute]] = ...
    """
    
    :return: 
    """
    def __init__(self, name: str):
        """

        :param name:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
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

class DefaultValueAttribute(Attribute, _Attribute):
    """"""

    @overload
    def __init__(self, value: bool):
        """

        :param value:
        """
    @overload
    def __init__(self, value: int):
        """

        :param value:
        """
    @overload
    def __init__(self, value: Char):
        """

        :param value:
        """
    @overload
    def __init__(self, value: float):
        """

        :param value:
        """
    @overload
    def __init__(self, value: int):
        """

        :param value:
        """
    @overload
    def __init__(self, value: int):
        """

        :param value:
        """
    @overload
    def __init__(self, value: int):
        """

        :param value:
        """
    @overload
    def __init__(self, value: object):
        """

        :param value:
        """
    @overload
    def __init__(self, value: float):
        """

        :param value:
        """
    @overload
    def __init__(self, value: str):
        """

        :param value:
        """
    @overload
    def __init__(self, type: Type, value: str):
        """

        :param type:
        :param value:
        """
    @property
    def TypeId(self) -> object:
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

class DelegatingTypeDescriptionProvider(TypeDescriptionProvider):
    """"""

    def CreateInstance(
        self,
        provider: IServiceProvider,
        objectType: Type,
        argTypes: Array[Type],
        args: Array[object],
    ) -> object:
        """

        :param provider:
        :param objectType:
        :param argTypes:
        :param args:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetCache(self, instance: object) -> IDictionary:
        """

        :param instance:
        :return:
        """
    def GetExtendedTypeDescriptor(self, instance: object) -> ICustomTypeDescriptor:
        """

        :param instance:
        :return:
        """
    def GetFullComponentName(self, component: object) -> str:
        """

        :param component:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetReflectionType(self, instance: object) -> Type:
        """

        :param instance:
        :return:
        """
    @overload
    def GetReflectionType(self, objectType: Type) -> Type:
        """

        :param objectType:
        :return:
        """
    @overload
    def GetReflectionType(self, objectType: Type, instance: object) -> Type:
        """

        :param objectType:
        :param instance:
        :return:
        """
    def GetRuntimeType(self, reflectionType: Type) -> Type:
        """

        :param reflectionType:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetTypeDescriptor(self, instance: object) -> ICustomTypeDescriptor:
        """

        :param instance:
        :return:
        """
    @overload
    def GetTypeDescriptor(self, objectType: Type) -> ICustomTypeDescriptor:
        """

        :param objectType:
        :return:
        """
    @overload
    def GetTypeDescriptor(self, objectType: Type, instance: object) -> ICustomTypeDescriptor:
        """

        :param objectType:
        :param instance:
        :return:
        """
    def IsSupportedType(self, type: Type) -> bool:
        """

        :param type:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class DescriptionAttribute(Attribute, _Attribute):
    """"""

    Default: Final[ClassVar[DescriptionAttribute]] = ...
    """
    
    :return: 
    """
    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, description: str):
        """

        :param description:
        """
    @property
    def Description(self) -> str:
        """

        :return:
        """
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

class DesignOnlyAttribute(Attribute, _Attribute):
    """"""

    Default: Final[ClassVar[DesignOnlyAttribute]] = ...
    """
    
    :return: 
    """
    No: Final[ClassVar[DesignOnlyAttribute]] = ...
    """
    
    :return: 
    """
    Yes: Final[ClassVar[DesignOnlyAttribute]] = ...
    """
    
    :return: 
    """
    def __init__(self, isDesignOnly: bool):
        """

        :param isDesignOnly:
        """
    @property
    def IsDesignOnly(self) -> bool:
        """

        :return:
        """
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

class DesignTimeVisibleAttribute(Attribute, _Attribute):
    """"""

    Default: Final[ClassVar[DesignTimeVisibleAttribute]] = ...
    """
    
    :return: 
    """
    No: Final[ClassVar[DesignTimeVisibleAttribute]] = ...
    """
    
    :return: 
    """
    Yes: Final[ClassVar[DesignTimeVisibleAttribute]] = ...
    """
    
    :return: 
    """
    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, visible: bool):
        """

        :param visible:
        """
    @property
    def TypeId(self) -> object:
        """

        :return:
        """
    @property
    def Visible(self) -> bool:
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

class DesignerAttribute(Attribute, _Attribute):
    """"""

    @overload
    def __init__(self, designerTypeName: str):
        """

        :param designerTypeName:
        """
    @overload
    def __init__(self, designerType: Type):
        """

        :param designerType:
        """
    @overload
    def __init__(self, designerTypeName: str, designerBaseTypeName: str):
        """

        :param designerTypeName:
        :param designerBaseTypeName:
        """
    @overload
    def __init__(self, designerTypeName: str, designerBaseType: Type):
        """

        :param designerTypeName:
        :param designerBaseType:
        """
    @overload
    def __init__(self, designerType: Type, designerBaseType: Type):
        """

        :param designerType:
        :param designerBaseType:
        """
    @property
    def DesignerBaseTypeName(self) -> str:
        """

        :return:
        """
    @property
    def DesignerTypeName(self) -> str:
        """

        :return:
        """
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

class DesignerCategoryAttribute(Attribute, _Attribute):
    """"""

    Component: Final[ClassVar[DesignerCategoryAttribute]] = ...
    """
    
    :return: 
    """
    Default: Final[ClassVar[DesignerCategoryAttribute]] = ...
    """
    
    :return: 
    """
    Form: Final[ClassVar[DesignerCategoryAttribute]] = ...
    """
    
    :return: 
    """
    Generic: Final[ClassVar[DesignerCategoryAttribute]] = ...
    """
    
    :return: 
    """
    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, category: str):
        """

        :param category:
        """
    @property
    def Category(self) -> str:
        """

        :return:
        """
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

class DesignerSerializationVisibility(Enum):
    """"""

    Hidden: DesignerSerializationVisibility = ...
    """"""
    Visible: DesignerSerializationVisibility = ...
    """"""
    Content: DesignerSerializationVisibility = ...
    """"""

class DesignerSerializationVisibilityAttribute(Attribute, _Attribute):
    """"""

    Content: Final[ClassVar[DesignerSerializationVisibilityAttribute]] = ...
    """
    
    :return: 
    """
    Default: Final[ClassVar[DesignerSerializationVisibilityAttribute]] = ...
    """
    
    :return: 
    """
    Hidden: Final[ClassVar[DesignerSerializationVisibilityAttribute]] = ...
    """
    
    :return: 
    """
    Visible: Final[ClassVar[DesignerSerializationVisibilityAttribute]] = ...
    """
    
    :return: 
    """
    def __init__(self, visibility: DesignerSerializationVisibility):
        """

        :param visibility:
        """
    @property
    def TypeId(self) -> object:
        """

        :return:
        """
    @property
    def Visibility(self) -> DesignerSerializationVisibility:
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

class DisplayNameAttribute(Attribute, _Attribute):
    """"""

    Default: Final[ClassVar[DisplayNameAttribute]] = ...
    """
    
    :return: 
    """
    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, displayName: str):
        """

        :param displayName:
        """
    @property
    def DisplayName(self) -> str:
        """

        :return:
        """
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

class DoWorkEventArgs(CancelEventArgs):
    """"""

    def __init__(self, argument: object):
        """

        :param argument:
        """
    @property
    def Argument(self) -> object:
        """

        :return:
        """
    @property
    def Cancel(self) -> bool:
        """

        :return:
        """
    @Cancel.setter
    def Cancel(self, value: bool) -> None: ...
    @property
    def Result(self) -> object:
        """

        :return:
        """
    @Result.setter
    def Result(self, value: object) -> None: ...
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

DoWorkEventHandler: Callable[[object, DoWorkEventArgs], None] = ...
"""

:param sender: 
:param e: 
"""

class DoubleConverter(BaseNumberConverter):
    """"""

    def __init__(self):
        """"""
    @overload
    def CanConvertFrom(self, sourceType: Type) -> bool:
        """

        :param sourceType:
        :return:
        """
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool:
        """

        :param context:
        :param sourceType:
        :return:
        """
    @overload
    def CanConvertTo(self, destinationType: Type) -> bool:
        """

        :param destinationType:
        :return:
        """
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, destinationType: Type) -> bool:
        """

        :param context:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertFrom(self, value: object) -> object:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertFrom(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> object:
        """

        :param context:
        :param culture:
        :param value:
        :return:
        """
    @overload
    def ConvertFromInvariantString(self, text: str) -> object:
        """

        :param text:
        :return:
        """
    @overload
    def ConvertFromInvariantString(self, context: ITypeDescriptorContext, text: str) -> object:
        """

        :param context:
        :param text:
        :return:
        """
    @overload
    def ConvertFromString(self, text: str) -> object:
        """

        :param text:
        :return:
        """
    @overload
    def ConvertFromString(self, context: ITypeDescriptorContext, text: str) -> object:
        """

        :param context:
        :param text:
        :return:
        """
    @overload
    def ConvertFromString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, text: str
    ) -> object:
        """

        :param context:
        :param culture:
        :param text:
        :return:
        """
    @overload
    def ConvertTo(self, value: object, destinationType: Type) -> object:
        """

        :param value:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertTo(
        self,
        context: ITypeDescriptorContext,
        culture: CultureInfo,
        value: object,
        destinationType: Type,
    ) -> object:
        """

        :param context:
        :param culture:
        :param value:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertToInvariantString(self, value: object) -> str:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertToInvariantString(self, context: ITypeDescriptorContext, value: object) -> str:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def ConvertToString(self, value: object) -> str:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertToString(self, context: ITypeDescriptorContext, value: object) -> str:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def ConvertToString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> str:
        """

        :param context:
        :param culture:
        :param value:
        :return:
        """
    @overload
    def CreateInstance(self, propertyValues: IDictionary) -> object:
        """

        :param propertyValues:
        :return:
        """
    @overload
    def CreateInstance(
        self, context: ITypeDescriptorContext, propertyValues: IDictionary
    ) -> object:
        """

        :param context:
        :param propertyValues:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetCreateInstanceSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetCreateInstanceSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetProperties(self, value: object) -> PropertyDescriptorCollection:
        """

        :param value:
        :return:
        """
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object
    ) -> PropertyDescriptorCollection:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]
    ) -> PropertyDescriptorCollection:
        """

        :param context:
        :param value:
        :param attributes:
        :return:
        """
    @overload
    def GetPropertiesSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetPropertiesSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValues(self) -> ICollection:
        """

        :return:
        """
    @overload
    def GetStandardValues(
        self, context: ITypeDescriptorContext
    ) -> TypeConverter.StandardValuesCollection:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValuesExclusive(self) -> bool:
        """

        :return:
        """
    @overload
    def GetStandardValuesExclusive(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValuesSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetStandardValuesSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def IsValid(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def IsValid(self, context: ITypeDescriptorContext, value: object) -> bool:
        """

        :param context:
        :param value:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class EditorAttribute(Attribute, _Attribute):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, typeName: str, baseTypeName: str):
        """

        :param typeName:
        :param baseTypeName:
        """
    @overload
    def __init__(self, typeName: str, baseType: Type):
        """

        :param typeName:
        :param baseType:
        """
    @overload
    def __init__(self, type: Type, baseType: Type):
        """

        :param type:
        :param baseType:
        """
    @property
    def EditorBaseTypeName(self) -> str:
        """

        :return:
        """
    @property
    def EditorTypeName(self) -> str:
        """

        :return:
        """
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

class EditorBrowsableAttribute(Attribute, _Attribute):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, state: EditorBrowsableState):
        """

        :param state:
        """
    @property
    def State(self) -> EditorBrowsableState:
        """

        :return:
        """
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

class EditorBrowsableState(Enum):
    """"""

    Always: EditorBrowsableState = ...
    """"""
    Never: EditorBrowsableState = ...
    """"""
    Advanced: EditorBrowsableState = ...
    """"""

class EnumConverter(TypeConverter):
    """"""

    def __init__(self, type: Type):
        """

        :param type:
        """
    @overload
    def CanConvertFrom(self, sourceType: Type) -> bool:
        """

        :param sourceType:
        :return:
        """
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool:
        """

        :param context:
        :param sourceType:
        :return:
        """
    @overload
    def CanConvertTo(self, destinationType: Type) -> bool:
        """

        :param destinationType:
        :return:
        """
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, destinationType: Type) -> bool:
        """

        :param context:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertFrom(self, value: object) -> object:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertFrom(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> object:
        """

        :param context:
        :param culture:
        :param value:
        :return:
        """
    @overload
    def ConvertFromInvariantString(self, text: str) -> object:
        """

        :param text:
        :return:
        """
    @overload
    def ConvertFromInvariantString(self, context: ITypeDescriptorContext, text: str) -> object:
        """

        :param context:
        :param text:
        :return:
        """
    @overload
    def ConvertFromString(self, text: str) -> object:
        """

        :param text:
        :return:
        """
    @overload
    def ConvertFromString(self, context: ITypeDescriptorContext, text: str) -> object:
        """

        :param context:
        :param text:
        :return:
        """
    @overload
    def ConvertFromString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, text: str
    ) -> object:
        """

        :param context:
        :param culture:
        :param text:
        :return:
        """
    @overload
    def ConvertTo(self, value: object, destinationType: Type) -> object:
        """

        :param value:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertTo(
        self,
        context: ITypeDescriptorContext,
        culture: CultureInfo,
        value: object,
        destinationType: Type,
    ) -> object:
        """

        :param context:
        :param culture:
        :param value:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertToInvariantString(self, value: object) -> str:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertToInvariantString(self, context: ITypeDescriptorContext, value: object) -> str:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def ConvertToString(self, value: object) -> str:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertToString(self, context: ITypeDescriptorContext, value: object) -> str:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def ConvertToString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> str:
        """

        :param context:
        :param culture:
        :param value:
        :return:
        """
    @overload
    def CreateInstance(self, propertyValues: IDictionary) -> object:
        """

        :param propertyValues:
        :return:
        """
    @overload
    def CreateInstance(
        self, context: ITypeDescriptorContext, propertyValues: IDictionary
    ) -> object:
        """

        :param context:
        :param propertyValues:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetCreateInstanceSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetCreateInstanceSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetProperties(self, value: object) -> PropertyDescriptorCollection:
        """

        :param value:
        :return:
        """
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object
    ) -> PropertyDescriptorCollection:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]
    ) -> PropertyDescriptorCollection:
        """

        :param context:
        :param value:
        :param attributes:
        :return:
        """
    @overload
    def GetPropertiesSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetPropertiesSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValues(self) -> ICollection:
        """

        :return:
        """
    @overload
    def GetStandardValues(
        self, context: ITypeDescriptorContext
    ) -> TypeConverter.StandardValuesCollection:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValuesExclusive(self) -> bool:
        """

        :return:
        """
    @overload
    def GetStandardValuesExclusive(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValuesSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetStandardValuesSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def IsValid(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def IsValid(self, context: ITypeDescriptorContext, value: object) -> bool:
        """

        :param context:
        :param value:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class EventDescriptor(ABC, MemberDescriptor):
    """"""

    @property
    def Attributes(self) -> AttributeCollection:
        """

        :return:
        """
    @property
    def Category(self) -> str:
        """

        :return:
        """
    @property
    def ComponentType(self) -> Type:
        """

        :return:
        """
    @property
    def Description(self) -> str:
        """

        :return:
        """
    @property
    def DesignTimeOnly(self) -> bool:
        """

        :return:
        """
    @property
    def DisplayName(self) -> str:
        """

        :return:
        """
    @property
    def EventType(self) -> Type:
        """

        :return:
        """
    @property
    def IsBrowsable(self) -> bool:
        """

        :return:
        """
    @property
    def IsMulticast(self) -> bool:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    def AddEventHandler(self, component: object, value: Delegate) -> None:
        """

        :param component:
        :param value:
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
    def RemoveEventHandler(self, component: object, value: Delegate) -> None:
        """

        :param component:
        :param value:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class EventDescriptorCollection(Object, ICollection, IEnumerable, IList):
    """"""

    Empty: Final[ClassVar[EventDescriptorCollection]] = ...
    """
    
    :return: 
    """
    @overload
    def __init__(self, events: Array[EventDescriptor]):
        """

        :param events:
        """
    @overload
    def __init__(self, events: Array[EventDescriptor], readOnly: bool):
        """

        :param events:
        :param readOnly:
        """
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
    def SyncRoot(self) -> object:
        """

        :return:
        """
    @overload
    def Add(self, value: EventDescriptor) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def Add(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    def Clear(self) -> None:
        """"""
    @overload
    def Contains(self, value: EventDescriptor) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def Contains(self, value: object) -> bool:
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
    def Find(self, name: str, ignoreCase: bool) -> EventDescriptor:
        """

        :param name:
        :param ignoreCase:
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
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def IndexOf(self, value: EventDescriptor) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def IndexOf(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def Insert(self, index: int, value: EventDescriptor) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def Insert(self, index: int, value: object) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def Remove(self, value: EventDescriptor) -> None:
        """

        :param value:
        """
    @overload
    def Remove(self, value: object) -> None:
        """

        :param value:
        """
    def RemoveAt(self, index: int) -> None:
        """

        :param index:
        """
    @overload
    def Sort(self) -> EventDescriptorCollection:
        """

        :return:
        """
    @overload
    def Sort(self, comparer: IComparer) -> EventDescriptorCollection:
        """

        :param comparer:
        :return:
        """
    @overload
    def Sort(self, names: Array[str]) -> EventDescriptorCollection:
        """

        :param names:
        :return:
        """
    @overload
    def Sort(self, names: Array[str], comparer: IComparer) -> EventDescriptorCollection:
        """

        :param names:
        :param comparer:
        :return:
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
    @overload
    def __getitem__(self, index: int) -> object:
        """

        :param index:
        :return:
        """
    @overload
    def __getitem__(self, name: str) -> EventDescriptor:
        """

        :param name:
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
    def __setitem__(self, index: int, value: object) -> None:
        """

        :param index:
        :param value:
        """

class EventHandlerList(Object, IDisposable):
    """"""

    def __init__(self):
        """"""
    @property
    def Item(self) -> Delegate:
        """

        :return:
        """
    @Item.setter
    def Item(self, value: Delegate) -> None: ...
    def AddHandler(self, key: object, value: Delegate) -> None:
        """

        :param key:
        :param value:
        """
    def AddHandlers(self, listToAddFrom: EventHandlerList) -> None:
        """

        :param listToAddFrom:
        """
    def Dispose(self) -> None:
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
    def RemoveHandler(self, key: object, value: Delegate) -> None:
        """

        :param key:
        :param value:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def __getitem__(self, key: object) -> Delegate:
        """

        :param key:
        :return:
        """
    def __setitem__(self, key: object, value: Delegate) -> None:
        """

        :param key:
        :param value:
        """

class ExpandableObjectConverter(TypeConverter):
    """"""

    def __init__(self):
        """"""
    @overload
    def CanConvertFrom(self, sourceType: Type) -> bool:
        """

        :param sourceType:
        :return:
        """
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool:
        """

        :param context:
        :param sourceType:
        :return:
        """
    @overload
    def CanConvertTo(self, destinationType: Type) -> bool:
        """

        :param destinationType:
        :return:
        """
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, destinationType: Type) -> bool:
        """

        :param context:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertFrom(self, value: object) -> object:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertFrom(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> object:
        """

        :param context:
        :param culture:
        :param value:
        :return:
        """
    @overload
    def ConvertFromInvariantString(self, text: str) -> object:
        """

        :param text:
        :return:
        """
    @overload
    def ConvertFromInvariantString(self, context: ITypeDescriptorContext, text: str) -> object:
        """

        :param context:
        :param text:
        :return:
        """
    @overload
    def ConvertFromString(self, text: str) -> object:
        """

        :param text:
        :return:
        """
    @overload
    def ConvertFromString(self, context: ITypeDescriptorContext, text: str) -> object:
        """

        :param context:
        :param text:
        :return:
        """
    @overload
    def ConvertFromString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, text: str
    ) -> object:
        """

        :param context:
        :param culture:
        :param text:
        :return:
        """
    @overload
    def ConvertTo(self, value: object, destinationType: Type) -> object:
        """

        :param value:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertTo(
        self,
        context: ITypeDescriptorContext,
        culture: CultureInfo,
        value: object,
        destinationType: Type,
    ) -> object:
        """

        :param context:
        :param culture:
        :param value:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertToInvariantString(self, value: object) -> str:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertToInvariantString(self, context: ITypeDescriptorContext, value: object) -> str:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def ConvertToString(self, value: object) -> str:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertToString(self, context: ITypeDescriptorContext, value: object) -> str:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def ConvertToString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> str:
        """

        :param context:
        :param culture:
        :param value:
        :return:
        """
    @overload
    def CreateInstance(self, propertyValues: IDictionary) -> object:
        """

        :param propertyValues:
        :return:
        """
    @overload
    def CreateInstance(
        self, context: ITypeDescriptorContext, propertyValues: IDictionary
    ) -> object:
        """

        :param context:
        :param propertyValues:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetCreateInstanceSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetCreateInstanceSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetProperties(self, value: object) -> PropertyDescriptorCollection:
        """

        :param value:
        :return:
        """
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object
    ) -> PropertyDescriptorCollection:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]
    ) -> PropertyDescriptorCollection:
        """

        :param context:
        :param value:
        :param attributes:
        :return:
        """
    @overload
    def GetPropertiesSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetPropertiesSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValues(self) -> ICollection:
        """

        :return:
        """
    @overload
    def GetStandardValues(
        self, context: ITypeDescriptorContext
    ) -> TypeConverter.StandardValuesCollection:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValuesExclusive(self) -> bool:
        """

        :return:
        """
    @overload
    def GetStandardValuesExclusive(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValuesSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetStandardValuesSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def IsValid(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def IsValid(self, context: ITypeDescriptorContext, value: object) -> bool:
        """

        :param context:
        :param value:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class ExtendedPropertyDescriptor(PropertyDescriptor):
    """"""

    @overload
    def __init__(self, extender: PropertyDescriptor, attributes: Array[Attribute]):
        """

        :param extender:
        :param attributes:
        """
    @overload
    def __init__(
        self,
        extenderInfo: ReflectPropertyDescriptor,
        receiverType: Type,
        provider: IExtenderProvider,
        attributes: Array[Attribute],
    ):
        """

        :param extenderInfo:
        :param receiverType:
        :param provider:
        :param attributes:
        """
    @property
    def Attributes(self) -> AttributeCollection:
        """

        :return:
        """
    @property
    def Category(self) -> str:
        """

        :return:
        """
    @property
    def ComponentType(self) -> Type:
        """

        :return:
        """
    @property
    def Converter(self) -> TypeConverter:
        """

        :return:
        """
    @property
    def Description(self) -> str:
        """

        :return:
        """
    @property
    def DesignTimeOnly(self) -> bool:
        """

        :return:
        """
    @property
    def DisplayName(self) -> str:
        """

        :return:
        """
    @property
    def IsBrowsable(self) -> bool:
        """

        :return:
        """
    @property
    def IsLocalizable(self) -> bool:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def PropertyType(self) -> Type:
        """

        :return:
        """
    @property
    def SerializationVisibility(self) -> DesignerSerializationVisibility:
        """

        :return:
        """
    @property
    def SupportsChangeEvents(self) -> bool:
        """

        :return:
        """
    def AddValueChanged(self, component: object, handler: EventHandler) -> None:
        """

        :param component:
        :param handler:
        """
    def CanResetValue(self, component: object) -> bool:
        """

        :param component:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetChildProperties(self) -> PropertyDescriptorCollection:
        """

        :return:
        """
    @overload
    def GetChildProperties(self, filter: Array[Attribute]) -> PropertyDescriptorCollection:
        """

        :param filter:
        :return:
        """
    @overload
    def GetChildProperties(self, instance: object) -> PropertyDescriptorCollection:
        """

        :param instance:
        :return:
        """
    @overload
    def GetChildProperties(
        self, instance: object, filter: Array[Attribute]
    ) -> PropertyDescriptorCollection:
        """

        :param instance:
        :param filter:
        :return:
        """
    def GetEditor(self, editorBaseType: Type) -> object:
        """

        :param editorBaseType:
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
    def GetValue(self, component: object) -> object:
        """

        :param component:
        :return:
        """
    def RemoveValueChanged(self, component: object, handler: EventHandler) -> None:
        """

        :param component:
        :param handler:
        """
    def ResetValue(self, component: object) -> None:
        """

        :param component:
        """
    def SetValue(self, component: object, value: object) -> None:
        """

        :param component:
        :param value:
        """
    def ShouldSerializeValue(self, component: object) -> bool:
        """

        :param component:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class ExtenderProvidedPropertyAttribute(Attribute, _Attribute):
    """"""

    def __init__(self):
        """"""
    @property
    def ExtenderProperty(self) -> PropertyDescriptor:
        """

        :return:
        """
    @property
    def Provider(self) -> IExtenderProvider:
        """

        :return:
        """
    @property
    def ReceiverType(self) -> Type:
        """

        :return:
        """
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

class GuidConverter(TypeConverter):
    """"""

    def __init__(self):
        """"""
    @overload
    def CanConvertFrom(self, sourceType: Type) -> bool:
        """

        :param sourceType:
        :return:
        """
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool:
        """

        :param context:
        :param sourceType:
        :return:
        """
    @overload
    def CanConvertTo(self, destinationType: Type) -> bool:
        """

        :param destinationType:
        :return:
        """
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, destinationType: Type) -> bool:
        """

        :param context:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertFrom(self, value: object) -> object:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertFrom(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> object:
        """

        :param context:
        :param culture:
        :param value:
        :return:
        """
    @overload
    def ConvertFromInvariantString(self, text: str) -> object:
        """

        :param text:
        :return:
        """
    @overload
    def ConvertFromInvariantString(self, context: ITypeDescriptorContext, text: str) -> object:
        """

        :param context:
        :param text:
        :return:
        """
    @overload
    def ConvertFromString(self, text: str) -> object:
        """

        :param text:
        :return:
        """
    @overload
    def ConvertFromString(self, context: ITypeDescriptorContext, text: str) -> object:
        """

        :param context:
        :param text:
        :return:
        """
    @overload
    def ConvertFromString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, text: str
    ) -> object:
        """

        :param context:
        :param culture:
        :param text:
        :return:
        """
    @overload
    def ConvertTo(self, value: object, destinationType: Type) -> object:
        """

        :param value:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertTo(
        self,
        context: ITypeDescriptorContext,
        culture: CultureInfo,
        value: object,
        destinationType: Type,
    ) -> object:
        """

        :param context:
        :param culture:
        :param value:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertToInvariantString(self, value: object) -> str:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertToInvariantString(self, context: ITypeDescriptorContext, value: object) -> str:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def ConvertToString(self, value: object) -> str:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertToString(self, context: ITypeDescriptorContext, value: object) -> str:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def ConvertToString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> str:
        """

        :param context:
        :param culture:
        :param value:
        :return:
        """
    @overload
    def CreateInstance(self, propertyValues: IDictionary) -> object:
        """

        :param propertyValues:
        :return:
        """
    @overload
    def CreateInstance(
        self, context: ITypeDescriptorContext, propertyValues: IDictionary
    ) -> object:
        """

        :param context:
        :param propertyValues:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetCreateInstanceSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetCreateInstanceSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetProperties(self, value: object) -> PropertyDescriptorCollection:
        """

        :param value:
        :return:
        """
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object
    ) -> PropertyDescriptorCollection:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]
    ) -> PropertyDescriptorCollection:
        """

        :param context:
        :param value:
        :param attributes:
        :return:
        """
    @overload
    def GetPropertiesSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetPropertiesSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValues(self) -> ICollection:
        """

        :return:
        """
    @overload
    def GetStandardValues(
        self, context: ITypeDescriptorContext
    ) -> TypeConverter.StandardValuesCollection:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValuesExclusive(self) -> bool:
        """

        :return:
        """
    @overload
    def GetStandardValuesExclusive(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValuesSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetStandardValuesSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def IsValid(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def IsValid(self, context: ITypeDescriptorContext, value: object) -> bool:
        """

        :param context:
        :param value:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class HandledEventArgs(EventArgs):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, defaultHandledValue: bool):
        """

        :param defaultHandledValue:
        """
    @property
    def Handled(self) -> bool:
        """

        :return:
        """
    @Handled.setter
    def Handled(self, value: bool) -> None: ...
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

HandledEventHandler: Callable[[object, HandledEventArgs], None] = ...
"""

:param sender: 
:param e: 
"""

class IBindingList(ICollection, IEnumerable, IList):
    """"""

    @property
    def AllowEdit(self) -> bool:
        """

        :return:
        """
    @property
    def AllowNew(self) -> bool:
        """

        :return:
        """
    @property
    def AllowRemove(self) -> bool:
        """

        :return:
        """
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
    def IsSorted(self) -> bool:
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
    def SortDirection(self) -> ListSortDirection:
        """

        :return:
        """
    @property
    def SortProperty(self) -> PropertyDescriptor:
        """

        :return:
        """
    @property
    def SupportsChangeNotification(self) -> bool:
        """

        :return:
        """
    @property
    def SupportsSearching(self) -> bool:
        """

        :return:
        """
    @property
    def SupportsSorting(self) -> bool:
        """

        :return:
        """
    @property
    def SyncRoot(self) -> object:
        """

        :return:
        """
    def Add(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    def AddIndex(self, property: PropertyDescriptor) -> None:
        """

        :param property:
        """
    def AddNew(self) -> object:
        """

        :return:
        """
    def ApplySort(self, property: PropertyDescriptor, direction: ListSortDirection) -> None:
        """

        :param property:
        :param direction:
        """
    def Clear(self) -> None:
        """"""
    def Contains(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    def Find(self, property: PropertyDescriptor, key: object) -> int:
        """

        :param property:
        :param key:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    def IndexOf(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    def Insert(self, index: int, value: object) -> None:
        """

        :param index:
        :param value:
        """
    def Remove(self, value: object) -> None:
        """

        :param value:
        """
    def RemoveAt(self, index: int) -> None:
        """

        :param index:
        """
    def RemoveIndex(self, property: PropertyDescriptor) -> None:
        """

        :param property:
        """
    def RemoveSort(self) -> None:
        """"""
    def __contains__(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    def __getitem__(self, index: int) -> object:
        """

        :param index:
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
    def __setitem__(self, index: int, value: object) -> None:
        """

        :param index:
        :param value:
        """
    ListChanged: EventType[ListChangedEventHandler] = ...
    """"""

class IBindingListView(ICollection, IEnumerable, IList, IBindingList):
    """"""

    @property
    def AllowEdit(self) -> bool:
        """

        :return:
        """
    @property
    def AllowNew(self) -> bool:
        """

        :return:
        """
    @property
    def AllowRemove(self) -> bool:
        """

        :return:
        """
    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def Filter(self) -> str:
        """

        :return:
        """
    @Filter.setter
    def Filter(self, value: str) -> None: ...
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
    def IsSorted(self) -> bool:
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
    def SortDescriptions(self) -> ListSortDescriptionCollection:
        """

        :return:
        """
    @property
    def SortDirection(self) -> ListSortDirection:
        """

        :return:
        """
    @property
    def SortProperty(self) -> PropertyDescriptor:
        """

        :return:
        """
    @property
    def SupportsAdvancedSorting(self) -> bool:
        """

        :return:
        """
    @property
    def SupportsChangeNotification(self) -> bool:
        """

        :return:
        """
    @property
    def SupportsFiltering(self) -> bool:
        """

        :return:
        """
    @property
    def SupportsSearching(self) -> bool:
        """

        :return:
        """
    @property
    def SupportsSorting(self) -> bool:
        """

        :return:
        """
    @property
    def SyncRoot(self) -> object:
        """

        :return:
        """
    def Add(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    def AddIndex(self, property: PropertyDescriptor) -> None:
        """

        :param property:
        """
    def AddNew(self) -> object:
        """

        :return:
        """
    @overload
    def ApplySort(self, sorts: ListSortDescriptionCollection) -> None:
        """

        :param sorts:
        """
    @overload
    def ApplySort(self, property: PropertyDescriptor, direction: ListSortDirection) -> None:
        """

        :param property:
        :param direction:
        """
    def Clear(self) -> None:
        """"""
    def Contains(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    def Find(self, property: PropertyDescriptor, key: object) -> int:
        """

        :param property:
        :param key:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    def IndexOf(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    def Insert(self, index: int, value: object) -> None:
        """

        :param index:
        :param value:
        """
    def Remove(self, value: object) -> None:
        """

        :param value:
        """
    def RemoveAt(self, index: int) -> None:
        """

        :param index:
        """
    def RemoveFilter(self) -> None:
        """"""
    def RemoveIndex(self, property: PropertyDescriptor) -> None:
        """

        :param property:
        """
    def RemoveSort(self) -> None:
        """"""
    def __contains__(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    def __getitem__(self, index: int) -> object:
        """

        :param index:
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
    def __setitem__(self, index: int, value: object) -> None:
        """

        :param index:
        :param value:
        """
    ListChanged: EventType[ListChangedEventHandler] = ...
    """"""

class ICancelAddNew:
    """"""

    def CancelNew(self, itemIndex: int) -> None:
        """

        :param itemIndex:
        """
    def EndNew(self, itemIndex: int) -> None:
        """

        :param itemIndex:
        """

class IChangeTracking:
    """"""

    @property
    def IsChanged(self) -> bool:
        """

        :return:
        """
    def AcceptChanges(self) -> None:
        """"""

class IComNativeDescriptorHandler:
    """"""

    def GetAttributes(self, component: object) -> AttributeCollection:
        """

        :param component:
        :return:
        """
    def GetClassName(self, component: object) -> str:
        """

        :param component:
        :return:
        """
    def GetConverter(self, component: object) -> TypeConverter:
        """

        :param component:
        :return:
        """
    def GetDefaultEvent(self, component: object) -> EventDescriptor:
        """

        :param component:
        :return:
        """
    def GetDefaultProperty(self, component: object) -> PropertyDescriptor:
        """

        :param component:
        :return:
        """
    def GetEditor(self, component: object, baseEditorType: Type) -> object:
        """

        :param component:
        :param baseEditorType:
        :return:
        """
    @overload
    def GetEvents(self, component: object) -> EventDescriptorCollection:
        """

        :param component:
        :return:
        """
    @overload
    def GetEvents(
        self, component: object, attributes: Array[Attribute]
    ) -> EventDescriptorCollection:
        """

        :param component:
        :param attributes:
        :return:
        """
    def GetName(self, component: object) -> str:
        """

        :param component:
        :return:
        """
    def GetProperties(
        self, component: object, attributes: Array[Attribute]
    ) -> PropertyDescriptorCollection:
        """

        :param component:
        :param attributes:
        :return:
        """
    @overload
    def GetPropertyValue(self, component: object, dispid: int, success: bool) -> object:
        """

        :param component:
        :param dispid:
        :param success:
        :return:
        """
    @overload
    def GetPropertyValue(self, component: object, propertyName: str, success: bool) -> object:
        """

        :param component:
        :param propertyName:
        :param success:
        :return:
        """

class IComponent(IDisposable):
    """"""

    @property
    def Site(self) -> ISite:
        """

        :return:
        """
    @Site.setter
    def Site(self, value: ISite) -> None: ...
    def Dispose(self) -> None:
        """"""
    Disposed: EventType[EventHandler] = ...
    """"""

class IContainer(IDisposable):
    """"""

    @property
    def Components(self) -> ComponentCollection:
        """

        :return:
        """
    @overload
    def Add(self, component: IComponent) -> None:
        """

        :param component:
        """
    @overload
    def Add(self, component: IComponent, name: str) -> None:
        """

        :param component:
        :param name:
        """
    def Dispose(self) -> None:
        """"""
    def Remove(self, component: IComponent) -> None:
        """

        :param component:
        """

class ICustomTypeDescriptor:
    """"""

    def GetAttributes(self) -> AttributeCollection:
        """

        :return:
        """
    def GetClassName(self) -> str:
        """

        :return:
        """
    def GetComponentName(self) -> str:
        """

        :return:
        """
    def GetConverter(self) -> TypeConverter:
        """

        :return:
        """
    def GetDefaultEvent(self) -> EventDescriptor:
        """

        :return:
        """
    def GetDefaultProperty(self) -> PropertyDescriptor:
        """

        :return:
        """
    def GetEditor(self, editorBaseType: Type) -> object:
        """

        :param editorBaseType:
        :return:
        """
    @overload
    def GetEvents(self) -> EventDescriptorCollection:
        """

        :return:
        """
    @overload
    def GetEvents(self, attributes: Array[Attribute]) -> EventDescriptorCollection:
        """

        :param attributes:
        :return:
        """
    @overload
    def GetProperties(self) -> PropertyDescriptorCollection:
        """

        :return:
        """
    @overload
    def GetProperties(self, attributes: Array[Attribute]) -> PropertyDescriptorCollection:
        """

        :param attributes:
        :return:
        """
    def GetPropertyOwner(self, pd: PropertyDescriptor) -> object:
        """

        :param pd:
        :return:
        """

class IDataErrorInfo:
    """"""

    @property
    def Error(self) -> str:
        """

        :return:
        """
    @property
    def Item(self) -> str:
        """

        :return:
        """
    def __getitem__(self, columnName: str) -> str:
        """

        :param columnName:
        :return:
        """

class IEditableObject:
    """"""

    def BeginEdit(self) -> None:
        """"""
    def CancelEdit(self) -> None:
        """"""
    def EndEdit(self) -> None:
        """"""

class IExtenderProvider:
    """"""

    def CanExtend(self, extendee: object) -> bool:
        """

        :param extendee:
        :return:
        """

class IIntellisenseBuilder:
    """"""

    @property
    def Name(self) -> str:
        """

        :return:
        """
    def Show(self, language: str, value: str, newValue: str) -> bool:
        """

        :param language:
        :param value:
        :param newValue:
        :return:
        """

class IListSource:
    """"""

    @property
    def ContainsListCollection(self) -> bool:
        """

        :return:
        """
    def GetList(self) -> IList:
        """

        :return:
        """

class INestedContainer(IContainer, IDisposable):
    """"""

    @property
    def Components(self) -> ComponentCollection:
        """

        :return:
        """
    @property
    def Owner(self) -> IComponent:
        """

        :return:
        """
    @overload
    def Add(self, component: IComponent) -> None:
        """

        :param component:
        """
    @overload
    def Add(self, component: IComponent, name: str) -> None:
        """

        :param component:
        :param name:
        """
    def Dispose(self) -> None:
        """"""
    def Remove(self, component: IComponent) -> None:
        """

        :param component:
        """

class INestedSite(ISite, IServiceProvider):
    """"""

    @property
    def Component(self) -> IComponent:
        """

        :return:
        """
    @property
    def Container(self) -> IContainer:
        """

        :return:
        """
    @property
    def DesignMode(self) -> bool:
        """

        :return:
        """
    @property
    def FullName(self) -> str:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @Name.setter
    def Name(self, value: str) -> None: ...
    def GetService(self, serviceType: Type) -> object:
        """

        :param serviceType:
        :return:
        """

class INotifyDataErrorInfo:
    """"""

    @property
    def HasErrors(self) -> bool:
        """

        :return:
        """
    def GetErrors(self, propertyName: str) -> IEnumerable:
        """

        :param propertyName:
        :return:
        """
    ErrorsChanged: EventType[EventHandler[DataErrorsChangedEventArgs]] = ...
    """"""

class INotifyPropertyChanged:
    """"""

    PropertyChanged: EventType[PropertyChangedEventHandler] = ...
    """"""

class INotifyPropertyChanging:
    """"""

    PropertyChanging: EventType[PropertyChangingEventHandler] = ...
    """"""

class IRaiseItemChangedEvents:
    """"""

    @property
    def RaisesItemChangedEvents(self) -> bool:
        """

        :return:
        """

class IRevertibleChangeTracking(IChangeTracking):
    """"""

    @property
    def IsChanged(self) -> bool:
        """

        :return:
        """
    def AcceptChanges(self) -> None:
        """"""
    def RejectChanges(self) -> None:
        """"""

class ISite(IServiceProvider):
    """"""

    @property
    def Component(self) -> IComponent:
        """

        :return:
        """
    @property
    def Container(self) -> IContainer:
        """

        :return:
        """
    @property
    def DesignMode(self) -> bool:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @Name.setter
    def Name(self, value: str) -> None: ...
    def GetService(self, serviceType: Type) -> object:
        """

        :param serviceType:
        :return:
        """

class ISupportInitialize:
    """"""

    def BeginInit(self) -> None:
        """"""
    def EndInit(self) -> None:
        """"""

class ISupportInitializeNotification(ISupportInitialize):
    """"""

    @property
    def IsInitialized(self) -> bool:
        """

        :return:
        """
    def BeginInit(self) -> None:
        """"""
    def EndInit(self) -> None:
        """"""
    Initialized: EventType[EventHandler] = ...
    """"""

class ISynchronizeInvoke:
    """"""

    @property
    def InvokeRequired(self) -> bool:
        """

        :return:
        """
    def BeginInvoke(self, method: Delegate, args: Array[object]) -> IAsyncResult:
        """

        :param method:
        :param args:
        :return:
        """
    def EndInvoke(self, result: IAsyncResult) -> object:
        """

        :param result:
        :return:
        """
    def Invoke(self, method: Delegate, args: Array[object]) -> object:
        """

        :param method:
        :param args:
        :return:
        """

class ITypeDescriptorContext(IServiceProvider):
    """"""

    @property
    def Container(self) -> IContainer:
        """

        :return:
        """
    @property
    def Instance(self) -> object:
        """

        :return:
        """
    @property
    def PropertyDescriptor(self) -> PropertyDescriptor:
        """

        :return:
        """
    def GetService(self, serviceType: Type) -> object:
        """

        :param serviceType:
        :return:
        """
    def OnComponentChanged(self) -> None:
        """"""
    def OnComponentChanging(self) -> bool:
        """

        :return:
        """

class ITypedList:
    """"""

    def GetItemProperties(
        self, listAccessors: Array[PropertyDescriptor]
    ) -> PropertyDescriptorCollection:
        """

        :param listAccessors:
        :return:
        """
    def GetListName(self, listAccessors: Array[PropertyDescriptor]) -> str:
        """

        :param listAccessors:
        :return:
        """

class ImmutableObjectAttribute(Attribute, _Attribute):
    """"""

    Default: Final[ClassVar[ImmutableObjectAttribute]] = ...
    """
    
    :return: 
    """
    No: Final[ClassVar[ImmutableObjectAttribute]] = ...
    """
    
    :return: 
    """
    Yes: Final[ClassVar[ImmutableObjectAttribute]] = ...
    """
    
    :return: 
    """
    def __init__(self, immutable: bool):
        """

        :param immutable:
        """
    @property
    def Immutable(self) -> bool:
        """

        :return:
        """
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

class InheritanceAttribute(Attribute, _Attribute):
    """"""

    Default: Final[ClassVar[InheritanceAttribute]] = ...
    """
    
    :return: 
    """
    Inherited: Final[ClassVar[InheritanceAttribute]] = ...
    """
    
    :return: 
    """
    InheritedReadOnly: Final[ClassVar[InheritanceAttribute]] = ...
    """
    
    :return: 
    """
    NotInherited: Final[ClassVar[InheritanceAttribute]] = ...
    """
    
    :return: 
    """
    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, inheritanceLevel: InheritanceLevel):
        """

        :param inheritanceLevel:
        """
    @property
    def InheritanceLevel(self) -> InheritanceLevel:
        """

        :return:
        """
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

class InheritanceLevel(Enum):
    """"""

    Inherited: InheritanceLevel = ...
    """"""
    InheritedReadOnly: InheritanceLevel = ...
    """"""
    NotInherited: InheritanceLevel = ...
    """"""

class InitializationEventAttribute(Attribute, _Attribute):
    """"""

    def __init__(self, eventName: str):
        """

        :param eventName:
        """
    @property
    def EventName(self) -> str:
        """

        :return:
        """
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

class InstallerTypeAttribute(Attribute, _Attribute):
    """"""

    @overload
    def __init__(self, typeName: str):
        """

        :param typeName:
        """
    @overload
    def __init__(self, installerType: Type):
        """

        :param installerType:
        """
    @property
    def InstallerType(self) -> Type:
        """

        :return:
        """
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

class InstanceCreationEditor(ABC, Object):
    """"""

    @property
    def Text(self) -> str:
        """

        :return:
        """
    def CreateInstance(self, context: ITypeDescriptorContext, instanceType: Type) -> object:
        """

        :param context:
        :param instanceType:
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

class Int16Converter(BaseNumberConverter):
    """"""

    def __init__(self):
        """"""
    @overload
    def CanConvertFrom(self, sourceType: Type) -> bool:
        """

        :param sourceType:
        :return:
        """
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool:
        """

        :param context:
        :param sourceType:
        :return:
        """
    @overload
    def CanConvertTo(self, destinationType: Type) -> bool:
        """

        :param destinationType:
        :return:
        """
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, destinationType: Type) -> bool:
        """

        :param context:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertFrom(self, value: object) -> object:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertFrom(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> object:
        """

        :param context:
        :param culture:
        :param value:
        :return:
        """
    @overload
    def ConvertFromInvariantString(self, text: str) -> object:
        """

        :param text:
        :return:
        """
    @overload
    def ConvertFromInvariantString(self, context: ITypeDescriptorContext, text: str) -> object:
        """

        :param context:
        :param text:
        :return:
        """
    @overload
    def ConvertFromString(self, text: str) -> object:
        """

        :param text:
        :return:
        """
    @overload
    def ConvertFromString(self, context: ITypeDescriptorContext, text: str) -> object:
        """

        :param context:
        :param text:
        :return:
        """
    @overload
    def ConvertFromString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, text: str
    ) -> object:
        """

        :param context:
        :param culture:
        :param text:
        :return:
        """
    @overload
    def ConvertTo(self, value: object, destinationType: Type) -> object:
        """

        :param value:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertTo(
        self,
        context: ITypeDescriptorContext,
        culture: CultureInfo,
        value: object,
        destinationType: Type,
    ) -> object:
        """

        :param context:
        :param culture:
        :param value:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertToInvariantString(self, value: object) -> str:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertToInvariantString(self, context: ITypeDescriptorContext, value: object) -> str:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def ConvertToString(self, value: object) -> str:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertToString(self, context: ITypeDescriptorContext, value: object) -> str:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def ConvertToString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> str:
        """

        :param context:
        :param culture:
        :param value:
        :return:
        """
    @overload
    def CreateInstance(self, propertyValues: IDictionary) -> object:
        """

        :param propertyValues:
        :return:
        """
    @overload
    def CreateInstance(
        self, context: ITypeDescriptorContext, propertyValues: IDictionary
    ) -> object:
        """

        :param context:
        :param propertyValues:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetCreateInstanceSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetCreateInstanceSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetProperties(self, value: object) -> PropertyDescriptorCollection:
        """

        :param value:
        :return:
        """
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object
    ) -> PropertyDescriptorCollection:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]
    ) -> PropertyDescriptorCollection:
        """

        :param context:
        :param value:
        :param attributes:
        :return:
        """
    @overload
    def GetPropertiesSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetPropertiesSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValues(self) -> ICollection:
        """

        :return:
        """
    @overload
    def GetStandardValues(
        self, context: ITypeDescriptorContext
    ) -> TypeConverter.StandardValuesCollection:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValuesExclusive(self) -> bool:
        """

        :return:
        """
    @overload
    def GetStandardValuesExclusive(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValuesSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetStandardValuesSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def IsValid(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def IsValid(self, context: ITypeDescriptorContext, value: object) -> bool:
        """

        :param context:
        :param value:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class Int32Converter(BaseNumberConverter):
    """"""

    def __init__(self):
        """"""
    @overload
    def CanConvertFrom(self, sourceType: Type) -> bool:
        """

        :param sourceType:
        :return:
        """
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool:
        """

        :param context:
        :param sourceType:
        :return:
        """
    @overload
    def CanConvertTo(self, destinationType: Type) -> bool:
        """

        :param destinationType:
        :return:
        """
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, destinationType: Type) -> bool:
        """

        :param context:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertFrom(self, value: object) -> object:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertFrom(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> object:
        """

        :param context:
        :param culture:
        :param value:
        :return:
        """
    @overload
    def ConvertFromInvariantString(self, text: str) -> object:
        """

        :param text:
        :return:
        """
    @overload
    def ConvertFromInvariantString(self, context: ITypeDescriptorContext, text: str) -> object:
        """

        :param context:
        :param text:
        :return:
        """
    @overload
    def ConvertFromString(self, text: str) -> object:
        """

        :param text:
        :return:
        """
    @overload
    def ConvertFromString(self, context: ITypeDescriptorContext, text: str) -> object:
        """

        :param context:
        :param text:
        :return:
        """
    @overload
    def ConvertFromString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, text: str
    ) -> object:
        """

        :param context:
        :param culture:
        :param text:
        :return:
        """
    @overload
    def ConvertTo(self, value: object, destinationType: Type) -> object:
        """

        :param value:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertTo(
        self,
        context: ITypeDescriptorContext,
        culture: CultureInfo,
        value: object,
        destinationType: Type,
    ) -> object:
        """

        :param context:
        :param culture:
        :param value:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertToInvariantString(self, value: object) -> str:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertToInvariantString(self, context: ITypeDescriptorContext, value: object) -> str:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def ConvertToString(self, value: object) -> str:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertToString(self, context: ITypeDescriptorContext, value: object) -> str:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def ConvertToString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> str:
        """

        :param context:
        :param culture:
        :param value:
        :return:
        """
    @overload
    def CreateInstance(self, propertyValues: IDictionary) -> object:
        """

        :param propertyValues:
        :return:
        """
    @overload
    def CreateInstance(
        self, context: ITypeDescriptorContext, propertyValues: IDictionary
    ) -> object:
        """

        :param context:
        :param propertyValues:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetCreateInstanceSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetCreateInstanceSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetProperties(self, value: object) -> PropertyDescriptorCollection:
        """

        :param value:
        :return:
        """
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object
    ) -> PropertyDescriptorCollection:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]
    ) -> PropertyDescriptorCollection:
        """

        :param context:
        :param value:
        :param attributes:
        :return:
        """
    @overload
    def GetPropertiesSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetPropertiesSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValues(self) -> ICollection:
        """

        :return:
        """
    @overload
    def GetStandardValues(
        self, context: ITypeDescriptorContext
    ) -> TypeConverter.StandardValuesCollection:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValuesExclusive(self) -> bool:
        """

        :return:
        """
    @overload
    def GetStandardValuesExclusive(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValuesSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetStandardValuesSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def IsValid(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def IsValid(self, context: ITypeDescriptorContext, value: object) -> bool:
        """

        :param context:
        :param value:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class Int64Converter(BaseNumberConverter):
    """"""

    def __init__(self):
        """"""
    @overload
    def CanConvertFrom(self, sourceType: Type) -> bool:
        """

        :param sourceType:
        :return:
        """
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool:
        """

        :param context:
        :param sourceType:
        :return:
        """
    @overload
    def CanConvertTo(self, destinationType: Type) -> bool:
        """

        :param destinationType:
        :return:
        """
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, destinationType: Type) -> bool:
        """

        :param context:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertFrom(self, value: object) -> object:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertFrom(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> object:
        """

        :param context:
        :param culture:
        :param value:
        :return:
        """
    @overload
    def ConvertFromInvariantString(self, text: str) -> object:
        """

        :param text:
        :return:
        """
    @overload
    def ConvertFromInvariantString(self, context: ITypeDescriptorContext, text: str) -> object:
        """

        :param context:
        :param text:
        :return:
        """
    @overload
    def ConvertFromString(self, text: str) -> object:
        """

        :param text:
        :return:
        """
    @overload
    def ConvertFromString(self, context: ITypeDescriptorContext, text: str) -> object:
        """

        :param context:
        :param text:
        :return:
        """
    @overload
    def ConvertFromString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, text: str
    ) -> object:
        """

        :param context:
        :param culture:
        :param text:
        :return:
        """
    @overload
    def ConvertTo(self, value: object, destinationType: Type) -> object:
        """

        :param value:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertTo(
        self,
        context: ITypeDescriptorContext,
        culture: CultureInfo,
        value: object,
        destinationType: Type,
    ) -> object:
        """

        :param context:
        :param culture:
        :param value:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertToInvariantString(self, value: object) -> str:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertToInvariantString(self, context: ITypeDescriptorContext, value: object) -> str:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def ConvertToString(self, value: object) -> str:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertToString(self, context: ITypeDescriptorContext, value: object) -> str:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def ConvertToString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> str:
        """

        :param context:
        :param culture:
        :param value:
        :return:
        """
    @overload
    def CreateInstance(self, propertyValues: IDictionary) -> object:
        """

        :param propertyValues:
        :return:
        """
    @overload
    def CreateInstance(
        self, context: ITypeDescriptorContext, propertyValues: IDictionary
    ) -> object:
        """

        :param context:
        :param propertyValues:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetCreateInstanceSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetCreateInstanceSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetProperties(self, value: object) -> PropertyDescriptorCollection:
        """

        :param value:
        :return:
        """
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object
    ) -> PropertyDescriptorCollection:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]
    ) -> PropertyDescriptorCollection:
        """

        :param context:
        :param value:
        :param attributes:
        :return:
        """
    @overload
    def GetPropertiesSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetPropertiesSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValues(self) -> ICollection:
        """

        :return:
        """
    @overload
    def GetStandardValues(
        self, context: ITypeDescriptorContext
    ) -> TypeConverter.StandardValuesCollection:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValuesExclusive(self) -> bool:
        """

        :return:
        """
    @overload
    def GetStandardValuesExclusive(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValuesSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetStandardValuesSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def IsValid(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def IsValid(self, context: ITypeDescriptorContext, value: object) -> bool:
        """

        :param context:
        :param value:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class IntSecurity(ABC, Object):
    """"""

    FullReflection: Final[ClassVar[CodeAccessPermission]] = ...
    """
    
    :return: 
    """
    UnmanagedCode: Final[ClassVar[CodeAccessPermission]] = ...
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
    @classmethod
    def UnsafeGetFullPath(cls, fileName: str) -> str:
        """

        :param fileName:
        :return:
        """

class InvalidAsynchronousStateException(ArgumentException, _Exception, ISerializable):
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
    def ParamName(self) -> str:
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

class InvalidEnumArgumentException(ArgumentException, _Exception, ISerializable):
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
    @overload
    def __init__(self, argumentName: str, invalidValue: int, enumClass: Type):
        """

        :param argumentName:
        :param invalidValue:
        :param enumClass:
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
    def ParamName(self) -> str:
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

class LicFileLicenseProvider(LicenseProvider):
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
    def GetLicense(
        self, context: LicenseContext, type: Type, instance: object, allowExceptions: bool
    ) -> License:
        """

        :param context:
        :param type:
        :param instance:
        :param allowExceptions:
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

class License(ABC, Object, IDisposable):
    """"""

    @property
    def LicenseKey(self) -> str:
        """

        :return:
        """
    def Dispose(self) -> None:
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

class LicenseContext(Object, IServiceProvider):
    """"""

    def __init__(self):
        """"""
    @property
    def UsageMode(self) -> LicenseUsageMode:
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
    def GetSavedLicenseKey(self, type: Type, resourceAssembly: Assembly) -> str:
        """

        :param type:
        :param resourceAssembly:
        :return:
        """
    def GetService(self, serviceType: Type) -> object:
        """

        :param serviceType:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def SetSavedLicenseKey(self, type: Type, key: str) -> None:
        """

        :param type:
        :param key:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class LicenseException(SystemException, _Exception, ISerializable):
    """"""

    @overload
    def __init__(self, type: Type):
        """

        :param type:
        """
    @overload
    def __init__(self, type: Type, instance: object):
        """

        :param type:
        :param instance:
        """
    @overload
    def __init__(self, type: Type, instance: object, message: str):
        """

        :param type:
        :param instance:
        :param message:
        """
    @overload
    def __init__(self, type: Type, instance: object, message: str, innerException: Exception):
        """

        :param type:
        :param instance:
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
    def LicensedType(self) -> Type:
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

class LicenseManager(Object):
    """"""

    @classmethod
    @property
    def CurrentContext(cls) -> LicenseContext:
        """

        :return:
        """
    @classmethod
    @CurrentContext.setter
    def CurrentContext(cls, value: LicenseContext) -> None: ...
    @classmethod
    @property
    def UsageMode(cls) -> LicenseUsageMode:
        """

        :return:
        """
    @classmethod
    @overload
    def CreateWithContext(cls, type: Type, creationContext: LicenseContext) -> object:
        """

        :param type:
        :param creationContext:
        :return:
        """
    @classmethod
    @overload
    def CreateWithContext(
        cls, type: Type, creationContext: LicenseContext, args: Array[object]
    ) -> object:
        """

        :param type:
        :param creationContext:
        :param args:
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
    def IsLicensed(cls, type: Type) -> bool:
        """

        :param type:
        :return:
        """
    @classmethod
    @overload
    def IsValid(cls, type: Type) -> bool:
        """

        :param type:
        :return:
        """
    @classmethod
    @overload
    def IsValid(cls, type: Type, instance: object, license: License) -> Tuple[bool, License]:
        """

        :param type:
        :param instance:
        :param license:
        :return:
        """
    @classmethod
    def LockContext(cls, contextUser: object) -> None:
        """

        :param contextUser:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @classmethod
    def UnlockContext(cls, contextUser: object) -> None:
        """

        :param contextUser:
        """
    @classmethod
    @overload
    def Validate(cls, type: Type) -> None:
        """

        :param type:
        """
    @classmethod
    @overload
    def Validate(cls, type: Type, instance: object) -> License:
        """

        :param type:
        :param instance:
        :return:
        """

class LicenseProvider(ABC, Object):
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
    def GetLicense(
        self, context: LicenseContext, type: Type, instance: object, allowExceptions: bool
    ) -> License:
        """

        :param context:
        :param type:
        :param instance:
        :param allowExceptions:
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

class LicenseProviderAttribute(Attribute, _Attribute):
    """"""

    Default: Final[ClassVar[LicenseProviderAttribute]] = ...
    """
    
    :return: 
    """
    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, typeName: str):
        """

        :param typeName:
        """
    @overload
    def __init__(self, type: Type):
        """

        :param type:
        """
    @property
    def LicenseProvider(self) -> Type:
        """

        :return:
        """
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

class LicenseUsageMode(Enum):
    """"""

    Runtime: LicenseUsageMode = ...
    """"""
    Designtime: LicenseUsageMode = ...
    """"""

class ListBindableAttribute(Attribute, _Attribute):
    """"""

    Default: Final[ClassVar[ListBindableAttribute]] = ...
    """
    
    :return: 
    """
    No: Final[ClassVar[ListBindableAttribute]] = ...
    """
    
    :return: 
    """
    Yes: Final[ClassVar[ListBindableAttribute]] = ...
    """
    
    :return: 
    """
    @overload
    def __init__(self, flags: BindableSupport):
        """

        :param flags:
        """
    @overload
    def __init__(self, listBindable: bool):
        """

        :param listBindable:
        """
    @property
    def ListBindable(self) -> bool:
        """

        :return:
        """
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

class ListChangedEventArgs(EventArgs):
    """"""

    @overload
    def __init__(self, listChangedType: ListChangedType, propDesc: PropertyDescriptor):
        """

        :param listChangedType:
        :param propDesc:
        """
    @overload
    def __init__(self, listChangedType: ListChangedType, newIndex: int):
        """

        :param listChangedType:
        :param newIndex:
        """
    @overload
    def __init__(
        self, listChangedType: ListChangedType, newIndex: int, propDesc: PropertyDescriptor
    ):
        """

        :param listChangedType:
        :param newIndex:
        :param propDesc:
        """
    @overload
    def __init__(self, listChangedType: ListChangedType, newIndex: int, oldIndex: int):
        """

        :param listChangedType:
        :param newIndex:
        :param oldIndex:
        """
    @property
    def ListChangedType(self) -> ListChangedType:
        """

        :return:
        """
    @property
    def NewIndex(self) -> int:
        """

        :return:
        """
    @property
    def OldIndex(self) -> int:
        """

        :return:
        """
    @property
    def PropertyDescriptor(self) -> PropertyDescriptor:
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

ListChangedEventHandler: Callable[[object, ListChangedEventArgs], None] = ...
"""

:param sender: 
:param e: 
"""

class ListChangedType(Enum):
    """"""

    Reset: ListChangedType = ...
    """"""
    ItemAdded: ListChangedType = ...
    """"""
    ItemDeleted: ListChangedType = ...
    """"""
    ItemMoved: ListChangedType = ...
    """"""
    ItemChanged: ListChangedType = ...
    """"""
    PropertyDescriptorAdded: ListChangedType = ...
    """"""
    PropertyDescriptorDeleted: ListChangedType = ...
    """"""
    PropertyDescriptorChanged: ListChangedType = ...
    """"""

class ListSortDescription(Object):
    """"""

    def __init__(self, property: PropertyDescriptor, direction: ListSortDirection):
        """

        :param property:
        :param direction:
        """
    @property
    def PropertyDescriptor(self) -> PropertyDescriptor:
        """

        :return:
        """
    @PropertyDescriptor.setter
    def PropertyDescriptor(self, value: PropertyDescriptor) -> None: ...
    @property
    def SortDirection(self) -> ListSortDirection:
        """

        :return:
        """
    @SortDirection.setter
    def SortDirection(self, value: ListSortDirection) -> None: ...
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

class ListSortDescriptionCollection(Object, ICollection, IEnumerable, IList):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, sorts: Array[ListSortDescription]):
        """

        :param sorts:
        """
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
    def SyncRoot(self) -> object:
        """

        :return:
        """
    def Add(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    def Clear(self) -> None:
        """"""
    def Contains(self, value: object) -> bool:
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
    def GetType(self) -> Type:
        """

        :return:
        """
    def IndexOf(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    def Insert(self, index: int, value: object) -> None:
        """

        :param index:
        :param value:
        """
    def Remove(self, value: object) -> None:
        """

        :param value:
        """
    def RemoveAt(self, index: int) -> None:
        """

        :param index:
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
    def __getitem__(self, index: int) -> object:
        """

        :param index:
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
    @overload
    def __setitem__(self, index: int, value: ListSortDescription) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def __setitem__(self, index: int, value: object) -> None:
        """

        :param index:
        :param value:
        """

class ListSortDirection(Enum):
    """"""

    Ascending: ListSortDirection = ...
    """"""
    Descending: ListSortDirection = ...
    """"""

class LocalizableAttribute(Attribute, _Attribute):
    """"""

    Default: Final[ClassVar[LocalizableAttribute]] = ...
    """
    
    :return: 
    """
    No: Final[ClassVar[LocalizableAttribute]] = ...
    """
    
    :return: 
    """
    Yes: Final[ClassVar[LocalizableAttribute]] = ...
    """
    
    :return: 
    """
    def __init__(self, isLocalizable: bool):
        """

        :param isLocalizable:
        """
    @property
    def IsLocalizable(self) -> bool:
        """

        :return:
        """
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

class LookupBindingPropertiesAttribute(Attribute, _Attribute):
    """"""

    Default: Final[ClassVar[LookupBindingPropertiesAttribute]] = ...
    """
    
    :return: 
    """
    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, dataSource: str, displayMember: str, valueMember: str, lookupMember: str):
        """

        :param dataSource:
        :param displayMember:
        :param valueMember:
        :param lookupMember:
        """
    @property
    def DataSource(self) -> str:
        """

        :return:
        """
    @property
    def DisplayMember(self) -> str:
        """

        :return:
        """
    @property
    def LookupMember(self) -> str:
        """

        :return:
        """
    @property
    def TypeId(self) -> object:
        """

        :return:
        """
    @property
    def ValueMember(self) -> str:
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

class MarshalByValueComponent(Object, IComponent, IDisposable, IServiceProvider):
    """"""

    def __init__(self):
        """"""
    @property
    def Container(self) -> IContainer:
        """

        :return:
        """
    @property
    def DesignMode(self) -> bool:
        """

        :return:
        """
    @property
    def Site(self) -> ISite:
        """

        :return:
        """
    @Site.setter
    def Site(self, value: ISite) -> None: ...
    def Dispose(self) -> None:
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
    def GetService(self, serviceType: Type) -> object:
        """

        :param serviceType:
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
    Disposed: EventType[EventHandler] = ...
    """"""

class MaskedTextProvider(Object, ICloneable):
    """"""

    @overload
    def __init__(self, mask: str):
        """

        :param mask:
        """
    @overload
    def __init__(self, mask: str, culture: CultureInfo):
        """

        :param mask:
        :param culture:
        """
    @overload
    def __init__(self, mask: str, restrictToAscii: bool):
        """

        :param mask:
        :param restrictToAscii:
        """
    @overload
    def __init__(self, mask: str, culture: CultureInfo, restrictToAscii: bool):
        """

        :param mask:
        :param culture:
        :param restrictToAscii:
        """
    @overload
    def __init__(self, mask: str, passwordChar: Char, allowPromptAsInput: bool):
        """

        :param mask:
        :param passwordChar:
        :param allowPromptAsInput:
        """
    @overload
    def __init__(
        self, mask: str, culture: CultureInfo, passwordChar: Char, allowPromptAsInput: bool
    ):
        """

        :param mask:
        :param culture:
        :param passwordChar:
        :param allowPromptAsInput:
        """
    @overload
    def __init__(
        self,
        mask: str,
        culture: CultureInfo,
        allowPromptAsInput: bool,
        promptChar: Char,
        passwordChar: Char,
        restrictToAscii: bool,
    ):
        """

        :param mask:
        :param culture:
        :param allowPromptAsInput:
        :param promptChar:
        :param passwordChar:
        :param restrictToAscii:
        """
    @property
    def AllowPromptAsInput(self) -> bool:
        """

        :return:
        """
    @property
    def AsciiOnly(self) -> bool:
        """

        :return:
        """
    @property
    def AssignedEditPositionCount(self) -> int:
        """

        :return:
        """
    @property
    def AvailableEditPositionCount(self) -> int:
        """

        :return:
        """
    @property
    def Culture(self) -> CultureInfo:
        """

        :return:
        """
    @classmethod
    @property
    def DefaultPasswordChar(cls) -> Char:
        """

        :return:
        """
    @property
    def EditPositionCount(self) -> int:
        """

        :return:
        """
    @property
    def EditPositions(self) -> IEnumerator:
        """

        :return:
        """
    @property
    def IncludeLiterals(self) -> bool:
        """

        :return:
        """
    @IncludeLiterals.setter
    def IncludeLiterals(self, value: bool) -> None: ...
    @property
    def IncludePrompt(self) -> bool:
        """

        :return:
        """
    @IncludePrompt.setter
    def IncludePrompt(self, value: bool) -> None: ...
    @classmethod
    @property
    def InvalidIndex(cls) -> int:
        """

        :return:
        """
    @property
    def IsPassword(self) -> bool:
        """

        :return:
        """
    @IsPassword.setter
    def IsPassword(self, value: bool) -> None: ...
    @property
    def Item(self) -> Char:
        """

        :return:
        """
    @property
    def LastAssignedPosition(self) -> int:
        """

        :return:
        """
    @property
    def Length(self) -> int:
        """

        :return:
        """
    @property
    def Mask(self) -> str:
        """

        :return:
        """
    @property
    def MaskCompleted(self) -> bool:
        """

        :return:
        """
    @property
    def MaskFull(self) -> bool:
        """

        :return:
        """
    @property
    def PasswordChar(self) -> Char:
        """

        :return:
        """
    @PasswordChar.setter
    def PasswordChar(self, value: Char) -> None: ...
    @property
    def PromptChar(self) -> Char:
        """

        :return:
        """
    @PromptChar.setter
    def PromptChar(self, value: Char) -> None: ...
    @property
    def ResetOnPrompt(self) -> bool:
        """

        :return:
        """
    @ResetOnPrompt.setter
    def ResetOnPrompt(self, value: bool) -> None: ...
    @property
    def ResetOnSpace(self) -> bool:
        """

        :return:
        """
    @ResetOnSpace.setter
    def ResetOnSpace(self, value: bool) -> None: ...
    @property
    def SkipLiterals(self) -> bool:
        """

        :return:
        """
    @SkipLiterals.setter
    def SkipLiterals(self, value: bool) -> None: ...
    @overload
    def Add(self, input: Char) -> bool:
        """

        :param input:
        :return:
        """
    @overload
    def Add(self, input: str) -> bool:
        """

        :param input:
        :return:
        """
    @overload
    def Add(
        self, input: Char, testPosition: int, resultHint: MaskedTextResultHint
    ) -> Tuple[bool, int, MaskedTextResultHint]:
        """

        :param input:
        :param testPosition:
        :param resultHint:
        :return:
        """
    @overload
    def Add(
        self, input: str, testPosition: int, resultHint: MaskedTextResultHint
    ) -> Tuple[bool, int, MaskedTextResultHint]:
        """

        :param input:
        :param testPosition:
        :param resultHint:
        :return:
        """
    @overload
    def Clear(self) -> None:
        """"""
    @overload
    def Clear(self, resultHint: MaskedTextResultHint) -> Tuple[None, MaskedTextResultHint]:
        """

        :param resultHint:
        """
    def Clone(self) -> object:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def FindAssignedEditPositionFrom(self, position: int, direction: bool) -> int:
        """

        :param position:
        :param direction:
        :return:
        """
    def FindAssignedEditPositionInRange(
        self, startPosition: int, endPosition: int, direction: bool
    ) -> int:
        """

        :param startPosition:
        :param endPosition:
        :param direction:
        :return:
        """
    def FindEditPositionFrom(self, position: int, direction: bool) -> int:
        """

        :param position:
        :param direction:
        :return:
        """
    def FindEditPositionInRange(self, startPosition: int, endPosition: int, direction: bool) -> int:
        """

        :param startPosition:
        :param endPosition:
        :param direction:
        :return:
        """
    def FindNonEditPositionFrom(self, position: int, direction: bool) -> int:
        """

        :param position:
        :param direction:
        :return:
        """
    def FindNonEditPositionInRange(
        self, startPosition: int, endPosition: int, direction: bool
    ) -> int:
        """

        :param startPosition:
        :param endPosition:
        :param direction:
        :return:
        """
    def FindUnassignedEditPositionFrom(self, position: int, direction: bool) -> int:
        """

        :param position:
        :param direction:
        :return:
        """
    def FindUnassignedEditPositionInRange(
        self, startPosition: int, endPosition: int, direction: bool
    ) -> int:
        """

        :param startPosition:
        :param endPosition:
        :param direction:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @classmethod
    def GetOperationResultFromHint(cls, hint: MaskedTextResultHint) -> bool:
        """

        :param hint:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def InsertAt(self, input: Char, position: int) -> bool:
        """

        :param input:
        :param position:
        :return:
        """
    @overload
    def InsertAt(self, input: str, position: int) -> bool:
        """

        :param input:
        :param position:
        :return:
        """
    @overload
    def InsertAt(
        self, input: Char, position: int, testPosition: int, resultHint: MaskedTextResultHint
    ) -> Tuple[bool, int, MaskedTextResultHint]:
        """

        :param input:
        :param position:
        :param testPosition:
        :param resultHint:
        :return:
        """
    @overload
    def InsertAt(
        self, input: str, position: int, testPosition: int, resultHint: MaskedTextResultHint
    ) -> Tuple[bool, int, MaskedTextResultHint]:
        """

        :param input:
        :param position:
        :param testPosition:
        :param resultHint:
        :return:
        """
    def IsAvailablePosition(self, position: int) -> bool:
        """

        :param position:
        :return:
        """
    def IsEditPosition(self, position: int) -> bool:
        """

        :param position:
        :return:
        """
    @classmethod
    def IsValidInputChar(cls, c: Char) -> bool:
        """

        :param c:
        :return:
        """
    @classmethod
    def IsValidMaskChar(cls, c: Char) -> bool:
        """

        :param c:
        :return:
        """
    @classmethod
    def IsValidPasswordChar(cls, c: Char) -> bool:
        """

        :param c:
        :return:
        """
    @overload
    def Remove(self) -> bool:
        """

        :return:
        """
    @overload
    def Remove(
        self, testPosition: int, resultHint: MaskedTextResultHint
    ) -> Tuple[bool, int, MaskedTextResultHint]:
        """

        :param testPosition:
        :param resultHint:
        :return:
        """
    @overload
    def RemoveAt(self, position: int) -> bool:
        """

        :param position:
        :return:
        """
    @overload
    def RemoveAt(self, startPosition: int, endPosition: int) -> bool:
        """

        :param startPosition:
        :param endPosition:
        :return:
        """
    @overload
    def RemoveAt(
        self,
        startPosition: int,
        endPosition: int,
        testPosition: int,
        resultHint: MaskedTextResultHint,
    ) -> Tuple[bool, int, MaskedTextResultHint]:
        """

        :param startPosition:
        :param endPosition:
        :param testPosition:
        :param resultHint:
        :return:
        """
    @overload
    def Replace(self, input: Char, position: int) -> bool:
        """

        :param input:
        :param position:
        :return:
        """
    @overload
    def Replace(self, input: str, position: int) -> bool:
        """

        :param input:
        :param position:
        :return:
        """
    @overload
    def Replace(
        self, input: Char, position: int, testPosition: int, resultHint: MaskedTextResultHint
    ) -> Tuple[bool, int, MaskedTextResultHint]:
        """

        :param input:
        :param position:
        :param testPosition:
        :param resultHint:
        :return:
        """
    @overload
    def Replace(
        self, input: str, position: int, testPosition: int, resultHint: MaskedTextResultHint
    ) -> Tuple[bool, int, MaskedTextResultHint]:
        """

        :param input:
        :param position:
        :param testPosition:
        :param resultHint:
        :return:
        """
    @overload
    def Replace(
        self,
        input: Char,
        startPosition: int,
        endPosition: int,
        testPosition: int,
        resultHint: MaskedTextResultHint,
    ) -> Tuple[bool, int, MaskedTextResultHint]:
        """

        :param input:
        :param startPosition:
        :param endPosition:
        :param testPosition:
        :param resultHint:
        :return:
        """
    @overload
    def Replace(
        self,
        input: str,
        startPosition: int,
        endPosition: int,
        testPosition: int,
        resultHint: MaskedTextResultHint,
    ) -> Tuple[bool, int, MaskedTextResultHint]:
        """

        :param input:
        :param startPosition:
        :param endPosition:
        :param testPosition:
        :param resultHint:
        :return:
        """
    @overload
    def Set(self, input: str) -> bool:
        """

        :param input:
        :return:
        """
    @overload
    def Set(
        self, input: str, testPosition: int, resultHint: MaskedTextResultHint
    ) -> Tuple[bool, int, MaskedTextResultHint]:
        """

        :param input:
        :param testPosition:
        :param resultHint:
        :return:
        """
    def ToDisplayString(self) -> str:
        """

        :return:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def ToString(self, ignorePasswordChar: bool) -> str:
        """

        :param ignorePasswordChar:
        :return:
        """
    @overload
    def ToString(self, includePrompt: bool, includeLiterals: bool) -> str:
        """

        :param includePrompt:
        :param includeLiterals:
        :return:
        """
    @overload
    def ToString(self, startPosition: int, length: int) -> str:
        """

        :param startPosition:
        :param length:
        :return:
        """
    @overload
    def ToString(self, ignorePasswordChar: bool, startPosition: int, length: int) -> str:
        """

        :param ignorePasswordChar:
        :param startPosition:
        :param length:
        :return:
        """
    @overload
    def ToString(
        self, includePrompt: bool, includeLiterals: bool, startPosition: int, length: int
    ) -> str:
        """

        :param includePrompt:
        :param includeLiterals:
        :param startPosition:
        :param length:
        :return:
        """
    @overload
    def ToString(
        self,
        ignorePasswordChar: bool,
        includePrompt: bool,
        includeLiterals: bool,
        startPosition: int,
        length: int,
    ) -> str:
        """

        :param ignorePasswordChar:
        :param includePrompt:
        :param includeLiterals:
        :param startPosition:
        :param length:
        :return:
        """
    def VerifyChar(
        self, input: Char, position: int, hint: MaskedTextResultHint
    ) -> Tuple[bool, MaskedTextResultHint]:
        """

        :param input:
        :param position:
        :param hint:
        :return:
        """
    def VerifyEscapeChar(self, input: Char, position: int) -> bool:
        """

        :param input:
        :param position:
        :return:
        """
    @overload
    def VerifyString(self, input: str) -> bool:
        """

        :param input:
        :return:
        """
    @overload
    def VerifyString(
        self, input: str, testPosition: int, resultHint: MaskedTextResultHint
    ) -> Tuple[bool, int, MaskedTextResultHint]:
        """

        :param input:
        :param testPosition:
        :param resultHint:
        :return:
        """
    def __getitem__(self, index: int) -> Char:
        """

        :param index:
        :return:
        """

class MaskedTextResultHint(Enum):
    """"""

    Unknown: MaskedTextResultHint = ...
    """"""
    CharacterEscaped: MaskedTextResultHint = ...
    """"""
    NoEffect: MaskedTextResultHint = ...
    """"""
    SideEffect: MaskedTextResultHint = ...
    """"""
    Success: MaskedTextResultHint = ...
    """"""
    PositionOutOfRange: MaskedTextResultHint = ...
    """"""
    NonEditPosition: MaskedTextResultHint = ...
    """"""
    UnavailableEditPosition: MaskedTextResultHint = ...
    """"""
    PromptCharNotAllowed: MaskedTextResultHint = ...
    """"""
    InvalidInput: MaskedTextResultHint = ...
    """"""
    SignedDigitExpected: MaskedTextResultHint = ...
    """"""
    LetterExpected: MaskedTextResultHint = ...
    """"""
    DigitExpected: MaskedTextResultHint = ...
    """"""
    AlphanumericCharacterExpected: MaskedTextResultHint = ...
    """"""
    AsciiCharacterExpected: MaskedTextResultHint = ...
    """"""

class MemberDescriptor(ABC, Object):
    """"""

    @property
    def Attributes(self) -> AttributeCollection:
        """

        :return:
        """
    @property
    def Category(self) -> str:
        """

        :return:
        """
    @property
    def Description(self) -> str:
        """

        :return:
        """
    @property
    def DesignTimeOnly(self) -> bool:
        """

        :return:
        """
    @property
    def DisplayName(self) -> str:
        """

        :return:
        """
    @property
    def IsBrowsable(self) -> bool:
        """

        :return:
        """
    @property
    def Name(self) -> str:
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

class MergablePropertyAttribute(Attribute, _Attribute):
    """"""

    Default: Final[ClassVar[MergablePropertyAttribute]] = ...
    """
    
    :return: 
    """
    No: Final[ClassVar[MergablePropertyAttribute]] = ...
    """
    
    :return: 
    """
    Yes: Final[ClassVar[MergablePropertyAttribute]] = ...
    """
    
    :return: 
    """
    def __init__(self, allowMerge: bool):
        """

        :param allowMerge:
        """
    @property
    def AllowMerge(self) -> bool:
        """

        :return:
        """
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

class MultilineStringConverter(TypeConverter):
    """"""

    def __init__(self):
        """"""
    @overload
    def CanConvertFrom(self, sourceType: Type) -> bool:
        """

        :param sourceType:
        :return:
        """
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool:
        """

        :param context:
        :param sourceType:
        :return:
        """
    @overload
    def CanConvertTo(self, destinationType: Type) -> bool:
        """

        :param destinationType:
        :return:
        """
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, destinationType: Type) -> bool:
        """

        :param context:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertFrom(self, value: object) -> object:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertFrom(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> object:
        """

        :param context:
        :param culture:
        :param value:
        :return:
        """
    @overload
    def ConvertFromInvariantString(self, text: str) -> object:
        """

        :param text:
        :return:
        """
    @overload
    def ConvertFromInvariantString(self, context: ITypeDescriptorContext, text: str) -> object:
        """

        :param context:
        :param text:
        :return:
        """
    @overload
    def ConvertFromString(self, text: str) -> object:
        """

        :param text:
        :return:
        """
    @overload
    def ConvertFromString(self, context: ITypeDescriptorContext, text: str) -> object:
        """

        :param context:
        :param text:
        :return:
        """
    @overload
    def ConvertFromString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, text: str
    ) -> object:
        """

        :param context:
        :param culture:
        :param text:
        :return:
        """
    @overload
    def ConvertTo(self, value: object, destinationType: Type) -> object:
        """

        :param value:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertTo(
        self,
        context: ITypeDescriptorContext,
        culture: CultureInfo,
        value: object,
        destinationType: Type,
    ) -> object:
        """

        :param context:
        :param culture:
        :param value:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertToInvariantString(self, value: object) -> str:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertToInvariantString(self, context: ITypeDescriptorContext, value: object) -> str:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def ConvertToString(self, value: object) -> str:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertToString(self, context: ITypeDescriptorContext, value: object) -> str:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def ConvertToString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> str:
        """

        :param context:
        :param culture:
        :param value:
        :return:
        """
    @overload
    def CreateInstance(self, propertyValues: IDictionary) -> object:
        """

        :param propertyValues:
        :return:
        """
    @overload
    def CreateInstance(
        self, context: ITypeDescriptorContext, propertyValues: IDictionary
    ) -> object:
        """

        :param context:
        :param propertyValues:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetCreateInstanceSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetCreateInstanceSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetProperties(self, value: object) -> PropertyDescriptorCollection:
        """

        :param value:
        :return:
        """
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object
    ) -> PropertyDescriptorCollection:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]
    ) -> PropertyDescriptorCollection:
        """

        :param context:
        :param value:
        :param attributes:
        :return:
        """
    @overload
    def GetPropertiesSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetPropertiesSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValues(self) -> ICollection:
        """

        :return:
        """
    @overload
    def GetStandardValues(
        self, context: ITypeDescriptorContext
    ) -> TypeConverter.StandardValuesCollection:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValuesExclusive(self) -> bool:
        """

        :return:
        """
    @overload
    def GetStandardValuesExclusive(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValuesSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetStandardValuesSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def IsValid(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def IsValid(self, context: ITypeDescriptorContext, value: object) -> bool:
        """

        :param context:
        :param value:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class NestedContainer(Container, IContainer, INestedContainer, IDisposable):
    """"""

    def __init__(self, owner: IComponent):
        """

        :param owner:
        """
    @property
    def Components(self) -> ComponentCollection:
        """

        :return:
        """
    @property
    def Owner(self) -> IComponent:
        """

        :return:
        """
    @overload
    def Add(self, component: IComponent) -> None:
        """

        :param component:
        """
    @overload
    def Add(self, component: IComponent, name: str) -> None:
        """

        :param component:
        :param name:
        """
    def Dispose(self) -> None:
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
    def Remove(self, component: IComponent) -> None:
        """

        :param component:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class NotifyParentPropertyAttribute(Attribute, _Attribute):
    """"""

    Default: Final[ClassVar[NotifyParentPropertyAttribute]] = ...
    """
    
    :return: 
    """
    No: Final[ClassVar[NotifyParentPropertyAttribute]] = ...
    """
    
    :return: 
    """
    Yes: Final[ClassVar[NotifyParentPropertyAttribute]] = ...
    """
    
    :return: 
    """
    def __init__(self, notifyParent: bool):
        """

        :param notifyParent:
        """
    @property
    def NotifyParent(self) -> bool:
        """

        :return:
        """
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

class NullableConverter(TypeConverter):
    """"""

    def __init__(self, type: Type):
        """

        :param type:
        """
    @property
    def NullableType(self) -> Type:
        """

        :return:
        """
    @property
    def UnderlyingType(self) -> Type:
        """

        :return:
        """
    @property
    def UnderlyingTypeConverter(self) -> TypeConverter:
        """

        :return:
        """
    @overload
    def CanConvertFrom(self, sourceType: Type) -> bool:
        """

        :param sourceType:
        :return:
        """
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool:
        """

        :param context:
        :param sourceType:
        :return:
        """
    @overload
    def CanConvertTo(self, destinationType: Type) -> bool:
        """

        :param destinationType:
        :return:
        """
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, destinationType: Type) -> bool:
        """

        :param context:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertFrom(self, value: object) -> object:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertFrom(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> object:
        """

        :param context:
        :param culture:
        :param value:
        :return:
        """
    @overload
    def ConvertFromInvariantString(self, text: str) -> object:
        """

        :param text:
        :return:
        """
    @overload
    def ConvertFromInvariantString(self, context: ITypeDescriptorContext, text: str) -> object:
        """

        :param context:
        :param text:
        :return:
        """
    @overload
    def ConvertFromString(self, text: str) -> object:
        """

        :param text:
        :return:
        """
    @overload
    def ConvertFromString(self, context: ITypeDescriptorContext, text: str) -> object:
        """

        :param context:
        :param text:
        :return:
        """
    @overload
    def ConvertFromString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, text: str
    ) -> object:
        """

        :param context:
        :param culture:
        :param text:
        :return:
        """
    @overload
    def ConvertTo(self, value: object, destinationType: Type) -> object:
        """

        :param value:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertTo(
        self,
        context: ITypeDescriptorContext,
        culture: CultureInfo,
        value: object,
        destinationType: Type,
    ) -> object:
        """

        :param context:
        :param culture:
        :param value:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertToInvariantString(self, value: object) -> str:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertToInvariantString(self, context: ITypeDescriptorContext, value: object) -> str:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def ConvertToString(self, value: object) -> str:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertToString(self, context: ITypeDescriptorContext, value: object) -> str:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def ConvertToString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> str:
        """

        :param context:
        :param culture:
        :param value:
        :return:
        """
    @overload
    def CreateInstance(self, propertyValues: IDictionary) -> object:
        """

        :param propertyValues:
        :return:
        """
    @overload
    def CreateInstance(
        self, context: ITypeDescriptorContext, propertyValues: IDictionary
    ) -> object:
        """

        :param context:
        :param propertyValues:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetCreateInstanceSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetCreateInstanceSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetProperties(self, value: object) -> PropertyDescriptorCollection:
        """

        :param value:
        :return:
        """
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object
    ) -> PropertyDescriptorCollection:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]
    ) -> PropertyDescriptorCollection:
        """

        :param context:
        :param value:
        :param attributes:
        :return:
        """
    @overload
    def GetPropertiesSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetPropertiesSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValues(self) -> ICollection:
        """

        :return:
        """
    @overload
    def GetStandardValues(
        self, context: ITypeDescriptorContext
    ) -> TypeConverter.StandardValuesCollection:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValuesExclusive(self) -> bool:
        """

        :return:
        """
    @overload
    def GetStandardValuesExclusive(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValuesSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetStandardValuesSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def IsValid(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def IsValid(self, context: ITypeDescriptorContext, value: object) -> bool:
        """

        :param context:
        :param value:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class ParenthesizePropertyNameAttribute(Attribute, _Attribute):
    """"""

    Default: Final[ClassVar[ParenthesizePropertyNameAttribute]] = ...
    """
    
    :return: 
    """
    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, needParenthesis: bool):
        """

        :param needParenthesis:
        """
    @property
    def NeedParenthesis(self) -> bool:
        """

        :return:
        """
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

class PasswordPropertyTextAttribute(Attribute, _Attribute):
    """"""

    Default: Final[ClassVar[PasswordPropertyTextAttribute]] = ...
    """
    
    :return: 
    """
    No: Final[ClassVar[PasswordPropertyTextAttribute]] = ...
    """
    
    :return: 
    """
    Yes: Final[ClassVar[PasswordPropertyTextAttribute]] = ...
    """
    
    :return: 
    """
    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, password: bool):
        """

        :param password:
        """
    @property
    def Password(self) -> bool:
        """

        :return:
        """
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

class ProgressChangedEventArgs(EventArgs):
    """"""

    def __init__(self, progressPercentage: int, userState: object):
        """

        :param progressPercentage:
        :param userState:
        """
    @property
    def ProgressPercentage(self) -> int:
        """

        :return:
        """
    @property
    def UserState(self) -> object:
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

ProgressChangedEventHandler: Callable[[object, ProgressChangedEventArgs], None] = ...
"""

:param sender: 
:param e: 
"""

class PropertyChangedEventArgs(EventArgs):
    """"""

    def __init__(self, propertyName: str):
        """

        :param propertyName:
        """
    @property
    def PropertyName(self) -> str:
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

PropertyChangedEventHandler: Callable[[object, PropertyChangedEventArgs], None] = ...
"""

:param sender: 
:param e: 
"""

class PropertyChangingEventArgs(EventArgs):
    """"""

    def __init__(self, propertyName: str):
        """

        :param propertyName:
        """
    @property
    def PropertyName(self) -> str:
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

PropertyChangingEventHandler: Callable[[object, PropertyChangingEventArgs], None] = ...
"""

:param sender: 
:param e: 
"""

class PropertyDescriptor(ABC, MemberDescriptor):
    """"""

    @property
    def Attributes(self) -> AttributeCollection:
        """

        :return:
        """
    @property
    def Category(self) -> str:
        """

        :return:
        """
    @property
    def ComponentType(self) -> Type:
        """

        :return:
        """
    @property
    def Converter(self) -> TypeConverter:
        """

        :return:
        """
    @property
    def Description(self) -> str:
        """

        :return:
        """
    @property
    def DesignTimeOnly(self) -> bool:
        """

        :return:
        """
    @property
    def DisplayName(self) -> str:
        """

        :return:
        """
    @property
    def IsBrowsable(self) -> bool:
        """

        :return:
        """
    @property
    def IsLocalizable(self) -> bool:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def PropertyType(self) -> Type:
        """

        :return:
        """
    @property
    def SerializationVisibility(self) -> DesignerSerializationVisibility:
        """

        :return:
        """
    @property
    def SupportsChangeEvents(self) -> bool:
        """

        :return:
        """
    def AddValueChanged(self, component: object, handler: EventHandler) -> None:
        """

        :param component:
        :param handler:
        """
    def CanResetValue(self, component: object) -> bool:
        """

        :param component:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetChildProperties(self) -> PropertyDescriptorCollection:
        """

        :return:
        """
    @overload
    def GetChildProperties(self, filter: Array[Attribute]) -> PropertyDescriptorCollection:
        """

        :param filter:
        :return:
        """
    @overload
    def GetChildProperties(self, instance: object) -> PropertyDescriptorCollection:
        """

        :param instance:
        :return:
        """
    @overload
    def GetChildProperties(
        self, instance: object, filter: Array[Attribute]
    ) -> PropertyDescriptorCollection:
        """

        :param instance:
        :param filter:
        :return:
        """
    def GetEditor(self, editorBaseType: Type) -> object:
        """

        :param editorBaseType:
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
    def GetValue(self, component: object) -> object:
        """

        :param component:
        :return:
        """
    def RemoveValueChanged(self, component: object, handler: EventHandler) -> None:
        """

        :param component:
        :param handler:
        """
    def ResetValue(self, component: object) -> None:
        """

        :param component:
        """
    def SetValue(self, component: object, value: object) -> None:
        """

        :param component:
        :param value:
        """
    def ShouldSerializeValue(self, component: object) -> bool:
        """

        :param component:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class PropertyDescriptorCollection(Object, ICollection, IDictionary, IEnumerable, IList):
    """"""

    Empty: Final[ClassVar[PropertyDescriptorCollection]] = ...
    """
    
    :return: 
    """
    @overload
    def __init__(self, properties: Array[PropertyDescriptor]):
        """

        :param properties:
        """
    @overload
    def __init__(self, properties: Array[PropertyDescriptor], readOnly: bool):
        """

        :param properties:
        :param readOnly:
        """
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
    @overload
    def Add(self, value: PropertyDescriptor) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def Add(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def Add(self, key: object, value: object) -> None:
        """

        :param key:
        :param value:
        """
    @overload
    def Clear(self) -> None:
        """"""
    @overload
    def Clear(self) -> None:
        """"""
    @overload
    def Contains(self, value: PropertyDescriptor) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def Contains(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def Contains(self, key: object) -> bool:
        """

        :param key:
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
    def Find(self, name: str, ignoreCase: bool) -> PropertyDescriptor:
        """

        :param name:
        :param ignoreCase:
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
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def IndexOf(self, value: PropertyDescriptor) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def IndexOf(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def Insert(self, index: int, value: PropertyDescriptor) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def Insert(self, index: int, value: object) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def Remove(self, value: PropertyDescriptor) -> None:
        """

        :param value:
        """
    @overload
    def Remove(self, value: object) -> None:
        """

        :param value:
        """
    @overload
    def Remove(self, key: object) -> None:
        """

        :param key:
        """
    def RemoveAt(self, index: int) -> None:
        """

        :param index:
        """
    @overload
    def Sort(self) -> PropertyDescriptorCollection:
        """

        :return:
        """
    @overload
    def Sort(self, comparer: IComparer) -> PropertyDescriptorCollection:
        """

        :param comparer:
        :return:
        """
    @overload
    def Sort(self, names: Array[str]) -> PropertyDescriptorCollection:
        """

        :param names:
        :return:
        """
    @overload
    def Sort(self, names: Array[str], comparer: IComparer) -> PropertyDescriptorCollection:
        """

        :param names:
        :param comparer:
        :return:
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
    @overload
    def __getitem__(self, index: int) -> object:
        """

        :param index:
        :return:
        """
    @overload
    def __getitem__(self, key: object) -> object:
        """

        :param key:
        :return:
        """
    @overload
    def __getitem__(self, name: str) -> PropertyDescriptor:
        """

        :param name:
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
    @overload
    def __setitem__(self, index: int, value: object) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def __setitem__(self, key: object, value: object) -> None:
        """

        :param key:
        :param value:
        """

class PropertyTabAttribute(Attribute, _Attribute):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, tabClassName: str):
        """

        :param tabClassName:
        """
    @overload
    def __init__(self, tabClass: Type):
        """

        :param tabClass:
        """
    @overload
    def __init__(self, tabClassName: str, tabScope: PropertyTabScope):
        """

        :param tabClassName:
        :param tabScope:
        """
    @overload
    def __init__(self, tabClass: Type, tabScope: PropertyTabScope):
        """

        :param tabClass:
        :param tabScope:
        """
    @property
    def TabClasses(self) -> Array[Type]:
        """

        :return:
        """
    @property
    def TabScopes(self) -> Array[PropertyTabScope]:
        """

        :return:
        """
    @property
    def TypeId(self) -> object:
        """

        :return:
        """
    @overload
    def Equals(self, other: PropertyTabAttribute) -> bool:
        """

        :param other:
        :return:
        """
    @overload
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

class PropertyTabScope(Enum):
    """"""

    Static: PropertyTabScope = ...
    """"""
    Global: PropertyTabScope = ...
    """"""
    Document: PropertyTabScope = ...
    """"""
    Component: PropertyTabScope = ...
    """"""

class ProvidePropertyAttribute(Attribute, _Attribute):
    """"""

    @overload
    def __init__(self, propertyName: str, receiverTypeName: str):
        """

        :param propertyName:
        :param receiverTypeName:
        """
    @overload
    def __init__(self, propertyName: str, receiverType: Type):
        """

        :param propertyName:
        :param receiverType:
        """
    @property
    def PropertyName(self) -> str:
        """

        :return:
        """
    @property
    def ReceiverTypeName(self) -> str:
        """

        :return:
        """
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

class ReadOnlyAttribute(Attribute, _Attribute):
    """"""

    Default: Final[ClassVar[ReadOnlyAttribute]] = ...
    """
    
    :return: 
    """
    No: Final[ClassVar[ReadOnlyAttribute]] = ...
    """
    
    :return: 
    """
    Yes: Final[ClassVar[ReadOnlyAttribute]] = ...
    """
    
    :return: 
    """
    def __init__(self, isReadOnly: bool):
        """

        :param isReadOnly:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
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

class RecommendedAsConfigurableAttribute(Attribute, _Attribute):
    """"""

    Default: Final[ClassVar[RecommendedAsConfigurableAttribute]] = ...
    """
    
    :return: 
    """
    No: Final[ClassVar[RecommendedAsConfigurableAttribute]] = ...
    """
    
    :return: 
    """
    Yes: Final[ClassVar[RecommendedAsConfigurableAttribute]] = ...
    """
    
    :return: 
    """
    def __init__(self, recommendedAsConfigurable: bool):
        """

        :param recommendedAsConfigurable:
        """
    @property
    def RecommendedAsConfigurable(self) -> bool:
        """

        :return:
        """
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

class ReferenceConverter(TypeConverter):
    """"""

    def __init__(self, type: Type):
        """

        :param type:
        """
    @overload
    def CanConvertFrom(self, sourceType: Type) -> bool:
        """

        :param sourceType:
        :return:
        """
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool:
        """

        :param context:
        :param sourceType:
        :return:
        """
    @overload
    def CanConvertTo(self, destinationType: Type) -> bool:
        """

        :param destinationType:
        :return:
        """
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, destinationType: Type) -> bool:
        """

        :param context:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertFrom(self, value: object) -> object:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertFrom(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> object:
        """

        :param context:
        :param culture:
        :param value:
        :return:
        """
    @overload
    def ConvertFromInvariantString(self, text: str) -> object:
        """

        :param text:
        :return:
        """
    @overload
    def ConvertFromInvariantString(self, context: ITypeDescriptorContext, text: str) -> object:
        """

        :param context:
        :param text:
        :return:
        """
    @overload
    def ConvertFromString(self, text: str) -> object:
        """

        :param text:
        :return:
        """
    @overload
    def ConvertFromString(self, context: ITypeDescriptorContext, text: str) -> object:
        """

        :param context:
        :param text:
        :return:
        """
    @overload
    def ConvertFromString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, text: str
    ) -> object:
        """

        :param context:
        :param culture:
        :param text:
        :return:
        """
    @overload
    def ConvertTo(self, value: object, destinationType: Type) -> object:
        """

        :param value:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertTo(
        self,
        context: ITypeDescriptorContext,
        culture: CultureInfo,
        value: object,
        destinationType: Type,
    ) -> object:
        """

        :param context:
        :param culture:
        :param value:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertToInvariantString(self, value: object) -> str:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertToInvariantString(self, context: ITypeDescriptorContext, value: object) -> str:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def ConvertToString(self, value: object) -> str:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertToString(self, context: ITypeDescriptorContext, value: object) -> str:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def ConvertToString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> str:
        """

        :param context:
        :param culture:
        :param value:
        :return:
        """
    @overload
    def CreateInstance(self, propertyValues: IDictionary) -> object:
        """

        :param propertyValues:
        :return:
        """
    @overload
    def CreateInstance(
        self, context: ITypeDescriptorContext, propertyValues: IDictionary
    ) -> object:
        """

        :param context:
        :param propertyValues:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetCreateInstanceSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetCreateInstanceSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetProperties(self, value: object) -> PropertyDescriptorCollection:
        """

        :param value:
        :return:
        """
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object
    ) -> PropertyDescriptorCollection:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]
    ) -> PropertyDescriptorCollection:
        """

        :param context:
        :param value:
        :param attributes:
        :return:
        """
    @overload
    def GetPropertiesSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetPropertiesSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValues(self) -> ICollection:
        """

        :return:
        """
    @overload
    def GetStandardValues(
        self, context: ITypeDescriptorContext
    ) -> TypeConverter.StandardValuesCollection:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValuesExclusive(self) -> bool:
        """

        :return:
        """
    @overload
    def GetStandardValuesExclusive(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValuesSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetStandardValuesSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def IsValid(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def IsValid(self, context: ITypeDescriptorContext, value: object) -> bool:
        """

        :param context:
        :param value:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class ReflectEventDescriptor(EventDescriptor):
    """"""

    @overload
    def __init__(self, componentClass: Type, eventInfo: EventInfo):
        """

        :param componentClass:
        :param eventInfo:
        """
    @overload
    def __init__(
        self,
        componentType: Type,
        oldReflectEventDescriptor: EventDescriptor,
        attributes: Array[Attribute],
    ):
        """

        :param componentType:
        :param oldReflectEventDescriptor:
        :param attributes:
        """
    @overload
    def __init__(self, componentClass: Type, name: str, type: Type, attributes: Array[Attribute]):
        """

        :param componentClass:
        :param name:
        :param type:
        :param attributes:
        """
    @property
    def Attributes(self) -> AttributeCollection:
        """

        :return:
        """
    @property
    def Category(self) -> str:
        """

        :return:
        """
    @property
    def ComponentType(self) -> Type:
        """

        :return:
        """
    @property
    def Description(self) -> str:
        """

        :return:
        """
    @property
    def DesignTimeOnly(self) -> bool:
        """

        :return:
        """
    @property
    def DisplayName(self) -> str:
        """

        :return:
        """
    @property
    def EventType(self) -> Type:
        """

        :return:
        """
    @property
    def IsBrowsable(self) -> bool:
        """

        :return:
        """
    @property
    def IsMulticast(self) -> bool:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    def AddEventHandler(self, component: object, value: Delegate) -> None:
        """

        :param component:
        :param value:
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
    def RemoveEventHandler(self, component: object, value: Delegate) -> None:
        """

        :param component:
        :param value:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class ReflectPropertyDescriptor(PropertyDescriptor):
    """"""

    @overload
    def __init__(
        self,
        componentClass: Type,
        oldReflectPropertyDescriptor: PropertyDescriptor,
        attributes: Array[Attribute],
    ):
        """

        :param componentClass:
        :param oldReflectPropertyDescriptor:
        :param attributes:
        """
    @overload
    def __init__(self, componentClass: Type, name: str, type: Type, attributes: Array[Attribute]):
        """

        :param componentClass:
        :param name:
        :param type:
        :param attributes:
        """
    @overload
    def __init__(
        self,
        componentClass: Type,
        name: str,
        type: Type,
        propInfo: PropertyInfo,
        getMethod: MethodInfo,
        setMethod: MethodInfo,
        attrs: Array[Attribute],
    ):
        """

        :param componentClass:
        :param name:
        :param type:
        :param propInfo:
        :param getMethod:
        :param setMethod:
        :param attrs:
        """
    @overload
    def __init__(
        self,
        componentClass: Type,
        name: str,
        type: Type,
        receiverType: Type,
        getMethod: MethodInfo,
        setMethod: MethodInfo,
        attrs: Array[Attribute],
    ):
        """

        :param componentClass:
        :param name:
        :param type:
        :param receiverType:
        :param getMethod:
        :param setMethod:
        :param attrs:
        """
    @property
    def Attributes(self) -> AttributeCollection:
        """

        :return:
        """
    @property
    def Category(self) -> str:
        """

        :return:
        """
    @property
    def ComponentType(self) -> Type:
        """

        :return:
        """
    @property
    def Converter(self) -> TypeConverter:
        """

        :return:
        """
    @property
    def Description(self) -> str:
        """

        :return:
        """
    @property
    def DesignTimeOnly(self) -> bool:
        """

        :return:
        """
    @property
    def DisplayName(self) -> str:
        """

        :return:
        """
    @property
    def IsBrowsable(self) -> bool:
        """

        :return:
        """
    @property
    def IsLocalizable(self) -> bool:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def PropertyType(self) -> Type:
        """

        :return:
        """
    @property
    def SerializationVisibility(self) -> DesignerSerializationVisibility:
        """

        :return:
        """
    @property
    def SupportsChangeEvents(self) -> bool:
        """

        :return:
        """
    def AddValueChanged(self, component: object, handler: EventHandler) -> None:
        """

        :param component:
        :param handler:
        """
    def CanResetValue(self, component: object) -> bool:
        """

        :param component:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetChildProperties(self) -> PropertyDescriptorCollection:
        """

        :return:
        """
    @overload
    def GetChildProperties(self, filter: Array[Attribute]) -> PropertyDescriptorCollection:
        """

        :param filter:
        :return:
        """
    @overload
    def GetChildProperties(self, instance: object) -> PropertyDescriptorCollection:
        """

        :param instance:
        :return:
        """
    @overload
    def GetChildProperties(
        self, instance: object, filter: Array[Attribute]
    ) -> PropertyDescriptorCollection:
        """

        :param instance:
        :param filter:
        :return:
        """
    def GetEditor(self, editorBaseType: Type) -> object:
        """

        :param editorBaseType:
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
    def GetValue(self, component: object) -> object:
        """

        :param component:
        :return:
        """
    def RemoveValueChanged(self, component: object, handler: EventHandler) -> None:
        """

        :param component:
        :param handler:
        """
    def ResetValue(self, component: object) -> None:
        """

        :param component:
        """
    def SetValue(self, component: object, value: object) -> None:
        """

        :param component:
        :param value:
        """
    def ShouldSerializeValue(self, component: object) -> bool:
        """

        :param component:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class ReflectTypeDescriptionProvider(TypeDescriptionProvider):
    """"""

    def CreateInstance(
        self,
        provider: IServiceProvider,
        objectType: Type,
        argTypes: Array[Type],
        args: Array[object],
    ) -> object:
        """

        :param provider:
        :param objectType:
        :param argTypes:
        :param args:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetCache(self, instance: object) -> IDictionary:
        """

        :param instance:
        :return:
        """
    def GetExtendedTypeDescriptor(self, instance: object) -> ICustomTypeDescriptor:
        """

        :param instance:
        :return:
        """
    def GetFullComponentName(self, component: object) -> str:
        """

        :param component:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetReflectionType(self, instance: object) -> Type:
        """

        :param instance:
        :return:
        """
    @overload
    def GetReflectionType(self, objectType: Type) -> Type:
        """

        :param objectType:
        :return:
        """
    @overload
    def GetReflectionType(self, objectType: Type, instance: object) -> Type:
        """

        :param objectType:
        :param instance:
        :return:
        """
    def GetRuntimeType(self, reflectionType: Type) -> Type:
        """

        :param reflectionType:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetTypeDescriptor(self, instance: object) -> ICustomTypeDescriptor:
        """

        :param instance:
        :return:
        """
    @overload
    def GetTypeDescriptor(self, objectType: Type) -> ICustomTypeDescriptor:
        """

        :param objectType:
        :return:
        """
    @overload
    def GetTypeDescriptor(self, objectType: Type, instance: object) -> ICustomTypeDescriptor:
        """

        :param objectType:
        :param instance:
        :return:
        """
    def IsSupportedType(self, type: Type) -> bool:
        """

        :param type:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class RefreshEventArgs(EventArgs):
    """"""

    @overload
    def __init__(self, componentChanged: object):
        """

        :param componentChanged:
        """
    @overload
    def __init__(self, typeChanged: Type):
        """

        :param typeChanged:
        """
    @property
    def ComponentChanged(self) -> object:
        """

        :return:
        """
    @property
    def TypeChanged(self) -> Type:
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

RefreshEventHandler: Callable[[RefreshEventArgs], None] = ...
"""

:param e: 
"""

class RefreshProperties(Enum):
    """"""

    _None: RefreshProperties = ...
    """"""
    All: RefreshProperties = ...
    """"""
    Repaint: RefreshProperties = ...
    """"""

class RefreshPropertiesAttribute(Attribute, _Attribute):
    """"""

    All: Final[ClassVar[RefreshPropertiesAttribute]] = ...
    """
    
    :return: 
    """
    Default: Final[ClassVar[RefreshPropertiesAttribute]] = ...
    """
    
    :return: 
    """
    Repaint: Final[ClassVar[RefreshPropertiesAttribute]] = ...
    """
    
    :return: 
    """
    def __init__(self, refresh: RefreshProperties):
        """

        :param refresh:
        """
    @property
    def RefreshProperties(self) -> RefreshProperties:
        """

        :return:
        """
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

class RunInstallerAttribute(Attribute, _Attribute):
    """"""

    Default: Final[ClassVar[RunInstallerAttribute]] = ...
    """
    
    :return: 
    """
    No: Final[ClassVar[RunInstallerAttribute]] = ...
    """
    
    :return: 
    """
    Yes: Final[ClassVar[RunInstallerAttribute]] = ...
    """
    
    :return: 
    """
    def __init__(self, runInstaller: bool):
        """

        :param runInstaller:
        """
    @property
    def RunInstaller(self) -> bool:
        """

        :return:
        """
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

class RunWorkerCompletedEventArgs(AsyncCompletedEventArgs):
    """"""

    def __init__(self, result: object, error: Exception, cancelled: bool):
        """

        :param result:
        :param error:
        :param cancelled:
        """
    @property
    def Cancelled(self) -> bool:
        """

        :return:
        """
    @property
    def Error(self) -> Exception:
        """

        :return:
        """
    @property
    def Result(self) -> object:
        """

        :return:
        """
    @property
    def UserState(self) -> object:
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

RunWorkerCompletedEventHandler: Callable[[object, RunWorkerCompletedEventArgs], None] = ...
"""

:param sender: 
:param e: 
"""

class SByteConverter(BaseNumberConverter):
    """"""

    def __init__(self):
        """"""
    @overload
    def CanConvertFrom(self, sourceType: Type) -> bool:
        """

        :param sourceType:
        :return:
        """
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool:
        """

        :param context:
        :param sourceType:
        :return:
        """
    @overload
    def CanConvertTo(self, destinationType: Type) -> bool:
        """

        :param destinationType:
        :return:
        """
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, destinationType: Type) -> bool:
        """

        :param context:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertFrom(self, value: object) -> object:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertFrom(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> object:
        """

        :param context:
        :param culture:
        :param value:
        :return:
        """
    @overload
    def ConvertFromInvariantString(self, text: str) -> object:
        """

        :param text:
        :return:
        """
    @overload
    def ConvertFromInvariantString(self, context: ITypeDescriptorContext, text: str) -> object:
        """

        :param context:
        :param text:
        :return:
        """
    @overload
    def ConvertFromString(self, text: str) -> object:
        """

        :param text:
        :return:
        """
    @overload
    def ConvertFromString(self, context: ITypeDescriptorContext, text: str) -> object:
        """

        :param context:
        :param text:
        :return:
        """
    @overload
    def ConvertFromString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, text: str
    ) -> object:
        """

        :param context:
        :param culture:
        :param text:
        :return:
        """
    @overload
    def ConvertTo(self, value: object, destinationType: Type) -> object:
        """

        :param value:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertTo(
        self,
        context: ITypeDescriptorContext,
        culture: CultureInfo,
        value: object,
        destinationType: Type,
    ) -> object:
        """

        :param context:
        :param culture:
        :param value:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertToInvariantString(self, value: object) -> str:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertToInvariantString(self, context: ITypeDescriptorContext, value: object) -> str:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def ConvertToString(self, value: object) -> str:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertToString(self, context: ITypeDescriptorContext, value: object) -> str:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def ConvertToString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> str:
        """

        :param context:
        :param culture:
        :param value:
        :return:
        """
    @overload
    def CreateInstance(self, propertyValues: IDictionary) -> object:
        """

        :param propertyValues:
        :return:
        """
    @overload
    def CreateInstance(
        self, context: ITypeDescriptorContext, propertyValues: IDictionary
    ) -> object:
        """

        :param context:
        :param propertyValues:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetCreateInstanceSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetCreateInstanceSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetProperties(self, value: object) -> PropertyDescriptorCollection:
        """

        :param value:
        :return:
        """
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object
    ) -> PropertyDescriptorCollection:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]
    ) -> PropertyDescriptorCollection:
        """

        :param context:
        :param value:
        :param attributes:
        :return:
        """
    @overload
    def GetPropertiesSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetPropertiesSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValues(self) -> ICollection:
        """

        :return:
        """
    @overload
    def GetStandardValues(
        self, context: ITypeDescriptorContext
    ) -> TypeConverter.StandardValuesCollection:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValuesExclusive(self) -> bool:
        """

        :return:
        """
    @overload
    def GetStandardValuesExclusive(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValuesSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetStandardValuesSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def IsValid(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def IsValid(self, context: ITypeDescriptorContext, value: object) -> bool:
        """

        :param context:
        :param value:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class SettingsBindableAttribute(Attribute, _Attribute):
    """"""

    No: Final[ClassVar[SettingsBindableAttribute]] = ...
    """
    
    :return: 
    """
    Yes: Final[ClassVar[SettingsBindableAttribute]] = ...
    """
    
    :return: 
    """
    def __init__(self, bindable: bool):
        """

        :param bindable:
        """
    @property
    def Bindable(self) -> bool:
        """

        :return:
        """
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

class SingleConverter(BaseNumberConverter):
    """"""

    def __init__(self):
        """"""
    @overload
    def CanConvertFrom(self, sourceType: Type) -> bool:
        """

        :param sourceType:
        :return:
        """
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool:
        """

        :param context:
        :param sourceType:
        :return:
        """
    @overload
    def CanConvertTo(self, destinationType: Type) -> bool:
        """

        :param destinationType:
        :return:
        """
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, destinationType: Type) -> bool:
        """

        :param context:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertFrom(self, value: object) -> object:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertFrom(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> object:
        """

        :param context:
        :param culture:
        :param value:
        :return:
        """
    @overload
    def ConvertFromInvariantString(self, text: str) -> object:
        """

        :param text:
        :return:
        """
    @overload
    def ConvertFromInvariantString(self, context: ITypeDescriptorContext, text: str) -> object:
        """

        :param context:
        :param text:
        :return:
        """
    @overload
    def ConvertFromString(self, text: str) -> object:
        """

        :param text:
        :return:
        """
    @overload
    def ConvertFromString(self, context: ITypeDescriptorContext, text: str) -> object:
        """

        :param context:
        :param text:
        :return:
        """
    @overload
    def ConvertFromString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, text: str
    ) -> object:
        """

        :param context:
        :param culture:
        :param text:
        :return:
        """
    @overload
    def ConvertTo(self, value: object, destinationType: Type) -> object:
        """

        :param value:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertTo(
        self,
        context: ITypeDescriptorContext,
        culture: CultureInfo,
        value: object,
        destinationType: Type,
    ) -> object:
        """

        :param context:
        :param culture:
        :param value:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertToInvariantString(self, value: object) -> str:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertToInvariantString(self, context: ITypeDescriptorContext, value: object) -> str:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def ConvertToString(self, value: object) -> str:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertToString(self, context: ITypeDescriptorContext, value: object) -> str:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def ConvertToString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> str:
        """

        :param context:
        :param culture:
        :param value:
        :return:
        """
    @overload
    def CreateInstance(self, propertyValues: IDictionary) -> object:
        """

        :param propertyValues:
        :return:
        """
    @overload
    def CreateInstance(
        self, context: ITypeDescriptorContext, propertyValues: IDictionary
    ) -> object:
        """

        :param context:
        :param propertyValues:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetCreateInstanceSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetCreateInstanceSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetProperties(self, value: object) -> PropertyDescriptorCollection:
        """

        :param value:
        :return:
        """
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object
    ) -> PropertyDescriptorCollection:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]
    ) -> PropertyDescriptorCollection:
        """

        :param context:
        :param value:
        :param attributes:
        :return:
        """
    @overload
    def GetPropertiesSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetPropertiesSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValues(self) -> ICollection:
        """

        :return:
        """
    @overload
    def GetStandardValues(
        self, context: ITypeDescriptorContext
    ) -> TypeConverter.StandardValuesCollection:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValuesExclusive(self) -> bool:
        """

        :return:
        """
    @overload
    def GetStandardValuesExclusive(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValuesSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetStandardValuesSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def IsValid(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def IsValid(self, context: ITypeDescriptorContext, value: object) -> bool:
        """

        :param context:
        :param value:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class StringConverter(TypeConverter):
    """"""

    def __init__(self):
        """"""
    @overload
    def CanConvertFrom(self, sourceType: Type) -> bool:
        """

        :param sourceType:
        :return:
        """
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool:
        """

        :param context:
        :param sourceType:
        :return:
        """
    @overload
    def CanConvertTo(self, destinationType: Type) -> bool:
        """

        :param destinationType:
        :return:
        """
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, destinationType: Type) -> bool:
        """

        :param context:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertFrom(self, value: object) -> object:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertFrom(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> object:
        """

        :param context:
        :param culture:
        :param value:
        :return:
        """
    @overload
    def ConvertFromInvariantString(self, text: str) -> object:
        """

        :param text:
        :return:
        """
    @overload
    def ConvertFromInvariantString(self, context: ITypeDescriptorContext, text: str) -> object:
        """

        :param context:
        :param text:
        :return:
        """
    @overload
    def ConvertFromString(self, text: str) -> object:
        """

        :param text:
        :return:
        """
    @overload
    def ConvertFromString(self, context: ITypeDescriptorContext, text: str) -> object:
        """

        :param context:
        :param text:
        :return:
        """
    @overload
    def ConvertFromString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, text: str
    ) -> object:
        """

        :param context:
        :param culture:
        :param text:
        :return:
        """
    @overload
    def ConvertTo(self, value: object, destinationType: Type) -> object:
        """

        :param value:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertTo(
        self,
        context: ITypeDescriptorContext,
        culture: CultureInfo,
        value: object,
        destinationType: Type,
    ) -> object:
        """

        :param context:
        :param culture:
        :param value:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertToInvariantString(self, value: object) -> str:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertToInvariantString(self, context: ITypeDescriptorContext, value: object) -> str:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def ConvertToString(self, value: object) -> str:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertToString(self, context: ITypeDescriptorContext, value: object) -> str:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def ConvertToString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> str:
        """

        :param context:
        :param culture:
        :param value:
        :return:
        """
    @overload
    def CreateInstance(self, propertyValues: IDictionary) -> object:
        """

        :param propertyValues:
        :return:
        """
    @overload
    def CreateInstance(
        self, context: ITypeDescriptorContext, propertyValues: IDictionary
    ) -> object:
        """

        :param context:
        :param propertyValues:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetCreateInstanceSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetCreateInstanceSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetProperties(self, value: object) -> PropertyDescriptorCollection:
        """

        :param value:
        :return:
        """
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object
    ) -> PropertyDescriptorCollection:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]
    ) -> PropertyDescriptorCollection:
        """

        :param context:
        :param value:
        :param attributes:
        :return:
        """
    @overload
    def GetPropertiesSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetPropertiesSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValues(self) -> ICollection:
        """

        :return:
        """
    @overload
    def GetStandardValues(
        self, context: ITypeDescriptorContext
    ) -> TypeConverter.StandardValuesCollection:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValuesExclusive(self) -> bool:
        """

        :return:
        """
    @overload
    def GetStandardValuesExclusive(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValuesSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetStandardValuesSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def IsValid(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def IsValid(self, context: ITypeDescriptorContext, value: object) -> bool:
        """

        :param context:
        :param value:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class SyntaxCheck(ABC, Object):
    """"""

    @classmethod
    def CheckMachineName(cls, value: str) -> bool:
        """

        :param value:
        :return:
        """
    @classmethod
    def CheckPath(cls, value: str) -> bool:
        """

        :param value:
        :return:
        """
    @classmethod
    def CheckRootedPath(cls, value: str) -> bool:
        """

        :param value:
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

class TimeSpanConverter(TypeConverter):
    """"""

    def __init__(self):
        """"""
    @overload
    def CanConvertFrom(self, sourceType: Type) -> bool:
        """

        :param sourceType:
        :return:
        """
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool:
        """

        :param context:
        :param sourceType:
        :return:
        """
    @overload
    def CanConvertTo(self, destinationType: Type) -> bool:
        """

        :param destinationType:
        :return:
        """
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, destinationType: Type) -> bool:
        """

        :param context:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertFrom(self, value: object) -> object:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertFrom(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> object:
        """

        :param context:
        :param culture:
        :param value:
        :return:
        """
    @overload
    def ConvertFromInvariantString(self, text: str) -> object:
        """

        :param text:
        :return:
        """
    @overload
    def ConvertFromInvariantString(self, context: ITypeDescriptorContext, text: str) -> object:
        """

        :param context:
        :param text:
        :return:
        """
    @overload
    def ConvertFromString(self, text: str) -> object:
        """

        :param text:
        :return:
        """
    @overload
    def ConvertFromString(self, context: ITypeDescriptorContext, text: str) -> object:
        """

        :param context:
        :param text:
        :return:
        """
    @overload
    def ConvertFromString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, text: str
    ) -> object:
        """

        :param context:
        :param culture:
        :param text:
        :return:
        """
    @overload
    def ConvertTo(self, value: object, destinationType: Type) -> object:
        """

        :param value:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertTo(
        self,
        context: ITypeDescriptorContext,
        culture: CultureInfo,
        value: object,
        destinationType: Type,
    ) -> object:
        """

        :param context:
        :param culture:
        :param value:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertToInvariantString(self, value: object) -> str:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertToInvariantString(self, context: ITypeDescriptorContext, value: object) -> str:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def ConvertToString(self, value: object) -> str:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertToString(self, context: ITypeDescriptorContext, value: object) -> str:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def ConvertToString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> str:
        """

        :param context:
        :param culture:
        :param value:
        :return:
        """
    @overload
    def CreateInstance(self, propertyValues: IDictionary) -> object:
        """

        :param propertyValues:
        :return:
        """
    @overload
    def CreateInstance(
        self, context: ITypeDescriptorContext, propertyValues: IDictionary
    ) -> object:
        """

        :param context:
        :param propertyValues:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetCreateInstanceSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetCreateInstanceSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetProperties(self, value: object) -> PropertyDescriptorCollection:
        """

        :param value:
        :return:
        """
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object
    ) -> PropertyDescriptorCollection:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]
    ) -> PropertyDescriptorCollection:
        """

        :param context:
        :param value:
        :param attributes:
        :return:
        """
    @overload
    def GetPropertiesSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetPropertiesSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValues(self) -> ICollection:
        """

        :return:
        """
    @overload
    def GetStandardValues(
        self, context: ITypeDescriptorContext
    ) -> TypeConverter.StandardValuesCollection:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValuesExclusive(self) -> bool:
        """

        :return:
        """
    @overload
    def GetStandardValuesExclusive(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValuesSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetStandardValuesSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def IsValid(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def IsValid(self, context: ITypeDescriptorContext, value: object) -> bool:
        """

        :param context:
        :param value:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class ToolboxItemAttribute(Attribute, _Attribute):
    """"""

    Default: Final[ClassVar[ToolboxItemAttribute]] = ...
    """
    
    :return: 
    """
    _None: Final[ClassVar[ToolboxItemAttribute]] = ...
    """
    
    :return: 
    """
    @overload
    def __init__(self, defaultType: bool):
        """

        :param defaultType:
        """
    @overload
    def __init__(self, toolboxItemTypeName: str):
        """

        :param toolboxItemTypeName:
        """
    @overload
    def __init__(self, toolboxItemType: Type):
        """

        :param toolboxItemType:
        """
    @property
    def ToolboxItemType(self) -> Type:
        """

        :return:
        """
    @property
    def ToolboxItemTypeName(self) -> str:
        """

        :return:
        """
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

class ToolboxItemFilterAttribute(Attribute, _Attribute):
    """"""

    @overload
    def __init__(self, filterString: str):
        """

        :param filterString:
        """
    @overload
    def __init__(self, filterString: str, filterType: ToolboxItemFilterType):
        """

        :param filterString:
        :param filterType:
        """
    @property
    def FilterString(self) -> str:
        """

        :return:
        """
    @property
    def FilterType(self) -> ToolboxItemFilterType:
        """

        :return:
        """
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

class ToolboxItemFilterType(Enum):
    """"""

    Allow: ToolboxItemFilterType = ...
    """"""
    Custom: ToolboxItemFilterType = ...
    """"""
    Prevent: ToolboxItemFilterType = ...
    """"""
    Require: ToolboxItemFilterType = ...
    """"""

class TypeConverter(Object):
    """"""

    def __init__(self):
        """"""
    @overload
    def CanConvertFrom(self, sourceType: Type) -> bool:
        """

        :param sourceType:
        :return:
        """
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool:
        """

        :param context:
        :param sourceType:
        :return:
        """
    @overload
    def CanConvertTo(self, destinationType: Type) -> bool:
        """

        :param destinationType:
        :return:
        """
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, destinationType: Type) -> bool:
        """

        :param context:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertFrom(self, value: object) -> object:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertFrom(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> object:
        """

        :param context:
        :param culture:
        :param value:
        :return:
        """
    @overload
    def ConvertFromInvariantString(self, text: str) -> object:
        """

        :param text:
        :return:
        """
    @overload
    def ConvertFromInvariantString(self, context: ITypeDescriptorContext, text: str) -> object:
        """

        :param context:
        :param text:
        :return:
        """
    @overload
    def ConvertFromString(self, text: str) -> object:
        """

        :param text:
        :return:
        """
    @overload
    def ConvertFromString(self, context: ITypeDescriptorContext, text: str) -> object:
        """

        :param context:
        :param text:
        :return:
        """
    @overload
    def ConvertFromString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, text: str
    ) -> object:
        """

        :param context:
        :param culture:
        :param text:
        :return:
        """
    @overload
    def ConvertTo(self, value: object, destinationType: Type) -> object:
        """

        :param value:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertTo(
        self,
        context: ITypeDescriptorContext,
        culture: CultureInfo,
        value: object,
        destinationType: Type,
    ) -> object:
        """

        :param context:
        :param culture:
        :param value:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertToInvariantString(self, value: object) -> str:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertToInvariantString(self, context: ITypeDescriptorContext, value: object) -> str:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def ConvertToString(self, value: object) -> str:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertToString(self, context: ITypeDescriptorContext, value: object) -> str:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def ConvertToString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> str:
        """

        :param context:
        :param culture:
        :param value:
        :return:
        """
    @overload
    def CreateInstance(self, propertyValues: IDictionary) -> object:
        """

        :param propertyValues:
        :return:
        """
    @overload
    def CreateInstance(
        self, context: ITypeDescriptorContext, propertyValues: IDictionary
    ) -> object:
        """

        :param context:
        :param propertyValues:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetCreateInstanceSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetCreateInstanceSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetProperties(self, value: object) -> PropertyDescriptorCollection:
        """

        :param value:
        :return:
        """
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object
    ) -> PropertyDescriptorCollection:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]
    ) -> PropertyDescriptorCollection:
        """

        :param context:
        :param value:
        :param attributes:
        :return:
        """
    @overload
    def GetPropertiesSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetPropertiesSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValues(self) -> ICollection:
        """

        :return:
        """
    @overload
    def GetStandardValues(
        self, context: ITypeDescriptorContext
    ) -> TypeConverter.StandardValuesCollection:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValuesExclusive(self) -> bool:
        """

        :return:
        """
    @overload
    def GetStandardValuesExclusive(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValuesSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetStandardValuesSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def IsValid(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def IsValid(self, context: ITypeDescriptorContext, value: object) -> bool:
        """

        :param context:
        :param value:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

    class StandardValuesCollection(Object, ICollection, IEnumerable):
        """"""

        def __init__(self, values: ICollection):
            """"""
        @property
        def Count(self) -> int:
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
            """"""
        @property
        def SyncRoot(self) -> object:
            """

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
        def GetType(self) -> Type:
            """

            :return:
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
        def __getitem__(self, index: int) -> object:
            """"""
        def __iter__(self) -> Iterator[object]:
            """

            :return:
            """
        def __len__(self) -> int:
            """

            :return:
            """

class TypeConverterAttribute(Attribute, _Attribute):
    """"""

    Default: Final[ClassVar[TypeConverterAttribute]] = ...
    """
    
    :return: 
    """
    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, typeName: str):
        """

        :param typeName:
        """
    @overload
    def __init__(self, type: Type):
        """

        :param type:
        """
    @property
    def ConverterTypeName(self) -> str:
        """

        :return:
        """
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

class TypeDescriptionProvider(ABC, Object):
    """"""

    def CreateInstance(
        self,
        provider: IServiceProvider,
        objectType: Type,
        argTypes: Array[Type],
        args: Array[object],
    ) -> object:
        """

        :param provider:
        :param objectType:
        :param argTypes:
        :param args:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetCache(self, instance: object) -> IDictionary:
        """

        :param instance:
        :return:
        """
    def GetExtendedTypeDescriptor(self, instance: object) -> ICustomTypeDescriptor:
        """

        :param instance:
        :return:
        """
    def GetFullComponentName(self, component: object) -> str:
        """

        :param component:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetReflectionType(self, instance: object) -> Type:
        """

        :param instance:
        :return:
        """
    @overload
    def GetReflectionType(self, objectType: Type) -> Type:
        """

        :param objectType:
        :return:
        """
    @overload
    def GetReflectionType(self, objectType: Type, instance: object) -> Type:
        """

        :param objectType:
        :param instance:
        :return:
        """
    def GetRuntimeType(self, reflectionType: Type) -> Type:
        """

        :param reflectionType:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetTypeDescriptor(self, instance: object) -> ICustomTypeDescriptor:
        """

        :param instance:
        :return:
        """
    @overload
    def GetTypeDescriptor(self, objectType: Type) -> ICustomTypeDescriptor:
        """

        :param objectType:
        :return:
        """
    @overload
    def GetTypeDescriptor(self, objectType: Type, instance: object) -> ICustomTypeDescriptor:
        """

        :param objectType:
        :param instance:
        :return:
        """
    def IsSupportedType(self, type: Type) -> bool:
        """

        :param type:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class TypeDescriptionProviderAttribute(Attribute, _Attribute):
    """"""

    @overload
    def __init__(self, typeName: str):
        """

        :param typeName:
        """
    @overload
    def __init__(self, type: Type):
        """

        :param type:
        """
    @property
    def TypeId(self) -> object:
        """

        :return:
        """
    @property
    def TypeName(self) -> str:
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

class TypeDescriptor(Object):
    """"""

    @classmethod
    @property
    def ComNativeDescriptorHandler(cls) -> IComNativeDescriptorHandler:
        """

        :return:
        """
    @classmethod
    @ComNativeDescriptorHandler.setter
    def ComNativeDescriptorHandler(cls, value: IComNativeDescriptorHandler) -> None: ...
    @classmethod
    @property
    def ComObjectType(cls) -> Type:
        """

        :return:
        """
    @classmethod
    @property
    def InterfaceType(cls) -> Type:
        """

        :return:
        """
    @classmethod
    @overload
    def AddAttributes(
        cls, instance: object, attributes: Array[Attribute]
    ) -> TypeDescriptionProvider:
        """

        :param instance:
        :param attributes:
        :return:
        """
    @classmethod
    @overload
    def AddAttributes(cls, type: Type, attributes: Array[Attribute]) -> TypeDescriptionProvider:
        """

        :param type:
        :param attributes:
        :return:
        """
    @classmethod
    def AddEditorTable(cls, editorBaseType: Type, table: Hashtable) -> None:
        """

        :param editorBaseType:
        :param table:
        """
    @classmethod
    @overload
    def AddProvider(cls, provider: TypeDescriptionProvider, instance: object) -> None:
        """

        :param provider:
        :param instance:
        """
    @classmethod
    @overload
    def AddProvider(cls, provider: TypeDescriptionProvider, type: Type) -> None:
        """

        :param provider:
        :param type:
        """
    @classmethod
    @overload
    def AddProviderTransparent(cls, provider: TypeDescriptionProvider, instance: object) -> None:
        """

        :param provider:
        :param instance:
        """
    @classmethod
    @overload
    def AddProviderTransparent(cls, provider: TypeDescriptionProvider, type: Type) -> None:
        """

        :param provider:
        :param type:
        """
    @classmethod
    def CreateAssociation(cls, primary: object, secondary: object) -> None:
        """

        :param primary:
        :param secondary:
        """
    @classmethod
    def CreateDesigner(cls, component: IComponent, designerBaseType: Type) -> IDesigner:
        """

        :param component:
        :param designerBaseType:
        :return:
        """
    @classmethod
    @overload
    def CreateEvent(
        cls, componentType: Type, oldEventDescriptor: EventDescriptor, attributes: Array[Attribute]
    ) -> EventDescriptor:
        """

        :param componentType:
        :param oldEventDescriptor:
        :param attributes:
        :return:
        """
    @classmethod
    @overload
    def CreateEvent(
        cls, componentType: Type, name: str, type: Type, attributes: Array[Attribute]
    ) -> EventDescriptor:
        """

        :param componentType:
        :param name:
        :param type:
        :param attributes:
        :return:
        """
    @classmethod
    def CreateInstance(
        cls,
        provider: IServiceProvider,
        objectType: Type,
        argTypes: Array[Type],
        args: Array[object],
    ) -> object:
        """

        :param provider:
        :param objectType:
        :param argTypes:
        :param args:
        :return:
        """
    @classmethod
    @overload
    def CreateProperty(
        cls,
        componentType: Type,
        oldPropertyDescriptor: PropertyDescriptor,
        attributes: Array[Attribute],
    ) -> PropertyDescriptor:
        """

        :param componentType:
        :param oldPropertyDescriptor:
        :param attributes:
        :return:
        """
    @classmethod
    @overload
    def CreateProperty(
        cls, componentType: Type, name: str, type: Type, attributes: Array[Attribute]
    ) -> PropertyDescriptor:
        """

        :param componentType:
        :param name:
        :param type:
        :param attributes:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @classmethod
    def GetAssociation(cls, type: Type, primary: object) -> object:
        """

        :param type:
        :param primary:
        :return:
        """
    @classmethod
    @overload
    def GetAttributes(cls, component: object) -> AttributeCollection:
        """

        :param component:
        :return:
        """
    @classmethod
    @overload
    def GetAttributes(cls, componentType: Type) -> AttributeCollection:
        """

        :param componentType:
        :return:
        """
    @classmethod
    @overload
    def GetAttributes(cls, component: object, noCustomTypeDesc: bool) -> AttributeCollection:
        """

        :param component:
        :param noCustomTypeDesc:
        :return:
        """
    @classmethod
    @overload
    def GetClassName(cls, component: object) -> str:
        """

        :param component:
        :return:
        """
    @classmethod
    @overload
    def GetClassName(cls, componentType: Type) -> str:
        """

        :param componentType:
        :return:
        """
    @classmethod
    @overload
    def GetClassName(cls, component: object, noCustomTypeDesc: bool) -> str:
        """

        :param component:
        :param noCustomTypeDesc:
        :return:
        """
    @classmethod
    @overload
    def GetComponentName(cls, component: object) -> str:
        """

        :param component:
        :return:
        """
    @classmethod
    @overload
    def GetComponentName(cls, component: object, noCustomTypeDesc: bool) -> str:
        """

        :param component:
        :param noCustomTypeDesc:
        :return:
        """
    @classmethod
    @overload
    def GetConverter(cls, component: object) -> TypeConverter:
        """

        :param component:
        :return:
        """
    @classmethod
    @overload
    def GetConverter(cls, type: Type) -> TypeConverter:
        """

        :param type:
        :return:
        """
    @classmethod
    @overload
    def GetConverter(cls, component: object, noCustomTypeDesc: bool) -> TypeConverter:
        """

        :param component:
        :param noCustomTypeDesc:
        :return:
        """
    @classmethod
    @overload
    def GetDefaultEvent(cls, component: object) -> EventDescriptor:
        """

        :param component:
        :return:
        """
    @classmethod
    @overload
    def GetDefaultEvent(cls, componentType: Type) -> EventDescriptor:
        """

        :param componentType:
        :return:
        """
    @classmethod
    @overload
    def GetDefaultEvent(cls, component: object, noCustomTypeDesc: bool) -> EventDescriptor:
        """

        :param component:
        :param noCustomTypeDesc:
        :return:
        """
    @classmethod
    @overload
    def GetDefaultProperty(cls, component: object) -> PropertyDescriptor:
        """

        :param component:
        :return:
        """
    @classmethod
    @overload
    def GetDefaultProperty(cls, componentType: Type) -> PropertyDescriptor:
        """

        :param componentType:
        :return:
        """
    @classmethod
    @overload
    def GetDefaultProperty(cls, component: object, noCustomTypeDesc: bool) -> PropertyDescriptor:
        """

        :param component:
        :param noCustomTypeDesc:
        :return:
        """
    @classmethod
    @overload
    def GetEditor(cls, component: object, editorBaseType: Type) -> object:
        """

        :param component:
        :param editorBaseType:
        :return:
        """
    @classmethod
    @overload
    def GetEditor(cls, type: Type, editorBaseType: Type) -> object:
        """

        :param type:
        :param editorBaseType:
        :return:
        """
    @classmethod
    @overload
    def GetEditor(cls, component: object, editorBaseType: Type, noCustomTypeDesc: bool) -> object:
        """

        :param component:
        :param editorBaseType:
        :param noCustomTypeDesc:
        :return:
        """
    @classmethod
    @overload
    def GetEvents(cls, component: object) -> EventDescriptorCollection:
        """

        :param component:
        :return:
        """
    @classmethod
    @overload
    def GetEvents(cls, componentType: Type) -> EventDescriptorCollection:
        """

        :param componentType:
        :return:
        """
    @classmethod
    @overload
    def GetEvents(
        cls, component: object, attributes: Array[Attribute]
    ) -> EventDescriptorCollection:
        """

        :param component:
        :param attributes:
        :return:
        """
    @classmethod
    @overload
    def GetEvents(cls, component: object, noCustomTypeDesc: bool) -> EventDescriptorCollection:
        """

        :param component:
        :param noCustomTypeDesc:
        :return:
        """
    @classmethod
    @overload
    def GetEvents(
        cls, componentType: Type, attributes: Array[Attribute]
    ) -> EventDescriptorCollection:
        """

        :param componentType:
        :param attributes:
        :return:
        """
    @classmethod
    @overload
    def GetEvents(
        cls, component: object, attributes: Array[Attribute], noCustomTypeDesc: bool
    ) -> EventDescriptorCollection:
        """

        :param component:
        :param attributes:
        :param noCustomTypeDesc:
        :return:
        """
    @classmethod
    def GetFullComponentName(cls, component: object) -> str:
        """

        :param component:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @classmethod
    @overload
    def GetProperties(cls, component: object) -> PropertyDescriptorCollection:
        """

        :param component:
        :return:
        """
    @classmethod
    @overload
    def GetProperties(cls, componentType: Type) -> PropertyDescriptorCollection:
        """

        :param componentType:
        :return:
        """
    @classmethod
    @overload
    def GetProperties(
        cls, component: object, attributes: Array[Attribute]
    ) -> PropertyDescriptorCollection:
        """

        :param component:
        :param attributes:
        :return:
        """
    @classmethod
    @overload
    def GetProperties(
        cls, component: object, noCustomTypeDesc: bool
    ) -> PropertyDescriptorCollection:
        """

        :param component:
        :param noCustomTypeDesc:
        :return:
        """
    @classmethod
    @overload
    def GetProperties(
        cls, componentType: Type, attributes: Array[Attribute]
    ) -> PropertyDescriptorCollection:
        """

        :param componentType:
        :param attributes:
        :return:
        """
    @classmethod
    @overload
    def GetProperties(
        cls, component: object, attributes: Array[Attribute], noCustomTypeDesc: bool
    ) -> PropertyDescriptorCollection:
        """

        :param component:
        :param attributes:
        :param noCustomTypeDesc:
        :return:
        """
    @classmethod
    @overload
    def GetProvider(cls, instance: object) -> TypeDescriptionProvider:
        """

        :param instance:
        :return:
        """
    @classmethod
    @overload
    def GetProvider(cls, type: Type) -> TypeDescriptionProvider:
        """

        :param type:
        :return:
        """
    @classmethod
    @overload
    def GetReflectionType(cls, instance: object) -> Type:
        """

        :param instance:
        :return:
        """
    @classmethod
    @overload
    def GetReflectionType(cls, type: Type) -> Type:
        """

        :param type:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @classmethod
    @overload
    def Refresh(cls, assembly: Assembly) -> None:
        """

        :param assembly:
        """
    @classmethod
    @overload
    def Refresh(cls, module: Module) -> None:
        """

        :param module:
        """
    @classmethod
    @overload
    def Refresh(cls, component: object) -> None:
        """

        :param component:
        """
    @classmethod
    @overload
    def Refresh(cls, type: Type) -> None:
        """

        :param type:
        """
    @classmethod
    def RemoveAssociation(cls, primary: object, secondary: object) -> None:
        """

        :param primary:
        :param secondary:
        """
    @classmethod
    def RemoveAssociations(cls, primary: object) -> None:
        """

        :param primary:
        """
    @classmethod
    @overload
    def RemoveProvider(cls, provider: TypeDescriptionProvider, instance: object) -> None:
        """

        :param provider:
        :param instance:
        """
    @classmethod
    @overload
    def RemoveProvider(cls, provider: TypeDescriptionProvider, type: Type) -> None:
        """

        :param provider:
        :param type:
        """
    @classmethod
    @overload
    def RemoveProviderTransparent(cls, provider: TypeDescriptionProvider, instance: object) -> None:
        """

        :param provider:
        :param instance:
        """
    @classmethod
    @overload
    def RemoveProviderTransparent(cls, provider: TypeDescriptionProvider, type: Type) -> None:
        """

        :param provider:
        :param type:
        """
    @classmethod
    def SortDescriptorArray(cls, infos: IList) -> None:
        """

        :param infos:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    Refreshed: EventType[RefreshEventHandler] = ...
    """"""

class TypeListConverter(ABC, TypeConverter):
    """"""

    @overload
    def CanConvertFrom(self, sourceType: Type) -> bool:
        """

        :param sourceType:
        :return:
        """
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool:
        """

        :param context:
        :param sourceType:
        :return:
        """
    @overload
    def CanConvertTo(self, destinationType: Type) -> bool:
        """

        :param destinationType:
        :return:
        """
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, destinationType: Type) -> bool:
        """

        :param context:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertFrom(self, value: object) -> object:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertFrom(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> object:
        """

        :param context:
        :param culture:
        :param value:
        :return:
        """
    @overload
    def ConvertFromInvariantString(self, text: str) -> object:
        """

        :param text:
        :return:
        """
    @overload
    def ConvertFromInvariantString(self, context: ITypeDescriptorContext, text: str) -> object:
        """

        :param context:
        :param text:
        :return:
        """
    @overload
    def ConvertFromString(self, text: str) -> object:
        """

        :param text:
        :return:
        """
    @overload
    def ConvertFromString(self, context: ITypeDescriptorContext, text: str) -> object:
        """

        :param context:
        :param text:
        :return:
        """
    @overload
    def ConvertFromString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, text: str
    ) -> object:
        """

        :param context:
        :param culture:
        :param text:
        :return:
        """
    @overload
    def ConvertTo(self, value: object, destinationType: Type) -> object:
        """

        :param value:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertTo(
        self,
        context: ITypeDescriptorContext,
        culture: CultureInfo,
        value: object,
        destinationType: Type,
    ) -> object:
        """

        :param context:
        :param culture:
        :param value:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertToInvariantString(self, value: object) -> str:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertToInvariantString(self, context: ITypeDescriptorContext, value: object) -> str:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def ConvertToString(self, value: object) -> str:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertToString(self, context: ITypeDescriptorContext, value: object) -> str:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def ConvertToString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> str:
        """

        :param context:
        :param culture:
        :param value:
        :return:
        """
    @overload
    def CreateInstance(self, propertyValues: IDictionary) -> object:
        """

        :param propertyValues:
        :return:
        """
    @overload
    def CreateInstance(
        self, context: ITypeDescriptorContext, propertyValues: IDictionary
    ) -> object:
        """

        :param context:
        :param propertyValues:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetCreateInstanceSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetCreateInstanceSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetProperties(self, value: object) -> PropertyDescriptorCollection:
        """

        :param value:
        :return:
        """
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object
    ) -> PropertyDescriptorCollection:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]
    ) -> PropertyDescriptorCollection:
        """

        :param context:
        :param value:
        :param attributes:
        :return:
        """
    @overload
    def GetPropertiesSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetPropertiesSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValues(self) -> ICollection:
        """

        :return:
        """
    @overload
    def GetStandardValues(
        self, context: ITypeDescriptorContext
    ) -> TypeConverter.StandardValuesCollection:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValuesExclusive(self) -> bool:
        """

        :return:
        """
    @overload
    def GetStandardValuesExclusive(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValuesSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetStandardValuesSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def IsValid(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def IsValid(self, context: ITypeDescriptorContext, value: object) -> bool:
        """

        :param context:
        :param value:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class UInt16Converter(BaseNumberConverter):
    """"""

    def __init__(self):
        """"""
    @overload
    def CanConvertFrom(self, sourceType: Type) -> bool:
        """

        :param sourceType:
        :return:
        """
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool:
        """

        :param context:
        :param sourceType:
        :return:
        """
    @overload
    def CanConvertTo(self, destinationType: Type) -> bool:
        """

        :param destinationType:
        :return:
        """
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, destinationType: Type) -> bool:
        """

        :param context:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertFrom(self, value: object) -> object:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertFrom(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> object:
        """

        :param context:
        :param culture:
        :param value:
        :return:
        """
    @overload
    def ConvertFromInvariantString(self, text: str) -> object:
        """

        :param text:
        :return:
        """
    @overload
    def ConvertFromInvariantString(self, context: ITypeDescriptorContext, text: str) -> object:
        """

        :param context:
        :param text:
        :return:
        """
    @overload
    def ConvertFromString(self, text: str) -> object:
        """

        :param text:
        :return:
        """
    @overload
    def ConvertFromString(self, context: ITypeDescriptorContext, text: str) -> object:
        """

        :param context:
        :param text:
        :return:
        """
    @overload
    def ConvertFromString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, text: str
    ) -> object:
        """

        :param context:
        :param culture:
        :param text:
        :return:
        """
    @overload
    def ConvertTo(self, value: object, destinationType: Type) -> object:
        """

        :param value:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertTo(
        self,
        context: ITypeDescriptorContext,
        culture: CultureInfo,
        value: object,
        destinationType: Type,
    ) -> object:
        """

        :param context:
        :param culture:
        :param value:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertToInvariantString(self, value: object) -> str:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertToInvariantString(self, context: ITypeDescriptorContext, value: object) -> str:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def ConvertToString(self, value: object) -> str:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertToString(self, context: ITypeDescriptorContext, value: object) -> str:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def ConvertToString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> str:
        """

        :param context:
        :param culture:
        :param value:
        :return:
        """
    @overload
    def CreateInstance(self, propertyValues: IDictionary) -> object:
        """

        :param propertyValues:
        :return:
        """
    @overload
    def CreateInstance(
        self, context: ITypeDescriptorContext, propertyValues: IDictionary
    ) -> object:
        """

        :param context:
        :param propertyValues:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetCreateInstanceSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetCreateInstanceSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetProperties(self, value: object) -> PropertyDescriptorCollection:
        """

        :param value:
        :return:
        """
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object
    ) -> PropertyDescriptorCollection:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]
    ) -> PropertyDescriptorCollection:
        """

        :param context:
        :param value:
        :param attributes:
        :return:
        """
    @overload
    def GetPropertiesSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetPropertiesSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValues(self) -> ICollection:
        """

        :return:
        """
    @overload
    def GetStandardValues(
        self, context: ITypeDescriptorContext
    ) -> TypeConverter.StandardValuesCollection:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValuesExclusive(self) -> bool:
        """

        :return:
        """
    @overload
    def GetStandardValuesExclusive(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValuesSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetStandardValuesSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def IsValid(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def IsValid(self, context: ITypeDescriptorContext, value: object) -> bool:
        """

        :param context:
        :param value:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class UInt32Converter(BaseNumberConverter):
    """"""

    def __init__(self):
        """"""
    @overload
    def CanConvertFrom(self, sourceType: Type) -> bool:
        """

        :param sourceType:
        :return:
        """
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool:
        """

        :param context:
        :param sourceType:
        :return:
        """
    @overload
    def CanConvertTo(self, destinationType: Type) -> bool:
        """

        :param destinationType:
        :return:
        """
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, destinationType: Type) -> bool:
        """

        :param context:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertFrom(self, value: object) -> object:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertFrom(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> object:
        """

        :param context:
        :param culture:
        :param value:
        :return:
        """
    @overload
    def ConvertFromInvariantString(self, text: str) -> object:
        """

        :param text:
        :return:
        """
    @overload
    def ConvertFromInvariantString(self, context: ITypeDescriptorContext, text: str) -> object:
        """

        :param context:
        :param text:
        :return:
        """
    @overload
    def ConvertFromString(self, text: str) -> object:
        """

        :param text:
        :return:
        """
    @overload
    def ConvertFromString(self, context: ITypeDescriptorContext, text: str) -> object:
        """

        :param context:
        :param text:
        :return:
        """
    @overload
    def ConvertFromString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, text: str
    ) -> object:
        """

        :param context:
        :param culture:
        :param text:
        :return:
        """
    @overload
    def ConvertTo(self, value: object, destinationType: Type) -> object:
        """

        :param value:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertTo(
        self,
        context: ITypeDescriptorContext,
        culture: CultureInfo,
        value: object,
        destinationType: Type,
    ) -> object:
        """

        :param context:
        :param culture:
        :param value:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertToInvariantString(self, value: object) -> str:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertToInvariantString(self, context: ITypeDescriptorContext, value: object) -> str:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def ConvertToString(self, value: object) -> str:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertToString(self, context: ITypeDescriptorContext, value: object) -> str:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def ConvertToString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> str:
        """

        :param context:
        :param culture:
        :param value:
        :return:
        """
    @overload
    def CreateInstance(self, propertyValues: IDictionary) -> object:
        """

        :param propertyValues:
        :return:
        """
    @overload
    def CreateInstance(
        self, context: ITypeDescriptorContext, propertyValues: IDictionary
    ) -> object:
        """

        :param context:
        :param propertyValues:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetCreateInstanceSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetCreateInstanceSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetProperties(self, value: object) -> PropertyDescriptorCollection:
        """

        :param value:
        :return:
        """
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object
    ) -> PropertyDescriptorCollection:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]
    ) -> PropertyDescriptorCollection:
        """

        :param context:
        :param value:
        :param attributes:
        :return:
        """
    @overload
    def GetPropertiesSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetPropertiesSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValues(self) -> ICollection:
        """

        :return:
        """
    @overload
    def GetStandardValues(
        self, context: ITypeDescriptorContext
    ) -> TypeConverter.StandardValuesCollection:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValuesExclusive(self) -> bool:
        """

        :return:
        """
    @overload
    def GetStandardValuesExclusive(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValuesSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetStandardValuesSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def IsValid(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def IsValid(self, context: ITypeDescriptorContext, value: object) -> bool:
        """

        :param context:
        :param value:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class UInt64Converter(BaseNumberConverter):
    """"""

    def __init__(self):
        """"""
    @overload
    def CanConvertFrom(self, sourceType: Type) -> bool:
        """

        :param sourceType:
        :return:
        """
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool:
        """

        :param context:
        :param sourceType:
        :return:
        """
    @overload
    def CanConvertTo(self, destinationType: Type) -> bool:
        """

        :param destinationType:
        :return:
        """
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, destinationType: Type) -> bool:
        """

        :param context:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertFrom(self, value: object) -> object:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertFrom(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> object:
        """

        :param context:
        :param culture:
        :param value:
        :return:
        """
    @overload
    def ConvertFromInvariantString(self, text: str) -> object:
        """

        :param text:
        :return:
        """
    @overload
    def ConvertFromInvariantString(self, context: ITypeDescriptorContext, text: str) -> object:
        """

        :param context:
        :param text:
        :return:
        """
    @overload
    def ConvertFromString(self, text: str) -> object:
        """

        :param text:
        :return:
        """
    @overload
    def ConvertFromString(self, context: ITypeDescriptorContext, text: str) -> object:
        """

        :param context:
        :param text:
        :return:
        """
    @overload
    def ConvertFromString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, text: str
    ) -> object:
        """

        :param context:
        :param culture:
        :param text:
        :return:
        """
    @overload
    def ConvertTo(self, value: object, destinationType: Type) -> object:
        """

        :param value:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertTo(
        self,
        context: ITypeDescriptorContext,
        culture: CultureInfo,
        value: object,
        destinationType: Type,
    ) -> object:
        """

        :param context:
        :param culture:
        :param value:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertToInvariantString(self, value: object) -> str:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertToInvariantString(self, context: ITypeDescriptorContext, value: object) -> str:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def ConvertToString(self, value: object) -> str:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertToString(self, context: ITypeDescriptorContext, value: object) -> str:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def ConvertToString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> str:
        """

        :param context:
        :param culture:
        :param value:
        :return:
        """
    @overload
    def CreateInstance(self, propertyValues: IDictionary) -> object:
        """

        :param propertyValues:
        :return:
        """
    @overload
    def CreateInstance(
        self, context: ITypeDescriptorContext, propertyValues: IDictionary
    ) -> object:
        """

        :param context:
        :param propertyValues:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetCreateInstanceSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetCreateInstanceSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetProperties(self, value: object) -> PropertyDescriptorCollection:
        """

        :param value:
        :return:
        """
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object
    ) -> PropertyDescriptorCollection:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]
    ) -> PropertyDescriptorCollection:
        """

        :param context:
        :param value:
        :param attributes:
        :return:
        """
    @overload
    def GetPropertiesSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetPropertiesSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValues(self) -> ICollection:
        """

        :return:
        """
    @overload
    def GetStandardValues(
        self, context: ITypeDescriptorContext
    ) -> TypeConverter.StandardValuesCollection:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValuesExclusive(self) -> bool:
        """

        :return:
        """
    @overload
    def GetStandardValuesExclusive(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValuesSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetStandardValuesSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def IsValid(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def IsValid(self, context: ITypeDescriptorContext, value: object) -> bool:
        """

        :param context:
        :param value:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class WarningException(SystemException, _Exception, ISerializable):
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
    @overload
    def __init__(self, message: str, helpUrl: str):
        """

        :param message:
        :param helpUrl:
        """
    @overload
    def __init__(self, message: str, helpUrl: str, helpTopic: str):
        """

        :param message:
        :param helpUrl:
        :param helpTopic:
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
    def HelpTopic(self) -> str:
        """

        :return:
        """
    @property
    def HelpUrl(self) -> str:
        """

        :return:
        """
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

class WeakHashtable(
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
    def SetWeak(self, key: object, value: object) -> None:
        """

        :param key:
        :param value:
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

class Win32Exception(ExternalException, _Exception, ISerializable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, error: int):
        """

        :param error:
        """
    @overload
    def __init__(self, message: str):
        """

        :param message:
        """
    @overload
    def __init__(self, error: int, message: str):
        """

        :param error:
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
    def ErrorCode(self) -> int:
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
    def NativeErrorCode(self) -> int:
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
