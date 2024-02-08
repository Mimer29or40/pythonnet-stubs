from __future__ import annotations

from typing import Tuple
from typing import overload

from System import Array
from System import Func
from System import Type
from System.Collections.ObjectModel import Collection
from System.Security import ManifestKinds
from System.Security.Cryptography import AsymmetricAlgorithm
from System.Security.Cryptography import KeyedHashAlgorithm
from System.Security.Cryptography import ManifestSignatureInformation
from System.Security.Cryptography.X509Certificates import X509Certificate2
from System.Security.Cryptography.X509Certificates import X509RevocationFlag
from System.Security.Cryptography.X509Certificates import X509RevocationMode
from System.Xml import XmlDocument
from System.Xml import XmlElement
from System.Xml import XmlResolver

class ManifestSignedXml(SignedXml):
    """"""

    def __init__(self, manifestXml: XmlDocument, manifest: ManifestKinds):
        """

        :param manifestXml:
        :param manifest:
        """
    @property
    def EncryptedXml(self) -> EncryptedXml:
        """"""
    @EncryptedXml.setter
    def EncryptedXml(self, value: EncryptedXml) -> None: ...
    @property
    def KeyInfo(self) -> KeyInfo:
        """"""
    @KeyInfo.setter
    def KeyInfo(self, value: KeyInfo) -> None: ...
    @property
    def Resolver(self) -> XmlResolver:
        """"""
    @Resolver.setter
    def Resolver(self, value: XmlResolver) -> None: ...
    @property
    def SafeCanonicalizationMethods(self) -> Collection[str]:
        """"""
    @property
    def Signature(self) -> Signature:
        """"""
    @property
    def SignatureFormatValidator(self) -> Func[SignedXml, bool]:
        """"""
    @SignatureFormatValidator.setter
    def SignatureFormatValidator(self, value: Func[SignedXml, bool]) -> None: ...
    @property
    def SignatureLength(self) -> str:
        """"""
    @property
    def SignatureMethod(self) -> str:
        """"""
    @property
    def SignatureValue(self) -> Array[int]:
        """"""
    @property
    def SignedInfo(self) -> SignedInfo:
        """"""
    @property
    def SigningKey(self) -> AsymmetricAlgorithm:
        """"""
    @SigningKey.setter
    def SigningKey(self, value: AsymmetricAlgorithm) -> None: ...
    @property
    def SigningKeyName(self) -> str:
        """"""
    @SigningKeyName.setter
    def SigningKeyName(self, value: str) -> None: ...
    def AddObject(self, dataObject: DataObject) -> None:
        """"""
    def AddReference(self, reference: Reference) -> None:
        """"""
    @overload
    def CheckSignature(self) -> bool:
        """"""
    @overload
    def CheckSignature(self, key: AsymmetricAlgorithm) -> bool:
        """"""
    @overload
    def CheckSignature(self, macAlg: KeyedHashAlgorithm) -> bool:
        """"""
    @overload
    def CheckSignature(self, certificate: X509Certificate2, verifySignatureOnly: bool) -> bool:
        """"""
    def CheckSignatureReturningKey(
        self, signingKey: AsymmetricAlgorithm
    ) -> Tuple[bool, AsymmetricAlgorithm]:
        """"""
    @overload
    def ComputeSignature(self) -> None:
        """"""
    @overload
    def ComputeSignature(self, macAlg: KeyedHashAlgorithm) -> None:
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
    def GetIdElement(self, document: XmlDocument, idValue: str) -> XmlElement:
        """"""
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetXml(self) -> XmlElement:
        """"""
    def LoadXml(self, value: XmlElement) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """
    def VerifySignature(
        self, revocationFlag: X509RevocationFlag, revocationMode: X509RevocationMode
    ) -> ManifestSignatureInformation:
        """

        :param revocationFlag:
        :param revocationMode:
        :return:
        """
