from abc import ABC
from typing import overload

from System import Array
from System import IntPtr
from System import Object
from System import Type

class IClrStrongName:
    """"""

    def GetHashFromAssemblyFile(
        self,
        pszFilePath: str,
        piHashAlg: int,
        pbHash: Array[int],
        cchHash: int,
        pchHash: int,
    ) -> tuple[int, int, Array[int], int]:
        """:param pszFilePath:
        :param piHashAlg:
        :param pbHash:
        :param cchHash:
        :param pchHash:
        :return:
        """
    def GetHashFromAssemblyFileW(
        self,
        pwzFilePath: str,
        piHashAlg: int,
        pbHash: Array[int],
        cchHash: int,
        pchHash: int,
    ) -> tuple[int, int, Array[int], int]:
        """:param pwzFilePath:
        :param piHashAlg:
        :param pbHash:
        :param cchHash:
        :param pchHash:
        :return:
        """
    def GetHashFromBlob(
        self,
        pbBlob: IntPtr,
        cchBlob: int,
        piHashAlg: int,
        pbHash: Array[int],
        cchHash: int,
        pchHash: int,
    ) -> tuple[int, int, Array[int], int]:
        """:param pbBlob:
        :param cchBlob:
        :param piHashAlg:
        :param pbHash:
        :param cchHash:
        :param pchHash:
        :return:
        """
    def GetHashFromFile(
        self,
        pszFilePath: str,
        piHashAlg: int,
        pbHash: Array[int],
        cchHash: int,
        pchHash: int,
    ) -> tuple[int, int, Array[int], int]:
        """:param pszFilePath:
        :param piHashAlg:
        :param pbHash:
        :param cchHash:
        :param pchHash:
        :return:
        """
    def GetHashFromFileW(
        self,
        pwzFilePath: str,
        piHashAlg: int,
        pbHash: Array[int],
        cchHash: int,
        pchHash: int,
    ) -> tuple[int, int, Array[int], int]:
        """:param pwzFilePath:
        :param piHashAlg:
        :param pbHash:
        :param cchHash:
        :param pchHash:
        :return:
        """
    def GetHashFromHandle(
        self,
        hFile: IntPtr,
        piHashAlg: int,
        pbHash: Array[int],
        cchHash: int,
        pchHash: int,
    ) -> tuple[int, int, Array[int], int]:
        """:param hFile:
        :param piHashAlg:
        :param pbHash:
        :param cchHash:
        :param pchHash:
        :return:
        """
    def StrongNameCompareAssemblies(
        self, pwzAssembly1: str, pwzAssembly2: str, dwResult: int
    ) -> tuple[int, int]:
        """:param pwzAssembly1:
        :param pwzAssembly2:
        :param dwResult:
        :return:
        """
    def StrongNameFreeBuffer(self, pbMemory: IntPtr) -> int:
        """:param pbMemory:
        :return:
        """
    def StrongNameGetBlob(
        self, pwzFilePath: str, pbBlob: Array[int], pcbBlob: int
    ) -> tuple[int, Array[int], int]:
        """:param pwzFilePath:
        :param pbBlob:
        :param pcbBlob:
        :return:
        """
    def StrongNameGetBlobFromImage(
        self, pbBase: IntPtr, dwLength: int, pbBlob: Array[int], pcbBlob: int
    ) -> tuple[int, Array[int], int]:
        """:param pbBase:
        :param dwLength:
        :param pbBlob:
        :param pcbBlob:
        :return:
        """
    def StrongNameGetPublicKey(
        self,
        pwzKeyContainer: str,
        pbKeyBlob: Array[int],
        cbKeyBlob: int,
        ppbPublicKeyBlob: IntPtr,
        pcbPublicKeyBlob: int,
    ) -> tuple[int, IntPtr, int]:
        """:param pwzKeyContainer:
        :param pbKeyBlob:
        :param cbKeyBlob:
        :param ppbPublicKeyBlob:
        :param pcbPublicKeyBlob:
        :return:
        """
    def StrongNameHashSize(self, ulHashAlg: int, cbSize: int) -> tuple[int, int]:
        """:param ulHashAlg:
        :param cbSize:
        :return:
        """
    def StrongNameKeyDelete(self, pwzKeyContainer: str) -> int:
        """:param pwzKeyContainer:
        :return:
        """
    def StrongNameKeyGen(
        self, pwzKeyContainer: str, dwFlags: int, ppbKeyBlob: IntPtr, pcbKeyBlob: int
    ) -> tuple[int, IntPtr, int]:
        """:param pwzKeyContainer:
        :param dwFlags:
        :param ppbKeyBlob:
        :param pcbKeyBlob:
        :return:
        """
    def StrongNameKeyGenEx(
        self,
        pwzKeyContainer: str,
        dwFlags: int,
        dwKeySize: int,
        ppbKeyBlob: IntPtr,
        pcbKeyBlob: int,
    ) -> tuple[int, IntPtr, int]:
        """:param pwzKeyContainer:
        :param dwFlags:
        :param dwKeySize:
        :param ppbKeyBlob:
        :param pcbKeyBlob:
        :return:
        """
    def StrongNameKeyInstall(
        self, pwzKeyContainer: str, pbKeyBlob: Array[int], cbKeyBlob: int
    ) -> int:
        """:param pwzKeyContainer:
        :param pbKeyBlob:
        :param cbKeyBlob:
        :return:
        """
    def StrongNameSignatureGeneration(
        self,
        pwzFilePath: str,
        pwzKeyContainer: str,
        pbKeyBlob: Array[int],
        cbKeyBlob: int,
        ppbSignatureBlob: IntPtr,
        pcbSignatureBlob: int,
    ) -> tuple[int, IntPtr, int]:
        """:param pwzFilePath:
        :param pwzKeyContainer:
        :param pbKeyBlob:
        :param cbKeyBlob:
        :param ppbSignatureBlob:
        :param pcbSignatureBlob:
        :return:
        """
    def StrongNameSignatureGenerationEx(
        self,
        wszFilePath: str,
        wszKeyContainer: str,
        pbKeyBlob: Array[int],
        cbKeyBlob: int,
        ppbSignatureBlob: IntPtr,
        pcbSignatureBlob: int,
        dwFlags: int,
    ) -> tuple[int, IntPtr, int]:
        """:param wszFilePath:
        :param wszKeyContainer:
        :param pbKeyBlob:
        :param cbKeyBlob:
        :param ppbSignatureBlob:
        :param pcbSignatureBlob:
        :param dwFlags:
        :return:
        """
    def StrongNameSignatureSize(
        self, pbPublicKeyBlob: Array[int], cbPublicKeyBlob: int, pcbSize: int
    ) -> tuple[int, int]:
        """:param pbPublicKeyBlob:
        :param cbPublicKeyBlob:
        :param pcbSize:
        :return:
        """
    def StrongNameSignatureVerification(
        self, pwzFilePath: str, dwInFlags: int, dwOutFlags: int
    ) -> tuple[int, int]:
        """:param pwzFilePath:
        :param dwInFlags:
        :param dwOutFlags:
        :return:
        """
    def StrongNameSignatureVerificationEx(
        self, pwzFilePath: str, fForceVerification: bool, fWasVerified: bool
    ) -> tuple[int, bool]:
        """:param pwzFilePath:
        :param fForceVerification:
        :param fWasVerified:
        :return:
        """
    def StrongNameSignatureVerificationFromImage(
        self, pbBase: IntPtr, dwLength: int, dwInFlags: int, dwOutFlags: int
    ) -> tuple[int, int]:
        """:param pbBase:
        :param dwLength:
        :param dwInFlags:
        :param dwOutFlags:
        :return:
        """
    def StrongNameTokenFromAssembly(
        self, pwzFilePath: str, ppbStrongNameToken: IntPtr, pcbStrongNameToken: int
    ) -> tuple[int, IntPtr, int]:
        """:param pwzFilePath:
        :param ppbStrongNameToken:
        :param pcbStrongNameToken:
        :return:
        """
    def StrongNameTokenFromAssemblyEx(
        self,
        pwzFilePath: str,
        ppbStrongNameToken: IntPtr,
        pcbStrongNameToken: int,
        ppbPublicKeyBlob: IntPtr,
        pcbPublicKeyBlob: int,
    ) -> tuple[int, IntPtr, int, IntPtr, int]:
        """:param pwzFilePath:
        :param ppbStrongNameToken:
        :param pcbStrongNameToken:
        :param ppbPublicKeyBlob:
        :param pcbPublicKeyBlob:
        :return:
        """
    def StrongNameTokenFromPublicKey(
        self,
        pbPublicKeyBlob: Array[int],
        cbPublicKeyBlob: int,
        ppbStrongNameToken: IntPtr,
        pcbStrongNameToken: int,
    ) -> tuple[int, IntPtr, int]:
        """:param pbPublicKeyBlob:
        :param cbPublicKeyBlob:
        :param ppbStrongNameToken:
        :param pcbStrongNameToken:
        :return:
        """

