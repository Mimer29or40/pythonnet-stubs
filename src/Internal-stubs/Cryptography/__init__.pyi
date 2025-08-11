"""Automatically generated stubs for C# namespace: Internal.Cryptography."""

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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class BasicSymmetricCipher(ABC, Object, IDisposable):
    """"""
    @property
    def BlockSizeInBytes(self) -> int:
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
    def Transform(
        self, input: Array[int], inputOffset: int, count: int, output: Array[int], outputOffset: int
    ) -> int:
        """"""
    def TransformFinal(self, input: Array[int], inputOffset: int, count: int) -> Array[int]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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
    ) -> None:
        """"""
    @property
    def BlockSizeInBytes(self) -> int:
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
    def Transform(
        self, input: Array[int], inputOffset: int, count: int, output: Array[int], outputOffset: int
    ) -> int:
        """"""
    def TransformFinal(self, input: Array[int], inputOffset: int, count: int) -> Array[int]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class BasicSymmetricCipherNCrypt(BasicSymmetricCipher, IDisposable):
    """"""
    def __init__(
        self,
        cngKeyFactory: Func[CngKey],
        cipherMode: CipherMode,
        blockSizeInBytes: int,
        iv: Array[int],
        encrypting: bool,
    ) -> None:
        """"""
    @property
    def BlockSizeInBytes(self) -> int:
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
    def Transform(
        self, input: Array[int], inputOffset: int, count: int, output: Array[int], outputOffset: int
    ) -> int:
        """"""
    def TransformFinal(self, input: Array[int], inputOffset: int, count: int) -> Array[int]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CngSymmetricAlgorithmCore(ValueType):
    """"""
    @overload
    def __init__(self, outer: ICngSymmetricAlgorithm) -> None:
        """"""
    @overload
    def __init__(
        self,
        outer: ICngSymmetricAlgorithm,
        keyName: str,
        provider: CngProvider,
        openOptions: CngKeyOpenOptions,
    ) -> None:
        """"""
    @overload
    def CreateDecryptor(self) -> ICryptoTransform:
        """"""
    @overload
    def CreateDecryptor(self, rgbKey: Array[int], rgbIV: Array[int]) -> ICryptoTransform:
        """"""
    @overload
    def CreateEncryptor(self) -> ICryptoTransform:
        """"""
    @overload
    def CreateEncryptor(self, rgbKey: Array[int], rgbIV: Array[int]) -> ICryptoTransform:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GenerateIV(self) -> None:
        """"""
    def GenerateKey(self) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetKeyIfExportable(self) -> Array[int]:
        """"""
    def GetType(self) -> Type:
        """"""
    def SetKey(self, key: Array[int]) -> None:
        """"""
    def SetKeySize(self, keySize: int, outer: ICngSymmetricAlgorithm) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CryptoThrowHelper(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def ToCryptographicException(cls, hr: int) -> CryptographicException:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class Helpers(ABC, Object):
    """"""
    @classmethod
    def BitSizeToByteSize(cls, bits: int) -> int:
        """"""
    @classmethod
    def CloneByteArray(cls, src: Array[int]) -> Array[int]:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def GenerateRandom(cls, count: int) -> Array[int]:
        """"""
    @classmethod
    def GetCipherIv(cls, cipherMode: CipherMode, iv: Array[int]) -> Array[int]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def IsLegalSize(cls, size: int, legalSizes: Array[KeySizes]) -> bool:
        """"""
    @classmethod
    def ToCryptographicException(
        cls, errorCode: Interop.NCrypt.ErrorCode
    ) -> CryptographicException:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def UsesIv(cls, cipherMode: CipherMode) -> bool:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ICngSymmetricAlgorithm(ABC):
    """"""
    @property
    def BaseKey(self) -> Array[int]:
        """"""
    @BaseKey.setter
    def BaseKey(self, value: Array[int]) -> None: ...
    @property
    def BaseKeySize(self) -> int:
        """"""
    @BaseKeySize.setter
    def BaseKeySize(self, value: int) -> None: ...
    @property
    def BlockSize(self) -> int:
        """"""
    @property
    def IV(self) -> Array[int]:
        """"""
    @IV.setter
    def IV(self, value: Array[int]) -> None: ...
    @property
    def LegalKeySizes(self) -> Array[KeySizes]:
        """"""
    @property
    def Mode(self) -> CipherMode:
        """"""
    @property
    def Padding(self) -> PaddingMode:
        """"""
    def GetEphemeralModeHandle(self) -> SafeBCryptAlgorithmHandle:
        """"""
    def GetNCryptAlgorithmIdentifier(self) -> str:
        """"""
    def IsWeakKey(self, key: Array[int]) -> bool:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class KeyPropertyName(ABC, Object):
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
class SymmetricImportExportExtensions(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @classmethod
    def GetSymmetricKeyDataIfExportable(cls, cngKey: CngKey, algorithm: str) -> Array[int]:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def ToCngKey(cls, key: Array[int], algorithm: str) -> CngKey:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class UniversalCryptoDecryptor(UniversalCryptoTransform, ICryptoTransform, IDisposable):
    """"""
    def __init__(
        self, paddingMode: PaddingMode, basicSymmetricCipher: BasicSymmetricCipher
    ) -> None:
        """"""
    @property
    def CanReuseTransform(self) -> bool:
        """"""
    @property
    def CanTransformMultipleBlocks(self) -> bool:
        """"""
    @property
    def InputBlockSize(self) -> int:
        """"""
    @property
    def OutputBlockSize(self) -> int:
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
    def TransformBlock(
        self,
        inputBuffer: Array[int],
        inputOffset: int,
        inputCount: int,
        outputBuffer: Array[int],
        outputOffset: int,
    ) -> int:
        """"""
    def TransformFinalBlock(
        self, inputBuffer: Array[int], inputOffset: int, inputCount: int
    ) -> Array[int]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class UniversalCryptoEncryptor(UniversalCryptoTransform, ICryptoTransform, IDisposable):
    """"""
    def __init__(
        self, paddingMode: PaddingMode, basicSymmetricCipher: BasicSymmetricCipher
    ) -> None:
        """"""
    @property
    def CanReuseTransform(self) -> bool:
        """"""
    @property
    def CanTransformMultipleBlocks(self) -> bool:
        """"""
    @property
    def InputBlockSize(self) -> int:
        """"""
    @property
    def OutputBlockSize(self) -> int:
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
    def TransformBlock(
        self,
        inputBuffer: Array[int],
        inputOffset: int,
        inputCount: int,
        outputBuffer: Array[int],
        outputOffset: int,
    ) -> int:
        """"""
    def TransformFinalBlock(
        self, inputBuffer: Array[int], inputOffset: int, inputCount: int
    ) -> Array[int]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class UniversalCryptoTransform(ABC, Object, ICryptoTransform, IDisposable):
    """"""
    @property
    def CanReuseTransform(self) -> bool:
        """"""
    @property
    def CanTransformMultipleBlocks(self) -> bool:
        """"""
    @property
    def InputBlockSize(self) -> int:
        """"""
    @property
    def OutputBlockSize(self) -> int:
        """"""
    @classmethod
    def Create(
        cls, paddingMode: PaddingMode, cipher: BasicSymmetricCipher, encrypting: bool
    ) -> ICryptoTransform:
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
    def TransformBlock(
        self,
        inputBuffer: Array[int],
        inputOffset: int,
        inputCount: int,
        outputBuffer: Array[int],
        outputOffset: int,
    ) -> int:
        """"""
    def TransformFinalBlock(
        self, inputBuffer: Array[int], inputOffset: int, inputCount: int
    ) -> Array[int]:
        """"""
