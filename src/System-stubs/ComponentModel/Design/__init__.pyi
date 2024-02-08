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

from System import Array
from System import Attribute
from System import Enum
from System import EventArgs
from System import EventHandler
from System import Exception
from System import Guid
from System import IDisposable
from System import IntPtr
from System import IServiceProvider
from System import Object
from System import Type
from System.Collections import CollectionBase
from System.Collections import ICollection
from System.Collections import IDictionary
from System.Collections import IEnumerable
from System.Collections import IEnumerator
from System.Collections import IList
from System.ComponentModel import EventDescriptor
from System.ComponentModel import EventDescriptorCollection
from System.ComponentModel import IComponent
from System.ComponentModel import IContainer
from System.ComponentModel import IExtenderProvider
from System.ComponentModel import InheritanceAttribute
from System.ComponentModel import LicenseContext
from System.ComponentModel import LicenseUsageMode
from System.ComponentModel import MemberDescriptor
from System.ComponentModel import PropertyDescriptor
from System.ComponentModel import PropertyDescriptorCollection
from System.ComponentModel import TypeDescriptionProvider
from System.ComponentModel.Design.DesignerOptionService import DesignerOptionCollection
from System.Globalization import CultureInfo
from System.IO import Stream
from System.Reflection import Assembly
from System.Reflection import AssemblyName
from System.Reflection import MethodBase
from System.Resources import IResourceReader
from System.Resources import IResourceWriter
from System.Runtime.InteropServices import ExternalException
from System.Runtime.InteropServices import _Attribute
from System.Runtime.InteropServices import _Exception
from System.Runtime.Serialization import ISerializable
from System.Runtime.Serialization import SerializationInfo
from System.Runtime.Serialization import StreamingContext

T = TypeVar("T")

class EventType(Generic[T]):
    def __iadd__(self, other: T): ...
    def __isub__(self, other: T): ...

class ActiveDesignerEventArgs(EventArgs):
    """"""

    def __init__(self, oldDesigner: IDesignerHost, newDesigner: IDesignerHost):
        """

        :param oldDesigner:
        :param newDesigner:
        """
    @property
    def NewDesigner(self) -> IDesignerHost:
        """

        :return:
        """
    @property
    def OldDesigner(self) -> IDesignerHost:
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

ActiveDesignerEventHandler: Callable[[object, ActiveDesignerEventArgs], None] = ...
"""

:param sender: 
:param e: 
"""

class CheckoutException(ExternalException, _Exception, ISerializable):
    """"""

    Canceled: Final[ClassVar[CheckoutException]] = ...
    """
    
    :return: 
    """
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
    def __init__(self, message: str, errorCode: int):
        """

        :param message:
        :param errorCode:
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

class CommandID(Object):
    """"""

    def __init__(self, menuGroup: Guid, commandID: int):
        """

        :param menuGroup:
        :param commandID:
        """
    @property
    def Guid(self) -> Guid:
        """

        :return:
        """
    @property
    def ID(self) -> int:
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

class ComponentChangedEventArgs(EventArgs):
    """"""

    def __init__(
        self, component: object, member: MemberDescriptor, oldValue: object, newValue: object
    ):
        """

        :param component:
        :param member:
        :param oldValue:
        :param newValue:
        """
    @property
    def Component(self) -> object:
        """

        :return:
        """
    @property
    def Member(self) -> MemberDescriptor:
        """

        :return:
        """
    @property
    def NewValue(self) -> object:
        """

        :return:
        """
    @property
    def OldValue(self) -> object:
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

ComponentChangedEventHandler: Callable[[object, ComponentChangedEventArgs], None] = ...
"""

:param sender: 
:param e: 
"""

class ComponentChangingEventArgs(EventArgs):
    """"""

    def __init__(self, component: object, member: MemberDescriptor):
        """

        :param component:
        :param member:
        """
    @property
    def Component(self) -> object:
        """

        :return:
        """
    @property
    def Member(self) -> MemberDescriptor:
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

ComponentChangingEventHandler: Callable[[object, ComponentChangingEventArgs], None] = ...
"""

:param sender: 
:param e: 
"""

class ComponentEventArgs(EventArgs):
    """"""

    def __init__(self, component: IComponent):
        """

        :param component:
        """
    @property
    def Component(self) -> IComponent:
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

ComponentEventHandler: Callable[[object, ComponentEventArgs], None] = ...
"""

:param sender: 
:param e: 
"""

class ComponentRenameEventArgs(EventArgs):
    """"""

    def __init__(self, component: object, oldName: str, newName: str):
        """

        :param component:
        :param oldName:
        :param newName:
        """
    @property
    def Component(self) -> object:
        """

        :return:
        """
    @property
    def NewName(self) -> str:
        """

        :return:
        """
    @property
    def OldName(self) -> str:
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

ComponentRenameEventHandler: Callable[[object, ComponentRenameEventArgs], None] = ...
"""

