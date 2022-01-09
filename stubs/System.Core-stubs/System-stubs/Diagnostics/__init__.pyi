from __future__ import annotations

from typing import List, Tuple, Union, overload

from System import Array, Boolean, Enum, Guid, IDisposable, Int32, Int64, IntPtr, Object, String, Void
from System.Diagnostics import TextWriterTraceListener, TraceEventCache, TraceEventType
from System.IO import TextWriter

# ---------- Types ---------- #

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
IntType = Union[int, Int32]
LongType = Union[int, Int64]
NIntType = Union[int, IntPtr]
ObjectType = Object
StringType = Union[str, String]
VoidType = Union[None, Void]

# ---------- Classes ---------- #

class EventSchemaTraceListener(TextWriterTraceListener, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, fileName: StringType): ...
    
    @overload
    def __init__(self, fileName: StringType, name: StringType): ...
    
    @overload
    def __init__(self, fileName: StringType, name: StringType, bufferSize: IntType): ...
    
    @overload
    def __init__(self, fileName: StringType, name: StringType, bufferSize: IntType, logRetentionOption: TraceLogRetentionOption): ...
    
    @overload
    def __init__(self, fileName: StringType, name: StringType, bufferSize: IntType, logRetentionOption: TraceLogRetentionOption, maximumFileSize: LongType): ...
    
    @overload
    def __init__(self, fileName: StringType, name: StringType, bufferSize: IntType, logRetentionOption: TraceLogRetentionOption, maximumFileSize: LongType, maximumNumberOfFiles: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def BufferSize(self) -> IntType: ...
    
    @property
    def IsThreadSafe(self) -> BooleanType: ...
    
    @property
    def MaximumFileSize(self) -> LongType: ...
    
    @property
    def MaximumNumberOfFiles(self) -> IntType: ...
    
    @property
    def TraceLogRetentionOption(self) -> TraceLogRetentionOption: ...
    
    @property
    def Writer(self) -> TextWriter: ...
    
    @Writer.setter
    def Writer(self, value: TextWriter) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    @overload
    def Fail(self, message: StringType, detailMessage: StringType) -> VoidType: ...
    
    def Flush(self) -> VoidType: ...
    
    @overload
    def TraceData(self, eventCache: TraceEventCache, source: StringType, eventType: TraceEventType, id: IntType, data: ObjectType) -> VoidType: ...
    
    @overload
    def TraceData(self, eventCache: TraceEventCache, source: StringType, eventType: TraceEventType, id: IntType, data: ArrayType[ObjectType]) -> VoidType: ...
    
    @overload
    def TraceEvent(self, eventCache: TraceEventCache, source: StringType, eventType: TraceEventType, id: IntType, format: StringType, args: ArrayType[ObjectType]) -> VoidType: ...
    
    @overload
    def TraceEvent(self, eventCache: TraceEventCache, source: StringType, eventType: TraceEventType, id: IntType, message: StringType) -> VoidType: ...
    
    def TraceTransfer(self, eventCache: TraceEventCache, source: StringType, id: IntType, message: StringType, relatedActivityId: Guid) -> VoidType: ...
    
    @overload
    def Write(self, message: StringType) -> VoidType: ...
    
    @overload
    def WriteLine(self, message: StringType) -> VoidType: ...
    
    def get_BufferSize(self) -> IntType: ...
    
    def get_IsThreadSafe(self) -> BooleanType: ...
    
    def get_MaximumFileSize(self) -> LongType: ...
    
    def get_MaximumNumberOfFiles(self) -> IntType: ...
    
    def get_TraceLogRetentionOption(self) -> TraceLogRetentionOption: ...
    
    @overload
    def get_Writer(self) -> TextWriter: ...
    
    @overload
    def set_Writer(self, value: TextWriter) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class StackTraceSymbols(ObjectType, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetSourceLineInfo(self, assemblyPath: StringType, loadedPeAddress: NIntType, loadedPeSize: IntType, inMemoryPdbAddress: NIntType, inMemoryPdbSize: IntType, methodToken: IntType, ilOffset: IntType, sourceFile: StringType, sourceLine: IntType, sourceColumn: IntType) -> Tuple[VoidType, StringType, IntType, IntType]: ...
    
    def GetSourceLineInfoWithoutCasAssert(self, assemblyPath: StringType, loadedPeAddress: NIntType, loadedPeSize: IntType, inMemoryPdbAddress: NIntType, inMemoryPdbSize: IntType, methodToken: IntType, ilOffset: IntType, sourceFile: StringType, sourceLine: IntType, sourceColumn: IntType) -> Tuple[VoidType, StringType, IntType, IntType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UnescapedXmlDiagnosticData(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, xmlPayload: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def UnescapedXml(self) -> StringType: ...
    
    @UnescapedXml.setter
    def UnescapedXml(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def ToString(self) -> StringType: ...
    
    def get_UnescapedXml(self) -> StringType: ...
    
    def set_UnescapedXml(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# No Structs

# No Interfaces

# ---------- Enums ---------- #

class TraceLogRetentionOption(Enum):
    UnlimitedSequentialFiles: IntType = 0
    LimitedCircularFiles: IntType = 1
    SingleFileUnboundedSize: IntType = 2
    LimitedSequentialFiles: IntType = 3
    SingleFileBoundedSize: IntType = 4


# No Delegates

__all__ = [
    EventSchemaTraceListener,
    StackTraceSymbols,
    UnescapedXmlDiagnosticData,
    TraceLogRetentionOption,
]
