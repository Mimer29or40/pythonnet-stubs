from __future__ import annotations

from abc import ABC
from typing import List, Protocol, Tuple, Union, overload

from Microsoft.Win32.SafeHandles import SafeHandleZeroOrMinusOneIsInvalid
from System import Array, Boolean, Byte, Enum, Exception, IDisposable, IEquatable, Int32, Int64, IntPtr, Object, String, SystemException, Type, ValueType, Void
from System.Collections import ICollection, IEnumerable, IEnumerator
from System.IO import SeekOrigin, Stream
from System.Runtime.InteropServices import _Exception
from System.Runtime.Serialization import ISerializable
from System.Security import SecureString, SecurityElement
from System.Security.AccessControl import CryptoKeySecurity
from System.Threading import CancellationToken
from System.Threading.Tasks import Task

# ---------- Types ---------- #

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
ByteType = Union[int, Byte]
IntType = Union[int, Int32]
LongType = Union[int, Int64]
NIntType = Union[int, IntPtr]
ObjectType = Object
StringType = Union[str, String]
TypeType = Union[type, Type]
VoidType = Union[None, Void]

# ---------- Classes ---------- #

class Aes(ABC, SymmetricAlgorithm, IDisposable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    @overload
    def Create(algorithmName: StringType) -> Aes: ...
    
    @staticmethod
    @overload
    def Create() -> Aes: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AsnEncodedData(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, rawData: ArrayType[ByteType]): ...
    
    @overload
    def __init__(self, oid: StringType, rawData: ArrayType[ByteType]): ...
    
    @overload
    def __init__(self, oid: Oid, rawData: ArrayType[ByteType]): ...
    
    @overload
    def __init__(self, asnEncodedData: AsnEncodedData): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Oid(self) -> Oid: ...
    
    @Oid.setter
    def Oid(self, value: Oid) -> None: ...
    
    @property
    def RawData(self) -> ArrayType[ByteType]: ...
    
    @RawData.setter
    def RawData(self, value: ArrayType[ByteType]) -> None: ...
    
    # ---------- Methods ---------- #
    
    def CopyFrom(self, asnEncodedData: AsnEncodedData) -> VoidType: ...
    
    def Format(self, multiLine: BooleanType) -> StringType: ...
    
    def get_Oid(self) -> Oid: ...
    
    def get_RawData(self) -> ArrayType[ByteType]: ...
    
    def set_Oid(self, value: Oid) -> VoidType: ...
    
    def set_RawData(self, value: ArrayType[ByteType]) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AsnEncodedDataCollection(ObjectType, ICollection, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, asnEncodedData: AsnEncodedData): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def IsSynchronized(self) -> BooleanType: ...
    
    @property
    def Item(self) -> AsnEncodedData: ...
    
    @property
    def SyncRoot(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, asnEncodedData: AsnEncodedData) -> IntType: ...
    
    def CopyTo(self, array: ArrayType[AsnEncodedData], index: IntType) -> VoidType: ...
    
    def GetEnumerator(self) -> AsnEncodedDataEnumerator: ...
    
    def Remove(self, asnEncodedData: AsnEncodedData) -> VoidType: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_IsSynchronized(self) -> BooleanType: ...
    
    def get_Item(self, index: IntType) -> AsnEncodedData: ...
    
    def get_SyncRoot(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AsnEncodedDataEnumerator(ObjectType, IEnumerator):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Current(self) -> AsnEncodedData: ...
    
    # ---------- Methods ---------- #
    
    def MoveNext(self) -> BooleanType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Current(self) -> AsnEncodedData: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AsymmetricAlgorithm(ABC, ObjectType, IDisposable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def KeyExchangeAlgorithm(self) -> StringType: ...
    
    @property
    def KeySize(self) -> IntType: ...
    
    @KeySize.setter
    def KeySize(self, value: IntType) -> None: ...
    
    @property
    def LegalKeySizes(self) -> ArrayType[KeySizes]: ...
    
    @property
    def SignatureAlgorithm(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def Clear(self) -> VoidType: ...
    
    @staticmethod
    @overload
    def Create(algName: StringType) -> AsymmetricAlgorithm: ...
    
    @staticmethod
    @overload
    def Create() -> AsymmetricAlgorithm: ...
    
    def Dispose(self) -> VoidType: ...
    
    def FromXmlString(self, xmlString: StringType) -> VoidType: ...
    
    def ToXmlString(self, includePrivateParameters: BooleanType) -> StringType: ...
    
    def get_KeyExchangeAlgorithm(self) -> StringType: ...
    
    def get_KeySize(self) -> IntType: ...
    
    def get_LegalKeySizes(self) -> ArrayType[KeySizes]: ...
    
    def get_SignatureAlgorithm(self) -> StringType: ...
    
    def set_KeySize(self, value: IntType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AsymmetricKeyExchangeDeformatter(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Parameters(self) -> StringType: ...
    
    @Parameters.setter
    def Parameters(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def DecryptKeyExchange(self, rgb: ArrayType[ByteType]) -> ArrayType[ByteType]: ...
    
    def SetKey(self, key: AsymmetricAlgorithm) -> VoidType: ...
    
    def get_Parameters(self) -> StringType: ...
    
    def set_Parameters(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AsymmetricKeyExchangeFormatter(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Parameters(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def CreateKeyExchange(self, data: ArrayType[ByteType]) -> ArrayType[ByteType]: ...
    
    @overload
    def CreateKeyExchange(self, data: ArrayType[ByteType], symAlgType: TypeType) -> ArrayType[ByteType]: ...
    
    def SetKey(self, key: AsymmetricAlgorithm) -> VoidType: ...
    
    def get_Parameters(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AsymmetricSignatureDeformatter(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def SetHashAlgorithm(self, strName: StringType) -> VoidType: ...
    
    def SetKey(self, key: AsymmetricAlgorithm) -> VoidType: ...
    
    @overload
    def VerifySignature(self, hash: HashAlgorithm, rgbSignature: ArrayType[ByteType]) -> BooleanType: ...
    
    @overload
    def VerifySignature(self, rgbHash: ArrayType[ByteType], rgbSignature: ArrayType[ByteType]) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AsymmetricSignatureFormatter(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def CreateSignature(self, hash: HashAlgorithm) -> ArrayType[ByteType]: ...
    
    @overload
    def CreateSignature(self, rgbHash: ArrayType[ByteType]) -> ArrayType[ByteType]: ...
    
    def SetHashAlgorithm(self, strName: StringType) -> VoidType: ...
    
    def SetKey(self, key: AsymmetricAlgorithm) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class BigInt(ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    @staticmethod
    def op_Equality(value1: BigInt, value2: BigInt) -> BooleanType: ...
    
    @staticmethod
    def op_GreaterThan(value1: BigInt, value2: BigInt) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(value1: BigInt, value2: BigInt) -> BooleanType: ...
    
    @staticmethod
    def op_LessThan(value1: BigInt, value2: BigInt) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CAPI(CAPIMethods):
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


class CAPIBase(ABC, ObjectType):
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


class CAPIMethods(ABC, CAPIUnsafe):
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


class CAPINative(ABC, CAPIBase):
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


class CAPISafe(ABC, CAPINative):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def FreeLibrary(hModule: NIntType) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CAPIUnsafe(ABC, CAPISafe):
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


class Constants(ABC, ObjectType):
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


class CryptoAPITransform(ObjectType, ICryptoTransform, IDisposable):
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
    def KeyHandle(self) -> NIntType: ...
    
    @property
    def OutputBlockSize(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def Clear(self) -> VoidType: ...
    
    def Dispose(self) -> VoidType: ...
    
    def Reset(self) -> VoidType: ...
    
    def TransformBlock(self, inputBuffer: ArrayType[ByteType], inputOffset: IntType, inputCount: IntType, outputBuffer: ArrayType[ByteType], outputOffset: IntType) -> IntType: ...
    
    def TransformFinalBlock(self, inputBuffer: ArrayType[ByteType], inputOffset: IntType, inputCount: IntType) -> ArrayType[ByteType]: ...
    
    def get_CanReuseTransform(self) -> BooleanType: ...
    
    def get_CanTransformMultipleBlocks(self) -> BooleanType: ...
    
    def get_InputBlockSize(self) -> IntType: ...
    
    def get_KeyHandle(self) -> NIntType: ...
    
    def get_OutputBlockSize(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CryptoConfig(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def AllowOnlyFipsAlgorithms() -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def AddAlgorithm(algorithm: TypeType, names: ArrayType[StringType]) -> VoidType: ...
    
    @staticmethod
    def AddOID(oid: StringType, names: ArrayType[StringType]) -> VoidType: ...
    
    @staticmethod
    @overload
    def CreateFromName(name: StringType, args: ArrayType[ObjectType]) -> ObjectType: ...
    
    @staticmethod
    @overload
    def CreateFromName(name: StringType) -> ObjectType: ...
    
    @staticmethod
    def EncodeOID(str: StringType) -> ArrayType[ByteType]: ...
    
    @staticmethod
    def MapNameToOID(name: StringType) -> StringType: ...
    
    @staticmethod
    def get_AllowOnlyFipsAlgorithms() -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CryptoStream(Stream, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, stream: Stream, transform: ICryptoTransform, mode: CryptoStreamMode): ...
    
    @overload
    def __init__(self, stream: Stream, transform: ICryptoTransform, mode: CryptoStreamMode, leaveOpen: BooleanType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CanRead(self) -> BooleanType: ...
    
    @property
    def CanSeek(self) -> BooleanType: ...
    
    @property
    def CanWrite(self) -> BooleanType: ...
    
    @property
    def HasFlushedFinalBlock(self) -> BooleanType: ...
    
    @property
    def Length(self) -> LongType: ...
    
    @property
    def Position(self) -> LongType: ...
    
    @Position.setter
    def Position(self, value: LongType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Clear(self) -> VoidType: ...
    
    def Flush(self) -> VoidType: ...
    
    @overload
    def FlushAsync(self, cancellationToken: CancellationToken) -> Task: ...
    
    def FlushFinalBlock(self) -> VoidType: ...
    
    def Read(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType) -> Tuple[IntType, ArrayType[ByteType]]: ...
    
    @overload
    def ReadAsync(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType, cancellationToken: CancellationToken) -> Task[IntType]: ...
    
    def Seek(self, offset: LongType, origin: SeekOrigin) -> LongType: ...
    
    def SetLength(self, value: LongType) -> VoidType: ...
    
    def Write(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType) -> VoidType: ...
    
    @overload
    def WriteAsync(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType, cancellationToken: CancellationToken) -> Task: ...
    
    def get_CanRead(self) -> BooleanType: ...
    
    def get_CanSeek(self) -> BooleanType: ...
    
    def get_CanWrite(self) -> BooleanType: ...
    
    def get_HasFlushedFinalBlock(self) -> BooleanType: ...
    
    def get_Length(self) -> LongType: ...
    
    def get_Position(self) -> LongType: ...
    
    def set_Position(self, value: LongType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CryptographicException(SystemException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, format: StringType, insert: StringType): ...
    
    @overload
    def __init__(self, message: StringType, inner: Exception): ...
    
    @overload
    def __init__(self, hr: IntType): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CryptographicUnexpectedOperationException(CryptographicException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, format: StringType, insert: StringType): ...
    
    @overload
    def __init__(self, message: StringType, inner: Exception): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CspKeyContainerInfo(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, parameters: CspParameters): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Accessible(self) -> BooleanType: ...
    
    @property
    def CryptoKeySecurity(self) -> CryptoKeySecurity: ...
    
    @property
    def Exportable(self) -> BooleanType: ...
    
    @property
    def HardwareDevice(self) -> BooleanType: ...
    
    @property
    def KeyContainerName(self) -> StringType: ...
    
    @property
    def KeyNumber(self) -> KeyNumber: ...
    
    @property
    def MachineKeyStore(self) -> BooleanType: ...
    
    @property
    def Protected(self) -> BooleanType: ...
    
    @property
    def ProviderName(self) -> StringType: ...
    
    @property
    def ProviderType(self) -> IntType: ...
    
    @property
    def RandomlyGenerated(self) -> BooleanType: ...
    
    @property
    def Removable(self) -> BooleanType: ...
    
    @property
    def UniqueKeyContainerName(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_Accessible(self) -> BooleanType: ...
    
    def get_CryptoKeySecurity(self) -> CryptoKeySecurity: ...
    
    def get_Exportable(self) -> BooleanType: ...
    
    def get_HardwareDevice(self) -> BooleanType: ...
    
    def get_KeyContainerName(self) -> StringType: ...
    
    def get_KeyNumber(self) -> KeyNumber: ...
    
    def get_MachineKeyStore(self) -> BooleanType: ...
    
    def get_Protected(self) -> BooleanType: ...
    
    def get_ProviderName(self) -> StringType: ...
    
    def get_ProviderType(self) -> IntType: ...
    
    def get_RandomlyGenerated(self) -> BooleanType: ...
    
    def get_Removable(self) -> BooleanType: ...
    
    def get_UniqueKeyContainerName(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CspParameters(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def KeyContainerName(self) -> StringType: ...
    
    @KeyContainerName.setter
    def KeyContainerName(self, value: StringType) -> None: ...
    
    @property
    def KeyNumber(self) -> IntType: ...
    
    @KeyNumber.setter
    def KeyNumber(self, value: IntType) -> None: ...
    
    @property
    def ProviderName(self) -> StringType: ...
    
    @ProviderName.setter
    def ProviderName(self, value: StringType) -> None: ...
    
    @property
    def ProviderType(self) -> IntType: ...
    
    @ProviderType.setter
    def ProviderType(self, value: IntType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, dwTypeIn: IntType): ...
    
    @overload
    def __init__(self, dwTypeIn: IntType, strProviderNameIn: StringType): ...
    
    @overload
    def __init__(self, dwTypeIn: IntType, strProviderNameIn: StringType, strContainerNameIn: StringType): ...
    
    @overload
    def __init__(self, providerType: IntType, providerName: StringType, keyContainerName: StringType, cryptoKeySecurity: CryptoKeySecurity, keyPassword: SecureString): ...
    
    @overload
    def __init__(self, providerType: IntType, providerName: StringType, keyContainerName: StringType, cryptoKeySecurity: CryptoKeySecurity, parentWindowHandle: NIntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CryptoKeySecurity(self) -> CryptoKeySecurity: ...
    
    @CryptoKeySecurity.setter
    def CryptoKeySecurity(self, value: CryptoKeySecurity) -> None: ...
    
    @property
    def Flags(self) -> CspProviderFlags: ...
    
    @Flags.setter
    def Flags(self, value: CspProviderFlags) -> None: ...
    
    @property
    def KeyPassword(self) -> SecureString: ...
    
    @KeyPassword.setter
    def KeyPassword(self, value: SecureString) -> None: ...
    
    @property
    def ParentWindowHandle(self) -> NIntType: ...
    
    @ParentWindowHandle.setter
    def ParentWindowHandle(self, value: NIntType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_CryptoKeySecurity(self) -> CryptoKeySecurity: ...
    
    def get_Flags(self) -> CspProviderFlags: ...
    
    def get_KeyPassword(self) -> SecureString: ...
    
    def get_ParentWindowHandle(self) -> NIntType: ...
    
    def set_CryptoKeySecurity(self, value: CryptoKeySecurity) -> VoidType: ...
    
    def set_Flags(self, value: CspProviderFlags) -> VoidType: ...
    
    def set_KeyPassword(self, value: SecureString) -> VoidType: ...
    
    def set_ParentWindowHandle(self, value: NIntType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DES(ABC, SymmetricAlgorithm, IDisposable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Key(self) -> ArrayType[ByteType]: ...
    
    @Key.setter
    def Key(self, value: ArrayType[ByteType]) -> None: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    @overload
    def Create(algName: StringType) -> DES: ...
    
    @staticmethod
    @overload
    def Create() -> DES: ...
    
    @staticmethod
    def IsSemiWeakKey(rgbKey: ArrayType[ByteType]) -> BooleanType: ...
    
    @staticmethod
    def IsWeakKey(rgbKey: ArrayType[ByteType]) -> BooleanType: ...
    
    def get_Key(self) -> ArrayType[ByteType]: ...
    
    def set_Key(self, value: ArrayType[ByteType]) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DESCryptoServiceProvider(DES, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def CreateDecryptor(self, rgbKey: ArrayType[ByteType], rgbIV: ArrayType[ByteType]) -> ICryptoTransform: ...
    
    @overload
    def CreateEncryptor(self, rgbKey: ArrayType[ByteType], rgbIV: ArrayType[ByteType]) -> ICryptoTransform: ...
    
    def GenerateIV(self) -> VoidType: ...
    
    def GenerateKey(self) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DSA(ABC, AsymmetricAlgorithm, IDisposable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    @overload
    def Create(algName: StringType) -> DSA: ...
    
    @staticmethod
    @overload
    def Create() -> DSA: ...
    
    @staticmethod
    @overload
    def Create(keySizeInBits: IntType) -> DSA: ...
    
    @staticmethod
    @overload
    def Create(parameters: DSAParameters) -> DSA: ...
    
    def CreateSignature(self, rgbHash: ArrayType[ByteType]) -> ArrayType[ByteType]: ...
    
    def ExportParameters(self, includePrivateParameters: BooleanType) -> DSAParameters: ...
    
    def FromXmlString(self, xmlString: StringType) -> VoidType: ...
    
    def ImportParameters(self, parameters: DSAParameters) -> VoidType: ...
    
    @overload
    def SignData(self, data: ArrayType[ByteType], hashAlgorithm: HashAlgorithmName) -> ArrayType[ByteType]: ...
    
    @overload
    def SignData(self, data: ArrayType[ByteType], offset: IntType, count: IntType, hashAlgorithm: HashAlgorithmName) -> ArrayType[ByteType]: ...
    
    @overload
    def SignData(self, data: Stream, hashAlgorithm: HashAlgorithmName) -> ArrayType[ByteType]: ...
    
    def ToXmlString(self, includePrivateParameters: BooleanType) -> StringType: ...
    
    @overload
    def VerifyData(self, data: ArrayType[ByteType], signature: ArrayType[ByteType], hashAlgorithm: HashAlgorithmName) -> BooleanType: ...
    
    @overload
    def VerifyData(self, data: ArrayType[ByteType], offset: IntType, count: IntType, signature: ArrayType[ByteType], hashAlgorithm: HashAlgorithmName) -> BooleanType: ...
    
    @overload
    def VerifyData(self, data: Stream, signature: ArrayType[ByteType], hashAlgorithm: HashAlgorithmName) -> BooleanType: ...
    
    def VerifySignature(self, rgbHash: ArrayType[ByteType], rgbSignature: ArrayType[ByteType]) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DSACryptoServiceProvider(DSA, IDisposable, ICspAsymmetricAlgorithm):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, dwKeySize: IntType): ...
    
    @overload
    def __init__(self, parameters: CspParameters): ...
    
    @overload
    def __init__(self, dwKeySize: IntType, parameters: CspParameters): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CspKeyContainerInfo(self) -> CspKeyContainerInfo: ...
    
    @property
    def KeyExchangeAlgorithm(self) -> StringType: ...
    
    @property
    def KeySize(self) -> IntType: ...
    
    @property
    def PersistKeyInCsp(self) -> BooleanType: ...
    
    @PersistKeyInCsp.setter
    def PersistKeyInCsp(self, value: BooleanType) -> None: ...
    
    @property
    def PublicOnly(self) -> BooleanType: ...
    
    @property
    def SignatureAlgorithm(self) -> StringType: ...
    
    @staticmethod
    @property
    def UseMachineKeyStore() -> BooleanType: ...
    
    @staticmethod
    @UseMachineKeyStore.setter
    def UseMachineKeyStore(value: BooleanType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def CreateSignature(self, rgbHash: ArrayType[ByteType]) -> ArrayType[ByteType]: ...
    
    def ExportCspBlob(self, includePrivateParameters: BooleanType) -> ArrayType[ByteType]: ...
    
    def ExportParameters(self, includePrivateParameters: BooleanType) -> DSAParameters: ...
    
    def ImportCspBlob(self, keyBlob: ArrayType[ByteType]) -> VoidType: ...
    
    def ImportParameters(self, parameters: DSAParameters) -> VoidType: ...
    
    @overload
    def SignData(self, inputStream: Stream) -> ArrayType[ByteType]: ...
    
    @overload
    def SignData(self, buffer: ArrayType[ByteType]) -> ArrayType[ByteType]: ...
    
    @overload
    def SignData(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType) -> ArrayType[ByteType]: ...
    
    def SignHash(self, rgbHash: ArrayType[ByteType], str: StringType) -> ArrayType[ByteType]: ...
    
    @overload
    def VerifyData(self, rgbData: ArrayType[ByteType], rgbSignature: ArrayType[ByteType]) -> BooleanType: ...
    
    def VerifyHash(self, rgbHash: ArrayType[ByteType], str: StringType, rgbSignature: ArrayType[ByteType]) -> BooleanType: ...
    
    def VerifySignature(self, rgbHash: ArrayType[ByteType], rgbSignature: ArrayType[ByteType]) -> BooleanType: ...
    
    def get_CspKeyContainerInfo(self) -> CspKeyContainerInfo: ...
    
    def get_KeyExchangeAlgorithm(self) -> StringType: ...
    
    def get_KeySize(self) -> IntType: ...
    
    def get_PersistKeyInCsp(self) -> BooleanType: ...
    
    def get_PublicOnly(self) -> BooleanType: ...
    
    def get_SignatureAlgorithm(self) -> StringType: ...
    
    @staticmethod
    def get_UseMachineKeyStore() -> BooleanType: ...
    
    def set_PersistKeyInCsp(self, value: BooleanType) -> VoidType: ...
    
    @staticmethod
    def set_UseMachineKeyStore(value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DSACspObject(ObjectType):
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


class DSASignatureDeformatter(AsymmetricSignatureDeformatter):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, key: AsymmetricAlgorithm): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def SetHashAlgorithm(self, strName: StringType) -> VoidType: ...
    
    def SetKey(self, key: AsymmetricAlgorithm) -> VoidType: ...
    
    @overload
    def VerifySignature(self, rgbHash: ArrayType[ByteType], rgbSignature: ArrayType[ByteType]) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DSASignatureDescription(SignatureDescription):
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


class DSASignatureFormatter(AsymmetricSignatureFormatter):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, key: AsymmetricAlgorithm): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def CreateSignature(self, rgbHash: ArrayType[ByteType]) -> ArrayType[ByteType]: ...
    
    def SetHashAlgorithm(self, strName: StringType) -> VoidType: ...
    
    def SetKey(self, key: AsymmetricAlgorithm) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DeriveBytes(ABC, ObjectType, IDisposable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Dispose(self) -> VoidType: ...
    
    def GetBytes(self, cb: IntType) -> ArrayType[ByteType]: ...
    
    def Reset(self) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class FromBase64Transform(ObjectType, ICryptoTransform, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, whitespaces: FromBase64TransformMode): ...
    
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
    
    def Clear(self) -> VoidType: ...
    
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


class HMAC(ABC, KeyedHashAlgorithm, IDisposable, ICryptoTransform):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def HashName(self) -> StringType: ...
    
    @HashName.setter
    def HashName(self, value: StringType) -> None: ...
    
    @property
    def Key(self) -> ArrayType[ByteType]: ...
    
    @Key.setter
    def Key(self, value: ArrayType[ByteType]) -> None: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    @overload
    def Create(algorithmName: StringType) -> HMAC: ...
    
    @staticmethod
    @overload
    def Create() -> HMAC: ...
    
    def Initialize(self) -> VoidType: ...
    
    def get_HashName(self) -> StringType: ...
    
    def get_Key(self) -> ArrayType[ByteType]: ...
    
    def set_HashName(self, value: StringType) -> VoidType: ...
    
    def set_Key(self, value: ArrayType[ByteType]) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class HMACMD5(HMAC, IDisposable, ICryptoTransform):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, key: ArrayType[ByteType]): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class HMACRIPEMD160(HMAC, IDisposable, ICryptoTransform):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, key: ArrayType[ByteType]): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class HMACSHA1(HMAC, IDisposable, ICryptoTransform):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, key: ArrayType[ByteType]): ...
    
    @overload
    def __init__(self, key: ArrayType[ByteType], useManagedSha1: BooleanType): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class HMACSHA256(HMAC, IDisposable, ICryptoTransform):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, key: ArrayType[ByteType]): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class HMACSHA384(HMAC, IDisposable, ICryptoTransform):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, key: ArrayType[ByteType]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ProduceLegacyHmacValues(self) -> BooleanType: ...
    
    @ProduceLegacyHmacValues.setter
    def ProduceLegacyHmacValues(self, value: BooleanType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_ProduceLegacyHmacValues(self) -> BooleanType: ...
    
    def set_ProduceLegacyHmacValues(self, value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class HMACSHA512(HMAC, IDisposable, ICryptoTransform):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, key: ArrayType[ByteType]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ProduceLegacyHmacValues(self) -> BooleanType: ...
    
    @ProduceLegacyHmacValues.setter
    def ProduceLegacyHmacValues(self, value: BooleanType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_ProduceLegacyHmacValues(self) -> BooleanType: ...
    
    def set_ProduceLegacyHmacValues(self, value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class HashAlgorithm(ABC, ObjectType, IDisposable, ICryptoTransform):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def CanReuseTransform(self) -> BooleanType: ...
    
    @property
    def CanTransformMultipleBlocks(self) -> BooleanType: ...
    
    @property
    def Hash(self) -> ArrayType[ByteType]: ...
    
    @property
    def HashSize(self) -> IntType: ...
    
    @property
    def InputBlockSize(self) -> IntType: ...
    
    @property
    def OutputBlockSize(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def Clear(self) -> VoidType: ...
    
    @overload
    def ComputeHash(self, inputStream: Stream) -> ArrayType[ByteType]: ...
    
    @overload
    def ComputeHash(self, buffer: ArrayType[ByteType]) -> ArrayType[ByteType]: ...
    
    @overload
    def ComputeHash(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType) -> ArrayType[ByteType]: ...
    
    @staticmethod
    @overload
    def Create(hashName: StringType) -> HashAlgorithm: ...
    
    @staticmethod
    @overload
    def Create() -> HashAlgorithm: ...
    
    def Dispose(self) -> VoidType: ...
    
    def Initialize(self) -> VoidType: ...
    
    def TransformBlock(self, inputBuffer: ArrayType[ByteType], inputOffset: IntType, inputCount: IntType, outputBuffer: ArrayType[ByteType], outputOffset: IntType) -> IntType: ...
    
    def TransformFinalBlock(self, inputBuffer: ArrayType[ByteType], inputOffset: IntType, inputCount: IntType) -> ArrayType[ByteType]: ...
    
    def get_CanReuseTransform(self) -> BooleanType: ...
    
    def get_CanTransformMultipleBlocks(self) -> BooleanType: ...
    
    def get_Hash(self) -> ArrayType[ByteType]: ...
    
    def get_HashSize(self) -> IntType: ...
    
    def get_InputBlockSize(self) -> IntType: ...
    
    def get_OutputBlockSize(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class KeySizes(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, minSize: IntType, maxSize: IntType, skipSize: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def MaxSize(self) -> IntType: ...
    
    @property
    def MinSize(self) -> IntType: ...
    
    @property
    def SkipSize(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def get_MaxSize(self) -> IntType: ...
    
    def get_MinSize(self) -> IntType: ...
    
    def get_SkipSize(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class KeyedHashAlgorithm(ABC, HashAlgorithm, IDisposable, ICryptoTransform):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Key(self) -> ArrayType[ByteType]: ...
    
    @Key.setter
    def Key(self, value: ArrayType[ByteType]) -> None: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    @overload
    def Create(algName: StringType) -> KeyedHashAlgorithm: ...
    
    @staticmethod
    @overload
    def Create() -> KeyedHashAlgorithm: ...
    
    def get_Key(self) -> ArrayType[ByteType]: ...
    
    def set_Key(self, value: ArrayType[ByteType]) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MACTripleDES(KeyedHashAlgorithm, IDisposable, ICryptoTransform):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, rgbKey: ArrayType[ByteType]): ...
    
    @overload
    def __init__(self, strTripleDES: StringType, rgbKey: ArrayType[ByteType]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Padding(self) -> PaddingMode: ...
    
    @Padding.setter
    def Padding(self, value: PaddingMode) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Initialize(self) -> VoidType: ...
    
    def get_Padding(self) -> PaddingMode: ...
    
    def set_Padding(self, value: PaddingMode) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MD5(ABC, HashAlgorithm, IDisposable, ICryptoTransform):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    @overload
    def Create(algName: StringType) -> MD5: ...
    
    @staticmethod
    @overload
    def Create() -> MD5: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MD5CryptoServiceProvider(MD5, IDisposable, ICryptoTransform):
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


class MaskGenerationMethod(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GenerateMask(self, rgbSeed: ArrayType[ByteType], cbReturn: IntType) -> ArrayType[ByteType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Oid(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, oid: StringType): ...
    
    @overload
    def __init__(self, value: StringType, friendlyName: StringType): ...
    
    @overload
    def __init__(self, oid: Oid): ...
    
    # ---------- Properties ---------- #
    
    @property
    def FriendlyName(self) -> StringType: ...
    
    @FriendlyName.setter
    def FriendlyName(self, value: StringType) -> None: ...
    
    @property
    def Value(self) -> StringType: ...
    
    @Value.setter
    def Value(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def FromFriendlyName(friendlyName: StringType, group: OidGroup) -> Oid: ...
    
    @staticmethod
    def FromOidValue(oidValue: StringType, group: OidGroup) -> Oid: ...
    
    def get_FriendlyName(self) -> StringType: ...
    
    def get_Value(self) -> StringType: ...
    
    def set_FriendlyName(self, value: StringType) -> VoidType: ...
    
    def set_Value(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class OidCollection(ObjectType, ICollection, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def IsSynchronized(self) -> BooleanType: ...
    
    @property
    def Item(self) -> Oid: ...
    
    @property
    def Item(self) -> Oid: ...
    
    @property
    def SyncRoot(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, oid: Oid) -> IntType: ...
    
    def CopyTo(self, array: ArrayType[Oid], index: IntType) -> VoidType: ...
    
    def GetEnumerator(self) -> OidEnumerator: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_IsSynchronized(self) -> BooleanType: ...
    
    @overload
    def get_Item(self, index: IntType) -> Oid: ...
    
    @overload
    def get_Item(self, oid: StringType) -> Oid: ...
    
    def get_SyncRoot(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class OidEnumerator(ObjectType, IEnumerator):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Current(self) -> Oid: ...
    
    # ---------- Methods ---------- #
    
    def MoveNext(self) -> BooleanType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Current(self) -> Oid: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PKCS1MaskGenerationMethod(MaskGenerationMethod):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def HashName(self) -> StringType: ...
    
    @HashName.setter
    def HashName(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def GenerateMask(self, rgbSeed: ArrayType[ByteType], cbReturn: IntType) -> ArrayType[ByteType]: ...
    
    def get_HashName(self) -> StringType: ...
    
    def set_HashName(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PasswordDeriveBytes(DeriveBytes, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, strPassword: StringType, rgbSalt: ArrayType[ByteType]): ...
    
    @overload
    def __init__(self, password: ArrayType[ByteType], salt: ArrayType[ByteType]): ...
    
    @overload
    def __init__(self, strPassword: StringType, rgbSalt: ArrayType[ByteType], strHashName: StringType, iterations: IntType): ...
    
    @overload
    def __init__(self, password: ArrayType[ByteType], salt: ArrayType[ByteType], hashName: StringType, iterations: IntType): ...
    
    @overload
    def __init__(self, strPassword: StringType, rgbSalt: ArrayType[ByteType], cspParams: CspParameters): ...
    
    @overload
    def __init__(self, password: ArrayType[ByteType], salt: ArrayType[ByteType], cspParams: CspParameters): ...
    
    @overload
    def __init__(self, strPassword: StringType, rgbSalt: ArrayType[ByteType], strHashName: StringType, iterations: IntType, cspParams: CspParameters): ...
    
    @overload
    def __init__(self, password: ArrayType[ByteType], salt: ArrayType[ByteType], hashName: StringType, iterations: IntType, cspParams: CspParameters): ...
    
    # ---------- Properties ---------- #
    
    @property
    def HashName(self) -> StringType: ...
    
    @HashName.setter
    def HashName(self, value: StringType) -> None: ...
    
    @property
    def IterationCount(self) -> IntType: ...
    
    @IterationCount.setter
    def IterationCount(self, value: IntType) -> None: ...
    
    @property
    def Salt(self) -> ArrayType[ByteType]: ...
    
    @Salt.setter
    def Salt(self, value: ArrayType[ByteType]) -> None: ...
    
    # ---------- Methods ---------- #
    
    def CryptDeriveKey(self, algname: StringType, alghashname: StringType, keySize: IntType, rgbIV: ArrayType[ByteType]) -> ArrayType[ByteType]: ...
    
    def GetBytes(self, cb: IntType) -> ArrayType[ByteType]: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_HashName(self) -> StringType: ...
    
    def get_IterationCount(self) -> IntType: ...
    
    def get_Salt(self) -> ArrayType[ByteType]: ...
    
    def set_HashName(self, value: StringType) -> VoidType: ...
    
    def set_IterationCount(self, value: IntType) -> VoidType: ...
    
    def set_Salt(self, value: ArrayType[ByteType]) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RC2(ABC, SymmetricAlgorithm, IDisposable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def EffectiveKeySize(self) -> IntType: ...
    
    @EffectiveKeySize.setter
    def EffectiveKeySize(self, value: IntType) -> None: ...
    
    @property
    def KeySize(self) -> IntType: ...
    
    @KeySize.setter
    def KeySize(self, value: IntType) -> None: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    @overload
    def Create(AlgName: StringType) -> RC2: ...
    
    @staticmethod
    @overload
    def Create() -> RC2: ...
    
    def get_EffectiveKeySize(self) -> IntType: ...
    
    def get_KeySize(self) -> IntType: ...
    
    def set_EffectiveKeySize(self, value: IntType) -> VoidType: ...
    
    def set_KeySize(self, value: IntType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RC2CryptoServiceProvider(RC2, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def EffectiveKeySize(self) -> IntType: ...
    
    @EffectiveKeySize.setter
    def EffectiveKeySize(self, value: IntType) -> None: ...
    
    @property
    def UseSalt(self) -> BooleanType: ...
    
    @UseSalt.setter
    def UseSalt(self, value: BooleanType) -> None: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def CreateDecryptor(self, rgbKey: ArrayType[ByteType], rgbIV: ArrayType[ByteType]) -> ICryptoTransform: ...
    
    @overload
    def CreateEncryptor(self, rgbKey: ArrayType[ByteType], rgbIV: ArrayType[ByteType]) -> ICryptoTransform: ...
    
    def GenerateIV(self) -> VoidType: ...
    
    def GenerateKey(self) -> VoidType: ...
    
    def get_EffectiveKeySize(self) -> IntType: ...
    
    def get_UseSalt(self) -> BooleanType: ...
    
    def set_EffectiveKeySize(self, value: IntType) -> VoidType: ...
    
    def set_UseSalt(self, value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RIPEMD160(ABC, HashAlgorithm, IDisposable, ICryptoTransform):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    @overload
    def Create(hashName: StringType) -> RIPEMD160: ...
    
    @staticmethod
    @overload
    def Create() -> RIPEMD160: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RIPEMD160Managed(RIPEMD160, IDisposable, ICryptoTransform):
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


class RNGCryptoServiceProvider(RandomNumberGenerator, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, str: StringType): ...
    
    @overload
    def __init__(self, rgb: ArrayType[ByteType]): ...
    
    @overload
    def __init__(self, cspParams: CspParameters): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def GetBytes(self, data: ArrayType[ByteType]) -> VoidType: ...
    
    def GetNonZeroBytes(self, data: ArrayType[ByteType]) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RSA(ABC, AsymmetricAlgorithm, IDisposable):
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
    def Create(algName: StringType) -> RSA: ...
    
    @staticmethod
    @overload
    def Create() -> RSA: ...
    
    @staticmethod
    @overload
    def Create(keySizeInBits: IntType) -> RSA: ...
    
    @staticmethod
    @overload
    def Create(parameters: RSAParameters) -> RSA: ...
    
    def Decrypt(self, data: ArrayType[ByteType], padding: RSAEncryptionPadding) -> ArrayType[ByteType]: ...
    
    def DecryptValue(self, rgb: ArrayType[ByteType]) -> ArrayType[ByteType]: ...
    
    def Encrypt(self, data: ArrayType[ByteType], padding: RSAEncryptionPadding) -> ArrayType[ByteType]: ...
    
    def EncryptValue(self, rgb: ArrayType[ByteType]) -> ArrayType[ByteType]: ...
    
    def ExportParameters(self, includePrivateParameters: BooleanType) -> RSAParameters: ...
    
    def FromXmlString(self, xmlString: StringType) -> VoidType: ...
    
    def ImportParameters(self, parameters: RSAParameters) -> VoidType: ...
    
    @overload
    def SignData(self, data: ArrayType[ByteType], hashAlgorithm: HashAlgorithmName, padding: RSASignaturePadding) -> ArrayType[ByteType]: ...
    
    @overload
    def SignData(self, data: ArrayType[ByteType], offset: IntType, count: IntType, hashAlgorithm: HashAlgorithmName, padding: RSASignaturePadding) -> ArrayType[ByteType]: ...
    
    @overload
    def SignData(self, data: Stream, hashAlgorithm: HashAlgorithmName, padding: RSASignaturePadding) -> ArrayType[ByteType]: ...
    
    def SignHash(self, hash: ArrayType[ByteType], hashAlgorithm: HashAlgorithmName, padding: RSASignaturePadding) -> ArrayType[ByteType]: ...
    
    def ToXmlString(self, includePrivateParameters: BooleanType) -> StringType: ...
    
    @overload
    def VerifyData(self, data: ArrayType[ByteType], signature: ArrayType[ByteType], hashAlgorithm: HashAlgorithmName, padding: RSASignaturePadding) -> BooleanType: ...
    
    @overload
    def VerifyData(self, data: ArrayType[ByteType], offset: IntType, count: IntType, signature: ArrayType[ByteType], hashAlgorithm: HashAlgorithmName, padding: RSASignaturePadding) -> BooleanType: ...
    
    @overload
    def VerifyData(self, data: Stream, signature: ArrayType[ByteType], hashAlgorithm: HashAlgorithmName, padding: RSASignaturePadding) -> BooleanType: ...
    
    def VerifyHash(self, hash: ArrayType[ByteType], signature: ArrayType[ByteType], hashAlgorithm: HashAlgorithmName, padding: RSASignaturePadding) -> BooleanType: ...
    
    def get_KeyExchangeAlgorithm(self) -> StringType: ...
    
    def get_SignatureAlgorithm(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RSACryptoServiceProvider(RSA, IDisposable, ICspAsymmetricAlgorithm):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, dwKeySize: IntType): ...
    
    @overload
    def __init__(self, parameters: CspParameters): ...
    
    @overload
    def __init__(self, dwKeySize: IntType, parameters: CspParameters): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CspKeyContainerInfo(self) -> CspKeyContainerInfo: ...
    
    @property
    def KeyExchangeAlgorithm(self) -> StringType: ...
    
    @property
    def KeySize(self) -> IntType: ...
    
    @property
    def PersistKeyInCsp(self) -> BooleanType: ...
    
    @PersistKeyInCsp.setter
    def PersistKeyInCsp(self, value: BooleanType) -> None: ...
    
    @property
    def PublicOnly(self) -> BooleanType: ...
    
    @property
    def SignatureAlgorithm(self) -> StringType: ...
    
    @staticmethod
    @property
    def UseMachineKeyStore() -> BooleanType: ...
    
    @staticmethod
    @UseMachineKeyStore.setter
    def UseMachineKeyStore(value: BooleanType) -> None: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Decrypt(self, rgb: ArrayType[ByteType], fOAEP: BooleanType) -> ArrayType[ByteType]: ...
    
    @overload
    def Decrypt(self, data: ArrayType[ByteType], padding: RSAEncryptionPadding) -> ArrayType[ByteType]: ...
    
    def DecryptValue(self, rgb: ArrayType[ByteType]) -> ArrayType[ByteType]: ...
    
    @overload
    def Encrypt(self, rgb: ArrayType[ByteType], fOAEP: BooleanType) -> ArrayType[ByteType]: ...
    
    @overload
    def Encrypt(self, data: ArrayType[ByteType], padding: RSAEncryptionPadding) -> ArrayType[ByteType]: ...
    
    def EncryptValue(self, rgb: ArrayType[ByteType]) -> ArrayType[ByteType]: ...
    
    def ExportCspBlob(self, includePrivateParameters: BooleanType) -> ArrayType[ByteType]: ...
    
    def ExportParameters(self, includePrivateParameters: BooleanType) -> RSAParameters: ...
    
    def ImportCspBlob(self, keyBlob: ArrayType[ByteType]) -> VoidType: ...
    
    def ImportParameters(self, parameters: RSAParameters) -> VoidType: ...
    
    @overload
    def SignData(self, inputStream: Stream, halg: ObjectType) -> ArrayType[ByteType]: ...
    
    @overload
    def SignData(self, buffer: ArrayType[ByteType], halg: ObjectType) -> ArrayType[ByteType]: ...
    
    @overload
    def SignData(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType, halg: ObjectType) -> ArrayType[ByteType]: ...
    
    @overload
    def SignHash(self, rgbHash: ArrayType[ByteType], str: StringType) -> ArrayType[ByteType]: ...
    
    @overload
    def SignHash(self, hash: ArrayType[ByteType], hashAlgorithm: HashAlgorithmName, padding: RSASignaturePadding) -> ArrayType[ByteType]: ...
    
    @overload
    def VerifyData(self, buffer: ArrayType[ByteType], halg: ObjectType, signature: ArrayType[ByteType]) -> BooleanType: ...
    
    @overload
    def VerifyHash(self, rgbHash: ArrayType[ByteType], str: StringType, rgbSignature: ArrayType[ByteType]) -> BooleanType: ...
    
    @overload
    def VerifyHash(self, hash: ArrayType[ByteType], signature: ArrayType[ByteType], hashAlgorithm: HashAlgorithmName, padding: RSASignaturePadding) -> BooleanType: ...
    
    def get_CspKeyContainerInfo(self) -> CspKeyContainerInfo: ...
    
    def get_KeyExchangeAlgorithm(self) -> StringType: ...
    
    def get_KeySize(self) -> IntType: ...
    
    def get_PersistKeyInCsp(self) -> BooleanType: ...
    
    def get_PublicOnly(self) -> BooleanType: ...
    
    def get_SignatureAlgorithm(self) -> StringType: ...
    
    @staticmethod
    def get_UseMachineKeyStore() -> BooleanType: ...
    
    def set_PersistKeyInCsp(self, value: BooleanType) -> VoidType: ...
    
    @staticmethod
    def set_UseMachineKeyStore(value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RSACspObject(ObjectType):
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


class RSAEncryptionPadding(ObjectType, IEquatable[RSAEncryptionPadding]):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Mode(self) -> RSAEncryptionPaddingMode: ...
    
    @property
    def OaepHashAlgorithm(self) -> HashAlgorithmName: ...
    
    @staticmethod
    @property
    def OaepSHA1() -> RSAEncryptionPadding: ...
    
    @staticmethod
    @property
    def OaepSHA256() -> RSAEncryptionPadding: ...
    
    @staticmethod
    @property
    def OaepSHA384() -> RSAEncryptionPadding: ...
    
    @staticmethod
    @property
    def OaepSHA512() -> RSAEncryptionPadding: ...
    
    @staticmethod
    @property
    def Pkcs1() -> RSAEncryptionPadding: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def CreateOaep(hashAlgorithm: HashAlgorithmName) -> RSAEncryptionPadding: ...
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, other: RSAEncryptionPadding) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Mode(self) -> RSAEncryptionPaddingMode: ...
    
    def get_OaepHashAlgorithm(self) -> HashAlgorithmName: ...
    
    @staticmethod
    def get_OaepSHA1() -> RSAEncryptionPadding: ...
    
    @staticmethod
    def get_OaepSHA256() -> RSAEncryptionPadding: ...
    
    @staticmethod
    def get_OaepSHA384() -> RSAEncryptionPadding: ...
    
    @staticmethod
    def get_OaepSHA512() -> RSAEncryptionPadding: ...
    
    @staticmethod
    def get_Pkcs1() -> RSAEncryptionPadding: ...
    
    @staticmethod
    def op_Equality(left: RSAEncryptionPadding, right: RSAEncryptionPadding) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(left: RSAEncryptionPadding, right: RSAEncryptionPadding) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RSAOAEPKeyExchangeDeformatter(AsymmetricKeyExchangeDeformatter):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, key: AsymmetricAlgorithm): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Parameters(self) -> StringType: ...
    
    @Parameters.setter
    def Parameters(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def DecryptKeyExchange(self, rgbData: ArrayType[ByteType]) -> ArrayType[ByteType]: ...
    
    def SetKey(self, key: AsymmetricAlgorithm) -> VoidType: ...
    
    def get_Parameters(self) -> StringType: ...
    
    def set_Parameters(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RSAOAEPKeyExchangeFormatter(AsymmetricKeyExchangeFormatter):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, key: AsymmetricAlgorithm): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Parameter(self) -> ArrayType[ByteType]: ...
    
    @Parameter.setter
    def Parameter(self, value: ArrayType[ByteType]) -> None: ...
    
    @property
    def Parameters(self) -> StringType: ...
    
    @property
    def Rng(self) -> RandomNumberGenerator: ...
    
    @Rng.setter
    def Rng(self, value: RandomNumberGenerator) -> None: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def CreateKeyExchange(self, rgbData: ArrayType[ByteType], symAlgType: TypeType) -> ArrayType[ByteType]: ...
    
    @overload
    def CreateKeyExchange(self, rgbData: ArrayType[ByteType]) -> ArrayType[ByteType]: ...
    
    def SetKey(self, key: AsymmetricAlgorithm) -> VoidType: ...
    
    def get_Parameter(self) -> ArrayType[ByteType]: ...
    
    def get_Parameters(self) -> StringType: ...
    
    def get_Rng(self) -> RandomNumberGenerator: ...
    
    def set_Parameter(self, value: ArrayType[ByteType]) -> VoidType: ...
    
    def set_Rng(self, value: RandomNumberGenerator) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RSAPKCS1KeyExchangeDeformatter(AsymmetricKeyExchangeDeformatter):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, key: AsymmetricAlgorithm): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Parameters(self) -> StringType: ...
    
    @Parameters.setter
    def Parameters(self, value: StringType) -> None: ...
    
    @property
    def RNG(self) -> RandomNumberGenerator: ...
    
    @RNG.setter
    def RNG(self, value: RandomNumberGenerator) -> None: ...
    
    # ---------- Methods ---------- #
    
    def DecryptKeyExchange(self, rgbIn: ArrayType[ByteType]) -> ArrayType[ByteType]: ...
    
    def SetKey(self, key: AsymmetricAlgorithm) -> VoidType: ...
    
    def get_Parameters(self) -> StringType: ...
    
    def get_RNG(self) -> RandomNumberGenerator: ...
    
    def set_Parameters(self, value: StringType) -> VoidType: ...
    
    def set_RNG(self, value: RandomNumberGenerator) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RSAPKCS1KeyExchangeFormatter(AsymmetricKeyExchangeFormatter):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, key: AsymmetricAlgorithm): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Parameters(self) -> StringType: ...
    
    @property
    def Rng(self) -> RandomNumberGenerator: ...
    
    @Rng.setter
    def Rng(self, value: RandomNumberGenerator) -> None: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def CreateKeyExchange(self, rgbData: ArrayType[ByteType], symAlgType: TypeType) -> ArrayType[ByteType]: ...
    
    @overload
    def CreateKeyExchange(self, rgbData: ArrayType[ByteType]) -> ArrayType[ByteType]: ...
    
    def SetKey(self, key: AsymmetricAlgorithm) -> VoidType: ...
    
    def get_Parameters(self) -> StringType: ...
    
    def get_Rng(self) -> RandomNumberGenerator: ...
    
    def set_Rng(self, value: RandomNumberGenerator) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RSAPKCS1SHA1SignatureDescription(RSAPKCS1SignatureDescription):
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


class RSAPKCS1SHA256SignatureDescription(RSAPKCS1SignatureDescription):
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


class RSAPKCS1SHA384SignatureDescription(RSAPKCS1SignatureDescription):
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


class RSAPKCS1SHA512SignatureDescription(RSAPKCS1SignatureDescription):
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


class RSAPKCS1SignatureDeformatter(AsymmetricSignatureDeformatter):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, key: AsymmetricAlgorithm): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def SetHashAlgorithm(self, strName: StringType) -> VoidType: ...
    
    def SetKey(self, key: AsymmetricAlgorithm) -> VoidType: ...
    
    @overload
    def VerifySignature(self, rgbHash: ArrayType[ByteType], rgbSignature: ArrayType[ByteType]) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RSAPKCS1SignatureDescription(ABC, SignatureDescription):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def CreateDeformatter(self, key: AsymmetricAlgorithm) -> AsymmetricSignatureDeformatter: ...
    
    def CreateFormatter(self, key: AsymmetricAlgorithm) -> AsymmetricSignatureFormatter: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RSAPKCS1SignatureFormatter(AsymmetricSignatureFormatter):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, key: AsymmetricAlgorithm): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def CreateSignature(self, rgbHash: ArrayType[ByteType]) -> ArrayType[ByteType]: ...
    
    def SetHashAlgorithm(self, strName: StringType) -> VoidType: ...
    
    def SetKey(self, key: AsymmetricAlgorithm) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RSASignaturePadding(ObjectType, IEquatable[RSASignaturePadding]):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Mode(self) -> RSASignaturePaddingMode: ...
    
    @staticmethod
    @property
    def Pkcs1() -> RSASignaturePadding: ...
    
    @staticmethod
    @property
    def Pss() -> RSASignaturePadding: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, other: RSASignaturePadding) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Mode(self) -> RSASignaturePaddingMode: ...
    
    @staticmethod
    def get_Pkcs1() -> RSASignaturePadding: ...
    
    @staticmethod
    def get_Pss() -> RSASignaturePadding: ...
    
    @staticmethod
    def op_Equality(left: RSASignaturePadding, right: RSASignaturePadding) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(left: RSASignaturePadding, right: RSASignaturePadding) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RandomNumberGenerator(ABC, ObjectType, IDisposable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    @overload
    def Create() -> RandomNumberGenerator: ...
    
    @staticmethod
    @overload
    def Create(rngName: StringType) -> RandomNumberGenerator: ...
    
    def Dispose(self) -> VoidType: ...
    
    @overload
    def GetBytes(self, data: ArrayType[ByteType], offset: IntType, count: IntType) -> VoidType: ...
    
    @overload
    def GetBytes(self, data: ArrayType[ByteType]) -> VoidType: ...
    
    def GetNonZeroBytes(self, data: ArrayType[ByteType]) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Rfc2898DeriveBytes(DeriveBytes, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, password: StringType, saltSize: IntType): ...
    
    @overload
    def __init__(self, password: StringType, saltSize: IntType, iterations: IntType): ...
    
    @overload
    def __init__(self, password: StringType, saltSize: IntType, iterations: IntType, hashAlgorithm: HashAlgorithmName): ...
    
    @overload
    def __init__(self, password: StringType, salt: ArrayType[ByteType]): ...
    
    @overload
    def __init__(self, password: StringType, salt: ArrayType[ByteType], iterations: IntType): ...
    
    @overload
    def __init__(self, password: StringType, salt: ArrayType[ByteType], iterations: IntType, hashAlgorithm: HashAlgorithmName): ...
    
    @overload
    def __init__(self, password: ArrayType[ByteType], salt: ArrayType[ByteType], iterations: IntType): ...
    
    @overload
    def __init__(self, password: ArrayType[ByteType], salt: ArrayType[ByteType], iterations: IntType, hashAlgorithm: HashAlgorithmName): ...
    
    # ---------- Properties ---------- #
    
    @property
    def IterationCount(self) -> IntType: ...
    
    @IterationCount.setter
    def IterationCount(self, value: IntType) -> None: ...
    
    @property
    def Salt(self) -> ArrayType[ByteType]: ...
    
    @Salt.setter
    def Salt(self, value: ArrayType[ByteType]) -> None: ...
    
    # ---------- Methods ---------- #
    
    def CryptDeriveKey(self, algname: StringType, alghashname: StringType, keySize: IntType, rgbIV: ArrayType[ByteType]) -> ArrayType[ByteType]: ...
    
    def GetBytes(self, cb: IntType) -> ArrayType[ByteType]: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_IterationCount(self) -> IntType: ...
    
    def get_Salt(self) -> ArrayType[ByteType]: ...
    
    def set_IterationCount(self, value: IntType) -> VoidType: ...
    
    def set_Salt(self, value: ArrayType[ByteType]) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Rijndael(ABC, SymmetricAlgorithm, IDisposable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    @overload
    def Create(algName: StringType) -> Rijndael: ...
    
    @staticmethod
    @overload
    def Create() -> Rijndael: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RijndaelManaged(Rijndael, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def CreateDecryptor(self, rgbKey: ArrayType[ByteType], rgbIV: ArrayType[ByteType]) -> ICryptoTransform: ...
    
    @overload
    def CreateEncryptor(self, rgbKey: ArrayType[ByteType], rgbIV: ArrayType[ByteType]) -> ICryptoTransform: ...
    
    def GenerateIV(self) -> VoidType: ...
    
    def GenerateKey(self) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RijndaelManagedTransform(ObjectType, ICryptoTransform, IDisposable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def BlockSizeValue(self) -> IntType: ...
    
    @property
    def CanReuseTransform(self) -> BooleanType: ...
    
    @property
    def CanTransformMultipleBlocks(self) -> BooleanType: ...
    
    @property
    def InputBlockSize(self) -> IntType: ...
    
    @property
    def OutputBlockSize(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def Clear(self) -> VoidType: ...
    
    def Dispose(self) -> VoidType: ...
    
    def Reset(self) -> VoidType: ...
    
    def TransformBlock(self, inputBuffer: ArrayType[ByteType], inputOffset: IntType, inputCount: IntType, outputBuffer: ArrayType[ByteType], outputOffset: IntType) -> IntType: ...
    
    def TransformFinalBlock(self, inputBuffer: ArrayType[ByteType], inputOffset: IntType, inputCount: IntType) -> ArrayType[ByteType]: ...
    
    def get_BlockSizeValue(self) -> IntType: ...
    
    def get_CanReuseTransform(self) -> BooleanType: ...
    
    def get_CanTransformMultipleBlocks(self) -> BooleanType: ...
    
    def get_InputBlockSize(self) -> IntType: ...
    
    def get_OutputBlockSize(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SHA1(ABC, HashAlgorithm, IDisposable, ICryptoTransform):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    @overload
    def Create(hashName: StringType) -> SHA1: ...
    
    @staticmethod
    @overload
    def Create() -> SHA1: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SHA1CryptoServiceProvider(SHA1, IDisposable, ICryptoTransform):
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


class SHA1Managed(SHA1, IDisposable, ICryptoTransform):
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


class SHA256(ABC, HashAlgorithm, IDisposable, ICryptoTransform):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    @overload
    def Create(hashName: StringType) -> SHA256: ...
    
    @staticmethod
    @overload
    def Create() -> SHA256: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SHA256Managed(SHA256, IDisposable, ICryptoTransform):
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


class SHA384(ABC, HashAlgorithm, IDisposable, ICryptoTransform):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    @overload
    def Create(hashName: StringType) -> SHA384: ...
    
    @staticmethod
    @overload
    def Create() -> SHA384: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SHA384Managed(SHA384, IDisposable, ICryptoTransform):
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


class SHA512(ABC, HashAlgorithm, IDisposable, ICryptoTransform):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    @overload
    def Create(hashName: StringType) -> SHA512: ...
    
    @staticmethod
    @overload
    def Create() -> SHA512: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SHA512Managed(SHA512, IDisposable, ICryptoTransform):
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


class SafeCertContextHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
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


class SafeCertStoreHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
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


class SafeCryptMsgHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
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


class SafeCryptProvHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
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


class SafeCspHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
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


class SafeCspHashHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
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


class SafeCspKeyHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
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


class SafeHashHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
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


class SafeKeyHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
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


class SafeLibraryHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
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


class SafeProvHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
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


class SignatureDescription(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, el: SecurityElement): ...
    
    # ---------- Properties ---------- #
    
    @property
    def DeformatterAlgorithm(self) -> StringType: ...
    
    @DeformatterAlgorithm.setter
    def DeformatterAlgorithm(self, value: StringType) -> None: ...
    
    @property
    def DigestAlgorithm(self) -> StringType: ...
    
    @DigestAlgorithm.setter
    def DigestAlgorithm(self, value: StringType) -> None: ...
    
    @property
    def FormatterAlgorithm(self) -> StringType: ...
    
    @FormatterAlgorithm.setter
    def FormatterAlgorithm(self, value: StringType) -> None: ...
    
    @property
    def KeyAlgorithm(self) -> StringType: ...
    
    @KeyAlgorithm.setter
    def KeyAlgorithm(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def CreateDeformatter(self, key: AsymmetricAlgorithm) -> AsymmetricSignatureDeformatter: ...
    
    def CreateDigest(self) -> HashAlgorithm: ...
    
    def CreateFormatter(self, key: AsymmetricAlgorithm) -> AsymmetricSignatureFormatter: ...
    
    def get_DeformatterAlgorithm(self) -> StringType: ...
    
    def get_DigestAlgorithm(self) -> StringType: ...
    
    def get_FormatterAlgorithm(self) -> StringType: ...
    
    def get_KeyAlgorithm(self) -> StringType: ...
    
    def set_DeformatterAlgorithm(self, value: StringType) -> VoidType: ...
    
    def set_DigestAlgorithm(self, value: StringType) -> VoidType: ...
    
    def set_FormatterAlgorithm(self, value: StringType) -> VoidType: ...
    
    def set_KeyAlgorithm(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SymmetricAlgorithm(ABC, ObjectType, IDisposable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def BlockSize(self) -> IntType: ...
    
    @BlockSize.setter
    def BlockSize(self, value: IntType) -> None: ...
    
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
    def LegalBlockSizes(self) -> ArrayType[KeySizes]: ...
    
    @property
    def LegalKeySizes(self) -> ArrayType[KeySizes]: ...
    
    @property
    def Mode(self) -> CipherMode: ...
    
    @Mode.setter
    def Mode(self, value: CipherMode) -> None: ...
    
    @property
    def Padding(self) -> PaddingMode: ...
    
    @Padding.setter
    def Padding(self, value: PaddingMode) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Clear(self) -> VoidType: ...
    
    @staticmethod
    @overload
    def Create(algName: StringType) -> SymmetricAlgorithm: ...
    
    @staticmethod
    @overload
    def Create() -> SymmetricAlgorithm: ...
    
    @overload
    def CreateDecryptor(self) -> ICryptoTransform: ...
    
    @overload
    def CreateDecryptor(self, rgbKey: ArrayType[ByteType], rgbIV: ArrayType[ByteType]) -> ICryptoTransform: ...
    
    @overload
    def CreateEncryptor(self) -> ICryptoTransform: ...
    
    @overload
    def CreateEncryptor(self, rgbKey: ArrayType[ByteType], rgbIV: ArrayType[ByteType]) -> ICryptoTransform: ...
    
    def Dispose(self) -> VoidType: ...
    
    def GenerateIV(self) -> VoidType: ...
    
    def GenerateKey(self) -> VoidType: ...
    
    def ValidKeySize(self, bitLength: IntType) -> BooleanType: ...
    
    def get_BlockSize(self) -> IntType: ...
    
    def get_FeedbackSize(self) -> IntType: ...
    
    def get_IV(self) -> ArrayType[ByteType]: ...
    
    def get_Key(self) -> ArrayType[ByteType]: ...
    
    def get_KeySize(self) -> IntType: ...
    
    def get_LegalBlockSizes(self) -> ArrayType[KeySizes]: ...
    
    def get_LegalKeySizes(self) -> ArrayType[KeySizes]: ...
    
    def get_Mode(self) -> CipherMode: ...
    
    def get_Padding(self) -> PaddingMode: ...
    
    def set_BlockSize(self, value: IntType) -> VoidType: ...
    
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


class TailStream(Stream, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, bufferSize: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Buffer(self) -> ArrayType[ByteType]: ...
    
    @property
    def CanRead(self) -> BooleanType: ...
    
    @property
    def CanSeek(self) -> BooleanType: ...
    
    @property
    def CanWrite(self) -> BooleanType: ...
    
    @property
    def Length(self) -> LongType: ...
    
    @property
    def Position(self) -> LongType: ...
    
    @Position.setter
    def Position(self, value: LongType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Clear(self) -> VoidType: ...
    
    def Flush(self) -> VoidType: ...
    
    def Read(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType) -> IntType: ...
    
    def Seek(self, offset: LongType, origin: SeekOrigin) -> LongType: ...
    
    def SetLength(self, value: LongType) -> VoidType: ...
    
    def Write(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType) -> VoidType: ...
    
    def get_Buffer(self) -> ArrayType[ByteType]: ...
    
    def get_CanRead(self) -> BooleanType: ...
    
    def get_CanSeek(self) -> BooleanType: ...
    
    def get_CanWrite(self) -> BooleanType: ...
    
    def get_Length(self) -> LongType: ...
    
    def get_Position(self) -> LongType: ...
    
    def set_Position(self, value: LongType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ToBase64Transform(ObjectType, ICryptoTransform, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
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
    
    def Clear(self) -> VoidType: ...
    
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


class TripleDES(ABC, SymmetricAlgorithm, IDisposable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Key(self) -> ArrayType[ByteType]: ...
    
    @Key.setter
    def Key(self, value: ArrayType[ByteType]) -> None: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    @overload
    def Create(str: StringType) -> TripleDES: ...
    
    @staticmethod
    @overload
    def Create() -> TripleDES: ...
    
    @staticmethod
    def IsWeakKey(rgbKey: ArrayType[ByteType]) -> BooleanType: ...
    
    def get_Key(self) -> ArrayType[ByteType]: ...
    
    def set_Key(self, value: ArrayType[ByteType]) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TripleDESCryptoServiceProvider(TripleDES, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def CreateDecryptor(self, rgbKey: ArrayType[ByteType], rgbIV: ArrayType[ByteType]) -> ICryptoTransform: ...
    
    @overload
    def CreateEncryptor(self, rgbKey: ArrayType[ByteType], rgbIV: ArrayType[ByteType]) -> ICryptoTransform: ...
    
    def GenerateIV(self) -> VoidType: ...
    
    def GenerateKey(self) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Utils(ABC, ObjectType):
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


# ---------- Structs ---------- #

class DSAParameters(ValueType):
    # ---------- Fields ---------- #
    
    @property
    def Counter(self) -> IntType: ...
    
    @Counter.setter
    def Counter(self, value: IntType) -> None: ...
    
    @property
    def G(self) -> ArrayType[ByteType]: ...
    
    @G.setter
    def G(self, value: ArrayType[ByteType]) -> None: ...
    
    @property
    def J(self) -> ArrayType[ByteType]: ...
    
    @J.setter
    def J(self, value: ArrayType[ByteType]) -> None: ...
    
    @property
    def P(self) -> ArrayType[ByteType]: ...
    
    @P.setter
    def P(self, value: ArrayType[ByteType]) -> None: ...
    
    @property
    def Q(self) -> ArrayType[ByteType]: ...
    
    @Q.setter
    def Q(self, value: ArrayType[ByteType]) -> None: ...
    
    @property
    def Seed(self) -> ArrayType[ByteType]: ...
    
    @Seed.setter
    def Seed(self, value: ArrayType[ByteType]) -> None: ...
    
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


class HashAlgorithmName(ValueType, IEquatable[HashAlgorithmName]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, name: StringType): ...
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def MD5() -> HashAlgorithmName: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @staticmethod
    @property
    def SHA1() -> HashAlgorithmName: ...
    
    @staticmethod
    @property
    def SHA256() -> HashAlgorithmName: ...
    
    @staticmethod
    @property
    def SHA384() -> HashAlgorithmName: ...
    
    @staticmethod
    @property
    def SHA512() -> HashAlgorithmName: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, other: HashAlgorithmName) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    @staticmethod
    def get_MD5() -> HashAlgorithmName: ...
    
    def get_Name(self) -> StringType: ...
    
    @staticmethod
    def get_SHA1() -> HashAlgorithmName: ...
    
    @staticmethod
    def get_SHA256() -> HashAlgorithmName: ...
    
    @staticmethod
    def get_SHA384() -> HashAlgorithmName: ...
    
    @staticmethod
    def get_SHA512() -> HashAlgorithmName: ...
    
    @staticmethod
    def op_Equality(left: HashAlgorithmName, right: HashAlgorithmName) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(left: HashAlgorithmName, right: HashAlgorithmName) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RSAParameters(ValueType):
    # ---------- Fields ---------- #
    
    @property
    def D(self) -> ArrayType[ByteType]: ...
    
    @D.setter
    def D(self, value: ArrayType[ByteType]) -> None: ...
    
    @property
    def DP(self) -> ArrayType[ByteType]: ...
    
    @DP.setter
    def DP(self, value: ArrayType[ByteType]) -> None: ...
    
    @property
    def DQ(self) -> ArrayType[ByteType]: ...
    
    @DQ.setter
    def DQ(self, value: ArrayType[ByteType]) -> None: ...
    
    @property
    def Exponent(self) -> ArrayType[ByteType]: ...
    
    @Exponent.setter
    def Exponent(self, value: ArrayType[ByteType]) -> None: ...
    
    @property
    def InverseQ(self) -> ArrayType[ByteType]: ...
    
    @InverseQ.setter
    def InverseQ(self, value: ArrayType[ByteType]) -> None: ...
    
    @property
    def Modulus(self) -> ArrayType[ByteType]: ...
    
    @Modulus.setter
    def Modulus(self, value: ArrayType[ByteType]) -> None: ...
    
    @property
    def P(self) -> ArrayType[ByteType]: ...
    
    @P.setter
    def P(self, value: ArrayType[ByteType]) -> None: ...
    
    @property
    def Q(self) -> ArrayType[ByteType]: ...
    
    @Q.setter
    def Q(self, value: ArrayType[ByteType]) -> None: ...
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# ---------- Interfaces ---------- #

class ICryptoTransform(Protocol, IDisposable):
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
    
    def TransformBlock(self, inputBuffer: ArrayType[ByteType], inputOffset: IntType, inputCount: IntType, outputBuffer: ArrayType[ByteType], outputOffset: IntType) -> IntType: ...
    
    def TransformFinalBlock(self, inputBuffer: ArrayType[ByteType], inputOffset: IntType, inputCount: IntType) -> ArrayType[ByteType]: ...
    
    def get_CanReuseTransform(self) -> BooleanType: ...
    
    def get_CanTransformMultipleBlocks(self) -> BooleanType: ...
    
    def get_InputBlockSize(self) -> IntType: ...
    
    def get_OutputBlockSize(self) -> IntType: ...
    
    # No Events


class ICspAsymmetricAlgorithm(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def CspKeyContainerInfo(self) -> CspKeyContainerInfo: ...
    
    # ---------- Methods ---------- #
    
    def ExportCspBlob(self, includePrivateParameters: BooleanType) -> ArrayType[ByteType]: ...
    
    def ImportCspBlob(self, rawData: ArrayType[ByteType]) -> VoidType: ...
    
    def get_CspKeyContainerInfo(self) -> CspKeyContainerInfo: ...
    
    # No Events


# ---------- Enums ---------- #

class CipherMode(Enum):
    CBC: IntType = 1
    ECB: IntType = 2
    OFB: IntType = 3
    CFB: IntType = 4
    CTS: IntType = 5


class CryptoAPITransformMode(Enum):
    Encrypt: IntType = 0
    Decrypt: IntType = 1


class CryptoStreamMode(Enum):
    Read: IntType = 0
    Write: IntType = 1


class CspAlgorithmType(Enum):
    Rsa: IntType = 0
    Dss: IntType = 1


class CspProviderFlags(Enum):
    NoFlags: IntType = 0
    UseMachineKeyStore: IntType = 1
    UseDefaultKeyContainer: IntType = 2
    UseNonExportableKey: IntType = 4
    UseExistingKey: IntType = 8
    UseArchivableKey: IntType = 16
    UseUserProtectedKey: IntType = 32
    NoPrompt: IntType = 64
    CreateEphemeralKey: IntType = 128


class FromBase64TransformMode(Enum):
    IgnoreWhiteSpaces: IntType = 0
    DoNotIgnoreWhiteSpaces: IntType = 1


class KeyNumber(Enum):
    Exchange: IntType = 1
    Signature: IntType = 2


class OidGroup(Enum):
    All: IntType = 0
    HashAlgorithm: IntType = 1
    EncryptionAlgorithm: IntType = 2
    PublicKeyAlgorithm: IntType = 3
    SignatureAlgorithm: IntType = 4
    Attribute: IntType = 5
    ExtensionOrAttribute: IntType = 6
    EnhancedKeyUsage: IntType = 7
    Policy: IntType = 8
    Template: IntType = 9
    KeyDerivationFunction: IntType = 10


class PaddingMode(Enum):
    #None: IntType = 1
    PKCS7: IntType = 2
    Zeros: IntType = 3
    ANSIX923: IntType = 4
    ISO10126: IntType = 5


class RSAEncryptionPaddingMode(Enum):
    Pkcs1: IntType = 0
    Oaep: IntType = 1


class RSASignaturePaddingMode(Enum):
    Pkcs1: IntType = 0
    Pss: IntType = 1


class RijndaelManagedTransformMode(Enum):
    Encrypt: IntType = 0
    Decrypt: IntType = 1


# No Delegates

__all__ = [
    Aes,
    AsnEncodedData,
    AsnEncodedDataCollection,
    AsnEncodedDataEnumerator,
    AsymmetricAlgorithm,
    AsymmetricKeyExchangeDeformatter,
    AsymmetricKeyExchangeFormatter,
    AsymmetricSignatureDeformatter,
    AsymmetricSignatureFormatter,
    BigInt,
    CAPI,
    CAPIBase,
    CAPIMethods,
    CAPINative,
    CAPISafe,
    CAPIUnsafe,
    CapiNative,
    Constants,
    CryptoAPITransform,
    CryptoConfig,
    CryptoStream,
    CryptographicException,
    CryptographicUnexpectedOperationException,
    CspKeyContainerInfo,
    CspParameters,
    DES,
    DESCryptoServiceProvider,
    DSA,
    DSACryptoServiceProvider,
    DSACspObject,
    DSASignatureDeformatter,
    DSASignatureDescription,
    DSASignatureFormatter,
    DeriveBytes,
    FromBase64Transform,
    HMAC,
    HMACMD5,
    HMACRIPEMD160,
    HMACSHA1,
    HMACSHA256,
    HMACSHA384,
    HMACSHA512,
    HashAlgorithm,
    KeySizes,
    KeyedHashAlgorithm,
    MACTripleDES,
    MD5,
    MD5CryptoServiceProvider,
    MaskGenerationMethod,
    Oid,
    OidCollection,
    OidEnumerator,
    PKCS1MaskGenerationMethod,
    PasswordDeriveBytes,
    RC2,
    RC2CryptoServiceProvider,
    RIPEMD160,
    RIPEMD160Managed,
    RNGCryptoServiceProvider,
    RSA,
    RSACryptoServiceProvider,
    RSACspObject,
    RSAEncryptionPadding,
    RSAOAEPKeyExchangeDeformatter,
    RSAOAEPKeyExchangeFormatter,
    RSAPKCS1KeyExchangeDeformatter,
    RSAPKCS1KeyExchangeFormatter,
    RSAPKCS1SHA1SignatureDescription,
    RSAPKCS1SHA256SignatureDescription,
    RSAPKCS1SHA384SignatureDescription,
    RSAPKCS1SHA512SignatureDescription,
    RSAPKCS1SignatureDeformatter,
    RSAPKCS1SignatureDescription,
    RSAPKCS1SignatureFormatter,
    RSASignaturePadding,
    RandomNumberGenerator,
    Rfc2898DeriveBytes,
    Rijndael,
    RijndaelManaged,
    RijndaelManagedTransform,
    SHA1,
    SHA1CryptoServiceProvider,
    SHA1Managed,
    SHA256,
    SHA256Managed,
    SHA384,
    SHA384Managed,
    SHA512,
    SHA512Managed,
    SafeCertContextHandle,
    SafeCertStoreHandle,
    SafeCryptMsgHandle,
    SafeCryptProvHandle,
    SafeCspHandle,
    SafeCspHashHandle,
    SafeCspKeyHandle,
    SafeHashHandle,
    SafeKeyHandle,
    SafeLibraryHandle,
    SafeLocalAllocHandle,
    SafeProvHandle,
    SignatureDescription,
    SymmetricAlgorithm,
    TailStream,
    ToBase64Transform,
    TripleDES,
    TripleDESCryptoServiceProvider,
    Utils,
    DSAParameters,
    HashAlgorithmName,
    RSAParameters,
    ICryptoTransform,
    ICspAsymmetricAlgorithm,
    CipherMode,
    CryptoAPITransformMode,
    CryptoStreamMode,
    CspAlgorithmType,
    CspProviderFlags,
    FromBase64TransformMode,
    KeyNumber,
    OidGroup,
    PaddingMode,
    RSAEncryptionPaddingMode,
    RSASignaturePaddingMode,
    RijndaelManagedTransformMode,
]