:param sender: 
:param e: 
"""

class DesignerCollection(Object, ICollection, IEnumerable):
    """"""

    @overload
    def __init__(self, designers: IList):
        """

        :param designers:
        """
    @overload
    def __init__(self, designers: Array[IDesignerHost]):
        """

        :param designers:
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
    def Item(self) -> IDesignerHost:
        """

        :return:
        """
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
    def __getitem__(self, index: int) -> IDesignerHost:
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

class DesignerEventArgs(EventArgs):
    """"""

    def __init__(self, host: IDesignerHost):
        """

        :param host:
        """
    @property
    def Designer(self) -> IDesignerHost:
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

DesignerEventHandler: Callable[[object, DesignerEventArgs], None] = ...
"""

:param sender: 
:param e: 
"""

class DesignerOptionService(ABC, Object, IDesignerOptionService):
    """"""

    @property
    def Options(self) -> DesignerOptionService.DesignerOptionCollection:
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
    def GetOptionValue(self, pageName: str, valueName: str) -> object:
        """

        :param pageName:
        :param valueName:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def SetOptionValue(self, pageName: str, valueName: str, value: object) -> None:
        """

        :param pageName:
        :param valueName:
        :param value:
        """
    def ToString(self) -> str:
        """

        :return:
        """

    class DesignerOptionCollection(Object, ICollection, IEnumerable, IList):
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
        def Name(self) -> str:
            """"""
        @property
        def Parent(self) -> DesignerOptionService.DesignerOptionCollection:
            """"""
        @property
        def Properties(self) -> PropertyDescriptorCollection:
            """"""
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
        @overload
        def IndexOf(self, value: DesignerOptionService.DesignerOptionCollection) -> int:
            """"""
        @overload
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
        def ShowDialog(self) -> bool:
            """"""
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
        def __getitem__(self, name: str) -> DesignerOptionService.DesignerOptionCollection:
            """"""
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

class DesignerTransaction(ABC, Object, IDisposable):
    """"""

    @property
    def Canceled(self) -> bool:
        """

        :return:
        """
    @property
    def Committed(self) -> bool:
        """

        :return:
        """
    @property
    def Description(self) -> str:
        """

        :return:
        """
    def Cancel(self) -> None:
        """"""
    def Commit(self) -> None:
        """"""
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

class DesignerTransactionCloseEventArgs(EventArgs):
    """"""

    @overload
    def __init__(self, commit: bool):
        """

        :param commit:
        """
    @overload
    def __init__(self, commit: bool, lastTransaction: bool):
        """

        :param commit:
        :param lastTransaction:
        """
    @property
    def LastTransaction(self) -> bool:
        """

        :return:
        """
    @property
    def TransactionCommitted(self) -> bool:
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

DesignerTransactionCloseEventHandler: Callable[
    [object, DesignerTransactionCloseEventArgs], None
] = ...
"""

:param sender: 
:param e: 
"""

class DesignerVerb(MenuCommand):
    """"""

    @overload
    def __init__(self, text: str, handler: EventHandler):
        """

        :param text:
        :param handler:
        """
    @overload
    def __init__(self, text: str, handler: EventHandler, startCommandID: CommandID):
        """

        :param text:
        :param handler:
        :param startCommandID:
        """
    @property
    def Checked(self) -> bool:
        """

        :return:
        """
    @Checked.setter
    def Checked(self, value: bool) -> None: ...
    @property
    def CommandID(self) -> CommandID:
        """

        :return:
        """
    @property
    def Description(self) -> str:
        """

        :return:
        """
    @Description.setter
    def Description(self, value: str) -> None: ...
    @property
    def Enabled(self) -> bool:
        """

        :return:
        """
    @Enabled.setter
    def Enabled(self, value: bool) -> None: ...
    @property
    def OleStatus(self) -> int:
        """

        :return:
        """
    @property
    def Properties(self) -> IDictionary:
        """

        :return:
        """
    @property
    def Supported(self) -> bool:
        """

        :return:
        """
    @Supported.setter
    def Supported(self, value: bool) -> None: ...
    @property
    def Text(self) -> str:
        """

        :return:
        """
    @property
    def Visible(self) -> bool:
        """

        :return:
        """
    @Visible.setter
    def Visible(self, value: bool) -> None: ...
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
    @overload
    def Invoke(self) -> None:
        """"""
    @overload
    def Invoke(self, arg: object) -> None:
        """

        :param arg:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    CommandChanged: EventType[EventHandler] = ...
    """"""

