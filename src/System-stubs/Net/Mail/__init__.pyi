from __future__ import annotations

from abc import ABC
from typing import Callable
from typing import Generic
from typing import Iterator
from typing import Tuple
from typing import TypeVar
from typing import overload

from System import Array
from System import AsyncCallback
from System import Char
from System import Enum
from System import Exception
from System import Guid
from System import IAsyncResult
from System import IDisposable
from System import IntPtr
from System import Object
from System import Type
from System import Uri
from System import ValueType
from System import __ComObject
from System.Collections import ICollection
from System.Collections import IDictionary
from System.Collections import IEnumerable
from System.Collections import IEnumerator
from System.Collections import IList
from System.Collections.Generic import ICollection
from System.Collections.Generic import IEnumerable
from System.Collections.Generic import IList
from System.Collections.Generic import IReadOnlyCollection
from System.Collections.Generic import IReadOnlyList
from System.Collections.ObjectModel import Collection
from System.Collections.Specialized import NameValueCollection
from System.ComponentModel import AsyncCompletedEventArgs
from System.IO import SeekOrigin
from System.IO import Stream
from System.Net import Authorization
from System.Net import ICredentialsByHost
from System.Net import LazyAsyncResult
from System.Net import NetworkCredential
from System.Net import PooledStream
from System.Net import ServicePoint
from System.Net.Mime import BaseWriter
from System.Net.Mime import ContentDisposition
from System.Net.Mime import ContentType
from System.Net.Mime import TransferEncoding
from System.Reflection import MethodBase
from System.Runtime.InteropServices import _Attribute
from System.Runtime.InteropServices import _Exception
from System.Runtime.InteropServices.ComTypes import FILETIME
from System.Runtime.Remoting import ObjRef
from System.Runtime.Serialization import ISerializable
from System.Runtime.Serialization import SerializationInfo
from System.Runtime.Serialization import StreamingContext
from System.Security import CodeAccessPermission
from System.Security import IPermission
from System.Security import ISecurityEncodable
from System.Security import IStackWalk
from System.Security import SecurityElement
from System.Security.Authentication.ExtendedProtection import ChannelBinding
from System.Security.Cryptography.X509Certificates import X509CertificateCollection
from System.Security.Permissions import CodeAccessSecurityAttribute
from System.Security.Permissions import IUnrestrictedPermission
from System.Security.Permissions import PermissionState
from System.Security.Permissions import SecurityAction
from System.Text import Encoding
from System.Text import StringBuilder
from System.Threading import CancellationToken
from System.Threading import WaitHandle
from System.Threading.Tasks import Task

T = TypeVar("T")

class EventType(Generic[T]):
    def __iadd__(self, other: T): ...
    def __isub__(self, other: T): ...

class AlternateView(AttachmentBase, IDisposable):
    """"""

    @overload
    def __init__(self, contentStream: Stream):
        """

        :param contentStream:
        """
    @overload
    def __init__(self, fileName: str):
        """

        :param fileName:
        """
    @overload
    def __init__(self, contentStream: Stream, contentType: ContentType):
        """

        :param contentStream:
        :param contentType:
        """
    @overload
    def __init__(self, contentStream: Stream, mediaType: str):
        """

        :param contentStream:
        :param mediaType:
        """
    @overload
    def __init__(self, fileName: str, contentType: ContentType):
        """

        :param fileName:
        :param contentType:
        """
    @overload
    def __init__(self, fileName: str, mediaType: str):
        """

        :param fileName:
        :param mediaType:
        """
    @property
    def BaseUri(self) -> Uri:
        """

        :return:
        """
    @BaseUri.setter
    def BaseUri(self, value: Uri) -> None: ...
    @property
    def ContentId(self) -> str:
        """

        :return:
        """
    @ContentId.setter
    def ContentId(self, value: str) -> None: ...
    @property
    def ContentStream(self) -> Stream:
        """

        :return:
        """
    @property
    def ContentType(self) -> ContentType:
        """

        :return:
        """
    @ContentType.setter
    def ContentType(self, value: ContentType) -> None: ...
    @property
    def LinkedResources(self) -> LinkedResourceCollection:
        """

        :return:
        """
    @property
    def TransferEncoding(self) -> TransferEncoding:
        """

        :return:
        """
    @TransferEncoding.setter
    def TransferEncoding(self, value: TransferEncoding) -> None: ...
    @classmethod
    @overload
    def CreateAlternateViewFromString(cls, content: str) -> AlternateView:
        """

        :param content:
        :return:
        """
    @classmethod
    @overload
    def CreateAlternateViewFromString(cls, content: str, contentType: ContentType) -> AlternateView:
        """

        :param content:
        :param contentType:
        :return:
        """
    @classmethod
    @overload
    def CreateAlternateViewFromString(
        cls, content: str, contentEncoding: Encoding, mediaType: str
    ) -> AlternateView:
        """

        :param content:
        :param contentEncoding:
        :param mediaType:
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

class AlternateViewCollection(
    Collection[AlternateView],
    ICollection[AlternateView],
    IEnumerable[AlternateView],
    IList[AlternateView],
    IReadOnlyCollection[AlternateView],
    IReadOnlyList[AlternateView],
    ICollection,
    IEnumerable,
    IList,
    IDisposable,
):
    """"""

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
    def IsSynchronized(self) -> bool:
        """

        :return:
        """
    @property
    def Item(self) -> AlternateView:
        """

        :return:
        """
    @Item.setter
    def Item(self, value: AlternateView) -> None: ...
    @property
    def Item(self) -> AlternateView:
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
    def Add(self, item: AlternateView) -> None:
        """

        :param item:
        """
    @overload
    def Add(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def Clear(self) -> None:
        """"""
    @overload
    def Clear(self) -> None:
        """"""
    @overload
    def Contains(self, item: AlternateView) -> bool:
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
    def CopyTo(self, array: Array[AlternateView], arrayIndex: int) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
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
    def IndexOf(self, item: AlternateView) -> int:
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
    def Insert(self, index: int, item: AlternateView) -> None:
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
    def Remove(self, item: AlternateView) -> bool:
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
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def __contains__(self, value: AlternateView) -> bool:
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
    def __getitem__(self, index: int) -> AlternateView:
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
    def __getitem__(self, index: int) -> AlternateView:
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
    def __iter__(self) -> Iterator[AlternateView]:
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
    def __setitem__(self, index: int, value: AlternateView) -> None:
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

class Attachment(AttachmentBase, IDisposable):
    """"""

    @overload
    def __init__(self, fileName: str):
        """

        :param fileName:
        """
    @overload
    def __init__(self, contentStream: Stream, contentType: ContentType):
        """

        :param contentStream:
        :param contentType:
        """
    @overload
    def __init__(self, contentStream: Stream, name: str):
        """

        :param contentStream:
        :param name:
        """
    @overload
    def __init__(self, fileName: str, contentType: ContentType):
        """

        :param fileName:
        :param contentType:
        """
    @overload
    def __init__(self, fileName: str, mediaType: str):
        """

        :param fileName:
        :param mediaType:
        """
    @overload
    def __init__(self, contentStream: Stream, name: str, mediaType: str):
        """

        :param contentStream:
        :param name:
        :param mediaType:
        """
    @property
    def ContentDisposition(self) -> ContentDisposition:
        """

        :return:
        """
    @property
    def ContentId(self) -> str:
        """

        :return:
        """
    @ContentId.setter
    def ContentId(self, value: str) -> None: ...
    @property
    def ContentStream(self) -> Stream:
        """

        :return:
        """
    @property
    def ContentType(self) -> ContentType:
        """

        :return:
        """
    @ContentType.setter
    def ContentType(self, value: ContentType) -> None: ...
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def NameEncoding(self) -> Encoding:
        """

        :return:
        """
    @NameEncoding.setter
    def NameEncoding(self, value: Encoding) -> None: ...
    @property
    def TransferEncoding(self) -> TransferEncoding:
        """

        :return:
        """
    @TransferEncoding.setter
    def TransferEncoding(self, value: TransferEncoding) -> None: ...
    @classmethod
    @overload
    def CreateAttachmentFromString(cls, content: str, contentType: ContentType) -> Attachment:
        """

        :param content:
        :param contentType:
        :return:
        """
    @classmethod
    @overload
    def CreateAttachmentFromString(cls, content: str, name: str) -> Attachment:
        """

        :param content:
        :param name:
        :return:
        """
    @classmethod
    @overload
    def CreateAttachmentFromString(
        cls, content: str, name: str, contentEncoding: Encoding, mediaType: str
    ) -> Attachment:
        """

        :param content:
        :param name:
        :param contentEncoding:
        :param mediaType:
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

