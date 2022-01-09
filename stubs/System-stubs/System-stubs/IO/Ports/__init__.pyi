from __future__ import annotations

from abc import ABC
from typing import Callable, Generic, List, Tuple, Union, overload

from System import Array, AsyncCallback, Boolean, Byte, Char, Enum, EventArgs, IAsyncResult, ICloneable, IDisposable, Int32, Int64, IntPtr, MulticastDelegate, Object, String, Void
from System.ComponentModel import Component, IComponent, IContainer
from System.IO import SeekOrigin, Stream
from System.Runtime.Serialization import ISerializable
from System.Text import Encoding

# ---------- Types ---------- #

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
ByteType = Union[int, Byte]
CharType = Union[str, Char]
IntType = Union[int, Int32]
LongType = Union[int, Int64]
NIntType = Union[int, IntPtr]
ObjectType = Object
StringType = Union[str, String]
VoidType = Union[None, Void]


class EventType(Generic[T]):
    def __iadd__(self, other: T): ...
    
    def __isub__(self, other: T): ...


# ---------- Classes ---------- #

class InternalResources(ABC, ObjectType):
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


class SerialDataReceivedEventArgs(EventArgs):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def EventType(self) -> SerialData: ...
    
    # ---------- Methods ---------- #
    
    def get_EventType(self) -> SerialData: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SerialDataReceivedEventHandler(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, sender: ObjectType, e: SerialDataReceivedEventArgs, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, sender: ObjectType, e: SerialDataReceivedEventArgs) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SerialErrorReceivedEventArgs(EventArgs):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def EventType(self) -> SerialError: ...
    
    # ---------- Methods ---------- #
    
    def get_EventType(self) -> SerialError: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SerialErrorReceivedEventHandler(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, sender: ObjectType, e: SerialErrorReceivedEventArgs, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, sender: ObjectType, e: SerialErrorReceivedEventArgs) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SerialPinChangedEventArgs(EventArgs):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def EventType(self) -> SerialPinChange: ...
    
    # ---------- Methods ---------- #
    
    def get_EventType(self) -> SerialPinChange: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SerialPinChangedEventHandler(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, sender: ObjectType, e: SerialPinChangedEventArgs, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, sender: ObjectType, e: SerialPinChangedEventArgs) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SerialPort(Component, IComponent, IDisposable):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def InfiniteTimeout() -> IntType: ...
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, container: IContainer): ...
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, portName: StringType): ...
    
    @overload
    def __init__(self, portName: StringType, baudRate: IntType): ...
    
    @overload
    def __init__(self, portName: StringType, baudRate: IntType, parity: Parity): ...
    
    @overload
    def __init__(self, portName: StringType, baudRate: IntType, parity: Parity, dataBits: IntType): ...
    
    @overload
    def __init__(self, portName: StringType, baudRate: IntType, parity: Parity, dataBits: IntType, stopBits: StopBits): ...
    
    # ---------- Properties ---------- #
    
    @property
    def BaseStream(self) -> Stream: ...
    
    @property
    def BaudRate(self) -> IntType: ...
    
    @BaudRate.setter
    def BaudRate(self, value: IntType) -> None: ...
    
    @property
    def BreakState(self) -> BooleanType: ...
    
    @BreakState.setter
    def BreakState(self, value: BooleanType) -> None: ...
    
    @property
    def BytesToRead(self) -> IntType: ...
    
    @property
    def BytesToWrite(self) -> IntType: ...
    
    @property
    def CDHolding(self) -> BooleanType: ...
    
    @property
    def CtsHolding(self) -> BooleanType: ...
    
    @property
    def DataBits(self) -> IntType: ...
    
    @DataBits.setter
    def DataBits(self, value: IntType) -> None: ...
    
    @property
    def DiscardNull(self) -> BooleanType: ...
    
    @DiscardNull.setter
    def DiscardNull(self, value: BooleanType) -> None: ...
    
    @property
    def DsrHolding(self) -> BooleanType: ...
    
    @property
    def DtrEnable(self) -> BooleanType: ...
    
    @DtrEnable.setter
    def DtrEnable(self, value: BooleanType) -> None: ...
    
    @property
    def Encoding(self) -> Encoding: ...
    
    @Encoding.setter
    def Encoding(self, value: Encoding) -> None: ...
    
    @property
    def Handshake(self) -> Handshake: ...
    
    @Handshake.setter
    def Handshake(self, value: Handshake) -> None: ...
    
    @property
    def IsOpen(self) -> BooleanType: ...
    
    @property
    def NewLine(self) -> StringType: ...
    
    @NewLine.setter
    def NewLine(self, value: StringType) -> None: ...
    
    @property
    def Parity(self) -> Parity: ...
    
    @Parity.setter
    def Parity(self, value: Parity) -> None: ...
    
    @property
    def ParityReplace(self) -> ByteType: ...
    
    @ParityReplace.setter
    def ParityReplace(self, value: ByteType) -> None: ...
    
    @property
    def PortName(self) -> StringType: ...
    
    @PortName.setter
    def PortName(self, value: StringType) -> None: ...
    
    @property
    def ReadBufferSize(self) -> IntType: ...
    
    @ReadBufferSize.setter
    def ReadBufferSize(self, value: IntType) -> None: ...
    
    @property
    def ReadTimeout(self) -> IntType: ...
    
    @ReadTimeout.setter
    def ReadTimeout(self, value: IntType) -> None: ...
    
    @property
    def ReceivedBytesThreshold(self) -> IntType: ...
    
    @ReceivedBytesThreshold.setter
    def ReceivedBytesThreshold(self, value: IntType) -> None: ...
    
    @property
    def RtsEnable(self) -> BooleanType: ...
    
    @RtsEnable.setter
    def RtsEnable(self, value: BooleanType) -> None: ...
    
    @property
    def StopBits(self) -> StopBits: ...
    
    @StopBits.setter
    def StopBits(self, value: StopBits) -> None: ...
    
    @property
    def WriteBufferSize(self) -> IntType: ...
    
    @WriteBufferSize.setter
    def WriteBufferSize(self, value: IntType) -> None: ...
    
    @property
    def WriteTimeout(self) -> IntType: ...
    
    @WriteTimeout.setter
    def WriteTimeout(self, value: IntType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    def DiscardInBuffer(self) -> VoidType: ...
    
    def DiscardOutBuffer(self) -> VoidType: ...
    
    @staticmethod
    def GetPortNames() -> ArrayType[StringType]: ...
    
    def Open(self) -> VoidType: ...
    
    @overload
    def Read(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType) -> IntType: ...
    
    @overload
    def Read(self, buffer: ArrayType[CharType], offset: IntType, count: IntType) -> IntType: ...
    
    def ReadByte(self) -> IntType: ...
    
    def ReadChar(self) -> IntType: ...
    
    def ReadExisting(self) -> StringType: ...
    
    def ReadLine(self) -> StringType: ...
    
    def ReadTo(self, value: StringType) -> StringType: ...
    
    @overload
    def Write(self, text: StringType) -> VoidType: ...
    
    @overload
    def Write(self, buffer: ArrayType[CharType], offset: IntType, count: IntType) -> VoidType: ...
    
    @overload
    def Write(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType) -> VoidType: ...
    
    def WriteLine(self, text: StringType) -> VoidType: ...
    
    def add_DataReceived(self, value: SerialDataReceivedEventHandler) -> VoidType: ...
    
    def add_ErrorReceived(self, value: SerialErrorReceivedEventHandler) -> VoidType: ...
    
    def add_PinChanged(self, value: SerialPinChangedEventHandler) -> VoidType: ...
    
    def get_BaseStream(self) -> Stream: ...
    
    def get_BaudRate(self) -> IntType: ...
    
    def get_BreakState(self) -> BooleanType: ...
    
    def get_BytesToRead(self) -> IntType: ...
    
    def get_BytesToWrite(self) -> IntType: ...
    
    def get_CDHolding(self) -> BooleanType: ...
    
    def get_CtsHolding(self) -> BooleanType: ...
    
    def get_DataBits(self) -> IntType: ...
    
    def get_DiscardNull(self) -> BooleanType: ...
    
    def get_DsrHolding(self) -> BooleanType: ...
    
    def get_DtrEnable(self) -> BooleanType: ...
    
    def get_Encoding(self) -> Encoding: ...
    
    def get_Handshake(self) -> Handshake: ...
    
    def get_IsOpen(self) -> BooleanType: ...
    
    def get_NewLine(self) -> StringType: ...
    
    def get_Parity(self) -> Parity: ...
    
    def get_ParityReplace(self) -> ByteType: ...
    
    def get_PortName(self) -> StringType: ...
    
    def get_ReadBufferSize(self) -> IntType: ...
    
    def get_ReadTimeout(self) -> IntType: ...
    
    def get_ReceivedBytesThreshold(self) -> IntType: ...
    
    def get_RtsEnable(self) -> BooleanType: ...
    
    def get_StopBits(self) -> StopBits: ...
    
    def get_WriteBufferSize(self) -> IntType: ...
    
    def get_WriteTimeout(self) -> IntType: ...
    
    def remove_DataReceived(self, value: SerialDataReceivedEventHandler) -> VoidType: ...
    
    def remove_ErrorReceived(self, value: SerialErrorReceivedEventHandler) -> VoidType: ...
    
    def remove_PinChanged(self, value: SerialPinChangedEventHandler) -> VoidType: ...
    
    def set_BaudRate(self, value: IntType) -> VoidType: ...
    
    def set_BreakState(self, value: BooleanType) -> VoidType: ...
    
    def set_DataBits(self, value: IntType) -> VoidType: ...
    
    def set_DiscardNull(self, value: BooleanType) -> VoidType: ...
    
    def set_DtrEnable(self, value: BooleanType) -> VoidType: ...
    
    def set_Encoding(self, value: Encoding) -> VoidType: ...
    
    def set_Handshake(self, value: Handshake) -> VoidType: ...
    
    def set_NewLine(self, value: StringType) -> VoidType: ...
    
    def set_Parity(self, value: Parity) -> VoidType: ...
    
    def set_ParityReplace(self, value: ByteType) -> VoidType: ...
    
    def set_PortName(self, value: StringType) -> VoidType: ...
    
    def set_ReadBufferSize(self, value: IntType) -> VoidType: ...
    
    def set_ReadTimeout(self, value: IntType) -> VoidType: ...
    
    def set_ReceivedBytesThreshold(self, value: IntType) -> VoidType: ...
    
    def set_RtsEnable(self, value: BooleanType) -> VoidType: ...
    
    def set_StopBits(self, value: StopBits) -> VoidType: ...
    
    def set_WriteBufferSize(self, value: IntType) -> VoidType: ...
    
    def set_WriteTimeout(self, value: IntType) -> VoidType: ...
    
    # ---------- Events ---------- #
    
    DataReceived: EventType[SerialDataReceivedEventHandler] = ...
    
    ErrorReceived: EventType[SerialErrorReceivedEventHandler] = ...
    
    PinChanged: EventType[SerialPinChangedEventHandler] = ...
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SerialStream(Stream, IDisposable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def BreakState(self) -> BooleanType: ...
    
    @BreakState.setter
    def BreakState(self, value: BooleanType) -> None: ...
    
    @property
    def CanRead(self) -> BooleanType: ...
    
    @property
    def CanSeek(self) -> BooleanType: ...
    
    @property
    def CanTimeout(self) -> BooleanType: ...
    
    @property
    def CanWrite(self) -> BooleanType: ...
    
    @property
    def Length(self) -> LongType: ...
    
    @property
    def Position(self) -> LongType: ...
    
    @Position.setter
    def Position(self, value: LongType) -> None: ...
    
    @property
    def ReadTimeout(self) -> IntType: ...
    
    @ReadTimeout.setter
    def ReadTimeout(self, value: IntType) -> None: ...
    
    @property
    def WriteTimeout(self) -> IntType: ...
    
    @WriteTimeout.setter
    def WriteTimeout(self, value: IntType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def BeginRead(self, array: ArrayType[ByteType], offset: IntType, numBytes: IntType, userCallback: AsyncCallback, stateObject: ObjectType) -> IAsyncResult: ...
    
    def BeginWrite(self, array: ArrayType[ByteType], offset: IntType, numBytes: IntType, userCallback: AsyncCallback, stateObject: ObjectType) -> IAsyncResult: ...
    
    def EndRead(self, asyncResult: IAsyncResult) -> IntType: ...
    
    def EndWrite(self, asyncResult: IAsyncResult) -> VoidType: ...
    
    def Flush(self) -> VoidType: ...
    
    def Read(self, array: ArrayType[ByteType], offset: IntType, count: IntType) -> Tuple[IntType, ArrayType[ByteType]]: ...
    
    def ReadByte(self) -> IntType: ...
    
    def Seek(self, offset: LongType, origin: SeekOrigin) -> LongType: ...
    
    def SetLength(self, value: LongType) -> VoidType: ...
    
    def Write(self, array: ArrayType[ByteType], offset: IntType, count: IntType) -> VoidType: ...
    
    def WriteByte(self, value: ByteType) -> VoidType: ...
    
    def get_BreakState(self) -> BooleanType: ...
    
    def get_CanRead(self) -> BooleanType: ...
    
    def get_CanSeek(self) -> BooleanType: ...
    
    def get_CanTimeout(self) -> BooleanType: ...
    
    def get_CanWrite(self) -> BooleanType: ...
    
    def get_Length(self) -> LongType: ...
    
    def get_Position(self) -> LongType: ...
    
    def get_ReadTimeout(self) -> IntType: ...
    
    def get_WriteTimeout(self) -> IntType: ...
    
    def set_BreakState(self, value: BooleanType) -> VoidType: ...
    
    def set_Position(self, value: LongType) -> VoidType: ...
    
    def set_ReadTimeout(self, value: IntType) -> VoidType: ...
    
    def set_WriteTimeout(self, value: IntType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# No Structs

# No Interfaces

# ---------- Enums ---------- #

class Handshake(Enum):
    #None: IntType = 0
    XOnXOff: IntType = 1
    RequestToSend: IntType = 2
    RequestToSendXOnXOff: IntType = 3


class Parity(Enum):
    #None: IntType = 0
    Odd: IntType = 1
    Even: IntType = 2
    Mark: IntType = 3
    Space: IntType = 4


class SerialData(Enum):
    Chars: IntType = 1
    Eof: IntType = 2


class SerialError(Enum):
    RXOver: IntType = 1
    Overrun: IntType = 2
    RXParity: IntType = 4
    Frame: IntType = 8
    TXFull: IntType = 256


class SerialPinChange(Enum):
    CtsChanged: IntType = 8
    DsrChanged: IntType = 16
    CDChanged: IntType = 32
    Break: IntType = 64
    Ring: IntType = 256


class StopBits(Enum):
    #None: IntType = 0
    One: IntType = 1
    Two: IntType = 2
    OnePointFive: IntType = 3


# ---------- Delegates ---------- #

SerialDataReceivedEventHandler = Callable[[ObjectType, SerialDataReceivedEventArgs], VoidType]

SerialErrorReceivedEventHandler = Callable[[ObjectType, SerialErrorReceivedEventArgs], VoidType]

SerialPinChangedEventHandler = Callable[[ObjectType, SerialPinChangedEventArgs], VoidType]

__all__ = [
    InternalResources,
    SerialDataReceivedEventArgs,
    SerialDataReceivedEventHandler,
    SerialErrorReceivedEventArgs,
    SerialErrorReceivedEventHandler,
    SerialPinChangedEventArgs,
    SerialPinChangedEventHandler,
    SerialPort,
    SerialStream,
    Handshake,
    Parity,
    SerialData,
    SerialError,
    SerialPinChange,
    StopBits,
    SerialDataReceivedEventHandler,
    SerialErrorReceivedEventHandler,
    SerialPinChangedEventHandler,
]
