from __future__ import annotations

from abc import ABC
from typing import Callable, Generic, List, Protocol, Tuple, TypeVar, Union, overload

from System import ArgumentException, Array, AsyncCallback, Attribute, Boolean, Byte, Char, Delegate, Double, Enum, EventArgs, EventHandler, Exception, IAsyncResult, ICloneable, IDisposable, IServiceProvider, Int16, Int32, Int64, IntPtr, MarshalByRefObject, MulticastDelegate, Object, Single, String, SystemException, Type, Void
from System.Collections import Hashtable, ICollection, IComparer, IDictionary, IEnumerable, IEnumerator, IList, ReadOnlyCollectionBase
from System.Collections.Generic import ICollection, IEnumerable, IList, IReadOnlyCollection, IReadOnlyList
from System.Collections.ObjectModel import Collection
from System.ComponentModel.Design import IDesigner
from System.Diagnostics import BooleanSwitch, TraceSwitch
from System.Globalization import CultureInfo
from System.Reflection import Assembly, EventInfo, MethodInfo, Module, PropertyInfo
from System.Resources import ResourceManager
from System.Runtime.InteropServices import ExternalException, _Attribute, _Exception
from System.Runtime.Serialization import IDeserializationCallback, ISerializable, SerializationInfo, StreamingContext
from System.Security import CodeAccessPermission
from System.Threading import SendOrPostCallback, SynchronizationContext

# ---------- Types ---------- #

T = TypeVar('T')

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
ByteType = Union[int, Byte]
CharType = Union[str, Char]
DoubleType = Union[float, Double]
FloatType = Union[float, Single]
IntType = Union[int, Int32]
LongType = Union[int, Int64]
NIntType = Union[int, IntPtr]
ObjectType = Object
ShortType = Union[int, Int16]
StringType = Union[str, String]
TypeType = Union[type, Type]
VoidType = Union[None, Void]


class EventType(Generic[T]):
    def __iadd__(self, other: T): ...
    
    def __isub__(self, other: T): ...



# ---------- Classes ---------- #