class AttachmentBase(ABC, Object, IDisposable):
    """"""

    @property
    def ContentId(self) -> str:
        """

        :return:
        """
    @ContentId.setter
    def ContentId(self, value: str) -> None: ...
    @property
    def ContentStream(self) -> Stream:
        """

        :return:
        """
    @property
    def ContentType(self) -> ContentType:
        """

        :return:
        """
    @ContentType.setter
    def ContentType(self, value: ContentType) -> None: ...
    @property
    def TransferEncoding(self) -> TransferEncoding:
        """

        :return:
        """
    @TransferEncoding.setter
    def TransferEncoding(self, value: TransferEncoding) -> None: ...
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

class AttachmentCollection(
    Collection[Attachment],
    ICollection[Attachment],
    IEnumerable[Attachment],
    IList[Attachment],
    IReadOnlyCollection[Attachment],
    IReadOnlyList[Attachment],
    ICollection,
    IEnumerable,
    IList,
    IDisposable,
):
    """"""

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
    def IsSynchronized(self) -> bool:
        """

        :return:
        """
    @property
    def Item(self) -> Attachment:
        """

        :return:
        """
    @Item.setter
    def Item(self, value: Attachment) -> None: ...
    @property
    def Item(self) -> Attachment:
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
    def Add(self, item: Attachment) -> None:
        """

        :param item:
        """
    @overload
    def Add(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def Clear(self) -> None:
        """"""
    @overload
    def Clear(self) -> None:
        """"""
    @overload
    def Contains(self, item: Attachment) -> bool:
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
    def CopyTo(self, array: Array[Attachment], arrayIndex: int) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
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
    def IndexOf(self, item: Attachment) -> int:
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
    def Insert(self, index: int, item: Attachment) -> None:
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
    def Remove(self, item: Attachment) -> bool:
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
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def __contains__(self, value: Attachment) -> bool:
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
    def __getitem__(self, index: int) -> Attachment:
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
    def __getitem__(self, index: int) -> Attachment:
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
    def __iter__(self) -> Iterator[Attachment]:
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
    def __setitem__(self, index: int, value: Attachment) -> None:
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

class AuthCommand(ABC, Object):
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

class BufferBuilder(Object):
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

class CheckCommand(ABC, Object):
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

class DataCommand(ABC, Object):
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

class DataStopCommand(ABC, Object):
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

class DeliveryNotificationOptions(Enum):
    """"""

    _None: DeliveryNotificationOptions = ...
    """"""
    OnSuccess: DeliveryNotificationOptions = ...
    """"""
    OnFailure: DeliveryNotificationOptions = ...
    """"""
    Delay: DeliveryNotificationOptions = ...
    """"""
    Never: DeliveryNotificationOptions = ...
    """"""

class DomainLiteralReader(ABC, Object):
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

class DotAtomReader(ABC, Object):
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

class EHelloCommand(ABC, Object):
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

class HelloCommand(ABC, Object):
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

class IMSAdminBase:
    """"""

    def AddKey(self, handle: IntPtr, Path: str) -> int:
        """

        :param handle:
        :param Path:
        :return:
        """
    def Backup(self, Location: str, Version: int, Flags: int) -> int:
        """

        :param Location:
        :param Version:
        :param Flags:
        :return:
        """
    def ChangePermissions(self, handle: IntPtr, TimeOut: int, AccessRequested: MBKeyAccess) -> None:
        """

        :param handle:
        :param TimeOut:
        :param AccessRequested:
        """
    def CloseKey(self, handle: IntPtr) -> int:
        """

        :param handle:
        :return:
        """
    def CopyData(
        self,
        sourcehandle: IntPtr,
        SourcePath: str,
        desthandle: IntPtr,
        DestPath: str,
        Attributes: int,
        UserType: int,
        DataType: int,
        CopyFlag: bool,
    ) -> int:
        """

        :param sourcehandle:
        :param SourcePath:
        :param desthandle:
        :param DestPath:
        :param Attributes:
        :param UserType:
        :param DataType:
        :param CopyFlag:
        :return:
        """
    def CopyKey(
        self,
        source: IntPtr,
        SourcePath: str,
        dest: IntPtr,
        DestPath: str,
        OverwriteFlag: bool,
        CopyFlag: bool,
    ) -> None:
        """

        :param source:
        :param SourcePath:
        :param dest:
        :param DestPath:
        :param OverwriteFlag:
        :param CopyFlag:
        """
    def DeleteAllData(self, handle: IntPtr, Path: str, UserType: int, DataType: int) -> None:
        """

        :param handle:
        :param Path:
        :param UserType:
        :param DataType:
        """
    def DeleteBackup(self, Location: str, Version: int) -> None:
        """

        :param Location:
        :param Version:
        """
    def DeleteChildKeys(self, handle: IntPtr, Path: str) -> None:
        """

        :param handle:
        :param Path:
        """
    def DeleteData(self, key: IntPtr, path: str, Identifier: int, DataType: int) -> int:
        """

        :param key:
        :param path:
        :param Identifier:
        :param DataType:
        :return:
        """
    def DeleteKey(self, handle: IntPtr, Path: str) -> int:
        """

        :param handle:
        :param Path:
        :return:
        """
    def EnumBackups(
        self, Location: str, Version: int, BackupTime: FILETIME, EnumIndex: int
    ) -> Tuple[None, str, int, FILETIME]:
        """

        :param Location:
        :param Version:
        :param BackupTime:
        :param EnumIndex:
        """
    def EnumData(
        self, key: IntPtr, path: str, data: MetadataRecord, EnumDataIndex: int, RequiredDataLen: int
    ) -> Tuple[int, int]:
        """

        :param key:
        :param path:
        :param data:
        :param EnumDataIndex:
        :param RequiredDataLen:
        :return:
        """
    def EnumKeys(self, handle: IntPtr, Path: str, Buffer: StringBuilder, EnumKeyIndex: int) -> int:
        """

        :param handle:
        :param Path:
        :param Buffer:
        :param EnumKeyIndex:
        :return:
        """
    def GetAllData(
        self,
        handle: IntPtr,
        Path: str,
        Attributes: int,
        UserType: int,
        DataType: int,
        NumDataEntries: int,
        DataSetNumber: int,
        BufferSize: int,
        buffer: IntPtr,
        RequiredBufferSize: int,
    ) -> Tuple[int, int, int, int]:
        """

        :param handle:
        :param Path:
        :param Attributes:
        :param UserType:
        :param DataType:
        :param NumDataEntries:
        :param DataSetNumber:
        :param BufferSize:
        :param buffer:
        :param RequiredBufferSize:
        :return:
        """
    def GetData(
        self, key: IntPtr, path: str, data: MetadataRecord, RequiredDataLen: int
    ) -> Tuple[int, int]:
        """

        :param key:
        :param path:
        :param data:
        :param RequiredDataLen:
        :return:
        """
    def GetDataPaths(
        self,
        handle: IntPtr,
        Path: str,
        Identifier: int,
        DataType: int,
        BufferSize: int,
        Buffer: Char,
        RequiredBufferSize: int,
    ) -> Tuple[None, Char, int]:
        """

        :param handle:
        :param Path:
        :param Identifier:
        :param DataType:
        :param BufferSize:
        :param Buffer:
        :param RequiredBufferSize:
        """
    def GetDataSetNumber(self, handle: IntPtr, Path: str, DataSetNumber: int) -> Tuple[None, int]:
        """

        :param handle:
        :param Path:
        :param DataSetNumber:
        """
    def GetHandleInfo(
        self, handle: IntPtr, Info: _METADATA_HANDLE_INFO
    ) -> Tuple[None, _METADATA_HANDLE_INFO]:
        """

        :param handle:
        :param Info:
        """
    def GetLastChangeTime(
        self, handle: IntPtr, Path: str, LastChangeTime: FILETIME, LocalTime: bool
    ) -> Tuple[int, FILETIME]:
        """

        :param handle:
        :param Path:
        :param LastChangeTime:
        :param LocalTime:
        :return:
        """
    def GetServerGuid(self) -> int:
        """

        :return:
        """
    def GetSystemChangeNumber(self, SystemChangeNumber: int) -> Tuple[None, int]:
        """

        :param SystemChangeNumber:
        """
    def KeyExchangePhase1(self) -> int:
        """

        :return:
        """
    def KeyExchangePhase2(self) -> int:
        """

        :return:
        """
    def OpenKey(
        self,
        handle: IntPtr,
        Path: str,
        AccessRequested: MBKeyAccess,
        TimeOut: int,
        NewHandle: IntPtr,
    ) -> Tuple[int, IntPtr]:
        """

        :param handle:
        :param Path:
        :param AccessRequested:
        :param TimeOut:
        :param NewHandle:
        :return:
        """
    def RenameKey(self, key: IntPtr, path: str, newName: str) -> None:
        """

        :param key:
        :param path:
        :param newName:
        """
    def Restore(self, Location: str, Version: int, Flags: int) -> int:
        """

        :param Location:
        :param Version:
        :param Flags:
        :return:
        """
    def SaveData(self) -> None:
        """"""
    def SetData(self, key: IntPtr, path: str, data: MetadataRecord) -> int:
        """

        :param key:
        :param path:
        :param data:
        :return:
        """
    def SetLastChangeTime(
        self, handle: IntPtr, Path: str, LastChangeTime: FILETIME, LocalTime: bool
    ) -> Tuple[None, FILETIME]:
        """

        :param handle:
        :param Path:
        :param LastChangeTime:
        :param LocalTime:
        """
    def UnmarshalInterface(self, interf: IMSAdminBase) -> Tuple[int, IMSAdminBase]:
        """

        :param interf:
        :return:
        """

class ISmtpAuthenticationModule:
    """"""

    @property
    def AuthenticationType(self) -> str:
        """

        :return:
        """
    def Authenticate(
        self,
        challenge: str,
        credentials: NetworkCredential,
        sessionCookie: object,
        spn: str,
        channelBindingToken: ChannelBinding,
    ) -> Authorization:
        """

        :param challenge:
        :param credentials:
        :param sessionCookie:
        :param spn:
        :param channelBindingToken:
        :return:
        """
    def CloseContext(self, sessionCookie: object) -> None:
        """

        :param sessionCookie:
        """

class IisPickupDirectory(ABC, Object):
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

class LineInfo(ValueType):
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

class LinkedResource(AttachmentBase, IDisposable):
    """"""

    @overload
    def __init__(self, contentStream: Stream):
        """

        :param contentStream:
        """
    @overload
    def __init__(self, fileName: str):
        """

        :param fileName:
        """
    @overload
    def __init__(self, contentStream: Stream, contentType: ContentType):
        """

        :param contentStream:
        :param contentType:
        """
    @overload
    def __init__(self, contentStream: Stream, mediaType: str):
        """

        :param contentStream:
        :param mediaType:
        """
    @overload
    def __init__(self, fileName: str, contentType: ContentType):
        """

        :param fileName:
        :param contentType:
        """
    @overload
    def __init__(self, fileName: str, mediaType: str):
        """

        :param fileName:
        :param mediaType:
        """
    @property
    def ContentId(self) -> str:
        """

        :return:
        """
    @ContentId.setter
    def ContentId(self, value: str) -> None: ...
    @property
    def ContentLink(self) -> Uri:
        """

        :return:
        """
    @ContentLink.setter
    def ContentLink(self, value: Uri) -> None: ...
    @property
    def ContentStream(self) -> Stream:
        """

        :return:
        """
    @property
    def ContentType(self) -> ContentType:
        """

        :return:
        """
    @ContentType.setter
    def ContentType(self, value: ContentType) -> None: ...
    @property
    def TransferEncoding(self) -> TransferEncoding:
        """

        :return:
        """
    @TransferEncoding.setter
    def TransferEncoding(self, value: TransferEncoding) -> None: ...
    @classmethod
    @overload
    def CreateLinkedResourceFromString(cls, content: str) -> LinkedResource:
        """

        :param content:
        :return:
        """
    @classmethod
    @overload
    def CreateLinkedResourceFromString(
        cls, content: str, contentType: ContentType
    ) -> LinkedResource:
        """

        :param content:
        :param contentType:
        :return:
        """
    @classmethod
    @overload
    def CreateLinkedResourceFromString(
        cls, content: str, contentEncoding: Encoding, mediaType: str
    ) -> LinkedResource:
        """

        :param content:
        :param contentEncoding:
        :param mediaType:
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

class LinkedResourceCollection(
    Collection[LinkedResource],
    ICollection[LinkedResource],
    IEnumerable[LinkedResource],
    IList[LinkedResource],
    IReadOnlyCollection[LinkedResource],
    IReadOnlyList[LinkedResource],
    ICollection,
    IEnumerable,
    IList,
    IDisposable,
):
    """"""

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
    def IsSynchronized(self) -> bool:
        """

        :return:
        """
    @property
    def Item(self) -> LinkedResource:
        """

        :return:
        """
    @Item.setter
    def Item(self, value: LinkedResource) -> None: ...
    @property
    def Item(self) -> LinkedResource:
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
    def Add(self, item: LinkedResource) -> None:
        """

        :param item:
        """
    @overload
    def Add(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def Clear(self) -> None:
        """"""
    @overload
    def Clear(self) -> None:
        """"""
    @overload
    def Contains(self, item: LinkedResource) -> bool:
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
    def CopyTo(self, array: Array[LinkedResource], arrayIndex: int) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
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
    def IndexOf(self, item: LinkedResource) -> int:
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
    def Insert(self, index: int, item: LinkedResource) -> None:
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
    def Remove(self, item: LinkedResource) -> bool:
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
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def __contains__(self, value: LinkedResource) -> bool:
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
    def __getitem__(self, index: int) -> LinkedResource:
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
    def __getitem__(self, index: int) -> LinkedResource:
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
    def __iter__(self) -> Iterator[LinkedResource]:
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
    def __setitem__(self, index: int, value: LinkedResource) -> None:
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

class MBDataType(Enum):
    """"""

    All: MBDataType = ...
    """"""
    Dword: MBDataType = ...
    """"""
    String: MBDataType = ...
    """"""
    Binary: MBDataType = ...
    """"""
    StringExpand: MBDataType = ...
    """"""
    MultiString: MBDataType = ...
    """"""

class MBErrors(Enum):
    """"""

    DuplicateNameWarning: MBErrors = ...
    """"""
    InvalidDataWarning: MBErrors = ...
    """"""
    PathNotFound: MBErrors = ...
    """"""
    AccessDenied: MBErrors = ...
    """"""
    InvalidParameter: MBErrors = ...
    """"""
    InsufficientBuffer: MBErrors = ...
    """"""
    PathBusy: MBErrors = ...
    """"""
    AlreadyExists: MBErrors = ...
    """"""
    NoMoreItems: MBErrors = ...
    """"""
    DataNotFound: MBErrors = ...
    """"""
    InvalidVersion: MBErrors = ...
    """"""

class MBKeyAccess(Enum):
    """"""

    Read: MBKeyAccess = ...
    """"""
    Write: MBKeyAccess = ...
    """"""

class MBUserType(Enum):
    """"""

    Other: MBUserType = ...
    """"""
    Server: MBUserType = ...
    """"""
    File: MBUserType = ...
    """"""
    Wam: MBUserType = ...
    """"""
    Asp: MBUserType = ...
    """"""

class MSAdminBase(__ComObject):
    """"""

    def __init__(self):
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """

        :param requestedType:
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

class MailAddress(Object):
    """"""

    @overload
    def __init__(self, address: str):
        """

        :param address:
        """
    @overload
    def __init__(self, address: str, displayName: str):
        """

        :param address:
        :param displayName:
        """
    @overload
    def __init__(self, address: str, displayName: str, displayNameEncoding: Encoding):
        """

        :param address:
        :param displayName:
        :param displayNameEncoding:
        """
    @property
    def Address(self) -> str:
        """

        :return:
        """
    @property
    def DisplayName(self) -> str:
        """

        :return:
        """
    @property
    def Host(self) -> str:
        """

        :return:
        """
    @property
    def User(self) -> str:
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

class MailAddressCollection(
    Collection[MailAddress],
    ICollection[MailAddress],
    IEnumerable[MailAddress],
    IList[MailAddress],
    IReadOnlyCollection[MailAddress],
    IReadOnlyList[MailAddress],
    ICollection,
    IEnumerable,
    IList,
):
    """"""

    def __init__(self):
        """"""
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
    def IsSynchronized(self) -> bool:
        """

        :return:
        """
    @property
    def Item(self) -> MailAddress:
        """

        :return:
        """
    @Item.setter
    def Item(self, value: MailAddress) -> None: ...
    @property
    def Item(self) -> MailAddress:
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
    def Add(self, item: MailAddress) -> None:
        """

        :param item:
        """
    @overload
    def Add(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def Add(self, addresses: str) -> None:
        """

        :param addresses:
        """
    @overload
    def Clear(self) -> None:
        """"""
    @overload
    def Clear(self) -> None:
        """"""
    @overload
    def Contains(self, item: MailAddress) -> bool:
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
    def CopyTo(self, array: Array[MailAddress], arrayIndex: int) -> None:
        """"""
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
    def IndexOf(self, item: MailAddress) -> int:
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
    def Insert(self, index: int, item: MailAddress) -> None:
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
    def Remove(self, item: MailAddress) -> bool:
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
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def __contains__(self, value: MailAddress) -> bool:
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
    def __getitem__(self, index: int) -> MailAddress:
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
    def __getitem__(self, index: int) -> MailAddress:
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
    def __iter__(self) -> Iterator[MailAddress]:
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
    def __setitem__(self, index: int, value: MailAddress) -> None:
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

class MailAddressParser(ABC, Object):
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

class MailCommand(ABC, Object):
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

class MailHeaderID(Enum):
    """"""

    Bcc: MailHeaderID = ...
    """"""
    Cc: MailHeaderID = ...
    """"""
    Comments: MailHeaderID = ...
    """"""
    ContentDescription: MailHeaderID = ...
    """"""
    ContentDisposition: MailHeaderID = ...
    """"""
    ContentID: MailHeaderID = ...
    """"""
    ContentLocation: MailHeaderID = ...
    """"""
    ContentTransferEncoding: MailHeaderID = ...
    """"""
    ContentType: MailHeaderID = ...
    """"""
    Date: MailHeaderID = ...
    """"""
    From: MailHeaderID = ...
    """"""
    Importance: MailHeaderID = ...
    """"""
    InReplyTo: MailHeaderID = ...
    """"""
    Keywords: MailHeaderID = ...
    """"""
    Max: MailHeaderID = ...
    """"""
    MessageID: MailHeaderID = ...
    """"""
    MimeVersion: MailHeaderID = ...
    """"""
    Priority: MailHeaderID = ...
    """"""
    References: MailHeaderID = ...
    """"""
    ReplyTo: MailHeaderID = ...
    """"""
    ResentBcc: MailHeaderID = ...
    """"""
    ResentCc: MailHeaderID = ...
    """"""
    ResentDate: MailHeaderID = ...
    """"""
    ResentFrom: MailHeaderID = ...
    """"""
    ResentMessageID: MailHeaderID = ...
    """"""
    ResentSender: MailHeaderID = ...
    """"""
    ResentTo: MailHeaderID = ...
    """"""
    Sender: MailHeaderID = ...
    """"""
    Subject: MailHeaderID = ...
    """"""
    To: MailHeaderID = ...
    """"""
    XPriority: MailHeaderID = ...
    """"""
    XReceiver: MailHeaderID = ...
    """"""
    XSender: MailHeaderID = ...
    """"""
    ZMaxEnumValue: MailHeaderID = ...
    """"""
    Unknown: MailHeaderID = ...
    """"""

class MailHeaderInfo(ABC, Object):
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

class MailMessage(Object, IDisposable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, _from: MailAddress, to: MailAddress):
        """

        :param _from:
        :param to:
        """
    @overload
    def __init__(self, _from: str, to: str):
        """

        :param _from:
        :param to:
        """
    @overload
    def __init__(self, _from: str, to: str, subject: str, body: str):
        """

        :param _from:
        :param to:
        :param subject:
        :param body:
        """
    @property
    def AlternateViews(self) -> AlternateViewCollection:
        """

        :return:
        """
    @property
    def Attachments(self) -> AttachmentCollection:
        """

        :return:
        """
    @property
    def Bcc(self) -> MailAddressCollection:
        """

        :return:
        """
    @property
    def Body(self) -> str:
        """

        :return:
        """
    @Body.setter
    def Body(self, value: str) -> None: ...
    @property
    def BodyEncoding(self) -> Encoding:
        """

        :return:
        """
    @BodyEncoding.setter
    def BodyEncoding(self, value: Encoding) -> None: ...
    @property
    def BodyTransferEncoding(self) -> TransferEncoding:
        """

        :return:
        """
    @BodyTransferEncoding.setter
    def BodyTransferEncoding(self, value: TransferEncoding) -> None: ...
    @property
    def CC(self) -> MailAddressCollection:
        """

        :return:
        """
    @property
    def DeliveryNotificationOptions(self) -> DeliveryNotificationOptions:
        """

        :return:
        """
    @DeliveryNotificationOptions.setter
    def DeliveryNotificationOptions(self, value: DeliveryNotificationOptions) -> None: ...
    @property
    def From(self) -> MailAddress:
        """

        :return:
        """
    @From.setter
    def From(self, value: MailAddress) -> None: ...
    @property
    def Headers(self) -> NameValueCollection:
        """

        :return:
        """
    @property
    def HeadersEncoding(self) -> Encoding:
        """

        :return:
        """
    @HeadersEncoding.setter
    def HeadersEncoding(self, value: Encoding) -> None: ...
    @property
    def IsBodyHtml(self) -> bool:
        """

        :return:
        """
    @IsBodyHtml.setter
    def IsBodyHtml(self, value: bool) -> None: ...
    @property
    def Priority(self) -> MailPriority:
        """

        :return:
        """
    @Priority.setter
    def Priority(self, value: MailPriority) -> None: ...
    @property
    def ReplyTo(self) -> MailAddress:
        """

        :return:
        """
    @ReplyTo.setter
    def ReplyTo(self, value: MailAddress) -> None: ...
    @property
    def ReplyToList(self) -> MailAddressCollection:
        """

        :return:
        """
    @property
    def Sender(self) -> MailAddress:
        """

        :return:
        """
    @Sender.setter
    def Sender(self, value: MailAddress) -> None: ...
    @property
    def Subject(self) -> str:
        """

        :return:
        """
    @Subject.setter
    def Subject(self, value: str) -> None: ...
    @property
    def SubjectEncoding(self) -> Encoding:
        """

        :return:
        """
    @SubjectEncoding.setter
    def SubjectEncoding(self, value: Encoding) -> None: ...
    @property
    def To(self) -> MailAddressCollection:
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

class MailPriority(Enum):
    """"""

    Normal: MailPriority = ...
    """"""
    Low: MailPriority = ...
    """"""
    High: MailPriority = ...
    """"""

class MailWriter(BaseWriter):
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

class Message(Object):
    """"""

    @property
    def Priority(self) -> MailPriority:
        """

        :return:
        """
    @Priority.setter
    def Priority(self, value: MailPriority) -> None: ...
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

class MetadataRecord(ValueType):
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

class PropertyName(Enum):
    """"""

    Invalid: PropertyName = ...
    """"""
    ServerState: PropertyName = ...
    """"""
    PickupDirectory: PropertyName = ...
    """"""

class QuotedPairReader(ABC, Object):
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

class QuotedStringFormatReader(ABC, Object):
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

class ReadLinesCommand(ABC, Object):
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

class RecipientCommand(ABC, Object):
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

class RecipientLocationType(Enum):
    """"""

    Local: RecipientLocationType = ...
    """"""
    Unknown: RecipientLocationType = ...
    """"""
    NotLocal: RecipientLocationType = ...
    """"""
    WillForward: RecipientLocationType = ...
    """"""
    Ambiguous: RecipientLocationType = ...
    """"""

SendCompletedEventHandler: Callable[[object, AsyncCompletedEventArgs], None] = ...
"""

:param sender: 
:param e: 
"""

class SendMailAsyncResult(LazyAsyncResult, IAsyncResult):
    """"""

    @property
    def AsyncState(self) -> object:
        """

        :return:
        """
    @property
    def AsyncWaitHandle(self) -> WaitHandle:
        """

        :return:
        """
    @property
    def CompletedSynchronously(self) -> bool:
        """

        :return:
        """
    @property
    def IsCompleted(self) -> bool:
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

class ServerState(Enum):
    """"""

    Starting: ServerState = ...
    """"""
    Started: ServerState = ...
    """"""
    Stopping: ServerState = ...
    """"""
    Stopped: ServerState = ...
    """"""
    Pausing: ServerState = ...
    """"""
    Paused: ServerState = ...
    """"""
    Continuing: ServerState = ...
    """"""

class SmtpAccess(Enum):
    """"""

    _None: SmtpAccess = ...
    """"""
    Connect: SmtpAccess = ...
    """"""
    ConnectToUnrestrictedPort: SmtpAccess = ...
    """"""

class SmtpAuthenticationManager(ABC, Object):
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

class SmtpClient(Object, IDisposable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, host: str):
        """

        :param host:
        """
    @overload
    def __init__(self, host: str, port: int):
        """

        :param host:
        :param port:
        """
    @property
    def ClientCertificates(self) -> X509CertificateCollection:
        """

        :return:
        """
    @property
    def Credentials(self) -> ICredentialsByHost:
        """

        :return:
        """
    @Credentials.setter
    def Credentials(self, value: ICredentialsByHost) -> None: ...
    @property
    def DeliveryFormat(self) -> SmtpDeliveryFormat:
        """

        :return:
        """
    @DeliveryFormat.setter
    def DeliveryFormat(self, value: SmtpDeliveryFormat) -> None: ...
    @property
    def DeliveryMethod(self) -> SmtpDeliveryMethod:
        """

        :return:
        """
    @DeliveryMethod.setter
    def DeliveryMethod(self, value: SmtpDeliveryMethod) -> None: ...
    @property
    def EnableSsl(self) -> bool:
        """

        :return:
        """
    @EnableSsl.setter
    def EnableSsl(self, value: bool) -> None: ...
    @property
    def Host(self) -> str:
        """

        :return:
        """
    @Host.setter
    def Host(self, value: str) -> None: ...
    @property
    def PickupDirectoryLocation(self) -> str:
        """

        :return:
        """
    @PickupDirectoryLocation.setter
    def PickupDirectoryLocation(self, value: str) -> None: ...
    @property
    def Port(self) -> int:
        """

        :return:
        """
    @Port.setter
    def Port(self, value: int) -> None: ...
    @property
    def ServicePoint(self) -> ServicePoint:
        """

        :return:
        """
    @property
    def TargetName(self) -> str:
        """

        :return:
        """
    @TargetName.setter
    def TargetName(self, value: str) -> None: ...
    @property
    def Timeout(self) -> int:
        """

        :return:
        """
    @Timeout.setter
    def Timeout(self, value: int) -> None: ...
    @property
    def UseDefaultCredentials(self) -> bool:
        """

        :return:
        """
    @UseDefaultCredentials.setter
    def UseDefaultCredentials(self, value: bool) -> None: ...
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
    @overload
    def Send(self, message: MailMessage) -> None:
        """

        :param message:
        """
    @overload
    def Send(self, _from: str, recipients: str, subject: str, body: str) -> None:
        """

        :param _from:
        :param recipients:
        :param subject:
        :param body:
        """
    @overload
    def SendAsync(self, message: MailMessage, userToken: object) -> None:
        """

        :param message:
        :param userToken:
        """
    @overload
    def SendAsync(
        self, _from: str, recipients: str, subject: str, body: str, userToken: object
    ) -> None:
        """

        :param _from:
        :param recipients:
        :param subject:
        :param body:
        :param userToken:
        """
    def SendAsyncCancel(self) -> None:
        """"""
    @overload
    def SendMailAsync(self, message: MailMessage) -> Task:
        """

        :param message:
        :return:
        """
    @overload
    def SendMailAsync(self, _from: str, recipients: str, subject: str, body: str) -> Task:
        """

        :param _from:
        :param recipients:
        :param subject:
        :param body:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    SendCompleted: EventType[SendCompletedEventHandler] = ...
    """"""

class SmtpCommands(ABC, Object):
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

class SmtpConnection(Object):
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

class SmtpDeliveryFormat(Enum):
    """"""

    SevenBit: SmtpDeliveryFormat = ...
    """"""
    International: SmtpDeliveryFormat = ...
    """"""

class SmtpDeliveryMethod(Enum):
    """"""

    Network: SmtpDeliveryMethod = ...
    """"""
    SpecifiedPickupDirectory: SmtpDeliveryMethod = ...
    """"""
    PickupDirectoryFromIis: SmtpDeliveryMethod = ...
    """"""

class SmtpDigestAuthenticationModule(Object, ISmtpAuthenticationModule):
    """"""

    @property
    def AuthenticationType(self) -> str:
        """

        :return:
        """
    def Authenticate(
        self,
        challenge: str,
        credentials: NetworkCredential,
        sessionCookie: object,
        spn: str,
        channelBindingToken: ChannelBinding,
    ) -> Authorization:
        """

        :param challenge:
        :param credentials:
        :param sessionCookie:
        :param spn:
        :param channelBindingToken:
        :return:
        """
    def CloseContext(self, sessionCookie: object) -> None:
        """

        :param sessionCookie:
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

class SmtpException(Exception, _Exception, ISerializable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, statusCode: SmtpStatusCode):
        """

        :param statusCode:
        """
    @overload
    def __init__(self, message: str):
        """

        :param message:
        """
    @overload
    def __init__(self, statusCode: SmtpStatusCode, message: str):
        """

        :param statusCode:
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
    def StatusCode(self) -> SmtpStatusCode:
        """

        :return:
        """
    @StatusCode.setter
    def StatusCode(self, value: SmtpStatusCode) -> None: ...
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

class SmtpFailedRecipientException(SmtpException, _Exception, ISerializable):
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
    def __init__(self, statusCode: SmtpStatusCode, failedRecipient: str):
        """

        :param statusCode:
        :param failedRecipient:
        """
    @overload
    def __init__(self, message: str, innerException: Exception):
        """

        :param message:
        :param innerException:
        """
    @overload
    def __init__(self, statusCode: SmtpStatusCode, failedRecipient: str, serverResponse: str):
        """

        :param statusCode:
        :param failedRecipient:
        :param serverResponse:
        """
    @overload
    def __init__(self, message: str, failedRecipient: str, innerException: Exception):
        """

        :param message:
        :param failedRecipient:
        :param innerException:
        """
    @property
    def Data(self) -> IDictionary:
        """

        :return:
        """
    @property
    def FailedRecipient(self) -> str:
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
    def StatusCode(self) -> SmtpStatusCode:
        """

        :return:
        """
    @StatusCode.setter
    def StatusCode(self, value: SmtpStatusCode) -> None: ...
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

class SmtpFailedRecipientsException(SmtpFailedRecipientException, _Exception, ISerializable):
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
    def __init__(self, message: str, innerExceptions: Array[SmtpFailedRecipientException]):
        """

        :param message:
        :param innerExceptions:
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
    def FailedRecipient(self) -> str:
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
    def InnerExceptions(self) -> Array[SmtpFailedRecipientException]:
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
    def StatusCode(self) -> SmtpStatusCode:
        """

        :return:
        """
    @StatusCode.setter
    def StatusCode(self, value: SmtpStatusCode) -> None: ...
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

class SmtpLoginAuthenticationModule(Object, ISmtpAuthenticationModule):
    """"""

    @property
    def AuthenticationType(self) -> str:
        """

        :return:
        """
    def Authenticate(
        self,
        challenge: str,
        credentials: NetworkCredential,
        sessionCookie: object,
        spn: str,
        channelBindingToken: ChannelBinding,
    ) -> Authorization:
        """

        :param challenge:
        :param credentials:
        :param sessionCookie:
        :param spn:
        :param channelBindingToken:
        :return:
        """
    def CloseContext(self, sessionCookie: object) -> None:
        """

        :param sessionCookie:
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

class SmtpNegotiateAuthenticationModule(Object, ISmtpAuthenticationModule):
    """"""

    @property
    def AuthenticationType(self) -> str:
        """

        :return:
        """
    def Authenticate(
        self,
        challenge: str,
        credentials: NetworkCredential,
        sessionCookie: object,
        spn: str,
        channelBindingToken: ChannelBinding,
    ) -> Authorization:
        """

        :param challenge:
        :param credentials:
        :param sessionCookie:
        :param spn:
        :param channelBindingToken:
        :return:
        """
    def CloseContext(self, sessionCookie: object) -> None:
        """

        :param sessionCookie:
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

class SmtpNtlmAuthenticationModule(Object, ISmtpAuthenticationModule):
    """"""

    @property
    def AuthenticationType(self) -> str:
        """

        :return:
        """
    def Authenticate(
        self,
        challenge: str,
        credentials: NetworkCredential,
        sessionCookie: object,
        spn: str,
        channelBindingToken: ChannelBinding,
    ) -> Authorization:
        """

        :param challenge:
        :param credentials:
        :param sessionCookie:
        :param spn:
        :param channelBindingToken:
        :return:
        """
    def CloseContext(self, sessionCookie: object) -> None:
        """

        :param sessionCookie:
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

class SmtpPermission(
    CodeAccessPermission, IUnrestrictedPermission, IPermission, ISecurityEncodable, IStackWalk
):
    """"""

    @overload
    def __init__(self, access: SmtpAccess):
        """

        :param access:
        """
    @overload
    def __init__(self, state: PermissionState):
        """

        :param state:
        """
    @overload
    def __init__(self, unrestricted: bool):
        """

        :param unrestricted:
        """
    @property
    def Access(self) -> SmtpAccess:
        """

        :return:
        """
    def AddPermission(self, access: SmtpAccess) -> None:
        """

        :param access:
        """
    def Assert(self) -> None:
        """"""
    def Copy(self) -> IPermission:
        """

        :return:
        """
    @overload
    def Demand(self) -> None:
        """"""
    @overload
    def Demand(self) -> None:
        """"""
    def Deny(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def FromXml(self, e: SecurityElement) -> None:
        """

        :param e:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def Intersect(self, target: IPermission) -> IPermission:
        """

        :param target:
        :return:
        """
    def IsSubsetOf(self, target: IPermission) -> bool:
        """

        :param target:
        :return:
        """
    def IsUnrestricted(self) -> bool:
        """

        :return:
        """
    def PermitOnly(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """
    def ToXml(self) -> SecurityElement:
        """

        :return:
        """
    def Union(self, target: IPermission) -> IPermission:
        """

        :param target:
        :return:
        """

class SmtpPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    """"""

    def __init__(self, action: SecurityAction):
        """

        :param action:
        """
    @property
    def Access(self) -> str:
        """

        :return:
        """
    @Access.setter
    def Access(self, value: str) -> None: ...
    @property
    def Action(self) -> SecurityAction:
        """

        :return:
        """
    @Action.setter
    def Action(self, value: SecurityAction) -> None: ...
    @property
    def TypeId(self) -> object:
        """

        :return:
        """
    @property
    def Unrestricted(self) -> bool:
        """

        :return:
        """
    @Unrestricted.setter
    def Unrestricted(self, value: bool) -> None: ...
    def CreatePermission(self) -> IPermission:
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

class SmtpPooledStream(PooledStream, IDisposable):
    """"""

    @property
    def CanRead(self) -> bool:
        """

        :return:
        """
    @property
    def CanSeek(self) -> bool:
        """

        :return:
        """
    @property
    def CanTimeout(self) -> bool:
        """

        :return:
        """
    @property
    def CanWrite(self) -> bool:
        """

        :return:
        """
    @property
    def Length(self) -> int:
        """

        :return:
        """
    @property
    def Position(self) -> int:
        """

        :return:
        """
    @Position.setter
    def Position(self, value: int) -> None: ...
    @property
    def ReadTimeout(self) -> int:
        """

        :return:
        """
    @ReadTimeout.setter
    def ReadTimeout(self, value: int) -> None: ...
    @property
    def WriteTimeout(self) -> int:
        """

        :return:
        """
    @WriteTimeout.setter
    def WriteTimeout(self, value: int) -> None: ...
    def BeginRead(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """

        :param buffer:
        :param offset:
        :param count:
        :param callback:
        :param state:
        :return:
        """
    def BeginWrite(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """

        :param buffer:
        :param offset:
        :param count:
        :param callback:
        :param state:
        :return:
        """
    @overload
    def Close(self) -> None:
        """"""
    @overload
    def Close(self, timeout: int) -> None:
        """

        :param timeout:
        """
    @overload
    def CopyTo(self, destination: Stream) -> None:
        """

        :param destination:
        """
    @overload
    def CopyTo(self, destination: Stream, bufferSize: int) -> None:
        """

        :param destination:
        :param bufferSize:
        """
    @overload
    def CopyToAsync(self, destination: Stream) -> Task:
        """

        :param destination:
        :return:
        """
    @overload
    def CopyToAsync(self, destination: Stream, bufferSize: int) -> Task:
        """

        :param destination:
        :param bufferSize:
        :return:
        """
    @overload
    def CopyToAsync(
        self, destination: Stream, bufferSize: int, cancellationToken: CancellationToken
    ) -> Task:
        """

        :param destination:
        :param bufferSize:
        :param cancellationToken:
        :return:
        """
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """

        :param requestedType:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    def EndRead(self, asyncResult: IAsyncResult) -> int:
        """

        :param asyncResult:
        :return:
        """
    def EndWrite(self, asyncResult: IAsyncResult) -> None:
        """

        :param asyncResult:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def Flush(self) -> None:
        """"""
    @overload
    def FlushAsync(self) -> Task:
        """

        :return:
        """
    @overload
    def FlushAsync(self, cancellationToken: CancellationToken) -> Task:
        """

        :param cancellationToken:
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
    def Read(self, buffer: Array[int], offset: int, count: int) -> Tuple[int, Array[int]]:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def ReadAsync(self, buffer: Array[int], offset: int, count: int) -> Task[int]:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def ReadAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task[int]:
        """

        :param buffer:
        :param offset:
        :param count:
        :param cancellationToken:
        :return:
        """
    def ReadByte(self) -> int:
        """

        :return:
        """
    def Seek(self, offset: int, origin: SeekOrigin) -> int:
        """

        :param offset:
        :param origin:
        :return:
        """
    def SetLength(self, value: int) -> None:
        """

        :param value:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Write(self, buffer: Array[int], offset: int, count: int) -> None:
        """

        :param buffer:
        :param offset:
        :param count:
        """
    @overload
    def WriteAsync(self, buffer: Array[int], offset: int, count: int) -> Task:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def WriteAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task:
        """

        :param buffer:
        :param offset:
        :param count:
        :param cancellationToken:
        :return:
        """
    def WriteByte(self, value: int) -> None:
        """

        :param value:
        """

class SmtpReplyReader(Object):
    """"""

    def Close(self) -> None:
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

class SmtpReplyReaderFactory(Object):
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

class SmtpStatusCode(Enum):
    """"""

    SystemStatus: SmtpStatusCode = ...
    """"""
    HelpMessage: SmtpStatusCode = ...
    """"""
    ServiceReady: SmtpStatusCode = ...
    """"""
    ServiceClosingTransmissionChannel: SmtpStatusCode = ...
    """"""
    Ok: SmtpStatusCode = ...
    """"""
    UserNotLocalWillForward: SmtpStatusCode = ...
    """"""
    CannotVerifyUserWillAttemptDelivery: SmtpStatusCode = ...
    """"""
    StartMailInput: SmtpStatusCode = ...
    """"""
    ServiceNotAvailable: SmtpStatusCode = ...
    """"""
    MailboxBusy: SmtpStatusCode = ...
    """"""
    LocalErrorInProcessing: SmtpStatusCode = ...
    """"""
    InsufficientStorage: SmtpStatusCode = ...
    """"""
    ClientNotPermitted: SmtpStatusCode = ...
    """"""
    CommandUnrecognized: SmtpStatusCode = ...
    """"""
    SyntaxError: SmtpStatusCode = ...
    """"""
    CommandNotImplemented: SmtpStatusCode = ...
    """"""
    BadCommandSequence: SmtpStatusCode = ...
    """"""
    CommandParameterNotImplemented: SmtpStatusCode = ...
    """"""
    MustIssueStartTlsFirst: SmtpStatusCode = ...
    """"""
    MailboxUnavailable: SmtpStatusCode = ...
    """"""
    UserNotLocalTryAlternatePath: SmtpStatusCode = ...
    """"""
    ExceededStorageAllocation: SmtpStatusCode = ...
    """"""
    MailboxNameNotAllowed: SmtpStatusCode = ...
    """"""
    TransactionFailed: SmtpStatusCode = ...
    """"""
    GeneralFailure: SmtpStatusCode = ...
    """"""

class SmtpTransport(Object):
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

class StartTlsCommand(ABC, Object):
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

class SupportedAuth(Enum):
    """"""

    _None: SupportedAuth = ...
    """"""
    Login: SupportedAuth = ...
    """"""
    NTLM: SupportedAuth = ...
    """"""
    GSSAPI: SupportedAuth = ...
    """"""
    WDigest: SupportedAuth = ...
    """"""

class WhitespaceReader(ABC, Object):
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

class _METADATA_HANDLE_INFO(Object):
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