class IClrStrongNameUsingIntPtr:
    """"""

    def GetHashFromAssemblyFile(
        self,
        pszFilePath: str,
        piHashAlg: int,
        pbHash: Array[int],
        cchHash: int,
        pchHash: int,
    ) -> tuple[int, int, Array[int], int]:
        """:param pszFilePath:
        :param piHashAlg:
        :param pbHash:
        :param cchHash:
        :param pchHash:
        :return:
        """
    def GetHashFromAssemblyFileW(
        self,
        pwzFilePath: str,
        piHashAlg: int,
        pbHash: Array[int],
        cchHash: int,
        pchHash: int,
    ) -> tuple[int, int, Array[int], int]:
        """:param pwzFilePath:
        :param piHashAlg:
        :param pbHash:
        :param cchHash:
        :param pchHash:
        :return:
        """
    def GetHashFromBlob(
        self,
        pbBlob: IntPtr,
        cchBlob: int,
        piHashAlg: int,
        pbHash: Array[int],
        cchHash: int,
        pchHash: int,
    ) -> tuple[int, int, Array[int], int]:
        """:param pbBlob:
        :param cchBlob:
        :param piHashAlg:
        :param pbHash:
        :param cchHash:
        :param pchHash:
        :return:
        """
    def GetHashFromFile(
        self,
        pszFilePath: str,
        piHashAlg: int,
        pbHash: Array[int],
        cchHash: int,
        pchHash: int,
    ) -> tuple[int, int, Array[int], int]:
        """:param pszFilePath:
        :param piHashAlg:
        :param pbHash:
        :param cchHash:
        :param pchHash:
        :return:
        """
    def GetHashFromFileW(
        self,
        pwzFilePath: str,
        piHashAlg: int,
        pbHash: Array[int],
        cchHash: int,
        pchHash: int,
    ) -> tuple[int, int, Array[int], int]:
        """:param pwzFilePath:
        :param piHashAlg:
        :param pbHash:
        :param cchHash:
        :param pchHash:
        :return:
        """
    def GetHashFromHandle(
        self,
        hFile: IntPtr,
        piHashAlg: int,
        pbHash: Array[int],
        cchHash: int,
        pchHash: int,
    ) -> tuple[int, int, Array[int], int]:
        """:param hFile:
        :param piHashAlg:
        :param pbHash:
        :param cchHash:
        :param pchHash:
        :return:
        """
    def StrongNameCompareAssemblies(
        self, pwzAssembly1: str, pwzAssembly2: str, dwResult: int
    ) -> tuple[int, int]:
        """:param pwzAssembly1:
        :param pwzAssembly2:
        :param dwResult:
        :return:
        """
    def StrongNameFreeBuffer(self, pbMemory: IntPtr) -> int:
        """:param pbMemory:
        :return:
        """
    def StrongNameGetBlob(
        self, pwzFilePath: str, pbBlob: Array[int], pcbBlob: int
    ) -> tuple[int, Array[int], int]:
        """:param pwzFilePath:
        :param pbBlob:
        :param pcbBlob:
        :return:
        """
    def StrongNameGetBlobFromImage(
        self, pbBase: IntPtr, dwLength: int, pbBlob: Array[int], pcbBlob: int
    ) -> tuple[int, Array[int], int]:
        """:param pbBase:
        :param dwLength:
        :param pbBlob:
        :param pcbBlob:
        :return:
        """
    def StrongNameGetPublicKey(
        self,
        pwzKeyContainer: str,
        pbKeyBlob: IntPtr,
        cbKeyBlob: int,
        ppbPublicKeyBlob: IntPtr,
        pcbPublicKeyBlob: int,
    ) -> tuple[int, IntPtr, int]:
        """:param pwzKeyContainer:
        :param pbKeyBlob:
        :param cbKeyBlob:
        :param ppbPublicKeyBlob:
        :param pcbPublicKeyBlob:
        :return:
        """
    def StrongNameHashSize(self, ulHashAlg: int, cbSize: int) -> tuple[int, int]:
        """:param ulHashAlg:
        :param cbSize:
        :return:
        """
    def StrongNameKeyDelete(self, pwzKeyContainer: str) -> int:
        """:param pwzKeyContainer:
        :return:
        """
    def StrongNameKeyGen(
        self, pwzKeyContainer: str, dwFlags: int, ppbKeyBlob: IntPtr, pcbKeyBlob: int
    ) -> tuple[int, IntPtr, int]:
        """:param pwzKeyContainer:
        :param dwFlags:
        :param ppbKeyBlob:
        :param pcbKeyBlob:
        :return:
        """
    def StrongNameKeyGenEx(
        self,
        pwzKeyContainer: str,
        dwFlags: int,
        dwKeySize: int,
        ppbKeyBlob: IntPtr,
        pcbKeyBlob: int,
    ) -> tuple[int, IntPtr, int]:
        """:param pwzKeyContainer:
        :param dwFlags:
        :param dwKeySize:
        :param ppbKeyBlob:
        :param pcbKeyBlob:
        :return:
        """
    def StrongNameKeyInstall(self, pwzKeyContainer: str, pbKeyBlob: IntPtr, cbKeyBlob: int) -> int:
        """:param pwzKeyContainer:
        :param pbKeyBlob:
        :param cbKeyBlob:
        :return:
        """
    def StrongNameSignatureGeneration(
        self,
        pwzFilePath: str,
        pwzKeyContainer: str,
        pbKeyBlob: IntPtr,
        cbKeyBlob: int,
        ppbSignatureBlob: IntPtr,
        pcbSignatureBlob: int,
    ) -> tuple[int, IntPtr, int]:
        """:param pwzFilePath:
        :param pwzKeyContainer:
        :param pbKeyBlob:
        :param cbKeyBlob:
        :param ppbSignatureBlob:
        :param pcbSignatureBlob:
        :return:
        """
    def StrongNameSignatureGenerationEx(
        self,
        wszFilePath: str,
        wszKeyContainer: str,
        pbKeyBlob: IntPtr,
        cbKeyBlob: int,
        ppbSignatureBlob: IntPtr,
        pcbSignatureBlob: int,
        dwFlags: int,
    ) -> tuple[int, IntPtr, int]:
        """:param wszFilePath:
        :param wszKeyContainer:
        :param pbKeyBlob:
        :param cbKeyBlob:
        :param ppbSignatureBlob:
        :param pcbSignatureBlob:
        :param dwFlags:
        :return:
        """
    def StrongNameSignatureSize(
        self, pbPublicKeyBlob: IntPtr, cbPublicKeyBlob: int, pcbSize: int
    ) -> tuple[int, int]:
        """:param pbPublicKeyBlob:
        :param cbPublicKeyBlob:
        :param pcbSize:
        :return:
        """
    def StrongNameSignatureVerification(
        self, pwzFilePath: str, dwInFlags: int, dwOutFlags: int
    ) -> tuple[int, int]:
        """:param pwzFilePath:
        :param dwInFlags:
        :param dwOutFlags:
        :return:
        """
    def StrongNameSignatureVerificationEx(
        self, pwzFilePath: str, fForceVerification: bool, fWasVerified: bool
    ) -> tuple[int, bool]:
        """:param pwzFilePath:
        :param fForceVerification:
        :param fWasVerified:
        :return:
        """
    def StrongNameSignatureVerificationFromImage(
        self, pbBase: IntPtr, dwLength: int, dwInFlags: int, dwOutFlags: int
    ) -> tuple[int, int]:
        """:param pbBase:
        :param dwLength:
        :param dwInFlags:
        :param dwOutFlags:
        :return:
        """
    def StrongNameTokenFromAssembly(
        self, pwzFilePath: str, ppbStrongNameToken: IntPtr, pcbStrongNameToken: int
    ) -> tuple[int, IntPtr, int]:
        """:param pwzFilePath:
        :param ppbStrongNameToken:
        :param pcbStrongNameToken:
        :return:
        """
    def StrongNameTokenFromAssemblyEx(
        self,
        pwzFilePath: str,
        ppbStrongNameToken: IntPtr,
        pcbStrongNameToken: int,
        ppbPublicKeyBlob: IntPtr,
        pcbPublicKeyBlob: int,
    ) -> tuple[int, IntPtr, int, IntPtr, int]:
        """:param pwzFilePath:
        :param ppbStrongNameToken:
        :param pcbStrongNameToken:
        :param ppbPublicKeyBlob:
        :param pcbPublicKeyBlob:
        :return:
        """
    def StrongNameTokenFromPublicKey(
        self,
        pbPublicKeyBlob: IntPtr,
        cbPublicKeyBlob: int,
        ppbStrongNameToken: IntPtr,
        pcbStrongNameToken: int,
    ) -> tuple[int, IntPtr, int]:
        """:param pbPublicKeyBlob:
        :param cbPublicKeyBlob:
        :param ppbStrongNameToken:
        :param pcbStrongNameToken:
        :return:
        """

