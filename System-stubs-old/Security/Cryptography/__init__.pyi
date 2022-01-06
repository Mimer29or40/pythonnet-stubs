__all__ = [
    'Aes',
    'AesCcm',
    'AesCng',
    'AesCryptoServiceProvider',
    'AesGcm',
    'AesManaged',
    'AsnEncodedData',
    'AsnEncodedDataCollection',
    'AsnEncodedDataEnumerator',
    'AsymmetricAlgorithm',
    'AsymmetricKeyExchangeDeformatter',
    'AsymmetricKeyExchangeFormatter',
    'AsymmetricSignatureDeformatter',
    'AsymmetricSignatureFormatter',
    'ChaCha20Poly1305',
    'CngAlgorithm',
    'CngAlgorithmGroup',
    'CngKey',
    'CngKeyBlobFormat',
    'CngKeyCreationParameters',
    'CngPropertyCollection',
    'CngProvider',
    'CngUIPolicy',
    'CryptoConfig',
    'CryptographicException',
    'CryptographicOperations',
    'CryptographicUnexpectedOperationException',
    'CryptoStream',
    'CspKeyContainerInfo',
    'CspParameters',
    'DeriveBytes',
    'DES',
    'DESCryptoServiceProvider',
    'DSA',
    'DSACng',
    'DSACryptoServiceProvider',
    'DSAOpenSsl',
    'DSASignatureDeformatter',
    'DSASignatureFormatter',
    'ECCurve',
    'ECDiffieHellman',
    'ECDiffieHellmanCng',
    'ECDiffieHellmanCngPublicKey',
    'ECDiffieHellmanOpenSsl',
    'ECDiffieHellmanPublicKey',
    'ECDsa',
    'ECDsaCng',
    'ECDsaOpenSsl',
    'FromBase64Transform',
    'HashAlgorithm',
    'HKDF',
    'HMAC',
    'HMACMD5',
    'HMACSHA1',
    'HMACSHA256',
    'HMACSHA384',
    'HMACSHA512',
    'IncrementalHash',
    'KeyedHashAlgorithm',
    'KeySizes',
    'MaskGenerationMethod',
    'MD5',
    'MD5CryptoServiceProvider',
    'Oid',
    'OidCollection',
    'OidEnumerator',
    'PasswordDeriveBytes',
    'PbeParameters',
    'PemEncoding',
    'PKCS1MaskGenerationMethod',
    'RandomNumberGenerator',
    'RC2',
    'RC2CryptoServiceProvider',
    'Rfc2898DeriveBytes',
    'Rijndael',
    'RijndaelManaged',
    'RNGCryptoServiceProvider',
    'RSA',
    'RSACng',
    'RSACryptoServiceProvider',
    'RSAEncryptionPadding',
    'RSAOAEPKeyExchangeDeformatter',
    'RSAOAEPKeyExchangeFormatter',
    'RSAOpenSsl',
    'RSAPKCS1KeyExchangeDeformatter',
    'RSAPKCS1KeyExchangeFormatter',
    'RSAPKCS1SignatureDeformatter',
    'RSAPKCS1SignatureFormatter',
    'RSASignaturePadding',
    'SafeEvpPKeyHandle',
    'SHA1',
    'SHA1CryptoServiceProvider',
    'SHA1Managed',
    'SHA256',
    'SHA256CryptoServiceProvider',
    'SHA256Managed',
    'SHA384',
    'SHA384CryptoServiceProvider',
    'SHA384Managed',
    'SHA512',
    'SHA512CryptoServiceProvider',
    'SHA512Managed',
    'SignatureDescription',
    'SymmetricAlgorithm',
    'ToBase64Transform',
    'TripleDES',
    'TripleDESCng',
    'TripleDESCryptoServiceProvider',
    'CngProperty',
    'DSAParameters',
    'ECCurve',
    'ECParameters',
    'ECPoint',
    'HashAlgorithmName',
    'PemFields',
    'RSAParameters',
    'ICryptoTransform',
    'ICspAsymmetricAlgorithm',
    'CipherMode',
    'CngExportPolicies',
    'CngKeyCreationOptions',
    'CngKeyHandleOpenOptions',
    'CngKeyOpenOptions',
    'CngKeyUsages',
    'CngPropertyOptions',
    'CngUIProtectionLevels',
    'CryptoStreamMode',
    'CspProviderFlags',
    'DSASignatureFormat',
    'ECCurve',
    'ECDiffieHellmanKeyDerivationFunction',
    'ECKeyXmlFormat',
    'FromBase64TransformMode',
    'KeyNumber',
    'OidGroup',
    'PaddingMode',
    'PbeEncryptionAlgorithm',
    'RSAEncryptionPaddingMode',
    'RSASignaturePaddingMode',
]