class DesignerVerbCollection(CollectionBase, ICollection, IEnumerable, IList):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, value: Array[DesignerVerb]):
        """

        :param value:
        """
    @property
    def Capacity(self) -> int:
        """

        :return:
        """
    @Capacity.setter
    def Capacity(self, value: int) -> None: ...
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
    def Add(self, value: DesignerVerb) -> int:
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
    def AddRange(self, value: DesignerVerbCollection) -> None:
        """

        :param value:
        """
    @overload
    def AddRange(self, value: Array[DesignerVerb]) -> None:
        """

        :param value:
        """
    def Clear(self) -> None:
        """"""
    @overload
    def Contains(self, value: DesignerVerb) -> bool:
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
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    @overload
    def CopyTo(self, array: Array[DesignerVerb], index: int) -> None:
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
    @overload
    def IndexOf(self, value: DesignerVerb) -> int:
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
    def Insert(self, index: int, value: DesignerVerb) -> None:
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
    def Remove(self, value: DesignerVerb) -> None:
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
    def __setitem__(self, index: int, value: DesignerVerb) -> None:
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

class DesigntimeLicenseContext(LicenseContext, IServiceProvider):
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

class DesigntimeLicenseContextSerializer(Object):
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
    def Serialize(cls, o: Stream, cryptoKey: str, context: DesigntimeLicenseContext) -> None:
        """

        :param o:
        :param cryptoKey:
        :param context:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class HelpContextType(Enum):
    """"""

    Ambient: HelpContextType = ...
    """"""
    Window: HelpContextType = ...
    """"""
    Selection: HelpContextType = ...
    """"""
    ToolWindowSelection: HelpContextType = ...
    """"""

class HelpKeywordAttribute(Attribute, _Attribute):
    """"""

    Default: Final[ClassVar[HelpKeywordAttribute]] = ...
    """
    
    :return: 
    """
    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, keyword: str):
        """

        :param keyword:
        """
    @overload
    def __init__(self, t: Type):
        """

        :param t:
        """
    @property
    def HelpKeyword(self) -> str:
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

class HelpKeywordType(Enum):
    """"""

    F1Keyword: HelpKeywordType = ...
    """"""
    GeneralKeyword: HelpKeywordType = ...
    """"""
    FilterKeyword: HelpKeywordType = ...
    """"""

class IComponentChangeService:
    """"""

    def OnComponentChanged(
        self, component: object, member: MemberDescriptor, oldValue: object, newValue: object
    ) -> None:
        """

        :param component:
        :param member:
        :param oldValue:
        :param newValue:
        """
    def OnComponentChanging(self, component: object, member: MemberDescriptor) -> None:
        """

        :param component:
        :param member:
        """
    ComponentAdded: EventType[ComponentEventHandler] = ...
    """"""
    ComponentAdding: EventType[ComponentEventHandler] = ...
    """"""
    ComponentChanged: EventType[ComponentChangedEventHandler] = ...
    """"""
    ComponentChanging: EventType[ComponentChangingEventHandler] = ...
    """"""
    ComponentRemoved: EventType[ComponentEventHandler] = ...
    """"""
    ComponentRemoving: EventType[ComponentEventHandler] = ...
    """"""
    ComponentRename: EventType[ComponentRenameEventHandler] = ...
    """"""

class IComponentDiscoveryService:
    """"""

    def GetComponentTypes(self, designerHost: IDesignerHost, baseType: Type) -> ICollection:
        """

        :param designerHost:
        :param baseType:
        :return:
        """

class IComponentInitializer:
    """"""

    def InitializeExistingComponent(self, defaultValues: IDictionary) -> None:
        """

        :param defaultValues:
        """
    def InitializeNewComponent(self, defaultValues: IDictionary) -> None:
        """

        :param defaultValues:
        """

class IDesigner(IDisposable):
    """"""

    @property
    def Component(self) -> IComponent:
        """

        :return:
        """
    @property
    def Verbs(self) -> DesignerVerbCollection:
        """

        :return:
        """
    def Dispose(self) -> None:
        """"""
    def DoDefaultAction(self) -> None:
        """"""
    def Initialize(self, component: IComponent) -> None:
        """

        :param component:
        """

class IDesignerEventService:
    """"""

    @property
    def ActiveDesigner(self) -> IDesignerHost:
        """

        :return:
        """
    @property
    def Designers(self) -> DesignerCollection:
        """

        :return:
        """
    ActiveDesignerChanged: EventType[ActiveDesignerEventHandler] = ...
    """"""
    DesignerCreated: EventType[DesignerEventHandler] = ...
    """"""
    DesignerDisposed: EventType[DesignerEventHandler] = ...
    """"""
    SelectionChanged: EventType[EventHandler] = ...
    """"""

class IDesignerFilter:
    """"""

    def PostFilterAttributes(self, attributes: IDictionary) -> None:
        """

        :param attributes:
        """
    def PostFilterEvents(self, events: IDictionary) -> None:
        """

        :param events:
        """
    def PostFilterProperties(self, properties: IDictionary) -> None:
        """

        :param properties:
        """
    def PreFilterAttributes(self, attributes: IDictionary) -> None:
        """

        :param attributes:
        """
    def PreFilterEvents(self, events: IDictionary) -> None:
        """

        :param events:
        """
    def PreFilterProperties(self, properties: IDictionary) -> None:
        """

        :param properties:
        """

class IDesignerHost(IServiceContainer, IServiceProvider):
    """"""

    @property
    def Container(self) -> IContainer:
        """

        :return:
        """
    @property
    def InTransaction(self) -> bool:
        """

        :return:
        """
    @property
    def Loading(self) -> bool:
        """

        :return:
        """
    @property
    def RootComponent(self) -> IComponent:
        """

        :return:
        """
    @property
    def RootComponentClassName(self) -> str:
        """

        :return:
        """
    @property
    def TransactionDescription(self) -> str:
        """

        :return:
        """
    def Activate(self) -> None:
        """"""
    @overload
    def AddService(self, serviceType: Type, callback: ServiceCreatorCallback) -> None:
        """

        :param serviceType:
        :param callback:
        """
    @overload
    def AddService(self, serviceType: Type, serviceInstance: object) -> None:
        """

        :param serviceType:
        :param serviceInstance:
        """
    @overload
    def AddService(
        self, serviceType: Type, callback: ServiceCreatorCallback, promote: bool
    ) -> None:
        """

        :param serviceType:
        :param callback:
        :param promote:
        """
    @overload
    def AddService(self, serviceType: Type, serviceInstance: object, promote: bool) -> None:
        """

        :param serviceType:
        :param serviceInstance:
        :param promote:
        """
    @overload
    def CreateComponent(self, componentClass: Type) -> IComponent:
        """

        :param componentClass:
        :return:
        """
    @overload
    def CreateComponent(self, componentClass: Type, name: str) -> IComponent:
        """

        :param componentClass:
        :param name:
        :return:
        """
    @overload
    def CreateTransaction(self) -> DesignerTransaction:
        """

        :return:
        """
    @overload
    def CreateTransaction(self, description: str) -> DesignerTransaction:
        """

        :param description:
        :return:
        """
    def DestroyComponent(self, component: IComponent) -> None:
        """

        :param component:
        """
    def GetDesigner(self, component: IComponent) -> IDesigner:
        """

        :param component:
        :return:
        """
    def GetService(self, serviceType: Type) -> object:
        """

        :param serviceType:
        :return:
        """
    def GetType(self, typeName: str) -> Type:
        """

        :param typeName:
        :return:
        """
    @overload
    def RemoveService(self, serviceType: Type) -> None:
        """

        :param serviceType:
        """
    @overload
    def RemoveService(self, serviceType: Type, promote: bool) -> None:
        """

        :param serviceType:
        :param promote:
        """
    Activated: EventType[EventHandler] = ...
    """"""
    Deactivated: EventType[EventHandler] = ...
    """"""
    LoadComplete: EventType[EventHandler] = ...
    """"""
    TransactionClosed: EventType[DesignerTransactionCloseEventHandler] = ...
    """"""
    TransactionClosing: EventType[DesignerTransactionCloseEventHandler] = ...
    """"""
    TransactionOpened: EventType[EventHandler] = ...
    """"""
    TransactionOpening: EventType[EventHandler] = ...
    """"""

class IDesignerHostTransactionState:
    """"""

    @property
    def IsClosingTransaction(self) -> bool:
        """

        :return:
        """

class IDesignerOptionService:
    """"""

    def GetOptionValue(self, pageName: str, valueName: str) -> object:
        """

        :param pageName:
        :param valueName:
        :return:
        """
    def SetOptionValue(self, pageName: str, valueName: str, value: object) -> None:
        """

        :param pageName:
        :param valueName:
        :param value:
        """

class IDictionaryService:
    """"""

    def GetKey(self, value: object) -> object:
        """

        :param value:
        :return:
        """
    def GetValue(self, key: object) -> object:
        """

        :param key:
        :return:
        """
    def SetValue(self, key: object, value: object) -> None:
        """

        :param key:
        :param value:
        """

class IEventBindingService:
    """"""

    def CreateUniqueMethodName(self, component: IComponent, e: EventDescriptor) -> str:
        """

        :param component:
        :param e:
        :return:
        """
    def GetCompatibleMethods(self, e: EventDescriptor) -> ICollection:
        """

        :param e:
        :return:
        """
    def GetEvent(self, property: PropertyDescriptor) -> EventDescriptor:
        """

        :param property:
        :return:
        """
    def GetEventProperties(self, events: EventDescriptorCollection) -> PropertyDescriptorCollection:
        """

        :param events:
        :return:
        """
    def GetEventProperty(self, e: EventDescriptor) -> PropertyDescriptor:
        """

        :param e:
        :return:
        """
    @overload
    def ShowCode(self) -> bool:
        """

        :return:
        """
    @overload
    def ShowCode(self, lineNumber: int) -> bool:
        """

        :param lineNumber:
        :return:
        """
    @overload
    def ShowCode(self, component: IComponent, e: EventDescriptor) -> bool:
        """

        :param component:
        :param e:
        :return:
        """

class IExtenderListService:
    """"""

    def GetExtenderProviders(self) -> Array[IExtenderProvider]:
        """

        :return:
        """

class IExtenderProviderService:
    """"""

    def AddExtenderProvider(self, provider: IExtenderProvider) -> None:
        """

        :param provider:
        """
    def RemoveExtenderProvider(self, provider: IExtenderProvider) -> None:
        """

        :param provider:
        """

class IHelpService:
    """"""

    def AddContextAttribute(self, name: str, value: str, keywordType: HelpKeywordType) -> None:
        """

        :param name:
        :param value:
        :param keywordType:
        """
    def ClearContextAttributes(self) -> None:
        """"""
    def CreateLocalContext(self, contextType: HelpContextType) -> IHelpService:
        """

        :param contextType:
        :return:
        """
    def RemoveContextAttribute(self, name: str, value: str) -> None:
        """

        :param name:
        :param value:
        """
    def RemoveLocalContext(self, localContext: IHelpService) -> None:
        """

        :param localContext:
        """
    def ShowHelpFromKeyword(self, helpKeyword: str) -> None:
        """

        :param helpKeyword:
        """
    def ShowHelpFromUrl(self, helpUrl: str) -> None:
        """

        :param helpUrl:
        """

class IInheritanceService:
    """"""

    def AddInheritedComponents(self, component: IComponent, container: IContainer) -> None:
        """

        :param component:
        :param container:
        """
    def GetInheritanceAttribute(self, component: IComponent) -> InheritanceAttribute:
        """

        :param component:
        :return:
        """

class IMenuCommandService:
    """"""

    @property
    def Verbs(self) -> DesignerVerbCollection:
        """

        :return:
        """
    def AddCommand(self, command: MenuCommand) -> None:
        """

        :param command:
        """
    def AddVerb(self, verb: DesignerVerb) -> None:
        """

        :param verb:
        """
    def FindCommand(self, commandID: CommandID) -> MenuCommand:
        """

        :param commandID:
        :return:
        """
    def GlobalInvoke(self, commandID: CommandID) -> bool:
        """

        :param commandID:
        :return:
        """
    def RemoveCommand(self, command: MenuCommand) -> None:
        """

        :param command:
        """
    def RemoveVerb(self, verb: DesignerVerb) -> None:
        """

        :param verb:
        """
    def ShowContextMenu(self, menuID: CommandID, x: int, y: int) -> None:
        """

        :param menuID:
        :param x:
        :param y:
        """

class IReferenceService:
    """"""

    def GetComponent(self, reference: object) -> IComponent:
        """

        :param reference:
        :return:
        """
    def GetName(self, reference: object) -> str:
        """

        :param reference:
        :return:
        """
    def GetReference(self, name: str) -> object:
        """

        :param name:
        :return:
        """
    @overload
    def GetReferences(self) -> Array[object]:
        """

        :return:
        """
    @overload
    def GetReferences(self, baseType: Type) -> Array[object]:
        """

        :param baseType:
        :return:
        """

class IResourceService:
    """"""

    def GetResourceReader(self, info: CultureInfo) -> IResourceReader:
        """

        :param info:
        :return:
        """
    def GetResourceWriter(self, info: CultureInfo) -> IResourceWriter:
        """

        :param info:
        :return:
        """

class IRootDesigner(IDesigner, IDisposable):
    """"""

    @property
    def Component(self) -> IComponent:
        """

        :return:
        """
    @property
    def SupportedTechnologies(self) -> Array[ViewTechnology]:
        """

        :return:
        """
    @property
    def Verbs(self) -> DesignerVerbCollection:
        """

        :return:
        """
    def Dispose(self) -> None:
        """"""
    def DoDefaultAction(self) -> None:
        """"""
    def GetView(self, technology: ViewTechnology) -> object:
        """

        :param technology:
        :return:
        """
    def Initialize(self, component: IComponent) -> None:
        """

        :param component:
        """

class ISelectionService:
    """"""

    @property
    def PrimarySelection(self) -> object:
        """

        :return:
        """
    @property
    def SelectionCount(self) -> int:
        """

        :return:
        """
    def GetComponentSelected(self, component: object) -> bool:
        """

        :param component:
        :return:
        """
    def GetSelectedComponents(self) -> ICollection:
        """

        :return:
        """
    @overload
    def SetSelectedComponents(self, components: ICollection) -> None:
        """

        :param components:
        """
    @overload
    def SetSelectedComponents(self, components: ICollection, selectionType: SelectionTypes) -> None:
        """

        :param components:
        :param selectionType:
        """
    SelectionChanged: EventType[EventHandler] = ...
    """"""
    SelectionChanging: EventType[EventHandler] = ...
    """"""

class IServiceContainer(IServiceProvider):
    """"""

    @overload
    def AddService(self, serviceType: Type, callback: ServiceCreatorCallback) -> None:
        """

        :param serviceType:
        :param callback:
        """
    @overload
    def AddService(self, serviceType: Type, serviceInstance: object) -> None:
        """

        :param serviceType:
        :param serviceInstance:
        """
    @overload
    def AddService(
        self, serviceType: Type, callback: ServiceCreatorCallback, promote: bool
    ) -> None:
        """

        :param serviceType:
        :param callback:
        :param promote:
        """
    @overload
    def AddService(self, serviceType: Type, serviceInstance: object, promote: bool) -> None:
        """

        :param serviceType:
        :param serviceInstance:
        :param promote:
        """
    def GetService(self, serviceType: Type) -> object:
        """

        :param serviceType:
        :return:
        """
    @overload
    def RemoveService(self, serviceType: Type) -> None:
        """

        :param serviceType:
        """
    @overload
    def RemoveService(self, serviceType: Type, promote: bool) -> None:
        """

        :param serviceType:
        :param promote:
        """

class ITreeDesigner(IDesigner, IDisposable):
    """"""

    @property
    def Children(self) -> ICollection:
        """

        :return:
        """
    @property
    def Component(self) -> IComponent:
        """

        :return:
        """
    @property
    def Parent(self) -> IDesigner:
        """

        :return:
        """
    @property
    def Verbs(self) -> DesignerVerbCollection:
        """

        :return:
        """
    def Dispose(self) -> None:
        """"""
    def DoDefaultAction(self) -> None:
        """"""
    def Initialize(self, component: IComponent) -> None:
        """

        :param component:
        """

class ITypeDescriptorFilterService:
    """"""

    def FilterAttributes(self, component: IComponent, attributes: IDictionary) -> bool:
        """

        :param component:
        :param attributes:
        :return:
        """
    def FilterEvents(self, component: IComponent, events: IDictionary) -> bool:
        """

        :param component:
        :param events:
        :return:
        """
    def FilterProperties(self, component: IComponent, properties: IDictionary) -> bool:
        """

        :param component:
        :param properties:
        :return:
        """

class ITypeDiscoveryService:
    """"""

    def GetTypes(self, baseType: Type, excludeGlobalTypes: bool) -> ICollection:
        """

        :param baseType:
        :param excludeGlobalTypes:
        :return:
        """

class ITypeResolutionService:
    """"""

    @overload
    def GetAssembly(self, name: AssemblyName) -> Assembly:
        """

        :param name:
        :return:
        """
    @overload
    def GetAssembly(self, name: AssemblyName, throwOnError: bool) -> Assembly:
        """

        :param name:
        :param throwOnError:
        :return:
        """
    def GetPathOfAssembly(self, name: AssemblyName) -> str:
        """

        :param name:
        :return:
        """
    @overload
    def GetType(self, name: str) -> Type:
        """

        :param name:
        :return:
        """
    @overload
    def GetType(self, name: str, throwOnError: bool) -> Type:
        """

        :param name:
        :param throwOnError:
        :return:
        """
    @overload
    def GetType(self, name: str, throwOnError: bool, ignoreCase: bool) -> Type:
        """

        :param name:
        :param throwOnError:
        :param ignoreCase:
        :return:
        """
    def ReferenceAssembly(self, name: AssemblyName) -> None:
        """

        :param name:
        """

class MenuCommand(Object):
    """"""

    def __init__(self, handler: EventHandler, command: CommandID):
        """

        :param handler:
        :param command:
        """
    @property
    def Checked(self) -> bool:
        """

        :return:
        """
    @Checked.setter
    def Checked(self, value: bool) -> None: ...
    @property
    def CommandID(self) -> CommandID:
        """

        :return:
        """
    @property
    def Enabled(self) -> bool:
        """

        :return:
        """
    @Enabled.setter
    def Enabled(self, value: bool) -> None: ...
    @property
    def OleStatus(self) -> int:
        """

        :return:
        """
    @property
    def Properties(self) -> IDictionary:
        """

        :return:
        """
    @property
    def Supported(self) -> bool:
        """

        :return:
        """
    @Supported.setter
    def Supported(self, value: bool) -> None: ...
    @property
    def Visible(self) -> bool:
        """

        :return:
        """
    @Visible.setter
    def Visible(self, value: bool) -> None: ...
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
    @overload
    def Invoke(self) -> None:
        """"""
    @overload
    def Invoke(self, arg: object) -> None:
        """

        :param arg:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    CommandChanged: EventType[EventHandler] = ...
    """"""

