__all__ = [
    'AlternateView',
    'AlternateViewCollection',
    'Attachment',
    'AttachmentBase',
    'AttachmentCollection',
    'LinkedResource',
    'LinkedResourceCollection',
    'MailAddress',
    'MailAddressCollection',
    'MailMessage',
    'SmtpClient',
    'SmtpException',
    'SmtpFailedRecipientException',
    'SmtpFailedRecipientsException',
    'DeliveryNotificationOptions',
    'MailPriority',
    'SmtpDeliveryFormat',
    'SmtpDeliveryMethod',
    'SmtpStatusCode',
    'SendCompletedEventHandler',
]


# TODO

# ---------- CLASSES ---------- #

class AlternateView:
    """Represents the format to view an email message."""


class AlternateViewCollection:
    """Represents a collection of AlternateView objects."""


class Attachment:
    """Represents an attachment to an email."""


class AttachmentBase:
    """Base class that represents an email attachment. Classes Attachment, AlternateView, and LinkedResource derive from this class."""


class AttachmentCollection:
    """Stores attachments to be sent as part of an email message."""


class LinkedResource:
    """Represents an embedded external resource in an email attachment, such as an image in an HTML attachment."""


class LinkedResourceCollection:
    """Stores linked resources to be sent as part of an email message."""


class MailAddress:
    """Represents the address of an electronic mail sender or recipient."""


class MailAddressCollection:
    """Store email addresses that are associated with an email message."""


class MailMessage:
    """Represents an email message that can be sent using the SmtpClient class."""


class SmtpClient:
    """Allows applications to send email by using the Simple Mail Transfer Protocol (SMTP). The SmtpClient type is obsolete on some platforms and not recommended on others; for more information, see the Remarks section."""


class SmtpException:
    """Represents the exception that is thrown when the SmtpClient is not able to complete a Send or SendAsync operation."""


class SmtpFailedRecipientException:
    """Represents the exception that is thrown when the SmtpClient is not able to complete a Send or SendAsync operation to a particular recipient."""


class SmtpFailedRecipientsException:
    """The exception that is thrown when email is sent using an SmtpClient and cannot be delivered to all recipients."""


# ---------- ENUMS ---------- #

class DeliveryNotificationOptions:
    """Describes the delivery notification options for email."""


class MailPriority:
    """Specifies the priority of a MailMessage."""


class SmtpDeliveryFormat:
    """The delivery format to use for sending outgoing email using the Simple Mail Transport Protocol (SMTP)."""


class SmtpDeliveryMethod:
    """Specifies how email messages are delivered."""


class SmtpStatusCode:
    """Specifies the outcome of sending email by using the SmtpClient class."""


# ---------- DELEGATES ---------- #

class SendCompletedEventHandler:
    """Represents the method that will handle the SendCompleted event."""
