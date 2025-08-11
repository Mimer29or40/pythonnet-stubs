"""Automatically generated stubs for C# namespace: System.ComponentModel."""

from abc import ABC
from collections.abc import Callable
from collections.abc import Iterator
from typing import ClassVar
from typing import Self
from typing import overload

from System import ArgumentException
from System import Array
from System import Attribute
from System import Boolean
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
from System import Int32
from System import IntPtr
from System import IServiceProvider
from System import MarshalByRefObject
from System import Object
from System import String
from System import SystemException
from System import Type
from System import UInt32
from System.Collections import Hashtable
from System.Collections import ICollection
from System.Collections import IComparer
from System.Collections import IDictionary
from System.Collections import IDictionaryEnumerator
from System.Collections import IEnumerable
from System.Collections import IEnumerator
from System.Collections import IList
from System.Collections import ReadOnlyCollectionBase
from System.Collections.Generic import ICollection
from System.Collections.Generic import IEnumerable
from System.Collections.Generic import IEnumerator
from System.Collections.Generic import IList
from System.Collections.Generic import IReadOnlyCollection
from System.Collections.Generic import IReadOnlyList
from System.Collections.ObjectModel import Collection
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

from .Design import IDesigner

class EventType[T]:
    def __iadd__(self, other: T) -> Self: ...
    def __isub__(self, other: T) -> Self: ...

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class AddingNewEventArgs(EventArgs):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, newObject: object) -> None:
        """"""
    @property
    def NewObject(self) -> object:
        """"""
    @NewObject.setter
    def NewObject(self, value: object) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

type AddingNewEventHandler = Callable[[object, AddingNewEventArgs], None]
""""""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class AmbientValueAttribute(Attribute, _Attribute):
    """"""
    @overload
    def __init__(self, type: Type, value: str) -> None:
        """"""
    @overload
    def __init__(self, value: Char) -> None:
        """"""
    @overload
    def __init__(self, value: int) -> None:
        """"""
    @overload
    def __init__(self, value: int) -> None:
        """"""
    @overload
    def __init__(self, value: int) -> None:
        """"""
    @overload
    def __init__(self, value: int) -> None:
        """"""
    @overload
    def __init__(self, value: float) -> None:
        """"""
    @overload
    def __init__(self, value: float) -> None:
        """"""
    @overload
    def __init__(self, value: bool) -> None:
        """"""
    @overload
    def __init__(self, value: str) -> None:
        """"""
    @overload
    def __init__(self, value: object) -> None:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
    @property
    def Value(self) -> object:
        """"""
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ArrayConverter(CollectionConverter):
    """"""
    def __init__(self) -> None:
        """"""
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool:
        """"""
    @overload
    def CanConvertFrom(self, sourceType: Type) -> bool:
        """"""
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, destinationType: Type) -> bool:
        """"""
    @overload
    def CanConvertTo(self, destinationType: Type) -> bool:
        """"""
    @overload
    def ConvertFrom(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> object:
        """"""
    @overload
    def ConvertFrom(self, value: object) -> object:
        """"""
    @overload
    def ConvertFromInvariantString(self, context: ITypeDescriptorContext, text: str) -> object:
        """"""
    @overload
    def ConvertFromInvariantString(self, text: str) -> object:
        """"""
    @overload
    def ConvertFromString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, text: str
    ) -> object:
        """"""
    @overload
    def ConvertFromString(self, context: ITypeDescriptorContext, text: str) -> object:
        """"""
    @overload
    def ConvertFromString(self, text: str) -> object:
        """"""
    @overload
    def ConvertTo(
        self,
        context: ITypeDescriptorContext,
        culture: CultureInfo,
        value: object,
        destinationType: Type,
    ) -> object:
        """"""
    @overload
    def ConvertTo(self, value: object, destinationType: Type) -> object:
        """"""
    @overload
    def ConvertToInvariantString(self, context: ITypeDescriptorContext, value: object) -> str:
        """"""
    @overload
    def ConvertToInvariantString(self, value: object) -> str:
        """"""
    @overload
    def ConvertToString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> str:
        """"""
    @overload
    def ConvertToString(self, context: ITypeDescriptorContext, value: object) -> str:
        """"""
    @overload
    def ConvertToString(self, value: object) -> str:
        """"""
    @overload
    def CreateInstance(self, propertyValues: IDictionary) -> object:
        """"""
    @overload
    def CreateInstance(
        self, context: ITypeDescriptorContext, propertyValues: IDictionary
    ) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetCreateInstanceSupported(self) -> bool:
        """"""
    @overload
    def GetCreateInstanceSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object
    ) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]
    ) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetProperties(self, value: object) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetPropertiesSupported(self) -> bool:
        """"""
    @overload
    def GetPropertiesSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    @overload
    def GetStandardValues(self) -> ICollection:
        """"""
    @overload
    def GetStandardValues(
        self, context: ITypeDescriptorContext
    ) -> TypeConverter.StandardValuesCollection:
        """"""
    @overload
    def GetStandardValuesExclusive(self) -> bool:
        """"""
    @overload
    def GetStandardValuesExclusive(self, context: ITypeDescriptorContext) -> bool:
        """"""
    @overload
    def GetStandardValuesSupported(self) -> bool:
        """"""
    @overload
    def GetStandardValuesSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IsValid(self, context: ITypeDescriptorContext, value: object) -> bool:
        """"""
    @overload
    def IsValid(self, value: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    # noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
    class StandardValuesCollection(Object, ICollection, IEnumerable):
        """"""
        def __init__(self, values: ICollection) -> None:
            """"""
        @property
        def Count(self) -> int:
            """"""
        @property
        def IsSynchronized(self) -> bool:
            """"""
        @property
        def Item(self) -> object:
            """"""
        @property
        def SyncRoot(self) -> object:
            """"""
        def CopyTo(self, array: Array, index: int) -> None:
            """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def GetEnumerator(self) -> IEnumerator:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def ToString(self) -> str:
            """"""
        def __iter__(self) -> Iterator:
            """"""
        def __len__(self) -> int:
            """"""
        def __getitem__(self, index: int) -> object:
            """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ArraySubsetEnumerator(Object, IEnumerator):
    """"""
    def __init__(self, array: Array, count: int) -> None:
        """"""
    @property
    def Current(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def MoveNext(self) -> bool:
        """"""
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class AsyncCompletedEventArgs(EventArgs):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, error: Exception, cancelled: bool, userState: object) -> None:
        """"""
    @property
    def Cancelled(self) -> bool:
        """"""
    @property
    def Error(self) -> Exception:
        """"""
    @property
    def UserState(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

type AsyncCompletedEventHandler = Callable[[object, AsyncCompletedEventArgs], None]
""""""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class AsyncOperation(Object):
    """"""
    @property
    def SynchronizationContext(self) -> SynchronizationContext:
        """"""
    @property
    def UserSuppliedState(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def OperationCompleted(self) -> None:
        """"""
    def Post(self, d: SendOrPostCallback, arg: object) -> None:
        """"""
    def PostOperationCompleted(self, d: SendOrPostCallback, arg: object) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class AsyncOperationManager(ABC, Object):
    """"""
    @classmethod
    @property
    def SynchronizationContext(cls) -> SynchronizationContext:
        """"""
    @classmethod
    @SynchronizationContext.setter
    def SynchronizationContext(cls, value: SynchronizationContext) -> None: ...
    @classmethod
    def CreateOperation(cls, userSuppliedState: object) -> AsyncOperation:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class AttributeCollection(Object, ICollection, IEnumerable):
    """"""

    Empty: ClassVar[AttributeCollection]
    """"""
    def __init__(self, attributes: Array[Attribute]) -> None:
        """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def Item(self) -> Attribute:
        """"""
    @property
    def SyncRoot(self) -> object:
        """"""
    @overload
    def Contains(self, attributes: Array[Attribute]) -> bool:
        """"""
    @overload
    def Contains(self, attribute: Attribute) -> bool:
        """"""
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def FromExisting(
        cls, existing: AttributeCollection, newAttributes: Array[Attribute]
    ) -> AttributeCollection:
        """"""
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def Matches(self, attributes: Array[Attribute]) -> bool:
        """"""
    @overload
    def Matches(self, attribute: Attribute) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __contains__(self, attributes: Array[Attribute]) -> bool:
        """"""
    @overload
    def __contains__(self, attribute: Attribute) -> bool:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    def __len__(self) -> int:
        """"""
    @overload
    def __getitem__(self, index: int) -> Attribute:
        """"""
    @overload
    def __getitem__(self, attributeType: Type) -> Attribute:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class AttributeProviderAttribute(Attribute, _Attribute):
    """"""
    @overload
    def __init__(self, typeName: str) -> None:
        """"""
    @overload
    def __init__(self, typeName: str, propertyName: str) -> None:
        """"""
    @overload
    def __init__(self, type: Type) -> None:
        """"""
    @property
    def PropertyName(self) -> str:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
    @property
    def TypeName(self) -> str:
        """"""
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class BackgroundWorker(Component, IComponent, IDisposable):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def CancellationPending(self) -> bool:
        """"""
    @property
    def Container(self) -> IContainer:
        """"""
    @property
    def IsBusy(self) -> bool:
        """"""
    @property
    def Site(self) -> ISite:
        """"""
    @Site.setter
    def Site(self, value: ISite) -> None: ...
    @property
    def WorkerReportsProgress(self) -> bool:
        """"""
    @WorkerReportsProgress.setter
    def WorkerReportsProgress(self, value: bool) -> None: ...
    @property
    def WorkerSupportsCancellation(self) -> bool:
        """"""
    @WorkerSupportsCancellation.setter
    def WorkerSupportsCancellation(self, value: bool) -> None: ...
    def CancelAsync(self) -> None:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetLifetimeService(self) -> object:
        """"""
    def GetType(self) -> Type:
        """"""
    def InitializeLifetimeService(self) -> object:
        """"""
    @overload
    def ReportProgress(self, percentProgress: int) -> None:
        """"""
    @overload
    def ReportProgress(self, percentProgress: int, userState: object) -> None:
        """"""
    @overload
    def RunWorkerAsync(self) -> None:
        """"""
    @overload
    def RunWorkerAsync(self, argument: object) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    Disposed: EventType[EventHandler] = ...
    """"""
    DoWork: EventType[DoWorkEventHandler] = ...
    """"""
    ProgressChanged: EventType[ProgressChangedEventHandler] = ...
    """"""
    RunWorkerCompleted: EventType[RunWorkerCompletedEventHandler] = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class BaseNumberConverter(ABC, TypeConverter):
    """"""
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool:
        """"""
    @overload
    def CanConvertFrom(self, sourceType: Type) -> bool:
        """"""
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, t: Type) -> bool:
        """"""
    @overload
    def CanConvertTo(self, destinationType: Type) -> bool:
        """"""
    @overload
    def ConvertFrom(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> object:
        """"""
    @overload
    def ConvertFrom(self, value: object) -> object:
        """"""
    @overload
    def ConvertFromInvariantString(self, context: ITypeDescriptorContext, text: str) -> object:
        """"""
    @overload
    def ConvertFromInvariantString(self, text: str) -> object:
        """"""
    @overload
    def ConvertFromString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, text: str
    ) -> object:
        """"""
    @overload
    def ConvertFromString(self, context: ITypeDescriptorContext, text: str) -> object:
        """"""
    @overload
    def ConvertFromString(self, text: str) -> object:
        """"""
    @overload
    def ConvertTo(
        self,
        context: ITypeDescriptorContext,
        culture: CultureInfo,
        value: object,
        destinationType: Type,
    ) -> object:
        """"""
    @overload
    def ConvertTo(self, value: object, destinationType: Type) -> object:
        """"""
    @overload
    def ConvertToInvariantString(self, context: ITypeDescriptorContext, value: object) -> str:
        """"""
    @overload
    def ConvertToInvariantString(self, value: object) -> str:
        """"""
    @overload
    def ConvertToString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> str:
        """"""
    @overload
    def ConvertToString(self, context: ITypeDescriptorContext, value: object) -> str:
        """"""
    @overload
    def ConvertToString(self, value: object) -> str:
        """"""
    @overload
    def CreateInstance(self, propertyValues: IDictionary) -> object:
        """"""
    @overload
    def CreateInstance(
        self, context: ITypeDescriptorContext, propertyValues: IDictionary
    ) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetCreateInstanceSupported(self) -> bool:
        """"""
    @overload
    def GetCreateInstanceSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object
    ) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]
    ) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetProperties(self, value: object) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetPropertiesSupported(self) -> bool:
        """"""
    @overload
    def GetPropertiesSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    @overload
    def GetStandardValues(self) -> ICollection:
        """"""
    @overload
    def GetStandardValues(
        self, context: ITypeDescriptorContext
    ) -> TypeConverter.StandardValuesCollection:
        """"""
    @overload
    def GetStandardValuesExclusive(self) -> bool:
        """"""
    @overload
    def GetStandardValuesExclusive(self, context: ITypeDescriptorContext) -> bool:
        """"""
    @overload
    def GetStandardValuesSupported(self) -> bool:
        """"""
    @overload
    def GetStandardValuesSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IsValid(self, context: ITypeDescriptorContext, value: object) -> bool:
        """"""
    @overload
    def IsValid(self, value: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    # noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
    class StandardValuesCollection(Object, ICollection, IEnumerable):
        """"""
        def __init__(self, values: ICollection) -> None:
            """"""
        @property
        def Count(self) -> int:
            """"""
        @property
        def IsSynchronized(self) -> bool:
            """"""
        @property
        def Item(self) -> object:
            """"""
        @property
        def SyncRoot(self) -> object:
            """"""
        def CopyTo(self, array: Array, index: int) -> None:
            """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def GetEnumerator(self) -> IEnumerator:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def ToString(self) -> str:
            """"""
        def __iter__(self) -> Iterator:
            """"""
        def __len__(self) -> int:
            """"""
        def __getitem__(self, index: int) -> object:
            """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class BindableAttribute(Attribute, _Attribute):
    """"""

    Default: ClassVar[BindableAttribute]
    """"""
    No: ClassVar[BindableAttribute]
    """"""
    Yes: ClassVar[BindableAttribute]
    """"""
    @overload
    def __init__(self, bindable: bool) -> None:
        """"""
    @overload
    def __init__(self, bindable: bool, direction: BindingDirection) -> None:
        """"""
    @overload
    def __init__(self, flags: BindableSupport) -> None:
        """"""
    @overload
    def __init__(self, flags: BindableSupport, direction: BindingDirection) -> None:
        """"""
    @property
    def Bindable(self) -> bool:
        """"""
    @property
    def Direction(self) -> BindingDirection:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
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

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class BindableSupport(Enum):
    """"""

    No: BindableSupport = ...
    """"""
    Yes: BindableSupport = ...
    """"""
    Default: BindableSupport = ...
    """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class BindingDirection(Enum):
    """"""

    OneWay: BindingDirection = ...
    """"""
    TwoWay: BindingDirection = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class BindingList[T](
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
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, list: IList[T]) -> None:
        """"""
    @property
    def AllowEdit(self) -> bool:
        """"""
    @AllowEdit.setter
    def AllowEdit(self, value: bool) -> None: ...
    @property
    def AllowNew(self) -> bool:
        """"""
    @AllowNew.setter
    def AllowNew(self, value: bool) -> None: ...
    @property
    def AllowRemove(self) -> bool:
        """"""
    @AllowRemove.setter
    def AllowRemove(self, value: bool) -> None: ...
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsFixedSize(self) -> bool:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def IsSorted(self) -> bool:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def Item(self) -> T:
        """"""
    @Item.setter
    def Item(self, value: T) -> None: ...
    @property
    def RaiseListChangedEvents(self) -> bool:
        """"""
    @RaiseListChangedEvents.setter
    def RaiseListChangedEvents(self, value: bool) -> None: ...
    @property
    def RaisesItemChangedEvents(self) -> bool:
        """"""
    @property
    def SortDirection(self) -> ListSortDirection:
        """"""
    @property
    def SortProperty(self) -> PropertyDescriptor:
        """"""
    @property
    def SupportsChangeNotification(self) -> bool:
        """"""
    @property
    def SupportsSearching(self) -> bool:
        """"""
    @property
    def SupportsSorting(self) -> bool:
        """"""
    @property
    def SyncRoot(self) -> object:
        """"""
    @overload
    def Add(self, item: T) -> None:
        """"""
    @overload
    def Add(self, value: object) -> int:
        """"""
    def AddIndex(self, property: PropertyDescriptor) -> None:
        """"""
    def AddNew[T](self) -> T:
        """"""
    def ApplySort(self, property: PropertyDescriptor, direction: ListSortDirection) -> None:
        """"""
    def CancelNew(self, itemIndex: int) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    @overload
    def Contains(self, item: T) -> bool:
        """"""
    @overload
    def Contains(self, value: object) -> bool:
        """"""
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array[T], index: int) -> None:
        """"""
    def EndNew(self, itemIndex: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Find(self, property: PropertyDescriptor, key: object) -> int:
        """"""
    def GetEnumerator[T](self) -> IEnumerator[T]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IndexOf(self, item: T) -> int:
        """"""
    @overload
    def IndexOf(self, value: object) -> int:
        """"""
    @overload
    def Insert(self, index: int, item: T) -> None:
        """"""
    @overload
    def Insert(self, index: int, value: object) -> None:
        """"""
    @overload
    def Remove(self, item: T) -> bool:
        """"""
    @overload
    def Remove(self, value: object) -> None:
        """"""
    def RemoveAt(self, index: int) -> None:
        """"""
    def RemoveIndex(self, property: PropertyDescriptor) -> None:
        """"""
    def RemoveSort(self) -> None:
        """"""
    def ResetBindings(self) -> None:
        """"""
    def ResetItem(self, position: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __contains__(self, item: T) -> bool:
        """"""
    @overload
    def __contains__(self, value: object) -> bool:
        """"""
    def __iter__[T](self) -> Iterator[T]:
        """"""
    @overload
    def __delitem__(self, item: T) -> bool:
        """"""
    @overload
    def __delitem__(self, value: object) -> None:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__[T](self, index: int) -> T:
        """"""
    @overload
    def __setitem__(self, index: int, value: T) -> None:
        """"""
    @overload
    def __setitem__(self, index: int, value: object) -> None:
        """"""
    AddingNew: EventType[AddingNewEventHandler] = ...
    """"""
    ListChanged: EventType[ListChangedEventHandler] = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class BooleanConverter(TypeConverter):
    """"""
    def __init__(self) -> None:
        """"""
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool:
        """"""
    @overload
    def CanConvertFrom(self, sourceType: Type) -> bool:
        """"""
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, destinationType: Type) -> bool:
        """"""
    @overload
    def CanConvertTo(self, destinationType: Type) -> bool:
        """"""
    @overload
    def ConvertFrom(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> object:
        """"""
    @overload
    def ConvertFrom(self, value: object) -> object:
        """"""
    @overload
    def ConvertFromInvariantString(self, context: ITypeDescriptorContext, text: str) -> object:
        """"""
    @overload
    def ConvertFromInvariantString(self, text: str) -> object:
        """"""
    @overload
    def ConvertFromString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, text: str
    ) -> object:
        """"""
    @overload
    def ConvertFromString(self, context: ITypeDescriptorContext, text: str) -> object:
        """"""
    @overload
    def ConvertFromString(self, text: str) -> object:
        """"""
    @overload
    def ConvertTo(
        self,
        context: ITypeDescriptorContext,
        culture: CultureInfo,
        value: object,
        destinationType: Type,
    ) -> object:
        """"""
    @overload
    def ConvertTo(self, value: object, destinationType: Type) -> object:
        """"""
    @overload
    def ConvertToInvariantString(self, context: ITypeDescriptorContext, value: object) -> str:
        """"""
    @overload
    def ConvertToInvariantString(self, value: object) -> str:
        """"""
    @overload
    def ConvertToString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> str:
        """"""
    @overload
    def ConvertToString(self, context: ITypeDescriptorContext, value: object) -> str:
        """"""
    @overload
    def ConvertToString(self, value: object) -> str:
        """"""
    @overload
    def CreateInstance(self, propertyValues: IDictionary) -> object:
        """"""
    @overload
    def CreateInstance(
        self, context: ITypeDescriptorContext, propertyValues: IDictionary
    ) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetCreateInstanceSupported(self) -> bool:
        """"""
    @overload
    def GetCreateInstanceSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object
    ) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]
    ) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetProperties(self, value: object) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetPropertiesSupported(self) -> bool:
        """"""
    @overload
    def GetPropertiesSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    @overload
    def GetStandardValues(self) -> ICollection:
        """"""
    @overload
    def GetStandardValues(
        self, context: ITypeDescriptorContext
    ) -> TypeConverter.StandardValuesCollection:
        """"""
    @overload
    def GetStandardValuesExclusive(self) -> bool:
        """"""
    @overload
    def GetStandardValuesExclusive(self, context: ITypeDescriptorContext) -> bool:
        """"""
    @overload
    def GetStandardValuesSupported(self) -> bool:
        """"""
    @overload
    def GetStandardValuesSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IsValid(self, context: ITypeDescriptorContext, value: object) -> bool:
        """"""
    @overload
    def IsValid(self, value: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    # noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
    class StandardValuesCollection(Object, ICollection, IEnumerable):
        """"""
        def __init__(self, values: ICollection) -> None:
            """"""
        @property
        def Count(self) -> int:
            """"""
        @property
        def IsSynchronized(self) -> bool:
            """"""
        @property
        def Item(self) -> object:
            """"""
        @property
        def SyncRoot(self) -> object:
            """"""
        def CopyTo(self, array: Array, index: int) -> None:
            """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def GetEnumerator(self) -> IEnumerator:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def ToString(self) -> str:
            """"""
        def __iter__(self) -> Iterator:
            """"""
        def __len__(self) -> int:
            """"""
        def __getitem__(self, index: int) -> object:
            """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class BrowsableAttribute(Attribute, _Attribute):
    """"""

    Default: ClassVar[BrowsableAttribute]
    """"""
    No: ClassVar[BrowsableAttribute]
    """"""
    Yes: ClassVar[BrowsableAttribute]
    """"""
    def __init__(self, browsable: bool) -> None:
        """"""
    @property
    def Browsable(self) -> bool:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ByteConverter(BaseNumberConverter):
    """"""
    def __init__(self) -> None:
        """"""
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool:
        """"""
    @overload
    def CanConvertFrom(self, sourceType: Type) -> bool:
        """"""
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, t: Type) -> bool:
        """"""
    @overload
    def CanConvertTo(self, destinationType: Type) -> bool:
        """"""
    @overload
    def ConvertFrom(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> object:
        """"""
    @overload
    def ConvertFrom(self, value: object) -> object:
        """"""
    @overload
    def ConvertFromInvariantString(self, context: ITypeDescriptorContext, text: str) -> object:
        """"""
    @overload
    def ConvertFromInvariantString(self, text: str) -> object:
        """"""
    @overload
    def ConvertFromString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, text: str
    ) -> object:
        """"""
    @overload
    def ConvertFromString(self, context: ITypeDescriptorContext, text: str) -> object:
        """"""
    @overload
    def ConvertFromString(self, text: str) -> object:
        """"""
    @overload
    def ConvertTo(
        self,
        context: ITypeDescriptorContext,
        culture: CultureInfo,
        value: object,
        destinationType: Type,
    ) -> object:
        """"""
    @overload
    def ConvertTo(self, value: object, destinationType: Type) -> object:
        """"""
    @overload
    def ConvertToInvariantString(self, context: ITypeDescriptorContext, value: object) -> str:
        """"""
    @overload
    def ConvertToInvariantString(self, value: object) -> str:
        """"""
    @overload
    def ConvertToString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> str:
        """"""
    @overload
    def ConvertToString(self, context: ITypeDescriptorContext, value: object) -> str:
        """"""
    @overload
    def ConvertToString(self, value: object) -> str:
        """"""
    @overload
    def CreateInstance(self, propertyValues: IDictionary) -> object:
        """"""
    @overload
    def CreateInstance(
        self, context: ITypeDescriptorContext, propertyValues: IDictionary
    ) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetCreateInstanceSupported(self) -> bool:
        """"""
    @overload
    def GetCreateInstanceSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object
    ) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]
    ) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetProperties(self, value: object) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetPropertiesSupported(self) -> bool:
        """"""
    @overload
    def GetPropertiesSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    @overload
    def GetStandardValues(self) -> ICollection:
        """"""
    @overload
    def GetStandardValues(
        self, context: ITypeDescriptorContext
    ) -> TypeConverter.StandardValuesCollection:
        """"""
    @overload
    def GetStandardValuesExclusive(self) -> bool:
        """"""
    @overload
    def GetStandardValuesExclusive(self, context: ITypeDescriptorContext) -> bool:
        """"""
    @overload
    def GetStandardValuesSupported(self) -> bool:
        """"""
    @overload
    def GetStandardValuesSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IsValid(self, context: ITypeDescriptorContext, value: object) -> bool:
        """"""
    @overload
    def IsValid(self, value: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    # noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
    class StandardValuesCollection(Object, ICollection, IEnumerable):
        """"""
        def __init__(self, values: ICollection) -> None:
            """"""
        @property
        def Count(self) -> int:
            """"""
        @property
        def IsSynchronized(self) -> bool:
            """"""
        @property
        def Item(self) -> object:
            """"""
        @property
        def SyncRoot(self) -> object:
            """"""
        def CopyTo(self, array: Array, index: int) -> None:
            """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def GetEnumerator(self) -> IEnumerator:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def ToString(self) -> str:
            """"""
        def __iter__(self) -> Iterator:
            """"""
        def __len__(self) -> int:
            """"""
        def __getitem__(self, index: int) -> object:
            """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CancelEventArgs(EventArgs):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, cancel: bool) -> None:
        """"""
    @property
    def Cancel(self) -> bool:
        """"""
    @Cancel.setter
    def Cancel(self, value: bool) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