class RuntimeLicenseContext(LicenseContext, IServiceProvider):
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

class SelectionTypes(Enum):
    """"""

    Auto: SelectionTypes = ...
    """"""
    Normal: SelectionTypes = ...
    """"""
    Replace: SelectionTypes = ...
    """"""
    MouseDown: SelectionTypes = ...
    """"""
    MouseUp: SelectionTypes = ...
    """"""
    Click: SelectionTypes = ...
    """"""
    Primary: SelectionTypes = ...
    """"""
    Valid: SelectionTypes = ...
    """"""
    Toggle: SelectionTypes = ...
    """"""
    Add: SelectionTypes = ...
    """"""
    Remove: SelectionTypes = ...
    """"""

class ServiceContainer(Object, IServiceContainer, IDisposable, IServiceProvider):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, parentProvider: IServiceProvider):
        """

        :param parentProvider:
        """
    @overload
    def AddService(self, serviceType: Type, callback: ServiceCreatorCallback) -> None:
        """

        :param serviceType:
        :param callback:
        """
    @overload
    def AddService(self, serviceType: Type, serviceInstance: object) -> None:
        """

        :param serviceType:
        :param serviceInstance:
        """
    @overload
    def AddService(
        self, serviceType: Type, callback: ServiceCreatorCallback, promote: bool
    ) -> None:
        """

        :param serviceType:
        :param callback:
        :param promote:
        """
    @overload
    def AddService(self, serviceType: Type, serviceInstance: object, promote: bool) -> None:
        """

        :param serviceType:
        :param serviceInstance:
        :param promote:
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
    def GetService(self, serviceType: Type) -> object:
        """

        :param serviceType:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def RemoveService(self, serviceType: Type) -> None:
        """

        :param serviceType:
        """
    @overload
    def RemoveService(self, serviceType: Type, promote: bool) -> None:
        """

        :param serviceType:
        :param promote:
        """
    def ToString(self) -> str:
        """

        :return:
        """

