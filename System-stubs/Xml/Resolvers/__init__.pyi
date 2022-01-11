from __future__ import annotations

from typing import List, Union, overload

from System import Array, Boolean, Byte, Enum, Int32, Object, String, Type, Uri, Void
from System.Collections.Generic import IEnumerable, IEqualityComparer
from System.IO import Stream
from System.Net import ICredentials
from System.Threading.Tasks import Task
from System.Xml import XmlResolver

# ---------- Types ---------- #

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
ByteType = Union[int, Byte]
IntType = Union[int, Int32]
ObjectType = Object
StringType = Union[str, String]
TypeType = Union[type, Type]
VoidType = Union[None, Void]


# ---------- Classes ---------- #

class XmlPreloadedResolver(XmlResolver):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, preloadedDtds: XmlKnownDtds): ...
    
    @overload
    def __init__(self, fallbackResolver: XmlResolver): ...
    
    @overload
    def __init__(self, fallbackResolver: XmlResolver, preloadedDtds: XmlKnownDtds): ...
    
    @overload
    def __init__(self, fallbackResolver: XmlResolver, preloadedDtds: XmlKnownDtds, uriComparer: IEqualityComparer[Uri]): ...
    
    # ---------- Properties ---------- #
    
    @Credentials.setter
    def Credentials(self, value: ICredentials) -> None: ...
    
    @property
    def PreloadedUris(self) -> IEnumerable[Uri]: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Add(self, uri: Uri, value: ArrayType[ByteType]) -> VoidType: ...
    
    @overload
    def Add(self, uri: Uri, value: ArrayType[ByteType], offset: IntType, count: IntType) -> VoidType: ...
    
    @overload
    def Add(self, uri: Uri, value: StringType) -> VoidType: ...
    
    @overload
    def Add(self, uri: Uri, value: Stream) -> VoidType: ...
    
    def GetEntity(self, absoluteUri: Uri, role: StringType, ofObjectToReturn: TypeType) -> ObjectType: ...
    
    def GetEntityAsync(self, absoluteUri: Uri, role: StringType, ofObjectToReturn: TypeType) -> Task[ObjectType]: ...
    
    def Remove(self, uri: Uri) -> VoidType: ...
    
    def ResolveUri(self, baseUri: Uri, relativeUri: StringType) -> Uri: ...
    
    def SupportsType(self, absoluteUri: Uri, type: TypeType) -> BooleanType: ...
    
    def get_PreloadedUris(self) -> IEnumerable[Uri]: ...
    
    def set_Credentials(self, value: ICredentials) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# No Structs

# No Interfaces

# ---------- Enums ---------- #

class XmlKnownDtds(Enum):
    #None: IntType = 0
    Xhtml10: IntType = 1
    Rss091: IntType = 2
    All: IntType = 65535


# No Delegates

__all__ = [
    XmlPreloadedResolver,
    XmlKnownDtds,
]