# TODO

# ---------- CLASSES ---------- #

class Aes:
    """Represents the abstract base class from which all implementations of the Advanced Encryption Standard (AES) must inherit."""


class AesCcm:
    """Represents an Advanced Encryption Standard (AES) key to be used with the Counter with CBC-MAC (CCM) mode of operation."""


class AesCng:
    """Provides a Cryptography Next Generation (CNG) implementation of the Advanced Encryption Standard (AES) algorithm."""


class AesCryptoServiceProvider:
    """Performs symmetric encryption and decryption using the Cryptographic Application Programming Interfaces (CAPI) implementation of the Advanced Encryption Standard (AES) algorithm."""


class AesGcm:
    """Represents an Advanced Encryption Standard (AES) key to be used with the Galois/Counter Mode (GCM) mode of operation."""


class AesManaged:
    """Provides a managed implementation of the Advanced Encryption Standard (AES) symmetric algorithm."""


class AsnEncodedData:
    """Represents Abstract Syntax Notation One (ASN.1)-encoded data."""


class AsnEncodedDataCollection:
    """Represents a collection of AsnEncodedData objects. This class cannot be inherited."""


class AsnEncodedDataEnumerator:
    """Provides the ability to navigate through an AsnEncodedDataCollection object. This class cannot be inherited."""


class AsymmetricAlgorithm:
    """Represents the abstract base class from which all implementations of asymmetric algorithms must inherit."""


class AsymmetricKeyExchangeDeformatter:
    """Represents the base class from which all asymmetric key exchange deformatters derive."""


class AsymmetricKeyExchangeFormatter:
    """Represents the base class from which all asymmetric key exchange formatters derive."""


class AsymmetricSignatureDeformatter:
    """Represents the abstract base class from which all implementations of asymmetric signature deformatters derive."""


class AsymmetricSignatureFormatter:
    """Represents the base class from which all implementations of asymmetric signature formatters derive."""


class ChaCha20Poly1305:
    """Represents a symmetric key to be used with the ChaCha20 stream cipher in the combined mode with the Poly1305 authenticator."""


class CngAlgorithm:
    """Encapsulates the name of an encryption algorithm."""


class CngAlgorithmGroup:
    """Encapsulates the name of an encryption algorithm group."""


class CngKey:
    """Defines the core functionality for keys that are used with Cryptography Next Generation (CNG) objects."""


class CngKeyBlobFormat:
    """Specifies a key BLOB format for use with Microsoft Cryptography Next Generation (CNG) objects."""


class CngKeyCreationParameters:
    """Contains advanced properties for key creation."""


class CngPropertyCollection:
    """Provides a strongly typed collection of Cryptography Next Generation (CNG) properties."""


class CngProvider:
    """Encapsulates the name of a key storage provider (KSP) for use with Cryptography Next Generation (CNG) objects."""


class CngUIPolicy:
    """Encapsulates optional configuration parameters for the user interface (UI) that Cryptography Next Generation (CNG) displays when you access a protected key."""


class CryptoConfig:
    """Accesses the cryptography configuration information."""


class CryptographicException:
    """The exception that is thrown when an error occurs during a cryptographic operation."""


class CryptographicOperations:
    """Provides methods for use in working with cryptography to reduce the risk of side-channel information leakage."""


class CryptographicUnexpectedOperationException:
    """The exception that is thrown when an unexpected operation occurs during a cryptographic operation."""


class CryptoStream:
    """Defines a stream that links data streams to cryptographic transformations."""


class CspKeyContainerInfo:
    """Provides additional information about a cryptographic key pair. This class cannot be inherited."""


class CspParameters:
    """Contains parameters that are passed to the cryptographic service provider (CSP) that performs cryptographic computations. This class cannot be inherited."""


class DeriveBytes:
    """Represents the abstract base class from which all classes that derive byte sequences of a specified length inherit."""