ServiceCreatorCallback: Callable[[IServiceContainer, Type], object] = ...
"""

:param container: 
:param serviceType: 
:return: 
"""

class StandardCommands(Object):
    """"""

    AlignBottom: Final[ClassVar[CommandID]] = ...
    """
    
    :return: 
    """
    AlignHorizontalCenters: Final[ClassVar[CommandID]] = ...
    """
    
    :return: 
    """
    AlignLeft: Final[ClassVar[CommandID]] = ...
    """
    
    :return: 
    """
    AlignRight: Final[ClassVar[CommandID]] = ...
    """
    
    :return: 
    """
    AlignToGrid: Final[ClassVar[CommandID]] = ...
    """
    
    :return: 
    """
    AlignTop: Final[ClassVar[CommandID]] = ...
    """
    
    :return: 
    """
    AlignVerticalCenters: Final[ClassVar[CommandID]] = ...
    """
    
    :return: 
    """
    ArrangeBottom: Final[ClassVar[CommandID]] = ...
    """
    
    :return: 
    """
    ArrangeIcons: Final[ClassVar[CommandID]] = ...
    """
    
    :return: 
    """
    ArrangeRight: Final[ClassVar[CommandID]] = ...
    """
    
    :return: 
    """
    BringForward: Final[ClassVar[CommandID]] = ...
    """
    
    :return: 
    """
    BringToFront: Final[ClassVar[CommandID]] = ...
    """
    
    :return: 
    """
    CenterHorizontally: Final[ClassVar[CommandID]] = ...
    """
    
    :return: 
    """
    CenterVertically: Final[ClassVar[CommandID]] = ...
    """
    
    :return: 
    """
    Copy: Final[ClassVar[CommandID]] = ...
    """
    
    :return: 
    """
    Cut: Final[ClassVar[CommandID]] = ...
    """
    
    :return: 
    """
    Delete: Final[ClassVar[CommandID]] = ...
    """
    
    :return: 
    """
    DocumentOutline: Final[ClassVar[CommandID]] = ...
    """
    
    :return: 
    """
    F1Help: Final[ClassVar[CommandID]] = ...
    """
    
    :return: 
    """
    Group: Final[ClassVar[CommandID]] = ...
    """
    
    :return: 
    """
    HorizSpaceConcatenate: Final[ClassVar[CommandID]] = ...
    """
    
    :return: 
    """
    HorizSpaceDecrease: Final[ClassVar[CommandID]] = ...
    """
    
    :return: 
    """
    HorizSpaceIncrease: Final[ClassVar[CommandID]] = ...
    """
    
    :return: 
    """
    HorizSpaceMakeEqual: Final[ClassVar[CommandID]] = ...
    """
    
    :return: 
    """
    LineupIcons: Final[ClassVar[CommandID]] = ...
    """
    
    :return: 
    """
    LockControls: Final[ClassVar[CommandID]] = ...
    """
    
    :return: 
    """
    MultiLevelRedo: Final[ClassVar[CommandID]] = ...
    """
    
    :return: 
    """
    MultiLevelUndo: Final[ClassVar[CommandID]] = ...
    """
    
    :return: 
    """
    Paste: Final[ClassVar[CommandID]] = ...
    """
    
    :return: 
    """
    Properties: Final[ClassVar[CommandID]] = ...
    """
    
    :return: 
    """
    PropertiesWindow: Final[ClassVar[CommandID]] = ...
    """
    
    :return: 
    """
    Redo: Final[ClassVar[CommandID]] = ...
    """
    
    :return: 
    """
    Replace: Final[ClassVar[CommandID]] = ...
    """
    
    :return: 
    """
    SelectAll: Final[ClassVar[CommandID]] = ...
    """
    
    :return: 
    """
    SendBackward: Final[ClassVar[CommandID]] = ...
    """
    
    :return: 
    """
    SendToBack: Final[ClassVar[CommandID]] = ...
    """
    
    :return: 
    """
    ShowGrid: Final[ClassVar[CommandID]] = ...
    """
    
    :return: 
    """
    ShowLargeIcons: Final[ClassVar[CommandID]] = ...
    """
    
    :return: 
    """
    SizeToControl: Final[ClassVar[CommandID]] = ...
    """
    
    :return: 
    """
    SizeToControlHeight: Final[ClassVar[CommandID]] = ...
    """
    
    :return: 
    """
    SizeToControlWidth: Final[ClassVar[CommandID]] = ...
    """
    
    :return: 
    """
    SizeToFit: Final[ClassVar[CommandID]] = ...
    """
    
    :return: 
    """
    SizeToGrid: Final[ClassVar[CommandID]] = ...
    """
    
    :return: 
    """
    SnapToGrid: Final[ClassVar[CommandID]] = ...
    """
    
    :return: 
    """
    TabOrder: Final[ClassVar[CommandID]] = ...
    """
    
    :return: 
    """
    Undo: Final[ClassVar[CommandID]] = ...
    """
    
    :return: 
    """
    Ungroup: Final[ClassVar[CommandID]] = ...
    """
    
    :return: 
    """
    VerbFirst: Final[ClassVar[CommandID]] = ...
    """
    
    :return: 
    """
    VerbLast: Final[ClassVar[CommandID]] = ...
    """
    
    :return: 
    """
    VertSpaceConcatenate: Final[ClassVar[CommandID]] = ...
    """
    
    :return: 
    """
    VertSpaceDecrease: Final[ClassVar[CommandID]] = ...
    """
    
    :return: 
    """
    VertSpaceIncrease: Final[ClassVar[CommandID]] = ...
    """
    
    :return: 
    """
    VertSpaceMakeEqual: Final[ClassVar[CommandID]] = ...
    """
    
    :return: 
    """
    ViewCode: Final[ClassVar[CommandID]] = ...
    """
    
    :return: 
    """
    ViewGrid: Final[ClassVar[CommandID]] = ...
    """
    
    :return: 
    """
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
    def ToString(self) -> str:
        """

        :return:
        """