type CancelEventHandler = Callable[[object, CancelEventArgs], None]
""""""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CategoryAttribute(Attribute, _Attribute):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, category: str) -> None:
        """"""
    @classmethod
    @property
    def Action(cls) -> CategoryAttribute:
        """"""
    @classmethod
    @property
    def Appearance(cls) -> CategoryAttribute:
        """"""
    @classmethod
    @property
    def Asynchronous(cls) -> CategoryAttribute:
        """"""
    @classmethod
    @property
    def Behavior(cls) -> CategoryAttribute:
        """"""
    @property
    def Category(self) -> str:
        """"""
    @classmethod
    @property
    def Data(cls) -> CategoryAttribute:
        """"""
    @classmethod
    @property
    def Default(cls) -> CategoryAttribute:
        """"""
    @classmethod
    @property
    def Design(cls) -> CategoryAttribute:
        """"""
    @classmethod
    @property
    def DragDrop(cls) -> CategoryAttribute:
        """"""
    @classmethod
    @property
    def Focus(cls) -> CategoryAttribute:
        """"""
    @classmethod
    @property
    def Format(cls) -> CategoryAttribute:
        """"""
    @classmethod
    @property
    def Key(cls) -> CategoryAttribute:
        """"""
    @classmethod
    @property
    def Layout(cls) -> CategoryAttribute:
        """"""
    @classmethod
    @property
    def Mouse(cls) -> CategoryAttribute:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
    @classmethod
    @property
    def WindowStyle(cls) -> CategoryAttribute:
        """"""
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CharConverter(TypeConverter):
    """"""
    def __init__(self) -> None:
        """"""
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool:
        """"""
    @overload
    def CanConvertFrom(self, sourceType: Type) -> bool:
        """"""
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, destinationType: Type) -> bool:
        """"""
    @overload
    def CanConvertTo(self, destinationType: Type) -> bool:
        """"""
    @overload
    def ConvertFrom(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> object:
        """"""
    @overload
    def ConvertFrom(self, value: object) -> object:
        """"""
    @overload
    def ConvertFromInvariantString(self, context: ITypeDescriptorContext, text: str) -> object:
        """"""
    @overload
    def ConvertFromInvariantString(self, text: str) -> object:
        """"""
    @overload
    def ConvertFromString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, text: str
    ) -> object:
        """"""
    @overload
    def ConvertFromString(self, context: ITypeDescriptorContext, text: str) -> object:
        """"""
    @overload
    def ConvertFromString(self, text: str) -> object:
        """"""
    @overload
    def ConvertTo(
        self,
        context: ITypeDescriptorContext,
        culture: CultureInfo,
        value: object,
        destinationType: Type,
    ) -> object:
        """"""
    @overload
    def ConvertTo(self, value: object, destinationType: Type) -> object:
        """"""
    @overload
    def ConvertToInvariantString(self, context: ITypeDescriptorContext, value: object) -> str:
        """"""
    @overload
    def ConvertToInvariantString(self, value: object) -> str:
        """"""
    @overload
    def ConvertToString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> str:
        """"""
    @overload
    def ConvertToString(self, context: ITypeDescriptorContext, value: object) -> str:
        """"""
    @overload
    def ConvertToString(self, value: object) -> str:
        """"""
    @overload
    def CreateInstance(self, propertyValues: IDictionary) -> object:
        """"""
    @overload
    def CreateInstance(
        self, context: ITypeDescriptorContext, propertyValues: IDictionary
    ) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetCreateInstanceSupported(self) -> bool:
        """"""
    @overload
    def GetCreateInstanceSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object
    ) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]
    ) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetProperties(self, value: object) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetPropertiesSupported(self) -> bool:
        """"""
    @overload
    def GetPropertiesSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    @overload
    def GetStandardValues(self) -> ICollection:
        """"""
    @overload
    def GetStandardValues(
        self, context: ITypeDescriptorContext
    ) -> TypeConverter.StandardValuesCollection:
        """"""
    @overload
    def GetStandardValuesExclusive(self) -> bool:
        """"""
    @overload
    def GetStandardValuesExclusive(self, context: ITypeDescriptorContext) -> bool:
        """"""
    @overload
    def GetStandardValuesSupported(self) -> bool:
        """"""
    @overload
    def GetStandardValuesSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IsValid(self, context: ITypeDescriptorContext, value: object) -> bool:
        """"""
    @overload
    def IsValid(self, value: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    # noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
    class StandardValuesCollection(Object, ICollection, IEnumerable):
        """"""
        def __init__(self, values: ICollection) -> None:
            """"""
        @property
        def Count(self) -> int:
            """"""
        @property
        def IsSynchronized(self) -> bool:
            """"""
        @property
        def Item(self) -> object:
            """"""
        @property
        def SyncRoot(self) -> object:
            """"""
        def CopyTo(self, array: Array, index: int) -> None:
            """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def GetEnumerator(self) -> IEnumerator:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def ToString(self) -> str:
            """"""
        def __iter__(self) -> Iterator:
            """"""
        def __len__(self) -> int:
            """"""
        def __getitem__(self, index: int) -> object:
            """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class CollectionChangeAction(Enum):
    """"""

    Add: CollectionChangeAction = ...
    """"""
    Remove: CollectionChangeAction = ...
    """"""
    Refresh: CollectionChangeAction = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CollectionChangeEventArgs(EventArgs):
    """"""
    def __init__(self, action: CollectionChangeAction, element: object) -> None:
        """"""
    @property
    def Action(self) -> CollectionChangeAction:
        """"""
    @property
    def Element(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

type CollectionChangeEventHandler = Callable[[object, CollectionChangeEventArgs], None]
""""""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CollectionConverter(TypeConverter):
    """"""
    def __init__(self) -> None:
        """"""
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool:
        """"""
    @overload
    def CanConvertFrom(self, sourceType: Type) -> bool:
        """"""
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, destinationType: Type) -> bool:
        """"""
    @overload
    def CanConvertTo(self, destinationType: Type) -> bool:
        """"""
    @overload
    def ConvertFrom(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> object:
        """"""
    @overload
    def ConvertFrom(self, value: object) -> object:
        """"""
    @overload
    def ConvertFromInvariantString(self, context: ITypeDescriptorContext, text: str) -> object:
        """"""
    @overload
    def ConvertFromInvariantString(self, text: str) -> object:
        """"""
    @overload
    def ConvertFromString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, text: str
    ) -> object:
        """"""
    @overload
    def ConvertFromString(self, context: ITypeDescriptorContext, text: str) -> object:
        """"""
    @overload
    def ConvertFromString(self, text: str) -> object:
        """"""
    @overload
    def ConvertTo(
        self,
        context: ITypeDescriptorContext,
        culture: CultureInfo,
        value: object,
        destinationType: Type,
    ) -> object:
        """"""
    @overload
    def ConvertTo(self, value: object, destinationType: Type) -> object:
        """"""
    @overload
    def ConvertToInvariantString(self, context: ITypeDescriptorContext, value: object) -> str:
        """"""
    @overload
    def ConvertToInvariantString(self, value: object) -> str:
        """"""
    @overload
    def ConvertToString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> str:
        """"""
    @overload
    def ConvertToString(self, context: ITypeDescriptorContext, value: object) -> str:
        """"""
    @overload
    def ConvertToString(self, value: object) -> str:
        """"""
    @overload
    def CreateInstance(self, propertyValues: IDictionary) -> object:
        """"""
    @overload
    def CreateInstance(
        self, context: ITypeDescriptorContext, propertyValues: IDictionary
    ) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetCreateInstanceSupported(self) -> bool:
        """"""
    @overload
    def GetCreateInstanceSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object
    ) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]
    ) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetProperties(self, value: object) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetPropertiesSupported(self) -> bool:
        """"""
    @overload
    def GetPropertiesSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    @overload
    def GetStandardValues(self) -> ICollection:
        """"""
    @overload
    def GetStandardValues(
        self, context: ITypeDescriptorContext
    ) -> TypeConverter.StandardValuesCollection:
        """"""
    @overload
    def GetStandardValuesExclusive(self) -> bool:
        """"""
    @overload
    def GetStandardValuesExclusive(self, context: ITypeDescriptorContext) -> bool:
        """"""
    @overload
    def GetStandardValuesSupported(self) -> bool:
        """"""
    @overload
    def GetStandardValuesSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IsValid(self, context: ITypeDescriptorContext, value: object) -> bool:
        """"""
    @overload
    def IsValid(self, value: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    # noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
    class StandardValuesCollection(Object, ICollection, IEnumerable):
        """"""
        def __init__(self, values: ICollection) -> None:
            """"""
        @property
        def Count(self) -> int:
            """"""
        @property
        def IsSynchronized(self) -> bool:
            """"""
        @property
        def Item(self) -> object:
            """"""
        @property
        def SyncRoot(self) -> object:
            """"""
        def CopyTo(self, array: Array, index: int) -> None:
            """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def GetEnumerator(self) -> IEnumerator:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def ToString(self) -> str:
            """"""
        def __iter__(self) -> Iterator:
            """"""
        def __len__(self) -> int:
            """"""
        def __getitem__(self, index: int) -> object:
            """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CompModSwitches(ABC, Object):
    """"""
    @classmethod
    @property
    def CommonDesignerServices(cls) -> BooleanSwitch:
        """"""
    @classmethod
    @property
    def EventLog(cls) -> TraceSwitch:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ComplexBindingPropertiesAttribute(Attribute, _Attribute):
    """"""

    Default: ClassVar[ComplexBindingPropertiesAttribute]
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, dataSource: str) -> None:
        """"""
    @overload
    def __init__(self, dataSource: str, dataMember: str) -> None:
        """"""
    @property
    def DataMember(self) -> str:
        """"""
    @property
    def DataSource(self) -> str:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class Component(MarshalByRefObject, IComponent, IDisposable):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Container(self) -> IContainer:
        """"""
    @property
    def Site(self) -> ISite:
        """"""
    @Site.setter
    def Site(self, value: ISite) -> None: ...
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetLifetimeService(self) -> object:
        """"""
    def GetType(self) -> Type:
        """"""
    def InitializeLifetimeService(self) -> object:
        """"""
    def ToString(self) -> str:
        """"""
    Disposed: EventType[EventHandler] = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ComponentCollection(ReadOnlyCollectionBase, ICollection, IEnumerable):
    """"""
    def __init__(self, components: Array[IComponent]) -> None:
        """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def Item(self) -> IComponent:
        """"""
    @property
    def SyncRoot(self) -> object:
        """"""
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array[IComponent], index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    def __len__(self) -> int:
        """"""
    @overload
    def __getitem__(self, index: int) -> IComponent:
        """"""
    @overload
    def __getitem__(self, name: str) -> IComponent:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ComponentConverter(ReferenceConverter):
    """"""
    def __init__(self, type: Type) -> None:
        """"""
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool:
        """"""
    @overload
    def CanConvertFrom(self, sourceType: Type) -> bool:
        """"""
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, destinationType: Type) -> bool:
        """"""
    @overload
    def CanConvertTo(self, destinationType: Type) -> bool:
        """"""
    @overload
    def ConvertFrom(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> object:
        """"""
    @overload
    def ConvertFrom(self, value: object) -> object:
        """"""
    @overload
    def ConvertFromInvariantString(self, context: ITypeDescriptorContext, text: str) -> object:
        """"""
    @overload
    def ConvertFromInvariantString(self, text: str) -> object:
        """"""
    @overload
    def ConvertFromString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, text: str
    ) -> object:
        """"""
    @overload
    def ConvertFromString(self, context: ITypeDescriptorContext, text: str) -> object:
        """"""
    @overload
    def ConvertFromString(self, text: str) -> object:
        """"""
    @overload
    def ConvertTo(
        self,
        context: ITypeDescriptorContext,
        culture: CultureInfo,
        value: object,
        destinationType: Type,
    ) -> object:
        """"""
    @overload
    def ConvertTo(self, value: object, destinationType: Type) -> object:
        """"""
    @overload
    def ConvertToInvariantString(self, context: ITypeDescriptorContext, value: object) -> str:
        """"""
    @overload
    def ConvertToInvariantString(self, value: object) -> str:
        """"""
    @overload
    def ConvertToString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> str:
        """"""
    @overload
    def ConvertToString(self, context: ITypeDescriptorContext, value: object) -> str:
        """"""
    @overload
    def ConvertToString(self, value: object) -> str:
        """"""
    @overload
    def CreateInstance(self, propertyValues: IDictionary) -> object:
        """"""
    @overload
    def CreateInstance(
        self, context: ITypeDescriptorContext, propertyValues: IDictionary
    ) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetCreateInstanceSupported(self) -> bool:
        """"""
    @overload
    def GetCreateInstanceSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object
    ) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]
    ) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetProperties(self, value: object) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetPropertiesSupported(self) -> bool:
        """"""
    @overload
    def GetPropertiesSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    @overload
    def GetStandardValues(self) -> ICollection:
        """"""
    @overload
    def GetStandardValues(
        self, context: ITypeDescriptorContext
    ) -> TypeConverter.StandardValuesCollection:
        """"""
    @overload
    def GetStandardValuesExclusive(self) -> bool:
        """"""
    @overload
    def GetStandardValuesExclusive(self, context: ITypeDescriptorContext) -> bool:
        """"""
    @overload
    def GetStandardValuesSupported(self) -> bool:
        """"""
    @overload
    def GetStandardValuesSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IsValid(self, context: ITypeDescriptorContext, value: object) -> bool:
        """"""
    @overload
    def IsValid(self, value: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    # noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
    class StandardValuesCollection(Object, ICollection, IEnumerable):
        """"""
        def __init__(self, values: ICollection) -> None:
            """"""
        @property
        def Count(self) -> int:
            """"""
        @property
        def IsSynchronized(self) -> bool:
            """"""
        @property
        def Item(self) -> object:
            """"""
        @property
        def SyncRoot(self) -> object:
            """"""
        def CopyTo(self, array: Array, index: int) -> None:
            """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def GetEnumerator(self) -> IEnumerator:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def ToString(self) -> str:
            """"""
        def __iter__(self) -> Iterator:
            """"""
        def __len__(self) -> int:
            """"""
        def __getitem__(self, index: int) -> object:
            """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ComponentEditor(ABC, Object):
    """"""
    @overload
    def EditComponent(self, context: ITypeDescriptorContext, component: object) -> bool:
        """"""
    @overload
    def EditComponent(self, component: object) -> bool:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ComponentResourceManager(ResourceManager):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, t: Type) -> None:
        """"""
    @property
    def BaseName(self) -> str:
        """"""
    @property
    def IgnoreCase(self) -> bool:
        """"""
    @IgnoreCase.setter
    def IgnoreCase(self, value: bool) -> None: ...
    @property
    def ResourceSetType(self) -> Type:
        """"""
    @overload
    def ApplyResources(self, value: object, objectName: str) -> None:
        """"""
    @overload
    def ApplyResources(self, value: object, objectName: str, culture: CultureInfo) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetObject(self, name: str) -> object:
        """"""
    @overload
    def GetObject(self, name: str, culture: CultureInfo) -> object:
        """"""
    def GetResourceSet(
        self, culture: CultureInfo, createIfNotExists: bool, tryParents: bool
    ) -> ResourceSet:
        """"""
    @overload
    def GetStream(self, name: str) -> UnmanagedMemoryStream:
        """"""
    @overload
    def GetStream(self, name: str, culture: CultureInfo) -> UnmanagedMemoryStream:
        """"""
    @overload
    def GetString(self, name: str) -> str:
        """"""
    @overload
    def GetString(self, name: str, culture: CultureInfo) -> str:
        """"""
    def GetType(self) -> Type:
        """"""
    def ReleaseAllResources(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class Container(Object, IContainer, IDisposable):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Components(self) -> ComponentCollection:
        """"""
    @overload
    def Add(self, component: IComponent) -> None:
        """"""
    @overload
    def Add(self, component: IComponent, name: str) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Remove(self, component: IComponent) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def __delitem__(self, component: IComponent) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ContainerFilterService(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def FilterComponents(self, components: ComponentCollection) -> ComponentCollection:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CultureInfoConverter(TypeConverter):
    """"""
    def __init__(self) -> None:
        """"""
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool:
        """"""
    @overload
    def CanConvertFrom(self, sourceType: Type) -> bool:
        """"""
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, destinationType: Type) -> bool:
        """"""
    @overload
    def CanConvertTo(self, destinationType: Type) -> bool:
        """"""
    @overload
    def ConvertFrom(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> object:
        """"""
    @overload
    def ConvertFrom(self, value: object) -> object:
        """"""
    @overload
    def ConvertFromInvariantString(self, context: ITypeDescriptorContext, text: str) -> object:
        """"""
    @overload
    def ConvertFromInvariantString(self, text: str) -> object:
        """"""
    @overload
    def ConvertFromString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, text: str
    ) -> object:
        """"""
    @overload
    def ConvertFromString(self, context: ITypeDescriptorContext, text: str) -> object:
        """"""
    @overload
    def ConvertFromString(self, text: str) -> object:
        """"""
    @overload
    def ConvertTo(
        self,
        context: ITypeDescriptorContext,
        culture: CultureInfo,
        value: object,
        destinationType: Type,
    ) -> object:
        """"""
    @overload
    def ConvertTo(self, value: object, destinationType: Type) -> object:
        """"""
    @overload
    def ConvertToInvariantString(self, context: ITypeDescriptorContext, value: object) -> str:
        """"""
    @overload
    def ConvertToInvariantString(self, value: object) -> str:
        """"""
    @overload
    def ConvertToString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> str:
        """"""
    @overload
    def ConvertToString(self, context: ITypeDescriptorContext, value: object) -> str:
        """"""
    @overload
    def ConvertToString(self, value: object) -> str:
        """"""
    @overload
    def CreateInstance(self, propertyValues: IDictionary) -> object:
        """"""
    @overload
    def CreateInstance(
        self, context: ITypeDescriptorContext, propertyValues: IDictionary
    ) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetCreateInstanceSupported(self) -> bool:
        """"""
    @overload
    def GetCreateInstanceSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object
    ) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]
    ) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetProperties(self, value: object) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetPropertiesSupported(self) -> bool:
        """"""
    @overload
    def GetPropertiesSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    @overload
    def GetStandardValues(self) -> ICollection:
        """"""
    @overload
    def GetStandardValues(
        self, context: ITypeDescriptorContext
    ) -> TypeConverter.StandardValuesCollection:
        """"""
    @overload
    def GetStandardValuesExclusive(self) -> bool:
        """"""
    @overload
    def GetStandardValuesExclusive(self, context: ITypeDescriptorContext) -> bool:
        """"""
    @overload
    def GetStandardValuesSupported(self) -> bool:
        """"""
    @overload
    def GetStandardValuesSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IsValid(self, context: ITypeDescriptorContext, value: object) -> bool:
        """"""
    @overload
    def IsValid(self, value: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    # noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
    class StandardValuesCollection(Object, ICollection, IEnumerable):
        """"""
        def __init__(self, values: ICollection) -> None:
            """"""
        @property
        def Count(self) -> int:
            """"""
        @property
        def IsSynchronized(self) -> bool:
            """"""
        @property
        def Item(self) -> object:
            """"""
        @property
        def SyncRoot(self) -> object:
            """"""
        def CopyTo(self, array: Array, index: int) -> None:
            """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def GetEnumerator(self) -> IEnumerator:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def ToString(self) -> str:
            """"""
        def __iter__(self) -> Iterator:
            """"""
        def __len__(self) -> int:
            """"""
        def __getitem__(self, index: int) -> object:
            """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CustomTypeDescriptor(ABC, Object, ICustomTypeDescriptor):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetAttributes(self) -> AttributeCollection:
        """"""
    def GetClassName(self) -> str:
        """"""
    def GetComponentName(self) -> str:
        """"""
    def GetConverter(self) -> TypeConverter:
        """"""
    def GetDefaultEvent(self) -> EventDescriptor:
        """"""
    def GetDefaultProperty(self) -> PropertyDescriptor:
        """"""
    def GetEditor(self, editorBaseType: Type) -> object:
        """"""
    @overload
    def GetEvents(self) -> EventDescriptorCollection:
        """"""
    @overload
    def GetEvents(self, attributes: Array[Attribute]) -> EventDescriptorCollection:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetProperties(self) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetProperties(self, attributes: Array[Attribute]) -> PropertyDescriptorCollection:
        """"""
    def GetPropertyOwner(self, pd: PropertyDescriptor) -> object:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class DataErrorsChangedEventArgs(EventArgs):
    """"""
    def __init__(self, propertyName: str) -> None:
        """"""
    @property
    def PropertyName(self) -> str:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class DataObjectAttribute(Attribute, _Attribute):
    """"""

    DataObject: ClassVar[DataObjectAttribute]
    """"""
    Default: ClassVar[DataObjectAttribute]
    """"""
    NonDataObject: ClassVar[DataObjectAttribute]
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, isDataObject: bool) -> None:
        """"""
    @property
    def IsDataObject(self) -> bool:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class DataObjectFieldAttribute(Attribute, _Attribute):
    """"""
    @overload
    def __init__(self, primaryKey: bool) -> None:
        """"""
    @overload
    def __init__(self, primaryKey: bool, isIdentity: bool) -> None:
        """"""
    @overload
    def __init__(self, primaryKey: bool, isIdentity: bool, isNullable: bool) -> None:
        """"""
    @overload
    def __init__(self, primaryKey: bool, isIdentity: bool, isNullable: bool, length: int) -> None:
        """"""
    @property
    def IsIdentity(self) -> bool:
        """"""
    @property
    def IsNullable(self) -> bool:
        """"""
    @property
    def Length(self) -> int:
        """"""
    @property
    def PrimaryKey(self) -> bool:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class DataObjectMethodAttribute(Attribute, _Attribute):
    """"""
    @overload
    def __init__(self, methodType: DataObjectMethodType) -> None:
        """"""
    @overload
    def __init__(self, methodType: DataObjectMethodType, isDefault: bool) -> None:
        """"""
    @property
    def IsDefault(self) -> bool:
        """"""
    @property
    def MethodType(self) -> DataObjectMethodType:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
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

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class DateTimeConverter(TypeConverter):
    """"""
    def __init__(self) -> None:
        """"""
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool:
        """"""
    @overload
    def CanConvertFrom(self, sourceType: Type) -> bool:
        """"""
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, destinationType: Type) -> bool:
        """"""
    @overload
    def CanConvertTo(self, destinationType: Type) -> bool:
        """"""
    @overload
    def ConvertFrom(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> object:
        """"""
    @overload
    def ConvertFrom(self, value: object) -> object:
        """"""
    @overload
    def ConvertFromInvariantString(self, context: ITypeDescriptorContext, text: str) -> object:
        """"""
    @overload
    def ConvertFromInvariantString(self, text: str) -> object:
        """"""
    @overload
    def ConvertFromString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, text: str
    ) -> object:
        """"""
    @overload
    def ConvertFromString(self, context: ITypeDescriptorContext, text: str) -> object:
        """"""
    @overload
    def ConvertFromString(self, text: str) -> object:
        """"""
    @overload
    def ConvertTo(
        self,
        context: ITypeDescriptorContext,
        culture: CultureInfo,
        value: object,
        destinationType: Type,
    ) -> object:
        """"""
    @overload
    def ConvertTo(self, value: object, destinationType: Type) -> object:
        """"""
    @overload
    def ConvertToInvariantString(self, context: ITypeDescriptorContext, value: object) -> str:
        """"""
    @overload
    def ConvertToInvariantString(self, value: object) -> str:
        """"""
    @overload
    def ConvertToString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> str:
        """"""
    @overload
    def ConvertToString(self, context: ITypeDescriptorContext, value: object) -> str:
        """"""
    @overload
    def ConvertToString(self, value: object) -> str:
        """"""
    @overload
    def CreateInstance(self, propertyValues: IDictionary) -> object:
        """"""
    @overload
    def CreateInstance(
        self, context: ITypeDescriptorContext, propertyValues: IDictionary
    ) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetCreateInstanceSupported(self) -> bool:
        """"""
    @overload
    def GetCreateInstanceSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object
    ) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]
    ) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetProperties(self, value: object) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetPropertiesSupported(self) -> bool:
        """"""
    @overload
    def GetPropertiesSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    @overload
    def GetStandardValues(self) -> ICollection:
        """"""
    @overload
    def GetStandardValues(
        self, context: ITypeDescriptorContext
    ) -> TypeConverter.StandardValuesCollection:
        """"""
    @overload
    def GetStandardValuesExclusive(self) -> bool:
        """"""
    @overload
    def GetStandardValuesExclusive(self, context: ITypeDescriptorContext) -> bool:
        """"""
    @overload
    def GetStandardValuesSupported(self) -> bool:
        """"""
    @overload
    def GetStandardValuesSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IsValid(self, context: ITypeDescriptorContext, value: object) -> bool:
        """"""
    @overload
    def IsValid(self, value: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    # noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
    class StandardValuesCollection(Object, ICollection, IEnumerable):
        """"""
        def __init__(self, values: ICollection) -> None:
            """"""
        @property
        def Count(self) -> int:
            """"""
        @property
        def IsSynchronized(self) -> bool:
            """"""
        @property
        def Item(self) -> object:
            """"""
        @property
        def SyncRoot(self) -> object:
            """"""
        def CopyTo(self, array: Array, index: int) -> None:
            """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def GetEnumerator(self) -> IEnumerator:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def ToString(self) -> str:
            """"""
        def __iter__(self) -> Iterator:
            """"""
        def __len__(self) -> int:
            """"""
        def __getitem__(self, index: int) -> object:
            """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class DateTimeOffsetConverter(TypeConverter):
    """"""
    def __init__(self) -> None:
        """"""
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool:
        """"""
    @overload
    def CanConvertFrom(self, sourceType: Type) -> bool:
        """"""
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, destinationType: Type) -> bool:
        """"""
    @overload
    def CanConvertTo(self, destinationType: Type) -> bool:
        """"""
    @overload
    def ConvertFrom(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> object:
        """"""
    @overload
    def ConvertFrom(self, value: object) -> object:
        """"""
    @overload
    def ConvertFromInvariantString(self, context: ITypeDescriptorContext, text: str) -> object:
        """"""
    @overload
    def ConvertFromInvariantString(self, text: str) -> object:
        """"""
    @overload
    def ConvertFromString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, text: str
    ) -> object:
        """"""
    @overload
    def ConvertFromString(self, context: ITypeDescriptorContext, text: str) -> object:
        """"""
    @overload
    def ConvertFromString(self, text: str) -> object:
        """"""
    @overload
    def ConvertTo(
        self,
        context: ITypeDescriptorContext,
        culture: CultureInfo,
        value: object,
        destinationType: Type,
    ) -> object:
        """"""
    @overload
    def ConvertTo(self, value: object, destinationType: Type) -> object:
        """"""
    @overload
    def ConvertToInvariantString(self, context: ITypeDescriptorContext, value: object) -> str:
        """"""
    @overload
    def ConvertToInvariantString(self, value: object) -> str:
        """"""
    @overload
    def ConvertToString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> str:
        """"""
    @overload
    def ConvertToString(self, context: ITypeDescriptorContext, value: object) -> str:
        """"""
    @overload
    def ConvertToString(self, value: object) -> str:
        """"""
    @overload
    def CreateInstance(self, propertyValues: IDictionary) -> object:
        """"""
    @overload
    def CreateInstance(
        self, context: ITypeDescriptorContext, propertyValues: IDictionary
    ) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetCreateInstanceSupported(self) -> bool:
        """"""
    @overload
    def GetCreateInstanceSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object
    ) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]
    ) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetProperties(self, value: object) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetPropertiesSupported(self) -> bool:
        """"""
    @overload
    def GetPropertiesSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    @overload
    def GetStandardValues(self) -> ICollection:
        """"""
    @overload
    def GetStandardValues(
        self, context: ITypeDescriptorContext
    ) -> TypeConverter.StandardValuesCollection:
        """"""
    @overload
    def GetStandardValuesExclusive(self) -> bool:
        """"""
    @overload
    def GetStandardValuesExclusive(self, context: ITypeDescriptorContext) -> bool:
        """"""
    @overload
    def GetStandardValuesSupported(self) -> bool:
        """"""
    @overload
    def GetStandardValuesSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IsValid(self, context: ITypeDescriptorContext, value: object) -> bool:
        """"""
    @overload
    def IsValid(self, value: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    # noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
    class StandardValuesCollection(Object, ICollection, IEnumerable):
        """"""
        def __init__(self, values: ICollection) -> None:
            """"""
        @property
        def Count(self) -> int:
            """"""
        @property
        def IsSynchronized(self) -> bool:
            """"""
        @property
        def Item(self) -> object:
            """"""
        @property
        def SyncRoot(self) -> object:
            """"""
        def CopyTo(self, array: Array, index: int) -> None:
            """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def GetEnumerator(self) -> IEnumerator:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def ToString(self) -> str:
            """"""
        def __iter__(self) -> Iterator:
            """"""
        def __len__(self) -> int:
            """"""
        def __getitem__(self, index: int) -> object:
            """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class DecimalConverter(BaseNumberConverter):
    """"""
    def __init__(self) -> None:
        """"""
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool:
        """"""
    @overload
    def CanConvertFrom(self, sourceType: Type) -> bool:
        """"""
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, destinationType: Type) -> bool:
        """"""
    @overload
    def CanConvertTo(self, destinationType: Type) -> bool:
        """"""
    @overload
    def ConvertFrom(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> object:
        """"""
    @overload
    def ConvertFrom(self, value: object) -> object:
        """"""
    @overload
    def ConvertFromInvariantString(self, context: ITypeDescriptorContext, text: str) -> object:
        """"""
    @overload
    def ConvertFromInvariantString(self, text: str) -> object:
        """"""
    @overload
    def ConvertFromString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, text: str
    ) -> object:
        """"""
    @overload
    def ConvertFromString(self, context: ITypeDescriptorContext, text: str) -> object:
        """"""
    @overload
    def ConvertFromString(self, text: str) -> object:
        """"""
    @overload
    def ConvertTo(
        self,
        context: ITypeDescriptorContext,
        culture: CultureInfo,
        value: object,
        destinationType: Type,
    ) -> object:
        """"""
    @overload
    def ConvertTo(self, value: object, destinationType: Type) -> object:
        """"""
    @overload
    def ConvertToInvariantString(self, context: ITypeDescriptorContext, value: object) -> str:
        """"""
    @overload
    def ConvertToInvariantString(self, value: object) -> str:
        """"""
    @overload
    def ConvertToString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> str:
        """"""
    @overload
    def ConvertToString(self, context: ITypeDescriptorContext, value: object) -> str:
        """"""
    @overload
    def ConvertToString(self, value: object) -> str:
        """"""
    @overload
    def CreateInstance(self, propertyValues: IDictionary) -> object:
        """"""
    @overload
    def CreateInstance(
        self, context: ITypeDescriptorContext, propertyValues: IDictionary
    ) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetCreateInstanceSupported(self) -> bool:
        """"""
    @overload
    def GetCreateInstanceSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object
    ) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]
    ) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetProperties(self, value: object) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetPropertiesSupported(self) -> bool:
        """"""
    @overload
    def GetPropertiesSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    @overload
    def GetStandardValues(self) -> ICollection:
        """"""
    @overload
    def GetStandardValues(
        self, context: ITypeDescriptorContext
    ) -> TypeConverter.StandardValuesCollection:
        """"""
    @overload
    def GetStandardValuesExclusive(self) -> bool:
        """"""
    @overload
    def GetStandardValuesExclusive(self, context: ITypeDescriptorContext) -> bool:
        """"""
    @overload
    def GetStandardValuesSupported(self) -> bool:
        """"""
    @overload
    def GetStandardValuesSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IsValid(self, context: ITypeDescriptorContext, value: object) -> bool:
        """"""
    @overload
    def IsValid(self, value: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    # noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
    class StandardValuesCollection(Object, ICollection, IEnumerable):
        """"""
        def __init__(self, values: ICollection) -> None:
            """"""
        @property
        def Count(self) -> int:
            """"""
        @property
        def IsSynchronized(self) -> bool:
            """"""
        @property
        def Item(self) -> object:
            """"""
        @property
        def SyncRoot(self) -> object:
            """"""
        def CopyTo(self, array: Array, index: int) -> None:
            """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def GetEnumerator(self) -> IEnumerator:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def ToString(self) -> str:
            """"""
        def __iter__(self) -> Iterator:
            """"""
        def __len__(self) -> int:
            """"""
        def __getitem__(self, index: int) -> object:
            """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class DefaultBindingPropertyAttribute(Attribute, _Attribute):
    """"""

    Default: ClassVar[DefaultBindingPropertyAttribute]
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, name: str) -> None:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class DefaultEventAttribute(Attribute, _Attribute):
    """"""

    Default: ClassVar[DefaultEventAttribute]
    """"""
    def __init__(self, name: str) -> None:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class DefaultPropertyAttribute(Attribute, _Attribute):
    """"""

    Default: ClassVar[DefaultPropertyAttribute]
    """"""
    def __init__(self, name: str) -> None:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class DefaultValueAttribute(Attribute, _Attribute):
    """"""
    @overload
    def __init__(self, type: Type, value: str) -> None:
        """"""
    @overload
    def __init__(self, value: Char) -> None:
        """"""
    @overload
    def __init__(self, value: int) -> None:
        """"""
    @overload
    def __init__(self, value: int) -> None:
        """"""
    @overload
    def __init__(self, value: int) -> None:
        """"""
    @overload
    def __init__(self, value: int) -> None:
        """"""
    @overload
    def __init__(self, value: float) -> None:
        """"""
    @overload
    def __init__(self, value: float) -> None:
        """"""
    @overload
    def __init__(self, value: bool) -> None:
        """"""
    @overload
    def __init__(self, value: str) -> None:
        """"""
    @overload
    def __init__(self, value: object) -> None:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
    @property
    def Value(self) -> object:
        """"""
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class DelegatingTypeDescriptionProvider(TypeDescriptionProvider):
    """"""
    def CreateInstance(
        self,
        provider: IServiceProvider,
        objectType: Type,
        argTypes: Array[Type],
        args: Array[object],
    ) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetCache(self, instance: object) -> IDictionary:
        """"""
    def GetExtendedTypeDescriptor(self, instance: object) -> ICustomTypeDescriptor:
        """"""
    def GetFullComponentName(self, component: object) -> str:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetReflectionType(self, instance: object) -> Type:
        """"""
    @overload
    def GetReflectionType(self, objectType: Type) -> Type:
        """"""
    @overload
    def GetReflectionType(self, objectType: Type, instance: object) -> Type:
        """"""
    def GetRuntimeType(self, objectType: Type) -> Type:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def GetTypeDescriptor(self, instance: object) -> ICustomTypeDescriptor:
        """"""
    @overload
    def GetTypeDescriptor(self, objectType: Type) -> ICustomTypeDescriptor:
        """"""
    @overload
    def GetTypeDescriptor(self, objectType: Type, instance: object) -> ICustomTypeDescriptor:
        """"""
    def IsSupportedType(self, type: Type) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class DescriptionAttribute(Attribute, _Attribute):
    """"""

    Default: ClassVar[DescriptionAttribute]
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, description: str) -> None:
        """"""
    @property
    def Description(self) -> str:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class DesignOnlyAttribute(Attribute, _Attribute):
    """"""

    Default: ClassVar[DesignOnlyAttribute]
    """"""
    No: ClassVar[DesignOnlyAttribute]
    """"""
    Yes: ClassVar[DesignOnlyAttribute]
    """"""
    def __init__(self, isDesignOnly: bool) -> None:
        """"""
    @property
    def IsDesignOnly(self) -> bool:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class DesignTimeVisibleAttribute(Attribute, _Attribute):
    """"""

    Default: ClassVar[DesignTimeVisibleAttribute]
    """"""
    No: ClassVar[DesignTimeVisibleAttribute]
    """"""
    Yes: ClassVar[DesignTimeVisibleAttribute]
    """"""
    @overload
    def __init__(self, visible: bool) -> None:
        """"""
    @overload
    def __init__(self) -> None:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
    @property
    def Visible(self) -> bool:
        """"""
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class DesignerAttribute(Attribute, _Attribute):
    """"""
    @overload
    def __init__(self, designerTypeName: str) -> None:
        """"""
    @overload
    def __init__(self, designerType: Type) -> None:
        """"""
    @overload
    def __init__(self, designerTypeName: str, designerBaseTypeName: str) -> None:
        """"""
    @overload
    def __init__(self, designerTypeName: str, designerBaseType: Type) -> None:
        """"""
    @overload
    def __init__(self, designerType: Type, designerBaseType: Type) -> None:
        """"""
    @property
    def DesignerBaseTypeName(self) -> str:
        """"""
    @property
    def DesignerTypeName(self) -> str:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class DesignerCategoryAttribute(Attribute, _Attribute):
    """"""

    Component: ClassVar[DesignerCategoryAttribute]
    """"""
    Default: ClassVar[DesignerCategoryAttribute]
    """"""
    Form: ClassVar[DesignerCategoryAttribute]
    """"""
    Generic: ClassVar[DesignerCategoryAttribute]
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, category: str) -> None:
        """"""
    @property
    def Category(self) -> str:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
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

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class DesignerSerializationVisibility(Enum):
    """"""

    Hidden: DesignerSerializationVisibility = ...
    """"""
    Visible: DesignerSerializationVisibility = ...
    """"""
    Content: DesignerSerializationVisibility = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class DesignerSerializationVisibilityAttribute(Attribute, _Attribute):
    """"""

    Content: ClassVar[DesignerSerializationVisibilityAttribute]
    """"""
    Default: ClassVar[DesignerSerializationVisibilityAttribute]
    """"""
    Hidden: ClassVar[DesignerSerializationVisibilityAttribute]
    """"""
    Visible: ClassVar[DesignerSerializationVisibilityAttribute]
    """"""
    def __init__(self, visibility: DesignerSerializationVisibility) -> None:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
    @property
    def Visibility(self) -> DesignerSerializationVisibility:
        """"""
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class DisplayNameAttribute(Attribute, _Attribute):
    """"""

    Default: ClassVar[DisplayNameAttribute]
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, displayName: str) -> None:
        """"""
    @property
    def DisplayName(self) -> str:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class DoWorkEventArgs(CancelEventArgs):
    """"""
    def __init__(self, argument: object) -> None:
        """"""
    @property
    def Argument(self) -> object:
        """"""
    @property
    def Cancel(self) -> bool:
        """"""
    @Cancel.setter
    def Cancel(self, value: bool) -> None: ...
    @property
    def Result(self) -> object:
        """"""
    @Result.setter
    def Result(self, value: object) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

type DoWorkEventHandler = Callable[[object, DoWorkEventArgs], None]
""""""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class DoubleConverter(BaseNumberConverter):
    """"""
    def __init__(self) -> None:
        """"""
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool:
        """"""
    @overload
    def CanConvertFrom(self, sourceType: Type) -> bool:
        """"""
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, t: Type) -> bool:
        """"""
    @overload
    def CanConvertTo(self, destinationType: Type) -> bool:
        """"""
    @overload
    def ConvertFrom(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> object:
        """"""
    @overload
    def ConvertFrom(self, value: object) -> object:
        """"""
    @overload
    def ConvertFromInvariantString(self, context: ITypeDescriptorContext, text: str) -> object:
        """"""
    @overload
    def ConvertFromInvariantString(self, text: str) -> object:
        """"""
    @overload
    def ConvertFromString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, text: str
    ) -> object:
        """"""
    @overload
    def ConvertFromString(self, context: ITypeDescriptorContext, text: str) -> object:
        """"""
    @overload
    def ConvertFromString(self, text: str) -> object:
        """"""
    @overload
    def ConvertTo(
        self,
        context: ITypeDescriptorContext,
        culture: CultureInfo,
        value: object,
        destinationType: Type,
    ) -> object:
        """"""
    @overload
    def ConvertTo(self, value: object, destinationType: Type) -> object:
        """"""
    @overload
    def ConvertToInvariantString(self, context: ITypeDescriptorContext, value: object) -> str:
        """"""
    @overload
    def ConvertToInvariantString(self, value: object) -> str:
        """"""
    @overload
    def ConvertToString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> str:
        """"""
    @overload
    def ConvertToString(self, context: ITypeDescriptorContext, value: object) -> str:
        """"""
    @overload
    def ConvertToString(self, value: object) -> str:
        """"""
    @overload
    def CreateInstance(self, propertyValues: IDictionary) -> object:
        """"""
    @overload
    def CreateInstance(
        self, context: ITypeDescriptorContext, propertyValues: IDictionary
    ) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetCreateInstanceSupported(self) -> bool:
        """"""
    @overload
    def GetCreateInstanceSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object
    ) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]
    ) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetProperties(self, value: object) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetPropertiesSupported(self) -> bool:
        """"""
    @overload
    def GetPropertiesSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    @overload
    def GetStandardValues(self) -> ICollection:
        """"""
    @overload
    def GetStandardValues(
        self, context: ITypeDescriptorContext
    ) -> TypeConverter.StandardValuesCollection:
        """"""
    @overload
    def GetStandardValuesExclusive(self) -> bool:
        """"""
    @overload
    def GetStandardValuesExclusive(self, context: ITypeDescriptorContext) -> bool:
        """"""
    @overload
    def GetStandardValuesSupported(self) -> bool:
        """"""
    @overload
    def GetStandardValuesSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IsValid(self, context: ITypeDescriptorContext, value: object) -> bool:
        """"""
    @overload
    def IsValid(self, value: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    # noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
    class StandardValuesCollection(Object, ICollection, IEnumerable):
        """"""
        def __init__(self, values: ICollection) -> None:
            """"""
        @property
        def Count(self) -> int:
            """"""
        @property
        def IsSynchronized(self) -> bool:
            """"""
        @property
        def Item(self) -> object:
            """"""
        @property
        def SyncRoot(self) -> object:
            """"""
        def CopyTo(self, array: Array, index: int) -> None:
            """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def GetEnumerator(self) -> IEnumerator:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def ToString(self) -> str:
            """"""
        def __iter__(self) -> Iterator:
            """"""
        def __len__(self) -> int:
            """"""
        def __getitem__(self, index: int) -> object:
            """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class EditorAttribute(Attribute, _Attribute):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, typeName: str, baseTypeName: str) -> None:
        """"""
    @overload
    def __init__(self, typeName: str, baseType: Type) -> None:
        """"""
    @overload
    def __init__(self, type: Type, baseType: Type) -> None:
        """"""
    @property
    def EditorBaseTypeName(self) -> str:
        """"""
    @property
    def EditorTypeName(self) -> str:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class EditorBrowsableAttribute(Attribute, _Attribute):
    """"""
    @overload
    def __init__(self, state: EditorBrowsableState) -> None:
        """"""
    @overload
    def __init__(self) -> None:
        """"""
    @property
    def State(self) -> EditorBrowsableState:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
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

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class EditorBrowsableState(Enum):
    """"""

    Always: EditorBrowsableState = ...
    """"""
    Never: EditorBrowsableState = ...
    """"""
    Advanced: EditorBrowsableState = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class EnumConverter(TypeConverter):
    """"""
    def __init__(self, type: Type) -> None:
        """"""
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool:
        """"""
    @overload
    def CanConvertFrom(self, sourceType: Type) -> bool:
        """"""
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, destinationType: Type) -> bool:
        """"""
    @overload
    def CanConvertTo(self, destinationType: Type) -> bool:
        """"""
    @overload
    def ConvertFrom(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> object:
        """"""
    @overload
    def ConvertFrom(self, value: object) -> object:
        """"""
    @overload
    def ConvertFromInvariantString(self, context: ITypeDescriptorContext, text: str) -> object:
        """"""
    @overload
    def ConvertFromInvariantString(self, text: str) -> object:
        """"""
    @overload
    def ConvertFromString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, text: str
    ) -> object:
        """"""
    @overload
    def ConvertFromString(self, context: ITypeDescriptorContext, text: str) -> object:
        """"""
    @overload
    def ConvertFromString(self, text: str) -> object:
        """"""
    @overload
    def ConvertTo(
        self,
        context: ITypeDescriptorContext,
        culture: CultureInfo,
        value: object,
        destinationType: Type,
    ) -> object:
        """"""
    @overload
    def ConvertTo(self, value: object, destinationType: Type) -> object:
        """"""
    @overload
    def ConvertToInvariantString(self, context: ITypeDescriptorContext, value: object) -> str:
        """"""
    @overload
    def ConvertToInvariantString(self, value: object) -> str:
        """"""
    @overload
    def ConvertToString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> str:
        """"""
    @overload
    def ConvertToString(self, context: ITypeDescriptorContext, value: object) -> str:
        """"""
    @overload
    def ConvertToString(self, value: object) -> str:
        """"""
    @overload
    def CreateInstance(self, propertyValues: IDictionary) -> object:
        """"""
    @overload
    def CreateInstance(
        self, context: ITypeDescriptorContext, propertyValues: IDictionary
    ) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetCreateInstanceSupported(self) -> bool:
        """"""
    @overload
    def GetCreateInstanceSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object
    ) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]
    ) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetProperties(self, value: object) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetPropertiesSupported(self) -> bool:
        """"""
    @overload
    def GetPropertiesSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    @overload
    def GetStandardValues(self) -> ICollection:
        """"""
    @overload
    def GetStandardValues(
        self, context: ITypeDescriptorContext
    ) -> TypeConverter.StandardValuesCollection:
        """"""
    @overload
    def GetStandardValuesExclusive(self) -> bool:
        """"""
    @overload
    def GetStandardValuesExclusive(self, context: ITypeDescriptorContext) -> bool:
        """"""
    @overload
    def GetStandardValuesSupported(self) -> bool:
        """"""
    @overload
    def GetStandardValuesSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IsValid(self, context: ITypeDescriptorContext, value: object) -> bool:
        """"""
    @overload
    def IsValid(self, value: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    # noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
    class StandardValuesCollection(Object, ICollection, IEnumerable):
        """"""
        def __init__(self, values: ICollection) -> None:
            """"""
        @property
        def Count(self) -> int:
            """"""
        @property
        def IsSynchronized(self) -> bool:
            """"""
        @property
        def Item(self) -> object:
            """"""
        @property
        def SyncRoot(self) -> object:
            """"""
        def CopyTo(self, array: Array, index: int) -> None:
            """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def GetEnumerator(self) -> IEnumerator:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def ToString(self) -> str:
            """"""
        def __iter__(self) -> Iterator:
            """"""
        def __len__(self) -> int:
            """"""
        def __getitem__(self, index: int) -> object:
            """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class EventDescriptor(ABC, MemberDescriptor):
    """"""
    @property
    def Attributes(self) -> AttributeCollection:
        """"""
    @property
    def Category(self) -> str:
        """"""
    @property
    def ComponentType(self) -> Type:
        """"""
    @property
    def Description(self) -> str:
        """"""
    @property
    def DesignTimeOnly(self) -> bool:
        """"""
    @property
    def DisplayName(self) -> str:
        """"""
    @property
    def EventType(self) -> Type:
        """"""
    @property
    def IsBrowsable(self) -> bool:
        """"""
    @property
    def IsMulticast(self) -> bool:
        """"""
    @property
    def Name(self) -> str:
        """"""
    def AddEventHandler(self, component: object, value: Delegate) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def RemoveEventHandler(self, component: object, value: Delegate) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class EventDescriptorCollection(Object, ICollection, IEnumerable, IList):
    """"""

    Empty: ClassVar[EventDescriptorCollection]
    """"""
    @overload
    def __init__(self, events: Array[EventDescriptor]) -> None:
        """"""
    @overload
    def __init__(self, events: Array[EventDescriptor], readOnly: bool) -> None:
        """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsFixedSize(self) -> bool:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def Item(self) -> EventDescriptor:
        """"""
    @property
    def SyncRoot(self) -> object:
        """"""
    @overload
    def Add(self, value: EventDescriptor) -> int:
        """"""
    @overload
    def Add(self, value: object) -> int:
        """"""
    def Clear(self) -> None:
        """"""
    @overload
    def Contains(self, value: EventDescriptor) -> bool:
        """"""
    @overload
    def Contains(self, value: object) -> bool:
        """"""
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Find(self, name: str, ignoreCase: bool) -> EventDescriptor:
        """"""
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IndexOf(self, value: EventDescriptor) -> int:
        """"""
    @overload
    def IndexOf(self, value: object) -> int:
        """"""
    @overload
    def Insert(self, index: int, value: EventDescriptor) -> None:
        """"""
    @overload
    def Insert(self, index: int, value: object) -> None:
        """"""
    @overload
    def Remove(self, value: EventDescriptor) -> None:
        """"""
    @overload
    def Remove(self, value: object) -> None:
        """"""
    def RemoveAt(self, index: int) -> None:
        """"""
    @overload
    def Sort(self) -> EventDescriptorCollection:
        """"""
    @overload
    def Sort(self, comparer: IComparer) -> EventDescriptorCollection:
        """"""
    @overload
    def Sort(self, names: Array[str]) -> EventDescriptorCollection:
        """"""
    @overload
    def Sort(self, names: Array[str], comparer: IComparer) -> EventDescriptorCollection:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __contains__(self, value: EventDescriptor) -> bool:
        """"""
    @overload
    def __contains__(self, value: object) -> bool:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    @overload
    def __delitem__(self, value: EventDescriptor) -> None:
        """"""
    @overload
    def __delitem__(self, value: object) -> None:
        """"""
    def __len__(self) -> int:
        """"""
    @overload
    def __getitem__(self, index: int) -> EventDescriptor:
        """"""
    @overload
    def __getitem__(self, name: str) -> EventDescriptor:
        """"""
    def __setitem__(self, index: int, value: object) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class EventHandlerList(Object, IDisposable):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Item(self) -> Delegate:
        """"""
    @Item.setter
    def Item(self, value: Delegate) -> None: ...
    def AddHandler(self, key: object, value: Delegate) -> None:
        """"""
    def AddHandlers(self, listToAddFrom: EventHandlerList) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def RemoveHandler(self, key: object, value: Delegate) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def __getitem__(self, key: object) -> Delegate:
        """"""
    def __setitem__(self, key: object, value: Delegate) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ExpandableObjectConverter(TypeConverter):
    """"""
    def __init__(self) -> None:
        """"""
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool:
        """"""
    @overload
    def CanConvertFrom(self, sourceType: Type) -> bool:
        """"""
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, destinationType: Type) -> bool:
        """"""
    @overload
    def CanConvertTo(self, destinationType: Type) -> bool:
        """"""
    @overload
    def ConvertFrom(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> object:
        """"""
    @overload
    def ConvertFrom(self, value: object) -> object:
        """"""
    @overload
    def ConvertFromInvariantString(self, context: ITypeDescriptorContext, text: str) -> object:
        """"""
    @overload
    def ConvertFromInvariantString(self, text: str) -> object:
        """"""
    @overload
    def ConvertFromString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, text: str
    ) -> object:
        """"""
    @overload
    def ConvertFromString(self, context: ITypeDescriptorContext, text: str) -> object:
        """"""
    @overload
    def ConvertFromString(self, text: str) -> object:
        """"""
    @overload
    def ConvertTo(
        self,
        context: ITypeDescriptorContext,
        culture: CultureInfo,
        value: object,
        destinationType: Type,
    ) -> object:
        """"""
    @overload
    def ConvertTo(self, value: object, destinationType: Type) -> object:
        """"""
    @overload
    def ConvertToInvariantString(self, context: ITypeDescriptorContext, value: object) -> str:
        """"""
    @overload
    def ConvertToInvariantString(self, value: object) -> str:
        """"""
    @overload
    def ConvertToString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> str:
        """"""
    @overload
    def ConvertToString(self, context: ITypeDescriptorContext, value: object) -> str:
        """"""
    @overload
    def ConvertToString(self, value: object) -> str:
        """"""
    @overload
    def CreateInstance(self, propertyValues: IDictionary) -> object:
        """"""
    @overload
    def CreateInstance(
        self, context: ITypeDescriptorContext, propertyValues: IDictionary
    ) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetCreateInstanceSupported(self) -> bool:
        """"""
    @overload
    def GetCreateInstanceSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object
    ) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]
    ) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetProperties(self, value: object) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetPropertiesSupported(self) -> bool:
        """"""
    @overload
    def GetPropertiesSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    @overload
    def GetStandardValues(self) -> ICollection:
        """"""
    @overload
    def GetStandardValues(
        self, context: ITypeDescriptorContext
    ) -> TypeConverter.StandardValuesCollection:
        """"""
    @overload
    def GetStandardValuesExclusive(self) -> bool:
        """"""
    @overload
    def GetStandardValuesExclusive(self, context: ITypeDescriptorContext) -> bool:
        """"""
    @overload
    def GetStandardValuesSupported(self) -> bool:
        """"""
    @overload
    def GetStandardValuesSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IsValid(self, context: ITypeDescriptorContext, value: object) -> bool:
        """"""
    @overload
    def IsValid(self, value: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    # noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
    class StandardValuesCollection(Object, ICollection, IEnumerable):
        """"""
        def __init__(self, values: ICollection) -> None:
            """"""
        @property
        def Count(self) -> int:
            """"""
        @property
        def IsSynchronized(self) -> bool:
            """"""
        @property
        def Item(self) -> object:
            """"""
        @property
        def SyncRoot(self) -> object:
            """"""
        def CopyTo(self, array: Array, index: int) -> None:
            """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def GetEnumerator(self) -> IEnumerator:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def ToString(self) -> str:
            """"""
        def __iter__(self) -> Iterator:
            """"""
        def __len__(self) -> int:
            """"""
        def __getitem__(self, index: int) -> object:
            """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ExtendedPropertyDescriptor(PropertyDescriptor):
    """"""
    @overload
    def __init__(
        self,
        extenderInfo: ReflectPropertyDescriptor,
        receiverType: Type,
        provider: IExtenderProvider,
        attributes: Array[Attribute],
    ) -> None:
        """"""
    @overload
    def __init__(self, extender: PropertyDescriptor, attributes: Array[Attribute]) -> None:
        """"""
    @property
    def Attributes(self) -> AttributeCollection:
        """"""
    @property
    def Category(self) -> str:
        """"""
    @property
    def ComponentType(self) -> Type:
        """"""
    @property
    def Converter(self) -> TypeConverter:
        """"""
    @property
    def Description(self) -> str:
        """"""
    @property
    def DesignTimeOnly(self) -> bool:
        """"""
    @property
    def DisplayName(self) -> str:
        """"""
    @property
    def IsBrowsable(self) -> bool:
        """"""
    @property
    def IsLocalizable(self) -> bool:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def PropertyType(self) -> Type:
        """"""
    @property
    def SerializationVisibility(self) -> DesignerSerializationVisibility:
        """"""
    @property
    def SupportsChangeEvents(self) -> bool:
        """"""
    def AddValueChanged(self, component: object, handler: EventHandler) -> None:
        """"""
    def CanResetValue(self, comp: object) -> bool:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetChildProperties(self) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetChildProperties(self, filter: Array[Attribute]) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetChildProperties(self, instance: object) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetChildProperties(
        self, instance: object, filter: Array[Attribute]
    ) -> PropertyDescriptorCollection:
        """"""
    def GetEditor(self, editorBaseType: Type) -> object:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetValue(self, comp: object) -> object:
        """"""
    def RemoveValueChanged(self, component: object, handler: EventHandler) -> None:
        """"""
    def ResetValue(self, comp: object) -> None:
        """"""
    def SetValue(self, component: object, value: object) -> None:
        """"""
    def ShouldSerializeValue(self, comp: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ExtenderProvidedPropertyAttribute(Attribute, _Attribute):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def ExtenderProperty(self) -> PropertyDescriptor:
        """"""
    @property
    def Provider(self) -> IExtenderProvider:
        """"""
    @property
    def ReceiverType(self) -> Type:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class GuidConverter(TypeConverter):
    """"""
    def __init__(self) -> None:
        """"""
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool:
        """"""
    @overload
    def CanConvertFrom(self, sourceType: Type) -> bool:
        """"""
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, destinationType: Type) -> bool:
        """"""
    @overload
    def CanConvertTo(self, destinationType: Type) -> bool:
        """"""
    @overload
    def ConvertFrom(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> object:
        """"""
    @overload
    def ConvertFrom(self, value: object) -> object:
        """"""
    @overload
    def ConvertFromInvariantString(self, context: ITypeDescriptorContext, text: str) -> object:
        """"""
    @overload
    def ConvertFromInvariantString(self, text: str) -> object:
        """"""
    @overload
    def ConvertFromString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, text: str
    ) -> object:
        """"""
    @overload
    def ConvertFromString(self, context: ITypeDescriptorContext, text: str) -> object:
        """"""
    @overload
    def ConvertFromString(self, text: str) -> object:
        """"""
    @overload
    def ConvertTo(
        self,
        context: ITypeDescriptorContext,
        culture: CultureInfo,
        value: object,
        destinationType: Type,
    ) -> object:
        """"""
    @overload
    def ConvertTo(self, value: object, destinationType: Type) -> object:
        """"""
    @overload
    def ConvertToInvariantString(self, context: ITypeDescriptorContext, value: object) -> str:
        """"""
    @overload
    def ConvertToInvariantString(self, value: object) -> str:
        """"""
    @overload
    def ConvertToString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> str:
        """"""
    @overload
    def ConvertToString(self, context: ITypeDescriptorContext, value: object) -> str:
        """"""
    @overload
    def ConvertToString(self, value: object) -> str:
        """"""
    @overload
    def CreateInstance(self, propertyValues: IDictionary) -> object:
        """"""
    @overload
    def CreateInstance(
        self, context: ITypeDescriptorContext, propertyValues: IDictionary
    ) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetCreateInstanceSupported(self) -> bool:
        """"""
    @overload
    def GetCreateInstanceSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object
    ) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]
    ) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetProperties(self, value: object) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetPropertiesSupported(self) -> bool:
        """"""
    @overload
    def GetPropertiesSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    @overload
    def GetStandardValues(self) -> ICollection:
        """"""
    @overload
    def GetStandardValues(
        self, context: ITypeDescriptorContext
    ) -> TypeConverter.StandardValuesCollection:
        """"""
    @overload
    def GetStandardValuesExclusive(self) -> bool:
        """"""
    @overload
    def GetStandardValuesExclusive(self, context: ITypeDescriptorContext) -> bool:
        """"""
    @overload
    def GetStandardValuesSupported(self) -> bool:
        """"""
    @overload
    def GetStandardValuesSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IsValid(self, context: ITypeDescriptorContext, value: object) -> bool:
        """"""
    @overload
    def IsValid(self, value: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    # noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
    class StandardValuesCollection(Object, ICollection, IEnumerable):
        """"""
        def __init__(self, values: ICollection) -> None:
            """"""
        @property
        def Count(self) -> int:
            """"""
        @property
        def IsSynchronized(self) -> bool:
            """"""
        @property
        def Item(self) -> object:
            """"""
        @property
        def SyncRoot(self) -> object:
            """"""
        def CopyTo(self, array: Array, index: int) -> None:
            """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def GetEnumerator(self) -> IEnumerator:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def ToString(self) -> str:
            """"""
        def __iter__(self) -> Iterator:
            """"""
        def __len__(self) -> int:
            """"""
        def __getitem__(self, index: int) -> object:
            """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class HandledEventArgs(EventArgs):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, defaultHandledValue: bool) -> None:
        """"""
    @property
    def Handled(self) -> bool:
        """"""
    @Handled.setter
    def Handled(self, value: bool) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

