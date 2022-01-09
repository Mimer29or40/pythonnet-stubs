from __future__ import annotations

from abc import ABC
from typing import List, Optional, Union, overload

from Internal.Cryptography import ICngSymmetricAlgorithm
from Microsoft.Win32.SafeHandles import SafeBCryptAlgorithmHandle, SafeBCryptKeyHandle, SafeCapiKeyHandle, SafeCspHandle, SafeHandleZeroOrMinusOneIsInvalid, SafeNCryptKeyHandle, SafeNCryptProviderHandle, SafeNCryptSecretHandle
from System import ActivationContext, Array, Boolean, Byte, Enum, IDisposable, IEquatable, Int32, IntPtr, Nullable, Object, String, ValueType, Void
from System.Collections import ICollection, IEnumerable, IList
from System.Collections.Generic import ICollection, IEnumerable, IList, IReadOnlyCollection, IReadOnlyList
from System.Collections.ObjectModel import Collection, ReadOnlyCollection
from System.IO import Stream
from System.Security import ManifestKinds
from System.Security.Cryptography import Aes, AsymmetricAlgorithm, CipherMode, DSA, DSAParameters, HashAlgorithmName, ICryptoTransform, KeySizes, MD5, Oid, PaddingMode, RSA, RSAEncryptionPadding, RSAParameters, RSASignaturePadding, SHA1, SHA256, SHA384, SHA512, TripleDES
from System.Security.Cryptography.X509Certificates import AuthenticodeSignatureInformation, X509RevocationFlag, X509RevocationMode

# ---------- Types ---------- #

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
ByteType = Union[int, Byte]
IntType = Union[int, Int32]
NIntType = Union[int, IntPtr]
NullableType = Union[Optional, Nullable]
ObjectType = Object
StringType = Union[str, String]
VoidType = Union[None, Void]

# ---------- Classes ---------- #

