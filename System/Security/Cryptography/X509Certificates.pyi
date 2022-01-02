__all__ = [
    'CertificateRequest',
    'DSACertificateExtensions',
    'ECDsaCertificateExtensions',
    'PublicKey',
    'RSACertificateExtensions',
    'SubjectAlternativeNameBuilder',
    'X500DistinguishedName',
    'X509BasicConstraintsExtension',
    'X509Certificate',
    'X509Certificate2',
    'X509Certificate2Collection',
    'X509Certificate2Enumerator',
    'X509CertificateCollection',
    'X509CertificateCollection',
    'X509Chain',
    'X509ChainElement',
    'X509ChainElementCollection',
    'X509ChainElementEnumerator',
    'X509ChainPolicy',
    'X509EnhancedKeyUsageExtension',
    'X509Extension',
    'X509ExtensionCollection',
    'X509ExtensionEnumerator',
    'X509KeyUsageExtension',
    'X509SignatureGenerator',
    'X509Store',
    'X509SubjectKeyIdentifierExtension',
    'X509ChainStatus',
    'OpenFlags',
    'StoreLocation',
    'StoreName',
    'X500DistinguishedNameFlags',
    'X509ChainStatusFlags',
    'X509ChainTrustMode',
    'X509ContentType',
    'X509FindType',
    'X509IncludeOption',
    'X509KeyStorageFlags',
    'X509KeyUsageFlags',
    'X509NameType',
    'X509RevocationFlag',
    'X509RevocationMode',
    'X509SubjectKeyIdentifierHashAlgorithm',
    'X509VerificationFlags',
]


# TODO

# ---------- CLASSES ---------- #

class CertificateRequest:
    """Represents an abstraction over the PKCS#10 CertificationRequestInfo and the X.509 TbsCertificate."""


class DSACertificateExtensions:
    """Provides extension methods for retrieving DSA implementations for the public and private keys of an X509Certificate2."""


class ECDsaCertificateExtensions:
    """Provides extension methods for retrieving ECDsa implementations for the public and private keys of a X509Certificate2 certificate."""


class PublicKey:
    """Represents a certificate's public key information. This class cannot be inherited."""


class RSACertificateExtensions:
    """Provides extension methods for retrieving RSA implementations for the public and private keys of an X509Certificate2."""


class SubjectAlternativeNameBuilder:
    """This class facilitates building a subject alternative name extension for an X.509 certificate."""


class X500DistinguishedName:
    """Represents the distinguished name of an X509 certificate. This class cannot be inherited."""


class X509BasicConstraintsExtension:
    """Defines the constraints set on a certificate. This class cannot be inherited."""


class X509Certificate:
    """Provides methods that help you use X.509 v.3 certificates."""


class X509Certificate2:
    """Represents an X.509 certificate."""


class X509Certificate2Collection:
    """Represents a collection of X509Certificate2 objects. This class cannot be inherited."""


class X509Certificate2Enumerator:
    """Supports a simple iteration over a X509Certificate2Collection object. This class cannot be inherited."""


class X509CertificateCollection:
    """Defines a collection that stores X509Certificate objects."""
    
    class X509CertificateEnumerator:
        """Enumerates the X509Certificate objects in an X509CertificateCollection."""


class X509Chain:
    """Represents a chain-building engine for X509Certificate2 certificates."""


class X509ChainElement:
    """Represents an element of an X.509 chain."""


class X509ChainElementCollection:
    """Represents a collection of X509ChainElement objects. This class cannot be inherited."""


class X509ChainElementEnumerator:
    """Supports a simple iteration over an X509ChainElementCollection. This class cannot be inherited."""


class X509ChainPolicy:
    """Represents the chain policy to be applied when building an X509 certificate chain. This class cannot be inherited."""


class X509EnhancedKeyUsageExtension:
    """Defines the collection of object identifiers (OIDs) that indicates the applications that use the key. This class cannot be inherited."""


class X509Extension:
    """Represents an X509 extension."""


class X509ExtensionCollection:
    """Represents a collection of X509Extension objects. This class cannot be inherited."""


class X509ExtensionEnumerator:
    """Supports a simple iteration over a X509ExtensionCollection. This class cannot be inherited."""


class X509KeyUsageExtension:
    """Defines the usage of a key contained within an X.509 certificate. This class cannot be inherited."""


class X509SignatureGenerator:
    """Base class for building encoded signatures as needed for X.509 certificates."""


class X509Store:
    """Represents an X.509 store, which is a physical store where certificates are persisted and managed. This class cannot be inherited."""


class X509SubjectKeyIdentifierExtension:
    """Defines a string that identifies a certificate's subject key identifier (SKI). This class cannot be inherited."""


# ---------- STRUCTS ---------- #

class X509ChainStatus:
    """Provides a simple structure for storing X509 chain status and error information."""


# ---------- ENUMS ---------- #

class OpenFlags:
    """Specifies the way to open the X.509 certificate store."""


class StoreLocation:
    """Specifies the location of the X.509 certificate store."""


class StoreName:
    """Specifies the name of the X.509 certificate store to open."""


class X500DistinguishedNameFlags:
    """Specifies characteristics of the X.500 distinguished name."""


class X509ChainStatusFlags:
    """Defines the status of an X509 chain."""


class X509ChainTrustMode:
    """The mode determining the root trust for building the certificate chain."""


class X509ContentType:
    """Specifies the format of an X.509 certificate."""


class X509FindType:
    """Specifies the type of value the Find(X509FindType, Object, Boolean) method searches for."""


class X509IncludeOption:
    """Specifies how much of the X.509 certificate chain should be included in the X.509 data."""


class X509KeyStorageFlags:
    """Defines where and how to import the private key of an X.509 certificate."""


class X509KeyUsageFlags:
    """Defines how the certificate key can be used. If this value is not defined, the key can be used for any purpose."""


class X509NameType:
    """Specifies the type of name the X509 certificate contains."""


class X509RevocationFlag:
    """Specifies which X509 certificates in the chain should be checked for revocation."""


class X509RevocationMode:
    """Specifies the mode used to check for X509 certificate revocation."""


class X509SubjectKeyIdentifierHashAlgorithm:
    """Defines the type of hash algorithm to use with the X509SubjectKeyIdentifierExtension class."""


class X509VerificationFlags:
    """Specifies conditions under which verification of certificates in the X509 chain should be conducted."""
