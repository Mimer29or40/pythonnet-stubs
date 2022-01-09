from __future__ import annotations

from abc import ABC
from typing import Callable, Generic, List, Protocol, Tuple, Union, overload

from System import Array, AsyncCallback, Boolean, Byte, Char, Enum, Exception, IAsyncResult, ICloneable, IDisposable, Int32, IntPtr, MulticastDelegate, Object, String, UInt32, Uri, ValueType, Void, __ComObject
from System.Collections import ICollection, IEnumerable, IList
from System.Collections.Generic import ICollection, IEnumerable, IList, IReadOnlyCollection, IReadOnlyList
from System.Collections.ObjectModel import Collection
from System.Collections.Specialized import NameValueCollection
from System.ComponentModel import AsyncCompletedEventArgs
from System.IO import Stream
from System.Net import Authorization, ICredentialsByHost, LazyAsyncResult, NetworkCredential, PooledStream, ServicePoint
from System.Net.Mime import BaseWriter, ContentDisposition, ContentType, TransferEncoding
from System.Runtime.InteropServices import _Attribute, _Exception
from System.Runtime.InteropServices.ComTypes import FILETIME
from System.Runtime.Serialization import ISerializable, SerializationInfo, StreamingContext
from System.Security import CodeAccessPermission, IPermission, ISecurityEncodable, IStackWalk, SecurityElement
from System.Security.Authentication.ExtendedProtection import ChannelBinding
from System.Security.Cryptography.X509Certificates import X509CertificateCollection
from System.Security.Permissions import CodeAccessSecurityAttribute, IUnrestrictedPermission, PermissionState, SecurityAction
from System.Text import Encoding, StringBuilder
from System.Threading.Tasks import Task

# ---------- Types ---------- #

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
ByteType = Union[int, Byte]
CharType = Union[str, Char]
IntType = Union[int, Int32]
NIntType = Union[int, IntPtr]
ObjectType = Object
StringType = Union[str, String]
UIntType = Union[int, UInt32]
VoidType = Union[None, Void]


class EventType(Generic[T]):
    def __iadd__(self, other: T): ...
    
    def __isub__(self, other: T): ...


# ---------- Classes ---------- #

