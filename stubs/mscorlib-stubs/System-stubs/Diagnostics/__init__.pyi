from __future__ import annotations

from abc import ABC
from typing import Callable, List, Protocol, Union, overload

from System import Array, AsyncCallback, Attribute, Boolean, Enum, Exception, IAsyncResult, ICloneable, IDisposable, Int32, IntPtr, MulticastDelegate, Object, String, Type, Void
from System.Reflection import MethodBase
from System.Runtime.InteropServices import _Attribute
from System.Runtime.Serialization import ISerializable
from System.Threading import Thread

# ---------- Types ---------- #

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
IntType = Union[int, Int32]
NIntType = Union[int, IntPtr]
ObjectType = Object
StringType = Union[str, String]
TypeType = Union[type, Type]
VoidType = Union[None, Void]

# ---------- Classes ---------- #

class Assert(ABC, ObjectType):
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


class AssertFilter(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def AssertFailure(self, condition: StringType, message: StringType, location: StackTrace, stackTraceFormat: TraceFormat, windowTitle: StringType) -> AssertFilters: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ConditionalAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, conditionString: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ConditionString(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_ConditionString(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DebuggableAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, isJITTrackingEnabled: BooleanType, isJITOptimizerDisabled: BooleanType): ...
    
    @overload
    def __init__(self, modes: DebuggingModes): ...
    
    # ---------- Properties ---------- #
    
    @property
    def DebuggingFlags(self) -> DebuggingModes: ...
    
    @property
    def IsJITOptimizerDisabled(self) -> BooleanType: ...
    
    @property
    def IsJITTrackingEnabled(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def get_DebuggingFlags(self) -> DebuggingModes: ...
    
    def get_IsJITOptimizerDisabled(self) -> BooleanType: ...
    
    def get_IsJITTrackingEnabled(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # ---------- Sub Enums ---------- #
    
    class DebuggingModes(Enum):
        #None: IntType = 0
        Default: IntType = 1
        IgnoreSymbolStoreSequencePoints: IntType = 2
        EnableEditAndContinue: IntType = 4
        DisableOptimizations: IntType = 256
    


class Debugger(ObjectType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def DefaultCategory() -> StringType: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def IsAttached() -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def Break() -> VoidType: ...
    
    @staticmethod
    def IsLogging() -> BooleanType: ...
    
    @staticmethod
    def Launch() -> BooleanType: ...
    
    @staticmethod
    def Log(level: IntType, category: StringType, message: StringType) -> VoidType: ...
    
    @staticmethod
    def NotifyOfCrossThreadDependency() -> VoidType: ...
    
    @staticmethod
    def get_IsAttached() -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DebuggerBrowsableAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, state: DebuggerBrowsableState): ...
    
    # ---------- Properties ---------- #
    
    @property
    def State(self) -> DebuggerBrowsableState: ...
    
    # ---------- Methods ---------- #
    
    def get_State(self) -> DebuggerBrowsableState: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DebuggerDisplayAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, value: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Name(self) -> StringType: ...
    
    @Name.setter
    def Name(self, value: StringType) -> None: ...
    
    @property
    def Target(self) -> TypeType: ...
    
    @Target.setter
    def Target(self, value: TypeType) -> None: ...
    
    @property
    def TargetTypeName(self) -> StringType: ...
    
    @TargetTypeName.setter
    def TargetTypeName(self, value: StringType) -> None: ...
    
    @property
    def Type(self) -> StringType: ...
    
    @Type.setter
    def Type(self, value: StringType) -> None: ...
    
    @property
    def Value(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_Name(self) -> StringType: ...
    
    def get_Target(self) -> TypeType: ...
    
    def get_TargetTypeName(self) -> StringType: ...
    
    def get_Type(self) -> StringType: ...
    
    def get_Value(self) -> StringType: ...
    
    def set_Name(self, value: StringType) -> VoidType: ...
    
    def set_Target(self, value: TypeType) -> VoidType: ...
    
    def set_TargetTypeName(self, value: StringType) -> VoidType: ...
    
    def set_Type(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DebuggerHiddenAttribute(Attribute, _Attribute):
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


class DebuggerNonUserCodeAttribute(Attribute, _Attribute):
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


class DebuggerStepThroughAttribute(Attribute, _Attribute):
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


class DebuggerStepperBoundaryAttribute(Attribute, _Attribute):
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


class DebuggerTypeProxyAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, type: TypeType): ...
    
    @overload
    def __init__(self, typeName: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ProxyTypeName(self) -> StringType: ...
    
    @property
    def Target(self) -> TypeType: ...
    
    @Target.setter
    def Target(self, value: TypeType) -> None: ...
    
    @property
    def TargetTypeName(self) -> StringType: ...
    
    @TargetTypeName.setter
    def TargetTypeName(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_ProxyTypeName(self) -> StringType: ...
    
    def get_Target(self) -> TypeType: ...
    
    def get_TargetTypeName(self) -> StringType: ...
    
    def set_Target(self, value: TypeType) -> VoidType: ...
    
    def set_TargetTypeName(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DebuggerVisualizerAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, visualizerTypeName: StringType): ...
    
    @overload
    def __init__(self, visualizerTypeName: StringType, visualizerObjectSourceTypeName: StringType): ...
    
    @overload
    def __init__(self, visualizerTypeName: StringType, visualizerObjectSource: TypeType): ...
    
    @overload
    def __init__(self, visualizer: TypeType): ...
    
    @overload
    def __init__(self, visualizer: TypeType, visualizerObjectSource: TypeType): ...
    
    @overload
    def __init__(self, visualizer: TypeType, visualizerObjectSourceTypeName: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Description(self) -> StringType: ...
    
    @Description.setter
    def Description(self, value: StringType) -> None: ...
    
    @property
    def Target(self) -> TypeType: ...
    
    @Target.setter
    def Target(self, value: TypeType) -> None: ...
    
    @property
    def TargetTypeName(self) -> StringType: ...
    
    @TargetTypeName.setter
    def TargetTypeName(self, value: StringType) -> None: ...
    
    @property
    def VisualizerObjectSourceTypeName(self) -> StringType: ...
    
    @property
    def VisualizerTypeName(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_Description(self) -> StringType: ...
    
    def get_Target(self) -> TypeType: ...
    
    def get_TargetTypeName(self) -> StringType: ...
    
    def get_VisualizerObjectSourceTypeName(self) -> StringType: ...
    
    def get_VisualizerTypeName(self) -> StringType: ...
    
    def set_Description(self, value: StringType) -> VoidType: ...
    
    def set_Target(self, value: TypeType) -> VoidType: ...
    
    def set_TargetTypeName(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DefaultFilter(AssertFilter):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def AssertFailure(self, condition: StringType, message: StringType, location: StackTrace, stackTraceFormat: TraceFormat, windowTitle: StringType) -> AssertFilters: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EditAndContinueHelper(ObjectType):
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


class Log(ABC, ObjectType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def GlobalSwitch() -> LogSwitch: ...
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def IsConsoleEnabled() -> BooleanType: ...
    
    @staticmethod
    @IsConsoleEnabled.setter
    def IsConsoleEnabled(value: BooleanType) -> None: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def AddOnLogMessage(handler: LogMessageEventHandler) -> VoidType: ...
    
    @staticmethod
    def AddOnLogSwitchLevel(handler: LogSwitchLevelHandler) -> VoidType: ...
    
    @staticmethod
    @overload
    def Error(logswitch: LogSwitch, message: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Error(switchname: StringType, message: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Error(message: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def LogMessage(level: LoggingLevels, message: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def LogMessage(level: LoggingLevels, logswitch: LogSwitch, message: StringType) -> VoidType: ...
    
    @staticmethod
    def Panic(message: StringType) -> VoidType: ...
    
    @staticmethod
    def RemoveOnLogMessage(handler: LogMessageEventHandler) -> VoidType: ...
    
    @staticmethod
    def RemoveOnLogSwitchLevel(handler: LogSwitchLevelHandler) -> VoidType: ...
    
    @staticmethod
    @overload
    def Status(logswitch: LogSwitch, message: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Status(switchname: StringType, message: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Status(message: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Trace(logswitch: LogSwitch, message: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Trace(switchname: StringType, message: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Trace(message: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Warning(logswitch: LogSwitch, message: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Warning(switchname: StringType, message: StringType) -> VoidType: ...
    
    @staticmethod
    @overload
    def Warning(message: StringType) -> VoidType: ...
    
    @staticmethod
    def get_IsConsoleEnabled() -> BooleanType: ...
    
    @staticmethod
    def set_IsConsoleEnabled(value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class LogMessageEventHandler(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, level: LoggingLevels, category: LogSwitch, message: StringType, location: StackTrace, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, level: LoggingLevels, category: LogSwitch, message: StringType, location: StackTrace) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class LogSwitch(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, name: StringType, description: StringType, parent: LogSwitch): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Description(self) -> StringType: ...
    
    @property
    def MinimumLevel(self) -> LoggingLevels: ...
    
    @MinimumLevel.setter
    def MinimumLevel(self, value: LoggingLevels) -> None: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def Parent(self) -> LogSwitch: ...
    
    # ---------- Methods ---------- #
    
    def CheckLevel(self, level: LoggingLevels) -> BooleanType: ...
    
    @staticmethod
    def GetSwitch(name: StringType) -> LogSwitch: ...
    
    def get_Description(self) -> StringType: ...
    
    def get_MinimumLevel(self) -> LoggingLevels: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_Parent(self) -> LogSwitch: ...
    
    def set_MinimumLevel(self, value: LoggingLevels) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class LogSwitchLevelHandler(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, ls: LogSwitch, newLevel: LoggingLevels, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, ls: LogSwitch, newLevel: LoggingLevels) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class StackFrame(ObjectType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def OFFSET_UNKNOWN() -> IntType: ...
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, fNeedFileInfo: BooleanType): ...
    
    @overload
    def __init__(self, skipFrames: IntType): ...
    
    @overload
    def __init__(self, skipFrames: IntType, fNeedFileInfo: BooleanType): ...
    
    @overload
    def __init__(self, fileName: StringType, lineNumber: IntType): ...
    
    @overload
    def __init__(self, fileName: StringType, lineNumber: IntType, colNumber: IntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetFileColumnNumber(self) -> IntType: ...
    
    def GetFileLineNumber(self) -> IntType: ...
    
    def GetFileName(self) -> StringType: ...
    
    def GetILOffset(self) -> IntType: ...
    
    def GetMethod(self) -> MethodBase: ...
    
    def GetNativeOffset(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class StackFrameHelper(ObjectType, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, target: Thread): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetColumnNumber(self, i: IntType) -> IntType: ...
    
    def GetFilename(self, i: IntType) -> StringType: ...
    
    def GetILOffset(self, i: IntType) -> IntType: ...
    
    def GetLineNumber(self, i: IntType) -> IntType: ...
    
    def GetMethodBase(self, i: IntType) -> MethodBase: ...
    
    def GetNumberOfFrames(self) -> IntType: ...
    
    def GetOffset(self, i: IntType) -> IntType: ...
    
    def IsLastFrameFromForeignExceptionStackTrace(self, i: IntType) -> BooleanType: ...
    
    def SetNumberOfFrames(self, i: IntType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class StackTrace(ObjectType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def METHODS_TO_SKIP() -> IntType: ...
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, fNeedFileInfo: BooleanType): ...
    
    @overload
    def __init__(self, skipFrames: IntType): ...
    
    @overload
    def __init__(self, skipFrames: IntType, fNeedFileInfo: BooleanType): ...
    
    @overload
    def __init__(self, e: Exception): ...
    
    @overload
    def __init__(self, e: Exception, fNeedFileInfo: BooleanType): ...
    
    @overload
    def __init__(self, e: Exception, skipFrames: IntType): ...
    
    @overload
    def __init__(self, e: Exception, skipFrames: IntType, fNeedFileInfo: BooleanType): ...
    
    @overload
    def __init__(self, frame: StackFrame): ...
    
    @overload
    def __init__(self, targetThread: Thread, needFileInfo: BooleanType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def FrameCount(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def GetFrame(self, index: IntType) -> StackFrame: ...
    
    def GetFrames(self) -> ArrayType[StackFrame]: ...
    
    def ToString(self) -> StringType: ...
    
    def get_FrameCount(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# No Structs

# ---------- Interfaces ---------- #

class ICustomDebuggerNotification(Protocol):
    """"""
    
    # No Properties
    
    # No Methods
    
    # No Events


# ---------- Enums ---------- #

class AssertFilters(Enum):
    FailDebug: IntType = 0
    FailIgnore: IntType = 1
    FailTerminate: IntType = 2
    FailContinueFilter: IntType = 3


class DebuggerBrowsableState(Enum):
    Never: IntType = 0
    Collapsed: IntType = 2
    RootHidden: IntType = 3


class LoggingLevels(Enum):
    TraceLevel0: IntType = 0
    TraceLevel1: IntType = 1
    TraceLevel2: IntType = 2
    TraceLevel3: IntType = 3
    TraceLevel4: IntType = 4
    StatusLevel0: IntType = 20
    StatusLevel1: IntType = 21
    StatusLevel2: IntType = 22
    StatusLevel3: IntType = 23
    StatusLevel4: IntType = 24
    WarningLevel: IntType = 40
    ErrorLevel: IntType = 50
    PanicLevel: IntType = 100


# ---------- Delegates ---------- #

LogMessageEventHandler = Callable[[LoggingLevels, LogSwitch, StringType, StackTrace], VoidType]

LogSwitchLevelHandler = Callable[[LogSwitch, LoggingLevels], VoidType]

__all__ = [
    Assert,
    AssertFilter,
    ConditionalAttribute,
    DebuggableAttribute,
    Debugger,
    DebuggerBrowsableAttribute,
    DebuggerDisplayAttribute,
    DebuggerHiddenAttribute,
    DebuggerNonUserCodeAttribute,
    DebuggerStepThroughAttribute,
    DebuggerStepperBoundaryAttribute,
    DebuggerTypeProxyAttribute,
    DebuggerVisualizerAttribute,
    DefaultFilter,
    EditAndContinueHelper,
    Log,
    LogMessageEventHandler,
    LogSwitch,
    LogSwitchLevelHandler,
    StackFrame,
    StackFrameHelper,
    StackTrace,
    ICustomDebuggerNotification,
    AssertFilters,
    DebuggerBrowsableState,
    LoggingLevels,
    LogMessageEventHandler,
    LogSwitchLevelHandler,
]
