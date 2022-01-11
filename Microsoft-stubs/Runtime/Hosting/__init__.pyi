from __future__ import annotations

from abc import ABC
from typing import List, Protocol, Tuple, Union, overload

from System import Array, Boolean, Byte, Int32, IntPtr, Object, String, Void

# ---------- Types ---------- #

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
ByteType = Union[int, Byte]
IntType = Union[int, Int32]
NIntType = Union[int, IntPtr]
ObjectType = Object
StringType = Union[str, String]
VoidType = Union[None, Void]


# ---------- Classes ---------- #

class StrongNameHelpers(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def StrongNameErrorInfo() -> IntType: ...
    
    @staticmethod
    def StrongNameFreeBuffer(pbMemory: NIntType) -> VoidType: ...
    
    @staticmethod
    @overload
    def StrongNameGetPublicKey(pwzKeyContainer: StringType, pbKeyBlob: NIntType, cbKeyBlob: IntType, ppbPublicKeyBlob: NIntType, pcbPublicKeyBlob: IntType) -> Tuple[BooleanType, NIntType, IntType]: ...
    
    @staticmethod
    @overload
    def StrongNameGetPublicKey(pwzKeyContainer: StringType, bKeyBlob: ArrayType[ByteType], cbKeyBlob: IntType, ppbPublicKeyBlob: NIntType, pcbPublicKeyBlob: IntType) -> Tuple[BooleanType, NIntType, IntType]: ...
    
    @staticmethod
    def StrongNameKeyDelete(pwzKeyContainer: StringType) -> BooleanType: ...
    
    @staticmethod
    def StrongNameKeyGen(pwzKeyContainer: StringType, dwFlags: IntType, ppbKeyBlob: NIntType, pcbKeyBlob: IntType) -> Tuple[BooleanType, NIntType, IntType]: ...
    
    @staticmethod
    @overload
    def StrongNameKeyInstall(pwzKeyContainer: StringType, pbKeyBlob: NIntType, cbKeyBlob: IntType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def StrongNameKeyInstall(pwzKeyContainer: StringType, bKeyBlob: ArrayType[ByteType], cbKeyBlob: IntType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def StrongNameSignatureGeneration(pwzFilePath: StringType, pwzKeyContainer: StringType, pbKeyBlob: NIntType, cbKeyBlob: IntType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def StrongNameSignatureGeneration(pwzFilePath: StringType, pwzKeyContainer: StringType, pbKeyBlob: NIntType, cbKeyBlob: IntType, ppbSignatureBlob: NIntType, pcbSignatureBlob: IntType) -> Tuple[BooleanType, NIntType, IntType]: ...
    
    @staticmethod
    @overload
    def StrongNameSignatureGeneration(pwzFilePath: StringType, pwzKeyContainer: StringType, bKeyBlob: ArrayType[ByteType], cbKeyBlob: IntType) -> BooleanType: ...
    
    @staticmethod
    @overload
    def StrongNameSignatureGeneration(pwzFilePath: StringType, pwzKeyContainer: StringType, bKeyBlob: ArrayType[ByteType], cbKeyBlob: IntType, ppbSignatureBlob: NIntType, pcbSignatureBlob: IntType) -> Tuple[BooleanType, NIntType, IntType]: ...
    
    @staticmethod
    @overload
    def StrongNameSignatureSize(pbPublicKeyBlob: NIntType, cbPublicKeyBlob: IntType, pcbSize: IntType) -> Tuple[BooleanType, IntType]: ...
    
    @staticmethod
    @overload
    def StrongNameSignatureSize(bPublicKeyBlob: ArrayType[ByteType], cbPublicKeyBlob: IntType, pcbSize: IntType) -> Tuple[BooleanType, IntType]: ...
    
    @staticmethod
    def StrongNameSignatureVerification(pwzFilePath: StringType, dwInFlags: IntType, pdwOutFlags: IntType) -> Tuple[BooleanType, IntType]: ...
    
    @staticmethod
    def StrongNameSignatureVerificationEx(pwzFilePath: StringType, fForceVerification: BooleanType, pfWasVerified: BooleanType) -> Tuple[BooleanType, BooleanType]: ...
    
    @staticmethod
    @overload
    def StrongNameTokenFromPublicKey(pbPublicKeyBlob: NIntType, cbPublicKeyBlob: IntType, ppbStrongNameToken: NIntType, pcbStrongNameToken: IntType) -> Tuple[BooleanType, NIntType, IntType]: ...
    
    @staticmethod
    @overload
    def StrongNameTokenFromPublicKey(bPublicKeyBlob: ArrayType[ByteType], cbPublicKeyBlob: IntType, ppbStrongNameToken: NIntType, pcbStrongNameToken: IntType) -> Tuple[BooleanType, NIntType, IntType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# No Structs

# ---------- Interfaces ---------- #

class IClrStrongName(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetHashFromAssemblyFile(self, pszFilePath: StringType, piHashAlg: IntType, pbHash: ArrayType[ByteType], cchHash: IntType, pchHash: IntType) -> Tuple[IntType, IntType, ArrayType[ByteType], IntType]: ...
    
    def GetHashFromAssemblyFileW(self, pwzFilePath: StringType, piHashAlg: IntType, pbHash: ArrayType[ByteType], cchHash: IntType, pchHash: IntType) -> Tuple[IntType, IntType, ArrayType[ByteType], IntType]: ...
    
    def GetHashFromBlob(self, pbBlob: NIntType, cchBlob: IntType, piHashAlg: IntType, pbHash: ArrayType[ByteType], cchHash: IntType, pchHash: IntType) -> Tuple[IntType, IntType, ArrayType[ByteType], IntType]: ...
    
    def GetHashFromFile(self, pszFilePath: StringType, piHashAlg: IntType, pbHash: ArrayType[ByteType], cchHash: IntType, pchHash: IntType) -> Tuple[IntType, IntType, ArrayType[ByteType], IntType]: ...
    
    def GetHashFromFileW(self, pwzFilePath: StringType, piHashAlg: IntType, pbHash: ArrayType[ByteType], cchHash: IntType, pchHash: IntType) -> Tuple[IntType, IntType, ArrayType[ByteType], IntType]: ...
    
    def GetHashFromHandle(self, hFile: NIntType, piHashAlg: IntType, pbHash: ArrayType[ByteType], cchHash: IntType, pchHash: IntType) -> Tuple[IntType, IntType, ArrayType[ByteType], IntType]: ...
    
    def StrongNameCompareAssemblies(self, pwzAssembly1: StringType, pwzAssembly2: StringType, dwResult: IntType) -> Tuple[IntType, IntType]: ...
    
    def StrongNameFreeBuffer(self, pbMemory: NIntType) -> IntType: ...
    
    def StrongNameGetBlob(self, pwzFilePath: StringType, pbBlob: ArrayType[ByteType], pcbBlob: IntType) -> Tuple[IntType, ArrayType[ByteType], IntType]: ...
    
    def StrongNameGetBlobFromImage(self, pbBase: NIntType, dwLength: IntType, pbBlob: ArrayType[ByteType], pcbBlob: IntType) -> Tuple[IntType, ArrayType[ByteType], IntType]: ...
    
    def StrongNameGetPublicKey(self, pwzKeyContainer: StringType, pbKeyBlob: ArrayType[ByteType], cbKeyBlob: IntType, ppbPublicKeyBlob: NIntType, pcbPublicKeyBlob: IntType) -> Tuple[IntType, NIntType, IntType]: ...
    
    def StrongNameHashSize(self, ulHashAlg: IntType, cbSize: IntType) -> Tuple[IntType, IntType]: ...
    
    def StrongNameKeyDelete(self, pwzKeyContainer: StringType) -> IntType: ...
    
    def StrongNameKeyGen(self, pwzKeyContainer: StringType, dwFlags: IntType, ppbKeyBlob: NIntType, pcbKeyBlob: IntType) -> Tuple[IntType, NIntType, IntType]: ...
    
    def StrongNameKeyGenEx(self, pwzKeyContainer: StringType, dwFlags: IntType, dwKeySize: IntType, ppbKeyBlob: NIntType, pcbKeyBlob: IntType) -> Tuple[IntType, NIntType, IntType]: ...
    
    def StrongNameKeyInstall(self, pwzKeyContainer: StringType, pbKeyBlob: ArrayType[ByteType], cbKeyBlob: IntType) -> IntType: ...
    
    def StrongNameSignatureGeneration(self, pwzFilePath: StringType, pwzKeyContainer: StringType, pbKeyBlob: ArrayType[ByteType], cbKeyBlob: IntType, ppbSignatureBlob: NIntType, pcbSignatureBlob: IntType) -> Tuple[IntType, NIntType, IntType]: ...
    
    def StrongNameSignatureGenerationEx(self, wszFilePath: StringType, wszKeyContainer: StringType, pbKeyBlob: ArrayType[ByteType], cbKeyBlob: IntType, ppbSignatureBlob: NIntType, pcbSignatureBlob: IntType, dwFlags: IntType) -> Tuple[IntType, NIntType, IntType]: ...
    
    def StrongNameSignatureSize(self, pbPublicKeyBlob: ArrayType[ByteType], cbPublicKeyBlob: IntType, pcbSize: IntType) -> Tuple[IntType, IntType]: ...
    
    def StrongNameSignatureVerification(self, pwzFilePath: StringType, dwInFlags: IntType, dwOutFlags: IntType) -> Tuple[IntType, IntType]: ...
    
    def StrongNameSignatureVerificationEx(self, pwzFilePath: StringType, fForceVerification: BooleanType, fWasVerified: BooleanType) -> Tuple[IntType, BooleanType]: ...
    
    def StrongNameSignatureVerificationFromImage(self, pbBase: NIntType, dwLength: IntType, dwInFlags: IntType, dwOutFlags: IntType) -> Tuple[IntType, IntType]: ...
    
    def StrongNameTokenFromAssembly(self, pwzFilePath: StringType, ppbStrongNameToken: NIntType, pcbStrongNameToken: IntType) -> Tuple[IntType, NIntType, IntType]: ...
    
    def StrongNameTokenFromAssemblyEx(self, pwzFilePath: StringType, ppbStrongNameToken: NIntType, pcbStrongNameToken: IntType, ppbPublicKeyBlob: NIntType, pcbPublicKeyBlob: IntType) -> Tuple[IntType, NIntType, IntType, NIntType, IntType]: ...
    
    def StrongNameTokenFromPublicKey(self, pbPublicKeyBlob: ArrayType[ByteType], cbPublicKeyBlob: IntType, ppbStrongNameToken: NIntType, pcbStrongNameToken: IntType) -> Tuple[IntType, NIntType, IntType]: ...
    
    # No Events


class IClrStrongNameUsingIntPtr(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetHashFromAssemblyFile(self, pszFilePath: StringType, piHashAlg: IntType, pbHash: ArrayType[ByteType], cchHash: IntType, pchHash: IntType) -> Tuple[IntType, IntType, ArrayType[ByteType], IntType]: ...
    
    def GetHashFromAssemblyFileW(self, pwzFilePath: StringType, piHashAlg: IntType, pbHash: ArrayType[ByteType], cchHash: IntType, pchHash: IntType) -> Tuple[IntType, IntType, ArrayType[ByteType], IntType]: ...
    
    def GetHashFromBlob(self, pbBlob: NIntType, cchBlob: IntType, piHashAlg: IntType, pbHash: ArrayType[ByteType], cchHash: IntType, pchHash: IntType) -> Tuple[IntType, IntType, ArrayType[ByteType], IntType]: ...
    
    def GetHashFromFile(self, pszFilePath: StringType, piHashAlg: IntType, pbHash: ArrayType[ByteType], cchHash: IntType, pchHash: IntType) -> Tuple[IntType, IntType, ArrayType[ByteType], IntType]: ...
    
    def GetHashFromFileW(self, pwzFilePath: StringType, piHashAlg: IntType, pbHash: ArrayType[ByteType], cchHash: IntType, pchHash: IntType) -> Tuple[IntType, IntType, ArrayType[ByteType], IntType]: ...
    
    def GetHashFromHandle(self, hFile: NIntType, piHashAlg: IntType, pbHash: ArrayType[ByteType], cchHash: IntType, pchHash: IntType) -> Tuple[IntType, IntType, ArrayType[ByteType], IntType]: ...
    
    def StrongNameCompareAssemblies(self, pwzAssembly1: StringType, pwzAssembly2: StringType, dwResult: IntType) -> Tuple[IntType, IntType]: ...
    
    def StrongNameFreeBuffer(self, pbMemory: NIntType) -> IntType: ...
    
    def StrongNameGetBlob(self, pwzFilePath: StringType, pbBlob: ArrayType[ByteType], pcbBlob: IntType) -> Tuple[IntType, ArrayType[ByteType], IntType]: ...
    
    def StrongNameGetBlobFromImage(self, pbBase: NIntType, dwLength: IntType, pbBlob: ArrayType[ByteType], pcbBlob: IntType) -> Tuple[IntType, ArrayType[ByteType], IntType]: ...
    
    def StrongNameGetPublicKey(self, pwzKeyContainer: StringType, pbKeyBlob: NIntType, cbKeyBlob: IntType, ppbPublicKeyBlob: NIntType, pcbPublicKeyBlob: IntType) -> Tuple[IntType, NIntType, IntType]: ...
    
    def StrongNameHashSize(self, ulHashAlg: IntType, cbSize: IntType) -> Tuple[IntType, IntType]: ...
    
    def StrongNameKeyDelete(self, pwzKeyContainer: StringType) -> IntType: ...
    
    def StrongNameKeyGen(self, pwzKeyContainer: StringType, dwFlags: IntType, ppbKeyBlob: NIntType, pcbKeyBlob: IntType) -> Tuple[IntType, NIntType, IntType]: ...
    
    def StrongNameKeyGenEx(self, pwzKeyContainer: StringType, dwFlags: IntType, dwKeySize: IntType, ppbKeyBlob: NIntType, pcbKeyBlob: IntType) -> Tuple[IntType, NIntType, IntType]: ...
    
    def StrongNameKeyInstall(self, pwzKeyContainer: StringType, pbKeyBlob: NIntType, cbKeyBlob: IntType) -> IntType: ...
    
    def StrongNameSignatureGeneration(self, pwzFilePath: StringType, pwzKeyContainer: StringType, pbKeyBlob: NIntType, cbKeyBlob: IntType, ppbSignatureBlob: NIntType, pcbSignatureBlob: IntType) -> Tuple[IntType, NIntType, IntType]: ...
    
    def StrongNameSignatureGenerationEx(self, wszFilePath: StringType, wszKeyContainer: StringType, pbKeyBlob: NIntType, cbKeyBlob: IntType, ppbSignatureBlob: NIntType, pcbSignatureBlob: IntType, dwFlags: IntType) -> Tuple[IntType, NIntType, IntType]: ...
    
    def StrongNameSignatureSize(self, pbPublicKeyBlob: NIntType, cbPublicKeyBlob: IntType, pcbSize: IntType) -> Tuple[IntType, IntType]: ...
    
    def StrongNameSignatureVerification(self, pwzFilePath: StringType, dwInFlags: IntType, dwOutFlags: IntType) -> Tuple[IntType, IntType]: ...
    
    def StrongNameSignatureVerificationEx(self, pwzFilePath: StringType, fForceVerification: BooleanType, fWasVerified: BooleanType) -> Tuple[IntType, BooleanType]: ...
    
    def StrongNameSignatureVerificationFromImage(self, pbBase: NIntType, dwLength: IntType, dwInFlags: IntType, dwOutFlags: IntType) -> Tuple[IntType, IntType]: ...
    
    def StrongNameTokenFromAssembly(self, pwzFilePath: StringType, ppbStrongNameToken: NIntType, pcbStrongNameToken: IntType) -> Tuple[IntType, NIntType, IntType]: ...
    
    def StrongNameTokenFromAssemblyEx(self, pwzFilePath: StringType, ppbStrongNameToken: NIntType, pcbStrongNameToken: IntType, ppbPublicKeyBlob: NIntType, pcbPublicKeyBlob: IntType) -> Tuple[IntType, NIntType, IntType, NIntType, IntType]: ...
    
    def StrongNameTokenFromPublicKey(self, pbPublicKeyBlob: NIntType, cbPublicKeyBlob: IntType, ppbStrongNameToken: NIntType, pcbStrongNameToken: IntType) -> Tuple[IntType, NIntType, IntType]: ...
    
    # No Events


# No Enums

# No Delegates

__all__ = [
    StrongNameHelpers,
    IClrStrongName,
    IClrStrongNameUsingIntPtr,
]
