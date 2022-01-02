__all__ = [
    'AsnContentException',
    'AsnDecoder',
    'AsnReader',
    'AsnWriter',
    'Asn1Tag',
    'AsnReaderOptions',
    'AsnEncodingRules',
    'TagClass',
    'UniversalTagNumber',
]


# TODO

# ---------- CLASSES ---------- #

class AsnContentException:
    """The exception that is thrown when an encoded ASN.1 value cannot be successfully decoded."""


class AsnDecoder:
    """Provides stateless methods for decoding BER-encoded, CER-encoded, and DER-encoded ASN.1 data."""


class AsnReader:
    """A stateful, forward-only reader for BER-, CER-, or DER-encoded ASN.1 data."""


class AsnWriter:
    """A writer for BER-, CER-, and DER-encoded ASN.1 data."""
    
    # ---------- STRUCTS ---------- #
    
    class Scope:
        """Provides an IDisposable target for safely closing an opened tag by using a lexical scope as a logical scope."""


# ---------- STRUCTS ---------- #

class Asn1Tag:
    """This type represents an ASN.1 tag, as described in ITU-T Recommendation X.680."""


class AsnReaderOptions:
    """Specifies options that modify the behavior of an AsnReader."""


# ---------- ENUMS ---------- #

class AsnEncodingRules:
    """The encoding ruleset for an AsnReader or AsnWriter."""


class TagClass:
    """The tag class for a particular ASN.1 tag."""


class UniversalTagNumber:
    """Tag assignments for the UNIVERSAL class in ITU-T X.680."""