type HandledEventHandler = Callable[[object, HandledEventArgs], None]
""""""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IBindingList(ABC, ICollection, IEnumerable, IList):
    """"""
    @property
    def AllowEdit(self) -> bool:
        """"""
    @property
    def AllowNew(self) -> bool:
        """"""
    @property
    def AllowRemove(self) -> bool:
        """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsFixedSize(self) -> bool:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def IsSorted(self) -> bool:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def Item(self) -> object:
        """"""
    @Item.setter
    def Item(self, value: object) -> None: ...
    @property
    def SortDirection(self) -> ListSortDirection:
        """"""
    @property
    def SortProperty(self) -> PropertyDescriptor:
        """"""
    @property
    def SupportsChangeNotification(self) -> bool:
        """"""
    @property
    def SupportsSearching(self) -> bool:
        """"""
    @property
    def SupportsSorting(self) -> bool:
        """"""
    @property
    def SyncRoot(self) -> object:
        """"""
    def Add(self, value: object) -> int:
        """"""
    def AddIndex(self, property: PropertyDescriptor) -> None:
        """"""
    def AddNew(self) -> object:
        """"""
    def ApplySort(self, property: PropertyDescriptor, direction: ListSortDirection) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    def Contains(self, value: object) -> bool:
        """"""
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    def Find(self, property: PropertyDescriptor, key: object) -> int:
        """"""
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def IndexOf(self, value: object) -> int:
        """"""
    def Insert(self, index: int, value: object) -> None:
        """"""
    def Remove(self, value: object) -> None:
        """"""
    def RemoveAt(self, index: int) -> None:
        """"""
    def RemoveIndex(self, property: PropertyDescriptor) -> None:
        """"""
    def RemoveSort(self) -> None:
        """"""
    def __contains__(self, value: object) -> bool:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    def __delitem__(self, value: object) -> None:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, index: int) -> object:
        """"""
    def __setitem__(self, index: int, value: object) -> None:
        """"""
    ListChanged: EventType[ListChangedEventHandler] = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IBindingListView(ABC, ICollection, IEnumerable, IList, IBindingList):
    """"""
    @property
    def AllowEdit(self) -> bool:
        """"""
    @property
    def AllowNew(self) -> bool:
        """"""
    @property
    def AllowRemove(self) -> bool:
        """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def Filter(self) -> str:
        """"""
    @Filter.setter
    def Filter(self, value: str) -> None: ...
    @property
    def IsFixedSize(self) -> bool:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def IsSorted(self) -> bool:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def Item(self) -> object:
        """"""
    @Item.setter
    def Item(self, value: object) -> None: ...
    @property
    def SortDescriptions(self) -> ListSortDescriptionCollection:
        """"""
    @property
    def SortDirection(self) -> ListSortDirection:
        """"""
    @property
    def SortProperty(self) -> PropertyDescriptor:
        """"""
    @property
    def SupportsAdvancedSorting(self) -> bool:
        """"""
    @property
    def SupportsChangeNotification(self) -> bool:
        """"""
    @property
    def SupportsFiltering(self) -> bool:
        """"""
    @property
    def SupportsSearching(self) -> bool:
        """"""
    @property
    def SupportsSorting(self) -> bool:
        """"""
    @property
    def SyncRoot(self) -> object:
        """"""
    def Add(self, value: object) -> int:
        """"""
    def AddIndex(self, property: PropertyDescriptor) -> None:
        """"""
    def AddNew(self) -> object:
        """"""
    @overload
    def ApplySort(self, sorts: ListSortDescriptionCollection) -> None:
        """"""
    @overload
    def ApplySort(self, property: PropertyDescriptor, direction: ListSortDirection) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    def Contains(self, value: object) -> bool:
        """"""
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    def Find(self, property: PropertyDescriptor, key: object) -> int:
        """"""
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def IndexOf(self, value: object) -> int:
        """"""
    def Insert(self, index: int, value: object) -> None:
        """"""
    def Remove(self, value: object) -> None:
        """"""
    def RemoveAt(self, index: int) -> None:
        """"""
    def RemoveFilter(self) -> None:
        """"""
    def RemoveIndex(self, property: PropertyDescriptor) -> None:
        """"""
    def RemoveSort(self) -> None:
        """"""
    def __contains__(self, value: object) -> bool:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    def __delitem__(self, value: object) -> None:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, index: int) -> object:
        """"""
    def __setitem__(self, index: int, value: object) -> None:
        """"""
    ListChanged: EventType[ListChangedEventHandler] = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ICancelAddNew(ABC):
    """"""
    def CancelNew(self, itemIndex: int) -> None:
        """"""
    def EndNew(self, itemIndex: int) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IChangeTracking(ABC):
    """"""
    @property
    def IsChanged(self) -> bool:
        """"""
    def AcceptChanges(self) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IComNativeDescriptorHandler(ABC):
    """"""
    def GetAttributes(self, component: object) -> AttributeCollection:
        """"""
    def GetClassName(self, component: object) -> str:
        """"""
    def GetConverter(self, component: object) -> TypeConverter:
        """"""
    def GetDefaultEvent(self, component: object) -> EventDescriptor:
        """"""
    def GetDefaultProperty(self, component: object) -> PropertyDescriptor:
        """"""
    def GetEditor(self, component: object, baseEditorType: Type) -> object:
        """"""
    @overload
    def GetEvents(self, component: object) -> EventDescriptorCollection:
        """"""
    @overload
    def GetEvents(
        self, component: object, attributes: Array[Attribute]
    ) -> EventDescriptorCollection:
        """"""
    def GetName(self, component: object) -> str:
        """"""
    def GetProperties(
        self, component: object, attributes: Array[Attribute]
    ) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetPropertyValue(self, component: object, dispid: int, success: Boolean) -> object:
        """"""
    @overload
    def GetPropertyValue(self, component: object, propertyName: str, success: Boolean) -> object:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IComponent(ABC, IDisposable):
    """"""
    @property
    def Site(self) -> ISite:
        """"""
    @Site.setter
    def Site(self, value: ISite) -> None: ...
    def Dispose(self) -> None:
        """"""
    Disposed: EventType[EventHandler] = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IContainer(ABC, IDisposable):
    """"""
    @property
    def Components(self) -> ComponentCollection:
        """"""
    @overload
    def Add(self, component: IComponent) -> None:
        """"""
    @overload
    def Add(self, component: IComponent, name: str) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Remove(self, component: IComponent) -> None:
        """"""
    def __delitem__(self, component: IComponent) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ICustomTypeDescriptor(ABC):
    """"""
    def GetAttributes(self) -> AttributeCollection:
        """"""
    def GetClassName(self) -> str:
        """"""
    def GetComponentName(self) -> str:
        """"""
    def GetConverter(self) -> TypeConverter:
        """"""
    def GetDefaultEvent(self) -> EventDescriptor:
        """"""
    def GetDefaultProperty(self) -> PropertyDescriptor:
        """"""
    def GetEditor(self, editorBaseType: Type) -> object:
        """"""
    @overload
    def GetEvents(self) -> EventDescriptorCollection:
        """"""
    @overload
    def GetEvents(self, attributes: Array[Attribute]) -> EventDescriptorCollection:
        """"""
    @overload
    def GetProperties(self) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetProperties(self, attributes: Array[Attribute]) -> PropertyDescriptorCollection:
        """"""
    def GetPropertyOwner(self, pd: PropertyDescriptor) -> object:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IDataErrorInfo(ABC):
    """"""
    @property
    def Error(self) -> str:
        """"""
    @property
    def Item(self) -> str:
        """"""
    def __getitem__(self, columnName: str) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IEditableObject(ABC):
    """"""
    def BeginEdit(self) -> None:
        """"""
    def CancelEdit(self) -> None:
        """"""
    def EndEdit(self) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IExtenderProvider(ABC):
    """"""
    def CanExtend(self, extendee: object) -> bool:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IIntellisenseBuilder(ABC):
    """"""
    @property
    def Name(self) -> str:
        """"""
    def Show(self, language: str, value: str, newValue: String) -> bool:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IListSource(ABC):
    """"""
    @property
    def ContainsListCollection(self) -> bool:
        """"""
    def GetList(self) -> IList:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class INestedContainer(ABC, IContainer, IDisposable):
    """"""
    @property
    def Components(self) -> ComponentCollection:
        """"""
    @property
    def Owner(self) -> IComponent:
        """"""
    @overload
    def Add(self, component: IComponent) -> None:
        """"""
    @overload
    def Add(self, component: IComponent, name: str) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Remove(self, component: IComponent) -> None:
        """"""
    def __delitem__(self, component: IComponent) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class INestedSite(ABC, ISite, IServiceProvider):
    """"""
    @property
    def Component(self) -> IComponent:
        """"""
    @property
    def Container(self) -> IContainer:
        """"""
    @property
    def DesignMode(self) -> bool:
        """"""
    @property
    def FullName(self) -> str:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @Name.setter
    def Name(self, value: str) -> None: ...
    def GetService(self, serviceType: Type) -> object:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class INotifyDataErrorInfo(ABC):
    """"""
    @property
    def HasErrors(self) -> bool:
        """"""
    def GetErrors(self, propertyName: str) -> IEnumerable:
        """"""
    ErrorsChanged: EventType[EventHandler[DataErrorsChangedEventArgs]] = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class INotifyPropertyChanged(ABC):
    """"""

    PropertyChanged: EventType[PropertyChangedEventHandler] = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class INotifyPropertyChanging(ABC):
    """"""

    PropertyChanging: EventType[PropertyChangingEventHandler] = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IRaiseItemChangedEvents(ABC):
    """"""
    @property
    def RaisesItemChangedEvents(self) -> bool:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IRevertibleChangeTracking(ABC, IChangeTracking):
    """"""
    @property
    def IsChanged(self) -> bool:
        """"""
    def AcceptChanges(self) -> None:
        """"""
    def RejectChanges(self) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ISite(ABC, IServiceProvider):
    """"""
    @property
    def Component(self) -> IComponent:
        """"""
    @property
    def Container(self) -> IContainer:
        """"""
    @property
    def DesignMode(self) -> bool:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @Name.setter
    def Name(self, value: str) -> None: ...
    def GetService(self, serviceType: Type) -> object:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ISupportInitialize(ABC):
    """"""
    def BeginInit(self) -> None:
        """"""
    def EndInit(self) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ISupportInitializeNotification(ABC, ISupportInitialize):
    """"""
    @property
    def IsInitialized(self) -> bool:
        """"""
    def BeginInit(self) -> None:
        """"""
    def EndInit(self) -> None:
        """"""
    Initialized: EventType[EventHandler] = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ISynchronizeInvoke(ABC):
    """"""
    @property
    def InvokeRequired(self) -> bool:
        """"""
    def BeginInvoke(self, method: Delegate, args: Array[object]) -> IAsyncResult:
        """"""
    def EndInvoke(self, result: IAsyncResult) -> object:
        """"""
    def Invoke(self, method: Delegate, args: Array[object]) -> object:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ITypeDescriptorContext(ABC, IServiceProvider):
    """"""
    @property
    def Container(self) -> IContainer:
        """"""
    @property
    def Instance(self) -> object:
        """"""
    @property
    def PropertyDescriptor(self) -> PropertyDescriptor:
        """"""
    def GetService(self, serviceType: Type) -> object:
        """"""
    def OnComponentChanged(self) -> None:
        """"""
    def OnComponentChanging(self) -> bool:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ITypedList(ABC):
    """"""
    def GetItemProperties(
        self, listAccessors: Array[PropertyDescriptor]
    ) -> PropertyDescriptorCollection:
        """"""
    def GetListName(self, listAccessors: Array[PropertyDescriptor]) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ImmutableObjectAttribute(Attribute, _Attribute):
    """"""

    Default: ClassVar[ImmutableObjectAttribute]
    """"""
    No: ClassVar[ImmutableObjectAttribute]
    """"""
    Yes: ClassVar[ImmutableObjectAttribute]
    """"""
    def __init__(self, immutable: bool) -> None:
        """"""
    @property
    def Immutable(self) -> bool:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class InheritanceAttribute(Attribute, _Attribute):
    """"""

    Default: ClassVar[InheritanceAttribute]
    """"""
    Inherited: ClassVar[InheritanceAttribute]
    """"""
    InheritedReadOnly: ClassVar[InheritanceAttribute]
    """"""
    NotInherited: ClassVar[InheritanceAttribute]
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, inheritanceLevel: InheritanceLevel) -> None:
        """"""
    @property
    def InheritanceLevel(self) -> InheritanceLevel:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
    def Equals(self, value: object) -> bool:
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

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class InheritanceLevel(Enum):
    """"""

    Inherited: InheritanceLevel = ...
    """"""
    InheritedReadOnly: InheritanceLevel = ...
    """"""
    NotInherited: InheritanceLevel = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class InitializationEventAttribute(Attribute, _Attribute):
    """"""
    def __init__(self, eventName: str) -> None:
        """"""
    @property
    def EventName(self) -> str:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class InstallerTypeAttribute(Attribute, _Attribute):
    """"""
    @overload
    def __init__(self, installerType: Type) -> None:
        """"""
    @overload
    def __init__(self, typeName: str) -> None:
        """"""
    @property
    def InstallerType(self) -> Type:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class InstanceCreationEditor(ABC, Object):
    """"""
    @property
    def Text(self) -> str:
        """"""
    def CreateInstance(self, context: ITypeDescriptorContext, instanceType: Type) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class Int16Converter(BaseNumberConverter):
    """"""
    def __init__(self) -> None:
        """"""
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool:
        """"""
    @overload
    def CanConvertFrom(self, sourceType: Type) -> bool:
        """"""
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, t: Type) -> bool:
        """"""
    @overload
    def CanConvertTo(self, destinationType: Type) -> bool:
        """"""
    @overload
    def ConvertFrom(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> object:
        """"""
    @overload
    def ConvertFrom(self, value: object) -> object:
        """"""
    @overload
    def ConvertFromInvariantString(self, context: ITypeDescriptorContext, text: str) -> object:
        """"""
    @overload
    def ConvertFromInvariantString(self, text: str) -> object:
        """"""
    @overload
    def ConvertFromString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, text: str
    ) -> object:
        """"""
    @overload
    def ConvertFromString(self, context: ITypeDescriptorContext, text: str) -> object:
        """"""
    @overload
    def ConvertFromString(self, text: str) -> object:
        """"""
    @overload
    def ConvertTo(
        self,
        context: ITypeDescriptorContext,
        culture: CultureInfo,
        value: object,
        destinationType: Type,
    ) -> object:
        """"""
    @overload
    def ConvertTo(self, value: object, destinationType: Type) -> object:
        """"""
    @overload
    def ConvertToInvariantString(self, context: ITypeDescriptorContext, value: object) -> str:
        """"""
    @overload
    def ConvertToInvariantString(self, value: object) -> str:
        """"""
    @overload
    def ConvertToString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> str:
        """"""
    @overload
    def ConvertToString(self, context: ITypeDescriptorContext, value: object) -> str:
        """"""
    @overload
    def ConvertToString(self, value: object) -> str:
        """"""
    @overload
    def CreateInstance(self, propertyValues: IDictionary) -> object:
        """"""
    @overload
    def CreateInstance(
        self, context: ITypeDescriptorContext, propertyValues: IDictionary
    ) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetCreateInstanceSupported(self) -> bool:
        """"""
    @overload
    def GetCreateInstanceSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object
    ) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]
    ) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetProperties(self, value: object) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetPropertiesSupported(self) -> bool:
        """"""
    @overload
    def GetPropertiesSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    @overload
    def GetStandardValues(self) -> ICollection:
        """"""
    @overload
    def GetStandardValues(
        self, context: ITypeDescriptorContext
    ) -> TypeConverter.StandardValuesCollection:
        """"""
    @overload
    def GetStandardValuesExclusive(self) -> bool:
        """"""
    @overload
    def GetStandardValuesExclusive(self, context: ITypeDescriptorContext) -> bool:
        """"""
    @overload
    def GetStandardValuesSupported(self) -> bool:
        """"""
    @overload
    def GetStandardValuesSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IsValid(self, context: ITypeDescriptorContext, value: object) -> bool:
        """"""
    @overload
    def IsValid(self, value: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    # noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
    class StandardValuesCollection(Object, ICollection, IEnumerable):
        """"""
        def __init__(self, values: ICollection) -> None:
            """"""
        @property
        def Count(self) -> int:
            """"""
        @property
        def IsSynchronized(self) -> bool:
            """"""
        @property
        def Item(self) -> object:
            """"""
        @property
        def SyncRoot(self) -> object:
            """"""
        def CopyTo(self, array: Array, index: int) -> None:
            """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def GetEnumerator(self) -> IEnumerator:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def ToString(self) -> str:
            """"""
        def __iter__(self) -> Iterator:
            """"""
        def __len__(self) -> int:
            """"""
        def __getitem__(self, index: int) -> object:
            """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class Int32Converter(BaseNumberConverter):
    """"""
    def __init__(self) -> None:
        """"""
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool:
        """"""
    @overload
    def CanConvertFrom(self, sourceType: Type) -> bool:
        """"""
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, t: Type) -> bool:
        """"""
    @overload
    def CanConvertTo(self, destinationType: Type) -> bool:
        """"""
    @overload
    def ConvertFrom(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> object:
        """"""
    @overload
    def ConvertFrom(self, value: object) -> object:
        """"""
    @overload
    def ConvertFromInvariantString(self, context: ITypeDescriptorContext, text: str) -> object:
        """"""
    @overload
    def ConvertFromInvariantString(self, text: str) -> object:
        """"""
    @overload
    def ConvertFromString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, text: str
    ) -> object:
        """"""
    @overload
    def ConvertFromString(self, context: ITypeDescriptorContext, text: str) -> object:
        """"""
    @overload
    def ConvertFromString(self, text: str) -> object:
        """"""
    @overload
    def ConvertTo(
        self,
        context: ITypeDescriptorContext,
        culture: CultureInfo,
        value: object,
        destinationType: Type,
    ) -> object:
        """"""
    @overload
    def ConvertTo(self, value: object, destinationType: Type) -> object:
        """"""
    @overload
    def ConvertToInvariantString(self, context: ITypeDescriptorContext, value: object) -> str:
        """"""
    @overload
    def ConvertToInvariantString(self, value: object) -> str:
        """"""
    @overload
    def ConvertToString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> str:
        """"""
    @overload
    def ConvertToString(self, context: ITypeDescriptorContext, value: object) -> str:
        """"""
    @overload
    def ConvertToString(self, value: object) -> str:
        """"""
    @overload
    def CreateInstance(self, propertyValues: IDictionary) -> object:
        """"""
    @overload
    def CreateInstance(
        self, context: ITypeDescriptorContext, propertyValues: IDictionary
    ) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetCreateInstanceSupported(self) -> bool:
        """"""
    @overload
    def GetCreateInstanceSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object
    ) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]
    ) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetProperties(self, value: object) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetPropertiesSupported(self) -> bool:
        """"""
    @overload
    def GetPropertiesSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    @overload
    def GetStandardValues(self) -> ICollection:
        """"""
    @overload
    def GetStandardValues(
        self, context: ITypeDescriptorContext
    ) -> TypeConverter.StandardValuesCollection:
        """"""
    @overload
    def GetStandardValuesExclusive(self) -> bool:
        """"""
    @overload
    def GetStandardValuesExclusive(self, context: ITypeDescriptorContext) -> bool:
        """"""
    @overload
    def GetStandardValuesSupported(self) -> bool:
        """"""
    @overload
    def GetStandardValuesSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IsValid(self, context: ITypeDescriptorContext, value: object) -> bool:
        """"""
    @overload
    def IsValid(self, value: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    # noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
    class StandardValuesCollection(Object, ICollection, IEnumerable):
        """"""
        def __init__(self, values: ICollection) -> None:
            """"""
        @property
        def Count(self) -> int:
            """"""
        @property
        def IsSynchronized(self) -> bool:
            """"""
        @property
        def Item(self) -> object:
            """"""
        @property
        def SyncRoot(self) -> object:
            """"""
        def CopyTo(self, array: Array, index: int) -> None:
            """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def GetEnumerator(self) -> IEnumerator:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def ToString(self) -> str:
            """"""
        def __iter__(self) -> Iterator:
            """"""
        def __len__(self) -> int:
            """"""
        def __getitem__(self, index: int) -> object:
            """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class Int64Converter(BaseNumberConverter):
    """"""
    def __init__(self) -> None:
        """"""
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool:
        """"""
    @overload
    def CanConvertFrom(self, sourceType: Type) -> bool:
        """"""
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, t: Type) -> bool:
        """"""
    @overload
    def CanConvertTo(self, destinationType: Type) -> bool:
        """"""
    @overload
    def ConvertFrom(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> object:
        """"""
    @overload
    def ConvertFrom(self, value: object) -> object:
        """"""
    @overload
    def ConvertFromInvariantString(self, context: ITypeDescriptorContext, text: str) -> object:
        """"""
    @overload
    def ConvertFromInvariantString(self, text: str) -> object:
        """"""
    @overload
    def ConvertFromString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, text: str
    ) -> object:
        """"""
    @overload
    def ConvertFromString(self, context: ITypeDescriptorContext, text: str) -> object:
        """"""
    @overload
    def ConvertFromString(self, text: str) -> object:
        """"""
    @overload
    def ConvertTo(
        self,
        context: ITypeDescriptorContext,
        culture: CultureInfo,
        value: object,
        destinationType: Type,
    ) -> object:
        """"""
    @overload
    def ConvertTo(self, value: object, destinationType: Type) -> object:
        """"""
    @overload
    def ConvertToInvariantString(self, context: ITypeDescriptorContext, value: object) -> str:
        """"""
    @overload
    def ConvertToInvariantString(self, value: object) -> str:
        """"""
    @overload
    def ConvertToString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> str:
        """"""
    @overload
    def ConvertToString(self, context: ITypeDescriptorContext, value: object) -> str:
        """"""
    @overload
    def ConvertToString(self, value: object) -> str:
        """"""
    @overload
    def CreateInstance(self, propertyValues: IDictionary) -> object:
        """"""
    @overload
    def CreateInstance(
        self, context: ITypeDescriptorContext, propertyValues: IDictionary
    ) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetCreateInstanceSupported(self) -> bool:
        """"""
    @overload
    def GetCreateInstanceSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object
    ) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]
    ) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetProperties(self, value: object) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetPropertiesSupported(self) -> bool:
        """"""
    @overload
    def GetPropertiesSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    @overload
    def GetStandardValues(self) -> ICollection:
        """"""
    @overload
    def GetStandardValues(
        self, context: ITypeDescriptorContext
    ) -> TypeConverter.StandardValuesCollection:
        """"""
    @overload
    def GetStandardValuesExclusive(self) -> bool:
        """"""
    @overload
    def GetStandardValuesExclusive(self, context: ITypeDescriptorContext) -> bool:
        """"""
    @overload
    def GetStandardValuesSupported(self) -> bool:
        """"""
    @overload
    def GetStandardValuesSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IsValid(self, context: ITypeDescriptorContext, value: object) -> bool:
        """"""
    @overload
    def IsValid(self, value: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    # noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
    class StandardValuesCollection(Object, ICollection, IEnumerable):
        """"""
        def __init__(self, values: ICollection) -> None:
            """"""
        @property
        def Count(self) -> int:
            """"""
        @property
        def IsSynchronized(self) -> bool:
            """"""
        @property
        def Item(self) -> object:
            """"""
        @property
        def SyncRoot(self) -> object:
            """"""
        def CopyTo(self, array: Array, index: int) -> None:
            """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def GetEnumerator(self) -> IEnumerator:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def ToString(self) -> str:
            """"""
        def __iter__(self) -> Iterator:
            """"""
        def __len__(self) -> int:
            """"""
        def __getitem__(self, index: int) -> object:
            """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IntSecurity(ABC, Object):
    """"""

    FullReflection: ClassVar[CodeAccessPermission]
    """"""
    UnmanagedCode: ClassVar[CodeAccessPermission]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def UnsafeGetFullPath(cls, fileName: str) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class InvalidAsynchronousStateException(ArgumentException, _Exception, ISerializable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, message: str) -> None:
        """"""
    @overload
    def __init__(self, message: str, innerException: Exception) -> None:
        """"""
    @property
    def Data(self) -> IDictionary:
        """"""
    @property
    def HResult(self) -> int:
        """"""
    @property
    def HelpLink(self) -> str:
        """"""
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """"""
    @property
    def Message(self) -> str:
        """"""
    @property
    def ParamName(self) -> str:
        """"""
    @property
    def Source(self) -> str:
        """"""
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """"""
    @property
    def TargetSite(self) -> MethodBase:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetBaseException(self) -> Exception:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class InvalidEnumArgumentException(ArgumentException, _Exception, ISerializable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, message: str) -> None:
        """"""
    @overload
    def __init__(self, message: str, innerException: Exception) -> None:
        """"""
    @overload
    def __init__(self, argumentName: str, invalidValue: int, enumClass: Type) -> None:
        """"""
    @property
    def Data(self) -> IDictionary:
        """"""
    @property
    def HResult(self) -> int:
        """"""
    @property
    def HelpLink(self) -> str:
        """"""
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """"""
    @property
    def Message(self) -> str:
        """"""
    @property
    def ParamName(self) -> str:
        """"""
    @property
    def Source(self) -> str:
        """"""
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """"""
    @property
    def TargetSite(self) -> MethodBase:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetBaseException(self) -> Exception:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class LicFileLicenseProvider(LicenseProvider):
    """"""
    def __init__(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetLicense(
        self, context: LicenseContext, type: Type, instance: object, allowExceptions: bool
    ) -> License:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class License(ABC, Object, IDisposable):
    """"""
    @property
    def LicenseKey(self) -> str:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class LicenseContext(Object, IServiceProvider):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def UsageMode(self) -> LicenseUsageMode:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetSavedLicenseKey(self, type: Type, resourceAssembly: Assembly) -> str:
        """"""
    def GetService(self, type: Type) -> object:
        """"""
    def GetType(self) -> Type:
        """"""
    def SetSavedLicenseKey(self, type: Type, key: str) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class LicenseException(SystemException, _Exception, ISerializable):
    """"""
    @overload
    def __init__(self, type: Type) -> None:
        """"""
    @overload
    def __init__(self, type: Type, instance: object) -> None:
        """"""
    @overload
    def __init__(self, type: Type, instance: object, message: str) -> None:
        """"""
    @overload
    def __init__(
        self, type: Type, instance: object, message: str, innerException: Exception
    ) -> None:
        """"""
    @property
    def Data(self) -> IDictionary:
        """"""
    @property
    def HResult(self) -> int:
        """"""
    @property
    def HelpLink(self) -> str:
        """"""
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """"""
    @property
    def LicensedType(self) -> Type:
        """"""
    @property
    def Message(self) -> str:
        """"""
    @property
    def Source(self) -> str:
        """"""
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """"""
    @property
    def TargetSite(self) -> MethodBase:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetBaseException(self) -> Exception:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class LicenseManager(Object):
    """"""
    @classmethod
    @property
    def CurrentContext(cls) -> LicenseContext:
        """"""
    @classmethod
    @CurrentContext.setter
    def CurrentContext(cls, value: LicenseContext) -> None: ...
    @classmethod
    @property
    def UsageMode(cls) -> LicenseUsageMode:
        """"""
    @classmethod
    @overload
    def CreateWithContext(cls, type: Type, creationContext: LicenseContext) -> object:
        """"""
    @classmethod
    @overload
    def CreateWithContext(
        cls, type: Type, creationContext: LicenseContext, args: Array[object]
    ) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def IsLicensed(cls, type: Type) -> bool:
        """"""
    @classmethod
    @overload
    def IsValid(cls, type: Type) -> bool:
        """"""
    @classmethod
    @overload
    def IsValid(cls, type: Type, instance: object, license: License) -> tuple[bool, License]:
        """"""
    @classmethod
    def LockContext(cls, contextUser: object) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def UnlockContext(cls, contextUser: object) -> None:
        """"""
    @classmethod
    @overload
    def Validate(cls, type: Type) -> None:
        """"""
    @classmethod
    @overload
    def Validate(cls, type: Type, instance: object) -> License:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class LicenseProvider(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetLicense(
        self, context: LicenseContext, type: Type, instance: object, allowExceptions: bool
    ) -> License:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class LicenseProviderAttribute(Attribute, _Attribute):
    """"""

    Default: ClassVar[LicenseProviderAttribute]
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, typeName: str) -> None:
        """"""
    @overload
    def __init__(self, type: Type) -> None:
        """"""
    @property
    def LicenseProvider(self) -> Type:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
    def Equals(self, value: object) -> bool:
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

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class LicenseUsageMode(Enum):
    """"""

    Runtime: LicenseUsageMode = ...
    """"""
    Designtime: LicenseUsageMode = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ListBindableAttribute(Attribute, _Attribute):
    """"""

    Default: ClassVar[ListBindableAttribute]
    """"""
    No: ClassVar[ListBindableAttribute]
    """"""
    Yes: ClassVar[ListBindableAttribute]
    """"""
    @overload
    def __init__(self, listBindable: bool) -> None:
        """"""
    @overload
    def __init__(self, flags: BindableSupport) -> None:
        """"""
    @property
    def ListBindable(self) -> bool:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ListChangedEventArgs(EventArgs):
    """"""
    @overload
    def __init__(self, listChangedType: ListChangedType, newIndex: int) -> None:
        """"""
    @overload
    def __init__(
        self, listChangedType: ListChangedType, newIndex: int, propDesc: PropertyDescriptor
    ) -> None:
        """"""
    @overload
    def __init__(self, listChangedType: ListChangedType, propDesc: PropertyDescriptor) -> None:
        """"""
    @overload
    def __init__(self, listChangedType: ListChangedType, newIndex: int, oldIndex: int) -> None:
        """"""
    @property
    def ListChangedType(self) -> ListChangedType:
        """"""
    @property
    def NewIndex(self) -> int:
        """"""
    @property
    def OldIndex(self) -> int:
        """"""
    @property
    def PropertyDescriptor(self) -> PropertyDescriptor:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

type ListChangedEventHandler = Callable[[object, ListChangedEventArgs], None]
""""""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ListSortDescription(Object):
    """"""
    def __init__(self, property: PropertyDescriptor, direction: ListSortDirection) -> None:
        """"""
    @property
    def PropertyDescriptor(self) -> PropertyDescriptor:
        """"""
    @PropertyDescriptor.setter
    def PropertyDescriptor(self, value: PropertyDescriptor) -> None: ...
    @property
    def SortDirection(self) -> ListSortDirection:
        """"""
    @SortDirection.setter
    def SortDirection(self, value: ListSortDirection) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ListSortDescriptionCollection(Object, ICollection, IEnumerable, IList):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, sorts: Array[ListSortDescription]) -> None:
        """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsFixedSize(self) -> bool:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def Item(self) -> ListSortDescription:
        """"""
    @Item.setter
    def Item(self, value: ListSortDescription) -> None: ...
    @property
    def SyncRoot(self) -> object:
        """"""
    def Add(self, value: object) -> int:
        """"""
    def Clear(self) -> None:
        """"""
    def Contains(self, value: object) -> bool:
        """"""
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def IndexOf(self, value: object) -> int:
        """"""
    def Insert(self, index: int, value: object) -> None:
        """"""
    def Remove(self, value: object) -> None:
        """"""
    def RemoveAt(self, index: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def __contains__(self, value: object) -> bool:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    def __delitem__(self, value: object) -> None:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, index: int) -> ListSortDescription:
        """"""
    @overload
    def __setitem__(self, index: int, value: ListSortDescription) -> None:
        """"""
    @overload
    def __setitem__(self, index: int, value: object) -> None:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class ListSortDirection(Enum):
    """"""

    Ascending: ListSortDirection = ...
    """"""
    Descending: ListSortDirection = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class LocalizableAttribute(Attribute, _Attribute):
    """"""

    Default: ClassVar[LocalizableAttribute]
    """"""
    No: ClassVar[LocalizableAttribute]
    """"""
    Yes: ClassVar[LocalizableAttribute]
    """"""
    def __init__(self, isLocalizable: bool) -> None:
        """"""
    @property
    def IsLocalizable(self) -> bool:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class LookupBindingPropertiesAttribute(Attribute, _Attribute):
    """"""

    Default: ClassVar[LookupBindingPropertiesAttribute]
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(
        self, dataSource: str, displayMember: str, valueMember: str, lookupMember: str
    ) -> None:
        """"""
    @property
    def DataSource(self) -> str:
        """"""
    @property
    def DisplayMember(self) -> str:
        """"""
    @property
    def LookupMember(self) -> str:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
    @property
    def ValueMember(self) -> str:
        """"""
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class MarshalByValueComponent(Object, IComponent, IDisposable, IServiceProvider):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Container(self) -> IContainer:
        """"""
    @property
    def DesignMode(self) -> bool:
        """"""
    @property
    def Site(self) -> ISite:
        """"""
    @Site.setter
    def Site(self, value: ISite) -> None: ...
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetService(self, service: Type) -> object:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    Disposed: EventType[EventHandler] = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class MaskedTextProvider(Object, ICloneable):
    """"""
    @overload
    def __init__(self, mask: str) -> None:
        """"""
    @overload
    def __init__(self, mask: str, restrictToAscii: bool) -> None:
        """"""
    @overload
    def __init__(self, mask: str, culture: CultureInfo) -> None:
        """"""
    @overload
    def __init__(self, mask: str, culture: CultureInfo, restrictToAscii: bool) -> None:
        """"""
    @overload
    def __init__(self, mask: str, passwordChar: Char, allowPromptAsInput: bool) -> None:
        """"""
    @overload
    def __init__(
        self, mask: str, culture: CultureInfo, passwordChar: Char, allowPromptAsInput: bool
    ) -> None:
        """"""
    @overload
    def __init__(
        self,
        mask: str,
        culture: CultureInfo,
        allowPromptAsInput: bool,
        promptChar: Char,
        passwordChar: Char,
        restrictToAscii: bool,
    ) -> None:
        """"""
    @property
    def AllowPromptAsInput(self) -> bool:
        """"""
    @property
    def AsciiOnly(self) -> bool:
        """"""
    @property
    def AssignedEditPositionCount(self) -> int:
        """"""
    @property
    def AvailableEditPositionCount(self) -> int:
        """"""
    @property
    def Culture(self) -> CultureInfo:
        """"""
    @classmethod
    @property
    def DefaultPasswordChar(cls) -> Char:
        """"""
    @property
    def EditPositionCount(self) -> int:
        """"""
    @property
    def EditPositions(self) -> IEnumerator:
        """"""
    @property
    def IncludeLiterals(self) -> bool:
        """"""
    @IncludeLiterals.setter
    def IncludeLiterals(self, value: bool) -> None: ...
    @property
    def IncludePrompt(self) -> bool:
        """"""
    @IncludePrompt.setter
    def IncludePrompt(self, value: bool) -> None: ...
    @classmethod
    @property
    def InvalidIndex(cls) -> int:
        """"""
    @property
    def IsPassword(self) -> bool:
        """"""
    @IsPassword.setter
    def IsPassword(self, value: bool) -> None: ...
    @property
    def Item(self) -> Char:
        """"""
    @property
    def LastAssignedPosition(self) -> int:
        """"""
    @property
    def Length(self) -> int:
        """"""
    @property
    def Mask(self) -> str:
        """"""
    @property
    def MaskCompleted(self) -> bool:
        """"""
    @property
    def MaskFull(self) -> bool:
        """"""
    @property
    def PasswordChar(self) -> Char:
        """"""
    @PasswordChar.setter
    def PasswordChar(self, value: Char) -> None: ...
    @property
    def PromptChar(self) -> Char:
        """"""
    @PromptChar.setter
    def PromptChar(self, value: Char) -> None: ...
    @property
    def ResetOnPrompt(self) -> bool:
        """"""
    @ResetOnPrompt.setter
    def ResetOnPrompt(self, value: bool) -> None: ...
    @property
    def ResetOnSpace(self) -> bool:
        """"""
    @ResetOnSpace.setter
    def ResetOnSpace(self, value: bool) -> None: ...
    @property
    def SkipLiterals(self) -> bool:
        """"""
    @SkipLiterals.setter
    def SkipLiterals(self, value: bool) -> None: ...
    @overload
    def Add(self, input: Char) -> bool:
        """"""
    @overload
    def Add(
        self, input: Char, testPosition: Int32, resultHint: MaskedTextResultHint
    ) -> tuple[bool, Int32, MaskedTextResultHint]:
        """"""
    @overload
    def Add(self, input: str) -> bool:
        """"""
    @overload
    def Add(
        self, input: str, testPosition: Int32, resultHint: MaskedTextResultHint
    ) -> tuple[bool, Int32, MaskedTextResultHint]:
        """"""
    @overload
    def Clear(self) -> None:
        """"""
    @overload
    def Clear(self, resultHint: MaskedTextResultHint) -> tuple[None, MaskedTextResultHint]:
        """"""
    def Clone(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def FindAssignedEditPositionFrom(self, position: int, direction: bool) -> int:
        """"""
    def FindAssignedEditPositionInRange(
        self, startPosition: int, endPosition: int, direction: bool
    ) -> int:
        """"""
    def FindEditPositionFrom(self, position: int, direction: bool) -> int:
        """"""
    def FindEditPositionInRange(self, startPosition: int, endPosition: int, direction: bool) -> int:
        """"""
    def FindNonEditPositionFrom(self, position: int, direction: bool) -> int:
        """"""
    def FindNonEditPositionInRange(
        self, startPosition: int, endPosition: int, direction: bool
    ) -> int:
        """"""
    def FindUnassignedEditPositionFrom(self, position: int, direction: bool) -> int:
        """"""
    def FindUnassignedEditPositionInRange(
        self, startPosition: int, endPosition: int, direction: bool
    ) -> int:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @classmethod
    def GetOperationResultFromHint(cls, hint: MaskedTextResultHint) -> bool:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def InsertAt(self, input: Char, position: int) -> bool:
        """"""
    @overload
    def InsertAt(
        self, input: Char, position: int, testPosition: Int32, resultHint: MaskedTextResultHint
    ) -> tuple[bool, Int32, MaskedTextResultHint]:
        """"""
    @overload
    def InsertAt(self, input: str, position: int) -> bool:
        """"""
    @overload
    def InsertAt(
        self, input: str, position: int, testPosition: Int32, resultHint: MaskedTextResultHint
    ) -> tuple[bool, Int32, MaskedTextResultHint]:
        """"""
    def IsAvailablePosition(self, position: int) -> bool:
        """"""
    def IsEditPosition(self, position: int) -> bool:
        """"""
    @classmethod
    def IsValidInputChar(cls, c: Char) -> bool:
        """"""
    @classmethod
    def IsValidMaskChar(cls, c: Char) -> bool:
        """"""
    @classmethod
    def IsValidPasswordChar(cls, c: Char) -> bool:
        """"""
    @overload
    def Remove(self) -> bool:
        """"""
    @overload
    def Remove(
        self, testPosition: Int32, resultHint: MaskedTextResultHint
    ) -> tuple[bool, Int32, MaskedTextResultHint]:
        """"""
    @overload
    def RemoveAt(self, position: int) -> bool:
        """"""
    @overload
    def RemoveAt(self, startPosition: int, endPosition: int) -> bool:
        """"""
    @overload
    def RemoveAt(
        self,
        startPosition: int,
        endPosition: int,
        testPosition: Int32,
        resultHint: MaskedTextResultHint,
    ) -> tuple[bool, Int32, MaskedTextResultHint]:
        """"""
    @overload
    def Replace(self, input: Char, position: int) -> bool:
        """"""
    @overload
    def Replace(
        self, input: Char, position: int, testPosition: Int32, resultHint: MaskedTextResultHint
    ) -> tuple[bool, Int32, MaskedTextResultHint]:
        """"""
    @overload
    def Replace(
        self,
        input: Char,
        startPosition: int,
        endPosition: int,
        testPosition: Int32,
        resultHint: MaskedTextResultHint,
    ) -> tuple[bool, Int32, MaskedTextResultHint]:
        """"""
    @overload
    def Replace(self, input: str, position: int) -> bool:
        """"""
    @overload
    def Replace(
        self, input: str, position: int, testPosition: Int32, resultHint: MaskedTextResultHint
    ) -> tuple[bool, Int32, MaskedTextResultHint]:
        """"""
    @overload
    def Replace(
        self,
        input: str,
        startPosition: int,
        endPosition: int,
        testPosition: Int32,
        resultHint: MaskedTextResultHint,
    ) -> tuple[bool, Int32, MaskedTextResultHint]:
        """"""
    @overload
    def Set(self, input: str) -> bool:
        """"""
    @overload
    def Set(
        self, input: str, testPosition: Int32, resultHint: MaskedTextResultHint
    ) -> tuple[bool, Int32, MaskedTextResultHint]:
        """"""
    def ToDisplayString(self) -> str:
        """"""
    @overload
    def ToString(self) -> str:
        """"""
    @overload
    def ToString(self, ignorePasswordChar: bool) -> str:
        """"""
    @overload
    def ToString(self, includePrompt: bool, includeLiterals: bool) -> str:
        """"""
    @overload
    def ToString(
        self,
        ignorePasswordChar: bool,
        includePrompt: bool,
        includeLiterals: bool,
        startPosition: int,
        length: int,
    ) -> str:
        """"""
    @overload
    def ToString(
        self, includePrompt: bool, includeLiterals: bool, startPosition: int, length: int
    ) -> str:
        """"""
    @overload
    def ToString(self, ignorePasswordChar: bool, startPosition: int, length: int) -> str:
        """"""
    @overload
    def ToString(self, startPosition: int, length: int) -> str:
        """"""
    def VerifyChar(
        self, input: Char, position: int, hint: MaskedTextResultHint
    ) -> tuple[bool, MaskedTextResultHint]:
        """"""
    def VerifyEscapeChar(self, input: Char, position: int) -> bool:
        """"""
    @overload
    def VerifyString(self, input: str) -> bool:
        """"""
    @overload
    def VerifyString(
        self, input: str, testPosition: Int32, resultHint: MaskedTextResultHint
    ) -> tuple[bool, Int32, MaskedTextResultHint]:
        """"""
    @overload
    def __delitem__(self) -> bool:
        """"""
    @overload
    def __delitem__(
        self, testPosition: Int32, resultHint: MaskedTextResultHint
    ) -> tuple[bool, Int32, MaskedTextResultHint]:
        """"""
    def __getitem__(self, index: int) -> Char:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class MemberDescriptor(ABC, Object):
    """"""
    @property
    def Attributes(self) -> AttributeCollection:
        """"""
    @property
    def Category(self) -> str:
        """"""
    @property
    def Description(self) -> str:
        """"""
    @property
    def DesignTimeOnly(self) -> bool:
        """"""
    @property
    def DisplayName(self) -> str:
        """"""
    @property
    def IsBrowsable(self) -> bool:
        """"""
    @property
    def Name(self) -> str:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class MergablePropertyAttribute(Attribute, _Attribute):
    """"""

    Default: ClassVar[MergablePropertyAttribute]
    """"""
    No: ClassVar[MergablePropertyAttribute]
    """"""
    Yes: ClassVar[MergablePropertyAttribute]
    """"""
    def __init__(self, allowMerge: bool) -> None:
        """"""
    @property
    def AllowMerge(self) -> bool:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class MultilineStringConverter(TypeConverter):
    """"""
    def __init__(self) -> None:
        """"""
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool:
        """"""
    @overload
    def CanConvertFrom(self, sourceType: Type) -> bool:
        """"""
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, destinationType: Type) -> bool:
        """"""
    @overload
    def CanConvertTo(self, destinationType: Type) -> bool:
        """"""
    @overload
    def ConvertFrom(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> object:
        """"""
    @overload
    def ConvertFrom(self, value: object) -> object:
        """"""
    @overload
    def ConvertFromInvariantString(self, context: ITypeDescriptorContext, text: str) -> object:
        """"""
    @overload
    def ConvertFromInvariantString(self, text: str) -> object:
        """"""
    @overload
    def ConvertFromString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, text: str
    ) -> object:
        """"""
    @overload
    def ConvertFromString(self, context: ITypeDescriptorContext, text: str) -> object:
        """"""
    @overload
    def ConvertFromString(self, text: str) -> object:
        """"""
    @overload
    def ConvertTo(
        self,
        context: ITypeDescriptorContext,
        culture: CultureInfo,
        value: object,
        destinationType: Type,
    ) -> object:
        """"""
    @overload
    def ConvertTo(self, value: object, destinationType: Type) -> object:
        """"""
    @overload
    def ConvertToInvariantString(self, context: ITypeDescriptorContext, value: object) -> str:
        """"""
    @overload
    def ConvertToInvariantString(self, value: object) -> str:
        """"""
    @overload
    def ConvertToString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> str:
        """"""
    @overload
    def ConvertToString(self, context: ITypeDescriptorContext, value: object) -> str:
        """"""
    @overload
    def ConvertToString(self, value: object) -> str:
        """"""
    @overload
    def CreateInstance(self, propertyValues: IDictionary) -> object:
        """"""
    @overload
    def CreateInstance(
        self, context: ITypeDescriptorContext, propertyValues: IDictionary
    ) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetCreateInstanceSupported(self) -> bool:
        """"""
    @overload
    def GetCreateInstanceSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object
    ) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]
    ) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetProperties(self, value: object) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetPropertiesSupported(self) -> bool:
        """"""
    @overload
    def GetPropertiesSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    @overload
    def GetStandardValues(self) -> ICollection:
        """"""
    @overload
    def GetStandardValues(
        self, context: ITypeDescriptorContext
    ) -> TypeConverter.StandardValuesCollection:
        """"""
    @overload
    def GetStandardValuesExclusive(self) -> bool:
        """"""
    @overload
    def GetStandardValuesExclusive(self, context: ITypeDescriptorContext) -> bool:
        """"""
    @overload
    def GetStandardValuesSupported(self) -> bool:
        """"""
    @overload
    def GetStandardValuesSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IsValid(self, context: ITypeDescriptorContext, value: object) -> bool:
        """"""
    @overload
    def IsValid(self, value: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    # noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
    class StandardValuesCollection(Object, ICollection, IEnumerable):
        """"""
        def __init__(self, values: ICollection) -> None:
            """"""
        @property
        def Count(self) -> int:
            """"""
        @property
        def IsSynchronized(self) -> bool:
            """"""
        @property
        def Item(self) -> object:
            """"""
        @property
        def SyncRoot(self) -> object:
            """"""
        def CopyTo(self, array: Array, index: int) -> None:
            """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def GetEnumerator(self) -> IEnumerator:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def ToString(self) -> str:
            """"""
        def __iter__(self) -> Iterator:
            """"""
        def __len__(self) -> int:
            """"""
        def __getitem__(self, index: int) -> object:
            """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class NestedContainer(Container, IContainer, INestedContainer, IDisposable):
    """"""
    def __init__(self, owner: IComponent) -> None:
        """"""
    @property
    def Components(self) -> ComponentCollection:
        """"""
    @property
    def Owner(self) -> IComponent:
        """"""
    @overload
    def Add(self, component: IComponent) -> None:
        """"""
    @overload
    def Add(self, component: IComponent, name: str) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Remove(self, component: IComponent) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def __delitem__(self, component: IComponent) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class NotifyParentPropertyAttribute(Attribute, _Attribute):
    """"""

    Default: ClassVar[NotifyParentPropertyAttribute]
    """"""
    No: ClassVar[NotifyParentPropertyAttribute]
    """"""
    Yes: ClassVar[NotifyParentPropertyAttribute]
    """"""
    def __init__(self, notifyParent: bool) -> None:
        """"""
    @property
    def NotifyParent(self) -> bool:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class NullableConverter(TypeConverter):
    """"""
    def __init__(self, type: Type) -> None:
        """"""
    @property
    def NullableType(self) -> Type:
        """"""
    @property
    def UnderlyingType(self) -> Type:
        """"""
    @property
    def UnderlyingTypeConverter(self) -> TypeConverter:
        """"""
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool:
        """"""
    @overload
    def CanConvertFrom(self, sourceType: Type) -> bool:
        """"""
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, destinationType: Type) -> bool:
        """"""
    @overload
    def CanConvertTo(self, destinationType: Type) -> bool:
        """"""
    @overload
    def ConvertFrom(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> object:
        """"""
    @overload
    def ConvertFrom(self, value: object) -> object:
        """"""
    @overload
    def ConvertFromInvariantString(self, context: ITypeDescriptorContext, text: str) -> object:
        """"""
    @overload
    def ConvertFromInvariantString(self, text: str) -> object:
        """"""
    @overload
    def ConvertFromString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, text: str
    ) -> object:
        """"""
    @overload
    def ConvertFromString(self, context: ITypeDescriptorContext, text: str) -> object:
        """"""
    @overload
    def ConvertFromString(self, text: str) -> object:
        """"""
    @overload
    def ConvertTo(
        self,
        context: ITypeDescriptorContext,
        culture: CultureInfo,
        value: object,
        destinationType: Type,
    ) -> object:
        """"""
    @overload
    def ConvertTo(self, value: object, destinationType: Type) -> object:
        """"""
    @overload
    def ConvertToInvariantString(self, context: ITypeDescriptorContext, value: object) -> str:
        """"""
    @overload
    def ConvertToInvariantString(self, value: object) -> str:
        """"""
    @overload
    def ConvertToString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> str:
        """"""
    @overload
    def ConvertToString(self, context: ITypeDescriptorContext, value: object) -> str:
        """"""
    @overload
    def ConvertToString(self, value: object) -> str:
        """"""
    @overload
    def CreateInstance(self, propertyValues: IDictionary) -> object:
        """"""
    @overload
    def CreateInstance(
        self, context: ITypeDescriptorContext, propertyValues: IDictionary
    ) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetCreateInstanceSupported(self) -> bool:
        """"""
    @overload
    def GetCreateInstanceSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object
    ) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]
    ) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetProperties(self, value: object) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetPropertiesSupported(self) -> bool:
        """"""
    @overload
    def GetPropertiesSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    @overload
    def GetStandardValues(self) -> ICollection:
        """"""
    @overload
    def GetStandardValues(
        self, context: ITypeDescriptorContext
    ) -> TypeConverter.StandardValuesCollection:
        """"""
    @overload
    def GetStandardValuesExclusive(self) -> bool:
        """"""
    @overload
    def GetStandardValuesExclusive(self, context: ITypeDescriptorContext) -> bool:
        """"""
    @overload
    def GetStandardValuesSupported(self) -> bool:
        """"""
    @overload
    def GetStandardValuesSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IsValid(self, context: ITypeDescriptorContext, value: object) -> bool:
        """"""
    @overload
    def IsValid(self, value: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    # noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
    class StandardValuesCollection(Object, ICollection, IEnumerable):
        """"""
        def __init__(self, values: ICollection) -> None:
            """"""
        @property
        def Count(self) -> int:
            """"""
        @property
        def IsSynchronized(self) -> bool:
            """"""
        @property
        def Item(self) -> object:
            """"""
        @property
        def SyncRoot(self) -> object:
            """"""
        def CopyTo(self, array: Array, index: int) -> None:
            """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def GetEnumerator(self) -> IEnumerator:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def ToString(self) -> str:
            """"""
        def __iter__(self) -> Iterator:
            """"""
        def __len__(self) -> int:
            """"""
        def __getitem__(self, index: int) -> object:
            """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ParenthesizePropertyNameAttribute(Attribute, _Attribute):
    """"""

    Default: ClassVar[ParenthesizePropertyNameAttribute]
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, needParenthesis: bool) -> None:
        """"""
    @property
    def NeedParenthesis(self) -> bool:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
    def Equals(self, o: object) -> bool:
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class PasswordPropertyTextAttribute(Attribute, _Attribute):
    """"""

    Default: ClassVar[PasswordPropertyTextAttribute]
    """"""
    No: ClassVar[PasswordPropertyTextAttribute]
    """"""
    Yes: ClassVar[PasswordPropertyTextAttribute]
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, password: bool) -> None:
        """"""
    @property
    def Password(self) -> bool:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
    def Equals(self, o: object) -> bool:
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ProgressChangedEventArgs(EventArgs):
    """"""
    def __init__(self, progressPercentage: int, userState: object) -> None:
        """"""
    @property
    def ProgressPercentage(self) -> int:
        """"""
    @property
    def UserState(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

type ProgressChangedEventHandler = Callable[[object, ProgressChangedEventArgs], None]
""""""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class PropertyChangedEventArgs(EventArgs):
    """"""
    def __init__(self, propertyName: str) -> None:
        """"""
    @property
    def PropertyName(self) -> str:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

type PropertyChangedEventHandler = Callable[[object, PropertyChangedEventArgs], None]
""""""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class PropertyChangingEventArgs(EventArgs):
    """"""
    def __init__(self, propertyName: str) -> None:
        """"""
    @property
    def PropertyName(self) -> str:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

type PropertyChangingEventHandler = Callable[[object, PropertyChangingEventArgs], None]
""""""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class PropertyDescriptor(ABC, MemberDescriptor):
    """"""
    @property
    def Attributes(self) -> AttributeCollection:
        """"""
    @property
    def Category(self) -> str:
        """"""
    @property
    def ComponentType(self) -> Type:
        """"""
    @property
    def Converter(self) -> TypeConverter:
        """"""
    @property
    def Description(self) -> str:
        """"""
    @property
    def DesignTimeOnly(self) -> bool:
        """"""
    @property
    def DisplayName(self) -> str:
        """"""
    @property
    def IsBrowsable(self) -> bool:
        """"""
    @property
    def IsLocalizable(self) -> bool:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def PropertyType(self) -> Type:
        """"""
    @property
    def SerializationVisibility(self) -> DesignerSerializationVisibility:
        """"""
    @property
    def SupportsChangeEvents(self) -> bool:
        """"""
    def AddValueChanged(self, component: object, handler: EventHandler) -> None:
        """"""
    def CanResetValue(self, component: object) -> bool:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetChildProperties(self) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetChildProperties(self, filter: Array[Attribute]) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetChildProperties(self, instance: object) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetChildProperties(
        self, instance: object, filter: Array[Attribute]
    ) -> PropertyDescriptorCollection:
        """"""
    def GetEditor(self, editorBaseType: Type) -> object:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetValue(self, component: object) -> object:
        """"""
    def RemoveValueChanged(self, component: object, handler: EventHandler) -> None:
        """"""
    def ResetValue(self, component: object) -> None:
        """"""
    def SetValue(self, component: object, value: object) -> None:
        """"""
    def ShouldSerializeValue(self, component: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class PropertyDescriptorCollection(Object, ICollection, IDictionary, IEnumerable, IList):
    """"""

    Empty: ClassVar[PropertyDescriptorCollection]
    """"""
    @overload
    def __init__(self, properties: Array[PropertyDescriptor]) -> None:
        """"""
    @overload
    def __init__(self, properties: Array[PropertyDescriptor], readOnly: bool) -> None:
        """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsFixedSize(self) -> bool:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def Item(self) -> PropertyDescriptor:
        """"""
    @property
    def Keys(self) -> ICollection:
        """"""
    @property
    def SyncRoot(self) -> object:
        """"""
    @property
    def Values(self) -> ICollection:
        """"""
    @overload
    def Add(self, value: PropertyDescriptor) -> int:
        """"""
    @overload
    def Add(self, value: object) -> int:
        """"""
    @overload
    def Add(self, key: object, value: object) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    @overload
    def Contains(self, value: PropertyDescriptor) -> bool:
        """"""
    @overload
    def Contains(self, value: object) -> bool:
        """"""
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Find(self, name: str, ignoreCase: bool) -> PropertyDescriptor:
        """"""
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IndexOf(self, value: PropertyDescriptor) -> int:
        """"""
    @overload
    def IndexOf(self, value: object) -> int:
        """"""
    @overload
    def Insert(self, index: int, value: PropertyDescriptor) -> None:
        """"""
    @overload
    def Insert(self, index: int, value: object) -> None:
        """"""
    @overload
    def Remove(self, value: PropertyDescriptor) -> None:
        """"""
    @overload
    def Remove(self, value: object) -> None:
        """"""
    def RemoveAt(self, index: int) -> None:
        """"""
    @overload
    def Sort(self) -> PropertyDescriptorCollection:
        """"""
    @overload
    def Sort(self, comparer: IComparer) -> PropertyDescriptorCollection:
        """"""
    @overload
    def Sort(self, names: Array[str]) -> PropertyDescriptorCollection:
        """"""
    @overload
    def Sort(self, names: Array[str], comparer: IComparer) -> PropertyDescriptorCollection:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __contains__(self, value: PropertyDescriptor) -> bool:
        """"""
    @overload
    def __contains__(self, value: object) -> bool:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    @overload
    def __delitem__(self, value: PropertyDescriptor) -> None:
        """"""
    @overload
    def __delitem__(self, value: object) -> None:
        """"""
    def __len__(self) -> int:
        """"""
    @overload
    def __getitem__(self, index: int) -> PropertyDescriptor:
        """"""
    @overload
    def __getitem__(self, key: object) -> object:
        """"""
    @overload
    def __getitem__(self, name: str) -> PropertyDescriptor:
        """"""
    @overload
    def __setitem__(self, index: int, value: object) -> None:
        """"""
    @overload
    def __setitem__(self, key: object, value: object) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class PropertyTabAttribute(Attribute, _Attribute):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, tabClass: Type) -> None:
        """"""
    @overload
    def __init__(self, tabClassName: str) -> None:
        """"""
    @overload
    def __init__(self, tabClass: Type, tabScope: PropertyTabScope) -> None:
        """"""
    @overload
    def __init__(self, tabClassName: str, tabScope: PropertyTabScope) -> None:
        """"""
    @property
    def TabClasses(self) -> Array[Type]:
        """"""
    @property
    def TabScopes(self) -> Array[PropertyTabScope]:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
    @overload
    def Equals(self, other: PropertyTabAttribute) -> bool:
        """"""
    @overload
    def Equals(self, other: object) -> bool:
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

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ProvidePropertyAttribute(Attribute, _Attribute):
    """"""
    @overload
    def __init__(self, propertyName: str, receiverType: Type) -> None:
        """"""
    @overload
    def __init__(self, propertyName: str, receiverTypeName: str) -> None:
        """"""
    @property
    def PropertyName(self) -> str:
        """"""
    @property
    def ReceiverTypeName(self) -> str:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ReadOnlyAttribute(Attribute, _Attribute):
    """"""

    Default: ClassVar[ReadOnlyAttribute]
    """"""
    No: ClassVar[ReadOnlyAttribute]
    """"""
    Yes: ClassVar[ReadOnlyAttribute]
    """"""
    def __init__(self, isReadOnly: bool) -> None:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
    def Equals(self, value: object) -> bool:
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class RecommendedAsConfigurableAttribute(Attribute, _Attribute):
    """"""

    Default: ClassVar[RecommendedAsConfigurableAttribute]
    """"""
    No: ClassVar[RecommendedAsConfigurableAttribute]
    """"""
    Yes: ClassVar[RecommendedAsConfigurableAttribute]
    """"""
    def __init__(self, recommendedAsConfigurable: bool) -> None:
        """"""
    @property
    def RecommendedAsConfigurable(self) -> bool:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ReferenceConverter(TypeConverter):
    """"""
    def __init__(self, type: Type) -> None:
        """"""
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool:
        """"""
    @overload
    def CanConvertFrom(self, sourceType: Type) -> bool:
        """"""
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, destinationType: Type) -> bool:
        """"""
    @overload
    def CanConvertTo(self, destinationType: Type) -> bool:
        """"""
    @overload
    def ConvertFrom(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> object:
        """"""
    @overload
    def ConvertFrom(self, value: object) -> object:
        """"""
    @overload
    def ConvertFromInvariantString(self, context: ITypeDescriptorContext, text: str) -> object:
        """"""
    @overload
    def ConvertFromInvariantString(self, text: str) -> object:
        """"""
    @overload
    def ConvertFromString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, text: str
    ) -> object:
        """"""
    @overload
    def ConvertFromString(self, context: ITypeDescriptorContext, text: str) -> object:
        """"""
    @overload
    def ConvertFromString(self, text: str) -> object:
        """"""
    @overload
    def ConvertTo(
        self,
        context: ITypeDescriptorContext,
        culture: CultureInfo,
        value: object,
        destinationType: Type,
    ) -> object:
        """"""
    @overload
    def ConvertTo(self, value: object, destinationType: Type) -> object:
        """"""
    @overload
    def ConvertToInvariantString(self, context: ITypeDescriptorContext, value: object) -> str:
        """"""
    @overload
    def ConvertToInvariantString(self, value: object) -> str:
        """"""
    @overload
    def ConvertToString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> str:
        """"""
    @overload
    def ConvertToString(self, context: ITypeDescriptorContext, value: object) -> str:
        """"""
    @overload
    def ConvertToString(self, value: object) -> str:
        """"""
    @overload
    def CreateInstance(self, propertyValues: IDictionary) -> object:
        """"""
    @overload
    def CreateInstance(
        self, context: ITypeDescriptorContext, propertyValues: IDictionary
    ) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetCreateInstanceSupported(self) -> bool:
        """"""
    @overload
    def GetCreateInstanceSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object
    ) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]
    ) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetProperties(self, value: object) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetPropertiesSupported(self) -> bool:
        """"""
    @overload
    def GetPropertiesSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    @overload
    def GetStandardValues(self) -> ICollection:
        """"""
    @overload
    def GetStandardValues(
        self, context: ITypeDescriptorContext
    ) -> TypeConverter.StandardValuesCollection:
        """"""
    @overload
    def GetStandardValuesExclusive(self) -> bool:
        """"""
    @overload
    def GetStandardValuesExclusive(self, context: ITypeDescriptorContext) -> bool:
        """"""
    @overload
    def GetStandardValuesSupported(self) -> bool:
        """"""
    @overload
    def GetStandardValuesSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IsValid(self, context: ITypeDescriptorContext, value: object) -> bool:
        """"""
    @overload
    def IsValid(self, value: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    # noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
    class StandardValuesCollection(Object, ICollection, IEnumerable):
        """"""
        def __init__(self, values: ICollection) -> None:
            """"""
        @property
        def Count(self) -> int:
            """"""
        @property
        def IsSynchronized(self) -> bool:
            """"""
        @property
        def Item(self) -> object:
            """"""
        @property
        def SyncRoot(self) -> object:
            """"""
        def CopyTo(self, array: Array, index: int) -> None:
            """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def GetEnumerator(self) -> IEnumerator:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def ToString(self) -> str:
            """"""
        def __iter__(self) -> Iterator:
            """"""
        def __len__(self) -> int:
            """"""
        def __getitem__(self, index: int) -> object:
            """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ReflectEventDescriptor(EventDescriptor):
    """"""
    @overload
    def __init__(
        self, componentClass: Type, name: str, type: Type, attributes: Array[Attribute]
    ) -> None:
        """"""
    @overload
    def __init__(self, componentClass: Type, eventInfo: EventInfo) -> None:
        """"""
    @overload
    def __init__(
        self,
        componentType: Type,
        oldReflectEventDescriptor: EventDescriptor,
        attributes: Array[Attribute],
    ) -> None:
        """"""
    @property
    def Attributes(self) -> AttributeCollection:
        """"""
    @property
    def Category(self) -> str:
        """"""
    @property
    def ComponentType(self) -> Type:
        """"""
    @property
    def Description(self) -> str:
        """"""
    @property
    def DesignTimeOnly(self) -> bool:
        """"""
    @property
    def DisplayName(self) -> str:
        """"""
    @property
    def EventType(self) -> Type:
        """"""
    @property
    def IsBrowsable(self) -> bool:
        """"""
    @property
    def IsMulticast(self) -> bool:
        """"""
    @property
    def Name(self) -> str:
        """"""
    def AddEventHandler(self, component: object, value: Delegate) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def RemoveEventHandler(self, component: object, value: Delegate) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ReflectPropertyDescriptor(PropertyDescriptor):
    """"""
    @overload
    def __init__(
        self, componentClass: Type, name: str, type: Type, attributes: Array[Attribute]
    ) -> None:
        """"""
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
    ) -> None:
        """"""
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
    ) -> None:
        """"""
    @overload
    def __init__(
        self,
        componentClass: Type,
        oldReflectPropertyDescriptor: PropertyDescriptor,
        attributes: Array[Attribute],
    ) -> None:
        """"""
    @property
    def Attributes(self) -> AttributeCollection:
        """"""
    @property
    def Category(self) -> str:
        """"""
    @property
    def ComponentType(self) -> Type:
        """"""
    @property
    def Converter(self) -> TypeConverter:
        """"""
    @property
    def Description(self) -> str:
        """"""
    @property
    def DesignTimeOnly(self) -> bool:
        """"""
    @property
    def DisplayName(self) -> str:
        """"""
    @property
    def IsBrowsable(self) -> bool:
        """"""
    @property
    def IsLocalizable(self) -> bool:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def PropertyType(self) -> Type:
        """"""
    @property
    def SerializationVisibility(self) -> DesignerSerializationVisibility:
        """"""
    @property
    def SupportsChangeEvents(self) -> bool:
        """"""
    def AddValueChanged(self, component: object, handler: EventHandler) -> None:
        """"""
    def CanResetValue(self, component: object) -> bool:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetChildProperties(self) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetChildProperties(self, filter: Array[Attribute]) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetChildProperties(self, instance: object) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetChildProperties(
        self, instance: object, filter: Array[Attribute]
    ) -> PropertyDescriptorCollection:
        """"""
    def GetEditor(self, editorBaseType: Type) -> object:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetValue(self, component: object) -> object:
        """"""
    def RemoveValueChanged(self, component: object, handler: EventHandler) -> None:
        """"""
    def ResetValue(self, component: object) -> None:
        """"""
    def SetValue(self, component: object, value: object) -> None:
        """"""
    def ShouldSerializeValue(self, component: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ReflectTypeDescriptionProvider(TypeDescriptionProvider):
    """"""
    def CreateInstance(
        self,
        provider: IServiceProvider,
        objectType: Type,
        argTypes: Array[Type],
        args: Array[object],
    ) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetCache(self, instance: object) -> IDictionary:
        """"""
    def GetExtendedTypeDescriptor(self, instance: object) -> ICustomTypeDescriptor:
        """"""
    def GetFullComponentName(self, component: object) -> str:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetReflectionType(self, instance: object) -> Type:
        """"""
    @overload
    def GetReflectionType(self, objectType: Type) -> Type:
        """"""
    @overload
    def GetReflectionType(self, objectType: Type, instance: object) -> Type:
        """"""
    def GetRuntimeType(self, reflectionType: Type) -> Type:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def GetTypeDescriptor(self, instance: object) -> ICustomTypeDescriptor:
        """"""
    @overload
    def GetTypeDescriptor(self, objectType: Type) -> ICustomTypeDescriptor:
        """"""
    @overload
    def GetTypeDescriptor(self, objectType: Type, instance: object) -> ICustomTypeDescriptor:
        """"""
    def IsSupportedType(self, type: Type) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class RefreshEventArgs(EventArgs):
    """"""
    @overload
    def __init__(self, componentChanged: object) -> None:
        """"""
    @overload
    def __init__(self, typeChanged: Type) -> None:
        """"""
    @property
    def ComponentChanged(self) -> object:
        """"""
    @property
    def TypeChanged(self) -> Type:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

type RefreshEventHandler = Callable[[RefreshEventArgs], None]
""""""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class RefreshProperties(Enum):
    """"""

    _None: RefreshProperties = ...
    """"""
    All: RefreshProperties = ...
    """"""
    Repaint: RefreshProperties = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class RefreshPropertiesAttribute(Attribute, _Attribute):
    """"""

    All: ClassVar[RefreshPropertiesAttribute]
    """"""
    Default: ClassVar[RefreshPropertiesAttribute]
    """"""
    Repaint: ClassVar[RefreshPropertiesAttribute]
    """"""
    def __init__(self, refresh: RefreshProperties) -> None:
        """"""
    @property
    def RefreshProperties(self) -> RefreshProperties:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
    def Equals(self, value: object) -> bool:
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class RunInstallerAttribute(Attribute, _Attribute):
    """"""

    Default: ClassVar[RunInstallerAttribute]
    """"""
    No: ClassVar[RunInstallerAttribute]
    """"""
    Yes: ClassVar[RunInstallerAttribute]
    """"""
    def __init__(self, runInstaller: bool) -> None:
        """"""
    @property
    def RunInstaller(self) -> bool:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class RunWorkerCompletedEventArgs(AsyncCompletedEventArgs):
    """"""
    def __init__(self, result: object, error: Exception, cancelled: bool) -> None:
        """"""
    @property
    def Cancelled(self) -> bool:
        """"""
    @property
    def Error(self) -> Exception:
        """"""
    @property
    def Result(self) -> object:
        """"""
    @property
    def UserState(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

type RunWorkerCompletedEventHandler = Callable[[object, RunWorkerCompletedEventArgs], None]
""""""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SByteConverter(BaseNumberConverter):
    """"""
    def __init__(self) -> None:
        """"""
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool:
        """"""
    @overload
    def CanConvertFrom(self, sourceType: Type) -> bool:
        """"""
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, t: Type) -> bool:
        """"""
    @overload
    def CanConvertTo(self, destinationType: Type) -> bool:
        """"""
    @overload
    def ConvertFrom(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> object:
        """"""
    @overload
    def ConvertFrom(self, value: object) -> object:
        """"""
    @overload
    def ConvertFromInvariantString(self, context: ITypeDescriptorContext, text: str) -> object:
        """"""
    @overload
    def ConvertFromInvariantString(self, text: str) -> object:
        """"""
    @overload
    def ConvertFromString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, text: str
    ) -> object:
        """"""
    @overload
    def ConvertFromString(self, context: ITypeDescriptorContext, text: str) -> object:
        """"""
    @overload
    def ConvertFromString(self, text: str) -> object:
        """"""
    @overload
    def ConvertTo(
        self,
        context: ITypeDescriptorContext,
        culture: CultureInfo,
        value: object,
        destinationType: Type,
    ) -> object:
        """"""
    @overload
    def ConvertTo(self, value: object, destinationType: Type) -> object:
        """"""
    @overload
    def ConvertToInvariantString(self, context: ITypeDescriptorContext, value: object) -> str:
        """"""
    @overload
    def ConvertToInvariantString(self, value: object) -> str:
        """"""
    @overload
    def ConvertToString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> str:
        """"""
    @overload
    def ConvertToString(self, context: ITypeDescriptorContext, value: object) -> str:
        """"""
    @overload
    def ConvertToString(self, value: object) -> str:
        """"""
    @overload
    def CreateInstance(self, propertyValues: IDictionary) -> object:
        """"""
    @overload
    def CreateInstance(
        self, context: ITypeDescriptorContext, propertyValues: IDictionary
    ) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetCreateInstanceSupported(self) -> bool:
        """"""
    @overload
    def GetCreateInstanceSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object
    ) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]
    ) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetProperties(self, value: object) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetPropertiesSupported(self) -> bool:
        """"""
    @overload
    def GetPropertiesSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    @overload
    def GetStandardValues(self) -> ICollection:
        """"""
    @overload
    def GetStandardValues(
        self, context: ITypeDescriptorContext
    ) -> TypeConverter.StandardValuesCollection:
        """"""
    @overload
    def GetStandardValuesExclusive(self) -> bool:
        """"""
    @overload
    def GetStandardValuesExclusive(self, context: ITypeDescriptorContext) -> bool:
        """"""
    @overload
    def GetStandardValuesSupported(self) -> bool:
        """"""
    @overload
    def GetStandardValuesSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IsValid(self, context: ITypeDescriptorContext, value: object) -> bool:
        """"""
    @overload
    def IsValid(self, value: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    # noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
    class StandardValuesCollection(Object, ICollection, IEnumerable):
        """"""
        def __init__(self, values: ICollection) -> None:
            """"""
        @property
        def Count(self) -> int:
            """"""
        @property
        def IsSynchronized(self) -> bool:
            """"""
        @property
        def Item(self) -> object:
            """"""
        @property
        def SyncRoot(self) -> object:
            """"""
        def CopyTo(self, array: Array, index: int) -> None:
            """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def GetEnumerator(self) -> IEnumerator:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def ToString(self) -> str:
            """"""
        def __iter__(self) -> Iterator:
            """"""
        def __len__(self) -> int:
            """"""
        def __getitem__(self, index: int) -> object:
            """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SettingsBindableAttribute(Attribute, _Attribute):
    """"""

    No: ClassVar[SettingsBindableAttribute]
    """"""
    Yes: ClassVar[SettingsBindableAttribute]
    """"""
    def __init__(self, bindable: bool) -> None:
        """"""
    @property
    def Bindable(self) -> bool:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SingleConverter(BaseNumberConverter):
    """"""
    def __init__(self) -> None:
        """"""
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool:
        """"""
    @overload
    def CanConvertFrom(self, sourceType: Type) -> bool:
        """"""
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, t: Type) -> bool:
        """"""
    @overload
    def CanConvertTo(self, destinationType: Type) -> bool:
        """"""
    @overload
    def ConvertFrom(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> object:
        """"""
    @overload
    def ConvertFrom(self, value: object) -> object:
        """"""
    @overload
    def ConvertFromInvariantString(self, context: ITypeDescriptorContext, text: str) -> object:
        """"""
    @overload
    def ConvertFromInvariantString(self, text: str) -> object:
        """"""
    @overload
    def ConvertFromString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, text: str
    ) -> object:
        """"""
    @overload
    def ConvertFromString(self, context: ITypeDescriptorContext, text: str) -> object:
        """"""
    @overload
    def ConvertFromString(self, text: str) -> object:
        """"""
    @overload
    def ConvertTo(
        self,
        context: ITypeDescriptorContext,
        culture: CultureInfo,
        value: object,
        destinationType: Type,
    ) -> object:
        """"""
    @overload
    def ConvertTo(self, value: object, destinationType: Type) -> object:
        """"""
    @overload
    def ConvertToInvariantString(self, context: ITypeDescriptorContext, value: object) -> str:
        """"""
    @overload
    def ConvertToInvariantString(self, value: object) -> str:
        """"""
    @overload
    def ConvertToString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> str:
        """"""
    @overload
    def ConvertToString(self, context: ITypeDescriptorContext, value: object) -> str:
        """"""
    @overload
    def ConvertToString(self, value: object) -> str:
        """"""
    @overload
    def CreateInstance(self, propertyValues: IDictionary) -> object:
        """"""
    @overload
    def CreateInstance(
        self, context: ITypeDescriptorContext, propertyValues: IDictionary
    ) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetCreateInstanceSupported(self) -> bool:
        """"""
    @overload
    def GetCreateInstanceSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object
    ) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]
    ) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetProperties(self, value: object) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetPropertiesSupported(self) -> bool:
        """"""
    @overload
    def GetPropertiesSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    @overload
    def GetStandardValues(self) -> ICollection:
        """"""
    @overload
    def GetStandardValues(
        self, context: ITypeDescriptorContext
    ) -> TypeConverter.StandardValuesCollection:
        """"""
    @overload
    def GetStandardValuesExclusive(self) -> bool:
        """"""
    @overload
    def GetStandardValuesExclusive(self, context: ITypeDescriptorContext) -> bool:
        """"""
    @overload
    def GetStandardValuesSupported(self) -> bool:
        """"""
    @overload
    def GetStandardValuesSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IsValid(self, context: ITypeDescriptorContext, value: object) -> bool:
        """"""
    @overload
    def IsValid(self, value: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    # noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
    class StandardValuesCollection(Object, ICollection, IEnumerable):
        """"""
        def __init__(self, values: ICollection) -> None:
            """"""
        @property
        def Count(self) -> int:
            """"""
        @property
        def IsSynchronized(self) -> bool:
            """"""
        @property
        def Item(self) -> object:
            """"""
        @property
        def SyncRoot(self) -> object:
            """"""
        def CopyTo(self, array: Array, index: int) -> None:
            """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def GetEnumerator(self) -> IEnumerator:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def ToString(self) -> str:
            """"""
        def __iter__(self) -> Iterator:
            """"""
        def __len__(self) -> int:
            """"""
        def __getitem__(self, index: int) -> object:
            """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class StringConverter(TypeConverter):
    """"""
    def __init__(self) -> None:
        """"""
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool:
        """"""
    @overload
    def CanConvertFrom(self, sourceType: Type) -> bool:
        """"""
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, destinationType: Type) -> bool:
        """"""
    @overload
    def CanConvertTo(self, destinationType: Type) -> bool:
        """"""
    @overload
    def ConvertFrom(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> object:
        """"""
    @overload
    def ConvertFrom(self, value: object) -> object:
        """"""
    @overload
    def ConvertFromInvariantString(self, context: ITypeDescriptorContext, text: str) -> object:
        """"""
    @overload
    def ConvertFromInvariantString(self, text: str) -> object:
        """"""
    @overload
    def ConvertFromString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, text: str
    ) -> object:
        """"""
    @overload
    def ConvertFromString(self, context: ITypeDescriptorContext, text: str) -> object:
        """"""
    @overload
    def ConvertFromString(self, text: str) -> object:
        """"""
    @overload
    def ConvertTo(
        self,
        context: ITypeDescriptorContext,
        culture: CultureInfo,
        value: object,
        destinationType: Type,
    ) -> object:
        """"""
    @overload
    def ConvertTo(self, value: object, destinationType: Type) -> object:
        """"""
    @overload
    def ConvertToInvariantString(self, context: ITypeDescriptorContext, value: object) -> str:
        """"""
    @overload
    def ConvertToInvariantString(self, value: object) -> str:
        """"""
    @overload
    def ConvertToString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> str:
        """"""
    @overload
    def ConvertToString(self, context: ITypeDescriptorContext, value: object) -> str:
        """"""
    @overload
    def ConvertToString(self, value: object) -> str:
        """"""
    @overload
    def CreateInstance(self, propertyValues: IDictionary) -> object:
        """"""
    @overload
    def CreateInstance(
        self, context: ITypeDescriptorContext, propertyValues: IDictionary
    ) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetCreateInstanceSupported(self) -> bool:
        """"""
    @overload
    def GetCreateInstanceSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object
    ) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]
    ) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetProperties(self, value: object) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetPropertiesSupported(self) -> bool:
        """"""
    @overload
    def GetPropertiesSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    @overload
    def GetStandardValues(self) -> ICollection:
        """"""
    @overload
    def GetStandardValues(
        self, context: ITypeDescriptorContext
    ) -> TypeConverter.StandardValuesCollection:
        """"""
    @overload
    def GetStandardValuesExclusive(self) -> bool:
        """"""
    @overload
    def GetStandardValuesExclusive(self, context: ITypeDescriptorContext) -> bool:
        """"""
    @overload
    def GetStandardValuesSupported(self) -> bool:
        """"""
    @overload
    def GetStandardValuesSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IsValid(self, context: ITypeDescriptorContext, value: object) -> bool:
        """"""
    @overload
    def IsValid(self, value: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    # noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
    class StandardValuesCollection(Object, ICollection, IEnumerable):
        """"""
        def __init__(self, values: ICollection) -> None:
            """"""
        @property
        def Count(self) -> int:
            """"""
        @property
        def IsSynchronized(self) -> bool:
            """"""
        @property
        def Item(self) -> object:
            """"""
        @property
        def SyncRoot(self) -> object:
            """"""
        def CopyTo(self, array: Array, index: int) -> None:
            """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def GetEnumerator(self) -> IEnumerator:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def ToString(self) -> str:
            """"""
        def __iter__(self) -> Iterator:
            """"""
        def __len__(self) -> int:
            """"""
        def __getitem__(self, index: int) -> object:
            """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SyntaxCheck(ABC, Object):
    """"""
    @classmethod
    def CheckMachineName(cls, value: str) -> bool:
        """"""
    @classmethod
    def CheckPath(cls, value: str) -> bool:
        """"""
    @classmethod
    def CheckRootedPath(cls, value: str) -> bool:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class TimeSpanConverter(TypeConverter):
    """"""
    def __init__(self) -> None:
        """"""
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool:
        """"""
    @overload
    def CanConvertFrom(self, sourceType: Type) -> bool:
        """"""
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, destinationType: Type) -> bool:
        """"""
    @overload
    def CanConvertTo(self, destinationType: Type) -> bool:
        """"""
    @overload
    def ConvertFrom(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> object:
        """"""
    @overload
    def ConvertFrom(self, value: object) -> object:
        """"""
    @overload
    def ConvertFromInvariantString(self, context: ITypeDescriptorContext, text: str) -> object:
        """"""
    @overload
    def ConvertFromInvariantString(self, text: str) -> object:
        """"""
    @overload
    def ConvertFromString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, text: str
    ) -> object:
        """"""
    @overload
    def ConvertFromString(self, context: ITypeDescriptorContext, text: str) -> object:
        """"""
    @overload
    def ConvertFromString(self, text: str) -> object:
        """"""
    @overload
    def ConvertTo(
        self,
        context: ITypeDescriptorContext,
        culture: CultureInfo,
        value: object,
        destinationType: Type,
    ) -> object:
        """"""
    @overload
    def ConvertTo(self, value: object, destinationType: Type) -> object:
        """"""
    @overload
    def ConvertToInvariantString(self, context: ITypeDescriptorContext, value: object) -> str:
        """"""
    @overload
    def ConvertToInvariantString(self, value: object) -> str:
        """"""
    @overload
    def ConvertToString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> str:
        """"""
    @overload
    def ConvertToString(self, context: ITypeDescriptorContext, value: object) -> str:
        """"""
    @overload
    def ConvertToString(self, value: object) -> str:
        """"""
    @overload
    def CreateInstance(self, propertyValues: IDictionary) -> object:
        """"""
    @overload
    def CreateInstance(
        self, context: ITypeDescriptorContext, propertyValues: IDictionary
    ) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetCreateInstanceSupported(self) -> bool:
        """"""
    @overload
    def GetCreateInstanceSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object
    ) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]
    ) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetProperties(self, value: object) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetPropertiesSupported(self) -> bool:
        """"""
    @overload
    def GetPropertiesSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    @overload
    def GetStandardValues(self) -> ICollection:
        """"""
    @overload
    def GetStandardValues(
        self, context: ITypeDescriptorContext
    ) -> TypeConverter.StandardValuesCollection:
        """"""
    @overload
    def GetStandardValuesExclusive(self) -> bool:
        """"""
    @overload
    def GetStandardValuesExclusive(self, context: ITypeDescriptorContext) -> bool:
        """"""
    @overload
    def GetStandardValuesSupported(self) -> bool:
        """"""
    @overload
    def GetStandardValuesSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IsValid(self, context: ITypeDescriptorContext, value: object) -> bool:
        """"""
    @overload
    def IsValid(self, value: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    # noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
    class StandardValuesCollection(Object, ICollection, IEnumerable):
        """"""
        def __init__(self, values: ICollection) -> None:
            """"""
        @property
        def Count(self) -> int:
            """"""
        @property
        def IsSynchronized(self) -> bool:
            """"""
        @property
        def Item(self) -> object:
            """"""
        @property
        def SyncRoot(self) -> object:
            """"""
        def CopyTo(self, array: Array, index: int) -> None:
            """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def GetEnumerator(self) -> IEnumerator:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def ToString(self) -> str:
            """"""
        def __iter__(self) -> Iterator:
            """"""
        def __len__(self) -> int:
            """"""
        def __getitem__(self, index: int) -> object:
            """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ToolboxItemAttribute(Attribute, _Attribute):
    """"""

    Default: ClassVar[ToolboxItemAttribute]
    """"""
    _None: ClassVar[ToolboxItemAttribute]
    """"""
    @overload
    def __init__(self, defaultType: bool) -> None:
        """"""
    @overload
    def __init__(self, toolboxItemTypeName: str) -> None:
        """"""
    @overload
    def __init__(self, toolboxItemType: Type) -> None:
        """"""
    @property
    def ToolboxItemType(self) -> Type:
        """"""
    @property
    def ToolboxItemTypeName(self) -> str:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ToolboxItemFilterAttribute(Attribute, _Attribute):
    """"""
    @overload
    def __init__(self, filterString: str) -> None:
        """"""
    @overload
    def __init__(self, filterString: str, filterType: ToolboxItemFilterType) -> None:
        """"""
    @property
    def FilterString(self) -> str:
        """"""
    @property
    def FilterType(self) -> ToolboxItemFilterType:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
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

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class TypeConverter(Object):
    """"""
    def __init__(self) -> None:
        """"""
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool:
        """"""
    @overload
    def CanConvertFrom(self, sourceType: Type) -> bool:
        """"""
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, destinationType: Type) -> bool:
        """"""
    @overload
    def CanConvertTo(self, destinationType: Type) -> bool:
        """"""
    @overload
    def ConvertFrom(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> object:
        """"""
    @overload
    def ConvertFrom(self, value: object) -> object:
        """"""
    @overload
    def ConvertFromInvariantString(self, context: ITypeDescriptorContext, text: str) -> object:
        """"""
    @overload
    def ConvertFromInvariantString(self, text: str) -> object:
        """"""
    @overload
    def ConvertFromString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, text: str
    ) -> object:
        """"""
    @overload
    def ConvertFromString(self, context: ITypeDescriptorContext, text: str) -> object:
        """"""
    @overload
    def ConvertFromString(self, text: str) -> object:
        """"""
    @overload
    def ConvertTo(
        self,
        context: ITypeDescriptorContext,
        culture: CultureInfo,
        value: object,
        destinationType: Type,
    ) -> object:
        """"""
    @overload
    def ConvertTo(self, value: object, destinationType: Type) -> object:
        """"""
    @overload
    def ConvertToInvariantString(self, context: ITypeDescriptorContext, value: object) -> str:
        """"""
    @overload
    def ConvertToInvariantString(self, value: object) -> str:
        """"""
    @overload
    def ConvertToString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> str:
        """"""
    @overload
    def ConvertToString(self, context: ITypeDescriptorContext, value: object) -> str:
        """"""
    @overload
    def ConvertToString(self, value: object) -> str:
        """"""
    @overload
    def CreateInstance(self, propertyValues: IDictionary) -> object:
        """"""
    @overload
    def CreateInstance(
        self, context: ITypeDescriptorContext, propertyValues: IDictionary
    ) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetCreateInstanceSupported(self) -> bool:
        """"""
    @overload
    def GetCreateInstanceSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object
    ) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]
    ) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetProperties(self, value: object) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetPropertiesSupported(self) -> bool:
        """"""
    @overload
    def GetPropertiesSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    @overload
    def GetStandardValues(self) -> ICollection:
        """"""
    @overload
    def GetStandardValues(
        self, context: ITypeDescriptorContext
    ) -> TypeConverter.StandardValuesCollection:
        """"""
    @overload
    def GetStandardValuesExclusive(self) -> bool:
        """"""
    @overload
    def GetStandardValuesExclusive(self, context: ITypeDescriptorContext) -> bool:
        """"""
    @overload
    def GetStandardValuesSupported(self) -> bool:
        """"""
    @overload
    def GetStandardValuesSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IsValid(self, context: ITypeDescriptorContext, value: object) -> bool:
        """"""
    @overload
    def IsValid(self, value: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    # noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
    class StandardValuesCollection(Object, ICollection, IEnumerable):
        """"""
        def __init__(self, values: ICollection) -> None:
            """"""
        @property
        def Count(self) -> int:
            """"""
        @property
        def IsSynchronized(self) -> bool:
            """"""
        @property
        def Item(self) -> object:
            """"""
        @property
        def SyncRoot(self) -> object:
            """"""
        def CopyTo(self, array: Array, index: int) -> None:
            """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def GetEnumerator(self) -> IEnumerator:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def ToString(self) -> str:
            """"""
        def __iter__(self) -> Iterator:
            """"""
        def __len__(self) -> int:
            """"""
        def __getitem__(self, index: int) -> object:
            """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class TypeConverterAttribute(Attribute, _Attribute):
    """"""

    Default: ClassVar[TypeConverterAttribute]
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, type: Type) -> None:
        """"""
    @overload
    def __init__(self, typeName: str) -> None:
        """"""
    @property
    def ConverterTypeName(self) -> str:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class TypeDescriptionProvider(ABC, Object):
    """"""
    def CreateInstance(
        self,
        provider: IServiceProvider,
        objectType: Type,
        argTypes: Array[Type],
        args: Array[object],
    ) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetCache(self, instance: object) -> IDictionary:
        """"""
    def GetExtendedTypeDescriptor(self, instance: object) -> ICustomTypeDescriptor:
        """"""
    def GetFullComponentName(self, component: object) -> str:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetReflectionType(self, instance: object) -> Type:
        """"""
    @overload
    def GetReflectionType(self, objectType: Type) -> Type:
        """"""
    @overload
    def GetReflectionType(self, objectType: Type, instance: object) -> Type:
        """"""
    def GetRuntimeType(self, reflectionType: Type) -> Type:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def GetTypeDescriptor(self, instance: object) -> ICustomTypeDescriptor:
        """"""
    @overload
    def GetTypeDescriptor(self, objectType: Type) -> ICustomTypeDescriptor:
        """"""
    @overload
    def GetTypeDescriptor(self, objectType: Type, instance: object) -> ICustomTypeDescriptor:
        """"""
    def IsSupportedType(self, type: Type) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class TypeDescriptionProviderAttribute(Attribute, _Attribute):
    """"""
    @overload
    def __init__(self, typeName: str) -> None:
        """"""
    @overload
    def __init__(self, type: Type) -> None:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
    @property
    def TypeName(self) -> str:
        """"""
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class TypeDescriptor(Object):
    """"""
    @classmethod
    @property
    def ComNativeDescriptorHandler(cls) -> IComNativeDescriptorHandler:
        """"""
    @classmethod
    @ComNativeDescriptorHandler.setter
    def ComNativeDescriptorHandler(cls, value: IComNativeDescriptorHandler) -> None: ...
    @classmethod
    @property
    def ComObjectType(cls) -> Type:
        """"""
    @classmethod
    @property
    def InterfaceType(cls) -> Type:
        """"""
    @classmethod
    @overload
    def AddAttributes(
        cls, instance: object, attributes: Array[Attribute]
    ) -> TypeDescriptionProvider:
        """"""
    @classmethod
    @overload
    def AddAttributes(cls, type: Type, attributes: Array[Attribute]) -> TypeDescriptionProvider:
        """"""
    @classmethod
    def AddEditorTable(cls, editorBaseType: Type, table: Hashtable) -> None:
        """"""
    @classmethod
    @overload
    def AddProvider(cls, provider: TypeDescriptionProvider, instance: object) -> None:
        """"""
    @classmethod
    @overload
    def AddProvider(cls, provider: TypeDescriptionProvider, type: Type) -> None:
        """"""
    @classmethod
    @overload
    def AddProviderTransparent(cls, provider: TypeDescriptionProvider, instance: object) -> None:
        """"""
    @classmethod
    @overload
    def AddProviderTransparent(cls, provider: TypeDescriptionProvider, type: Type) -> None:
        """"""
    @classmethod
    def CreateAssociation(cls, primary: object, secondary: object) -> None:
        """"""
    @classmethod
    def CreateDesigner(cls, component: IComponent, designerBaseType: Type) -> IDesigner:
        """"""
    @classmethod
    @overload
    def CreateEvent(
        cls, componentType: Type, oldEventDescriptor: EventDescriptor, attributes: Array[Attribute]
    ) -> EventDescriptor:
        """"""
    @classmethod
    @overload
    def CreateEvent(
        cls, componentType: Type, name: str, type: Type, attributes: Array[Attribute]
    ) -> EventDescriptor:
        """"""
    @classmethod
    def CreateInstance(
        cls,
        provider: IServiceProvider,
        objectType: Type,
        argTypes: Array[Type],
        args: Array[object],
    ) -> object:
        """"""
    @classmethod
    @overload
    def CreateProperty(
        cls,
        componentType: Type,
        oldPropertyDescriptor: PropertyDescriptor,
        attributes: Array[Attribute],
    ) -> PropertyDescriptor:
        """"""
    @classmethod
    @overload
    def CreateProperty(
        cls, componentType: Type, name: str, type: Type, attributes: Array[Attribute]
    ) -> PropertyDescriptor:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def GetAssociation(cls, type: Type, primary: object) -> object:
        """"""
    @classmethod
    @overload
    def GetAttributes(cls, component: object) -> AttributeCollection:
        """"""
    @classmethod
    @overload
    def GetAttributes(cls, component: object, noCustomTypeDesc: bool) -> AttributeCollection:
        """"""
    @classmethod
    @overload
    def GetAttributes(cls, componentType: Type) -> AttributeCollection:
        """"""
    @classmethod
    @overload
    def GetClassName(cls, component: object) -> str:
        """"""
    @classmethod
    @overload
    def GetClassName(cls, component: object, noCustomTypeDesc: bool) -> str:
        """"""
    @classmethod
    @overload
    def GetClassName(cls, componentType: Type) -> str:
        """"""
    @classmethod
    @overload
    def GetComponentName(cls, component: object) -> str:
        """"""
    @classmethod
    @overload
    def GetComponentName(cls, component: object, noCustomTypeDesc: bool) -> str:
        """"""
    @classmethod
    @overload
    def GetConverter(cls, component: object) -> TypeConverter:
        """"""
    @classmethod
    @overload
    def GetConverter(cls, component: object, noCustomTypeDesc: bool) -> TypeConverter:
        """"""
    @classmethod
    @overload
    def GetConverter(cls, type: Type) -> TypeConverter:
        """"""
    @classmethod
    @overload
    def GetDefaultEvent(cls, component: object) -> EventDescriptor:
        """"""
    @classmethod
    @overload
    def GetDefaultEvent(cls, component: object, noCustomTypeDesc: bool) -> EventDescriptor:
        """"""
    @classmethod
    @overload
    def GetDefaultEvent(cls, componentType: Type) -> EventDescriptor:
        """"""
    @classmethod
    @overload
    def GetDefaultProperty(cls, component: object) -> PropertyDescriptor:
        """"""
    @classmethod
    @overload
    def GetDefaultProperty(cls, component: object, noCustomTypeDesc: bool) -> PropertyDescriptor:
        """"""
    @classmethod
    @overload
    def GetDefaultProperty(cls, componentType: Type) -> PropertyDescriptor:
        """"""
    @classmethod
    @overload
    def GetEditor(cls, component: object, editorBaseType: Type) -> object:
        """"""
    @classmethod
    @overload
    def GetEditor(cls, component: object, editorBaseType: Type, noCustomTypeDesc: bool) -> object:
        """"""
    @classmethod
    @overload
    def GetEditor(cls, type: Type, editorBaseType: Type) -> object:
        """"""
    @classmethod
    @overload
    def GetEvents(cls, component: object) -> EventDescriptorCollection:
        """"""
    @classmethod
    @overload
    def GetEvents(
        cls, component: object, attributes: Array[Attribute]
    ) -> EventDescriptorCollection:
        """"""
    @classmethod
    @overload
    def GetEvents(
        cls, component: object, attributes: Array[Attribute], noCustomTypeDesc: bool
    ) -> EventDescriptorCollection:
        """"""
    @classmethod
    @overload
    def GetEvents(cls, component: object, noCustomTypeDesc: bool) -> EventDescriptorCollection:
        """"""
    @classmethod
    @overload
    def GetEvents(cls, componentType: Type) -> EventDescriptorCollection:
        """"""
    @classmethod
    @overload
    def GetEvents(
        cls, componentType: Type, attributes: Array[Attribute]
    ) -> EventDescriptorCollection:
        """"""
    @classmethod
    def GetFullComponentName(cls, component: object) -> str:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @classmethod
    @overload
    def GetProperties(cls, component: object) -> PropertyDescriptorCollection:
        """"""
    @classmethod
    @overload
    def GetProperties(
        cls, component: object, attributes: Array[Attribute]
    ) -> PropertyDescriptorCollection:
        """"""
    @classmethod
    @overload
    def GetProperties(
        cls, component: object, attributes: Array[Attribute], noCustomTypeDesc: bool
    ) -> PropertyDescriptorCollection:
        """"""
    @classmethod
    @overload
    def GetProperties(
        cls, component: object, noCustomTypeDesc: bool
    ) -> PropertyDescriptorCollection:
        """"""
    @classmethod
    @overload
    def GetProperties(cls, componentType: Type) -> PropertyDescriptorCollection:
        """"""
    @classmethod
    @overload
    def GetProperties(
        cls, componentType: Type, attributes: Array[Attribute]
    ) -> PropertyDescriptorCollection:
        """"""
    @classmethod
    @overload
    def GetProvider(cls, instance: object) -> TypeDescriptionProvider:
        """"""
    @classmethod
    @overload
    def GetProvider(cls, type: Type) -> TypeDescriptionProvider:
        """"""
    @classmethod
    @overload
    def GetReflectionType(cls, instance: object) -> Type:
        """"""
    @classmethod
    @overload
    def GetReflectionType(cls, type: Type) -> Type:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    @overload
    def Refresh(cls, assembly: Assembly) -> None:
        """"""
    @classmethod
    @overload
    def Refresh(cls, module: Module) -> None:
        """"""
    @classmethod
    @overload
    def Refresh(cls, component: object) -> None:
        """"""
    @classmethod
    @overload
    def Refresh(cls, type: Type) -> None:
        """"""
    @classmethod
    def RemoveAssociation(cls, primary: object, secondary: object) -> None:
        """"""
    @classmethod
    def RemoveAssociations(cls, primary: object) -> None:
        """"""
    @classmethod
    @overload
    def RemoveProvider(cls, provider: TypeDescriptionProvider, instance: object) -> None:
        """"""
    @classmethod
    @overload
    def RemoveProvider(cls, provider: TypeDescriptionProvider, type: Type) -> None:
        """"""
    @classmethod
    @overload
    def RemoveProviderTransparent(cls, provider: TypeDescriptionProvider, instance: object) -> None:
        """"""
    @classmethod
    @overload
    def RemoveProviderTransparent(cls, provider: TypeDescriptionProvider, type: Type) -> None:
        """"""
    @classmethod
    def SortDescriptorArray(cls, infos: IList) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    Refreshed: EventType[RefreshEventHandler] = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class TypeListConverter(ABC, TypeConverter):
    """"""
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool:
        """"""
    @overload
    def CanConvertFrom(self, sourceType: Type) -> bool:
        """"""
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, destinationType: Type) -> bool:
        """"""
    @overload
    def CanConvertTo(self, destinationType: Type) -> bool:
        """"""
    @overload
    def ConvertFrom(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> object:
        """"""
    @overload
    def ConvertFrom(self, value: object) -> object:
        """"""
    @overload
    def ConvertFromInvariantString(self, context: ITypeDescriptorContext, text: str) -> object:
        """"""
    @overload
    def ConvertFromInvariantString(self, text: str) -> object:
        """"""
    @overload
    def ConvertFromString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, text: str
    ) -> object:
        """"""
    @overload
    def ConvertFromString(self, context: ITypeDescriptorContext, text: str) -> object:
        """"""
    @overload
    def ConvertFromString(self, text: str) -> object:
        """"""
    @overload
    def ConvertTo(
        self,
        context: ITypeDescriptorContext,
        culture: CultureInfo,
        value: object,
        destinationType: Type,
    ) -> object:
        """"""
    @overload
    def ConvertTo(self, value: object, destinationType: Type) -> object:
        """"""
    @overload
    def ConvertToInvariantString(self, context: ITypeDescriptorContext, value: object) -> str:
        """"""
    @overload
    def ConvertToInvariantString(self, value: object) -> str:
        """"""
    @overload
    def ConvertToString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> str:
        """"""
    @overload
    def ConvertToString(self, context: ITypeDescriptorContext, value: object) -> str:
        """"""
    @overload
    def ConvertToString(self, value: object) -> str:
        """"""
    @overload
    def CreateInstance(self, propertyValues: IDictionary) -> object:
        """"""
    @overload
    def CreateInstance(
        self, context: ITypeDescriptorContext, propertyValues: IDictionary
    ) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetCreateInstanceSupported(self) -> bool:
        """"""
    @overload
    def GetCreateInstanceSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object
    ) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]
    ) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetProperties(self, value: object) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetPropertiesSupported(self) -> bool:
        """"""
    @overload
    def GetPropertiesSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    @overload
    def GetStandardValues(self) -> ICollection:
        """"""
    @overload
    def GetStandardValues(
        self, context: ITypeDescriptorContext
    ) -> TypeConverter.StandardValuesCollection:
        """"""
    @overload
    def GetStandardValuesExclusive(self) -> bool:
        """"""
    @overload
    def GetStandardValuesExclusive(self, context: ITypeDescriptorContext) -> bool:
        """"""
    @overload
    def GetStandardValuesSupported(self) -> bool:
        """"""
    @overload
    def GetStandardValuesSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IsValid(self, context: ITypeDescriptorContext, value: object) -> bool:
        """"""
    @overload
    def IsValid(self, value: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    # noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
    class StandardValuesCollection(Object, ICollection, IEnumerable):
        """"""
        def __init__(self, values: ICollection) -> None:
            """"""
        @property
        def Count(self) -> int:
            """"""
        @property
        def IsSynchronized(self) -> bool:
            """"""
        @property
        def Item(self) -> object:
            """"""
        @property
        def SyncRoot(self) -> object:
            """"""
        def CopyTo(self, array: Array, index: int) -> None:
            """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def GetEnumerator(self) -> IEnumerator:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def ToString(self) -> str:
            """"""
        def __iter__(self) -> Iterator:
            """"""
        def __len__(self) -> int:
            """"""
        def __getitem__(self, index: int) -> object:
            """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class UInt16Converter(BaseNumberConverter):
    """"""
    def __init__(self) -> None:
        """"""
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool:
        """"""
    @overload
    def CanConvertFrom(self, sourceType: Type) -> bool:
        """"""
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, t: Type) -> bool:
        """"""
    @overload
    def CanConvertTo(self, destinationType: Type) -> bool:
        """"""
    @overload
    def ConvertFrom(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> object:
        """"""
    @overload
    def ConvertFrom(self, value: object) -> object:
        """"""
    @overload
    def ConvertFromInvariantString(self, context: ITypeDescriptorContext, text: str) -> object:
        """"""
    @overload
    def ConvertFromInvariantString(self, text: str) -> object:
        """"""
    @overload
    def ConvertFromString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, text: str
    ) -> object:
        """"""
    @overload
    def ConvertFromString(self, context: ITypeDescriptorContext, text: str) -> object:
        """"""
    @overload
    def ConvertFromString(self, text: str) -> object:
        """"""
    @overload
    def ConvertTo(
        self,
        context: ITypeDescriptorContext,
        culture: CultureInfo,
        value: object,
        destinationType: Type,
    ) -> object:
        """"""
    @overload
    def ConvertTo(self, value: object, destinationType: Type) -> object:
        """"""
    @overload
    def ConvertToInvariantString(self, context: ITypeDescriptorContext, value: object) -> str:
        """"""
    @overload
    def ConvertToInvariantString(self, value: object) -> str:
        """"""
    @overload
    def ConvertToString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> str:
        """"""
    @overload
    def ConvertToString(self, context: ITypeDescriptorContext, value: object) -> str:
        """"""
    @overload
    def ConvertToString(self, value: object) -> str:
        """"""
    @overload
    def CreateInstance(self, propertyValues: IDictionary) -> object:
        """"""
    @overload
    def CreateInstance(
        self, context: ITypeDescriptorContext, propertyValues: IDictionary
    ) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetCreateInstanceSupported(self) -> bool:
        """"""
    @overload
    def GetCreateInstanceSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object
    ) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]
    ) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetProperties(self, value: object) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetPropertiesSupported(self) -> bool:
        """"""
    @overload
    def GetPropertiesSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    @overload
    def GetStandardValues(self) -> ICollection:
        """"""
    @overload
    def GetStandardValues(
        self, context: ITypeDescriptorContext
    ) -> TypeConverter.StandardValuesCollection:
        """"""
    @overload
    def GetStandardValuesExclusive(self) -> bool:
        """"""
    @overload
    def GetStandardValuesExclusive(self, context: ITypeDescriptorContext) -> bool:
        """"""
    @overload
    def GetStandardValuesSupported(self) -> bool:
        """"""
    @overload
    def GetStandardValuesSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IsValid(self, context: ITypeDescriptorContext, value: object) -> bool:
        """"""
    @overload
    def IsValid(self, value: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    # noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
    class StandardValuesCollection(Object, ICollection, IEnumerable):
        """"""
        def __init__(self, values: ICollection) -> None:
            """"""
        @property
        def Count(self) -> int:
            """"""
        @property
        def IsSynchronized(self) -> bool:
            """"""
        @property
        def Item(self) -> object:
            """"""
        @property
        def SyncRoot(self) -> object:
            """"""
        def CopyTo(self, array: Array, index: int) -> None:
            """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def GetEnumerator(self) -> IEnumerator:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def ToString(self) -> str:
            """"""
        def __iter__(self) -> Iterator:
            """"""
        def __len__(self) -> int:
            """"""
        def __getitem__(self, index: int) -> object:
            """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class UInt32Converter(BaseNumberConverter):
    """"""
    def __init__(self) -> None:
        """"""
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool:
        """"""
    @overload
    def CanConvertFrom(self, sourceType: Type) -> bool:
        """"""
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, t: Type) -> bool:
        """"""
    @overload
    def CanConvertTo(self, destinationType: Type) -> bool:
        """"""
    @overload
    def ConvertFrom(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> object:
        """"""
    @overload
    def ConvertFrom(self, value: object) -> object:
        """"""
    @overload
    def ConvertFromInvariantString(self, context: ITypeDescriptorContext, text: str) -> object:
        """"""
    @overload
    def ConvertFromInvariantString(self, text: str) -> object:
        """"""
    @overload
    def ConvertFromString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, text: str
    ) -> object:
        """"""
    @overload
    def ConvertFromString(self, context: ITypeDescriptorContext, text: str) -> object:
        """"""
    @overload
    def ConvertFromString(self, text: str) -> object:
        """"""
    @overload
    def ConvertTo(
        self,
        context: ITypeDescriptorContext,
        culture: CultureInfo,
        value: object,
        destinationType: Type,
    ) -> object:
        """"""
    @overload
    def ConvertTo(self, value: object, destinationType: Type) -> object:
        """"""
    @overload
    def ConvertToInvariantString(self, context: ITypeDescriptorContext, value: object) -> str:
        """"""
    @overload
    def ConvertToInvariantString(self, value: object) -> str:
        """"""
    @overload
    def ConvertToString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> str:
        """"""
    @overload
    def ConvertToString(self, context: ITypeDescriptorContext, value: object) -> str:
        """"""
    @overload
    def ConvertToString(self, value: object) -> str:
        """"""
    @overload
    def CreateInstance(self, propertyValues: IDictionary) -> object:
        """"""
    @overload
    def CreateInstance(
        self, context: ITypeDescriptorContext, propertyValues: IDictionary
    ) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetCreateInstanceSupported(self) -> bool:
        """"""
    @overload
    def GetCreateInstanceSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object
    ) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]
    ) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetProperties(self, value: object) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetPropertiesSupported(self) -> bool:
        """"""
    @overload
    def GetPropertiesSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    @overload
    def GetStandardValues(self) -> ICollection:
        """"""
    @overload
    def GetStandardValues(
        self, context: ITypeDescriptorContext
    ) -> TypeConverter.StandardValuesCollection:
        """"""
    @overload
    def GetStandardValuesExclusive(self) -> bool:
        """"""
    @overload
    def GetStandardValuesExclusive(self, context: ITypeDescriptorContext) -> bool:
        """"""
    @overload
    def GetStandardValuesSupported(self) -> bool:
        """"""
    @overload
    def GetStandardValuesSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IsValid(self, context: ITypeDescriptorContext, value: object) -> bool:
        """"""
    @overload
    def IsValid(self, value: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    # noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
    class StandardValuesCollection(Object, ICollection, IEnumerable):
        """"""
        def __init__(self, values: ICollection) -> None:
            """"""
        @property
        def Count(self) -> int:
            """"""
        @property
        def IsSynchronized(self) -> bool:
            """"""
        @property
        def Item(self) -> object:
            """"""
        @property
        def SyncRoot(self) -> object:
            """"""
        def CopyTo(self, array: Array, index: int) -> None:
            """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def GetEnumerator(self) -> IEnumerator:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def ToString(self) -> str:
            """"""
        def __iter__(self) -> Iterator:
            """"""
        def __len__(self) -> int:
            """"""
        def __getitem__(self, index: int) -> object:
            """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class UInt64Converter(BaseNumberConverter):
    """"""
    def __init__(self) -> None:
        """"""
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool:
        """"""
    @overload
    def CanConvertFrom(self, sourceType: Type) -> bool:
        """"""
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, t: Type) -> bool:
        """"""
    @overload
    def CanConvertTo(self, destinationType: Type) -> bool:
        """"""
    @overload
    def ConvertFrom(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> object:
        """"""
    @overload
    def ConvertFrom(self, value: object) -> object:
        """"""
    @overload
    def ConvertFromInvariantString(self, context: ITypeDescriptorContext, text: str) -> object:
        """"""
    @overload
    def ConvertFromInvariantString(self, text: str) -> object:
        """"""
    @overload
    def ConvertFromString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, text: str
    ) -> object:
        """"""
    @overload
    def ConvertFromString(self, context: ITypeDescriptorContext, text: str) -> object:
        """"""
    @overload
    def ConvertFromString(self, text: str) -> object:
        """"""
    @overload
    def ConvertTo(
        self,
        context: ITypeDescriptorContext,
        culture: CultureInfo,
        value: object,
        destinationType: Type,
    ) -> object:
        """"""
    @overload
    def ConvertTo(self, value: object, destinationType: Type) -> object:
        """"""
    @overload
    def ConvertToInvariantString(self, context: ITypeDescriptorContext, value: object) -> str:
        """"""
    @overload
    def ConvertToInvariantString(self, value: object) -> str:
        """"""
    @overload
    def ConvertToString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> str:
        """"""
    @overload
    def ConvertToString(self, context: ITypeDescriptorContext, value: object) -> str:
        """"""
    @overload
    def ConvertToString(self, value: object) -> str:
        """"""
    @overload
    def CreateInstance(self, propertyValues: IDictionary) -> object:
        """"""
    @overload
    def CreateInstance(
        self, context: ITypeDescriptorContext, propertyValues: IDictionary
    ) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetCreateInstanceSupported(self) -> bool:
        """"""
    @overload
    def GetCreateInstanceSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object
    ) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]
    ) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetProperties(self, value: object) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetPropertiesSupported(self) -> bool:
        """"""
    @overload
    def GetPropertiesSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    @overload
    def GetStandardValues(self) -> ICollection:
        """"""
    @overload
    def GetStandardValues(
        self, context: ITypeDescriptorContext
    ) -> TypeConverter.StandardValuesCollection:
        """"""
    @overload
    def GetStandardValuesExclusive(self) -> bool:
        """"""
    @overload
    def GetStandardValuesExclusive(self, context: ITypeDescriptorContext) -> bool:
        """"""
    @overload
    def GetStandardValuesSupported(self) -> bool:
        """"""
    @overload
    def GetStandardValuesSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IsValid(self, context: ITypeDescriptorContext, value: object) -> bool:
        """"""
    @overload
    def IsValid(self, value: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    # noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
    class StandardValuesCollection(Object, ICollection, IEnumerable):
        """"""
        def __init__(self, values: ICollection) -> None:
            """"""
        @property
        def Count(self) -> int:
            """"""
        @property
        def IsSynchronized(self) -> bool:
            """"""
        @property
        def Item(self) -> object:
            """"""
        @property
        def SyncRoot(self) -> object:
            """"""
        def CopyTo(self, array: Array, index: int) -> None:
            """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def GetEnumerator(self) -> IEnumerator:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def ToString(self) -> str:
            """"""
        def __iter__(self) -> Iterator:
            """"""
        def __len__(self) -> int:
            """"""
        def __getitem__(self, index: int) -> object:
            """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class WarningException(SystemException, _Exception, ISerializable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, message: str) -> None:
        """"""
    @overload
    def __init__(self, message: str, helpUrl: str) -> None:
        """"""
    @overload
    def __init__(self, message: str, innerException: Exception) -> None:
        """"""
    @overload
    def __init__(self, message: str, helpUrl: str, helpTopic: str) -> None:
        """"""
    @property
    def Data(self) -> IDictionary:
        """"""
    @property
    def HResult(self) -> int:
        """"""
    @property
    def HelpLink(self) -> str:
        """"""
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def HelpTopic(self) -> str:
        """"""
    @property
    def HelpUrl(self) -> str:
        """"""
    @property
    def InnerException(self) -> Exception:
        """"""
    @property
    def Message(self) -> str:
        """"""
    @property
    def Source(self) -> str:
        """"""
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """"""
    @property
    def TargetSite(self) -> MethodBase:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetBaseException(self) -> Exception:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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
        """"""
    @property
    def IsFixedSize(self) -> bool:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def Item(self) -> object:
        """"""
    @Item.setter
    def Item(self, value: object) -> None: ...
    @property
    def Keys(self) -> ICollection:
        """"""
    @property
    def SyncRoot(self) -> object:
        """"""
    @property
    def Values(self) -> ICollection:
        """"""
    def Add(self, key: object, value: object) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    def Clone(self) -> object:
        """"""
    def Contains(self, key: object) -> bool:
        """"""
    def ContainsKey(self, key: object) -> bool:
        """"""
    def ContainsValue(self, value: object) -> bool:
        """"""
    def CopyTo(self, array: Array, arrayIndex: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IDictionaryEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def OnDeserialization(self, sender: object) -> None:
        """"""
    def Remove(self, key: object) -> None:
        """"""
    def SetWeak(self, key: object, value: object) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def __contains__(self, key: object) -> bool:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    def __delitem__(self, key: object) -> None:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, key: object) -> object:
        """"""
    def __setitem__(self, key: object, value: object) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class Win32Exception(ExternalException, _Exception, ISerializable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, error: int) -> None:
        """"""
    @overload
    def __init__(self, error: int, message: str) -> None:
        """"""
    @overload
    def __init__(self, message: str) -> None:
        """"""
    @overload
    def __init__(self, message: str, innerException: Exception) -> None:
        """"""
    @property
    def Data(self) -> IDictionary:
        """"""
    @property
    def ErrorCode(self) -> int:
        """"""
    @property
    def HResult(self) -> int:
        """"""
    @property
    def HelpLink(self) -> str:
        """"""
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """"""
    @property
    def Message(self) -> str:
        """"""
    @property
    def NativeErrorCode(self) -> int:
        """"""
    @property
    def Source(self) -> str:
        """"""
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """"""
    @property
    def TargetSite(self) -> MethodBase:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetBaseException(self) -> Exception:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