class DES:
    """Represents the base class for the Data Encryption Standard (DES) algorithm from which all DES implementations must derive."""


class DESCryptoServiceProvider:
    """Defines a wrapper object to access the cryptographic service provider (CSP) version of the Data Encryption Standard (DES) algorithm. This class cannot be inherited."""


class DSA:
    """Represents the abstract base class from which all implementations of the Digital Signature Algorithm (DSA) must inherit."""


class DSACng:
    """Provides a Cryptography Next Generation (CNG) implementation of the Digital Signature Algorithm (DSA)."""


class DSACryptoServiceProvider:
    """Defines a wrapper object to access the cryptographic service provider (CSP) implementation of the DSA algorithm. This class cannot be inherited."""


class DSAOpenSsl:
    """Provides an implementation of the Digital Signature Algorithm (DSA) backed by OpenSSL."""


class DSASignatureDeformatter:
    """Verifies a Digital Signature Algorithm (DSA) PKCS#1 v1.5 signature."""


class DSASignatureFormatter:
    """Creates a Digital Signature Algorithm (DSA) signature."""


class ECDiffieHellman:
    """Provides an abstract base class that Elliptic Curve Diffie-Hellman (ECDH) algorithm implementations can derive from. This class provides the basic set of operations that all ECDH implementations must support."""


class ECDiffieHellmanCng:
    """Provides a Cryptography Next Generation (CNG) implementation of the Elliptic Curve Diffie-Hellman (ECDH) algorithm. This class is used to perform cryptographic operations."""


class ECDiffieHellmanCngPublicKey:
    """Specifies an Elliptic Curve Diffie-Hellman (ECDH) public key for use with the ECDiffieHellmanCng class."""


class ECDiffieHellmanOpenSsl:
    """Provides an implementation of the Elliptic Curve Diffie-Hellman (ECDH) algorithm backed by OpenSSL."""


class ECDiffieHellmanPublicKey:
    """Provides an abstract base class from which all ECDiffieHellmanCngPublicKey implementations must inherit."""


class ECDsa:
    """Provides an abstract base class that encapsulates the Elliptic Curve Digital Signature Algorithm (ECDSA)."""


class ECDsaCng:
    """Provides a Cryptography Next Generation (CNG) implementation of the Elliptic Curve Digital Signature Algorithm (ECDSA)."""


class ECDsaOpenSsl:
    """Provides an implementation of the Elliptic Curve Digital Signature Algorithm (ECDSA) backed by OpenSSL."""


class FromBase64Transform:
    """Converts a CryptoStream from base 64."""


class HashAlgorithm:
    """Represents the base class from which all implementations of cryptographic hash algorithms must derive."""


class HKDF:
    """RFC5869 HMAC-based Extract-and-Expand Key Derivation (HKDF)"""


class HMAC:
    """Represents the abstract class from which all implementations of Hash-based Message Authentication Code (HMAC) must derive."""


class HMACMD5:
    """Computes a Hash-based Message Authentication Code (HMAC) by using the MD5 hash function."""


class HMACSHA1:
    """Computes a Hash-based Message Authentication Code (HMAC) using the SHA1 hash function."""


class HMACSHA256:
    """Computes a Hash-based Message Authentication Code (HMAC) by using the SHA256 hash function."""


class HMACSHA384:
    """Computes a Hash-based Message Authentication Code (HMAC) using the SHA384 hash function."""


class HMACSHA512:
    """Computes a Hash-based Message Authentication Code (HMAC) using the SHA512 hash function."""


class IncrementalHash:
    """Provides support for computing a hash or Hash-based Message Authentication Code (HMAC) value incrementally across several segments."""


class KeyedHashAlgorithm:
    """Represents the abstract class from which all implementations of keyed hash algorithms must derive."""


class KeySizes:
    """Determines the set of valid key sizes for the symmetric cryptographic algorithms."""


class MaskGenerationMethod:
    """Represents the abstract class from which all mask generator algorithms must derive."""


class MD5:
    """Represents the abstract class from which all implementations of the MD5 hash algorithm inherit."""


class MD5CryptoServiceProvider:
    """Computes the MD5 hash value for the input data using the implementation provided by the cryptographic service provider (CSP). This class cannot be inherited."""


class Oid:
    """Represents a cryptographic object identifier. This class cannot be inherited."""


