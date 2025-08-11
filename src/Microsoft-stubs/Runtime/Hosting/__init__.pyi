"""Automatically generated stubs for C# namespace: Microsoft.Runtime.Hosting."""

from abc import ABC
from typing import overload

from System import Array
from System import Boolean
from System import Int32
from System import IntPtr
from System import Object
from System import Type

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IClrStrongName(ABC):
    """"""
    def GetHashFromAssemblyFile(
        self, pszFilePath: str, piHashAlg: Int32, pbHash: Array[int], cchHash: int, pchHash: Int32
    ) -> tuple[int, Int32, Array[int], Int32]:
        """"""
    def GetHashFromAssemblyFileW(
        self, pwzFilePath: str, piHashAlg: Int32, pbHash: Array[int], cchHash: int, pchHash: Int32
    ) -> tuple[int, Int32, Array[int], Int32]:
        """"""
    def GetHashFromBlob(
        self,
        pbBlob: IntPtr,
        cchBlob: int,
        piHashAlg: Int32,
        pbHash: Array[int],
        cchHash: int,
        pchHash: Int32,
    ) -> tuple[int, Int32, Array[int], Int32]:
        """"""
    def GetHashFromFile(
        self, pszFilePath: str, piHashAlg: Int32, pbHash: Array[int], cchHash: int, pchHash: Int32
    ) -> tuple[int, Int32, Array[int], Int32]:
        """"""
    def GetHashFromFileW(
        self, pwzFilePath: str, piHashAlg: Int32, pbHash: Array[int], cchHash: int, pchHash: Int32
    ) -> tuple[int, Int32, Array[int], Int32]:
        """"""
    def GetHashFromHandle(
        self, hFile: IntPtr, piHashAlg: Int32, pbHash: Array[int], cchHash: int, pchHash: Int32
    ) -> tuple[int, Int32, Array[int], Int32]:
        """"""
    def StrongNameCompareAssemblies(
        self, pwzAssembly1: str, pwzAssembly2: str, dwResult: Int32
    ) -> tuple[int, Int32]:
        """"""
    def StrongNameFreeBuffer(self, pbMemory: IntPtr) -> int:
        """"""
    def StrongNameGetBlob(
        self, pwzFilePath: str, pbBlob: Array[int], pcbBlob: Int32
    ) -> tuple[int, Array[int], Int32]:
        """"""
    def StrongNameGetBlobFromImage(
        self, pbBase: IntPtr, dwLength: int, pbBlob: Array[int], pcbBlob: Int32
    ) -> tuple[int, Array[int], Int32]:
        """"""
    def StrongNameGetPublicKey(
        self,
        pwzKeyContainer: str,
        pbKeyBlob: Array[int],
        cbKeyBlob: int,
        ppbPublicKeyBlob: IntPtr,
        pcbPublicKeyBlob: Int32,
    ) -> tuple[int, IntPtr, Int32]:
        """"""
    def StrongNameHashSize(self, ulHashAlg: int, cbSize: Int32) -> tuple[int, Int32]:
        """"""
    def StrongNameKeyDelete(self, pwzKeyContainer: str) -> int:
        """"""
    def StrongNameKeyGen(
        self, pwzKeyContainer: str, dwFlags: int, ppbKeyBlob: IntPtr, pcbKeyBlob: Int32
    ) -> tuple[int, IntPtr, Int32]:
        """"""
    def StrongNameKeyGenEx(
        self,
        pwzKeyContainer: str,
        dwFlags: int,
        dwKeySize: int,
        ppbKeyBlob: IntPtr,
        pcbKeyBlob: Int32,
    ) -> tuple[int, IntPtr, Int32]:
        """"""
    def StrongNameKeyInstall(
        self, pwzKeyContainer: str, pbKeyBlob: Array[int], cbKeyBlob: int
    ) -> int:
        """"""
    def StrongNameSignatureGeneration(
        self,
        pwzFilePath: str,
        pwzKeyContainer: str,
        pbKeyBlob: Array[int],
        cbKeyBlob: int,
        ppbSignatureBlob: IntPtr,
        pcbSignatureBlob: Int32,
    ) -> tuple[int, IntPtr, Int32]:
        """"""
    def StrongNameSignatureGenerationEx(
        self,
        wszFilePath: str,
        wszKeyContainer: str,
        pbKeyBlob: Array[int],
        cbKeyBlob: int,
        ppbSignatureBlob: IntPtr,
        pcbSignatureBlob: Int32,
        dwFlags: int,
    ) -> tuple[int, IntPtr, Int32]:
        """"""
    def StrongNameSignatureSize(
        self, pbPublicKeyBlob: Array[int], cbPublicKeyBlob: int, pcbSize: Int32
    ) -> tuple[int, Int32]:
        """"""
    def StrongNameSignatureVerification(
        self, pwzFilePath: str, dwInFlags: int, dwOutFlags: Int32
    ) -> tuple[int, Int32]:
        """"""
    def StrongNameSignatureVerificationEx(
        self, pwzFilePath: str, fForceVerification: bool, fWasVerified: Boolean
    ) -> tuple[int, Boolean]:
        """"""
    def StrongNameSignatureVerificationFromImage(
        self, pbBase: IntPtr, dwLength: int, dwInFlags: int, dwOutFlags: Int32
    ) -> tuple[int, Int32]:
        """"""
    def StrongNameTokenFromAssembly(
        self, pwzFilePath: str, ppbStrongNameToken: IntPtr, pcbStrongNameToken: Int32
    ) -> tuple[int, IntPtr, Int32]:
        """"""
    def StrongNameTokenFromAssemblyEx(
        self,
        pwzFilePath: str,
        ppbStrongNameToken: IntPtr,
        pcbStrongNameToken: Int32,
        ppbPublicKeyBlob: IntPtr,
        pcbPublicKeyBlob: Int32,
    ) -> tuple[int, IntPtr, Int32, IntPtr, Int32]:
        """"""
    def StrongNameTokenFromPublicKey(
        self,
        pbPublicKeyBlob: Array[int],
        cbPublicKeyBlob: int,
        ppbStrongNameToken: IntPtr,
        pcbStrongNameToken: Int32,
    ) -> tuple[int, IntPtr, Int32]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IClrStrongNameUsingIntPtr(ABC):
    """"""
    def GetHashFromAssemblyFile(
        self, pszFilePath: str, piHashAlg: Int32, pbHash: Array[int], cchHash: int, pchHash: Int32
    ) -> tuple[int, Int32, Array[int], Int32]:
        """"""
    def GetHashFromAssemblyFileW(
        self, pwzFilePath: str, piHashAlg: Int32, pbHash: Array[int], cchHash: int, pchHash: Int32
    ) -> tuple[int, Int32, Array[int], Int32]:
        """"""
    def GetHashFromBlob(
        self,
        pbBlob: IntPtr,
        cchBlob: int,
        piHashAlg: Int32,
        pbHash: Array[int],
        cchHash: int,
        pchHash: Int32,
    ) -> tuple[int, Int32, Array[int], Int32]:
        """"""
    def GetHashFromFile(
        self, pszFilePath: str, piHashAlg: Int32, pbHash: Array[int], cchHash: int, pchHash: Int32
    ) -> tuple[int, Int32, Array[int], Int32]:
        """"""
    def GetHashFromFileW(
        self, pwzFilePath: str, piHashAlg: Int32, pbHash: Array[int], cchHash: int, pchHash: Int32
    ) -> tuple[int, Int32, Array[int], Int32]:
        """"""
    def GetHashFromHandle(
        self, hFile: IntPtr, piHashAlg: Int32, pbHash: Array[int], cchHash: int, pchHash: Int32
    ) -> tuple[int, Int32, Array[int], Int32]:
        """"""
    def StrongNameCompareAssemblies(
        self, pwzAssembly1: str, pwzAssembly2: str, dwResult: Int32
    ) -> tuple[int, Int32]:
        """"""
    def StrongNameFreeBuffer(self, pbMemory: IntPtr) -> int:
        """"""
    def StrongNameGetBlob(
        self, pwzFilePath: str, pbBlob: Array[int], pcbBlob: Int32
    ) -> tuple[int, Array[int], Int32]:
        """"""
    def StrongNameGetBlobFromImage(
        self, pbBase: IntPtr, dwLength: int, pbBlob: Array[int], pcbBlob: Int32
    ) -> tuple[int, Array[int], Int32]:
        """"""
    def StrongNameGetPublicKey(
        self,
        pwzKeyContainer: str,
        pbKeyBlob: IntPtr,
        cbKeyBlob: int,
        ppbPublicKeyBlob: IntPtr,
        pcbPublicKeyBlob: Int32,
    ) -> tuple[int, IntPtr, Int32]:
        """"""
    def StrongNameHashSize(self, ulHashAlg: int, cbSize: Int32) -> tuple[int, Int32]:
        """"""
    def StrongNameKeyDelete(self, pwzKeyContainer: str) -> int:
        """"""
    def StrongNameKeyGen(
        self, pwzKeyContainer: str, dwFlags: int, ppbKeyBlob: IntPtr, pcbKeyBlob: Int32
    ) -> tuple[int, IntPtr, Int32]:
        """"""
    def StrongNameKeyGenEx(
        self,
        pwzKeyContainer: str,
        dwFlags: int,
        dwKeySize: int,
        ppbKeyBlob: IntPtr,
        pcbKeyBlob: Int32,
    ) -> tuple[int, IntPtr, Int32]:
        """"""
    def StrongNameKeyInstall(self, pwzKeyContainer: str, pbKeyBlob: IntPtr, cbKeyBlob: int) -> int:
        """"""
    def StrongNameSignatureGeneration(
        self,
        pwzFilePath: str,
        pwzKeyContainer: str,
        pbKeyBlob: IntPtr,
        cbKeyBlob: int,
        ppbSignatureBlob: IntPtr,
        pcbSignatureBlob: Int32,
    ) -> tuple[int, IntPtr, Int32]:
        """"""
    def StrongNameSignatureGenerationEx(
        self,
        wszFilePath: str,
        wszKeyContainer: str,
        pbKeyBlob: IntPtr,
        cbKeyBlob: int,
        ppbSignatureBlob: IntPtr,
        pcbSignatureBlob: Int32,
        dwFlags: int,
    ) -> tuple[int, IntPtr, Int32]:
        """"""
    def StrongNameSignatureSize(
        self, pbPublicKeyBlob: IntPtr, cbPublicKeyBlob: int, pcbSize: Int32
    ) -> tuple[int, Int32]:
        """"""
    def StrongNameSignatureVerification(
        self, pwzFilePath: str, dwInFlags: int, dwOutFlags: Int32
    ) -> tuple[int, Int32]:
        """"""
    def StrongNameSignatureVerificationEx(
        self, pwzFilePath: str, fForceVerification: bool, fWasVerified: Boolean
    ) -> tuple[int, Boolean]:
        """"""
    def StrongNameSignatureVerificationFromImage(
        self, pbBase: IntPtr, dwLength: int, dwInFlags: int, dwOutFlags: Int32
    ) -> tuple[int, Int32]:
        """"""
    def StrongNameTokenFromAssembly(
        self, pwzFilePath: str, ppbStrongNameToken: IntPtr, pcbStrongNameToken: Int32
    ) -> tuple[int, IntPtr, Int32]:
        """"""
    def StrongNameTokenFromAssemblyEx(
        self,
        pwzFilePath: str,
        ppbStrongNameToken: IntPtr,
        pcbStrongNameToken: Int32,
        ppbPublicKeyBlob: IntPtr,
        pcbPublicKeyBlob: Int32,
    ) -> tuple[int, IntPtr, Int32, IntPtr, Int32]:
        """"""
    def StrongNameTokenFromPublicKey(
        self,
        pbPublicKeyBlob: IntPtr,
        cbPublicKeyBlob: int,
        ppbStrongNameToken: IntPtr,
        pcbStrongNameToken: Int32,
    ) -> tuple[int, IntPtr, Int32]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class StrongNameHelpers(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def StrongNameErrorInfo(cls) -> int:
        """"""
    @classmethod
    def StrongNameFreeBuffer(cls, pbMemory: IntPtr) -> None:
        """"""
    @classmethod
    @overload
    def StrongNameGetPublicKey(
        cls,
        pwzKeyContainer: str,
        bKeyBlob: Array[int],
        cbKeyBlob: int,
        ppbPublicKeyBlob: IntPtr,
        pcbPublicKeyBlob: Int32,
    ) -> tuple[bool, IntPtr, Int32]:
        """"""
    @classmethod
    @overload
    def StrongNameGetPublicKey(
        cls,
        pwzKeyContainer: str,
        pbKeyBlob: IntPtr,
        cbKeyBlob: int,
        ppbPublicKeyBlob: IntPtr,
        pcbPublicKeyBlob: Int32,
    ) -> tuple[bool, IntPtr, Int32]:
        """"""
    @classmethod
    def StrongNameKeyDelete(cls, pwzKeyContainer: str) -> bool:
        """"""
    @classmethod
    def StrongNameKeyGen(
        cls, pwzKeyContainer: str, dwFlags: int, ppbKeyBlob: IntPtr, pcbKeyBlob: Int32
    ) -> tuple[bool, IntPtr, Int32]:
        """"""
    @classmethod
    @overload
    def StrongNameKeyInstall(
        cls, pwzKeyContainer: str, bKeyBlob: Array[int], cbKeyBlob: int
    ) -> bool:
        """"""
    @classmethod
    @overload
    def StrongNameKeyInstall(cls, pwzKeyContainer: str, pbKeyBlob: IntPtr, cbKeyBlob: int) -> bool:
        """"""
    @classmethod
    @overload
    def StrongNameSignatureGeneration(
        cls, pwzFilePath: str, pwzKeyContainer: str, bKeyBlob: Array[int], cbKeyBlob: int
    ) -> bool:
        """"""
    @classmethod
    @overload
    def StrongNameSignatureGeneration(
        cls,
        pwzFilePath: str,
        pwzKeyContainer: str,
        bKeyBlob: Array[int],
        cbKeyBlob: int,
        ppbSignatureBlob: IntPtr,
        pcbSignatureBlob: Int32,
    ) -> tuple[bool, Int32]:
        """"""
    @classmethod
    @overload
    def StrongNameSignatureGeneration(
        cls, pwzFilePath: str, pwzKeyContainer: str, pbKeyBlob: IntPtr, cbKeyBlob: int
    ) -> bool:
        """"""
    @classmethod
    @overload
    def StrongNameSignatureGeneration(
        cls,
        pwzFilePath: str,
        pwzKeyContainer: str,
        pbKeyBlob: IntPtr,
        cbKeyBlob: int,
        ppbSignatureBlob: IntPtr,
        pcbSignatureBlob: Int32,
    ) -> tuple[bool, Int32]:
        """"""
    @classmethod
    @overload
    def StrongNameSignatureSize(
        cls, bPublicKeyBlob: Array[int], cbPublicKeyBlob: int, pcbSize: Int32
    ) -> tuple[bool, Int32]:
        """"""
    @classmethod
    @overload
    def StrongNameSignatureSize(
        cls, pbPublicKeyBlob: IntPtr, cbPublicKeyBlob: int, pcbSize: Int32
    ) -> tuple[bool, Int32]:
        """"""
    @classmethod
    def StrongNameSignatureVerification(
        cls, pwzFilePath: str, dwInFlags: int, pdwOutFlags: Int32
    ) -> tuple[bool, Int32]:
        """"""
    @classmethod
    def StrongNameSignatureVerificationEx(
        cls, pwzFilePath: str, fForceVerification: bool, pfWasVerified: Boolean
    ) -> tuple[bool, Boolean]:
        """"""
    @classmethod
    @overload
    def StrongNameTokenFromPublicKey(
        cls,
        bPublicKeyBlob: Array[int],
        cbPublicKeyBlob: int,
        ppbStrongNameToken: IntPtr,
        pcbStrongNameToken: Int32,
    ) -> tuple[bool, IntPtr, Int32]:
        """"""
    @classmethod
    @overload
    def StrongNameTokenFromPublicKey(
        cls,
        pbPublicKeyBlob: IntPtr,
        cbPublicKeyBlob: int,
        ppbStrongNameToken: IntPtr,
        pcbStrongNameToken: Int32,
    ) -> tuple[bool, IntPtr, Int32]:
        """"""
    def ToString(self) -> str:
        """"""
