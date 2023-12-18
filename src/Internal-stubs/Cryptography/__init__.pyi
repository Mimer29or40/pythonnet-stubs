from __future__ import annotations

from abc import ABC
from typing import List
from typing import Protocol
from typing import Union
from typing import overload

from Microsoft.Win32.SafeHandles import SafeBCryptAlgorithmHandle
from System import Array
from System import Boolean
from System import Byte
from System import Func
from System import IDisposable
from System import Int32
from System import Object
from System import String
from System import ValueType
from System import Void
from System.Security.Cryptography import CipherMode
from System.Security.Cryptography import CngKey
from System.Security.Cryptography import CngKeyOpenOptions
from System.Security.Cryptography import CngProvider
from System.Security.Cryptography import CryptographicException
from System.Security.Cryptography import ICryptoTransform
from System.Security.Cryptography import KeySizes
from System.Security.Cryptography import PaddingMode

# ---------- Types ---------- #

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
ByteType = Union[int, Byte]
IntType = Union[int, Int32]
ObjectType = Object
StringType = Union[str, String]
VoidType = Union[None, Void]

# ---------- Classes ---------- #

class BasicSymmetricCipher(ABC, ObjectType, IDisposable):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def BlockSizeInBytes(self) -> IntType: ...

    # ---------- Methods ---------- #

    def Dispose(self) -> VoidType: ...
    def Transform(
        self,
        input: ArrayType[ByteType],
        inputOffset: IntType,
        count: IntType,
        output: ArrayType[ByteType],
        outputOffset: IntType,
    ) -> IntType: ...
    def TransformFinal(
        self, input: ArrayType[ByteType], inputOffset: IntType, count: IntType
    ) -> ArrayType[ByteType]: ...
    def get_BlockSizeInBytes(self) -> IntType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class BasicSymmetricCipherBCrypt(BasicSymmetricCipher, IDisposable):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(
        self,
        algorithm: SafeBCryptAlgorithmHandle,
        cipherMode: CipherMode,
        blockSizeInBytes: IntType,
        key: ArrayType[ByteType],
        iv: ArrayType[ByteType],
        encrypting: BooleanType,
    ): ...

    # No Properties

    # ---------- Methods ---------- #

    def Transform(
        self,
        input: ArrayType[ByteType],
        inputOffset: IntType,
        count: IntType,
        output: ArrayType[ByteType],
        outputOffset: IntType,
    ) -> IntType: ...
    def TransformFinal(
        self, input: ArrayType[ByteType], inputOffset: IntType, count: IntType
    ) -> ArrayType[ByteType]: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class BasicSymmetricCipherNCrypt(BasicSymmetricCipher, IDisposable):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(
        self,
        cngKeyFactory: Func[CngKey],
        cipherMode: CipherMode,
        blockSizeInBytes: IntType,
        iv: ArrayType[ByteType],
        encrypting: BooleanType,
    ): ...

    # No Properties

    # ---------- Methods ---------- #

    def Transform(
        self,
        input: ArrayType[ByteType],
        inputOffset: IntType,
        count: IntType,
        output: ArrayType[ByteType],
        outputOffset: IntType,
    ) -> IntType: ...
    def TransformFinal(
        self, input: ArrayType[ByteType], inputOffset: IntType, count: IntType
    ) -> ArrayType[ByteType]: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class CryptoThrowHelper(ABC, ObjectType):
    # No Fields

    # No Constructors

    # No Properties

    # ---------- Methods ---------- #

    @staticmethod
    def ToCryptographicException(hr: IntType) -> CryptographicException: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class Helpers(ABC, ObjectType):
    # No Fields

    # No Constructors

    # No Properties

    # ---------- Methods ---------- #

    @staticmethod
    def BitSizeToByteSize(bits: IntType) -> IntType: ...
    @staticmethod
    def CloneByteArray(src: ArrayType[ByteType]) -> ArrayType[ByteType]: ...
    @staticmethod
    def GenerateRandom(count: IntType) -> ArrayType[ByteType]: ...
    @staticmethod
    def GetCipherIv(cipherMode: CipherMode, iv: ArrayType[ByteType]) -> ArrayType[ByteType]: ...
    @staticmethod
    def IsLegalSize(size: IntType, legalSizes: ArrayType[KeySizes]) -> BooleanType: ...
    @staticmethod
    def ToCryptographicException(errorCode: ErrorCode) -> CryptographicException: ...
    @staticmethod
    def UsesIv(cipherMode: CipherMode) -> BooleanType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class KeyPropertyName(ABC, ObjectType):
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