class AddingNewEventArgs(EventArgs):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, newObject: ObjectType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def NewObject(self) -> ObjectType: ...
    
    @NewObject.setter
    def NewObject(self, value: ObjectType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_NewObject(self) -> ObjectType: ...
    
    def set_NewObject(self, value: ObjectType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AddingNewEventHandler(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, sender: ObjectType, e: AddingNewEventArgs, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, sender: ObjectType, e: AddingNewEventArgs) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AmbientValueAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, type: TypeType, value: StringType): ...
    
    @overload
    def __init__(self, value: CharType): ...
    
    @overload
    def __init__(self, value: ByteType): ...
    
    @overload
    def __init__(self, value: ShortType): ...
    
    @overload
    def __init__(self, value: IntType): ...
    
    @overload
    def __init__(self, value: LongType): ...
    
    @overload
    def __init__(self, value: FloatType): ...
    
    @overload
    def __init__(self, value: DoubleType): ...
    
    @overload
    def __init__(self, value: BooleanType): ...
    
    @overload
    def __init__(self, value: StringType): ...
    
    @overload
    def __init__(self, value: ObjectType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def get_Value(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ArrayConverter(CollectionConverter):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def ConvertTo(self, context: ITypeDescriptorContext, culture: CultureInfo, value: ObjectType, destinationType: TypeType) -> ObjectType: ...
    
    @overload
    def GetProperties(self, context: ITypeDescriptorContext, value: ObjectType, attributes: ArrayType[Attribute]) -> PropertyDescriptorCollection: ...
    
    @overload
    def GetPropertiesSupported(self, context: ITypeDescriptorContext) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ArraySubsetEnumerator(ObjectType, IEnumerator):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, array: Array, count: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Current(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def MoveNext(self) -> BooleanType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Current(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AsyncCompletedEventArgs(EventArgs):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, error: Exception, cancelled: BooleanType, userState: ObjectType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Cancelled(self) -> BooleanType: ...
    
    @property
    def Error(self) -> Exception: ...
    
    @property
    def UserState(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def get_Cancelled(self) -> BooleanType: ...
    
    def get_Error(self) -> Exception: ...
    
    def get_UserState(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AsyncCompletedEventHandler(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, sender: ObjectType, e: AsyncCompletedEventArgs, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, sender: ObjectType, e: AsyncCompletedEventArgs) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AsyncOperation(ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def SynchronizationContext(self) -> SynchronizationContext: ...
    
    @property
    def UserSuppliedState(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def OperationCompleted(self) -> VoidType: ...
    
    def Post(self, d: SendOrPostCallback, arg: ObjectType) -> VoidType: ...
    
    def PostOperationCompleted(self, d: SendOrPostCallback, arg: ObjectType) -> VoidType: ...
    
    def get_SynchronizationContext(self) -> SynchronizationContext: ...
    
    def get_UserSuppliedState(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AsyncOperationManager(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def SynchronizationContext() -> SynchronizationContext: ...
    
    @staticmethod
    @SynchronizationContext.setter
    def SynchronizationContext(value: SynchronizationContext) -> None: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def CreateOperation(userSuppliedState: ObjectType) -> AsyncOperation: ...
    
    @staticmethod
    def get_SynchronizationContext() -> SynchronizationContext: ...
    
    @staticmethod
    def set_SynchronizationContext(value: SynchronizationContext) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AttributeCollection(ObjectType, ICollection, IEnumerable):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Empty() -> AttributeCollection: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self, attributes: ArrayType[Attribute]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    def __getitem__(self, key: IntType) -> Attribute: ...
    
    def __getitem__(self, key: TypeType) -> Attribute: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Contains(self, attribute: Attribute) -> BooleanType: ...
    
    @overload
    def Contains(self, attributes: ArrayType[Attribute]) -> BooleanType: ...
    
    def CopyTo(self, array: Array, index: IntType) -> VoidType: ...
    
    @staticmethod
    def FromExisting(existing: AttributeCollection, newAttributes: ArrayType[Attribute]) -> AttributeCollection: ...
    
    def GetEnumerator(self) -> IEnumerator: ...
    
    @overload
    def Matches(self, attribute: Attribute) -> BooleanType: ...
    
    @overload
    def Matches(self, attributes: ArrayType[Attribute]) -> BooleanType: ...
    
    def get_Count(self) -> IntType: ...
    
    @overload
    def get_Item(self, index: IntType) -> Attribute: ...
    
    @overload
    def get_Item(self, attributeType: TypeType) -> Attribute: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AttributeProviderAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, typeName: StringType): ...
    
    @overload
    def __init__(self, typeName: StringType, propertyName: StringType): ...
    
    @overload
    def __init__(self, type: TypeType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def PropertyName(self) -> StringType: ...
    
    @property
    def TypeName(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_PropertyName(self) -> StringType: ...
    
    def get_TypeName(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class BackgroundWorker(Component, IComponent, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CancellationPending(self) -> BooleanType: ...
    
    @property
    def IsBusy(self) -> BooleanType: ...
    
    @property
    def WorkerReportsProgress(self) -> BooleanType: ...
    
    @WorkerReportsProgress.setter
    def WorkerReportsProgress(self, value: BooleanType) -> None: ...
    
    @property
    def WorkerSupportsCancellation(self) -> BooleanType: ...
    
    @WorkerSupportsCancellation.setter
    def WorkerSupportsCancellation(self, value: BooleanType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def CancelAsync(self) -> VoidType: ...
    
    @overload
    def ReportProgress(self, percentProgress: IntType) -> VoidType: ...
    
    @overload
    def ReportProgress(self, percentProgress: IntType, userState: ObjectType) -> VoidType: ...
    
    @overload
    def RunWorkerAsync(self) -> VoidType: ...
    
    @overload
    def RunWorkerAsync(self, argument: ObjectType) -> VoidType: ...
    
    def add_DoWork(self, value: DoWorkEventHandler) -> VoidType: ...
    
    def add_ProgressChanged(self, value: ProgressChangedEventHandler) -> VoidType: ...
    
    def add_RunWorkerCompleted(self, value: RunWorkerCompletedEventHandler) -> VoidType: ...
    
    def get_CancellationPending(self) -> BooleanType: ...
    
    def get_IsBusy(self) -> BooleanType: ...
    
    def get_WorkerReportsProgress(self) -> BooleanType: ...
    
    def get_WorkerSupportsCancellation(self) -> BooleanType: ...
    
    def remove_DoWork(self, value: DoWorkEventHandler) -> VoidType: ...
    
    def remove_ProgressChanged(self, value: ProgressChangedEventHandler) -> VoidType: ...
    
    def remove_RunWorkerCompleted(self, value: RunWorkerCompletedEventHandler) -> VoidType: ...
    
    def set_WorkerReportsProgress(self, value: BooleanType) -> VoidType: ...
    
    def set_WorkerSupportsCancellation(self, value: BooleanType) -> VoidType: ...
    
    # ---------- Events ---------- #
    
    DoWork: EventType[DoWorkEventHandler] = ...
    
    ProgressChanged: EventType[ProgressChangedEventHandler] = ...
    
    RunWorkerCompleted: EventType[RunWorkerCompletedEventHandler] = ...
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class BaseNumberConverter(ABC, TypeConverter):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: TypeType) -> BooleanType: ...
    
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, t: TypeType) -> BooleanType: ...
    
    @overload
    def ConvertFrom(self, context: ITypeDescriptorContext, culture: CultureInfo, value: ObjectType) -> ObjectType: ...
    
    @overload
    def ConvertTo(self, context: ITypeDescriptorContext, culture: CultureInfo, value: ObjectType, destinationType: TypeType) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class BindableAttribute(Attribute, _Attribute):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Default() -> BindableAttribute: ...
    
    @staticmethod
    @property
    def No() -> BindableAttribute: ...
    
    @staticmethod
    @property
    def Yes() -> BindableAttribute: ...
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, bindable: BooleanType): ...
    
    @overload
    def __init__(self, bindable: BooleanType, direction: BindingDirection): ...
    
    @overload
    def __init__(self, flags: BindableSupport): ...
    
    @overload
    def __init__(self, flags: BindableSupport, direction: BindingDirection): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Bindable(self) -> BooleanType: ...
    
    @property
    def Direction(self) -> BindingDirection: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def IsDefaultAttribute(self) -> BooleanType: ...
    
    def get_Bindable(self) -> BooleanType: ...
    
    def get_Direction(self) -> BindingDirection: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class BindingList(Generic[T], Collection[T], IList[T], ICollection[T], IEnumerable[T], IEnumerable, IList, ICollection, IReadOnlyList[T], IReadOnlyCollection[T], IBindingList, ICancelAddNew, IRaiseItemChangedEvents):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, list: IList[T]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AllowEdit(self) -> BooleanType: ...
    
    @AllowEdit.setter
    def AllowEdit(self, value: BooleanType) -> None: ...
    
    @property
    def AllowNew(self) -> BooleanType: ...
    
    @AllowNew.setter
    def AllowNew(self, value: BooleanType) -> None: ...
    
    @property
    def AllowRemove(self) -> BooleanType: ...
    
    @AllowRemove.setter
    def AllowRemove(self, value: BooleanType) -> None: ...
    
    @property
    def RaiseListChangedEvents(self) -> BooleanType: ...
    
    @RaiseListChangedEvents.setter
    def RaiseListChangedEvents(self, value: BooleanType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def AddNew(self) -> T: ...
    
    def CancelNew(self, itemIndex: IntType) -> VoidType: ...
    
    def EndNew(self, itemIndex: IntType) -> VoidType: ...
    
    def ResetBindings(self) -> VoidType: ...
    
    def ResetItem(self, position: IntType) -> VoidType: ...
    
    def add_AddingNew(self, value: AddingNewEventHandler) -> VoidType: ...
    
    def add_ListChanged(self, value: ListChangedEventHandler) -> VoidType: ...
    
    def get_AllowEdit(self) -> BooleanType: ...
    
    def get_AllowNew(self) -> BooleanType: ...
    
    def get_AllowRemove(self) -> BooleanType: ...
    
    def get_RaiseListChangedEvents(self) -> BooleanType: ...
    
    def remove_AddingNew(self, value: AddingNewEventHandler) -> VoidType: ...
    
    def remove_ListChanged(self, value: ListChangedEventHandler) -> VoidType: ...
    
    def set_AllowEdit(self, value: BooleanType) -> VoidType: ...
    
    def set_AllowNew(self, value: BooleanType) -> VoidType: ...
    
    def set_AllowRemove(self, value: BooleanType) -> VoidType: ...
    
    def set_RaiseListChangedEvents(self, value: BooleanType) -> VoidType: ...
    
    # ---------- Events ---------- #
    
    AddingNew: EventType[AddingNewEventHandler] = ...
    
    ListChanged: EventType[ListChangedEventHandler] = ...
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class BooleanConverter(TypeConverter):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: TypeType) -> BooleanType: ...
    
    @overload
    def ConvertFrom(self, context: ITypeDescriptorContext, culture: CultureInfo, value: ObjectType) -> ObjectType: ...
    
    @overload
    def GetStandardValues(self, context: ITypeDescriptorContext) -> StandardValuesCollection: ...
    
    @overload
    def GetStandardValuesExclusive(self, context: ITypeDescriptorContext) -> BooleanType: ...
    
    @overload
    def GetStandardValuesSupported(self, context: ITypeDescriptorContext) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class BrowsableAttribute(Attribute, _Attribute):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Default() -> BrowsableAttribute: ...
    
    @staticmethod
    @property
    def No() -> BrowsableAttribute: ...
    
    @staticmethod
    @property
    def Yes() -> BrowsableAttribute: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self, browsable: BooleanType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Browsable(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def IsDefaultAttribute(self) -> BooleanType: ...
    
    def get_Browsable(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ByteConverter(BaseNumberConverter):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CancelEventArgs(EventArgs):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, cancel: BooleanType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Cancel(self) -> BooleanType: ...
    
    @Cancel.setter
    def Cancel(self, value: BooleanType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Cancel(self) -> BooleanType: ...
    
    def set_Cancel(self, value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CancelEventHandler(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, sender: ObjectType, e: CancelEventArgs, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, sender: ObjectType, e: CancelEventArgs) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CategoryAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, category: StringType): ...
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def Action() -> CategoryAttribute: ...
    
    @staticmethod
    @property
    def Appearance() -> CategoryAttribute: ...
    
    @staticmethod
    @property
    def Asynchronous() -> CategoryAttribute: ...
    
    @staticmethod
    @property
    def Behavior() -> CategoryAttribute: ...
    
    @property
    def Category(self) -> StringType: ...
    
    @staticmethod
    @property
    def Data() -> CategoryAttribute: ...
    
    @staticmethod
    @property
    def Default() -> CategoryAttribute: ...
    
    @staticmethod
    @property
    def Design() -> CategoryAttribute: ...
    
    @staticmethod
    @property
    def DragDrop() -> CategoryAttribute: ...
    
    @staticmethod
    @property
    def Focus() -> CategoryAttribute: ...
    
    @staticmethod
    @property
    def Format() -> CategoryAttribute: ...
    
    @staticmethod
    @property
    def Key() -> CategoryAttribute: ...
    
    @staticmethod
    @property
    def Layout() -> CategoryAttribute: ...
    
    @staticmethod
    @property
    def Mouse() -> CategoryAttribute: ...
    
    @staticmethod
    @property
    def WindowStyle() -> CategoryAttribute: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def IsDefaultAttribute(self) -> BooleanType: ...
    
    @staticmethod
    def get_Action() -> CategoryAttribute: ...
    
    @staticmethod
    def get_Appearance() -> CategoryAttribute: ...
    
    @staticmethod
    def get_Asynchronous() -> CategoryAttribute: ...
    
    @staticmethod
    def get_Behavior() -> CategoryAttribute: ...
    
    def get_Category(self) -> StringType: ...
    
    @staticmethod
    def get_Data() -> CategoryAttribute: ...
    
    @staticmethod
    def get_Default() -> CategoryAttribute: ...
    
    @staticmethod
    def get_Design() -> CategoryAttribute: ...
    
    @staticmethod
    def get_DragDrop() -> CategoryAttribute: ...
    
    @staticmethod
    def get_Focus() -> CategoryAttribute: ...
    
    @staticmethod
    def get_Format() -> CategoryAttribute: ...
    
    @staticmethod
    def get_Key() -> CategoryAttribute: ...
    
    @staticmethod
    def get_Layout() -> CategoryAttribute: ...
    
    @staticmethod
    def get_Mouse() -> CategoryAttribute: ...
    
    @staticmethod
    def get_WindowStyle() -> CategoryAttribute: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CharConverter(TypeConverter):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: TypeType) -> BooleanType: ...
    
    @overload
    def ConvertFrom(self, context: ITypeDescriptorContext, culture: CultureInfo, value: ObjectType) -> ObjectType: ...
    
    @overload
    def ConvertTo(self, context: ITypeDescriptorContext, culture: CultureInfo, value: ObjectType, destinationType: TypeType) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CollectionChangeEventArgs(EventArgs):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, action: CollectionChangeAction, element: ObjectType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Action(self) -> CollectionChangeAction: ...
    
    @property
    def Element(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def get_Action(self) -> CollectionChangeAction: ...
    
    def get_Element(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CollectionChangeEventHandler(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, sender: ObjectType, e: CollectionChangeEventArgs, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, sender: ObjectType, e: CollectionChangeEventArgs) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CollectionConverter(TypeConverter):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def ConvertTo(self, context: ITypeDescriptorContext, culture: CultureInfo, value: ObjectType, destinationType: TypeType) -> ObjectType: ...
    
    @overload
    def GetProperties(self, context: ITypeDescriptorContext, value: ObjectType, attributes: ArrayType[Attribute]) -> PropertyDescriptorCollection: ...
    
    @overload
    def GetPropertiesSupported(self, context: ITypeDescriptorContext) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CompModSwitches(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def CommonDesignerServices() -> BooleanSwitch: ...
    
    @staticmethod
    @property
    def EventLog() -> TraceSwitch: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def get_CommonDesignerServices() -> BooleanSwitch: ...
    
    @staticmethod
    def get_EventLog() -> TraceSwitch: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ComplexBindingPropertiesAttribute(Attribute, _Attribute):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Default() -> ComplexBindingPropertiesAttribute: ...
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, dataSource: StringType): ...
    
    @overload
    def __init__(self, dataSource: StringType, dataMember: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def DataMember(self) -> StringType: ...
    
    @property
    def DataSource(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def get_DataMember(self) -> StringType: ...
    
    def get_DataSource(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Component(MarshalByRefObject, IComponent, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Container(self) -> IContainer: ...
    
    @property
    def Site(self) -> ISite: ...
    
    @Site.setter
    def Site(self, value: ISite) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Dispose(self) -> VoidType: ...
    
    def ToString(self) -> StringType: ...
    
    def add_Disposed(self, value: EventHandler) -> VoidType: ...
    
    def get_Container(self) -> IContainer: ...
    
    def get_Site(self) -> ISite: ...
    
    def remove_Disposed(self, value: EventHandler) -> VoidType: ...
    
    def set_Site(self, value: ISite) -> VoidType: ...
    
    # ---------- Events ---------- #
    
    Disposed: EventType[EventHandler] = ...
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ComponentCollection(ReadOnlyCollectionBase, ICollection, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, components: ArrayType[IComponent]): ...
    
    # ---------- Properties ---------- #
    
    def __getitem__(self, key: StringType) -> IComponent: ...
    
    def __getitem__(self, key: IntType) -> IComponent: ...
    
    # ---------- Methods ---------- #
    
    def CopyTo(self, array: ArrayType[IComponent], index: IntType) -> VoidType: ...
    
    @overload
    def get_Item(self, name: StringType) -> IComponent: ...
    
    @overload
    def get_Item(self, index: IntType) -> IComponent: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ComponentConverter(ReferenceConverter):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, type: TypeType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def GetProperties(self, context: ITypeDescriptorContext, value: ObjectType, attributes: ArrayType[Attribute]) -> PropertyDescriptorCollection: ...
    
    @overload
    def GetPropertiesSupported(self, context: ITypeDescriptorContext) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ComponentEditor(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def EditComponent(self, component: ObjectType) -> BooleanType: ...
    
    @overload
    def EditComponent(self, context: ITypeDescriptorContext, component: ObjectType) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ComponentResourceManager(ResourceManager):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, t: TypeType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def ApplyResources(self, value: ObjectType, objectName: StringType) -> VoidType: ...
    
    @overload
    def ApplyResources(self, value: ObjectType, objectName: StringType, culture: CultureInfo) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Container(ObjectType, IContainer, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Components(self) -> ComponentCollection: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Add(self, component: IComponent) -> VoidType: ...
    
    @overload
    def Add(self, component: IComponent, name: StringType) -> VoidType: ...
    
    def Dispose(self) -> VoidType: ...
    
    def Remove(self, component: IComponent) -> VoidType: ...
    
    def get_Components(self) -> ComponentCollection: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ContainerFilterService(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def FilterComponents(self, components: ComponentCollection) -> ComponentCollection: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CultureInfoConverter(TypeConverter):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: TypeType) -> BooleanType: ...
    
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, destinationType: TypeType) -> BooleanType: ...
    
    @overload
    def ConvertFrom(self, context: ITypeDescriptorContext, culture: CultureInfo, value: ObjectType) -> ObjectType: ...
    
    @overload
    def ConvertTo(self, context: ITypeDescriptorContext, culture: CultureInfo, value: ObjectType, destinationType: TypeType) -> ObjectType: ...
    
    @overload
    def GetStandardValues(self, context: ITypeDescriptorContext) -> StandardValuesCollection: ...
    
    @overload
    def GetStandardValuesExclusive(self, context: ITypeDescriptorContext) -> BooleanType: ...
    
    @overload
    def GetStandardValuesSupported(self, context: ITypeDescriptorContext) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CustomTypeDescriptor(ABC, ObjectType, ICustomTypeDescriptor):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetAttributes(self) -> AttributeCollection: ...
    
    def GetClassName(self) -> StringType: ...
    
    def GetComponentName(self) -> StringType: ...
    
    def GetConverter(self) -> TypeConverter: ...
    
    def GetDefaultEvent(self) -> EventDescriptor: ...
    
    def GetDefaultProperty(self) -> PropertyDescriptor: ...
    
    def GetEditor(self, editorBaseType: TypeType) -> ObjectType: ...
    
    @overload
    def GetEvents(self) -> EventDescriptorCollection: ...
    
    @overload
    def GetEvents(self, attributes: ArrayType[Attribute]) -> EventDescriptorCollection: ...
    
    @overload
    def GetProperties(self, attributes: ArrayType[Attribute]) -> PropertyDescriptorCollection: ...
    
    @overload
    def GetProperties(self) -> PropertyDescriptorCollection: ...
    
    def GetPropertyOwner(self, pd: PropertyDescriptor) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DataErrorsChangedEventArgs(EventArgs):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, propertyName: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def PropertyName(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_PropertyName(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DataObjectAttribute(Attribute, _Attribute):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def DataObject() -> DataObjectAttribute: ...
    
    @staticmethod
    @property
    def Default() -> DataObjectAttribute: ...
    
    @staticmethod
    @property
    def NonDataObject() -> DataObjectAttribute: ...
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, isDataObject: BooleanType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def IsDataObject(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def IsDefaultAttribute(self) -> BooleanType: ...
    
    def get_IsDataObject(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DataObjectFieldAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, primaryKey: BooleanType): ...
    
    @overload
    def __init__(self, primaryKey: BooleanType, isIdentity: BooleanType): ...
    
    @overload
    def __init__(self, primaryKey: BooleanType, isIdentity: BooleanType, isNullable: BooleanType): ...
    
    @overload
    def __init__(self, primaryKey: BooleanType, isIdentity: BooleanType, isNullable: BooleanType, length: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def IsIdentity(self) -> BooleanType: ...
    
    @property
    def IsNullable(self) -> BooleanType: ...
    
    @property
    def Length(self) -> IntType: ...
    
    @property
    def PrimaryKey(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def get_IsIdentity(self) -> BooleanType: ...
    
    def get_IsNullable(self) -> BooleanType: ...
    
    def get_Length(self) -> IntType: ...
    
    def get_PrimaryKey(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DataObjectMethodAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, methodType: DataObjectMethodType): ...
    
    @overload
    def __init__(self, methodType: DataObjectMethodType, isDefault: BooleanType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def IsDefault(self) -> BooleanType: ...
    
    @property
    def MethodType(self) -> DataObjectMethodType: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def Match(self, obj: ObjectType) -> BooleanType: ...
    
    def get_IsDefault(self) -> BooleanType: ...
    
    def get_MethodType(self) -> DataObjectMethodType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DateTimeConverter(TypeConverter):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: TypeType) -> BooleanType: ...
    
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, destinationType: TypeType) -> BooleanType: ...
    
    @overload
    def ConvertFrom(self, context: ITypeDescriptorContext, culture: CultureInfo, value: ObjectType) -> ObjectType: ...
    
    @overload
    def ConvertTo(self, context: ITypeDescriptorContext, culture: CultureInfo, value: ObjectType, destinationType: TypeType) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DateTimeOffsetConverter(TypeConverter):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: TypeType) -> BooleanType: ...
    
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, destinationType: TypeType) -> BooleanType: ...
    
    @overload
    def ConvertFrom(self, context: ITypeDescriptorContext, culture: CultureInfo, value: ObjectType) -> ObjectType: ...
    
    @overload
    def ConvertTo(self, context: ITypeDescriptorContext, culture: CultureInfo, value: ObjectType, destinationType: TypeType) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DecimalConverter(BaseNumberConverter):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, destinationType: TypeType) -> BooleanType: ...
    
    @overload
    def ConvertTo(self, context: ITypeDescriptorContext, culture: CultureInfo, value: ObjectType, destinationType: TypeType) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DefaultBindingPropertyAttribute(Attribute, _Attribute):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Default() -> DefaultBindingPropertyAttribute: ...
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, name: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Name(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def get_Name(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DefaultEventAttribute(Attribute, _Attribute):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Default() -> DefaultEventAttribute: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self, name: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Name(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def get_Name(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DefaultPropertyAttribute(Attribute, _Attribute):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Default() -> DefaultPropertyAttribute: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self, name: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Name(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def get_Name(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DefaultValueAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, type: TypeType, value: StringType): ...
    
    @overload
    def __init__(self, value: CharType): ...
    
    @overload
    def __init__(self, value: ByteType): ...
    
    @overload
    def __init__(self, value: ShortType): ...
    
    @overload
    def __init__(self, value: IntType): ...
    
    @overload
    def __init__(self, value: LongType): ...
    
    @overload
    def __init__(self, value: FloatType): ...
    
    @overload
    def __init__(self, value: DoubleType): ...
    
    @overload
    def __init__(self, value: BooleanType): ...
    
    @overload
    def __init__(self, value: StringType): ...
    
    @overload
    def __init__(self, value: ObjectType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def get_Value(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DelegatingTypeDescriptionProvider(TypeDescriptionProvider):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def CreateInstance(self, provider: IServiceProvider, objectType: TypeType, argTypes: ArrayType[TypeType], args: ArrayType[ObjectType]) -> ObjectType: ...
    
    def GetCache(self, instance: ObjectType) -> IDictionary: ...
    
    def GetExtendedTypeDescriptor(self, instance: ObjectType) -> ICustomTypeDescriptor: ...
    
    def GetFullComponentName(self, component: ObjectType) -> StringType: ...
    
    @overload
    def GetReflectionType(self, objectType: TypeType, instance: ObjectType) -> TypeType: ...
    
    def GetRuntimeType(self, objectType: TypeType) -> TypeType: ...
    
    @overload
    def GetTypeDescriptor(self, objectType: TypeType, instance: ObjectType) -> ICustomTypeDescriptor: ...
    
    def IsSupportedType(self, type: TypeType) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DescriptionAttribute(Attribute, _Attribute):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Default() -> DescriptionAttribute: ...
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, description: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Description(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def IsDefaultAttribute(self) -> BooleanType: ...
    
    def get_Description(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DesignOnlyAttribute(Attribute, _Attribute):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Default() -> DesignOnlyAttribute: ...
    
    @staticmethod
    @property
    def No() -> DesignOnlyAttribute: ...
    
    @staticmethod
    @property
    def Yes() -> DesignOnlyAttribute: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self, isDesignOnly: BooleanType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def IsDesignOnly(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def IsDefaultAttribute(self) -> BooleanType: ...
    
    def get_IsDesignOnly(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DesignTimeVisibleAttribute(Attribute, _Attribute):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Default() -> DesignTimeVisibleAttribute: ...
    
    @staticmethod
    @property
    def No() -> DesignTimeVisibleAttribute: ...
    
    @staticmethod
    @property
    def Yes() -> DesignTimeVisibleAttribute: ...
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, visible: BooleanType): ...
    
    @overload
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Visible(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def IsDefaultAttribute(self) -> BooleanType: ...
    
    def get_Visible(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DesignerAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, designerTypeName: StringType): ...
    
    @overload
    def __init__(self, designerType: TypeType): ...
    
    @overload
    def __init__(self, designerTypeName: StringType, designerBaseTypeName: StringType): ...
    
    @overload
    def __init__(self, designerTypeName: StringType, designerBaseType: TypeType): ...
    
    @overload
    def __init__(self, designerType: TypeType, designerBaseType: TypeType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def DesignerBaseTypeName(self) -> StringType: ...
    
    @property
    def DesignerTypeName(self) -> StringType: ...
    
    @property
    def TypeId(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def get_DesignerBaseTypeName(self) -> StringType: ...
    
    def get_DesignerTypeName(self) -> StringType: ...
    
    def get_TypeId(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DesignerCategoryAttribute(Attribute, _Attribute):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Component() -> DesignerCategoryAttribute: ...
    
    @staticmethod
    @property
    def Default() -> DesignerCategoryAttribute: ...
    
    @staticmethod
    @property
    def Form() -> DesignerCategoryAttribute: ...
    
    @staticmethod
    @property
    def Generic() -> DesignerCategoryAttribute: ...
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, category: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Category(self) -> StringType: ...
    
    @property
    def TypeId(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def IsDefaultAttribute(self) -> BooleanType: ...
    
    def get_Category(self) -> StringType: ...
    
    def get_TypeId(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DesignerSerializationVisibilityAttribute(Attribute, _Attribute):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Content() -> DesignerSerializationVisibilityAttribute: ...
    
    @staticmethod
    @property
    def Default() -> DesignerSerializationVisibilityAttribute: ...
    
    @staticmethod
    @property
    def Hidden() -> DesignerSerializationVisibilityAttribute: ...
    
    @staticmethod
    @property
    def Visible() -> DesignerSerializationVisibilityAttribute: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self, visibility: DesignerSerializationVisibility): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Visibility(self) -> DesignerSerializationVisibility: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def IsDefaultAttribute(self) -> BooleanType: ...
    
    def get_Visibility(self) -> DesignerSerializationVisibility: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DisplayNameAttribute(Attribute, _Attribute):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Default() -> DisplayNameAttribute: ...
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, displayName: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def DisplayName(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def IsDefaultAttribute(self) -> BooleanType: ...
    
    def get_DisplayName(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DoWorkEventArgs(CancelEventArgs):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, argument: ObjectType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Argument(self) -> ObjectType: ...
    
    @property
    def Result(self) -> ObjectType: ...
    
    @Result.setter
    def Result(self, value: ObjectType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Argument(self) -> ObjectType: ...
    
    def get_Result(self) -> ObjectType: ...
    
    def set_Result(self, value: ObjectType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DoWorkEventHandler(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, sender: ObjectType, e: DoWorkEventArgs, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, sender: ObjectType, e: DoWorkEventArgs) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DoubleConverter(BaseNumberConverter):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EditorAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, typeName: StringType, baseTypeName: StringType): ...
    
    @overload
    def __init__(self, typeName: StringType, baseType: TypeType): ...
    
    @overload
    def __init__(self, type: TypeType, baseType: TypeType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def EditorBaseTypeName(self) -> StringType: ...
    
    @property
    def EditorTypeName(self) -> StringType: ...
    
    @property
    def TypeId(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def get_EditorBaseTypeName(self) -> StringType: ...
    
    def get_EditorTypeName(self) -> StringType: ...
    
    def get_TypeId(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EditorBrowsableAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, state: EditorBrowsableState): ...
    
    @overload
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def State(self) -> EditorBrowsableState: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def get_State(self) -> EditorBrowsableState: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EnumConverter(TypeConverter):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, type: TypeType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: TypeType) -> BooleanType: ...
    
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, destinationType: TypeType) -> BooleanType: ...
    
    @overload
    def ConvertFrom(self, context: ITypeDescriptorContext, culture: CultureInfo, value: ObjectType) -> ObjectType: ...
    
    @overload
    def ConvertTo(self, context: ITypeDescriptorContext, culture: CultureInfo, value: ObjectType, destinationType: TypeType) -> ObjectType: ...
    
    @overload
    def GetStandardValues(self, context: ITypeDescriptorContext) -> StandardValuesCollection: ...
    
    @overload
    def GetStandardValuesExclusive(self, context: ITypeDescriptorContext) -> BooleanType: ...
    
    @overload
    def GetStandardValuesSupported(self, context: ITypeDescriptorContext) -> BooleanType: ...
    
    @overload
    def IsValid(self, context: ITypeDescriptorContext, value: ObjectType) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EventDescriptor(ABC, MemberDescriptor):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def ComponentType(self) -> TypeType: ...
    
    @property
    def EventType(self) -> TypeType: ...
    
    @property
    def IsMulticast(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def AddEventHandler(self, component: ObjectType, value: Delegate) -> VoidType: ...
    
    def RemoveEventHandler(self, component: ObjectType, value: Delegate) -> VoidType: ...
    
    def get_ComponentType(self) -> TypeType: ...
    
    def get_EventType(self) -> TypeType: ...
    
    def get_IsMulticast(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EventDescriptorCollection(ObjectType, ICollection, IEnumerable, IList):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Empty() -> EventDescriptorCollection: ...
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, events: ArrayType[EventDescriptor]): ...
    
    @overload
    def __init__(self, events: ArrayType[EventDescriptor], readOnly: BooleanType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    def __getitem__(self, key: IntType) -> EventDescriptor: ...
    
    def __getitem__(self, key: StringType) -> EventDescriptor: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, value: EventDescriptor) -> IntType: ...
    
    def Clear(self) -> VoidType: ...
    
    def Contains(self, value: EventDescriptor) -> BooleanType: ...
    
    def Find(self, name: StringType, ignoreCase: BooleanType) -> EventDescriptor: ...
    
    def GetEnumerator(self) -> IEnumerator: ...
    
    def IndexOf(self, value: EventDescriptor) -> IntType: ...
    
    def Insert(self, index: IntType, value: EventDescriptor) -> VoidType: ...
    
    def Remove(self, value: EventDescriptor) -> VoidType: ...
    
    def RemoveAt(self, index: IntType) -> VoidType: ...
    
    @overload
    def Sort(self) -> EventDescriptorCollection: ...
    
    @overload
    def Sort(self, names: ArrayType[StringType]) -> EventDescriptorCollection: ...
    
    @overload
    def Sort(self, names: ArrayType[StringType], comparer: IComparer) -> EventDescriptorCollection: ...
    
    @overload
    def Sort(self, comparer: IComparer) -> EventDescriptorCollection: ...
    
    def get_Count(self) -> IntType: ...
    
    @overload
    def get_Item(self, index: IntType) -> EventDescriptor: ...
    
    @overload
    def get_Item(self, name: StringType) -> EventDescriptor: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EventHandlerList(ObjectType, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    def __getitem__(self, key: ObjectType) -> Delegate: ...
    
    def __setitem__(self, key: ObjectType, value: Delegate) -> None: ...
    
    # ---------- Methods ---------- #
    
    def AddHandler(self, key: ObjectType, value: Delegate) -> VoidType: ...
    
    def AddHandlers(self, listToAddFrom: EventHandlerList) -> VoidType: ...
    
    def Dispose(self) -> VoidType: ...
    
    def RemoveHandler(self, key: ObjectType, value: Delegate) -> VoidType: ...
    
    def get_Item(self, key: ObjectType) -> Delegate: ...
    
    def set_Item(self, key: ObjectType, value: Delegate) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ExpandableObjectConverter(TypeConverter):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def GetProperties(self, context: ITypeDescriptorContext, value: ObjectType, attributes: ArrayType[Attribute]) -> PropertyDescriptorCollection: ...
    
    @overload
    def GetPropertiesSupported(self, context: ITypeDescriptorContext) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ExtendedPropertyDescriptor(PropertyDescriptor):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, extenderInfo: ReflectPropertyDescriptor, receiverType: TypeType, provider: IExtenderProvider, attributes: ArrayType[Attribute]): ...
    
    @overload
    def __init__(self, extender: PropertyDescriptor, attributes: ArrayType[Attribute]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ComponentType(self) -> TypeType: ...
    
    @property
    def DisplayName(self) -> StringType: ...
    
    @property
    def IsReadOnly(self) -> BooleanType: ...
    
    @property
    def PropertyType(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def CanResetValue(self, comp: ObjectType) -> BooleanType: ...
    
    def GetValue(self, comp: ObjectType) -> ObjectType: ...
    
    def ResetValue(self, comp: ObjectType) -> VoidType: ...
    
    def SetValue(self, component: ObjectType, value: ObjectType) -> VoidType: ...
    
    def ShouldSerializeValue(self, comp: ObjectType) -> BooleanType: ...
    
    def get_ComponentType(self) -> TypeType: ...
    
    def get_DisplayName(self) -> StringType: ...
    
    def get_IsReadOnly(self) -> BooleanType: ...
    
    def get_PropertyType(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ExtenderProvidedPropertyAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ExtenderProperty(self) -> PropertyDescriptor: ...
    
    @property
    def Provider(self) -> IExtenderProvider: ...
    
    @property
    def ReceiverType(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def IsDefaultAttribute(self) -> BooleanType: ...
    
    def get_ExtenderProperty(self) -> PropertyDescriptor: ...
    
    def get_Provider(self) -> IExtenderProvider: ...
    
    def get_ReceiverType(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class GuidConverter(TypeConverter):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: TypeType) -> BooleanType: ...
    
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, destinationType: TypeType) -> BooleanType: ...
    
    @overload
    def ConvertFrom(self, context: ITypeDescriptorContext, culture: CultureInfo, value: ObjectType) -> ObjectType: ...
    
    @overload
    def ConvertTo(self, context: ITypeDescriptorContext, culture: CultureInfo, value: ObjectType, destinationType: TypeType) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class HandledEventArgs(EventArgs):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, defaultHandledValue: BooleanType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Handled(self) -> BooleanType: ...
    
    @Handled.setter
    def Handled(self, value: BooleanType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Handled(self) -> BooleanType: ...
    
    def set_Handled(self, value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class HandledEventHandler(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, sender: ObjectType, e: HandledEventArgs, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, sender: ObjectType, e: HandledEventArgs) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ImmutableObjectAttribute(Attribute, _Attribute):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Default() -> ImmutableObjectAttribute: ...
    
    @staticmethod
    @property
    def No() -> ImmutableObjectAttribute: ...
    
    @staticmethod
    @property
    def Yes() -> ImmutableObjectAttribute: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self, immutable: BooleanType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Immutable(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def IsDefaultAttribute(self) -> BooleanType: ...
    
    def get_Immutable(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class InheritanceAttribute(Attribute, _Attribute):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Default() -> InheritanceAttribute: ...
    
    @staticmethod
    @property
    def Inherited() -> InheritanceAttribute: ...
    
    @staticmethod
    @property
    def InheritedReadOnly() -> InheritanceAttribute: ...
    
    @staticmethod
    @property
    def NotInherited() -> InheritanceAttribute: ...
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, inheritanceLevel: InheritanceLevel): ...
    
    # ---------- Properties ---------- #
    
    @property
    def InheritanceLevel(self) -> InheritanceLevel: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, value: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def IsDefaultAttribute(self) -> BooleanType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_InheritanceLevel(self) -> InheritanceLevel: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class InitializationEventAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, eventName: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def EventName(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_EventName(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class InstallerTypeAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, installerType: TypeType): ...
    
    @overload
    def __init__(self, typeName: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def InstallerType(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def get_InstallerType(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class InstanceCreationEditor(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Text(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def CreateInstance(self, context: ITypeDescriptorContext, instanceType: TypeType) -> ObjectType: ...
    
    def get_Text(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Int16Converter(BaseNumberConverter):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Int32Converter(BaseNumberConverter):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Int64Converter(BaseNumberConverter):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IntSecurity(ABC, ObjectType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def FullReflection() -> CodeAccessPermission: ...
    
    @staticmethod
    @property
    def UnmanagedCode() -> CodeAccessPermission: ...
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def UnsafeGetFullPath(fileName: StringType) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class InvalidAsynchronousStateException(ArgumentException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class InvalidEnumArgumentException(ArgumentException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    @overload
    def __init__(self, argumentName: StringType, invalidValue: IntType, enumClass: TypeType): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class LicFileLicenseProvider(LicenseProvider):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetLicense(self, context: LicenseContext, type: TypeType, instance: ObjectType, allowExceptions: BooleanType) -> License: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class License(ABC, ObjectType, IDisposable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def LicenseKey(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def Dispose(self) -> VoidType: ...
    
    def get_LicenseKey(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class LicenseContext(ObjectType, IServiceProvider):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def UsageMode(self) -> LicenseUsageMode: ...
    
    # ---------- Methods ---------- #
    
    def GetSavedLicenseKey(self, type: TypeType, resourceAssembly: Assembly) -> StringType: ...
    
    def GetService(self, type: TypeType) -> ObjectType: ...
    
    def SetSavedLicenseKey(self, type: TypeType, key: StringType) -> VoidType: ...
    
    def get_UsageMode(self) -> LicenseUsageMode: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class LicenseException(SystemException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, type: TypeType): ...
    
    @overload
    def __init__(self, type: TypeType, instance: ObjectType): ...
    
    @overload
    def __init__(self, type: TypeType, instance: ObjectType, message: StringType): ...
    
    @overload
    def __init__(self, type: TypeType, instance: ObjectType, message: StringType, innerException: Exception): ...
    
    # ---------- Properties ---------- #
    
    @property
    def LicensedType(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    
    def get_LicensedType(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class LicenseManager(ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def CurrentContext() -> LicenseContext: ...
    
    @staticmethod
    @CurrentContext.setter
    def CurrentContext(value: LicenseContext) -> None: ...
    
    @staticmethod
    @property
    def UsageMode() -> LicenseUsageMode: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    @overload
    def CreateWithContext(type: TypeType, creationContext: LicenseContext, args: ArrayType[ObjectType]) -> ObjectType: ...
    
    @staticmethod
    @overload
    def CreateWithContext(type: TypeType, creationContext: LicenseContext) -> ObjectType: ...
    
    @staticmethod
    def IsLicensed(type: TypeType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def IsValid(type: TypeType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def IsValid(type: TypeType, instance: ObjectType, license: License) -> Tuple[BooleanType, License]: ...
    
    @staticmethod
    def LockContext(contextUser: ObjectType) -> VoidType: ...
    
    @staticmethod
    def UnlockContext(contextUser: ObjectType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Validate(type: TypeType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Validate(type: TypeType, instance: ObjectType) -> License: ...
    
    @staticmethod
    def get_CurrentContext() -> LicenseContext: ...
    
    @staticmethod
    def get_UsageMode() -> LicenseUsageMode: ...
    
    @staticmethod
    def set_CurrentContext(value: LicenseContext) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class LicenseProvider(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetLicense(self, context: LicenseContext, type: TypeType, instance: ObjectType, allowExceptions: BooleanType) -> License: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class LicenseProviderAttribute(Attribute, _Attribute):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Default() -> LicenseProviderAttribute: ...
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, typeName: StringType): ...
    
    @overload
    def __init__(self, type: TypeType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def LicenseProvider(self) -> TypeType: ...
    
    @property
    def TypeId(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, value: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def get_LicenseProvider(self) -> TypeType: ...
    
    def get_TypeId(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ListBindableAttribute(Attribute, _Attribute):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Default() -> ListBindableAttribute: ...
    
    @staticmethod
    @property
    def No() -> ListBindableAttribute: ...
    
    @staticmethod
    @property
    def Yes() -> ListBindableAttribute: ...
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, listBindable: BooleanType): ...
    
    @overload
    def __init__(self, flags: BindableSupport): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ListBindable(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def IsDefaultAttribute(self) -> BooleanType: ...
    
    def get_ListBindable(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ListChangedEventArgs(EventArgs):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, listChangedType: ListChangedType, newIndex: IntType): ...
    
    @overload
    def __init__(self, listChangedType: ListChangedType, newIndex: IntType, propDesc: PropertyDescriptor): ...
    
    @overload
    def __init__(self, listChangedType: ListChangedType, propDesc: PropertyDescriptor): ...
    
    @overload
    def __init__(self, listChangedType: ListChangedType, newIndex: IntType, oldIndex: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ListChangedType(self) -> ListChangedType: ...
    
    @property
    def NewIndex(self) -> IntType: ...
    
    @property
    def OldIndex(self) -> IntType: ...
    
    @property
    def PropertyDescriptor(self) -> PropertyDescriptor: ...
    
    # ---------- Methods ---------- #
    
    def get_ListChangedType(self) -> ListChangedType: ...
    
    def get_NewIndex(self) -> IntType: ...
    
    def get_OldIndex(self) -> IntType: ...
    
    def get_PropertyDescriptor(self) -> PropertyDescriptor: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ListChangedEventHandler(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, sender: ObjectType, e: ListChangedEventArgs, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, sender: ObjectType, e: ListChangedEventArgs) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ListSortDescription(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, property: PropertyDescriptor, direction: ListSortDirection): ...
    
    # ---------- Properties ---------- #
    
    @property
    def PropertyDescriptor(self) -> PropertyDescriptor: ...
    
    @PropertyDescriptor.setter
    def PropertyDescriptor(self, value: PropertyDescriptor) -> None: ...
    
    @property
    def SortDirection(self) -> ListSortDirection: ...
    
    @SortDirection.setter
    def SortDirection(self, value: ListSortDirection) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_PropertyDescriptor(self) -> PropertyDescriptor: ...
    
    def get_SortDirection(self) -> ListSortDirection: ...
    
    def set_PropertyDescriptor(self, value: PropertyDescriptor) -> VoidType: ...
    
    def set_SortDirection(self, value: ListSortDirection) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ListSortDescriptionCollection(ObjectType, IList, ICollection, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, sorts: ArrayType[ListSortDescription]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    def __getitem__(self, key: IntType) -> ListSortDescription: ...
    
    def __setitem__(self, key: IntType, value: ListSortDescription) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Contains(self, value: ObjectType) -> BooleanType: ...
    
    def CopyTo(self, array: Array, index: IntType) -> VoidType: ...
    
    def IndexOf(self, value: ObjectType) -> IntType: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_Item(self, index: IntType) -> ListSortDescription: ...
    
    def set_Item(self, index: IntType, value: ListSortDescription) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class LocalizableAttribute(Attribute, _Attribute):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Default() -> LocalizableAttribute: ...
    
    @staticmethod
    @property
    def No() -> LocalizableAttribute: ...
    
    @staticmethod
    @property
    def Yes() -> LocalizableAttribute: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self, isLocalizable: BooleanType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def IsLocalizable(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def IsDefaultAttribute(self) -> BooleanType: ...
    
    def get_IsLocalizable(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class LookupBindingPropertiesAttribute(Attribute, _Attribute):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Default() -> LookupBindingPropertiesAttribute: ...
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, dataSource: StringType, displayMember: StringType, valueMember: StringType, lookupMember: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def DataSource(self) -> StringType: ...
    
    @property
    def DisplayMember(self) -> StringType: ...
    
    @property
    def LookupMember(self) -> StringType: ...
    
    @property
    def ValueMember(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def get_DataSource(self) -> StringType: ...
    
    def get_DisplayMember(self) -> StringType: ...
    
    def get_LookupMember(self) -> StringType: ...
    
    def get_ValueMember(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MarshalByValueComponent(ObjectType, IComponent, IDisposable, IServiceProvider):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Container(self) -> IContainer: ...
    
    @property
    def DesignMode(self) -> BooleanType: ...
    
    @property
    def Site(self) -> ISite: ...
    
    @Site.setter
    def Site(self, value: ISite) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Dispose(self) -> VoidType: ...
    
    def GetService(self, service: TypeType) -> ObjectType: ...
    
    def ToString(self) -> StringType: ...
    
    def add_Disposed(self, value: EventHandler) -> VoidType: ...
    
    def get_Container(self) -> IContainer: ...
    
    def get_DesignMode(self) -> BooleanType: ...
    
    def get_Site(self) -> ISite: ...
    
    def remove_Disposed(self, value: EventHandler) -> VoidType: ...
    
    def set_Site(self, value: ISite) -> VoidType: ...
    
    # ---------- Events ---------- #
    
    Disposed: EventType[EventHandler] = ...
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MaskedTextProvider(ObjectType, ICloneable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, mask: StringType): ...
    
    @overload
    def __init__(self, mask: StringType, restrictToAscii: BooleanType): ...
    
    @overload
    def __init__(self, mask: StringType, culture: CultureInfo): ...
    
    @overload
    def __init__(self, mask: StringType, culture: CultureInfo, restrictToAscii: BooleanType): ...
    
    @overload
    def __init__(self, mask: StringType, passwordChar: CharType, allowPromptAsInput: BooleanType): ...
    
    @overload
    def __init__(self, mask: StringType, culture: CultureInfo, passwordChar: CharType, allowPromptAsInput: BooleanType): ...
    
    @overload
    def __init__(self, mask: StringType, culture: CultureInfo, allowPromptAsInput: BooleanType, promptChar: CharType, passwordChar: CharType, restrictToAscii: BooleanType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AllowPromptAsInput(self) -> BooleanType: ...
    
    @property
    def AsciiOnly(self) -> BooleanType: ...
    
    @property
    def AssignedEditPositionCount(self) -> IntType: ...
    
    @property
    def AvailableEditPositionCount(self) -> IntType: ...
    
    @property
    def Culture(self) -> CultureInfo: ...
    
    @staticmethod
    @property
    def DefaultPasswordChar() -> CharType: ...
    
    @property
    def EditPositionCount(self) -> IntType: ...
    
    @property
    def EditPositions(self) -> IEnumerator: ...
    
    @property
    def IncludeLiterals(self) -> BooleanType: ...
    
    @IncludeLiterals.setter
    def IncludeLiterals(self, value: BooleanType) -> None: ...
    
    @property
    def IncludePrompt(self) -> BooleanType: ...
    
    @IncludePrompt.setter
    def IncludePrompt(self, value: BooleanType) -> None: ...
    
    @staticmethod
    @property
    def InvalidIndex() -> IntType: ...
    
    @property
    def IsPassword(self) -> BooleanType: ...
    
    @IsPassword.setter
    def IsPassword(self, value: BooleanType) -> None: ...
    
    def __getitem__(self, key: IntType) -> CharType: ...
    
    @property
    def LastAssignedPosition(self) -> IntType: ...
    
    @property
    def Length(self) -> IntType: ...
    
    @property
    def Mask(self) -> StringType: ...
    
    @property
    def MaskCompleted(self) -> BooleanType: ...
    
    @property
    def MaskFull(self) -> BooleanType: ...
    
    @property
    def PasswordChar(self) -> CharType: ...
    
    @PasswordChar.setter
    def PasswordChar(self, value: CharType) -> None: ...
    
    @property
    def PromptChar(self) -> CharType: ...
    
    @PromptChar.setter
    def PromptChar(self, value: CharType) -> None: ...
    
    @property
    def ResetOnPrompt(self) -> BooleanType: ...
    
    @ResetOnPrompt.setter
    def ResetOnPrompt(self, value: BooleanType) -> None: ...
    
    @property
    def ResetOnSpace(self) -> BooleanType: ...
    
    @ResetOnSpace.setter
    def ResetOnSpace(self, value: BooleanType) -> None: ...
    
    @property
    def SkipLiterals(self) -> BooleanType: ...
    
    @SkipLiterals.setter
    def SkipLiterals(self, value: BooleanType) -> None: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Add(self, input: CharType) -> BooleanType: ...
    
    @overload
    def Add(self, input: CharType, testPosition: IntType, resultHint: MaskedTextResultHint) -> Tuple[BooleanType, IntType, MaskedTextResultHint]: ...
    
    @overload
    def Add(self, input: StringType) -> BooleanType: ...
    
    @overload
    def Add(self, input: StringType, testPosition: IntType, resultHint: MaskedTextResultHint) -> Tuple[BooleanType, IntType, MaskedTextResultHint]: ...
    
    @overload
    def Clear(self) -> VoidType: ...
    
    @overload
    def Clear(self, resultHint: MaskedTextResultHint) -> Tuple[VoidType, MaskedTextResultHint]: ...
    
    def Clone(self) -> ObjectType: ...
    
    def FindAssignedEditPositionFrom(self, position: IntType, direction: BooleanType) -> IntType: ...
    
    def FindAssignedEditPositionInRange(self, startPosition: IntType, endPosition: IntType, direction: BooleanType) -> IntType: ...
    
    def FindEditPositionFrom(self, position: IntType, direction: BooleanType) -> IntType: ...
    
    def FindEditPositionInRange(self, startPosition: IntType, endPosition: IntType, direction: BooleanType) -> IntType: ...
    
    def FindNonEditPositionFrom(self, position: IntType, direction: BooleanType) -> IntType: ...
    
    def FindNonEditPositionInRange(self, startPosition: IntType, endPosition: IntType, direction: BooleanType) -> IntType: ...
    
    def FindUnassignedEditPositionFrom(self, position: IntType, direction: BooleanType) -> IntType: ...
    
    def FindUnassignedEditPositionInRange(self, startPosition: IntType, endPosition: IntType, direction: BooleanType) -> IntType: ...
    
    @staticmethod
    def GetOperationResultFromHint(hint: MaskedTextResultHint) -> BooleanType: ...
    
    @overload
    def InsertAt(self, input: CharType, position: IntType) -> BooleanType: ...
    
    @overload
    def InsertAt(self, input: CharType, position: IntType, testPosition: IntType, resultHint: MaskedTextResultHint) -> Tuple[BooleanType, IntType, MaskedTextResultHint]: ...
    
    @overload
    def InsertAt(self, input: StringType, position: IntType) -> BooleanType: ...
    
    @overload
    def InsertAt(self, input: StringType, position: IntType, testPosition: IntType, resultHint: MaskedTextResultHint) -> Tuple[BooleanType, IntType, MaskedTextResultHint]: ...
    
    def IsAvailablePosition(self, position: IntType) -> BooleanType: ...
    
    def IsEditPosition(self, position: IntType) -> BooleanType: ...
    
    @staticmethod
    def IsValidInputChar(c: CharType) -> BooleanType: ...
    
    @staticmethod
    def IsValidMaskChar(c: CharType) -> BooleanType: ...
    
    @staticmethod
    def IsValidPasswordChar(c: CharType) -> BooleanType: ...
    
    @overload
    def Remove(self) -> BooleanType: ...
    
    @overload
    def Remove(self, testPosition: IntType, resultHint: MaskedTextResultHint) -> Tuple[BooleanType, IntType, MaskedTextResultHint]: ...
    
    @overload
    def RemoveAt(self, position: IntType) -> BooleanType: ...
    
    @overload
    def RemoveAt(self, startPosition: IntType, endPosition: IntType) -> BooleanType: ...
    
    @overload
    def RemoveAt(self, startPosition: IntType, endPosition: IntType, testPosition: IntType, resultHint: MaskedTextResultHint) -> Tuple[BooleanType, IntType, MaskedTextResultHint]: ...
    
    @overload
    def Replace(self, input: CharType, position: IntType) -> BooleanType: ...
    
    @overload
    def Replace(self, input: CharType, position: IntType, testPosition: IntType, resultHint: MaskedTextResultHint) -> Tuple[BooleanType, IntType, MaskedTextResultHint]: ...
    
    @overload
    def Replace(self, input: CharType, startPosition: IntType, endPosition: IntType, testPosition: IntType, resultHint: MaskedTextResultHint) -> Tuple[BooleanType, IntType, MaskedTextResultHint]: ...
    
    @overload
    def Replace(self, input: StringType, position: IntType) -> BooleanType: ...
    
    @overload
    def Replace(self, input: StringType, position: IntType, testPosition: IntType, resultHint: MaskedTextResultHint) -> Tuple[BooleanType, IntType, MaskedTextResultHint]: ...
    
    @overload
    def Replace(self, input: StringType, startPosition: IntType, endPosition: IntType, testPosition: IntType, resultHint: MaskedTextResultHint) -> Tuple[BooleanType, IntType, MaskedTextResultHint]: ...
    
    @overload
    def Set(self, input: StringType) -> BooleanType: ...
    
    @overload
    def Set(self, input: StringType, testPosition: IntType, resultHint: MaskedTextResultHint) -> Tuple[BooleanType, IntType, MaskedTextResultHint]: ...
    
    def ToDisplayString(self) -> StringType: ...
    
    @overload
    def ToString(self) -> StringType: ...
    
    @overload
    def ToString(self, ignorePasswordChar: BooleanType) -> StringType: ...
    
    @overload
    def ToString(self, startPosition: IntType, length: IntType) -> StringType: ...
    
    @overload
    def ToString(self, ignorePasswordChar: BooleanType, startPosition: IntType, length: IntType) -> StringType: ...
    
    @overload
    def ToString(self, includePrompt: BooleanType, includeLiterals: BooleanType) -> StringType: ...
    
    @overload
    def ToString(self, includePrompt: BooleanType, includeLiterals: BooleanType, startPosition: IntType, length: IntType) -> StringType: ...
    
    @overload
    def ToString(self, ignorePasswordChar: BooleanType, includePrompt: BooleanType, includeLiterals: BooleanType, startPosition: IntType, length: IntType) -> StringType: ...
    
    def VerifyChar(self, input: CharType, position: IntType, hint: MaskedTextResultHint) -> Tuple[BooleanType, MaskedTextResultHint]: ...
    
    def VerifyEscapeChar(self, input: CharType, position: IntType) -> BooleanType: ...
    
    @overload
    def VerifyString(self, input: StringType) -> BooleanType: ...
    
    @overload
    def VerifyString(self, input: StringType, testPosition: IntType, resultHint: MaskedTextResultHint) -> Tuple[BooleanType, IntType, MaskedTextResultHint]: ...
    
    def get_AllowPromptAsInput(self) -> BooleanType: ...
    
    def get_AsciiOnly(self) -> BooleanType: ...
    
    def get_AssignedEditPositionCount(self) -> IntType: ...
    
    def get_AvailableEditPositionCount(self) -> IntType: ...
    
    def get_Culture(self) -> CultureInfo: ...
    
    @staticmethod
    def get_DefaultPasswordChar() -> CharType: ...
    
    def get_EditPositionCount(self) -> IntType: ...
    
    def get_EditPositions(self) -> IEnumerator: ...
    
    def get_IncludeLiterals(self) -> BooleanType: ...
    
    def get_IncludePrompt(self) -> BooleanType: ...
    
    @staticmethod
    def get_InvalidIndex() -> IntType: ...
    
    def get_IsPassword(self) -> BooleanType: ...
    
    def get_Item(self, index: IntType) -> CharType: ...
    
    def get_LastAssignedPosition(self) -> IntType: ...
    
    def get_Length(self) -> IntType: ...
    
    def get_Mask(self) -> StringType: ...
    
    def get_MaskCompleted(self) -> BooleanType: ...
    
    def get_MaskFull(self) -> BooleanType: ...
    
    def get_PasswordChar(self) -> CharType: ...
    
    def get_PromptChar(self) -> CharType: ...
    
    def get_ResetOnPrompt(self) -> BooleanType: ...
    
    def get_ResetOnSpace(self) -> BooleanType: ...
    
    def get_SkipLiterals(self) -> BooleanType: ...
    
    def set_IncludeLiterals(self, value: BooleanType) -> VoidType: ...
    
    def set_IncludePrompt(self, value: BooleanType) -> VoidType: ...
    
    def set_IsPassword(self, value: BooleanType) -> VoidType: ...
    
    def set_PasswordChar(self, value: CharType) -> VoidType: ...
    
    def set_PromptChar(self, value: CharType) -> VoidType: ...
    
    def set_ResetOnPrompt(self, value: BooleanType) -> VoidType: ...
    
    def set_ResetOnSpace(self, value: BooleanType) -> VoidType: ...
    
    def set_SkipLiterals(self, value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MemberDescriptor(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Attributes(self) -> AttributeCollection: ...
    
    @property
    def Category(self) -> StringType: ...
    
    @property
    def Description(self) -> StringType: ...
    
    @property
    def DesignTimeOnly(self) -> BooleanType: ...
    
    @property
    def DisplayName(self) -> StringType: ...
    
    @property
    def IsBrowsable(self) -> BooleanType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def get_Attributes(self) -> AttributeCollection: ...
    
    def get_Category(self) -> StringType: ...
    
    def get_Description(self) -> StringType: ...
    
    def get_DesignTimeOnly(self) -> BooleanType: ...
    
    def get_DisplayName(self) -> StringType: ...
    
    def get_IsBrowsable(self) -> BooleanType: ...
    
    def get_Name(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MergablePropertyAttribute(Attribute, _Attribute):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Default() -> MergablePropertyAttribute: ...
    
    @staticmethod
    @property
    def No() -> MergablePropertyAttribute: ...
    
    @staticmethod
    @property
    def Yes() -> MergablePropertyAttribute: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self, allowMerge: BooleanType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AllowMerge(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def IsDefaultAttribute(self) -> BooleanType: ...
    
    def get_AllowMerge(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MultilineStringConverter(TypeConverter):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def ConvertTo(self, context: ITypeDescriptorContext, culture: CultureInfo, value: ObjectType, destinationType: TypeType) -> ObjectType: ...
    
    @overload
    def GetProperties(self, context: ITypeDescriptorContext, value: ObjectType, attributes: ArrayType[Attribute]) -> PropertyDescriptorCollection: ...
    
    @overload
    def GetPropertiesSupported(self, context: ITypeDescriptorContext) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class NestedContainer(Container, IContainer, IDisposable, INestedContainer):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, owner: IComponent): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Owner(self) -> IComponent: ...
    
    # ---------- Methods ---------- #
    
    def get_Owner(self) -> IComponent: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class NotifyParentPropertyAttribute(Attribute, _Attribute):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Default() -> NotifyParentPropertyAttribute: ...
    
    @staticmethod
    @property
    def No() -> NotifyParentPropertyAttribute: ...
    
    @staticmethod
    @property
    def Yes() -> NotifyParentPropertyAttribute: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self, notifyParent: BooleanType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def NotifyParent(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def IsDefaultAttribute(self) -> BooleanType: ...
    
    def get_NotifyParent(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class NullableConverter(TypeConverter):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, type: TypeType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def NullableType(self) -> TypeType: ...
    
    @property
    def UnderlyingType(self) -> TypeType: ...
    
    @property
    def UnderlyingTypeConverter(self) -> TypeConverter: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: TypeType) -> BooleanType: ...
    
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, destinationType: TypeType) -> BooleanType: ...
    
    @overload
    def ConvertFrom(self, context: ITypeDescriptorContext, culture: CultureInfo, value: ObjectType) -> ObjectType: ...
    
    @overload
    def ConvertTo(self, context: ITypeDescriptorContext, culture: CultureInfo, value: ObjectType, destinationType: TypeType) -> ObjectType: ...
    
    @overload
    def CreateInstance(self, context: ITypeDescriptorContext, propertyValues: IDictionary) -> ObjectType: ...
    
    @overload
    def GetCreateInstanceSupported(self, context: ITypeDescriptorContext) -> BooleanType: ...
    
    @overload
    def GetProperties(self, context: ITypeDescriptorContext, value: ObjectType, attributes: ArrayType[Attribute]) -> PropertyDescriptorCollection: ...
    
    @overload
    def GetPropertiesSupported(self, context: ITypeDescriptorContext) -> BooleanType: ...
    
    @overload
    def GetStandardValues(self, context: ITypeDescriptorContext) -> StandardValuesCollection: ...
    
    @overload
    def GetStandardValuesExclusive(self, context: ITypeDescriptorContext) -> BooleanType: ...
    
    @overload
    def GetStandardValuesSupported(self, context: ITypeDescriptorContext) -> BooleanType: ...
    
    @overload
    def IsValid(self, context: ITypeDescriptorContext, value: ObjectType) -> BooleanType: ...
    
    def get_NullableType(self) -> TypeType: ...
    
    def get_UnderlyingType(self) -> TypeType: ...
    
    def get_UnderlyingTypeConverter(self) -> TypeConverter: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ParenthesizePropertyNameAttribute(Attribute, _Attribute):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Default() -> ParenthesizePropertyNameAttribute: ...
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, needParenthesis: BooleanType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def NeedParenthesis(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def IsDefaultAttribute(self) -> BooleanType: ...
    
    def get_NeedParenthesis(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PasswordPropertyTextAttribute(Attribute, _Attribute):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Default() -> PasswordPropertyTextAttribute: ...
    
    @staticmethod
    @property
    def No() -> PasswordPropertyTextAttribute: ...
    
    @staticmethod
    @property
    def Yes() -> PasswordPropertyTextAttribute: ...
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, password: BooleanType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Password(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def IsDefaultAttribute(self) -> BooleanType: ...
    
    def get_Password(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ProgressChangedEventArgs(EventArgs):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, progressPercentage: IntType, userState: ObjectType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ProgressPercentage(self) -> IntType: ...
    
    @property
    def UserState(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def get_ProgressPercentage(self) -> IntType: ...
    
    def get_UserState(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ProgressChangedEventHandler(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, sender: ObjectType, e: ProgressChangedEventArgs, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, sender: ObjectType, e: ProgressChangedEventArgs) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PropertyChangedEventArgs(EventArgs):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, propertyName: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def PropertyName(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_PropertyName(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PropertyChangedEventHandler(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, sender: ObjectType, e: PropertyChangedEventArgs, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, sender: ObjectType, e: PropertyChangedEventArgs) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PropertyChangingEventArgs(EventArgs):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, propertyName: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def PropertyName(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_PropertyName(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PropertyChangingEventHandler(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, sender: ObjectType, e: PropertyChangingEventArgs, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, sender: ObjectType, e: PropertyChangingEventArgs) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PropertyDescriptor(ABC, MemberDescriptor):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def ComponentType(self) -> TypeType: ...
    
    @property
    def Converter(self) -> TypeConverter: ...
    
    @property
    def IsLocalizable(self) -> BooleanType: ...
    
    @property
    def IsReadOnly(self) -> BooleanType: ...
    
    @property
    def PropertyType(self) -> TypeType: ...
    
    @property
    def SerializationVisibility(self) -> DesignerSerializationVisibility: ...
    
    @property
    def SupportsChangeEvents(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def AddValueChanged(self, component: ObjectType, handler: EventHandler) -> VoidType: ...
    
    def CanResetValue(self, component: ObjectType) -> BooleanType: ...
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @overload
    def GetChildProperties(self) -> PropertyDescriptorCollection: ...
    
    @overload
    def GetChildProperties(self, filter: ArrayType[Attribute]) -> PropertyDescriptorCollection: ...
    
    @overload
    def GetChildProperties(self, instance: ObjectType) -> PropertyDescriptorCollection: ...
    
    @overload
    def GetChildProperties(self, instance: ObjectType, filter: ArrayType[Attribute]) -> PropertyDescriptorCollection: ...
    
    def GetEditor(self, editorBaseType: TypeType) -> ObjectType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def GetValue(self, component: ObjectType) -> ObjectType: ...
    
    def RemoveValueChanged(self, component: ObjectType, handler: EventHandler) -> VoidType: ...
    
    def ResetValue(self, component: ObjectType) -> VoidType: ...
    
    def SetValue(self, component: ObjectType, value: ObjectType) -> VoidType: ...
    
    def ShouldSerializeValue(self, component: ObjectType) -> BooleanType: ...
    
    def get_ComponentType(self) -> TypeType: ...
    
    def get_Converter(self) -> TypeConverter: ...
    
    def get_IsLocalizable(self) -> BooleanType: ...
    
    def get_IsReadOnly(self) -> BooleanType: ...
    
    def get_PropertyType(self) -> TypeType: ...
    
    def get_SerializationVisibility(self) -> DesignerSerializationVisibility: ...
    
    def get_SupportsChangeEvents(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PropertyDescriptorCollection(ObjectType, ICollection, IEnumerable, IList, IDictionary):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Empty() -> PropertyDescriptorCollection: ...
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, properties: ArrayType[PropertyDescriptor]): ...
    
    @overload
    def __init__(self, properties: ArrayType[PropertyDescriptor], readOnly: BooleanType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    def __getitem__(self, key: IntType) -> PropertyDescriptor: ...
    
    def __getitem__(self, key: StringType) -> PropertyDescriptor: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, value: PropertyDescriptor) -> IntType: ...
    
    def Clear(self) -> VoidType: ...
    
    def Contains(self, value: PropertyDescriptor) -> BooleanType: ...
    
    def CopyTo(self, array: Array, index: IntType) -> VoidType: ...
    
    def Find(self, name: StringType, ignoreCase: BooleanType) -> PropertyDescriptor: ...
    
    def GetEnumerator(self) -> IEnumerator: ...
    
    def IndexOf(self, value: PropertyDescriptor) -> IntType: ...
    
    def Insert(self, index: IntType, value: PropertyDescriptor) -> VoidType: ...
    
    def Remove(self, value: PropertyDescriptor) -> VoidType: ...
    
    def RemoveAt(self, index: IntType) -> VoidType: ...
    
    @overload
    def Sort(self) -> PropertyDescriptorCollection: ...
    
    @overload
    def Sort(self, names: ArrayType[StringType]) -> PropertyDescriptorCollection: ...
    
    @overload
    def Sort(self, names: ArrayType[StringType], comparer: IComparer) -> PropertyDescriptorCollection: ...
    
    @overload
    def Sort(self, comparer: IComparer) -> PropertyDescriptorCollection: ...
    
    def get_Count(self) -> IntType: ...
    
    @overload
    def get_Item(self, index: IntType) -> PropertyDescriptor: ...
    
    @overload
    def get_Item(self, name: StringType) -> PropertyDescriptor: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PropertyTabAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, tabClass: TypeType): ...
    
    @overload
    def __init__(self, tabClassName: StringType): ...
    
    @overload
    def __init__(self, tabClass: TypeType, tabScope: PropertyTabScope): ...
    
    @overload
    def __init__(self, tabClassName: StringType, tabScope: PropertyTabScope): ...
    
    # ---------- Properties ---------- #
    
    @property
    def TabClasses(self) -> ArrayType[TypeType]: ...
    
    @property
    def TabScopes(self) -> ArrayType[PropertyTabScope]: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Equals(self, other: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, other: PropertyTabAttribute) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def get_TabClasses(self) -> ArrayType[TypeType]: ...
    
    def get_TabScopes(self) -> ArrayType[PropertyTabScope]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ProvidePropertyAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, propertyName: StringType, receiverType: TypeType): ...
    
    @overload
    def __init__(self, propertyName: StringType, receiverTypeName: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def PropertyName(self) -> StringType: ...
    
    @property
    def ReceiverTypeName(self) -> StringType: ...
    
    @property
    def TypeId(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def get_PropertyName(self) -> StringType: ...
    
    def get_ReceiverTypeName(self) -> StringType: ...
    
    def get_TypeId(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ReadOnlyAttribute(Attribute, _Attribute):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Default() -> ReadOnlyAttribute: ...
    
    @staticmethod
    @property
    def No() -> ReadOnlyAttribute: ...
    
    @staticmethod
    @property
    def Yes() -> ReadOnlyAttribute: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self, isReadOnly: BooleanType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def IsReadOnly(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, value: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def IsDefaultAttribute(self) -> BooleanType: ...
    
    def get_IsReadOnly(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RecommendedAsConfigurableAttribute(Attribute, _Attribute):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Default() -> RecommendedAsConfigurableAttribute: ...
    
    @staticmethod
    @property
    def No() -> RecommendedAsConfigurableAttribute: ...
    
    @staticmethod
    @property
    def Yes() -> RecommendedAsConfigurableAttribute: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self, recommendedAsConfigurable: BooleanType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def RecommendedAsConfigurable(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def IsDefaultAttribute(self) -> BooleanType: ...
    
    def get_RecommendedAsConfigurable(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ReferenceConverter(TypeConverter):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, type: TypeType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: TypeType) -> BooleanType: ...
    
    @overload
    def ConvertFrom(self, context: ITypeDescriptorContext, culture: CultureInfo, value: ObjectType) -> ObjectType: ...
    
    @overload
    def ConvertTo(self, context: ITypeDescriptorContext, culture: CultureInfo, value: ObjectType, destinationType: TypeType) -> ObjectType: ...
    
    @overload
    def GetStandardValues(self, context: ITypeDescriptorContext) -> StandardValuesCollection: ...
    
    @overload
    def GetStandardValuesExclusive(self, context: ITypeDescriptorContext) -> BooleanType: ...
    
    @overload
    def GetStandardValuesSupported(self, context: ITypeDescriptorContext) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ReflectEventDescriptor(EventDescriptor):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, componentClass: TypeType, name: StringType, type: TypeType, attributes: ArrayType[Attribute]): ...
    
    @overload
    def __init__(self, componentClass: TypeType, eventInfo: EventInfo): ...
    
    @overload
    def __init__(self, componentType: TypeType, oldReflectEventDescriptor: EventDescriptor, attributes: ArrayType[Attribute]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ComponentType(self) -> TypeType: ...
    
    @property
    def EventType(self) -> TypeType: ...
    
    @property
    def IsMulticast(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def AddEventHandler(self, component: ObjectType, value: Delegate) -> VoidType: ...
    
    def RemoveEventHandler(self, component: ObjectType, value: Delegate) -> VoidType: ...
    
    def get_ComponentType(self) -> TypeType: ...
    
    def get_EventType(self) -> TypeType: ...
    
    def get_IsMulticast(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ReflectPropertyDescriptor(PropertyDescriptor):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, componentClass: TypeType, name: StringType, type: TypeType, attributes: ArrayType[Attribute]): ...
    
    @overload
    def __init__(self, componentClass: TypeType, name: StringType, type: TypeType, propInfo: PropertyInfo, getMethod: MethodInfo, setMethod: MethodInfo, attrs: ArrayType[Attribute]): ...
    
    @overload
    def __init__(self, componentClass: TypeType, name: StringType, type: TypeType, receiverType: TypeType, getMethod: MethodInfo, setMethod: MethodInfo, attrs: ArrayType[Attribute]): ...
    
    @overload
    def __init__(self, componentClass: TypeType, oldReflectPropertyDescriptor: PropertyDescriptor, attributes: ArrayType[Attribute]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ComponentType(self) -> TypeType: ...
    
    @property
    def IsReadOnly(self) -> BooleanType: ...
    
    @property
    def PropertyType(self) -> TypeType: ...
    
    @property
    def SupportsChangeEvents(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def AddValueChanged(self, component: ObjectType, handler: EventHandler) -> VoidType: ...
    
    def CanResetValue(self, component: ObjectType) -> BooleanType: ...
    
    def GetValue(self, component: ObjectType) -> ObjectType: ...
    
    def RemoveValueChanged(self, component: ObjectType, handler: EventHandler) -> VoidType: ...
    
    def ResetValue(self, component: ObjectType) -> VoidType: ...
    
    def SetValue(self, component: ObjectType, value: ObjectType) -> VoidType: ...
    
    def ShouldSerializeValue(self, component: ObjectType) -> BooleanType: ...
    
    def get_ComponentType(self) -> TypeType: ...
    
    def get_IsReadOnly(self) -> BooleanType: ...
    
    def get_PropertyType(self) -> TypeType: ...
    
    def get_SupportsChangeEvents(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ReflectTypeDescriptionProvider(TypeDescriptionProvider):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def CreateInstance(self, provider: IServiceProvider, objectType: TypeType, argTypes: ArrayType[TypeType], args: ArrayType[ObjectType]) -> ObjectType: ...
    
    def GetCache(self, instance: ObjectType) -> IDictionary: ...
    
    def GetExtendedTypeDescriptor(self, instance: ObjectType) -> ICustomTypeDescriptor: ...
    
    def GetFullComponentName(self, component: ObjectType) -> StringType: ...
    
    @overload
    def GetReflectionType(self, objectType: TypeType, instance: ObjectType) -> TypeType: ...
    
    @overload
    def GetTypeDescriptor(self, objectType: TypeType, instance: ObjectType) -> ICustomTypeDescriptor: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RefreshEventArgs(EventArgs):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, componentChanged: ObjectType): ...
    
    @overload
    def __init__(self, typeChanged: TypeType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ComponentChanged(self) -> ObjectType: ...
    
    @property
    def TypeChanged(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def get_ComponentChanged(self) -> ObjectType: ...
    
    def get_TypeChanged(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RefreshEventHandler(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, e: RefreshEventArgs, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, e: RefreshEventArgs) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RefreshPropertiesAttribute(Attribute, _Attribute):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def All() -> RefreshPropertiesAttribute: ...
    
    @staticmethod
    @property
    def Default() -> RefreshPropertiesAttribute: ...
    
    @staticmethod
    @property
    def Repaint() -> RefreshPropertiesAttribute: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self, refresh: RefreshProperties): ...
    
    # ---------- Properties ---------- #
    
    @property
    def RefreshProperties(self) -> RefreshProperties: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, value: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def IsDefaultAttribute(self) -> BooleanType: ...
    
    def get_RefreshProperties(self) -> RefreshProperties: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RunInstallerAttribute(Attribute, _Attribute):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Default() -> RunInstallerAttribute: ...
    
    @staticmethod
    @property
    def No() -> RunInstallerAttribute: ...
    
    @staticmethod
    @property
    def Yes() -> RunInstallerAttribute: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self, runInstaller: BooleanType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def RunInstaller(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def IsDefaultAttribute(self) -> BooleanType: ...
    
    def get_RunInstaller(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RunWorkerCompletedEventArgs(AsyncCompletedEventArgs):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, result: ObjectType, error: Exception, cancelled: BooleanType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Result(self) -> ObjectType: ...
    
    @property
    def UserState(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def get_Result(self) -> ObjectType: ...
    
    @overload
    def get_UserState(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RunWorkerCompletedEventHandler(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, sender: ObjectType, e: RunWorkerCompletedEventArgs, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, sender: ObjectType, e: RunWorkerCompletedEventArgs) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SByteConverter(BaseNumberConverter):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SettingsBindableAttribute(Attribute, _Attribute):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def No() -> SettingsBindableAttribute: ...
    
    @staticmethod
    @property
    def Yes() -> SettingsBindableAttribute: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self, bindable: BooleanType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Bindable(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def get_Bindable(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SingleConverter(BaseNumberConverter):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class StringConverter(TypeConverter):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: TypeType) -> BooleanType: ...
    
    @overload
    def ConvertFrom(self, context: ITypeDescriptorContext, culture: CultureInfo, value: ObjectType) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SyntaxCheck(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def CheckMachineName(value: StringType) -> BooleanType: ...
    
    @staticmethod
    def CheckPath(value: StringType) -> BooleanType: ...
    
    @staticmethod
    def CheckRootedPath(value: StringType) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TimeSpanConverter(TypeConverter):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: TypeType) -> BooleanType: ...
    
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, destinationType: TypeType) -> BooleanType: ...
    
    @overload
    def ConvertFrom(self, context: ITypeDescriptorContext, culture: CultureInfo, value: ObjectType) -> ObjectType: ...
    
    @overload
    def ConvertTo(self, context: ITypeDescriptorContext, culture: CultureInfo, value: ObjectType, destinationType: TypeType) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ToolboxItemAttribute(Attribute, _Attribute):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Default() -> ToolboxItemAttribute: ...
    
    @staticmethod
    @property
    def _None() -> ToolboxItemAttribute: ...
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, defaultType: BooleanType): ...
    
    @overload
    def __init__(self, toolboxItemTypeName: StringType): ...
    
    @overload
    def __init__(self, toolboxItemType: TypeType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ToolboxItemType(self) -> TypeType: ...
    
    @property
    def ToolboxItemTypeName(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def IsDefaultAttribute(self) -> BooleanType: ...
    
    def get_ToolboxItemType(self) -> TypeType: ...
    
    def get_ToolboxItemTypeName(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ToolboxItemFilterAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, filterString: StringType): ...
    
    @overload
    def __init__(self, filterString: StringType, filterType: ToolboxItemFilterType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def FilterString(self) -> StringType: ...
    
    @property
    def FilterType(self) -> ToolboxItemFilterType: ...
    
    @property
    def TypeId(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def Match(self, obj: ObjectType) -> BooleanType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_FilterString(self) -> StringType: ...
    
    def get_FilterType(self) -> ToolboxItemFilterType: ...
    
    def get_TypeId(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TypeConverter(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def CanConvertFrom(self, sourceType: TypeType) -> BooleanType: ...
    
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: TypeType) -> BooleanType: ...
    
    @overload
    def CanConvertTo(self, destinationType: TypeType) -> BooleanType: ...
    
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, destinationType: TypeType) -> BooleanType: ...
    
    @overload
    def ConvertFrom(self, value: ObjectType) -> ObjectType: ...
    
    @overload
    def ConvertFrom(self, context: ITypeDescriptorContext, culture: CultureInfo, value: ObjectType) -> ObjectType: ...
    
    @overload
    def ConvertFromInvariantString(self, text: StringType) -> ObjectType: ...
    
    @overload
    def ConvertFromInvariantString(self, context: ITypeDescriptorContext, text: StringType) -> ObjectType: ...
    
    @overload
    def ConvertFromString(self, text: StringType) -> ObjectType: ...
    
    @overload
    def ConvertFromString(self, context: ITypeDescriptorContext, text: StringType) -> ObjectType: ...
    
    @overload
    def ConvertFromString(self, context: ITypeDescriptorContext, culture: CultureInfo, text: StringType) -> ObjectType: ...
    
    @overload
    def ConvertTo(self, value: ObjectType, destinationType: TypeType) -> ObjectType: ...
    
    @overload
    def ConvertTo(self, context: ITypeDescriptorContext, culture: CultureInfo, value: ObjectType, destinationType: TypeType) -> ObjectType: ...
    
    @overload
    def ConvertToInvariantString(self, value: ObjectType) -> StringType: ...
    
    @overload
    def ConvertToInvariantString(self, context: ITypeDescriptorContext, value: ObjectType) -> StringType: ...
    
    @overload
    def ConvertToString(self, value: ObjectType) -> StringType: ...
    
    @overload
    def ConvertToString(self, context: ITypeDescriptorContext, value: ObjectType) -> StringType: ...
    
    @overload
    def ConvertToString(self, context: ITypeDescriptorContext, culture: CultureInfo, value: ObjectType) -> StringType: ...
    
    @overload
    def CreateInstance(self, propertyValues: IDictionary) -> ObjectType: ...
    
    @overload
    def CreateInstance(self, context: ITypeDescriptorContext, propertyValues: IDictionary) -> ObjectType: ...
    
    @overload
    def GetCreateInstanceSupported(self) -> BooleanType: ...
    
    @overload
    def GetCreateInstanceSupported(self, context: ITypeDescriptorContext) -> BooleanType: ...
    
    @overload
    def GetProperties(self, value: ObjectType) -> PropertyDescriptorCollection: ...
    
    @overload
    def GetProperties(self, context: ITypeDescriptorContext, value: ObjectType, attributes: ArrayType[Attribute]) -> PropertyDescriptorCollection: ...
    
    @overload
    def GetProperties(self, context: ITypeDescriptorContext, value: ObjectType) -> PropertyDescriptorCollection: ...
    
    @overload
    def GetPropertiesSupported(self) -> BooleanType: ...
    
    @overload
    def GetPropertiesSupported(self, context: ITypeDescriptorContext) -> BooleanType: ...
    
    @overload
    def GetStandardValues(self) -> ICollection: ...
    
    @overload
    def GetStandardValues(self, context: ITypeDescriptorContext) -> StandardValuesCollection: ...
    
    @overload
    def GetStandardValuesExclusive(self) -> BooleanType: ...
    
    @overload
    def GetStandardValuesExclusive(self, context: ITypeDescriptorContext) -> BooleanType: ...
    
    @overload
    def GetStandardValuesSupported(self) -> BooleanType: ...
    
    @overload
    def GetStandardValuesSupported(self, context: ITypeDescriptorContext) -> BooleanType: ...
    
    @overload
    def IsValid(self, value: ObjectType) -> BooleanType: ...
    
    @overload
    def IsValid(self, context: ITypeDescriptorContext, value: ObjectType) -> BooleanType: ...
    
    # No Events
    
    
    # ---------- Sub Classes ---------- #
    
    class StandardValuesCollection(ObjectType, ICollection, IEnumerable):
        # No Fields
        
        # ---------- Constructors ---------- #
        
        def __init__(self, values: ICollection): ...
        
        # ---------- Properties ---------- #
        
        @property
        def Count(self) -> IntType: ...
        
        def __getitem__(self, key: IntType) -> ObjectType: ...
        
        # ---------- Methods ---------- #
        
        def CopyTo(self, array: Array, index: IntType) -> VoidType: ...
        
        def GetEnumerator(self) -> IEnumerator: ...
        
        def get_Count(self) -> IntType: ...
        
        def get_Item(self, index: IntType) -> ObjectType: ...
        
        # No Events
        
        # No Sub Classes
        
        # No Sub Structs
        
        # No Sub Interfaces
        
        # No Sub Enums
    
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TypeConverterAttribute(Attribute, _Attribute):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Default() -> TypeConverterAttribute: ...
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, type: TypeType): ...
    
    @overload
    def __init__(self, typeName: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ConverterTypeName(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def get_ConverterTypeName(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TypeDescriptionProvider(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def CreateInstance(self, provider: IServiceProvider, objectType: TypeType, argTypes: ArrayType[TypeType], args: ArrayType[ObjectType]) -> ObjectType: ...
    
    def GetCache(self, instance: ObjectType) -> IDictionary: ...
    
    def GetExtendedTypeDescriptor(self, instance: ObjectType) -> ICustomTypeDescriptor: ...
    
    def GetFullComponentName(self, component: ObjectType) -> StringType: ...
    
    @overload
    def GetReflectionType(self, objectType: TypeType) -> TypeType: ...
    
    @overload
    def GetReflectionType(self, instance: ObjectType) -> TypeType: ...
    
    @overload
    def GetReflectionType(self, objectType: TypeType, instance: ObjectType) -> TypeType: ...
    
    def GetRuntimeType(self, reflectionType: TypeType) -> TypeType: ...
    
    @overload
    def GetTypeDescriptor(self, objectType: TypeType, instance: ObjectType) -> ICustomTypeDescriptor: ...
    
    @overload
    def GetTypeDescriptor(self, objectType: TypeType) -> ICustomTypeDescriptor: ...
    
    @overload
    def GetTypeDescriptor(self, instance: ObjectType) -> ICustomTypeDescriptor: ...
    
    def IsSupportedType(self, type: TypeType) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TypeDescriptionProviderAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, typeName: StringType): ...
    
    @overload
    def __init__(self, type: TypeType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def TypeName(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_TypeName(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TypeDescriptor(ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def ComNativeDescriptorHandler() -> IComNativeDescriptorHandler: ...
    
    @staticmethod
    @ComNativeDescriptorHandler.setter
    def ComNativeDescriptorHandler(value: IComNativeDescriptorHandler) -> None: ...
    
    @staticmethod
    @property
    def ComObjectType() -> TypeType: ...
    
    @staticmethod
    @property
    def InterfaceType() -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    @overload
    def AddAttributes(type: TypeType, attributes: ArrayType[Attribute]) -> TypeDescriptionProvider: ...
    
    @staticmethod
    @overload
    def AddAttributes(instance: ObjectType, attributes: ArrayType[Attribute]) -> TypeDescriptionProvider: ...
    
    @staticmethod
    def AddEditorTable(editorBaseType: TypeType, table: Hashtable) -> VoidType: ...
    
    @staticmethod
    @overload
    def AddProvider(provider: TypeDescriptionProvider, type: TypeType) -> VoidType: ...
    
    @staticmethod
    @overload
    def AddProvider(provider: TypeDescriptionProvider, instance: ObjectType) -> VoidType: ...
    
    @staticmethod
    @overload
    def AddProviderTransparent(provider: TypeDescriptionProvider, type: TypeType) -> VoidType: ...
    
    @staticmethod
    @overload
    def AddProviderTransparent(provider: TypeDescriptionProvider, instance: ObjectType) -> VoidType: ...
    
    @staticmethod
    def CreateAssociation(primary: ObjectType, secondary: ObjectType) -> VoidType: ...
    
    @staticmethod
    def CreateDesigner(component: IComponent, designerBaseType: TypeType) -> IDesigner: ...
    
    @staticmethod
    @overload
    def CreateEvent(componentType: TypeType, name: StringType, type: TypeType, attributes: ArrayType[Attribute]) -> EventDescriptor: ...
    
    @staticmethod
    @overload
    def CreateEvent(componentType: TypeType, oldEventDescriptor: EventDescriptor, attributes: ArrayType[Attribute]) -> EventDescriptor: ...
    
    @staticmethod
    def CreateInstance(provider: IServiceProvider, objectType: TypeType, argTypes: ArrayType[TypeType], args: ArrayType[ObjectType]) -> ObjectType: ...
    
    @staticmethod
    @overload
    def CreateProperty(componentType: TypeType, name: StringType, type: TypeType, attributes: ArrayType[Attribute]) -> PropertyDescriptor: ...
    
    @staticmethod
    @overload
    def CreateProperty(componentType: TypeType, oldPropertyDescriptor: PropertyDescriptor, attributes: ArrayType[Attribute]) -> PropertyDescriptor: ...
    
    @staticmethod
    def GetAssociation(type: TypeType, primary: ObjectType) -> ObjectType: ...
    
    @staticmethod
    @overload
    def GetAttributes(component: ObjectType) -> AttributeCollection: ...
    
    @staticmethod
    @overload
    def GetAttributes(componentType: TypeType) -> AttributeCollection: ...
    
    @staticmethod
    @overload
    def GetAttributes(component: ObjectType, noCustomTypeDesc: BooleanType) -> AttributeCollection: ...
    
    @staticmethod
    @overload
    def GetClassName(component: ObjectType) -> StringType: ...
    
    @staticmethod
    @overload
    def GetClassName(component: ObjectType, noCustomTypeDesc: BooleanType) -> StringType: ...
    
    @staticmethod
    @overload
    def GetClassName(componentType: TypeType) -> StringType: ...
    
    @staticmethod
    @overload
    def GetComponentName(component: ObjectType) -> StringType: ...
    
    @staticmethod
    @overload
    def GetComponentName(component: ObjectType, noCustomTypeDesc: BooleanType) -> StringType: ...
    
    @staticmethod
    @overload
    def GetConverter(component: ObjectType) -> TypeConverter: ...
    
    @staticmethod
    @overload
    def GetConverter(component: ObjectType, noCustomTypeDesc: BooleanType) -> TypeConverter: ...
    
    @staticmethod
    @overload
    def GetConverter(type: TypeType) -> TypeConverter: ...
    
    @staticmethod
    @overload
    def GetDefaultEvent(component: ObjectType) -> EventDescriptor: ...
    
    @staticmethod
    @overload
    def GetDefaultEvent(component: ObjectType, noCustomTypeDesc: BooleanType) -> EventDescriptor: ...
    
    @staticmethod
    @overload
    def GetDefaultEvent(componentType: TypeType) -> EventDescriptor: ...
    
    @staticmethod
    @overload
    def GetDefaultProperty(component: ObjectType) -> PropertyDescriptor: ...
    
    @staticmethod
    @overload
    def GetDefaultProperty(component: ObjectType, noCustomTypeDesc: BooleanType) -> PropertyDescriptor: ...
    
    @staticmethod
    @overload
    def GetDefaultProperty(componentType: TypeType) -> PropertyDescriptor: ...
    
    @staticmethod
    @overload
    def GetEditor(component: ObjectType, editorBaseType: TypeType) -> ObjectType: ...
    
    @staticmethod
    @overload
    def GetEditor(component: ObjectType, editorBaseType: TypeType, noCustomTypeDesc: BooleanType) -> ObjectType: ...
    
    @staticmethod
    @overload
    def GetEditor(type: TypeType, editorBaseType: TypeType) -> ObjectType: ...
    
    @staticmethod
    @overload
    def GetEvents(component: ObjectType) -> EventDescriptorCollection: ...
    
    @staticmethod
    @overload
    def GetEvents(component: ObjectType, noCustomTypeDesc: BooleanType) -> EventDescriptorCollection: ...
    
    @staticmethod
    @overload
    def GetEvents(component: ObjectType, attributes: ArrayType[Attribute]) -> EventDescriptorCollection: ...
    
    @staticmethod
    @overload
    def GetEvents(componentType: TypeType, attributes: ArrayType[Attribute]) -> EventDescriptorCollection: ...
    
    @staticmethod
    @overload
    def GetEvents(component: ObjectType, attributes: ArrayType[Attribute], noCustomTypeDesc: BooleanType) -> EventDescriptorCollection: ...
    
    @staticmethod
    @overload
    def GetEvents(componentType: TypeType) -> EventDescriptorCollection: ...
    
    @staticmethod
    def GetFullComponentName(component: ObjectType) -> StringType: ...
    
    @staticmethod
    @overload
    def GetProperties(component: ObjectType) -> PropertyDescriptorCollection: ...
    
    @staticmethod
    @overload
    def GetProperties(component: ObjectType, noCustomTypeDesc: BooleanType) -> PropertyDescriptorCollection: ...
    
    @staticmethod
    @overload
    def GetProperties(component: ObjectType, attributes: ArrayType[Attribute]) -> PropertyDescriptorCollection: ...
    
    @staticmethod
    @overload
    def GetProperties(component: ObjectType, attributes: ArrayType[Attribute], noCustomTypeDesc: BooleanType) -> PropertyDescriptorCollection: ...
    
    @staticmethod
    @overload
    def GetProperties(componentType: TypeType, attributes: ArrayType[Attribute]) -> PropertyDescriptorCollection: ...
    
    @staticmethod
    @overload
    def GetProperties(componentType: TypeType) -> PropertyDescriptorCollection: ...
    
    @staticmethod
    @overload
    def GetProvider(type: TypeType) -> TypeDescriptionProvider: ...
    
    @staticmethod
    @overload
    def GetProvider(instance: ObjectType) -> TypeDescriptionProvider: ...
    
    @staticmethod
    @overload
    def GetReflectionType(type: TypeType) -> TypeType: ...
    
    @staticmethod
    @overload
    def GetReflectionType(instance: ObjectType) -> TypeType: ...
    
    @staticmethod
    @overload
    def Refresh(component: ObjectType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Refresh(type: TypeType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Refresh(module: Module) -> VoidType: ...
    
    @staticmethod
    @overload
    def Refresh(assembly: Assembly) -> VoidType: ...
    
    @staticmethod
    def RemoveAssociation(primary: ObjectType, secondary: ObjectType) -> VoidType: ...
    
    @staticmethod
    def RemoveAssociations(primary: ObjectType) -> VoidType: ...
    
    @staticmethod
    @overload
    def RemoveProvider(provider: TypeDescriptionProvider, type: TypeType) -> VoidType: ...
    
    @staticmethod
    @overload
    def RemoveProvider(provider: TypeDescriptionProvider, instance: ObjectType) -> VoidType: ...
    
    @staticmethod
    @overload
    def RemoveProviderTransparent(provider: TypeDescriptionProvider, type: TypeType) -> VoidType: ...
    
    @staticmethod
    @overload
    def RemoveProviderTransparent(provider: TypeDescriptionProvider, instance: ObjectType) -> VoidType: ...
    
    @staticmethod
    def SortDescriptorArray(infos: IList) -> VoidType: ...
    
    @staticmethod
    def add_Refreshed(value: RefreshEventHandler) -> VoidType: ...
    
    @staticmethod
    def get_ComNativeDescriptorHandler() -> IComNativeDescriptorHandler: ...
    
    @staticmethod
    def get_ComObjectType() -> TypeType: ...
    
    @staticmethod
    def get_InterfaceType() -> TypeType: ...
    
    @staticmethod
    def remove_Refreshed(value: RefreshEventHandler) -> VoidType: ...
    
    @staticmethod
    def set_ComNativeDescriptorHandler(value: IComNativeDescriptorHandler) -> VoidType: ...
    
    # ---------- Events ---------- #
    
    Refreshed: EventType[RefreshEventHandler] = ...
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TypeListConverter(ABC, TypeConverter):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: TypeType) -> BooleanType: ...
    
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, destinationType: TypeType) -> BooleanType: ...
    
    @overload
    def ConvertFrom(self, context: ITypeDescriptorContext, culture: CultureInfo, value: ObjectType) -> ObjectType: ...
    
    @overload
    def ConvertTo(self, context: ITypeDescriptorContext, culture: CultureInfo, value: ObjectType, destinationType: TypeType) -> ObjectType: ...
    
    @overload
    def GetStandardValues(self, context: ITypeDescriptorContext) -> StandardValuesCollection: ...
    
    @overload
    def GetStandardValuesExclusive(self, context: ITypeDescriptorContext) -> BooleanType: ...
    
    @overload
    def GetStandardValuesSupported(self, context: ITypeDescriptorContext) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UInt16Converter(BaseNumberConverter):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UInt32Converter(BaseNumberConverter):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UInt64Converter(BaseNumberConverter):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class WarningException(SystemException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, helpUrl: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    @overload
    def __init__(self, message: StringType, helpUrl: StringType, helpTopic: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def HelpTopic(self) -> StringType: ...
    
    @property
    def HelpUrl(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    
    def get_HelpTopic(self) -> StringType: ...
    
    def get_HelpUrl(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class WeakHashtable(Hashtable, IDictionary, ICollection, IEnumerable, ISerializable, IDeserializationCallback, ICloneable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Clear(self) -> VoidType: ...
    
    def Remove(self, key: ObjectType) -> VoidType: ...
    
    def SetWeak(self, key: ObjectType, value: ObjectType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Win32Exception(ExternalException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, error: IntType): ...
    
    @overload
    def __init__(self, error: IntType, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    # ---------- Properties ---------- #
    
    @property
    def NativeErrorCode(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    
    def get_NativeErrorCode(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# No Structs

# ---------- Interfaces ---------- #

class IBindingList(Protocol, IList, ICollection, IEnumerable):
    # ---------- Properties ---------- #
    
    @property
    def AllowEdit(self) -> BooleanType: ...
    
    @property
    def AllowNew(self) -> BooleanType: ...
    
    @property
    def AllowRemove(self) -> BooleanType: ...
    
    @property
    def IsSorted(self) -> BooleanType: ...
    
    @property
    def SortDirection(self) -> ListSortDirection: ...
    
    @property
    def SortProperty(self) -> PropertyDescriptor: ...
    
    @property
    def SupportsChangeNotification(self) -> BooleanType: ...
    
    @property
    def SupportsSearching(self) -> BooleanType: ...
    
    @property
    def SupportsSorting(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def AddIndex(self, property: PropertyDescriptor) -> VoidType: ...
    
    def AddNew(self) -> ObjectType: ...
    
    def ApplySort(self, property: PropertyDescriptor, direction: ListSortDirection) -> VoidType: ...
    
    def Find(self, property: PropertyDescriptor, key: ObjectType) -> IntType: ...
    
    def RemoveIndex(self, property: PropertyDescriptor) -> VoidType: ...
    
    def RemoveSort(self) -> VoidType: ...
    
    def add_ListChanged(self, value: ListChangedEventHandler) -> VoidType: ...
    
    def get_AllowEdit(self) -> BooleanType: ...
    
    def get_AllowNew(self) -> BooleanType: ...
    
    def get_AllowRemove(self) -> BooleanType: ...
    
    def get_IsSorted(self) -> BooleanType: ...
    
    def get_SortDirection(self) -> ListSortDirection: ...
    
    def get_SortProperty(self) -> PropertyDescriptor: ...
    
    def get_SupportsChangeNotification(self) -> BooleanType: ...
    
    def get_SupportsSearching(self) -> BooleanType: ...
    
    def get_SupportsSorting(self) -> BooleanType: ...
    
    def remove_ListChanged(self, value: ListChangedEventHandler) -> VoidType: ...
    
    # ---------- Events ---------- #
    
    ListChanged: EventType[ListChangedEventHandler] = ...


class IBindingListView(Protocol, IBindingList, IList, ICollection, IEnumerable):
    # ---------- Properties ---------- #
    
    @property
    def Filter(self) -> StringType: ...
    
    @Filter.setter
    def Filter(self, value: StringType) -> None: ...
    
    @property
    def SortDescriptions(self) -> ListSortDescriptionCollection: ...
    
    @property
    def SupportsAdvancedSorting(self) -> BooleanType: ...
    
    @property
    def SupportsFiltering(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def ApplySort(self, sorts: ListSortDescriptionCollection) -> VoidType: ...
    
    def RemoveFilter(self) -> VoidType: ...
    
    def get_Filter(self) -> StringType: ...
    
    def get_SortDescriptions(self) -> ListSortDescriptionCollection: ...
    
    def get_SupportsAdvancedSorting(self) -> BooleanType: ...
    
    def get_SupportsFiltering(self) -> BooleanType: ...
    
    def set_Filter(self, value: StringType) -> VoidType: ...
    
    # No Events


class ICancelAddNew(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def CancelNew(self, itemIndex: IntType) -> VoidType: ...
    
    def EndNew(self, itemIndex: IntType) -> VoidType: ...
    
    # No Events


class IChangeTracking(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def IsChanged(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def AcceptChanges(self) -> VoidType: ...
    
    def get_IsChanged(self) -> BooleanType: ...
    
    # No Events


class IComNativeDescriptorHandler(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetAttributes(self, component: ObjectType) -> AttributeCollection: ...
    
    def GetClassName(self, component: ObjectType) -> StringType: ...
    
    def GetConverter(self, component: ObjectType) -> TypeConverter: ...
    
    def GetDefaultEvent(self, component: ObjectType) -> EventDescriptor: ...
    
    def GetDefaultProperty(self, component: ObjectType) -> PropertyDescriptor: ...
    
    def GetEditor(self, component: ObjectType, baseEditorType: TypeType) -> ObjectType: ...
    
    @overload
    def GetEvents(self, component: ObjectType) -> EventDescriptorCollection: ...
    
    @overload
    def GetEvents(self, component: ObjectType, attributes: ArrayType[Attribute]) -> EventDescriptorCollection: ...
    
    def GetName(self, component: ObjectType) -> StringType: ...
    
    def GetProperties(self, component: ObjectType, attributes: ArrayType[Attribute]) -> PropertyDescriptorCollection: ...
    
    @overload
    def GetPropertyValue(self, component: ObjectType, propertyName: StringType, success: BooleanType) -> Tuple[ObjectType, BooleanType]: ...
    
    @overload
    def GetPropertyValue(self, component: ObjectType, dispid: IntType, success: BooleanType) -> Tuple[ObjectType, BooleanType]: ...
    
    # No Events


class IComponent(Protocol, IDisposable):
    # ---------- Properties ---------- #
    
    @property
    def Site(self) -> ISite: ...
    
    @Site.setter
    def Site(self, value: ISite) -> None: ...
    
    # ---------- Methods ---------- #
    
    def add_Disposed(self, value: EventHandler) -> VoidType: ...
    
    def get_Site(self) -> ISite: ...
    
    def remove_Disposed(self, value: EventHandler) -> VoidType: ...
    
    def set_Site(self, value: ISite) -> VoidType: ...
    
    # ---------- Events ---------- #
    
    Disposed: EventType[EventHandler] = ...


class IContainer(Protocol, IDisposable):
    # ---------- Properties ---------- #
    
    @property
    def Components(self) -> ComponentCollection: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Add(self, component: IComponent) -> VoidType: ...
    
    @overload
    def Add(self, component: IComponent, name: StringType) -> VoidType: ...
    
    def Remove(self, component: IComponent) -> VoidType: ...
    
    def get_Components(self) -> ComponentCollection: ...
    
    # No Events


class ICustomTypeDescriptor(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetAttributes(self) -> AttributeCollection: ...
    
    def GetClassName(self) -> StringType: ...
    
    def GetComponentName(self) -> StringType: ...
    
    def GetConverter(self) -> TypeConverter: ...
    
    def GetDefaultEvent(self) -> EventDescriptor: ...
    
    def GetDefaultProperty(self) -> PropertyDescriptor: ...
    
    def GetEditor(self, editorBaseType: TypeType) -> ObjectType: ...
    
    @overload
    def GetEvents(self) -> EventDescriptorCollection: ...
    
    @overload
    def GetEvents(self, attributes: ArrayType[Attribute]) -> EventDescriptorCollection: ...
    
    @overload
    def GetProperties(self) -> PropertyDescriptorCollection: ...
    
    @overload
    def GetProperties(self, attributes: ArrayType[Attribute]) -> PropertyDescriptorCollection: ...
    
    def GetPropertyOwner(self, pd: PropertyDescriptor) -> ObjectType: ...
    
    # No Events


class IDataErrorInfo(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def Error(self) -> StringType: ...
    
    def __getitem__(self, key: StringType) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_Error(self) -> StringType: ...
    
    def get_Item(self, columnName: StringType) -> StringType: ...
    
    # No Events


class IEditableObject(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginEdit(self) -> VoidType: ...
    
    def CancelEdit(self) -> VoidType: ...
    
    def EndEdit(self) -> VoidType: ...
    
    # No Events


class IExtenderProvider(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def CanExtend(self, extendee: ObjectType) -> BooleanType: ...
    
    # No Events


class IIntellisenseBuilder(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def Name(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def Show(self, language: StringType, value: StringType, newValue: StringType) -> Tuple[BooleanType, StringType]: ...
    
    def get_Name(self) -> StringType: ...
    
    # No Events


class IListSource(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def ContainsListCollection(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def GetList(self) -> IList: ...
    
    def get_ContainsListCollection(self) -> BooleanType: ...
    
    # No Events


class INestedContainer(Protocol, IContainer, IDisposable):
    # ---------- Properties ---------- #
    
    @property
    def Owner(self) -> IComponent: ...
    
    # ---------- Methods ---------- #
    
    def get_Owner(self) -> IComponent: ...
    
    # No Events


class INestedSite(Protocol, ISite, IServiceProvider):
    # ---------- Properties ---------- #
    
    @property
    def FullName(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_FullName(self) -> StringType: ...
    
    # No Events


class INotifyDataErrorInfo(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def HasErrors(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def GetErrors(self, propertyName: StringType) -> IEnumerable: ...
    
    def add_ErrorsChanged(self, value: EventHandler[DataErrorsChangedEventArgs]) -> VoidType: ...
    
    def get_HasErrors(self) -> BooleanType: ...
    
    def remove_ErrorsChanged(self, value: EventHandler[DataErrorsChangedEventArgs]) -> VoidType: ...
    
    # ---------- Events ---------- #
    
    ErrorsChanged: EventType[EventHandler[DataErrorsChangedEventArgs]] = ...


class INotifyPropertyChanged(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def add_PropertyChanged(self, value: PropertyChangedEventHandler) -> VoidType: ...
    
    def remove_PropertyChanged(self, value: PropertyChangedEventHandler) -> VoidType: ...
    
    # ---------- Events ---------- #
    
    PropertyChanged: EventType[PropertyChangedEventHandler] = ...


class INotifyPropertyChanging(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def add_PropertyChanging(self, value: PropertyChangingEventHandler) -> VoidType: ...
    
    def remove_PropertyChanging(self, value: PropertyChangingEventHandler) -> VoidType: ...
    
    # ---------- Events ---------- #
    
    PropertyChanging: EventType[PropertyChangingEventHandler] = ...


class IRaiseItemChangedEvents(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def RaisesItemChangedEvents(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def get_RaisesItemChangedEvents(self) -> BooleanType: ...
    
    # No Events


class IRevertibleChangeTracking(Protocol, IChangeTracking):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def RejectChanges(self) -> VoidType: ...
    
    # No Events


class ISite(Protocol, IServiceProvider):
    # ---------- Properties ---------- #
    
    @property
    def Component(self) -> IComponent: ...
    
    @property
    def Container(self) -> IContainer: ...
    
    @property
    def DesignMode(self) -> BooleanType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @Name.setter
    def Name(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Component(self) -> IComponent: ...
    
    def get_Container(self) -> IContainer: ...
    
    def get_DesignMode(self) -> BooleanType: ...
    
    def get_Name(self) -> StringType: ...
    
    def set_Name(self, value: StringType) -> VoidType: ...
    
    # No Events


class ISupportInitialize(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInit(self) -> VoidType: ...
    
    def EndInit(self) -> VoidType: ...
    
    # No Events


class ISupportInitializeNotification(Protocol, ISupportInitialize):
    # ---------- Properties ---------- #
    
    @property
    def IsInitialized(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def add_Initialized(self, value: EventHandler) -> VoidType: ...
    
    def get_IsInitialized(self) -> BooleanType: ...
    
    def remove_Initialized(self, value: EventHandler) -> VoidType: ...
    
    # ---------- Events ---------- #
    
    Initialized: EventType[EventHandler] = ...


class ISynchronizeInvoke(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def InvokeRequired(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, method: Delegate, args: ArrayType[ObjectType]) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> ObjectType: ...
    
    def Invoke(self, method: Delegate, args: ArrayType[ObjectType]) -> ObjectType: ...
    
    def get_InvokeRequired(self) -> BooleanType: ...
    
    # No Events


class ITypeDescriptorContext(Protocol, IServiceProvider):
    # ---------- Properties ---------- #
    
    @property
    def Container(self) -> IContainer: ...
    
    @property
    def Instance(self) -> ObjectType: ...
    
    @property
    def PropertyDescriptor(self) -> PropertyDescriptor: ...
    
    # ---------- Methods ---------- #
    
    def OnComponentChanged(self) -> VoidType: ...
    
    def OnComponentChanging(self) -> BooleanType: ...
    
    def get_Container(self) -> IContainer: ...
    
    def get_Instance(self) -> ObjectType: ...
    
    def get_PropertyDescriptor(self) -> PropertyDescriptor: ...
    
    # No Events


class ITypedList(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetItemProperties(self, listAccessors: ArrayType[PropertyDescriptor]) -> PropertyDescriptorCollection: ...
    
    def GetListName(self, listAccessors: ArrayType[PropertyDescriptor]) -> StringType: ...
    
    # No Events


# ---------- Enums ---------- #

class BindableSupport(Enum):
    No: IntType = 0
    Yes: IntType = 1
    Default: IntType = 2


class BindingDirection(Enum):
    OneWay: IntType = 0
    TwoWay: IntType = 1


class CollectionChangeAction(Enum):
    Add: IntType = 1
    Remove: IntType = 2
    Refresh: IntType = 3


class DataObjectMethodType(Enum):
    Fill: IntType = 0
    Select: IntType = 1
    Update: IntType = 2
    Insert: IntType = 3
    Delete: IntType = 4


class DesignerSerializationVisibility(Enum):
    Hidden: IntType = 0
    Visible: IntType = 1
    Content: IntType = 2


class EditorBrowsableState(Enum):
    Always: IntType = 0
    Never: IntType = 1
    Advanced: IntType = 2


class InheritanceLevel(Enum):
    Inherited: IntType = 1
    InheritedReadOnly: IntType = 2
    NotInherited: IntType = 3


class LicenseUsageMode(Enum):
    Runtime: IntType = 0
    Designtime: IntType = 1


class ListChangedType(Enum):
    Reset: IntType = 0
    ItemAdded: IntType = 1
    ItemDeleted: IntType = 2
    ItemMoved: IntType = 3
    ItemChanged: IntType = 4
    PropertyDescriptorAdded: IntType = 5
    PropertyDescriptorDeleted: IntType = 6
    PropertyDescriptorChanged: IntType = 7


class ListSortDirection(Enum):
    Ascending: IntType = 0
    Descending: IntType = 1


class MaskedTextResultHint(Enum):
    PositionOutOfRange: IntType = -55
    NonEditPosition: IntType = -54
    UnavailableEditPosition: IntType = -53
    PromptCharNotAllowed: IntType = -52
    InvalidInput: IntType = -51
    SignedDigitExpected: IntType = -5
    LetterExpected: IntType = -4
    DigitExpected: IntType = -3
    AlphanumericCharacterExpected: IntType = -2
    AsciiCharacterExpected: IntType = -1
    Unknown: IntType = 0
    CharacterEscaped: IntType = 1
    NoEffect: IntType = 2
    SideEffect: IntType = 3
    Success: IntType = 4


class PropertyTabScope(Enum):
    Static: IntType = 0
    Global: IntType = 1
    Document: IntType = 2
    Component: IntType = 3


class RefreshProperties(Enum):
    #None: IntType = 0
    All: IntType = 1
    Repaint: IntType = 2


class ToolboxItemFilterType(Enum):
    Allow: IntType = 0
    Custom: IntType = 1
    Prevent: IntType = 2
    Require: IntType = 3


# ---------- Delegates ---------- #

AddingNewEventHandler = Callable[[ObjectType, AddingNewEventArgs], VoidType]

AsyncCompletedEventHandler = Callable[[ObjectType, AsyncCompletedEventArgs], VoidType]

CancelEventHandler = Callable[[ObjectType, CancelEventArgs], VoidType]

CollectionChangeEventHandler = Callable[[ObjectType, CollectionChangeEventArgs], VoidType]

DoWorkEventHandler = Callable[[ObjectType, DoWorkEventArgs], VoidType]

HandledEventHandler = Callable[[ObjectType, HandledEventArgs], VoidType]

ListChangedEventHandler = Callable[[ObjectType, ListChangedEventArgs], VoidType]

ProgressChangedEventHandler = Callable[[ObjectType, ProgressChangedEventArgs], VoidType]

PropertyChangedEventHandler = Callable[[ObjectType, PropertyChangedEventArgs], VoidType]

PropertyChangingEventHandler = Callable[[ObjectType, PropertyChangingEventArgs], VoidType]

RefreshEventHandler = Callable[[RefreshEventArgs], VoidType]

RunWorkerCompletedEventHandler = Callable[[ObjectType, RunWorkerCompletedEventArgs], VoidType]

__all__ = [
    AddingNewEventArgs,
    AddingNewEventHandler,
    AmbientValueAttribute,
    ArrayConverter,
    ArraySubsetEnumerator,
    AsyncCompletedEventArgs,
    AsyncCompletedEventHandler,
    AsyncOperation,
    AsyncOperationManager,
    AttributeCollection,
    AttributeProviderAttribute,
    BackgroundWorker,
    BaseNumberConverter,
    BindableAttribute,
    BindingList,
    BooleanConverter,
    BrowsableAttribute,
    ByteConverter,
    CancelEventArgs,
    CancelEventHandler,
    CategoryAttribute,
    CharConverter,
    CollectionChangeEventArgs,
    CollectionChangeEventHandler,
    CollectionConverter,
    CompModSwitches,
    ComplexBindingPropertiesAttribute,
    Component,
    ComponentCollection,
    ComponentConverter,
    ComponentEditor,
    ComponentResourceManager,
    Container,
    ContainerFilterService,
    CultureInfoConverter,
    CustomTypeDescriptor,
    DataErrorsChangedEventArgs,
    DataObjectAttribute,
    DataObjectFieldAttribute,
    DataObjectMethodAttribute,
    DateTimeConverter,
    DateTimeOffsetConverter,
    DecimalConverter,
    DefaultBindingPropertyAttribute,
    DefaultEventAttribute,
    DefaultPropertyAttribute,
    DefaultValueAttribute,
    DelegatingTypeDescriptionProvider,
    DescriptionAttribute,
    DesignOnlyAttribute,
    DesignTimeVisibleAttribute,
    DesignerAttribute,
    DesignerCategoryAttribute,
    DesignerSerializationVisibilityAttribute,
    DisplayNameAttribute,
    DoWorkEventArgs,
    DoWorkEventHandler,
    DoubleConverter,
    EditorAttribute,
    EditorBrowsableAttribute,
    EnumConverter,
    EventDescriptor,
    EventDescriptorCollection,
    EventHandlerList,
    ExpandableObjectConverter,
    ExtendedPropertyDescriptor,
    ExtenderProvidedPropertyAttribute,
    GuidConverter,
    HandledEventArgs,
    HandledEventHandler,
    ImmutableObjectAttribute,
    InheritanceAttribute,
    InitializationEventAttribute,
    InstallerTypeAttribute,
    InstanceCreationEditor,
    Int16Converter,
    Int32Converter,
    Int64Converter,
    IntSecurity,
    InvalidAsynchronousStateException,
    InvalidEnumArgumentException,
    LicFileLicenseProvider,
    License,
    LicenseContext,
    LicenseException,
    LicenseManager,
    LicenseProvider,
    LicenseProviderAttribute,
    ListBindableAttribute,
    ListChangedEventArgs,
    ListChangedEventHandler,
    ListSortDescription,
    ListSortDescriptionCollection,
    LocalizableAttribute,
    LookupBindingPropertiesAttribute,
    MarshalByValueComponent,
    MaskedTextProvider,
    MemberDescriptor,
    MergablePropertyAttribute,
    MultilineStringConverter,
    NestedContainer,
    NotifyParentPropertyAttribute,
    NullableConverter,
    ParenthesizePropertyNameAttribute,
    PasswordPropertyTextAttribute,
    ProgressChangedEventArgs,
    ProgressChangedEventHandler,
    PropertyChangedEventArgs,
    PropertyChangedEventHandler,
    PropertyChangingEventArgs,
    PropertyChangingEventHandler,
    PropertyDescriptor,
    PropertyDescriptorCollection,
    PropertyTabAttribute,
    ProvidePropertyAttribute,
    ReadOnlyAttribute,
    RecommendedAsConfigurableAttribute,
    ReferenceConverter,
    ReflectEventDescriptor,
    ReflectPropertyDescriptor,
    ReflectTypeDescriptionProvider,
    RefreshEventArgs,
    RefreshEventHandler,
    RefreshPropertiesAttribute,
    RunInstallerAttribute,
    RunWorkerCompletedEventArgs,
    RunWorkerCompletedEventHandler,
    SByteConverter,
    SettingsBindableAttribute,
    SingleConverter,
    StringConverter,
    SyntaxCheck,
    TimeSpanConverter,
    ToolboxItemAttribute,
    ToolboxItemFilterAttribute,
    TypeConverter,
    TypeConverterAttribute,
    TypeDescriptionProvider,
    TypeDescriptionProviderAttribute,
    TypeDescriptor,
    TypeListConverter,
    UInt16Converter,
    UInt32Converter,
    UInt64Converter,
    WarningException,
    WeakHashtable,
    Win32Exception,
    IBindingList,
    IBindingListView,
    ICancelAddNew,
    IChangeTracking,
    IComNativeDescriptorHandler,
    IComponent,
    IContainer,
    ICustomTypeDescriptor,
    IDataErrorInfo,
    IEditableObject,
    IExtenderProvider,
    IIntellisenseBuilder,
    IListSource,
    INestedContainer,
    INestedSite,
    INotifyDataErrorInfo,
    INotifyPropertyChanged,
    INotifyPropertyChanging,
    IRaiseItemChangedEvents,
    IRevertibleChangeTracking,
    ISite,
    ISupportInitialize,
    ISupportInitializeNotification,
    ISynchronizeInvoke,
    ITypeDescriptorContext,
    ITypedList,
    BindableSupport,
    BindingDirection,
    CollectionChangeAction,
    DataObjectMethodType,
    DesignerSerializationVisibility,
    EditorBrowsableState,
    InheritanceLevel,
    LicenseUsageMode,
    ListChangedType,
    ListSortDirection,
    MaskedTextResultHint,
    PropertyTabScope,
    RefreshProperties,
    ToolboxItemFilterType,
    AddingNewEventHandler,
    AsyncCompletedEventHandler,
    CancelEventHandler,
    CollectionChangeEventHandler,
    DoWorkEventHandler,
    HandledEventHandler,
    ListChangedEventHandler,
    ProgressChangedEventHandler,
    PropertyChangedEventHandler,
    PropertyChangingEventHandler,
    RefreshEventHandler,
    RunWorkerCompletedEventHandler,
]
