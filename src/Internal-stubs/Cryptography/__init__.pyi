from abc import ABC
from typing import overload

from Microsoft.Win32.SafeHandles import SafeBCryptAlgorithmHandle
from System import Array
from System import Func
from System import IDisposable
from System import Object
from System import Type
from System import ValueType
from System.Security.Cryptography import CipherMode
from System.Security.Cryptography import CngKey
from System.Security.Cryptography import CngKeyOpenOptions
from System.Security.Cryptography import CngProvider
from System.Security.Cryptography import CryptographicException
from System.Security.Cryptography import ICryptoTransform
from System.Security.Cryptography import KeySizes
from System.Security.Cryptography import PaddingMode

class BasicSymmetricCipher(ABC, Object, IDisposable):
    """"""

    @property
    def BlockSizeInBytes(self) -> int:
        """:return:"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""
    def Transform(
        self,
        input: Array[int],
        inputOffset: int,
        count: int,
        output: Array[int],
        outputOffset: int,
    ) -> int:
        """:param input:
        :param inputOffset:
        :param count:
        :param output:
        :param outputOffset:
        :return:
        """
    def TransformFinal(self, input: Array[int], inputOffset: int, count: int) -> Array[int]:
        """:param input:
        :param inputOffset:
        :param count:
        :return:
        """

class BasicSymmetricCipherBCrypt(BasicSymmetricCipher, IDisposable):
    """"""

    def __init__(
        self,
        algorithm: SafeBCryptAlgorithmHandle,
        cipherMode: CipherMode,
        blockSizeInBytes: int,
        key: Array[int],
        iv: Array[int],
        encrypting: bool,
    ):
        """:param algorithm:
        :param cipherMode:
        :param blockSizeInBytes:
        :param key:
        :param iv:
        :param encrypting:
        """
    @property
    def BlockSizeInBytes(self) -> int:
        """:return:"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""
    def Transform(
        self,
        input: Array[int],
        inputOffset: int,
        count: int,
        output: Array[int],
        outputOffset: int,
    ) -> int:
        """:param input:
        :param inputOffset:
        :param count:
        :param output:
        :param outputOffset:
        :return:
        """
    def TransformFinal(self, input: Array[int], inputOffset: int, count: int) -> Array[int]:
        """:param input:
        :param inputOffset:
        :param count:
        :return:
        """

class BasicSymmetricCipherNCrypt(BasicSymmetricCipher, IDisposable):
    """"""

    def __init__(
        self,
        cngKeyFactory: Func[CngKey],
        cipherMode: CipherMode,
        blockSizeInBytes: int,
        iv: Array[int],
        encrypting: bool,
    ):
        """:param cngKeyFactory:
        :param cipherMode:
        :param blockSizeInBytes:
        :param iv:
        :param encrypting:
        """
    @property
    def BlockSizeInBytes(self) -> int:
        """:return:"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""
    def Transform(
        self,
        input: Array[int],
        inputOffset: int,
        count: int,
        output: Array[int],
        outputOffset: int,
    ) -> int:
        """:param input:
        :param inputOffset:
        :param count:
        :param output:
        :param outputOffset:
        :return:
        """
    def TransformFinal(self, input: Array[int], inputOffset: int, count: int) -> Array[int]:
        """:param input:
        :param inputOffset:
        :param count:
        :return:
        """

class CngSymmetricAlgorithmCore(ValueType):
    """"""

    @overload
    def __init__(self, outer: ICngSymmetricAlgorithm):
        """:param outer:"""
    @overload
    def __init__(
        self,
        outer: ICngSymmetricAlgorithm,
        keyName: str,
        provider: CngProvider,
        openOptions: CngKeyOpenOptions,
    ):
        """:param outer:
        :param keyName:
        :param provider:
        :param openOptions:
        """
    @overload
    def CreateDecryptor(self) -> ICryptoTransform:
        """:return:"""
    @overload
    def CreateDecryptor(self, rgbKey: Array[int], rgbIV: Array[int]) -> ICryptoTransform:
        """:param rgbKey:
        :param rgbIV:
        :return:
        """
    @overload
    def CreateEncryptor(self) -> ICryptoTransform:
        """:return:"""
    @overload
    def CreateEncryptor(self, rgbKey: Array[int], rgbIV: Array[int]) -> ICryptoTransform:
        """:param rgbKey:
        :param rgbIV:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GenerateIV(self) -> None:
        """"""
    def GenerateKey(self) -> None:
        """"""
    def GetHashCode(self) -> int:
        """:return:"""
    def GetKeyIfExportable(self) -> Array[int]:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def SetKey(self, key: Array[int]) -> None:
        """:param key:"""
    def SetKeySize(self, keySize: int, outer: ICngSymmetricAlgorithm) -> None:
        """:param keySize:
        :param outer:
        """
    def ToString(self) -> str:
        """:return:"""