class StandardToolWindows(Object):
    """"""

    ObjectBrowser: Final[ClassVar[Guid]] = ...
    """
    
    :return: 
    """
    OutputWindow: Final[ClassVar[Guid]] = ...
    """
    
    :return: 
    """
    ProjectExplorer: Final[ClassVar[Guid]] = ...
    """
    
    :return: 
    """
    PropertyBrowser: Final[ClassVar[Guid]] = ...
    """
    
    :return: 
    """
    RelatedLinks: Final[ClassVar[Guid]] = ...
    """
    
    :return: 
    """
    ServerExplorer: Final[ClassVar[Guid]] = ...
    """
    
    :return: 
    """
    TaskList: Final[ClassVar[Guid]] = ...
    """
    
    :return: 
    """
    Toolbox: Final[ClassVar[Guid]] = ...
    """
    
    :return: 
    """
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
    def ToString(self) -> str:
        """

        :return:
        """

class TypeDescriptionProviderService(ABC, Object):
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
    @overload
    def GetProvider(self, instance: object) -> TypeDescriptionProvider:
        """

        :param instance:
        :return:
        """
    @overload
    def GetProvider(self, type: Type) -> TypeDescriptionProvider:
        """

        :param type:
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

class ViewTechnology(Enum):
    """"""

    Passthrough: ViewTechnology = ...
    """"""
    WindowsForms: ViewTechnology = ...
    """"""
    Default: ViewTechnology = ...
    """"""
