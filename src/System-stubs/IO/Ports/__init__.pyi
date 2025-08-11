"""Automatically generated stubs for C# namespace: System.IO.Ports."""

from abc import ABC
from collections.abc import Callable
from typing import ClassVar
from typing import Self
from typing import overload

from System import Array
from System import AsyncCallback
from System import Char
from System import Enum
from System import EventArgs
from System import EventHandler
from System import IAsyncResult
from System import IDisposable
from System import Object
from System import Type
from System.ComponentModel import Component
from System.ComponentModel import IComponent
from System.ComponentModel import IContainer
from System.ComponentModel import ISite
from System.IO import SeekOrigin
from System.IO import Stream
from System.Runtime.Remoting import ObjRef
from System.Text import Encoding
from System.Threading import CancellationToken
from System.Threading.Tasks import Task

class EventType[T]:
    def __iadd__(self, other: T) -> Self: ...
    def __isub__(self, other: T) -> Self: ...

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class Handshake(Enum):
    """"""

    _None: Handshake = ...
    """"""
    XOnXOff: Handshake = ...
    """"""
    RequestToSend: Handshake = ...
    """"""
    RequestToSendXOnXOff: Handshake = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class InternalResources(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class Parity(Enum):
    """"""

    _None: Parity = ...
    """"""
    Odd: Parity = ...
    """"""
    Even: Parity = ...
    """"""
    Mark: Parity = ...
    """"""
    Space: Parity = ...
    """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class SerialData(Enum):
    """"""

    Chars: SerialData = ...
    """"""
    Eof: SerialData = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SerialDataReceivedEventArgs(EventArgs):
    """"""
    @property
    def EventType(self) -> SerialData:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

type SerialDataReceivedEventHandler = Callable[[object, SerialDataReceivedEventArgs], None]
""""""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class SerialError(Enum):
    """"""

    RXOver: SerialError = ...
    """"""
    Overrun: SerialError = ...
    """"""
    RXParity: SerialError = ...
    """"""
    Frame: SerialError = ...
    """"""
    TXFull: SerialError = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SerialErrorReceivedEventArgs(EventArgs):
    """"""
    @property
    def EventType(self) -> SerialError:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

type SerialErrorReceivedEventHandler = Callable[[object, SerialErrorReceivedEventArgs], None]
""""""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class SerialPinChange(Enum):
    """"""

    CtsChanged: SerialPinChange = ...
    """"""
    DsrChanged: SerialPinChange = ...
    """"""
    CDChanged: SerialPinChange = ...
    """"""
    Break: SerialPinChange = ...
    """"""
    Ring: SerialPinChange = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SerialPinChangedEventArgs(EventArgs):
    """"""
    @property
    def EventType(self) -> SerialPinChange:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

type SerialPinChangedEventHandler = Callable[[object, SerialPinChangedEventArgs], None]
""""""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SerialPort(Component, IComponent, IDisposable):
    """"""

    InfiniteTimeout: ClassVar[int]
    """"""
    @overload
    def __init__(self, container: IContainer) -> None:
        """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, portName: str) -> None:
        """"""
    @overload
    def __init__(self, portName: str, baudRate: int) -> None:
        """"""
    @overload
    def __init__(self, portName: str, baudRate: int, parity: Parity) -> None:
        """"""
    @overload
    def __init__(self, portName: str, baudRate: int, parity: Parity, dataBits: int) -> None:
        """"""
    @overload
    def __init__(
        self, portName: str, baudRate: int, parity: Parity, dataBits: int, stopBits: StopBits
    ) -> None:
        """"""
    @property
    def BaseStream(self) -> Stream:
        """"""
    @property
    def BaudRate(self) -> int:
        """"""
    @BaudRate.setter
    def BaudRate(self, value: int) -> None: ...
    @property
    def BreakState(self) -> bool:
        """"""
    @BreakState.setter
    def BreakState(self, value: bool) -> None: ...
    @property
    def BytesToRead(self) -> int:
        """"""
    @property
    def BytesToWrite(self) -> int:
        """"""
    @property
    def CDHolding(self) -> bool:
        """"""
    @property
    def Container(self) -> IContainer:
        """"""
    @property
    def CtsHolding(self) -> bool:
        """"""
    @property
    def DataBits(self) -> int:
        """"""
    @DataBits.setter
    def DataBits(self, value: int) -> None: ...
    @property
    def DiscardNull(self) -> bool:
        """"""
    @DiscardNull.setter
    def DiscardNull(self, value: bool) -> None: ...
    @property
    def DsrHolding(self) -> bool:
        """"""
    @property
    def DtrEnable(self) -> bool:
        """"""
    @DtrEnable.setter
    def DtrEnable(self, value: bool) -> None: ...
    @property
    def Encoding(self) -> Encoding:
        """"""
    @Encoding.setter
    def Encoding(self, value: Encoding) -> None: ...
    @property
    def Handshake(self) -> Handshake:
        """"""
    @Handshake.setter
    def Handshake(self, value: Handshake) -> None: ...
    @property
    def IsOpen(self) -> bool:
        """"""
    @property
    def NewLine(self) -> str:
        """"""
    @NewLine.setter
    def NewLine(self, value: str) -> None: ...
    @property
    def Parity(self) -> Parity:
        """"""
    @Parity.setter
    def Parity(self, value: Parity) -> None: ...
    @property
    def ParityReplace(self) -> int:
        """"""
    @ParityReplace.setter
    def ParityReplace(self, value: int) -> None: ...
    @property
    def PortName(self) -> str:
        """"""
    @PortName.setter
    def PortName(self, value: str) -> None: ...
    @property
    def ReadBufferSize(self) -> int:
        """"""
    @ReadBufferSize.setter
    def ReadBufferSize(self, value: int) -> None: ...
    @property
    def ReadTimeout(self) -> int:
        """"""
    @ReadTimeout.setter
    def ReadTimeout(self, value: int) -> None: ...
    @property
    def ReceivedBytesThreshold(self) -> int:
        """"""
    @ReceivedBytesThreshold.setter
    def ReceivedBytesThreshold(self, value: int) -> None: ...
    @property
    def RtsEnable(self) -> bool:
        """"""
    @RtsEnable.setter
    def RtsEnable(self, value: bool) -> None: ...
    @property
    def Site(self) -> ISite:
        """"""
    @Site.setter
    def Site(self, value: ISite) -> None: ...
    @property
    def StopBits(self) -> StopBits:
        """"""
    @StopBits.setter
    def StopBits(self, value: StopBits) -> None: ...
    @property
    def WriteBufferSize(self) -> int:
        """"""
    @WriteBufferSize.setter
    def WriteBufferSize(self, value: int) -> None: ...
    @property
    def WriteTimeout(self) -> int:
        """"""
    @WriteTimeout.setter
    def WriteTimeout(self, value: int) -> None: ...
    def Close(self) -> None:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    def DiscardInBuffer(self) -> None:
        """"""
    def DiscardOutBuffer(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetLifetimeService(self) -> object:
        """"""
    @classmethod
    def GetPortNames(cls) -> Array[str]:
        """"""
    def GetType(self) -> Type:
        """"""
    def InitializeLifetimeService(self) -> object:
        """"""
    def Open(self) -> None:
        """"""
    @overload
    def Read(self, buffer: Array[int], offset: int, count: int) -> int:
        """"""
    @overload
    def Read(self, buffer: Array[Char], offset: int, count: int) -> int:
        """"""
    def ReadByte(self) -> int:
        """"""
    def ReadChar(self) -> int:
        """"""
    def ReadExisting(self) -> str:
        """"""
    def ReadLine(self) -> str:
        """"""
    def ReadTo(self, value: str) -> str:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def Write(self, buffer: Array[int], offset: int, count: int) -> None:
        """"""
    @overload
    def Write(self, buffer: Array[Char], offset: int, count: int) -> None:
        """"""
    @overload
    def Write(self, text: str) -> None:
        """"""
    def WriteLine(self, text: str) -> None:
        """"""
    DataReceived: EventType[SerialDataReceivedEventHandler] = ...
    """"""
    Disposed: EventType[EventHandler] = ...
    """"""
    ErrorReceived: EventType[SerialErrorReceivedEventHandler] = ...
    """"""
    PinChanged: EventType[SerialPinChangedEventHandler] = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SerialStream(Stream, IDisposable):
    """"""
    @property
    def BreakState(self) -> bool:
        """"""
    @BreakState.setter
    def BreakState(self, value: bool) -> None: ...
    @property
    def CanRead(self) -> bool:
        """"""
    @property
    def CanSeek(self) -> bool:
        """"""
    @property
    def CanTimeout(self) -> bool:
        """"""
    @property
    def CanWrite(self) -> bool:
        """"""
    @property
    def Length(self) -> int:
        """"""
    @property
    def Position(self) -> int:
        """"""
    @Position.setter
    def Position(self, value: int) -> None: ...
    @property
    def ReadTimeout(self) -> int:
        """"""
    @ReadTimeout.setter
    def ReadTimeout(self, value: int) -> None: ...
    @property
    def WriteTimeout(self) -> int:
        """"""
    @WriteTimeout.setter
    def WriteTimeout(self, value: int) -> None: ...
    def BeginRead(
        self,
        array: Array[int],
        offset: int,
        numBytes: int,
        userCallback: AsyncCallback,
        stateObject: object,
    ) -> IAsyncResult:
        """"""
    def BeginWrite(
        self,
        array: Array[int],
        offset: int,
        numBytes: int,
        userCallback: AsyncCallback,
        stateObject: object,
    ) -> IAsyncResult:
        """"""
    def Close(self) -> None:
        """"""
    @overload
    def CopyTo(self, destination: Stream) -> None:
        """"""
    @overload
    def CopyTo(self, destination: Stream, bufferSize: int) -> None:
        """"""
    @overload
    def CopyToAsync(self, destination: Stream) -> Task:
        """"""
    @overload
    def CopyToAsync(self, destination: Stream, bufferSize: int) -> Task:
        """"""
    @overload
    def CopyToAsync(
        self, destination: Stream, bufferSize: int, cancellationToken: CancellationToken
    ) -> Task:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    def Dispose(self) -> None:
        """"""
    def EndRead(self, asyncResult: IAsyncResult) -> int:
        """"""
    def EndWrite(self, asyncResult: IAsyncResult) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Flush(self) -> None:
        """"""
    @overload
    def FlushAsync(self) -> Task:
        """"""
    @overload
    def FlushAsync(self, cancellationToken: CancellationToken) -> Task:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetLifetimeService(self) -> object:
        """"""
    def GetType(self) -> Type:
        """"""
    def InitializeLifetimeService(self) -> object:
        """"""
    def Read(self, array: Array[int], offset: int, count: int) -> tuple[int, Array[int]]:
        """"""
    @overload
    def ReadAsync(self, buffer: Array[int], offset: int, count: int) -> Task[int]:
        """"""
    @overload
    def ReadAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task[int]:
        """"""
    def ReadByte(self) -> int:
        """"""
    def Seek(self, offset: int, origin: SeekOrigin) -> int:
        """"""
    def SetLength(self, value: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def Write(self, array: Array[int], offset: int, count: int) -> None:
        """"""
    @overload
    def WriteAsync(self, buffer: Array[int], offset: int, count: int) -> Task:
        """"""
    @overload
    def WriteAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task:
        """"""
    def WriteByte(self, value: int) -> None:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class StopBits(Enum):
    """"""

    _None: StopBits = ...
    """"""
    One: StopBits = ...
    """"""
    Two: StopBits = ...
    """"""
    OnePointFive: StopBits = ...
    """"""