class AesCng(Aes, IDisposable, ICngSymmetricAlgorithm):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, keyName: StringType): ...
    
    @overload
    def __init__(self, keyName: StringType, provider: CngProvider): ...
    
    @overload
    def __init__(self, keyName: StringType, provider: CngProvider, openOptions: CngKeyOpenOptions): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Key(self) -> ArrayType[ByteType]: ...
    
    @Key.setter
    def Key(self, value: ArrayType[ByteType]) -> None: ...
    
    @property
    def KeySize(self) -> IntType: ...
    
    @KeySize.setter
    def KeySize(self, value: IntType) -> None: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def CreateDecryptor(self) -> ICryptoTransform: ...
    
    @overload
    def CreateDecryptor(self, rgbKey: ArrayType[ByteType], rgbIV: ArrayType[ByteType]) -> ICryptoTransform: ...
    
    @overload
    def CreateEncryptor(self) -> ICryptoTransform: ...
    
    @overload
    def CreateEncryptor(self, rgbKey: ArrayType[ByteType], rgbIV: ArrayType[ByteType]) -> ICryptoTransform: ...
    
    def GenerateIV(self) -> VoidType: ...
    
    def GenerateKey(self) -> VoidType: ...
    
    def get_Key(self) -> ArrayType[ByteType]: ...
    
    def get_KeySize(self) -> IntType: ...
    
    def set_Key(self, value: ArrayType[ByteType]) -> VoidType: ...
    
    def set_KeySize(self, value: IntType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AesCryptoServiceProvider(Aes, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Key(self) -> ArrayType[ByteType]: ...
    
    @Key.setter
    def Key(self, value: ArrayType[ByteType]) -> None: ...
    
    @property
    def KeySize(self) -> IntType: ...
    
    @KeySize.setter
    def KeySize(self, value: IntType) -> None: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def CreateDecryptor(self) -> ICryptoTransform: ...
    
    @overload
    def CreateDecryptor(self, key: ArrayType[ByteType], iv: ArrayType[ByteType]) -> ICryptoTransform: ...
    
    @overload
    def CreateEncryptor(self) -> ICryptoTransform: ...
    
    @overload
    def CreateEncryptor(self, key: ArrayType[ByteType], iv: ArrayType[ByteType]) -> ICryptoTransform: ...
    
    def GenerateIV(self) -> VoidType: ...
    
    def GenerateKey(self) -> VoidType: ...
    
    def get_Key(self) -> ArrayType[ByteType]: ...
    
    def get_KeySize(self) -> IntType: ...
    
    def set_Key(self, value: ArrayType[ByteType]) -> VoidType: ...
    
    def set_KeySize(self, value: IntType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AesManaged(Aes, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def FeedbackSize(self) -> IntType: ...
    
    @FeedbackSize.setter
    def FeedbackSize(self, value: IntType) -> None: ...
    
    @property
    def IV(self) -> ArrayType[ByteType]: ...
    
    @IV.setter
    def IV(self, value: ArrayType[ByteType]) -> None: ...
    
    @property
    def Key(self) -> ArrayType[ByteType]: ...
    
    @Key.setter
    def Key(self, value: ArrayType[ByteType]) -> None: ...
    
    @property
    def KeySize(self) -> IntType: ...
    
    @KeySize.setter
    def KeySize(self, value: IntType) -> None: ...
    
    @property
    def Mode(self) -> CipherMode: ...
    
    @Mode.setter
    def Mode(self, value: CipherMode) -> None: ...
    
    @property
    def Padding(self) -> PaddingMode: ...
    
    @Padding.setter
    def Padding(self, value: PaddingMode) -> None: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def CreateDecryptor(self) -> ICryptoTransform: ...
    
    @overload
    def CreateDecryptor(self, key: ArrayType[ByteType], iv: ArrayType[ByteType]) -> ICryptoTransform: ...
    
    @overload
    def CreateEncryptor(self) -> ICryptoTransform: ...
    
    @overload
    def CreateEncryptor(self, key: ArrayType[ByteType], iv: ArrayType[ByteType]) -> ICryptoTransform: ...
    
    def GenerateIV(self) -> VoidType: ...
    
    def GenerateKey(self) -> VoidType: ...
    
    def get_FeedbackSize(self) -> IntType: ...
    
    def get_IV(self) -> ArrayType[ByteType]: ...
    
    def get_Key(self) -> ArrayType[ByteType]: ...
    
    def get_KeySize(self) -> IntType: ...
    
    def get_Mode(self) -> CipherMode: ...
    
    def get_Padding(self) -> PaddingMode: ...
    
    def set_FeedbackSize(self, value: IntType) -> VoidType: ...
    
    def set_IV(self, value: ArrayType[ByteType]) -> VoidType: ...
    
    def set_Key(self, value: ArrayType[ByteType]) -> VoidType: ...
    
    def set_KeySize(self, value: IntType) -> VoidType: ...
    
    def set_Mode(self, value: CipherMode) -> VoidType: ...
    
    def set_Padding(self, value: PaddingMode) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class BCryptAlgorithmHandleCache(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetCachedAlgorithmHandle(self, algorithm: StringType, implementation: StringType) -> SafeBCryptAlgorithmHandle: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class BCryptHashAlgorithm(ObjectType, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, algorithm: CngAlgorithm, implementation: StringType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Dispose(self) -> VoidType: ...
    
    def HashCore(self, array: ArrayType[ByteType], ibStart: IntType, cbSize: IntType) -> VoidType: ...
    
    def HashFinal(self) -> ArrayType[ByteType]: ...
    
    def HashStream(self, stream: Stream) -> VoidType: ...
    
    def Initialize(self) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class BCryptNative(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def BCryptDecrypt(hKey: SafeBCryptKeyHandle, input: ArrayType[ByteType], inputOffset: IntType, inputCount: IntType, iv: ArrayType[ByteType], output: ArrayType[ByteType], outputOffset: IntType, outputCount: IntType) -> IntType: ...
    
    @staticmethod
    def BCryptEncrypt(hKey: SafeBCryptKeyHandle, input: ArrayType[ByteType], inputOffset: IntType, inputCount: IntType, iv: ArrayType[ByteType], output: ArrayType[ByteType], outputOffset: IntType, outputCount: IntType) -> IntType: ...
    
    @staticmethod
    def SetCipherMode(hAlg: SafeBCryptAlgorithmHandle, cipherMode: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CapiHashAlgorithm(ObjectType, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, provider: StringType, providerType: ProviderType, algorithm: AlgorithmId): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Dispose(self) -> VoidType: ...
    
    def HashCore(self, array: ArrayType[ByteType], ibStart: IntType, cbSize: IntType) -> VoidType: ...
    
    def HashFinal(self) -> ArrayType[ByteType]: ...
    
    def Initialize(self) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CapiNative(ABC, ObjectType):
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


class CapiSymmetricAlgorithm(ObjectType, ICryptoTransform, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, blockSize: IntType, feedbackSize: IntType, provider: SafeCspHandle, key: SafeCapiKeyHandle, iv: ArrayType[ByteType], cipherMode: CipherMode, paddingMode: PaddingMode, encryptionMode: EncryptionMode): ...
    
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
    
    def Dispose(self) -> VoidType: ...
    
    def TransformBlock(self, inputBuffer: ArrayType[ByteType], inputOffset: IntType, inputCount: IntType, outputBuffer: ArrayType[ByteType], outputOffset: IntType) -> IntType: ...
    
    def TransformFinalBlock(self, inputBuffer: ArrayType[ByteType], inputOffset: IntType, inputCount: IntType) -> ArrayType[ByteType]: ...
    
    def get_CanReuseTransform(self) -> BooleanType: ...
    
    def get_CanTransformMultipleBlocks(self) -> BooleanType: ...
    
    def get_InputBlockSize(self) -> IntType: ...
    
    def get_OutputBlockSize(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CngAlgorithm(ObjectType, IEquatable[CngAlgorithm]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, algorithm: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Algorithm(self) -> StringType: ...
    
    @staticmethod
    @property
    def ECDiffieHellman() -> CngAlgorithm: ...
    
    @staticmethod
    @property
    def ECDiffieHellmanP256() -> CngAlgorithm: ...
    
    @staticmethod
    @property
    def ECDiffieHellmanP384() -> CngAlgorithm: ...
    
    @staticmethod
    @property
    def ECDiffieHellmanP521() -> CngAlgorithm: ...
    
    @staticmethod
    @property
    def ECDsa() -> CngAlgorithm: ...
    
    @staticmethod
    @property
    def ECDsaP256() -> CngAlgorithm: ...
    
    @staticmethod
    @property
    def ECDsaP384() -> CngAlgorithm: ...
    
    @staticmethod
    @property
    def ECDsaP521() -> CngAlgorithm: ...
    
    @staticmethod
    @property
    def MD5() -> CngAlgorithm: ...
    
    @staticmethod
    @property
    def Rsa() -> CngAlgorithm: ...
    
    @staticmethod
    @property
    def Sha1() -> CngAlgorithm: ...
    
    @staticmethod
    @property
    def Sha256() -> CngAlgorithm: ...
    
    @staticmethod
    @property
    def Sha384() -> CngAlgorithm: ...
    
    @staticmethod
    @property
    def Sha512() -> CngAlgorithm: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, other: CngAlgorithm) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Algorithm(self) -> StringType: ...
    
    @staticmethod
    def get_ECDiffieHellman() -> CngAlgorithm: ...
    
    @staticmethod
    def get_ECDiffieHellmanP256() -> CngAlgorithm: ...
    
    @staticmethod
    def get_ECDiffieHellmanP384() -> CngAlgorithm: ...
    
    @staticmethod
    def get_ECDiffieHellmanP521() -> CngAlgorithm: ...
    
    @staticmethod
    def get_ECDsa() -> CngAlgorithm: ...
    
    @staticmethod
    def get_ECDsaP256() -> CngAlgorithm: ...
    
    @staticmethod
    def get_ECDsaP384() -> CngAlgorithm: ...
    
    @staticmethod
    def get_ECDsaP521() -> CngAlgorithm: ...
    
    @staticmethod
    def get_MD5() -> CngAlgorithm: ...
    
    @staticmethod
    def get_Rsa() -> CngAlgorithm: ...
    
    @staticmethod
    def get_Sha1() -> CngAlgorithm: ...
    
    @staticmethod
    def get_Sha256() -> CngAlgorithm: ...
    
    @staticmethod
    def get_Sha384() -> CngAlgorithm: ...
    
    @staticmethod
    def get_Sha512() -> CngAlgorithm: ...
    
    @staticmethod
    def op_Equality(left: CngAlgorithm, right: CngAlgorithm) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(left: CngAlgorithm, right: CngAlgorithm) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CngAlgorithmGroup(ObjectType, IEquatable[CngAlgorithmGroup]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, algorithmGroup: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AlgorithmGroup(self) -> StringType: ...
    
    @staticmethod
    @property
    def DiffieHellman() -> CngAlgorithmGroup: ...
    
    @staticmethod
    @property
    def Dsa() -> CngAlgorithmGroup: ...
    
    @staticmethod
    @property
    def ECDiffieHellman() -> CngAlgorithmGroup: ...
    
    @staticmethod
    @property
    def ECDsa() -> CngAlgorithmGroup: ...
    
    @staticmethod
    @property
    def Rsa() -> CngAlgorithmGroup: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, other: CngAlgorithmGroup) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_AlgorithmGroup(self) -> StringType: ...
    
    @staticmethod
    def get_DiffieHellman() -> CngAlgorithmGroup: ...
    
    @staticmethod
    def get_Dsa() -> CngAlgorithmGroup: ...
    
    @staticmethod
    def get_ECDiffieHellman() -> CngAlgorithmGroup: ...
    
    @staticmethod
    def get_ECDsa() -> CngAlgorithmGroup: ...
    
    @staticmethod
    def get_Rsa() -> CngAlgorithmGroup: ...
    
    @staticmethod
    def op_Equality(left: CngAlgorithmGroup, right: CngAlgorithmGroup) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(left: CngAlgorithmGroup, right: CngAlgorithmGroup) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CngKey(ObjectType, IDisposable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Algorithm(self) -> CngAlgorithm: ...
    
    @property
    def AlgorithmGroup(self) -> CngAlgorithmGroup: ...
    
    @property
    def ExportPolicy(self) -> CngExportPolicies: ...
    
    @property
    def Handle(self) -> SafeNCryptKeyHandle: ...
    
    @property
    def IsEphemeral(self) -> BooleanType: ...
    
    @property
    def IsMachineKey(self) -> BooleanType: ...
    
    @property
    def KeyName(self) -> StringType: ...
    
    @property
    def KeySize(self) -> IntType: ...
    
    @property
    def KeyUsage(self) -> CngKeyUsages: ...
    
    @property
    def ParentWindowHandle(self) -> NIntType: ...
    
    @ParentWindowHandle.setter
    def ParentWindowHandle(self, value: NIntType) -> None: ...
    
    @property
    def Provider(self) -> CngProvider: ...
    
    @property
    def ProviderHandle(self) -> SafeNCryptProviderHandle: ...
    
    @property
    def UIPolicy(self) -> CngUIPolicy: ...
    
    @property
    def UniqueName(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    @overload
    def Create(algorithm: CngAlgorithm) -> CngKey: ...
    
    @staticmethod
    @overload
    def Create(algorithm: CngAlgorithm, keyName: StringType) -> CngKey: ...
    
    @staticmethod
    @overload
    def Create(algorithm: CngAlgorithm, keyName: StringType, creationParameters: CngKeyCreationParameters) -> CngKey: ...
    
    def Delete(self) -> VoidType: ...
    
    def Dispose(self) -> VoidType: ...
    
    @staticmethod
    @overload
    def Exists(keyName: StringType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def Exists(keyName: StringType, provider: CngProvider) -> BooleanType: ...
    
    @staticmethod
    @overload
    def Exists(keyName: StringType, provider: CngProvider, options: CngKeyOpenOptions) -> BooleanType: ...
    
    def Export(self, format: CngKeyBlobFormat) -> ArrayType[ByteType]: ...
    
    def GetProperty(self, name: StringType, options: CngPropertyOptions) -> CngProperty: ...
    
    def HasProperty(self, name: StringType, options: CngPropertyOptions) -> BooleanType: ...
    
    @staticmethod
    @overload
    def Import(keyBlob: ArrayType[ByteType], format: CngKeyBlobFormat) -> CngKey: ...
    
    @staticmethod
    @overload
    def Import(keyBlob: ArrayType[ByteType], format: CngKeyBlobFormat, provider: CngProvider) -> CngKey: ...
    
    @staticmethod
    @overload
    def Open(keyName: StringType) -> CngKey: ...
    
    @staticmethod
    @overload
    def Open(keyName: StringType, provider: CngProvider) -> CngKey: ...
    
    @staticmethod
    @overload
    def Open(keyName: StringType, provider: CngProvider, openOptions: CngKeyOpenOptions) -> CngKey: ...
    
    @staticmethod
    @overload
    def Open(keyHandle: SafeNCryptKeyHandle, keyHandleOpenOptions: CngKeyHandleOpenOptions) -> CngKey: ...
    
    def SetProperty(self, property: CngProperty) -> VoidType: ...
    
    def get_Algorithm(self) -> CngAlgorithm: ...
    
    def get_AlgorithmGroup(self) -> CngAlgorithmGroup: ...
    
    def get_ExportPolicy(self) -> CngExportPolicies: ...
    
    def get_Handle(self) -> SafeNCryptKeyHandle: ...
    
    def get_IsEphemeral(self) -> BooleanType: ...
    
    def get_IsMachineKey(self) -> BooleanType: ...
    
    def get_KeyName(self) -> StringType: ...
    
    def get_KeySize(self) -> IntType: ...
    
    def get_KeyUsage(self) -> CngKeyUsages: ...
    
    def get_ParentWindowHandle(self) -> NIntType: ...
    
    def get_Provider(self) -> CngProvider: ...
    
    def get_ProviderHandle(self) -> SafeNCryptProviderHandle: ...
    
    def get_UIPolicy(self) -> CngUIPolicy: ...
    
    def get_UniqueName(self) -> StringType: ...
    
    def set_ParentWindowHandle(self, value: NIntType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CngKeyBlobFormat(ObjectType, IEquatable[CngKeyBlobFormat]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, format: StringType): ...
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def EccFullPrivateBlob() -> CngKeyBlobFormat: ...
    
    @staticmethod
    @property
    def EccFullPublicBlob() -> CngKeyBlobFormat: ...
    
    @staticmethod
    @property
    def EccPrivateBlob() -> CngKeyBlobFormat: ...
    
    @staticmethod
    @property
    def EccPublicBlob() -> CngKeyBlobFormat: ...
    
    @property
    def Format(self) -> StringType: ...
    
    @staticmethod
    @property
    def GenericPrivateBlob() -> CngKeyBlobFormat: ...
    
    @staticmethod
    @property
    def GenericPublicBlob() -> CngKeyBlobFormat: ...
    
    @staticmethod
    @property
    def OpaqueTransportBlob() -> CngKeyBlobFormat: ...
    
    @staticmethod
    @property
    def Pkcs8PrivateBlob() -> CngKeyBlobFormat: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, other: CngKeyBlobFormat) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    @staticmethod
    def get_EccFullPrivateBlob() -> CngKeyBlobFormat: ...
    
    @staticmethod
    def get_EccFullPublicBlob() -> CngKeyBlobFormat: ...
    
    @staticmethod
    def get_EccPrivateBlob() -> CngKeyBlobFormat: ...
    
    @staticmethod
    def get_EccPublicBlob() -> CngKeyBlobFormat: ...
    
    def get_Format(self) -> StringType: ...
    
    @staticmethod
    def get_GenericPrivateBlob() -> CngKeyBlobFormat: ...
    
    @staticmethod
    def get_GenericPublicBlob() -> CngKeyBlobFormat: ...
    
    @staticmethod
    def get_OpaqueTransportBlob() -> CngKeyBlobFormat: ...
    
    @staticmethod
    def get_Pkcs8PrivateBlob() -> CngKeyBlobFormat: ...
    
    @staticmethod
    def op_Equality(left: CngKeyBlobFormat, right: CngKeyBlobFormat) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(left: CngKeyBlobFormat, right: CngKeyBlobFormat) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CngKeyCreationParameters(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ExportPolicy(self) -> NullableType[Nullable[CngExportPolicies]]: ...
    
    @ExportPolicy.setter
    def ExportPolicy(self, value: NullableType[Nullable[CngExportPolicies]]) -> None: ...
    
    @property
    def KeyCreationOptions(self) -> CngKeyCreationOptions: ...
    
    @KeyCreationOptions.setter
    def KeyCreationOptions(self, value: CngKeyCreationOptions) -> None: ...
    
    @property
    def KeyUsage(self) -> NullableType[Nullable[CngKeyUsages]]: ...
    
    @KeyUsage.setter
    def KeyUsage(self, value: NullableType[Nullable[CngKeyUsages]]) -> None: ...
    
    @property
    def Parameters(self) -> CngPropertyCollection: ...
    
    @property
    def ParentWindowHandle(self) -> NIntType: ...
    
    @ParentWindowHandle.setter
    def ParentWindowHandle(self, value: NIntType) -> None: ...
    
    @property
    def Provider(self) -> CngProvider: ...
    
    @Provider.setter
    def Provider(self, value: CngProvider) -> None: ...
    
    @property
    def UIPolicy(self) -> CngUIPolicy: ...
    
    @UIPolicy.setter
    def UIPolicy(self, value: CngUIPolicy) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_ExportPolicy(self) -> NullableType[Nullable[CngExportPolicies]]: ...
    
    def get_KeyCreationOptions(self) -> CngKeyCreationOptions: ...
    
    def get_KeyUsage(self) -> NullableType[Nullable[CngKeyUsages]]: ...
    
    def get_Parameters(self) -> CngPropertyCollection: ...
    
    def get_ParentWindowHandle(self) -> NIntType: ...
    
    def get_Provider(self) -> CngProvider: ...
    
    def get_UIPolicy(self) -> CngUIPolicy: ...
    
    def set_ExportPolicy(self, value: NullableType[Nullable[CngExportPolicies]]) -> VoidType: ...
    
    def set_KeyCreationOptions(self, value: CngKeyCreationOptions) -> VoidType: ...
    
    def set_KeyUsage(self, value: NullableType[Nullable[CngKeyUsages]]) -> VoidType: ...
    
    def set_ParentWindowHandle(self, value: NIntType) -> VoidType: ...
    
    def set_Provider(self, value: CngProvider) -> VoidType: ...
    
    def set_UIPolicy(self, value: CngUIPolicy) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CngPropertyCollection(Collection[CngProperty], IList[CngProperty], ICollection[CngProperty], IEnumerable[CngProperty], IEnumerable, IList, ICollection, IReadOnlyList[CngProperty], IReadOnlyCollection[CngProperty]):
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


class CngProvider(ObjectType, IEquatable[CngProvider]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, provider: StringType): ...
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def MicrosoftSmartCardKeyStorageProvider() -> CngProvider: ...
    
    @staticmethod
    @property
    def MicrosoftSoftwareKeyStorageProvider() -> CngProvider: ...
    
    @property
    def Provider(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, other: CngProvider) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    @staticmethod
    def get_MicrosoftSmartCardKeyStorageProvider() -> CngProvider: ...
    
    @staticmethod
    def get_MicrosoftSoftwareKeyStorageProvider() -> CngProvider: ...
    
    def get_Provider(self) -> StringType: ...
    
    @staticmethod
    def op_Equality(left: CngProvider, right: CngProvider) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(left: CngProvider, right: CngProvider) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CngUIPolicy(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, protectionLevel: CngUIProtectionLevels): ...
    
    @overload
    def __init__(self, protectionLevel: CngUIProtectionLevels, friendlyName: StringType): ...
    
    @overload
    def __init__(self, protectionLevel: CngUIProtectionLevels, friendlyName: StringType, description: StringType): ...
    
    @overload
    def __init__(self, protectionLevel: CngUIProtectionLevels, friendlyName: StringType, description: StringType, useContext: StringType): ...
    
    @overload
    def __init__(self, protectionLevel: CngUIProtectionLevels, friendlyName: StringType, description: StringType, useContext: StringType, creationTitle: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CreationTitle(self) -> StringType: ...
    
    @property
    def Description(self) -> StringType: ...
    
    @property
    def FriendlyName(self) -> StringType: ...
    
    @property
    def ProtectionLevel(self) -> CngUIProtectionLevels: ...
    
    @property
    def UseContext(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_CreationTitle(self) -> StringType: ...
    
    def get_Description(self) -> StringType: ...
    
    def get_FriendlyName(self) -> StringType: ...
    
    def get_ProtectionLevel(self) -> CngUIProtectionLevels: ...
    
    def get_UseContext(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DSACng(DSA, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, keySize: IntType): ...
    
    @overload
    def __init__(self, key: CngKey): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Key(self) -> CngKey: ...
    
    @property
    def KeyExchangeAlgorithm(self) -> StringType: ...
    
    @property
    def LegalKeySizes(self) -> ArrayType[KeySizes]: ...
    
    @property
    def SignatureAlgorithm(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def CreateSignature(self, rgbHash: ArrayType[ByteType]) -> ArrayType[ByteType]: ...
    
    def ExportParameters(self, includePrivateParameters: BooleanType) -> DSAParameters: ...
    
    def ImportParameters(self, parameters: DSAParameters) -> VoidType: ...
    
    def VerifySignature(self, rgbHash: ArrayType[ByteType], rgbSignature: ArrayType[ByteType]) -> BooleanType: ...
    
    def get_Key(self) -> CngKey: ...
    
    def get_KeyExchangeAlgorithm(self) -> StringType: ...
    
    def get_LegalKeySizes(self) -> ArrayType[KeySizes]: ...
    
    def get_SignatureAlgorithm(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ECCng(ABC, ObjectType):
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


class ECDiffieHellman(ABC, AsymmetricAlgorithm, IDisposable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def KeyExchangeAlgorithm(self) -> StringType: ...
    
    @property
    def PublicKey(self) -> ECDiffieHellmanPublicKey: ...
    
    @property
    def SignatureAlgorithm(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    @overload
    def Create() -> ECDiffieHellman: ...
    
    @staticmethod
    @overload
    def Create(algorithm: StringType) -> ECDiffieHellman: ...
    
    @staticmethod
    @overload
    def Create(curve: ECCurve) -> ECDiffieHellman: ...
    
    @staticmethod
    @overload
    def Create(parameters: ECParameters) -> ECDiffieHellman: ...
    
    @overload
    def DeriveKeyFromHash(self, otherPartyPublicKey: ECDiffieHellmanPublicKey, hashAlgorithm: HashAlgorithmName) -> ArrayType[ByteType]: ...
    
    @overload
    def DeriveKeyFromHash(self, otherPartyPublicKey: ECDiffieHellmanPublicKey, hashAlgorithm: HashAlgorithmName, secretPrepend: ArrayType[ByteType], secretAppend: ArrayType[ByteType]) -> ArrayType[ByteType]: ...
    
    @overload
    def DeriveKeyFromHmac(self, otherPartyPublicKey: ECDiffieHellmanPublicKey, hashAlgorithm: HashAlgorithmName, hmacKey: ArrayType[ByteType]) -> ArrayType[ByteType]: ...
    
    @overload
    def DeriveKeyFromHmac(self, otherPartyPublicKey: ECDiffieHellmanPublicKey, hashAlgorithm: HashAlgorithmName, hmacKey: ArrayType[ByteType], secretPrepend: ArrayType[ByteType], secretAppend: ArrayType[ByteType]) -> ArrayType[ByteType]: ...
    
    def DeriveKeyMaterial(self, otherPartyPublicKey: ECDiffieHellmanPublicKey) -> ArrayType[ByteType]: ...
    
    def DeriveKeyTls(self, otherPartyPublicKey: ECDiffieHellmanPublicKey, prfLabel: ArrayType[ByteType], prfSeed: ArrayType[ByteType]) -> ArrayType[ByteType]: ...
    
    def ExportExplicitParameters(self, includePrivateParameters: BooleanType) -> ECParameters: ...
    
    def ExportParameters(self, includePrivateParameters: BooleanType) -> ECParameters: ...
    
    def GenerateKey(self, curve: ECCurve) -> VoidType: ...
    
    def ImportParameters(self, parameters: ECParameters) -> VoidType: ...
    
    def get_KeyExchangeAlgorithm(self) -> StringType: ...
    
    def get_PublicKey(self) -> ECDiffieHellmanPublicKey: ...
    
    def get_SignatureAlgorithm(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ECDiffieHellmanCng(ECDiffieHellman, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, keySize: IntType): ...
    
    @overload
    def __init__(self, curve: ECCurve): ...
    
    @overload
    def __init__(self, key: CngKey): ...
    
    # ---------- Properties ---------- #
    
    @property
    def HashAlgorithm(self) -> CngAlgorithm: ...
    
    @HashAlgorithm.setter
    def HashAlgorithm(self, value: CngAlgorithm) -> None: ...
    
    @property
    def HmacKey(self) -> ArrayType[ByteType]: ...
    
    @HmacKey.setter
    def HmacKey(self, value: ArrayType[ByteType]) -> None: ...
    
    @property
    def Key(self) -> CngKey: ...
    
    @property
    def KeyDerivationFunction(self) -> ECDiffieHellmanKeyDerivationFunction: ...
    
    @KeyDerivationFunction.setter
    def KeyDerivationFunction(self, value: ECDiffieHellmanKeyDerivationFunction) -> None: ...
    
    @property
    def Label(self) -> ArrayType[ByteType]: ...
    
    @Label.setter
    def Label(self, value: ArrayType[ByteType]) -> None: ...
    
    @property
    def PublicKey(self) -> ECDiffieHellmanPublicKey: ...
    
    @property
    def SecretAppend(self) -> ArrayType[ByteType]: ...
    
    @SecretAppend.setter
    def SecretAppend(self, value: ArrayType[ByteType]) -> None: ...
    
    @property
    def SecretPrepend(self) -> ArrayType[ByteType]: ...
    
    @SecretPrepend.setter
    def SecretPrepend(self, value: ArrayType[ByteType]) -> None: ...
    
    @property
    def Seed(self) -> ArrayType[ByteType]: ...
    
    @Seed.setter
    def Seed(self, value: ArrayType[ByteType]) -> None: ...
    
    @property
    def UseSecretAgreementAsHmacKey(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def DeriveKeyFromHash(self, otherPartyPublicKey: ECDiffieHellmanPublicKey, hashAlgorithm: HashAlgorithmName, secretPrepend: ArrayType[ByteType], secretAppend: ArrayType[ByteType]) -> ArrayType[ByteType]: ...
    
    @overload
    def DeriveKeyFromHmac(self, otherPartyPublicKey: ECDiffieHellmanPublicKey, hashAlgorithm: HashAlgorithmName, hmacKey: ArrayType[ByteType], secretPrepend: ArrayType[ByteType], secretAppend: ArrayType[ByteType]) -> ArrayType[ByteType]: ...
    
    @overload
    def DeriveKeyMaterial(self, otherPartyPublicKey: ECDiffieHellmanPublicKey) -> ArrayType[ByteType]: ...
    
    @overload
    def DeriveKeyMaterial(self, otherPartyPublicKey: CngKey) -> ArrayType[ByteType]: ...
    
    def DeriveKeyTls(self, otherPartyPublicKey: ECDiffieHellmanPublicKey, prfLabel: ArrayType[ByteType], prfSeed: ArrayType[ByteType]) -> ArrayType[ByteType]: ...
    
    @overload
    def DeriveSecretAgreementHandle(self, otherPartyPublicKey: ECDiffieHellmanPublicKey) -> SafeNCryptSecretHandle: ...
    
    @overload
    def DeriveSecretAgreementHandle(self, otherPartyPublicKey: CngKey) -> SafeNCryptSecretHandle: ...
    
    def ExportExplicitParameters(self, includePrivateParameters: BooleanType) -> ECParameters: ...
    
    def ExportParameters(self, includePrivateParameters: BooleanType) -> ECParameters: ...
    
    @overload
    def FromXmlString(self, xmlString: StringType) -> VoidType: ...
    
    @overload
    def FromXmlString(self, xml: StringType, format: ECKeyXmlFormat) -> VoidType: ...
    
    def GenerateKey(self, curve: ECCurve) -> VoidType: ...
    
    def ImportParameters(self, parameters: ECParameters) -> VoidType: ...
    
    @overload
    def ToXmlString(self, includePrivateParameters: BooleanType) -> StringType: ...
    
    @overload
    def ToXmlString(self, format: ECKeyXmlFormat) -> StringType: ...
    
    def get_HashAlgorithm(self) -> CngAlgorithm: ...
    
    def get_HmacKey(self) -> ArrayType[ByteType]: ...
    
    def get_Key(self) -> CngKey: ...
    
    def get_KeyDerivationFunction(self) -> ECDiffieHellmanKeyDerivationFunction: ...
    
    def get_Label(self) -> ArrayType[ByteType]: ...
    
    def get_PublicKey(self) -> ECDiffieHellmanPublicKey: ...
    
    def get_SecretAppend(self) -> ArrayType[ByteType]: ...
    
    def get_SecretPrepend(self) -> ArrayType[ByteType]: ...
    
    def get_Seed(self) -> ArrayType[ByteType]: ...
    
    def get_UseSecretAgreementAsHmacKey(self) -> BooleanType: ...
    
    def set_HashAlgorithm(self, value: CngAlgorithm) -> VoidType: ...
    
    def set_HmacKey(self, value: ArrayType[ByteType]) -> VoidType: ...
    
    def set_KeyDerivationFunction(self, value: ECDiffieHellmanKeyDerivationFunction) -> VoidType: ...
    
    def set_Label(self, value: ArrayType[ByteType]) -> VoidType: ...
    
    def set_SecretAppend(self, value: ArrayType[ByteType]) -> VoidType: ...
    
    def set_SecretPrepend(self, value: ArrayType[ByteType]) -> VoidType: ...
    
    def set_Seed(self, value: ArrayType[ByteType]) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ECDiffieHellmanCngPublicKey(ECDiffieHellmanPublicKey, IDisposable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def BlobFormat(self) -> CngKeyBlobFormat: ...
    
    # ---------- Methods ---------- #
    
    def ExportExplicitParameters(self) -> ECParameters: ...
    
    def ExportParameters(self) -> ECParameters: ...
    
    @staticmethod
    def FromByteArray(publicKeyBlob: ArrayType[ByteType], format: CngKeyBlobFormat) -> ECDiffieHellmanPublicKey: ...
    
    @staticmethod
    def FromXmlString(xml: StringType) -> ECDiffieHellmanCngPublicKey: ...
    
    def Import(self) -> CngKey: ...
    
    def ToXmlString(self) -> StringType: ...
    
    def get_BlobFormat(self) -> CngKeyBlobFormat: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ECDiffieHellmanPublicKey(ABC, ObjectType, IDisposable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Dispose(self) -> VoidType: ...
    
    def ExportExplicitParameters(self) -> ECParameters: ...
    
    def ExportParameters(self) -> ECParameters: ...
    
    def ToByteArray(self) -> ArrayType[ByteType]: ...
    
    def ToXmlString(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ECDsa(ABC, AsymmetricAlgorithm, IDisposable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def KeyExchangeAlgorithm(self) -> StringType: ...
    
    @property
    def SignatureAlgorithm(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    @overload
    def Create() -> ECDsa: ...
    
    @staticmethod
    @overload
    def Create(algorithm: StringType) -> ECDsa: ...
    
    @staticmethod
    @overload
    def Create(curve: ECCurve) -> ECDsa: ...
    
    @staticmethod
    @overload
    def Create(parameters: ECParameters) -> ECDsa: ...
    
    def ExportExplicitParameters(self, includePrivateParameters: BooleanType) -> ECParameters: ...
    
    def ExportParameters(self, includePrivateParameters: BooleanType) -> ECParameters: ...
    
    def GenerateKey(self, curve: ECCurve) -> VoidType: ...
    
    def ImportParameters(self, parameters: ECParameters) -> VoidType: ...
    
    @overload
    def SignData(self, data: ArrayType[ByteType], hashAlgorithm: HashAlgorithmName) -> ArrayType[ByteType]: ...
    
    @overload
    def SignData(self, data: ArrayType[ByteType], offset: IntType, count: IntType, hashAlgorithm: HashAlgorithmName) -> ArrayType[ByteType]: ...
    
    @overload
    def SignData(self, data: Stream, hashAlgorithm: HashAlgorithmName) -> ArrayType[ByteType]: ...
    
    def SignHash(self, hash: ArrayType[ByteType]) -> ArrayType[ByteType]: ...
    
    @overload
    def VerifyData(self, data: ArrayType[ByteType], signature: ArrayType[ByteType], hashAlgorithm: HashAlgorithmName) -> BooleanType: ...
    
    @overload
    def VerifyData(self, data: ArrayType[ByteType], offset: IntType, count: IntType, signature: ArrayType[ByteType], hashAlgorithm: HashAlgorithmName) -> BooleanType: ...
    
    @overload
    def VerifyData(self, data: Stream, signature: ArrayType[ByteType], hashAlgorithm: HashAlgorithmName) -> BooleanType: ...
    
    def VerifyHash(self, hash: ArrayType[ByteType], signature: ArrayType[ByteType]) -> BooleanType: ...
    
    def get_KeyExchangeAlgorithm(self) -> StringType: ...
    
    def get_SignatureAlgorithm(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ECDsaCng(ECDsa, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, keySize: IntType): ...
    
    @overload
    def __init__(self, curve: ECCurve): ...
    
    @overload
    def __init__(self, key: CngKey): ...
    
    # ---------- Properties ---------- #
    
    @property
    def HashAlgorithm(self) -> CngAlgorithm: ...
    
    @HashAlgorithm.setter
    def HashAlgorithm(self, value: CngAlgorithm) -> None: ...
    
    @property
    def Key(self) -> CngKey: ...
    
    # ---------- Methods ---------- #
    
    def ExportExplicitParameters(self, includePrivateParameters: BooleanType) -> ECParameters: ...
    
    def ExportParameters(self, includePrivateParameters: BooleanType) -> ECParameters: ...
    
    @overload
    def FromXmlString(self, xmlString: StringType) -> VoidType: ...
    
    @overload
    def FromXmlString(self, xml: StringType, format: ECKeyXmlFormat) -> VoidType: ...
    
    def GenerateKey(self, curve: ECCurve) -> VoidType: ...
    
    def ImportParameters(self, parameters: ECParameters) -> VoidType: ...
    
    @overload
    def SignData(self, data: ArrayType[ByteType]) -> ArrayType[ByteType]: ...
    
    @overload
    def SignData(self, data: ArrayType[ByteType], offset: IntType, count: IntType) -> ArrayType[ByteType]: ...
    
    @overload
    def SignData(self, data: Stream) -> ArrayType[ByteType]: ...
    
    def SignHash(self, hash: ArrayType[ByteType]) -> ArrayType[ByteType]: ...
    
    @overload
    def ToXmlString(self, includePrivateParameters: BooleanType) -> StringType: ...
    
    @overload
    def ToXmlString(self, format: ECKeyXmlFormat) -> StringType: ...
    
    @overload
    def VerifyData(self, data: ArrayType[ByteType], signature: ArrayType[ByteType]) -> BooleanType: ...
    
    @overload
    def VerifyData(self, data: ArrayType[ByteType], offset: IntType, count: IntType, signature: ArrayType[ByteType]) -> BooleanType: ...
    
    @overload
    def VerifyData(self, data: Stream, signature: ArrayType[ByteType]) -> BooleanType: ...
    
    def VerifyHash(self, hash: ArrayType[ByteType], signature: ArrayType[ByteType]) -> BooleanType: ...
    
    def get_HashAlgorithm(self) -> CngAlgorithm: ...
    
    def get_Key(self) -> CngKey: ...
    
    def set_HashAlgorithm(self, value: CngAlgorithm) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IncrementalHash(ObjectType, IDisposable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def AlgorithmName(self) -> HashAlgorithmName: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def AppendData(self, data: ArrayType[ByteType]) -> VoidType: ...
    
    @overload
    def AppendData(self, data: ArrayType[ByteType], offset: IntType, count: IntType) -> VoidType: ...
    
    @staticmethod
    def CreateHMAC(hashAlgorithm: HashAlgorithmName, key: ArrayType[ByteType]) -> IncrementalHash: ...
    
    @staticmethod
    def CreateHash(hashAlgorithm: HashAlgorithmName) -> IncrementalHash: ...
    
    def Dispose(self) -> VoidType: ...
    
    def GetHashAndReset(self) -> ArrayType[ByteType]: ...
    
    def get_AlgorithmName(self) -> HashAlgorithmName: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MD5Cng(MD5, IDisposable, ICryptoTransform):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Initialize(self) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ManifestSignatureInformation(ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def AuthenticodeSignature(self) -> AuthenticodeSignatureInformation: ...
    
    @property
    def Manifest(self) -> ManifestKinds: ...
    
    @property
    def StrongNameSignature(self) -> StrongNameSignatureInformation: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    @overload
    def VerifySignature(application: ActivationContext) -> ManifestSignatureInformationCollection: ...
    
    @staticmethod
    @overload
    def VerifySignature(application: ActivationContext, manifests: ManifestKinds) -> ManifestSignatureInformationCollection: ...
    
    @staticmethod
    @overload
    def VerifySignature(application: ActivationContext, manifests: ManifestKinds, revocationFlag: X509RevocationFlag, revocationMode: X509RevocationMode) -> ManifestSignatureInformationCollection: ...
    
    def get_AuthenticodeSignature(self) -> AuthenticodeSignatureInformation: ...
    
    def get_Manifest(self) -> ManifestKinds: ...
    
    def get_StrongNameSignature(self) -> StrongNameSignatureInformation: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ManifestSignatureInformationCollection(ReadOnlyCollection[ManifestSignatureInformation], IList[ManifestSignatureInformation], ICollection[ManifestSignatureInformation], IEnumerable[ManifestSignatureInformation], IEnumerable, IList, ICollection, IReadOnlyList[ManifestSignatureInformation], IReadOnlyCollection[ManifestSignatureInformation]):
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


class NCryptNative(ABC, ObjectType):
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


class RSACng(RSA, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, keySize: IntType): ...
    
    @overload
    def __init__(self, key: CngKey): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Key(self) -> CngKey: ...
    
    @property
    def KeyExchangeAlgorithm(self) -> StringType: ...
    
    @property
    def SignatureAlgorithm(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def Decrypt(self, data: ArrayType[ByteType], padding: RSAEncryptionPadding) -> ArrayType[ByteType]: ...
    
    def DecryptValue(self, rgb: ArrayType[ByteType]) -> ArrayType[ByteType]: ...
    
    def Encrypt(self, data: ArrayType[ByteType], padding: RSAEncryptionPadding) -> ArrayType[ByteType]: ...
    
    def EncryptValue(self, rgb: ArrayType[ByteType]) -> ArrayType[ByteType]: ...
    
    def ExportParameters(self, includePrivateParameters: BooleanType) -> RSAParameters: ...
    
    def ImportParameters(self, parameters: RSAParameters) -> VoidType: ...
    
    def SignHash(self, hash: ArrayType[ByteType], hashAlgorithm: HashAlgorithmName, padding: RSASignaturePadding) -> ArrayType[ByteType]: ...
    
    def VerifyHash(self, hash: ArrayType[ByteType], signature: ArrayType[ByteType], hashAlgorithm: HashAlgorithmName, padding: RSASignaturePadding) -> BooleanType: ...
    
    def get_Key(self) -> CngKey: ...
    
    def get_KeyExchangeAlgorithm(self) -> StringType: ...
    
    def get_SignatureAlgorithm(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Rfc4050KeyFormatter(ABC, ObjectType):
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


class SHA1Cng(SHA1, IDisposable, ICryptoTransform):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Initialize(self) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SHA256Cng(SHA256, IDisposable, ICryptoTransform):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Initialize(self) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SHA256CryptoServiceProvider(SHA256, IDisposable, ICryptoTransform):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Initialize(self) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SHA384Cng(SHA384, IDisposable, ICryptoTransform):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Initialize(self) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SHA384CryptoServiceProvider(SHA384, IDisposable, ICryptoTransform):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Initialize(self) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SHA512Cng(SHA512, IDisposable, ICryptoTransform):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Initialize(self) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SHA512CryptoServiceProvider(SHA512, IDisposable, ICryptoTransform):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Initialize(self) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SafeLocalAllocHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
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


class StrongNameSignatureInformation(ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def HResult(self) -> IntType: ...
    
    @property
    def HashAlgorithm(self) -> StringType: ...
    
    @property
    def IsValid(self) -> BooleanType: ...
    
    @property
    def PublicKey(self) -> AsymmetricAlgorithm: ...
    
    @property
    def VerificationResult(self) -> SignatureVerificationResult: ...
    
    # ---------- Methods ---------- #
    
    def get_HResult(self) -> IntType: ...
    
    def get_HashAlgorithm(self) -> StringType: ...
    
    def get_IsValid(self) -> BooleanType: ...
    
    def get_PublicKey(self) -> AsymmetricAlgorithm: ...
    
    def get_VerificationResult(self) -> SignatureVerificationResult: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TripleDESCng(TripleDES, IDisposable, ICngSymmetricAlgorithm):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, keyName: StringType): ...
    
    @overload
    def __init__(self, keyName: StringType, provider: CngProvider): ...
    
    @overload
    def __init__(self, keyName: StringType, provider: CngProvider, openOptions: CngKeyOpenOptions): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Key(self) -> ArrayType[ByteType]: ...
    
    @Key.setter
    def Key(self, value: ArrayType[ByteType]) -> None: ...
    
    @property
    def KeySize(self) -> IntType: ...
    
    @KeySize.setter
    def KeySize(self, value: IntType) -> None: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def CreateDecryptor(self) -> ICryptoTransform: ...
    
    @overload
    def CreateDecryptor(self, rgbKey: ArrayType[ByteType], rgbIV: ArrayType[ByteType]) -> ICryptoTransform: ...
    
    @overload
    def CreateEncryptor(self) -> ICryptoTransform: ...
    
    @overload
    def CreateEncryptor(self, rgbKey: ArrayType[ByteType], rgbIV: ArrayType[ByteType]) -> ICryptoTransform: ...
    
    def GenerateIV(self) -> VoidType: ...
    
    def GenerateKey(self) -> VoidType: ...
    
    def get_Key(self) -> ArrayType[ByteType]: ...
    
    def get_KeySize(self) -> IntType: ...
    
    def set_Key(self, value: ArrayType[ByteType]) -> VoidType: ...
    
    def set_KeySize(self, value: IntType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class X509Utils(ObjectType):
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


# ---------- Structs ---------- #

class BCRYPT_DSA_KEY_BLOB_V2(ValueType):
    # ---------- Fields ---------- #
    
    @property
    def Count0(self) -> ByteType: ...
    
    @Count0.setter
    def Count0(self, value: ByteType) -> None: ...
    
    @property
    def Count1(self) -> ByteType: ...
    
    @Count1.setter
    def Count1(self, value: ByteType) -> None: ...
    
    @property
    def Count2(self) -> ByteType: ...
    
    @Count2.setter
    def Count2(self, value: ByteType) -> None: ...
    
    @property
    def Count3(self) -> ByteType: ...
    
    @Count3.setter
    def Count3(self, value: ByteType) -> None: ...
    
    @property
    def cbGroupSize(self) -> IntType: ...
    
    @cbGroupSize.setter
    def cbGroupSize(self, value: IntType) -> None: ...
    
    @property
    def cbKey(self) -> IntType: ...
    
    @cbKey.setter
    def cbKey(self, value: IntType) -> None: ...
    
    @property
    def cbSeedLength(self) -> IntType: ...
    
    @cbSeedLength.setter
    def cbSeedLength(self, value: IntType) -> None: ...
    
    @property
    def dwMagic(self) -> KeyBlobMagicNumber: ...
    
    @dwMagic.setter
    def dwMagic(self, value: KeyBlobMagicNumber) -> None: ...
    
    @property
    def hashAlgorithm(self) -> HASHALGORITHM_ENUM: ...
    
    @hashAlgorithm.setter
    def hashAlgorithm(self, value: HASHALGORITHM_ENUM) -> None: ...
    
    @property
    def standardVersion(self) -> DSAFIPSVERSION_ENUM: ...
    
    @standardVersion.setter
    def standardVersion(self, value: DSAFIPSVERSION_ENUM) -> None: ...
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CngProperty(ValueType, IEquatable[CngProperty]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, name: StringType, value: ArrayType[ByteType], options: CngPropertyOptions): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def Options(self) -> CngPropertyOptions: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, other: CngProperty) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def GetValue(self) -> ArrayType[ByteType]: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_Options(self) -> CngPropertyOptions: ...
    
    @staticmethod
    def op_Equality(left: CngProperty, right: CngProperty) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(left: CngProperty, right: CngProperty) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ECCurve(ValueType):
    # ---------- Fields ---------- #
    
    @property
    def A(self) -> ArrayType[ByteType]: ...
    
    @A.setter
    def A(self, value: ArrayType[ByteType]) -> None: ...
    
    @property
    def B(self) -> ArrayType[ByteType]: ...
    
    @B.setter
    def B(self, value: ArrayType[ByteType]) -> None: ...
    
    @property
    def Cofactor(self) -> ArrayType[ByteType]: ...
    
    @Cofactor.setter
    def Cofactor(self, value: ArrayType[ByteType]) -> None: ...
    
    @property
    def CurveType(self) -> ECCurveType: ...
    
    @CurveType.setter
    def CurveType(self, value: ECCurveType) -> None: ...
    
    @property
    def G(self) -> ECPoint: ...
    
    @G.setter
    def G(self, value: ECPoint) -> None: ...
    
    @property
    def Hash(self) -> NullableType[Nullable[HashAlgorithmName]]: ...
    
    @Hash.setter
    def Hash(self, value: NullableType[Nullable[HashAlgorithmName]]) -> None: ...
    
    @property
    def Order(self) -> ArrayType[ByteType]: ...
    
    @Order.setter
    def Order(self, value: ArrayType[ByteType]) -> None: ...
    
    @property
    def Polynomial(self) -> ArrayType[ByteType]: ...
    
    @Polynomial.setter
    def Polynomial(self, value: ArrayType[ByteType]) -> None: ...
    
    @property
    def Prime(self) -> ArrayType[ByteType]: ...
    
    @Prime.setter
    def Prime(self, value: ArrayType[ByteType]) -> None: ...
    
    @property
    def Seed(self) -> ArrayType[ByteType]: ...
    
    @Seed.setter
    def Seed(self, value: ArrayType[ByteType]) -> None: ...
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def IsCharacteristic2(self) -> BooleanType: ...
    
    @property
    def IsExplicit(self) -> BooleanType: ...
    
    @property
    def IsNamed(self) -> BooleanType: ...
    
    @property
    def IsPrime(self) -> BooleanType: ...
    
    @property
    def Oid(self) -> Oid: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def CreateFromFriendlyName(oidFriendlyName: StringType) -> ECCurve: ...
    
    @staticmethod
    def CreateFromOid(curveOid: Oid) -> ECCurve: ...
    
    @staticmethod
    def CreateFromValue(oidValue: StringType) -> ECCurve: ...
    
    def Validate(self) -> VoidType: ...
    
    def get_IsCharacteristic2(self) -> BooleanType: ...
    
    def get_IsExplicit(self) -> BooleanType: ...
    
    def get_IsNamed(self) -> BooleanType: ...
    
    def get_IsPrime(self) -> BooleanType: ...
    
    def get_Oid(self) -> Oid: ...
    
    # No Events
    
    
    # ---------- Sub Classes ---------- #
    
    class NamedCurves(ABC, ObjectType):
        # No Fields
        
        # No Constructors
        
        # ---------- Properties ---------- #
        
        @staticmethod
        @property
        def brainpoolP160r1() -> ECCurve: ...
        
        @staticmethod
        @property
        def brainpoolP160t1() -> ECCurve: ...
        
        @staticmethod
        @property
        def brainpoolP192r1() -> ECCurve: ...
        
        @staticmethod
        @property
        def brainpoolP192t1() -> ECCurve: ...
        
        @staticmethod
        @property
        def brainpoolP224r1() -> ECCurve: ...
        
        @staticmethod
        @property
        def brainpoolP224t1() -> ECCurve: ...
        
        @staticmethod
        @property
        def brainpoolP256r1() -> ECCurve: ...
        
        @staticmethod
        @property
        def brainpoolP256t1() -> ECCurve: ...
        
        @staticmethod
        @property
        def brainpoolP320r1() -> ECCurve: ...
        
        @staticmethod
        @property
        def brainpoolP320t1() -> ECCurve: ...
        
        @staticmethod
        @property
        def brainpoolP384r1() -> ECCurve: ...
        
        @staticmethod
        @property
        def brainpoolP384t1() -> ECCurve: ...
        
        @staticmethod
        @property
        def brainpoolP512r1() -> ECCurve: ...
        
        @staticmethod
        @property
        def brainpoolP512t1() -> ECCurve: ...
        
        @staticmethod
        @property
        def nistP256() -> ECCurve: ...
        
        @staticmethod
        @property
        def nistP384() -> ECCurve: ...
        
        @staticmethod
        @property
        def nistP521() -> ECCurve: ...
        
        # ---------- Methods ---------- #
        
        @staticmethod
        def get_brainpoolP160r1() -> ECCurve: ...
        
        @staticmethod
        def get_brainpoolP160t1() -> ECCurve: ...
        
        @staticmethod
        def get_brainpoolP192r1() -> ECCurve: ...
        
        @staticmethod
        def get_brainpoolP192t1() -> ECCurve: ...
        
        @staticmethod
        def get_brainpoolP224r1() -> ECCurve: ...
        
        @staticmethod
        def get_brainpoolP224t1() -> ECCurve: ...
        
        @staticmethod
        def get_brainpoolP256r1() -> ECCurve: ...
        
        @staticmethod
        def get_brainpoolP256t1() -> ECCurve: ...
        
        @staticmethod
        def get_brainpoolP320r1() -> ECCurve: ...
        
        @staticmethod
        def get_brainpoolP320t1() -> ECCurve: ...
        
        @staticmethod
        def get_brainpoolP384r1() -> ECCurve: ...
        
        @staticmethod
        def get_brainpoolP384t1() -> ECCurve: ...
        
        @staticmethod
        def get_brainpoolP512r1() -> ECCurve: ...
        
        @staticmethod
        def get_brainpoolP512t1() -> ECCurve: ...
        
        @staticmethod
        def get_nistP256() -> ECCurve: ...
        
        @staticmethod
        def get_nistP384() -> ECCurve: ...
        
        @staticmethod
        def get_nistP521() -> ECCurve: ...
        
        # No Events
        
        # No Sub Classes
        
        # No Sub Structs
        
        # No Sub Interfaces
        
        # No Sub Enums
    
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # ---------- Sub Enums ---------- #
    
    class ECCurveType(Enum):
        Implicit: IntType = 0
        PrimeShortWeierstrass: IntType = 1
        PrimeTwistedEdwards: IntType = 2
        PrimeMontgomery: IntType = 3
        Characteristic2: IntType = 4
        Named: IntType = 5
    


class ECParameters(ValueType):
    # ---------- Fields ---------- #
    
    @property
    def Curve(self) -> ECCurve: ...
    
    @Curve.setter
    def Curve(self, value: ECCurve) -> None: ...
    
    @property
    def D(self) -> ArrayType[ByteType]: ...
    
    @D.setter
    def D(self, value: ArrayType[ByteType]) -> None: ...
    
    @property
    def Q(self) -> ECPoint: ...
    
    @Q.setter
    def Q(self, value: ECPoint) -> None: ...
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Validate(self) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ECPoint(ValueType):
    # ---------- Fields ---------- #
    
    @property
    def X(self) -> ArrayType[ByteType]: ...
    
    @X.setter
    def X(self, value: ArrayType[ByteType]) -> None: ...
    
    @property
    def Y(self) -> ArrayType[ByteType]: ...
    
    @Y.setter
    def Y(self, value: ArrayType[ByteType]) -> None: ...
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# No Interfaces

# ---------- Enums ---------- #

class AsymmetricPaddingMode(Enum):
    #None: IntType = 1
    Pkcs1: IntType = 2
    Oaep: IntType = 4
    Pss: IntType = 8


class CngExportPolicies(Enum):
    #None: IntType = 0
    AllowExport: IntType = 1
    AllowPlaintextExport: IntType = 2
    AllowArchiving: IntType = 4
    AllowPlaintextArchiving: IntType = 8


class CngKeyCreationOptions(Enum):
    #None: IntType = 0
    MachineKey: IntType = 32
    OverwriteExistingKey: IntType = 128


class CngKeyHandleOpenOptions(Enum):
    #None: IntType = 0
    EphemeralKey: IntType = 1


class CngKeyOpenOptions(Enum):
    #None: IntType = 0
    UserKey: IntType = 0
    MachineKey: IntType = 32
    Silent: IntType = 64


class CngKeyTypes(Enum):
    #None: IntType = 0
    MachineKey: IntType = 32


class CngKeyUsages(Enum):
    #None: IntType = 0
    Decryption: IntType = 1
    Signing: IntType = 2
    KeyAgreement: IntType = 4
    AllUsages: IntType = 16777215


class CngPropertyOptions(Enum):
    Persist: IntType = -2147483648
    #None: IntType = 0
    CustomProperty: IntType = 1073741824


class CngUIProtectionLevels(Enum):
    #None: IntType = 0
    ProtectKey: IntType = 1
    ForceHighProtection: IntType = 2


class DSAFIPSVERSION_ENUM(Enum):
    DSA_FIPS186_2: IntType = 0
    DSA_FIPS186_3: IntType = 1


class ECDiffieHellmanKeyDerivationFunction(Enum):
    Hash: IntType = 0
    Hmac: IntType = 1
    Tls: IntType = 2


class ECKeyXmlFormat(Enum):
    Rfc4050: IntType = 0


class EncryptionMode(Enum):
    Encrypt: IntType = 0
    Decrypt: IntType = 1


class HASHALGORITHM_ENUM(Enum):
    DSA_HASH_ALGORITHM_SHA1: IntType = 0
    DSA_HASH_ALGORITHM_SHA256: IntType = 1
    DSA_HASH_ALGORITHM_SHA512: IntType = 2


class SignatureVerificationResult(Enum):
    SystemError: IntType = -2146869247
    InvalidSignerCertificate: IntType = -2146869246
    InvalidCountersignature: IntType = -2146869245
    InvalidCertificateSignature: IntType = -2146869244
    InvalidTimestamp: IntType = -2146869243
    BadDigest: IntType = -2146869232
    BasicConstraintsNotObserved: IntType = -2146869223
    UnknownTrustProvider: IntType = -2146762751
    UnknownVerificationAction: IntType = -2146762750
    BadSignatureFormat: IntType = -2146762749
    CertificateNotExplicitlyTrusted: IntType = -2146762748
    MissingSignature: IntType = -2146762496
    CertificateExpired: IntType = -2146762495
    InvalidTimePeriodNesting: IntType = -2146762494
    InvalidCertificateRole: IntType = -2146762493
    PathLengthConstraintViolated: IntType = -2146762492
    UnknownCriticalExtension: IntType = -2146762491
    CertificateUsageNotAllowed: IntType = -2146762490
    IssuerChainingError: IntType = -2146762489
    CertificateMalformed: IntType = -2146762488
    UntrustedRootCertificate: IntType = -2146762487
    CouldNotBuildChain: IntType = -2146762486
    GenericTrustFailure: IntType = -2146762485
    CertificateRevoked: IntType = -2146762484
    UntrustedTestRootCertificate: IntType = -2146762483
    RevocationCheckFailure: IntType = -2146762482
    InvalidCertificateUsage: IntType = -2146762480
    CertificateExplicitlyDistrusted: IntType = -2146762479
    UntrustedCertificationAuthority: IntType = -2146762478
    InvalidCertificatePolicy: IntType = -2146762477
    InvalidCertificateName: IntType = -2146762476
    Valid: IntType = 0
    AssemblyIdentityMismatch: IntType = 1
    ContainingSignatureInvalid: IntType = 2
    PublicKeyTokenMismatch: IntType = 3
    PublisherMismatch: IntType = 4


# No Delegates

__all__ = [
    AesCng,
    AesCryptoServiceProvider,
    AesManaged,
    BCryptAlgorithmHandleCache,
    BCryptHashAlgorithm,
    BCryptNative,
    CapiHashAlgorithm,
    CapiNative,
    CapiSymmetricAlgorithm,
    CngAlgorithm,
    CngAlgorithmGroup,
    CngKey,
    CngKeyBlobFormat,
    CngKeyCreationParameters,
    CngPropertyCollection,
    CngProvider,
    CngUIPolicy,
    DSACng,
    ECCng,
    ECDiffieHellman,
    ECDiffieHellmanCng,
    ECDiffieHellmanCngPublicKey,
    ECDiffieHellmanPublicKey,
    ECDsa,
    ECDsaCng,
    IncrementalHash,
    MD5Cng,
    ManifestSignatureInformation,
    ManifestSignatureInformationCollection,
    NCryptNative,
    RSACng,
    Rfc4050KeyFormatter,
    SHA1Cng,
    SHA256Cng,
    SHA256CryptoServiceProvider,
    SHA384Cng,
    SHA384CryptoServiceProvider,
    SHA512Cng,
    SHA512CryptoServiceProvider,
    SafeLocalAllocHandle,
    StrongNameSignatureInformation,
    TripleDESCng,
    X509Utils,
    BCRYPT_DSA_KEY_BLOB_V2,
    CngProperty,
    ECCurve,
    ECParameters,
    ECPoint,
    AsymmetricPaddingMode,
    CngExportPolicies,
    CngKeyCreationOptions,
    CngKeyHandleOpenOptions,
    CngKeyOpenOptions,
    CngKeyTypes,
    CngKeyUsages,
    CngPropertyOptions,
    CngUIProtectionLevels,
    DSAFIPSVERSION_ENUM,
    ECDiffieHellmanKeyDerivationFunction,
    ECKeyXmlFormat,
    EncryptionMode,
    HASHALGORITHM_ENUM,
    SignatureVerificationResult,
]