class CryptoThrowHelper(ABC, Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    @classmethod
    def ToCryptographicException(cls, hr: int) -> CryptographicException:
        """:param hr:
        :return:
        """
    def ToString(self) -> str:
        """:return:"""

class Helpers(ABC, Object):
    """"""

    @classmethod
    def BitSizeToByteSize(cls, bits: int) -> int:
        """:param bits:
        :return:
        """
    @classmethod
    def CloneByteArray(cls, src: Array[int]) -> Array[int]:
        """:param src:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    @classmethod
    def GenerateRandom(cls, count: int) -> Array[int]:
        """:param count:
        :return:
        """
    @classmethod
    def GetCipherIv(cls, cipherMode: CipherMode, iv: Array[int]) -> Array[int]:
        """:param cipherMode:
        :param iv:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    @classmethod
    def IsLegalSize(cls, size: int, legalSizes: Array[KeySizes]) -> bool:
        """:param size:
        :param legalSizes:
        :return:
        """
    @classmethod
    def ToCryptographicException(
        cls, errorCode: Interop.NCrypt.ErrorCode
    ) -> CryptographicException:
        """:param errorCode:
        :return:
        """
    def ToString(self) -> str:
        """:return:"""
    @classmethod
    def UsesIv(cls, cipherMode: CipherMode) -> bool:
        """:param cipherMode:
        :return:
        """

class ICngSymmetricAlgorithm:
    """"""

    @property
    def BaseKey(self) -> Array[int]:
        """:return:"""
    @BaseKey.setter
    def BaseKey(self, value: Array[int]) -> None: ...
    @property
    def BaseKeySize(self) -> int:
        """:return:"""
    @BaseKeySize.setter
    def BaseKeySize(self, value: int) -> None: ...
    @property
    def BlockSize(self) -> int:
        """:return:"""
    @property
    def IV(self) -> Array[int]:
        """:return:"""
    @IV.setter
    def IV(self, value: Array[int]) -> None: ...
    @property
    def LegalKeySizes(self) -> Array[KeySizes]:
        """:return:"""
    @property
    def Mode(self) -> CipherMode:
        """:return:"""
    @property
    def Padding(self) -> PaddingMode:
        """:return:"""
    def GetEphemeralModeHandle(self) -> SafeBCryptAlgorithmHandle:
        """:return:"""
    def GetNCryptAlgorithmIdentifier(self) -> str:
        """:return:"""
    def IsWeakKey(self, key: Array[int]) -> bool:
        """:param key:
        :return:
        """

class KeyPropertyName(ABC, Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class SymmetricImportExportExtensions(ABC, Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    @classmethod
    def GetSymmetricKeyDataIfExportable(cls, cngKey: CngKey, algorithm: str) -> Array[int]:
        """:param cngKey:
        :param algorithm:
        :return:
        """
    def GetType(self) -> Type:
        """:return:"""
    @classmethod
    def ToCngKey(cls, key: Array[int], algorithm: str) -> CngKey:
        """:param key:
        :param algorithm:
        :return:
        """
    def ToString(self) -> str:
        """:return:"""

class UniversalCryptoDecryptor(UniversalCryptoTransform, ICryptoTransform, IDisposable):
    """"""

    def __init__(self, paddingMode: PaddingMode, basicSymmetricCipher: BasicSymmetricCipher):
        """:param paddingMode:
        :param basicSymmetricCipher:
        """
    @property
    def CanReuseTransform(self) -> bool:
        """:return:"""
    @property
    def CanTransformMultipleBlocks(self) -> bool:
        """:return:"""
    @property
    def InputBlockSize(self) -> int:
        """:return:"""
    @property
    def OutputBlockSize(self) -> int:
        """:return:"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""
    def TransformBlock(
        self,
        inputBuffer: Array[int],
        inputOffset: int,
        inputCount: int,
        outputBuffer: Array[int],
        outputOffset: int,
    ) -> int:
        """:param inputBuffer:
        :param inputOffset:
        :param inputCount:
        :param outputBuffer:
        :param outputOffset:
        :return:
        """
    def TransformFinalBlock(
        self, inputBuffer: Array[int], inputOffset: int, inputCount: int
    ) -> Array[int]:
        """:param inputBuffer:
        :param inputOffset:
        :param inputCount:
        :return:
        """

class UniversalCryptoEncryptor(UniversalCryptoTransform, ICryptoTransform, IDisposable):
    """"""

    def __init__(self, paddingMode: PaddingMode, basicSymmetricCipher: BasicSymmetricCipher):
        """:param paddingMode:
        :param basicSymmetricCipher:
        """
    @property
    def CanReuseTransform(self) -> bool:
        """:return:"""
    @property
    def CanTransformMultipleBlocks(self) -> bool:
        """:return:"""
    @property
    def InputBlockSize(self) -> int:
        """:return:"""
    @property
    def OutputBlockSize(self) -> int:
        """:return:"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""
    def TransformBlock(
        self,
        inputBuffer: Array[int],
        inputOffset: int,
        inputCount: int,
        outputBuffer: Array[int],
        outputOffset: int,
    ) -> int:
        """:param inputBuffer:
        :param inputOffset:
        :param inputCount:
        :param outputBuffer:
        :param outputOffset:
        :return:
        """
    def TransformFinalBlock(
        self, inputBuffer: Array[int], inputOffset: int, inputCount: int
    ) -> Array[int]:
        """:param inputBuffer:
        :param inputOffset:
        :param inputCount:
        :return:
        """

class UniversalCryptoTransform(ABC, Object, ICryptoTransform, IDisposable):
    """"""

    @property
    def CanReuseTransform(self) -> bool:
        """:return:"""
    @property
    def CanTransformMultipleBlocks(self) -> bool:
        """:return:"""
    @property
    def InputBlockSize(self) -> int:
        """:return:"""
    @property
    def OutputBlockSize(self) -> int:
        """:return:"""
    @classmethod
    def Create(
        cls, paddingMode: PaddingMode, cipher: BasicSymmetricCipher, encrypting: bool
    ) -> ICryptoTransform:
        """:param paddingMode:
        :param cipher:
        :param encrypting:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""
    def TransformBlock(
        self,
        inputBuffer: Array[int],
        inputOffset: int,
        inputCount: int,
        outputBuffer: Array[int],
        outputOffset: int,
    ) -> int:
        """:param inputBuffer:
        :param inputOffset:
        :param inputCount:
        :param outputBuffer:
        :param outputOffset:
        :return:
        """
    def TransformFinalBlock(
        self, inputBuffer: Array[int], inputOffset: int, inputCount: int
    ) -> Array[int]:
        """:param inputBuffer:
        :param inputOffset:
        :param inputCount:
        :return:
        """