class StrongNameHelpers(ABC, Object):
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
    def StrongNameErrorInfo(cls) -> int:
        """:return:"""
    @classmethod
    def StrongNameFreeBuffer(cls, pbMemory: IntPtr) -> None:
        """:param pbMemory:"""
    @classmethod
    @overload
    def StrongNameGetPublicKey(
        cls,
        pwzKeyContainer: str,
        bKeyBlob: Array[int],
        cbKeyBlob: int,
        ppbPublicKeyBlob: IntPtr,
        pcbPublicKeyBlob: int,
    ) -> tuple[bool, IntPtr, int]:
        """:param pwzKeyContainer:
        :param bKeyBlob:
        :param cbKeyBlob:
        :param ppbPublicKeyBlob:
        :param pcbPublicKeyBlob:
        :return:
        """
    @classmethod
    @overload
    def StrongNameGetPublicKey(
        cls,
        pwzKeyContainer: str,
        pbKeyBlob: IntPtr,
        cbKeyBlob: int,
        ppbPublicKeyBlob: IntPtr,
        pcbPublicKeyBlob: int,
    ) -> tuple[bool, IntPtr, int]:
        """:param pwzKeyContainer:
        :param pbKeyBlob:
        :param cbKeyBlob:
        :param ppbPublicKeyBlob:
        :param pcbPublicKeyBlob:
        :return:
        """
    @classmethod
    def StrongNameKeyDelete(cls, pwzKeyContainer: str) -> bool:
        """:param pwzKeyContainer:
        :return:
        """
    @classmethod
    def StrongNameKeyGen(
        cls, pwzKeyContainer: str, dwFlags: int, ppbKeyBlob: IntPtr, pcbKeyBlob: int
    ) -> tuple[bool, IntPtr, int]:
        """:param pwzKeyContainer:
        :param dwFlags:
        :param ppbKeyBlob:
        :param pcbKeyBlob:
        :return:
        """
    @classmethod
    @overload
    def StrongNameKeyInstall(
        cls, pwzKeyContainer: str, bKeyBlob: Array[int], cbKeyBlob: int
    ) -> bool:
        """:param pwzKeyContainer:
        :param bKeyBlob:
        :param cbKeyBlob:
        :return:
        """
    @classmethod
    @overload
    def StrongNameKeyInstall(cls, pwzKeyContainer: str, pbKeyBlob: IntPtr, cbKeyBlob: int) -> bool:
        """:param pwzKeyContainer:
        :param pbKeyBlob:
        :param cbKeyBlob:
        :return:
        """
    @classmethod
    @overload
    def StrongNameSignatureGeneration(
        cls,
        pwzFilePath: str,
        pwzKeyContainer: str,
        bKeyBlob: Array[int],
        cbKeyBlob: int,
    ) -> bool:
        """:param pwzFilePath:
        :param pwzKeyContainer:
        :param bKeyBlob:
        :param cbKeyBlob:
        :return:
        """
    @classmethod
    @overload
    def StrongNameSignatureGeneration(
        cls, pwzFilePath: str, pwzKeyContainer: str, pbKeyBlob: IntPtr, cbKeyBlob: int
    ) -> bool:
        """:param pwzFilePath:
        :param pwzKeyContainer:
        :param pbKeyBlob:
        :param cbKeyBlob:
        :return:
        """
    @classmethod
    @overload
    def StrongNameSignatureGeneration(
        cls,
        pwzFilePath: str,
        pwzKeyContainer: str,
        bKeyBlob: Array[int],
        cbKeyBlob: int,
        ppbSignatureBlob: IntPtr,
        pcbSignatureBlob: int,
    ) -> tuple[bool, int]:
        """:param pwzFilePath:
        :param pwzKeyContainer:
        :param bKeyBlob:
        :param cbKeyBlob:
        :param ppbSignatureBlob:
        :param pcbSignatureBlob:
        :return:
        """
    @classmethod
    @overload
    def StrongNameSignatureGeneration(
        cls,
        pwzFilePath: str,
        pwzKeyContainer: str,
        pbKeyBlob: IntPtr,
        cbKeyBlob: int,
        ppbSignatureBlob: IntPtr,
        pcbSignatureBlob: int,
    ) -> tuple[bool, int]:
        """:param pwzFilePath:
        :param pwzKeyContainer:
        :param pbKeyBlob:
        :param cbKeyBlob:
        :param ppbSignatureBlob:
        :param pcbSignatureBlob:
        :return:
        """
    @classmethod
    @overload
    def StrongNameSignatureSize(
        cls, bPublicKeyBlob: Array[int], cbPublicKeyBlob: int, pcbSize: int
    ) -> tuple[bool, int]:
        """:param bPublicKeyBlob:
        :param cbPublicKeyBlob:
        :param pcbSize:
        :return:
        """
    @classmethod
    @overload
    def StrongNameSignatureSize(
        cls, pbPublicKeyBlob: IntPtr, cbPublicKeyBlob: int, pcbSize: int
    ) -> tuple[bool, int]:
        """:param pbPublicKeyBlob:
        :param cbPublicKeyBlob:
        :param pcbSize:
        :return:
        """
    @classmethod
    def StrongNameSignatureVerification(
        cls, pwzFilePath: str, dwInFlags: int, pdwOutFlags: int
    ) -> tuple[bool, int]:
        """:param pwzFilePath:
        :param dwInFlags:
        :param pdwOutFlags:
        :return:
        """
    @classmethod
    def StrongNameSignatureVerificationEx(
        cls, pwzFilePath: str, fForceVerification: bool, pfWasVerified: bool
    ) -> tuple[bool, bool]:
        """:param pwzFilePath:
        :param fForceVerification:
        :param pfWasVerified:
        :return:
        """
    @classmethod
    @overload
    def StrongNameTokenFromPublicKey(
        cls,
        bPublicKeyBlob: Array[int],
        cbPublicKeyBlob: int,
        ppbStrongNameToken: IntPtr,
        pcbStrongNameToken: int,
    ) -> tuple[bool, IntPtr, int]:
        """:param bPublicKeyBlob:
        :param cbPublicKeyBlob:
        :param ppbStrongNameToken:
        :param pcbStrongNameToken:
        :return:
        """
    @classmethod
    @overload
    def StrongNameTokenFromPublicKey(
        cls,
        pbPublicKeyBlob: IntPtr,
        cbPublicKeyBlob: int,
        ppbStrongNameToken: IntPtr,
        pcbStrongNameToken: int,
    ) -> tuple[bool, IntPtr, int]:
        """:param pbPublicKeyBlob:
        :param cbPublicKeyBlob:
        :param ppbStrongNameToken:
        :param pcbStrongNameToken:
        :return:
        """
    def ToString(self) -> str:
        """:return:"""