class AlternateView(AttachmentBase, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, fileName: StringType): ...
    
    @overload
    def __init__(self, fileName: StringType, mediaType: StringType): ...
    
    @overload
    def __init__(self, fileName: StringType, contentType: ContentType): ...
    
    @overload
    def __init__(self, contentStream: Stream): ...
    
    @overload
    def __init__(self, contentStream: Stream, mediaType: StringType): ...
    
    @overload
    def __init__(self, contentStream: Stream, contentType: ContentType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def BaseUri(self) -> Uri: ...
    
    @BaseUri.setter
    def BaseUri(self, value: Uri) -> None: ...
    
    @property
    def LinkedResources(self) -> LinkedResourceCollection: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    @overload
    def CreateAlternateViewFromString(content: StringType) -> AlternateView: ...
    
    @staticmethod
    @overload
    def CreateAlternateViewFromString(content: StringType, contentEncoding: Encoding, mediaType: StringType) -> AlternateView: ...
    
    @staticmethod
    @overload
    def CreateAlternateViewFromString(content: StringType, contentType: ContentType) -> AlternateView: ...
    
    def get_BaseUri(self) -> Uri: ...
    
    def get_LinkedResources(self) -> LinkedResourceCollection: ...
    
    def set_BaseUri(self, value: Uri) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AlternateViewCollection(Collection[AlternateView], IList[AlternateView], ICollection[AlternateView], IEnumerable[AlternateView], IEnumerable, IList, ICollection, IReadOnlyList[AlternateView], IReadOnlyCollection[AlternateView], IDisposable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Dispose(self) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Attachment(AttachmentBase, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, fileName: StringType): ...
    
    @overload
    def __init__(self, fileName: StringType, mediaType: StringType): ...
    
    @overload
    def __init__(self, fileName: StringType, contentType: ContentType): ...
    
    @overload
    def __init__(self, contentStream: Stream, name: StringType): ...
    
    @overload
    def __init__(self, contentStream: Stream, name: StringType, mediaType: StringType): ...
    
    @overload
    def __init__(self, contentStream: Stream, contentType: ContentType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ContentDisposition(self) -> ContentDisposition: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @Name.setter
    def Name(self, value: StringType) -> None: ...
    
    @property
    def NameEncoding(self) -> Encoding: ...
    
    @NameEncoding.setter
    def NameEncoding(self, value: Encoding) -> None: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    @overload
    def CreateAttachmentFromString(content: StringType, name: StringType) -> Attachment: ...
    
    @staticmethod
    @overload
    def CreateAttachmentFromString(content: StringType, name: StringType, contentEncoding: Encoding, mediaType: StringType) -> Attachment: ...
    
    @staticmethod
    @overload
    def CreateAttachmentFromString(content: StringType, contentType: ContentType) -> Attachment: ...
    
    def get_ContentDisposition(self) -> ContentDisposition: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_NameEncoding(self) -> Encoding: ...
    
    def set_Name(self, value: StringType) -> VoidType: ...
    
    def set_NameEncoding(self, value: Encoding) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AttachmentBase(ABC, ObjectType, IDisposable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def ContentId(self) -> StringType: ...
    
    @ContentId.setter
    def ContentId(self, value: StringType) -> None: ...
    
    @property
    def ContentStream(self) -> Stream: ...
    
    @property
    def ContentType(self) -> ContentType: ...
    
    @ContentType.setter
    def ContentType(self, value: ContentType) -> None: ...
    
    @property
    def TransferEncoding(self) -> TransferEncoding: ...
    
    @TransferEncoding.setter
    def TransferEncoding(self, value: TransferEncoding) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Dispose(self) -> VoidType: ...
    
    def get_ContentId(self) -> StringType: ...
    
    def get_ContentStream(self) -> Stream: ...
    
    def get_ContentType(self) -> ContentType: ...
    
    def get_TransferEncoding(self) -> TransferEncoding: ...
    
    def set_ContentId(self, value: StringType) -> VoidType: ...
    
    def set_ContentType(self, value: ContentType) -> VoidType: ...
    
    def set_TransferEncoding(self, value: TransferEncoding) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AttachmentCollection(Collection[Attachment], IList[Attachment], ICollection[Attachment], IEnumerable[Attachment], IEnumerable, IList, ICollection, IReadOnlyList[Attachment], IReadOnlyCollection[Attachment], IDisposable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Dispose(self) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AuthCommand(ABC, ObjectType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class BufferBuilder(ObjectType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CheckCommand(ABC, ObjectType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DataCommand(ABC, ObjectType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DataStopCommand(ABC, ObjectType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DomainLiteralReader(ABC, ObjectType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DotAtomReader(ABC, ObjectType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EHelloCommand(ABC, ObjectType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class HelloCommand(ABC, ObjectType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IisPickupDirectory(ABC, ObjectType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class LinkedResource(AttachmentBase, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, fileName: StringType): ...
    
    @overload
    def __init__(self, fileName: StringType, mediaType: StringType): ...
    
    @overload
    def __init__(self, fileName: StringType, contentType: ContentType): ...
    
    @overload
    def __init__(self, contentStream: Stream): ...
    
    @overload
    def __init__(self, contentStream: Stream, mediaType: StringType): ...
    
    @overload
    def __init__(self, contentStream: Stream, contentType: ContentType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ContentLink(self) -> Uri: ...
    
    @ContentLink.setter
    def ContentLink(self, value: Uri) -> None: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    @overload
    def CreateLinkedResourceFromString(content: StringType) -> LinkedResource: ...
    
    @staticmethod
    @overload
    def CreateLinkedResourceFromString(content: StringType, contentEncoding: Encoding, mediaType: StringType) -> LinkedResource: ...
    
    @staticmethod
    @overload
    def CreateLinkedResourceFromString(content: StringType, contentType: ContentType) -> LinkedResource: ...
    
    def get_ContentLink(self) -> Uri: ...
    
    def set_ContentLink(self, value: Uri) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class LinkedResourceCollection(Collection[LinkedResource], IList[LinkedResource], ICollection[LinkedResource], IEnumerable[LinkedResource], IEnumerable, IList, ICollection, IReadOnlyList[LinkedResource], IReadOnlyCollection[LinkedResource], IDisposable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Dispose(self) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MSAdminBase(__ComObject):
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


class MailAddress(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, address: StringType): ...
    
    @overload
    def __init__(self, address: StringType, displayName: StringType): ...
    
    @overload
    def __init__(self, address: StringType, displayName: StringType, displayNameEncoding: Encoding): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Address(self) -> StringType: ...
    
    @property
    def DisplayName(self) -> StringType: ...
    
    @property
    def Host(self) -> StringType: ...
    
    @property
    def User(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, value: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Address(self) -> StringType: ...
    
    def get_DisplayName(self) -> StringType: ...
    
    def get_Host(self) -> StringType: ...
    
    def get_User(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MailAddressCollection(Collection[MailAddress], IList[MailAddress], ICollection[MailAddress], IEnumerable[MailAddress], IEnumerable, IList, ICollection, IReadOnlyList[MailAddress], IReadOnlyCollection[MailAddress]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def Add(self, addresses: StringType) -> VoidType: ...
    
    def ToString(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MailAddressParser(ABC, ObjectType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MailCommand(ABC, ObjectType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MailHeaderInfo(ABC, ObjectType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MailMessage(ObjectType, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, _from: StringType, to: StringType): ...
    
    @overload
    def __init__(self, _from: StringType, to: StringType, subject: StringType, body: StringType): ...
    
    @overload
    def __init__(self, _from: MailAddress, to: MailAddress): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AlternateViews(self) -> AlternateViewCollection: ...
    
    @property
    def Attachments(self) -> AttachmentCollection: ...
    
    @property
    def Bcc(self) -> MailAddressCollection: ...
    
    @property
    def Body(self) -> StringType: ...
    
    @Body.setter
    def Body(self, value: StringType) -> None: ...
    
    @property
    def BodyEncoding(self) -> Encoding: ...
    
    @BodyEncoding.setter
    def BodyEncoding(self, value: Encoding) -> None: ...
    
    @property
    def BodyTransferEncoding(self) -> TransferEncoding: ...
    
    @BodyTransferEncoding.setter
    def BodyTransferEncoding(self, value: TransferEncoding) -> None: ...
    
    @property
    def CC(self) -> MailAddressCollection: ...
    
    @property
    def DeliveryNotificationOptions(self) -> DeliveryNotificationOptions: ...
    
    @DeliveryNotificationOptions.setter
    def DeliveryNotificationOptions(self, value: DeliveryNotificationOptions) -> None: ...
    
    @property
    def From(self) -> MailAddress: ...
    
    @From.setter
    def From(self, value: MailAddress) -> None: ...
    
    @property
    def Headers(self) -> NameValueCollection: ...
    
    @property
    def HeadersEncoding(self) -> Encoding: ...
    
    @HeadersEncoding.setter
    def HeadersEncoding(self, value: Encoding) -> None: ...
    
    @property
    def IsBodyHtml(self) -> BooleanType: ...
    
    @IsBodyHtml.setter
    def IsBodyHtml(self, value: BooleanType) -> None: ...
    
    @property
    def Priority(self) -> MailPriority: ...
    
    @Priority.setter
    def Priority(self, value: MailPriority) -> None: ...
    
    @property
    def ReplyTo(self) -> MailAddress: ...
    
    @ReplyTo.setter
    def ReplyTo(self, value: MailAddress) -> None: ...
    
    @property
    def ReplyToList(self) -> MailAddressCollection: ...
    
    @property
    def Sender(self) -> MailAddress: ...
    
    @Sender.setter
    def Sender(self, value: MailAddress) -> None: ...
    
    @property
    def Subject(self) -> StringType: ...
    
    @Subject.setter
    def Subject(self, value: StringType) -> None: ...
    
    @property
    def SubjectEncoding(self) -> Encoding: ...
    
    @SubjectEncoding.setter
    def SubjectEncoding(self, value: Encoding) -> None: ...
    
    @property
    def To(self) -> MailAddressCollection: ...
    
    # ---------- Methods ---------- #
    
    def Dispose(self) -> VoidType: ...
    
    def get_AlternateViews(self) -> AlternateViewCollection: ...
    
    def get_Attachments(self) -> AttachmentCollection: ...
    
    def get_Bcc(self) -> MailAddressCollection: ...
    
    def get_Body(self) -> StringType: ...
    
    def get_BodyEncoding(self) -> Encoding: ...
    
    def get_BodyTransferEncoding(self) -> TransferEncoding: ...
    
    def get_CC(self) -> MailAddressCollection: ...
    
    def get_DeliveryNotificationOptions(self) -> DeliveryNotificationOptions: ...
    
    def get_From(self) -> MailAddress: ...
    
    def get_Headers(self) -> NameValueCollection: ...
    
    def get_HeadersEncoding(self) -> Encoding: ...
    
    def get_IsBodyHtml(self) -> BooleanType: ...
    
    def get_Priority(self) -> MailPriority: ...
    
    def get_ReplyTo(self) -> MailAddress: ...
    
    def get_ReplyToList(self) -> MailAddressCollection: ...
    
    def get_Sender(self) -> MailAddress: ...
    
    def get_Subject(self) -> StringType: ...
    
    def get_SubjectEncoding(self) -> Encoding: ...
    
    def get_To(self) -> MailAddressCollection: ...
    
    def set_Body(self, value: StringType) -> VoidType: ...
    
    def set_BodyEncoding(self, value: Encoding) -> VoidType: ...
    
    def set_BodyTransferEncoding(self, value: TransferEncoding) -> VoidType: ...
    
    def set_DeliveryNotificationOptions(self, value: DeliveryNotificationOptions) -> VoidType: ...
    
    def set_From(self, value: MailAddress) -> VoidType: ...
    
    def set_HeadersEncoding(self, value: Encoding) -> VoidType: ...
    
    def set_IsBodyHtml(self, value: BooleanType) -> VoidType: ...
    
    def set_Priority(self, value: MailPriority) -> VoidType: ...
    
    def set_ReplyTo(self, value: MailAddress) -> VoidType: ...
    
    def set_Sender(self, value: MailAddress) -> VoidType: ...
    
    def set_Subject(self, value: StringType) -> VoidType: ...
    
    def set_SubjectEncoding(self, value: Encoding) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MailWriter(BaseWriter):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Message(ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Priority(self) -> MailPriority: ...
    
    @Priority.setter
    def Priority(self, value: MailPriority) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Priority(self) -> MailPriority: ...
    
    def set_Priority(self, value: MailPriority) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class QuotedPairReader(ABC, ObjectType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class QuotedStringFormatReader(ABC, ObjectType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ReadLinesCommand(ABC, ObjectType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RecipientCommand(ABC, ObjectType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SendCompletedEventHandler(MulticastDelegate, ICloneable, ISerializable):
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


class SendMailAsyncResult(LazyAsyncResult, IAsyncResult):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SmtpAuthenticationManager(ABC, ObjectType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SmtpClient(ObjectType, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, host: StringType): ...
    
    @overload
    def __init__(self, host: StringType, port: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ClientCertificates(self) -> X509CertificateCollection: ...
    
    @property
    def Credentials(self) -> ICredentialsByHost: ...
    
    @Credentials.setter
    def Credentials(self, value: ICredentialsByHost) -> None: ...
    
    @property
    def DeliveryFormat(self) -> SmtpDeliveryFormat: ...
    
    @DeliveryFormat.setter
    def DeliveryFormat(self, value: SmtpDeliveryFormat) -> None: ...
    
    @property
    def DeliveryMethod(self) -> SmtpDeliveryMethod: ...
    
    @DeliveryMethod.setter
    def DeliveryMethod(self, value: SmtpDeliveryMethod) -> None: ...
    
    @property
    def EnableSsl(self) -> BooleanType: ...
    
    @EnableSsl.setter
    def EnableSsl(self, value: BooleanType) -> None: ...
    
    @property
    def Host(self) -> StringType: ...
    
    @Host.setter
    def Host(self, value: StringType) -> None: ...
    
    @property
    def PickupDirectoryLocation(self) -> StringType: ...
    
    @PickupDirectoryLocation.setter
    def PickupDirectoryLocation(self, value: StringType) -> None: ...
    
    @property
    def Port(self) -> IntType: ...
    
    @Port.setter
    def Port(self, value: IntType) -> None: ...
    
    @property
    def ServicePoint(self) -> ServicePoint: ...
    
    @property
    def TargetName(self) -> StringType: ...
    
    @TargetName.setter
    def TargetName(self, value: StringType) -> None: ...
    
    @property
    def Timeout(self) -> IntType: ...
    
    @Timeout.setter
    def Timeout(self, value: IntType) -> None: ...
    
    @property
    def UseDefaultCredentials(self) -> BooleanType: ...
    
    @UseDefaultCredentials.setter
    def UseDefaultCredentials(self, value: BooleanType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Dispose(self) -> VoidType: ...
    
    @overload
    def Send(self, _from: StringType, recipients: StringType, subject: StringType, body: StringType) -> VoidType: ...
    
    @overload
    def Send(self, message: MailMessage) -> VoidType: ...
    
    @overload
    def SendAsync(self, _from: StringType, recipients: StringType, subject: StringType, body: StringType, userToken: ObjectType) -> VoidType: ...
    
    @overload
    def SendAsync(self, message: MailMessage, userToken: ObjectType) -> VoidType: ...
    
    def SendAsyncCancel(self) -> VoidType: ...
    
    @overload
    def SendMailAsync(self, _from: StringType, recipients: StringType, subject: StringType, body: StringType) -> Task: ...
    
    @overload
    def SendMailAsync(self, message: MailMessage) -> Task: ...
    
    def add_SendCompleted(self, value: SendCompletedEventHandler) -> VoidType: ...
    
    def get_ClientCertificates(self) -> X509CertificateCollection: ...
    
    def get_Credentials(self) -> ICredentialsByHost: ...
    
    def get_DeliveryFormat(self) -> SmtpDeliveryFormat: ...
    
    def get_DeliveryMethod(self) -> SmtpDeliveryMethod: ...
    
    def get_EnableSsl(self) -> BooleanType: ...
    
    def get_Host(self) -> StringType: ...
    
    def get_PickupDirectoryLocation(self) -> StringType: ...
    
    def get_Port(self) -> IntType: ...
    
    def get_ServicePoint(self) -> ServicePoint: ...
    
    def get_TargetName(self) -> StringType: ...
    
    def get_Timeout(self) -> IntType: ...
    
    def get_UseDefaultCredentials(self) -> BooleanType: ...
    
    def remove_SendCompleted(self, value: SendCompletedEventHandler) -> VoidType: ...
    
    def set_Credentials(self, value: ICredentialsByHost) -> VoidType: ...
    
    def set_DeliveryFormat(self, value: SmtpDeliveryFormat) -> VoidType: ...
    
    def set_DeliveryMethod(self, value: SmtpDeliveryMethod) -> VoidType: ...
    
    def set_EnableSsl(self, value: BooleanType) -> VoidType: ...
    
    def set_Host(self, value: StringType) -> VoidType: ...
    
    def set_PickupDirectoryLocation(self, value: StringType) -> VoidType: ...
    
    def set_Port(self, value: IntType) -> VoidType: ...
    
    def set_TargetName(self, value: StringType) -> VoidType: ...
    
    def set_Timeout(self, value: IntType) -> VoidType: ...
    
    def set_UseDefaultCredentials(self, value: BooleanType) -> VoidType: ...
    
    # ---------- Events ---------- #
    
    SendCompleted: EventType[SendCompletedEventHandler] = ...
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SmtpCommands(ABC, ObjectType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SmtpConnection(ObjectType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SmtpDigestAuthenticationModule(ObjectType, ISmtpAuthenticationModule):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def AuthenticationType(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def Authenticate(self, challenge: StringType, credential: NetworkCredential, sessionCookie: ObjectType, spn: StringType, channelBindingToken: ChannelBinding) -> Authorization: ...
    
    def CloseContext(self, sessionCookie: ObjectType) -> VoidType: ...
    
    def get_AuthenticationType(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SmtpException(Exception, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, statusCode: SmtpStatusCode): ...
    
    @overload
    def __init__(self, statusCode: SmtpStatusCode, message: StringType): ...
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    # ---------- Properties ---------- #
    
    @property
    def StatusCode(self) -> SmtpStatusCode: ...
    
    @StatusCode.setter
    def StatusCode(self, value: SmtpStatusCode) -> None: ...
    
    # ---------- Methods ---------- #
    
    def GetObjectData(self, serializationInfo: SerializationInfo, streamingContext: StreamingContext) -> VoidType: ...
    
    def get_StatusCode(self) -> SmtpStatusCode: ...
    
    def set_StatusCode(self, value: SmtpStatusCode) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SmtpFailedRecipientException(SmtpException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    @overload
    def __init__(self, statusCode: SmtpStatusCode, failedRecipient: StringType): ...
    
    @overload
    def __init__(self, statusCode: SmtpStatusCode, failedRecipient: StringType, serverResponse: StringType): ...
    
    @overload
    def __init__(self, message: StringType, failedRecipient: StringType, innerException: Exception): ...
    
    # ---------- Properties ---------- #
    
    @property
    def FailedRecipient(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetObjectData(self, serializationInfo: SerializationInfo, streamingContext: StreamingContext) -> VoidType: ...
    
    def get_FailedRecipient(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SmtpFailedRecipientsException(SmtpFailedRecipientException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    @overload
    def __init__(self, message: StringType, innerExceptions: ArrayType[SmtpFailedRecipientException]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def InnerExceptions(self) -> ArrayType[SmtpFailedRecipientException]: ...
    
    # ---------- Methods ---------- #
    
    def GetObjectData(self, serializationInfo: SerializationInfo, streamingContext: StreamingContext) -> VoidType: ...
    
    def get_InnerExceptions(self) -> ArrayType[SmtpFailedRecipientException]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SmtpLoginAuthenticationModule(ObjectType, ISmtpAuthenticationModule):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def AuthenticationType(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def Authenticate(self, challenge: StringType, credential: NetworkCredential, sessionCookie: ObjectType, spn: StringType, channelBindingToken: ChannelBinding) -> Authorization: ...
    
    def CloseContext(self, sessionCookie: ObjectType) -> VoidType: ...
    
    def get_AuthenticationType(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SmtpNegotiateAuthenticationModule(ObjectType, ISmtpAuthenticationModule):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def AuthenticationType(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def Authenticate(self, challenge: StringType, credential: NetworkCredential, sessionCookie: ObjectType, spn: StringType, channelBindingToken: ChannelBinding) -> Authorization: ...
    
    def CloseContext(self, sessionCookie: ObjectType) -> VoidType: ...
    
    def get_AuthenticationType(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SmtpNtlmAuthenticationModule(ObjectType, ISmtpAuthenticationModule):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def AuthenticationType(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def Authenticate(self, challenge: StringType, credential: NetworkCredential, sessionCookie: ObjectType, spn: StringType, channelBindingToken: ChannelBinding) -> Authorization: ...
    
    def CloseContext(self, sessionCookie: ObjectType) -> VoidType: ...
    
    def get_AuthenticationType(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SmtpPermission(CodeAccessPermission, IPermission, ISecurityEncodable, IStackWalk, IUnrestrictedPermission):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, state: PermissionState): ...
    
    @overload
    def __init__(self, unrestricted: BooleanType): ...
    
    @overload
    def __init__(self, access: SmtpAccess): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Access(self) -> SmtpAccess: ...
    
    # ---------- Methods ---------- #
    
    def AddPermission(self, access: SmtpAccess) -> VoidType: ...
    
    def Copy(self) -> IPermission: ...
    
    def FromXml(self, securityElement: SecurityElement) -> VoidType: ...
    
    def Intersect(self, target: IPermission) -> IPermission: ...
    
    def IsSubsetOf(self, target: IPermission) -> BooleanType: ...
    
    def IsUnrestricted(self) -> BooleanType: ...
    
    def ToXml(self) -> SecurityElement: ...
    
    def Union(self, target: IPermission) -> IPermission: ...
    
    def get_Access(self) -> SmtpAccess: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SmtpPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, action: SecurityAction): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Access(self) -> StringType: ...
    
    @Access.setter
    def Access(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def CreatePermission(self) -> IPermission: ...
    
    def get_Access(self) -> StringType: ...
    
    def set_Access(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SmtpPooledStream(PooledStream, IDisposable):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SmtpReplyReader(ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SmtpReplyReaderFactory(ObjectType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SmtpTransport(ObjectType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class StartTlsCommand(ABC, ObjectType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class WhitespaceReader(ABC, ObjectType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class _METADATA_HANDLE_INFO(ObjectType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# ---------- Structs ---------- #

class LineInfo(ValueType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MetadataRecord(ValueType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# ---------- Interfaces ---------- #

class IMSAdminBase(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def AddKey(self, handle: NIntType, Path: StringType) -> IntType: ...
    
    def Backup(self, Location: StringType, Version: IntType, Flags: IntType) -> IntType: ...
    
    def ChangePermissions(self, handle: NIntType, TimeOut: IntType, AccessRequested: MBKeyAccess) -> VoidType: ...
    
    def CloseKey(self, handle: NIntType) -> IntType: ...
    
    def CopyData(self, sourcehandle: NIntType, SourcePath: StringType, desthandle: NIntType, DestPath: StringType, Attributes: IntType, UserType: IntType, DataType: IntType, CopyFlag: BooleanType) -> IntType: ...
    
    def CopyKey(self, source: NIntType, SourcePath: StringType, dest: NIntType, DestPath: StringType, OverwriteFlag: BooleanType, CopyFlag: BooleanType) -> VoidType: ...
    
    def DeleteAllData(self, handle: NIntType, Path: StringType, UserType: UIntType, DataType: UIntType) -> VoidType: ...
    
    def DeleteBackup(self, Location: StringType, Version: IntType) -> VoidType: ...
    
    def DeleteChildKeys(self, handle: NIntType, Path: StringType) -> VoidType: ...
    
    def DeleteData(self, key: NIntType, path: StringType, Identifier: UIntType, DataType: UIntType) -> IntType: ...
    
    def DeleteKey(self, handle: NIntType, Path: StringType) -> IntType: ...
    
    def EnumBackups(self, Location: StringType, Version: UIntType, BackupTime: FILETIME, EnumIndex: UIntType) -> Tuple[VoidType, StringType, UIntType, FILETIME]: ...
    
    def EnumData(self, key: NIntType, path: StringType, data: MetadataRecord, EnumDataIndex: IntType, RequiredDataLen: UIntType) -> Tuple[IntType, MetadataRecord, UIntType]: ...
    
    def EnumKeys(self, handle: NIntType, Path: StringType, Buffer: StringBuilder, EnumKeyIndex: IntType) -> IntType: ...
    
    def GetAllData(self, handle: NIntType, Path: StringType, Attributes: UIntType, UserType: UIntType, DataType: UIntType, NumDataEntries: UIntType, DataSetNumber: UIntType, BufferSize: UIntType, buffer: NIntType, RequiredBufferSize: UIntType) -> Tuple[IntType, UIntType, UIntType, UIntType]: ...
    
    def GetData(self, key: NIntType, path: StringType, data: MetadataRecord, RequiredDataLen: UIntType) -> Tuple[IntType, MetadataRecord, UIntType]: ...
    
    def GetDataPaths(self, handle: NIntType, Path: StringType, Identifier: IntType, DataType: IntType, BufferSize: IntType, Buffer: CharType, RequiredBufferSize: IntType) -> Tuple[VoidType, CharType, IntType]: ...
    
    def GetDataSetNumber(self, handle: NIntType, Path: StringType, DataSetNumber: UIntType) -> Tuple[VoidType, UIntType]: ...
    
    def GetHandleInfo(self, handle: NIntType, Info: _METADATA_HANDLE_INFO) -> Tuple[VoidType, _METADATA_HANDLE_INFO]: ...
    
    def GetLastChangeTime(self, handle: NIntType, Path: StringType, LastChangeTime: FILETIME, LocalTime: BooleanType) -> Tuple[IntType, FILETIME]: ...
    
    def GetServerGuid(self) -> IntType: ...
    
    def GetSystemChangeNumber(self, SystemChangeNumber: UIntType) -> Tuple[VoidType, UIntType]: ...
    
    def KeyExchangePhase1(self) -> IntType: ...
    
    def KeyExchangePhase2(self) -> IntType: ...
    
    def OpenKey(self, handle: NIntType, Path: StringType, AccessRequested: MBKeyAccess, TimeOut: IntType, NewHandle: NIntType) -> Tuple[IntType, NIntType]: ...
    
    def RenameKey(self, key: NIntType, path: StringType, newName: StringType) -> VoidType: ...
    
    def Restore(self, Location: StringType, Version: IntType, Flags: IntType) -> IntType: ...
    
    def SaveData(self) -> VoidType: ...
    
    def SetData(self, key: NIntType, path: StringType, data: MetadataRecord) -> Tuple[IntType, MetadataRecord]: ...
    
    def SetLastChangeTime(self, handle: NIntType, Path: StringType, LastChangeTime: FILETIME, LocalTime: BooleanType) -> Tuple[VoidType, FILETIME]: ...
    
    def UnmarshalInterface(self, interf: IMSAdminBase) -> Tuple[IntType, IMSAdminBase]: ...
    
    # No Events


class ISmtpAuthenticationModule(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def AuthenticationType(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def Authenticate(self, challenge: StringType, credentials: NetworkCredential, sessionCookie: ObjectType, spn: StringType, channelBindingToken: ChannelBinding) -> Authorization: ...
    
    def CloseContext(self, sessionCookie: ObjectType) -> VoidType: ...
    
    def get_AuthenticationType(self) -> StringType: ...
    
    # No Events


# ---------- Enums ---------- #

class DeliveryNotificationOptions(Enum):
    #None: IntType = 0
    OnSuccess: IntType = 1
    OnFailure: IntType = 2
    Delay: IntType = 4
    Never: IntType = 134217728


class MBDataType(Enum):
    All: ByteType = 0
    Dword: ByteType = 1
    String: ByteType = 2
    Binary: ByteType = 3
    StringExpand: ByteType = 4
    MultiString: ByteType = 5


class MBErrors(Enum):
    PathNotFound: IntType = -2147024893
    AccessDenied: IntType = -2147024891
    InvalidParameter: IntType = -2147024809
    InsufficientBuffer: IntType = -2147024774
    PathBusy: IntType = -2147024748
    AlreadyExists: IntType = -2147024713
    NoMoreItems: IntType = -2147024637
    DataNotFound: IntType = -2146646015
    InvalidVersion: IntType = -2146646014
    DuplicateNameWarning: IntType = 837636
    InvalidDataWarning: IntType = 837637


class MBKeyAccess(Enum):
    Read: UIntType = 1
    Write: UIntType = 2


class MBUserType(Enum):
    Other: ByteType = 0
    Server: ByteType = 1
    File: ByteType = 2
    Wam: ByteType = 100
    Asp: ByteType = 101


class MailHeaderID(Enum):
    Unknown: IntType = -1
    Bcc: IntType = 0
    Cc: IntType = 1
    Comments: IntType = 2
    ContentDescription: IntType = 3
    ContentDisposition: IntType = 4
    ContentID: IntType = 5
    ContentLocation: IntType = 6
    ContentTransferEncoding: IntType = 7
    ContentType: IntType = 8
    Date: IntType = 9
    From: IntType = 10
    Importance: IntType = 11
    InReplyTo: IntType = 12
    Keywords: IntType = 13
    Max: IntType = 14
    MessageID: IntType = 15
    MimeVersion: IntType = 16
    Priority: IntType = 17
    References: IntType = 18
    ReplyTo: IntType = 19
    ResentBcc: IntType = 20
    ResentCc: IntType = 21
    ResentDate: IntType = 22
    ResentFrom: IntType = 23
    ResentMessageID: IntType = 24
    ResentSender: IntType = 25
    ResentTo: IntType = 26
    Sender: IntType = 27
    Subject: IntType = 28
    To: IntType = 29
    XPriority: IntType = 30
    XReceiver: IntType = 31
    XSender: IntType = 32
    ZMaxEnumValue: IntType = 32


class MailPriority(Enum):
    Normal: IntType = 0
    Low: IntType = 1
    High: IntType = 2


class PropertyName(Enum):
    Invalid: IntType = 0
    ServerState: IntType = 1016
    PickupDirectory: IntType = 36880


class RecipientLocationType(Enum):
    Local: IntType = 0
    Unknown: IntType = 1
    NotLocal: IntType = 2
    WillForward: IntType = 3
    Ambiguous: IntType = 4


class ServerState(Enum):
    Starting: IntType = 1
    Started: IntType = 2
    Stopping: IntType = 3
    Stopped: IntType = 4
    Pausing: IntType = 5
    Paused: IntType = 6
    Continuing: IntType = 7


class SmtpAccess(Enum):
    #None: IntType = 0
    Connect: IntType = 1
    ConnectToUnrestrictedPort: IntType = 2


class SmtpDeliveryFormat(Enum):
    SevenBit: IntType = 0
    International: IntType = 1


class SmtpDeliveryMethod(Enum):
    Network: IntType = 0
    SpecifiedPickupDirectory: IntType = 1
    PickupDirectoryFromIis: IntType = 2


class SmtpStatusCode(Enum):
    GeneralFailure: IntType = -1
    SystemStatus: IntType = 211
    HelpMessage: IntType = 214
    ServiceReady: IntType = 220
    ServiceClosingTransmissionChannel: IntType = 221
    Ok: IntType = 250
    UserNotLocalWillForward: IntType = 251
    CannotVerifyUserWillAttemptDelivery: IntType = 252
    StartMailInput: IntType = 354
    ServiceNotAvailable: IntType = 421
    MailboxBusy: IntType = 450
    LocalErrorInProcessing: IntType = 451
    InsufficientStorage: IntType = 452
    ClientNotPermitted: IntType = 454
    CommandUnrecognized: IntType = 500
    SyntaxError: IntType = 501
    CommandNotImplemented: IntType = 502
    BadCommandSequence: IntType = 503
    CommandParameterNotImplemented: IntType = 504
    MustIssueStartTlsFirst: IntType = 530
    MailboxUnavailable: IntType = 550
    UserNotLocalTryAlternatePath: IntType = 551
    ExceededStorageAllocation: IntType = 552
    MailboxNameNotAllowed: IntType = 553
    TransactionFailed: IntType = 554


class SupportedAuth(Enum):
    #None: IntType = 0
    Login: IntType = 1
    NTLM: IntType = 2
    GSSAPI: IntType = 4
    WDigest: IntType = 8


# ---------- Delegates ---------- #

SendCompletedEventHandler = Callable[[ObjectType, AsyncCompletedEventArgs], VoidType]

__all__ = [
    AlternateView,
    AlternateViewCollection,
    Attachment,
    AttachmentBase,
    AttachmentCollection,
    AuthCommand,
    BufferBuilder,
    CheckCommand,
    DataCommand,
    DataStopCommand,
    DomainLiteralReader,
    DotAtomReader,
    EHelloCommand,
    HelloCommand,
    IisPickupDirectory,
    LinkedResource,
    LinkedResourceCollection,
    MSAdminBase,
    MailAddress,
    MailAddressCollection,
    MailAddressParser,
    MailCommand,
    MailHeaderInfo,
    MailMessage,
    MailWriter,
    Message,
    QuotedPairReader,
    QuotedStringFormatReader,
    ReadLinesCommand,
    RecipientCommand,
    SendCompletedEventHandler,
    SendMailAsyncResult,
    SmtpAuthenticationManager,
    SmtpClient,
    SmtpCommands,
    SmtpConnection,
    SmtpDigestAuthenticationModule,
    SmtpException,
    SmtpFailedRecipientException,
    SmtpFailedRecipientsException,
    SmtpLoginAuthenticationModule,
    SmtpNegotiateAuthenticationModule,
    SmtpNtlmAuthenticationModule,
    SmtpPermission,
    SmtpPermissionAttribute,
    SmtpPooledStream,
    SmtpReplyReader,
    SmtpReplyReaderFactory,
    SmtpTransport,
    StartTlsCommand,
    WhitespaceReader,
    _METADATA_HANDLE_INFO,
    LineInfo,
    MetadataRecord,
    IMSAdminBase,
    ISmtpAuthenticationModule,
    DeliveryNotificationOptions,
    MBDataType,
    MBErrors,
    MBKeyAccess,
    MBUserType,
    MailHeaderID,
    MailPriority,
    PropertyName,
    RecipientLocationType,
    ServerState,
    SmtpAccess,
    SmtpDeliveryFormat,
    SmtpDeliveryMethod,
    SmtpStatusCode,
    SupportedAuth,
    SendCompletedEventHandler,
]