class OidCollection:
    """Represents a collection of Oid objects. This class cannot be inherited."""


class OidEnumerator:
    """Provides the ability to navigate through an OidCollection object. This class cannot be inherited."""


class PasswordDeriveBytes:
    """Derives a key from a password using an extension of the PBKDF1 algorithm."""


class PbeParameters:
    """Represents parameters to be used for Password-Based Encryption (PBE)."""


class PemEncoding:
    """Provides methods for reading and writing the IETF RFC 7468 subset of PEM (Privacy-Enhanced Mail) textual encodings. This class cannot be inherited."""


class PKCS1MaskGenerationMethod:
    """Computes masks according to PKCS #1 for use by key exchange algorithms."""


class RandomNumberGenerator:
    """Represents the abstract class from which all implementations of cryptographic random number generators derive."""


class RC2:
    """Represents the base class from which all implementations of the RC2 algorithm must derive."""


class RC2CryptoServiceProvider:
    """Defines a wrapper object to access the cryptographic service provider (CSP) implementation of the RC2 algorithm. This class cannot be inherited."""


class Rfc2898DeriveBytes:
    """Implements password-based key derivation functionality, PBKDF2, by using a pseudo-random number generator based on HMACSHA1."""


class Rijndael:
    """Represents the base class from which all implementations of the Rijndael symmetric encryption algorithm must inherit."""


class RijndaelManaged:
    """Accesses the managed version of the Rijndael algorithm. This class cannot be inherited."""


class RNGCryptoServiceProvider:
    """Implements a cryptographic Random Number Generator (RNG) using the implementation provided by the cryptographic service provider (CSP). This class cannot be inherited."""


class RSA:
    """Represents the base class from which all implementations of the RSA algorithm inherit."""


class RSACng:
    """Provides a Cryptography Next Generation (CNG) implementation of the RSA algorithm."""


class RSACryptoServiceProvider:
    """Performs asymmetric encryption and decryption using the implementation of the RSA algorithm provided by the cryptographic service provider (CSP). This class cannot be inherited."""


class RSAEncryptionPadding:
    """Specifies the padding mode and parameters to use with RSA encryption or decryption operations."""


class RSAOAEPKeyExchangeDeformatter:
    """Decrypts Optimal Asymmetric Encryption Padding (OAEP) key exchange data."""


class RSAOAEPKeyExchangeFormatter:
    """Creates Optimal Asymmetric Encryption Padding (OAEP) key exchange data using RSA."""


class RSAOpenSsl:
    """Provides an implementation of the RSA algorithm backed by OpenSSL."""


class RSAPKCS1KeyExchangeDeformatter:
    """Decrypts the PKCS #1 key exchange data."""


class RSAPKCS1KeyExchangeFormatter:
    """Creates the PKCS#1 key exchange data using RSA."""


class RSAPKCS1SignatureDeformatter:
    """Verifies an RSA PKCS #1 version 1.5 signature."""


class RSAPKCS1SignatureFormatter:
    """Creates an RSA PKCS #1 version 1.5 signature."""


class RSASignaturePadding:
    """Specifies the padding mode and parameters to use with RSA signature creation or verification operations."""


class SafeEvpPKeyHandle:
    """Represents the EVP_PKEY* pointer type from OpenSSL."""


class SHA1:
    """Computes the SHA1 hash for the input data."""


class SHA1CryptoServiceProvider:
    """Computes the SHA1 hash value for the input data using the implementation provided by the cryptographic service provider (CSP). This class cannot be inherited."""


class SHA1Managed:
    """Computes the SHA1 hash for the input data using the managed library."""


class SHA256:
    """Computes the SHA256 hash for the input data."""


class SHA256CryptoServiceProvider:
    """Defines a wrapper object to access the cryptographic service provider (CSP) implementation of the SHA256 algorithm."""


class SHA256Managed:
    """Computes the SHA256 hash for the input data using the managed library."""


class SHA384:
    """Computes the SHA384 hash for the input data."""


class SHA384CryptoServiceProvider:
    """Defines a wrapper object to access the cryptographic service provider (CSP) implementation of the SHA384 algorithm."""


class SHA384Managed:
    """Computes the SHA384 hash for the input data using the managed library."""


class SHA512:
    """Computes the SHA512 hash for the input data."""


class SHA512CryptoServiceProvider:
    """Defines a wrapper object to access the cryptographic service provider (CSP) implementation of the SHA512 algorithm."""


