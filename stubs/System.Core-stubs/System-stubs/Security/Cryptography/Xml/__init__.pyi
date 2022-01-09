from __future__ import annotations

from typing import Union

from System import String
from System.Security import ManifestKinds
from System.Security.Cryptography import ManifestSignatureInformation
from System.Security.Cryptography.X509Certificates import X509RevocationFlag, X509RevocationMode
from System.Security.Cryptography.Xml import SignedXml
from System.Xml import XmlDocument, XmlElement

# ---------- Types ---------- #

StringType = Union[str, String]

# ---------- Classes ---------- #

class ManifestSignedXml(SignedXml):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, manifestXml: XmlDocument, manifest: ManifestKinds): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetIdElement(self, document: XmlDocument, idValue: StringType) -> XmlElement: ...
    
    def VerifySignature(self, revocationFlag: X509RevocationFlag, revocationMode: X509RevocationMode) -> ManifestSignatureInformation: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# No Structs

# No Interfaces

# No Enums

# No Delegates

__all__ = [
    ManifestSignedXml,
]