class SymmetricImportExportExtensions(ABC, ObjectType):
    # No Fields

    # No Constructors

    # No Properties

    # ---------- Methods ---------- #

    @staticmethod
    def GetSymmetricKeyDataIfExportable(
        cngKey: CngKey, algorithm: StringType
    ) -> ArrayType[ByteType]: ...
    @staticmethod
    def ToCngKey(key: ArrayType[ByteType], algorithm: StringType) -> CngKey: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class UniversalCryptoDecryptor(UniversalCryptoTransform, ICryptoTransform, IDisposable):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, paddingMode: PaddingMode, basicSymmetricCipher: BasicSymmetricCipher): ...

    # No Properties

    # No Methods

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class UniversalCryptoEncryptor(UniversalCryptoTransform, ICryptoTransform, IDisposable):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, paddingMode: PaddingMode, basicSymmetricCipher: BasicSymmetricCipher): ...

    # No Properties

    # No Methods

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class UniversalCryptoTransform(ABC, ObjectType, ICryptoTransform, IDisposable):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def CanReuseTransform(self) -> BooleanType: ...
    @property
    def CanTransformMultipleBlocks(self) -> BooleanType: ...
    @property
    def InputBlockSize(self) -> IntType: ...
    @property
    def OutputBlockSize(self) -> IntType: ...

    # ---------- Methods ---------- #

    @staticmethod
    def Create(
        paddingMode: PaddingMode, cipher: BasicSymmetricCipher, encrypting: BooleanType
    ) -> ICryptoTransform: ...
    def Dispose(self) -> VoidType: ...
    def TransformBlock(
        self,
        inputBuffer: ArrayType[ByteType],
        inputOffset: IntType,
        inputCount: IntType,
        outputBuffer: ArrayType[ByteType],
        outputOffset: IntType,
    ) -> IntType: ...
    def TransformFinalBlock(
        self, inputBuffer: ArrayType[ByteType], inputOffset: IntType, inputCount: IntType
    ) -> ArrayType[ByteType]: ...
    def get_CanReuseTransform(self) -> BooleanType: ...
    def get_CanTransformMultipleBlocks(self) -> BooleanType: ...
    def get_InputBlockSize(self) -> IntType: ...
    def get_OutputBlockSize(self) -> IntType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

# ---------- Structs ---------- #

class CngSymmetricAlgorithmCore(ValueType):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self, outer: ICngSymmetricAlgorithm): ...
    @overload
    def __init__(
        self,
        outer: ICngSymmetricAlgorithm,
        keyName: StringType,
        provider: CngProvider,
        openOptions: CngKeyOpenOptions,
    ): ...

    # No Properties

    # ---------- Methods ---------- #

    @overload
    def CreateDecryptor(self) -> ICryptoTransform: ...
    @overload
    def CreateDecryptor(
        self, rgbKey: ArrayType[ByteType], rgbIV: ArrayType[ByteType]
    ) -> ICryptoTransform: ...
    @overload
    def CreateEncryptor(self) -> ICryptoTransform: ...
    @overload
    def CreateEncryptor(
        self, rgbKey: ArrayType[ByteType], rgbIV: ArrayType[ByteType]
    ) -> ICryptoTransform: ...
    def GenerateIV(self) -> VoidType: ...
    def GenerateKey(self) -> VoidType: ...
    def GetKeyIfExportable(self) -> ArrayType[ByteType]: ...
    def SetKey(self, key: ArrayType[ByteType]) -> VoidType: ...
    def SetKeySize(self, keySize: IntType, outer: ICngSymmetricAlgorithm) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

# ---------- Interfaces ---------- #

class ICngSymmetricAlgorithm(Protocol):
    # ---------- Properties ---------- #

    @property
    def BaseKey(self) -> ArrayType[ByteType]: ...
    @BaseKey.setter
    def BaseKey(self, value: ArrayType[ByteType]) -> None: ...
    @property
    def BaseKeySize(self) -> IntType: ...
    @BaseKeySize.setter
    def BaseKeySize(self, value: IntType) -> None: ...
    @property
    def BlockSize(self) -> IntType: ...
    @property
    def IV(self) -> ArrayType[ByteType]: ...
    @IV.setter
    def IV(self, value: ArrayType[ByteType]) -> None: ...
    @property
    def LegalKeySizes(self) -> ArrayType[KeySizes]: ...
    @property
    def Mode(self) -> CipherMode: ...
    @property
    def Padding(self) -> PaddingMode: ...

    # ---------- Methods ---------- #

    def GetEphemeralModeHandle(self) -> SafeBCryptAlgorithmHandle: ...
    def GetNCryptAlgorithmIdentifier(self) -> StringType: ...
    def IsWeakKey(self, key: ArrayType[ByteType]) -> BooleanType: ...
    def get_BaseKey(self) -> ArrayType[ByteType]: ...
    def get_BaseKeySize(self) -> IntType: ...
    def get_BlockSize(self) -> IntType: ...
    def get_IV(self) -> ArrayType[ByteType]: ...
    def get_LegalKeySizes(self) -> ArrayType[KeySizes]: ...
    def get_Mode(self) -> CipherMode: ...
    def get_Padding(self) -> PaddingMode: ...
    def set_BaseKey(self, value: ArrayType[ByteType]) -> VoidType: ...
    def set_BaseKeySize(self, value: IntType) -> VoidType: ...
    def set_IV(self, value: ArrayType[ByteType]) -> VoidType: ...

    # No Events

# No Enums

# No Delegates

__all__ = [
    BasicSymmetricCipher,
    BasicSymmetricCipherBCrypt,
    BasicSymmetricCipherNCrypt,
    CryptoThrowHelper,
    Helpers,
    KeyPropertyName,
    SymmetricImportExportExtensions,
    UniversalCryptoDecryptor,
    UniversalCryptoEncryptor,
    UniversalCryptoTransform,
    CngSymmetricAlgorithmCore,
    ICngSymmetricAlgorithm,
]