class SHA512Managed:
    """Computes the SHA512 hash algorithm for the input data using the managed library."""


class SignatureDescription:
    """Contains information about the properties of a digital signature."""


class SymmetricAlgorithm:
    """Represents the abstract base class from which all implementations of symmetric algorithms must inherit."""


class ToBase64Transform:
    """Converts a CryptoStream to base 64."""


class TripleDES:
    """Represents the base class for Triple Data Encryption Standard algorithms from which all TripleDES implementations must derive."""


class TripleDESCng:
    """Provides a Cryptography Next Generation (CNG) implementation of the Triple Data Encryption Standard (3DES) algorithm."""


class TripleDESCryptoServiceProvider:
    """Defines a wrapper object to access the cryptographic service provider (CSP) version of the TripleDES algorithm. This class cannot be inherited."""


# ---------- STRUCTS ---------- #

class CngProperty:
    """Encapsulates a property of a Cryptography Next Generation (CNG) key or provider."""


class DSAParameters:
    """Contains the typical parameters for the DSA algorithm."""


class ECCurve:
    """Represents an elliptic curve."""
    
    # ---------- CLASSES ---------- #
    
    class NamedCurves:
        """Represents a factory class for creating named curves."""
    
    # ---------- ENUMS ---------- #
    
    class ECCurveType:
        """Indicates how to interpret the data contained in an ECCurve object."""


class ECParameters:
    """Represents the standard parameters for the elliptic curve cryptography (ECC) algorithm."""


class ECPoint:
    """Represents a (X,Y) coordinate pair for elliptic curve cryptography (ECC) structures."""


class HashAlgorithmName:
    """Specifies the name of a cryptographic hash algorithm."""


class PemFields:
    """Contains information about the location of PEM data."""


class RSAParameters:
    """Represents the standard parameters for the RSA algorithm."""


# ---------- INTERFACES ---------- #

class ICryptoTransform:
    """Defines the basic operations of cryptographic transformations."""


class ICspAsymmetricAlgorithm:
    """Defines methods that allow an AsymmetricAlgorithm class to enumerate key container information, and import and export Microsoft Cryptographic API (CAPI)-compatible key blobs."""


# ---------- ENUMS ---------- #

class CipherMode:
    """Specifies the block cipher mode to use for encryption."""


class CngExportPolicies:
    """Specifies the key export policies for a key."""


class CngKeyCreationOptions:
    """Specifies options used for key creation."""


class CngKeyHandleOpenOptions:
    """Specifies options for opening key handles."""


class CngKeyOpenOptions:
    """Specifies options for opening a key."""


class CngKeyUsages:
    """Specifies the cryptographic operations that a Cryptography Next Generation (CNG) key may be used with."""


class CngPropertyOptions:
    """Specifies Cryptography Next Generation (CNG) key property options."""


class CngUIProtectionLevels:
    """Specifies the protection level for the key in user interface (UI) prompting scenarios."""


class CryptoStreamMode:
    """Specifies the mode of a cryptographic stream."""


class CspProviderFlags:
    """Specifies flags that modify the behavior of the cryptographic service providers (CSP)."""


class DSASignatureFormat:
    """Specifies the data format for signatures with the DSA family of algorithms."""


class ECDiffieHellmanKeyDerivationFunction:
    """Specifies the key derivation function that the ECDiffieHellmanCng class will use to convert secret agreements into key material."""


class ECKeyXmlFormat:
    """Defines XML serialization formats for elliptic curve keys."""


class FromBase64TransformMode:
    """Specifies whether white space should be ignored in the base 64 transformation."""


class KeyNumber:
    """Specifies whether to create an asymmetric signature key or an asymmetric exchange key."""


class OidGroup:
    """Identifies Windows cryptographic object identifier (OID) groups."""


class PaddingMode:
    """Specifies the type of padding to apply when the message data block is shorter than the full number of bytes needed for a cryptographic operation."""


class PbeEncryptionAlgorithm:
    """Specifies encryption algorithms to be used with Password-Based Encryption (PBE)."""


class RSAEncryptionPaddingMode:
    """Specifies the padding mode to use with RSA encryption or decryption operations."""


class RSASignaturePaddingMode:
    """Specifies the padding mode to use with RSA signature creation or verification operations."""
