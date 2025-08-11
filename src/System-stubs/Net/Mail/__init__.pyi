"""Automatically generated stubs for C# namespace: System.Net.Mail."""

from abc import ABC
from collections.abc import Callable
from collections.abc import Iterator
from typing import Self
from typing import overload

from System import Array
from System import AsyncCallback
from System import Char
from System import Enum
from System import Exception
from System import Guid
from System import IAsyncResult
from System import IDisposable
from System import Int32
from System import IntPtr
from System import Object
from System import String
from System import Type
from System import UInt32
from System import Uri
from System import ValueType
from System import __ComObject
from System.Collections import IDictionary
from System.Collections.Generic import ICollection
from System.Collections.Generic import IEnumerable
from System.Collections.Generic import IEnumerator
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

class EventType[T]:
    def __iadd__(self, other: T) -> Self: ...
    def __isub__(self, other: T) -> Self: ...

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class AlternateView(AttachmentBase, IDisposable):
    """"""
    @overload
    def __init__(self, fileName: str) -> None:
        """"""
    @overload
    def __init__(self, fileName: str, mediaType: str) -> None:
        """"""
    @overload
    def __init__(self, fileName: str, contentType: ContentType) -> None:
        """"""
    @overload
    def __init__(self, contentStream: Stream) -> None:
        """"""
    @overload
    def __init__(self, contentStream: Stream, mediaType: str) -> None:
        """"""
    @overload
    def __init__(self, contentStream: Stream, contentType: ContentType) -> None:
        """"""
    @property
    def BaseUri(self) -> Uri:
        """"""
    @BaseUri.setter
    def BaseUri(self, value: Uri) -> None: ...
    @property
    def ContentId(self) -> str:
        """"""
    @ContentId.setter
    def ContentId(self, value: str) -> None: ...
    @property
    def ContentStream(self) -> Stream:
        """"""
    @property
    def ContentType(self) -> ContentType:
        """"""
    @ContentType.setter
    def ContentType(self, value: ContentType) -> None: ...
    @property
    def LinkedResources(self) -> LinkedResourceCollection:
        """"""
    @property
    def TransferEncoding(self) -> TransferEncoding:
        """"""
    @TransferEncoding.setter
    def TransferEncoding(self, value: TransferEncoding) -> None: ...
    @classmethod
    @overload
    def CreateAlternateViewFromString(cls, content: str) -> AlternateView:
        """"""
    @classmethod
    @overload
    def CreateAlternateViewFromString(cls, content: str, contentType: ContentType) -> AlternateView:
        """"""
    @classmethod
    @overload
    def CreateAlternateViewFromString(
        cls, content: str, contentEncoding: Encoding, mediaType: str
    ) -> AlternateView:
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
    def Item(self) -> AlternateView:
        """"""
    @Item.setter
    def Item(self, value: AlternateView) -> None: ...
    @property
    def SyncRoot(self) -> object:
        """"""
    @overload
    def Add(self, item: AlternateView) -> None:
        """"""
    @overload
    def Add(self, value: object) -> int:
        """"""
    def Clear(self) -> None:
        """"""
    @overload
    def Contains(self, item: AlternateView) -> bool:
        """"""
    @overload
    def Contains(self, value: object) -> bool:
        """"""
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array[AlternateView], index: int) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator[AlternateView]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IndexOf(self, item: AlternateView) -> int:
        """"""
    @overload
    def IndexOf(self, value: object) -> int:
        """"""
    @overload
    def Insert(self, index: int, item: AlternateView) -> None:
        """"""
    @overload
    def Insert(self, index: int, value: object) -> None:
        """"""
    @overload
    def Remove(self, item: AlternateView) -> bool:
        """"""
    @overload
    def Remove(self, value: object) -> None:
        """"""
    def RemoveAt(self, index: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __contains__(self, item: AlternateView) -> bool:
        """"""
    @overload
    def __contains__(self, value: object) -> bool:
        """"""
    def __iter__(self) -> Iterator[AlternateView]:
        """"""
    @overload
    def __delitem__(self, item: AlternateView) -> bool:
        """"""
    @overload
    def __delitem__(self, value: object) -> None:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, index: int) -> AlternateView:
        """"""
    @overload
    def __setitem__(self, index: int, value: AlternateView) -> None:
        """"""
    @overload
    def __setitem__(self, index: int, value: object) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class Attachment(AttachmentBase, IDisposable):
    """"""
    @overload
    def __init__(self, fileName: str) -> None:
        """"""
    @overload
    def __init__(self, fileName: str, mediaType: str) -> None:
        """"""
    @overload
    def __init__(self, fileName: str, contentType: ContentType) -> None:
        """"""
    @overload
    def __init__(self, contentStream: Stream, name: str) -> None:
        """"""
    @overload
    def __init__(self, contentStream: Stream, name: str, mediaType: str) -> None:
        """"""
    @overload
    def __init__(self, contentStream: Stream, contentType: ContentType) -> None:
        """"""
    @property
    def ContentDisposition(self) -> ContentDisposition:
        """"""
    @property
    def ContentId(self) -> str:
        """"""
    @ContentId.setter
    def ContentId(self, value: str) -> None: ...
    @property
    def ContentStream(self) -> Stream:
        """"""
    @property
    def ContentType(self) -> ContentType:
        """"""
    @ContentType.setter
    def ContentType(self, value: ContentType) -> None: ...
    @property
    def Name(self) -> str:
        """"""
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def NameEncoding(self) -> Encoding:
        """"""
    @NameEncoding.setter
    def NameEncoding(self, value: Encoding) -> None: ...
    @property
    def TransferEncoding(self) -> TransferEncoding:
        """"""
    @TransferEncoding.setter
    def TransferEncoding(self, value: TransferEncoding) -> None: ...
    @classmethod
    @overload
    def CreateAttachmentFromString(cls, content: str, contentType: ContentType) -> Attachment:
        """"""
    @classmethod
    @overload
    def CreateAttachmentFromString(cls, content: str, name: str) -> Attachment:
        """"""
    @classmethod
    @overload
    def CreateAttachmentFromString(
        cls, content: str, name: str, contentEncoding: Encoding, mediaType: str
    ) -> Attachment:
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
class AttachmentBase(ABC, Object, IDisposable):
    """"""
    @property
    def ContentId(self) -> str:
        """"""
    @ContentId.setter
    def ContentId(self, value: str) -> None: ...
    @property
    def ContentStream(self) -> Stream:
        """"""
    @property
    def ContentType(self) -> ContentType:
        """"""
    @ContentType.setter
    def ContentType(self, value: ContentType) -> None: ...
    @property
    def TransferEncoding(self) -> TransferEncoding:
        """"""
    @TransferEncoding.setter
    def TransferEncoding(self, value: TransferEncoding) -> None: ...
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
    def Item(self) -> Attachment:
        """"""
    @Item.setter
    def Item(self, value: Attachment) -> None: ...
    @property
    def SyncRoot(self) -> object:
        """"""
    @overload
    def Add(self, item: Attachment) -> None:
        """"""
    @overload
    def Add(self, value: object) -> int:
        """"""
    def Clear(self) -> None:
        """"""
    @overload
    def Contains(self, item: Attachment) -> bool:
        """"""
    @overload
    def Contains(self, value: object) -> bool:
        """"""
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array[Attachment], index: int) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator[Attachment]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IndexOf(self, item: Attachment) -> int:
        """"""
    @overload
    def IndexOf(self, value: object) -> int:
        """"""
    @overload
    def Insert(self, index: int, item: Attachment) -> None:
        """"""
    @overload
    def Insert(self, index: int, value: object) -> None:
        """"""
    @overload
    def Remove(self, item: Attachment) -> bool:
        """"""
    @overload
    def Remove(self, value: object) -> None:
        """"""
    def RemoveAt(self, index: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __contains__(self, item: Attachment) -> bool:
        """"""
    @overload
    def __contains__(self, value: object) -> bool:
        """"""
    def __iter__(self) -> Iterator[Attachment]:
        """"""
    @overload
    def __delitem__(self, item: Attachment) -> bool:
        """"""
    @overload
    def __delitem__(self, value: object) -> None:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, index: int) -> Attachment:
        """"""
    @overload
    def __setitem__(self, index: int, value: Attachment) -> None:
        """"""
    @overload
    def __setitem__(self, index: int, value: object) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class AuthCommand(ABC, Object):
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
class BufferBuilder(Object):
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
class CheckCommand(ABC, Object):
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
class DataCommand(ABC, Object):
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
class DataStopCommand(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class DomainLiteralReader(ABC, Object):
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
class DotAtomReader(ABC, Object):
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
class EHelloCommand(ABC, Object):
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
class HelloCommand(ABC, Object):
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
class IMSAdminBase(ABC):
    """"""
    def AddKey(self, handle: IntPtr, Path: str) -> int:
        """"""
    def Backup(self, Location: str, Version: int, Flags: int) -> int:
        """"""
    def ChangePermissions(self, handle: IntPtr, TimeOut: int, AccessRequested: MBKeyAccess) -> None:
        """"""
    def CloseKey(self, handle: IntPtr) -> int:
        """"""
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
        """"""
    def CopyKey(
        self,
        source: IntPtr,
        SourcePath: str,
        dest: IntPtr,
        DestPath: str,
        OverwriteFlag: bool,
        CopyFlag: bool,
    ) -> None:
        """"""
    def DeleteAllData(self, handle: IntPtr, Path: str, UserType: int, DataType: int) -> None:
        """"""
    def DeleteBackup(self, Location: str, Version: int) -> None:
        """"""
    def DeleteChildKeys(self, handle: IntPtr, Path: str) -> None:
        """"""
    def DeleteData(self, key: IntPtr, path: str, Identifier: int, DataType: int) -> int:
        """"""
    def DeleteKey(self, handle: IntPtr, Path: str) -> int:
        """"""
    def EnumBackups(
        self, Location: String, Version: UInt32, BackupTime: FILETIME, EnumIndex: int
    ) -> tuple[None, String, UInt32, FILETIME]:
        """"""
    def EnumData(
        self,
        key: IntPtr,
        path: str,
        data: MetadataRecord,
        EnumDataIndex: int,
        RequiredDataLen: UInt32,
    ) -> tuple[int, UInt32]:
        """"""
    def EnumKeys(self, handle: IntPtr, Path: str, Buffer: StringBuilder, EnumKeyIndex: int) -> int:
        """"""
    def GetAllData(
        self,
        handle: IntPtr,
        Path: str,
        Attributes: int,
        UserType: int,
        DataType: int,
        NumDataEntries: UInt32,
        DataSetNumber: UInt32,
        BufferSize: int,
        buffer: IntPtr,
        RequiredBufferSize: UInt32,
    ) -> tuple[int, UInt32, UInt32, UInt32]:
        """"""
    def GetData(
        self, key: IntPtr, path: str, data: MetadataRecord, RequiredDataLen: UInt32
    ) -> tuple[int, UInt32]:
        """"""
    def GetDataPaths(
        self,
        handle: IntPtr,
        Path: str,
        Identifier: int,
        DataType: int,
        BufferSize: int,
        Buffer: Char,
        RequiredBufferSize: Int32,
    ) -> tuple[None, Char, Int32]:
        """"""
    def GetDataSetNumber(
        self, handle: IntPtr, Path: str, DataSetNumber: UInt32
    ) -> tuple[None, UInt32]:
        """"""
    def GetHandleInfo(
        self, handle: IntPtr, Info: _METADATA_HANDLE_INFO
    ) -> tuple[None, _METADATA_HANDLE_INFO]:
        """"""
    def GetLastChangeTime(
        self, handle: IntPtr, Path: str, LastChangeTime: FILETIME, LocalTime: bool
    ) -> tuple[int, FILETIME]:
        """"""
    def GetServerGuid(self) -> int:
        """"""
    def GetSystemChangeNumber(self, SystemChangeNumber: UInt32) -> tuple[None, UInt32]:
        """"""
    def KeyExchangePhase1(self) -> int:
        """"""
    def KeyExchangePhase2(self) -> int:
        """"""
    def OpenKey(
        self,
        handle: IntPtr,
        Path: str,
        AccessRequested: MBKeyAccess,
        TimeOut: int,
        NewHandle: IntPtr,
    ) -> tuple[int, IntPtr]:
        """"""
    def RenameKey(self, key: IntPtr, path: str, newName: str) -> None:
        """"""
    def Restore(self, Location: str, Version: int, Flags: int) -> int:
        """"""
    def SaveData(self) -> None:
        """"""
    def SetData(self, key: IntPtr, path: str, data: MetadataRecord) -> int:
        """"""
    def SetLastChangeTime(
        self, handle: IntPtr, Path: str, LastChangeTime: FILETIME, LocalTime: bool
    ) -> tuple[None, FILETIME]:
        """"""
    def UnmarshalInterface(self, interf: IMSAdminBase) -> tuple[int, IMSAdminBase]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ISmtpAuthenticationModule(ABC):
    """"""
    @property
    def AuthenticationType(self) -> str:
        """"""
    def Authenticate(
        self,
        challenge: str,
        credentials: NetworkCredential,
        sessionCookie: object,
        spn: str,
        channelBindingToken: ChannelBinding,
    ) -> Authorization:
        """"""
    def CloseContext(self, sessionCookie: object) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IisPickupDirectory(ABC, Object):
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
class LineInfo(ValueType):
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
class LinkedResource(AttachmentBase, IDisposable):
    """"""
    @overload
    def __init__(self, fileName: str) -> None:
        """"""
    @overload
    def __init__(self, fileName: str, mediaType: str) -> None:
        """"""
    @overload
    def __init__(self, fileName: str, contentType: ContentType) -> None:
        """"""
    @overload
    def __init__(self, contentStream: Stream) -> None:
        """"""
    @overload
    def __init__(self, contentStream: Stream, mediaType: str) -> None:
        """"""
    @overload
    def __init__(self, contentStream: Stream, contentType: ContentType) -> None:
        """"""
    @property
    def ContentId(self) -> str:
        """"""
    @ContentId.setter
    def ContentId(self, value: str) -> None: ...
    @property
    def ContentLink(self) -> Uri:
        """"""
    @ContentLink.setter
    def ContentLink(self, value: Uri) -> None: ...
    @property
    def ContentStream(self) -> Stream:
        """"""
    @property
    def ContentType(self) -> ContentType:
        """"""
    @ContentType.setter
    def ContentType(self, value: ContentType) -> None: ...
    @property
    def TransferEncoding(self) -> TransferEncoding:
        """"""
    @TransferEncoding.setter
    def TransferEncoding(self, value: TransferEncoding) -> None: ...
    @classmethod
    @overload
    def CreateLinkedResourceFromString(cls, content: str) -> LinkedResource:
        """"""
    @classmethod
    @overload
    def CreateLinkedResourceFromString(
        cls, content: str, contentType: ContentType
    ) -> LinkedResource:
        """"""
    @classmethod
    @overload
    def CreateLinkedResourceFromString(
        cls, content: str, contentEncoding: Encoding, mediaType: str
    ) -> LinkedResource:
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
    def Item(self) -> LinkedResource:
        """"""
    @Item.setter
    def Item(self, value: LinkedResource) -> None: ...
    @property
    def SyncRoot(self) -> object:
        """"""
    @overload
    def Add(self, item: LinkedResource) -> None:
        """"""
    @overload
    def Add(self, value: object) -> int:
        """"""
    def Clear(self) -> None:
        """"""
    @overload
    def Contains(self, item: LinkedResource) -> bool:
        """"""
    @overload
    def Contains(self, value: object) -> bool:
        """"""
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array[LinkedResource], index: int) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator[LinkedResource]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IndexOf(self, item: LinkedResource) -> int:
        """"""
    @overload
    def IndexOf(self, value: object) -> int:
        """"""
    @overload
    def Insert(self, index: int, item: LinkedResource) -> None:
        """"""
    @overload
    def Insert(self, index: int, value: object) -> None:
        """"""
    @overload
    def Remove(self, item: LinkedResource) -> bool:
        """"""
    @overload
    def Remove(self, value: object) -> None:
        """"""
    def RemoveAt(self, index: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __contains__(self, item: LinkedResource) -> bool:
        """"""
    @overload
    def __contains__(self, value: object) -> bool:
        """"""
    def __iter__(self) -> Iterator[LinkedResource]:
        """"""
    @overload
    def __delitem__(self, item: LinkedResource) -> bool:
        """"""
    @overload
    def __delitem__(self, value: object) -> None:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, index: int) -> LinkedResource:
        """"""
    @overload
    def __setitem__(self, index: int, value: LinkedResource) -> None:
        """"""
    @overload
    def __setitem__(self, index: int, value: object) -> None:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class MBKeyAccess(Enum):
    """"""

    Read: MBKeyAccess = ...
    """"""
    Write: MBKeyAccess = ...
    """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class MSAdminBase(__ComObject):
    """"""
    def __init__(self) -> None:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class MailAddress(Object):
    """"""
    @overload
    def __init__(self, address: str) -> None:
        """"""
    @overload
    def __init__(self, address: str, displayName: str) -> None:
        """"""
    @overload
    def __init__(self, address: str, displayName: str, displayNameEncoding: Encoding) -> None:
        """"""
    @property
    def Address(self) -> str:
        """"""
    @property
    def DisplayName(self) -> str:
        """"""
    @property
    def Host(self) -> str:
        """"""
    @property
    def User(self) -> str:
        """"""
    def Equals(self, value: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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
    def __init__(self) -> None:
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
    def Item(self) -> MailAddress:
        """"""
    @Item.setter
    def Item(self, value: MailAddress) -> None: ...
    @property
    def SyncRoot(self) -> object:
        """"""
    @overload
    def Add(self, item: MailAddress) -> None:
        """"""
    @overload
    def Add(self, value: object) -> int:
        """"""
    @overload
    def Add(self, addresses: str) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    @overload
    def Contains(self, item: MailAddress) -> bool:
        """"""
    @overload
    def Contains(self, value: object) -> bool:
        """"""
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array[MailAddress], index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator[MailAddress]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IndexOf(self, item: MailAddress) -> int:
        """"""
    @overload
    def IndexOf(self, value: object) -> int:
        """"""
    @overload
    def Insert(self, index: int, item: MailAddress) -> None:
        """"""
    @overload
    def Insert(self, index: int, value: object) -> None:
        """"""
    @overload
    def Remove(self, item: MailAddress) -> bool:
        """"""
    @overload
    def Remove(self, value: object) -> None:
        """"""
    def RemoveAt(self, index: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __contains__(self, item: MailAddress) -> bool:
        """"""
    @overload
    def __contains__(self, value: object) -> bool:
        """"""
    def __iter__(self) -> Iterator[MailAddress]:
        """"""
    @overload
    def __delitem__(self, item: MailAddress) -> bool:
        """"""
    @overload
    def __delitem__(self, value: object) -> None:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, index: int) -> MailAddress:
        """"""
    @overload
    def __setitem__(self, index: int, value: MailAddress) -> None:
        """"""
    @overload
    def __setitem__(self, index: int, value: object) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class MailAddressParser(ABC, Object):
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
class MailCommand(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class MailHeaderInfo(ABC, Object):
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
class MailMessage(Object, IDisposable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, _from: str, to: str) -> None:
        """"""
    @overload
    def __init__(self, _from: str, to: str, subject: str, body: str) -> None:
        """"""
    @overload
    def __init__(self, _from: MailAddress, to: MailAddress) -> None:
        """"""
    @property
    def AlternateViews(self) -> AlternateViewCollection:
        """"""
    @property
    def Attachments(self) -> AttachmentCollection:
        """"""
    @property
    def Bcc(self) -> MailAddressCollection:
        """"""
    @property
    def Body(self) -> str:
        """"""
    @Body.setter
    def Body(self, value: str) -> None: ...
    @property
    def BodyEncoding(self) -> Encoding:
        """"""
    @BodyEncoding.setter
    def BodyEncoding(self, value: Encoding) -> None: ...
    @property
    def BodyTransferEncoding(self) -> TransferEncoding:
        """"""
    @BodyTransferEncoding.setter
    def BodyTransferEncoding(self, value: TransferEncoding) -> None: ...
    @property
    def CC(self) -> MailAddressCollection:
        """"""
    @property
    def DeliveryNotificationOptions(self) -> DeliveryNotificationOptions:
        """"""
    @DeliveryNotificationOptions.setter
    def DeliveryNotificationOptions(self, value: DeliveryNotificationOptions) -> None: ...
    @property
    def From(self) -> MailAddress:
        """"""
    @From.setter
    def From(self, value: MailAddress) -> None: ...
    @property
    def Headers(self) -> NameValueCollection:
        """"""
    @property
    def HeadersEncoding(self) -> Encoding:
        """"""
    @HeadersEncoding.setter
    def HeadersEncoding(self, value: Encoding) -> None: ...
    @property
    def IsBodyHtml(self) -> bool:
        """"""
    @IsBodyHtml.setter
    def IsBodyHtml(self, value: bool) -> None: ...
    @property
    def Priority(self) -> MailPriority:
        """"""
    @Priority.setter
    def Priority(self, value: MailPriority) -> None: ...
    @property
    def ReplyTo(self) -> MailAddress:
        """"""
    @ReplyTo.setter
    def ReplyTo(self, value: MailAddress) -> None: ...
    @property
    def ReplyToList(self) -> MailAddressCollection:
        """"""
    @property
    def Sender(self) -> MailAddress:
        """"""
    @Sender.setter
    def Sender(self, value: MailAddress) -> None: ...
    @property
    def Subject(self) -> str:
        """"""
    @Subject.setter
    def Subject(self, value: str) -> None: ...
    @property
    def SubjectEncoding(self) -> Encoding:
        """"""
    @SubjectEncoding.setter
    def SubjectEncoding(self, value: Encoding) -> None: ...
    @property
    def To(self) -> MailAddressCollection:
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

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class MailPriority(Enum):
    """"""

    Normal: MailPriority = ...
    """"""
    Low: MailPriority = ...
    """"""
    High: MailPriority = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class MailWriter(BaseWriter):
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
class Message(Object):
    """"""
    @property
    def Priority(self) -> MailPriority:
        """"""
    @Priority.setter
    def Priority(self, value: MailPriority) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class MetadataRecord(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class PropertyName(Enum):
    """"""

    Invalid: PropertyName = ...
    """"""
    ServerState: PropertyName = ...
    """"""
    PickupDirectory: PropertyName = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class QuotedPairReader(ABC, Object):
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
class QuotedStringFormatReader(ABC, Object):
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
class ReadLinesCommand(ABC, Object):
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
class RecipientCommand(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

type SendCompletedEventHandler = Callable[[object, AsyncCompletedEventArgs], None]
""""""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SendMailAsyncResult(LazyAsyncResult, IAsyncResult):
    """"""
    @property
    def AsyncState(self) -> object:
        """"""
    @property
    def AsyncWaitHandle(self) -> WaitHandle:
        """"""
    @property
    def CompletedSynchronously(self) -> bool:
        """"""
    @property
    def IsCompleted(self) -> bool:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class SmtpAccess(Enum):
    """"""

    _None: SmtpAccess = ...
    """"""
    Connect: SmtpAccess = ...
    """"""
    ConnectToUnrestrictedPort: SmtpAccess = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SmtpAuthenticationManager(ABC, Object):
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
class SmtpClient(Object, IDisposable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, host: str) -> None:
        """"""
    @overload
    def __init__(self, host: str, port: int) -> None:
        """"""
    @property
    def ClientCertificates(self) -> X509CertificateCollection:
        """"""
    @property
    def Credentials(self) -> ICredentialsByHost:
        """"""
    @Credentials.setter
    def Credentials(self, value: ICredentialsByHost) -> None: ...
    @property
    def DeliveryFormat(self) -> SmtpDeliveryFormat:
        """"""
    @DeliveryFormat.setter
    def DeliveryFormat(self, value: SmtpDeliveryFormat) -> None: ...
    @property
    def DeliveryMethod(self) -> SmtpDeliveryMethod:
        """"""
    @DeliveryMethod.setter
    def DeliveryMethod(self, value: SmtpDeliveryMethod) -> None: ...
    @property
    def EnableSsl(self) -> bool:
        """"""
    @EnableSsl.setter
    def EnableSsl(self, value: bool) -> None: ...
    @property
    def Host(self) -> str:
        """"""
    @Host.setter
    def Host(self, value: str) -> None: ...
    @property
    def PickupDirectoryLocation(self) -> str:
        """"""
    @PickupDirectoryLocation.setter
    def PickupDirectoryLocation(self, value: str) -> None: ...
    @property
    def Port(self) -> int:
        """"""
    @Port.setter
    def Port(self, value: int) -> None: ...
    @property
    def ServicePoint(self) -> ServicePoint:
        """"""
    @property
    def TargetName(self) -> str:
        """"""
    @TargetName.setter
    def TargetName(self, value: str) -> None: ...
    @property
    def Timeout(self) -> int:
        """"""
    @Timeout.setter
    def Timeout(self, value: int) -> None: ...
    @property
    def UseDefaultCredentials(self) -> bool:
        """"""
    @UseDefaultCredentials.setter
    def UseDefaultCredentials(self, value: bool) -> None: ...
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def Send(self, message: MailMessage) -> None:
        """"""
    @overload
    def Send(self, _from: str, recipients: str, subject: str, body: str) -> None:
        """"""
    @overload
    def SendAsync(self, message: MailMessage, userToken: object) -> None:
        """"""
    @overload
    def SendAsync(
        self, _from: str, recipients: str, subject: str, body: str, userToken: object
    ) -> None:
        """"""
    def SendAsyncCancel(self) -> None:
        """"""
    @overload
    def SendMailAsync(self, message: MailMessage) -> Task:
        """"""
    @overload
    def SendMailAsync(self, _from: str, recipients: str, subject: str, body: str) -> Task:
        """"""
    def ToString(self) -> str:
        """"""
    SendCompleted: EventType[SendCompletedEventHandler] = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SmtpCommands(ABC, Object):
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
class SmtpConnection(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class SmtpDeliveryFormat(Enum):
    """"""

    SevenBit: SmtpDeliveryFormat = ...
    """"""
    International: SmtpDeliveryFormat = ...
    """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class SmtpDeliveryMethod(Enum):
    """"""

    Network: SmtpDeliveryMethod = ...
    """"""
    SpecifiedPickupDirectory: SmtpDeliveryMethod = ...
    """"""
    PickupDirectoryFromIis: SmtpDeliveryMethod = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SmtpDigestAuthenticationModule(Object, ISmtpAuthenticationModule):
    """"""
    @property
    def AuthenticationType(self) -> str:
        """"""
    def Authenticate(
        self,
        challenge: str,
        credential: NetworkCredential,
        sessionCookie: object,
        spn: str,
        channelBindingToken: ChannelBinding,
    ) -> Authorization:
        """"""
    def CloseContext(self, sessionCookie: object) -> None:
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
class SmtpException(Exception, _Exception, ISerializable):
    """"""
    @overload
    def __init__(self, statusCode: SmtpStatusCode) -> None:
        """"""
    @overload
    def __init__(self, statusCode: SmtpStatusCode, message: str) -> None:
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
    def Source(self) -> str:
        """"""
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """"""
    @property
    def StatusCode(self) -> SmtpStatusCode:
        """"""
    @StatusCode.setter
    def StatusCode(self, value: SmtpStatusCode) -> None: ...
    @property
    def TargetSite(self) -> MethodBase:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetBaseException(self) -> Exception:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetObjectData(
        self, serializationInfo: SerializationInfo, streamingContext: StreamingContext
    ) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SmtpFailedRecipientException(SmtpException, _Exception, ISerializable):
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
    def __init__(self, statusCode: SmtpStatusCode, failedRecipient: str) -> None:
        """"""
    @overload
    def __init__(
        self, statusCode: SmtpStatusCode, failedRecipient: str, serverResponse: str
    ) -> None:
        """"""
    @overload
    def __init__(self, message: str, failedRecipient: str, innerException: Exception) -> None:
        """"""
    @property
    def Data(self) -> IDictionary:
        """"""
    @property
    def FailedRecipient(self) -> str:
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
    def Source(self) -> str:
        """"""
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """"""
    @property
    def StatusCode(self) -> SmtpStatusCode:
        """"""
    @StatusCode.setter
    def StatusCode(self, value: SmtpStatusCode) -> None: ...
    @property
    def TargetSite(self) -> MethodBase:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetBaseException(self) -> Exception:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetObjectData(
        self, serializationInfo: SerializationInfo, streamingContext: StreamingContext
    ) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SmtpFailedRecipientsException(SmtpFailedRecipientException, _Exception, ISerializable):
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
    def __init__(self, message: str, innerExceptions: Array[SmtpFailedRecipientException]) -> None:
        """"""
    @property
    def Data(self) -> IDictionary:
        """"""
    @property
    def FailedRecipient(self) -> str:
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
    def InnerExceptions(self) -> Array[SmtpFailedRecipientException]:
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
    def StatusCode(self) -> SmtpStatusCode:
        """"""
    @StatusCode.setter
    def StatusCode(self, value: SmtpStatusCode) -> None: ...
    @property
    def TargetSite(self) -> MethodBase:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetBaseException(self) -> Exception:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetObjectData(
        self, serializationInfo: SerializationInfo, streamingContext: StreamingContext
    ) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SmtpLoginAuthenticationModule(Object, ISmtpAuthenticationModule):
    """"""
    @property
    def AuthenticationType(self) -> str:
        """"""
    def Authenticate(
        self,
        challenge: str,
        credential: NetworkCredential,
        sessionCookie: object,
        spn: str,
        channelBindingToken: ChannelBinding,
    ) -> Authorization:
        """"""
    def CloseContext(self, sessionCookie: object) -> None:
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
class SmtpNegotiateAuthenticationModule(Object, ISmtpAuthenticationModule):
    """"""
    @property
    def AuthenticationType(self) -> str:
        """"""
    def Authenticate(
        self,
        challenge: str,
        credential: NetworkCredential,
        sessionCookie: object,
        spn: str,
        channelBindingToken: ChannelBinding,
    ) -> Authorization:
        """"""
    def CloseContext(self, sessionCookie: object) -> None:
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
class SmtpNtlmAuthenticationModule(Object, ISmtpAuthenticationModule):
    """"""
    @property
    def AuthenticationType(self) -> str:
        """"""
    def Authenticate(
        self,
        challenge: str,
        credential: NetworkCredential,
        sessionCookie: object,
        spn: str,
        channelBindingToken: ChannelBinding,
    ) -> Authorization:
        """"""
    def CloseContext(self, sessionCookie: object) -> None:
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
class SmtpPermission(
    CodeAccessPermission, IUnrestrictedPermission, IPermission, ISecurityEncodable, IStackWalk
):
    """"""
    @overload
    def __init__(self, state: PermissionState) -> None:
        """"""
    @overload
    def __init__(self, unrestricted: bool) -> None:
        """"""
    @overload
    def __init__(self, access: SmtpAccess) -> None:
        """"""
    @property
    def Access(self) -> SmtpAccess:
        """"""
    def AddPermission(self, access: SmtpAccess) -> None:
        """"""
    def Assert(self) -> None:
        """"""
    def Copy(self) -> IPermission:
        """"""
    def Demand(self) -> None:
        """"""
    def Deny(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def FromXml(self, securityElement: SecurityElement) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Intersect(self, target: IPermission) -> IPermission:
        """"""
    def IsSubsetOf(self, target: IPermission) -> bool:
        """"""
    def IsUnrestricted(self) -> bool:
        """"""
    def PermitOnly(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def ToXml(self) -> SecurityElement:
        """"""
    def Union(self, target: IPermission) -> IPermission:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SmtpPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    """"""
    def __init__(self, action: SecurityAction) -> None:
        """"""
    @property
    def Access(self) -> str:
        """"""
    @Access.setter
    def Access(self, value: str) -> None: ...
    @property
    def Action(self) -> SecurityAction:
        """"""
    @Action.setter
    def Action(self, value: SecurityAction) -> None: ...
    @property
    def TypeId(self) -> object:
        """"""
    @property
    def Unrestricted(self) -> bool:
        """"""
    @Unrestricted.setter
    def Unrestricted(self, value: bool) -> None: ...
    def CreatePermission(self) -> IPermission:
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
class SmtpPooledStream(PooledStream, IDisposable):
    """"""
    @property
    def CanRead(self) -> bool:
        """"""
    @property
    def CanSeek(self) -> bool:
        """"""
    @property
    def CanTimeout(self) -> bool:
        """"""
    @property
    def CanWrite(self) -> bool:
        """"""
    @property
    def Length(self) -> int:
        """"""
    @property
    def Position(self) -> int:
        """"""
    @Position.setter
    def Position(self, value: int) -> None: ...
    @property
    def ReadTimeout(self) -> int:
        """"""
    @ReadTimeout.setter
    def ReadTimeout(self, value: int) -> None: ...
    @property
    def WriteTimeout(self) -> int:
        """"""
    @WriteTimeout.setter
    def WriteTimeout(self, value: int) -> None: ...
    def BeginRead(
        self, buffer: Array[int], offset: int, size: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """"""
    def BeginWrite(
        self, buffer: Array[int], offset: int, size: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """"""
    @overload
    def Close(self) -> None:
        """"""
    @overload
    def Close(self, timeout: int) -> None:
        """"""
    @overload
    def CopyTo(self, destination: Stream) -> None:
        """"""
    @overload
    def CopyTo(self, destination: Stream, bufferSize: int) -> None:
        """"""
    @overload
    def CopyToAsync(self, destination: Stream) -> Task:
        """"""
    @overload
    def CopyToAsync(self, destination: Stream, bufferSize: int) -> Task:
        """"""
    @overload
    def CopyToAsync(
        self, destination: Stream, bufferSize: int, cancellationToken: CancellationToken
    ) -> Task:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    def Dispose(self) -> None:
        """"""
    def EndRead(self, asyncResult: IAsyncResult) -> int:
        """"""
    def EndWrite(self, asyncResult: IAsyncResult) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Flush(self) -> None:
        """"""
    @overload
    def FlushAsync(self) -> Task:
        """"""
    @overload
    def FlushAsync(self, cancellationToken: CancellationToken) -> Task:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetLifetimeService(self) -> object:
        """"""
    def GetType(self) -> Type:
        """"""
    def InitializeLifetimeService(self) -> object:
        """"""
    def Read(self, buffer: Array[int], offset: int, size: int) -> int:
        """"""
    @overload
    def ReadAsync(self, buffer: Array[int], offset: int, count: int) -> Task[int]:
        """"""
    @overload
    def ReadAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task[int]:
        """"""
    def ReadByte(self) -> int:
        """"""
    def Seek(self, offset: int, origin: SeekOrigin) -> int:
        """"""
    def SetLength(self, value: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def Write(self, buffer: Array[int], offset: int, size: int) -> None:
        """"""
    @overload
    def WriteAsync(self, buffer: Array[int], offset: int, count: int) -> Task:
        """"""
    @overload
    def WriteAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task:
        """"""
    def WriteByte(self, value: int) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SmtpReplyReader(Object):
    """"""
    def Close(self) -> None:
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
class SmtpReplyReaderFactory(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SmtpTransport(Object):
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
class StartTlsCommand(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class WhitespaceReader(ABC, Object):
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
class _METADATA_HANDLE_INFO(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
